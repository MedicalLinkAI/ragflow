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
#  MedLinkAI 扩展：知识库 embd_id 直更接口
#
#  背景：标准 PUT /api/v1/datasets/<id> 在 chunk_num > 0 时禁止修改
#  embedding_model（"When chunk_num (N) > 0, embedding_model must remain ..."）。
#  MedLinkAI Pipeline 模型配置页需要切换 Tokenizer 向量模型，
#  此接口绕过该限制，直接更新 knowledgebase 表。等价 SQL：
#    SELECT id FROM tenant_llm WHERE llm_name = :embd_id;
#    UPDATE knowledgebase SET embd_id = :embd_id, tenant_embd_id = :id WHERE id = :dataset_id;
#
import logging

from api.apps import login_required
from api.db.services.knowledgebase_service import KnowledgebaseService
from api.db.services.tenant_llm_service import TenantLLMService
from api.utils.api_utils import (
    add_tenant_id_to_kwargs,
    get_error_argument_result,
    get_error_data_result,
    get_request_json,
    get_result,
)


@manager.route("/datasets/<dataset_id>/embd_id", methods=["PUT"])  # noqa: F821
@login_required
@add_tenant_id_to_kwargs
async def update_kb_embd_id(tenant_id, dataset_id):
    """
    Update knowledgebase embd_id directly (bypass chunk_num > 0 restriction).
    ---
    tags:
      - Datasets
    security:
      - ApiKeyAuth: []
    parameters:
      - in: path
        name: dataset_id
        type: string
        required: true
        description: ID of the dataset to update.
      - in: header
        name: Authorization
        type: string
        required: true
        description: Bearer token for authentication.
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - embd_id
          properties:
            embd_id:
              type: string
              description: New embedding model name (tenant_llm.llm_name).
    responses:
      200:
        description: Successful operation.
        schema:
          type: object
    """
    req = await get_request_json()
    embd_id = (req or {}).get("embd_id", "").strip()
    if not embd_id:
        return get_error_argument_result("embd_id is required")

    try:
        ok, kb = KnowledgebaseService.get_by_id(dataset_id)
        if not ok or not kb:
            return get_error_data_result(message=f"Dataset not found: {dataset_id}")

        # Step 1: SELECT id FROM tenant_llm WHERE llm_name = :embd_id
        rows = TenantLLMService.query(llm_name=embd_id, model_type="embedding")
        if not rows and "@" in embd_id:
            # 兼容 model@provider 格式
            rows = TenantLLMService.query(llm_name=embd_id.rsplit("@", 1)[0], model_type="embedding")
        if not rows:
            rows = TenantLLMService.query(llm_name=embd_id)
        if not rows:
            return get_error_data_result(message=f"Embedding model not found in tenant_llm: {embd_id}")
        # 优先取当前租户的记录
        row = next((r for r in rows if r.tenant_id == tenant_id), rows[0])

        # Step 2: UPDATE knowledgebase SET embd_id = ..., tenant_embd_id = ... WHERE id = ...
        KnowledgebaseService.update_by_id(dataset_id, {"embd_id": embd_id, "tenant_embd_id": row.id})
        logging.info(
            "kb embd_id updated directly: dataset_id=%s, embd_id=%s -> %s, tenant_embd_id=%s",
            dataset_id, kb.embd_id, embd_id, row.id,
        )
        return get_result(data={
            "dataset_id": dataset_id,
            "old_embd_id": kb.embd_id,
            "embd_id": embd_id,
            "tenant_embd_id": row.id,
        })
    except Exception as e:
        logging.exception(e)
        return get_error_data_result(message="Internal server error")
