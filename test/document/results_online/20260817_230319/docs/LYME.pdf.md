# 线上统计：LYME.pdf

## 基本信息

- 文件：`LYME.pdf`
- 大小：2679.1 KB
- PDF 总页数：-
- doc_id：`74df3e7878f211f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：14  orm_synced：True
- 处理耗时(服务端)：210.05956s  脚本耗时：212.5s
- 重解析前快照（无基线结果）：chunk_count=12 run=DONE clinical 类型记录数={'OutpatientRecord': 1, 'LabReport': 8, 'ExaminationReport': 3}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 2c2a0dac | 1 | 1-1 | 营口方大医院有限公司 病理报告单 病理号: 姓名: 住院 5024 年龄: 54 |
| 2 | 008a9849 | 1 | 2-2 | 营口方大医院 核医学科 PET/CT 报告单 检查号: 姓名: 性别: 女 年龄 |
| 3 | a8c5b33c | 1 | 3-3 | 营口方大医院 核医学科 PET/CT 报告单 检查号 姓名: 性别: 女 检查日 |
| 4 | fe34cf86 | 1 | 4-4 | 营口方大医院 复诊记录 M000747 介入科(肿瘤方向)/老年病 日期选择:  |
| 5 | 9cc0ecce | 1 | 5-5 | \begin{tabular}{lllllllll} 报告时间: 2026-03 |
| 6 | a5d427a7 | 1 | 8-8 | \begin{tabular}{ccccccll} 报告时间: 2026-03- |
| 7 | ca800fb9 | 1 | 5-5 | <table><tr><td>白细胞</td><td>WBC</td><td>6 |
| 8 | 659622da | 1 | 6-6 | <table><tr><td>谷丙转氨酶</td><td>ALT</td><td |
| 9 | f64c69bb | 1 | 6-6 | <table><tr><td>癌胚抗原</td><td>CEA</td><td> |
| 10 | 8ff59d82 | 1 | 8-8 | <table><tr><td>人类免疫缺陷病毒抗体</td><td>HIV</t |
| 11 | 093a544c | 1 | 6-6 | <table><tr><td>神经元特异性烯醇化酶</td><td>NSE</t |
| 12 | 111f1b19 | 1 | 7-7 | <table><tr><td>胚胎抗原125</td><td>CA125</td |
| 13 | 83770c4a | 1 | 7-7 | <table><tr><td>尿胆原</td><td>UBG</td><td>N |
| 14 | 973980a5 | 1 | 7-7 | <table><tr><td>癌胚抗原测定</td><td>CEA</td><t |

- chunks 总数：14
- 各 chunk 页数合计（含跨页重复）：14
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8]`
- 覆盖页数：8 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| ExaminationReport | 检查报告 | 3 | 3 | ✅ |
| LabReport | 检验报告 | 10 | 8 | ❌ |
| OutpatientRecord | 门诊 | 1 | 1 | ✅ |

- 判定：❌ 不匹配类型: LabReport
