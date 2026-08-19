# 线上统计：KLYY-男-70岁-肺癌.pdf

## 基本信息

- 文件：`KLYY-男-70岁-肺癌.pdf`
- 大小：27144.5 KB
- PDF 总页数：-
- doc_id：`6d4b67b096fa11f19d3ab1cda0a97c3d`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：18  orm_synced：True
- 处理耗时(服务端)：1351.8597s  脚本耗时：1354.3s
- 重解析前快照（无基线结果）：chunk_count=0 run=DONE clinical 类型记录数={'LabReport': 11, 'AdmissionRecord': 1, 'ExaminationReport': 7}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | ecaf6da1 | 9 | 1-9 | 病史 主诉：咳嗽、咳痰1月余 现病史：患者及家属共诉1月余前无明显诱因下出现阵发 |
| 2 | 1d5ae207 | 1 | 10-10 | 影像检查报告单 病人ID: 姓名: 性别: 男 年龄: 67岁 申请科室: 老年 |
| 3 | 1e9957e8 | 2 | 11-12 | 科 检查部位：全身骨显像 显像剂：99mTc-MDP 临床诊断：1.肺占位性病变 |
| 4 | f243e10a | 1 | 12-12 | 影像检查报告单 病人 ID: 姓名: 性别: 男 年龄: 67岁 申请科室: 机 |
| 5 | 21f8daee | 1 | 13-13 | 广西医科大学第一附属医院 影像检查报告单 病人ID: 姓名: 男 年龄: 67岁 |
| 6 | 3c6d2549 | 1 | 14-14 | 测量参数值: 测量项目 结果 单位 参考范围 测量项目 结果 单位 参考范围 主 |
| 7 | 531e9646 | 1 | 26-26 | 广西金域医学检验实验室 本报告单经过电子签名认证 Guangxi Kingmed |
| 8 | 66b3bd43 | 1 | 17-17 | <table><tr><td>丙型肝炎抗体定量*</td><td>None</t |
| 9 | 2ea978e9 | 1 | 18-18 | <table><tr><td>糖化血红蛋白HbA1c*</td><td>HbA1 |
| 10 | a853c8cb | 1 | 20-20 | <table><tr><td>总胆红素*</td><td>TBIL</td><t |
| 11 | 483116b4 | 1 | 22-22 | <table><tr><td>白细胞计数*</td><td>WBC</td><t |
| 12 | 6403e569 | 1 | 23-23 | <table><tr><td>吸氧浓度</td><td>FI02</td><td |
| 13 | e1802ca8 | 1 | 15-15 | <table><tr><td>结核杆菌DNA*</td><td>TB-DNA</ |
| 14 | 7b7dbf48 | 1 | 16-16 | <table><tr><td>乙型肝炎表面抗原*</td><td>None</t |
| 15 | 1730366b | 1 | 19-19 | <table><tr><td>凝血酶原时间</td><td>None</td>< |
| 16 | 411c73b3 | 1 | 21-21 | <table><tr><td>胆碱酯酶*</td><td>CHE</td><td |
| 17 | 46b4e6e9 | 1 | 24-24 | <table><tr><td>酸碱度 (PH)</td><td>PH</td>< |
| 18 | 9806558c | 1 | 25-25 | <table><tr><td>ALK</td><td>None</td><td> |

- chunks 总数：18
- 各 chunk 页数合计（含跨页重复）：27
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]`
- 覆盖页数：26 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 1 | ✅ |
| ExaminationReport | 检查报告 | 6 | 6 | ✅ |
| LabReport | 检验报告 | 11 | 11 | ✅ |

- 判定：✅ 全部类型匹配
