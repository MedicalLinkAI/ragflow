# 线上统计：徐州-LIYE-小肺-方穹推荐706-Ia期.pdf

## 基本信息

- 文件：`徐州-LIYE-小肺-方穹推荐706-Ia期.pdf`
- 大小：2804.8 KB
- PDF 总页数：-
- doc_id：`14e1a4847eb011f1af97e3985ba7f8da`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：9  orm_synced：True
- 处理耗时(服务端)：559.1923s  脚本耗时：560.3s
- 重解析前快照（无基线结果）：chunk_count=8 run=DONE clinical 类型记录数={'ExaminationReport': 4, 'DischargeRecord': 1, 'LabReport': 2, 'OutpatientRecord': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | eb9bc3cf | 4 | 1-4 | 2025.5.21确诊小细胞肺癌 2025.5.28-2025.7.16 依托泊 |
| 2 | bcfbb0d6 | 1 | 5-5 | 河北省人民医院 病理检查报告单 病理号 姓名: 性别: 女 年龄: 74岁 送检 |
| 3 | 41e501ce | 2 | 5-6 | 住院病历 河北省人民医院 病理检查补充报告单 病理号: 姓名: 性别: 女 年龄 |
| 4 | 347e5133 | 1 | 7-7 | 南京鼓楼医院云胶片 ◎ 南京鼓楼医院 南京大学医学院附属鼓楼医院 影像检查诊断报 |
| 5 | 4e7a1c44 | 4 | 8-11 | 南京鼓楼医院云胶片 女/75岁 设备类型 CT 患者类型 无 检查项目 [CT平 |
| 6 | 51101381 | 1 | 12-12 | 南京鼓楼医院 南京大学医学院附属鼓楼医院 互联网医院 门诊病历 姓名: 性别:女 |
| 7 | 5cabc9ee | 1 | 13-13 | <table><tr><td>白细胞计数</td><td>None</td><t |
| 8 | 2639d2d3 | 1 | 14-14 | <table><tr><td>丙氨酸氨基转移酶</td><td>None</td |
| 9 | af402a9e | 1 | 14-14 | <table><tr><td>C反应蛋白</td><td>None</td><t |

- chunks 总数：9
- 各 chunk 页数合计（含跨页重复）：16
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]`
- 覆盖页数：14 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| DischargeRecord | 出院 | 1 | 1 | ✅ |
| ExaminationReport | 检查报告 | 4 | 4 | ✅ |
| LabReport | 检验报告 | 3 | 3 | ✅ |
| OutpatientRecord | 门诊 | 1 | 1 | ✅ |

- 判定：✅ 全部类型匹配
