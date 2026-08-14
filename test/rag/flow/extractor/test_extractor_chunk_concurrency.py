#
#  Copyright 2026 MedLinkAI. All Rights Reserved.
#
#  Tests for rag/flow/extractor/extractor.py chunk-level concurrency.
#
#  背景：QwenVLParser 页级并发落地后，Extractor 的逐 chunk 串行循环成为新瓶颈
#  （每个 chunk 要等 1 次 LLM 提取 + 若干次坐标调用全部返回才轮到下一个）。
#  本组测试验证：
#    - chunk 并发执行（限流常量 CHUNK_CONCURRENCY）
#    - 输出顺序与输入一致（完成顺序可以乱）
#    - 并发上限不被突破
#    - chunk 异常向上传播（与串行行为一致）
#
import asyncio
import importlib.util
import os
import sys
import time
import types

import pytest

# ── Bootstrap: stub heavy dependencies before importing module under test ──
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


_fake_pkg("rag", os.path.join(project_root, "rag"))
_fake_pkg("rag.flow", os.path.join(project_root, "rag", "flow"))
_fake_pkg("rag.flow.extractor", os.path.join(project_root, "rag", "flow", "extractor"))

# xxhash (not installed in bare test env; only used in TOC/id hashing paths)
try:
    import xxhash  # noqa: F401
except ImportError:
    _xx_mod = types.ModuleType("xxhash")

    class _XXH64:
        def __init__(self, data=b""):
            import hashlib

            self._h = hashlib.sha256(data).hexdigest()

        def hexdigest(self):
            return self._h[:16]

    _xx_mod.xxh64 = _XXH64
    sys.modules["xxhash"] = _xx_mod

# agent.component.llm
_fake_pkg("agent")
_fake_pkg("agent.component")
_llm_mod = types.ModuleType("agent.component.llm")


class LLMParam:
    def check(self):
        pass

    def check_empty(self, *a, **kw):
        pass

    def gen_conf(self):
        return {}


class LLM:
    pass


_llm_mod.LLMParam = LLMParam
_llm_mod.LLM = LLM
sys.modules["agent.component.llm"] = _llm_mod

# rag.flow.base
_base_mod = types.ModuleType("rag.flow.base")


class ProcessParamBase:
    pass


class ProcessBase:
    pass


_base_mod.ProcessBase = ProcessBase
_base_mod.ProcessParamBase = ProcessParamBase
sys.modules["rag.flow.base"] = _base_mod

# rag.prompts.generator
_fake_pkg("rag.prompts")
_gen_mod = types.ModuleType("rag.prompts.generator")
_gen_mod.run_toc_from_text = None
sys.modules["rag.prompts.generator"] = _gen_mod

# rag.utils.base64_image
_fake_pkg("rag.utils")
_b64_mod = types.ModuleType("rag.utils.base64_image")
_b64_mod.id2image = lambda *a, **kw: None
sys.modules["rag.utils.base64_image"] = _b64_mod

# common.settings
_common_mod = _fake_pkg("common")
_settings_mod = types.ModuleType("common.settings")
_settings_mod.STORAGE_IMPL = None
sys.modules["common.settings"] = _settings_mod
_common_mod.settings = _settings_mod

# qwen30b_ocr / qwen_vl_ocr: real logic not under test here
for _name in ("qwen30b_ocr", "qwen_vl_ocr"):
    _m = types.ModuleType(f"rag.flow.extractor.{_name}")

    async def _noop_process(ext, ck, llm_name):
        pass

    _m.process_table = _noop_process
    _m.process_text = _noop_process
    sys.modules[f"rag.flow.extractor.{_name}"] = _m

# Import the module under test directly by path (bypasses rag/flow/__init__ walk-import)
_mod_path = os.path.join(project_root, "rag", "flow", "extractor", "extractor.py")
_spec = importlib.util.spec_from_file_location("rag.flow.extractor.extractor", _mod_path)
extractor_module = importlib.util.module_from_spec(_spec)
sys.modules["rag.flow.extractor.extractor"] = extractor_module
_spec.loader.exec_module(extractor_module)

# 恢复 sys.modules 中被 stub 污染的模块，避免影响同目录其他测试文件
# （test_qwen_vl_ocr.py / test_qwen30b_ocr.py 会真实导入这些模块）
for _n in ("rag.flow.extractor.qwen_vl_ocr", "rag.flow.extractor.qwen30b_ocr",
           "rag", "rag.flow", "rag.flow.extractor",
           "agent", "agent.component", "agent.component.llm",
           "rag.flow.base", "rag.prompts", "rag.prompts.generator",
           "rag.utils", "rag.utils.base64_image", "common", "common.settings"):
    sys.modules.pop(_n, None)
sys.modules["rag.flow.extractor.extractor"] = extractor_module

Extractor = extractor_module.Extractor


# ── Test helpers ──
def _make_extractor(chunks, parse_method="", field_name="extracted_data_tks"):
    """Build a bare Extractor instance with just enough plumbing for _invoke."""
    ext = Extractor.__new__(Extractor)

    class _Param:
        pass

    ext._param = _Param()
    ext._param.field_name = field_name

    canvas = types.SimpleNamespace(components={}, _doc_id="doc-1")
    if parse_method:
        canvas.components["p0"] = {
            "obj": types.SimpleNamespace(
                component_name="Parser",
                _param=types.SimpleNamespace(setups={"pdf": {"parse_method": parse_method}}),
            )
        }
    ext._canvas = canvas

    ext._outputs = {}
    ext.set_output = lambda k, v: ext._outputs.__setitem__(k, v)
    ext.callback_calls = []
    ext.callback = lambda prog, msg="": ext.callback_calls.append((prog, msg))
    ext.get_input_elements = lambda: {"chunks_in": {"value": chunks}}
    ext._sys_prompt_and_msg = lambda history, args: ([{"role": "user", "content": args.get("text", "")}], "SYS")

    async def _fake_generate(msg):
        return "{}"

    ext._generate_async = _fake_generate
    return ext


