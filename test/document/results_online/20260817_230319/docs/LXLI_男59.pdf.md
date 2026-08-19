# 线上统计：LXLI 男59.pdf

## 基本信息

- 文件：`LXLI 男59.pdf`
- 大小：12960.6 KB
- PDF 总页数：-
- doc_id：`1236eaa878f911f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：12  orm_synced：True
- 处理耗时(服务端)：307.04807s  脚本耗时：311.7s
- 重解析前快照（无基线结果）：chunk_count=12 run=DONE clinical 类型记录数={'LabReport': 5, 'ExaminationReport': 6, 'DischargeRecord': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | f162894e | 1 | 1-1 | 湖南 HR 姓名 龄:59岁 申请科室: 病人 检查项目:层平扫增强,CT 及肾 |
| 2 | 7dd7e9a6 | 1 | 2-2 | 年龄：59岁 性别：男 临床诊断： 检查项目：全身骨SPECT/CT显像 采集方 |
| 3 | cc78bfe8 | 2 | 3-4 | 姓名 申请 检查项目：MR颅脑平扫增强+薄层成像 临床诊断：肺病变（CA? 炎性 |
| 4 | 2e3d5a8e | 1 | 4-4 | 心电图报告单 姓名： P-R间期:124 ms 诊断：1、窦性心律 性别：男 Q |
| 5 | a24866ad | 2 | 5-6 | 入院时间：2026-04-03 08:14 出院时间：2026-04-09 15 |
| 6 | 7af4b0e4 | 1 | 12-12 | 病 号 2084303 送检科室 信息 送检单 位 本院 标本名称 EBUS-T |
| 7 | 11aa8cf0 | 2 | 12-13 | 打印 姓名 性别：男 病 院号 送检 信息 送检单 位 本院 送检医生 标本名称 |
| 8 | 7a8bea6c | 1 | 9-9 | <table><tr><td>总蛋白</td><td>None</td><td> |
| 9 | da5a650f | 1 | 7-7 | <table><tr><td>真菌培养及鉴定</td><td>None</td> |
| 10 | 7efe07a1 | 1 | 8-8 | <table><tr><td>HBsAg检测(化学发光法)</td><td>No |
| 11 | d5f68caa | 1 | 10-10 | <table><tr><td>凝血酶原时间</td><td>None</td>< |
| 12 | 18a92f58 | 1 | 11-11 | <table><tr><td>白细胞计数</td><td>None</td><t |

- chunks 总数：12
- 各 chunk 页数合计（含跨页重复）：15
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]`
- 覆盖页数：13 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| DischargeRecord | 出院 | 1 | 1 | ✅ |
| ExaminationReport | 检查报告 | 6 | 6 | ✅ |
| LabReport | 检验报告 | 5 | 5 | ✅ |

- 判定：✅ 全部类型匹配
