#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""倍增容量探测脚本：一次提交 N 份同源同尺寸文档，找 30min 内跑完且 VLM 超时率<2% 的最大 N。

背景与口径：
- MedLinkAI upload_file 按【内容哈希】去重（Spike 已证），无法靠改文件名复制；
- 故用 PyMuPDF 给每份副本写入唯一元数据后另存，字节不同→绕过去重，页数/内容/尺寸几乎不变；
- N 按倍增阶梯递增（4,8,16,32），某档 makespan>预算 或 超时率≥阈值 即停，上一档 N 为答案；
- 可选在 (last_ok, first_fail) 间按 refine-step 等差细化逼近精确边界。

复用契约：
- benchmark_online.MedlinkaiClient：upload_file / upload / wait_status
- benchmark_concurrency_probe：server_window / ssh_count_vlm / timeout_rate / retry_with_backoff

约束：只触发上传+解析与只读日志取证；服务器零写操作；不重启服务。

用法:
    python benchmark_capacity_probe.py --source-pdf D:\\dowload\\RRUU-男-23岁-哮喘(1).pdf --dry-run
    python benchmark_capacity_probe.py --source-pdf <path> --levels 4,8,16,32
    python benchmark_capacity_probe.py --customer-pages 350 --seed 350 [--dry-run]
    python benchmark_capacity_probe.py --customer-pages 400 --seed 400 --in-customer-env [--dry-run]
      （--in-customer-env：同一混合选批流程，压测目标环境切到客户现场，源/目标同环境重解析）
    python benchmark_capacity_probe.py --reparse-plan <上轮capacity_result_full.json> --max-wait 5400 [--dry-run]
      （存量文档重解析：不删不传，对客户环境现存文档触发 reparse，makespan 以终态时间戳为准）

vLLM 监控（全模式通用）：
- 默认每 30s 采样 --metrics-url（vLLM Prometheus /metrics），轨迹写 <结果目录>/vllm_monitor_trace.txt；
- --metrics-interval 0 关闭监控；dry-run 不监控。
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from benchmark_online import MedlinkaiClient  # noqa: E402
from benchmark_concurrency_probe import (  # noqa: E402
    BAND_NAMES,
    group_docs,
    resolve_group_alias,
    retry_with_backoff,
    server_window,
    ssh_count_vlm,
    timeout_rate,
)

DEFAULT_SSH_KEY = r"C:\Users\James Lu\.ssh\id_ed25519_futurefab_lsc"
DEFAULT_ASKPASS = str(Path(__file__).resolve().parents[3] / "askpass.bat")
DEFAULT_METRICS_URL = "http://10.16.3.16:8090/metrics"


# ══════════════════════════════════════════════════════════════════
# 纯逻辑（单元测试覆盖）
# ══════════════════════════════════════════════════════════════════


def gen_ladder(start: int, factor: int, cap: int) -> list[int]:
    """倍增阶梯：start, start*factor, ... 直到 <= cap；至少返回 [start]。"""
    ladder: list[int] = []
    v = start
    while v <= cap:
        ladder.append(v)
        v *= factor
    if not ladder:
        ladder.append(start)
    return ladder


def build_auth_headers(api_key: str, basic_auth: str) -> tuple[dict, tuple | None]:
    """构造 requests 凭据：X-Api-Key 头 + Basic Auth 元组（与 MedlinkaiClient 同契约）。"""
    headers: dict = {}
    if api_key:
        headers["X-Api-Key"] = api_key
    auth = tuple(basic_auth.split(":", 1)) if basic_auth and ":" in basic_auth else None
    return headers, auth


def resolve_target_env(args: argparse.Namespace) -> tuple[str, str]:
    """解析压测目标环境：--in-customer-env 直指客户现场（源/目标同环境重解析），
    否则默认 medlinkai 目标。返回 (base, dataset_id)。"""
    if getattr(args, "in_customer_env", False):
        return args.customer_base.rstrip("/"), args.customer_dataset
    return args.medlinkai_base.rstrip("/"), args.dataset_id


def load_reparse_plan(path: Path | str) -> tuple[list[dict], dict]:
    """从上一轮 capacity_result_full.json 读取存量文档重解析清单（不重新上传）。

    返回 (plan[{doc_id,name,pages}], meta{n,total_pages,source})；
    文件不存在或无有效 docs 抛 ValueError。"""
    p = Path(path)
    if not p.exists():
        raise ValueError(f"重解析清单不存在: {p}")
    data = json.loads(p.read_text(encoding="utf-8"))
    docs = data.get("docs")
    if not docs:
        raise ValueError(f"清单无 docs 条目: {p}")
    plan = [{"doc_id": d["doc_id"], "name": d.get("name"), "pages": d.get("pages") or 0}
            for d in docs if d.get("doc_id")]
    if not plan:
        raise ValueError(f"清单无有效 doc_id 条目: {p}")
    meta = {"source": str(p), "n": len(plan),
            "total_pages": sum(x["pages"] for x in plan)}
    return plan, meta


