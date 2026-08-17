# 线上统计：CRFE,男，74，肺鳞癌.pdf

## 基本信息

- 文件：`CRFE,男，74，肺鳞癌.pdf`
- 大小：13614.6 KB
- PDF 总页数：-
- doc_id：`ec00f8867b8e11f1b6baf3b5d53eafd8`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：0  orm_synced：True
- 处理耗时(服务端)：325.1706s  脚本耗时：381.1s
- 备注：progress_msg 未找到 SmartSplitter 类型日志。 
- 重解析前快照（无基线结果）：chunk_count=16 run=DONE clinical 类型记录数={'AdmissionRecord': 1, 'LabReport': 9, 'ExaminationReport': 6}

## 1. 页面覆盖率

**该文档没有任何 chunk（文档级被过滤或解析失败）**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 0 | 1 | ❌ |
| ExaminationReport | 检查报告 | 0 | 6 | ❌ |
| LabReport | 检验报告 | 0 | 9 | ❌ |

- 判定：❌ 不匹配类型: AdmissionRecord, ExaminationReport, LabReport
