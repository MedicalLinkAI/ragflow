#
#  Copyright 2026 MedLinkAI. All Rights Reserved.
#
#  Tests for rag/flow/extractor/qwen30b_ocr.py (process_table / LabReport 路径)
#
#  回归背景（与 qwen_vl_ocr.py 同步修复）：
#    - Step B 从 LaTeX 提取 items 后未做 _detex 归一化，reference_range/unit
#      残留 LaTeX 转义（$<14$、$\mu$mol/L），落库非归一化值，且 Step C
#      坐标匹配空间与图片纯文本不一致
#
import asyncio
import json
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


# rag / rag.flow / rag.flow.extractor: fake packages with real __path__
# (avoids rag/flow/__init__.py's walk-import of every submodule)
_fake_pkg("rag", os.path.join(project_root, "rag"))
_fake_pkg("rag.flow", os.path.join(project_root, "rag", "flow"))
_fake_pkg("rag.flow.extractor", os.path.join(project_root, "rag", "flow", "extractor"))

# rag.flow.extractor.extractor — heavy module; only strip_markdown_json_fence needed
_extractor_stub = types.ModuleType("rag.flow.extractor.extractor")
_extractor_stub.strip_markdown_json_fence = lambda s: s
sys.modules["rag.flow.extractor.extractor"] = _extractor_stub

# api.db.services.file2document_service
for _n in ("api", "api.db", "api.db.services"):
    _fake_pkg(_n)
_fds_mod = types.ModuleType("api.db.services.file2document_service")


class _File2DocumentService:
    @staticmethod
    def get_storage_address(doc_id=None):
        return "bucket", "name"


_fds_mod.File2DocumentService = _File2DocumentService
sys.modules["api.db.services.file2document_service"] = _fds_mod

# common.settings with STORAGE_IMPL
_common_mod = _fake_pkg("common")
_settings_mod = types.ModuleType("common.settings")


class _Storage:
    @staticmethod
    def get(b, n):
        return b"%PDF-FAKE"


_settings_mod.STORAGE_IMPL = _Storage
sys.modules["common.settings"] = _settings_mod
_common_mod.settings = _settings_mod


# fitz fake: renders any page as a fixed-size pixmap
class _FakePixmap:
    width = 1000
    height = 1400

    def tobytes(self, fmt):
        return b"PNGDATA"


class _FakeRect:
    width = 595.0
    height = 842.0


class _FakePage:
    rect = _FakeRect()

    def get_pixmap(self, matrix):
        return _FakePixmap()


class _FakeDoc:
    def __init__(self, n=20):
        self._n = n

    def __len__(self):
        return self._n

    def __getitem__(self, i):
        return _FakePage()

    def close(self):
        pass


_fitz_mod = types.ModuleType("fitz")
_fitz_mod.open = lambda stream=None, filetype=None: _FakeDoc()
_fitz_mod.Matrix = lambda a, b: None
sys.modules["fitz"] = _fitz_mod

# ── Import module under test ──────────────────────────────────────────
import rag.flow.extractor.qwen30b_ocr as q30b  # noqa: E402


# ================================================================
# process_table — Step B 输出必须经 _detex 归一化（与 qwen_vl_ocr 对齐）
# ================================================================

class _FakeExt:
    """Stub extractor component: Step B LLM 返回含 LaTeX 转义的 items。"""

    def __init__(self):
        self._canvas = types.SimpleNamespace(
            get_tenant_id=lambda: "tenant-x", _doc_id="doc-x"
        )
        self._param = types.SimpleNamespace(field_name="lab_result")

    def get_input_elements(self):
        return {"text": {"value": []}}

    def _sys_prompt_and_msg(self, history, args):
        return [{"role": "user", "content": args["text"]}], "SYS"

    async def _generate_async(self, msg):
        # 模拟 LLM 从 LaTeX 表格提取时残留的转义：
        # $<14$（数学模式比较符）、$\mu$mol/L（希腊字母）
        return json.dumps({
            "report_date": None,
            "items": [
                {"name": "肌钙蛋白T", "item_code": "TnT", "value": "5",
                 "unit": "ng/L", "reference_range": "$<14$", "abnormal": False},
                {"name": "肌红蛋白", "item_code": "MYO", "value": "20",
                 "unit": "$\\mu$mol/L", "reference_range": "0-70", "abnormal": False},
            ],
        }, ensure_ascii=False)


