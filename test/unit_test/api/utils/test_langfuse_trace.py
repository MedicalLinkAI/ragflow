import importlib.util
import sys
from pathlib import Path
from types import ModuleType, SimpleNamespace


def _load_trace_module(monkeypatch):
    repo_root = Path(__file__).resolve().parents[4]

    langfuse_mod = ModuleType("langfuse")

    class _DummyLangfuse:
        def __init__(self, *args, **kwargs):
            pass

        def create_trace_id(self):
            return "f" * 32

    langfuse_mod.Langfuse = _DummyLangfuse
    monkeypatch.setitem(sys.modules, "langfuse", langfuse_mod)

    langfuse_service_mod = ModuleType("api.db.services.langfuse_service")
    langfuse_service_mod.TenantLangfuseService = SimpleNamespace(filter_by_tenant=lambda **_kwargs: None)
    monkeypatch.setitem(sys.modules, "api.db.services.langfuse_service", langfuse_service_mod)

    module_path = repo_root / "api" / "utils" / "langfuse_trace.py"
    spec = importlib.util.spec_from_file_location("test_langfuse_trace_unit", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_resolve_trace_context_prefers_traceparent(monkeypatch):
    module = _load_trace_module(monkeypatch)

    context = module.resolve_trace_context(
        traceparent=f"00-{'a' * 32}-{'b' * 16}-01",
        x_trace_id="c" * 32,
        x_langfuse_trace_id="d" * 32,
    )

    assert context == {
        "trace_id": "a" * 32,
        "traceparent": f"00-{'a' * 32}-{'b' * 16}-01",
        "source": "traceparent",
    }


def test_resolve_trace_context_falls_back_to_unified_header_before_legacy(monkeypatch):
    module = _load_trace_module(monkeypatch)

    context = module.resolve_trace_context(
        traceparent="bad-header",
        x_trace_id="c" * 32,
        x_langfuse_trace_id="d" * 32,
    )

    assert context["trace_id"] == "c" * 32
    assert context["source"] == "x-trace-id"
    assert context["traceparent"].startswith("00-")


def test_resolve_trace_context_uses_legacy_header_as_compatibility_fallback(monkeypatch):
    module = _load_trace_module(monkeypatch)

    context = module.resolve_trace_context(
        x_trace_id=None,
        x_langfuse_trace_id="e" * 32,
    )

    assert context["trace_id"] == "e" * 32
    assert context["source"] == "x-langfuse-trace-id"


def test_build_outbound_headers_and_queue_payload_follow_bound_context(monkeypatch):
    module = _load_trace_module(monkeypatch)
    context = module.resolve_trace_context(x_trace_id="9" * 32)
    module.bind_trace_context(context)
    try:
        headers = module.build_outbound_trace_headers()
        queue_payload = module.build_queue_trace_payload()
    finally:
        module.clear_trace_context()

    assert headers == {
        "traceparent": context["traceparent"],
        "X-Trace-Id": "9" * 32,
    }
    assert queue_payload == {
        "root_trace_id": "9" * 32,
        "root_traceparent": context["traceparent"],
        "trace_source": "x-trace-id",
    }


def test_build_outbound_headers_can_include_compatibility_shim(monkeypatch):
    module = _load_trace_module(monkeypatch)
    context = module.resolve_trace_context(x_trace_id="1" * 32)
    module.bind_trace_context(context)
    try:
        headers = module.build_outbound_trace_headers(include_compatibility_header=True)
    finally:
        module.clear_trace_context()

    assert headers["X-Trace-Id"] == "1" * 32
    assert headers["X-Langfuse-Trace-Id"] == "1" * 32


def test_bind_trace_context_accepts_traceparent_only_payload(monkeypatch):
    module = _load_trace_module(monkeypatch)
    traceparent = f"00-{'2' * 32}-{'3' * 16}-01"
    module.bind_trace_context({"traceparent": traceparent, "source": "queue"})
    try:
        context = module.get_trace_context()
    finally:
        module.clear_trace_context()

    assert context == {
        "trace_id": "2" * 32,
        "traceparent": traceparent,
        "source": "queue",
    }


def test_merge_queue_trace_payload_reapplies_redis_trace_fields(monkeypatch):
    module = _load_trace_module(monkeypatch)

    merged = module.merge_queue_trace_payload(
        {"id": "task-1", "doc_id": "doc-1"},
        {
            "root_trace_id": "a" * 32,
            "root_traceparent": f"00-{'a' * 32}-{'b' * 16}-01",
            "trace_source": "queue",
        },
    )

    assert merged["id"] == "task-1"
    assert merged["doc_id"] == "doc-1"
    assert merged["root_trace_id"] == "a" * 32
    assert merged["root_traceparent"] == f"00-{'a' * 32}-{'b' * 16}-01"
    assert merged["trace_source"] == "queue"
