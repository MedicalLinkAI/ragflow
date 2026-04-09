#
#  Langfuse tracing decorator for RAGFlow API endpoints.
#
#  IMPORTANT: This decorator MUST be placed AFTER @token_required,
#  because it depends on tenant_id being resolved by the auth layer.
#
#  Correct order:
#    @manager.route("/retrieval", methods=["POST"])
#    @token_required          ← resolves tenant_id
#    @langfuse_span("xxx")   ← uses tenant_id, wraps business logic only
#    async def handler(tenant_id): ...
#
import atexit
from contextvars import ContextVar
import functools
import inspect
import logging
import os
import re
import time

try:
    from langfuse import Langfuse
    from api.db.services.langfuse_service import TenantLangfuseService
    _LANGFUSE_AVAILABLE = True
except ImportError:
    _LANGFUSE_AVAILABLE = False

_logger = logging.getLogger(__name__)
_TRACEPARENT_RE = re.compile(
    r"^(?P<version>[0-9a-f]{2})-(?P<trace_id>[0-9a-f]{32})-(?P<parent_id>[0-9a-f]{16})-(?P<flags>[0-9a-f]{2})$"
)
_TRACE_ID_RE = re.compile(r"^[0-9a-f]{32}$")

_CLIENT_TTL_SECONDS = 3600  # 1 hour — key changes are rare, use invalidate_cache() for immediate effect
_client_cache: dict[str, tuple[object, float]] = {}  # tenant_id -> (client, created_at)
_trace_context_var: ContextVar[dict | None] = ContextVar("ragflow_trace_context", default=None)


def normalize_trace_id(trace_id: str | None) -> str | None:
    candidate = (trace_id or "").strip().lower()
    if not candidate:
        return None
    if not _TRACE_ID_RE.fullmatch(candidate):
        return None
    if set(candidate) == {"0"}:
        return None
    return candidate


def normalize_traceparent(traceparent: str | None) -> str | None:
    candidate = (traceparent or "").strip().lower()
    if not candidate:
        return None
    match = _TRACEPARENT_RE.fullmatch(candidate)
    if not match:
        return None
    if set(match.group("trace_id")) == {"0"} or set(match.group("parent_id")) == {"0"}:
        return None
    return candidate


def extract_trace_id_from_traceparent(traceparent: str | None) -> str | None:
    normalized = normalize_traceparent(traceparent)
    if not normalized:
        return None
    return normalized.split("-")[1]


def synthesize_traceparent(trace_id: str) -> str:
    return f"00-{trace_id}-{os.urandom(8).hex()}-01"


def resolve_trace_context(
    *,
    traceparent: str | None = None,
    x_trace_id: str | None = None,
    x_langfuse_trace_id: str | None = None,
    client=None,
) -> dict[str, str]:
    normalized_traceparent = normalize_traceparent(traceparent)
    if normalized_traceparent:
        trace_id = extract_trace_id_from_traceparent(normalized_traceparent)
        if trace_id:
            return {
                "trace_id": trace_id,
                "traceparent": normalized_traceparent,
                "source": "traceparent",
            }

    normalized_trace_id = normalize_trace_id(x_trace_id)
    if normalized_trace_id:
        return {
            "trace_id": normalized_trace_id,
            "traceparent": synthesize_traceparent(normalized_trace_id),
            "source": "x-trace-id",
        }

    normalized_compat_trace_id = normalize_trace_id(x_langfuse_trace_id)
    if normalized_compat_trace_id:
        return {
            "trace_id": normalized_compat_trace_id,
            "traceparent": synthesize_traceparent(normalized_compat_trace_id),
            "source": "x-langfuse-trace-id",
        }

    generated_trace_id = client.create_trace_id() if client else os.urandom(16).hex()
    return {
        "trace_id": generated_trace_id,
        "traceparent": synthesize_traceparent(generated_trace_id),
        "source": "generated",
    }


