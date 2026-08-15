# 线上统计：YXLA（支气管哮喘）222.pdf

## 基本信息

- 文件：`YXLA（支气管哮喘）222.pdf`
- 大小：20976.6 KB
- PDF 总页数：19
- doc_id：`c0fe480c96df11f19d3ab1cda0a97c3d`
- 处理方式：existing+reparse
- 状态：run=DONE  progress=1.0
- chunk_count(status)：0  orm_synced：True
- 处理耗时(服务端)：344.86404s  脚本耗时：397.2s
- 备注：progress_msg 未找到 SmartSplitter 类型日志。 
- 基线对比（20260814_095003）：基线 chunks=15 → 本次 chunks=0

## 1. 页面覆盖率

**该文档没有任何 chunk（文档级被过滤或解析失败）**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 0 | 1 | ❌ |
| DischargeRecord | 出院 | 0 | 2 | ❌ |
| ExaminationReport | 检查报告 | 0 | 6 | ❌ |
| MedicationRecord | 购药 | 0 | 1 | ❌ |
| PrescriptionRecord | 处方 | 0 | 2 | ❌ |

- 判定：❌ 不匹配类型: AdmissionRecord, DischargeRecord, ExaminationReport, MedicationRecord, PrescriptionRecord
