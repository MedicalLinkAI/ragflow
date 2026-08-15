# 线上统计：LGLA肺鳞癌初治-天津.pdf

## 基本信息

- 文件：`LGLA肺鳞癌初治-天津.pdf`
- 大小：10247.0 KB
- PDF 总页数：-
- doc_id：`ab9e1adc7b9111f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：13  orm_synced：True
- 处理耗时(服务端)：349.81934s  脚本耗时：352.2s
- 重解析前快照（无基线结果）：chunk_count=11 run=DONE clinical 类型记录数={'AdmissionRecord': 1, 'LabReport': 7, 'ExaminationReport': 2, 'DischargeRecord': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | d4db1329 | 1 | 1-1 | 华北理工大学附属医院 病理检查报告单 姓名： 性别：男 年龄： 申请科室：肿瘤放 |
| 2 | 87f431a0 | 5 | 2-6 | 华北理工大学附属医院 NORTH CHINA UNIVERSITY OF SCI |
| 3 | 1ffece8f | 2 | 7-8 | 华北理工大学附属医院 NORTH CHINA UNIVERSITY OF SCI |
| 4 | 591ec1ea | 1 | 9-9 | 姓名 性别：男 年龄：71岁 检查日期：2025-12-10 申请科室：肿瘤放化 |
| 5 | 724cca1d | 1 | 12-12 | \begin{tabular}{llll} 报告时间: 2025-12-09 \ |
| 6 | c48bca19 | 1 | 10-10 | <table><tr><td>总T细胞(CD3+)百分比</td><td>CD3 |
| 7 | 7a754894 | 1 | 11-11 | <table><tr><td>血浆凝血酶原时间</td><td>PT</td>< |
| 8 | 2b050a2f | 1 | 12-12 | <table><tr><td>总蛋白</td><td>TP</td><td>76 |
| 9 | 414f3c64 | 1 | 15-15 | <table><tr><td>乙型肝炎病毒表面抗原</td><td>HBsAg< |
| 10 | dbb0e80c | 1 | 16-16 | <table><tr><td>人免疫缺陷病毒(1+2)抗体[CLIA]</td> |
| 11 | 4ed8b9ff | 1 | 12-12 | <table><tr><td>总胆固醇</td><td>CHOL</td><td |
| 12 | b41b4c3d | 1 | 13-13 | <table><tr><td>白细胞</td><td>WBC</td><td>6 |
| 13 | f11419a9 | 1 | 14-14 | <table><tr><td>癌胚抗原</td><td>CEA</td><td> |

- chunks 总数：13
- 各 chunk 页数合计（含跨页重复）：18
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]`
- 覆盖页数：16 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 0 | ❌ |
| DischargeRecord | 出院 | 1 | 0 | ❌ |
| ExaminationReport | 检查报告 | 2 | 0 | ❌ |
| LabReport | 检验报告 | 9 | 0 | ❌ |

- 判定：❌ 不匹配类型: AdmissionRecord, DischargeRecord, ExaminationReport, LabReport
