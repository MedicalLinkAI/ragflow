#
#  Copyright 2026 The InfiniFlow Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
import importlib
import sys
import types
import warnings

import pytest

warnings.filterwarnings(
    "ignore",
    message="pkg_resources is deprecated as an API.*",
    category=UserWarning,
)
warnings.filterwarnings(
    "ignore",
    message="Tensorflow not installed; ParametricUMAP will be unavailable",
    category=ImportWarning,
)


def _install_xgboost_stub_if_unavailable():
    if "xgboost" in sys.modules:
        return
    try:
        importlib.import_module("xgboost")
        sys.modules["xgboost"] = types.ModuleType("xgboost")
    except Exception:
        sys.modules["xgboost"] = types.ModuleType("xgboost")


_install_xgboost_stub_if_unavailable()

# task_executor transitively imports third-party packages (scholarly,
# graspologic, ...) that contain invalid escape sequences. deepdoc's
# beartype claw import hook recompiles them while pytest's
# filterwarnings=["error"] is active, turning SyntaxWarning into
# SyntaxError. Downgrade warnings for the whole import chain.
with warnings.catch_warnings():
    warnings.simplefilter("default")
    from rag.svr import task_executor


class FakeLock:
    instances = []
    acquire_result = True

    def __init__(self, lock_key, lock_value=None, timeout=10, blocking_timeout=1):
        self.lock_key = lock_key
        self.lock_value = lock_value
        self.timeout = timeout
        self.blocking_timeout = blocking_timeout
        self.released = False
        FakeLock.instances.append(self)

    def acquire(self):
        return type(self).acquire_result

    def release(self):
        self.released = True


@pytest.fixture
def fake_lock(monkeypatch):
    FakeLock.instances = []
    FakeLock.acquire_result = True
    monkeypatch.setattr(task_executor, "RedisDistributedLock", FakeLock)
    return FakeLock


def test_recover_uses_all_queue_names_and_heartbeat_timeout(monkeypatch, fake_lock):
    calls = []

    def fake_recover(queue_names, group_name, min_idle_ms):
        calls.append((queue_names, group_name, min_idle_ms))
        return 2

    monkeypatch.setattr(task_executor.REDIS_CONN, "recover_stale_pending_msgs", fake_recover)

    recovered = task_executor.recover_stale_pending_messages()

    assert recovered == 2
    assert calls == [
        (
            task_executor.settings.get_svr_queue_names(),
            task_executor.SVR_CONSUMER_GROUP_NAME,
            task_executor.WORKER_HEARTBEAT_TIMEOUT * 1000,
        )
    ]
    assert len(fake_lock.instances) == 1
    assert fake_lock.instances[0].released is True


def test_recover_skipped_when_lock_not_acquired(monkeypatch, fake_lock):
    calls = []

    def fake_recover(queue_names, group_name, min_idle_ms):
        calls.append((queue_names, group_name, min_idle_ms))
        return 9

    fake_lock.acquire_result = False
    monkeypatch.setattr(task_executor.REDIS_CONN, "recover_stale_pending_msgs", fake_recover)

    recovered = task_executor.recover_stale_pending_messages()

    assert recovered == 0
    assert calls == []


def test_recover_releases_lock_on_error(monkeypatch, fake_lock):
    def fake_recover(queue_names, group_name, min_idle_ms):
        raise RuntimeError("redis down")

    monkeypatch.setattr(task_executor.REDIS_CONN, "recover_stale_pending_msgs", fake_recover)

    recovered = task_executor.recover_stale_pending_messages()

    assert recovered == 0
    assert fake_lock.instances[0].released is True
