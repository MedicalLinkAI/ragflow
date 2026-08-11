# 基准结果：XJYo-糖尿病-哈大四.pdf

## 基本信息

- 文件：`XJYo-糖尿病-哈大四.pdf`
- 大小：1624.0 KB
- PDF 总页数：9
- doc_id：`6f804630871511f1a42715083c6c5e0f`
- 上传方式：skip
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T15:15:51  完成时间：2026-08-10T15:15:52  耗时：0.9s

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 103338e9 | 1 | 2-2 | 哈尔滨同迈综合门诊 姓名: 就诊日期: 2021-09-12 就诊号: 2021 |
| 2 | 0a397492 | 1 | 3-3 | \begin{tabular}{ccccccc} 报告时间: 2021-09-1 |
| 3 | ff116cb7 | 1 | 5-5 | 哈尔滨体诚人药房有限公司 (P23010122054)销售单 号12875 日期 |
| 4 | d88e3099 | 1 | 6-6 | 哈尔滨泽福大药房有限 公司销售单据 NO.8555800415612312005 |
| 5 | 0b46f5d6 | 1 | 9-9 | <table><tr><td>葡萄糖（已糖激酶法）</td><td>None</ |
| 6 | 9ddfb73d | 1 | 4-4 | <table><tr><td>糖化血红蛋白</td><td>None</td>< |
| 7 | b50880ca | 1 | 7-7 | <table><tr><td>糖化血红蛋白LA1c</td><td>None</ |
| 8 | d8a91d61 | 1 | 8-8 | <table><tr><td>糖化血红蛋白A1</td><td>None</td |

- chunks 总数：8
- 各 chunk 页数合计（含跨页重复）：8
- 页码并集：`[2, 3, 4, 5, 6, 7, 8, 9]`
- 覆盖页数：8 / 9；缺失页：`[1]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：❌ 未完全覆盖：覆盖 8/9 页，缺失 [1]，超范围 []**

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
