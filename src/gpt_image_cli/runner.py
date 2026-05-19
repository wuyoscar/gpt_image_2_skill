"""Batch execution, statistics, and progress reporting for gpt-image.

A single batch is ``count`` independent API calls — each call may return
``n`` images (when the backend supports it). The runner manages the thread
pool, accumulates timing, success, and failure stats, drives the progress bar,
and forwards a shared :class:`threading.Event` so workers can exit early when
the user hits ``Ctrl+C``.

Tests can use :func:`run_batch` directly without standing up a real backend.
"""
from __future__ import annotations

import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Sequence

try:  # tqdm is a soft dep — fall back to a quiet counter when unavailable.
    from tqdm import tqdm as _tqdm  # type: ignore[import-not-found]
    _HAS_TQDM = True
except ImportError:  # pragma: no cover
    _HAS_TQDM = False

TaskFn = Callable[[int, threading.Event], list[bytes]]
WriteFn = Callable[[int, list[bytes]], list[Path]]


@dataclass
class TaskRecord:
    task_id: int
    status: str  # "ok" | "fail" | "cancelled"
    elapsed: float
    files: list[Path] = field(default_factory=list)
    error: str = ""


@dataclass
class BatchStats:
    total: int = 0
    success: int = 0
    fail: int = 0
    cancelled: int = 0
    total_elapsed: float = 0.0
    success_elapsed: float = 0.0
    per_task: list[TaskRecord] = field(default_factory=list)

    @property
    def avg_seconds(self) -> float:
        return (self.success_elapsed / self.success) if self.success else 0.0

    def to_dict(self) -> dict[str, Any]:
        return {
            "total": self.total,
            "success": self.success,
            "fail": self.fail,
            "cancelled": self.cancelled,
            "total_elapsed_seconds": round(self.total_elapsed, 3),
            "average_success_seconds": round(self.avg_seconds, 3),
            "tasks": [
                {
                    "task_id": r.task_id,
                    "status": r.status,
                    "elapsed_seconds": round(r.elapsed, 3),
                    "files": [str(p) for p in r.files],
                    "error": r.error,
                }
                for r in self.per_task
            ],
        }


def _make_progress(total: int, enabled: bool):
    """Return a context-manager-like progress wrapper with .update() and .close()."""
    if not enabled or total <= 1 or not _HAS_TQDM:
        class _Noop:
            def update(self, _n: int = 1) -> None:
                return None

            def close(self) -> None:
                return None

        return _Noop()
    return _tqdm(total=total, unit="img", dynamic_ncols=True)


def run_batch(
    *,
    count: int,
    concurrency: int,
    task_fn: TaskFn,
    write_fn: WriteFn,
    cancel_event: threading.Event,
    progress: bool = True,
    log: Callable[[str], None] | None = None,
) -> BatchStats:
    """Execute ``count`` tasks with up to ``concurrency`` workers.

    ``task_fn(task_id, cancel_event)`` produces image bytes; ``write_fn(task_id,
    images)`` lands them on disk and returns the written paths. Splitting the
    two lets tests drive the runner without touching disk or the network.
    """
    stats = BatchStats(total=count)
    log_fn = log or (lambda _msg: None)
    progress_bar = _make_progress(count, enabled=progress)

    started = time.monotonic()

    def _wrap(task_id: int) -> TaskRecord:
        task_start = time.monotonic()
        if cancel_event.is_set():
            return TaskRecord(task_id, "cancelled", 0.0, [], "cancelled before start")
        try:
            blobs = task_fn(task_id, cancel_event)
        except Exception as exc:  # noqa: BLE001 — fan-in error reporting
            elapsed = time.monotonic() - task_start
            kind = type(exc).__name__
            return TaskRecord(task_id, "fail", elapsed, [], f"{kind}: {exc}")
        try:
            paths = write_fn(task_id, blobs)
        except Exception as exc:  # noqa: BLE001 — disk write failure isolated per task
            elapsed = time.monotonic() - task_start
            kind = type(exc).__name__
            return TaskRecord(task_id, "fail", elapsed, [], f"write {kind}: {exc}")
        elapsed = time.monotonic() - task_start
        return TaskRecord(task_id, "ok", elapsed, paths, "")

    try:
        with ThreadPoolExecutor(max_workers=max(1, concurrency)) as ex:
            futures = {ex.submit(_wrap, i + 1): i + 1 for i in range(count)}
            try:
                for fut in as_completed(futures):
                    record = fut.result()
                    stats.per_task.append(record)
                    if record.status == "ok":
                        stats.success += 1
                        stats.success_elapsed += record.elapsed
                    elif record.status == "cancelled":
                        stats.cancelled += 1
                    else:
                        stats.fail += 1
                    progress_bar.update(1)
                    if record.status == "ok":
                        log_fn(_format_ok(record))
                    elif record.status == "fail":
                        log_fn(_format_fail(record))
            except KeyboardInterrupt:
                cancel_event.set()
                # Drain remaining futures so they complete or check the event.
                for fut in futures:
                    if not fut.done():
                        try:
                            record = fut.result(timeout=1.0)
                        except Exception:
                            continue
                        else:
                            stats.per_task.append(record)
                raise
    finally:
        progress_bar.close()
        stats.total_elapsed = time.monotonic() - started

    stats.per_task.sort(key=lambda r: r.task_id)
    return stats


def _format_ok(record: TaskRecord) -> str:
    files = ", ".join(str(p) for p in record.files)
    return f"[#{record.task_id:03d}] OK {record.elapsed:.1f}s  {files}"


def _format_fail(record: TaskRecord) -> str:
    return f"[#{record.task_id:03d}] FAIL {record.elapsed:.1f}s  {record.error}"


def format_summary(stats: BatchStats) -> str:
    parts = [
        f"OK:{stats.success}",
        f"FAIL:{stats.fail}",
    ]
    if stats.cancelled:
        parts.append(f"CANCELLED:{stats.cancelled}")
    parts.append(f"/ {stats.total}")
    parts.append(f"avg {stats.avg_seconds:.1f}s")
    parts.append(f"total {stats.total_elapsed:.1f}s")
    return "  ".join(parts)


def all_files(stats: BatchStats) -> Sequence[Path]:
    out: list[Path] = []
    for rec in stats.per_task:
        out.extend(rec.files)
    return out
