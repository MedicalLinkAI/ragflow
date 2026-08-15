#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上测试环境（a800-116）病案上传解析批量统计脚本。

与 benchmark_upload.py 的区别：
- 目标环境默认 http://10.16.3.16:3160（内网测试环境），RAGFlow 走 39480 端口
- **不分析 worker 日志**（日志在服务器上），只统计：
  1. 覆盖率：chunks positions 页码并集 vs PDF 总页数
  2. 类型一致性：解析 status 接口 progress_msg 里 "SmartSplitter done: ... Types: {...}"
     日志的类型个数，与 clinical 接口 encounters 各类型记录个数比对是否匹配

重复文件处理（upload_file 返回 409）：
- 默认：略过上传，复用已有 doc_id，调 /{doc_id}/parse 直接重新解析（不更新病案字段）
- --reupload：先 DELETE 再重新上传（重新解析）
- --stats-only：不上传、不触发解析，只对已有文档做统计
- --reparse-list：取 GET /api/v1/documents 列表返回的文档（默认 20 个），
  调 /{doc_id}/parse 直接触发重新解析并统计，完全不涉及上传、不改病案字段

增强能力：
- 每次测试前快照 pipeline DSL（GET /api/v1/pipeline/agents/<agent_id>/dsl）到输出目录
  pipeline_dsl.json，便于事后比对是否提示词变更导致结果差异
- --concurrency：并发解析病例数（默认 4）
- 重解析前若该文档无基线结果，先保存"重解析前"快照（before：chunk 数 + clinical 类型记录数）
- --compare-with：与基线结果目录（summary.json）按文件名比对 chunks 数与类型一致性

用法:
    python benchmark_online.py                        # 默认：已上传则略过上传直接重新解析
    python benchmark_online.py --reupload             # 409 重复时删除后重传
    python benchmark_online.py --stats-only           # 只统计，不触发任何解析
    python benchmark_online.py --reparse-list         # 取文档列表前 20 个，只重解析+统计
    python benchmark_online.py --only 哮喘            # 只处理文件名含"哮喘"的
    python benchmark_online.py --dataset-id <id>      # 手动指定 dataset（默认自动探测）
    python benchmark_online.py --concurrency 4        # 并发解析病例数（默认 4）
    python benchmark_online.py --compare-with <dir>   # 与历史结果目录对比（默认 20260814_095003）
