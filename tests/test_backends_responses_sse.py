"""Tests for the streaming /v1/responses backend.

We mock ``requests.post`` so the backend never reaches the network. The fake
response object yields a hand-crafted SSE stream that exercises:

* ``response.image_generation_call.partial_image`` events (must be kept as
  fallback, must not trigger early-exit).
* ``response.completed`` containing the final ``output[].result``.
* Mid-stream cancellation via ``threading.Event``.
"""
from __future__ import annotations

import base64
import threading
from pathlib import Path

import pytest

from gpt_image_cli import backends
from gpt_image_cli.config import EffectiveConfig

_PIXEL_BYTES = b"\x89PNG\r\n\x1a\nfake-png-bytes"
_PIXEL_B64 = base64.b64encode(_PIXEL_BYTES).decode("ascii")
_PARTIAL_BYTES = b"\x89PNG\r\n\x1a\npartial-bytes"
_PARTIAL_B64 = base64.b64encode(_PARTIAL_BYTES).decode("ascii")


def _make_cfg(**overrides) -> EffectiveConfig:
    cfg = EffectiveConfig(
        api_key="sk-test",
        model="gpt-image-2",
        backend="responses",
        size="1k-16:9",
        quality="low",
        output_format="png",
        n=1,
    )
    for k, v in overrides.items():
        setattr(cfg, k, v)
    return cfg


class _FakeResponse:
    def __init__(self, lines: list[str], status_code: int = 200, text: str = ""):
        self.status_code = status_code
        self._lines = list(lines)
        self.text = text
        self._closed = False

    def iter_lines(self, decode_unicode: bool = True):  # noqa: ARG002
        for line in self._lines:
            yield line

    def close(self) -> None:
        self._closed = True


def _sse(events: list[dict]) -> list[str]:
    import json
    out: list[str] = []
    for evt in events:
        out.append(f"data: {json.dumps(evt)}")
    out.append("data: [DONE]")
    return out


def test_response_completed_yields_final_bytes(monkeypatch):
    events = [
        {"type": "response.image_generation_call.in_progress"},
        {"type": "response.image_generation_call.partial_image", "partial_image_b64": _PARTIAL_B64},
        {"type": "response.completed", "response": {
            "output": [{"type": "image_generation_call", "result": _PIXEL_B64}],
        }},
    ]
    fake = _FakeResponse(_sse(events))
    monkeypatch.setattr(backends.requests, "post", lambda *a, **kw: fake)

    result = backends.call_responses_stream(
        prompt="hello",
        images=None,
        mask=None,
        cfg=_make_cfg(),
        cancel_event=threading.Event(),
    )
    assert result == [_PIXEL_BYTES]
    assert fake._closed is True


def test_partial_used_as_fallback_when_completed_missing(monkeypatch):
    events = [
        {"type": "response.image_generation_call.partial_image", "partial_image_b64": _PARTIAL_B64},
    ]
    fake = _FakeResponse(_sse(events))
    monkeypatch.setattr(backends.requests, "post", lambda *a, **kw: fake)

    result = backends.call_responses_stream(
        prompt="hello",
        images=None,
        mask=None,
        cfg=_make_cfg(),
        cancel_event=threading.Event(),
    )
    assert result == [_PARTIAL_BYTES]


def test_partial_does_not_early_exit_before_completed(monkeypatch):
    # If partial caused early-exit, the LATER partial would be lost and the
    # final completed result would never be honoured.
    events = [
        {"type": "response.image_generation_call.partial_image", "partial_image_b64": "AAAA"},
        {"type": "response.image_generation_call.partial_image", "partial_image_b64": _PARTIAL_B64},
        {"type": "response.completed", "response": {
            "output": [{"type": "image_generation_call", "result": _PIXEL_B64}],
        }},
    ]
    fake = _FakeResponse(_sse(events))
    monkeypatch.setattr(backends.requests, "post", lambda *a, **kw: fake)
    result = backends.call_responses_stream(
        prompt="hello",
        images=None,
        mask=None,
        cfg=_make_cfg(),
        cancel_event=threading.Event(),
    )
    assert result == [_PIXEL_BYTES]


def test_http_error_raises_backend_error(monkeypatch):
    fake = _FakeResponse([], status_code=401, text="unauthorized")
    monkeypatch.setattr(backends.requests, "post", lambda *a, **kw: fake)
    with pytest.raises(backends.BackendError, match="HTTP 401"):
        backends.call_responses_stream(
            prompt="hello",
            images=None,
            mask=None,
            cfg=_make_cfg(),
            cancel_event=threading.Event(),
        )


