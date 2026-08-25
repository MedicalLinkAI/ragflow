#
#  Copyright 2026 MedLinkAI. All Rights Reserved.
#
#  Tests for rag/svr/task_executor.py — task-level memory release.
#
#  8/23 客户事故取证结论：4 个 task_executor 常驻 3 天累积 160G RSS
#  （anon=160.1G，非页缓存挂账），任务结束后既不触发 gc.collect，
#  glibc 也不归还 arena → RSS 只涨不降，挤干主机页缓存引发 IO 风暴。
#  修复契约：
#    1) _release_task_memory() 每任务收尾强制回收（gc.collect + Linux malloc_trim）；
#    2) handle_task 的 done/canceled/exception 三路径 finally 都会调用它；
#    3) 释放动作自身失败不得影响任务收尾（吞异常）。
#
import importlib
import sys
import types
import warnings
from types import SimpleNamespace

import pytest

warnings.filterwarnings(
    "ignore",
    message="pkg_resources is deprecated as an API.*",
    category=UserWarning,
)
warnings.filterwarnings(
    "ignore",
    message="Tensorflow not installed; ParametricUMAP will be unavailable",
    category=ImportWarning,
)


def _install_xgboost_stub_if_unavailable():
    if "xgboost" in sys.modules:
        return
    try:
        importlib.import_module("xgboost")
        sys.modules["xgboost"] = types.ModuleType("xgboost")
    except Exception:
        sys.modules["xgboost"] = types.ModuleType("xgboost")


_install_xgboost_stub_if_unavailable()

# task_executor transitively imports third-party packages (scholarly,
# graspologic, ...) that contain invalid escape sequences. Downgrade
# warnings for the whole import chain (same rationale as guards test).
with warnings.catch_warnings():
    warnings.simplefilter("default")
    from rag.svr import task_executor


# ── _release_task_memory 单元契约 ──────────────────────────────────


class TestReleaseTaskMemory:
    def test_calls_gc_collect(self):
        calls = []
        monkey = pytest.MonkeyPatch()
        monkey.setattr(task_executor.gc, "collect", lambda *a, **k: calls.append("gc"))
        try:
            task_executor._release_task_memory()
        finally:
            monkey.undo()
        assert "gc" in calls

    def test_linux_calls_malloc_trim_zero(self):
        trim_args = []

        class FakeLibc:
            def malloc_trim(self, pad):
                trim_args.append(pad)

        monkey = pytest.MonkeyPatch()
        # 桩掉真实 gc.collect：避免翻出前序测试垃圾触发 unraisable
        monkey.setattr(task_executor.gc, "collect", lambda *a, **k: None)
        monkey.setattr(sys, "platform", "linux")
        monkey.setattr(task_executor.ctypes, "CDLL", lambda name: FakeLibc())
        try:
            task_executor._release_task_memory()
        finally:
            monkey.undo()
        assert trim_args == [0]

    def test_non_linux_skips_malloc_trim(self):
        def fail_cdll(name):
            raise AssertionError("CDLL must not be called off-linux")

        monkey = pytest.MonkeyPatch()
        monkey.setattr(task_executor.gc, "collect", lambda *a, **k: None)
        monkey.setattr(sys, "platform", "win32")
        monkey.setattr(task_executor.ctypes, "CDLL", fail_cdll)
        try:
            task_executor._release_task_memory()  # must not raise
        finally:
            monkey.undo()

    def test_malloc_trim_failure_swallowed(self):
        def fail_cdll(name):
            raise OSError("libc unavailable")

        monkey = pytest.MonkeyPatch()
        monkey.setattr(task_executor.gc, "collect", lambda *a, **k: None)
        monkey.setattr(sys, "platform", "linux")
        monkey.setattr(task_executor.ctypes, "CDLL", fail_cdll)
        try:
            task_executor._release_task_memory()  # must not raise
        finally:
            monkey.undo()


# ── handle_task 收尾接线契约 ───────────────────────────────────────


def _patch_task_flow(monkeypatch, do_handle_task):
    """把 handle_task 的外部依赖全部桩掉，只验证收尾释放接线。"""
    released = []
    fake_msg = SimpleNamespace(ack=lambda: None)
    fake_task = {"id": "task-1", "task_type": "parse", "doc_id": "doc-1"}

    async def fake_collect():
        return fake_msg, fake_task

    monkeypatch.setattr(task_executor, "collect", fake_collect)
    monkeypatch.setattr(task_executor, "do_handle_task", do_handle_task)
    monkeypatch.setattr(task_executor, "set_progress", lambda *a, **k: None)
    monkeypatch.setattr(task_executor, "has_canceled", lambda tid: False)
    monkeypatch.setattr(
        task_executor.PipelineOperationLogService,
        "record_pipeline_operation",
        staticmethod(lambda **k: None),
    )
    monkeypatch.setattr(
        task_executor, "_release_task_memory", lambda: released.append(1)
    )
    return released


@pytest.mark.asyncio
async def test_handle_task_releases_memory_on_success(monkeypatch):
    async def ok(task):
        pass

    released = _patch_task_flow(monkeypatch, ok)
    await task_executor.handle_task()
    assert released == [1]


@pytest.mark.asyncio
async def test_handle_task_releases_memory_on_exception(monkeypatch):
    async def boom(task):
        raise RuntimeError("parse exploded")

    released = _patch_task_flow(monkeypatch, boom)
    await task_executor.handle_task()  # 异常被 handle_task 吞掉记日志
    assert released == [1]


@pytest.mark.asyncio
async def test_handle_task_releases_memory_on_cancel(monkeypatch):
    from common.exceptions import TaskCanceledException

    async def canceled(task):
        raise TaskCanceledException("user canceled")

    released = _patch_task_flow(monkeypatch, canceled)
    await task_executor.handle_task()
    assert released == [1]
