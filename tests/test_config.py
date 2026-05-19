"""Tests for config file IO and precedence merging."""
from __future__ import annotations

import os
from pathlib import Path

import pytest

from gpt_image_cli import config


@pytest.fixture(autouse=True)
def _clear_env(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)


def test_default_merge_uses_builtins():
    cfg = config.merge({})
    assert cfg.model == "gpt-image-2"
    assert cfg.backend == "openai"
    assert cfg.count == 1
    assert cfg.concurrency == 1
    assert cfg.timeout == 600


def test_config_file_overrides_defaults(tmp_path: Path):
    path = tmp_path / "config.ini"
    path.write_text(
        "[settings]\n"
        "model = gpt-image-2-mini\n"
        "size = 2k-16:9\n"
        "count = 5\n"
        "concurrency = 2\n"
        "backend = responses\n",
        encoding="utf-8",
    )
    values = config.load_config_file(path)
    cfg = config.merge({}, values, path)
    assert cfg.model == "gpt-image-2-mini"
    assert cfg.size == "2k-16:9"
    assert cfg.count == 5
    assert cfg.concurrency == 2
    assert cfg.backend == "responses"
    assert cfg.config_path == str(path)


def test_cli_override_wins_over_config_file(tmp_path: Path):
    path = tmp_path / "config.ini"
    path.write_text("[settings]\nmodel = old-model\ncount = 10\n", encoding="utf-8")
    values = config.load_config_file(path)
    cfg = config.merge({"model": "new-model", "count": 1}, values, path)
    assert cfg.model == "new-model"
    assert cfg.count == 1


def test_env_api_key_fills_when_file_empty(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test-from-env")
    cfg = config.merge({})
    assert cfg.api_key == "sk-test-from-env"


def test_cli_api_key_overrides_env(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "sk-env")
    cfg = config.merge({"api_key": "sk-cli"})
    assert cfg.api_key == "sk-cli"


def test_save_round_trip_excludes_api_key_by_default(tmp_path: Path):
    cfg = config.merge({"model": "m", "size": "1k", "api_key": "sk-secret"})
    target = tmp_path / "out.ini"
    config.save_config_file(target, config.serializable_snapshot(cfg))

    loaded = config.load_config_file(target)
    assert loaded["model"] == "m"
    assert loaded["size"] == "1k"
    assert "api_key" not in loaded


def test_save_with_api_key_when_explicit(tmp_path: Path):
    cfg = config.merge({"api_key": "sk-keep"})
    target = tmp_path / "out.ini"
    config.save_config_file(target, config.serializable_snapshot(cfg, include_api_key=True))
    loaded = config.load_config_file(target)
    assert loaded["api_key"] == "sk-keep"


def test_public_view_redacts_api_key():
    cfg = config.merge({"api_key": "sk-abcdefghijklmnop"})
    view = cfg.public_view()
    assert view["api_key"].startswith("sk-a")
    assert view["api_key"].endswith("mnop")
    assert "abcdefgh" not in view["api_key"]


def test_responses_backend_default_base_url():
    cfg = config.merge({"backend": "responses"})
    assert cfg.effective_base_url() == config.DEFAULT_RESPONSES_BASE_URL


def test_openai_backend_no_default_base_url():
    cfg = config.merge({})
    assert cfg.effective_base_url() is None


def test_explicit_base_url_wins_for_any_backend():
    cfg = config.merge({"base_url": "https://proxy.example/", "backend": "openai"})
    assert cfg.effective_base_url() == "https://proxy.example/"


def test_discover_prefers_explicit(tmp_path: Path):
    f = tmp_path / "custom.ini"
    f.write_text("[settings]\n", encoding="utf-8")
    assert config.discover_config_path(str(f)) == f


def test_discover_falls_back_to_cwd(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "config.ini").write_text("[settings]\n", encoding="utf-8")
    discovered = config.discover_config_path(None)
    assert discovered is not None
    assert discovered.name == "config.ini"


def test_discover_returns_none_when_missing(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    assert config.discover_config_path(None) is None


def test_empty_compression_round_trips_as_none(tmp_path: Path):
    path = tmp_path / "config.ini"
    path.write_text("[settings]\ncompression =\n", encoding="utf-8")
    values = config.load_config_file(path)
    cfg = config.merge({}, values, path)
    assert cfg.compression is None
