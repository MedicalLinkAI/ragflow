# 线上统计：LQLI 男 57 鳞癌.pdf

## 基本信息

- 文件：`LQLI 男 57 鳞癌.pdf`
- 大小：10228.9 KB
- PDF 总页数：-
- doc_id：`695fc5f679b811f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：10  orm_synced：True
- 处理耗时(服务端)：300.1148s  脚本耗时：305.7s
- 重解析前快照（无基线结果）：chunk_count=8 run=DONE clinical 类型记录数={'ExaminationReport': 4, 'LabReport': 3, 'DischargeRecord': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 69cf1cab | 1 | 1-1 | 病理检查补充报告单 病理号: 姓名: 性别: 出生日期: 送检单位: 病区: 病 |
| 2 | 0217df4a | 1 | 2-2 | 检查 检查日期：2026年04月17日 10:11:39 姓名： 性别： 年龄： |
| 3 | 0ebb5a0a | 1 | 3-3 | 及纵隔）薄层平扫增强报告单 临床诊断：肺病变 检查方法： CT胸部（肺及纵隔）薄 |
| 4 | 06f10e22 | 1 | 4-4 | 病人i 住院号 床位号 科 姓名 性别：男 年龄：57岁 心率：70 bpm P |
| 5 | 648eb0ab | 3 | 5-7 | 出院记录 姓名： 出生日期：1968-07-15 病人 科室： 床号：48 住院 |
| 6 | 859d2f7e | 1 | 12-12 | 项目：PD-L1免疫组化检测 技术：免疫组化 试剂：Dako 22C3 结果 质 |
| 7 | 6bb6d95d | 1 | 9-9 | <table><tr><td>HIV抗原/抗体联合检测</td><td>6522 |
| 8 | 3f42b018 | 1 | 10-10 | <table><tr><td>凝血酶原百分率</td><td>77</td><t |
| 9 | e7e66494 | 1 | 8-8 | <table><tr><td>尿素</td><td>None</td><td>3 |
| 10 | b52fddcb | 1 | 11-11 | <table><tr><td>中性粒细胞分类计数</td><td>5009</t |

- chunks 总数：10
- 各 chunk 页数合计（含跨页重复）：12
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]`
- 覆盖页数：12 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| DischargeRecord | 出院 | 1 | 0 | ❌ |
| ExaminationReport | 检查报告 | 5 | 0 | ❌ |
| LabReport | 检验报告 | 4 | 0 | ❌ |

- 判定：❌ 不匹配类型: DischargeRecord, ExaminationReport, LabReport
