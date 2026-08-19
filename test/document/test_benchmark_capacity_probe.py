# -*- coding: utf-8 -*-
"""benchmark_capacity_probe.py 纯逻辑单元测试（TDD 红灯先行）。"""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from benchmark_capacity_probe import (  # noqa: E402
    capacity_verdict,
    copy_names,
    doc_pages_from_msg,
    fmt_metrics_line,
    gen_ladder,
    makespan_ok,
    parse_case_from_name,
    parse_vllm_metrics,
    pick_batch_by_pages,
    refine_range,
    sample_docs,
    select_band,
    vlm_err_stats,
)


class TestGenLadder:
    def test_exact_cap(self):
        assert gen_ladder(4, 2, 32) == [4, 8, 16, 32]

    def test_cap_not_multiple(self):
        # 16*2=32 > 10，停在 8
        assert gen_ladder(4, 2, 10) == [4, 8]

    def test_start_above_cap_still_returns_start(self):
        assert gen_ladder(4, 2, 3) == [4]

    def test_factor_3(self):
        assert gen_ladder(2, 3, 20) == [2, 6, 18]


class TestRefineRange:
    def test_between(self):
        assert refine_range(16, 32, 4) == [20, 24, 28]

    def test_single_mid(self):
        assert refine_range(16, 32, 8) == [24]

    def test_no_room(self):
        assert refine_range(16, 20, 4) == []

    def test_excludes_endpoints(self):
        r = refine_range(8, 16, 4)
        assert 8 not in r and 16 not in r
        assert r == [12]


class TestCopyNames:
    def test_count_and_unique(self):
        names = copy_names("RRUU", 8, "n8")
        assert len(names) == 8
        assert len(set(names)) == 8

    def test_suffix_pdf(self):
        names = copy_names("RRUU", 2, "n4")
        assert all(n.endswith(".pdf") for n in names)

    def test_contains_stem_and_tag(self):
        names = copy_names("RRUU", 3, "n16")
        assert all("RRUU" in n and "n16" in n for n in names)


class TestMakespanOk:
    def test_within_budget(self):
        assert makespan_ok(0, 100, 30) is True

    def test_exactly_budget_passes(self):
        # 恰好 30 分钟 = 1800s 视为通过
        assert makespan_ok(0, 1800, 30) is True

    def test_over_budget_fails(self):
        assert makespan_ok(0, 1801, 30) is False

    def test_nonzero_start(self):
        assert makespan_ok(100, 100 + 1800, 30) is True
        assert makespan_ok(100, 100 + 1801, 30) is False


class TestCapacityVerdict:
    def test_both_ok(self):
        v = capacity_verdict(25, 1.0, 30, 2.0)
        assert v["passed"] is True

    def test_makespan_over(self):
        v = capacity_verdict(35, 1.0, 30, 2.0)
        assert v["passed"] is False
        assert "时长" in v["reason"] or "makespan" in v["reason"].lower()

    def test_rate_over(self):
        v = capacity_verdict(25, 2.5, 30, 2.0)
        assert v["passed"] is False
        assert "超时" in v["reason"]

    def test_both_over(self):
        v = capacity_verdict(35, 2.5, 30, 2.0)
        assert v["passed"] is False

    def test_rate_boundary_not_passed(self):
        # 恰好等于阈值视为不通过（要求 < 2%）
        v = capacity_verdict(25, 2.0, 30, 2.0)
        assert v["passed"] is False

    def test_makespan_boundary_passed(self):
        v = capacity_verdict(30, 1.0, 30, 2.0)
        assert v["passed"] is True


