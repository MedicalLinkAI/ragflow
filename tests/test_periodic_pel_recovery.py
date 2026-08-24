"""Contract tests: PEL stale-message recovery must run periodically.

Incident 2026-08-22 (§4.2): recover_stale_pending_messages() only ran once
at executor startup, so messages stranded by zombie consumer threads were
never requeued and 18 documents stayed RUNNING for 5+ hours.

New contract:
- the heartbeat loop (report_status) invokes recover_stale_pending_messages
  on a fixed interval (STALE_RECOVERY_INTERVAL seconds);
- the invocation is exception-safe (a recovery failure must not break the
  heartbeat loop);
- the original startup-time invocation in main() is preserved.

AST-based source-contract tests: the local venv lacks the full ragflow
runtime dependencies, so importing rag.svr.task_executor is not possible.
"""
import ast
import os
import sys

import pytest

_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

TASK_EXECUTOR_PATH = os.path.join(_project_root, "rag", "svr", "task_executor.py")


def _find_funcdef(tree: ast.AST, name: str):
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name:
            return node
    return None


def _calls_named(scope: ast.AST, func_name: str):
    """All Call nodes inside scope whose callee is `func_name`."""
    hits = []
    for node in ast.walk(scope):
        if isinstance(node, ast.Call):
            callee = node.func
            if getattr(callee, "id", None) == func_name or getattr(callee, "attr", None) == func_name:
                hits.append(node)
    return hits


def _eval_const_expr(node: ast.expr):
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mult):
        return _eval_const_expr(node.left) * _eval_const_expr(node.right)
    raise ValueError(f"not a constant expression: {ast.dump(node)}")


@pytest.fixture(scope="module")
def executor_tree():
    with open(TASK_EXECUTOR_PATH, "r", encoding="utf-8") as f:
        return ast.parse(f.read())


def test_report_status_runs_periodic_pel_recovery(executor_tree):
    """The heartbeat loop must invoke recover_stale_pending_messages."""
    report_status = _find_funcdef(executor_tree, "report_status")
    assert report_status is not None, "report_status not found in task_executor.py"

    calls = _calls_named(report_status, "recover_stale_pending_messages")
    assert calls, (
        "report_status must call recover_stale_pending_messages periodically; "
        "a startup-only invocation leaves zombie-stranded messages unrecovered "
        "(incident 2026-08-22 §4.2)"
    )


def test_pel_recovery_in_heartbeat_is_exception_safe(executor_tree):
    """A failing recovery must not kill the heartbeat loop: the call must sit
    inside a try/except within report_status."""
    report_status = _find_funcdef(executor_tree, "report_status")
    assert report_status is not None

    safe = False
    for try_node in ast.walk(report_status):
        if isinstance(try_node, ast.Try) and _calls_named(try_node, "recover_stale_pending_messages"):
            safe = True
            break
    assert safe, "recover_stale_pending_messages call must be wrapped in try/except inside report_status"


def test_stale_recovery_interval_is_30_seconds(executor_tree):
    """Throttle constant: recover at most once per heartbeat beat (30s)."""
    const = None
    for node in executor_tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "STALE_RECOVERY_INTERVAL":
                    const = _eval_const_expr(node.value)
    assert const is not None, "module-level STALE_RECOVERY_INTERVAL constant is missing"
    assert const == 30, f"STALE_RECOVERY_INTERVAL must be 30 (seconds), got {const}"


def test_startup_pel_recovery_preserved(executor_tree):
    """Regression guard: the original startup-time invocation in main() must
    not be removed by the periodic-recovery change."""
    main_def = _find_funcdef(executor_tree, "main")
    assert main_def is not None
    assert _calls_named(main_def, "recover_stale_pending_messages"), (
        "main() must still call recover_stale_pending_messages at startup"
    )
