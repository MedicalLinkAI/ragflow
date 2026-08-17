# 线上统计：黑龙江省中医医院- WYXI-糖尿病.pdf

## 基本信息

- 文件：`黑龙江省中医医院- WYXI-糖尿病.pdf`
- 大小：1255.3 KB
- PDF 总页数：-
- doc_id：`9ca00bd278f111f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：6  orm_synced：True
- 处理耗时(服务端)：129.97499s  脚本耗时：135.6s
- 重解析前快照（无基线结果）：chunk_count=6 run=DONE clinical 类型记录数={'OutpatientRecord': 1, 'MedicationRecord': 2, 'LabReport': 3}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 4bd7a096 | 1 | 1-1 | 道里区人民医院门诊病历 姓名 就诊号：00342905 2025-02-06 1 |
| 2 | 7bca6be4 | 1 | 5-5 | 电子发票(普通发票) 发票号码：25232000000018649374 开票日 |
| 3 | f176d1e6 | 1 | 6-6 | 哈尔滨市万福堂大药房有 限公司 会员卡号03601103 积分:223.16 会 |
| 4 | cfc6c42d | 1 | 2-2 | <table><tr><td>糖化血红蛋白</td><td>HbA1c</td> |
| 5 | 6c7dedfb | 1 | 3-3 | <table><tr><td>葡萄糖</td><td>GLU</td><td>8 |
| 6 | 8abe8dec | 1 | 4-4 | <table><tr><td>糖化血红蛋白</td><td>HBA1C</td> |

- chunks 总数：6
- 各 chunk 页数合计（含跨页重复）：6
- 页码并集：`[1, 2, 3, 4, 5, 6]`
- 覆盖页数：6 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| LabReport | 检验报告 | 3 | 3 | ✅ |
| MedicationRecord | 购药 | 2 | 2 | ✅ |
| OutpatientRecord | 门诊 | 1 | 1 | ✅ |

- 判定：✅ 全部类型匹配
