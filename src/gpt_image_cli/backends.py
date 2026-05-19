"""API backends for gpt-image.

Two backends share a single CLI surface:

- ``openai`` (default) — uses the official ``openai`` Python SDK against
  ``/v1/images/generations`` and ``/v1/images/edits``. Supports multi-reference
  edits, alpha-channel inpainting, and the full ``--n`` grid.
- ``responses`` — raw HTTP + SSE streaming against the ``/v1/responses``
  endpoint (default host ``https://www.codexapis.com``). Mirrors the bundled
  Tkinter UI's transport. ``-m`` (mask) and ``--n > 1`` are not supported by
  this endpoint and are rejected up front.

Both backends enforce the documented 4 MB input-image size cap before any
network call. Backends return raw image bytes; naming and disk writes happen
in :mod:`gpt_image_cli.outputs` so the runner can place files consistently.
"""
from __future__ import annotations

import base64
import json
import threading
import urllib.request
from pathlib import Path
from typing import Any

import requests
from openai import OpenAI

from .config import DEFAULT_RESPONSES_BASE_URL, EffectiveConfig

MAX_INPUT_BYTES = 4 * 1024 * 1024  # gpt-image-2 documented input cap.

_MIME_FOR_EXT = {
    "png": "image/png",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "webp": "image/webp",
    "gif": "image/gif",
}


class BackendError(RuntimeError):
    """Raised when a backend cannot fulfil a request (HTTP error, no image, …)."""


class CancelledError(RuntimeError):
    """Raised when a cancel event fires mid-stream."""


def _filter_none(d: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in d.items() if v is not None}


def _check_input_size(path: Path) -> None:
    size = path.stat().st_size
    if size > MAX_INPUT_BYTES:
        raise BackendError(
            f"input image {path} is {size / 1024 / 1024:.1f}MB; "
            f"gpt-image-2 requires ≤ {MAX_INPUT_BYTES // (1024 * 1024)}MB"
        )


def _model_rejects_input_fidelity(model: str) -> bool:
    return model.strip().lower().startswith("gpt-image-2")


# ── OpenAI SDK backend ──────────────────────────────────────────────────────


def _extract_bytes(item: Any) -> bytes:
    b64 = getattr(item, "b64_json", None)
    if b64:
        return base64.b64decode(b64)
    url = getattr(item, "url", None)
    if url:
        # OpenAI-owned host; urllib is fine here for the URL-mode response.
        with urllib.request.urlopen(url, timeout=300) as r:  # noqa: S310
            return r.read()
    raise BackendError("response item has neither b64_json nor url")


def call_openai_images(
    *,
    prompt: str,
    images: list[Path] | None,
    mask: Path | None,
    cfg: EffectiveConfig,
    cancel_event: threading.Event | None = None,
) -> list[bytes]:
    """Call ``client.images.generate`` or ``client.images.edit``.

    Returns the decoded bytes for each of the ``n`` images the API produced.
    Cancellation between tasks is handled at the runner layer; in-flight SDK
    calls cannot be interrupted by ``cancel_event`` on the OpenAI backend.
    """
    if mask and not images:
        raise BackendError("--mask requires --image (edits endpoint only)")
    if images:
        for p in images:
            if not p.is_file():
                raise BackendError(f"--image not found: {p}")
            _check_input_size(p)
    if mask:
        if not mask.is_file():
            raise BackendError(f"--mask not found: {mask}")
        _check_input_size(mask)

    client_kwargs: dict[str, Any] = {}
    if cfg.api_key:
        client_kwargs["api_key"] = cfg.api_key
    if cfg.base_url:
        client_kwargs["base_url"] = cfg.base_url
    if cfg.timeout:
        client_kwargs["timeout"] = float(cfg.timeout)
    client = OpenAI(**client_kwargs)

    common = _filter_none({
        "model": cfg.model,
        "prompt": prompt,
        "size": cfg.size,
        "quality": cfg.quality,
        "n": cfg.n,
        "background": cfg.background,
        "output_format": cfg.output_format,
        "output_compression": cfg.compression,
        "user": cfg.user,
    })

    if images:
        input_fidelity = cfg.input_fidelity
        if input_fidelity and _model_rejects_input_fidelity(cfg.model):
            input_fidelity = None
        image_handles = [p.open("rb") for p in images]
        mask_handle = mask.open("rb") if mask else None
        try:
            result = client.images.edit(**_filter_none({
                **common,
                "image": image_handles,
                "mask": mask_handle,
                "input_fidelity": input_fidelity,
            }))
        finally:
            for h in image_handles:
                h.close()
            if mask_handle:
                mask_handle.close()
    else:
        result = client.images.generate(**_filter_none({
            **common,
            "moderation": cfg.moderation,
        }))

    data = getattr(result, "data", None) or []
    if not data:
        raise BackendError("OpenAI API returned no image data")
    return [_extract_bytes(item) for item in data]


