# 线上统计：大连-SZRU-食管癌-方穹推荐706-I期（IA期）.pdf

## 基本信息

- 文件：`大连-SZRU-食管癌-方穹推荐706-I期（IA期）.pdf`
- 大小：1822.4 KB
- PDF 总页数：-
- doc_id：`a94970ae75b711f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：12  orm_synced：True
- 处理耗时(服务端)：275.83453s  脚本耗时：279.7s
- 重解析前快照（无基线结果）：chunk_count=12 run=DONE clinical 类型记录数={'ExaminationReport': 5, 'AdmissionRecord': 1, 'LabReport': 5, 'DischargeRecord': 1}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 259028b6 | 3 | 1-3 | 身高169厘米，体重65公斤，没有基础疾病及合并用药，自愿放弃标准治疗 鞍山市肿 |
| 2 | 6653be95 | 1 | 4-4 | 鞍山市肿瘤医院 出院记录 姓名： 性别：女性 年龄：55岁 科室： 床号：8 住 |
| 3 | 1610a556 | 1 | 5-5 | 解放军总医院第一医学中心 PLAGH 病理标本检查报告单 姓名： 性别：女 年龄 |
| 4 | 1fdc840f | 1 | 6-6 | 解放军总医院第一医学中心消化内科医学部 内镜报告单 姓名： 性别：女 检查年龄： |
| 5 | 34539a74 | 1 | 7-7 | 鞍山市肿瘤医院 彩色超声诊断报告单 姓名： 性别：女 年龄：55岁 住院号： 申 |
| 6 | 8aea5ecf | 1 | 8-8 | 鞍山HR 鞍山市肿瘤医院 医学影像学CT诊断报告书 云影像 患者姓名 性别：女  |
| 7 | a6057d1c | 1 | 9-9 | 中国医科大学附属第一医院鞍山医院 鞍山HR CT检查报告单 病人编号：P0000 |
| 8 | ec05df64 | 1 | 11-11 | <table><tr><td>总胆红素</td><td>None</td><td |
| 9 | a87c76ca | 1 | 12-12 | <table><tr><td>红细胞分布宽度SD</td><td>RDW-SD< |
| 10 | 85eed28f | 1 | 14-14 | <table><tr><td>白细胞计数</td><td>WBC</td><td |
| 11 | 7a0c2235 | 1 | 10-10 | <table><tr><td>癌胚抗原</td><td>None</td><td |
| 12 | 7aaa8577 | 1 | 13-13 | <table><tr><td>谷丙转氨酶</td><td>ALT</td><td |

- chunks 总数：12
- 各 chunk 页数合计（含跨页重复）：14
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]`
- 覆盖页数：14 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 1 | ✅ |
| DischargeRecord | 出院 | 1 | 1 | ✅ |
| ExaminationReport | 检查报告 | 5 | 5 | ✅ |
| LabReport | 检验报告 | 5 | 5 | ✅ |

- 判定：✅ 全部类型匹配
