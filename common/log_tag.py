#
#  Copyright 2026 MedLinkAI. All Rights Reserved.
#
#  日志归因 TAG 构造（零依赖模块）。
#
#  背景：多 task_executor 共享同一进程日志流，VLM/LLM 调用日志若不带
#  doc/task 标识，并发时超时/失败无法归属真实文档（曾误把其他大文档的
#  coord 超时归到 LBZH）。doc/task 取前 8 位与 [Trace] 日志口径对齐。
#
#  独立成模块的原因：agent/component/llm.py 位于 agent.component 包
#  walk-import 链上，若从 rag.flow.extractor.qwen_vl_ocr 导入会触发
#  rag/flow/__init__.py 全组件 walk-import，与 extractor.py 回导
#  LLMParam 形成循环导入，导致 ExtractorParam 等组件注册失败
#  （2026-08-17 worker "Can't import ExtractorParam" 事故）。
#  本模块只依赖标准库，任何调用方均可安全顶层导入。
#


def build_log_tag(ext, base_tag: str) -> str:
    """构造带归因信息的日志 TAG："<base> doc=xxxxxxxx task=xxxxxxxx case=<病案名>"。

    Args:
        ext: 持有 _canvas 的组件实例（extractor/parser/agent component），
             也接受直接伪造 _canvas 的对象（用于测试与 naive 路径降级）。
        base_tag: 日志前缀，如 "[qwen30b-text]"、"[LLM] Extractor call"。

    Returns:
        str: 归因 TAG；doc/task 缺失降级为 "-"，doc_name 为 "unknown" 不输出 case。
    """
    canvas = getattr(ext, "_canvas", None)
    doc_id = getattr(canvas, "_doc_id", None) or ""
    task_id = getattr(canvas, "task_id", None) or ""
    doc_name = getattr(canvas, "_doc_name", None) or ""
    tag = f"{base_tag} doc={doc_id[:8] if doc_id else '-'} task={task_id[:8] if task_id else '-'}"
    if doc_name and doc_name != "unknown":
        tag += f" case={doc_name}"
    return tag