# ── Tests ──
class TestExtractorChunkConcurrency:
    def test_chunks_processed_concurrently(self):
        """多 chunk 必须重叠执行；串行实现墙钟 = sum(delay)，并发后应显著更短。"""
        n, delay = 6, 0.3
        chunks = [{"text": f"t{i}"} for i in range(n)]
        ext = _make_extractor(chunks, parse_method="paddleocr")

        ocr_mod = extractor_module.qwen30b_ocr
        current = 0
        peak = 0

        async def fake_process_text(ext_, ck, llm_name):
            nonlocal current, peak
            current += 1
            peak = max(peak, current)
            await asyncio.sleep(delay)
            current -= 1

        orig = ocr_mod.process_text
        ocr_mod.process_text = fake_process_text
        try:
            t0 = time.monotonic()
            asyncio.run(ext._invoke())
            elapsed = time.monotonic() - t0
        finally:
            ocr_mod.process_text = orig

        assert peak >= 2, f"chunks ran serially, peak concurrency={peak}"
        assert elapsed < n * delay * 0.8, f"wall time {elapsed:.2f}s not concurrent (serial={n * delay:.1f}s)"

    def test_concurrency_capped_at_chunk_concurrency(self):
        """并发峰值不得超过 CHUNK_CONCURRENCY。"""
        n = 14
        chunks = [{"text": f"t{i}"} for i in range(n)]
        ext = _make_extractor(chunks, parse_method="paddleocr")

        ocr_mod = extractor_module.qwen30b_ocr
        current = 0
        peak = 0

        async def fake_process_text(ext_, ck, llm_name):
            nonlocal current, peak
            current += 1
            peak = max(peak, current)
            await asyncio.sleep(0.05)
            current -= 1

        orig = ocr_mod.process_text
        ocr_mod.process_text = fake_process_text
        try:
            asyncio.run(ext._invoke())
        finally:
            ocr_mod.process_text = orig

        assert peak <= Extractor.CHUNK_CONCURRENCY
        assert peak >= 2

    def test_output_order_preserved_despite_reversed_completion(self):
        """完成顺序颠倒时，输出 chunks 顺序和字段仍与输入一致。"""
        delays = [0.4, 0.2, 0.05, 0.3]
        chunks = [{"text": f"t{i}"} for i in range(len(delays))]
        ext = _make_extractor(chunks, parse_method="paddleocr")

        ocr_mod = extractor_module.qwen30b_ocr

        async def fake_process_text(ext_, ck, llm_name):
            idx = int(ck["text"][1:])
            await asyncio.sleep(delays[idx])
            ck[ext_._param.field_name] = f'"R{idx}"'

        orig = ocr_mod.process_text
        ocr_mod.process_text = fake_process_text
        try:
            asyncio.run(ext._invoke())
        finally:
            ocr_mod.process_text = orig

        out = ext._outputs["chunks"]
        assert len(out) == len(chunks)
        # 原对象原地更新，顺序不变
        assert [c["text"] for c in out] == ["t0", "t1", "t2", "t3"]
        assert [c["extracted_data_tks"] for c in out] == ['"R0"', '"R1"', '"R2"', '"R3"']

    def test_chunk_exception_propagates(self):
        """任一 chunk 处理抛异常时，_invoke 向上传播（与串行版一致）。"""
        chunks = [{"text": f"t{i}"} for i in range(4)]
        ext = _make_extractor(chunks, parse_method="paddleocr")

        ocr_mod = extractor_module.qwen30b_ocr

        async def fake_process_text(ext_, ck, llm_name):
            if ck["text"] == "t2":
                raise ConnectionError("vl endpoint down")
            await asyncio.sleep(0.05)

        orig = ocr_mod.process_text
        ocr_mod.process_text = fake_process_text
        try:
            with pytest.raises(ConnectionError):
                asyncio.run(ext._invoke())
        finally:
            ocr_mod.process_text = orig

    def test_qwenvl_path_runs_process_text_concurrently(self):
        """QwenVL 路径下 qwen_vl_ocr.process_text 也必须并发执行。"""
        n, delay = 5, 0.25
        chunks = [{"text": f"t{i}", "classify_result_tks": '{"type": "ProgressNote"}'} for i in range(n)]
        ext = _make_extractor(chunks, parse_method="Qwen/Qwen3-VL-30B-A3B-Instruct-FP8")

        vl_mod = extractor_module.qwen_vl_ocr
        current = 0
        peak = 0

        async def fake_process_text(ext_, ck, llm_name):
            nonlocal current, peak
            current += 1
            peak = max(peak, current)
            await asyncio.sleep(delay)
            current -= 1

        orig = vl_mod.process_text
        vl_mod.process_text = fake_process_text
        try:
            t0 = time.monotonic()
            asyncio.run(ext._invoke())
            elapsed = time.monotonic() - t0
        finally:
            vl_mod.process_text = orig

        assert peak >= 2, f"process_text ran serially, peak={peak}"
        assert elapsed < n * delay * 0.8
