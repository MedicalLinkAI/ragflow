# 线上统计：SYQI肺鳞癌.pdf

## 基本信息

- 文件：`SYQI肺鳞癌.pdf`
- 大小：6541.0 KB
- PDF 总页数：-
- doc_id：`737f81ac94f211f1bd9827cf206dfa2d`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：15  orm_synced：True
- 处理耗时(服务端)：383.5659s  脚本耗时：393.3s
- 重解析前快照（无基线结果）：chunk_count=15 run=DONE clinical 类型记录数={'LabReport': 10, 'DischargeRecord': 1, 'ExaminationReport': 2}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | c250c2c1 | 1 | 1-1 | 空军军医大学唐都医院 查阅电子胶片 CT检查报告单 ID号：62893718 检 |
| 2 | 87a09170 | 1 | 3-3 | 空军军医大学第二附属医院(唐都医院) 病理图文诊断报告单 病理号: 261044 |
| 3 | 85a170ae | 2 | 4-5 | 中国人民解放军联勤保障部队第九八九医院 出院证 姓名： 性别：男 年龄：55岁  |
| 4 | 854794c6 | 1 | 5-5 | 姓名:水月强 病区(科):肿瘤科病区 床号:11 出院记录 姓名: 性别:男 年 |
| 5 | a9657c8f | 1 | 6-6 | <table><tr><td>凝血酶原时间</td><td>PT-1</td>< |
| 6 | 3e48fae1 | 1 | 7-7 | <table><tr><td>乙肝肝炎病毒表面抗原</td><td>HBsAg< |
| 7 | 1def1326 | 1 | 8-8 | <table><tr><td>白细胞计数(8-HR)</td><td>WBC</ |
| 8 | c6510ee1 | 1 | 9-9 | <table><tr><td>乙肝表面抗原</td><td>HBsAg</td> |
| 9 | fb312758 | 1 | 11-11 | <table><tr><td>游离三碘甲状腺原氨酸(8-HR)</td><td> |
| 10 | 77869164 | 1 | 14-14 | <table><tr><td>血糖(空腹)(8-HR)</td><td>GLU< |
| 11 | fc961fff | 1 | 6-6 | <table><tr><td>白细胞计数</td><td>WBC</td><td |
| 12 | 0315c5f2 | 1 | 10-10 | <table><tr><td>ABO血型鉴定</td><td>ABO</td>< |
| 13 | 5ff08417 | 1 | 12-12 | <table><tr><td>肌酸激酶同工酶</td><td>CK-MB</td |
| 14 | d4666ac9 | 1 | 13-13 | <table><tr><td>凝血酶原时间(陕HR)</td><td>PT</t |

- chunks 总数：14
- 各 chunk 页数合计（含跨页重复）：15
- 页码并集：`[1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]`
- 覆盖页数：13 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| DischargeRecord | 出院 | 2 | 1 | ❌ |
| ExaminationReport | 检查报告 | 2 | 2 | ✅ |
| LabReport | 检验报告 | 11 | 10 | ❌ |

- 判定：❌ 不匹配类型: DischargeRecord, LabReport
