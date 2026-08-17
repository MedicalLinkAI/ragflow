# 线上统计：WKQI+63岁男+肺鳞癌.pdf

## 基本信息

- 文件：`WKQI+63岁男+肺鳞癌.pdf`
- 大小：4021.3 KB
- PDF 总页数：-
- doc_id：`c99014da7b8e11f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：10  orm_synced：True
- 处理耗时(服务端)：253.73755s  脚本耗时：259.0s
- 重解析前快照（无基线结果）：chunk_count=10 run=DONE clinical 类型记录数={'ExaminationReport': 2, 'AdmissionRecord': 1, 'LabReport': 7}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | ad56f226 | 3 | 1-3 | 过敏史：无 肿瘤科一病区T第1次入院记录 主 诉：咳嗽、咳痰2年余，确诊肺癌3月 |
| 2 | 2912cea8 | 1 | 11-11 | 沈丘县人民医院 病理检查报告单 病理号：B20257205 姓名：王克强 性别： |
| 3 | fe4e99ce | 1 | 12-12 | 沈丘县人民医院 CT诊断报告单 微信扫一扫获取电子胶片和报告 病人号P01853 |
| 4 | 879978e8 | 1 | 5-5 | <table><tr><td>三碘甲状腺原氨酸</td><td>TOTT3</t |
| 5 | 55a543e7 | 1 | 6-6 | <table><tr><td>钾</td><td>K</td><td>4.57< |
| 6 | 951a72a4 | 1 | 10-10 | <table><tr><td>尿胆原</td><td>UBG</td><td>正 |
| 7 | 75115863 | 1 | 4-4 | <table><tr><td>肿瘤相关抗原72-4</td><td>CA72-4 |
| 8 | 8ed600b9 | 1 | 7-7 | <table><tr><td>降钙素原</td><td>PCT</td><td> |
| 9 | 3f118a69 | 1 | 8-8 | <table><tr><td>凝血酶原时间</td><td>PT</td><td |
| 10 | 88a976a5 | 1 | 9-9 | <table><tr><td>*★白细胞计数</td><td>WBC</td>< |

- chunks 总数：10
- 各 chunk 页数合计（含跨页重复）：12
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]`
- 覆盖页数：12 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 1 | ✅ |
| ExaminationReport | 检查报告 | 2 | 2 | ✅ |
| LabReport | 检验报告 | 7 | 7 | ✅ |

- 判定：✅ 全部类型匹配
