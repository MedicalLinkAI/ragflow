#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""病案 PDF 上传 + 解析基准测试脚本（MedLinkAI + RAGFlow 本地环境）。

流程（按文档逐个执行）：
1. 读取 --pdf-dir 下所有 PDF，用 PyMuPDF 读取总页数
2. 两阶段上传：POST /api/v1/documents/upload_file → POST /api/v1/documents/upload
3. 轮询 GET /api/v1/documents 监控进度，直到 progress >= 1（run 终态）
4. 从 RAGFlow chunks API 拉取每个 chunk 的 positions，统计页数并与 PDF 总页数核对
5. 抓取 docker logs --container 日志，按 doc_id 切分，分析 6 类文档（门诊/入院/出院/购药/
   处方/检查报告）是否因核心字段缺失被过滤
6. 每个文档输出一份基准结果文件（Markdown + JSON），并生成汇总 summary.md

所有接口地址 / 凭据 / 默认病案字段均可通过命令行参数或环境变量配置：

环境变量:  MLA_BASE / RAGFLOW_BASE / RAGFLOW_API_KEY / RAGFLOW_DATASET_ID /
           PDF_DIR / WORKER_CONTAINER / OUT_DIR
用法:
    python benchmark_upload.py                      # 全部默认（本地环境）
    python benchmark_upload.py --only 哮喘          # 只处理文件名含"哮喘"的
    python benchmark_upload.py --skip-upload        # 不上传，只分析已有文档
    python benchmark_upload.py --force-reupload     # 409 重复时先删除再重传（会重新触发解析）
"""

from __future__ import annotations

import argparse
import json
import os
import random
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any

import requests

# ══════════════════════════════════════════════════════════════════
# 常量：6 类文档核心字段（缺失则可能被过滤）
# ══════════════════════════════════════════════════════════════════

DOC_TYPE_CORE_FIELDS: dict[str, list[str]] = {
    "OutpatientRecord": ["encounter_date", "chief_complaint", "diagnosis"],
    "AdmissionRecord": ["encounter_date", "dm_admission_time", "cc_text", "department"],
    "DischargeRecord": ["admission_date", "discharge_date", "department", "outcome"],
    "MedicationRecord": ["encounter_date", "pharmacy", "payment_total"],
    "PrescriptionRecord": ["encounter_date", "prescriber", "diagnosis"],
    "ExaminationReport": ["exam_date", "report_date", "exam_name", "body_part", "department"],
    "LabReport": ["report_time", "report_category", "report_name"],
}

DOC_TYPE_LABELS: dict[str, str] = {
    "OutpatientRecord": "门诊",
    "AdmissionRecord": "入院",
    "DischargeRecord": "出院",
    "MedicationRecord": "购药",
    "PrescriptionRecord": "处方",
    "ExaminationReport": "检查报告",
    "LabReport": "检验报告",
}

# RAGFlow run 状态映射
RUN_MAP = {0: "UNSTART", 1: "RUNNING", 2: "CANCEL", 3: "DONE", 4: "FAIL"}

# ══════════════════════════════════════════════════════════════════
# 配置
# ══════════════════════════════════════════════════════════════════


def _env(name: str, default: str) -> str:
    return os.environ.get(name, default)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="病案 PDF 上传解析基准测试（MedLinkAI + RAGFlow）",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--medlinkai-base", default=_env("MLA_BASE", "http://localhost:3160"),
                   help="MedLinkAI API base，不含 /api/v1")
    p.add_argument("--ragflow-base", default=_env("RAGFLOW_BASE", "http://localhost:19380/api/v1"),
                   help="RAGFlow API base（含 /api/v1）")
    p.add_argument("--ragflow-api-key", default=_env("RAGFLOW_API_KEY", "ragflow-ZihvOw9xL9fS9nKMWPrAHe3Qxeb9E2eo6VzXyIcIyq4"),
                   help="RAGFlow API Key")
    p.add_argument("--dataset-id", default=_env("RAGFLOW_DATASET_ID", "fb850778372011f195bd2a5fbb884e34"),
                   help="数据集 ID（RAGFlow dataset）")
    p.add_argument("--pdf-dir", default=_env("PDF_DIR", r"D:\futureCode\三月病历\麦济哮喘"),
                   help="待上传 PDF 所在目录")
    p.add_argument("--container", default=_env("WORKER_CONTAINER", "ragflow-dev-worker"),
                   help="worker 容器名（docker logs 用）")
    p.add_argument("--out-dir", default=_env("OUT_DIR", ""),
                   help="结果输出目录（默认 <脚本目录>/results/<时间戳>）")
    p.add_argument("--only", default="", help="只处理文件名包含该关键字的 PDF（空=全部）")
    p.add_argument("--skip-upload", action="store_true", help="跳过上传，只对已有文档做分析")
    p.add_argument("--force-reupload", action="store_true",
                   help="上传遇 409 重复时先 DELETE 再重传（会重新触发解析）")
    p.add_argument("--max-wait", type=int, default=900, help="单文档进度等待上限（秒）")
    p.add_argument("--poll-interval", type=int, default=5, help="进度轮询间隔（秒）")
    p.add_argument("--page-size", type=int, default=100, help="监控接口分页大小")
    p.add_argument("--log-tail", type=int, default=100000, help="docker logs 抓取行数")
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
                   help="病案必填：一级疾病名称（默认从文件夹名匹配字典推导）")
    p.add_argument("--illness-code-l2", default=_env("MLA_IL2_CODE", "1001000"),
                   help="病案必填：二级疾病 code（默认从文件夹名匹配字典推导）")
    p.add_argument("--illness-label-l2", default=_env("MLA_IL2_LABEL", "呼吸疾病"),
                   help="病案必填：二级疾病名称（默认从文件夹名匹配字典推导）")
    p.add_argument("--illness-code-l3", default=_env("MLA_IL3_CODE", "1001001"),
                   help="病案必填：三级疾病 code（默认从文件夹名匹配字典推导）")
    p.add_argument("--illness-label-l3", default=_env("MLA_IL3_LABEL", "哮喘"),
                   help="病案必填：三级疾病名称（默认从文件夹名匹配字典推导）")
    return p.parse_args()


# ══════════════════════════════════════════════════════════════════
# 工具
# ══════════════════════════════════════════════════════════════════


def pdf_page_count(path: Path) -> int | None:
    """读取 PDF 总页数（PyMuPDF，失败返回 None）。"""
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
    """从 PDF 文件名提取姓名缩写（第一个 >=2 的连续字母段）。

    例："1_GWYA-女-35岁222.pdf" → GWYA；"chho-麦济122-…pdf" → chho；
        "麦济WRNA(2).pdf" → WRNA；无字母时回退 P+序号。
    """
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
    """从文件夹名匹配三级疾病，并沿 parent_code 链推导 l2/l1。

    例：文件夹名"麦济哮喘" → l3=哮喘(1001001) → l2=呼吸疾病(1001000) → l1=慢病(1000000)。
    匹配失败返回 None（调用方回退到命令行默认）。
    """
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
    """从 chunk positions 提取页码列表（1-based，每个 position 记一次页码）。

    positions 兼容两种格式：
      - [{"value": [page, x0, x1, top, bottom], "Count": n}, ...]
        （Count 是该位置的行数，与页码无关，不展开）
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


