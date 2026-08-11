# 基准结果：HZNA高血糖郑州.pdf

## 基本信息

- 文件：`HZNA高血糖郑州.pdf`
- 大小：7407.5 KB
- PDF 总页数：9
- doc_id：`3bedc7b681e811f18b4685712ca9598c`
- 上传方式：skip
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T15:08:15  完成时间：2026-08-10T15:08:17  耗时：2.2s

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | e229e16f | 1 | 1-1 | 民医院 出院证 住院号：024 医疗保险证号： 姓名： 性别：男 年龄：37岁  |
| 2 | 2b5da9f8 | 1 | 3-3 | 天医院 门诊患者费用清单(汇总) 证件号:4107251 姓名. 卡号:4 开始 |
| 3 | d3b2f76f | 1 | 5-5 | 中心药店 日期: 2025 02 15 19:20:00 销售员: 毛爱青 药品 |
| 4 | a4266757 | 1 | 6-6 | 原阳县人民医院 门诊病历 门诊号：135700000737 姓名： 性别：男 年 |
| 5 | f4b865fe | 1 | 7-7 | 原阳县人民医院处方笺 普通 门诊号：1595205 No： 2504105697 |
| 6 | 78d5fcc8 | 1 | 8-8 | 原阳县人民医院 姓名： 医保类别：自费 收费时间：2025-04-10 00:0 |
| 7 | 97508809 | 1 | 9-9 | 原阳县人民医院 门诊患者费用清单 卡号：410725198706033639 账 |
| 8 | 0e4c0c51 | 1 | 2-2 | <table><tr><td>糖化血红蛋白</td><td>HbA1C</td> |
| 9 | 8bfe33fb | 1 | 4-4 | <table><tr><td>随机血糖</td><td>SJXT</td><td |
| 10 | 3b358091 | 1 | 4-4 | <table><tr><td>糖化血红蛋白</td><td>HbA1C</td> |

- chunks 总数：10
- 各 chunk 页数合计（含跨页重复）：10
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9]`
- 覆盖页数：9 / 9；缺失页：`[]`
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
