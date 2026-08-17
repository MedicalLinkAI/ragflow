# 线上统计：07-毓璜顶-ZPQI，后线肺癌，方穹招募推荐.pdf

## 基本信息

- 文件：`07-毓璜顶-ZPQI，后线肺癌，方穹招募推荐.pdf`
- 大小：6889.5 KB
- PDF 总页数：-
- doc_id：`c50f9bd894e811f1bd9827cf206dfa2d`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：0  orm_synced：True
- 处理耗时(服务端)：746.0013s  脚本耗时：804.9s
- 备注：progress_msg 未找到 SmartSplitter 类型日志。 
- 重解析前快照（无基线结果）：chunk_count=28 run=DONE clinical 类型记录数={'LabReport': 5, 'ExaminationReport': 18, 'AdmissionRecord': 1, 'DischargeRecord': 1, 'OutpatientRecord': 2}

## 1. 页面覆盖率

**该文档没有任何 chunk（文档级被过滤或解析失败）**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 0 | 1 | ❌ |
| DischargeRecord | 出院 | 0 | 1 | ❌ |
| ExaminationReport | 检查报告 | 0 | 18 | ❌ |
| LabReport | 检验报告 | 0 | 5 | ❌ |
| OutpatientRecord | 门诊 | 0 | 2 | ❌ |

- 判定：❌ 不匹配类型: AdmissionRecord, DischargeRecord, ExaminationReport, LabReport, OutpatientRecord
