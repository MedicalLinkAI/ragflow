#!/usr/bin/env python3
"""
Pipeline 端到端回归验证脚本

功能：
  Phase 1: 静态检查（调用 pipeline_check_dsl.py）
  Phase 2: 快速验证 — 触发 xypp 小文档解析，验证 DB 状态 + 日志
  Phase 3: 完整验证 — 触发 ZLHU 大文档解析（--full 时）
  Phase 4: 全量验证 — 触发所有文档解析（--all 时）

用法：
  cd ragflow/
  python scripts/pipeline_regression.py                          # Phase 1 + 2
  python scripts/pipeline_regression.py --full                   # Phase 1 + 2 + 3
  python scripts/pipeline_regression.py --all                    # Phase 1 + 2 + 3 + 4
  python scripts/pipeline_regression.py --static-only            # Phase 1 only
  python scripts/pipeline_regression.py --log-file /tmp/xxx.log  # 指定日志文件

环境变量：
  RAGFLOW_API_KEY      (required)
  RAGFLOW_BASE_URL     (default: http://localhost)
  RAGFLOW_DATASET_ID   (default: 926402fa1c9311f18d9b2a5fbb884ed3)
  RAGFLOW_CANVAS_ID    (default: 192c7f7898814e99a34a856ce567a57c)
  RAGFLOW_LOG_FILE     (default: /tmp/task_executor_restart4.log)
  DB_USER / DB_PASSWORD / DB_HOST / DB_PORT / DB_NAME
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from collections import Counter
from datetime import datetime

import requests


# ─── Configuration ─────────────────────────────────────────────────────

API_KEY = os.environ.get("RAGFLOW_API_KEY", "ragflow-ZihvOw9xL9fS9nKMWPrAHe3Qxeb9E2eo6VzXyIcIyq4")
BASE_URL = os.environ.get("RAGFLOW_BASE_URL", "http://localhost")
DATASET_ID = os.environ.get("RAGFLOW_DATASET_ID", "926402fa1c9311f18d9b2a5fbb884ed3")
CANVAS_ID = os.environ.get("RAGFLOW_CANVAS_ID", "192c7f7898814e99a34a856ce567a57c")
LOG_FILE = os.environ.get("RAGFLOW_LOG_FILE", "/tmp/task_executor_restart4.log")

# 基准文档定义
BASELINE_DOCS = {
    "quick": {
        "id": "3d8175e21dc411f1b8302a5fbb884ed3",
        "name": "xypp-吉大一 .pdf",
        "expected_chunks_min": 3,
        "expected_chunks_max": 5,
        "description": "小文档快速验证（3 页）"
    },
    "full": {
        "id": "add49a001e8111f19b272a5fbb884ed3",
        "name": "ZLHU-女-类风湿-安徽省立中心.pdf",
        "expected_chunks_min": 12,
        "expected_chunks_max": 25,
        "description": "大文档完整验证（500+ blocks，SmartSplitter LLM 有非确定性，范围放宽）"
    },
}

# Pipeline 预期步数
EXPECTED_PATH_LENGTH = 11

# 预期组件列表（按执行顺序）
EXPECTED_COMPONENTS = [
    "Parser:MedLink",
    "SmartSplitter:MedLink",
    "ChunkRouter:Router",
    "Extractor:LabExam",
    "Extractor:Imaging",
    "Extractor:Clinical",
    "Extractor:Default",
    "ChunkMerger:Merger",
    "Tokenizer:MedEmbed",
    "Invoke:SyncChunks",
]


# ─── Helpers ───────────────────────────────────────────────────────────

class RegressionResult:
    def __init__(self):
        self.phases = {}
        self.current_phase = None

    def start_phase(self, name):
        self.current_phase = name
        self.phases[name] = {"passed": [], "failed": [], "warnings": []}
        print(f"\n{'─' * 60}")
        print(f"[{name}]")
        print(f"{'─' * 60}")

    def ok(self, msg):
        self.phases[self.current_phase]["passed"].append(msg)
        print(f"  ✅ {msg}")

    def fail(self, msg):
        self.phases[self.current_phase]["failed"].append(msg)
        print(f"  ❌ {msg}")

    def warn(self, msg):
        self.phases[self.current_phase]["warnings"].append(msg)
        print(f"  ⚠️  {msg}")

    def info(self, msg):
        print(f"  ℹ️  {msg}")

    @property
    def success(self):
        return all(
            len(p["failed"]) == 0
            for p in self.phases.values()
        )

    def report(self):
        print(f"\n{'═' * 60}")
        print("Pipeline Regression Report")
        print(f"{'═' * 60}")

        total_passed = 0
        total_failed = 0
        total_warnings = 0

        for phase_name, phase in self.phases.items():
            status = "✅" if not phase["failed"] else "❌"
            p = len(phase["passed"])
            f = len(phase["failed"])
            w = len(phase["warnings"])
            print(f"  {status} {phase_name}: {p} passed, {f} failed, {w} warnings")
            total_passed += p
            total_failed += f
            total_warnings += w

        print(f"{'─' * 60}")
        if self.success:
            print(f"  RESULT: ALL {total_passed} CHECKS PASSED ✅")
        else:
            print(f"  RESULT: {total_failed} CHECKS FAILED ❌ ({total_passed} passed)")
        if total_warnings:
            print(f"  WARNINGS: {total_warnings}")
        print(f"{'═' * 60}\n")
        return self.success


def api_headers():
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }


def get_document(doc_id):
    """Get document status from RAGflow API."""
    resp = requests.get(
        f"{BASE_URL}/api/v1/datasets/{DATASET_ID}/documents",
        headers=api_headers(),
        params={"id": doc_id},
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    if data.get("code") != 0:
        raise RuntimeError(f"API error: {data}")
    docs = data["data"]["docs"]
    if not docs:
        raise RuntimeError(f"Document {doc_id} not found")
    return docs[0]


def trigger_parse(doc_id):
    """Trigger document parsing via RAGflow API."""
    resp = requests.post(
        f"{BASE_URL}/api/v1/datasets/{DATASET_ID}/chunks",
        headers=api_headers(),
        json={"document_ids": [doc_id]},
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    if data.get("code") != 0:
        raise RuntimeError(f"API error triggering parse: {data}")


def wait_for_completion(doc_id, timeout_seconds=300, poll_interval=5):
    """Wait for document to finish parsing."""
    start = time.time()
    while time.time() - start < timeout_seconds:
        doc = get_document(doc_id)
        run_status = doc.get("run", "")
        if run_status == "DONE":
            return doc
        if run_status == "FAIL" or run_status == "CANCEL":
            return doc
        time.sleep(poll_interval)
    raise TimeoutError(f"Document {doc_id} did not complete within {timeout_seconds}s")


def get_log_tail(log_file, since_time=None, max_lines=500):
    """Read log file tail, optionally filtering by time."""
    if not os.path.exists(log_file):
        return []

    lines = []
    with open(log_file, "r") as f:
        # Read last max_lines * 10 bytes to be safe
        f.seek(0, 2)
        fsize = f.tell()
        read_size = min(fsize, max_lines * 500)
        f.seek(max(0, fsize - read_size))
        all_lines = f.readlines()

    if since_time:
        for line in all_lines:
            # Parse log timestamp: 2026-03-13 17:28:55,602
            m = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", line)
            if m:
                try:
                    log_time = datetime.strptime(m.group(1), "%Y-%m-%d %H:%M:%S")
                    if log_time >= since_time:
                        lines.append(line)
                except ValueError:
                    pass
    else:
        lines = all_lines[-max_lines:]

    return lines


def check_pipeline_logs(log_lines, result):
    """Check pipeline execution logs for a single document run."""
    # Extract component execution lines
    executing = []
    finished = []

    for line in log_lines:
        m = re.search(r"\[Pipeline\] Executing component \[(\d+)\]: (\S+) \(type=(\S+)\)", line)
        if m:
            executing.append({"idx": int(m.group(1)), "id": m.group(2), "type": m.group(3)})

        m = re.search(r"\[Pipeline\] Component \[(\d+)\]: (\S+) finished\. error=(.*)", line)
        if m:
            finished.append({"idx": int(m.group(1)), "id": m.group(2), "error": m.group(3)})

    if not executing:
        result.warn("No pipeline execution logs found in the time window")
        return

    # Check 1: Component execution count
    exec_ids = [e["id"] for e in executing]
    exec_counter = Counter(exec_ids)
    duplicates = {k: v for k, v in exec_counter.items() if v > 1}

    if not duplicates:
        result.ok(f"Components: {len(executing)} unique executions, 0 duplicates")
    else:
        result.fail(f"Components executed MULTIPLE times: {duplicates}")

    # Check 2: All expected components executed
    executed_set = set(exec_ids)
    missing = [c for c in EXPECTED_COMPONENTS if c not in executed_set]
    if not missing:
        result.ok(f"All {len(EXPECTED_COMPONENTS)} expected components executed")
    else:
        result.fail(f"Missing components: {missing}")

    # Check 3: All errors are None
    errors = [f for f in finished if f["error"] != "None"]
    if not errors:
        result.ok(f"Errors: 0 (all {len(finished)} components returned None)")
    else:
        for e in errors:
            result.fail(f"Component [{e['idx']}] {e['id']}: error={e['error']}")

    # Check 4: Invoke:SyncChunks specifically
    invoke_results = [f for f in finished if "Invoke" in f["id"]]
    if invoke_results:
        for inv in invoke_results:
            if inv["error"] == "None":
                result.ok(f"{inv['id']}: success")
            else:
                result.fail(f"{inv['id']}: error={inv['error']}")
    else:
        result.warn("Invoke:SyncChunks not found in finished logs")


# ─── Phase Functions ───────────────────────────────────────────────────

def phase1_static_check(result, canvas_id):
    """Phase 1: Static DSL consistency check."""
    result.start_phase("Phase 1: Static Check")

    script_dir = os.path.dirname(os.path.abspath(__file__))
    dsl_check = os.path.join(script_dir, "pipeline_check_dsl.py")

    if not os.path.exists(dsl_check):
        result.fail(f"pipeline_check_dsl.py not found at {dsl_check}")
        return

    try:
        proc = subprocess.run(
            [sys.executable, dsl_check, "--canvas-id", canvas_id],
            capture_output=True, text=True, timeout=30,
        )
        if proc.returncode == 0:
            result.ok("DSL static check: ALL PASSED")
        else:
            # Extract failed items from output
            for line in proc.stdout.splitlines():
                if "❌" in line:
                    result.fail(line.strip())
            if not any("❌" in line for line in proc.stdout.splitlines()):
                result.fail(f"DSL check failed with return code {proc.returncode}")
        # Print the full output for reference
        if proc.stdout:
            for line in proc.stdout.splitlines():
                if line.strip() and "═" not in line and "─" not in line:
                    result.info(line.strip())
    except subprocess.TimeoutExpired:
        result.fail("DSL static check timed out after 30s")
    except Exception as e:
        result.fail(f"DSL static check error: {e}")


def phase_dynamic_check(result, phase_name, doc_key, log_file):
    """Phase 2/3: Dynamic validation — trigger parse and verify."""
    doc_config = BASELINE_DOCS[doc_key]
    doc_id = doc_config["id"]
    doc_name = doc_config["name"]
    min_chunks = doc_config["expected_chunks_min"]
    max_chunks = doc_config["expected_chunks_max"]

    result.start_phase(f"{phase_name} ({doc_name})")

    # Record time before triggering (for log filtering)
    before_time = datetime.now()

    # Step 1: Trigger parse
    try:
        result.info(f"Triggering parse for: {doc_name} (id={doc_id})")
        trigger_parse(doc_id)
        result.ok("Parse triggered successfully")
    except Exception as e:
        result.fail(f"Failed to trigger parse: {e}")
        return

    # Step 2: Wait for completion
    try:
        timeout = 120 if doc_key == "quick" else 300
        result.info(f"Waiting for completion (timeout={timeout}s)...")
        doc = wait_for_completion(doc_id, timeout_seconds=timeout)
    except TimeoutError as e:
        result.fail(str(e))
        return
    except Exception as e:
        result.fail(f"Error waiting for completion: {e}")
        return

    # Step 3: Check DB status
    run_status = doc.get("run", "?")
    if run_status == "DONE":
        result.ok(f"Status: DONE")
    else:
        result.fail(f"Status: {run_status} (expected DONE)")
        return

    # Step 4: Check chunk count
    chunk_count = doc.get("chunk_count", 0)
    if min_chunks <= chunk_count <= max_chunks:
        result.ok(f"Chunks: {chunk_count} (expected: {min_chunks}-{max_chunks})")
    else:
        result.fail(f"Chunks: {chunk_count} (expected: {min_chunks}-{max_chunks})")

    # Step 5: Check pipeline logs
    result.info("Checking pipeline execution logs...")
    # Give a small buffer (2s before trigger time)
    from datetime import timedelta
    log_since = before_time - timedelta(seconds=2)
    log_lines = get_log_tail(log_file, since_time=log_since)

    # Filter to only the lines for this specific document run
    # Look for lines between "handle_task begin" for this doc and the next one
    relevant_lines = []
    in_section = False
    for line in log_lines:
        if doc_name in line and "handle_task begin" in line:
            in_section = True
        if in_section:
            relevant_lines.append(line)
            if "[Pipeline] Component" in line and "Invoke" in line and "finished" in line:
                # Found the last component — keep a few more lines then stop
                continue

    if not relevant_lines:
        # Fallback: use all recent pipeline lines
        relevant_lines = [l for l in log_lines if "[Pipeline]" in l]

    check_pipeline_logs(relevant_lines, result)


def phase4_all_docs(result, log_file):
    """Phase 4: Full validation — all documents in KB."""
    result.start_phase("Phase 4: All Documents")

    try:
        resp = requests.get(
            f"{BASE_URL}/api/v1/datasets/{DATASET_ID}/documents",
            headers=api_headers(),
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        docs = data["data"]["docs"]
    except Exception as e:
        result.fail(f"Failed to list documents: {e}")
        return

    doc_ids = [d["id"] for d in docs]
    result.info(f"Found {len(doc_ids)} documents, triggering parse for all...")

    # Trigger all at once
    try:
        trigger_resp = requests.post(
            f"{BASE_URL}/api/v1/datasets/{DATASET_ID}/chunks",
            headers=api_headers(),
            json={"document_ids": doc_ids},
            timeout=30,
        )
        trigger_resp.raise_for_status()
        trigger_data = trigger_resp.json()
        if trigger_data.get("code") != 0:
            result.fail(f"API error: {trigger_data}")
            return
        result.ok(f"Triggered parse for {len(doc_ids)} documents")
    except Exception as e:
        result.fail(f"Failed to trigger parse: {e}")
        return

    # Wait for all to complete
    result.info("Waiting for all documents to complete (timeout=600s)...")
    start = time.time()
    timeout = 600

    while time.time() - start < timeout:
        try:
            resp = requests.get(
                f"{BASE_URL}/api/v1/datasets/{DATASET_ID}/documents",
                headers=api_headers(),
                params={"limit": 100},
                timeout=30,
            )
            docs = resp.json()["data"]["docs"]
        except Exception:
            time.sleep(10)
            continue

        running = [d for d in docs if d.get("run") == "RUNNING"]
        done = [d for d in docs if d.get("run") == "DONE"]
        failed = [d for d in docs if d.get("run") == "FAIL"]

        if not running:
            break
        time.sleep(10)

    # Final check
    try:
        resp = requests.get(
            f"{BASE_URL}/api/v1/datasets/{DATASET_ID}/documents",
            headers=api_headers(),
            params={"limit": 100},
            timeout=30,
        )
        docs = resp.json()["data"]["docs"]
    except Exception as e:
        result.fail(f"Failed to get final status: {e}")
        return

    done_count = sum(1 for d in docs if d.get("run") == "DONE")
    fail_count = sum(1 for d in docs if d.get("run") == "FAIL")

    if fail_count == 0:
        result.ok(f"All {done_count} documents: DONE, 0 failures")
    else:
        result.fail(f"{fail_count} documents FAILED:")
        for d in docs:
            if d.get("run") == "FAIL":
                result.fail(f"  {d['name']}: FAIL (chunks={d.get('chunk_count', 0)})")

    # Check each document has chunks
    zero_chunks = [d for d in docs if d.get("run") == "DONE" and d.get("chunk_count", 0) == 0]
    if zero_chunks:
        for d in zero_chunks:
            result.warn(f"  {d['name']}: DONE but 0 chunks")
    else:
        result.ok(f"All DONE documents have chunks > 0")


# ─── Main ──────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Pipeline End-to-End Regression Test")
    parser.add_argument("--static-only", action="store_true", help="Phase 1 only (no parsing)")
    parser.add_argument("--full", action="store_true", help="Include Phase 3 (ZLHU large doc)")
    parser.add_argument("--all", action="store_true", help="Include Phase 4 (all documents)")
    parser.add_argument("--log-file", default=LOG_FILE, help="Task executor log file path")
    parser.add_argument("--canvas-id", default=CANVAS_ID, help="Canvas ID for DSL check")
    args = parser.parse_args()

    print(f"{'═' * 60}")
    print(f"Pipeline Regression Test — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'═' * 60}")
    print(f"  Dataset:   {DATASET_ID}")
    print(f"  Canvas:    {args.canvas_id}")
    print(f"  Log file:  {args.log_file}")
    print(f"  API:       {BASE_URL}")

    result = RegressionResult()

    # Phase 1: Static
    phase1_static_check(result, args.canvas_id)

    if args.static_only:
        success = result.report()
        sys.exit(0 if success else 1)

    # Phase 2: Quick validation
    phase_dynamic_check(result, "Phase 2: Quick Validation", "quick", args.log_file)

    # Phase 3: Full validation (optional)
    if args.full or args.all:
        phase_dynamic_check(result, "Phase 3: Full Validation", "full", args.log_file)

    # Phase 4: All documents (optional)
    if args.all:
        phase4_all_docs(result, args.log_file)

    # Report
    success = result.report()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
