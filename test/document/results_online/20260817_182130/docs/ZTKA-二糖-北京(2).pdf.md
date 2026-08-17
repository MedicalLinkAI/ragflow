# 线上统计：ZTKA-二糖-北京(2).pdf

## 基本信息

- 文件：`ZTKA-二糖-北京(2).pdf`
- 大小：2573.5 KB
- PDF 总页数：-
- doc_id：`4fe9672078f111f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：4  orm_synced：True
- 处理耗时(服务端)：168.64072s  脚本耗时：171.5s
- 重解析前快照（无基线结果）：chunk_count=6 run=DONE clinical 类型记录数={'OutpatientRecord': 1, 'MedicationRecord': 2, 'PrescriptionRecord': 2, 'LabReport': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 94ae514e | 1 | 1-1 | 全科医疗诊疗记录 姓名 性别:男 年龄:30岁 档案号 2025-02-01 崔 |
| 2 | a8086d2b | 1 | 2-2 | 已收费,开具医生:李瑞林,处方日期:2025-02-01 11:46:29,诊断 |
| 3 | fa1ad26e | 1 | 3-3 | 崔村社区卫生服务中心处方笺 西医普通 医保处方 定点医疗机构编码: 141100 |
| 4 | d3e91832 | 1 | 4-4 | <table><tr><td>糖化血红蛋白A1c</td><td>HbA1c</ |

- chunks 总数：4
- 各 chunk 页数合计（含跨页重复）：4
- 页码并集：`[1, 2, 3, 4]`
- 覆盖页数：4 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| LabReport | 检验报告 | 1 | 1 | ✅ |
| OutpatientRecord | 门诊 | 1 | 1 | ✅ |
| PrescriptionRecord | 处方 | 2 | 2 | ✅ |

- 判定：✅ 全部类型匹配
