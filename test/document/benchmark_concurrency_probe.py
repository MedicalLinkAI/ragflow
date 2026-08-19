#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按文件大小分组的最大并发数探测脚本（约束：VLM 接口超时率 < 阈值）。

基于 benchmark_online.py 的客户端契约（list_docs / trigger_parse / wait_status）：

1. 拉取线上文档列表，按大小分组：小 <5MB / 中 5-10MB / 大 >=10MB；
2. 每组按并发阶梯（默认 4,6,8）升序各跑一轮 reparse（同组固定样本，轮间可比）；
3. 每轮结束后 SSH **只读** grep 服务器 executor 日志（UTC 时间戳），
   窗口内配平 VLM 尝试数与超时数：
   - 尝试 = 含 "API call start" 且不含 "coord API call start" 的行（含重试产生的 start(raw)）
   - 超时 = 含 "API call failed (attempt" 且含 "Read timed out" 的行（coord 失败无 (attempt，天然排除）
   超时率 = 超时 / (尝试 + 超时)，与 20260817_230319 取证口径一致；
4. 某轮超时率 >= 阈值（默认 2%）即停止该组阶梯，最大并发 = 上一个通过档；首档即挂记 None。

约束：只触发 reparse 与只读日志，不改病案字段、不重启服务、服务器零写操作。

用法:
    python benchmark_concurrency_probe.py --dry-run                 # 只看分组与样本
    python benchmark_concurrency_probe.py --levels 4,6,8 --sample 8
    python benchmark_concurrency_probe.py --only-group 大>10MB
"""

from __future__ import annotations

import argparse
import json
import os
import random
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from benchmark_online import MedlinkaiClient

BAND_NAMES = ["小<5MB", "中5-10MB", "大>10MB"]

GROUP_ALIASES = {
    "小": "小<5MB", "小<5MB": "小<5MB",
    "s": "小<5MB", "small": "小<5MB",
    "中": "中5-10MB", "中5-10MB": "中5-10MB",
    "m": "中5-10MB", "medium": "中5-10MB",
    "大": "大>10MB", "大>10MB": "大>10MB",
    "l": "大>10MB", "large": "大>10MB",
}

DEFAULT_SSH_KEY = r"C:\Users\James Lu\.ssh\id_ed25519_futurefab_lsc"
DEFAULT_ASKPASS = str(Path(__file__).resolve().parents[3] / "askpass.bat")
SERVER_LOG_GLOB = "/data/kca/medlink/ragflow/logs/task_executor_medlink_*.log"


# ══════════════════════════════════════════════════════════════════
# 纯逻辑（单元测试覆盖）
# ══════════════════════════════════════════════════════════════════


def resolve_group_alias(raw: str) -> str:
    """将 only-group 参数的中/英文别名统一解析为 BAND_NAMES 中的标准名。"""
    if not raw:
        return ""
    return GROUP_ALIASES.get(raw.strip().lower(), raw)


def retry_with_backoff(fn, max_retries: int = 3, base_delay: float = 1.0,
                       max_delay: float = 8.0,
                       exceptions: tuple[type[Exception], ...] = (Exception,)):
    """指数退避重试，第 n 次等待 min(base_delay * 2^(n-1), max_delay) 秒。"""
    last_err: Exception | None = None
    for attempt in range(max_retries):
        try:
            return fn()
        except exceptions as e:
            last_err = e
            if attempt < max_retries - 1:
                delay = min(base_delay * (2 ** attempt), max_delay)
                time.sleep(delay)
    raise last_err


def group_docs(docs: list[dict]) -> dict[str, list[dict]]:
    """按 size_kb 分三档：小 <5MB / 中 [5,10)MB / 大 >=10MB；无大小信息跳过。"""
    out = {name: [] for name in BAND_NAMES}
    for d in docs:
        size_kb = d.get("size_kb")
        if not size_kb:
            continue
        mb = size_kb / 1024
        if mb < 5:
            out["小<5MB"].append(d)
        elif mb < 10:
            out["中5-10MB"].append(d)
        else:
            out["大>10MB"].append(d)
    return out


def pick_sample(docs: list[dict], n: int, seed: int) -> list[dict]:
    """固定种子抽样（<=n 全取），同组各并发档复用同一样本保证可比。"""
    if len(docs) <= n:
        return list(docs)
    return random.Random(seed).sample(list(docs), n)


def timeout_rate(starts: int, timeouts: int) -> float:
    """超时率% = 超时 / (尝试+超时)；尝试数 = 逻辑 start 数（含重试再发起）。"""
    total = starts + timeouts
    return timeouts * 100.0 / total if total else 0.0


def evaluate_ladder(results: list[tuple[int, float]], max_rate: float) -> dict:
    """升序阶梯判定：rate < max_rate 才通过；首档挂记 max_ok_level=None。"""
    max_ok = None
    stopped = None
    for level, rate in results:
        if rate < max_rate:
            max_ok = level
        else:
            stopped = level
            break
    return {"max_ok_level": max_ok, "stopped_at": stopped}


def server_window(local_start: str, local_end: str, tz_offset: int = 8,
                  grace_s: int = 60) -> tuple[str, str]:
    """本地时间串 → 服务器日志（UTC）窗口串，结束侧加 grace 容纳在途重试。"""
    fmt = "%Y-%m-%d %H:%M:%S"
    s = datetime.strptime(local_start, fmt) - timedelta(hours=tz_offset)
    e = datetime.strptime(local_end, fmt) - timedelta(hours=tz_offset) + timedelta(seconds=grace_s)
    return s.strftime("%Y-%m-%d %H:%M"), e.strftime("%Y-%m-%d %H:%M")


# ══════════════════════════════════════════════════════════════════
# SSH 只读取证
# ══════════════════════════════════════════════════════════════════


def build_count_cmd(s: str, e: str) -> str:
    """awk 窗口配平命令（服务器 sh 执行，只读）。"""
    return (
        "awk -v s='%s' -v e='%s' '"
        "{ ts = substr($1 \" \" $2, 1, 16) } "
        "ts >= s && ts <= e { "
        "if (index($0, \"API call start\") && !index($0, \"coord API call start\")) starts++; "
        "if (index($0, \"API call failed (attempt\") && index($0, \"Read timed out\")) timeouts++ "
        "} "
        "END { printf \"%%d %%d\\n\", starts+0, timeouts+0 }' %s" % (s, e, SERVER_LOG_GLOB)
    )


def ssh_count_vlm(args: argparse.Namespace, s: str, e: str) -> tuple[int, int]:
    env = os.environ.copy()
    env["SSH_ASKPASS"] = args.ssh_askpass
    env["SSH_ASKPASS_REQUIRE"] = "force"
    cmd = ["ssh", "-i", args.ssh_key, "-o", "StrictHostKeyChecking=no",
           f"{args.ssh_user}@{args.ssh_host}", build_count_cmd(s, e)]
    p = subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=180)
    if p.returncode != 0:
        raise RuntimeError(f"ssh 取证失败: {p.stderr.strip()[:200]}")
    nums = p.stdout.strip().split()
    return int(nums[0]), int(nums[1])


# ══════════════════════════════════════════════════════════════════
# 单轮 reparse
# ══════════════════════════════════════════════════════════════════


def process_doc(args: argparse.Namespace, dataset_id: str, doc: dict) -> dict:
    """单文档：触发 reparse → 轮询终态（不拉 chunks，缩短轮次）。"""
    mla = MedlinkaiClient(args.medlinkai_base, dataset_id, args.page_size,
                          api_key=args.api_key, basic_auth=args.basic_auth)
    t0 = time.time()
    rep = {"name": doc["name"], "run": None, "elapsed_s": None, "note": ""}
    try:
        retry_with_backoff(lambda: mla.trigger_parse(doc["doc_id"]),
                           max_retries=args.submit_retries,
                           base_delay=args.submit_retry_delay)
        status, note = mla.wait_status(doc["doc_id"], args.max_wait,
                                       args.poll_interval, wait_running=True)
        rep["run"] = (status or {}).get("run")
        rep["note"] = note
    except Exception as e:
        rep["note"] = f"error: {e}"
    rep["elapsed_s"] = round(time.time() - t0, 1)
    print(f"  [{rep['run'] or 'ERR'}] {doc['name']} {rep['elapsed_s']}s {rep['note'][:60]}")
    return rep


def run_round(args: argparse.Namespace, dataset_id: str, sample: list[dict],
              level: int) -> tuple[str, str, list[dict]]:
    t_start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with ThreadPoolExecutor(max_workers=level) as ex:
        futs = []
        for i, d in enumerate(sample):
            if i and args.submit_stagger > 0:
                time.sleep(args.submit_stagger)
            futs.append(ex.submit(process_doc, args, dataset_id, d))
        reps = [f.result() for f in futs]
    t_end = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return t_start, t_end, reps


# ══════════════════════════════════════════════════════════════════
# 主流程
# ══════════════════════════════════════════════════════════════════


def parse_probe_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="分组最大并发探测（VLM 超时率约束）")
    p.add_argument("--medlinkai-base", default=os.environ.get("MLA_BASE", "http://10.16.3.16:3160"))
    p.add_argument("--dataset-id", default="fb850778372011f195bd2a5fbb884e34")
    p.add_argument("--api-key", default=os.environ.get("MLA_API_KEY", ""))
    p.add_argument("--basic-auth", default=os.environ.get("MLA_BASIC_AUTH", ""))
    p.add_argument("--page-size", type=int, default=100)
    p.add_argument("--levels", default="4,6,8", help="并发阶梯（升序）")
    p.add_argument("--sample", type=int, default=8, help="每组每档样本数")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--max-timeout-rate", type=float, default=2.0, help="VLM 超时率上限%%（< 才通过）")
    p.add_argument("--only-group", default="", help="只跑某一档（小<5MB / 中5-10MB / 大>10MB）")
    p.add_argument("--max-wait", type=int, default=1800)
    p.add_argument("--poll-interval", type=int, default=5)
    p.add_argument("--submit-stagger", type=float, default=2.0,
                   help="提交 trigger_parse 之间错峰间隔（秒），缓解 Nginx 并发 POST 502")
    p.add_argument("--submit-retries", type=int, default=3,
                   help="trigger_parse 502/503 时指数退避重试次数")
    p.add_argument("--submit-retry-delay", type=float, default=1.0,
                   help="trigger_parse 重试基础退避秒数")
    p.add_argument("--tz-offset", type=int, default=0, help="本地相对服务器日志时区的小时差（默认 0，服务器日志为 CST 与本地同）")
    p.add_argument("--grace", type=int, default=60, help="轮次结束侧宽限秒数（容纳在途重试）")
    p.add_argument("--ssh-host", default="10.16.3.16")
    p.add_argument("--ssh-user", default="root")
    p.add_argument("--ssh-key", default=DEFAULT_SSH_KEY)
    p.add_argument("--ssh-askpass", default=DEFAULT_ASKPASS)
    p.add_argument("--out-dir", default="", help="默认 <脚本目录>/results_probe/<时间戳>")
    p.add_argument("--dry-run", action="store_true", help="只打印分组与样本，不触发解析/不 SSH")
    return p.parse_args()


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    args = parse_probe_args()
    args.only_group = resolve_group_alias(args.only_group)
    levels = [int(x) for x in args.levels.split(",") if x.strip()]

    mla = MedlinkaiClient(args.medlinkai_base, args.dataset_id, args.page_size,
                          api_key=args.api_key, basic_auth=args.basic_auth)
    docs: list[dict] = []
    page = 1
    while True:
        batch = mla.list_docs(page=page, page_size=args.page_size)
        docs.extend(batch)
        if len(batch) < args.page_size:
            break
        page += 1
    groups = group_docs(docs)

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = Path(args.out_dir) if args.out_dir else Path(__file__).resolve().parent / "results_probe" / stamp
    out.mkdir(parents=True, exist_ok=True)

    print("=" * 72)
    print(f"文档总数 {len(docs)}；分组：小 {len(groups['小<5MB'])} / "
          f"中 {len(groups['中5-10MB'])} / 大 {len(groups['大>10MB'])}")
    print(f"阶梯 {levels}  样本 {args.sample}/组  超时率上限 <{args.max_timeout_rate}%")
    print("=" * 72)

    summary: dict[str, dict] = {}
    for band in BAND_NAMES:
        if args.only_group and band != args.only_group:
            continue
        pool = groups[band]
        if not pool:
            print(f"\n[{band}] 无文档，跳过")
            continue
        sample = pick_sample(pool, args.sample, args.seed)
        print(f"\n[{band}] 样本 {len(sample)} 个：" +
              ", ".join(f"{d['name']}({d['size_kb']/1024:.1f}MB)" for d in sample))
        if args.dry_run:
            continue

        results: list[tuple[int, float]] = []
        for level in levels:
            print(f"\n[{band}] ── 并发 {level} 轮开始 ──")
            t0, t1, reps = run_round(args, args.dataset_id, sample, level)
            s, e = server_window(t0, t1, args.tz_offset, args.grace)
            starts, timeouts = ssh_count_vlm(args, s, e)
            rate = timeout_rate(starts, timeouts)
            ok = rate < args.max_timeout_rate
            results.append((level, rate))
            done = sum(1 for r in reps if r["run"] == "DONE")
            print(f"[{band}] 并发 {level}: 窗口 {s}~{e} UTC  VLM 尝试 {starts} "
                  f"超时 {timeouts} → 超时率 {rate:.2f}% {'✅' if ok else '❌'}"
                  f"（文档 DONE {done}/{len(sample)}）")
            if not ok:
                break

        verdict = evaluate_ladder(results, args.max_timeout_rate)
        summary[band] = {"samples": [d["name"] for d in sample],
                         "rounds": [{"level": lv, "rate": rt} for lv, rt in results],
                         **verdict}
        print(f"[{band}] 最大并发 = {verdict['max_ok_level']}"
              + (f"（并发 {verdict['stopped_at']} 超时率超标停止）" if verdict["stopped_at"] else "（阶梯全过）"))

    if not args.dry_run:
        (out / "probe_summary.json").write_text(
            json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
        lines = ["# 分组最大并发探测汇总", "", f"- 时间：{stamp}",
                 f"- 阶梯：{levels}  超时率上限 <{args.max_timeout_rate}%", ""]
        lines.append("| 档位 | 各档超时率 | 最大并发 | 停止于 |")
        lines.append("|---|---|---:|---|")
        for band, item in summary.items():
            rates = " / ".join(f"{lv}:{rt:.2f}%" for lv, rt in item["rounds"])
            lines.append(f"| {band} | {rates} | {item['max_ok_level'] or '-'} "
                         f"| {item['stopped_at'] or '-'} |")
        (out / "probe_summary.md").write_text("\n".join(lines), encoding="utf-8")
        print(f"\n结果目录: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
