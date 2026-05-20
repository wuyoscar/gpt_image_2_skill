"""Tests for size preset resolution and custom WxH validation."""
from __future__ import annotations

import pytest

from gpt_image_cli.sizes import (
    SIZE_PRESETS,
    MAX_DIM,
    MIN_DIM,
    list_presets,
    resolve_size,
    validate_custom_size,
)


def test_existing_shortcuts_unchanged():
    assert SIZE_PRESETS["1k"] == "1024x1024"
    assert SIZE_PRESETS["2k"] == "2048x2048"
    assert SIZE_PRESETS["4k"] == "3840x2160"
    assert SIZE_PRESETS["portrait"] == "1024x1536"
    assert SIZE_PRESETS["landscape"] == "1536x1024"
    assert SIZE_PRESETS["square"] == "1024x1024"
    assert SIZE_PRESETS["wide"] == "2048x1152"
    assert SIZE_PRESETS["tall"] == "2160x3840"


def test_new_aspect_presets():
    assert SIZE_PRESETS["1k-16:9"] == "1792x1008"
    assert SIZE_PRESETS["2k-16:9"] == "2048x1152"
    assert SIZE_PRESETS["2.5k-16:9"] == "2560x1440"
    assert SIZE_PRESETS["3k-16:9"] == "3072x1728"
    assert SIZE_PRESETS["4k-16:9"] == "3840x2160"
    assert SIZE_PRESETS["1k-9:16"] == "1008x1792"
    assert SIZE_PRESETS["2k-9:16"] == "1152x2048"
    assert SIZE_PRESETS["4k-9:16"] == "2160x3840"
    assert SIZE_PRESETS["1k-3:2"] == "1536x1024"
    assert SIZE_PRESETS["1k-2:3"] == "1024x1536"
    assert SIZE_PRESETS["auto"] == "auto"


def test_resolve_is_case_insensitive():
    assert resolve_size("1K") == "1024x1024"
    assert resolve_size("4K-16:9") == "3840x2160"


def test_resolve_passes_through_valid_custom():
    assert resolve_size("1024x1024") == "1024x1024"
    assert resolve_size("1536X1024") == "1536x1024"
    assert resolve_size("  2048×1152 ") == "2048x1152"


def test_list_presets_contains_old_and_new():
    presets = list_presets()
    assert "1k" in presets
    assert "1k-16:9" in presets
    assert "auto" in presets


@pytest.mark.parametrize("bad", ["", "abc", "1024", "1024x", "x1024"])
def test_unparseable_custom_rejected(bad):
    with pytest.raises(ValueError):
        validate_custom_size(bad)


def test_below_min_rejected():
    with pytest.raises(ValueError, match="≥"):
        validate_custom_size(f"{MIN_DIM - 16}x1024")


def test_above_max_rejected():
    with pytest.raises(ValueError, match="≤"):
        validate_custom_size(f"{MAX_DIM + 16}x1024")


def test_non_multiple_of_16_rejected():
    with pytest.raises(ValueError, match="multiples of 16"):
        validate_custom_size("100x100")
    with pytest.raises(ValueError, match="multiples of 16"):
        validate_custom_size("1024x100")


def test_extreme_aspect_ratio_rejected():
    # 4:1 ratio breaks the 3:1 cap.
    with pytest.raises(ValueError, match="ratio"):
        validate_custom_size("4096x1024")


def test_aspect_ratio_exactly_three_to_one_allowed():
    # 3072 / 1024 == 3.0 — boundary should pass.
    assert validate_custom_size("3072x1024") == "3072x1024"


def test_resolve_raises_for_none():
    with pytest.raises(ValueError):
        resolve_size(None)  # type: ignore[arg-type]
