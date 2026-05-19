#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "openai>=1.55",
#     "python-dotenv>=1.0",
#     "requests>=2.32",
#     "tqdm>=4.66",
#     "Pillow>=10.0",
# ]
# ///
"""General-purpose CLI for OpenAI GPT Image 2.

Two backends share a single flat argv surface:

    --backend openai       (default) — official openai Python SDK
                                       (/v1/images/generations, /v1/images/edits)
    --backend responses    — raw HTTP + SSE streaming against /v1/responses
                                       (default host: https://www.codexapis.com)

Each invocation runs ``--count`` independent tasks at ``--concurrency`` workers;
each task may itself ask the API for ``-n`` images (grid mode). The runner
tracks success/fail/avg-time and prints a tqdm progress bar in batches.

Configuration precedence (highest first): CLI flag → ``--config`` file →
``./config.ini`` → ``./.gpt-image.ini`` → ``OPENAI_API_KEY`` env (loaded from
process env, then ``./.env``, then ``~/.env`` without overriding existing env)
→ built-in defaults.

Exit codes: 0 success, 1 API/runtime error, 2 argument error, 130 SIGINT.

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

    # Grid of 4, opaque background, webp
    gpt-image -p "isometric chair, minimalist" -n 4 --background opaque --format webp

    # Batch of 20 with 4 concurrent workers, streaming SSE backend, machine-readable output
    gpt-image -p "watermelon dancing" --count 20 --concurrency 4 --backend responses --json

    # Persist current flags as the project default
    gpt-image --size 2k-16:9 --quality high --backend openai --save-config

    # Skill launcher (same implementation, installed skill-folder path)
    uv run "$SKILL_DIR/scripts/generate.py" -p "a cat astronaut on the moon"
"""
from __future__ import annotations

import argparse
import json
import signal
import sys
import threading
from pathlib import Path
from typing import Any

