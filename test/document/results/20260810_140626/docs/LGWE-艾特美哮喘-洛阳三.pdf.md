# 基准结果：LGWE-艾特美哮喘-洛阳三.pdf

## 基本信息

- 文件：`LGWE-艾特美哮喘-洛阳三.pdf`
- 大小：1610.3 KB
- PDF 总页数：3
- doc_id：`db492056948211f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T14:15:16  完成时间：2026-08-10T14:20:34  耗时：318.5s
- progress_msg：`06:19:59 Indexing done (0.04s). Task done (225.99s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

**该文档没有任何 chunk（文档级被过滤或解析失败）**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 1 | 0 | 1 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 2 | 2 | 2 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 0 | 0 | 0 | report_time, report_category, report_name | **-** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 1, "ExaminationReport": 2}`
- ChunkMerger：`{"found": true, "merged": 3, "sources": 8, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 2}, "filtered_noise": 6}`
- Extractor skip 证据：2 条
  - `[no_text_noise] 2026-08-10 06:19:08,866 INFO     29 [ChunkMerger] Merged 40 chunks from 8 sources: {'Extractor:LabExam': 13, 'Extractor:Imaging': 1, 'Extractor:Clinical': 14, 'Extractor:Medication': 1, 'Extractor:Pre`
  - `[no_text_noise] 2026-08-10 06:19:57,958 INFO     29 [ChunkMerger] Merged 3 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 06:16:12,608 INFO     29 handle_task begin for task {"id": "dbae825c948211f1bd9827cf206dfa2d", "doc_id": "db492056948211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LGWE-\u827e\u7279\u7f8e\u54ee\u5598-\u6d1b\u9633\u4e09.pdf", "type": "pdf", "location": "LGWE-\u827e\u7279\u7f8e\u54ee\u5598-\u6d1b\u9633\u4e09.pdf", "size": 1648931, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786342517754, "task_type": "dataflow", "root_trace_id": "aaa86c5dcc2c462f88c0ac982e1d484f", "root_traceparent": "00-aaa86c5dcc2c462f88c0ac982e1d484f-c2d6050d16147908-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 06:16:12,853 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 06:16:12,967 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 06:16:13,248 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:16:13,248 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 06:16:13,248 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 06:16:13,261 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 06:16:13,261 INFO     29 ============================================================
2026-08-10 06:16:13,261 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 06:16:13,261 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 06:16:13,261 INFO     29 ============================================================
2026-08-10 06:16:13,261 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 06:16:13,262 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 06:16:13,264 INFO     29 No torch found.
2026-08-10 06:16:13,981 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=3
2026-08-10 06:16:14,085 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=716317, prompt_len=764
2026-08-10 06:16:15,517 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 06:16:15,517 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 06:16:15,529 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=716317, prompt_len=401
2026-08-10 06:16:18,108 INFO     29 [qwen-vl-parser] text API response (len=343):
["郑州市第一人民医院门诊病历", "科室：呼吸内科一门诊", "就诊日期：2025-05-25", "初诊", "姓名：", "性别：男", "年龄：61岁", "ID：", "主 诉：咳嗽、胸闷3月", "现 病 史：3月前出现咳嗽、胸闷，来诊", "既 往 史：无高血压病、冠心病、糖尿病病史，无乙肝、肝炎病史。无", "药物过敏史。", "体格检查：神志清，双肺呼吸音粗，未闻及啰音；", "处 理：完善肺功能", "建 议：门诊口服药物治疗，如出现此疾病复发或症状加重的可能，", "请随时就诊", "诊 断：1.支气管哮喘；", "检查", "肺功能检查+支气管舒张实验", "医生：张朝杰", "打印日期：2025-05-25 12:03", "第 1 页，共 1 页"]
2026-08-10 06:16:18,109 INFO     29 [qwen-vl-parser] page=1 text: 22 lines (bbox 0-21)
2026-08-10 06:16:18,109 INFO     29 [qwen-vl-parser] page=1 text: 22 sections
2026-08-10 06:16:18,208 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=664058, prompt_len=764
2026-08-10 06:16:19,689 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2025-05-25"
}
```
2026-08-10 06:16:19,689 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=2025-05-25
2026-08-10 06:16:19,696 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=664058, prompt_len=401
2026-08-10 06:16:26,127 INFO     29 [qwen-vl-parser] text API response (len=944):
["郑州市第一人民医院", "肺功能检查报告", "舒张试验", "姓名：", "性别：男", "年龄：61岁", "身高：174 cm", "体重：85 kg", "科别：呼吸内科", "住院号：", "测试号：2025052513", "吸烟史：", "联系电话：", "测试日期 25-5-25", "测试时间 11:46:55", "预计值", "前次", "前/预", "后次", "后/预", "改善率", "25-5-25", "25-5-25", "11:46:55", "11:57:14", "FVC [L] 4.10 2.84 69.4 3.49 85.2 22.91", "FEV 1 [L] 3.22 2.51 78.0 3.06 95.0 21.81", "FEV 1 % FVC [%] 83.40 88.46 106.1 87.66 105.1 -0.90", "PEF [L/s] 8.21 6.40 77.9 6.63 80.8 3.68", "MEF 75 [L/s] 7.26 6.18 85.1 6.13 84.4 -0.76", "MEF 50 [L/s] 4.35 3.04 69.9 4.48 102.9 47.19", "MEF 25 [L/s] 1.62 1.18 72.8 1.25 77.6 6.56", "MMEF 75/25 [L/s] 3.45 2.26 65.4 3.32 96.0 46.80", "Flow [L/s]", "F/V ex", "10", "5", "0", "1", "2", "3", "4", "5", "F/V In", "6", "Vol [L]", "5", "Vol%Vmax", "100", "V Cmax", "80", "3", "60", "2", "40", "20", "1", "0", "0", "Time [s]", "0.0", "0.5", "1.0", "1.5", "2.0", "2.5", "3.0", "测试结果：", "支气管舒张试验阳性。", "(请结合临床全面诊断)", "医生签字：毛锦涛", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 06:16:26,128 INFO     29 [qwen-vl-parser] page=2 text: 73 lines (bbox 22-94)
2026-08-10 06:16:26,128 INFO     29 [qwen-vl-parser] page=2 text: 73 sections
2026-08-10 06:16:26,242 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=785551, prompt_len=764
2026-08-10 06:16:27,335 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:16:27,335 INFO     29 [qwen-vl-text] LLM output (len=1115):
{
  "exam_date": "2026-01-15",
  "report_date": "2026-01-15",
  "exam_name": "肺功能检查",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": "预计\n实1 %(实1/预)\n实2 %(实2/预)\n变异率\n测试日期\n26/1/15\n26/1/15\n测试时间\n9:51:00上午\n10:14:56上午\nFVC\n[L]\n3.13\n3.15\n100.5\n3.25\n103.9\n3.3\nFEV 1\n[L]\n2.70\n1.99\n73.9\n2.26\n83.8\n13.4\nFEV 1 % FVC\n[%]\n83.98\n63.25\n75.3\n69.40\n82.6\n9.7\nFEV 1 % VC MAX\n[%]\n81.31\n63.25\n77.8\n69.40\n85.4\n9.7\nPEF\n[L/s]\n6.46\n6.33\n98.0\n7.25\n112.2\n14.5\nMEF 75\n[L/s]\n5.73\n3.01\n52.6\n3.73\n65.1\n23.8\nMEF 50\n[L/s]\n4.06\n1.25\n30.9\n1.67\n41.2\n33.3\nMEF 25\n[L/s]\n1.77\n0.46\n26.3\n0.59\n33.6\n27.7\nMMEF 75/25\n[L/s]\n3.53\n1.06\n30.0\n1.46\n41.3\n37.6\nFET\n[s]\n8.73\n4.94\n-43.4\nV backextrapolation ex [L]\n0.06\n0.07\n20.1\nV backextrapol. % FVC [%]\n1.86\n2.17\n16.3\nFlow [L/s]\nF/V ex\n10\n5\n0\n1\n2\n3\n4\n5\n6\n7\n10\nF/V In",
  "conclusion": "支气管舒张试验阳性。\n(通过储雾罐吸入硫酸沙丁胺醇气雾剂400ug20分钟后。\nFEV1较基线增加大于12 %，且绝对值增加大于200 ml。",
  "physician": "朱龙华",
  "reviewer": "孙帅森"
}
2026-08-10 06:16:27,337 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=738007, prompt_len=1775
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共125行）
["肺功能报告单", "姓名：", "出生日期：", "住院号：", "身高：160 cm", "身份证号：", "性别：女", "年龄：41岁", "测试号：", "体重：48 kg", "预计", "实1 %(实1/预)", "实2 %(实2/预)", "变异率", "测试日期", "26/1/15", "26/1/15", "测试时间", "9:51:00上午", "10:14:56上午", "FVC", "[L]", "3.13", "3.15", "100.5", "3.25", "103.9", "3.3", "FEV 1", "[L]", "2.70", "1.99", "73.9", "2.26", "83.8", "13.4", "FEV 1 % FVC", "[%]", "83.98", "63.25", "75.3", "69.40", "82.6", "9.7", "FEV 1 % VC MAX", "[%]", "81.31", "63.25", "77.8", "69.40", "85.4", "9.7", "PEF", "[L/s]", "6.46", "6.33", "98.0", "7.25", "112.2", "14.5", "MEF 75", "[L/s]", "5.73", "3.01", "52.6", "3.73", "65.1", "23.8", "MEF 50", "[L/s]", "4.06", "1.25", "30.9", "1.67", "41.2", "33.3", "MEF 25", "[L/s]", "1.77", "0.46", "26.3", "0.59", "33.6", "27.7", "MMEF 75/25", "[L/s]", "3.53", "1.06", "30.0", "1.46", "41.3", "37.6", "FET", "[s]", "8.73", "4.94", "-43.4", "V backextrapolation ex [L]", "0.06", "0.07", "20.1", "V backextrapol. % FVC [%]", "1.86", "2.17", "16.3", "Flow [L/s]", "F/V ex", "10", "5", "0", "1", "2", "3", "4", "5", "6", "7", "10", "F/V In", "医生意见：", "支气管舒张试验阳性。", "(通过储雾罐吸入硫酸沙丁胺醇气雾剂400ug20分钟后。", "FEV1较基线增加大于12 %，且绝对值增加大于200 ml。", "审核医生：孙帅森", "检测技师：朱龙华"]

## 定位规则
1. 对于列表中的每行文本，找到它在图片中**精确出现**的位置
2. bbox必须是该行文字的**最小紧密包围框**，紧贴文字边缘，不要包含额外的空白区域
3. 坐标归一化到0-1000，格式[x1,y1,x2,y2]
4. 如果某行文本在图片中未找到，跳过不输出
5. text字段必须与给定的文本完全一致

## 包围框精度要求
- x1必须紧贴该行第一个字符的左边缘
- x2必须紧贴该行最后一个字符的右边缘
- y1必须紧贴该行文字的顶部
- y2必须紧贴该行文字的底部
- 禁止将多行文字合并到同一个bbox中

## 严格JSON格式要求
直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。
正确示例：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230]},
  {"text": "年龄：68岁", "bbox": [100, 250, 270, 280]}
]
错误示例（禁止额外字段）：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230], "label": "个人信息"}
]
请直接输出纯JSON数组，不要用markdown代码块包裹。
2026-08-10 06:16:27,705 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 06:16:27,705 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 06:16:27,717 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=785551, prompt_len=401
2026-08-10 06:16:37,585 INFO     29 [qwen-vl-parser] text API response (len=1100):
["郑州市第一人民医院", "肺功能检查报告", "常规通气", "姓名：", "性别：男", "年龄：61岁", "身高：174 cm", "科别：呼吸内科", "住院号：门诊", "测试号：2025052513", "体重：85 kg", "测试日期 25-5-25", "测试时间 11:46:55", "预计值 实测值 实/预", "IRV [L] 1.14", "ERV [L] 3.12", "IC [L] 0.61", "VT [L] 4.26 0.65 106.5", "VC IN [L] 4.26 3.01 70.7", "VC EX [L] 4.26 2.84 66.8", "BF [1/min] 20.00 17.72 88.6", "MV [L/min] 12.14 11.46 94.4", "VC MAX [L] 4.26 3.01 70.7", "FVC [L] 4.10 2.84 69.4", "FEV 1 [L] 3.22 2.51 78.0", "FEV 1 % FVC [%] 83.40 88.46 106.1", "FEV 1 % VC MAX [%] 76.23 83.54 109.6", "PEF [L/s] 8.21 6.40 77.9", "MEF 75 [L/s] 7.26 6.18 85.1", "MEF 50 [L/s] 4.35 3.04 69.9", "MEF 25 [L/s] 1.62 1.18 72.8", "MMEF 75/25 [L/s] . 3.45 2.26 65.4", "MVV [L/min] 119.91 77.46 64.6", "FEV 1*30 [L/min] 119.91 75.39 62.9", "Vol [L]", "TLC 6", "FRC pleth", "RV 2", "PredA0.0 0.2 0.4 0.6 0.8 1.0", "Time [min]", "Flow [L/s]", "F/V ex", "10", "5", "0", "1", "2", "3", "4", "5", "F/V in", "Vol [L]", "2", "1", "0", "1", "2", "Time [s]", "0 2 4 6 8 10 12", "测试结果：", "提示：", "1、轻度阻塞性肺通气功能障碍；", "2、肺储备功能下降。", "(请结合临床全面诊断)", "医生签字：毛锦涛", "报告日期：2025-5-27", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 06:16:37,586 INFO     29 [qwen-vl-parser] page=3 text: 68 lines (bbox 95-162)
2026-08-10 06:16:37,586 INFO     29 [qwen-vl-parser] page=3 text: 68 sections
2026-08-10 06:16:37,586 INFO     29 [qwen-vl-parser] parse_pdf done: 163 sections from 3 pages.
2026-08-10 06:16:37,596 INFO     29 Close text detector.
2026-08-10 06:16:38,025 INFO     29 Close text recognizer.
2026-08-10 06:16:38,428 INFO     29 Close recognizer.
2026-08-10 06:16:38,837 INFO     29 Close recognizer.
2026-08-10 06:17:07,886 INFO     29 [qwen-vl-text] coord API raw response (len=6256):
[
	{"text": "肺功能报告单", "bbox": [410, 81, 555, 101]},
	{"text": "姓名：", "bbox": [91, 104, 140, 117]},
	{"text": "出生日期：", "bbox": [91, 117, 178, 130]},
	{"text": "住院号：", "bbox": [91, 130, 158, 144]},
	{"text": "身高：160 cm", "bbox": [91, 144, 345, 158]},
	{"text": "身份证号：", "bbox": [91, 158, 178, 172]},
	{"text": "性别：", "bbox": [483, 102, 535, 116]},
	{"text": "年龄：", "bbox": [483, 116, 535, 130]},
	{"text": "测试号：", "bbox": [483, 130, 555, 144]},
	{"text": "体重：", "bbox": [483, 144, 535, 158]},
	{"text": "预计", "bbox": [344, 178, 380, 193]},
	{"text": "实1 %(实1/预)", "bbox": [464, 178, 578, 194]},
	{"text": "实2 %(实2/预)", "bbox": [661, 178, 777, 194]},
	{"text": "变异率", "bbox": [807, 178, 860, 193]},
	{"text": "测试日期", "bbox": [97, 195, 168, 209]},
	{"text": "26/1/15", "bbox": [431, 195, 492, 209]},
	{"text": "26/1/15", "bbox": [628, 195, 690, 209]},
	{"text": "测试时间", "bbox": [97, 210, 168, 224]},
	{"text": "9:51:00上午", "bbox": [395, 210, 492, 224]},
	{"text": "10:14:56上午", "bbox": [587, 210, 690, 224]},
	{"text": "FVC", "bbox": [97, 243, 134, 257]},
	{"text": "[L]", "bbox": [297, 243, 320, 258]},
	{"text": "3.13", "bbox": [344, 243, 380, 257]},
	{"text": "3.15", "bbox": [455, 243, 492, 257]},
	{"text": "100.5", "bbox": [532, 243, 577, 257]},
	{"text": "3.25", "bbox": [654, 243, 690, 257]},
	{"text": "103.9", "bbox": [732, 243, 777, 257]},
	{"text": "3.3", "bbox": [837, 243, 862, 257]},
	{"text": "FEV 1", "bbox": [97, 258, 146, 272]},
	{"text": "[L]", "bbox": [297, 258, 320, 273]},
	{"text": "2.70", "bbox": [344, 258, 380, 272]},
	{"text": "1.99", "bbox": [455, 258, 492, 272]},
	{"text": "73.9", "bbox": [541, 258, 577, 272]},
	{"text": "2.26", "bbox": [654, 258, 690, 272]},
	{"text": "83.8", "bbox": [741, 258, 777, 272]},
	{"text": "13.4", "bbox": [828, 258, 862, 272]},
	{"text": "FEV 1 % FVC", "bbox": [97, 274, 208, 288]},
	{"text": "[%]", "bbox": [292, 274, 320, 289]},
	{"text": "83.98", "bbox": [335, 274, 380, 288]},
	{"text": "63.25", "bbox": [445, 274, 492, 288]},
	{"text": "75.3", "bbox": [541, 274, 577, 288]},
	{"text": "69.40", "bbox": [644, 274, 690, 288]},
	{"text": "82.6", "bbox": [741, 274, 777, 288]},
	{"text": "9.7", "bbox": [837, 274, 862, 288]},
	{"text": "FEV 1 % VC MAX", "bbox": [97, 290, 242, 304]},
	{"text": "[%]", "bbox": [292, 290, 320, 305]},
	{"text": "81.31", "bbox": [335, 290, 380, 304]},
	{"text": "63.25", "bbox": [445, 290, 492, 304]},
	{"text": "77.8", "bbox": [541, 290, 577, 304]},
	{"text": "69.40", "bbox": [644, 290, 690, 304]},
	{"text": "85.4", "bbox": [741, 290, 777, 304]},
	{"text": "9.7", "bbox": [837, 290, 862, 304]},
	{"text": "PEF", "bbox": [97, 306, 134, 320]},
	{"text": "[L/s]", "bbox": [282, 306, 320, 321]},
	{"text": "6.46", "bbox": [344, 306, 380, 320]},
	{"text": "6.33", "bbox": [455, 306, 492, 320]},
	{"text": "98.0", "bbox": [541, 306, 577, 320]},
	{"text": "7.25", "bbox": [654, 306, 690, 320]},
	{"text": "112.2", "bbox": [732, 306, 777, 320]},
	{"text": "14.5", "bbox": [828, 306, 862, 320]},
	{"text": "MEF 75", "bbox": [97, 322, 160, 336]},
	{"text": "[L/s]", "bbox": [282, 322, 320, 337]},
	{"text": "5.73", "bbox": [344, 322, 380, 336]},
	{"text": "3.01", "bbox": [455, 322, 492, 336]},
	{"text": "52.6", "bbox": [541, 322, 577, 336]},
	{"text": "3.73", "bbox": [654, 322, 690, 336]},
	{"text": "65.1", "bbox": [741, 322, 777, 336]},
	{"text": "23.8", "bbox": [828, 322, 862, 336]},
	{"text": "MEF 50", "bbox": [97, 338, 160, 352]},
	{"text": "[L/s]", "bbox": [282, 338, 320, 353]},
	{"text": "4.06", "bbox": [344, 338, 380, 352]},
	{"text": "1.25", "bbox": [455, 338, 492, 352]},
	{"text": "30.9", "bbox": [541, 338, 577, 352]},
	{"text": "1.67", "bbox": [654, 338, 690, 352]},
	{"text": "41.2", "bbox": [741, 338, 777, 352]},
	{"text": "33.3", "bbox": [828, 338, 862, 352]},
	{"text": "MEF 25", "bbox": [97, 354, 160, 368]},
	{"text": "[L/s]", "bbox": [282, 354, 320, 369]},
	{"text": "1.77", "bbox": [344, 354, 380, 368]},
	{"text": "0.46", "bbox": [455, 354, 492, 368]},
	{"text": "26.3", "bbox": [541, 354, 577, 368]},
	{"text": "0.59", "bbox": [654, 354, 690, 368]},
	{"text": "33.6", "bbox": [741, 354, 777, 368]},
	{"text": "27.7", "bbox": [828, 354, 862, 368]},
	{"text": "MMEF 75/25", "bbox": [97, 370, 200, 384]},
	{"text": "[L/s]", "bbox": [282, 370, 320, 385]},
	{"text": "3.53", "bbox": [344, 370, 380, 384]},
	{"text": "1.06", "bbox": [455, 370, 492, 384]},
	{"text": "30.0", "bbox": [541, 370, 577, 384]},
	{"text": "1.46", "bbox": [654, 370, 690, 384]},
	{"text": "41.3", "bbox": [741, 370, 777, 384]},
	{"text": "37.6", "bbox": [828, 370, 862, 384]},
	{"text": "FET", "bbox": [97, 386, 134, 400]},
	{"text": "[s]", "bbox": [297, 386, 320, 401]},
	{"text": "8.73", "bbox": [455, 386, 492, 400]},
	{"text": "4.94", "bbox": [654, 386, 690, 400]},
	{"text": "-43.4", "bbox": [821, 386, 862, 400]},
	{"text": "V backextrapolation ex [L]", "bbox": [97, 402, 320, 416]},
	{"text": "0.06", "bbox": [455, 402, 492, 416]},
	{"text": "0.07", "bbox": [654, 402, 690, 416]},
	{"text": "20.1", "bbox": [828, 402, 862, 416]},
	{"text": "V backextrapol. % FVC [%]", "bbox": [97, 417, 320, 432]},
	{"text": "1.86", "bbox": [455, 417, 492, 432]},
	{"text": "2.17", "bbox": [654, 417, 690, 432]},
	{"text": "16.3", "bbox": [828, 417, 862, 432]},
	{"text": "Flow [L/s]", "bbox": [150, 500, 201, 512]},
	{"text": "F/V ex", "bbox": [589, 501, 622, 511]},
	{"text": "10", "bbox": [133, 518, 148, 528]},
	{"text": "5", "bbox": [137, 545, 146, 555]},
	{"text": "0", "bbox": [137, 572, 146, 582]},
	{"text": "1", "bbox": [230, 582, 238, 591]},
	{"text": "2", "bbox": [315, 582, 324, 591]},
	{"text": "3", "bbox": [402, 582, 410, 591]},
	{"text": "4", "bbox": [487, 582, 496, 591]},
	{"text": "5", "bbox": [573, 582, 582, 591]},
	{"text": "6", "bbox": [661, 582, 670, 591]},
	{"text": "7", "bbox": [747, 582, 755, 591]},
	{"text": "10", "bbox": [133, 626, 148, 636]},
	{"text": "F/V In", "bbox": [593, 644, 622, 654]},
	{"text": "医生意见：", "bbox": [93, 664, 197, 681]},
	{"text": "支气管舒张试验阳性。", "bbox": [93, 684, 264, 697]},
	{"text": "(通过储雾罐吸入硫酸沙丁胺醇气雾剂400ug20分钟后。", "bbox": [93, 697, 526, 710]},
	{"text": "FEV1较基线增加大于12 %，且绝对值增加大于200 ml。", "bbox": [93, 709, 519, 722]},
	{"text": "审核医生：孙帅森", "bbox": [649, 791, 784, 806]},
	{"text": "检测技师：朱龙华", "bbox": [645, 812, 806, 838]}
]
2026-08-10 06:17:07,887 INFO     29 [qwen-vl-text] coord API: raw_items=125, valid_items=125, elapsed=40.5s
2026-08-10 06:17:07,887 INFO     29 [qwen-vl-text] coord item[0]: text=肺功能报告单, bbox=[410, 81, 555, 101]
2026-08-10 06:17:07,887 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[91, 104, 140, 117]
2026-08-10 06:17:07,887 INFO     29 [qwen-vl-text] coord item[2]: text=出生日期：, bbox=[91, 117, 178, 130]
2026-08-10 06:17:07,887 INFO     29 [qwen-vl-text] coord item[3]: text=住院号：, bbox=[91, 130, 158, 144]
2026-08-10 06:17:07,887 INFO     29 [qwen-vl-text] coord item[4]: text=身高：160 cm, bbox=[91, 144, 345, 158]
2026-08-10 06:17:07,887 INFO     29 [qwen-vl-text] coord item[5]: text=身份证号：, bbox=[91, 158, 178, 172]
2026-08-10 06:17:07,887 INFO     29 [qwen-vl-text] coord item[6]: text=性别：, bbox=[483, 102, 535, 116]
2026-08-10 06:17:07,887 INFO     29 [qwen-vl-text] coord item[7]: text=年龄：, bbox=[483, 116, 535, 130]
2026-08-10 06:17:07,887 INFO     29 [qwen-vl-text] coord item[8]: text=测试号：, bbox=[483, 130, 555, 144]
2026-08-10 06:17:07,887 INFO     29 [qwen-vl-text] coord item[9]: text=体重：, bbox=[483, 144, 535, 158]
2026-08-10 06:17:07,887 INFO     29 [qwen-vl-text] coord item[10]: text=预计, bbox=[344, 178, 380, 193]
2026-08-10 06:17:07,887 INFO     29 [qwen-vl-text] coord item[11]: text=实1 %(实1/预), bbox=[464, 178, 578, 194]
2026-08-10 06:17:07,887 INFO     29 [qwen-vl-text] coord item[12]: text=实2 %(实2/预), bbox=[661, 178, 777, 194]
2026-08-10 06:17:07,887 INFO     29 [qwen-vl-text] coord item[13]: text=变异率, bbox=[807, 178, 860, 193]
2026-08-10 06:17:07,887 INFO     29 [qwen-vl-text] coord item[14]: text=测试日期, bbox=[97, 195, 168, 209]
2026-08-10 06:17:07,887 INFO     29 [qwen-vl-text] coord item[15]: text=26/1/15, bbox=[431, 195, 492, 209]
2026-08-10 06:17:07,887 INFO     29 [qwen-vl-text] coord item[16]: text=26/1/15, bbox=[628, 195, 690, 209]
2026-08-10 06:17:07,887 INFO     29 [qwen-vl-text] coord item[17]: text=测试时间, bbox=[97, 210, 168, 224]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[18]: text=9:51:00上午, bbox=[395, 210, 492, 224]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[19]: text=10:14:56上午, bbox=[587, 210, 690, 224]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[20]: text=FVC, bbox=[97, 243, 134, 257]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[21]: text=[L], bbox=[297, 243, 320, 258]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[22]: text=3.13, bbox=[344, 243, 380, 257]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[23]: text=3.15, bbox=[455, 243, 492, 257]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[24]: text=100.5, bbox=[532, 243, 577, 257]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[25]: text=3.25, bbox=[654, 243, 690, 257]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[26]: text=103.9, bbox=[732, 243, 777, 257]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[27]: text=3.3, bbox=[837, 243, 862, 257]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[28]: text=FEV 1, bbox=[97, 258, 146, 272]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[29]: text=[L], bbox=[297, 258, 320, 273]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[30]: text=2.70, bbox=[344, 258, 380, 272]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[31]: text=1.99, bbox=[455, 258, 492, 272]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[32]: text=73.9, bbox=[541, 258, 577, 272]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[33]: text=2.26, bbox=[654, 258, 690, 272]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[34]: text=83.8, bbox=[741, 258, 777, 272]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[35]: text=13.4, bbox=[828, 258, 862, 272]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[36]: text=FEV 1 % FVC, bbox=[97, 274, 208, 288]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[37]: text=[%], bbox=[292, 274, 320, 289]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[38]: text=83.98, bbox=[335, 274, 380, 288]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[39]: text=63.25, bbox=[445, 274, 492, 288]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[40]: text=75.3, bbox=[541, 274, 577, 288]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[41]: text=69.40, bbox=[644, 274, 690, 288]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[42]: text=82.6, bbox=[741, 274, 777, 288]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[43]: text=9.7, bbox=[837, 274, 862, 288]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[44]: text=FEV 1 % VC MAX, bbox=[97, 290, 242, 304]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[45]: text=[%], bbox=[292, 290, 320, 305]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[46]: text=81.31, bbox=[335, 290, 380, 304]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[47]: text=63.25, bbox=[445, 290, 492, 304]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[48]: text=77.8, bbox=[541, 290, 577, 304]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[49]: text=69.40, bbox=[644, 290, 690, 304]
2026-08-10 06:17:07,888 INFO     29 [qwen-vl-text] coord item[50]: text=85.4, bbox=[741, 290, 777, 304]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[51]: text=9.7, bbox=[837, 290, 862, 304]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[52]: text=PEF, bbox=[97, 306, 134, 320]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[53]: text=[L/s], bbox=[282, 306, 320, 321]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[54]: text=6.46, bbox=[344, 306, 380, 320]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[55]: text=6.33, bbox=[455, 306, 492, 320]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[56]: text=98.0, bbox=[541, 306, 577, 320]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[57]: text=7.25, bbox=[654, 306, 690, 320]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[58]: text=112.2, bbox=[732, 306, 777, 320]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[59]: text=14.5, bbox=[828, 306, 862, 320]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[60]: text=MEF 75, bbox=[97, 322, 160, 336]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[61]: text=[L/s], bbox=[282, 322, 320, 337]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[62]: text=5.73, bbox=[344, 322, 380, 336]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[63]: text=3.01, bbox=[455, 322, 492, 336]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[64]: text=52.6, bbox=[541, 322, 577, 336]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[65]: text=3.73, bbox=[654, 322, 690, 336]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[66]: text=65.1, bbox=[741, 322, 777, 336]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[67]: text=23.8, bbox=[828, 322, 862, 336]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[68]: text=MEF 50, bbox=[97, 338, 160, 352]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[69]: text=[L/s], bbox=[282, 338, 320, 353]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[70]: text=4.06, bbox=[344, 338, 380, 352]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[71]: text=1.25, bbox=[455, 338, 492, 352]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[72]: text=30.9, bbox=[541, 338, 577, 352]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[73]: text=1.67, bbox=[654, 338, 690, 352]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[74]: text=41.2, bbox=[741, 338, 777, 352]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[75]: text=33.3, bbox=[828, 338, 862, 352]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[76]: text=MEF 25, bbox=[97, 354, 160, 368]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[77]: text=[L/s], bbox=[282, 354, 320, 369]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[78]: text=1.77, bbox=[344, 354, 380, 368]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[79]: text=0.46, bbox=[455, 354, 492, 368]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[80]: text=26.3, bbox=[541, 354, 577, 368]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[81]: text=0.59, bbox=[654, 354, 690, 368]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[82]: text=33.6, bbox=[741, 354, 777, 368]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[83]: text=27.7, bbox=[828, 354, 862, 368]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[84]: text=MMEF 75/25, bbox=[97, 370, 200, 384]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[85]: text=[L/s], bbox=[282, 370, 320, 385]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[86]: text=3.53, bbox=[344, 370, 380, 384]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[87]: text=1.06, bbox=[455, 370, 492, 384]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[88]: text=30.0, bbox=[541, 370, 577, 384]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[89]: text=1.46, bbox=[654, 370, 690, 384]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[90]: text=41.3, bbox=[741, 370, 777, 384]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[91]: text=37.6, bbox=[828, 370, 862, 384]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[92]: text=FET, bbox=[97, 386, 134, 400]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[93]: text=[s], bbox=[297, 386, 320, 401]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[94]: text=8.73, bbox=[455, 386, 492, 400]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[95]: text=4.94, bbox=[654, 386, 690, 400]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[96]: text=-43.4, bbox=[821, 386, 862, 400]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[97]: text=V backextrapolation ex [L], bbox=[97, 402, 320, 416]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[98]: text=0.06, bbox=[455, 402, 492, 416]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[99]: text=0.07, bbox=[654, 402, 690, 416]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[100]: text=20.1, bbox=[828, 402, 862, 416]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[101]: text=V backextrapol. % FVC [%], bbox=[97, 417, 320, 432]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[102]: text=1.86, bbox=[455, 417, 492, 432]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[103]: text=2.17, bbox=[654, 417, 690, 432]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[104]: text=16.3, bbox=[828, 417, 862, 432]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[105]: text=Flow [L/s], bbox=[150, 500, 201, 512]
2026-08-10 06:17:07,889 INFO     29 [qwen-vl-text] coord item[106]: text=F/V ex, bbox=[589, 501, 622, 511]
2026-08-10 06:17:07,890 INFO     29 [qwen-vl-text] coord item[107]: text=10, bbox=[133, 518, 148, 528]
2026-08-10 06:17:07,890 INFO     29 [qwen-vl-text] coord item[108]: text=5, bbox=[137, 545, 146, 555]
2026-08-10 06:17:07,890 INFO     29 [qwen-vl-text] coord item[109]: text=0, bbox=[137, 572, 146, 582]
2026-08-10 06:17:07,890 INFO     29 [qwen-vl-text] coord item[110]: text=1, bbox=[230, 582, 238, 591]
2026-08-10 06:17:07,890 INFO     29 [qwen-vl-text] coord item[111]: text=2, bbox=[315, 582, 324, 591]
2026-08-10 06:17:07,890 INFO     29 [qwen-vl-text] coord item[112]: text=3, bbox=[402, 582, 410, 591]
2026-08-10 06:17:07,890 INFO     29 [qwen-vl-text] coord item[113]: text=4, bbox=[487, 582, 496, 591]
2026-08-10 06:17:07,890 INFO     29 [qwen-vl-text] coord item[114]: text=5, bbox=[573, 582, 582, 591]
2026-08-10 06:17:07,890 INFO     29 [qwen-vl-text] coord item[115]: text=6, bbox=[661, 582, 670, 591]
2026-08-10 06:17:07,890 INFO     29 [qwen-vl-text] coord item[116]: text=7, bbox=[747, 582, 755, 591]
2026-08-10 06:17:07,890 INFO     29 [qwen-vl-text] coord item[117]: text=10, bbox=[133, 626, 148, 636]
2026-08-10 06:17:07,890 INFO     29 [qwen-vl-text] coord item[118]: text=F/V In, bbox=[593, 644, 622, 654]
2026-08-10 06:17:07,890 INFO     29 [qwen-vl-text] coord item[119]: text=医生意见：, bbox=[93, 664, 197, 681]
2026-08-10 06:17:07,890 INFO     29 [qwen-vl-text] coord item[120]: text=支气管舒张试验阳性。, bbox=[93, 684, 264, 697]
2026-08-10 06:17:07,890 INFO     29 [qwen-vl-text] coord item[121]: text=(通过储雾罐吸入硫酸沙丁胺醇气雾剂400ug20分钟后。, bbox=[93, 697, 526, 710]
2026-08-10 06:17:07,890 INFO     29 [qwen-vl-text] coord item[122]: text=FEV1较基线增加大于12 %，且绝对值增加大于200 ml。, bbox=[93, 709, 519, 722]
2026-08-10 06:17:07,890 INFO     29 [qwen-vl-text] coord item[123]: text=审核医生：孙帅森, bbox=[649, 791, 784, 806]
2026-08-10 06:17:07,890 INFO     29 [qwen-vl-text] coord item[124]: text=检测技师：朱龙华, bbox=[645, 812, 806, 838]
2026-08-10 06:17:07,890 INFO     29 [qwen-vl-text] page=2 — 125/125 coords, api_time=40.5s
2026-08-10 06:17:07,890 INFO     29 [qwen-vl-text] new_positions (125):
[[2, 243.95, 330.22499999999997, 68.202, 85.042], [2, 54.144999999999996, 83.3, 87.568, 98.514], [2, 54.144999999999996, 105.91, 98.514, 109.46], [2, 54.144999999999996, 94.00999999999999, 109.46, 121.24799999999999], [2, 54.144999999999996, 205.27499999999998, 121.24799999999999, 133.036], [2, 54.144999999999996, 105.91, 133.036, 144.82399999999998], [2, 287.385, 318.325, 85.884, 97.672], [2, 287.385, 318.325, 97.672, 109.46], [2, 287.385, 330.22499999999997, 109.46, 121.24799999999999], [2, 287.385, 318.325, 121.24799999999999, 133.036], [2, 204.67999999999998, 226.1, 149.876, 162.506], [2, 276.08, 343.90999999999997, 149.876, 163.34799999999998], [2, 393.29499999999996, 462.315, 149.876, 163.34799999999998], [2, 480.16499999999996, 511.7, 149.876, 162.506], [2, 57.714999999999996, 99.96, 164.19, 175.97799999999998], [2, 256.445, 292.74, 164.19, 175.97799999999998], [2, 373.65999999999997, 410.54999999999995, 164.19, 175.97799999999998], [2, 57.714999999999996, 99.96, 176.82, 188.608], [2, 235.02499999999998, 292.74, 176.82, 188.608], [2, 349.265, 410.54999999999995, 176.82, 188.608], [2, 57.714999999999996, 79.72999999999999, 204.606, 216.394], [2, 176.715, 190.39999999999998, 204.606, 217.236], [2, 204.67999999999998, 226.1, 204.606, 216.394], [2, 270.72499999999997, 292.74, 204.606, 216.394], [2, 316.53999999999996, 343.315, 204.606, 216.394], [2, 389.13, 410.54999999999995, 204.606, 216.394], [2, 435.53999999999996, 462.315, 204.606, 216.394], [2, 498.015, 512.89, 204.606, 216.394], [2, 57.714999999999996, 86.86999999999999, 217.236, 229.024], [2, 176.715, 190.39999999999998, 217.236, 229.86599999999999], [2, 204.67999999999998, 226.1, 217.236, 229.024], [2, 270.72499999999997, 292.74, 217.236, 229.024], [2, 321.895, 343.315, 217.236, 229.024], [2, 389.13, 410.54999999999995, 217.236, 229.024], [2, 440.895, 462.315, 217.236, 229.024], [2, 492.65999999999997, 512.89, 217.236, 229.024], [2, 57.714999999999996, 123.75999999999999, 230.708, 242.49599999999998], [2, 173.73999999999998, 190.39999999999998, 230.708, 243.338], [2, 199.325, 226.1, 230.708, 242.49599999999998], [2, 264.775, 292.74, 230.708, 242.49599999999998], [2, 321.895, 343.315, 230.708, 242.49599999999998], [2, 383.18, 410.54999999999995, 230.708, 242.49599999999998], [2, 440.895, 462.315, 230.708, 242.49599999999998], [2, 498.015, 512.89, 230.708, 242.49599999999998], [2, 57.714999999999996, 143.98999999999998, 244.17999999999998, 255.968], [2, 173.73999999999998, 190.39999999999998, 244.17999999999998, 256.81], [2, 199.325, 226.1, 244.17999999999998, 255.968], [2, 264.775, 292.74, 244.17999999999998, 255.968], [2, 321.895, 343.315, 244.17999999999998, 255.968], [2, 383.18, 410.54999999999995, 244.17999999999998, 255.968], [2, 440.895, 462.315, 244.17999999999998, 255.968], [2, 498.015, 512.89, 244.17999999999998, 255.968], [2, 57.714999999999996, 79.72999999999999, 257.652, 269.44], [2, 167.79, 190.39999999999998, 257.652, 270.282], [2, 204.67999999999998, 226.1, 257.652, 269.44], [2, 270.72499999999997, 292.74, 257.652, 269.44], [2, 321.895, 343.315, 257.652, 269.44], [2, 389.13, 410.54999999999995, 257.652, 269.44], [2, 435.53999999999996, 462.315, 257.652, 269.44], [2, 492.65999999999997, 512.89, 257.652, 269.44], [2, 57.714999999999996, 95.19999999999999, 271.12399999999997, 282.912], [2, 167.79, 190.39999999999998, 271.12399999999997, 283.75399999999996], [2, 204.67999999999998, 226.1, 271.12399999999997, 282.912], [2, 270.72499999999997, 292.74, 271.12399999999997, 282.912], [2, 321.895, 343.315, 271.12399999999997, 282.912], [2, 389.13, 410.54999999999995, 271.12399999999997, 282.912], [2, 440.895, 462.315, 271.12399999999997, 282.912], [2, 492.65999999999997, 512.89, 271.12399999999997, 282.912], [2, 57.714999999999996, 95.19999999999999, 284.596, 296.384], [2, 167.79, 190.39999999999998, 284.596, 297.226], [2, 204.67999999999998, 226.1, 284.596, 296.384], [2, 270.72499999999997, 292.74, 284.596, 296.384], [2, 321.895, 343.315, 284.596, 296.384], [2, 389.13, 410.54999999999995, 284.596, 296.384], [2, 440.895, 462.315, 284.596, 296.384], [2, 492.65999999999997, 512.89, 284.596, 296.384], [2, 57.714999999999996, 95.19999999999999, 298.068, 309.856], [2, 167.79, 190.39999999999998, 298.068, 310.698], [2, 204.67999999999998, 226.1, 298.068, 309.856], [2, 270.72499999999997, 292.74, 298.068, 309.856], [2, 321.895, 343.315, 298.068, 309.856], [2, 389.13, 410.54999999999995, 298.068, 309.856], [2, 440.895, 462.315, 298.068, 309.856], [2, 492.65999999999997, 512.89, 298.068, 309.856], [2, 57.714999999999996, 119.0, 311.53999999999996, 323.328], [2, 167.79, 190.39999999999998, 311.53999999999996, 324.17], [2, 204.67999999999998, 226.1, 311.53999999999996, 323.328], [2, 270.72499999999997, 292.74, 311.53999999999996, 323.328], [2, 321.895, 343.315, 311.53999999999996, 323.328], [2, 389.13, 410.54999999999995, 311.53999999999996, 323.328], [2, 440.895, 462.315, 311.53999999999996, 323.328], [2, 492.65999999999997, 512.89, 311.53999999999996, 323.328], [2, 57.714999999999996, 79.72999999999999, 325.012, 336.8], [2, 176.715, 190.39999999999998, 325.012, 337.642], [2, 270.72499999999997, 292.74, 325.012, 336.8], [2, 389.13, 410.54999999999995, 325.012, 336.8], [2, 488.495, 512.89, 325.012, 336.8], [2, 57.714999999999996, 190.39999999999998, 338.484, 350.272], [2, 270.72499999999997, 292.74, 338.484, 350.272], [2, 389.13, 410.54999999999995, 338.484, 350.272], [2, 492.65999999999997, 512.89, 338.484, 350.272], [2, 57.714999999999996, 190.39999999999998, 351.114, 363.74399999999997], [2, 270.72499999999997, 292.74, 351.114, 363.74399999999997], [2, 389.13, 410.54999999999995, 351.114, 363.74399999999997], [2, 492.65999999999997, 512.89, 351.114, 363.74399999999997], [2, 89.25, 119.595, 421.0, 431.104], [2, 350.455, 370.09, 421.842, 430.262], [2, 79.13499999999999, 88.06, 436.156, 444.57599999999996], [2, 81.515, 86.86999999999999, 458.89, 467.31], [2, 81.515, 86.86999999999999, 481.62399999999997, 490.044], [2, 136.85, 141.60999999999999, 490.044, 497.62199999999996], [2, 187.42499999999998, 192.78, 490.044, 497.62199999999996], [2, 239.19, 243.95, 490.044, 497.62199999999996], [2, 289.765, 295.12, 490.044, 497.62199999999996], [2, 340.935, 346.28999999999996, 490.044, 497.62199999999996], [2, 393.29499999999996, 398.65, 490.044, 497.62199999999996], [2, 444.465, 449.22499999999997, 490.044, 497.62199999999996], [2, 79.13499999999999, 88.06, 527.092, 535.512], [2, 352.835, 370.09, 542.2479999999999, 550.668], [2, 55.335, 117.21499999999999, 559.088, 573.4019999999999], [2, 55.335, 157.07999999999998, 575.928, 586.874], [2, 55.335, 312.96999999999997, 586.874, 597.8199999999999], [2, 55.335, 308.805, 596.978, 607.924], [2, 386.155, 466.47999999999996, 666.0219999999999, 678.6519999999999], [2, 383.775, 479.57, 683.704, 705.596]]
2026-08-10 06:17:07,890 INFO     29 [qwen-vl-text] ═══ DONE ═══ 125 positions, pages=1, time=55.5s
2026-08-10 06:17:07,890 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 06:17:07,897 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:17:07,897 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 06:17:07,897 INFO     29 [qwen-vl-text] positions(151): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 06:17:07,897 INFO     29 [qwen-vl-text] page grouping: [3], lines per page: [151]
2026-08-10 06:17:08,131 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 06:17:08,132 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1055
2026-08-10 06:17:08,132 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:17:08,132 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 394, \"bbox_end\": 544, \"encounter_dates\": [\"2025-04-11\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "肺功能报告单\n姓名：\n出生日期：1984/4/02\n门诊/住院/体检：\n身高：160 cm\n身份证号：\n性别：女\n年龄：41 岁\n测试号：\n体重：50 kg\n测试日期\n测试时间\n预计\n实测 % (实/预)\n25/4/11\n14:56:4\nVT\n[L]\n0.36\n0.41\n114.9\nBF\n[1/min]\n20.00\n20.79\n104.0\nMV\n[L/min]\n7.14\n8.54\n119.5\nERV\n[L]\n1.07\n1.07\n99.4\nVC MAX\n[L]\n3.19\n2.84\n88.9\nFVC\n[L]\n3.13\n2.84\n90.6\nFEV 1\n[L]\n2.70\n1.53\n56.9\nFEV 1 % FVC\n[%]\n83.98\n54.07\n64.4\nFEV 1 % VC MAX\n[%]\n81.31\n54.07\n66.5\nPEF\n[L/s]\n6.46\n4.56\n70.7\nMEF 75\n[L/s]\n5.73\n1.84\n32.1\nMEF 50\n[L/s]\n4.06\n0.84\n20.7\nMEF 25\n[L/s]\n1.77\n0.28\n15.6\nMMEF 75/25\n[L/s]\n3.53\n0.65\n18.3\nFET\n[s]\n8.46\nV backextrapolation ex\n[L]\n0.03\nV backextrapol. % FVC\n[%]\n1.23\nMVV\n[L/min]\n101.93\n75.75\n74.3\nFEV 1*30\n[L/min]\n101.93\n46.03\n45.2\nRV-SB\n[L]\n1.55\n2.56\n164.9\nRV%TLC-SB\n[%]\n32.90\n47.52\n144.4\nTLC-SB\n[L]\n4.77\n5.39\n112.9\nFRC-SB\n[L]\n2.63\n3.31\n126.0\nFRC%TLC-SB\n[%]\n51.66\n61.42\n118.9\nDLCOc SB\n[mmol/min/kPa]\n8.34\n6.95\n83.4\nDLCO SB\n[mmol/min/kPa]\n8.34\n6.95\n83.4\n医生意见：\n1.中重度阻塞性通气功能障碍。\n检查质量：FVC：A级 。 FEV1：A级 。\n备注：受检者检查配合佳。 结果仅供参考，请结合临床分析。\n2.最大自主分钟通气量（MVV）轻度下降。\n备注：患者MVV配合佳。结果仅供参考，请结合临床分析。\n3.弥散功能在正常范围。4.残总比中度增高。\n审核医生：孙帅森\n检测技师：张青苹\n通气弥散B\n2025/4/11 15:18",
    "role": "user"
  }
]
2026-08-10 06:17:08,135 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T06:17:08.135+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 2, "failed": 0, "current": {"801b5176947e11f182aec5d26bc6c4ae": {"id": "801b5176947e11f182aec5d26bc6c4ae", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786340646131, "task_type": "dataflow", "root_trace_id": "97b84aa3d1154f6db808c154432c5554", "root_traceparent": "00-97b84aa3d1154f6db808c154432c5554-dd9503e7c4e14a5d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "dbae825c948211f1bd9827cf206dfa2d": {"id": "dbae825c948211f1bd9827cf206dfa2d", "doc_id": "db492056948211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LGWE-\u827e\u7279\u7f8e\u54ee\u5598-\u6d1b\u9633\u4e09.pdf", "type": "pdf", "location": "LGWE-\u827e\u7279\u7f8e\u54ee\u5598-\u6d1b\u9633\u4e09.pdf", "size": 1648931, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786342517754, "task_type": "dataflow", "root_trace_id": "aaa86c5dcc2c462f88c0ac982e1d484f", "root_traceparent": "00-aaa86c5dcc2c462f88c0ac982e1d484f-c2d6050d16147908-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 06:17:08,458 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 06:17:08,459 INFO     29 [Trace] task=dbae825c | doc=LGWE-艾特美哮喘-洛阳三.pdf | Parser:MedLink | outputs={"html": "", "json": "163 items", "markdown": "", "text": "", "name": "LGWE-艾特美哮喘-洛阳三.pdf", "output_format": "json"}
2026-08-10 06:17:08,459 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 06:17:08,504 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:17:08,505 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 郑州市第一人民医院门诊病历\n[BBOX-1] 科室：呼吸内科一门诊\n[BBOX-2] 就诊日期：2025-05-25\n[BBOX-3] 初诊\n[BBOX-4] 姓名：\n[BBOX-5] 性别：男\n[BBOX-6] 年龄：61岁\n[BBOX-7] ID：\n[BBOX-8] 主 诉：咳嗽、胸闷3月\n[BBOX-9] 现 病 史：3月前出现咳嗽、胸闷，来诊\n[BBOX-10] 既 往 史：无高血压病、冠心病、糖尿病病史，无乙肝、肝炎病史。无\n[BBOX-11] 药物过敏史。\n[BBOX-12] 体格检查：神志清，双肺呼吸音粗，未闻及啰音；\n[BBOX-13] 处 理：完善肺功能\n[BBOX-14] 建 议：门诊口服药物治疗，如出现此疾病复发或症状加重的可能，\n[BBOX-15] 请随时就诊\n[BBOX-16] 诊 断：1.支气管哮喘；\n[BBOX-17] 检查\n[BBOX-18] 肺功能检查+支气管舒张实验\n[BBOX-19] 医生：张朝杰\n[BBOX-20] 打印日期：2025-05-25 12:03\n[BBOX-21] 第 1 页，共 1 页\n[BBOX-22] 郑州市第一人民医院\n[BBOX-23] 肺功能检查报告\n[BBOX-24] 舒张试验\n[BBOX-25] 姓名：\n[BBOX-26] 性别：男\n[BBOX-27] 年龄：61岁\n[BBOX-28] 身高：174 cm\n[BBOX-29] 体重：85 kg\n[BBOX-30] 科别：呼吸内科\n[BBOX-31] 住院号：\n[BBOX-32] 测试号：2025052513\n[BBOX-33] 吸烟史：\n[BBOX-34] 联系电话：\n[BBOX-35] 测试日期 25-5-25\n[BBOX-36] 测试时间 11:46:55\n[BBOX-37] 预计值\n[BBOX-38] 前次\n[BBOX-39] 前/预\n[BBOX-40] 后次\n[BBOX-41] 后/预\n[BBOX-42] 改善率\n[BBOX-43] 25-5-25\n[BBOX-44] 25-5-25\n[BBOX-45] 11:46:55\n[BBOX-46] 11:57:14\n[BBOX-47] FVC [L] 4.10 2.84 69.4 3.49 85.2 22.91\n[BBOX-48] FEV 1 [L] 3.22 2.51 78.0 3.06 95.0 21.81\n[BBOX-49] FEV 1 % FVC [%] 83.40 88.46 106.1 87.66 105.1 -0.90\n[BBOX-50] PEF [L/s] 8.21 6.40 77.9 6.63 80.8 3.68\n[BBOX-51] MEF 75 [L/s] 7.26 6.18 85.1 6.13 84.4 -0.76\n[BBOX-52] MEF 50 [L/s] 4.35 3.04 69.9 4.48 102.9 47.19\n[BBOX-53] MEF 25 [L/s] 1.62 1.18 72.8 1.25 77.6 6.56\n[BBOX-54] MMEF 75/25 [L/s] 3.45 2.26 65.4 3.32 96.0 46.80\n[BBOX-55] Flow [L/s]\n[BBOX-56] F/V ex\n[BBOX-57] 10\n[BBOX-58] 5\n[BBOX-59] 0\n[BBOX-60] 1\n[BBOX-61] 2\n[BBOX-62] 3\n[BBOX-63] 4\n[BBOX-64] 5\n[BBOX-65] F/V In\n[BBOX-66] 6\n[BBOX-67] Vol [L]\n[BBOX-68] 5\n[BBOX-69] Vol%Vmax\n[BBOX-70] 100\n[BBOX-71] V Cmax\n[BBOX-72] 80\n[BBOX-73] 3\n[BBOX-74] 60\n[BBOX-75] 2\n[BBOX-76] 40\n[BBOX-77] 20\n[BBOX-78] 1\n[BBOX-79] 0\n[BBOX-80] 0\n[BBOX-81] Time [s]\n[BBOX-82] 0.0\n[BBOX-83] 0.5\n[BBOX-84] 1.0\n[BBOX-85] 1.5\n[BBOX-86] 2.0\n[BBOX-87] 2.5\n[BBOX-88] 3.0\n[BBOX-89] 测试结果：\n[BBOX-90] 支气管舒张试验阳性。\n[BBOX-91] (请结合临床全面诊断)\n[BBOX-92] 医生签字：毛锦涛\n[BBOX-93] CS 扫描全能王\n[BBOX-94] 3亿人都在用的扫描App\n[BBOX-95] 郑州市第一人民医院\n[BBOX-96] 肺功能检查报告\n[BBOX-97] 常规通气\n[BBOX-98] 姓名：\n[BBOX-99] 性别：男\n[BBOX-100] 年龄：61岁\n[BBOX-101] 身高：174 cm\n[BBOX-102] 科别：呼吸内科\n[BBOX-103] 住院号：门诊\n[BBOX-104] 测试号：2025052513\n[BBOX-105] 体重：85 kg\n[BBOX-106] 测试日期 25-5-25\n[BBOX-107] 测试时间 11:46:55\n[BBOX-108] 预计值 实测值 实/预\n[BBOX-109] IRV [L] 1.14\n[BBOX-110] ERV [L] 3.12\n[BBOX-111] IC [L] 0.61\n[BBOX-112] VT [L] 4.26 0.65 106.5\n[BBOX-113] VC IN [L] 4.26 3.01 70.7\n[BBOX-114] VC EX [L] 4.26 2.84 66.8\n[BBOX-115] BF [1/min] 20.00 17.72 88.6\n[BBOX-116] MV [L/min] 12.14 11.46 94.4\n[BBOX-117] VC MAX [L] 4.26 3.01 70.7\n[BBOX-118] FVC [L] 4.10 2.84 69.4\n[BBOX-119] FEV 1 [L] 3.22 2.51 78.0\n[BBOX-120] FEV 1 % FVC [%] 83.40 88.46 106.1\n[BBOX-121] FEV 1 % VC MAX [%] 76.23 83.54 109.6\n[BBOX-122] PEF [L/s] 8.21 6.40 77.9\n[BBOX-123] MEF 75 [L/s] 7.26 6.18 85.1\n[BBOX-124] MEF 50 [L/s] 4.35 3.04 69.9\n[BBOX-125] MEF 25 [L/s] 1.62 1.18 72.8\n[BBOX-126] MMEF 75/25 [L/s] . 3.45 2.26 65.4\n[BBOX-127] MVV [L/min] 119.91 77.46 64.6\n[BBOX-128] FEV 1*30 [L/min] 119.91 75.39 62.9\n[BBOX-129] Vol [L]\n[BBOX-130] TLC 6\n[BBOX-131] FRC pleth\n[BBOX-132] RV 2\n[BBOX-133] PredA0.0 0.2 0.4 0.6 0.8 1.0\n[BBOX-134] Time [min]\n[BBOX-135] Flow [L/s]\n[BBOX-136] F/V ex\n[BBOX-137] 10\n[BBOX-138] 5\n[BBOX-139] 0\n[BBOX-140] 1\n[BBOX-141] 2\n[BBOX-142] 3\n[BBOX-143] 4\n[BBOX-144] 5\n[BBOX-145] F/V in\n[BBOX-146] Vol [L]\n[BBOX-147] 2\n[BBOX-148] 1\n[BBOX-149] 0\n[BBOX-150] 1\n[BBOX-151] 2\n[BBOX-152] Time [s]\n[BBOX-153] 0 2 4 6 8 10 12\n[BBOX-154] 测试结果：\n[BBOX-155] 提示：\n[BBOX-156] 1、轻度阻塞性肺通气功能障碍；\n[BBOX-157] 2、肺储备功能下降。\n[BBOX-158] (请结合临床全面诊断)\n[BBOX-159] 医生签字：毛锦涛\n[BBOX-160] 报告日期：2025-5-27\n[BBOX-161] CS 扫描全能王\n[BBOX-162] 3亿人都在用的扫描App"
  }
]
2026-08-10 06:17:12,435 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:17:12,466 INFO     29 [SmartSplitter] SmartSplitter done: 3 chunks from 3 LLM segments (all bbox_id). Types: {'OutpatientRecord': 1, 'ExaminationReport': 2}
2026-08-10 06:17:12,487 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 06:17:12,487 INFO     29 [Trace] task=dbae825c | doc=LGWE-艾特美哮喘-洛阳三.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "163 items", "markdown": "", "text": "", "name": "LGWE-艾特美哮喘-洛阳三.pdf", "output_format": "chunks", "chunks": "3 items, types={'OutpatientRecord': 1, 'ExaminationReport': 2}"}
2026-08-10 06:17:12,487 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 06:17:12,488 INFO     29 [ChunkRouter] Routed 3 chunks into 2 groups: {'chunks_Clinical': 1, 'chunks_Examination': 2}
2026-08-10 06:17:12,500 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 06:17:12,501 INFO     29 [Trace] task=dbae825c | doc=LGWE-艾特美哮喘-洛阳三.pdf | ChunkRouter:Router | outputs={"html": "", "json": "163 items", "markdown": "", "text": "", "name": "LGWE-艾特美哮喘-洛阳三.pdf", "output_format": "chunks", "chunks": "3 items, types={'OutpatientRecord': 1, 'ExaminationReport': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 06:17:12,501 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 06:17:12,510 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:17:12,511 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:17:13,108 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:17:13,120 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 06:17:13,120 INFO     29 [Trace] task=dbae825c | doc=LGWE-艾特美哮喘-洛阳三.pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "163 items", "markdown": "", "text": "", "name": "LGWE-艾特美哮喘-洛阳三.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 06:17:13,120 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 06:17:13,130 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:17:13,130 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:17:13,983 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:17:13,996 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 06:17:13,997 INFO     29 [Trace] task=dbae825c | doc=LGWE-艾特美哮喘-洛阳三.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "163 items", "markdown": "", "text": "", "name": "LGWE-艾特美哮喘-洛阳三.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 06:17:13,997 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 06:17:14,003 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 06:17:14,004 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:17:14,004 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 06:17:14,004 INFO     29 [qwen-vl-text] positions(22): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 06:17:14,004 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [22]
2026-08-10 06:17:14,226 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 06:17:14,226 INFO     29 [qwen-vl-text] LLM extraction start, text_len=276
2026-08-10 06:17:14,227 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:17:14,227 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 21, \"encounter_dates\": [\"2025-05-25\"], \"department\": \"呼吸内科一门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "郑州市第一人民医院门诊病历\n科室：呼吸内科一门诊\n就诊日期：2025-05-25\n初诊\n姓名：\n性别：男\n年龄：61岁\nID：\n主 诉：咳嗽、胸闷3月\n现 病 史：3月前出现咳嗽、胸闷，来诊\n既 往 史：无高血压病、冠心病、糖尿病病史，无乙肝、肝炎病史。无\n药物过敏史。\n体格检查：神志清，双肺呼吸音粗，未闻及啰音；\n处 理：完善肺功能\n建 议：门诊口服药物治疗，如出现此疾病复发或症状加重的可能，\n请随时就诊\n诊 断：1.支气管哮喘；\n检查\n肺功能检查+支气管舒张实验\n医生：张朝杰\n打印日期：2025-05-25 12:03\n第 1 页，共 1 页",
    "role": "user"
  }
]
2026-08-10 06:17:17,156 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:17:17,156 INFO     29 [qwen-vl-text] LLM output (len=225):
{
  "encounter_date": "2025-05-25",
  "chief_complaint": "咳嗽、胸闷3月",
  "present_illness": "3月前出现咳嗽、胸闷，来诊",
  "past_history": "无高血压病、冠心病、糖尿病病史，无乙肝、肝炎病史。无药物过敏史。",
  "diagnosis": "1.支气管哮喘；",
  "treatment_plan": "完善肺功能；门诊口服药物治疗"
}
2026-08-10 06:17:17,156 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-05-25]
2026-08-10 06:17:17,159 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=709343, prompt_len=955
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["郑州市第一人民医院门诊病历", "科室：呼吸内科一门诊", "就诊日期：2025-05-25", "初诊", "姓名：", "性别：男", "年龄：61岁", "ID：", "主 诉：咳嗽、胸闷3月", "现 病 史：3月前出现咳嗽、胸闷，来诊", "既 往 史：无高血压病、冠心病、糖尿病病史，无乙肝、肝炎病史。无", "药物过敏史。", "体格检查：神志清，双肺呼吸音粗，未闻及啰音；", "处 理：完善肺功能", "建 议：门诊口服药物治疗，如出现此疾病复发或症状加重的可能，", "请随时就诊", "诊 断：1.支气管哮喘；", "检查", "肺功能检查+支气管舒张实验", "医生：张朝杰", "打印日期：2025-05-25 12:03", "第 1 页，共 1 页"]

