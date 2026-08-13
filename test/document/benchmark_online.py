#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""线上测试环境（a800-116）病案上传解析批量统计脚本。

与 benchmark_upload.py 的区别：
- 目标环境默认 http://10.16.3.16:3160（内网测试环境），RAGFlow 走 39480 端口
- **不分析 worker 日志**（日志在服务器上），只统计：
  1. 覆盖率：chunks positions 页码并集 vs PDF 总页数
  2. 关键字段：逐 chunk 拉 extracted_data_tks（结构化提取结果），
     按特征字段归类到 7 类文档，统计各类核心字段是否提取到

重复文件处理（upload_file 返回 409）：
- 默认：略过上传，复用 existing_doc_id，调 /upload（doc_id 模式）更新病案字段并重新解析
- --reupload：先 DELETE 再重新上传（重新解析）
- --stats-only：不上传、不触发解析，只对已有文档做统计

用法:
    python benchmark_online.py                        # 默认：已上传则略过上传只重新解析
    python benchmark_online.py --reupload             # 409 重复时删除后重传
    python benchmark_online.py --stats-only           # 只统计，不触发任何解析
    python benchmark_online.py --only 哮喘            # 只处理文件名含"哮喘"的
    python benchmark_online.py --dataset-id <id>      # 手动指定 dataset（默认自动探测）
