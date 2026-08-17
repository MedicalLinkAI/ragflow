# 线上统计：LIQU高血糖郑州.pdf

## 基本信息

- 文件：`LIQU高血糖郑州.pdf`
- 大小：9368.0 KB
- PDF 总页数：-
- doc_id：`39b727fe948e11f18f67cb8e99b562ad`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：23  orm_synced：True
- 处理耗时(服务端)：203.85643s  脚本耗时：207.2s
- 备注：progress_msg 未找到 SmartSplitter 类型日志。 
- 重解析前快照（无基线结果）：chunk_count=23 run=DONE clinical 类型记录数={'OutpatientRecord': 2, 'LabReport': 8, 'MedicationRecord': 3, 'PrescriptionRecord': 1, 'ExaminationReport': 4}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 864e4d9d | 1 | 1-1 | 郑州市金水区国基路沙门社区卫生服务中心门诊电子病历 No: 2024111600 |
| 2 | eb44c929 | 1 | 5-5 | 金水区国基路沙门社区卫生服务中心 Jinshui Gaoji Street Sh |
| 3 | 9b70450a | 1 | 5-5 | ◆泌尿系彩超（男） (彩超检查) 检查医生：高培利 项目 结果 单位 双肾 双肾 |
| 4 | 59169813 | 1 | 5-5 | ◆心电图12号 (心电图) 检查医生：李天柱 项目 结果 单位 心电图 T波异常 |
| 5 | 094d49c9 | 1 | 5-5 | ◆胸部正位检查DR(不出片) (DR拍片) 检查医生：申静 项目 结果 单位 胸 |
| 6 | b1a9c772 | 1 | 7-7 | 越人大药房 祝您身体健康 日期：2025-04-02 NO：1.2468223  |
| 7 | cfc9d11e | 1 | 8-8 | 越人大药房 祝您身体健康 日期：2025-02-13 NO：1.2467129  |
| 8 | 587c3567 | 1 | 9-9 | 郑州市金水区国基路沙门社区卫生服务中心门诊电子病历 No: 2025041700 |
| 9 | 3244123a | 1 | 10-10 | 郑州市金水区国基路沙门社区 卫生服务中心处方笺 医保证号: 费别:自费 门诊号: |
| 10 | 6820b8d3 | 1 | 11-11 | No 20250417000C 郑州市金水区国基路沙门社区 自费及其他 No 2 |
| 11 | d9d63041 | 1 | 3-3 | <table><tr><td>乙型肝炎病毒表面抗原</td><td>HBsAg< |
| 12 | d014c0b3 | 1 | 6-6 | <table><tr><td>空腹血糖</td><td>None</td><td |
| 13 | 7876693c | 1 | 12-12 | <table><tr><td>糖化血红蛋白</td><td>None</td>< |
| 14 | 5787d4b6 | 1 | 2-2 | <table><tr><td>糖化血红蛋白</td><td>2461</td>< |
| 15 | 5974ad26 | 1 | 6-6 | <table><tr><td>红细胞平均分布宽度标准差</td><td>None |
| 16 | 2ff03bc4 | 1 | 6-6 | <table><tr><td>尿酸</td><td>None</td><td>2 |
| 17 | 70d25904 | 1 | 6-6 | <table><tr><td>丙氨酸氨基转移酶</td><td>None</td |
| 18 | ddb33272 | 1 | 6-6 | <table><tr><td>酸碱度</td><td>None</td><td> |

- chunks 总数：18
- 各 chunk 页数合计（含跨页重复）：18
- 页码并集：`[1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12]`
- 覆盖页数：11 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| ExaminationReport | 检查报告 | 0 | 4 | ❌ |
| LabReport | 检验报告 | 0 | 8 | ❌ |
| MedicationRecord | 购药 | 0 | 3 | ❌ |
| OutpatientRecord | 门诊 | 0 | 2 | ❌ |
| PrescriptionRecord | 处方 | 0 | 1 | ❌ |

- 判定：❌ 不匹配类型: ExaminationReport, LabReport, MedicationRecord, OutpatientRecord, PrescriptionRecord