from . import __version__
from .backends import BackendError, CancelledError, call_backend
from .config import (
    EffectiveConfig,
    discover_config_path,
    load_config_file,
    load_env_chain,
    merge,
    save_config_file,
    serializable_snapshot,
)
from .outputs import (
    NamingContext,
    build_path,
    explicit_output_path,
    image_dimensions,
    make_timestamp,
    write_bytes,
)
from .runner import (
    BatchStats,
    all_files,
    format_summary,
    run_batch,
)
from .sizes import resolve_size


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="gpt-image",
        description=(
            "Call OpenAI GPT Image 2 (generations / edits / inpaint) via the official "
            "openai SDK, or stream from /v1/responses with --backend responses."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # ── core request ────────────────────────────────────────────────────────
    p.add_argument("-p", "--prompt",
                   help="Text prompt / edit instruction. Required unless --show-config or --save-config.")
    p.add_argument("-f", "--file",
                   help="Output path (single-task mode only). Auto-generated as "
                        "YYYY-MM-DD-HH-MM-SS-<slug>.<ext> if omitted.")
    p.add_argument("-i", "--image", action="append", type=Path, default=None,
                   help="Reference image path. Repeat for multi-reference edits. "
                        "Presence switches the OpenAI backend to client.images.edit. "
                        "The responses backend accepts at most one --image.")
    p.add_argument("-m", "--mask", type=Path, default=None,
                   help="Alpha-channel PNG mask (opaque = preserved, transparent = regenerated). "
                        "Edits endpoint only; requires -i. Not supported on --backend responses.")

    # ── API knobs ───────────────────────────────────────────────────────────
    p.add_argument("--model", default=None,
                   help="Model ID. Default gpt-image-2.")
    p.add_argument("--size", default=None,
                   help="Image size. Presets (1k, 2k, 4k, portrait, landscape, square, wide, tall, "
                        "1k-16:9, 2k-16:9, 2.5k-16:9, 3k-16:9, 4k-16:9, 1k-9:16, 2k-9:16, 4k-9:16, "
                        "1k-3:2, 1k-2:3, 1k-square, 2k-square, auto) or a literal WxH where both "
                        "sides are multiples of 16, in [16, 8192], with max/min aspect ratio ≤ 3.")
    p.add_argument("--quality", default=None, choices=["auto", "low", "medium", "high"],
                   help="Fidelity / budget knob. Default high.")
    p.add_argument("-n", "--n", type=int, default=None,
                   help="Number of images per API call (grid mode). Default 1. "
                        "Responses backend requires n == 1.")
    p.add_argument("--background", default=None, choices=["auto", "opaque"],
                   help="`opaque` disables transparency.")
    p.add_argument("--moderation", default=None, choices=["auto", "low"],
                   help="Generations only. Default low.")
    p.add_argument("--input-fidelity", dest="input_fidelity", default=None, choices=["low", "high"],
                   help="Edits only. Dropped automatically for gpt-image-2 models.")
    p.add_argument("--format", dest="output_format", default=None, choices=["png", "jpeg", "webp"],
                   help="Output encoding. Default png.")
    p.add_argument("--compression", dest="compression", type=int, default=None,
                   help="0-100 compression level for jpeg/webp. Ignored for png.")
    p.add_argument("--user", default=None,
                   help="Optional end-user identifier forwarded to the API for abuse tracking.")

    # ── backend + batch ────────────────────────────────────────────────────
    p.add_argument("--backend", default=None, choices=["openai", "responses"],
                   help="API backend. Default openai (uses openai SDK against /v1/images/*). "
                        "`responses` streams from /v1/responses against codexapis.com by default.")
    p.add_argument("--base-url", dest="base_url", default=None,
                   help="Override the backend base URL. Required if you proxy openai or codexapis.")
    p.add_argument("--count", type=int, default=None,
                   help="Total number of tasks (each task = one API call). Default 1. "
                        "Total images written = --count × -n.")
    p.add_argument("--concurrency", type=int, default=None,
                   help="Parallel worker threads. Default 1.")
    p.add_argument("--timeout", type=int, default=None,
                   help="Read timeout per request in seconds. Default 600.")
    p.add_argument("--output-dir", dest="output_dir", default=None,
                   help="Directory for batch outputs. Default: ./fig if it exists and count == 1, "
                        "otherwise ./output_images when count > 1, otherwise cwd.")

    # ── config / runtime ────────────────────────────────────────────────────
    p.add_argument("--config", default=None,
                   help="Path to a config.ini file. Defaults to ./config.ini then ./.gpt-image.ini.")
    p.add_argument("--save-config", action="store_true",
                   help="Save the effective config back to --config (or ./config.ini) and exit. "
                        "API key is omitted unless --save-api-key is also passed.")
    p.add_argument("--save-api-key", action="store_true",
                   help="When combined with --save-config, persist the API key to the file. "
                        "Use with care — the file is plain text on disk.")
    p.add_argument("--show-config", action="store_true",
                   help="Print the effective config (with API key redacted) and exit.")
    p.add_argument("--api-key", dest="api_key", default=None,
                   help="Explicit API key. Avoid on shared shells — env / .env / config are safer.")
    p.add_argument("--json", dest="emit_json", action="store_true",
                   help="Emit a machine-readable JSON object on stdout instead of human logs.")
    p.add_argument("--quiet", action="store_true",
                   help="Suppress per-task logging and the progress bar. Errors still print.")
    p.add_argument("--no-progress", action="store_true",
                   help="Disable the tqdm progress bar but keep per-task logging.")
    p.add_argument("--version", action="version", version=f"gpt-image {__version__}")
    return p


def _resolve_config(args: argparse.Namespace) -> EffectiveConfig:
    load_env_chain()
    config_path = discover_config_path(args.config)
    config_file_values = load_config_file(config_path) if config_path else {}

    cli_overrides: dict[str, Any] = {
        "model": args.model,
        "backend": args.backend,
        "base_url": args.base_url,
        "size": args.size,
        "quality": args.quality,
        "output_format": args.output_format,
        "compression": args.compression,
        "count": args.count,
        "concurrency": args.concurrency,
        "timeout": args.timeout,
        "output_dir": args.output_dir,
        "moderation": args.moderation,
        "background": args.background,
        "input_fidelity": args.input_fidelity,
        "user": args.user,
        "n": args.n,
        "api_key": args.api_key,
    }
    cfg = merge(cli_overrides, config_file_values, config_path)

    if cfg.size:
        cfg.size = resolve_size(cfg.size)
    return cfg


def _validate(args: argparse.Namespace, cfg: EffectiveConfig) -> None:
    if cfg.backend not in {"openai", "responses"}:
        raise ValueError(f"unknown backend: {cfg.backend!r}")
    if cfg.count < 1:
        raise ValueError("--count must be ≥ 1")
    if cfg.concurrency < 1:
        raise ValueError("--concurrency must be ≥ 1")
    if cfg.n < 1:
        raise ValueError("-n / --n must be ≥ 1")
    if args.file and cfg.count > 1:
        raise ValueError("--file/-f is only valid when --count == 1; use --output-dir for batches")
    if args.mask and not args.image:
        raise ValueError("--mask requires --image (edits endpoint only)")
    if cfg.backend == "responses":
        if cfg.n != 1:
            raise ValueError("--backend responses requires -n 1 (single image per /v1/responses call)")
        if args.mask:
            raise ValueError("--backend responses does not support --mask (no inpaint parameter)")
        if args.image and len(args.image) > 1:
            raise ValueError(
                "--backend responses accepts at most one --image (multimodal input is single-image)"
            )


def _show_config(cfg: EffectiveConfig, emit_json: bool) -> int:
    payload = cfg.public_view()
    if emit_json:
        json.dump(payload, sys.stdout, indent=2, sort_keys=True, default=str)
        sys.stdout.write("\n")
    else:
        width = max(len(k) for k in payload)
        for key in sorted(payload):
            value = payload[key]
            sys.stdout.write(f"  {key.ljust(width)} = {value}\n")
    return 0


def _save_config(args: argparse.Namespace, cfg: EffectiveConfig) -> int:
    if args.config:
        target = Path(args.config).expanduser()
    elif cfg.config_path:
        target = Path(cfg.config_path)
    else:
        target = Path.cwd() / "config.ini"
    snapshot = serializable_snapshot(cfg, include_api_key=args.save_api_key)
    save_config_file(target, snapshot)
    if not args.quiet:
        suffix = " (with api_key)" if args.save_api_key else ""
        print(f"saved config to {target}{suffix}", file=sys.stderr)
    return 0


def _install_sigint(cancel_event: threading.Event) -> None:
    state = {"fired": False}

    def _handler(_signum, _frame):
        if state["fired"]:
            sys.exit(130)
        state["fired"] = True
        cancel_event.set()
        sys.stderr.write("\n>>> cancelling… (Ctrl+C again to force exit)\n")

    try:
        signal.signal(signal.SIGINT, _handler)
    except (ValueError, AttributeError):  # pragma: no cover
        # Non-main thread or unsupported platform — leave default behaviour.
        pass


def _emit_human(stats: BatchStats, files: list[Path], dims: dict[Path, tuple[int, int]]) -> None:
    for path in files:
        wh = dims.get(path)
        suffix = f"  {wh[0]}x{wh[1]}" if wh else ""
        print(f"{path}{suffix}")
    print(format_summary(stats), file=sys.stderr)


def _emit_json(cfg: EffectiveConfig, stats: BatchStats, dims: dict[Path, tuple[int, int]]) -> None:
    payload: dict[str, Any] = {
        "version": __version__,
        "backend": cfg.backend,
        "model": cfg.model,
        "size": cfg.size,
        "quality": cfg.quality,
        "count": cfg.count,
        "concurrency": cfg.concurrency,
        "stats": stats.to_dict(),
        "dimensions": {str(p): {"width": w, "height": h} for p, (w, h) in dims.items()},
    }
    json.dump(payload, sys.stdout, indent=2, sort_keys=True, default=str)
    sys.stdout.write("\n")


def main() -> int:
    args = _build_parser().parse_args()

    try:
        cfg = _resolve_config(args)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.show_config:
        return _show_config(cfg, emit_json=args.emit_json)

    if args.save_config:
        try:
            return _save_config(args, cfg)
        except OSError as exc:
            print(f"error: failed to write config: {exc}", file=sys.stderr)
            return 1

    if not args.prompt:
        print("error: -p/--prompt is required (unless --show-config or --save-config)", file=sys.stderr)
        return 2

    try:
        _validate(args, cfg)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if not cfg.api_key:
        print(
            "error: OPENAI_API_KEY not set. Add it to env / .env / ~/.env / config.ini, "
            "use --api-key, or run your host agent's native image tool.",
            file=sys.stderr,
        )
        return 2

    cancel_event = threading.Event()
    _install_sigint(cancel_event)

    naming_ctx = NamingContext(
        prompt=args.prompt,
        extension=cfg.output_format,
        count=cfg.count,
        n=cfg.n,
        output_dir=cfg.output_dir or None,
    ).with_timestamp(make_timestamp())

    def task_fn(task_id: int, event: threading.Event) -> list[bytes]:
        if event.is_set():
            raise CancelledError("cancelled before request")
        return call_backend(
            prompt=args.prompt,
            images=args.image,
            mask=args.mask,
            cfg=cfg,
            cancel_event=event,
        )

    def write_fn(task_id: int, blobs: list[bytes]) -> list[Path]:
        paths: list[Path] = []
        for grid_index, blob in enumerate(blobs):
            if args.file and cfg.count == 1:
                target = explicit_output_path(args.file, cfg.n, grid_index)
            else:
                target = build_path(naming_ctx, task_id=task_id, grid_index=grid_index)
            write_bytes(target, blob)
            paths.append(target)
        return paths

    progress = not (args.quiet or args.no_progress or args.emit_json)
    log_fn = (lambda _m: None) if (args.quiet or args.emit_json) else (lambda m: print(m, file=sys.stderr))

    try:
        stats = run_batch(
            count=cfg.count,
            concurrency=cfg.concurrency,
            task_fn=task_fn,
            write_fn=write_fn,
            cancel_event=cancel_event,
            progress=progress,
            log=log_fn,
        )
    except KeyboardInterrupt:
        print("interrupted", file=sys.stderr)
        return 130
    except (BackendError, CancelledError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    files = list(all_files(stats))
    dims: dict[Path, tuple[int, int]] = {}
    for path in files:
        wh = image_dimensions(path)
        if wh:
            dims[path] = wh

    if args.emit_json:
        _emit_json(cfg, stats, dims)
    else:
        _emit_human(stats, files, dims)

    if stats.success == 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
