# 线上统计：LYNO 男 62.pdf

## 基本信息

- 文件：`LYNO 男 62.pdf`
- 大小：10256.7 KB
- PDF 总页数：-
- doc_id：`db07974478f811f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：8  orm_synced：True
- 处理耗时(服务端)：418.03836s  脚本耗时：423.5s
- 重解析前快照（无基线结果）：chunk_count=7 run=DONE clinical 类型记录数={'LabReport': 4, 'ExaminationReport': 2, 'DischargeRecord': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 9604881c | 1 | 2-2 | 病理检查补充报告单 病理号: 姓 性别:男 年龄:62岁 出生日期: 送检单 病 |
| 2 | 92757ca9 | 1 | 3-3 | 姓名 性别：男 出生日期：1905年11月28日 申请科室： 检查项目：CT胸部 |
| 3 | 3f3d750f | 1 | 4-4 | 性别： ID号： 内镜编 科 塘 电 临床诊断：位性病变（右肿门） 吸烟史：有  |
| 4 | 417da535 | 1 | 6-6 | \begin{tabular}{cccccc} 报告时间: 2026-03-11 |
| 5 | 045f3d79 | 2 | 8-9 | 入院时间：2026-03-12 14:28 出院时间：2026-03-14 09 |
| 6 | 1701e585 | 1 | 7-7 | <table><tr><td>NSE</td><td>None</td><td> |
| 7 | 3ce48129 | 1 | 5-5 | <table><tr><td>血小板计数</td><td>None</td><t |
| 8 | 1add7dba | 1 | 6-6 | <table><tr><td>HIV抗原/抗体联合检测</td><td>None |

- chunks 总数：8
- 各 chunk 页数合计（含跨页重复）：9
- 页码并集：`[2, 3, 4, 5, 6, 7, 8, 9]`
- 覆盖页数：8 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| DischargeRecord | 出院 | 1 | 0 | ❌ |
| ExaminationReport | 检查报告 | 3 | 0 | ❌ |
| LabReport | 检验报告 | 4 | 0 | ❌ |

- 判定：❌ 不匹配类型: DischargeRecord, ExaminationReport, LabReport