def bind_trace_context(context: dict | None) -> None:
    normalized_traceparent = normalize_traceparent((context or {}).get("traceparent"))
    normalized_trace_id = normalize_trace_id((context or {}).get("trace_id")) or extract_trace_id_from_traceparent(
        normalized_traceparent
    )
    if not normalized_trace_id:
        clear_trace_context()
        return
    payload = {
        "trace_id": normalized_trace_id,
        "traceparent": normalized_traceparent or synthesize_traceparent(normalized_trace_id),
        "source": (context or {}).get("source", "context"),
    }
    _trace_context_var.set(payload)
    try:
        from quart import g as quart_g

        quart_g._langfuse_trace_context = payload
    except Exception:
        pass


def get_trace_context() -> dict | None:
    try:
        from quart import g as quart_g

        shared_ctx = getattr(quart_g, "_langfuse_trace_context", None)
    except Exception:
        shared_ctx = None

    payload = shared_ctx or _trace_context_var.get()
    if not payload:
        return None

    normalized_trace_id = normalize_trace_id(payload.get("trace_id"))
    if not normalized_trace_id:
        return None
    return {
        "trace_id": normalized_trace_id,
        "traceparent": normalize_traceparent(payload.get("traceparent")) or synthesize_traceparent(normalized_trace_id),
        "source": payload.get("source", "context"),
    }


def clear_trace_context() -> None:
    _trace_context_var.set(None)
    try:
        from quart import g as quart_g

        if hasattr(quart_g, "_langfuse_trace_context"):
            delattr(quart_g, "_langfuse_trace_context")
    except Exception:
        pass


def build_outbound_trace_headers(
    *,
    context: dict | None = None,
    include_compatibility_header: bool = False,
) -> dict[str, str]:
    active_context = context or get_trace_context()
    if not active_context:
        return {}
    headers = {
        "traceparent": active_context["traceparent"],
        "X-Trace-Id": active_context["trace_id"],
    }
    if include_compatibility_header:
        headers["X-Langfuse-Trace-Id"] = active_context["trace_id"]
    return headers


def build_queue_trace_payload(context: dict | None = None) -> dict[str, str]:
    active_context = context or get_trace_context()
    if not active_context:
        return {}
    return {
        "root_trace_id": active_context["trace_id"],
        "root_traceparent": active_context["traceparent"],
        "trace_source": active_context.get("source", "context"),
    }


def merge_queue_trace_payload(task: dict | None, payload: dict | None) -> dict:
    merged = dict(task or {})
    for key in ("root_trace_id", "root_traceparent", "trace_source"):
        if (payload or {}).get(key):
            merged[key] = payload[key]
    return merged


def _get_langfuse_client(tenant_id: str):
    """Get or create a cached Langfuse client for this tenant.

    Design decisions:
      - NO auth_check(): it's a synchronous HTTP call that would block the
        event loop and violate "never impact business latency". If credentials
        are wrong, start_span() will silently fail inside try-except.
      - TTL-based cache: re-reads DB keys every 1 hour so key rotation
        takes effect without process restart. Old clients are replaced.
    """
    if not _LANGFUSE_AVAILABLE:
        return None

    now = time.time()
    cached = _client_cache.get(tenant_id)
    if cached and (now - cached[1]) < _CLIENT_TTL_SECONDS:
        return cached[0]

    try:
        keys = TenantLangfuseService.filter_by_tenant(tenant_id=tenant_id)
        if not keys:
            return None
        client = Langfuse(
            public_key=keys.public_key,
            secret_key=keys.secret_key,
            host=keys.host,
        )
        _client_cache[tenant_id] = (client, now)
        return client
    except Exception:
        _logger.warning("Langfuse client init failed for tenant %s", tenant_id, exc_info=True)
    return None


def invalidate_cache(tenant_id: str = None):
    """Invalidate cached client(s). Call after tenant changes Langfuse keys."""
    if tenant_id:
        _client_cache.pop(tenant_id, None)
    else:
        _client_cache.clear()


def _flush_all_clients():
    """atexit hook: flush buffered traces before process exit."""
    for client, _ in _client_cache.values():
        try:
            client.flush()
        except Exception:
            pass


atexit.register(_flush_all_clients)


