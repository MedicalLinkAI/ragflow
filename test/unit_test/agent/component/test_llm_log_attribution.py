#
#  Copyright 2026 MedLinkAI. All Rights Reserved.
#
#  Tests for agent/component/llm.py _generate_async 日志归因
#
#  背景（LBZH page 21/23 误归因教训）：多 task_executor 共享同一进程日志流，
#  "[LLM] SmartSplitter call" / "[LLM] Extractor call" 不带 doc/task/case
#  时，并发场景下 LLM 调用日志无法归属到真实文档。须与 extractor 侧
#  _build_log_tag 口径对齐。
#
import asyncio
import logging
import os
import sys
import types

# ── Bootstrap: fake heavy packages before importing module under test ──
project_root = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
)
sys.path.insert(0, project_root)


def _fake_pkg(name, path=None):
    mod = types.ModuleType(name)
    if path:
        mod.__path__ = [path]
    sys.modules[name] = mod
    return mod


_fake_pkg("agent", os.path.join(project_root, "agent"))
_fake_pkg("agent.component", os.path.join(project_root, "agent", "component"))
_fake_pkg("common", os.path.join(project_root, "common"))
_fake_pkg("api")
_fake_pkg("api.db")
_fake_pkg("api.db.services")
_fake_pkg("api.db.joint_services")
_fake_pkg("rag", os.path.join(project_root, "rag"))
_fake_pkg("rag.flow", os.path.join(project_root, "rag", "flow"))
_fake_pkg("rag.flow.extractor", os.path.join(project_root, "rag", "flow", "extractor"))

# common.constants
_const_mod = types.ModuleType("common.constants")
_const_mod.LLMType = types.SimpleNamespace(CHAT=types.SimpleNamespace(value="chat"),
                                           IMAGE2TEXT=types.SimpleNamespace(value="image2text"))
sys.modules["common.constants"] = _const_mod

# api.db.services.llm_service / tenant_llm_service
_llm_svc = types.ModuleType("api.db.services.llm_service")
_llm_svc.LLMBundle = type("LLMBundle", (), {})
sys.modules["api.db.services.llm_service"] = _llm_svc
_tls = types.ModuleType("api.db.services.tenant_llm_service")
_tls.TenantLLMService = type("TenantLLMService", (), {})
sys.modules["api.db.services.tenant_llm_service"] = _tls

# api.db.joint_services.tenant_model_service
_tms = types.ModuleType("api.db.joint_services.tenant_model_service")
_tms.get_model_config_by_type_and_name = lambda *a, **k: None
sys.modules["api.db.joint_services.tenant_model_service"] = _tms

# agent.component.base — plain classes (skip real base.py's pandas/agent.settings deps)
_base_mod = types.ModuleType("agent.component.base")


class _ComponentBase:
    component_name = "LLM"


class _ComponentParamBase:
    pass


_base_mod.ComponentBase = _ComponentBase
_base_mod.ComponentParamBase = _ComponentParamBase
sys.modules["agent.component.base"] = _base_mod

# common.connection_utils
_cu = types.ModuleType("common.connection_utils")
_cu.timeout = lambda *a, **k: (lambda f: f)
sys.modules["common.connection_utils"] = _cu

# rag.prompts.generator
_gen_mod = types.ModuleType("rag.prompts.generator")
_gen_mod.tool_call_summary = lambda *a, **k: ""
_gen_mod.message_fit_in = lambda *a, **k: a
_gen_mod.citation_prompt = lambda *a, **k: ""
_gen_mod.structured_output_prompt = lambda *a, **k: ""
sys.modules["rag.prompts.generator"] = _gen_mod

# ── Import module under test ──────────────────────────────────────────
import agent.component.llm as llm_mod  # noqa: E402


class _FakeChatMdl:
    async def async_chat(self, *args, **kwargs):
        return "resp"


def _make_component(component_name, canvas):
    obj = llm_mod.LLM.__new__(llm_mod.LLM)
    obj.component_name = component_name
    obj._canvas = canvas
    obj._param = types.SimpleNamespace(
        llm_id="qwen3.6-27b-fp8___OpenAI-API", gen_conf=lambda: {})
    obj.imgs = []
    obj.chat_mdl = _FakeChatMdl()
    return obj


# ================================================================
# [LLM] <component> call/response 日志必须携带 doc/task/case 归因
# ================================================================