## 定位规则
1. 对于列表中的每行文本，找到它在图片中**精确出现**的位置
2. bbox必须是该行文字的**最小紧密包围框**，紧贴文字边缘，不要包含额外的空白区域
3. 坐标归一化到0-1000，格式[x1,y1,x2,y2]
4. 如果某行文本在图片中未找到，跳过不输出
5. text字段必须与给定的文本完全一致

## 包围框精度要求
- x1必须紧贴该行第一个字符的左边缘
- x2必须紧贴该行最后一个字符的右边缘
- y1必须紧贴该行文字的顶部
- y2必须紧贴该行文字的底部
- 禁止将多行文字合并到同一个bbox中

## 严格JSON格式要求
直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。
正确示例：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230]},
  {"text": "年龄：68岁", "bbox": [100, 250, 270, 280]}
]
错误示例（禁止额外字段）：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230], "label": "个人信息"}
]
请直接输出纯JSON数组，不要用markdown代码块包裹。
2026-08-10 06:17:24,684 INFO     29 [qwen-vl-text] coord API raw response (len=1239):
[
	{"text": "郑州市第一人民医院门诊病历", "bbox": [295, 31, 742, 63]},
	{"text": "科室：呼吸内科一门诊", "bbox": [166, 77, 381, 96]},
	{"text": "就诊日期：2025-05-25", "bbox": [523, 76, 734, 94]},
	{"text": "初诊", "bbox": [793, 77, 835, 94]},
	{"text": "姓名：", "bbox": [166, 108, 218, 126]},
	{"text": "性别：男", "bbox": [373, 108, 453, 125]},
	{"text": "年龄：61岁", "bbox": [495, 107, 600, 125]},
	{"text": "ID：", "bbox": [629, 108, 664, 125]},
	{"text": "主 诉：咳嗽、胸闷3月", "bbox": [173, 139, 416, 157]},
	{"text": "现 病 史：3月前出现咳嗽、胸闷，来诊", "bbox": [173, 177, 544, 195]},
	{"text": "既 往 史：无高血压病、冠心病、糖尿病病史，无乙肝、肝炎病史。无", "bbox": [173, 245, 836, 263]},
	{"text": "药物过敏史。", "bbox": [173, 264, 290, 281]},
	{"text": "体格检查：神志清，双肺呼吸音粗，未闻及啰音；", "bbox": [173, 303, 627, 321]},
	{"text": "处 理：完善肺功能", "bbox": [173, 406, 388, 423]},
	{"text": "建 议：门诊口服药物治疗，如出现此疾病复发或症状加重的可能，", "bbox": [173, 491, 817, 509]},
	{"text": "请随时就诊", "bbox": [173, 509, 279, 526]},
	{"text": "诊 断：1.支气管哮喘；", "bbox": [173, 597, 418, 615]},
	{"text": "检查", "bbox": [176, 672, 219, 689]},
	{"text": "肺功能检查+支气管舒张实验", "bbox": [173, 696, 442, 714]},
	{"text": "医生：张朝杰", "bbox": [178, 751, 360, 770]},
	{"text": "打印日期：2025-05-25 12:03", "bbox": [541, 753, 811, 770]},
	{"text": "第 1 页，共 1 页", "bbox": [434, 818, 588, 836]}
]
2026-08-10 06:17:24,684 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=7.5s
2026-08-10 06:17:24,684 INFO     29 [qwen-vl-text] coord item[0]: text=郑州市第一人民医院门诊病历, bbox=[295, 31, 742, 63]
2026-08-10 06:17:24,685 INFO     29 [qwen-vl-text] coord item[1]: text=科室：呼吸内科一门诊, bbox=[166, 77, 381, 96]
2026-08-10 06:17:24,685 INFO     29 [qwen-vl-text] coord item[2]: text=就诊日期：2025-05-25, bbox=[523, 76, 734, 94]
2026-08-10 06:17:24,685 INFO     29 [qwen-vl-text] coord item[3]: text=初诊, bbox=[793, 77, 835, 94]
2026-08-10 06:17:24,685 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[166, 108, 218, 126]
2026-08-10 06:17:24,685 INFO     29 [qwen-vl-text] coord item[5]: text=性别：男, bbox=[373, 108, 453, 125]
2026-08-10 06:17:24,685 INFO     29 [qwen-vl-text] coord item[6]: text=年龄：61岁, bbox=[495, 107, 600, 125]
2026-08-10 06:17:24,685 INFO     29 [qwen-vl-text] coord item[7]: text=ID：, bbox=[629, 108, 664, 125]
2026-08-10 06:17:24,685 INFO     29 [qwen-vl-text] coord item[8]: text=主 诉：咳嗽、胸闷3月, bbox=[173, 139, 416, 157]
2026-08-10 06:17:24,685 INFO     29 [qwen-vl-text] coord item[9]: text=现 病 史：3月前出现咳嗽、胸闷，来诊, bbox=[173, 177, 544, 195]
2026-08-10 06:17:24,685 INFO     29 [qwen-vl-text] coord item[10]: text=既 往 史：无高血压病、冠心病、糖尿病病史，无乙肝、肝炎病史。无, bbox=[173, 245, 836, 263]
2026-08-10 06:17:24,685 INFO     29 [qwen-vl-text] coord item[11]: text=药物过敏史。, bbox=[173, 264, 290, 281]
2026-08-10 06:17:24,686 INFO     29 [qwen-vl-text] coord item[12]: text=体格检查：神志清，双肺呼吸音粗，未闻及啰音；, bbox=[173, 303, 627, 321]
2026-08-10 06:17:24,686 INFO     29 [qwen-vl-text] coord item[13]: text=处 理：完善肺功能, bbox=[173, 406, 388, 423]
2026-08-10 06:17:24,686 INFO     29 [qwen-vl-text] coord item[14]: text=建 议：门诊口服药物治疗，如出现此疾病复发或症状加重的可能，, bbox=[173, 491, 817, 509]
2026-08-10 06:17:24,686 INFO     29 [qwen-vl-text] coord item[15]: text=请随时就诊, bbox=[173, 509, 279, 526]
2026-08-10 06:17:24,686 INFO     29 [qwen-vl-text] coord item[16]: text=诊 断：1.支气管哮喘；, bbox=[173, 597, 418, 615]
2026-08-10 06:17:24,686 INFO     29 [qwen-vl-text] coord item[17]: text=检查, bbox=[176, 672, 219, 689]
2026-08-10 06:17:24,686 INFO     29 [qwen-vl-text] coord item[18]: text=肺功能检查+支气管舒张实验, bbox=[173, 696, 442, 714]
2026-08-10 06:17:24,686 INFO     29 [qwen-vl-text] coord item[19]: text=医生：张朝杰, bbox=[178, 751, 360, 770]
2026-08-10 06:17:24,686 INFO     29 [qwen-vl-text] coord item[20]: text=打印日期：2025-05-25 12:03, bbox=[541, 753, 811, 770]
2026-08-10 06:17:24,686 INFO     29 [qwen-vl-text] coord item[21]: text=第 1 页，共 1 页, bbox=[434, 818, 588, 836]
2026-08-10 06:17:24,687 INFO     29 [qwen-vl-text] page=0 — 22/22 coords, api_time=7.5s
2026-08-10 06:17:24,687 INFO     29 [qwen-vl-text] new_positions (22):
[[0, 175.525, 441.48999999999995, 26.102, 53.046], [0, 98.77, 226.695, 64.834, 80.832], [0, 311.185, 436.72999999999996, 63.992, 79.148], [0, 471.835, 496.825, 64.834, 79.148], [0, 98.77, 129.71, 90.93599999999999, 106.092], [0, 221.935, 269.53499999999997, 90.93599999999999, 105.25], [0, 294.525, 357.0, 90.094, 105.25], [0, 374.255, 395.08, 90.93599999999999, 105.25], [0, 102.935, 247.51999999999998, 117.038, 132.194], [0, 102.935, 323.68, 149.034, 164.19], [0, 102.935, 497.41999999999996, 206.29, 221.446], [0, 102.935, 172.54999999999998, 222.28799999999998, 236.602], [0, 102.935, 373.065, 255.126, 270.282], [0, 102.935, 230.85999999999999, 341.852, 356.166], [0, 102.935, 486.11499999999995, 413.42199999999997, 428.578], [0, 102.935, 166.005, 428.578, 442.892], [0, 102.935, 248.70999999999998, 502.674, 517.8299999999999], [0, 104.72, 130.305, 565.824, 580.138], [0, 102.935, 262.99, 586.0319999999999, 601.188], [0, 105.91, 214.2, 632.342, 648.34], [0, 321.895, 482.54499999999996, 634.026, 648.34], [0, 258.22999999999996, 349.85999999999996, 688.756, 703.9119999999999]]
2026-08-10 06:17:24,687 INFO     29 [qwen-vl-text] ═══ DONE ═══ 22 positions, pages=1, time=10.7s
2026-08-10 06:17:24,697 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 06:17:24,697 INFO     29 [Trace] task=dbae825c | doc=LGWE-艾特美哮喘-洛阳三.pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "163 items", "markdown": "", "text": "", "name": "LGWE-艾特美哮喘-洛阳三.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 06:17:24,697 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 06:17:24,705 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:17:24,705 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:17:25,776 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:17:25,786 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 06:17:25,786 INFO     29 [Trace] task=dbae825c | doc=LGWE-艾特美哮喘-洛阳三.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "163 items", "markdown": "", "text": "", "name": "LGWE-艾特美哮喘-洛阳三.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 06:17:25,786 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 06:17:25,794 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:17:25,794 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:17:26,470 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:17:26,483 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:17:26,483 INFO     29 [qwen-vl-text] LLM output (len=1244):
{
  "exam_date": "2025-04-11",
  "report_date": "2025-04-11",
  "exam_name": "肺功能检查",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": "预计 实测 % (实/预)\nVT [L] 0.36 0.41 114.9\nBF [1/min] 20.00 20.79 104.0\nMV [L/min] 7.14 8.54 119.5\nERV [L] 1.07 1.07 99.4\nVC MAX [L] 3.19 2.84 88.9\nFVC [L] 3.13 2.84 90.6\nFEV 1 [L] 2.70 1.53 56.9\nFEV 1 % FVC [%] 83.98 54.07 64.4\nFEV 1 % VC MAX [%] 81.31 54.07 66.5\nPEF [L/s] 6.46 4.56 70.7\nMEF 75 [L/s] 5.73 1.84 32.1\nMEF 50 [L/s] 4.06 0.84 20.7\nMEF 25 [L/s] 1.77 0.28 15.6\nMMEF 75/25 [L/s] 3.53 0.65 18.3\nFET [s] 8.46\nV backextrapolation ex [L] 0.03\nV backextrapol. % FVC [%] 1.23\nMVV [L/min] 101.93 75.75 74.3\nFEV 1*30 [L/min] 101.93 46.03 45.2\nRV-SB [L] 1.55 2.56 164.9\nRV%TLC-SB [%] 32.90 47.52 144.4\nTLC-SB [L] 4.77 5.39 112.9\nFRC-SB [L] 2.63 3.31 126.0\nFRC%TLC-SB [%] 51.66 61.42 118.9\nDLCOc SB [mmol/min/kPa] 8.34 6.95 83.4\nDLCO SB [mmol/min/kPa] 8.34 6.95 83.4\n检查质量：FVC：A级 。 FEV1：A级 。\n备注：受检者检查配合佳。 结果仅供参考，请结合临床分析。\n备注：患者MVV配合佳。结果仅供参考，请结合临床分析。",
  "conclusion": "1.中重度阻塞性通气功能障碍。\n2.最大自主分钟通气量（MVV）轻度下降。\n3.弥散功能在正常范围。\n4.残总比中度增高。",
  "physician": "张青苹",
  "reviewer": "孙帅森"
}
2026-08-10 06:17:26,487 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1165294, prompt_len=2122
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共151行）
["肺功能报告单", "姓名：", "出生日期：1984/4/02", "门诊/住院/体检：", "身高：160 cm", "身份证号：", "性别：女", "年龄：41 岁", "测试号：", "体重：50 kg", "测试日期", "测试时间", "预计", "实测 % (实/预)", "25/4/11", "14:56:4", "VT", "[L]", "0.36", "0.41", "114.9", "BF", "[1/min]", "20.00", "20.79", "104.0", "MV", "[L/min]", "7.14", "8.54", "119.5", "ERV", "[L]", "1.07", "1.07", "99.4", "VC MAX", "[L]", "3.19", "2.84", "88.9", "FVC", "[L]", "3.13", "2.84", "90.6", "FEV 1", "[L]", "2.70", "1.53", "56.9", "FEV 1 % FVC", "[%]", "83.98", "54.07", "64.4", "FEV 1 % VC MAX", "[%]", "81.31", "54.07", "66.5", "PEF", "[L/s]", "6.46", "4.56", "70.7", "MEF 75", "[L/s]", "5.73", "1.84", "32.1", "MEF 50", "[L/s]", "4.06", "0.84", "20.7", "MEF 25", "[L/s]", "1.77", "0.28", "15.6", "MMEF 75/25", "[L/s]", "3.53", "0.65", "18.3", "FET", "[s]", "8.46", "V backextrapolation ex", "[L]", "0.03", "V backextrapol. % FVC", "[%]", "1.23", "MVV", "[L/min]", "101.93", "75.75", "74.3", "FEV 1*30", "[L/min]", "101.93", "46.03", "45.2", "RV-SB", "[L]", "1.55", "2.56", "164.9", "RV%TLC-SB", "[%]", "32.90", "47.52", "144.4", "TLC-SB", "[L]", "4.77", "5.39", "112.9", "FRC-SB", "[L]", "2.63", "3.31", "126.0", "FRC%TLC-SB", "[%]", "51.66", "61.42", "118.9", "DLCOc SB", "[mmol/min/kPa]", "8.34", "6.95", "83.4", "DLCO SB", "[mmol/min/kPa]", "8.34", "6.95", "83.4", "医生意见：", "1.中重度阻塞性通气功能障碍。", "检查质量：FVC：A级 。 FEV1：A级 。", "备注：受检者检查配合佳。 结果仅供参考，请结合临床分析。", "2.最大自主分钟通气量（MVV）轻度下降。", "备注：患者MVV配合佳。结果仅供参考，请结合临床分析。", "3.弥散功能在正常范围。4.残总比中度增高。", "审核医生：孙帅森", "检测技师：张青苹", "通气弥散B", "2025/4/11 15:18"]