class TestSelectBand:
    """线上实档重解析模式：按大小档位从文档列表中筛选（复用 group_docs 口径）。"""

    def _doc(self, name: str, kb: float | None) -> dict:
        return {"name": name, "doc_id": name, "size_kb": kb}

    def test_small_band_boundary(self):
        # <5MB 入小档；恰好 5MB（5120KB）归中档
        docs = [self._doc("a", 5119), self._doc("b", 5120), self._doc("c", 1024)]
        got = select_band(docs, "小<5MB")
        assert [d["name"] for d in got] == ["a", "c"]

    def test_medium_band_boundaries(self):
        # [5,10)MB 归中档；恰好 10MB（10240KB）归大档
        docs = [self._doc("a", 5120), self._doc("b", 10239), self._doc("c", 10240)]
        got = select_band(docs, "中5-10MB")
        assert [d["name"] for d in got] == ["a", "b"]

    def test_large_band(self):
        docs = [self._doc("a", 10240), self._doc("b", 157696)]
        got = select_band(docs, "大>10MB")
        assert [d["name"] for d in got] == ["a", "b"]

    def test_alias_resolved(self):
        docs = [self._doc("a", 1024)]
        assert [d["name"] for d in select_band(docs, "小")] == ["a"]
        assert [d["name"] for d in select_band(docs, "small")] == ["a"]

    def test_missing_size_skipped(self):
        docs = [self._doc("a", None), self._doc("b", 0), self._doc("c", 1024)]
        got = select_band(docs, "小<5MB")
        assert [d["name"] for d in got] == ["c"]

    def test_unknown_band_raises(self):
        with pytest.raises(ValueError):
            select_band([self._doc("a", 1024)], "超大")

    def test_exclude_probe_copies(self):
        # 容量探测副本命名 <stem>_n<N>_<序号>(可选).pdf，应被排除
        docs = [
            self._doc("RRUU-男-23岁-哮喘.pdf", 4864),
            self._doc("RRUU-男-23岁-哮喘(1)_n80_080(1).pdf", 4864),
            self._doc("麦济WRNA(2)_n64_007.pdf", 12728),
            self._doc("ZGLI-男-50岁-哮喘_n4_001.pdf", 4720),
        ]
        got = select_band(docs, "小<5MB", exclude_copies=True)
        assert [d["name"] for d in got] == ["RRUU-男-23岁-哮喘.pdf"]

    def test_keep_copies_by_default(self):
        docs = [self._doc("a_n8_001.pdf", 1024), self._doc("b.pdf", 1024)]
        got = select_band(docs, "小<5MB")
        assert len(got) == 2

    def test_exclude_copies_keeps_natural_names(self):
        # 真实病例名含数字不应误伤；副本序号固定 3 位（{i:03d}），2 位序号不算
        docs = [self._doc("1_CZYO 52 2型糖尿病B160cm 58kg 广州.pdf", 1024),
                self._doc("XZGU(1)_n4_01.pdf", 1024)]
        got = select_band(docs, "小<5MB", exclude_copies=True)
        assert [d["name"] for d in got] == [
            "1_CZYO 52 2型糖尿病B160cm 58kg 广州.pdf", "XZGU(1)_n4_01.pdf"]


class TestSampleDocs:
    """跨档随机抽样：从全部原始文档（排除探测副本、跳过缺 size）中抽 n 份。"""

    def _doc(self, name: str, kb: float | None) -> dict:
        return {"name": name, "doc_id": name, "size_kb": kb}

    def _pool(self, n_small=5, n_med=3, n_large=2):
        docs = [self._doc(f"s{i}.pdf", 1024) for i in range(n_small)]
        docs += [self._doc(f"m{i}.pdf", 6144) for i in range(n_med)]
        docs += [self._doc(f"l{i}.pdf", 12288) for i in range(n_large)]
        return docs

    def test_count_and_unique(self):
        got = sample_docs(self._pool(), 6, seed=1)
        assert len(got) == 6
        assert len({d["name"] for d in got}) == 6

    def test_n_exceeds_pool_returns_all(self):
        # 样本量超过候选池时返回全部候选（线上 116 份抽 100 不会触发，防御性行为）
        got = sample_docs(self._pool(), 99, seed=1)
        assert len(got) == 10

    def test_same_seed_reproducible(self):
        # dry-run 与实跑用同一种子必须抽出同一批
        a = sample_docs(self._pool(), 5, seed=42)
        b = sample_docs(self._pool(), 5, seed=42)
        assert [d["name"] for d in a] == [d["name"] for d in b]

    def test_different_seed_differs(self):
        pool = self._pool(10, 5, 5)
        a = sample_docs(pool, 8, seed=1)
        b = sample_docs(pool, 8, seed=2)
        assert {d["name"] for d in a} != {d["name"] for d in b}

    def test_excludes_probe_copies_by_default(self):
        docs = self._pool() + [self._doc("RRUU-男-23岁-哮喘(1)_n80_080(1).pdf", 4864)]
        got = sample_docs(docs, 99, seed=1)
        assert all("_n80_080" not in d["name"] for d in got)
        assert len(got) == 10

    def test_missing_size_skipped(self):
        docs = self._pool() + [self._doc("bad.pdf", None)]
        got = sample_docs(docs, 99, seed=1)
        assert len(got) == 10
        assert all(d["name"] != "bad.pdf" for d in got)


