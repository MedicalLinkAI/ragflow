"""
RAGFlow 独立验证测试套件

本测试套件用于在 RAGFlow 侧独立验证 RAG 核心能力：
1. 文档解析能力验证
2. Chunk 分块质量验证
3. 语义检索能力验证
4. Embedding 质量验证

使用方式：
    # 在 RAGFlow 项目根目录运行
    cd /path/to/ragflow
    python test/test_noeticai_rag_capabilities.py

    # 或者使用 pytest
    pytest test/test_noeticai_rag_capabilities.py -v
"""

import os
import sys
import json
import asyncio
import requests
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from datetime import datetime

# ============================================================================
# 配置
# ============================================================================

# RAGFlow API 配置
RAGFLOW_API_URL = os.getenv("RAGFLOW_API_URL", "http://localhost:9380")
RAGFLOW_API_KEY = os.getenv("RAGFLOW_API_KEY", "")

# 测试知识库ID
TEST_KB_ID = os.getenv("TEST_KB_ID", "e20b9926fcea11f099d72a5fbb884ed2")

# API Headers
def get_headers():
    return {
        "Authorization": f"Bearer {RAGFLOW_API_KEY}",
        "Content-Type": "application/json"
    }


# ============================================================================
# 测试用例定义
# ============================================================================

@dataclass
class RAGTestCase:
    """RAG 能力测试用例"""
    id: str
    category: str
    name: str
    query: str
    expected_keywords: List[str]
    min_results: int = 1
    min_similarity: float = 0.3
    description: str = ""


