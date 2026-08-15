# 线上统计：LJLA-女-类风湿-山东菏泽中心.pdf

## 基本信息

- 文件：`LJLA-女-类风湿-山东菏泽中心.pdf`
- 大小：8190.6 KB
- PDF 总页数：-
- doc_id：`513714c87c4e11f18d62dd81525255fa`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：16  orm_synced：True
- 处理耗时(服务端)：559.06757s  脚本耗时：563.0s
- 重解析前快照（无基线结果）：chunk_count=17 run=DONE clinical 类型记录数={'OutpatientRecord': 7, 'PrescriptionRecord': 6, 'MedicationRecord': 2, 'LabReport': 2}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | a9162f7f | 1 | 1-1 | 安徽医科大学第一附属医院 THE FIRST AFFILIATED HOSPIT |
| 2 | 87aa8c9e | 1 | 2-2 | 安徽医科大学第一附属医院 取药单 取药窗口:门诊药房窗二 姓名: 性别:女 年龄 |
| 3 | c7fdc4da | 1 | 4-4 | 安徽医科大学第一附属医院 THE FIRST AFFILIATED HOSPIT |
| 4 | a00f7b3f | 1 | 5-5 | 安徽医科大学第一附属医院 取药单 取药窗口:门诊药房窗二 姓名 性别:女 年龄: |
| 5 | d10cc15e | 1 | 7-7 | 安徽医科大学第一附属医院 THE FIRST AFFILIATED HOSPIT |
| 6 | c3fd6a18 | 1 | 8-8 | 安徽医科大学第一附属医院 取药单 取药窗口:门诊药房窗三 姓名 性别:女 年龄: |
| 7 | cea61fd3 | 1 | 10-10 | 安徽医科大学第一附属医院 THE FIRST AFFILIATED HOSPIT |
| 8 | 43160c2f | 1 | 11-11 | 安徽医科大学第一附属医院 取药单 取药窗口:门诊药房窗二 姓名： 性别：女 年龄 |
| 9 | df3f4fe6 | 1 | 13-13 | 安徽医科大学第一附属医院 THE FIRST AFFILIATED HOSPIT |
| 10 | 8eddff39 | 1 | 14-14 | 安徽医科大学第一附属医院 取药单 取药窗口:门诊药房窗二 姓名: 性别:女 年龄 |
| 11 | 395d08fe | 1 | 16-16 | 安徽医科大学第一附属医院 THE FIRST AFFILIATED HOSPIT |
| 12 | 277a30fe | 1 | 17-17 | 安徽医科大学第一附属医院 取药单 取药窗口:门诊药房窗三 姓名: 性别:女 年龄 |
| 13 | 8d432823 | 1 | 19-19 | 安徽医科大学第一附属医院 THE FIRST AFFILIATED HOSPIT |
| 14 | 3f579a20 | 1 | 20-20 | 丰华大药房 售药凭证 日期：2024-11-13 19:08:25 单据号：24 |
| 15 | fe10d333 | 1 | 21-21 | 丰华大药房 售药凭证 日期：2024-08-05 18:18:19 单据号：24 |
| 16 | 123c7f2f | 2 | 22-23 | <table><tr><td>WBC</td><td>None</td><td> |

- chunks 总数：16
- 各 chunk 页数合计（含跨页重复）：17
- 页码并集：`[1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 21, 22, 23]`
- 覆盖页数：17 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| LabReport | 检验报告 | 1 | 0 | ❌ |
| MedicationRecord | 购药 | 2 | 0 | ❌ |
| OutpatientRecord | 门诊 | 7 | 0 | ❌ |
| PrescriptionRecord | 处方 | 6 | 0 | ❌ |

- 判定：❌ 不匹配类型: LabReport, MedicationRecord, OutpatientRecord, PrescriptionRecord
