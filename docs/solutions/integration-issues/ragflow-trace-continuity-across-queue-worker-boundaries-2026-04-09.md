---
title: RAGflow trace continuity across queue and worker boundaries
date: 2026-04-09
category: integration-issues
module: ragflow observability
problem_type: integration_issue
component: tooling
symptoms:
  - Langfuse traces stopped at async queue boundaries and did not reconnect to worker execution.
  - Canvas DataFlow requests lost trace context when execution crossed thread_pool_exec().
  - Downstream pipeline and invoke calls could miss compatibility trace headers.
root_cause: thread_violation
resolution_type: code_fix
severity: medium
tags: [langfuse, trace-continuity, queue-propagation, thread-pool, observability]
---

# RAGflow trace continuity across queue and worker boundaries

## Problem

RAGflow's new observability work needed end-to-end trace continuity from API entrypoints to queued worker execution and downstream pipeline calls. The fix had to stay strictly additive: improve trace propagation without changing original business logic, rollback behavior, or failure semantics.

## Symptoms

- API spans and worker execution showed up as disconnected trace segments.
- Canvas DataFlow requests could lose trace context when the request crossed `thread_pool_exec(queue_dataflow, ...)`.
- Downstream calls from worker-side pipeline/invoke paths could miss compatibility headers needed by existing trace consumers.

## What Didn't Work

- Treating the problem as a business-logic hardening task and adding rollback or compensation behavior to `queue_dataflow()`, SDK parse, or rerun paths. That crossed the agreed boundary and risked changing historical RAGflow semantics.
- Relying only on ambient request context. That was not sufficient once execution moved across queue and thread-pool boundaries.

## Solution

Keep the patch observability-only and propagate trace context explicitly at each execution boundary:

1. Normalize, bind, and clear trace context in `api/utils/langfuse_trace.py`.
2. Attach queue-only trace metadata in `api/db/services/task_service.py` without polluting DB task payloads.
3. Capture `trace_payload` before `canvas_app.py` crosses `thread_pool_exec(...)`, then pass it explicitly into `queue_dataflow(...)`.
4. Restore queue trace context in `rag/svr/task_executor.py` and emit outbound compatibility headers for downstream pipeline execution.
5. Merge custom and static outbound headers safely in `agent/component/invoke.py`.
6. Reuse the shared trace helper in `api/db/services/tenant_llm_service.py` instead of ad hoc request-context access.

Representative boundary handoff:

```python
# api/apps/canvas_app.py
trace_payload = build_queue_trace_payload()
ok, error_message = await thread_pool_exec(
    queue_dataflow,
    user_id,
    req["id"],
    task_id,
    CANVAS_DEBUG_DOC_ID,
    files[0],
    0,
    trace_payload=trace_payload,
)
```

Queue payload isolation:

```python
# api/db/services/task_service.py
queue_task = _copy_task_for_queue(task, trace_payload or build_queue_trace_payload())
queue_task["kb_id"] = DocumentService.get_knowledgebase_id(doc_id)
queue_task["tenant_id"] = tenant_id
queue_task["dataflow_id"] = flow_id
queue_task["file"] = file
```

Worker restore:

```python
# rag/svr/task_executor.py
if task.get("root_trace_id") or task.get("root_traceparent"):
    bind_trace_context(
        {
            "trace_id": task.get("root_trace_id"),
            "traceparent": task.get("root_traceparent"),
            "source": task.get("trace_source", "queue"),
        }
    )
```

## Why This Works

The fix targets only observability boundaries:

- **Request boundary**: route spans capture trace context once.
- **Queue boundary**: queue messages carry trace metadata without changing persisted task rows.
- **Thread boundary**: explicit `trace_payload` avoids relying on `contextvars` crossing a thread pool.
- **Worker boundary**: workers restore the original trace context before downstream execution.
- **Outbound boundary**: invoke/pipeline calls receive consistent trace headers, including compatibility shims.

Because the patch no longer adds rollback or compensation logic, it improves observability without altering historical RAGflow business behavior.

## Prevention

- For any new async, queue, or thread-pool hop, decide trace propagation at the handoff point instead of assuming ambient context survives.
- Keep observability data queue-only unless the business model explicitly requires persistence.
- Treat scope discipline as part of the fix: observability patches should not quietly rewrite business failure semantics.
- Preserve focused tests for:
  - trace normalization and header building
  - queue payload isolation
  - queue-to-worker trace restoration
  - thread-pool handoff coverage for Canvas DataFlow

## Related Issues

- `docs/administrator/tracing.mdx` documents Langfuse setup, but not this queue/worker continuity pattern.
- `docs/references/http_api_reference.md` documents trace-facing APIs and is the closest existing reference surface.
