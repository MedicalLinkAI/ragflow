# 基准结果：SZQI-糖尿病-河北.pdf

## 基本信息

- 文件：`SZQI-糖尿病-河北.pdf`
- 大小：350.2 KB
- PDF 总页数：2
- doc_id：`561df61c871311f1a42715083c6c5e0f`
- 上传方式：skip
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T15:12:14  完成时间：2026-08-10T15:12:15  耗时：0.9s

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 21022a19 | 1 | 1-1 | 门诊病历 姓名： 性别：男 年龄：60 ID号： 科室：卫生室 日期：2024年 |
| 2 | bec1986b | 1 | 2-2 | <table><tr><td>糖化血红蛋白</td><td>HBA1C</td> |
| 3 | 924e463d | 1 | 2-2 | <table><tr><td>葡萄糖</td><td>GL</td><td>9. |

- chunks 总数：3
- 各 chunk 页数合计（含跨页重复）：3
- 页码并集：`[1, 2]`
- 覆盖页数：2 / 2；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

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