## 定位规则
1. 对于列表中的每行文本，找到它在图片中**精确出现**的位置
2. bbox必须是该行文字的**最小紧密包围框**，紧贴文字边缘，不要包含额外的空白区域
3. 坐标归一化到0-1000，格式[x1,y1,x2,y2]
4. 如果某行文本在图片中未找到，跳过不输出
5. text字段必须与给定的文本完全一致

## 包围框精度要求
- x1必须紧贴该行第一个字符的左边缘
- x2必须紧贴该行最后一个字符的右边缘
- y1必须紧贴该行文字的顶部
- y2必须紧贴该行文字的底部
- 禁止将多行文字合并到同一个bbox中

## 严格JSON格式要求
直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。
正确示例：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230]},
  {"text": "年龄：68岁", "bbox": [100, 250, 270, 280]}
]
错误示例（禁止额外字段）：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230], "label": "个人信息"}
]
请直接输出纯JSON数组，不要用markdown代码块包裹。
2026-08-10 06:18:06,058 INFO     29 [qwen-vl-text] coord API raw response (len=7708):
[
	{"text": "肺功能报告单", "bbox": [407, 59, 548, 77]},
	{"text": "姓名：", "bbox": [83, 88, 135, 103]},
	{"text": "出生日期：", "bbox": [83, 103, 176, 117]},
	{"text": "门诊/住院/体检：", "bbox": [83, 117, 240, 131]},
	{"text": "身高：", "bbox": [83, 131, 135, 145]},
	{"text": "身份证号：", "bbox": [83, 145, 176, 159]},
	{"text": "性别：", "bbox": [476, 88, 527, 103]},
	{"text": "年龄：", "bbox": [476, 103, 527, 117]},
	{"text": "测试号：", "bbox": [476, 117, 548, 131]},
	{"text": "体重：", "bbox": [476, 131, 527, 145]},
	{"text": "测试日期", "bbox": [109, 189, 181, 203]},
	{"text": "测试时间", "bbox": [109, 203, 181, 218]},
	{"text": "预计", "bbox": [373, 173, 409, 188]},
	{"text": "实测 % (实/预)", "bbox": [445, 173, 553, 188]},
	{"text": "25/4/11", "bbox": [419, 190, 480, 203]},
	{"text": "14:56:4", "bbox": [419, 205, 480, 218]},
	{"text": "VT", "bbox": [109, 236, 128, 249]},
	{"text": "[L]", "bbox": [320, 236, 344, 250]},
	{"text": "0.36", "bbox": [373, 236, 409, 249]},
	{"text": "0.41", "bbox": [445, 236, 480, 249]},
	{"text": "114.9", "bbox": [510, 236, 553, 249]},
	{"text": "BF", "bbox": [109, 250, 128, 264]},
	{"text": "[1/min]", "bbox": [285, 250, 344, 264]},
	{"text": "20.00", "bbox": [364, 250, 409, 264]},
	{"text": "20.79", "bbox": [436, 250, 480, 264]},
	{"text": "104.0", "bbox": [510, 250, 553, 264]},
	{"text": "MV", "bbox": [109, 265, 128, 279]},
	{"text": "[L/min]", "bbox": [285, 265, 344, 279]},
	{"text": "7.14", "bbox": [373, 265, 409, 279]},
	{"text": "8.54", "bbox": [445, 265, 480, 279]},
	{"text": "119.5", "bbox": [510, 265, 553, 279]},
	{"text": "ERV", "bbox": [109, 280, 137, 293]},
	{"text": "[L]", "bbox": [320, 280, 344, 294]},
	{"text": "1.07", "bbox": [373, 280, 409, 293]},
	{"text": "1.07", "bbox": [445, 280, 480, 293]},
	{"text": "99.4", "bbox": [517, 280, 553, 293]},
	{"text": "VC MAX", "bbox": [109, 295, 164, 309]},
	{"text": "[L]", "bbox": [320, 295, 344, 309]},
	{"text": "3.19", "bbox": [373, 295, 409, 309]},
	{"text": "2.84", "bbox": [445, 295, 480, 309]},
	{"text": "88.9", "bbox": [517, 295, 553, 309]},
	{"text": "FVC", "bbox": [109, 326, 137, 339]},
	{"text": "[L]", "bbox": [320, 326, 344, 340]},
	{"text": "3.13", "bbox": [373, 326, 409, 339]},
	{"text": "2.84", "bbox": [445, 326, 480, 339]},
	{"text": "90.6", "bbox": [517, 326, 553, 339]},
	{"text": "FEV 1", "bbox": [109, 341, 153, 355]},
	{"text": "[L]", "bbox": [320, 341, 344, 355]},
	{"text": "2.70", "bbox": [373, 341, 409, 355]},
	{"text": "1.53", "bbox": [445, 341, 480, 355]},
	{"text": "56.9", "bbox": [517, 341, 553, 355]},
	{"text": "FEV 1 % FVC", "bbox": [109, 356, 210, 370]},
	{"text": "[%]", "bbox": [320, 356, 344, 370]},
	{"text": "83.98", "bbox": [364, 356, 409, 370]},
	{"text": "54.07", "bbox": [436, 356, 480, 370]},
	{"text": "64.4", "bbox": [517, 356, 553, 370]},
	{"text": "FEV 1 % VC MAX", "bbox": [109, 371, 237, 385]},
	{"text": "[%]", "bbox": [320, 371, 344, 385]},
	{"text": "81.31", "bbox": [364, 371, 409, 385]},
	{"text": "54.07", "bbox": [436, 371, 480, 385]},
	{"text": "66.5", "bbox": [517, 371, 553, 385]},
	{"text": "PEF", "bbox": [109, 386, 137, 400]},
	{"text": "[L/s]", "bbox": [302, 386, 344, 400]},
	{"text": "6.46", "bbox": [373, 386, 409, 400]},
	{"text": "4.56", "bbox": [436, 386, 480, 400]},
	{"text": "70.7", "bbox": [517, 386, 553, 400]},
	{"text": "MEF 75", "bbox": [109, 401, 164, 415]},
	{"text": "[L/s]", "bbox": [302, 401, 344, 415]},
	{"text": "5.73", "bbox": [373, 401, 409, 415]},
	{"text": "1.84", "bbox": [445, 401, 480, 415]},
	{"text": "32.1", "bbox": [517, 401, 553, 415]},
	{"text": "MEF 50", "bbox": [109, 416, 164, 430]},
	{"text": "[L/s]", "bbox": [302, 416, 344, 430]},
	{"text": "4.06", "bbox": [373, 416, 409, 430]},
	{"text": "0.84", "bbox": [445, 416, 480, 430]},
	{"text": "20.7", "bbox": [517, 416, 553, 430]},
	{"text": "MEF 25", "bbox": [109, 431, 164, 445]},
	{"text": "[L/s]", "bbox": [302, 431, 344, 445]},
	{"text": "1.77", "bbox": [373, 431, 409, 445]},
	{"text": "0.28", "bbox": [445, 431, 480, 445]},
	{"text": "15.6", "bbox": [517, 431, 553, 445]},
	{"text": "MMEF 75/25", "bbox": [109, 446, 200, 460]},
	{"text": "[L/s]", "bbox": [302, 446, 344, 460]},
	{"text": "3.53", "bbox": [373, 446, 409, 460]},
	{"text": "0.65", "bbox": [445, 446, 480, 460]},
	{"text": "18.3", "bbox": [517, 446, 553, 460]},
	{"text": "FET", "bbox": [109, 461, 137, 475]},
	{"text": "[s]", "bbox": [320, 461, 344, 475]},
	{"text": "8.46", "bbox": [445, 461, 480, 475]},
	{"text": "V backextrapolation ex", "bbox": [109, 476, 307, 490]},
	{"text": "[L]", "bbox": [320, 476, 344, 490]},
	{"text": "0.03", "bbox": [445, 476, 480, 490]},
	{"text": "V backextrapol. % FVC", "bbox": [109, 491, 300, 505]},
	{"text": "[%]", "bbox": [320, 491, 344, 505]},
	{"text": "1.23", "bbox": [445, 491, 480, 505]},
	{"text": "MVV", "bbox": [109, 523, 137, 537]},
	{"text": "[L/min]", "bbox": [285, 523, 344, 537]},
	{"text": "101.93", "bbox": [356, 523, 409, 537]},
	{"text": "75.75", "bbox": [436, 523, 480, 537]},
	{"text": "74.3", "bbox": [517, 523, 553, 537]},
	{"text": "FEV 1*30", "bbox": [109, 538, 181, 552]},
	{"text": "[L/min]", "bbox": [285, 538, 344, 552]},
	{"text": "101.93", "bbox": [356, 538, 409, 552]},
	{"text": "46.03", "bbox": [436, 538, 480, 552]},
	{"text": "45.2", "bbox": [517, 538, 553, 552]},
	{"text": "RV-SB", "bbox": [109, 569, 153, 583]},
	{"text": "[L]", "bbox": [320, 569, 344, 583]},
	{"text": "1.55", "bbox": [373, 569, 409, 583]},
	{"text": "2.56", "bbox": [445, 569, 480, 583]},
	{"text": "164.9", "bbox": [508, 569, 553, 583]},
	{"text": "RV%TLC-SB", "bbox": [109, 584, 190, 598]},
	{"text": "[%]", "bbox": [320, 584, 344, 598]},
	{"text": "32.90", "bbox": [364, 584, 409, 598]},
	{"text": "47.52", "bbox": [436, 584, 480, 598]},
	{"text": "144.4", "bbox": [508, 584, 553, 598]},
	{"text": "TLC-SB", "bbox": [109, 600, 162, 613]},
	{"text": "[L]", "bbox": [320, 600, 344, 613]},
	{"text": "4.77", "bbox": [373, 600, 409, 613]},
	{"text": "5.39", "bbox": [445, 600, 480, 613]},
	{"text": "112.9", "bbox": [508, 600, 553, 613]},
	{"text": "FRC-SB", "bbox": [109, 614, 162, 628]},
	{"text": "[L]", "bbox": [320, 614, 344, 628]},
	{"text": "2.63", "bbox": [373, 614, 409, 628]},
	{"text": "3.31", "bbox": [445, 614, 480, 628]},
	{"text": "126.0", "bbox": [508, 614, 553, 628]},
	{"text": "FRC%TLC-SB", "bbox": [109, 629, 198, 643]},
	{"text": "[%]", "bbox": [320, 629, 344, 643]},
	{"text": "51.66", "bbox": [364, 629, 409, 643]},
	{"text": "61.42", "bbox": [436, 629, 480, 643]},
	{"text": "118.9", "bbox": [508, 629, 553, 643]},
	{"text": "DLCOc SB", "bbox": [109, 645, 180, 659]},
	{"text": "[mmol/min/kPa]", "bbox": [218, 645, 344, 659]},
	{"text": "8.34", "bbox": [373, 645, 409, 659]},
	{"text": "6.95", "bbox": [445, 645, 480, 659]},
	{"text": "83.4", "bbox": [517, 645, 553, 659]},
	{"text": "DLCO SB", "bbox": [109, 660, 171, 674]},
	{"text": "[mmol/min/kPa]", "bbox": [218, 660, 344, 674]},
	{"text": "8.34", "bbox": [373, 660, 409, 674]},
	{"text": "6.95", "bbox": [445, 660, 480, 674]},
	{"text": "83.4", "bbox": [517, 660, 553, 674]},
	{"text": "医生意见：", "bbox": [87, 705, 190, 722]},
	{"text": "1.中重度阻塞性通气功能障碍。", "bbox": [87, 727, 327, 740]},
	{"text": "检查质量：FVC：A级 。 FEV1：A级 。", "bbox": [87, 740, 400, 753]},
	{"text": "备注：受检者检查配合佳。 结果仅供参考，请结合临床分析。", "bbox": [87, 751, 594, 765]},
	{"text": "2.最大自主分钟通气量（MVV）轻度下降。", "bbox": [87, 764, 409, 777]},
	{"text": "备注：患者MVV配合佳。结果仅供参考，请结合临床分析。", "bbox": [87, 776, 532, 789]},
	{"text": "3.弥散功能在正常范围。4.残总比中度增高。", "bbox": [87, 788, 435, 801]},
	{"text": "审核医生：孙帅森", "bbox": [555, 841, 697, 857]},
	{"text": "检测技师：张青苹", "bbox": [552, 861, 703, 877]},
	{"text": "通气弥散B", "bbox": [72, 906, 123, 915]},
	{"text": "2025/4/11 15:18", "bbox": [451, 906, 529, 915]},
	{"text": "1/1", "bbox": [901, 907, 914, 915]}
]
2026-08-10 06:18:06,059 INFO     29 [qwen-vl-text] coord API: raw_items=152, valid_items=152, elapsed=39.6s
2026-08-10 06:18:06,059 INFO     29 [qwen-vl-text] coord item[0]: text=肺功能报告单, bbox=[407, 59, 548, 77]
2026-08-10 06:18:06,060 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[83, 88, 135, 103]
2026-08-10 06:18:06,060 INFO     29 [qwen-vl-text] coord item[2]: text=出生日期：, bbox=[83, 103, 176, 117]
2026-08-10 06:18:06,060 INFO     29 [qwen-vl-text] coord item[3]: text=门诊/住院/体检：, bbox=[83, 117, 240, 131]
2026-08-10 06:18:06,060 INFO     29 [qwen-vl-text] coord item[4]: text=身高：, bbox=[83, 131, 135, 145]
2026-08-10 06:18:06,060 INFO     29 [qwen-vl-text] coord item[5]: text=身份证号：, bbox=[83, 145, 176, 159]
2026-08-10 06:18:06,060 INFO     29 [qwen-vl-text] coord item[6]: text=性别：, bbox=[476, 88, 527, 103]
2026-08-10 06:18:06,060 INFO     29 [qwen-vl-text] coord item[7]: text=年龄：, bbox=[476, 103, 527, 117]
2026-08-10 06:18:06,060 INFO     29 [qwen-vl-text] coord item[8]: text=测试号：, bbox=[476, 117, 548, 131]
2026-08-10 06:18:06,060 INFO     29 [qwen-vl-text] coord item[9]: text=体重：, bbox=[476, 131, 527, 145]
2026-08-10 06:18:06,060 INFO     29 [qwen-vl-text] coord item[10]: text=测试日期, bbox=[109, 189, 181, 203]
2026-08-10 06:18:06,060 INFO     29 [qwen-vl-text] coord item[11]: text=测试时间, bbox=[109, 203, 181, 218]
2026-08-10 06:18:06,061 INFO     29 [qwen-vl-text] coord item[12]: text=预计, bbox=[373, 173, 409, 188]
2026-08-10 06:18:06,061 INFO     29 [qwen-vl-text] coord item[13]: text=实测 % (实/预), bbox=[445, 173, 553, 188]
2026-08-10 06:18:06,061 INFO     29 [qwen-vl-text] coord item[14]: text=25/4/11, bbox=[419, 190, 480, 203]
2026-08-10 06:18:06,061 INFO     29 [qwen-vl-text] coord item[15]: text=14:56:4, bbox=[419, 205, 480, 218]
2026-08-10 06:18:06,061 INFO     29 [qwen-vl-text] coord item[16]: text=VT, bbox=[109, 236, 128, 249]
2026-08-10 06:18:06,061 INFO     29 [qwen-vl-text] coord item[17]: text=[L], bbox=[320, 236, 344, 250]
2026-08-10 06:18:06,061 INFO     29 [qwen-vl-text] coord item[18]: text=0.36, bbox=[373, 236, 409, 249]
2026-08-10 06:18:06,061 INFO     29 [qwen-vl-text] coord item[19]: text=0.41, bbox=[445, 236, 480, 249]
2026-08-10 06:18:06,061 INFO     29 [qwen-vl-text] coord item[20]: text=114.9, bbox=[510, 236, 553, 249]
2026-08-10 06:18:06,061 INFO     29 [qwen-vl-text] coord item[21]: text=BF, bbox=[109, 250, 128, 264]
2026-08-10 06:18:06,061 INFO     29 [qwen-vl-text] coord item[22]: text=[1/min], bbox=[285, 250, 344, 264]
2026-08-10 06:18:06,061 INFO     29 [qwen-vl-text] coord item[23]: text=20.00, bbox=[364, 250, 409, 264]
2026-08-10 06:18:06,061 INFO     29 [qwen-vl-text] coord item[24]: text=20.79, bbox=[436, 250, 480, 264]
2026-08-10 06:18:06,061 INFO     29 [qwen-vl-text] coord item[25]: text=104.0, bbox=[510, 250, 553, 264]
2026-08-10 06:18:06,061 INFO     29 [qwen-vl-text] coord item[26]: text=MV, bbox=[109, 265, 128, 279]
2026-08-10 06:18:06,061 INFO     29 [qwen-vl-text] coord item[27]: text=[L/min], bbox=[285, 265, 344, 279]
2026-08-10 06:18:06,062 INFO     29 [qwen-vl-text] coord item[28]: text=7.14, bbox=[373, 265, 409, 279]
2026-08-10 06:18:06,062 INFO     29 [qwen-vl-text] coord item[29]: text=8.54, bbox=[445, 265, 480, 279]
2026-08-10 06:18:06,062 INFO     29 [qwen-vl-text] coord item[30]: text=119.5, bbox=[510, 265, 553, 279]
2026-08-10 06:18:06,062 INFO     29 [qwen-vl-text] coord item[31]: text=ERV, bbox=[109, 280, 137, 293]
2026-08-10 06:18:06,062 INFO     29 [qwen-vl-text] coord item[32]: text=[L], bbox=[320, 280, 344, 294]
2026-08-10 06:18:06,062 INFO     29 [qwen-vl-text] coord item[33]: text=1.07, bbox=[373, 280, 409, 293]
2026-08-10 06:18:06,062 INFO     29 [qwen-vl-text] coord item[34]: text=1.07, bbox=[445, 280, 480, 293]
2026-08-10 06:18:06,062 INFO     29 [qwen-vl-text] coord item[35]: text=99.4, bbox=[517, 280, 553, 293]
2026-08-10 06:18:06,062 INFO     29 [qwen-vl-text] coord item[36]: text=VC MAX, bbox=[109, 295, 164, 309]
2026-08-10 06:18:06,062 INFO     29 [qwen-vl-text] coord item[37]: text=[L], bbox=[320, 295, 344, 309]
2026-08-10 06:18:06,062 INFO     29 [qwen-vl-text] coord item[38]: text=3.19, bbox=[373, 295, 409, 309]
2026-08-10 06:18:06,062 INFO     29 [qwen-vl-text] coord item[39]: text=2.84, bbox=[445, 295, 480, 309]
2026-08-10 06:18:06,062 INFO     29 [qwen-vl-text] coord item[40]: text=88.9, bbox=[517, 295, 553, 309]
2026-08-10 06:18:06,062 INFO     29 [qwen-vl-text] coord item[41]: text=FVC, bbox=[109, 326, 137, 339]
2026-08-10 06:18:06,062 INFO     29 [qwen-vl-text] coord item[42]: text=[L], bbox=[320, 326, 344, 340]
2026-08-10 06:18:06,062 INFO     29 [qwen-vl-text] coord item[43]: text=3.13, bbox=[373, 326, 409, 339]
2026-08-10 06:18:06,062 INFO     29 [qwen-vl-text] coord item[44]: text=2.84, bbox=[445, 326, 480, 339]
2026-08-10 06:18:06,062 INFO     29 [qwen-vl-text] coord item[45]: text=90.6, bbox=[517, 326, 553, 339]
2026-08-10 06:18:06,062 INFO     29 [qwen-vl-text] coord item[46]: text=FEV 1, bbox=[109, 341, 153, 355]
2026-08-10 06:18:06,062 INFO     29 [qwen-vl-text] coord item[47]: text=[L], bbox=[320, 341, 344, 355]
2026-08-10 06:18:06,062 INFO     29 [qwen-vl-text] coord item[48]: text=2.70, bbox=[373, 341, 409, 355]
2026-08-10 06:18:06,062 INFO     29 [qwen-vl-text] coord item[49]: text=1.53, bbox=[445, 341, 480, 355]
2026-08-10 06:18:06,062 INFO     29 [qwen-vl-text] coord item[50]: text=56.9, bbox=[517, 341, 553, 355]
2026-08-10 06:18:06,063 INFO     29 [qwen-vl-text] coord item[51]: text=FEV 1 % FVC, bbox=[109, 356, 210, 370]
2026-08-10 06:18:06,063 INFO     29 [qwen-vl-text] coord item[52]: text=[%], bbox=[320, 356, 344, 370]
2026-08-10 06:18:06,063 INFO     29 [qwen-vl-text] coord item[53]: text=83.98, bbox=[364, 356, 409, 370]
2026-08-10 06:18:06,063 INFO     29 [qwen-vl-text] coord item[54]: text=54.07, bbox=[436, 356, 480, 370]
2026-08-10 06:18:06,063 INFO     29 [qwen-vl-text] coord item[55]: text=64.4, bbox=[517, 356, 553, 370]
2026-08-10 06:18:06,063 INFO     29 [qwen-vl-text] coord item[56]: text=FEV 1 % VC MAX, bbox=[109, 371, 237, 385]
2026-08-10 06:18:06,063 INFO     29 [qwen-vl-text] coord item[57]: text=[%], bbox=[320, 371, 344, 385]
2026-08-10 06:18:06,063 INFO     29 [qwen-vl-text] coord item[58]: text=81.31, bbox=[364, 371, 409, 385]
2026-08-10 06:18:06,063 INFO     29 [qwen-vl-text] coord item[59]: text=54.07, bbox=[436, 371, 480, 385]
2026-08-10 06:18:06,063 INFO     29 [qwen-vl-text] coord item[60]: text=66.5, bbox=[517, 371, 553, 385]
2026-08-10 06:18:06,063 INFO     29 [qwen-vl-text] coord item[61]: text=PEF, bbox=[109, 386, 137, 400]
2026-08-10 06:18:06,063 INFO     29 [qwen-vl-text] coord item[62]: text=[L/s], bbox=[302, 386, 344, 400]
2026-08-10 06:18:06,063 INFO     29 [qwen-vl-text] coord item[63]: text=6.46, bbox=[373, 386, 409, 400]
2026-08-10 06:18:06,063 INFO     29 [qwen-vl-text] coord item[64]: text=4.56, bbox=[436, 386, 480, 400]
2026-08-10 06:18:06,063 INFO     29 [qwen-vl-text] coord item[65]: text=70.7, bbox=[517, 386, 553, 400]
2026-08-10 06:18:06,063 INFO     29 [qwen-vl-text] coord item[66]: text=MEF 75, bbox=[109, 401, 164, 415]
2026-08-10 06:18:06,063 INFO     29 [qwen-vl-text] coord item[67]: text=[L/s], bbox=[302, 401, 344, 415]
2026-08-10 06:18:06,063 INFO     29 [qwen-vl-text] coord item[68]: text=5.73, bbox=[373, 401, 409, 415]
2026-08-10 06:18:06,063 INFO     29 [qwen-vl-text] coord item[69]: text=1.84, bbox=[445, 401, 480, 415]
2026-08-10 06:18:06,063 INFO     29 [qwen-vl-text] coord item[70]: text=32.1, bbox=[517, 401, 553, 415]
2026-08-10 06:18:06,064 INFO     29 [qwen-vl-text] coord item[71]: text=MEF 50, bbox=[109, 416, 164, 430]
2026-08-10 06:18:06,064 INFO     29 [qwen-vl-text] coord item[72]: text=[L/s], bbox=[302, 416, 344, 430]
2026-08-10 06:18:06,064 INFO     29 [qwen-vl-text] coord item[73]: text=4.06, bbox=[373, 416, 409, 430]
2026-08-10 06:18:06,064 INFO     29 [qwen-vl-text] coord item[74]: text=0.84, bbox=[445, 416, 480, 430]
2026-08-10 06:18:06,064 INFO     29 [qwen-vl-text] coord item[75]: text=20.7, bbox=[517, 416, 553, 430]
2026-08-10 06:18:06,064 INFO     29 [qwen-vl-text] coord item[76]: text=MEF 25, bbox=[109, 431, 164, 445]
2026-08-10 06:18:06,064 INFO     29 [qwen-vl-text] coord item[77]: text=[L/s], bbox=[302, 431, 344, 445]
2026-08-10 06:18:06,064 INFO     29 [qwen-vl-text] coord item[78]: text=1.77, bbox=[373, 431, 409, 445]
2026-08-10 06:18:06,064 INFO     29 [qwen-vl-text] coord item[79]: text=0.28, bbox=[445, 431, 480, 445]
2026-08-10 06:18:06,064 INFO     29 [qwen-vl-text] coord item[80]: text=15.6, bbox=[517, 431, 553, 445]
2026-08-10 06:18:06,064 INFO     29 [qwen-vl-text] coord item[81]: text=MMEF 75/25, bbox=[109, 446, 200, 460]
2026-08-10 06:18:06,064 INFO     29 [qwen-vl-text] coord item[82]: text=[L/s], bbox=[302, 446, 344, 460]
2026-08-10 06:18:06,064 INFO     29 [qwen-vl-text] coord item[83]: text=3.53, bbox=[373, 446, 409, 460]
2026-08-10 06:18:06,064 INFO     29 [qwen-vl-text] coord item[84]: text=0.65, bbox=[445, 446, 480, 460]
2026-08-10 06:18:06,064 INFO     29 [qwen-vl-text] coord item[85]: text=18.3, bbox=[517, 446, 553, 460]
2026-08-10 06:18:06,064 INFO     29 [qwen-vl-text] coord item[86]: text=FET, bbox=[109, 461, 137, 475]
2026-08-10 06:18:06,064 INFO     29 [qwen-vl-text] coord item[87]: text=[s], bbox=[320, 461, 344, 475]
2026-08-10 06:18:06,064 INFO     29 [qwen-vl-text] coord item[88]: text=8.46, bbox=[445, 461, 480, 475]
2026-08-10 06:18:06,064 INFO     29 [qwen-vl-text] coord item[89]: text=V backextrapolation ex, bbox=[109, 476, 307, 490]
2026-08-10 06:18:06,064 INFO     29 [qwen-vl-text] coord item[90]: text=[L], bbox=[320, 476, 344, 490]
2026-08-10 06:18:06,064 INFO     29 [qwen-vl-text] coord item[91]: text=0.03, bbox=[445, 476, 480, 490]
2026-08-10 06:18:06,064 INFO     29 [qwen-vl-text] coord item[92]: text=V backextrapol. % FVC, bbox=[109, 491, 300, 505]
2026-08-10 06:18:06,064 INFO     29 [qwen-vl-text] coord item[93]: text=[%], bbox=[320, 491, 344, 505]
2026-08-10 06:18:06,064 INFO     29 [qwen-vl-text] coord item[94]: text=1.23, bbox=[445, 491, 480, 505]
2026-08-10 06:18:06,065 INFO     29 [qwen-vl-text] coord item[95]: text=MVV, bbox=[109, 523, 137, 537]
2026-08-10 06:18:06,065 INFO     29 [qwen-vl-text] coord item[96]: text=[L/min], bbox=[285, 523, 344, 537]
2026-08-10 06:18:06,065 INFO     29 [qwen-vl-text] coord item[97]: text=101.93, bbox=[356, 523, 409, 537]
2026-08-10 06:18:06,065 INFO     29 [qwen-vl-text] coord item[98]: text=75.75, bbox=[436, 523, 480, 537]
2026-08-10 06:18:06,065 INFO     29 [qwen-vl-text] coord item[99]: text=74.3, bbox=[517, 523, 553, 537]
2026-08-10 06:18:06,065 INFO     29 [qwen-vl-text] coord item[100]: text=FEV 1*30, bbox=[109, 538, 181, 552]
2026-08-10 06:18:06,065 INFO     29 [qwen-vl-text] coord item[101]: text=[L/min], bbox=[285, 538, 344, 552]
2026-08-10 06:18:06,065 INFO     29 [qwen-vl-text] coord item[102]: text=101.93, bbox=[356, 538, 409, 552]
2026-08-10 06:18:06,065 INFO     29 [qwen-vl-text] coord item[103]: text=46.03, bbox=[436, 538, 480, 552]
2026-08-10 06:18:06,065 INFO     29 [qwen-vl-text] coord item[104]: text=45.2, bbox=[517, 538, 553, 552]
2026-08-10 06:18:06,065 INFO     29 [qwen-vl-text] coord item[105]: text=RV-SB, bbox=[109, 569, 153, 583]
2026-08-10 06:18:06,065 INFO     29 [qwen-vl-text] coord item[106]: text=[L], bbox=[320, 569, 344, 583]
2026-08-10 06:18:06,065 INFO     29 [qwen-vl-text] coord item[107]: text=1.55, bbox=[373, 569, 409, 583]
2026-08-10 06:18:06,065 INFO     29 [qwen-vl-text] coord item[108]: text=2.56, bbox=[445, 569, 480, 583]
2026-08-10 06:18:06,065 INFO     29 [qwen-vl-text] coord item[109]: text=164.9, bbox=[508, 569, 553, 583]
2026-08-10 06:18:06,065 INFO     29 [qwen-vl-text] coord item[110]: text=RV%TLC-SB, bbox=[109, 584, 190, 598]
2026-08-10 06:18:06,065 INFO     29 [qwen-vl-text] coord item[111]: text=[%], bbox=[320, 584, 344, 598]
2026-08-10 06:18:06,065 INFO     29 [qwen-vl-text] coord item[112]: text=32.90, bbox=[364, 584, 409, 598]
2026-08-10 06:18:06,065 INFO     29 [qwen-vl-text] coord item[113]: text=47.52, bbox=[436, 584, 480, 598]
2026-08-10 06:18:06,065 INFO     29 [qwen-vl-text] coord item[114]: text=144.4, bbox=[508, 584, 553, 598]
2026-08-10 06:18:06,065 INFO     29 [qwen-vl-text] coord item[115]: text=TLC-SB, bbox=[109, 600, 162, 613]
2026-08-10 06:18:06,065 INFO     29 [qwen-vl-text] coord item[116]: text=[L], bbox=[320, 600, 344, 613]
2026-08-10 06:18:06,065 INFO     29 [qwen-vl-text] coord item[117]: text=4.77, bbox=[373, 600, 409, 613]
2026-08-10 06:18:06,066 INFO     29 [qwen-vl-text] coord item[118]: text=5.39, bbox=[445, 600, 480, 613]
2026-08-10 06:18:06,066 INFO     29 [qwen-vl-text] coord item[119]: text=112.9, bbox=[508, 600, 553, 613]
2026-08-10 06:18:06,066 INFO     29 [qwen-vl-text] coord item[120]: text=FRC-SB, bbox=[109, 614, 162, 628]
2026-08-10 06:18:06,066 INFO     29 [qwen-vl-text] coord item[121]: text=[L], bbox=[320, 614, 344, 628]
2026-08-10 06:18:06,066 INFO     29 [qwen-vl-text] coord item[122]: text=2.63, bbox=[373, 614, 409, 628]
2026-08-10 06:18:06,066 INFO     29 [qwen-vl-text] coord item[123]: text=3.31, bbox=[445, 614, 480, 628]
2026-08-10 06:18:06,066 INFO     29 [qwen-vl-text] coord item[124]: text=126.0, bbox=[508, 614, 553, 628]
2026-08-10 06:18:06,066 INFO     29 [qwen-vl-text] coord item[125]: text=FRC%TLC-SB, bbox=[109, 629, 198, 643]
2026-08-10 06:18:06,066 INFO     29 [qwen-vl-text] coord item[126]: text=[%], bbox=[320, 629, 344, 643]
2026-08-10 06:18:06,066 INFO     29 [qwen-vl-text] coord item[127]: text=51.66, bbox=[364, 629, 409, 643]
2026-08-10 06:18:06,066 INFO     29 [qwen-vl-text] coord item[128]: text=61.42, bbox=[436, 629, 480, 643]
2026-08-10 06:18:06,066 INFO     29 [qwen-vl-text] coord item[129]: text=118.9, bbox=[508, 629, 553, 643]
2026-08-10 06:18:06,066 INFO     29 [qwen-vl-text] coord item[130]: text=DLCOc SB, bbox=[109, 645, 180, 659]
2026-08-10 06:18:06,066 INFO     29 [qwen-vl-text] coord item[131]: text=[mmol/min/kPa], bbox=[218, 645, 344, 659]
2026-08-10 06:18:06,066 INFO     29 [qwen-vl-text] coord item[132]: text=8.34, bbox=[373, 645, 409, 659]
2026-08-10 06:18:06,066 INFO     29 [qwen-vl-text] coord item[133]: text=6.95, bbox=[445, 645, 480, 659]
2026-08-10 06:18:06,066 INFO     29 [qwen-vl-text] coord item[134]: text=83.4, bbox=[517, 645, 553, 659]
2026-08-10 06:18:06,066 INFO     29 [qwen-vl-text] coord item[135]: text=DLCO SB, bbox=[109, 660, 171, 674]
2026-08-10 06:18:06,066 INFO     29 [qwen-vl-text] coord item[136]: text=[mmol/min/kPa], bbox=[218, 660, 344, 674]
2026-08-10 06:18:06,066 INFO     29 [qwen-vl-text] coord item[137]: text=8.34, bbox=[373, 660, 409, 674]
2026-08-10 06:18:06,066 INFO     29 [qwen-vl-text] coord item[138]: text=6.95, bbox=[445, 660, 480, 674]
2026-08-10 06:18:06,066 INFO     29 [qwen-vl-text] coord item[139]: text=83.4, bbox=[517, 660, 553, 674]
2026-08-10 06:18:06,067 INFO     29 [qwen-vl-text] coord item[140]: text=医生意见：, bbox=[87, 705, 190, 722]
2026-08-10 06:18:06,067 INFO     29 [qwen-vl-text] coord item[141]: text=1.中重度阻塞性通气功能障碍。, bbox=[87, 727, 327, 740]
2026-08-10 06:18:06,067 INFO     29 [qwen-vl-text] coord item[142]: text=检查质量：FVC：A级 。 FEV1：A级 。, bbox=[87, 740, 400, 753]
2026-08-10 06:18:06,067 INFO     29 [qwen-vl-text] coord item[143]: text=备注：受检者检查配合佳。 结果仅供参考，请结合临床分析。, bbox=[87, 751, 594, 765]
2026-08-10 06:18:06,067 INFO     29 [qwen-vl-text] coord item[144]: text=2.最大自主分钟通气量（MVV）轻度下降。, bbox=[87, 764, 409, 777]
2026-08-10 06:18:06,067 INFO     29 [qwen-vl-text] coord item[145]: text=备注：患者MVV配合佳。结果仅供参考，请结合临床分析。, bbox=[87, 776, 532, 789]
2026-08-10 06:18:06,067 INFO     29 [qwen-vl-text] coord item[146]: text=3.弥散功能在正常范围。4.残总比中度增高。, bbox=[87, 788, 435, 801]
2026-08-10 06:18:06,067 INFO     29 [qwen-vl-text] coord item[147]: text=审核医生：孙帅森, bbox=[555, 841, 697, 857]
2026-08-10 06:18:06,067 INFO     29 [qwen-vl-text] coord item[148]: text=检测技师：张青苹, bbox=[552, 861, 703, 877]
2026-08-10 06:18:06,067 INFO     29 [qwen-vl-text] coord item[149]: text=通气弥散B, bbox=[72, 906, 123, 915]
2026-08-10 06:18:06,067 INFO     29 [qwen-vl-text] coord item[150]: text=2025/4/11 15:18, bbox=[451, 906, 529, 915]
2026-08-10 06:18:06,067 INFO     29 [qwen-vl-text] coord item[151]: text=1/1, bbox=[901, 907, 914, 915]
2026-08-10 06:18:06,067 INFO     29 [qwen-vl-text] page=3 — 151/151 coords, api_time=39.6s
2026-08-10 06:18:06,068 INFO     29 [qwen-vl-text] new_positions (151):
[[3, 242.165, 326.06, 49.678, 64.834], [3, 49.385, 80.325, 74.096, 86.726], [3, 49.385, 104.72, 86.726, 98.514], [3, 49.385, 142.79999999999998, 98.514, 110.30199999999999], [3, 49.385, 80.325, 110.30199999999999, 122.08999999999999], [3, 49.385, 104.72, 122.08999999999999, 133.878], [3, 283.21999999999997, 313.565, 74.096, 86.726], [3, 283.21999999999997, 313.565, 86.726, 98.514], [3, 283.21999999999997, 326.06, 98.514, 110.30199999999999], [3, 283.21999999999997, 313.565, 110.30199999999999, 122.08999999999999], [3, 64.855, 107.695, 159.138, 170.926], [3, 64.855, 107.695, 170.926, 183.55599999999998], [3, 221.935, 243.355, 145.666, 158.296], [3, 264.775, 329.03499999999997, 145.666, 158.296], [3, 249.30499999999998, 285.59999999999997, 159.98, 170.926], [3, 249.30499999999998, 285.59999999999997, 172.60999999999999, 183.55599999999998], [3, 64.855, 76.16, 198.712, 209.658], [3, 190.39999999999998, 204.67999999999998, 198.712, 210.5], [3, 221.935, 243.355, 198.712, 209.658], [3, 264.775, 285.59999999999997, 198.712, 209.658], [3, 303.45, 329.03499999999997, 198.712, 209.658], [3, 64.855, 76.16, 210.5, 222.28799999999998], [3, 169.575, 204.67999999999998, 210.5, 222.28799999999998], [3, 216.57999999999998, 243.355, 210.5, 222.28799999999998], [3, 259.42, 285.59999999999997, 210.5, 222.28799999999998], [3, 303.45, 329.03499999999997, 210.5, 222.28799999999998], [3, 64.855, 76.16, 223.13, 234.91799999999998], [3, 169.575, 204.67999999999998, 223.13, 234.91799999999998], [3, 221.935, 243.355, 223.13, 234.91799999999998], [3, 264.775, 285.59999999999997, 223.13, 234.91799999999998], [3, 303.45, 329.03499999999997, 223.13, 234.91799999999998], [3, 64.855, 81.515, 235.76, 246.706], [3, 190.39999999999998, 204.67999999999998, 235.76, 247.548], [3, 221.935, 243.355, 235.76, 246.706], [3, 264.775, 285.59999999999997, 235.76, 246.706], [3, 307.615, 329.03499999999997, 235.76, 246.706], [3, 64.855, 97.58, 248.39, 260.178], [3, 190.39999999999998, 204.67999999999998, 248.39, 260.178], [3, 221.935, 243.355, 248.39, 260.178], [3, 264.775, 285.59999999999997, 248.39, 260.178], [3, 307.615, 329.03499999999997, 248.39, 260.178], [3, 64.855, 81.515, 274.492, 285.438], [3, 190.39999999999998, 204.67999999999998, 274.492, 286.28], [3, 221.935, 243.355, 274.492, 285.438], [3, 264.775, 285.59999999999997, 274.492, 285.438], [3, 307.615, 329.03499999999997, 274.492, 285.438], [3, 64.855, 91.035, 287.122, 298.90999999999997], [3, 190.39999999999998, 204.67999999999998, 287.122, 298.90999999999997], [3, 221.935, 243.355, 287.122, 298.90999999999997], [3, 264.775, 285.59999999999997, 287.122, 298.90999999999997], [3, 307.615, 329.03499999999997, 287.122, 298.90999999999997], [3, 64.855, 124.94999999999999, 299.752, 311.53999999999996], [3, 190.39999999999998, 204.67999999999998, 299.752, 311.53999999999996], [3, 216.57999999999998, 243.355, 299.752, 311.53999999999996], [3, 259.42, 285.59999999999997, 299.752, 311.53999999999996], [3, 307.615, 329.03499999999997, 299.752, 311.53999999999996], [3, 64.855, 141.015, 312.382, 324.17], [3, 190.39999999999998, 204.67999999999998, 312.382, 324.17], [3, 216.57999999999998, 243.355, 312.382, 324.17], [3, 259.42, 285.59999999999997, 312.382, 324.17], [3, 307.615, 329.03499999999997, 312.382, 324.17], [3, 64.855, 81.515, 325.012, 336.8], [3, 179.69, 204.67999999999998, 325.012, 336.8], [3, 221.935, 243.355, 325.012, 336.8], [3, 259.42, 285.59999999999997, 325.012, 336.8], [3, 307.615, 329.03499999999997, 325.012, 336.8], [3, 64.855, 97.58, 337.642, 349.43], [3, 179.69, 204.67999999999998, 337.642, 349.43], [3, 221.935, 243.355, 337.642, 349.43], [3, 264.775, 285.59999999999997, 337.642, 349.43], [3, 307.615, 329.03499999999997, 337.642, 349.43], [3, 64.855, 97.58, 350.272, 362.06], [3, 179.69, 204.67999999999998, 350.272, 362.06], [3, 221.935, 243.355, 350.272, 362.06], [3, 264.775, 285.59999999999997, 350.272, 362.06], [3, 307.615, 329.03499999999997, 350.272, 362.06], [3, 64.855, 97.58, 362.902, 374.69], [3, 179.69, 204.67999999999998, 362.902, 374.69], [3, 221.935, 243.355, 362.902, 374.69], [3, 264.775, 285.59999999999997, 362.902, 374.69], [3, 307.615, 329.03499999999997, 362.902, 374.69], [3, 64.855, 119.0, 375.532, 387.32], [3, 179.69, 204.67999999999998, 375.532, 387.32], [3, 221.935, 243.355, 375.532, 387.32], [3, 264.775, 285.59999999999997, 375.532, 387.32], [3, 307.615, 329.03499999999997, 375.532, 387.32], [3, 64.855, 81.515, 388.162, 399.95], [3, 190.39999999999998, 204.67999999999998, 388.162, 399.95], [3, 264.775, 285.59999999999997, 388.162, 399.95], [3, 64.855, 182.665, 400.792, 412.58], [3, 190.39999999999998, 204.67999999999998, 400.792, 412.58], [3, 264.775, 285.59999999999997, 400.792, 412.58], [3, 64.855, 178.5, 413.42199999999997, 425.21], [3, 190.39999999999998, 204.67999999999998, 413.42199999999997, 425.21], [3, 264.775, 285.59999999999997, 413.42199999999997, 425.21], [3, 64.855, 81.515, 440.366, 452.154], [3, 169.575, 204.67999999999998, 440.366, 452.154], [3, 211.82, 243.355, 440.366, 452.154], [3, 259.42, 285.59999999999997, 440.366, 452.154], [3, 307.615, 329.03499999999997, 440.366, 452.154], [3, 64.855, 107.695, 452.996, 464.784], [3, 169.575, 204.67999999999998, 452.996, 464.784], [3, 211.82, 243.355, 452.996, 464.784], [3, 259.42, 285.59999999999997, 452.996, 464.784], [3, 307.615, 329.03499999999997, 452.996, 464.784], [3, 64.855, 91.035, 479.09799999999996, 490.88599999999997], [3, 190.39999999999998, 204.67999999999998, 479.09799999999996, 490.88599999999997], [3, 221.935, 243.355, 479.09799999999996, 490.88599999999997], [3, 264.775, 285.59999999999997, 479.09799999999996, 490.88599999999997], [3, 302.26, 329.03499999999997, 479.09799999999996, 490.88599999999997], [3, 64.855, 113.05, 491.728, 503.51599999999996], [3, 190.39999999999998, 204.67999999999998, 491.728, 503.51599999999996], [3, 216.57999999999998, 243.355, 491.728, 503.51599999999996], [3, 259.42, 285.59999999999997, 491.728, 503.51599999999996], [3, 302.26, 329.03499999999997, 491.728, 503.51599999999996], [3, 64.855, 96.39, 505.2, 516.146], [3, 190.39999999999998, 204.67999999999998, 505.2, 516.146], [3, 221.935, 243.355, 505.2, 516.146], [3, 264.775, 285.59999999999997, 505.2, 516.146], [3, 302.26, 329.03499999999997, 505.2, 516.146], [3, 64.855, 96.39, 516.9879999999999, 528.776], [3, 190.39999999999998, 204.67999999999998, 516.9879999999999, 528.776], [3, 221.935, 243.355, 516.9879999999999, 528.776], [3, 264.775, 285.59999999999997, 516.9879999999999, 528.776], [3, 302.26, 329.03499999999997, 516.9879999999999, 528.776], [3, 64.855, 117.80999999999999, 529.6179999999999, 541.406], [3, 190.39999999999998, 204.67999999999998, 529.6179999999999, 541.406], [3, 216.57999999999998, 243.355, 529.6179999999999, 541.406], [3, 259.42, 285.59999999999997, 529.6179999999999, 541.406], [3, 302.26, 329.03499999999997, 529.6179999999999, 541.406], [3, 64.855, 107.1, 543.09, 554.8779999999999], [3, 129.71, 204.67999999999998, 543.09, 554.8779999999999], [3, 221.935, 243.355, 543.09, 554.8779999999999], [3, 264.775, 285.59999999999997, 543.09, 554.8779999999999], [3, 307.615, 329.03499999999997, 543.09, 554.8779999999999], [3, 64.855, 101.74499999999999, 555.72, 567.5079999999999], [3, 129.71, 204.67999999999998, 555.72, 567.5079999999999], [3, 221.935, 243.355, 555.72, 567.5079999999999], [3, 264.775, 285.59999999999997, 555.72, 567.5079999999999], [3, 307.615, 329.03499999999997, 555.72, 567.5079999999999], [3, 51.765, 113.05, 593.61, 607.924], [3, 51.765, 194.565, 612.134, 623.0799999999999], [3, 51.765, 238.0, 623.0799999999999, 634.026], [3, 51.765, 353.43, 632.342, 644.13], [3, 51.765, 243.355, 643.288, 654.2339999999999], [3, 51.765, 316.53999999999996, 653.3919999999999, 664.338], [3, 51.765, 258.825, 663.496, 674.442], [3, 330.22499999999997, 414.715, 708.122, 721.5939999999999], [3, 328.44, 418.28499999999997, 724.962, 738.434], [3, 42.839999999999996, 73.185, 762.852, 770.43], [3, 268.34499999999997, 314.755, 762.852, 770.43]]
2026-08-10 06:18:06,068 INFO     29 [qwen-vl-text] ═══ DONE ═══ 151 positions, pages=1, time=58.2s
2026-08-10 06:18:06,069 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 06:18:06,076 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:18:06,076 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 06:18:06,076 INFO     29 [qwen-vl-text] positions(126): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 06:18:06,076 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [126]
2026-08-10 06:18:06,274 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 06:18:06,276 INFO     29 [qwen-vl-text] LLM extraction start, text_len=801
2026-08-10 06:18:06,276 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:18:06,276 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 588, \"bbox_end\": 713, \"encounter_dates\": [\"2025-04-11\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "肺功能报告单\n姓名：\n性别：女\n出生日期：1984/4/02\n年龄：41岁\n门诊/住院/体检：\n测试号：\n身高：160 cm\n体重：50 kg\n身份证号：\n预计\n实1 %(实1/预)\n实2 %(实2/预)\n变异率\n测试日期\n25/4/11\n25/4/11\n测试时间\n14:56:47下午\n15:14:32下午\nFVC\n[L]\n3.13\n2.84\n90.6\n3.05\n97.4\n7.5\nFEV 1\n[L]\n2.70\n1.53\n56.9\n1.91\n71.0\n24.7\nFEV 1 % FVC\n[%]\n83.98\n54.07\n64.4\n62.70\n74.7\n16.0\nFEV 1 % VC MAX\n[%]\n81.31\n54.07\n66.5\n62.70\n77.1\n16.0\nPEF\n[L/s]\n6.46\n4.56\n70.7\n5.64\n87.3\n23.6\nMEF 75\n[L/s]\n5.73\n1.84\n32.1\n2.65\n46.3\n44.3\nMEF 50\n[L/s]\n4.06\n0.84\n20.7\n1.23\n30.4\n47.0\nMEF 25\n[L/s]\n1.77\n0.28\n15.6\n0.44\n25.0\n60.2\nMMEF 75/25\n[L/s]\n3.53\n0.65\n18.3\n1.02\n29.1\n58.8\nFET\n[s]\n8.46\n6.41\n-24.2\nV backextrapolation ex [L]\n0.03\n0.06\n71.7\nV backextrapol. % FVC [%]\n1.23\n1.96\n59.6\nFlow [L/s]\nF/V ex\n10\n5\n0\n1\n2\n3\n4\n5\n6\n7\n10\n5\nF/V In\n医生意见：\n支气管舒张试验阳性。\n（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后。\nFEV1较基线增加大于12%，且绝对值增加大于200ml。）\n审核医生：孙帅森\n检测技师：张青苹",
    "role": "user"
  }
]
2026-08-10 06:18:06,277 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 06:18:06,277 INFO     29 [Trace] task=dbae825c | doc=LGWE-艾特美哮喘-洛阳三.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "163 items", "markdown": "", "text": "", "name": "LGWE-艾特美哮喘-洛阳三.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 06:18:06,277 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 06:18:06,287 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:18:06,288 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:18:06,289 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T06:18:06.289+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 2, "failed": 0, "current": {"801b5176947e11f182aec5d26bc6c4ae": {"id": "801b5176947e11f182aec5d26bc6c4ae", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786340646131, "task_type": "dataflow", "root_trace_id": "97b84aa3d1154f6db808c154432c5554", "root_traceparent": "00-97b84aa3d1154f6db808c154432c5554-dd9503e7c4e14a5d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "dbae825c948211f1bd9827cf206dfa2d": {"id": "dbae825c948211f1bd9827cf206dfa2d", "doc_id": "db492056948211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LGWE-\u827e\u7279\u7f8e\u54ee\u5598-\u6d1b\u9633\u4e09.pdf", "type": "pdf", "location": "LGWE-\u827e\u7279\u7f8e\u54ee\u5598-\u6d1b\u9633\u4e09.pdf", "size": 1648931, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786342517754, "task_type": "dataflow", "root_trace_id": "aaa86c5dcc2c462f88c0ac982e1d484f", "root_traceparent": "00-aaa86c5dcc2c462f88c0ac982e1d484f-c2d6050d16147908-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 06:18:07,653 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:18:07,665 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 06:18:07,665 INFO     29 [Trace] task=dbae825c | doc=LGWE-艾特美哮喘-洛阳三.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "163 items", "markdown": "", "text": "", "name": "LGWE-艾特美哮喘-洛阳三.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 06:18:07,665 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 06:18:07,672 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:18:07,673 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:18:08,353 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:18:08,360 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 06:18:08,360 INFO     29 [Trace] task=dbae825c | doc=LGWE-艾特美哮喘-洛阳三.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "163 items", "markdown": "", "text": "", "name": "LGWE-艾特美哮喘-洛阳三.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 06:18:08,360 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 06:18:08,369 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 06:18:08,370 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:18:08,370 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 06:18:08,370 INFO     29 [qwen-vl-text] positions(71): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 06:18:08,370 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [71]
2026-08-10 06:18:08,506 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 06:18:08,506 INFO     29 [qwen-vl-text] LLM extraction start, text_len=702
2026-08-10 06:18:08,506 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:18:08,507 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 22, \"bbox_end\": 92, \"encounter_dates\": [\"2025-05-25\"], \"department\": \"呼吸内科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "郑州市第一人民医院\n肺功能检查报告\n舒张试验\n姓名：\n性别：男\n年龄：61岁\n身高：174 cm\n体重：85 kg\n科别：呼吸内科\n住院号：\n测试号：2025052513\n吸烟史：\n联系电话：\n测试日期 25-5-25\n测试时间 11:46:55\n预计值\n前次\n前/预\n后次\n后/预\n改善率\n25-5-25\n25-5-25\n11:46:55\n11:57:14\nFVC [L] 4.10 2.84 69.4 3.49 85.2 22.91\nFEV 1 [L] 3.22 2.51 78.0 3.06 95.0 21.81\nFEV 1 % FVC [%] 83.40 88.46 106.1 87.66 105.1 -0.90\nPEF [L/s] 8.21 6.40 77.9 6.63 80.8 3.68\nMEF 75 [L/s] 7.26 6.18 85.1 6.13 84.4 -0.76\nMEF 50 [L/s] 4.35 3.04 69.9 4.48 102.9 47.19\nMEF 25 [L/s] 1.62 1.18 72.8 1.25 77.6 6.56\nMMEF 75/25 [L/s] 3.45 2.26 65.4 3.32 96.0 46.80\nFlow [L/s]\nF/V ex\n10\n5\n0\n1\n2\n3\n4\n5\nF/V In\n6\nVol [L]\n5\nVol%Vmax\n100\nV Cmax\n80\n3\n60\n2\n40\n20\n1\n0\n0\nTime [s]\n0.0\n0.5\n1.0\n1.5\n2.0\n2.5\n3.0\n测试结果：\n支气管舒张试验阳性。\n(请结合临床全面诊断)\n医生签字：毛锦涛",
    "role": "user"
  }
]
2026-08-10 06:18:14,106 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:18:14,106 INFO     29 [qwen-vl-text] LLM output (len=937):
{
  "exam_date": "2025-05-25",
  "report_date": "2025-05-25",
  "exam_name": "肺功能检查报告 舒张试验",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "男",
  "department": "呼吸内科",
  "bed_number": null,
  "findings": "预计值\n前次\n前/预\n后次\n后/预\n改善率\n25-5-25\n25-5-25\n11:46:55\n11:57:14\nFVC [L] 4.10 2.84 69.4 3.49 85.2 22.91\nFEV 1 [L] 3.22 2.51 78.0 3.06 95.0 21.81\nFEV 1 % FVC [%] 83.40 88.46 106.1 87.66 105.1 -0.90\nPEF [L/s] 8.21 6.40 77.9 6.63 80.8 3.68\nMEF 75 [L/s] 7.26 6.18 85.1 6.13 84.4 -0.76\nMEF 50 [L/s] 4.35 3.04 69.9 4.48 102.9 47.19\nMEF 25 [L/s] 1.62 1.18 72.8 1.25 77.6 6.56\nMMEF 75/25 [L/s] 3.45 2.26 65.4 3.32 96.0 46.80\nFlow [L/s]\nF/V ex\n10\n5\n0\n1\n2\n3\n4\n5\nF/V In\n6\nVol [L]\n5\nVol%Vmax\n100\nV Cmax\n80\n3\n60\n2\n40\n20\n1\n0\n0\nTime [s]\n0.0\n0.5\n1.0\n1.5\n2.0\n2.5\n3.0",
  "conclusion": "测试结果：\n支气管舒张试验阳性。\n(请结合临床全面诊断)",
  "physician": "毛锦涛",
  "reviewer": null
}
2026-08-10 06:18:14,108 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=650512, prompt_len=1528
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共71行）
["郑州市第一人民医院", "肺功能检查报告", "舒张试验", "姓名：", "性别：男", "年龄：61岁", "身高：174 cm", "体重：85 kg", "科别：呼吸内科", "住院号：", "测试号：2025052513", "吸烟史：", "联系电话：", "测试日期 25-5-25", "测试时间 11:46:55", "预计值", "前次", "前/预", "后次", "后/预", "改善率", "25-5-25", "25-5-25", "11:46:55", "11:57:14", "FVC [L] 4.10 2.84 69.4 3.49 85.2 22.91", "FEV 1 [L] 3.22 2.51 78.0 3.06 95.0 21.81", "FEV 1 % FVC [%] 83.40 88.46 106.1 87.66 105.1 -0.90", "PEF [L/s] 8.21 6.40 77.9 6.63 80.8 3.68", "MEF 75 [L/s] 7.26 6.18 85.1 6.13 84.4 -0.76", "MEF 50 [L/s] 4.35 3.04 69.9 4.48 102.9 47.19", "MEF 25 [L/s] 1.62 1.18 72.8 1.25 77.6 6.56", "MMEF 75/25 [L/s] 3.45 2.26 65.4 3.32 96.0 46.80", "Flow [L/s]", "F/V ex", "10", "5", "0", "1", "2", "3", "4", "5", "F/V In", "6", "Vol [L]", "5", "Vol%Vmax", "100", "V Cmax", "80", "3", "60", "2", "40", "20", "1", "0", "0", "Time [s]", "0.0", "0.5", "1.0", "1.5", "2.0", "2.5", "3.0", "测试结果：", "支气管舒张试验阳性。", "(请结合临床全面诊断)", "医生签字：毛锦涛"]

