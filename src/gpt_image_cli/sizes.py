"""Size presets and custom-size validation for gpt-image.

Combines the legacy 8-shortcut table from the original CLI with the 14-preset
table the bundled Tkinter UI (`生图代码.py`) exposes. Custom WxH values are
validated against gpt-image-2's documented constraints: both dimensions are
multiples of 16, in [16, 8192], and the aspect ratio max/min is at most 3:1.
"""
from __future__ import annotations

import re

SIZE_PRESETS: dict[str, str] = {
    # Legacy shortcuts (must keep — backward compatible with v0.2.x).
    "1k": "1024x1024",
    "2k": "2048x2048",
    "4k": "3840x2160",
    "portrait": "1024x1536",
    "landscape": "1536x1024",
    "square": "1024x1024",
    "wide": "2048x1152",
    "tall": "2160x3840",
    # Square presets (mirror Tkinter UI labels).
    "1k-square": "1024x1024",
    "2k-square": "2048x2048",
    # 16:9 landscape ladder.
    "1k-16:9": "1792x1008",
    "2k-16:9": "2048x1152",
    "2.5k-16:9": "2560x1440",
    "3k-16:9": "3072x1728",
    "4k-16:9": "3840x2160",
    # 9:16 portrait ladder.
    "1k-9:16": "1008x1792",
    "2k-9:16": "1152x2048",
    "4k-9:16": "2160x3840",
    # 3:2 / 2:3 photography aspect.
    "1k-3:2": "1536x1024",
    "1k-2:3": "1024x1536",
    # Defer to model's automatic aspect inference.
    "auto": "auto",
}

_LITERAL = re.compile(r"^\s*(\d+)\s*[xX×]\s*(\d+)\s*$")

MIN_DIM = 16
MAX_DIM = 8192
MAX_RATIO = 3.0


def list_presets() -> list[str]:
    return list(SIZE_PRESETS.keys())


def resolve_size(value: str) -> str:
    """Map shortcut to literal WxH, validate custom WxH, or pass `auto` through.

    Raises ValueError with a precise reason when a custom spec violates the
    16-multiple, dimension-range, or aspect-ratio rules.
    """
    if value is None:
        raise ValueError("size is required")
    key = value.strip().lower()
    if key in SIZE_PRESETS:
        return SIZE_PRESETS[key]
    return validate_custom_size(value)


def validate_custom_size(spec: str) -> str:
    """Return a canonical `WxH` string if `spec` satisfies gpt-image-2 rules."""
    m = _LITERAL.match(spec)
    if not m:
        raise ValueError(
            f"invalid size {spec!r}: use a preset ({', '.join(list_presets()[:6])}, ...) "
            f"or a literal like 1536x1024"
        )
    w, h = int(m.group(1)), int(m.group(2))
    if w < MIN_DIM or h < MIN_DIM:
        raise ValueError(f"size {w}x{h}: both sides must be ≥ {MIN_DIM}")
    if w > MAX_DIM or h > MAX_DIM:
        raise ValueError(f"size {w}x{h}: both sides must be ≤ {MAX_DIM}")
    if w % 16 != 0 or h % 16 != 0:
        raise ValueError(f"size {w}x{h}: both sides must be multiples of 16")
    long_side, short_side = max(w, h), min(w, h)
    if long_side / short_side > MAX_RATIO:
        raise ValueError(
            f"size {w}x{h}: aspect ratio {long_side / short_side:.2f}:1 exceeds {MAX_RATIO:.0f}:1 cap"
        )
    return f"{w}x{h}"
