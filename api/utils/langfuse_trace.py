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
import functools
import inspect
import logging
import time

try:
    from langfuse import Langfuse
    from api.db.services.langfuse_service import TenantLangfuseService
    _LANGFUSE_AVAILABLE = True
except ImportError:
    _LANGFUSE_AVAILABLE = False

_logger = logging.getLogger(__name__)

_CLIENT_TTL_SECONDS = 3600  # 1 hour — key changes are rare, use invalidate_cache() for immediate effect
_client_cache: dict[str, tuple[object, float]] = {}  # tenant_id -> (client, created_at)


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

            if client:
                try:
                    from quart import request as quart_request, g as quart_g
                    trace_input = await quart_request.get_json(silent=True) or {}
                    # cross-service: reuse upstream trace_id if passed via header
                    trace_id = quart_request.headers.get("X-Langfuse-Trace-Id") or client.create_trace_id()
                    quart_g._langfuse_trace_context = {"trace_id": trace_id}
                    span = client.start_span(
                        trace_context={"trace_id": trace_id},
                        name=trace_name,
                        input=trace_input,
                    )
                except Exception:
                    _logger.warning("Langfuse trace start failed", exc_info=True)

            try:
                result = await fn(*args, **kwargs)
            except Exception as e:
                if span:
                    try:
                        span.update(level="ERROR", status_message=str(e))
                        span.end()
                    except Exception:
                        pass
                raise

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

        @functools.wraps(fn)
        def sync_wrapper(*args, **kwargs):
            tenant_id = kwargs.get(tenant_id_param) or (args[0] if args else None)
            client = _get_langfuse_client(tenant_id) if tenant_id else None

            span = None
            trace_id = None
            t0 = time.time()

            if client:
                try:
                    trace_id = client.create_trace_id()
                    # share trace context for LLMBundle (same as async_wrapper)
                    try:
                        from quart import g as quart_g
                        quart_g._langfuse_trace_context = {"trace_id": trace_id}
                    except Exception:
                        pass
                    span = client.start_span(
                        trace_context={"trace_id": trace_id},
                        name=trace_name,
                        input={"note": "sync endpoint"},
                    )
                except Exception:
                    _logger.warning("Langfuse trace start failed", exc_info=True)

            try:
                result = fn(*args, **kwargs)
            except Exception as e:
                if span:
                    try:
                        span.update(level="ERROR", status_message=str(e))
                        span.end()
                    except Exception:
                        pass
                raise

            if span:
                try:
                    elapsed_ms = round((time.time() - t0) * 1000, 2)
                    span.update(output={"_elapsed_ms": elapsed_ms})
                    span.end()
                except Exception:
                    _logger.warning("Langfuse trace end failed", exc_info=True)

            return result

        return async_wrapper if is_async else sync_wrapper
    return decorator
