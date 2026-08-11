# 基准结果：LHPI+单药+司美医大一院.pdf

## 基本信息

- 文件：`LHPI+单药+司美医大一院.pdf`
- 大小：3490.2 KB
- PDF 总页数：7
- doc_id：`96ec9424870811f1a42715083c6c5e0f`
- 上传方式：skip
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T15:08:19  完成时间：2026-08-10T15:08:21  耗时：2.0s

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 6fbbc443 | 1 | 1-1 | 石家庄真仁中医钩活术总医院 姓名：刘 性别：男 年龄：56 科室：中西医结合 主 |
| 2 | 563462b0 | 1 | 2-2 | 石家庄明瀚医院门诊病历 姓名:刘会平 性别:男 年龄:56岁 科室:内二门诊 过 |
| 3 | d45f97de | 1 | 5-5 | 世纪康大药房 流水单号：20250329032 会员姓名：刘会平 商品名称 单价 |
| 4 | 4ec7e8ab | 1 | 6-6 | 世纪康大药房 流水单号：20250102026 会员姓名： 商品名称 单价 折后 |
| 5 | 6efcfc02 | 1 | 7-7 | mm W A29216 DOL Exam.: 2025/四月/21 Diagno |
| 6 | 508bbb12 | 1 | 3-3 | <table><tr><td>糖化血红蛋白</td><td>HbA1C</td> |
| 7 | c287c913 | 1 | 4-4 | <table><tr><td>葡萄糖</td><td>GLU</td><td>8 |

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
