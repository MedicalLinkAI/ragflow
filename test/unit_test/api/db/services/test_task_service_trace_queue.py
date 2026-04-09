import copy
import importlib
import importlib.util
import sys
import types
import warnings
from types import SimpleNamespace

warnings.filterwarnings(
    "ignore",
    message="pkg_resources is deprecated as an API.*",
    category=UserWarning,
)


def _install_cv2_stub_if_unavailable():
    try:
        importlib.import_module("cv2")
        return
    except Exception:
        pass

    stub = types.ModuleType("cv2")
    stub.INTER_LINEAR = 1
    stub.INTER_CUBIC = 2
    stub.BORDER_CONSTANT = 0
    stub.BORDER_REPLICATE = 1

    def _missing(*_args, **_kwargs):
        raise RuntimeError("cv2 runtime call is unavailable in this test environment")

    def _module_getattr(name):
        if name.isupper():
            return 0
        return _missing

    stub.__getattr__ = _module_getattr
    sys.modules["cv2"] = stub


def _install_xgboost_stub_if_unavailable():
    if "xgboost" in sys.modules:
        return
    if importlib.util.find_spec("xgboost") is not None:
        sys.modules["xgboost"] = types.ModuleType("xgboost")
        return
    sys.modules["xgboost"] = types.ModuleType("xgboost")


_install_cv2_stub_if_unavailable()
_install_xgboost_stub_if_unavailable()

from api.db.services import task_service as task_service_module


TRACE_FIELDS = {"root_trace_id", "root_traceparent", "trace_source"}


def test_queue_tasks_keeps_trace_fields_out_of_db_payload(monkeypatch):
    insert_payloads = []
    queue_messages = []

    monkeypatch.setattr(task_service_module, "get_uuid", lambda: "task-1")
    monkeypatch.setattr(
        task_service_module,
        "build_queue_trace_payload",
        lambda: {
            "root_trace_id": "a" * 32,
            "root_traceparent": f"00-{'a' * 32}-{'b' * 16}-01",
            "trace_source": "traceparent",
        },
    )
    monkeypatch.setattr(
        task_service_module,
        "bulk_insert_into_db",
        lambda *args, **kwargs: insert_payloads.extend(
            kwargs["data_source"] if "data_source" in kwargs else args[1]
        ),
    )
    monkeypatch.setattr(task_service_module.DocumentService, "get_chunking_config", lambda _doc_id: {"tenant_id": "tenant-1", "kb_id": "kb-1", "parser_config": {}})
    monkeypatch.setattr(task_service_module.TaskService, "get_tasks", lambda _doc_id: [])
    monkeypatch.setattr(task_service_module.DocumentService, "update_by_id", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(task_service_module.DocumentService, "begin2parse", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(task_service_module.settings, "get_svr_queue_name", lambda _priority: "queue")
    monkeypatch.setattr(
        task_service_module.REDIS_CONN,
        "queue_product",
        lambda _queue_name, message: queue_messages.append(copy.deepcopy(message)) or True,
    )

    task_service_module.queue_tasks(
        {
            "id": "doc-1",
            "type": "txt",
            "parser_id": "naive",
            "parser_config": {},
        },
        bucket="bucket",
        name="demo.txt",
        priority=3,
    )

    assert len(insert_payloads) == 1
    assert len(queue_messages) == 1

    db_task = insert_payloads[0]
    queue_task = queue_messages[0]

    assert TRACE_FIELDS.isdisjoint(db_task.keys())
    assert TRACE_FIELDS.issubset(queue_task.keys())

    for key, value in db_task.items():
        assert queue_task[key] == value


def test_queue_dataflow_keeps_trace_fields_out_of_db_payload(monkeypatch):
    insert_payloads = []
    queue_messages = []

    monkeypatch.setattr(
        task_service_module,
        "build_queue_trace_payload",
        lambda: {
            "root_trace_id": "c" * 32,
            "root_traceparent": f"00-{'c' * 32}-{'d' * 16}-01",
            "trace_source": "queue",
        },
    )
    monkeypatch.setattr(
        task_service_module,
        "bulk_insert_into_db",
        lambda *args, **kwargs: insert_payloads.extend(
            kwargs["data_source"] if "data_source" in kwargs else args[1]
        ),
    )
    monkeypatch.setattr(task_service_module.DocumentService, "get_knowledgebase_id", lambda _doc_id: "kb-1")
    monkeypatch.setattr(task_service_module.settings, "get_svr_queue_name", lambda _priority: "queue")
    monkeypatch.setattr(
        task_service_module.REDIS_CONN,
        "queue_product",
        lambda _queue_name, message: queue_messages.append(copy.deepcopy(message)) or True,
    )

    ok, detail = task_service_module.queue_dataflow(
        tenant_id="tenant-1",
        flow_id="flow-1",
        task_id="task-1",
        doc_id=task_service_module.CANVAS_DEBUG_DOC_ID,
        file={"name": "demo.txt"},
        priority=1,
    )

    assert ok is True
    assert detail == ""
    assert len(insert_payloads) == 1
    assert len(queue_messages) == 1

    db_task = insert_payloads[0]
    queue_task = queue_messages[0]

    assert TRACE_FIELDS.isdisjoint(db_task.keys())
    assert TRACE_FIELDS.issubset(queue_task.keys())
    assert queue_task["tenant_id"] == "tenant-1"
    assert queue_task["dataflow_id"] == "flow-1"
    assert queue_task["kb_id"] == "kb-1"
    assert queue_task["file"] == {"name": "demo.txt"}

    for key, value in db_task.items():
        assert queue_task[key] == value


def test_queue_dataflow_prefers_explicit_trace_payload_across_thread_boundaries(monkeypatch):
    queue_messages = []

    class _Field:
        def __eq__(self, other):
            return ("eq", other)

    class _DeleteQuery:
        def where(self, _expr):
            return self

        def execute(self):
            return 1

    class _TaskModel:
        doc_id = _Field()

        @staticmethod
        def delete():
            return _DeleteQuery()

    monkeypatch.setattr(task_service_module.TaskService, "model", _TaskModel)
    monkeypatch.setattr(task_service_module, "bulk_insert_into_db", lambda *args, **kwargs: None)
    monkeypatch.setattr(task_service_module.DocumentService, "begin2parse", lambda *_args, **_kwargs: None)
    monkeypatch.setattr(task_service_module.DocumentService, "get_knowledgebase_id", lambda _doc_id: "kb-1")
    monkeypatch.setattr(task_service_module, "build_queue_trace_payload", lambda: {})
    monkeypatch.setattr(task_service_module.settings, "get_svr_queue_name", lambda _priority: "queue")
    monkeypatch.setattr(
        task_service_module.REDIS_CONN,
        "queue_product",
        lambda _queue_name, message: queue_messages.append(copy.deepcopy(message)) or True,
    )

    explicit_trace_payload = {
        "root_trace_id": "e" * 32,
        "root_traceparent": f"00-{'e' * 32}-{'f' * 16}-01",
        "trace_source": "threadpool",
    }

    ok, detail = task_service_module.queue_dataflow(
        tenant_id="tenant-1",
        flow_id="flow-1",
        task_id="task-1",
        doc_id="doc-1",
        priority=1,
        trace_payload=explicit_trace_payload,
    )

    assert ok is True
    assert detail == ""
    assert queue_messages[0]["root_trace_id"] == explicit_trace_payload["root_trace_id"]
    assert queue_messages[0]["root_traceparent"] == explicit_trace_payload["root_traceparent"]
    assert queue_messages[0]["trace_source"] == "threadpool"
