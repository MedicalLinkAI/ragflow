#!/usr/bin/env python3
"""
Pipeline DSL 静态一致性检查脚本

功能：
  1. edges ↔ downstream 双向一致性检查
  2. graph.nodes ↔ components 一致性检查
  3. BFS path 模拟（检查步数和重复）
  4. pull 模式组件重复触发检查
  5. source_components / variable refs 引用有效性检查
  6. downstream 指向不存在组件检查

用法：
  cd ragflow/
  python scripts/pipeline_check_dsl.py --canvas-id 192c7f7898814e99a34a856ce567a57c

环境变量：
  DB_USER     (default: noeticai)
  DB_PASSWORD (default: noeticai)
  DB_HOST     (default: localhost)
  DB_PORT     (default: 5432)
  DB_NAME     (default: ragflow)
"""

import argparse
import json
import os
import sys
from collections import defaultdict


# ─── Configuration ─────────────────────────────────────────────────────

DB_USER = os.environ.get("DB_USER", "noeticai")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "noeticai")
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = int(os.environ.get("DB_PORT", "5432"))
DB_NAME = os.environ.get("DB_NAME", "ragflow")


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
        print("Pipeline DSL Static Check Report")
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
        print("ERROR: psycopg2 not installed. Install with: pip install psycopg2-binary")
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
        print(f"ERROR: Canvas '{canvas_id}' not found in user_canvas table.")
        sys.exit(1)

    return json.loads(row[0]) if isinstance(row[0], str) else row[0]


def load_dsl_from_file(filepath):
    """Load DSL from a JSON file."""
    with open(filepath) as f:
        return json.load(f)


# ─── Check Functions ───────────────────────────────────────────────────

def check_nodes_components_consistency(dsl, result):
    """Check 1: graph.nodes ↔ components keys 一致性"""
    node_ids = {n["id"] for n in dsl["graph"]["nodes"] if n.get("id") != "begin"}
    comp_ids = set(dsl["components"].keys())

    missing_in_components = node_ids - comp_ids
    missing_in_nodes = comp_ids - node_ids

    if not missing_in_components and not missing_in_nodes:
        result.ok(f"Nodes ↔ Components consistent: {len(node_ids)} nodes, {len(comp_ids)} components")
    else:
        if missing_in_components:
            result.fail(f"Nodes in graph but missing in components: {missing_in_components}")
        if missing_in_nodes:
            result.fail(f"Components exist but missing in graph.nodes: {missing_in_nodes}")


def check_edges_downstream_consistency(dsl, result):
    """Check 2: graph.edges ↔ components.downstream 双向一致性"""
    # Build edge map from graph.edges
    edges_downstream = defaultdict(set)
    for e in dsl["graph"]["edges"]:
        src = e.get("source", "")
        tgt = e.get("target", "")
        if src and tgt and src != "begin":
            edges_downstream[src].add(tgt)

    # Build downstream map from components
    comp_downstream = {}
    for cid, comp in dsl["components"].items():
        comp_downstream[cid] = set(comp.get("downstream", []))

    # Compare: edges → downstream
    mismatches = []
    all_src_ids = set(edges_downstream.keys()) | set(comp_downstream.keys())
    for cid in sorted(all_src_ids):
        edge_ds = edges_downstream.get(cid, set())
        comp_ds = comp_downstream.get(cid, set())
        if edge_ds != comp_ds:
            mismatches.append(f"  {cid}: edges→{sorted(edge_ds)}, components→{sorted(comp_ds)}")

    if not mismatches:
        total_edges = sum(len(v) for v in edges_downstream.values())
        result.ok(f"Edges ↔ Downstream consistent: {total_edges} edges match")
    else:
        result.fail("Edges ↔ Downstream MISMATCH:\n" + "\n".join(mismatches))


def check_upstream_consistency(dsl, result):
    """Check 3: components.upstream 反向一致性 — 每个 downstream 条目对应的目标组件的 upstream 应包含源"""
    issues = []
    for cid, comp in dsl["components"].items():
        for ds_id in comp.get("downstream", []):
            ds_comp = dsl["components"].get(ds_id)
            if not ds_comp:
                issues.append(f"  {cid} → downstream '{ds_id}' does not exist in components")
                continue
            us_list = ds_comp.get("upstream", [])
            if cid not in us_list:
                issues.append(f"  {cid} → {ds_id}: {ds_id}.upstream={us_list} does not contain '{cid}'")

    if not issues:
        result.ok("Upstream ↔ Downstream reverse consistency: OK")
    else:
        result.fail("Upstream ↔ Downstream reverse MISMATCH:\n" + "\n".join(issues))