def _run_process_table(monkeypatch, coord_calls):
    monkeypatch.setattr(q30b, "resolve_vl_ocr_endpoint",
                        lambda tenant, llm: ("http://fake/v1", "fake-model", "key"))
    monkeypatch.setattr(q30b, "_call_qwen30b_latex_only",
                        lambda img, prompt, tag, cfg, system_msg=None: (
                            "\\begin{tabular}{ccccc}肌钙蛋白T & TnT & 5 \\\\ \\end{tabular}",
                            0.1, "ok"))

    def fake_coord(img_bytes, prompt, tag, endpoint_cfg):
        seg = prompt.split("## 需要定位的检验项目名称\n", 1)[1].split("\n\n", 1)[0]
        names = seg.split("、")
        coord_calls.append(names)
        return [{"text": n, "bbox": [10, 10, 100, 20]} for n in names], 0.1, "ok"

    monkeypatch.setattr(q30b, "_call_qwen30b_to_coord", fake_coord)

    ck = {
        "doc_id": "doc-x",
        "positions": [[0, 0.0, 0.0, 0.0, 0.0]],  # 单页 pn=0
    }
    asyncio.run(q30b.process_table(_FakeExt(), ck, "fake-llm"))
    return ck


class TestProcessTableDetex:
    def test_saved_items_are_detexed(self, monkeypatch):
        """落库 items 的 LaTeX 转义必须归一化为 Unicode（$<14$ → <14）。"""
        ck = _run_process_table(monkeypatch, [])
        saved = json.loads(ck["lab_result"])
        items = saved["items"]
        assert items[0]["reference_range"] == "<14", (
            f"reference_range 残留 LaTeX 转义: {items[0]['reference_range']}"
        )
        assert items[1]["unit"] == "μmol/L", (
            f"unit 残留 LaTeX 转义: {items[1]['unit']}"
        )

    def test_row_positions_still_matched(self, monkeypatch):
        """detex 不影响坐标匹配：两个 item 均定位成功，页码 pn+1=1。"""
        coord_calls = []
        ck = _run_process_table(monkeypatch, coord_calls)
        assert coord_calls == [["肌钙蛋白T", "肌红蛋白"]]
        assert sorted(rp[0] for rp in ck["row_positions"]) == [1, 1]


# ================================================================
# process_table Step A — 幻觉防御（对齐 qwen_vl_parser 分层防御）
# ================================================================

_SPAM_ROW = r"\multicolumn{2}{c}{肌钙蛋白T} & 5 \\"
_SPAM_LATEX = "\n".join(
    [r"\begin{tabular}{cc}", r"项目 & 结果 \\"] + [_SPAM_ROW] * 8 + [r"\end{tabular}"]
)

# 嵌套宏失控：\textup{ 连续嵌套 >=10 层
_LOOP_LATEX = (
    r"\begin{tabular}{cc}" + "\n"
    + r"\textup{" * 12 + r"\textup{\textup{↑}}" + "}" * 12 + r" & 5 \\" + "\n"
    + r"\end{tabular}"
)


def _patch_endpoint(monkeypatch):
    monkeypatch.setattr(q30b, "resolve_vl_ocr_endpoint",
                        lambda tenant, llm: ("http://fake/v1", "fake-model", "key"))


def _patch_coord(monkeypatch):
    monkeypatch.setattr(
        q30b, "_call_qwen30b_to_coord",
        lambda img, prompt, tag, cfg: ([{"text": "肌钙蛋白T", "bbox": [10, 10, 100, 20]}], 0.1, "ok"))


def _run_with_step_a(monkeypatch, step_a_fn):
    _patch_endpoint(monkeypatch)
    _patch_coord(monkeypatch)
    monkeypatch.setattr(q30b, "_call_qwen30b_latex_only", step_a_fn)
    ck = {"doc_id": "doc-x", "positions": [[0, 0.0, 0.0, 0.0, 0.0]]}
    asyncio.run(q30b.process_table(_FakeExt(), ck, "fake-llm"))
    return ck


