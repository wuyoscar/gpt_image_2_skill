"""Output file naming, disk writes, and optional PIL dimension reporting.

Filename matrix (``count`` = total tasks, ``n`` = grid size per API call)::

    count=1 n=1  →  {YYYY-MM-DD-HH-MM-SS}-{slug}.{ext}
    count=1 n>1  →  {YYYY-MM-DD-HH-MM-SS}-{slug}_{i}.{ext}
    count>1 n=1  →  {YYYY-MM-DD-HH-MM-SS}-{slug}_{tid:03d}.{ext}
    count>1 n>1  →  {YYYY-MM-DD-HH-MM-SS}-{slug}_{tid:03d}_{i}.{ext}

Output directory:
- ``--output-dir`` wins if set
- otherwise ``./fig/`` if it exists (legacy v0.2.x behaviour) and count == 1
- otherwise ``./output_images/`` (matches bundled Tkinter UI) when count > 1
- otherwise cwd
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

try:  # Pillow is optional — dimension reporting is a polish, not a requirement.
    from PIL import Image as _PILImage  # type: ignore[import-not-found]
    _HAS_PIL = True
except ImportError:  # pragma: no cover — depends on install profile
    _HAS_PIL = False


@dataclass(frozen=True)
class NamingContext:
    prompt: str
    extension: str
    count: int
    n: int
    output_dir: str | None
    timestamp: str = ""  # populated lazily so all files in a batch share it

    def with_timestamp(self, stamp: str) -> "NamingContext":
        return NamingContext(
            prompt=self.prompt,
            extension=self.extension,
            count=self.count,
            n=self.n,
            output_dir=self.output_dir,
            timestamp=stamp,
        )


def slugify(text: str, max_len: int = 30) -> str:
    s = re.sub(r"[^\w\s-]", "", text.lower()).strip()
    s = re.sub(r"[-\s]+", "-", s)[:max_len]
    return s or "image"


def make_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d-%H-%M-%S")


def resolve_output_dir(output_dir: str | None, count: int) -> Path:
    """Pick the directory for batch / single output, with legacy fallback."""
    if output_dir:
        return Path(output_dir).expanduser()
    cwd = Path.cwd()
    if count == 1:
        legacy_fig = cwd / "fig"
        return legacy_fig if legacy_fig.is_dir() else cwd
    return cwd / "output_images"


def build_path(
    ctx: NamingContext,
    task_id: int = 0,
    grid_index: int = 0,
) -> Path:
    """Return the path for a specific (task_id, grid_index) write."""
    out_dir = resolve_output_dir(ctx.output_dir, ctx.count)
    stamp = ctx.timestamp or make_timestamp()
    slug = slugify(ctx.prompt)
    parts = [stamp, "-", slug]
    if ctx.count > 1:
        parts.append(f"_{task_id:03d}")
    if ctx.n > 1:
        parts.append(f"_{grid_index}")
    name = "".join(parts) + f".{ctx.extension}"
    return out_dir / name


def explicit_output_path(file_arg: str, n: int, grid_index: int = 0) -> Path:
    """Return the path when ``-f/--file`` is set explicitly.

    For ``n > 1`` we follow the existing v0.2.x behaviour and suffix the index
    before the extension: ``poster.png`` → ``poster_0.png``, ``poster_1.png``…
    """
    base = Path(file_arg).expanduser().resolve()
    if n == 1:
        return base
    stem = base.with_suffix("")
    return stem.parent / f"{stem.name}_{grid_index}{base.suffix}"


def write_bytes(path: Path, data: bytes) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return path


def image_dimensions(path: Path) -> tuple[int, int] | None:
    """Return ``(width, height)`` if Pillow is available and can read the file."""
    if not _HAS_PIL:
        return None
    try:
        with _PILImage.open(path) as img:
            return int(img.width), int(img.height)
    except Exception:  # pragma: no cover — never block the CLI on dim reporting
        return None