class TestDocPagesFromMsg:
    """从 progress_msg 提取页数：Done 行优先，回退 page 行 / pages done 行。"""

    def test_done_line(self):
        msg = "15:53:16: [QwenVL] Done: 299 sections from 12 pages.\n"
        assert doc_pages_from_msg(msg) == 12

    def test_fallback_page_lines(self):
        msg = "\n".join([
            "14:33:05: [QwenVL] page 1/9 (text)",
            "14:34:15: [QwenVL] page 9/9 (text)",
        ])
        assert doc_pages_from_msg(msg) == 9

    def test_fallback_pages_done_new_format(self):
        msg = "15:53:16: [QwenVL] 12/12 pages done\n"
        assert doc_pages_from_msg(msg) == 12

    def test_empty(self):
        assert doc_pages_from_msg("") == 0
        assert doc_pages_from_msg(None) == 0


class TestPickBatchByPages:
    """按目标总页数贪心选批（seed 可复现，不超目标，余额精确补齐）。"""

    def _infos(self):
        return [{"name": f"d{i}.pdf", "pages": p}
                for i, p in enumerate([5, 3, 2, 7, 1, 4])]

    def test_exact_target(self):
        chosen, used = pick_batch_by_pages(self._infos(), 10, seed=1)
        assert used == 10
        assert sum(d["pages"] for d in chosen) == 10

    def test_never_exceeds_target(self):
        for seed in range(5):
            chosen, used = pick_batch_by_pages(self._infos(), 11, seed=seed)
            assert used <= 11

    def test_target_above_total_returns_all(self):
        chosen, used = pick_batch_by_pages(self._infos(), 100, seed=1)
        assert used == 22 and len(chosen) == 6

    def test_same_seed_reproducible(self):
        a, ua = pick_batch_by_pages(self._infos(), 10, seed=42)
        b, ub = pick_batch_by_pages(self._infos(), 10, seed=42)
        assert ua == ub
        assert [d["name"] for d in a] == [d["name"] for d in b]

    def test_zero_pages_docs_skipped(self):
        infos = self._infos() + [{"name": "bad.pdf", "pages": 0}]
        chosen, _ = pick_batch_by_pages(infos, 100, seed=1)
        assert all(d["name"] != "bad.pdf" for d in chosen)


class TestParseCaseFromName:
    """从客户侧文件名 <缩写>-<性别>-<年龄>岁-<疾病>.pdf 解析病案字段。"""

    def test_standard_name(self):
        c = parse_case_from_name("ZLME-男-66岁-胃癌.pdf")
        assert c is not None
        assert c["name_abbr"] == "ZLME"
        assert c["gender"] == "man"
        assert c["age"] == 66
        assert c["illness_label_l3"] == "胃癌"
        assert c["illness_code_l1"].endswith("000000")
        assert c["illness_code_l2"].endswith("0000")
        assert c["illness_code_l3"].endswith("00")

    def test_female(self):
        c = parse_case_from_name("XLLI-女-42岁-子宫肌瘤.pdf")
        assert c["gender"] == "woman" and c["age"] == 42

    def test_nonstandard_returns_none(self):
        # 非四段式命名无法解析病案字段
        assert parse_case_from_name("哮喘-HJCH222   2.27.pdf") is None
        assert parse_case_from_name("random.pdf") is None


class TestVlmErrStats:
    """从 progress_msg 统计超时/错误/跳过痕迹。"""

    def test_timeout_line(self):
        msg = "19:10:19: HTTPConnectionPool(host='x', port=8090): Read timed out. (read timeout=300)"
        st = vlm_err_stats(msg)
        assert st["timeouts"] == 1

    def test_error_and_failed(self):
        msg = "15:00:00: [ERROR]boom\n15:00:01: Failed to process page 3"
        st = vlm_err_stats(msg)
        assert st["errors"] >= 2

    def test_skipping(self):
        msg = "15:40:23: No chunks to process, skipping."
        assert vlm_err_stats(msg)["skipping"] == 1

    def test_clean_msg_all_zero(self):
        msg = "15:53:16: [QwenVL] Done: 299 sections from 12 pages.\n15:53:16: Done"
        st = vlm_err_stats(msg)
        assert st == {"timeouts": 0, "errors": 0, "failed_pages": 0, "skipping": 0}


