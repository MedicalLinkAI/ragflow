# 基准结果：LTSH 三门峡.pdf

## 基本信息

- 文件：`LTSH 三门峡.pdf`
- 大小：6481.0 KB
- PDF 总页数：5
- doc_id：`ab76d5fc948311f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T14:21:05  完成时间：2026-08-10T14:26:07  耗时：302.0s
- progress_msg：`06:25:31 Indexing done (0.06s). Task done (260.91s)`
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
| ExaminationReport | 检查报告 | 1 | 1 | 1 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 0 | 0 | 0 | report_time, report_category, report_name | **-** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 1, "ExaminationReport": 1}`
- ChunkMerger：`{"found": true, "merged": 2, "sources": 8, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1}, "filtered_noise": 6}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 06:25:28,897 INFO     29 [ChunkMerger] Merged 2 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 06:21:09,321 INFO     29 handle_task begin for task {"id": "abd585c0948311f1bd9827cf206dfa2d", "doc_id": "ab76d5fc948311f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LTSH \u4e09\u95e8\u5ce1.pdf", "type": "pdf", "location": "LTSH \u4e09\u95e8\u5ce1.pdf", "size": 6636575, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786342866974, "task_type": "dataflow", "root_trace_id": "bcc06c371b5649ffa23cad2dd92769a3", "root_traceparent": "00-bcc06c371b5649ffa23cad2dd92769a3-aca0c6f6ccf15910-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 06:21:09,636 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.002s]
2026-08-10 06:21:09,753 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 06:21:09,771 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:21:09,771 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 06:21:09,771 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 06:21:09,776 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 06:21:09,777 INFO     29 ============================================================
2026-08-10 06:21:09,777 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 06:21:09,777 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 06:21:09,777 INFO     29 ============================================================
2026-08-10 06:21:09,777 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 06:21:09,777 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 06:21:09,778 INFO     29 No torch found.
2026-08-10 06:21:10,384 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=5
2026-08-10 06:21:10,671 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1397957, prompt_len=764
2026-08-10 06:21:12,342 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-05-27"}
```
2026-08-10 06:21:12,342 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=2025-05-27
2026-08-10 06:21:12,351 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1397957, prompt_len=401
2026-08-10 06:21:16,025 INFO     29 [qwen-vl-parser] text API response (len=561):
["渑池县人民医院", "门诊病历", "姓名:", "门诊号: 613003", "就诊时间:2025-05-27 14:24 科别: 呼吸与危重症医学科门诊", "姓名", "性别:男 年龄:56岁 婚否:已婚", "职业:农民 工作单位:无", "联系电话: 住址:河南省三门峡市渑池县仁村乡大", "水沟村八组8号", "病史叙述者:本人 身份证号:", "过敏史:无", "主诉:发作性胸闷、气喘4天。", "现病史:患者于4天前受凉后出现胸闷、气喘,活动后加重,伴有咳", "嗽,咳痰不明显,无胸痛、发热、咯血、盗汗等,未予治疗,症", "状持续无缓解。", "既往史:平素身体良好;无特殊疾病史;否认“肝炎、结核”等病史;", "否认手术史;否认外伤史;否认输血史及献血史;否认药物及食", "物过敏史;无预防接种史", "流行病学史:无", "体格检查:体温36.7℃,脉搏80次/分,呼吸22次/分,", "血压132/80mmHg,双肺呼吸音粗,可闻及哮鸣音,未闻及", "明显湿性啰音,心率80次/分,未闻及病理性杂音。", "辅助检查:肺功能四项+支气管舒张实验;沙丁胺醇气雾剂支气管舒", "张实验呈阳性,FEV1.0改善41.1%。", "初步诊断:门诊诊断:1.支气管哮喘。", "-1-"]
2026-08-10 06:21:16,026 INFO     29 [qwen-vl-parser] page=1 text: 27 lines (bbox 0-26)
2026-08-10 06:21:16,026 INFO     29 [qwen-vl-parser] page=1 text: 27 sections
2026-08-10 06:21:16,279 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1102391, prompt_len=764
2026-08-10 06:21:17,722 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 06:21:17,723 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 06:21:17,735 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1102391, prompt_len=401
2026-08-10 06:21:18,643 INFO     29 [qwen-vl-parser] text API response (len=99):
["渑池县人民医院", "门诊病历", "姓名：", "门诊号", "处理意见：1.避免受凉，避免进食刺激性食物，避免接触刺激性气味；", "2.如有不适，及时就医。", "经治医师：", "2"]
2026-08-10 06:21:18,644 INFO     29 [qwen-vl-parser] page=2 text: 8 lines (bbox 27-34)
2026-08-10 06:21:18,644 INFO     29 [qwen-vl-parser] page=2 text: 8 sections
2026-08-10 06:21:19,003 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1964770, prompt_len=764
2026-08-10 06:21:20,739 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 06:21:20,739 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 06:21:20,752 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1964770, prompt_len=401
2026-08-10 06:21:28,241 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T06:21:28.240+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 4, "failed": 0, "current": {"abd585c0948311f1bd9827cf206dfa2d": {"id": "abd585c0948311f1bd9827cf206dfa2d", "doc_id": "ab76d5fc948311f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LTSH \u4e09\u95e8\u5ce1.pdf", "type": "pdf", "location": "LTSH \u4e09\u95e8\u5ce1.pdf", "size": 6636575, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786342866974, "task_type": "dataflow", "root_trace_id": "bcc06c371b5649ffa23cad2dd92769a3", "root_traceparent": "00-bcc06c371b5649ffa23cad2dd92769a3-aca0c6f6ccf15910-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 06:21:28,970 INFO     29 [qwen-vl-parser] text API response (len=1736):
["JAEGE R PCMED", "渑池县人民医院", "肺功能检查报告", "综合测试", "姓名：", "性别：男", "年龄：56 Years", "身高：165 cm", "体重：70 kg", "备注：", "联系电话：", "住院号：0", "测试号：", "吸烟史：", "既往史：", "职业：", "测试日期", "测试时间", "预计值", "实测值", "实/预", "VC MAX", "[L]", "3.85", "2.72", "70.6", "FVC", "[L]", "3.71", "2.68", "72.2", "MV", "[L/min]", "10.00", "18.75", "187.5", "FEV 1", "[L]", "2.98", "1.10", "36.9", "FEV 1 % FVC", "[%]", "83.77", "41.10", "49.1", "PEF", "[L/s]", "7.87", "2.33", "29.6", "MEF 75", "[L/s]", "6.92", "0.96", "13.9", "MEF 50", "[L/s]", "4.17", "0.52", "12.5", "MEF 25", "[L/s]", "1.51", "0.22", "14.3", "MMEF 75/25", "[L/s]", "3.49", "0.44", "12.6", "MVV", "[L/min]", "113.25", "52.56", "46.4", "TLC-SB", "[L]", "6.10", "5.24", "85.9", "RV-SB", "[L]", "2.16", "2.69", "124.4", "RV%TLC-SB", "[%]", "35.80", "51.32", "143.4", "FRC-SB", "[L]", "3.28", "3.71", "113.3", "FRC%TLC-SB", "[%]", "55.56", "70.79", "127.4", "DLCO SB [mmol/min/kPa]", "8.61", "7.20", "83.7", "DLCO/Va mmol/min/kPa/L]", "1.41", "1.42", "100.4", "Hb", "[g/100ml]", "14.60", "VA", "[L]", "5.95", "5.09", "85.5", "DLCOc SB [mmol/min/kPa]", "8.61", "7.20", "83.7", "DLCOc/Va mmol/min/kPa/L]", "1.41", "1.42", "100.4", "VIN", "[L]", "3.85", "2.55", "66.3", "Insp. time", "[s]", "1.52", "Exp. time", "[s]", "2.15", "Sample vol", "[L]", "System dead space [ml]", "172.00", "Anatom. dead space[ml]", "154.00", "TA", "[s]", "11.54", "测试结果：", "TLC", "6", "Vol [L]", "FRCoeth", "25/4/25", "9:19:05上", "RW", "Time [min]", "PredAdt.0", "0.2", "0.4", "0.6", "0.8", "1.0", "Flow [L/s]", "F/V ex", "10", "5", "0", "2", "4", "6", "F/V in", "10", "Vol [L]", "Vol [L]", "100", "10", "50", "Time [s]", "0", "2", "4", "6", "8", "10", "Volume [L]", "4", "2", "0", "1", "4", "Time [s]", "0", "10", "20", "30", "40"]
2026-08-10 06:21:28,971 INFO     29 [qwen-vl-parser] page=3 text: 194 lines (bbox 35-228)
2026-08-10 06:21:28,971 INFO     29 [qwen-vl-parser] page=3 text: 194 sections
2026-08-10 06:21:29,188 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1210531, prompt_len=764
2026-08-10 06:21:30,753 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-04-25"}
```
2026-08-10 06:21:30,753 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=2025-04-25
2026-08-10 06:21:30,767 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1210531, prompt_len=401
2026-08-10 06:21:37,079 INFO     29 [qwen-vl-parser] text API response (len=1201):
["JAEGE R PCMED", "渑池县人民医院", "肺功能检查报告", "舒张试验", "姓名：", "科别：", "住院号：0", "测试号：2025042503", "性别：男", "年龄：56 Years", "身高：165 cm", "体重：70 kg", "标准体重：108 %", "体表面积：1.77 m", "吸烟史：", "Flow [L/s]", "F/V ex", "Vol%VCmax", "Vol [L]", "10", "20", "40", "60", "2", "80", "100", "VCmax", "1", "0", "2", "3", "4", "5", "6", "7", "1", "2", "4", "5", "6", "7", "8", "10", "Time [s]", "F/V in", "8", "0", "1", "2", "3", "4", "5", "6", "7", "8", "预计值", "前次", "前/预", "后次", "后/预", "改善率", "测试日期", "25/4/25", "25/4/25", "测试时间", "9:19:05", "9:43:24", "VC MAX", "[L]", "3.85", "2.72", "70.6", "3.07", "79.9", "13.2", "FVC", "[L]", "3.71", "2.68", "72.2", "3.05", "82.4", "14.1", "FEV 1", "[L]", "2.98", "1.10", "36.9", "1.55", "52.1", "41.1", "FEV 1 % FVC", "[%]", "83.77", "41.10", "49.1", "50.82", "60.7", "23.6", "FEV 1 % VC MAX", "[%]", "77.13", "40.51", "52.5", "50.49", "65.5", "24.6", "PEF", "[L/s]", "7.87", "2.33", "29.6", "3.18", "40.4", "36.6", "MEF 75", "[L/s]", "6.92", "0.96", "13.9", "1.65", "23.9", "72.1", "MEF 50", "[L/s]", "4.17", "0.52", "12.5", "0.85", "20.3", "63.0", "MEF 25", "[L/s]", "1.51", "0.22", "14.3", "0.35", "23.2", "62.9", "MMEF 75/25", "[L/s]", "3.49", "0.44", "12.6", "0.75", "21.3", "69.5"]
2026-08-10 06:21:37,080 INFO     29 [qwen-vl-parser] page=4 text: 147 lines (bbox 229-375)
2026-08-10 06:21:37,080 INFO     29 [qwen-vl-parser] page=4 text: 147 sections
2026-08-10 06:21:37,445 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2169828, prompt_len=764
2026-08-10 06:21:38,985 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 06:21:38,986 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 06:21:38,999 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2169828, prompt_len=401
2026-08-10 06:21:47,305 INFO     29 [qwen-vl-parser] text API response (len=1403):
["JAEGER PCMED", "渑池县人民医院", "肺功能检查报告", "常规通气", "姓名：", "住院号：0", "性别：男", "身高：165 cm", "标准体重：108 %", "吸烟史：", "科别：", "测试号：2025042503", "年龄：56 Years", "体重：70 kg", "体表面积：1.77 m", "预计值 实测值 实测/预", "测试日期 25/4/25", "测试时间 9:19:05]", "VC MAX [L] 3.85 2.72 70.6", "IRV [L] 0.91", "ERV [L] 1.11 1.02 91.8", "IC [L] 2.74 1.69 61.9", "VT [L] 0.50 0.78 156.7", "MV [L/min] 10.00 18.75 187.5", "VC IN [L] 3.85 2.69 70.0", "VC EX [L] 3.85 2.72 70.6", "BF [1/min] 20.00 23.93 119.7", "FVC [L] 3.71 2.68 72.2", "PEF [L/s] 7.87 2.33 29.6", "FEV 0.5 [L] 0.70", "FEV 1 [L] 2.98 1.10 36.9", "FEV 2 [L] 1.60", "FEV 3 [L] 1.91", "FEV6 [L] 2.45", "FEF 200-1200 [L/s] 0.94", "FEV 1 % FVC [%] 83.77 41.10 49.1", "FEV 1 % VC MAX [%] 77.13 40.51 52.5", "MEF 75 [L/s] 6.92 0.96 13.9", "MEF 50 [L/s] 4.17 0.52 12.5", "MEF 25 [L/s] 1.51 0.22 14.3", "MMEF 75/25 [L/s] 3.49 0.44 12.6", "FEF 75/85 [L/s] 0.77 0.18 23.0", "FEF50 % FIF50 [%] 38.63", "PIF [L/s] 1.41", "FVC IN [L] 3.85 2.69 70.0", "FET [s] 7.87", "FIF 50 [L/s] 1.35", "FIV1 [L] 1.10", "FIV1 % FVC [%] 40.89", "T IN [s] 1.21", "T EX [s] 1.30", "T TOT [s] 2.51", "MIF [L/s] 0.65", "MEF [L/s] 0.60", "MVV [L/min] 113.25 52.56 46.4", "FEF50 % FIF50 [%] 38.63", "V backextrapolation ex [L] 0.02", "V backextrapol. % FVC [%] 0.75", "测试结果", "1、重度阻塞性肺通气功能障碍，小气道功能降低。", "2、肺弥散功能正常。", "3、残气量正常，残气量/肺总量增高。", "4、沙丁胺醇气雾剂支气管舒张试验呈阳性，FEV1.0改41.1%。", "5、建议定期复查。", "报告医师：李朝红/崔艳芳 报告日期：2025.4.25"]
2026-08-10 06:21:47,306 INFO     29 [qwen-vl-parser] page=5 text: 65 lines (bbox 376-440)
2026-08-10 06:21:47,306 INFO     29 [qwen-vl-parser] page=5 text: 65 sections
2026-08-10 06:21:47,307 INFO     29 [qwen-vl-parser] parse_pdf done: 441 sections from 5 pages.
2026-08-10 06:21:47,336 INFO     29 Close text detector.
2026-08-10 06:21:47,970 INFO     29 Close text recognizer.
2026-08-10 06:21:48,351 INFO     29 Close recognizer.
2026-08-10 06:21:48,796 INFO     29 Close recognizer.
2026-08-10 06:21:49,274 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 06:21:49,274 INFO     29 [Trace] task=abd585c0 | doc=LTSH 三门峡.pdf | Parser:MedLink | outputs={"html": "", "json": "441 items", "markdown": "", "text": "", "name": "LTSH 三门峡.pdf", "output_format": "json"}
2026-08-10 06:21:49,274 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 06:21:49,306 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:21:49,307 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 渑池县人民医院\n[BBOX-1] 门诊病历\n[BBOX-2] 姓名:\n[BBOX-3] 门诊号: 613003\n[BBOX-4] 就诊时间:2025-05-27 14:24 科别: 呼吸与危重症医学科门诊\n[BBOX-5] 姓名\n[BBOX-6] 性别:男 年龄:56岁 婚否:已婚\n[BBOX-7] 职业:农民 工作单位:无\n[BBOX-8] 联系电话: 住址:河南省三门峡市渑池县仁村乡大\n[BBOX-9] 水沟村八组8号\n[BBOX-10] 病史叙述者:本人 身份证号:\n[BBOX-11] 过敏史:无\n[BBOX-12] 主诉:发作性胸闷、气喘4天。\n[BBOX-13] 现病史:患者于4天前受凉后出现胸闷、气喘,活动后加重,伴有咳\n[BBOX-14] 嗽,咳痰不明显,无胸痛、发热、咯血、盗汗等,未予治疗,症\n[BBOX-15] 状持续无缓解。\n[BBOX-16] 既往史:平素身体良好;无特殊疾病史;否认“肝炎、结核”等病史;\n[BBOX-17] 否认手术史;否认外伤史;否认输血史及献血史;否认药物及食\n[BBOX-18] 物过敏史;无预防接种史\n[BBOX-19] 流行病学史:无\n[BBOX-20] 体格检查:体温36.7℃,脉搏80次/分,呼吸22次/分,\n[BBOX-21] 血压132/80mmHg,双肺呼吸音粗,可闻及哮鸣音,未闻及\n[BBOX-22] 明显湿性啰音,心率80次/分,未闻及病理性杂音。\n[BBOX-23] 辅助检查:肺功能四项+支气管舒张实验;沙丁胺醇气雾剂支气管舒\n[BBOX-24] 张实验呈阳性,FEV1.0改善41.1%。\n[BBOX-25] 初步诊断:门诊诊断:1.支气管哮喘。\n[BBOX-26] -1-\n[BBOX-27] 渑池县人民医院\n[BBOX-28] 门诊病历\n[BBOX-29] 姓名：\n[BBOX-30] 门诊号\n[BBOX-31] 处理意见：1.避免受凉，避免进食刺激性食物，避免接触刺激性气味；\n[BBOX-32] 2.如有不适，及时就医。\n[BBOX-33] 经治医师：\n[BBOX-34] 2\n[BBOX-35] JAEGE R PCMED\n[BBOX-36] 渑池县人民医院\n[BBOX-37] 肺功能检查报告\n[BBOX-38] 综合测试\n[BBOX-39] 姓名：\n[BBOX-40] 性别：男\n[BBOX-41] 年龄：56 Years\n[BBOX-42] 身高：165 cm\n[BBOX-43] 体重：70 kg\n[BBOX-44] 备注：\n[BBOX-45] 联系电话：\n[BBOX-46] 住院号：0\n[BBOX-47] 测试号：\n[BBOX-48] 吸烟史：\n[BBOX-49] 既往史：\n[BBOX-50] 职业：\n[BBOX-51] 测试日期\n[BBOX-52] 测试时间\n[BBOX-53] 预计值\n[BBOX-54] 实测值\n[BBOX-55] 实/预\n[BBOX-56] VC MAX\n[BBOX-57] [L]\n[BBOX-58] 3.85\n[BBOX-59] 2.72\n[BBOX-60] 70.6\n[BBOX-61] FVC\n[BBOX-62] [L]\n[BBOX-63] 3.71\n[BBOX-64] 2.68\n[BBOX-65] 72.2\n[BBOX-66] MV\n[BBOX-67] [L/min]\n[BBOX-68] 10.00\n[BBOX-69] 18.75\n[BBOX-70] 187.5\n[BBOX-71] FEV 1\n[BBOX-72] [L]\n[BBOX-73] 2.98\n[BBOX-74] 1.10\n[BBOX-75] 36.9\n[BBOX-76] FEV 1 % FVC\n[BBOX-77] [%]\n[BBOX-78] 83.77\n[BBOX-79] 41.10\n[BBOX-80] 49.1\n[BBOX-81] PEF\n[BBOX-82] [L/s]\n[BBOX-83] 7.87\n[BBOX-84] 2.33\n[BBOX-85] 29.6\n[BBOX-86] MEF 75\n[BBOX-87] [L/s]\n[BBOX-88] 6.92\n[BBOX-89] 0.96\n[BBOX-90] 13.9\n[BBOX-91] MEF 50\n[BBOX-92] [L/s]\n[BBOX-93] 4.17\n[BBOX-94] 0.52\n[BBOX-95] 12.5\n[BBOX-96] MEF 25\n[BBOX-97] [L/s]\n[BBOX-98] 1.51\n[BBOX-99] 0.22\n[BBOX-100] 14.3\n[BBOX-101] MMEF 75/25\n[BBOX-102] [L/s]\n[BBOX-103] 3.49\n[BBOX-104] 0.44\n[BBOX-105] 12.6\n[BBOX-106] MVV\n[BBOX-107] [L/min]\n[BBOX-108] 113.25\n[BBOX-109] 52.56\n[BBOX-110] 46.4\n[BBOX-111] TLC-SB\n[BBOX-112] [L]\n[BBOX-113] 6.10\n[BBOX-114] 5.24\n[BBOX-115] 85.9\n[BBOX-116] RV-SB\n[BBOX-117] [L]\n[BBOX-118] 2.16\n[BBOX-119] 2.69\n[BBOX-120] 124.4\n[BBOX-121] RV%TLC-SB\n[BBOX-122] [%]\n[BBOX-123] 35.80\n[BBOX-124] 51.32\n[BBOX-125] 143.4\n[BBOX-126] FRC-SB\n[BBOX-127] [L]\n[BBOX-128] 3.28\n[BBOX-129] 3.71\n[BBOX-130] 113.3\n[BBOX-131] FRC%TLC-SB\n[BBOX-132] [%]\n[BBOX-133] 55.56\n[BBOX-134] 70.79\n[BBOX-135] 127.4\n[BBOX-136] DLCO SB [mmol/min/kPa]\n[BBOX-137] 8.61\n[BBOX-138] 7.20\n[BBOX-139] 83.7\n[BBOX-140] DLCO/Va mmol/min/kPa/L]\n[BBOX-141] 1.41\n[BBOX-142] 1.42\n[BBOX-143] 100.4\n[BBOX-144] Hb\n[BBOX-145] [g/100ml]\n[BBOX-146] 14.60\n[BBOX-147] VA\n[BBOX-148] [L]\n[BBOX-149] 5.95\n[BBOX-150] 5.09\n[BBOX-151] 85.5\n[BBOX-152] DLCOc SB [mmol/min/kPa]\n[BBOX-153] 8.61\n[BBOX-154] 7.20\n[BBOX-155] 83.7\n[BBOX-156] DLCOc/Va mmol/min/kPa/L]\n[BBOX-157] 1.41\n[BBOX-158] 1.42\n[BBOX-159] 100.4\n[BBOX-160] VIN\n[BBOX-161] [L]\n[BBOX-162] 3.85\n[BBOX-163] 2.55\n[BBOX-164] 66.3\n[BBOX-165] Insp. time\n[BBOX-166] [s]\n[BBOX-167] 1.52\n[BBOX-168] Exp. time\n[BBOX-169] [s]\n[BBOX-170] 2.15\n[BBOX-171] Sample vol\n[BBOX-172] [L]\n[BBOX-173] System dead space [ml]\n[BBOX-174] 172.00\n[BBOX-175] Anatom. dead space[ml]\n[BBOX-176] 154.00\n[BBOX-177] TA\n[BBOX-178] [s]\n[BBOX-179] 11.54\n[BBOX-180] 测试结果：\n[BBOX-181] TLC\n[BBOX-182] 6\n[BBOX-183] Vol [L]\n[BBOX-184] FRCoeth\n[BBOX-185] 25/4/25\n[BBOX-186] 9:19:05上\n[BBOX-187] RW\n[BBOX-188] Time [min]\n[BBOX-189] PredAdt.0\n[BBOX-190] 0.2\n[BBOX-191] 0.4\n[BBOX-192] 0.6\n[BBOX-193] 0.8\n[BBOX-194] 1.0\n[BBOX-195] Flow [L/s]\n[BBOX-196] F/V ex\n[BBOX-197] 10\n[BBOX-198] 5\n[BBOX-199] 0\n[BBOX-200] 2\n[BBOX-201] 4\n[BBOX-202] 6\n[BBOX-203] F/V in\n[BBOX-204] 10\n[BBOX-205] Vol [L]\n[BBOX-206] Vol [L]\n[BBOX-207] 100\n[BBOX-208] 10\n[BBOX-209] 50\n[BBOX-210] Time [s]\n[BBOX-211] 0\n[BBOX-212] 2\n[BBOX-213] 4\n[BBOX-214] 6\n[BBOX-215] 8\n[BBOX-216] 10\n[BBOX-217] Volume [L]\n[BBOX-218] 4\n[BBOX-219] 2\n[BBOX-220] 0\n[BBOX-221] 1\n[BBOX-222] 4\n[BBOX-223] Time [s]\n[BBOX-224] 0\n[BBOX-225] 10\n[BBOX-226] 20\n[BBOX-227] 30\n[BBOX-228] 40\n[BBOX-229] JAEGE R PCMED\n[BBOX-230] 渑池县人民医院\n[BBOX-231] 肺功能检查报告\n[BBOX-232] 舒张试验\n[BBOX-233] 姓名：\n[BBOX-234] 科别：\n[BBOX-235] 住院号：0\n[BBOX-236] 测试号：2025042503\n[BBOX-237] 性别：男\n[BBOX-238] 年龄：56 Years\n[BBOX-239] 身高：165 cm\n[BBOX-240] 体重：70 kg\n[BBOX-241] 标准体重：108 %\n[BBOX-242] 体表面积：1.77 m\n[BBOX-243] 吸烟史：\n[BBOX-244] Flow [L/s]\n[BBOX-245] F/V ex\n[BBOX-246] Vol%VCmax\n[BBOX-247] Vol [L]\n[BBOX-248] 10\n[BBOX-249] 20\n[BBOX-250] 40\n[BBOX-251] 60\n[BBOX-252] 2\n[BBOX-253] 80\n[BBOX-254] 100\n[BBOX-255] VCmax\n[BBOX-256] 1\n[BBOX-257] 0\n[BBOX-258] 2\n[BBOX-259] 3\n[BBOX-260] 4\n[BBOX-261] 5\n[BBOX-262] 6\n[BBOX-263] 7\n[BBOX-264] 1\n[BBOX-265] 2\n[BBOX-266] 4\n[BBOX-267] 5\n[BBOX-268] 6\n[BBOX-269] 7\n[BBOX-270] 8\n[BBOX-271] 10\n[BBOX-272] Time [s]\n[BBOX-273] F/V in\n[BBOX-274] 8\n[BBOX-275] 0\n[BBOX-276] 1\n[BBOX-277] 2\n[BBOX-278] 3\n[BBOX-279] 4\n[BBOX-280] 5\n[BBOX-281] 6\n[BBOX-282] 7\n[BBOX-283] 8\n[BBOX-284] 预计值\n[BBOX-285] 前次\n[BBOX-286] 前/预\n[BBOX-287] 后次\n[BBOX-288] 后/预\n[BBOX-289] 改善率\n[BBOX-290] 测试日期\n[BBOX-291] 25/4/25\n[BBOX-292] 25/4/25\n[BBOX-293] 测试时间\n[BBOX-294] 9:19:05\n[BBOX-295] 9:43:24\n[BBOX-296] VC MAX\n[BBOX-297] [L]\n[BBOX-298] 3.85\n[BBOX-299] 2.72\n[BBOX-300] 70.6\n[BBOX-301] 3.07\n[BBOX-302] 79.9\n[BBOX-303] 13.2\n[BBOX-304] FVC\n[BBOX-305] [L]\n[BBOX-306] 3.71\n[BBOX-307] 2.68\n[BBOX-308] 72.2\n[BBOX-309] 3.05\n[BBOX-310] 82.4\n[BBOX-311] 14.1\n[BBOX-312] FEV 1\n[BBOX-313] [L]\n[BBOX-314] 2.98\n[BBOX-315] 1.10\n[BBOX-316] 36.9\n[BBOX-317] 1.55\n[BBOX-318] 52.1\n[BBOX-319] 41.1\n[BBOX-320] FEV 1 % FVC\n[BBOX-321] [%]\n[BBOX-322] 83.77\n[BBOX-323] 41.10\n[BBOX-324] 49.1\n[BBOX-325] 50.82\n[BBOX-326] 60.7\n[BBOX-327] 23.6\n[BBOX-328] FEV 1 % VC MAX\n[BBOX-329] [%]\n[BBOX-330] 77.13\n[BBOX-331] 40.51\n[BBOX-332] 52.5\n[BBOX-333] 50.49\n[BBOX-334] 65.5\n[BBOX-335] 24.6\n[BBOX-336] PEF\n[BBOX-337] [L/s]\n[BBOX-338] 7.87\n[BBOX-339] 2.33\n[BBOX-340] 29.6\n[BBOX-341] 3.18\n[BBOX-342] 40.4\n[BBOX-343] 36.6\n[BBOX-344] MEF 75\n[BBOX-345] [L/s]\n[BBOX-346] 6.92\n[BBOX-347] 0.96\n[BBOX-348] 13.9\n[BBOX-349] 1.65\n[BBOX-350] 23.9\n[BBOX-351] 72.1\n[BBOX-352] MEF 50\n[BBOX-353] [L/s]\n[BBOX-354] 4.17\n[BBOX-355] 0.52\n[BBOX-356] 12.5\n[BBOX-357] 0.85\n[BBOX-358] 20.3\n[BBOX-359] 63.0\n[BBOX-360] MEF 25\n[BBOX-361] [L/s]\n[BBOX-362] 1.51\n[BBOX-363] 0.22\n[BBOX-364] 14.3\n[BBOX-365] 0.35\n[BBOX-366] 23.2\n[BBOX-367] 62.9\n[BBOX-368] MMEF 75/25\n[BBOX-369] [L/s]\n[BBOX-370] 3.49\n[BBOX-371] 0.44\n[BBOX-372] 12.6\n[BBOX-373] 0.75\n[BBOX-374] 21.3\n[BBOX-375] 69.5\n[BBOX-376] JAEGER PCMED\n[BBOX-377] 渑池县人民医院\n[BBOX-378] 肺功能检查报告\n[BBOX-379] 常规通气\n[BBOX-380] 姓名：\n[BBOX-381] 住院号：0\n[BBOX-382] 性别：男\n[BBOX-383] 身高：165 cm\n[BBOX-384] 标准体重：108 %\n[BBOX-385] 吸烟史：\n[BBOX-386] 科别：\n[BBOX-387] 测试号：2025042503\n[BBOX-388] 年龄：56 Years\n[BBOX-389] 体重：70 kg\n[BBOX-390] 体表面积：1.77 m\n[BBOX-391] 预计值 实测值 实测/预\n[BBOX-392] 测试日期 25/4/25\n[BBOX-393] 测试时间 9:19:05]\n[BBOX-394] VC MAX [L] 3.85 2.72 70.6\n[BBOX-395] IRV [L] 0.91\n[BBOX-396] ERV [L] 1.11 1.02 91.8\n[BBOX-397] IC [L] 2.74 1.69 61.9\n[BBOX-398] VT [L] 0.50 0.78 156.7\n[BBOX-399] MV [L/min] 10.00 18.75 187.5\n[BBOX-400] VC IN [L] 3.85 2.69 70.0\n[BBOX-401] VC EX [L] 3.85 2.72 70.6\n[BBOX-402] BF [1/min] 20.00 23.93 119.7\n[BBOX-403] FVC [L] 3.71 2.68 72.2\n[BBOX-404] PEF [L/s] 7.87 2.33 29.6\n[BBOX-405] FEV 0.5 [L] 0.70\n[BBOX-406] FEV 1 [L] 2.98 1.10 36.9\n[BBOX-407] FEV 2 [L] 1.60\n[BBOX-408] FEV 3 [L] 1.91\n[BBOX-409] FEV6 [L] 2.45\n[BBOX-410] FEF 200-1200 [L/s] 0.94\n[BBOX-411] FEV 1 % FVC [%] 83.77 41.10 49.1\n[BBOX-412] FEV 1 % VC MAX [%] 77.13 40.51 52.5\n[BBOX-413] MEF 75 [L/s] 6.92 0.96 13.9\n[BBOX-414] MEF 50 [L/s] 4.17 0.52 12.5\n[BBOX-415] MEF 25 [L/s] 1.51 0.22 14.3\n[BBOX-416] MMEF 75/25 [L/s] 3.49 0.44 12.6\n[BBOX-417] FEF 75/85 [L/s] 0.77 0.18 23.0\n[BBOX-418] FEF50 % FIF50 [%] 38.63\n[BBOX-419] PIF [L/s] 1.41\n[BBOX-420] FVC IN [L] 3.85 2.69 70.0\n[BBOX-421] FET [s] 7.87\n[BBOX-422] FIF 50 [L/s] 1.35\n[BBOX-423] FIV1 [L] 1.10\n[BBOX-424] FIV1 % FVC [%] 40.89\n[BBOX-425] T IN [s] 1.21\n[BBOX-426] T EX [s] 1.30\n[BBOX-427] T TOT [s] 2.51\n[BBOX-428] MIF [L/s] 0.65\n[BBOX-429] MEF [L/s] 0.60\n[BBOX-430] MVV [L/min] 113.25 52.56 46.4\n[BBOX-431] FEF50 % FIF50 [%] 38.63\n[BBOX-432] V backextrapolation ex [L] 0.02\n[BBOX-433] V backextrapol. % FVC [%] 0.75\n[BBOX-434] 测试结果\n[BBOX-435] 1、重度阻塞性肺通气功能障碍，小气道功能降低。\n[BBOX-436] 2、肺弥散功能正常。\n[BBOX-437] 3、残气量正常，残气量/肺总量增高。\n[BBOX-438] 4、沙丁胺醇气雾剂支气管舒张试验呈阳性，FEV1.0改41.1%。\n[BBOX-439] 5、建议定期复查。\n[BBOX-440] 报告医师：李朝红/崔艳芳 报告日期：2025.4.25"
  }
]
2026-08-10 06:21:53,874 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:21:53,902 INFO     29 [SmartSplitter] SmartSplitter done: 2 chunks from 2 LLM segments (all bbox_id). Types: {'OutpatientRecord': 1, 'ExaminationReport': 1}
2026-08-10 06:21:53,920 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 06:21:53,920 INFO     29 [Trace] task=abd585c0 | doc=LTSH 三门峡.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "441 items", "markdown": "", "text": "", "name": "LTSH 三门峡.pdf", "output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}"}
2026-08-10 06:21:53,920 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 06:21:53,921 INFO     29 [ChunkRouter] Routed 2 chunks into 2 groups: {'chunks_Clinical': 1, 'chunks_Examination': 1}
2026-08-10 06:21:53,934 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 06:21:53,934 INFO     29 [Trace] task=abd585c0 | doc=LTSH 三门峡.pdf | ChunkRouter:Router | outputs={"html": "", "json": "441 items", "markdown": "", "text": "", "name": "LTSH 三门峡.pdf", "output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:21:53,934 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 06:21:53,945 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:21:53,945 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:21:54,547 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:21:54,554 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 06:21:54,554 INFO     29 [Trace] task=abd585c0 | doc=LTSH 三门峡.pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "441 items", "markdown": "", "text": "", "name": "LTSH 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:21:54,555 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 06:21:54,564 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:21:54,564 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:21:55,508 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:21:55,523 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 06:21:55,523 INFO     29 [Trace] task=abd585c0 | doc=LTSH 三门峡.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "441 items", "markdown": "", "text": "", "name": "LTSH 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:21:55,523 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 06:21:55,533 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 06:21:55,534 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:21:55,534 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 06:21:55,534 INFO     29 [qwen-vl-text] positions(35): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 06:21:55,534 INFO     29 [qwen-vl-text] page grouping: [0, 1], lines per page: [27, 8]
2026-08-10 06:21:55,772 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 06:21:55,963 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 06:21:55,964 INFO     29 [qwen-vl-text] LLM extraction start, text_len=554
2026-08-10 06:21:55,964 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:21:55,964 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 34, \"encounter_dates\": [\"2025-05-27\"], \"department\": \"呼吸与危重症医学科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "渑池县人民医院\n门诊病历\n姓名:\n门诊号: 613003\n就诊时间:2025-05-27 14:24 科别: 呼吸与危重症医学科门诊\n姓名\n性别:男 年龄:56岁 婚否:已婚\n职业:农民 工作单位:无\n联系电话: 住址:河南省三门峡市渑池县仁村乡大\n水沟村八组8号\n病史叙述者:本人 身份证号:\n过敏史:无\n主诉:发作性胸闷、气喘4天。\n现病史:患者于4天前受凉后出现胸闷、气喘,活动后加重,伴有咳\n嗽,咳痰不明显,无胸痛、发热、咯血、盗汗等,未予治疗,症\n状持续无缓解。\n既往史:平素身体良好;无特殊疾病史;否认“肝炎、结核”等病史;\n否认手术史;否认外伤史;否认输血史及献血史;否认药物及食\n物过敏史;无预防接种史\n流行病学史:无\n体格检查:体温36.7℃,脉搏80次/分,呼吸22次/分,\n血压132/80mmHg,双肺呼吸音粗,可闻及哮鸣音,未闻及\n明显湿性啰音,心率80次/分,未闻及病理性杂音。\n辅助检查:肺功能四项+支气管舒张实验;沙丁胺醇气雾剂支气管舒\n张实验呈阳性,FEV1.0改善41.1%。\n初步诊断:门诊诊断:1.支气管哮喘。\n-1-\n渑池县人民医院\n门诊病历\n姓名：\n门诊号\n处理意见：1.避免受凉，避免进食刺激性食物，避免接触刺激性气味；\n2.如有不适，及时就医。\n经治医师：\n2",
    "role": "user"
  }
]
2026-08-10 06:21:58,291 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T06:21:58.290+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 4, "failed": 0, "current": {"abd585c0948311f1bd9827cf206dfa2d": {"id": "abd585c0948311f1bd9827cf206dfa2d", "doc_id": "ab76d5fc948311f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LTSH \u4e09\u95e8\u5ce1.pdf", "type": "pdf", "location": "LTSH \u4e09\u95e8\u5ce1.pdf", "size": 6636575, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786342866974, "task_type": "dataflow", "root_trace_id": "bcc06c371b5649ffa23cad2dd92769a3", "root_traceparent": "00-bcc06c371b5649ffa23cad2dd92769a3-aca0c6f6ccf15910-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 06:21:58,316 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:21:58,316 INFO     29 [qwen-vl-text] LLM output (len=336):
{
  "encounter_date": "2025-05-27",
  "chief_complaint": "发作性胸闷、气喘4天。",
  "present_illness": "患者于4天前受凉后出现胸闷、气喘,活动后加重,伴有咳嗽,咳痰不明显,无胸痛、发热、咯血、盗汗等,未予治疗,症状持续无缓解。",
  "past_history": "平素身体良好;无特殊疾病史;否认“肝炎、结核”等病史;否认手术史;否认外伤史;否认输血史及献血史;否认药物及食物过敏史;无预防接种史",
  "diagnosis": "1.支气管哮喘。",
  "treatment_plan": "1.避免受凉，避免进食刺激性食物，避免接触刺激性气味；2.如有不适，及时就医。"
}
2026-08-10 06:21:58,316 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-05-27]
2026-08-10 06:21:58,321 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1931395, prompt_len=1173
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共27行）
["渑池县人民医院", "门诊病历", "姓名:", "门诊号: 613003", "就诊时间:2025-05-27 14:24 科别: 呼吸与危重症医学科门诊", "姓名", "性别:男 年龄:56岁 婚否:已婚", "职业:农民 工作单位:无", "联系电话: 住址:河南省三门峡市渑池县仁村乡大", "水沟村八组8号", "病史叙述者:本人 身份证号:", "过敏史:无", "主诉:发作性胸闷、气喘4天。", "现病史:患者于4天前受凉后出现胸闷、气喘,活动后加重,伴有咳", "嗽,咳痰不明显,无胸痛、发热、咯血、盗汗等,未予治疗,症", "状持续无缓解。", "既往史:平素身体良好;无特殊疾病史;否认“肝炎、结核”等病史;", "否认手术史;否认外伤史;否认输血史及献血史;否认药物及食", "物过敏史;无预防接种史", "流行病学史:无", "体格检查:体温36.7℃,脉搏80次/分,呼吸22次/分,", "血压132/80mmHg,双肺呼吸音粗,可闻及哮鸣音,未闻及", "明显湿性啰音,心率80次/分,未闻及病理性杂音。", "辅助检查:肺功能四项+支气管舒张实验;沙丁胺醇气雾剂支气管舒", "张实验呈阳性,FEV1.0改善41.1%。", "初步诊断:门诊诊断:1.支气管哮喘。", "-1-"]

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
2026-08-10 06:22:09,601 INFO     29 [qwen-vl-text] coord API raw response (len=1670):
[
	{"text": "渑池县人民医院", "bbox": [357, 209, 550, 230]},
	{"text": "门诊病历", "bbox": [378, 237, 530, 257]},
	{"text": "姓名:", "bbox": [171, 264, 216, 279]},
	{"text": "门诊号: 613003", "bbox": [453, 264, 583, 278]},
	{"text": "就诊时间:2025-05-27 14:24 科别: 呼吸与危重症医学科门诊", "bbox": [170, 295, 687, 309]},
	{"text": "姓名", "bbox": [167, 323, 204, 337]},
	{"text": "性别:男 年龄:56岁 婚否:已婚", "bbox": [300, 323, 643, 337]},
	{"text": "职业:农民 工作单位:无", "bbox": [166, 342, 520, 356]},
	{"text": "联系电话: 住址:河南省三门峡市渑池县仁村乡大", "bbox": [164, 360, 730, 374]},
	{"text": "水沟村八组8号", "bbox": [163, 379, 298, 393]},
	{"text": "病史叙述者:本人 身份证号:", "bbox": [161, 398, 491, 412]},
	{"text": "过敏史:无", "bbox": [159, 417, 258, 432]},
	{"text": "主诉:发作性胸闷、气喘4天。", "bbox": [159, 446, 413, 461]},
	{"text": "现病史:患者于4天前受凉后出现胸闷、气喘,活动后加重,伴有咳", "bbox": [157, 466, 733, 481]},
	{"text": "嗽,咳痰不明显,无胸痛、发热、咯血、盗汗等,未予治疗,症", "bbox": [193, 485, 744, 500]},
	{"text": "状持续无缓解。", "bbox": [192, 505, 322, 520]},
	{"text": "既往史:平素身体良好;无特殊疾病史;否认“肝炎、结核”等病史;", "bbox": [152, 525, 754, 541]},
	{"text": "否认手术史;否认外伤史;否认输血史及献血史;否认药物及食", "bbox": [190, 546, 748, 561]},
	{"text": "物过敏史;无预防接种史", "bbox": [188, 567, 412, 582]},
	{"text": "流行病学史:无", "bbox": [147, 589, 290, 605]},
	{"text": "体格检查:体温36.7℃,脉搏80次/分,呼吸22次/分,", "bbox": [144, 610, 607, 627]},
	{"text": "血压132/80mmHg,双肺呼吸音粗,可闻及哮鸣音,未闻及", "bbox": [245, 631, 754, 648]},
	{"text": "明显湿性啰音,心率80次/分,未闻及病理性杂音。", "bbox": [181, 654, 633, 671]},
	{"text": "辅助检查:肺功能四项+支气管舒张实验;沙丁胺醇气雾剂支气管舒", "bbox": [138, 676, 747, 693]},
	{"text": "张实验呈阳性,FEV1.0改善41.1%。", "bbox": [177, 700, 491, 717]},
	{"text": "初步诊断:门诊诊断:1.支气管哮喘。", "bbox": [135, 722, 471, 739]},
	{"text": "-1-", "bbox": [428, 780, 475, 792]}
]
2026-08-10 06:22:09,602 INFO     29 [qwen-vl-text] coord API: raw_items=27, valid_items=27, elapsed=11.3s
2026-08-10 06:22:09,602 INFO     29 [qwen-vl-text] coord item[0]: text=渑池县人民医院, bbox=[357, 209, 550, 230]
2026-08-10 06:22:09,602 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[378, 237, 530, 257]
2026-08-10 06:22:09,602 INFO     29 [qwen-vl-text] coord item[2]: text=姓名:, bbox=[171, 264, 216, 279]
2026-08-10 06:22:09,602 INFO     29 [qwen-vl-text] coord item[3]: text=门诊号: 613003, bbox=[453, 264, 583, 278]
2026-08-10 06:22:09,602 INFO     29 [qwen-vl-text] coord item[4]: text=就诊时间:2025-05-27 14:24 科别: 呼吸与危重症医学科门诊, bbox=[170, 295, 687, 309]
2026-08-10 06:22:09,602 INFO     29 [qwen-vl-text] coord item[5]: text=姓名, bbox=[167, 323, 204, 337]
2026-08-10 06:22:09,602 INFO     29 [qwen-vl-text] coord item[6]: text=性别:男 年龄:56岁 婚否:已婚, bbox=[300, 323, 643, 337]
2026-08-10 06:22:09,602 INFO     29 [qwen-vl-text] coord item[7]: text=职业:农民 工作单位:无, bbox=[166, 342, 520, 356]
2026-08-10 06:22:09,602 INFO     29 [qwen-vl-text] coord item[8]: text=联系电话: 住址:河南省三门峡市渑池县仁村乡大, bbox=[164, 360, 730, 374]
2026-08-10 06:22:09,602 INFO     29 [qwen-vl-text] coord item[9]: text=水沟村八组8号, bbox=[163, 379, 298, 393]
2026-08-10 06:22:09,602 INFO     29 [qwen-vl-text] coord item[10]: text=病史叙述者:本人 身份证号:, bbox=[161, 398, 491, 412]
2026-08-10 06:22:09,602 INFO     29 [qwen-vl-text] coord item[11]: text=过敏史:无, bbox=[159, 417, 258, 432]
2026-08-10 06:22:09,602 INFO     29 [qwen-vl-text] coord item[12]: text=主诉:发作性胸闷、气喘4天。, bbox=[159, 446, 413, 461]
2026-08-10 06:22:09,602 INFO     29 [qwen-vl-text] coord item[13]: text=现病史:患者于4天前受凉后出现胸闷、气喘,活动后加重,伴有咳, bbox=[157, 466, 733, 481]
2026-08-10 06:22:09,603 INFO     29 [qwen-vl-text] coord item[14]: text=嗽,咳痰不明显,无胸痛、发热、咯血、盗汗等,未予治疗,症, bbox=[193, 485, 744, 500]
2026-08-10 06:22:09,603 INFO     29 [qwen-vl-text] coord item[15]: text=状持续无缓解。, bbox=[192, 505, 322, 520]
2026-08-10 06:22:09,603 INFO     29 [qwen-vl-text] coord item[16]: text=既往史:平素身体良好;无特殊疾病史;否认“肝炎、结核”等病史;, bbox=[152, 525, 754, 541]
2026-08-10 06:22:09,603 INFO     29 [qwen-vl-text] coord item[17]: text=否认手术史;否认外伤史;否认输血史及献血史;否认药物及食, bbox=[190, 546, 748, 561]
2026-08-10 06:22:09,603 INFO     29 [qwen-vl-text] coord item[18]: text=物过敏史;无预防接种史, bbox=[188, 567, 412, 582]
2026-08-10 06:22:09,603 INFO     29 [qwen-vl-text] coord item[19]: text=流行病学史:无, bbox=[147, 589, 290, 605]
2026-08-10 06:22:09,603 INFO     29 [qwen-vl-text] coord item[20]: text=体格检查:体温36.7℃,脉搏80次/分,呼吸22次/分,, bbox=[144, 610, 607, 627]
2026-08-10 06:22:09,603 INFO     29 [qwen-vl-text] coord item[21]: text=血压132/80mmHg,双肺呼吸音粗,可闻及哮鸣音,未闻及, bbox=[245, 631, 754, 648]
2026-08-10 06:22:09,603 INFO     29 [qwen-vl-text] coord item[22]: text=明显湿性啰音,心率80次/分,未闻及病理性杂音。, bbox=[181, 654, 633, 671]
2026-08-10 06:22:09,603 INFO     29 [qwen-vl-text] coord item[23]: text=辅助检查:肺功能四项+支气管舒张实验;沙丁胺醇气雾剂支气管舒, bbox=[138, 676, 747, 693]
2026-08-10 06:22:09,603 INFO     29 [qwen-vl-text] coord item[24]: text=张实验呈阳性,FEV1.0改善41.1%。, bbox=[177, 700, 491, 717]
2026-08-10 06:22:09,603 INFO     29 [qwen-vl-text] coord item[25]: text=初步诊断:门诊诊断:1.支气管哮喘。, bbox=[135, 722, 471, 739]
2026-08-10 06:22:09,603 INFO     29 [qwen-vl-text] coord item[26]: text=-1-, bbox=[428, 780, 475, 792]
2026-08-10 06:22:09,603 INFO     29 [qwen-vl-text] page=0 — 27/27 coords, api_time=11.3s
2026-08-10 06:22:09,606 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1603850, prompt_len=710
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共8行）
["渑池县人民医院", "门诊病历", "姓名：", "门诊号", "处理意见：1.避免受凉，避免进食刺激性食物，避免接触刺激性气味；", "2.如有不适，及时就医。", "经治医师：", "2"]

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
2026-08-10 06:22:13,140 INFO     29 [qwen-vl-text] coord API raw response (len=441):
```json
[
	{"text": "渑池县人民医院", "bbox": [399, 233, 583, 251]},
	{"text": "门诊病历", "bbox": [418, 258, 564, 278]},
	{"text": "姓名：", "bbox": [223, 286, 265, 299]},
	{"text": "门诊号", "bbox": [490, 285, 542, 299]},
	{"text": "处理意见：1.避免受凉，避免进食刺激性食物，避免接触刺激性气味；", "bbox": [220, 315, 766, 329]},
	{"text": "2.如有不适，及时就医。", "bbox": [308, 334, 498, 347]},
	{"text": "经治医师：", "bbox": [508, 357, 638, 373]},
	{"text": "2", "bbox": [479, 780, 492, 791]}
]
```
2026-08-10 06:22:13,140 INFO     29 [qwen-vl-text] coord API: raw_items=8, valid_items=8, elapsed=3.5s
2026-08-10 06:22:13,140 INFO     29 [qwen-vl-text] coord item[0]: text=渑池县人民医院, bbox=[399, 233, 583, 251]
2026-08-10 06:22:13,141 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[418, 258, 564, 278]
2026-08-10 06:22:13,141 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[223, 286, 265, 299]
2026-08-10 06:22:13,141 INFO     29 [qwen-vl-text] coord item[3]: text=门诊号, bbox=[490, 285, 542, 299]
2026-08-10 06:22:13,141 INFO     29 [qwen-vl-text] coord item[4]: text=处理意见：1.避免受凉，避免进食刺激性食物，避免接触刺激性气味；, bbox=[220, 315, 766, 329]
2026-08-10 06:22:13,141 INFO     29 [qwen-vl-text] coord item[5]: text=2.如有不适，及时就医。, bbox=[308, 334, 498, 347]
2026-08-10 06:22:13,141 INFO     29 [qwen-vl-text] coord item[6]: text=经治医师：, bbox=[508, 357, 638, 373]
2026-08-10 06:22:13,141 INFO     29 [qwen-vl-text] coord item[7]: text=2, bbox=[479, 780, 492, 791]
2026-08-10 06:22:13,141 INFO     29 [qwen-vl-text] page=1 — 8/8 coords, api_time=3.5s
2026-08-10 06:22:13,141 INFO     29 [qwen-vl-text] new_positions (35):
[[0, 212.415, 327.25, 175.97799999999998, 193.66], [0, 224.91, 315.34999999999997, 199.554, 216.394], [0, 101.74499999999999, 128.51999999999998, 222.28799999999998, 234.91799999999998], [0, 269.53499999999997, 346.885, 222.28799999999998, 234.076], [0, 101.14999999999999, 408.765, 248.39, 260.178], [0, 99.365, 121.38, 271.966, 283.75399999999996], [0, 178.5, 382.585, 271.966, 283.75399999999996], [0, 98.77, 309.4, 287.964, 299.752], [0, 97.58, 434.34999999999997, 303.12, 314.908], [0, 96.985, 177.31, 319.118, 330.906], [0, 95.795, 292.145, 335.116, 346.904], [0, 94.60499999999999, 153.51, 351.114, 363.74399999999997], [0, 94.60499999999999, 245.73499999999999, 375.532, 388.162], [0, 93.41499999999999, 436.135, 392.372, 405.002], [0, 114.835, 442.68, 408.37, 421.0], [0, 114.24, 191.59, 425.21, 437.84], [0, 90.44, 448.63, 442.05, 455.522], [0, 113.05, 445.06, 459.73199999999997, 472.36199999999997], [0, 111.86, 245.14, 477.414, 490.044], [0, 87.46499999999999, 172.54999999999998, 495.938, 509.40999999999997], [0, 85.67999999999999, 361.16499999999996, 513.62, 527.934], [0, 145.775, 448.63, 531.302, 545.616], [0, 107.695, 376.635, 550.668, 564.982], [0, 82.11, 444.465, 569.192, 583.506], [0, 105.315, 292.145, 589.4, 603.7139999999999], [0, 80.325, 280.245, 607.924, 622.2379999999999], [0, 254.66, 282.625, 656.76, 666.864], [1, 237.405, 346.885, 196.186, 211.34199999999998], [1, 248.70999999999998, 335.58, 217.236, 234.076], [1, 132.685, 157.67499999999998, 240.81199999999998, 251.75799999999998], [1, 291.55, 322.49, 239.97, 251.75799999999998], [1, 130.9, 455.77, 265.23, 277.018], [1, 183.26, 296.31, 281.228, 292.174], [1, 302.26, 379.60999999999996, 300.594, 314.066], [1, 285.005, 292.74, 656.76, 666.0219999999999]]
2026-08-10 06:22:13,141 INFO     29 [qwen-vl-text] ═══ DONE ═══ 35 positions, pages=2, time=17.6s
2026-08-10 06:22:13,148 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 06:22:13,148 INFO     29 [Trace] task=abd585c0 | doc=LTSH 三门峡.pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "441 items", "markdown": "", "text": "", "name": "LTSH 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:22:13,148 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 06:22:13,155 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:22:13,155 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:22:14,557 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:22:14,567 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 06:22:14,568 INFO     29 [Trace] task=abd585c0 | doc=LTSH 三门峡.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "441 items", "markdown": "", "text": "", "name": "LTSH 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:22:14,568 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 06:22:14,579 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:22:14,580 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:22:15,100 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:22:15,108 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 06:22:15,108 INFO     29 [Trace] task=abd585c0 | doc=LTSH 三门峡.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "441 items", "markdown": "", "text": "", "name": "LTSH 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:22:15,108 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 06:22:15,116 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:22:15,117 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:22:15,845 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:22:15,856 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 06:22:15,856 INFO     29 [Trace] task=abd585c0 | doc=LTSH 三门峡.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "441 items", "markdown": "", "text": "", "name": "LTSH 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:22:15,856 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 06:22:15,869 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:22:15,869 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:22:16,371 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:22:16,382 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 06:22:16,382 INFO     29 [Trace] task=abd585c0 | doc=LTSH 三门峡.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "441 items", "markdown": "", "text": "", "name": "LTSH 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:22:16,382 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 06:22:16,389 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 06:22:16,390 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:22:16,390 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 06:22:16,391 INFO     29 [qwen-vl-text] positions(406): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 06:22:16,392 INFO     29 [qwen-vl-text] page grouping: [2, 3, 4], lines per page: [194, 147, 65]
2026-08-10 06:22:16,714 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 06:22:16,941 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 06:22:17,253 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 06:22:17,254 INFO     29 [qwen-vl-text] LLM extraction start, text_len=3121
2026-08-10 06:22:17,254 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:22:17,255 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 35, \"bbox_end\": 440, \"encounter_dates\": [\"2025-04-25\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "JAEGE R PCMED\n渑池县人民医院\n肺功能检查报告\n综合测试\n姓名：\n性别：男\n年龄：56 Years\n身高：165 cm\n体重：70 kg\n备注：\n联系电话：\n住院号：0\n测试号：\n吸烟史：\n既往史：\n职业：\n测试日期\n测试时间\n预计值\n实测值\n实/预\nVC MAX\n[L]\n3.85\n2.72\n70.6\nFVC\n[L]\n3.71\n2.68\n72.2\nMV\n[L/min]\n10.00\n18.75\n187.5\nFEV 1\n[L]\n2.98\n1.10\n36.9\nFEV 1 % FVC\n[%]\n83.77\n41.10\n49.1\nPEF\n[L/s]\n7.87\n2.33\n29.6\nMEF 75\n[L/s]\n6.92\n0.96\n13.9\nMEF 50\n[L/s]\n4.17\n0.52\n12.5\nMEF 25\n[L/s]\n1.51\n0.22\n14.3\nMMEF 75/25\n[L/s]\n3.49\n0.44\n12.6\nMVV\n[L/min]\n113.25\n52.56\n46.4\nTLC-SB\n[L]\n6.10\n5.24\n85.9\nRV-SB\n[L]\n2.16\n2.69\n124.4\nRV%TLC-SB\n[%]\n35.80\n51.32\n143.4\nFRC-SB\n[L]\n3.28\n3.71\n113.3\nFRC%TLC-SB\n[%]\n55.56\n70.79\n127.4\nDLCO SB [mmol/min/kPa]\n8.61\n7.20\n83.7\nDLCO/Va mmol/min/kPa/L]\n1.41\n1.42\n100.4\nHb\n[g/100ml]\n14.60\nVA\n[L]\n5.95\n5.09\n85.5\nDLCOc SB [mmol/min/kPa]\n8.61\n7.20\n83.7\nDLCOc/Va mmol/min/kPa/L]\n1.41\n1.42\n100.4\nVIN\n[L]\n3.85\n2.55\n66.3\nInsp. time\n[s]\n1.52\nExp. time\n[s]\n2.15\nSample vol\n[L]\nSystem dead space [ml]\n172.00\nAnatom. dead space[ml]\n154.00\nTA\n[s]\n11.54\n测试结果：\nTLC\n6\nVol [L]\nFRCoeth\n25/4/25\n9:19:05上\nRW\nTime [min]\nPredAdt.0\n0.2\n0.4\n0.6\n0.8\n1.0\nFlow [L/s]\nF/V ex\n10\n5\n0\n2\n4\n6\nF/V in\n10\nVol [L]\nVol [L]\n100\n10\n50\nTime [s]\n0\n2\n4\n6\n8\n10\nVolume [L]\n4\n2\n0\n1\n4\nTime [s]\n0\n10\n20\n30\n40\nJAEGE R PCMED\n渑池县人民医院\n肺功能检查报告\n舒张试验\n姓名：\n科别：\n住院号：0\n测试号：2025042503\n性别：男\n年龄：56 Years\n身高：165 cm\n体重：70 kg\n标准体重：108 %\n体表面积：1.77 m\n吸烟史：\nFlow [L/s]\nF/V ex\nVol%VCmax\nVol [L]\n10\n20\n40\n60\n2\n80\n100\nVCmax\n1\n0\n2\n3\n4\n5\n6\n7\n1\n2\n4\n5\n6\n7\n8\n10\nTime [s]\nF/V in\n8\n0\n1\n2\n3\n4\n5\n6\n7\n8\n预计值\n前次\n前/预\n后次\n后/预\n改善率\n测试日期\n25/4/25\n25/4/25\n测试时间\n9:19:05\n9:43:24\nVC MAX\n[L]\n3.85\n2.72\n70.6\n3.07\n79.9\n13.2\nFVC\n[L]\n3.71\n2.68\n72.2\n3.05\n82.4\n14.1\nFEV 1\n[L]\n2.98\n1.10\n36.9\n1.55\n52.1\n41.1\nFEV 1 % FVC\n[%]\n83.77\n41.10\n49.1\n50.82\n60.7\n23.6\nFEV 1 % VC MAX\n[%]\n77.13\n40.51\n52.5\n50.49\n65.5\n24.6\nPEF\n[L/s]\n7.87\n2.33\n29.6\n3.18\n40.4\n36.6\nMEF 75\n[L/s]\n6.92\n0.96\n13.9\n1.65\n23.9\n72.1\nMEF 50\n[L/s]\n4.17\n0.52\n12.5\n0.85\n20.3\n63.0\nMEF 25\n[L/s]\n1.51\n0.22\n14.3\n0.35\n23.2\n62.9\nMMEF 75/25\n[L/s]\n3.49\n0.44\n12.6\n0.75\n21.3\n69.5\nJAEGER PCMED\n渑池县人民医院\n肺功能检查报告\n常规通气\n姓名：\n住院号：0\n性别：男\n身高：165 cm\n标准体重：108 %\n吸烟史：\n科别：\n测试号：2025042503\n年龄：56 Years\n体重：70 kg\n体表面积：1.77 m\n预计值 实测值 实测/预\n测试日期 25/4/25\n测试时间 9:19:05]\nVC MAX [L] 3.85 2.72 70.6\nIRV [L] 0.91\nERV [L] 1.11 1.02 91.8\nIC [L] 2.74 1.69 61.9\nVT [L] 0.50 0.78 156.7\nMV [L/min] 10.00 18.75 187.5\nVC IN [L] 3.85 2.69 70.0\nVC EX [L] 3.85 2.72 70.6\nBF [1/min] 20.00 23.93 119.7\nFVC [L] 3.71 2.68 72.2\nPEF [L/s] 7.87 2.33 29.6\nFEV 0.5 [L] 0.70\nFEV 1 [L] 2.98 1.10 36.9\nFEV 2 [L] 1.60\nFEV 3 [L] 1.91\nFEV6 [L] 2.45\nFEF 200-1200 [L/s] 0.94\nFEV 1 % FVC [%] 83.77 41.10 49.1\nFEV 1 % VC MAX [%] 77.13 40.51 52.5\nMEF 75 [L/s] 6.92 0.96 13.9\nMEF 50 [L/s] 4.17 0.52 12.5\nMEF 25 [L/s] 1.51 0.22 14.3\nMMEF 75/25 [L/s] 3.49 0.44 12.6\nFEF 75/85 [L/s] 0.77 0.18 23.0\nFEF50 % FIF50 [%] 38.63\nPIF [L/s] 1.41\nFVC IN [L] 3.85 2.69 70.0\nFET [s] 7.87\nFIF 50 [L/s] 1.35\nFIV1 [L] 1.10\nFIV1 % FVC [%] 40.89\nT IN [s] 1.21\nT EX [s] 1.30\nT TOT [s] 2.51\nMIF [L/s] 0.65\nMEF [L/s] 0.60\nMVV [L/min] 113.25 52.56 46.4\nFEF50 % FIF50 [%] 38.63\nV backextrapolation ex [L] 0.02\nV backextrapol. % FVC [%] 0.75\n测试结果\n1、重度阻塞性肺通气功能障碍，小气道功能降低。\n2、肺弥散功能正常。\n3、残气量正常，残气量/肺总量增高。\n4、沙丁胺醇气雾剂支气管舒张试验呈阳性，FEV1.0改41.1%。\n5、建议定期复查。\n报告医师：李朝红/崔艳芳 报告日期：2025.4.25",
    "role": "user"
  }
]
2026-08-10 06:22:28,431 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T06:22:28.430+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 4, "failed": 0, "current": {"abd585c0948311f1bd9827cf206dfa2d": {"id": "abd585c0948311f1bd9827cf206dfa2d", "doc_id": "ab76d5fc948311f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LTSH \u4e09\u95e8\u5ce1.pdf", "type": "pdf", "location": "LTSH \u4e09\u95e8\u5ce1.pdf", "size": 6636575, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786342866974, "task_type": "dataflow", "root_trace_id": "bcc06c371b5649ffa23cad2dd92769a3", "root_traceparent": "00-bcc06c371b5649ffa23cad2dd92769a3-aca0c6f6ccf15910-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 06:22:58,515 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T06:22:58.513+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 4, "failed": 0, "current": {"abd585c0948311f1bd9827cf206dfa2d": {"id": "abd585c0948311f1bd9827cf206dfa2d", "doc_id": "ab76d5fc948311f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LTSH \u4e09\u95e8\u5ce1.pdf", "type": "pdf", "location": "LTSH \u4e09\u95e8\u5ce1.pdf", "size": 6636575, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786342866974, "task_type": "dataflow", "root_trace_id": "bcc06c371b5649ffa23cad2dd92769a3", "root_traceparent": "00-bcc06c371b5649ffa23cad2dd92769a3-aca0c6f6ccf15910-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 06:23:17,145 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:23:17,145 INFO     29 [qwen-vl-text] LLM output (len=3958):
{
  "exam_date": "2025-04-25",
  "report_date": "2025-04-25",
  "exam_name": "肺功能检查",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "综合测试\n测试日期: 25/4/25\n测试时间: 9:19:05\n\n| 指标 | 预计值 | 实测值 | 实/预 | 单位 |\n| :--- | :--- | :--- | :--- | :--- |\n| VC MAX | 3.85 | 2.72 | 70.6 | L |\n| FVC | 3.71 | 2.68 | 72.2 | L |\n| MV | 10.00 | 18.75 | 187.5 | L/min |\n| FEV 1 | 2.98 | 1.10 | 36.9 | L |\n| FEV 1 % FVC | 83.77 | 41.10 | 49.1 | % |\n| PEF | 7.87 | 2.33 | 29.6 | L/s |\n| MEF 75 | 6.92 | 0.96 | 13.9 | L/s |\n| MEF 50 | 4.17 | 0.52 | 12.5 | L/s |\n| MEF 25 | 1.51 | 0.22 | 14.3 | L/s |\n| MMEF 75/25 | 3.49 | 0.44 | 12.6 | L/s |\n| MVV | 113.25 | 52.56 | 46.4 | L/min |\n| TLC-SB | 6.10 | 5.24 | 85.9 | L |\n| RV-SB | 2.16 | 2.69 | 124.4 | L |\n| RV%TLC-SB | 35.80 | 51.32 | 143.4 | % |\n| FRC-SB | 3.28 | 3.71 | 113.3 | L |\n| FRC%TLC-SB | 55.56 | 70.79 | 127.4 | % |\n| DLCO SB | 8.61 | 7.20 | 83.7 | mmol/min/kPa |\n| DLCO/Va | 1.41 | 1.42 | 100.4 | mmol/min/kPa/L |\n| Hb | 14.60 | - | - | g/100ml |\n| VA | 5.95 | 5.09 | 85.5 | L |\n| DLCOc SB | 8.61 | 7.20 | 83.7 | mmol/min/kPa |\n| DLCOc/Va | 1.41 | 1.42 | 100.4 | mmol/min/kPa/L |\n| VIN | 3.85 | 2.55 | 66.3 | L |\n| Insp. time | - | 1.52 | - | s |\n| Exp. time | - | 2.15 | - | s |\n| System dead space | - | 172.00 | - | ml |\n| Anatom. dead space | - | 154.00 | - | ml |\n| TA | - | 11.54 | - | s |\n\n舒张试验\n测试日期: 25/4/25\n测试时间: 9:19:05 (前次), 9:43:24 (后次)\n\n| 指标 | 预计值 | 前次实测 | 前/预 | 后次实测 | 后/预 | 改善率 | 单位 |\n| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n| VC MAX | 3.85 | 2.72 | 70.6 | 3.07 | 79.9 | 13.2 | L |\n| FVC | 3.71 | 2.68 | 72.2 | 3.05 | 82.4 | 14.1 | L |\n| FEV 1 | 2.98 | 1.10 | 36.9 | 1.55 | 52.1 | 41.1 | L |\n| FEV 1 % FVC | 83.77 | 41.10 | 49.1 | 50.82 | 60.7 | 23.6 | % |\n| FEV 1 % VC MAX | 77.13 | 40.51 | 52.5 | 50.49 | 65.5 | 24.6 | % |\n| PEF | 7.87 | 2.33 | 29.6 | 3.18 | 40.4 | 36.6 | L/s |\n| MEF 75 | 6.92 | 0.96 | 13.9 | 1.65 | 23.9 | 72.1 | L/s |\n| MEF 50 | 4.17 | 0.52 | 12.5 | 0.85 | 20.3 | 63.0 | L/s |\n| MEF 25 | 1.51 | 0.22 | 14.3 | 0.35 | 23.2 | 62.9 | L/s |\n| MMEF 75/25 | 3.49 | 0.44 | 12.6 | 0.75 | 21.3 | 69.5 | L/s |\n\n常规通气\n测试日期: 25/4/25\n测试时间: 9:19:05\n\n| 指标 | 预计值 | 实测值 | 实测/预 | 单位 |\n| :--- | :--- | :--- | :--- | :--- |\n| VC MAX | 3.85 | 2.72 | 70.6 | L |\n| IRV | 0.91 | - | - | L |\n| ERV | 1.11 | 1.02 | 91.8 | L |\n| IC | 2.74 | 1.69 | 61.9 | L |\n| VT | 0.50 | 0.78 | 156.7 | L |\n| MV | 10.00 | 18.75 | 187.5 | L/min |\n| VC IN | 3.85 | 2.69 | 70.0 | L |\n| VC EX | 3.85 | 2.72 | 70.6 | L |\n| BF | 20.00 | 23.93 | 119.7 | 1/min |\n| FVC | 3.71 | 2.68 | 72.2 | L |\n| PEF | 7.87 | 2.33 | 29.6 | L/s |\n| FEV 0.5 | 0.70 | - | - | L |\n| FEV 1 | 2.98 | 1.10 | 36.9 | L |\n| FEV 2 | 1.60 | - | - | L |\n| FEV 3 | 1.91 | - | - | L |\n| FEV6 | 2.45 | - | - | L |\n| FEF 200-1200 | 0.94 | - | - | L/s |\n| FEV 1 % FVC | 83.77 | 41.10 | 49.1 | % |\n| FEV 1 % VC MAX | 77.13 | 40.51 | 52.5 | % |\n| MEF 75 | 6.92 | 0.96 | 13.9 | L/s |\n| MEF 50 | 4.17 | 0.52 | 12.5 | L/s |\n| MEF 25 | 1.51 | 0.22 | 14.3 | L/s |\n| MMEF 75/25 | 3.49 | 0.44 | 12.6 | L/s |\n| FEF 75/85 | 0.77 | 0.18 | 23.0 | L/s |\n| FEF50 % FIF50 | 38.63 | - | - | % |\n| PIF | 1.41 | - | - | L/s |\n| FVC IN | 3.85 | 2.69 | 70.0 | L |\n| FET | 7.87 | - | - | s |\n| FIF 50 | 1.35 | - | - | L/s |\n| FIV1 | 1.10 | - | - | L |\n| FIV1 % FVC | 40.89 | - | - | % |\n| T IN | 1.21 | - | - | s |\n| T EX | 1.30 | - | - | s |\n| T TOT | 2.51 | - | - | s |\n| MIF | 0.65 | - | - | L/s |\n| MEF | 0.60 | - | - | L/s |\n| MVV | 113.25 | 52.56 | 46.4 | L/min |\n| FEF50 % FIF50 | 38.63 | - | - | % |\n| V backextrapolation ex | 0.02 | - | - | L |\n| V backextrapol. % FVC | 0.75 | - | - | % |",
  "conclusion": "测试结果\n1、重度阻塞性肺通气功能障碍，小气道功能降低。\n2、肺弥散功能正常。\n3、残气量正常，残气量/肺总量增高。\n4、沙丁胺醇气雾剂支气管舒张试验呈阳性，FEV1.0改41.1%。\n5、建议定期复查。",
  "physician": "李朝红/崔艳芳",
  "reviewer": null
}
2026-08-10 06:23:17,150 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2543785, prompt_len=2349
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共194行）
["JAEGE R PCMED", "渑池县人民医院", "肺功能检查报告", "综合测试", "姓名：", "性别：男", "年龄：56 Years", "身高：165 cm", "体重：70 kg", "备注：", "联系电话：", "住院号：0", "测试号：", "吸烟史：", "既往史：", "职业：", "测试日期", "测试时间", "预计值", "实测值", "实/预", "VC MAX", "[L]", "3.85", "2.72", "70.6", "FVC", "[L]", "3.71", "2.68", "72.2", "MV", "[L/min]", "10.00", "18.75", "187.5", "FEV 1", "[L]", "2.98", "1.10", "36.9", "FEV 1 % FVC", "[%]", "83.77", "41.10", "49.1", "PEF", "[L/s]", "7.87", "2.33", "29.6", "MEF 75", "[L/s]", "6.92", "0.96", "13.9", "MEF 50", "[L/s]", "4.17", "0.52", "12.5", "MEF 25", "[L/s]", "1.51", "0.22", "14.3", "MMEF 75/25", "[L/s]", "3.49", "0.44", "12.6", "MVV", "[L/min]", "113.25", "52.56", "46.4", "TLC-SB", "[L]", "6.10", "5.24", "85.9", "RV-SB", "[L]", "2.16", "2.69", "124.4", "RV%TLC-SB", "[%]", "35.80", "51.32", "143.4", "FRC-SB", "[L]", "3.28", "3.71", "113.3", "FRC%TLC-SB", "[%]", "55.56", "70.79", "127.4", "DLCO SB [mmol/min/kPa]", "8.61", "7.20", "83.7", "DLCO/Va mmol/min/kPa/L]", "1.41", "1.42", "100.4", "Hb", "[g/100ml]", "14.60", "VA", "[L]", "5.95", "5.09", "85.5", "DLCOc SB [mmol/min/kPa]", "8.61", "7.20", "83.7", "DLCOc/Va mmol/min/kPa/L]", "1.41", "1.42", "100.4", "VIN", "[L]", "3.85", "2.55", "66.3", "Insp. time", "[s]", "1.52", "Exp. time", "[s]", "2.15", "Sample vol", "[L]", "System dead space [ml]", "172.00", "Anatom. dead space[ml]", "154.00", "TA", "[s]", "11.54", "测试结果：", "TLC", "6", "Vol [L]", "FRCoeth", "25/4/25", "9:19:05上", "RW", "Time [min]", "PredAdt.0", "0.2", "0.4", "0.6", "0.8", "1.0", "Flow [L/s]", "F/V ex", "10", "5", "0", "2", "4", "6", "F/V in", "10", "Vol [L]", "Vol [L]", "100", "10", "50", "Time [s]", "0", "2", "4", "6", "8", "10", "Volume [L]", "4", "2", "0", "1", "4", "Time [s]", "0", "10", "20", "30", "40"]

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
2026-08-10 06:23:58,677 INFO     29 [qwen-vl-text] coord API raw response (len=6230):
[
	{"text": "JAEGE R PCMED", "bbox": [708, 43, 896, 57]},
	{"text": "渑池县人民医院", "bbox": [380, 57, 592, 78],
	"bbox": [414, 80, 562, 97],
	"bbox": [455, 100, 541, 116],
	"bbox": [80, 119, 126, 131],
	"bbox": [80, 131, 126, 143],
	"bbox": [250, 131, 267, 143],
	"bbox": [424, 119, 507, 131],
	"bbox": [424, 131, 490, 143],
	"bbox": [80, 143, 126, 155],
	"bbox": [250, 143, 324, 155],
	"bbox": [424, 143, 490, 155],
	"bbox": [80, 155, 126, 167],
	"bbox": [250, 155, 307, 167],
	"bbox": [424, 155, 490, 167],
	"bbox": [80, 167, 126, 180],
	"bbox": [250, 167, 297, 179],
	"bbox": [424, 167, 472, 180],
	"bbox": [424, 179, 472, 191],
	"bbox": [75, 222, 159, 234],
	"bbox": [356, 210, 419, 223],
	"bbox": [468, 210, 529, 223],
	"bbox": [579, 210, 630, 223],
	"bbox": [635, 212, 656, 223],
	"bbox": [661, 210, 708, 223],
	"bbox": [75, 234, 159, 246],
	"bbox": [458, 223, 530, 234],
	"bbox": [428, 235, 531, 246],
	"bbox": [67, 259, 134, 269],
	"bbox": [272, 259, 300, 270],
	"bbox": [376, 259, 418, 269],
	"bbox": [490, 259, 531, 269],
	"bbox": [593, 259, 635, 269],
	"bbox": [639, 259, 684, 269],
	"bbox": [66, 271, 100, 281],
	"bbox": [272, 271, 300, 282],
	"bbox": [376, 271, 418, 281],
	"bbox": [490, 271, 531, 281],
	"bbox": [593, 271, 635, 281],
	"bbox": [640, 275, 656, 285],
	"bbox": [666, 271, 675, 279],
	"bbox": [63, 285, 88, 294],
	"bbox": [228, 284, 298, 296],
	"bbox": [366, 284, 418, 294],
	"bbox": [482, 284, 532, 294],
	"bbox": [585, 284, 635, 294],
	"bbox": [66, 298, 117, 308],
	"bbox": [272, 298, 298, 309],
	"bbox": [376, 298, 418, 308],
	"bbox": [490, 298, 532, 308],
	"bbox": [595, 298, 636, 308],
	"bbox": [66, 312, 182, 322],
	"bbox": [272, 312, 298, 323],
	"bbox": [366, 312, 418, 322],
	"bbox": [482, 312, 532, 322],
	"bbox": [595, 312, 636, 322],
	"bbox": [643, 312, 693, 322],
	"bbox": [717, 312, 735, 322],
	"bbox": [759, 312, 777, 322],
	"bbox": [801, 312, 819, 322],
	"bbox": [843, 312, 861, 322],
	"bbox": [885, 312, 903, 322],
	"bbox": [63, 326, 96, 336],
	"bbox": [250, 325, 298, 337],
	"bbox": [376, 325, 418, 336],
	"bbox": [490, 325, 532, 336],
	"bbox": [595, 325, 636, 336],
	"bbox": [670, 330, 722, 342],
	"bbox": [804, 330, 838, 340],
	"bbox": [63, 340, 127, 350],
	"bbox": [250, 340, 298, 351],
	"bbox": [376, 340, 418, 350],
	"bbox": [490, 340, 532, 350],
	"bbox": [595, 340, 636, 350],
	"bbox": [651, 342, 667, 352],
	"bbox": [63, 354, 127, 364],
	"bbox": [250, 354, 298, 365],
	"bbox": [376, 354, 418, 364],
	"bbox": [490, 354, 532, 364],
	"bbox": [595, 354, 636, 364],
	"bbox": [656, 364, 667, 373],
	"bbox": [63, 368, 127, 378],
	"bbox": [250, 368, 298, 379],
	"bbox": [376, 368, 418, 378],
	"bbox": [490, 368, 532, 378],
	"bbox": [595, 368, 636, 378],
	"bbox": [656, 385, 667, 394],
	"bbox": [63, 382, 172, 392],
	"bbox": [250, 382, 298, 393],
	"bbox": [376, 382, 418, 392],
	"bbox": [490, 382, 532, 392],
	"bbox": [595, 382, 636, 392],
	"bbox": [722, 393, 732, 401],
	"bbox": [779, 393, 788, 401],
	"bbox": [834, 393, 843, 401],
	"bbox": [63, 397, 98, 407],
	"bbox": [228, 396, 300, 408],
	"bbox": [356, 396, 418, 407],
	"bbox": [482, 396, 532, 407],
	"bbox": [595, 396, 636, 407],
	"bbox": [656, 404, 667, 413],
	"bbox": [66, 425, 132, 435],
	"bbox": [272, 425, 300, 436],
	"bbox": [376, 425, 418, 435],
	"bbox": [490, 425, 532, 435],
	"bbox": [595, 423, 636, 435],
	"bbox": [651, 425, 667, 435],
	"bbox": [66, 440, 122, 450],
	"bbox": [272, 440, 300, 451],
	"bbox": [376, 440, 418, 450],
	"bbox": [490, 440, 532, 450],
	"bbox": [587, 437, 636, 448],
	"bbox": [804, 435, 835, 445],
	"bbox": [66, 454, 165, 464],
	"bbox": [272, 454, 300, 465],
	"bbox": [366, 454, 418, 464],
	"bbox": [482, 454, 532, 464],
	"bbox": [587, 452, 636, 463],
	"bbox": [66, 468, 132, 478],
	"bbox": [272, 468, 300, 479],
	"bbox": [376, 468, 418, 478],
	"bbox": [490, 468, 532, 478],
	"bbox": [587, 466, 636, 477],
	"bbox": [670, 460, 707, 471],
	"bbox": [843, 458, 880, 470],
	"bbox": [66, 482, 174, 492],
	"bbox": [272, 482, 300, 493],
	"bbox": [366, 482, 418, 492],
	"bbox": [482, 480, 532, 492],
	"bbox": [587, 479, 636, 490],
	"bbox": [645, 480, 667, 490],
	"bbox": [887, 478, 903, 488],
	"bbox": [66, 496, 298, 507],
	"bbox": [376, 496, 418, 506],
	"bbox": [490, 494, 532, 505],
	"bbox": [595, 492, 636, 504],
	"bbox": [66, 510, 298, 521],
	"bbox": [376, 509, 418, 519],
	"bbox": [490, 508, 532, 519],
	"bbox": [587, 506, 636, 517],
	"bbox": [66, 525, 86, 535],
	"bbox": [208, 523, 300, 536],
	"bbox": [482, 521, 532, 532],
	"bbox": [656, 522, 670, 531],
	"bbox": [875, 511, 907, 522],
	"bbox": [63, 540, 86, 549],
	"bbox": [272, 537, 300, 549],
	"bbox": [376, 537, 418, 547],
	"bbox": [490, 535, 532, 546],
	"bbox": [600, 534, 642, 545],
	"bbox": [63, 553, 298, 564],
	"bbox": [376, 551, 418, 561],
	"bbox": [490, 550, 532, 560],
	"bbox": [600, 548, 642, 558],
	"bbox": [63, 567, 298, 578],
	"bbox": [376, 565, 418, 575],
	"bbox": [490, 564, 532, 574],
	"bbox": [590, 562, 642, 573],
	"bbox": [662, 565, 670, 573],
	"bbox": [759, 554, 803, 565],
	"bbox": [894, 562, 903, 570],
	"bbox": [672, 574, 680, 582],
	"bbox": [710, 574, 719, 582],
	"bbox": [750, 574, 758, 582],
	"bbox": [789, 574, 797, 582],
	"bbox": [828, 574, 836, 582],
	"bbox": [864, 572, 877, 580],
	"bbox": [63, 597, 96, 607],
	"bbox": [272, 595, 300, 607],
	"bbox": [376, 594, 418, 604],
	"bbox": [490, 593, 532, 604],
	"bbox": [602, 591, 644, 602],
	"bbox": [680, 593, 738, 605],
	"bbox": [666, 603, 675, 611],
	"bbox": [63, 612, 170, 623],
	"bbox": [272, 610, 300, 622],
	"bbox": [490, 607, 532, 618],
	"bbox": [63, 627, 159, 638],
	"bbox": [272, 625, 300, 637],
	"bbox": [490, 621, 532, 632],
	"bbox": [666, 623, 675, 631],
	"bbox": [63, 642, 168, 653],
	"bbox": [272, 640, 300, 652],
	"bbox": [666, 646, 675, 654],
	"bbox": [60, 656, 248, 669],
	"bbox": [260, 655, 298, 667],
	"bbox": [475, 651, 538, 662],
	"bbox": [55, 671, 298, 684],
	"bbox": [475, 666, 538, 677],
	"bbox": [666, 669, 675, 677],
	"bbox": [55, 689, 79, 699],
	"bbox": [272, 686, 298, 698],
	"bbox": [487, 680, 538, 691],
	"bbox": [672, 692, 680, 700],
	"bbox": [773, 691, 817, 703],
	"bbox": [47, 704, 170, 722],
	"bbox": [683, 712, 691, 720],
	"bbox": [728, 711, 743, 720],
	"bbox": [777, 711, 791, 720],
	"bbox": [825, 710, 840, 719],
	"bbox": [873, 709, 888, 718]
]
2026-08-10 06:23:58,678 INFO     29 [qwen-vl-text] coord JSON strict parse failed, trying json_repair
2026-08-10 06:23:58,682 INFO     29 [qwen-vl-text] coord API: raw_items=201, valid_items=2, elapsed=41.5s
2026-08-10 06:23:58,682 INFO     29 [qwen-vl-text] coord item[0]: text=JAEGE R PCMED, bbox=[708, 43, 896, 57]
2026-08-10 06:23:58,682 INFO     29 [qwen-vl-text] coord item[1]: text=渑池县人民医院, bbox=[380, 57, 592, 78]
2026-08-10 06:23:58,690 INFO     29 [qwen-vl-text] page=2 — 2/194 coords, api_time=41.5s
2026-08-10 06:23:58,692 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1660617, prompt_len=1814
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共147行）
["JAEGE R PCMED", "渑池县人民医院", "肺功能检查报告", "舒张试验", "姓名：", "科别：", "住院号：0", "测试号：2025042503", "性别：男", "年龄：56 Years", "身高：165 cm", "体重：70 kg", "标准体重：108 %", "体表面积：1.77 m", "吸烟史：", "Flow [L/s]", "F/V ex", "Vol%VCmax", "Vol [L]", "10", "20", "40", "60", "2", "80", "100", "VCmax", "1", "0", "2", "3", "4", "5", "6", "7", "1", "2", "4", "5", "6", "7", "8", "10", "Time [s]", "F/V in", "8", "0", "1", "2", "3", "4", "5", "6", "7", "8", "预计值", "前次", "前/预", "后次", "后/预", "改善率", "测试日期", "25/4/25", "25/4/25", "测试时间", "9:19:05", "9:43:24", "VC MAX", "[L]", "3.85", "2.72", "70.6", "3.07", "79.9", "13.2", "FVC", "[L]", "3.71", "2.68", "72.2", "3.05", "82.4", "14.1", "FEV 1", "[L]", "2.98", "1.10", "36.9", "1.55", "52.1", "41.1", "FEV 1 % FVC", "[%]", "83.77", "41.10", "49.1", "50.82", "60.7", "23.6", "FEV 1 % VC MAX", "[%]", "77.13", "40.51", "52.5", "50.49", "65.5", "24.6", "PEF", "[L/s]", "7.87", "2.33", "29.6", "3.18", "40.4", "36.6", "MEF 75", "[L/s]", "6.92", "0.96", "13.9", "1.65", "23.9", "72.1", "MEF 50", "[L/s]", "4.17", "0.52", "12.5", "0.85", "20.3", "63.0", "MEF 25", "[L/s]", "1.51", "0.22", "14.3", "0.35", "23.2", "62.9", "MMEF 75/25", "[L/s]", "3.49", "0.44", "12.6", "0.75", "21.3", "69.5"]

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
2026-08-10 06:25:04,047 INFO     29 [qwen-vl-text] coord API raw response (len=11282):
[
	{"text": "JAEGE R PCMED", "bbox": [696, 38, 875, 54]},
	{"text": "渑池县人民医院", "bbox": [361, 50, 588, 69]},
	{"text": "肺功能检查报告", "bbox": [375, 74, 565, 92]},
	{"text": "舒张试验", "bbox": [420, 97, 513, 115]},
	{"text": "姓名：", "bbox": [67, 115, 118, 128]},
	{"text": "科别：", "bbox": [440, 118, 489, 131]},
	{"text": "住院号：", "bbox": [67, 128, 138, 141]},
	{"text": "0", "bbox": [251, 131, 260, 141]},
	{"text": "测试号：", "bbox": [440, 131, 508, 144]},
	{"text": "2025042503", "bbox": [615, 133, 711, 144]},
	{"text": "性别：", "bbox": [67, 141, 118, 154]},
	{"text": "男", "bbox": [252, 142, 271, 154]},
	{"text": "年龄：", "bbox": [440, 144, 489, 157]},
	{"text": "56 Years", "bbox": [615, 146, 692, 157]},
	{"text": "身高：", "bbox": [67, 154, 118, 167]},
	{"text": "165 cm", "bbox": [252, 156, 314, 167]},
	{"text": "体重：", "bbox": [440, 157, 489, 170]},
	{"text": "70 kg", "bbox": [615, 158, 663, 170]},
	{"text": "标准体重：", "bbox": [67, 167, 160, 180]},
	{"text": "108 %", "bbox": [252, 169, 314, 180]},
	{"text": "体表面积：", "bbox": [440, 170, 526, 183]},
	{"text": "1.77 m", "bbox": [615, 171, 674, 183]},
	{"text": "吸烟史：", "bbox": [67, 180, 141, 193]},
	{"text": "Flow [L/s]", "bbox": [104, 230, 161, 242]},
	{"text": "F/V ex", "bbox": [324, 232, 362, 242]},
	{"text": "Vol%VCmax", "bbox": [487, 228, 550, 238]},
	{"text": "0", "bbox": [504, 238, 514, 247]},
	{"text": "0", "bbox": [520, 238, 529, 247]},
	{"text": "Vol [L]", "bbox": [535, 241, 570, 254]},
	{"text": "10", "bbox": [84, 250, 100, 260]},
	{"text": "20", "bbox": [498, 250, 514, 260]},
	{"text": "40", "bbox": [498, 261, 514, 271]},
	{"text": "60", "bbox": [498, 273, 514, 283]},
	{"text": "2", "bbox": [522, 275, 532, 285]},
	{"text": "5", "bbox": [89, 280, 99, 290]},
	{"text": "80", "bbox": [498, 285, 514, 295]},
	{"text": "100", "bbox": [494, 295, 514, 305]},
	{"text": "VCmax", "bbox": [550, 292, 588, 302]},
	{"text": "1", "bbox": [453, 307, 467, 317], "bbox": [453, 307, 467, 317]},
	{"text": "1", "bbox": [820, 305, 845, 315], "bbox": [820, 305, 845, 315]},
	{"text": "0", "bbox": [90, 312, 100, 322], "bbox": [90, 312, 100, 322]},
	{"text": "1", "bbox": [147, 322, 155, 332], "bbox": [147, 322, 155, 332]},
	{"text": "2", "bbox": [191, 322, 201, 332], "bbox": [191, 322, 201, 332]},
	{"text": "3", "bbox": [238, 322, 247, 332], "bbox": [238, 322, 247, 332]},
	{"text": "4", "bbox": [283, 322, 292, 332], "bbox": [283, 322, 292, 332]},
	{"text": "5", "bbox": [328, 322, 337, 332], "bbox": [328, 322, 337, 332]},
	{"text": "6", "bbox": [372, 322, 381, 332], "bbox": [372, 322, 381, 332]},
	{"text": "7", "bbox": [415, 322, 424, 332], "bbox": [415, 322, 424, 332]},
	{"text": "2", "bbox": [453, 319, 467, 329], "bbox": [453, 319, 467, 329]},
	{"text": "2", "bbox": [820, 315, 845, 325], "bbox": [820, 315, 845, 325]},
	{"text": "4", "bbox": [523, 313, 532, 322], "bbox": [523, 313, 532, 322]},
	{"text": "5", "bbox": [93, 345, 103, 355], "bbox": [93, 345, 103, 355]},
	{"text": "6", "bbox": [523, 352, 532, 361], "bbox": [523, 352, 532, 361]},
	{"text": "10", "bbox": [90, 376, 107, 386], "bbox": [90, 376, 107, 386]},
	{"text": "Time [s]", "bbox": [666, 378, 709, 389], "bbox": [666, 378, 709, 389]},
	{"text": "F/V in", "bbox": [335, 395, 368, 405], "bbox": [335, 395, 368, 405]},
	{"text": "8", "bbox": [525, 390, 534, 399], "bbox": [525, 390, 534, 399]},
	{"text": "0", "bbox": [535, 399, 544, 408], "bbox": [535, 399, 544, 408]},
	{"text": "1", "bbox": [572, 399, 579, 408], "bbox": [572, 399, 579, 408]},
	{"text": "2", "bbox": [608, 399, 617, 408], "bbox": [608, 399, 617, 408]},
	{"text": "3", "bbox": [645, 399, 654, 408], "bbox": [645, 399, 654, 408]},
	{"text": "4", "bbox": [683, 399, 692, 408], "bbox": [683, 399, 692, 408]},
	{"text": "5", "bbox": [720, 399, 729, 408], "bbox": [720, 399, 729, 408]},
	{"text": "6", "bbox": [758, 399, 767, 408], "bbox": [758, 399, 767, 408]},
	{"text": "7", "bbox": [796, 399, 805, 408], "bbox": [796, 399, 805, 408]},
	{"text": "8", "bbox": [834, 396, 843, 405], "bbox": [834, 396, 843, 405]},
	{"text": "预计值", "bbox": [378, 416, 438, 429], "bbox": [378, 416, 438, 429]},
	{"text": "前次", "bbox": [484, 416, 521, 429], "bbox": [484, 416, 521, 429]},
	{"text": "前/预", "bbox": [557, 415, 605, 428], "bbox": [557, 415, 605, 428]},
	{"text": "后次", "bbox": [650, 414, 689, 427], "bbox": [650, 414, 689, 427]},
	{"text": "后/预", "bbox": [724, 412, 773, 425], "bbox": [724, 412, 773, 425]},
	{"text": "改善率", "bbox": [800, 410, 857, 423], "bbox": [800, 410, 857, 423]},
	{"text": "测试日期", "bbox": [90, 432, 171, 445], "bbox": [90, 432, 171, 445]},
	{"text": "25/4/25", "bbox": [455, 430, 521, 441], "bbox": [455, 430, 521, 441]},
	{"text": "25/4/25", "bbox": [622, 428, 689, 439], "bbox": [622, 428, 689, 439]},
	{"text": "测试时间", "bbox": [90, 445, 171, 458], "bbox": [90, 445, 171, 458]},
	{"text": "9:19:05", "bbox": [448, 442, 521, 454], "bbox": [448, 442, 521, 454]},
	{"text": "9:43:24", "bbox": [615, 440, 689, 452], "bbox": [615, 440, 689, 452]},
	{"text": "VC MAX", "bbox": [94, 472, 157, 482], "bbox": [94, 472, 157, 482]},
	{"text": "[L]", "bbox": [327, 470, 352, 481], "bbox": [327, 470, 352, 481]},
	{"text": "3.85", "bbox": [401, 469, 439, 480], "bbox": [401, 469, 439, 480]},
	{"text": "2.72", "bbox": [485, 468, 521, 479], "bbox": [485, 468, 521, 479]},
	{"text": "70.6", "bbox": [568, 467, 605, 477], "bbox": [568, 467, 605, 477]},
	{"text": "3.07", "bbox": [652, 465, 689, 476], "bbox": [652, 465, 689, 476]},
	{"text": "79.9", "bbox": [735, 464, 773, 475], "bbox": [735, 464, 773, 475]},
	{"text": "13.2", "bbox": [820, 462, 857, 473], "bbox": [820, 462, 857, 473]},
	{"text": "FVC", "bbox": [94, 485, 127, 495], "bbox": [94, 485, 127, 495]},
	{"text": "[L]", "bbox": [327, 483, 352, 494], "bbox": [327, 483, 352, 494]},
	{"text": "3.71", "bbox": [401, 481, 439, 492], "bbox": [401, 481, 439, 492]},
	{"text": "2.68", "bbox": [485, 480, 521, 491], "bbox": [485, 480, 521, 491]},
	{"text": "72.2", "bbox": [568, 478, 605, 489], "bbox": [568, 478, 605, 489]},
	{"text": "3.05", "bbox": [652, 477, 689, 488], "bbox": [652, 477, 689, 488]},
	{"text": "82.4", "bbox": [735, 476, 773, 487], "bbox": [735, 476, 773, 487]},
	{"text": "14.1", "bbox": [820, 475, 857, 485], "bbox": [820, 475, 857, 485]},
	{"text": "FEV 1", "bbox": [94, 498, 145, 508], "bbox": [94, 498, 145, 508]},
	{"text": "[L]", "bbox": [327, 496, 352, 507], "bbox": [327, 496, 352, 507]},
	{"text": "2.98", "bbox": [401, 494, 439, 505], "bbox": [401, 494, 439, 505]},
	{"text": "1.10", "bbox": [485, 493, 521, 504], "bbox": [485, 493, 521, 504]},
	{"text": "36.9", "bbox": [568, 491, 605, 502], "bbox": [568, 491, 605, 502]},
	{"text": "1.55", "bbox": [652, 490, 689, 500], "bbox": [652, 490, 689, 500]},
	{"text": "52.1", "bbox": [735, 488, 773, 499], "bbox": [735, 488, 773, 499]},
	{"text": "41.1", "bbox": [820, 487, 857, 498], "bbox": [820, 487, 857, 498]},
	{"text": "FEV 1 % FVC", "bbox": [94, 510, 207, 520], "bbox": [94, 510, 207, 520]},
	{"text": "[%]", "bbox": [327, 508, 352, 519], "bbox": [327, 508, 352, 519]},
	{"text": "83.77", "bbox": [392, 506, 439, 517], "bbox": [392, 506, 439, 517]},
	{"text": "41.10", "bbox": [477, 505, 521, 516], "bbox": [477, 505, 521, 516]},
	{"text": "49.1", "bbox": [568, 504, 605, 515], "bbox": [568, 504, 605, 515]},
	{"text": "50.82", "bbox": [645, 502, 689, 513], "bbox": [645, 502, 689, 513]},
	{"text": "60.7", "bbox": [735, 501, 773, 512], "bbox": [735, 501, 773, 512]},
	{"text": "23.6", "bbox": [820, 499, 857, 510], "bbox": [820, 499, 857, 510]},
	{"text": "FEV 1 % VC MAX", "bbox": [94, 523, 238, 533], "bbox": [94, 523, 238, 533]},
	{"text": "[%]", "bbox": [327, 521, 352, 532], "bbox": [327, 521, 352, 532]},
	{"text": "77.13", "bbox": [392, 519, 439, 530], "bbox": [392, 519, 439, 530]},
	{"text": "40.51", "bbox": [477, 518, 521, 529], "bbox": [477, 518, 521, 529]},
	{"text": "52.5", "bbox": [568, 516, 605, 527], "bbox": [568, 516, 605, 527]},
	{"text": "50.49", "bbox": [645, 514, 689, 525], "bbox": [645, 514, 689, 525]},
	{"text": "65.5", "bbox": [735, 513, 773, 524], "bbox": [735, 513, 773, 524]},
	{"text": "24.6", "bbox": [820, 512, 857, 523], "bbox": [820, 512, 857, 523]},
	{"text": "PEF", "bbox": [94, 537, 127, 547], "bbox": [94, 537, 127, 547]},
	{"text": "[L/s]", "bbox": [308, 534, 352, 545], "bbox": [308, 534, 352, 545]},
	{"text": "7.87", "bbox": [401, 532, 439, 543], "bbox": [401, 532, 439, 543]},
	{"text": "2.33", "bbox": [485, 530, 521, 541], "bbox": [485, 530, 521, 541]},
	{"text": "29.6", "bbox": [568, 528, 605, 539], "bbox": [568, 528, 605, 539]},
	{"text": "3.18", "bbox": [652, 527, 689, 538], "bbox": [652, 527, 689, 538]},
	{"text": "40.4", "bbox": [735, 526, 773, 537], "bbox": [735, 526, 773, 537]},
	{"text": "36.6", "bbox": [820, 524, 857, 535], "bbox": [820, 524, 857, 535]},
	{"text": "MEF 75", "bbox": [94, 550, 157, 560], "bbox": [94, 550, 157, 560]},
	{"text": "[L/s]", "bbox": [308, 547, 352, 558], "bbox": [308, 547, 352, 558]},
	{"text": "6.92", "bbox": [401, 545, 439, 556], "bbox": [401, 545, 439, 556]},
	{"text": "0.96", "bbox": [485, 543, 521, 554], "bbox": [485, 543, 521, 554]},
	{"text": "13.9", "bbox": [568, 541, 605, 552], "bbox": [568, 541, 605, 552]},
	{"text": "1.65", "bbox": [652, 540, 689, 551], "bbox": [652, 540, 689, 551]},
	{"text": "23.9", "bbox": [735, 539, 773, 550], "bbox": [735, 539, 773, 550]},
	{"text": "72.1", "bbox": [820, 537, 857, 548], "bbox": [820, 537, 857, 548]},
	{"text": "MEF 50", "bbox": [94, 563, 157, 573], "bbox": [94, 563, 157, 573]},
	{"text": "[L/s]", "bbox": [308, 559, 352, 570], "bbox": [308, 559, 352, 570]},
	{"text": "4.17", "bbox": [401, 557, 439, 568], "bbox": [401, 557, 439, 568]},
	{"text": "0.52", "bbox": [485, 556, 521, 567], "bbox": [485, 556, 521, 567]},
	{"text": "12.5", "bbox": [568, 554, 605, 565], "bbox": [568, 554, 605, 565]},
	{"text": "0.85", "bbox": [652, 553, 689, 564], "bbox": [652, 553, 689, 564]},
	{"text": "20.3", "bbox": [735, 552, 773, 563], "bbox": [735, 552, 773, 563]},
	{"text": "63.0", "bbox": [820, 550, 857, 561], "bbox": [820, 550, 857, 561]},
	{"text": "MEF 25", "bbox": [94, 576, 157, 586], "bbox": [94, 576, 157, 586]},
	{"text": "[L/s]", "bbox": [308, 572, 352, 583], "bbox": [308, 572, 352, 583]},
	{"text": "1.51", "bbox": [401, 570, 439, 581], "bbox": [401, 570, 439, 581]},
	{"text": "0.22", "bbox": [485, 568, 521, 579], "bbox": [485, 568, 521, 579]},
	{"text": "14.3", "bbox": [568, 567, 605, 578], "bbox": [568, 567, 605, 578]},
	{"text": "0.35", "bbox": [652, 566, 689, 577], "bbox": [652, 566, 689, 577]},
	{"text": "23.2", "bbox": [735, 565, 773, 576], "bbox": [735, 565, 773, 576]},
	{"text": "62.9", "bbox": [820, 563, 857, 574], "bbox": [820, 563, 857, 574]},
	{"text": "MMEF 75/25", "bbox": [94, 589, 197, 600], "bbox": [94, 589, 197, 600]},
	{"text": "[L/s]", "bbox": [308, 585, 352, 596], "bbox": [308, 585, 352, 596]},
	{"text": "3.49", "bbox": [401, 583, 439, 594], "bbox": [401, 583, 439, 594]},
	{"text": "0.44", "bbox": [485, 581, 521, 592], "bbox": [485, 581, 521, 592]},
	{"text": "12.6", "bbox": [568, 579, 605, 590], "bbox": [568, 579, 605, 590]},
	{"text": "0.75", "bbox": [652, 578, 689, 589], "bbox": [652, 578, 689, 589]},
	{"text": "21.3", "bbox": [735, 577, 773, 588], "bbox": [735, 577, 773, 588]},
	{"text": "69.5", "bbox": [820, 575, 857, 586], "bbox": [820, 575, 857, 586]}
]
2026-08-10 06:25:04,047 INFO     29 [qwen-vl-text] coord API: raw_items=158, valid_items=158, elapsed=65.4s
2026-08-10 06:25:04,047 INFO     29 [qwen-vl-text] coord item[0]: text=JAEGE R PCMED, bbox=[696, 38, 875, 54]
2026-08-10 06:25:04,047 INFO     29 [qwen-vl-text] coord item[1]: text=渑池县人民医院, bbox=[361, 50, 588, 69]
2026-08-10 06:25:04,047 INFO     29 [qwen-vl-text] coord item[2]: text=肺功能检查报告, bbox=[375, 74, 565, 92]
2026-08-10 06:25:04,047 INFO     29 [qwen-vl-text] coord item[3]: text=舒张试验, bbox=[420, 97, 513, 115]
2026-08-10 06:25:04,047 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[67, 115, 118, 128]
2026-08-10 06:25:04,047 INFO     29 [qwen-vl-text] coord item[5]: text=科别：, bbox=[440, 118, 489, 131]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[6]: text=住院号：, bbox=[67, 128, 138, 141]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[7]: text=0, bbox=[251, 131, 260, 141]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[8]: text=测试号：, bbox=[440, 131, 508, 144]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[9]: text=2025042503, bbox=[615, 133, 711, 144]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[10]: text=性别：, bbox=[67, 141, 118, 154]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[11]: text=男, bbox=[252, 142, 271, 154]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[12]: text=年龄：, bbox=[440, 144, 489, 157]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[13]: text=56 Years, bbox=[615, 146, 692, 157]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[14]: text=身高：, bbox=[67, 154, 118, 167]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[15]: text=165 cm, bbox=[252, 156, 314, 167]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[16]: text=体重：, bbox=[440, 157, 489, 170]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[17]: text=70 kg, bbox=[615, 158, 663, 170]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[18]: text=标准体重：, bbox=[67, 167, 160, 180]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[19]: text=108 %, bbox=[252, 169, 314, 180]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[20]: text=体表面积：, bbox=[440, 170, 526, 183]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[21]: text=1.77 m, bbox=[615, 171, 674, 183]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[22]: text=吸烟史：, bbox=[67, 180, 141, 193]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[23]: text=Flow [L/s], bbox=[104, 230, 161, 242]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[24]: text=F/V ex, bbox=[324, 232, 362, 242]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[25]: text=Vol%VCmax, bbox=[487, 228, 550, 238]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[26]: text=0, bbox=[504, 238, 514, 247]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[27]: text=0, bbox=[520, 238, 529, 247]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[28]: text=Vol [L], bbox=[535, 241, 570, 254]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[29]: text=10, bbox=[84, 250, 100, 260]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[30]: text=20, bbox=[498, 250, 514, 260]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[31]: text=40, bbox=[498, 261, 514, 271]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[32]: text=60, bbox=[498, 273, 514, 283]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[33]: text=2, bbox=[522, 275, 532, 285]
2026-08-10 06:25:04,048 INFO     29 [qwen-vl-text] coord item[34]: text=5, bbox=[89, 280, 99, 290]
2026-08-10 06:25:04,049 INFO     29 [qwen-vl-text] coord item[35]: text=80, bbox=[498, 285, 514, 295]
2026-08-10 06:25:04,049 INFO     29 [qwen-vl-text] coord item[36]: text=100, bbox=[494, 295, 514, 305]
2026-08-10 06:25:04,049 INFO     29 [qwen-vl-text] coord item[37]: text=VCmax, bbox=[550, 292, 588, 302]
2026-08-10 06:25:04,049 INFO     29 [qwen-vl-text] coord item[38]: text=1, bbox=[453, 307, 467, 317]
2026-08-10 06:25:04,049 INFO     29 [qwen-vl-text] coord item[39]: text=1, bbox=[820, 305, 845, 315]
2026-08-10 06:25:04,049 INFO     29 [qwen-vl-text] coord item[40]: text=0, bbox=[90, 312, 100, 322]
2026-08-10 06:25:04,049 INFO     29 [qwen-vl-text] coord item[41]: text=1, bbox=[147, 322, 155, 332]
2026-08-10 06:25:04,049 INFO     29 [qwen-vl-text] coord item[42]: text=2, bbox=[191, 322, 201, 332]
2026-08-10 06:25:04,049 INFO     29 [qwen-vl-text] coord item[43]: text=3, bbox=[238, 322, 247, 332]
2026-08-10 06:25:04,049 INFO     29 [qwen-vl-text] coord item[44]: text=4, bbox=[283, 322, 292, 332]
2026-08-10 06:25:04,049 INFO     29 [qwen-vl-text] coord item[45]: text=5, bbox=[328, 322, 337, 332]
2026-08-10 06:25:04,049 INFO     29 [qwen-vl-text] coord item[46]: text=6, bbox=[372, 322, 381, 332]
2026-08-10 06:25:04,049 INFO     29 [qwen-vl-text] coord item[47]: text=7, bbox=[415, 322, 424, 332]
2026-08-10 06:25:04,049 INFO     29 [qwen-vl-text] coord item[48]: text=2, bbox=[453, 319, 467, 329]
2026-08-10 06:25:04,049 INFO     29 [qwen-vl-text] coord item[49]: text=2, bbox=[820, 315, 845, 325]
2026-08-10 06:25:04,049 INFO     29 [qwen-vl-text] coord item[50]: text=4, bbox=[523, 313, 532, 322]
2026-08-10 06:25:04,049 INFO     29 [qwen-vl-text] coord item[51]: text=5, bbox=[93, 345, 103, 355]
2026-08-10 06:25:04,049 INFO     29 [qwen-vl-text] coord item[52]: text=6, bbox=[523, 352, 532, 361]
2026-08-10 06:25:04,049 INFO     29 [qwen-vl-text] coord item[53]: text=10, bbox=[90, 376, 107, 386]
2026-08-10 06:25:04,049 INFO     29 [qwen-vl-text] coord item[54]: text=Time [s], bbox=[666, 378, 709, 389]
2026-08-10 06:25:04,049 INFO     29 [qwen-vl-text] coord item[55]: text=F/V in, bbox=[335, 395, 368, 405]
2026-08-10 06:25:04,049 INFO     29 [qwen-vl-text] coord item[56]: text=8, bbox=[525, 390, 534, 399]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[57]: text=0, bbox=[535, 399, 544, 408]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[58]: text=1, bbox=[572, 399, 579, 408]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[59]: text=2, bbox=[608, 399, 617, 408]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[60]: text=3, bbox=[645, 399, 654, 408]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[61]: text=4, bbox=[683, 399, 692, 408]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[62]: text=5, bbox=[720, 399, 729, 408]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[63]: text=6, bbox=[758, 399, 767, 408]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[64]: text=7, bbox=[796, 399, 805, 408]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[65]: text=8, bbox=[834, 396, 843, 405]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[66]: text=预计值, bbox=[378, 416, 438, 429]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[67]: text=前次, bbox=[484, 416, 521, 429]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[68]: text=前/预, bbox=[557, 415, 605, 428]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[69]: text=后次, bbox=[650, 414, 689, 427]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[70]: text=后/预, bbox=[724, 412, 773, 425]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[71]: text=改善率, bbox=[800, 410, 857, 423]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[72]: text=测试日期, bbox=[90, 432, 171, 445]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[73]: text=25/4/25, bbox=[455, 430, 521, 441]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[74]: text=25/4/25, bbox=[622, 428, 689, 439]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[75]: text=测试时间, bbox=[90, 445, 171, 458]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[76]: text=9:19:05, bbox=[448, 442, 521, 454]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[77]: text=9:43:24, bbox=[615, 440, 689, 452]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[78]: text=VC MAX, bbox=[94, 472, 157, 482]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[79]: text=[L], bbox=[327, 470, 352, 481]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[80]: text=3.85, bbox=[401, 469, 439, 480]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[81]: text=2.72, bbox=[485, 468, 521, 479]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[82]: text=70.6, bbox=[568, 467, 605, 477]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[83]: text=3.07, bbox=[652, 465, 689, 476]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[84]: text=79.9, bbox=[735, 464, 773, 475]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[85]: text=13.2, bbox=[820, 462, 857, 473]
2026-08-10 06:25:04,050 INFO     29 [qwen-vl-text] coord item[86]: text=FVC, bbox=[94, 485, 127, 495]
2026-08-10 06:25:04,051 INFO     29 [qwen-vl-text] coord item[87]: text=[L], bbox=[327, 483, 352, 494]
2026-08-10 06:25:04,051 INFO     29 [qwen-vl-text] coord item[88]: text=3.71, bbox=[401, 481, 439, 492]
2026-08-10 06:25:04,051 INFO     29 [qwen-vl-text] coord item[89]: text=2.68, bbox=[485, 480, 521, 491]
2026-08-10 06:25:04,051 INFO     29 [qwen-vl-text] coord item[90]: text=72.2, bbox=[568, 478, 605, 489]
2026-08-10 06:25:04,051 INFO     29 [qwen-vl-text] coord item[91]: text=3.05, bbox=[652, 477, 689, 488]
2026-08-10 06:25:04,051 INFO     29 [qwen-vl-text] coord item[92]: text=82.4, bbox=[735, 476, 773, 487]
2026-08-10 06:25:04,051 INFO     29 [qwen-vl-text] coord item[93]: text=14.1, bbox=[820, 475, 857, 485]
2026-08-10 06:25:04,051 INFO     29 [qwen-vl-text] coord item[94]: text=FEV 1, bbox=[94, 498, 145, 508]
2026-08-10 06:25:04,051 INFO     29 [qwen-vl-text] coord item[95]: text=[L], bbox=[327, 496, 352, 507]
2026-08-10 06:25:04,051 INFO     29 [qwen-vl-text] coord item[96]: text=2.98, bbox=[401, 494, 439, 505]
2026-08-10 06:25:04,051 INFO     29 [qwen-vl-text] coord item[97]: text=1.10, bbox=[485, 493, 521, 504]
2026-08-10 06:25:04,051 INFO     29 [qwen-vl-text] coord item[98]: text=36.9, bbox=[568, 491, 605, 502]
2026-08-10 06:25:04,051 INFO     29 [qwen-vl-text] coord item[99]: text=1.55, bbox=[652, 490, 689, 500]
2026-08-10 06:25:04,051 INFO     29 [qwen-vl-text] coord item[100]: text=52.1, bbox=[735, 488, 773, 499]
2026-08-10 06:25:04,051 INFO     29 [qwen-vl-text] coord item[101]: text=41.1, bbox=[820, 487, 857, 498]
2026-08-10 06:25:04,051 INFO     29 [qwen-vl-text] coord item[102]: text=FEV 1 % FVC, bbox=[94, 510, 207, 520]
2026-08-10 06:25:04,051 INFO     29 [qwen-vl-text] coord item[103]: text=[%], bbox=[327, 508, 352, 519]
2026-08-10 06:25:04,051 INFO     29 [qwen-vl-text] coord item[104]: text=83.77, bbox=[392, 506, 439, 517]
2026-08-10 06:25:04,051 INFO     29 [qwen-vl-text] coord item[105]: text=41.10, bbox=[477, 505, 521, 516]
2026-08-10 06:25:04,052 INFO     29 [qwen-vl-text] coord item[106]: text=49.1, bbox=[568, 504, 605, 515]
2026-08-10 06:25:04,052 INFO     29 [qwen-vl-text] coord item[107]: text=50.82, bbox=[645, 502, 689, 513]
2026-08-10 06:25:04,052 INFO     29 [qwen-vl-text] coord item[108]: text=60.7, bbox=[735, 501, 773, 512]
2026-08-10 06:25:04,052 INFO     29 [qwen-vl-text] coord item[109]: text=23.6, bbox=[820, 499, 857, 510]
2026-08-10 06:25:04,052 INFO     29 [qwen-vl-text] coord item[110]: text=FEV 1 % VC MAX, bbox=[94, 523, 238, 533]
2026-08-10 06:25:04,052 INFO     29 [qwen-vl-text] coord item[111]: text=[%], bbox=[327, 521, 352, 532]
2026-08-10 06:25:04,052 INFO     29 [qwen-vl-text] coord item[112]: text=77.13, bbox=[392, 519, 439, 530]
2026-08-10 06:25:04,052 INFO     29 [qwen-vl-text] coord item[113]: text=40.51, bbox=[477, 518, 521, 529]
2026-08-10 06:25:04,052 INFO     29 [qwen-vl-text] coord item[114]: text=52.5, bbox=[568, 516, 605, 527]
2026-08-10 06:25:04,052 INFO     29 [qwen-vl-text] coord item[115]: text=50.49, bbox=[645, 514, 689, 525]
2026-08-10 06:25:04,052 INFO     29 [qwen-vl-text] coord item[116]: text=65.5, bbox=[735, 513, 773, 524]
2026-08-10 06:25:04,052 INFO     29 [qwen-vl-text] coord item[117]: text=24.6, bbox=[820, 512, 857, 523]
2026-08-10 06:25:04,052 INFO     29 [qwen-vl-text] coord item[118]: text=PEF, bbox=[94, 537, 127, 547]
2026-08-10 06:25:04,053 INFO     29 [qwen-vl-text] coord item[119]: text=[L/s], bbox=[308, 534, 352, 545]
2026-08-10 06:25:04,053 INFO     29 [qwen-vl-text] coord item[120]: text=7.87, bbox=[401, 532, 439, 543]
2026-08-10 06:25:04,053 INFO     29 [qwen-vl-text] coord item[121]: text=2.33, bbox=[485, 530, 521, 541]
2026-08-10 06:25:04,053 INFO     29 [qwen-vl-text] coord item[122]: text=29.6, bbox=[568, 528, 605, 539]
2026-08-10 06:25:04,053 INFO     29 [qwen-vl-text] coord item[123]: text=3.18, bbox=[652, 527, 689, 538]
2026-08-10 06:25:04,053 INFO     29 [qwen-vl-text] coord item[124]: text=40.4, bbox=[735, 526, 773, 537]
2026-08-10 06:25:04,053 INFO     29 [qwen-vl-text] coord item[125]: text=36.6, bbox=[820, 524, 857, 535]
2026-08-10 06:25:04,053 INFO     29 [qwen-vl-text] coord item[126]: text=MEF 75, bbox=[94, 550, 157, 560]
2026-08-10 06:25:04,053 INFO     29 [qwen-vl-text] coord item[127]: text=[L/s], bbox=[308, 547, 352, 558]
2026-08-10 06:25:04,053 INFO     29 [qwen-vl-text] coord item[128]: text=6.92, bbox=[401, 545, 439, 556]
2026-08-10 06:25:04,053 INFO     29 [qwen-vl-text] coord item[129]: text=0.96, bbox=[485, 543, 521, 554]
2026-08-10 06:25:04,054 INFO     29 [qwen-vl-text] coord item[130]: text=13.9, bbox=[568, 541, 605, 552]
2026-08-10 06:25:04,054 INFO     29 [qwen-vl-text] coord item[131]: text=1.65, bbox=[652, 540, 689, 551]
2026-08-10 06:25:04,054 INFO     29 [qwen-vl-text] coord item[132]: text=23.9, bbox=[735, 539, 773, 550]
2026-08-10 06:25:04,054 INFO     29 [qwen-vl-text] coord item[133]: text=72.1, bbox=[820, 537, 857, 548]
2026-08-10 06:25:04,054 INFO     29 [qwen-vl-text] coord item[134]: text=MEF 50, bbox=[94, 563, 157, 573]
2026-08-10 06:25:04,054 INFO     29 [qwen-vl-text] coord item[135]: text=[L/s], bbox=[308, 559, 352, 570]
2026-08-10 06:25:04,054 INFO     29 [qwen-vl-text] coord item[136]: text=4.17, bbox=[401, 557, 439, 568]
2026-08-10 06:25:04,054 INFO     29 [qwen-vl-text] coord item[137]: text=0.52, bbox=[485, 556, 521, 567]
2026-08-10 06:25:04,054 INFO     29 [qwen-vl-text] coord item[138]: text=12.5, bbox=[568, 554, 605, 565]
2026-08-10 06:25:04,054 INFO     29 [qwen-vl-text] coord item[139]: text=0.85, bbox=[652, 553, 689, 564]
2026-08-10 06:25:04,054 INFO     29 [qwen-vl-text] coord item[140]: text=20.3, bbox=[735, 552, 773, 563]
2026-08-10 06:25:04,054 INFO     29 [qwen-vl-text] coord item[141]: text=63.0, bbox=[820, 550, 857, 561]
2026-08-10 06:25:04,054 INFO     29 [qwen-vl-text] coord item[142]: text=MEF 25, bbox=[94, 576, 157, 586]
2026-08-10 06:25:04,054 INFO     29 [qwen-vl-text] coord item[143]: text=[L/s], bbox=[308, 572, 352, 583]
2026-08-10 06:25:04,054 INFO     29 [qwen-vl-text] coord item[144]: text=1.51, bbox=[401, 570, 439, 581]
2026-08-10 06:25:04,054 INFO     29 [qwen-vl-text] coord item[145]: text=0.22, bbox=[485, 568, 521, 579]
2026-08-10 06:25:04,054 INFO     29 [qwen-vl-text] coord item[146]: text=14.3, bbox=[568, 567, 605, 578]
2026-08-10 06:25:04,054 INFO     29 [qwen-vl-text] coord item[147]: text=0.35, bbox=[652, 566, 689, 577]
2026-08-10 06:25:04,055 INFO     29 [qwen-vl-text] coord item[148]: text=23.2, bbox=[735, 565, 773, 576]
2026-08-10 06:25:04,055 INFO     29 [qwen-vl-text] coord item[149]: text=62.9, bbox=[820, 563, 857, 574]
2026-08-10 06:25:04,055 INFO     29 [qwen-vl-text] coord item[150]: text=MMEF 75/25, bbox=[94, 589, 197, 600]
2026-08-10 06:25:04,055 INFO     29 [qwen-vl-text] coord item[151]: text=[L/s], bbox=[308, 585, 352, 596]
2026-08-10 06:25:04,055 INFO     29 [qwen-vl-text] coord item[152]: text=3.49, bbox=[401, 583, 439, 594]
2026-08-10 06:25:04,055 INFO     29 [qwen-vl-text] coord item[153]: text=0.44, bbox=[485, 581, 521, 592]
2026-08-10 06:25:04,055 INFO     29 [qwen-vl-text] coord item[154]: text=12.6, bbox=[568, 579, 605, 590]
2026-08-10 06:25:04,055 INFO     29 [qwen-vl-text] coord item[155]: text=0.75, bbox=[652, 578, 689, 589]
2026-08-10 06:25:04,055 INFO     29 [qwen-vl-text] coord item[156]: text=21.3, bbox=[735, 577, 773, 588]
2026-08-10 06:25:04,055 INFO     29 [qwen-vl-text] coord item[157]: text=69.5, bbox=[820, 575, 857, 586]
2026-08-10 06:25:04,056 INFO     29 [qwen-vl-text] page=3 — 147/147 coords, api_time=65.4s
2026-08-10 06:25:04,062 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2855176, prompt_len=2015
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共65行）
["JAEGER PCMED", "渑池县人民医院", "肺功能检查报告", "常规通气", "姓名：", "住院号：0", "性别：男", "身高：165 cm", "标准体重：108 %", "吸烟史：", "科别：", "测试号：2025042503", "年龄：56 Years", "体重：70 kg", "体表面积：1.77 m", "预计值 实测值 实测/预", "测试日期 25/4/25", "测试时间 9:19:05]", "VC MAX [L] 3.85 2.72 70.6", "IRV [L] 0.91", "ERV [L] 1.11 1.02 91.8", "IC [L] 2.74 1.69 61.9", "VT [L] 0.50 0.78 156.7", "MV [L/min] 10.00 18.75 187.5", "VC IN [L] 3.85 2.69 70.0", "VC EX [L] 3.85 2.72 70.6", "BF [1/min] 20.00 23.93 119.7", "FVC [L] 3.71 2.68 72.2", "PEF [L/s] 7.87 2.33 29.6", "FEV 0.5 [L] 0.70", "FEV 1 [L] 2.98 1.10 36.9", "FEV 2 [L] 1.60", "FEV 3 [L] 1.91", "FEV6 [L] 2.45", "FEF 200-1200 [L/s] 0.94", "FEV 1 % FVC [%] 83.77 41.10 49.1", "FEV 1 % VC MAX [%] 77.13 40.51 52.5", "MEF 75 [L/s] 6.92 0.96 13.9", "MEF 50 [L/s] 4.17 0.52 12.5", "MEF 25 [L/s] 1.51 0.22 14.3", "MMEF 75/25 [L/s] 3.49 0.44 12.6", "FEF 75/85 [L/s] 0.77 0.18 23.0", "FEF50 % FIF50 [%] 38.63", "PIF [L/s] 1.41", "FVC IN [L] 3.85 2.69 70.0", "FET [s] 7.87", "FIF 50 [L/s] 1.35", "FIV1 [L] 1.10", "FIV1 % FVC [%] 40.89", "T IN [s] 1.21", "T EX [s] 1.30", "T TOT [s] 2.51", "MIF [L/s] 0.65", "MEF [L/s] 0.60", "MVV [L/min] 113.25 52.56 46.4", "FEF50 % FIF50 [%] 38.63", "V backextrapolation ex [L] 0.02", "V backextrapol. % FVC [%] 0.75", "测试结果", "1、重度阻塞性肺通气功能障碍，小气道功能降低。", "2、肺弥散功能正常。", "3、残气量正常，残气量/肺总量增高。", "4、沙丁胺醇气雾剂支气管舒张试验呈阳性，FEV1.0改41.1%。", "5、建议定期复查。", "报告医师：李朝红/崔艳芳 报告日期：2025.4.25"]

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
2026-08-10 06:25:28,875 INFO     29 [qwen-vl-text] coord API raw response (len=4218):
[
	{"text": "JAEGER PCMED", "bbox": [723, 64, 901, 78]},
	{"text": "渑池县人民医院", "bbox": [364, 79, 616, 101]},
	{"text": "肺功能检查报告", "bbox": [393, 104, 594, 121]},
	{"text": "常规通气", "bbox": [448, 126, 548, 141]},
	{"text": "姓名：", "bbox": [119, 149, 165, 161]},
	{"text": "住院号：", "bbox": [119, 160, 181, 172]},
	{"text": "0", "bbox": [283, 163, 293, 172]},
	{"text": "性别：", "bbox": [119, 172, 165, 184]},
	{"text": "男", "bbox": [284, 172, 302, 184]},
	{"text": "身高：", "bbox": [119, 184, 165, 195]},
	{"text": "165 cm", "bbox": [284, 185, 340, 195]},
	{"text": "标准体重：", "bbox": [119, 195, 200, 207]},
	{"text": "108 %", "bbox": [284, 196, 340, 206]},
	{"text": "吸烟史：", "bbox": [119, 207, 183, 219]},
	{"text": "科别：", "bbox": [454, 146, 499, 158]},
	{"text": "测试号：", "bbox": [454, 158, 516, 169]},
	{"text": "年龄：", "bbox": [454, 169, 500, 180]},
	{"text": "体重：", "bbox": [454, 180, 500, 192]},
	{"text": "体表面积：", "bbox": [454, 192, 535, 204]},
	{"text": "预计值 实测值 实测/预", "bbox": [385, 220, 602, 233]},
	{"text": "测试日期 25/4/25", "bbox": [124, 236, 196, 248]},
	{"text": "测试时间 9:19:05]", "bbox": [124, 248, 196, 260]},
	{"text": "VC MAX [L] 3.85 2.72 70.6", "bbox": [120, 270, 604, 282]},
	{"text": "IRV [L] 0.91", "bbox": [120, 282, 522, 294]},
	{"text": "ERV [L] 1.11 1.02 91.8", "bbox": [115, 294, 604, 306]},
	{"text": "IC [L] 2.74 1.69 61.9", "bbox": [115, 306, 604, 318]},
	{"text": "VT [L] 0.50 0.78 156.7", "bbox": [114, 318, 604, 329]},
	{"text": "MV [L/min] 10.00 18.75 187.5", "bbox": [112, 329, 604, 341]},
	{"text": "VC IN [L] 3.85 2.69 70.0", "bbox": [111, 341, 604, 353]},
	{"text": "VC EX [L] 3.85 2.72 70.6", "bbox": [111, 353, 604, 365]},
	{"text": "BF [1/min] 20.00 23.93 119.7", "bbox": [111, 365, 604, 377]},
	{"text": "FVC [L] 3.71 2.68 72.2", "bbox": [111, 377, 604, 389]},
	{"text": "PEF [L/s] 7.87 2.33 29.6", "bbox": [312, 389, 604, 400]},
	{"text": "FEV 0.5 [L] 0.70", "bbox": [111, 412, 526, 424]},
	{"text": "FEV 1 [L] 2.98 1.10 36.9", "bbox": [111, 424, 604, 436]},
	{"text": "FEV 2 [L] 1.60", "bbox": [111, 436, 526, 448]},
	{"text": "FEV 3 [L] 1.91", "bbox": [111, 448, 526, 460]},
	{"text": "FEV6 [L] 2.45", "bbox": [111, 460, 526, 472]},
	{"text": "FEF 200-1200 [L/s] 0.94", "bbox": [115, 472, 526, 484]},
	{"text": "FEV 1 % FVC [%] 83.77 41.10 49.1", "bbox": [119, 498, 604, 510]},
	{"text": "FEV 1 % VC MAX [%] 77.13 40.51 52.5", "bbox": [119, 510, 604, 522]},
	{"text": "MEF 75 [L/s] 6.92 0.96 13.9", "bbox": [119, 522, 604, 534]},
	{"text": "MEF 50 [L/s] 4.17 0.52 12.5", "bbox": [317, 534, 604, 546]},
	{"text": "MEF 25 [L/s] 1.51 0.22 14.3", "bbox": [317, 546, 604, 558]},
	{"text": "MMEF 75/25 [L/s] 3.49 0.44 12.6", "bbox": [115, 560, 604, 572]},
	{"text": "FEF 75/85 [L/s] 0.77 0.18 23.0", "bbox": [115, 572, 604, 584]},
	{"text": "FEF50 % FIF50 [%] 38.63", "bbox": [115, 584, 526, 596]},
	{"text": "PIF [L/s] 1.41", "bbox": [115, 596, 526, 608]},
	{"text": "FVC IN [L] 3.85 2.69 70.0", "bbox": [115, 608, 604, 620]},
	{"text": "FET [s] 7.87", "bbox": [115, 620, 526, 632]},
	{"text": "FIF 50 [L/s] 1.35", "bbox": [115, 632, 526, 644]},
	{"text": "FIV1 [L] 1.10", "bbox": [115, 644, 526, 656]},
	{"text": "FIV1 % FVC [%] 40.89", "bbox": [115, 656, 526, 668]},
	{"text": "T IN [s] 1.21", "bbox": [115, 668, 526, 680]},
	{"text": "T EX [s] 1.30", "bbox": [115, 680, 526, 692]},
	{"text": "T TOT [s] 2.51", "bbox": [115, 692, 526, 704]},
	{"text": "MIF [L/s] 0.65", "bbox": [111, 704, 526, 716]},
	{"text": "MEF [L/s] 0.60", "bbox": [317, 716, 526, 728]},
	{"text": "MVV [L/min] 113.25 52.56 46.4", "bbox": [111, 728, 616, 740]},
	{"text": "FEF50 % FIF50 [%] 38.63", "bbox": [111, 740, 526, 752]},
	{"text": "V backextrapolation ex [L] 0.02", "bbox": [108, 752, 526, 764]},
	{"text": "V backextrapol. % FVC [%] 0.75", "bbox": [108, 764, 526, 776]},
	{"text": "测试结果", "bbox": [108, 797, 218, 817]},
	{"text": "1、重度阻塞性肺通气功能障碍，小气道功能降低。", "bbox": [104, 815, 600, 841]},
	{"text": "2、肺弥散功能正常。", "bbox": [102, 837, 310, 860]},
	{"text": "3、残气量正常，残气量/肺总量增高。", "bbox": [102, 849, 480, 876]},
	{"text": "4、沙丁胺醇气雾剂支气管舒张试验呈阳性，FEV1.0改41.1%。", "bbox": [100, 864, 703, 893]},
	{"text": "5、建议定期复查。", "bbox": [100, 890, 286, 913]},
	{"text": "报告医师：李朝红/崔艳芳 报告日期：2025.4.25", "bbox": [415, 903, 916, 934]}
]
2026-08-10 06:25:28,875 INFO     29 [qwen-vl-text] coord API: raw_items=69, valid_items=69, elapsed=24.8s
2026-08-10 06:25:28,875 INFO     29 [qwen-vl-text] coord item[0]: text=JAEGER PCMED, bbox=[723, 64, 901, 78]
2026-08-10 06:25:28,875 INFO     29 [qwen-vl-text] coord item[1]: text=渑池县人民医院, bbox=[364, 79, 616, 101]
2026-08-10 06:25:28,875 INFO     29 [qwen-vl-text] coord item[2]: text=肺功能检查报告, bbox=[393, 104, 594, 121]
2026-08-10 06:25:28,875 INFO     29 [qwen-vl-text] coord item[3]: text=常规通气, bbox=[448, 126, 548, 141]
2026-08-10 06:25:28,875 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[119, 149, 165, 161]
2026-08-10 06:25:28,875 INFO     29 [qwen-vl-text] coord item[5]: text=住院号：, bbox=[119, 160, 181, 172]
2026-08-10 06:25:28,875 INFO     29 [qwen-vl-text] coord item[6]: text=0, bbox=[283, 163, 293, 172]
2026-08-10 06:25:28,875 INFO     29 [qwen-vl-text] coord item[7]: text=性别：, bbox=[119, 172, 165, 184]
2026-08-10 06:25:28,875 INFO     29 [qwen-vl-text] coord item[8]: text=男, bbox=[284, 172, 302, 184]
2026-08-10 06:25:28,875 INFO     29 [qwen-vl-text] coord item[9]: text=身高：, bbox=[119, 184, 165, 195]
2026-08-10 06:25:28,875 INFO     29 [qwen-vl-text] coord item[10]: text=165 cm, bbox=[284, 185, 340, 195]
2026-08-10 06:25:28,875 INFO     29 [qwen-vl-text] coord item[11]: text=标准体重：, bbox=[119, 195, 200, 207]
2026-08-10 06:25:28,875 INFO     29 [qwen-vl-text] coord item[12]: text=108 %, bbox=[284, 196, 340, 206]
2026-08-10 06:25:28,875 INFO     29 [qwen-vl-text] coord item[13]: text=吸烟史：, bbox=[119, 207, 183, 219]
2026-08-10 06:25:28,875 INFO     29 [qwen-vl-text] coord item[14]: text=科别：, bbox=[454, 146, 499, 158]
2026-08-10 06:25:28,875 INFO     29 [qwen-vl-text] coord item[15]: text=测试号：, bbox=[454, 158, 516, 169]
2026-08-10 06:25:28,875 INFO     29 [qwen-vl-text] coord item[16]: text=年龄：, bbox=[454, 169, 500, 180]
2026-08-10 06:25:28,875 INFO     29 [qwen-vl-text] coord item[17]: text=体重：, bbox=[454, 180, 500, 192]
2026-08-10 06:25:28,875 INFO     29 [qwen-vl-text] coord item[18]: text=体表面积：, bbox=[454, 192, 535, 204]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[19]: text=预计值 实测值 实测/预, bbox=[385, 220, 602, 233]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[20]: text=测试日期 25/4/25, bbox=[124, 236, 196, 248]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[21]: text=测试时间 9:19:05], bbox=[124, 248, 196, 260]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[22]: text=VC MAX [L] 3.85 2.72 70.6, bbox=[120, 270, 604, 282]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[23]: text=IRV [L] 0.91, bbox=[120, 282, 522, 294]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[24]: text=ERV [L] 1.11 1.02 91.8, bbox=[115, 294, 604, 306]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[25]: text=IC [L] 2.74 1.69 61.9, bbox=[115, 306, 604, 318]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[26]: text=VT [L] 0.50 0.78 156.7, bbox=[114, 318, 604, 329]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[27]: text=MV [L/min] 10.00 18.75 187.5, bbox=[112, 329, 604, 341]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[28]: text=VC IN [L] 3.85 2.69 70.0, bbox=[111, 341, 604, 353]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[29]: text=VC EX [L] 3.85 2.72 70.6, bbox=[111, 353, 604, 365]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[30]: text=BF [1/min] 20.00 23.93 119.7, bbox=[111, 365, 604, 377]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[31]: text=FVC [L] 3.71 2.68 72.2, bbox=[111, 377, 604, 389]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[32]: text=PEF [L/s] 7.87 2.33 29.6, bbox=[312, 389, 604, 400]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[33]: text=FEV 0.5 [L] 0.70, bbox=[111, 412, 526, 424]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[34]: text=FEV 1 [L] 2.98 1.10 36.9, bbox=[111, 424, 604, 436]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[35]: text=FEV 2 [L] 1.60, bbox=[111, 436, 526, 448]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[36]: text=FEV 3 [L] 1.91, bbox=[111, 448, 526, 460]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[37]: text=FEV6 [L] 2.45, bbox=[111, 460, 526, 472]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[38]: text=FEF 200-1200 [L/s] 0.94, bbox=[115, 472, 526, 484]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[39]: text=FEV 1 % FVC [%] 83.77 41.10 49.1, bbox=[119, 498, 604, 510]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[40]: text=FEV 1 % VC MAX [%] 77.13 40.51 52.5, bbox=[119, 510, 604, 522]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[41]: text=MEF 75 [L/s] 6.92 0.96 13.9, bbox=[119, 522, 604, 534]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[42]: text=MEF 50 [L/s] 4.17 0.52 12.5, bbox=[317, 534, 604, 546]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[43]: text=MEF 25 [L/s] 1.51 0.22 14.3, bbox=[317, 546, 604, 558]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[44]: text=MMEF 75/25 [L/s] 3.49 0.44 12.6, bbox=[115, 560, 604, 572]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[45]: text=FEF 75/85 [L/s] 0.77 0.18 23.0, bbox=[115, 572, 604, 584]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[46]: text=FEF50 % FIF50 [%] 38.63, bbox=[115, 584, 526, 596]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[47]: text=PIF [L/s] 1.41, bbox=[115, 596, 526, 608]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[48]: text=FVC IN [L] 3.85 2.69 70.0, bbox=[115, 608, 604, 620]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[49]: text=FET [s] 7.87, bbox=[115, 620, 526, 632]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[50]: text=FIF 50 [L/s] 1.35, bbox=[115, 632, 526, 644]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[51]: text=FIV1 [L] 1.10, bbox=[115, 644, 526, 656]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[52]: text=FIV1 % FVC [%] 40.89, bbox=[115, 656, 526, 668]
2026-08-10 06:25:28,876 INFO     29 [qwen-vl-text] coord item[53]: text=T IN [s] 1.21, bbox=[115, 668, 526, 680]
2026-08-10 06:25:28,877 INFO     29 [qwen-vl-text] coord item[54]: text=T EX [s] 1.30, bbox=[115, 680, 526, 692]
2026-08-10 06:25:28,877 INFO     29 [qwen-vl-text] coord item[55]: text=T TOT [s] 2.51, bbox=[115, 692, 526, 704]
2026-08-10 06:25:28,877 INFO     29 [qwen-vl-text] coord item[56]: text=MIF [L/s] 0.65, bbox=[111, 704, 526, 716]
2026-08-10 06:25:28,877 INFO     29 [qwen-vl-text] coord item[57]: text=MEF [L/s] 0.60, bbox=[317, 716, 526, 728]
2026-08-10 06:25:28,877 INFO     29 [qwen-vl-text] coord item[58]: text=MVV [L/min] 113.25 52.56 46.4, bbox=[111, 728, 616, 740]
2026-08-10 06:25:28,877 INFO     29 [qwen-vl-text] coord item[59]: text=FEF50 % FIF50 [%] 38.63, bbox=[111, 740, 526, 752]
2026-08-10 06:25:28,877 INFO     29 [qwen-vl-text] coord item[60]: text=V backextrapolation ex [L] 0.02, bbox=[108, 752, 526, 764]
2026-08-10 06:25:28,877 INFO     29 [qwen-vl-text] coord item[61]: text=V backextrapol. % FVC [%] 0.75, bbox=[108, 764, 526, 776]
2026-08-10 06:25:28,877 INFO     29 [qwen-vl-text] coord item[62]: text=测试结果, bbox=[108, 797, 218, 817]
2026-08-10 06:25:28,877 INFO     29 [qwen-vl-text] coord item[63]: text=1、重度阻塞性肺通气功能障碍，小气道功能降低。, bbox=[104, 815, 600, 841]
2026-08-10 06:25:28,877 INFO     29 [qwen-vl-text] coord item[64]: text=2、肺弥散功能正常。, bbox=[102, 837, 310, 860]
2026-08-10 06:25:28,877 INFO     29 [qwen-vl-text] coord item[65]: text=3、残气量正常，残气量/肺总量增高。, bbox=[102, 849, 480, 876]
2026-08-10 06:25:28,877 INFO     29 [qwen-vl-text] coord item[66]: text=4、沙丁胺醇气雾剂支气管舒张试验呈阳性，FEV1.0改41.1%。, bbox=[100, 864, 703, 893]
2026-08-10 06:25:28,877 INFO     29 [qwen-vl-text] coord item[67]: text=5、建议定期复查。, bbox=[100, 890, 286, 913]
2026-08-10 06:25:28,877 INFO     29 [qwen-vl-text] coord item[68]: text=报告医师：李朝红/崔艳芳 报告日期：2025.4.25, bbox=[415, 903, 916, 934]
2026-08-10 06:25:28,878 INFO     29 [qwen-vl-text] page=4 — 65/65 coords, api_time=24.8s
2026-08-10 06:25:28,878 INFO     29 [qwen-vl-text] new_positions (406):
[[2, 421.26, 533.12, 36.205999999999996, 47.994], [2, 226.1, 352.24, 47.994, 65.676], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 0, 0, 0, 0], [3, 414.12, 520.625, 31.996, 45.467999999999996], [3, 214.795, 349.85999999999996, 42.1, 58.098], [3, 223.125, 336.175, 62.308, 77.464], [3, 249.89999999999998, 305.235, 81.67399999999999, 96.83], [3, 39.864999999999995, 70.21, 96.83, 107.776], [3, 261.8, 290.955, 99.356, 110.30199999999999], [3, 39.864999999999995, 82.11, 107.776, 118.722], [3, 149.345, 154.7, 110.30199999999999, 118.722], [3, 261.8, 302.26, 110.30199999999999, 121.24799999999999], [3, 365.925, 423.04499999999996, 111.98599999999999, 121.24799999999999], [3, 39.864999999999995, 70.21, 118.722, 129.668], [3, 149.94, 161.245, 119.564, 129.668], [3, 261.8, 290.955, 121.24799999999999, 132.194], [3, 365.925, 411.74, 122.932, 132.194], [3, 39.864999999999995, 70.21, 129.668, 140.614], [3, 149.94, 186.82999999999998, 131.352, 140.614], [3, 261.8, 290.955, 132.194, 143.14], [3, 365.925, 394.48499999999996, 133.036, 143.14], [3, 39.864999999999995, 95.19999999999999, 140.614, 151.56], [3, 149.94, 186.82999999999998, 142.298, 151.56], [3, 261.8, 312.96999999999997, 143.14, 154.08599999999998], [3, 365.925, 401.03, 143.982, 154.08599999999998], [3, 39.864999999999995, 83.895, 151.56, 162.506], [3, 61.879999999999995, 95.795, 193.66, 203.76399999999998], [3, 192.78, 215.39, 195.344, 203.76399999999998], [3, 289.765, 327.25, 191.976, 200.396], [3, 299.88, 305.83, 200.396, 207.974], [3, 309.4, 314.755, 200.396, 207.974], [3, 318.325, 339.15, 202.922, 213.868], [3, 49.98, 59.5, 210.5, 218.92], [3, 296.31, 305.83, 210.5, 218.92], [3, 296.31, 305.83, 219.762, 228.182], [3, 296.31, 305.83, 229.86599999999999, 238.286], [3, 310.59, 316.53999999999996, 231.54999999999998, 239.97], [3, 52.955, 58.904999999999994, 235.76, 244.17999999999998], [3, 296.31, 305.83, 239.97, 248.39], [3, 293.93, 305.83, 248.39, 256.81], [3, 327.25, 349.85999999999996, 245.864, 254.284], [3, 269.53499999999997, 277.865, 258.49399999999997, 266.914], [3, 487.9, 502.775, 256.81, 265.23], [3, 53.55, 59.5, 262.704, 271.12399999999997], [3, 87.46499999999999, 92.225, 271.12399999999997, 279.544], [3, 113.645, 119.595, 271.12399999999997, 279.544], [3, 141.60999999999999, 146.965, 271.12399999999997, 279.544], [3, 168.385, 173.73999999999998, 271.12399999999997, 279.544], [3, 195.16, 200.515, 271.12399999999997, 279.544], [3, 221.34, 226.695, 271.12399999999997, 279.544], [3, 246.92499999999998, 252.28, 271.12399999999997, 279.544], [3, 269.53499999999997, 277.865, 268.598, 277.018], [3, 487.9, 502.775, 265.23, 273.65], [3, 311.185, 316.53999999999996, 263.546, 271.12399999999997], [3, 55.335, 61.285, 290.49, 298.90999999999997], [3, 311.185, 316.53999999999996, 296.384, 303.962], [3, 53.55, 63.665, 316.592, 325.012], [3, 396.27, 421.85499999999996, 318.276, 327.538], [3, 199.325, 218.95999999999998, 332.59, 341.01], [3, 312.375, 317.72999999999996, 328.38, 335.95799999999997], [3, 318.325, 323.68, 335.95799999999997, 343.536], [3, 340.34, 344.505, 335.95799999999997, 343.536], [3, 361.76, 367.115, 335.95799999999997, 343.536], [3, 383.775, 389.13, 335.95799999999997, 343.536], [3, 406.385, 411.74, 335.95799999999997, 343.536], [3, 428.4, 433.755, 335.95799999999997, 343.536], [3, 451.01, 456.36499999999995, 335.95799999999997, 343.536], [3, 473.62, 478.97499999999997, 335.95799999999997, 343.536], [3, 496.22999999999996, 501.585, 333.432, 341.01], [3, 224.91, 260.61, 350.272, 361.21799999999996], [3, 287.97999999999996, 309.995, 350.272, 361.21799999999996], [3, 331.41499999999996, 359.97499999999997, 349.43, 360.376], [3, 386.75, 409.955, 348.58799999999997, 359.534], [3, 430.78, 459.935, 346.904, 357.84999999999997], [3, 476.0, 509.91499999999996, 345.21999999999997, 356.166], [3, 53.55, 101.74499999999999, 363.74399999999997, 374.69], [3, 270.72499999999997, 309.995, 362.06, 371.322], [3, 370.09, 409.955, 360.376, 369.638], [3, 53.55, 101.74499999999999, 374.69, 385.63599999999997], [3, 266.56, 309.995, 372.164, 382.268], [3, 365.925, 409.955, 370.47999999999996, 380.584], [3, 55.93, 93.41499999999999, 397.424, 405.844], [3, 194.565, 209.44, 395.74, 405.002], [3, 238.595, 261.205, 394.89799999999997, 404.15999999999997], [3, 288.575, 309.995, 394.056, 403.318], [3, 337.96, 359.97499999999997, 393.214, 401.63399999999996], [3, 387.94, 409.955, 391.53, 400.792], [3, 437.325, 459.935, 390.688, 399.95], [3, 487.9, 509.91499999999996, 389.00399999999996, 398.26599999999996], [3, 55.93, 75.565, 408.37, 416.78999999999996], [3, 194.565, 209.44, 406.686, 415.948], [3, 238.595, 261.205, 405.002, 414.264], [3, 288.575, 309.995, 404.15999999999997, 413.42199999999997], [3, 337.96, 359.97499999999997, 402.476, 411.738], [3, 387.94, 409.955, 401.63399999999996, 410.89599999999996], [3, 437.325, 459.935, 400.792, 410.054], [3, 487.9, 509.91499999999996, 399.95, 408.37], [3, 55.93, 86.27499999999999, 419.316, 427.736], [3, 194.565, 209.44, 417.632, 426.894], [3, 238.595, 261.205, 415.948, 425.21], [3, 288.575, 309.995, 415.106, 424.368], [3, 337.96, 359.97499999999997, 413.42199999999997, 422.68399999999997], [3, 387.94, 409.955, 412.58, 421.0], [3, 437.325, 459.935, 410.89599999999996, 420.15799999999996], [3, 487.9, 509.91499999999996, 410.054, 419.316], [3, 55.93, 123.16499999999999, 429.41999999999996, 437.84], [3, 194.565, 209.44, 427.736, 436.998], [3, 233.23999999999998, 261.205, 426.05199999999996, 435.31399999999996], [3, 283.815, 309.995, 425.21, 434.472], [3, 337.96, 359.97499999999997, 424.368, 433.63], [3, 383.775, 409.955, 422.68399999999997, 431.94599999999997], [3, 437.325, 459.935, 421.842, 431.104], [3, 487.9, 509.91499999999996, 420.15799999999996, 429.41999999999996], [3, 55.93, 141.60999999999999, 440.366, 448.786], [3, 194.565, 209.44, 438.68199999999996, 447.94399999999996], [3, 233.23999999999998, 261.205, 436.998, 446.26], [3, 283.815, 309.995, 436.156, 445.418], [3, 337.96, 359.97499999999997, 434.472, 443.734], [3, 383.775, 409.955, 432.788, 442.05], [3, 437.325, 459.935, 431.94599999999997, 441.20799999999997], [3, 487.9, 509.91499999999996, 431.104, 440.366], [3, 55.93, 75.565, 452.154, 460.574], [3, 183.26, 209.44, 449.628, 458.89], [3, 238.595, 261.205, 447.94399999999996, 457.20599999999996], [3, 288.575, 309.995, 446.26, 455.522], [3, 337.96, 359.97499999999997, 444.57599999999996, 453.83799999999997], [3, 387.94, 409.955, 443.734, 452.996], [3, 437.325, 459.935, 442.892, 452.154], [3, 487.9, 509.91499999999996, 441.20799999999997, 450.46999999999997], [3, 55.93, 93.41499999999999, 463.09999999999997, 471.52], [3, 183.26, 209.44, 460.574, 469.83599999999996], [3, 238.595, 261.205, 458.89, 468.152], [3, 288.575, 309.995, 457.20599999999996, 466.46799999999996], [3, 337.96, 359.97499999999997, 455.522, 464.784], [3, 387.94, 409.955, 454.68, 463.942], [3, 437.325, 459.935, 453.83799999999997, 463.09999999999997], [3, 487.9, 509.91499999999996, 452.154, 461.416], [3, 55.93, 93.41499999999999, 474.046, 482.466], [3, 183.26, 209.44, 470.678, 479.94], [3, 238.595, 261.205, 468.99399999999997, 478.256], [3, 288.575, 309.995, 468.152, 477.414], [3, 337.96, 359.97499999999997, 466.46799999999996, 475.72999999999996], [3, 387.94, 409.955, 465.626, 474.888], [3, 437.325, 459.935, 464.784, 474.046], [3, 487.9, 509.91499999999996, 463.09999999999997, 472.36199999999997], [3, 55.93, 93.41499999999999, 484.99199999999996, 493.412], [3, 183.26, 209.44, 481.62399999999997, 490.88599999999997], [3, 238.595, 261.205, 479.94, 489.202], [3, 288.575, 309.995, 478.256, 487.518], [3, 337.96, 359.97499999999997, 477.414, 486.676], [4, 430.185, 536.095, 53.888, 65.676], [4, 216.57999999999998, 366.52, 66.518, 85.042], [4, 233.83499999999998, 353.43, 87.568, 101.88199999999999], [4, 266.56, 326.06, 106.092, 118.722], [4, 70.80499999999999, 98.175, 125.458, 135.56199999999998], [4, 70.80499999999999, 107.695, 134.72, 144.82399999999998], [4, 168.385, 174.33499999999998, 137.246, 144.82399999999998], [4, 70.80499999999999, 98.175, 144.82399999999998, 154.928], [4, 168.98, 179.69, 144.82399999999998, 154.928], [4, 70.80499999999999, 98.175, 154.928, 164.19], [4, 168.98, 202.29999999999998, 155.76999999999998, 164.19], [4, 70.80499999999999, 119.0, 164.19, 174.29399999999998], [4, 168.98, 202.29999999999998, 165.03199999999998, 173.452], [4, 70.80499999999999, 108.88499999999999, 174.29399999999998, 184.398], [4, 270.13, 296.905, 122.932, 133.036], [4, 270.13, 307.02, 133.036, 142.298], [4, 270.13, 297.5, 142.298, 151.56], [4, 270.13, 297.5, 151.56, 161.664], [4, 270.13, 318.325, 161.664, 171.768], [4, 229.075, 358.19, 185.23999999999998, 196.186], [4, 73.78, 116.61999999999999, 198.712, 208.816], [4, 73.78, 116.61999999999999, 208.816, 218.92], [4, 71.39999999999999, 359.38, 227.34, 237.444], [4, 71.39999999999999, 310.59, 237.444, 247.548], [4, 68.425, 359.38, 247.548, 257.652], [4, 68.425, 359.38, 257.652, 267.756], [4, 67.83, 359.38, 267.756, 277.018], [4, 66.64, 359.38, 277.018, 287.122], [4, 66.045, 359.38, 287.122, 297.226], [4, 66.045, 359.38, 297.226, 307.33], [4, 66.045, 359.38, 307.33, 317.43399999999997], [4, 66.045, 359.38, 317.43399999999997, 327.538], [4, 185.64, 359.38, 327.538, 336.8], [4, 66.045, 312.96999999999997, 346.904, 357.008], [4, 66.045, 359.38, 357.008, 367.11199999999997], [4, 66.045, 312.96999999999997, 367.11199999999997, 377.216], [4, 66.045, 312.96999999999997, 377.216, 387.32], [4, 66.045, 312.96999999999997, 387.32, 397.424], [4, 68.425, 312.96999999999997, 397.424, 407.52799999999996], [4, 70.80499999999999, 359.38, 419.316, 429.41999999999996], [4, 70.80499999999999, 359.38, 429.41999999999996, 439.524], [4, 70.80499999999999, 359.38, 439.524, 449.628], [4, 188.61499999999998, 359.38, 449.628, 459.73199999999997], [4, 188.61499999999998, 359.38, 459.73199999999997, 469.83599999999996], [4, 68.425, 359.38, 471.52, 481.62399999999997], [4, 68.425, 359.38, 481.62399999999997, 491.728], [4, 68.425, 312.96999999999997, 491.728, 501.832], [4, 68.425, 312.96999999999997, 501.832, 511.936], [4, 68.425, 359.38, 511.936, 522.04], [4, 68.425, 312.96999999999997, 522.04, 532.144], [4, 68.425, 312.96999999999997, 532.144, 542.2479999999999], [4, 68.425, 312.96999999999997, 542.2479999999999, 552.352], [4, 68.425, 312.96999999999997, 552.352, 562.456], [4, 68.425, 312.96999999999997, 562.456, 572.56], [4, 68.425, 312.96999999999997, 572.56, 582.664], [4, 68.425, 312.96999999999997, 582.664, 592.768], [4, 66.045, 312.96999999999997, 592.768, 602.872], [4, 188.61499999999998, 312.96999999999997, 602.872, 612.976], [4, 66.045, 366.52, 612.976, 623.0799999999999], [4, 66.045, 312.96999999999997, 623.0799999999999, 633.184], [4, 64.25999999999999, 312.96999999999997, 633.184, 643.288], [4, 64.25999999999999, 312.96999999999997, 643.288, 653.3919999999999], [4, 64.25999999999999, 129.71, 671.074, 687.914], [4, 61.879999999999995, 357.0, 686.23, 708.122], [4, 60.69, 184.45, 704.754, 724.12]]
2026-08-10 06:25:28,878 INFO     29 [qwen-vl-text] ═══ DONE ═══ 406 positions, pages=3, time=192.5s
2026-08-10 06:25:28,894 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 06:25:28,894 INFO     29 [Trace] task=abd585c0 | doc=LTSH 三门峡.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items, types={'ExaminationReport': 1}", "html": "", "json": "441 items", "markdown": "", "text": "", "name": "LTSH 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:25:28,895 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 06:25:28,895 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T06:25:28.895+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 4, "failed": 0, "current": {"abd585c0948311f1bd9827cf206dfa2d": {"id": "abd585c0948311f1bd9827cf206dfa2d", "doc_id": "ab76d5fc948311f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LTSH \u4e09\u95e8\u5ce1.pdf", "type": "pdf", "location": "LTSH \u4e09\u95e8\u5ce1.pdf", "size": 6636575, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786342866974, "task_type": "dataflow", "root_trace_id": "bcc06c371b5649ffa23cad2dd92769a3", "root_traceparent": "00-bcc06c371b5649ffa23cad2dd92769a3-aca0c6f6ccf15910-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 06:25:28,897 INFO     29 [ChunkMerger] Merged 2 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1} (filtered 6 noise chunks)
2026-08-10 06:25:29,532 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-10 06:25:29,533 INFO     29 [Trace] task=abd585c0 | doc=LTSH 三门峡.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}", "name": "LTSH 三门峡.pdf"}
2026-08-10 06:25:29,533 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 06:25:29,711 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786342917086, 'update_date': datetime.datetime(2026, 8, 10, 6, 21, 57), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 805739, 'status': '1'}
2026-08-10 06:25:29,998 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=渑池县人民医院
门诊病历
姓名:
门诊号: 613003
就诊时间:2025-05-27 14:24 科别: 呼吸与危重症医学科门诊
姓名
性别:男 年龄:56岁 婚否:已婚
职业:农民 工作单位:无
联系电话: 住址:河南省三门峡市渑池县仁村乡大
水沟村八组8号
病史叙述者:本人 身份证号:
过敏史:无
主诉:发作性胸闷、气喘4天。
现病史:患者于4天前受凉后出现胸闷、气喘,活动后加重,伴有咳
嗽,咳痰不明显,无胸痛、发热、咯血、盗汗等,未予治疗,症
状持续无缓解。
既往史:平素身体良好;无特殊疾病史;否认“肝炎、结核”等病史;
否认手术史;否认外伤史;否认输血史及献血史;否认药物及食
物过敏史;无预防接种史
流行病学史:无
体格检查:体温36.7℃,脉搏80次/分,呼吸22次/分,
血压132/80mmHg,双肺呼吸音粗,可闻及哮鸣音,未闻及
明显湿性啰音,心率80次/分,未闻及病理性杂音。
辅助检查:肺功能四项+支气管舒张实验;沙丁胺醇气雾剂支气管舒
张实验呈阳性,FEV1.0改善41.1%。
初步诊断:门诊诊断:1.支气管哮喘。
-1-
渑池县人民医院
门诊病历
姓名：
门诊号
处理意见：1.避免受凉，避免进食刺激性食物，避免接触刺激性气味；
2.如有不适，及时就医。
经治医师：
2
---
JAEGE R PCMED
渑池县人民医院
肺功能检查报告
综合测试
姓名：
性别：男
年龄：56 Years
身高：165 cm
体重：70 kg
备注：
联系电话：
住院号：0
测试号：
吸烟史：
既往史：
职业：
测试日期
测试时间
预计值
实测值
实/预
VC MAX
[L]
3.85
2.72
70.6
FVC
[L]
3.71
2.68
72.2
MV
[L/min]
10.00
18.75
187.5
FEV 1
[L]
2.98
1.10
36.9
FEV 1 % FVC
[%]
83.77
41.10
49.1
PEF
[L/s]
7.87
2.33
29.6
MEF 75
[L/s]
6.92
0.96
13.9
MEF 50
[L/s]
4.17
0.52
12.5
MEF 25
[L/s]
1.51
0.22
14.3
MMEF 75/25
[L/s]
3.49
0.44
12.6
MVV
[L/min]
113.25
52.56
46.4
TLC-SB
[L]
6.10
5.24
85.9
RV-SB
[L]
2.16
2.69
124.4
RV%TLC-SB
[%]
35.80
51.32
143.4
FRC-SB
[L]
3.28
3.71
113.3
FRC%TLC-SB
[%]
55.56
70.79
127.4
DLCO SB [mmol/min/kPa]
8.61
7.20
83.7
DLCO/Va mmol/min/kPa/L]
1.41
1.42
100.4
Hb
[g/100ml]
14.60
VA
[L]
5.95
5.09
85.5
DLCOc SB [mmol/min/kPa]
8.61
7.20
83.7
DLCOc/Va mmol/min/kPa/L]
1.41
1.42
100.4
VIN
[L]
3.85
2.55
66.3
Insp. time
[s]
1.52
Exp. time
[s]
2.15
Sample vol
[L]
System dead space [ml]
172.00
Anatom. dead space[ml]
154.00
TA
[s]
11.54
测试结果：
TLC
6
Vol [L]
FRCoeth
25/4/25
9:19:05上
RW
Time [min]
PredAdt.0
0.2
0.4
0.6
0.8
1.0
Flow [L/s]
F/V ex
10
5
0
2
4
6
F/V in
10
Vol [L]
Vol [L]
100
10
50
Time [s]
0
2
4
6
8
10
Volume [L]
4
2
0
1
4
Time [s]
0
10
20
30
40
JAEGE R PCMED
渑池县人民医院
肺功能检查报告
舒张试验
姓名：
科别：
住院号：0
测试号：2025042503
性别：男
年龄：56 Years
身高：165 cm
体重：70 kg
标准体重：108 %
体表面积：1.77 m
吸烟史：
Flow [L/s]
F/V ex
Vol%VCmax
Vol [L]
10
20
40
60
2
80
100
VCmax
1
0
2
3
4
5
6
7
1
2
4
5
6
7
8
10
Time [s]
F/V in
8
0
1
2
3
4
5
6
7
8
预计值
前次
前/预
后次
后/预
改善率
测试日期
25/4/25
25/4/25
测试时间
9:19:05
9:43:24
VC MAX
[L]
3.85
2.72
70.6
3.07
79.9
13.2
FVC
[L]
3.71
2.68
72.2
3.05
82.4
14.1
FEV 1
[L]
2.98
1.10
36.9
1.55
52.1
41.1
FEV 1 % FVC
[%]
83.77
41.10
49.1
50.82
60.7
23.6
FEV 1 % VC MAX
[%]
77.13
40.51
52.5
50.49
65.5
24.6
PEF
[L/s]
7.87
2.33
29.6
3.18
40.4
36.6
MEF 75
[L/s]
6.92
0.96
13.9
1.65
23.9
72.1
MEF 50
[L/s]
4.17
0.52
12.5
0.85
20.3
63.0
MEF 25
[L/s]
1.51
0.22
14.3
0.35
23.2
62.9
MMEF 75/25
[L/s]
3.49
0.44
12.6
0.75
21.3
69.5
JAEGER PCMED
渑池县人民医院
肺功能检查报告
常规通气
姓名：
住院号：0
性别：男
身高：165 cm
标准体重：108 %
吸烟史：
科别：
测试号：2025042503
年龄：56 Years
体重：70 kg
体表面积：1.77 m
预计值 实测值 实测/预
测试日期 25/4/25
测试时间 9:19:05]
VC MAX [L] 3.85 2.72 70.6
IRV [L] 0.91
ERV [L] 1.11 1.02 91.8
IC [L] 2.74 1.69 61.9
VT [L] 0.50 0.78 156.7
MV [L/min] 10.00 18.75 187.5
VC IN [L] 3.85 2.69 70.0
VC EX [L] 3.85 2.72 70.6
BF [1/min] 20.00 23.93 119.7
FVC [L] 3.71 2.68 72.2
PEF [L/s] 7.87 2.33 29.6
FEV 0.5 [L] 0.70
FEV 1 [L] 2.98 1.10 36.9
FEV 2 [L] 1.60
FEV 3 [L] 1.91
FEV6 [L] 2.45
FEF 200-1200 [L/s] 0.94
FEV 1 % FVC [%] 83.77 41.10 49.1
FEV 1 % VC MAX [%] 77.13 40.51 52.5
MEF 75 [L/s] 6.92 0.96 13.9
MEF 50 [L/s] 4.17 0.52 12.5
MEF 25 [L/s] 1.51 0.22 14.3
MMEF 75/25 [L/s] 3.49 0.44 12.6
FEF 75/85 [L/s] 0.77 0.18 23.0
FEF50 % FIF50 [%] 38.63
PIF [L/s] 1.41
FVC IN [L] 3.85 2.69 70.0
FET [s] 7.87
FIF 50 [L/s] 1.35
FIV1 [L] 1.10
FIV1 % FVC [%] 40.89
T IN [s] 1.21
T EX [s] 1.30
T TOT [s] 2.51
MIF [L/s] 0.65
MEF [L/s] 0.60
MVV [L/min] 113.25 52.56 46.4
FEF50 % FIF50 [%] 38.63
V backextrapolation ex [L] 0.02
V backextrapol. % FVC [%] 0.75
测试结果
1、重度阻塞性肺通气功能障碍，小气道功能降低。
2、肺弥散功能正常。
3、残气量正常，残气量/肺总量增高。
4、沙丁胺醇气雾剂支气管舒张试验呈阳性，FEV1.0改41.1%。
5、建议定期复查。
报告医师：李朝红/崔艳芳 报告日期：2025.4.25
2026-08-10 06:25:30,347 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-10 06:25:30,348 INFO     29 [Trace] task=abd585c0 | doc=LTSH 三门峡.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}", "name": "LTSH 三门峡.pdf", "embedding_token_consumption": 2911}
2026-08-10 06:25:30,348 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-10 06:25:30,954 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-10 06:25:30,955 INFO     29 [Trace] task=abd585c0 | doc=LTSH 三门峡.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":2,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 06:25:30,962 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:25:30,963 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:25:30,975 INFO     29 set_progress(abd585c0948311f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 06:25:30 [DOC Engine]:
Start to index...
2026-08-10 06:25:31,015 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.031s]
2026-08-10 06:25:31,022 INFO     29 set_progress(abd585c0948311f1bd9827cf206dfa2d), progress: 0.8500000000000001, progress_msg: 
2026-08-10 06:25:31,043 INFO     29 set_progress(abd585c0948311f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 06:25:31 Indexing done (0.06s). Task done (260.91s)
2026-08-10 06:25:31,050 INFO     29 [Done], chunks(2), token(2911), elapsed:260.91
2026-08-10 06:25:31,141 INFO     29 handle_task done for task {"id": "abd585c0948311f1bd9827cf206dfa2d", "doc_id": "ab76d5fc948311f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LTSH \u4e09\u95e8\u5ce1.pdf", "type": "pdf", "location": "LTSH \u4e09\u95e8\u5ce1.pdf", "size": 6636575, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786342866974, "task_type": "dataflow", "root_trace_id": "bcc06c371b5649ffa23cad2dd92769a3", "root_traceparent": "00-bcc06c371b5649ffa23cad2dd92769a3-aca0c6f6ccf15910-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