# ── Responses-streaming backend ─────────────────────────────────────────────


def _build_responses_input(prompt: str, image_path: Path | None) -> Any:
    if not image_path:
        return prompt
    _check_input_size(image_path)
    ext = image_path.suffix.lstrip(".").lower()
    mime = _MIME_FOR_EXT.get(ext, "image/png")
    encoded = base64.b64encode(image_path.read_bytes()).decode("ascii")
    return [{
        "role": "user",
        "content": [
            {"type": "input_image", "image_url": f"data:{mime};base64,{encoded}"},
            {"type": "input_text", "text": prompt},
        ],
    }]


def _build_responses_tool(cfg: EffectiveConfig) -> dict[str, Any]:
    tool: dict[str, Any] = {
        "type": "image_generation",
        "quality": cfg.quality,
        "output_format": cfg.output_format,
    }
    if cfg.size and cfg.size != "auto":
        tool["size"] = cfg.size
    if cfg.output_format in ("jpeg", "webp") and cfg.compression is not None:
        tool["output_compression"] = cfg.compression
    return tool


def call_responses_stream(
    *,
    prompt: str,
    images: list[Path] | None,
    mask: Path | None,
    cfg: EffectiveConfig,
    cancel_event: threading.Event | None = None,
) -> list[bytes]:
    """Call ``/v1/responses`` with streaming SSE; return a single decoded image.

    Constraints (validated up front so the user sees them before the network
    round-trip):

    - ``--n > 1`` is rejected — the responses image-generation tool returns
      exactly one image per call.
    - ``--mask`` is rejected — the tool has no mask parameter.
    - Multiple ``--image`` references are rejected — the multimodal input
      schema sends a single ``input_image`` block per turn.
    """
    if cfg.n != 1:
        raise BackendError("--backend responses does not support --n > 1 (single image per call)")
    if mask:
        raise BackendError("--backend responses does not support --mask (no inpaint param)")
    if images and len(images) > 1:
        raise BackendError(
            "--backend responses takes at most one --image; pass references through the prompt instead"
        )

    image_path = images[0] if images else None
    if image_path and not image_path.is_file():
        raise BackendError(f"--image not found: {image_path}")

    base = cfg.effective_base_url() or DEFAULT_RESPONSES_BASE_URL
    url = f"{base.rstrip('/')}/v1/responses"

    payload = {
        "model": cfg.model,
        "input": _build_responses_input(prompt, image_path),
        "tools": [_build_responses_tool(cfg)],
        "stream": True,
    }
    if cfg.user:
        payload["user"] = cfg.user

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {cfg.api_key}",
    }

    resp = requests.post(
        url,
        headers=headers,
        json=payload,
        stream=True,
        timeout=(10, cfg.timeout),
    )
    if resp.status_code != 200:
        body = (resp.text or "")[:300]
        resp.close()
        raise BackendError(f"HTTP {resp.status_code} from {url}: {body!r}")

    final_b64: str | None = None
    partial_b64: str | None = None  # fallback if `response.completed` never arrives
    try:
        for line in resp.iter_lines(decode_unicode=True):
            if cancel_event is not None and cancel_event.is_set():
                raise CancelledError("cancelled mid-stream")
            if not line or not line.startswith("data: "):
                continue
            payload_str = line[6:]
            if payload_str.strip() == "[DONE]":
                break
            try:
                evt = json.loads(payload_str)
            except json.JSONDecodeError:
                continue

            evt_type = evt.get("type", "")
            if evt_type == "response.image_generation_call.partial_image":
                b64 = evt.get("partial_image_b64") or ""
                if b64:
                    partial_b64 = b64  # keep latest as fallback, do not exit early
            elif evt_type == "response.completed":
                response_obj = evt.get("response", {}) or {}
                for out in response_obj.get("output", []) or []:
                    if out.get("type") == "image_generation_call":
                        result = out.get("result", "")
                        if result:
                            final_b64 = result
                            break
                break  # response.completed terminates the stream
    finally:
        resp.close()

    chosen = final_b64 or partial_b64
    if not chosen:
        raise BackendError("/v1/responses stream contained no image data")
    return [base64.b64decode(chosen)]


# ── Dispatcher ──────────────────────────────────────────────────────────────


def call_backend(
    *,
    prompt: str,
    images: list[Path] | None,
    mask: Path | None,
    cfg: EffectiveConfig,
    cancel_event: threading.Event | None = None,
) -> list[bytes]:
    """Route to the configured backend."""
    if cfg.backend == "openai":
        return call_openai_images(
            prompt=prompt, images=images, mask=mask, cfg=cfg, cancel_event=cancel_event,
        )
    if cfg.backend == "responses":
        return call_responses_stream(
            prompt=prompt, images=images, mask=mask, cfg=cfg, cancel_event=cancel_event,
        )
    raise BackendError(f"unknown backend: {cfg.backend!r}")
