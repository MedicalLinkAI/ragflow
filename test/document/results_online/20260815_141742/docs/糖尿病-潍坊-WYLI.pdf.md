# 线上统计：糖尿病-潍坊-WYLI.pdf

## 基本信息

- 文件：`糖尿病-潍坊-WYLI.pdf`
- 大小：7573.9 KB
- PDF 总页数：-
- doc_id：`246392427c3e11f18d62dd81525255fa`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：7  orm_synced：True
- 处理耗时(服务端)：240.8525s  脚本耗时：243.1s
- 重解析前快照（无基线结果）：chunk_count=9 run=DONE clinical 类型记录数={'OutpatientRecord': 2, 'PrescriptionRecord': 1, 'MedicationRecord': 1, 'LabReport': 4}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 4fa5edd7 | 1 | 1-1 | 门诊病历 姓名 性别：女 年龄：64岁 卡号 2024-12-18 14:20  |
| 2 | cf4698be | 1 | 2-2 | 门诊病历 姓名 性别：女 年龄：65岁 卡号 2025-02-14 11:24  |
| 3 | 0442c578 | 1 | 3-3 | 方明细 全部 西成药 中草药 项目 检验 检查 显示无库存 显示控制或停用药品  |
| 4 | c487f564 | 1 | 4-4 | Rp: 康复楼药房 已缴费 2025-03-23 09:18:49 2 [甲]盐 |
| 5 | 229fa6ea | 1 | 9-9 | 历史处方明细 Rp 组 名称 规格 剂量 剂量单位 用法 Rp:2 特病： 内分 |
| 6 | e8e43441 | 1 | 10-10 | 姓名： 性别：女 年龄：65岁 收款员：3013 打印时间：2025-04-28 |
| 7 | 0f1b79b9 | 4 | 5-8 | <table><tr><td>尿隐血(尿干化学)</td><td>BLD</td |

- chunks 总数：7
- 各 chunk 页数合计（含跨页重复）：10
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
- 覆盖页数：10 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| LabReport | 检验报告 | 1 | 0 | ❌ |
| MedicationRecord | 购药 | 1 | 0 | ❌ |
| OutpatientRecord | 门诊 | 2 | 0 | ❌ |
| PrescriptionRecord | 处方 | 3 | 0 | ❌ |

- 判定：❌ 不匹配类型: LabReport, MedicationRecord, OutpatientRecord, PrescriptionRecord
