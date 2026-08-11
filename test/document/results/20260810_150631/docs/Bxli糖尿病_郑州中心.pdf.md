# 基准结果：Bxli糖尿病 郑州中心.pdf

## 基本信息

- 文件：`Bxli糖尿病 郑州中心.pdf`
- 大小：1126.6 KB
- PDF 总页数：7
- doc_id：`85a42d98870411f1a42715083c6c5e0f`
- 上传方式：skip
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T15:06:32  完成时间：2026-08-10T15:06:35  耗时：2.7s

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 30a611ce | 1 | 1-1 | 中西医结合医院 病人门（急）诊病历 病人ID M024474 姓名 性别：女 出 |
| 2 | b47d2066 | 1 | 2-2 | 医结合医院处方笺 普通 性别：女 年龄：67岁 费别：自费 病人ID：M0244 |
| 3 | 1fc70b8f | 1 | 3-3 | 中西医结合医院处方笺 普通 姓名 性别：女 年龄：66岁 费别：自费 病人ID： |
| 4 | 83066453 | 1 | 6-6 | 百顺中西医结合医院 527836 自费 西药费 50.00 大额记账: 大病补充 |
| 5 | 58b8dec9 | 1 | 7-7 | 20250507530576 新密佰顺中西医结合医院 530576 女 自费 西 |
| 6 | 0fe25ebb | 1 | 4-4 | <table><tr><td>糖化血红蛋白</td><td>HbA1c</td> |
| 7 | 0be52e34 | 1 | 5-5 | <table><tr><td>糖化血红蛋白</td><td>HbA1c</td> |

- chunks 总数：7
- 各 chunk 页数合计（含跨页重复）：7
- 页码并集：`[1, 2, 3, 4, 5, 6, 7]`
- 覆盖页数：7 / 7；缺失页：`[]`
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
