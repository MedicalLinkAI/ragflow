# 线上统计：KLYY-男-70岁-肺癌.pdf

## 基本信息

- 文件：`KLYY-男-70岁-肺癌.pdf`
- 大小：27144.5 KB
- PDF 总页数：-
- doc_id：`6d4b67b096fa11f19d3ab1cda0a97c3d`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：0  orm_synced：True
- 处理耗时(服务端)：324.81848s  脚本耗时：378.2s
- 备注：progress_msg 未找到 SmartSplitter 类型日志。 
- 重解析前快照（无基线结果）：chunk_count=19 run=DONE clinical 类型记录数={'LabReport': 11, 'AdmissionRecord': 1, 'ExaminationReport': 7}

## 1. 页面覆盖率

**该文档没有任何 chunk（文档级被过滤或解析失败）**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 0 | 1 | ❌ |
| ExaminationReport | 检查报告 | 0 | 7 | ❌ |
| LabReport | 检验报告 | 0 | 11 | ❌ |

- 判定：❌ 不匹配类型: AdmissionRecord, ExaminationReport, LabReport
