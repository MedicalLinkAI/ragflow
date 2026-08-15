# 线上统计：LBZH，男，63岁，胃癌一线(1).pdf

## 基本信息

- 文件：`LBZH，男，63岁，胃癌一线(1).pdf`
- 大小：27790.0 KB
- PDF 总页数：-
- doc_id：`f77057f0960c11f1abb555ceeebece40`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：7  orm_synced：True
- 处理耗时(服务端)：897.0087s  脚本耗时：901.3s
- 重解析前快照（无基线结果）：chunk_count=7 run=DONE clinical 类型记录数={'ExaminationReport': 4, 'AdmissionRecord': 1, 'LabReport': 1, 'OutpatientRecord': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | bd92c59e | 2 | 8-9 | 双侧颈部4区探及数个淋巴结，大者分别约1.7cm×1.2cm（左）、1.6cm× |
| 2 | 51c1b9e6 | 1 | 10-10 | 浏览影像报告文件 检查(检验)结果比较 影像分析处理 检查部位名称 检查报告 影 |
| 3 | c0d09f1d | 1 | 11-11 | 58 未F 863 已F 76 已F 病例库 病理会诊 姓名 性别 男 住院号  |
| 4 | 32ef4c17 | 2 | 11-12 | 报告状态 已审核 姓名 性别男 年龄01岁 床号 送检单位本院 送检科室 收到日 |
| 5 | c8de19ba | 5 | 13-17 | 29.11.11.73 临时用户 福建省肿瘤医院病历记录 姓名 入院记录 姓 出 |
| 6 | e34a4ce1 | 3 | 18-20 | 2026-03-24 15:16 于2024-09-02以'进行性吞咽困难2个月 |
| 7 | c4f736b5 | 7 | 1-7 | <table><tr><td>白蛋白</td><td>ALB</td><td>3 |

- chunks 总数：7
- 各 chunk 页数合计（含跨页重复）：21
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]`
- 覆盖页数：20 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| DischargeRecord | 出院 | 1 | 1 | ✅ |
| ExaminationReport | 检查报告 | 4 | 4 | ✅ |
| LabReport | 检验报告 | 1 | 1 | ✅ |
| OutpatientRecord | 门诊 | 1 | 1 | ✅ |

- 判定：✅ 全部类型匹配
