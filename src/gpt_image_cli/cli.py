#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "openai>=1.55",
#     "python-dotenv>=1.0",
# ]
# ///
"""General-purpose CLI for OpenAI GPT Image 2.

Mirrors the two official endpoints from the OpenAI cookbook using the official
`openai` Python SDK:

    client.images.generate(...)   — text → image          (no  -i)
    client.images.edit(...)       — text + image(s) → image (with -i; mask via -m)

Every documented parameter is exposed as a flag. Reads OPENAI_API_KEY from
process env, then .env, then ~/.env without overriding existing env. The
optional Atlas Cloud text-to-image provider reads ATLASCLOUD_API_KEY or
ATLAS_CLOUD_API_KEY and uses Atlas Cloud's async media API. Writes the returned
PNG/JPEG/WebP bytes to disk and prints the output path(s) on stdout.

Exit codes: 0 success, 1 API error, 2 bad args.

Examples:
    # Basic generate, auto filename, 1K square
    gpt-image -p "a cat astronaut on the moon"

    # Named output, portrait 2K, high quality
    gpt-image -p "Chinese tea poster" -f poster.png --size 2k --quality high

    # Edit existing image (colorize, restyle, translate text, etc.)
    gpt-image -p "colorize this manga page" -i page.jpg -f colored.png

    # Multi-reference edit (outfit transfer, pet + brand, etc.)
    gpt-image -p "77 × KFC collab poster" -i cat.png -i kfc_logo.png -f collab.png

    # Alpha-channel inpaint (mask opaque = keep, transparent = regenerate)
    gpt-image -p "replace sky with aurora" -i photo.jpg -m sky_mask.png -f aurora.png

    # Grid of 4, transparent background, webp
    gpt-image -p "isometric chair, minimalist" -n 4 --background opaque --format webp

    # Skill launcher (same implementation, installed skill-folder path)
    uv run "$SKILL_DIR/scripts/generate.py" -p "a cat astronaut on the moon"
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from openai import APIError, OpenAI


def _load_env_chain() -> None:
    """Resolve OPENAI_API_KEY without overriding runtime-provided env.

    Order: process env → ./.env → ~/.env. Existing process env wins so
    hosted agents or explicit shell exports are not replaced by local files.
    """
    load_dotenv(Path.cwd() / ".env", override=False)
    load_dotenv(Path.home() / ".env", override=False)


SIZE_SHORTCUTS: dict[str, str] = {
    "1k": "1024x1024",
    "2k": "2048x2048",
    "4k": "3840x2160",
    "portrait": "1024x1536",
    "landscape": "1536x1024",
    "square": "1024x1024",
    "wide": "2048x1152",
    "tall": "2160x3840",
}

DEFAULT_MODEL = "gpt-image-2"
ATLAS_CLOUD_DEFAULT_MODEL = "openai/gpt-image-2/text-to-image"
ATLAS_CLOUD_API_BASE = "https://api.atlascloud.ai/api/v1"
DEFAULT_SIZE = "1024x1024"
DEFAULT_MODERATION = "low"
POLL_INTERVAL_SECONDS = 3.0
POLL_TIMEOUT_SECONDS = 300.0


def slugify(text: str, max_len: int = 30) -> str:
    s = re.sub(r"[^\w\s-]", "", text.lower()).strip()
    s = re.sub(r"[-\s]+", "-", s)[:max_len]
    return s or "image"


def default_output_path(prompt: str, extension: str) -> Path:
    cwd = Path.cwd()
    target_dir = cwd / "fig" if (cwd / "fig").is_dir() else cwd
    stamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    return target_dir / f"{stamp}-{slugify(prompt)}.{extension}"


def resolve_size(value: str) -> str:
    return SIZE_SHORTCUTS.get(value.lower(), value)


def model_rejects_input_fidelity(model: str) -> bool:
    return model.strip().lower().startswith("gpt-image-2")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="gpt-image",
        description="Call OpenAI GPT Image 2 (generations or edits) via the official openai Python SDK.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("-p", "--prompt", required=True, help="Text prompt / edit instruction.")
    p.add_argument(
        "--provider",
        default="openai",
        choices=["openai", "atlascloud"],
        help="Image generation provider. Default openai. atlascloud currently supports text-to-image generation.",
    )
    p.add_argument(
        "-f", "--file",
        help="Output path. Auto-generated as YYYY-MM-DD-HH-MM-SS-<slug>.<ext> if omitted "
             "(written to ./fig/ if that dir exists, else ./).",
    )
    p.add_argument(
        "-i", "--image", action="append", type=Path, default=None,
        help="Reference image path. Repeat flag for multi-reference edits. "
             "Presence of any -i switches endpoint to client.images.edit().",
    )
    p.add_argument(
        "-m", "--mask", type=Path, default=None,
        help="Alpha-channel PNG mask (opaque = preserved, transparent = regenerated). "
             "Edits endpoint only; requires -i.",
    )
    p.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Model ID. Defaults to {DEFAULT_MODEL} for openai and {ATLAS_CLOUD_DEFAULT_MODEL} for atlascloud.",
    )
    p.add_argument(
        "--size", default=DEFAULT_SIZE,
        help="Image size. Accepts literals (1024x1024, 1536x1024, 2048x2048, 3840x2160, "
             "any 16px-multiple up to 3840 max edge, 3:1 ratio cap) or shortcuts "
             "(1k, 2k, 4k, portrait, landscape, square, wide, tall). Default 1024x1024.",
    )
    p.add_argument(
        "--quality", default="high", choices=["auto", "low", "medium", "high"],
        help="Rendering fidelity / budget knob (cost scales ~10× per step). Default high. "
        "Use low for cheap drafts, medium for normal exploration, high for final text-heavy or shipping-facing assets.",
    )
    p.add_argument("-n", "--n", type=int, default=1, help="Number of images to return. Default 1.")
    p.add_argument(
        "--background", default=None, choices=["auto", "opaque"],
        help="`opaque` disables transparency. Default API-side auto.",
    )
    p.add_argument(
        "--moderation", default=DEFAULT_MODERATION, choices=["auto", "low"],
        help="Generations only. Default low. Use `auto` if you want the stricter API-side default.",
    )
    p.add_argument(
        "--input-fidelity", dest="input_fidelity", default=None, choices=["low", "high"],
        help="Edits only. gpt-image-2 rejects this parameter, so the CLI drops it locally before calling the API.",
    )
    p.add_argument(
        "--format", dest="output_format", default=None,
        choices=["png", "jpeg", "webp"],
        help="Output encoding. Default png.",
    )
    p.add_argument(
        "--compression", dest="output_compression", type=int, default=None,
        help="0-100 compression level for jpeg/webp. Ignored for png.",
    )
    p.add_argument(
        "--user", default=None,
        help="Optional end-user identifier forwarded to OpenAI for abuse tracking.",
    )
    p.add_argument(
        "--atlas-poll-interval",
        type=float,
        default=POLL_INTERVAL_SECONDS,
        help=f"Seconds between Atlas Cloud prediction polls. Default {POLL_INTERVAL_SECONDS:g}.",
    )
    p.add_argument(
        "--atlas-timeout",
        type=float,
        default=POLL_TIMEOUT_SECONDS,
        help=f"Maximum seconds to wait for an Atlas Cloud prediction. Default {POLL_TIMEOUT_SECONDS:g}.",
    )
    return p.parse_args()


def _filter_none(d: dict[str, Any]) -> dict[str, Any]:
    """Drop keys whose value is None — SDK treats missing vs None differently."""
    return {k: v for k, v in d.items() if v is not None}


def call_generate(client: OpenAI, args: argparse.Namespace) -> Any:
    return client.images.generate(**_filter_none({
        "model": args.model,
        "prompt": args.prompt,
        "size": resolve_size(args.size),
        "quality": args.quality,
        "n": args.n,
        "background": args.background,
        "moderation": args.moderation,
        "output_format": args.output_format,
        "output_compression": args.output_compression,
        "user": args.user,
    }))


def call_edit(client: OpenAI, args: argparse.Namespace) -> Any:
    for p in args.image:
        if not p.is_file():
            print(f"error: --image not found: {p}", file=sys.stderr)
            sys.exit(2)
    if args.mask and not args.mask.is_file():
        print(f"error: --mask not found: {args.mask}", file=sys.stderr)
        sys.exit(2)

    input_fidelity = args.input_fidelity
    if input_fidelity and model_rejects_input_fidelity(args.model):
        print(
            "note: dropping --input-fidelity because gpt-image-2 rejects that parameter.",
            file=sys.stderr,
        )
        input_fidelity = None

    image_handles = [p.open("rb") for p in args.image]
    mask_handle = args.mask.open("rb") if args.mask else None
    try:
        return client.images.edit(**_filter_none({
            "model": args.model,
            "image": image_handles,
            "mask": mask_handle,
            "prompt": args.prompt,
            "size": resolve_size(args.size),
            "quality": args.quality,
            "n": args.n,
            "background": args.background,
            "input_fidelity": input_fidelity,
            "output_format": args.output_format,
            "output_compression": args.output_compression,
            "user": args.user,
        }))
    finally:
        for h in image_handles:
            h.close()
        if mask_handle:
            mask_handle.close()


def _atlascloud_api_key() -> str:
    return os.environ.get("ATLASCLOUD_API_KEY") or os.environ.get("ATLAS_CLOUD_API_KEY") or ""


def _atlascloud_model(args: argparse.Namespace) -> str:
    if args.model == DEFAULT_MODEL:
        return ATLAS_CLOUD_DEFAULT_MODEL
    return args.model


def _atlascloud_request(method: str, path: str, api_key: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    req = urllib.request.Request(
        f"{ATLAS_CLOUD_API_BASE}{path}",
        data=body,
        headers=headers,
        method=method,
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as response:  # noqa: S310 - configured Atlas Cloud API host
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Atlas Cloud API error {exc.code}: {error_body}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Atlas Cloud API request failed: {exc}") from exc


def _prediction_payload(response: dict[str, Any]) -> dict[str, Any]:
    data = response.get("data")
    return data if isinstance(data, dict) else response


def _prediction_id(response: dict[str, Any]) -> str:
    payload = _prediction_payload(response)
    value = payload.get("id") or payload.get("prediction_id")
    return str(value or "")


def _prediction_outputs(payload: dict[str, Any]) -> list[Any]:
    for key in ("outputs", "output", "result", "images", "urls"):
        value = payload.get(key)
        if isinstance(value, list):
            return value
        if value:
            return [value]
    return []


def call_atlascloud_generate(args: argparse.Namespace) -> list[Any]:
    if args.image:
        print(
            "error: --provider atlascloud currently supports text-to-image only; omit --image/--mask.",
            file=sys.stderr,
        )
        sys.exit(2)
    if args.n != 1:
        print("error: --provider atlascloud currently supports one image per request; keep --n 1.", file=sys.stderr)
        sys.exit(2)
    if args.output_format == "webp":
        print("error: --provider atlascloud supports png or jpeg output for this model, not webp.", file=sys.stderr)
        sys.exit(2)
    if args.background is not None:
        print("error: --background is not supported by --provider atlascloud for this model.", file=sys.stderr)
        sys.exit(2)
    if args.output_compression is not None:
        print("error: --compression is not supported by --provider atlascloud for this model.", file=sys.stderr)
        sys.exit(2)
    if args.input_fidelity is not None:
        print("error: --input-fidelity is only valid for edit-capable OpenAI models.", file=sys.stderr)
        sys.exit(2)
    if args.user is not None:
        print("error: --user is only forwarded for the OpenAI provider.", file=sys.stderr)
        sys.exit(2)

    api_key = _atlascloud_api_key()
    if not api_key:
        print("error: ATLASCLOUD_API_KEY not set. Add it to env, or use --provider openai.", file=sys.stderr)
        sys.exit(2)

    output_format = args.output_format or "png"
    body = _filter_none(
        {
            "model": _atlascloud_model(args),
            "prompt": args.prompt,
            "size": resolve_size(args.size),
            "quality": None if args.quality == "auto" else args.quality,
            "output_format": output_format,
            "moderation": args.moderation,
        }
    )
    submitted = _atlascloud_request("POST", "/model/generateImage", api_key, body)
    prediction_id = _prediction_id(submitted)
    if not prediction_id:
        raise RuntimeError(f"Atlas Cloud response did not include a prediction id: {submitted}")

    deadline = time.monotonic() + max(1.0, args.atlas_timeout)
    interval = max(1.0, args.atlas_poll_interval)
    while time.monotonic() < deadline:
        current = _prediction_payload(_atlascloud_request("GET", f"/model/prediction/{prediction_id}", api_key))
        status = str(current.get("status") or "").lower()
        if status in {"completed", "succeeded", "success"}:
            outputs = _prediction_outputs(current)
            if outputs:
                return outputs
            raise RuntimeError(f"Atlas Cloud prediction completed without outputs: {current}")
        if status in {"failed", "error", "canceled", "cancelled"}:
            raise RuntimeError(f"Atlas Cloud prediction failed: {current}")
        time.sleep(interval)

    raise RuntimeError(f"Atlas Cloud prediction timed out after {args.atlas_timeout:g}s: {prediction_id}")


def write_outputs(data: list[Any], out_path: Path, n: int) -> list[Path]:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for i, item in enumerate(data):
        b64 = getattr(item, "b64_json", None)
        url = getattr(item, "url", None)
        if b64:
            raw = base64.b64decode(b64)
        elif url:
            with urllib.request.urlopen(url, timeout=300) as r:  # noqa: S310 — OpenAI-owned host
                raw = r.read()
        else:
            print(f"error: response item {i} has neither b64_json nor url", file=sys.stderr)
            sys.exit(1)

        if n == 1:
            target = out_path
        else:
            stem = out_path.with_suffix("")
            target = stem.parent / f"{stem.name}_{i}{out_path.suffix}"
        target.write_bytes(raw)
        written.append(target)
    return written


def _bytes_from_output(item: Any) -> bytes:
    if isinstance(item, str):
        if item.startswith("data:") and "," in item:
            return base64.b64decode(item.split(",", 1)[1])
        if item.startswith(("http://", "https://")):
            with urllib.request.urlopen(item, timeout=300) as response:  # noqa: S310 - model output URL
                return response.read()
        return base64.b64decode(item)
    if isinstance(item, dict):
        for key in ("url", "download_url", "image_url"):
            value = item.get(key)
            if isinstance(value, str) and value:
                return _bytes_from_output(value)
        for key in ("b64_json", "base64", "data"):
            value = item.get(key)
            if isinstance(value, str) and value:
                return _bytes_from_output(value)
    raise ValueError(f"unsupported image output item: {item!r}")


def write_atlascloud_outputs(data: list[Any], out_path: Path) -> list[Path]:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for i, item in enumerate(data):
        if len(data) == 1:
            target = out_path
        else:
            stem = out_path.with_suffix("")
            target = stem.parent / f"{stem.name}_{i}{out_path.suffix}"
        target.write_bytes(_bytes_from_output(item))
        written.append(target)
    return written


def main() -> int:
    args = parse_args()

    _load_env_chain()
    if args.provider == "openai" and not os.environ.get("OPENAI_API_KEY"):
        print(
            "error: OPENAI_API_KEY not set. Add it to env / .env / ~/.env, or use your host agent's native image tool.",
            file=sys.stderr,
        )
        return 2

    if args.mask and not args.image:
        print("error: --mask requires --image (edits endpoint only)", file=sys.stderr)
        return 2

    ext = args.output_format or "png"
    out_path = Path(args.file).expanduser().resolve() if args.file else default_output_path(args.prompt, ext)

    if args.provider == "atlascloud":
        try:
            outputs = call_atlascloud_generate(args)
        except RuntimeError as e:
            print(f"error: {e}", file=sys.stderr)
            return 1
        try:
            written = write_atlascloud_outputs(outputs, out_path)
        except (OSError, ValueError, urllib.error.URLError) as e:
            print(f"error: failed to write Atlas Cloud output: {e}", file=sys.stderr)
            return 1
        for p in written:
            print(p)
        return 0

    client = OpenAI()  # auto-reads OPENAI_API_KEY

    try:
        result = call_edit(client, args) if args.image else call_generate(client, args)
    except APIError as e:
        print(f"error: {type(e).__name__}: {e}", file=sys.stderr)
        return 1

    data = result.data or []
    if not data:
        print(f"error: no image data in response: {result}", file=sys.stderr)
        return 1

    for p in write_outputs(data, out_path, args.n):
        print(p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