## 定位规则
1. 对于列表中的每行文本，找到它在图片中**精确出现**的位置
2. bbox必须是该行文字的**最小紧密包围框**，紧贴文字边缘，不要包含额外的空白区域
3. 坐标归一化到0-1000，格式[x1,y1,x2,y2]
4. 如果某行文本在图片中未找到，跳过不输出
5. text字段必须与给定的文本完全一致

## 包围框精度要求
- x1必须紧贴该行第一个字符的左边缘
- x2必须紧贴该行最后一个字符的右边缘
- y1必须紧贴该行文字的顶部
- y2必须紧贴该行文字的底部
- 禁止将多行文字合并到同一个bbox中

## 严格JSON格式要求
直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。
正确示例：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230]},
  {"text": "年龄：68岁", "bbox": [100, 250, 270, 280]}
]
错误示例（禁止额外字段）：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230], "label": "个人信息"}
]
请直接输出纯JSON数组，不要用markdown代码块包裹。
2026-08-10 06:18:34,521 INFO     29 [qwen-vl-text] coord API raw response (len=3809):
[
	{"text": "郑州市第一人民医院", "bbox": [382, 50, 634, 78]},
	{"text": "肺功能检查报告", "bbox": [410, 82, 603, 106]},
	{"text": "舒张试验", "bbox": [447, 114, 556, 138]},
	{"text": "姓名：", "bbox": [171, 165, 213, 177]},
	{"text": "性别：男", "bbox": [171, 176, 352, 188]},
	{"text": "年龄：61岁", "bbox": [171, 187, 380, 199]},
	{"text": "身高：174 cm", "bbox": [171, 198, 390, 210]},
	{"text": "体重：85 kg", "bbox": [171, 210, 380, 222]},
	{"text": "科别：呼吸内科", "bbox": [511, 157, 752, 171]},
	{"text": "住院号：", "bbox": [511, 170, 715, 183]},
	{"text": "测试号：2025052513", "bbox": [511, 182, 771, 195]},
	{"text": "吸烟史：", "bbox": [511, 195, 575, 207]},
	{"text": "联系电话：", "bbox": [511, 207, 593, 220]},
	{"text": "测试日期", "bbox": [108, 274, 183, 288]},
	{"text": "测试时间", "bbox": [108, 289, 183, 303]},
	{"text": "预计值", "bbox": [393, 253, 457, 268]},
	{"text": "前次", "bbox": [507, 253, 546, 268]},
	{"text": "前/预", "bbox": [587, 253, 638, 268]},
	{"text": "后次", "bbox": [690, 253, 730, 268]},
	{"text": "后/预", "bbox": [772, 253, 821, 268]},
	{"text": "改善率", "bbox": [851, 253, 910, 268]},
	{"text": "25-5-25", "bbox": [476, 268, 546, 281]},
	{"text": "25-5-25", "bbox": [659, 268, 730, 281]},
	{"text": "11:46:55", "bbox": [467, 283, 546, 296]},
	{"text": "11:57:14", "bbox": [650, 283, 730, 296]},
	{"text": "FVC [L] 4.10 2.84 69.4 3.49 85.2 22.91", "bbox": [108, 317, 910, 331]},
	{"text": "FEV 1 [L] 3.22 2.51 78.0 3.06 95.0 21.81", "bbox": [108, 333, 910, 347]},
	{"text": "FEV 1 % FVC [%] 83.40 88.46 106.1 87.66 105.1 -0.90", "bbox": [108, 348, 910, 362]},
	{"text": "PEF [L/s] 8.21 6.40 77.9 6.63 80.8 3.68", "bbox": [108, 363, 910, 377]},
	{"text": "MEF 75 [L/s] 7.26 6.18 85.1 6.13 84.4 -0.76", "bbox": [108, 378, 910, 392]},
	{"text": "MEF 50 [L/s] 4.35 3.04 69.9 4.48 102.9 47.19", "bbox": [108, 393, 910, 407]},
	{"text": "MEF 25 [L/s] 1.62 1.18 72.8 1.25 77.6 6.56", "bbox": [108, 408, 910, 422]},
	{"text": "MMEF 75/25 [L/s] 3.45 2.26 65.4 3.32 96.0 46.80", "bbox": [108, 423, 910, 437]},
	{"text": "Flow [L/s]", "bbox": [181, 489, 230, 500]},
	{"text": "F/V ex", "bbox": [377, 488, 412, 497]},
	{"text": "10", "bbox": [163, 508, 176, 517]},
	{"text": "5", "bbox": [167, 537, 176, 546]},
	{"text": "0", "bbox": [165, 565, 174, 574]},
	{"text": "1", "bbox": [224, 575, 233, 584]},
	{"text": "2", "bbox": [279, 575, 288, 584]},
	{"text": "3", "bbox": [334, 575, 343, 584]},
	{"text": "4", "bbox": [389, 575, 398, 584]},
	{"text": "5", "bbox": [445, 575, 454, 584]},
	{"text": "F/V In", "bbox": [380, 640, 410, 650]},
	{"text": "6", "bbox": [570, 488, 579, 497]},
	{"text": "Vol [L]", "bbox": [585, 490, 619, 501]},
	{"text": "5", "bbox": [570, 512, 579, 521]},
	{"text": "Vol%Vmax", "bbox": [537, 531, 600, 541]},
	{"text": "100", "bbox": [540, 542, 560, 551]},
	{"text": "V Cmax", "bbox": [598, 547, 635, 556]},
	{"text": "80", "bbox": [547, 561, 559, 570]},
	{"text": "3", "bbox": [570, 561, 577, 570]},
	{"text": "60", "bbox": [547, 580, 559, 589]},
	{"text": "2", "bbox": [570, 580, 577, 589]},
	{"text": "40", "bbox": [547, 597, 559, 606]},
	{"text": "20", "bbox": [547, 615, 559, 624]},
	{"text": "1", "bbox": [570, 611, 577, 620]},
	{"text": "0", "bbox": [552, 633, 560, 642]},
	{"text": "0", "bbox": [568, 633, 577, 642]},
	{"text": "Time [s]", "bbox": [713, 624, 754, 634]},
	{"text": "0.0", "bbox": [573, 644, 592, 653]},
	{"text": "0.5", "bbox": [624, 644, 643, 653]},
	{"text": "1.0", "bbox": [677, 644, 694, 653]},
	{"text": "1.5", "bbox": [725, 644, 742, 653]},
	{"text": "2.0", "bbox": [774, 644, 791, 653]},
	{"text": "2.5", "bbox": [821, 644, 838, 653]},
	{"text": "3.0", "bbox": [868, 644, 885, 653]},
	{"text": "测试结果：", "bbox": [105, 667, 197, 684]},
	{"text": "支气管舒张试验阳性。", "bbox": [128, 702, 300, 714]},
	{"text": "(请结合临床全面诊断)", "bbox": [132, 827, 345, 845]},
	{"text": "医生签字：毛锦涛", "bbox": [556, 827, 868, 869]}
]
2026-08-10 06:18:34,522 INFO     29 [qwen-vl-text] coord API: raw_items=71, valid_items=71, elapsed=20.4s
2026-08-10 06:18:34,522 INFO     29 [qwen-vl-text] coord item[0]: text=郑州市第一人民医院, bbox=[382, 50, 634, 78]
2026-08-10 06:18:34,522 INFO     29 [qwen-vl-text] coord item[1]: text=肺功能检查报告, bbox=[410, 82, 603, 106]
2026-08-10 06:18:34,522 INFO     29 [qwen-vl-text] coord item[2]: text=舒张试验, bbox=[447, 114, 556, 138]
2026-08-10 06:18:34,522 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[171, 165, 213, 177]
2026-08-10 06:18:34,522 INFO     29 [qwen-vl-text] coord item[4]: text=性别：男, bbox=[171, 176, 352, 188]
2026-08-10 06:18:34,522 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：61岁, bbox=[171, 187, 380, 199]
2026-08-10 06:18:34,522 INFO     29 [qwen-vl-text] coord item[6]: text=身高：174 cm, bbox=[171, 198, 390, 210]
2026-08-10 06:18:34,522 INFO     29 [qwen-vl-text] coord item[7]: text=体重：85 kg, bbox=[171, 210, 380, 222]
2026-08-10 06:18:34,522 INFO     29 [qwen-vl-text] coord item[8]: text=科别：呼吸内科, bbox=[511, 157, 752, 171]
2026-08-10 06:18:34,522 INFO     29 [qwen-vl-text] coord item[9]: text=住院号：, bbox=[511, 170, 715, 183]
2026-08-10 06:18:34,522 INFO     29 [qwen-vl-text] coord item[10]: text=测试号：2025052513, bbox=[511, 182, 771, 195]
2026-08-10 06:18:34,522 INFO     29 [qwen-vl-text] coord item[11]: text=吸烟史：, bbox=[511, 195, 575, 207]
2026-08-10 06:18:34,523 INFO     29 [qwen-vl-text] coord item[12]: text=联系电话：, bbox=[511, 207, 593, 220]
2026-08-10 06:18:34,523 INFO     29 [qwen-vl-text] coord item[13]: text=测试日期, bbox=[108, 274, 183, 288]
2026-08-10 06:18:34,523 INFO     29 [qwen-vl-text] coord item[14]: text=测试时间, bbox=[108, 289, 183, 303]
2026-08-10 06:18:34,523 INFO     29 [qwen-vl-text] coord item[15]: text=预计值, bbox=[393, 253, 457, 268]
2026-08-10 06:18:34,523 INFO     29 [qwen-vl-text] coord item[16]: text=前次, bbox=[507, 253, 546, 268]
2026-08-10 06:18:34,523 INFO     29 [qwen-vl-text] coord item[17]: text=前/预, bbox=[587, 253, 638, 268]
2026-08-10 06:18:34,523 INFO     29 [qwen-vl-text] coord item[18]: text=后次, bbox=[690, 253, 730, 268]
2026-08-10 06:18:34,523 INFO     29 [qwen-vl-text] coord item[19]: text=后/预, bbox=[772, 253, 821, 268]
2026-08-10 06:18:34,523 INFO     29 [qwen-vl-text] coord item[20]: text=改善率, bbox=[851, 253, 910, 268]
2026-08-10 06:18:34,523 INFO     29 [qwen-vl-text] coord item[21]: text=25-5-25, bbox=[476, 268, 546, 281]
2026-08-10 06:18:34,523 INFO     29 [qwen-vl-text] coord item[22]: text=25-5-25, bbox=[659, 268, 730, 281]
2026-08-10 06:18:34,523 INFO     29 [qwen-vl-text] coord item[23]: text=11:46:55, bbox=[467, 283, 546, 296]
2026-08-10 06:18:34,523 INFO     29 [qwen-vl-text] coord item[24]: text=11:57:14, bbox=[650, 283, 730, 296]
2026-08-10 06:18:34,523 INFO     29 [qwen-vl-text] coord item[25]: text=FVC [L] 4.10 2.84 69.4 3.49 85.2 22.91, bbox=[108, 317, 910, 331]
2026-08-10 06:18:34,523 INFO     29 [qwen-vl-text] coord item[26]: text=FEV 1 [L] 3.22 2.51 78.0 3.06 95.0 21.81, bbox=[108, 333, 910, 347]
2026-08-10 06:18:34,523 INFO     29 [qwen-vl-text] coord item[27]: text=FEV 1 % FVC [%] 83.40 88.46 106.1 87.66 105.1 -0.90, bbox=[108, 348, 910, 362]
2026-08-10 06:18:34,524 INFO     29 [qwen-vl-text] coord item[28]: text=PEF [L/s] 8.21 6.40 77.9 6.63 80.8 3.68, bbox=[108, 363, 910, 377]
2026-08-10 06:18:34,524 INFO     29 [qwen-vl-text] coord item[29]: text=MEF 75 [L/s] 7.26 6.18 85.1 6.13 84.4 -0.76, bbox=[108, 378, 910, 392]
2026-08-10 06:18:34,524 INFO     29 [qwen-vl-text] coord item[30]: text=MEF 50 [L/s] 4.35 3.04 69.9 4.48 102.9 47.19, bbox=[108, 393, 910, 407]
2026-08-10 06:18:34,524 INFO     29 [qwen-vl-text] coord item[31]: text=MEF 25 [L/s] 1.62 1.18 72.8 1.25 77.6 6.56, bbox=[108, 408, 910, 422]
2026-08-10 06:18:34,524 INFO     29 [qwen-vl-text] coord item[32]: text=MMEF 75/25 [L/s] 3.45 2.26 65.4 3.32 96.0 46.80, bbox=[108, 423, 910, 437]
2026-08-10 06:18:34,524 INFO     29 [qwen-vl-text] coord item[33]: text=Flow [L/s], bbox=[181, 489, 230, 500]
2026-08-10 06:18:34,524 INFO     29 [qwen-vl-text] coord item[34]: text=F/V ex, bbox=[377, 488, 412, 497]
2026-08-10 06:18:34,524 INFO     29 [qwen-vl-text] coord item[35]: text=10, bbox=[163, 508, 176, 517]
2026-08-10 06:18:34,524 INFO     29 [qwen-vl-text] coord item[36]: text=5, bbox=[167, 537, 176, 546]
2026-08-10 06:18:34,524 INFO     29 [qwen-vl-text] coord item[37]: text=0, bbox=[165, 565, 174, 574]
2026-08-10 06:18:34,524 INFO     29 [qwen-vl-text] coord item[38]: text=1, bbox=[224, 575, 233, 584]
2026-08-10 06:18:34,524 INFO     29 [qwen-vl-text] coord item[39]: text=2, bbox=[279, 575, 288, 584]
2026-08-10 06:18:34,524 INFO     29 [qwen-vl-text] coord item[40]: text=3, bbox=[334, 575, 343, 584]
2026-08-10 06:18:34,524 INFO     29 [qwen-vl-text] coord item[41]: text=4, bbox=[389, 575, 398, 584]
2026-08-10 06:18:34,524 INFO     29 [qwen-vl-text] coord item[42]: text=5, bbox=[445, 575, 454, 584]
2026-08-10 06:18:34,524 INFO     29 [qwen-vl-text] coord item[43]: text=F/V In, bbox=[380, 640, 410, 650]
2026-08-10 06:18:34,524 INFO     29 [qwen-vl-text] coord item[44]: text=6, bbox=[570, 488, 579, 497]
2026-08-10 06:18:34,525 INFO     29 [qwen-vl-text] coord item[45]: text=Vol [L], bbox=[585, 490, 619, 501]
2026-08-10 06:18:34,525 INFO     29 [qwen-vl-text] coord item[46]: text=5, bbox=[570, 512, 579, 521]
2026-08-10 06:18:34,525 INFO     29 [qwen-vl-text] coord item[47]: text=Vol%Vmax, bbox=[537, 531, 600, 541]
2026-08-10 06:18:34,525 INFO     29 [qwen-vl-text] coord item[48]: text=100, bbox=[540, 542, 560, 551]
2026-08-10 06:18:34,525 INFO     29 [qwen-vl-text] coord item[49]: text=V Cmax, bbox=[598, 547, 635, 556]
2026-08-10 06:18:34,525 INFO     29 [qwen-vl-text] coord item[50]: text=80, bbox=[547, 561, 559, 570]
2026-08-10 06:18:34,525 INFO     29 [qwen-vl-text] coord item[51]: text=3, bbox=[570, 561, 577, 570]
2026-08-10 06:18:34,525 INFO     29 [qwen-vl-text] coord item[52]: text=60, bbox=[547, 580, 559, 589]
2026-08-10 06:18:34,525 INFO     29 [qwen-vl-text] coord item[53]: text=2, bbox=[570, 580, 577, 589]
2026-08-10 06:18:34,525 INFO     29 [qwen-vl-text] coord item[54]: text=40, bbox=[547, 597, 559, 606]
2026-08-10 06:18:34,525 INFO     29 [qwen-vl-text] coord item[55]: text=20, bbox=[547, 615, 559, 624]
2026-08-10 06:18:34,525 INFO     29 [qwen-vl-text] coord item[56]: text=1, bbox=[570, 611, 577, 620]
2026-08-10 06:18:34,525 INFO     29 [qwen-vl-text] coord item[57]: text=0, bbox=[552, 633, 560, 642]
2026-08-10 06:18:34,525 INFO     29 [qwen-vl-text] coord item[58]: text=0, bbox=[568, 633, 577, 642]
2026-08-10 06:18:34,525 INFO     29 [qwen-vl-text] coord item[59]: text=Time [s], bbox=[713, 624, 754, 634]
2026-08-10 06:18:34,525 INFO     29 [qwen-vl-text] coord item[60]: text=0.0, bbox=[573, 644, 592, 653]
2026-08-10 06:18:34,525 INFO     29 [qwen-vl-text] coord item[61]: text=0.5, bbox=[624, 644, 643, 653]
2026-08-10 06:18:34,525 INFO     29 [qwen-vl-text] coord item[62]: text=1.0, bbox=[677, 644, 694, 653]
2026-08-10 06:18:34,525 INFO     29 [qwen-vl-text] coord item[63]: text=1.5, bbox=[725, 644, 742, 653]
2026-08-10 06:18:34,525 INFO     29 [qwen-vl-text] coord item[64]: text=2.0, bbox=[774, 644, 791, 653]
2026-08-10 06:18:34,525 INFO     29 [qwen-vl-text] coord item[65]: text=2.5, bbox=[821, 644, 838, 653]
2026-08-10 06:18:34,526 INFO     29 [qwen-vl-text] coord item[66]: text=3.0, bbox=[868, 644, 885, 653]
2026-08-10 06:18:34,526 INFO     29 [qwen-vl-text] coord item[67]: text=测试结果：, bbox=[105, 667, 197, 684]
2026-08-10 06:18:34,526 INFO     29 [qwen-vl-text] coord item[68]: text=支气管舒张试验阳性。, bbox=[128, 702, 300, 714]
2026-08-10 06:18:34,526 INFO     29 [qwen-vl-text] coord item[69]: text=(请结合临床全面诊断), bbox=[132, 827, 345, 845]
2026-08-10 06:18:34,526 INFO     29 [qwen-vl-text] coord item[70]: text=医生签字：毛锦涛, bbox=[556, 827, 868, 869]
2026-08-10 06:18:34,526 INFO     29 [qwen-vl-text] page=1 — 71/71 coords, api_time=20.4s
2026-08-10 06:18:34,526 INFO     29 [qwen-vl-text] new_positions (71):
[[1, 227.29, 377.22999999999996, 42.1, 65.676], [1, 243.95, 358.78499999999997, 69.044, 89.252], [1, 265.965, 330.82, 95.988, 116.196], [1, 101.74499999999999, 126.735, 138.93, 149.034], [1, 101.74499999999999, 209.44, 148.192, 158.296], [1, 101.74499999999999, 226.1, 157.454, 167.558], [1, 101.74499999999999, 232.04999999999998, 166.716, 176.82], [1, 101.74499999999999, 226.1, 176.82, 186.924], [1, 304.04499999999996, 447.44, 132.194, 143.982], [1, 304.04499999999996, 425.42499999999995, 143.14, 154.08599999999998], [1, 304.04499999999996, 458.745, 153.244, 164.19], [1, 304.04499999999996, 342.125, 164.19, 174.29399999999998], [1, 304.04499999999996, 352.835, 174.29399999999998, 185.23999999999998], [1, 64.25999999999999, 108.88499999999999, 230.708, 242.49599999999998], [1, 64.25999999999999, 108.88499999999999, 243.338, 255.126], [1, 233.83499999999998, 271.91499999999996, 213.02599999999998, 225.656], [1, 301.66499999999996, 324.87, 213.02599999999998, 225.656], [1, 349.265, 379.60999999999996, 213.02599999999998, 225.656], [1, 410.54999999999995, 434.34999999999997, 213.02599999999998, 225.656], [1, 459.34, 488.495, 213.02599999999998, 225.656], [1, 506.34499999999997, 541.4499999999999, 213.02599999999998, 225.656], [1, 283.21999999999997, 324.87, 225.656, 236.602], [1, 392.10499999999996, 434.34999999999997, 225.656, 236.602], [1, 277.865, 324.87, 238.286, 249.232], [1, 386.75, 434.34999999999997, 238.286, 249.232], [1, 64.25999999999999, 541.4499999999999, 266.914, 278.702], [1, 64.25999999999999, 541.4499999999999, 280.38599999999997, 292.174], [1, 64.25999999999999, 541.4499999999999, 293.01599999999996, 304.804], [1, 64.25999999999999, 541.4499999999999, 305.646, 317.43399999999997], [1, 64.25999999999999, 541.4499999999999, 318.276, 330.06399999999996], [1, 64.25999999999999, 541.4499999999999, 330.906, 342.69399999999996], [1, 64.25999999999999, 541.4499999999999, 343.536, 355.324], [1, 64.25999999999999, 541.4499999999999, 356.166, 367.954], [1, 107.695, 136.85, 411.738, 421.0], [1, 224.315, 245.14, 410.89599999999996, 418.474], [1, 96.985, 104.72, 427.736, 435.31399999999996], [1, 99.365, 104.72, 452.154, 459.73199999999997], [1, 98.175, 103.53, 475.72999999999996, 483.308], [1, 133.28, 138.635, 484.15, 491.728], [1, 166.005, 171.35999999999999, 484.15, 491.728], [1, 198.73, 204.08499999999998, 484.15, 491.728], [1, 231.45499999999998, 236.81, 484.15, 491.728], [1, 264.775, 270.13, 484.15, 491.728], [1, 226.1, 243.95, 538.88, 547.3], [1, 339.15, 344.505, 410.89599999999996, 418.474], [1, 348.075, 368.305, 412.58, 421.842], [1, 339.15, 344.505, 431.104, 438.68199999999996], [1, 319.515, 357.0, 447.102, 455.522], [1, 321.3, 333.2, 456.364, 463.942], [1, 355.81, 377.825, 460.574, 468.152], [1, 325.465, 332.60499999999996, 472.36199999999997, 479.94], [1, 339.15, 343.315, 472.36199999999997, 479.94], [1, 325.465, 332.60499999999996, 488.35999999999996, 495.938], [1, 339.15, 343.315, 488.35999999999996, 495.938], [1, 325.465, 332.60499999999996, 502.674, 510.252], [1, 325.465, 332.60499999999996, 517.8299999999999, 525.408], [1, 339.15, 343.315, 514.462, 522.04], [1, 328.44, 333.2, 532.986, 540.564], [1, 337.96, 343.315, 532.986, 540.564], [1, 424.23499999999996, 448.63, 525.408, 533.828], [1, 340.935, 352.24, 542.2479999999999, 549.826], [1, 371.28, 382.585, 542.2479999999999, 549.826], [1, 402.815, 412.93, 542.2479999999999, 549.826], [1, 431.375, 441.48999999999995, 542.2479999999999, 549.826], [1, 460.53, 470.645, 542.2479999999999, 549.826], [1, 488.495, 498.60999999999996, 542.2479999999999, 549.826], [1, 516.4599999999999, 526.5749999999999, 542.2479999999999, 549.826], [1, 62.474999999999994, 117.21499999999999, 561.614, 575.928], [1, 76.16, 178.5, 591.084, 601.188], [1, 78.53999999999999, 205.27499999999998, 696.334, 711.49], [1, 330.82, 516.4599999999999, 696.334, 731.698]]
2026-08-10 06:18:34,526 INFO     29 [qwen-vl-text] ═══ DONE ═══ 71 positions, pages=1, time=26.2s
2026-08-10 06:18:34,526 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 06:18:34,527 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:18:34,528 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 06:18:34,528 INFO     29 [qwen-vl-text] positions(66): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 06:18:34,528 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [66]
2026-08-10 06:18:34,757 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 06:18:34,757 INFO     29 [qwen-vl-text] LLM extraction start, text_len=873
2026-08-10 06:18:34,757 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:18:34,758 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 95, \"bbox_end\": 160, \"encounter_dates\": [\"2025-05-25\"], \"department\": \"呼吸内科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "郑州市第一人民医院\n肺功能检查报告\n常规通气\n姓名：\n性别：男\n年龄：61岁\n身高：174 cm\n科别：呼吸内科\n住院号：门诊\n测试号：2025052513\n体重：85 kg\n测试日期 25-5-25\n测试时间 11:46:55\n预计值 实测值 实/预\nIRV [L] 1.14\nERV [L] 3.12\nIC [L] 0.61\nVT [L] 4.26 0.65 106.5\nVC IN [L] 4.26 3.01 70.7\nVC EX [L] 4.26 2.84 66.8\nBF [1/min] 20.00 17.72 88.6\nMV [L/min] 12.14 11.46 94.4\nVC MAX [L] 4.26 3.01 70.7\nFVC [L] 4.10 2.84 69.4\nFEV 1 [L] 3.22 2.51 78.0\nFEV 1 % FVC [%] 83.40 88.46 106.1\nFEV 1 % VC MAX [%] 76.23 83.54 109.6\nPEF [L/s] 8.21 6.40 77.9\nMEF 75 [L/s] 7.26 6.18 85.1\nMEF 50 [L/s] 4.35 3.04 69.9\nMEF 25 [L/s] 1.62 1.18 72.8\nMMEF 75/25 [L/s] . 3.45 2.26 65.4\nMVV [L/min] 119.91 77.46 64.6\nFEV 1*30 [L/min] 119.91 75.39 62.9\nVol [L]\nTLC 6\nFRC pleth\nRV 2\nPredA0.0 0.2 0.4 0.6 0.8 1.0\nTime [min]\nFlow [L/s]\nF/V ex\n10\n5\n0\n1\n2\n3\n4\n5\nF/V in\nVol [L]\n2\n1\n0\n1\n2\nTime [s]\n0 2 4 6 8 10 12\n测试结果：\n提示：\n1、轻度阻塞性肺通气功能障碍；\n2、肺储备功能下降。\n(请结合临床全面诊断)\n医生签字：毛锦涛\n报告日期：2025-5-27",
    "role": "user"
  }
]
2026-08-10 06:18:34,763 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:18:34,763 INFO     29 [qwen-vl-text] LLM output (len=1117):
{
  "exam_date": "2025-04-11",
  "report_date": "2025-04-11",
  "exam_name": "肺功能检查",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": "预计\n实1 %(实1/预)\n实2 %(实2/预)\n变异率\n测试日期\n25/4/11\n25/4/11\n测试时间\n14:56:47下午\n15:14:32下午\nFVC\n[L]\n3.13\n2.84\n90.6\n3.05\n97.4\n7.5\nFEV 1\n[L]\n2.70\n1.53\n56.9\n1.91\n71.0\n24.7\nFEV 1 % FVC\n[%]\n83.98\n54.07\n64.4\n62.70\n74.7\n16.0\nFEV 1 % VC MAX\n[%]\n81.31\n54.07\n66.5\n62.70\n77.1\n16.0\nPEF\n[L/s]\n6.46\n4.56\n70.7\n5.64\n87.3\n23.6\nMEF 75\n[L/s]\n5.73\n1.84\n32.1\n2.65\n46.3\n44.3\nMEF 50\n[L/s]\n4.06\n0.84\n20.7\n1.23\n30.4\n47.0\nMEF 25\n[L/s]\n1.77\n0.28\n15.6\n0.44\n25.0\n60.2\nMMEF 75/25\n[L/s]\n3.53\n0.65\n18.3\n1.02\n29.1\n58.8\nFET\n[s]\n8.46\n6.41\n-24.2\nV backextrapolation ex [L]\n0.03\n0.06\n71.7\nV backextrapol. % FVC [%]\n1.23\n1.96\n59.6\nFlow [L/s]\nF/V ex\n10\n5\n0\n1\n2\n3\n4\n5\n6\n7\n10\n5\nF/V In",
  "conclusion": "支气管舒张试验阳性。\n（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后。\nFEV1较基线增加大于12%，且绝对值增加大于200ml。）",
  "physician": "张青苹",
  "reviewer": "孙帅森"
}
2026-08-10 06:18:34,765 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=737988, prompt_len=1793
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共126行）
["肺功能报告单", "姓名：", "性别：女", "出生日期：1984/4/02", "年龄：41岁", "门诊/住院/体检：", "测试号：", "身高：160 cm", "体重：50 kg", "身份证号：", "预计", "实1 %(实1/预)", "实2 %(实2/预)", "变异率", "测试日期", "25/4/11", "25/4/11", "测试时间", "14:56:47下午", "15:14:32下午", "FVC", "[L]", "3.13", "2.84", "90.6", "3.05", "97.4", "7.5", "FEV 1", "[L]", "2.70", "1.53", "56.9", "1.91", "71.0", "24.7", "FEV 1 % FVC", "[%]", "83.98", "54.07", "64.4", "62.70", "74.7", "16.0", "FEV 1 % VC MAX", "[%]", "81.31", "54.07", "66.5", "62.70", "77.1", "16.0", "PEF", "[L/s]", "6.46", "4.56", "70.7", "5.64", "87.3", "23.6", "MEF 75", "[L/s]", "5.73", "1.84", "32.1", "2.65", "46.3", "44.3", "MEF 50", "[L/s]", "4.06", "0.84", "20.7", "1.23", "30.4", "47.0", "MEF 25", "[L/s]", "1.77", "0.28", "15.6", "0.44", "25.0", "60.2", "MMEF 75/25", "[L/s]", "3.53", "0.65", "18.3", "1.02", "29.1", "58.8", "FET", "[s]", "8.46", "6.41", "-24.2", "V backextrapolation ex [L]", "0.03", "0.06", "71.7", "V backextrapol. % FVC [%]", "1.23", "1.96", "59.6", "Flow [L/s]", "F/V ex", "10", "5", "0", "1", "2", "3", "4", "5", "6", "7", "10", "5", "F/V In", "医生意见：", "支气管舒张试验阳性。", "（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后。", "FEV1较基线增加大于12%，且绝对值增加大于200ml。）", "审核医生：孙帅森", "检测技师：张青苹"]

