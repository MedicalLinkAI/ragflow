# RAGflow PDF Parser Evaluation with OmniDocBench

本目录包含基于 OmniDocBench 数据集评测 RAGflow PDF 解析器的完整工具链。

## 📋 评测目标

客观对比 RAGflow 的 4 个 PDF 解析器在真实场景下的表现：
- **DeepDOC**（RAGflow 自带，基于 PaddleOCR）
- **MinerU**（开源 PDF 解析工具）
- **Docling**（IBM 的文档解析工具）
- **DeepSeek-OCR2**（本次新集成的 Visual Causal Flow 解析器）

## 🎯 评测指标

基于 OmniDocBench 官方标准：

### 自动化指标（全量）
1. **Success Rate**: 成功解析页面比例
2. **Text Edit Distance**: 文本准确性（0=完美，1=完全错误）
3. **Table TEDS**: 表格结构准确性（0=错误，1=完美）
4. **Processing Time**: 每页平均处理时间
5. **Overall Score**: 综合分 = `((1 - Text_ED) * 100 + TEDS) / 2`

### 数据集规模
- **测试集**: 100 样本（快速验证，~30 分钟）
- **全量集**: 1355 样本（完整评测，~4-6 小时）

## 🚀 快速开始（5090 GPU 服务器）

### 方式 1：一键部署（推荐）

```bash
# SSH 登录到 5090 服务器
ssh user@5090-server-ip

# 运行一键部署脚本
cd /path/to/ragflow
bash scripts/deploy_to_5090.sh
```

部署脚本会自动：
- ✅ 检查 GPU/CUDA/Python 环境
- ✅ 拉取最新代码（develop 分支）
- ✅ 安装所有依赖（RAGflow + 4 个解析器 + OmniDocBench）
- ✅ 下载 100 样本测试集

### 方式 2：手动部署

```bash
# 1. 克隆代码
git clone -b develop git@github.com:redleaves/ragflow.git
cd ragflow

# 2. 创建虚拟环境
python3.11 -m venv .venv
source .venv/bin/activate

# 3. 安装依赖
pip install -e .
pip install -e .[deepseek-ocr2]
pip install magic-pdf docling datasets tabulate

# 4. 克隆 OmniDocBench 评测工具
git clone https://github.com/opendatalab/OmniDocBench.git
cd OmniDocBench && pip install -r requirements.txt && cd ..

# 5. 下载测试数据集
python scripts/download_omnidocbench.py --max-samples 100
```

## 📊 运行评测

### 快速测试（100 样本）

```bash
source .venv/bin/activate

python scripts/validate_with_omnidocbench.py \
  --max-samples 100 \
  --parsers deepdoc,mineru,docling,deepseek-ocr2 \
  --output validation_omnidoc_test.json
```

**预计时间**: 30-60 分钟（取决于 GPU 性能）

### 全量评测（1355 样本）

```bash
# 先下载全量数据集
python scripts/download_omnidocbench.py --max-samples 1355

# 运行全量评测
python scripts/validate_with_omnidocbench.py \
  --max-samples 1355 \
  --parsers deepdoc,mineru,docling,deepseek-ocr2 \
  --output validation_omnidoc_full.json
```

**预计时间**: 4-6 小时

### 指定解析器评测

```bash
# 只测试 DeepDOC 和 DeepSeek-OCR2
python scripts/validate_with_omnidocbench.py \
  --max-samples 100 \
  --parsers deepdoc,deepseek-ocr2
```

## 📈 生成报告

评测完成后，生成可视化报告：

```bash
python scripts/generate_report.py validation_omnidoc_test.json --output-dir ./reports
```

**输出文件**:
```
reports/
├── comparison_table.md          # Markdown 对比表格
├── comparison_heatmap.png       # 热力图可视化
├── recommendation.md            # 场景推荐（哪种文档用哪个解析器）
└── detailed/
    ├── deepdoc_detailed.csv
    ├── mineru_detailed.csv
    ├── docling_detailed.csv
    └── deepseek_ocr2_detailed.csv
```

## 📁 脚本说明

| 脚本 | 功能 | 用途 |
|------|------|------|
| `deploy_to_5090.sh` | 一键部署脚本 | 在 5090 服务器上快速搭建评测环境 |
| `download_omnidocbench.py` | 下载数据集 | 从 HuggingFace 下载 OmniDocBench 测试集 |
| `ragflow_to_omnidoc_adapter.py` | 格式适配器 | 将 RAGflow 输出转为 OmniDocBench 评测格式 |
| `validate_with_omnidocbench.py` | 主评测脚本 | 运行 4 个解析器并计算官方指标 |
| `generate_report.py` | 报告生成器 | 从评测结果生成表格/图表/推荐 |

## 🔍 评测流程说明

```
1. 加载 OmniDocBench 数据集
   ├─ 1355 页 PDF（带人工标注 GT）
   └─ 覆盖 9 种文档类型、4 种布局、3 种语言

2. 对每个解析器运行
   ├─ 调用 RAGflow 统一入口 (PARSERS dict)
   ├─ 记录：处理时间、内存占用、GPU 显存
   └─ 输出：sections + tables

3. 格式归一化
   ├─ sections → 纯文本（去坐标 tag、统一换行、去多余空格）
   └─ tables → HTML/LaTeX（用于 TEDS 计算）

4. 计算指标（对照 GT）
   ├─ Text Edit Distance（归一化编辑距离）
   ├─ Table TEDS（表格结构+内容相似度）
   └─ Overall Score = ((1 - ED) * 100 + TEDS) / 2

5. 生成报告
   ├─ 对比表格（Markdown）
   ├─ 热力图（PNG）
   └─ 场景推荐（根据指标推荐最佳解析器）
```

## 📊 预期结果示例

```
COMPARISON TABLE
========================================
Parser               | Success% | Text ED  | TEDS     | Overall 
---------------------|----------|----------|----------|----------
DeepSeek-OCR2        |    98.5% |   0.1234 |   0.8567 |    90.45
MinerU               |    96.2% |   0.1456 |   0.8234 |    87.89
Docling              |    95.0% |   0.1678 |   0.7890 |    85.11
DeepDOC              |    92.3% |   0.1890 |   0.7456 |    82.33

🏆 Winner: DeepSeek-OCR2 (Overall Score: 90.45)
```

## 🐛 常见问题

### Q1: `ModuleNotFoundError: No module named 'docx'`
**A**: 运行 `pip install python-docx`

### Q2: CUDA out of memory
**A**: 减少 batch size 或使用 `--max-samples 50` 先测试小规模

### Q3: OmniDocBench 下载失败
**A**: 检查网络，或手动从 HuggingFace 下载：https://huggingface.co/datasets/opendatalab/OmniDocBench

### Q4: 想只测试单个解析器
**A**: 使用 `--parsers deepseek-ocr2` 参数

## 📚 参考资料

- [OmniDocBench GitHub](https://github.com/opendatalab/OmniDocBench)
- [OmniDocBench Paper (CVPR 2025)](https://arxiv.org/abs/xxxx.xxxxx)
- [DeepSeek-OCR2 GitHub](https://github.com/deepseek-ai/DeepSeek-OCR-2)
- [RAGflow Documentation](https://github.com/infiniflow/ragflow)

## 📞 联系方式

如有问题，请联系：
- GitHub Issues: https://github.com/redleaves/ragflow/issues
- Email: your-email@example.com
