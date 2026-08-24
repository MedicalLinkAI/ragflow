"""Behavioral tests: the timeout assertion (watchdog) must be ON by default.

Incident 2026-08-22 showed the watchdog was a paper gun because it only
armed itself when the ENABLE_TIMEOUT_ASSERTION env var was set — which no
deployment had done, so zombie tasks blocked executor slots for 5+ hours.

New contract:
- env var UNSET  -> assertion ENABLED (default)
- env var 0/false/no/off/"" -> assertion disabled (explicit escape hatch)
- any other value -> assertion enabled

The local venv lacks quart/strenum, so those two modules are stubbed just
enough to import common.connection_utils; the timeout logic under test is
real, unmocked code.
"""
import asyncio
import os
import sys
import types

import pytest

_project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _project_root not in sys.path:
    sys.path.insert(0, _project_root)

# ---- dependency stubs (quart/strenum are absent from the local venv) ----
if "quart" not in sys.modules:
    _quart = types.ModuleType("quart")
    _quart.make_response = lambda *a, **k: None
    _quart.jsonify = lambda *a, **k: None
    sys.modules["quart"] = _quart

try:
    import strenum  # noqa: F401
except ImportError:
    from enum import Enum

    class _StrEnumFallback(str, Enum):
        pass

    _strenum = types.ModuleType("strenum")
    _strenum.StrEnum = _StrEnumFallback
    sys.modules["strenum"] = _strenum

from common.connection_utils import timeout  # noqa: E402


@pytest.fixture(autouse=True)
def _clean_env(monkeypatch):
    monkeypatch.delenv("ENABLE_TIMEOUT_ASSERTION", raising=False)


def test_async_watchdog_fires_by_default(monkeypatch):
    """Env var unset: a hung coroutine must be cancelled by the watchdog."""
    monkeypatch.delenv("ENABLE_TIMEOUT_ASSERTION", raising=False)

    @timeout(0.05, 1)
    async def hung():
        await asyncio.sleep(2)
        return "should not get here"

    with pytest.raises(TimeoutError):
        asyncio.run(hung())


def test_sync_watchdog_fires_by_default(monkeypatch):
    """Env var unset: a hung sync function must be timed out too."""
    monkeypatch.delenv("ENABLE_TIMEOUT_ASSERTION", raising=False)

    @timeout(0.05, 1)
    def hung():
        import time
        time.sleep(0.3)
        return "should not get here"

    with pytest.raises(TimeoutError):
        hung()


def test_watchdog_can_be_disabled_explicitly(monkeypatch):
    """Setting the env var to a falsy value keeps the legacy escape hatch."""
    monkeypatch.setenv("ENABLE_TIMEOUT_ASSERTION", "0")

    @timeout(0.05, 1)
    async def slow_but_ok():
        await asyncio.sleep(0.2)
        return "done"

    assert asyncio.run(slow_but_ok()) == "done"


def test_watchdog_still_enabled_for_truthy_values(monkeypatch):
    """Legacy 'true'/'1' values keep the watchdog armed."""
    for value in ("true", "1"):
        monkeypatch.setenv("ENABLE_TIMEOUT_ASSERTION", value)

        @timeout(0.05, 1)
        async def hung():
            await asyncio.sleep(2)
            return "should not get here"

        with pytest.raises(TimeoutError):
            asyncio.run(hung())
