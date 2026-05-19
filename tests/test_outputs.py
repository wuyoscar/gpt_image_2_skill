"""Tests for output naming policy and PIL graceful fallback."""
from __future__ import annotations

import re
from pathlib import Path

import pytest

from gpt_image_cli import outputs


def _ctx(count: int, n: int, tmp_path: Path, ext: str = "png") -> outputs.NamingContext:
    return outputs.NamingContext(
        prompt="A watermelon dancing",
        extension=ext,
        count=count,
        n=n,
        output_dir=str(tmp_path),
        timestamp="2026-05-19-10-00-00",
    )


def test_count1_n1_no_suffix(tmp_path: Path):
    path = outputs.build_path(_ctx(1, 1, tmp_path), task_id=1, grid_index=0)
    assert path.parent == tmp_path
    assert path.name == "2026-05-19-10-00-00-a-watermelon-dancing.png"


def test_count1_n_gt_1_appends_grid_index(tmp_path: Path):
    path0 = outputs.build_path(_ctx(1, 4, tmp_path), task_id=1, grid_index=0)
    path3 = outputs.build_path(_ctx(1, 4, tmp_path), task_id=1, grid_index=3)
    assert path0.name.endswith("-dancing_0.png")
    assert path3.name.endswith("-dancing_3.png")


def test_count_gt_1_n1_appends_task_id(tmp_path: Path):
    path = outputs.build_path(_ctx(10, 1, tmp_path), task_id=7, grid_index=0)
    assert path.name.endswith("-dancing_007.png")
    assert "_0.png" not in path.name  # no spurious grid index


def test_count_gt_1_n_gt_1_appends_both(tmp_path: Path):
    path = outputs.build_path(_ctx(10, 2, tmp_path), task_id=7, grid_index=1)
    assert path.name.endswith("-dancing_007_1.png")


def test_explicit_output_path_n1(tmp_path: Path):
    target = outputs.explicit_output_path(str(tmp_path / "poster.png"), n=1, grid_index=0)
    assert target.name == "poster.png"


def test_explicit_output_path_n_gt_1_indexes(tmp_path: Path):
    target0 = outputs.explicit_output_path(str(tmp_path / "poster.png"), n=4, grid_index=0)
    target3 = outputs.explicit_output_path(str(tmp_path / "poster.png"), n=4, grid_index=3)
    assert target0.name == "poster_0.png"
    assert target3.name == "poster_3.png"


def test_write_bytes_creates_parents(tmp_path: Path):
    nested = tmp_path / "a" / "b" / "c.png"
    outputs.write_bytes(nested, b"\x89PNG\r\n\x1a\n")
    assert nested.exists()
    assert nested.read_bytes().startswith(b"\x89PNG")


def test_slugify_strips_and_collapses():
    assert outputs.slugify("Hello, World!!") == "hello-world"
    assert outputs.slugify("   spaced     out   ") == "spaced-out"
    assert outputs.slugify("") == "image"


def test_make_timestamp_is_iso_like():
    stamp = outputs.make_timestamp()
    assert re.match(r"^\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}$", stamp)


def test_resolve_output_dir_legacy_fig_used_when_present(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "fig").mkdir()
    out = outputs.resolve_output_dir(None, count=1)
    assert out == tmp_path / "fig"


def test_resolve_output_dir_batch_default(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    out = outputs.resolve_output_dir(None, count=5)
    assert out == tmp_path / "output_images"


def test_resolve_output_dir_explicit_wins(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "fig").mkdir()
    out = outputs.resolve_output_dir(str(tmp_path / "custom"), count=1)
    assert out == tmp_path / "custom"


def test_image_dimensions_graceful_for_non_image(tmp_path: Path):
    path = tmp_path / "not_an_image.png"
    path.write_bytes(b"definitely-not-png")
    # Either Pillow is installed and returns None (read failure),
    # or Pillow is missing and we also return None — both must not raise.
    assert outputs.image_dimensions(path) is None