class TestProcessTableRowSpamDefense:
    def test_row_spam_retry_clean_adopted(self, monkeypatch):
        """行级刷屏：首次脏 → 带 repetition_penalty 重试干净 → 采用重试结果。"""
        calls = []

        def step_a(img, prompt, tag, cfg, system_msg=None, extra_params=None):
            calls.append(extra_params)
            if extra_params and extra_params.get("repetition_penalty"):
                clean = "\n".join([r"\begin{tabular}{cc}", r"肌钙蛋白T & 5 \\", r"\end{tabular}"])
                return clean, 0.1, "ok"
            return _SPAM_LATEX, 0.1, "ok"

        _run_with_step_a(monkeypatch, step_a)
        assert len(calls) == 2, f"行级刷屏应触发重试, calls={calls}"
        assert calls[1].get("repetition_penalty") == 1.2

    def test_row_spam_retry_still_dirty_keeps_collapsed(self, monkeypatch):
        """行级刷屏：重试仍脏 → 采用折叠版（刷屏行只保留 1 次），Step B 输入不含连续重复行。"""
        seen_latex = []

        def step_a(img, prompt, tag, cfg, system_msg=None, extra_params=None):
            return _SPAM_LATEX, 0.1, "ok"

        class _SpyExt(_FakeExt):
            async def _generate_async(self, msg):
                user = next(m["content"] for m in msg if m.get("role") == "user")
                seen_latex.append(user)
                return await super()._generate_async(msg)

        _patch_endpoint(monkeypatch)
        _patch_coord(monkeypatch)
        monkeypatch.setattr(q30b, "_call_qwen30b_latex_only", step_a)
        ck = {"doc_id": "doc-x", "positions": [[0, 0.0, 0.0, 0.0, 0.0]]}
        asyncio.run(q30b.process_table(_SpyExt(), ck, "fake-llm"))
        b_input = "\n".join(seen_latex)
        assert b_input.count(_SPAM_ROW) <= 1, "Step B 输入仍含刷屏行（未折叠）"


class TestProcessTableLoopDefense:
    def test_nested_macro_loop_truncated(self, monkeypatch):
        """嵌套宏失控：重试仍失控 → 截断到循环起点，Step B 输入不含嵌套宏循环。"""
        def step_a(img, prompt, tag, cfg, system_msg=None, extra_params=None):
            return _LOOP_LATEX, 0.1, "ok"

        class _SpyExt(_FakeExt):
            def __init__(self):
                super().__init__()
                self.b_inputs = []

            async def _generate_async(self, msg):
                user = next(m["content"] for m in msg if m.get("role") == "user")
                self.b_inputs.append(user)
                return await super()._generate_async(msg)

        _patch_endpoint(monkeypatch)
        _patch_coord(monkeypatch)
        monkeypatch.setattr(q30b, "_call_qwen30b_latex_only", step_a)
        ext = _SpyExt()
        ck = {"doc_id": "doc-x", "positions": [[0, 0.0, 0.0, 0.0, 0.0]]}
        asyncio.run(q30b.process_table(ext, ck, "fake-llm"))
        b_input = "\n".join(ext.b_inputs)
        assert r"\textup{\textup{" not in b_input, "Step B 输入仍含嵌套宏循环（未截断）"


# ================================================================
# process_text Step 3 — 行级重复防御（复用 qwen_vl_parser._dedup_repeated_blocks）
# ================================================================

