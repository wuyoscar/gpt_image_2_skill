"""Configuration resolution for gpt-image.

Precedence (highest first): CLI flag → ``--config`` file → ``./config.ini`` →
``./.gpt-image.ini`` → ``OPENAI_API_KEY`` env (after loading ``.env`` and
``~/.env`` without overriding existing env) → built-in defaults.

The config file format mirrors the bundled Tkinter UI (`生图代码.py`) so users
can move between the two surfaces with a single ``config.ini``::

    [settings]
    api_key = sk-...
    model = gpt-image-2
    backend = openai
    base_url =
    size = 4k-16:9
    quality = auto
    output_format = png
    compression = 100
    count = 1
    concurrency = 1
    timeout = 600
    output_dir = ./output_images
"""
from __future__ import annotations

import configparser
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

CONFIG_SECTION = "settings"

DEFAULT_BACKEND = "openai"
DEFAULT_MODEL = "gpt-image-2"
DEFAULT_RESPONSES_BASE_URL = "https://www.codexapis.com"

# Built-in defaults; every field is overridable by config file or CLI flag.
BUILTIN_DEFAULTS: dict[str, str] = {
    "api_key": "",
    "model": DEFAULT_MODEL,
    "backend": DEFAULT_BACKEND,
    "base_url": "",
    "size": "1024x1024",
    "quality": "high",
    "output_format": "png",
    "compression": "",
    "count": "1",
    "concurrency": "1",
    "timeout": "600",
    "output_dir": "",
    "moderation": "low",
    "background": "",
    "input_fidelity": "",
    "user": "",
    "n": "1",
    "prompt": "",
}

# Keys whose effective value should be redacted in --show-config output.
_REDACTED_KEYS = frozenset({"api_key"})


def load_env_chain() -> None:
    """Resolve ``OPENAI_API_KEY`` without overriding runtime-provided env.

    Order: process env → ``./.env`` → ``~/.env``. Existing process env wins so
    hosted agents or explicit shell exports are not replaced by local files.
    """
    load_dotenv(Path.cwd() / ".env", override=False)
    load_dotenv(Path.home() / ".env", override=False)


def discover_config_path(explicit: str | os.PathLike[str] | None) -> Path | None:
    """Return the first existing config path in precedence order."""
    if explicit:
        p = Path(explicit).expanduser()
        return p if p.is_file() else None
    for candidate in (Path.cwd() / "config.ini", Path.cwd() / ".gpt-image.ini"):
        if candidate.is_file():
            return candidate
    return None


def load_config_file(path: Path) -> dict[str, str]:
    """Read ``[settings]`` from a config file and return a flat string dict."""
    parser = configparser.ConfigParser()
    parser.read(path, encoding="utf-8")
    if not parser.has_section(CONFIG_SECTION):
        return {}
    return {k: v for k, v in parser.items(CONFIG_SECTION)}


def save_config_file(path: Path, values: dict[str, str]) -> None:
    """Write a flat string dict back to a config file under ``[settings]``."""
    parser = configparser.ConfigParser()
    parser[CONFIG_SECTION] = {k: str(v) for k, v in values.items()}
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        parser.write(handle)


@dataclass
class EffectiveConfig:
    """Frozen, fully-merged configuration for a single CLI invocation."""

    api_key: str = ""
    model: str = DEFAULT_MODEL
    backend: str = DEFAULT_BACKEND
    base_url: str = ""
    size: str = "1024x1024"
    quality: str = "high"
    output_format: str = "png"
    compression: int | None = None
    count: int = 1
    concurrency: int = 1
    timeout: int = 600
    output_dir: str = ""
    moderation: str = "low"
    background: str | None = None
    input_fidelity: str | None = None
    user: str | None = None
    n: int = 1
    config_path: str = ""
    extra: dict[str, str] = field(default_factory=dict)

    def effective_base_url(self) -> str | None:
        """Return the base URL the backend should target, or None to use SDK default."""
        if self.base_url:
            return self.base_url
        if self.backend == "responses":
            return DEFAULT_RESPONSES_BASE_URL
        return None

    def public_view(self) -> dict[str, Any]:
        """Return a dict safe for ``--show-config``; redacts secrets."""
        out: dict[str, Any] = {}
        for key in (
            "model", "backend", "base_url", "size", "quality", "output_format",
            "compression", "count", "concurrency", "timeout", "output_dir",
            "moderation", "background", "input_fidelity", "user", "n",
            "config_path",
        ):
            value = getattr(self, key)
            out[key] = value
        out["api_key"] = _redact(self.api_key)
        out["effective_base_url"] = self.effective_base_url()
        return out


