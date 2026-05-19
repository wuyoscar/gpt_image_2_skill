"""Tests for the batch runner: stats accumulation and cancellation."""
from __future__ import annotations

import threading
from pathlib import Path

import pytest

from gpt_image_cli.runner import BatchStats, format_summary, run_batch


def _ok_task_fn(payload: bytes):
    def fn(task_id: int, cancel_event: threading.Event) -> list[bytes]:
        return [payload]
    return fn


def _failing_task_fn():
    def fn(task_id: int, cancel_event: threading.Event) -> list[bytes]:
        raise RuntimeError(f"boom-{task_id}")
    return fn


def _write_fn_factory(root: Path):
    def write(task_id: int, blobs: list[bytes]) -> list[Path]:
        paths = []
        for i, blob in enumerate(blobs):
            p = root / f"t{task_id:03d}_{i}.bin"
            p.write_bytes(blob)
            paths.append(p)
        return paths

    return write


def test_run_batch_counts_successes(tmp_path: Path):
    stats = run_batch(
        count=5,
        concurrency=2,
        task_fn=_ok_task_fn(b"hello"),
        write_fn=_write_fn_factory(tmp_path),
        cancel_event=threading.Event(),
        progress=False,
    )
    assert stats.total == 5
    assert stats.success == 5
    assert stats.fail == 0
    assert stats.cancelled == 0
    assert {r.task_id for r in stats.per_task} == {1, 2, 3, 4, 5}
    assert all(r.status == "ok" for r in stats.per_task)


def test_run_batch_records_failures_per_task(tmp_path: Path):
    stats = run_batch(
        count=3,
        concurrency=1,
        task_fn=_failing_task_fn(),
        write_fn=_write_fn_factory(tmp_path),
        cancel_event=threading.Event(),
        progress=False,
    )
    assert stats.success == 0
    assert stats.fail == 3
    assert all("boom-" in r.error for r in stats.per_task)


def test_pre_set_cancel_marks_all_cancelled(tmp_path: Path):
    cancel = threading.Event()
    cancel.set()
    stats = run_batch(
        count=4,
        concurrency=2,
        task_fn=_ok_task_fn(b"x"),
        write_fn=_write_fn_factory(tmp_path),
        cancel_event=cancel,
        progress=False,
    )
    assert stats.cancelled == 4
    assert stats.success == 0


def test_write_failure_isolated_per_task(tmp_path: Path):
    fail_after = {"flag": False}

    def write(task_id: int, blobs: list[bytes]) -> list[Path]:
        if task_id == 2:
            raise OSError("disk full")
        path = tmp_path / f"t{task_id}.bin"
        path.write_bytes(blobs[0])
        return [path]

    stats = run_batch(
        count=3,
        concurrency=1,
        task_fn=_ok_task_fn(b"x"),
        write_fn=write,
        cancel_event=threading.Event(),
        progress=False,
    )
    assert stats.success == 2
    assert stats.fail == 1
    fail_rec = next(r for r in stats.per_task if r.status == "fail")
    assert "disk full" in fail_rec.error


def test_avg_seconds_zero_when_no_success(tmp_path: Path):
    stats = run_batch(
        count=2,
        concurrency=1,
        task_fn=_failing_task_fn(),
        write_fn=_write_fn_factory(tmp_path),
        cancel_event=threading.Event(),
        progress=False,
    )
    assert stats.avg_seconds == 0.0


def test_format_summary_lists_counts():
    stats = BatchStats(total=10, success=7, fail=2, cancelled=1, total_elapsed=12.5, success_elapsed=14.0)
    s = format_summary(stats)
    assert "OK:7" in s
    assert "FAIL:2" in s
    assert "CANCELLED:1" in s
    assert "/ 10" in s


def test_to_dict_round_trip(tmp_path: Path):
    stats = run_batch(
        count=2,
        concurrency=1,
        task_fn=_ok_task_fn(b"x"),
        write_fn=_write_fn_factory(tmp_path),
        cancel_event=threading.Event(),
        progress=False,
    )
    d = stats.to_dict()
    assert d["total"] == 2
    assert d["success"] == 2
    assert isinstance(d["tasks"], list)
    assert len(d["tasks"]) == 2