"""

from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any

import requests

# ══════════════════════════════════════════════════════════════════
# 常量：7 类文档核心字段 + 类型归属特征字段
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

# 类型归属特征字段：extracted_data 中出现这些字段即计分，得分最高的类型胜出。
# 核心字段本身也在其中；额外补充各类型特有的结构字段。
DOC_TYPE_HINT_FIELDS: dict[str, list[str]] = {
    "OutpatientRecord": ["chief_complaint", "diagnosis", "treatment_plan",
                         "encounter_date", "visit_type"],
    "AdmissionRecord": ["dm_admission_time", "cc_text", "pi_text", "dm_name",
                        "dm_gender", "department"],
    "DischargeRecord": ["discharge_date", "admission_date", "discharge_diagnosis",
                        "treatment_summary", "outcome"],
    "MedicationRecord": ["pharmacy", "payment_total", "medications",
                         "purchase_date", "invoice_no"],
    "PrescriptionRecord": ["prescriber", "prescription_type", "prescription_no",
                           "diagnosis"],
    "ExaminationReport": ["exam_name", "body_part", "exam_date", "report_date",
                          "department"],
    "LabReport": ["report_category", "report_name", "report_time", "lab_name",
                  "items"],
}

# 线上测试环境（a800-116）默认配置
DEFAULT_MLA_BASE = "http://10.16.3.16:3160"
DEFAULT_RAGFLOW_BASE = "http://10.16.3.16:39480/api/v1"
DEFAULT_RAGFLOW_KEY = "ragflow-ZihvOw9xL9fS9nKMWPrAHe3Qxeb9E2eo6VzXyIcIyq4"
DEFAULT_DATASET_ID = "fb850778372011f195bd2a5fbb884e34"  # MedLinkAI-v7.0

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
    p.add_argument("--max-wait", type=int, default=1800, help="单文档进度等待上限（秒）")
    p.add_argument("--poll-interval", type=int, default=5, help="进度轮询间隔（秒）")
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


def safe_name(name: str, limit: int = 60) -> str:
    """文件名的安全形式（用于输出文件名）。"""
    cleaned = re.sub(r'[\\/:*?"<>|\r\n\t ]+', "_", name).strip("._")
    return cleaned[:limit] or "unnamed"


def try_json(text: str) -> Any:
    try:
        return json.loads(text)
    except Exception:
        return None


def is_nonempty(v: Any) -> bool:
    """字段值是否非空（None/空串/空列表/空 dict 视为空）。"""
    if v is None:
        return False
    if isinstance(v, str):
        return bool(v.strip())
    if isinstance(v, (list, dict)):
        return len(v) > 0
    return True


def normalize_extracted(raw: Any) -> list[dict]:
    """extracted_data_tks 归一化为 dict 列表（可能是 JSON 字符串 / dict / list）。"""
    if isinstance(raw, str):
        raw = try_json(raw) if raw.strip() else None
    if raw is None:
        return []
    if isinstance(raw, dict):
        return [raw]
    if isinstance(raw, list):
        return [d for d in raw if isinstance(d, dict)]
    return []


def match_record_type(record: dict) -> tuple[str, int] | None:
    """按特征字段给提取记录归类：返回 (类型, 命中字段数)，无命中返回 None。"""
    best: tuple[str, int] | None = None
    for dtype, hints in DOC_TYPE_HINT_FIELDS.items():
        score = sum(1 for f in hints if is_nonempty(record.get(f)))
        if score > 0 and (best is None or score > best[1]):
            best = (dtype, score)
    return best


def analyze_key_fields(chunk_details: list[dict]) -> dict[str, dict[str, Any]]:
    """关键字段统计：逐 chunk 的 extracted_data_tks 归类到 7 类并核对核心字段。

    返回 {dtype: {records, matched_records, present_fields, missing_fields, verdict}}
    """
    type_records: dict[str, list[dict]] = {t: [] for t in DOC_TYPE_LABELS}
    unmatched = 0
    for detail in chunk_details:
        records = normalize_extracted(detail.get("extracted_data_tks"))
        for rec in records:
            hit = match_record_type(rec)
            if hit:
                type_records[hit[0]].append(rec)
            else:
                unmatched += 1
    result: dict[str, dict[str, Any]] = {}
    for dtype, core in DOC_TYPE_CORE_FIELDS.items():
        recs = type_records[dtype]
        present = [f for f in core if any(is_nonempty(r.get(f)) for r in recs)]
        missing = [f for f in core if f not in present]
        result[dtype] = {
            "label": DOC_TYPE_LABELS[dtype],
            "core_fields": core,
            "matched_records": len(recs),
            "present_fields": present,
            "missing_fields": missing,
            "verdict": "OK" if recs else "-",
        }
    result["_meta"] = {"unmatched_records": unmatched}
    return result


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

    # ── 按文件名查找已有文档（skip-upload / stats-only 兜底）──
    def find_existing(self, filename: str) -> str | None:
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
                        return d.get("doc_id")
                if len(docs) < self.page_size:
                    break
            except requests.RequestException:
                break
        return None


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

    def get_chunk_detail(self, dataset_id: str, doc_id: str, chunk_id: str) -> dict | None:
        """单 chunk 详情（含 extracted_data_tks 结构化提取字段）。"""
        try:
            resp = requests.get(
                f"{self.base}/datasets/{dataset_id}/documents/{doc_id}/chunks",
                params={"id": chunk_id},
                headers=self.headers,
                timeout=30,
            )
            resp.raise_for_status()
            items = resp.json().get("data", {}).get("chunks", [])
            return items[0] if items else None
        except Exception:
            return None


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
    lines.append(f"- PDF 总页数：{pdf.get('pages')}")
    lines.append(f"- doc_id：`{rep.get('doc_id')}`")
    lines.append(f"- 处理方式：{rep.get('mode')}")
    lines.append(f"- 状态：run={rep.get('run')}  progress={rep.get('progress')}")
    lines.append(f"- chunk_count(status)：{rep.get('chunk_count_api')}  "
                 f"orm_synced：{rep.get('orm_synced')}")
    lines.append(f"- 处理耗时(服务端)：{rep.get('process_duration')}s  "
                 f"脚本耗时：{rep.get('elapsed_s')}s")
    if rep.get("note"):
        lines.append(f"- 备注：{rep.get('note')}")
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
    lines.append("## 2. 关键字段提取统计（基于 chunks extracted_data_tks）")
    lines.append("")
    kf = rep.get("key_fields", {})
    lines.append("| 类型 | 中文 | 提取记录数 | 核心字段命中 | 缺失字段 | 判定 |")
    lines.append("|------|------|-----------|--------------|----------|------|")
    for dtype, item in kf.items():
        if dtype == "_meta":
            continue
        lines.append(f"| {dtype} | {item['label']} | {item['matched_records']} "
                     f"| {', '.join(item['present_fields']) or '-'} "
                     f"| {', '.join(item['missing_fields']) or '-'} | **{item['verdict']}** |")
    meta = kf.get("_meta", {})
    if meta.get("unmatched_records"):
        lines.append("")
        lines.append(f"- 未归类提取记录：{meta['unmatched_records']} 条")
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
    out_root = Path(args.out_dir) if args.out_dir else Path(__file__).resolve().parent / "results_online"
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

    # dataset_id：手动指定 > 自动探测
    rf_probe = RagflowClient(args.ragflow_base, args.ragflow_api_key)
    dataset_id = rf_probe.resolve_dataset(args.dataset_id, args.dataset_name)

    mode_desc = ("只统计，不触发解析" if args.stats_only
                 else "重复时删除重传" if args.reupload
                 else "重复时略过上传，只重新解析（默认）")

    print("=" * 72)
    print("线上测试环境病案上传解析批量统计")
    print("=" * 72)
    print(f"MedLinkAI : {args.medlinkai_base}")
    print(f"RAGFlow   : {args.ragflow_base}")
    print(f"dataset   : {dataset_id}")
    print(f"PDF 目录   : {pdf_dir}")
    print(f"重复处理   : {mode_desc}")
    print(f"病案字段   : name_abbr/gender/age 每文档自动生成；疾病=文件夹「{pdf_dir.name}」推导 → "
          f"{illness_case['illness_label_l3']}({illness_case['illness_code_l3']})")
    print(f"输出目录   : {out}")
    print("=" * 72)

    pdfs = collect_pdfs(pdf_dir, args.only)
    if not pdfs:
        print("[error] 未找到 PDF 文件")
        return 1
    print(f"发现 {len(pdfs)} 个 PDF")

    mla = MedlinkaiClient(args.medlinkai_base, dataset_id, args.page_size,
                          api_key=args.api_key, basic_auth=args.basic_auth)
    rf = RagflowClient(args.ragflow_base, args.ragflow_api_key)

    all_reports: list[dict] = []

    for idx, pdf in enumerate(pdfs, 1):
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
            "mode": "-",
            "run": None,
            "progress": None,
            "chunk_count_api": None,
            "orm_synced": None,
            "process_duration": None,
            "begin_at": datetime.now().isoformat(timespec="seconds"),
            "end_at": None,
            "elapsed_s": None,
            "chunks": [],
            "pages": {},
            "key_fields": {},
            "note": "",
        }

        t0 = time.time()
        doc_id: str | None = None
        triggered = False  # 本次是否触发了（重新）解析

        # ── 上传 / 复用阶段 ──
        if args.stats_only:
            doc_id = mla.find_existing(pdf["name"])
            rep["mode"] = "stats-only"
            if doc_id:
                print(f"  stats-only：找到已有文档 doc_id={doc_id}")
            else:
                rep["note"] += "stats-only 模式下未找到同名已有文档。 "
                print("  [warn] 未找到同名已有文档，跳过")
        elif args.reupload:
            try:
                up = mla.upload_file(pdf["path"])
                if up.get("duplicate") and up.get("doc_id"):
                    print(f"  409 重复 doc_id={up['doc_id']} → 删除后重传")
                    mla.delete_document(up["doc_id"])
                    time.sleep(2)
                    up = mla.upload_file(pdf["path"])
                doc_id = up.get("doc_id")
                if doc_id:
                    mla.upload(doc_id, case)
                    triggered = True
                    rep["mode"] = "reupload+upload" if up.get("duplicate") else "upload_file+upload"
                    print(f"  上传并触发解析 OK → doc_id={doc_id}")
            except Exception as e:
                rep["note"] += f"上传失败: {e} "
                print(f"  [error] 上传失败: {e}")
        else:
            # 默认：先查已有文档（略过上传），没有再上传
            doc_id = mla.find_existing(pdf["name"])
            if doc_id:
                rep["mode"] = "existing+reparse"
                print(f"  已上传，略过上传 → doc_id={doc_id}，触发重新解析")
                try:
                    mla.upload(doc_id, case)  # doc_id 模式：更新病案字段 + 触发解析
                    triggered = True
                except Exception as e:
                    rep["note"] += f"触发重新解析失败: {e} "
                    print(f"  [error] 触发重新解析失败: {e}")
            else:
                try:
                    up = mla.upload_file(pdf["path"])
                    if up.get("duplicate"):
                        # 列表里没匹配到（可能名字被改过），复用 409 返回的 doc_id
                        doc_id = up.get("doc_id")
                        rep["mode"] = "duplicate+reparse"
                        rep["note"] += f"409 重复：{up.get('message')} "
                        print(f"  409 重复：复用 doc_id={doc_id}，触发重新解析")
                    else:
                        doc_id = up.get("doc_id")
                        rep["mode"] = "upload_file+upload"
                        print(f"  upload_file OK → doc_id={doc_id}")
                    if doc_id:
                        mla.upload(doc_id, case)
                        triggered = True
                        if rep["mode"] != "duplicate+reparse":
                            print("  upload OK（已触发解析）")
                except Exception as e:
                    rep["note"] += f"上传失败: {e} "
                    print(f"  [error] 上传失败: {e}")

        if not doc_id:
            rep["end_at"] = datetime.now().isoformat(timespec="seconds")
            rep["elapsed_s"] = round(time.time() - t0, 1)
            all_reports.append(rep)
            continue
        rep["doc_id"] = doc_id

        # ── 进度监控（status 接口）──
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
                if status.get("progress_msg"):
                    rep["progress_msg"] = str(status.get("progress_msg"))[:300]
                print(f"  run={rep['run']} progress={rep['progress']} "
                      f"chunk_count={rep.get('chunk_count_api')} orm_synced={rep.get('orm_synced')}")
        except Exception as e:
            rep["note"] += f"状态查询失败: {e} "
            print(f"  [error] 状态查询失败: {e}")

        # ── 覆盖率统计（chunks positions；终态后 ES 近实时延迟，为空时重试）──
        chunks: list[dict] = []
        try:
            for attempt in range(1, 7):
                chunks, _doc_info = rf.list_chunks(dataset_id, doc_id)
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
                })
                union.update(pg_set)
                page_sum += len(pg_set)
            total_pages = pdf.get("pages")
            missing = sorted(set(range(1, (total_pages or 0) + 1)) - union) if total_pages else []
            out_of_range = sorted(p for p in union if total_pages and p > total_pages)
            covered = len(union)
            coverage_pct = round(covered * 100.0 / total_pages, 1) if total_pages else None
            if not chunks:
                verdict = "❌ 无任何 chunk（文档级被过滤 / 解析失败）"
            elif total_pages is None:
                verdict = "⚠️ PDF 页数未知，无法核对"
            elif covered == total_pages and not out_of_range:
                verdict = "✅ 完全覆盖：chunk 页码并集 = PDF 总页数"
            else:
                verdict = (f"❌ 未完全覆盖：覆盖 {covered}/{total_pages} 页，"
                           f"缺失 {missing}，超范围 {out_of_range}")
            rep["pages"] = {
                "union": sorted(union),
                "page_sum": page_sum,
                "check": {"covered": covered, "total": total_pages,
                          "coverage_pct": coverage_pct,
                          "missing": missing, "out_of_range": out_of_range,
                          "verdict": verdict},
            }
            print(f"  chunks={len(chunks)} 覆盖页数={covered}/{total_pages}"
                  f"（{coverage_pct}%） 缺失={missing}")
        except Exception as e:
            rep["note"] += f"chunks 查询失败: {e} "
            print(f"  [error] chunks 查询失败: {e}")

        # ── 关键字段统计（逐 chunk 拉 extracted_data_tks）──
        try:
            details: list[dict] = []
            for c in rep["chunks"]:
                cid = c.get("chunk_id")
                if not cid:
                    continue
                d = rf.get_chunk_detail(dataset_id, doc_id, cid)
                if d:
                    details.append(d)
            rep["key_fields"] = analyze_key_fields(details)
            hit_types = [f"{t}({v['matched_records']})"
                         for t, v in rep["key_fields"].items()
                         if t != "_meta" and v["matched_records"] > 0]
            print(f"  关键字段: 提取到类型 {', '.join(hit_types) or '无'}")
        except Exception as e:
            rep["note"] += f"关键字段统计失败: {e} "
            print(f"  [error] 关键字段统计失败: {e}")

        rep["end_at"] = datetime.now().isoformat(timespec="seconds")
        rep["elapsed_s"] = round(time.time() - t0, 1)

        # ── 写结果文件 ──
        base = safe_name(pdf["name"])
        (docs_dir / f"{base}.md").write_text(render_doc_md(pdf, rep), encoding="utf-8")
        (docs_dir / f"{base}.json").write_text(
            json.dumps(rep, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
        all_reports.append(rep)

    # ── 汇总 ──
    type_cols = list(DOC_TYPE_LABELS.values())
    summary_md = ["# 线上批量统计汇总", "",
                  f"- 时间：{stamp}", f"- PDF 目录：{pdf_dir}", f"- dataset_id：{dataset_id}",
                  f"- MedLinkAI：{args.medlinkai_base}  RAGFlow：{args.ragflow_base}",
                  f"- 重复处理：{mode_desc}", f"- 文档数：{len(all_reports)}", "",
                  "| 文件 | PDF页数 | doc_id | run | chunks | 覆盖页 | 覆盖率% | 缺失页 "
                  + "".join(f"| {lb}" for lb in type_cols) + " |",
                  "|------|---------|--------|-----|--------|--------|---------|--------"
                  + "|----" * len(type_cols) + "|"]
    for rep in all_reports:
        p = rep["pdf"]
        check = rep["pages"].get("check", {})
        kf = rep.get("key_fields", {})

        def cell(dtype: str) -> str:
            item = kf.get(dtype)
            if not item or item["matched_records"] == 0:
                return "-"
            miss = len(item["missing_fields"])
            return "OK" if miss == 0 else f"缺{miss}"

        summary_md.append(
            f"| {p['name']} | {p['pages']} | {rep['doc_id'] or '-'} | {rep['run'] or '-'} "
            f"| {len(rep['chunks'])} | {check.get('covered', '-')} "
            f"| {check.get('coverage_pct', '-')} | {check.get('missing', [])} "
            + "".join(f"| {cell(t)}" for t in DOC_TYPE_LABELS) + " |")

    n_total = len(all_reports)
    n_done = sum(1 for r in all_reports if r.get("run") == "DONE")
    n_full = sum(1 for r in all_reports
                 if r["pages"].get("check", {}).get("verdict", "").startswith("✅"))
    summary_md += [
        "",
        f"- run=DONE：{n_done}/{n_total}；页面完全覆盖：{n_full}/{n_total}",
        "",
        "判定说明：OK=该类型提取记录齐全（核心字段全部非空）；缺N=命中该类型但缺 N 个核心字段；"
        "-=未提取到该类型记录",
        "",
    ]
    (out / "summary.md").write_text("\n".join(summary_md), encoding="utf-8")
    (out / "summary.json").write_text(
        json.dumps(all_reports, ensure_ascii=False, indent=2, default=str), encoding="utf-8")

    print("\n" + "=" * 72)
    print(f"完成：{len(all_reports)} 个文档，结果目录: {out}")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(run())