def langfuse_span(
    trace_name: str,
    tenant_id_param: str = "tenant_id",
):
    """Decorator that wraps an API handler with Langfuse tracing.

    Captures full raw request JSON as input, full raw response JSON as output.
    All Langfuse operations are try-excepted — zero impact on business logic.

    Args:
        trace_name: Name shown in Langfuse dashboard (e.g. "retrieval_api")
        tenant_id_param: Name of the function parameter holding tenant_id.
    """
    def decorator(fn):
        is_async = inspect.iscoroutinefunction(fn)

        @functools.wraps(fn)
        async def async_wrapper(*args, **kwargs):
            tenant_id = kwargs.get(tenant_id_param) or (args[0] if args else None)
            client = _get_langfuse_client(tenant_id) if tenant_id else None

            span = None
            t0 = time.time()
            trace_context = None

            try:
                from quart import request as quart_request

                trace_context = resolve_trace_context(
                    traceparent=quart_request.headers.get("traceparent"),
                    x_trace_id=quart_request.headers.get("X-Trace-Id"),
                    x_langfuse_trace_id=quart_request.headers.get("X-Langfuse-Trace-Id"),
                    client=client,
                )
                bind_trace_context(trace_context)
                trace_input = await quart_request.get_json(silent=True) or {}
            except Exception:
                trace_input = {}

            if client and trace_context:
                try:
                    span = client.start_span(
                        trace_context={"trace_id": trace_context["trace_id"]},
                        name=trace_name,
                        input=trace_input,
                    )
                except Exception:
                    _logger.warning("Langfuse trace start failed", exc_info=True)

            try:
                result = await fn(*args, **kwargs)
                if span:
                    try:
                        elapsed_ms = round((time.time() - t0) * 1000, 2)
                        trace_output = {"_elapsed_ms": elapsed_ms}
                        if hasattr(result, 'get_json'):
                            try:
                                resp_json = await result.get_json(silent=True) or {}
                                resp_json["_elapsed_ms"] = elapsed_ms
                                trace_output = resp_json
                            except Exception:
                                pass
                        span.update(output=trace_output)
                        span.end()
                    except Exception:
                        _logger.warning("Langfuse trace end failed", exc_info=True)
                return result
            except Exception as e:
                if span:
                    try:
                        span.update(level="ERROR", status_message=str(e))
                        span.end()
                    except Exception:
                        pass
                raise
            finally:
                clear_trace_context()

        @functools.wraps(fn)
        def sync_wrapper(*args, **kwargs):
            tenant_id = kwargs.get(tenant_id_param) or (args[0] if args else None)
            client = _get_langfuse_client(tenant_id) if tenant_id else None

            span = None
            t0 = time.time()
            trace_context = None

            try:
                from quart import request as quart_request

                trace_context = resolve_trace_context(
                    traceparent=quart_request.headers.get("traceparent"),
                    x_trace_id=quart_request.headers.get("X-Trace-Id"),
                    x_langfuse_trace_id=quart_request.headers.get("X-Langfuse-Trace-Id"),
                    client=client,
                )
                bind_trace_context(trace_context)
            except Exception:
                trace_context = None

            if client:
                try:
                    if not trace_context:
                        trace_context = resolve_trace_context(client=client)
                        bind_trace_context(trace_context)
                    span = client.start_span(
                        trace_context={"trace_id": trace_context["trace_id"]},
                        name=trace_name,
                        input={"note": "sync endpoint"},
                    )
                except Exception:
                    _logger.warning("Langfuse trace start failed", exc_info=True)

            try:
                result = fn(*args, **kwargs)
                if span:
                    try:
                        elapsed_ms = round((time.time() - t0) * 1000, 2)
                        span.update(output={"_elapsed_ms": elapsed_ms})
                        span.end()
                    except Exception:
                        _logger.warning("Langfuse trace end failed", exc_info=True)
                return result
            except Exception as e:
                if span:
                    try:
                        span.update(level="ERROR", status_message=str(e))
                        span.end()
                    except Exception:
                        pass
                raise
            finally:
                clear_trace_context()

        return async_wrapper if is_async else sync_wrapper
    return decorator
