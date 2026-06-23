#!/usr/bin/env python3
"""Atlas Cloud backend for the gpt-image CLI.

Atlas Cloud (https://www.atlascloud.ai) serves OpenAI GPT Image 2 through its
own **asynchronous** media API (submit task -> poll result), not the
OpenAI-compatible synchronous `/v1/images/{generations,edits}` shape. So this
module talks to that async API directly and returns a tiny result object that
mimics the part of the OpenAI SDK response the CLI consumes (``result.data`` is
a list of items, each exposing ``.url`` / ``.b64_json``). That lets the rest of
``cli.py`` — argument parsing, ``write_outputs`` — stay completely unchanged.

Enable it by exporting ``GPT_IMAGE_BACKEND=atlas`` (or passing ``--backend
atlas``) together with ``ATLASCLOUD_API_KEY``. The default OpenAI path is
untouched when neither is set.

Endpoints (https://api.atlascloud.ai/api/v1/model):
    POST /generateImage              — text -> image and image edit
    GET  /prediction/{id}            — poll until status == completed

Model mapping (the CLI's ``gpt-image-2`` -> Atlas model ids):
    text -> image : openai/gpt-image-2/text-to-image
    edit          : openai/gpt-image-2/edit
"""
from __future__ import annotations

import base64
import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ATLAS_API_BASE = os.environ.get(
    "ATLASCLOUD_API_BASE", "https://api.atlascloud.ai/api/v1/model"
).rstrip("/")

# CLI model id -> Atlas model ids per endpoint.
_ATLAS_MODEL_MAP: dict[str, dict[str, str]] = {
    "gpt-image-2": {
        "generate": "openai/gpt-image-2/text-to-image",
        "edit": "openai/gpt-image-2/edit",
    },
}

_POLL_INTERVAL_SECONDS = 4
_POLL_TIMEOUT_SECONDS = 300


class AtlasError(RuntimeError):
    """Raised when the Atlas Cloud API returns an error or times out."""


class _Item:
    """Mimics one entry of OpenAI ``response.data`` (``.url`` / ``.b64_json``)."""

    def __init__(self, url: str | None = None, b64_json: str | None = None) -> None:
        self.url = url
        self.b64_json = b64_json


class _Result:
    """Mimics the OpenAI image response object consumed by ``write_outputs``."""

    def __init__(self, data: list[_Item]) -> None:
        self.data = data


def atlas_api_key() -> str | None:
    return os.environ.get("ATLASCLOUD_API_KEY") or os.environ.get("ATLAS_CLOUD_API_KEY")


def resolve_model(cli_model: str, endpoint: str) -> str:
    """Map a CLI model id to the Atlas model id for the given endpoint.

    If the caller already passes a full Atlas model id (``openai/...``), it is
    used verbatim so power users can target any Atlas image model.
    """
    if "/" in cli_model:
        return cli_model
    mapping = _ATLAS_MODEL_MAP.get(cli_model.strip().lower())
    if mapping and endpoint in mapping:
        return mapping[endpoint]
    raise AtlasError(
        f"no Atlas model mapping for '{cli_model}' ({endpoint}); "
        f"pass a full Atlas model id such as 'openai/gpt-image-2/text-to-image'"
    )


def _request(url: str, *, method: str, api_key: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
    body = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=body, method=method)
    req.add_header("Authorization", f"Bearer {api_key}")
    req.add_header("Content-Type", "application/json")
    # Atlas sits behind a CDN that rejects the default urllib UA.
    req.add_header("User-Agent", "gpt-image-cli (+https://github.com/wuyoscar/gpt_image_2_skill)")
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:  # noqa: S310 — Atlas-owned host
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:  # surface the API error body
        detail = e.read().decode(errors="replace")
        raise AtlasError(f"HTTP {e.code} from Atlas: {detail}") from e
    except urllib.error.URLError as e:
        raise AtlasError(f"could not reach Atlas Cloud: {e}") from e


def _file_to_data_uri(path: Path) -> str:
    raw = path.read_bytes()
    suffix = path.suffix.lstrip(".").lower() or "png"
    mime = "jpeg" if suffix in {"jpg", "jpeg"} else suffix
    return f"data:image/{mime};base64,{base64.b64encode(raw).decode()}"


def _submit(api_key: str, model: str, payload: dict[str, Any], *, edit: bool) -> str:
    endpoint = f"{ATLAS_API_BASE}/generateImage"
    data = _request(endpoint, method="POST", api_key=api_key, payload=payload)
    if data.get("code") != 200:
        raise AtlasError(f"submit failed: {data.get('msg') or data.get('message') or data}")
    pred_id = (data.get("data") or {}).get("id")
    if not pred_id:
        raise AtlasError(f"submit returned no prediction id: {data}")
    return pred_id


def _poll(api_key: str, pred_id: str) -> list[str]:
    url = f"{ATLAS_API_BASE}/prediction/{pred_id}"
    deadline = time.monotonic() + _POLL_TIMEOUT_SECONDS
    while True:
        data = _request(url, method="GET", api_key=api_key)
        node = data.get("data") or {}
        status = node.get("status")
        if status == "completed":
            outputs = node.get("outputs") or []
            if not outputs:
                raise AtlasError(f"completed but no outputs: {data}")
            return outputs
        if status == "failed":
            raise AtlasError(f"generation failed: {node.get('error') or data}")
        if time.monotonic() >= deadline:
            raise AtlasError(f"timed out after {_POLL_TIMEOUT_SECONDS}s (last status={status})")
        time.sleep(_POLL_INTERVAL_SECONDS)


def generate(*, api_key: str, model: str, prompt: str, size: str, n: int) -> _Result:
    atlas_model = resolve_model(model, "generate")
    payload: dict[str, Any] = {"model": atlas_model, "prompt": prompt}
    # Atlas's gpt-image-2 expects size as WxH (e.g. 1024x1024), like OpenAI.
    if size:
        payload["size"] = size
    if n and n > 1:
        payload["num_images"] = n
    pred_id = _submit(api_key, atlas_model, payload, edit=False)
    urls = _poll(api_key, pred_id)
    return _Result([_Item(url=u) for u in urls])


def edit(*, api_key: str, model: str, prompt: str, size: str, n: int, images: list[Path]) -> _Result:
    atlas_model = resolve_model(model, "edit")
    # Atlas takes input images via the `images` field; multiple are newline-separated.
    images_field = "\n".join(_file_to_data_uri(p) for p in images)
    payload: dict[str, Any] = {"model": atlas_model, "prompt": prompt, "images": images_field}
    if size:
        payload["size"] = size
    if n and n > 1:
        payload["num_images"] = n
    pred_id = _submit(api_key, atlas_model, payload, edit=True)
    urls = _poll(api_key, pred_id)
    return _Result([_Item(url=u) for u in urls])
