# 基准结果：JBYA 联药 湘雅三.pdf

## 基本信息

- 文件：`JBYA 联药 湘雅三.pdf`
- 大小：775.7 KB
- PDF 总页数：8
- doc_id：`c2d3fb5a870711f1a42715083c6c5e0f`
- 上传方式：skip
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T15:08:17  完成时间：2026-08-10T15:08:19  耗时：2.0s

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 4c2a0561 | 1 | 3-3 | 门诊病历 科室 门诊全科 就诊日期 2025-03-01 就诊时间 14:12: |
| 2 | 98faf303 | 1 | 6-6 | 养天和大药房 流水号：806581202503230257 收银员：唐红娟 日期 |
| 3 | 38e84ce6 | 1 | 7-7 | 养天和大药房 流水号：806581202501220207 收银员：唐红娟 日期 |
| 4 | 6b5ccfd7 | 1 | 8-8 | 长沙市岳麓区观沙岭街道社区卫生服务中心 门诊病历 科室 门诊全科 就诊日期 20 |
| 5 | 41e27671 | 1 | 1-1 | <table><tr><td>糖化血红蛋白</td><td>HbA1c</td> |
| 6 | ee9adf9b | 1 | 5-5 | <table><tr><td>GLU</td><td>None</td><td> |
| 7 | c7a08cb1 | 1 | 2-2 | <table><tr><td>糖化血红蛋白</td><td>GllbA1c</t |
| 8 | 4130157a | 1 | 4-4 | <table><tr><td>葡萄糖餐前</td><td>BS(餐前)</td> |

- chunks 总数：8
- 各 chunk 页数合计（含跨页重复）：8
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8]`
- 覆盖页数：8 / 8；缺失页：`[]`
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
