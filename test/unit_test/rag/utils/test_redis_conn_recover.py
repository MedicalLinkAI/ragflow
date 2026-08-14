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

"""
Unit tests for RedisDB.recover_stale_pending_msgs.

Scenario: when a task executor container restarts, messages delivered to the
old consumers stay in the consumer group's PEL (pending entries list) forever,
because live consumers only read new messages. recover_stale_pending_msgs must
requeue pending entries whose idle time exceeds the threshold so tasks are not
lost, while leaving messages of alive consumers untouched.
"""

from common import settings  # noqa: F401  warm circular import chain before redis_conn
from rag.utils.redis_conn import RedisDB


class FakeRedis:
    def __init__(self, pending_entries=None, xrange_result=None, xpending_error=None):
        self.pending_entries = pending_entries or []
        self.xrange_result = xrange_result if xrange_result is not None else []
        self.xpending_error = xpending_error
        self.xpending_calls = []
        self.xrange_calls = []
        self.xadd_calls = []
        self.xack_calls = []

    def xpending_range(self, queue, group, min, max, count):
        self.xpending_calls.append((queue, group, min, max, count))
        if self.xpending_error:
            raise self.xpending_error
        return self.pending_entries

    def xrange(self, queue, start, end):
        self.xrange_calls.append((queue, start, end))
        return self.xrange_result

    def xadd(self, queue, fields):
        self.xadd_calls.append((queue, fields))
        return "9999-0"

    def xack(self, queue, group, msg_id):
        self.xack_calls.append((queue, group, msg_id))
        return 1


def _make_db(fake_redis):
    # @singleton wraps RedisDB into a factory function; recover the real
    # class from its closure to instantiate without touching Redis.
    redis_db_cls = next(
        cell.cell_contents for cell in RedisDB.__closure__ if isinstance(cell.cell_contents, type)
    )
    db = object.__new__(redis_db_cls)
    db.REDIS = fake_redis
    return db


STALE_FIELDS = {"message": b'{"id": "task-stale"}'}


def test_requeues_only_stale_pending_messages():
    fake = FakeRedis(
        pending_entries=[
            {"message_id": "1000-1", "consumer": "task_executor_old_0", "time_since_delivered": 300000, "times_delivered": 1},
            {"message_id": "1000-2", "consumer": "task_executor_new_1", "time_since_delivered": 5000, "times_delivered": 1},
        ],
        xrange_result=[("1000-1", STALE_FIELDS)],
    )
    db = _make_db(fake)

    recovered = db.recover_stale_pending_msgs(["q"], "rag_svr", min_idle_ms=120000)

    assert recovered == 1
    assert fake.xadd_calls == [("q", STALE_FIELDS)]
    assert fake.xack_calls == [("q", "rag_svr", "1000-1")]
    assert fake.xrange_calls == [("q", "1000-1", "1000-1")]


def test_acks_stale_message_missing_from_stream_without_requeue():
    fake = FakeRedis(
        pending_entries=[
            {"message_id": "1000-1", "consumer": "task_executor_old_0", "time_since_delivered": 300000, "times_delivered": 1},
        ],
        xrange_result=[],
    )
    db = _make_db(fake)

    recovered = db.recover_stale_pending_msgs(["q"], "rag_svr", min_idle_ms=120000)

    assert recovered == 0
    assert fake.xadd_calls == []
    assert fake.xack_calls == [("q", "rag_svr", "1000-1")]


def test_handles_bytes_message_id_and_consumer():
    fake = FakeRedis(
        pending_entries=[
            {"message_id": b"1000-1", "consumer": b"task_executor_old_0", "time_since_delivered": 300000, "times_delivered": 1},
        ],
        xrange_result=[(b"1000-1", STALE_FIELDS)],
    )
    db = _make_db(fake)

    recovered = db.recover_stale_pending_msgs(["q"], "rag_svr", min_idle_ms=120000)

    assert recovered == 1
    assert fake.xrange_calls == [("q", "1000-1", "1000-1")]
    assert fake.xack_calls == [("q", "rag_svr", "1000-1")]


def test_missing_queue_is_tolerated():
    fake = FakeRedis(xpending_error=Exception("No such key"))
    db = _make_db(fake)

    recovered = db.recover_stale_pending_msgs(["q"], "rag_svr", min_idle_ms=120000)

    assert recovered == 0
    assert fake.xadd_calls == []
    assert fake.xack_calls == []


def test_iterates_all_queue_names():
    fake = FakeRedis(pending_entries=[])
    db = _make_db(fake)

    db.recover_stale_pending_msgs(["rag_flow_svr_queue_1", "rag_flow_svr_queue"], "rag_svr", min_idle_ms=120000)

    assert [c[0] for c in fake.xpending_calls] == ["rag_flow_svr_queue_1", "rag_flow_svr_queue"]
