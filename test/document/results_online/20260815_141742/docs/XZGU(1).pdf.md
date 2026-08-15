# 线上统计：XZGU(1).pdf

## 基本信息

- 文件：`XZGU(1).pdf`
- 大小：1015.7 KB
- PDF 总页数：-
- doc_id：`2753e13278f111f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：4  orm_synced：True
- 处理耗时(服务端)：84.05614s  脚本耗时：88.6s
- 重解析前快照（无基线结果）：chunk_count=4 run=DONE clinical 类型记录数={'OutpatientRecord': 1, 'MedicationRecord': 2, 'LabReport': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 2c126f89 | 1 | 1-1 | 西安市未央宫社区卫生服务中心 门诊病历 姓名： 性别：男 年龄：47岁 费别：自 |
| 2 | 79eaad53 | 1 | 3-3 | 电子发票(普通发票) 国家税务总局 陕西省税务局 发票号码:2561200000 |
| 3 | a8b43fdd | 1 | 4-4 | 合德堂医药超市 单据号：XC05013042501070089 日期:2025- |
| 4 | 88b7d70d | 1 | 2-2 | <table><tr><td>糖化血红蛋白*陕HR</td><td>HbA1c< |

- chunks 总数：4
- 各 chunk 页数合计（含跨页重复）：4
- 页码并集：`[1, 2, 3, 4]`
- 覆盖页数：4 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| LabReport | 检验报告 | 1 | 0 | ❌ |
| MedicationRecord | 购药 | 2 | 0 | ❌ |
| OutpatientRecord | 门诊 | 1 | 0 | ❌ |

- 判定：❌ 不匹配类型: LabReport, MedicationRecord, OutpatientRecord
