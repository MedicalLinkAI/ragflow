# qwen3-vl OCR 模型端点动态解析
# 端点与密钥从 tenant_llm 表按 llm_name（即 DSL 中 Parser 的 parse_method 值）查询，
# 与 RAGFlow 模型管理注册信息保持一致，不依赖环境变量。

import logging


def resolve_vl_ocr_endpoint(tenant_id: str, llm_name: str) -> tuple:
    """按 tenant_llm 表注册信息解析 OCR 视觉模型的调用端点。

    Args:
        tenant_id: 当前 canvas 所属租户 ID
        llm_name: 模型注册名（DSL Parser 组件的 parse_method 值）

    Returns:
        tuple: (endpoint, model, api_key)
            endpoint: 完整 chat completions URL（api_base + /chat/completions）
            model: OpenAI 协议 payload 中的 model 字段（去掉 ___厂商 后缀）
            api_key: 注册的 API Key（未配置时为空字符串）

    Raises:
        LookupError: tenant_llm 中未找到该模型或未配置 api_base
    """
    from api.db.services.tenant_llm_service import TenantLLMService

    cfg = TenantLLMService.get_api_key(tenant_id, llm_name)
    if not cfg or not getattr(cfg, "api_base", None):
        raise LookupError(
            f"[vl-ocr-endpoint] llm_name={llm_name} not found in tenant_llm "
            f"(tenant={tenant_id}) or api_base empty, please register the model in RAGFlow"
        )
    model = llm_name.split("___")[0]
    api_base = str(cfg.api_base).rstrip("/")
    endpoint = api_base if api_base.endswith("/chat/completions") \
        else api_base + "/chat/completions"
    logging.info(
        f"[vl-ocr-endpoint] resolved from tenant_llm: tenant={tenant_id}, "
        f"llm_name={llm_name}, endpoint={endpoint}, model={model}"
    )
    return endpoint, model, getattr(cfg, "api_key", "") or ""
