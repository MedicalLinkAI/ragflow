# 线上统计：博泰奥赛诺糖尿病 黑龙江省中医医院 LGRO.pdf

## 基本信息

- 文件：`博泰奥赛诺糖尿病 黑龙江省中医医院 LGRO.pdf`
- 大小：1489.2 KB
- PDF 总页数：-
- doc_id：`d9a240fa78f011f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：6  orm_synced：True
- 处理耗时(服务端)：62.96616s  脚本耗时：73.1s
- 重解析前快照（无基线结果）：chunk_count=6 run=DONE clinical 类型记录数={'OutpatientRecord': 1, 'MedicationRecord': 2, 'LabReport': 3}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 1d498ee9 | 1 | 1-1 | 哈尔滨市第四医院 门诊病历 姓名： 病人ID：1023031039 性别：女 年 |
| 2 | 7c155f9f | 1 | 5-5 | 哈尔滨三多大药房 有限公司 会员名 会员号：001020 1D2410448 盐 |
| 3 | d9b5d95e | 1 | 6-6 | 电子发票(普通发票) 发票号码：25232000000019614197 开票日 |
| 4 | 4cefbb90 | 1 | 2-2 | <table><tr><td>葡萄糖</td><td>GLU</td><td>9 |
| 5 | 44d4d0ec | 1 | 3-3 | <table><tr><td>*糖化血红蛋白 A1</td><td>HBA1C< |
| 6 | 0a1b2cd9 | 1 | 4-4 | <table><tr><td>糖化血红蛋白 A1</td><td>HBA1C</ |

- chunks 总数：6
- 各 chunk 页数合计（含跨页重复）：6
- 页码并集：`[1, 2, 3, 4, 5, 6]`
- 覆盖页数：6 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| LabReport | 检验报告 | 3 | 0 | ❌ |
| MedicationRecord | 购药 | 2 | 0 | ❌ |
| OutpatientRecord | 门诊 | 1 | 0 | ❌ |

- 判定：❌ 不匹配类型: LabReport, MedicationRecord, OutpatientRecord