## 定位规则
1. 对于列表中的每行文本，找到它在图片中**精确出现**的位置
2. bbox必须是该行文字的**最小紧密包围框**，紧贴文字边缘，不要包含额外的空白区域
3. 坐标归一化到0-1000，格式[x1,y1,x2,y2]
4. 如果某行文本在图片中未找到，跳过不输出
5. text字段必须与给定的文本完全一致

## 包围框精度要求
- x1必须紧贴该行第一个字符的左边缘
- x2必须紧贴该行最后一个字符的右边缘
- y1必须紧贴该行文字的顶部
- y2必须紧贴该行文字的底部
- 禁止将多行文字合并到同一个bbox中

## 严格JSON格式要求
直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。
正确示例：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230]},
  {"text": "年龄：68岁", "bbox": [100, 250, 270, 280]}
]
错误示例（禁止额外字段）：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230], "label": "个人信息"}
]
请直接输出纯JSON数组，不要用markdown代码块包裹。
2026-08-10 06:19:08,585 INFO     29 [qwen-vl-text] coord API raw response (len=6549):
[
	{"text": "肺功能报告单", "bbox": [407, 83, 554, 102]},
	{"text": "姓名：", "bbox": [76, 104, 130, 117]},
	{"text": "性别：", "bbox": [481, 104, 535, 117]},
	{"text": "女", "bbox": [680, 104, 701, 117]},
	{"text": "出生日期：", "bbox": [76, 117, 171, 131]},
	{"text": "1984/4/02", "bbox": [273, 119, 371, 131]},
	{"text": "年龄：", "bbox": [481, 117, 535, 131]},
	{"text": "41岁", "bbox": [680, 117, 733, 131]},
	{"text": "门诊/住院/体检：", "bbox": [76, 131, 237, 145]},
	{"text": "测试号：", "bbox": [481, 131, 555, 145]},
	{"text": "身高：", "bbox": [76, 145, 130, 158]},
	{"text": "160 cm", "bbox": [273, 147, 340, 159]},
	{"text": "体重：", "bbox": [481, 145, 535, 158]},
	{"text": "50 kg", "bbox": [680, 147, 734, 160]},
	{"text": "身份证号：", "bbox": [76, 158, 171, 172]},
	{"text": "预计", "bbox": [340, 179, 377, 193]},
	{"text": "实1 %(实1/预)", "bbox": [462, 179, 580, 193]},
	{"text": "实2 %(实2/预)", "bbox": [666, 179, 783, 193]},
	{"text": "变异率", "bbox": [814, 179, 870, 193]},
	{"text": "测试日期", "bbox": [87, 195, 161, 209]},
	{"text": "25/4/11", "bbox": [428, 196, 490, 209]},
	{"text": "25/4/11", "bbox": [632, 196, 694, 209]},
	{"text": "测试时间", "bbox": [87, 210, 161, 224]},
	{"text": "14:56:47下午", "bbox": [387, 210, 492, 224]},
	{"text": "15:14:32下午", "bbox": [589, 210, 696, 224]},
	{"text": "FVC", "bbox": [87, 243, 124, 256]},
	{"text": "[L]", "bbox": [292, 243, 315, 258]},
	{"text": "3.13", "bbox": [340, 243, 377, 256]},
	{"text": "2.84", "bbox": [454, 243, 491, 256]},
	{"text": "90.6", "bbox": [543, 243, 580, 256]},
	{"text": "3.05", "bbox": [658, 243, 695, 256]},
	{"text": "97.4", "bbox": [747, 243, 784, 256]},
	{"text": "7.5", "bbox": [845, 243, 871, 256]},
	{"text": "FEV 1", "bbox": [87, 258, 137, 272]},
	{"text": "[L]", "bbox": [292, 258, 315, 273]},
	{"text": "2.70", "bbox": [340, 258, 377, 272]},
	{"text": "1.53", "bbox": [454, 258, 491, 272]},
	{"text": "56.9", "bbox": [543, 258, 580, 272]},
	{"text": "1.91", "bbox": [658, 258, 695, 272]},
	{"text": "71.0", "bbox": [747, 258, 784, 272]},
	{"text": "24.7", "bbox": [835, 258, 871, 272]},
	{"text": "FEV 1 % FVC", "bbox": [87, 274, 200, 288]},
	{"text": "[%]", "bbox": [288, 274, 315, 289]},
	{"text": "83.98", "bbox": [330, 274, 377, 288]},
	{"text": "54.07", "bbox": [444, 274, 491, 288]},
	{"text": "64.4", "bbox": [543, 274, 580, 288]},
	{"text": "62.70", "bbox": [648, 274, 695, 288]},
	{"text": "74.7", "bbox": [747, 274, 784, 288]},
	{"text": "16.0", "bbox": [835, 274, 871, 288]},
	{"text": "FEV 1 % VC MAX", "bbox": [87, 290, 235, 304]},
	{"text": "[%]", "bbox": [288, 290, 315, 305]},
	{"text": "81.31", "bbox": [330, 290, 377, 304]},
	{"text": "54.07", "bbox": [444, 290, 491, 304]},
	{"text": "66.5", "bbox": [543, 290, 580, 304]},
	{"text": "62.70", "bbox": [648, 290, 695, 304]},
	{"text": "77.1", "bbox": [747, 290, 784, 304]},
	{"text": "16.0", "bbox": [835, 290, 871, 304]},
	{"text": "PEF", "bbox": [87, 306, 124, 320]},
	{"text": "[L/s]", "bbox": [277, 306, 315, 321]},
	{"text": "6.46", "bbox": [340, 306, 377, 320]},
	{"text": "4.56", "bbox": [454, 306, 491, 320]},
	{"text": "70.7", "bbox": [543, 306, 580, 320]},
	{"text": "5.64", "bbox": [658, 306, 695, 320]},
	{"text": "87.3", "bbox": [747, 306, 784, 320]},
	{"text": "23.6", "bbox": [835, 306, 871, 320]},
	{"text": "MEF 75", "bbox": [87, 322, 151, 336]},
	{"text": "[L/s]", "bbox": [277, 322, 315, 337]},
	{"text": "5.73", "bbox": [340, 322, 377, 336]},
	{"text": "1.84", "bbox": [454, 322, 491, 336]},
	{"text": "32.1", "bbox": [543, 322, 580, 336]},
	{"text": "2.65", "bbox": [658, 322, 695, 336]},
	{"text": "46.3", "bbox": [747, 322, 784, 336]},
	{"text": "44.3", "bbox": [835, 322, 871, 336]},
	{"text": "MEF 50", "bbox": [87, 338, 151, 352]},
	{"text": "[L/s]", "bbox": [277, 338, 315, 353]},
	{"text": "4.06", "bbox": [340, 338, 377, 352]},
	{"text": "0.84", "bbox": [454, 338, 491, 352]},
	{"text": "20.7", "bbox": [543, 338, 580, 352]},
	{"text": "1.23", "bbox": [658, 338, 695, 352]},
	{"text": "30.4", "bbox": [747, 338, 784, 352]},
	{"text": "47.0", "bbox": [835, 338, 871, 352]},
	{"text": "MEF 25", "bbox": [87, 354, 151, 368]},
	{"text": "[L/s]", "bbox": [277, 354, 315, 369]},
	{"text": "1.77", "bbox": [340, 354, 377, 368]},
	{"text": "0.28", "bbox": [454, 354, 491, 368]},
	{"text": "15.6", "bbox": [543, 354, 580, 368]},
	{"text": "0.44", "bbox": [658, 354, 695, 368]},
	{"text": "25.0", "bbox": [747, 354, 784, 368]},
	{"text": "60.2", "bbox": [835, 354, 871, 368]},
	{"text": "MMEF 75/25", "bbox": [87, 370, 192, 384]},
	{"text": "[L/s]", "bbox": [277, 370, 315, 385]},
	{"text": "3.53", "bbox": [340, 370, 377, 384]},
	{"text": "0.65", "bbox": [454, 370, 491, 384]},
	{"text": "18.3", "bbox": [543, 370, 580, 384]},
	{"text": "1.02", "bbox": [658, 370, 695, 384]},
	{"text": "29.1", "bbox": [747, 370, 784, 384]},
	{"text": "58.8", "bbox": [835, 370, 871, 384]},
	{"text": "FET", "bbox": [87, 386, 124, 400]},
	{"text": "[s]", "bbox": [292, 386, 315, 401]},
	{"text": "8.46", "bbox": [454, 386, 491, 400]},
	{"text": "6.41", "bbox": [658, 386, 695, 400]},
	{"text": "-24.2", "bbox": [829, 386, 871, 400]},
	{"text": "V backextrapolation ex [L]", "bbox": [87, 402, 315, 416]},
	{"text": "0.03", "bbox": [454, 402, 491, 416]},
	{"text": "0.06", "bbox": [658, 402, 695, 416]},
	{"text": "71.7", "bbox": [835, 402, 871, 416]},
	{"text": "V backextrapol. % FVC [%]", "bbox": [87, 418, 315, 432]},
	{"text": "1.23", "bbox": [454, 418, 491, 432]},
	{"text": "1.96", "bbox": [658, 418, 695, 432]},
	{"text": "59.6", "bbox": [835, 418, 871, 432]},
	{"text": "Flow [L/s]", "bbox": [142, 503, 194, 514]},
	{"text": "F/V ex", "bbox": [589, 504, 622, 513]},
	{"text": "10", "bbox": [124, 520, 140, 529]},
	{"text": "5", "bbox": [129, 548, 140, 557]},
	{"text": "0", "bbox": [129, 575, 137, 584]},
	{"text": "1", "bbox": [224, 584, 231, 592]},
	{"text": "2", "bbox": [310, 584, 318, 592]},
	{"text": "3", "bbox": [396, 584, 404, 592]},
	{"text": "4", "bbox": [483, 584, 491, 592]},
	{"text": "5", "bbox": [570, 584, 578, 592]},
	{"text": "6", "bbox": [658, 584, 667, 592]},
	{"text": "7", "bbox": [747, 584, 755, 592]},
	{"text": "10", "bbox": [124, 629, 140, 638]},
	{"text": "5", "bbox": [129, 602, 140, 611]},
	{"text": "F/V In", "bbox": [589, 646, 619, 655]},
	{"text": "医生意见：", "bbox": [84, 666, 190, 684]},
	{"text": "支气管舒张试验阳性。", "bbox": [84, 686, 257, 699]},
	{"text": "（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后。", "bbox": [92, 699, 493, 711]},
	{"text": "FEV1较基线增加大于12%，且绝对值增加大于200ml。）", "bbox": [84, 711, 513, 723]},
	{"text": "审核医生：孙帅森", "bbox": [645, 795, 783, 810]},
	{"text": "检测技师：张青苹", "bbox": [641, 818, 800, 840]}
]
2026-08-10 06:19:08,585 INFO     29 [qwen-vl-text] coord API: raw_items=131, valid_items=131, elapsed=33.8s
2026-08-10 06:19:08,585 INFO     29 [qwen-vl-text] coord item[0]: text=肺功能报告单, bbox=[407, 83, 554, 102]
2026-08-10 06:19:08,585 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[76, 104, 130, 117]
2026-08-10 06:19:08,585 INFO     29 [qwen-vl-text] coord item[2]: text=性别：, bbox=[481, 104, 535, 117]
2026-08-10 06:19:08,585 INFO     29 [qwen-vl-text] coord item[3]: text=女, bbox=[680, 104, 701, 117]
2026-08-10 06:19:08,585 INFO     29 [qwen-vl-text] coord item[4]: text=出生日期：, bbox=[76, 117, 171, 131]
2026-08-10 06:19:08,585 INFO     29 [qwen-vl-text] coord item[5]: text=1984/4/02, bbox=[273, 119, 371, 131]
2026-08-10 06:19:08,585 INFO     29 [qwen-vl-text] coord item[6]: text=年龄：, bbox=[481, 117, 535, 131]
2026-08-10 06:19:08,585 INFO     29 [qwen-vl-text] coord item[7]: text=41岁, bbox=[680, 117, 733, 131]
2026-08-10 06:19:08,585 INFO     29 [qwen-vl-text] coord item[8]: text=门诊/住院/体检：, bbox=[76, 131, 237, 145]
2026-08-10 06:19:08,585 INFO     29 [qwen-vl-text] coord item[9]: text=测试号：, bbox=[481, 131, 555, 145]
2026-08-10 06:19:08,585 INFO     29 [qwen-vl-text] coord item[10]: text=身高：, bbox=[76, 145, 130, 158]
2026-08-10 06:19:08,585 INFO     29 [qwen-vl-text] coord item[11]: text=160 cm, bbox=[273, 147, 340, 159]
2026-08-10 06:19:08,585 INFO     29 [qwen-vl-text] coord item[12]: text=体重：, bbox=[481, 145, 535, 158]
2026-08-10 06:19:08,585 INFO     29 [qwen-vl-text] coord item[13]: text=50 kg, bbox=[680, 147, 734, 160]
2026-08-10 06:19:08,585 INFO     29 [qwen-vl-text] coord item[14]: text=身份证号：, bbox=[76, 158, 171, 172]
2026-08-10 06:19:08,585 INFO     29 [qwen-vl-text] coord item[15]: text=预计, bbox=[340, 179, 377, 193]
2026-08-10 06:19:08,585 INFO     29 [qwen-vl-text] coord item[16]: text=实1 %(实1/预), bbox=[462, 179, 580, 193]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[17]: text=实2 %(实2/预), bbox=[666, 179, 783, 193]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[18]: text=变异率, bbox=[814, 179, 870, 193]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[19]: text=测试日期, bbox=[87, 195, 161, 209]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[20]: text=25/4/11, bbox=[428, 196, 490, 209]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[21]: text=25/4/11, bbox=[632, 196, 694, 209]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[22]: text=测试时间, bbox=[87, 210, 161, 224]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[23]: text=14:56:47下午, bbox=[387, 210, 492, 224]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[24]: text=15:14:32下午, bbox=[589, 210, 696, 224]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[25]: text=FVC, bbox=[87, 243, 124, 256]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[26]: text=[L], bbox=[292, 243, 315, 258]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[27]: text=3.13, bbox=[340, 243, 377, 256]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[28]: text=2.84, bbox=[454, 243, 491, 256]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[29]: text=90.6, bbox=[543, 243, 580, 256]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[30]: text=3.05, bbox=[658, 243, 695, 256]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[31]: text=97.4, bbox=[747, 243, 784, 256]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[32]: text=7.5, bbox=[845, 243, 871, 256]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[33]: text=FEV 1, bbox=[87, 258, 137, 272]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[34]: text=[L], bbox=[292, 258, 315, 273]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[35]: text=2.70, bbox=[340, 258, 377, 272]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[36]: text=1.53, bbox=[454, 258, 491, 272]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[37]: text=56.9, bbox=[543, 258, 580, 272]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[38]: text=1.91, bbox=[658, 258, 695, 272]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[39]: text=71.0, bbox=[747, 258, 784, 272]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[40]: text=24.7, bbox=[835, 258, 871, 272]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[41]: text=FEV 1 % FVC, bbox=[87, 274, 200, 288]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[42]: text=[%], bbox=[288, 274, 315, 289]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[43]: text=83.98, bbox=[330, 274, 377, 288]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[44]: text=54.07, bbox=[444, 274, 491, 288]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[45]: text=64.4, bbox=[543, 274, 580, 288]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[46]: text=62.70, bbox=[648, 274, 695, 288]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[47]: text=74.7, bbox=[747, 274, 784, 288]
2026-08-10 06:19:08,586 INFO     29 [qwen-vl-text] coord item[48]: text=16.0, bbox=[835, 274, 871, 288]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[49]: text=FEV 1 % VC MAX, bbox=[87, 290, 235, 304]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[50]: text=[%], bbox=[288, 290, 315, 305]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[51]: text=81.31, bbox=[330, 290, 377, 304]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[52]: text=54.07, bbox=[444, 290, 491, 304]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[53]: text=66.5, bbox=[543, 290, 580, 304]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[54]: text=62.70, bbox=[648, 290, 695, 304]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[55]: text=77.1, bbox=[747, 290, 784, 304]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[56]: text=16.0, bbox=[835, 290, 871, 304]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[57]: text=PEF, bbox=[87, 306, 124, 320]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[58]: text=[L/s], bbox=[277, 306, 315, 321]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[59]: text=6.46, bbox=[340, 306, 377, 320]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[60]: text=4.56, bbox=[454, 306, 491, 320]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[61]: text=70.7, bbox=[543, 306, 580, 320]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[62]: text=5.64, bbox=[658, 306, 695, 320]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[63]: text=87.3, bbox=[747, 306, 784, 320]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[64]: text=23.6, bbox=[835, 306, 871, 320]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[65]: text=MEF 75, bbox=[87, 322, 151, 336]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[66]: text=[L/s], bbox=[277, 322, 315, 337]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[67]: text=5.73, bbox=[340, 322, 377, 336]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[68]: text=1.84, bbox=[454, 322, 491, 336]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[69]: text=32.1, bbox=[543, 322, 580, 336]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[70]: text=2.65, bbox=[658, 322, 695, 336]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[71]: text=46.3, bbox=[747, 322, 784, 336]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[72]: text=44.3, bbox=[835, 322, 871, 336]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[73]: text=MEF 50, bbox=[87, 338, 151, 352]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[74]: text=[L/s], bbox=[277, 338, 315, 353]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[75]: text=4.06, bbox=[340, 338, 377, 352]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[76]: text=0.84, bbox=[454, 338, 491, 352]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[77]: text=20.7, bbox=[543, 338, 580, 352]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[78]: text=1.23, bbox=[658, 338, 695, 352]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[79]: text=30.4, bbox=[747, 338, 784, 352]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[80]: text=47.0, bbox=[835, 338, 871, 352]
2026-08-10 06:19:08,587 INFO     29 [qwen-vl-text] coord item[81]: text=MEF 25, bbox=[87, 354, 151, 368]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[82]: text=[L/s], bbox=[277, 354, 315, 369]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[83]: text=1.77, bbox=[340, 354, 377, 368]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[84]: text=0.28, bbox=[454, 354, 491, 368]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[85]: text=15.6, bbox=[543, 354, 580, 368]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[86]: text=0.44, bbox=[658, 354, 695, 368]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[87]: text=25.0, bbox=[747, 354, 784, 368]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[88]: text=60.2, bbox=[835, 354, 871, 368]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[89]: text=MMEF 75/25, bbox=[87, 370, 192, 384]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[90]: text=[L/s], bbox=[277, 370, 315, 385]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[91]: text=3.53, bbox=[340, 370, 377, 384]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[92]: text=0.65, bbox=[454, 370, 491, 384]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[93]: text=18.3, bbox=[543, 370, 580, 384]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[94]: text=1.02, bbox=[658, 370, 695, 384]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[95]: text=29.1, bbox=[747, 370, 784, 384]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[96]: text=58.8, bbox=[835, 370, 871, 384]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[97]: text=FET, bbox=[87, 386, 124, 400]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[98]: text=[s], bbox=[292, 386, 315, 401]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[99]: text=8.46, bbox=[454, 386, 491, 400]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[100]: text=6.41, bbox=[658, 386, 695, 400]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[101]: text=-24.2, bbox=[829, 386, 871, 400]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[102]: text=V backextrapolation ex [L], bbox=[87, 402, 315, 416]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[103]: text=0.03, bbox=[454, 402, 491, 416]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[104]: text=0.06, bbox=[658, 402, 695, 416]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[105]: text=71.7, bbox=[835, 402, 871, 416]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[106]: text=V backextrapol. % FVC [%], bbox=[87, 418, 315, 432]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[107]: text=1.23, bbox=[454, 418, 491, 432]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[108]: text=1.96, bbox=[658, 418, 695, 432]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[109]: text=59.6, bbox=[835, 418, 871, 432]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[110]: text=Flow [L/s], bbox=[142, 503, 194, 514]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[111]: text=F/V ex, bbox=[589, 504, 622, 513]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[112]: text=10, bbox=[124, 520, 140, 529]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[113]: text=5, bbox=[129, 548, 140, 557]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[114]: text=0, bbox=[129, 575, 137, 584]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[115]: text=1, bbox=[224, 584, 231, 592]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[116]: text=2, bbox=[310, 584, 318, 592]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[117]: text=3, bbox=[396, 584, 404, 592]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[118]: text=4, bbox=[483, 584, 491, 592]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[119]: text=5, bbox=[570, 584, 578, 592]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[120]: text=6, bbox=[658, 584, 667, 592]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[121]: text=7, bbox=[747, 584, 755, 592]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[122]: text=10, bbox=[124, 629, 140, 638]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[123]: text=5, bbox=[129, 602, 140, 611]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[124]: text=F/V In, bbox=[589, 646, 619, 655]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[125]: text=医生意见：, bbox=[84, 666, 190, 684]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[126]: text=支气管舒张试验阳性。, bbox=[84, 686, 257, 699]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[127]: text=（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后。, bbox=[92, 699, 493, 711]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[128]: text=FEV1较基线增加大于12%，且绝对值增加大于200ml。）, bbox=[84, 711, 513, 723]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[129]: text=审核医生：孙帅森, bbox=[645, 795, 783, 810]
2026-08-10 06:19:08,588 INFO     29 [qwen-vl-text] coord item[130]: text=检测技师：张青苹, bbox=[641, 818, 800, 840]
2026-08-10 06:19:08,589 INFO     29 [qwen-vl-text] page=4 — 126/126 coords, api_time=33.8s
2026-08-10 06:19:08,589 INFO     29 [qwen-vl-text] new_positions (126):
[[4, 242.165, 329.63, 69.886, 85.884], [4, 45.22, 77.35, 87.568, 98.514], [4, 286.195, 318.325, 87.568, 98.514], [4, 404.59999999999997, 417.09499999999997, 87.568, 98.514], [4, 45.22, 101.74499999999999, 98.514, 110.30199999999999], [4, 162.435, 220.74499999999998, 100.198, 110.30199999999999], [4, 286.195, 318.325, 98.514, 110.30199999999999], [4, 404.59999999999997, 436.135, 98.514, 110.30199999999999], [4, 45.22, 141.015, 110.30199999999999, 122.08999999999999], [4, 286.195, 330.22499999999997, 110.30199999999999, 122.08999999999999], [4, 45.22, 77.35, 122.08999999999999, 133.036], [4, 162.435, 202.29999999999998, 123.774, 133.878], [4, 286.195, 318.325, 122.08999999999999, 133.036], [4, 404.59999999999997, 436.72999999999996, 123.774, 134.72], [4, 45.22, 101.74499999999999, 133.036, 144.82399999999998], [4, 202.29999999999998, 224.315, 150.718, 162.506], [4, 274.89, 345.09999999999997, 150.718, 162.506], [4, 396.27, 465.885, 150.718, 162.506], [4, 484.33, 517.65, 150.718, 162.506], [4, 51.765, 95.795, 164.19, 175.97799999999998], [4, 254.66, 291.55, 165.03199999999998, 175.97799999999998], [4, 376.03999999999996, 412.93, 165.03199999999998, 175.97799999999998], [4, 51.765, 95.795, 176.82, 188.608], [4, 230.265, 292.74, 176.82, 188.608], [4, 350.455, 414.12, 176.82, 188.608], [4, 51.765, 73.78, 204.606, 215.552], [4, 173.73999999999998, 187.42499999999998, 204.606, 217.236], [4, 202.29999999999998, 224.315, 204.606, 215.552], [4, 270.13, 292.145, 204.606, 215.552], [4, 323.085, 345.09999999999997, 204.606, 215.552], [4, 391.51, 413.525, 204.606, 215.552], [4, 444.465, 466.47999999999996, 204.606, 215.552], [4, 502.775, 518.245, 204.606, 215.552], [4, 51.765, 81.515, 217.236, 229.024], [4, 173.73999999999998, 187.42499999999998, 217.236, 229.86599999999999], [4, 202.29999999999998, 224.315, 217.236, 229.024], [4, 270.13, 292.145, 217.236, 229.024], [4, 323.085, 345.09999999999997, 217.236, 229.024], [4, 391.51, 413.525, 217.236, 229.024], [4, 444.465, 466.47999999999996, 217.236, 229.024], [4, 496.825, 518.245, 217.236, 229.024], [4, 51.765, 119.0, 230.708, 242.49599999999998], [4, 171.35999999999999, 187.42499999999998, 230.708, 243.338], [4, 196.35, 224.315, 230.708, 242.49599999999998], [4, 264.18, 292.145, 230.708, 242.49599999999998], [4, 323.085, 345.09999999999997, 230.708, 242.49599999999998], [4, 385.56, 413.525, 230.708, 242.49599999999998], [4, 444.465, 466.47999999999996, 230.708, 242.49599999999998], [4, 496.825, 518.245, 230.708, 242.49599999999998], [4, 51.765, 139.825, 244.17999999999998, 255.968], [4, 171.35999999999999, 187.42499999999998, 244.17999999999998, 256.81], [4, 196.35, 224.315, 244.17999999999998, 255.968], [4, 264.18, 292.145, 244.17999999999998, 255.968], [4, 323.085, 345.09999999999997, 244.17999999999998, 255.968], [4, 385.56, 413.525, 244.17999999999998, 255.968], [4, 444.465, 466.47999999999996, 244.17999999999998, 255.968], [4, 496.825, 518.245, 244.17999999999998, 255.968], [4, 51.765, 73.78, 257.652, 269.44], [4, 164.815, 187.42499999999998, 257.652, 270.282], [4, 202.29999999999998, 224.315, 257.652, 269.44], [4, 270.13, 292.145, 257.652, 269.44], [4, 323.085, 345.09999999999997, 257.652, 269.44], [4, 391.51, 413.525, 257.652, 269.44], [4, 444.465, 466.47999999999996, 257.652, 269.44], [4, 496.825, 518.245, 257.652, 269.44], [4, 51.765, 89.845, 271.12399999999997, 282.912], [4, 164.815, 187.42499999999998, 271.12399999999997, 283.75399999999996], [4, 202.29999999999998, 224.315, 271.12399999999997, 282.912], [4, 270.13, 292.145, 271.12399999999997, 282.912], [4, 323.085, 345.09999999999997, 271.12399999999997, 282.912], [4, 391.51, 413.525, 271.12399999999997, 282.912], [4, 444.465, 466.47999999999996, 271.12399999999997, 282.912], [4, 496.825, 518.245, 271.12399999999997, 282.912], [4, 51.765, 89.845, 284.596, 296.384], [4, 164.815, 187.42499999999998, 284.596, 297.226], [4, 202.29999999999998, 224.315, 284.596, 296.384], [4, 270.13, 292.145, 284.596, 296.384], [4, 323.085, 345.09999999999997, 284.596, 296.384], [4, 391.51, 413.525, 284.596, 296.384], [4, 444.465, 466.47999999999996, 284.596, 296.384], [4, 496.825, 518.245, 284.596, 296.384], [4, 51.765, 89.845, 298.068, 309.856], [4, 164.815, 187.42499999999998, 298.068, 310.698], [4, 202.29999999999998, 224.315, 298.068, 309.856], [4, 270.13, 292.145, 298.068, 309.856], [4, 323.085, 345.09999999999997, 298.068, 309.856], [4, 391.51, 413.525, 298.068, 309.856], [4, 444.465, 466.47999999999996, 298.068, 309.856], [4, 496.825, 518.245, 298.068, 309.856], [4, 51.765, 114.24, 311.53999999999996, 323.328], [4, 164.815, 187.42499999999998, 311.53999999999996, 324.17], [4, 202.29999999999998, 224.315, 311.53999999999996, 323.328], [4, 270.13, 292.145, 311.53999999999996, 323.328], [4, 323.085, 345.09999999999997, 311.53999999999996, 323.328], [4, 391.51, 413.525, 311.53999999999996, 323.328], [4, 444.465, 466.47999999999996, 311.53999999999996, 323.328], [4, 496.825, 518.245, 311.53999999999996, 323.328], [4, 51.765, 73.78, 325.012, 336.8], [4, 173.73999999999998, 187.42499999999998, 325.012, 337.642], [4, 270.13, 292.145, 325.012, 336.8], [4, 391.51, 413.525, 325.012, 336.8], [4, 493.255, 518.245, 325.012, 336.8], [4, 51.765, 187.42499999999998, 338.484, 350.272], [4, 270.13, 292.145, 338.484, 350.272], [4, 391.51, 413.525, 338.484, 350.272], [4, 496.825, 518.245, 338.484, 350.272], [4, 51.765, 187.42499999999998, 351.95599999999996, 363.74399999999997], [4, 270.13, 292.145, 351.95599999999996, 363.74399999999997], [4, 391.51, 413.525, 351.95599999999996, 363.74399999999997], [4, 496.825, 518.245, 351.95599999999996, 363.74399999999997], [4, 84.49, 115.42999999999999, 423.526, 432.788], [4, 350.455, 370.09, 424.368, 431.94599999999997], [4, 73.78, 83.3, 437.84, 445.418], [4, 76.755, 83.3, 461.416, 468.99399999999997], [4, 76.755, 81.515, 484.15, 491.728], [4, 133.28, 137.445, 491.728, 498.464], [4, 184.45, 189.20999999999998, 491.728, 498.464], [4, 235.61999999999998, 240.38, 491.728, 498.464], [4, 287.385, 292.145, 491.728, 498.464], [4, 339.15, 343.90999999999997, 491.728, 498.464], [4, 391.51, 396.865, 491.728, 498.464], [4, 444.465, 449.22499999999997, 491.728, 498.464], [4, 73.78, 83.3, 529.6179999999999, 537.196], [4, 76.755, 83.3, 506.88399999999996, 514.462], [4, 350.455, 368.305, 543.932, 551.51], [4, 49.98, 113.05, 560.7719999999999, 575.928]]
2026-08-10 06:19:08,589 INFO     29 [qwen-vl-text] ═══ DONE ═══ 126 positions, pages=1, time=62.5s
2026-08-10 06:19:08,861 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 06:19:08,861 INFO     29 [Trace] task=801b5176 | doc=DAXI-哮喘.pdf | Extractor:ExaminationReport | outputs={"chunks": "5 items, types={'ExaminationReport': 5}", "html": "", "json": "2283 items", "markdown": "", "text": "", "name": "DAXI-哮喘.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "14 items, types={'OutpatientRecord': 14}", "chunks_Prescription": "6 items, types={'PrescriptionRecord': 6}", "chunks_LabExam": "13 items, types={'LabReport': 13}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 14, \"chunks_Prescription\": 6, \"chunks_LabExam\": 13}"}
2026-08-10 06:19:08,861 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 06:19:08,862 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T06:19:08.861+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 2, "failed": 0, "current": {"801b5176947e11f182aec5d26bc6c4ae": {"id": "801b5176947e11f182aec5d26bc6c4ae", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786340646131, "task_type": "dataflow", "root_trace_id": "97b84aa3d1154f6db808c154432c5554", "root_traceparent": "00-97b84aa3d1154f6db808c154432c5554-dd9503e7c4e14a5d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "dbae825c948211f1bd9827cf206dfa2d": {"id": "dbae825c948211f1bd9827cf206dfa2d", "doc_id": "db492056948211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LGWE-\u827e\u7279\u7f8e\u54ee\u5598-\u6d1b\u9633\u4e09.pdf", "type": "pdf", "location": "LGWE-\u827e\u7279\u7f8e\u54ee\u5598-\u6d1b\u9633\u4e09.pdf", "size": 1648931, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786342517754, "task_type": "dataflow", "root_trace_id": "aaa86c5dcc2c462f88c0ac982e1d484f", "root_traceparent": "00-aaa86c5dcc2c462f88c0ac982e1d484f-c2d6050d16147908-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 06:19:08,866 INFO     29 [ChunkMerger] Merged 40 chunks from 8 sources: {'Extractor:LabExam': 13, 'Extractor:Imaging': 1, 'Extractor:Clinical': 14, 'Extractor:Medication': 1, 'Extractor:Prescription': 6, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 5} (filtered 2 noise chunks)
2026-08-10 06:19:08,878 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-10 06:19:08,879 INFO     29 [Trace] task=801b5176 | doc=DAXI-哮喘.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "40 items, types={'LabReport': 13, 'OutpatientRecord': 14, 'PrescriptionRecord': 6, 'DischargeRecord': 1, 'AdmissionRecord': 1, 'ExaminationReport': 5}", "name": "DAXI-哮喘.pdf"}
2026-08-10 06:19:08,879 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 06:19:09,966 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786342572850, 'update_date': datetime.datetime(2026, 8, 10, 6, 16, 12), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 778292, 'status': '1'}
2026-08-10 06:19:10,222 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   白细胞数目  WBC  4.28  10^9/L  3.5~9.5  False    淋巴细胞百分比  Lym%  28.4  %  20~50  False    单核细胞百分比  Mon%  4.7  %  3~10  False    中性粒细胞百分比  Neu%  64.4  %  40~75  False    嗜酸性细胞百分比  Eos%  2.4  %  0.4~8  False    嗜碱性细胞百分比  Bas%  0.1  %  0.0~1.0  False    淋巴细胞数目  Lym#  1.22  10^9/L  1.1~3.2  False    单核细胞数目  Mon#  0.20  10^9/L  0.1~0.6  False    中性粒细胞数目  Neu#  2.76  10^9/L  1.8~6.3  False    嗜酸性细胞数目  Eos#  0.10  10^9/L  0.02~0.52  False    嗜碱性细胞数目  Bas#  0.00  10^9/L  0.00~0.06  False    红细胞数目  RBC  4.70  10^12/L  3.8~5.1  False    血红蛋白  HGB  122  g/L  115~150  False    红细胞压积  HCT  37.8  %  35~45  False    平均红细胞体积  MCV  80.4  fL  82~100  True    平均红细胞血红蛋白含量  MCH  26.0  pg  27~34  True    平均红细胞血红蛋白浓度  MCHC  323  g/L  316~354  False    红细胞分布宽度变异系数  RDW-CV  15.2  %  11~16  False    红细胞分布宽度标准差  RDW-SD  43.0  fL  35.0~56.0  False    血小板数目  PLT  224  10^9/L  125~350  False    平均血小板体积  MPV  8.0  fL  6.5~12  False    血小板分布宽度  PDW  16.0  fL  9~17  False    血小板压积  PCT  0.180  %  0.108~  False    大型血小板比率  P-LCR  15.8  %  11~45  False    未成熟粒细胞百分比  IG%  0.4  %  0.0~0.6  False    未成熟粒细胞计数  IG#  0.02  10^9/L  0.00~0.06  False   
---
   血沉  ESR  7  mm/h  0~20  False   
