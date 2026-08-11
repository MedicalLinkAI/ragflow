# 基准结果：CLHo糖尿病-哈大四.pdf

## 基本信息

- 文件：`CLHo糖尿病-哈大四.pdf`
- 大小：1000.5 KB
- PDF 总页数：5
- doc_id：`31265bf4870611f1a42715083c6c5e0f`
- 上传方式：skip
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T15:06:37  完成时间：2026-08-10T15:06:39  耗时：2.2s

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 0afdbdff | 1 | 1-1 | 肇东市维康大药房 有限公司销售单 流水号9999000234562564544  |
| 2 | 2ea8ed63 | 1 | 2-2 | 肇东市永馨福园综合门诊 门诊号：MZ9925103 科室：门诊 接诊日期：202 |
| 3 | ac24ae37 | 1 | 5-5 | 哈尔滨泽福大药房销售单 NO.98222250454552 2024-12-07 |
| 4 | 52d72916 | 1 | 3-3 | <table><tr><td>葡萄糖</td><td>GLU</td><td>1 |
| 5 | 08d2cfc0 | 2 | 0-4 | <table><tr><td>维生素C</td><td>None</td><td |
| 6 | 09628089 | 1 | 4-4 | <table><tr><td>葡萄糖</td><td>GLU</td><td>8 |
| 7 | 4ee80e04 | 1 | 4-4 | <table><tr><td>糖化血红蛋白</td><td>None</td>< |

- chunks 总数：7
- 各 chunk 页数合计（含跨页重复）：8
- 页码并集：`[0, 1, 2, 3, 4, 5]`
- 覆盖页数：6 / 5；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：❌ 未完全覆盖：覆盖 6/5 页，缺失 []，超范围 []**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 0 | 0 | 0 | encounter_date, chief_complaint, diagnosis | **-** |
| AdmissionRecord | 入院 | 0 | 0 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 0 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 0 | 0 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | 0 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 0 | 0 | 0 | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 0 | 0 | 0 | report_time, report_category, report_name | **-** |

- SmartSplitter Types 统计：`{}`
- ChunkMerger：`{}`
- Extractor skip 证据：0 条
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
（worker 日志中未找到该 doc_id 的记录，可能容器已重启或文档未重新解析）
```
