# 基准结果：GWHU-48岁-男(2).pdf

## 基本信息

- 文件：`GWHU-48岁-男(2).pdf`
- 大小：1154.7 KB
- PDF 总页数：2
- doc_id：`40948096948211f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T14:10:56  完成时间：2026-08-10T14:15:16  耗时：259.4s
- progress_msg：`06:14:44 Indexing done (0.08s). Task done (205.53s)`
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
  - `[no_text_noise] 2026-08-10 06:14:43,445 INFO     29 [ChunkMerger] Merged 2 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 06:11:18,366 INFO     29 handle_task begin for task {"id": "4115cdf4948211f1bd9827cf206dfa2d", "doc_id": "40948096948211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "GWHU-48\u5c81-\u7537(2).pdf", "type": "pdf", "location": "GWHU-48\u5c81-\u7537(2).pdf", "size": 1182408, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786342258386, "task_type": "dataflow", "root_trace_id": "0d4f1377f2e04befb139f86a697fd302", "root_traceparent": "00-0d4f1377f2e04befb139f86a697fd302-ea5641fe487f4324-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 06:11:18,632 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 06:11:18,759 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 06:11:19,286 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:11:19,286 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 06:11:19,286 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 06:11:19,292 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 06:11:19,292 INFO     29 ============================================================
2026-08-10 06:11:19,293 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 06:11:19,293 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 06:11:19,293 INFO     29 ============================================================
2026-08-10 06:11:19,293 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 06:11:19,293 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 06:11:19,295 INFO     29 No torch found.
2026-08-10 06:11:19,712 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=2
2026-08-10 06:11:19,851 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=990933, prompt_len=764
2026-08-10 06:11:21,373 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 06:11:21,374 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 06:11:21,384 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=990933, prompt_len=401
2026-08-10 06:11:21,821 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T06:11:21.820+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 1, "failed": 0, "current": {"801b5176947e11f182aec5d26bc6c4ae": {"id": "801b5176947e11f182aec5d26bc6c4ae", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786340646131, "task_type": "dataflow", "root_trace_id": "97b84aa3d1154f6db808c154432c5554", "root_traceparent": "00-97b84aa3d1154f6db808c154432c5554-dd9503e7c4e14a5d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "4115cdf4948211f1bd9827cf206dfa2d": {"id": "4115cdf4948211f1bd9827cf206dfa2d", "doc_id": "40948096948211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "GWHU-48\u5c81-\u7537(2).pdf", "type": "pdf", "location": "GWHU-48\u5c81-\u7537(2).pdf", "size": 1182408, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786342258386, "task_type": "dataflow", "root_trace_id": "0d4f1377f2e04befb139f86a697fd302", "root_traceparent": "00-0d4f1377f2e04befb139f86a697fd302-ea5641fe487f4324-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 06:11:24,048 INFO     29 [qwen-vl-parser] text API response (len=391):
["初诊病历", "姓名：", "病历号：00125638", "科别：呼吸与危重症医学二科", "门诊", "性别：男", "身份证号：", "出生日期：1975-12-14", "年龄：49岁", "就诊序号：113598", "就诊日期：2025-05-24 10:38", "民族：民族", "联系电话：", "医保费别：自费", "详细地址：地址", "主诉：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。", "现病史：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。", "既往史：无", "过敏史：{否认食物、药物过敏史}。", "体格检查：{体温、脉搏、呼吸、血压未查}。", "辅助检查：无", "初步诊断：1、支气管哮喘", "处理意见：对症", "接诊医生：李志军", "签名时间：2025年05月24日10时38分"]
2026-08-10 06:11:24,048 INFO     29 [qwen-vl-parser] page=1 text: 25 lines (bbox 0-24)
2026-08-10 06:11:24,048 INFO     29 [qwen-vl-parser] page=1 text: 25 sections
2026-08-10 06:11:24,197 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1063452, prompt_len=764
2026-08-10 06:11:25,725 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2024-07-22"
}
```
2026-08-10 06:11:25,726 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=2024-07-22
2026-08-10 06:11:25,750 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1063452, prompt_len=401
2026-08-10 06:11:35,662 INFO     29 [qwen-vl-parser] text API response (len=2139):
["鹤煤总医院肺功能报告单", "ID号：4000", "姓名：", "性别：男", "年龄：48", "身高：170 cm", "体重：95 kg", "B.S.A：2.06m²", "温度(℃)：22", "湿度(%)：50", "气压(mmHg)：1013.3", "科室：", "病区：", "预测公式：亚洲", "医生：李志军", "备注：", "SVC", "实测", "预测", "%预测", "BD后", "改进率", "VC", "L", "2.94", "3.78", "77.8", "", "", "IC", "L", "", "", "", "", "", "TV", "L", "", "", "", "", "", "ERV", "L", "", "", "", "", "", "IRV", "L", "", "", "", "", "", "FVC", "实测", "预测", "%预测", "BD后", "改进率", "FVC", "L", "2.94", "3.78", "77.8", "3.01", "2.4", "FEV0.5", "L", "1.26", "", "", "1.62", "28.6", "FEV1.0", "L", "1.88", "3.26", "57.7", "2.21", "17.6", "FEV3.0", "L", "2.74", "", "", "2.91", "6.2", "FEV1.0%(G)", "%", "63.95", "73.89", "86.5", "73.42", "14.8", "FEV1.0%(T)", "%", "63.95", "", "", "", "", "FEV1/VCpr", "%", "49.7", "", "", "58.5", "17.7", "MMF", "L/s", "1.17", "4.16", "28.1", "1.69", "44.4", "PEF", "L/s", "5.36", "8.7", "61.6", "4.37", "-18.5", "FEF25", "L/s", "2.3", "7.82", "29.4", "3.84", "67", "FEF50", "L/s", "1.45", "5.31", "27.3", "2.11", "45.5", "FEF75", "L/s", "0.61", "2.39", "25.5", "0.7", "14.8", "FEF90", "L/s", "0.23", "", "", "0.31", "34.8", "FEF50/FEF75", "", "2.38", "", "", "3.01", "26.5", "PEF/HT", "L/s/m", "3.15", "", "", "2.57", "-18.4", "FEF25/HT", "L/s/m", "1.35", "", "", "2.26", "67.4", "FEF75-85", "L/s", "0.47", "", "", "0.53", "12.8", "FEF0.2-1.2", "L/s", "2.37", "", "", "3.61", "52.3", "OI", "L/s", "5.21", "", "", "2.19", "-58", "ATI", "%", "", "", "", "", "", "PEFTIME", "Sec", "0.05", "", "", "0.08", "60", "FET", "Sec", "4.46", "", "", "3.72", "-16.6", "Vextrap", "L", "0.05", "", "", "0.09", "80", "Extrap V", "%", "1.7", "", "", "2.99", "75.9", "FIVC", "L", "2.93", "", "", "3.42", "16.7", "MVV", "实测", "预测", "%预测", "BD后", "改进率", "MVV", "L/min", "", "126.6", "", "", "", "RR", "C/min", "", "", "", "", "", "TV", "L", "", "", "", "", "", "MVV/BSA", "L/min/m²", "", "", "", "", "", "AVI", "", "", "", "", "", "", "诊断报告：", "检查技师：", "检查日期：2024-7-22", "FEV1% Restictive Normal", "SVC", "70", "Mixed", "Obstructive", "60", "%VC", "3", "0", "30", "50", "90 SEC", "12", "FVC", "8", "4", "0", "8 L", "-4", "-8", "-12", "4L", "MVV", "2", "0", "5", "10", "15 SEC", ""]
2026-08-10 06:11:35,662 INFO     29 [qwen-vl-parser] page=2 text: 223 lines (bbox 25-247)
2026-08-10 06:11:35,662 INFO     29 [qwen-vl-parser] page=2 text: 223 sections
2026-08-10 06:11:35,662 INFO     29 [qwen-vl-parser] parse_pdf done: 248 sections from 2 pages.
2026-08-10 06:11:35,670 INFO     29 Close text detector.
2026-08-10 06:11:36,180 INFO     29 Close text recognizer.
2026-08-10 06:11:36,584 INFO     29 Close recognizer.
2026-08-10 06:11:36,974 INFO     29 Close recognizer.
2026-08-10 06:11:37,427 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 06:11:37,427 INFO     29 [Trace] task=4115cdf4 | doc=GWHU-48岁-男(2).pdf | Parser:MedLink | outputs={"html": "", "json": "248 items", "markdown": "", "text": "", "name": "GWHU-48岁-男(2).pdf", "output_format": "json"}
2026-08-10 06:11:37,427 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 06:11:37,469 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:11:37,469 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 初诊病历\n[BBOX-1] 姓名：\n[BBOX-2] 病历号：00125638\n[BBOX-3] 科别：呼吸与危重症医学二科\n[BBOX-4] 门诊\n[BBOX-5] 性别：男\n[BBOX-6] 身份证号：\n[BBOX-7] 出生日期：1975-12-14\n[BBOX-8] 年龄：49岁\n[BBOX-9] 就诊序号：113598\n[BBOX-10] 就诊日期：2025-05-24 10:38\n[BBOX-11] 民族：民族\n[BBOX-12] 联系电话：\n[BBOX-13] 医保费别：自费\n[BBOX-14] 详细地址：地址\n[BBOX-15] 主诉：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。\n[BBOX-16] 现病史：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。\n[BBOX-17] 既往史：无\n[BBOX-18] 过敏史：{否认食物、药物过敏史}。\n[BBOX-19] 体格检查：{体温、脉搏、呼吸、血压未查}。\n[BBOX-20] 辅助检查：无\n[BBOX-21] 初步诊断：1、支气管哮喘\n[BBOX-22] 处理意见：对症\n[BBOX-23] 接诊医生：李志军\n[BBOX-24] 签名时间：2025年05月24日10时38分\n[BBOX-25] 鹤煤总医院肺功能报告单\n[BBOX-26] ID号：4000\n[BBOX-27] 姓名：\n[BBOX-28] 性别：男\n[BBOX-29] 年龄：48\n[BBOX-30] 身高：170 cm\n[BBOX-31] 体重：95 kg\n[BBOX-32] B.S.A：2.06m²\n[BBOX-33] 温度(℃)：22\n[BBOX-34] 湿度(%)：50\n[BBOX-35] 气压(mmHg)：1013.3\n[BBOX-36] 科室：\n[BBOX-37] 病区：\n[BBOX-38] 预测公式：亚洲\n[BBOX-39] 医生：李志军\n[BBOX-40] 备注：\n[BBOX-41] SVC\n[BBOX-42] 实测\n[BBOX-43] 预测\n[BBOX-44] %预测\n[BBOX-45] BD后\n[BBOX-46] 改进率\n[BBOX-47] VC\n[BBOX-48] L\n[BBOX-49] 2.94\n[BBOX-50] 3.78\n[BBOX-51] 77.8\n[BBOX-52] IC\n[BBOX-53] L\n[BBOX-54] TV\n[BBOX-55] L\n[BBOX-56] ERV\n[BBOX-57] L\n[BBOX-58] IRV\n[BBOX-59] L\n[BBOX-60] FVC\n[BBOX-61] 实测\n[BBOX-62] 预测\n[BBOX-63] %预测\n[BBOX-64] BD后\n[BBOX-65] 改进率\n[BBOX-66] FVC\n[BBOX-67] L\n[BBOX-68] 2.94\n[BBOX-69] 3.78\n[BBOX-70] 77.8\n[BBOX-71] 3.01\n[BBOX-72] 2.4\n[BBOX-73] FEV0.5\n[BBOX-74] L\n[BBOX-75] 1.26\n[BBOX-76] 1.62\n[BBOX-77] 28.6\n[BBOX-78] FEV1.0\n[BBOX-79] L\n[BBOX-80] 1.88\n[BBOX-81] 3.26\n[BBOX-82] 57.7\n[BBOX-83] 2.21\n[BBOX-84] 17.6\n[BBOX-85] FEV3.0\n[BBOX-86] L\n[BBOX-87] 2.74\n[BBOX-88] 2.91\n[BBOX-89] 6.2\n[BBOX-90] FEV1.0%(G)\n[BBOX-91] %\n[BBOX-92] 63.95\n[BBOX-93] 73.89\n[BBOX-94] 86.5\n[BBOX-95] 73.42\n[BBOX-96] 14.8\n[BBOX-97] FEV1.0%(T)\n[BBOX-98] %\n[BBOX-99] 63.95\n[BBOX-100] FEV1/VCpr\n[BBOX-101] %\n[BBOX-102] 49.7\n[BBOX-103] 58.5\n[BBOX-104] 17.7\n[BBOX-105] MMF\n[BBOX-106] L/s\n[BBOX-107] 1.17\n[BBOX-108] 4.16\n[BBOX-109] 28.1\n[BBOX-110] 1.69\n[BBOX-111] 44.4\n[BBOX-112] PEF\n[BBOX-113] L/s\n[BBOX-114] 5.36\n[BBOX-115] 8.7\n[BBOX-116] 61.6\n[BBOX-117] 4.37\n[BBOX-118] -18.5\n[BBOX-119] FEF25\n[BBOX-120] L/s\n[BBOX-121] 2.3\n[BBOX-122] 7.82\n[BBOX-123] 29.4\n[BBOX-124] 3.84\n[BBOX-125] 67\n[BBOX-126] FEF50\n[BBOX-127] L/s\n[BBOX-128] 1.45\n[BBOX-129] 5.31\n[BBOX-130] 27.3\n[BBOX-131] 2.11\n[BBOX-132] 45.5\n[BBOX-133] FEF75\n[BBOX-134] L/s\n[BBOX-135] 0.61\n[BBOX-136] 2.39\n[BBOX-137] 25.5\n[BBOX-138] 0.7\n[BBOX-139] 14.8\n[BBOX-140] FEF90\n[BBOX-141] L/s\n[BBOX-142] 0.23\n[BBOX-143] 0.31\n[BBOX-144] 34.8\n[BBOX-145] FEF50/FEF75\n[BBOX-146] 2.38\n[BBOX-147] 3.01\n[BBOX-148] 26.5\n[BBOX-149] PEF/HT\n[BBOX-150] L/s/m\n[BBOX-151] 3.15\n[BBOX-152] 2.57\n[BBOX-153] -18.4\n[BBOX-154] FEF25/HT\n[BBOX-155] L/s/m\n[BBOX-156] 1.35\n[BBOX-157] 2.26\n[BBOX-158] 67.4\n[BBOX-159] FEF75-85\n[BBOX-160] L/s\n[BBOX-161] 0.47\n[BBOX-162] 0.53\n[BBOX-163] 12.8\n[BBOX-164] FEF0.2-1.2\n[BBOX-165] L/s\n[BBOX-166] 2.37\n[BBOX-167] 3.61\n[BBOX-168] 52.3\n[BBOX-169] OI\n[BBOX-170] L/s\n[BBOX-171] 5.21\n[BBOX-172] 2.19\n[BBOX-173] -58\n[BBOX-174] ATI\n[BBOX-175] %\n[BBOX-176] PEFTIME\n[BBOX-177] Sec\n[BBOX-178] 0.05\n[BBOX-179] 0.08\n[BBOX-180] 60\n[BBOX-181] FET\n[BBOX-182] Sec\n[BBOX-183] 4.46\n[BBOX-184] 3.72\n[BBOX-185] -16.6\n[BBOX-186] Vextrap\n[BBOX-187] L\n[BBOX-188] 0.05\n[BBOX-189] 0.09\n[BBOX-190] 80\n[BBOX-191] Extrap V\n[BBOX-192] %\n[BBOX-193] 1.7\n[BBOX-194] 2.99\n[BBOX-195] 75.9\n[BBOX-196] FIVC\n[BBOX-197] L\n[BBOX-198] 2.93\n[BBOX-199] 3.42\n[BBOX-200] 16.7\n[BBOX-201] MVV\n[BBOX-202] 实测\n[BBOX-203] 预测\n[BBOX-204] %预测\n[BBOX-205] BD后\n[BBOX-206] 改进率\n[BBOX-207] MVV\n[BBOX-208] L/min\n[BBOX-209] 126.6\n[BBOX-210] RR\n[BBOX-211] C/min\n[BBOX-212] TV\n[BBOX-213] L\n[BBOX-214] MVV/BSA\n[BBOX-215] L/min/m²\n[BBOX-216] AVI\n[BBOX-217] 诊断报告：\n[BBOX-218] 检查技师：\n[BBOX-219] 检查日期：2024-7-22\n[BBOX-220] FEV1% Restictive Normal\n[BBOX-221] SVC\n[BBOX-222] 70\n[BBOX-223] Mixed\n[BBOX-224] Obstructive\n[BBOX-225] 60\n[BBOX-226] %VC\n[BBOX-227] 3\n[BBOX-228] 0\n[BBOX-229] 30\n[BBOX-230] 50\n[BBOX-231] 90 SEC\n[BBOX-232] 12\n[BBOX-233] FVC\n[BBOX-234] 8\n[BBOX-235] 4\n[BBOX-236] 0\n[BBOX-237] 8 L\n[BBOX-238] -4\n[BBOX-239] -8\n[BBOX-240] -12\n[BBOX-241] 4L\n[BBOX-242] MVV\n[BBOX-243] 2\n[BBOX-244] 0\n[BBOX-245] 5\n[BBOX-246] 10\n[BBOX-247] 15 SEC"
  }
]
2026-08-10 06:11:42,059 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:11:42,089 INFO     29 [SmartSplitter] SmartSplitter done: 2 chunks from 2 LLM segments (all bbox_id). Types: {'OutpatientRecord': 1, 'ExaminationReport': 1}
2026-08-10 06:11:42,105 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 06:11:42,105 INFO     29 [Trace] task=4115cdf4 | doc=GWHU-48岁-男(2).pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "248 items", "markdown": "", "text": "", "name": "GWHU-48岁-男(2).pdf", "output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}"}
2026-08-10 06:11:42,105 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 06:11:42,106 INFO     29 [ChunkRouter] Routed 2 chunks into 2 groups: {'chunks_Clinical': 1, 'chunks_Examination': 1}
2026-08-10 06:11:42,124 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 06:11:42,124 INFO     29 [Trace] task=4115cdf4 | doc=GWHU-48岁-男(2).pdf | ChunkRouter:Router | outputs={"html": "", "json": "248 items", "markdown": "", "text": "", "name": "GWHU-48岁-男(2).pdf", "output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:11:42,124 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 06:11:42,132 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:11:42,132 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:11:43,041 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:11:43,048 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 06:11:43,048 INFO     29 [Trace] task=4115cdf4 | doc=GWHU-48岁-男(2).pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "248 items", "markdown": "", "text": "", "name": "GWHU-48岁-男(2).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:11:43,048 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 06:11:43,058 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:11:43,058 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:11:43,863 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:11:43,877 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 06:11:43,878 INFO     29 [Trace] task=4115cdf4 | doc=GWHU-48岁-男(2).pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "248 items", "markdown": "", "text": "", "name": "GWHU-48岁-男(2).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:11:43,878 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 06:11:43,893 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 06:11:43,894 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:11:43,894 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 06:11:43,894 INFO     29 [qwen-vl-text] positions(25): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 06:11:43,894 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [25]
2026-08-10 06:11:44,064 INFO     29 [qwen-vl-text] page=0, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 06:11:44,065 INFO     29 [qwen-vl-text] LLM extraction start, text_len=315
2026-08-10 06:11:44,065 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:11:44,065 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 24, \"encounter_dates\": [\"2025-05-24\"], \"department\": \"呼吸与危重症医学二科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "初诊病历\n姓名：\n病历号：00125638\n科别：呼吸与危重症医学二科\n门诊\n性别：男\n身份证号：\n出生日期：1975-12-14\n年龄：49岁\n就诊序号：113598\n就诊日期：2025-05-24 10:38\n民族：民族\n联系电话：\n医保费别：自费\n详细地址：地址\n主诉：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。\n现病史：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。\n既往史：无\n过敏史：{否认食物、药物过敏史}。\n体格检查：{体温、脉搏、呼吸、血压未查}。\n辅助检查：无\n初步诊断：1、支气管哮喘\n处理意见：对症\n接诊医生：李志军\n签名时间：2025年05月24日10时38分",
    "role": "user"
  }
]
2026-08-10 06:11:46,255 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:11:46,255 INFO     29 [qwen-vl-text] LLM output (len=227):
{
  "encounter_date": "2025-05-24",
  "chief_complaint": "咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。",
  "present_illness": "咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。",
  "past_history": "无",
  "diagnosis": "1、支气管哮喘",
  "treatment_plan": "对症"
}
2026-08-10 06:11:46,255 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-05-24]
2026-08-10 06:11:46,258 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1124779, prompt_len=1003
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["初诊病历", "姓名：", "病历号：00125638", "科别：呼吸与危重症医学二科", "门诊", "性别：男", "身份证号：", "出生日期：1975-12-14", "年龄：49岁", "就诊序号：113598", "就诊日期：2025-05-24 10:38", "民族：民族", "联系电话：", "医保费别：自费", "详细地址：地址", "主诉：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。", "现病史：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。", "既往史：无", "过敏史：{否认食物、药物过敏史}。", "体格检查：{体温、脉搏、呼吸、血压未查}。", "辅助检查：无", "初步诊断：1、支气管哮喘", "处理意见：对症", "接诊医生：李志军", "签名时间：2025年05月24日10时38分"]

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
2026-08-10 06:11:57,697 INFO     29 [qwen-vl-text] coord API raw response (len=2012):
[
	{"text": "初诊病历", "bbox": [455, 12, 562, 48]},
	{"text": "姓名：", "bbox": [143, 73, 188, 100], "label": "姓名："},
	{"text": "病历号：00125638", "bbox": [326, 74, 479, 100], "label": "病历号：00125638"},
	{"text": "科别：呼吸与危重症医学二科", "bbox": [597, 72, 841, 100], "label": "科别：呼吸与危重症医学二科"},
	{"text": "门诊", "bbox": [589, 113, 636, 139], "label": "门诊"},
	{"text": "性别：男", "bbox": [144, 156, 227, 183], "label": "性别：男"},
	{"text": "身份证号：", "bbox": [328, 156, 407, 183], "label": "身份证号："},
	{"text": "出生日期：1975-12-14", "bbox": [596, 156, 784, 181], "label": "出生日期：1975-12-14"},
	{"text": "年龄：49岁", "bbox": [144, 197, 247, 223], "label": "年龄：49岁"},
	{"text": "就诊序号：113598", "bbox": [328, 197, 480, 223], "label": "就诊序号：113598"},
	{"text": "就诊日期：2025-05-24 10:38", "bbox": [596, 197, 836, 223], "label": "就诊日期：2025-05-24 10:38"},
	{"text": "民族：民族", "bbox": [145, 238, 247, 264], "label": "民族：民族"},
	{"text": "联系电话：", "bbox": [328, 238, 407, 264], "label": "联系电话："},
	{"text": "医保费别：自费", "bbox": [596, 237, 733, 263], "label": "医保费别：自费"},
	{"text": "详细地址：地址", "bbox": [144, 279, 274, 305], "label": "详细地址：地址"},
	{"text": "主诉：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。", "bbox": [138, 321, 815, 348], "label": "主诉：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。"},
	{"text": "现病史：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。", "bbox": [138, 362, 834, 389], "label": "现病史：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。"},
	{"text": "既往史：无", "bbox": [138, 403, 250, 429], "label": "既往史：无"},
	{"text": "过敏史：{否认食物、药物过敏史}。", "bbox": [138, 443, 443, 470], "label": "过敏史：{否认食物、药物过敏史}。"},
	{"text": "体格检查：{体温、脉搏、呼吸、血压未查}。", "bbox": [138, 483, 513, 510], "label": "体格检查：{体温、脉搏、呼吸、血压未查}。"},
	{"text": "辅助检查：无", "bbox": [138, 524, 270, 551], "label": "辅助检查：无"},
	{"text": "初步诊断：1、支气管哮喘", "bbox": [138, 565, 364, 592], "label": "初步诊断：1、支气管哮喘"},
	{"text": "处理意见：对症", "bbox": [138, 606, 285, 633], "label": "处理意见：对症"},
	{"text": "接诊医生：李志军", "bbox": [574, 688, 737, 715], "label": "接诊医生：李志军"},
	{"text": "签名时间：2025年05月24日10时38分", "bbox": [574, 729, 867, 756], "label": "签名时间：2025年05月24日10时38分"}
]
2026-08-10 06:11:57,697 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=11.4s
2026-08-10 06:11:57,698 INFO     29 [qwen-vl-text] coord item[0]: text=初诊病历, bbox=[455, 12, 562, 48]
2026-08-10 06:11:57,698 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[143, 73, 188, 100]
2026-08-10 06:11:57,698 INFO     29 [qwen-vl-text] coord item[2]: text=病历号：00125638, bbox=[326, 74, 479, 100]
2026-08-10 06:11:57,698 INFO     29 [qwen-vl-text] coord item[3]: text=科别：呼吸与危重症医学二科, bbox=[597, 72, 841, 100]
2026-08-10 06:11:57,698 INFO     29 [qwen-vl-text] coord item[4]: text=门诊, bbox=[589, 113, 636, 139]
2026-08-10 06:11:57,698 INFO     29 [qwen-vl-text] coord item[5]: text=性别：男, bbox=[144, 156, 227, 183]
2026-08-10 06:11:57,698 INFO     29 [qwen-vl-text] coord item[6]: text=身份证号：, bbox=[328, 156, 407, 183]
2026-08-10 06:11:57,698 INFO     29 [qwen-vl-text] coord item[7]: text=出生日期：1975-12-14, bbox=[596, 156, 784, 181]
2026-08-10 06:11:57,698 INFO     29 [qwen-vl-text] coord item[8]: text=年龄：49岁, bbox=[144, 197, 247, 223]
2026-08-10 06:11:57,698 INFO     29 [qwen-vl-text] coord item[9]: text=就诊序号：113598, bbox=[328, 197, 480, 223]
2026-08-10 06:11:57,698 INFO     29 [qwen-vl-text] coord item[10]: text=就诊日期：2025-05-24 10:38, bbox=[596, 197, 836, 223]
2026-08-10 06:11:57,698 INFO     29 [qwen-vl-text] coord item[11]: text=民族：民族, bbox=[145, 238, 247, 264]
2026-08-10 06:11:57,698 INFO     29 [qwen-vl-text] coord item[12]: text=联系电话：, bbox=[328, 238, 407, 264]
2026-08-10 06:11:57,698 INFO     29 [qwen-vl-text] coord item[13]: text=医保费别：自费, bbox=[596, 237, 733, 263]
2026-08-10 06:11:57,698 INFO     29 [qwen-vl-text] coord item[14]: text=详细地址：地址, bbox=[144, 279, 274, 305]
2026-08-10 06:11:57,698 INFO     29 [qwen-vl-text] coord item[15]: text=主诉：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。, bbox=[138, 321, 815, 348]
2026-08-10 06:11:57,698 INFO     29 [qwen-vl-text] coord item[16]: text=现病史：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。, bbox=[138, 362, 834, 389]
2026-08-10 06:11:57,698 INFO     29 [qwen-vl-text] coord item[17]: text=既往史：无, bbox=[138, 403, 250, 429]
2026-08-10 06:11:57,698 INFO     29 [qwen-vl-text] coord item[18]: text=过敏史：{否认食物、药物过敏史}。, bbox=[138, 443, 443, 470]
2026-08-10 06:11:57,698 INFO     29 [qwen-vl-text] coord item[19]: text=体格检查：{体温、脉搏、呼吸、血压未查}。, bbox=[138, 483, 513, 510]
2026-08-10 06:11:57,698 INFO     29 [qwen-vl-text] coord item[20]: text=辅助检查：无, bbox=[138, 524, 270, 551]
2026-08-10 06:11:57,699 INFO     29 [qwen-vl-text] coord item[21]: text=初步诊断：1、支气管哮喘, bbox=[138, 565, 364, 592]
2026-08-10 06:11:57,699 INFO     29 [qwen-vl-text] coord item[22]: text=处理意见：对症, bbox=[138, 606, 285, 633]
2026-08-10 06:11:57,699 INFO     29 [qwen-vl-text] coord item[23]: text=接诊医生：李志军, bbox=[574, 688, 737, 715]
2026-08-10 06:11:57,699 INFO     29 [qwen-vl-text] coord item[24]: text=签名时间：2025年05月24日10时38分, bbox=[574, 729, 867, 756]
2026-08-10 06:11:57,699 INFO     29 [qwen-vl-text] page=0 — 25/25 coords, api_time=11.4s
2026-08-10 06:11:57,699 INFO     29 [qwen-vl-text] new_positions (25):
[[0, 383.11, 473.204, 7.14, 28.56], [0, 120.40599999999999, 158.296, 43.434999999999995, 59.5], [0, 274.492, 403.318, 44.03, 59.5], [0, 502.674, 708.122, 42.839999999999996, 59.5], [0, 495.938, 535.512, 67.235, 82.705], [0, 121.24799999999999, 191.134, 92.82, 108.88499999999999], [0, 276.176, 342.69399999999996, 92.82, 108.88499999999999], [0, 501.832, 660.1279999999999, 92.82, 107.695], [0, 121.24799999999999, 207.974, 117.21499999999999, 132.685], [0, 276.176, 404.15999999999997, 117.21499999999999, 132.685], [0, 501.832, 703.9119999999999, 117.21499999999999, 132.685], [0, 122.08999999999999, 207.974, 141.60999999999999, 157.07999999999998], [0, 276.176, 342.69399999999996, 141.60999999999999, 157.07999999999998], [0, 501.832, 617.1859999999999, 141.015, 156.48499999999999], [0, 121.24799999999999, 230.708, 166.005, 181.475], [0, 116.196, 686.23, 190.995, 207.06], [0, 116.196, 702.228, 215.39, 231.45499999999998], [0, 116.196, 210.5, 239.785, 255.255], [0, 116.196, 373.006, 263.585, 279.65], [0, 116.196, 431.94599999999997, 287.385, 303.45], [0, 116.196, 227.34, 311.78, 327.84499999999997], [0, 116.196, 306.488, 336.175, 352.24], [0, 116.196, 239.97, 360.57, 376.635], [0, 483.308, 620.554, 409.35999999999996, 425.42499999999995], [0, 483.308, 730.014, 433.755, 449.82]]
2026-08-10 06:11:57,699 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=13.8s
2026-08-10 06:11:57,716 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 06:11:57,717 INFO     29 [Trace] task=4115cdf4 | doc=GWHU-48岁-男(2).pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "248 items", "markdown": "", "text": "", "name": "GWHU-48岁-男(2).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:11:57,717 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 06:11:57,718 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T06:11:57.718+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 1, "failed": 0, "current": {"801b5176947e11f182aec5d26bc6c4ae": {"id": "801b5176947e11f182aec5d26bc6c4ae", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786340646131, "task_type": "dataflow", "root_trace_id": "97b84aa3d1154f6db808c154432c5554", "root_traceparent": "00-97b84aa3d1154f6db808c154432c5554-dd9503e7c4e14a5d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "4115cdf4948211f1bd9827cf206dfa2d": {"id": "4115cdf4948211f1bd9827cf206dfa2d", "doc_id": "40948096948211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "GWHU-48\u5c81-\u7537(2).pdf", "type": "pdf", "location": "GWHU-48\u5c81-\u7537(2).pdf", "size": 1182408, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786342258386, "task_type": "dataflow", "root_trace_id": "0d4f1377f2e04befb139f86a697fd302", "root_traceparent": "00-0d4f1377f2e04befb139f86a697fd302-ea5641fe487f4324-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 06:11:57,727 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:11:57,727 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:11:57,730 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:11:57,730 INFO     29 [qwen-vl-text] LLM output (len=2795):
{
  "encounter_date": "2020-07-08",
  "dm_name": null,
  "dm_gender": "女",
  "dm_age": 36,
  "dm_ethnicity": "汉族",
  "dm_marital_status": "已婚",
  "dm_occupation": "护士",
  "dm_admission_time": "2020-07-08 08:36",
  "dm_record_time": "2020-07-08 08:36",
  "dm_history_provider": "本人",
  "cc_text": "停经39周，要求住院待产。",
  "cc_main_symptoms": [
    "停经"
  ],
  "cc_duration": "39周",
  "pi_text": "平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日（阳历），预产期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单活胎，发育符合孕周。孕早期无早孕反应，孕早期无腹痛、出立，阴道流液，出血史，无放射线、有害物质接触史。孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正常，孕中期行无创DNA结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正常，未行糖耐量筛查，未查B族链球菌。孕期经过顺利，孕晚期无头痛、头晕、眼花等症状，无皮肤黄染及痰痒。现停经39周，无腹痛，未见红及破水，遂入院要求住院待产，门诊以“足月妊娠、瘢痕子宫”收住院。自孕以来精神好，饮食、睡眠好，大小便正常，体重增加约10KG。",
  "pmh_disease_history": [
    "平素体健",
    "否认有“心脏病、高血压、糖尿病、肾病”等慢性病史",
    "否认有“肝炎、结核”等传染性疾病"
  ],
  "pmh_allergy_history": [
    "无"
  ],
  "pmh_surgery_trauma_history": [
    "2016.08行剖宫产手术",
    "否认余手术及外伤史"
  ],
  "ph_smoking": "无",
  "ph_drinking": "无",
  "oh_menarche_age": 12,
  "oh_menopause_age": null,
  "oh_pregnancies": "G2P1，2016年足月剖宫产1活男婴",
  "fh_text": "父母亲体健,1弟1妹均体健,1子体健,否认家族中有遗传性及传染性疾病史。",
  "fh_hereditary_diseases": [],
  "vs_temperature_c": 36.5,
  "vs_pulse_bpm": 78,
  "vs_respiration_rpm": 18,
  "vs_systolic_bp_mmhg": 98,
  "vs_diastolic_bp_mmhg": 64,
  "pe_general_condition": "发育正常;营养中等;自动体位:面色红润;面容及表情自如;神志清晰;言语状态流利;检查时能合作等。",
  "pe_skin_mucosa": "色泽正常,弹性正常,无水肿、出汗、紫癜、皮疹、色素沉着、蜘蛛痣、瘢痕、创伤、溃疡、结节。",
  "pe_lymph_nodes": "全身或局部表浅淋巴结未触及肿大;局部皮肤无红热、瘘管、瘢痕。",
  "pe_lungs": "视诊:腹式呼吸,呼吸节律正常,呼吸深度正常,两侧呼吸运动对称。触诊:语音震颤两侧相等,无摩擦感。叩诊:叩诊声响清音,肺下界肩胛线在第10肋间,呼吸移动度6cm。听诊:呼吸音性质为肺泡呼吸音,强度正常,语音传导正常,无摩擦音、哮鸣音、干啰音、湿啰音。",
  "pe_heart": "视诊：心尖搏动的位置在左侧锁骨中线内第4肋间，范围为2.5cm，强度正常，心前区无异常搏动、局限性膨隆。触诊：心尖搏动最强部位在左侧锁骨中线第4肋间，范围为2.5cm，无抬举性搏动、震颤、摩擦感。叩诊：左右心界线以每肋间距胸骨中线的cm数记载。听诊：心率78次/分，心律整齐，无心脏杂音，无第三心音、第四心音、心音分裂，P2<A2。",
  "pe_abdomen": "视诊：腹部膨隆，晓孕腹型，腹壁对称，无凹陷、膨隆、静脉曲张、蠕动波、局限性隆起，下腹可见一长约15cm横行手术疤痕。触诊：腹壁柔软，无压痛，无反跳痛；未触及肿块，无搏动、波动感等。肝脏：肋缘下未触及，无压痛。胆囊：未触及，无压痛。脾脏：肋缘下未触及。肾：未触及，无压痛等。叩诊：肝上界位于第5肋间，肝浊音界正常，肝区无叩击痛、脾区无叩击痛、腹部无过度鼓音，移动性浊音阴性。听诊：肠蠕动音正常，频率4次/分，胃区无振水声，肝区无摩擦音、脾区无摩擦音，无血管杂音。",
  "pe_extremities": "无畸形、杵状指（趾）、静脉曲张、外伤、骨折；肌肉张力正常与肌力5级，无萎缩;关节无红肿、畸形、运动障碍,双下肢水肿。",
  "pe_nervous_system": "膝腱反射正常、跟腱反射正常、肱二头肌腱反射正常、肱三头肌腱反射正常、腹壁反射正常、巴彬斯基征阴性、克尼格征阴性等。",
  "pe_specialist_exam": "宫高34CM,腹围102CM,估计胎儿体重:3200g,胎位:头位,胎心152次/分,律齐,无宫缩,未见红,未破水,骨盆外测量及内诊:未做。",
  "pe_ecog_score": null,
  "pat_text": "B超(2020.07.02 本院):晓孕宫内单活胎头位(双顶径9.4cm,股骨长7.0cm羊水指数8.5cm),胎盘成熟度II°。",
  "pat_items": [
    "B超(2020.07.02 本院):晓孕宫内单活胎头位(双顶径9.4cm,股骨长7.0cm羊水指数8.5cm),胎盘成熟度II°"
  ],
  "preliminary_diagnoses": [
    {
      "name": "妊娠合并子宫瘢痕",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "孕2产1，宫内孕39周头位待产",
      "diagnosis_type": "西医",
      "is_primary": true
    }
  ],
  "department": "产科二区"
}
2026-08-10 06:11:57,730 INFO     29 [qwen-vl-text] Updated encounter_dates=[2020-07-08]
2026-08-10 06:11:57,732 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1324264, prompt_len=1697
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共49行）
["院", "入院记录", "姓名：", "科室：产科二区", "床号：", "科室：产科二区", "第(1)次入院记录", "过敏史：无", "姓名：", "性别：女", "年龄：36岁", "身份证号", "职业：", "婚姻：已婚", "民族：汉族", "出生地：", "现住址：", "入院日期：2020-07-08 08:36:09", "邮编", "病史采集时间：2020-07-08 08:36:09", "联系人：", "与病人关系：夫妻", "病史叙述者：本人", "联系人地址：同上地址", "电话.", "可靠程度：可靠", "主诉：停经39周，要求住院待产。", "现病史：平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日（阳历），预产", "期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单活胎，发育符合", "孕周。孕早期无早孕反应，孕早期无腹痛、出立，阴道流液，出血史，无放射线、有害物质接", "触史。孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正常，孕中期行无创DNA", "结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正常，未行糖耐量筛", "查，未查B族链球菌。孕期经过顺利，孕晚期无头痛、头晕、眼花等症状，无皮肤黄染及痰", "痒。现停经39周，无腹痛，未见红及破水，遂入院要求住院待产，门诊以“足月妊娠、瘢痕子", "宫”收住院。自孕以来精神好，饮食、睡眠好，大小便正常，体重增加约10KG。", "既往史：患者平素体健；否认有“心脏病、高血压、糖尿病、肾病”等慢性病史，否认有", "“肝炎、结核”等传染性疾病。于2016.08行剖宫产手术，否认余手术及外伤史。否认有输血", "史，有献血史，否认食物及药物过敏史。预防接种随社会进行。", "个人史：出生于原籍，护士，本科文化，工作于三门峡市中心医院。否认长期外地居住", "史，无疫区居住史，无烟酒等不良嗜好。生长环境一般，否认有冶游史。", "婚育史：31岁结婚，爱人", "现年37岁，职员，工作于三门峡市党校，身体健康，无吸", "烟史，有饮酒史，否认“肝炎、结核”病史，夫妻感情好。孕;产;，2016年足月剖宫产1活男", "婴，现体健，否认产后出血及产褥感染史，否认不良孕产史。", "月经史：平素月经规律，12岁，5-7天/30-35天，末次月经为：2019年10月08日（阳", "历），量中等，色暗红，偶有血块，无痛经。", "页", "书写者签名：", "总第 页"]

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
2026-08-10 06:12:17,701 INFO     29 [qwen-vl-text] coord API raw response (len=3093):
[
	{"text": "院", "bbox": [587, 57, 619, 77]},
	{"text": "入院记录", "bbox": [445, 93, 580, 111]},
	{"text": "姓名：", "bbox": [139, 120, 216, 136]},
	{"text": "科室：产科二区", "bbox": [320, 120, 452, 136]},
	{"text": "床号：", "bbox": [519, 120, 562, 136]},
	{"text": "科室：产科二区", "bbox": [139, 144, 270, 159]},
	{"text": "第(1)次入院记录", "bbox": [389, 144, 529, 159]},
	{"text": "过敏史：无", "bbox": [597, 144, 693, 159]},
	{"text": "姓名：", "bbox": [139, 170, 184, 185]},
	{"text": "性别：女", "bbox": [315, 170, 391, 185]},
	{"text": "年龄：36岁", "bbox": [446, 170, 538, 185]},
	{"text": "身份证号", "bbox": [585, 170, 656, 185]},
	{"text": "职业：", "bbox": [139, 195, 184, 210]},
	{"text": "婚姻：已婚", "bbox": [315, 195, 410, 210]},
	{"text": "民族：汉族", "bbox": [446, 195, 540, 210]},
	{"text": "出生地：", "bbox": [585, 195, 647, 210]},
	{"text": "现住址：", "bbox": [139, 222, 231, 238]},
	{"text": "入院日期：2020-07-08 08:36:09", "bbox": [550, 222, 818, 238]},
	{"text": "邮编", "bbox": [139, 248, 177, 264]},
	{"text": "病史采集时间：2020-07-08 08:36:09", "bbox": [541, 248, 846, 264]},
	{"text": "联系人：", "bbox": [139, 274, 202, 290]},
	{"text": "与病人关系：夫妻", "bbox": [445, 274, 592, 290]},
	{"text": "病史叙述者：本人", "bbox": [667, 274, 814, 290]},
	{"text": "联系人地址：同上地址", "bbox": [139, 301, 328, 317]},
	{"text": "电话.", "bbox": [445, 301, 489, 317]},
	{"text": "可靠程度：可靠", "bbox": [667, 301, 796, 317]},
	{"text": "主诉：停经39周，要求住院待产。", "bbox": [168, 347, 440, 363]},
	{"text": "现病史：平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日（阳历），预产", "bbox": [131, 372, 891, 389]},
	{"text": "期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单活胎，发育符合", "bbox": [131, 398, 891, 415]},
	{"text": "孕周。孕早期无早孕反应，孕早期无腹痛、出立，阴道流液，出血史，无放射线、有害物质接", "bbox": [131, 424, 891, 441]},
	{"text": "触史。孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正常，孕中期行无创DNA", "bbox": [131, 450, 891, 467]},
	{"text": "结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正常，未行糖耐量筛", "bbox": [131, 477, 891, 493]},
	{"text": "查，未查B族链球菌。孕期经过顺利，孕晚期无头痛、头晕、眼花等症状，无皮肤黄染及痰", "bbox": [131, 503, 891, 520]},
	{"text": "痒。现停经39周，无腹痛，未见红及破水，遂入院要求住院待产，门诊以“足月妊娠、瘢痕子", "bbox": [131, 529, 891, 546]},
	{"text": "宫”收住院。自孕以来精神好，饮食、睡眠好，大小便正常，体重增加约10KG。", "bbox": [131, 555, 770, 572]},
	{"text": "既往史：患者平素体健；否认有“心脏病、高血压、糖尿病、肾病”等慢性病史，否认有", "bbox": [170, 581, 890, 598]},
	{"text": "“肝炎、结核”等传染性疾病。于2016.08行剖宫产手术，否认余手术及外伤史。否认有输血", "bbox": [139, 608, 882, 625]},
	{"text": "史，有献血史，否认食物及药物过敏史。预防接种随社会进行。", "bbox": [131, 634, 643, 651]},
	{"text": "个人史：出生于原籍，护士，本科文化，工作于三门峡市中心医院。否认长期外地居住", "bbox": [172, 661, 893, 677]},
	{"text": "史，无疫区居住史，无烟酒等不良嗜好。生长环境一般，否认有冶游史。", "bbox": [131, 687, 716, 704]},
	{"text": "婚育史：31岁结婚，爱人", "bbox": [169, 714, 378, 730]},
	{"text": "现年37岁，职员，工作于三门峡市党校，身体健康，无吸", "bbox": [431, 714, 893, 730]},
	{"text": "烟史，有饮酒史，否认“肝炎、结核”病史，夫妻感情好。孕;产;，2016年足月剖宫产1活男", "bbox": [131, 740, 876, 757]},
	{"text": "婴，现体健，否认产后出血及产褥感染史，否认不良孕产史。", "bbox": [131, 767, 624, 784]},
	{"text": "月经史：平素月经规律，12岁，5-7天/30-35天，末次月经为：2019年10月08日（阳", "bbox": [179, 793, 894, 810]},
	{"text": "历），量中等，色暗红，偶有血块，无痛经。", "bbox": [131, 820, 496, 837]},
	{"text": "页", "bbox": [491, 887, 538, 901]},
	{"text": "书写者签名：", "bbox": [613, 887, 700, 901]},
	{"text": "总第 页", "bbox": [833, 885, 896, 900]}
]
2026-08-10 06:12:17,701 INFO     29 [qwen-vl-text] coord API: raw_items=49, valid_items=49, elapsed=20.0s
2026-08-10 06:12:17,701 INFO     29 [qwen-vl-text] coord item[0]: text=院, bbox=[587, 57, 619, 77]
2026-08-10 06:12:17,701 INFO     29 [qwen-vl-text] coord item[1]: text=入院记录, bbox=[445, 93, 580, 111]
2026-08-10 06:12:17,701 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[139, 120, 216, 136]
2026-08-10 06:12:17,701 INFO     29 [qwen-vl-text] coord item[3]: text=科室：产科二区, bbox=[320, 120, 452, 136]
2026-08-10 06:12:17,701 INFO     29 [qwen-vl-text] coord item[4]: text=床号：, bbox=[519, 120, 562, 136]
2026-08-10 06:12:17,701 INFO     29 [qwen-vl-text] coord item[5]: text=科室：产科二区, bbox=[139, 144, 270, 159]
2026-08-10 06:12:17,701 INFO     29 [qwen-vl-text] coord item[6]: text=第(1)次入院记录, bbox=[389, 144, 529, 159]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[7]: text=过敏史：无, bbox=[597, 144, 693, 159]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[8]: text=姓名：, bbox=[139, 170, 184, 185]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[9]: text=性别：女, bbox=[315, 170, 391, 185]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[10]: text=年龄：36岁, bbox=[446, 170, 538, 185]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[11]: text=身份证号, bbox=[585, 170, 656, 185]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[12]: text=职业：, bbox=[139, 195, 184, 210]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[13]: text=婚姻：已婚, bbox=[315, 195, 410, 210]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[14]: text=民族：汉族, bbox=[446, 195, 540, 210]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[15]: text=出生地：, bbox=[585, 195, 647, 210]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[16]: text=现住址：, bbox=[139, 222, 231, 238]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[17]: text=入院日期：2020-07-08 08:36:09, bbox=[550, 222, 818, 238]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[18]: text=邮编, bbox=[139, 248, 177, 264]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[19]: text=病史采集时间：2020-07-08 08:36:09, bbox=[541, 248, 846, 264]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[20]: text=联系人：, bbox=[139, 274, 202, 290]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[21]: text=与病人关系：夫妻, bbox=[445, 274, 592, 290]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[22]: text=病史叙述者：本人, bbox=[667, 274, 814, 290]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[23]: text=联系人地址：同上地址, bbox=[139, 301, 328, 317]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[24]: text=电话., bbox=[445, 301, 489, 317]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[25]: text=可靠程度：可靠, bbox=[667, 301, 796, 317]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[26]: text=主诉：停经39周，要求住院待产。, bbox=[168, 347, 440, 363]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[27]: text=现病史：平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日（阳历），预产, bbox=[131, 372, 891, 389]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[28]: text=期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单活胎，发育符合, bbox=[131, 398, 891, 415]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[29]: text=孕周。孕早期无早孕反应，孕早期无腹痛、出立，阴道流液，出血史，无放射线、有害物质接, bbox=[131, 424, 891, 441]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[30]: text=触史。孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正常，孕中期行无创DNA, bbox=[131, 450, 891, 467]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[31]: text=结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正常，未行糖耐量筛, bbox=[131, 477, 891, 493]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[32]: text=查，未查B族链球菌。孕期经过顺利，孕晚期无头痛、头晕、眼花等症状，无皮肤黄染及痰, bbox=[131, 503, 891, 520]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[33]: text=痒。现停经39周，无腹痛，未见红及破水，遂入院要求住院待产，门诊以“足月妊娠、瘢痕子, bbox=[131, 529, 891, 546]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[34]: text=宫”收住院。自孕以来精神好，饮食、睡眠好，大小便正常，体重增加约10KG。, bbox=[131, 555, 770, 572]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[35]: text=既往史：患者平素体健；否认有“心脏病、高血压、糖尿病、肾病”等慢性病史，否认有, bbox=[170, 581, 890, 598]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[36]: text=“肝炎、结核”等传染性疾病。于2016.08行剖宫产手术，否认余手术及外伤史。否认有输血, bbox=[139, 608, 882, 625]
2026-08-10 06:12:17,702 INFO     29 [qwen-vl-text] coord item[37]: text=史，有献血史，否认食物及药物过敏史。预防接种随社会进行。, bbox=[131, 634, 643, 651]
2026-08-10 06:12:17,703 INFO     29 [qwen-vl-text] coord item[38]: text=个人史：出生于原籍，护士，本科文化，工作于三门峡市中心医院。否认长期外地居住, bbox=[172, 661, 893, 677]
2026-08-10 06:12:17,703 INFO     29 [qwen-vl-text] coord item[39]: text=史，无疫区居住史，无烟酒等不良嗜好。生长环境一般，否认有冶游史。, bbox=[131, 687, 716, 704]
2026-08-10 06:12:17,703 INFO     29 [qwen-vl-text] coord item[40]: text=婚育史：31岁结婚，爱人, bbox=[169, 714, 378, 730]
2026-08-10 06:12:17,703 INFO     29 [qwen-vl-text] coord item[41]: text=现年37岁，职员，工作于三门峡市党校，身体健康，无吸, bbox=[431, 714, 893, 730]
2026-08-10 06:12:17,703 INFO     29 [qwen-vl-text] coord item[42]: text=烟史，有饮酒史，否认“肝炎、结核”病史，夫妻感情好。孕;产;，2016年足月剖宫产1活男, bbox=[131, 740, 876, 757]
2026-08-10 06:12:17,703 INFO     29 [qwen-vl-text] coord item[43]: text=婴，现体健，否认产后出血及产褥感染史，否认不良孕产史。, bbox=[131, 767, 624, 784]
2026-08-10 06:12:17,703 INFO     29 [qwen-vl-text] coord item[44]: text=月经史：平素月经规律，12岁，5-7天/30-35天，末次月经为：2019年10月08日（阳, bbox=[179, 793, 894, 810]
2026-08-10 06:12:17,703 INFO     29 [qwen-vl-text] coord item[45]: text=历），量中等，色暗红，偶有血块，无痛经。, bbox=[131, 820, 496, 837]
2026-08-10 06:12:17,703 INFO     29 [qwen-vl-text] coord item[46]: text=页, bbox=[491, 887, 538, 901]
2026-08-10 06:12:17,703 INFO     29 [qwen-vl-text] coord item[47]: text=书写者签名：, bbox=[613, 887, 700, 901]
2026-08-10 06:12:17,703 INFO     29 [qwen-vl-text] coord item[48]: text=总第 页, bbox=[833, 885, 896, 900]
2026-08-10 06:12:17,703 INFO     29 [qwen-vl-text] page=5 — 49/49 coords, api_time=20.0s
2026-08-10 06:12:17,706 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1249766, prompt_len=1544
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共40行）
["院", "入院记录", "姓名:", "科室:产科二区", "床号:", "生.", "家族史:父母亲体健,1弟1妹均体健,1子体健,否认家族中有遗传性及传染性疾病史。", "体格检查", "体温:36.5℃", "脉搏:78次/分", "呼吸:18次/分", "血压:98/64mmHg", "身高160cm", "体重:60Kg", "一般状况:发育正常;营养中等;自动体位:面色红润;面容及表情自如;神志清晰;言", "语状态流利;检查时能合作等。", "皮肤:色泽正常,弹性正常,无水肿、出汗、紫癜、皮疹、色素沉着、蜘蛛痣、瘢痕、创", "伤、溃疡、结节。", "淋巴结:全身或局部表浅淋巴结未触及肿大;局部皮肤无红热、瘘管、瘢痕。", "头部:", "头颅:大小无异常、外形无异常;眉发分布正常;无疖、痈、外伤、瘢痕、肿块。", "眼部:双眼裂正常,双眼睑无水肿,眼球运动正常。瞳孔:左3.0mm直接对光反应灵敏,", "间接对光反应灵敏;右3.0mm直接对光反应灵敏,间接对光反应灵敏。视力粗测正常。", "耳部:耳廓无畸形,外耳道无分泌物,乳突无压痛,听力粗测5米。", "鼻部:无畸形、鼻翼扇动、阻塞、分泌物、鼻中隔异常、嗅觉障碍、鼻窦压痛等。", "口腔:口唇红润,无畸形、疱疹、微血管搏动、口角皲裂;牙齿无缺损、龋病、镶补等异", "常;牙龈无溢血、溢脓、萎缩、色素沉着;口腔粘膜无溃疡、假膜、色素沉着;扁桃体无肿", "大、分泌物;咽部无充血、分泌物。", "颈部:对称,无强直、压痛、运动受限、颈静脉怒张、颈动脉明显搏动、肿块,气管居", "中,甲状腺无肿大。", "胸部", "胸廓:形状正常,对称,运动程度正常,肋间正常,胸壁无水肿、皮下气肿、肿块、静脉", "曲张,肋骨及肋软骨无压痛、凹陷等异常。乳头,正常。", "肺脏:视诊:腹式呼吸,呼吸节律正常,呼吸深度正常,两侧呼吸运动对称。", "触诊:语音震颤两侧相等,无摩擦感。", "叩诊:叩诊声响清音,肺下界肩胛线在第10肋间,呼吸移动度6cm,", "听诊:呼吸音性质为肺泡呼吸音,强度正常,语音传导正常,无摩擦音、哮鸣音、", "第页", "书写者签名:", "总第页"]

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
2026-08-10 06:12:32,923 INFO     29 [qwen-vl-text] coord API raw response (len=2583):
```json
[
	{"text": "院", "bbox": [577, 61, 624, 81]},
	{"text": "入院记录", "bbox": [442, 98, 584, 116]},
	{"text": "姓名:", "bbox": [125, 126, 170, 141]},
	{"text": "科室:产科二区", "bbox": [313, 126, 450, 141]},
	{"text": "床号:", "bbox": [519, 126, 564, 141]},
	{"text": "生.", "bbox": [698, 126, 762, 141]},
	{"text": "家族史:父母亲体健,1弟1妹均体健,1子体健,否认家族中有遗传性及传染性疾病史。", "bbox": [154, 149, 889, 165]},
	{"text": "体格检查", "bbox": [464, 180, 557, 197]},
	{"text": "体温:36.5℃", "bbox": [154, 212, 269, 227]},
	{"text": "脉搏:78次/分", "bbox": [309, 212, 435, 227]},
	{"text": "呼吸:18次/分", "bbox": [480, 212, 606, 227]},
	{"text": "血压:98/64mmHg", "bbox": [667, 212, 812, 228]},
	{"text": "身高160cm", "bbox": [154, 240, 251, 255]},
	{"text": "体重:60Kg", "bbox": [309, 240, 407, 257]},
	{"text": "一般状况:发育正常;营养中等;自动体位:面色红润;面容及表情自如;神志清晰;言", "bbox": [154, 267, 909, 283]},
	{"text": "语状态流利;检查时能合作等。", "bbox": [114, 293, 376, 309]},
	{"text": "皮肤:色泽正常,弹性正常,无水肿、出汗、紫癜、皮疹、色素沉着、蜘蛛痣、瘢痕、创", "bbox": [154, 321, 909, 337]},
	{"text": "伤、溃疡、结节。", "bbox": [114, 348, 259, 364]},
	{"text": "淋巴结:全身或局部表浅淋巴结未触及肿大;局部皮肤无红热、瘘管、瘢痕。", "bbox": [154, 375, 800, 391]},
	{"text": "头部:", "bbox": [154, 403, 198, 418]},
	{"text": "头颅:大小无异常、外形无异常;眉发分布正常;无疖、痈、外伤、瘢痕、肿块。", "bbox": [154, 429, 839, 445]},
	{"text": "眼部:双眼裂正常,双眼睑无水肿,眼球运动正常。瞳孔:左3.0mm直接对光反应灵敏,", "bbox": [154, 456, 897, 472]},
	{"text": "间接对光反应灵敏;右3.0mm直接对光反应灵敏,间接对光反应灵敏。视力粗测正常。", "bbox": [114, 483, 840, 499]},
	{"text": "耳部:耳廓无畸形,外耳道无分泌物,乳突无压痛,听力粗测5米。", "bbox": [154, 510, 713, 526]},
	{"text": "鼻部:无畸形、鼻翼扇动、阻塞、分泌物、鼻中隔异常、嗅觉障碍、鼻窦压痛等。", "bbox": [154, 536, 839, 552]},
	{"text": "口腔:口唇红润,无畸形、疱疹、微血管搏动、口角皲裂;牙齿无缺损、龋病、镶补等异", "bbox": [154, 563, 909, 579]},
	{"text": "常;牙龈无溢血、溢脓、萎缩、色素沉着;口腔粘膜无溃疡、假膜、色素沉着;扁桃体无肿", "bbox": [114, 590, 890, 606]},
	{"text": "大、分泌物;咽部无充血、分泌物。", "bbox": [114, 617, 416, 633]},
	{"text": "颈部:对称,无强直、压痛、运动受限、颈静脉怒张、颈动脉明显搏动、肿块,气管居", "bbox": [154, 644, 890, 660]},
	{"text": "中,甲状腺无肿大。", "bbox": [114, 671, 278, 687]},
	{"text": "胸部", "bbox": [154, 698, 193, 713]},
	{"text": "胸廓:形状正常,对称,运动程度正常,肋间正常,胸壁无水肿、皮下气肿、肿块、静脉", "bbox": [154, 725, 909, 741]},
	{"text": "曲张,肋骨及肋软骨无压痛、凹陷等异常。乳头,正常。", "bbox": [114, 752, 588, 768]},
	{"text": "肺脏:视诊:腹式呼吸,呼吸节律正常,呼吸深度正常,两侧呼吸运动对称。", "bbox": [154, 779, 800, 795]},
	{"text": "触诊:语音震颤两侧相等,无摩擦感。", "bbox": [212, 806, 529, 822]},
	{"text": "叩诊:叩诊声响清音,肺下界肩胛线在第10肋间,呼吸移动度6cm,", "bbox": [212, 833, 772, 849]},
	{"text": "听诊:呼吸音性质为肺泡呼吸音,强度正常,语音传导正常,无摩擦音、哮鸣音、", "bbox": [212, 859, 898, 875]},
	{"text": "第页", "bbox": [487, 906, 536, 920]},
	{"text": "书写者签名:", "bbox": [614, 906, 704, 920]},
	{"text": "总第页", "bbox": [844, 906, 910, 920]}
]
```
2026-08-10 06:12:32,923 INFO     29 [qwen-vl-text] coord API: raw_items=40, valid_items=40, elapsed=15.2s
2026-08-10 06:12:32,923 INFO     29 [qwen-vl-text] coord item[0]: text=院, bbox=[577, 61, 624, 81]
2026-08-10 06:12:32,923 INFO     29 [qwen-vl-text] coord item[1]: text=入院记录, bbox=[442, 98, 584, 116]
2026-08-10 06:12:32,924 INFO     29 [qwen-vl-text] coord item[2]: text=姓名:, bbox=[125, 126, 170, 141]
2026-08-10 06:12:32,924 INFO     29 [qwen-vl-text] coord item[3]: text=科室:产科二区, bbox=[313, 126, 450, 141]
2026-08-10 06:12:32,924 INFO     29 [qwen-vl-text] coord item[4]: text=床号:, bbox=[519, 126, 564, 141]
2026-08-10 06:12:32,924 INFO     29 [qwen-vl-text] coord item[5]: text=生., bbox=[698, 126, 762, 141]
2026-08-10 06:12:32,924 INFO     29 [qwen-vl-text] coord item[6]: text=家族史:父母亲体健,1弟1妹均体健,1子体健,否认家族中有遗传性及传染性疾病史。, bbox=[154, 149, 889, 165]
2026-08-10 06:12:32,924 INFO     29 [qwen-vl-text] coord item[7]: text=体格检查, bbox=[464, 180, 557, 197]
2026-08-10 06:12:32,924 INFO     29 [qwen-vl-text] coord item[8]: text=体温:36.5℃, bbox=[154, 212, 269, 227]
2026-08-10 06:12:32,924 INFO     29 [qwen-vl-text] coord item[9]: text=脉搏:78次/分, bbox=[309, 212, 435, 227]
2026-08-10 06:12:32,924 INFO     29 [qwen-vl-text] coord item[10]: text=呼吸:18次/分, bbox=[480, 212, 606, 227]
2026-08-10 06:12:32,924 INFO     29 [qwen-vl-text] coord item[11]: text=血压:98/64mmHg, bbox=[667, 212, 812, 228]
2026-08-10 06:12:32,924 INFO     29 [qwen-vl-text] coord item[12]: text=身高160cm, bbox=[154, 240, 251, 255]
2026-08-10 06:12:32,925 INFO     29 [qwen-vl-text] coord item[13]: text=体重:60Kg, bbox=[309, 240, 407, 257]
2026-08-10 06:12:32,925 INFO     29 [qwen-vl-text] coord item[14]: text=一般状况:发育正常;营养中等;自动体位:面色红润;面容及表情自如;神志清晰;言, bbox=[154, 267, 909, 283]
2026-08-10 06:12:32,925 INFO     29 [qwen-vl-text] coord item[15]: text=语状态流利;检查时能合作等。, bbox=[114, 293, 376, 309]
2026-08-10 06:12:32,925 INFO     29 [qwen-vl-text] coord item[16]: text=皮肤:色泽正常,弹性正常,无水肿、出汗、紫癜、皮疹、色素沉着、蜘蛛痣、瘢痕、创, bbox=[154, 321, 909, 337]
2026-08-10 06:12:32,925 INFO     29 [qwen-vl-text] coord item[17]: text=伤、溃疡、结节。, bbox=[114, 348, 259, 364]
2026-08-10 06:12:32,925 INFO     29 [qwen-vl-text] coord item[18]: text=淋巴结:全身或局部表浅淋巴结未触及肿大;局部皮肤无红热、瘘管、瘢痕。, bbox=[154, 375, 800, 391]
2026-08-10 06:12:32,925 INFO     29 [qwen-vl-text] coord item[19]: text=头部:, bbox=[154, 403, 198, 418]
2026-08-10 06:12:32,925 INFO     29 [qwen-vl-text] coord item[20]: text=头颅:大小无异常、外形无异常;眉发分布正常;无疖、痈、外伤、瘢痕、肿块。, bbox=[154, 429, 839, 445]
2026-08-10 06:12:32,925 INFO     29 [qwen-vl-text] coord item[21]: text=眼部:双眼裂正常,双眼睑无水肿,眼球运动正常。瞳孔:左3.0mm直接对光反应灵敏,, bbox=[154, 456, 897, 472]
2026-08-10 06:12:32,925 INFO     29 [qwen-vl-text] coord item[22]: text=间接对光反应灵敏;右3.0mm直接对光反应灵敏,间接对光反应灵敏。视力粗测正常。, bbox=[114, 483, 840, 499]
2026-08-10 06:12:32,925 INFO     29 [qwen-vl-text] coord item[23]: text=耳部:耳廓无畸形,外耳道无分泌物,乳突无压痛,听力粗测5米。, bbox=[154, 510, 713, 526]
2026-08-10 06:12:32,925 INFO     29 [qwen-vl-text] coord item[24]: text=鼻部:无畸形、鼻翼扇动、阻塞、分泌物、鼻中隔异常、嗅觉障碍、鼻窦压痛等。, bbox=[154, 536, 839, 552]
2026-08-10 06:12:32,925 INFO     29 [qwen-vl-text] coord item[25]: text=口腔:口唇红润,无畸形、疱疹、微血管搏动、口角皲裂;牙齿无缺损、龋病、镶补等异, bbox=[154, 563, 909, 579]
2026-08-10 06:12:32,926 INFO     29 [qwen-vl-text] coord item[26]: text=常;牙龈无溢血、溢脓、萎缩、色素沉着;口腔粘膜无溃疡、假膜、色素沉着;扁桃体无肿, bbox=[114, 590, 890, 606]
2026-08-10 06:12:32,926 INFO     29 [qwen-vl-text] coord item[27]: text=大、分泌物;咽部无充血、分泌物。, bbox=[114, 617, 416, 633]
2026-08-10 06:12:32,926 INFO     29 [qwen-vl-text] coord item[28]: text=颈部:对称,无强直、压痛、运动受限、颈静脉怒张、颈动脉明显搏动、肿块,气管居, bbox=[154, 644, 890, 660]
2026-08-10 06:12:32,926 INFO     29 [qwen-vl-text] coord item[29]: text=中,甲状腺无肿大。, bbox=[114, 671, 278, 687]
2026-08-10 06:12:32,926 INFO     29 [qwen-vl-text] coord item[30]: text=胸部, bbox=[154, 698, 193, 713]
2026-08-10 06:12:32,926 INFO     29 [qwen-vl-text] coord item[31]: text=胸廓:形状正常,对称,运动程度正常,肋间正常,胸壁无水肿、皮下气肿、肿块、静脉, bbox=[154, 725, 909, 741]
2026-08-10 06:12:32,926 INFO     29 [qwen-vl-text] coord item[32]: text=曲张,肋骨及肋软骨无压痛、凹陷等异常。乳头,正常。, bbox=[114, 752, 588, 768]
2026-08-10 06:12:32,926 INFO     29 [qwen-vl-text] coord item[33]: text=肺脏:视诊:腹式呼吸,呼吸节律正常,呼吸深度正常,两侧呼吸运动对称。, bbox=[154, 779, 800, 795]
2026-08-10 06:12:32,926 INFO     29 [qwen-vl-text] coord item[34]: text=触诊:语音震颤两侧相等,无摩擦感。, bbox=[212, 806, 529, 822]
2026-08-10 06:12:32,926 INFO     29 [qwen-vl-text] coord item[35]: text=叩诊:叩诊声响清音,肺下界肩胛线在第10肋间,呼吸移动度6cm,, bbox=[212, 833, 772, 849]
2026-08-10 06:12:32,926 INFO     29 [qwen-vl-text] coord item[36]: text=听诊:呼吸音性质为肺泡呼吸音,强度正常,语音传导正常,无摩擦音、哮鸣音、, bbox=[212, 859, 898, 875]
2026-08-10 06:12:32,926 INFO     29 [qwen-vl-text] coord item[37]: text=第页, bbox=[487, 906, 536, 920]
2026-08-10 06:12:32,926 INFO     29 [qwen-vl-text] coord item[38]: text=书写者签名:, bbox=[614, 906, 704, 920]
2026-08-10 06:12:32,926 INFO     29 [qwen-vl-text] coord item[39]: text=总第页, bbox=[844, 906, 910, 920]
2026-08-10 06:12:32,927 INFO     29 [qwen-vl-text] page=6 — 40/40 coords, api_time=15.2s
2026-08-10 06:12:32,932 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1167410, prompt_len=1429
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共44行）
["院", "入院记录", "姓名：", "科室：产科二区", "床号", "病号：", "干啰音、湿啰音。", "心脏：视诊：心尖搏动的位置在左侧锁骨中线内第4肋间，范围为2.5cm，强度正常，心前", "区无异常搏动、局限性膨隆。", "触诊：心尖搏动最强部位在左侧锁骨中线第4肋间，范围为2.5cm，无抬举性搏动、", "震颤、摩擦感。", "叩诊：左右心界线以每肋间距胸骨中线的cm数记载。", "右cm", "肋间", "左cm", "2", "Ⅱ", "2.5", "2", "Ⅲ", "4", "3", "Ⅳ", "5.5", "Ⅴ", "8", "左锁骨中线至前正中线的距离9cm。", "听诊：心率78次/分，心律整齐，无心脏杂音，无第三心音、第四心音、心音分", "裂，P2<A2。", "血管：桡动脉搏动正常，血管壁硬度正常。", "周围血管征：无毛细血管搏动征、水冲脉、枪击音、动脉异常搏动。", "腹部：", "视诊：腹部膨隆，晓孕腹型，腹壁对称，无凹陷、膨隆、静脉曲张、蠕动波、局限性隆", "起，下腹可见一长约15cm横行手术疤痕。", "触诊：腹壁柔软，无压痛，无反跳痛；未触及肿块，无搏动、波动感等。肝脏：肋缘下未", "触及，无压痛。胆囊：未触及，无压痛。脾脏：肋缘下未触及。肾：未触及，无压痛等。", "叩诊：肝上界位于第5肋间，肝浊音界正常，肝区无叩击痛、脾区无叩击痛、腹部无过度", "鼓音，移动性浊音阴性。", "听诊：肠蠕动音正常，频率4次/分，胃区无振水声，肝区无摩擦音、脾区无摩擦音，无血", "管杂音。", "外阴及肛门：阴毛分布正常；外生殖器发育正常，肛门检查：无外痔、肛裂、肛瘘、脱", "肛、湿疣等。", "脊柱：脊柱无畸形、压痛、叩击痛；脊柱两侧肌肉无紧张、压痛；肋脊角无压痛、叩痛。", "四肢：无畸形、杵状指（趾）、静脉曲张、外伤、骨折；肌肉张力正常与肌力5级，无萎"]

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
2026-08-10 06:12:48,394 INFO     29 [qwen-vl-text] coord API raw response (len=2621):
[
	{"text": "院", "bbox": [579, 63, 625, 84]},
	{"text": "入院记录", "bbox": [442, 100, 586, 119]},
	{"text": "姓名：", "bbox": [115, 130, 164, 145]},
	{"text": "科室：产科二区", "bbox": [309, 130, 448, 145]},
	{"text": "床号", "bbox": [520, 130, 556, 145]},
	{"text": "病号：", "bbox": [718, 130, 766, 145]},
	{"text": "干啰音、湿啰音。", "bbox": [107, 154, 254, 170]},
	{"text": "心脏：视诊：心尖搏动的位置在左侧锁骨中线内第4肋间，范围为2.5cm，强度正常，心前", "bbox": [147, 180, 916, 196]},
	{"text": "区无异常搏动、局限性膨隆。", "bbox": [107, 208, 353, 224]},
	{"text": "触诊：心尖搏动最强部位在左侧锁骨中线第4肋间，范围为2.5cm，无抬举性搏动、", "bbox": [205, 237, 906, 253]},
	{"text": "震颤、摩擦感。", "bbox": [107, 264, 234, 280]},
	{"text": "叩诊：左右心界线以每肋间距胸骨中线的cm数记载。", "bbox": [205, 291, 648, 307]},
	{"text": "右cm", "bbox": [188, 317, 230, 331]},
	{"text": "肋间", "bbox": [418, 317, 459, 331]},
	{"text": "左cm", "bbox": [653, 317, 695, 331]},
	{"text": "2", "bbox": [202, 337, 214, 350]},
	{"text": "Ⅱ", "bbox": [431, 337, 447, 350]},
	{"text": "2.5", "bbox": [657, 337, 689, 350]},
	{"text": "2", "bbox": [202, 356, 214, 369]},
	{"text": "Ⅲ", "bbox": [429, 356, 451, 369]},
	{"text": "4", "bbox": [667, 356, 678, 369]},
	{"text": "3", "bbox": [202, 374, 214, 387]},
	{"text": "Ⅳ", "bbox": [430, 374, 450, 387]},
	{"text": "5.5", "bbox": [657, 374, 689, 387]},
	{"text": "Ⅴ", "bbox": [431, 392, 447, 405]},
	{"text": "8", "bbox": [667, 392, 678, 405]},
	{"text": "左锁骨中线至前正中线的距离9cm。", "bbox": [156, 414, 451, 429]},
	{"text": "听诊：心率78次/分，心律整齐，无心脏杂音，无第三心音、第四心音、心音分", "bbox": [205, 442, 888, 458]},
	{"text": "裂，P2<A2。", "bbox": [107, 470, 204, 485]},
	{"text": "血管：桡动脉搏动正常，血管壁硬度正常。", "bbox": [147, 497, 509, 513]},
	{"text": "周围血管征：无毛细血管搏动征、水冲脉、枪击音、动脉异常搏动。", "bbox": [147, 525, 726, 541]},
	{"text": "腹部：", "bbox": [147, 552, 193, 568]},
	{"text": "视诊：腹部膨隆，晓孕腹型，腹壁对称，无凹陷、膨隆、静脉曲张、蠕动波、局限性隆", "bbox": [147, 579, 897, 595]},
	{"text": "起，下腹可见一长约15cm横行手术疤痕。", "bbox": [107, 607, 451, 623]},
	{"text": "触诊：腹壁柔软，无压痛，无反跳痛；未触及肿块，无搏动、波动感等。肝脏：肋缘下未", "bbox": [147, 634, 916, 651]},
	{"text": "触及，无压痛。胆囊：未触及，无压痛。脾脏：肋缘下未触及。肾：未触及，无压痛等。", "bbox": [107, 662, 865, 678]},
	{"text": "叩诊：肝上界位于第5肋间，肝浊音界正常，肝区无叩击痛、脾区无叩击痛、腹部无过度", "bbox": [147, 690, 906, 706]},
	{"text": "鼓音，移动性浊音阴性。", "bbox": [107, 717, 312, 733]},
	{"text": "听诊：肠蠕动音正常，频率4次/分，胃区无振水声，肝区无摩擦音、脾区无摩擦音，无血", "bbox": [147, 744, 916, 760]},
	{"text": "管杂音。", "bbox": [107, 772, 174, 788]},
	{"text": "外阴及肛门：阴毛分布正常；外生殖器发育正常，肛门检查：无外痔、肛裂、肛瘘、脱", "bbox": [147, 800, 896, 816]},
	{"text": "肛、湿疣等。", "bbox": [107, 827, 214, 843]},
	{"text": "脊柱：脊柱无畸形、压痛、叩击痛；脊柱两侧肌肉无紧张、压痛；肋脊角无压痛、叩痛。", "bbox": [147, 855, 902, 871]},
	{"text": "四肢：无畸形、杵状指（趾）、静脉曲张、外伤、骨折；肌肉张力正常与肌力5级，无萎", "bbox": [147, 881, 903, 898]}
]
2026-08-10 06:12:48,394 INFO     29 [qwen-vl-text] coord API: raw_items=44, valid_items=44, elapsed=15.5s
2026-08-10 06:12:48,394 INFO     29 [qwen-vl-text] coord item[0]: text=院, bbox=[579, 63, 625, 84]
2026-08-10 06:12:48,394 INFO     29 [qwen-vl-text] coord item[1]: text=入院记录, bbox=[442, 100, 586, 119]
2026-08-10 06:12:48,394 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[115, 130, 164, 145]
2026-08-10 06:12:48,394 INFO     29 [qwen-vl-text] coord item[3]: text=科室：产科二区, bbox=[309, 130, 448, 145]
2026-08-10 06:12:48,394 INFO     29 [qwen-vl-text] coord item[4]: text=床号, bbox=[520, 130, 556, 145]
2026-08-10 06:12:48,394 INFO     29 [qwen-vl-text] coord item[5]: text=病号：, bbox=[718, 130, 766, 145]
2026-08-10 06:12:48,394 INFO     29 [qwen-vl-text] coord item[6]: text=干啰音、湿啰音。, bbox=[107, 154, 254, 170]
2026-08-10 06:12:48,394 INFO     29 [qwen-vl-text] coord item[7]: text=心脏：视诊：心尖搏动的位置在左侧锁骨中线内第4肋间，范围为2.5cm，强度正常，心前, bbox=[147, 180, 916, 196]
2026-08-10 06:12:48,395 INFO     29 [qwen-vl-text] coord item[8]: text=区无异常搏动、局限性膨隆。, bbox=[107, 208, 353, 224]
2026-08-10 06:12:48,395 INFO     29 [qwen-vl-text] coord item[9]: text=触诊：心尖搏动最强部位在左侧锁骨中线第4肋间，范围为2.5cm，无抬举性搏动、, bbox=[205, 237, 906, 253]
2026-08-10 06:12:48,395 INFO     29 [qwen-vl-text] coord item[10]: text=震颤、摩擦感。, bbox=[107, 264, 234, 280]
2026-08-10 06:12:48,395 INFO     29 [qwen-vl-text] coord item[11]: text=叩诊：左右心界线以每肋间距胸骨中线的cm数记载。, bbox=[205, 291, 648, 307]
2026-08-10 06:12:48,395 INFO     29 [qwen-vl-text] coord item[12]: text=右cm, bbox=[188, 317, 230, 331]
2026-08-10 06:12:48,395 INFO     29 [qwen-vl-text] coord item[13]: text=肋间, bbox=[418, 317, 459, 331]
2026-08-10 06:12:48,395 INFO     29 [qwen-vl-text] coord item[14]: text=左cm, bbox=[653, 317, 695, 331]
2026-08-10 06:12:48,395 INFO     29 [qwen-vl-text] coord item[15]: text=2, bbox=[202, 337, 214, 350]
2026-08-10 06:12:48,395 INFO     29 [qwen-vl-text] coord item[16]: text=Ⅱ, bbox=[431, 337, 447, 350]
2026-08-10 06:12:48,395 INFO     29 [qwen-vl-text] coord item[17]: text=2.5, bbox=[657, 337, 689, 350]
2026-08-10 06:12:48,395 INFO     29 [qwen-vl-text] coord item[18]: text=2, bbox=[202, 356, 214, 369]
2026-08-10 06:12:48,395 INFO     29 [qwen-vl-text] coord item[19]: text=Ⅲ, bbox=[429, 356, 451, 369]
2026-08-10 06:12:48,395 INFO     29 [qwen-vl-text] coord item[20]: text=4, bbox=[667, 356, 678, 369]
2026-08-10 06:12:48,395 INFO     29 [qwen-vl-text] coord item[21]: text=3, bbox=[202, 374, 214, 387]
2026-08-10 06:12:48,395 INFO     29 [qwen-vl-text] coord item[22]: text=Ⅳ, bbox=[430, 374, 450, 387]
2026-08-10 06:12:48,395 INFO     29 [qwen-vl-text] coord item[23]: text=5.5, bbox=[657, 374, 689, 387]
2026-08-10 06:12:48,396 INFO     29 [qwen-vl-text] coord item[24]: text=Ⅴ, bbox=[431, 392, 447, 405]
2026-08-10 06:12:48,396 INFO     29 [qwen-vl-text] coord item[25]: text=8, bbox=[667, 392, 678, 405]
2026-08-10 06:12:48,396 INFO     29 [qwen-vl-text] coord item[26]: text=左锁骨中线至前正中线的距离9cm。, bbox=[156, 414, 451, 429]
2026-08-10 06:12:48,396 INFO     29 [qwen-vl-text] coord item[27]: text=听诊：心率78次/分，心律整齐，无心脏杂音，无第三心音、第四心音、心音分, bbox=[205, 442, 888, 458]
2026-08-10 06:12:48,396 INFO     29 [qwen-vl-text] coord item[28]: text=裂，P2<A2。, bbox=[107, 470, 204, 485]
2026-08-10 06:12:48,396 INFO     29 [qwen-vl-text] coord item[29]: text=血管：桡动脉搏动正常，血管壁硬度正常。, bbox=[147, 497, 509, 513]
2026-08-10 06:12:48,396 INFO     29 [qwen-vl-text] coord item[30]: text=周围血管征：无毛细血管搏动征、水冲脉、枪击音、动脉异常搏动。, bbox=[147, 525, 726, 541]
2026-08-10 06:12:48,396 INFO     29 [qwen-vl-text] coord item[31]: text=腹部：, bbox=[147, 552, 193, 568]
2026-08-10 06:12:48,396 INFO     29 [qwen-vl-text] coord item[32]: text=视诊：腹部膨隆，晓孕腹型，腹壁对称，无凹陷、膨隆、静脉曲张、蠕动波、局限性隆, bbox=[147, 579, 897, 595]
2026-08-10 06:12:48,396 INFO     29 [qwen-vl-text] coord item[33]: text=起，下腹可见一长约15cm横行手术疤痕。, bbox=[107, 607, 451, 623]
2026-08-10 06:12:48,396 INFO     29 [qwen-vl-text] coord item[34]: text=触诊：腹壁柔软，无压痛，无反跳痛；未触及肿块，无搏动、波动感等。肝脏：肋缘下未, bbox=[147, 634, 916, 651]
2026-08-10 06:12:48,396 INFO     29 [qwen-vl-text] coord item[35]: text=触及，无压痛。胆囊：未触及，无压痛。脾脏：肋缘下未触及。肾：未触及，无压痛等。, bbox=[107, 662, 865, 678]
2026-08-10 06:12:48,396 INFO     29 [qwen-vl-text] coord item[36]: text=叩诊：肝上界位于第5肋间，肝浊音界正常，肝区无叩击痛、脾区无叩击痛、腹部无过度, bbox=[147, 690, 906, 706]
2026-08-10 06:12:48,396 INFO     29 [qwen-vl-text] coord item[37]: text=鼓音，移动性浊音阴性。, bbox=[107, 717, 312, 733]
2026-08-10 06:12:48,396 INFO     29 [qwen-vl-text] coord item[38]: text=听诊：肠蠕动音正常，频率4次/分，胃区无振水声，肝区无摩擦音、脾区无摩擦音，无血, bbox=[147, 744, 916, 760]
2026-08-10 06:12:48,396 INFO     29 [qwen-vl-text] coord item[39]: text=管杂音。, bbox=[107, 772, 174, 788]
2026-08-10 06:12:48,396 INFO     29 [qwen-vl-text] coord item[40]: text=外阴及肛门：阴毛分布正常；外生殖器发育正常，肛门检查：无外痔、肛裂、肛瘘、脱, bbox=[147, 800, 896, 816]
2026-08-10 06:12:48,396 INFO     29 [qwen-vl-text] coord item[41]: text=肛、湿疣等。, bbox=[107, 827, 214, 843]
2026-08-10 06:12:48,397 INFO     29 [qwen-vl-text] coord item[42]: text=脊柱：脊柱无畸形、压痛、叩击痛；脊柱两侧肌肉无紧张、压痛；肋脊角无压痛、叩痛。, bbox=[147, 855, 902, 871]
2026-08-10 06:12:48,397 INFO     29 [qwen-vl-text] coord item[43]: text=四肢：无畸形、杵状指（趾）、静脉曲张、外伤、骨折；肌肉张力正常与肌力5级，无萎, bbox=[147, 881, 903, 898]
2026-08-10 06:12:48,397 INFO     29 [qwen-vl-text] page=7 — 44/44 coords, api_time=15.5s
2026-08-10 06:12:48,399 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=596812, prompt_len=1012
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共23行）
["院", "入院记录", "姓名.", "科室:产科二区", "床号", "住院号.", "缩;关节无红肿、畸形、运动障碍,双下肢水肿。", "神经反射:膝腱反射正常、跟腱反射正常、肱二头肌腱反射正常、肱三头肌腱反射正常、", "腹壁反射正常、巴彬斯基征阴性、克尼格征阴性等。", "专科情况", "宫高34CM,腹围102CM,估计胎儿体重:3200g,胎位:头位,胎心152次/分,律齐,无", "宫缩,未见红,未破水,骨盆外测量及内诊:未做。", "辅助检查", "B超(2020.07.02 本院):晓孕宫内单活胎头位(双顶径9.4cm,股骨长7.0cm羊水指", "数8.5cm),胎盘成熟度II°.", "初步诊断:", "1.妊娠合并子宫瘢痕;", "3.孕2产,宫内孕39周头位待产。", "主治医师:", "孙小丹", "副主任医师:", "彭琼玉", "2020.07.08"]

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
2026-08-10 06:12:57,387 INFO     29 [qwen-vl-text] coord API raw response (len=1343):
[
	{"text": "院", "bbox": [569, 62, 629, 84]},
	{"text": "入院记录", "bbox": [440, 101, 588, 120]},
	{"text": "姓名.", "bbox": [111, 131, 158, 147]},
	{"text": "科室:产科二区", "bbox": [307, 131, 448, 147]},
	{"text": "床号", "bbox": [520, 131, 560, 147]},
	{"text": "住院号.", "bbox": [703, 131, 770, 147]},
	{"text": "缩;关节无红肿、畸形、运动障碍,双下肢水肿。", "bbox": [100, 155, 521, 172]},
	{"text": "神经反射:膝腱反射正常、跟腱反射正常、肱二头肌腱反射正常、肱三头肌腱反射正常、", "bbox": [141, 183, 912, 200]},
	{"text": "腹壁反射正常、巴彬斯基征阴性、克尼格征阴性等。", "bbox": [100, 210, 550, 227]},
	{"text": "专科情况", "bbox": [462, 245, 558, 263]},
	{"text": "宫高34CM,腹围102CM,估计胎儿体重:3200g,胎位:头位,胎心152次/分,律齐,无", "bbox": [158, 277, 925, 294]},
	{"text": "宫缩,未见红,未破水,骨盆外测量及内诊:未做。", "bbox": [102, 305, 550, 322]},
	{"text": "辅助检查", "bbox": [469, 334, 550, 350]},
	{"text": "B超(2020.07.02 本院):晓孕宫内单活胎头位(双顶径9.4cm,股骨长7.0cm羊水指", "bbox": [141, 362, 925, 379]},
	{"text": "数8.5cm),胎盘成熟度II°.", "bbox": [102, 389, 352, 406]},
	{"text": "初步诊断:", "bbox": [407, 417, 496, 434]},
	{"text": "1.妊娠合并子宫瘢痕;", "bbox": [541, 445, 728, 462]},
	{"text": "3.孕2产,宫内孕39周头位待产。", "bbox": [541, 472, 845, 489]},
	{"text": "主治医师:", "bbox": [669, 526, 756, 542]},
	{"text": "孙小丹", "bbox": [777, 507, 860, 534]},
	{"text": "副主任医师:", "bbox": [649, 582, 756, 598]},
	{"text": "彭琼玉", "bbox": [772, 562, 863, 596]},
	{"text": "2020.07.08", "bbox": [702, 610, 804, 624]}
]
2026-08-10 06:12:57,387 INFO     29 [qwen-vl-text] coord API: raw_items=23, valid_items=23, elapsed=9.0s
2026-08-10 06:12:57,388 INFO     29 [qwen-vl-text] coord item[0]: text=院, bbox=[569, 62, 629, 84]
2026-08-10 06:12:57,388 INFO     29 [qwen-vl-text] coord item[1]: text=入院记录, bbox=[440, 101, 588, 120]
2026-08-10 06:12:57,388 INFO     29 [qwen-vl-text] coord item[2]: text=姓名., bbox=[111, 131, 158, 147]
2026-08-10 06:12:57,388 INFO     29 [qwen-vl-text] coord item[3]: text=科室:产科二区, bbox=[307, 131, 448, 147]
2026-08-10 06:12:57,388 INFO     29 [qwen-vl-text] coord item[4]: text=床号, bbox=[520, 131, 560, 147]
2026-08-10 06:12:57,388 INFO     29 [qwen-vl-text] coord item[5]: text=住院号., bbox=[703, 131, 770, 147]
2026-08-10 06:12:57,388 INFO     29 [qwen-vl-text] coord item[6]: text=缩;关节无红肿、畸形、运动障碍,双下肢水肿。, bbox=[100, 155, 521, 172]
2026-08-10 06:12:57,388 INFO     29 [qwen-vl-text] coord item[7]: text=神经反射:膝腱反射正常、跟腱反射正常、肱二头肌腱反射正常、肱三头肌腱反射正常、, bbox=[141, 183, 912, 200]
2026-08-10 06:12:57,388 INFO     29 [qwen-vl-text] coord item[8]: text=腹壁反射正常、巴彬斯基征阴性、克尼格征阴性等。, bbox=[100, 210, 550, 227]
2026-08-10 06:12:57,388 INFO     29 [qwen-vl-text] coord item[9]: text=专科情况, bbox=[462, 245, 558, 263]
2026-08-10 06:12:57,388 INFO     29 [qwen-vl-text] coord item[10]: text=宫高34CM,腹围102CM,估计胎儿体重:3200g,胎位:头位,胎心152次/分,律齐,无, bbox=[158, 277, 925, 294]
2026-08-10 06:12:57,388 INFO     29 [qwen-vl-text] coord item[11]: text=宫缩,未见红,未破水,骨盆外测量及内诊:未做。, bbox=[102, 305, 550, 322]
2026-08-10 06:12:57,388 INFO     29 [qwen-vl-text] coord item[12]: text=辅助检查, bbox=[469, 334, 550, 350]
2026-08-10 06:12:57,388 INFO     29 [qwen-vl-text] coord item[13]: text=B超(2020.07.02 本院):晓孕宫内单活胎头位(双顶径9.4cm,股骨长7.0cm羊水指, bbox=[141, 362, 925, 379]
2026-08-10 06:12:57,388 INFO     29 [qwen-vl-text] coord item[14]: text=数8.5cm),胎盘成熟度II°., bbox=[102, 389, 352, 406]
2026-08-10 06:12:57,388 INFO     29 [qwen-vl-text] coord item[15]: text=初步诊断:, bbox=[407, 417, 496, 434]
2026-08-10 06:12:57,388 INFO     29 [qwen-vl-text] coord item[16]: text=1.妊娠合并子宫瘢痕;, bbox=[541, 445, 728, 462]
2026-08-10 06:12:57,388 INFO     29 [qwen-vl-text] coord item[17]: text=3.孕2产,宫内孕39周头位待产。, bbox=[541, 472, 845, 489]
2026-08-10 06:12:57,388 INFO     29 [qwen-vl-text] coord item[18]: text=主治医师:, bbox=[669, 526, 756, 542]
2026-08-10 06:12:57,388 INFO     29 [qwen-vl-text] coord item[19]: text=孙小丹, bbox=[777, 507, 860, 534]
2026-08-10 06:12:57,389 INFO     29 [qwen-vl-text] coord item[20]: text=副主任医师:, bbox=[649, 582, 756, 598]
2026-08-10 06:12:57,389 INFO     29 [qwen-vl-text] coord item[21]: text=彭琼玉, bbox=[772, 562, 863, 596]
2026-08-10 06:12:57,389 INFO     29 [qwen-vl-text] coord item[22]: text=2020.07.08, bbox=[702, 610, 804, 624]
2026-08-10 06:12:57,389 INFO     29 [qwen-vl-text] page=8 — 23/23 coords, api_time=9.0s
2026-08-10 06:12:57,389 INFO     29 [qwen-vl-text] new_positions (156):
[[5, 349.265, 368.305, 47.994, 64.834], [5, 264.775, 345.09999999999997, 78.306, 93.462], [5, 82.705, 128.51999999999998, 101.03999999999999, 114.512], [5, 190.39999999999998, 268.94, 101.03999999999999, 114.512], [5, 308.805, 334.39, 101.03999999999999, 114.512], [5, 82.705, 160.65, 121.24799999999999, 133.878], [5, 231.45499999999998, 314.755, 121.24799999999999, 133.878], [5, 355.215, 412.335, 121.24799999999999, 133.878], [5, 82.705, 109.47999999999999, 143.14, 155.76999999999998], [5, 187.42499999999998, 232.64499999999998, 143.14, 155.76999999999998], [5, 265.37, 320.11, 143.14, 155.76999999999998], [5, 348.075, 390.32, 143.14, 155.76999999999998], [5, 82.705, 109.47999999999999, 164.19, 176.82], [5, 187.42499999999998, 243.95, 164.19, 176.82], [5, 265.37, 321.3, 164.19, 176.82], [5, 348.075, 384.965, 164.19, 176.82], [5, 82.705, 137.445, 186.924, 200.396], [5, 327.25, 486.71, 186.924, 200.396], [5, 82.705, 105.315, 208.816, 222.28799999999998], [5, 321.895, 503.37, 208.816, 222.28799999999998], [5, 82.705, 120.19, 230.708, 244.17999999999998], [5, 264.775, 352.24, 230.708, 244.17999999999998], [5, 396.865, 484.33, 230.708, 244.17999999999998], [5, 82.705, 195.16, 253.44199999999998, 266.914], [5, 264.775, 290.955, 253.44199999999998, 266.914], [5, 396.865, 473.62, 253.44199999999998, 266.914], [5, 99.96, 261.8, 292.174, 305.646], [5, 77.945, 530.145, 313.224, 327.538], [5, 77.945, 530.145, 335.116, 349.43], [5, 77.945, 530.145, 357.008, 371.322], [5, 77.945, 530.145, 378.9, 393.214], [5, 77.945, 530.145, 401.63399999999996, 415.106], [5, 77.945, 530.145, 423.526, 437.84], [5, 77.945, 530.145, 445.418, 459.73199999999997], [5, 77.945, 458.15, 467.31, 481.62399999999997], [5, 101.14999999999999, 529.55, 489.202, 503.51599999999996], [5, 82.705, 524.79, 511.936, 526.25], [5, 77.945, 382.585, 533.828, 548.1419999999999], [5, 102.33999999999999, 531.3349999999999, 556.562, 570.034], [5, 77.945, 426.02, 578.454, 592.768], [5, 100.55499999999999, 224.91, 601.188, 614.66], [5, 256.445, 531.3349999999999, 601.188, 614.66], [5, 77.945, 521.22, 623.0799999999999, 637.394], [5, 77.945, 371.28, 645.814, 660.1279999999999], [5, 106.505, 531.93, 667.706, 682.02], [5, 77.945, 295.12, 690.4399999999999, 704.754], [5, 292.145, 320.11, 746.8539999999999, 758.6419999999999], [5, 364.73499999999996, 416.5, 746.8539999999999, 758.6419999999999], [5, 495.635, 533.12, 745.17, 757.8], [6, 343.315, 371.28, 51.361999999999995, 68.202], [6, 262.99, 347.47999999999996, 82.51599999999999, 97.672], [6, 74.375, 101.14999999999999, 106.092, 118.722], [6, 186.23499999999999, 267.75, 106.092, 118.722], [6, 308.805, 335.58, 106.092, 118.722], [6, 415.31, 453.39, 106.092, 118.722], [6, 91.63, 528.9549999999999, 125.458, 138.93], [6, 276.08, 331.41499999999996, 151.56, 165.874], [6, 91.63, 160.055, 178.504, 191.134], [6, 183.855, 258.825, 178.504, 191.134], [6, 285.59999999999997, 360.57, 178.504, 191.134], [6, 396.865, 483.14, 178.504, 191.976], [6, 91.63, 149.345, 202.07999999999998, 214.70999999999998], [6, 183.855, 242.165, 202.07999999999998, 216.394], [6, 91.63, 540.855, 224.814, 238.286], [6, 67.83, 223.72, 246.706, 260.178], [6, 91.63, 540.855, 270.282, 283.75399999999996], [6, 67.83, 154.105, 293.01599999999996, 306.488], [6, 91.63, 476.0, 315.75, 329.222], [6, 91.63, 117.80999999999999, 339.32599999999996, 351.95599999999996], [6, 91.63, 499.205, 361.21799999999996, 374.69], [6, 91.63, 533.715, 383.952, 397.424], [6, 67.83, 499.79999999999995, 406.686, 420.15799999999996], [6, 91.63, 424.23499999999996, 429.41999999999996, 442.892], [6, 91.63, 499.205, 451.312, 464.784], [6, 91.63, 540.855, 474.046, 487.518], [6, 67.83, 529.55, 496.78, 510.252], [6, 67.83, 247.51999999999998, 519.514, 532.986], [6, 91.63, 529.55, 542.2479999999999, 555.72], [6, 67.83, 165.41, 564.982, 578.454], [6, 91.63, 114.835, 587.716, 600.346], [6, 91.63, 540.855, 610.4499999999999, 623.922], [6, 67.83, 349.85999999999996, 633.184, 646.656], [6, 91.63, 476.0, 655.918, 669.39], [6, 126.14, 314.755, 678.6519999999999, 692.124], [6, 126.14, 459.34, 701.386, 714.858], [6, 126.14, 534.31, 723.278, 736.75], [6, 289.765, 318.91999999999996, 762.852, 774.64], [6, 365.33, 418.88, 762.852, 774.64], [6, 502.17999999999995, 541.4499999999999, 762.852, 774.64], [7, 344.505, 371.875, 53.046, 70.728], [7, 262.99, 348.66999999999996, 84.2, 100.198], [7, 68.425, 97.58, 109.46, 122.08999999999999], [7, 183.855, 266.56, 109.46, 122.08999999999999], [7, 309.4, 330.82, 109.46, 122.08999999999999], [7, 427.21, 455.77, 109.46, 122.08999999999999], [7, 63.665, 151.13, 129.668, 143.14], [7, 87.46499999999999, 545.02, 151.56, 165.03199999999998], [7, 63.665, 210.035, 175.136, 188.608], [7, 121.975, 539.0699999999999, 199.554, 213.02599999999998], [7, 63.665, 139.23, 222.28799999999998, 235.76], [7, 121.975, 385.56, 245.022, 258.49399999999997], [7, 111.86, 136.85, 266.914, 278.702], [7, 248.70999999999998, 273.10499999999996, 266.914, 278.702], [7, 388.53499999999997, 413.525, 266.914, 278.702], [7, 120.19, 127.33, 283.75399999999996, 294.7], [7, 256.445, 265.965, 283.75399999999996, 294.7], [7, 390.91499999999996, 409.955, 283.75399999999996, 294.7], [7, 120.19, 127.33, 299.752, 310.698], [7, 255.255, 268.34499999999997, 299.752, 310.698], [7, 396.865, 403.40999999999997, 299.752, 310.698], [7, 120.19, 127.33, 314.908, 325.854], [7, 255.85, 267.75, 314.908, 325.854], [7, 390.91499999999996, 409.955, 314.908, 325.854], [7, 256.445, 265.965, 330.06399999999996, 341.01], [7, 396.865, 403.40999999999997, 330.06399999999996, 341.01], [7, 92.82, 268.34499999999997, 348.58799999999997, 361.21799999999996], [7, 121.975, 528.36, 372.164, 385.63599999999997], [7, 63.665, 121.38, 395.74, 408.37], [7, 87.46499999999999, 302.85499999999996, 418.474, 431.94599999999997], [7, 87.46499999999999, 431.96999999999997, 442.05, 455.522], [7, 87.46499999999999, 114.835, 464.784, 478.256], [7, 87.46499999999999, 533.715, 487.518, 500.99], [7, 63.665, 268.34499999999997, 511.094, 524.566], [7, 87.46499999999999, 545.02, 533.828, 548.1419999999999], [7, 63.665, 514.675, 557.404, 570.876], [7, 87.46499999999999, 539.0699999999999, 580.98, 594.452], [7, 63.665, 185.64, 603.7139999999999, 617.1859999999999], [7, 87.46499999999999, 545.02, 626.448, 639.92], [7, 63.665, 103.53, 650.024, 663.496], [7, 87.46499999999999, 533.12, 673.6, 687.072], [7, 63.665, 127.33, 696.334, 709.8059999999999], [7, 87.46499999999999, 536.6899999999999, 719.91, 733.382], [7, 87.46499999999999, 537.285, 741.802, 756.116], [8, 338.555, 374.255, 52.204, 70.728], [8, 261.8, 349.85999999999996, 85.042, 101.03999999999999], [8, 66.045, 94.00999999999999, 110.30199999999999, 123.774], [8, 182.665, 266.56, 110.30199999999999, 123.774], [8, 309.4, 333.2, 110.30199999999999, 123.774], [8, 418.28499999999997, 458.15, 110.30199999999999, 123.774], [8, 59.5, 309.995, 130.51, 144.82399999999998], [8, 83.895, 542.64, 154.08599999999998, 168.4], [8, 59.5, 327.25, 176.82, 191.134], [8, 274.89, 332.01, 206.29, 221.446], [8, 94.00999999999999, 550.375, 233.23399999999998, 247.548], [8, 60.69, 327.25, 256.81, 271.12399999999997], [8, 279.055, 327.25, 281.228, 294.7], [8, 83.895, 550.375, 304.804, 319.118], [8, 60.69, 209.44, 327.538, 341.852], [8, 242.165, 295.12, 351.114, 365.428], [8, 321.895, 433.15999999999997, 374.69, 389.00399999999996], [8, 321.895, 502.775, 397.424, 411.738], [8, 398.055, 449.82, 442.892, 456.364], [8, 462.315, 511.7, 426.894, 449.628], [8, 386.155, 449.82, 490.044, 503.51599999999996], [8, 459.34, 513.485, 473.204, 501.832], [8, 417.69, 478.38, 513.62, 525.408]]
2026-08-10 06:12:57,389 INFO     29 [qwen-vl-text] ═══ DONE ═══ 156 positions, pages=4, time=100.0s
2026-08-10 06:12:57,966 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 06:12:57,967 INFO     29 [Trace] task=801b5176 | doc=DAXI-哮喘.pdf | Extractor:Admission | outputs={"chunks": "1 items, types={'AdmissionRecord': 1}", "html": "", "json": "2283 items", "markdown": "", "text": "", "name": "DAXI-哮喘.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "14 items, types={'OutpatientRecord': 14}", "chunks_Prescription": "6 items, types={'PrescriptionRecord': 6}", "chunks_LabExam": "13 items, types={'LabReport': 13}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 14, \"chunks_Prescription\": 6, \"chunks_LabExam\": 13}"}
2026-08-10 06:12:57,967 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 06:12:57,968 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T06:12:57.967+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 1, "failed": 0, "current": {"801b5176947e11f182aec5d26bc6c4ae": {"id": "801b5176947e11f182aec5d26bc6c4ae", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786340646131, "task_type": "dataflow", "root_trace_id": "97b84aa3d1154f6db808c154432c5554", "root_traceparent": "00-97b84aa3d1154f6db808c154432c5554-dd9503e7c4e14a5d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "4115cdf4948211f1bd9827cf206dfa2d": {"id": "4115cdf4948211f1bd9827cf206dfa2d", "doc_id": "40948096948211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "GWHU-48\u5c81-\u7537(2).pdf", "type": "pdf", "location": "GWHU-48\u5c81-\u7537(2).pdf", "size": 1182408, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786342258386, "task_type": "dataflow", "root_trace_id": "0d4f1377f2e04befb139f86a697fd302", "root_traceparent": "00-0d4f1377f2e04befb139f86a697fd302-ea5641fe487f4324-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 06:12:57,980 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 06:12:57,982 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:12:57,982 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 06:12:57,982 INFO     29 [qwen-vl-text] positions(70): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 06:12:57,982 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [70]
2026-08-10 06:12:58,200 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 06:12:58,202 INFO     29 [qwen-vl-text] LLM extraction start, text_len=768
2026-08-10 06:12:58,202 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:12:58,202 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 0, \"bbox_end\": 69, \"encounter_dates\": [\"2026-01-29\"], \"department\": \"普通儿科一区\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "呼出气一氧化氮测定报告单\n病人信息：\n编号：482\n姓名：\n年龄：41岁9月27天\n性别：女\n科室：普通儿科一区\n出生日期：1984-04-02\n测定时间：2026/1/29 11:02:42\n测定信息：\n一小时内禁止饮食：■是\n一小时内禁止剧烈运动：■是\n三小时内禁止食用特殊食品*：■是\n一小时内禁止抽烟：■是\n三天内使用激素类药物：■是 □否\n三天内使用抗生素：□是 ■否\n症状：□咳嗽 □喘息 □鼻塞 □喷嚏 ■其他\n病史：□过敏史 □其它\n*是指西兰花、芥蓝、生菜、莴苣、芹菜、水萝卜、熏制、腌制类食品。\n测定项目：\n呼气方式：■在线 □离线 □潮气\n呼气温度：20.1℃\n呼气压力：13.6cmH20\n呼气平均流速：48ml/s\n呼气NO浓度：\n32.7,31.0,32.0,31.8,32.1,31.7ppb\n呼气NO浓度均值:32ppb\n呼气方式：■在线 □离线 □潮气\n呼气温度：20.3℃\n呼气压力：7.9cmH20\n呼气平均流速：207ml/s\n呼气NO浓度：\n11.7,11.9,11.3,11.6,11.6,11.6ppb\n呼气NO浓度均值:12ppb\n测定结果：\nFeNO50：32ppb\nFeNO200：12ppb\nCaNO：3.6ppb\n测定意义：\n测定浓度\n参考值\n炎症鉴别诊断\n>12岁\n≤12岁\nFeNO50\n<25ppb\n<20ppb*\n非嗜酸性气道炎症\n25-50ppb\n20-35ppb*\n混合型气道炎症\n≥50ppb\n≥35ppb*\n嗜酸性气道炎症\nFeNO200\n>10ppb\n>8ppb\n小气道炎症\nCaNO\n>5ppb\n>3ppb\n肺泡炎症\n(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)\n复查时间：\n操作员：赵彩红\n医生：马春英\n电\n告\n单\n更",
    "role": "user"
  }
]
2026-08-10 06:12:59,881 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:12:59,893 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 06:12:59,893 INFO     29 [Trace] task=4115cdf4 | doc=GWHU-48岁-男(2).pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "248 items", "markdown": "", "text": "", "name": "GWHU-48岁-男(2).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:12:59,893 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 06:12:59,921 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:12:59,921 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:13:00,560 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:13:00,569 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 06:13:00,569 INFO     29 [Trace] task=4115cdf4 | doc=GWHU-48岁-男(2).pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "248 items", "markdown": "", "text": "", "name": "GWHU-48岁-男(2).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:13:00,569 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 06:13:00,579 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:13:00,579 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:13:01,259 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:13:01,266 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 06:13:01,266 INFO     29 [Trace] task=4115cdf4 | doc=GWHU-48岁-男(2).pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "248 items", "markdown": "", "text": "", "name": "GWHU-48岁-男(2).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:13:01,266 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 06:13:01,273 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:13:01,273 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 06:13:01,968 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:13:01,976 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 06:13:01,976 INFO     29 [Trace] task=4115cdf4 | doc=GWHU-48岁-男(2).pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "248 items", "markdown": "", "text": "", "name": "GWHU-48岁-男(2).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:13:01,976 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 06:13:01,986 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 06:13:01,987 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:13:01,987 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 06:13:01,987 INFO     29 [qwen-vl-text] positions(223): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 06:13:01,988 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [223]
2026-08-10 06:13:02,193 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 06:13:02,194 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1117
2026-08-10 06:13:02,194 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:13:02,194 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 25, \"bbox_end\": 247, \"encounter_dates\": [\"2024-07-22\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "鹤煤总医院肺功能报告单\nID号：4000\n姓名：\n性别：男\n年龄：48\n身高：170 cm\n体重：95 kg\nB.S.A：2.06m²\n温度(℃)：22\n湿度(%)：50\n气压(mmHg)：1013.3\n科室：\n病区：\n预测公式：亚洲\n医生：李志军\n备注：\nSVC\n实测\n预测\n%预测\nBD后\n改进率\nVC\nL\n2.94\n3.78\n77.8\nIC\nL\nTV\nL\nERV\nL\nIRV\nL\nFVC\n实测\n预测\n%预测\nBD后\n改进率\nFVC\nL\n2.94\n3.78\n77.8\n3.01\n2.4\nFEV0.5\nL\n1.26\n1.62\n28.6\nFEV1.0\nL\n1.88\n3.26\n57.7\n2.21\n17.6\nFEV3.0\nL\n2.74\n2.91\n6.2\nFEV1.0%(G)\n%\n63.95\n73.89\n86.5\n73.42\n14.8\nFEV1.0%(T)\n%\n63.95\nFEV1/VCpr\n%\n49.7\n58.5\n17.7\nMMF\nL/s\n1.17\n4.16\n28.1\n1.69\n44.4\nPEF\nL/s\n5.36\n8.7\n61.6\n4.37\n-18.5\nFEF25\nL/s\n2.3\n7.82\n29.4\n3.84\n67\nFEF50\nL/s\n1.45\n5.31\n27.3\n2.11\n45.5\nFEF75\nL/s\n0.61\n2.39\n25.5\n0.7\n14.8\nFEF90\nL/s\n0.23\n0.31\n34.8\nFEF50/FEF75\n2.38\n3.01\n26.5\nPEF/HT\nL/s/m\n3.15\n2.57\n-18.4\nFEF25/HT\nL/s/m\n1.35\n2.26\n67.4\nFEF75-85\nL/s\n0.47\n0.53\n12.8\nFEF0.2-1.2\nL/s\n2.37\n3.61\n52.3\nOI\nL/s\n5.21\n2.19\n-58\nATI\n%\nPEFTIME\nSec\n0.05\n0.08\n60\nFET\nSec\n4.46\n3.72\n-16.6\nVextrap\nL\n0.05\n0.09\n80\nExtrap V\n%\n1.7\n2.99\n75.9\nFIVC\nL\n2.93\n3.42\n16.7\nMVV\n实测\n预测\n%预测\nBD后\n改进率\nMVV\nL/min\n126.6\nRR\nC/min\nTV\nL\nMVV/BSA\nL/min/m²\nAVI\n诊断报告：\n检查技师：\n检查日期：2024-7-22\nFEV1% Restictive Normal\nSVC\n70\nMixed\nObstructive\n60\n%VC\n3\n0\n30\n50\n90 SEC\n12\nFVC\n8\n4\n0\n8 L\n-4\n-8\n-12\n4L\nMVV\n2\n0\n5\n10\n15 SEC",
    "role": "user"
  }
]
2026-08-10 06:13:10,739 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:13:10,740 INFO     29 [qwen-vl-text] LLM output (len=1104):
{
  "exam_date": "2026-01-29",
  "report_date": "2026-01-29",
  "exam_name": "呼出气一氧化氮测定",
  "exam_category": "other",
  "body_part": "呼出气",
  "patient_name": null,
  "patient_gender": "女",
  "department": "普通儿科一区",
  "bed_number": null,
  "findings": "测定信息：\n一小时内禁止饮食：■是\n一小时内禁止剧烈运动：■是\n三小时内禁止食用特殊食品*：■是\n一小时内禁止抽烟：■是\n三天内使用激素类药物：■是 □否\n三天内使用抗生素：□是 ■否\n症状：□咳嗽 □喘息 □鼻塞 □喷嚏 ■其他\n病史：□过敏史 □其它\n*是指西兰花、芥蓝、生菜、莴苣、芹菜、水萝卜、熏制、腌制类食品。\n测定项目：\n呼气方式：■在线 □离线 □潮气\n呼气温度：20.1℃\n呼气压力：13.6cmH20\n呼气平均流速：48ml/s\n呼气NO浓度：\n32.7,31.0,32.0,31.8,32.1,31.7ppb\n呼气NO浓度均值:32ppb\n呼气方式：■在线 □离线 □潮气\n呼气温度：20.3℃\n呼气压力：7.9cmH20\n呼气平均流速：207ml/s\n呼气NO浓度：\n11.7,11.9,11.3,11.6,11.6,11.6ppb\n呼气NO浓度均值:12ppb",
  "conclusion": "测定结果：\nFeNO50：32ppb\nFeNO200：12ppb\nCaNO：3.6ppb\n测定意义：\n| 测定浓度 | 参考值 >12岁 | 参考值 ≤12岁 | 炎症鉴别诊断 |\n| :--- | :--- | :--- | :--- |\n| FeNO50 | <25ppb | <20ppb* | 非嗜酸性气道炎症 |\n| FeNO50 | 25-50ppb | 20-35ppb* | 混合型气道炎症 |\n| FeNO50 | ≥50ppb | ≥35ppb* | 嗜酸性气道炎症 |\n| FeNO200 | >10ppb | >8ppb | 小气道炎症 |\n| CaNO | >5ppb | >3ppb | 肺泡炎症 |\n\n(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)",
  "physician": "马春英",
  "reviewer": null
}
2026-08-10 06:13:10,743 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1025288, prompt_len=1591
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共70行）
["呼出气一氧化氮测定报告单", "病人信息：", "编号：482", "姓名：", "年龄：41岁9月27天", "性别：女", "科室：普通儿科一区", "出生日期：1984-04-02", "测定时间：2026/1/29 11:02:42", "测定信息：", "一小时内禁止饮食：■是", "一小时内禁止剧烈运动：■是", "三小时内禁止食用特殊食品*：■是", "一小时内禁止抽烟：■是", "三天内使用激素类药物：■是 □否", "三天内使用抗生素：□是 ■否", "症状：□咳嗽 □喘息 □鼻塞 □喷嚏 ■其他", "病史：□过敏史 □其它", "*是指西兰花、芥蓝、生菜、莴苣、芹菜、水萝卜、熏制、腌制类食品。", "测定项目：", "呼气方式：■在线 □离线 □潮气", "呼气温度：20.1℃", "呼气压力：13.6cmH20", "呼气平均流速：48ml/s", "呼气NO浓度：", "32.7,31.0,32.0,31.8,32.1,31.7ppb", "呼气NO浓度均值:32ppb", "呼气方式：■在线 □离线 □潮气", "呼气温度：20.3℃", "呼气压力：7.9cmH20", "呼气平均流速：207ml/s", "呼气NO浓度：", "11.7,11.9,11.3,11.6,11.6,11.6ppb", "呼气NO浓度均值:12ppb", "测定结果：", "FeNO50：32ppb", "FeNO200：12ppb", "CaNO：3.6ppb", "测定意义：", "测定浓度", "参考值", "炎症鉴别诊断", ">12岁", "≤12岁", "FeNO50", "<25ppb", "<20ppb*", "非嗜酸性气道炎症", "25-50ppb", "20-35ppb*", "混合型气道炎症", "≥50ppb", "≥35ppb*", "嗜酸性气道炎症", "FeNO200", ">10ppb", ">8ppb", "小气道炎症", "CaNO", ">5ppb", ">3ppb", "肺泡炎症", "(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)", "复查时间：", "操作员：赵彩红", "医生：马春英", "电", "告", "单", "更"]

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
2026-08-10 06:13:34,982 INFO     29 [qwen-vl-text] coord API raw response (len=3851):
[
	{"text": "呼出气一氧化氮测定报告单", "bbox": [376, 112, 653, 129]},
	{"text": "病人信息：", "bbox": [125, 140, 215, 154]},
	{"text": "编号：482", "bbox": [125, 156, 200, 169]},
	{"text": "姓名：", "bbox": [388, 156, 442, 169]},
	{"text": "年龄：41岁9月27天", "bbox": [647, 156, 790, 169]},
	{"text": "性别：女", "bbox": [125, 170, 191, 183]},
	{"text": "科室：普通儿科一区", "bbox": [388, 170, 536, 183]},
	{"text": "出生日期：1984-04-02", "bbox": [647, 170, 815, 183]},
	{"text": "测定时间：2026/1/29 11:02:42", "bbox": [125, 184, 360, 197]},
	{"text": "测定信息：", "bbox": [125, 199, 215, 213]},
	{"text": "一小时内禁止饮食：■是", "bbox": [125, 217, 458, 230]},
	{"text": "一小时内禁止剧烈运动：■是", "bbox": [516, 217, 867, 230]},
	{"text": "三小时内禁止食用特殊食品*：■是", "bbox": [125, 231, 458, 244]},
	{"text": "一小时内禁止抽烟：■是", "bbox": [516, 231, 867, 244]},
	{"text": "三天内使用激素类药物：■是 □否", "bbox": [125, 245, 458, 258]},
	{"text": "三天内使用抗生素：□是 ■否", "bbox": [516, 245, 867, 258]},
	{"text": "症状：□咳嗽 □喘息 □鼻塞 □喷嚏 ■其他", "bbox": [125, 259, 458, 272]},
	{"text": "病史：□过敏史 □其它", "bbox": [516, 259, 740, 272]},
	{"text": "*是指西兰花、芥蓝、生菜、莴苣、芹菜、水萝卜、熏制、腌制类食品。", "bbox": [125, 273, 638, 286]},
	{"text": "测定项目：", "bbox": [125, 288, 215, 302]},
	{"text": "呼气方式：■在线 □离线 □潮气", "bbox": [125, 305, 425, 318]},
	{"text": "呼气温度：20.1℃", "bbox": [125, 320, 257, 333]},
	{"text": "呼气压力：13.6cmH20", "bbox": [125, 335, 283, 348]},
	{"text": "呼气平均流速：48ml/s", "bbox": [125, 349, 291, 362]},
	{"text": "呼气NO浓度：", "bbox": [125, 363, 214, 376]},
	{"text": "32.7,31.0,32.0,31.8,32.1,31.7ppb", "bbox": [125, 377, 391, 390]},
	{"text": "呼气NO浓度均值:32ppb", "bbox": [125, 391, 296, 404]},
	{"text": "呼气方式：■在线 □离线 □潮气", "bbox": [516, 305, 815, 318]},
	{"text": "呼气温度：20.3℃", "bbox": [516, 320, 647, 333]},
	{"text": "呼气压力：7.9cmH20", "bbox": [516, 335, 665, 348]},
	{"text": "呼气平均流速：207ml/s", "bbox": [516, 349, 690, 362]},
	{"text": "呼气NO浓度：", "bbox": [516, 363, 606, 376]},
	{"text": "11.7,11.9,11.3,11.6,11.6,11.6ppb", "bbox": [516, 377, 782, 390]},
	{"text": "呼气NO浓度均值:12ppb", "bbox": [516, 391, 688, 404]},
	{"text": "测定结果：", "bbox": [125, 590, 215, 605]},
	{"text": "FeNO50：32ppb", "bbox": [266, 591, 394, 605]},
	{"text": "FeNO200：12ppb", "bbox": [475, 591, 608, 605]},
	{"text": "CaNO：3.6ppb", "bbox": [691, 591, 815, 605]},
	{"text": "测定意义：", "bbox": [125, 609, 215, 623]},
	{"text": "测定浓度", "bbox": [170, 627, 240, 640]},
	{"text": "参考值", "bbox": [376, 627, 427, 640]},
	{"text": "炎症鉴别诊断", "bbox": [658, 627, 760, 640]},
	{"text": ">12岁", "bbox": [314, 642, 360, 655]},
	{"text": "≤12岁", "bbox": [444, 642, 490, 655]},
	{"text": "FeNO50", "bbox": [180, 671, 229, 683]},
	{"text": "<25ppb", "bbox": [311, 657, 365, 669]},
	{"text": "<20ppb*", "bbox": [438, 657, 498, 669]},
	{"text": "非嗜酸性气道炎症", "bbox": [647, 657, 770, 669]},
	{"text": "25-50ppb", "bbox": [306, 671, 368, 683]},
	{"text": "20-35ppb*", "bbox": [433, 671, 503, 683]},
	{"text": "混合型气道炎症", "bbox": [655, 671, 763, 683]},
	{"text": "≥50ppb", "bbox": [310, 685, 365, 698]},
	{"text": "≥35ppb*", "bbox": [437, 685, 499, 698]},
	{"text": "嗜酸性气道炎症", "bbox": [655, 685, 763, 698]},
	{"text": "FeNO200", "bbox": [175, 700, 233, 712]},
	{"text": ">10ppb", "bbox": [311, 700, 365, 712]},
	{"text": ">8ppb", "bbox": [444, 700, 490, 712]},
	{"text": "小气道炎症", "bbox": [670, 700, 747, 712]},
	{"text": "CaNO", "bbox": [188, 714, 221, 726]},
	{"text": ">5ppb", "bbox": [314, 714, 360, 726]},
	{"text": ">3ppb", "bbox": [444, 714, 490, 726]},
	{"text": "肺泡炎症", "bbox": [678, 714, 740, 726]},
	{"text": "(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)", "bbox": [150, 727, 653, 739]},
	{"text": "复查时间：", "bbox": [129, 817, 209, 831]},
	{"text": "操作员：赵彩红", "bbox": [129, 840, 278, 854]},
	{"text": "医生：马春英", "bbox": [185, 862, 278, 876]},
	{"text": "电", "bbox": [488, 820, 505, 838]},
	{"text": "告", "bbox": [488, 853, 505, 877]},
	{"text": "单", "bbox": [488, 865, 505, 880]},
	{"text": "更", "bbox": [710, 826, 727, 840]}
]
2026-08-10 06:13:34,982 INFO     29 [qwen-vl-text] coord API: raw_items=70, valid_items=70, elapsed=24.2s
2026-08-10 06:13:34,982 INFO     29 [qwen-vl-text] coord item[0]: text=呼出气一氧化氮测定报告单, bbox=[376, 112, 653, 129]
2026-08-10 06:13:34,982 INFO     29 [qwen-vl-text] coord item[1]: text=病人信息：, bbox=[125, 140, 215, 154]
2026-08-10 06:13:34,982 INFO     29 [qwen-vl-text] coord item[2]: text=编号：482, bbox=[125, 156, 200, 169]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[388, 156, 442, 169]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：41岁9月27天, bbox=[647, 156, 790, 169]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[5]: text=性别：女, bbox=[125, 170, 191, 183]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[6]: text=科室：普通儿科一区, bbox=[388, 170, 536, 183]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[7]: text=出生日期：1984-04-02, bbox=[647, 170, 815, 183]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[8]: text=测定时间：2026/1/29 11:02:42, bbox=[125, 184, 360, 197]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[9]: text=测定信息：, bbox=[125, 199, 215, 213]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[10]: text=一小时内禁止饮食：■是, bbox=[125, 217, 458, 230]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[11]: text=一小时内禁止剧烈运动：■是, bbox=[516, 217, 867, 230]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[12]: text=三小时内禁止食用特殊食品*：■是, bbox=[125, 231, 458, 244]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[13]: text=一小时内禁止抽烟：■是, bbox=[516, 231, 867, 244]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[14]: text=三天内使用激素类药物：■是 □否, bbox=[125, 245, 458, 258]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[15]: text=三天内使用抗生素：□是 ■否, bbox=[516, 245, 867, 258]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[16]: text=症状：□咳嗽 □喘息 □鼻塞 □喷嚏 ■其他, bbox=[125, 259, 458, 272]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[17]: text=病史：□过敏史 □其它, bbox=[516, 259, 740, 272]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[18]: text=*是指西兰花、芥蓝、生菜、莴苣、芹菜、水萝卜、熏制、腌制类食品。, bbox=[125, 273, 638, 286]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[19]: text=测定项目：, bbox=[125, 288, 215, 302]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[20]: text=呼气方式：■在线 □离线 □潮气, bbox=[125, 305, 425, 318]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[21]: text=呼气温度：20.1℃, bbox=[125, 320, 257, 333]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[22]: text=呼气压力：13.6cmH20, bbox=[125, 335, 283, 348]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[23]: text=呼气平均流速：48ml/s, bbox=[125, 349, 291, 362]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[24]: text=呼气NO浓度：, bbox=[125, 363, 214, 376]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[25]: text=32.7,31.0,32.0,31.8,32.1,31.7ppb, bbox=[125, 377, 391, 390]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[26]: text=呼气NO浓度均值:32ppb, bbox=[125, 391, 296, 404]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[27]: text=呼气方式：■在线 □离线 □潮气, bbox=[516, 305, 815, 318]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[28]: text=呼气温度：20.3℃, bbox=[516, 320, 647, 333]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[29]: text=呼气压力：7.9cmH20, bbox=[516, 335, 665, 348]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[30]: text=呼气平均流速：207ml/s, bbox=[516, 349, 690, 362]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[31]: text=呼气NO浓度：, bbox=[516, 363, 606, 376]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[32]: text=11.7,11.9,11.3,11.6,11.6,11.6ppb, bbox=[516, 377, 782, 390]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[33]: text=呼气NO浓度均值:12ppb, bbox=[516, 391, 688, 404]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[34]: text=测定结果：, bbox=[125, 590, 215, 605]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[35]: text=FeNO50：32ppb, bbox=[266, 591, 394, 605]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[36]: text=FeNO200：12ppb, bbox=[475, 591, 608, 605]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[37]: text=CaNO：3.6ppb, bbox=[691, 591, 815, 605]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[38]: text=测定意义：, bbox=[125, 609, 215, 623]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[39]: text=测定浓度, bbox=[170, 627, 240, 640]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[40]: text=参考值, bbox=[376, 627, 427, 640]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[41]: text=炎症鉴别诊断, bbox=[658, 627, 760, 640]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[42]: text=>12岁, bbox=[314, 642, 360, 655]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[43]: text=≤12岁, bbox=[444, 642, 490, 655]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[44]: text=FeNO50, bbox=[180, 671, 229, 683]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[45]: text=<25ppb, bbox=[311, 657, 365, 669]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[46]: text=<20ppb*, bbox=[438, 657, 498, 669]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[47]: text=非嗜酸性气道炎症, bbox=[647, 657, 770, 669]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[48]: text=25-50ppb, bbox=[306, 671, 368, 683]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[49]: text=20-35ppb*, bbox=[433, 671, 503, 683]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[50]: text=混合型气道炎症, bbox=[655, 671, 763, 683]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[51]: text=≥50ppb, bbox=[310, 685, 365, 698]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[52]: text=≥35ppb*, bbox=[437, 685, 499, 698]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[53]: text=嗜酸性气道炎症, bbox=[655, 685, 763, 698]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[54]: text=FeNO200, bbox=[175, 700, 233, 712]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[55]: text=>10ppb, bbox=[311, 700, 365, 712]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[56]: text=>8ppb, bbox=[444, 700, 490, 712]
2026-08-10 06:13:34,983 INFO     29 [qwen-vl-text] coord item[57]: text=小气道炎症, bbox=[670, 700, 747, 712]
2026-08-10 06:13:34,984 INFO     29 [qwen-vl-text] coord item[58]: text=CaNO, bbox=[188, 714, 221, 726]
2026-08-10 06:13:34,984 INFO     29 [qwen-vl-text] coord item[59]: text=>5ppb, bbox=[314, 714, 360, 726]
2026-08-10 06:13:34,984 INFO     29 [qwen-vl-text] coord item[60]: text=>3ppb, bbox=[444, 714, 490, 726]
2026-08-10 06:13:34,984 INFO     29 [qwen-vl-text] coord item[61]: text=肺泡炎症, bbox=[678, 714, 740, 726]
2026-08-10 06:13:34,984 INFO     29 [qwen-vl-text] coord item[62]: text=(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb), bbox=[150, 727, 653, 739]
2026-08-10 06:13:34,984 INFO     29 [qwen-vl-text] coord item[63]: text=复查时间：, bbox=[129, 817, 209, 831]
2026-08-10 06:13:34,984 INFO     29 [qwen-vl-text] coord item[64]: text=操作员：赵彩红, bbox=[129, 840, 278, 854]
2026-08-10 06:13:34,984 INFO     29 [qwen-vl-text] coord item[65]: text=医生：马春英, bbox=[185, 862, 278, 876]
2026-08-10 06:13:34,984 INFO     29 [qwen-vl-text] coord item[66]: text=电, bbox=[488, 820, 505, 838]
2026-08-10 06:13:34,984 INFO     29 [qwen-vl-text] coord item[67]: text=告, bbox=[488, 853, 505, 877]
2026-08-10 06:13:34,984 INFO     29 [qwen-vl-text] coord item[68]: text=单, bbox=[488, 865, 505, 880]
2026-08-10 06:13:34,984 INFO     29 [qwen-vl-text] coord item[69]: text=更, bbox=[710, 826, 727, 840]
2026-08-10 06:13:34,984 INFO     29 [qwen-vl-text] page=0 — 70/70 coords, api_time=24.2s
2026-08-10 06:13:34,984 INFO     29 [qwen-vl-text] new_positions (70):
[[0, 223.72, 388.53499999999997, 94.304, 108.618], [0, 74.375, 127.925, 117.88, 129.668], [0, 74.375, 119.0, 131.352, 142.298], [0, 230.85999999999999, 262.99, 131.352, 142.298], [0, 384.965, 470.04999999999995, 131.352, 142.298], [0, 74.375, 113.645, 143.14, 154.08599999999998], [0, 230.85999999999999, 318.91999999999996, 143.14, 154.08599999999998], [0, 384.965, 484.92499999999995, 143.14, 154.08599999999998], [0, 74.375, 214.2, 154.928, 165.874], [0, 74.375, 127.925, 167.558, 179.346], [0, 74.375, 272.51, 182.714, 193.66], [0, 307.02, 515.865, 182.714, 193.66], [0, 74.375, 272.51, 194.50199999999998, 205.44799999999998], [0, 307.02, 515.865, 194.50199999999998, 205.44799999999998], [0, 74.375, 272.51, 206.29, 217.236], [0, 307.02, 515.865, 206.29, 217.236], [0, 74.375, 272.51, 218.078, 229.024], [0, 307.02, 440.29999999999995, 218.078, 229.024], [0, 74.375, 379.60999999999996, 229.86599999999999, 240.81199999999998], [0, 74.375, 127.925, 242.49599999999998, 254.284], [0, 74.375, 252.875, 256.81, 267.756], [0, 74.375, 152.915, 269.44, 280.38599999999997], [0, 74.375, 168.385, 282.07, 293.01599999999996], [0, 74.375, 173.14499999999998, 293.858, 304.804], [0, 74.375, 127.33, 305.646, 316.592], [0, 74.375, 232.64499999999998, 317.43399999999997, 328.38], [0, 74.375, 176.12, 329.222, 340.168], [0, 307.02, 484.92499999999995, 256.81, 267.756], [0, 307.02, 384.965, 269.44, 280.38599999999997], [0, 307.02, 395.67499999999995, 282.07, 293.01599999999996], [0, 307.02, 410.54999999999995, 293.858, 304.804], [0, 307.02, 360.57, 305.646, 316.592], [0, 307.02, 465.28999999999996, 317.43399999999997, 328.38], [0, 307.02, 409.35999999999996, 329.222, 340.168], [0, 74.375, 127.925, 496.78, 509.40999999999997], [0, 158.26999999999998, 234.42999999999998, 497.62199999999996, 509.40999999999997], [0, 282.625, 361.76, 497.62199999999996, 509.40999999999997], [0, 411.145, 484.92499999999995, 497.62199999999996, 509.40999999999997], [0, 74.375, 127.925, 512.778, 524.566], [0, 101.14999999999999, 142.79999999999998, 527.934, 538.88], [0, 223.72, 254.065, 527.934, 538.88], [0, 391.51, 452.2, 527.934, 538.88], [0, 186.82999999999998, 214.2, 540.564, 551.51], [0, 264.18, 291.55, 540.564, 551.51], [0, 107.1, 136.255, 564.982, 575.086], [0, 185.045, 217.17499999999998, 553.194, 563.298], [0, 260.61, 296.31, 553.194, 563.298], [0, 384.965, 458.15, 553.194, 563.298], [0, 182.07, 218.95999999999998, 564.982, 575.086], [0, 257.635, 299.28499999999997, 564.982, 575.086], [0, 389.72499999999997, 453.98499999999996, 564.982, 575.086], [0, 184.45, 217.17499999999998, 576.77, 587.716], [0, 260.015, 296.905, 576.77, 587.716], [0, 389.72499999999997, 453.98499999999996, 576.77, 587.716], [0, 104.125, 138.635, 589.4, 599.504], [0, 185.045, 217.17499999999998, 589.4, 599.504], [0, 264.18, 291.55, 589.4, 599.504], [0, 398.65, 444.465, 589.4, 599.504], [0, 111.86, 131.495, 601.188, 611.292], [0, 186.82999999999998, 214.2, 601.188, 611.292], [0, 264.18, 291.55, 601.188, 611.292], [0, 403.40999999999997, 440.29999999999995, 601.188, 611.292], [0, 89.25, 388.53499999999997, 612.134, 622.2379999999999], [0, 76.755, 124.35499999999999, 687.914, 699.702], [0, 76.755, 165.41, 707.28, 719.068], [0, 110.07499999999999, 165.41, 725.804, 737.592], [0, 290.36, 300.47499999999997, 690.4399999999999, 705.596], [0, 290.36, 300.47499999999997, 718.226, 738.434], [0, 290.36, 300.47499999999997, 728.3299999999999, 740.9599999999999], [0, 422.45, 432.565, 695.492, 707.28]]
2026-08-10 06:13:34,984 INFO     29 [qwen-vl-text] ═══ DONE ═══ 70 positions, pages=1, time=37.0s
2026-08-10 06:13:34,984 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 06:13:34,991 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 06:13:34,991 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 06:13:34,991 INFO     29 [qwen-vl-text] positions(197): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 06:13:34,992 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [197]
2026-08-10 06:13:35,231 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 06:13:35,233 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1255
2026-08-10 06:13:35,233 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:13:35,233 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 70, \"bbox_end\": 266, \"encounter_dates\": [\"2026-01-15\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "肺功能检查报告单\n姓名：\n测试号：\n住院号：\n身高：\n160 cm\n年龄：\n41 岁\n体重：\n48 kg\n性别：\n女\n身份证号：\n科别：\n联系电话：\n预计值\nBst % (Bst/\nA1\nA2\nA3\nFVC\n[L]\n3.13\n3.15\n100.54\n3.15\n3.08\n3.07\nFEV 1\n[L]\n2.70\n1.99\n73.90\n1.99\n1.85\n1.96\nFEV6\n[L]\n3.13\n3.13\n3.05\nFEV 1 % FVC\n[%]\n83.98\n63.25\n75.31\n63.25\n60.02\n63.82\nFEV 1 % VC MAX\n[%]\n81.31\n63.25\n77.78\n63.25\n58.74\n62.12\nFIF 50\n[L/s]\n5.84\n5.77\n5.84\n5.48\nFEV3 % FVC\n[%]\n89.30\n89.30\n87.11\n88.97\nVC MAX\n[L]\n3.19\n3.15\n98.65\n2.99\nPEF\n[L/s]\n6.46\n6.33\n97.97\n6.33\n5.90\n5.95\nMMEF 75/25\n[L/s]\n3.53\n1.06\n30.03\n1.06\n0.89\n0.99\nMEF 25\n[L/s]\n1.77\n0.46\n26.28\n0.46\n0.38\n0.40\nMEF 50\n[L/s]\n4.06\n1.25\n30.90\n1.25\n1.13\n1.24\nMEF 75\n[L/s]\n5.73\n3.01\n52.56\n3.01\n2.22\n2.68\nV backextrapolation [B]\n0.06\n0.06\n0.05\n0.06\nV backextrapol. % FVC\n1.86\n1.86\n1.52\n1.82\nFET\n[s]\n8.73\n8.73\n5.99\n6.71\nFEF 200-1200\n[L/s]\n3.07\n3.07\n2.51\n2.98\nFVC IN\n[L]\n3.19\n2.99\n93.64\n2.26\n2.99\n2.94\nFIV1\n[L]\n2.96\n2.24\n2.96\n2.92\nFIV1 % FVC\n[%]\n99.14\n99.32\n99.14\n99.48\nFEF50 % FIF50\n[%]\n21.46\n21.72\n19.34\n22.60\nPIF\n[L/s]\n6.10\n5.87\n6.10\n5.50\nMVV\n[L/min]\n101.9\n91.45\n89.73\n91.45\nBF MVV\n[1/min]\n75.65\n75.65\n10\nFlow [L/s]\nF/V ex\nVol [L]\nVol%VCmax\nVol [L]\nTime [s]\nVol [L]\nTime [s]\n意见：\n1.轻度阻塞性通气功能障碍。\n检查质量：FVC：A级。 FEV1：A级。\n备注：受检者检查配合佳。结果仅供参考，请结合临床分析。\n2.最大自主分钟通气量（MVV）在正常范围。\n备注：患者MVV配合佳。结果仅供参考，请结合临床分析。\n审核医生：孙帅森\n检测技师：韦龙华\n2026/1/15",
    "role": "user"
  }
]
2026-08-10 06:13:35,236 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T06:13:35.235+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 1, "failed": 0, "current": {"801b5176947e11f182aec5d26bc6c4ae": {"id": "801b5176947e11f182aec5d26bc6c4ae", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786340646131, "task_type": "dataflow", "root_trace_id": "97b84aa3d1154f6db808c154432c5554", "root_traceparent": "00-97b84aa3d1154f6db808c154432c5554-dd9503e7c4e14a5d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "4115cdf4948211f1bd9827cf206dfa2d": {"id": "4115cdf4948211f1bd9827cf206dfa2d", "doc_id": "40948096948211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "GWHU-48\u5c81-\u7537(2).pdf", "type": "pdf", "location": "GWHU-48\u5c81-\u7537(2).pdf", "size": 1182408, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786342258386, "task_type": "dataflow", "root_trace_id": "0d4f1377f2e04befb139f86a697fd302", "root_traceparent": "00-0d4f1377f2e04befb139f86a697fd302-ea5641fe487f4324-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 06:13:35,240 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 06:13:35,240 INFO     29 [qwen-vl-text] LLM output (len=1488):
{
  "exam_date": "2024-07-22",
  "report_date": null,
  "exam_name": "肺功能检查",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "ID号：4000\n姓名：\n性别：男\n年龄：48\n身高：170 cm\n体重：95 kg\nB.S.A：2.06m²\n温度(℃)：22\n湿度(%)：50\n气压(mmHg)：1013.3\n科室：\n病区：\n预测公式：亚洲\n医生：李志军\n备注：\nSVC\n实测 预测 %预测 BD后 改进率\nVC L 2.94 3.78 77.8\nIC L\nTV L\nERV L\nIRV L\nFVC\n实测 预测 %预测 BD后 改进率\nFVC L 2.94 3.78 77.8 3.01 2.4\nFEV0.5 L 1.26 1.62 28.6\nFEV1.0 L 1.88 3.26 57.7 2.21 17.6\nFEV3.0 L 2.74 2.91 6.2\nFEV1.0%(G) % 63.95 73.89 86.5 73.42 14.8\nFEV1.0%(T) % 63.95\nFEV1/VCpr % 49.7 58.5 17.7\nMMF L/s 1.17 4.16 28.1 1.69 44.4\nPEF L/s 5.36 8.7 61.6 4.37 -18.5\nFEF25 L/s 2.3 7.82 29.4 3.84 67\nFEF50 L/s 1.45 5.31 27.3 2.11 45.5\nFEF75 L/s 0.61 2.39 25.5 0.7 14.8\nFEF90 L/s 0.23 0.31 34.8\nFEF50/FEF75 2.38 3.01 26.5\nPEF/HT L/s/m 3.15 2.57 -18.4\nFEF25/HT L/s/m 1.35 2.26 67.4\nFEF75-85 L/s 0.47 0.53 12.8\nFEF0.2-1.2 L/s 2.37 3.61 52.3\nOI L/s 5.21 2.19 -58\nATI %\nPEFTIME Sec 0.05 0.08 60\nFET Sec 4.46 3.72 -16.6\nVextrap L 0.05 0.09 80\nExtrap V % 1.7 2.99 75.9\nFIVC L 2.93 3.42 16.7\nMVV\n实测 预测 %预测 BD后 改进率\nMVV L/min 126.6\nRR C/min\nTV L\nMVV/BSA L/min/m²\nAVI",
  "conclusion": "诊断报告：\n检查技师：\n检查日期：2024-7-22\nFEV1% Restictive Normal\nSVC\n70\nMixed\nObstructive\n60\n%VC\n3\n0\n30\n50\n90 SEC\n12\nFVC\n8\n4\n0\n8 L\n-4\n-8\n-12\n4L\nMVV\n2\n0\n5\n10\n15 SEC",
  "physician": "李志军",
  "reviewer": null
}
2026-08-10 06:13:35,242 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1090086, prompt_len=2400
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共223行）
["鹤煤总医院肺功能报告单", "ID号：4000", "姓名：", "性别：男", "年龄：48", "身高：170 cm", "体重：95 kg", "B.S.A：2.06m²", "温度(℃)：22", "湿度(%)：50", "气压(mmHg)：1013.3", "科室：", "病区：", "预测公式：亚洲", "医生：李志军", "备注：", "SVC", "实测", "预测", "%预测", "BD后", "改进率", "VC", "L", "2.94", "3.78", "77.8", "IC", "L", "TV", "L", "ERV", "L", "IRV", "L", "FVC", "实测", "预测", "%预测", "BD后", "改进率", "FVC", "L", "2.94", "3.78", "77.8", "3.01", "2.4", "FEV0.5", "L", "1.26", "1.62", "28.6", "FEV1.0", "L", "1.88", "3.26", "57.7", "2.21", "17.6", "FEV3.0", "L", "2.74", "2.91", "6.2", "FEV1.0%(G)", "%", "63.95", "73.89", "86.5", "73.42", "14.8", "FEV1.0%(T)", "%", "63.95", "FEV1/VCpr", "%", "49.7", "58.5", "17.7", "MMF", "L/s", "1.17", "4.16", "28.1", "1.69", "44.4", "PEF", "L/s", "5.36", "8.7", "61.6", "4.37", "-18.5", "FEF25", "L/s", "2.3", "7.82", "29.4", "3.84", "67", "FEF50", "L/s", "1.45", "5.31", "27.3", "2.11", "45.5", "FEF75", "L/s", "0.61", "2.39", "25.5", "0.7", "14.8", "FEF90", "L/s", "0.23", "0.31", "34.8", "FEF50/FEF75", "2.38", "3.01", "26.5", "PEF/HT", "L/s/m", "3.15", "2.57", "-18.4", "FEF25/HT", "L/s/m", "1.35", "2.26", "67.4", "FEF75-85", "L/s", "0.47", "0.53", "12.8", "FEF0.2-1.2", "L/s", "2.37", "3.61", "52.3", "OI", "L/s", "5.21", "2.19", "-58", "ATI", "%", "PEFTIME", "Sec", "0.05", "0.08", "60", "FET", "Sec", "4.46", "3.72", "-16.6", "Vextrap", "L", "0.05", "0.09", "80", "Extrap V", "%", "1.7", "2.99", "75.9", "FIVC", "L", "2.93", "3.42", "16.7", "MVV", "实测", "预测", "%预测", "BD后", "改进率", "MVV", "L/min", "126.6", "RR", "C/min", "TV", "L", "MVV/BSA", "L/min/m²", "AVI", "诊断报告：", "检查技师：", "检查日期：2024-7-22", "FEV1% Restictive Normal", "SVC", "70", "Mixed", "Obstructive", "60", "%VC", "3", "0", "30", "50", "90 SEC", "12", "FVC", "8", "4", "0", "8 L", "-4", "-8", "-12", "4L", "MVV", "2", "0", "5", "10", "15 SEC"]

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
2026-08-10 06:14:43,142 INFO     29 [qwen-vl-text] coord API raw response (len=10810):
[
	{"text": "鹤煤总医院肺功能报告单", "bbox": [327, 52, 613, 71]},
	{"text": "ID号：4000", "bbox": [64, 90, 145, 102]},
	{"text": "姓名：", "bbox": [226, 90, 266, 102]},
	{"text": "性别：男", "bbox": [392, 90, 457, 102]},
	{"text": "年龄：48", "bbox": [555, 88, 620, 100]},
	{"text": "身高：170 cm", "bbox": [721, 88, 819, 100]},
	{"text": "体重：95 kg", "bbox": [64, 110, 153, 122]},
	{"text": "B.S.A：2.06m²", "bbox": [226, 110, 335, 122]},
	{"text": "温度(℃)：22", "bbox": [392, 109, 491, 121]},
	{"text": "湿度(%)：50", "bbox": [555, 109, 645, 121]},
	{"text": "气压(mmHg)：1013.3", "bbox": [721, 108, 868, 120]},
	{"text": "科室：", "bbox": [64, 130, 102, 142]},
	{"text": "病区：", "bbox": [226, 130, 266, 142]},
	{"text": "预测公式：亚洲", "bbox": [392, 130, 506, 142]},
	{"text": "医生：李志军", "bbox": [555, 129, 652, 141]},
	{"text": "备注：", "bbox": [721, 129, 759, 141]},
	{"text": "SVC", "bbox": [117, 156, 145, 168]},
	{"text": "实测", "bbox": [231, 156, 265, 168]},
	{"text": "预测", "bbox": [302, 156, 336, 168]},
	{"text": "%预测", "bbox": [365, 156, 408, 168]},
	{"text": "BD后", "bbox": [440, 156, 473, 168]},
	{"text": "改进率", "bbox": [501, 156, 549, 168]},
	{"text": "VC", "bbox": [51, 171, 69, 183]},
	{"text": "L", "bbox": [201, 171, 210, 183]},
	{"text": "2.94", "bbox": [218, 171, 250, 183]},
	{"text": "3.78", "bbox": [287, 171, 320, 183]},
	{"text": "77.8", "bbox": [356, 171, 390, 183]},
	{"text": "IC", "bbox": [51, 187, 69, 199]},
	{"text": "L", "bbox": [201, 187, 210, 199]},
	{"text": "TV", "bbox": [51, 202, 67, 214]},
	{"text": "L", "bbox": [201, 202, 210, 214]},
	{"text": "ERV", "bbox": [51, 218, 77, 230]},
	{"text": "L", "bbox": [201, 218, 210, 230]},
	{"text": "IRV", "bbox": [51, 234, 77, 246]},
	{"text": "L", "bbox": [201, 234, 210, 246]},
	{"text": "FVC", "bbox": [117, 249, 145, 261]},
	{"text": "实测", "bbox": [231, 249, 265, 261]},
	{"text": "预测", "bbox": [302, 249, 336, 261]},
	{"text": "%预测", "bbox": [365, 249, 408, 261]},
	{"text": "BD后", "bbox": [440, 249, 473, 261]},
	{"text": "改进率", "bbox": [501, 249, 549, 261]},
	{"text": "FVC", "bbox": [51, 265, 77, 277]},
	{"text": "L", "bbox": [201, 265, 210, 277]},
	{"text": "2.94", "bbox": [218, 265, 250, 277]},
	{"text": "3.78", "bbox": [287, 265, 320, 277]},
	{"text": "77.8", "bbox": [356, 265, 390, 277]},
	{"text": "3.01", "bbox": [424, 265, 457, 277]},
	{"text": "2.4", "bbox": [493, 265, 519, 277]},
	{"text": "FEV0.5", "bbox": [51, 280, 102, 292]},
	{"text": "L", "bbox": [201, 280, 210, 292]},
	{"text": "1.26", "bbox": [218, 280, 250, 292]},
	{"text": "1.62", "bbox": [424, 280, 457, 292]},
	{"text": "28.6", "bbox": [493, 280, 526, 292]},
	{"text": "FEV1.0", "bbox": [51, 296, 102, 308]},
	{"text": "L", "bbox": [201, 296, 210, 308]},
	{"text": "1.88", "bbox": [218, 296, 250, 308]},
	{"text": "3.26", "bbox": [287, 296, 320, 308]},
	{"text": "57.7", "bbox": [356, 296, 390, 308]},
	{"text": "2.21", "bbox": [424, 296, 457, 308]},
	{"text": "17.6", "bbox": [493, 296, 526, 308]},
	{"text": "FEV3.0", "bbox": [51, 311, 102, 323]},
	{"text": "L", "bbox": [201, 311, 210, 323]},
	{"text": "2.74", "bbox": [218, 311, 250, 323]},
	{"text": "2.91", "bbox": [424, 311, 457, 323]},
	{"text": "6.2", "bbox": [493, 311, 519, 323]},
	{"text": "FEV1.0%(G)", "bbox": [51, 327, 132, 339]},
	{"text": "%", "bbox": [201, 327, 210, 339]},
	{"text": "63.95", "bbox": [218, 327, 259, 339]},
	{"text": "73.89", "bbox": [287, 327, 329, 339]},
	{"text": "86.5", "bbox": [356, 327, 390, 339]},
	{"text": "73.42", "bbox": [424, 327, 467, 339]},
	{"text": "14.8", "bbox": [493, 327, 526, 339]},
	{"text": "FEV1.0%(T)", "bbox": [51, 342, 132, 354]},
	{"text": "%", "bbox": [201, 342, 210, 354]},
	{"text": "63.95", "bbox": [218, 342, 259, 354]},
	{"text": "FEV1/VCpr", "bbox": [51, 358, 127, 370]},
	{"text": "%", "bbox": [201, 358, 210, 370]},
	{"text": "49.7", "bbox": [218, 358, 250, 370]},
	{"text": "58.5", "bbox": [424, 358, 460, 370]},
	{"text": "17.7", "bbox": [493, 358, 526, 370]},
	{"text": "MMF", "bbox": [51, 373, 80, 385]},
	{"text": "L/s", "bbox": [185, 373, 210, 385]},
	{"text": "1.17", "bbox": [218, 373, 250, 385]},
	{"text": "4.16", "bbox": [287, 373, 320, 385]},
	{"text": "28.1", "bbox": [356, 373, 390, 385]},
	{"text": "1.69", "bbox": [424, 373, 457, 385]},
	{"text": "44.4", "bbox": [493, 373, 526, 385]},
	{"text": "PEF", "bbox": [51, 389, 80, 401]},
	{"text": "L/s", "bbox": [185, 389, 210, 401]},
	{"text": "5.36", "bbox": [218, 389, 250, 401]},
	{"text": "8.7", "bbox": [287, 389, 312, 401]},
	{"text": "61.6", "bbox": [356, 389, 390, 401]},
	{"text": "4.37", "bbox": [424, 389, 457, 401]},
	{"text": "-18.5", "bbox": [493, 389, 535, 401]},
	{"text": "FEF25", "bbox": [51, 404, 95, 416]},
	{"text": "L/s", "bbox": [185, 404, 210, 416]},
	{"text": "2.3", "bbox": [218, 404, 242, 416]},
	{"text": "7.82", "bbox": [287, 404, 320, 416]},
	{"text": "29.4", "bbox": [356, 404, 390, 416]},
	{"text": "3.84", "bbox": [424, 404, 457, 416]},
	{"text": "67", "bbox": [493, 404, 511, 416]},
	{"text": "FEF50", "bbox": [51, 419, 95, 431]},
	{"text": "L/s", "bbox": [185, 419, 210, 431]},
	{"text": "1.45", "bbox": [218, 419, 250, 431]},
	{"text": "5.31", "bbox": [287, 419, 320, 431]},
	{"text": "27.3", "bbox": [356, 419, 390, 431]},
	{"text": "2.11", "bbox": [424, 419, 457, 431]},
	{"text": "45.5", "bbox": [493, 419, 526, 431]},
	{"text": "FEF75", "bbox": [51, 435, 95, 447]},
	{"text": "L/s", "bbox": 185, 435, 210, 447]},
	{"text": "0.61", "bbox": [218, 435, 250, 447]},
	{"text": "2.39", "bbox": [287, 435, 320, 447]},
	{"text": "25.5", "bbox": [356, 435, 390, 447]},
	{"text": "0.7", "bbox": [424, 435, 452, 447]},
	{"text": "14.8", "bbox": [493, 435, 526, 447]},
	{"text": "FEF90", "bbox": [51, 450, 95, 462]},
	{"text": "L/s", "bbox": 185, 450, 210, 462]},
	{"text": "0.23", "bbox": [218, 450, 250, 462]},
	{"text": "0.31", "bbox": [424, 450, 457, 462]},
	{"text": "34.8", "bbox": [493, 450, 526, 462]},
	{"text": "FEF50/FEF75", "bbox": [51, 465, 145, 477]},
	{"text": "2.38", "bbox": [218, 465, 250, 477]},
	{"text": "3.01", "bbox": [424, 465, 457, 477]},
	{"text": "26.5", "bbox": [493, 465, 526, 477]},
	{"text": "PEF/HT", "bbox": [51, 480, 104, 492]},
	{"text": "L/s/m", "bbox": [171, 480, 210, 492]},
	{"text": "3.15", "bbox": [218, 480, 250, 492]},
	{"text": "2.57", "bbox": [424, 480, 457, 492]},
	{"text": "-18.4", "bbox": [493, 480, 535, 492]},
	{"text": "FEF25/HT", "bbox": [51, 496, 120, 508]},
	{"text": "L/s/m", "bbox": 171, 496, 210, 508]},
	{"text": "1.35", "bbox": [218, 496, 250, 508]},
	{"text": "2.26", "bbox": 424, 496, 457, 508]},
	{"text": "67.4", "bbox": [493, 496, 526, 508]},
	{"text": "FEF75-85", "bbox": [51, 511, 120, 523]},
	{"text": "L/s", "bbox": 185, 511, 210, 523]},
	{"text": "0.47", "bbox": [218, 511, 250, 523]},
	{"text": "0.53", "bbox": 424, 511, 457, 523]},
	{"text": "12.8", "bbox": 493, 511, 526, 523]},
	{"text": "FEF0.2-1.2", "bbox": [51, 526, 136, 538]},
	{"text": "L/s", "bbox": 185, 526, 210, 538]},
	{"text": "2.37", "bbox": 218, 526, 250, 538]},
	{"text": "3.61", "bbox": 424, 526, 457, 538]},
	{"text": "52.3", "bbox": 493, 526, 526, 538]},
	{"text": "OI", "bbox": [51, 542, 69, 554]},
	{"text": "L/s", "bbox": 185, 542, 210, 554]},
	{"text": "5.21", "bbox": 218, 542, 250, 554]},
	{"text": "2.19", "bbox": 424, 542, 457, 554]},
	{"text": "-58", "bbox": 493, 542, 519, 554]},
	{"text": "ATI", "bbox": [51, 557, 79, 569]},
	{"text": "%", "bbox": 201, 557, 210, 569]},
	{"text": "PEFTIME", "bbox": [51, 572, 111, 584]},
	{"text": "Sec", "bbox": 187, 572, 210, 584]},
	{"text": "0.05", "bbox": 218, 572, 250, 584]},
	{"text": "0.08", "bbox": 424, 572, 457, 584]},
	{"text": "60", "bbox": 493, 572, 511, 584]},
	{"text": "FET", "bbox": 51, 588, 79, 600]},
	{"text": "Sec", "bbox": 187, 588, 210, 600]},
	{"text": "4.46", "bbox": 218, 588, 250, 600]},
	{"text": "3.72", "bbox": 424, 588, 457, 600]},
	{"text": "-16.6", "bbox": 493, 588, 535, 600]},
	{"text": "Vextrap", "bbox": 51, 603, 111, 615]},
	{"text": "L", "bbox": 201, 603, 210, 615]},
	{"text": "0.05", "bbox": 218, 603, 250, 615]},
	{"text": "0.09", "bbox": 424, 603, 457, 615]},
	{"text": "80", "bbox": 493, 603, 511, 615]},
	{"text": "Extrap V", "bbox": 51, 618, 119, 630]},
	{"text": "%", "bbox": 201, 618, 210, 630]},
	{"text": "1.7", "bbox": 218, 618, 242, 630]},
	{"text": "2.99", "bbox": 424, 618, 457, 630]},
	{"text": "75.9", "bbox": 493, 618, 526, 630]},
	{"text": "FIVC", "bbox": 51, 633, 89, 645]},
	{"text": "L", "bbox": 201, 633, 210, 645]},
	{"text": "2.93", "bbox": 218, 633, 250, 645]},
	{"text": "3.42", "bbox": 424, 633, 457, 645]},
	{"text": "16.7", "bbox": 493, 633, 526, 645]},
	{"text": "MVV", "bbox": [119, 649, 145, 661]},
	{"text": "实测", "bbox": 231, 649, 265, 661]},
	{"text": "预测", "bbox": 302, 649, 336, 661]},
	{"text": "%预测", "bbox": 365, 649, 408, 661]},
	{"text": "BD后", "bbox": 440, 649, 473, 661]},
	{"text": "改进率", "bbox": 501, 649, 549, 661]},
	{"text": "MVV", "bbox": 51, 664, 79, 676]},
	{"text": "L/min", "bbox": 171, 664, 210, 676]},
	{"text": "126.6", "bbox": 287, 664, 329, 676]},
	{"text": "RR", "bbox": 51, 680, 71, 692]},
	{"text": "C/min", "bbox": 171, 680, 210, 692]},
	{"text": "TV", "bbox": 51, 695, 71, 707]},
	{"text": "L", "bbox": 201, 695, 210, 707]},
	{"text": "MVV/BSA", "bbox": 51, 710, 111, 722]},
	{"text": "L/min/m²", "bbox": 145, 710, 210, 722]},
	{"text": "AVI", "bbox": 51, 726, 79, 738]},
	{"text": "诊断报告：", "bbox": [71, 740, 141, 752]},
	{"text": "检查技师：", "bbox": [53, 870, 122, 882]},
	{"text": "检查日期：2024-7-22", "bbox": [751, 870, 906, 882]},
	{"text": "FEV1% Restictive Normal", "bbox": [747, 164, 907, 173]},
	{"text": "SVC", "bbox": [698, 180, 724, 190]},
	{"text": "70", "bbox": [766, 190, 780, 198]},
	{"text": "Mixed", "bbox": [794, 221, 826, 229]},
	{"text": "Obstructive", "bbox": [865, 220, 934, 229]},
	{"text": "60", "bbox": [856, 235, 870, 243]},
	{"text": "%VC", "bbox": [893, 235, 912, 243]},
	{"text": "3", "bbox": [580, 245, 594, 255]},
	{"text": "0", "bbox": [589, 319, 599, 328]},
	{"text": "30", "bbox": [680, 317, 698, 327]},
	{"text": "50", "bbox": [774, 317, 792, 327]},
	{"text": "90 SEC", "bbox": [854, 317, 907, 327]},
	{"text": "12", "bbox": [574, 365, 594, 375]},
	{"text": "FVC", "bbox": [696, 363, 724, 373]},
	{"text": "8", "bbox": [584, 406, 594, 416]},
	{"text": "4", "bbox": [584, 447, 594, 457]},
	{"text": "0", "bbox": [584, 488, 594, 498]},
	{"text": "8 L", "bbox": [865, 494, 895, 505]},
	{"text": "-4", "bbox": [574, 529, 594, 539]},
	{"text": "-8", "bbox": [574, 570, 594, 580]},
	{"text": "-12", "bbox": [564, 611, 594, 621]},
	{"text": "4L", "bbox": [574, 690, 594, 700]},
	{"text": "MVV", "bbox": [698, 690, 724, 700]},
	{"text": "2", "bbox": [584, 752, 594, 762]},
	{"text": "0", "bbox": [593, 826, 602, 836]},
	{"text": "5", "bbox": [688, 825, 698, 835]},
	{"text": "10", "bbox": [780, 825, 798, 835]},
	{"text": "15 SEC", "bbox": [858, 825, 912, 835]}
]
2026-08-10 06:14:43,143 INFO     29 [qwen-vl-text] coord JSON strict parse failed, trying json_repair
2026-08-10 06:14:43,149 INFO     29 [qwen-vl-text] coord API: raw_items=223, valid_items=168, elapsed=67.9s
2026-08-10 06:14:43,149 INFO     29 [qwen-vl-text] coord item[0]: text=鹤煤总医院肺功能报告单, bbox=[327, 52, 613, 71]
2026-08-10 06:14:43,149 INFO     29 [qwen-vl-text] coord item[1]: text=ID号：4000, bbox=[64, 90, 145, 102]
2026-08-10 06:14:43,149 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[226, 90, 266, 102]
2026-08-10 06:14:43,149 INFO     29 [qwen-vl-text] coord item[3]: text=性别：男, bbox=[392, 90, 457, 102]
2026-08-10 06:14:43,149 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：48, bbox=[555, 88, 620, 100]
2026-08-10 06:14:43,149 INFO     29 [qwen-vl-text] coord item[5]: text=身高：170 cm, bbox=[721, 88, 819, 100]
2026-08-10 06:14:43,149 INFO     29 [qwen-vl-text] coord item[6]: text=体重：95 kg, bbox=[64, 110, 153, 122]
2026-08-10 06:14:43,149 INFO     29 [qwen-vl-text] coord item[7]: text=B.S.A：2.06m², bbox=[226, 110, 335, 122]
2026-08-10 06:14:43,149 INFO     29 [qwen-vl-text] coord item[8]: text=温度(℃)：22, bbox=[392, 109, 491, 121]
2026-08-10 06:14:43,149 INFO     29 [qwen-vl-text] coord item[9]: text=湿度(%)：50, bbox=[555, 109, 645, 121]
2026-08-10 06:14:43,149 INFO     29 [qwen-vl-text] coord item[10]: text=气压(mmHg)：1013.3, bbox=[721, 108, 868, 120]
2026-08-10 06:14:43,149 INFO     29 [qwen-vl-text] coord item[11]: text=科室：, bbox=[64, 130, 102, 142]
2026-08-10 06:14:43,149 INFO     29 [qwen-vl-text] coord item[12]: text=病区：, bbox=[226, 130, 266, 142]
2026-08-10 06:14:43,150 INFO     29 [qwen-vl-text] coord item[13]: text=预测公式：亚洲, bbox=[392, 130, 506, 142]
2026-08-10 06:14:43,150 INFO     29 [qwen-vl-text] coord item[14]: text=医生：李志军, bbox=[555, 129, 652, 141]
2026-08-10 06:14:43,150 INFO     29 [qwen-vl-text] coord item[15]: text=备注：, bbox=[721, 129, 759, 141]
2026-08-10 06:14:43,150 INFO     29 [qwen-vl-text] coord item[16]: text=SVC, bbox=[117, 156, 145, 168]
2026-08-10 06:14:43,150 INFO     29 [qwen-vl-text] coord item[17]: text=实测, bbox=[231, 156, 265, 168]
2026-08-10 06:14:43,150 INFO     29 [qwen-vl-text] coord item[18]: text=预测, bbox=[302, 156, 336, 168]
2026-08-10 06:14:43,150 INFO     29 [qwen-vl-text] coord item[19]: text=%预测, bbox=[365, 156, 408, 168]
2026-08-10 06:14:43,150 INFO     29 [qwen-vl-text] coord item[20]: text=BD后, bbox=[440, 156, 473, 168]
2026-08-10 06:14:43,150 INFO     29 [qwen-vl-text] coord item[21]: text=改进率, bbox=[501, 156, 549, 168]
2026-08-10 06:14:43,150 INFO     29 [qwen-vl-text] coord item[22]: text=VC, bbox=[51, 171, 69, 183]
2026-08-10 06:14:43,150 INFO     29 [qwen-vl-text] coord item[23]: text=L, bbox=[201, 171, 210, 183]
2026-08-10 06:14:43,150 INFO     29 [qwen-vl-text] coord item[24]: text=2.94, bbox=[218, 171, 250, 183]
2026-08-10 06:14:43,150 INFO     29 [qwen-vl-text] coord item[25]: text=3.78, bbox=[287, 171, 320, 183]
2026-08-10 06:14:43,150 INFO     29 [qwen-vl-text] coord item[26]: text=77.8, bbox=[356, 171, 390, 183]
2026-08-10 06:14:43,150 INFO     29 [qwen-vl-text] coord item[27]: text=IC, bbox=[51, 187, 69, 199]
2026-08-10 06:14:43,150 INFO     29 [qwen-vl-text] coord item[28]: text=L, bbox=[201, 187, 210, 199]
2026-08-10 06:14:43,150 INFO     29 [qwen-vl-text] coord item[29]: text=TV, bbox=[51, 202, 67, 214]
2026-08-10 06:14:43,151 INFO     29 [qwen-vl-text] coord item[30]: text=L, bbox=[201, 202, 210, 214]
2026-08-10 06:14:43,151 INFO     29 [qwen-vl-text] coord item[31]: text=ERV, bbox=[51, 218, 77, 230]
2026-08-10 06:14:43,151 INFO     29 [qwen-vl-text] coord item[32]: text=L, bbox=[201, 218, 210, 230]
2026-08-10 06:14:43,151 INFO     29 [qwen-vl-text] coord item[33]: text=IRV, bbox=[51, 234, 77, 246]
2026-08-10 06:14:43,151 INFO     29 [qwen-vl-text] coord item[34]: text=L, bbox=[201, 234, 210, 246]
2026-08-10 06:14:43,151 INFO     29 [qwen-vl-text] coord item[35]: text=FVC, bbox=[117, 249, 145, 261]
2026-08-10 06:14:43,151 INFO     29 [qwen-vl-text] coord item[36]: text=实测, bbox=[231, 249, 265, 261]
2026-08-10 06:14:43,151 INFO     29 [qwen-vl-text] coord item[37]: text=预测, bbox=[302, 249, 336, 261]
2026-08-10 06:14:43,151 INFO     29 [qwen-vl-text] coord item[38]: text=%预测, bbox=[365, 249, 408, 261]
2026-08-10 06:14:43,151 INFO     29 [qwen-vl-text] coord item[39]: text=BD后, bbox=[440, 249, 473, 261]
2026-08-10 06:14:43,151 INFO     29 [qwen-vl-text] coord item[40]: text=改进率, bbox=[501, 249, 549, 261]
2026-08-10 06:14:43,151 INFO     29 [qwen-vl-text] coord item[41]: text=FVC, bbox=[51, 265, 77, 277]
2026-08-10 06:14:43,151 INFO     29 [qwen-vl-text] coord item[42]: text=L, bbox=[201, 265, 210, 277]
2026-08-10 06:14:43,151 INFO     29 [qwen-vl-text] coord item[43]: text=2.94, bbox=[218, 265, 250, 277]
2026-08-10 06:14:43,151 INFO     29 [qwen-vl-text] coord item[44]: text=3.78, bbox=[287, 265, 320, 277]
2026-08-10 06:14:43,151 INFO     29 [qwen-vl-text] coord item[45]: text=77.8, bbox=[356, 265, 390, 277]
2026-08-10 06:14:43,152 INFO     29 [qwen-vl-text] coord item[46]: text=3.01, bbox=[424, 265, 457, 277]
2026-08-10 06:14:43,152 INFO     29 [qwen-vl-text] coord item[47]: text=2.4, bbox=[493, 265, 519, 277]
2026-08-10 06:14:43,152 INFO     29 [qwen-vl-text] coord item[48]: text=FEV0.5, bbox=[51, 280, 102, 292]
2026-08-10 06:14:43,152 INFO     29 [qwen-vl-text] coord item[49]: text=L, bbox=[201, 280, 210, 292]
2026-08-10 06:14:43,152 INFO     29 [qwen-vl-text] coord item[50]: text=1.26, bbox=[218, 280, 250, 292]
2026-08-10 06:14:43,152 INFO     29 [qwen-vl-text] coord item[51]: text=1.62, bbox=[424, 280, 457, 292]
2026-08-10 06:14:43,152 INFO     29 [qwen-vl-text] coord item[52]: text=28.6, bbox=[493, 280, 526, 292]
2026-08-10 06:14:43,152 INFO     29 [qwen-vl-text] coord item[53]: text=FEV1.0, bbox=[51, 296, 102, 308]
2026-08-10 06:14:43,152 INFO     29 [qwen-vl-text] coord item[54]: text=L, bbox=[201, 296, 210, 308]
2026-08-10 06:14:43,152 INFO     29 [qwen-vl-text] coord item[55]: text=1.88, bbox=[218, 296, 250, 308]
2026-08-10 06:14:43,152 INFO     29 [qwen-vl-text] coord item[56]: text=3.26, bbox=[287, 296, 320, 308]
2026-08-10 06:14:43,152 INFO     29 [qwen-vl-text] coord item[57]: text=57.7, bbox=[356, 296, 390, 308]
2026-08-10 06:14:43,152 INFO     29 [qwen-vl-text] coord item[58]: text=2.21, bbox=[424, 296, 457, 308]
2026-08-10 06:14:43,152 INFO     29 [qwen-vl-text] coord item[59]: text=17.6, bbox=[493, 296, 526, 308]
2026-08-10 06:14:43,152 INFO     29 [qwen-vl-text] coord item[60]: text=FEV3.0, bbox=[51, 311, 102, 323]
2026-08-10 06:14:43,152 INFO     29 [qwen-vl-text] coord item[61]: text=L, bbox=[201, 311, 210, 323]
2026-08-10 06:14:43,153 INFO     29 [qwen-vl-text] coord item[62]: text=2.74, bbox=[218, 311, 250, 323]
2026-08-10 06:14:43,153 INFO     29 [qwen-vl-text] coord item[63]: text=2.91, bbox=[424, 311, 457, 323]
2026-08-10 06:14:43,153 INFO     29 [qwen-vl-text] coord item[64]: text=6.2, bbox=[493, 311, 519, 323]
2026-08-10 06:14:43,153 INFO     29 [qwen-vl-text] coord item[65]: text=FEV1.0%(G), bbox=[51, 327, 132, 339]
2026-08-10 06:14:43,153 INFO     29 [qwen-vl-text] coord item[66]: text=%, bbox=[201, 327, 210, 339]
2026-08-10 06:14:43,153 INFO     29 [qwen-vl-text] coord item[67]: text=63.95, bbox=[218, 327, 259, 339]
2026-08-10 06:14:43,153 INFO     29 [qwen-vl-text] coord item[68]: text=73.89, bbox=[287, 327, 329, 339]
2026-08-10 06:14:43,153 INFO     29 [qwen-vl-text] coord item[69]: text=86.5, bbox=[356, 327, 390, 339]
2026-08-10 06:14:43,153 INFO     29 [qwen-vl-text] coord item[70]: text=73.42, bbox=[424, 327, 467, 339]
2026-08-10 06:14:43,153 INFO     29 [qwen-vl-text] coord item[71]: text=14.8, bbox=[493, 327, 526, 339]
2026-08-10 06:14:43,154 INFO     29 [qwen-vl-text] coord item[72]: text=FEV1.0%(T), bbox=[51, 342, 132, 354]
2026-08-10 06:14:43,154 INFO     29 [qwen-vl-text] coord item[73]: text=%, bbox=[201, 342, 210, 354]
2026-08-10 06:14:43,154 INFO     29 [qwen-vl-text] coord item[74]: text=63.95, bbox=[218, 342, 259, 354]
2026-08-10 06:14:43,154 INFO     29 [qwen-vl-text] coord item[75]: text=FEV1/VCpr, bbox=[51, 358, 127, 370]
2026-08-10 06:14:43,154 INFO     29 [qwen-vl-text] coord item[76]: text=%, bbox=[201, 358, 210, 370]
2026-08-10 06:14:43,154 INFO     29 [qwen-vl-text] coord item[77]: text=49.7, bbox=[218, 358, 250, 370]
2026-08-10 06:14:43,154 INFO     29 [qwen-vl-text] coord item[78]: text=58.5, bbox=[424, 358, 460, 370]
2026-08-10 06:14:43,154 INFO     29 [qwen-vl-text] coord item[79]: text=17.7, bbox=[493, 358, 526, 370]
2026-08-10 06:14:43,154 INFO     29 [qwen-vl-text] coord item[80]: text=MMF, bbox=[51, 373, 80, 385]
2026-08-10 06:14:43,154 INFO     29 [qwen-vl-text] coord item[81]: text=L/s, bbox=[185, 373, 210, 385]
2026-08-10 06:14:43,154 INFO     29 [qwen-vl-text] coord item[82]: text=1.17, bbox=[218, 373, 250, 385]
2026-08-10 06:14:43,154 INFO     29 [qwen-vl-text] coord item[83]: text=4.16, bbox=[287, 373, 320, 385]
2026-08-10 06:14:43,154 INFO     29 [qwen-vl-text] coord item[84]: text=28.1, bbox=[356, 373, 390, 385]
2026-08-10 06:14:43,154 INFO     29 [qwen-vl-text] coord item[85]: text=1.69, bbox=[424, 373, 457, 385]
2026-08-10 06:14:43,154 INFO     29 [qwen-vl-text] coord item[86]: text=44.4, bbox=[493, 373, 526, 385]
2026-08-10 06:14:43,154 INFO     29 [qwen-vl-text] coord item[87]: text=PEF, bbox=[51, 389, 80, 401]
2026-08-10 06:14:43,154 INFO     29 [qwen-vl-text] coord item[88]: text=L/s, bbox=[185, 389, 210, 401]
2026-08-10 06:14:43,154 INFO     29 [qwen-vl-text] coord item[89]: text=5.36, bbox=[218, 389, 250, 401]
2026-08-10 06:14:43,154 INFO     29 [qwen-vl-text] coord item[90]: text=8.7, bbox=[287, 389, 312, 401]
2026-08-10 06:14:43,154 INFO     29 [qwen-vl-text] coord item[91]: text=61.6, bbox=[356, 389, 390, 401]
2026-08-10 06:14:43,155 INFO     29 [qwen-vl-text] coord item[92]: text=4.37, bbox=[424, 389, 457, 401]
2026-08-10 06:14:43,155 INFO     29 [qwen-vl-text] coord item[93]: text=-18.5, bbox=[493, 389, 535, 401]
2026-08-10 06:14:43,155 INFO     29 [qwen-vl-text] coord item[94]: text=FEF25, bbox=[51, 404, 95, 416]
2026-08-10 06:14:43,155 INFO     29 [qwen-vl-text] coord item[95]: text=L/s, bbox=[185, 404, 210, 416]
2026-08-10 06:14:43,155 INFO     29 [qwen-vl-text] coord item[96]: text=2.3, bbox=[218, 404, 242, 416]
2026-08-10 06:14:43,155 INFO     29 [qwen-vl-text] coord item[97]: text=7.82, bbox=[287, 404, 320, 416]
2026-08-10 06:14:43,155 INFO     29 [qwen-vl-text] coord item[98]: text=29.4, bbox=[356, 404, 390, 416]
2026-08-10 06:14:43,155 INFO     29 [qwen-vl-text] coord item[99]: text=3.84, bbox=[424, 404, 457, 416]
2026-08-10 06:14:43,155 INFO     29 [qwen-vl-text] coord item[100]: text=67, bbox=[493, 404, 511, 416]
2026-08-10 06:14:43,155 INFO     29 [qwen-vl-text] coord item[101]: text=FEF50, bbox=[51, 419, 95, 431]
2026-08-10 06:14:43,155 INFO     29 [qwen-vl-text] coord item[102]: text=L/s, bbox=[185, 419, 210, 431]
2026-08-10 06:14:43,155 INFO     29 [qwen-vl-text] coord item[103]: text=1.45, bbox=[218, 419, 250, 431]
2026-08-10 06:14:43,155 INFO     29 [qwen-vl-text] coord item[104]: text=5.31, bbox=[287, 419, 320, 431]
2026-08-10 06:14:43,155 INFO     29 [qwen-vl-text] coord item[105]: text=27.3, bbox=[356, 419, 390, 431]
2026-08-10 06:14:43,156 INFO     29 [qwen-vl-text] coord item[106]: text=2.11, bbox=[424, 419, 457, 431]
2026-08-10 06:14:43,156 INFO     29 [qwen-vl-text] coord item[107]: text=45.5, bbox=[493, 419, 526, 431]
2026-08-10 06:14:43,156 INFO     29 [qwen-vl-text] coord item[108]: text=FEF75, bbox=[51, 435, 95, 447]
2026-08-10 06:14:43,156 INFO     29 [qwen-vl-text] coord item[109]: text=0.61, bbox=[218, 435, 250, 447]
2026-08-10 06:14:43,156 INFO     29 [qwen-vl-text] coord item[110]: text=2.39, bbox=[287, 435, 320, 447]
2026-08-10 06:14:43,156 INFO     29 [qwen-vl-text] coord item[111]: text=25.5, bbox=[356, 435, 390, 447]
2026-08-10 06:14:43,156 INFO     29 [qwen-vl-text] coord item[112]: text=0.7, bbox=[424, 435, 452, 447]
2026-08-10 06:14:43,156 INFO     29 [qwen-vl-text] coord item[113]: text=14.8, bbox=[493, 435, 526, 447]
2026-08-10 06:14:43,156 INFO     29 [qwen-vl-text] coord item[114]: text=FEF90, bbox=[51, 450, 95, 462]
2026-08-10 06:14:43,156 INFO     29 [qwen-vl-text] coord item[115]: text=0.23, bbox=[218, 450, 250, 462]
2026-08-10 06:14:43,156 INFO     29 [qwen-vl-text] coord item[116]: text=0.31, bbox=[424, 450, 457, 462]
2026-08-10 06:14:43,156 INFO     29 [qwen-vl-text] coord item[117]: text=34.8, bbox=[493, 450, 526, 462]
2026-08-10 06:14:43,156 INFO     29 [qwen-vl-text] coord item[118]: text=FEF50/FEF75, bbox=[51, 465, 145, 477]
2026-08-10 06:14:43,156 INFO     29 [qwen-vl-text] coord item[119]: text=2.38, bbox=[218, 465, 250, 477]
2026-08-10 06:14:43,156 INFO     29 [qwen-vl-text] coord item[120]: text=3.01, bbox=[424, 465, 457, 477]
2026-08-10 06:14:43,156 INFO     29 [qwen-vl-text] coord item[121]: text=26.5, bbox=[493, 465, 526, 477]
2026-08-10 06:14:43,156 INFO     29 [qwen-vl-text] coord item[122]: text=PEF/HT, bbox=[51, 480, 104, 492]
2026-08-10 06:14:43,156 INFO     29 [qwen-vl-text] coord item[123]: text=L/s/m, bbox=[171, 480, 210, 492]
2026-08-10 06:14:43,156 INFO     29 [qwen-vl-text] coord item[124]: text=3.15, bbox=[218, 480, 250, 492]
2026-08-10 06:14:43,156 INFO     29 [qwen-vl-text] coord item[125]: text=2.57, bbox=[424, 480, 457, 492]
2026-08-10 06:14:43,156 INFO     29 [qwen-vl-text] coord item[126]: text=-18.4, bbox=[493, 480, 535, 492]
2026-08-10 06:14:43,156 INFO     29 [qwen-vl-text] coord item[127]: text=FEF25/HT, bbox=[51, 496, 120, 508]
2026-08-10 06:14:43,157 INFO     29 [qwen-vl-text] coord item[128]: text=1.35, bbox=[218, 496, 250, 508]
2026-08-10 06:14:43,157 INFO     29 [qwen-vl-text] coord item[129]: text=67.4, bbox=[493, 496, 526, 508]
2026-08-10 06:14:43,157 INFO     29 [qwen-vl-text] coord item[130]: text=FEF75-85, bbox=[51, 511, 120, 523]
2026-08-10 06:14:43,157 INFO     29 [qwen-vl-text] coord item[131]: text=0.47, bbox=[218, 511, 250, 523]
2026-08-10 06:14:43,157 INFO     29 [qwen-vl-text] coord item[132]: text=FEF0.2-1.2, bbox=[51, 526, 136, 538]
2026-08-10 06:14:43,157 INFO     29 [qwen-vl-text] coord item[133]: text=OI, bbox=[51, 542, 69, 554]
2026-08-10 06:14:43,157 INFO     29 [qwen-vl-text] coord item[134]: text=ATI, bbox=[51, 557, 79, 569]
2026-08-10 06:14:43,157 INFO     29 [qwen-vl-text] coord item[135]: text=PEFTIME, bbox=[51, 572, 111, 584]
2026-08-10 06:14:43,157 INFO     29 [qwen-vl-text] coord item[136]: text=MVV, bbox=[119, 649, 145, 661]
2026-08-10 06:14:43,157 INFO     29 [qwen-vl-text] coord item[137]: text=诊断报告：, bbox=[71, 740, 141, 752]
2026-08-10 06:14:43,157 INFO     29 [qwen-vl-text] coord item[138]: text=检查技师：, bbox=[53, 870, 122, 882]
2026-08-10 06:14:43,157 INFO     29 [qwen-vl-text] coord item[139]: text=检查日期：2024-7-22, bbox=[751, 870, 906, 882]
2026-08-10 06:14:43,157 INFO     29 [qwen-vl-text] coord item[140]: text=FEV1% Restictive Normal, bbox=[747, 164, 907, 173]
2026-08-10 06:14:43,157 INFO     29 [qwen-vl-text] coord item[141]: text=SVC, bbox=[698, 180, 724, 190]
2026-08-10 06:14:43,158 INFO     29 [qwen-vl-text] coord item[142]: text=70, bbox=[766, 190, 780, 198]
2026-08-10 06:14:43,158 INFO     29 [qwen-vl-text] coord item[143]: text=Mixed, bbox=[794, 221, 826, 229]
2026-08-10 06:14:43,158 INFO     29 [qwen-vl-text] coord item[144]: text=Obstructive, bbox=[865, 220, 934, 229]
2026-08-10 06:14:43,158 INFO     29 [qwen-vl-text] coord item[145]: text=60, bbox=[856, 235, 870, 243]
2026-08-10 06:14:43,158 INFO     29 [qwen-vl-text] coord item[146]: text=%VC, bbox=[893, 235, 912, 243]
2026-08-10 06:14:43,158 INFO     29 [qwen-vl-text] coord item[147]: text=3, bbox=[580, 245, 594, 255]
2026-08-10 06:14:43,158 INFO     29 [qwen-vl-text] coord item[148]: text=0, bbox=[589, 319, 599, 328]
2026-08-10 06:14:43,158 INFO     29 [qwen-vl-text] coord item[149]: text=30, bbox=[680, 317, 698, 327]
2026-08-10 06:14:43,158 INFO     29 [qwen-vl-text] coord item[150]: text=50, bbox=[774, 317, 792, 327]
2026-08-10 06:14:43,158 INFO     29 [qwen-vl-text] coord item[151]: text=90 SEC, bbox=[854, 317, 907, 327]
2026-08-10 06:14:43,158 INFO     29 [qwen-vl-text] coord item[152]: text=12, bbox=[574, 365, 594, 375]
2026-08-10 06:14:43,158 INFO     29 [qwen-vl-text] coord item[153]: text=FVC, bbox=[696, 363, 724, 373]
2026-08-10 06:14:43,158 INFO     29 [qwen-vl-text] coord item[154]: text=8, bbox=[584, 406, 594, 416]
2026-08-10 06:14:43,158 INFO     29 [qwen-vl-text] coord item[155]: text=4, bbox=[584, 447, 594, 457]
2026-08-10 06:14:43,158 INFO     29 [qwen-vl-text] coord item[156]: text=0, bbox=[584, 488, 594, 498]
2026-08-10 06:14:43,158 INFO     29 [qwen-vl-text] coord item[157]: text=8 L, bbox=[865, 494, 895, 505]
2026-08-10 06:14:43,158 INFO     29 [qwen-vl-text] coord item[158]: text=-4, bbox=[574, 529, 594, 539]
2026-08-10 06:14:43,158 INFO     29 [qwen-vl-text] coord item[159]: text=-8, bbox=[574, 570, 594, 580]
2026-08-10 06:14:43,158 INFO     29 [qwen-vl-text] coord item[160]: text=-12, bbox=[564, 611, 594, 621]
2026-08-10 06:14:43,158 INFO     29 [qwen-vl-text] coord item[161]: text=4L, bbox=[574, 690, 594, 700]
2026-08-10 06:14:43,158 INFO     29 [qwen-vl-text] coord item[162]: text=MVV, bbox=[698, 690, 724, 700]
2026-08-10 06:14:43,158 INFO     29 [qwen-vl-text] coord item[163]: text=2, bbox=[584, 752, 594, 762]
2026-08-10 06:14:43,158 INFO     29 [qwen-vl-text] coord item[164]: text=0, bbox=[593, 826, 602, 836]
2026-08-10 06:14:43,158 INFO     29 [qwen-vl-text] coord item[165]: text=5, bbox=[688, 825, 698, 835]
2026-08-10 06:14:43,158 INFO     29 [qwen-vl-text] coord item[166]: text=10, bbox=[780, 825, 798, 835]
2026-08-10 06:14:43,159 INFO     29 [qwen-vl-text] coord item[167]: text=15 SEC, bbox=[858, 825, 912, 835]
2026-08-10 06:14:43,165 INFO     29 [qwen-vl-text] page=1 — 220/223 coords, api_time=67.9s
2026-08-10 06:14:43,166 INFO     29 [qwen-vl-text] new_positions (223):
[[1, 194.565, 364.73499999999996, 43.784, 59.782], [1, 38.08, 86.27499999999999, 75.78, 85.884], [1, 134.47, 158.26999999999998, 75.78, 85.884], [1, 233.23999999999998, 271.91499999999996, 75.78, 85.884], [1, 330.22499999999997, 368.9, 74.096, 84.2], [1, 428.995, 487.30499999999995, 74.096, 84.2], [1, 38.08, 91.035, 92.61999999999999, 102.72399999999999], [1, 134.47, 199.325, 92.61999999999999, 102.72399999999999], [1, 233.23999999999998, 292.145, 91.77799999999999, 101.88199999999999], [1, 330.22499999999997, 383.775, 91.77799999999999, 101.88199999999999], [1, 428.995, 516.4599999999999, 90.93599999999999, 101.03999999999999], [1, 38.08, 60.69, 109.46, 119.564], [1, 134.47, 158.26999999999998, 109.46, 119.564], [1, 233.23999999999998, 301.07, 109.46, 119.564], [1, 330.22499999999997, 387.94, 108.618, 118.722], [1, 428.995, 451.60499999999996, 108.618, 118.722], [1, 69.615, 86.27499999999999, 131.352, 141.456], [1, 137.445, 157.67499999999998, 131.352, 141.456], [1, 179.69, 199.92, 131.352, 141.456], [1, 217.17499999999998, 242.76, 131.352, 141.456], [1, 261.8, 281.435, 131.352, 141.456], [1, 298.09499999999997, 326.655, 131.352, 141.456], [1, 30.345, 41.055, 143.982, 154.08599999999998], [1, 119.595, 124.94999999999999, 143.982, 154.08599999999998], [1, 129.71, 148.75, 143.982, 154.08599999999998], [1, 170.765, 190.39999999999998, 143.982, 154.08599999999998], [1, 211.82, 232.04999999999998, 143.982, 154.08599999999998], [1, 30.345, 41.055, 157.454, 167.558], [1, 119.595, 124.94999999999999, 157.454, 167.558], [1, 30.345, 39.864999999999995, 170.084, 180.188], [1, 119.595, 124.94999999999999, 170.084, 180.188], [1, 30.345, 45.815, 183.55599999999998, 193.66], [1, 119.595, 124.94999999999999, 183.55599999999998, 193.66], [1, 30.345, 45.815, 197.028, 207.132], [1, 119.595, 124.94999999999999, 197.028, 207.132], [1, 69.615, 86.27499999999999, 209.658, 219.762], [1, 137.445, 157.67499999999998, 209.658, 219.762], [1, 179.69, 199.92, 209.658, 219.762], [1, 217.17499999999998, 242.76, 209.658, 219.762], [1, 261.8, 281.435, 209.658, 219.762], [1, 298.09499999999997, 326.655, 209.658, 219.762], [1, 30.345, 45.815, 223.13, 233.23399999999998], [1, 119.595, 124.94999999999999, 223.13, 233.23399999999998], [1, 129.71, 148.75, 223.13, 233.23399999999998], [1, 170.765, 190.39999999999998, 223.13, 233.23399999999998], [1, 211.82, 232.04999999999998, 223.13, 233.23399999999998], [1, 252.28, 271.91499999999996, 223.13, 233.23399999999998], [1, 293.335, 308.805, 223.13, 233.23399999999998], [1, 30.345, 60.69, 235.76, 245.864], [1, 119.595, 124.94999999999999, 235.76, 245.864], [1, 129.71, 148.75, 235.76, 245.864], [1, 252.28, 271.91499999999996, 235.76, 245.864], [1, 293.335, 312.96999999999997, 235.76, 245.864], [1, 30.345, 60.69, 249.232, 259.336], [1, 119.595, 124.94999999999999, 249.232, 259.336], [1, 129.71, 148.75, 249.232, 259.336], [1, 170.765, 190.39999999999998, 249.232, 259.336], [1, 211.82, 232.04999999999998, 249.232, 259.336], [1, 252.28, 271.91499999999996, 249.232, 259.336], [1, 293.335, 312.96999999999997, 249.232, 259.336], [1, 30.345, 60.69, 261.86199999999997, 271.966], [1, 119.595, 124.94999999999999, 261.86199999999997, 271.966], [1, 129.71, 148.75, 261.86199999999997, 271.966], [1, 252.28, 271.91499999999996, 261.86199999999997, 271.966], [1, 293.335, 308.805, 261.86199999999997, 271.966], [1, 30.345, 78.53999999999999, 275.334, 285.438], [1, 119.595, 124.94999999999999, 275.334, 285.438], [1, 129.71, 154.105, 275.334, 285.438], [1, 170.765, 195.755, 275.334, 285.438], [1, 211.82, 232.04999999999998, 275.334, 285.438], [1, 252.28, 277.865, 275.334, 285.438], [1, 293.335, 312.96999999999997, 275.334, 285.438], [1, 30.345, 78.53999999999999, 287.964, 298.068], [1, 119.595, 124.94999999999999, 287.964, 298.068], [1, 129.71, 154.105, 287.964, 298.068], [1, 30.345, 75.565, 301.436, 311.53999999999996], [1, 119.595, 124.94999999999999, 301.436, 311.53999999999996], [1, 129.71, 148.75, 301.436, 311.53999999999996], [1, 252.28, 273.7, 301.436, 311.53999999999996], [1, 293.335, 312.96999999999997, 301.436, 311.53999999999996], [1, 30.345, 47.599999999999994, 314.066, 324.17], [1, 110.07499999999999, 124.94999999999999, 314.066, 324.17], [1, 129.71, 148.75, 314.066, 324.17], [1, 170.765, 190.39999999999998, 314.066, 324.17], [1, 211.82, 232.04999999999998, 314.066, 324.17], [1, 252.28, 271.91499999999996, 314.066, 324.17], [1, 293.335, 312.96999999999997, 314.066, 324.17], [1, 30.345, 47.599999999999994, 327.538, 337.642], [1, 110.07499999999999, 124.94999999999999, 327.538, 337.642], [1, 129.71, 148.75, 327.538, 337.642], [1, 170.765, 185.64, 327.538, 337.642], [1, 211.82, 232.04999999999998, 327.538, 337.642], [1, 252.28, 271.91499999999996, 327.538, 337.642], [1, 293.335, 318.325, 327.538, 337.642], [1, 30.345, 56.525, 340.168, 350.272], [1, 110.07499999999999, 124.94999999999999, 340.168, 350.272], [1, 129.71, 143.98999999999998, 340.168, 350.272], [1, 170.765, 190.39999999999998, 340.168, 350.272], [1, 211.82, 232.04999999999998, 340.168, 350.272], [1, 252.28, 271.91499999999996, 340.168, 350.272], [1, 293.335, 304.04499999999996, 340.168, 350.272], [1, 30.345, 56.525, 352.798, 362.902], [1, 110.07499999999999, 124.94999999999999, 352.798, 362.902], [1, 129.71, 148.75, 352.798, 362.902], [1, 170.765, 190.39999999999998, 352.798, 362.902], [1, 211.82, 232.04999999999998, 352.798, 362.902], [1, 252.28, 271.91499999999996, 352.798, 362.902], [1, 293.335, 312.96999999999997, 352.798, 362.902], [1, 30.345, 56.525, 366.27, 376.37399999999997], [1, 129.71, 148.75, 366.27, 376.37399999999997], [1, 170.765, 190.39999999999998, 366.27, 376.37399999999997], [1, 211.82, 232.04999999999998, 366.27, 376.37399999999997], [1, 252.28, 268.94, 366.27, 376.37399999999997], [1, 293.335, 312.96999999999997, 366.27, 376.37399999999997], [1, 30.345, 56.525, 378.9, 389.00399999999996], [1, 129.71, 148.75, 378.9, 389.00399999999996], [1, 252.28, 271.91499999999996, 378.9, 389.00399999999996], [1, 293.335, 312.96999999999997, 378.9, 389.00399999999996], [1, 30.345, 86.27499999999999, 391.53, 401.63399999999996], [1, 129.71, 148.75, 391.53, 401.63399999999996], [1, 252.28, 271.91499999999996, 391.53, 401.63399999999996], [1, 293.335, 312.96999999999997, 391.53, 401.63399999999996], [1, 30.345, 61.879999999999995, 404.15999999999997, 414.264], [1, 101.74499999999999, 124.94999999999999, 404.15999999999997, 414.264], [1, 129.71, 148.75, 404.15999999999997, 414.264], [1, 252.28, 271.91499999999996, 404.15999999999997, 414.264], [1, 293.335, 318.325, 404.15999999999997, 414.264], [1, 30.345, 71.39999999999999, 417.632, 427.736], [1, 129.71, 148.75, 417.632, 427.736], [1, 293.335, 312.96999999999997, 417.632, 427.736], [1, 30.345, 71.39999999999999, 430.262, 440.366], [1, 129.71, 148.75, 430.262, 440.366], [1, 30.345, 80.92, 442.892, 452.996], [1, 30.345, 41.055, 456.364, 466.46799999999996], [1, 30.345, 47.004999999999995, 468.99399999999997, 479.09799999999996], [1, 30.345, 66.045, 481.62399999999997, 491.728], [1, 70.80499999999999, 86.27499999999999, 546.458, 556.562], [1, 42.245, 83.895, 623.0799999999999, 633.184], [1, 31.535, 72.59, 732.54, 742.644], [1, 446.84499999999997, 539.0699999999999, 732.54, 742.644], [1, 444.465, 539.665, 138.088, 145.666], [1, 415.31, 430.78, 151.56, 159.98], [1, 455.77, 464.09999999999997, 159.98, 166.716], [1, 472.43, 491.46999999999997, 186.082, 192.81799999999998], [1, 514.675, 555.73, 185.23999999999998, 192.81799999999998], [1, 509.32, 517.65, 197.87, 204.606], [1, 531.3349999999999, 542.64, 197.87, 204.606], [1, 345.09999999999997, 353.43, 206.29, 214.70999999999998], [1, 350.455, 356.405, 268.598, 276.176], [1, 404.59999999999997, 415.31, 266.914, 275.334], [1, 460.53, 471.23999999999995, 266.914, 275.334], [1, 508.13, 539.665, 266.914, 275.334], [1, 341.53, 353.43, 307.33, 315.75], [1, 414.12, 430.78, 305.646, 314.066], [1, 347.47999999999996, 353.43, 341.852, 350.272], [1, 347.47999999999996, 353.43, 376.37399999999997, 384.794], [1, 347.47999999999996, 353.43, 410.89599999999996, 419.316], [1, 514.675, 532.525, 415.948, 425.21], [1, 341.53, 353.43, 445.418, 453.83799999999997], [1, 341.53, 353.43, 479.94, 488.35999999999996], [1, 335.58, 353.43, 514.462, 522.882], [1, 341.53, 353.43, 580.98, 589.4], [1, 415.31, 430.78, 580.98, 589.4], [1, 347.47999999999996, 353.43, 633.184, 641.6039999999999], [1, 352.835, 358.19, 695.492, 703.9119999999999], [1, 409.35999999999996, 415.31, 694.65, 703.0699999999999], [1, 464.09999999999997, 474.81, 694.65, 703.0699999999999], [1, 510.51, 542.64, 694.65, 703.0699999999999], [1, 293.335, 312.96999999999997, 301.436, 311.53999999999996], [1, 129.71, 148.75, 223.13, 233.23399999999998], [1, 170.765, 195.755, 275.334, 285.438], [1, 414.12, 430.78, 305.646, 314.066], [1, 119.595, 124.94999999999999, 261.86199999999997, 271.966], [1, 129.71, 148.75, 223.13, 233.23399999999998], [1, 252.28, 277.865, 275.334, 285.438], [1, 293.335, 312.96999999999997, 301.436, 311.53999999999996], [1, 415.31, 430.78, 580.98, 589.4], [1, 137.445, 157.67499999999998, 209.658, 219.762], [1, 179.69, 199.92, 209.658, 219.762], [1, 217.17499999999998, 242.76, 209.658, 219.762], [1, 261.8, 281.435, 209.658, 219.762], [1, 298.09499999999997, 326.655, 209.658, 219.762], [1, 415.31, 430.78, 580.98, 589.4], [1, 101.74499999999999, 124.94999999999999, 404.15999999999997, 414.264], [1, 129.71, 148.75, 235.76, 245.864], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 30.345, 39.864999999999995, 170.084, 180.188], [1, 119.595, 124.94999999999999, 261.86199999999997, 271.966], [1, 0, 0, 0, 0], [1, 101.74499999999999, 124.94999999999999, 404.15999999999997, 414.264], [1, 30.345, 47.004999999999995, 468.99399999999997, 479.09799999999996], [1, 42.245, 83.895, 623.0799999999999, 633.184], [1, 31.535, 72.59, 732.54, 742.644], [1, 446.84499999999997, 539.0699999999999, 732.54, 742.644], [1, 444.465, 539.665, 138.088, 145.666], [1, 415.31, 430.78, 151.56, 159.98], [1, 455.77, 464.09999999999997, 159.98, 166.716], [1, 472.43, 491.46999999999997, 186.082, 192.81799999999998], [1, 514.675, 555.73, 185.23999999999998, 192.81799999999998], [1, 509.32, 517.65, 197.87, 204.606], [1, 531.3349999999999, 542.64, 197.87, 204.606], [1, 345.09999999999997, 353.43, 206.29, 214.70999999999998], [1, 352.835, 358.19, 695.492, 703.9119999999999], [1, 404.59999999999997, 415.31, 266.914, 275.334], [1, 460.53, 471.23999999999995, 266.914, 275.334], [1, 508.13, 539.665, 266.914, 275.334], [1, 341.53, 353.43, 307.33, 315.75], [1, 414.12, 430.78, 305.646, 314.066], [1, 347.47999999999996, 353.43, 341.852, 350.272], [1, 347.47999999999996, 353.43, 376.37399999999997, 384.794], [1, 352.835, 358.19, 695.492, 703.9119999999999], [1, 514.675, 532.525, 415.948, 425.21], [1, 341.53, 353.43, 445.418, 453.83799999999997], [1, 341.53, 353.43, 479.94, 488.35999999999996], [1, 335.58, 353.43, 514.462, 522.882], [1, 341.53, 353.43, 580.98, 589.4], [1, 415.31, 430.78, 580.98, 589.4], [1, 347.47999999999996, 353.43, 633.184, 641.6039999999999], [1, 352.835, 358.19, 695.492, 703.9119999999999], [1, 409.35999999999996, 415.31, 694.65, 703.0699999999999], [1, 464.09999999999997, 474.81, 694.65, 703.0699999999999], [1, 510.51, 542.64, 694.65, 703.0699999999999]]
2026-08-10 06:14:43,166 INFO     29 [qwen-vl-text] ═══ DONE ═══ 223 positions, pages=1, time=101.2s
2026-08-10 06:14:43,439 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 06:14:43,440 INFO     29 [Trace] task=4115cdf4 | doc=GWHU-48岁-男(2).pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items, types={'ExaminationReport': 1}", "html": "", "json": "248 items", "markdown": "", "text": "", "name": "GWHU-48岁-男(2).pdf", "output_format": "chunks", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_Examination": "1 items, types={'ExaminationReport': 1}", "route_summary": "{\"chunks_Clinical\": 1, \"chunks_Examination\": 1}"}
2026-08-10 06:14:43,440 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 06:14:43,442 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T06:14:43.440+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 1, "failed": 0, "current": {"801b5176947e11f182aec5d26bc6c4ae": {"id": "801b5176947e11f182aec5d26bc6c4ae", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786340646131, "task_type": "dataflow", "root_trace_id": "97b84aa3d1154f6db808c154432c5554", "root_traceparent": "00-97b84aa3d1154f6db808c154432c5554-dd9503e7c4e14a5d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "4115cdf4948211f1bd9827cf206dfa2d": {"id": "4115cdf4948211f1bd9827cf206dfa2d", "doc_id": "40948096948211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "GWHU-48\u5c81-\u7537(2).pdf", "type": "pdf", "location": "GWHU-48\u5c81-\u7537(2).pdf", "size": 1182408, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786342258386, "task_type": "dataflow", "root_trace_id": "0d4f1377f2e04befb139f86a697fd302", "root_traceparent": "00-0d4f1377f2e04befb139f86a697fd302-ea5641fe487f4324-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 06:14:43,445 INFO     29 [ChunkMerger] Merged 2 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1} (filtered 6 noise chunks)
2026-08-10 06:14:43,463 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-10 06:14:43,463 INFO     29 [Trace] task=4115cdf4 | doc=GWHU-48岁-男(2).pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}", "name": "GWHU-48岁-男(2).pdf"}
2026-08-10 06:14:43,463 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 06:14:43,558 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786342278628, 'update_date': datetime.datetime(2026, 8, 10, 6, 11, 18), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 777092, 'status': '1'}
2026-08-10 06:14:43,815 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=初诊病历
姓名：
病历号：00125638
科别：呼吸与危重症医学二科
门诊
性别：男
身份证号：
出生日期：1975-12-14
年龄：49岁
就诊序号：113598
就诊日期：2025-05-24 10:38
民族：民族
联系电话：
医保费别：自费
详细地址：地址
主诉：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。
现病史：咳嗽咳痰胸闷10年,无发热胸痛。。。。。。。。。。。。。。。。。。
既往史：无
过敏史：{否认食物、药物过敏史}。
体格检查：{体温、脉搏、呼吸、血压未查}。
辅助检查：无
初步诊断：1、支气管哮喘
处理意见：对症
接诊医生：李志军
签名时间：2025年05月24日10时38分
---
鹤煤总医院肺功能报告单
ID号：4000
姓名：
性别：男
年龄：48
身高：170 cm
体重：95 kg
B.S.A：2.06m²
温度(℃)：22
湿度(%)：50
气压(mmHg)：1013.3
科室：
病区：
预测公式：亚洲
医生：李志军
备注：
SVC
实测
预测
%预测
BD后
改进率
VC
L
2.94
3.78
77.8
IC
L
TV
L
ERV
L
IRV
L
FVC
实测
预测
%预测
BD后
改进率
FVC
L
2.94
3.78
77.8
3.01
2.4
FEV0.5
L
1.26
1.62
28.6
FEV1.0
L
1.88
3.26
57.7
2.21
17.6
FEV3.0
L
2.74
2.91
6.2
FEV1.0%(G)
%
63.95
73.89
86.5
73.42
14.8
FEV1.0%(T)
%
63.95
FEV1/VCpr
%
49.7
58.5
17.7
MMF
L/s
1.17
4.16
28.1
1.69
44.4
PEF
L/s
5.36
8.7
61.6
4.37
-18.5
FEF25
L/s
2.3
7.82
29.4
3.84
67
FEF50
L/s
1.45
5.31
27.3
2.11
45.5
FEF75
L/s
0.61
2.39
25.5
0.7
14.8
FEF90
L/s
0.23
0.31
34.8
FEF50/FEF75
2.38
3.01
26.5
PEF/HT
L/s/m
3.15
2.57
-18.4
FEF25/HT
L/s/m
1.35
2.26
67.4
FEF75-85
L/s
0.47
0.53
12.8
FEF0.2-1.2
L/s
2.37
3.61
52.3
OI
L/s
5.21
2.19
-58
ATI
%
PEFTIME
Sec
0.05
0.08
60
FET
Sec
4.46
3.72
-16.6
Vextrap
L
0.05
0.09
80
Extrap V
%
1.7
2.99
75.9
FIVC
L
2.93
3.42
16.7
MVV
实测
预测
%预测
BD后
改进率
MVV
L/min
126.6
RR
C/min
TV
L
MVV/BSA
L/min/m²
AVI
诊断报告：
检查技师：
检查日期：2024-7-22
FEV1% Restictive Normal
SVC
70
Mixed
Obstructive
60
%VC
3
0
30
50
90 SEC
12
FVC
8
4
0
8 L
-4
-8
-12
4L
MVV
2
0
5
10
15 SEC
2026-08-10 06:14:44,094 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-10 06:14:44,094 INFO     29 [Trace] task=4115cdf4 | doc=GWHU-48岁-男(2).pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "2 items, types={'OutpatientRecord': 1, 'ExaminationReport': 1}", "name": "GWHU-48岁-男(2).pdf", "embedding_token_consumption": 1198}
2026-08-10 06:14:44,094 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-10 06:14:44,292 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-10 06:14:44,292 INFO     29 [Trace] task=4115cdf4 | doc=GWHU-48岁-男(2).pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":2,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 06:14:44,296 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:14:44,297 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 06:14:44,304 INFO     29 set_progress(4115cdf4948211f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 06:14:44 [DOC Engine]:
Start to index...
2026-08-10 06:14:44,358 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.048s]
2026-08-10 06:14:44,368 INFO     29 set_progress(4115cdf4948211f1bd9827cf206dfa2d), progress: 0.8500000000000001, progress_msg: 
2026-08-10 06:14:44,387 INFO     29 set_progress(4115cdf4948211f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 06:14:44 Indexing done (0.08s). Task done (205.53s)
2026-08-10 06:14:44,397 INFO     29 [Done], chunks(2), token(1198), elapsed:205.53
2026-08-10 06:14:44,482 INFO     29 handle_task done for task {"id": "4115cdf4948211f1bd9827cf206dfa2d", "doc_id": "40948096948211f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "GWHU-48\u5c81-\u7537(2).pdf", "type": "pdf", "location": "GWHU-48\u5c81-\u7537(2).pdf", "size": 1182408, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786342258386, "task_type": "dataflow", "root_trace_id": "0d4f1377f2e04befb139f86a697fd302", "root_traceparent": "00-0d4f1377f2e04befb139f86a697fd302-ea5641fe487f4324-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
