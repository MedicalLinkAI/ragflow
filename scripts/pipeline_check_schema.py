#!/usr/bin/env python3
"""
Pipeline Schema 兼容性检查脚本

功能：
  验证 Pipeline 中每对 push 模式 (上游→下游) 的输出字段是否兼容下游的 FromUpstream schema。
  重点检查使用 extra="forbid" 的节点（SmartSplitter / Extractor / Tokenizer），
  上游任何未定义的输出字段都会导致运行时 ValidationError。

用法：
  cd ragflow/
  python scripts/pipeline_check_schema.py --canvas-id 192c7f7898814e99a34a856ce567a57c

设计说明：
  - 读取 DSL 中每个组件的 component_name
  - 根据 component_name 查找对应的 FromUpstream schema 类
  - 读取上游组件的 set_output 字段列表（从源码 grep）
  - 验证上游输出字段 ⊆ 下游 schema 字段 ∪ 系统字段

环境变量：
  DB_USER / DB_PASSWORD / DB_HOST / DB_PORT / DB_NAME
"""

import argparse
import json
import os
import sys

# Add ragflow project to path
RAGFLOW_ROOT = os.environ.get(
    "RAGFLOW_ROOT",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
)
sys.path.insert(0, RAGFLOW_ROOT)


# ─── Configuration ─────────────────────────────────────────────────────

DB_USER = os.environ.get("DB_USER", "noeticai")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "noeticai")
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = int(os.environ.get("DB_PORT", "5432"))
DB_NAME = os.environ.get("DB_NAME", "ragflow")

# System fields that base.py always adds to output (not from component logic)
SYSTEM_OUTPUT_FIELDS = {"_created_time", "_elapsed_time", "_ERROR"}

# Known output fields per component type (manually verified from source code)
# These are the fields set via set_output() in each component's _invoke method.
COMPONENT_OUTPUTS = {
    "File": {"file"},
    "Parser": {"json", "markdown", "text", "html", "output_format", "name"},
    "SmartSplitter": {"chunks", "output_format", "_ERROR"},
    "ChunkRouter": {
        "chunks", "output_format", "name", "route_summary",
        # Dynamic: also sets each route_key as output, e.g., "LabExam_chunks"
    },
    "Extractor": {"chunks", "output_format"},
    "ChunkMerger": {"chunks", "output_format", "name"},
    "Tokenizer": {"chunks", "output_format", "embedding_token_consumption", "_ERROR"},
    "Invoke": {"result"},
}

# Schema classes per component type that use model_validate(kwargs)
# Components NOT listed here either use kwargs.get() or get_input_elements()
SCHEMA_VALIDATED_COMPONENTS = {
    "SmartSplitter": "rag.flow.splitter.schema.SplitterFromUpstream",
    "Tokenizer": "rag.flow.tokenizer.schema.TokenizerFromUpstream",
    # Extractor uses get_input_elements(), NOT kwargs validation
    # ChunkRouter uses kwargs.get(), NOT schema validation
    # ChunkMerger uses canvas.get_variable_value(), NOT kwargs
    # Invoke uses canvas.get_variable_value(), NOT kwargs
}


# ─── Helpers ───────────────────────────────────────────────────────────

class CheckResult:
    def __init__(self):
        self.passed = []
        self.failed = []
        self.warnings = []

    def ok(self, msg):
        self.passed.append(msg)

    def fail(self, msg):
        self.failed.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)

    @property
    def success(self):
        return len(self.failed) == 0

    def report(self):
        print("\n" + "=" * 60)
        print("Pipeline Schema Compatibility Check Report")
        print("=" * 60)
        for msg in self.passed:
            print(f"  ✅ {msg}")
        for msg in self.warnings:
            print(f"  ⚠️  {msg}")
        for msg in self.failed:
            print(f"  ❌ {msg}")
        print("-" * 60)
        total = len(self.passed) + len(self.failed)
        if self.success:
            print(f"  RESULT: ALL {total} CHECKS PASSED ✅")
        else:
            print(f"  RESULT: {len(self.failed)}/{total} CHECKS FAILED ❌")
        if self.warnings:
            print(f"  WARNINGS: {len(self.warnings)}")
        print("=" * 60 + "\n")
        return self.success


def load_dsl_from_db(canvas_id):
    """Load DSL from PostgreSQL database."""
    try:
        import psycopg2
    except ImportError:
        print("ERROR: psycopg2 not installed.")
        sys.exit(1)

    conn = psycopg2.connect(
        user=DB_USER, password=DB_PASSWORD,
        host=DB_HOST, port=DB_PORT, dbname=DB_NAME
    )
    cur = conn.cursor()
    cur.execute("SELECT dsl FROM user_canvas WHERE id=%s", (canvas_id,))
    row = cur.fetchone()
    conn.close()

    if not row:
        print(f"ERROR: Canvas '{canvas_id}' not found.")
        sys.exit(1)

    return json.loads(row[0]) if isinstance(row[0], str) else row[0]


