# 线上统计：糖尿病患者WGA-济南.pdf

## 基本信息

- 文件：`糖尿病患者WGA-济南.pdf`
- 大小：2268.4 KB
- PDF 总页数：-
- doc_id：`2034315e7e6911f1af97e3985ba7f8da`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：5  orm_synced：True
- 处理耗时(服务端)：180.7441s  脚本耗时：182.0s
- 重解析前快照（无基线结果）：chunk_count=5 run=DONE clinical 类型记录数={'LabReport': 2, 'OutpatientRecord': 2, 'MedicationRecord': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 768f76ba | 2 | 1-2 | 电子发票(普通发票) 国家税务总局 山东省税务局 发票号码：2537200000 |
| 2 | c4716a49 | 1 | 3-3 | 葡萄园社区卫生服务站病历信息 门诊编号：2503210006 姓名： 性别：男  |
| 3 | 643db746 | 1 | 4-4 | 兰园社区卫生服务站病历信息 门诊编号：2409160009 姓名： 性别：男 科 |
| 4 | 6c3c8716 | 1 | 5-5 | <table><tr><td>糖化血红蛋白</td><td>None</td>< |
| 5 | 3223aa8b | 1 | 6-6 | <table><tr><td>糖化血红蛋白</td><td>None</td>< |

- chunks 总数：5
- 各 chunk 页数合计（含跨页重复）：6
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