# LBZH/XJJA 实证（2025-07-03 入院记录第 9 页）：头部"姓名/性别/年龄"块重复出现一次
# （双栏表单物理印两次），其后全部为互不相同的主诉/现病史等正文。旧实现仅凭
# lines[3:6]==lines[0:3] 即判定 cycle=3 循环，把 45 行截成 3 行，
# 主诉/现病史/姓名全部丢失 → server 端 _write_admission 判空 SKIP 不落库。
_PAGE9_LINES = [
    "姓名：", "性别：女", "年龄：57岁",
    "姓名：", "性别：女", "年龄：57岁",
    "民族：汉族", "婚姻：已婚", "籍贯：河南省新乡市",
    "职业：农民", "身份证号：410725196", "住址：河南省新乡市原阳县官",
    "工作单位：河南省新乡市原阳县官厂", "号", "165号",
    "联系电话：13837", "入院情况：一般", "入院时间：2025-07-03 14:18",
    "病史记录时间：2025-07-03 16:09", "病史陈述者：患者本人", "病史可靠性：可靠",
    "联系人姓名：周小娄", "联系人电话：138373", "联系人地址：河南省新乡市原阳县官厂",
    "联系人与患者关系：", "乡三", "过敏史：无",
    "呼吸内五科第1次入院记录", "主诉：确诊肺腺癌2年余",
    "现病史：2年余前无明显诱因出现发热、咳嗽，就诊于当地医院，完善胸部CT（未见报",
    "告），予以输液治疗（具体用药不详）效差，于2023-06-18就诊于河南省人民医院，查增强",
    "CT（2023-06-20）1.左肺高密度影、双肺多发结节，考虑恶性可能 2.双肺炎症，以左侧为",
    "著 3.纵膈内稍大淋巴结 4.左侧胸膜增厚 5.所示肝内小囊肿，行气管镜检查：接环形径向",
    "超声，于左固有上叶前段支气管、左侧舌叶支气管探及病灶，分别给予盲检，免疫组化结果",
    "示：ALK-D5F3(-)，考虑肺腺癌，于2023-06-26行“培美曲塞+奈达铂”化疗，并予以基因检",
    "测，结果示EGFR基因第21外显子LA858R突变，口服“阿美替尼”，2024.03入院复查胸部CT",
    "评估肿瘤稳定，双肺间质改变，考虑药物相关可能性大，嘱其暂停“阿美替尼”，给予“通",
    "关藤”、“甲泼尼龙琥珀酸钠”激素治疗，辅以解痉平喘、护胃等对症支持治疗好转后出",
    "院，规律口服“伏美替尼”，2025.05.15复查相关指标示进展，于2025.05.15行“培美曲塞",
    "+顺铂”治疗，于2025.06.15行“培美曲塞+顺铂+贝伐珠单抗+信迪利单抗”治疗。现为进一",
    "步治疗，门诊以“肺恶性肿瘤”收入院。自发病以来，食欲正常，睡眠欠佳，大小便正常，",
    "精神欠佳，体重下降。",
    "既往史：有慢性乙型病毒性肝炎病史30年，未规律治疗。无高血压、心脏疾病病史，",
]


class TestTextCycleDefense:
    """与 qwen_vl_parser._dedup_repeated_blocks 同款语义（轻量副本，须保持同步）"""

    def test_form_header_double_block_keeps_tail(self):
        """LBZH/XJJA 实证：双栏表头物理印两次，仅折叠重复块，主诉/现病史必须保留。"""
        result, rep = q30b._dedup_repeated_blocks(list(_PAGE9_LINES))
        header = _PAGE9_LINES[0:3]
        assert result == header + _PAGE9_LINES[6:], "双表头应折叠为一次，尾部唯一内容不得丢失"
        assert rep == (3, 14, 43)
        assert any("主诉" in l for l in result), "主诉被截断丢失"
        assert any("现病史" in l for l in result), "现病史被截断丢失"

    def test_real_loop_collapsed_to_first_block(self):
        """真实幻觉：同一 3 行块连续重复 15 次 → 折叠为首次出现。"""
        block = ["住院记录表头", "项目 & 结果", "第 1 页"]
        out, rep = q30b._dedup_repeated_blocks(block * 15)
        assert out == block
        assert rep == (3, 15, 45)

    def test_loop_followed_by_tail_keeps_tail(self):
        """循环后接正常内容：只折叠循环部分，尾部必须保留。"""
        block = ["重复行A", "重复行B", "重复行C"]
        tail = [f"正常内容第{i}行" for i in range(8)]
        out, rep = q30b._dedup_repeated_blocks(block * 5 + tail)
        assert out == block + tail

    def test_mid_run_collapsed(self):
        """任意位置单行刷屏（非从头开始）：折叠为一行，前后内容保留。"""
        head = [f"line{i}" for i in range(10)]
        tail = [f"tail{i}" for i in range(10)]
        out, rep = q30b._dedup_repeated_blocks(head + ["病理诊断："] * 30 + tail)
        assert out == head + ["病理诊断："] + tail
        assert rep == (1, 30, 50)

    def test_run_below_threshold_untouched(self):
        """连续重复 <5 次不构成刷屏，原样保留。"""
        lines = [f"line{i}" for i in range(20)] + ["dup"] * 4
        out, rep = q30b._dedup_repeated_blocks(lines)
        assert rep is None
        assert out == lines

    def test_short_page_untouched(self):
        """小页（<=20 行）不进入检测，原样返回。"""
        lines = ["a", "b", "c"] * 6  # 18 行，即便是真循环也不处理
        out, rep = q30b._dedup_repeated_blocks(lines)
        assert out == lines
        assert rep is None
