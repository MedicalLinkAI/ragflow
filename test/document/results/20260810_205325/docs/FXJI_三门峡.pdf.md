# 基准结果：FXJI 三门峡.pdf

## 基本信息

- 文件：`FXJI 三门峡.pdf`
- 大小：7812.7 KB
- PDF 总页数：5
- doc_id：`7a7d42ec94ba11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T20:53:25  完成时间：2026-08-10T20:59:51  耗时：386.2s
- progress_msg：`12:59:49 Indexing done (0.04s). Task done (366.04s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 8bd151bd | 2 | 1-2 | 渑池县人民医院 门诊病历 姓名: 门诊号: 773264 就诊时间:2025-0 |
| 2 | b81cdf53 | 3 | 3-5 | JAEGER PCMED 渑池县人民医院 肺功能检查报告 舒张试验 姓名： 住院 |

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
  - `[no_text_noise] 2026-08-10 12:59:48,482 INFO     29 [ChunkMerger] Merged 2 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 12:53:26,989 INFO     29 handle_task begin for task {"id": "7ac5bf0e94ba11f1bd9827cf206dfa2d", "doc_id": "7a7d42ec94ba11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "FXJI \u4e09\u95e8\u5ce1.pdf", "type": "pdf", "location": "FXJI \u4e09\u95e8\u5ce1.pdf", "size": 8000159, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786366406983, "task_type": "dataflow", "root_trace_id": "bc9b9d974a834eb18f6171d96f843bf1", "root_traceparent": "00-bc9b9d974a834eb18f6171d96f843bf1-0c5099cebc4db2c7-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 12:53:27,472 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 12:53:27,586 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 12:53:27,600 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:53:27,600 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 12:53:27,600 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 12:53:27,609 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 12:53:27,610 INFO     29 ============================================================
2026-08-10 12:53:27,610 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 12:53:27,610 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 12:53:27,610 INFO     29 ============================================================
2026-08-10 12:53:27,610 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 12:53:27,610 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 12:53:27,612 INFO     29 No torch found.
2026-08-10 12:53:28,144 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=5
2026-08-10 12:53:28,430 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1572504, prompt_len=764
2026-08-10 12:53:29,929 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-05-27"}
```
2026-08-10 12:53:29,929 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=2025-05-27
2026-08-10 12:53:29,942 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1572504, prompt_len=401
2026-08-10 12:53:33,478 INFO     29 [qwen-vl-parser] text API response (len=569):
["渑池县人民医院", "门诊病历", "姓名:", "门诊号: 773264", "就诊时间:2025-05-27 09:30 科别: 呼吸与危重症医学科门诊", "姓名:范心静 性别:女 年龄:29岁 婚否:已婚", "职业:自由职业 工作单位:无", "联系电话: 住址:河南省三门峡市渑池县郭窑村15", "组", "病史叙述者:本人 身份证号", "过敏史:无", "主诉:咳嗽、咳痰、胸闷、气喘1周。", "现病史:患者于1周前受凉后出现咳嗽、咳痰、胸闷、气喘,痰为白", "色粘稠痰,咳出困难,夜间及清晨咳嗽明显,活动后胸闷、气喘,", "自行给予“喘息定片”药物治疗,症状无改善。", "既往史:平素身体良好;无特殊疾病史;否认“肝炎、结核”等病史;", "否认手术史;否认外伤史;否认输血史及献血史;否认药物及食", "物过敏史;无预防接种史", "流行病学史:无", "体格检查:体温36.5℃,脉搏78次/分,呼吸20次/分,", "血压120/80mmHg,双肺呼吸音粗,可闻及哮鸣音,心率78", "次/分,律齐,未闻及病理性杂音。", "辅助检查:肺功能四项+支气管舒张实验:沙丁胺醇气雾剂支气管舒", "张实验呈阳性,FEV1.0改善17.1%。", "初步诊断:门诊诊断:1.支气管哮喘。", "-1-"]
2026-08-10 12:53:33,479 INFO     29 [qwen-vl-parser] page=1 text: 26 lines (bbox 0-25)
2026-08-10 12:53:33,479 INFO     29 [qwen-vl-parser] page=1 text: 26 sections
2026-08-10 12:53:33,701 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1025274, prompt_len=764
2026-08-10 12:53:34,982 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 12:53:34,983 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 12:53:34,999 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1025274, prompt_len=401
2026-08-10 12:53:35,915 INFO     29 [qwen-vl-parser] text API response (len=118):
["渑池县人民医院", "门诊病历", "姓名：", "门诊号：", "处理意见：1.注意避免受凉，避免接触刺激性气味，避免接触花粉等", "诱发急性发作；2.如有不适，及时就诊。", "经治医师：", "Ehun", "- 2 -"]
2026-08-10 12:53:35,915 INFO     29 [qwen-vl-parser] page=2 text: 9 lines (bbox 26-34)
2026-08-10 12:53:35,915 INFO     29 [qwen-vl-parser] page=2 text: 9 sections
2026-08-10 12:53:36,294 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2031579, prompt_len=764
2026-08-10 12:53:39,240 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2025-05-27"
}
```
2026-08-10 12:53:39,241 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=2025-05-27
2026-08-10 12:53:39,257 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2031579, prompt_len=401
2026-08-10 12:53:44,578 INFO     29 [qwen-vl-parser] text API response (len=1030):
["JAEGER PCMED", "渑池县人民医院", "肺功能检查报告", "舒张试验", "姓名：", "住院号：", "性别：女", "身高：154 cm", "标准体重：125 %", "吸烟史：", "科别：", "测试号：2025052701", "年龄：29 Years", "体重：67.5 kg", "体表面积：1.66 m", "Flow [L/s]", "F/V ex", "Vol%VCmax", "Vol [L]", "VCmax", "Time [s]", "F/V in", "测试日期", "测试时间", "预计值", "前次", "前/预", "后次", "后/预", "改善率", "25/5/27", "25/5/27", "10:10:05", "10:32:25", "VC MAX", "[L]", "3.20", "2.87", "89.6", "3.38", "105.6", "17.9", "FVC", "[L]", "3.18", "2.79", "87.6", "3.37", "106.0", "20.9", "FEV 1", "[L]", "2.76", "1.57", "57.0", "1.84", "66.7", "17.1", "FEV 1 % FVC", "[%]", "84.23", "56.40", "67.0", "54.61", "64.8", "-3.2", "FEV 1 % VC MAX", "[%]", "83.59", "54.79", "65.5", "54.42", "65.1", "-0.7", "PEF", "[L/s]", "6.49", "3.62", "55.8", "4.32", "66.5", "19.2", "MEF 75", "[L/s]", "5.83", "2.32", "39.8", "2.52", "43.2", "8.5", "MEF 50", "[L/s]", "4.21", "0.76", "18.0", "0.91", "21.6", "20.5", "MEF 25", "[L/s]", "2.00", "0.23", "11.6", "0.24", "12.0", "3.0", "MMEF 75/25", "[L/s]", "3.86", "0.58", "14.9", "0.67", "17.3", "16.2"]
2026-08-10 12:53:44,579 INFO     29 [qwen-vl-parser] page=3 text: 114 lines (bbox 35-148)
2026-08-10 12:53:44,579 INFO     29 [qwen-vl-parser] page=3 text: 114 sections
2026-08-10 12:53:44,983 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2302998, prompt_len=764
2026-08-10 12:53:46,364 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 12:53:46,364 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-10 12:53:46,377 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2302998, prompt_len=401
2026-08-10 12:53:48,050 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:53:48.049+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 35, "failed": 0, "current": {"7ac5bf0e94ba11f1bd9827cf206dfa2d": {"id": "7ac5bf0e94ba11f1bd9827cf206dfa2d", "doc_id": "7a7d42ec94ba11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "FXJI \u4e09\u95e8\u5ce1.pdf", "type": "pdf", "location": "FXJI \u4e09\u95e8\u5ce1.pdf", "size": 8000159, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786366406983, "task_type": "dataflow", "root_trace_id": "bc9b9d974a834eb18f6171d96f843bf1", "root_traceparent": "00-bc9b9d974a834eb18f6171d96f843bf1-0c5099cebc4db2c7-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:54:19,378 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:54:19.375+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 35, "failed": 0, "current": {"7ac5bf0e94ba11f1bd9827cf206dfa2d": {"id": "7ac5bf0e94ba11f1bd9827cf206dfa2d", "doc_id": "7a7d42ec94ba11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "FXJI \u4e09\u95e8\u5ce1.pdf", "type": "pdf", "location": "FXJI \u4e09\u95e8\u5ce1.pdf", "size": 8000159, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786366406983, "task_type": "dataflow", "root_trace_id": "bc9b9d974a834eb18f6171d96f843bf1", "root_traceparent": "00-bc9b9d974a834eb18f6171d96f843bf1-0c5099cebc4db2c7-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:54:50,792 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:54:50.790+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 35, "failed": 0, "current": {"7ac5bf0e94ba11f1bd9827cf206dfa2d": {"id": "7ac5bf0e94ba11f1bd9827cf206dfa2d", "doc_id": "7a7d42ec94ba11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "FXJI \u4e09\u95e8\u5ce1.pdf", "type": "pdf", "location": "FXJI \u4e09\u95e8\u5ce1.pdf", "size": 8000159, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786366406983, "task_type": "dataflow", "root_trace_id": "bc9b9d974a834eb18f6171d96f843bf1", "root_traceparent": "00-bc9b9d974a834eb18f6171d96f843bf1-0c5099cebc4db2c7-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:55:21,357 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:55:21.357+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 35, "failed": 0, "current": {"7ac5bf0e94ba11f1bd9827cf206dfa2d": {"id": "7ac5bf0e94ba11f1bd9827cf206dfa2d", "doc_id": "7a7d42ec94ba11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "FXJI \u4e09\u95e8\u5ce1.pdf", "type": "pdf", "location": "FXJI \u4e09\u95e8\u5ce1.pdf", "size": 8000159, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786366406983, "task_type": "dataflow", "root_trace_id": "bc9b9d974a834eb18f6171d96f843bf1", "root_traceparent": "00-bc9b9d974a834eb18f6171d96f843bf1-0c5099cebc4db2c7-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:55:53,444 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:55:53.441+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 35, "failed": 0, "current": {"7ac5bf0e94ba11f1bd9827cf206dfa2d": {"id": "7ac5bf0e94ba11f1bd9827cf206dfa2d", "doc_id": "7a7d42ec94ba11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "FXJI \u4e09\u95e8\u5ce1.pdf", "type": "pdf", "location": "FXJI \u4e09\u95e8\u5ce1.pdf", "size": 8000159, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786366406983, "task_type": "dataflow", "root_trace_id": "bc9b9d974a834eb18f6171d96f843bf1", "root_traceparent": "00-bc9b9d974a834eb18f6171d96f843bf1-0c5099cebc4db2c7-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:55:55,746 INFO     29 [qwen-vl-parser] text API response (len=24730):
["JAEGER PCMED", "渑池县人民医院", "肺功能检查报告", "综合测试", "姓名：", "性别：女", "年龄：29 Years", "身高：154 cm", "体重：67.5 kg", "备注：", "联系电话：", "住院号：0", "测试号：2025052701", "吸烟史：", "既往史：", "职业：", "测试日期", "测试时间", "预计值", "实测值", "实/预", "VC MAX", "[L]", "3.20", "2.87", "89.6", "FVC", "[L]", "3.18", "2.79", "87.6", "MV", "[L/min]", "9.64", "25.12", "260.5", "FEV 1", "[L]", "2.76", "1.57", "57.0", "FEV 1 % FVC", "[%]", "84.23", "56.40", "67.0", "PEF", "[L/s]", "6.49", "3.62", "55.8", "MEF 75", "[L/s]", "5.83", "2.32", "39.8", "MEF 50", "[L/s]", "4.21", "0.76", "18.0", "MEF 25", "[L/s]", "2.00", "0.23", "11.6", "MMEF 75/25", "[L/s]", "3.86", "0.58", "14.9", "MVV", "[L/min]", "105.09", "71.84", "68.4", "TLC-SB", "[L]", "4.37", "4.10", "93.8", "RV-SB", "[L]", "1.25", "1.38", "110.4", "RV%TLC-SB", "[%]", "28.82", "33.70", "116.9", "FRC-SB", "[L]", "2.48", "2.31", "93.1", "FRC%TLC-SB", "[%]", "49.74", "56.25", "113.1", "DLCO SB [mmol/min/kPa]", "8.44", "6.84", "81.0", "DLCO/VAmmol/min/kPa/L]", "1.93", "1.73", "89.7", "Hb", "[g/100ml]", "13.40", "VA", "[L]", "4.22", "3.95", "93.6", "DLCOc SB[mmol/min/kPa]", "8.44", "6.84", "81.0", "DLCOc/VAmmol/min/kPa/L]", "1.93", "1.73", "89.7", "VIN", "[L]", "3.20", "2.72", "85.0", "Insp. time", "[s]", "0.95", "Exp. time", "[s]", "1.95", "Sample vol", "[L]", "System dead space [ml]", "172.00", "Anatom. dead space[ml]", "148.50", "TA", "[s]", "11.32", "测试结果：", "Vol [L]", "Time [min]", "PredAdj.0", "0.2", "0.4", "0.6", "0.8", "1.0", "Flow [L/s]", "F/V ex", "10", "5", "0", "2", "4", "6", "5", "10", "F/V in", "Vol [L]", "100", "50", "0", "Time [s]", "10", "15", "Volume [L]", "4", "2", "0", "4", "10", "20", "30", "40", "Time [s]", "25/5/27", "10:10:05上", "FRCP&th", "RV", "Vol [L]", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10
2026-08-10 12:55:55,767 INFO     29 [qwen-vl-parser] page=4 text: 4025 lines (bbox 149-4173)
2026-08-10 12:55:55,767 INFO     29 [qwen-vl-parser] page=4 text: 4025 sections
2026-08-10 12:55:56,162 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2441908, prompt_len=764
2026-08-10 12:55:57,632 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 12:55:57,633 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 12:55:57,648 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2441908, prompt_len=401
2026-08-10 12:56:06,895 INFO     29 [qwen-vl-parser] text API response (len=1748):
["JAEGER PCMED", "渑池县人民医院", "肺功能检查报告", "常规通气", "姓名：", "住院号：0", "性别：女", "身高：154 cm", "标准体重：125 %", "吸烟史：", "科别：", "测试号：2025052701", "年龄：29 Years", "体重：67.5 kg", "体表面积：1.66 m", "测试日期 25/5/27", "测试时间 10:10:05", "预计值 实测值 实测/预", "VC MAX [L] 3.20 2.87 89.6", "IRV [L] 1.14", "ERV [L] 1.23 0.92 75.3", "IC [L] 1.97 1.94 98.4", "VT [L] 0.48 0.80 166.0", "MV [L/min] 9.64 25.12 260.5", "VC IN [L] 3.20 2.87 89.6", "VC EX [L] 3.20 2.82 88.0", "BF [1/min] 20.00 31.39 157.0", "FVC [L] 3.18 2.79 87.6", "PEF [L/s] 6.49 3.62 55.8", "FEV 0.5 [L] 1.15", "FEV 1 [L] 2.76 1.57 57.0", "FEV 2 [L] 1.98", "FEV 3 [L] 2.21", "FEV6 [L] 2.61", "FEF 200-1200 [L/s] 2.06", "FEV 1 % FVC [%] 84.23 56.40 67.0", "FEV 1 % VC MAX [%] 83.59 54.79 65.5", "MEF 75 [L/s] 5.83 2.32 39.8", "MEF 50 [L/s] 4.21 0.76 18.0", "MEF 25 [L/s] 2.00 0.23 11.6", "MMEF 75/25 [L/s] 3.86 0.58 14.9", "FEF 75/85 [L/s] 1.22 0.16 13.3", "FEF50 % FIF50 [%] 19.86", "PIF [L/s] 4.32", "FVC IN [L] 3.20 2.72 84.9", "FET [s] 8.39", "FIF 50 [L/s] 3.80", "FIV1 [L] 2.68", "FIV1 % FVC [%] 98.67", "T IN [s] 0.84", "T EX [s] 1.07", "T TOT [s] 1.91", "MIF [L/s] 0.95", "MEF [L/s] 0.75", "MVV [L/min] 105.09 71.84 68.4", "FEF50 % FIF50 [%] 19.86", "V backextrapolation ex [L] 0.04", "V backextrapol. % FVC [%] 1.50", "测试结果", "1、中重度阻塞性肺通气功能障碍，小气道功能降低。", "2、肺弥散功能正常。", "3、残气量、残气量/肺总量正常。", "4、沙丁胺醇气雾剂支气管舒张试验呈阳性，FEV1.0改善17.1%。", "5、建议定期复查。", "报告医师：李朝红/王晓红 报告日期：2025.5.27", "6 Vol [L]", "TLC 4", "FRCPth", "RV", "PredAdt.0 0.2 0.4 0.6 0.8 1.0", "Time [min]", "Flow [L/s]", "F/V ex", "10", "5", "0", "2", "4", "6", "10", "5", "10", "F/V in", "Vol%VCmax", "0", "20", "40", "60", "80", "100", "Vol [L]", "2", "VCmax", "4", "6", "8", "Time [s]", "4", "Vol [L]", "2", "0", "2", "4", "6", "8", "10", "12", "14", "Time [s]"]
2026-08-10 12:56:06,895 INFO     29 [qwen-vl-parser] page=5 text: 109 lines (bbox 4174-4282)
2026-08-10 12:56:06,895 INFO     29 [qwen-vl-parser] page=5 text: 109 sections
2026-08-10 12:56:06,895 INFO     29 [qwen-vl-parser] parse_pdf done: 4283 sections from 5 pages.
2026-08-10 12:56:06,904 INFO     29 Close text detector.
2026-08-10 12:56:07,313 INFO     29 Close text recognizer.
2026-08-10 12:56:07,725 INFO     29 Close recognizer.
2026-08-10 12:56:08,187 INFO     29 Close recognizer.
2026-08-10 12:56:08,715 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 12:56:08,715 INFO     29 [Trace] task=7ac5bf0e | doc=FXJI 三门峡.pdf | Parser:MedLink | outputs={"html": "", "json": "4283 items", "markdown": "", "text": "", "name": "FXJI 三门峡.pdf", "output_format": "json"}
2026-08-10 12:56:08,716 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 12:56:08,737 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:56:08,738 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 渑池县人民医院\n[BBOX-1] 门诊病历\n[BBOX-2] 姓名:\n[BBOX-3] 门诊号: 773264\n[BBOX-4] 就诊时间:2025-05-27 09:30 科别: 呼吸与危重症医学科门诊\n[BBOX-5] 姓名:范心静 性别:女 年龄:29岁 婚否:已婚\n[BBOX-6] 职业:自由职业 工作单位:无\n[BBOX-7] 联系电话: 住址:河南省三门峡市渑池县郭窑村15\n[BBOX-8] 组\n[BBOX-9] 病史叙述者:本人 身份证号\n[BBOX-10] 过敏史:无\n[BBOX-11] 主诉:咳嗽、咳痰、胸闷、气喘1周。\n[BBOX-12] 现病史:患者于1周前受凉后出现咳嗽、咳痰、胸闷、气喘,痰为白\n[BBOX-13] 色粘稠痰,咳出困难,夜间及清晨咳嗽明显,活动后胸闷、气喘,\n[BBOX-14] 自行给予“喘息定片”药物治疗,症状无改善。\n[BBOX-15] 既往史:平素身体良好;无特殊疾病史;否认“肝炎、结核”等病史;\n[BBOX-16] 否认手术史;否认外伤史;否认输血史及献血史;否认药物及食\n[BBOX-17] 物过敏史;无预防接种史\n[BBOX-18] 流行病学史:无\n[BBOX-19] 体格检查:体温36.5℃,脉搏78次/分,呼吸20次/分,\n[BBOX-20] 血压120/80mmHg,双肺呼吸音粗,可闻及哮鸣音,心率78\n[BBOX-21] 次/分,律齐,未闻及病理性杂音。\n[BBOX-22] 辅助检查:肺功能四项+支气管舒张实验:沙丁胺醇气雾剂支气管舒\n[BBOX-23] 张实验呈阳性,FEV1.0改善17.1%。\n[BBOX-24] 初步诊断:门诊诊断:1.支气管哮喘。\n[BBOX-25] -1-\n[BBOX-26] 渑池县人民医院\n[BBOX-27] 门诊病历\n[BBOX-28] 姓名：\n[BBOX-29] 门诊号：\n[BBOX-30] 处理意见：1.注意避免受凉，避免接触刺激性气味，避免接触花粉等\n[BBOX-31] 诱发急性发作；2.如有不适，及时就诊。\n[BBOX-32] 经治医师：\n[BBOX-33] Ehun\n[BBOX-34] - 2 -\n[BBOX-35] JAEGER PCMED\n[BBOX-36] 渑池县人民医院\n[BBOX-37] 肺功能检查报告\n[BBOX-38] 舒张试验\n[BBOX-39] 姓名：\n[BBOX-40] 住院号：\n[BBOX-41] 性别：女\n[BBOX-42] 身高：154 cm\n[BBOX-43] 标准体重：125 %\n[BBOX-44] 吸烟史：\n[BBOX-45] 科别：\n[BBOX-46] 测试号：2025052701\n[BBOX-47] 年龄：29 Years\n[BBOX-48] 体重：67.5 kg\n[BBOX-49] 体表面积：1.66 m\n[BBOX-50] Flow [L/s]\n[BBOX-51] F/V ex\n[BBOX-52] Vol%VCmax\n[BBOX-53] Vol [L]\n[BBOX-54] VCmax\n[BBOX-55] Time [s]\n[BBOX-56] F/V in\n[BBOX-57] 测试日期\n[BBOX-58] 测试时间\n[BBOX-59] 预计值\n[BBOX-60] 前次\n[BBOX-61] 前/预\n[BBOX-62] 后次\n[BBOX-63] 后/预\n[BBOX-64] 改善率\n[BBOX-65] 25/5/27\n[BBOX-66] 25/5/27\n[BBOX-67] 10:10:05\n[BBOX-68] 10:32:25\n[BBOX-69] VC MAX\n[BBOX-70] [L]\n[BBOX-71] 3.20\n[BBOX-72] 2.87\n[BBOX-73] 89.6\n[BBOX-74] 3.38\n[BBOX-75] 105.6\n[BBOX-76] 17.9\n[BBOX-77] FVC\n[BBOX-78] [L]\n[BBOX-79] 3.18\n[BBOX-80] 2.79\n[BBOX-81] 87.6\n[BBOX-82] 3.37\n[BBOX-83] 106.0\n[BBOX-84] 20.9\n[BBOX-85] FEV 1\n[BBOX-86] [L]\n[BBOX-87] 2.76\n[BBOX-88] 1.57\n[BBOX-89] 57.0\n[BBOX-90] 1.84\n[BBOX-91] 66.7\n[BBOX-92] 17.1\n[BBOX-93] FEV 1 % FVC\n[BBOX-94] [%]\n[BBOX-95] 84.23\n[BBOX-96] 56.40\n[BBOX-97] 67.0\n[BBOX-98] 54.61\n[BBOX-99] 64.8\n[BBOX-100] -3.2\n[BBOX-101] FEV 1 % VC MAX\n[BBOX-102] [%]\n[BBOX-103] 83.59\n[BBOX-104] 54.79\n[BBOX-105] 65.5\n[BBOX-106] 54.42\n[BBOX-107] 65.1\n[BBOX-108] -0.7\n[BBOX-109] PEF\n[BBOX-110] [L/s]\n[BBOX-111] 6.49\n[BBOX-112] 3.62\n[BBOX-113] 55.8\n[BBOX-114] 4.32\n[BBOX-115] 66.5\n[BBOX-116] 19.2\n[BBOX-117] MEF 75\n[BBOX-118] [L/s]\n[BBOX-119] 5.83\n[BBOX-120] 2.32\n[BBOX-121] 39.8\n[BBOX-122] 2.52\n[BBOX-123] 43.2\n[BBOX-124] 8.5\n[BBOX-125] MEF 50\n[BBOX-126] [L/s]\n[BBOX-127] 4.21\n[BBOX-128] 0.76\n[BBOX-129] 18.0\n[BBOX-130] 0.91\n[BBOX-131] 21.6\n[BBOX-132] 20.5\n[BBOX-133] MEF 25\n[BBOX-134] [L/s]\n[BBOX-135] 2.00\n[BBOX-136] 0.23\n[BBOX-137] 11.6\n[BBOX-138] 0.24\n[BBOX-139] 12.0\n[BBOX-140] 3.0\n[BBOX-141] MMEF 75/25\n[BBOX-142] [L/s]\n[BBOX-143] 3.86\n[BBOX-144] 0.58\n[BBOX-145] 14.9\n[BBOX-146] 0.67\n[BBOX-147] 17.3\n[BBOX-148] 16.2\n[BBOX-149] JAEGER PCMED\n[BBOX-150] 渑池县人民医院\n[BBOX-151] 肺功能检查报告\n[BBOX-152] 综合测试\n[BBOX-153] 姓名：\n[BBOX-154] 性别：女\n[BBOX-155] 年龄：29 Years\n[BBOX-156] 身高：154 cm\n[BBOX-157] 体重：67.5 kg\n[BBOX-158] 备注：\n[BBOX-159] 联系电话：\n[BBOX-160] 住院号：0\n[BBOX-161] 测试号：2025052701\n[BBOX-162] 吸烟史：\n[BBOX-163] 既往史：\n[BBOX-164] 职业：\n[BBOX-165] 测试日期\n[BBOX-166] 测试时间\n[BBOX-167] 预计值\n[BBOX-168] 实测值\n[BBOX-169] 实/预\n[BBOX-170] VC MAX\n[BBOX-171] [L]\n[BBOX-172] 3.20\n[BBOX-173] 2.87\n[BBOX-174] 89.6\n[BBOX-175] FVC\n[BBOX-176] [L]\n[BBOX-177] 3.18\n[BBOX-178] 2.79\n[BBOX-179] 87.6\n[BBOX-180] MV\n[BBOX-181] [L/min]\n[BBOX-182] 9.64\n[BBOX-183] 25.12\n[BBOX-184] 260.5\n[BBOX-185] FEV 1\n[BBOX-186] [L]\n[BBOX-187] 2.76\n[BBOX-188] 1.57\n[BBOX-189] 57.0\n[BBOX-190] FEV 1 % FVC\n[BBOX-191] [%]\n[BBOX-192] 84.23\n[BBOX-193] 56.40\n[BBOX-194] 67.0\n[BBOX-195] PEF\n[BBOX-196] [L/s]\n[BBOX-197] 6.49\n[BBOX-198] 3.62\n[BBOX-199] 55.8\n[BBOX-200] MEF 75\n[BBOX-201] [L/s]\n[BBOX-202] 5.83\n[BBOX-203] 2.32\n[BBOX-204] 39.8\n[BBOX-205] MEF 50\n[BBOX-206] [L/s]\n[BBOX-207] 4.21\n[BBOX-208] 0.76\n[BBOX-209] 18.0\n[BBOX-210] MEF 25\n[BBOX-211] [L/s]\n[BBOX-212] 2.00\n[BBOX-213] 0.23\n[BBOX-214] 11.6\n[BBOX-215] MMEF 75/25\n[BBOX-216] [L/s]\n[BBOX-217] 3.86\n[BBOX-218] 0.58\n[BBOX-219] 14.9\n[BBOX-220] MVV\n[BBOX-221] [L/min]\n[BBOX-222] 105.09\n[BBOX-223] 71.84\n[BBOX-224] 68.4\n[BBOX-225] TLC-SB\n[BBOX-226] [L]\n[BBOX-227] 4.37\n[BBOX-228] 4.10\n[BBOX-229] 93.8\n[BBOX-230] RV-SB\n[BBOX-231] [L]\n[BBOX-232] 1.25\n[BBOX-233] 1.38\n[BBOX-234] 110.4\n[BBOX-235] RV%TLC-SB\n[BBOX-236] [%]\n[BBOX-237] 28.82\n[BBOX-238] 33.70\n[BBOX-239] 116.9\n[BBOX-240] FRC-SB\n[BBOX-241] [L]\n[BBOX-242] 2.48\n[BBOX-243] 2.31\n[BBOX-244] 93.1\n[BBOX-245] FRC%TLC-SB\n[BBOX-246] [%]\n[BBOX-247] 49.74\n[BBOX-248] 56.25\n[BBOX-249] 113.1\n[BBOX-250] DLCO SB [mmol/min/kPa]\n[BBOX-251] 8.44\n[BBOX-252] 6.84\n[BBOX-253] 81.0\n[BBOX-254] DLCO/VAmmol/min/kPa/L]\n[BBOX-255] 1.93\n[BBOX-256] 1.73\n[BBOX-257] 89.7\n[BBOX-258] Hb\n[BBOX-259] [g/100ml]\n[BBOX-260] 13.40\n[BBOX-261] VA\n[BBOX-262] [L]\n[BBOX-263] 4.22\n[BBOX-264] 3.95\n[BBOX-265] 93.6\n[BBOX-266] DLCOc SB[mmol/min/kPa]\n[BBOX-267] 8.44\n[BBOX-268] 6.84\n[BBOX-269] 81.0\n[BBOX-270] DLCOc/VAmmol/min/kPa/L]\n[BBOX-271] 1.93\n[BBOX-272] 1.73\n[BBOX-273] 89.7\n[BBOX-274] VIN\n[BBOX-275] [L]\n[BBOX-276] 3.20\n[BBOX-277] 2.72\n[BBOX-278] 85.0\n[BBOX-279] Insp. time\n[BBOX-280] [s]\n[BBOX-281] 0.95\n[BBOX-282] Exp. time\n[BBOX-283] [s]\n[BBOX-284] 1.95\n[BBOX-285] Sample vol\n[BBOX-286] [L]\n[BBOX-287] System dead space [ml]\n[BBOX-288] 172.00\n[BBOX-289] Anatom. dead space[ml]\n[BBOX-290] 148.50\n[BBOX-291] TA\n[BBOX-292] [s]\n[BBOX-293] 11.32\n[BBOX-294] 测试结果：\n[BBOX-295] Vol [L]\n[BBOX-296] Time [min]\n[BBOX-297] PredAdj.0\n[BBOX-298] 0.2\n[BBOX-299] 0.4\n[BBOX-300] 0.6\n[BBOX-301] 0.8\n[BBOX-302] 1.0\n[BBOX-303] Flow [L/s]\n[BBOX-304] F/V ex\n[BBOX-305] 10\n[BBOX-306] 5\n[BBOX-307] 0\n[BBOX-308] 2\n[BBOX-309] 4\n[BBOX-310] 6\n[BBOX-311] 5\n[BBOX-312] 10\n[BBOX-313] F/V in\n[BBOX-314] Vol [L]\n[BBOX-315] 100\n[BBOX-316] 50\n[BBOX-317] 0\n[BBOX-318] Time [s]\n[BBOX-319] 10\n[BBOX-320] 15\n[BBOX-321] Volume [L]\n[BBOX-322] 4\n[BBOX-323] 2\n[BBOX-324] 0\n[BBOX-325] 4\n[BBOX-326] 10\n[BBOX-327] 20\n[BBOX-328] 30\n[BBOX-329] 40\n[BBOX-330] Time [s]\n[BBOX-331] 25/5/27\n[BBOX-332] 10:10:05上\n[BBOX-333] FRCP&th\n[BBOX-334] RV\n[BBOX-335] Vol [L]\n[BBOX-336] 10\n[BBOX-337] 10\n[BBOX-338] 10\n[BBOX-339] 10\n[BBOX-340] 10\n[BBOX-341] 10\n[BBOX-342] 10\n[BBOX-343] 10\n[BBOX-344] 10\n[BBOX-345] 10\n[BBOX-346] 10\n[BBOX-347] 10\n[BBOX-348] 10\n[BBOX-349] 10\n[BBOX-350] 10\n[BBOX-351] 10\n[BBOX-352] 10\n[BBOX-353] 10\n[BBOX-354] 10\n[BBOX-355] 10\n[BBOX-356] 10\n[BBOX-357] 10\n[BBOX-358] 10\n[BBOX-359] 10\n[BBOX-360] 10\n[BBOX-361] 10\n[BBOX-362] 10\n[BBOX-363] 10\n[BBOX-364] 10\n[BBOX-365] 10\n[BBOX-366] 10\n[BBOX-367] 10\n[BBOX-368] 10\n[BBOX-369] 10\n[BBOX-370] 10\n[BBOX-371] 10\n[BBOX-372] 10\n[BBOX-373] 10\n[BBOX-374] 10\n[BBOX-375] 10\n[BBOX-376] 10\n[BBOX-377] 10\n[BBOX-378] 10\n[BBOX-379] 10\n[BBOX-380] 10\n[BBOX-381] 10\n[BBOX-382] 10\n[BBOX-383] 10\n[BBOX-384] 10\n[BBOX-385] 10\n[BBOX-386] 10\n[BBOX-387] 10\n[BBOX-388] 10\n[BBOX-389] 10\n[BBOX-390] 10\n[BBOX-391] 10\n[BBOX-392] 10\n[BBOX-393] 10\n[BBOX-394] 10\n[BBOX-395] 10\n[BBOX-396] 10\n[BBOX-397] 10\n[BBOX-398] 10\n[BBOX-399] 10\n[BBOX-400] 10\n[BBOX-401] 10\n[BBOX-402] 10\n[BBOX-403] 10\n[BBOX-404] 10\n[BBOX-405] 10\n[BBOX-406] 10\n[BBOX-407] 10\n[BBOX-408] 10\n[BBOX-409] 10\n[BBOX-410] 10\n[BBOX-411] 10\n[BBOX-412] 10\n[BBOX-413] 10\n[BBOX-414] 10\n[BBOX-415] 10\n[BBOX-416] 10\n[BBOX-417] 10\n[BBOX-418] 10\n[BBOX-419] 10\n[BBOX-420] 10\n[BBOX-421] 10\n[BBOX-422] 10\n[BBOX-423] 10\n[BBOX-424] 10\n[BBOX-425] 10\n[BBOX-426] 10\n[BBOX-427] 10\n[BBOX-428] 10\n[BBOX-429] 10\n[BBOX-430] 10\n[BBOX-431] 10\n[BBOX-432] 10\n[BBOX-433] 10\n[BBOX-434] 10\n[BBOX-435] 10\n[BBOX-436] 10\n[BBOX-437] 10\n[BBOX-438] 10\n[BBOX-439] 10\n[BBOX-440] 10\n[BBOX-441] 10\n[BBOX-442] 10\n[BBOX-443] 10\n[BBOX-444] 10\n[BBOX-445] 10\n[BBOX-446] 10\n[BBOX-447] 10\n[BBOX-448] 10\n[BBOX-449] 10\n[BBOX-450] 10\n[BBOX-451] 10\n[BBOX-452] 10\n[BBOX-453] 10\n[BBOX-454] 10\n[BBOX-455] 10\n[BBOX-456] 10\n[BBOX-457] 10\n[BBOX-458] 10\n[BBOX-459] 10\n[BBOX-460] 10\n[BBOX-461] 10\n[BBOX-462] 10\n[BBOX-463] 10\n[BBOX-464] 10\n[BBOX-465] 10\n[BBOX-466] 10\n[BBOX-467] 10\n[BBOX-468] 10\n[BBOX-469] 10\n[BBOX-470] 10\n[BBOX-471] 10\n[BBOX-472] 10\n[BBOX-473] 10\n[BBOX-474] 10\n[BBOX-475] 10\n[BBOX-476] 10\n[BBOX-477] 10\n[BBOX-478] 10\n[BBOX-479] 10\n[BBOX-480] 10\n[BBOX-481] 10\n[BBOX-482] 10\n[BBOX-483] 10\n[BBOX-484] 10\n[BBOX-485] 10\n[BBOX-486] 10\n[BBOX-487] 10\n[BBOX-488] 10\n[BBOX-489] 10\n[BBOX-490] 10\n[BBOX-491] 10\n[BBOX-492] 10\n[BBOX-493] 10\n[BBOX-494] 10\n[BBOX-495] 10\n[BBOX-496] 10\n[BBOX-497] 10\n[BBOX-498] 10\n[BBOX-499] 10\n[BBOX-500] 10\n[BBOX-501] 10\n[BBOX-502] 10\n[BBOX-503] 10\n[BBOX-504] 10\n[BBOX-505] 10\n[BBOX-506] 10\n[BBOX-507] 10\n[BBOX-508] 10\n[BBOX-509] 10\n[BBOX-510] 10\n[BBOX-511] 10\n[BBOX-512] 10\n[BBOX-513] 10\n[BBOX-514] 10\n[BBOX-515] 10\n[BBOX-516] 10\n[BBOX-517] 10\n[BBOX-518] 10\n[BBOX-519] 10\n[BBOX-520] 10\n[BBOX-521] 10\n[BBOX-522] 10\n[BBOX-523] 10\n[BBOX-524] 10\n[BBOX-525] 10\n[BBOX-526] 10\n[BBOX-527] 10\n[BBOX-528] 10\n[BBOX-529] 10\n[BBOX-530] 10\n[BBOX-531] 10\n[BBOX-532] 10\n[BBOX-533] 10\n[BBOX-534] 10\n[BBOX-535] 10\n[BBOX-536] 10\n[BBOX-537] 10\n[BBOX-538] 10\n[BBOX-539] 10\n[BBOX-540] 10\n[BBOX-541] 10\n[BBOX-542] 10\n[BBOX-543] 10\n[BBOX-544] 10\n[BBOX-545] 10\n[BBOX-546] 10\n[BBOX-547] 10\n[BBOX-548] 10\n[BBOX-549] 10\n[BBOX-550] 10\n[BBOX-551] 10\n[BBOX-552] 10\n[BBOX-553] 10\n[BBOX-554] 10\n[BBOX-555] 10\n[BBOX-556] 10\n[BBOX-557] 10\n[BBOX-558] 10\n[BBOX-559] 10\n[BBOX-560] 10\n[BBOX-561] 10\n[BBOX-562] 10\n[BBOX-563] 10\n[BBOX-564] 10\n[BBOX-565] 10\n[BBOX-566] 10\n[BBOX-567] 10\n[BBOX-568] 10\n[BBOX-569] 10\n[BBOX-570] 10\n[BBOX-571] 10\n[BBOX-572] 10\n[BBOX-573] 10\n[BBOX-574] 10\n[BBOX-575] 10\n[BBOX-576] 10\n[BBOX-577] 10\n[BBOX-578] 10\n[BBOX-579] 10\n[BBOX-580] 10\n[BBOX-581] 10\n[BBOX-582] 10\n[BBOX-583] 10\n[BBOX-584] 10\n[BBOX-585] 10\n[BBOX-586] 10\n[BBOX-587] 10\n[BBOX-588] 10\n[BBOX-589] 10\n[BBOX-590] 10\n[BBOX-591] 10\n[BBOX-592] 10\n[BBOX-593] 10\n[BBOX-594] 10\n[BBOX-595] 10\n[BBOX-596] 10\n[BBOX-597] 10\n[BBOX-598] 10\n[BBOX-599] 10\n[BBOX-600] 10\n[BBOX-601] 10\n[BBOX-602] 10\n[BBOX-603] 10\n[BBOX-604] 10\n[BBOX-605] 10\n[BBOX-606] 10\n[BBOX-607] 10\n[BBOX-608] 10\n[BBOX-609] 10\n[BBOX-610] 10\n[BBOX-611] 10\n[BBOX-612] 10\n[BBOX-613] 10\n[BBOX-614] 10\n[BBOX-615] 10\n[BBOX-616] 10\n[BBOX-617] 10\n[BBOX-618] 10\n[BBOX-619] 10\n[BBOX-620] 10\n[BBOX-621] 10\n[BBOX-622] 10\n[BBOX-623] 10\n[BBOX-624] 10\n[BBOX-625] 10\n[BBOX-626] 10\n[BBOX-627] 10\n[BBOX-628] 10\n[BBOX-629] 10\n[BBOX-630] 10\n[BBOX-631] 10\n[BBOX-632] 10\n[BBOX-633] 10\n[BBOX-634] 10\n[BBOX-635] 10\n[BBOX-636] 10\n[BBOX-637] 10\n[BBOX-638] 10\n[BBOX-639] 10\n[BBOX-640] 10\n[BBOX-641] 10\n[BBOX-642] 10\n[BBOX-643] 10\n[BBOX-644] 10\n[BBOX-645] 10\n[BBOX-646] 10\n[BBOX-647] 10\n[BBOX-648] 10\n[BBOX-649] 10\n[BBOX-650] 10\n[BBOX-651] 10\n[BBOX-652] 10\n[BBOX-653] 10\n[BBOX-654] 10\n[BBOX-655] 10\n[BBOX-656] 10\n[BBOX-657] 10\n[BBOX-658] 10\n[BBOX-659] 10\n[BBOX-660] 10\n[BBOX-661] 10\n[BBOX-662] 10\n[BBOX-663] 10\n[BBOX-664] 10\n[BBOX-665] 10\n[BBOX-666] 10\n[BBOX-667] 10\n[BBOX-668] 10\n[BBOX-669] 10\n[BBOX-670] 10\n[BBOX-671] 10\n[BBOX-672] 10\n[BBOX-673] 10\n[BBOX-674] 10\n[BBOX-675] 10\n[BBOX-676] 10\n[BBOX-677] 10\n[BBOX-678] 10\n[BBOX-679] 10\n[BBOX-680] 10\n[BBOX-681] 10\n[BBOX-682] 10\n[BBOX-683] 10\n[BBOX-684] 10\n[BBOX-685] 10\n[BBOX-686] 10\n[BBOX-687] 10\n[BBOX-688] 10\n[BBOX-689] 10\n[BBOX-690] 10\n[BBOX-691] 10\n[BBOX-692] 10\n[BBOX-693] 10\n[BBOX-694] 10\n[BBOX-695] 10\n[BBOX-696] 10\n[BBOX-697] 10\n[BBOX-698] 10\n[BBOX-699] 10\n[BBOX-700] 10\n[BBOX-701] 10\n[BBOX-702] 10\n[BBOX-703] 10\n[BBOX-704] 10\n[BBOX-705] 10\n[BBOX-706] 10\n[BBOX-707] 10\n[BBOX-708] 10\n[BBOX-709] 10\n[BBOX-710] 10\n[BBOX-711] 10\n[BBOX-712] 10\n[BBOX-713] 10\n[BBOX-714] 10\n[BBOX-715] 10\n[BBOX-716] 10\n[BBOX-717] 10\n[BBOX-718] 10\n[BBOX-719] 10\n[BBOX-720] 10\n[BBOX-721] 10\n[BBOX-722] 10\n[BBOX-723] 10\n[BBOX-724] 10\n[BBOX-725] 10\n[BBOX-726] 10\n[BBOX-727] 10\n[BBOX-728] 10\n[BBOX-729] 10\n[BBOX-730] 10\n[BBOX-731] 10\n[BBOX-732] 10\n[BBOX-733] 10\n[BBOX-734] 10\n[BBOX-735] 10\n[BBOX-736] 10\n[BBOX-737] 10\n[BBOX-738] 10\n[BBOX-739] 10\n[BBOX-740] 10\n[BBOX-741] 10\n[BBOX-742] 10\n[BBOX-743] 10\n[BBOX-744] 10\n[BBOX-745] 10\n[BBOX-746] 10\n[BBOX-747] 10\n[BBOX-748] 10\n[BBOX-749] 10\n[BBOX-750] 10\n[BBOX-751] 10\n[BBOX-752] 10\n[BBOX-753] 10\n[BBOX-754] 10\n[BBOX-755] 10\n[BBOX-756] 10\n[BBOX-757] 10\n[BBOX-758] 10\n[BBOX-759] 10\n[BBOX-760] 10\n[BBOX-761] 10\n[BBOX-762] 10\n[BBOX-763] 10\n[BBOX-764] 10\n[BBOX-765] 10\n[BBOX-766] 10\n[BBOX-767] 10\n[BBOX-768] 10\n[BBOX-769] 10\n[BBOX-770] 10\n[BBOX-771] 10\n[BBOX-772] 10\n[BBOX-773] 10\n[BBOX-774] 10\n[BBOX-775] 10\n[BBOX-776] 10\n[BBOX-777] 10\n[BBOX-778] 10\n[BBOX-779] 10\n[BBOX-780] 10\n[BBOX-781] 10\n[BBOX-782] 10\n[BBOX-783] 10\n[BBOX-784] 10\n[BBOX-785] 10\n[BBOX-786] 10\n[BBOX-787] 10\n[BBOX-788] 10\n[BBOX-789] 10\n[BBOX-790] 10\n[BBOX-791] 10\n[BBOX-792] 10\n[BBOX-793] 10\n[BBOX-794] 10\n[BBOX-795] 10\n[BBOX-796] 10\n[BBOX-797] 10\n[BBOX-798] 10\n[BBOX-799] 10\n[BBOX-800] 10\n[BBOX-801] 10\n[BBOX-802] 10\n[BBOX-803] 10\n[BBOX-804] 10\n[BBOX-805] 10\n[BBOX-806] 10\n[BBOX-807] 10\n[BBOX-808] 10\n[BBOX-809] 10\n[BBOX-810] 10\n[BBOX-811] 10\n[BBOX-812] 10\n[BBOX-813] 10\n[BBOX-814] 10\n[BBOX-815] 10\n[BBOX-816] 10\n[BBOX-817] 10\n[BBOX-818] 10\n[BBOX-819] 10\n[BBOX-820] 10\n[BBOX-821] 10\n[BBOX-822] 10\n[BBOX-823] 10\n[BBOX-824] 10\n[BBOX-825] 10\n[BBOX-826] 10\n[BBOX-827] 10\n[BBOX-828] 10\n[BBOX-829] 10\n[BBOX-830] 10\n[BBOX-831] 10\n[BBOX-832] 10\n[BBOX-833] 10\n[BBOX-834] 10\n[BBOX-835] 10\n[BBOX-836] 10\n[BBOX-837] 10\n[BBOX-838] 10\n[BBOX-839] 10\n[BBOX-840] 10\n[BBOX-841] 10\n[BBOX-842] 10\n[BBOX-843] 10\n[BBOX-844] 10\n[BBOX-845] 10\n[BBOX-846] 10\n[BBOX-847] 10\n[BBOX-848] 10\n[BBOX-849] 10\n[BBOX-850] 10\n[BBOX-851] 10\n[BBOX-852] 10\n[BBOX-853] 10\n[BBOX-854] 10\n[BBOX-855] 10\n[BBOX-856] 10\n[BBOX-857] 10\n[BBOX-858] 10\n[BBOX-859] 10\n[BBOX-860] 10\n[BBOX-861] 10\n[BBOX-862] 10\n[BBOX-863] 10\n[BBOX-864] 10\n[BBOX-865] 10\n[BBOX-866] 10\n[BBOX-867] 10\n[BBOX-868] 10\n[BBOX-869] 10\n[BBOX-870] 10\n[BBOX-871] 10\n[BBOX-872] 10\n[BBOX-873] 10\n[BBOX-874] 10\n[BBOX-875] 10\n[BBOX-876] 10\n[BBOX-877] 10\n[BBOX-878] 10\n[BBOX-879] 10\n[BBOX-880] 10\n[BBOX-881] 10\n[BBOX-882] 10\n[BBOX-883] 10\n[BBOX-884] 10\n[BBOX-885] 10\n[BBOX-886] 10\n[BBOX-887] 10\n[BBOX-888] 10\n[BBOX-889] 10\n[BBOX-890] 10\n[BBOX-891] 10\n[BBOX-892] 10\n[BBOX-893] 10\n[BBOX-894] 10\n[BBOX-895] 10\n[BBOX-896] 10\n[BBOX-897] 10\n[BBOX-898] 10\n[BBOX-899] 10\n[BBOX-900] 10\n[BBOX-901] 10\n[BBOX-902] 10\n[BBOX-903] 10\n[BBOX-904] 10\n[BBOX-905] 10\n[BBOX-906] 10\n[BBOX-907] 10\n[BBOX-908] 10\n[BBOX-909] 10\n[BBOX-910] 10\n[BBOX-911] 10\n[BBOX-912] 10\n[BBOX-913] 10\n[BBOX-914] 10\n[BBOX-915] 10\n[BBOX-916] 10\n[BBOX-917] 10\n[BBOX-918] 10\n[BBOX-919] 10\n[BBOX-920] 10\n[BBOX-921] 10\n[BBOX-922] 10\n[BBOX-923] 10\n[BBOX-924] 10\n[BBOX-925] 10\n[BBOX-926] 10\n[BBOX-927] 10\n[BBOX-928] 10\n[BBOX-929] 10\n[BBOX-930] 10\n[BBOX-931] 10\n[BBOX-932] 10\n[BBOX-933] 10\n[BBOX-934] 10\n[BBOX-935] 10\n[BBOX-936] 10\n[BBOX-937] 10\n[BBOX-938] 10\n[BBOX-939] 10\n[BBOX-940] 10\n[BBOX-941] 10\n[BBOX-942] 10\n[BBOX-943] 10\n[BBOX-944] 10\n[BBOX-945] 10\n[BBOX-946] 10\n[BBOX-947] 10\n[BBOX-948] 10\n[BBOX-949] 10\n[BBOX-950] 10\n[BBOX-951] 10\n[BBOX-952] 10\n[BBOX-953] 10\n[BBOX-954] 10\n[BBOX-955] 10\n[BBOX-956] 10\n[BBOX-957] 10\n[BBOX-958] 10\n[BBOX-959] 10\n[BBOX-960] 10\n[BBOX-961] 10\n[BBOX-962] 10\n[BBOX-963] 10\n[BBOX-964] 10\n[BBOX-965] 10\n[BBOX-966] 10\n[BBOX-967] 10\n[BBOX-968] 10\n[BBOX-969] 10\n[BBOX-970] 10\n[BBOX-971] 10\n[BBOX-972] 10\n[BBOX-973] 10\n[BBOX-974] 10\n[BBOX-975] 10\n[BBOX-976] 10\n[BBOX-977] 10\n[BBOX-978] 10\n[BBOX-979] 10\n[BBOX-980] 10\n[BBOX-981] 10\n[BBOX-982] 10\n[BBOX-983] 10\n[BBOX-984] 10\n[BBOX-985] 10\n[BBOX-986] 10\n[BBOX-987] 10\n[BBOX-988] 10\n[BBOX-989] 10\n[BBOX-990] 10\n[BBOX-991] 10\n[BBOX-992] 10\n[BBOX-993] 10\n[BBOX-994] 10\n[BBOX-995] 10\n[BBOX-996] 10\n[BBOX-997] 10\n[BBOX-998] 10\n[BBOX-999] 10\n[BBOX-1000] 10\n[BBOX-1001] 10\n[BBOX-1002] 10\n[BBOX-1003] 10\n[BBOX-1004] 10\n[BBOX-1005] 10\n[BBOX-1006] 10\n[BBOX-1007] 10\n[BBOX-1008] 10\n[BBOX-1009] 10\n[BBOX-1010] 10\n[BBOX-1011] 10\n[BBOX-1012] 10\n[BBOX-1013] 10\n[BBOX-1014] 10\n[BBOX-1015] 10\n[BBOX-1016] 10\n[BBOX-1017] 10\n[BBOX-1018] 10\n[BBOX-1019] 10\n[BBOX-1020] 10\n[BBOX-1021] 10\n[BBOX-1022] 10\n[BBOX-1023] 10\n[BBOX-1024] 10\n[BBOX-1025] 10\n[BBOX-1026] 10\n[BBOX-1027] 10\n[BBOX-1028] 10\n[BBOX-1029] 10\n[BBOX-1030] 10\n[BBOX-1031] 10\n[BBOX-1032] 10\n[BBOX-1033] 10\n[BBOX-1034] 10\n[BBOX-1035] 10\n[BBOX-1036] 10\n[BBOX-1037] 10\n[BBOX-1038] 10\n[BBOX-1039] 10\n[BBOX-1040] 10\n[BBOX-1041] 10\n[BBOX-1042] 10\n[BBOX-1043] 10\n[BBOX-1044] 10\n[BBOX-1045] 10\n[BBOX-1046] 10\n[BBOX-1047] 10\n[BBOX-1048] 10\n[BBOX-1049] 10\n[BBOX-1050] 10\n[BBOX-1051] 10\n[BBOX-1052] 10\n[BBOX-1053] 10\n[BBOX-1054] 10\n[BBOX-1055] 10\n[BBOX-1056] 10\n[BBOX-1057] 10\n[BBOX-1058] 10\n[BBOX-1059] 10\n[BBOX-1060] 10\n[BBOX-1061] 10\n[BBOX-1062] 10\n[BBOX-1063] 10\n[BBOX-1064] 10\n[BBOX-1065] 10\n[BBOX-1066] 10\n[BBOX-1067] 10\n[BBOX-1068] 10\n[BBOX-1069] 10\n[BBOX-1070] 10\n[BBOX-1071] 10\n[BBOX-1072] 10\n[BBOX-1073] 10\n[BBOX-1074] 10\n[BBOX-1075] 10\n[BBOX-1076] 10\n[BBOX-1077] 10\n[BBOX-1078] 10\n[BBOX-1079] 10\n[BBOX-1080] 10\n[BBOX-1081] 10\n[BBOX-1082] 10\n[BBOX-1083] 10\n[BBOX-1084] 10\n[BBOX-1085] 10\n[BBOX-1086] 10\n[BBOX-1087] 10\n[BBOX-1088] 10\n[BBOX-1089] 10\n[BBOX-1090] 10\n[BBOX-1091] 10\n[BBOX-1092] 10\n[BBOX-1093] 10\n[BBOX-1094] 10\n[BBOX-1095] 10\n[BBOX-1096] 10\n[BBOX-1097] 10\n[BBOX-1098] 10\n[BBOX-1099] 10\n[BBOX-1100] 10\n[BBOX-1101] 10\n[BBOX-1102] 10\n[BBOX-1103] 10\n[BBOX-1104] 10\n[BBOX-1105] 10\n[BBOX-1106] 10\n[BBOX-1107] 10\n[BBOX-1108] 10\n[BBOX-1109] 10\n[BBOX-1110] 10\n[BBOX-1111] 10\n[BBOX-1112] 10\n[BBOX-1113] 10\n[BBOX-1114] 10\n[BBOX-1115] 10\n[BBOX-1116] 10\n[BBOX-1117] 10\n[BBOX-1118] 10\n[BBOX-1119] 10\n[BBOX-1120] 10\n[BBOX-1121] 10\n[BBOX-1122] 10\n[BBOX-1123] 10\n[BBOX-1124] 10\n[BBOX-1125] 10\n[BBOX-1126] 10\n[BBOX-1127] 10\n[BBOX-1128] 10\n[BBOX-1129] 10\n[BBOX-1130] 10\n[BBOX-1131] 10\n[BBOX-1132] 10\n[BBOX-1133] 10\n[BBOX-1134] 10\n[BBOX-1135] 10\n[BBOX-1136] 10\n[BBOX-1137] 10\n[BBOX-1138] 10\n[BBOX-1139] 10\n[BBOX-1140] 10\n[BBOX-1141] 10\n[BBOX-1142] 10\n[BBOX-1143] 10\n[BBOX-1144] 10\n[BBOX-1145] 10\n[BBOX-1146] 10\n[BBOX-1147] 10\n[BBOX-1148] 10\n[BBOX-1149] 10\n[BBOX-1150] 10\n[BBOX-1151] 10\n[BBOX-1152] 10\n[BBOX-1153] 10\n[BBOX-1154] 10\n[BBOX-1155] 10\n[BBOX-1156] 10\n[BBOX-1157] 10\n[BBOX-1158] 10\n[BBOX-1159] 10\n[BBOX-1160] 10\n[BBOX-1161] 10\n[BBOX-1162] 10\n[BBOX-1163] 10\n[BBOX-1164] 10\n[BBOX-1165] 10\n[BBOX-1166] 10\n[BBOX-1167] 10\n[BBOX-1168] 10\n[BBOX-1169] 10\n[BBOX-1170] 10\n[BBOX-1171] 10\n[BBOX-1172] 10\n[BBOX-1173] 10\n[BBOX-1174] 10\n[BBOX-1175] 10\n[BBOX-1176] 10\n[BBOX-1177] 10\n[BBOX-1178] 10\n[BBOX-1179] 10\n[BBOX-1180] 10\n[BBOX-1181] 10\n[BBOX-1182] 10\n[BBOX-1183] 10\n[BBOX-1184] 10\n[BBOX-1185] 10\n[BBOX-1186] 10\n[BBOX-1187] 10\n[BBOX-1188] 10\n[BBOX-1189] 10\n[BBOX-1190] 10\n[BBOX-1191] 10\n[BBOX-1192] 10\n[BBOX-1193] 10\n[BBOX-1194] 10\n[BBOX-1195] 10\n[BBOX-1196] 10\n[BBOX-1197] 10\n[BBOX-1198] 10\n[BBOX-1199] 10\n[BBOX-1200] 10\n[BBOX-1201] 10\n[BBOX-1202] 10\n[BBOX-1203] 10\n[BBOX-1204] 10\n[BBOX-1205] 10\n[BBOX-1206] 10\n[BBOX-1207] 10\n[BBOX-1208] 10\n[BBOX-1209] 10\n[BBOX-1210] 10\n[BBOX-1211] 10\n[BBOX-1212] 10\n[BBOX-1213] 10\n[BBOX-1214] 10\n[BBOX-1215] 10\n[BBOX-1216] 10\n[BBOX-1217] 10\n[BBOX-1218] 10\n[BBOX-1219] 10\n[BBOX-1220] 10\n[BBOX-1221] 10\n[BBOX-1222] 10\n[BBOX-1223] 10\n[BBOX-1224] 10\n[BBOX-1225] 10\n[BBOX-1226] 10\n[BBOX-1227] 10\n[BBOX-1228] 10\n[BBOX-1229] 10\n[BBOX-1230] 10\n[BBOX-1231] 10\n[BBOX-1232] 10\n[BBOX-1233] 10\n[BBOX-1234] 10\n[BBOX-1235] 10\n[BBOX-1236] 10\n[BBOX-1237] 10\n[BBOX-1238] 10\n[BBOX-1239] 10\n[BBOX-1240] 10\n[BBOX-1241] 10\n[BBOX-1242] 10\n[BBOX-1243] 10\n[BBOX-1244] 10\n[BBOX-1245] 10\n[BBOX-1246] 10\n[BBOX-1247] 10\n[BBOX-1248] 10\n[BBOX-1249] 10\n[BBOX-1250] 10\n[BBOX-1251] 10\n[BBOX-1252] 10\n[BBOX-1253] 10\n[BBOX-1254] 10\n[BBOX-1255] 10\n[BBOX-1256] 10\n[BBOX-1257] 10\n[BBOX-1258] 10\n[BBOX-1259] 10\n[BBOX-1260] 10\n[BBOX-1261] 10\n[BBOX-1262] 10\n[BBOX-1263] 10\n[BBOX-1264] 10\n[BBOX-1265] 10\n[BBOX-1266] 10\n[BBOX-1267] 10\n[BBOX-1268] 10\n[BBOX-1269] 10\n[BBOX-1270] 10\n[BBOX-1271] 10\n[BBOX-1272] 10\n[BBOX-1273] 10\n[BBOX-1274] 10\n[BBOX-1275] 10\n[BBOX-1276] 10\n[BBOX-1277] 10\n[BBOX-1278] 10\n[BBOX-1279] 10\n[BBOX-1280] 10\n[BBOX-1281] 10\n[BBOX-1282] 10\n[BBOX-1283] 10\n[BBOX-1284] 10\n[BBOX-1285] 10\n[BBOX-1286] 10\n[BBOX-1287] 10\n[BBOX-1288] 10\n[BBOX-1289] 10\n[BBOX-1290] 10\n[BBOX-1291] 10\n[BBOX-1292] 10\n[BBOX-1293] 10\n[BBOX-1294] 10\n[BBOX-1295] 10\n[BBOX-1296] 10\n[BBOX-1297] 10\n[BBOX-1298] 10\n[BBOX-1299] 10\n[BBOX-1300] 10\n[BBOX-1301] 10\n[BBOX-1302] 10\n[BBOX-1303] 10\n[BBOX-1304] 10\n[BBOX-1305] 10\n[BBOX-1306] 10\n[BBOX-1307] 10\n[BBOX-1308] 10\n[BBOX-1309] 10\n[BBOX-1310] 10\n[BBOX-1311] 10\n[BBOX-1312] 10\n[BBOX-1313] 10\n[BBOX-1314] 10\n[BBOX-1315] 10\n[BBOX-1316] 10\n[BBOX-1317] 10\n[BBOX-1318] 10\n[BBOX-1319] 10\n[BBOX-1320] 10\n[BBOX-1321] 10\n[BBOX-1322] 10\n[BBOX-1323] 10\n[BBOX-1324] 10\n[BBOX-1325] 10\n[BBOX-1326] 10\n[BBOX-1327] 10\n[BBOX-1328] 10\n[BBOX-1329] 10\n[BBOX-1330] 10\n[BBOX-1331] 10\n[BBOX-1332] 10\n[BBOX-1333] 10\n[BBOX-1334] 10\n[BBOX-1335] 10\n[BBOX-1336] 10\n[BBOX-1337] 10\n[BBOX-1338] 10\n[BBOX-1339] 10\n[BBOX-1340] 10\n[BBOX-1341] 10\n[BBOX-1342] 10\n[BBOX-1343] 10\n[BBOX-1344] 10\n[BBOX-1345] 10\n[BBOX-1346] 10\n[BBOX-1347] 10\n[BBOX-1348] 10\n[BBOX-1349] 10\n[BBOX-1350] 10\n[BBOX-1351] 10\n[BBOX-1352] 10\n[BBOX-1353] 10\n[BBOX-1354] 10\n[BBOX-1355] 10\n[BBOX-1356] 10\n[BBOX-1357] 10\n[BBOX-1358] 10\n[BBOX-1359] 10\n[BBOX-1360] 10\n[BBOX-1361] 10\n[BBOX-1362] 10\n[BBOX-1363] 10\n[BBOX-1364] 10\n[BBOX-1365] 10\n[BBOX-1366] 10\n[BBOX-1367] 10\n[BBOX-1368] 10\n[BBOX-1369] 10\n[BBOX-1370] 10\n[BBOX-1371] 10\n[BBOX-1372] 10\n[BBOX-1373] 10\n[BBOX-1374] 10\n[BBOX-1375] 10\n[BBOX-1376] 10\n[BBOX-1377] 10\n[BBOX-1378] 10\n[BBOX-1379] 10\n[BBOX-1380] 10\n[BBOX-1381] 10\n[BBOX-1382] 10\n[BBOX-1383] 10\n[BBOX-1384] 10\n[BBOX-1385] 10\n[BBOX-1386] 10\n[BBOX-1387] 10\n[BBOX-1388] 10\n[BBOX-1389] 10\n[BBOX-1390] 10\n[BBOX-1391] 10\n[BBOX-1392] 10\n[BBOX-1393] 10\n[BBOX-1394] 10\n[BBOX-1395] 10\n[BBOX-1396] 10\n[BBOX-1397] 10\n[BBOX-1398] 10\n[BBOX-1399] 10\n[BBOX-1400] 10\n[BBOX-1401] 10\n[BBOX-1402] 10\n[BBOX-1403] 10\n[BBOX-1404] 10\n[BBOX-1405] 10\n[BBOX-1406] 10\n[BBOX-1407] 10\n[BBOX-1408] 10\n[BBOX-1409] 10\n[BBOX-1410] 10\n[BBOX-1411] 10\n[BBOX-1412] 10\n[BBOX-1413] 10\n[BBOX-1414] 10\n[BBOX-1415] 10\n[BBOX-1416] 10\n[BBOX-1417] 10\n[BBOX-1418] 10\n[BBOX-1419] 10\n[BBOX-1420] 10\n[BBOX-1421] 10\n[BBOX-1422] 10\n[BBOX-1423] 10\n[BBOX-1424] 10\n[BBOX-1425] 10\n[BBOX-1426] 10\n[BBOX-1427] 10\n[BBOX-1428] 10\n[BBOX-1429] 10\n[BBOX-1430] 10\n[BBOX-1431] 10\n[BBOX-1432] 10\n[BBOX-1433] 10\n[BBOX-1434] 10\n[BBOX-1435] 10\n[BBOX-1436] 10\n[BBOX-1437] 10\n[BBOX-1438] 10\n[BBOX-1439] 10\n[BBOX-1440] 10\n[BBOX-1441] 10\n[BBOX-1442] 10\n[BBOX-1443] 10\n[BBOX-1444] 10\n[BBOX-1445] 10\n[BBOX-1446] 10\n[BBOX-1447] 10\n[BBOX-1448] 10\n[BBOX-1449] 10\n[BBOX-1450] 10\n[BBOX-1451] 10\n[BBOX-1452] 10\n[BBOX-1453] 10\n[BBOX-1454] 10\n[BBOX-1455] 10\n[BBOX-1456] 10\n[BBOX-1457] 10\n[BBOX-1458] 10\n[BBOX-1459] 10\n[BBOX-1460] 10\n[BBOX-1461] 10\n[BBOX-1462] 10\n[BBOX-1463] 10\n[BBOX-1464] 10\n[BBOX-1465] 10\n[BBOX-1466] 10\n[BBOX-1467] 10\n[BBOX-1468] 10\n[BBOX-1469] 10\n[BBOX-1470] 10\n[BBOX-1471] 10\n[BBOX-1472] 10\n[BBOX-1473] 10\n[BBOX-1474] 10\n[BBOX-1475] 10\n[BBOX-1476] 10\n[BBOX-1477] 10\n[BBOX-1478] 10\n[BBOX-1479] 10\n[BBOX-1480] 10\n[BBOX-1481] 10\n[BBOX-1482] 10\n[BBOX-1483] 10\n[BBOX-1484] 10\n[BBOX-1485] 10\n[BBOX-1486] 10\n[BBOX-1487] 10\n[BBOX-1488] 10\n[BBOX-1489] 10\n[BBOX-1490] 10\n[BBOX-1491] 10\n[BBOX-1492] 10\n[BBOX-1493] 10\n[BBOX-1494] 10\n[BBOX-1495] 10\n[BBOX-1496] 10\n[BBOX-1497] 10\n[BBOX-1498] 10\n[BBOX-1499] 10\n[BBOX-1500] 10\n[BBOX-1501] 10\n[BBOX-1502] 10\n[BBOX-1503] 10\n[BBOX-1504] 10\n[BBOX-1505] 10\n[BBOX-1506] 10\n[BBOX-1507] 10\n[BBOX-1508] 10\n[BBOX-1509] 10\n[BBOX-1510] 10\n[BBOX-1511] 10\n[BBOX-1512] 10\n[BBOX-1513] 10\n[BBOX-1514] 10\n[BBOX-1515] 10\n[BBOX-1516] 10\n[BBOX-1517] 10\n[BBOX-1518] 10\n[BBOX-1519] 10\n[BBOX-1520] 10\n[BBOX-1521] 10\n[BBOX-1522] 10\n[BBOX-1523] 10\n[BBOX-1524] 10\n[BBOX-1525] 10\n[BBOX-1526] 10\n[BBOX-1527] 10\n[BBOX-1528] 10\n[BBOX-1529] 10\n[BBOX-1530] 10\n[BBOX-1531] 10\n[BBOX-1532] 10\n[BBOX-1533] 10\n[BBOX-1534] 10\n[BBOX-1535] 10\n[BBOX-1536] 10\n[BBOX-1537] 10\n[BBOX-1538] 10\n[BBOX-1539] 10\n[BBOX-1540] 10\n[BBOX-1541] 10\n[BBOX-1542] 10\n[BBOX-1543] 10\n[BBOX-1544] 10\n[BBOX-1545] 10\n[BBOX-1546] 10\n[BBOX-1547] 10\n[BBOX-1548] 10\n[BBOX-1549] 10\n[BBOX-1550] 10\n[BBOX-1551] 10\n[BBOX-1552] 10\n[BBOX-1553] 10\n[BBOX-1554] 10\n[BBOX-1555] 10\n[BBOX-1556] 10\n[BBOX-1557] 10\n[BBOX-1558] 10\n[BBOX-1559] 10\n[BBOX-1560] 10\n[BBOX-1561] 10\n[BBOX-1562] 10\n[BBOX-1563] 10\n[BBOX-1564] 10\n[BBOX-1565] 10\n[BBOX-1566] 10\n[BBOX-1567] 10\n[BBOX-1568] 10\n[BBOX-1569] 10\n[BBOX-1570] 10\n[BBOX-1571] 10\n[BBOX-1572] 10\n[BBOX-1573] 10\n[BBOX-1574] 10\n[BBOX-1575] 10\n[BBOX-1576] 10\n[BBOX-1577] 10\n[BBOX-1578] 10\n[BBOX-1579] 10\n[BBOX-1580] 10\n[BBOX-1581] 10\n[BBOX-1582] 10\n[BBOX-1583] 10\n[BBOX-1584] 10\n[BBOX-1585] 10\n[BBOX-1586] 10\n[BBOX-1587] 10\n[BBOX-1588] 10\n[BBOX-1589] 10\n[BBOX-1590] 10\n[BBOX-1591] 10\n[BBOX-1592] 10\n[BBOX-1593] 10\n[BBOX-1594] 10\n[BBOX-1595] 10\n[BBOX-1596] 10\n[BBOX-1597] 10\n[BBOX-1598] 10\n[BBOX-1599] 10\n[BBOX-1600] 10\n[BBOX-1601] 10\n[BBOX-1602] 10\n[BBOX-1603] 10\n[BBOX-1604] 10\n[BBOX-1605] 10\n[BBOX-1606] 10\n[BBOX-1607] 10\n[BBOX-1608] 10\n[BBOX-1609] 10\n[BBOX-1610] 10\n[BBOX-1611] 10\n[BBOX-1612] 10\n[BBOX-1613] 10\n[BBOX-1614] 10\n[BBOX-1615] 10\n[BBOX-1616] 10\n[BBOX-1617] 10\n[BBOX-1618] 10\n[BBOX-1619] 10\n[BBOX-1620] 10\n[BBOX-1621] 10\n[BBOX-1622] 10\n[BBOX-1623] 10\n[BBOX-1624] 10\n[BBOX-1625] 10\n[BBOX-1626] 10\n[BBOX-1627] 10\n[BBOX-1628] 10\n[BBOX-1629] 10\n[BBOX-1630] 10\n[BBOX-1631] 10\n[BBOX-1632] 10\n[BBOX-1633] 10\n[BBOX-1634] 10\n[BBOX-1635] 10\n[BBOX-1636] 10\n[BBOX-1637] 10\n[BBOX-1638] 10\n[BBOX-1639] 10\n[BBOX-1640] 10\n[BBOX-1641] 10\n[BBOX-1642] 10\n[BBOX-1643] 10\n[BBOX-1644] 10\n[BBOX-1645] 10\n[BBOX-1646] 10\n[BBOX-1647] 10\n[BBOX-1648] 10\n[BBOX-1649] 10\n[BBOX-1650] 10\n[BBOX-1651] 10\n[BBOX-1652] 10\n[BBOX-1653] 10\n[BBOX-1654] 10\n[BBOX-1655] 10\n[BBOX-1656] 10\n[BBOX-1657] 10\n[BBOX-1658] 10\n[BBOX-1659] 10\n[BBOX-1660] 10\n[BBOX-1661] 10\n[BBOX-1662] 10\n[BBOX-1663] 10\n[BBOX-1664] 10\n[BBOX-1665] 10\n[BBOX-1666] 10\n[BBOX-1667] 10\n[BBOX-1668] 10\n[BBOX-1669] 10\n[BBOX-1670] 10\n[BBOX-1671] 10\n[BBOX-1672] 10\n[BBOX-1673] 10\n[BBOX-1674] 10\n[BBOX-1675] 10\n[BBOX-1676] 10\n[BBOX-1677] 10\n[BBOX-1678] 10\n[BBOX-1679] 10\n[BBOX-1680] 10\n[BBOX-1681] 10\n[BBOX-1682] 10\n[BBOX-1683] 10\n[BBOX-1684] 10\n[BBOX-1685] 10\n[BBOX-1686] 10\n[BBOX-1687] 10\n[BBOX-1688] 10\n[BBOX-1689] 10\n[BBOX-1690] 10\n[BBOX-1691] 10\n[BBOX-1692] 10\n[BBOX-1693] 10\n[BBOX-1694] 10\n[BBOX-1695] 10\n[BBOX-1696] 10\n[BBOX-1697] 10\n[BBOX-1698] 10\n[BBOX-1699] 10\n[BBOX-1700] 10\n[BBOX-1701] 10\n[BBOX-1702] 10\n[BBOX-1703] 10\n[BBOX-1704] 10\n[BBOX-1705] 10\n[BBOX-1706] 10\n[BBOX-1707] 10\n[BBOX-1708] 10\n[BBOX-1709] 10\n[BBOX-1710] 10\n[BBOX-1711] 10\n[BBOX-1712] 10\n[BBOX-1713] 10\n[BBOX-1714] 10\n[BBOX-1715] 10\n[BBOX-1716] 10\n[BBOX-1717] 10\n[BBOX-1718] 10\n[BBOX-1719] 10\n[BBOX-1720] 10\n[BBOX-1721] 10\n[BBOX-1722] 10\n[BBOX-1723] 10\n[BBOX-1724] 10\n[BBOX-1725] 10\n[BBOX-1726] 10\n[BBOX-1727] 10\n[BBOX-1728] 10\n[BBOX-1729] 10\n[BBOX-1730] 10\n[BBOX-1731] 10\n[BBOX-1732] 10\n[BBOX-1733] 10\n[BBOX-1734] 10\n[BBOX-1735] 10\n[BBOX-1736] 10\n[BBOX-1737] 10\n[BBOX-1738] 10\n[BBOX-1739] 10\n[BBOX-1740] 10\n[BBOX-1741] 10\n[BBOX-1742] 10\n[BBOX-1743] 10\n[BBOX-1744] 10\n[BBOX-1745] 10\n[BBOX-1746] 10\n[BBOX-1747] 10\n[BBOX-1748] 10\n[BBOX-1749] 10\n[BBOX-1750] 10\n[BBOX-1751] 10\n[BBOX-1752] 10\n[BBOX-1753] 10\n[BBOX-1754] 10\n[BBOX-1755] 10\n[BBOX-1756] 10\n[BBOX-1757] 10\n[BBOX-1758] 10\n[BBOX-1759] 10\n[BBOX-1760] 10\n[BBOX-1761] 10\n[BBOX-1762] 10\n[BBOX-1763] 10\n[BBOX-1764] 10\n[BBOX-1765] 10\n[BBOX-1766] 10\n[BBOX-1767] 10\n[BBOX-1768] 10\n[BBOX-1769] 10\n[BBOX-1770] 10\n[BBOX-1771] 10\n[BBOX-1772] 10\n[BBOX-1773] 10\n[BBOX-1774] 10\n[BBOX-1775] 10\n[BBOX-1776] 10\n[BBOX-1777] 10\n[BBOX-1778] 10\n[BBOX-1779] 10\n[BBOX-1780] 10\n[BBOX-1781] 10\n[BBOX-1782] 10\n[BBOX-1783] 10\n[BBOX-1784] 10\n[BBOX-1785] 10\n[BBOX-1786] 10\n[BBOX-1787] 10\n[BBOX-1788] 10\n[BBOX-1789] 10\n[BBOX-1790] 10\n[BBOX-1791] 10\n[BBOX-1792] 10\n[BBOX-1793] 10\n[BBOX-1794] 10\n[BBOX-1795] 10\n[BBOX-1796] 10\n[BBOX-1797] 10\n[BBOX-1798] 10\n[BBOX-1799] 10\n[BBOX-1800] 10\n[BBOX-1801] 10\n[BBOX-1802] 10\n[BBOX-1803] 10\n[BBOX-1804] 10\n[BBOX-1805] 10\n[BBOX-1806] 10\n[BBOX-1807] 10\n[BBOX-1808] 10\n[BBOX-1809] 10\n[BBOX-1810] 10\n[BBOX-1811] 10\n[BBOX-1812] 10\n[BBOX-1813] 10\n[BBOX-1814] 10\n[BBOX-1815] 10\n[BBOX-1816] 10\n[BBOX-1817] 10\n[BBOX-1818] 10\n[BBOX-1819] 10\n[BBOX-1820] 10\n[BBOX-1821] 10\n[BBOX-1822] 10\n[BBOX-1823] 10\n[BBOX-1824] 10\n[BBOX-1825] 10\n[BBOX-1826] 10\n[BBOX-1827] 10\n[BBOX-1828] 10\n[BBOX-1829] 10\n[BBOX-1830] 10\n[BBOX-1831] 10\n[BBOX-1832] 10\n[BBOX-1833] 10\n[BBOX-1834] 10\n[BBOX-1835] 10\n[BBOX-1836] 10\n[BBOX-1837] 10\n[BBOX-1838] 10\n[BBOX-1839] 10\n[BBOX-1840] 10\n[BBOX-1841] 10\n[BBOX-1842] 10\n[BBOX-1843] 10\n[BBOX-1844] 10\n[BBOX-1845] 10\n[BBOX-1846] 10\n[BBOX-1847] 10\n[BBOX-1848] 10\n[BBOX-1849] 10\n[BBOX-1850] 10\n[BBOX-1851] 10\n[BBOX-1852] 10\n[BBOX-1853] 10\n[BBOX-1854] 10\n[BBOX-1855] 10\n[BBOX-1856] 10\n[BBOX-1857] 10\n[BBOX-1858] 10\n[BBOX-1859] 10\n[BBOX-1860] 10\n[BBOX-1861] 10\n[BBOX-1862] 10\n[BBOX-1863] 10\n[BBOX-1864] 10\n[BBOX-1865] 10\n[BBOX-1866] 10\n[BBOX-1867] 10\n[BBOX-1868] 10\n[BBOX-1869] 10\n[BBOX-1870] 10\n[BBOX-1871] 10\n[BBOX-1872] 10\n[BBOX-1873] 10\n[BBOX-1874] 10\n[BBOX-1875] 10\n[BBOX-1876] 10\n[BBOX-1877] 10\n[BBOX-1878] 10\n[BBOX-1879] 10\n[BBOX-1880] 10\n[BBOX-1881] 10\n[BBOX-1882] 10\n[BBOX-1883] 10\n[BBOX-1884] 10\n[BBOX-1885] 10\n[BBOX-1886] 10\n[BBOX-1887] 10\n[BBOX-1888] 10\n[BBOX-1889] 10\n[BBOX-1890] 10\n[BBOX-1891] 10\n[BBOX-1892] 10\n[BBOX-1893] 10\n[BBOX-1894] 10\n[BBOX-1895] 10\n[BBOX-1896] 10\n[BBOX-1897] 10\n[BBOX-1898] 10\n[BBOX-1899] 10\n[BBOX-1900] 10\n[BBOX-1901] 10\n[BBOX-1902] 10\n[BBOX-1903] 10\n[BBOX-1904] 10\n[BBOX-1905] 10\n[BBOX-1906] 10\n[BBOX-1907] 10\n[BBOX-1908] 10\n[BBOX-1909] 10\n[BBOX-1910] 10\n[BBOX-1911] 10\n[BBOX-1912] 10\n[BBOX-1913] 10\n[BBOX-1914] 10\n[BBOX-1915] 10\n[BBOX-1916] 10\n[BBOX-1917] 10\n[BBOX-1918] 10\n[BBOX-1919] 10\n[BBOX-1920] 10\n[BBOX-1921] 10\n[BBOX-1922] 10\n[BBOX-1923] 10\n[BBOX-1924] 10\n[BBOX-1925] 10\n[BBOX-1926] 10\n[BBOX-1927] 10\n[BBOX-1928] 10\n[BBOX-1929] 10\n[BBOX-1930] 10\n[BBOX-1931] 10\n[BBOX-1932] 10\n[BBOX-1933] 10\n[BBOX-1934] 10\n[BBOX-1935] 10\n[BBOX-1936] 10\n[BBOX-1937] 10\n[BBOX-1938] 10\n[BBOX-1939] 10\n[BBOX-1940] 10\n[BBOX-1941] 10\n[BBOX-1942] 10\n[BBOX-1943] 10\n[BBOX-1944] 10\n[BBOX-1945] 10\n[BBOX-1946] 10\n[BBOX-1947] 10\n[BBOX-1948] 10\n[BBOX-1949] 10\n[BBOX-1950] 10\n[BBOX-1951] 10\n[BBOX-1952] 10\n[BBOX-1953] 10\n[BBOX-1954] 10\n[BBOX-1955] 10\n[BBOX-1956] 10\n[BBOX-1957] 10\n[BBOX-1958] 10\n[BBOX-1959] 10\n[BBOX-1960] 10\n[BBOX-1961] 10\n[BBOX-1962] 10\n[BBOX-1963] 10\n[BBOX-1964] 10\n[BBOX-1965] 10\n[BBOX-1966] 10\n[BBOX-1967] 10\n[BBOX-1968] 10\n[BBOX-1969] 10\n[BBOX-1970] 10\n[BBOX-1971] 10\n[BBOX-1972] 10\n[BBOX-1973] 10\n[BBOX-1974] 10\n[BBOX-1975] 10\n[BBOX-1976] 10\n[BBOX-1977] 10\n[BBOX-1978] 10\n[BBOX-1979] 10\n[BBOX-1980] 10\n[BBOX-1981] 10\n[BBOX-1982] 10\n[BBOX-1983] 10\n[BBOX-1984] 10\n[BBOX-1985] 10\n[BBOX-1986] 10\n[BBOX-1987] 10\n[BBOX-1988] 10\n[BBOX-1989] 10\n[BBOX-1990] 10\n[BBOX-1991] 10\n[BBOX-1992] 10\n[BBOX-1993] 10\n[BBOX-1994] 10\n[BBOX-1995] 10\n[BBOX-1996] 10\n[BBOX-1997] 10\n[BBOX-1998] 10\n[BBOX-1999] 10\n[BBOX-2000] 10\n[BBOX-2001] 10\n[BBOX-2002] 10\n[BBOX-2003] 10\n[BBOX-2004] 10\n[BBOX-2005] 10\n[BBOX-2006] 10\n[BBOX-2007] 10\n[BBOX-2008] 10\n[BBOX-2009] 10\n[BBOX-2010] 10\n[BBOX-2011] 10\n[BBOX-2012] 10\n[BBOX-2013] 10\n[BBOX-2014] 10\n[BBOX-2015] 10\n[BBOX-2016] 10\n[BBOX-2017] 10\n[BBOX-2018] 10\n[BBOX-2019] 10\n[BBOX-2020] 10\n[BBOX-2021] 10\n[BBOX-2022] 10\n[BBOX-2023] 10\n[BBOX-2024] 10\n[BBOX-2025] 10\n[BBOX-2026] 10\n[BBOX-2027] 10\n[BBOX-2028] 10\n[BBOX-2029] 10\n[BBOX-2030] 10\n[BBOX-2031] 10\n[BBOX-2032] 10\n[BBOX-2033] 10\n[BBOX-2034] 10\n[BBOX-2035] 10\n[BBOX-2036] 10\n[BBOX-2037] 10\n[BBOX-2038] 10\n[BBOX-2039] 10\n[BBOX-2040] 10\n[BBOX-2041] 10\n[BBOX-2042] 10\n[BBOX-2043] 10\n[BBOX-2044] 10\n[BBOX-2045] 10\n[BBOX-2046] 10\n[BBOX-2047] 10\n[BBOX-2048] 10\n[BBOX-2049] 10\n[BBOX-2050] 10\n[BBOX-2051] 10\n[BBOX-2052] 10\n[BBOX-2053] 10\n[BBOX-2054] 10\n[BBOX-2055] 10\n[BBOX-2056] 10\n[BBOX-2057] 10\n[BBOX-2058] 10\n[BBOX-2059] 10\n[BBOX-2060] 10\n[BBOX-2061] 10\n[BBOX-2062] 10\n[BBOX-2063] 10\n[BBOX-2064] 10\n[BBOX-2065] 10\n[BBOX-2066] 10\n[BBOX-2067] 10\n[BBOX-2068] 10\n[BBOX-2069] 10\n[BBOX-2070] 10\n[BBOX-2071] 10\n[BBOX-2072] 10\n[BBOX-2073] 10\n[BBOX-2074] 10\n[BBOX-2075] 10\n[BBOX-2076] 10\n[BBOX-2077] 10\n[BBOX-2078] 10\n[BBOX-2079] 10\n[BBOX-2080] 10\n[BBOX-2081] 10\n[BBOX-2082] 10\n[BBOX-2083] 10\n[BBOX-2084] 10\n[BBOX-2085] 10\n[BBOX-2086] 10\n[BBOX-2087] 10\n[BBOX-2088] 10\n[BBOX-2089] 10\n[BBOX-2090] 10\n[BBOX-2091] 10\n[BBOX-2092] 10\n[BBOX-2093] 10\n[BBOX-2094] 10\n[BBOX-2095] 10\n[BBOX-2096] 10\n[BBOX-2097] 10\n[BBOX-2098] 10\n[BBOX-2099] 10\n[BBOX-2100] 10\n[BBOX-2101] 10\n[BBOX-2102] 10\n[BBOX-2103] 10\n[BBOX-2104] 10\n[BBOX-2105] 10\n[BBOX-2106] 10\n[BBOX-2107] 10\n[BBOX-2108] 10\n[BBOX-2109] 10\n[BBOX-2110] 10\n[BBOX-2111] 10\n[BBOX-2112] 10\n[BBOX-2113] 10\n[BBOX-2114] 10\n[BBOX-2115] 10\n[BBOX-2116] 10\n[BBOX-2117] 10\n[BBOX-2118] 10\n[BBOX-2119] 10\n[BBOX-2120] 10\n[BBOX-2121] 10\n[BBOX-2122] 10\n[BBOX-2123] 10\n[BBOX-2124] 10\n[BBOX-2125] 10\n[BBOX-2126] 10\n[BBOX-2127] 10\n[BBOX-2128] 10\n[BBOX-2129] 10\n[BBOX-2130] 10\n[BBOX-2131] 10\n[BBOX-2132] 10\n[BBOX-2133] 10\n[BBOX-2134] 10\n[BBOX-2135] 10\n[BBOX-2136] 10\n[BBOX-2137] 10\n[BBOX-2138] 10\n[BBOX-2139] 10\n[BBOX-2140] 10\n[BBOX-2141] 10\n[BBOX-2142] 10\n[BBOX-2143] 10\n[BBOX-2144] 10\n[BBOX-2145] 10\n[BBOX-2146] 10\n[BBOX-2147] 10\n[BBOX-2148] 10\n[BBOX-2149] 10\n[BBOX-2150] 10\n[BBOX-2151] 10\n[BBOX-2152] 10\n[BBOX-2153] 10\n[BBOX-2154] 10\n[BBOX-2155] 10\n[BBOX-2156] 10\n[BBOX-2157] 10\n[BBOX-2158] 10\n[BBOX-2159] 10\n[BBOX-2160] 10\n[BBOX-2161] 10\n[BBOX-2162] 10\n[BBOX-2163] 10\n[BBOX-2164] 10\n[BBOX-2165] 10\n[BBOX-2166] 10\n[BBOX-2167] 10\n[BBOX-2168] 10\n[BBOX-2169] 10\n[BBOX-2170] 10\n[BBOX-2171] 10\n[BBOX-2172] 10\n[BBOX-2173] 10\n[BBOX-2174] 10\n[BBOX-2175] 10\n[BBOX-2176] 10\n[BBOX-2177] 10\n[BBOX-2178] 10\n[BBOX-2179] 10\n[BBOX-2180] 10\n[BBOX-2181] 10\n[BBOX-2182] 10\n[BBOX-2183] 10\n[BBOX-2184] 10\n[BBOX-2185] 10\n[BBOX-2186] 10\n[BBOX-2187] 10\n[BBOX-2188] 10\n[BBOX-2189] 10\n[BBOX-2190] 10\n[BBOX-2191] 10\n[BBOX-2192] 10\n[BBOX-2193] 10\n[BBOX-2194] 10\n[BBOX-2195] 10\n[BBOX-2196] 10\n[BBOX-2197] 10\n[BBOX-2198] 10\n[BBOX-2199] 10\n[BBOX-2200] 10\n[BBOX-2201] 10\n[BBOX-2202] 10\n[BBOX-2203] 10\n[BBOX-2204] 10\n[BBOX-2205] 10\n[BBOX-2206] 10\n[BBOX-2207] 10\n[BBOX-2208] 10\n[BBOX-2209] 10\n[BBOX-2210] 10\n[BBOX-2211] 10\n[BBOX-2212] 10\n[BBOX-2213] 10\n[BBOX-2214] 10\n[BBOX-2215] 10\n[BBOX-2216] 10\n[BBOX-2217] 10\n[BBOX-2218] 10\n[BBOX-2219] 10\n[BBOX-2220] 10\n[BBOX-2221] 10\n[BBOX-2222] 10\n[BBOX-2223] 10\n[BBOX-2224] 10\n[BBOX-2225] 10\n[BBOX-2226] 10\n[BBOX-2227] 10\n[BBOX-2228] 10\n[BBOX-2229] 10\n[BBOX-2230] 10\n[BBOX-2231] 10\n[BBOX-2232] 10\n[BBOX-2233] 10\n[BBOX-2234] 10\n[BBOX-2235] 10\n[BBOX-2236] 10\n[BBOX-2237] 10\n[BBOX-2238] 10\n[BBOX-2239] 10\n[BBOX-2240] 10\n[BBOX-2241] 10\n[BBOX-2242] 10\n[BBOX-2243] 10\n[BBOX-2244] 10\n[BBOX-2245] 10\n[BBOX-2246] 10\n[BBOX-2247] 10\n[BBOX-2248] 10\n[BBOX-2249] 10\n[BBOX-2250] 10\n[BBOX-2251] 10\n[BBOX-2252] 10\n[BBOX-2253] 10\n[BBOX-2254] 10\n[BBOX-2255] 10\n[BBOX-2256] 10\n[BBOX-2257] 10\n[BBOX-2258] 10\n[BBOX-2259] 10\n[BBOX-2260] 10\n[BBOX-2261] 10\n[BBOX-2262] 10\n[BBOX-2263] 10\n[BBOX-2264] 10\n[BBOX-2265] 10\n[BBOX-2266] 10\n[BBOX-2267] 10\n[BBOX-2268] 10\n[BBOX-2269] 10\n[BBOX-2270] 10\n[BBOX-2271] 10\n[BBOX-2272] 10\n[BBOX-2273] 10\n[BBOX-2274] 10\n[BBOX-2275] 10\n[BBOX-2276] 10\n[BBOX-2277] 10\n[BBOX-2278] 10\n[BBOX-2279] 10\n[BBOX-2280] 10\n[BBOX-2281] 10\n[BBOX-2282] 10\n[BBOX-2283] 10\n[BBOX-2284] 10\n[BBOX-2285] 10\n[BBOX-2286] 10\n[BBOX-2287] 10\n[BBOX-2288] 10\n[BBOX-2289] 10\n[BBOX-2290] 10\n[BBOX-2291] 10\n[BBOX-2292] 10\n[BBOX-2293] 10\n[BBOX-2294] 10\n[BBOX-2295] 10\n[BBOX-2296] 10\n[BBOX-2297] 10\n[BBOX-2298] 10\n[BBOX-2299] 10\n[BBOX-2300] 10\n[BBOX-2301] 10\n[BBOX-2302] 10\n[BBOX-2303] 10\n[BBOX-2304] 10\n[BBOX-2305] 10\n[BBOX-2306] 10\n[BBOX-2307] 10\n[BBOX-2308] 10\n[BBOX-2309] 10\n[BBOX-2310] 10\n[BBOX-2311] 10\n[BBOX-2312] 10\n[BBOX-2313] 10\n[BBOX-2314] 10\n[BBOX-2315] 10\n[BBOX-2316] 10\n[BBOX-2317] 10\n[BBOX-2318] 10\n[BBOX-2319] 10\n[BBOX-2320] 10\n[BBOX-2321] 10\n[BBOX-2322] 10\n[BBOX-2323] 10\n[BBOX-2324] 10\n[BBOX-2325] 10\n[BBOX-2326] 10\n[BBOX-2327] 10\n[BBOX-2328] 10\n[BBOX-2329] 10\n[BBOX-2330] 10\n[BBOX-2331] 10\n[BBOX-2332] 10\n[BBOX-2333] 10\n[BBOX-2334] 10\n[BBOX-2335] 10\n[BBOX-2336] 10\n[BBOX-2337] 10\n[BBOX-2338] 10\n[BBOX-2339] 10\n[BBOX-2340] 10\n[BBOX-2341] 10\n[BBOX-2342] 10\n[BBOX-2343] 10\n[BBOX-2344] 10\n[BBOX-2345] 10\n[BBOX-2346] 10\n[BBOX-2347] 10\n[BBOX-2348] 10\n[BBOX-2349] 10\n[BBOX-2350] 10\n[BBOX-2351] 10\n[BBOX-2352] 10\n[BBOX-2353] 10\n[BBOX-2354] 10\n[BBOX-2355] 10\n[BBOX-2356] 10\n[BBOX-2357] 10\n[BBOX-2358] 10\n[BBOX-2359] 10\n[BBOX-2360] 10\n[BBOX-2361] 10\n[BBOX-2362] 10\n[BBOX-2363] 10\n[BBOX-2364] 10\n[BBOX-2365] 10\n[BBOX-2366] 10\n[BBOX-2367] 10\n[BBOX-2368] 10\n[BBOX-2369] 10\n[BBOX-2370] 10\n[BBOX-2371] 10\n[BBOX-2372] 10\n[BBOX-2373] 10\n[BBOX-2374] 10\n[BBOX-2375] 10\n[BBOX-2376] 10\n[BBOX-2377] 10\n[BBOX-2378] 10\n[BBOX-2379] 10\n[BBOX-2380] 10\n[BBOX-2381] 10\n[BBOX-2382] 10\n[BBOX-2383] 10\n[BBOX-2384] 10\n[BBOX-2385] 10\n[BBOX-2386] 10\n[BBOX-2387] 10\n[BBOX-2388] 10\n[BBOX-2389] 10\n[BBOX-2390] 10\n[BBOX-2391] 10\n[BBOX-2392] 10\n[BBOX-2393] 10\n[BBOX-2394] 10\n[BBOX-2395] 10\n[BBOX-2396] 10\n[BBOX-2397] 10\n[BBOX-2398] 10\n[BBOX-2399] 10\n[BBOX-2400] 10\n[BBOX-2401] 10\n[BBOX-2402] 10\n[BBOX-2403] 10\n[BBOX-2404] 10\n[BBOX-2405] 10\n[BBOX-2406] 10\n[BBOX-2407] 10\n[BBOX-2408] 10\n[BBOX-2409] 10\n[BBOX-2410] 10\n[BBOX-2411] 10\n[BBOX-2412] 10\n[BBOX-2413] 10\n[BBOX-2414] 10\n[BBOX-2415] 10\n[BBOX-2416] 10\n[BBOX-2417] 10\n[BBOX-2418] 10\n[BBOX-2419] 10\n[BBOX-2420] 10\n[BBOX-2421] 10\n[BBOX-2422] 10\n[BBOX-2423] 10\n[BBOX-2424] 10\n[BBOX-2425] 10\n[BBOX-2426] 10\n[BBOX-2427] 10\n[BBOX-2428] 10\n[BBOX-2429] 10\n[BBOX-2430] 10\n[BBOX-2431] 10\n[BBOX-2432] 10\n[BBOX-2433] 10\n[BBOX-2434] 10\n[BBOX-2435] 10\n[BBOX-2436] 10\n[BBOX-2437] 10\n[BBOX-2438] 10\n[BBOX-2439] 10\n[BBOX-2440] 10\n[BBOX-2441] 10\n[BBOX-2442] 10\n[BBOX-2443] 10\n[BBOX-2444] 10\n[BBOX-2445] 10\n[BBOX-2446] 10\n[BBOX-2447] 10\n[BBOX-2448] 10\n[BBOX-2449] 10\n[BBOX-2450] 10\n[BBOX-2451] 10\n[BBOX-2452] 10\n[BBOX-2453] 10\n[BBOX-2454] 10\n[BBOX-2455] 10\n[BBOX-2456] 10\n[BBOX-2457] 10\n[BBOX-2458] 10\n[BBOX-2459] 10\n[BBOX-2460] 10\n[BBOX-2461] 10\n[BBOX-2462] 10\n[BBOX-2463] 10\n[BBOX-2464] 10\n[BBOX-2465] 10\n[BBOX-2466] 10\n[BBOX-2467] 10\n[BBOX-2468] 10\n[BBOX-2469] 10\n[BBOX-2470] 10\n[BBOX-2471] 10\n[BBOX-2472] 10\n[BBOX-2473] 10\n[BBOX-2474] 10\n[BBOX-2475] 10\n[BBOX-2476] 10\n[BBOX-2477] 10\n[BBOX-2478] 10\n[BBOX-2479] 10\n[BBOX-2480] 10\n[BBOX-2481] 10\n[BBOX-2482] 10\n[BBOX-2483] 10\n[BBOX-2484] 10\n[BBOX-2485] 10\n[BBOX-2486] 10\n[BBOX-2487] 10\n[BBOX-2488] 10\n[BBOX-2489] 10\n[BBOX-2490] 10\n[BBOX-2491] 10\n[BBOX-2492] 10\n[BBOX-2493] 10\n[BBOX-2494] 10\n[BBOX-2495] 10\n[BBOX-2496] 10\n[BBOX-2497] 10\n[BBOX-2498] 10\n[BBOX-2499] 10\n[BBOX-2500] 10\n[BBOX-2501] 10\n[BBOX-2502] 10\n[BBOX-2503] 10\n[BBOX-2504] 10\n[BBOX-2505] 10\n[BBOX-2506] 10\n[BBOX-2507] 10\n[BBOX-2508] 10\n[BBOX-2509] 10\n[BBOX-2510] 10\n[BBOX-2511] 10\n[BBOX-2512] 10\n[BBOX-2513] 10\n[BBOX-2514] 10\n[BBOX-2515] 10\n[BBOX-2516] 10\n[BBOX-2517] 10\n[BBOX-2518] 10\n[BBOX-2519] 10\n[BBOX-2520] 10\n[BBOX-2521] 10\n[BBOX-2522] 10\n[BBOX-2523] 10\n[BBOX-2524] 10\n[BBOX-2525] 10\n[BBOX-2526] 10\n[BBOX-2527] 10\n[BBOX-2528] 10\n[BBOX-2529] 10\n[BBOX-2530] 10\n[BBOX-2531] 10\n[BBOX-2532] 10\n[BBOX-2533] 10\n[BBOX-2534] 10\n[BBOX-2535] 10\n[BBOX-2536] 10\n[BBOX-2537] 10\n[BBOX-2538] 10\n[BBOX-2539] 10\n[BBOX-2540] 10\n[BBOX-2541] 10\n[BBOX-2542] 10\n[BBOX-2543] 10\n[BBOX-2544] 10\n[BBOX-2545] 10\n[BBOX-2546] 10\n[BBOX-2547] 10\n[BBOX-2548] 10\n[BBOX-2549] 10\n[BBOX-2550] 10\n[BBOX-2551] 10\n[BBOX-2552] 10\n[BBOX-2553] 10\n[BBOX-2554] 10\n[BBOX-2555] 10\n[BBOX-2556] 10\n[BBOX-2557] 10\n[BBOX-2558] 10\n[BBOX-2559] 10\n[BBOX-2560] 10\n[BBOX-2561] 10\n[BBOX-2562] 10\n[BBOX-2563] 10\n[BBOX-2564] 10\n[BBOX-2565] 10\n[BBOX-2566] 10\n[BBOX-2567] 10\n[BBOX-2568] 10\n[BBOX-2569] 10\n[BBOX-2570] 10\n[BBOX-2571] 10\n[BBOX-2572] 10\n[BBOX-2573] 10\n[BBOX-2574] 10\n[BBOX-2575] 10\n[BBOX-2576] 10\n[BBOX-2577] 10\n[BBOX-2578] 10\n[BBOX-2579] 10\n[BBOX-2580] 10\n[BBOX-2581] 10\n[BBOX-2582] 10\n[BBOX-2583] 10\n[BBOX-2584] 10\n[BBOX-2585] 10\n[BBOX-2586] 10\n[BBOX-2587] 10\n[BBOX-2588] 10\n[BBOX-2589] 10\n[BBOX-2590] 10\n[BBOX-2591] 10\n[BBOX-2592] 10\n[BBOX-2593] 10\n[BBOX-2594] 10\n[BBOX-2595] 10\n[BBOX-2596] 10\n[BBOX-2597] 10\n[BBOX-2598] 10\n[BBOX-2599] 10\n[BBOX-2600] 10\n[BBOX-2601] 10\n[BBOX-2602] 10\n[BBOX-2603] 10\n[BBOX-2604] 10\n[BBOX-2605] 10\n[BBOX-2606] 10\n[BBOX-2607] 10\n[BBOX-2608] 10\n[BBOX-2609] 10\n[BBOX-2610] 10\n[BBOX-2611] 10\n[BBOX-2612] 10\n[BBOX-2613] 10\n[BBOX-2614] 10\n[BBOX-2615] 10\n[BBOX-2616] 10\n[BBOX-2617] 10\n[BBOX-2618] 10\n[BBOX-2619] 10\n[BBOX-2620] 10\n[BBOX-2621] 10\n[BBOX-2622] 10\n[BBOX-2623] 10\n[BBOX-2624] 10\n[BBOX-2625] 10\n[BBOX-2626] 10\n[BBOX-2627] 10\n[BBOX-2628] 10\n[BBOX-2629] 10\n[BBOX-2630] 10\n[BBOX-2631] 10\n[BBOX-2632] 10\n[BBOX-2633] 10\n[BBOX-2634] 10\n[BBOX-2635] 10\n[BBOX-2636] 10\n[BBOX-2637] 10\n[BBOX-2638] 10\n[BBOX-2639] 10\n[BBOX-2640] 10\n[BBOX-2641] 10\n[BBOX-2642] 10\n[BBOX-2643] 10\n[BBOX-2644] 10\n[BBOX-2645] 10\n[BBOX-2646] 10\n[BBOX-2647] 10\n[BBOX-2648] 10\n[BBOX-2649] 10\n[BBOX-2650] 10\n[BBOX-2651] 10\n[BBOX-2652] 10\n[BBOX-2653] 10\n[BBOX-2654] 10\n[BBOX-2655] 10\n[BBOX-2656] 10\n[BBOX-2657] 10\n[BBOX-2658] 10\n[BBOX-2659] 10\n[BBOX-2660] 10\n[BBOX-2661] 10\n[BBOX-2662] 10\n[BBOX-2663] 10\n[BBOX-2664] 10\n[BBOX-2665] 10\n[BBOX-2666] 10\n[BBOX-2667] 10\n[BBOX-2668] 10\n[BBOX-2669] 10\n[BBOX-2670] 10\n[BBOX-2671] 10\n[BBOX-2672] 10\n[BBOX-2673] 10\n[BBOX-2674] 10\n[BBOX-2675] 10\n[BBOX-2676] 10\n[BBOX-2677] 10\n[BBOX-2678] 10\n[BBOX-2679] 10\n[BBOX-2680] 10\n[BBOX-2681] 10\n[BBOX-2682] 10\n[BBOX-2683] 10\n[BBOX-2684] 10\n[BBOX-2685] 10\n[BBOX-2686] 10\n[BBOX-2687] 10\n[BBOX-2688] 10\n[BBOX-2689] 10\n[BBOX-2690] 10\n[BBOX-2691] 10\n[BBOX-2692] 10\n[BBOX-2693] 10\n[BBOX-2694] 10\n[BBOX-2695] 10\n[BBOX-2696] 10\n[BBOX-2697] 10\n[BBOX-2698] 10\n[BBOX-2699] 10\n[BBOX-2700] 10\n[BBOX-2701] 10\n[BBOX-2702] 10\n[BBOX-2703] 10\n[BBOX-2704] 10\n[BBOX-2705] 10\n[BBOX-2706] 10\n[BBOX-2707] 10\n[BBOX-2708] 10\n[BBOX-2709] 10\n[BBOX-2710] 10\n[BBOX-2711] 10\n[BBOX-2712] 10\n[BBOX-2713] 10\n[BBOX-2714] 10\n[BBOX-2715] 10\n[BBOX-2716] 10\n[BBOX-2717] 10\n[BBOX-2718] 10\n[BBOX-2719] 10\n[BBOX-2720] 10\n[BBOX-2721] 10\n[BBOX-2722] 10\n[BBOX-2723] 10\n[BBOX-2724] 10\n[BBOX-2725] 10\n[BBOX-2726] 10\n[BBOX-2727] 10\n[BBOX-2728] 10\n[BBOX-2729] 10\n[BBOX-2730] 10\n[BBOX-2731] 10\n[BBOX-2732] 10\n[BBOX-2733] 10\n[BBOX-2734] 10\n[BBOX-2735] 10\n[BBOX-2736] 10\n[BBOX-2737] 10\n[BBOX-2738] 10\n[BBOX-2739] 10\n[BBOX-2740] 10\n[BBOX-2741] 10\n[BBOX-2742] 10\n[BBOX-2743] 10\n[BBOX-2744] 10\n[BBOX-2745] 10\n[BBOX-2746] 10\n[BBOX-2747] 10\n[BBOX-2748] 10\n[BBOX-2749] 10\n[BBOX-2750] 10\n[BBOX-2751] 10\n[BBOX-2752] 10\n[BBOX-2753] 10\n[BBOX-2754] 10\n[BBOX-2755] 10\n[BBOX-2756] 10\n[BBOX-2757] 10\n[BBOX-2758] 10\n[BBOX-2759] 10\n[BBOX-2760] 10\n[BBOX-2761] 10\n[BBOX-2762] 10\n[BBOX-2763] 10\n[BBOX-2764] 10\n[BBOX-2765] 10\n[BBOX-2766] 10\n[BBOX-2767] 10\n[BBOX-2768] 10\n[BBOX-2769] 10\n[BBOX-2770] 10\n[BBOX-2771] 10\n[BBOX-2772] 10\n[BBOX-2773] 10\n[BBOX-2774] 10\n[BBOX-2775] 10\n[BBOX-2776] 10\n[BBOX-2777] 10\n[BBOX-2778] 10\n[BBOX-2779] 10\n[BBOX-2780] 10\n[BBOX-2781] 10\n[BBOX-2782] 10\n[BBOX-2783] 10\n[BBOX-2784] 10\n[BBOX-2785] 10\n[BBOX-2786] 10\n[BBOX-2787] 10\n[BBOX-2788] 10\n[BBOX-2789] 10\n[BBOX-2790] 10\n[BBOX-2791] 10\n[BBOX-2792] 10\n[BBOX-2793] 10\n[BBOX-2794] 10\n[BBOX-2795] 10\n[BBOX-2796] 10\n[BBOX-2797] 10\n[BBOX-2798] 10\n[BBOX-2799] 10\n[BBOX-2800] 10\n[BBOX-2801] 10\n[BBOX-2802] 10\n[BBOX-2803] 10\n[BBOX-2804] 10\n[BBOX-2805] 10\n[BBOX-2806] 10\n[BBOX-2807] 10\n[BBOX-2808] 10\n[BBOX-2809] 10\n[BBOX-2810] 10\n[BBOX-2811] 10\n[BBOX-2812] 10\n[BBOX-2813] 10\n[BBOX-2814] 10\n[BBOX-2815] 10\n[BBOX-2816] 10\n[BBOX-2817] 10\n[BBOX-2818] 10\n[BBOX-2819] 10\n[BBOX-2820] 10\n[BBOX-2821] 10\n[BBOX-2822] 10\n[BBOX-2823] 10\n[BBOX-2824] 10\n[BBOX-2825] 10\n[BBOX-2826] 10\n[BBOX-2827] 10\n[BBOX-2828] 10\n[BBOX-2829] 10\n[BBOX-2830] 10\n[BBOX-2831] 10\n[BBOX-2832] 10\n[BBOX-2833] 10\n[BBOX-2834] 10\n[BBOX-2835] 10\n[BBOX-2836] 10\n[BBOX-2837] 10\n[BBOX-2838] 10\n[BBOX-2839] 10\n[BBOX-2840] 10\n[BBOX-2841] 10\n[BBOX-2842] 10\n[BBOX-2843] 10\n[BBOX-2844] 10\n[BBOX-2845] 10\n[BBOX-2846] 10\n[BBOX-2847] 10\n[BBOX-2848] 10\n[BBOX-2849] 10\n[BBOX-2850] 10\n[BBOX-2851] 10\n[BBOX-2852] 10\n[BBOX-2853] 10\n[BBOX-2854] 10\n[BBOX-2855] 10\n[BBOX-2856] 10\n[BBOX-2857] 10\n[BBOX-2858] 10\n[BBOX-2859] 10\n[BBOX-2860] 10\n[BBOX-2861] 10\n[BBOX-2862] 10\n[BBOX-2863] 10\n[BBOX-2864] 10\n[BBOX-2865] 10\n[BBOX-2866] 10\n[BBOX-2867] 10\n[BBOX-2868] 10\n[BBOX-2869] 10\n[BBOX-2870] 10\n[BBOX-2871] 10\n[BBOX-2872] 10\n[BBOX-2873] 10\n[BBOX-2874] 10\n[BBOX-2875] 10\n[BBOX-2876] 10\n[BBOX-2877] 10\n[BBOX-2878] 10\n[BBOX-2879] 10\n[BBOX-2880] 10\n[BBOX-2881] 10\n[BBOX-2882] 10\n[BBOX-2883] 10\n[BBOX-2884] 10\n[BBOX-2885] 10\n[BBOX-2886] 10\n[BBOX-2887] 10\n[BBOX-2888] 10\n[BBOX-2889] 10\n[BBOX-2890] 10\n[BBOX-2891] 10\n[BBOX-2892] 10\n[BBOX-2893] 10\n[BBOX-2894] 10\n[BBOX-2895] 10\n[BBOX-2896] 10\n[BBOX-2897] 10\n[BBOX-2898] 10\n[BBOX-2899] 10\n[BBOX-2900] 10\n[BBOX-2901] 10\n[BBOX-2902] 10\n[BBOX-2903] 10\n[BBOX-2904] 10\n[BBOX-2905] 10\n[BBOX-2906] 10\n[BBOX-2907] 10\n[BBOX-2908] 10\n[BBOX-2909] 10\n[BBOX-2910] 10\n[BBOX-2911] 10\n[BBOX-2912] 10\n[BBOX-2913] 10\n[BBOX-2914] 10\n[BBOX-2915] 10\n[BBOX-2916] 10\n[BBOX-2917] 10\n[BBOX-2918] 10\n[BBOX-2919] 10\n[BBOX-2920] 10\n[BBOX-2921] 10\n[BBOX-2922] 10\n[BBOX-2923] 10\n[BBOX-2924] 10\n[BBOX-2925] 10\n[BBOX-2926] 10\n[BBOX-2927] 10\n[BBOX-2928] 10\n[BBOX-2929] 10\n[BBOX-2930] 10\n[BBOX-2931] 10\n[BBOX-2932] 10\n[BBOX-2933] 10\n[BBOX-2934] 10\n[BBOX-2935] 10\n[BBOX-2936] 10\n[BBOX-2937] 10\n[BBOX-2938] 10\n[BBOX-2939] 10\n[BBOX-2940] 10\n[BBOX-2941] 10\n[BBOX-2942] 10\n[BBOX-2943] 10\n[BBOX-2944] 10\n[BBOX-2945] 10\n[BBOX-2946] 10\n[BBOX-2947] 10\n[BBOX-2948] 10\n[BBOX-2949] 10\n[BBOX-2950] 10\n[BBOX-2951] 10\n[BBOX-2952] 10\n[BBOX-2953] 10\n[BBOX-2954] 10\n[BBOX-2955] 10\n[BBOX-2956] 10\n[BBOX-2957] 10\n[BBOX-2958] 10\n[BBOX-2959] 10\n[BBOX-2960] 10\n[BBOX-2961] 10\n[BBOX-2962] 10\n[BBOX-2963] 10\n[BBOX-2964] 10\n[BBOX-2965] 10\n[BBOX-2966] 10\n[BBOX-2967] 10\n[BBOX-2968] 10\n[BBOX-2969] 10\n[BBOX-2970] 10\n[BBOX-2971] 10\n[BBOX-2972] 10\n[BBOX-2973] 10\n[BBOX-2974] 10\n[BBOX-2975] 10\n[BBOX-2976] 10\n[BBOX-2977] 10\n[BBOX-2978] 10\n[BBOX-2979] 10\n[BBOX-2980] 10\n[BBOX-2981] 10\n[BBOX-2982] 10\n[BBOX-2983] 10\n[BBOX-2984] 10\n[BBOX-2985] 10\n[BBOX-2986] 10\n[BBOX-2987] 10\n[BBOX-2988] 10\n[BBOX-2989] 10\n[BBOX-2990] 10\n[BBOX-2991] 10\n[BBOX-2992] 10\n[BBOX-2993] 10\n[BBOX-2994] 10\n[BBOX-2995] 10\n[BBOX-2996] 10\n[BBOX-2997] 10\n[BBOX-2998] 10\n[BBOX-2999] 10\n[BBOX-3000] 10\n[BBOX-3001] 10\n[BBOX-3002] 10\n[BBOX-3003] 10\n[BBOX-3004] 10\n[BBOX-3005] 10\n[BBOX-3006] 10\n[BBOX-3007] 10\n[BBOX-3008] 10\n[BBOX-3009] 10\n[BBOX-3010] 10\n[BBOX-3011] 10\n[BBOX-3012] 10\n[BBOX-3013] 10\n[BBOX-3014] 10\n[BBOX-3015] 10\n[BBOX-3016] 10\n[BBOX-3017] 10\n[BBOX-3018] 10\n[BBOX-3019] 10\n[BBOX-3020] 10\n[BBOX-3021] 10\n[BBOX-3022] 10\n[BBOX-3023] 10\n[BBOX-3024] 10\n[BBOX-3025] 10\n[BBOX-3026] 10\n[BBOX-3027] 10\n[BBOX-3028] 10\n[BBOX-3029] 10\n[BBOX-3030] 10\n[BBOX-3031] 10\n[BBOX-3032] 10\n[BBOX-3033] 10\n[BBOX-3034] 10\n[BBOX-3035] 10\n[BBOX-3036] 10\n[BBOX-3037] 10\n[BBOX-3038] 10\n[BBOX-3039] 10\n[BBOX-3040] 10\n[BBOX-3041] 10\n[BBOX-3042] 10\n[BBOX-3043] 10\n[BBOX-3044] 10\n[BBOX-3045] 10\n[BBOX-3046] 10\n[BBOX-3047] 10\n[BBOX-3048] 10\n[BBOX-3049] 10\n[BBOX-3050] 10\n[BBOX-3051] 10\n[BBOX-3052] 10\n[BBOX-3053] 10\n[BBOX-3054] 10\n[BBOX-3055] 10\n[BBOX-3056] 10\n[BBOX-3057] 10\n[BBOX-3058] 10\n[BBOX-3059] 10\n[BBOX-3060] 10\n[BBOX-3061] 10\n[BBOX-3062] 10\n[BBOX-3063] 10\n[BBOX-3064] 10\n[BBOX-3065] 10\n[BBOX-3066] 10\n[BBOX-3067] 10\n[BBOX-3068] 10\n[BBOX-3069] 10\n[BBOX-3070] 10\n[BBOX-3071] 10\n[BBOX-3072] 10\n[BBOX-3073] 10\n[BBOX-3074] 10\n[BBOX-3075] 10\n[BBOX-3076] 10\n[BBOX-3077] 10\n[BBOX-3078] 10\n[BBOX-3079] 10\n[BBOX-3080] 10\n[BBOX-3081] 10\n[BBOX-3082] 10\n[BBOX-3083] 10\n[BBOX-3084] 10\n[BBOX-3085] 10\n[BBOX-3086] 10\n[BBOX-3087] 10\n[BBOX-3088] 10\n[BBOX-3089] 10\n[BBOX-3090] 10\n[BBOX-3091] 10\n[BBOX-3092] 10\n[BBOX-3093] 10\n[BBOX-3094] 10\n[BBOX-3095] 10\n[BBOX-3096] 10\n[BBOX-3097] 10\n[BBOX-3098] 10\n[BBOX-3099] 10\n[BBOX-3100] 10\n[BBOX-3101] 10\n[BBOX-3102] 10\n[BBOX-3103] 10\n[BBOX-3104] 10\n[BBOX-3105] 10\n[BBOX-3106] 10\n[BBOX-3107] 10\n[BBOX-3108] 10\n[BBOX-3109] 10\n[BBOX-3110] 10\n[BBOX-3111] 10\n[BBOX-3112] 10\n[BBOX-3113] 10\n[BBOX-3114] 10\n[BBOX-3115] 10\n[BBOX-3116] 10\n[BBOX-3117] 10\n[BBOX-3118] 10\n[BBOX-3119] 10\n[BBOX-3120] 10\n[BBOX-3121] 10\n[BBOX-3122] 10\n[BBOX-3123] 10\n[BBOX-3124] 10\n[BBOX-3125] 10\n[BBOX-3126] 10\n[BBOX-3127] 10\n[BBOX-3128] 10\n[BBOX-3129] 10\n[BBOX-3130] 10\n[BBOX-3131] 10\n[BBOX-3132] 10\n[BBOX-3133] 10\n[BBOX-3134] 10\n[BBOX-3135] 10\n[BBOX-3136] 10\n[BBOX-3137] 10\n[BBOX-3138] 10\n[BBOX-3139] 10\n[BBOX-3140] 10\n[BBOX-3141] 10\n[BBOX-3142] 10\n[BBOX-3143] 10\n[BBOX-3144] 10\n[BBOX-3145] 10\n[BBOX-3146] 10\n[BBOX-3147] 10\n[BBOX-3148] 10\n[BBOX-3149] 10\n[BBOX-3150] 10\n[BBOX-3151] 10\n[BBOX-3152] 10\n[BBOX-3153] 10\n[BBOX-3154] 10\n[BBOX-3155] 10\n[BBOX-3156] 10\n[BBOX-3157] 10\n[BBOX-3158] 10\n[BBOX-3159] 10\n[BBOX-3160] 10\n[BBOX-3161] 10\n[BBOX-3162] 10\n[BBOX-3163] 10\n[BBOX-3164] 10\n[BBOX-3165] 10\n[BBOX-3166] 10\n[BBOX-3167] 10\n[BBOX-3168] 10\n[BBOX-3169] 10\n[BBOX-3170] 10\n[BBOX-3171] 10\n[BBOX-3172] 10\n[BBOX-3173] 10\n[BBOX-3174] 10\n[BBOX-3175] 10\n[BBOX-3176] 10\n[BBOX-3177] 10\n[BBOX-3178] 10\n[BBOX-3179] 10\n[BBOX-3180] 10\n[BBOX-3181] 10\n[BBOX-3182] 10\n[BBOX-3183] 10\n[BBOX-3184] 10\n[BBOX-3185] 10\n[BBOX-3186] 10\n[BBOX-3187] 10\n[BBOX-3188] 10\n[BBOX-3189] 10\n[BBOX-3190] 10\n[BBOX-3191] 10\n[BBOX-3192] 10\n[BBOX-3193] 10\n[BBOX-3194] 10\n[BBOX-3195] 10\n[BBOX-3196] 10\n[BBOX-3197] 10\n[BBOX-3198] 10\n[BBOX-3199] 10\n[BBOX-3200] 10\n[BBOX-3201] 10\n[BBOX-3202] 10\n[BBOX-3203] 10\n[BBOX-3204] 10\n[BBOX-3205] 10\n[BBOX-3206] 10\n[BBOX-3207] 10\n[BBOX-3208] 10\n[BBOX-3209] 10\n[BBOX-3210] 10\n[BBOX-3211] 10\n[BBOX-3212] 10\n[BBOX-3213] 10\n[BBOX-3214] 10\n[BBOX-3215] 10\n[BBOX-3216] 10\n[BBOX-3217] 10\n[BBOX-3218] 10\n[BBOX-3219] 10\n[BBOX-3220] 10\n[BBOX-3221] 10\n[BBOX-3222] 10\n[BBOX-3223] 10\n[BBOX-3224] 10\n[BBOX-3225] 10\n[BBOX-3226] 10\n[BBOX-3227] 10\n[BBOX-3228] 10\n[BBOX-3229] 10\n[BBOX-3230] 10\n[BBOX-3231] 10\n[BBOX-3232] 10\n[BBOX-3233] 10\n[BBOX-3234] 10\n[BBOX-3235] 10\n[BBOX-3236] 10\n[BBOX-3237] 10\n[BBOX-3238] 10\n[BBOX-3239] 10\n[BBOX-3240] 10\n[BBOX-3241] 10\n[BBOX-3242] 10\n[BBOX-3243] 10\n[BBOX-3244] 10\n[BBOX-3245] 10\n[BBOX-3246] 10\n[BBOX-3247] 10\n[BBOX-3248] 10\n[BBOX-3249] 10\n[BBOX-3250] 10\n[BBOX-3251] 10\n[BBOX-3252] 10\n[BBOX-3253] 10\n[BBOX-3254] 10\n[BBOX-3255] 10\n[BBOX-3256] 10\n[BBOX-3257] 10\n[BBOX-3258] 10\n[BBOX-3259] 10\n[BBOX-3260] 10\n[BBOX-3261] 10\n[BBOX-3262] 10\n[BBOX-3263] 10\n[BBOX-3264] 10\n[BBOX-3265] 10\n[BBOX-3266] 10\n[BBOX-3267] 10\n[BBOX-3268] 10\n[BBOX-3269] 10\n[BBOX-3270] 10\n[BBOX-3271] 10\n[BBOX-3272] 10\n[BBOX-3273] 10\n[BBOX-3274] 10\n[BBOX-3275] 10\n[BBOX-3276] 10\n[BBOX-3277] 10\n[BBOX-3278] 10\n[BBOX-3279] 10\n[BBOX-3280] 10\n[BBOX-3281] 10\n[BBOX-3282] 10\n[BBOX-3283] 10\n[BBOX-3284] 10\n[BBOX-3285] 10\n[BBOX-3286] 10\n[BBOX-3287] 10\n[BBOX-3288] 10\n[BBOX-3289] 10\n[BBOX-3290] 10\n[BBOX-3291] 10\n[BBOX-3292] 10\n[BBOX-3293] 10\n[BBOX-3294] 10\n[BBOX-3295] 10\n[BBOX-3296] 10\n[BBOX-3297] 10\n[BBOX-3298] 10\n[BBOX-3299] 10\n[BBOX-3300] 10\n[BBOX-3301] 10\n[BBOX-3302] 10\n[BBOX-3303] 10\n[BBOX-3304] 10\n[BBOX-3305] 10\n[BBOX-3306] 10\n[BBOX-3307] 10\n[BBOX-3308] 10\n[BBOX-3309] 10\n[BBOX-3310] 10\n[BBOX-3311] 10\n[BBOX-3312] 10\n[BBOX-3313] 10\n[BBOX-3314] 10\n[BBOX-3315] 10\n[BBOX-3316] 10\n[BBOX-3317] 10\n[BBOX-3318] 10\n[BBOX-3319] 10\n[BBOX-3320] 10\n[BBOX-3321] 10\n[BBOX-3322] 10\n[BBOX-3323] 10\n[BBOX-3324] 10\n[BBOX-3325] 10\n[BBOX-3326] 10\n[BBOX-3327] 10\n[BBOX-3328] 10\n[BBOX-3329] 10\n[BBOX-3330] 10\n[BBOX-3331] 10\n[BBOX-3332] 10\n[BBOX-3333] 10\n[BBOX-3334] 10\n[BBOX-3335] 10\n[BBOX-3336] 10\n[BBOX-3337] 10\n[BBOX-3338] 10\n[BBOX-3339] 10\n[BBOX-3340] 10\n[BBOX-3341] 10\n[BBOX-3342] 10\n[BBOX-3343] 10\n[BBOX-3344] 10\n[BBOX-3345] 10\n[BBOX-3346] 10\n[BBOX-3347] 10\n[BBOX-3348] 10\n[BBOX-3349] 10\n[BBOX-3350] 10\n[BBOX-3351] 10\n[BBOX-3352] 10\n[BBOX-3353] 10\n[BBOX-3354] 10\n[BBOX-3355] 10\n[BBOX-3356] 10\n[BBOX-3357] 10\n[BBOX-3358] 10\n[BBOX-3359] 10\n[BBOX-3360] 10\n[BBOX-3361] 10\n[BBOX-3362] 10\n[BBOX-3363] 10\n[BBOX-3364] 10\n[BBOX-3365] 10\n[BBOX-3366] 10\n[BBOX-3367] 10\n[BBOX-3368] 10\n[BBOX-3369] 10\n[BBOX-3370] 10\n[BBOX-3371] 10\n[BBOX-3372] 10\n[BBOX-3373] 10\n[BBOX-3374] 10\n[BBOX-3375] 10\n[BBOX-3376] 10\n[BBOX-3377] 10\n[BBOX-3378] 10\n[BBOX-3379] 10\n[BBOX-3380] 10\n[BBOX-3381] 10\n[BBOX-3382] 10\n[BBOX-3383] 10\n[BBOX-3384] 10\n[BBOX-3385] 10\n[BBOX-3386] 10\n[BBOX-3387] 10\n[BBOX-3388] 10\n[BBOX-3389] 10\n[BBOX-3390] 10\n[BBOX-3391] 10\n[BBOX-3392] 10\n[BBOX-3393] 10\n[BBOX-3394] 10\n[BBOX-3395] 10\n[BBOX-3396] 10\n[BBOX-3397] 10\n[BBOX-3398] 10\n[BBOX-3399] 10\n[BBOX-3400] 10\n[BBOX-3401] 10\n[BBOX-3402] 10\n[BBOX-3403] 10\n[BBOX-3404] 10\n[BBOX-3405] 10\n[BBOX-3406] 10\n[BBOX-3407] 10\n[BBOX-3408] 10\n[BBOX-3409] 10\n[BBOX-3410] 10\n[BBOX-3411] 10\n[BBOX-3412] 10\n[BBOX-3413] 10\n[BBOX-3414] 10\n[BBOX-3415] 10\n[BBOX-3416] 10\n[BBOX-3417] 10\n[BBOX-3418] 10\n[BBOX-3419] 10\n[BBOX-3420] 10\n[BBOX-3421] 10\n[BBOX-3422] 10\n[BBOX-3423] 10\n[BBOX-3424] 10\n[BBOX-3425] 10\n[BBOX-3426] 10\n[BBOX-3427] 10\n[BBOX-3428] 10\n[BBOX-3429] 10\n[BBOX-3430] 10\n[BBOX-3431] 10\n[BBOX-3432] 10\n[BBOX-3433] 10\n[BBOX-3434] 10\n[BBOX-3435] 10\n[BBOX-3436] 10\n[BBOX-3437] 10\n[BBOX-3438] 10\n[BBOX-3439] 10\n[BBOX-3440] 10\n[BBOX-3441] 10\n[BBOX-3442] 10\n[BBOX-3443] 10\n[BBOX-3444] 10\n[BBOX-3445] 10\n[BBOX-3446] 10\n[BBOX-3447] 10\n[BBOX-3448] 10\n[BBOX-3449] 10\n[BBOX-3450] 10\n[BBOX-3451] 10\n[BBOX-3452] 10\n[BBOX-3453] 10\n[BBOX-3454] 10\n[BBOX-3455] 10\n[BBOX-3456] 10\n[BBOX-3457] 10\n[BBOX-3458] 10\n[BBOX-3459] 10\n[BBOX-3460] 10\n[BBOX-3461] 10\n[BBOX-3462] 10\n[BBOX-3463] 10\n[BBOX-3464] 10\n[BBOX-3465] 10\n[BBOX-3466] 10\n[BBOX-3467] 10\n[BBOX-3468] 10\n[BBOX-3469] 10\n[BBOX-3470] 10\n[BBOX-3471] 10\n[BBOX-3472] 10\n[BBOX-3473] 10\n[BBOX-3474] 10\n[BBOX-3475] 10\n[BBOX-3476] 10\n[BBOX-3477] 10\n[BBOX-3478] 10\n[BBOX-3479] 10\n[BBOX-3480] 10\n[BBOX-3481] 10\n[BBOX-3482] 10\n[BBOX-3483] 10\n[BBOX-3484] 10\n[BBOX-3485] 10\n[BBOX-3486] 10\n[BBOX-3487] 10\n[BBOX-3488] 10\n[BBOX-3489] 10\n[BBOX-3490] 10\n[BBOX-3491] 10\n[BBOX-3492] 10\n[BBOX-3493] 10\n[BBOX-3494] 10\n[BBOX-3495] 10\n[BBOX-3496] 10\n[BBOX-3497] 10\n[BBOX-3498] 10\n[BBOX-3499] 10\n[BBOX-3500] 10\n[BBOX-3501] 10\n[BBOX-3502] 10\n[BBOX-3503] 10\n[BBOX-3504] 10\n[BBOX-3505] 10\n[BBOX-3506] 10\n[BBOX-3507] 10\n[BBOX-3508] 10\n[BBOX-3509] 10\n[BBOX-3510] 10\n[BBOX-3511] 10\n[BBOX-3512] 10\n[BBOX-3513] 10\n[BBOX-3514] 10\n[BBOX-3515] 10\n[BBOX-3516] 10\n[BBOX-3517] 10\n[BBOX-3518] 10\n[BBOX-3519] 10\n[BBOX-3520] 10\n[BBOX-3521] 10\n[BBOX-3522] 10\n[BBOX-3523] 10\n[BBOX-3524] 10\n[BBOX-3525] 10\n[BBOX-3526] 10\n[BBOX-3527] 10\n[BBOX-3528] 10\n[BBOX-3529] 10\n[BBOX-3530] 10\n[BBOX-3531] 10\n[BBOX-3532] 10\n[BBOX-3533] 10\n[BBOX-3534] 10\n[BBOX-3535] 10\n[BBOX-3536] 10\n[BBOX-3537] 10\n[BBOX-3538] 10\n[BBOX-3539] 10\n[BBOX-3540] 10\n[BBOX-3541] 10\n[BBOX-3542] 10\n[BBOX-3543] 10\n[BBOX-3544] 10\n[BBOX-3545] 10\n[BBOX-3546] 10\n[BBOX-3547] 10\n[BBOX-3548] 10\n[BBOX-3549] 10\n[BBOX-3550] 10\n[BBOX-3551] 10\n[BBOX-3552] 10\n[BBOX-3553] 10\n[BBOX-3554] 10\n[BBOX-3555] 10\n[BBOX-3556] 10\n[BBOX-3557] 10\n[BBOX-3558] 10\n[BBOX-3559] 10\n[BBOX-3560] 10\n[BBOX-3561] 10\n[BBOX-3562] 10\n[BBOX-3563] 10\n[BBOX-3564] 10\n[BBOX-3565] 10\n[BBOX-3566] 10\n[BBOX-3567] 10\n[BBOX-3568] 10\n[BBOX-3569] 10\n[BBOX-3570] 10\n[BBOX-3571] 10\n[BBOX-3572] 10\n[BBOX-3573] 10\n[BBOX-3574] 10\n[BBOX-3575] 10\n[BBOX-3576] 10\n[BBOX-3577] 10\n[BBOX-3578] 10\n[BBOX-3579] 10\n[BBOX-3580] 10\n[BBOX-3581] 10\n[BBOX-3582] 10\n[BBOX-3583] 10\n[BBOX-3584] 10\n[BBOX-3585] 10\n[BBOX-3586] 10\n[BBOX-3587] 10\n[BBOX-3588] 10\n[BBOX-3589] 10\n[BBOX-3590] 10\n[BBOX-3591] 10\n[BBOX-3592] 10\n[BBOX-3593] 10\n[BBOX-3594] 10\n[BBOX-3595] 10\n[BBOX-3596] 10\n[BBOX-3597] 10\n[BBOX-3598] 10\n[BBOX-3599] 10\n[BBOX-3600] 10\n[BBOX-3601] 10\n[BBOX-3602] 10\n[BBOX-3603] 10\n[BBOX-3604] 10\n[BBOX-3605] 10\n[BBOX-3606] 10\n[BBOX-3607] 10\n[BBOX-3608] 10\n[BBOX-3609] 10\n[BBOX-3610] 10\n[BBOX-3611] 10\n[BBOX-3612] 10\n[BBOX-3613] 10\n[BBOX-3614] 10\n[BBOX-3615] 10\n[BBOX-3616] 10\n[BBOX-3617] 10\n[BBOX-3618] 10\n[BBOX-3619] 10\n[BBOX-3620] 10\n[BBOX-3621] 10\n[BBOX-3622] 10\n[BBOX-3623] 10\n[BBOX-3624] 10\n[BBOX-3625] 10\n[BBOX-3626] 10\n[BBOX-3627] 10\n[BBOX-3628] 10\n[BBOX-3629] 10\n[BBOX-3630] 10\n[BBOX-3631] 10\n[BBOX-3632] 10\n[BBOX-3633] 10\n[BBOX-3634] 10\n[BBOX-3635] 10\n[BBOX-3636] 10\n[BBOX-3637] 10\n[BBOX-3638] 10\n[BBOX-3639] 10\n[BBOX-3640] 10\n[BBOX-3641] 10\n[BBOX-3642] 10\n[BBOX-3643] 10\n[BBOX-3644] 10\n[BBOX-3645] 10\n[BBOX-3646] 10\n[BBOX-3647] 10\n[BBOX-3648] 10\n[BBOX-3649] 10\n[BBOX-3650] 10\n[BBOX-3651] 10\n[BBOX-3652] 10\n[BBOX-3653] 10\n[BBOX-3654] 10\n[BBOX-3655] 10\n[BBOX-3656] 10\n[BBOX-3657] 10\n[BBOX-3658] 10\n[BBOX-3659] 10\n[BBOX-3660] 10\n[BBOX-3661] 10\n[BBOX-3662] 10\n[BBOX-3663] 10\n[BBOX-3664] 10\n[BBOX-3665] 10\n[BBOX-3666] 10\n[BBOX-3667] 10\n[BBOX-3668] 10\n[BBOX-3669] 10\n[BBOX-3670] 10\n[BBOX-3671] 10\n[BBOX-3672] 10\n[BBOX-3673] 10\n[BBOX-3674] 10\n[BBOX-3675] 10\n[BBOX-3676] 10\n[BBOX-3677] 10\n[BBOX-3678] 10\n[BBOX-3679] 10\n[BBOX-3680] 10\n[BBOX-3681] 10\n[BBOX-3682] 10\n[BBOX-3683] 10\n[BBOX-3684] 10\n[BBOX-3685] 10\n[BBOX-3686] 10\n[BBOX-3687] 10\n[BBOX-3688] 10\n[BBOX-3689] 10\n[BBOX-3690] 10\n[BBOX-3691] 10\n[BBOX-3692] 10\n[BBOX-3693] 10\n[BBOX-3694] 10\n[BBOX-3695] 10\n[BBOX-3696] 10\n[BBOX-3697] 10\n[BBOX-3698] 10\n[BBOX-3699] 10\n[BBOX-3700] 10\n[BBOX-3701] 10\n[BBOX-3702] 10\n[BBOX-3703] 10\n[BBOX-3704] 10\n[BBOX-3705] 10\n[BBOX-3706] 10\n[BBOX-3707] 10\n[BBOX-3708] 10\n[BBOX-3709] 10\n[BBOX-3710] 10\n[BBOX-3711] 10\n[BBOX-3712] 10\n[BBOX-3713] 10\n[BBOX-3714] 10\n[BBOX-3715] 10\n[BBOX-3716] 10\n[BBOX-3717] 10\n[BBOX-3718] 10\n[BBOX-3719] 10\n[BBOX-3720] 10\n[BBOX-3721] 10\n[BBOX-3722] 10\n[BBOX-3723] 10\n[BBOX-3724] 10\n[BBOX-3725] 10\n[BBOX-3726] 10\n[BBOX-3727] 10\n[BBOX-3728] 10\n[BBOX-3729] 10\n[BBOX-3730] 10\n[BBOX-3731] 10\n[BBOX-3732] 10\n[BBOX-3733] 10\n[BBOX-3734] 10\n[BBOX-3735] 10\n[BBOX-3736] 10\n[BBOX-3737] 10\n[BBOX-3738] 10\n[BBOX-3739] 10\n[BBOX-3740] 10\n[BBOX-3741] 10\n[BBOX-3742] 10\n[BBOX-3743] 10\n[BBOX-3744] 10\n[BBOX-3745] 10\n[BBOX-3746] 10\n[BBOX-3747] 10\n[BBOX-3748] 10\n[BBOX-3749] 10\n[BBOX-3750] 10\n[BBOX-3751] 10\n[BBOX-3752] 10\n[BBOX-3753] 10\n[BBOX-3754] 10\n[BBOX-3755] 10\n[BBOX-3756] 10\n[BBOX-3757] 10\n[BBOX-3758] 10\n[BBOX-3759] 10\n[BBOX-3760] 10\n[BBOX-3761] 10\n[BBOX-3762] 10\n[BBOX-3763] 10\n[BBOX-3764] 10\n[BBOX-3765] 10\n[BBOX-3766] 10\n[BBOX-3767] 10\n[BBOX-3768] 10\n[BBOX-3769] 10\n[BBOX-3770] 10\n[BBOX-3771] 10\n[BBOX-3772] 10\n[BBOX-3773] 10\n[BBOX-3774] 10\n[BBOX-3775] 10\n[BBOX-3776] 10\n[BBOX-3777] 10\n[BBOX-3778] 10\n[BBOX-3779] 10\n[BBOX-3780] 10\n[BBOX-3781] 10\n[BBOX-3782] 10\n[BBOX-3783] 10\n[BBOX-3784] 10\n[BBOX-3785] 10\n[BBOX-3786] 10\n[BBOX-3787] 10\n[BBOX-3788] 10\n[BBOX-3789] 10\n[BBOX-3790] 10\n[BBOX-3791] 10\n[BBOX-3792] 10\n[BBOX-3793] 10\n[BBOX-3794] 10\n[BBOX-3795] 10\n[BBOX-3796] 10\n[BBOX-3797] 10\n[BBOX-3798] 10\n[BBOX-3799] 10\n[BBOX-3800] 10\n[BBOX-3801] 10\n[BBOX-3802] 10\n[BBOX-3803] 10\n[BBOX-3804] 10\n[BBOX-3805] 10\n[BBOX-3806] 10\n[BBOX-3807] 10\n[BBOX-3808] 10\n[BBOX-3809] 10\n[BBOX-3810] 10\n[BBOX-3811] 10\n[BBOX-3812] 10\n[BBOX-3813] 10\n[BBOX-3814] 10\n[BBOX-3815] 10\n[BBOX-3816] 10\n[BBOX-3817] 10\n[BBOX-3818] 10\n[BBOX-3819] 10\n[BBOX-3820] 10\n[BBOX-3821] 10\n[BBOX-3822] 10\n[BBOX-3823] 10\n[BBOX-3824] 10\n[BBOX-3825] 10\n[BBOX-3826] 10\n[BBOX-3827] 10\n[BBOX-3828] 10\n[BBOX-3829] 10\n[BBOX-3830] 10\n[BBOX-3831] 10\n[BBOX-3832] 10\n[BBOX-3833] 10\n[BBOX-3834] 10\n[BBOX-3835] 10\n[BBOX-3836] 10\n[BBOX-3837] 10\n[BBOX-3838] 10\n[BBOX-3839] 10\n[BBOX-3840] 10\n[BBOX-3841] 10\n[BBOX-3842] 10\n[BBOX-3843] 10\n[BBOX-3844] 10\n[BBOX-3845] 10\n[BBOX-3846] 10\n[BBOX-3847] 10\n[BBOX-3848] 10\n[BBOX-3849] 10\n[BBOX-3850] 10\n[BBOX-3851] 10\n[BBOX-3852] 10\n[BBOX-3853] 10\n[BBOX-3854] 10\n[BBOX-3855] 10\n[BBOX-3856] 10\n[BBOX-3857] 10\n[BBOX-3858] 10\n[BBOX-3859] 10\n[BBOX-3860] 10\n[BBOX-3861] 10\n[BBOX-3862] 10\n[BBOX-3863] 10\n[BBOX-3864] 10\n[BBOX-3865] 10\n[BBOX-3866] 10\n[BBOX-3867] 10\n[BBOX-3868] 10\n[BBOX-3869] 10\n[BBOX-3870] 10\n[BBOX-3871] 10\n[BBOX-3872] 10\n[BBOX-3873] 10\n[BBOX-3874] 10\n[BBOX-3875] 10\n[BBOX-3876] 10\n[BBOX-3877] 10\n[BBOX-3878] 10\n[BBOX-3879] 10\n[BBOX-3880] 10\n[BBOX-3881] 10\n[BBOX-3882] 10\n[BBOX-3883] 10\n[BBOX-3884] 10\n[BBOX-3885] 10\n[BBOX-3886] 10\n[BBOX-3887] 10\n[BBOX-3888] 10\n[BBOX-3889] 10\n[BBOX-3890] 10\n[BBOX-3891] 10\n[BBOX-3892] 10\n[BBOX-3893] 10\n[BBOX-3894] 10\n[BBOX-3895] 10\n[BBOX-3896] 10\n[BBOX-3897] 10\n[BBOX-3898] 10\n[BBOX-3899] 10\n[BBOX-3900] 10\n[BBOX-3901] 10\n[BBOX-3902] 10\n[BBOX-3903] 10\n[BBOX-3904] 10\n[BBOX-3905] 10\n[BBOX-3906] 10\n[BBOX-3907] 10\n[BBOX-3908] 10\n[BBOX-3909] 10\n[BBOX-3910] 10\n[BBOX-3911] 10\n[BBOX-3912] 10\n[BBOX-3913] 10\n[BBOX-3914] 10\n[BBOX-3915] 10\n[BBOX-3916] 10\n[BBOX-3917] 10\n[BBOX-3918] 10\n[BBOX-3919] 10\n[BBOX-3920] 10\n[BBOX-3921] 10\n[BBOX-3922] 10\n[BBOX-3923] 10\n[BBOX-3924] 10\n[BBOX-3925] 10\n[BBOX-3926] 10\n[BBOX-3927] 10\n[BBOX-3928] 10\n[BBOX-3929] 10\n[BBOX-3930] 10\n[BBOX-3931] 10\n[BBOX-3932] 10\n[BBOX-3933] 10\n[BBOX-3934] 10\n[BBOX-3935] 10\n[BBOX-3936] 10\n[BBOX-3937] 10\n[BBOX-3938] 10\n[BBOX-3939] 10\n[BBOX-3940] 10\n[BBOX-3941] 10\n[BBOX-3942] 10\n[BBOX-3943] 10\n[BBOX-3944] 10\n[BBOX-3945] 10\n[BBOX-3946] 10\n[BBOX-3947] 10\n[BBOX-3948] 10\n[BBOX-3949] 10\n[BBOX-3950] 10\n[BBOX-3951] 10\n[BBOX-3952] 10\n[BBOX-3953] 10\n[BBOX-3954] 10\n[BBOX-3955] 10\n[BBOX-3956] 10\n[BBOX-3957] 10\n[BBOX-3958] 10\n[BBOX-3959] 10\n[BBOX-3960] 10\n[BBOX-3961] 10\n[BBOX-3962] 10\n[BBOX-3963] 10\n[BBOX-3964] 10\n[BBOX-3965] 10\n[BBOX-3966] 10\n[BBOX-3967] 10\n[BBOX-3968] 10\n[BBOX-3969] 10\n[BBOX-3970] 10\n[BBOX-3971] 10\n[BBOX-3972] 10\n[BBOX-3973] 10\n[BBOX-3974] 10\n[BBOX-3975] 10\n[BBOX-3976] 10\n[BBOX-3977] 10\n[BBOX-3978] 10\n[BBOX-3979] 10\n[BBOX-3980] 10\n[BBOX-3981] 10\n[BBOX-3982] 10\n[BBOX-3983] 10\n[BBOX-3984] 10\n[BBOX-3985] 10\n[BBOX-3986] 10\n[BBOX-3987] 10\n[BBOX-3988] 10\n[BBOX-3989] 10\n[BBOX-3990] 10\n[BBOX-3991] 10\n[BBOX-3992] 10\n[BBOX-3993] 10\n[BBOX-3994] 10\n[BBOX-3995] 10\n[BBOX-3996] 10\n[BBOX-3997] 10\n[BBOX-3998] 10\n[BBOX-3999] 10\n[BBOX-4000] 10\n[BBOX-4001] 10\n[BBOX-4002] 10\n[BBOX-4003] 10\n[BBOX-4004] 10\n[BBOX-4005] 10\n[BBOX-4006] 10\n[BBOX-4007] 10\n[BBOX-4008] 10\n[BBOX-4009] 10\n[BBOX-4010] 10\n[BBOX-4011] 10\n[BBOX-4012] 10\n[BBOX-4013] 10\n[BBOX-4014] 10\n[BBOX-4015] 10\n[BBOX-4016] 10\n[BBOX-4017] 10\n[BBOX-4018] 10\n[BBOX-4019] 10\n[BBOX-4020] 10\n[BBOX-4021] 10\n[BBOX-4022] 10\n[BBOX-4023] 10\n[BBOX-4024] 10\n[BBOX-4025] 10\n[BBOX-4026] 10\n[BBOX-4027] 10\n[BBOX-4028] 10\n[BBOX-4029] 10\n[BBOX-4030] 10\n[BBOX-4031] 10\n[BBOX-4032] 10\n[BBOX-4033] 10\n[BBOX-4034] 10\n[BBOX-4035] 10\n[BBOX-4036] 10\n[BBOX-4037] 10\n[BBOX-4038] 10\n[BBOX-4039] 10\n[BBOX-4040] 10\n[BBOX-4041] 10\n[BBOX-4042] 10\n[BBOX-4043] 10\n[BBOX-4044] 10\n[BBOX-4045] 10\n[BBOX-4046] 10\n[BBOX-4047] 10\n[BBOX-4048] 10\n[BBOX-4049] 10\n[BBOX-4050] 10\n[BBOX-4051] 10\n[BBOX-4052] 10\n[BBOX-4053] 10\n[BBOX-4054] 10\n[BBOX-4055] 10\n[BBOX-4056] 10\n[BBOX-4057] 10\n[BBOX-4058] 10\n[BBOX-4059] 10\n[BBOX-4060] 10\n[BBOX-4061] 10\n[BBOX-4062] 10\n[BBOX-4063] 10\n[BBOX-4064] 10\n[BBOX-4065] 10\n[BBOX-4066] 10\n[BBOX-4067] 10\n[BBOX-4068] 10\n[BBOX-4069] 10\n[BBOX-4070] 10\n[BBOX-4071] 10\n[BBOX-4072] 10\n[BBOX-4073] 10\n[BBOX-4074] 10\n[BBOX-4075] 10\n[BBOX-4076] 10\n[BBOX-4077] 10\n[BBOX-4078] 10\n[BBOX-4079] 10\n[BBOX-4080] 10\n[BBOX-4081] 10\n[BBOX-4082] 10\n[BBOX-4083] 10\n[BBOX-4084] 10\n[BBOX-4085] 10\n[BBOX-4086] 10\n[BBOX-4087] 10\n[BBOX-4088] 10\n[BBOX-4089] 10\n[BBOX-4090] 10\n[BBOX-4091] 10\n[BBOX-4092] 10\n[BBOX-4093] 10\n[BBOX-4094] 10\n[BBOX-4095] 10\n[BBOX-4096] 10\n[BBOX-4097] 10\n[BBOX-4098] 10\n[BBOX-4099] 10\n[BBOX-4100] 10\n[BBOX-4101] 10\n[BBOX-4102] 10\n[BBOX-4103] 10\n[BBOX-4104] 10\n[BBOX-4105] 10\n[BBOX-4106] 10\n[BBOX-4107] 10\n[BBOX-4108] 10\n[BBOX-4109] 10\n[BBOX-4110] 10\n[BBOX-4111] 10\n[BBOX-4112] 10\n[BBOX-4113] 10\n[BBOX-4114] 10\n[BBOX-4115] 10\n[BBOX-4116] 10\n[BBOX-4117] 10\n[BBOX-4118] 10\n[BBOX-4119] 10\n[BBOX-4120] 10\n[BBOX-4121] 10\n[BBOX-4122] 10\n[BBOX-4123] 10\n[BBOX-4124] 10\n[BBOX-4125] 10\n[BBOX-4126] 10\n[BBOX-4127] 10\n[BBOX-4128] 10\n[BBOX-4129] 10\n[BBOX-4130] 10\n[BBOX-4131] 10\n[BBOX-4132] 10\n[BBOX-4133] 10\n[BBOX-4134] 10\n[BBOX-4135] 10\n[BBOX-4136] 10\n[BBOX-4137] 10\n[BBOX-4138] 10\n[BBOX-4139] 10\n[BBOX-4140] 10\n[BBOX-4141] 10\n[BBOX-4142] 10\n[BBOX-4143] 10\n[BBOX-4144] 10\n[BBOX-4145] 10\n[BBOX-4146] 10\n[BBOX-4147] 10\n[BBOX-4148] 10\n[BBOX-4149] 10\n[BBOX-4150] 10\n[BBOX-4151] 10\n[BBOX-4152] 10\n[BBOX-4153] 10\n[BBOX-4154] 10\n[BBOX-4155] 10\n[BBOX-4156] 10\n[BBOX-4157] 10\n[BBOX-4158] 10\n[BBOX-4159] 10\n[BBOX-4160] 10\n[BBOX-4161] 10\n[BBOX-4162] 10\n[BBOX-4163] 10\n[BBOX-4164] 10\n[BBOX-4165] 10\n[BBOX-4166] 10\n[BBOX-4167] 10\n[BBOX-4168] 10\n[BBOX-4169] 10\n[BBOX-4170] 10\n[BBOX-4171] 10\n[BBOX-4172] 10\n[BBOX-4173] 10\n[BBOX-4174] JAEGER PCMED\n[BBOX-4175] 渑池县人民医院\n[BBOX-4176] 肺功能检查报告\n[BBOX-4177] 常规通气\n[BBOX-4178] 姓名：\n[BBOX-4179] 住院号：0\n[BBOX-4180] 性别：女\n[BBOX-4181] 身高：154 cm\n[BBOX-4182] 标准体重：125 %\n[BBOX-4183] 吸烟史：\n[BBOX-4184] 科别：\n[BBOX-4185] 测试号：2025052701\n[BBOX-4186] 年龄：29 Years\n[BBOX-4187] 体重：67.5 kg\n[BBOX-4188] 体表面积：1.66 m\n[BBOX-4189] 测试日期 25/5/27\n[BBOX-4190] 测试时间 10:10:05\n[BBOX-4191] 预计值 实测值 实测/预\n[BBOX-4192] VC MAX [L] 3.20 2.87 89.6\n[BBOX-4193] IRV [L] 1.14\n[BBOX-4194] ERV [L] 1.23 0.92 75.3\n[BBOX-4195] IC [L] 1.97 1.94 98.4\n[BBOX-4196] VT [L] 0.48 0.80 166.0\n[BBOX-4197] MV [L/min] 9.64 25.12 260.5\n[BBOX-4198] VC IN [L] 3.20 2.87 89.6\n[BBOX-4199] VC EX [L] 3.20 2.82 88.0\n[BBOX-4200] BF [1/min] 20.00 31.39 157.0\n[BBOX-4201] FVC [L] 3.18 2.79 87.6\n[BBOX-4202] PEF [L/s] 6.49 3.62 55.8\n[BBOX-4203] FEV 0.5 [L] 1.15\n[BBOX-4204] FEV 1 [L] 2.76 1.57 57.0\n[BBOX-4205] FEV 2 [L] 1.98\n[BBOX-4206] FEV 3 [L] 2.21\n[BBOX-4207] FEV6 [L] 2.61\n[BBOX-4208] FEF 200-1200 [L/s] 2.06\n[BBOX-4209] FEV 1 % FVC [%] 84.23 56.40 67.0\n[BBOX-4210] FEV 1 % VC MAX [%] 83.59 54.79 65.5\n[BBOX-4211] MEF 75 [L/s] 5.83 2.32 39.8\n[BBOX-4212] MEF 50 [L/s] 4.21 0.76 18.0\n[BBOX-4213] MEF 25 [L/s] 2.00 0.23 11.6\n[BBOX-4214] MMEF 75/25 [L/s] 3.86 0.58 14.9\n[BBOX-4215] FEF 75/85 [L/s] 1.22 0.16 13.3\n[BBOX-4216] FEF50 % FIF50 [%] 19.86\n[BBOX-4217] PIF [L/s] 4.32\n[BBOX-4218] FVC IN [L] 3.20 2.72 84.9\n[BBOX-4219] FET [s] 8.39\n[BBOX-4220] FIF 50 [L/s] 3.80\n[BBOX-4221] FIV1 [L] 2.68\n[BBOX-4222] FIV1 % FVC [%] 98.67\n[BBOX-4223] T IN [s] 0.84\n[BBOX-4224] T EX [s] 1.07\n[BBOX-4225] T TOT [s] 1.91\n[BBOX-4226] MIF [L/s] 0.95\n[BBOX-4227] MEF [L/s] 0.75\n[BBOX-4228] MVV [L/min] 105.09 71.84 68.4\n[BBOX-4229] FEF50 % FIF50 [%] 19.86\n[BBOX-4230] V backextrapolation ex [L] 0.04\n[BBOX-4231] V backextrapol. % FVC [%] 1.50\n[BBOX-4232] 测试结果\n[BBOX-4233] 1、中重度阻塞性肺通气功能障碍，小气道功能降低。\n[BBOX-4234] 2、肺弥散功能正常。\n[BBOX-4235] 3、残气量、残气量/肺总量正常。\n[BBOX-4236] 4、沙丁胺醇气雾剂支气管舒张试验呈阳性，FEV1.0改善17.1%。\n[BBOX-4237] 5、建议定期复查。\n[BBOX-4238] 报告医师：李朝红/王晓红 报告日期：2025.5.27\n[BBOX-4239] 6 Vol [L]\n[BBOX-4240] TLC 4\n[BBOX-4241] FRCPth\n[BBOX-4242] RV\n[BBOX-4243] PredAdt.0 0.2 0.4 0.6 0.8 1.0\n[BBOX-4244] Time [min]\n[BBOX-4245] Flow [L/s]\n[BBOX-4246] F/V ex\n[BBOX-4247] 10\n[BBOX-4248] 5\n[BBOX-4249] 0\n[BBOX-4250] 2\n[BBOX-4251] 4\n[BBOX-4252] 6\n[BBOX-4253] 10\n[BBOX-4254] 5\n[BBOX-4255] 10\n[BBOX-4256] F/V in\n[BBOX-4257] Vol%VCmax\n[BBOX-4258] 0\n[BBOX-4259] 20\n[BBOX-4260] 40\n[BBOX-4261] 60\n[BBOX-4262] 80\n[BBOX-4263] 100\n[BBOX-4264] Vol [L]\n[BBOX-4265] 2\n[BBOX-4266] VCmax\n[BBOX-4267] 4\n[BBOX-4268] 6\n[BBOX-4269] 8\n[BBOX-4270] Time [s]\n[BBOX-4271] 4\n[BBOX-4272] Vol [L]\n[BBOX-4273] 2\n[BBOX-4274] 0\n[BBOX-4275] 2\n[BBOX-4276] 4\n[BBOX-4277] 6\n[BBOX-4278] 8\n[BBOX-4279] 10\n[BBOX-4280] 12\n[BBOX-4281] 14\n[BBOX-4282] Time [s]"
  }
]
2026-08-10 12:56:24,915 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:56:24.913+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 35, "failed": 0, "current": {"7ac5bf0e94ba11f1bd9827cf206dfa2d": {"id": "7ac5bf0e94ba11f1bd9827cf206dfa2d", "doc_id": "7a7d42ec94ba11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "FXJI \u4e09\u95e8\u5ce1.pdf", "type": "pdf", "location": "FXJI \u4e09\u95e8\u5ce1.pdf", "size": 8000159, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786366406983, "task_type": "dataflow", "root_trace_id": "bc9b9d974a834eb18f6171d96f843bf1", "root_traceparent": "00-bc9b9d974a834eb18f6171d96f843bf1-0c5099cebc4db2c7-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:56:34,142 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:56:34,164 INFO     29 [SmartSplitter] SmartSplitter done: 2 chunks from 2 LLM segments (all bbox_id). Types: {'OutpatientRecord': 1, 'ExaminationReport': 1}
2026-08-10 12:56:34,173 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 12:56:34,174 INFO     29 [Trace] task=7ac5bf0e | doc=FXJI 三门峡.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "4283 items", "markdown": "", "text": "", "name": "FXJI 三门峡.pdf", "output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}"}
2026-08-10 12:56:34,174 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 12:56:34,179 INFO     29 [ChunkRouter] Routed 2 chunks into 2 groups: {'chunks_Clinical': 1, 'chunks_Examination': 1}
2026-08-10 12:56:34,187 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 12:56:34,187 INFO     29 [Trace] task=7ac5bf0e | doc=FXJI 三门峡.pdf | ChunkRouter:Router | outputs={"html": "", "json": "4283 items", "markdown": "", "text": "", "name": "FXJI 三门峡.pdf", "output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 12:56:34,187 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 12:56:34,192 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:56:34,192 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:56:34,784 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:56:34,795 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 12:56:34,795 INFO     29 [Trace] task=7ac5bf0e | doc=FXJI 三门峡.pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "4283 items", "markdown": "", "text": "", "name": "FXJI 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 12:56:34,796 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 12:56:34,803 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:56:34,803 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:56:35,219 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:56:35,228 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 12:56:35,229 INFO     29 [Trace] task=7ac5bf0e | doc=FXJI 三门峡.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "4283 items", "markdown": "", "text": "", "name": "FXJI 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 12:56:35,229 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 12:56:35,236 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:56:35,237 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:56:35,238 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 12:56:35,238 INFO     29 [qwen-vl-text] positions(35): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:56:35,238 INFO     29 [qwen-vl-text] page grouping: [0, 1], lines per page: [26, 9]
2026-08-10 12:56:35,455 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:56:35,632 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:56:35,633 INFO     29 [qwen-vl-text] LLM extraction start, text_len=581
2026-08-10 12:56:35,633 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:56:35,634 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 34, \"encounter_dates\": [\"2025-05-27\"], \"department\": \"呼吸与危重症医学科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "渑池县人民医院\n门诊病历\n姓名:\n门诊号: 773264\n就诊时间:2025-05-27 09:30 科别: 呼吸与危重症医学科门诊\n姓名:范心静 性别:女 年龄:29岁 婚否:已婚\n职业:自由职业 工作单位:无\n联系电话: 住址:河南省三门峡市渑池县郭窑村15\n组\n病史叙述者:本人 身份证号\n过敏史:无\n主诉:咳嗽、咳痰、胸闷、气喘1周。\n现病史:患者于1周前受凉后出现咳嗽、咳痰、胸闷、气喘,痰为白\n色粘稠痰,咳出困难,夜间及清晨咳嗽明显,活动后胸闷、气喘,\n自行给予“喘息定片”药物治疗,症状无改善。\n既往史:平素身体良好;无特殊疾病史;否认“肝炎、结核”等病史;\n否认手术史;否认外伤史;否认输血史及献血史;否认药物及食\n物过敏史;无预防接种史\n流行病学史:无\n体格检查:体温36.5℃,脉搏78次/分,呼吸20次/分,\n血压120/80mmHg,双肺呼吸音粗,可闻及哮鸣音,心率78\n次/分,律齐,未闻及病理性杂音。\n辅助检查:肺功能四项+支气管舒张实验:沙丁胺醇气雾剂支气管舒\n张实验呈阳性,FEV1.0改善17.1%。\n初步诊断:门诊诊断:1.支气管哮喘。\n-1-\n渑池县人民医院\n门诊病历\n姓名：\n门诊号：\n处理意见：1.注意避免受凉，避免接触刺激性气味，避免接触花粉等\n诱发急性发作；2.如有不适，及时就诊。\n经治医师：\nEhun\n- 2 -",
    "role": "user"
  }
]
2026-08-10 12:56:37,926 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:56:37,926 INFO     29 [qwen-vl-text] LLM output (len=360):
{
  "encounter_date": "2025-05-27",
  "chief_complaint": "咳嗽、咳痰、胸闷、气喘1周。",
  "present_illness": "患者于1周前受凉后出现咳嗽、咳痰、胸闷、气喘,痰为白色粘稠痰,咳出困难,夜间及清晨咳嗽明显,活动后胸闷、气喘,自行给予“喘息定片”药物治疗,症状无改善。",
  "past_history": "平素身体良好;无特殊疾病史;否认“肝炎、结核”等病史;否认手术史;否认外伤史;否认输血史及献血史;否认药物及食物过敏史;无预防接种史",
  "diagnosis": "1.支气管哮喘。",
  "treatment_plan": "1.注意避免受凉，避免接触刺激性气味，避免接触花粉等诱发急性发作；2.如有不适，及时就诊。"
}
2026-08-10 12:56:37,927 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-05-27]
2026-08-10 12:56:37,934 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2130684, prompt_len=1181
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["渑池县人民医院", "门诊病历", "姓名:", "门诊号: 773264", "就诊时间:2025-05-27 09:30 科别: 呼吸与危重症医学科门诊", "姓名:范心静 性别:女 年龄:29岁 婚否:已婚", "职业:自由职业 工作单位:无", "联系电话: 住址:河南省三门峡市渑池县郭窑村15", "组", "病史叙述者:本人 身份证号", "过敏史:无", "主诉:咳嗽、咳痰、胸闷、气喘1周。", "现病史:患者于1周前受凉后出现咳嗽、咳痰、胸闷、气喘,痰为白", "色粘稠痰,咳出困难,夜间及清晨咳嗽明显,活动后胸闷、气喘,", "自行给予“喘息定片”药物治疗,症状无改善。", "既往史:平素身体良好;无特殊疾病史;否认“肝炎、结核”等病史;", "否认手术史;否认外伤史;否认输血史及献血史;否认药物及食", "物过敏史;无预防接种史", "流行病学史:无", "体格检查:体温36.5℃,脉搏78次/分,呼吸20次/分,", "血压120/80mmHg,双肺呼吸音粗,可闻及哮鸣音,心率78", "次/分,律齐,未闻及病理性杂音。", "辅助检查:肺功能四项+支气管舒张实验:沙丁胺醇气雾剂支气管舒", "张实验呈阳性,FEV1.0改善17.1%。", "初步诊断:门诊诊断:1.支气管哮喘。", "-1-"]

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
2026-08-10 12:56:48,756 INFO     29 [qwen-vl-text] coord API raw response (len=1638):
[
	{"text": "渑池县人民医院", "bbox": [380, 185, 593, 207]},
	{"text": "门诊病历", "bbox": [404, 215, 570, 238]},
	{"text": "姓名:", "bbox": [179, 250, 225, 265]},
	{"text": "门诊号: 773264", "bbox": [486, 247, 630, 262]},
	{"text": "就诊时间:2025-05-27 09:30 科别: 呼吸与危重症医学科门诊", "bbox": [178, 282, 744, 299]},
	{"text": "姓名:范心静 性别:女 年龄:29岁 婚否:已婚", "bbox": [176, 313, 697, 330]},
	{"text": "职业:自由职业 工作单位:无", "bbox": [175, 335, 560, 352]},
	{"text": "联系电话: 住址:河南省三门峡市渑池县郭窑村15", "bbox": [174, 356, 792, 373]},
	{"text": "组", "bbox": [173, 378, 193, 394]},
	{"text": "病史叙述者: 本人 身份证号", "bbox": [172, 399, 514, 416]},
	{"text": "过敏史:无", "bbox": [170, 420, 275, 437]},
	{"text": "主诉:咳嗽、咳痰、胸闷、气喘1周。", "bbox": [168, 452, 506, 469]},
	{"text": "现病史:患者于1周前受凉后出现咳嗽、咳痰、胸闷、气喘,痰为白", "bbox": [167, 473, 792, 490]},
	{"text": "色粘稠痰,咳出困难,夜间及清晨咳嗽明显,活动后胸闷、气喘,", "bbox": [209, 495, 812, 512]},
	{"text": "自行给予“喘息定片”药物治疗,症状无改善。", "bbox": [209, 516, 642, 533]},
	{"text": "既往史:平素身体良好;无特殊疾病史;否认“肝炎、结核”等病史;", "bbox": [166, 538, 813, 556]},
	{"text": "否认手术史;否认外伤史;否认输血史及献血史;否认药物及食", "bbox": [207, 561, 806, 578]},
	{"text": "物过敏史;无预防接种史", "bbox": [205, 583, 443, 600]},
	{"text": "流行病学史:无", "bbox": [163, 607, 313, 624]},
	{"text": "体格检查:体温36.5℃,脉搏78次/分,呼吸20次/分,", "bbox": [162, 630, 653, 648]},
	{"text": "血压120/80mmHg,双肺呼吸音粗,可闻及哮鸣音,心率78", "bbox": [268, 654, 811, 672]},
	{"text": "次/分,律齐,未闻及病理性杂音。", "bbox": [201, 677, 527, 694]},
	{"text": "辅助检查:肺功能四项+支气管舒张实验:沙丁胺醇气雾剂支气管舒", "bbox": [158, 701, 802, 719]},
	{"text": "张实验呈阳性,FEV1.0改善17.1%。", "bbox": [199, 724, 527, 742]},
	{"text": "初步诊断:门诊诊断:1.支气管哮喘。", "bbox": [156, 747, 506, 765]},
	{"text": "-1-", "bbox": [461, 809, 510, 822]}
]
2026-08-10 12:56:48,756 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=10.8s
2026-08-10 12:56:48,756 INFO     29 [qwen-vl-text] coord item[0]: text=渑池县人民医院, bbox=[380, 185, 593, 207]
2026-08-10 12:56:48,756 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[404, 215, 570, 238]
2026-08-10 12:56:48,756 INFO     29 [qwen-vl-text] coord item[2]: text=姓名:, bbox=[179, 250, 225, 265]
2026-08-10 12:56:48,756 INFO     29 [qwen-vl-text] coord item[3]: text=门诊号: 773264, bbox=[486, 247, 630, 262]
2026-08-10 12:56:48,756 INFO     29 [qwen-vl-text] coord item[4]: text=就诊时间:2025-05-27 09:30 科别: 呼吸与危重症医学科门诊, bbox=[178, 282, 744, 299]
2026-08-10 12:56:48,757 INFO     29 [qwen-vl-text] coord item[5]: text=姓名:范心静 性别:女 年龄:29岁 婚否:已婚, bbox=[176, 313, 697, 330]
2026-08-10 12:56:48,757 INFO     29 [qwen-vl-text] coord item[6]: text=职业:自由职业 工作单位:无, bbox=[175, 335, 560, 352]
2026-08-10 12:56:48,757 INFO     29 [qwen-vl-text] coord item[7]: text=联系电话: 住址:河南省三门峡市渑池县郭窑村15, bbox=[174, 356, 792, 373]
2026-08-10 12:56:48,757 INFO     29 [qwen-vl-text] coord item[8]: text=组, bbox=[173, 378, 193, 394]
2026-08-10 12:56:48,757 INFO     29 [qwen-vl-text] coord item[9]: text=病史叙述者: 本人 身份证号, bbox=[172, 399, 514, 416]
2026-08-10 12:56:48,757 INFO     29 [qwen-vl-text] coord item[10]: text=过敏史:无, bbox=[170, 420, 275, 437]
2026-08-10 12:56:48,757 INFO     29 [qwen-vl-text] coord item[11]: text=主诉:咳嗽、咳痰、胸闷、气喘1周。, bbox=[168, 452, 506, 469]
2026-08-10 12:56:48,757 INFO     29 [qwen-vl-text] coord item[12]: text=现病史:患者于1周前受凉后出现咳嗽、咳痰、胸闷、气喘,痰为白, bbox=[167, 473, 792, 490]
2026-08-10 12:56:48,757 INFO     29 [qwen-vl-text] coord item[13]: text=色粘稠痰,咳出困难,夜间及清晨咳嗽明显,活动后胸闷、气喘,, bbox=[209, 495, 812, 512]
2026-08-10 12:56:48,757 INFO     29 [qwen-vl-text] coord item[14]: text=自行给予“喘息定片”药物治疗,症状无改善。, bbox=[209, 516, 642, 533]
2026-08-10 12:56:48,757 INFO     29 [qwen-vl-text] coord item[15]: text=既往史:平素身体良好;无特殊疾病史;否认“肝炎、结核”等病史;, bbox=[166, 538, 813, 556]
2026-08-10 12:56:48,757 INFO     29 [qwen-vl-text] coord item[16]: text=否认手术史;否认外伤史;否认输血史及献血史;否认药物及食, bbox=[207, 561, 806, 578]
2026-08-10 12:56:48,757 INFO     29 [qwen-vl-text] coord item[17]: text=物过敏史;无预防接种史, bbox=[205, 583, 443, 600]
2026-08-10 12:56:48,757 INFO     29 [qwen-vl-text] coord item[18]: text=流行病学史:无, bbox=[163, 607, 313, 624]
2026-08-10 12:56:48,757 INFO     29 [qwen-vl-text] coord item[19]: text=体格检查:体温36.5℃,脉搏78次/分,呼吸20次/分,, bbox=[162, 630, 653, 648]
2026-08-10 12:56:48,757 INFO     29 [qwen-vl-text] coord item[20]: text=血压120/80mmHg,双肺呼吸音粗,可闻及哮鸣音,心率78, bbox=[268, 654, 811, 672]
2026-08-10 12:56:48,757 INFO     29 [qwen-vl-text] coord item[21]: text=次/分,律齐,未闻及病理性杂音。, bbox=[201, 677, 527, 694]
2026-08-10 12:56:48,757 INFO     29 [qwen-vl-text] coord item[22]: text=辅助检查:肺功能四项+支气管舒张实验:沙丁胺醇气雾剂支气管舒, bbox=[158, 701, 802, 719]
2026-08-10 12:56:48,757 INFO     29 [qwen-vl-text] coord item[23]: text=张实验呈阳性,FEV1.0改善17.1%。, bbox=[199, 724, 527, 742]
2026-08-10 12:56:48,757 INFO     29 [qwen-vl-text] coord item[24]: text=初步诊断:门诊诊断:1.支气管哮喘。, bbox=[156, 747, 506, 765]
2026-08-10 12:56:48,757 INFO     29 [qwen-vl-text] coord item[25]: text=-1-, bbox=[461, 809, 510, 822]
2026-08-10 12:56:48,758 INFO     29 [qwen-vl-text] page=0 — 26/26 coords, api_time=10.8s
2026-08-10 12:56:48,763 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1535652, prompt_len=729
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共9行）
["渑池县人民医院", "门诊病历", "姓名：", "门诊号：", "处理意见：1.注意避免受凉，避免接触刺激性气味，避免接触花粉等", "诱发急性发作；2.如有不适，及时就诊。", "经治医师：", "Ehun", "- 2 -"]

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
2026-08-10 12:56:52,215 INFO     29 [qwen-vl-text] coord API raw response (len=489):
[
	{"text": "渑池县人民医院", "bbox": [385, 222, 599, 244]},
	{"text": "门诊病历", "bbox": [409, 252, 577, 275]},
	{"text": "姓名：", "bbox": [180, 285, 214, 300]},
	{"text": "门诊号：", "bbox": [492, 285, 561, 300]},
	{"text": "处理意见：1.注意避免受凉，避免接触刺激性气味，避免接触花粉等", "bbox": [179, 321, 799, 338]},
	{"text": "诱发急性发作；2.如有不适，及时就诊。", "bbox": [219, 342, 584, 358]},
	{"text": "经治医师：", "bbox": [574, 373, 669, 389]},
	{"text": "Ehun", "bbox": [679, 370, 724, 387]},
	{"text": "- 2 -", "bbox": [467, 854, 514, 867]}
]
2026-08-10 12:56:52,216 INFO     29 [qwen-vl-text] coord API: raw_items=9, valid_items=9, elapsed=3.5s
2026-08-10 12:56:52,216 INFO     29 [qwen-vl-text] coord item[0]: text=渑池县人民医院, bbox=[385, 222, 599, 244]
2026-08-10 12:56:52,216 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[409, 252, 577, 275]
2026-08-10 12:56:52,216 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[180, 285, 214, 300]
2026-08-10 12:56:52,216 INFO     29 [qwen-vl-text] coord item[3]: text=门诊号：, bbox=[492, 285, 561, 300]
2026-08-10 12:56:52,216 INFO     29 [qwen-vl-text] coord item[4]: text=处理意见：1.注意避免受凉，避免接触刺激性气味，避免接触花粉等, bbox=[179, 321, 799, 338]
2026-08-10 12:56:52,217 INFO     29 [qwen-vl-text] coord item[5]: text=诱发急性发作；2.如有不适，及时就诊。, bbox=[219, 342, 584, 358]
2026-08-10 12:56:52,217 INFO     29 [qwen-vl-text] coord item[6]: text=经治医师：, bbox=[574, 373, 669, 389]
2026-08-10 12:56:52,217 INFO     29 [qwen-vl-text] coord item[7]: text=Ehun, bbox=[679, 370, 724, 387]
2026-08-10 12:56:52,217 INFO     29 [qwen-vl-text] coord item[8]: text=- 2 -, bbox=[467, 854, 514, 867]
2026-08-10 12:56:52,217 INFO     29 [qwen-vl-text] page=1 — 9/9 coords, api_time=3.5s
2026-08-10 12:56:52,217 INFO     29 [qwen-vl-text] new_positions (35):
[[0, 226.1, 352.835, 155.76999999999998, 174.29399999999998], [0, 240.38, 339.15, 181.03, 200.396], [0, 106.505, 133.875, 210.5, 223.13], [0, 289.16999999999996, 374.84999999999997, 207.974, 220.60399999999998], [0, 105.91, 442.68, 237.444, 251.75799999999998], [0, 104.72, 414.715, 263.546, 277.86], [0, 104.125, 333.2, 282.07, 296.384], [0, 103.53, 471.23999999999995, 299.752, 314.066], [0, 102.935, 114.835, 318.276, 331.748], [0, 102.33999999999999, 305.83, 335.95799999999997, 350.272], [0, 101.14999999999999, 163.625, 353.64, 367.954], [0, 99.96, 301.07, 380.584, 394.89799999999997], [0, 99.365, 471.23999999999995, 398.26599999999996, 412.58], [0, 124.35499999999999, 483.14, 416.78999999999996, 431.104], [0, 124.35499999999999, 381.99, 434.472, 448.786], [0, 98.77, 483.73499999999996, 452.996, 468.152], [0, 123.16499999999999, 479.57, 472.36199999999997, 486.676], [0, 121.975, 263.585, 490.88599999999997, 505.2], [0, 96.985, 186.23499999999999, 511.094, 525.408], [0, 96.39, 388.53499999999997, 530.46, 545.616], [0, 159.45999999999998, 482.54499999999996, 550.668, 565.824], [0, 119.595, 313.565, 570.034, 584.348], [0, 94.00999999999999, 477.19, 590.242, 605.398], [0, 118.405, 313.565, 609.608, 624.764], [0, 92.82, 301.07, 628.9739999999999, 644.13], [0, 274.295, 303.45, 681.178, 692.124], [1, 229.075, 356.405, 186.924, 205.44799999999998], [1, 243.355, 343.315, 212.184, 231.54999999999998], [1, 107.1, 127.33, 239.97, 252.6], [1, 292.74, 333.79499999999996, 239.97, 252.6], [1, 106.505, 475.405, 270.282, 284.596], [1, 130.305, 347.47999999999996, 287.964, 301.436], [1, 341.53, 398.055, 314.066, 327.538], [1, 404.005, 430.78, 311.53999999999996, 325.854], [1, 277.865, 305.83, 719.068, 730.014]]
2026-08-10 12:56:52,218 INFO     29 [qwen-vl-text] ═══ DONE ═══ 35 positions, pages=2, time=17.0s
2026-08-10 12:56:52,229 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 12:56:52,230 INFO     29 [Trace] task=7ac5bf0e | doc=FXJI 三门峡.pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "4283 items", "markdown": "", "text": "", "name": "FXJI 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 12:56:52,230 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 12:56:52,237 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:56:52,238 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:56:53,331 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:56:53,338 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 12:56:53,339 INFO     29 [Trace] task=7ac5bf0e | doc=FXJI 三门峡.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "4283 items", "markdown": "", "text": "", "name": "FXJI 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 12:56:53,339 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 12:56:53,344 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:56:53,344 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:56:53,777 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:56:53,786 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 12:56:53,787 INFO     29 [Trace] task=7ac5bf0e | doc=FXJI 三门峡.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "4283 items", "markdown": "", "text": "", "name": "FXJI 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 12:56:53,787 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 12:56:53,793 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:56:53,793 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:56:54,218 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:56:54,222 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 12:56:54,223 INFO     29 [Trace] task=7ac5bf0e | doc=FXJI 三门峡.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "4283 items", "markdown": "", "text": "", "name": "FXJI 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 12:56:54,223 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 12:56:54,228 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:56:54,228 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:56:54,741 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:56:54,745 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 12:56:54,746 INFO     29 [Trace] task=7ac5bf0e | doc=FXJI 三门峡.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "4283 items", "markdown": "", "text": "", "name": "FXJI 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 12:56:54,746 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 12:56:54,756 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 12:56:54,756 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 12:56:54,757 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 12:56:54,758 INFO     29 [qwen-vl-text] positions(4248): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 12:56:54,761 INFO     29 [qwen-vl-text] page grouping: [2, 3, 4], lines per page: [114, 4025, 109]
2026-08-10 12:56:55,095 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:56:55,444 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:56:55,789 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 12:56:55,790 INFO     29 [qwen-vl-text] LLM extraction start, text_len=14765
2026-08-10 12:56:55,791 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:56:55,791 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 35, \"bbox_end\": 4282, \"encounter_dates\": [\"2025-05-27\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "JAEGER PCMED\n渑池县人民医院\n肺功能检查报告\n舒张试验\n姓名：\n住院号：\n性别：女\n身高：154 cm\n标准体重：125 %\n吸烟史：\n科别：\n测试号：2025052701\n年龄：29 Years\n体重：67.5 kg\n体表面积：1.66 m\nFlow [L/s]\nF/V ex\nVol%VCmax\nVol [L]\nVCmax\nTime [s]\nF/V in\n测试日期\n测试时间\n预计值\n前次\n前/预\n后次\n后/预\n改善率\n25/5/27\n25/5/27\n10:10:05\n10:32:25\nVC MAX\n[L]\n3.20\n2.87\n89.6\n3.38\n105.6\n17.9\nFVC\n[L]\n3.18\n2.79\n87.6\n3.37\n106.0\n20.9\nFEV 1\n[L]\n2.76\n1.57\n57.0\n1.84\n66.7\n17.1\nFEV 1 % FVC\n[%]\n84.23\n56.40\n67.0\n54.61\n64.8\n-3.2\nFEV 1 % VC MAX\n[%]\n83.59\n54.79\n65.5\n54.42\n65.1\n-0.7\nPEF\n[L/s]\n6.49\n3.62\n55.8\n4.32\n66.5\n19.2\nMEF 75\n[L/s]\n5.83\n2.32\n39.8\n2.52\n43.2\n8.5\nMEF 50\n[L/s]\n4.21\n0.76\n18.0\n0.91\n21.6\n20.5\nMEF 25\n[L/s]\n2.00\n0.23\n11.6\n0.24\n12.0\n3.0\nMMEF 75/25\n[L/s]\n3.86\n0.58\n14.9\n0.67\n17.3\n16.2\nJAEGER PCMED\n渑池县人民医院\n肺功能检查报告\n综合测试\n姓名：\n性别：女\n年龄：29 Years\n身高：154 cm\n体重：67.5 kg\n备注：\n联系电话：\n住院号：0\n测试号：2025052701\n吸烟史：\n既往史：\n职业：\n测试日期\n测试时间\n预计值\n实测值\n实/预\nVC MAX\n[L]\n3.20\n2.87\n89.6\nFVC\n[L]\n3.18\n2.79\n87.6\nMV\n[L/min]\n9.64\n25.12\n260.5\nFEV 1\n[L]\n2.76\n1.57\n57.0\nFEV 1 % FVC\n[%]\n84.23\n56.40\n67.0\nPEF\n[L/s]\n6.49\n3.62\n55.8\nMEF 75\n[L/s]\n5.83\n2.32\n39.8\nMEF 50\n[L/s]\n4.21\n0.76\n18.0\nMEF 25\n[L/s]\n2.00\n0.23\n11.6\nMMEF 75/25\n[L/s]\n3.86\n0.58\n14.9\nMVV\n[L/min]\n105.09\n71.84\n68.4\nTLC-SB\n[L]\n4.37\n4.10\n93.8\nRV-SB\n[L]\n1.25\n1.38\n110.4\nRV%TLC-SB\n[%]\n28.82\n33.70\n116.9\nFRC-SB\n[L]\n2.48\n2.31\n93.1\nFRC%TLC-SB\n[%]\n49.74\n56.25\n113.1\nDLCO SB [mmol/min/kPa]\n8.44\n6.84\n81.0\nDLCO/VAmmol/min/kPa/L]\n1.93\n1.73\n89.7\nHb\n[g/100ml]\n13.40\nVA\n[L]\n4.22\n3.95\n93.6\nDLCOc SB[mmol/min/kPa]\n8.44\n6.84\n81.0\nDLCOc/VAmmol/min/kPa/L]\n1.93\n1.73\n89.7\nVIN\n[L]\n3.20\n2.72\n85.0\nInsp. time\n[s]\n0.95\nExp. time\n[s]\n1.95\nSample vol\n[L]\nSystem dead space [ml]\n172.00\nAnatom. dead space[ml]\n148.50\nTA\n[s]\n11.32\n测试结果：\nVol [L]\nTime [min]\nPredAdj.0\n0.2\n0.4\n0.6\n0.8\n1.0\nFlow [L/s]\nF/V ex\n10\n5\n0\n2\n4\n6\n5\n10\nF/V in\nVol [L]\n100\n50\n0\nTime [s]\n10\n15\nVolume [L]\n4\n2\n0\n4\n10\n20\n30\n40\nTime [s]\n25/5/27\n10:10:05上\nFRCP th\nRV\nVol [L]\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\n10\nJAEGER PCMED\n渑池县人民医院\n肺功能检查报告\n常规通气\n姓名：\n住院号：0\n性别：女\n身高：154 cm\n标准体重：125 %\n吸烟史：\n科别：\n测试号：2025052701\n年龄：29 Years\n体重：67.5 kg\n体表面积：1.66 m\n测试日期 25/5/27\n测试时间 10:10:05\n预计值 实测值 实测/预\nVC MAX [L] 3.20 2.87 89.6\nIRV [L] 1.14\nERV [L] 1.23 0.92 75.3\nIC [L] 1.97 1.94 98.4\nVT [L] 0.48 0.80 166.0\nMV [L/min] 9.64 25.12 260.5\nVC IN [L] 3.20 2.87 89.6\nVC EX [L] 3.20 2.82 88.0\nBF [1/min] 20.00 31.39 157.0\nFVC [L] 3.18 2.79 87.6\nPEF [L/s] 6.49 3.62 55.8\nFEV 0.5 [L] 1.15\nFEV 1 [L] 2.76 1.57 57.0\nFEV 2 [L] 1.98\nFEV 3 [L] 2.21\nFEV6 [L] 2.61\nFEF 200-1200 [L/s] 2.06\nFEV 1 % FVC [%] 84.23 56.40 67.0\nFEV 1 % VC MAX [%] 83.59 54.79 65.5\nMEF 75 [L/s] 5.83 2.32 39.8\nMEF 50 [L/s] 4.21 0.76 18.0\nMEF 25 [L/s] 2.00 0.23 11.6\nMMEF 75/25 [L/s] 3.86 0.58 14.9\nFEF 75/85 [L/s] 1.22 0.16 13.3\nFEF50 % FIF50 [%] 19.86\nPIF [L/s] 4.32\nFVC IN [L] 3.20 2.72 84.9\nFET [s] 8.39\nFIF 50 [L/s] 3.80\nFIV1 [L] 2.68\nFIV1 % FVC [%] 98.67\nT IN [s] 0.84\nT EX [s] 1.07\nT TOT [s] 1.91\nMIF [L/s] 0.95\nMEF [L/s] 0.75\nMVV [L/min] 105.09 71.84 68.4\nFEF50 % FIF50 [%] 19.86\nV backextrapolation ex [L] 0.04\nV backextrapol. % FVC [%] 1.50\n测试结果\n1、中重度阻塞性肺通气功能障碍，小气道功能降低。\n2、肺弥散功能正常。\n3、残气量、残气量/肺总量正常。\n4、沙丁胺醇气雾剂支气管舒张试验呈阳性，FEV1.0改善17.1%。\n5、建议定期复查。\n报告医师：李朝红/王晓红 报告日期：2025.5.27\n6 Vol [L]\nTLC 4\nFRCPth\nRV\nPredAdt.0 0.2 0.4 0.6 0.8 1.0\nTime [min]\nFlow [L/s]\nF/V ex\n10\n5\n0\n2\n4\n6\n10\n5\n10\nF/V in\nVol%VCmax\n0\n20\n40\n60\n80\n100\nVol [L]\n2\nVCmax\n4\n6\n8\nTime [s]\n4\nVol [L]\n2\n0\n2\n4\n6\n8\n10\n12\n14\nTime [s]",
    "role": "user"
  }
]
2026-08-10 12:56:56,249 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:56:56.247+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 35, "failed": 0, "current": {"7ac5bf0e94ba11f1bd9827cf206dfa2d": {"id": "7ac5bf0e94ba11f1bd9827cf206dfa2d", "doc_id": "7a7d42ec94ba11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "FXJI \u4e09\u95e8\u5ce1.pdf", "type": "pdf", "location": "FXJI \u4e09\u95e8\u5ce1.pdf", "size": 8000159, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786366406983, "task_type": "dataflow", "root_trace_id": "bc9b9d974a834eb18f6171d96f843bf1", "root_traceparent": "00-bc9b9d974a834eb18f6171d96f843bf1-0c5099cebc4db2c7-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:57:22,896 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:57:22,897 INFO     29 [qwen-vl-text] LLM output (len=2793):
{
  "exam_date": "2025-05-27",
  "report_date": "2025-05-27",
  "exam_name": "肺功能检查",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": "舒张试验\n测试日期 25/5/27\n测试时间 10:10:05\n预计值 前次 前/预 后次 后/预 改善率\nVC MAX [L] 3.20 2.87 89.6 3.38 105.6 17.9\nFVC [L] 3.18 2.79 87.6 3.37 106.0 20.9\nFEV 1 [L] 2.76 1.57 57.0 1.84 66.7 17.1\nFEV 1 % FVC [%] 84.23 56.40 67.0 54.61 64.8 -3.2\nFEV 1 % VC MAX [%] 83.59 54.79 65.5 54.42 65.1 -0.7\nPEF [L/s] 6.49 3.62 55.8 4.32 66.5 19.2\nMEF 75 [L/s] 5.83 2.32 39.8 2.52 43.2 8.5\nMEF 50 [L/s] 4.21 0.76 18.0 0.91 21.6 20.5\nMEF 25 [L/s] 2.00 0.23 11.6 0.24 12.0 3.0\nMMEF 75/25 [L/s] 3.86 0.58 14.9 0.67 17.3 16.2\n\n综合测试\n测试日期 25/5/27\n测试时间 10:10:05\n预计值 实测值 实/预\nVC MAX [L] 3.20 2.87 89.6\nFVC [L] 3.18 2.79 87.6\nMV [L/min] 9.64 25.12 260.5\nFEV 1 [L] 2.76 1.57 57.0\nFEV 1 % FVC [%] 84.23 56.40 67.0\nPEF [L/s] 6.49 3.62 55.8\nMEF 75 [L/s] 5.83 2.32 39.8\nMEF 50 [L/s] 4.21 0.76 18.0\nMEF 25 [L/s] 2.00 0.23 11.6\nMMEF 75/25 [L/s] 3.86 0.58 14.9\nMVV [L/min] 105.09 71.84 68.4\nTLC-SB [L] 4.37 4.10 93.8\nRV-SB [L] 1.25 1.38 110.4\nRV%TLC-SB [%] 28.82 33.70 116.9\nFRC-SB [L] 2.48 2.31 93.1\nFRC%TLC-SB [%] 49.74 56.25 113.1\nDLCO SB [mmol/min/kPa] 8.44 6.84 81.0\nDLCO/VAmmol/min/kPa/L] 1.93 1.73 89.7\nHb [g/100ml] 13.40\nVA [L] 4.22 3.95 93.6\nDLCOc SB[mmol/min/kPa] 8.44 6.84 81.0\nDLCOc/VAmmol/min/kPa/L] 1.93 1.73 89.7\nVIN [L] 3.20 2.72 85.0\nInsp. time [s] 0.95\nExp. time [s] 1.95\nSample vol [L]\nSystem dead space [ml] 172.00\nAnatom. dead space[ml] 148.50\nTA [s] 11.32\n\n常规通气\n测试日期 25/5/27\n测试时间 10:10:05\n预计值 实测值 实测/预\nVC MAX [L] 3.20 2.87 89.6\nIRV [L] 1.14\nERV [L] 1.23 0.92 75.3\nIC [L] 1.97 1.94 98.4\nVT [L] 0.48 0.80 166.0\nMV [L/min] 9.64 25.12 260.5\nVC IN [L] 3.20 2.87 89.6\nVC EX [L] 3.20 2.82 88.0\nBF [1/min] 20.00 31.39 157.0\nFVC [L] 3.18 2.79 87.6\nPEF [L/s] 6.49 3.62 55.8\nFEV 0.5 [L] 1.15\nFEV 1 [L] 2.76 1.57 57.0\nFEV 2 [L] 1.98\nFEV 3 [L] 2.21\nFEV6 [L] 2.61\nFEF 200-1200 [L/s] 2.06\nFEV 1 % FVC [%] 84.23 56.40 67.0\nFEV 1 % VC MAX [%] 83.59 54.79 65.5\nMEF 75 [L/s] 5.83 2.32 39.8\nMEF 50 [L/s] 4.21 0.76 18.0\nMEF 25 [L/s] 2.00 0.23 11.6\nMMEF 75/25 [L/s] 3.86 0.58 14.9\nFEF 75/85 [L/s] 1.22 0.16 13.3\nFEF50 % FIF50 [%] 19.86\nPIF [L/s] 4.32\nFVC IN [L] 3.20 2.72 84.9\nFET [s] 8.39\nFIF 50 [L/s] 3.80\nFIV1 [L] 2.68\nFIV1 % FVC [%] 98.67\nT IN [s] 0.84\nT EX [s] 1.07\nT TOT [s] 1.91\nMIF [L/s] 0.95\nMEF [L/s] 0.75\nMVV [L/min] 105.09 71.84 68.4\nFEF50 % FIF50 [%] 19.86\nV backextrapolation ex [L] 0.04\nV backextrapol. % FVC [%] 1.50",
  "conclusion": "测试结果：\n1、中重度阻塞性肺通气功能障碍，小气道功能降低。\n2、肺弥散功能正常。\n3、残气量、残气量/肺总量正常。\n4、沙丁胺醇气雾剂支气管舒张试验呈阳性，FEV1.0改善17.1%。\n5、建议定期复查。",
  "physician": "李朝红/王晓红",
  "reviewer": null
}
2026-08-10 12:57:22,901 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2647939, prompt_len=1643
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共114行）
["JAEGER PCMED", "渑池县人民医院", "肺功能检查报告", "舒张试验", "姓名：", "住院号：", "性别：女", "身高：154 cm", "标准体重：125 %", "吸烟史：", "科别：", "测试号：2025052701", "年龄：29 Years", "体重：67.5 kg", "体表面积：1.66 m", "Flow [L/s]", "F/V ex", "Vol%VCmax", "Vol [L]", "VCmax", "Time [s]", "F/V in", "测试日期", "测试时间", "预计值", "前次", "前/预", "后次", "后/预", "改善率", "25/5/27", "25/5/27", "10:10:05", "10:32:25", "VC MAX", "[L]", "3.20", "2.87", "89.6", "3.38", "105.6", "17.9", "FVC", "[L]", "3.18", "2.79", "87.6", "3.37", "106.0", "20.9", "FEV 1", "[L]", "2.76", "1.57", "57.0", "1.84", "66.7", "17.1", "FEV 1 % FVC", "[%]", "84.23", "56.40", "67.0", "54.61", "64.8", "-3.2", "FEV 1 % VC MAX", "[%]", "83.59", "54.79", "65.5", "54.42", "65.1", "-0.7", "PEF", "[L/s]", "6.49", "3.62", "55.8", "4.32", "66.5", "19.2", "MEF 75", "[L/s]", "5.83", "2.32", "39.8", "2.52", "43.2", "8.5", "MEF 50", "[L/s]", "4.21", "0.76", "18.0", "0.91", "21.6", "20.5", "MEF 25", "[L/s]", "2.00", "0.23", "11.6", "0.24", "12.0", "3.0", "MMEF 75/25", "[L/s]", "3.86", "0.58", "14.9", "0.67", "17.3", "16.2"]

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
2026-08-10 12:58:00,037 INFO     29 [qwen-vl-text] coord API raw response (len=7244):
[
	{"text": "JAEGER PCMED", "bbox": [744, 45, 929, 63]},
	{"text": "渑池县人民医院", "bbox": [411, 65, 633, 90]},
	{"text": "肺功能检查报告", "bbox": [424, 94, 610, 112]},
	{"text": "舒张试验", "bbox": [467, 117, 556, 134]},
	{"text": "姓名：", "bbox": [128, 134, 176, 147]},
	{"text": "住院号：", "bbox": [128, 147, 195, 159]},
	{"text": "性别：", "bbox": [128, 159, 176, 171]},
	{"text": "女", "bbox": [304, 160, 323, 172]},
	{"text": "身高：", "bbox": [128, 171, 176, 183]},
	{"text": "154 cm", "bbox": [304, 173, 363, 184]},
	{"text": "标准体重：", "bbox": [128, 183, 214, 195]},
	{"text": "125 %", "bbox": [304, 185, 363, 196]},
	{"text": "吸烟史：", "bbox": [128, 195, 195, 207]},
	{"text": "科别：", "bbox": [486, 138, 533, 150]},
	{"text": "测试号：", "bbox": [486, 150, 552, 162]},
	{"text": "年龄：", "bbox": [486, 162, 533, 174]},
	{"text": "体重：", "bbox": [486, 174, 533, 186]},
	{"text": "体表面积：", "bbox": [486, 186, 570, 198]},
	{"text": "Flow [L/s]", "bbox": [159, 245, 212, 256]},
	{"text": "F/V ex", "bbox": [370, 247, 405, 256]},
	{"text": "Vol%VCmax", "bbox": [528, 243, 591, 252]},
	{"text": "0.0", "bbox": [544, 252, 570, 262]},
	{"text": "Vol [L]", "bbox": [577, 256, 611, 267]},
	{"text": "10", "bbox": [139, 265, 154, 274]},
	{"text": "20", "bbox": [539, 265, 554, 274]},
	{"text": "40", "bbox": [539, 277, 554, 286]},
	{"text": "60", "bbox": [539, 289, 554, 299]},
	{"text": "2", "bbox": [562, 289, 570, 299]},
	{"text": "80", "bbox": [539, 301, 554, 310]},
	{"text": "5", "bbox": [144, 295, 154, 303]},
	{"text": "100", "bbox": [534, 314, 554, 323]},
	{"text": "VCmax", "bbox": [590, 311, 628, 320]},
	{"text": "1", "bbox": [498, 321, 506, 330]},
	{"text": "2", "bbox": [498, 332, 506, 341]},
	{"text": "0", "bbox": [144, 325, 154, 334]},
	{"text": "1", "bbox": [195, 335, 204, 344]},
	{"text": "2", "bbox": [240, 335, 250, 344]},
	{"text": "3", "bbox": [283, 335, 292, 344]},
	{"text": "4", "bbox": [326, 335, 335, 344]},
	{"text": "5", "bbox": [369, 335, 378, 344]},
	{"text": "6", "bbox": [411, 335, 420, 344]},
	{"text": "7", "bbox": [454, 335, 463, 344]},
	{"text": "4", "bbox": [562, 326, 570, 335]},
	{"text": "6", "bbox": [562, 363, 570, 372]},
	{"text": "10", "bbox": [139, 385, 154, 394]},
	{"text": "F/V in", "bbox": [370, 404, 405, 414]},
	{"text": "Time [s]", "bbox": [707, 391, 751, 401]},
	{"text": "8", "bbox": [562, 400, 570, 409]},
	{"text": "0", "bbox": [572, 409, 580, 418]},
	{"text": "2", "bbox": [616, 409, 624, 418]},
	{"text": "4", "bbox": [660, 409, 668, 418]},
	{"text": "6", "bbox": [704, 409, 712, 418]},
	{"text": "8", "bbox": [748, 409, 756, 418]},
	{"text": "10", "bbox": [789, 409, 801, 418]},
	{"text": "12", "bbox": [833, 409, 845, 418]},
	{"text": "14", "bbox": [875, 409, 888, 418]},
	{"text": "测试日期", "bbox": [128, 439, 208, 452]},
	{"text": "测试时间", "bbox": [128, 452, 208, 465]},
	{"text": "预计值", "bbox": [413, 425, 472, 438]},
	{"text": "前次", "bbox": [519, 425, 558, 438]},
	{"text": "前/预", "bbox": [596, 425, 645, 438]},
	{"text": "后次", "bbox": [692, 425, 730, 438]},
	{"text": "后/预", "bbox": [768, 425, 816, 438]},
	{"text": "改善率", "bbox": [844, 425, 900, 438]},
	{"text": "25/5/27", "bbox": [490, 440, 558, 451]},
	{"text": "25/5/27", "bbox": [663, 440, 730, 451]},
	{"text": "10:10:05", "bbox": [482, 453, 558, 464]},
	{"text": "10:32:25", "bbox": [654, 453, 730, 464]},
	{"text": "VC MAX", "bbox": [128, 480, 190, 490]},
	{"text": "[L]", "bbox": [357, 480, 383, 491]},
	{"text": "3.20", "bbox": [433, 480, 472, 490]},
	{"text": "2.87", "bbox": [519, 480, 558, 490]},
	{"text": "89.6", "bbox": [605, 480, 645, 490]},
	{"text": "3.38", "bbox": [692, 480, 730, 490]},
	{"text": "105.6", "bbox": [768, 480, 816, 490]},
	{"text": "17.9", "bbox": [863, 480, 901, 490]},
	{"text": "FVC", "bbox": [128, 493, 160, 503]},
	{"text": "[L]", "bbox": [357, 493, 383, 504]},
	{"text": "3.18", "bbox": [433, 493, 472, 503]},
	{"text": "2.79", "bbox": [519, 493, 558, 503]},
	{"text": "87.6", "bbox": [605, 493, 645, 503]},
	{"text": "3.37", "bbox": [692, 493, 730, 503]},
	{"text": "106.0", "bbox": [768, 493, 816, 503]},
	{"text": "20.9", "bbox": [863, 493, 901, 503]},
	{"text": "FEV 1", "bbox": [128, 506, 177, 516]},
	{"text": "[L]", "bbox": [357, 506, 383, 517]},
	{"text": "2.76", "bbox": [433, 506, 472, 516]},
	{"text": "1.57", "bbox": [519, 506, 558, 516]},
	{"text": "57.0", "bbox": [605, 506, 645, 516]},
	{"text": "1.84", "bbox": [692, 506, 730, 516]},
	{"text": "66.7", "bbox": [778, 506, 816, 516]},
	{"text": "17.1", "bbox": [863, 506, 901, 516]},
	{"text": "FEV 1 % FVC", "bbox": [128, 519, 239, 529]},
	{"text": "[%]", "bbox": [357, 519, 383, 530]},
	{"text": "84.23", "bbox": [423, 519, 472, 529]},
	{"text": "56.40", "bbox": [510, 519, 558, 529]},
	{"text": "67.0", "bbox": [605, 519, 645, 529]},
	{"text": "54.61", "bbox": [683, 519, 730, 529]},
	{"text": "64.8", "bbox": [778, 519, 816, 529]},
	{"text": "-3.2", "bbox": [863, 519, 901, 529]},
	{"text": "FEV 1 % VC MAX", "bbox": [128, 532, 268, 542]},
	{"text": "[%]", "bbox": [357, 532, 383, 543]},
	{"text": "83.59", "bbox": [423, 532, 472, 542]},
	{"text": "54.79", "bbox": [510, 532, 558, 542]},
	{"text": "65.5", "bbox": [605, 532, 645, 542]},
	{"text": "54.42", "bbox": [683, 532, 730, 542]},
	{"text": "65.1", "bbox": [778, 532, 816, 542]},
	{"text": "-0.7", "bbox": [863, 532, 901, 542]},
	{"text": "PEF", "bbox": [128, 545, 160, 555]},
	{"text": "[L/s]", "bbox": [338, 545, 383, 556]},
	{"text": "6.49", "bbox": [433, 545, 472, 555]},
	{"text": "3.62", "bbox": [519, 545, 558, 555]},
	{"text": "55.8", "bbox": [605, 545, 645, 555]},
	{"text": "4.32", "bbox": [692, 545, 730, 555]},
	{"text": "66.5", "bbox": [778, 545, 816, 555]},
	{"text": "19.2", "bbox": [863, 545, 901, 555]},
	{"text": "MEF 75", "bbox": [128, 558, 188, 568]},
	{"text": "[L/s]", "bbox": [338, 558, 383, 569]},
	{"text": "5.83", "bbox": [433, 558, 472, 568]},
	{"text": "2.32", "bbox": [519, 558, 558, 568]},
	{"text": "39.8", "bbox": [605, 558, 645, 568]},
	{"text": "2.52", "bbox": [692, 558, 730, 568]},
	{"text": "43.2", "bbox": [778, 558, 816, 568]},
	{"text": "8.5", "bbox": [873, 558, 901, 568]},
	{"text": "MEF 50", "bbox": [128, 571, 188, 581]},
	{"text": "[L/s]", "bbox": [338, 571, 383, 582]},
	{"text": "4.21", "bbox": [433, 571, 472, 581]},
	{"text": "0.76", "bbox": [519, 571, 558, 581]},
	{"text": "18.0", "bbox": [605, 571, 645, 581]},
	{"text": "0.91", "bbox": [692, 571, 730, 581]},
	{"text": "21.6", "bbox": [778, 571, 816, 581]},
	{"text": "20.5", "bbox": [863, 571, 901, 581]},
	{"text": "MEF 25", "bbox": [128, 584, 188, 594]},
	{"text": "[L/s]", "bbox": [338, 584, 383, 595]},
	{"text": "2.00", "bbox": [433, 584, 472, 594]},
	{"text": "0.23", "bbox": [519, 584, 558, 594]},
	{"text": "11.6", "bbox": [605, 584, 645, 594]},
	{"text": "0.24", "bbox": [692, 584, 730, 594]},
	{"text": "12.0", "bbox": [778, 584, 816, 594]},
	{"text": "3.0", "bbox": [873, 584, 901, 594]},
	{"text": "MMEF 75/25", "bbox": [128, 597, 227, 608]},
	{"text": "[L/s]", "bbox": [338, 597, 383, 608]},
	{"text": "3.86", "bbox": [433, 597, 472, 608]},
	{"text": "0.58", "bbox": [519, 597, 558, 608]},
	{"text": "14.9", "bbox": [605, 597, 645, 608]},
	{"text": "0.67", "bbox": [692, 597, 730, 608]},
	{"text": "17.3", "bbox": [778, 597, 816, 608]},
	{"text": "16.2", "bbox": [863, 597, 901, 608]}
]
2026-08-10 12:58:00,037 INFO     29 [qwen-vl-text] coord API: raw_items=148, valid_items=148, elapsed=37.1s
2026-08-10 12:58:00,037 INFO     29 [qwen-vl-text] coord item[0]: text=JAEGER PCMED, bbox=[744, 45, 929, 63]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[1]: text=渑池县人民医院, bbox=[411, 65, 633, 90]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[2]: text=肺功能检查报告, bbox=[424, 94, 610, 112]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[3]: text=舒张试验, bbox=[467, 117, 556, 134]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[128, 134, 176, 147]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[5]: text=住院号：, bbox=[128, 147, 195, 159]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[6]: text=性别：, bbox=[128, 159, 176, 171]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[7]: text=女, bbox=[304, 160, 323, 172]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[8]: text=身高：, bbox=[128, 171, 176, 183]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[9]: text=154 cm, bbox=[304, 173, 363, 184]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[10]: text=标准体重：, bbox=[128, 183, 214, 195]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[11]: text=125 %, bbox=[304, 185, 363, 196]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[12]: text=吸烟史：, bbox=[128, 195, 195, 207]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[13]: text=科别：, bbox=[486, 138, 533, 150]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[14]: text=测试号：, bbox=[486, 150, 552, 162]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[15]: text=年龄：, bbox=[486, 162, 533, 174]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[16]: text=体重：, bbox=[486, 174, 533, 186]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[17]: text=体表面积：, bbox=[486, 186, 570, 198]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[18]: text=Flow [L/s], bbox=[159, 245, 212, 256]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[19]: text=F/V ex, bbox=[370, 247, 405, 256]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[20]: text=Vol%VCmax, bbox=[528, 243, 591, 252]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[21]: text=0.0, bbox=[544, 252, 570, 262]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[22]: text=Vol [L], bbox=[577, 256, 611, 267]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[23]: text=10, bbox=[139, 265, 154, 274]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[24]: text=20, bbox=[539, 265, 554, 274]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[25]: text=40, bbox=[539, 277, 554, 286]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[26]: text=60, bbox=[539, 289, 554, 299]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[27]: text=2, bbox=[562, 289, 570, 299]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[28]: text=80, bbox=[539, 301, 554, 310]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[29]: text=5, bbox=[144, 295, 154, 303]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[30]: text=100, bbox=[534, 314, 554, 323]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[31]: text=VCmax, bbox=[590, 311, 628, 320]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[32]: text=1, bbox=[498, 321, 506, 330]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[33]: text=2, bbox=[498, 332, 506, 341]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[34]: text=0, bbox=[144, 325, 154, 334]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[35]: text=1, bbox=[195, 335, 204, 344]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[36]: text=2, bbox=[240, 335, 250, 344]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[37]: text=3, bbox=[283, 335, 292, 344]
2026-08-10 12:58:00,038 INFO     29 [qwen-vl-text] coord item[38]: text=4, bbox=[326, 335, 335, 344]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[39]: text=5, bbox=[369, 335, 378, 344]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[40]: text=6, bbox=[411, 335, 420, 344]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[41]: text=7, bbox=[454, 335, 463, 344]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[42]: text=4, bbox=[562, 326, 570, 335]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[43]: text=6, bbox=[562, 363, 570, 372]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[44]: text=10, bbox=[139, 385, 154, 394]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[45]: text=F/V in, bbox=[370, 404, 405, 414]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[46]: text=Time [s], bbox=[707, 391, 751, 401]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[47]: text=8, bbox=[562, 400, 570, 409]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[48]: text=0, bbox=[572, 409, 580, 418]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[49]: text=2, bbox=[616, 409, 624, 418]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[50]: text=4, bbox=[660, 409, 668, 418]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[51]: text=6, bbox=[704, 409, 712, 418]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[52]: text=8, bbox=[748, 409, 756, 418]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[53]: text=10, bbox=[789, 409, 801, 418]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[54]: text=12, bbox=[833, 409, 845, 418]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[55]: text=14, bbox=[875, 409, 888, 418]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[56]: text=测试日期, bbox=[128, 439, 208, 452]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[57]: text=测试时间, bbox=[128, 452, 208, 465]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[58]: text=预计值, bbox=[413, 425, 472, 438]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[59]: text=前次, bbox=[519, 425, 558, 438]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[60]: text=前/预, bbox=[596, 425, 645, 438]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[61]: text=后次, bbox=[692, 425, 730, 438]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[62]: text=后/预, bbox=[768, 425, 816, 438]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[63]: text=改善率, bbox=[844, 425, 900, 438]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[64]: text=25/5/27, bbox=[490, 440, 558, 451]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[65]: text=25/5/27, bbox=[663, 440, 730, 451]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[66]: text=10:10:05, bbox=[482, 453, 558, 464]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[67]: text=10:32:25, bbox=[654, 453, 730, 464]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[68]: text=VC MAX, bbox=[128, 480, 190, 490]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[69]: text=[L], bbox=[357, 480, 383, 491]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[70]: text=3.20, bbox=[433, 480, 472, 490]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[71]: text=2.87, bbox=[519, 480, 558, 490]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[72]: text=89.6, bbox=[605, 480, 645, 490]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[73]: text=3.38, bbox=[692, 480, 730, 490]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[74]: text=105.6, bbox=[768, 480, 816, 490]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[75]: text=17.9, bbox=[863, 480, 901, 490]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[76]: text=FVC, bbox=[128, 493, 160, 503]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[77]: text=[L], bbox=[357, 493, 383, 504]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[78]: text=3.18, bbox=[433, 493, 472, 503]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[79]: text=2.79, bbox=[519, 493, 558, 503]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[80]: text=87.6, bbox=[605, 493, 645, 503]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[81]: text=3.37, bbox=[692, 493, 730, 503]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[82]: text=106.0, bbox=[768, 493, 816, 503]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[83]: text=20.9, bbox=[863, 493, 901, 503]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[84]: text=FEV 1, bbox=[128, 506, 177, 516]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[85]: text=[L], bbox=[357, 506, 383, 517]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[86]: text=2.76, bbox=[433, 506, 472, 516]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[87]: text=1.57, bbox=[519, 506, 558, 516]
2026-08-10 12:58:00,039 INFO     29 [qwen-vl-text] coord item[88]: text=57.0, bbox=[605, 506, 645, 516]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[89]: text=1.84, bbox=[692, 506, 730, 516]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[90]: text=66.7, bbox=[778, 506, 816, 516]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[91]: text=17.1, bbox=[863, 506, 901, 516]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[92]: text=FEV 1 % FVC, bbox=[128, 519, 239, 529]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[93]: text=[%], bbox=[357, 519, 383, 530]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[94]: text=84.23, bbox=[423, 519, 472, 529]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[95]: text=56.40, bbox=[510, 519, 558, 529]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[96]: text=67.0, bbox=[605, 519, 645, 529]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[97]: text=54.61, bbox=[683, 519, 730, 529]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[98]: text=64.8, bbox=[778, 519, 816, 529]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[99]: text=-3.2, bbox=[863, 519, 901, 529]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[100]: text=FEV 1 % VC MAX, bbox=[128, 532, 268, 542]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[101]: text=[%], bbox=[357, 532, 383, 543]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[102]: text=83.59, bbox=[423, 532, 472, 542]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[103]: text=54.79, bbox=[510, 532, 558, 542]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[104]: text=65.5, bbox=[605, 532, 645, 542]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[105]: text=54.42, bbox=[683, 532, 730, 542]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[106]: text=65.1, bbox=[778, 532, 816, 542]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[107]: text=-0.7, bbox=[863, 532, 901, 542]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[108]: text=PEF, bbox=[128, 545, 160, 555]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[109]: text=[L/s], bbox=[338, 545, 383, 556]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[110]: text=6.49, bbox=[433, 545, 472, 555]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[111]: text=3.62, bbox=[519, 545, 558, 555]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[112]: text=55.8, bbox=[605, 545, 645, 555]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[113]: text=4.32, bbox=[692, 545, 730, 555]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[114]: text=66.5, bbox=[778, 545, 816, 555]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[115]: text=19.2, bbox=[863, 545, 901, 555]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[116]: text=MEF 75, bbox=[128, 558, 188, 568]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[117]: text=[L/s], bbox=[338, 558, 383, 569]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[118]: text=5.83, bbox=[433, 558, 472, 568]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[119]: text=2.32, bbox=[519, 558, 558, 568]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[120]: text=39.8, bbox=[605, 558, 645, 568]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[121]: text=2.52, bbox=[692, 558, 730, 568]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[122]: text=43.2, bbox=[778, 558, 816, 568]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[123]: text=8.5, bbox=[873, 558, 901, 568]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[124]: text=MEF 50, bbox=[128, 571, 188, 581]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[125]: text=[L/s], bbox=[338, 571, 383, 582]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[126]: text=4.21, bbox=[433, 571, 472, 581]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[127]: text=0.76, bbox=[519, 571, 558, 581]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[128]: text=18.0, bbox=[605, 571, 645, 581]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[129]: text=0.91, bbox=[692, 571, 730, 581]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[130]: text=21.6, bbox=[778, 571, 816, 581]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[131]: text=20.5, bbox=[863, 571, 901, 581]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[132]: text=MEF 25, bbox=[128, 584, 188, 594]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[133]: text=[L/s], bbox=[338, 584, 383, 595]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[134]: text=2.00, bbox=[433, 584, 472, 594]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[135]: text=0.23, bbox=[519, 584, 558, 594]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[136]: text=11.6, bbox=[605, 584, 645, 594]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[137]: text=0.24, bbox=[692, 584, 730, 594]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[138]: text=12.0, bbox=[778, 584, 816, 594]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[139]: text=3.0, bbox=[873, 584, 901, 594]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[140]: text=MMEF 75/25, bbox=[128, 597, 227, 608]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[141]: text=[L/s], bbox=[338, 597, 383, 608]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[142]: text=3.86, bbox=[433, 597, 472, 608]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[143]: text=0.58, bbox=[519, 597, 558, 608]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[144]: text=14.9, bbox=[605, 597, 645, 608]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[145]: text=0.67, bbox=[692, 597, 730, 608]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[146]: text=17.3, bbox=[778, 597, 816, 608]
2026-08-10 12:58:00,040 INFO     29 [qwen-vl-text] coord item[147]: text=16.2, bbox=[863, 597, 901, 608]
2026-08-10 12:58:00,041 INFO     29 [qwen-vl-text] page=2 — 114/114 coords, api_time=37.1s
2026-08-10 12:58:00,047 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3000136, prompt_len=25346
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共4025行）
["JAEGER PCMED", "渑池县人民医院", "肺功能检查报告", "综合测试", "姓名：", "性别：女", "年龄：29 Years", "身高：154 cm", "体重：67.5 kg", "备注：", "联系电话：", "住院号：0", "测试号：2025052701", "吸烟史：", "既往史：", "职业：", "测试日期", "测试时间", "预计值", "实测值", "实/预", "VC MAX", "[L]", "3.20", "2.87", "89.6", "FVC", "[L]", "3.18", "2.79", "87.6", "MV", "[L/min]", "9.64", "25.12", "260.5", "FEV 1", "[L]", "2.76", "1.57", "57.0", "FEV 1 % FVC", "[%]", "84.23", "56.40", "67.0", "PEF", "[L/s]", "6.49", "3.62", "55.8", "MEF 75", "[L/s]", "5.83", "2.32", "39.8", "MEF 50", "[L/s]", "4.21", "0.76", "18.0", "MEF 25", "[L/s]", "2.00", "0.23", "11.6", "MMEF 75/25", "[L/s]", "3.86", "0.58", "14.9", "MVV", "[L/min]", "105.09", "71.84", "68.4", "TLC-SB", "[L]", "4.37", "4.10", "93.8", "RV-SB", "[L]", "1.25", "1.38", "110.4", "RV%TLC-SB", "[%]", "28.82", "33.70", "116.9", "FRC-SB", "[L]", "2.48", "2.31", "93.1", "FRC%TLC-SB", "[%]", "49.74", "56.25", "113.1", "DLCO SB [mmol/min/kPa]", "8.44", "6.84", "81.0", "DLCO/VAmmol/min/kPa/L]", "1.93", "1.73", "89.7", "Hb", "[g/100ml]", "13.40", "VA", "[L]", "4.22", "3.95", "93.6", "DLCOc SB[mmol/min/kPa]", "8.44", "6.84", "81.0", "DLCOc/VAmmol/min/kPa/L]", "1.93", "1.73", "89.7", "VIN", "[L]", "3.20", "2.72", "85.0", "Insp. time", "[s]", "0.95", "Exp. time", "[s]", "1.95", "Sample vol", "[L]", "System dead space [ml]", "172.00", "Anatom. dead space[ml]", "148.50", "TA", "[s]", "11.32", "测试结果：", "Vol [L]", "Time [min]", "PredAdj.0", "0.2", "0.4", "0.6", "0.8", "1.0", "Flow [L/s]", "F/V ex", "10", "5", "0", "2", "4", "6", "5", "10", "F/V in", "Vol [L]", "100", "50", "0", "Time [s]", "10", "15", "Volume [L]", "4", "2", "0", "4", "10", "20", "30", "40", "Time [s]", "25/5/27", "10:10:05上", "FRCP th", "RV", "Vol [L]", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10", "10"]

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
2026-08-10 12:59:13,370 INFO     29 [qwen-vl-text] coord API raw response (len=12050):
[
	{"text": "JAEGER PCMED", "bbox": [708, 63, 900, 80]},
	{"text": "渑池县人民医院", "bbox": [370, 82, 586, 104]},
	{"text": "肺功能检查报告", "bbox": [404, 107, 555, 124],
	"text": "综合测试", "bbox": [446, 128, 534, 144],
	"text": "姓名：", "bbox": [65, 144, 112, 156],
	"text": "性别：女", "bbox": [65, 156, 255, 169],
	"text": "年龄：29 Years", "bbox": [65, 169, 313, 181],
	"text": "身高：154 cm", "bbox": [65, 181, 296, 193],
	"text": "体重：67.5 kg", "bbox": [65, 193, 303, 205],
	"text": "备注：", "bbox": [65, 204, 112, 216],
	"text": "联系电话：", "bbox": [414, 147, 498, 159],
	"text": "住院号：0", "bbox": [414, 159, 592, 171],
	"text": "测试号：2025052701", "bbox": [414, 171, 674, 183],
	"text": "吸烟史：", "bbox": [414, 183, 480, 194],
	"text": "既往史：", "bbox": [414, 194, 480, 206],
	"text": "职业：", "bbox": [414, 206, 462, 217],
	"text": "测试日期", "bbox": [63, 251, 147, 264],
	"text": "测试时间", "bbox": [63, 264, 147, 278],
	"text": "预计值", "bbox": [345, 239, 407, 252],
	"text": "实测值", "bbox": [458, 239, 519, 252],
	"text": "实/预", "bbox": [571, 239, 622, 252],
	"text": "25/5/27", "bbox": [448, 253, 519, 265],
	"text": "10:10:05上", "bbox": [417, 266, 519, 278],
	"text": "VC MAX", "bbox": [62, 294, 127, 305],
	"text": "[L]", "bbox": [264, 294, 290, 306],
	"text": "3.20", "bbox": [365, 294, 407, 306],
	"text": "2.87", "bbox": [478, 294, 519, 306],
	"text": "89.6", "bbox": [582, 294, 622, 306],
	"text": "FVC", "bbox": [62, 308, 94, 319],
	"text": "[L]", "bbox": [264, 308, 290, 320],
	"text": "3.18", "bbox": [365, 308, 407, 320],
	"text": "2.79", "bbox": [478, 308, 519, 320],
	"text": "87.6", "bbox": [582, 308, 622, 320],
	"text": "MV", "bbox": [62, 322, 85, 333],
	"text": "[L/min]", "bbox": [222, 322, 290, 334],
	"text": "9.64", "bbox": [365, 322, 407, 334],
	"text": "25.12", "bbox": [468, 322, 519, 334],
	"text": "260.5", "bbox": [571, 322, 622, 334],
	"text": "FEV 1", "bbox": [62, 336, 114, 347],
	"text": "[L]", "bbox": [264, 336, 290, 348],
	"text": "2.76", "bbox": [365, 336, 407, 348],
	"text": "1.57", "bbox": [478, 336, 519, 348],
	"text": "57.0", "bbox": [582, 336, 622, 348],
	"text": "FEV 1 % FVC", "bbox": [62, 350, 177, 361],
	"text": "[%]", "bbox": [264, 350, 290, 362],
	"text": "84.23", "bbox": [355, 350, 407, 362],
	"text": "56.40", "bbox": [468, 350, 519, 362],
	"text": "67.0", "bbox": [582, 350, 622, 362],
	"text": "PEF", "bbox": [62, 364, 94, 375],
	"text": "[L/s]", "bbox": [243, 364, 290, 376],
	"text": "6.49", "bbox": [365, 364, 407, 376],
	"text": "3.62", "bbox": [478, 364, 519, 376],
	"text": "55.8", "bbox": [582, 364, 622, 376],
	"text": "MEF 75", "bbox": [62, 378, 124, 389],
	"text": "[L/s]", "bbox": [243, 378, 290, 390],
	"text": "5.83", "bbox": [365, 378, 407, 390],
	"text": "2.32", "bbox": [478, 378, 519, 390],
	"text": "39.8", "bbox": [582, 378, 622, 390],
	"text": "MEF 50", "bbox": [62, 392, 124, 403],
	"text": "[L/s]", "bbox": [243, 392, 290, 404],
	"text": "4.21", "bbox": [365, 392, 407, 404],
	"text": "0.76", "bbox": [478, 392, 519, 404],
	"text": "18.0", "bbox": [582, 392, 622, 404],
	"text": "MEF 25", "bbox": [62, 406, 124, 417],
	"text": "[L/s]", "bbox": [243, 406, 290, 418],
	"text": "2.00", "bbox": [365, 406, 407, 418],
	"text": "0.23", "bbox": [478, 406, 519, 418],
	"text": "11.6", "bbox": [582, 406, 622, 418],
	"text": "MMEF 75/25", "bbox": [62, 419, 165, 430],
	"text": "[L/s]", "bbox": [243, 419, 290, 431],
	"text": "3.86", "bbox": [365, 419, 407, 431],
	"text": "0.58", "bbox": [478, 419, 519, 431],
	"text": "14.9", "bbox": [582, 419, 622, 431],
	"text": "MVV", "bbox": [62, 433, 94, 444],
	"text": "[L/min]", "bbox": [222, 433, 290, 445],
	"text": "105.09", "bbox": [345, 433, 407, 445],
	"text": "71.84", "bbox": [468, 433, 519, 445],
	"text": "68.4", "bbox": [582, 433, 622, 445],
	"text": "TLC-SB", "bbox": [62, 461, 124, 472],
	"text": "[L]", "bbox": [264, 461, 290, 473],
	"text": "4.37", "bbox": [365, 461, 407, 473],
	"text": "4.10", "bbox": [478, 461, 519, 473],
	"text": "93.8", "bbox": [582, 461, 622, 473],
	"text": "RV-SB", "bbox": [62, 475, 112, 486],
	"text": "[L]", "bbox": [264, 475, 290, 487],
	"text": "1.25", "bbox": [365, 475, 407, 487],
	"text": "1.38", "bbox": [478, 475, 519, 487],
	"text": "110.4", "bbox": [571, 475, 622, 487],
	"text": "RV%TLC-SB", "bbox": [62, 489, 155, 500],
	"text": "[%]", "bbox": [264, 489, 290, 501],
	"text": "28.82", "bbox": [355, 489, 407, 501],
	"text": "33.70", "bbox": [468, 489, 519, 501],
	"text": "116.9", "bbox": [571, 489, 622, 501],
	"text": "FRC-SB", "bbox": [62, 503, 124, 514],
	"text": "[L]", "bbox": [264, 503, 290, 515],
	"text": "2.48", "bbox": [365, 503, 407, 515],
	"text": "2.31", "bbox": [478, 503, 519, 515],
	"text": "93.1", "bbox": [582, 503, 622, 515],
	"text": "FRC%TLC-SB", "bbox": [62, 517, 165, 528],
	"text": "[%]", "bbox": [264, 517, 290, 529],
	"text": "49.74", "bbox": [355, 517, 407, 529],
	"text": "56.25", "bbox": [468, 517, 519, 529],
	"text": "113.1", "bbox": [571, 517, 622, 529],
	"text": "DLCO SB [mmol/min/kPa]", "bbox": [62, 530, 289, 542],
	"text": "8.44", "bbox": [365, 530, 407, 542],
	"text": "6.84", "bbox": [478, 530, 519, 542],
	"text": "81.0", "bbox": [582, 530, 622, 542],
	"text": "DLCO/VAmmol/min/kPa/L]", "bbox": [62, 544, 289, 556],
	"text": "1.93", "bbox": [365, 544, 407, 556],
	"text": "1.73", "bbox": [478, 544, 519, 556],
	"text": "89.7", "bbox": [582, 544, 622, 556],
	"text": "Hb", "bbox": [62, 558, 80, 569],
	"text": "[g/100ml]", "bbox": [198, 558, 290, 570],
	"text": "13.40", "bbox": [468, 558, 519, 570],
	"text": "VA", "bbox": [62, 572, 80, 583],
	"text": "[L]", "bbox": [264, 572, 290, 584],
	"text": "4.22", "bbox": [365, 572, 407, 584],
	"text": "3.95", "bbox": [478, 572, 519, 584],
	"text": "93.6", "bbox": [582, 572, 622, 584],
	"text": "DLCOc SB[mmol/min/kPa]", "bbox": [62, 586, 289, 597],
	"text": "8.44", "bbox": [365, 586, 407, 597],
	"text": "6.84", "bbox": [478, 586, 519, 597],
	"text": "81.0", "bbox": [582, 586, 622, 597],
	"text": "DLCOc/VAmmol/min/kPa/L]", "bbox": [62, 600, 289, 612],
	"text": "1.93", "bbox": [365, 600, 407, 612],
	"text": "1.73", "bbox": [478, 600, 519, 612],
	"text": "89.7", "bbox": [582, 600, 622, 612],
	"text": "VIN", "bbox": [62, 629, 90, 640],
	"text": "[L]", "bbox": [264, 629, 290, 641],
	"text": "3.20", "bbox": [365, 629, 407, 641],
	"text": "2.72", "bbox": [478, 629, 519, 641],
	"text": "85.0", "bbox": [582, 629, 622, 641],
	"text": "Insp. time", "bbox": [62, 643, 163, 655],
	"text": "[s]", "bbox": [264, 643, 290, 655],
	"text": "0.95", "bbox": [478, 643, 519, 655],
	"text": "Exp. time", "bbox": [62, 657, 152, 669],
	"text": "[s]", "bbox": [264, 657, 290, 669],
	"text": "1.95", "bbox": [478, 657, 519, 669],
	"text": "Sample vol", "bbox": [62, 671, 161, 683],
	"text": "[L]", "bbox": [264, 671, 290, 683],
	"text": "System dead space [ml]", "bbox": [62, 685, 289, 697],
	"text": "172.00", "bbox": [460, 685, 519, 697],
	"text": "Anatom. dead space[ml]", "bbox": [62, 699, 289, 711],
	"text": "148.50", "bbox": [460, 699, 519, 711],
	"text": "TA", "bbox": [62, 714, 78, 725],
	"text": "[s]", "bbox": [264, 714, 290, 726],
	"text": "11.32", "bbox": [470, 712, 519, 724],
	"text": "测试结果：", "bbox": [47, 730, 167, 748],
	"text": "Vol [L]", "bbox": [657, 241, 700, 253],
	"text": "Time [min]", "bbox": [745, 334, 800, 344],
	"text": "PredAdj.0", "bbox": [627, 350, 678, 360],
	"text": "0.2", "bbox": [703, 350, 720, 360],
	"text": "0.4", "bbox": [745, 350, 761, 360],
	"text": "0.6", "bbox": [786, 350, 803, 360],
	"text": "0.8", "bbox": [828, 350, 845, 360],
	"text": "1.0", "bbox": [870, 350, 886, 360],
	"text": "Flow [L/s]", "bbox": [657, 368, 707, 379],
	"text": "F/V ex", "bbox": [788, 368, 820, 378],
	"text": "10", "bbox": [637, 380, 651, 389],
	"text": "5", "bbox": [642, 400, 651, 409],
	"text": "0", "bbox": [642, 420, 651, 429],
	"text": "2", "bbox": [707, 430, 716, 439],
	"text": "4", "bbox": [764, 430, 772, 439],
	"text": "6", "bbox": [820, 430, 828, 439],
	"text": "5", "bbox": [642, 442, 651, 451],
	"text": "10", "bbox": [637, 462, 651, 471],
	"text": "F/V in", "bbox": [792, 472, 820, 481],
	"text": "Vol [L]", "bbox": [657, 495, 692, 507],
	"text": "100", "bbox": [633, 516, 651, 525],
	"text": "50", "bbox": [637, 558, 651, 567],
	"text": "0", "bbox": [642, 599, 651, 608],
	"text": "Time [s]", "bbox": [745, 590, 784, 601],
	"text": "10", "bbox": [792, 607, 805, 616],
	"text": "15", "bbox": [863, 607, 875, 616],
	"text": "Volume [L]", "bbox": [662, 627, 719, 638],
	"text": "4", "bbox": [649, 635, 657, 644],
	"text": "2", "bbox": [649, 657, 657, 666],
	"text": "0", "bbox": [649, 678, 657, 687],
	"text": "2", "bbox": [649, 700, 657, 709],
	"text": "4", "bbox": [649, 721, 657, 730],
	"text": "10", "bbox": [705, 741, 719, 750],
	"text": "20", "bbox": [752, 741, 766, 750],
	"text": "30", "bbox": [800, 741, 813, 750],
	"text": "40", "bbox": [847, 741, 860, 750],
	"text": "Time [s]", "bbox": [748, 723, 791, 734],
	"text": "FRCP th", "bbox": [627, 308, 673, 318],
	"text": "RV", "bbox": [627, 327, 644, 338],
	"text": "Vol [L]", "bbox": [830, 495, 865, 507],
	"text": "10", "bbox": [871, 516, 884, 525],
	"text": "10", "bbox": [871, 548, 884, 557],
	"text": "10", "bbox": [871, 599, 884, 608],
	"text": "10", "bbox": [871, 635, 884, 644],
	"text": "10", "bbox": [871, 678, 884, 687],
	"text": "10", "bbox": [871, 700, 884, 709],
	"text": "10", "bbox": [871, 721, 884, 730],
	"text": "10", "bbox": [871, 741, 884, 750],
	"text": "10", "bbox": [871, 762, 884, 771],
	"text": "10", "bbox": [871, 784, 884, 793],
	"text": "10", "bbox": [871, 805, 884, 814],
	"text": "10", "bbox": [871, 827, 884, 836],
	"text": "10", "bbox": [871, 848, 884, 857],
	"text": "10", "bbox": [871, 870, 884, 879],
	"text": "10", "bbox": [871, 891, 884, 900],
	"text": "10", "bbox": [871, 913, 884, 922],
	"text": "10", "bbox": [871, 934, 884, 943],
	"text": "10", "bbox": [871, 956, 884, 965],
	"text": "10", "bbox": [871, 977, 884, 986],
	"text": "10", "bbox": [871, 999, 884, 1008],
	"text": "10", "bbox": [871, 1020, 884, 1029],
	"text": "10", "bbox": [871, 1042, 884, 1051],
	"text": "10", "bbox": [871, 1063, 884, 1072],
	"text": "10", "bbox": [871, 1085, 884, 1094],
	"text": "10", "bbox": [871, 1106, 884, 1115],
	"text": "10", "bbox": [871, 1128, 884, 1137],
	"text": "10", "bbox": [871, 1149, 884, 1158],
	"text": "10", "bbox": [871, 1171, 884, 1180],
	"text": "10", "bbox": [871, 1192, 884, 1201],
	"text": "10", "bbox": [871, 1214, 884, 1223],
	"text": "10", "bbox": [871, 1235, 884, 1244],
	"text": "10", "bbox": [871, 1257, 884, 1266],
	"text": "10", "bbox": [871, 1278, 884, 1287],
	"text": "10", "bbox": [871, 1300, 884, 1309],
	"text": "10", "bbox": [871, 1321, 884, 1330],
	"text": "10", "bbox": [871, 1343, 884, 1352],
	"text": "10", "bbox": [871, 1364, 884, 1373],
	"text": "10", "bbox": [871, 1386, 884, 1395],
	"text": "10", "bbox": [871, 1407, 884, 1416],
	"text": "10", "bbox": [871, 1429, 884, 1438],
	"text": "10", "bbox": [871, 1450, 884, 1459],
	"text": "10", "bbox": [871, 1472, 884, 1481],
	"text": "10", "bbox": [871, 1493, 884, 1502],
	"text": "10", "bbox": [871, 1515, 884, 1524],
	"text": "10", "bbox": [871, 1536, 884, 1545],
	"text": "10", "bbox": [871, 1558, 884, 1567],
	"text": "10", "bbox": [871, 1579, 884, 1588],
	"text": "10", "bbox": [871, 1601, 884, 1610],
	"text": "10", "bbox": [871, 1622, 884, 1631],
	"text": "10", "bbox": [871, 1644, 884, 1653],
	"text": "10", "bbox": [871, 1665, 884, 1674],
	"text": "10", "bbox": [871, 1687, 884, 1696],
	"text": "10", "bbox": [871, 1708, 884, 1717],
	"text": "10", "bbox": [871, 1730, 884, 1739],
	"text": "10", "bbox": [871, 1751, 884, 1760],
	"text": "10", "bbox": [871, 1773, 884, 1782],
	"text": "10", "bbox": [871, 1794, 884, 1803],
	"text": "10", "bbox": [871, 1816, 884, 1825],
	"text": "10", "bbox": [871, 1837, 884, 1846],
	"text": "10", "bbox": [871, 1859, 884, 1868],
	"text": "10", "bbox": [871, 1880, 884, 1889],
	"text": "10", "bbox": [871, 1902, 884, 1911],
	"text": "10", "bbox": [871, 1923, 884, 1932],
	"text": "10", "bbox": [871, 1945, 884, 1954],
	"text": "10", "bbox": [871, 1966, 884, 1975],
	"text": "10", "bbox": [871, 1988, 
2026-08-10 12:59:13,370 INFO     29 [qwen-vl-text] coord JSON strict parse failed, trying json_repair
2026-08-10 12:59:13,374 INFO     29 [qwen-vl-text] coord API: raw_items=254, valid_items=253, elapsed=73.3s
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[0]: text=JAEGER PCMED, bbox=[708, 63, 900, 80]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[1]: text=渑池县人民医院, bbox=[370, 82, 586, 104]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[2]: text=肺功能检查报告, bbox=[404, 107, 555, 124]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[3]: text=综合测试, bbox=[446, 128, 534, 144]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[65, 144, 112, 156]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[5]: text=性别：女, bbox=[65, 156, 255, 169]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[6]: text=年龄：29 Years, bbox=[65, 169, 313, 181]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[7]: text=身高：154 cm, bbox=[65, 181, 296, 193]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[8]: text=体重：67.5 kg, bbox=[65, 193, 303, 205]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[9]: text=备注：, bbox=[65, 204, 112, 216]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[10]: text=联系电话：, bbox=[414, 147, 498, 159]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[11]: text=住院号：0, bbox=[414, 159, 592, 171]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[12]: text=测试号：2025052701, bbox=[414, 171, 674, 183]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[13]: text=吸烟史：, bbox=[414, 183, 480, 194]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[14]: text=既往史：, bbox=[414, 194, 480, 206]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[15]: text=职业：, bbox=[414, 206, 462, 217]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[16]: text=测试日期, bbox=[63, 251, 147, 264]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[17]: text=测试时间, bbox=[63, 264, 147, 278]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[18]: text=预计值, bbox=[345, 239, 407, 252]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[19]: text=实测值, bbox=[458, 239, 519, 252]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[20]: text=实/预, bbox=[571, 239, 622, 252]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[21]: text=25/5/27, bbox=[448, 253, 519, 265]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[22]: text=10:10:05上, bbox=[417, 266, 519, 278]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[23]: text=VC MAX, bbox=[62, 294, 127, 305]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[24]: text=[L], bbox=[264, 294, 290, 306]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[25]: text=3.20, bbox=[365, 294, 407, 306]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[26]: text=2.87, bbox=[478, 294, 519, 306]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[27]: text=89.6, bbox=[582, 294, 622, 306]
2026-08-10 12:59:13,375 INFO     29 [qwen-vl-text] coord item[28]: text=FVC, bbox=[62, 308, 94, 319]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[29]: text=[L], bbox=[264, 308, 290, 320]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[30]: text=3.18, bbox=[365, 308, 407, 320]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[31]: text=2.79, bbox=[478, 308, 519, 320]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[32]: text=87.6, bbox=[582, 308, 622, 320]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[33]: text=MV, bbox=[62, 322, 85, 333]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[34]: text=[L/min], bbox=[222, 322, 290, 334]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[35]: text=9.64, bbox=[365, 322, 407, 334]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[36]: text=25.12, bbox=[468, 322, 519, 334]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[37]: text=260.5, bbox=[571, 322, 622, 334]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[38]: text=FEV 1, bbox=[62, 336, 114, 347]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[39]: text=[L], bbox=[264, 336, 290, 348]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[40]: text=2.76, bbox=[365, 336, 407, 348]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[41]: text=1.57, bbox=[478, 336, 519, 348]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[42]: text=57.0, bbox=[582, 336, 622, 348]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[43]: text=FEV 1 % FVC, bbox=[62, 350, 177, 361]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[44]: text=[%], bbox=[264, 350, 290, 362]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[45]: text=84.23, bbox=[355, 350, 407, 362]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[46]: text=56.40, bbox=[468, 350, 519, 362]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[47]: text=67.0, bbox=[582, 350, 622, 362]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[48]: text=PEF, bbox=[62, 364, 94, 375]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[49]: text=[L/s], bbox=[243, 364, 290, 376]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[50]: text=6.49, bbox=[365, 364, 407, 376]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[51]: text=3.62, bbox=[478, 364, 519, 376]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[52]: text=55.8, bbox=[582, 364, 622, 376]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[53]: text=MEF 75, bbox=[62, 378, 124, 389]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[54]: text=[L/s], bbox=[243, 378, 290, 390]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[55]: text=5.83, bbox=[365, 378, 407, 390]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[56]: text=2.32, bbox=[478, 378, 519, 390]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[57]: text=39.8, bbox=[582, 378, 622, 390]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[58]: text=MEF 50, bbox=[62, 392, 124, 403]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[59]: text=[L/s], bbox=[243, 392, 290, 404]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[60]: text=4.21, bbox=[365, 392, 407, 404]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[61]: text=0.76, bbox=[478, 392, 519, 404]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[62]: text=18.0, bbox=[582, 392, 622, 404]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[63]: text=MEF 25, bbox=[62, 406, 124, 417]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[64]: text=[L/s], bbox=[243, 406, 290, 418]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[65]: text=2.00, bbox=[365, 406, 407, 418]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[66]: text=0.23, bbox=[478, 406, 519, 418]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[67]: text=11.6, bbox=[582, 406, 622, 418]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[68]: text=MMEF 75/25, bbox=[62, 419, 165, 430]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[69]: text=[L/s], bbox=[243, 419, 290, 431]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[70]: text=3.86, bbox=[365, 419, 407, 431]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[71]: text=0.58, bbox=[478, 419, 519, 431]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[72]: text=14.9, bbox=[582, 419, 622, 431]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[73]: text=MVV, bbox=[62, 433, 94, 444]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[74]: text=[L/min], bbox=[222, 433, 290, 445]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[75]: text=105.09, bbox=[345, 433, 407, 445]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[76]: text=71.84, bbox=[468, 433, 519, 445]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[77]: text=68.4, bbox=[582, 433, 622, 445]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[78]: text=TLC-SB, bbox=[62, 461, 124, 472]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[79]: text=[L], bbox=[264, 461, 290, 473]
2026-08-10 12:59:13,376 INFO     29 [qwen-vl-text] coord item[80]: text=4.37, bbox=[365, 461, 407, 473]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[81]: text=4.10, bbox=[478, 461, 519, 473]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[82]: text=93.8, bbox=[582, 461, 622, 473]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[83]: text=RV-SB, bbox=[62, 475, 112, 486]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[84]: text=[L], bbox=[264, 475, 290, 487]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[85]: text=1.25, bbox=[365, 475, 407, 487]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[86]: text=1.38, bbox=[478, 475, 519, 487]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[87]: text=110.4, bbox=[571, 475, 622, 487]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[88]: text=RV%TLC-SB, bbox=[62, 489, 155, 500]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[89]: text=[%], bbox=[264, 489, 290, 501]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[90]: text=28.82, bbox=[355, 489, 407, 501]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[91]: text=33.70, bbox=[468, 489, 519, 501]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[92]: text=116.9, bbox=[571, 489, 622, 501]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[93]: text=FRC-SB, bbox=[62, 503, 124, 514]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[94]: text=[L], bbox=[264, 503, 290, 515]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[95]: text=2.48, bbox=[365, 503, 407, 515]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[96]: text=2.31, bbox=[478, 503, 519, 515]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[97]: text=93.1, bbox=[582, 503, 622, 515]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[98]: text=FRC%TLC-SB, bbox=[62, 517, 165, 528]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[99]: text=[%], bbox=[264, 517, 290, 529]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[100]: text=49.74, bbox=[355, 517, 407, 529]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[101]: text=56.25, bbox=[468, 517, 519, 529]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[102]: text=113.1, bbox=[571, 517, 622, 529]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[103]: text=DLCO SB [mmol/min/kPa], bbox=[62, 530, 289, 542]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[104]: text=8.44, bbox=[365, 530, 407, 542]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[105]: text=6.84, bbox=[478, 530, 519, 542]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[106]: text=81.0, bbox=[582, 530, 622, 542]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[107]: text=DLCO/VAmmol/min/kPa/L], bbox=[62, 544, 289, 556]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[108]: text=1.93, bbox=[365, 544, 407, 556]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[109]: text=1.73, bbox=[478, 544, 519, 556]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[110]: text=89.7, bbox=[582, 544, 622, 556]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[111]: text=Hb, bbox=[62, 558, 80, 569]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[112]: text=[g/100ml], bbox=[198, 558, 290, 570]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[113]: text=13.40, bbox=[468, 558, 519, 570]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[114]: text=VA, bbox=[62, 572, 80, 583]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[115]: text=[L], bbox=[264, 572, 290, 584]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[116]: text=4.22, bbox=[365, 572, 407, 584]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[117]: text=3.95, bbox=[478, 572, 519, 584]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[118]: text=93.6, bbox=[582, 572, 622, 584]
2026-08-10 12:59:13,377 INFO     29 [qwen-vl-text] coord item[119]: text=DLCOc SB[mmol/min/kPa], bbox=[62, 586, 289, 597]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[120]: text=8.44, bbox=[365, 586, 407, 597]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[121]: text=6.84, bbox=[478, 586, 519, 597]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[122]: text=81.0, bbox=[582, 586, 622, 597]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[123]: text=DLCOc/VAmmol/min/kPa/L], bbox=[62, 600, 289, 612]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[124]: text=1.93, bbox=[365, 600, 407, 612]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[125]: text=1.73, bbox=[478, 600, 519, 612]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[126]: text=89.7, bbox=[582, 600, 622, 612]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[127]: text=VIN, bbox=[62, 629, 90, 640]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[128]: text=[L], bbox=[264, 629, 290, 641]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[129]: text=3.20, bbox=[365, 629, 407, 641]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[130]: text=2.72, bbox=[478, 629, 519, 641]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[131]: text=85.0, bbox=[582, 629, 622, 641]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[132]: text=Insp. time, bbox=[62, 643, 163, 655]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[133]: text=[s], bbox=[264, 643, 290, 655]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[134]: text=0.95, bbox=[478, 643, 519, 655]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[135]: text=Exp. time, bbox=[62, 657, 152, 669]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[136]: text=[s], bbox=[264, 657, 290, 669]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[137]: text=1.95, bbox=[478, 657, 519, 669]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[138]: text=Sample vol, bbox=[62, 671, 161, 683]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[139]: text=[L], bbox=[264, 671, 290, 683]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[140]: text=System dead space [ml], bbox=[62, 685, 289, 697]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[141]: text=172.00, bbox=[460, 685, 519, 697]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[142]: text=Anatom. dead space[ml], bbox=[62, 699, 289, 711]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[143]: text=148.50, bbox=[460, 699, 519, 711]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[144]: text=TA, bbox=[62, 714, 78, 725]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[145]: text=[s], bbox=[264, 714, 290, 726]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[146]: text=11.32, bbox=[470, 712, 519, 724]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[147]: text=测试结果：, bbox=[47, 730, 167, 748]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[148]: text=Vol [L], bbox=[657, 241, 700, 253]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[149]: text=Time [min], bbox=[745, 334, 800, 344]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[150]: text=PredAdj.0, bbox=[627, 350, 678, 360]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[151]: text=0.2, bbox=[703, 350, 720, 360]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[152]: text=0.4, bbox=[745, 350, 761, 360]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[153]: text=0.6, bbox=[786, 350, 803, 360]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[154]: text=0.8, bbox=[828, 350, 845, 360]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[155]: text=1.0, bbox=[870, 350, 886, 360]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[156]: text=Flow [L/s], bbox=[657, 368, 707, 379]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[157]: text=F/V ex, bbox=[788, 368, 820, 378]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[158]: text=10, bbox=[637, 380, 651, 389]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[159]: text=5, bbox=[642, 400, 651, 409]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[160]: text=0, bbox=[642, 420, 651, 429]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[161]: text=2, bbox=[707, 430, 716, 439]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[162]: text=4, bbox=[764, 430, 772, 439]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[163]: text=6, bbox=[820, 430, 828, 439]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[164]: text=5, bbox=[642, 442, 651, 451]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[165]: text=10, bbox=[637, 462, 651, 471]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[166]: text=F/V in, bbox=[792, 472, 820, 481]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[167]: text=Vol [L], bbox=[657, 495, 692, 507]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[168]: text=100, bbox=[633, 516, 651, 525]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[169]: text=50, bbox=[637, 558, 651, 567]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[170]: text=0, bbox=[642, 599, 651, 608]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[171]: text=Time [s], bbox=[745, 590, 784, 601]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[172]: text=10, bbox=[792, 607, 805, 616]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[173]: text=15, bbox=[863, 607, 875, 616]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[174]: text=Volume [L], bbox=[662, 627, 719, 638]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[175]: text=4, bbox=[649, 635, 657, 644]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[176]: text=2, bbox=[649, 657, 657, 666]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[177]: text=0, bbox=[649, 678, 657, 687]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[178]: text=2, bbox=[649, 700, 657, 709]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[179]: text=4, bbox=[649, 721, 657, 730]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[180]: text=10, bbox=[705, 741, 719, 750]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[181]: text=20, bbox=[752, 741, 766, 750]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[182]: text=30, bbox=[800, 741, 813, 750]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[183]: text=40, bbox=[847, 741, 860, 750]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[184]: text=Time [s], bbox=[748, 723, 791, 734]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[185]: text=FRCP th, bbox=[627, 308, 673, 318]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[186]: text=RV, bbox=[627, 327, 644, 338]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[187]: text=Vol [L], bbox=[830, 495, 865, 507]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[188]: text=10, bbox=[871, 516, 884, 525]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[189]: text=10, bbox=[871, 548, 884, 557]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[190]: text=10, bbox=[871, 599, 884, 608]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[191]: text=10, bbox=[871, 635, 884, 644]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[192]: text=10, bbox=[871, 678, 884, 687]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[193]: text=10, bbox=[871, 700, 884, 709]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[194]: text=10, bbox=[871, 721, 884, 730]
2026-08-10 12:59:13,378 INFO     29 [qwen-vl-text] coord item[195]: text=10, bbox=[871, 741, 884, 750]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[196]: text=10, bbox=[871, 762, 884, 771]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[197]: text=10, bbox=[871, 784, 884, 793]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[198]: text=10, bbox=[871, 805, 884, 814]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[199]: text=10, bbox=[871, 827, 884, 836]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[200]: text=10, bbox=[871, 848, 884, 857]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[201]: text=10, bbox=[871, 870, 884, 879]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[202]: text=10, bbox=[871, 891, 884, 900]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[203]: text=10, bbox=[871, 913, 884, 922]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[204]: text=10, bbox=[871, 934, 884, 943]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[205]: text=10, bbox=[871, 956, 884, 965]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[206]: text=10, bbox=[871, 977, 884, 986]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[207]: text=10, bbox=[871, 999, 884, 1008]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[208]: text=10, bbox=[871, 1020, 884, 1029]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[209]: text=10, bbox=[871, 1042, 884, 1051]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[210]: text=10, bbox=[871, 1063, 884, 1072]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[211]: text=10, bbox=[871, 1085, 884, 1094]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[212]: text=10, bbox=[871, 1106, 884, 1115]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[213]: text=10, bbox=[871, 1128, 884, 1137]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[214]: text=10, bbox=[871, 1149, 884, 1158]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[215]: text=10, bbox=[871, 1171, 884, 1180]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[216]: text=10, bbox=[871, 1192, 884, 1201]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[217]: text=10, bbox=[871, 1214, 884, 1223]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[218]: text=10, bbox=[871, 1235, 884, 1244]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[219]: text=10, bbox=[871, 1257, 884, 1266]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[220]: text=10, bbox=[871, 1278, 884, 1287]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[221]: text=10, bbox=[871, 1300, 884, 1309]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[222]: text=10, bbox=[871, 1321, 884, 1330]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[223]: text=10, bbox=[871, 1343, 884, 1352]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[224]: text=10, bbox=[871, 1364, 884, 1373]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[225]: text=10, bbox=[871, 1386, 884, 1395]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[226]: text=10, bbox=[871, 1407, 884, 1416]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[227]: text=10, bbox=[871, 1429, 884, 1438]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[228]: text=10, bbox=[871, 1450, 884, 1459]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[229]: text=10, bbox=[871, 1472, 884, 1481]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[230]: text=10, bbox=[871, 1493, 884, 1502]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[231]: text=10, bbox=[871, 1515, 884, 1524]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[232]: text=10, bbox=[871, 1536, 884, 1545]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[233]: text=10, bbox=[871, 1558, 884, 1567]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[234]: text=10, bbox=[871, 1579, 884, 1588]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[235]: text=10, bbox=[871, 1601, 884, 1610]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[236]: text=10, bbox=[871, 1622, 884, 1631]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[237]: text=10, bbox=[871, 1644, 884, 1653]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[238]: text=10, bbox=[871, 1665, 884, 1674]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[239]: text=10, bbox=[871, 1687, 884, 1696]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[240]: text=10, bbox=[871, 1708, 884, 1717]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[241]: text=10, bbox=[871, 1730, 884, 1739]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[242]: text=10, bbox=[871, 1751, 884, 1760]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[243]: text=10, bbox=[871, 1773, 884, 1782]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[244]: text=10, bbox=[871, 1794, 884, 1803]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[245]: text=10, bbox=[871, 1816, 884, 1825]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[246]: text=10, bbox=[871, 1837, 884, 1846]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[247]: text=10, bbox=[871, 1859, 884, 1868]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[248]: text=10, bbox=[871, 1880, 884, 1889]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[249]: text=10, bbox=[871, 1902, 884, 1911]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[250]: text=10, bbox=[871, 1923, 884, 1932]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[251]: text=10, bbox=[871, 1945, 884, 1954]
2026-08-10 12:59:13,379 INFO     29 [qwen-vl-text] coord item[252]: text=10, bbox=[871, 1966, 884, 1975]
2026-08-10 12:59:13,382 INFO     29 [qwen-vl-text] page=3 — 4025/4025 coords, api_time=73.3s
2026-08-10 12:59:13,387 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3139659, prompt_len=2361
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共109行）
["JAEGER PCMED", "渑池县人民医院", "肺功能检查报告", "常规通气", "姓名：", "住院号：0", "性别：女", "身高：154 cm", "标准体重：125 %", "吸烟史：", "科别：", "测试号：2025052701", "年龄：29 Years", "体重：67.5 kg", "体表面积：1.66 m", "测试日期 25/5/27", "测试时间 10:10:05", "预计值 实测值 实测/预", "VC MAX [L] 3.20 2.87 89.6", "IRV [L] 1.14", "ERV [L] 1.23 0.92 75.3", "IC [L] 1.97 1.94 98.4", "VT [L] 0.48 0.80 166.0", "MV [L/min] 9.64 25.12 260.5", "VC IN [L] 3.20 2.87 89.6", "VC EX [L] 3.20 2.82 88.0", "BF [1/min] 20.00 31.39 157.0", "FVC [L] 3.18 2.79 87.6", "PEF [L/s] 6.49 3.62 55.8", "FEV 0.5 [L] 1.15", "FEV 1 [L] 2.76 1.57 57.0", "FEV 2 [L] 1.98", "FEV 3 [L] 2.21", "FEV6 [L] 2.61", "FEF 200-1200 [L/s] 2.06", "FEV 1 % FVC [%] 84.23 56.40 67.0", "FEV 1 % VC MAX [%] 83.59 54.79 65.5", "MEF 75 [L/s] 5.83 2.32 39.8", "MEF 50 [L/s] 4.21 0.76 18.0", "MEF 25 [L/s] 2.00 0.23 11.6", "MMEF 75/25 [L/s] 3.86 0.58 14.9", "FEF 75/85 [L/s] 1.22 0.16 13.3", "FEF50 % FIF50 [%] 19.86", "PIF [L/s] 4.32", "FVC IN [L] 3.20 2.72 84.9", "FET [s] 8.39", "FIF 50 [L/s] 3.80", "FIV1 [L] 2.68", "FIV1 % FVC [%] 98.67", "T IN [s] 0.84", "T EX [s] 1.07", "T TOT [s] 1.91", "MIF [L/s] 0.95", "MEF [L/s] 0.75", "MVV [L/min] 105.09 71.84 68.4", "FEF50 % FIF50 [%] 19.86", "V backextrapolation ex [L] 0.04", "V backextrapol. % FVC [%] 1.50", "测试结果", "1、中重度阻塞性肺通气功能障碍，小气道功能降低。", "2、肺弥散功能正常。", "3、残气量、残气量/肺总量正常。", "4、沙丁胺醇气雾剂支气管舒张试验呈阳性，FEV1.0改善17.1%。", "5、建议定期复查。", "报告医师：李朝红/王晓红 报告日期：2025.5.27", "6 Vol [L]", "TLC 4", "FRCPth", "RV", "PredAdt.0 0.2 0.4 0.6 0.8 1.0", "Time [min]", "Flow [L/s]", "F/V ex", "10", "5", "0", "2", "4", "6", "10", "5", "10", "F/V in", "Vol%VCmax", "0", "20", "40", "60", "80", "100", "Vol [L]", "2", "VCmax", "4", "6", "8", "Time [s]", "4", "Vol [L]", "2", "0", "2", "4", "6", "8", "10", "12", "14", "Time [s]"]

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
2026-08-10 12:59:47,519 INFO     29 [qwen-vl-text] coord API raw response (len=6485):
[
	{"text": "JAEGER PCMED", "bbox": [724, 59, 905, 73]},
	{"text": "渑池县人民医院", "bbox": [365, 70, 617, 93]},
	{"text": "肺功能检查报告", "bbox": [393, 96, 595, 113]},
	{"text": "常规通气", "bbox": [448, 118, 548, 133]},
	{"text": "姓名：", "bbox": [116, 135, 164, 147]},
	{"text": "住院号：", "bbox": [116, 147, 180, 159]},
	{"text": "性别：", "bbox": [116, 158, 164, 170]},
	{"text": "身高：", "bbox": [116, 170, 164, 182]},
	{"text": "标准体重：", "bbox": [116, 181, 197, 193]},
	{"text": "吸烟史：", "bbox": [116, 192, 180, 204]},
	{"text": "科别：", "bbox": [453, 138, 498, 150]},
	{"text": "测试号：", "bbox": [453, 149, 515, 161]},
	{"text": "年龄：", "bbox": [453, 160, 498, 172]},
	{"text": "体重：", "bbox": [453, 171, 498, 183]},
	{"text": "体表面积：", "bbox": [453, 182, 533, 194]},
	{"text": "测试日期 25/5/27", "bbox": [116, 220, 191, 233]},
	{"text": "测试时间 10:10:05", "bbox": [116, 232, 191, 244]},
	{"text": "预计值 实测值 实测/预", "bbox": [381, 208, 600, 221]},
	{"text": "VC MAX [L] 3.20 2.87 89.6", "bbox": [114, 257, 600, 270]},
	{"text": "IRV [L] 1.14", "bbox": [114, 269, 518, 282]},
	{"text": "ERV [L] 1.23 0.92 75.3", "bbox": [114, 281, 600, 294]},
	{"text": "IC [L] 1.97 1.94 98.4", "bbox": [114, 293, 600, 306]},
	{"text": "VT [L] 0.48 0.80 166.0", "bbox": [114, 305, 600, 318]},
	{"text": "MV [L/min] 9.64 25.12 260.5", "bbox": [290, 317, 600, 330]},
	{"text": "VC IN [L] 3.20 2.87 89.6", "bbox": [114, 330, 600, 343]},
	{"text": "VC EX [L] 3.20 2.82 88.0", "bbox": [114, 342, 600, 355]},
	{"text": "BF [1/min] 20.00 31.39 157.0", "bbox": [290, 354, 600, 367]},
	{"text": "FVC [L] 3.18 2.79 87.6", "bbox": [114, 366, 600, 379]},
	{"text": "PEF [L/s] 6.49 3.62 55.8", "bbox": [308, 378, 600, 391]},
	{"text": "FEV 0.5 [L] 1.15", "bbox": [111, 403, 518, 416]},
	{"text": "FEV 1 [L] 2.76 1.57 57.0", "bbox": [111, 415, 600, 428]},
	{"text": "FEV 2 [L] 1.98", "bbox": [111, 427, 518, 440]},
	{"text": "FEV 3 [L] 2.21", "bbox": [111, 439, 518, 452]},
	{"text": "FEV6 [L] 2.61", "bbox": [111, 451, 518, 464]},
	{"text": "FEF 200-1200 [L/s] 2.06", "bbox": [111, 463, 518, 476]},
	{"text": "FEV 1 % FVC [%] 84.23 56.40 67.0", "bbox": [108, 490, 600, 503]},
	{"text": "FEV 1 % VC MAX [%] 83.59 54.79 65.5", "bbox": [108, 502, 600, 515]},
	{"text": "MEF 75 [L/s] 5.83 2.32 39.8", "bbox": [108, 514, 600, 527]},
	{"text": "MEF 50 [L/s] 4.21 0.76 18.0", "bbox": [108, 526, 600, 539]},
	{"text": "MEF 25 [L/s] 2.00 0.23 11.6", "bbox": [108, 538, 600, 551]},
	{"text": "MMEF 75/25 [L/s] 3.86 0.58 14.9", "bbox": [108, 550, 600, 563]},
	{"text": "FEF 75/85 [L/s] 1.22 0.16 13.3", "bbox": [108, 562, 600, 575]},
	{"text": "FEF50 % FIF50 [%] 19.86", "bbox": [105, 574, 518, 587]},
	{"text": "PIF [L/s] 4.32", "bbox": [105, 586, 518, 600]},
	{"text": "FVC IN [L] 3.20 2.72 84.9", "bbox": [105, 600, 600, 613]},
	{"text": "FET [s] 8.39", "bbox": [105, 612, 518, 625]},
	{"text": "FIF 50 [L/s] 3.80", "bbox": [105, 624, 518, 637]},
	{"text": "FIV1 [L] 2.68", "bbox": [105, 636, 518, 649]},
	{"text": "FIV1 % FVC [%] 98.67", "bbox": [105, 648, 518, 661]},
	{"text": "T IN [s] 0.84", "bbox": [105, 660, 518, 673]},
	{"text": "T EX [s] 1.07", "bbox": [105, 672, 518, 685]},
	{"text": "T TOT [s] 1.91", "bbox": [105, 684, 518, 697]},
	{"text": "MIF [L/s] 0.95", "bbox": [105, 696, 518, 709]},
	{"text": "MEF [L/s] 0.75", "bbox": [105, 708, 518, 721]},
	{"text": "MVV [L/min] 105.09 71.84 68.4", "bbox": [105, 720, 600, 733]},
	{"text": "FEF50 % FIF50 [%] 19.86", "bbox": [105, 732, 518, 745]},
	{"text": "V backextrapolation ex [L] 0.04", "bbox": [105, 744, 518, 757]},
	{"text": "V backextrapol. % FVC [%] 1.50", "bbox": [105, 756, 518, 769]},
	{"text": "测试结果", "bbox": [96, 787, 203, 805]},
	{"text": "1、中重度阻塞性肺通气功能障碍，小气道功能降低。", "bbox": [94, 812, 606, 830]},
	{"text": "2、肺弥散功能正常。", "bbox": [94, 829, 294, 847]},
	{"text": "3、残气量、残气量/肺总量正常。", "bbox": [94, 845, 418, 864]},
	{"text": "4、沙丁胺醇气雾剂支气管舒张试验呈阳性，FEV1.0改善17.1%。", "bbox": [94, 860, 707, 879]},
	{"text": "5、建议定期复查。", "bbox": [94, 878, 269, 896]},
	{"text": "报告医师：李朝红/王晓红 报告日期：2025.5.27", "bbox": [397, 900, 880, 927]},
	{"text": "6 Vol [L]", "bbox": [642, 225, 690, 239]},
	{"text": "TLC 4", "bbox": [616, 258, 652, 270]},
	{"text": "FRCPth", "bbox": [616, 292, 660, 303]},
	{"text": "RV", "bbox": [616, 312, 632, 323]},
	{"text": "PredAdt.0 0.2 0.4 0.6 0.8 1.0", "bbox": [616, 334, 871, 345]},
	{"text": "Time [min]", "bbox": [731, 318, 785, 329]},
	{"text": "Flow [L/s]", "bbox": [644, 357, 693, 368]},
	{"text": "F/V ex", "bbox": [773, 358, 805, 367]},
	{"text": "10", "bbox": [624, 368, 638, 377]},
	{"text": "5", "bbox": [630, 388, 638, 397]},
	{"text": "0", "bbox": [630, 408, 638, 417]},
	{"text": "2", "bbox": [695, 417, 703, 425]},
	{"text": "4", "bbox": [750, 417, 758, 425]},
	{"text": "6", "bbox": [805, 417, 813, 425]},
	{"text": "10", "bbox": [624, 448, 638, 457]},
	{"text": "5", "bbox": [630, 428, 638, 437]},
	{"text": "F/V in", "bbox": [777, 459, 805, 468]},
	{"text": "Vol%VCmax", "bbox": [618, 483, 680, 492]},
	{"text": "0", "bbox": [635, 493, 644, 502]},
	{"text": "20", "bbox": [630, 500, 644, 509]},
	{"text": "40", "bbox": [630, 508, 644, 517]},
	{"text": "60", "bbox": [630, 516, 644, 525]},
	{"text": "80", "bbox": [630, 524, 644, 533]},
	{"text": "100", "bbox": [624, 527, 642, 536]},
	{"text": "Vol [L]", "bbox": [665, 497, 699, 507]},
	{"text": "2", "bbox": [652, 517, 660, 525]},
	{"text": "VCmax", "bbox": [679, 525, 714, 533]},
	{"text": "4", "bbox": [652, 541, 660, 549]},
	{"text": "6", "bbox": [652, 566, 660, 574]},
	{"text": "8", "bbox": [652, 590, 660, 598]},
	{"text": "Time [s]", "bbox": [747, 582, 789, 592]},
	{"text": "0", "bbox": [663, 600, 670, 608]},
	{"text": "2", "bbox": [708, 600, 715, 608]},
	{"text": "4", "bbox": [753, 600, 760, 608]},
	{"text": "6", "bbox": [800, 600, 807, 608]},
	{"text": "8", "bbox": [845, 600, 852, 608]},
	{"text": "4", "bbox": [628, 623, 636, 632]},
	{"text": "Vol [L]", "bbox": [644, 627, 676, 637]},
	{"text": "2", "bbox": [628, 650, 636, 658]},
	{"text": "0", "bbox": [628, 676, 636, 684]},
	{"text": "2", "bbox": [628, 704, 636, 712]},
	{"text": "4", "bbox": [628, 731, 636, 739]},
	{"text": "0", "bbox": [639, 741, 647, 749]},
	{"text": "2", "bbox": [671, 741, 678, 749]},
	{"text": "4", "bbox": [702, 741, 709, 749]},
	{"text": "6", "bbox": [734, 741, 741, 749]},
	{"text": "8", "bbox": [765, 741, 772, 749]},
	{"text": "10", "bbox": [794, 741, 805, 749]},
	{"text": "12", "bbox": [825, 741, 837, 749]},
	{"text": "14", "bbox": [857, 741, 868, 749]},
	{"text": "Time [s]", "bbox": [738, 723, 780, 733]}
]
2026-08-10 12:59:47,520 INFO     29 [qwen-vl-text] coord API: raw_items=116, valid_items=116, elapsed=34.1s
2026-08-10 12:59:47,520 INFO     29 [qwen-vl-text] coord item[0]: text=JAEGER PCMED, bbox=[724, 59, 905, 73]
2026-08-10 12:59:47,520 INFO     29 [qwen-vl-text] coord item[1]: text=渑池县人民医院, bbox=[365, 70, 617, 93]
2026-08-10 12:59:47,520 INFO     29 [qwen-vl-text] coord item[2]: text=肺功能检查报告, bbox=[393, 96, 595, 113]
2026-08-10 12:59:47,521 INFO     29 [qwen-vl-text] coord item[3]: text=常规通气, bbox=[448, 118, 548, 133]
2026-08-10 12:59:47,521 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[116, 135, 164, 147]
2026-08-10 12:59:47,521 INFO     29 [qwen-vl-text] coord item[5]: text=住院号：, bbox=[116, 147, 180, 159]
2026-08-10 12:59:47,521 INFO     29 [qwen-vl-text] coord item[6]: text=性别：, bbox=[116, 158, 164, 170]
2026-08-10 12:59:47,521 INFO     29 [qwen-vl-text] coord item[7]: text=身高：, bbox=[116, 170, 164, 182]
2026-08-10 12:59:47,521 INFO     29 [qwen-vl-text] coord item[8]: text=标准体重：, bbox=[116, 181, 197, 193]
2026-08-10 12:59:47,521 INFO     29 [qwen-vl-text] coord item[9]: text=吸烟史：, bbox=[116, 192, 180, 204]
2026-08-10 12:59:47,521 INFO     29 [qwen-vl-text] coord item[10]: text=科别：, bbox=[453, 138, 498, 150]
2026-08-10 12:59:47,521 INFO     29 [qwen-vl-text] coord item[11]: text=测试号：, bbox=[453, 149, 515, 161]
2026-08-10 12:59:47,521 INFO     29 [qwen-vl-text] coord item[12]: text=年龄：, bbox=[453, 160, 498, 172]
2026-08-10 12:59:47,521 INFO     29 [qwen-vl-text] coord item[13]: text=体重：, bbox=[453, 171, 498, 183]
2026-08-10 12:59:47,521 INFO     29 [qwen-vl-text] coord item[14]: text=体表面积：, bbox=[453, 182, 533, 194]
2026-08-10 12:59:47,521 INFO     29 [qwen-vl-text] coord item[15]: text=测试日期 25/5/27, bbox=[116, 220, 191, 233]
2026-08-10 12:59:47,521 INFO     29 [qwen-vl-text] coord item[16]: text=测试时间 10:10:05, bbox=[116, 232, 191, 244]
2026-08-10 12:59:47,521 INFO     29 [qwen-vl-text] coord item[17]: text=预计值 实测值 实测/预, bbox=[381, 208, 600, 221]
2026-08-10 12:59:47,521 INFO     29 [qwen-vl-text] coord item[18]: text=VC MAX [L] 3.20 2.87 89.6, bbox=[114, 257, 600, 270]
2026-08-10 12:59:47,522 INFO     29 [qwen-vl-text] coord item[19]: text=IRV [L] 1.14, bbox=[114, 269, 518, 282]
2026-08-10 12:59:47,522 INFO     29 [qwen-vl-text] coord item[20]: text=ERV [L] 1.23 0.92 75.3, bbox=[114, 281, 600, 294]
2026-08-10 12:59:47,522 INFO     29 [qwen-vl-text] coord item[21]: text=IC [L] 1.97 1.94 98.4, bbox=[114, 293, 600, 306]
2026-08-10 12:59:47,522 INFO     29 [qwen-vl-text] coord item[22]: text=VT [L] 0.48 0.80 166.0, bbox=[114, 305, 600, 318]
2026-08-10 12:59:47,522 INFO     29 [qwen-vl-text] coord item[23]: text=MV [L/min] 9.64 25.12 260.5, bbox=[290, 317, 600, 330]
2026-08-10 12:59:47,522 INFO     29 [qwen-vl-text] coord item[24]: text=VC IN [L] 3.20 2.87 89.6, bbox=[114, 330, 600, 343]
2026-08-10 12:59:47,522 INFO     29 [qwen-vl-text] coord item[25]: text=VC EX [L] 3.20 2.82 88.0, bbox=[114, 342, 600, 355]
2026-08-10 12:59:47,522 INFO     29 [qwen-vl-text] coord item[26]: text=BF [1/min] 20.00 31.39 157.0, bbox=[290, 354, 600, 367]
2026-08-10 12:59:47,522 INFO     29 [qwen-vl-text] coord item[27]: text=FVC [L] 3.18 2.79 87.6, bbox=[114, 366, 600, 379]
2026-08-10 12:59:47,522 INFO     29 [qwen-vl-text] coord item[28]: text=PEF [L/s] 6.49 3.62 55.8, bbox=[308, 378, 600, 391]
2026-08-10 12:59:47,522 INFO     29 [qwen-vl-text] coord item[29]: text=FEV 0.5 [L] 1.15, bbox=[111, 403, 518, 416]
2026-08-10 12:59:47,522 INFO     29 [qwen-vl-text] coord item[30]: text=FEV 1 [L] 2.76 1.57 57.0, bbox=[111, 415, 600, 428]
2026-08-10 12:59:47,522 INFO     29 [qwen-vl-text] coord item[31]: text=FEV 2 [L] 1.98, bbox=[111, 427, 518, 440]
2026-08-10 12:59:47,522 INFO     29 [qwen-vl-text] coord item[32]: text=FEV 3 [L] 2.21, bbox=[111, 439, 518, 452]
2026-08-10 12:59:47,522 INFO     29 [qwen-vl-text] coord item[33]: text=FEV6 [L] 2.61, bbox=[111, 451, 518, 464]
2026-08-10 12:59:47,522 INFO     29 [qwen-vl-text] coord item[34]: text=FEF 200-1200 [L/s] 2.06, bbox=[111, 463, 518, 476]
2026-08-10 12:59:47,522 INFO     29 [qwen-vl-text] coord item[35]: text=FEV 1 % FVC [%] 84.23 56.40 67.0, bbox=[108, 490, 600, 503]
2026-08-10 12:59:47,522 INFO     29 [qwen-vl-text] coord item[36]: text=FEV 1 % VC MAX [%] 83.59 54.79 65.5, bbox=[108, 502, 600, 515]
2026-08-10 12:59:47,523 INFO     29 [qwen-vl-text] coord item[37]: text=MEF 75 [L/s] 5.83 2.32 39.8, bbox=[108, 514, 600, 527]
2026-08-10 12:59:47,523 INFO     29 [qwen-vl-text] coord item[38]: text=MEF 50 [L/s] 4.21 0.76 18.0, bbox=[108, 526, 600, 539]
2026-08-10 12:59:47,523 INFO     29 [qwen-vl-text] coord item[39]: text=MEF 25 [L/s] 2.00 0.23 11.6, bbox=[108, 538, 600, 551]
2026-08-10 12:59:47,523 INFO     29 [qwen-vl-text] coord item[40]: text=MMEF 75/25 [L/s] 3.86 0.58 14.9, bbox=[108, 550, 600, 563]
2026-08-10 12:59:47,523 INFO     29 [qwen-vl-text] coord item[41]: text=FEF 75/85 [L/s] 1.22 0.16 13.3, bbox=[108, 562, 600, 575]
2026-08-10 12:59:47,523 INFO     29 [qwen-vl-text] coord item[42]: text=FEF50 % FIF50 [%] 19.86, bbox=[105, 574, 518, 587]
2026-08-10 12:59:47,523 INFO     29 [qwen-vl-text] coord item[43]: text=PIF [L/s] 4.32, bbox=[105, 586, 518, 600]
2026-08-10 12:59:47,523 INFO     29 [qwen-vl-text] coord item[44]: text=FVC IN [L] 3.20 2.72 84.9, bbox=[105, 600, 600, 613]
2026-08-10 12:59:47,523 INFO     29 [qwen-vl-text] coord item[45]: text=FET [s] 8.39, bbox=[105, 612, 518, 625]
2026-08-10 12:59:47,523 INFO     29 [qwen-vl-text] coord item[46]: text=FIF 50 [L/s] 3.80, bbox=[105, 624, 518, 637]
2026-08-10 12:59:47,523 INFO     29 [qwen-vl-text] coord item[47]: text=FIV1 [L] 2.68, bbox=[105, 636, 518, 649]
2026-08-10 12:59:47,523 INFO     29 [qwen-vl-text] coord item[48]: text=FIV1 % FVC [%] 98.67, bbox=[105, 648, 518, 661]
2026-08-10 12:59:47,523 INFO     29 [qwen-vl-text] coord item[49]: text=T IN [s] 0.84, bbox=[105, 660, 518, 673]
2026-08-10 12:59:47,523 INFO     29 [qwen-vl-text] coord item[50]: text=T EX [s] 1.07, bbox=[105, 672, 518, 685]
2026-08-10 12:59:47,523 INFO     29 [qwen-vl-text] coord item[51]: text=T TOT [s] 1.91, bbox=[105, 684, 518, 697]
2026-08-10 12:59:47,523 INFO     29 [qwen-vl-text] coord item[52]: text=MIF [L/s] 0.95, bbox=[105, 696, 518, 709]
2026-08-10 12:59:47,523 INFO     29 [qwen-vl-text] coord item[53]: text=MEF [L/s] 0.75, bbox=[105, 708, 518, 721]
2026-08-10 12:59:47,523 INFO     29 [qwen-vl-text] coord item[54]: text=MVV [L/min] 105.09 71.84 68.4, bbox=[105, 720, 600, 733]
2026-08-10 12:59:47,523 INFO     29 [qwen-vl-text] coord item[55]: text=FEF50 % FIF50 [%] 19.86, bbox=[105, 732, 518, 745]
2026-08-10 12:59:47,523 INFO     29 [qwen-vl-text] coord item[56]: text=V backextrapolation ex [L] 0.04, bbox=[105, 744, 518, 757]
2026-08-10 12:59:47,523 INFO     29 [qwen-vl-text] coord item[57]: text=V backextrapol. % FVC [%] 1.50, bbox=[105, 756, 518, 769]
2026-08-10 12:59:47,523 INFO     29 [qwen-vl-text] coord item[58]: text=测试结果, bbox=[96, 787, 203, 805]
2026-08-10 12:59:47,524 INFO     29 [qwen-vl-text] coord item[59]: text=1、中重度阻塞性肺通气功能障碍，小气道功能降低。, bbox=[94, 812, 606, 830]
2026-08-10 12:59:47,524 INFO     29 [qwen-vl-text] coord item[60]: text=2、肺弥散功能正常。, bbox=[94, 829, 294, 847]
2026-08-10 12:59:47,524 INFO     29 [qwen-vl-text] coord item[61]: text=3、残气量、残气量/肺总量正常。, bbox=[94, 845, 418, 864]
2026-08-10 12:59:47,524 INFO     29 [qwen-vl-text] coord item[62]: text=4、沙丁胺醇气雾剂支气管舒张试验呈阳性，FEV1.0改善17.1%。, bbox=[94, 860, 707, 879]
2026-08-10 12:59:47,524 INFO     29 [qwen-vl-text] coord item[63]: text=5、建议定期复查。, bbox=[94, 878, 269, 896]
2026-08-10 12:59:47,524 INFO     29 [qwen-vl-text] coord item[64]: text=报告医师：李朝红/王晓红 报告日期：2025.5.27, bbox=[397, 900, 880, 927]
2026-08-10 12:59:47,524 INFO     29 [qwen-vl-text] coord item[65]: text=6 Vol [L], bbox=[642, 225, 690, 239]
2026-08-10 12:59:47,524 INFO     29 [qwen-vl-text] coord item[66]: text=TLC 4, bbox=[616, 258, 652, 270]
2026-08-10 12:59:47,524 INFO     29 [qwen-vl-text] coord item[67]: text=FRCPth, bbox=[616, 292, 660, 303]
2026-08-10 12:59:47,524 INFO     29 [qwen-vl-text] coord item[68]: text=RV, bbox=[616, 312, 632, 323]
2026-08-10 12:59:47,524 INFO     29 [qwen-vl-text] coord item[69]: text=PredAdt.0 0.2 0.4 0.6 0.8 1.0, bbox=[616, 334, 871, 345]
2026-08-10 12:59:47,524 INFO     29 [qwen-vl-text] coord item[70]: text=Time [min], bbox=[731, 318, 785, 329]
2026-08-10 12:59:47,524 INFO     29 [qwen-vl-text] coord item[71]: text=Flow [L/s], bbox=[644, 357, 693, 368]
2026-08-10 12:59:47,524 INFO     29 [qwen-vl-text] coord item[72]: text=F/V ex, bbox=[773, 358, 805, 367]
2026-08-10 12:59:47,524 INFO     29 [qwen-vl-text] coord item[73]: text=10, bbox=[624, 368, 638, 377]
2026-08-10 12:59:47,524 INFO     29 [qwen-vl-text] coord item[74]: text=5, bbox=[630, 388, 638, 397]
2026-08-10 12:59:47,524 INFO     29 [qwen-vl-text] coord item[75]: text=0, bbox=[630, 408, 638, 417]
2026-08-10 12:59:47,524 INFO     29 [qwen-vl-text] coord item[76]: text=2, bbox=[695, 417, 703, 425]
2026-08-10 12:59:47,524 INFO     29 [qwen-vl-text] coord item[77]: text=4, bbox=[750, 417, 758, 425]
2026-08-10 12:59:47,524 INFO     29 [qwen-vl-text] coord item[78]: text=6, bbox=[805, 417, 813, 425]
2026-08-10 12:59:47,524 INFO     29 [qwen-vl-text] coord item[79]: text=10, bbox=[624, 448, 638, 457]
2026-08-10 12:59:47,524 INFO     29 [qwen-vl-text] coord item[80]: text=5, bbox=[630, 428, 638, 437]
2026-08-10 12:59:47,524 INFO     29 [qwen-vl-text] coord item[81]: text=F/V in, bbox=[777, 459, 805, 468]
2026-08-10 12:59:47,524 INFO     29 [qwen-vl-text] coord item[82]: text=Vol%VCmax, bbox=[618, 483, 680, 492]
2026-08-10 12:59:47,525 INFO     29 [qwen-vl-text] coord item[83]: text=0, bbox=[635, 493, 644, 502]
2026-08-10 12:59:47,525 INFO     29 [qwen-vl-text] coord item[84]: text=20, bbox=[630, 500, 644, 509]
2026-08-10 12:59:47,525 INFO     29 [qwen-vl-text] coord item[85]: text=40, bbox=[630, 508, 644, 517]
2026-08-10 12:59:47,525 INFO     29 [qwen-vl-text] coord item[86]: text=60, bbox=[630, 516, 644, 525]
2026-08-10 12:59:47,525 INFO     29 [qwen-vl-text] coord item[87]: text=80, bbox=[630, 524, 644, 533]
2026-08-10 12:59:47,525 INFO     29 [qwen-vl-text] coord item[88]: text=100, bbox=[624, 527, 642, 536]
2026-08-10 12:59:47,525 INFO     29 [qwen-vl-text] coord item[89]: text=Vol [L], bbox=[665, 497, 699, 507]
2026-08-10 12:59:47,525 INFO     29 [qwen-vl-text] coord item[90]: text=2, bbox=[652, 517, 660, 525]
2026-08-10 12:59:47,525 INFO     29 [qwen-vl-text] coord item[91]: text=VCmax, bbox=[679, 525, 714, 533]
2026-08-10 12:59:47,525 INFO     29 [qwen-vl-text] coord item[92]: text=4, bbox=[652, 541, 660, 549]
2026-08-10 12:59:47,525 INFO     29 [qwen-vl-text] coord item[93]: text=6, bbox=[652, 566, 660, 574]
2026-08-10 12:59:47,525 INFO     29 [qwen-vl-text] coord item[94]: text=8, bbox=[652, 590, 660, 598]
2026-08-10 12:59:47,525 INFO     29 [qwen-vl-text] coord item[95]: text=Time [s], bbox=[747, 582, 789, 592]
2026-08-10 12:59:47,525 INFO     29 [qwen-vl-text] coord item[96]: text=0, bbox=[663, 600, 670, 608]
2026-08-10 12:59:47,525 INFO     29 [qwen-vl-text] coord item[97]: text=2, bbox=[708, 600, 715, 608]
2026-08-10 12:59:47,525 INFO     29 [qwen-vl-text] coord item[98]: text=4, bbox=[753, 600, 760, 608]
2026-08-10 12:59:47,525 INFO     29 [qwen-vl-text] coord item[99]: text=6, bbox=[800, 600, 807, 608]
2026-08-10 12:59:47,525 INFO     29 [qwen-vl-text] coord item[100]: text=8, bbox=[845, 600, 852, 608]
2026-08-10 12:59:47,525 INFO     29 [qwen-vl-text] coord item[101]: text=4, bbox=[628, 623, 636, 632]
2026-08-10 12:59:47,525 INFO     29 [qwen-vl-text] coord item[102]: text=Vol [L], bbox=[644, 627, 676, 637]
2026-08-10 12:59:47,525 INFO     29 [qwen-vl-text] coord item[103]: text=2, bbox=[628, 650, 636, 658]
2026-08-10 12:59:47,526 INFO     29 [qwen-vl-text] coord item[104]: text=0, bbox=[628, 676, 636, 684]
2026-08-10 12:59:47,526 INFO     29 [qwen-vl-text] coord item[105]: text=2, bbox=[628, 704, 636, 712]
2026-08-10 12:59:47,526 INFO     29 [qwen-vl-text] coord item[106]: text=4, bbox=[628, 731, 636, 739]
2026-08-10 12:59:47,526 INFO     29 [qwen-vl-text] coord item[107]: text=0, bbox=[639, 741, 647, 749]
2026-08-10 12:59:47,526 INFO     29 [qwen-vl-text] coord item[108]: text=2, bbox=[671, 741, 678, 749]
2026-08-10 12:59:47,526 INFO     29 [qwen-vl-text] coord item[109]: text=4, bbox=[702, 741, 709, 749]
2026-08-10 12:59:47,526 INFO     29 [qwen-vl-text] coord item[110]: text=6, bbox=[734, 741, 741, 749]
2026-08-10 12:59:47,526 INFO     29 [qwen-vl-text] coord item[111]: text=8, bbox=[765, 741, 772, 749]
2026-08-10 12:59:47,526 INFO     29 [qwen-vl-text] coord item[112]: text=10, bbox=[794, 741, 805, 749]
2026-08-10 12:59:47,526 INFO     29 [qwen-vl-text] coord item[113]: text=12, bbox=[825, 741, 837, 749]
2026-08-10 12:59:47,526 INFO     29 [qwen-vl-text] coord item[114]: text=14, bbox=[857, 741, 868, 749]
2026-08-10 12:59:47,526 INFO     29 [qwen-vl-text] coord item[115]: text=Time [s], bbox=[738, 723, 780, 733]
2026-08-10 12:59:47,527 INFO     29 [qwen-vl-text] page=4 — 109/109 coords, api_time=34.1s
2026-08-10 12:59:47,533 INFO     29 [qwen-vl-text] new_positions (4248):
[[2, 442.68, 552.755, 37.89, 53.046], [2, 244.545, 376.635, 54.73, 75.78], [2, 252.28, 362.95, 79.148, 94.304], [2, 277.865, 330.82, 98.514, 112.828], [2, 76.16, 104.72, 112.828, 123.774], [2, 76.16, 116.02499999999999, 123.774, 133.878], [2, 76.16, 104.72, 133.878, 143.982], [2, 180.88, 192.185, 134.72, 144.82399999999998], [2, 76.16, 104.72, 143.982, 154.08599999999998], [2, 180.88, 215.98499999999999, 145.666, 154.928], [2, 76.16, 127.33, 154.08599999999998, 164.19], [2, 180.88, 215.98499999999999, 155.76999999999998, 165.03199999999998], [2, 76.16, 116.02499999999999, 164.19, 174.29399999999998], [2, 289.16999999999996, 317.135, 116.196, 126.3], [2, 289.16999999999996, 328.44, 126.3, 136.404], [2, 289.16999999999996, 317.135, 136.404, 146.50799999999998], [2, 289.16999999999996, 317.135, 146.50799999999998, 156.612], [2, 289.16999999999996, 339.15, 156.612, 166.716], [2, 94.60499999999999, 126.14, 206.29, 215.552], [2, 220.14999999999998, 240.975, 207.974, 215.552], [2, 314.15999999999997, 351.645, 204.606, 212.184], [2, 323.68, 339.15, 212.184, 220.60399999999998], [2, 343.315, 363.54499999999996, 215.552, 224.814], [2, 82.705, 91.63, 223.13, 230.708], [2, 320.705, 329.63, 223.13, 230.708], [2, 320.705, 329.63, 233.23399999999998, 240.81199999999998], [2, 320.705, 329.63, 243.338, 251.75799999999998], [2, 334.39, 339.15, 243.338, 251.75799999999998], [2, 320.705, 329.63, 253.44199999999998, 261.02], [2, 85.67999999999999, 91.63, 248.39, 255.126], [2, 317.72999999999996, 329.63, 264.388, 271.966], [2, 351.05, 373.65999999999997, 261.86199999999997, 269.44], [2, 296.31, 301.07, 270.282, 277.86], [2, 296.31, 301.07, 279.544, 287.122], [2, 85.67999999999999, 91.63, 273.65, 281.228], [2, 116.02499999999999, 121.38, 282.07, 289.64799999999997], [2, 142.79999999999998, 148.75, 282.07, 289.64799999999997], [2, 168.385, 173.73999999999998, 282.07, 289.64799999999997], [2, 193.97, 199.325, 282.07, 289.64799999999997], [2, 219.55499999999998, 224.91, 282.07, 289.64799999999997], [2, 244.545, 249.89999999999998, 282.07, 289.64799999999997], [2, 270.13, 275.485, 282.07, 289.64799999999997], [2, 334.39, 339.15, 274.492, 282.07], [2, 334.39, 339.15, 305.646, 313.224], [2, 82.705, 91.63, 324.17, 331.748], [2, 220.14999999999998, 240.975, 340.168, 348.58799999999997], [2, 420.66499999999996, 446.84499999999997, 329.222, 337.642], [2, 334.39, 339.15, 336.8, 344.378], [2, 340.34, 345.09999999999997, 344.378, 351.95599999999996], [2, 366.52, 371.28, 344.378, 351.95599999999996], [2, 392.7, 397.46, 344.378, 351.95599999999996], [2, 418.88, 423.64, 344.378, 351.95599999999996], [2, 445.06, 449.82, 344.378, 351.95599999999996], [2, 469.455, 476.59499999999997, 344.378, 351.95599999999996], [2, 495.635, 502.775, 344.378, 351.95599999999996], [2, 520.625, 528.36, 344.378, 351.95599999999996], [2, 76.16, 123.75999999999999, 369.638, 380.584], [2, 76.16, 123.75999999999999, 380.584, 391.53], [2, 245.73499999999999, 280.84, 357.84999999999997, 368.796], [2, 308.805, 332.01, 357.84999999999997, 368.796], [2, 354.62, 383.775, 357.84999999999997, 368.796], [2, 411.74, 434.34999999999997, 357.84999999999997, 368.796], [2, 456.96, 485.52, 357.84999999999997, 368.796], [2, 502.17999999999995, 535.5, 357.84999999999997, 368.796], [2, 291.55, 332.01, 370.47999999999996, 379.74199999999996], [2, 394.48499999999996, 434.34999999999997, 370.47999999999996, 379.74199999999996], [2, 286.78999999999996, 332.01, 381.426, 390.688], [2, 389.13, 434.34999999999997, 381.426, 390.688], [2, 76.16, 113.05, 404.15999999999997, 412.58], [2, 212.415, 227.885, 404.15999999999997, 413.42199999999997], [2, 257.635, 280.84, 404.15999999999997, 412.58], [2, 308.805, 332.01, 404.15999999999997, 412.58], [2, 359.97499999999997, 383.775, 404.15999999999997, 412.58], [2, 411.74, 434.34999999999997, 404.15999999999997, 412.58], [2, 456.96, 485.52, 404.15999999999997, 412.58], [2, 513.485, 536.095, 404.15999999999997, 412.58], [2, 76.16, 95.19999999999999, 415.106, 423.526], [2, 212.415, 227.885, 415.106, 424.368], [2, 257.635, 280.84, 415.106, 423.526], [2, 308.805, 332.01, 415.106, 423.526], [2, 359.97499999999997, 383.775, 415.106, 423.526], [2, 411.74, 434.34999999999997, 415.106, 423.526], [2, 456.96, 485.52, 415.106, 423.526], [2, 513.485, 536.095, 415.106, 423.526], [2, 76.16, 105.315, 426.05199999999996, 434.472], [2, 212.415, 227.885, 426.05199999999996, 435.31399999999996], [2, 257.635, 280.84, 426.05199999999996, 434.472], [2, 308.805, 332.01, 426.05199999999996, 434.472], [2, 359.97499999999997, 383.775, 426.05199999999996, 434.472], [2, 411.74, 434.34999999999997, 426.05199999999996, 434.472], [2, 462.90999999999997, 485.52, 426.05199999999996, 434.472], [2, 513.485, 536.095, 426.05199999999996, 434.472], [2, 76.16, 142.20499999999998, 436.998, 445.418], [2, 212.415, 227.885, 436.998, 446.26], [2, 251.685, 280.84, 436.998, 445.418], [2, 303.45, 332.01, 436.998, 445.418], [2, 359.97499999999997, 383.775, 436.998, 445.418], [2, 406.385, 434.34999999999997, 436.998, 445.418], [2, 462.90999999999997, 485.52, 436.998, 445.418], [2, 513.485, 536.095, 436.998, 445.418], [2, 76.16, 159.45999999999998, 447.94399999999996, 456.364], [2, 212.415, 227.885, 447.94399999999996, 457.20599999999996], [2, 251.685, 280.84, 447.94399999999996, 456.364], [2, 303.45, 332.01, 447.94399999999996, 456.364], [2, 359.97499999999997, 383.775, 447.94399999999996, 456.364], [2, 406.385, 434.34999999999997, 447.94399999999996, 456.364], [2, 462.90999999999997, 485.52, 447.94399999999996, 456.364], [2, 513.485, 536.095, 447.94399999999996, 456.364], [2, 76.16, 95.19999999999999, 458.89, 467.31], [2, 201.10999999999999, 227.885, 458.89, 468.152], [2, 257.635, 280.84, 458.89, 467.31], [2, 308.805, 332.01, 458.89, 467.31], [2, 359.97499999999997, 383.775, 458.89, 467.31], [2, 411.74, 434.34999999999997, 458.89, 467.31], [3, 421.26, 535.5, 53.046, 67.36], [3, 220.14999999999998, 348.66999999999996, 69.044, 87.568], [3, 240.38, 330.22499999999997, 90.094, 104.408], [3, 265.37, 317.72999999999996, 107.776, 121.24799999999999], [3, 38.675, 66.64, 121.24799999999999, 131.352], [3, 38.675, 151.725, 131.352, 142.298], [3, 38.675, 186.23499999999999, 142.298, 152.402], [3, 38.675, 176.12, 152.402, 162.506], [3, 38.675, 180.285, 162.506, 172.60999999999999], [3, 38.675, 66.64, 171.768, 181.87199999999999], [3, 246.32999999999998, 296.31, 123.774, 133.878], [3, 246.32999999999998, 352.24, 133.878, 143.982], [3, 246.32999999999998, 401.03, 143.982, 154.08599999999998], [3, 246.32999999999998, 285.59999999999997, 154.08599999999998, 163.34799999999998], [3, 246.32999999999998, 285.59999999999997, 163.34799999999998, 173.452], [3, 246.32999999999998, 274.89, 173.452, 182.714], [3, 37.485, 87.46499999999999, 211.34199999999998, 222.28799999999998], [3, 37.485, 87.46499999999999, 222.28799999999998, 234.076], [3, 205.27499999999998, 242.165, 201.238, 212.184], [3, 272.51, 308.805, 201.238, 212.184], [3, 339.745, 370.09, 201.238, 212.184], [3, 266.56, 308.805, 213.02599999999998, 223.13], [3, 248.11499999999998, 308.805, 223.97199999999998, 234.076], [3, 36.89, 75.565, 247.548, 256.81], [3, 157.07999999999998, 172.54999999999998, 247.548, 257.652], [3, 217.17499999999998, 242.165, 247.548, 257.652], [3, 284.40999999999997, 308.805, 247.548, 257.652], [3, 346.28999999999996, 370.09, 247.548, 257.652], [3, 36.89, 55.93, 259.336, 268.598], [3, 157.07999999999998, 172.54999999999998, 259.336, 269.44], [3, 217.17499999999998, 242.165, 259.336, 269.44], [3, 284.40999999999997, 308.805, 259.336, 269.44], [3, 346.28999999999996, 370.09, 259.336, 269.44], [3, 36.89, 50.574999999999996, 271.12399999999997, 280.38599999999997], [3, 132.09, 172.54999999999998, 271.12399999999997, 281.228], [3, 217.17499999999998, 242.165, 271.12399999999997, 281.228], [3, 278.46, 308.805, 271.12399999999997, 281.228], [3, 339.745, 370.09, 271.12399999999997, 281.228], [3, 36.89, 67.83, 282.912, 292.174], [3, 157.07999999999998, 172.54999999999998, 282.912, 293.01599999999996], [3, 217.17499999999998, 242.165, 282.912, 293.01599999999996], [3, 284.40999999999997, 308.805, 282.912, 293.01599999999996], [3, 346.28999999999996, 370.09, 282.912, 293.01599999999996], [3, 36.89, 105.315, 294.7, 303.962], [3, 157.07999999999998, 172.54999999999998, 294.7, 304.804], [3, 211.225, 242.165, 294.7, 304.804], [3, 278.46, 308.805, 294.7, 304.804], [3, 346.28999999999996, 370.09, 294.7, 304.804], [3, 36.89, 55.93, 306.488, 315.75], [3, 144.58499999999998, 172.54999999999998, 306.488, 316.592], [3, 217.17499999999998, 242.165, 306.488, 316.592], [3, 284.40999999999997, 308.805, 306.488, 316.592], [3, 346.28999999999996, 370.09, 306.488, 316.592], [3, 36.89, 73.78, 318.276, 327.538], [3, 144.58499999999998, 172.54999999999998, 318.276, 328.38], [3, 217.17499999999998, 242.165, 318.276, 328.38], [3, 284.40999999999997, 308.805, 318.276, 328.38], [3, 346.28999999999996, 370.09, 318.276, 328.38], [3, 36.89, 73.78, 330.06399999999996, 339.32599999999996], [3, 144.58499999999998, 172.54999999999998, 330.06399999999996, 340.168], [3, 217.17499999999998, 242.165, 330.06399999999996, 340.168], [3, 284.40999999999997, 308.805, 330.06399999999996, 340.168], [3, 346.28999999999996, 370.09, 330.06399999999996, 340.168], [3, 36.89, 73.78, 341.852, 351.114], [3, 144.58499999999998, 172.54999999999998, 341.852, 351.95599999999996], [3, 217.17499999999998, 242.165, 341.852, 351.95599999999996], [3, 284.40999999999997, 308.805, 341.852, 351.95599999999996], [3, 346.28999999999996, 370.09, 341.852, 351.95599999999996], [3, 36.89, 98.175, 352.798, 362.06], [3, 144.58499999999998, 172.54999999999998, 352.798, 362.902], [3, 217.17499999999998, 242.165, 352.798, 362.902], [3, 284.40999999999997, 308.805, 352.798, 362.902], [3, 346.28999999999996, 370.09, 352.798, 362.902], [3, 36.89, 55.93, 364.586, 373.848], [3, 132.09, 172.54999999999998, 364.586, 374.69], [3, 205.27499999999998, 242.165, 364.586, 374.69], [3, 278.46, 308.805, 364.586, 374.69], [3, 346.28999999999996, 370.09, 364.586, 374.69], [3, 36.89, 73.78, 388.162, 397.424], [3, 157.07999999999998, 172.54999999999998, 388.162, 398.26599999999996], [3, 217.17499999999998, 242.165, 388.162, 398.26599999999996], [3, 284.40999999999997, 308.805, 388.162, 398.26599999999996], [3, 346.28999999999996, 370.09, 388.162, 398.26599999999996], [3, 36.89, 66.64, 399.95, 409.212], [3, 157.07999999999998, 172.54999999999998, 399.95, 410.054], [3, 217.17499999999998, 242.165, 399.95, 410.054], [3, 284.40999999999997, 308.805, 399.95, 410.054], [3, 339.745, 370.09, 399.95, 410.054], [3, 36.89, 92.225, 411.738, 421.0], [3, 157.07999999999998, 172.54999999999998, 411.738, 421.842], [3, 211.225, 242.165, 411.738, 421.842], [3, 278.46, 308.805, 411.738, 421.842], [3, 339.745, 370.09, 411.738, 421.842], [3, 36.89, 73.78, 423.526, 432.788], [3, 157.07999999999998, 172.54999999999998, 423.526, 433.63], [3, 217.17499999999998, 242.165, 423.526, 433.63], [3, 284.40999999999997, 308.805, 423.526, 433.63], [3, 346.28999999999996, 370.09, 423.526, 433.63], [3, 36.89, 98.175, 435.31399999999996, 444.57599999999996], [3, 157.07999999999998, 172.54999999999998, 435.31399999999996, 445.418], [3, 211.225, 242.165, 435.31399999999996, 445.418], [3, 278.46, 308.805, 435.31399999999996, 445.418], [3, 339.745, 370.09, 435.31399999999996, 445.418], [3, 36.89, 171.95499999999998, 446.26, 456.364], [3, 217.17499999999998, 242.165, 446.26, 456.364], [3, 284.40999999999997, 308.805, 446.26, 456.364], [3, 346.28999999999996, 370.09, 446.26, 456.364], [3, 36.89, 171.95499999999998, 458.048, 468.152], [3, 217.17499999999998, 242.165, 458.048, 468.152], [3, 284.40999999999997, 308.805, 458.048, 468.152], [3, 346.28999999999996, 370.09, 458.048, 468.152], [3, 36.89, 47.599999999999994, 469.83599999999996, 479.09799999999996], [3, 117.80999999999999, 172.54999999999998, 469.83599999999996, 479.94], [3, 278.46, 308.805, 469.83599999999996, 479.94], [3, 36.89, 47.599999999999994, 481.62399999999997, 490.88599999999997], [3, 157.07999999999998, 172.54999999999998, 481.62399999999997, 491.728], [3, 217.17499999999998, 242.165, 481.62399999999997, 491.728], [3, 284.40999999999997, 308.805, 481.62399999999997, 491.728], [3, 346.28999999999996, 370.09, 481.62399999999997, 491.728], [3, 36.89, 171.95499999999998, 493.412, 502.674], [3, 217.17499999999998, 242.165, 493.412, 502.674], [3, 284.40999999999997, 308.805, 493.412, 502.674], [3, 346.28999999999996, 370.09, 493.412, 502.674], [3, 36.89, 171.95499999999998, 505.2, 515.304], [3, 217.17499999999998, 242.165, 505.2, 515.304], [3, 284.40999999999997, 308.805, 505.2, 515.304], [3, 346.28999999999996, 370.09, 505.2, 515.304], [3, 36.89, 53.55, 529.6179999999999, 538.88], [3, 157.07999999999998, 172.54999999999998, 529.6179999999999, 539.722], [3, 217.17499999999998, 242.165, 529.6179999999999, 539.722], [3, 284.40999999999997, 308.805, 529.6179999999999, 539.722], [3, 346.28999999999996, 370.09, 529.6179999999999, 539.722], [3, 36.89, 96.985, 541.406, 551.51], [3, 157.07999999999998, 172.54999999999998, 541.406, 551.51], [3, 284.40999999999997, 308.805, 541.406, 551.51], [3, 36.89, 90.44, 553.194, 563.298], [3, 157.07999999999998, 172.54999999999998, 553.194, 563.298], [3, 284.40999999999997, 308.805, 553.194, 563.298], [3, 36.89, 95.795, 564.982, 575.086], [3, 157.07999999999998, 172.54999999999998, 564.982, 575.086], [3, 36.89, 171.95499999999998, 576.77, 586.874], [3, 273.7, 308.805, 576.77, 586.874], [3, 36.89, 171.95499999999998, 588.558, 598.662], [3, 273.7, 308.805, 588.558, 598.662], [3, 36.89, 46.41, 601.188, 610.4499999999999], [3, 157.07999999999998, 172.54999999999998, 601.188, 611.292], [3, 279.65, 308.805, 599.504, 609.608], [3, 27.965, 99.365, 614.66, 629.816], [3, 390.91499999999996, 416.5, 202.922, 213.02599999999998], [3, 443.275, 476.0, 281.228, 289.64799999999997], [3, 373.065, 403.40999999999997, 294.7, 303.12], [3, 418.28499999999997, 428.4, 294.7, 303.12], [3, 443.275, 452.79499999999996, 294.7, 303.12], [3, 467.66999999999996, 477.78499999999997, 294.7, 303.12], [3, 492.65999999999997, 502.775, 294.7, 303.12], [3, 517.65, 527.17, 294.7, 303.12], [3, 390.91499999999996, 420.66499999999996, 309.856, 319.118], [3, 468.85999999999996, 487.9, 309.856, 318.276], [3, 379.015, 387.34499999999997, 319.96, 327.538], [3, 381.99, 387.34499999999997, 336.8, 344.378], [3, 381.99, 387.34499999999997, 353.64, 361.21799999999996], [3, 420.66499999999996, 426.02, 362.06, 369.638], [3, 454.58, 459.34, 362.06, 369.638], [3, 487.9, 492.65999999999997, 362.06, 369.638], [3, 381.99, 387.34499999999997, 372.164, 379.74199999999996], [3, 379.015, 387.34499999999997, 389.00399999999996, 396.582], [3, 471.23999999999995, 487.9, 397.424, 405.002], [3, 390.91499999999996, 411.74, 416.78999999999996, 426.894], [3, 376.635, 387.34499999999997, 434.472, 442.05], [3, 379.015, 387.34499999999997, 469.83599999999996, 477.414], [3, 381.99, 387.34499999999997, 504.358, 511.936], [3, 443.275, 466.47999999999996, 496.78, 506.042], [3, 471.23999999999995, 478.97499999999997, 511.094, 518.672], [3, 513.485, 520.625, 511.094, 518.672], [3, 393.89, 427.805, 527.934, 537.196], [3, 386.155, 390.91499999999996, 534.67, 542.2479999999999], [3, 386.155, 390.91499999999996, 553.194, 560.7719999999999], [3, 386.155, 390.91499999999996, 570.876, 578.454], [3, 386.155, 390.91499999999996, 589.4, 596.978], [3, 386.155, 390.91499999999996, 607.082, 614.66], [3, 419.47499999999997, 427.805, 623.922, 631.5], [3, 447.44, 455.77, 623.922, 631.5], [3, 476.0, 483.73499999999996, 623.922, 631.5], [3, 503.965, 511.7, 623.922, 631.5], [3, 445.06, 470.645, 608.766, 618.028], [3, 373.065, 400.435, 259.336, 267.756], [3, 373.065, 383.18, 275.334, 284.596], [3, 493.84999999999997, 514.675, 416.78999999999996, 426.894], [3, 518.245, 525.98, 434.472, 442.05], [3, 518.245, 525.98, 461.416, 468.99399999999997], [3, 518.245, 525.98, 504.358, 511.936], [3, 518.245, 525.98, 534.67, 542.2479999999999], [3, 518.245, 525.98, 570.876, 578.454], [3, 518.245, 525.98, 589.4, 596.978], [3, 518.245, 525.98, 607.082, 614.66], [3, 518.245, 525.98, 623.922, 631.5], [3, 518.245, 525.98, 641.6039999999999, 649.182], [3, 518.245, 525.98, 660.1279999999999, 667.706], [3, 518.245, 525.98, 677.81, 685.3879999999999], [3, 518.245, 525.98, 696.334, 703.9119999999999], [3, 518.245, 525.98, 714.016, 721.5939999999999], [3, 518.245, 525.98, 732.54, 740.1179999999999], [3, 518.245, 525.98, 750.222, 757.8], [3, 518.245, 525.98, 768.746, 776.324], [3, 518.245, 525.98, 786.428, 794.006], [3, 518.245, 525.98, 804.952, 812.53], [3, 518.245, 525.98, 822.634, 830.212], [3, 518.245, 525.98, 841.158, 848.736], [3, 518.245, 525.98, 858.8399999999999, 866.418], [3, 518.245, 525.98, 877.3639999999999, 884.942], [3, 518.245, 525.98, 895.0459999999999, 902.624], [3, 518.245, 525.98, 913.5699999999999, 921.148], [3, 518.245, 525.98, 931.252, 938.8299999999999], [3, 518.245, 525.98, 949.776, 957.3539999999999], [3, 518.245, 525.98, 967.458, 975.036], [3, 518.245, 525.98, 985.982, 993.56], [3, 518.245, 525.98, 1003.664, 1011.242], [3, 518.245, 525.98, 1022.188, 1029.766], [3, 518.245, 525.98, 1039.87, 1047.4479999999999], [3, 518.245, 525.98, 1058.394, 1065.972], [3, 518.245, 525.98, 1076.076, 1083.654], [3, 518.245, 525.98, 1094.6, 1102.1779999999999], [3, 518.245, 525.98, 1112.282, 1119.86], [3, 518.245, 525.98, 1130.806, 1138.384], [3, 518.245, 525.98, 1148.488, 1156.066], [3, 518.245, 525.98, 1167.012, 1174.59], [3, 518.245, 525.98, 1184.694, 1192.272], [3, 518.245, 525.98, 1203.2179999999998, 1210.796], [3, 518.245, 525.98, 1220.8999999999999, 1228.478], [3, 518.245, 525.98, 1239.424, 1247.002], [3, 518.245, 525.98, 1257.106, 1264.684], [3, 518.245, 525.98, 1275.6299999999999, 1283.2079999999999], [3, 518.245, 525.98, 1293.312, 1300.8899999999999], [3, 518.245, 525.98, 1311.836, 1319.414], [3, 518.245, 525.98, 1329.518, 1337.096], [3, 518.245, 525.98, 1348.042, 1355.62], [3, 518.245, 525.98, 1365.724, 1373.302], [3, 518.245, 525.98, 1384.248, 1391.826], [3, 518.245, 525.98, 1401.93, 1409.508], [3, 518.245, 525.98, 1420.454, 1428.032], [3, 518.245, 525.98, 1438.136, 1445.714], [3, 518.245, 525.98, 1456.6599999999999, 1464.238], [3, 518.245, 525.98, 1474.3419999999999, 1481.9199999999998], [3, 518.245, 525.98, 1492.866, 1500.444], [3, 518.245, 525.98, 1510.548, 1518.126], [3, 518.245, 525.98, 1529.072, 1536.6499999999999], [3, 518.245, 525.98, 1546.754, 1554.3319999999999], [3, 518.245, 525.98, 1565.278, 1572.856], [3, 518.245, 525.98, 1582.96, 1590.538], [3, 518.245, 525.98, 1601.484, 1609.062], [3, 518.245, 525.98, 1619.166, 1626.744], [3, 518.245, 525.98, 1637.69, 1645.268], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [3, 518.245, 525.98, 1655.3719999999998, 1662.95], [4, 430.78, 538.475, 49.678, 61.466], [4, 217.17499999999998, 367.115, 58.94, 78.306], [4, 233.83499999999998, 354.025, 80.832, 95.146], [4, 266.56, 326.06, 99.356, 111.98599999999999], [4, 69.02, 97.58, 113.67, 123.774], [4, 69.02, 107.1, 123.774, 133.878], [4, 69.02, 97.58, 133.036, 143.14], [4, 69.02, 97.58, 143.14, 153.244], [4, 69.02, 117.21499999999999, 152.402, 162.506], [4, 69.02, 107.1, 161.664, 171.768], [4, 269.53499999999997, 296.31, 116.196, 126.3], [4, 269.53499999999997, 306.425, 125.458, 135.56199999999998], [4, 269.53499999999997, 296.31, 134.72, 144.82399999999998], [4, 269.53499999999997, 296.31, 143.982, 154.08599999999998], [4, 269.53499999999997, 317.135, 153.244, 163.34799999999998], [4, 69.02, 113.645, 185.23999999999998, 196.186], [4, 69.02, 113.645, 195.344, 205.44799999999998], [4, 226.695, 357.0, 175.136, 186.082], [4, 67.83, 357.0, 216.394, 227.34], [4, 67.83, 308.21, 226.498, 237.444], [4, 67.83, 357.0, 236.602, 247.548], [4, 67.83, 357.0, 246.706, 257.652], [4, 67.83, 357.0, 256.81, 267.756], [4, 172.54999999999998, 357.0, 266.914, 277.86], [4, 67.83, 357.0, 277.86, 288.806], [4, 67.83, 357.0, 287.964, 298.90999999999997], [4, 172.54999999999998, 357.0, 298.068, 309.014], [4, 67.83, 357.0, 308.17199999999997, 319.118], [4, 183.26, 357.0, 318.276, 329.222], [4, 66.045, 308.21, 339.32599999999996, 350.272], [4, 66.045, 357.0, 349.43, 360.376], [4, 66.045, 308.21, 359.534, 370.47999999999996], [4, 66.045, 308.21, 369.638, 380.584], [4, 66.045, 308.21, 379.74199999999996, 390.688], [4, 66.045, 308.21, 389.846, 400.792], [4, 64.25999999999999, 357.0, 412.58, 423.526], [4, 64.25999999999999, 357.0, 422.68399999999997, 433.63], [4, 64.25999999999999, 357.0, 432.788, 443.734], [4, 64.25999999999999, 357.0, 442.892, 453.83799999999997], [4, 64.25999999999999, 357.0, 452.996, 463.942], [4, 64.25999999999999, 357.0, 463.09999999999997, 474.046], [4, 64.25999999999999, 357.0, 473.204, 484.15], [4, 62.474999999999994, 308.21, 483.308, 494.25399999999996], [4, 62.474999999999994, 308.21, 493.412, 505.2], [4, 62.474999999999994, 357.0, 505.2, 516.146], [4, 62.474999999999994, 308.21, 515.304, 526.25], [4, 62.474999999999994, 308.21, 525.408, 536.3539999999999], [4, 62.474999999999994, 308.21, 535.512, 546.458], [4, 62.474999999999994, 308.21, 545.616, 556.562], [4, 62.474999999999994, 308.21, 555.72, 566.6659999999999], [4, 62.474999999999994, 308.21, 565.824, 576.77], [4, 62.474999999999994, 308.21, 575.928, 586.874], [4, 62.474999999999994, 308.21, 586.0319999999999, 596.978], [4, 62.474999999999994, 308.21, 596.136, 607.082], [4, 62.474999999999994, 357.0, 606.24, 617.1859999999999], [4, 62.474999999999994, 308.21, 616.3439999999999, 627.29], [4, 62.474999999999994, 308.21, 626.448, 637.394], [4, 62.474999999999994, 308.21, 636.552, 647.4979999999999], [4, 57.12, 120.785, 662.654, 677.81], [4, 55.93, 360.57, 683.704, 698.86], [4, 55.93, 174.92999999999998, 698.018, 713.174], [4, 55.93, 248.70999999999998, 711.49, 727.4879999999999], [4, 55.93, 420.66499999999996, 724.12, 740.1179999999999], [4, 55.93, 160.055, 739.276, 754.432], [4, 236.215, 523.6, 757.8, 780.534], [4, 381.99, 410.54999999999995, 189.45, 201.238], [4, 366.52, 387.94, 217.236, 227.34], [4, 366.52, 392.7, 245.864, 255.126], [4, 366.52, 376.03999999999996, 262.704, 271.966], [4, 366.52, 518.245, 281.228, 290.49], [4, 434.945, 467.075, 267.756, 277.018], [4, 383.18, 412.335, 300.594, 309.856], [4, 459.935, 478.97499999999997, 301.436, 309.014], [4, 371.28, 379.60999999999996, 309.856, 317.43399999999997], [4, 374.84999999999997, 379.60999999999996, 326.69599999999997, 334.274], [4, 374.84999999999997, 379.60999999999996, 343.536, 351.114], [4, 413.525, 418.28499999999997, 351.114, 357.84999999999997], [4, 446.25, 451.01, 351.114, 357.84999999999997], [4, 478.97499999999997, 483.73499999999996, 351.114, 357.84999999999997], [4, 371.28, 379.60999999999996, 377.216, 384.794], [4, 374.84999999999997, 379.60999999999996, 360.376, 367.954], [4, 462.315, 478.97499999999997, 386.478, 394.056], [4, 367.71, 404.59999999999997, 406.686, 414.264], [4, 377.825, 383.18, 415.106, 422.68399999999997], [4, 374.84999999999997, 383.18, 421.0, 428.578], [4, 374.84999999999997, 383.18, 427.736, 435.31399999999996], [4, 374.84999999999997, 383.18, 434.472, 442.05], [4, 374.84999999999997, 383.18, 441.20799999999997, 448.786], [4, 371.28, 381.99, 443.734, 451.312], [4, 395.67499999999995, 415.905, 418.474, 426.894], [4, 387.94, 392.7, 435.31399999999996, 442.05], [4, 404.005, 424.83, 442.05, 448.786], [4, 387.94, 392.7, 455.522, 462.258], [4, 387.94, 392.7, 476.572, 483.308], [4, 387.94, 392.7, 496.78, 503.51599999999996], [4, 444.465, 469.455, 490.044, 498.464], [4, 394.48499999999996, 398.65, 505.2, 511.936], [4, 421.26, 425.42499999999995, 505.2, 511.936], [4, 448.03499999999997, 452.2, 505.2, 511.936], [4, 476.0, 480.16499999999996, 505.2, 511.936], [4, 502.775, 506.94, 505.2, 511.936], [4, 373.65999999999997, 378.41999999999996, 524.566, 532.144], [4, 383.18, 402.21999999999997, 527.934, 536.3539999999999], [4, 373.65999999999997, 378.41999999999996, 547.3, 554.036], [4, 373.65999999999997, 378.41999999999996, 569.192, 575.928], [4, 373.65999999999997, 378.41999999999996, 592.768, 599.504], [4, 373.65999999999997, 378.41999999999996, 615.502, 622.2379999999999], [4, 380.205, 384.965, 623.922, 630.658], [4, 399.245, 403.40999999999997, 623.922, 630.658]]
2026-08-10 12:59:47,534 INFO     29 [qwen-vl-text] ═══ DONE ═══ 4248 positions, pages=3, time=172.8s
2026-08-10 12:59:47,553 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 12:59:47,554 INFO     29 [Trace] task=7ac5bf0e | doc=FXJI 三门峡.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items, types={'ExaminationReport': 1}", "html": "", "json": "4283 items", "markdown": "", "text": "", "name": "FXJI 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 12:59:47,554 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 12:59:47,554 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T12:59:47.554+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 35, "failed": 0, "current": {"7ac5bf0e94ba11f1bd9827cf206dfa2d": {"id": "7ac5bf0e94ba11f1bd9827cf206dfa2d", "doc_id": "7a7d42ec94ba11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "FXJI \u4e09\u95e8\u5ce1.pdf", "type": "pdf", "location": "FXJI \u4e09\u95e8\u5ce1.pdf", "size": 8000159, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786366406983, "task_type": "dataflow", "root_trace_id": "bc9b9d974a834eb18f6171d96f843bf1", "root_traceparent": "00-bc9b9d974a834eb18f6171d96f843bf1-0c5099cebc4db2c7-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 12:59:47,561 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:59:47,561 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 12:59:48,472 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 12:59:48,476 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 12:59:48,476 INFO     29 [Trace] task=7ac5bf0e | doc=FXJI 三门峡.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "4283 items", "markdown": "", "text": "", "name": "FXJI 三门峡.pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 12:59:48,477 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 12:59:48,482 INFO     29 [ChunkMerger] Merged 2 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 7 noise chunks)
2026-08-10 12:59:48,490 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 12:59:48,490 INFO     29 [Trace] task=7ac5bf0e | doc=FXJI 三门峡.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}", "name": "FXJI 三门峡.pdf"}
2026-08-10 12:59:48,490 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 12:59:48,588 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786366407468, 'update_date': datetime.datetime(2026, 8, 10, 12, 53, 27), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1006915, 'status': '1'}
2026-08-10 12:59:48,805 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=渑池县人民医院
门诊病历
姓名:
门诊号: 773264
就诊时间:2025-05-27 09:30 科别: 呼吸与危重症医学科门诊
姓名:范心静 性别:女 年龄:29岁 婚否:已婚
职业:自由职业 工作单位:无
联系电话: 住址:河南省三门峡市渑池县郭窑村15
组
病史叙述者:本人 身份证号
过敏史:无
主诉:咳嗽、咳痰、胸闷、气喘1周。
现病史:患者于1周前受凉后出现咳嗽、咳痰、胸闷、气喘,痰为白
色粘稠痰,咳出困难,夜间及清晨咳嗽明显,活动后胸闷、气喘,
自行给予“喘息定片”药物治疗,症状无改善。
既往史:平素身体良好;无特殊疾病史;否认“肝炎、结核”等病史;
否认手术史;否认外伤史;否认输血史及献血史;否认药物及食
物过敏史;无预防接种史
流行病学史:无
体格检查:体温36.5℃,脉搏78次/分,呼吸20次/分,
血压120/80mmHg,双肺呼吸音粗,可闻及哮鸣音,心率78
次/分,律齐,未闻及病理性杂音。
辅助检查:肺功能四项+支气管舒张实验:沙丁胺醇气雾剂支气管舒
张实验呈阳性,FEV1.0改善17.1%。
初步诊断:门诊诊断:1.支气管哮喘。
-1-
渑池县人民医院
门诊病历
姓名：
门诊号：
处理意见：1.注意避免受凉，避免接触刺激性气味，避免接触花粉等
诱发急性发作；2.如有不适，及时就诊。
经治医师：
Ehun
- 2 -
---
JAEGER PCMED
渑池县人民医院
肺功能检查报告
舒张试验
姓名：
住院号：
性别：女
身高：154 cm
标准体重：125 %
吸烟史：
科别：
测试号：2025052701
年龄：29 Years
体重：67.5 kg
体表面积：1.66 m
Flow [L/s]
F/V ex
Vol%VCmax
Vol [L]
VCmax
Time [s]
F/V in
测试日期
测试时间
预计值
前次
前/预
后次
后/预
改善率
25/5/27
25/5/27
10:10:05
10:32:25
VC MAX
[L]
3.20
2.87
89.6
3.38
105.6
17.9
FVC
[L]
3.18
2.79
87.6
3.37
106.0
20.9
FEV 1
[L]
2.76
1.57
57.0
1.84
66.7
17.1
FEV 1 % FVC
[%]
84.23
56.40
67.0
54.61
64.8
-3.2
FEV 1 % VC MAX
[%]
83.59
54.79
65.5
54.42
65.1
-0.7
PEF
[L/s]
6.49
3.62
55.8
4.32
66.5
19.2
MEF 75
[L/s]
5.83
2.32
39.8
2.52
43.2
8.5
MEF 50
[L/s]
4.21
0.76
18.0
0.91
21.6
20.5
MEF 25
[L/s]
2.00
0.23
11.6
0.24
12.0
3.0
MMEF 75/25
[L/s]
3.86
0.58
14.9
0.67
17.3
16.2
JAEGER PCMED
渑池县人民医院
肺功能检查报告
综合测试
姓名：
性别：女
年龄：29 Years
身高：154 cm
体重：67.5 kg
备注：
联系电话：
住院号：0
测试号：2025052701
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
3.20
2.87
89.6
FVC
[L]
3.18
2.79
87.6
MV
[L/min]
9.64
25.12
260.5
FEV 1
[L]
2.76
1.57
57.0
FEV 1 % FVC
[%]
84.23
56.40
67.0
PEF
[L/s]
6.49
3.62
55.8
MEF 75
[L/s]
5.83
2.32
39.8
MEF 50
[L/s]
4.21
0.76
18.0
MEF 25
[L/s]
2.00
0.23
11.6
MMEF 75/25
[L/s]
3.86
0.58
14.9
MVV
[L/min]
105.09
71.84
68.4
TLC-SB
[L]
4.37
4.10
93.8
RV-SB
[L]
1.25
1.38
110.4
RV%TLC-SB
[%]
28.82
33.70
116.9
FRC-SB
[L]
2.48
2.31
93.1
FRC%TLC-SB
[%]
49.74
56.25
113.1
DLCO SB [mmol/min/kPa]
8.44
6.84
81.0
DLCO/VAmmol/min/kPa/L]
1.93
1.73
89.7
Hb
[g/100ml]
13.40
VA
[L]
4.22
3.95
93.6
DLCOc SB[mmol/min/kPa]
8.44
6.84
81.0
DLCOc/VAmmol/min/kPa/L]
1.93
1.73
89.7
VIN
[L]
3.20
2.72
85.0
Insp. time
[s]
0.95
Exp. time
[s]
1.95
Sample vol
[L]
System dead space [ml]
172.00
Anatom. dead space[ml]
148.50
TA
[s]
11.32
测试结果：
Vol [L]
Time [min]
PredAdj.0
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
5
10
F/V in
Vol [L]
100
50
0
Time [s]
10
15
Volume [L]
4
2
0
4
10
20
30
40
Time [s]
25/5/27
10:10:05上
FRCP th
RV
Vol [L]
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
10
JAEGER PCMED
渑池县人民医院
肺功能检查报告
常规通气
姓名：
住院号：0
性别：女
身高：154 cm
标准体重：125 %
吸烟史：
科别：
测试号：2025052701
年龄：29 Years
体重：67.5 kg
体表面积：1.66 m
测试日期 25/5/27
测试时间 10:10:05
预计值 实测值 实测/预
VC MAX [L] 3.20 2.87 89.6
IRV [L] 1.14
ERV [L] 1.23 0.92 75.3
IC [L] 1.97 1.94 98.4
VT [L] 0.48 0.80 166.0
MV [L/min] 9.64 25.12 260.5
VC IN [L] 3.20 2.87 89.6
VC EX [L] 3.20 2.82 88.0
BF [1/min] 20.00 31.39 157.0
FVC [L] 3.18 2.79 87.6
PEF [L/s] 6.49 3.62 55.8
FEV 0.5 [L] 1.15
FEV 1 [L] 2.76 1.57 57.0
FEV 2 [L] 1.98
FEV 3 [L] 2.21
FEV6 [L] 2.61
FEF 200-1200 [L/s] 2.06
FEV 1 % FVC [%] 84.23 56.40 67.0
FEV 1 % VC MAX [%] 83.59 54.79 65.5
MEF 75 [L/s] 5.83 2.32 39.8
MEF 50 [L/s] 4.21 0.76 18.0
MEF 25 [L/s] 2.00 0.23 11.6
MMEF 75/25 [L/s] 3.86 0.58 14.9
FEF 75/85 [L/s] 1.22 0.16 13.3
FEF50 % FIF50 [%] 19.86
PIF [L/s] 4.32
FVC IN [L] 3.20 2.72 84.9
FET [s] 8.39
FIF 50 [L/s] 3.80
FIV1 [L] 2.68
FIV1 % FVC [%] 98.67
T IN [s] 0.84
T EX [s] 1.07
T TOT [s] 1.91
MIF [L/s] 0.95
MEF [L/s] 0.75
MVV [L/min] 105.09 71.84 68.4
FEF50 % FIF50 [%] 19.86
V backextrapolation ex [L] 0.04
V backextrapol. % FVC [%] 1.50
测试结果
1、中重度阻塞性肺通气功能障碍，小气道功能降低。
2、肺弥散功能正常。
3、残气量、残气量/肺总量正常。
4、沙丁胺醇气雾剂支气管舒张试验呈阳性，FEV1.0改善17.1%。
5、建议定期复查。
报告医师：李朝红/王晓红 报告日期：2025.5.27
6 Vol [L]
TLC 4
FRCPth
RV
PredAdt.0 0.2 0.4 0.6 0.8 1.0
Time [min]
Flow [L/s]
F/V ex
10
5
0
2
4
6
10
5
10
F/V in
Vol%VCmax
0
20
40
60
80
100
Vol [L]
2
VCmax
4
6
8
Time [s]
4
Vol [L]
2
0
2
4
6
8
10
12
14
Time [s]
2026-08-10 12:59:49,690 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 12:59:49,690 INFO     29 [Trace] task=7ac5bf0e | doc=FXJI 三门峡.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}", "name": "FXJI 三门峡.pdf", "embedding_token_consumption": 12278}
2026-08-10 12:59:49,690 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 12:59:49,804 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 12:59:49,804 INFO     29 [Trace] task=7ac5bf0e | doc=FXJI 三门峡.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":2,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 12:59:49,811 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:59:49,813 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 12:59:49,817 INFO     29 set_progress(7ac5bf0e94ba11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 12:59:49 [DOC Engine]:
Start to index...
2026-08-10 12:59:49,845 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.016s]
2026-08-10 12:59:49,848 INFO     29 set_progress(7ac5bf0e94ba11f1bd9827cf206dfa2d), progress: 0.8500000000000001, progress_msg: 
2026-08-10 12:59:49,855 INFO     29 set_progress(7ac5bf0e94ba11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 12:59:49 Indexing done (0.04s). Task done (366.04s)
2026-08-10 12:59:49,859 INFO     29 [Done], chunks(2), token(12278), elapsed:366.04
2026-08-10 12:59:50,268 INFO     29 handle_task done for task {"id": "7ac5bf0e94ba11f1bd9827cf206dfa2d", "doc_id": "7a7d42ec94ba11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "FXJI \u4e09\u95e8\u5ce1.pdf", "type": "pdf", "location": "FXJI \u4e09\u95e8\u5ce1.pdf", "size": 8000159, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786366406983, "task_type": "dataflow", "root_trace_id": "bc9b9d974a834eb18f6171d96f843bf1", "root_traceparent": "00-bc9b9d974a834eb18f6171d96f843bf1-0c5099cebc4db2c7-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