---
   总胆红素  TBIL  8.5  μmol/L  0.0~21.0  False    直接胆红素  DBIL  2.3  μmol/L  0.0~8.0  False    间接胆红素  IBIL  6.2  μmol/L  0.0~13.0  False    谷丙转氨酶  ALT  12.2  U/L  7~40  False    谷草转氨酶  AST  18  U/L  13~35  False    谷草/谷丙  AST/ALT  1.48  None  0.8~1.5  False    总蛋白  TP  73.6  g/L  65.0~85.0  False    白蛋白  ALB  46.0  g/L  40.0~55.0  False    球蛋白  GLB  27.6  g/L  20.0~40.0  False    白球比值  A/G  1.67  None  1.20~2.4  False    谷氨酰转肽酶  GGT  9.0  U/L  7~45  False    碱性磷酸酶  ALP  66  U/L  40~150  False    尿素  Urea  4.27  mmol/L  2.6~7.5  False    肌酐  CRE  49.9  μmol/L  41~73  False   
---
   清洁度  None  II  None  ~≤II  False    白细胞  None  5-15  /HP  ≤15/HP  False    红细胞  None  未检出  None  ~未检出  False    线索细胞  None  未检出  None  ~未检出  False    上皮细胞  None  10-15  None  ~满视野  False    滴虫  None  未检出  None  ~未检出  False    菌丝  None  未检出  None  ~未检出  False    孢子  None  未检出  None  ~未检出  False    芽生孢子  None  未检出  None  ~未检出  False    菌群密集度  None  ++  None  ~++  False    多样性  None  +  None  ~++  False    优势菌  None  G+杆菌  None  ~G阳性杆菌  False    β-N-乙酰氨基葡萄糖苷酶(NAG)  NAG  -  None  ~-  False    唾液酸苷酶  None  -  None  ~-  False    白细胞酯酶  None  -  None  ~-  False    胺试验  None  -  None  ~-  False    脯氨酸氨基肽酶PIP  PIP  -  None  ~-  False    过氧化氢(H2O2)  H2O2  +  None  ~-  True    pH值  None  3.8  None  3.8 ~ 4.5  False    Nugent评分2  None  AV评分1  None  None  False   
---
   [β-HCG]人绒毛膜促性腺激素  β-HCG  0.40  None  非孕期 0~2.9; 0.2-1周 5~50; 1-2周 50~500; 2-3周 100~5000; 3-4周 500~10000; 4-5周 1000~50000; 5-6周 10000~100000; 6-8周 15000~200000  False   
---
   CA-125  CA-125  59.70  U/ml  0.00~35.00  True   
---
   颜色  颜色  黄色  None  清  False    尿酸结晶  尿酸结晶  0  个/ul  0~15  False    浊度  浊度  清亮  None  清  False    草酸钙结晶  草酸钙结晶  0  个/ul  0~30  False    葡萄糖  GLU  -  None  阴性  False    上皮细胞  上皮细胞  14  个/ul  0~20  False    潜血  BLD  -  None  阴性  False    粘液丝  粘液丝  5  个/ul  0~20  False    白细胞  LEU  2+  None  阴性  True    酵母菌  酵母菌  6  个/ul  0~0  True    蛋白质  PRO  -  None  阴性  False    透明管型  透明管型  0  个/ul  0~1  False    亚硝酸盐  NIT  +  None  阴性  True    颗粒管型  颗粒管型  0  个/ul  0~0  False    尿胆素原  URO  -  None  阴性  False    小圆上皮  小圆上皮  0  个/ul  0~3  False    胆红素  BIL  -  None  阴性  False    其他管型  其他管型  0  个/ul  0~0  False    酮体  KET  -  None  阴性  False    其他上皮  其他上皮  0  个/ul  0~10  False    维生素C  Vc  -  None  -  False    异常红细胞  异常红细胞  0  个/ul  0~5  False    酸碱性  pH  6.0  None  5.0~8.5  False    细菌  细菌  1072  个/ul  0~50  True    比重  SG  1.020  None  1.010~1.025  False    尿沉渣镜检  尿沉渣镜检  :  None  None  False    红细胞  红细胞  0  个/ul  0~5  False    白细胞  白细胞  +++/HP  /HP  ≤5/HP  True    白细胞  白细胞  218  个/ul  0~7  True    红细胞  红细胞  未查见  /HP  ≤3/HP  False   
---
   凝血酶原时间  PT  11.0  s  9.4~12.5  False    国际标准化比例  INR  0.98  INR  0.8~1.2  False    凝血酶原活动度  HDD  103.00  %  70~130  False    部分凝血活酶时间(胶质硅)  APTT  33.7  s  25.1~36.5  False    纤维蛋白原  Fib  2.65  g/L  2.00~4.00  False    凝血酶时间  TT  15.1  s  10.3~16.6  False   
---
   白细胞数目  WBC  4.20  10^9/L  3.5~9.5  False    淋巴细胞百分比  Lym%  28.6  %  20~50  False    单核细胞百分比  Mon%  5.0  %  3~10  False    中性粒细胞百分比  Neu%  64.5  %  40~75  False    嗜酸性细胞百分比  Eos%  1.7  %  0.4~8  False    嗜碱性细胞百分比  Bas%  0.2  %  0.0~1.0  False    淋巴细胞数目  Lym#  1.20  10^9/L  1.1~3.2  False    单核细胞数目  Mon#  0.21  10^9/L  0.1~0.6  False    中性粒细胞数目  Neu#  2.71  10^9/L  1.8~6.3  False    嗜酸性细胞数目  Eos#  0.07  10^9/L  0.02~0.52  False    嗜碱性细胞数目  Bas#  0.01  10^9/L  0.00~0.06  False    红细胞数目  RBC  4.71  10^12/L  3.8~5.1  False    血红蛋白  HGB  120  g/L  115~150  False    红细胞压积  HCT  38.3  None  None  False    平均红细胞体积  MCV  81.3  None  None  False    平均红细胞血红蛋白含量  MCH  25.6  None  None  False    平均红细胞血红蛋白浓度  MCHC  313  None  None  False    红细胞分布宽度变异系数  RDW-CV  14.9  None  None  False    红细胞分布宽度标准差  RDW-SD  43.2  None  None  False    血小板数目  PLT  288  None  None  False    平均血小板体积  MPV  9.0  None  None  False    血小板分布宽度  PDW  15.6  None  None  False    血小板压积  PCT  0.258  None  None  False    大型血小板比率  P-LCR  19.3  None  None  False    未成熟粒细胞百分比  IG%  0.1  None  None  False    未成熟粒细胞计数  IG#  0.00  None  None  False   
---
   总胆红素  TBIL  8.7  µmol/L  0.0~21.0  False    直接胆红素  DBIL  3.5  µmol/L  0.0~8.0  False    间接胆红素  IBIL  5.2  µmol/L  0.0~13.0  False    谷丙转氨酶  ALT  7.0  U/L  7~40  False    谷草转氨酶  AST  15  U/L  13~35  False    谷草/谷丙  AST/ALT  2.14  None  None  False    氯  Cl  105  None  None  False    钙  Ca  2.38  None  None  False    二氧化碳结合力  CO2cp  27.6  None  None  False    谷草转氨酶线粒体同工酶  m-AST  2.0  None  None  False   
---
   颜色  None  黄色  None  黄、淡黄  False    尿比重  SG  1.020  None  1.003~  False    浊度  None  清亮  None  清  False    维生素C  VC  0.0  mmol/l  -  False    葡萄糖  GLU  -  None  -  False    白细胞  WBC  28.00  个/ul  0~28  False    尿潜血  NQX  -  mg/l  -  False    红细胞  RBC  6.00  个/ul  0~17  False    白细胞  LEU  -  None  -  False    粘液丝  None  11  个/ul  0~28  False    尿蛋白  PRO  -  None  -  False    结晶  None  0.0  个/ul  0~28  False    亚硝酸盐  NIT  +  None  -  True    管型  None  0  个/ul  0~2  False    尿胆原  URO  -  None  -  False    上皮细胞  EC  39.00  /ul  0~34  True    胆红素  BIL  -  None  -  False    细菌  BACT  163.00  /ul  0~7  True    尿酮体  KET  -  None  -  False    真菌  BYST  0  /ul  0~1  False    pH值  pH  6.0  None  4.5~8.0  False   
---
   游离三碘甲状腺原氨酸  FT3  3.11  pg/mL  2.14~4.21  False    游离甲状腺素  FR T4  0.76  ng/dL  0.61~1.12  False    超敏促甲状腺素  fTSH3  1.350  uIU/ml  0.560~5.910  False   
---
   乙肝表面抗原(酶免法)  HBsAg  阴性  s/co  阴性  False    丙肝抗体(酶免法)  抗-HCV  阴性  s/co  阴性  False    人免疫缺陷病毒抗体(酶免法)  抗-HIV  阴性  s/co  阴性  False    梅毒螺旋体抗体(酶免法)  TP-Ab  阴性  s/co  阴性  False   
