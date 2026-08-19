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
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

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
# 主流程
# ══════════════════════════════════════════════════════════════════


def parse_capacity_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="倍增容量探测（30min 预算 + VLM 超时率约束）")
    p.add_argument("--source-pdf", default="", help="源 PDF 路径（复制模式必填，~5MB 如 RRUU）")
    p.add_argument("--reparse-band", default="",
                   help="线上实档重解析模式：小<5MB / 中5-10MB / 大>10MB（与复制模式二选一）")
    p.add_argument("--reparse-sample", type=int, default=0,
                   help="跨档随机抽样重解析模式：从全部原始文档中随机抽 N 份（与上两者三选一）")
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
    p.add_argument("--dry-run", action="store_true", help="只打印阶梯与副本命名，不上传/不 SSH")
    return p.parse_args()


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    args = parse_capacity_args()
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

    rounds: list[dict] = []
    last_ok: int | None = None
    first_fail: int | None = None
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

    r = run_reparse_round(args, mla, args.reparse_band)
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
    r = run_reparse_round(args, mla, band="小<5MB", picked=picked, label=label)
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