def load_dsl_from_file(filepath):
    with open(filepath) as f:
        return json.load(f)


def get_schema_fields(schema_module_path):
    """Dynamically import a schema class and return its field names + aliases."""
    parts = schema_module_path.rsplit(".", 1)
    module_path, class_name = parts[0], parts[1]

    try:
        import importlib
        mod = importlib.import_module(module_path)
        schema_cls = getattr(mod, class_name)
    except Exception as e:
        return None, str(e)

    # Get all field names (both real names and aliases)
    accepted_fields = set()
    for field_name, field_info in schema_cls.model_fields.items():
        accepted_fields.add(field_name)
        # Also add alias if it exists
        if hasattr(field_info, "alias") and field_info.alias:
            accepted_fields.add(field_info.alias)

    # Check if extra="forbid"
    config = getattr(schema_cls, "model_config", {})
    extra_mode = config.get("extra", "ignore")

    return {
        "fields": accepted_fields,
        "extra": extra_mode,
        "class": class_name,
    }, None


# ─── Check Functions ───────────────────────────────────────────────────

def check_push_mode_compatibility(dsl, result):
    """
    For each push-mode pair (upstream → downstream),
    verify upstream's output fields are accepted by downstream's schema.
    """
    components = dsl["components"]

    for cid, comp in components.items():
        obj = comp.get("obj", {})
        cpn_type = obj.get("component_name", "")

        # Only check components that use model_validate(kwargs)
        if cpn_type not in SCHEMA_VALIDATED_COMPONENTS:
            continue

        schema_path = SCHEMA_VALIDATED_COMPONENTS[cpn_type]

        # Get schema fields
        schema_info, err = get_schema_fields(schema_path)
        if err:
            result.warn(f"{cid} ({cpn_type}): Cannot load schema {schema_path}: {err}")
            continue

        schema_fields = schema_info["fields"] | SYSTEM_OUTPUT_FIELDS
        extra_mode = schema_info["extra"]

        # Only matters if extra="forbid"
        if extra_mode != "forbid":
            result.ok(f"{cid} ({cpn_type}): extra='{extra_mode}' (lenient, skip)")
            continue

        # Find upstream components
        upstream_ids = comp.get("upstream", [])
        if not upstream_ids:
            result.warn(f"{cid} ({cpn_type}): No upstream found")
            continue

        for us_id in upstream_ids:
            us_comp = components.get(us_id, {})
            us_obj = us_comp.get("obj", {})
            us_type = us_obj.get("component_name", "?")

            # Get upstream's known output fields
            us_outputs = COMPONENT_OUTPUTS.get(us_type, set()) | SYSTEM_OUTPUT_FIELDS

            # Find extra fields that upstream outputs but schema doesn't accept
            extra_fields = us_outputs - schema_fields

            if not extra_fields:
                result.ok(
                    f"{us_id} ({us_type}) → {cid} ({cpn_type}): "
                    f"all {len(us_outputs)} output fields accepted by schema"
                )
            else:
                result.fail(
                    f"{us_id} ({us_type}) → {cid} ({cpn_type}): "
                    f"EXTRA FIELDS rejected by schema (extra='forbid'): {extra_fields}"
                )


def check_input_mode_summary(dsl, result):
    """Print a summary of how each component gets its input."""
    components = dsl["components"]

    INPUT_MODES = {
        "File": "filesystem",
        "Parser": "kwargs (no schema)",
        "SmartSplitter": "kwargs → model_validate (extra=forbid) ⚠️",
        "ChunkRouter": "kwargs.get() (lenient)",
        "Extractor": "get_input_elements() (lenient)",
        "ChunkMerger": "canvas.get_variable_value() (pull)",
        "Tokenizer": "kwargs → model_validate (extra=forbid) ⚠️",
        "Invoke": "canvas.get_variable_value() (pull)",
    }

    print("\n  Input Mode Summary:")
    for cid, comp in components.items():
        obj = comp.get("obj", {})
        cpn_type = obj.get("component_name", "?")
        mode = INPUT_MODES.get(cpn_type, "unknown")
        print(f"    {cid:30s} → {mode}")
    print()

    # Count high-risk components
    high_risk = [
        cid for cid, comp in components.items()
        if comp.get("obj", {}).get("component_name", "") in ("SmartSplitter", "Tokenizer")
    ]
    result.ok(f"High-risk components (extra=forbid): {len(high_risk)} — {high_risk}")


# ─── Main ──────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Pipeline Schema Compatibility Check")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--canvas-id", help="Canvas ID to load from database")
    group.add_argument("--file", help="DSL JSON file path")
    args = parser.parse_args()

    if args.canvas_id:
        print(f"Loading DSL from database: canvas_id={args.canvas_id}")
        dsl = load_dsl_from_db(args.canvas_id)
    else:
        print(f"Loading DSL from file: {args.file}")
        dsl = load_dsl_from_file(args.file)

    result = CheckResult()

    check_push_mode_compatibility(dsl, result)
    check_input_mode_summary(dsl, result)

    success = result.report()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
