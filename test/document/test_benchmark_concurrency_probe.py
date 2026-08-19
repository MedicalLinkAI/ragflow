# -*- coding: utf-8 -*-
"""benchmark_concurrency_probe.py 纯逻辑单元测试（TDD 红灯先行）。"""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from benchmark_concurrency_probe import (  # noqa: E402
    evaluate_ladder,
    group_docs,
    pick_sample,
    resolve_group_alias,
    retry_with_backoff,
    server_window,
    timeout_rate,
)


def _doc(name, size_kb):
    return {"doc_id": name, "patient_id": "", "name": name, "size_kb": size_kb}


class TestGroupDocs:
    def test_bands(self):
        docs = [
            _doc("a", 4.9 * 1024),      # <5MB 小
            _doc("b", 5.0 * 1024),      # =5MB 中
            _doc("c", 9.9 * 1024),      # <10MB 中
            _doc("d", 10.0 * 1024),     # =10MB 大
            _doc("e", 61.5 * 1024),     # 大
            _doc("f", 0.5 * 1024),      # 小
        ]
        g = group_docs(docs)
        assert [d["name"] for d in g["小<5MB"]] == ["a", "f"]
        assert [d["name"] for d in g["中5-10MB"]] == ["b", "c"]
        assert [d["name"] for d in g["大>10MB"]] == ["d", "e"]

    def test_skip_no_size(self):
        g = group_docs([_doc("x", None), _doc("y", 1024)])
        assert [d["name"] for d in g["小<5MB"]] == ["y"]


class TestTimeoutRate:
    def test_formula(self):
        # 与 230319 轮取证口径一致：24/(3110+24)=0.77%
        assert timeout_rate(3110, 24) == pytest.approx(0.766, abs=0.001)

    def test_zero(self):
        assert timeout_rate(100, 0) == 0.0

    def test_no_calls(self):
        assert timeout_rate(0, 0) == 0.0


class TestEvaluateLadder:
    def test_stop_at_first_fail(self):
        res = evaluate_ladder([(4, 0.5), (6, 1.2), (8, 3.0)], max_rate=2.0)
        assert res["max_ok_level"] == 6
        assert res["stopped_at"] == 8

    def test_first_level_fails(self):
        res = evaluate_ladder([(4, 2.5)], max_rate=2.0)
        assert res["max_ok_level"] is None
        assert res["stopped_at"] == 4

    def test_all_ok(self):
        res = evaluate_ladder([(4, 0.1), (6, 0.2), (8, 0.3)], max_rate=2.0)
        assert res["max_ok_level"] == 8
        assert res["stopped_at"] is None

    def test_boundary_rate_is_ok(self):
        # 恰好等于阈值视为不通过（要求 < 2%）
        res = evaluate_ladder([(4, 2.0)], max_rate=2.0)
        assert res["max_ok_level"] is None


class TestServerWindow:
    def test_utc_minus_8_with_grace(self):
        s, e = server_window("2026-08-18 10:00:00", "2026-08-18 10:30:00",
                             tz_offset=8, grace_s=60)
        assert s == "2026-08-18 02:00"
        assert e == "2026-08-18 02:31"

    def test_cross_day(self):
        s, e = server_window("2026-08-18 06:00:00", "2026-08-18 06:10:00",
                             tz_offset=8, grace_s=0)
        assert s == "2026-08-17 22:00"
        assert e == "2026-08-17 22:10"


class TestPickSample:
    def test_cap_and_deterministic(self):
        docs = [_doc(f"d{i}", 1024) for i in range(20)]
        s1 = pick_sample(docs, 8, seed=7)
        s2 = pick_sample(docs, 8, seed=7)
        assert len(s1) == 8
        assert [d["name"] for d in s1] == [d["name"] for d in s2]

    def test_small_group_returns_all(self):
        docs = [_doc(f"d{i}", 1024) for i in range(3)]
        assert len(pick_sample(docs, 8, seed=1)) == 3


class TestResolveGroupAlias:
    def test_empty(self):
        assert resolve_group_alias("") == ""

    def test_chinese_full(self):
        assert resolve_group_alias("小<5MB") == "小<5MB"
        assert resolve_group_alias("中5-10MB") == "中5-10MB"
        assert resolve_group_alias("大>10MB") == "大>10MB"

    def test_english_aliases(self):
        assert resolve_group_alias("s") == "小<5MB"
        assert resolve_group_alias("small") == "小<5MB"
        assert resolve_group_alias("m") == "中5-10MB"
        assert resolve_group_alias("medium") == "中5-10MB"
        assert resolve_group_alias("l") == "大>10MB"
        assert resolve_group_alias("large") == "大>10MB"

    def test_unknown_passthrough(self):
        assert resolve_group_alias("unknown") == "unknown"


class TestRetryWithBackoff:
    def test_succeed_first_call(self, monkeypatch):
        sleeps = []
        monkeypatch.setattr("benchmark_concurrency_probe.time.sleep", lambda s: sleeps.append(s))
        assert retry_with_backoff(lambda: "ok") == "ok"
        assert sleeps == []

    def test_succeed_after_retries(self, monkeypatch):
        sleeps = []
        monkeypatch.setattr("benchmark_concurrency_probe.time.sleep", lambda s: sleeps.append(s))
        attempts = [0]

        def fn():
            attempts[0] += 1
            if attempts[0] < 3:
                raise RuntimeError("boom")
            return "ok"

        assert retry_with_backoff(fn, max_retries=3, base_delay=1.0) == "ok"
        assert attempts[0] == 3
        assert sleeps == [1.0, 2.0]

    def test_exhaust_raises_last_error(self, monkeypatch):
        sleeps = []
        monkeypatch.setattr("benchmark_concurrency_probe.time.sleep", lambda s: sleeps.append(s))

        def fn():
            raise ValueError("final")

        with pytest.raises(ValueError, match="final"):
            retry_with_backoff(fn, max_retries=2, base_delay=0.5)
        assert sleeps == [0.5]

    def test_does_not_catch_unexpected_exception(self, monkeypatch):
        sleeps = []
        monkeypatch.setattr("benchmark_concurrency_probe.time.sleep", lambda s: sleeps.append(s))

        def fn():
            raise KeyError("nope")

        with pytest.raises(KeyError):
            retry_with_backoff(fn, max_retries=3, exceptions=(RuntimeError,))
        assert sleeps == []
