"""Contract tests: PEL recovery must NOT requeue messages held by live executors.

Regression found 2026-08-24 during local acceptance of the S5 periodic PEL
recovery: a single document parsed once produced THREE full pipeline runs
(107 chunks instead of 35). Root cause: recover_stale_pending_msgs requeued
any PEL entry idle > 120s, but a legitimately running task keeps its message
in the PEL until completion (ack on done) — a 9-minute parse is always
"stale" by that rule, so periodic recovery cloned it every ~2 minutes.

New contract:
- RedisDB.recover_stale_pending_msgs accepts a should_requeue(consumer,
  task_id) predicate and must consult it before requeuing;
- task_executor supplies a liveness guard:
  * own consumer name: skip messages whose task is in CURRENT_TASKS
    (currently executing in this process); previous-incarnation entries
    after a restart are still recovered because CURRENT_TASKS is empty;
  * other consumer names: skip while their heartbeat is fresh (zcount over
    the heartbeat zset within WORKER_HEARTBEAT_TIMEOUT).

AST + isolated-exec tests: the local venv lacks the full ragflow runtime
dependencies (filelock etc.), so importing rag.utils.redis_conn /
rag.svr.task_executor is not possible.
"""
import ast
import json
import os
import sys
import textwrap

import pytest

_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

TASK_EXECUTOR_PATH = os.path.join(_project_root, "rag", "svr", "task_executor.py")
REDIS_CONN_PATH = os.path.join(_project_root, "rag", "utils", "redis_conn.py")


def _parse(path):
    with open(path, "r", encoding="utf-8") as f:
        return ast.parse(f.read())


def _find_funcdef(tree, name):
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name:
            return node
    return None


@pytest.fixture(scope="module")
def executor_tree():
    return _parse(TASK_EXECUTOR_PATH)


@pytest.fixture(scope="module")
def redis_tree():
    return _parse(REDIS_CONN_PATH)


# ── redis_conn.py: recover_stale_pending_msgs must support a liveness guard ──


def test_recover_accepts_should_requeue_predicate(redis_tree):
    func = _find_funcdef(redis_tree, "recover_stale_pending_msgs")
    assert func is not None, "recover_stale_pending_msgs not found"
    arg_names = [a.arg for a in func.args.args] + [a.arg for a in func.args.kwonlyargs]
    assert "should_requeue" in arg_names, (
        "recover_stale_pending_msgs must accept a should_requeue predicate; "
        "idle-only requeue duplicates in-flight long tasks (regression 2026-08-24)"
    )


def test_recover_consults_predicate_before_requeue(redis_tree):
    """The predicate must actually gate the xadd/xack requeue path."""
    func = _find_funcdef(redis_tree, "recover_stale_pending_msgs")
    assert func is not None

    consulted = False
    for node in ast.walk(func):
        if isinstance(node, ast.Call) and getattr(node.func, "id", None) == "should_requeue":
            consulted = True
            break
    assert consulted, "recover_stale_pending_msgs must call should_requeue to gate requeue"

    # gate must sit before the requeue side effect
    src = ast.unparse(func)
    gate_pos = src.find("should_requeue(")
    add_pos = src.find("xadd(")
    assert 0 <= gate_pos < add_pos, "should_requeue gate must precede the xadd requeue"


# ── task_executor.py: liveness guard wiring ──


def test_periodic_recovery_passes_liveness_guard(executor_tree):
    wrapper = _find_funcdef(executor_tree, "recover_stale_pending_messages")
    assert wrapper is not None

    passed = False
    for node in ast.walk(wrapper):
        if isinstance(node, ast.Call) and getattr(node.func, "attr", None) == "recover_stale_pending_msgs":
            for kw in node.keywords:
                if kw.arg == "should_requeue" and not (isinstance(kw.value, ast.Constant) and kw.value.value is None):
                    passed = True
    assert passed, (
        "recover_stale_pending_messages must pass a non-None should_requeue guard; "
        "without it periodic recovery clones in-flight long tasks (regression 2026-08-24)"
    )


