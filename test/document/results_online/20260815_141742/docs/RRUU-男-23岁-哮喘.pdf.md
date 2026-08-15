# 线上统计：RRUU-男-23岁-哮喘.pdf

## 基本信息

- 文件：`RRUU-男-23岁-哮喘.pdf`
- 大小：4859.8 KB
- PDF 总页数：-
- doc_id：`31a5cfb2873111f1bb8027103a248952`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：6  orm_synced：True
- 处理耗时(服务端)：196.19025s  脚本耗时：197.1s
- 重解析前快照（无基线结果）：chunk_count=6 run=DONE clinical 类型记录数={'AdmissionRecord': 1, 'LabReport': 4, 'ExaminationReport': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | bc6dcff5 | 3 | 1-3 | PASS (省集1)注射用七... 科室:肿瘤科、血液科病历号: 费别:职工 成 |
| 2 | 7660404f | 2 | 8-9 | PASS (省集1)注射用七... 科室:肿瘤科、血液科病历号: 费别:职工 定 |
| 3 | 3c2a2199 | 1 | 5-5 | <table><tr><td>白细胞计数</td><td>WBC</td><td |
| 4 | e5176d3d | 1 | 6-6 | <table><tr><td>乙型肝炎病毒表面抗原</td><td>HBsAg< |
| 5 | 63b1de4b | 1 | 7-7 | <table><tr><td>白细胞白介素-1β</td><td>None</t |
| 6 | 6429fc9a | 1 | 4-4 | <table><tr><td>天门冬氨酸氨基转氨酶</td><td>AST</t |

- chunks 总数：6
- 各 chunk 页数合计（含跨页重复）：9
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9]`
- 覆盖页数：9 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 1 | ✅ |
| ExaminationReport | 检查报告 | 1 | 1 | ✅ |
| LabReport | 检验报告 | 4 | 4 | ✅ |

- 判定：✅ 全部类型匹配
