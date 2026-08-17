# 线上统计：06-临沂人民-LSPI，后线肺癌，方穹招募.pdf

## 基本信息

- 文件：`06-临沂人民-LSPI，后线肺癌，方穹招募.pdf`
- 大小：6420.2 KB
- PDF 总页数：-
- doc_id：`15bf5b9494e011f1bd9827cf206dfa2d`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：9  orm_synced：True
- 处理耗时(服务端)：352.51898s  脚本耗时：368.6s
- 重解析前快照（无基线结果）：chunk_count=9 run=DONE clinical 类型记录数={'ExaminationReport': 3, 'DischargeRecord': 1, 'LabReport': 3, 'OutpatientRecord': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 72e83788 | 1 | 2-2 | 彩色病理图文报告 姓名： 性别：女 年龄：59岁 收到日期：2025-10-24 |
| 2 | 1c2c6065 | 1 | 3-3 | CT检查报告单 患者编号: 扫描日期: 1/13/2026 姓名: 性别:女 年 |
| 3 | 76e4bfcd | 1 | 4-4 | CT检查报告单 患者编号： 放射编号： 扫描日期：2/26/2026 姓名： 性 |
| 4 | bc3fc466 | 2 | 5-6 | 科室：呼吸与危重症医学科 姓名： 出院记录 女，59岁，主因“确诊右肺腺癌5年” |
| 5 | 586f1f3b | 1 | 7-7 | 科室：呼吸内科 姓名： 门诊病历号： [初诊病历记录(门诊放化疗患者专用)] 就 |
| 6 | 95fd0e45 | 2 | 10-12 | <table><tr><td>EGFR c.2369C>T (p.T790M)< |
| 7 | be184af7 | 1 | 13-13 | <table><tr><td>尿液分析-酸碱度</td><td>PH</td>< |
| 8 | 2ec87768 | 1 | 15-15 | <table><tr><td>白细胞计数</td><td>WBC</td><td |
| 9 | f773ad68 | 1 | 14-14 | <table><tr><td>血清丙氨酸氨基转移酶测定</td><td>ALT< |

- chunks 总数：9
- 各 chunk 页数合计（含跨页重复）：11
- 页码并集：`[2, 3, 4, 5, 6, 7, 10, 12, 13, 14, 15]`
- 覆盖页数：11 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| DischargeRecord | 出院 | 1 | 1 | ✅ |
| ExaminationReport | 检查报告 | 3 | 3 | ✅ |
| LabReport | 检验报告 | 4 | 4 | ✅ |
| OutpatientRecord | 门诊 | 1 | 1 | ✅ |

- 判定：✅ 全部类型匹配