# 完整测试用例集 (60个)
RAG_TEST_CASES: List[RAGTestCase] = [
    # ========== 1. 信用等级定义 (15个) ==========
    RAGTestCase(
        id="CRD001", category="信用等级定义",
        name="AAA级定义",
        query="AAA级信用评级的定义是什么",
        expected_keywords=["AAA", "偿还债务", "极强", "违约风险极低"]
    ),
    RAGTestCase(
        id="CRD002", category="信用等级定义",
        name="AA级定义",
        query="AA级信用评级代表什么含义",
        expected_keywords=["AA", "偿还债务", "很强", "违约风险很低"]
    ),
    RAGTestCase(
        id="CRD003", category="信用等级定义",
        name="A级定义",
        query="A级信用评级的含义",
        expected_keywords=["A", "偿还债务", "较强"]
    ),
    RAGTestCase(
        id="CRD004", category="信用等级定义",
        name="BBB级定义",
        query="BBB级信用评级是什么意思",
        expected_keywords=["BBB", "偿还债务", "一般"]
    ),
    RAGTestCase(
        id="CRD005", category="信用等级定义",
        name="BB级定义",
        query="BB级信用评级的风险",
        expected_keywords=["BB", "偿还债务", "较弱"]
    ),
    RAGTestCase(
        id="CRD006", category="信用等级定义",
        name="B级定义",
        query="B级信用评级代表的风险程度",
        expected_keywords=["B", "依赖", "违约风险很高"]
    ),
    RAGTestCase(
        id="CRD007", category="信用等级定义",
        name="CCC级定义",
        query="CCC级信用评级的含义",
        expected_keywords=["CCC", "极度依赖", "违约风险极高"]
    ),
    RAGTestCase(
        id="CRD008", category="信用等级定义",
        name="CC级定义",
        query="CC级信用评级说明什么",
        expected_keywords=["CC", "基本不能偿还", "违约"]
    ),
    RAGTestCase(
        id="CRD009", category="信用等级定义",
        name="C级定义",
        query="C级信用评级的意义",
        expected_keywords=["C", "不能偿还"]
    ),
    RAGTestCase(
        id="CRD010", category="信用等级定义",
        name="等级微调符号",
        query="信用等级加号减号的含义",
        expected_keywords=["＋", "－", "微调"]
    ),
    RAGTestCase(
        id="CRD011", category="信用等级定义",
        name="担保公司AAA",
        query="担保公司AAA级信用定义",
        expected_keywords=["担保公司", "AAA", "代偿义务"]
    ),
    RAGTestCase(
        id="CRD012", category="信用等级定义",
        name="影子评级",
        query="什么是影子评级",
        expected_keywords=["影子评级", "结构化产品"]
    ),
    RAGTestCase(
        id="CRD013", category="信用等级定义",
        name="BCA个体评估",
        query="个体信用评估BCA的定义",
        expected_keywords=["BCA", "个体信用评估"]
    ),
    RAGTestCase(
        id="CRD014", category="信用等级定义",
        name="全球人民币序列",
        query="全球人民币序列信用等级符号",
        expected_keywords=["全球人民币", "AAAgr"]
    ),
    RAGTestCase(
        id="CRD015", category="信用等级定义",
        name="科技创新企业等级",
        query="科技创新企业信用等级符号AAAsti",
        expected_keywords=["AAAsti", "科技创新"]
    ),

    # ========== 2. 科技创新企业评级 (15个) ==========
    RAGTestCase(
        id="STI001", category="科技创新企业",
        name="评估框架",
        query="科技创新企业评级的评估框架",
        expected_keywords=["科技创新竞争力", "财务风险"]
    ),
    RAGTestCase(
        id="STI002", category="科技创新企业",
        name="科技创新能力权重",
        query="科技创新能力评估权重是多少",
        expected_keywords=["科技创新能力", "40%"]
    ),
    RAGTestCase(
        id="STI003", category="科技创新企业",
        name="研发实力评估",
        query="研发实力如何评估",
        expected_keywords=["研发投入", "研发人员"]
    ),
    RAGTestCase(
        id="STI004", category="科技创新企业",
        name="科技创新成果转化",
        query="科技创新成果转化评估方法",
        expected_keywords=["成果转化", "专利"]
    ),
    RAGTestCase(
        id="STI005", category="科技创新企业",
        name="企业经营实力",
        query="科技创新企业经营实力评估",
        expected_keywords=["经营实力", "竞争实力", "成长质量"]
    ),
    RAGTestCase(
        id="STI006", category="科技创新企业",
        name="竞争实力权重",
        query="竞争实力在评估中的权重",
        expected_keywords=["竞争实力", "40%"]
    ),
    RAGTestCase(
        id="STI007", category="科技创新企业",
        name="成长质量评估",
        query="企业成长质量如何衡量",
        expected_keywords=["成长质量", "收入增速"]
    ),
    RAGTestCase(
        id="STI008", category="科技创新企业",
        name="资本实力评估",
        query="资本实力对评级的影响",
        expected_keywords=["资本实力", "所有者权益"]
    ),
    RAGTestCase(
        id="STI009", category="科技创新企业",
        name="战略发展评估",
        query="企业战略发展评估指标",
        expected_keywords=["战略发展", "25%"]
    ),
    RAGTestCase(
        id="STI010", category="科技创新企业",
        name="产业影响力",
        query="产业及社会影响力评估",
        expected_keywords=["产业", "社会影响力", "35%"]
    ),
    RAGTestCase(
        id="STI011", category="科技创新企业",
        name="科技创新价值",
        query="科技创新价值评估权重",
        expected_keywords=["科技创新价值", "30%"]
    ),
    RAGTestCase(
        id="STI012", category="科技创新企业",
        name="EBIT利润率",
        query="EBIT利润率在科技企业评级中的作用",
        expected_keywords=["EBIT", "利润率"]
    ),
    RAGTestCase(
        id="STI013", category="科技创新企业",
        name="总资本化比率",
        query="总资本化比率反映什么",
        expected_keywords=["总资本化比率", "财务政策"]
    ),
    RAGTestCase(
        id="STI014", category="科技创新企业",
        name="ESG因素",
        query="ESG因素对科技企业评级的影响",
        expected_keywords=["ESG", "环境", "社会", "治理"]
    ),
    RAGTestCase(
        id="STI015", category="科技创新企业",
        name="外部支持",
        query="外部支持对企业评级的影响",
        expected_keywords=["外部支持", "股东", "政府"]
    ),

    # ========== 3. 电子行业评级 (15个) ==========
    RAGTestCase(
        id="ELE001", category="电子行业",
        name="评级框架",
        query="电子行业企业信用评级考虑哪些因素",
        expected_keywords=["业务风险", "财务风险"]
    ),
    RAGTestCase(
        id="ELE002", category="电子行业",
        name="行业风险特点",
        query="电子行业的风险特点",
        expected_keywords=["市场竞争", "产能过剩"]
    ),
    RAGTestCase(
        id="ELE003", category="电子行业",
        name="运营实力评估",
        query="电子企业运营实力评估指标",
        expected_keywords=["营业总收入", "市场地位"]
    ),
    RAGTestCase(
        id="ELE004", category="电子行业",
        name="产品多元化",
        query="产品多元化对电子企业评级的影响",
        expected_keywords=["产品多元化", "产业链", "30%"]
    ),
    RAGTestCase(
        id="ELE005", category="电子行业",
        name="营运能力",
        query="电子企业营运能力评估",
        expected_keywords=["营运能力", "20%"]
    ),
    RAGTestCase(
        id="ELE006", category="电子行业",
        name="财务风险指标",
        query="电子企业财务风险评估指标",
        expected_keywords=["盈利能力", "资本结构", "偿债能力"]
    ),
    RAGTestCase(
        id="ELE007", category="电子行业",
        name="EBITDA保障倍数",
        query="EBITDA利息保障倍数的意义",
        expected_keywords=["EBITDA", "利息", "保障倍数"]
    ),
    RAGTestCase(
        id="ELE008", category="电子行业",
        name="FFO债务覆盖",
        query="FFO总债务比率的含义",
        expected_keywords=["FFO", "债务"]
    ),
    RAGTestCase(
        id="ELE009", category="电子行业",
        name="流动性评估",
        query="电子企业流动性风险评估",
        expected_keywords=["流动性", "现金", "短期"]
    ),
    RAGTestCase(
        id="ELE010", category="电子行业",
        name="政策影响",
        query="产业政策对电子行业的影响",
        expected_keywords=["政策", "补贴"]
    ),
    RAGTestCase(
        id="ELE011", category="电子行业",
        name="国际环境",
        query="国际环境对电子企业的影响",
        expected_keywords=["国际", "竞争", "技术"]
    ),
    RAGTestCase(
        id="ELE012", category="电子行业",
        name="准入壁垒",
        query="电子行业准入壁垒",
        expected_keywords=["准入壁垒", "技术", "资金"]
    ),
    RAGTestCase(
        id="ELE013", category="电子行业",
        name="竞争格局",
        query="电子行业竞争格局评估",
        expected_keywords=["竞争", "市场地位", "行业排名"]
    ),
    RAGTestCase(
        id="ELE014", category="电子行业",
        name="ESG评估影响",
        query="ESG评估对电子企业信用的影响",
        expected_keywords=["ESG", "环境", "治理"]
    ),
    RAGTestCase(
        id="ELE015", category="电子行业",
        name="特殊调整",
        query="电子企业评级的特殊调整因素",
        expected_keywords=["调整", "转型", "诉讼"]
    ),

    # ========== 4. 综合检索 (15个) ==========
    RAGTestCase(
        id="GEN001", category="综合检索",
        name="违约风险核心指标",
        query="违约风险评估的核心指标有哪些",
        expected_keywords=["违约风险", "评估", "指标"]
    ),
    RAGTestCase(
        id="GEN002", category="综合检索",
        name="信用评级委员会",
        query="信用评级委员会的作用",
        expected_keywords=["信用评级委员会", "评定"]
    ),
    RAGTestCase(
        id="GEN003", category="综合检索",
        name="BCA和模型级别",
        query="BCA级别和模型级别的关系",
        expected_keywords=["BCA", "模型级别"]
    ),
    RAGTestCase(
        id="GEN004", category="综合检索",
        name="评级方法论",
        query="中诚信国际评级方法论",
        expected_keywords=["评级方法", "模型"]
    ),
    RAGTestCase(
        id="GEN005", category="综合检索",
        name="评级调整",
        query="信用评级调整的触发因素",
        expected_keywords=["调整", "级别"]
    ),
    RAGTestCase(
        id="GEN006", category="综合检索",
        name="行业对比",
        query="不同行业评级方法的差异",
        expected_keywords=["行业", "评级方法"]
    ),
    RAGTestCase(
        id="GEN007", category="综合检索",
        name="定性定量结合",
        query="评级中定性和定量因素如何结合",
        expected_keywords=["定性", "定量"]
    ),
    RAGTestCase(
        id="GEN008", category="综合检索",
        name="评级模型局限",
        query="评级模型的局限性",
        expected_keywords=["模型", "局限", "预测"]
    ),
    RAGTestCase(
        id="GEN009", category="综合检索",
        name="产业链影响",
        query="产业链稳定性对信用评级的影响",
        expected_keywords=["产业链", "稳定"]
    ),
    RAGTestCase(
        id="GEN010", category="综合检索",
        name="政府支持",
        query="政府支持对企业信用的影响",
        expected_keywords=["政府", "支持"]
    ),
    RAGTestCase(
        id="GEN011", category="综合检索",
        name="股东支持",
        query="股东支持在评级中的作用",
        expected_keywords=["股东", "支持"]
    ),
    RAGTestCase(
        id="GEN012", category="综合检索",
        name="公司治理",
        query="公司治理与信用风险的关系",
        expected_keywords=["治理", "风险"]
    ),
    RAGTestCase(
        id="GEN013", category="综合检索",
        name="债务负担",
        query="企业债务负担评估",
        expected_keywords=["债务", "负担", "杠杆"]
    ),
    RAGTestCase(
        id="GEN014", category="综合检索",
        name="盈利能力评估",
        query="企业盈利能力对评级的影响",
        expected_keywords=["盈利能力", "利润"]
    ),
    RAGTestCase(
        id="GEN015", category="综合检索",
        name="现金流分析",
        query="现金流分析在评级中的重要性",
        expected_keywords=["现金流", "偿付"]
    ),
]


