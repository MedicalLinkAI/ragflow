# 线上统计：哮喘-YHHU-男-44岁-湘雅医院.pdf

## 基本信息

- 文件：`哮喘-YHHU-男-44岁-湘雅医院.pdf`
- 大小：4816.7 KB
- PDF 总页数：-
- doc_id：`0ff4c94e7ea911f1af97e3985ba7f8da`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：6  orm_synced：True
- 处理耗时(服务端)：499.10446s  脚本耗时：500.5s
- 重解析前快照（无基线结果）：chunk_count=0 run=DONE clinical 类型记录数={'OutpatientRecord': 3, 'PrescriptionRecord': 2, 'ExaminationReport': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 138e69f0 | 1 | 1-1 | 门(急)诊病历 年龄:44岁 性别:男 就诊科室:呼吸与危重症医学科门诊 就诊日 |
| 2 | 3a81f93e | 2 | 2-3 | 门诊(急)诊病历 姓名: 年龄:44岁 性别:男 就诊科室:呼吸与危重症医学科门 |
| 3 | 4958701b | 1 | 4-4 | 长沙德雅医院处方笺 普 处方编号 8002727 费别 科别 皮肤 门诊号 住院 |
| 4 | 56e4fc6d | 1 | 5-5 | 年龄:44岁 性别:男 就诊科室:呼吸与危重症医学科门诊 就诊日期:2024年0 |
| 5 | 46f8fcf4 | 1 | 6-6 | 中南大学湘雅二医院 肺功能检查 试验检查报告 测试号: 姓名: 出生日期: 19 |
| 6 | a8324416 | 1 | 10-10 | 中南大学湘雅二医院 The Second Xiangya Hospital of |

- chunks 总数：6
- 各 chunk 页数合计（含跨页重复）：7
- 页码并集：`[1, 2, 3, 4, 5, 6, 10]`
- 覆盖页数：7 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| ExaminationReport | 检查报告 | 1 | 0 | ❌ |
| OutpatientRecord | 门诊 | 4 | 0 | ❌ |
| PrescriptionRecord | 处方 | 1 | 0 | ❌ |

- 判定：❌ 不匹配类型: ExaminationReport, OutpatientRecord, PrescriptionRecord
