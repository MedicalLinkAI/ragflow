# 线上统计：湘潭中心医院-LWPI-38岁(1).pdf

## 基本信息

- 文件：`湘潭中心医院-LWPI-38岁(1).pdf`
- 大小：4697.2 KB
- PDF 总页数：-
- doc_id：`66d23528859b11f1bb8027103a248952`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：10  orm_synced：True
- 处理耗时(服务端)：410.6864s  脚本耗时：414.6s
- 重解析前快照（无基线结果）：chunk_count=8 run=DONE clinical 类型记录数={'LabReport': 4, 'OutpatientRecord': 1, 'PrescriptionRecord': 3}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | b6d66fd5 | 1 | 1-1 | 处方笺 性别：男 女 年龄：38岁 地址/电话： 年9月5日 诊断：类风湿性关节 |
| 2 | 3b80e2b2 | 1 | 8-8 | 宁乡市坝塘镇保安村邱意文医疗点 科室：全科 性别：女 年龄：39岁 诊断：类风湿 |
| 3 | 1d4fdc8d | 1 | 9-9 | 门诊 宁乡市坝塘镇保安村邱意文医疗点 科室：儿科 性别：女 年龄：38岁 诊断： |
| 4 | 7d2d75c0 | 1 | 10-10 | 宁乡市坝塘镇保安村邱意文医疗点 性别：女 年龄：38 日期：2023年9月5日  |
| 5 | 454afc5e | 1 | 3-3 | <table><tr><td>尿素</td><td>None</td><td>8 |
| 6 | 1f18316d | 1 | 4-4 | <table><tr><td>白细胞</td><td>WBC</td><td>8 |
| 7 | d3d98a5c | 1 | 5-5 | <table><tr><td>类风湿因子</td><td>RF</td><td> |
| 8 | e3b55a78 | 1 | 6-6 | <table><tr><td>血沉（仪器法）</td><td>ESR</td>< |
| 9 | ff0b2d6f | 1 | 2-2 | <table><tr><td>白细胞</td><td>WBC</td><td>9 |
| 10 | 9edc7574 | 1 | 7-7 | <table><tr><td>超敏C反应蛋白</td><td>hsCRP</td |

- chunks 总数：10
- 各 chunk 页数合计（含跨页重复）：10
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
- 覆盖页数：10 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| LabReport | 检验报告 | 6 | 6 | ✅ |
| OutpatientRecord | 门诊 | 1 | 1 | ✅ |
| PrescriptionRecord | 处方 | 3 | 3 | ✅ |

- 判定：✅ 全部类型匹配
