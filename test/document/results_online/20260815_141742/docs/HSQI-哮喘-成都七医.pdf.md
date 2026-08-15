# 线上统计：HSQI-哮喘-成都七医.pdf

## 基本信息

- 文件：`HSQI-哮喘-成都七医.pdf`
- 大小：543.6 KB
- PDF 总页数：-
- doc_id：`9b33ca087c1211f18d62dd81525255fa`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：3  orm_synced：True
- 处理耗时(服务端)：190.60262s  脚本耗时：201.6s
- 重解析前快照（无基线结果）：chunk_count=3 run=DONE clinical 类型记录数={'OutpatientRecord': 1, 'PrescriptionRecord': 1, 'ExaminationReport': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 9463148b | 1 | 1-1 | 四川大学华西天府医院 肺功能报告 测试ID: TF0035519712 姓名：  |
| 2 | e72bed14 | 2 | 2-3 | 门诊病历 就诊时间：2025-01-08 08:18:16 就诊号：250108 |
| 3 | 5623336b | 1 | 3-3 | 姓名： 年龄：39岁 性别：女性 体重： 就诊号：250108730788 西药 |

- chunks 总数：3
- 各 chunk 页数合计（含跨页重复）：4
- 页码并集：`[1, 2, 3]`
- 覆盖页数：3 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| ExaminationReport | 检查报告 | 1 | 0 | ❌ |
| OutpatientRecord | 门诊 | 1 | 0 | ❌ |
| PrescriptionRecord | 处方 | 1 | 0 | ❌ |

- 判定：❌ 不匹配类型: ExaminationReport, OutpatientRecord, PrescriptionRecord