def safe_name(name: str, limit: int = 60) -> str:
    """文件名的安全形式（用于输出文件名）。"""
    cleaned = re.sub(r'[\\/:*?"<>|\r\n\t ]+', "_", name).strip("._")
    return cleaned[:limit] or "unnamed"


def try_json(text: str) -> Any:
    try:
        return json.loads(text)
    except Exception:
        return None


def try_pyobj(text: str) -> Any:
    """解析日志中的 dict 字面量：RAGFlow Trace 输出多为 Python 单引号 repr（非 JSON）。"""
    obj = try_json(text)
    if obj is not None:
        return obj
    try:
        import ast
        return ast.literal_eval(text)
    except Exception:
        return None


# ══════════════════════════════════════════════════════════════════
# 客户端
# ══════════════════════════════════════════════════════════════════


class MedlinkaiClient:
    """MedLinkAI 两阶段上传 + 进度监控。"""

    def __init__(self, base: str, dataset_id: str, page_size: int):
        self.base = base.rstrip("/")
        self.dataset_id = dataset_id
        self.page_size = page_size
        self.s = requests.Session()

    # ── Step A: 纯文件上传 ──
    def upload_file(self, pdf_path: Path) -> dict:
        """POST /api/v1/documents/upload_file；409 重复时返回 existing_doc_id。"""
        with open(pdf_path, "rb") as f:
            resp = self.s.post(
                f"{self.base}/api/v1/documents/upload_file",
                params={"dataset_id": self.dataset_id},
                data={"dataset_id": self.dataset_id},
                files={"file": (pdf_path.name, f, "application/pdf")},
                timeout=180,
            )
        if resp.status_code == 409:
            # 兼容两种响应体：{"detail": {...}} 或 {"error": {...}}
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

    # ── Step B: 提交处理（doc_id + 病案必填字段）──
    def upload(self, doc_id: str, case: dict[str, str]) -> dict:
        form = {
            "doc_id": doc_id,
            "dataset_id": self.dataset_id,
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
        resp = self.s.post(f"{self.base}/api/v1/documents/upload", data=form, timeout=120)
        resp.raise_for_status()
        return resp.json()

    # ── 删除（force-reupload 用）──
    def delete_document(self, doc_id: str) -> bool:
        resp = self.s.delete(
            f"{self.base}/api/v1/documents/{doc_id}",
            params={"dataset_id": self.dataset_id},
            timeout=120,
        )
        return resp.status_code in (200, 204)

    # ── 进度监控：轮询文档列表直到 progress >= 1 ──
    def wait_progress(self, doc_id: str, max_wait: int, interval: int) -> dict | None:
        deadline = time.time() + max_wait
        last = None
        while time.time() < deadline:
            try:
                resp = self.s.get(
                    f"{self.base}/api/v1/documents",
                    params={"page": 1, "page_size": self.page_size, "dataset_id": self.dataset_id},
                    timeout=30,
                )
                resp.raise_for_status()
                docs = resp.json().get("documents", [])
                for d in docs:
                    if d.get("doc_id") == doc_id:
                        last = d
                        run = d.get("run")
                        progress = d.get("progress") or 0
                        if run in (2, 3, 4) or float(progress) >= 1.0:
                            return d
            except requests.RequestException as e:
                print(f"  [warn] 监控请求失败: {e}")
            time.sleep(interval)
        return last


class RagflowClient:
    """RAGFlow chunks 查询。"""

    def __init__(self, base: str, api_key: str, dataset_id: str):
        self.base = base.rstrip("/")
        self.headers = {"Authorization": f"Bearer {api_key}"}
        self.dataset_id = dataset_id

    def list_chunks(self, doc_id: str) -> tuple[list[dict], dict]:
        """分页拉取文档全部 chunks；返回 (chunks, doc_info)。"""
        chunks: list[dict] = []
        doc_info: dict = {}
        page = 1
        while True:
            resp = requests.get(
                f"{self.base}/datasets/{self.dataset_id}/documents/{doc_id}/chunks",
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
# worker 日志分析
# ══════════════════════════════════════════════════════════════════

# 已知日志模式（RAGFlow pipeline / task_executor）
_SMART_RE = re.compile(r"SmartSplitter done:\s*(\d+)\s*chunks from\s*(\d+)\s*LLM segments.*?Types:\s*(\{.*\})")
_MERGE_RE = re.compile(r"ChunkMerger\] Merged\s*(\d+)\s*chunks from\s*(\d+)\s*sources:\s*(\{.*?\})(?:\s*\(filtered\s*(\d+)\s*noise chunks\))?")
_TRACE_MERGE_RE = re.compile(r"(?:ChunkMerger:Merger|Tokenizer:MedEmbed)\s*\|\s*outputs=(\{.*\})")
_PROGRESS_MSG_RE = re.compile(r"set_progress\([^)]*\), progress:\s*([0-9.]+), progress_msg:\s*(.*)")
_DONE_NO_CHUNKS_RE = re.compile(r"\[Done\] (.*)")
_SYNC_ERR_RE = re.compile(r"Invoke:SyncChunks finished\. error=(\S+)")
_SKIP_PATTERNS: list[tuple[str, re.Pattern]] = [
    ("no_items_extracted", re.compile(r"no items extracted", re.I)),
    ("json_parse_error", re.compile(r"JSON parse error", re.I)),
    ("multi_page_skip", re.compile(r"multi-page chunk.*skipping", re.I)),
    ("extracted_list_skip", re.compile(r"extracted_data is list, skip saves", re.I)),
    ("no_text_noise", re.compile(r"noise chunk", re.I)),
]


def fetch_worker_logs(container: str, tail: int, timeout: int = 180) -> list[str]:
    """docker logs 抓取（UTF-8 解码，避免 PowerShell 管道乱码）。"""
    cmd = ["docker", "logs", container, "--tail", str(tail)]
    r = subprocess.run(cmd, capture_output=True, timeout=timeout)
    raw = (r.stdout + b"\n" + r.stderr).decode("utf-8", errors="replace")
    return raw.splitlines()


def split_logs_by_doc(lines: list[str], doc_ids: list[str]) -> dict[str, list[str]]:
    """按 doc_id 在日志中的处理区间切分日志段。

    优先用 handle_task begin/done 行做边界：单 worker 顺序处理，begin→done
    即该文档的完整处理过程，可排除 heartbeat 等全局行与其他文档的串档；
    找不到 begin/done（如容器重启清空日志、复用旧文档）时回退：
    doc_id 首次出现行前 150 行起，到下一个 doc 首次出现行止。
    """
    segments: dict[str, list[str]] = {d: [] for d in doc_ids}
    _BEGIN_RE = re.compile(r"handle_task begin for task\s*(\{.*\})")
    _DONE_TASK_RE = re.compile(r"handle_task done for task\s*(\{.*\})")
    begins: dict[str, int] = {}
    dones: dict[str, int] = {}
    for i, line in enumerate(lines):
        mb = _BEGIN_RE.search(line)
        if mb:
            try:
                did = json.loads(mb.group(1)).get("doc_id")
                if did in segments:
                    begins[did] = i  # 取最后一次 begin（覆盖重试）
            except Exception:
                pass
        md = _DONE_TASK_RE.search(line)
        if md:
            try:
                did = json.loads(md.group(1)).get("doc_id")
                if did in segments:
                    dones[did] = i  # 取最后一次 done
            except Exception:
                pass
    for d in doc_ids:
        if d in begins and d in dones:
            segments[d] = lines[begins[d]:dones[d] + 1]
            continue
        # 回退：doc_id 子串匹配（旧逻辑）
        first = next((i for i, ln in enumerate(lines) if d in ln), None)
        if first is None:
            continue
        end = len(lines)
        for j in range(first + 1, len(lines)):
            if any(d2 != d and d2 in lines[j] for d2 in doc_ids):
                end = j
                break
        segments[d] = lines[max(0, first - 150):end]
    return segments


def analyze_doc_log(seg: list[str]) -> dict[str, Any]:
    """从文档日志段提取 SmartSplitter / ChunkMerger / Extractor / 错误证据。"""
    smart: dict[str, Any] = {"found": False}
    merge: dict[str, Any] = {"found": False}
    skips: list[dict[str, str]] = []
    errors: list[str] = []
    progress_msg: str | None = None
    done_msg: str | None = None
    sync_error: str | None = None
    for line in seg:
        m = _SMART_RE.search(line)
        if m:
            smart = {
                "found": True,
                "chunks": int(m.group(1)),
                "segments": int(m.group(2)),
                "types": try_pyobj(m.group(3)) or {},
            }
        m = _MERGE_RE.search(line)
        if m:
            noise = int(m.group(4)) if m.group(4) else 0
            merge = {
                "found": True,
                "merged": int(m.group(1)),
                "sources": int(m.group(2)),
                "stats": try_pyobj(m.group(3)) or {},
                "filtered_noise": noise,
            }
        for name, pat in _SKIP_PATTERNS:
            if pat.search(line):
                skips.append({"kind": name, "line": line.strip()[:400]})
        if "_ERROR" in line or re.search(r"^\d{4}-\d{2}-\d{2}.*\bERROR\b", line):
            errors.append(line.strip()[:400])
        m = _PROGRESS_MSG_RE.search(line)
        if m:
            progress_msg = m.group(2).strip()[:300]
        m = _DONE_NO_CHUNKS_RE.search(line)
        if m:
            done_msg = m.group(1).strip()[:300]
        m = _SYNC_ERR_RE.search(line)
        if m:
            sync_error = m.group(1)[:200]
    return {"smart_splitter": smart, "chunk_merger": merge, "skips": skips,
            "errors": errors,
            "progress_msg": progress_msg, "done_msg": done_msg, "sync_error": sync_error}


def extractor_stats_to_types(stats: dict) -> dict[str, int]:
    """把 ChunkMerger stats（键形如 "Extractor:Discharge"）映射为文档类型输出计数。

    "Extractor:Discharge" → DischargeRecord（子串匹配）；
    "Extractor:Clinical" 不匹配任何 6 类名，忽略。
    """
    out: dict[str, int] = {}
    for k, v in stats.items():
        short = str(k).replace("Extractor:", "", 1)
        if not isinstance(v, (int, float)):
            continue
        for dtype in DOC_TYPE_LABELS:
            if short == dtype or (short and short in dtype):
                out[dtype] = out.get(dtype, 0) + int(v)
                break
    return out


def check_type_filtering(types: dict[str, int], skips: list[dict[str, str]],
                         chunk_types: dict[str, int], sync_error: str | None = None,
                         extractor_output: dict[str, int] | None = None) -> dict[str, dict[str, Any]]:
    """6 类文档过滤判定。

    判定逻辑：
      - OK:      该类型最终有 chunk 落库（chunk_types > 0）
      - LOST:    SmartSplitter 已识别该类型（types > 0），但最终未落库
                 （多为后置环节失败，如 SyncChunks 同步失败）
      - FILTERED: 该类型无 chunk，但 Extractor 有输出（extractor_output > 0）且最终被滤
                 （典型：输出 chunk 无 text 被 ChunkMerger 当 noise 过滤，即核心字段缺失）
                 或日志中有 skip / 提取失败证据
      - UNKNOWN: 该类型无 chunk，且无直接证据（可能 PDF 中本无该类型文档）
    """
    extractor_output = extractor_output or {}
    result: dict[str, dict[str, Any]] = {}
    for dtype, label in DOC_TYPE_LABELS.items():
        n_chunks = chunk_types.get(dtype, 0) or 0
        n_recognized = types.get(dtype, 0) or 0
        n_extracted = extractor_output.get(dtype, 0) or 0
        evidence = [s for s in skips if dtype.lower() in s["line"].lower()]
        if n_chunks > 0:
            verdict = "OK"
        elif n_recognized > 0:
            verdict = "LOST"
        elif n_extracted > 0 or evidence:
            verdict = "FILTERED"
        else:
            verdict = "UNKNOWN"
        result[dtype] = {
            "label": label,
            "chunk_count": n_chunks,
            "recognized_count": n_recognized,
            "extractor_count": n_extracted,
            "core_fields": DOC_TYPE_CORE_FIELDS[dtype],
            "verdict": verdict,
            "evidence": [e["line"] for e in evidence],
        }
    if sync_error:
        for item in result.values():
            if item["verdict"] == "LOST":
                item["evidence"] = item["evidence"] + [f"SyncChunks 同步失败: {sync_error}"]
    return result


# ══════════════════════════════════════════════════════════════════
# 报告生成
# ══════════════════════════════════════════════════════════════════


def build_doc_report(pdf: dict, result: dict) -> dict:
    return {"pdf": pdf, "result": result}


def render_doc_md(pdf: dict, result: dict) -> str:
    r = result
    pages = r.get("pages", {})
    check = pages.get("check", {})
    lines: list[str] = []
    lines.append(f"# 基准结果：{pdf['name']}")
    lines.append("")
    lines.append("## 基本信息")
    lines.append("")
    lines.append(f"- 文件：`{pdf['name']}`")
    lines.append(f"- 大小：{pdf.get('size_kb')} KB")
    lines.append(f"- PDF 总页数：{pdf.get('pages')}")
    lines.append(f"- doc_id：`{r.get('doc_id')}`")
    lines.append(f"- 上传方式：{r.get('upload_mode')}")
    lines.append(f"- 状态：run={r.get('run_label')} (code={r.get('run')})  progress={r.get('progress')}")
    lines.append(f"- 开始时间：{r.get('begin_at')}  完成时间：{r.get('end_at')}  耗时：{r.get('elapsed_s')}s")
    if r.get("done_msg"):
        lines.append(f"- Pipeline 结束：`{r.get('done_msg')}`")
    if r.get("progress_msg"):
        lines.append(f"- progress_msg：`{r.get('progress_msg')}`")
    if r.get("sync_error"):
        lines.append(f"- **SyncChunks 同步失败：`{r.get('sync_error')}`**")
    lines.append("")
    lines.append("## 1. Chunk 页数核对")
    lines.append("")
    chunks = r.get("chunks", [])
    if not chunks:
        lines.append("**该文档没有任何 chunk（文档级被过滤或解析失败）**")
    else:
        lines.append(f"| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |")
        lines.append(f"|---|----------------|------|----------|----------|")
        for i, c in enumerate(chunks, 1):
            cpg = c["pages"]
            span = f"{min(cpg)}-{max(cpg)}" if cpg else "-"
            summary = (c.get("content") or "").replace("|", "/").replace("\n", " ")[:40]
            lines.append(f"| {i} | {c['chunk_id'][:8]} | {len(cpg)} | {span} | {summary} |")
        lines.append("")
        lines.append(f"- chunks 总数：{len(chunks)}")
        lines.append(f"- 各 chunk 页数合计（含跨页重复）：{pages.get('page_sum')}")
        lines.append(f"- 页码并集：`{sorted(pages.get('union', []))}`")
        lines.append(f"- 覆盖页数：{check.get('covered')} / {pdf.get('pages')}；缺失页：`{check.get('missing')}`")
        lines.append(f"- 超范围页（> PDF 总页数）：`{check.get('out_of_range')}`")
        lines.append(f"- **结论：{check.get('verdict')}**")
    lines.append("")
    lines.append("## 2. 六类文档过滤检查")
    lines.append("")
    lines.append("| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |")
    lines.append("|------|------|------|----------|------|--------------------------|------|")
    for dtype, item in r.get("type_check", {}).items():
        v = "-" if item['verdict'] in ("FILTERED", "UNKNOWN") else item['verdict']
        lines.append(f"| {dtype} | {item['label']} | {item.get('recognized_count', '-')} "
                     f"| {item.get('extractor_count', '-')} | {item['chunk_count']} "
                     f"| {', '.join(item['core_fields'])} | **{v}** |")
    lines.append("")
    lines.append(f"- SmartSplitter Types 统计：`{json.dumps(r.get('smart_types', {}), ensure_ascii=False)}`")
    lines.append(f"- ChunkMerger：`{json.dumps(r.get('merge_info', {}), ensure_ascii=False)}`")
    lines.append(f"- Extractor skip 证据：{len(r.get('skips', []))} 条")
    for s in r.get("skips", []):
        lines.append(f"  - `[{s['kind']}] {s['line'][:200]}`")
    lines.append(f"- worker 日志错误：{len(r.get('log_errors', []))} 条")
    for e in r.get("log_errors", [])[:10]:
        lines.append(f"  - `{e[:200]}`")
    lines.append("")
    lines.append("## 3. 完整日志（该文档在 worker 容器中的全部日志行）")
    lines.append("")
    lines.append("```text")
    seg = r.get("log_segment", [])
    if seg:
        for line in seg:
            lines.append(line)
    else:
        lines.append("（worker 日志中未找到该 doc_id 的记录，可能容器已重启或文档未重新解析）")
    lines.append("```")
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


def run() -> int:
    args = parse_args()
    pdf_dir = Path(args.pdf_dir)
    if not pdf_dir.is_dir():
        print(f"[error] PDF 目录不存在: {pdf_dir}")
        return 1

    # 输出目录
    if args.out_dir:
        out_root = Path(args.out_dir)
    else:
        out_root = Path(__file__).resolve().parent / "results"
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = out_root / stamp
    docs_dir = out / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)

    # 疾病三级分类：优先从文件夹名匹配字典推导，失败回退命令行默认
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

    print("=" * 72)
    print("病案 PDF 上传解析基准测试")
    print("=" * 72)
    print(f"MedLinkAI : {args.medlinkai_base}")
    print(f"RAGFlow   : {args.ragflow_base}")
    print(f"dataset   : {args.dataset_id}")
    print(f"PDF 目录   : {pdf_dir}")
    print(f"worker    : {args.container}")
    print(f"病案字段   : name_abbr/gender/age 每文档自动生成；疾病=文件夹「{pdf_dir.name}」推导 → "
          f"{illness_case['illness_label_l3']}({illness_case['illness_code_l3']})")
    print(f"输出目录   : {out}")
    print("=" * 72)

    pdfs = collect_pdfs(pdf_dir, args.only)
    if not pdfs:
        print("[error] 未找到 PDF 文件")
        return 1
    print(f"发现 {len(pdfs)} 个 PDF")

    mla = MedlinkaiClient(args.medlinkai_base, args.dataset_id, args.page_size)
    rf = RagflowClient(args.ragflow_base, args.ragflow_api_key, args.dataset_id)

    all_reports: list[dict] = []

    for idx, pdf in enumerate(pdfs, 1):
        # 病案字段：name_abbr 从文件名提取；gender/age 随机；疾病三级来自文件夹名推导
        case = {
            "name_abbr": args.name_abbr or extract_name_abbr(pdf["name"], idx),
            "gender": args.gender or random.choice(["man", "woman"]),
            "age": args.age or random.randint(18, 80),
            **illness_case,
        }
        print(f"\n[{idx}/{len(pdfs)}] {pdf['name']} （PDF 页数: {pdf['pages']}）"
              f" 病案: {case['name_abbr']}/{case['gender']}/{case['age']}岁")
        rep: dict[str, Any] = {
            "pdf": pdf,
            "doc_id": None,
            "upload_mode": "skip",
            "run": None,
            "run_label": None,
            "progress": None,
            "begin_at": datetime.now().isoformat(timespec="seconds"),
            "end_at": None,
            "elapsed_s": None,
            "chunks": [],
            "pages": {},
            "type_check": {},
            "smart_types": {},
            "merge_info": {},
            "skips": [],
            "log_errors": [],
            "log_segment": [],
            "note": "",
        }

        t0 = time.time()
        doc_id: str | None = None
        duplicate = False

        # ── 上传阶段 ──
        if not args.skip_upload:
            try:
                up = mla.upload_file(pdf["path"])
                if up.get("duplicate"):
                    duplicate = True
                    doc_id = up.get("doc_id")
                    rep["note"] += f"重复文件(409)：{up.get('message')} "
                    if args.force_reupload and doc_id:
                        print(f"  409 重复 doc_id={doc_id} → 删除后重传")
                        mla.delete_document(doc_id)
                        up = mla.upload_file(pdf["path"])
                        doc_id = up.get("doc_id")
                        duplicate = False
                        rep["note"] += "已删除重传。 "
                    else:
                        print(f"  409 重复：复用 doc_id={doc_id}（--force-reupload 可重新解析）")
                else:
                    doc_id = up.get("doc_id")
                    rep["upload_mode"] = "upload_file"
                    print(f"  upload_file OK → doc_id={doc_id}")
                if doc_id and not duplicate:
                    mla.upload(doc_id, case)
                    rep["upload_mode"] = "upload_file+upload"
                    print(f"  upload OK（已触发解析）")
            except Exception as e:
                rep["note"] += f"上传失败: {e} "
                print(f"  [error] 上传失败: {e}")
                # 上传失败也尝试用已有 doc_id 分析（从监控列表找同名文档）

        # ── 兜底：上传失败/跳过时，从监控列表按文件名找 doc_id ──
        if not doc_id:
            try:
                resp = requests.get(
                    f"{mla.base}/api/v1/documents",
                    params={"page": 1, "page_size": args.page_size, "dataset_id": args.dataset_id},
                    timeout=30,
                )
                for d in resp.json().get("documents", []):
                    if d.get("name") == pdf["name"] or (d.get("name") or "").endswith(pdf["name"]):
                        doc_id = d.get("doc_id")
                        rep["upload_mode"] = "existing"
                        rep["note"] += "复用监控列表中同名已有文档。 "
                        print(f"  复用同名已有文档 doc_id={doc_id}")
                        break
            except Exception as e:
                print(f"  [warn] 按文件名查找已有文档失败: {e}")

        # ── 进度监控 ──
        if doc_id:
            rep["doc_id"] = doc_id
            if not args.skip_upload:
                print(f"  监控进度（最多 {args.max_wait}s）…")
                status = mla.wait_progress(doc_id, args.max_wait, args.poll_interval)
                if status:
                    rep["run"] = status.get("run")
                    rep["run_label"] = RUN_MAP.get(status.get("run"), str(status.get("run")))
                    rep["progress"] = status.get("progress")
                    rep["chunk_count_api"] = status.get("chunk_count")
                    rep["process_begin_at"] = status.get("process_begin_at")
                    rep["process_duration"] = status.get("process_duration")
                    print(f"  run={rep['run_label']} progress={rep['progress']} "
                          f"chunk_count={rep.get('chunk_count_api')}")
                else:
                    rep["note"] += "进度监控超时（未达终态）。 "

        # ── chunk 页数统计（终态后 ES 近实时延迟，chunks 为空时重试）──
        if doc_id:
            try:
                chunks: list[dict] = []
                _doc_info: dict = {}
                for attempt in range(1, 7):
                    chunks, _doc_info = rf.list_chunks(doc_id)
                    if chunks or attempt == 6:
                        break
                    if attempt == 1:
                        print("  chunks 暂为 0（ES 近实时延迟），重试中…")
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
                        "row_position_int": c.get("row_position_int"),
                    })
                    union.update(pg_set)
                    page_sum += len(pg_set)
                total_pages = pdf.get("pages")
                missing = sorted(set(range(1, (total_pages or 0) + 1)) - union) if total_pages else []
                out_of_range = sorted(p for p in union if total_pages and p > total_pages)
                covered = len(union)
                verdict = ""
                if not chunks:
                    verdict = "❌ 无任何 chunk（文档级被过滤 / 解析失败）"
                elif total_pages is None:
                    verdict = "⚠️ PDF 页数未知，无法核对"
                elif covered == total_pages and not out_of_range:
                    verdict = "✅ 完全覆盖：chunk 页码并集 = PDF 总页数"
                else:
                    verdict = f"❌ 未完全覆盖：覆盖 {covered}/{total_pages} 页，缺失 {missing}，超范围 {out_of_range}"
                rep["pages"] = {
                    "union": sorted(union),
                    "page_sum": page_sum,
                    "check": {"covered": covered, "total": total_pages,
                              "missing": missing, "out_of_range": out_of_range,
                              "verdict": verdict},
                }
                print(f"  chunks={len(chunks)} 覆盖页数={covered}/{total_pages} 缺失={missing}")
            except Exception as e:
                rep["note"] += f"chunks 查询失败: {e} "
                print(f"  [error] chunks 查询失败: {e}")

        # ── worker 日志分析（处理完成后抓取，确保包含本次解析记录）──
        if doc_id:
            try:
                log_lines = fetch_worker_logs(args.container, args.log_tail)
            except Exception as e:
                print(f"  [warn] 日志抓取失败: {e}")
                log_lines = []
            seg = split_logs_by_doc(log_lines, [doc_id]).get(doc_id, [])
            rep["log_segment"] = seg
            if not seg:
                rep["note"] += "worker 日志中未找到该 doc_id（容器可能已重启或未重新解析）。 "
            log_an = analyze_doc_log(seg)
            rep["smart_types"] = log_an["smart_splitter"].get("types", {}) if log_an["smart_splitter"].get("found") else {}
            rep["merge_info"] = log_an["chunk_merger"] if log_an["chunk_merger"].get("found") else {}
            rep["skips"] = log_an["skips"]
            rep["log_errors"] = log_an["errors"]
            rep["progress_msg"] = log_an["progress_msg"]
            rep["done_msg"] = log_an["done_msg"]
            rep["sync_error"] = log_an["sync_error"]

            # chunk 类型分布（最终落库分布）：优先从 Trace outputs 的 chunks types 解析
            # （ChunkMerger/Tokenizer 输出的 "N items, types={...}" 即最终落库类型），
            # 拿不到时回退 ChunkMerger stats（键形如 "Extractor:Type"，需映射到 6 类）
            chunk_types: dict[str, int] = {}
            for line in seg:
                m = _TRACE_MERGE_RE.search(line)
                if not m:
                    continue
                payload = try_json(m.group(1))
                if not isinstance(payload, dict) or "chunks" not in payload:
                    continue
                ck = payload["chunks"]
                parsed: dict[str, int] = {}
                if isinstance(ck, dict):
                    parsed = {str(k): int(v) for k, v in ck.items()}
                elif isinstance(ck, str):
                    # Trace 输出格式: "N items, types={...}"（Python repr，非 JSON）
                    tm = re.search(r"types=\s*(\{.*\})", ck)
                    if tm:
                        types_obj = try_pyobj(tm.group(1))
                        if isinstance(types_obj, dict):
                            parsed = {str(k): int(v) for k, v in types_obj.items()}
                if parsed:
                    chunk_types = parsed  # 保留最后一次成功解析（最接近终态）
            if not chunk_types:
                stats = rep["merge_info"].get("stats") or {}
                for k, v in stats.items():
                    short = str(k).replace("Extractor:", "", 1)
                    if isinstance(v, (int, float)) and short in DOC_TYPE_LABELS:
                        chunk_types[short] = chunk_types.get(short, 0) + int(v)
            rep["chunk_types"] = chunk_types
            # Extractor 输出统计（从 ChunkMerger stats 映射到 6 类类型）
            rep["extractor_types"] = extractor_stats_to_types(rep["merge_info"].get("stats") or {})
            rep["type_check"] = check_type_filtering(rep["smart_types"], rep["skips"], chunk_types,
                                                      rep.get("sync_error"), rep["extractor_types"])
            print(f"  类型过滤: { {k: 'OK' if v['verdict']=='OK' else 'LOST' if v['verdict']=='LOST' else '-' for k, v in rep['type_check'].items()} }")

        rep["end_at"] = datetime.now().isoformat(timespec="seconds")
        rep["elapsed_s"] = round(time.time() - t0, 1)

        # ── 写基准结果文件（JSON 不含日志正文；每文档完整日志见 docs/*.md）──
        # 文件名只用 PDF 名（doc_id 在文件内容中已有，不参与命名）
        md = render_doc_md(pdf, rep)
        base = safe_name(pdf["name"])
        (docs_dir / f"{base}.md").write_text(md, encoding="utf-8")
        rep_json = {k: v for k, v in rep.items() if k != "log_segment"}
        (docs_dir / f"{base}.json").write_text(
            json.dumps(rep_json, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
        all_reports.append(rep)

    # ── 汇总 ──
    summary_md = ["# 基准测试汇总", "",
                  f"- 时间：{stamp}", f"- PDF 目录：{pdf_dir}", f"- dataset_id：{args.dataset_id}",
                  f"- MedLinkAI：{args.medlinkai_base}  RAGFlow：{args.ragflow_base}",
                  f"- 文档数：{len(all_reports)}", "",
                  "| 文件 | PDF页数 | doc_id | run | chunks | 覆盖页 | 缺失页 | 页数核对 | 门诊 | 入院 | 出院 | 购药 | 处方 | 检查报告 | 检验报告 |",
                  "|------|---------|--------|-----|--------|--------|--------|----------|------|------|------|------|------|----------|----------|"]
    for rep in all_reports:
        p = rep["pdf"]
        check = rep["pages"].get("check", {})
        tc = rep.get("type_check", {})
        v = lambda t: (lambda v: '-' if v in ('FILTERED','UNKNOWN') else v)(tc.get(t, {}).get("verdict", "-")) if tc else "-"
        summary_md.append(
            f"| {p['name']} | {p['pages']} | {rep['doc_id'] or '-'} | {rep['run_label'] or '-'} "
            f"| {len(rep['chunks'])} | {check.get('covered', '-')} | {check.get('missing', [])} "
            f"| {check.get('verdict', '-')[:20]} | {v('OutpatientRecord')} | {v('AdmissionRecord')} "
            f"| {v('DischargeRecord')} | {v('MedicationRecord')} | {v('PrescriptionRecord')} | {v('ExaminationReport')} | {v('LabReport')} |")
    summary_md += ["", "判定说明：OK=该类型有 chunk 落库；LOST=SmartSplitter 已识别但最终未落库（多为 SyncChunks 同步失败）", ""]
    (out / "summary.md").write_text("\n".join(summary_md), encoding="utf-8")
    # 汇总 JSON：基准结果，不含日志正文（每文档完整日志见 docs/*.md）
    summaries = [{k: v for k, v in rep.items() if k != "log_segment"} for rep in all_reports]
    (out / "summary.json").write_text(
        json.dumps(summaries, ensure_ascii=False, indent=2, default=str), encoding="utf-8")

    print("\n" + "=" * 72)
    print(f"完成：{len(all_reports)} 个文档，结果目录: {out}")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(run())