def test_cancel_event_raises_cancelled_error(monkeypatch):
    # Construct a stream that would otherwise yield a completed event but
    # cancel before the first SSE line is consumed.
    events = [{"type": "response.completed", "response": {
        "output": [{"type": "image_generation_call", "result": _PIXEL_B64}],
    }}]
    fake = _FakeResponse(_sse(events))
    monkeypatch.setattr(backends.requests, "post", lambda *a, **kw: fake)

    cancel = threading.Event()
    cancel.set()  # already cancelled
    with pytest.raises(backends.CancelledError):
        backends.call_responses_stream(
            prompt="hello",
            images=None,
            mask=None,
            cfg=_make_cfg(),
            cancel_event=cancel,
        )


def test_n_gt_1_rejected_up_front():
    with pytest.raises(backends.BackendError, match="--n > 1"):
        backends.call_responses_stream(
            prompt="hello",
            images=None,
            mask=None,
            cfg=_make_cfg(n=2),
            cancel_event=threading.Event(),
        )


def test_mask_rejected_up_front(tmp_path: Path):
    mask = tmp_path / "mask.png"
    mask.write_bytes(b"\x89PNG\r\n\x1a\nfake")
    with pytest.raises(backends.BackendError, match="--mask"):
        backends.call_responses_stream(
            prompt="hello",
            images=None,
            mask=mask,
            cfg=_make_cfg(),
            cancel_event=threading.Event(),
        )


def test_multiple_images_rejected(tmp_path: Path):
    img1 = tmp_path / "a.png"
    img1.write_bytes(b"\x89PNG\r\n\x1a\n")
    img2 = tmp_path / "b.png"
    img2.write_bytes(b"\x89PNG\r\n\x1a\n")
    with pytest.raises(backends.BackendError, match="at most one --image"):
        backends.call_responses_stream(
            prompt="hello",
            images=[img1, img2],
            mask=None,
            cfg=_make_cfg(),
            cancel_event=threading.Event(),
        )


def test_oversize_input_image_rejected(tmp_path: Path, monkeypatch):
    big = tmp_path / "big.png"
    big.write_bytes(b"\x00" * (backends.MAX_INPUT_BYTES + 1))
    with pytest.raises(backends.BackendError, match="4MB"):
        backends.call_responses_stream(
            prompt="hello",
            images=[big],
            mask=None,
            cfg=_make_cfg(),
            cancel_event=threading.Event(),
        )


def test_payload_includes_size_and_compression(monkeypatch):
    captured: dict = {}

    def fake_post(url, headers=None, json=None, stream=None, timeout=None, **_):
        captured["url"] = url
        captured["payload"] = json
        return _FakeResponse(_sse([{
            "type": "response.completed",
            "response": {"output": [{"type": "image_generation_call", "result": _PIXEL_B64}]},
        }]))

    monkeypatch.setattr(backends.requests, "post", fake_post)
    cfg = _make_cfg(output_format="jpeg", compression=70)
    backends.call_responses_stream(
        prompt="hi",
        images=None,
        mask=None,
        cfg=cfg,
        cancel_event=threading.Event(),
    )
    tool = captured["payload"]["tools"][0]
    assert tool["size"] == "1k-16:9"
    assert tool["output_compression"] == 70
    assert tool["output_format"] == "jpeg"


def test_payload_omits_compression_for_png(monkeypatch):
    captured: dict = {}

    def fake_post(url, headers=None, json=None, stream=None, timeout=None, **_):
        captured["payload"] = json
        return _FakeResponse(_sse([{
            "type": "response.completed",
            "response": {"output": [{"type": "image_generation_call", "result": _PIXEL_B64}]},
        }]))

    monkeypatch.setattr(backends.requests, "post", fake_post)
    cfg = _make_cfg(output_format="png", compression=80)
    backends.call_responses_stream(
        prompt="hi",
        images=None,
        mask=None,
        cfg=cfg,
        cancel_event=threading.Event(),
    )
    tool = captured["payload"]["tools"][0]
    assert "output_compression" not in tool


def test_size_auto_is_omitted(monkeypatch):
    captured: dict = {}

    def fake_post(url, headers=None, json=None, stream=None, timeout=None, **_):
        captured["payload"] = json
        return _FakeResponse(_sse([{
            "type": "response.completed",
            "response": {"output": [{"type": "image_generation_call", "result": _PIXEL_B64}]},
        }]))

    monkeypatch.setattr(backends.requests, "post", fake_post)
    cfg = _make_cfg(size="auto")
    backends.call_responses_stream(
        prompt="hi",
        images=None,
        mask=None,
        cfg=cfg,
        cancel_event=threading.Event(),
    )
    tool = captured["payload"]["tools"][0]
    assert "size" not in tool
