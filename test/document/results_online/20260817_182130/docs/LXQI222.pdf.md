# 线上统计：LXQI222.pdf

## 基本信息

- 文件：`LXQI222.pdf`
- 大小：62937.7 KB
- PDF 总页数：-
- doc_id：`a4816fe696d111f19d3ab1cda0a97c3d`
- 处理方式：reparse-list
- 状态：run=DONE  progress=1.0
- chunk_count(status)：0  orm_synced：False
- 处理耗时(服务端)：328.34604s  脚本耗时：381.2s
- 备注：progress_msg 未找到 SmartSplitter 类型日志。 
- 基线对比（20260814_095003）：基线 chunks=4 → 本次 chunks=0

## 1. 页面覆盖率

**该文档没有任何 chunk（文档级被过滤或解析失败）**

## 2. 类型一致性（SmartSplitter 日志 vs clinical encounters）

| 类型 | 中文 | SmartSplitter chunks | clinical 记录 | 匹配 |
|------|------|---------------------|---------------|------|
| AdmissionRecord | 入院 | 0 | 1 | ❌ |
| DischargeRecord | 出院 | 0 | 1 | ❌ |
| ExaminationReport | 检查报告 | 0 | 2 | ❌ |
| PrescriptionRecord | 处方 | 0 | 1 | ❌ |

- 判定：❌ 不匹配类型: AdmissionRecord, DischargeRecord, ExaminationReport, PrescriptionRecord
