# 基准结果：Wlge-肝癌-男-57岁.pdf

## 基本信息

- 文件：`Wlge-肝癌-男-57岁.pdf`
- 大小：7702.0 KB
- PDF 总页数：16
- doc_id：`e31f265081e911f18b4685712ca9598c`
- 上传方式：skip
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-06T19:04:16  完成时间：2026-08-06T19:04:20  耗时：4.1s

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 66ecb72f | 2 | 1-2 | 族:汉族 婚姻:已婚 出生地:江西省南昌市湾里区 业:其他 现住址:江西省南昌市 |
| 2 | 57ea0674 | 1 | 2-2 | 就诊科室:红角洲肝胆外科门诊 就诊时间:2025年12月07日 08:46 药物 |
| 3 | bc47af26 | 1 | 3-3 | 就诊科室:红角洲肝胆外科门诊 就诊时间:2026年03月05日 09:51 药物 |
| 4 | 38bdc420 | 1 | 4-4 | 职业： 出生日期：1968年01月06日 工作单位或地址：湾里区 就诊科室：红角 |
| 5 | 6184098a | 2 | 5-6 | 入院日期：2025年08月02日 出院日期：2025年08月06日 住院天数：4 |
| 6 | 573767b2 | 2 | 6-7 | I 肝区介入术后复查所见。 入院诊断：1.肝癌介入治疗2.原发性肝癌(BCLC  |
| 7 | b599a40b | 2 | 7-8 | 第1页 入院诊断：1.原发性肝癌(BCLC B期，CNLC IIb期)2.左肾结 |
| 8 | 38339e64 | 2 | 9-10 | 入院日期：2025年03月18日 出院日期：2025年03月24日 住院天数：6 |
| 9 | 1a70cb77 | 1 | 10-10 | 向治疗,4.恶性肿瘤免疫治疗,5.肝癌介入治疗 检查项目:上腹部薄层CT平扫+增 |
| 10 | 2f625b69 | 1 | 11-11 | 临床诊断:1.肝细胞癌(BCLC B期,CNLC 11b期),2.慢性乙型病毒性 |
| 11 | cf5c8a30 | 2 | 11-12 | 第1页 共1页 临床诊断:1.肝癌介入治疗,2.原发性肝癌 检查项目:胸部CT平 |
| 12 | 31742646 | 1 | 13-13 | 临床诊断:1.肝癌介入治疗,2.原发性肝癌(BCLC B期,CNLC Ⅱb期), |
| 13 | 81871f59 | 1 | 14-14 | <table><tr><td>白细胞计数</td><td>WBC</td><td |
| 14 | 66ad9186 | 1 | 15-15 | <table><tr><td>总蛋白</td><td>TP</td><td>77 |
| 15 | e7686182 | 1 | 16-16 | <table><tr><td>甲胎蛋白测定</td><td>AFP</td><t |

- chunks 总数：15
- 各 chunk 页数合计（含跨页重复）：21
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]`
- 覆盖页数：16 / 16；缺失页：`[]`
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
