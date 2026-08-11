# 基准结果：LiJu(1)(1)哈大四.pdf

## 基本信息

- 文件：`LiJu(1)(1)哈大四.pdf`
- 大小：1878.7 KB
- PDF 总页数：7
- doc_id：`3b5ad530870d11f1a42715083c6c5e0f`
- 上传方式：skip
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T15:08:21  完成时间：2026-08-10T15:08:23  耗时：1.9s

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | a5783b76 | 1 | 2-2 | 哈尔滨美颐医院门诊单 门诊号：102800000989 诊疗号：00081601 |
| 2 | 5ef662a0 | 1 | 5-5 | 哈尔滨康华大药房有限公 NO.55550534536320004523 日期:  |
| 3 | 2a106bba | 1 | 6-6 | <table><tr><td>糖化血红蛋白</td><td>None</td>< |
| 4 | 4bbe145b | 1 | 7-7 | <table><tr><td>葡萄糖</td><td>GLU</td><td>9 |
| 5 | d83aa78a | 1 | 3-3 | <table><tr><td>糖化血红蛋白</td><td>HbAlc</td> |
| 6 | c60c9f6d | 1 | 4-4 | <table><tr><td>糖化血红蛋白</td><td>None</td>< |

- chunks 总数：6
- 各 chunk 页数合计（含跨页重复）：6
- 页码并集：`[2, 3, 4, 5, 6, 7]`
- 覆盖页数：6 / 7；缺失页：`[1]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：❌ 未完全覆盖：覆盖 6/7 页，缺失 [1]，超范围 []**

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