"""

from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from typing import Any

import requests

# ══════════════════════════════════════════════════════════════════
# 常量：类型标签 + clinical 接口类型键映射
# ══════════════════════════════════════════════════════════════════

DOC_TYPE_LABELS: dict[str, str] = {
    "OutpatientRecord": "门诊",
    "AdmissionRecord": "入院",
    "DischargeRecord": "出院",
    "MedicationRecord": "购药",
    "PrescriptionRecord": "处方",
    "ExaminationReport": "检查报告",
    "LabReport": "检验报告",
    "ProgressNote": "病程记录",
    "MedicalOrder": "医嘱",
}

# clinical 接口 encounters 的类型列表键 → SmartSplitter 类型名
CLINICAL_KEY_TO_TYPE: dict[str, str] = {
    "outpatients": "OutpatientRecord",
    "admission_records": "AdmissionRecord",
    "discharge_summaries": "DischargeRecord",
    "medications": "MedicationRecord",
    "prescriptions": "PrescriptionRecord",
    "examination_reports": "ExaminationReport",
    "lab_reports": "LabReport",
    "progress_notes": "ProgressNote",
    "medical_orders": "MedicalOrder",
}

SMART_SPLITTER_TYPES_RE = re.compile(r"SmartSplitter done:.*?Types:\s*\{([^}]*)\}")

# 线上测试环境（a800-116）默认配置
DEFAULT_MLA_BASE = "http://10.16.3.16:3160"
DEFAULT_RAGFLOW_BASE = "http://10.16.3.16:39480/api/v1"
DEFAULT_RAGFLOW_KEY = "ragflow-ZihvOw9xL9fS9nKMWPrAHe3Qxeb9E2eo6VzXyIcIyq4"
DEFAULT_DATASET_ID = "fb850778372011f195bd2a5fbb884e34"  # MedLinkAI-v7.0

# pipeline DSL 快照的 agent id（dataflow）
DEFAULT_AGENT_ID = "3be6fcd058ce11f1ab13b5606b24de97"

# 默认基线结果目录（--compare-with），空字符串=不对比
DEFAULT_BASELINE_DIR = str(
    Path(__file__).resolve().parent / "results_online" / "20260814_095003")

# RAGFlow run 状态（status 接口返回字符串）
TERMINAL_RUNS = {"CANCEL", "DONE", "FAIL"}


# ══════════════════════════════════════════════════════════════════
# 配置
# ══════════════════════════════════════════════════════════════════


def _env(name: str, default: str) -> str:
    return os.environ.get(name, default)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="线上测试环境病案上传解析批量统计（覆盖率 + 关键字段，无日志分析）",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--medlinkai-base", default=_env("MLA_BASE", DEFAULT_MLA_BASE),
                   help="MedLinkAI API base，不含 /api/v1")
    p.add_argument("--ragflow-base", default=_env("RAGFLOW_BASE", DEFAULT_RAGFLOW_BASE),
                   help="RAGFlow API base（含 /api/v1），用于 chunks 统计")
    p.add_argument("--ragflow-api-key", default=_env("RAGFLOW_API_KEY", DEFAULT_RAGFLOW_KEY),
                   help="RAGFlow API Key")
    p.add_argument("--dataset-id", default=_env("RAGFLOW_DATASET_ID", DEFAULT_DATASET_ID),
                   help="数据集 ID（默认 MedLinkAI-v7.0；传空字符串=自动探测 RAGFlow datasets 列表）")
    p.add_argument("--dataset-name", default="",
                   help="自动探测 dataset 时按名称子串筛选（空=取第一个）")
    p.add_argument("pos_pdf_dir", nargs="?", default="",
                   help="待上传 PDF 所在目录（位置参数，等价于 --pdf-dir）")
    p.add_argument("--pdf-dir", default=_env("PDF_DIR", r"D:\futureCode\三月病历\麦济哮喘"),
                   help="待上传 PDF 所在目录")
    p.add_argument("--out-dir", default=_env("OUT_DIR", ""),
                   help="结果输出目录（默认 <脚本目录>/results_online/<时间戳>）")
    p.add_argument("--only", default="", help="只处理文件名包含该关键字的 PDF（空=全部）")
    p.add_argument("--reupload", action="store_true",
                   help="409 重复时先 DELETE 再重传（默认：略过上传，只重新解析）")
    p.add_argument("--stats-only", action="store_true",
                   help="不上传、不触发解析，只对已有文档做统计")
    p.add_argument("--reparse-list", action="store_true",
                   help="不上传：取 GET /api/v1/documents 列表返回的文档，"
                        "调 /{doc_id}/parse 触发重新解析并统计")
    p.add_argument("--list-count", type=int, default=0,
                   help="--reparse-list 模式：从文档列表取多少个文档（0=分页拉取全部）")
    p.add_argument("--exclude-file", default="",
                   help="--reparse-list 模式：每行一个文件名，列表中的文档跳过不重解析")
    p.add_argument("--max-wait", type=int, default=1800, help="单文档进度等待上限（秒）")
    p.add_argument("--poll-interval", type=int, default=5, help="进度轮询间隔（秒）")
    p.add_argument("--concurrency", type=int, default=4,
                   help="并发解析的病例数（每批同时跑多少个文档）")
    p.add_argument("--agent-id", default=_env("MLA_AGENT_ID", DEFAULT_AGENT_ID),
                   help="pipeline agent ID（测试前快照该 pipeline 的 DSL）")
    p.add_argument("--no-dsl-snapshot", action="store_true",
                   help="跳过 pipeline DSL 快照")
    p.add_argument("--compare-with", default=DEFAULT_BASELINE_DIR,
                   help="基线结果目录（按文件名与 summary.json 对比；空字符串=不对比）")
    p.add_argument("--page-size", type=int, default=100, help="文档列表分页大小")
    p.add_argument("--api-key", default=_env("MLA_API_KEY", ""),
                   help="可选：MedLinkAI X-Api-Key（白名单 key 可不传 dataset_id）")
    p.add_argument("--basic-auth", default=_env("MLA_BASIC_AUTH", ""),
                   help="可选：nginx Basic Auth，格式 user:pass（内网直连一般不需要）")
    p.add_argument("--name-abbr", default=_env("MLA_NAME_ABBR", ""),
                   help="病案必填：姓名缩写（默认从 PDF 文件名自动提取）")
    p.add_argument("--gender", default=_env("MLA_GENDER", ""),
                   help="病案必填：性别 code（默认随机 man/woman）")
    p.add_argument("--age", type=int, default=int(_env("MLA_AGE", "0") or 0),
                   help="病案必填：年龄（默认随机 18-80）")
    p.add_argument("--seed", type=int, default=None, help="随机种子（固定 gender/age 便于复现）")
    p.add_argument("--illness-code-l1", default=_env("MLA_IL1_CODE", "1000000"),
                   help="病案必填：一级疾病 code（默认从文件夹名匹配字典推导）")
    p.add_argument("--illness-label-l1", default=_env("MLA_IL1_LABEL", "慢病"),
                   help="病案必填：一级疾病名称")
    p.add_argument("--illness-code-l2", default=_env("MLA_IL2_CODE", "1001000"),
                   help="病案必填：二级疾病 code")
    p.add_argument("--illness-label-l2", default=_env("MLA_IL2_LABEL", "呼吸疾病"),
                   help="病案必填：二级疾病名称")
    p.add_argument("--illness-code-l3", default=_env("MLA_IL3_CODE", "1001001"),
                   help="病案必填：三级疾病 code")
    p.add_argument("--illness-label-l3", default=_env("MLA_IL3_LABEL", "哮喘"),
                   help="病案必填：三级疾病名称")
    ns = p.parse_args()
    if ns.pos_pdf_dir:
        ns.pdf_dir = ns.pos_pdf_dir
    return ns


# ══════════════════════════════════════════════════════════════════
# 工具
# ══════════════════════════════════════════════════════════════════


def pdf_page_count(path: Path) -> int | None:
    """读取 PDF 总页数（PyMuPDF，失败回退 pypdf，再失败返回 None）。"""
    try:
        import fitz  # PyMuPDF
        with fitz.open(str(path)) as doc:
            return doc.page_count
    except Exception:
        pass
    try:
        from pypdf import PdfReader
        with open(path, "rb") as f:
            return len(PdfReader(f).pages)
    except Exception as e:
        print(f"  [warn] 无法读取 PDF 页数 {path.name}: {e}")
        return None


def extract_name_abbr(filename: str, idx: int) -> str:
    """从 PDF 文件名提取姓名缩写（第一个 >=2 的连续字母段），无字母回退 P+序号。"""
    m = re.search(r"[A-Za-z]{2,}", filename)
    if m:
        return m.group(0)[:20]
    return f"P{idx:02d}"


def fetch_illness_catalog(base: str) -> list[dict]:
    """拉取 illness_catalog 字典条目（供文件夹名匹配疾病）。失败返回空列表。"""
    try:
        resp = requests.get(f"{base.rstrip('/')}/api/v1/dict/illness_catalog", timeout=15)
        resp.raise_for_status()
        data = resp.json()
        entries = data.get("entries") or data.get("payload", {}).get("entries") or []
        return [e for e in entries if isinstance(e, dict)]
    except Exception:
        return []


def resolve_illness_from_folder(folder_name: str, entries: list[dict]) -> dict | None:
    """从文件夹名匹配三级疾病，并沿 parent_code 链推导 l2/l1。失败返回 None。"""
    by_code = {str(e.get("code")): e for e in entries if e.get("code")}
    l3_candidates = [
        e for e in entries
        if int(e.get("level") or 0) == 3 and e.get("label") and e["label"] in folder_name
    ]
    if not l3_candidates:
        return None
    pick = max(l3_candidates, key=lambda e: len(e["label"]))
    chain: list[dict] = []
    cur = pick
    while cur and str(cur.get("code")) != "0":
        chain.append(cur)
        cur = by_code.get(str(cur.get("parent_code") or ""))
    chain.sort(key=lambda e: int(e.get("level") or 0))
    out: dict[str, str] = {}
    for e in chain:
        lv = int(e.get("level") or 0)
        if lv == 1:
            out["illness_code_l1"], out["illness_label_l1"] = e["code"], e["label"]
        elif lv == 2:
            out["illness_code_l2"], out["illness_label_l2"] = e["code"], e["label"]
        elif lv == 3:
            out["illness_code_l3"], out["illness_label_l3"] = e["code"], e["label"]
    return out if len(chain) >= 2 else None


def chunk_pages(positions: Any) -> list[int]:
    """从 chunk positions 提取页码列表（1-based）。

    兼容两种格式：
      - [{"value": [page, x0, x1, top, bottom], "Count": n}, ...]
      - [[page, x0, x1, top, bottom], ...]
    """
    pages: list[int] = []
    for pos in positions or []:
        if isinstance(pos, dict):
            v = pos.get("value") or []
        else:
            v = pos or []
        if v and isinstance(v[0], (int, float)):
            pages.append(int(v[0]))
    return pages


def build_page_check(union: set[int], total_pages: int | None) -> dict:
    """按页码并集生成覆盖率检查结论（total_pages 为 None 时无法核对）。"""
    missing = sorted(set(range(1, (total_pages or 0) + 1)) - union) if total_pages else []
    out_of_range = sorted(p for p in union if total_pages and p > total_pages)
    covered = len(union)
    coverage_pct = round(covered * 100.0 / total_pages, 1) if total_pages else None
    if not union:
        verdict = "❌ 无任何 chunk（文档级被过滤 / 解析失败）"
    elif total_pages is None:
        verdict = "⚠️ PDF 页数未知，无法核对"
    elif covered == total_pages and not out_of_range:
        verdict = "✅ 完全覆盖：chunk 页码并集 = PDF 总页数"
    else:
        verdict = (f"❌ 未完全覆盖：覆盖 {covered}/{total_pages} 页，"
                   f"缺失 {missing}，超范围 {out_of_range}")
    return {"covered": covered, "total": total_pages, "coverage_pct": coverage_pct,
            "missing": missing, "out_of_range": out_of_range, "verdict": verdict}


def safe_name(name: str, limit: int = 60) -> str:
    """文件名的安全形式（用于输出文件名）。"""
    cleaned = re.sub(r'[\\/:*?"<>|\r\n\t ]+', "_", name).strip("._")
    return cleaned[:limit] or "unnamed"


def parse_smart_splitter_types(progress_msg: Any) -> dict[str, int]:
    """从 progress_msg 的 "SmartSplitter done: ... Types: {...}" 日志解析类型个数。

    多次出现时取最后一行（重解析场景）。无匹配返回空 dict。
    """
    if not progress_msg:
        return {}
    matches = SMART_SPLITTER_TYPES_RE.findall(str(progress_msg))
    if not matches:
        return {}
    return {name: int(cnt) for name, cnt in re.findall(r"'(\w+)':\s*(\d+)", matches[-1])}


def count_clinical_types(encounters: Any) -> dict[str, int]:
    """汇总 clinical 接口 encounters 各类型列表的记录个数（按 SmartSplitter 类型名）。"""
    counts: dict[str, int] = {}
    for enc in encounters or []:
        if not isinstance(enc, dict):
            continue
        for key, dtype in CLINICAL_KEY_TO_TYPE.items():
            items = enc.get(key)
            if isinstance(items, list) and items:
                counts[dtype] = counts.get(dtype, 0) + len(items)
    return counts


def compare_type_counts(splitter: dict[str, int], clinical: dict[str, int]) -> dict[str, dict]:
    """按类型比对两侧个数；任一侧出现的类型都列出，缺失侧按 0 计。"""
    result: dict[str, dict] = {}
    for dtype in sorted(set(splitter) | set(clinical)):
        s = int(splitter.get(dtype, 0))
        c = int(clinical.get(dtype, 0))
        result[dtype] = {"splitter": s, "clinical": c, "match": s == c}
    return result


def snapshot_pipeline_dsl(base: str, agent_id: str, out_dir: Path) -> Path | None:
    """测试前快照当前 pipeline DSL 到 out_dir/pipeline_dsl.json（便于比对提示词变更）。"""
    url = f"{base.rstrip('/')}/api/v1/pipeline/agents/{agent_id}/dsl"
    try:
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
        try:
            text = json.dumps(resp.json(), ensure_ascii=False, indent=2)
        except ValueError:
            text = resp.text
        path = out_dir / "pipeline_dsl.json"
        path.write_text(text, encoding="utf-8")
        return path
    except Exception as e:
        print(f"[warn] pipeline DSL 快照失败: {e}")
        return None


def load_baseline(compare_with: str) -> tuple[dict[str, dict], str]:
    """加载基线结果目录的 summary.json，返回 (文件名→报告 映射, 目录名)。"""
    if not compare_with:
        return {}, ""
    base_dir = Path(compare_with)
    sj = base_dir / "summary.json"
    if not sj.is_file():
        print(f"[warn] 基线目录缺少 summary.json，跳过对比: {sj}")
        return {}, ""
    try:
        reps = json.loads(sj.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[warn] 基线 summary.json 读取失败: {e}")
        return {}, ""
    out: dict[str, dict] = {}
    for rep in reps:
        name = (rep.get("pdf") or {}).get("name")
        if name:
            out[name] = rep
    return out, base_dir.name


# ══════════════════════════════════════════════════════════════════
# 客户端
# ══════════════════════════════════════════════════════════════════


class MedlinkaiClient:
    """MedLinkAI 两阶段上传 + 状态轮询 + 重新解析。"""

    def __init__(self, base: str, dataset_id: str, page_size: int,
                 api_key: str = "", basic_auth: str = ""):
        self.base = base.rstrip("/")
        self.dataset_id = dataset_id
        self.page_size = page_size
        self.s = requests.Session()
        if api_key:
            self.s.headers["X-Api-Key"] = api_key
        if basic_auth and ":" in basic_auth:
            self.s.auth = tuple(basic_auth.split(":", 1))

    def _ds_params(self) -> dict:
        return {"dataset_id": self.dataset_id} if self.dataset_id else {}

    # ── Step A: 纯文件上传 ──
    def upload_file(self, pdf_path: Path) -> dict:
        """POST /api/v1/documents/upload_file；409 重复时返回 existing_doc_id。"""
        with open(pdf_path, "rb") as f:
            resp = self.s.post(
                f"{self.base}/api/v1/documents/upload_file",
                params=self._ds_params(),
                data={"dataset_id": self.dataset_id} if self.dataset_id else {},
                files={"file": (pdf_path.name, f, "application/pdf")},
                timeout=300,
            )
        if resp.status_code == 409:
            body = resp.json()
            detail = body.get("detail") or body.get("error") or {}
            return {
                "duplicate": True,
                "doc_id": detail.get("existing_doc_id"),
                "message": str(detail.get("message", ""))[:200],
            }
        resp.raise_for_status()
        data = resp.json().get("data", {})
        return {"duplicate": False, "doc_id": data.get("doc_id"), "message": ""}

    # ── Step B: 提交处理（doc_id + 病案必填字段，会触发解析）──
    def upload(self, doc_id: str, case: dict[str, str]) -> dict:
        form = {
            "doc_id": doc_id,
            "name_abbr": case["name_abbr"],
            "gender": case["gender"],
            "age": str(case["age"]),
            "illness_code_l1": case["illness_code_l1"],
            "illness_label_l1": case["illness_label_l1"],
            "illness_code_l2": case["illness_code_l2"],
            "illness_label_l2": case["illness_label_l2"],
            "illness_code_l3": case["illness_code_l3"],
            "illness_label_l3": case["illness_label_l3"],
        }
        if self.dataset_id:
            form["dataset_id"] = self.dataset_id
        resp = self.s.post(f"{self.base}/api/v1/documents/upload", data=form, timeout=120)
        resp.raise_for_status()
        return resp.json()

    # ── 删除（--reupload 用）──
    def delete_document(self, doc_id: str) -> bool:
        resp = self.s.delete(
            f"{self.base}/api/v1/documents/{doc_id}",
            params=self._ds_params(),
            timeout=120,
        )
        return resp.status_code in (200, 204)

    # ── clinical 接口：按 source_id 拉 encounters（类型一致性比对用）──
    def get_clinical(self, patient_id: str, source_id: str) -> dict:
        resp = self.s.get(
            f"{self.base}/api/v1/patients/{patient_id}/clinical",
            params={"source_id": source_id},
            timeout=60,
        )
        resp.raise_for_status()
        return resp.json()

    # ── 状态查询：GET /{doc_id}/status（透传 RAGFlow，返回 run 字符串）──
    def get_status(self, doc_id: str) -> dict | None:
        resp = self.s.get(
            f"{self.base}/api/v1/documents/{doc_id}/status",
            params=self._ds_params(),
            timeout=30,
        )
        resp.raise_for_status()
        return resp.json()

    # ── 进度等待 ──
    def wait_status(self, doc_id: str, max_wait: int, interval: int,
                    wait_running: bool) -> tuple[dict | None, str]:
        """轮询 status 直到终态；返回 (最后状态, 备注)。

        wait_running=True（刚触发解析）：先等 run 变 RUNNING / progress 回落，
        避免把上一轮 DONE 当成本次终态；60s 内没等到也继续等终态并记录备注。
        """
        note = ""
        deadline = time.time() + max_wait
        last: dict | None = None
        if wait_running:
            grace = time.time() + 60
            seen_running = False
            while time.time() < grace:
                try:
                    st = self.get_status(doc_id)
                except requests.RequestException:
                    st = None
                if st:
                    last = st
                    if st.get("run") == "RUNNING" or float(st.get("progress") or 0) < 1.0:
                        seen_running = True
                        break
                time.sleep(min(interval, 3))
            if not seen_running:
                note += "触发解析后 60s 内未观察到 RUNNING（可能解析未启动或秒完成）。 "
        while time.time() < deadline:
            try:
                st = self.get_status(doc_id)
                if st:
                    last = st
                    run = str(st.get("run") or "")
                    progress = float(st.get("progress") or 0)
                    if run in TERMINAL_RUNS or progress >= 1.0:
                        return st, note
            except requests.RequestException as e:
                print(f"  [warn] 状态查询失败: {e}")
            time.sleep(interval)
        return last, note + "进度等待超时（未达终态）。 "

    # ── 触发重新解析（--reparse-list 用）：POST /{doc_id}/parse ──
    def trigger_parse(self, doc_id: str) -> bool:
        resp = self.s.post(
            f"{self.base}/api/v1/documents/{doc_id}/parse",
            params=self._ds_params(),
            timeout=60,
        )
        resp.raise_for_status()
        return True

    # ── 文档列表（--reparse-list 用），返回 [{doc_id, patient_id, name, size_kb}] ──
    def list_docs(self, page: int, page_size: int) -> list[dict]:
        resp = self.s.get(
            f"{self.base}/api/v1/documents",
            params={**self._ds_params(), "page": page, "page_size": page_size},
            timeout=30,
        )
        resp.raise_for_status()
        body = resp.json()
        out = []
        for d in body.get("documents", []):
            if not d.get("doc_id"):
                continue
            size = int(d.get("size") or 0)
            out.append({
                "doc_id": d["doc_id"],
                "patient_id": d.get("patient_id") or "",
                "name": d.get("name") or d["doc_id"],
                "size_kb": round(size / 1024, 1) if size else None,
            })
        return out

    # ── 按文件名查找已有文档（skip-upload / stats-only 兜底），返回 (doc_id, patient_id) ──
    def find_existing(self, filename: str) -> tuple[str | None, str]:
        for page in range(1, 11):
            try:
                resp = self.s.get(
                    f"{self.base}/api/v1/documents",
                    params={**self._ds_params(), "page": page, "page_size": self.page_size},
                    timeout=30,
                )
                resp.raise_for_status()
                body = resp.json()
                docs = body.get("documents", [])
                for d in docs:
                    name = d.get("name") or ""
                    if name == filename or name.endswith(filename):
                        return d.get("doc_id"), d.get("patient_id") or ""
                if len(docs) < self.page_size:
                    break
            except requests.RequestException:
                break
        return None, ""


class RagflowClient:
    """RAGFlow datasets 探测 + chunks 查询。"""

    def __init__(self, base: str, api_key: str):
        self.base = base.rstrip("/")
        self.headers = {"Authorization": f"Bearer {api_key}"}

    def list_datasets(self) -> list[dict]:
        resp = requests.get(f"{self.base}/datasets",
                            params={"page": 1, "page_size": 100},
                            headers=self.headers, timeout=30)
        resp.raise_for_status()
        data = resp.json().get("data")
        return data if isinstance(data, list) else []

    def resolve_dataset(self, dataset_id: str, dataset_name: str) -> str:
        """确定 dataset_id：手动指定 > 按名称匹配 > 唯一/第一个 > 默认值兜底。"""
        if dataset_id:
            return dataset_id
        try:
            datasets = self.list_datasets()
        except Exception as e:
            print(f"[warn] 自动探测 dataset 失败（{e}），回退默认 {DEFAULT_DATASET_ID}")
            return DEFAULT_DATASET_ID
        if not datasets:
            print(f"[warn] RAGFlow 无 dataset，回退默认 {DEFAULT_DATASET_ID}")
            return DEFAULT_DATASET_ID
        if dataset_name:
            hit = [d for d in datasets if dataset_name in str(d.get("name", ""))]
            if hit:
                pick = hit[0]
                print(f"自动探测 dataset（名称匹配 '{dataset_name}'）：{pick['name']} → {pick['id']}")
                return pick["id"]
        pick = datasets[0]
        if len(datasets) > 1:
            names = ", ".join(f"{d.get('name')}({d.get('id')[:8]}…)" for d in datasets)
            print(f"[warn] RAGFlow 有 {len(datasets)} 个 dataset：{names}；默认取第一个，"
                  f"可用 --dataset-id / --dataset-name 指定")
        print(f"自动探测 dataset：{pick.get('name')} → {pick['id']}")
        return pick["id"]

    def list_chunks(self, dataset_id: str, doc_id: str) -> tuple[list[dict], dict]:
        """分页拉取文档全部 chunks；返回 (chunks, doc_info)。"""
        chunks: list[dict] = []
        doc_info: dict = {}
        page = 1
        while True:
            resp = requests.get(
                f"{self.base}/datasets/{dataset_id}/documents/{doc_id}/chunks",
                params={"page": page, "page_size": 100},
                headers=self.headers,
                timeout=60,
            )
            resp.raise_for_status()
            body = resp.json()
            data = body.get("data", {})
            items = data.get("chunks", [])
            chunks.extend(items)
            if data.get("doc"):
                doc_info = data["doc"]
            total = int(data.get("total", 0) or 0)
            if page * 100 >= total or not items:
                break
            page += 1
        return chunks, doc_info


# ══════════════════════════════════════════════════════════════════
# 报告生成
# ══════════════════════════════════════════════════════════════════


def render_doc_md(pdf: dict, rep: dict) -> str:
    pages = rep.get("pages", {})
    check = pages.get("check", {})
    lines: list[str] = []
    lines.append(f"# 线上统计：{pdf['name']}")
    lines.append("")
    lines.append("## 基本信息")
    lines.append("")
    lines.append(f"- 文件：`{pdf['name']}`")
    lines.append(f"- 大小：{pdf.get('size_kb')} KB")
    lines.append(f"- PDF 总页数：{pdf.get('pages') or '-'}")
    lines.append(f"- doc_id：`{rep.get('doc_id')}`")
    lines.append(f"- 处理方式：{rep.get('mode')}")
    lines.append(f"- 状态：run={rep.get('run')}  progress={rep.get('progress')}")
    lines.append(f"- chunk_count(status)：{rep.get('chunk_count_api')}  "
                 f"orm_synced：{rep.get('orm_synced')}")
    lines.append(f"- 处理耗时(服务端)：{rep.get('process_duration')}s  "
                 f"脚本耗时：{rep.get('elapsed_s')}s")
    if rep.get("note"):
        lines.append(f"- 备注：{rep.get('note')}")
    if rep.get("before"):
        b = rep["before"]
        lines.append(f"- 重解析前快照（无基线结果）：chunk_count={b.get('chunk_count')} "
                     f"run={b.get('run')} clinical 类型记录数={b.get('type_counts')}")
    if rep.get("baseline"):
        lines.append(f"- 基线对比（{rep['baseline']['dir']}）：基线 chunks={rep['baseline']['chunks']} "
                     f"→ 本次 chunks={len(rep.get('chunks') or [])}")
    lines.append("")
    lines.append("## 1. 页面覆盖率")
    lines.append("")
    chunks = rep.get("chunks", [])
    if not chunks:
        lines.append("**该文档没有任何 chunk（文档级被过滤或解析失败）**")
    else:
        lines.append("| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |")
        lines.append("|---|----------------|------|----------|----------|")
        for i, c in enumerate(chunks, 1):
            cpg = c["pages"]
            span = f"{min(cpg)}-{max(cpg)}" if cpg else "-"
            summary = (c.get("content") or "").replace("|", "/").replace("\n", " ")[:40]
            lines.append(f"| {i} | {c['chunk_id'][:8]} | {len(cpg)} | {span} | {summary} |")
        lines.append("")
        lines.append(f"- chunks 总数：{len(chunks)}")
        lines.append(f"- 各 chunk 页数合计（含跨页重复）：{pages.get('page_sum')}")
        lines.append(f"- 页码并集：`{sorted(pages.get('union', []))}`")
        lines.append(f"- 覆盖页数：{check.get('covered')} / {check.get('total')}"
                     f"（覆盖率 {check.get('coverage_pct', '-')}%）")
        lines.append(f"- 缺失页：`{check.get('missing')}`  超范围页：`{check.get('out_of_range')}`")
        lines.append(f"- **结论：{check.get('verdict')}**")
    lines.append("")
    lines.append("## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）")
    lines.append("")
    tm = rep.get("type_match", {})
    if not tm:
        lines.append("**两侧均无可比对类型记录（SmartSplitter 日志缺失或 clinical 无类型）**")
    else:
        lines.append("| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |")
        lines.append("|------|------|---------------------|---------------|------|")
        for dtype, item in tm.items():
            mark = "✅" if item["match"] else "❌"
            lines.append(f"| {dtype} | {DOC_TYPE_LABELS.get(dtype, dtype)} | {item['splitter']} "
                         f"| {item['clinical']} | {mark} |")
        bad = [dtype for dtype, item in tm.items() if not item["match"]]
        lines.append("")
        lines.append(f"- 判定：{'✅ 全部类型匹配' if not bad else '❌ 不匹配类型: ' + ', '.join(bad)}")
    lines.append("")
    return "\n".join(lines)


# ══════════════════════════════════════════════════════════════════
# 主流程
# ══════════════════════════════════════════════════════════════════


def collect_pdfs(pdf_dir: Path, only: str) -> list[dict]:
    pdfs: list[dict] = []
    for f in sorted(pdf_dir.iterdir()):
        if not f.is_file() or f.suffix.lower() != ".pdf":
            continue
        if only and only not in f.name:
            continue
        pdfs.append({
            "path": f,
            "name": f.name,
            "size_kb": round(f.stat().st_size / 1024, 1),
            "pages": pdf_page_count(f),
        })
    return pdfs


def process_one(args: argparse.Namespace, idx: int, total: int, pdf: dict,
                dataset_id: str, illness_case: dict, baseline_map: dict[str, dict],
                baseline_label: str, docs_dir: Path) -> dict:
    """单文档处理（可并发）：复用/上传 → 重解析前快照 → 触发解析 → 进度轮询 → 覆盖率与类型统计。"""
    name = pdf["name"]
    tag = f"[{idx}/{total} {name}]"
    # 每任务独立客户端，避免跨线程共享 requests.Session
    mla = MedlinkaiClient(args.medlinkai_base, dataset_id, args.page_size,
                          api_key=args.api_key, basic_auth=args.basic_auth)
    rf = RagflowClient(args.ragflow_base, args.ragflow_api_key)
    brep = baseline_map.get(name)

    if args.reparse_list:
        print(f"{tag} （doc_id={pdf.get('doc_id')}）")
        case: dict[str, Any] = {}
    else:
        case = {
            "name_abbr": args.name_abbr or extract_name_abbr(name, idx),
            "gender": args.gender or random.choice(["man", "woman"]),
            "age": args.age or random.randint(18, 80),
            **illness_case,
        }
        print(f"{tag} （PDF 页数: {pdf['pages']}）"
              f" 病案: {case['name_abbr']}/{case['gender']}/{case['age']}岁")
    rep: dict[str, Any] = {
        "pdf": pdf,
        "doc_id": None,
        "mode": "-",
        "run": None,
        "progress": None,
        "chunk_count_api": None,
        "orm_synced": None,
        "process_duration": None,
        "begin_at": datetime.now().isoformat(timespec="seconds"),
        "end_at": None,
        "elapsed_s": None,
        "before": None,
        "baseline": {"dir": baseline_label,
                     "chunks": len(brep.get("chunks") or [])} if brep else None,
        "chunks": [],
        "pages": {},
        "type_match": {},
        "note": "",
    }

    t0 = time.time()
    doc_id: str | None = None
    patient_id = ""
    triggered = False  # 本次是否已触发（重新）解析

    # ── 上传 / 复用阶段（不立即触发解析，先留给"重解析前快照"）──
    if args.reparse_list:
        doc_id = pdf.get("doc_id")
        patient_id = pdf.get("patient_id") or ""
        rep["mode"] = "reparse-list"
    elif args.stats_only:
        doc_id, patient_id = mla.find_existing(name)
        rep["mode"] = "stats-only"
        if doc_id:
            print(f"{tag} stats-only：找到已有文档 doc_id={doc_id}")
        else:
            rep["note"] += "stats-only 模式下未找到同名已有文档。 "
            print(f"{tag} [warn] 未找到同名已有文档，跳过")
    elif args.reupload:
        try:
            up = mla.upload_file(pdf["path"])
            if up.get("duplicate") and up.get("doc_id"):
                print(f"{tag} 409 重复 doc_id={up['doc_id']} → 删除后重传")
                mla.delete_document(up["doc_id"])
                time.sleep(2)
                up = mla.upload_file(pdf["path"])
            doc_id = up.get("doc_id")
            if doc_id:
                mla.upload(doc_id, case)
                triggered = True
                rep["mode"] = "reupload+upload" if up.get("duplicate") else "upload_file+upload"
                print(f"{tag} 上传并触发解析 OK → doc_id={doc_id}")
        except Exception as e:
            rep["note"] += f"上传失败: {e} "
            print(f"{tag} [error] 上传失败: {e}")
    else:
        # 默认：先查已有文档（略过上传）→ 直接重新解析；没有再上传
        doc_id, patient_id = mla.find_existing(name)
        if doc_id:
            rep["mode"] = "existing+reparse"
            print(f"{tag} 已上传，略过上传 → doc_id={doc_id}")
        else:
            try:
                up = mla.upload_file(pdf["path"])
                if up.get("duplicate"):
                    # 列表里没匹配到（可能名字被改过），复用 409 返回的 doc_id
                    doc_id = up.get("doc_id")
                    rep["mode"] = "duplicate+reparse"
                    rep["note"] += f"409 重复：{up.get('message')} "
                    print(f"{tag} 409 重复：复用 doc_id={doc_id}")
                else:
                    doc_id = up.get("doc_id")
                    rep["mode"] = "upload_file+upload"
                    print(f"{tag} upload_file OK → doc_id={doc_id}")
                if doc_id:
                    mla.upload(doc_id, case)
                    triggered = True
                    if rep["mode"] != "duplicate+reparse":
                        print(f"{tag} upload OK（已触发解析）")
            except Exception as e:
                rep["note"] += f"上传失败: {e} "
                print(f"{tag} [error] 上传失败: {e}")

    if not doc_id:
        rep["end_at"] = datetime.now().isoformat(timespec="seconds")
        rep["elapsed_s"] = round(time.time() - t0, 1)
        return rep
    rep["doc_id"] = doc_id

    # ── 重解析前快照：无基线结果时保存旧 chunk 数/记录数，便于前后对比 ──
    if not triggered and not args.stats_only and brep is None:
        try:
            st0 = mla.get_status(doc_id) or {}
            before_types: dict[str, int] = {}
            if patient_id:
                try:
                    clinical0 = mla.get_clinical(patient_id, doc_id)
                    before_types = count_clinical_types(clinical0.get("encounters") or [])
                except Exception:
                    pass
            rep["before"] = {"chunk_count": st0.get("chunk_count"),
                             "run": st0.get("run"),
                             "type_counts": before_types}
            print(f"{tag} 无基线结果，已保存重解析前快照: chunks={st0.get('chunk_count')} "
                  f"type_counts={before_types}")
        except Exception as e:
            rep["note"] += f"重解析前快照失败: {e} "

    # ── 触发重新解析（不上传、不改病案字段）──
    if not triggered and not args.stats_only:
        try:
            mla.trigger_parse(doc_id)
            triggered = True
            print(f"{tag} 已触发重新解析 → doc_id={doc_id}")
        except Exception as e:
            rep["note"] += f"触发重新解析失败: {e} "
            print(f"{tag} [error] 触发重新解析失败: {e}")

    # ── 进度监控（status 接口）──
    full_progress_msg = ""
    try:
        status, wait_note = mla.wait_status(doc_id, args.max_wait, args.poll_interval,
                                            wait_running=triggered)
        rep["note"] += wait_note
        if status:
            rep["run"] = status.get("run")
            rep["progress"] = status.get("progress")
            rep["chunk_count_api"] = status.get("chunk_count")
            rep["orm_synced"] = status.get("orm_synced")
            rep["process_duration"] = status.get("process_duration")
            full_progress_msg = str(status.get("progress_msg") or "")
            if full_progress_msg:
                rep["progress_msg"] = full_progress_msg[:300]
            print(f"{tag} run={rep['run']} progress={rep['progress']} "
                  f"chunk_count={rep.get('chunk_count_api')} orm_synced={rep.get('orm_synced')}")
    except Exception as e:
        rep["note"] += f"状态查询失败: {e} "
        print(f"{tag} [error] 状态查询失败: {e}")

    # ── 覆盖率统计（chunks positions；终态后 ES 近实时延迟，为空时重试）──
    chunks: list[dict] = []
    try:
        for attempt in range(1, 7):
            chunks, _doc_info = rf.list_chunks(dataset_id, doc_id)
            if chunks or attempt == 6:
                break
            if attempt == 1:
                print(f"{tag} chunks 暂为 0（ES 近实时延迟），重试中…")
            time.sleep(10)
        rep["chunks"] = []
        union: set[int] = set()
        page_sum = 0
        for c in chunks:
            pg = chunk_pages(c.get("positions"))
            if not pg:
                # 部分 chunk（如表格型检验报告）positions 为空，但 row_position_int 有坐标
                pg = chunk_pages(c.get("row_position_int"))
            pg_set = set(pg)
            rep["chunks"].append({
                "chunk_id": c.get("id", ""),
                "pages": sorted(pg_set),
                "page_count_raw": len(pg),
                "content": (c.get("content") or "")[:300],
            })
            union.update(pg_set)
            page_sum += len(pg_set)
        total_pages = pdf.get("pages")
        check = build_page_check(union, total_pages)
        missing = check["missing"]
        covered = check["covered"]
        coverage_pct = check["coverage_pct"]
        rep["pages"] = {
            "union": sorted(union),
            "page_sum": page_sum,
            "check": check,
        }
        print(f"{tag} chunks={len(chunks)} 覆盖页数={covered}/{total_pages}"
              f"（{coverage_pct}%） 缺失={missing}")
    except Exception as e:
        rep["note"] += f"chunks 查询失败: {e} "
        print(f"{tag} [error] chunks 查询失败: {e}")

    # ── 类型一致性统计（SmartSplitter 日志 vs clinical encounters）──
    try:
        splitter_types = parse_smart_splitter_types(full_progress_msg)
        if not splitter_types:
            rep["note"] += "progress_msg 未找到 SmartSplitter 类型日志。 "
        if not patient_id:
            _doc_id2, patient_id = mla.find_existing(name)
        clinical_types: dict[str, int] = {}
        if patient_id:
            clinical = mla.get_clinical(patient_id, doc_id)
            clinical_types = count_clinical_types(clinical.get("encounters") or [])
        else:
            rep["note"] += "未获取到 patient_id，跳过 clinical 比对。 "
        rep["type_match"] = compare_type_counts(splitter_types, clinical_types)
        bad = [f"{t}({v['splitter']}/{v['clinical']})"
               for t, v in rep["type_match"].items() if not v["match"]]
        if bad:
            print(f"{tag} 类型不匹配: {', '.join(bad)}")
        else:
            print(f"{tag} 类型匹配 ✅ {len(rep['type_match'])} 类，"
                  f"共 {sum(v['splitter'] for v in rep['type_match'].values())} chunks")
    except Exception as e:
        rep["note"] += f"类型一致性统计失败: {e} "
        print(f"{tag} [error] 类型一致性统计失败: {e}")

    rep["end_at"] = datetime.now().isoformat(timespec="seconds")
    rep["elapsed_s"] = round(time.time() - t0, 1)

    # ── 写结果文件 ──
    base = safe_name(name)
    (docs_dir / f"{base}.md").write_text(render_doc_md(pdf, rep), encoding="utf-8")
    (docs_dir / f"{base}.json").write_text(
        json.dumps(rep, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    return rep


def run() -> int:
    args = parse_args()
    pdf_dir = Path(args.pdf_dir)
    if not args.reparse_list and not pdf_dir.is_dir():
        print(f"[error] PDF 目录不存在: {pdf_dir}")
        return 1

    # 输出目录
    out_root = Path(args.out_dir) if args.out_dir else Path(__file__).resolve().parent / "results_online"
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = out_root / stamp
    docs_dir = out / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)

    # 测试前快照 pipeline DSL + 加载基线结果（便于事后比对是否提示词变更）
    dsl_path = None
    if not args.no_dsl_snapshot:
        dsl_path = snapshot_pipeline_dsl(args.medlinkai_base, args.agent_id, out)
    baseline_map, baseline_label = load_baseline(args.compare_with)

    # 疾病三级分类：优先从文件夹名匹配字典推导，失败回退命令行默认（--reparse-list 不改病案字段，跳过）
    if args.reparse_list:
        illness_case: dict[str, str] = {}
    else:
        illness_entries = fetch_illness_catalog(args.medlinkai_base)
        folder_illness = resolve_illness_from_folder(pdf_dir.name, illness_entries)
        illness_case = {
            "illness_code_l1": (folder_illness or {}).get("illness_code_l1") or args.illness_code_l1,
            "illness_label_l1": (folder_illness or {}).get("illness_label_l1") or args.illness_label_l1,
            "illness_code_l2": (folder_illness or {}).get("illness_code_l2") or args.illness_code_l2,
            "illness_label_l2": (folder_illness or {}).get("illness_label_l2") or args.illness_label_l2,
            "illness_code_l3": (folder_illness or {}).get("illness_code_l3") or args.illness_code_l3,
            "illness_label_l3": (folder_illness or {}).get("illness_label_l3") or args.illness_label_l3,
        }
    if args.seed is not None:
        random.seed(args.seed)

    # dataset_id：手动指定 > 自动探测
    rf_probe = RagflowClient(args.ragflow_base, args.ragflow_api_key)
    dataset_id = rf_probe.resolve_dataset(args.dataset_id, args.dataset_name)

    mode_desc = ("取文档列表只重解析+统计，不上传" if args.reparse_list
                 else "只统计，不触发解析" if args.stats_only
                 else "重复时删除重传" if args.reupload
                 else "重复时略过上传，只重新解析（默认，不改病案字段）")

    print("=" * 72)
    print("线上测试环境病案上传解析批量统计")
    print("=" * 72)
    print(f"MedLinkAI : {args.medlinkai_base}")
    print(f"RAGFlow   : {args.ragflow_base}")
    print(f"dataset   : {dataset_id}")
    if args.reparse_list:
        print(f"文档来源   : GET /api/v1/documents 列表前 {args.list_count} 个")
    else:
        print(f"PDF 目录   : {pdf_dir}")
        print(f"病案字段   : name_abbr/gender/age 每文档自动生成；疾病=文件夹「{pdf_dir.name}」推导 → "
              f"{illness_case['illness_label_l3']}({illness_case['illness_code_l3']})")
    print(f"重复处理   : {mode_desc}")
    print(f"并发数    : {args.concurrency}")
    print(f"DSL 快照  : {dsl_path or '失败/跳过'}")
    print(f"基线对比  : {baseline_label or '无'}")
    print(f"输出目录   : {out}")
    print("=" * 72)

    mla = MedlinkaiClient(args.medlinkai_base, dataset_id, args.page_size,
                          api_key=args.api_key, basic_auth=args.basic_auth)

    if args.reparse_list:
        # 从文档列表取已有文档（不上传）；分页拉取全部，--list-count 限制条数
        docs: list[dict] = []
        page = 1
        while True:
            batch = mla.list_docs(page=page, page_size=args.page_size)
            docs.extend(batch)
            if len(batch) < args.page_size:
                break
            if args.list_count > 0 and len(docs) >= args.list_count:
                break
            page += 1
        if args.list_count > 0:
            docs = docs[:args.list_count]
        exclude: set[str] = set()
        if args.exclude_file:
            ep = Path(args.exclude_file)
            if ep.is_file():
                exclude = {ln.strip() for ln in ep.read_text(encoding="utf-8").splitlines()
                           if ln.strip()}
        if args.only:
            docs = [d for d in docs if args.only in d["name"]]
        if exclude:
            docs = [d for d in docs if d["name"] not in exclude]
        pdfs: list[dict] = [
            {"path": None, "name": d["name"], "size_kb": d["size_kb"], "pages": None,
             "doc_id": d["doc_id"], "patient_id": d["patient_id"]}
            for d in docs
        ]
        if not pdfs:
            print("[error] 文档列表为空")
            return 1
        print(f"从文档列表取 {len(pdfs)} 个文档"
              + (f"（排除清单 {len(exclude)} 个）" if exclude else ""))
    else:
        pdfs = collect_pdfs(pdf_dir, args.only)
        if not pdfs:
            print("[error] 未找到 PDF 文件")
            return 1
        print(f"发现 {len(pdfs)} 个 PDF")

    # ── 并发处理（--concurrency 个病例同时跑）──
    all_reports = [None] * len(pdfs)
    with ThreadPoolExecutor(max_workers=max(1, args.concurrency)) as ex:
        futures = {
            ex.submit(process_one, args, i, len(pdfs), pdf, dataset_id,
                      illness_case, baseline_map, baseline_label, docs_dir): i
            for i, pdf in enumerate(pdfs, 1)
        }
        for fut in as_completed(futures):
            i = futures[fut]
            try:
                all_reports[i - 1] = fut.result()
            except Exception as e:
                print(f"[error] {pdfs[i - 1]['name']} 处理异常: {e}")
                all_reports[i - 1] = {
                    "pdf": pdfs[i - 1], "doc_id": None, "mode": "-", "run": None,
                    "progress": None, "chunk_count_api": None, "orm_synced": None,
                    "process_duration": None, "begin_at": None, "end_at": None,
                    "elapsed_s": None, "before": None, "baseline": None,
                    "chunks": [], "pages": {}, "type_match": {},
                    "note": f"处理异常: {e} ",
                }
    all_reports = [r for r in all_reports if r is not None]

    # ── 汇总 ──
    type_cols = list(DOC_TYPE_LABELS.values())
    summary_md = ["# 线上批量统计汇总", "",
                  f"- 时间：{stamp}", f"- PDF 目录：{pdf_dir}", f"- dataset_id：{dataset_id}",
                  f"- MedLinkAI：{args.medlinkai_base}  RAGFlow：{args.ragflow_base}",
                  f"- 重复处理：{mode_desc}", f"- 文档数：{len(all_reports)}",
                  f"- 并发数：{args.concurrency}；DSL 快照："
                  f"{'pipeline_dsl.json' if dsl_path else '失败/跳过'}",
                  f"- 基线对比：{baseline_label or '无'}", "",
                  "| 文件 | PDF页数 | doc_id | run | chunks | 覆盖页 | 覆盖率% | 缺失页 "
                  + "".join(f"| {lb}" for lb in type_cols) + " |",
                  "|------|---------|--------|-----|--------|--------|---------|--------"
                  + "|----" * len(type_cols) + "|"]
    for rep in all_reports:
        p = rep["pdf"]
        check = rep["pages"].get("check", {})
        tm = rep.get("type_match", {})

        def cell(dtype: str) -> str:
            item = tm.get(dtype)
            if not item or (item["splitter"] == 0 and item["clinical"] == 0):
                return "-"
            mark = "" if item["match"] else "✗"
            return f"{item['splitter']}/{item['clinical']}{mark}"

        summary_md.append(
            f"| {p['name']} | {p['pages'] or '-'} | {rep['doc_id'] or '-'} | {rep['run'] or '-'} "
            f"| {len(rep['chunks'])} | {check.get('covered', '-')} "
            f"| {check.get('coverage_pct', '-')} | {check.get('missing', [])} "
            + "".join(f"| {cell(t)}" for t in DOC_TYPE_LABELS) + " |")

    n_total = len(all_reports)
    n_done = sum(1 for r in all_reports if r.get("run") == "DONE")
    n_full = sum(1 for r in all_reports
                 if r["pages"].get("check", {}).get("verdict", "").startswith("✅"))
    n_match = sum(1 for r in all_reports
                  if r.get("type_match")
                  and all(v["match"] for v in r["type_match"].values()))
    summary_md += [
        "",
        f"- run=DONE：{n_done}/{n_total}；页面完全覆盖：{n_full}/{n_total}；"
        f"类型全部匹配：{n_match}/{n_total}",
        "",
        "判定说明：单元格=SmartSplitter chunk 数 / clinical 记录数，✗=两侧不一致；"
        "-=两侧均无该类型记录",
        "",
    ]

    # ── 与基线结果对比 ──
    if baseline_map:
        summary_md += [f"## 与基线 {baseline_label} 对比", "",
                       "| 文件 | 基线 chunks | 新 chunks | Δ | 类型变化（类型: 旧 splitter/clinical → 新） |",
                       "|------|------------|-----------|---|--------------------------------------------|"]
        for rep in all_reports:
            bname = rep["pdf"]["name"]
            brep = baseline_map.get(bname)
            new_n = len(rep.get("chunks") or [])
            if not brep:
                bef = rep.get("before") or {}
                summary_md.append(f"| {bname} | - | {new_n} | - "
                                  f"| 无基线（重解析前 chunks={bef.get('chunk_count')}） |")
                continue
            old_n = len(brep.get("chunks") or [])
            otm = brep.get("type_match") or {}
            ntm = rep.get("type_match") or {}
            changes = []
            for t in sorted(set(otm) | set(ntm)):
                o_s = f"{otm[t]['splitter']}/{otm[t]['clinical']}" if t in otm else "-"
                n_s = f"{ntm[t]['splitter']}/{ntm[t]['clinical']}" if t in ntm else "-"
                if o_s != n_s:
                    changes.append(f"{DOC_TYPE_LABELS.get(t, t)} {o_s}→{n_s}")
            summary_md.append(f"| {bname} | {old_n} | {new_n} | {new_n - old_n:+d} "
                              f"| {'; '.join(changes) or '无'} |")
        summary_md.append("")

    (out / "summary.md").write_text("\n".join(summary_md), encoding="utf-8")
    (out / "summary.json").write_text(
        json.dumps(all_reports, ensure_ascii=False, indent=2, default=str), encoding="utf-8")

    print("\n" + "=" * 72)
    print(f"完成：{len(all_reports)} 个文档，结果目录: {out}")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(run())