# ============================================================================
# API 调用函数
# ============================================================================

def retrieve_chunks(query: str, dataset_ids: List[str], top_k: int = 10) -> List[Dict]:
    """调用 RAGFlow API 检索 chunks"""
    url = f"{RAGFLOW_API_URL}/api/v1/retrieval"

    payload = {
        "question": query,
        "dataset_ids": dataset_ids,
        "top_k": top_k,
        "similarity_threshold": 0.2,
        "vector_similarity_weight": 0.3,
        "highlight": True
    }

    try:
        response = requests.post(url, json=payload, headers=get_headers(), timeout=30)
        response.raise_for_status()
        data = response.json()

        if data.get("code") == 0:
            return data.get("data", {}).get("chunks", [])
        else:
            print(f"API Error: {data.get('message')}")
            return []
    except Exception as e:
        print(f"Request Error: {e}")
        return []


def get_dataset_info(dataset_id: str) -> Dict:
    """获取知识库信息"""
    url = f"{RAGFLOW_API_URL}/api/v1/datasets/{dataset_id}"

    try:
        response = requests.get(url, headers=get_headers(), timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("data", {})
    except Exception as e:
        print(f"Error getting dataset info: {e}")
        return {}


def list_documents(dataset_id: str) -> List[Dict]:
    """列出知识库文档"""
    url = f"{RAGFLOW_API_URL}/api/v1/datasets/{dataset_id}/documents"

    try:
        response = requests.get(url, headers=get_headers(), timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("data", [])
    except Exception as e:
        print(f"Error listing documents: {e}")
        return []


def get_document_chunks(dataset_id: str, document_id: str) -> List[Dict]:
    """获取文档 chunks"""
    url = f"{RAGFLOW_API_URL}/api/v1/datasets/{dataset_id}/documents/{document_id}/chunks"

    try:
        response = requests.get(url, headers=get_headers(), timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("data", {}).get("chunks", [])
    except Exception as e:
        print(f"Error getting chunks: {e}")
        return []


# ============================================================================
# 测试执行
# ============================================================================

@dataclass
class TestResult:
    """测试结果"""
    test_case: RAGTestCase
    passed: bool
    result_count: int
    top_similarity: float
    matched_keywords: List[str]
    missing_keywords: List[str]
    execution_time_ms: float
    error: str = ""


class RAGCapabilityTester:
    """RAG 能力测试器"""

    def __init__(self, kb_id: str = TEST_KB_ID):
        self.kb_id = kb_id
        self.results: List[TestResult] = []

    def run_test(self, tc: RAGTestCase) -> TestResult:
        """运行单个测试"""
        import time
        start = time.time()

        try:
            # 执行检索
            chunks = retrieve_chunks(
                query=tc.query,
                dataset_ids=[self.kb_id],
                top_k=20
            )

            execution_time = (time.time() - start) * 1000

            # 分析结果
            result_count = len(chunks)
            top_similarity = chunks[0].get("similarity", 0) if chunks else 0

            # 检查关键词
            all_content = " ".join([c.get("content", "") for c in chunks[:10]])
            matched = [kw for kw in tc.expected_keywords if kw in all_content]
            missing = [kw for kw in tc.expected_keywords if kw not in all_content]

            # 判断通过
            passed = (
                result_count >= tc.min_results and
                top_similarity >= tc.min_similarity and
                len(matched) >= len(tc.expected_keywords) * 0.5
            )

            return TestResult(
                test_case=tc,
                passed=passed,
                result_count=result_count,
                top_similarity=top_similarity,
                matched_keywords=matched,
                missing_keywords=missing,
                execution_time_ms=execution_time
            )

        except Exception as e:
            return TestResult(
                test_case=tc,
                passed=False,
                result_count=0,
                top_similarity=0,
                matched_keywords=[],
                missing_keywords=tc.expected_keywords,
                execution_time_ms=(time.time() - start) * 1000,
                error=str(e)
            )

    def run_all_tests(self, categories: List[str] = None):
        """运行所有测试"""
        test_cases = RAG_TEST_CASES
        if categories:
            test_cases = [tc for tc in test_cases if tc.category in categories]

        print(f"🚀 开始 RAGFlow RAG 能力验证")
        print(f"📚 知识库ID: {self.kb_id}")
        print(f"📝 测试用例数: {len(test_cases)}")
        print("-" * 80)

        self.results = []
        for tc in test_cases:
            result = self.run_test(tc)
            self.results.append(result)

            status = "✅" if result.passed else "❌"
            sim = f"{result.top_similarity:.2f}" if result.top_similarity else "0.00"
            print(f"{status} [{tc.id}] {tc.name}: {result.result_count} results, sim={sim}")

    def print_report(self):
        """打印报告"""
        if not self.results:
            print("No results available")
            return

        total = len(self.results)
        passed = sum(1 for r in self.results if r.passed)
        failed = total - passed

        print("\n" + "=" * 80)
        print("📊 RAGFlow RAG 能力验证报告")
        print("=" * 80)

        print(f"\n📈 总体统计:")
        print(f"  - 总用例: {total}")
        print(f"  - 通过: {passed} ✅")
        print(f"  - 失败: {failed} ❌")
        print(f"  - 通过率: {passed/total*100:.1f}%")

        # 平均统计
        avg_time = sum(r.execution_time_ms for r in self.results) / total
        sims = [r.top_similarity for r in self.results if r.top_similarity > 0]
        avg_sim = sum(sims) / len(sims) if sims else 0

        print(f"  - 平均响应时间: {avg_time:.1f}ms")
        print(f"  - 平均Top1相似度: {avg_sim:.4f}")

        # 按类别
        by_cat = {}
        for r in self.results:
            cat = r.test_case.category
            if cat not in by_cat:
                by_cat[cat] = {"total": 0, "passed": 0}
            by_cat[cat]["total"] += 1
            if r.passed:
                by_cat[cat]["passed"] += 1

        print(f"\n📂 按类别统计:")
        for cat, stats in by_cat.items():
            rate = stats["passed"] / stats["total"] * 100
            print(f"  - {cat}: {stats['passed']}/{stats['total']} ({rate:.0f}%)")

        # 失败用例
        if failed > 0:
            print(f"\n❌ 失败用例 (前10个):")
            for r in self.results[:10]:
                if not r.passed:
                    print(f"  - [{r.test_case.id}] {r.test_case.query[:40]}...")
                    if r.error:
                        print(f"    Error: {r.error}")
                    else:
                        print(f"    Results: {r.result_count}, Sim: {r.top_similarity:.2f}")
                        print(f"    Missing: {r.missing_keywords}")

        print("\n" + "=" * 80)

    def save_report(self, filename: str = "rag_capability_report.json"):
        """保存报告"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "kb_id": self.kb_id,
            "summary": {
                "total": len(self.results),
                "passed": sum(1 for r in self.results if r.passed),
                "failed": sum(1 for r in self.results if not r.passed),
                "pass_rate": f"{sum(1 for r in self.results if r.passed)/len(self.results)*100:.1f}%"
            },
            "results": [
                {
                    "id": r.test_case.id,
                    "category": r.test_case.category,
                    "name": r.test_case.name,
                    "query": r.test_case.query,
                    "passed": r.passed,
                    "result_count": r.result_count,
                    "top_similarity": r.top_similarity,
                    "matched_keywords": r.matched_keywords,
                    "missing_keywords": r.missing_keywords,
                    "execution_time_ms": r.execution_time_ms,
                    "error": r.error
                }
                for r in self.results
            ]
        }

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        print(f"\n📄 报告已保存: {filename}")


# ============================================================================
# 文档解析质量验证
# ============================================================================

def verify_document_parsing():
    """验证文档解析质量"""
    print("\n📄 文档解析质量验证")
    print("-" * 40)

    # 获取知识库信息
    kb_info = get_dataset_info(TEST_KB_ID)
    if kb_info:
        print(f"知识库: {kb_info.get('name', 'Unknown')}")
        print(f"文档数: {kb_info.get('document_count', 0)}")
        print(f"Chunks数: {kb_info.get('chunk_num', 0)}")

    # 列出文档
    docs = list_documents(TEST_KB_ID)
    print(f"\n文档列表 ({len(docs)} 个):")
    for doc in docs[:10]:
        name = doc.get("name", "Unknown")[:50]
        chunks = doc.get("chunk_num", 0)
        status = doc.get("progress", 0)
        print(f"  - {name}... ({chunks} chunks, {status}%)")


def verify_chunk_quality():
    """验证 Chunk 分块质量"""
    print("\n🧩 Chunk 分块质量验证")
    print("-" * 40)

    # 获取文档列表
    docs = list_documents(TEST_KB_ID)
    if not docs:
        print("无文档")
        return

    # 抽样检查第一个文档
    doc = docs[0]
    doc_id = doc.get("id")
    chunks = get_document_chunks(TEST_KB_ID, doc_id)

    if chunks:
        print(f"文档: {doc.get('name', 'Unknown')[:40]}...")
        print(f"Chunks数: {len(chunks)}")

        # 统计
        lengths = [len(c.get("content", "")) for c in chunks]
        avg_len = sum(lengths) / len(lengths) if lengths else 0
        min_len = min(lengths) if lengths else 0
        max_len = max(lengths) if lengths else 0

        print(f"平均长度: {avg_len:.0f} 字符")
        print(f"最短: {min_len} 字符")
        print(f"最长: {max_len} 字符")

        # 显示样例
        print(f"\n前3个 Chunk 样例:")
        for i, chunk in enumerate(chunks[:3]):
            content = chunk.get("content", "")[:100]
            print(f"  [{i+1}] {content}...")


# ============================================================================
# 主函数
# ============================================================================

def main():
    """主函数"""
    print("=" * 80)
    print("RAGFlow RAG 能力完整验证")
    print("=" * 80)

    if not RAGFLOW_API_KEY:
        print("⚠️  RAGFLOW_API_KEY 未设置!")
        print("请设置环境变量: export RAGFLOW_API_KEY=your_key")
        return

    # 1. 文档解析验证
    verify_document_parsing()

    # 2. Chunk 质量验证
    verify_chunk_quality()

    # 3. 检索能力验证
    tester = RAGCapabilityTester()
    tester.run_all_tests()
    tester.print_report()
    tester.save_report()


if __name__ == "__main__":
    main()
