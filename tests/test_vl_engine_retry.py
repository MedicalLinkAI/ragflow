"""Behavioral tests: fast-fail + bounded backoff retry on engine death.

Incident 2026-08-22 (report §11 S6): when vLLM died (EngineDeadError →
HTTP 500) the OCR clients failed every in-flight call immediately with no
retry, wasting the ~15s container-restart window. Contract:

- HTTP 500 whose body carries an engine-death signature (EngineDeadError,
  engine core startup failures) is retried with backoff;
- HTTP 502/503 (gateway sees the dead engine) is retried even without a
  signature in the body;
- HTTP 200 returns immediately, no retry;
- HTTP 4xx (request errors, retrying is pointless) returns immediately;
- ConnectionError (port closed during restart) is retried;
- backoff sleeps between attempts (bounded), never sleeps after the last
  attempt, and gives up after VL_ENGINE_MAX_ATTEMPTS total attempts;
- ReadTimeout is NOT retried here (120s hangs are bounded by the task
  watchdog; retrying them would only add load to a stalled engine).

vl_engine_retry.py is dependency-free (stdlib + requests), so these are
real behavioral tests with requests.post / time.sleep monkeypatched.
"""
import os
import sys

import pytest
import requests

_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

from rag.flow.extractor import vl_engine_retry as mod  # noqa: E402


class _FakeResponse:
    def __init__(self, status_code=200, text=""):
        self.status_code = status_code
        self.text = text


@pytest.fixture
def patch_sleep(monkeypatch):
    sleeps = []
    monkeypatch.setattr(mod.time, "sleep", lambda s: sleeps.append(s))
    return sleeps


def _patch_post(monkeypatch, outcomes):
    """queue of results for consecutive post calls: _FakeResponse or Exception."""
    calls = {"n": 0}

    def fake_post(*args, **kwargs):
        i = calls["n"]
        calls["n"] += 1
        outcome = outcomes[i] if i < len(outcomes) else outcomes[-1]
        if isinstance(outcome, Exception):
            raise outcome
        return outcome

    monkeypatch.setattr(mod.requests, "post", fake_post)
    return calls


def test_200_returns_immediately_without_retry(monkeypatch, patch_sleep):
    calls = _patch_post(monkeypatch, [_FakeResponse(200, "ok")])
    r = mod.post_with_engine_retry("http://x/v1/chat/completions", json={})
    assert r.status_code == 200
    assert calls["n"] == 1
    assert patch_sleep == []


def test_engine_dead_500_is_retried_until_success(monkeypatch, patch_sleep):
    dead = _FakeResponse(500, '{"error": "EngineDeadError: Engine core initialization failed"}')
    calls = _patch_post(monkeypatch, [dead, dead, _FakeResponse(200, "ok")])
    r = mod.post_with_engine_retry("http://x", json={})
    assert r.status_code == 200
    assert calls["n"] == 3
    assert len(patch_sleep) == 2, "两次重试之间各睡一次，最后一次尝试后不再睡"


def test_plain_500_without_signature_is_not_retried(monkeypatch, patch_sleep):
    """非引擎死亡的 500（请求本身问题）重试无意义，快速失败。"""
    calls = _patch_post(monkeypatch, [_FakeResponse(500, '{"error": "invalid prompt"}')])
    r = mod.post_with_engine_retry("http://x", json={})
    assert r.status_code == 500
    assert calls["n"] == 1
    assert patch_sleep == []


def test_502_503_retried_without_signature(monkeypatch, patch_sleep):
    """网关代理看到死引擎：无签名也重试。"""
    calls = _patch_post(monkeypatch, [_FakeResponse(502, ""), _FakeResponse(200, "ok")])
    r = mod.post_with_engine_retry("http://x", json={})
    assert r.status_code == 200
    assert calls["n"] == 2


def test_400_is_not_retried(monkeypatch, patch_sleep):
    calls = _patch_post(monkeypatch, [_FakeResponse(400, "bad request")])
    r = mod.post_with_engine_retry("http://x", json={})
    assert r.status_code == 400
    assert calls["n"] == 1
    assert patch_sleep == []


def test_connection_error_is_retried(monkeypatch, patch_sleep):
    """重启窗口内端口关闭 → ConnectionError，等引擎回来。"""
    calls = _patch_post(
        monkeypatch,
        [requests.exceptions.ConnectionError("connection refused"), _FakeResponse(200, "ok")],
    )
    r = mod.post_with_engine_retry("http://x", json={})
    assert r.status_code == 200
    assert calls["n"] == 2


def test_read_timeout_is_not_retried(monkeypatch, patch_sleep):
    """ReadTimeout 维持现状不在此处重试（由任务看门狗兜底）。"""
    calls = _patch_post(monkeypatch, [requests.exceptions.ReadTimeout("read timed out")])
    with pytest.raises(requests.exceptions.ReadTimeout):
        mod.post_with_engine_retry("http://x", json={})
    assert calls["n"] == 1
    assert patch_sleep == []


def test_gives_up_after_max_attempts_returning_last_response(monkeypatch, patch_sleep):
    dead = _FakeResponse(500, "EngineDeadError")
    calls = _patch_post(monkeypatch, [dead])  # 队列耗尽后一直返回同一个
    r = mod.post_with_engine_retry("http://x", json={})
    assert r.status_code == 500
    assert calls["n"] == mod.VL_ENGINE_MAX_ATTEMPTS
    assert len(patch_sleep) == mod.VL_ENGINE_MAX_ATTEMPTS - 1


def test_connection_error_exhausted_is_raised(monkeypatch, patch_sleep):
    calls = _patch_post(
        monkeypatch, [requests.exceptions.ConnectionError("refused")]
    )
    with pytest.raises(requests.exceptions.ConnectionError):
        mod.post_with_engine_retry("http://x", json={})
    assert calls["n"] == mod.VL_ENGINE_MAX_ATTEMPTS


def test_backoff_sequence_is_bounded_and_increasing(monkeypatch, patch_sleep):
    dead = _FakeResponse(500, "EngineDeadError")
    _patch_post(monkeypatch, [dead])
    r = mod.post_with_engine_retry("http://x", json={})
    assert r.status_code == 500
    assert patch_sleep == [2, 4], "退避序列 2s → 4s，有界且递增"
