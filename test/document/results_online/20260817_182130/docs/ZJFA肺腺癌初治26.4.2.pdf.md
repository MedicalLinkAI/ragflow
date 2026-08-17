# 线上统计：ZJFA肺腺癌初治26.4.2.pdf

## 基本信息

- 文件：`ZJFA肺腺癌初治26.4.2.pdf`
- 大小：23117.5 KB
- PDF 总页数：-
- doc_id：`e753d7de78f711f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：6  orm_synced：True
- 处理耗时(服务端)：497.63193s  脚本耗时：500.8s
- 重解析前快照（无基线结果）：chunk_count=5 run=DONE clinical 类型记录数={'AdmissionRecord': 1, 'LabReport': 1, 'DischargeRecord': 1, 'ExaminationReport': 2}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | bab38898 | 2 | 1-2 | 姓名： 性别：男 年龄：58岁 住院号： 姓名： 性别：男 年龄：58岁 民族： |
| 2 | b571f99e | 3 | 2-4 | 2026-4-2 聊城市人民医院 出院记录 姓名： 性别：男 年龄：58岁 住院 |
| 3 | f10a36e6 | 1 | 5-5 | 技术参数: 聊城市人民医院 CT影像检查报告 影像号 姓名 性别:男 年龄:58 |
| 4 | a071c23b | 1 | 6-6 | 院 病理报告 聊城市人民医院 病理检查补充报告单 病理号: 姓名: 性别: 男  |
| 5 | 0e70e5a0 | 1 | 7-7 | <table><tr><td>白细胞计数</td><td>None</td><t |
| 6 | 2c6a7c33 | 1 | 8-8 | <table><tr><td>丙氨酸氨基转移酶</td><td>None</td |

- chunks 总数：6
- 各 chunk 页数合计（含跨页重复）：9
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8]`
- 覆盖页数：8 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 1 | ✅ |
| DischargeRecord | 出院 | 1 | 1 | ✅ |
| ExaminationReport | 检查报告 | 2 | 2 | ✅ |
| LabReport | 检验报告 | 2 | 2 | ✅ |

- 判定：✅ 全部类型匹配
