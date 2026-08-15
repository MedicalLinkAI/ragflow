# 线上统计：ZLME 女  54 胃癌初诊.pdf

## 基本信息

- 文件：`ZLME 女  54 胃癌初诊.pdf`
- 大小：56936.4 KB
- PDF 总页数：-
- doc_id：`51787d0a78f711f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：12  orm_synced：True
- 处理耗时(服务端)：458.2952s  脚本耗时：460.9s
- 重解析前快照（无基线结果）：chunk_count=6 run=DONE clinical 类型记录数={'AdmissionRecord': 1, 'ExaminationReport': 5}

## 1. 页面覆盖率

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 21bad2c8 | 1 | 1-1 | 浏阳市人民医院 病理会诊报告单 病理号： 姓名： 性别：女 年龄：54岁 送检医 |
| 2 | f3a28f0a | 2 | 2-3 | 常规通气报告 姓名： 年龄：54岁 性别：女 科室：-- 住址： 预计值模式：S |
| 3 | 41bfdfbb | 1 | 3-3 | 彩超报告单 超声号：CS 检查设备：住院腹部浅表 床号： 姓名： 性别：女 年龄 |
| 4 | 9338c5de | 1 | 4-4 | 测阳市人民医院 彩超报告单 超声号： 检查设备：住院腹部浅表 床号： 名： 性别 |
| 5 | 2e535126 | 3 | 5-7 | 浏阳市人民医院 姓名： 科室：[胃肠外科 床号：[49] 住院号：[ 一病区]  |
| 6 | 0cd9ef7e | 1 | 13-13 | ID: 姓名: 性别:女 年龄:54岁 科室/床号:胃肠外科一病区19 门诊/住 |
| 7 | 3de6a40d | 1 | 14-14 | 浏阳市人民医院 湖南HR CT诊断报告 住院号：0 影像号：26( 姓名： 性别 |
| 8 | 25ff399c | 1 | 8-8 | <table><tr><td>*白细胞计数</td><td>WBC</td><t |
| 9 | 02232f70 | 1 | 9-9 | <table><tr><td>葡萄糖</td><td>GLU</td><td>4 |
| 10 | c399b5e4 | 1 | 10-10 | <table><tr><td>大凝血酶原时间</td><td>PT</td><t |
| 11 | 7f733902 | 1 | 11-11 | <table><tr><td>甲胎蛋白</td><td>AFP</td><td> |
| 12 | 72e38173 | 1 | 12-12 | <table><tr><td>乙型肝炎病毒表面抗原</td><td>HBsAg< |

- chunks 总数：12
- 各 chunk 页数合计（含跨页重复）：15
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]`
- 覆盖页数：14 / None（覆盖率 None%）
- 缺失页：`[]`  超范围页：`[]`
- **结论：⚠️ PDF 页数未知，无法核对**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 1 | 0 | ❌ |
| ExaminationReport | 检查报告 | 6 | 0 | ❌ |
| LabReport | 检验报告 | 5 | 0 | ❌ |

- 判定：❌ 不匹配类型: AdmissionRecord, ExaminationReport, LabReport
