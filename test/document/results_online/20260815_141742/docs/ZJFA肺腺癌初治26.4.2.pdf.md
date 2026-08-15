# 线上统计：ZJFA肺腺癌初治26.4.2.pdf

## 基本信息

- 文件：`ZJFA肺腺癌初治26.4.2.pdf`
- 大小：23117.5 KB
- PDF 总页数：-
- doc_id：`e753d7de78f711f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：5  orm_synced：True
- 处理耗时(服务端)：614.8879s  脚本耗时：620.2s
- 重解析前快照（无基线结果）：chunk_count=6 run=DONE clinical 类型记录数={'AdmissionRecord': 1, 'LabReport': 2, 'ExaminationReport': 2, 'DischargeRecord': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | d221d13b | 2 | 1-2 | 签 直接打印 操作记录 聊城市人民医院 入院记录 姓名： 性别：男 年龄：58岁 |
| 2 | 640dcf85 | 3 | 2-4 | 2026-4-2 聊城市人民医院 出院记录 姓名： 性别：男 年龄：58岁 住院 |
| 3 | a6dd42eb | 1 | 5-5 | 技术参数: 聊城市人民医院 CT影像检查报告 流水号 影像号 姓名 性别:男 年 |
| 4 | c8b756d5 | 1 | 6-6 | 院 病理报告 聊城市人民医院 病理检查补充报告单 病理号: 姓名: 性别: 男  |
| 5 | 73039a33 | 2 | 7-8 | <table><tr><td>白细胞计数</td><td>None</td><t |

- chunks 总数：5
- 各 chunk 页数合计（含跨页重复）：9
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8]`
- 覆盖页数：8 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 0 | ❌ |
| DischargeRecord | 出院 | 1 | 0 | ❌ |
| ExaminationReport | 检查报告 | 2 | 0 | ❌ |
| LabReport | 检验报告 | 1 | 0 | ❌ |

- 判定：❌ 不匹配类型: AdmissionRecord, DischargeRecord, ExaminationReport, LabReport