def _redact(value: str) -> str:
    if not value:
        return ""
    if len(value) <= 8:
        return "***"
    return f"{value[:4]}…{value[-4:]}"


def _coerce_int(raw: str, default: int) -> int:
    raw = (raw or "").strip()
    if not raw:
        return default
    try:
        return int(raw)
    except ValueError as exc:
        raise ValueError(f"expected integer, got {raw!r}") from exc


def _coerce_optional_int(raw: str) -> int | None:
    raw = (raw or "").strip()
    if not raw:
        return None
    try:
        return int(raw)
    except ValueError as exc:
        raise ValueError(f"expected integer, got {raw!r}") from exc


def _coerce_optional_str(raw: str) -> str | None:
    raw = (raw or "").strip()
    return raw or None


def merge(
    cli_overrides: dict[str, Any],
    config_file_values: dict[str, str] | None = None,
    config_path: Path | None = None,
) -> EffectiveConfig:
    """Compose ``EffectiveConfig`` from defaults < config file < CLI overrides.

    ``cli_overrides`` is a dict where values of ``None`` mean "not provided"
    (defer to lower-precedence layers). String, int, and bool values are passed
    through. Unknown keys land in ``EffectiveConfig.extra`` for downstream use.
    """
    merged: dict[str, str] = dict(BUILTIN_DEFAULTS)
    if config_file_values:
        for k, v in config_file_values.items():
            if v is None:
                continue
            merged[k] = str(v)
    for k, v in cli_overrides.items():
        if v is None:
            continue
        merged[k] = str(v) if not isinstance(v, str) else v

    api_key = (merged.get("api_key") or os.environ.get("OPENAI_API_KEY", "")).strip()

    cfg = EffectiveConfig(
        api_key=api_key,
        model=(merged.get("model") or DEFAULT_MODEL).strip(),
        backend=(merged.get("backend") or DEFAULT_BACKEND).strip().lower(),
        base_url=(merged.get("base_url") or "").strip(),
        size=(merged.get("size") or "1024x1024").strip(),
        quality=(merged.get("quality") or "high").strip().lower(),
        output_format=(merged.get("output_format") or "png").strip().lower(),
        compression=_coerce_optional_int(merged.get("compression", "")),
        count=_coerce_int(merged.get("count", "1"), 1),
        concurrency=_coerce_int(merged.get("concurrency", "1"), 1),
        timeout=_coerce_int(merged.get("timeout", "600"), 600),
        output_dir=(merged.get("output_dir") or "").strip(),
        moderation=(merged.get("moderation") or "low").strip().lower(),
        background=_coerce_optional_str(merged.get("background", "")),
        input_fidelity=_coerce_optional_str(merged.get("input_fidelity", "")),
        user=_coerce_optional_str(merged.get("user", "")),
        n=_coerce_int(merged.get("n", "1"), 1),
        config_path=str(config_path) if config_path else "",
    )

    known = {
        "api_key", "model", "backend", "base_url", "size", "quality",
        "output_format", "compression", "count", "concurrency", "timeout",
        "output_dir", "moderation", "background", "input_fidelity", "user", "n",
        "prompt",
    }
    cfg.extra = {k: v for k, v in merged.items() if k not in known}
    return cfg


def serializable_snapshot(cfg: EffectiveConfig, include_api_key: bool = False) -> dict[str, str]:
    """Return the dict shape used by ``save_config_file``.

    By default the API key is omitted so ``--save-config`` does not silently
    write secrets to disk; callers that explicitly want to persist the key can
    pass ``include_api_key=True``.
    """
    data: dict[str, str] = {
        "model": cfg.model,
        "backend": cfg.backend,
        "base_url": cfg.base_url,
        "size": cfg.size,
        "quality": cfg.quality,
        "output_format": cfg.output_format,
        "compression": "" if cfg.compression is None else str(cfg.compression),
        "count": str(cfg.count),
        "concurrency": str(cfg.concurrency),
        "timeout": str(cfg.timeout),
        "output_dir": cfg.output_dir,
        "moderation": cfg.moderation,
        "background": cfg.background or "",
        "input_fidelity": cfg.input_fidelity or "",
        "user": cfg.user or "",
        "n": str(cfg.n),
    }
    if include_api_key and cfg.api_key:
        data["api_key"] = cfg.api_key
    return data