def parse_doc_update_epoch(s: str | None) -> float | None:
    """解析文档 update_date（UTC，如 2026-08-21T11:34:04）为 epoch；非法/空返回 None。

    用于真实终态 makespan（轮询窗口可能早于大文档实际完成）。"""
    if not s:
        return None
    try:
        dt = datetime.strptime(s[:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)
        return dt.timestamp()
    except ValueError:
        return None


def refine_range(lo: int, hi: int, step: int) -> list[int]:
    """在 (lo, hi) 开区间内按 step 等差生成细化档（不含端点）。"""
    out: list[int] = []
    v = lo + step
    while v < hi:
        out.append(v)
        v += step
    return out


def copy_names(stem: str, n: int, round_tag: str) -> list[str]:
    """生成 N 个唯一副本文件名：<stem>_<round_tag>_<序号>.pdf。"""
    return [f"{stem}_{round_tag}_{i:03d}.pdf" for i in range(1, n + 1)]


def makespan_ok(start_ts: float, end_ts: float, budget_min: float) -> bool:
    """makespan（秒）<= 预算分钟即通过；恰好等于预算视为通过。"""
    return (end_ts - start_ts) <= budget_min * 60


def capacity_verdict(makespan_min: float, rate: float,
                     budget_min: float, max_rate: float) -> dict:
    """双约束判定：makespan<=预算 且 超时率<阈值 才通过。"""
    reasons: list[str] = []
    if makespan_min > budget_min:
        reasons.append(f"总时长 {makespan_min:.1f}min 超预算 {budget_min}min")
    if rate >= max_rate:
        reasons.append(f"VLM 超时率 {rate:.2f}% ≥ 阈值 {max_rate}%")
    return {"passed": not reasons, "reason": "；".join(reasons) if reasons else "通过"}


def select_band(docs: list[dict], band: str, exclude_copies: bool = False) -> list[dict]:
    """按档位（小<5MB / 中5-10MB / 大>10MB）从文档列表筛选；未知档位报错。

    exclude_copies=True 时排除容量探测产生的变异副本（<stem>_n<N>_<3位序号>…）。
    """
    name = resolve_group_alias(band)
    if name not in BAND_NAMES:
        raise ValueError(f"未知档位: {band}")
    picked = group_docs(docs)[name]
    if exclude_copies:
        picked = [d for d in picked
                  if not re.search(r"_n\d+_\d{3}[^/]*\.pdf$", d.get("name") or "")]
    return picked


def sample_docs(docs: list[dict], n: int, exclude_copies: bool = True,
                seed: int = 0) -> list[dict]:
    """跨档随机抽样：从全部有效文档（有 size_kb）中随机抽 n 份。

    - exclude_copies=True（默认）排除容量探测变异副本；
    - n 超过候选池时返回全部候选；
    - 同一种子结果可复现（dry-run 与实跑同批）。
    """
    import random
    pool = [d for d in docs if d.get("size_kb")]
    if exclude_copies:
        pool = [d for d in pool
                if not re.search(r"_n\d+_\d{3}[^/]*\.pdf$", d.get("name") or "")]
    rng = random.Random(seed)
    k = min(n, len(pool))
    return rng.sample(pool, k)


RE_VL_DONE = re.compile(r"\[QwenVL\] Done: \d+ sections from (\d+) pages")
RE_VL_PAGES_DONE = re.compile(r"\[QwenVL\] \d+/(\d+) pages done")
RE_VL_PAGE = re.compile(r"\[QwenVL\] page \d+/(\d+)")


def doc_pages_from_msg(msg: str | None) -> int:
    """从 progress_msg 提取文档页数：Done 行优先，回退 pages done / page N/M 行取最大值。"""
    if not msg:
        return 0
    m = RE_VL_DONE.search(msg)
    if m:
        return int(m.group(1))
    nums = [int(x) for x in RE_VL_PAGES_DONE.findall(msg)]
    nums += [int(x) for x in RE_VL_PAGE.findall(msg)]
    return max(nums) if nums else 0


def _subset_sum_pick(pool: list[dict], target: int) -> list[dict]:
    """子集和 DP：在 pool 中选子集使总页数最大且 <= target（可重建具体子集）。"""
    prev = [-2] + [-1] * target  # prev[s] = 到达页数 s 所用的文档下标；-2=起点，-1=不可达
    for i, d in enumerate(pool):
        p = d["pages"]
        if p > target:
            continue
        for s in range(target - p, -1, -1):
            if prev[s] != -1 and prev[s + p] == -1:
                prev[s + p] = i
    best_s = max(s for s in range(target + 1) if prev[s] != -1)
    picked: list[dict] = []
    s = best_s
    while s > 0:
        i = prev[s]
        picked.append(pool[i])
        s -= pool[i]["pages"]
    return picked


def pick_batch_by_pages(infos: list[dict], target: int,
                        seed: int = 0, max_doc_pages: int = 0) -> tuple[list[dict], int]:
    """按目标总页数选批：种子洗牌后贪心累加（不超目标），贪心未精确命中时用子集和 DP 补齐。

    返回 (选中列表, 实际总页数)；页数<=0 的文档跳过；总页数不足目标时返回全部有效文档。
    max_doc_pages>0 时排除页数超上限的文档（防长尾超大档钉死 makespan）。
    """
    import random
    pool = [d for d in infos if (d.get("pages") or 0) > 0]
    if max_doc_pages > 0:
        pool = [d for d in pool if d["pages"] <= max_doc_pages]
    total = sum(d["pages"] for d in pool)
    if total <= target:
        return pool, total
    rng = random.Random(seed)
    order = pool[:]
    rng.shuffle(order)
    chosen: list[dict] = []
    used = 0
    for d in order:
        if used + d["pages"] <= target:
            chosen.append(d)
            used += d["pages"]
    if used == target:
        return chosen, used
    best = _subset_sum_pick(pool, target)
    bsum = sum(d["pages"] for d in best)
    return (best, bsum) if bsum > used else (chosen, used)


# 病案编码映射（来自客户现场 dataset 实测值，供文件名解析兜底）
ILLNESS_MAP: dict[str, tuple] = {
    "哮喘": ("1000000", "慢病", "1001000", "呼吸疾病", "1001001", "哮喘"),
    "慢性阻塞性肺疾病": ("1000000", "慢病", "1001000", "呼吸系统疾病", "1001002", "慢性阻塞性肺疾病"),
    "糖尿病": ("1000000", "慢病", "1004000", "内分泌疾病", "1004007", "糖尿病"),
    "痛风": ("1000000", "慢病", "1004000", "内分泌疾病", "1004005", "痛风"),
    "类风湿关节炎": ("1000000", "慢病", "1005000", "风湿免疫疾病", "1005002", "类风湿关节炎"),
    "特异性性皮炎（AD)": ("1000000", "慢病", "1006000", "皮肤病", "1006006", "特异性性皮炎（AD)"),
    "黄斑变性": ("1000000", "慢病", "1015000", "眼科疾病", "1015004", "黄斑变性"),
    "肺癌": ("2000000", "肿瘤", "2001000", "胸部", "2001001", "肺癌"),
    "肺腺癌": ("2000000", "肿瘤", "2001000", "胸部", "2001006", "肺腺癌"),
    "非小细胞肺癌": ("2000000", "肿瘤", "2001000", "胸部", "2001004", "非小细胞肺癌"),
    "乳腺癌": ("2000000", "肿瘤", "2001000", "胸部", "2001003", "乳腺癌"),
    "胃癌": ("2000000", "肿瘤", "2002000", "消化道", "2002001", "胃癌"),
    "食管癌": ("2000000", "肿瘤", "2002000", "消化道", "2002003", "食管癌"),
    "结直肠癌": ("2000000", "肿瘤", "2002000", "消化道", "2002016", "结直肠癌"),
    "胰腺癌": ("2000000", "肿瘤", "2003000", "肝胆胰", "2003003", "胰腺癌"),
    "肾细胞癌": ("2000000", "肿瘤", "2005000", "泌尿", "2005001", "肾细胞癌"),
    "子宫肌瘤": ("2000000", "肿瘤", "2006000", "女性", "2006006", "子宫肌瘤"),
    "甲状腺髓样癌": ("2000000", "肿瘤", "2007000", "头颈", "2007002", "甲状腺髓样癌"),
    "转移性骨肿瘤": ("2000000", "肿瘤", "2010000", "骨与软组织", "2010009", "转移性骨肿瘤"),
}
RE_CASE_NAME = re.compile(r"^(?P<abbr>[A-Za-z0-9]+)-(?P<gender>男|女)-(?P<age>\d+)岁-(?P<disease>.+)\.pdf$")


def parse_case_from_name(filename: str) -> dict | None:
    """从客户侧文件名 <缩写>-<性别>-<年龄>岁-<疾病>.pdf 解析病案字段；非四段式返回 None。

    未知疾病回退哮喘编码（label 用原疾病名），保证上传表单字段合法。
    """
    m = RE_CASE_NAME.match(filename or "")
    if not m:
        return None
    disease = m.group("disease")
    codes = ILLNESS_MAP.get(disease) or ("1000000", "慢病", "1001000", "呼吸疾病", "1001001", disease)
    return {
        "name_abbr": m.group("abbr"),
        "gender": "man" if m.group("gender") == "男" else "woman",
        "age": int(m.group("age")),
        "illness_code_l1": codes[0], "illness_label_l1": codes[1],
        "illness_code_l2": codes[2], "illness_label_l2": codes[3],
        "illness_code_l3": codes[4], "illness_label_l3": codes[5],
    }


RE_TIMEOUT_LINE = re.compile(r"timed\s*out|timeout", re.I)
RE_ERR_LINE = re.compile(r"\[ERROR\]|Failed to process|Traceback", re.I)
RE_FAILED_PAGE = re.compile(r"Failed to process page", re.I)
RE_SKIPPING = re.compile(r"skipping", re.I)


def vlm_err_stats(msg: str | None) -> dict:
    """从 progress_msg 逐行统计超时/错误/失败页/跳过痕迹。"""
    st = {"timeouts": 0, "errors": 0, "failed_pages": 0, "skipping": 0}
    if not msg:
        return st
    for ln in msg.splitlines():
        if RE_TIMEOUT_LINE.search(ln):
            st["timeouts"] += 1
        if RE_ERR_LINE.search(ln):
            st["errors"] += 1
        if RE_FAILED_PAGE.search(ln):
            st["failed_pages"] += 1
        if RE_SKIPPING.search(ln):
            st["skipping"] += 1
    return st


VLLM_METRIC_KEYS = {
    "vllm:num_requests_running": "running",
    "vllm:num_requests_waiting": "waiting",
    "vllm:kv_cache_usage_perc": "kv_cache",
    "vllm:prompt_tokens_total": "prompt_tokens",
    "vllm:generation_tokens_total": "gen_tokens",
    "vllm:request_success_total": "req_success",
    "vllm:request_failure_total": "req_failure",
    "vllm:num_preemptions_total": "preemptions",
}
RE_METRIC_LINE = re.compile(r"^(vllm:\w+)\{[^}]*\}\s+([-+0-9.eE]+)\s*$")


def parse_vllm_metrics(text: str) -> dict:
    """解析 vLLM /metrics Prometheus 文本为关键指标字典；缺失指标为 None，同名多行求和。"""
    vals: dict = {k: None for k in VLLM_METRIC_KEYS.values()}
    if not text:
        return vals
    for ln in text.splitlines():
        if ln.startswith("#"):
            continue
        m = RE_METRIC_LINE.match(ln)
        if not m or m.group(1) not in VLLM_METRIC_KEYS:
            continue
        try:
            v = float(m.group(2))
        except ValueError:
            continue
        key = VLLM_METRIC_KEYS[m.group(1)]
        vals[key] = v if vals[key] is None else vals[key] + v
    return vals


def fmt_metrics_line(ts: str, vals: dict, prev: dict | None = None) -> str:
    """格式化单条监控采样行：瞬时值 + 与上一采样点的增量（无上一采样点按 0）。"""
    prev = prev or {}

    def cur(k: str) -> str:
        v = vals.get(k)
        return "-" if v is None else f"{v:.0f}"

    def cur3(k: str) -> str:
        v = vals.get(k)
        return "-" if v is None else f"{v:.3f}"

    def delta(k: str) -> float:
        # 首采样（prev 无该键）无法算增量，按 0 处理
        if k not in prev:
            return 0.0
        return (vals.get(k) or 0) - (prev.get(k) or 0)

    return (f"{ts} run={cur('running')} wait={cur('waiting')} kv={cur3('kv_cache')} "
            f"prompt+{delta('prompt_tokens'):.0f} gen+{delta('gen_tokens'):.0f} "
            f"ok+{delta('req_success'):.0f} fail+{delta('req_failure'):.0f} "
            f"req_ok={cur('req_success')} preemp={cur('preemptions')}")


# ══════════════════════════════════════════════════════════════════
# vLLM 指标监控（后台线程定期采样 /metrics，等价 curl -s <url> | grep vllm）
# ══════════════════════════════════════════════════════════════════


class MetricsMonitor:
    """后台线程每 interval 秒采样 vLLM /metrics，逐行写入轨迹文件并打印。

    用法：mon = MetricsMonitor(url, trace_path, 30); mon.start()
          … 压测结束后 … mon.stop()
    """

    def __init__(self, url: str, trace_path: Path, interval: float = 30.0):
        self.url = url
        self.trace_path = Path(trace_path)
        self.interval = interval
        self._stop = threading.Event()
        self._thread: threading.Thread | None = None

    def start(self) -> None:
        self.trace_path.parent.mkdir(parents=True, exist_ok=True)
        self._thread = threading.Thread(target=self._loop, daemon=True,
                                        name="vllm-metrics-monitor")
        self._thread.start()
        print(f"[vLLM 监控] {self.url}  每 {self.interval:.0f}s 采样 → {self.trace_path.name}")

    def _loop(self) -> None:
        prev: dict | None = None
        with open(self.trace_path, "a", encoding="utf-8") as f:
            while not self._stop.is_set():
                line = None
                try:
                    r = requests.get(self.url, timeout=10)
                    vals = parse_vllm_metrics(r.text)
                    ts = time.strftime("%H:%M:%S")
                    line = fmt_metrics_line(ts, vals, prev)
                    prev = vals
                except Exception as e:  # noqa: BLE001
                    line = f"{time.strftime('%H:%M:%S')} [采样失败] {e}"
                f.write(line + "\n")
                f.flush()
                print(f"[vLLM] {line}", flush=True)
                self._stop.wait(self.interval)

    def stop(self) -> None:
        self._stop.set()
        if self._thread:
            self._thread.join(timeout=self.interval + 15)


def start_metrics_monitor(args: argparse.Namespace, out: Path) -> MetricsMonitor | None:
    """按参数启动监控；interval<=0 或 dry-run 时返回 None。"""
    if args.metrics_interval <= 0 or not args.metrics_url or args.dry_run:
        return None
    mon = MetricsMonitor(args.metrics_url, out / "vllm_monitor_trace.txt",
                         args.metrics_interval)
    mon.start()
    return mon


def stop_metrics_monitor(mon: MetricsMonitor | None) -> None:
    if mon:
        mon.stop()
        print(f"[vLLM 监控] 已停止，轨迹: {mon.trace_path}")


# ══════════════════════════════════════════════════════════════════
# PDF 变异（绕过内容哈希去重）
# ══════════════════════════════════════════════════════════════════


def mutate_copies(source: Path, names: list[str], out_dir: Path) -> list[Path]:
    """把源 PDF 逐份写入唯一元数据另存为 names，返回本地路径列表。"""
    import fitz  # PyMuPDF，延迟导入避免纯逻辑测试依赖
    out_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    for idx, name in enumerate(names, 1):
        doc = fitz.open(source)
        doc.set_metadata({"title": f"capacity_probe_{name}",
                          "producer": f"capacity-probe-{idx}"})
        out = out_dir / name
        doc.save(out)
        doc.close()
        paths.append(out)
    return paths


# ══════════════════════════════════════════════════════════════════
# 单轮容量探测（上传 N 份 → 并发轮询终态 → SSH 取证 → 判定）
# ══════════════════════════════════════════════════════════════════


def build_case(args: argparse.Namespace, name_abbr: str) -> dict:
    return {
        "name_abbr": name_abbr,
        "gender": args.gender,
        "age": args.age,
        "illness_code_l1": args.illness_code_l1,
        "illness_label_l1": args.illness_label_l1,
        "illness_code_l2": args.illness_code_l2,
        "illness_label_l2": args.illness_label_l2,
        "illness_code_l3": args.illness_code_l3,
        "illness_label_l3": args.illness_label_l3,
    }


def upload_one(args: argparse.Namespace, mla: MedlinkaiClient,
               pdf_path: Path, name_abbr: str) -> dict:
    """上传单份：upload_file（取 doc_id）→ upload（带病案字段触发解析）。"""
    rep = {"name": pdf_path.name, "doc_id": None, "note": ""}
    try:
        step_a = retry_with_backoff(lambda: mla.upload_file(pdf_path),
                                    max_retries=args.submit_retries,
                                    base_delay=args.submit_retry_delay)
        if step_a.get("duplicate"):
            rep["note"] = "duplicate(内容哈希) " + step_a.get("message", "")[:60]
            return rep
        doc_id = step_a.get("doc_id")
        rep["doc_id"] = doc_id
        retry_with_backoff(lambda: mla.upload(doc_id, build_case(args, name_abbr)),
                           max_retries=args.submit_retries,
                           base_delay=args.submit_retry_delay)
    except Exception as e:  # noqa: BLE001
        rep["note"] = f"upload error: {e}"
    return rep


def wait_one(args: argparse.Namespace, mla: MedlinkaiClient, doc_id: str) -> dict:
    """轮询单文档至终态，返回 (run, note)。"""
    try:
        status, note = mla.wait_status(doc_id, args.max_wait,
                                       args.poll_interval, wait_running=True)
        return {"run": (status or {}).get("run"), "note": note}
    except Exception as e:  # noqa: BLE001
        return {"run": None, "note": f"wait error: {e}"}


def run_capacity_round(args: argparse.Namespace, mla: MedlinkaiClient,
                       n: int, source: Path, stem: str,
                       copies_dir: Path) -> dict:
    tag = f"n{n}"
    names = copy_names(stem, n, tag)
    print(f"\n[容量 N={n}] 生成 {n} 份变异副本 …")
    paths = mutate_copies(source, names, copies_dir)

    t0_epoch = time.time()
    t0 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 错峰上传
    uploads: list[dict] = []
    for i, p in enumerate(paths):
        if i and args.submit_stagger > 0:
            time.sleep(args.submit_stagger)
        name_abbr = f"CAP{tag.upper()}{i + 1:02d}"
        rep = upload_one(args, mla, p, name_abbr)
        uploads.append(rep)
        flag = "ok" if rep["doc_id"] and not rep["note"].startswith("duplicate") else "SKIP"
        print(f"  [上传 {flag}] {rep['name']} → {rep['doc_id']} {rep['note'][:50]}")

    doc_ids = [u["doc_id"] for u in uploads if u["doc_id"]]
    if not doc_ids:
        return {"n": n, "error": "无成功上传", "passed": False, "reason": "无成功上传"}

    # 并发轮询所有文档至终态
    print(f"[容量 N={n}] 已上传 {len(doc_ids)}/{n}，并发轮询终态 …")
    poll_client = MedlinkaiClient(args.medlinkai_base, args.dataset_id, args.page_size,
                                  api_key=args.api_key, basic_auth=args.basic_auth)
    with ThreadPoolExecutor(max_workers=max(len(doc_ids), 1)) as ex:
        futs = {ex.submit(wait_one, args, poll_client, d): d for d in doc_ids}
        results = {d: f.result() for f, d in futs.items()}

    t1_epoch = time.time()
    t1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    makespan_min = (t1_epoch - t0_epoch) / 60.0
    done = sum(1 for r in results.values() if r["run"] == "DONE")

    s, e = server_window(t0, t1, args.tz_offset, args.grace)
    starts, timeouts = ssh_count_vlm(args, s, e)
    rate = timeout_rate(starts, timeouts)
    verdict = capacity_verdict(makespan_min, rate, args.budget_min, args.max_timeout_rate)

    print(f"[容量 N={n}] makespan {makespan_min:.1f}min  DONE {done}/{len(doc_ids)}  "
          f"VLM 尝试 {starts} 超时 {timeouts} → 超时率 {rate:.2f}%  "
          f"{'✅通过' if verdict['passed'] else '❌未过'} {'' if verdict['passed'] else verdict['reason']}")

    return {"n": n, "makespan_min": round(makespan_min, 2), "done": done,
            "total": len(doc_ids), "starts": starts, "timeouts": timeouts,
            "rate": round(rate, 3), "passed": verdict["passed"],
            "reason": verdict["reason"], "window": [s, e]}


# ══════════════════════════════════════════════════════════════════
# 线上实档重解析轮次（按档位筛选现存文档 → 一次性全触发 → 全并发轮询）
# ══════════════════════════════════════════════════════════════════


def list_all_docs(mla: MedlinkaiClient, page_size: int) -> list[dict]:
    """分页拉取线上文档列表全量。"""
    docs: list[dict] = []
    page = 1
    while True:
        batch = mla.list_docs(page=page, page_size=page_size)
        docs.extend(batch)
        if len(batch) < page_size:
            break
        page += 1
    return docs


def run_reparse_round(args: argparse.Namespace, mla: MedlinkaiClient,
                      band: str, picked: list[dict] | None = None,
                      label: str | None = None) -> dict:
    """按档位选档内全部现存文档（或外部传入 picked），错峰触发 reparse 后全并发轮询终态。"""
    docs = list_all_docs(mla, args.page_size)
    if picked is None:
        picked = select_band(docs, band, exclude_copies=not args.include_copies)
    band_name = label or resolve_group_alias(band)
    print(f"\n[实档重解析 {band_name}] 线上共 {len(docs)} 份，档内 {len(picked)} 份，全部触发 reparse …")
    if not picked:
        return {"band": band_name, "error": "档内无文档", "passed": False, "reason": "档内无文档"}

    t0_epoch = time.time()
    t0 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    triggered: list[dict] = []
    for i, d in enumerate(picked):
        if i and args.submit_stagger > 0:
            time.sleep(args.submit_stagger)
        rep = {"name": d.get("name"), "doc_id": d.get("doc_id"), "note": ""}
        try:
            retry_with_backoff(lambda did=d["doc_id"]: mla.trigger_parse(did),
                               max_retries=args.submit_retries,
                               base_delay=args.submit_retry_delay)
        except Exception as e:  # noqa: BLE001
            rep["note"] = f"trigger error: {e}"
        triggered.append(rep)
        print(f"  [触发 {'ok' if not rep['note'] else 'SKIP'}] {rep['name']} {rep['note'][:50]}")

    doc_ids = [t["doc_id"] for t in triggered if t["doc_id"] and not t["note"]]
    if not doc_ids:
        return {"band": band_name, "error": "无成功触发", "passed": False, "reason": "无成功触发"}

    print(f"[实档重解析 {band_name}] 已触发 {len(doc_ids)}/{len(picked)}，全并发轮询终态 …")
    poll_client = MedlinkaiClient(args.medlinkai_base, args.dataset_id, args.page_size,
                                  api_key=args.api_key, basic_auth=args.basic_auth)
    with ThreadPoolExecutor(max_workers=max(len(doc_ids), 1)) as ex:
        futs = {ex.submit(wait_one, args, poll_client, d): d for d in doc_ids}
        results = {d: f.result() for f, d in futs.items()}

    t1_epoch = time.time()
    t1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    makespan_min = (t1_epoch - t0_epoch) / 60.0
    done = sum(1 for r in results.values() if r["run"] == "DONE")

    s, e = server_window(t0, t1, args.tz_offset, args.grace)
    starts, timeouts = ssh_count_vlm(args, s, e)
    rate = timeout_rate(starts, timeouts)
    verdict = capacity_verdict(makespan_min, rate, args.budget_min, args.max_timeout_rate)

    print(f"[实档重解析 {band_name}] makespan {makespan_min:.1f}min  DONE {done}/{len(doc_ids)}  "
          f"VLM 尝试 {starts} 超时 {timeouts} → 超时率 {rate:.2f}%  "
          f"{'✅通过' if verdict['passed'] else '❌未过'} {'' if verdict['passed'] else verdict['reason']}")

    fails = {d: r["note"] for d, r in results.items() if r["run"] != "DONE"}
    return {"band": band_name, "n": len(doc_ids), "makespan_min": round(makespan_min, 2),
            "done": done, "total": len(doc_ids), "starts": starts, "timeouts": timeouts,
            "rate": round(rate, 3), "passed": verdict["passed"], "reason": verdict["reason"],
            "window": [s, e], "not_done": fails,
            "docs": [{"name": t["name"], "doc_id": t["doc_id"],
                      "run": (results.get(t["doc_id"]) or {}).get("run"),
                      "note": (results.get(t["doc_id"]) or {}).get("note", "")}
                     for t in triggered if t["doc_id"]]}


# ══════════════════════════════════════════════════════════════════
# 客户现场真实文档压测（选批 → download → 删同名旧副本 → 全新上传立即解析）
# ══════════════════════════════════════════════════════════════════


def fetch_customer_docs(base: str, dataset_id: str, page_size: int = 100,
                        headers: dict | None = None,
                        auth: tuple | None = None) -> list[dict]:
    """分页拉取客户现场 dataset 全量文档列表（只读）。"""
    docs: list[dict] = []
    page = 1
    while True:
        r = requests.get(f"{base}/api/v1/documents",
                         params={"page": page, "page_size": page_size,
                                 "dataset_id": dataset_id},
                         headers=headers or {}, auth=auth, timeout=60)
        r.raise_for_status()
        batch = r.json().get("documents", [])
        docs.extend(batch)
        if len(batch) < page_size:
            break
        page += 1
    return docs


def build_customer_infos(docs: list[dict]) -> tuple[list[dict], int]:
    """客户文档 → 选批信息（pages 从 progress_msg 提取，病案字段列表优先、文件名兜底）。"""
    infos: list[dict] = []
    no_pages = 0
    for d in docs:
        pages = doc_pages_from_msg(d.get("progress_msg"))
        if pages <= 0:
            no_pages += 1
            continue
        case = {k: d.get(k) for k in ("name_abbr", "gender", "age",
                                      "illness_code_l1", "illness_label_l1",
                                      "illness_code_l2", "illness_label_l2",
                                      "illness_code_l3", "illness_label_l3")}
        if not all(case.values()):
            case = parse_case_from_name(d.get("name") or "") or case
        infos.append({"doc_id": d.get("doc_id"), "name": d.get("name"),
                      "pages": pages, "size": d.get("size") or 0, "case": case})
    return infos, no_pages


def normalize_pdf_bytes(data: bytes) -> bytes | None:
    """清洗下载内容：部分响应因分块传输在 %PDF 魔数前带少量空白/CRLF。

    魔数前垃圾超过 1KB 视为异常内容返回 None。
    """
    if not data:
        return None
    idx = data.find(b"%PDF")
    if idx < 0 or idx > 1024:
        return None
    return data[idx:]


def download_customer_pdf(base: str, doc_id: str, dest: Path,
                          headers: dict | None = None,
                          auth: tuple | None = None) -> Path:
    """经客户侧 /download 接口下载单份 PDF，校验 %PDF 魔数后落盘。"""
    r = requests.get(f"{base}/api/v1/documents/{doc_id}/download",
                     headers=headers or {}, auth=auth,
                     timeout=(30, 600), stream=True)
    r.raise_for_status()
    data = normalize_pdf_bytes(r.content)
    if data is None:
        raise ValueError(f"返回内容非 PDF（{r.content[:8]!r}）")
    dest.write_bytes(data)
    return dest


def run_customer_round(args: argparse.Namespace, mla: MedlinkaiClient,
                       chosen: list[dict], pdf_dir: Path) -> dict:
    """删测试环境同名旧副本 → 全新两阶段上传（成功即触发解析）→ 全并发轮询终态。"""
    # 1. 删同名旧副本（压测批次从干净状态开始；其余历史副本不动）
    existing = list_all_docs(mla, args.page_size)
    by_name: dict[str, list[dict]] = {}
    for x in existing:
        by_name.setdefault(x.get("name"), []).append(x)
    removed = 0
    for d in chosen:
        for x in by_name.get(d["name"], []):
            try:
                if mla.delete_document(x["doc_id"]):
                    removed += 1
            except Exception as e:  # noqa: BLE001
                print(f"  [删旧失败] {d['name']}: {e}")
    print(f"[客户压测] 已删除同名旧副本 {removed} 份")

    # 2. 全新上传：Step A upload_file → Step B upload（上传成功即开始解析）
    t0_epoch = time.time()
    t0 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    uploads: list[dict] = []
    for i, d in enumerate(chosen):
        if i and args.submit_stagger > 0:
            time.sleep(args.submit_stagger)
        rep = {"name": d["name"], "doc_id": None, "pages": d["pages"], "note": ""}
        pdf = pdf_dir / d["name"]
        try:
            step_a = retry_with_backoff(lambda: mla.upload_file(pdf),
                                        max_retries=args.submit_retries,
                                        base_delay=args.submit_retry_delay)
            if step_a.get("duplicate"):
                old_id = step_a.get("doc_id")
                if old_id:
                    mla.delete_document(old_id)  # 同内容哈希旧档：删后重传
                step_a = retry_with_backoff(lambda: mla.upload_file(pdf),
                                            max_retries=args.submit_retries,
                                            base_delay=args.submit_retry_delay)
            doc_id = step_a.get("doc_id")
            rep["doc_id"] = doc_id
            if doc_id:
                retry_with_backoff(lambda: mla.upload(doc_id, d["case"]),
                                   max_retries=args.submit_retries,
                                   base_delay=args.submit_retry_delay)
        except Exception as e:  # noqa: BLE001
            rep["note"] = f"upload error: {e}"
        uploads.append(rep)
        print(f"  [上传 {'ok' if rep['doc_id'] and not rep['note'] else 'SKIP'}] "
              f"{rep['name']} {rep['doc_id']} {rep['note'][:60]}")

    doc_ids = [u["doc_id"] for u in uploads if u["doc_id"] and not u["note"]]
    if not doc_ids:
        return {"error": "无成功上传", "passed": False, "reason": "无成功上传"}
    up_sec = time.time() - t0_epoch

    # 3. 全并发轮询终态
    print(f"[客户压测] 上传 {len(doc_ids)}/{len(chosen)}（{up_sec:.0f}s），并发轮询终态 …")
    poll_client = MedlinkaiClient(args.medlinkai_base, args.dataset_id, args.page_size,
                                  api_key=args.api_key, basic_auth=args.basic_auth)
    with ThreadPoolExecutor(max_workers=max(len(doc_ids), 1)) as ex:
        futs = {ex.submit(wait_one, args, poll_client, d): d for d in doc_ids}
        results = {d: f.result() for f, d in futs.items()}

    t1_epoch = time.time()
    t1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    makespan_min = (t1_epoch - t0_epoch) / 60.0
    done = sum(1 for r in results.values() if r["run"] == "DONE")

    # 4. progress_msg 取证：超时/错误统计（客户侧口径，不依赖 SSH）
    final_docs = {x.get("doc_id"): x for x in list_all_docs(mla, args.page_size)}
    agg = {"timeouts": 0, "errors": 0, "failed_pages": 0, "skipping": 0}
    doc_details: list[dict] = []
    for u in uploads:
        fin = final_docs.get(u["doc_id"]) or {}
        msg = fin.get("progress_msg") or ""
        st = vlm_err_stats(msg)
        for k in agg:
            agg[k] += st[k]
        doc_details.append({"name": u["name"], "doc_id": u["doc_id"],
                            "pages": u["pages"],
                            "run": (results.get(u["doc_id"]) or {}).get("run"),
                            "note": (results.get(u["doc_id"]) or {}).get("note", ""),
                            "err": st, "progress_msg": msg})
    total_pages = sum(u["pages"] for u in uploads if u["doc_id"])
    rate = agg["timeouts"] * 100.0 / max(total_pages, 1)
    verdict = capacity_verdict(makespan_min, rate, args.budget_min, args.max_timeout_rate)

    print(f"[客户压测] makespan {makespan_min:.1f}min  DONE {done}/{len(doc_ids)}  "
          f"总页数 {total_pages}  超时行 {agg['timeouts']} → 超时率 {rate:.2f}%  "
          f"{'✅通过' if verdict['passed'] else '❌未过'} {'' if verdict['passed'] else verdict['reason']}")

    return {"makespan_min": round(makespan_min, 2), "upload_sec": round(up_sec, 1),
            "done": done, "total": len(doc_ids), "total_pages": total_pages,
            "agg": agg, "rate": round(rate, 3),
            "passed": verdict["passed"], "reason": verdict["reason"],
            "window": [t0, t1], "docs": doc_details}


def run_customer_reparse_round(args: argparse.Namespace, mla: MedlinkaiClient,
                               plan: list[dict]) -> dict:
    """存量文档重解析：不删不传，对 plan 内文档触发 reparse → 全并发轮询。

    取证口径同客户压测（progress_msg，不依赖 SSH）；
    额外按终态 update_date 计算真实 makespan（防轮询窗口低估尾部大文档）。"""
    t0_epoch = time.time()
    t0 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    triggered: list[dict] = []
    for i, d in enumerate(plan):
        if i and args.submit_stagger > 0:
            time.sleep(args.submit_stagger)
        rep = {"name": d["name"], "doc_id": d["doc_id"], "pages": d["pages"], "note": ""}
        try:
            retry_with_backoff(lambda did=d["doc_id"]: mla.trigger_parse(did),
                               max_retries=args.submit_retries,
                               base_delay=args.submit_retry_delay)
        except Exception as e:  # noqa: BLE001
            rep["note"] = f"trigger error: {e}"
        triggered.append(rep)
        print(f"  [触发 {'ok' if not rep['note'] else 'SKIP'}] "
              f"{rep['name']} {rep['note'][:60]}")

    doc_ids = [x["doc_id"] for x in triggered if not x["note"]]
    if not doc_ids:
        return {"error": "无成功触发", "passed": False, "reason": "无成功触发"}
    trig_sec = time.time() - t0_epoch

    print(f"[存量重解析] 已触发 {len(doc_ids)}/{len(plan)}（{trig_sec:.0f}s），全并发轮询终态 …")
    poll_client = MedlinkaiClient(args.medlinkai_base, args.dataset_id, args.page_size,
                                  api_key=args.api_key, basic_auth=args.basic_auth)
    with ThreadPoolExecutor(max_workers=max(len(doc_ids), 1)) as ex:
        futs = {ex.submit(wait_one, args, poll_client, d): d for d in doc_ids}
        results = {d: f.result() for f, d in futs.items()}

    t1_epoch = time.time()
    t1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    makespan_min = (t1_epoch - t0_epoch) / 60.0
    done = sum(1 for r in results.values() if r["run"] == "DONE")

    # progress_msg 取证 + update_date 真实终态 makespan
    final_docs = {x.get("doc_id"): x for x in list_all_docs(mla, args.page_size)}
    agg = {"timeouts": 0, "errors": 0, "failed_pages": 0, "skipping": 0}
    doc_details: list[dict] = []
    max_end_epoch: float | None = None
    for x in triggered:
        fin = final_docs.get(x["doc_id"]) or {}
        msg = fin.get("progress_msg") or ""
        st = vlm_err_stats(msg)
        for k in agg:
            agg[k] += st[k]
        end_epoch = parse_doc_update_epoch(fin.get("update_date"))
        if end_epoch is not None and (max_end_epoch is None or end_epoch > max_end_epoch):
            max_end_epoch = end_epoch
        doc_details.append({"name": x["name"], "doc_id": x["doc_id"], "pages": x["pages"],
                            "run": (results.get(x["doc_id"]) or {}).get("run"),
                            "note": (results.get(x["doc_id"]) or {}).get("note", ""),
                            "err": st, "progress_msg": msg,
                            "update_date": fin.get("update_date")})
    total_pages = sum(x["pages"] for x in triggered)
    rate = agg["timeouts"] * 100.0 / max(total_pages, 1)
    true_makespan_min = round((max_end_epoch - t0_epoch) / 60.0, 2) if max_end_epoch else None
    verdict = capacity_verdict(true_makespan_min or makespan_min, rate,
                               args.budget_min, args.max_timeout_rate)

    print(f"[存量重解析] 轮询makespan {makespan_min:.1f}min  真实终态makespan "
          f"{true_makespan_min if true_makespan_min is not None else 'N/A'}min  "
          f"DONE {done}/{len(doc_ids)}  总页数 {total_pages}  "
          f"超时行 {agg['timeouts']} → 超时率 {rate:.2f}%  "
          f"{'✅通过' if verdict['passed'] else '❌未过'} {'' if verdict['passed'] else verdict['reason']}")

    return {"makespan_min": round(makespan_min, 2),
            "true_makespan_min": true_makespan_min,
            "trigger_sec": round(trig_sec, 1),
            "done": done, "total": len(doc_ids), "total_pages": total_pages,
            "agg": agg, "rate": round(rate, 3),
            "passed": verdict["passed"], "reason": verdict["reason"],
            "window": [t0, t1], "docs": doc_details}


def main_customer(args: argparse.Namespace) -> int:
    """客户现场真实文档压测：按目标总页数选批 → 下载 → 删旧副本 → 全新上传立即解析。

    --in-customer-env：压测目标环境切到客户现场（源/目标同环境重解析，流程不变），
    用于压测客户环境真实性能。"""
    target = args.customer_pages
    in_cust = getattr(args, "in_customer_env", False)
    target_base, target_dataset = resolve_target_env(args)
    if in_cust:
        # 目标环境直指客户现场：run_customer_round 内删副本/上传/轮询均走 args.medlinkai_base
        args.medlinkai_base, args.dataset_id = target_base, target_dataset
        # 测试环境 vLLM 监控对客户现场无意义且误导；未显式换地址时自动关闭
        if args.metrics_url == DEFAULT_METRICS_URL:
            print("[客户压测] 目标为客户现场：默认测试环境 vLLM 监控已自动关闭"
                  "（--metrics-url 指定客户现场地址可恢复）")
            args.metrics_interval = 0
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    env_tag = "_atCust" if in_cust else ""
    out = Path(args.out_dir) if args.out_dir else \
        Path(__file__).resolve().parent / "results_capacity" / f"{stamp}_cust{target}{env_tag}"
    pdf_dir = out / "pdfs"

    auth_headers, auth_tuple = build_auth_headers(args.api_key, args.basic_auth)

    print("=" * 72)
    print(f"[客户现场压测] 目标 {target} 页  seed={args.seed}  "
          f"客户源 {args.customer_base}  dataset={args.customer_dataset}")
    print(f"压测目标环境: {target_base}  dataset={target_dataset}"
          + ("  ⚠️ 删旧副本/上传将发生在客户现场环境" if in_cust else ""))
    print(f"预算 {args.budget_min}min  超时率上限 <{args.max_timeout_rate}%  结果目录: {out}")
    print("=" * 72)

    docs = fetch_customer_docs(args.customer_base, args.customer_dataset, args.page_size,
                               headers=auth_headers, auth=auth_tuple)
    infos, no_pages = build_customer_infos(docs)
    print(f"客户侧共 {len(docs)} 份，可提取页数 {len(infos)} 份（{no_pages} 份无法提取跳过）")

    chosen, used = pick_batch_by_pages(infos, target, seed=args.seed,
                                       max_doc_pages=args.max_doc_pages)
    dist = {b: len(items) for b, items in group_docs(
        [{"name": d["name"], "doc_id": d["doc_id"],
          "size_kb": (d.get("size") or 0) / 1024.0} for d in chosen]).items()}
    dist_str = " / ".join(f"{b} {c}" for b, c in dist.items())
    print(f"选批: {len(chosen)} 份 共 {used} 页（目标 {target}）  档位分布: {dist_str}")

    manifest = {"meta": {"seed": args.seed, "target_pages": target,
                         "total_pages": used, "n": len(chosen),
                         "band_dist": dist,
                         "customer_base": args.customer_base,
                         "customer_dataset": args.customer_dataset,
                         "in_customer_env": in_cust,
                         "target_base": target_base,
                         "target_dataset": target_dataset},
                "docs": [{**d, "case": d["case"]} for d in chosen]}

    if args.dry_run:
        for d in chosen:
            print(f"  [dry-run] {d['pages']:3d}页 {d['size']/1024/1024:7.2f}MB  {d['name']}")
        print("[dry-run] 结束，不下载/不上传")
        return 0

    out.mkdir(parents=True, exist_ok=True)
    (out / "batch_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    # 下载
    pdf_dir.mkdir(parents=True, exist_ok=True)
    print(f"[客户压测] 开始下载 {len(chosen)} 份 PDF → {pdf_dir}")
    dl_fail: list[dict] = []
    for d in chosen:
        dest = pdf_dir / d["name"]
        if dest.exists() and dest.stat().st_size == d.get("size"):
            continue
        try:
            retry_with_backoff(lambda did=d["doc_id"], ds=dest:
                               download_customer_pdf(args.customer_base, did, ds,
                                                     headers=auth_headers, auth=auth_tuple),
                               max_retries=args.submit_retries,
                               base_delay=args.submit_retry_delay)
        except Exception as e:  # noqa: BLE001
            dl_fail.append({"name": d["name"], "err": str(e)})
            print(f"  [下载失败] {d['name']}: {e}")
    print(f"[客户压测] 下载完成 {len(chosen) - len(dl_fail)}/{len(chosen)}")
    if dl_fail:
        (out / "download_failures.json").write_text(
            json.dumps(dl_fail, ensure_ascii=False, indent=2), encoding="utf-8")
        print("存在下载失败，中止压测（详见 download_failures.json）")
        return 1

    mon = start_metrics_monitor(args, out)
    mla = MedlinkaiClient(args.medlinkai_base, args.dataset_id, args.page_size,
                          api_key=args.api_key, basic_auth=args.basic_auth)
    try:
        r = run_customer_round(args, mla, chosen, pdf_dir)
    finally:
        stop_metrics_monitor(mon)

    summary = {"mode": "customer-batch", "meta": manifest["meta"],
               "budget_min": args.budget_min, "max_timeout_rate": args.max_timeout_rate,
               "metrics_url": args.metrics_url if args.metrics_interval > 0 else None,
               "round": {k: v for k, v in r.items() if k != "docs"},
               "docs": r.get("docs", [])}
    (out / "capacity_result.json").write_text(
        json.dumps({k: v for k, v in summary.items() if k != "docs"},
                   ensure_ascii=False, indent=2), encoding="utf-8")
    (out / "capacity_result_full.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [f"# 客户现场真实文档压测（{r.get('total', 0)} 份 / {manifest['meta']['total_pages']} 页）", "",
             f"- 选批 seed={args.seed}  档位分布: {dist_str}",
             f"- 预算 {args.budget_min}min  超时率上限 <{args.max_timeout_rate}%", ""]
    if "error" in r:
        lines.append(f"**错误：{r['error']}**")
    else:
        agg = r["agg"]
        lines.append(f"- **makespan {r['makespan_min']}min（上传耗时 {r['upload_sec']}s）  "
                     f"DONE {r['done']}/{r['total']}**")
        lines.append(f"- 超时行 {agg['timeouts']} / 错误行 {agg['errors']} / "
                     f"失败页 {agg['failed_pages']} / 跳过 {agg['skipping']} → "
                     f"**超时率 {r['rate']}%**")
        lines.append(f"- **{'✅通过' if r['passed'] else '❌未过'}** {r['reason']}")
        lines += ["", "| 文档 | 页数 | 结果 | 超时行 | 备注 |", "|---|---:|---|---:|---|"]
        for d in r.get("docs", []):
            lines.append(f"| {d['name']} | {d['pages']} | {d['run']} "
                         f"| {d['err']['timeouts']} | {d['note'][:60]} |")
    (out / "capacity_summary.md").write_text("\n".join(lines), encoding="utf-8")

    print("\n" + "=" * 72)
    if "error" not in r:
        print(f"makespan {r['makespan_min']}min（预算 {args.budget_min}min）"
              f"  {'✅未超预算' if r['makespan_min'] <= args.budget_min else '❌超预算'}"
              f"  超时率 {r['rate']}%")
    print(f"结果目录: {out}")
    print("=" * 72)
    return 0


def main_reparse_plan(args: argparse.Namespace) -> int:
    """存量文档重解析模式：按 --reparse-plan 清单对现存文档触发 reparse（不删不传）。

    目标环境固定为客户现场（清单来自客户环境批次）；
    makespan 以终态 update_date 为准（防轮询窗口低估尾部大文档）。"""
    plan, pmeta = load_reparse_plan(args.reparse_plan)
    target_base = args.customer_base.rstrip("/")
    target_dataset = args.customer_dataset
    args.medlinkai_base, args.dataset_id = target_base, target_dataset
    if args.metrics_url == DEFAULT_METRICS_URL:
        print("[存量重解析] 目标为客户现场：默认测试环境 vLLM 监控已自动关闭"
              "（--metrics-url 指定客户现场地址可恢复）")
        args.metrics_interval = 0

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = Path(args.out_dir) if args.out_dir else \
        Path(__file__).resolve().parent / "results_capacity" / \
        f"{stamp}_reparse{pmeta['total_pages']}_atCust"

    print("=" * 72)
    print(f"[存量重解析] {pmeta['n']} 份 / {pmeta['total_pages']} 页（清单: {pmeta['source']}）")
    print(f"目标环境: {target_base}  dataset={target_dataset}"
          "  ⚠️ reparse 发生在客户生产环境")
    print(f"预算 {args.budget_min}min  超时率上限 <{args.max_timeout_rate}%  "
          f"max_wait {args.max_wait}s  结果目录: {out}")
    print("=" * 72)

    if args.dry_run:
        for d in plan:
            print(f"  [dry-run] {d['pages']:3d}页  {d['name']}  {d['doc_id']}")
        print("[dry-run] 结束，不触发解析")
        return 0

    out.mkdir(parents=True, exist_ok=True)
    mla = MedlinkaiClient(args.medlinkai_base, args.dataset_id, args.page_size,
                          api_key=args.api_key, basic_auth=args.basic_auth)
    mon = start_metrics_monitor(args, out)
    try:
        r = run_customer_reparse_round(args, mla, plan)
    finally:
        stop_metrics_monitor(mon)

    meta = {"mode": "reparse-plan", "plan_source": pmeta["source"],
            "n": pmeta["n"], "total_pages": pmeta["total_pages"],
            "target_base": target_base, "target_dataset": target_dataset}
    summary = {"mode": "reparse-plan", "meta": meta,
               "budget_min": args.budget_min, "max_timeout_rate": args.max_timeout_rate,
               "metrics_url": args.metrics_url if args.metrics_interval > 0 else None,
               "round": {k: v for k, v in r.items() if k != "docs"},
               "docs": r.get("docs", [])}
    (out / "capacity_result.json").write_text(
        json.dumps({k: v for k, v in summary.items() if k != "docs"},
                   ensure_ascii=False, indent=2), encoding="utf-8")
    (out / "capacity_result_full.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [f"# 客户环境存量文档重解析（{pmeta['n']} 份 / {pmeta['total_pages']} 页）", "",
             f"- 清单: {pmeta['source']}",
             f"- 预算 {args.budget_min}min  超时率上限 <{args.max_timeout_rate}%", ""]
    if "error" in r:
        lines.append(f"**错误：{r['error']}**")
    else:
        agg = r["agg"]
        lines.append(f"- **轮询makespan {r['makespan_min']}min  "
                     f"真实终态makespan {r['true_makespan_min']}min  "
                     f"DONE {r['done']}/{r['total']}**")
        lines.append(f"- 超时行 {agg['timeouts']} / 错误行 {agg['errors']} / "
                     f"失败页 {agg['failed_pages']} / 跳过 {agg['skipping']} → "
                     f"**超时率 {r['rate']}%**")
        lines.append(f"- **{'✅通过' if r['passed'] else '❌未过'}** {r['reason']}")
        lines += ["", "| 文档 | 页数 | 结果 | 完成时刻(UTC) | 备注 |", "|---|---:|---|---|---|"]
        for d in r.get("docs", []):
            lines.append(f"| {d['name']} | {d['pages']} | {d['run']} "
                         f"| {d.get('update_date') or '-'} | {d['note'][:60]} |")
    (out / "capacity_summary.md").write_text("\n".join(lines), encoding="utf-8")

    print("\n" + "=" * 72)
    if "error" not in r:
        tm = r.get("true_makespan_min")
        print(f"真实终态makespan {tm}min / 轮询makespan {r['makespan_min']}min"
              f"（预算 {args.budget_min}min）  超时率 {r['rate']}%")
    print(f"结果目录: {out}")
    print("=" * 72)
    return 0


# ══════════════════════════════════════════════════════════════════
# 主流程
# ══════════════════════════════════════════════════════════════════


def parse_capacity_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="倍增容量探测（30min 预算 + VLM 超时率约束）")
    p.add_argument("--source-pdf", default="", help="源 PDF 路径（复制模式必填，~5MB 如 RRUU）")
    p.add_argument("--reparse-band", default="",
                   help="线上实档重解析模式：小<5MB / 中5-10MB / 大>10MB（与复制模式二选一）")
    p.add_argument("--reparse-sample", type=int, default=0,
                   help="跨档随机抽样重解析模式：从全部原始文档中随机抽 N 份（与上两者三选一）")
    p.add_argument("--customer-pages", type=int, default=0,
                   help="客户现场真实文档压测模式：按目标总页数选批 → 下载 → 删旧副本 → 全新上传")
    p.add_argument("--reparse-plan", default="",
                   help="存量文档重解析模式：指定上一轮 capacity_result_full.json，"
                        "对其中文档在客户环境触发 reparse（不删不传）")
    p.add_argument("--max-doc-pages", type=int, default=0,
                   help="客户批次选批时单文档页数上限（0=不限），排除长尾超大档")
    p.add_argument("--customer-base", default="http://123.157.144.10:30080",
                   help="客户现场 API 基址（customer 模式）")
    p.add_argument("--customer-dataset", default="fb850778372011f195bd2a5fbb884e34",
                   help="客户现场 dataset_id（customer 模式）")
    p.add_argument("--in-customer-env", action="store_true",
                   help="customer 模式：压测目标环境直指客户现场（--customer-base/--customer-dataset），"
                        "流程不变（混合页数选批 → 下载 → 删同名旧副本 → 全新上传解析），压测客户环境真实性能")
    p.add_argument("--seed", type=int, default=0,
                   help="抽样随机种子（dry-run 与实跑同种子保证同批）")
    p.add_argument("--include-copies", action="store_true",
                   help="实档模式默认排除容量探测变异副本；加此参数则一并纳入")
    p.add_argument("--medlinkai-base", default=os.environ.get("MLA_BASE", "http://10.16.3.16:3160"))
    p.add_argument("--dataset-id", default="fb850778372011f195bd2a5fbb884e34")
    p.add_argument("--api-key", default=os.environ.get("MLA_API_KEY", ""))
    p.add_argument("--basic-auth", default=os.environ.get("MLA_BASIC_AUTH", ""))
    p.add_argument("--page-size", type=int, default=100)
    p.add_argument("--levels", default="4,8,16,32", help="倍增阶梯（逗号分隔）")
    p.add_argument("--refine-step", type=int, default=4,
                   help="超界后细化步长（0=不细化）")
    p.add_argument("--budget-min", type=float, default=30.0, help="makespan 预算（分钟）")
    p.add_argument("--max-timeout-rate", type=float, default=2.0, help="VLM 超时率上限%%")
    p.add_argument("--submit-stagger", type=float, default=1.0, help="上传错峰间隔（秒）")
    p.add_argument("--submit-retries", type=int, default=5, help="上传 502 重试次数")
    p.add_argument("--submit-retry-delay", type=float, default=2.0, help="重试基础退避秒数")
    p.add_argument("--max-wait", type=int, default=1800)
    p.add_argument("--poll-interval", type=int, default=5)
    p.add_argument("--tz-offset", type=int, default=0, help="本地与服务器日志时区差（默认 0）")
    p.add_argument("--grace", type=int, default=60, help="取证窗口结束侧宽限秒数")
    # 病案字段默认（RRUU=哮喘）
    p.add_argument("--gender", default="man")
    p.add_argument("--age", type=int, default=23)
    p.add_argument("--illness-code-l1", default="1000000")
    p.add_argument("--illness-label-l1", default="慢病")
    p.add_argument("--illness-code-l2", default="1001000")
    p.add_argument("--illness-label-l2", default="呼吸疾病")
    p.add_argument("--illness-code-l3", default="1001001")
    p.add_argument("--illness-label-l3", default="哮喘")
    # SSH 只读取证
    p.add_argument("--ssh-host", default="10.16.3.16")
    p.add_argument("--ssh-user", default="root")
    p.add_argument("--ssh-key", default=DEFAULT_SSH_KEY)
    p.add_argument("--ssh-askpass", default=DEFAULT_ASKPASS)
    p.add_argument("--out-dir", default="", help="默认 <脚本目录>/results_capacity/<时间戳>")
    p.add_argument("--metrics-url", default=DEFAULT_METRICS_URL,
                   help="vLLM Prometheus /metrics 地址（空串=不监控）")
    p.add_argument("--metrics-interval", type=float, default=30.0,
                   help="vLLM 监控采样间隔秒数（<=0 关闭监控）")
    p.add_argument("--dry-run", action="store_true", help="只打印阶梯与副本命名，不上传/不 SSH")
    return p.parse_args()


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    args = parse_capacity_args()
    if args.reparse_plan:
        return main_reparse_plan(args)
    if args.customer_pages > 0:
        return main_customer(args)
    if args.reparse_sample > 0:
        return main_sample(args)
    if args.reparse_band:
        return main_reparse(args)

    if not args.source_pdf:
        print("复制模式需要 --source-pdf（或用 --reparse-band 走线上实档重解析模式）")
        return 1
    source = Path(args.source_pdf)
    if not source.exists():
        print(f"源 PDF 不存在: {source}")
        return 1
    stem = source.stem
    levels = [int(x) for x in args.levels.split(",") if x.strip()]

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = Path(args.out_dir) if args.out_dir else Path(__file__).resolve().parent / "results_capacity" / stamp
    copies_dir = out / "copies"

    print("=" * 72)
    print(f"源 PDF: {source.name}  ({source.stat().st_size/1024/1024:.2f} MB)")
    print(f"倍增阶梯: {levels}  预算 {args.budget_min}min  超时率上限 <{args.max_timeout_rate}%")
    print(f"细化步长: {args.refine_step}  结果目录: {out}")
    print("=" * 72)

    if args.dry_run:
        for n in levels:
            print(f"[dry-run] N={n}: 副本 {copy_names(stem, n, f'n{n}')[:3]} …（共 {n}）")
        print("[dry-run] 结束，不上传/不 SSH")
        return 0

    out.mkdir(parents=True, exist_ok=True)
    mla = MedlinkaiClient(args.medlinkai_base, args.dataset_id, args.page_size,
                          api_key=args.api_key, basic_auth=args.basic_auth)

    mon = start_metrics_monitor(args, out)
    rounds: list[dict] = []
    last_ok: int | None = None
    first_fail: int | None = None
    try:
        for n in levels:
            r = run_capacity_round(args, mla, n, source, stem, copies_dir)
            rounds.append(r)
            if r.get("passed"):
                last_ok = n
            else:
                first_fail = n
                break

        # 细化
        if args.refine_step > 0 and last_ok is not None and first_fail is not None:
            for n in refine_range(last_ok, first_fail, args.refine_step):
                r = run_capacity_round(args, mla, n, source, stem, copies_dir)
                rounds.append(r)
                if r.get("passed"):
                    last_ok = n
                else:
                    break
    finally:
        stop_metrics_monitor(mon)

    summary = {
        "source": source.name,
        "levels": levels,
        "budget_min": args.budget_min,
        "max_timeout_rate": args.max_timeout_rate,
        "max_capacity_n": last_ok,
        "rounds": rounds,
    }
    (out / "capacity_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = ["# 倍增容量探测汇总", "",
             f"- 源：{source.name}  预算 {args.budget_min}min  超时率上限 <{args.max_timeout_rate}%",
             f"- **最大容量 N = {last_ok if last_ok is not None else '无（首档即失败）'}**", "",
             "| N | makespan(min) | DONE | 超时率% | 结果 | 原因 |",
             "|---:|---:|---:|---:|---|---|"]
    for r in rounds:
        if "error" in r:
            lines.append(f"| {r['n']} | - | - | - | 错误 | {r['error']} |")
        else:
            lines.append(f"| {r['n']} | {r['makespan_min']} | {r['done']}/{r['total']} "
                         f"| {r['rate']} | {'通过' if r['passed'] else '未过'} | {r['reason']} |")
    (out / "capacity_summary.md").write_text("\n".join(lines), encoding="utf-8")

    print("\n" + "=" * 72)
    print(f"最大容量 N = {last_ok if last_ok is not None else '无（首档即失败）'}")
    print(f"结果目录: {out}")
    print("=" * 72)
    return 0


def main_reparse(args: argparse.Namespace) -> int:
    """线上实档重解析模式：档内全部现存文档一次性触发 reparse，看 30min 预算与超时率。"""
    band = resolve_group_alias(args.reparse_band)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = Path(args.out_dir) if args.out_dir else Path(__file__).resolve().parent / "results_capacity" / f"{stamp}_reparse"

    mla = MedlinkaiClient(args.medlinkai_base, args.dataset_id, args.page_size,
                          api_key=args.api_key, basic_auth=args.basic_auth)
    docs = list_all_docs(mla, args.page_size)
    picked = select_band(docs, args.reparse_band, exclude_copies=not args.include_copies)

    print("=" * 72)
    print(f"[实档重解析 {band}] 线上共 {len(docs)} 份，档内 {len(picked)} 份"
          f"（{'含' if args.include_copies else '已排除'}探测副本）")
    print(f"预算 {args.budget_min}min  超时率上限 <{args.max_timeout_rate}%  结果目录: {out}")
    print("=" * 72)

    if args.dry_run:
        for d in picked:
            mb = (d.get("size_kb") or 0) / 1024.0
            print(f"  [dry-run] {mb:7.2f} MB  {d.get('name')}  {d.get('doc_id')}")
        print(f"[dry-run] 共 {len(picked)} 份，不触发解析/不 SSH")
        return 0

    mon = start_metrics_monitor(args, out)
    try:
        r = run_reparse_round(args, mla, args.reparse_band)
    finally:
        stop_metrics_monitor(mon)
    out.mkdir(parents=True, exist_ok=True)
    summary = {"mode": "reparse-band", "band": band,
               "budget_min": args.budget_min, "max_timeout_rate": args.max_timeout_rate,
               "round": r}
    (out / "capacity_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [f"# 线上实档重解析容量探测（{band}）", "",
             f"- 预算 {args.budget_min}min  超时率上限 <{args.max_timeout_rate}%",
             f"- 档内 {r.get('total', 0)} 份一次性触发 reparse", ""]
    if "error" in r:
        lines.append(f"**错误：{r['error']}**")
    else:
        lines.append(f"- **makespan {r['makespan_min']}min  DONE {r['done']}/{r['total']}  "
                     f"VLM 尝试 {r['starts']} 超时 {r['timeouts']} → 超时率 {r['rate']}%**")
        lines.append(f"- **{'✅通过' if r['passed'] else '❌未过'}** {r['reason']}")
        lines += ["", "| 文档 | 结果 | 备注 |", "|---|---|---|"]
        for d in r.get("docs", []):
            lines.append(f"| {d['name']} | {d['run']} | {d['note'][:80]} |")
    (out / "capacity_summary.md").write_text("\n".join(lines), encoding="utf-8")

    print("\n" + "=" * 72)
    if "error" not in r:
        print(f"makespan {r['makespan_min']}min（预算 {args.budget_min}min）"
              f"  {'✅未超预算' if r['makespan_min'] <= args.budget_min else '❌超预算'}")
    print(f"结果目录: {out}")
    print("=" * 72)
    return 0


def main_sample(args: argparse.Namespace) -> int:
    """跨档随机抽样重解析模式：从全部原始文档中随机抽 N 份一次性触发 reparse。"""
    n = args.reparse_sample
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = Path(args.out_dir) if args.out_dir else Path(__file__).resolve().parent / "results_capacity" / f"{stamp}_sample{n}"

    mla = MedlinkaiClient(args.medlinkai_base, args.dataset_id, args.page_size,
                          api_key=args.api_key, basic_auth=args.basic_auth)
    docs = list_all_docs(mla, args.page_size)
    picked = sample_docs(docs, n, exclude_copies=not args.include_copies, seed=args.seed)

    # 抽样档位分布
    dist = {b: 0 for b in BAND_NAMES}
    for band_name, items in group_docs(picked).items():
        dist[band_name] = len(items)
    dist_str = " / ".join(f"{b} {c}" for b, c in dist.items())

    print("=" * 72)
    print(f"[抽样重解析 N={n} seed={args.seed}] 线上共 {len(docs)} 份，抽中 {len(picked)} 份"
          f"（{'含' if args.include_copies else '已排除'}探测副本）")
    print(f"档位分布: {dist_str}")
    print(f"预算 {args.budget_min}min  超时率上限 <{args.max_timeout_rate}%  结果目录: {out}")
    print("=" * 72)

    if args.dry_run:
        for d in picked:
            mb = (d.get("size_kb") or 0) / 1024.0
            print(f"  [dry-run] {mb:7.2f} MB  {d.get('name')}  {d.get('doc_id')}")
        print(f"[dry-run] 共 {len(picked)} 份，不触发解析/不 SSH")
        return 0

    label = f"抽样N={n}"
    mon = start_metrics_monitor(args, out)
    try:
        r = run_reparse_round(args, mla, band="小<5MB", picked=picked, label=label)
    finally:
        stop_metrics_monitor(mon)
    out.mkdir(parents=True, exist_ok=True)
    summary = {"mode": "reparse-sample", "n": n, "seed": args.seed,
               "band_dist": dist,
               "budget_min": args.budget_min, "max_timeout_rate": args.max_timeout_rate,
               "round": r}
    (out / "capacity_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [f"# 线上实档抽样重解析容量探测（随机 {n} 份，seed={args.seed}）", "",
             f"- 预算 {args.budget_min}min  超时率上限 <{args.max_timeout_rate}%",
             f"- 档位分布: {dist_str}",
             f"- 抽中 {r.get('total', 0)} 份一次性触发 reparse", ""]
    if "error" in r:
        lines.append(f"**错误：{r['error']}**")
    else:
        lines.append(f"- **makespan {r['makespan_min']}min  DONE {r['done']}/{r['total']}  "
                     f"VLM 尝试 {r['starts']} 超时 {r['timeouts']} → 超时率 {r['rate']}%**")
        lines.append(f"- **{'✅通过' if r['passed'] else '❌未过'}** {r['reason']}")
        lines += ["", "| 文档 | 结果 | 备注 |", "|---|---|---|"]
        for d in r.get("docs", []):
            lines.append(f"| {d['name']} | {d['run']} | {d['note'][:80]} |")
    (out / "capacity_summary.md").write_text("\n".join(lines), encoding="utf-8")

    print("\n" + "=" * 72)
    if "error" not in r:
        print(f"makespan {r['makespan_min']}min（预算 {args.budget_min}min）"
              f"  {'✅未超预算' if r['makespan_min'] <= args.budget_min else '❌超预算'}")
    print(f"结果目录: {out}")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main())
