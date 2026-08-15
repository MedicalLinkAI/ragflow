# 线上统计：类风湿-LHGE-郑州(1).pdf

## 基本信息

- 文件：`类风湿-LHGE-郑州(1).pdf`
- 大小：8821.7 KB
- PDF 总页数：-
- doc_id：`a2dc44f47c5011f18d62dd81525255fa`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：9  orm_synced：True
- 处理耗时(服务端)：208.60791s  脚本耗时：212.6s
- 重解析前快照（无基线结果）：chunk_count=8 run=DONE clinical 类型记录数={'OutpatientRecord': 2, 'MedicationRecord': 3, 'PrescriptionRecord': 2, 'LabReport': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 3b6022da | 2 | 1-2 | 郑州中医骨伤病医院 门（急）诊病历 姓名： 性别：女性 年龄：40岁 病历号：2 |
| 2 | 3a095cc7 | 1 | 3-3 | 郑州中医骨伤病医院 处方笺 住院（门诊）号：100 日期：2025年02月17日 |
| 3 | 83ef1096 | 1 | 4-4 | 郑州中医骨伤病医院 处方笺 住院（门诊）号：10 日期：2025年02月17日  |
| 4 | 42fd6d7b | 2 | 4-5 | 普 郑州中医骨伤病医院费用清单 患者姓名： 患者分类：自费 患者编码：10005 |
| 5 | 610948e0 | 2 | 5-6 | 顺丰 还 河南省药源春医药有限公司 P41018401480 购药人: 票据号: |
| 6 | 9cf0147e | 1 | 7-7 | 河南省药源春医药有限公司 P41018401480 购药人: 票据号: 2360 |
| 7 | 5dd789ac | 1 | 8-8 | 河南省药源春医药有限公司 P41018401480 购药人 票据号：2769 个 |
| 8 | 21b86245 | 2 | 9-10 | 郑州中医骨伤病医院 门（急）诊病历 姓名： 性别：女性年龄：42岁 病历号： 复 |
| 9 | 71bbc274 | 1 | 11-11 | <table><tr><td>抗链球菌溶血素O</td><td>ASO</td> |

- chunks 总数：9
- 各 chunk 页数合计（含跨页重复）：13
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]`
- 覆盖页数：11 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| LabReport | 检验报告 | 1 | 0 | ❌ |
| MedicationRecord | 购药 | 4 | 0 | ❌ |
| OutpatientRecord | 门诊 | 2 | 0 | ❌ |
| PrescriptionRecord | 处方 | 2 | 0 | ❌ |

- 判定：❌ 不匹配类型: LabReport, MedicationRecord, OutpatientRecord, PrescriptionRecord
