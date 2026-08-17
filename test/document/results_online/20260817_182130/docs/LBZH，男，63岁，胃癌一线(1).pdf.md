# 线上统计：LBZH，男，63岁，胃癌一线(1).pdf

## 基本信息

- 文件：`LBZH，男，63岁，胃癌一线(1).pdf`
- 大小：27790.0 KB
- PDF 总页数：-
- doc_id：`f77057f0960c11f1abb555ceeebece40`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：0  orm_synced：True
- 处理耗时(服务端)：332.50314s  脚本耗时：386.8s
- 备注：progress_msg 未找到 SmartSplitter 类型日志。 
- 重解析前快照（无基线结果）：chunk_count=7 run=DONE clinical 类型记录数={'ExaminationReport': 4, 'DischargeRecord': 1, 'LabReport': 1, 'OutpatientRecord': 1}

## 1. 页面覆盖率

**该文档没有任何 chunk（文档级被过滤或解析失败）**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| DischargeRecord | 出院 | 0 | 1 | ❌ |
| ExaminationReport | 检查报告 | 0 | 4 | ❌ |
| LabReport | 检验报告 | 0 | 1 | ❌ |
| OutpatientRecord | 门诊 | 0 | 1 | ❌ |

- 判定：❌ 不匹配类型: DischargeRecord, ExaminationReport, LabReport, OutpatientRecord