def test_liveness_guard_skips_own_inflight_tasks(executor_tree):
    """Guard must consult CURRENT_TASKS so a task executing in this process
    is never requeued mid-flight."""
    guard = _find_guard(executor_tree)
    src = ast.unparse(guard)
    assert "CURRENT_TASKS" in src, "liveness guard must protect tasks in CURRENT_TASKS"
    assert "CONSUMER_NAME" in src, "liveness guard must distinguish own consumer from others"


def test_liveness_guard_checks_other_consumers_heartbeat(executor_tree):
    """For other consumers, freshness of their heartbeat zset decides."""
    guard = _find_guard(executor_tree)
    src = ast.unparse(guard)
    assert "zcount" in src, "liveness guard must check other consumers via heartbeat zcount"
    assert "WORKER_HEARTBEAT_TIMEOUT" in src, "heartbeat freshness window must be WORKER_HEARTBEAT_TIMEOUT"


def _find_guard(executor_tree):
    """The guard is the function passed as should_requeue in the wrapper."""
    wrapper = _find_funcdef(executor_tree, "recover_stale_pending_messages")
    assert wrapper is not None
    guard_name = None
    for node in ast.walk(wrapper):
        if isinstance(node, ast.Call) and getattr(node.func, "attr", None) == "recover_stale_pending_msgs":
            for kw in node.keywords:
                if kw.arg == "should_requeue":
                    guard_name = getattr(kw.value, "id", None) or getattr(kw.value, "attr", None)
    assert guard_name, "should_requeue keyword not found on recover_stale_pending_msgs call"
    guard = _find_funcdef(executor_tree, guard_name)
    assert guard is not None, f"guard function {guard_name} not found"
    return guard


# ── isolated behavior tests of the guard predicate ──


def _load_guard(executor_tree):
    """Exec only the guard function source with stubbed globals."""
    guard = _find_guard(executor_tree)
    src = textwrap.dedent(ast.unparse(guard))

    zcount_calls = []

    class FakeRedis:
        def __init__(self, alive_consumers):
            self.alive = set(alive_consumers)

        def zcount(self, key, lo, hi):
            zcount_calls.append(key)
            return 1 if key in self.alive else 0

    namespace = {
        "CONSUMER_NAME": "exec_self",
        "CURRENT_TASKS": {"task-inflight": {}},
        "REDIS_CONN": FakeRedis(alive_consumers={"exec_other_alive"}),
        "WORKER_HEARTBEAT_TIMEOUT": 120,
        "time": __import__("time"),
        "logging": __import__("logging"),
    }
    exec(compile(src, "<guard>", "exec"), namespace)
    return namespace[guard.name], zcount_calls


def test_guard_behavior_own_inflight_task_is_protected(executor_tree):
    guard, _ = _load_guard(executor_tree)
    assert guard("exec_self", "task-inflight") is False, (
        "own consumer holding a task currently executing must not be requeued"
    )


def test_guard_behavior_own_dead_incarnation_is_recovered(executor_tree):
    """After restart CURRENT_TASKS is empty: old PEL entries under the same
    consumer name must still be recovered (incident hand-over case)."""
    guard, _ = _load_guard(executor_tree)
    assert guard("exec_self", "task-from-old-incarnation") is True


def test_guard_behavior_other_live_consumer_is_protected(executor_tree):
    guard, _ = _load_guard(executor_tree)
    assert guard("exec_other_alive", "any-task") is False, (
        "another executor with a fresh heartbeat may legitimately hold long tasks"
    )


def test_guard_behavior_other_dead_consumer_is_recovered(executor_tree):
    guard, zcount_calls = _load_guard(executor_tree)
    assert guard("exec_crashed", "any-task") is True
    assert "exec_crashed" in zcount_calls, "dead-consumer decision must come from heartbeat check"
