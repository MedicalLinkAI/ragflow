# 线上统计：CRFE,男，74，肺鳞癌.pdf

## 基本信息

- 文件：`CRFE,男，74，肺鳞癌.pdf`
- 大小：13614.6 KB
- PDF 总页数：-
- doc_id：`ec00f8867b8e11f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：16  orm_synced：True
- 处理耗时(服务端)：484.71155s  脚本耗时：490.1s
- 重解析前快照（无基线结果）：chunk_count=15 run=DONE clinical 类型记录数={'AdmissionRecord': 1, 'LabReport': 9, 'ExaminationReport': 5}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 9c7710a4 | 2 | 1-2 | 门诊号: 性别：男性 年龄：74岁 科 性别：男性 年龄：74岁 民族：汉族 婚 |
| 2 | ae105857 | 1 | 12-12 | 病理诊断：（左上叶口肿物活检组织）鳞状上皮乳头瘤样增生伴高级别上皮内瘤变；另见游 |
| 3 | 004c3233 | 1 | 13-13 | （胸部、全腹部CT平扫+增强+薄层）左肺上叶肺门旁见一结节状软组织密度影，大小约 |
| 4 | 8c0e959f | 1 | 14-14 | 心率(60-100)： 3.34 cm LA(2.7-3.8)： 3.11 cm |
| 5 | 2e93a2d3 | 1 | 15-15 | Vol [L] Vol%VCmax VCmax Time [s] Flow [L |
| 6 | c18c1806 | 1 | 16-16 | 检查 临床诊断：肺不张 呼吸内科/内分泌 床号：25 检查设备：ACUSON S |
| 7 | dda75eaa | 1 | 17-17 | 病理检查报告单 年龄：14岁 收到日期：2026-02-26 送检医生：史逸娴  |
| 8 | 3a4279fc | 1 | 5-5 | <table><tr><td>总蛋白</td><td>None</td><td> |
| 9 | dede0899 | 1 | 6-6 | <table><tr><td>凝血酶原时间</td><td>None</td>< |
| 10 | eece945f | 1 | 7-7 | <table><tr><td>红细胞沉降率</td><td>None</td>< |
| 11 | 31660359 | 1 | 8-8 | <table><tr><td>游离三碘甲状腺原氨酸</td><td>FT3</t |
| 12 | d1ce9603 | 1 | 10-10 | <table><tr><td>乙肝表面抗原</td><td>None</td>< |
| 13 | d96c658f | 1 | 11-11 | <table><tr><td>丙型肝炎抗体测定</td><td>None</td |
| 14 | b4600833 | 1 | 3-3 | <table><tr><td>C反应蛋白</td><td>None</td><t |
| 15 | 27aef596 | 1 | 4-4 | <table><tr><td>肌钙蛋白I</td><td>None</td><t |
| 16 | d4317098 | 1 | 9-9 | <table><tr><td>*人免疫缺陷病毒抗原/抗体检测</td><td>N |

- chunks 总数：16
- 各 chunk 页数合计（含跨页重复）：17
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]`
- 覆盖页数：17 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 0 | ❌ |
| ExaminationReport | 检查报告 | 6 | 0 | ❌ |
| LabReport | 检验报告 | 9 | 0 | ❌ |

- 判定：❌ 不匹配类型: AdmissionRecord, ExaminationReport, LabReport
