# 线上统计：WCLI-糖尿病(1).pdf

## 基本信息

- 文件：`WCLI-糖尿病(1).pdf`
- 大小：1678.2 KB
- PDF 总页数：-
- doc_id：`1411c4bc78f211f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：5  orm_synced：True
- 处理耗时(服务端)：173.17987s  脚本耗时：177.6s
- 重解析前快照（无基线结果）：chunk_count=5 run=DONE clinical 类型记录数={'OutpatientRecord': 2, 'MedicationRecord': 1, 'LabReport': 2}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | b02ca15e | 1 | 1-1 | 郑州市北下街社区卫生服务中心 诊断证明书 姓名 性别：女 年龄：60 科别： 门 |
| 2 | d9f251a6 | 2 | 4-5 | 郑州市第三人民医院门诊病历 日期：2025/04/01 ID: 20238365 |
| 3 | 397cfb2c | 2 | 5-6 | 郑州康元堂大药房有限公司 -30.50 当前状态 支付成功 支付时间 2025年 |
| 4 | 3a6e9eb5 | 1 | 2-2 | <table><tr><td>糖化血红蛋白</td><td>HbA1C</td> |
| 5 | b178dc5d | 1 | 3-3 | <table><tr><td>谷丙转氨酶</td><td>ALT</td><td |

- chunks 总数：5
- 各 chunk 页数合计（含跨页重复）：7
- 页码并集：`[1, 2, 3, 4, 5, 6]`
- 覆盖页数：6 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| LabReport | 检验报告 | 2 | 2 | ✅ |
| MedicationRecord | 购药 | 1 | 1 | ✅ |
| OutpatientRecord | 门诊 | 2 | 2 | ✅ |

- 判定：✅ 全部类型匹配
