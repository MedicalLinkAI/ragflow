# 线上统计：湘潭中心医院-LWPI-38岁(1).pdf

## 基本信息

- 文件：`湘潭中心医院-LWPI-38岁(1).pdf`
- 大小：4697.2 KB
- PDF 总页数：-
- doc_id：`66d23528859b11f1bb8027103a248952`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：8  orm_synced：True
- 处理耗时(服务端)：178.7615s  脚本耗时：182.0s
- 重解析前快照（无基线结果）：chunk_count=10 run=DONE clinical 类型记录数={'LabReport': 6, 'OutpatientRecord': 1, 'PrescriptionRecord': 3}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 810d467a | 1 | 1-1 | 处方笺 性别：男 女 年龄：38岁 地址/电话： 年9月5日 诊断：类风湿性关节 |
| 2 | 3b80e2b2 | 1 | 8-8 | 宁乡市坝塘镇保安村邱意文医疗点 科室：全科 性别：女 年龄：39岁 诊断：类风湿 |
| 3 | 1d4fdc8d | 1 | 9-9 | 门诊 宁乡市坝塘镇保安村邱意文医疗点 科室：儿科 性别：女 年龄：38岁 诊断： |
| 4 | 14b12467 | 1 | 10-10 | 宁乡市坝塘镇保安村邱意文医疗点 性别：女 年龄：38 日期：2023年9月5日  |
| 5 | 22959af4 | 1 | 3-3 | <table><tr><td>尿素</td><td>None</td><td>8 |
| 6 | 1f18316d | 1 | 4-4 | <table><tr><td>白细胞</td><td>WBC</td><td>8 |
| 7 | 137658b9 | 1 | 2-2 | <table><tr><td>白细胞</td><td>WBC</td><td>9 |
| 8 | fabb9891 | 3 | 5-7 | <table><tr><td>类风湿因子</td><td>RF</td><td> |

- chunks 总数：8
- 各 chunk 页数合计（含跨页重复）：10
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
- 覆盖页数：10 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| LabReport | 检验报告 | 4 | 4 | ✅ |
| OutpatientRecord | 门诊 | 1 | 1 | ✅ |
| PrescriptionRecord | 处方 | 3 | 3 | ✅ |

- 判定：✅ 全部类型匹配
