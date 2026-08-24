"""Tests for the build_chunks task watchdog contract.

Incident 2026-08-22: zombie tasks occupied all executor slots for 5+ hours
because the @timeout watchdog never fired (ENABLE_TIMEOUT_ASSERTION unset)
and, when it does fire, the outer bound must be 60 minutes (not 80).

These tests are AST-based source-contract tests: the local venv lacks the
full ragflow runtime dependencies (quart/werkzeug), so importing
rag.svr.task_executor is not possible. The contract we care about is the
declared decorator arguments, which AST inspection verifies exactly.
"""
import ast
import os
import re
import sys

import pytest

_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

TASK_EXECUTOR_PATH = os.path.join(_project_root, "rag", "svr", "task_executor.py")
CONNECTION_UTILS_PATH = os.path.join(_project_root, "common", "connection_utils.py")


def _find_timeout_decorator(funcdef: ast.FunctionDef | ast.AsyncFunctionDef):
    """Return the ast.Call node of a @timeout(...) decorator, or None."""
    for deco in funcdef.decorator_list:
        if isinstance(deco, ast.Call):
            func = deco.func
            name = getattr(func, "id", None) or getattr(func, "attr", None)
            if name == "timeout":
                return deco
    return None


def _eval_const_expr(node: ast.expr):
    """Evaluate a constant expression like ``60 * 60``.

    Python 3.14's ast.literal_eval no longer accepts BinOps, so fold
    arithmetic over constants manually (only +-*/, no names/calls).
    """
    fold = getattr(ast, "constant_fold", None)
    if fold is not None:
        return fold(node)
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.BinOp):
        left = _eval_const_expr(node.left)
        right = _eval_const_expr(node.right)
        ops = {ast.Mult: lambda a, b: a * b, ast.Add: lambda a, b: a + b,
               ast.Sub: lambda a, b: a - b, ast.Div: lambda a, b: a / b}
        op = ops.get(type(node.op))
        if op is None:
            raise ValueError(f"unsupported operator in timeout argument: {ast.dump(node.op)}")
        return op(left, right)
    raise ValueError(f"timeout argument is not a constant expression: {ast.dump(node)}")


def _find_funcdef(tree: ast.AST, name: str):
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name:
            return node
    return None


@pytest.fixture(scope="module")
def executor_tree():
    with open(TASK_EXECUTOR_PATH, "r", encoding="utf-8") as f:
        return ast.parse(f.read())


def test_build_chunks_watchdog_is_60_minutes(executor_tree):
    """build_chunks must be guarded by a 60-minute (3600s) outer watchdog."""
    funcdef = _find_funcdef(executor_tree, "build_chunks")
    assert funcdef is not None, "build_chunks not found in task_executor.py"
    deco = _find_timeout_decorator(funcdef)
    assert deco is not None, "build_chunks must carry an @timeout(...) decorator"

    seconds = _eval_const_expr(deco.args[0])
    assert seconds == 60 * 60, (
        f"build_chunks watchdog must be 60 minutes (3600s), got {seconds}s"
    )


def test_build_chunks_watchdog_does_not_retry(executor_tree):
    """attempts must stay 1: a timed-out task fails fast instead of
    spending another full watchdog window on the same zombie."""
    funcdef = _find_funcdef(executor_tree, "build_chunks")
    deco = _find_timeout_decorator(funcdef)
    assert deco is not None

    assert len(deco.args) >= 2, "@timeout must declare attempts explicitly"
    attempts = _eval_const_expr(deco.args[1])
    assert attempts == 1, f"build_chunks watchdog attempts must be 1, got {attempts}"


def test_timeout_decorator_records_config():
    """The timeout decorator must expose seconds/attempts on the wrapper so
    the watchdog contract is inspectable at runtime (e.g. by tests and ops)."""
    with open(CONNECTION_UTILS_PATH, "r", encoding="utf-8") as f:
        source = f.read()

    # Both the sync and async wrappers must record the configuration.
    assert re.search(r"_timeout_seconds\s*=\s*seconds", source), (
        "timeout decorator must record _timeout_seconds on the wrapper"
    )
    assert re.search(r"_timeout_attempts\s*=\s*attempts", source), (
        "timeout decorator must record _timeout_attempts on the wrapper"
    )

    tree = ast.parse(source)
    timeout_def = _find_funcdef(tree, "timeout")
    assert timeout_def is not None
    body_src = ast.unparse(timeout_def)
    assert "_timeout_seconds" in body_src and "_timeout_attempts" in body_src, (
        "recording must happen inside timeout()'s decorator/wrappers"
    )