---
门诊号.
姓名：
性别：女
年龄：39岁
民族：汉族
身份证
现住址：
就诊类型：初诊
就诊科室：普通儿科三组（门）
就诊日期：2023-08-14 15:29
联系电
主诉：咽峡炎购药
现病史：咽峡炎购药
既往史：平素体健，无肝炎、结核类传染病史
过敏史：无
体格检查：发育正常，营养良好，精神一般，口唇红润，双侧扁桃体无肿大，无充血、分泌物。咽腔黏膜无充
血、红肿、疱疹，双肺呼吸音清，听诊心律齐，无杂音，腹平软，无压痛、反跳痛
辅助检查：
初步印象：急性咽峡炎
处理意见：门诊
备注：
医师签名：谭真真
第1页
---
门诊病历
门诊号：
姓名
性别：女
年龄：39岁
民族：汉族
身份证号
现住址：
就诊类型：急诊
就诊科室：妇科一病区(门)
就诊日期：2024-01-05 10:32
联系电话
主诉：下腹痛2小时
现病史：患者月经第二天，无明显诱因出现下腹持续疼痛
既往史：平素体健，无高血压、冠心病、糖尿病病史，无肝炎、结核等传染病史，无手术史
婚育史：
月经史：患者平素月经规律，量中等，色正常，无痛经。
过敏史：无
专科检查：外阴：发育正常，阴毛呈女性分布；阴道：通畅，粘膜红润，未见异常分泌物；宫颈：光滑，大小正常，宫体：正常大小，无压痛。附件：左侧附件区压痛明显。
辅助检查：
初步印象：女性盆腔炎性疾病
处理意见：门诊治疗
备注：
医师签名：汪会芳
第1页
---
门诊号:
姓名
性别: 女
年龄:40岁
民族: 汉族
身份证号
现住址:
就诊类型:初诊
就诊科室:妇科一病区(门)
就诊日期: 2024-04-08 09:44
联系电话
主诉: 月经期下腹间断疼痛2个月
现病史: 2024.1月经第3天左侧附件区疼痛,超声提示无异常,输消炎药后好转,2024.2无异常,2024.3月经
第3天下腹疼痛但是疼痛程度较前减轻,
既往史: 平素体健,无高血压、冠心病、糖尿病病史,无肝炎、结核等传染病史,无手术史
婚育史:
月经史: 患者平素月经规律,量中等,色正常,无痛经。
过敏史: 无
专科检查: 外阴:发育正常,阴毛呈女性分布;阴道:通畅,粘膜红润,未见异常分泌物;宫颈:光滑,大小
正常,宫体:正常大小,无压痛。附件:双侧附件区未触及明显异常。
辅助检查:
初步印象: 女性盆腔炎性疾病
处理意见: 门诊检查
备注:
医师签名: 权丽丽
第1页
2026-08-10 06:19:11,242 INFO     29 [EMBED-PIPELINE] batch[16:32] text_for_embed=门诊号
姓名
性别：女
年龄：40岁
民族：汉族
身份证号
现住址：
就诊类型：初诊
就诊科室：妇科门诊
就诊日期：2024-04-08 11:32
联系电话
主诉：月经期下腹间断疼痛2个月
现病史：2024.1月经第3天左侧附件区疼痛，超声提示无异常，输消炎药后好转，2024.2无异常，2024.3月经
第3天下腹疼痛但是疼痛程度较前减轻，
既往史：平素体健，无高血压、冠心病、糖尿病病史，无肝炎、结核等传染病史，无手术史
婚育史：
月经史：患者平素月经规律，量中等，色正常，无痛经。
过敏史：无
专科检查：外阴：发育正常，阴毛呈女性分布；阴道：通畅，粘膜红润，未见异常分泌物；宫颈：光滑，大小
正常，宫体：正常大小，无压痛。附件：双侧附件区未触及明显异常。
辅助检查：
初步印象：女性盆腔炎性疾病
处理意见：门诊检查
备注：
医师签名：
第1页
---
门诊号
姓
性别:女 年龄:40岁 民族:汉族
身份证号:
现住址:
就诊类型:急诊
就诊科室:普通儿科一组(门) 就诊日期:2024-04-19 08:07 联系电话:
主诉:因呼吸道感染)不适要求开药
现病史:患者因(呼吸道感染)不适,要求开药(家属代开)。
既往史:既往体质一般
过敏史:无
体格检查:神志清晰,精神一般,自主体位,查体合作
辅助检查:
初步印象:1、急性上呼吸道感染.2、维生素A缺乏伴夜盲症
处理意见:开立药品
备注:
医师签名:李婉莹
第1页
---
（总）诊病历
门诊号：
姓
性别：女
年龄：41岁
民族：汉族
婚姻状况：已婚
身份证
职业：专业技术人员
现住址：
就诊类型：初诊
就诊科室：呼吸危重二病区(门)
就诊日期：2025-04-11
14:47
联系电话：
主诉：咳嗽憋气一周
现病史：患者无发热，感冒后咳嗽、憋气一周，间断治疗，时轻时重，今日来诊
既往史：平素体健，无高血压、冠心病、糖尿病病史
个人史：无吸烟史
过敏史：无
体格检查：呼吸平稳，口唇无紫绀，听诊：双肺呼吸音清，未闻及干、湿性啰音
辅助检查：肺功能检查提示中重度阻塞性肺通气功能障碍，支气管舒张试验阳性。
初步印象：1、支气管哮喘(急性发作期).2、过敏性鼻炎[变应性鼻炎]
处理意见：坚持门诊治疗，定期复查
备注：
医师签名：段竹云
第1页
---
门诊病历
门诊号
姓名
性别: 女
年龄:41岁
民族: 汉族
婚姻状况: 已婚
身份证号
职业: 职员
现住址:
就诊类型: 初诊
就诊科室:耳鼻咽喉头颈外科
就诊日期: 2025-04-11 15:43
联系电
主诉:鼻塞流涕,咳嗽憋气1周
现病史:1周前发现鼻塞流涕,患者无发热,感冒后咳嗽、憋气,间断治疗,时轻时重,今日来诊
既往史:平素体健,无高血压、冠心病、糖尿病病史
家族史:无家族遗传病史
过敏史:无
体格检查:鼻腔粘膜充血,水肿,水样分泌物附着
辅助检查:肺功能检查提示中重度阻塞性肺通气功能障碍,支气管舒张试验阳性。
初步印象:1、支气管哮喘(急性发作期)2、过敏性鼻炎[变应性鼻炎]
处理意见:坚持门诊治疗,定期复查
备注:
医师签名:刘秀
第1页
---
门诊号:
11(急)诊病历
性别:女 年龄:41岁 民族:汉族
婚姻状况:已婚 身份证 业:专业技术人员
现住址:
就诊类型:复诊
就诊科室:呼吸危重二病区(门) 就诊日期:2025-05-09 17:00 联系电
主诉:咳嗽憋气一周
现病史:患者无发热,感冒后咳嗽、憋气一周,间断治疗,时轻时重,今日来诊
既往史:平素体健,无高血压、冠心病、糖尿病病史
个人史:无吸烟史
过敏史:无
体格检查:听诊:双肺呼吸音清,未闻及干、湿性啰音
辅助检查:肺功能检查提示中重度阻塞性肺通气功能障碍,支气管舒张试验阳性。
初步印象:1、支气管哮喘.2、过敏性鼻炎[变应性鼻炎]
处理意见:坚持门诊治疗,定期复查
备注:
医师签名:段竹云
第1页
---
门诊号:
姓名
性别: 女
年龄:41岁
民族: 汉族
婚姻状况: 小组
身份证号:
职业: 专业技术人员
现住址:
就诊类型:初诊
就诊科室:普通儿科三组(门)
就诊日期: 2025-06-23 10:49
联系电话
主诉: 呼吸道感染购药
现病史: 呼吸道感染购药
既往史: 平素体健, 无肝炎、结核类传染病史
过敏史: 无
体格检查: 发育正常, 营养良好, 精神一般, 口唇红润, 双侧扁桃体无肿大, 无充血、分泌物。咽腔黏膜有充
血, 无红肿、疱疹, 双肺呼吸音清, 听诊心律齐, 无杂音, 腹平软, 无压痛、反跳痛
辅助检查:
初步印象: 上呼吸道感染
处理意见: 门诊药物治疗
备注:
医师签名: 谭真真
第1页
---
门诊号
病历
姓名
性别:女
年龄:41岁
民族:汉族
婚姻状况:未婚
身份证
职业:专业技术人员
现住址:
就诊类型:初诊
就诊科室:普通儿科一组(门)
就诊日期:2025-07-1110:02
联系电话
主诉:呼吸道感染购药
现病史:呼吸道感染购药
既往史:平素体健,无肝炎、结核类传染病史
过敏史:无
体格检查:发育正常,营养良好,精神一般,口唇红润,双侧扁桃体无肿大,无充血、分泌物。咽腔黏膜无充
血、红肿、疱疹,双肺呼吸音清,听诊心律齐,无杂音,腹平软,无压痛、反跳痛
辅助检查:
初步印象:支气管炎
处理意见:门诊药物治疗
备注:
医师签名:赵艳
第1页
---
门诊病历
门诊
姓名:
性别：女
年龄:41岁
民族：汉族
婚姻状况：未婚
身份证
职业：职员
现住址：
就诊类型:初诊
就诊科室:普通儿科二区（门）
就诊日期：2025-09-18 15:22
联系电话
主诉：咽部疼痛伴眼部不适4天
现病史：4天前无明显诱因出现咽部疼痛，伴鼻塞，伴眼部不适，无发热、呕吐、腹泻、皮疹等不适。病后精神、食欲欠佳，大小便正常。
既往史：无特殊。
过敏史：无
体格检查：发育正常，营养良好，精神一般，呼吸平稳，双眼睑结膜充血，口唇红润，咽腔充血，无疱疹，双侧扁桃体I°，充血，无分泌物，双肺呼吸音清，未闻及干湿性啰音，听诊心律齐，无杂音，腹平软，无压痛、反跳痛，未触及包块，肠鸣音活跃，神经系统未见阳性体征。
辅助检查：无
初步印象：1.急性咽峡炎.2.急性变应性结膜炎
处理意见：门诊治疗，动态观察病情变化，不适及时随诊。
备注：
医师签名：赵艳
第1页
---
1.门诊病历
门诊
2026-01-15 呼吸危重三病区(门)
2026-01-06 妇科一病区(门)
2025-12-09 普通儿科二区(...
2025-12-07 普通儿科二区(...
2025-12-01 普通儿科二区(...
2025-11-27 普通儿科二区(...
2025-11-24 普通儿科二区(...
2025-09-18 普通儿科二区(...
2025-07-11 普通儿科一组(...
2025-06-23 普通儿科三组(...
2025-05-09 呼吸危重二病区(门)
姓名:
性别: 女
年龄:41岁
民族: 汉族
婚姻状况: 未...
身份证:
职业: 专业技术人员
现住址:
就诊类型:初诊
就诊科室:普通儿科二区(门)
就诊日期: 2025-12-01 15:28
联系电
主诉: 发热半天。
现病史: 半天前出现发热,最高体温38.0℃,口服药物治疗1次,无咳嗽,无喘息,无呼吸困难,无咯血,无腹泻、呕吐等。精神食欲一般,大小便正常。
既往史: 无。
过敏史: 无
体格检查: 神志清,精神一般,呼吸浅快,咽充血,扁桃体二度大,充血,无疱疹,无脓点,双肺呼吸音清,
心音有力,律齐,腹软。
辅助检查:
初步印象: 急性上呼吸道感染
处理意见: 口服药物,动态观察,不适随诊。
备注:
医师签名: 赵海国
第1页
---
姓名：
性别：女
年龄：41岁
民族：汉族
婚姻状况：已婚
身份证号
职业：专业技术人员
现住址
就诊类型：初诊
就诊科室：妇科一病区(门)
就诊日期：2026-01-06 08:36
联系电话.
主诉：左下腹间断疼痛1年左右来诊
现病史：患者诉于2024年01月05日无明显诱因出现下腹持续疼痛行相关检查后诊断为盆腔炎性疾病后遗症，
慢性盆腔痛，药物治疗后好转，慢性盆腔痛病程12月，目前疾病状态持续，未治疗。
既往史：2025年11月24日-2025年12月12日本院儿科门诊就诊代家属开药，否认3个月内其他病史及合并用药/
非药物治疗，现患者无盆腔炎性疾病急性发作，否认既往有子宫肌瘤、子宫内膜异位症、子宫腺肌病、结核性
盆腔炎、间质性膀胱炎、异常子宫出血、盆腔淤血综合征、子宫颈高级别上皮内病变等其他病症引起相关症状
者；未放置宫内节育器；无子宫及双侧附件缺如；近2周内未使用过本方案规定研究期间禁止使用的治疗（包括
药物和非药物治疗）；无控制不稳定的心血管、肝、肾和血液系统、糖尿病、甲状腺疾病等严重原发性疾病；
获得知情同意书前5年内未患有恶性肿瘤；否认对试验用药品过敏，包括对本品成分或者药物辅料有过敏史；否
认长期酗酒、药物滥用史；无智力障碍或精神障碍；近1个月内未参加过任何干预性临床试验；患者当前不在妊
娠期、哺乳期，同意在试验期间及试验结束后3个月内采取有效避孕措施。
婚育史：已婚已育，孕2产2，有性生活史
手术史：2016年8月31日、2020年7月9日因生产行剖宫产手术
月经史：初潮12岁，既往月经周期规律，经量中，色红，无痛经，末次月经2025.12.29-2025.1.2，周期26-
28天，经期5天，经量较前不变
过敏史：无
生命体征：2026.1.6测量身高：160.0cm 体重：51.0kg 体温：36.4℃ 脉搏：76次/分 呼吸：18次/分 血压：
98/76mmHg
体格检查：淋巴结、头颈部、胸部、脊柱/四肢/关节、神经系统未见异常，腹部异常（左下腹压痛，CS，研究
疾病相关），皮肤黏膜异常（腹部皮肤约5-6cm剖宫产手术瘢痕，NCS），其他未查。
专科检查：外阴已婚型，阴道畅，宫颈光滑，无摇举痛，有宫体压痛，无子宫活动受限或粘连固定，左侧附件
区、右侧附件区压痛，无宫骶韧带增粗、变硬、触痛。
辅助检查：今日按方案要求开具血常规、尿沉渣（含尿常规）、肝功八项、肾功两项、血妊娠、血沉、血清C -
125、妇科微生态、十二导联心电图、妇科阴道彩色B超检查，结果详见检查单。
初步印象：盆腔痛中医辨证：主症：下腹胀痛，腰骶部胀痛、带下量多；次症：神疲乏力、口苦口腻、小便
黄；舌象：舌质红、苔黄腻；脉象：脉弦滑；2026年01月06日由张丹丹医生辨证为湿热瘀阻症。 西医：盆腔炎
性疾病后遗症,慢性盆腔痛
处理意见：根据目前临床表现及患者情况，权丽丽医生于2026年01月06日08时38分在9号楼4楼医患沟通室向患
绍“妇科千金片治疗盆腔炎性疾病后遗症（湿热瘀阻证）的随机、双盲、安慰剂平行对照、多中心临
床试验”及知情同意书内容，已告知参加试验可能的风险与获益，患者已充分理解并同意参加该研究，未提出
门路 电 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 ��� 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七 七
既往史：2025年11月24日-2025年12月12日本院儿科门诊就诊代家属开药，否认3个月内其他病史及合并用药/非药物治疗，现患者无盆腔炎性疾病急性发作，否认既往有子宫肌瘤、子宫内膜异位症、子宫腺肌病、结核性盆腔炎、间质性膀胱炎、异常子宫出血、盆腔淤血综合征、子宫颈高级别上皮内病变等其他病症引起相关症状者；未放置宫内节育器；无子宫及双侧附件缺如；近2周内未使用过本方案规定研究期间禁止使用的治疗（包括药物和非药物治疗）；无控制不稳定的心血管、肝、肾和血液系统、糖尿病、甲状腺疾病等严重原发性疾病；获得知情同意书前5年内未患有恶性肿瘤；否认对试验用药品过敏，包括对本品成分或者药物辅料有过敏史；否认长期酗酒、药物滥用史；无智力障碍或精神障碍；近1个月内未参加过任何干预性临床试验；患者当前不在妊娠期、哺乳期，同意在试验期间及试验结束后3个月内采取有效避孕措施。
婚育史：已婚已育，孕2产2，有性生活史
手术史：2016年8月31日、2020年7月9日因生产行剖宫产手术
月经史：初潮12岁，既往月经周期规律，经量中，色红，无痛经，末次月经2025.12.29-2025.1.2，周期26-28天，经期5天，经量较前不变
过敏史：无
生命体征：2026.1.6测量身高：160.0cm 体重：51.0kg 体温：36.4℃ 脉搏：76次/分 呼吸：18次/分 血压：98/76mmHg
体格检查：淋巴结、头颈部、胸部、脊柱/四肢/关节、神经系统未见异常，腹部异常（左下腹压痛，CS，研究疾病相关），皮肤黏膜异常（腹部皮肤约5-6cm剖宫产手术瘢痕，NCS），其他未查。
专科检查：外阴已婚型，阴道畅，宫颈光滑，无摇举痛，有宫体压痛，无子宫活动受限或粘连固定，左侧附件区、右侧附件区压痛，无宫骶韧带增粗、变硬、触痛。
辅助检查：今日按方案要求开具血常规、尿沉渣（含尿常规）、肝功八项、肾功两项、血妊娠、血沉、血清CA-125、妇科微生态、十二导联心电图、妇科阴道彩色B超检查，结果详见检查单。
初步印象：盆腔痛中医辨证：主症：下腹胀痛，腰骶部胀痛、带下量多；次症：神疲乏力、口苦口腻、小便黄；舌象：舌质红、苔黄腻；脉象：脉弦滑；2026年01月06日由张丹丹医生辨证为湿热瘀阻症。 西医：盆腔炎性疾病后遗症，慢性盆腔痛
从细之间、根据目前临床表现及患者情况，权丽丽医生于2026年01月06日08时38分在9号楼4楼医患沟通室向患者“妇科千金片治疗盆腔炎性疾病后遗症（湿热瘀阻证）的随机、双盲、安慰剂平行对照、多中心临床试验”及知情同意书内容，已告知参加试验可能的风险与获益，患者已充分理解并同意参加该研究，未提出问题，患者本人于2026年01月06日08时58分签署知情同意书（版本号：V1.0 三门峡市中心医院专用版，版本日期：2025年08月05日），权丽丽医生于2026年01月06日08时59分签署知情同意书（版本号：V1.0 三门峡市中心医院专用版，版本日期：2025年08月05日），知情同意书原件一份保存于受试者文件夹，一份交给患者本人，确定患者筛选号为04011，进入试验筛选，根据方案要求，收集受试者的试验相关资料，并于今日开始进行筛选期相关检查。
1.已完成体征McCormack量表评分，总分8分，回顾近1周非经期腹痛/腰骶疼痛NRS平均分为5分。
2.嘱受试者合理饮食，避免过度劳累；避免盆浴和坐浴，避免穿紧身衣物和化纤内裤；注意经期卫生。
3.今日结合受试者情况，2026年1月6日血清CA-125示：59.70（0.00-35.00）U/mL，符合排除标准第（8）条，筛选失败，告知受试者转为门诊常规诊疗。
备注：
医师签名：
---
门诊
姓名
性别：女
年龄：41岁
民族：汉族
婚姻状况：已婚
身份证号
职业：其他
现住址
就诊类型：复诊
就诊科室：呼吸危重三病区(门)
就诊日期：2026-01-15
10:56
联系电话
主诉：咳嗽憋气一周
现病史：患者无发热，感冒后咳嗽、憋气一周，间断治疗，时轻时重，今日来诊
既往史：平素体健，无高血压、冠心病、糖尿病病史
个人史：无吸烟史
过敏史：无
体格检查：听诊：双肺呼吸音清，未闻及干、湿性啰音
辅助检查：肺功能检查提示中重度阻塞性肺通气功能障碍，支气管舒张试验阳性。
初步印象：1、支气管哮喘(急性发作期).2、过敏性鼻炎[变应性鼻炎]
处理意见：坚持门诊治疗，定期复查
备注
医师签名：王辉
第1页
---
请输入药品内容，按回车键检索
查询全部
类型 组 药品名称[规格] 用法 频率 实际用量 总量 开立时间 开立医师
药品 (320ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 320ug 1 2026-02-25 07:47:00 赵海国
药品 鼻渊通窍颗粒 口服 tid 1袋 3 2026-02-12 09:40:21 谭真真
药品 阿莫西林克拉维酸钾片(选) 口服(继续用药) tid 0.375g 24 2026-02-12 09:40:21 谭真真
药品 (160ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 160ug 1 2026-01-17 08:04:36 彭文娟
药品 (320ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 320ug 1 2026-01-17 08:04:36 彭文娟
药品 磷酸奥司他韦胶囊(东阳光) 口服 bid 75mg 10 2025-12-07 10:50:33 彭文娟
药品 鼻渊通窍颗粒 口服 bid 1袋 2 2025-11-27 15:02:43 烟海丽
药品 盐酸氮卓斯丁滴眼液 滴眼 qid 0.01ml 1 2025-09-18 15:29:34 赵艳
药品 阿莫西林克拉维酸钾片(选) 口服(继续用药) tid 0.375g 24 2025-09-18 15:25:48 赵艳
药品 (成人)双黄连口服液(选) 口服 tid 20ml 2 2025-09-18 15:25:48 赵艳
药品 (160ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 160ug 1 2025-07-11 10:07:36 赵艳
药品 (小儿)双黄连口服液(选) 口服 tid 20ml 2 2025-06-23 10:52:35 谭真真
药品 (倾尔宁片)孟鲁司特钠片(选) 口服 qn 10mg 30 2025-05-09 17:04:48 段竹云
共10页 2026-02-12 1 2 3 4 > 前往 1 页
50/patientsMainPage.html?parentPageJump=1 showTable=true#/patientView
984-04-02 首诊日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>
时间: 2026-02-12 11:40.02 接诊科室: 呼吸危重三病区(门) 接诊医生: 孙帅森
返回概览视图
集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告
请输入药品内容,按回车键检索
查询全部
类型 组 药品名称(规格) 用法 频率 实际用量 总量 开立时间 开立医师
药品 鼻渊通窍颗粒 口服 bid 1袋 2 2025-11-27 15:02.43 烟海丽
药品 盐酸氮卓斯丁滴眼液 滴眼 qid 0.01ml 1 2025-09-18 15:29.34 赵艳
药品 阿莫西林克拉维酸钾片(选) 口服(继续用药) tid 0.375g 24 2025-09-18 15:25.48 赵艳
药品 (成人)双黄连口服液(选) 口服 tid 20ml 2 2025-09-18 15:25.48 赵艳
药品 (160ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 160ug 1 2025-07-11 10:07.36 赵艳
药品 (小儿)双黄连口服液(选) 口服 tid 20ml 2 2025-06-23 10:52.35 谭真真
药品 (顺尔宁片)孟鲁司特钠片(选) 口服 qn 10mg 30 2025-05-09 17:04.48 段竹云
药品 (320ug)布地奈德福莫特罗粉吸入剂 吸入 bid 320ug 2 2025-05-09 17:04.48 段竹云
药品 酮酸泼尼松片 口服 qm 30mg 36 2025-04-11 15:46.53 刘秀层
药品 鼻酸莫米松鼻喷雾剂(选) 喷鼻 bid 100ug 1 2025-04-11 15:31.05 段竹云
药品 (顺尔宁片)孟鲁司特钠片(选) 口服 qn 10mg 5 2025-04-11 15:31.05 段竹云
药品 (320ug)布地奈德福莫特罗粉吸入剂 吸入 bid 320ug 1 2025-04-11 15:31.05 段竹云
药品 磷酸奥司他韦胶囊(东阳光) 口服 bid 75mg 10 2025-01-06 17:15.28 谭真真
药品 氯雷他定颗粒 口服 qd 10mg 1 2024-12-30 10:40:10 谭真真
共70条 20条/页 < 1 2 3 4 > 前往 1
/patientsMainPage.html?parentPageJump=1 showTable=true#/patientView
84-04-02
最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>
返回概览视图
门诊时间: 2026-02-12 11:40:02 接诊科室: 呼吸危重三病区(门) 接诊医生: 孙帅森
集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告
请输入药品内容, 按回车键检索
查询全部
类型 组 药品名称[规格] 用法 频率 实际用量 总量 开立时间 开立医师
药品 (大伊可新)维生素AD滴剂 口服 qd 2000u 3 2024-07-05 09:30:58 李婉莹
药品 (普米克令舒)吸入用布地奈德混悬液 压缩雾化吸入 tid 2ml 20 2024-07-05 09:30:58 李婉莹
药品 小儿豉翘清热颗粒 口服 tid 6g 3 2024-04-24 11:59:55 赵艳
药品 (成人)双黄连口服液(基选) 口服 tid 20ml 3 2024-04-19 08.14.06 李婉莹
药品 (强力)阿莫西林克拉维酸钾干混悬剂(选) 口服(继续用药) bid 0.457g 2 2024-04-19 08:14.06 李婉莹
药品 (大伊可新)维生素AD滴剂 口服 qd 2000u 3 2024-04-19 08:14.06 李婉莹
药品 (普米克令舒)吸入用布地奈德混悬液 压缩雾化吸入 tid 2ml 20 2024-04-19 08:14.06 李婉莹
药品 替硝唑氯化钠注射液 静滴 qd 200ml 6 2024-01-05 10:37.47 程会芳
药品 左氧氟沙星氯化钠注射液(选) 静滴 qd 0.5g 3 2024-01-05 10:37:47 程会芳
药品 蒲地蓝消炎口服液 口服 tid 10ml 2 2023-08-14 15:30:23 谭真真
药品 (盖克)小儿氨酚黄那敏颗粒 口服 tid 12g 2 2023-07-06 20:00:14 谭真真
药品 蒲地蓝消炎口服液 口服 tid 10ml 2 2023-07-06 20.00.14 谭真真
共70条 20条/页 < 1 2 3 4 > 前往 2 页
---
集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告
请输入药品内容,按回车键检索
查询全部
类型 组 药品名称[规格]
药品 替硝唑氯化钠注射液
药品 左氧氟沙星氯化钠注射液(选)
药品 蒲地蓝消炎口服液
药品 (盖克)小儿氨酚黄那敏颗粒
药品 蒲地蓝消炎口服液
药品 (小儿)双黄连口服液(选)
药品 地塞米松磷酸钠注射液(选)
药品 5ml灭菌注射用水
药品 (扑尔敏针)马来酸氯苯那敏注射液
药品 消旋山莨菪碱注射液
药品 头孢克肟颗粒(选)
药品 (天晴速畅)吸入用布地奈德混悬液(选)
药品 (大伊可新)维生素AD滴剂
用法 频率 实际用量 总量 开立时间 开立医师
入
静滴 qd 200ml 6 2024-01-05 10:37:47 程会芳
静滴 qd 0.5g 3 2024-01-05 10:37:47 程会芳
口服 tid 10ml 2 2023-08-14 15:30:23 谭真真
口服 tid 12g 2 2023-07-06 20:00:14 谭真真
口服 tid 10ml 2 2023-07-06 20:00:14 谭真真
口服 tid 20ml 2 2023-07-06 20:00:14 谭真真
外用 bid 10mg 2 2023-06-26 15:19:59 谭真真
外用 bid 5ml 4 2023-06-26 15:19:59 谭真真
外用 bid 20mg 2 2023-06-26 15:19:59 谭真真
外用 bid 20mg 2 2023-06-26 15:19:59 谭真真
口服 bid 100mg 30 2023-05-08 19:56:47 陈音
压缩雾化吸入 bid 2ml 10 2023-05-08 19:52:42 段艳霞
口服 qd 2000u 2 2023-05-08 19:52:42 段艳霞
共70条 20条/页 < 1 2 3 4 > 前往: 2 页
---
集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告
请输入药品内容,按回车键检索
查询全部
类型 组 药品名称|规格 用法 频率 实际用量 总量 开立时间 开立医师
药品 *乙2)(大伊可新)维生素AD滴剂 口服 qd 2000u 2 2023-04-07 16:29.03 陈音
药品 乙1)头孢克肟颗粒(选) 口服 bid 100mg 30 2023-04-07 16:28.02 陈音
药品 乙0)阿奇霉素干混悬剂 口服 qd 0.25g 1 2023-04-07 16:27:17 陈音
药品 乙2)三拗片 口服 tid 2片 1 2023-04-07 16:27:17 陈音
药品 乙0)富马酸酮替芬片 口服 bid 1mg 6 2023-04-07 16:27:17 陈音
药品 蒲地蓝消炎口服液 口服 tid 10ml 2 2022-08-08 15:40.53 王晶
药品 乙1)盐酸氨溴索口服溶液(基) 口服 bid 5ml 1 2022-05-09 19:49:32 赵海国
药品 赖氨肌醇维B12口服溶液 口服 bid 10ml 3 2022-05-09 19:49:32 赵海国
药品 乙0)5ml灭菌注射用水 外用 bid 20ml 4 2022-05-05 09:58:24 李凌蔚
药品 乙1)(扑尔敏针)马来酸氯苯那敏注射液 外用 bid 20mg 2 2022-05-05 09:58:24 李凌蔚
药品 甲)地塞米松磷酸钠注射液(基) 外用 bid 10mg 2 2022-05-05 09:58:24 李凌蔚
药品 乙1)消旋山莨菪碱注射液(基) 外用 bid 20mg 2 2022-05-05 09:58:24 李凌蔚
药品 赖氨肌醇维B12口服溶液 口服 bid 10ml 1 2022-05-05 09:57:04 李凌蔚
药品 乙1)复合维生素B片 口服 tid 1片 100 2022-05-05 09:56:29 李凌蔚
药品 用维生素004/基 口服 4 100 2022-05-05 09:56:29 李凌蔚
共70条 20条/页 < 1 2 3 4 > 前往 3 页
---
集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告
请输入药品内容，按回车键检索
查询全部
类型 组 药品名称/规格 用法 频率 实际用量 总量 开立时间 开立医师
药品 口服 bid 5ml 1 2022-05-09 19.49.32 赵海国
药品 乙1)盐酸氨溴索口服溶液(基) 口服 bid 10ml 3 2022-05-09 19.49.32 赵海国
药品 赖氨肌醇维B12口服溶液 口服 bid 20ml 4 2022-05-05 09.58.24 李凌蔚
药品 乙0)5ml灭菌注射用水 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚
药品 乙1)(扑尔敏针)马来酸氯苯那敏注射液 外用 bid 10mg 2 2022-05-05 09.58.24 李凌蔚
药品 甲)地塞米松磷酸钠注射液(基) 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚
药品 乙1)消旋山莨菪碱注射液(基) 外用 bid 10ml 1 2022-05-05 09.57.04 李凌蔚
药品 赖氨肌醇维B12口服溶液 口服 bid 1片 100 2022-05-05 09.56.29 李凌蔚
药品 乙1)复合维生素B片 口服 tid 5mg 100 2022-05-05 09.56.29 李凌蔚
药品 甲)维生素B2片(基) 口服 tid 50mg 2 2022-05-05 09.54.38 李凌蔚
药品 乙1)头孢克肟颗粒 口服 bid 10ml 1 2022-05-05 09.54.38 李凌蔚
药品 乙1)金振口服液(基) 口服 bid 3g 2 2022-04-19 16.05.18 陈媛
药品 (盖克)小儿氨酚黄那敏颗粒 口服 tid 4ml 1 2022-04-19 16.05.18 陈媛
药品 乙1)美敏伪麻口服溶液 口服 qid 5ml 1 2022-04-19 16.05.18 陈媛
共70条 20条/页 < 1 2 3 4 > 前往 3 页
---
集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告
请输入药品内容,按回车键检索
查询全部
类型 组 药品名称(规格)
药品 甲)(小儿)双黄连口服液(基)
药品 (盖克)小儿氨酚黄那敏颗粒
药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(基)
药品 蒲地蓝消炎口服液
药品 复方氨酚甲麻口服液
药品 (盖克)小儿氨酚黄那敏颗粒
药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(国基)
药品 乙0)(普米克令舒)吸入用布地奈德混悬液(国基)
药品 右旋糖酐铁颗粒
药品 盐酸氨卓斯丁滴眼液
用法 频率 实际用量 总量 开立时间 开立医师
口服 tid 10ml 1 2022-03-26 19:51:46 谭真真
口服 tid 6g 2 2022-03-26 19:51:18 谭真真
口服(继续 用药) bid 0.228g 2 2022-03-26 19:51:18 谭真真
口服 bid 10ml 1 2022-03-26 19:51:18 谭真真
口服 q6h 10ml 2 2021-11-04 17:18:07 宁秀琴
口服 tid 12g 2 2021-11-04 17:18:07 宁秀琴
口服(继续 用药) q12h 0.45g 2 2021-11-04 17:18:07 宁秀琴
压缩雾化 bid 2ml 5 2021-10-11 10:07:54 张冬梅
口服 tid 1袋 80 2021-09-28 15:12:34 党建华
滴双眼 bid 0.1ml 1 2021-09-09 15:18:56 史艳艳
共70条 20条/页 < 1 2 3 4 > 前往 4 页
2026-08-10 06:19:12,286 INFO     29 [EMBED-PIPELINE] batch[32:48] text_for_embed=处方笺
4970401
姓名：
性别：□男 □女 年龄：60岁
科别： 费别： 电话/住址：
过敏史：无 开具日期：2021年2月16日
临床诊断：支气管哮喘
Rp
孟鲁司特钠片 10mg 2板
用法：二天一次 1片
审核： 调配： 医师：
核对： 发药： 金额：
---
出院记录
姓名
科室：产科二区
床号.
住院号.
2020年07月12日
出院记录
患者.
36岁
住院号：
入院日期：2020-07-08 08:36:09
出院日期：2020年07月12日
住院天数：4天
入院情况：以“停经39周，要求住院待产”为主诉入院。入院查体：生命体征平稳，心肺
听诊未闻及异常。腹隆，晚孕腹型，肝脾肋下未触及。专科检查：宫高34CM，腹围102CM，估
计胎儿体宣：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水，骨盆外
测量及内诊：未做。辅助检查：B超（2020.07.02 本院）：晚孕宫内单活胎头位(双顶径
9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。
入院诊断：1.妊娠合并子宫瘢痕；2.孕产：宫内孕39周头位待产。
诊疗经过：患者入院后完善相关检查，要求剖宫产，于2020年07月09日 08：29-09：30在
腰硬联合麻醉+基础麻醉下行二次于宫下段剖宫产术+子宫修补术。取下腹原横切口，剔除原瘢
痕，逐层进腹，膀下指膀胱，暴露子宫下段，可见子宫下段肌层较薄，胎儿头发及胎脂漂浮，
切开子宫后见羊水清，约600ml，吸净后以头位助娩一活男婴，出生1-10分钟均评10分，胎盘
胎膜自娩完整，子宫收缩可，纱布球擦拭子宫腔，可见子宫下段肌层断裂，用可吸收线间断缝
合子宫下段肌层，断裂的立皆给予缝合，以伦桥可吸收线分两层连续缝合子宫切口。探查子宫
切口无活动性出血，双侧附件外观正常，关腹，术程顺利，术中出血不多，术后予以降压、抗
感染、加强宫缩支持及对症治疗。
出院诊断：1.妊娠合并子宫瘢痕；2.孕产：宫内孕39+周头位剖宫产：
出院情况：患者精神、饮食好，无特殊不适。查体：生命体征平稳，心肺听诊未闻及明显
异常，双乳泌乳量可，双乳稍涨，腹部平软，切口无红肿、渗出、硬结等愈合良好，子宫收缩
好，宫底约脐耻之间，宫体无压痛，恶露呈淡红色，量少，无异味。现患者一般情况好，双乳
泌乳量多，子宫复旧好，腹部切口愈合良好，无需拆线，达临床治愈，于今日出院。完成计划
性剖宫产临床路径。
出院医嘱：1.注意休息，合理营养；
2.禁性生活、盆浴及重体力劳动2个月；
3.坚持纯母乳喂养大于4-6月；
第 页
总第 页
医院
出院记录
姓名：
科室：产科二区
床号：
住院号：2
4.产后42天门诊复查，如出院后出现任何异常情况请立即就诊，注意产妇心理
状态，必要时心理咨询门诊就诊；若阴道出血淋漓不尽持续1月或阴道出血量多于平素月经
量、腹痛、发热等，及时就诊：（每周二、周六门诊326彭琼玉副主任医师坐诊）
5.严格避孕，术后六个月可安环避孕，术后2年以上方可再次妊娠：
6.新生儿乙肝疫苗第一针，卡介苗已接种，新生儿生后10天补充维生素AD滴剂
1粒/次，一次/日（至2岁），出院后新生儿每日测胆红素值，黄疸加重或持续14天未消退，或
出院后有不适，可直接到1号楼9楼新生儿科探视大厅就诊（携带宝宝就诊卡）；
7.咨询电话产科：
，新生儿科：0398-3118382。母乳咨询电话：
0398-3118618.
主治医师：
孙州
---
院
入院记录
姓名：
科室：产科二区
床号：
科室：产科二区
第(1)次入院记录
过敏史：无
姓名：
性别：女
年龄：36岁
身份证号
职业：
婚姻：已婚
民族：汉族
出生地：
现住址：
入院日期：2020-07-08 08:36:09
邮编
病史采集时间：2020-07-08 08:36:09
联系人：
与病人关系：夫妻
病史叙述者：本人
联系人地址：同上地址
电话.
可靠程度：可靠
主诉：停经39周，要求住院待产。
现病史：平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日（阳历），预产
期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单活胎，发育符合
孕周。孕早期无早孕反应，孕早期无腹痛、出立，阴道流液，出血史，无放射线、有害物质接
触史。孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正常，孕中期行无创DNA
结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正常，未行糖耐量筛
查，未查B族链球菌。孕期经过顺利，孕晚期无头痛、头晕、眼花等症状，无皮肤黄染及痰
痒。现停经39周，无腹痛，未见红及破水，遂入院要求住院待产，门诊以“足月妊娠、瘢痕子
宫”收住院。自孕以来精神好，饮食、睡眠好，大小便正常，体重增加约10KG。
既往史：患者平素体健；否认有“心脏病、高血压、糖尿病、肾病”等慢性病史，否认有
“肝炎、结核”等传染性疾病。于2016.08行剖宫产手术，否认余手术及外伤史。否认有输血
史，有献血史，否认食物及药物过敏史。预防接种随社会进行。
个人史：出生于原籍，护士，本科文化，工作于三门峡市中心医院。否认长期外地居住
史，无疫区居住史，无烟酒等不良嗜好。生长环境一般，否认有冶游史。
婚育史：31岁结婚，爱人
现年37岁，职员，工作于三门峡市党校，身体健康，无吸
烟史，有饮酒史，否认“肝炎、结核”病史，夫妻感情好。孕;产;，2016年足月剖宫产1活男
婴，现体健，否认产后出血及产褥感染史，否认不良孕产史。
月经史：平素月经规律，12岁，5-7天/30-35天，末次月经为：2019年10月08日（阳
历），量中等，色暗红，偶有血块，无痛经。
页
书写者签名：
总第 页
院
入院记录
姓名:
科室:产科二区
床号:
生.
家族史:父母亲体健,1弟1妹均体健,1子体健,否认家族中有遗传性及传染性疾病史。
体格检查
体温:36.5℃
脉搏:78次/分
呼吸:18次/分
血压:98/64mmHg
身高160cm
体重:60Kg
一般状况:发育正常;营养中等;自动体位:面色红润;面容及表情自如;神志清晰;言
语状态流利;检查时能合作等。
皮肤:色泽正常,弹性正常,无水肿、出汗、紫癜、皮疹、色素沉着、蜘蛛痣、瘢痕、创
伤、溃疡、结节。
淋巴结:全身或局部表浅淋巴结未触及肿大;局部皮肤无红热、瘘管、瘢痕。
头部:
头颅:大小无异常、外形无异常;眉发分布正常;无疖、痈、外伤、瘢痕、肿块。
眼部:双眼裂正常,双眼睑无水肿,眼球运动正常。瞳孔:左3.0mm直接对光反应灵敏,
间接对光反应灵敏;右3.0mm直接对光反应灵敏,间接对光反应灵敏。视力粗测正常。
耳部:耳廓无畸形,外耳道无分泌物,乳突无压痛,听力粗测5米。
鼻部:无畸形、鼻翼扇动、阻塞、分泌物、鼻中隔异常、嗅觉障碍、鼻窦压痛等。
口腔:口唇红润,无畸形、疱疹、微血管搏动、口角皲裂;牙齿无缺损、龋病、镶补等异
常;牙龈无溢血、溢脓、萎缩、色素沉着;口腔粘膜无溃疡、假膜、色素沉着;扁桃体无肿
大、分泌物;咽部无充血、分泌物。
颈部:对称,无强直、压痛、运动受限、颈静脉怒张、颈动脉明显搏动、肿块,气管居
中,甲状腺无肿大。
胸部
胸廓:形状正常,对称,运动程度正常,肋间正常,胸壁无水肿、皮下气肿、肿块、静脉
曲张,肋骨及肋软骨无压痛、凹陷等异常。乳头,正常。
肺脏:视诊:腹式呼吸,呼吸节律正常,呼吸深度正常,两侧呼吸运动对称。
触诊:语音震颤两侧相等,无摩擦感。
叩诊:叩诊声响清音,肺下界肩胛线在第10肋间,呼吸移动度6cm,
听诊:呼吸音性质为肺泡呼吸音,强度正常,语音传导正常,无摩擦音、哮鸣音、
第页
书写者签名:
总第页
院
入院记录
姓名：
科室：产科二区
床号
病号：
干啰音、湿啰音。
心脏：视诊：心尖搏动的位置在左侧锁骨中线内第4肋间，范围为2.5cm，强度正常，心前
区无异常搏动、局限性膨隆。
触诊：心尖搏动最强部位在左侧锁骨中线第4肋间，范围为2.5cm，无抬举性搏动、
震颤、摩擦感。
叩诊：左右心界线以每肋间距胸骨中线的cm数记载。
右cm
肋间
左cm
2
Ⅱ
2.5
2
Ⅲ
4
3
Ⅳ
5.5
Ⅴ
8
左锁骨中线至前正中线的距离9cm。
听诊：心率78次/分，心律整齐，无心脏杂音，无第三心音、第四心音、心音分
裂，P2<A2。
血管：桡动脉搏动正常，血管壁硬度正常。
周围血管征：无毛细血管搏动征、水冲脉、枪击音、动脉异常搏动。
腹部：
视诊：腹部膨隆，晓孕腹型，腹壁对称，无凹陷、膨隆、静脉曲张、蠕动波、局限性隆
起，下腹可见一长约15cm横行手术疤痕。
触诊：腹壁柔软，无压痛，无反跳痛；未触及肿块，无搏动、波动感等。肝脏：肋缘下未
触及，无压痛。胆囊：未触及，无压痛。脾脏：肋缘下未触及。肾：未触及，无压痛等。
叩诊：肝上界位于第5肋间，肝浊音界正常，肝区无叩击痛、脾区无叩击痛、腹部无过度
鼓音，移动性浊音阴性。
听诊：肠蠕动音正常，频率4次/分，胃区无振水声，肝区无摩擦音、脾区无摩擦音，无血
管杂音。
外阴及肛门：阴毛分布正常；外生殖器发育正常，肛门检查：无外痔、肛裂、肛瘘、脱
肛、湿疣等。
脊柱：脊柱无畸形、压痛、叩击痛；脊柱两侧肌肉无紧张、压痛；肋脊角无压痛、叩痛。
四肢：无畸形、杵状指（趾）、静脉曲张、外伤、骨折；肌肉张力正常与肌力5级，无萎
院
入院记录
姓名.
科室:产科二区
床号
住院号.
缩;关节无红肿、畸形、运动障碍,双下肢水肿。
神经反射:膝腱反射正常、跟腱反射正常、肱二头肌腱反射正常、肱三头肌腱反射正常、
腹壁反射正常、巴彬斯基征阴性、克尼格征阴性等。
专科情况
宫高34CM,腹围102CM,估计胎儿体重:3200g,胎位:头位,胎心152次/分,律齐,无
宫缩,未见红,未破水,骨盆外测量及内诊:未做。
辅助检查
B超(2020.07.02 本院):晓孕宫内单活胎头位(双顶径9.4cm,股骨长7.0cm羊水指
数8.5cm),胎盘成熟度II°.
初步诊断:
1.妊娠合并子宫瘢痕;
3.孕2产,宫内孕39周头位待产。
主治医师:
孙小丹
副主任医师:
彭琼玉
2020.07.08
---
呼出气一氧化氮测定报告单
病人信息：
编号：482
姓名：
年龄：41岁9月27天
性别：女
科室：普通儿科一区
出生日期：1984-04-02
测定时间：2026/1/29 11:02:42
测定信息：
一小时内禁止饮食：■是
一小时内禁止剧烈运动：■是
三小时内禁止食用特殊食品*：■是
一小时内禁止抽烟：■是
三天内使用激素类药物：■是 □否
三天内使用抗生素：□是 ■否
症状：□咳嗽 □喘息 □鼻塞 □喷嚏 ■其他
病史：□过敏史 □其它
*是指西兰花、芥蓝、生菜、莴苣、芹菜、水萝卜、熏制、腌制类食品。
测定项目：
呼气方式：■在线 □离线 □潮气
呼气温度：20.1℃
呼气压力：13.6cmH20
呼气平均流速：48ml/s
呼气NO浓度：
32.7,31.0,32.0,31.8,32.1,31.7ppb
呼气NO浓度均值:32ppb
呼气方式：■在线 □离线 □潮气
呼气温度：20.3℃
呼气压力：7.9cmH20
呼气平均流速：207ml/s
呼气NO浓度：
11.7,11.9,11.3,11.6,11.6,11.6ppb
呼气NO浓度均值:12ppb
测定结果：
FeNO50：32ppb
FeNO200：12ppb
CaNO：3.6ppb
测定意义：
测定浓度
参考值
炎症鉴别诊断
>12岁
≤12岁
FeNO50
<25ppb
<20ppb*
非嗜酸性气道炎症
25-50ppb
20-35ppb*
混合型气道炎症
≥50ppb
≥35ppb*
嗜酸性气道炎症
FeNO200
>10ppb
>8ppb
小气道炎症
CaNO
>5ppb
>3ppb
肺泡炎症
(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)
复查时间：
操作员：赵彩红
医生：马春英
电
告
单
更
---
肺功能检查报告单
姓名：
测试号：
住院号：
身高：
160 cm
年龄：
41 岁
体重：
48 kg
性别：
女
身份证号：
科别：
联系电话：
预计值
Bst % (Bst/
A1
A2
A3
FVC
[L]
3.13
3.15
100.54
3.15
3.08
3.07
FEV 1
[L]
2.70
1.99
73.90
1.99
1.85
1.96
FEV6
[L]
3.13
3.13
3.05
FEV 1 % FVC
[%]
83.98
63.25
75.31
63.25
60.02
63.82
FEV 1 % VC MAX
[%]
81.31
63.25
77.78
63.25
58.74
62.12
FIF 50
[L/s]
5.84
5.77
5.84
5.48
FEV3 % FVC
[%]
89.30
89.30
87.11
88.97
VC MAX
[L]
3.19
3.15
98.65
2.99
PEF
[L/s]
6.46
6.33
97.97
6.33
5.90
5.95
MMEF 75/25
[L/s]
3.53
1.06
30.03
1.06
0.89
0.99
MEF 25
[L/s]
1.77
0.46
26.28
0.46
0.38
0.40
MEF 50
[L/s]
4.06
1.25
30.90
1.25
1.13
1.24
MEF 75
[L/s]
5.73
3.01
52.56
3.01
2.22
2.68
V backextrapolation [B]
0.06
0.06
0.05
0.06
V backextrapol. % FVC
1.86
1.86
1.52
1.82
FET
[s]
8.73
8.73
5.99
6.71
FEF 200-1200
[L/s]
3.07
3.07
2.51
2.98
FVC IN
[L]
3.19
2.99
93.64
2.26
2.99
2.94
FIV1
[L]
2.96
2.24
2.96
2.92
FIV1 % FVC
[%]
99.14
99.32
99.14
99.48
FEF50 % FIF50
[%]
21.46
21.72
19.34
22.60
PIF
[L/s]
6.10
5.87
6.10
5.50
MVV
[L/min]
101.9
91.45
89.73
91.45
BF MVV
[1/min]
75.65
75.65
10
Flow [L/s]
F/V ex
Vol [L]
Vol%VCmax
Vol [L]
Time [s]
Vol [L]
Time [s]
意见：
1.轻度阻塞性通气功能障碍。
检查质量：FVC：A级。 FEV1：A级。
备注：受检者检查配合佳。结果仅供参考，请结合临床分析。
2.最大自主分钟通气量（MVV）在正常范围。
备注：患者MVV配合佳。结果仅供参考，请结合临床分析。
审核医生：孙帅森
检测技师：韦龙华
2026/1/15
---
肺功能报告单
姓名：
出生日期：
住院号：
身高：160 cm
身份证号：
性别：女
年龄：41岁
测试号：
体重：48 kg
预计
实1 %(实1/预)
实2 %(实2/预)
变异率
测试日期
26/1/15
26/1/15
测试时间
9:51:00上午
10:14:56上午
FVC
[L]
3.13
3.15
100.5
3.25
103.9
3.3
FEV 1
[L]
2.70
1.99
73.9
2.26
83.8
13.4
FEV 1 % FVC
[%]
83.98
63.25
75.3
69.40
82.6
9.7
FEV 1 % VC MAX
[%]
81.31
63.25
77.8
69.40
85.4
9.7
PEF
[L/s]
6.46
6.33
98.0
7.25
112.2
14.5
MEF 75
[L/s]
5.73
3.01
52.6
3.73
65.1
23.8
MEF 50
[L/s]
4.06
1.25
30.9
1.67
41.2
33.3
MEF 25
[L/s]
1.77
0.46
26.3
0.59
33.6
27.7
MMEF 75/25
[L/s]
3.53
1.06
30.0
1.46
41.3
37.6
FET
[s]
8.73
4.94
-43.4
V backextrapolation ex [L]
0.06
0.07
20.1
V backextrapol. % FVC [%]
1.86
2.17
16.3
Flow [L/s]
F/V ex
10
5
0
1
2
3
4
5
6
7
10
F/V In
医生意见：
支气管舒张试验阳性。
(通过储雾罐吸入硫酸沙丁胺醇气雾剂400ug20分钟后。
FEV1较基线增加大于12 %，且绝对值增加大于200 ml。
审核医生：孙帅森
检测技师：朱龙华
---
肺功能报告单
姓名：
出生日期：1984/4/02
门诊/住院/体检：
身高：160 cm
身份证号：
性别：女
年龄：41 岁
测试号：
体重：50 kg
测试日期
测试时间
预计
实测 % (实/预)
25/4/11
14:56:4
VT
[L]
0.36
0.41
114.9
BF
[1/min]
20.00
20.79
104.0
MV
[L/min]
7.14
8.54
119.5
ERV
[L]
1.07
1.07
99.4
VC MAX
[L]
3.19
2.84
88.9
FVC
[L]
3.13
2.84
90.6
FEV 1
[L]
2.70
1.53
56.9
FEV 1 % FVC
[%]
83.98
54.07
64.4
FEV 1 % VC MAX
[%]
81.31
54.07
66.5
PEF
[L/s]
6.46
4.56
70.7
MEF 75
[L/s]
5.73
1.84
32.1
MEF 50
[L/s]
4.06
0.84
20.7
MEF 25
[L/s]
1.77
0.28
15.6
MMEF 75/25
[L/s]
3.53
0.65
18.3
FET
[s]
8.46
V backextrapolation ex
[L]
0.03
V backextrapol. % FVC
[%]
1.23
MVV
[L/min]
101.93
75.75
74.3
FEV 1*30
[L/min]
101.93
46.03
45.2
RV-SB
[L]
1.55
2.56
164.9
RV%TLC-SB
[%]
32.90
47.52
144.4
TLC-SB
[L]
4.77
5.39
112.9
FRC-SB
[L]
2.63
3.31
126.0
FRC%TLC-SB
[%]
51.66
61.42
118.9
DLCOc SB
[mmol/min/kPa]
8.34
6.95
83.4
DLCO SB
[mmol/min/kPa]
8.34
6.95
83.4
医生意见：
1.中重度阻塞性通气功能障碍。
检查质量：FVC：A级 。 FEV1：A级 。
备注：受检者检查配合佳。 结果仅供参考，请结合临床分析。
2.最大自主分钟通气量（MVV）轻度下降。
备注：患者MVV配合佳。结果仅供参考，请结合临床分析。
3.弥散功能在正常范围。4.残总比中度增高。
审核医生：孙帅森
检测技师：张青苹
通气弥散B
2025/4/11 15:18
---
肺功能报告单
姓名：
性别：女
出生日期：1984/4/02
年龄：41岁
门诊/住院/体检：
测试号：
身高：160 cm
体重：50 kg
身份证号：
预计
实1 %(实1/预)
实2 %(实2/预)
变异率
测试日期
25/4/11
25/4/11
测试时间
14:56:47下午
15:14:32下午
FVC
[L]
3.13
2.84
90.6
3.05
97.4
7.5
FEV 1
[L]
2.70
1.53
56.9
1.91
71.0
24.7
FEV 1 % FVC
[%]
83.98
54.07
64.4
62.70
74.7
16.0
FEV 1 % VC MAX
[%]
81.31
54.07
66.5
62.70
77.1
16.0
PEF
[L/s]
6.46
4.56
70.7
5.64
87.3
23.6
MEF 75
[L/s]
5.73
1.84
32.1
2.65
46.3
44.3
MEF 50
[L/s]
4.06
0.84
20.7
1.23
30.4
47.0
MEF 25
[L/s]
1.77
0.28
15.6
0.44
25.0
60.2
MMEF 75/25
[L/s]
3.53
0.65
18.3
1.02
29.1
58.8
FET
[s]
8.46
6.41
-24.2
V backextrapolation ex [L]
0.03
0.06
71.7
V backextrapol. % FVC [%]
1.23
1.96
59.6
Flow [L/s]
F/V ex
10
5
0
1
2
3
4
5
6
7
10
5
F/V In
医生意见：
支气管舒张试验阳性。
（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后。
FEV1较基线增加大于12%，且绝对值增加大于200ml。）
审核医生：孙帅森
检测技师：张青苹
2026-08-10 06:19:12,829 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-10 06:19:12,829 INFO     29 [Trace] task=801b5176 | doc=DAXI-哮喘.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "40 items, types={'LabReport': 13, 'OutpatientRecord': 14, 'PrescriptionRecord': 6, 'DischargeRecord': 1, 'AdmissionRecord': 1, 'ExaminationReport': 5}", "name": "DAXI-哮喘.pdf", "embedding_token_consumption": 25890}
2026-08-10 06:19:12,829 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-10 06:19:14,128 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-10 06:19:14,129 INFO     29 [Trace] task=801b5176 | doc=DAXI-哮喘.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"partial\",\"synced_chunks\":39,\"skipped_hallucinated\":0,\"failed\":[{\"chunk_id\":\"e13bf3b136f8f3bc\",\"error\":\"(sqlalchemy.dialects.postgresql.asyncpg.Error) <class 'asyncpg.exceptions.StringDataRi...(965 chars)"}
2026-08-10 06:19:14,144 INFO     29 [DIAG-EXECUTOR] row_position_int len=26 row[0]=(39, 131, 220, 166, 178) row[-1]=(39, 425, 541, 438, 451)
2026-08-10 06:19:14,144 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(40, 158, 218, 124, 139) row[-1]=(40, 158, 218, 124, 139)
2026-08-10 06:19:14,144 INFO     29 [DIAG-EXECUTOR] row_position_int len=14 row[0]=(41, 91, 176, 183, 198) row[-1]=(41, 91, 149, 423, 438)
2026-08-10 06:19:14,144 INFO     29 [DIAG-EXECUTOR] row_position_int len=20 row[0]=(42, 59, 94, 195, 208) row[-1]=(42, 59, 129, 651, 665)
2026-08-10 06:19:14,145 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(43, 67, 202, 254, 287) row[-1]=(43, 67, 202, 254, 287)
2026-08-10 06:19:14,145 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(44, 159, 202, 125, 138) row[-1]=(44, 159, 202, 125, 138)
2026-08-10 06:19:14,145 INFO     29 [DIAG-EXECUTOR] row_position_int len=30 row[0]=(45, 106, 162, 174, 187) row[-1]=(45, 424, 501, 421, 434)
2026-08-10 06:19:14,145 INFO     29 [DIAG-EXECUTOR] row_position_int len=6 row[0]=(46, 78, 181, 187, 202) row[-1]=(46, 78, 168, 283, 298)
2026-08-10 06:19:14,145 INFO     29 [DIAG-EXECUTOR] row_position_int len=26 row[0]=(47, 121, 212, 163, 175) row[-1]=(47, 425, 545, 437, 449)
2026-08-10 06:19:14,145 INFO     29 [DIAG-EXECUTOR] row_position_int len=10 row[0]=(48, 106, 186, 189, 202) row[-1]=(48, 424, 554, 240, 267)
2026-08-10 06:19:14,145 INFO     29 [DIAG-EXECUTOR] row_position_int len=21 row[0]=(49, 48, 115, 203, 218) row[-1]=(49, 48, 111, 408, 424)
2026-08-10 06:19:14,145 INFO     29 [DIAG-EXECUTOR] row_position_int len=3 row[0]=(50, 65, 232, 197, 211) row[-1]=(50, 65, 206, 234, 248)
2026-08-10 06:19:14,145 INFO     29 [DIAG-EXECUTOR] row_position_int len=4 row[0]=(51, 12, 224, 221, 239) row[-1]=(51, 12, 237, 289, 307)
2026-08-10 06:19:14,145 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,145 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,145 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,145 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,146 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,146 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,146 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,146 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,146 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,146 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,146 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,146 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,146 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,146 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,147 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,147 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,147 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,147 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,147 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,147 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,147 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,147 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,147 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,148 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,148 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,148 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,148 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:14,154 INFO     29 set_progress(801b5176947e11f182aec5d26bc6c4ae), progress: 0.82, progress_msg: 06:19:14 [DOC Engine]:
Start to index...
2026-08-10 06:19:14,194 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.035s]
2026-08-10 06:19:14,199 INFO     29 set_progress(801b5176947e11f182aec5d26bc6c4ae), progress: 0.8025, progress_msg: 
2026-08-10 06:19:14,272 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.062s]
2026-08-10 06:19:14,325 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.041s]
2026-08-10 06:19:14,357 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.018s]
2026-08-10 06:19:14,391 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.023s]
2026-08-10 06:19:14,424 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.021s]
2026-08-10 06:19:14,459 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.027s]
2026-08-10 06:19:14,514 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.048s]
2026-08-10 06:19:14,574 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.044s]
2026-08-10 06:19:14,602 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.019s]
2026-08-10 06:19:14,618 INFO     29 set_progress(801b5176947e11f182aec5d26bc6c4ae), progress: 1.0, progress_msg: 06:19:14 Indexing done (0.46s). Task done (2104.83s)
2026-08-10 06:19:14,624 INFO     29 [Done], chunks(40), token(25890), elapsed:2104.83
2026-08-10 06:19:15,266 INFO     29 handle_task done for task {"id": "801b5176947e11f182aec5d26bc6c4ae", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786340646131, "task_type": "dataflow", "root_trace_id": "97b84aa3d1154f6db808c154432c5554", "root_traceparent": "00-97b84aa3d1154f6db808c154432c5554-dd9503e7c4e14a5d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 06:19:25,916 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:19:25,916 INFO     29 [qwen-vl-text] LLM output (len=1097):
{
  "exam_date": "2025-05-25",
  "report_date": "2025-05-27",
  "exam_name": "肺功能检查",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "男",
  "department": "呼吸内科",
  "bed_number": null,
  "findings": "常规通气\n预计值 实测值 实/预\nIRV [L] 1.14\nERV [L] 3.12\nIC [L] 0.61\nVT [L] 4.26 0.65 106.5\nVC IN [L] 4.26 3.01 70.7\nVC EX [L] 4.26 2.84 66.8\nBF [1/min] 20.00 17.72 88.6\nMV [L/min] 12.14 11.46 94.4\nVC MAX [L] 4.26 3.01 70.7\nFVC [L] 4.10 2.84 69.4\nFEV 1 [L] 3.22 2.51 78.0\nFEV 1 % FVC [%] 83.40 88.46 106.1\nFEV 1 % VC MAX [%] 76.23 83.54 109.6\nPEF [L/s] 8.21 6.40 77.9\nMEF 75 [L/s] 7.26 6.18 85.1\nMEF 50 [L/s] 4.35 3.04 69.9\nMEF 25 [L/s] 1.62 1.18 72.8\nMMEF 75/25 [L/s] . 3.45 2.26 65.4\nMVV [L/min] 119.91 77.46 64.6\nFEV 1*30 [L/min] 119.91 75.39 62.9\nVol [L]\nTLC 6\nFRC pleth\nRV 2\nPredA0.0 0.2 0.4 0.6 0.8 1.0\nTime [min]\nFlow [L/s]\nF/V ex\n10\n5\n0\n1\n2\n3\n4\n5\nF/V in\nVol [L]\n2\n1\n0\n1\n2\nTime [s]\n0 2 4 6 8 10 12",
  "conclusion": "测试结果：\n提示：\n1、轻度阻塞性肺通气功能障碍；\n2、肺储备功能下降。\n(请结合临床全面诊断)",
  "physician": "毛锦涛",
  "reviewer": null
}
2026-08-10 06:19:25,919 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=756233, prompt_len=1684
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共66行）
["郑州市第一人民医院", "肺功能检查报告", "常规通气", "姓名：", "性别：男", "年龄：61岁", "身高：174 cm", "科别：呼吸内科", "住院号：门诊", "测试号：2025052513", "体重：85 kg", "测试日期 25-5-25", "测试时间 11:46:55", "预计值 实测值 实/预", "IRV [L] 1.14", "ERV [L] 3.12", "IC [L] 0.61", "VT [L] 4.26 0.65 106.5", "VC IN [L] 4.26 3.01 70.7", "VC EX [L] 4.26 2.84 66.8", "BF [1/min] 20.00 17.72 88.6", "MV [L/min] 12.14 11.46 94.4", "VC MAX [L] 4.26 3.01 70.7", "FVC [L] 4.10 2.84 69.4", "FEV 1 [L] 3.22 2.51 78.0", "FEV 1 % FVC [%] 83.40 88.46 106.1", "FEV 1 % VC MAX [%] 76.23 83.54 109.6", "PEF [L/s] 8.21 6.40 77.9", "MEF 75 [L/s] 7.26 6.18 85.1", "MEF 50 [L/s] 4.35 3.04 69.9", "MEF 25 [L/s] 1.62 1.18 72.8", "MMEF 75/25 [L/s] . 3.45 2.26 65.4", "MVV [L/min] 119.91 77.46 64.6", "FEV 1*30 [L/min] 119.91 75.39 62.9", "Vol [L]", "TLC 6", "FRC pleth", "RV 2", "PredA0.0 0.2 0.4 0.6 0.8 1.0", "Time [min]", "Flow [L/s]", "F/V ex", "10", "5", "0", "1", "2", "3", "4", "5", "F/V in", "Vol [L]", "2", "1", "0", "1", "2", "Time [s]", "0 2 4 6 8 10 12", "测试结果：", "提示：", "1、轻度阻塞性肺通气功能障碍；", "2、肺储备功能下降。", "(请结合临床全面诊断)", "医生签字：毛锦涛", "报告日期：2025-5-27"]

## 定位规则
1. 对于列表中的每行文本，找到它在图片中**精确出现**的位置
2. bbox必须是该行文字的**最小紧密包围框**，紧贴文字边缘，不要包含额外的空白区域
3. 坐标归一化到0-1000，格式[x1,y1,x2,y2]
4. 如果某行文本在图片中未找到，跳过不输出
5. text字段必须与给定的文本完全一致

## 包围框精度要求
- x1必须紧贴该行第一个字符的左边缘
- x2必须紧贴该行最后一个字符的右边缘
- y1必须紧贴该行文字的顶部
- y2必须紧贴该行文字的底部
- 禁止将多行文字合并到同一个bbox中

## 严格JSON格式要求
直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。
正确示例：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230]},
  {"text": "年龄：68岁", "bbox": [100, 250, 270, 280]}
]
错误示例（禁止额外字段）：
[
  {"text": "性别：女", "bbox": [100, 200, 250, 230], "label": "个人信息"}
]
请直接输出纯JSON数组，不要用markdown代码块包裹。
2026-08-10 06:19:57,924 INFO     29 [qwen-vl-text] coord API raw response (len=5836):
[
	{"text": "郑州市第一人民医院", "bbox": [390, 28, 660, 48]},
	{"text": "肺功能检查报告", "bbox": [416, 55, 622, 75]},
	{"text": "常规通气", "bbox": [463, 79, 580, 101]},
	{"text": "姓名：", "bbox": [137, 112, 187, 125]},
	{"text": "性别：", "bbox": [137, 125, 187, 138]},
	{"text": "男", "bbox": [335, 127, 354, 138]},
	{"text": "年龄：", "bbox": [137, 138, 187, 150]},
	{"text": "61岁", "bbox": [335, 139, 384, 150]},
	{"text": "身高：", "bbox": [137, 150, 187, 162]},
	{"text": "174 cm", "bbox": [335, 151, 396, 162]},
	{"text": "科别：", "bbox": [528, 114, 577, 127]},
	{"text": "住院号：", "bbox": [528, 126, 593, 138]},
	{"text": "测试号：", "bbox": [528, 138, 593, 150]},
	{"text": "体重：", "bbox": [528, 150, 577, 162]},
	{"text": "呼吸内科", "bbox": [714, 114, 796, 126]},
	{"text": "门诊", "bbox": [714, 126, 755, 138]},
	{"text": "2025052513", "bbox": [714, 139, 816, 150]},
	{"text": "85 kg", "bbox": [714, 151, 766, 162]},
	{"text": "测试日期", "bbox": [77, 202, 161, 214], "bbox": [77, 202, 161, 214]},
	{"text": "测试时间", "bbox": [77, 214, 161, 227], "bbox": [77, 214, 161, 227]},
	{"text": "25-5-25", "bbox": [490, 202, 558, 214], "bbox": [490, 202, 558, 214]},
	{"text": "11:46:55", "bbox": [470, 214, 558, 227], "bbox": [470, 214, 558, 227]},
	{"text": "预计值 实测值 实/预", "bbox": [396, 187, 664, 200], "bbox": [396, 187, 664, 200]},
	{"text": "IRV [L] 1.14", "bbox": [77, 243, 458, 256], "bbox": [77, 243, 458, 256]},
	{"text": "ERV [L] 3.12", "bbox": [77, 256, 458, 269], "bbox": [77, 256, 458, 269]},
	{"text": "IC [L] 0.61", "bbox": [77, 269, 458, 282], "bbox": [77, 269, 458, 282]},
	{"text": "VT [L] 4.26 0.65 106.5", "bbox": [77, 282, 664, 295], "bbox": [77, 282, 664, 295]},
	{"text": "VC IN [L] 4.26 3.01 70.7", "bbox": [77, 295, 664, 308], "bbox": [77, 295, 664, 308]},
	{"text": "VC EX [L] 4.26 2.84 66.8", "bbox": [77, 308, 664, 321], "bbox": [77, 308, 664, 321]},
	{"text": "BF [1/min] 20.00 17.72 88.6", "bbox": [77, 321, 664, 334], "bbox": [77, 321, 664, 334]},
	{"text": "MV [L/min] 12.14 11.46 94.4", "bbox": [77, 334, 664, 347], "bbox": [77, 334, 664, 347]},
	{"text": "VC MAX [L] 4.26 3.01 70.7", "bbox": [77, 347, 664, 360], "bbox": [77, 347, 664, 360]},
	{"text": "FVC [L] 4.10 2.84 69.4", "bbox": [77, 369, 664, 382], "bbox": [77, 369, 664, 382]},
	{"text": "FEV 1 [L] 3.22 2.51 78.0", "bbox": [77, 382, 664, 395], "bbox": [77, 382, 664, 395]},
	{"text": "FEV 1 % FVC [%] 83.40 88.46 106.1", "bbox": [77, 395, 664, 408], "bbox": [77, 395, 664, 408]},
	{"text": "FEV 1 % VC MAX [%] 76.23 83.54 109.6", "bbox": [77, 408, 664, 421], "bbox": [77, 408, 664, 421]},
	{"text": "PEF [L/s] 8.21 6.40 77.9", "bbox": [77, 421, 664, 434], "bbox": [77, 421, 664, 434]},
	{"text": "MEF 75 [L/s] 7.26 6.18 85.1", "bbox": [77, 434, 664, 447], "bbox": [77, 434, 664, 447]},
	{"text": "MEF 50 [L/s] 4.35 3.04 69.9", "bbox": [77, 447, 664, 460], "bbox": [77, 447, 664, 460]},
	{"text": "MEF 25 [L/s] 1.62 1.18 72.8", "bbox": [77, 460, 664, 473], "bbox": [77, 460, 664, 473]},
	{"text": "MMEF 75/25 [L/s] . 3.45 2.26 65.4", "bbox": [77, 473, 664, 486], "bbox": [77, 473, 664, 486]},
	{"text": "MVV [L/min] 119.91 77.46 64.6", "bbox": [77, 499, 664, 512], "bbox": [77, 499, 664, 512]},
	{"text": "FEV 1*30 [L/min] 119.91 75.39 62.9", "bbox": [77, 512, 664, 525], "bbox": [77, 512, 664, 525]},
	{"text": "Vol [L]", "bbox": [723, 194, 762, 206], "bbox": [723, 194, 762, 206]},
	{"text": "TLC 6", "bbox": [678, 202, 717, 214], "bbox": [678, 202, 717, 214]},
	{"text": "FRC pleth", "bbox": [678, 255, 728, 267], "bbox": [678, 255, 728, 267]},
	{"text": "RV 2", "bbox": [678, 272, 717, 284], "bbox": [678, 272, 717, 284]},
	{"text": "PredA0.0 0.2 0.4 0.6 0.8 1.0", "bbox": [678, 312, 960, 324], "bbox": [678, 312, 960, 324]},
	{"text": "Time [min]", "bbox": [810, 295, 868, 305], "bbox": [810, 295, 868, 305]},
	{"text": "Flow [L/s]", "bbox": [708, 332, 764, 343], "bbox": [708, 332, 764, 343]},
	{"text": "F/V ex", "bbox": [853, 332, 888, 342], "bbox": [853, 332, 888, 342]},
	{"text": "10", "bbox": [687, 344, 702, 354], "bbox": [687, 344, 702, 354]},
	{"text": "5", "bbox": [693, 365, 702, 375], "bbox": [693, 365, 702, 375]},
	{"text": "0", "bbox": [693, 387, 702, 397], "bbox": [693, 387, 702, 397]},
	{"text": "1", "bbox": [744, 397, 753, 405], "bbox": [744, 397, 753, 405]},
	{"text": "2", "bbox": [785, 397, 794, 405], "bbox": [785, 397, 794, 405]},
	{"text": "3", "bbox": [826, 397, 835, 405], "bbox": [826, 397, 835, 405]},
	{"text": "4", "bbox": [867, 397, 875, 405], "bbox": [867, 397, 875, 405]},
	{"text": "5", "bbox": [907, 397, 915, 405], "bbox": [907, 397, 915, 405]},
	{"text": "F/V in", "bbox": [853, 440, 884, 450], "bbox": [853, 440, 884, 450]},
	{"text": "Vol [L]", "bbox": [708, 467, 745, 478], "bbox": [708, 467, 745, 478]},
	{"text": "2", "bbox": [693, 472, 702, 482], "bbox": [693, 472, 702, 482]},
	{"text": "1", "bbox": [693, 495, 702, 505], "bbox": [693, 495, 702, 505]},
	{"text": "0", "bbox": [693, 517, 702, 527], "bbox": [693, 517, 702, 527]},
	{"text": "1", "bbox": [693, 540, 702, 550], "bbox": [693, 540, 702, 550]},
	{"text": "2", "bbox": [693, 563, 702, 573], "bbox": [693, 563, 702, 573]},
	{"text": "Time [s]", "bbox": [810, 567, 854, 578], "bbox": [810, 567, 854, 578]},
	{"text": "0 2 4 6 8 10 12", "bbox": [705, 585, 940, 596], "bbox": [705, 585, 940, 596]},
	{"text": "测试结果：", "bbox": [66, 603, 170, 620], "bbox": [66, 603, 170, 620]},
	{"text": "提示：", "bbox": [77, 645, 134, 662], "bbox": [77, 645, 134, 662]},
	{"text": "1、轻度阻塞性肺通气功能障碍；", "bbox": [77, 662, 418, 678], "bbox": [77, 662, 418, 678]},
	{"text": "2、肺储备功能下降。", "bbox": [77, 678, 296, 694], "bbox": [77, 678, 296, 694]},
	{"text": "(请结合临床全面诊断)", "bbox": [112, 761, 405, 780], "bbox": [112, 761, 405, 780]},
	{"text": "医生签字：毛锦涛", "bbox": [552, 765, 914, 807], "bbox": [552, 765, 914, 807]},
	{"text": "报告日期：2025-5-27", "bbox": [654, 829, 896, 845], "bbox": [654, 829, 896, 845]}
]
2026-08-10 06:19:57,926 INFO     29 [qwen-vl-text] coord API: raw_items=75, valid_items=75, elapsed=32.0s
2026-08-10 06:19:57,927 INFO     29 [qwen-vl-text] coord item[0]: text=郑州市第一人民医院, bbox=[390, 28, 660, 48]
2026-08-10 06:19:57,927 INFO     29 [qwen-vl-text] coord item[1]: text=肺功能检查报告, bbox=[416, 55, 622, 75]
2026-08-10 06:19:57,927 INFO     29 [qwen-vl-text] coord item[2]: text=常规通气, bbox=[463, 79, 580, 101]
2026-08-10 06:19:57,927 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[137, 112, 187, 125]
2026-08-10 06:19:57,927 INFO     29 [qwen-vl-text] coord item[4]: text=性别：, bbox=[137, 125, 187, 138]
2026-08-10 06:19:57,927 INFO     29 [qwen-vl-text] coord item[5]: text=男, bbox=[335, 127, 354, 138]
2026-08-10 06:19:57,927 INFO     29 [qwen-vl-text] coord item[6]: text=年龄：, bbox=[137, 138, 187, 150]
2026-08-10 06:19:57,927 INFO     29 [qwen-vl-text] coord item[7]: text=61岁, bbox=[335, 139, 384, 150]
2026-08-10 06:19:57,927 INFO     29 [qwen-vl-text] coord item[8]: text=身高：, bbox=[137, 150, 187, 162]
2026-08-10 06:19:57,927 INFO     29 [qwen-vl-text] coord item[9]: text=174 cm, bbox=[335, 151, 396, 162]
2026-08-10 06:19:57,927 INFO     29 [qwen-vl-text] coord item[10]: text=科别：, bbox=[528, 114, 577, 127]
2026-08-10 06:19:57,927 INFO     29 [qwen-vl-text] coord item[11]: text=住院号：, bbox=[528, 126, 593, 138]
2026-08-10 06:19:57,927 INFO     29 [qwen-vl-text] coord item[12]: text=测试号：, bbox=[528, 138, 593, 150]
2026-08-10 06:19:57,927 INFO     29 [qwen-vl-text] coord item[13]: text=体重：, bbox=[528, 150, 577, 162]
2026-08-10 06:19:57,927 INFO     29 [qwen-vl-text] coord item[14]: text=呼吸内科, bbox=[714, 114, 796, 126]
2026-08-10 06:19:57,927 INFO     29 [qwen-vl-text] coord item[15]: text=门诊, bbox=[714, 126, 755, 138]
2026-08-10 06:19:57,928 INFO     29 [qwen-vl-text] coord item[16]: text=2025052513, bbox=[714, 139, 816, 150]
2026-08-10 06:19:57,928 INFO     29 [qwen-vl-text] coord item[17]: text=85 kg, bbox=[714, 151, 766, 162]
2026-08-10 06:19:57,928 INFO     29 [qwen-vl-text] coord item[18]: text=测试日期, bbox=[77, 202, 161, 214]
2026-08-10 06:19:57,928 INFO     29 [qwen-vl-text] coord item[19]: text=测试时间, bbox=[77, 214, 161, 227]
2026-08-10 06:19:57,928 INFO     29 [qwen-vl-text] coord item[20]: text=25-5-25, bbox=[490, 202, 558, 214]
2026-08-10 06:19:57,928 INFO     29 [qwen-vl-text] coord item[21]: text=11:46:55, bbox=[470, 214, 558, 227]
2026-08-10 06:19:57,928 INFO     29 [qwen-vl-text] coord item[22]: text=预计值 实测值 实/预, bbox=[396, 187, 664, 200]
2026-08-10 06:19:57,928 INFO     29 [qwen-vl-text] coord item[23]: text=IRV [L] 1.14, bbox=[77, 243, 458, 256]
2026-08-10 06:19:57,928 INFO     29 [qwen-vl-text] coord item[24]: text=ERV [L] 3.12, bbox=[77, 256, 458, 269]
2026-08-10 06:19:57,928 INFO     29 [qwen-vl-text] coord item[25]: text=IC [L] 0.61, bbox=[77, 269, 458, 282]
2026-08-10 06:19:57,928 INFO     29 [qwen-vl-text] coord item[26]: text=VT [L] 4.26 0.65 106.5, bbox=[77, 282, 664, 295]
2026-08-10 06:19:57,928 INFO     29 [qwen-vl-text] coord item[27]: text=VC IN [L] 4.26 3.01 70.7, bbox=[77, 295, 664, 308]
2026-08-10 06:19:57,928 INFO     29 [qwen-vl-text] coord item[28]: text=VC EX [L] 4.26 2.84 66.8, bbox=[77, 308, 664, 321]
2026-08-10 06:19:57,928 INFO     29 [qwen-vl-text] coord item[29]: text=BF [1/min] 20.00 17.72 88.6, bbox=[77, 321, 664, 334]
2026-08-10 06:19:57,928 INFO     29 [qwen-vl-text] coord item[30]: text=MV [L/min] 12.14 11.46 94.4, bbox=[77, 334, 664, 347]
2026-08-10 06:19:57,928 INFO     29 [qwen-vl-text] coord item[31]: text=VC MAX [L] 4.26 3.01 70.7, bbox=[77, 347, 664, 360]
2026-08-10 06:19:57,928 INFO     29 [qwen-vl-text] coord item[32]: text=FVC [L] 4.10 2.84 69.4, bbox=[77, 369, 664, 382]
2026-08-10 06:19:57,928 INFO     29 [qwen-vl-text] coord item[33]: text=FEV 1 [L] 3.22 2.51 78.0, bbox=[77, 382, 664, 395]
2026-08-10 06:19:57,929 INFO     29 [qwen-vl-text] coord item[34]: text=FEV 1 % FVC [%] 83.40 88.46 106.1, bbox=[77, 395, 664, 408]
2026-08-10 06:19:57,929 INFO     29 [qwen-vl-text] coord item[35]: text=FEV 1 % VC MAX [%] 76.23 83.54 109.6, bbox=[77, 408, 664, 421]
2026-08-10 06:19:57,929 INFO     29 [qwen-vl-text] coord item[36]: text=PEF [L/s] 8.21 6.40 77.9, bbox=[77, 421, 664, 434]
2026-08-10 06:19:57,929 INFO     29 [qwen-vl-text] coord item[37]: text=MEF 75 [L/s] 7.26 6.18 85.1, bbox=[77, 434, 664, 447]
2026-08-10 06:19:57,929 INFO     29 [qwen-vl-text] coord item[38]: text=MEF 50 [L/s] 4.35 3.04 69.9, bbox=[77, 447, 664, 460]
2026-08-10 06:19:57,929 INFO     29 [qwen-vl-text] coord item[39]: text=MEF 25 [L/s] 1.62 1.18 72.8, bbox=[77, 460, 664, 473]
2026-08-10 06:19:57,929 INFO     29 [qwen-vl-text] coord item[40]: text=MMEF 75/25 [L/s] . 3.45 2.26 65.4, bbox=[77, 473, 664, 486]
2026-08-10 06:19:57,929 INFO     29 [qwen-vl-text] coord item[41]: text=MVV [L/min] 119.91 77.46 64.6, bbox=[77, 499, 664, 512]
2026-08-10 06:19:57,929 INFO     29 [qwen-vl-text] coord item[42]: text=FEV 1*30 [L/min] 119.91 75.39 62.9, bbox=[77, 512, 664, 525]
2026-08-10 06:19:57,929 INFO     29 [qwen-vl-text] coord item[43]: text=Vol [L], bbox=[723, 194, 762, 206]
2026-08-10 06:19:57,929 INFO     29 [qwen-vl-text] coord item[44]: text=TLC 6, bbox=[678, 202, 717, 214]
2026-08-10 06:19:57,929 INFO     29 [qwen-vl-text] coord item[45]: text=FRC pleth, bbox=[678, 255, 728, 267]
2026-08-10 06:19:57,929 INFO     29 [qwen-vl-text] coord item[46]: text=RV 2, bbox=[678, 272, 717, 284]
2026-08-10 06:19:57,929 INFO     29 [qwen-vl-text] coord item[47]: text=PredA0.0 0.2 0.4 0.6 0.8 1.0, bbox=[678, 312, 960, 324]
2026-08-10 06:19:57,930 INFO     29 [qwen-vl-text] coord item[48]: text=Time [min], bbox=[810, 295, 868, 305]
2026-08-10 06:19:57,930 INFO     29 [qwen-vl-text] coord item[49]: text=Flow [L/s], bbox=[708, 332, 764, 343]
2026-08-10 06:19:57,930 INFO     29 [qwen-vl-text] coord item[50]: text=F/V ex, bbox=[853, 332, 888, 342]
2026-08-10 06:19:57,930 INFO     29 [qwen-vl-text] coord item[51]: text=10, bbox=[687, 344, 702, 354]
2026-08-10 06:19:57,930 INFO     29 [qwen-vl-text] coord item[52]: text=5, bbox=[693, 365, 702, 375]
2026-08-10 06:19:57,930 INFO     29 [qwen-vl-text] coord item[53]: text=0, bbox=[693, 387, 702, 397]
2026-08-10 06:19:57,930 INFO     29 [qwen-vl-text] coord item[54]: text=1, bbox=[744, 397, 753, 405]
2026-08-10 06:19:57,930 INFO     29 [qwen-vl-text] coord item[55]: text=2, bbox=[785, 397, 794, 405]
2026-08-10 06:19:57,930 INFO     29 [qwen-vl-text] coord item[56]: text=3, bbox=[826, 397, 835, 405]
2026-08-10 06:19:57,930 INFO     29 [qwen-vl-text] coord item[57]: text=4, bbox=[867, 397, 875, 405]
2026-08-10 06:19:57,931 INFO     29 [qwen-vl-text] coord item[58]: text=5, bbox=[907, 397, 915, 405]
2026-08-10 06:19:57,931 INFO     29 [qwen-vl-text] coord item[59]: text=F/V in, bbox=[853, 440, 884, 450]
2026-08-10 06:19:57,931 INFO     29 [qwen-vl-text] coord item[60]: text=Vol [L], bbox=[708, 467, 745, 478]
2026-08-10 06:19:57,931 INFO     29 [qwen-vl-text] coord item[61]: text=2, bbox=[693, 472, 702, 482]
2026-08-10 06:19:57,931 INFO     29 [qwen-vl-text] coord item[62]: text=1, bbox=[693, 495, 702, 505]
2026-08-10 06:19:57,931 INFO     29 [qwen-vl-text] coord item[63]: text=0, bbox=[693, 517, 702, 527]
2026-08-10 06:19:57,931 INFO     29 [qwen-vl-text] coord item[64]: text=1, bbox=[693, 540, 702, 550]
2026-08-10 06:19:57,931 INFO     29 [qwen-vl-text] coord item[65]: text=2, bbox=[693, 563, 702, 573]
2026-08-10 06:19:57,931 INFO     29 [qwen-vl-text] coord item[66]: text=Time [s], bbox=[810, 567, 854, 578]
2026-08-10 06:19:57,931 INFO     29 [qwen-vl-text] coord item[67]: text=0 2 4 6 8 10 12, bbox=[705, 585, 940, 596]
2026-08-10 06:19:57,931 INFO     29 [qwen-vl-text] coord item[68]: text=测试结果：, bbox=[66, 603, 170, 620]
2026-08-10 06:19:57,931 INFO     29 [qwen-vl-text] coord item[69]: text=提示：, bbox=[77, 645, 134, 662]
2026-08-10 06:19:57,932 INFO     29 [qwen-vl-text] coord item[70]: text=1、轻度阻塞性肺通气功能障碍；, bbox=[77, 662, 418, 678]
2026-08-10 06:19:57,932 INFO     29 [qwen-vl-text] coord item[71]: text=2、肺储备功能下降。, bbox=[77, 678, 296, 694]
2026-08-10 06:19:57,932 INFO     29 [qwen-vl-text] coord item[72]: text=(请结合临床全面诊断), bbox=[112, 761, 405, 780]
2026-08-10 06:19:57,932 INFO     29 [qwen-vl-text] coord item[73]: text=医生签字：毛锦涛, bbox=[552, 765, 914, 807]
2026-08-10 06:19:57,932 INFO     29 [qwen-vl-text] coord item[74]: text=报告日期：2025-5-27, bbox=[654, 829, 896, 845]
2026-08-10 06:19:57,932 INFO     29 [qwen-vl-text] page=2 — 66/66 coords, api_time=32.0s
2026-08-10 06:19:57,933 INFO     29 [qwen-vl-text] new_positions (66):
[[2, 232.04999999999998, 392.7, 23.576, 40.416], [2, 247.51999999999998, 370.09, 46.309999999999995, 63.15], [2, 275.485, 345.09999999999997, 66.518, 85.042], [2, 81.515, 111.265, 94.304, 105.25], [2, 81.515, 111.265, 105.25, 116.196], [2, 199.325, 210.63, 106.934, 116.196], [2, 81.515, 111.265, 116.196, 126.3], [2, 199.325, 228.48, 117.038, 126.3], [2, 81.515, 111.265, 126.3, 136.404], [2, 199.325, 235.61999999999998, 127.142, 136.404], [2, 314.15999999999997, 343.315, 95.988, 106.934], [2, 314.15999999999997, 352.835, 106.092, 116.196], [2, 314.15999999999997, 352.835, 116.196, 126.3], [2, 314.15999999999997, 343.315, 126.3, 136.404], [2, 424.83, 473.62, 95.988, 106.092], [2, 424.83, 449.22499999999997, 106.092, 116.196], [2, 424.83, 485.52, 117.038, 126.3], [2, 424.83, 455.77, 127.142, 136.404], [2, 45.815, 95.795, 170.084, 180.188], [2, 45.815, 95.795, 180.188, 191.134], [2, 291.55, 332.01, 170.084, 180.188], [2, 279.65, 332.01, 180.188, 191.134], [2, 235.61999999999998, 395.08, 157.454, 168.4], [2, 45.815, 272.51, 204.606, 215.552], [2, 45.815, 272.51, 215.552, 226.498], [2, 45.815, 272.51, 226.498, 237.444], [2, 45.815, 395.08, 237.444, 248.39], [2, 45.815, 395.08, 248.39, 259.336], [2, 45.815, 395.08, 259.336, 270.282], [2, 45.815, 395.08, 270.282, 281.228], [2, 45.815, 395.08, 281.228, 292.174], [2, 45.815, 395.08, 292.174, 303.12], [2, 45.815, 395.08, 310.698, 321.644], [2, 45.815, 395.08, 321.644, 332.59], [2, 45.815, 395.08, 332.59, 343.536], [2, 45.815, 395.08, 343.536, 354.48199999999997], [2, 45.815, 395.08, 354.48199999999997, 365.428], [2, 45.815, 395.08, 365.428, 376.37399999999997], [2, 45.815, 395.08, 376.37399999999997, 387.32], [2, 45.815, 395.08, 387.32, 398.26599999999996], [2, 45.815, 395.08, 398.26599999999996, 409.212], [2, 45.815, 395.08, 420.15799999999996, 431.104], [2, 45.815, 395.08, 431.104, 442.05], [2, 430.185, 453.39, 163.34799999999998, 173.452], [2, 403.40999999999997, 426.615, 170.084, 180.188], [2, 403.40999999999997, 433.15999999999997, 214.70999999999998, 224.814], [2, 403.40999999999997, 426.615, 229.024, 239.128], [2, 403.40999999999997, 571.1999999999999, 262.704, 272.808], [2, 481.95, 516.4599999999999, 248.39, 256.81], [2, 421.26, 454.58, 279.544, 288.806], [2, 507.53499999999997, 528.36, 279.544, 287.964], [2, 408.765, 417.69, 289.64799999999997, 298.068], [2, 412.335, 417.69, 307.33, 315.75], [2, 412.335, 417.69, 325.854, 334.274], [2, 442.68, 448.03499999999997, 334.274, 341.01], [2, 467.075, 472.43, 334.274, 341.01], [2, 491.46999999999997, 496.825, 334.274, 341.01], [2, 515.865, 520.625, 334.274, 341.01], [2, 539.665, 544.425, 334.274, 341.01], [2, 507.53499999999997, 525.98, 370.47999999999996, 378.9], [2, 421.26, 443.275, 393.214, 402.476], [2, 412.335, 417.69, 397.424, 405.844], [2, 412.335, 417.69, 416.78999999999996, 425.21], [2, 412.335, 417.69, 435.31399999999996, 443.734], [2, 412.335, 417.69, 454.68, 463.09999999999997], [2, 412.335, 417.69, 474.046, 482.466]]
2026-08-10 06:19:57,933 INFO     29 [qwen-vl-text] ═══ DONE ═══ 66 positions, pages=1, time=83.4s
2026-08-10 06:19:57,954 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 06:19:57,954 INFO     29 [Trace] task=dbae825c | doc=LGWE-艾特美哮喘-洛阳三.pdf | Extractor:ExaminationReport | outputs={"chunks": "2 items, types={'ExaminationReport': 2}", "html": "", "json": "163 items", "markdown": "", "text": "", "name": "LGWE-艾特美哮喘-洛阳三.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 2}"}
2026-08-10 06:19:57,954 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 06:19:57,955 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T06:19:57.954+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 3, "failed": 0, "current": {"dbae825c948211f1bd9827cf206dfa2d": {"id": "dbae825c948211f1bd9827cf206dfa2d", "doc_id": "db492056948211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LGWE-\u827e\u7279\u7f8e\u54ee\u5598-\u6d1b\u9633\u4e09.pdf", "type": "pdf", "location": "LGWE-\u827e\u7279\u7f8e\u54ee\u5598-\u6d1b\u9633\u4e09.pdf", "size": 1648931, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786342517754, "task_type": "dataflow", "root_trace_id": "aaa86c5dcc2c462f88c0ac982e1d484f", "root_traceparent": "00-aaa86c5dcc2c462f88c0ac982e1d484f-c2d6050d16147908-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 06:19:57,958 INFO     29 [ChunkMerger] Merged 3 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 2} (filtered 6 noise chunks)
2026-08-10 06:19:58,347 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-10 06:19:58,347 INFO     29 [Trace] task=dbae825c | doc=LGWE-艾特美哮喘-洛阳三.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "3 items, types={'OutpatientRecord': 1, 'ExaminationReport': 2}", "name": "LGWE-艾特美哮喘-洛阳三.pdf"}
2026-08-10 06:19:58,347 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 06:19:58,404 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786342752802, 'update_date': datetime.datetime(2026, 8, 10, 6, 19, 12), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 804182, 'status': '1'}
2026-08-10 06:19:58,611 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=郑州市第一人民医院门诊病历
科室：呼吸内科一门诊
就诊日期：2025-05-25
初诊
姓名：
性别：男
年龄：61岁
ID：
主 诉：咳嗽、胸闷3月
现 病 史：3月前出现咳嗽、胸闷，来诊
既 往 史：无高血压病、冠心病、糖尿病病史，无乙肝、肝炎病史。无
药物过敏史。
体格检查：神志清，双肺呼吸音粗，未闻及啰音；
处 理：完善肺功能
建 议：门诊口服药物治疗，如出现此疾病复发或症状加重的可能，
请随时就诊
诊 断：1.支气管哮喘；
检查
肺功能检查+支气管舒张实验
医生：张朝杰
打印日期：2025-05-25 12:03
第 1 页，共 1 页
---
郑州市第一人民医院
肺功能检查报告
舒张试验
姓名：
性别：男
年龄：61岁
身高：174 cm
体重：85 kg
科别：呼吸内科
住院号：
测试号：2025052513
吸烟史：
联系电话：
测试日期 25-5-25
测试时间 11:46:55
预计值
前次
前/预
后次
后/预
改善率
25-5-25
25-5-25
11:46:55
11:57:14
FVC [L] 4.10 2.84 69.4 3.49 85.2 22.91
FEV 1 [L] 3.22 2.51 78.0 3.06 95.0 21.81
FEV 1 % FVC [%] 83.40 88.46 106.1 87.66 105.1 -0.90
PEF [L/s] 8.21 6.40 77.9 6.63 80.8 3.68
MEF 75 [L/s] 7.26 6.18 85.1 6.13 84.4 -0.76
MEF 50 [L/s] 4.35 3.04 69.9 4.48 102.9 47.19
MEF 25 [L/s] 1.62 1.18 72.8 1.25 77.6 6.56
MMEF 75/25 [L/s] 3.45 2.26 65.4 3.32 96.0 46.80
Flow [L/s]
F/V ex
10
5
0
1
2
3
4
5
F/V In
6
Vol [L]
5
Vol%Vmax
100
V Cmax
80
3
60
2
40
20
1
0
0
Time [s]
0.0
0.5
1.0
1.5
2.0
2.5
3.0
测试结果：
支气管舒张试验阳性。
(请结合临床全面诊断)
医生签字：毛锦涛
---
郑州市第一人民医院
肺功能检查报告
常规通气
姓名：
性别：男
年龄：61岁
身高：174 cm
科别：呼吸内科
住院号：门诊
测试号：2025052513
体重：85 kg
测试日期 25-5-25
测试时间 11:46:55
预计值 实测值 实/预
IRV [L] 1.14
ERV [L] 3.12
IC [L] 0.61
VT [L] 4.26 0.65 106.5
VC IN [L] 4.26 3.01 70.7
VC EX [L] 4.26 2.84 66.8
BF [1/min] 20.00 17.72 88.6
MV [L/min] 12.14 11.46 94.4
VC MAX [L] 4.26 3.01 70.7
FVC [L] 4.10 2.84 69.4
FEV 1 [L] 3.22 2.51 78.0
FEV 1 % FVC [%] 83.40 88.46 106.1
FEV 1 % VC MAX [%] 76.23 83.54 109.6
PEF [L/s] 8.21 6.40 77.9
MEF 75 [L/s] 7.26 6.18 85.1
MEF 50 [L/s] 4.35 3.04 69.9
MEF 25 [L/s] 1.62 1.18 72.8
MMEF 75/25 [L/s] . 3.45 2.26 65.4
MVV [L/min] 119.91 77.46 64.6
FEV 1*30 [L/min] 119.91 75.39 62.9
Vol [L]
TLC 6
FRC pleth
RV 2
PredA0.0 0.2 0.4 0.6 0.8 1.0
Time [min]
Flow [L/s]
F/V ex
10
5
0
1
2
3
4
5
F/V in
Vol [L]
2
1
0
1
2
Time [s]
0 2 4 6 8 10 12
测试结果：
提示：
1、轻度阻塞性肺通气功能障碍；
2、肺储备功能下降。
(请结合临床全面诊断)
医生签字：毛锦涛
报告日期：2025-5-27
2026-08-10 06:19:58,876 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-10 06:19:58,876 INFO     29 [Trace] task=dbae825c | doc=LGWE-艾特美哮喘-洛阳三.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "3 items, types={'OutpatientRecord': 1, 'ExaminationReport': 2}", "name": "LGWE-艾特美哮喘-洛阳三.pdf", "embedding_token_consumption": 1534}
2026-08-10 06:19:58,876 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-10 06:19:59,155 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-10 06:19:59,156 INFO     29 [Trace] task=dbae825c | doc=LGWE-艾特美哮喘-洛阳三.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":3,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 06:19:59,158 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:59,159 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:59,159 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:19:59,167 INFO     29 set_progress(dbae825c948211f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 06:19:59 [DOC Engine]:
Start to index...
2026-08-10 06:19:59,193 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.020s]
2026-08-10 06:19:59,199 INFO     29 set_progress(dbae825c948211f1bd9827cf206dfa2d), progress: 0.8333333333333334, progress_msg: 
2026-08-10 06:19:59,211 INFO     29 set_progress(dbae825c948211f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 06:19:59 Indexing done (0.04s). Task done (225.99s)
2026-08-10 06:19:59,218 INFO     29 [Done], chunks(3), token(1534), elapsed:225.99
2026-08-10 06:19:59,282 INFO     29 handle_task done for task {"id": "dbae825c948211f1bd9827cf206dfa2d", "doc_id": "db492056948211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LGWE-\u827e\u7279\u7f8e\u54ee\u5598-\u6d1b\u9633\u4e09.pdf", "type": "pdf", "location": "LGWE-\u827e\u7279\u7f8e\u54ee\u5598-\u6d1b\u9633\u4e09.pdf", "size": 1648931, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786342517754, "task_type": "dataflow", "root_trace_id": "aaa86c5dcc2c462f88c0ac982e1d484f", "root_traceparent": "00-aaa86c5dcc2c462f88c0ac982e1d484f-c2d6050d16147908-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
