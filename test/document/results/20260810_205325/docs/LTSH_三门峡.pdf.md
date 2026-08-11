# 基准结果：LTSH 三门峡.pdf

## 基本信息

- 文件：`LTSH 三门峡.pdf`
- 大小：6481.0 KB
- PDF 总页数：5
- doc_id：`907f140694bc11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T21:08:21  完成时间：2026-08-10T21:12:22  耗时：241.7s
- progress_msg：`13:12:20 Indexing done (0.02s). Task done (227.02s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 2ed1d433 | 2 | 1-2 | 渑池县人民医院 门诊病历 姓名: 门诊号: 613003 就诊时间:2025-0 |
| 2 | a8533aeb | 3 | 3-5 | JAEGE R PCMED 渑池县人民医院 肺功能检查报告 综合测试 姓名： 性 |

- chunks 总数：2
- 各 chunk 页数合计（含跨页重复）：5
- 页码并集：`[1, 2, 3, 4, 5]`
- 覆盖页数：5 / 5；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

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
- ChunkMerger：`{"found": true, "merged": 2, "sources": 9, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1, "Extractor:Progress": 1}, "filtered_noise": 7}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 13:12:19,771 INFO     29 [ChunkMerger] Merged 2 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 13:08:23,553 INFO     29 handle_task begin for task {"id": "90cba70894bc11f1bd9827cf206dfa2d", "doc_id": "907f140694bc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LTSH \u4e09\u95e8\u5ce1.pdf", "type": "pdf", "location": "LTSH \u4e09\u95e8\u5ce1.pdf", "size": 6636575, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786367302926, "task_type": "dataflow", "root_trace_id": "3e86fc61695b452a8b4ef13e7466fe92", "root_traceparent": "00-3e86fc61695b452a8b4ef13e7466fe92-eb986cfdcd997396-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 13:08:23,763 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.002s]
2026-08-10 13:08:23,874 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 13:08:23,886 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:08:23,886 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 13:08:23,886 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 13:08:23,891 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 13:08:23,891 INFO     29 ============================================================
2026-08-10 13:08:23,891 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 13:08:23,891 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 13:08:23,891 INFO     29 ============================================================
2026-08-10 13:08:23,891 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 13:08:23,891 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 13:08:23,893 INFO     29 No torch found.
2026-08-10 13:08:24,321 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=5
2026-08-10 13:08:24,591 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1397957, prompt_len=764
2026-08-10 13:08:26,233 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-05-27"}
```
2026-08-10 13:08:26,234 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=2025-05-27
2026-08-10 13:08:26,250 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1397957, prompt_len=401
2026-08-10 13:08:29,736 INFO     29 [qwen-vl-parser] text API response (len=561):
["渑池县人民医院", "门诊病历", "姓名:", "门诊号: 613003", "就诊时间:2025-05-27 14:24 科别: 呼吸与危重症医学科门诊", "姓名", "性别:男 年龄:56岁 婚否:已婚", "职业:农民 工作单位:无", "联系电话: 住址:河南省三门峡市渑池县仁村乡大", "水沟村八组8号", "病史叙述者:本人 身份证号:", "过敏史:无", "主诉:发作性胸闷、气喘4天。", "现病史:患者于4天前受凉后出现胸闷、气喘,活动后加重,伴有咳", "嗽,咳痰不明显,无胸痛、发热、咯血、盗汗等,未予治疗,症", "状持续无缓解。", "既往史:平素身体良好;无特殊疾病史;否认“肝炎、结核”等病史;", "否认手术史;否认外伤史;否认输血史及献血史;否认药物及食", "物过敏史;无预防接种史", "流行病学史:无", "体格检查:体温36.7℃,脉搏80次/分,呼吸22次/分,", "血压132/80mmHg,双肺呼吸音粗,可闻及哮鸣音,未闻及", "明显湿性啰音,心率80次/分,未闻及病理性杂音。", "辅助检查:肺功能四项+支气管舒张实验;沙丁胺醇气雾剂支气管舒", "张实验呈阳性,FEV1.0改善41.1%。", "初步诊断:门诊诊断:1.支气管哮喘。", "-1-"]
2026-08-10 13:08:29,736 INFO     29 [qwen-vl-parser] page=1 text: 27 lines (bbox 0-26)
2026-08-10 13:08:29,736 INFO     29 [qwen-vl-parser] page=1 text: 27 sections
2026-08-10 13:08:29,972 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1102391, prompt_len=764
2026-08-10 13:08:31,383 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:08:31,383 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 13:08:31,391 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1102391, prompt_len=401
2026-08-10 13:08:32,259 INFO     29 [qwen-vl-parser] text API response (len=99):
["渑池县人民医院", "门诊病历", "姓名：", "门诊号", "处理意见：1.避免受凉，避免进食刺激性食物，避免接触刺激性气味；", "2.如有不适，及时就医。", "经治医师：", "2"]
2026-08-10 13:08:32,259 INFO     29 [qwen-vl-parser] page=2 text: 8 lines (bbox 27-34)
2026-08-10 13:08:32,259 INFO     29 [qwen-vl-parser] page=2 text: 8 sections
2026-08-10 13:08:32,588 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1964770, prompt_len=764
2026-08-10 13:08:34,057 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 13:08:34,058 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 13:08:34,074 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1964770, prompt_len=401
2026-08-10 13:08:42,123 INFO     29 [qwen-vl-parser] text API response (len=1754):
["JAEGE R PCMED", "渑池县人民医院", "肺功能检查报告", "综合测试", "姓名：", "性别：男", "年龄：56 Years", "身高：165 cm", "体重：70 kg", "备注：", "联系电话：", "住院号：0", "测试号：", "吸烟史：", "既往史：", "职业：", "测试日期", "测试时间", "预计值", "实测值", "实/预", "VC MAX", "[L]", "3.85", "2.72", "70.6", "FVC", "[L]", "3.71", "2.68", "72.2", "MV", "[L/min]", "10.00", "18.75", "187.5", "FEV 1", "[L]", "2.98", "1.10", "36.9", "FEV 1 % FVC", "[%]", "83.77", "41.10", "49.1", "PEF", "[L/s]", "7.87", "2.33", "29.6", "MEF 75", "[L/s]", "6.92", "0.96", "13.9", "MEF 50", "[L/s]", "4.17", "0.52", "12.5", "MEF 25", "[L/s]", "1.51", "0.22", "14.3", "MMEF 75/25", "[L/s]", "3.49", "0.44", "12.6", "MVV", "[L/min]", "113.25", "52.56", "46.4", "TLC-SB", "[L]", "6.10", "5.24", "85.9", "RV-SB", "[L]", "2.16", "2.69", "124.4", "RV%TLC-SB", "[%]", "35.80", "51.32", "143.4", "FRC-SB", "[L]", "3.28", "3.71", "113.3", "FRC%TLC-SB", "[%]", "55.56", "70.79", "127.4", "DLCO SB [mmol/min/kPa]", "8.61", "7.20", "83.7", "DLCO/Va mmol/min/kPa/L]", "1.41", "1.42", "100.4", "Hb", "[g/100ml]", "14.60", "VA", "[L]", "5.95", "5.09", "85.5", "DLCOc SB [mmol/min/kPa]", "8.61", "7.20", "83.7", "DLCOc/Va mmol/min/kPa/L]", "1.41", "1.42", "100.4", "VIN", "[L]", "3.85", "2.55", "66.3", "Insp. time", "[s]", "1.52", "Exp. time", "[s]", "2.15", "Sample vol", "[L]", "System dead space [ml]", "172.00", "Anatom. dead space[ml]", "154.00", "TA", "[s]", "11.54", "测试结果：", "TLC", "6", "Vol [L]", "FRCPleth", "25/4/25", "9:19:05上午", "RW", "PredAdt.0", "0.2", "0.4", "0.6", "0.8", "1.0", "Time [min]", "Flow [L/s]", "F/V ex", "10", "5", "0", "2", "4", "6", "1", "5", "10", "F/V in", "Vol [L]", "100", "10", "50", "100", "Time [s]", "0", "2", "4", "6", "8", "10", "0", "Volume [L]", "4", "2", "0", "1", "2", "4", "Time [s]", "10", "20", "30", "40", "0"]
2026-08-10 13:08:42,126 INFO     29 [qwen-vl-parser] page=3 text: 198 lines (bbox 35-232)
2026-08-10 13:08:42,126 INFO     29 [qwen-vl-parser] page=3 text: 198 sections
2026-08-10 13:08:42,341 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1210531, prompt_len=764
2026-08-10 13:08:43,845 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 13:08:43,845 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-10 13:08:43,856 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1210531, prompt_len=401
2026-08-10 13:08:46,708 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:08:46.707+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 40, "failed": 0, "current": {"90cba70894bc11f1bd9827cf206dfa2d": {"id": "90cba70894bc11f1bd9827cf206dfa2d", "doc_id": "907f140694bc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LTSH \u4e09\u95e8\u5ce1.pdf", "type": "pdf", "location": "LTSH \u4e09\u95e8\u5ce1.pdf", "size": 6636575, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786367302926, "task_type": "dataflow", "root_trace_id": "3e86fc61695b452a8b4ef13e7466fe92", "root_traceparent": "00-3e86fc61695b452a8b4ef13e7466fe92-eb986cfdcd997396-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:08:51,207 INFO     29 [qwen-vl-parser] text API response (len=1196):
["JAEGE R PCMED", "渑池县人民医院", "肺功能检查报告", "舒张试验", "姓名：", "科别：", "住院号：0", "测试号：2025042503", "性别：男", "年龄：56 Years", "身高：165 cm", "体重：70 kg", "标准体重：108 %", "体表面积：1.77 m", "吸烟史：", "Flow [L/s]", "F/V ex", "Vol%VCmax", "Vol [L]", "10", "20", "40", "60", "80", "100", "2", "VCmax", "1", "1", "0", "2", "3", "4", "5", "6", "7", "1", "2", "4", "5", "6", "10", "Time [s]", "F/V in", "8", "0", "1", "2", "3", "4", "5", "6", "7", "8", "预计值", "前次", "前/预", "后次", "后/预", "改善率", "测试日期", "25/4/25", "25/4/25", "测试时间", "9:19:05", "9:43:24", "VC MAX", "[L]", "3.85", "2.72", "70.6", "3.07", "79.9", "13.2", "FVC", "[L]", "3.71", "2.68", "72.2", "3.05", "82.4", "14.1", "FEV 1", "[L]", "2.98", "1.10", "36.9", "1.55", "52.1", "41.1", "FEV 1 % FVC", "[%]", "83.77", "41.10", "49.1", "50.82", "60.7", "23.6", "FEV 1 % VC MAX", "[%]", "77.13", "40.51", "52.5", "50.49", "65.5", "24.6", "PEF", "[L/s]", "7.87", "2.33", "29.6", "3.18", "40.4", "36.6", "MEF 75", "[L/s]", "6.92", "0.96", "13.9", "1.65", "23.9", "72.1", "MEF 50", "[L/s]", "4.17", "0.52", "12.5", "0.85", "20.3", "63.0", "MEF 25", "[L/s]", "1.51", "0.22", "14.3", "0.35", "23.2", "62.9", "MMEF 75/25", "[L/s]", "3.49", "0.44", "12.6", "0.75", "21.3", "69.5"]
2026-08-10 13:08:51,208 INFO     29 [qwen-vl-parser] page=4 text: 146 lines (bbox 233-378)
2026-08-10 13:08:51,210 INFO     29 [qwen-vl-parser] page=4 text: 146 sections
2026-08-10 13:08:51,556 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2169828, prompt_len=764
2026-08-10 13:08:52,942 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 13:08:52,943 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 13:08:52,960 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2169828, prompt_len=401
2026-08-10 13:09:02,199 INFO     29 [qwen-vl-parser] text API response (len=1754):
["JAEGER PCMED", "渑池县人民医院", "肺功能检查报告", "常规通气", "姓名：", "住院号：0", "性别：男", "身高：165 cm", "标准体重：108 %", "吸烟史：", "科别：", "测试号：2025042503", "年龄：56 Years", "体重：70 kg", "体表面积：1.77 m", "预计值 实测值 实测/预", "测试日期 25/4/25", "测试时间 9:19:05]", "VC MAX [L] 3.85 2.72 70.6", "IRV [L] 0.91", "ERV [L] 1.11 1.02 91.8", "IC [L] 2.74 1.69 61.9", "VT [L] 0.50 0.78 156.7", "MV [L/min] 10.00 18.75 187.5", "VC IN [L] 3.85 2.69 70.0", "VC EX [L] 3.85 2.72 70.6", "BF [1/min] 20.00 23.93 119.7", "FVC [L] 3.71 2.68 72.2", "PEF [L/s] 7.87 2.33 29.6", "FEV 0.5 [L] 0.70", "FEV 1 [L] 2.98 1.10 36.9", "FEV 2 [L] 1.60", "FEV 3 [L] 1.91", "FEV6 [L] 2.45", "FEF 200-1200 [L/s] 0.94", "FEV 1 % FVC [%] 83.77 41.10 49.1", "FEV 1 % VC MAX [%] 77.13 40.51 52.5", "MEF 75 [L/s] 6.92 0.96 13.9", "MEF 50 [L/s] 4.17 0.52 12.5", "MEF 25 [L/s] 1.51 0.22 14.3", "MMEF 75/25 [L/s] 3.49 0.44 12.6", "FEF 75/85 [L/s] 0.77 0.18 23.0", "FEF50 % FIF50 [%] 38.63", "PIF [L/s] 1.41", "FVC IN [L] 3.85 2.69 70.0", "FET [s] 7.87", "FIF 50 [L/s] 1.35", "FIV1 [L] 1.10", "FIV1 % FVC [%] 40.89", "T IN [s] 1.21", "T EX [s] 1.30", "T TOT [s] 2.51", "MIF [L/s] 0.65", "MEF [L/s] 0.60", "MVV [L/min] 113.25 52.56 46.4", "FEF50 % FIF50 [%] 38.63", "V backextrapolation ex [L] 0.02", "V backextrapol. % FVC [%] 0.75", "测试结果", "1、重度阻塞性肺通气功能障碍，小气道功能降低。", "2、肺弥散功能正常。", "3、残气量正常，残气量/肺总量增高。", "4、沙丁胺醇气雾剂支气管舒张试验呈阳性，FEV1.0改41.1%。", "5、建议定期复查。", "报告医师：", "报告日期：2025.4.25", "TLC", "6 Vol [L]", "FRCl eth", "R", "Time [min]", "PredA@0 0.2 0.4 0.6 0.8 1.0", "Flow [L/s]", "F/V ex", "10", "5", "0", "2", "4", "6", "10", "F/V in", "Vol%VCmax", "0", "0", "Vol [L]", "20", "40", "60", "80", "100", "2", "VCmax", "4", "6", "8", "Time [s]", "8", "4", "Vol [L]", "2", "0", "2", "4", "Time [s]", "0", "2", "4", "6", "8", "10", "12", "14"]
2026-08-10 13:09:02,201 INFO     29 [qwen-vl-parser] page=5 text: 113 lines (bbox 379-491)
2026-08-10 13:09:02,203 INFO     29 [qwen-vl-parser] page=5 text: 113 sections
2026-08-10 13:09:02,203 INFO     29 [qwen-vl-parser] parse_pdf done: 492 sections from 5 pages.
2026-08-10 13:09:02,212 INFO     29 Close text detector.
2026-08-10 13:09:02,662 INFO     29 Close text recognizer.
2026-08-10 13:09:03,027 INFO     29 Close recognizer.
2026-08-10 13:09:03,468 INFO     29 Close recognizer.
2026-08-10 13:09:04,156 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 13:09:04,157 INFO     29 [Trace] task=90cba708 | doc=LTSH 三门峡.pdf | Parser:MedLink | outputs={"html": "", "json": "492 items", "markdown": "", "text": "", "name": "LTSH 三门峡.pdf", "output_format": "json"}
2026-08-10 13:09:04,157 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 13:09:04,192 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:09:04,192 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 渑池县人民医院\n[BBOX-1] 门诊病历\n[BBOX-2] 姓名:\n[BBOX-3] 门诊号: 613003\n[BBOX-4] 就诊时间:2025-05-27 14:24 科别: 呼吸与危重症医学科门诊\n[BBOX-5] 姓名\n[BBOX-6] 性别:男 年龄:56岁 婚否:已婚\n[BBOX-7] 职业:农民 工作单位:无\n[BBOX-8] 联系电话: 住址:河南省三门峡市渑池县仁村乡大\n[BBOX-9] 水沟村八组8号\n[BBOX-10] 病史叙述者:本人 身份证号:\n[BBOX-11] 过敏史:无\n[BBOX-12] 主诉:发作性胸闷、气喘4天。\n[BBOX-13] 现病史:患者于4天前受凉后出现胸闷、气喘,活动后加重,伴有咳\n[BBOX-14] 嗽,咳痰不明显,无胸痛、发热、咯血、盗汗等,未予治疗,症\n[BBOX-15] 状持续无缓解。\n[BBOX-16] 既往史:平素身体良好;无特殊疾病史;否认“肝炎、结核”等病史;\n[BBOX-17] 否认手术史;否认外伤史;否认输血史及献血史;否认药物及食\n[BBOX-18] 物过敏史;无预防接种史\n[BBOX-19] 流行病学史:无\n[BBOX-20] 体格检查:体温36.7℃,脉搏80次/分,呼吸22次/分,\n[BBOX-21] 血压132/80mmHg,双肺呼吸音粗,可闻及哮鸣音,未闻及\n[BBOX-22] 明显湿性啰音,心率80次/分,未闻及病理性杂音。\n[BBOX-23] 辅助检查:肺功能四项+支气管舒张实验;沙丁胺醇气雾剂支气管舒\n[BBOX-24] 张实验呈阳性,FEV1.0改善41.1%。\n[BBOX-25] 初步诊断:门诊诊断:1.支气管哮喘。\n[BBOX-26] -1-\n[BBOX-27] 渑池县人民医院\n[BBOX-28] 门诊病历\n[BBOX-29] 姓名：\n[BBOX-30] 门诊号\n[BBOX-31] 处理意见：1.避免受凉，避免进食刺激性食物，避免接触刺激性气味；\n[BBOX-32] 2.如有不适，及时就医。\n[BBOX-33] 经治医师：\n[BBOX-34] 2\n[BBOX-35] JAEGE R PCMED\n[BBOX-36] 渑池县人民医院\n[BBOX-37] 肺功能检查报告\n[BBOX-38] 综合测试\n[BBOX-39] 姓名：\n[BBOX-40] 性别：男\n[BBOX-41] 年龄：56 Years\n[BBOX-42] 身高：165 cm\n[BBOX-43] 体重：70 kg\n[BBOX-44] 备注：\n[BBOX-45] 联系电话：\n[BBOX-46] 住院号：0\n[BBOX-47] 测试号：\n[BBOX-48] 吸烟史：\n[BBOX-49] 既往史：\n[BBOX-50] 职业：\n[BBOX-51] 测试日期\n[BBOX-52] 测试时间\n[BBOX-53] 预计值\n[BBOX-54] 实测值\n[BBOX-55] 实/预\n[BBOX-56] VC MAX\n[BBOX-57] [L]\n[BBOX-58] 3.85\n[BBOX-59] 2.72\n[BBOX-60] 70.6\n[BBOX-61] FVC\n[BBOX-62] [L]\n[BBOX-63] 3.71\n[BBOX-64] 2.68\n[BBOX-65] 72.2\n[BBOX-66] MV\n[BBOX-67] [L/min]\n[BBOX-68] 10.00\n[BBOX-69] 18.75\n[BBOX-70] 187.5\n[BBOX-71] FEV 1\n[BBOX-72] [L]\n[BBOX-73] 2.98\n[BBOX-74] 1.10\n[BBOX-75] 36.9\n[BBOX-76] FEV 1 % FVC\n[BBOX-77] [%]\n[BBOX-78] 83.77\n[BBOX-79] 41.10\n[BBOX-80] 49.1\n[BBOX-81] PEF\n[BBOX-82] [L/s]\n[BBOX-83] 7.87\n[BBOX-84] 2.33\n[BBOX-85] 29.6\n[BBOX-86] MEF 75\n[BBOX-87] [L/s]\n[BBOX-88] 6.92\n[BBOX-89] 0.96\n[BBOX-90] 13.9\n[BBOX-91] MEF 50\n[BBOX-92] [L/s]\n[BBOX-93] 4.17\n[BBOX-94] 0.52\n[BBOX-95] 12.5\n[BBOX-96] MEF 25\n[BBOX-97] [L/s]\n[BBOX-98] 1.51\n[BBOX-99] 0.22\n[BBOX-100] 14.3\n[BBOX-101] MMEF 75/25\n[BBOX-102] [L/s]\n[BBOX-103] 3.49\n[BBOX-104] 0.44\n[BBOX-105] 12.6\n[BBOX-106] MVV\n[BBOX-107] [L/min]\n[BBOX-108] 113.25\n[BBOX-109] 52.56\n[BBOX-110] 46.4\n[BBOX-111] TLC-SB\n[BBOX-112] [L]\n[BBOX-113] 6.10\n[BBOX-114] 5.24\n[BBOX-115] 85.9\n[BBOX-116] RV-SB\n[BBOX-117] [L]\n[BBOX-118] 2.16\n[BBOX-119] 2.69\n[BBOX-120] 124.4\n[BBOX-121] RV%TLC-SB\n[BBOX-122] [%]\n[BBOX-123] 35.80\n[BBOX-124] 51.32\n[BBOX-125] 143.4\n[BBOX-126] FRC-SB\n[BBOX-127] [L]\n[BBOX-128] 3.28\n[BBOX-129] 3.71\n[BBOX-130] 113.3\n[BBOX-131] FRC%TLC-SB\n[BBOX-132] [%]\n[BBOX-133] 55.56\n[BBOX-134] 70.79\n[BBOX-135] 127.4\n[BBOX-136] DLCO SB [mmol/min/kPa]\n[BBOX-137] 8.61\n[BBOX-138] 7.20\n[BBOX-139] 83.7\n[BBOX-140] DLCO/Va mmol/min/kPa/L]\n[BBOX-141] 1.41\n[BBOX-142] 1.42\n[BBOX-143] 100.4\n[BBOX-144] Hb\n[BBOX-145] [g/100ml]\n[BBOX-146] 14.60\n[BBOX-147] VA\n[BBOX-148] [L]\n[BBOX-149] 5.95\n[BBOX-150] 5.09\n[BBOX-151] 85.5\n[BBOX-152] DLCOc SB [mmol/min/kPa]\n[BBOX-153] 8.61\n[BBOX-154] 7.20\n[BBOX-155] 83.7\n[BBOX-156] DLCOc/Va mmol/min/kPa/L]\n[BBOX-157] 1.41\n[BBOX-158] 1.42\n[BBOX-159] 100.4\n[BBOX-160] VIN\n[BBOX-161] [L]\n[BBOX-162] 3.85\n[BBOX-163] 2.55\n[BBOX-164] 66.3\n[BBOX-165] Insp. time\n[BBOX-166] [s]\n[BBOX-167] 1.52\n[BBOX-168] Exp. time\n[BBOX-169] [s]\n[BBOX-170] 2.15\n[BBOX-171] Sample vol\n[BBOX-172] [L]\n[BBOX-173] System dead space [ml]\n[BBOX-174] 172.00\n[BBOX-175] Anatom. dead space[ml]\n[BBOX-176] 154.00\n[BBOX-177] TA\n[BBOX-178] [s]\n[BBOX-179] 11.54\n[BBOX-180] 测试结果：\n[BBOX-181] TLC\n[BBOX-182] 6\n[BBOX-183] Vol [L]\n[BBOX-184] FRCPleth\n[BBOX-185] 25/4/25\n[BBOX-186] 9:19:05上午\n[BBOX-187] RW\n[BBOX-188] PredAdt.0\n[BBOX-189] 0.2\n[BBOX-190] 0.4\n[BBOX-191] 0.6\n[BBOX-192] 0.8\n[BBOX-193] 1.0\n[BBOX-194] Time [min]\n[BBOX-195] Flow [L/s]\n[BBOX-196] F/V ex\n[BBOX-197] 10\n[BBOX-198] 5\n[BBOX-199] 0\n[BBOX-200] 2\n[BBOX-201] 4\n[BBOX-202] 6\n[BBOX-203] 1\n[BBOX-204] 5\n[BBOX-205] 10\n[BBOX-206] F/V in\n[BBOX-207] Vol [L]\n[BBOX-208] 100\n[BBOX-209] 10\n[BBOX-210] 50\n[BBOX-211] 100\n[BBOX-212] Time [s]\n[BBOX-213] 0\n[BBOX-214] 2\n[BBOX-215] 4\n[BBOX-216] 6\n[BBOX-217] 8\n[BBOX-218] 10\n[BBOX-219] 0\n[BBOX-220] Volume [L]\n[BBOX-221] 4\n[BBOX-222] 2\n[BBOX-223] 0\n[BBOX-224] 1\n[BBOX-225] 2\n[BBOX-226] 4\n[BBOX-227] Time [s]\n[BBOX-228] 10\n[BBOX-229] 20\n[BBOX-230] 30\n[BBOX-231] 40\n[BBOX-232] 0\n[BBOX-233] JAEGE R PCMED\n[BBOX-234] 渑池县人民医院\n[BBOX-235] 肺功能检查报告\n[BBOX-236] 舒张试验\n[BBOX-237] 姓名：\n[BBOX-238] 科别：\n[BBOX-239] 住院号：0\n[BBOX-240] 测试号：2025042503\n[BBOX-241] 性别：男\n[BBOX-242] 年龄：56 Years\n[BBOX-243] 身高：165 cm\n[BBOX-244] 体重：70 kg\n[BBOX-245] 标准体重：108 %\n[BBOX-246] 体表面积：1.77 m\n[BBOX-247] 吸烟史：\n[BBOX-248] Flow [L/s]\n[BBOX-249] F/V ex\n[BBOX-250] Vol%VCmax\n[BBOX-251] Vol [L]\n[BBOX-252] 10\n[BBOX-253] 20\n[BBOX-254] 40\n[BBOX-255] 60\n[BBOX-256] 80\n[BBOX-257] 100\n[BBOX-258] 2\n[BBOX-259] VCmax\n[BBOX-260] 1\n[BBOX-261] 1\n[BBOX-262] 0\n[BBOX-263] 2\n[BBOX-264] 3\n[BBOX-265] 4\n[BBOX-266] 5\n[BBOX-267] 6\n[BBOX-268] 7\n[BBOX-269] 1\n[BBOX-270] 2\n[BBOX-271] 4\n[BBOX-272] 5\n[BBOX-273] 6\n[BBOX-274] 10\n[BBOX-275] Time [s]\n[BBOX-276] F/V in\n[BBOX-277] 8\n[BBOX-278] 0\n[BBOX-279] 1\n[BBOX-280] 2\n[BBOX-281] 3\n[BBOX-282] 4\n[BBOX-283] 5\n[BBOX-284] 6\n[BBOX-285] 7\n[BBOX-286] 8\n[BBOX-287] 预计值\n[BBOX-288] 前次\n[BBOX-289] 前/预\n[BBOX-290] 后次\n[BBOX-291] 后/预\n[BBOX-292] 改善率\n[BBOX-293] 测试日期\n[BBOX-294] 25/4/25\n[BBOX-295] 25/4/25\n[BBOX-296] 测试时间\n[BBOX-297] 9:19:05\n[BBOX-298] 9:43:24\n[BBOX-299] VC MAX\n[BBOX-300] [L]\n[BBOX-301] 3.85\n[BBOX-302] 2.72\n[BBOX-303] 70.6\n[BBOX-304] 3.07\n[BBOX-305] 79.9\n[BBOX-306] 13.2\n[BBOX-307] FVC\n[BBOX-308] [L]\n[BBOX-309] 3.71\n[BBOX-310] 2.68\n[BBOX-311] 72.2\n[BBOX-312] 3.05\n[BBOX-313] 82.4\n[BBOX-314] 14.1\n[BBOX-315] FEV 1\n[BBOX-316] [L]\n[BBOX-317] 2.98\n[BBOX-318] 1.10\n[BBOX-319] 36.9\n[BBOX-320] 1.55\n[BBOX-321] 52.1\n[BBOX-322] 41.1\n[BBOX-323] FEV 1 % FVC\n[BBOX-324] [%]\n[BBOX-325] 83.77\n[BBOX-326] 41.10\n[BBOX-327] 49.1\n[BBOX-328] 50.82\n[BBOX-329] 60.7\n[BBOX-330] 23.6\n[BBOX-331] FEV 1 % VC MAX\n[BBOX-332] [%]\n[BBOX-333] 77.13\n[BBOX-334] 40.51\n[BBOX-335] 52.5\n[BBOX-336] 50.49\n[BBOX-337] 65.5\n[BBOX-338] 24.6\n[BBOX-339] PEF\n[BBOX-340] [L/s]\n[BBOX-341] 7.87\n[BBOX-342] 2.33\n[BBOX-343] 29.6\n[BBOX-344] 3.18\n[BBOX-345] 40.4\n[BBOX-346] 36.6\n[BBOX-347] MEF 75\n[BBOX-348] [L/s]\n[BBOX-349] 6.92\n[BBOX-350] 0.96\n[BBOX-351] 13.9\n[BBOX-352] 1.65\n[BBOX-353] 23.9\n[BBOX-354] 72.1\n[BBOX-355] MEF 50\n[BBOX-356] [L/s]\n[BBOX-357] 4.17\n[BBOX-358] 0.52\n[BBOX-359] 12.5\n[BBOX-360] 0.85\n[BBOX-361] 20.3\n[BBOX-362] 63.0\n[BBOX-363] MEF 25\n[BBOX-364] [L/s]\n[BBOX-365] 1.51\n[BBOX-366] 0.22\n[BBOX-367] 14.3\n[BBOX-368] 0.35\n[BBOX-369] 23.2\n[BBOX-370] 62.9\n[BBOX-371] MMEF 75/25\n[BBOX-372] [L/s]\n[BBOX-373] 3.49\n[BBOX-374] 0.44\n[BBOX-375] 12.6\n[BBOX-376] 0.75\n[BBOX-377] 21.3\n[BBOX-378] 69.5\n[BBOX-379] JAEGER PCMED\n[BBOX-380] 渑池县人民医院\n[BBOX-381] 肺功能检查报告\n[BBOX-382] 常规通气\n[BBOX-383] 姓名：\n[BBOX-384] 住院号：0\n[BBOX-385] 性别：男\n[BBOX-386] 身高：165 cm\n[BBOX-387] 标准体重：108 %\n[BBOX-388] 吸烟史：\n[BBOX-389] 科别：\n[BBOX-390] 测试号：2025042503\n[BBOX-391] 年龄：56 Years\n[BBOX-392] 体重：70 kg\n[BBOX-393] 体表面积：1.77 m\n[BBOX-394] 预计值 实测值 实测/预\n[BBOX-395] 测试日期 25/4/25\n[BBOX-396] 测试时间 9:19:05]\n[BBOX-397] VC MAX [L] 3.85 2.72 70.6\n[BBOX-398] IRV [L] 0.91\n[BBOX-399] ERV [L] 1.11 1.02 91.8\n[BBOX-400] IC [L] 2.74 1.69 61.9\n[BBOX-401] VT [L] 0.50 0.78 156.7\n[BBOX-402] MV [L/min] 10.00 18.75 187.5\n[BBOX-403] VC IN [L] 3.85 2.69 70.0\n[BBOX-404] VC EX [L] 3.85 2.72 70.6\n[BBOX-405] BF [1/min] 20.00 23.93 119.7\n[BBOX-406] FVC [L] 3.71 2.68 72.2\n[BBOX-407] PEF [L/s] 7.87 2.33 29.6\n[BBOX-408] FEV 0.5 [L] 0.70\n[BBOX-409] FEV 1 [L] 2.98 1.10 36.9\n[BBOX-410] FEV 2 [L] 1.60\n[BBOX-411] FEV 3 [L] 1.91\n[BBOX-412] FEV6 [L] 2.45\n[BBOX-413] FEF 200-1200 [L/s] 0.94\n[BBOX-414] FEV 1 % FVC [%] 83.77 41.10 49.1\n[BBOX-415] FEV 1 % VC MAX [%] 77.13 40.51 52.5\n[BBOX-416] MEF 75 [L/s] 6.92 0.96 13.9\n[BBOX-417] MEF 50 [L/s] 4.17 0.52 12.5\n[BBOX-418] MEF 25 [L/s] 1.51 0.22 14.3\n[BBOX-419] MMEF 75/25 [L/s] 3.49 0.44 12.6\n[BBOX-420] FEF 75/85 [L/s] 0.77 0.18 23.0\n[BBOX-421] FEF50 % FIF50 [%] 38.63\n[BBOX-422] PIF [L/s] 1.41\n[BBOX-423] FVC IN [L] 3.85 2.69 70.0\n[BBOX-424] FET [s] 7.87\n[BBOX-425] FIF 50 [L/s] 1.35\n[BBOX-426] FIV1 [L] 1.10\n[BBOX-427] FIV1 % FVC [%] 40.89\n[BBOX-428] T IN [s] 1.21\n[BBOX-429] T EX [s] 1.30\n[BBOX-430] T TOT [s] 2.51\n[BBOX-431] MIF [L/s] 0.65\n[BBOX-432] MEF [L/s] 0.60\n[BBOX-433] MVV [L/min] 113.25 52.56 46.4\n[BBOX-434] FEF50 % FIF50 [%] 38.63\n[BBOX-435] V backextrapolation ex [L] 0.02\n[BBOX-436] V backextrapol. % FVC [%] 0.75\n[BBOX-437] 测试结果\n[BBOX-438] 1、重度阻塞性肺通气功能障碍，小气道功能降低。\n[BBOX-439] 2、肺弥散功能正常。\n[BBOX-440] 3、残气量正常，残气量/肺总量增高。\n[BBOX-441] 4、沙丁胺醇气雾剂支气管舒张试验呈阳性，FEV1.0改41.1%。\n[BBOX-442] 5、建议定期复查。\n[BBOX-443] 报告医师：\n[BBOX-444] 报告日期：2025.4.25\n[BBOX-445] TLC\n[BBOX-446] 6 Vol [L]\n[BBOX-447] FRCl eth\n[BBOX-448] R\n[BBOX-449] Time [min]\n[BBOX-450] PredA@0 0.2 0.4 0.6 0.8 1.0\n[BBOX-451] Flow [L/s]\n[BBOX-452] F/V ex\n[BBOX-453] 10\n[BBOX-454] 5\n[BBOX-455] 0\n[BBOX-456] 2\n[BBOX-457] 4\n[BBOX-458] 6\n[BBOX-459] 10\n[BBOX-460] F/V in\n[BBOX-461] Vol%VCmax\n[BBOX-462] 0\n[BBOX-463] 0\n[BBOX-464] Vol [L]\n[BBOX-465] 20\n[BBOX-466] 40\n[BBOX-467] 60\n[BBOX-468] 80\n[BBOX-469] 100\n[BBOX-470] 2\n[BBOX-471] VCmax\n[BBOX-472] 4\n[BBOX-473] 6\n[BBOX-474] 8\n[BBOX-475] Time [s]\n[BBOX-476] 8\n[BBOX-477] 4\n[BBOX-478] Vol [L]\n[BBOX-479] 2\n[BBOX-480] 0\n[BBOX-481] 2\n[BBOX-482] 4\n[BBOX-483] Time [s]\n[BBOX-484] 0\n[BBOX-485] 2\n[BBOX-486] 4\n[BBOX-487] 6\n[BBOX-488] 8\n[BBOX-489] 10\n[BBOX-490] 12\n[BBOX-491] 14"
  }
]
2026-08-10 13:09:09,048 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:09:09,068 INFO     29 [SmartSplitter] SmartSplitter done: 2 chunks from 2 LLM segments (all bbox_id). Types: {'OutpatientRecord': 1, 'ExaminationReport': 1}
2026-08-10 13:09:09,172 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 13:09:09,173 INFO     29 [Trace] task=90cba708 | doc=LTSH 三门峡.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "492 items", "markdown": "", "text": "", "name": "LTSH 三门峡.pdf", "output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}"}
2026-08-10 13:09:09,173 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 13:09:09,176 INFO     29 [ChunkRouter] Routed 2 chunks into 2 groups: {'chunks_Clinical': 1, 'chunks_Examination': 1}
2026-08-10 13:09:09,190 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 13:09:09,191 INFO     29 [Trace] task=90cba708 | doc=LTSH 三门峡.pdf | ChunkRouter:Router | outputs={"html": "", "json": "492 items", "markdown": "", "text": "", "name": "LTSH 三门峡.pdf", "output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:09:09,191 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 13:09:09,287 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:09:09,288 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:09:10,000 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:09:10,004 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 13:09:10,005 INFO     29 [Trace] task=90cba708 | doc=LTSH 三门峡.pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "492 items", "markdown": "", "text": "", "name": "LTSH 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:09:10,005 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 13:09:10,009 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:09:10,009 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:09:10,400 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:09:10,407 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 13:09:10,407 INFO     29 [Trace] task=90cba708 | doc=LTSH 三门峡.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "492 items", "markdown": "", "text": "", "name": "LTSH 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:09:10,407 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 13:09:10,411 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:09:10,412 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:09:10,412 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 13:09:10,412 INFO     29 [qwen-vl-text] positions(35): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:09:10,412 INFO     29 [qwen-vl-text] page grouping: [0, 1], lines per page: [27, 8]
2026-08-10 13:09:10,631 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:09:10,810 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:09:10,811 INFO     29 [qwen-vl-text] LLM extraction start, text_len=554
2026-08-10 13:09:10,811 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:09:10,811 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 34, \"encounter_dates\": [\"2025-05-27\"], \"department\": \"呼吸与危重症医学科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "渑池县人民医院\n门诊病历\n姓名:\n门诊号: 613003\n就诊时间:2025-05-27 14:24 科别: 呼吸与危重症医学科门诊\n姓名\n性别:男 年龄:56岁 婚否:已婚\n职业:农民 工作单位:无\n联系电话: 住址:河南省三门峡市渑池县仁村乡大\n水沟村八组8号\n病史叙述者:本人 身份证号:\n过敏史:无\n主诉:发作性胸闷、气喘4天。\n现病史:患者于4天前受凉后出现胸闷、气喘,活动后加重,伴有咳\n嗽,咳痰不明显,无胸痛、发热、咯血、盗汗等,未予治疗,症\n状持续无缓解。\n既往史:平素身体良好;无特殊疾病史;否认“肝炎、结核”等病史;\n否认手术史;否认外伤史;否认输血史及献血史;否认药物及食\n物过敏史;无预防接种史\n流行病学史:无\n体格检查:体温36.7℃,脉搏80次/分,呼吸22次/分,\n血压132/80mmHg,双肺呼吸音粗,可闻及哮鸣音,未闻及\n明显湿性啰音,心率80次/分,未闻及病理性杂音。\n辅助检查:肺功能四项+支气管舒张实验;沙丁胺醇气雾剂支气管舒\n张实验呈阳性,FEV1.0改善41.1%。\n初步诊断:门诊诊断:1.支气管哮喘。\n-1-\n渑池县人民医院\n门诊病历\n姓名：\n门诊号\n处理意见：1.避免受凉，避免进食刺激性食物，避免接触刺激性气味；\n2.如有不适，及时就医。\n经治医师：\n2",
    "role": "user"
  }
]
2026-08-10 13:09:12,865 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:09:12,865 INFO     29 [qwen-vl-text] LLM output (len=336):
{
  "encounter_date": "2025-05-27",
  "chief_complaint": "发作性胸闷、气喘4天。",
  "present_illness": "患者于4天前受凉后出现胸闷、气喘,活动后加重,伴有咳嗽,咳痰不明显,无胸痛、发热、咯血、盗汗等,未予治疗,症状持续无缓解。",
  "past_history": "平素身体良好;无特殊疾病史;否认“肝炎、结核”等病史;否认手术史;否认外伤史;否认输血史及献血史;否认药物及食物过敏史;无预防接种史",
  "diagnosis": "1.支气管哮喘。",
  "treatment_plan": "1.避免受凉，避免进食刺激性食物，避免接触刺激性气味；2.如有不适，及时就医。"
}
2026-08-10 13:09:12,865 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-05-27]
2026-08-10 13:09:12,867 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1931395, prompt_len=1173
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
2026-08-10 13:09:23,757 INFO     29 [qwen-vl-text] coord API raw response (len=1670):
[
	{"text": "渑池县人民医院", "bbox": [357, 209, 550, 230]},
	{"text": "门诊病历", "bbox": [378, 236, 530, 257]},
	{"text": "姓名:", "bbox": [172, 264, 216, 279]},
	{"text": "门诊号: 613003", "bbox": [453, 263, 583, 278]},
	{"text": "就诊时间:2025-05-27 14:24 科别: 呼吸与危重症医学科门诊", "bbox": [170, 294, 687, 310]},
	{"text": "姓名", "bbox": [168, 322, 204, 337]},
	{"text": "性别:男 年龄:56岁 婚否:已婚", "bbox": [300, 322, 644, 338]},
	{"text": "职业:农民 工作单位:无", "bbox": [166, 341, 520, 357]},
	{"text": "联系电话: 住址:河南省三门峡市渑池县仁村乡大", "bbox": [165, 360, 730, 375]},
	{"text": "水沟村八组8号", "bbox": [163, 379, 298, 394]},
	{"text": "病史叙述者:本人 身份证号:", "bbox": [161, 398, 491, 414]},
	{"text": "过敏史:无", "bbox": [159, 417, 258, 433]},
	{"text": "主诉:发作性胸闷、气喘4天。", "bbox": [159, 446, 413, 462]},
	{"text": "现病史:患者于4天前受凉后出现胸闷、气喘,活动后加重,伴有咳", "bbox": [157, 466, 733, 482]},
	{"text": "嗽,咳痰不明显,无胸痛、发热、咯血、盗汗等,未予治疗,症", "bbox": [193, 485, 744, 501]},
	{"text": "状持续无缓解。", "bbox": [192, 505, 322, 521]},
	{"text": "既往史:平素身体良好;无特殊疾病史;否认“肝炎、结核”等病史;", "bbox": [152, 525, 754, 541]},
	{"text": "否认手术史;否认外伤史;否认输血史及献血史;否认药物及食", "bbox": [190, 545, 748, 562]},
	{"text": "物过敏史;无预防接种史", "bbox": [188, 567, 412, 583]},
	{"text": "流行病学史:无", "bbox": [147, 589, 290, 605]},
	{"text": "体格检查:体温36.7℃,脉搏80次/分,呼吸22次/分,", "bbox": [144, 610, 607, 627]},
	{"text": "血压132/80mmHg,双肺呼吸音粗,可闻及哮鸣音,未闻及", "bbox": [245, 631, 754, 649]},
	{"text": "明显湿性啰音,心率80次/分,未闻及病理性杂音。", "bbox": [182, 654, 633, 671]},
	{"text": "辅助检查:肺功能四项+支气管舒张实验;沙丁胺醇气雾剂支气管舒", "bbox": [138, 676, 747, 693]},
	{"text": "张实验呈阳性,FEV1.0改善41.1%。", "bbox": [177, 700, 491, 717]},
	{"text": "初步诊断:门诊诊断:1.支气管哮喘。", "bbox": [135, 722, 471, 740]},
	{"text": "-1-", "bbox": [428, 780, 475, 792]}
]
2026-08-10 13:09:23,758 INFO     29 [qwen-vl-text] coord API: raw_items=27, valid_items=27, elapsed=10.9s
2026-08-10 13:09:23,758 INFO     29 [qwen-vl-text] coord item[0]: text=渑池县人民医院, bbox=[357, 209, 550, 230]
2026-08-10 13:09:23,758 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[378, 236, 530, 257]
2026-08-10 13:09:23,758 INFO     29 [qwen-vl-text] coord item[2]: text=姓名:, bbox=[172, 264, 216, 279]
2026-08-10 13:09:23,758 INFO     29 [qwen-vl-text] coord item[3]: text=门诊号: 613003, bbox=[453, 263, 583, 278]
2026-08-10 13:09:23,758 INFO     29 [qwen-vl-text] coord item[4]: text=就诊时间:2025-05-27 14:24 科别: 呼吸与危重症医学科门诊, bbox=[170, 294, 687, 310]
2026-08-10 13:09:23,758 INFO     29 [qwen-vl-text] coord item[5]: text=姓名, bbox=[168, 322, 204, 337]
2026-08-10 13:09:23,758 INFO     29 [qwen-vl-text] coord item[6]: text=性别:男 年龄:56岁 婚否:已婚, bbox=[300, 322, 644, 338]
2026-08-10 13:09:23,758 INFO     29 [qwen-vl-text] coord item[7]: text=职业:农民 工作单位:无, bbox=[166, 341, 520, 357]
2026-08-10 13:09:23,758 INFO     29 [qwen-vl-text] coord item[8]: text=联系电话: 住址:河南省三门峡市渑池县仁村乡大, bbox=[165, 360, 730, 375]
2026-08-10 13:09:23,758 INFO     29 [qwen-vl-text] coord item[9]: text=水沟村八组8号, bbox=[163, 379, 298, 394]
2026-08-10 13:09:23,758 INFO     29 [qwen-vl-text] coord item[10]: text=病史叙述者:本人 身份证号:, bbox=[161, 398, 491, 414]
2026-08-10 13:09:23,758 INFO     29 [qwen-vl-text] coord item[11]: text=过敏史:无, bbox=[159, 417, 258, 433]
2026-08-10 13:09:23,758 INFO     29 [qwen-vl-text] coord item[12]: text=主诉:发作性胸闷、气喘4天。, bbox=[159, 446, 413, 462]
2026-08-10 13:09:23,758 INFO     29 [qwen-vl-text] coord item[13]: text=现病史:患者于4天前受凉后出现胸闷、气喘,活动后加重,伴有咳, bbox=[157, 466, 733, 482]
2026-08-10 13:09:23,758 INFO     29 [qwen-vl-text] coord item[14]: text=嗽,咳痰不明显,无胸痛、发热、咯血、盗汗等,未予治疗,症, bbox=[193, 485, 744, 501]
2026-08-10 13:09:23,758 INFO     29 [qwen-vl-text] coord item[15]: text=状持续无缓解。, bbox=[192, 505, 322, 521]
2026-08-10 13:09:23,758 INFO     29 [qwen-vl-text] coord item[16]: text=既往史:平素身体良好;无特殊疾病史;否认“肝炎、结核”等病史;, bbox=[152, 525, 754, 541]
2026-08-10 13:09:23,758 INFO     29 [qwen-vl-text] coord item[17]: text=否认手术史;否认外伤史;否认输血史及献血史;否认药物及食, bbox=[190, 545, 748, 562]
2026-08-10 13:09:23,759 INFO     29 [qwen-vl-text] coord item[18]: text=物过敏史;无预防接种史, bbox=[188, 567, 412, 583]
2026-08-10 13:09:23,759 INFO     29 [qwen-vl-text] coord item[19]: text=流行病学史:无, bbox=[147, 589, 290, 605]
2026-08-10 13:09:23,759 INFO     29 [qwen-vl-text] coord item[20]: text=体格检查:体温36.7℃,脉搏80次/分,呼吸22次/分,, bbox=[144, 610, 607, 627]
2026-08-10 13:09:23,759 INFO     29 [qwen-vl-text] coord item[21]: text=血压132/80mmHg,双肺呼吸音粗,可闻及哮鸣音,未闻及, bbox=[245, 631, 754, 649]
2026-08-10 13:09:23,759 INFO     29 [qwen-vl-text] coord item[22]: text=明显湿性啰音,心率80次/分,未闻及病理性杂音。, bbox=[182, 654, 633, 671]
2026-08-10 13:09:23,759 INFO     29 [qwen-vl-text] coord item[23]: text=辅助检查:肺功能四项+支气管舒张实验;沙丁胺醇气雾剂支气管舒, bbox=[138, 676, 747, 693]
2026-08-10 13:09:23,759 INFO     29 [qwen-vl-text] coord item[24]: text=张实验呈阳性,FEV1.0改善41.1%。, bbox=[177, 700, 491, 717]
2026-08-10 13:09:23,759 INFO     29 [qwen-vl-text] coord item[25]: text=初步诊断:门诊诊断:1.支气管哮喘。, bbox=[135, 722, 471, 740]
2026-08-10 13:09:23,759 INFO     29 [qwen-vl-text] coord item[26]: text=-1-, bbox=[428, 780, 475, 792]
2026-08-10 13:09:23,760 INFO     29 [qwen-vl-text] page=0 — 27/27 coords, api_time=10.9s
2026-08-10 13:09:23,765 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1603850, prompt_len=710
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
2026-08-10 13:09:27,113 INFO     29 [qwen-vl-text] coord API raw response (len=441):
```json
[
	{"text": "渑池县人民医院", "bbox": [399, 233, 583, 251]},
	{"text": "门诊病历", "bbox": [418, 258, 564, 278]},
	{"text": "姓名：", "bbox": [222, 286, 265, 299]},
	{"text": "门诊号", "bbox": [490, 285, 542, 299]},
	{"text": "处理意见：1.避免受凉，避免进食刺激性食物，避免接触刺激性气味；", "bbox": [220, 315, 766, 329]},
	{"text": "2.如有不适，及时就医。", "bbox": [308, 334, 498, 347]},
	{"text": "经治医师：", "bbox": [508, 357, 638, 373]},
	{"text": "2", "bbox": [479, 780, 492, 791]}
]
```
2026-08-10 13:09:27,114 INFO     29 [qwen-vl-text] coord API: raw_items=8, valid_items=8, elapsed=3.3s
2026-08-10 13:09:27,114 INFO     29 [qwen-vl-text] coord item[0]: text=渑池县人民医院, bbox=[399, 233, 583, 251]
2026-08-10 13:09:27,114 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[418, 258, 564, 278]
2026-08-10 13:09:27,114 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[222, 286, 265, 299]
2026-08-10 13:09:27,114 INFO     29 [qwen-vl-text] coord item[3]: text=门诊号, bbox=[490, 285, 542, 299]
2026-08-10 13:09:27,114 INFO     29 [qwen-vl-text] coord item[4]: text=处理意见：1.避免受凉，避免进食刺激性食物，避免接触刺激性气味；, bbox=[220, 315, 766, 329]
2026-08-10 13:09:27,114 INFO     29 [qwen-vl-text] coord item[5]: text=2.如有不适，及时就医。, bbox=[308, 334, 498, 347]
2026-08-10 13:09:27,114 INFO     29 [qwen-vl-text] coord item[6]: text=经治医师：, bbox=[508, 357, 638, 373]
2026-08-10 13:09:27,114 INFO     29 [qwen-vl-text] coord item[7]: text=2, bbox=[479, 780, 492, 791]
2026-08-10 13:09:27,115 INFO     29 [qwen-vl-text] page=1 — 8/8 coords, api_time=3.3s
2026-08-10 13:09:27,115 INFO     29 [qwen-vl-text] new_positions (35):
[[0, 212.415, 327.25, 175.97799999999998, 193.66], [0, 224.91, 315.34999999999997, 198.712, 216.394], [0, 102.33999999999999, 128.51999999999998, 222.28799999999998, 234.91799999999998], [0, 269.53499999999997, 346.885, 221.446, 234.076], [0, 101.14999999999999, 408.765, 247.548, 261.02], [0, 99.96, 121.38, 271.12399999999997, 283.75399999999996], [0, 178.5, 383.18, 271.12399999999997, 284.596], [0, 98.77, 309.4, 287.122, 300.594], [0, 98.175, 434.34999999999997, 303.12, 315.75], [0, 96.985, 177.31, 319.118, 331.748], [0, 95.795, 292.145, 335.116, 348.58799999999997], [0, 94.60499999999999, 153.51, 351.114, 364.586], [0, 94.60499999999999, 245.73499999999999, 375.532, 389.00399999999996], [0, 93.41499999999999, 436.135, 392.372, 405.844], [0, 114.835, 442.68, 408.37, 421.842], [0, 114.24, 191.59, 425.21, 438.68199999999996], [0, 90.44, 448.63, 442.05, 455.522], [0, 113.05, 445.06, 458.89, 473.204], [0, 111.86, 245.14, 477.414, 490.88599999999997], [0, 87.46499999999999, 172.54999999999998, 495.938, 509.40999999999997], [0, 85.67999999999999, 361.16499999999996, 513.62, 527.934], [0, 145.775, 448.63, 531.302, 546.458], [0, 108.28999999999999, 376.635, 550.668, 564.982], [0, 82.11, 444.465, 569.192, 583.506], [0, 105.315, 292.145, 589.4, 603.7139999999999], [0, 80.325, 280.245, 607.924, 623.0799999999999], [0, 254.66, 282.625, 656.76, 666.864], [1, 237.405, 346.885, 196.186, 211.34199999999998], [1, 248.70999999999998, 335.58, 217.236, 234.076], [1, 132.09, 157.67499999999998, 240.81199999999998, 251.75799999999998], [1, 291.55, 322.49, 239.97, 251.75799999999998], [1, 130.9, 455.77, 265.23, 277.018], [1, 183.26, 296.31, 281.228, 292.174], [1, 302.26, 379.60999999999996, 300.594, 314.066], [1, 285.005, 292.74, 656.76, 666.0219999999999]]
2026-08-10 13:09:27,115 INFO     29 [qwen-vl-text] ═══ DONE ═══ 35 positions, pages=2, time=16.7s
2026-08-10 13:09:27,134 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 13:09:27,134 INFO     29 [Trace] task=90cba708 | doc=LTSH 三门峡.pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "492 items", "markdown": "", "text": "", "name": "LTSH 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:09:27,134 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 13:09:27,135 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:09:27.134+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 40, "failed": 0, "current": {"90cba70894bc11f1bd9827cf206dfa2d": {"id": "90cba70894bc11f1bd9827cf206dfa2d", "doc_id": "907f140694bc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LTSH \u4e09\u95e8\u5ce1.pdf", "type": "pdf", "location": "LTSH \u4e09\u95e8\u5ce1.pdf", "size": 6636575, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786367302926, "task_type": "dataflow", "root_trace_id": "3e86fc61695b452a8b4ef13e7466fe92", "root_traceparent": "00-3e86fc61695b452a8b4ef13e7466fe92-eb986cfdcd997396-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:09:27,141 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:09:27,141 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:09:28,284 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:09:28,291 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 13:09:28,292 INFO     29 [Trace] task=90cba708 | doc=LTSH 三门峡.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "492 items", "markdown": "", "text": "", "name": "LTSH 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:09:28,292 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 13:09:28,297 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:09:28,297 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:09:28,737 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:09:28,748 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 13:09:28,748 INFO     29 [Trace] task=90cba708 | doc=LTSH 三门峡.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "492 items", "markdown": "", "text": "", "name": "LTSH 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:09:28,748 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 13:09:28,755 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:09:28,755 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:09:29,242 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:09:29,246 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 13:09:29,247 INFO     29 [Trace] task=90cba708 | doc=LTSH 三门峡.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "492 items", "markdown": "", "text": "", "name": "LTSH 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:09:29,247 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 13:09:29,251 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:09:29,251 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:09:29,727 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:09:29,736 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 13:09:29,736 INFO     29 [Trace] task=90cba708 | doc=LTSH 三门峡.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "492 items", "markdown": "", "text": "", "name": "LTSH 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:09:29,737 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 13:09:29,745 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:09:29,746 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:09:29,746 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 13:09:29,746 INFO     29 [qwen-vl-text] positions(457): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:09:29,746 INFO     29 [qwen-vl-text] page grouping: [2, 3, 4], lines per page: [198, 146, 113]
2026-08-10 13:09:30,039 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:09:30,227 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:09:30,535 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 13:09:30,536 INFO     29 [qwen-vl-text] LLM extraction start, text_len=3332
2026-08-10 13:09:30,536 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:09:30,536 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 35, \"bbox_end\": 491, \"encounter_dates\": [\"2025-04-25\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "JAEGE R PCMED\n渑池县人民医院\n肺功能检查报告\n综合测试\n姓名：\n性别：男\n年龄：56 Years\n身高：165 cm\n体重：70 kg\n备注：\n联系电话：\n住院号：0\n测试号：\n吸烟史：\n既往史：\n职业：\n测试日期\n测试时间\n预计值\n实测值\n实/预\nVC MAX\n[L]\n3.85\n2.72\n70.6\nFVC\n[L]\n3.71\n2.68\n72.2\nMV\n[L/min]\n10.00\n18.75\n187.5\nFEV 1\n[L]\n2.98\n1.10\n36.9\nFEV 1 % FVC\n[%]\n83.77\n41.10\n49.1\nPEF\n[L/s]\n7.87\n2.33\n29.6\nMEF 75\n[L/s]\n6.92\n0.96\n13.9\nMEF 50\n[L/s]\n4.17\n0.52\n12.5\nMEF 25\n[L/s]\n1.51\n0.22\n14.3\nMMEF 75/25\n[L/s]\n3.49\n0.44\n12.6\nMVV\n[L/min]\n113.25\n52.56\n46.4\nTLC-SB\n[L]\n6.10\n5.24\n85.9\nRV-SB\n[L]\n2.16\n2.69\n124.4\nRV%TLC-SB\n[%]\n35.80\n51.32\n143.4\nFRC-SB\n[L]\n3.28\n3.71\n113.3\nFRC%TLC-SB\n[%]\n55.56\n70.79\n127.4\nDLCO SB [mmol/min/kPa]\n8.61\n7.20\n83.7\nDLCO/Va mmol/min/kPa/L]\n1.41\n1.42\n100.4\nHb\n[g/100ml]\n14.60\nVA\n[L]\n5.95\n5.09\n85.5\nDLCOc SB [mmol/min/kPa]\n8.61\n7.20\n83.7\nDLCOc/Va mmol/min/kPa/L]\n1.41\n1.42\n100.4\nVIN\n[L]\n3.85\n2.55\n66.3\nInsp. time\n[s]\n1.52\nExp. time\n[s]\n2.15\nSample vol\n[L]\nSystem dead space [ml]\n172.00\nAnatom. dead space[ml]\n154.00\nTA\n[s]\n11.54\n测试结果：\nTLC\n6\nVol [L]\nFRCPleth\n25/4/25\n9:19:05上午\nRW\nPredAdt.0\n0.2\n0.4\n0.6\n0.8\n1.0\nTime [min]\nFlow [L/s]\nF/V ex\n10\n5\n0\n2\n4\n6\n1\n5\n10\nF/V in\nVol [L]\n100\n10\n50\n100\nTime [s]\n0\n2\n4\n6\n8\n10\n0\nVolume [L]\n4\n2\n0\n1\n2\n4\nTime [s]\n10\n20\n30\n40\n0\nJAEGE R PCMED\n渑池县人民医院\n肺功能检查报告\n舒张试验\n姓名：\n科别：\n住院号：0\n测试号：2025042503\n性别：男\n年龄：56 Years\n身高：165 cm\n体重：70 kg\n标准体重：108 %\n体表面积：1.77 m\n吸烟史：\nFlow [L/s]\nF/V ex\nVol%VCmax\nVol [L]\n10\n20\n40\n60\n80\n100\n2\nVCmax\n1\n1\n0\n2\n3\n4\n5\n6\n7\n1\n2\n4\n5\n6\n10\nTime [s]\nF/V in\n8\n0\n1\n2\n3\n4\n5\n6\n7\n8\n预计值\n前次\n前/预\n后次\n后/预\n改善率\n测试日期\n25/4/25\n25/4/25\n测试时间\n9:19:05\n9:43:24\nVC MAX\n[L]\n3.85\n2.72\n70.6\n3.07\n79.9\n13.2\nFVC\n[L]\n3.71\n2.68\n72.2\n3.05\n82.4\n14.1\nFEV 1\n[L]\n2.98\n1.10\n36.9\n1.55\n52.1\n41.1\nFEV 1 % FVC\n[%]\n83.77\n41.10\n49.1\n50.82\n60.7\n23.6\nFEV 1 % VC MAX\n[%]\n77.13\n40.51\n52.5\n50.49\n65.5\n24.6\nPEF\n[L/s]\n7.87\n2.33\n29.6\n3.18\n40.4\n36.6\nMEF 75\n[L/s]\n6.92\n0.96\n13.9\n1.65\n23.9\n72.1\nMEF 50\n[L/s]\n4.17\n0.52\n12.5\n0.85\n20.3\n63.0\nMEF 25\n[L/s]\n1.51\n0.22\n14.3\n0.35\n23.2\n62.9\nMMEF 75/25\n[L/s]\n3.49\n0.44\n12.6\n0.75\n21.3\n69.5\nJAEGER PCMED\n渑池县人民医院\n肺功能检查报告\n常规通气\n姓名：\n住院号：0\n性别：男\n身高：165 cm\n标准体重：108 %\n吸烟史：\n科别：\n测试号：2025042503\n年龄：56 Years\n体重：70 kg\n体表面积：1.77 m\n预计值 实测值 实测/预\n测试日期 25/4/25\n测试时间 9:19:05]\nVC MAX [L] 3.85 2.72 70.6\nIRV [L] 0.91\nERV [L] 1.11 1.02 91.8\nIC [L] 2.74 1.69 61.9\nVT [L] 0.50 0.78 156.7\nMV [L/min] 10.00 18.75 187.5\nVC IN [L] 3.85 2.69 70.0\nVC EX [L] 3.85 2.72 70.6\nBF [1/min] 20.00 23.93 119.7\nFVC [L] 3.71 2.68 72.2\nPEF [L/s] 7.87 2.33 29.6\nFEV 0.5 [L] 0.70\nFEV 1 [L] 2.98 1.10 36.9\nFEV 2 [L] 1.60\nFEV 3 [L] 1.91\nFEV6 [L] 2.45\nFEF 200-1200 [L/s] 0.94\nFEV 1 % FVC [%] 83.77 41.10 49.1\nFEV 1 % VC MAX [%] 77.13 40.51 52.5\nMEF 75 [L/s] 6.92 0.96 13.9\nMEF 50 [L/s] 4.17 0.52 12.5\nMEF 25 [L/s] 1.51 0.22 14.3\nMMEF 75/25 [L/s] 3.49 0.44 12.6\nFEF 75/85 [L/s] 0.77 0.18 23.0\nFEF50 % FIF50 [%] 38.63\nPIF [L/s] 1.41\nFVC IN [L] 3.85 2.69 70.0\nFET [s] 7.87\nFIF 50 [L/s] 1.35\nFIV1 [L] 1.10\nFIV1 % FVC [%] 40.89\nT IN [s] 1.21\nT EX [s] 1.30\nT TOT [s] 2.51\nMIF [L/s] 0.65\nMEF [L/s] 0.60\nMVV [L/min] 113.25 52.56 46.4\nFEF50 % FIF50 [%] 38.63\nV backextrapolation ex [L] 0.02\nV backextrapol. % FVC [%] 0.75\n测试结果\n1、重度阻塞性肺通气功能障碍，小气道功能降低。\n2、肺弥散功能正常。\n3、残气量正常，残气量/肺总量增高。\n4、沙丁胺醇气雾剂支气管舒张试验呈阳性，FEV1.0改41.1%。\n5、建议定期复查。\n报告医师：\n报告日期：2025.4.25\nTLC\n6 Vol [L]\nFRCl eth\nR\nTime [min]\nPredA@0 0.2 0.4 0.6 0.8 1.0\nFlow [L/s]\nF/V ex\n10\n5\n0\n2\n4\n6\n10\nF/V in\nVol%VCmax\n0\n0\nVol [L]\n20\n40\n60\n80\n100\n2\nVCmax\n4\n6\n8\nTime [s]\n8\n4\nVol [L]\n2\n0\n2\n4\nTime [s]\n0\n2\n4\n6\n8\n10\n12\n14",
    "role": "user"
  }
]
2026-08-10 13:09:54,712 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:09:54,712 INFO     29 [qwen-vl-text] LLM output (len=4111):
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
  "findings": "综合测试\n测试日期: 25/4/25\n测试时间: 9:19:05上午\n\n| 指标 | 预计值 | 实测值 | 实/预 | 单位 |\n| :--- | :--- | :--- | :--- | :--- |\n| VC MAX | 3.85 | 2.72 | 70.6 | [L] |\n| FVC | 3.71 | 2.68 | 72.2 | [L] |\n| MV | 10.00 | 18.75 | 187.5 | [L/min] |\n| FEV 1 | 2.98 | 1.10 | 36.9 | [L] |\n| FEV 1 % FVC | 83.77 | 41.10 | 49.1 | [%] |\n| PEF | 7.87 | 2.33 | 29.6 | [L/s] |\n| MEF 75 | 6.92 | 0.96 | 13.9 | [L/s] |\n| MEF 50 | 4.17 | 0.52 | 12.5 | [L/s] |\n| MEF 25 | 1.51 | 0.22 | 14.3 | [L/s] |\n| MMEF 75/25 | 3.49 | 0.44 | 12.6 | [L/s] |\n| MVV | 113.25 | 52.56 | 46.4 | [L/min] |\n| TLC-SB | 6.10 | 5.24 | 85.9 | [L] |\n| RV-SB | 2.16 | 2.69 | 124.4 | [L] |\n| RV%TLC-SB | 35.80 | 51.32 | 143.4 | [%] |\n| FRC-SB | 3.28 | 3.71 | 113.3 | [L] |\n| FRC%TLC-SB | 55.56 | 70.79 | 127.4 | [%] |\n| DLCO SB | 8.61 | 7.20 | 83.7 | [mmol/min/kPa] |\n| DLCO/Va | 1.41 | 1.42 | 100.4 | [mmol/min/kPa/L] |\n| Hb | 14.60 | - | - | [g/100ml] |\n| VA | 5.95 | 5.09 | 85.5 | [L] |\n| DLCOc SB | 8.61 | 7.20 | 83.7 | [mmol/min/kPa] |\n| DLCOc/Va | 1.41 | 1.42 | 100.4 | [mmol/min/kPa/L] |\n| VIN | 3.85 | 2.55 | 66.3 | [L] |\n| Insp. time | - | 1.52 | - | [s] |\n| Exp. time | - | 2.15 | - | [s] |\n| System dead space | - | 172.00 | - | [ml] |\n| Anatom. dead space | - | 154.00 | - | [ml] |\n| TA | - | 11.54 | - | [s] |\n\n舒张试验\n测试日期: 25/4/25\n测试时间: 9:19:05 (前次), 9:43:24 (后次)\n\n| 指标 | 预计值 | 前次实测 | 前/预 | 后次实测 | 后/预 | 改善率 | 单位 |\n| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n| VC MAX | 3.85 | 2.72 | 70.6 | 3.07 | 79.9 | 13.2 | [L] |\n| FVC | 3.71 | 2.68 | 72.2 | 3.05 | 82.4 | 14.1 | [L] |\n| FEV 1 | 2.98 | 1.10 | 36.9 | 1.55 | 52.1 | 41.1 | [L] |\n| FEV 1 % FVC | 83.77 | 41.10 | 49.1 | 50.82 | 60.7 | 23.6 | [%] |\n| FEV 1 % VC MAX | 77.13 | 40.51 | 52.5 | 50.49 | 65.5 | 24.6 | [%] |\n| PEF | 7.87 | 2.33 | 29.6 | 3.18 | 40.4 | 36.6 | [L/s] |\n| MEF 75 | 6.92 | 0.96 | 13.9 | 1.65 | 23.9 | 72.1 | [L/s] |\n| MEF 50 | 4.17 | 0.52 | 12.5 | 0.85 | 20.3 | 63.0 | [L/s] |\n| MEF 25 | 1.51 | 0.22 | 14.3 | 0.35 | 23.2 | 62.9 | [L/s] |\n| MMEF 75/25 | 3.49 | 0.44 | 12.6 | 0.75 | 21.3 | 69.5 | [L/s] |\n\n常规通气\n测试日期: 25/4/25\n测试时间: 9:19:05\n\n| 指标 | 预计值 | 实测值 | 实测/预 | 单位 |\n| :--- | :--- | :--- | :--- | :--- |\n| VC MAX | 3.85 | 2.72 | 70.6 | [L] |\n| IRV | 0.91 | - | - | [L] |\n| ERV | 1.11 | 1.02 | 91.8 | [L] |\n| IC | 2.74 | 1.69 | 61.9 | [L] |\n| VT | 0.50 | 0.78 | 156.7 | [L] |\n| MV | 10.00 | 18.75 | 187.5 | [L/min] |\n| VC IN | 3.85 | 2.69 | 70.0 | [L] |\n| VC EX | 3.85 | 2.72 | 70.6 | [L] |\n| BF | 20.00 | 23.93 | 119.7 | [1/min] |\n| FVC | 3.71 | 2.68 | 72.2 | [L] |\n| PEF | 7.87 | 2.33 | 29.6 | [L/s] |\n| FEV 0.5 | 0.70 | - | - | [L] |\n| FEV 1 | 2.98 | 1.10 | 36.9 | [L] |\n| FEV 2 | 1.60 | - | - | [L] |\n| FEV 3 | 1.91 | - | - | [L] |\n| FEV6 | 2.45 | - | - | [L] |\n| FEF 200-1200 | 0.94 | - | - | [L/s] |\n| FEV 1 % FVC | 83.77 | 41.10 | 49.1 | [%] |\n| FEV 1 % VC MAX | 77.13 | 40.51 | 52.5 | [%] |\n| MEF 75 | 6.92 | 0.96 | 13.9 | [L/s] |\n| MEF 50 | 4.17 | 0.52 | 12.5 | [L/s] |\n| MEF 25 | 1.51 | 0.22 | 14.3 | [L/s] |\n| MMEF 75/25 | 3.49 | 0.44 | 12.6 | [L/s] |\n| FEF 75/85 | 0.77 | 0.18 | 23.0 | [L/s] |\n| FEF50 % FIF50 | 38.63 | - | - | [%] |\n| PIF | 1.41 | - | - | [L/s] |\n| FVC IN | 3.85 | 2.69 | 70.0 | [L] |\n| FET | 7.87 | - | - | [s] |\n| FIF 50 | 1.35 | - | - | [L/s] |\n| FIV1 | 1.10 | - | - | [L] |\n| FIV1 % FVC | 40.89 | - | - | [%] |\n| T IN | 1.21 | - | - | [s] |\n| T EX | 1.30 | - | - | [s] |\n| T TOT | 2.51 | - | - | [s] |\n| MIF | 0.65 | - | - | [L/s] |\n| MEF | 0.60 | - | - | [L/s] |\n| MVV | 113.25 | 52.56 | 46.4 | [L/min] |\n| FEF50 % FIF50 | 38.63 | - | - | [%] |\n| V backextrapolation ex | 0.02 | - | - | [L] |\n| V backextrapol. % FVC | 0.75 | - | - | [%] |",
  "conclusion": "测试结果\n1、重度阻塞性肺通气功能障碍，小气道功能降低。\n2、肺弥散功能正常。\n3、残气量正常，残气量/肺总量增高。\n4、沙丁胺醇气雾剂支气管舒张试验呈阳性，FEV1.0改41.1%。\n5、建议定期复查。",
  "physician": null,
  "reviewer": null
}
2026-08-10 13:09:54,717 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2543785, prompt_len=2367
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共198行）
["JAEGE R PCMED", "渑池县人民医院", "肺功能检查报告", "综合测试", "姓名：", "性别：男", "年龄：56 Years", "身高：165 cm", "体重：70 kg", "备注：", "联系电话：", "住院号：0", "测试号：", "吸烟史：", "既往史：", "职业：", "测试日期", "测试时间", "预计值", "实测值", "实/预", "VC MAX", "[L]", "3.85", "2.72", "70.6", "FVC", "[L]", "3.71", "2.68", "72.2", "MV", "[L/min]", "10.00", "18.75", "187.5", "FEV 1", "[L]", "2.98", "1.10", "36.9", "FEV 1 % FVC", "[%]", "83.77", "41.10", "49.1", "PEF", "[L/s]", "7.87", "2.33", "29.6", "MEF 75", "[L/s]", "6.92", "0.96", "13.9", "MEF 50", "[L/s]", "4.17", "0.52", "12.5", "MEF 25", "[L/s]", "1.51", "0.22", "14.3", "MMEF 75/25", "[L/s]", "3.49", "0.44", "12.6", "MVV", "[L/min]", "113.25", "52.56", "46.4", "TLC-SB", "[L]", "6.10", "5.24", "85.9", "RV-SB", "[L]", "2.16", "2.69", "124.4", "RV%TLC-SB", "[%]", "35.80", "51.32", "143.4", "FRC-SB", "[L]", "3.28", "3.71", "113.3", "FRC%TLC-SB", "[%]", "55.56", "70.79", "127.4", "DLCO SB [mmol/min/kPa]", "8.61", "7.20", "83.7", "DLCO/Va mmol/min/kPa/L]", "1.41", "1.42", "100.4", "Hb", "[g/100ml]", "14.60", "VA", "[L]", "5.95", "5.09", "85.5", "DLCOc SB [mmol/min/kPa]", "8.61", "7.20", "83.7", "DLCOc/Va mmol/min/kPa/L]", "1.41", "1.42", "100.4", "VIN", "[L]", "3.85", "2.55", "66.3", "Insp. time", "[s]", "1.52", "Exp. time", "[s]", "2.15", "Sample vol", "[L]", "System dead space [ml]", "172.00", "Anatom. dead space[ml]", "154.00", "TA", "[s]", "11.54", "测试结果：", "TLC", "6", "Vol [L]", "FRCPleth", "25/4/25", "9:19:05上午", "RW", "PredAdt.0", "0.2", "0.4", "0.6", "0.8", "1.0", "Time [min]", "Flow [L/s]", "F/V ex", "10", "5", "0", "2", "4", "6", "1", "5", "10", "F/V in", "Vol [L]", "100", "10", "50", "100", "Time [s]", "0", "2", "4", "6", "8", "10", "0", "Volume [L]", "4", "2", "0", "1", "2", "4", "Time [s]", "10", "20", "30", "40", "0"]

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
2026-08-10 13:10:43,435 INFO     29 [qwen-vl-text] coord API raw response (len=9785):
[
	{"text": "JAEGE R PCMED", "bbox": [708, 43, 896, 57]},
	{"text": "渑池县人民医院", "bbox": [380, 57, 592, 78]},
	{"text": "肺功能检查报告", "bbox": [414, 80, 562, 97]},
	{"text": "综合测试", "bbox": [455, 101, 541, 116]},
	{"text": "姓名：", "bbox": [81, 119, 127, 131]},
	{"text": "性别：男", "bbox": [81, 131, 266, 143]},
	{"text": "年龄：56 Years", "bbox": [81, 143, 324, 155]},
	{"text": "身高：165 cm", "bbox": [81, 155, 307, 167]},
	{"text": "体重：70 kg", "bbox": [81, 167, 297, 179]},
	{"text": "备注：", "bbox": [81, 179, 127, 190]},
	{"text": "联系电话：", "bbox": [424, 119, 507, 131]},
	{"text": "住院号：0", "bbox": [424, 131, 598, 143]},
	{"text": "测试号：", "bbox": [424, 143, 490, 155]},
	{"text": "吸烟史：", "bbox": [424, 155, 490, 167]},
	{"text": "既往史：", "bbox": [424, 167, 490, 179]},
	{"text": "职业：", "bbox": [424, 179, 471, 190]},
	{"text": "测试日期", "bbox": [75, 222, 159, 234]},
	{"text": "测试时间", "bbox": [75, 234, 159, 246]},
	{"text": "预计值", "bbox": [356, 210, 419, 222]},
	{"text": "实测值", "bbox": [468, 210, 529, 222]},
	{"text": "实/预", "bbox": [580, 210, 630, 222]},
	{"text": "TLC", "bbox": [635, 214, 656, 224]},
	{"text": "6", "bbox": [661, 210, 670, 218], "label": "数字"},
	{"text": "Vol [L]", "bbox": [675, 212, 708, 222]},
	{"text": "25/4/25", "bbox": [459, 224, 530, 234]},
	{"text": "9:19:05上午", "bbox": [428, 236, 532, 246]},
	{"text": "VC MAX", "bbox": [67, 259, 134, 269]},
	{"text": "[L]", "bbox": [272, 259, 300, 270]},
	{"text": "3.85", "bbox": [376, 259, 418, 269]},
	{"text": "2.72", "bbox": [490, 259, 532, 269]},
	{"text": "70.6", "bbox": [593, 259, 635, 269]},
	{"text": "FVC", "bbox": [65, 271, 100, 281]},
	{"text": "[L]", "bbox": [272, 271, 300, 282]},
	{"text": "3.71", "bbox": [376, 271, 418, 281]},
	{"text": "2.68", "bbox": [490, 271, 532, 281]},
	{"text": "72.2", "bbox": [593, 271, 635, 281]},
	{"text": "MV", "bbox": [63, 284, 88, 294]},
	{"text": "[L/min]", "bbox": [228, 284, 298, 295]},
	{"text": "10.00", "bbox": [366, 284, 418, 294]},
	{"text": "18.75", "bbox": [482, 284, 532, 294]},
	{"text": "187.5", "bbox": [585, 284, 635, 294]},
	{"text": "FEV 1", "bbox": [63, 297, 117, 307]},
	{"text": "[L]", "bbox": [272, 297, 300, 308]},
	{"text": "2.98", "bbox": [376, 297, 418, 307]},
	{"text": "1.10", "bbox": [490, 297, 532, 307]},
	{"text": "36.9", "bbox": [595, 297, 637, 307]},
	{"text": "FEV 1 % FVC", "bbox": [63, 310, 182, 321]},
	{"text": "[%]", "bbox": [272, 310, 300, 321]},
	{"text": "83.77", "bbox": [366, 310, 418, 321]},
	{"text": "41.10", "bbox": [482, 310, 532, 321]},
	{"text": "49.1", "bbox": [595, 310, 637, 321]},
	{"text": "PEF", "bbox": [63, 325, 95, 335]},
	{"text": "[L/s]", "bbox": [250, 325, 298, 336]},
	{"text": "7.87", "bbox": [376, 325, 418, 335]},
	{"text": "2.33", "bbox": [490, 325, 532, 335]},
	{"text": "29.6", "bbox": [595, 325, 637, 335]},
	{"text": "MEF 75", "bbox": [63, 340, 127, 350]},
	{"text": "[L/s]", "bbox": [250, 340, 298, 351]},
	{"text": "6.92", "bbox": [376, 340, 418, 350]},
	{"text": "0.96", "bbox": [490, 340, 532, 350]},
	{"text": "13.9", "bbox": [595, 340, 637, 350]},
	{"text": "MEF 50", "bbox": [63, 354, 127, 365]},
	{"text": "[L/s]", "bbox": [250, 354, 298, 365]},
	{"text": "4.17", "bbox": [376, 354, 418, 365]},
	{"text": "0.52", "bbox": [490, 354, 532, 365]},
	{"text": "12.5", "bbox": [595, 354, 637, 365]},
	{"text": "MEF 25", "bbox": [63, 368, 127, 379]},
	{"text": "[L/s]", "bbox": [250, 368, 298, 379]},
	{"text": "1.51", "bbox": [376, 368, 418, 379]},
	{"text": "0.22", "bbox": [490, 368, 532, 379]},
	{"text": "14.3", "bbox": [595, 368, 637, 379]},
	{"text": "MMEF 75/25", "bbox": [63, 382, 172, 393]},
	{"text": "[L/s]", "bbox": [250, 382, 298, 393]},
	{"text": "3.49", "bbox": [376, 382, 418, 393]},
	{"text": "0.44", "bbox": [490, 382, 532, 393]},
	{"text": "12.6", "bbox": [595, 382, 637, 393]},
	{"text": "MVV", "bbox": [63, 397, 98, 407]},
	{"text": "[L/min]", "bbox": [228, 397, 300, 408]},
	{"text": "113.25", "bbox": [356, 397, 418, 407]},
	{"text": "52.56", "bbox": [482, 397, 532, 407]},
	{"text": "46.4", "bbox": [595, 397, 637, 407]},
	{"text": "TLC-SB", "bbox": [67, 425, 132, 436]},
	{"text": "[L]", "bbox": [274, 425, 300, 436]},
	{"text": "6.10", "bbox": [378, 425, 419, 436]},
	{"text": "5.24", "bbox": [492, 425, 534, 436]},
	{"text": "85.9", "bbox": [597, 425, 638, 436]},
	{"text": "RV-SB", "bbox": [67, 440, 122, 450]},
	{"text": "[L]", "bbox": [274, 440, 300, 451]},
	{"text": "2.16", "bbox": [378, 440, 419, 450]},
	{"text": "2.69", "bbox": [492, 440, 534, 450]},
	{"text": "124.4", "bbox": [587, 440, 638, 450]},
	{"text": "RV%TLC-SB", "bbox": [67, 454, 165, 465]},
	{"text": "[%]", "bbox": [274, 454, 300, 465]},
	{"text": "35.80", "bbox": [368, 454, 419, 465]},
	{"text": "51.32", "bbox": [484, 454, 534, 465]},
	{"text": "143.4", "bbox": [587, 454, 638, 465]},
	{"text": "FRC-SB", "bbox": [67, 468, 132, 479]},
	{"text": "[L]", "bbox": [274, 468, 300, 479]},
	{"text": "3.28", "bbox": [378, 468, 419, 479]},
	{"text": "3.71", "bbox": [492, 468, 534, 479]},
	{"text": "113.3", "bbox": [587, 468, 638, 479]},
	{"text": "FRC%TLC-SB", "bbox": [67, 482, 174, 493]},
	{"text": "[%]", "bbox": [274, 482, 300, 493]},
	{"text": "55.56", "bbox": [368, 482, 419, 493]},
	{"text": "70.79", "bbox": [484, 482, 534, 493]},
	{"text": "127.4", "bbox": [587, 482, 638, 493]},
	{"text": "DLCO SB [mmol/min/kPa]", "bbox": [65, 496, 300, 507]},
	{"text": "8.61", "bbox": [378, 496, 419, 507]},
	{"text": "7.20", "bbox": [492, 496, 534, 507]},
	{"text": "83.7", "bbox": [597, 496, 638, 507]},
	{"text": "DLCO/Va mmol/min/kPa/L]", "bbox": [65, 510, 300, 521]},
	{"text": "1.41", "bbox": [378, 510, 419, 521]},
	{"text": "1.42", "bbox": [492, 510, 534, 521]},
	{"text": "100.4", "bbox": [587, 510, 638, 521]},
	{"text": "Hb", "bbox": [63, 525, 85, 535]},
	{"text": "[g/100ml]", "bbox": [208, 525, 300, 536]},
	{"text": "14.60", "bbox": [484, 522, 534, 532]},
	{"text": "VA", "bbox": [63, 540, 85, 550]},
	{"text": "[L]", "bbox": [274, 538, 300, 550]},
	{"text": "5.95", "bbox": [378, 538, 419, 550]},
	{"text": "5.09", "bbox": [492, 538, 534, 550]},
	{"text": "85.5", "bbox": [600, 535, 641, 546]},
	{"text": "DLCOc SB [mmol/min/kPa]", "bbox": [63, 553, 300, 564]},
	{"text": "8.61", "bbox": [378, 553, 419, 564]},
	{"text": "7.20", "bbox": [492, 553, 534, 564]},
	{"text": "83.7", "bbox": [600, 550, 641, 561]},
	{"text": "DLCOc/Va mmol/min/kPa/L]", "bbox": [63, 567, 300, 578]},
	{"text": "1.41", "bbox": [378, 567, 419, 578]},
	{"text": "1.42", "bbox": [492, 567, 534, 578]},
	{"text": "100.4", "bbox": [590, 564, 641, 575]},
	{"text": "VIN", "bbox": [62, 597, 95, 608]},
	{"text": "[L]", "bbox": [272, 595, 300, 607]},
	{"text": "3.85", "bbox": [378, 595, 419, 607]},
	{"text": "2.55", "bbox": [494, 593, 536, 604]},
	{"text": "66.3", "bbox": [602, 591, 643, 602]},
	{"text": "Insp. time", "bbox": [62, 612, 170, 623]},
	{"text": "[s]", "bbox": [272, 610, 300, 622]},
	{"text": "1.52", "bbox": [494, 607, 536, 618]},
	{"text": "Exp. time", "bbox": [62, 626, 160, 638]},
	{"text": "[s]", "bbox": [272, 625, 300, 637]},
	{"text": "2.15", "bbox": [494, 621, 536, 632]},
	{"text": "Sample vol", "bbox": [62, 641, 168, 653]},
	{"text": "[L]", "bbox": [272, 640, 300, 651]},
	{"text": "System dead space [ml]", "bbox": [60, 656, 298, 668]},
	{"text": "172.00", "bbox": [475, 651, 538, 662]},
	{"text": "Anatom. dead space[ml]", "bbox": [57, 671, 298, 683]},
	{"text": "154.00", "bbox": [475, 666, 538, 677]},
	{"text": "TA", "bbox": [57, 688, 80, 699]},
	{"text": "[s]", "bbox": [270, 686, 298, 698]},
	{"text": "11.54", "bbox": [487, 681, 538, 692]},
	{"text": "测试结果：", "bbox": [47, 704, 172, 722]},
	{"text": "FRCPleth", "bbox": [639, 259, 683, 267]},
	{"text": "RW", "bbox": [641, 276, 656, 284]},
	{"text": "PredAdt.0", "bbox": [643, 312, 692, 321]},
	{"text": "0.2", "bbox": [717, 312, 734, 321]},
	{"text": "0.4", "bbox": [759, 312, 776, 321]},
	{"text": "0.6", "bbox": [801, 312, 817, 321]},
	{"text": "0.8", "bbox": [843, 312, 859, 321]},
	{"text": "1.0", "bbox": [885, 312, 901, 321]},
	{"text": "Time [min]", "bbox": [760, 296, 814, 304]},
	{"text": "Flow [L/s]", "bbox": [670, 331, 720, 341]},
	{"text": "F/V ex", "bbox": [804, 331, 837, 340]},
	{"text": "10", "bbox": [652, 343, 665, 351]},
	{"text": "5", "bbox": [657, 364, 665, 372]},
	{"text": "0", "bbox": [657, 385, 665, 393]},
	{"text": "2", "bbox": [722, 393, 730, 401]},
	{"text": "4", "bbox": [780, 393, 787, 401]},
	{"text": "6", "bbox": [835, 393, 843, 401]},
	{"text": "1", "bbox": [890, 384, 900, 393]},
	{"text": "5", "bbox": [657, 405, 665, 413]},
	{"text": "10", "bbox": [652, 425, 665, 434]},
	{"text": "F/V in", "bbox": [804, 435, 834, 444]},
	{"text": "Vol [L]", "bbox": [670, 460, 705, 470]},
	{"text": "100", "bbox": [647, 480, 665, 489]},
	{"text": "10", "bbox": [888, 478, 901, 487]},
	{"text": "50", "bbox": [655, 522, 668, 530]},
	{"text": "100", "bbox": [661, 564, 670, 572]},
	{"text": "0", "bbox": [672, 575, 680, 583]},
	{"text": "2", "bbox": [710, 575, 718, 583]},
	{"text": "4", "bbox": [750, 575, 757, 583]},
	{"text": "6", "bbox": [790, 575, 797, 583]},
	{"text": "8", "bbox": [828, 575, 835, 583]},
	{"text": "10", "bbox": [864, 573, 876, 581]},
	{"text": "0", "bbox": [894, 564, 901, 572]},
	{"text": "Volume [L]", "bbox": [680, 593, 737, 604]},
	{"text": "4", "bbox": [667, 603, 675, 611]},
	{"text": "2", "bbox": [667, 623, 675, 631]},
	{"text": "0", "bbox": [667, 646, 675, 654]},
	{"text": "1", "bbox": [911, 646, 921, 655]},
	{"text": "2", "bbox": [670, 668, 678, 677]},
	{"text": "4", "bbox": [670, 691, 678, 699]},
	{"text": "Time [s]", "bbox": [773, 691, 816, 701]},
	{"text": "0", "bbox": [683, 712, 691, 720]},
	{"text": "10", "bbox": [728, 712, 742, 720]},
	{"text": "20", "bbox": [777, 712, 790, 720]},
	{"text": "30", "bbox": [825, 710, 839, 718]},
	{"text": "40", "bbox": [873, 710, 887, 718]}
]
2026-08-10 13:10:43,436 INFO     29 [qwen-vl-text] coord API: raw_items=197, valid_items=197, elapsed=48.7s
2026-08-10 13:10:43,436 INFO     29 [qwen-vl-text] coord item[0]: text=JAEGE R PCMED, bbox=[708, 43, 896, 57]
2026-08-10 13:10:43,436 INFO     29 [qwen-vl-text] coord item[1]: text=渑池县人民医院, bbox=[380, 57, 592, 78]
2026-08-10 13:10:43,436 INFO     29 [qwen-vl-text] coord item[2]: text=肺功能检查报告, bbox=[414, 80, 562, 97]
2026-08-10 13:10:43,436 INFO     29 [qwen-vl-text] coord item[3]: text=综合测试, bbox=[455, 101, 541, 116]
2026-08-10 13:10:43,436 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[81, 119, 127, 131]
2026-08-10 13:10:43,436 INFO     29 [qwen-vl-text] coord item[5]: text=性别：男, bbox=[81, 131, 266, 143]
2026-08-10 13:10:43,436 INFO     29 [qwen-vl-text] coord item[6]: text=年龄：56 Years, bbox=[81, 143, 324, 155]
2026-08-10 13:10:43,436 INFO     29 [qwen-vl-text] coord item[7]: text=身高：165 cm, bbox=[81, 155, 307, 167]
2026-08-10 13:10:43,436 INFO     29 [qwen-vl-text] coord item[8]: text=体重：70 kg, bbox=[81, 167, 297, 179]
2026-08-10 13:10:43,436 INFO     29 [qwen-vl-text] coord item[9]: text=备注：, bbox=[81, 179, 127, 190]
2026-08-10 13:10:43,436 INFO     29 [qwen-vl-text] coord item[10]: text=联系电话：, bbox=[424, 119, 507, 131]
2026-08-10 13:10:43,436 INFO     29 [qwen-vl-text] coord item[11]: text=住院号：0, bbox=[424, 131, 598, 143]
2026-08-10 13:10:43,436 INFO     29 [qwen-vl-text] coord item[12]: text=测试号：, bbox=[424, 143, 490, 155]
2026-08-10 13:10:43,436 INFO     29 [qwen-vl-text] coord item[13]: text=吸烟史：, bbox=[424, 155, 490, 167]
2026-08-10 13:10:43,436 INFO     29 [qwen-vl-text] coord item[14]: text=既往史：, bbox=[424, 167, 490, 179]
2026-08-10 13:10:43,436 INFO     29 [qwen-vl-text] coord item[15]: text=职业：, bbox=[424, 179, 471, 190]
2026-08-10 13:10:43,436 INFO     29 [qwen-vl-text] coord item[16]: text=测试日期, bbox=[75, 222, 159, 234]
2026-08-10 13:10:43,436 INFO     29 [qwen-vl-text] coord item[17]: text=测试时间, bbox=[75, 234, 159, 246]
2026-08-10 13:10:43,436 INFO     29 [qwen-vl-text] coord item[18]: text=预计值, bbox=[356, 210, 419, 222]
2026-08-10 13:10:43,436 INFO     29 [qwen-vl-text] coord item[19]: text=实测值, bbox=[468, 210, 529, 222]
2026-08-10 13:10:43,437 INFO     29 [qwen-vl-text] coord item[20]: text=实/预, bbox=[580, 210, 630, 222]
2026-08-10 13:10:43,437 INFO     29 [qwen-vl-text] coord item[21]: text=TLC, bbox=[635, 214, 656, 224]
2026-08-10 13:10:43,437 INFO     29 [qwen-vl-text] coord item[22]: text=6, bbox=[661, 210, 670, 218]
2026-08-10 13:10:43,437 INFO     29 [qwen-vl-text] coord item[23]: text=Vol [L], bbox=[675, 212, 708, 222]
2026-08-10 13:10:43,437 INFO     29 [qwen-vl-text] coord item[24]: text=25/4/25, bbox=[459, 224, 530, 234]
2026-08-10 13:10:43,437 INFO     29 [qwen-vl-text] coord item[25]: text=9:19:05上午, bbox=[428, 236, 532, 246]
2026-08-10 13:10:43,437 INFO     29 [qwen-vl-text] coord item[26]: text=VC MAX, bbox=[67, 259, 134, 269]
2026-08-10 13:10:43,437 INFO     29 [qwen-vl-text] coord item[27]: text=[L], bbox=[272, 259, 300, 270]
2026-08-10 13:10:43,437 INFO     29 [qwen-vl-text] coord item[28]: text=3.85, bbox=[376, 259, 418, 269]
2026-08-10 13:10:43,437 INFO     29 [qwen-vl-text] coord item[29]: text=2.72, bbox=[490, 259, 532, 269]
2026-08-10 13:10:43,437 INFO     29 [qwen-vl-text] coord item[30]: text=70.6, bbox=[593, 259, 635, 269]
2026-08-10 13:10:43,437 INFO     29 [qwen-vl-text] coord item[31]: text=FVC, bbox=[65, 271, 100, 281]
2026-08-10 13:10:43,437 INFO     29 [qwen-vl-text] coord item[32]: text=[L], bbox=[272, 271, 300, 282]
2026-08-10 13:10:43,437 INFO     29 [qwen-vl-text] coord item[33]: text=3.71, bbox=[376, 271, 418, 281]
2026-08-10 13:10:43,437 INFO     29 [qwen-vl-text] coord item[34]: text=2.68, bbox=[490, 271, 532, 281]
2026-08-10 13:10:43,437 INFO     29 [qwen-vl-text] coord item[35]: text=72.2, bbox=[593, 271, 635, 281]
2026-08-10 13:10:43,437 INFO     29 [qwen-vl-text] coord item[36]: text=MV, bbox=[63, 284, 88, 294]
2026-08-10 13:10:43,437 INFO     29 [qwen-vl-text] coord item[37]: text=[L/min], bbox=[228, 284, 298, 295]
2026-08-10 13:10:43,437 INFO     29 [qwen-vl-text] coord item[38]: text=10.00, bbox=[366, 284, 418, 294]
2026-08-10 13:10:43,437 INFO     29 [qwen-vl-text] coord item[39]: text=18.75, bbox=[482, 284, 532, 294]
2026-08-10 13:10:43,437 INFO     29 [qwen-vl-text] coord item[40]: text=187.5, bbox=[585, 284, 635, 294]
2026-08-10 13:10:43,437 INFO     29 [qwen-vl-text] coord item[41]: text=FEV 1, bbox=[63, 297, 117, 307]
2026-08-10 13:10:43,437 INFO     29 [qwen-vl-text] coord item[42]: text=[L], bbox=[272, 297, 300, 308]
2026-08-10 13:10:43,437 INFO     29 [qwen-vl-text] coord item[43]: text=2.98, bbox=[376, 297, 418, 307]
2026-08-10 13:10:43,438 INFO     29 [qwen-vl-text] coord item[44]: text=1.10, bbox=[490, 297, 532, 307]
2026-08-10 13:10:43,438 INFO     29 [qwen-vl-text] coord item[45]: text=36.9, bbox=[595, 297, 637, 307]
2026-08-10 13:10:43,438 INFO     29 [qwen-vl-text] coord item[46]: text=FEV 1 % FVC, bbox=[63, 310, 182, 321]
2026-08-10 13:10:43,438 INFO     29 [qwen-vl-text] coord item[47]: text=[%], bbox=[272, 310, 300, 321]
2026-08-10 13:10:43,438 INFO     29 [qwen-vl-text] coord item[48]: text=83.77, bbox=[366, 310, 418, 321]
2026-08-10 13:10:43,438 INFO     29 [qwen-vl-text] coord item[49]: text=41.10, bbox=[482, 310, 532, 321]
2026-08-10 13:10:43,438 INFO     29 [qwen-vl-text] coord item[50]: text=49.1, bbox=[595, 310, 637, 321]
2026-08-10 13:10:43,438 INFO     29 [qwen-vl-text] coord item[51]: text=PEF, bbox=[63, 325, 95, 335]
2026-08-10 13:10:43,438 INFO     29 [qwen-vl-text] coord item[52]: text=[L/s], bbox=[250, 325, 298, 336]
2026-08-10 13:10:43,438 INFO     29 [qwen-vl-text] coord item[53]: text=7.87, bbox=[376, 325, 418, 335]
2026-08-10 13:10:43,438 INFO     29 [qwen-vl-text] coord item[54]: text=2.33, bbox=[490, 325, 532, 335]
2026-08-10 13:10:43,438 INFO     29 [qwen-vl-text] coord item[55]: text=29.6, bbox=[595, 325, 637, 335]
2026-08-10 13:10:43,438 INFO     29 [qwen-vl-text] coord item[56]: text=MEF 75, bbox=[63, 340, 127, 350]
2026-08-10 13:10:43,438 INFO     29 [qwen-vl-text] coord item[57]: text=[L/s], bbox=[250, 340, 298, 351]
2026-08-10 13:10:43,438 INFO     29 [qwen-vl-text] coord item[58]: text=6.92, bbox=[376, 340, 418, 350]
2026-08-10 13:10:43,438 INFO     29 [qwen-vl-text] coord item[59]: text=0.96, bbox=[490, 340, 532, 350]
2026-08-10 13:10:43,438 INFO     29 [qwen-vl-text] coord item[60]: text=13.9, bbox=[595, 340, 637, 350]
2026-08-10 13:10:43,438 INFO     29 [qwen-vl-text] coord item[61]: text=MEF 50, bbox=[63, 354, 127, 365]
2026-08-10 13:10:43,438 INFO     29 [qwen-vl-text] coord item[62]: text=[L/s], bbox=[250, 354, 298, 365]
2026-08-10 13:10:43,438 INFO     29 [qwen-vl-text] coord item[63]: text=4.17, bbox=[376, 354, 418, 365]
2026-08-10 13:10:43,438 INFO     29 [qwen-vl-text] coord item[64]: text=0.52, bbox=[490, 354, 532, 365]
2026-08-10 13:10:43,438 INFO     29 [qwen-vl-text] coord item[65]: text=12.5, bbox=[595, 354, 637, 365]
2026-08-10 13:10:43,438 INFO     29 [qwen-vl-text] coord item[66]: text=MEF 25, bbox=[63, 368, 127, 379]
2026-08-10 13:10:43,439 INFO     29 [qwen-vl-text] coord item[67]: text=[L/s], bbox=[250, 368, 298, 379]
2026-08-10 13:10:43,439 INFO     29 [qwen-vl-text] coord item[68]: text=1.51, bbox=[376, 368, 418, 379]
2026-08-10 13:10:43,439 INFO     29 [qwen-vl-text] coord item[69]: text=0.22, bbox=[490, 368, 532, 379]
2026-08-10 13:10:43,439 INFO     29 [qwen-vl-text] coord item[70]: text=14.3, bbox=[595, 368, 637, 379]
2026-08-10 13:10:43,439 INFO     29 [qwen-vl-text] coord item[71]: text=MMEF 75/25, bbox=[63, 382, 172, 393]
2026-08-10 13:10:43,439 INFO     29 [qwen-vl-text] coord item[72]: text=[L/s], bbox=[250, 382, 298, 393]
2026-08-10 13:10:43,439 INFO     29 [qwen-vl-text] coord item[73]: text=3.49, bbox=[376, 382, 418, 393]
2026-08-10 13:10:43,439 INFO     29 [qwen-vl-text] coord item[74]: text=0.44, bbox=[490, 382, 532, 393]
2026-08-10 13:10:43,439 INFO     29 [qwen-vl-text] coord item[75]: text=12.6, bbox=[595, 382, 637, 393]
2026-08-10 13:10:43,439 INFO     29 [qwen-vl-text] coord item[76]: text=MVV, bbox=[63, 397, 98, 407]
2026-08-10 13:10:43,439 INFO     29 [qwen-vl-text] coord item[77]: text=[L/min], bbox=[228, 397, 300, 408]
2026-08-10 13:10:43,439 INFO     29 [qwen-vl-text] coord item[78]: text=113.25, bbox=[356, 397, 418, 407]
2026-08-10 13:10:43,439 INFO     29 [qwen-vl-text] coord item[79]: text=52.56, bbox=[482, 397, 532, 407]
2026-08-10 13:10:43,439 INFO     29 [qwen-vl-text] coord item[80]: text=46.4, bbox=[595, 397, 637, 407]
2026-08-10 13:10:43,439 INFO     29 [qwen-vl-text] coord item[81]: text=TLC-SB, bbox=[67, 425, 132, 436]
2026-08-10 13:10:43,439 INFO     29 [qwen-vl-text] coord item[82]: text=[L], bbox=[274, 425, 300, 436]
2026-08-10 13:10:43,439 INFO     29 [qwen-vl-text] coord item[83]: text=6.10, bbox=[378, 425, 419, 436]
2026-08-10 13:10:43,439 INFO     29 [qwen-vl-text] coord item[84]: text=5.24, bbox=[492, 425, 534, 436]
2026-08-10 13:10:43,440 INFO     29 [qwen-vl-text] coord item[85]: text=85.9, bbox=[597, 425, 638, 436]
2026-08-10 13:10:43,440 INFO     29 [qwen-vl-text] coord item[86]: text=RV-SB, bbox=[67, 440, 122, 450]
2026-08-10 13:10:43,440 INFO     29 [qwen-vl-text] coord item[87]: text=[L], bbox=[274, 440, 300, 451]
2026-08-10 13:10:43,440 INFO     29 [qwen-vl-text] coord item[88]: text=2.16, bbox=[378, 440, 419, 450]
2026-08-10 13:10:43,440 INFO     29 [qwen-vl-text] coord item[89]: text=2.69, bbox=[492, 440, 534, 450]
2026-08-10 13:10:43,440 INFO     29 [qwen-vl-text] coord item[90]: text=124.4, bbox=[587, 440, 638, 450]
2026-08-10 13:10:43,440 INFO     29 [qwen-vl-text] coord item[91]: text=RV%TLC-SB, bbox=[67, 454, 165, 465]
2026-08-10 13:10:43,440 INFO     29 [qwen-vl-text] coord item[92]: text=[%], bbox=[274, 454, 300, 465]
2026-08-10 13:10:43,440 INFO     29 [qwen-vl-text] coord item[93]: text=35.80, bbox=[368, 454, 419, 465]
2026-08-10 13:10:43,440 INFO     29 [qwen-vl-text] coord item[94]: text=51.32, bbox=[484, 454, 534, 465]
2026-08-10 13:10:43,440 INFO     29 [qwen-vl-text] coord item[95]: text=143.4, bbox=[587, 454, 638, 465]
2026-08-10 13:10:43,440 INFO     29 [qwen-vl-text] coord item[96]: text=FRC-SB, bbox=[67, 468, 132, 479]
2026-08-10 13:10:43,440 INFO     29 [qwen-vl-text] coord item[97]: text=[L], bbox=[274, 468, 300, 479]
2026-08-10 13:10:43,440 INFO     29 [qwen-vl-text] coord item[98]: text=3.28, bbox=[378, 468, 419, 479]
2026-08-10 13:10:43,440 INFO     29 [qwen-vl-text] coord item[99]: text=3.71, bbox=[492, 468, 534, 479]
2026-08-10 13:10:43,441 INFO     29 [qwen-vl-text] coord item[100]: text=113.3, bbox=[587, 468, 638, 479]
2026-08-10 13:10:43,441 INFO     29 [qwen-vl-text] coord item[101]: text=FRC%TLC-SB, bbox=[67, 482, 174, 493]
2026-08-10 13:10:43,441 INFO     29 [qwen-vl-text] coord item[102]: text=[%], bbox=[274, 482, 300, 493]
2026-08-10 13:10:43,441 INFO     29 [qwen-vl-text] coord item[103]: text=55.56, bbox=[368, 482, 419, 493]
2026-08-10 13:10:43,441 INFO     29 [qwen-vl-text] coord item[104]: text=70.79, bbox=[484, 482, 534, 493]
2026-08-10 13:10:43,441 INFO     29 [qwen-vl-text] coord item[105]: text=127.4, bbox=[587, 482, 638, 493]
2026-08-10 13:10:43,441 INFO     29 [qwen-vl-text] coord item[106]: text=DLCO SB [mmol/min/kPa], bbox=[65, 496, 300, 507]
2026-08-10 13:10:43,441 INFO     29 [qwen-vl-text] coord item[107]: text=8.61, bbox=[378, 496, 419, 507]
2026-08-10 13:10:43,441 INFO     29 [qwen-vl-text] coord item[108]: text=7.20, bbox=[492, 496, 534, 507]
2026-08-10 13:10:43,441 INFO     29 [qwen-vl-text] coord item[109]: text=83.7, bbox=[597, 496, 638, 507]
2026-08-10 13:10:43,441 INFO     29 [qwen-vl-text] coord item[110]: text=DLCO/Va mmol/min/kPa/L], bbox=[65, 510, 300, 521]
2026-08-10 13:10:43,441 INFO     29 [qwen-vl-text] coord item[111]: text=1.41, bbox=[378, 510, 419, 521]
2026-08-10 13:10:43,441 INFO     29 [qwen-vl-text] coord item[112]: text=1.42, bbox=[492, 510, 534, 521]
2026-08-10 13:10:43,441 INFO     29 [qwen-vl-text] coord item[113]: text=100.4, bbox=[587, 510, 638, 521]
2026-08-10 13:10:43,442 INFO     29 [qwen-vl-text] coord item[114]: text=Hb, bbox=[63, 525, 85, 535]
2026-08-10 13:10:43,442 INFO     29 [qwen-vl-text] coord item[115]: text=[g/100ml], bbox=[208, 525, 300, 536]
2026-08-10 13:10:43,442 INFO     29 [qwen-vl-text] coord item[116]: text=14.60, bbox=[484, 522, 534, 532]
2026-08-10 13:10:43,442 INFO     29 [qwen-vl-text] coord item[117]: text=VA, bbox=[63, 540, 85, 550]
2026-08-10 13:10:43,442 INFO     29 [qwen-vl-text] coord item[118]: text=[L], bbox=[274, 538, 300, 550]
2026-08-10 13:10:43,442 INFO     29 [qwen-vl-text] coord item[119]: text=5.95, bbox=[378, 538, 419, 550]
2026-08-10 13:10:43,442 INFO     29 [qwen-vl-text] coord item[120]: text=5.09, bbox=[492, 538, 534, 550]
2026-08-10 13:10:43,442 INFO     29 [qwen-vl-text] coord item[121]: text=85.5, bbox=[600, 535, 641, 546]
2026-08-10 13:10:43,442 INFO     29 [qwen-vl-text] coord item[122]: text=DLCOc SB [mmol/min/kPa], bbox=[63, 553, 300, 564]
2026-08-10 13:10:43,442 INFO     29 [qwen-vl-text] coord item[123]: text=8.61, bbox=[378, 553, 419, 564]
2026-08-10 13:10:43,442 INFO     29 [qwen-vl-text] coord item[124]: text=7.20, bbox=[492, 553, 534, 564]
2026-08-10 13:10:43,442 INFO     29 [qwen-vl-text] coord item[125]: text=83.7, bbox=[600, 550, 641, 561]
2026-08-10 13:10:43,442 INFO     29 [qwen-vl-text] coord item[126]: text=DLCOc/Va mmol/min/kPa/L], bbox=[63, 567, 300, 578]
2026-08-10 13:10:43,442 INFO     29 [qwen-vl-text] coord item[127]: text=1.41, bbox=[378, 567, 419, 578]
2026-08-10 13:10:43,442 INFO     29 [qwen-vl-text] coord item[128]: text=1.42, bbox=[492, 567, 534, 578]
2026-08-10 13:10:43,443 INFO     29 [qwen-vl-text] coord item[129]: text=100.4, bbox=[590, 564, 641, 575]
2026-08-10 13:10:43,443 INFO     29 [qwen-vl-text] coord item[130]: text=VIN, bbox=[62, 597, 95, 608]
2026-08-10 13:10:43,443 INFO     29 [qwen-vl-text] coord item[131]: text=[L], bbox=[272, 595, 300, 607]
2026-08-10 13:10:43,443 INFO     29 [qwen-vl-text] coord item[132]: text=3.85, bbox=[378, 595, 419, 607]
2026-08-10 13:10:43,443 INFO     29 [qwen-vl-text] coord item[133]: text=2.55, bbox=[494, 593, 536, 604]
2026-08-10 13:10:43,443 INFO     29 [qwen-vl-text] coord item[134]: text=66.3, bbox=[602, 591, 643, 602]
2026-08-10 13:10:43,443 INFO     29 [qwen-vl-text] coord item[135]: text=Insp. time, bbox=[62, 612, 170, 623]
2026-08-10 13:10:43,443 INFO     29 [qwen-vl-text] coord item[136]: text=[s], bbox=[272, 610, 300, 622]
2026-08-10 13:10:43,443 INFO     29 [qwen-vl-text] coord item[137]: text=1.52, bbox=[494, 607, 536, 618]
2026-08-10 13:10:43,443 INFO     29 [qwen-vl-text] coord item[138]: text=Exp. time, bbox=[62, 626, 160, 638]
2026-08-10 13:10:43,443 INFO     29 [qwen-vl-text] coord item[139]: text=[s], bbox=[272, 625, 300, 637]
2026-08-10 13:10:43,443 INFO     29 [qwen-vl-text] coord item[140]: text=2.15, bbox=[494, 621, 536, 632]
2026-08-10 13:10:43,443 INFO     29 [qwen-vl-text] coord item[141]: text=Sample vol, bbox=[62, 641, 168, 653]
2026-08-10 13:10:43,443 INFO     29 [qwen-vl-text] coord item[142]: text=[L], bbox=[272, 640, 300, 651]
2026-08-10 13:10:43,444 INFO     29 [qwen-vl-text] coord item[143]: text=System dead space [ml], bbox=[60, 656, 298, 668]
2026-08-10 13:10:43,444 INFO     29 [qwen-vl-text] coord item[144]: text=172.00, bbox=[475, 651, 538, 662]
2026-08-10 13:10:43,444 INFO     29 [qwen-vl-text] coord item[145]: text=Anatom. dead space[ml], bbox=[57, 671, 298, 683]
2026-08-10 13:10:43,444 INFO     29 [qwen-vl-text] coord item[146]: text=154.00, bbox=[475, 666, 538, 677]
2026-08-10 13:10:43,444 INFO     29 [qwen-vl-text] coord item[147]: text=TA, bbox=[57, 688, 80, 699]
2026-08-10 13:10:43,444 INFO     29 [qwen-vl-text] coord item[148]: text=[s], bbox=[270, 686, 298, 698]
2026-08-10 13:10:43,444 INFO     29 [qwen-vl-text] coord item[149]: text=11.54, bbox=[487, 681, 538, 692]
2026-08-10 13:10:43,444 INFO     29 [qwen-vl-text] coord item[150]: text=测试结果：, bbox=[47, 704, 172, 722]
2026-08-10 13:10:43,444 INFO     29 [qwen-vl-text] coord item[151]: text=FRCPleth, bbox=[639, 259, 683, 267]
2026-08-10 13:10:43,444 INFO     29 [qwen-vl-text] coord item[152]: text=RW, bbox=[641, 276, 656, 284]
2026-08-10 13:10:43,445 INFO     29 [qwen-vl-text] coord item[153]: text=PredAdt.0, bbox=[643, 312, 692, 321]
2026-08-10 13:10:43,445 INFO     29 [qwen-vl-text] coord item[154]: text=0.2, bbox=[717, 312, 734, 321]
2026-08-10 13:10:43,445 INFO     29 [qwen-vl-text] coord item[155]: text=0.4, bbox=[759, 312, 776, 321]
2026-08-10 13:10:43,445 INFO     29 [qwen-vl-text] coord item[156]: text=0.6, bbox=[801, 312, 817, 321]
2026-08-10 13:10:43,445 INFO     29 [qwen-vl-text] coord item[157]: text=0.8, bbox=[843, 312, 859, 321]
2026-08-10 13:10:43,445 INFO     29 [qwen-vl-text] coord item[158]: text=1.0, bbox=[885, 312, 901, 321]
2026-08-10 13:10:43,445 INFO     29 [qwen-vl-text] coord item[159]: text=Time [min], bbox=[760, 296, 814, 304]
2026-08-10 13:10:43,445 INFO     29 [qwen-vl-text] coord item[160]: text=Flow [L/s], bbox=[670, 331, 720, 341]
2026-08-10 13:10:43,445 INFO     29 [qwen-vl-text] coord item[161]: text=F/V ex, bbox=[804, 331, 837, 340]
2026-08-10 13:10:43,445 INFO     29 [qwen-vl-text] coord item[162]: text=10, bbox=[652, 343, 665, 351]
2026-08-10 13:10:43,445 INFO     29 [qwen-vl-text] coord item[163]: text=5, bbox=[657, 364, 665, 372]
2026-08-10 13:10:43,446 INFO     29 [qwen-vl-text] coord item[164]: text=0, bbox=[657, 385, 665, 393]
2026-08-10 13:10:43,446 INFO     29 [qwen-vl-text] coord item[165]: text=2, bbox=[722, 393, 730, 401]
2026-08-10 13:10:43,446 INFO     29 [qwen-vl-text] coord item[166]: text=4, bbox=[780, 393, 787, 401]
2026-08-10 13:10:43,446 INFO     29 [qwen-vl-text] coord item[167]: text=6, bbox=[835, 393, 843, 401]
2026-08-10 13:10:43,446 INFO     29 [qwen-vl-text] coord item[168]: text=1, bbox=[890, 384, 900, 393]
2026-08-10 13:10:43,446 INFO     29 [qwen-vl-text] coord item[169]: text=5, bbox=[657, 405, 665, 413]
2026-08-10 13:10:43,446 INFO     29 [qwen-vl-text] coord item[170]: text=10, bbox=[652, 425, 665, 434]
2026-08-10 13:10:43,446 INFO     29 [qwen-vl-text] coord item[171]: text=F/V in, bbox=[804, 435, 834, 444]
2026-08-10 13:10:43,446 INFO     29 [qwen-vl-text] coord item[172]: text=Vol [L], bbox=[670, 460, 705, 470]
2026-08-10 13:10:43,446 INFO     29 [qwen-vl-text] coord item[173]: text=100, bbox=[647, 480, 665, 489]
2026-08-10 13:10:43,446 INFO     29 [qwen-vl-text] coord item[174]: text=10, bbox=[888, 478, 901, 487]
2026-08-10 13:10:43,446 INFO     29 [qwen-vl-text] coord item[175]: text=50, bbox=[655, 522, 668, 530]
2026-08-10 13:10:43,446 INFO     29 [qwen-vl-text] coord item[176]: text=100, bbox=[661, 564, 670, 572]
2026-08-10 13:10:43,446 INFO     29 [qwen-vl-text] coord item[177]: text=0, bbox=[672, 575, 680, 583]
2026-08-10 13:10:43,446 INFO     29 [qwen-vl-text] coord item[178]: text=2, bbox=[710, 575, 718, 583]
2026-08-10 13:10:43,446 INFO     29 [qwen-vl-text] coord item[179]: text=4, bbox=[750, 575, 757, 583]
2026-08-10 13:10:43,446 INFO     29 [qwen-vl-text] coord item[180]: text=6, bbox=[790, 575, 797, 583]
2026-08-10 13:10:43,446 INFO     29 [qwen-vl-text] coord item[181]: text=8, bbox=[828, 575, 835, 583]
2026-08-10 13:10:43,446 INFO     29 [qwen-vl-text] coord item[182]: text=10, bbox=[864, 573, 876, 581]
2026-08-10 13:10:43,447 INFO     29 [qwen-vl-text] coord item[183]: text=0, bbox=[894, 564, 901, 572]
2026-08-10 13:10:43,447 INFO     29 [qwen-vl-text] coord item[184]: text=Volume [L], bbox=[680, 593, 737, 604]
2026-08-10 13:10:43,447 INFO     29 [qwen-vl-text] coord item[185]: text=4, bbox=[667, 603, 675, 611]
2026-08-10 13:10:43,447 INFO     29 [qwen-vl-text] coord item[186]: text=2, bbox=[667, 623, 675, 631]
2026-08-10 13:10:43,447 INFO     29 [qwen-vl-text] coord item[187]: text=0, bbox=[667, 646, 675, 654]
2026-08-10 13:10:43,447 INFO     29 [qwen-vl-text] coord item[188]: text=1, bbox=[911, 646, 921, 655]
2026-08-10 13:10:43,447 INFO     29 [qwen-vl-text] coord item[189]: text=2, bbox=[670, 668, 678, 677]
2026-08-10 13:10:43,447 INFO     29 [qwen-vl-text] coord item[190]: text=4, bbox=[670, 691, 678, 699]
2026-08-10 13:10:43,447 INFO     29 [qwen-vl-text] coord item[191]: text=Time [s], bbox=[773, 691, 816, 701]
2026-08-10 13:10:43,447 INFO     29 [qwen-vl-text] coord item[192]: text=0, bbox=[683, 712, 691, 720]
2026-08-10 13:10:43,447 INFO     29 [qwen-vl-text] coord item[193]: text=10, bbox=[728, 712, 742, 720]
2026-08-10 13:10:43,447 INFO     29 [qwen-vl-text] coord item[194]: text=20, bbox=[777, 712, 790, 720]
2026-08-10 13:10:43,447 INFO     29 [qwen-vl-text] coord item[195]: text=30, bbox=[825, 710, 839, 718]
2026-08-10 13:10:43,447 INFO     29 [qwen-vl-text] coord item[196]: text=40, bbox=[873, 710, 887, 718]
2026-08-10 13:10:43,449 INFO     29 [qwen-vl-text] page=2 — 198/198 coords, api_time=48.7s
2026-08-10 13:10:43,452 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1660617, prompt_len=1809
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共146行）
["JAEGE R PCMED", "渑池县人民医院", "肺功能检查报告", "舒张试验", "姓名：", "科别：", "住院号：0", "测试号：2025042503", "性别：男", "年龄：56 Years", "身高：165 cm", "体重：70 kg", "标准体重：108 %", "体表面积：1.77 m", "吸烟史：", "Flow [L/s]", "F/V ex", "Vol%VCmax", "Vol [L]", "10", "20", "40", "60", "80", "100", "2", "VCmax", "1", "1", "0", "2", "3", "4", "5", "6", "7", "1", "2", "4", "5", "6", "10", "Time [s]", "F/V in", "8", "0", "1", "2", "3", "4", "5", "6", "7", "8", "预计值", "前次", "前/预", "后次", "后/预", "改善率", "测试日期", "25/4/25", "25/4/25", "测试时间", "9:19:05", "9:43:24", "VC MAX", "[L]", "3.85", "2.72", "70.6", "3.07", "79.9", "13.2", "FVC", "[L]", "3.71", "2.68", "72.2", "3.05", "82.4", "14.1", "FEV 1", "[L]", "2.98", "1.10", "36.9", "1.55", "52.1", "41.1", "FEV 1 % FVC", "[%]", "83.77", "41.10", "49.1", "50.82", "60.7", "23.6", "FEV 1 % VC MAX", "[%]", "77.13", "40.51", "52.5", "50.49", "65.5", "24.6", "PEF", "[L/s]", "7.87", "2.33", "29.6", "3.18", "40.4", "36.6", "MEF 75", "[L/s]", "6.92", "0.96", "13.9", "1.65", "23.9", "72.1", "MEF 50", "[L/s]", "4.17", "0.52", "12.5", "0.85", "20.3", "63.0", "MEF 25", "[L/s]", "1.51", "0.22", "14.3", "0.35", "23.2", "62.9", "MMEF 75/25", "[L/s]", "3.49", "0.44", "12.6", "0.75", "21.3", "69.5"]

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
2026-08-10 13:11:43,584 INFO     29 [qwen-vl-text] coord API raw response (len=11128):
[
	{"text": "JAEGE R PCMED", "bbox": [696, 38, 875, 54]},
	{"text": "渑池县人民医院", "bbox": [361, 50, 588, 69]},
	{"text": "肺功能检查报告", "bbox": [375, 74, 565, 92]},
	{"text": "舒张试验", "bbox": [420, 97, 513, 115]},
	{"text": "姓名：", "bbox": [67, 115, 117, 128]},
	{"text": "科别：", "bbox": [440, 118, 489, 131]},
	{"text": "住院号：", "bbox": [67, 128, 138, 141]},
	{"text": "0", "bbox": [251, 131, 260, 141]},
	{"text": "测试号：", "bbox": [440, 131, 508, 144]},
	{"text": "2025042503", "bbox": [615, 133, 711, 144]},
	{"text": "性别：", "bbox": [67, 141, 117, 154]},
	{"text": "男", "bbox": [251, 142, 271, 154]},
	{"text": "年龄：", "bbox": [440, 144, 489, 157]},
	{"text": "56 Years", "bbox": [615, 146, 692, 157]},
	{"text": "身高：", "bbox": [67, 154, 117, 167]},
	{"text": "165 cm", "bbox": [251, 156, 314, 167]},
	{"text": "体重：", "bbox": [440, 157, 489, 170]},
	{"text": "70 kg", "bbox": [615, 158, 663, 170]},
	{"text": "标准体重：", "bbox": [67, 167, 159, 180]},
	{"text": "108 %", "bbox": [251, 169, 314, 180]},
	{"text": "体表面积：", "bbox": [440, 170, 526, 183]},
	{"text": "1.77 m", "bbox": [615, 171, 674, 183]},
	{"text": "吸烟史：", "bbox": [67, 180, 141, 193]},
	{"text": "Flow [L/s]", "bbox": [104, 231, 161, 242]},
	{"text": "F/V ex", "bbox": [324, 233, 361, 242]},
	{"text": "Vol%VCmax", "bbox": [487, 228, 550, 238]},
	{"text": "0", "bbox": [504, 239, 513, 248]},
	{"text": "0", "bbox": [521, 239, 529, 248]},
	{"text": "Vol [L]", "bbox": [535, 242, 570, 254]},
	{"text": "20", "bbox": [498, 250, 513, 259]},
	{"text": "40", "bbox": [498, 261, 513, 270]},
	{"text": "60", "bbox": [498, 273, 513, 282]},
	{"text": "5", "bbox": [90, 280, 98, 289]},
	{"text": "80", "bbox": [498, 284, 513, 293]},
	{"text": "2", "bbox": [523, 275, 531, 284]},
	{"text": "100", "bbox": [494, 295, 514, 304]},
	{"text": "VCmax", "bbox": [551, 293, 588, 302]},
	{"text": "1", "bbox": [457, 308, 467, 317], "bbox": [457, 308, 467, 317]},
	{"text": "1", "bbox": [837, 305, 846, 314], "bbox": [837, 305, 846, 314]},
	{"text": "0", "bbox": [90, 313, 98, 322], "bbox": [90, 313, 98, 322]},
	{"text": "1", "bbox": [147, 323, 155, 332], "bbox": [147, 323, 155, 332]},
	{"text": "2", "bbox": [192, 323, 200, 332], "bbox": [192, 323, 200, 332]},
	{"text": "3", "bbox": [238, 323, 246, 332], "bbox": [238, 323, 246, 332]},
	{"text": "4", "bbox": [284, 323, 292, 332], "bbox": [284, 323, 292, 332]},
	{"text": "5", "bbox": [329, 323, 337, 332], "bbox": [329, 323, 337, 332]},
	{"text": "6", "bbox": [373, 323, 381, 332], "bbox": [373, 323, 381, 332]},
	{"text": "7", "bbox": [416, 323, 424, 332], "bbox": [416, 323, 424, 332]},
	{"text": "2", "bbox": [460, 320, 468, 329], "bbox": [460, 320, 468, 329]},
	{"text": "4", "bbox": [524, 314, 532, 323], "bbox": [524, 314, 532, 323]},
	{"text": "5", "bbox": [93, 345, 102, 354], "bbox": [93, 345, 102, 354]},
	{"text": "6", "bbox": [524, 353, 532, 362], "bbox": [524, 353, 532, 362]},
	{"text": "10", "bbox": [90, 377, 107, 386], "bbox": [90, 377, 107, 386]},
	{"text": "Time [s]", "bbox": [666, 379, 709, 389]},
	{"text": "F/V in", "bbox": [336, 396, 368, 405], "bbox": [336, 396, 368, 405]},
	{"text": "8", "bbox": [525, 390, 534, 399], "bbox": [525, 390, 534, 399]},
	{"text": "0", "bbox": [536, 400, 544, 408], "bbox": [536, 400, 544, 408]},
	{"text": "1", "bbox": [572, 400, 579, 408], "bbox": [572, 400, 579, 408]},
	{"text": "2", "bbox": [609, 400, 617, 408], "bbox": [609, 400, 617, 408]},
	{"text": "3", "bbox": [646, 400, 654, 408], "bbox": [646, 400, 654, 408]},
	{"text": "4", "bbox": [684, 400, 692, 408], "bbox": [684, 400, 692, 408]},
	{"text": "5", "bbox": [721, 400, 729, 408], "bbox": [721, 400, 729, 408]},
	{"text": "6", "bbox": [760, 400, 767, 408], "bbox": [760, 400, 767, 408]},
	{"text": "7", "bbox": [798, 397, 805, 405], "bbox": [798, 397, 805, 405]},
	{"text": "8", "bbox": [836, 397, 843, 405], "bbox": [836, 397, 843, 405]},
	{"text": "预计值", "bbox": [379, 417, 437, 430], "bbox": [379, 417, 437, 430]},
	{"text": "前次", "bbox": [484, 417, 521, 429], "bbox": [484, 417, 521, 429]},
	{"text": "前/预", "bbox": [558, 416, 605, 428], "bbox": [558, 416, 605, 428]},
	{"text": "后次", "bbox": [650, 415, 689, 427], "bbox": [650, 415, 689, 427]},
	{"text": "后/预", "bbox": [725, 413, 773, 425], "bbox": [725, 413, 773, 425]},
	{"text": "改善率", "bbox": [800, 411, 857, 423], "bbox": [800, 411, 857, 423]},
	{"text": "测试日期", "bbox": [90, 432, 171, 445], "bbox": [90, 432, 171, 445]},
	{"text": "25/4/25", "bbox": [456, 430, 521, 441], "bbox": [456, 430, 521, 441]},
	{"text": "25/4/25", "bbox": [622, 428, 689, 439], "bbox": [622, 428, 689, 439]},
	{"text": "测试时间", "bbox": [90, 445, 171, 458], "bbox": [90, 445, 171, 458]},
	{"text": "9:19:05", "bbox": [448, 443, 521, 454], "bbox": [448, 443, 521, 454]},
	{"text": "9:43:24", "bbox": [615, 441, 689, 452], "bbox": [615, 441, 689, 452]},
	{"text": "VC MAX", "bbox": [94, 473, 157, 482], "bbox": [94, 473, 157, 482]},
	{"text": "[L]", "bbox": [327, 471, 351, 481], "bbox": [327, 471, 351, 481]},
	{"text": "3.85", "bbox": [401, 470, 439, 480], "bbox": [401, 470, 439, 480]},
	{"text": "2.72", "bbox": [485, 469, 521, 479], "bbox": [485, 469, 521, 479]},
	{"text": "70.6", "bbox": [568, 467, 605, 477], "bbox": [568, 467, 605, 477]},
	{"text": "3.07", "bbox": [652, 466, 689, 476], "bbox": [652, 466, 689, 476]},
	{"text": "79.9", "bbox": [735, 465, 773, 475], "bbox": [735, 465, 773, 475]},
	{"text": "13.2", "bbox": [820, 463, 857, 473], "bbox": [820, 463, 857, 473]},
	{"text": "FVC", "bbox": [94, 486, 127, 495], "bbox": [94, 486, 127, 495]},
	{"text": "[L]", "bbox": [327, 484, 351, 494], "bbox": [327, 484, 351, 494]},
	{"text": "3.71", "bbox": [401, 482, 439, 492], "bbox": [401, 482, 439, 492]},
	{"text": "2.68", "bbox": [485, 481, 521, 491], "bbox": [485, 481, 521, 491]},
	{"text": "72.2", "bbox": [568, 480, 605, 490], "bbox": [568, 480, 605, 490]},
	{"text": "3.05", "bbox": [652, 479, 689, 489], "bbox": [652, 479, 689, 489]},
	{"text": "82.4", "bbox": [735, 478, 773, 488], "bbox": [735, 478, 773, 488]},
	{"text": "14.1", "bbox": [820, 476, 857, 486], "bbox": [820, 476, 857, 486]},
	{"text": "FEV 1", "bbox": [94, 499, 145, 508], "bbox": [94, 499, 145, 508]},
	{"text": "[L]", "bbox": [327, 497, 351, 507], "bbox": [327, 497, 351, 507]},
	{"text": "2.98", "bbox": [401, 495, 439, 505], "bbox": [401, 495, 439, 505]},
	{"text": "1.10", "bbox": [485, 494, 521, 504], "bbox": [485, 494, 521, 504]},
	{"text": "36.9", "bbox": [568, 492, 605, 502], "bbox": [568, 492, 605, 502]},
	{"text": "1.55", "bbox": [652, 491, 689, 501], "bbox": [652, 491, 689, 501]},
	{"text": "52.1", "bbox": [735, 490, 773, 500], "bbox": [735, 490, 773, 500]},
	{"text": "41.1", "bbox": [820, 488, 857, 498], "bbox": [820, 488, 857, 498]},
	{"text": "FEV 1 % FVC", "bbox": [94, 511, 207, 520], "bbox": [94, 511, 207, 520]},
	{"text": "[%]", "bbox": [327, 509, 351, 519], "bbox": [327, 509, 351, 519]},
	{"text": "83.77", "bbox": [392, 507, 439, 517], "bbox": [392, 507, 439, 517]},
	{"text": "41.10", "bbox": [477, 506, 521, 516], "bbox": [477, 506, 521, 516]},
	{"text": "49.1", "bbox": [568, 505, 605, 515], "bbox": [568, 505, 605, 515]},
	{"text": "50.82", "bbox": [645, 504, 689, 514], "bbox": [645, 504, 689, 514]},
	{"text": "60.7", "bbox": [735, 503, 773, 513], "bbox": [735, 503, 773, 513]},
	{"text": "23.6", "bbox": [820, 501, 857, 511], "bbox": [820, 501, 857, 511]},
	{"text": "FEV 1 % VC MAX", "bbox": [94, 524, 238, 533], "bbox": [94, 524, 238, 533]},
	{"text": "[%]", "bbox": [327, 522, 351, 532], "bbox": [327, 522, 351, 532]},
	{"text": "77.13", "bbox": [392, 520, 439, 530], "bbox": [392, 520, 439, 530]},
	{"text": "40.51", "bbox": [477, 519, 521, 529], "bbox": [477, 519, 521, 529]},
	{"text": "52.5", "bbox": [568, 517, 605, 527], "bbox": [568, 517, 605, 527]},
	{"text": "50.49", "bbox": [645, 516, 689, 526], "bbox": [645, 516, 689, 526]},
	{"text": "65.5", "bbox": [735, 515, 773, 525], "bbox": [735, 515, 773, 525]},
	{"text": "24.6", "bbox": [820, 513, 857, 523], "bbox": [820, 513, 857, 523]},
	{"text": "PEF", "bbox": [94, 538, 127, 547], "bbox": [94, 538, 127, 547]},
	{"text": "[L/s]", "bbox": [309, 535, 351, 545], "bbox": [309, 535, 351, 545]},
	{"text": "7.87", "bbox": [401, 533, 439, 543], "bbox": [401, 533, 439, 543]},
	{"text": "2.33", "bbox": [485, 532, 521, 542], "bbox": [485, 532, 521, 542]},
	{"text": "29.6", "bbox": [568, 530, 605, 540], "bbox": [568, 530, 605, 540]},
	{"text": "3.18", "bbox": [652, 529, 689, 539], "bbox": [652, 529, 689, 539]},
	{"text": "40.4", "bbox": [735, 528, 773, 538], "bbox": [735, 528, 773, 538]},
	{"text": "36.6", "bbox": [820, 526, 857, 536], "bbox": [820, 526, 857, 536]},
	{"text": "MEF 75", "bbox": [94, 551, 157, 560], "bbox": [94, 551, 157, 560]},
	{"text": "[L/s]", "bbox": [309, 548, 351, 558], "bbox": [309, 548, 351, 558]},
	{"text": "6.92", "bbox": [401, 546, 439, 556], "bbox": [401, 546, 439, 556]},
	{"text": "0.96", "bbox": [485, 545, 521, 555], "bbox": [485, 545, 521, 555]},
	{"text": "13.9", "bbox": [568, 543, 605, 553], "bbox": [568, 543, 605, 553]},
	{"text": "1.65", "bbox": [652, 542, 689, 552], "bbox": [652, 542, 689, 552]},
	{"text": "23.9", "bbox": [735, 541, 773, 551], "bbox": [735, 541, 773, 551]},
	{"text": "72.1", "bbox": [820, 539, 857, 549], "bbox": [820, 539, 857, 549]},
	{"text": "MEF 50", "bbox": [94, 564, 157, 573], "bbox": [94, 564, 157, 573]},
	{"text": "[L/s]", "bbox": [309, 561, 351, 571], "bbox": [309, 561, 351, 571]},
	{"text": "4.17", "bbox": [401, 558, 439, 568], "bbox": [401, 558, 439, 568]},
	{"text": "0.52", "bbox": [485, 557, 521, 567], "bbox": [485, 557, 521, 567]},
	{"text": "12.5", "bbox": [568, 556, 605, 566], "bbox": [568, 556, 605, 566]},
	{"text": "0.85", "bbox": [652, 555, 689, 565], "bbox": [652, 555, 689, 565]},
	{"text": "20.3", "bbox": [735, 554, 773, 564], "bbox": [735, 554, 773, 564]},
	{"text": "63.0", "bbox": [820, 552, 857, 562], "bbox": [820, 552, 857, 562]},
	{"text": "MEF 25", "bbox": [94, 577, 157, 586], "bbox": [94, 577, 157, 586]},
	{"text": "[L/s]", "bbox": [309, 574, 351, 584], "bbox": [309, 574, 351, 584]},
	{"text": "1.51", "bbox": [401, 571, 439, 581], "bbox": [401, 571, 439, 581]},
	{"text": "0.22", "bbox": [485, 570, 521, 580], "bbox": [485, 570, 521, 580]},
	{"text": "14.3", "bbox": [568, 568, 605, 578], "bbox": [568, 568, 605, 578]},
	{"text": "0.35", "bbox": [652, 567, 689, 577], "bbox": [652, 567, 689, 577]},
	{"text": "23.2", "bbox": [735, 566, 773, 576], "bbox": [735, 566, 773, 576]},
	{"text": "62.9", "bbox": [820, 564, 857, 574], "bbox": [820, 564, 857, 574]},
	{"text": "MMEF 75/25", "bbox": [94, 590, 197, 600], "bbox": [94, 590, 197, 600]},
	{"text": "[L/s]", "bbox": [309, 587, 351, 597], "bbox": [309, 587, 351, 597]},
	{"text": "3.49", "bbox": [401, 584, 439, 594], "bbox": [401, 584, 439, 594]},
	{"text": "0.44", "bbox": [485, 583, 521, 593], "bbox": [485, 583, 521, 593]},
	{"text": "12.6", "bbox": [568, 581, 605, 591], "bbox": [568, 581, 605, 591]},
	{"text": "0.75", "bbox": [652, 580, 689, 590], "bbox": [652, 580, 689, 590]},
	{"text": "21.3", "bbox": [735, 578, 773, 588], "bbox": [735, 578, 773, 588]},
	{"text": "69.5", "bbox": [820, 576, 857, 586], "bbox": [820, 576, 857, 586]}
]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord API: raw_items=156, valid_items=156, elapsed=60.1s
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[0]: text=JAEGE R PCMED, bbox=[696, 38, 875, 54]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[1]: text=渑池县人民医院, bbox=[361, 50, 588, 69]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[2]: text=肺功能检查报告, bbox=[375, 74, 565, 92]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[3]: text=舒张试验, bbox=[420, 97, 513, 115]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[67, 115, 117, 128]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[5]: text=科别：, bbox=[440, 118, 489, 131]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[6]: text=住院号：, bbox=[67, 128, 138, 141]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[7]: text=0, bbox=[251, 131, 260, 141]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[8]: text=测试号：, bbox=[440, 131, 508, 144]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[9]: text=2025042503, bbox=[615, 133, 711, 144]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[10]: text=性别：, bbox=[67, 141, 117, 154]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[11]: text=男, bbox=[251, 142, 271, 154]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[12]: text=年龄：, bbox=[440, 144, 489, 157]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[13]: text=56 Years, bbox=[615, 146, 692, 157]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[14]: text=身高：, bbox=[67, 154, 117, 167]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[15]: text=165 cm, bbox=[251, 156, 314, 167]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[16]: text=体重：, bbox=[440, 157, 489, 170]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[17]: text=70 kg, bbox=[615, 158, 663, 170]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[18]: text=标准体重：, bbox=[67, 167, 159, 180]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[19]: text=108 %, bbox=[251, 169, 314, 180]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[20]: text=体表面积：, bbox=[440, 170, 526, 183]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[21]: text=1.77 m, bbox=[615, 171, 674, 183]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[22]: text=吸烟史：, bbox=[67, 180, 141, 193]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[23]: text=Flow [L/s], bbox=[104, 231, 161, 242]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[24]: text=F/V ex, bbox=[324, 233, 361, 242]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[25]: text=Vol%VCmax, bbox=[487, 228, 550, 238]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[26]: text=0, bbox=[504, 239, 513, 248]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[27]: text=0, bbox=[521, 239, 529, 248]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[28]: text=Vol [L], bbox=[535, 242, 570, 254]
2026-08-10 13:11:43,585 INFO     29 [qwen-vl-text] coord item[29]: text=20, bbox=[498, 250, 513, 259]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[30]: text=40, bbox=[498, 261, 513, 270]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[31]: text=60, bbox=[498, 273, 513, 282]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[32]: text=5, bbox=[90, 280, 98, 289]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[33]: text=80, bbox=[498, 284, 513, 293]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[34]: text=2, bbox=[523, 275, 531, 284]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[35]: text=100, bbox=[494, 295, 514, 304]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[36]: text=VCmax, bbox=[551, 293, 588, 302]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[37]: text=1, bbox=[457, 308, 467, 317]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[38]: text=1, bbox=[837, 305, 846, 314]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[39]: text=0, bbox=[90, 313, 98, 322]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[40]: text=1, bbox=[147, 323, 155, 332]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[41]: text=2, bbox=[192, 323, 200, 332]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[42]: text=3, bbox=[238, 323, 246, 332]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[43]: text=4, bbox=[284, 323, 292, 332]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[44]: text=5, bbox=[329, 323, 337, 332]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[45]: text=6, bbox=[373, 323, 381, 332]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[46]: text=7, bbox=[416, 323, 424, 332]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[47]: text=2, bbox=[460, 320, 468, 329]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[48]: text=4, bbox=[524, 314, 532, 323]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[49]: text=5, bbox=[93, 345, 102, 354]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[50]: text=6, bbox=[524, 353, 532, 362]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[51]: text=10, bbox=[90, 377, 107, 386]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[52]: text=Time [s], bbox=[666, 379, 709, 389]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[53]: text=F/V in, bbox=[336, 396, 368, 405]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[54]: text=8, bbox=[525, 390, 534, 399]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[55]: text=0, bbox=[536, 400, 544, 408]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[56]: text=1, bbox=[572, 400, 579, 408]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[57]: text=2, bbox=[609, 400, 617, 408]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[58]: text=3, bbox=[646, 400, 654, 408]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[59]: text=4, bbox=[684, 400, 692, 408]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[60]: text=5, bbox=[721, 400, 729, 408]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[61]: text=6, bbox=[760, 400, 767, 408]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[62]: text=7, bbox=[798, 397, 805, 405]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[63]: text=8, bbox=[836, 397, 843, 405]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[64]: text=预计值, bbox=[379, 417, 437, 430]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[65]: text=前次, bbox=[484, 417, 521, 429]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[66]: text=前/预, bbox=[558, 416, 605, 428]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[67]: text=后次, bbox=[650, 415, 689, 427]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[68]: text=后/预, bbox=[725, 413, 773, 425]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[69]: text=改善率, bbox=[800, 411, 857, 423]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[70]: text=测试日期, bbox=[90, 432, 171, 445]
2026-08-10 13:11:43,586 INFO     29 [qwen-vl-text] coord item[71]: text=25/4/25, bbox=[456, 430, 521, 441]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[72]: text=25/4/25, bbox=[622, 428, 689, 439]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[73]: text=测试时间, bbox=[90, 445, 171, 458]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[74]: text=9:19:05, bbox=[448, 443, 521, 454]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[75]: text=9:43:24, bbox=[615, 441, 689, 452]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[76]: text=VC MAX, bbox=[94, 473, 157, 482]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[77]: text=[L], bbox=[327, 471, 351, 481]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[78]: text=3.85, bbox=[401, 470, 439, 480]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[79]: text=2.72, bbox=[485, 469, 521, 479]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[80]: text=70.6, bbox=[568, 467, 605, 477]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[81]: text=3.07, bbox=[652, 466, 689, 476]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[82]: text=79.9, bbox=[735, 465, 773, 475]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[83]: text=13.2, bbox=[820, 463, 857, 473]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[84]: text=FVC, bbox=[94, 486, 127, 495]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[85]: text=[L], bbox=[327, 484, 351, 494]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[86]: text=3.71, bbox=[401, 482, 439, 492]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[87]: text=2.68, bbox=[485, 481, 521, 491]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[88]: text=72.2, bbox=[568, 480, 605, 490]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[89]: text=3.05, bbox=[652, 479, 689, 489]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[90]: text=82.4, bbox=[735, 478, 773, 488]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[91]: text=14.1, bbox=[820, 476, 857, 486]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[92]: text=FEV 1, bbox=[94, 499, 145, 508]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[93]: text=[L], bbox=[327, 497, 351, 507]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[94]: text=2.98, bbox=[401, 495, 439, 505]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[95]: text=1.10, bbox=[485, 494, 521, 504]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[96]: text=36.9, bbox=[568, 492, 605, 502]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[97]: text=1.55, bbox=[652, 491, 689, 501]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[98]: text=52.1, bbox=[735, 490, 773, 500]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[99]: text=41.1, bbox=[820, 488, 857, 498]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[100]: text=FEV 1 % FVC, bbox=[94, 511, 207, 520]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[101]: text=[%], bbox=[327, 509, 351, 519]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[102]: text=83.77, bbox=[392, 507, 439, 517]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[103]: text=41.10, bbox=[477, 506, 521, 516]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[104]: text=49.1, bbox=[568, 505, 605, 515]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[105]: text=50.82, bbox=[645, 504, 689, 514]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[106]: text=60.7, bbox=[735, 503, 773, 513]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[107]: text=23.6, bbox=[820, 501, 857, 511]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[108]: text=FEV 1 % VC MAX, bbox=[94, 524, 238, 533]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[109]: text=[%], bbox=[327, 522, 351, 532]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[110]: text=77.13, bbox=[392, 520, 439, 530]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[111]: text=40.51, bbox=[477, 519, 521, 529]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[112]: text=52.5, bbox=[568, 517, 605, 527]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[113]: text=50.49, bbox=[645, 516, 689, 526]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[114]: text=65.5, bbox=[735, 515, 773, 525]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[115]: text=24.6, bbox=[820, 513, 857, 523]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[116]: text=PEF, bbox=[94, 538, 127, 547]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[117]: text=[L/s], bbox=[309, 535, 351, 545]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[118]: text=7.87, bbox=[401, 533, 439, 543]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[119]: text=2.33, bbox=[485, 532, 521, 542]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[120]: text=29.6, bbox=[568, 530, 605, 540]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[121]: text=3.18, bbox=[652, 529, 689, 539]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[122]: text=40.4, bbox=[735, 528, 773, 538]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[123]: text=36.6, bbox=[820, 526, 857, 536]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[124]: text=MEF 75, bbox=[94, 551, 157, 560]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[125]: text=[L/s], bbox=[309, 548, 351, 558]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[126]: text=6.92, bbox=[401, 546, 439, 556]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[127]: text=0.96, bbox=[485, 545, 521, 555]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[128]: text=13.9, bbox=[568, 543, 605, 553]
2026-08-10 13:11:43,587 INFO     29 [qwen-vl-text] coord item[129]: text=1.65, bbox=[652, 542, 689, 552]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[130]: text=23.9, bbox=[735, 541, 773, 551]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[131]: text=72.1, bbox=[820, 539, 857, 549]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[132]: text=MEF 50, bbox=[94, 564, 157, 573]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[133]: text=[L/s], bbox=[309, 561, 351, 571]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[134]: text=4.17, bbox=[401, 558, 439, 568]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[135]: text=0.52, bbox=[485, 557, 521, 567]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[136]: text=12.5, bbox=[568, 556, 605, 566]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[137]: text=0.85, bbox=[652, 555, 689, 565]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[138]: text=20.3, bbox=[735, 554, 773, 564]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[139]: text=63.0, bbox=[820, 552, 857, 562]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[140]: text=MEF 25, bbox=[94, 577, 157, 586]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[141]: text=[L/s], bbox=[309, 574, 351, 584]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[142]: text=1.51, bbox=[401, 571, 439, 581]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[143]: text=0.22, bbox=[485, 570, 521, 580]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[144]: text=14.3, bbox=[568, 568, 605, 578]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[145]: text=0.35, bbox=[652, 567, 689, 577]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[146]: text=23.2, bbox=[735, 566, 773, 576]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[147]: text=62.9, bbox=[820, 564, 857, 574]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[148]: text=MMEF 75/25, bbox=[94, 590, 197, 600]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[149]: text=[L/s], bbox=[309, 587, 351, 597]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[150]: text=3.49, bbox=[401, 584, 439, 594]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[151]: text=0.44, bbox=[485, 583, 521, 593]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[152]: text=12.6, bbox=[568, 581, 605, 591]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[153]: text=0.75, bbox=[652, 580, 689, 590]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[154]: text=21.3, bbox=[735, 578, 773, 588]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] coord item[155]: text=69.5, bbox=[820, 576, 857, 586]
2026-08-10 13:11:43,588 INFO     29 [qwen-vl-text] page=3 — 146/146 coords, api_time=60.1s
2026-08-10 13:11:43,594 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2855176, prompt_len=2367
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共113行）
["JAEGER PCMED", "渑池县人民医院", "肺功能检查报告", "常规通气", "姓名：", "住院号：0", "性别：男", "身高：165 cm", "标准体重：108 %", "吸烟史：", "科别：", "测试号：2025042503", "年龄：56 Years", "体重：70 kg", "体表面积：1.77 m", "预计值 实测值 实测/预", "测试日期 25/4/25", "测试时间 9:19:05]", "VC MAX [L] 3.85 2.72 70.6", "IRV [L] 0.91", "ERV [L] 1.11 1.02 91.8", "IC [L] 2.74 1.69 61.9", "VT [L] 0.50 0.78 156.7", "MV [L/min] 10.00 18.75 187.5", "VC IN [L] 3.85 2.69 70.0", "VC EX [L] 3.85 2.72 70.6", "BF [1/min] 20.00 23.93 119.7", "FVC [L] 3.71 2.68 72.2", "PEF [L/s] 7.87 2.33 29.6", "FEV 0.5 [L] 0.70", "FEV 1 [L] 2.98 1.10 36.9", "FEV 2 [L] 1.60", "FEV 3 [L] 1.91", "FEV6 [L] 2.45", "FEF 200-1200 [L/s] 0.94", "FEV 1 % FVC [%] 83.77 41.10 49.1", "FEV 1 % VC MAX [%] 77.13 40.51 52.5", "MEF 75 [L/s] 6.92 0.96 13.9", "MEF 50 [L/s] 4.17 0.52 12.5", "MEF 25 [L/s] 1.51 0.22 14.3", "MMEF 75/25 [L/s] 3.49 0.44 12.6", "FEF 75/85 [L/s] 0.77 0.18 23.0", "FEF50 % FIF50 [%] 38.63", "PIF [L/s] 1.41", "FVC IN [L] 3.85 2.69 70.0", "FET [s] 7.87", "FIF 50 [L/s] 1.35", "FIV1 [L] 1.10", "FIV1 % FVC [%] 40.89", "T IN [s] 1.21", "T EX [s] 1.30", "T TOT [s] 2.51", "MIF [L/s] 0.65", "MEF [L/s] 0.60", "MVV [L/min] 113.25 52.56 46.4", "FEF50 % FIF50 [%] 38.63", "V backextrapolation ex [L] 0.02", "V backextrapol. % FVC [%] 0.75", "测试结果", "1、重度阻塞性肺通气功能障碍，小气道功能降低。", "2、肺弥散功能正常。", "3、残气量正常，残气量/肺总量增高。", "4、沙丁胺醇气雾剂支气管舒张试验呈阳性，FEV1.0改41.1%。", "5、建议定期复查。", "报告医师：", "报告日期：2025.4.25", "TLC", "6 Vol [L]", "FRCl eth", "R", "Time [min]", "PredA@0 0.2 0.4 0.6 0.8 1.0", "Flow [L/s]", "F/V ex", "10", "5", "0", "2", "4", "6", "10", "F/V in", "Vol%VCmax", "0", "0", "Vol [L]", "20", "40", "60", "80", "100", "2", "VCmax", "4", "6", "8", "Time [s]", "8", "4", "Vol [L]", "2", "0", "2", "4", "Time [s]", "0", "2", "4", "6", "8", "10", "12", "14"]

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
2026-08-10 13:12:18,820 INFO     29 [qwen-vl-text] coord API raw response (len=6721):
[
	{"text": "JAEGER PCMED", "bbox": [723, 64, 901, 78]},
	{"text": "渑池县人民医院", "bbox": [364, 79, 616, 101]},
	{"text": "肺功能检查报告", "bbox": [393, 104, 594, 121]},
	{"text": "常规通气", "bbox": [448, 126, 548, 141]},
	{"text": "姓名：", "bbox": [119, 149, 165, 161]},
	{"text": "住院号：", "bbox": [119, 160, 181, 172]},
	{"text": "0", "bbox": [283, 163, 293, 173]},
	{"text": "性别：", "bbox": [119, 171, 165, 183]},
	{"text": "男", "bbox": [284, 173, 302, 184]},
	{"text": "身高：", "bbox": [119, 183, 165, 194]},
	{"text": "165 cm", "bbox": [284, 184, 340, 195]},
	{"text": "标准体重：", "bbox": [119, 194, 200, 206]},
	{"text": "108 %", "bbox": [284, 196, 340, 207]},
	{"text": "吸烟史：", "bbox": [119, 206, 183, 218]},
	{"text": "科别：", "bbox": [454, 146, 499, 158]},
	{"text": "测试号：", "bbox": [454, 157, 516, 169]},
	{"text": "年龄：", "bbox": [454, 168, 500, 180]},
	{"text": "体重：", "bbox": [454, 180, 500, 192]},
	{"text": "体表面积：", "bbox": [454, 191, 535, 203]},
	{"text": "预计值 实测值 实测/预", "bbox": [385, 220, 602, 233]},
	{"text": "测试日期 25/4/25", "bbox": [124, 236, 196, 248]},
	{"text": "测试时间 9:19:05]", "bbox": [124, 248, 196, 260]},
	{"text": "VC MAX [L] 3.85 2.72 70.6", "bbox": [120, 270, 604, 281]},
	{"text": "IRV [L] 0.91", "bbox": [120, 281, 522, 293]},
	{"text": "ERV [L] 1.11 1.02 91.8", "bbox": [117, 293, 604, 304]},
	{"text": "IC [L] 2.74 1.69 61.9", "bbox": [117, 304, 604, 316]},
	{"text": "VT [L] 0.50 0.78 156.7", "bbox": [114, 316, 604, 327]},
	{"text": "MV [L/min] 10.00 18.75 187.5", "bbox": [112, 327, 604, 339]},
	{"text": "VC IN [L] 3.85 2.69 70.0", "bbox": [111, 339, 604, 351]},
	{"text": "VC EX [L] 3.85 2.72 70.6", "bbox": [111, 351, 604, 363]},
	{"text": "BF [1/min] 20.00 23.93 119.7", "bbox": [111, 363, 604, 374]},
	{"text": "FVC [L] 3.71 2.68 72.2", "bbox": [111, 374, 604, 386]},
	{"text": "PEF [L/s] 7.87 2.33 29.6", "bbox": [312, 386, 604, 398]},
	{"text": "FEV 0.5 [L] 0.70", "bbox": [111, 411, 526, 423]},
	{"text": "FEV 1 [L] 2.98 1.10 36.9", "bbox": [111, 423, 604, 435]},
	{"text": "FEV 2 [L] 1.60", "bbox": [111, 435, 526, 447]},
	{"text": "FEV 3 [L] 1.91", "bbox": [111, 447, 526, 459]},
	{"text": "FEV6 [L] 2.45", "bbox": [111, 459, 526, 471]},
	{"text": "FEF 200-1200 [L/s] 0.94", "bbox": [117, 471, 526, 483]},
	{"text": "FEV 1 % FVC [%] 83.77 41.10 49.1", "bbox": [119, 497, 598, 509]},
	{"text": "FEV 1 % VC MAX [%] 77.13 40.51 52.5", "bbox": [119, 509, 598, 521]},
	{"text": "MEF 75 [L/s] 6.92 0.96 13.9", "bbox": [119, 521, 598, 533]},
	{"text": "MEF 50 [L/s] 4.17 0.52 12.5", "bbox": [119, 533, 598, 545]},
	{"text": "MEF 25 [L/s] 1.51 0.22 14.3", "bbox": [119, 545, 598, 557]},
	{"text": "MMEF 75/25 [L/s] 3.49 0.44 12.6", "bbox": [117, 557, 598, 569]},
	{"text": "FEF 75/85 [L/s] 0.77 0.18 23.0", "bbox": [117, 569, 598, 581]},
	{"text": "FEF50 % FIF50 [%] 38.63", "bbox": [117, 581, 526, 593]},
	{"text": "PIF [L/s] 1.41", "bbox": [117, 593, 526, 605]},
	{"text": "FVC IN [L] 3.85 2.69 70.0", "bbox": [117, 605, 614, 617]},
	{"text": "FET [s] 7.87", "bbox": [117, 617, 526, 629]},
	{"text": "FIF 50 [L/s] 1.35", "bbox": [117, 629, 526, 641]},
	{"text": "FIV1 [L] 1.10", "bbox": [117, 641, 526, 653]},
	{"text": "FIV1 % FVC [%] 40.89", "bbox": [117, 653, 526, 665]},
	{"text": "T IN [s] 1.21", "bbox": [117, 665, 526, 677]},
	{"text": "T EX [s] 1.30", "bbox": [117, 677, 526, 689]},
	{"text": "T TOT [s] 2.51", "bbox": [117, 689, 526, 701]},
	{"text": "MIF [L/s] 0.65", "bbox": [111, 701, 526, 713]},
	{"text": "MEF [L/s] 0.60", "bbox": [111, 713, 526, 725]},
	{"text": "MVV [L/min] 113.25 52.56 46.4", "bbox": [298, 725, 614, 737]},
	{"text": "FEF50 % FIF50 [%] 38.63", "bbox": [111, 737, 526, 749]},
	{"text": "V backextrapolation ex [L] 0.02", "bbox": [108, 749, 526, 761]},
	{"text": "V backextrapol. % FVC [%] 0.75", "bbox": [108, 761, 526, 773]},
	{"text": "测试结果", "bbox": [108, 796, 218, 817]},
	{"text": "1、重度阻塞性肺通气功能障碍，小气道功能降低。", "bbox": [105, 814, 600, 840]},
	{"text": "2、肺弥散功能正常。", "bbox": [102, 835, 310, 860]},
	{"text": "3、残气量正常，残气量/肺总量增高。", "bbox": [102, 848, 480, 875]},
	{"text": "4、沙丁胺醇气雾剂支气管舒张试验呈阳性，FEV1.0改41.1%。", "bbox": [100, 862, 703, 892]},
	{"text": "5、建议定期复查。", "bbox": [100, 888, 286, 912]},
	{"text": "报告医师：", "bbox": [415, 907, 675, 934]},
	{"text": "报告日期：2025.4.25", "bbox": [683, 905, 916, 931]},
	{"text": "TLC", "bbox": [618, 240, 638, 248]},
	{"text": "6 Vol [L]", "bbox": [643, 236, 690, 247]},
	{"text": "FRCl eth", "bbox": [620, 285, 664, 293]},
	{"text": "R", "bbox": [621, 302, 634, 310]},
	{"text": "Time [min]", "bbox": [739, 321, 793, 329]},
	{"text": "PredA@0 0.2 0.4 0.6 0.8 1.0", "bbox": [624, 338, 880, 347]},
	{"text": "Flow [L/s]", "bbox": [651, 360, 703, 369]},
	{"text": "F/V ex", "bbox": [783, 360, 816, 368]},
	{"text": "10", "bbox": [634, 373, 647, 380]},
	{"text": "5", "bbox": [639, 393, 647, 400]},
	{"text": "0", "bbox": [639, 413, 647, 420]},
	{"text": "2", "bbox": [704, 420, 712, 428]},
	{"text": "4", "bbox": [760, 420, 768, 428]},
	{"text": "6", "bbox": [816, 420, 824, 428]},
	{"text": "10", "bbox": [634, 453, 647, 460]},
	{"text": "F/V in", "bbox": [785, 462, 814, 470]},
	{"text": "Vol%VCmax", "bbox": [626, 487, 688, 495]},
	{"text": "0", "bbox": [643, 497, 651, 505]},
	{"text": "0", "bbox": [660, 497, 668, 505]},
	{"text": "Vol [L]", "bbox": [675, 500, 707, 509]},
	{"text": "20", "bbox": [640, 505, 651, 513]},
	{"text": "40", "bbox": [640, 513, 651, 521]},
	{"text": "60", "bbox": [640, 521, 651, 529]},
	{"text": "80", "bbox": [640, 529, 651, 537]},
	{"text": "100", "bbox": [634, 530, 651, 538]},
	{"text": "2", "bbox": [660, 521, 668, 529]},
	{"text": "VCmax", "bbox": [688, 525, 723, 533]},
	{"text": "4", "bbox": [662, 545, 670, 553]},
	{"text": "6", "bbox": [662, 570, 670, 578]},
	{"text": "8", "bbox": [664, 595, 672, 603]},
	{"text": "Time [s]", "bbox": [758, 585, 800, 594]},
	{"text": "0", "bbox": [675, 604, 682, 612]},
	{"text": "2", "bbox": [725, 604, 733, 612]},
	{"text": "4", "bbox": [777, 604, 784, 612]},
	{"text": "6", "bbox": [828, 604, 836, 612]},
	{"text": "8", "bbox": [879, 604, 886, 612]},
	{"text": "4", "bbox": [640, 628, 647, 636]},
	{"text": "Vol [L]", "bbox": [655, 631, 688, 640]},
	{"text": "2", "bbox": [640, 654, 647, 662]},
	{"text": "0", "bbox": [640, 680, 647, 688]},
	{"text": "2", "bbox": [643, 708, 651, 716]},
	{"text": "4", "bbox": [643, 736, 651, 744]},
	{"text": "Time [s]", "bbox": [753, 725, 796, 735]},
	{"text": "0", "bbox": [655, 745, 662, 753]},
	{"text": "2", "bbox": [686, 745, 693, 753]},
	{"text": "4", "bbox": [717, 745, 724, 753]},
	{"text": "6", "bbox": [750, 745, 757, 753]},
	{"text": "8", "bbox": [781, 745, 788, 753]},
	{"text": "10", "bbox": [810, 745, 822, 753]},
	{"text": "12", "bbox": [842, 745, 854, 753]},
	{"text": "14", "bbox": [874, 745, 886, 753]}
]
2026-08-10 13:12:18,821 INFO     29 [qwen-vl-text] coord API: raw_items=121, valid_items=121, elapsed=35.2s
2026-08-10 13:12:18,821 INFO     29 [qwen-vl-text] coord item[0]: text=JAEGER PCMED, bbox=[723, 64, 901, 78]
2026-08-10 13:12:18,821 INFO     29 [qwen-vl-text] coord item[1]: text=渑池县人民医院, bbox=[364, 79, 616, 101]
2026-08-10 13:12:18,821 INFO     29 [qwen-vl-text] coord item[2]: text=肺功能检查报告, bbox=[393, 104, 594, 121]
2026-08-10 13:12:18,821 INFO     29 [qwen-vl-text] coord item[3]: text=常规通气, bbox=[448, 126, 548, 141]
2026-08-10 13:12:18,821 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[119, 149, 165, 161]
2026-08-10 13:12:18,821 INFO     29 [qwen-vl-text] coord item[5]: text=住院号：, bbox=[119, 160, 181, 172]
2026-08-10 13:12:18,821 INFO     29 [qwen-vl-text] coord item[6]: text=0, bbox=[283, 163, 293, 173]
2026-08-10 13:12:18,821 INFO     29 [qwen-vl-text] coord item[7]: text=性别：, bbox=[119, 171, 165, 183]
2026-08-10 13:12:18,821 INFO     29 [qwen-vl-text] coord item[8]: text=男, bbox=[284, 173, 302, 184]
2026-08-10 13:12:18,821 INFO     29 [qwen-vl-text] coord item[9]: text=身高：, bbox=[119, 183, 165, 194]
2026-08-10 13:12:18,821 INFO     29 [qwen-vl-text] coord item[10]: text=165 cm, bbox=[284, 184, 340, 195]
2026-08-10 13:12:18,821 INFO     29 [qwen-vl-text] coord item[11]: text=标准体重：, bbox=[119, 194, 200, 206]
2026-08-10 13:12:18,821 INFO     29 [qwen-vl-text] coord item[12]: text=108 %, bbox=[284, 196, 340, 207]
2026-08-10 13:12:18,821 INFO     29 [qwen-vl-text] coord item[13]: text=吸烟史：, bbox=[119, 206, 183, 218]
2026-08-10 13:12:18,821 INFO     29 [qwen-vl-text] coord item[14]: text=科别：, bbox=[454, 146, 499, 158]
2026-08-10 13:12:18,821 INFO     29 [qwen-vl-text] coord item[15]: text=测试号：, bbox=[454, 157, 516, 169]
2026-08-10 13:12:18,821 INFO     29 [qwen-vl-text] coord item[16]: text=年龄：, bbox=[454, 168, 500, 180]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[17]: text=体重：, bbox=[454, 180, 500, 192]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[18]: text=体表面积：, bbox=[454, 191, 535, 203]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[19]: text=预计值 实测值 实测/预, bbox=[385, 220, 602, 233]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[20]: text=测试日期 25/4/25, bbox=[124, 236, 196, 248]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[21]: text=测试时间 9:19:05], bbox=[124, 248, 196, 260]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[22]: text=VC MAX [L] 3.85 2.72 70.6, bbox=[120, 270, 604, 281]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[23]: text=IRV [L] 0.91, bbox=[120, 281, 522, 293]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[24]: text=ERV [L] 1.11 1.02 91.8, bbox=[117, 293, 604, 304]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[25]: text=IC [L] 2.74 1.69 61.9, bbox=[117, 304, 604, 316]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[26]: text=VT [L] 0.50 0.78 156.7, bbox=[114, 316, 604, 327]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[27]: text=MV [L/min] 10.00 18.75 187.5, bbox=[112, 327, 604, 339]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[28]: text=VC IN [L] 3.85 2.69 70.0, bbox=[111, 339, 604, 351]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[29]: text=VC EX [L] 3.85 2.72 70.6, bbox=[111, 351, 604, 363]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[30]: text=BF [1/min] 20.00 23.93 119.7, bbox=[111, 363, 604, 374]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[31]: text=FVC [L] 3.71 2.68 72.2, bbox=[111, 374, 604, 386]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[32]: text=PEF [L/s] 7.87 2.33 29.6, bbox=[312, 386, 604, 398]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[33]: text=FEV 0.5 [L] 0.70, bbox=[111, 411, 526, 423]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[34]: text=FEV 1 [L] 2.98 1.10 36.9, bbox=[111, 423, 604, 435]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[35]: text=FEV 2 [L] 1.60, bbox=[111, 435, 526, 447]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[36]: text=FEV 3 [L] 1.91, bbox=[111, 447, 526, 459]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[37]: text=FEV6 [L] 2.45, bbox=[111, 459, 526, 471]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[38]: text=FEF 200-1200 [L/s] 0.94, bbox=[117, 471, 526, 483]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[39]: text=FEV 1 % FVC [%] 83.77 41.10 49.1, bbox=[119, 497, 598, 509]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[40]: text=FEV 1 % VC MAX [%] 77.13 40.51 52.5, bbox=[119, 509, 598, 521]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[41]: text=MEF 75 [L/s] 6.92 0.96 13.9, bbox=[119, 521, 598, 533]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[42]: text=MEF 50 [L/s] 4.17 0.52 12.5, bbox=[119, 533, 598, 545]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[43]: text=MEF 25 [L/s] 1.51 0.22 14.3, bbox=[119, 545, 598, 557]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[44]: text=MMEF 75/25 [L/s] 3.49 0.44 12.6, bbox=[117, 557, 598, 569]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[45]: text=FEF 75/85 [L/s] 0.77 0.18 23.0, bbox=[117, 569, 598, 581]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[46]: text=FEF50 % FIF50 [%] 38.63, bbox=[117, 581, 526, 593]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[47]: text=PIF [L/s] 1.41, bbox=[117, 593, 526, 605]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[48]: text=FVC IN [L] 3.85 2.69 70.0, bbox=[117, 605, 614, 617]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[49]: text=FET [s] 7.87, bbox=[117, 617, 526, 629]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[50]: text=FIF 50 [L/s] 1.35, bbox=[117, 629, 526, 641]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[51]: text=FIV1 [L] 1.10, bbox=[117, 641, 526, 653]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[52]: text=FIV1 % FVC [%] 40.89, bbox=[117, 653, 526, 665]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[53]: text=T IN [s] 1.21, bbox=[117, 665, 526, 677]
2026-08-10 13:12:18,822 INFO     29 [qwen-vl-text] coord item[54]: text=T EX [s] 1.30, bbox=[117, 677, 526, 689]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[55]: text=T TOT [s] 2.51, bbox=[117, 689, 526, 701]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[56]: text=MIF [L/s] 0.65, bbox=[111, 701, 526, 713]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[57]: text=MEF [L/s] 0.60, bbox=[111, 713, 526, 725]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[58]: text=MVV [L/min] 113.25 52.56 46.4, bbox=[298, 725, 614, 737]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[59]: text=FEF50 % FIF50 [%] 38.63, bbox=[111, 737, 526, 749]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[60]: text=V backextrapolation ex [L] 0.02, bbox=[108, 749, 526, 761]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[61]: text=V backextrapol. % FVC [%] 0.75, bbox=[108, 761, 526, 773]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[62]: text=测试结果, bbox=[108, 796, 218, 817]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[63]: text=1、重度阻塞性肺通气功能障碍，小气道功能降低。, bbox=[105, 814, 600, 840]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[64]: text=2、肺弥散功能正常。, bbox=[102, 835, 310, 860]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[65]: text=3、残气量正常，残气量/肺总量增高。, bbox=[102, 848, 480, 875]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[66]: text=4、沙丁胺醇气雾剂支气管舒张试验呈阳性，FEV1.0改41.1%。, bbox=[100, 862, 703, 892]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[67]: text=5、建议定期复查。, bbox=[100, 888, 286, 912]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[68]: text=报告医师：, bbox=[415, 907, 675, 934]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[69]: text=报告日期：2025.4.25, bbox=[683, 905, 916, 931]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[70]: text=TLC, bbox=[618, 240, 638, 248]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[71]: text=6 Vol [L], bbox=[643, 236, 690, 247]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[72]: text=FRCl eth, bbox=[620, 285, 664, 293]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[73]: text=R, bbox=[621, 302, 634, 310]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[74]: text=Time [min], bbox=[739, 321, 793, 329]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[75]: text=PredA@0 0.2 0.4 0.6 0.8 1.0, bbox=[624, 338, 880, 347]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[76]: text=Flow [L/s], bbox=[651, 360, 703, 369]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[77]: text=F/V ex, bbox=[783, 360, 816, 368]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[78]: text=10, bbox=[634, 373, 647, 380]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[79]: text=5, bbox=[639, 393, 647, 400]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[80]: text=0, bbox=[639, 413, 647, 420]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[81]: text=2, bbox=[704, 420, 712, 428]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[82]: text=4, bbox=[760, 420, 768, 428]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[83]: text=6, bbox=[816, 420, 824, 428]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[84]: text=10, bbox=[634, 453, 647, 460]
2026-08-10 13:12:18,823 INFO     29 [qwen-vl-text] coord item[85]: text=F/V in, bbox=[785, 462, 814, 470]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[86]: text=Vol%VCmax, bbox=[626, 487, 688, 495]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[87]: text=0, bbox=[643, 497, 651, 505]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[88]: text=0, bbox=[660, 497, 668, 505]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[89]: text=Vol [L], bbox=[675, 500, 707, 509]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[90]: text=20, bbox=[640, 505, 651, 513]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[91]: text=40, bbox=[640, 513, 651, 521]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[92]: text=60, bbox=[640, 521, 651, 529]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[93]: text=80, bbox=[640, 529, 651, 537]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[94]: text=100, bbox=[634, 530, 651, 538]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[95]: text=2, bbox=[660, 521, 668, 529]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[96]: text=VCmax, bbox=[688, 525, 723, 533]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[97]: text=4, bbox=[662, 545, 670, 553]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[98]: text=6, bbox=[662, 570, 670, 578]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[99]: text=8, bbox=[664, 595, 672, 603]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[100]: text=Time [s], bbox=[758, 585, 800, 594]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[101]: text=0, bbox=[675, 604, 682, 612]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[102]: text=2, bbox=[725, 604, 733, 612]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[103]: text=4, bbox=[777, 604, 784, 612]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[104]: text=6, bbox=[828, 604, 836, 612]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[105]: text=8, bbox=[879, 604, 886, 612]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[106]: text=4, bbox=[640, 628, 647, 636]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[107]: text=Vol [L], bbox=[655, 631, 688, 640]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[108]: text=2, bbox=[640, 654, 647, 662]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[109]: text=0, bbox=[640, 680, 647, 688]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[110]: text=2, bbox=[643, 708, 651, 716]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[111]: text=4, bbox=[643, 736, 651, 744]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[112]: text=Time [s], bbox=[753, 725, 796, 735]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[113]: text=0, bbox=[655, 745, 662, 753]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[114]: text=2, bbox=[686, 745, 693, 753]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[115]: text=4, bbox=[717, 745, 724, 753]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[116]: text=6, bbox=[750, 745, 757, 753]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[117]: text=8, bbox=[781, 745, 788, 753]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[118]: text=10, bbox=[810, 745, 822, 753]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[119]: text=12, bbox=[842, 745, 854, 753]
2026-08-10 13:12:18,824 INFO     29 [qwen-vl-text] coord item[120]: text=14, bbox=[874, 745, 886, 753]
2026-08-10 13:12:18,825 INFO     29 [qwen-vl-text] page=4 — 113/113 coords, api_time=35.2s
2026-08-10 13:12:18,826 INFO     29 [qwen-vl-text] new_positions (457):
[[2, 421.26, 533.12, 36.205999999999996, 47.994], [2, 226.1, 352.24, 47.994, 65.676], [2, 246.32999999999998, 334.39, 67.36, 81.67399999999999], [2, 270.72499999999997, 321.895, 85.042, 97.672], [2, 48.195, 75.565, 100.198, 110.30199999999999], [2, 48.195, 158.26999999999998, 110.30199999999999, 120.40599999999999], [2, 48.195, 192.78, 120.40599999999999, 130.51], [2, 48.195, 182.665, 130.51, 140.614], [2, 48.195, 176.715, 140.614, 150.718], [2, 48.195, 75.565, 150.718, 159.98], [2, 252.28, 301.66499999999996, 100.198, 110.30199999999999], [2, 252.28, 355.81, 110.30199999999999, 120.40599999999999], [2, 252.28, 291.55, 120.40599999999999, 130.51], [2, 252.28, 291.55, 130.51, 140.614], [2, 252.28, 291.55, 140.614, 150.718], [2, 252.28, 280.245, 150.718, 159.98], [2, 44.625, 94.60499999999999, 186.924, 197.028], [2, 44.625, 94.60499999999999, 197.028, 207.132], [2, 211.82, 249.30499999999998, 176.82, 186.924], [2, 278.46, 314.755, 176.82, 186.924], [2, 345.09999999999997, 374.84999999999997, 176.82, 186.924], [2, 377.825, 390.32, 180.188, 188.608], [2, 393.29499999999996, 398.65, 176.82, 183.55599999999998], [2, 401.625, 421.26, 178.504, 186.924], [2, 273.10499999999996, 315.34999999999997, 188.608, 197.028], [2, 254.66, 316.53999999999996, 198.712, 207.132], [2, 39.864999999999995, 79.72999999999999, 218.078, 226.498], [2, 161.84, 178.5, 218.078, 227.34], [2, 223.72, 248.70999999999998, 218.078, 226.498], [2, 291.55, 316.53999999999996, 218.078, 226.498], [2, 352.835, 377.825, 218.078, 226.498], [2, 38.675, 59.5, 228.182, 236.602], [2, 161.84, 178.5, 228.182, 237.444], [2, 223.72, 248.70999999999998, 228.182, 236.602], [2, 291.55, 316.53999999999996, 228.182, 236.602], [2, 352.835, 377.825, 228.182, 236.602], [2, 37.485, 52.36, 239.128, 247.548], [2, 135.66, 177.31, 239.128, 248.39], [2, 217.76999999999998, 248.70999999999998, 239.128, 247.548], [2, 286.78999999999996, 316.53999999999996, 239.128, 247.548], [2, 348.075, 377.825, 239.128, 247.548], [2, 37.485, 69.615, 250.07399999999998, 258.49399999999997], [2, 161.84, 178.5, 250.07399999999998, 259.336], [2, 223.72, 248.70999999999998, 250.07399999999998, 258.49399999999997], [2, 291.55, 316.53999999999996, 250.07399999999998, 258.49399999999997], [2, 354.025, 379.015, 250.07399999999998, 258.49399999999997], [2, 37.485, 108.28999999999999, 261.02, 270.282], [2, 161.84, 178.5, 261.02, 270.282], [2, 217.76999999999998, 248.70999999999998, 261.02, 270.282], [2, 286.78999999999996, 316.53999999999996, 261.02, 270.282], [2, 354.025, 379.015, 261.02, 270.282], [2, 37.485, 56.525, 273.65, 282.07], [2, 148.75, 177.31, 273.65, 282.912], [2, 223.72, 248.70999999999998, 273.65, 282.07], [2, 291.55, 316.53999999999996, 273.65, 282.07], [2, 354.025, 379.015, 273.65, 282.07], [2, 37.485, 75.565, 286.28, 294.7], [2, 148.75, 177.31, 286.28, 295.542], [2, 223.72, 248.70999999999998, 286.28, 294.7], [2, 291.55, 316.53999999999996, 286.28, 294.7], [2, 354.025, 379.015, 286.28, 294.7], [2, 37.485, 75.565, 298.068, 307.33], [2, 148.75, 177.31, 298.068, 307.33], [2, 223.72, 248.70999999999998, 298.068, 307.33], [2, 291.55, 316.53999999999996, 298.068, 307.33], [2, 354.025, 379.015, 298.068, 307.33], [2, 37.485, 75.565, 309.856, 319.118], [2, 148.75, 177.31, 309.856, 319.118], [2, 223.72, 248.70999999999998, 309.856, 319.118], [2, 291.55, 316.53999999999996, 309.856, 319.118], [2, 354.025, 379.015, 309.856, 319.118], [2, 37.485, 102.33999999999999, 321.644, 330.906], [2, 148.75, 177.31, 321.644, 330.906], [2, 223.72, 248.70999999999998, 321.644, 330.906], [2, 291.55, 316.53999999999996, 321.644, 330.906], [2, 354.025, 379.015, 321.644, 330.906], [2, 37.485, 58.309999999999995, 334.274, 342.69399999999996], [2, 135.66, 178.5, 334.274, 343.536], [2, 211.82, 248.70999999999998, 334.274, 342.69399999999996], [2, 286.78999999999996, 316.53999999999996, 334.274, 342.69399999999996], [2, 354.025, 379.015, 334.274, 342.69399999999996], [2, 39.864999999999995, 78.53999999999999, 357.84999999999997, 367.11199999999997], [2, 163.03, 178.5, 357.84999999999997, 367.11199999999997], [2, 224.91, 249.30499999999998, 357.84999999999997, 367.11199999999997], [2, 292.74, 317.72999999999996, 357.84999999999997, 367.11199999999997], [2, 355.215, 379.60999999999996, 357.84999999999997, 367.11199999999997], [2, 39.864999999999995, 72.59, 370.47999999999996, 378.9], [2, 163.03, 178.5, 370.47999999999996, 379.74199999999996], [2, 224.91, 249.30499999999998, 370.47999999999996, 378.9], [2, 292.74, 317.72999999999996, 370.47999999999996, 378.9], [2, 349.265, 379.60999999999996, 370.47999999999996, 378.9], [2, 39.864999999999995, 98.175, 382.268, 391.53], [2, 163.03, 178.5, 382.268, 391.53], [2, 218.95999999999998, 249.30499999999998, 382.268, 391.53], [2, 287.97999999999996, 317.72999999999996, 382.268, 391.53], [2, 349.265, 379.60999999999996, 382.268, 391.53], [2, 39.864999999999995, 78.53999999999999, 394.056, 403.318], [2, 163.03, 178.5, 394.056, 403.318], [2, 224.91, 249.30499999999998, 394.056, 403.318], [2, 292.74, 317.72999999999996, 394.056, 403.318], [2, 349.265, 379.60999999999996, 394.056, 403.318], [2, 39.864999999999995, 103.53, 405.844, 415.106], [2, 163.03, 178.5, 405.844, 415.106], [2, 218.95999999999998, 249.30499999999998, 405.844, 415.106], [2, 287.97999999999996, 317.72999999999996, 405.844, 415.106], [2, 349.265, 379.60999999999996, 405.844, 415.106], [2, 38.675, 178.5, 417.632, 426.894], [2, 224.91, 249.30499999999998, 417.632, 426.894], [2, 292.74, 317.72999999999996, 417.632, 426.894], [2, 355.215, 379.60999999999996, 417.632, 426.894], [2, 38.675, 178.5, 429.41999999999996, 438.68199999999996], [2, 224.91, 249.30499999999998, 429.41999999999996, 438.68199999999996], [2, 292.74, 317.72999999999996, 429.41999999999996, 438.68199999999996], [2, 349.265, 379.60999999999996, 429.41999999999996, 438.68199999999996], [2, 37.485, 50.574999999999996, 442.05, 450.46999999999997], [2, 123.75999999999999, 178.5, 442.05, 451.312], [2, 287.97999999999996, 317.72999999999996, 439.524, 447.94399999999996], [2, 37.485, 50.574999999999996, 454.68, 463.09999999999997], [2, 163.03, 178.5, 452.996, 463.09999999999997], [2, 224.91, 249.30499999999998, 452.996, 463.09999999999997], [2, 292.74, 317.72999999999996, 452.996, 463.09999999999997], [2, 357.0, 381.395, 450.46999999999997, 459.73199999999997], [2, 37.485, 178.5, 465.626, 474.888], [2, 224.91, 249.30499999999998, 465.626, 474.888], [2, 292.74, 317.72999999999996, 465.626, 474.888], [2, 357.0, 381.395, 463.09999999999997, 472.36199999999997], [2, 37.485, 178.5, 477.414, 486.676], [2, 224.91, 249.30499999999998, 477.414, 486.676], [2, 292.74, 317.72999999999996, 477.414, 486.676], [2, 351.05, 381.395, 474.888, 484.15], [2, 36.89, 56.525, 502.674, 511.936], [2, 161.84, 178.5, 500.99, 511.094], [2, 224.91, 249.30499999999998, 500.99, 511.094], [2, 293.93, 318.91999999999996, 499.306, 508.568], [2, 358.19, 382.585, 497.62199999999996, 506.88399999999996], [2, 36.89, 101.14999999999999, 515.304, 524.566], [2, 161.84, 178.5, 513.62, 523.7239999999999], [2, 293.93, 318.91999999999996, 511.094, 520.356], [2, 36.89, 95.19999999999999, 527.092, 537.196], [2, 161.84, 178.5, 526.25, 536.3539999999999], [2, 293.93, 318.91999999999996, 522.882, 532.144], [2, 36.89, 99.96, 539.722, 549.826], [2, 161.84, 178.5, 538.88, 548.1419999999999], [2, 35.699999999999996, 177.31, 552.352, 562.456], [2, 282.625, 320.11, 548.1419999999999, 557.404], [2, 33.915, 177.31, 564.982, 575.086], [2, 282.625, 320.11, 560.7719999999999, 570.034], [2, 33.915, 47.599999999999994, 579.2959999999999, 588.558], [2, 160.65, 177.31, 577.612, 587.716], [2, 289.765, 320.11, 573.4019999999999, 582.664], [2, 27.965, 102.33999999999999, 592.768, 607.924], [2, 380.205, 406.385, 218.078, 224.814], [2, 381.395, 390.32, 232.392, 239.128], [2, 382.585, 411.74, 262.704, 270.282], [2, 426.615, 436.72999999999996, 262.704, 270.282], [2, 451.60499999999996, 461.71999999999997, 262.704, 270.282], [2, 476.59499999999997, 486.11499999999995, 262.704, 270.282], [2, 501.585, 511.10499999999996, 262.704, 270.282], [2, 526.5749999999999, 536.095, 262.704, 270.282], [2, 452.2, 484.33, 249.232, 255.968], [2, 398.65, 428.4, 278.702, 287.122], [2, 478.38, 498.015, 278.702, 286.28], [2, 387.94, 395.67499999999995, 288.806, 295.542], [2, 390.91499999999996, 395.67499999999995, 306.488, 313.224], [2, 390.91499999999996, 395.67499999999995, 324.17, 330.906], [2, 429.59, 434.34999999999997, 330.906, 337.642], [2, 464.09999999999997, 468.265, 330.906, 337.642], [2, 496.825, 501.585, 330.906, 337.642], [2, 529.55, 535.5, 323.328, 330.906], [2, 390.91499999999996, 395.67499999999995, 341.01, 347.746], [2, 387.94, 395.67499999999995, 357.84999999999997, 365.428], [2, 478.38, 496.22999999999996, 366.27, 373.848], [2, 398.65, 419.47499999999997, 387.32, 395.74], [2, 384.965, 395.67499999999995, 404.15999999999997, 411.738], [2, 528.36, 536.095, 402.476, 410.054], [2, 389.72499999999997, 397.46, 439.524, 446.26], [2, 393.29499999999996, 398.65, 474.888, 481.62399999999997], [2, 399.84, 404.59999999999997, 484.15, 490.88599999999997], [2, 422.45, 427.21, 484.15, 490.88599999999997], [2, 446.25, 450.41499999999996, 484.15, 490.88599999999997], [2, 470.04999999999995, 474.215, 484.15, 490.88599999999997], [2, 492.65999999999997, 496.825, 484.15, 490.88599999999997], [2, 514.0799999999999, 521.22, 482.466, 489.202], [2, 531.93, 536.095, 474.888, 481.62399999999997], [2, 404.59999999999997, 438.515, 499.306, 508.568], [2, 396.865, 401.625, 507.726, 514.462], [2, 396.865, 401.625, 524.566, 531.302], [2, 396.865, 401.625, 543.932, 550.668], [2, 542.045, 547.995, 543.932, 551.51], [2, 398.65, 403.40999999999997, 562.456, 570.034], [2, 398.65, 403.40999999999997, 581.822, 588.558], [2, 459.935, 485.52, 581.822, 590.242], [2, 406.385, 411.145, 599.504, 606.24], [2, 433.15999999999997, 441.48999999999995, 599.504, 606.24], [2, 462.315, 470.04999999999995, 599.504, 606.24], [2, 490.875, 499.205, 597.8199999999999, 604.5559999999999], [2, 519.435, 527.765, 597.8199999999999, 604.5559999999999], [2, 406.385, 411.145, 599.504, 606.24], [3, 414.12, 520.625, 31.996, 45.467999999999996], [3, 214.795, 349.85999999999996, 42.1, 58.098], [3, 223.125, 336.175, 62.308, 77.464], [3, 249.89999999999998, 305.235, 81.67399999999999, 96.83], [3, 39.864999999999995, 69.615, 96.83, 107.776], [3, 261.8, 290.955, 99.356, 110.30199999999999], [3, 39.864999999999995, 82.11, 107.776, 118.722], [3, 149.345, 154.7, 110.30199999999999, 118.722], [3, 261.8, 302.26, 110.30199999999999, 121.24799999999999], [3, 365.925, 423.04499999999996, 111.98599999999999, 121.24799999999999], [3, 39.864999999999995, 69.615, 118.722, 129.668], [3, 149.345, 161.245, 119.564, 129.668], [3, 261.8, 290.955, 121.24799999999999, 132.194], [3, 365.925, 411.74, 122.932, 132.194], [3, 39.864999999999995, 69.615, 129.668, 140.614], [3, 149.345, 186.82999999999998, 131.352, 140.614], [3, 261.8, 290.955, 132.194, 143.14], [3, 365.925, 394.48499999999996, 133.036, 143.14], [3, 39.864999999999995, 94.60499999999999, 140.614, 151.56], [3, 149.345, 186.82999999999998, 142.298, 151.56], [3, 261.8, 312.96999999999997, 143.14, 154.08599999999998], [3, 365.925, 401.03, 143.982, 154.08599999999998], [3, 39.864999999999995, 83.895, 151.56, 162.506], [3, 61.879999999999995, 95.795, 194.50199999999998, 203.76399999999998], [3, 192.78, 214.795, 196.186, 203.76399999999998], [3, 289.765, 327.25, 191.976, 200.396], [3, 299.88, 305.235, 201.238, 208.816], [3, 309.995, 314.755, 201.238, 208.816], [3, 318.325, 339.15, 203.76399999999998, 213.868], [3, 296.31, 305.235, 210.5, 218.078], [3, 296.31, 305.235, 219.762, 227.34], [3, 296.31, 305.235, 229.86599999999999, 237.444], [3, 53.55, 58.309999999999995, 235.76, 243.338], [3, 296.31, 305.235, 239.128, 246.706], [3, 311.185, 315.945, 231.54999999999998, 239.128], [3, 293.93, 305.83, 248.39, 255.968], [3, 327.84499999999997, 349.85999999999996, 246.706, 254.284], [3, 271.91499999999996, 277.865, 259.336, 266.914], [3, 498.015, 503.37, 256.81, 264.388], [3, 53.55, 58.309999999999995, 263.546, 271.12399999999997], [3, 87.46499999999999, 92.225, 271.966, 279.544], [3, 114.24, 119.0, 271.966, 279.544], [3, 141.60999999999999, 146.37, 271.966, 279.544], [3, 168.98, 173.73999999999998, 271.966, 279.544], [3, 195.755, 200.515, 271.966, 279.544], [3, 221.935, 226.695, 271.966, 279.544], [3, 247.51999999999998, 252.28, 271.966, 279.544], [3, 273.7, 278.46, 269.44, 277.018], [3, 311.78, 316.53999999999996, 264.388, 271.966], [3, 55.335, 60.69, 290.49, 298.068], [3, 311.78, 316.53999999999996, 297.226, 304.804], [3, 53.55, 63.665, 317.43399999999997, 325.012], [3, 396.27, 421.85499999999996, 319.118, 327.538], [3, 199.92, 218.95999999999998, 333.432, 341.01], [3, 312.375, 317.72999999999996, 328.38, 335.95799999999997], [3, 318.91999999999996, 323.68, 336.8, 343.536], [3, 340.34, 344.505, 336.8, 343.536], [3, 362.35499999999996, 367.115, 336.8, 343.536], [3, 384.37, 389.13, 336.8, 343.536], [3, 406.97999999999996, 411.74, 336.8, 343.536], [3, 428.995, 433.755, 336.8, 343.536], [3, 452.2, 456.36499999999995, 336.8, 343.536], [3, 474.81, 478.97499999999997, 334.274, 341.01], [3, 497.41999999999996, 501.585, 334.274, 341.01], [3, 225.505, 260.015, 351.114, 362.06], [3, 287.97999999999996, 309.995, 351.114, 361.21799999999996], [3, 332.01, 359.97499999999997, 350.272, 360.376], [3, 386.75, 409.955, 349.43, 359.534], [3, 431.375, 459.935, 347.746, 357.84999999999997], [3, 476.0, 509.91499999999996, 346.062, 356.166], [3, 53.55, 101.74499999999999, 363.74399999999997, 374.69], [3, 271.32, 309.995, 362.06, 371.322], [3, 370.09, 409.955, 360.376, 369.638], [3, 53.55, 101.74499999999999, 374.69, 385.63599999999997], [3, 266.56, 309.995, 373.006, 382.268], [3, 365.925, 409.955, 371.322, 380.584], [3, 55.93, 93.41499999999999, 398.26599999999996, 405.844], [3, 194.565, 208.845, 396.582, 405.002], [3, 238.595, 261.205, 395.74, 404.15999999999997], [3, 288.575, 309.995, 394.89799999999997, 403.318], [3, 337.96, 359.97499999999997, 393.214, 401.63399999999996], [3, 387.94, 409.955, 392.372, 400.792], [3, 437.325, 459.935, 391.53, 399.95], [3, 487.9, 509.91499999999996, 389.846, 398.26599999999996], [3, 55.93, 75.565, 409.212, 416.78999999999996], [3, 194.565, 208.845, 407.52799999999996, 415.948], [3, 238.595, 261.205, 405.844, 414.264], [3, 288.575, 309.995, 405.002, 413.42199999999997], [3, 337.96, 359.97499999999997, 404.15999999999997, 412.58], [3, 387.94, 409.955, 403.318, 411.738], [3, 437.325, 459.935, 402.476, 410.89599999999996], [3, 487.9, 509.91499999999996, 400.792, 409.212], [3, 55.93, 86.27499999999999, 420.15799999999996, 427.736], [3, 194.565, 208.845, 418.474, 426.894], [3, 238.595, 261.205, 416.78999999999996, 425.21], [3, 288.575, 309.995, 415.948, 424.368], [3, 337.96, 359.97499999999997, 414.264, 422.68399999999997], [3, 387.94, 409.955, 413.42199999999997, 421.842], [3, 437.325, 459.935, 412.58, 421.0], [3, 487.9, 509.91499999999996, 410.89599999999996, 419.316], [3, 55.93, 123.16499999999999, 430.262, 437.84], [3, 194.565, 208.845, 428.578, 436.998], [3, 233.23999999999998, 261.205, 426.894, 435.31399999999996], [3, 283.815, 309.995, 426.05199999999996, 434.472], [3, 337.96, 359.97499999999997, 425.21, 433.63], [3, 383.775, 409.955, 424.368, 432.788], [3, 437.325, 459.935, 423.526, 431.94599999999997], [3, 487.9, 509.91499999999996, 421.842, 430.262], [3, 55.93, 141.60999999999999, 441.20799999999997, 448.786], [3, 194.565, 208.845, 439.524, 447.94399999999996], [3, 233.23999999999998, 261.205, 437.84, 446.26], [3, 283.815, 309.995, 436.998, 445.418], [3, 337.96, 359.97499999999997, 435.31399999999996, 443.734], [3, 383.775, 409.955, 434.472, 442.892], [3, 437.325, 459.935, 433.63, 442.05], [3, 487.9, 509.91499999999996, 431.94599999999997, 440.366], [3, 55.93, 75.565, 452.996, 460.574], [3, 183.855, 208.845, 450.46999999999997, 458.89], [3, 238.595, 261.205, 448.786, 457.20599999999996], [3, 288.575, 309.995, 447.94399999999996, 456.364], [3, 337.96, 359.97499999999997, 446.26, 454.68], [3, 387.94, 409.955, 445.418, 453.83799999999997], [3, 437.325, 459.935, 444.57599999999996, 452.996], [3, 487.9, 509.91499999999996, 442.892, 451.312], [3, 55.93, 93.41499999999999, 463.942, 471.52], [3, 183.855, 208.845, 461.416, 469.83599999999996], [3, 238.595, 261.205, 459.73199999999997, 468.152], [3, 288.575, 309.995, 458.89, 467.31], [3, 337.96, 359.97499999999997, 457.20599999999996, 465.626], [3, 387.94, 409.955, 456.364, 464.784], [3, 437.325, 459.935, 455.522, 463.942], [3, 487.9, 509.91499999999996, 453.83799999999997, 462.258], [3, 55.93, 93.41499999999999, 474.888, 482.466], [3, 183.855, 208.845, 472.36199999999997, 480.782], [3, 238.595, 261.205, 469.83599999999996, 478.256], [3, 288.575, 309.995, 468.99399999999997, 477.414], [3, 337.96, 359.97499999999997, 468.152, 476.572], [3, 387.94, 409.955, 467.31, 475.72999999999996], [3, 437.325, 459.935, 466.46799999999996, 474.888], [3, 487.9, 509.91499999999996, 464.784, 473.204], [3, 55.93, 93.41499999999999, 485.834, 493.412], [3, 183.855, 208.845, 483.308, 491.728], [3, 238.595, 261.205, 480.782, 489.202], [3, 288.575, 309.995, 479.94, 488.35999999999996], [3, 337.96, 359.97499999999997, 478.256, 486.676], [3, 387.94, 409.955, 477.414, 485.834], [4, 430.185, 536.095, 53.888, 65.676], [4, 216.57999999999998, 366.52, 66.518, 85.042], [4, 233.83499999999998, 353.43, 87.568, 101.88199999999999], [4, 266.56, 326.06, 106.092, 118.722], [4, 70.80499999999999, 98.175, 125.458, 135.56199999999998], [4, 70.80499999999999, 107.695, 134.72, 144.82399999999998], [4, 168.385, 174.33499999999998, 137.246, 145.666], [4, 70.80499999999999, 98.175, 143.982, 154.08599999999998], [4, 168.98, 179.69, 145.666, 154.928], [4, 70.80499999999999, 98.175, 154.08599999999998, 163.34799999999998], [4, 168.98, 202.29999999999998, 154.928, 164.19], [4, 70.80499999999999, 119.0, 163.34799999999998, 173.452], [4, 168.98, 202.29999999999998, 165.03199999999998, 174.29399999999998], [4, 70.80499999999999, 108.88499999999999, 173.452, 183.55599999999998], [4, 270.13, 296.905, 122.932, 133.036], [4, 270.13, 307.02, 132.194, 142.298], [4, 270.13, 297.5, 141.456, 151.56], [4, 270.13, 297.5, 151.56, 161.664], [4, 270.13, 318.325, 160.822, 170.926], [4, 229.075, 358.19, 185.23999999999998, 196.186], [4, 73.78, 116.61999999999999, 198.712, 208.816], [4, 73.78, 116.61999999999999, 208.816, 218.92], [4, 71.39999999999999, 359.38, 227.34, 236.602], [4, 71.39999999999999, 310.59, 236.602, 246.706], [4, 69.615, 359.38, 246.706, 255.968], [4, 69.615, 359.38, 255.968, 266.072], [4, 67.83, 359.38, 266.072, 275.334], [4, 66.64, 359.38, 275.334, 285.438], [4, 66.045, 359.38, 285.438, 295.542], [4, 66.045, 359.38, 295.542, 305.646], [4, 66.045, 359.38, 305.646, 314.908], [4, 66.045, 359.38, 314.908, 325.012], [4, 185.64, 359.38, 325.012, 335.116], [4, 66.045, 312.96999999999997, 346.062, 356.166], [4, 66.045, 359.38, 356.166, 366.27], [4, 66.045, 312.96999999999997, 366.27, 376.37399999999997], [4, 66.045, 312.96999999999997, 376.37399999999997, 386.478], [4, 66.045, 312.96999999999997, 386.478, 396.582], [4, 69.615, 312.96999999999997, 396.582, 406.686], [4, 70.80499999999999, 355.81, 418.474, 428.578], [4, 70.80499999999999, 355.81, 428.578, 438.68199999999996], [4, 70.80499999999999, 355.81, 438.68199999999996, 448.786], [4, 70.80499999999999, 355.81, 448.786, 458.89], [4, 70.80499999999999, 355.81, 458.89, 468.99399999999997], [4, 69.615, 355.81, 468.99399999999997, 479.09799999999996], [4, 69.615, 355.81, 479.09799999999996, 489.202], [4, 69.615, 312.96999999999997, 489.202, 499.306], [4, 69.615, 312.96999999999997, 499.306, 509.40999999999997], [4, 69.615, 365.33, 509.40999999999997, 519.514], [4, 69.615, 312.96999999999997, 519.514, 529.6179999999999], [4, 69.615, 312.96999999999997, 529.6179999999999, 539.722], [4, 69.615, 312.96999999999997, 539.722, 549.826], [4, 69.615, 312.96999999999997, 549.826, 559.93], [4, 69.615, 312.96999999999997, 559.93, 570.034], [4, 69.615, 312.96999999999997, 570.034, 580.138], [4, 69.615, 312.96999999999997, 580.138, 590.242], [4, 66.045, 312.96999999999997, 590.242, 600.346], [4, 66.045, 312.96999999999997, 600.346, 610.4499999999999], [4, 177.31, 365.33, 610.4499999999999, 620.554], [4, 66.045, 312.96999999999997, 620.554, 630.658], [4, 64.25999999999999, 312.96999999999997, 630.658, 640.762], [4, 64.25999999999999, 312.96999999999997, 640.762, 650.866], [4, 64.25999999999999, 129.71, 670.232, 687.914], [4, 62.474999999999994, 357.0, 685.3879999999999, 707.28], [4, 60.69, 184.45, 703.0699999999999, 724.12], [4, 60.69, 285.59999999999997, 714.016, 736.75], [4, 59.5, 418.28499999999997, 725.804, 751.064], [4, 59.5, 170.17, 747.696, 767.904], [4, 246.92499999999998, 401.625, 763.694, 786.428], [4, 406.385, 545.02, 762.01, 783.9019999999999], [4, 367.71, 379.60999999999996, 202.07999999999998, 208.816], [4, 382.585, 410.54999999999995, 198.712, 207.974], [4, 368.9, 395.08, 239.97, 246.706], [4, 369.495, 377.22999999999996, 254.284, 261.02], [4, 439.705, 471.835, 270.282, 277.018], [4, 371.28, 523.6, 284.596, 292.174], [4, 387.34499999999997, 418.28499999999997, 303.12, 310.698], [4, 465.885, 485.52, 303.12, 309.856], [4, 377.22999999999996, 384.965, 314.066, 319.96], [4, 380.205, 384.965, 330.906, 336.8], [4, 380.205, 384.965, 347.746, 353.64], [4, 418.88, 423.64, 353.64, 360.376], [4, 452.2, 456.96, 353.64, 360.376], [4, 485.52, 490.28, 353.64, 360.376], [4, 377.22999999999996, 384.965, 381.426, 387.32], [4, 467.075, 484.33, 389.00399999999996, 395.74], [4, 372.46999999999997, 409.35999999999996, 410.054, 416.78999999999996], [4, 382.585, 387.34499999999997, 418.474, 425.21], [4, 392.7, 397.46, 418.474, 425.21], [4, 401.625, 420.66499999999996, 421.0, 428.578], [4, 380.79999999999995, 387.34499999999997, 425.21, 431.94599999999997], [4, 380.79999999999995, 387.34499999999997, 431.94599999999997, 438.68199999999996], [4, 380.79999999999995, 387.34499999999997, 438.68199999999996, 445.418], [4, 380.79999999999995, 387.34499999999997, 445.418, 452.154], [4, 377.22999999999996, 387.34499999999997, 446.26, 452.996], [4, 392.7, 397.46, 438.68199999999996, 445.418], [4, 409.35999999999996, 430.185, 442.05, 448.786], [4, 393.89, 398.65, 458.89, 465.626], [4, 393.89, 398.65, 479.94, 486.676], [4, 395.08, 399.84, 500.99, 507.726], [4, 451.01, 476.0, 492.57, 500.14799999999997], [4, 401.625, 405.78999999999996, 508.568, 515.304], [4, 431.375, 436.135, 508.568, 515.304], [4, 462.315, 466.47999999999996, 508.568, 515.304], [4, 492.65999999999997, 497.41999999999996, 508.568, 515.304], [4, 523.005, 527.17, 508.568, 515.304], [4, 380.79999999999995, 384.965, 528.776, 535.512], [4, 389.72499999999997, 409.35999999999996, 531.302, 538.88], [4, 380.79999999999995, 384.965, 550.668, 557.404], [4, 380.79999999999995, 384.965, 572.56, 579.2959999999999], [4, 382.585, 387.34499999999997, 596.136, 602.872], [4, 382.585, 387.34499999999997, 619.712, 626.448], [4, 448.03499999999997, 473.62, 610.4499999999999, 618.87]]
2026-08-10 13:12:18,827 INFO     29 [qwen-vl-text] ═══ DONE ═══ 457 positions, pages=3, time=169.1s
2026-08-10 13:12:18,838 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 13:12:18,838 INFO     29 [Trace] task=90cba708 | doc=LTSH 三门峡.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items, types={'ExaminationReport': 1}", "html": "", "json": "492 items", "markdown": "", "text": "", "name": "LTSH 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:12:18,838 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 13:12:18,839 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:12:18.838+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 40, "failed": 0, "current": {"90cba70894bc11f1bd9827cf206dfa2d": {"id": "90cba70894bc11f1bd9827cf206dfa2d", "doc_id": "907f140694bc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LTSH \u4e09\u95e8\u5ce1.pdf", "type": "pdf", "location": "LTSH \u4e09\u95e8\u5ce1.pdf", "size": 6636575, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786367302926, "task_type": "dataflow", "root_trace_id": "3e86fc61695b452a8b4ef13e7466fe92", "root_traceparent": "00-3e86fc61695b452a8b4ef13e7466fe92-eb986cfdcd997396-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:12:18,844 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:12:18,845 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:12:19,760 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:12:19,769 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 13:12:19,769 INFO     29 [Trace] task=90cba708 | doc=LTSH 三门峡.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "492 items", "markdown": "", "text": "", "name": "LTSH 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 13:12:19,769 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 13:12:19,771 INFO     29 [ChunkMerger] Merged 2 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 7 noise chunks)
2026-08-10 13:12:19,781 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 13:12:19,781 INFO     29 [Trace] task=90cba708 | doc=LTSH 三门峡.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}", "name": "LTSH 三门峡.pdf"}
2026-08-10 13:12:19,781 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 13:12:19,825 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786367303758, 'update_date': datetime.datetime(2026, 8, 10, 13, 8, 23), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1025774, 'status': '1'}
2026-08-10 13:12:20,041 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=渑池县人民医院
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
FRCPleth
25/4/25
9:19:05上午
RW
PredAdt.0
0.2
0.4
0.6
0.8
1.0
Time [min]
Flow [L/s]
F/V ex
10
5
0
2
4
6
1
5
10
F/V in
Vol [L]
100
10
50
100
Time [s]
0
2
4
6
8
10
0
Volume [L]
4
2
0
1
2
4
Time [s]
10
20
30
40
0
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
80
100
2
VCmax
1
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
报告医师：
报告日期：2025.4.25
TLC
6 Vol [L]
FRCl eth
R
Time [min]
PredA@0 0.2 0.4 0.6 0.8 1.0
Flow [L/s]
F/V ex
10
5
0
2
4
6
10
F/V in
Vol%VCmax
0
0
Vol [L]
20
40
60
80
100
2
VCmax
4
6
8
Time [s]
8
4
Vol [L]
2
0
2
4
Time [s]
0
2
4
6
8
10
12
14
2026-08-10 13:12:20,342 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 13:12:20,342 INFO     29 [Trace] task=90cba708 | doc=LTSH 三门峡.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}", "name": "LTSH 三门峡.pdf", "embedding_token_consumption": 3064}
2026-08-10 13:12:20,342 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 13:12:20,459 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 13:12:20,459 INFO     29 [Trace] task=90cba708 | doc=LTSH 三门峡.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":2,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 13:12:20,461 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:12:20,461 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:12:20,465 INFO     29 set_progress(90cba70894bc11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 13:12:20 [DOC Engine]:
Start to index...
2026-08-10 13:12:20,479 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.010s]
2026-08-10 13:12:20,482 INFO     29 set_progress(90cba70894bc11f1bd9827cf206dfa2d), progress: 0.8500000000000001, progress_msg: 
2026-08-10 13:12:20,488 INFO     29 set_progress(90cba70894bc11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 13:12:20 Indexing done (0.02s). Task done (227.02s)
2026-08-10 13:12:20,491 INFO     29 [Done], chunks(2), token(3064), elapsed:227.02
2026-08-10 13:12:20,583 INFO     29 handle_task done for task {"id": "90cba70894bc11f1bd9827cf206dfa2d", "doc_id": "907f140694bc11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LTSH \u4e09\u95e8\u5ce1.pdf", "type": "pdf", "location": "LTSH \u4e09\u95e8\u5ce1.pdf", "size": 6636575, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786367302926, "task_type": "dataflow", "root_trace_id": "3e86fc61695b452a8b4ef13e7466fe92", "root_traceparent": "00-3e86fc61695b452a8b4ef13e7466fe92-eb986cfdcd997396-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
