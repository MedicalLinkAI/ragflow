# 线上统计：重庆-LFQU-肺腺癌-方穹推荐706-I期（IB期）.pdf

## 基本信息

- 文件：`重庆-LFQU-肺腺癌-方穹推荐706-I期（IB期）.pdf`
- 大小：6214.6 KB
- PDF 总页数：-
- doc_id：`82ffa866837f11f1af97e3985ba7f8da`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：12  orm_synced：True
- 处理耗时(服务端)：552.1478s  脚本耗时：552.8s
- 重解析前快照（无基线结果）：chunk_count=12 run=DONE clinical 类型记录数={'AdmissionRecord': 2, 'LabReport': 4, 'ExaminationReport': 4}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | a99fb111 | 2 | 1-2 | 2026年02月18日 姓名： 性别：(男) 年龄：(65岁) 籍贯：(长寿)  |
| 2 | 9d3ccf4b | 1 | 2-2 | 首次病程： 2026年02月18日 13时25分10秒 姓名：[李福泉] ，性别 |
| 3 | 01e17410 | 1 | 3-3 | 开始 病历列表 住院病历 - 感染费 床号: 13 - 住院... 住院病历 - |
| 4 | 27a5d9b4 | 1 | 3-3 | 2025年12月23日 10时30分14秒 彭雷王治医师查房记录 今日查房主治医 |
| 5 | 07b1ad45 | 1 | 4-4 | 病理诊断报告单 性别：男 年龄：66岁 送检日期：2026-02-24 门诊号： |
| 6 | 6d2eac58 | 2 | 5-6 | 姓名： 性别：男 年龄：~岁 申请单号： 科别：呼吸与危重症医学科 住院号：27 |
| 7 | 2dcd65fd | 1 | 12-12 | 肺功能综合检查报告 姓名： 测试号：2026031831-1 性别：男 体重：5 |
| 8 | 411bb0a8 | 1 | 7-7 | <table><tr><td>丙氨酸氨基转移酶</td><td>None</td |
| 9 | f579a866 | 2 | 10-11 | <table><tr><td>EGFR L858R</td><td>None</ |
| 10 | a5de9407 | 1 | 6-6 | <table><tr><td>白细胞</td><td>None</td><td> |
| 11 | ba2b70fb | 1 | 8-8 | <table><tr><td>凝血酶原时间测定</td><td>None</td |
| 12 | 4cd92ce7 | 1 | 9-9 | <table><tr><td>丙型肝炎抗体</td><td>None</td>< |

- chunks 总数：12
- 各 chunk 页数合计（含跨页重复）：15
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]`
- 覆盖页数：12 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 0 | ❌ |
| ExaminationReport | 检查报告 | 3 | 0 | ❌ |
| LabReport | 检验报告 | 5 | 0 | ❌ |
| ProgressNote | 病程记录 | 3 | 0 | ❌ |

- 判定：❌ 不匹配类型: AdmissionRecord, ExaminationReport, LabReport, ProgressNote