class TestLlmCallLogAttribution:
    DOC_ID = "dbef275894d711f1bd9827cf206dfa2d"
    TASK_ID = "c3fe5538998211f18e23b137b0b8cefc"
    CASE_NAME = "LBZH，男，63岁，胃癌一线(1).pdf"

    def _canvas(self):
        return types.SimpleNamespace(
            _doc_id=self.DOC_ID, task_id=self.TASK_ID, _doc_name=self.CASE_NAME)

    def _logs(self, caplog, component_name, kind):
        return [r.getMessage() for r in caplog.records
                if f"{component_name} {kind}" in r.getMessage()]

    def test_smart_splitter_call_log_carries_attribution(self, caplog):
        comp = _make_component("SmartSplitter", self._canvas())
        with caplog.at_level(logging.INFO):
            asyncio.run(comp._generate_async([{"role": "user", "content": "hi"}]))
        hits = self._logs(caplog, "SmartSplitter", "call")
        assert hits, "SmartSplitter call 日志缺失"
        msg = hits[0]
        assert "llm_id=qwen3.6-27b-fp8___OpenAI-API" in msg, f"既有 llm_id 信息丢失: {msg}"
        assert "doc=dbef2758" in msg, f"call 日志缺 doc 归因: {msg}"
        assert "task=c3fe5538" in msg, f"call 日志缺 task 归因: {msg}"
        assert f"case={self.CASE_NAME}" in msg, f"call 日志缺 case 归因: {msg}"

    def test_extractor_call_log_carries_attribution(self, caplog):
        comp = _make_component("Extractor", self._canvas())
        with caplog.at_level(logging.INFO):
            asyncio.run(comp._generate_async([{"role": "user", "content": "hi"}]))
        hits = self._logs(caplog, "Extractor", "call")
        assert hits, "Extractor call 日志缺失"
        msg = hits[0]
        assert "doc=dbef2758" in msg, f"call 日志缺 doc 归因: {msg}"
        assert "task=c3fe5538" in msg, f"call 日志缺 task 归因: {msg}"
        assert f"case={self.CASE_NAME}" in msg, f"call 日志缺 case 归因: {msg}"

    def test_missing_canvas_attrs_degrade_to_dash(self, caplog):
        """canvas 无归因属性（如非文档处理场景）降级 doc=- task=-。"""
        comp = _make_component("SmartSplitter", types.SimpleNamespace())
        with caplog.at_level(logging.INFO):
            asyncio.run(comp._generate_async([{"role": "user", "content": "hi"}]))
        hits = self._logs(caplog, "SmartSplitter", "call")
        assert hits
        msg = hits[0]
        assert "doc=-" in msg, msg
        assert "task=-" in msg, msg
        assert "case=" not in msg, msg

    def test_response_log_carries_same_attribution(self, caplog):
        """response 行与 call 行同源，须携带相同归因以便并发场景配对。"""
        comp = _make_component("Extractor", self._canvas())
        with caplog.at_level(logging.INFO):
            asyncio.run(comp._generate_async([{"role": "user", "content": "hi"}]))
        hits = self._logs(caplog, "Extractor", "response")
        assert hits, "Extractor response 日志缺失"
        msg = hits[0]
        assert "llm_id=qwen3.6-27b-fp8___OpenAI-API" in msg, f"既有 llm_id 信息丢失: {msg}"
        assert "doc=dbef2758" in msg, f"response 日志缺 doc 归因: {msg}"
        assert "task=c3fe5538" in msg, f"response 日志缺 task 归因: {msg}"
        assert f"case={self.CASE_NAME}" in msg, f"response 日志缺 case 归因: {msg}"


# ================================================================
# 循环导入回归：llm.py 顶层禁止 import rag.flow.extractor.qwen_vl_ocr
# ================================================================
# 实证（容器冷启动复现）：llm.py 顶层该 import 触发 rag/flow/__init__.py
# walk-import → extractor.py 回导 agent.component.llm.LLMParam，此时 llm.py
# 尚未执行完 → ImportError 被 walk 吞掉 → ExtractorParam 未注册 →
# Pipeline 实例化 assert "Can't import ExtractorParam"（2026-08-17 worker 报错）。
# _build_log_tag 必须迁到零依赖模块（common.log_tag），不得经 rag.flow 包获取。

class TestNoCircularImportViaQwenVlOcr:
    def test_llm_module_does_not_import_qwen_vl_ocr(self):
        import re

        llm_path = os.path.join(project_root, "agent", "component", "llm.py")
        with open(llm_path, encoding="utf-8") as f:
            src = f.read()
        # 只匹配真实 import 语句，不命中注释/文档中的模块名提及
        hits = re.findall(
            r"^\s*(?:from|import)\s+rag\.flow\.extractor\.qwen_vl_ocr",
            src, flags=re.MULTILINE)
        assert not hits, (
            "llm.py 顶层 import qwen_vl_ocr 会触发 rag.flow 包 walk-import，"
            "worker 冷启动循环导入导致 ExtractorParam 注册失败")

    def test_build_log_tag_lives_in_common_log_tag(self):
        from common.log_tag import build_log_tag

        canvas = types.SimpleNamespace(
            _doc_id="dbef275894d711f1bd9827cf206dfa2d",
            task_id="c3fe5538998211f18e23b137b0b8cefc",
            _doc_name="case.pdf",
        )
        ext = types.SimpleNamespace(_canvas=canvas)
        tag = build_log_tag(ext, "[LLM] Extractor call")
        assert tag == ("[LLM] Extractor call doc=dbef2758 task=c3fe5538 case=case.pdf"), tag

    def test_build_log_tag_degrades_without_canvas(self):
        from common.log_tag import build_log_tag

        tag = build_log_tag(types.SimpleNamespace(), "[LLM] LLM call")
        assert tag == "[LLM] LLM call doc=- task=-", tag
