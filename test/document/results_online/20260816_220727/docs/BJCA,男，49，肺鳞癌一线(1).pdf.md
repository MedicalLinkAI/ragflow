# 线上统计：BJCA,男，49，肺鳞癌一线(1).pdf

## 基本信息

- 文件：`BJCA,男，49，肺鳞癌一线(1).pdf`
- 大小：14180.7 KB
- PDF 总页数：-
- doc_id：`14840e4e94f111f1bd9827cf206dfa2d`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：14  orm_synced：True
- 处理耗时(服务端)：656.66547s  脚本耗时：663.8s
- 重解析前快照（无基线结果）：chunk_count=13 run=DONE clinical 类型记录数={'ExaminationReport': 7, 'AdmissionRecord': 1, 'LabReport': 5}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 8357a215 | 3 | 1-3 | 姓名 住址：福建省三明市尤溪县 性别：男 工作单位：/ 年龄：49岁 入院日期： |
| 2 | 7729d291 | 1 | 4-4 | 测量结果: Lved:46.5 mm Lves:28.9 mm La:26.6  |
| 3 | 49057c88 | 1 | 5-5 | 性别：男 年龄：49岁 门诊号： 检查部位：肺部 检查设备：GE-HD750 流 |
| 4 | b11c6ffa | 1 | 6-6 | 门诊号: 医院: 申请医生 申请科室 检查日期: 2026-03-17 10:5 |
| 5 | 453ee80c | 1 | 7-7 | 检查部位：头颅 检查设备：飞利浦MR9 流水号：0013240580 检查技术： |
| 6 | 116413b2 | 1 | 11-11 | \begin{tabular}{lllllll} 报告时间: 2026-03-1 |
| 7 | a2505c7f | 1 | 12-12 | 病案号: 11诊号:1K3392539b3 血型:FEI/CI独/业冰(111) |
| 8 | 7fbf63cc | 1 | 13-13 | 福建医科大学附属协和医院 肺功能检查报告单 姓名： 年龄：49 Years 性别 |
| 9 | 8e349f6a | 1 | 14-14 | 姓 住院 性别：男 年龄：40岁 送检单位：本院 送检科室：呼吸与危重症医学科  |
| 10 | e973753a | 1 | 9-9 | <table><tr><td>总胆红素</td><td>TBIL</td><td |
| 11 | 5a112d19 | 1 | 9-9 | <table><tr><td>尿素</td><td>UREA</td><td>4 |
| 12 | f651f2ea | 1 | 8-8 | <table><tr><td>乙肝病毒表面抗原</td><td>None</td |
| 13 | 082a2e34 | 1 | 10-10 | <table><tr><td>白细胞计数</td><td>None</td><t |
| 14 | fa1b16ce | 1 | 11-11 | <table><tr><td>凝血酶原时间</td><td>PT</td><td |

- chunks 总数：14
- 各 chunk 页数合计（含跨页重复）：16
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]`
- 覆盖页数：14 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 1 | ✅ |
| ExaminationReport | 检查报告 | 7 | 7 | ✅ |
| LabReport | 检验报告 | 6 | 5 | ❌ |

- 判定：❌ 不匹配类型: LabReport