def check_bfs_path(dsl, result):
    """Check 4: BFS path 模拟 — 检查步数和重复"""
    components = dsl["components"]

    # Find start node (File component, or node with no upstream)
    start_id = None
    for cid, comp in components.items():
        obj = comp.get("obj", {})
        if obj.get("component_name") == "File":
            start_id = cid
            break
    if not start_id:
        # Fallback: find node with no upstream
        for cid, comp in components.items():
            if not comp.get("upstream", []):
                start_id = cid
                break
    if not start_id:
        result.fail("Cannot find start node for BFS path simulation")
        return

    # Simulate BFS path construction (mirrors pipeline.py logic)
    path = [start_id]
    idx = 0
    # Extend with first node's downstream
    path.extend(components[start_id].get("downstream", []))
    idx = 1

    max_iterations = 100  # Safety limit
    while idx < len(path) and max_iterations > 0:
        max_iterations -= 1
        cpn_id = path[idx]
        downstream = components.get(cpn_id, {}).get("downstream", [])
        path.extend(downstream)
        idx += 1

    if max_iterations <= 0:
        result.fail(f"BFS path simulation exceeded 100 iterations (infinite loop?). Path length: {len(path)}")
        return

    # Check for duplicates
    seen = set()
    duplicates = []
    for i, cid in enumerate(path):
        if cid in seen:
            duplicates.append(f"  Step [{i}]: {cid} (already seen)")
        seen.add(cid)

    if not duplicates:
        result.ok(f"BFS path simulation: {len(path)} steps, no duplicates")
        result.ok(f"Path: {' → '.join(path)}")
    else:
        result.fail(f"BFS path has DUPLICATES ({len(path)} steps):\n" + "\n".join(duplicates))
        result.fail(f"Full path: {' → '.join(path)}")


def check_pull_mode_triggers(dsl, result):
    """Check 5: pull 模式组件（ChunkMerger/Invoke）不应被多条 downstream 指向"""
    components = dsl["components"]

    # Identify pull-mode components
    pull_components = {}
    for cid, comp in components.items():
        obj = comp.get("obj", {})
        cpn_name = obj.get("component_name", "")
        if cpn_name in ("ChunkMerger", "Invoke"):
            pull_components[cid] = cpn_name

    # Count how many components point to each pull-mode component via downstream
    incoming_count = defaultdict(list)
    for cid, comp in components.items():
        for ds_id in comp.get("downstream", []):
            if ds_id in pull_components:
                incoming_count[ds_id].append(cid)

    issues = []
    for pull_id, sources in incoming_count.items():
        if len(sources) > 1:
            issues.append(
                f"  {pull_id} ({pull_components[pull_id]}): "
                f"triggered by {len(sources)} upstream components: {sources} "
                f"→ will execute {len(sources)} times!"
            )

    if not issues:
        pull_info = ", ".join(f"{cid}({cn}): 1 trigger" for cid, cn in pull_components.items())
        result.ok(f"Pull-mode trigger check: OK ({pull_info})")
    else:
        result.fail("Pull-mode components triggered MULTIPLE times:\n" + "\n".join(issues))


def check_source_components_refs(dsl, result):
    """Check 6: source_components / variable refs 引用有效性"""
    components = dsl["components"]
    comp_ids = set(components.keys())
    issues = []

    for cid, comp in components.items():
        obj = comp.get("obj", {})
        params = obj.get("params", {})

        # Check source_components (ChunkMerger)
        src_comps = params.get("source_components", None)
        if src_comps is not None:
            for sc in src_comps:
                if sc not in comp_ids:
                    issues.append(f"  {cid}: source_components ref '{sc}' not found in components")

        # Check variable refs (Invoke)
        variables = params.get("variables", None)
        if variables is not None:
            for var in variables:
                ref = var.get("ref", "")
                if ref and "@" in ref:
                    ref_comp = ref.split("@")[0]
                    if ref_comp not in comp_ids:
                        issues.append(f"  {cid}: variable ref '{ref}' references non-existent component '{ref_comp}'")

    if not issues:
        # Count refs
        total_refs = 0
        for cid, comp in components.items():
            obj = comp.get("obj", {})
            params = obj.get("params", {})
            sc = params.get("source_components")
            if sc:
                total_refs += len(sc)
            vs = params.get("variables")
            if vs:
                total_refs += sum(1 for v in vs if v.get("ref"))
        result.ok(f"Source/variable refs: all {total_refs} references valid")
    else:
        result.fail("Invalid refs found:\n" + "\n".join(issues))


def check_downstream_targets_exist(dsl, result):
    """Check 7: downstream 指向的组件必须存在"""
    components = dsl["components"]
    comp_ids = set(components.keys())
    issues = []

    for cid, comp in components.items():
        for ds_id in comp.get("downstream", []):
            if ds_id not in comp_ids:
                issues.append(f"  {cid}: downstream '{ds_id}' not found in components")

    if not issues:
        result.ok("Downstream targets: all exist in components")
    else:
        result.fail("Downstream targets NOT FOUND:\n" + "\n".join(issues))


# ─── Main ──────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Pipeline DSL Static Consistency Check")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--canvas-id", help="Canvas ID to load from database")
    group.add_argument("--file", help="DSL JSON file path")
    args = parser.parse_args()

    # Load DSL
    if args.canvas_id:
        print(f"Loading DSL from database: canvas_id={args.canvas_id}")
        dsl = load_dsl_from_db(args.canvas_id)
    else:
        print(f"Loading DSL from file: {args.file}")
        dsl = load_dsl_from_file(args.file)

    result = CheckResult()

    # Run all checks
    check_nodes_components_consistency(dsl, result)
    check_edges_downstream_consistency(dsl, result)
    check_upstream_consistency(dsl, result)
    check_bfs_path(dsl, result)
    check_pull_mode_triggers(dsl, result)
    check_source_components_refs(dsl, result)
    check_downstream_targets_exist(dsl, result)

    # Report
    success = result.report()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
