# 线上统计：糖尿病-哈大四-SuTa.pdf

## 基本信息

- 文件：`糖尿病-哈大四-SuTa.pdf`
- 大小：1205.5 KB
- PDF 总页数：-
- doc_id：`79a3d7cc7e6811f1af97e3985ba7f8da`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：6  orm_synced：True
- 处理耗时(服务端)：124.555756s  脚本耗时：125.3s
- 重解析前快照（无基线结果）：chunk_count=6 run=DONE clinical 类型记录数={'OutpatientRecord': 1, 'LabReport': 4, 'MedicationRecord': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | bd4f8bb0 | 1 | 2-2 | 哈尔滨弘医京德综合门诊 姓名： 性别：男 年龄：51岁 门诊号：23022504 |
| 2 | 1ecfce10 | 1 | 7-7 | 哈尔滨及时雨大药房 销售单 流水号：9992512204100450 日期：20 |
| 3 | beae0c0b | 1 | 3-3 | <table><tr><td>糖化血红蛋白值测定</td><td>HbA1c</ |
| 4 | c005d855 | 1 | 5-5 | <table><tr><td>糖化血红蛋白</td><td>None</td>< |
| 5 | 21f717d8 | 1 | 4-4 | <table><tr><td>糖化血红蛋白值测定</td><td>HbA1c</ |
| 6 | 68fbbcb4 | 1 | 6-6 | <table><tr><td>葡萄糖</td><td>GLU</td><td>9 |

- chunks 总数：6
- 各 chunk 页数合计（含跨页重复）：6
- 页码并集：`[2, 3, 4, 5, 6, 7]`
- 覆盖页数：6 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| LabReport | 检验报告 | 4 | 4 | ✅ |
| MedicationRecord | 购药 | 1 | 1 | ✅ |
| OutpatientRecord | 门诊 | 1 | 1 | ✅ |

- 判定：✅ 全部类型匹配