SAMPLE_METRICS = """\
# HELP vllm:num_requests_running Number of requests in model execution batches.
# TYPE vllm:num_requests_running gauge
vllm:num_requests_running{engine="0",model_name="Qwen/Qwen3-VL-30B-A3B-Instruct-FP8"} 30.0
# TYPE vllm:num_requests_waiting gauge
vllm:num_requests_waiting{engine="0",model_name="Qwen/Qwen3-VL-30B-A3B-Instruct-FP8"} 0.0
# TYPE vllm:kv_cache_usage_perc gauge
vllm:kv_cache_usage_perc{engine="0",model_name="Qwen/Qwen3-VL-30B-A3B-Instruct-FP8"} 0.4508602
# TYPE vllm:generation_tokens_total counter
vllm:generation_tokens_total{engine="0",model_name="Qwen/Qwen3-VL-30B-A3B-Instruct-FP8"} 4.2421665e+07
# TYPE vllm:request_success_total counter
vllm:request_success_total{engine="0",finished_reason="stop",model_name="Qwen/Qwen3-VL-30B-A3B-Instruct-FP8"} 63184.0
# TYPE vllm:num_preemptions_total counter
vllm:num_preemptions_total{engine="0",model_name="Qwen/Qwen3-VL-30B-A3B-Instruct-FP8"} 0.0
"""


class TestParseVllmMetrics:
    """解析 vLLM /metrics Prometheus 文本为关键指标字典。"""

    def test_key_values(self):
        v = parse_vllm_metrics(SAMPLE_METRICS)
        assert v["running"] == 30.0
        assert v["waiting"] == 0.0
        assert abs(v["kv_cache"] - 0.4508602) < 1e-9
        assert v["gen_tokens"] == 4.2421665e+07
        assert v["req_success"] == 63184.0
        assert v["preemptions"] == 0.0

    def test_missing_metric_is_none(self):
        v = parse_vllm_metrics("# only comments\n")
        assert v["running"] is None
        assert v["kv_cache"] is None

    def test_multi_label_summed(self):
        # 多标签行（如 request_success 按 finished_reason 拆分）应求和
        text = ('vllm:request_success_total{finished_reason="stop"} 10.0\n'
                'vllm:request_success_total{finished_reason="length"} 5.0\n')
        assert parse_vllm_metrics(text)["req_success"] == 15.0


class TestFmtMetricsLine:
    """采样行格式化：当前值 + 与上一采样点的增量。"""

    def test_with_prev_deltas(self):
        prev = {"gen_tokens": 100.0, "req_success": 10.0}
        vals = {"running": 30.0, "waiting": 0.0, "kv_cache": 0.45,
                "gen_tokens": 260.0, "req_success": 15.0,
                "prompt_tokens": None, "req_failure": None, "preemptions": 0.0}
        line = fmt_metrics_line("15:51:23", vals, prev)
        assert "run=30" in line and "wait=0" in line
        assert "gen+160" in line          # 260-100
        assert "ok+5" in line             # 15-10

    def test_first_sample_no_prev(self):
        vals = {"running": 30.0, "waiting": 0.0, "kv_cache": 0.45,
                "gen_tokens": 100.0, "req_success": 10.0,
                "prompt_tokens": None, "req_failure": None, "preemptions": 0.0}
        line = fmt_metrics_line("15:50:53", vals, {})
        assert "run=30" in line
        assert "gen+0" in line  # 无上一采样点按 0 增量

    def test_missing_values_render_dash(self):
        vals = {"running": None, "waiting": None, "kv_cache": None,
                "gen_tokens": None, "req_success": None,
                "prompt_tokens": None, "req_failure": None, "preemptions": None}
        line = fmt_metrics_line("15:50:53", vals, {})
        assert "run=-" in line and "kv=-" in line


