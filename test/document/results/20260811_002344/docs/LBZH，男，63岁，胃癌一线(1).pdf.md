# 基准结果：LBZH，男，63岁，胃癌一线(1).pdf

## 基本信息

- 文件：`LBZH，男，63岁，胃癌一线(1).pdf`
- 大小：27790.0 KB
- PDF 总页数：20
- doc_id：`dbef275894d711f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-11T00:23:44  完成时间：2026-08-11T00:38:46  耗时：901.4s
- progress_msg：`16:38:39 Indexing done (0.25s). Task done (836.32s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 0ec1ba55 | 2 | 8-9 | 双侧颈部4区探及数个淋巴结，大者分别约1.7cm×1.2cm（左）、1.6cm× |
| 2 | 3ad7d086 | 3 | 9-11 | 手术过程 阳性 阳性 报告 申请 申请 申请 手术申请单 报告 报告 报告 浏览 |
| 3 | 3ed8f632 | 1 | 11-11 | 863 已F 76 已F 病例库 病理会诊 姓名 性别 男 住院号 年龄 61岁 |
| 4 | bb8ae086 | 1 | 12-12 | 姓名 性别男 年龄01岁 床号 送检单位本院 送检科室 收到日期2024-11- |
| 5 | 0d54c9ac | 5 | 13-17 | 29.11.11.73 临时用户 福建省肿瘤医院病历记录 姓名 入院记录 姓 出 |
| 6 | 8e88bb8c | 3 | 18-20 | 2026-03-24 15:16 于2024-09-02以'进行性吞咽困难2个月 |
| 7 | c8735e1c | 6 | 1-7 | <table><tr><td>白蛋白</td><td>ALB</td><td>3 |

- chunks 总数：7
- 各 chunk 页数合计（含跨页重复）：21
- 页码并集：`[1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]`
- 覆盖页数：19 / 20；缺失页：`[4]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：❌ 未完全覆盖：覆盖 19/20 页，缺失 [4]，超范围 []**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 1 | 0 | 1 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 1 | 1 | 1 | encounter_date, dm_admission_time, cc_text, department | **OK** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 4 | 4 | 4 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 1 | 0 | 1 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"LabReport": 1, "ExaminationReport": 4, "AdmissionRecord": 1, "OutpatientRecord": 1}`
- ChunkMerger：`{"found": true, "merged": 7, "sources": 9, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 4, "Extractor:Progress": 1}, "filtered_noise": 5}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 16:38:37,323 INFO     29 [ChunkMerger] Merged 7 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 16:23:49,552 INFO     29 handle_task begin for task {"id": "dca6cdea94d711f1bd9827cf206dfa2d", "doc_id": "dbef275894d711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "size": 28457006, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786379026603, "task_type": "dataflow", "root_trace_id": "00f6a24fb6bd4742ba80c2030b932c44", "root_traceparent": "00-00f6a24fb6bd4742ba80c2030b932c44-fbfb6d98b4675b32-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 16:23:49,790 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.002s]
2026-08-10 16:23:49,906 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 16:23:49,937 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:23:49,937 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 16:23:49,937 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 16:23:49,942 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 16:23:49,942 INFO     29 ============================================================
2026-08-10 16:23:49,942 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 16:23:49,942 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 16:23:49,942 INFO     29 ============================================================
2026-08-10 16:23:49,942 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 16:23:49,942 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 16:23:49,944 INFO     29 No torch found.
2026-08-10 16:23:53,126 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:23:53.070+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 74, "failed": 0, "current": {"dca6cdea94d711f1bd9827cf206dfa2d": {"id": "dca6cdea94d711f1bd9827cf206dfa2d", "doc_id": "dbef275894d711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "size": 28457006, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786379026603, "task_type": "dataflow", "root_trace_id": "00f6a24fb6bd4742ba80c2030b932c44", "root_traceparent": "00-00f6a24fb6bd4742ba80c2030b932c44-fbfb6d98b4675b32-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:23:59,740 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=20
2026-08-10 16:24:02,420 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7702830, prompt_len=764
2026-08-10 16:24:11,129 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-23"
}
```
2026-08-10 16:24:11,131 INFO     29 [qwen-vl-parser] page=1 classify=table report_date=2026-03-23
2026-08-10 16:24:11,157 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7702830, prompt_len=756
2026-08-10 16:24:21,409 INFO     29 [qwen-vl-parser] table API response (len=2015):
\begin{tabular}{ccccccccccc}
\hline
类型 & 检查日期 & 检验项目 & 分组 & 样本 & 中文名称 & 英文名称 & 结果 & 定性 & 参考值 & 单位 \\
\hline
门诊 & 2026-03-23 18:27 & L,ALT,AST,GGT,ALI & G001 & 血清 & *白蛋白 & ALB & 38.4 & $\downarrow$ & 40.0-55.0 & g/L \\
门诊 & 2026-03-23 14:29 & TSH,FT3,FT4 & G001 & 血清 & 总胆红素 & TBIL & 9.3 & & 5.0-21.0 & umol/L \\
门诊 & 2026-03-23 12:47 & PCT,CRP,NT-proBNP & G002 & 血清 & 直接胆红素 & DBIL & 1.9 & & 0-8.0 & umol/L \\
门诊 & 2026-03-23 12:49 & 肌钙蛋白T & G002 & 血清 & 间接胆红素 & IBIL & 7.4 & & 0-20.0 & umol/L \\
门诊 & 2026-03-23 12:04 & 血常规(五分类) & G004 & 全血 & *谷丙转氨酶 & ALT & 80 & $\uparrow$ & 9-50 & U/L \\
门诊 & 2026-03-23 12:43 & PT,APTT & G029 & 血浆 & *谷草转氨酶 & AST & 58 & $\uparrow$ & 5-40 & U/L \\
\multicolumn{11}{c}{共6份报告} \\
\multicolumn{11}{c}{ALT/AST} \\
\multicolumn{11}{c}{ALT/AST} \\
\multicolumn{11}{c}{1.38} \\
\multicolumn{11}{c}{*γ谷氨酰转肽酶} \\
\multicolumn{11}{c}{GGT} \\
\multicolumn{11}{c}{50} \\
\multicolumn{11}{c}{10-60} \\
\multicolumn{11}{c}{U/L} \\
\multicolumn{11}{c}{*碱性磷酸酶} \\
\multicolumn{11}{c}{ALP} \\
\multicolumn{11}{c}{93} \\
\multicolumn{11}{c}{45-125} \\
\multicolumn{11}{c}{U/L} \\
\multicolumn{11}{c}{*乳酸脱氢酶} \\
\multicolumn{11}{c}{LDH} \\
\multicolumn{11}{c}{208} \\
\multicolumn{11}{c}{120-250} \\
\multicolumn{11}{c}{U/L} \\
\multicolumn{11}{c}{*尿素} \\
\multicolumn{11}{c}{Urea} \\
\multicolumn{11}{c}{3.12} \\
\multicolumn{11}{c}{$\downarrow$} \\
\multicolumn{11}{c}{3.6-9.5} \\
\multicolumn{11}{c}{mmol/L} \\
\multicolumn{11}{c}{肌酐} \\
\multicolumn{11}{c}{Cr} \\
\multicolumn{11}{c}{62} \\
\multicolumn{11}{c}{57-111} \\
\multicolumn{11}{c}{umol/L} \\
\multicolumn{11}{c}{尿素/肌酐} \\
\multicolumn{11}{c}{B/C} \\
\multicolumn{11}{c}{0.050} \\
\multicolumn{11}{c}{*尿酸} \\
\multicolumn{11}{c}{UA} \\
\multicolumn{11}{c}{354} \\
\multicolumn{11}{c}{208.3-428.4} \\
\multicolumn{11}{c}{umol/L} \\
\multicolumn{11}{c}{*葡萄糖} \\
\multicolumn{11}{c}{Glu} \\
\multicolumn{11}{c}{6.39} \\
\multicolumn{11}{c}{$\uparrow$} \\
\multicolumn{11}{c}{3.70-6.10} \\
\multicolumn{11}{c}{mmol/L} \\
\hline
\end{tabular}
2026-08-10 16:24:21,416 INFO     29 [qwen-vl-parser] page=1 table: 57 LaTeX lines (bbox 0-56)
2026-08-10 16:24:21,416 INFO     29 [qwen-vl-parser] page=1 table: 57 sections
2026-08-10 16:24:24,281 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7262551, prompt_len=764
2026-08-10 16:24:25,010 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:24:25.008+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 74, "failed": 0, "current": {"dca6cdea94d711f1bd9827cf206dfa2d": {"id": "dca6cdea94d711f1bd9827cf206dfa2d", "doc_id": "dbef275894d711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "size": 28457006, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786379026603, "task_type": "dataflow", "root_trace_id": "00f6a24fb6bd4742ba80c2030b932c44", "root_traceparent": "00-00f6a24fb6bd4742ba80c2030b932c44-fbfb6d98b4675b32-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:24:34,657 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-23"
}
```
2026-08-10 16:24:34,659 INFO     29 [qwen-vl-parser] page=2 classify=table report_date=2026-03-23
2026-08-10 16:24:34,687 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7262551, prompt_len=756
2026-08-10 16:24:39,530 INFO     29 [qwen-vl-parser] table API response (len=648):
\begin{tabular}{ccccccccccc}
\hline
类型 & 检查日期 & 检验项目 & 分组 & 样本 & 中文名称 & 英文名称 & 结果 & 定性 & 参考值 & 单位 \\
\hline
门诊 & 2026-03-23 18:27 & L,ALT,AST,GGT,ALI & G001 & 血清 & *游离三碘甲状原氨酸 & FT3 & 5.55 & & 3.53-7.37 & pmol/L \\
门诊 & 2026-03-23 14:29 & TSH,FT3,FT4 & G001 & 血清 & *游离甲状腺素 & FT4 & 11.03 & & 7.98-19.24 & pmol/L \\
门诊 & 2026-03-23 12:47 & PCT,CRP,NT-proBNP & G002 & 血清 & *促甲状腺刺激激素 & s-TSH & 1.397 & & 0.340-5.600 & mIU/L \\
门诊 & 2026-03-23 12:49 & 肌钙蛋白T & G002 & 血清 & & & & & & \\
门诊 & 2026-03-23 12:04 & 血常规(五分类) & G004 & 全血 & & & & & & \\
门诊 & 2026-03-23 12:43 & PT,APTT & G029 & 血浆 & & & & & & \\
\multicolumn{11}{c}{共6份报告} \\
\hline
\end{tabular}
2026-08-10 16:24:39,533 INFO     29 [qwen-vl-parser] page=2 table: 14 LaTeX lines (bbox 57-70)
2026-08-10 16:24:39,533 INFO     29 [qwen-vl-parser] page=2 table: 14 sections
2026-08-10 16:24:42,704 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=8639157, prompt_len=764
2026-08-10 16:24:51,585 INFO     29 [qwen-vl-parser] classify API response (len=50):
```json
{"type": "table", "report_date": null}
```
2026-08-10 16:24:51,587 INFO     29 [qwen-vl-parser] page=3 classify=table report_date=None
2026-08-10 16:24:51,615 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=8639157, prompt_len=756
2026-08-10 16:24:55,111 INFO     29 [qwen-vl-parser] table API response (len=443):
\begin{tabular}{ccccccccc}
\hline
检验项目 & 分组 & 样本 & 中文名称 & 英文名称 & 结果 & 定性 & 参考值 & 单位 \\
\hline
ALT, AST, GGT, ALI & G001 & 血清 & N端-B型钠尿肽前体 & NT-proBNP & 191.85 & & <210.64 & ng/L \\
TSH, FT3, FT4 & G001 & 血清 & C反应蛋白 & CRP & 1.15 & & <5.0 & mg/L \\
T, CRP, NT-proBNP & G002 & 血清 & 降钙素原 & PCT & 0.04 & & <0.05 & ng/mL \\
肌钙蛋白T & G002 & 血清 & & & & & & \\
血常规(五分类) & G004 & 全血 & & & & & & \\
PT, APTT & G029 & 血浆 & & & & & & \\
\hline
\end{tabular}
2026-08-10 16:24:55,113 INFO     29 [qwen-vl-parser] page=3 table: 12 LaTeX lines (bbox 71-82)
2026-08-10 16:24:55,114 INFO     29 [qwen-vl-parser] page=3 table: 12 sections
2026-08-10 16:24:56,922 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:24:56.921+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 74, "failed": 0, "current": {"dca6cdea94d711f1bd9827cf206dfa2d": {"id": "dca6cdea94d711f1bd9827cf206dfa2d", "doc_id": "dbef275894d711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "size": 28457006, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786379026603, "task_type": "dataflow", "root_trace_id": "00f6a24fb6bd4742ba80c2030b932c44", "root_traceparent": "00-00f6a24fb6bd4742ba80c2030b932c44-fbfb6d98b4675b32-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:24:58,190 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9052560, prompt_len=764
2026-08-10 16:25:09,612 INFO     29 [qwen-vl-parser] classify API response (len=50):
```json
{"type": "table", "report_date": null}
```
2026-08-10 16:25:09,615 INFO     29 [qwen-vl-parser] page=4 classify=table report_date=None
2026-08-10 16:25:09,654 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9052560, prompt_len=756
2026-08-10 16:25:12,899 INFO     29 [qwen-vl-parser] table API response (len=372):
\begin{tabular}{cccccccccc}
\hline
检验项目 & 分组 & 样本 & 中文名称 & 英文名称 & 结果 & 定性 & 参考值 & 单位 \\
\hline
LT, AST, GGT, ALI & G001 & 血清 & 肌钙蛋白T & TnT & 5 & & $<14$ & ng/L \\
TSH, FT3, FT4 & G001 & 血清 & & & & & & \\
, CRP, NT-proBNP & G002 & 血清 & & & & & & \\
肌钙蛋白T & G002 & 血清 & & & & & & \\
常规(五分类) & G004 & 全血 & & & & & & \\
PT, APTT & G029 & 血浆 & & & & & & \\
\hline
\end{tabular}
2026-08-10 16:25:12,902 INFO     29 [qwen-vl-parser] page=4 table: 12 LaTeX lines (bbox 83-94)
2026-08-10 16:25:12,902 INFO     29 [qwen-vl-parser] page=4 table: 12 sections
2026-08-10 16:25:15,974 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=8014894, prompt_len=764
2026-08-10 16:25:24,140 INFO     29 [qwen-vl-parser] classify API response (len=50):
```json
{"type": "table", "report_date": null}
```
2026-08-10 16:25:24,143 INFO     29 [qwen-vl-parser] page=5 classify=table report_date=None
2026-08-10 16:25:24,169 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=8014894, prompt_len=756
2026-08-10 16:25:28,855 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:25:28.851+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 74, "failed": 0, "current": {"dca6cdea94d711f1bd9827cf206dfa2d": {"id": "dca6cdea94d711f1bd9827cf206dfa2d", "doc_id": "dbef275894d711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "size": 28457006, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786379026603, "task_type": "dataflow", "root_trace_id": "00f6a24fb6bd4742ba80c2030b932c44", "root_traceparent": "00-00f6a24fb6bd4742ba80c2030b932c44-fbfb6d98b4675b32-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:25:31,563 INFO     29 [qwen-vl-parser] table API response (len=1127):
\begin{tabular}{ccccccccc}
\hline
检验项目 & 分组 & 样本 & 中文名称 & 英文名称 & 结果 & 定性 & 参考值 & 单位 \\
\hline
LT, AST, GGT, ALI & G001 & 血清 & *白细胞计数 & WBC & 6.18 & & 3.5-9.5 & 10E9/L \\
SH, FT3, FT4 & G001 & 血清 & 中性粒细胞百分比 & NE\% & 64.8 & & 40-75 & \% \\
CRP, NT-proBNP & G002 & 血清 & 淋巴细胞百分比 & LY\% & 23.3 & & 20-50 & \% \\
肌钙蛋白T & G002 & 血清 & 单核细胞百分比 & MO\% & 7.7 & & 3-10 & \% \\
常规(五分类) & G004 & 全血 & 嗜酸粒细胞百分比 & EO\% & 4.1 & & 0.4-8.0 & \% \\
PT, APTT & G029 & 血浆 & 嗜碱粒细胞百分比 & BA\% & 0.1 & & 0-1 & \% \\
共6份报告 & & & 中性粒细胞绝对值 & NE\# & 4.00 & & 1.8-6.3 & 10E9/L \\
& & & 淋巴细胞绝对值 & LY\# & 1.44 & & 1.1-3.2 & 10E9/L \\
& & & 单核细胞绝对值 & MO\# & 0.48 & & 0.1-0.6 & 10E9/L \\
& & & 嗜酸粒细胞绝对值 & EO\# & 0.25 & & 0.02-0.52 & 10E9/L \\
& & & 嗜碱粒细胞绝对值 & BA\# & 0.01 & & 0-0.06 & 10E9/L \\
& & & *红细胞计数 & RBC & 4.26 & $\downarrow$ & 4.3-5.8 & 10E12/L \\
& & & *血红蛋白 & Hb & 132 & & 130-175 & g/L \\
& & & *红细胞压积 & HCT & 40.6 & & 40-50 & \% \\
& & & *平均RBC体积 & MCV & 95.2 & & 82-100 & fL \\
& & & 平均RBC血红蛋白含量 & MCH & 30.9 & & 27-34 & pg \\
& & & 平均RBC血红蛋白浓度 & MCHC & 325 & & 316-354 & g/L \\
& & & 红细胞体积分布宽度 & RDW & 12.5 & & $<$15 & \% \\
\hline
\end{tabular}
2026-08-10 16:25:31,565 INFO     29 [qwen-vl-parser] page=5 table: 24 LaTeX lines (bbox 95-118)
2026-08-10 16:25:31,565 INFO     29 [qwen-vl-parser] page=5 table: 24 sections
2026-08-10 16:25:36,768 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=8389343, prompt_len=764
2026-08-10 16:25:45,459 INFO     29 [qwen-vl-parser] classify API response (len=50):
```json
{"type": "table", "report_date": null}
```
2026-08-10 16:25:45,461 INFO     29 [qwen-vl-parser] page=6 classify=table report_date=None
2026-08-10 16:25:45,497 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=8389343, prompt_len=756
2026-08-10 16:25:53,009 INFO     29 [qwen-vl-parser] table API response (len=1198):
\begin{tabular}{cccccccccc}
\hline
检验项目 & 分组 & 样本 & 中文名称 & 英文名称 & 结果 & 定性 & 参考值 & 单位 & \\
\hline
,AST,GGT,ALI & G001 & 血清 & 嗜酸粒细胞百分比 & E0\% & 4.1 & & 0.4-8.0 & \% & \\
H,FT3,FT4 & G001 & 血清 & 嗜碱粒细胞百分比 & BA\% & 0.1 & & 0-1 & \% & \\
RP,NT-proBNP & G002 & 血清 & 中性粒细胞绝对值 & NE\# & 4.00 & & 1.8-6.3 & 10E9/L & \\
肌钙蛋白T & G002 & 血清 & 淋巴细胞绝对值 & LY\# & 1.44 & & 1.1-3.2 & 10E9/L & \\
规(五分类) & G004 & 全血 & 单核细胞绝对值 & MO\# & 0.48 & & 0.1-0.6 & 10E9/L & \\
PT,APTT & G029 & 血浆 & 嗜酸粒细胞绝对值 & EO\# & 0.25 & & 0.02-0.52 & 10E9/L & \\
共6份报告 & & & 嗜碱粒细胞绝对值 & BA\# & 0.01 & & 0-0.06 & 10E9/L & \\
& & & *红细胞计数 & RBC & 4.26 & $\downarrow$ & 4.3-5.8 & 10E12/L & \\
& & & *血红蛋白 & Hb & 132 & & 130-175 & g/L & \\
& & & *红细胞压积 & HCT & 40.6 & & 40-50 & \% & \\
& & & *平均RBC体积 & MCV & 95.2 & & 82-100 & fL & \\
& & & 平均RBC血红蛋白含量 & MCH & 30.9 & & 27-34 & pg & \\
& & & 平均RBC血红蛋白浓度 & MCHC & 325 & & 316-354 & g/L & \\
\hline
\rowcolor{blue!20}
红细胞体积分布宽度 & & & & RDW & 12.5 & & $<$15 & \% & \\
\hline
& & & *血小板计数 & PLT & 166 & & 125-350 & 10E9/L & \\
& & & 平均血小板体积 & MPV & 8.90 & & 8.0-15.0 & fL & \\
& & & 血小板压积 & PCT & 0.147 & & 0.100-0.250 & \% & \\
& & & 血小板体积分布宽度 & PDW & 15.9 & & 14.0-18.0 & \% & \\
\hline
\end{tabular}
2026-08-10 16:25:53,015 INFO     29 [qwen-vl-parser] page=6 table: 27 LaTeX lines (bbox 119-145)
2026-08-10 16:25:53,016 INFO     29 [qwen-vl-parser] page=6 table: 27 sections
2026-08-10 16:25:56,212 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9893096, prompt_len=764
2026-08-10 16:26:00,789 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:26:00.787+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 74, "failed": 0, "current": {"dca6cdea94d711f1bd9827cf206dfa2d": {"id": "dca6cdea94d711f1bd9827cf206dfa2d", "doc_id": "dbef275894d711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "size": 28457006, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786379026603, "task_type": "dataflow", "root_trace_id": "00f6a24fb6bd4742ba80c2030b932c44", "root_traceparent": "00-00f6a24fb6bd4742ba80c2030b932c44-fbfb6d98b4675b32-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:26:06,759 INFO     29 [qwen-vl-parser] classify API response (len=50):
```json
{"type": "table", "report_date": null}
```
2026-08-10 16:26:06,763 INFO     29 [qwen-vl-parser] page=7 classify=table report_date=None
2026-08-10 16:26:06,795 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9893096, prompt_len=756
2026-08-10 16:26:11,006 INFO     29 [qwen-vl-parser] table API response (len=421):
\begin{tabular}{llllllllll}
\hline
项目 & 分组 & 样本 & 中文名称 & 英文名称 & 结果 & 定性 & 参考值 & 单位 & \\
\hline
T,GGT,ALI & G001 & 血清 & *凝血酶原时间 & PT & 12.3 & & 9.8-12.9 & s & \\
T3,FT4 & G001 & 血清 & PT国际标准化比率 & INR & 1.07 & & 0.82-1.20 & & \\
NT-proBNP & G002 & 血清 & *活化部分凝血酶原时间 & APTT & 28.3 & & 23.3-32.5 & s & \\
蛋白T & G002 & 血清 & & & & & & & \\
(五分类) & G004 & 全血 & & & & & & & \\
APTT & G029 & 血浆 & & & & & & & \\
\hline
\end{tabular}
2026-08-10 16:26:11,012 INFO     29 [qwen-vl-parser] page=7 table: 12 LaTeX lines (bbox 146-157)
2026-08-10 16:26:11,012 INFO     29 [qwen-vl-parser] page=7 table: 12 sections
2026-08-10 16:26:13,913 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7162064, prompt_len=764
2026-08-10 16:26:24,401 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 16:26:24,404 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=None
2026-08-10 16:26:24,437 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7162064, prompt_len=401
2026-08-10 16:26:27,041 INFO     29 [qwen-vl-parser] text API response (len=164):
["双侧颈部4区探及数个淋巴结，大者分别约1.7cm×1.2cm（左）、1.6cm×0.7cm（右），边界尚清，形", "态饱满，淋巴结门消失，CDFI示：内部及周边见有血流信号；余颈部未见明显异常肿大淋巴结。", "检查所见", "双侧颈部多发淋巴结肿大（倾向淋巴结转移）", "检查提示", "手术过程", "阳性 阳性"]
2026-08-10 16:26:27,044 INFO     29 [qwen-vl-parser] page=8 text: 7 lines (bbox 158-164)
2026-08-10 16:26:27,045 INFO     29 [qwen-vl-parser] page=8 text: 7 sections
2026-08-10 16:26:30,826 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9377828, prompt_len=764
2026-08-10 16:26:33,618 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:26:33.617+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 74, "failed": 0, "current": {"dca6cdea94d711f1bd9827cf206dfa2d": {"id": "dca6cdea94d711f1bd9827cf206dfa2d", "doc_id": "dbef275894d711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "size": 28457006, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786379026603, "task_type": "dataflow", "root_trace_id": "00f6a24fb6bd4742ba80c2030b932c44", "root_traceparent": "00-00f6a24fb6bd4742ba80c2030b932c44-fbfb6d98b4675b32-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:26:41,470 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 16:26:41,474 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-10 16:26:41,506 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9377828, prompt_len=401
2026-08-10 16:26:45,897 INFO     29 [qwen-vl-parser] text API response (len=403):
["病理报告", "骨髓报告", "检查申请", "检验申请", "输血申请", "手术申请单", "感染报告", "传染报告", "死亡报告", "浏览超声报告文件", "检查(检验)结果比较", "影像分析处理", "超声报告", "超声影像", "穿刺活检前超声检查（仅对穿刺活检淋巴结描述）：左侧锁骨上见肿大淋巴结，大小约1.8cm×1.1cm，", "边界尚清，内部未见淋巴门回声，CDFI：淋巴结内可见血流信号。", "今日15：00-15:08在彩超引导下，常规消毒、铺巾、局麻后，用16G半自动快速组织活检枪，由左下颈分别", "进针约2.8cm、2.7cm，达左侧锁骨上淋巴结内缘后，按压快门，接着迅速拔针，可见短条状组织块送细胞及组织病", "理检查。", "穿刺过程顺利，患者无不适。", "彩超引导下左侧锁骨上淋巴结快速组织活检", "检查提示", "手术过程", "阳性 阳性"]
2026-08-10 16:26:45,899 INFO     29 [qwen-vl-parser] page=9 text: 24 lines (bbox 165-188)
2026-08-10 16:26:45,899 INFO     29 [qwen-vl-parser] page=9 text: 24 sections
2026-08-10 16:26:48,834 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=8081642, prompt_len=764
2026-08-10 16:26:57,425 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-03-18"
}
```
2026-08-10 16:26:57,429 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=2026-03-18
2026-08-10 16:26:57,470 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=8081642, prompt_len=401
2026-08-10 16:27:04,552 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:27:04.551+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 74, "failed": 0, "current": {"dca6cdea94d711f1bd9827cf206dfa2d": {"id": "dca6cdea94d711f1bd9827cf206dfa2d", "doc_id": "dbef275894d711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "size": 28457006, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786379026603, "task_type": "dataflow", "root_trace_id": "00f6a24fb6bd4742ba80c2030b932c44", "root_traceparent": "00-00f6a24fb6bd4742ba80c2030b932c44-fbfb6d98b4675b32-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:27:07,172 INFO     29 [qwen-vl-parser] text API response (len=1404):
["报告", "申请", "申请", "申请", "手术申请单", "报告", "报告", "报告", "浏览影像报告文件", "检查(检验)结果比较", "影像分析处理", "检查部位名称", "检查报告", "影像列表", "4.头颅+躯干(颅底至", "检查序号0005140996", "检查日期2026-03-18 14:04:49", "检查类型PETCT", "检查片号P68729", "检查部位头颅+躯干(颅底到大腿中上 检查方式", "报告医师陈炜佳", "报告时间2026-03-18 14 审核医师刘道佳", "审核时间2026-03-18", "影像所见", "是否异常 是", "“胃食管连接处癌术后”：吻合口壁未见明显增厚及FDG摄取异常增高。腹膜后见多发肿大淋巴", "结，较大者最大横截面约2.1cm×1.1cm，FDG摄取增高，SUVmax5.0。腹膜稍增厚，FDG摄取未见", "明显增高。腹水征阴性。\n大脑各部显像清晰，脑实质密度正常，中线居中，诸脑室系统未见明", "显扩大，脑池、脑沟未见明显增宽。脑皮质及基底节区FDG分布均匀，左右对称，未见明显异常稀", "疏或缺损改变。小脑FDG分布亦未见明显异常。双眼及副鼻窦未见明显异常密度影及异常FDG摄取", "增高。鼻咽部结构对称，两侧未见软组织肿块影，双侧咽隐窝、咽旁间隙存在，咽旁肌群未见FDG", "异常摄取增高，颅底骨质未见破坏。口咽部两侧腺体显影对称。甲状腺两叶不大，形态可，腺实质", "内未见FDG增高灶。颈部未见肿大淋巴结，相应部位未见FDG异常摄取增高。\n双肺见多发不规则", "斑片、条索、结节、粟粒影，部分伴钙化，以双肺上叶为著，FDG摄取轻度增高，SUVmax3.5；双", "肺见多发透亮无肺纹理区，较大者位于右肺尖，最大横截面约8.9cm×5.8cm。双侧锁骨区见数枚", "肿大淋巴结，较大者位于左侧，最大横截面约1.8cm×0.9cm，FDG摄取轻度增高，SUVmax4.0。纵", "隔、双侧肺门见多发肿大淋巴结，伴钙化，较大者短径约1.7cm，FDG摄取轻度增高，SUVmax4.0", "。两侧腋窝未见肿大淋巴结或淋巴结FDG异常摄取增高。心肌显影清晰。气管居中。双侧胸膜稍增", "厚。双侧胸腔少量积液。纵隔大血管本底SUVmax1.4。\n肝脏形态可，轮廓光整，肝叶比例正常，", "肝V段见一囊样低密度影，最大横截面约5.9cm×4.6cm，FDG摄取缺损；余肝实质内FDG分布稍欠", "均匀，SUVmax2.0。肝内外胆管无扩张。胆囊大小正常，密度均匀，胆囊壁无增厚。肝门结构正", "常。胰腺形态FDG分布尚好，胰管不扩张。脾脏轻度显影，FDG分布均匀。两侧肾脏显影可，左肾", "影像诊断", "“胃食管连接处癌术后”：\n1、①腹膜后多发肿大淋巴结，代谢增高，考虑转移可能；②双侧锁", "骨区数枚肿大淋巴结，代谢轻度增高，炎性增生？转移待排除，请结合临床。\n2、腹膜稍增厚，", "低代谢，建议随诊。\n3、双肺多形性改变，纵隔、双侧肺门多发淋巴结，轻微代谢，结合职业", "史，以上考虑炎性肉芽肿性病变，建议随诊；双肺多发肺大泡。\n4、双侧胸膜稍增厚；双侧胸腔", "少量积液。\n5、肝囊肿；左肾囊肿。\n6、左侧肩关节、右侧髋关节炎性病变。"]
2026-08-10 16:27:07,174 INFO     29 [qwen-vl-parser] page=10 text: 48 lines (bbox 189-236)
2026-08-10 16:27:07,174 INFO     29 [qwen-vl-parser] page=10 text: 48 sections
2026-08-10 16:27:12,581 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9022017, prompt_len=764
2026-08-10 16:27:21,413 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-09-02"}
```
2026-08-10 16:27:21,415 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=2024-09-02
2026-08-10 16:27:21,439 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9022017, prompt_len=401
2026-08-10 16:27:24,745 INFO     29 [qwen-vl-parser] text API response (len=279):
["58 未F", "863 已F", "76 已F", "病例库 病理会诊", "姓名", "性别 男", "住院号", "年龄 61岁", "病区/", "床号 /", "送检单位 连江县晓澳卫 送检科室 /", "送检医生", "收到日期 2024-08-28", "取材医生", "取材日期 2024-08-28", "标本名称 /", "临床诊断", "肉眼所见", "镜下所见", "病理诊断（贲门）腺癌。", "特殊检查", "未发报告原因", "报告医生 力超", "审核医生 力超", "报告日期 2024-09-02 报告状态 已审核"]
2026-08-10 16:27:24,748 INFO     29 [qwen-vl-parser] page=11 text: 25 lines (bbox 237-261)
2026-08-10 16:27:24,748 INFO     29 [qwen-vl-parser] page=11 text: 25 sections
2026-08-10 16:27:28,480 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=8552248, prompt_len=764
2026-08-10 16:27:36,528 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:27:36.527+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 74, "failed": 0, "current": {"dca6cdea94d711f1bd9827cf206dfa2d": {"id": "dca6cdea94d711f1bd9827cf206dfa2d", "doc_id": "dbef275894d711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "size": 28457006, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786379026603, "task_type": "dataflow", "root_trace_id": "00f6a24fb6bd4742ba80c2030b932c44", "root_traceparent": "00-00f6a24fb6bd4742ba80c2030b932c44-fbfb6d98b4675b32-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:27:37,234 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-12-05"}
```
2026-08-10 16:27:37,236 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=2024-12-05
2026-08-10 16:27:37,266 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=8552248, prompt_len=401
2026-08-10 16:27:45,853 INFO     29 [qwen-vl-parser] text API response (len=858):
["姓名", "性别男", "年龄01岁", "床号", "送检单位本院", "送检科室", "收到日期2024-11-28", "取材医生", "取材日期2024-11-29", "标本名称下段食管+近端胃", "临床诊断", "肉眼所见小弯LN8个，直径0.1-0.5cm；大弯LN未见；", "1LN2个，直径0.5-1.5cm；2LN2个，直径1.5-2cm；3LN未见；4LN2个，直径0.1-0.2cm；", "5LN未见；7LN6个，直径0.5-2.5cm；8LN1个，直径2.5cm；9LN1个，直径1.5cm；10LN2", "个，直径1-1.5cm；11LN1个，直径1.5cm；", "[肉眼诊断]", "下段食管+近端胃切除标本：上切间距3cm，下切间距10cm，小弯8cm，大弯12cm，紧靠上", "切，距下切1.5cm，于食管胃交界小弯处见一隆起型肿物，大小8x7cm，切面灰白，质硬，", "镜下所见", "病理诊断下段食管+近端胃切除标本：", "（食管胃交界）隆起型低分化腺癌（肿物大小8x7cm，Lauren分型：混合型），伴治疗反", "应（TRG：3级，残余肿瘤约占90%），肿瘤侵犯浆膜下层，脉管内见癌栓，神经见癌侵犯。", "标本上、下切端及另送“上切端”未见癌。淋巴结2/35见转移癌（“", "2”LN1/4、“7”LN1/14、胃小弯LNO/6、“", "1”LNO/2、“4”LNO/2、“8”LNO/6、“9”LNO/1、“11”LNO/2，“3、5”未见LN，", "“10”查见癌结节1枚）。胃小弯LN1/6、“7”LN1/14见治疗后反应。", "肿瘤病理分期：ypT3N1Mx（AJCC第八版）。", "特殊检查", "免疫组化结果：MSH2（+），MSH6（+），MLH1（+），PMS2（+），HER2（0），CD34（血", "未发报告原因", "报告医生陈丽芳", "审核医生陈丽芳", "报告日期2024-12-05", "报告状态已审核"]
2026-08-10 16:27:45,856 INFO     29 [qwen-vl-parser] page=12 text: 34 lines (bbox 262-295)
2026-08-10 16:27:45,856 INFO     29 [qwen-vl-parser] page=12 text: 34 sections
2026-08-10 16:27:50,182 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=11235756, prompt_len=764
2026-08-10 16:28:00,160 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 16:28:00,163 INFO     29 [qwen-vl-parser] page=13 classify=text report_date=None
2026-08-10 16:28:00,206 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=11235756, prompt_len=401
2026-08-10 16:28:06,497 INFO     29 [qwen-vl-parser] text API response (len=676):
["29.11.11.73", "临时用户", "福建省肿瘤医院病历记录", "姓名", "入院记录", "姓", "出生地：福建省福", "性", "别：男", "职业：无职业", "年", "龄：61岁", "病史陈述者：患者本人", "民", "族：汉族", "可靠程度：基本可靠", "婚", "姻：已婚", "入院时间：2024年12月31日08时12分", "过敏史：未发现", "记录时间：2024年12月31日08时36分", "主诉：食管胃连接处腺癌新辅助化免治疗后术后1月余。", "现病史：患者于2024-09-02以\"进行性吞咽困难2个月\"为主诉入院。2024-08-", "23于连江县晓澳卫生院行胃镜示\"贲门肿块浸润性癌；食管下段浸润伴狭窄\"；", "胃镜病理示：（贲门）腺癌。多层螺旋CT平扫+增强扫描+MPR：1.考虑贲门-", "胃体癌伴胃周淋巴结肿大，请结合胃镜及腹部影像学检查；2.双肺多形性变", "伴纵隔、双肺门淋巴结钙化，尘肺可能，请结合病史；3.双肺上叶、右肺中", "叶较大肺大泡；4.扫及肝囊肿，请结合腹部影像学检查；病理会诊报告号（", "H24-03863）：（贲门）腺癌。相关检查未见明显化疗禁忌症，遂于", "2024.09.04、2024.09.27、2024.10.25以\"奥沙利铂 160mg ivgtt d1+5-FU", "4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w\"方案行术前第1-3周期", "129.11.11.73", "临时用户"]
2026-08-10 16:28:06,499 INFO     29 [qwen-vl-parser] page=13 text: 33 lines (bbox 296-328)
2026-08-10 16:28:06,499 INFO     29 [qwen-vl-parser] page=13 text: 33 sections
2026-08-10 16:28:08,489 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:28:08.488+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 74, "failed": 0, "current": {"dca6cdea94d711f1bd9827cf206dfa2d": {"id": "dca6cdea94d711f1bd9827cf206dfa2d", "doc_id": "dbef275894d711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "size": 28457006, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786379026603, "task_type": "dataflow", "root_trace_id": "00f6a24fb6bd4742ba80c2030b932c44", "root_traceparent": "00-00f6a24fb6bd4742ba80c2030b932c44-fbfb6d98b4675b32-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:28:10,279 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9959988, prompt_len=764
2026-08-10 16:28:20,861 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 16:28:20,865 INFO     29 [qwen-vl-parser] page=14 classify=text report_date=None
2026-08-10 16:28:20,906 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9959988, prompt_len=401
2026-08-10 16:28:27,066 INFO     29 [qwen-vl-parser] text API response (len=735):
["T牧入肿入泡；4.扫及肝囊肿，有结台腹部影像子检查；病理会诊报告号（", "H24-03863）：（贲门）腺癌。相关检查未见明显化疗禁忌症，遂于", "2024.09.04、2024.09.27、2024.10.25以\"奥沙利铂 160mg ivgtt d1+5-FU", "4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w\"方案行术前第1-3周期", "化疗，化疗过程顺利。相关检查无手术禁忌症，经充分术前准备后于2024-11", "-28在全麻下行\"腹腔镜辅助食管胃交界处癌根治术\"，术程顺利，恢复良好。", "术后病理回报（病理号：24-31776）：下段食管+近端胃切除标本：（食管胃", "交界）隆起型低分化腺癌（肿物大小8x7cm，Lauren分型：混合型），伴治疗", "反应（TRG：3级，残余肿瘤约占90%），肿瘤侵犯浆膜下层，脉管内见癌栓，", "神经见癌侵犯。标本上、下切端及另送“上切端”未见癌。淋巴结2/35见转", "移癌（“2”LN1/4、“7”LN1/14、胃小弯LN0/6、“1”LN0/2、“4”LN0/2、", "“8”LN0/6、“9”LN0/1、“11”LN0/2，“3、5”未见LN，“10”查见癌结", "节1枚）。胃小弯LN1/6、“7”LN1/14见治疗后反应。肿瘤病理分期：", "ypT3N1Mx（AJCC 第八版）。免疫组化结果：MSH2（+），MSH6（+），", "MLH1（+），PMS2（+），HER2（0），CD34（血管+），D2-40（淋巴管+），", "129.1.11.73", "临时用户", "第 1 页", "129.1.11.73", "临时用户"]
2026-08-10 16:28:27,068 INFO     29 [qwen-vl-parser] page=14 text: 20 lines (bbox 329-348)
2026-08-10 16:28:27,068 INFO     29 [qwen-vl-parser] page=14 text: 20 sections
2026-08-10 16:28:33,965 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=11759905, prompt_len=764
2026-08-10 16:28:41,323 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:28:41.323+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 74, "failed": 0, "current": {"dca6cdea94d711f1bd9827cf206dfa2d": {"id": "dca6cdea94d711f1bd9827cf206dfa2d", "doc_id": "dbef275894d711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "size": 28457006, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786379026603, "task_type": "dataflow", "root_trace_id": "00f6a24fb6bd4742ba80c2030b932c44", "root_traceparent": "00-00f6a24fb6bd4742ba80c2030b932c44-fbfb6d98b4675b32-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:28:43,585 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 16:28:43,589 INFO     29 [qwen-vl-parser] page=15 classify=text report_date=None
2026-08-10 16:28:43,624 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=11759905, prompt_len=401
2026-08-10 16:28:51,441 INFO     29 [qwen-vl-parser] text API response (len=793):
["P53（+），EGFR（60%强着色，20%中等着色，20%弱着色），Ki-67（80% +），CD3（T细胞+，约占肿瘤区域10%），CD8（约占CD3阳性细胞数60%），", "PD1（约占CD3阳性细胞数20%），PD-L1（CPS=5），PD-L1neg（-），P40（ -），Syn（部分+），CgA（少量+），CD56（-），CK5/6（-）。原位杂交", "EBER（-）。患者无咯血丝痰；无咳嗽、盗汗，无胸痛、心悸、头晕、头痛，", "无寒战、发热，无声音嘶哑、饮水呛咳、眼睑下垂，无血尿、少尿、腰背酸", "痛。今为求进一步治疗就诊我院，门诊拟\"食管胃连接处癌新辅助化免治疗后", "术后\"收入院。发病以来精神睡眠尚可，食欲欠佳，大小便正常，体力、体重", "无明显下降。", "既往史：详见旧病历（住院号：", "个人史：详见旧病历（住院号.", "婚育史：详见旧病历（住院号：", "家族史：详见旧病历（住院号：", "73", "体格检查", "T: 36.5 ℃ P: 74 次/分 R: 12 次/分 BP: 120 / 80 mmHg", "发育正常，营养中等，表情自然，正常面容，自主体位，步入病房，步态正常。", "神志清楚，查体合作。全身皮肤粘膜无黄染、苍白、发绀、出血点、水肿、肝", "掌、溃疡、蜘蛛痣。浅表淋巴结检查详见专科情况。头颅无畸形，双眼睑无水", "肿，眼球无突出及震颤，结膜无苍白、充血、出血或水肿，巩膜无黄染，双侧", "瞳孔等大正圆，对光反射灵敏。耳廓外形正常，外耳道无分泌物，乳突无压痛。", "鼻外形正常，口唇无苍白，咽无充血，颈无抵抗，未见颈动脉异常搏动，未见", "颈静脉怒张。气管居中，甲状腺未触及肿大，质软，未及结节，未及震颤，", "间及九立 万列晾对称 未触及肿物 引业于活流 小前区子收扣 小小博动"]
2026-08-10 16:28:51,446 INFO     29 [qwen-vl-parser] page=15 text: 22 lines (bbox 349-370)
2026-08-10 16:28:51,446 INFO     29 [qwen-vl-parser] page=15 text: 22 sections
2026-08-10 16:28:54,878 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9619594, prompt_len=764
2026-08-10 16:29:03,760 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 16:29:03,763 INFO     29 [qwen-vl-parser] page=16 classify=text report_date=None
2026-08-10 16:29:03,812 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9619594, prompt_len=401
2026-08-10 16:29:09,511 INFO     29 [qwen-vl-parser] text API response (len=669):
["临时用户", "体格检查", "T: 36.5 ℃ P: 74 次/分 R: 12 次/分 BP: 120 / 80 mmHg", "发育正常，营养中等，表情自然，正常面容，自主体位，步入病房，步态正常。", "神志清楚，查体合作。全身皮肤粘膜无黄染、苍白、发绀、出血点、水肿、肝", "掌、溃疡、蜘蛛痣。浅表淋巴结检查详见专科情况。头颅无畸形，双眼睑无水", "肿，眼球无突出及震颤，结膜无苍白、充血、出血或水肿，巩膜无黄染，双侧", "瞳孔等大正圆，对光反射灵敏。耳廓外形正常，外耳道无分泌物，乳突无压痛。", "鼻外形正常，口唇无苍白，咽无充血，颈无抵抗，未见颈动脉异常搏动，未见", "颈静脉怒张。气管居中，甲状腺未触及肿大，质软，未及结节，未及震颤，未", "闻及杂音。双乳腺对称，未触及肿物，乳头无溢液。心前区无隆起，心尖搏动", "位于第5肋间左锁骨中线内0.5cm，未见异常搏动，未触及震颤，无心包摩擦感，", "心界不大，心率74次/分，心律齐，心音正常。P2<A2，未见异常血管征，各瓣", "膜听诊区未闻及杂音及心包摩擦音，腹部平坦，未见胃、肠型及蠕动波，未见", "腹壁静脉曲张，腹软，无压痛、未触及包块，Murphy征阴性，肝脾肋下未及。", "肝区肾区无叩痛，腹部叩诊鼓音，移动性浊音(-)。肠鸣音4次/分。脊柱活动", "度可，生理弯曲存在，四肢无畸形，关节无红肿及压痛，主动活动正常，双下", "129.1.11.73", "临时用户", "第 2 页", "129.1.11.73", "临时用户"]
2026-08-10 16:29:09,512 INFO     29 [qwen-vl-parser] page=16 text: 22 lines (bbox 371-392)
2026-08-10 16:29:09,513 INFO     29 [qwen-vl-parser] page=16 text: 22 sections
2026-08-10 16:29:12,223 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:29:12.221+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 74, "failed": 0, "current": {"dca6cdea94d711f1bd9827cf206dfa2d": {"id": "dca6cdea94d711f1bd9827cf206dfa2d", "doc_id": "dbef275894d711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "size": 28457006, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786379026603, "task_type": "dataflow", "root_trace_id": "00f6a24fb6bd4742ba80c2030b932c44", "root_traceparent": "00-00f6a24fb6bd4742ba80c2030b932c44-fbfb6d98b4675b32-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:29:14,036 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=11401514, prompt_len=764
2026-08-10 16:29:25,072 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 16:29:25,074 INFO     29 [qwen-vl-parser] page=17 classify=text report_date=None
2026-08-10 16:29:25,106 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=11401514, prompt_len=401
2026-08-10 16:29:30,183 INFO     29 [qwen-vl-parser] text API response (len=540):
["姓名", "肢无水肿。双侧膝腱反射对称引出，双侧Babinski征(-)，脑膜刺激征-，肛门", "及外生殖器未见明显异常。", "专科检查：神志清楚，营养中等。双颈、双锁骨上、双腋窝未触及肿大淋巴", "结。腹部见术痕，愈合好；胸廓无畸形，气管居中；双肺呼吸运动平稳，触", "觉语颤正常对称，叩诊清音，听诊未闻及干湿罗音及胸膜摩擦音，双肺呼吸", "音清晰。", "辅助检查：暂缺。", "出院诊断", "1、手术后恶性肿瘤化学治疗", "2、食管胃连接处隆起型低分化腺", "癌新辅助化疗后术后（", "ypT3N1M0 IIIIB期）", "3、尘肺？", "4、右肝囊肿", "5、左肝胆管内结石", "6、左肾囊肿", "7、PICC置入术", "书写医生：", "2025年01月06日", "审核医生：", "2025年01月06日", "初步诊断", "1、食管胃连接处隆起型低分化腺癌新辅", "助化免治疗后术后（ypT3N1M0 IIIIB期）", "2、尘肺？", "3、右肝囊肿", "4、左肝胆管内结石", "5、左肾囊肿", "6、PICC置入术", "书写医生：", "2024年12月31日", "审核医生：", "2024年12月31日"]
2026-08-10 16:29:30,189 INFO     29 [qwen-vl-parser] page=17 text: 34 lines (bbox 393-426)
2026-08-10 16:29:30,189 INFO     29 [qwen-vl-parser] page=17 text: 34 sections
2026-08-10 16:29:32,240 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3083359, prompt_len=764
2026-08-10 16:29:40,541 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-03-24"}
```
2026-08-10 16:29:40,541 INFO     29 [qwen-vl-parser] page=18 classify=text report_date=2026-03-24
2026-08-10 16:29:40,561 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3083359, prompt_len=401
2026-08-10 16:29:44,142 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:29:44.141+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 74, "failed": 0, "current": {"dca6cdea94d711f1bd9827cf206dfa2d": {"id": "dca6cdea94d711f1bd9827cf206dfa2d", "doc_id": "dbef275894d711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "size": 28457006, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786379026603, "task_type": "dataflow", "root_trace_id": "00f6a24fb6bd4742ba80c2030b932c44", "root_traceparent": "00-00f6a24fb6bd4742ba80c2030b932c44-fbfb6d98b4675b32-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:29:54,539 INFO     29 [qwen-vl-parser] text API response (len=1859):
["2026-03-24 15:16", "于2024-09-02以'进行性吞咽困难2个月'为主诉入院。2024-08-23于连江县晓澳卫生院行胃镜示'贲门肿块浸润性癌；食管下段浸润伴狭窄'；胃镜病理示：（贲门）腺癌，多层螺旋CT平扫+增强扫描+MPR：1.考虑贲门-胃体癌伴胃周淋巴结肿大", "胃镜及腹部影像学检查；2.双肺多形性支气管纵隔、双肺门淋巴结钙化，尘肺可能，请结合病史；3.双肺上叶、右肺中叶较大肺大泡；4.扫及肝囊肿，请结合腹部影像学检查；病理会诊报告号(H24-03863)：(贲门)腺癌，相关检查未见明显化疗禁忌", "于2024.09.04、2024.09.27、2024.10.25以'奥沙利铂160mg ivgtt d1+5-FU 4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w'方案行术前第1-3周期化疗，化疗过程顺利，相关检查无手术禁忌症，经充分术前准备后于2024-11-28在全麻下行", "胃镜辅助食管胃交界处癌根治术'，术程顺利，恢复良好，术后病理回报(病理号：24-31776)：下段食管+近端胃切除标本：(食管胃交界)隆起型低分化腺癌(肿物大小8x7cm，L...[未打印]", "姓名", "性别：男 年龄：62岁", "主诉：食管癌术后化疗免疫治疗后1年余。", "现病史：于2024-09-02以'进行性吞咽困难2个月'为主诉入院。2024-08-23", "于连江县晓澳卫生院行胃镜示'贲门肿块浸润性癌；食管下段浸润伴狭窄'；胃", "镜病理示：（贲门）腺癌，多层螺旋CT平扫+增强扫描+MPR：1.考虑贲门-", "胃体癌伴胃周淋巴结肿大，请结合胃镜及腹部影像学检查；2.双肺多形性支气管", "纵隔、双肺门淋巴结钙化，尘肺可能，请结合病史；3.双肺上叶、右肺中叶较", "大肺大泡；4.扫及肝囊肿，请结合腹部影像学检查；病理会诊报告号(H24-", "03863)：(贲门)腺癌，相关检查未见明显化疗禁忌症，遂于2024.09.04、", "2024.09.27、2024.10.25以'奥沙利铂160mg ivgtt d1+5-FU 4.5g 微量泵", "泵入 48h+信迪利单抗 200mg ivgtt q3w'方案行术前第1-3周期化疗，化疗", "过程顺利，相关检查无手术禁忌症，经充分术前准备后于2024-11-28在全麻", "下行'腹腔镜辅助食管胃交界处癌根治术'，术程顺利，恢复良好，术后病理回", "报(病理号：24-31776)：下段食管+近端胃切除标本：(食管胃交界)隆", "起型低分化腺癌(肿物大小8x7cm，Lauren分型：混合型)，伴治疗反应", "(TRG：3级，残余肿瘤约占90%)，肿瘤侵犯浆膜下层，脉管内见癌栓，神经", "见癌侵犯。标本上、下切缘及另送'上切缘'未见癌。淋巴结2/35见转移癌", "(\"2\" LN1/4、\"7\" LN1/14、胃小弯LN0/6、\"1\" LN0/2、", "\"4\" LN0/2、\"8\" LN0/6、\"9\" LN0/1、\"11\" LN0/2、\"3、5\" 未见", "LN，\"10\" 查见癌结节1枚)。胃小弯LN1/6、\"7\" LN1/14见治疗后反应。", "肿瘤病理分期：ypT3N1Mx (AJCC 第八版)。免疫组化结果：MSH2", "(+)，MSH6 (+)，MLH1 (+)，PMS2 (+)，HER2 (0)，CD34", "(血管+)，D2-40 (淋巴管+)，P53 (+)，EGFR (60%强着色，20%中", "等着色，20%弱着色)，KI-67 (80%+)，CD3 (T细胞+)，约占肿瘤区域", "10%)，CD8 (约占CD3阳性细胞数60%)，PD1 (约占CD3阳性细胞数", "20%)，PD-L1 (CPS=5)，PD-L1neg (-)，P40 (-)，Syn (部分+)，", "CgA (少量+)，CD56 (-)，CK5/6 (-)。原位杂交EBER (-)。于", "2025.01.02以'紫杉醇 200mg ivgtt d1+奥沙利铂 160mg ivgtt d1+5-FU", "3.4g 微量泵泵入 48h'方案行术后第1周期化疗。后予 '斯鲁利单抗' 免疫治", "疗至今。2026-03-13放射报告：计算机体层成像(CT)增强(胸部+上腹)(故", "<"]
2026-08-10 16:29:54,543 INFO     29 [qwen-vl-parser] page=18 text: 37 lines (bbox 427-463)
2026-08-10 16:29:54,543 INFO     29 [qwen-vl-parser] page=18 text: 37 sections
2026-08-10 16:29:57,163 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3502631, prompt_len=764
2026-08-10 16:30:05,931 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 16:30:05,931 INFO     29 [qwen-vl-parser] page=19 classify=text report_date=None
2026-08-10 16:30:05,958 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3502631, prompt_len=401
2026-08-10 16:30:14,190 INFO     29 [qwen-vl-parser] text API response (len=1177):
["102床 涂美石", "多重耐药感染上报", "4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w\"方案行术前第1-3周期化疗，化疗过程顺利。相关检", "24-31776）：下段食管+近端胃切除标本：（食管胃交界）隆起型低分化腺癌（肿物大小8x7cm，L...[未", "20%），PD-L1（CPS=5），PD-L1neg（-），P40（-），Syn（部分+），", "CgA（少量+），CD56（-），CK5/6（-）。原位杂交EBER（-）。于", "2025.01.02以\"紫杉醇 200mg ivgtt d1+奥沙利铂 160mg ivgtt d1+5-FU", "3.4g 微量泵泵入 48h\"方案行术后第1周期化疗。后予 \"斯鲁利单抗\" 免疫治", "疗至今。2026-03-13放射报告：计算机体层成像（CT）增强(胸部+上腹)(放", "射报告号:CT00333122)1.胃食管交界处癌术后改变，腹腔淋巴结较前相仿，", "腹膜后淋巴结较前增大，转移可能2.双锁骨上区淋巴结，转移可能3.双肺多形", "性变伴纵隔、双肺门淋巴结钙化与前大致相仿，尘肺可能，请结合病史4.双肺", "上叶、右肺中叶肺大泡，较前相仿5.双侧胸腔少量积液较前相仿6.肝囊肿较前", "大致相仿7.左肾囊肿较前相仿。2026-03-18复查PET-CT检查(核医学科报告", "号:P68729) \"胃食管连接处癌术后\"：1、①腹膜后多发肿大淋巴结，代谢增", "高，考虑转移可能；②双侧锁骨区数枚肿大淋巴结，代谢轻度增高，炎性增", "生？转移待排除，请结合临床。2、腹膜稍增厚，低代谢，建议随诊。3、双", "肺多形性改变，纵隔、双侧肺门多发淋巴结，轻微代谢，结合职业史，以上考", "虑炎性肉芽肿性病变，建议随诊；双肺多发肺大泡。4、双侧胸膜稍增厚；双", "侧胸腔少量积液。5、肝囊肿；左肾囊肿。6、左侧肩关节、右侧髋关节炎性", "病变。今日行超声引导下左侧锁骨上淋巴结快速组织活检，今为求进一步诊", "治，再次就诊我院。", "过敏史：未发现。", "体格检查：神志清晰，皮肤色泽正常，淋巴结未触及肿大；心脏：心律齐，心", "音正常；肺：双肺语颤正常、对称，双肺呼吸音清，未闻及异常呼吸音，双肺", "未闻及干湿性啰音；腹部：平软，无压痛、反跳痛，肝脾肋下未触及。", "辅助检查：2026-03-24超声报告：彩超检查（常规）-浅表(超声报告", "号:20260070720)双侧颈部多发淋巴结肿大（倾向淋巴结转移）；", "诊断：", "西医诊断：", "食管恶性肿瘤(ypT3N1M0 III B期)", "中医诊断：", "处理措施：进一步系统治疗。", "药品处方：", "检验检查："]
2026-08-10 16:30:14,191 INFO     29 [qwen-vl-parser] page=19 text: 35 lines (bbox 464-498)
2026-08-10 16:30:14,191 INFO     29 [qwen-vl-parser] page=19 text: 35 sections
2026-08-10 16:30:16,061 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:30:16.061+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 74, "failed": 0, "current": {"dca6cdea94d711f1bd9827cf206dfa2d": {"id": "dca6cdea94d711f1bd9827cf206dfa2d", "doc_id": "dbef275894d711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "size": 28457006, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786379026603, "task_type": "dataflow", "root_trace_id": "00f6a24fb6bd4742ba80c2030b932c44", "root_traceparent": "00-00f6a24fb6bd4742ba80c2030b932c44-fbfb6d98b4675b32-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:30:16,562 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2450187, prompt_len=764
2026-08-10 16:30:27,066 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 16:30:27,067 INFO     29 [qwen-vl-parser] page=20 classify=text report_date=None
2026-08-10 16:30:27,087 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2450187, prompt_len=401
2026-08-10 16:30:31,979 INFO     29 [qwen-vl-parser] text API response (len=650):
["大致相仿7.左肾囊肿较前相仿。2026-03-18复查PET-CT检查(核医学科报告", "号:P68729)“胃食管连接处癌术后”：1、①腹膜后多发肿大淋巴结，代谢增", "高，考虑转移可能；②双侧锁骨区数枚肿大淋巴结，代谢轻度增高，炎性增", "生？转移待排除，请结合临床。2、腹膜稍增厚，低代谢，建议随诊。3、双", "肺多形性改变，纵隔、双侧肺门多发淋巴结，轻微代谢，结合职业史，以上考", "虑炎性肉芽肿性病变，建议随诊；双肺多发肺大泡。4、双侧胸膜稍增厚；双", "侧胸腔少量积液。5、肝囊肿；左肾囊肿。6、左侧肩关节、右侧髋关节炎性", "病变。今日行超声引导下左侧锁骨上淋巴结快速组织活检，今为求进一步诊", "治，再次就诊我院。", "过敏史：未发现。", "体格检查：神志清晰，皮肤色泽正常，淋巴结未触及肿大；心脏：心律齐，心", "音正常；肺：双肺语颤正常、对称，双肺呼吸音清，未闻及异常呼吸音，双肺", "未闻及干湿性啰音；腹部：平软，无压痛、反跳痛，肝脾肋下未触及。", "辅助检查：2026-03-24超声报告：彩超检查（常规）-浅表(超声报告", "号:20260070720)双侧颈部多发淋巴结肿大（倾向淋巴结转移）；", "诊断：", "西医诊断：", "食管恶性肿瘤(ypT3N1M0 IIIIB期)", "中医诊断：", "处理措施：进一步系统治疗。", "药品处方：", "检验检查：", "医生签名：", "签名时间:2026-03-24 15:16"]
2026-08-10 16:30:31,979 INFO     29 [qwen-vl-parser] page=20 text: 24 lines (bbox 499-522)
2026-08-10 16:30:31,979 INFO     29 [qwen-vl-parser] page=20 text: 24 sections
2026-08-10 16:30:31,979 INFO     29 [qwen-vl-parser] parse_pdf done: 523 sections from 20 pages.
2026-08-10 16:30:32,001 INFO     29 Close text detector.
2026-08-10 16:30:41,093 INFO     29 Close text recognizer.
2026-08-10 16:30:41,526 INFO     29 Close recognizer.
2026-08-10 16:30:41,934 INFO     29 Close recognizer.
2026-08-10 16:30:43,105 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 16:30:43,106 INFO     29 [Trace] task=dca6cdea | doc=LBZH，男，63岁，胃癌一线(1).pdf | Parser:MedLink | outputs={"html": "", "json": "523 items", "markdown": "", "text": "", "name": "LBZH，男，63岁，胃癌一线(1).pdf", "output_format": "json"}
2026-08-10 16:30:43,106 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 16:30:43,140 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:30:43,142 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] \\begin{tabular}{ccccccccccc}\n[BBOX-1] 报告时间: 2026-03-23\n[BBOX-2] \\hline\n[BBOX-3] 类型 & 检查日期 & 检验项目 & 分组 & 样本 & 中文名称 & 英文名称 & 结果 & 定性 & 参考值 & 单位 \\\\\n[BBOX-4] \\hline\n[BBOX-5] 门诊 & 2026-03-23 18:27 & L,ALT,AST,GGT,ALI & G001 & 血清 & *白蛋白 & ALB & 38.4 & $\\downarrow$ & 40.0-55.0 & g/L \\\\\n[BBOX-6] 门诊 & 2026-03-23 14:29 & TSH,FT3,FT4 & G001 & 血清 & 总胆红素 & TBIL & 9.3 & & 5.0-21.0 & umol/L \\\\\n[BBOX-7] 门诊 & 2026-03-23 12:47 & PCT,CRP,NT-proBNP & G002 & 血清 & 直接胆红素 & DBIL & 1.9 & & 0-8.0 & umol/L \\\\\n[BBOX-8] 门诊 & 2026-03-23 12:49 & 肌钙蛋白T & G002 & 血清 & 间接胆红素 & IBIL & 7.4 & & 0-20.0 & umol/L \\\\\n[BBOX-9] 门诊 & 2026-03-23 12:04 & 血常规(五分类) & G004 & 全血 & *谷丙转氨酶 & ALT & 80 & $\\uparrow$ & 9-50 & U/L \\\\\n[BBOX-10] 门诊 & 2026-03-23 12:43 & PT,APTT & G029 & 血浆 & *谷草转氨酶 & AST & 58 & $\\uparrow$ & 5-40 & U/L \\\\\n[BBOX-11] \\multicolumn{11}{c}{共6份报告} \\\\\n[BBOX-12] \\multicolumn{11}{c}{ALT/AST} \\\\\n[BBOX-13] \\multicolumn{11}{c}{ALT/AST} \\\\\n[BBOX-14] \\multicolumn{11}{c}{1.38} \\\\\n[BBOX-15] \\multicolumn{11}{c}{*γ谷氨酰转肽酶} \\\\\n[BBOX-16] \\multicolumn{11}{c}{GGT} \\\\\n[BBOX-17] \\multicolumn{11}{c}{50} \\\\\n[BBOX-18] \\multicolumn{11}{c}{10-60} \\\\\n[BBOX-19] \\multicolumn{11}{c}{U/L} \\\\\n[BBOX-20] \\multicolumn{11}{c}{*碱性磷酸酶} \\\\\n[BBOX-21] \\multicolumn{11}{c}{ALP} \\\\\n[BBOX-22] \\multicolumn{11}{c}{93} \\\\\n[BBOX-23] \\multicolumn{11}{c}{45-125} \\\\\n[BBOX-24] \\multicolumn{11}{c}{U/L} \\\\\n[BBOX-25] \\multicolumn{11}{c}{*乳酸脱氢酶} \\\\\n[BBOX-26] \\multicolumn{11}{c}{LDH} \\\\\n[BBOX-27] \\multicolumn{11}{c}{208} \\\\\n[BBOX-28] \\multicolumn{11}{c}{120-250} \\\\\n[BBOX-29] \\multicolumn{11}{c}{U/L} \\\\\n[BBOX-30] \\multicolumn{11}{c}{*尿素} \\\\\n[BBOX-31] \\multicolumn{11}{c}{Urea} \\\\\n[BBOX-32] \\multicolumn{11}{c}{3.12} \\\\\n[BBOX-33] \\multicolumn{11}{c}{$\\downarrow$} \\\\\n[BBOX-34] \\multicolumn{11}{c}{3.6-9.5} \\\\\n[BBOX-35] \\multicolumn{11}{c}{mmol/L} \\\\\n[BBOX-36] \\multicolumn{11}{c}{肌酐} \\\\\n[BBOX-37] \\multicolumn{11}{c}{Cr} \\\\\n[BBOX-38] \\multicolumn{11}{c}{62} \\\\\n[BBOX-39] \\multicolumn{11}{c}{57-111} \\\\\n[BBOX-40] \\multicolumn{11}{c}{umol/L} \\\\\n[BBOX-41] \\multicolumn{11}{c}{尿素/肌酐} \\\\\n[BBOX-42] \\multicolumn{11}{c}{B/C} \\\\\n[BBOX-43] \\multicolumn{11}{c}{0.050} \\\\\n[BBOX-44] \\multicolumn{11}{c}{*尿酸} \\\\\n[BBOX-45] \\multicolumn{11}{c}{UA} \\\\\n[BBOX-46] \\multicolumn{11}{c}{354} \\\\\n[BBOX-47] \\multicolumn{11}{c}{208.3-428.4} \\\\\n[BBOX-48] \\multicolumn{11}{c}{umol/L} \\\\\n[BBOX-49] \\multicolumn{11}{c}{*葡萄糖} \\\\\n[BBOX-50] \\multicolumn{11}{c}{Glu} \\\\\n[BBOX-51] \\multicolumn{11}{c}{6.39} \\\\\n[BBOX-52] \\multicolumn{11}{c}{$\\uparrow$} \\\\\n[BBOX-53] \\multicolumn{11}{c}{3.70-6.10} \\\\\n[BBOX-54] \\multicolumn{11}{c}{mmol/L} \\\\\n[BBOX-55] \\hline\n[BBOX-56] \\end{tabular}\n[BBOX-57] \\begin{tabular}{ccccccccccc}\n[BBOX-58] 报告时间: 2026-03-23\n[BBOX-59] \\hline\n[BBOX-60] 类型 & 检查日期 & 检验项目 & 分组 & 样本 & 中文名称 & 英文名称 & 结果 & 定性 & 参考值 & 单位 \\\\\n[BBOX-61] \\hline\n[BBOX-62] 门诊 & 2026-03-23 18:27 & L,ALT,AST,GGT,ALI & G001 & 血清 & *游离三碘甲状原氨酸 & FT3 & 5.55 & & 3.53-7.37 & pmol/L \\\\\n[BBOX-63] 门诊 & 2026-03-23 14:29 & TSH,FT3,FT4 & G001 & 血清 & *游离甲状腺素 & FT4 & 11.03 & & 7.98-19.24 & pmol/L \\\\\n[BBOX-64] 门诊 & 2026-03-23 12:47 & PCT,CRP,NT-proBNP & G002 & 血清 & *促甲状腺刺激激素 & s-TSH & 1.397 & & 0.340-5.600 & mIU/L \\\\\n[BBOX-65] 门诊 & 2026-03-23 12:49 & 肌钙蛋白T & G002 & 血清 & & & & & & \\\\\n[BBOX-66] 门诊 & 2026-03-23 12:04 & 血常规(五分类) & G004 & 全血 & & & & & & \\\\\n[BBOX-67] 门诊 & 2026-03-23 12:43 & PT,APTT & G029 & 血浆 & & & & & & \\\\\n[BBOX-68] \\multicolumn{11}{c}{共6份报告} \\\\\n[BBOX-69] \\hline\n[BBOX-70] \\end{tabular}\n[BBOX-71] \\begin{tabular}{ccccccccc}\n[BBOX-72] \\hline\n[BBOX-73] 检验项目 & 分组 & 样本 & 中文名称 & 英文名称 & 结果 & 定性 & 参考值 & 单位 \\\\\n[BBOX-74] \\hline\n[BBOX-75] ALT, AST, GGT, ALI & G001 & 血清 & N端-B型钠尿肽前体 & NT-proBNP & 191.85 & & <210.64 & ng/L \\\\\n[BBOX-76] TSH, FT3, FT4 & G001 & 血清 & C反应蛋白 & CRP & 1.15 & & <5.0 & mg/L \\\\\n[BBOX-77] T, CRP, NT-proBNP & G002 & 血清 & 降钙素原 & PCT & 0.04 & & <0.05 & ng/mL \\\\\n[BBOX-78] 肌钙蛋白T & G002 & 血清 & & & & & & \\\\\n[BBOX-79] 血常规(五分类) & G004 & 全血 & & & & & & \\\\\n[BBOX-80] PT, APTT & G029 & 血浆 & & & & & & \\\\\n[BBOX-81] \\hline\n[BBOX-82] \\end{tabular}\n[BBOX-83] \\begin{tabular}{cccccccccc}\n[BBOX-84] \\hline\n[BBOX-85] 检验项目 & 分组 & 样本 & 中文名称 & 英文名称 & 结果 & 定性 & 参考值 & 单位 \\\\\n[BBOX-86] \\hline\n[BBOX-87] LT, AST, GGT, ALI & G001 & 血清 & 肌钙蛋白T & TnT & 5 & & $<14$ & ng/L \\\\\n[BBOX-88] TSH, FT3, FT4 & G001 & 血清 & & & & & & \\\\\n[BBOX-89] , CRP, NT-proBNP & G002 & 血清 & & & & & & \\\\\n[BBOX-90] 肌钙蛋白T & G002 & 血清 & & & & & & \\\\\n[BBOX-91] 常规(五分类) & G004 & 全血 & & & & & & \\\\\n[BBOX-92] PT, APTT & G029 & 血浆 & & & & & & \\\\\n[BBOX-93] \\hline\n[BBOX-94] \\end{tabular}\n[BBOX-95] \\begin{tabular}{ccccccccc}\n[BBOX-96] \\hline\n[BBOX-97] 检验项目 & 分组 & 样本 & 中文名称 & 英文名称 & 结果 & 定性 & 参考值 & 单位 \\\\\n[BBOX-98] \\hline\n[BBOX-99] LT, AST, GGT, ALI & G001 & 血清 & *白细胞计数 & WBC & 6.18 & & 3.5-9.5 & 10E9/L \\\\\n[BBOX-100] SH, FT3, FT4 & G001 & 血清 & 中性粒细胞百分比 & NE\\% & 64.8 & & 40-75 & \\% \\\\\n[BBOX-101] CRP, NT-proBNP & G002 & 血清 & 淋巴细胞百分比 & LY\\% & 23.3 & & 20-50 & \\% \\\\\n[BBOX-102] 肌钙蛋白T & G002 & 血清 & 单核细胞百分比 & MO\\% & 7.7 & & 3-10 & \\% \\\\\n[BBOX-103] 常规(五分类) & G004 & 全血 & 嗜酸粒细胞百分比 & EO\\% & 4.1 & & 0.4-8.0 & \\% \\\\\n[BBOX-104] PT, APTT & G029 & 血浆 & 嗜碱粒细胞百分比 & BA\\% & 0.1 & & 0-1 & \\% \\\\\n[BBOX-105] 共6份报告 & & & 中性粒细胞绝对值 & NE\\# & 4.00 & & 1.8-6.3 & 10E9/L \\\\\n[BBOX-106] & & & 淋巴细胞绝对值 & LY\\# & 1.44 & & 1.1-3.2 & 10E9/L \\\\\n[BBOX-107] & & & 单核细胞绝对值 & MO\\# & 0.48 & & 0.1-0.6 & 10E9/L \\\\\n[BBOX-108] & & & 嗜酸粒细胞绝对值 & EO\\# & 0.25 & & 0.02-0.52 & 10E9/L \\\\\n[BBOX-109] & & & 嗜碱粒细胞绝对值 & BA\\# & 0.01 & & 0-0.06 & 10E9/L \\\\\n[BBOX-110] & & & *红细胞计数 & RBC & 4.26 & $\\downarrow$ & 4.3-5.8 & 10E12/L \\\\\n[BBOX-111] & & & *血红蛋白 & Hb & 132 & & 130-175 & g/L \\\\\n[BBOX-112] & & & *红细胞压积 & HCT & 40.6 & & 40-50 & \\% \\\\\n[BBOX-113] & & & *平均RBC体积 & MCV & 95.2 & & 82-100 & fL \\\\\n[BBOX-114] & & & 平均RBC血红蛋白含量 & MCH & 30.9 & & 27-34 & pg \\\\\n[BBOX-115] & & & 平均RBC血红蛋白浓度 & MCHC & 325 & & 316-354 & g/L \\\\\n[BBOX-116] & & & 红细胞体积分布宽度 & RDW & 12.5 & & $<$15 & \\% \\\\\n[BBOX-117] \\hline\n[BBOX-118] \\end{tabular}\n[BBOX-119] \\begin{tabular}{cccccccccc}\n[BBOX-120] \\hline\n[BBOX-121] 检验项目 & 分组 & 样本 & 中文名称 & 英文名称 & 结果 & 定性 & 参考值 & 单位 & \\\\\n[BBOX-122] \\hline\n[BBOX-123] ,AST,GGT,ALI & G001 & 血清 & 嗜酸粒细胞百分比 & E0\\% & 4.1 & & 0.4-8.0 & \\% & \\\\\n[BBOX-124] H,FT3,FT4 & G001 & 血清 & 嗜碱粒细胞百分比 & BA\\% & 0.1 & & 0-1 & \\% & \\\\\n[BBOX-125] RP,NT-proBNP & G002 & 血清 & 中性粒细胞绝对值 & NE\\# & 4.00 & & 1.8-6.3 & 10E9/L & \\\\\n[BBOX-126] 肌钙蛋白T & G002 & 血清 & 淋巴细胞绝对值 & LY\\# & 1.44 & & 1.1-3.2 & 10E9/L & \\\\\n[BBOX-127] 规(五分类) & G004 & 全血 & 单核细胞绝对值 & MO\\# & 0.48 & & 0.1-0.6 & 10E9/L & \\\\\n[BBOX-128] PT,APTT & G029 & 血浆 & 嗜酸粒细胞绝对值 & EO\\# & 0.25 & & 0.02-0.52 & 10E9/L & \\\\\n[BBOX-129] 共6份报告 & & & 嗜碱粒细胞绝对值 & BA\\# & 0.01 & & 0-0.06 & 10E9/L & \\\\\n[BBOX-130] & & & *红细胞计数 & RBC & 4.26 & $\\downarrow$ & 4.3-5.8 & 10E12/L & \\\\\n[BBOX-131] & & & *血红蛋白 & Hb & 132 & & 130-175 & g/L & \\\\\n[BBOX-132] & & & *红细胞压积 & HCT & 40.6 & & 40-50 & \\% & \\\\\n[BBOX-133] & & & *平均RBC体积 & MCV & 95.2 & & 82-100 & fL & \\\\\n[BBOX-134] & & & 平均RBC血红蛋白含量 & MCH & 30.9 & & 27-34 & pg & \\\\\n[BBOX-135] & & & 平均RBC血红蛋白浓度 & MCHC & 325 & & 316-354 & g/L & \\\\\n[BBOX-136] \\hline\n[BBOX-137] \\rowcolor{blue!20}\n[BBOX-138] 红细胞体积分布宽度 & & & & RDW & 12.5 & & $<$15 & \\% & \\\\\n[BBOX-139] \\hline\n[BBOX-140] & & & *血小板计数 & PLT & 166 & & 125-350 & 10E9/L & \\\\\n[BBOX-141] & & & 平均血小板体积 & MPV & 8.90 & & 8.0-15.0 & fL & \\\\\n[BBOX-142] & & & 血小板压积 & PCT & 0.147 & & 0.100-0.250 & \\% & \\\\\n[BBOX-143] & & & 血小板体积分布宽度 & PDW & 15.9 & & 14.0-18.0 & \\% & \\\\\n[BBOX-144] \\hline\n[BBOX-145] \\end{tabular}\n[BBOX-146] \\begin{tabular}{llllllllll}\n[BBOX-147] \\hline\n[BBOX-148] 项目 & 分组 & 样本 & 中文名称 & 英文名称 & 结果 & 定性 & 参考值 & 单位 & \\\\\n[BBOX-149] \\hline\n[BBOX-150] T,GGT,ALI & G001 & 血清 & *凝血酶原时间 & PT & 12.3 & & 9.8-12.9 & s & \\\\\n[BBOX-151] T3,FT4 & G001 & 血清 & PT国际标准化比率 & INR & 1.07 & & 0.82-1.20 & & \\\\\n[BBOX-152] NT-proBNP & G002 & 血清 & *活化部分凝血酶原时间 & APTT & 28.3 & & 23.3-32.5 & s & \\\\\n[BBOX-153] 蛋白T & G002 & 血清 & & & & & & & \\\\\n[BBOX-154] (五分类) & G004 & 全血 & & & & & & & \\\\\n[BBOX-155] APTT & G029 & 血浆 & & & & & & & \\\\\n[BBOX-156] \\hline\n[BBOX-157] \\end{tabular}\n[BBOX-158] 双侧颈部4区探及数个淋巴结，大者分别约1.7cm×1.2cm（左）、1.6cm×0.7cm（右），边界尚清，形\n[BBOX-159] 态饱满，淋巴结门消失，CDFI示：内部及周边见有血流信号；余颈部未见明显异常肿大淋巴结。\n[BBOX-160] 检查所见\n[BBOX-161] 双侧颈部多发淋巴结肿大（倾向淋巴结转移）\n[BBOX-162] 检查提示\n[BBOX-163] 手术过程\n[BBOX-164] 阳性 阳性\n[BBOX-165] 病理报告\n[BBOX-166] 骨髓报告\n[BBOX-167] 检查申请\n[BBOX-168] 检验申请\n[BBOX-169] 输血申请\n[BBOX-170] 手术申请单\n[BBOX-171] 感染报告\n[BBOX-172] 传染报告\n[BBOX-173] 死亡报告\n[BBOX-174] 浏览超声报告文件\n[BBOX-175] 检查(检验)结果比较\n[BBOX-176] 影像分析处理\n[BBOX-177] 超声报告\n[BBOX-178] 超声影像\n[BBOX-179] 穿刺活检前超声检查（仅对穿刺活检淋巴结描述）：左侧锁骨上见肿大淋巴结，大小约1.8cm×1.1cm，\n[BBOX-180] 边界尚清，内部未见淋巴门回声，CDFI：淋巴结内可见血流信号。\n[BBOX-181] 今日15：00-15:08在彩超引导下，常规消毒、铺巾、局麻后，用16G半自动快速组织活检枪，由左下颈分别\n[BBOX-182] 进针约2.8cm、2.7cm，达左侧锁骨上淋巴结内缘后，按压快门，接着迅速拔针，可见短条状组织块送细胞及组织病\n[BBOX-183] 理检查。\n[BBOX-184] 穿刺过程顺利，患者无不适。\n[BBOX-185] 彩超引导下左侧锁骨上淋巴结快速组织活检\n[BBOX-186] 检查提示\n[BBOX-187] 手术过程\n[BBOX-188] 阳性 阳性\n[BBOX-189] 报告\n[BBOX-190] 申请\n[BBOX-191] 申请\n[BBOX-192] 申请\n[BBOX-193] 手术申请单\n[BBOX-194] 报告\n[BBOX-195] 报告\n[BBOX-196] 报告\n[BBOX-197] 浏览影像报告文件\n[BBOX-198] 检查(检验)结果比较\n[BBOX-199] 影像分析处理\n[BBOX-200] 检查部位名称\n[BBOX-201] 检查报告\n[BBOX-202] 影像列表\n[BBOX-203] 4.头颅+躯干(颅底至\n[BBOX-204] 检查序号0005140996\n[BBOX-205] 检查日期2026-03-18 14:04:49\n[BBOX-206] 检查类型PETCT\n[BBOX-207] 检查片号P68729\n[BBOX-208] 检查部位头颅+躯干(颅底到大腿中上 检查方式\n[BBOX-209] 报告医师陈炜佳\n[BBOX-210] 报告时间2026-03-18 14 审核医师刘道佳\n[BBOX-211] 审核时间2026-03-18\n[BBOX-212] 影像所见\n[BBOX-213] 是否异常 是\n[BBOX-214] “胃食管连接处癌术后”：吻合口壁未见明显增厚及FDG摄取异常增高。腹膜后见多发肿大淋巴\n[BBOX-215] 结，较大者最大横截面约2.1cm×1.1cm，FDG摄取增高，SUVmax5.0。腹膜稍增厚，FDG摄取未见\n[BBOX-216] 明显增高。腹水征阴性。\n大脑各部显像清晰，脑实质密度正常，中线居中，诸脑室系统未见明\n[BBOX-217] 显扩大，脑池、脑沟未见明显增宽。脑皮质及基底节区FDG分布均匀，左右对称，未见明显异常稀\n[BBOX-218] 疏或缺损改变。小脑FDG分布亦未见明显异常。双眼及副鼻窦未见明显异常密度影及异常FDG摄取\n[BBOX-219] 增高。鼻咽部结构对称，两侧未见软组织肿块影，双侧咽隐窝、咽旁间隙存在，咽旁肌群未见FDG\n[BBOX-220] 异常摄取增高，颅底骨质未见破坏。口咽部两侧腺体显影对称。甲状腺两叶不大，形态可，腺实质\n[BBOX-221] 内未见FDG增高灶。颈部未见肿大淋巴结，相应部位未见FDG异常摄取增高。\n双肺见多发不规则\n[BBOX-222] 斑片、条索、结节、粟粒影，部分伴钙化，以双肺上叶为著，FDG摄取轻度增高，SUVmax3.5；双\n[BBOX-223] 肺见多发透亮无肺纹理区，较大者位于右肺尖，最大横截面约8.9cm×5.8cm。双侧锁骨区见数枚\n[BBOX-224] 肿大淋巴结，较大者位于左侧，最大横截面约1.8cm×0.9cm，FDG摄取轻度增高，SUVmax4.0。纵\n[BBOX-225] 隔、双侧肺门见多发肿大淋巴结，伴钙化，较大者短径约1.7cm，FDG摄取轻度增高，SUVmax4.0\n[BBOX-226] 。两侧腋窝未见肿大淋巴结或淋巴结FDG异常摄取增高。心肌显影清晰。气管居中。双侧胸膜稍增\n[BBOX-227] 厚。双侧胸腔少量积液。纵隔大血管本底SUVmax1.4。\n肝脏形态可，轮廓光整，肝叶比例正常，\n[BBOX-228] 肝V段见一囊样低密度影，最大横截面约5.9cm×4.6cm，FDG摄取缺损；余肝实质内FDG分布稍欠\n[BBOX-229] 均匀，SUVmax2.0。肝内外胆管无扩张。胆囊大小正常，密度均匀，胆囊壁无增厚。肝门结构正\n[BBOX-230] 常。胰腺形态FDG分布尚好，胰管不扩张。脾脏轻度显影，FDG分布均匀。两侧肾脏显影可，左肾\n[BBOX-231] 影像诊断\n[BBOX-232] “胃食管连接处癌术后”：\n1、①腹膜后多发肿大淋巴结，代谢增高，考虑转移可能；②双侧锁\n[BBOX-233] 骨区数枚肿大淋巴结，代谢轻度增高，炎性增生？转移待排除，请结合临床。\n2、腹膜稍增厚，\n[BBOX-234] 低代谢，建议随诊。\n3、双肺多形性改变，纵隔、双侧肺门多发淋巴结，轻微代谢，结合职业\n[BBOX-235] 史，以上考虑炎性肉芽肿性病变，建议随诊；双肺多发肺大泡。\n4、双侧胸膜稍增厚；双侧胸腔\n[BBOX-236] 少量积液。\n5、肝囊肿；左肾囊肿。\n6、左侧肩关节、右侧髋关节炎性病变。\n[BBOX-237] 58 未F\n[BBOX-238] 863 已F\n[BBOX-239] 76 已F\n[BBOX-240] 病例库 病理会诊\n[BBOX-241] 姓名\n[BBOX-242] 性别 男\n[BBOX-243] 住院号\n[BBOX-244] 年龄 61岁\n[BBOX-245] 病区/\n[BBOX-246] 床号 /\n[BBOX-247] 送检单位 连江县晓澳卫 送检科室 /\n[BBOX-248] 送检医生\n[BBOX-249] 收到日期 2024-08-28\n[BBOX-250] 取材医生\n[BBOX-251] 取材日期 2024-08-28\n[BBOX-252] 标本名称 /\n[BBOX-253] 临床诊断\n[BBOX-254] 肉眼所见\n[BBOX-255] 镜下所见\n[BBOX-256] 病理诊断（贲门）腺癌。\n[BBOX-257] 特殊检查\n[BBOX-258] 未发报告原因\n[BBOX-259] 报告医生 力超\n[BBOX-260] 审核医生 力超\n[BBOX-261] 报告日期 2024-09-02 报告状态 已审核\n[BBOX-262] 姓名\n[BBOX-263] 性别男\n[BBOX-264] 年龄01岁\n[BBOX-265] 床号\n[BBOX-266] 送检单位本院\n[BBOX-267] 送检科室\n[BBOX-268] 收到日期2024-11-28\n[BBOX-269] 取材医生\n[BBOX-270] 取材日期2024-11-29\n[BBOX-271] 标本名称下段食管+近端胃\n[BBOX-272] 临床诊断\n[BBOX-273] 肉眼所见小弯LN8个，直径0.1-0.5cm；大弯LN未见���\n[BBOX-274] 1LN2个，直径0.5-1.5cm；2LN2个，直径1.5-2cm；3LN未见；4LN2个，直径0.1-0.2cm；\n[BBOX-275] 5LN未见；7LN6个，直径0.5-2.5cm；8LN1个，直径2.5cm；9LN1个，直径1.5cm；10LN2\n[BBOX-276] 个，直径1-1.5cm；11LN1个，直径1.5cm；\n[BBOX-277] [肉眼诊断]\n[BBOX-278] 下段食管+近端胃切除标本：上切间距3cm，下切间距10cm，小弯8cm，大弯12cm，紧靠上\n[BBOX-279] 切，距下切1.5cm，于食管胃交界小弯处见一隆起型肿物，大小8x7cm，切面灰白，质硬，\n[BBOX-280] 镜下所见\n[BBOX-281] 病理诊断下段食管+近端胃切除标本：\n[BBOX-282] （食管胃交界）隆起型低分化腺癌（肿物大小8x7cm，Lauren分型：混合型），伴治疗反\n[BBOX-283] 应（TRG：3级，残余肿瘤约占90%），肿瘤侵犯浆膜下层，脉管内见癌栓，神经见癌侵犯。\n[BBOX-284] 标本上、下切端及另送“上切端”未见癌。淋巴结2/35见转移癌（“\n[BBOX-285] 2”LN1/4、“7”LN1/14、胃小弯LNO/6、“\n[BBOX-286] 1”LNO/2、“4”LNO/2、“8”LNO/6、“9”LNO/1、“11”LNO/2，“3、5”未见LN，\n[BBOX-287] “10”查见癌结节1枚）。胃小弯LN1/6、“7”LN1/14见治疗后反应。\n[BBOX-288] 肿瘤病理分期：ypT3N1Mx（AJCC第八版）。\n[BBOX-289] 特殊检查\n[BBOX-290] 免疫组化结果：MSH2（+），MSH6（+），MLH1（+），PMS2（+），HER2（0），CD34（血\n[BBOX-291] 未发报告原因\n[BBOX-292] 报告医生陈丽芳\n[BBOX-293] 审核医生陈丽芳\n[BBOX-294] 报告日期2024-12-05\n[BBOX-295] 报告状态已审核\n[BBOX-296] 29.11.11.73\n[BBOX-297] 临时用户\n[BBOX-298] 福建省肿瘤医院病历记录\n[BBOX-299] 姓名\n[BBOX-300] 入院记录\n[BBOX-301] 姓\n[BBOX-302] 出生地：福建省福\n[BBOX-303] 性\n[BBOX-304] 别：男\n[BBOX-305] 职业：无职业\n[BBOX-306] 年\n[BBOX-307] 龄：61岁\n[BBOX-308] 病史陈述者：患者本人\n[BBOX-309] 民\n[BBOX-310] 族：汉族\n[BBOX-311] 可靠程度：基本可靠\n[BBOX-312] 婚\n[BBOX-313] 姻：已婚\n[BBOX-314] 入院时间：2024年12月31日08时12分\n[BBOX-315] 过敏史：未发现\n[BBOX-316] 记录时间：2024年12月31日08时36分\n[BBOX-317] 主诉：食管胃连接处腺癌新辅助化免治疗后术后1月余。\n[BBOX-318] 现病史：患者于2024-09-02以\"进行性吞咽困难2个月\"为主诉入院。2024-08-\n[BBOX-319] 23于连江县晓澳卫生院行胃镜示\"贲门肿块浸润性癌；食管下段浸润伴狭窄\"；\n[BBOX-320] 胃镜病理示：（贲门）腺癌。多层螺旋CT平扫+增强扫描+MPR：1.考虑贲门-\n[BBOX-321] 胃体癌伴胃周淋巴结肿大，请结合胃镜及腹部影像学检查；2.双肺多形性变\n[BBOX-322] 伴纵隔、双肺门淋巴结钙化，尘肺可能，请结合病史；3.双肺上叶、右肺中\n[BBOX-323] 叶较大肺大泡；4.扫及肝囊肿，请结合腹部影像学检查；病理会诊报告号（\n[BBOX-324] H24-03863）：（贲门）腺癌。相关检查未见明显化疗禁忌症，遂于\n[BBOX-325] 2024.09.04、2024.09.27、2024.10.25以\"奥沙利铂 160mg ivgtt d1+5-FU\n[BBOX-326] 4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w\"方案行术前第1-3周期\n[BBOX-327] 129.11.11.73\n[BBOX-328] 临时用户\n[BBOX-329] T牧入肿入泡；4.扫及肝囊肿，有结台腹部影像子检查；病理会诊报告号（\n[BBOX-330] H24-03863）：（贲门）腺癌。相关检查未见明显化疗禁忌症，遂于\n[BBOX-331] 2024.09.04、2024.09.27、2024.10.25以\"奥沙利铂 160mg ivgtt d1+5-FU\n[BBOX-332] 4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w\"方案行术前第1-3周期\n[BBOX-333] 化疗，化疗过程顺利。相关检查无手术禁忌症，经充分术前准备后于2024-11\n[BBOX-334] -28在全麻下行\"腹腔镜辅助食管胃交界处癌根治术\"，术程顺利，恢复良好。\n[BBOX-335] 术后病理回报（病理号：24-31776）：下段食管+近端胃切除标本：（食管胃\n[BBOX-336] 交界）隆起型低分化腺癌（肿物大小8x7cm，Lauren分型：混合型），伴治疗\n[BBOX-337] 反应（TRG：3级，残余肿瘤约占90%），肿瘤侵犯浆膜下层，脉管内见癌栓，\n[BBOX-338] 神经见癌侵犯。标本上、下切端及另送“上切端”未见癌。淋巴结2/35见转\n[BBOX-339] 移癌（“2”LN1/4、“7”LN1/14、胃小弯LN0/6、“1”LN0/2、“4”LN0/2、\n[BBOX-340] “8”LN0/6、“9”LN0/1、“11”LN0/2，“3、5”未见LN，“10”查见癌结\n[BBOX-341] 节1枚）。胃小弯LN1/6、“7”LN1/14见治疗后反应。肿瘤病理分期：\n[BBOX-342] ypT3N1Mx（AJCC 第八版）。免疫组化结果：MSH2（+），MSH6（+），\n[BBOX-343] MLH1（+），PMS2（+），HER2（0），CD34（血管+），D2-40（淋巴管+），\n[BBOX-344] 129.1.11.73\n[BBOX-345] 临时用户\n[BBOX-346] 第 1 页\n[BBOX-347] 129.1.11.73\n[BBOX-348] 临时用户\n[BBOX-349] P53（+），EGFR（60%强着色，20%中等着色，20%弱着色），Ki-67（80% +），CD3（T细胞+，约占肿瘤区域10%），CD8（约占CD3阳性细胞数60%），\n[BBOX-350] PD1（约占CD3阳性细胞数20%），PD-L1（CPS=5），PD-L1neg（-），P40（ -），Syn（部分+），CgA（少量+），CD56（-），CK5/6（-）。原位杂交\n[BBOX-351] EBER（-）。患者无咯血丝痰；无咳嗽、盗汗，无胸痛、心悸、头晕、头痛，\n[BBOX-352] 无寒战、发热，无声音嘶哑、饮水呛咳、眼睑下垂，无血尿、少尿、腰背酸\n[BBOX-353] 痛。今为求进一步治疗就诊我院，门诊拟\"食管胃连接处癌新辅助化免治疗后\n[BBOX-354] 术后\"收入院。发病以来精神睡眠尚可，食欲欠佳，大小便正常，体力、体重\n[BBOX-355] 无明显下降。\n[BBOX-356] 既往史：详见旧病历（住院号：\n[BBOX-357] 个人史：详见旧病历（住院号.\n[BBOX-358] 婚育史：详见旧病历（住院号：\n[BBOX-359] 家族史：详见旧病历（住院号：\n[BBOX-360] 73\n[BBOX-361] 体格检查\n[BBOX-362] T: 36.5 ℃ P: 74 次/分 R: 12 次/分 BP: 120 / 80 mmHg\n[BBOX-363] 发育正常，营养中等，表情自然，正常面容，自主体位，步入病房，步态正常。\n[BBOX-364] 神志清楚，查体合作。全身皮肤粘膜无黄染、苍白、发绀、出血点、水肿、肝\n[BBOX-365] 掌、溃疡、蜘蛛痣。浅表淋巴结检查详见专科情况。头颅无畸形，双眼睑无水\n[BBOX-366] 肿，眼球无突出及震颤，结膜无苍白、充血、出血或水肿，巩膜无黄染，双侧\n[BBOX-367] 瞳孔等大正圆，对光反射灵敏。耳廓外形正常，外耳道无分泌物，乳突无压痛。\n[BBOX-368] 鼻外形正常，口唇无苍白，咽无充血，颈无抵抗，未见颈动脉异常搏动，未见\n[BBOX-369] 颈静脉怒张。气管居中，甲状腺未触及肿大，质软，未及结节，未及震颤，\n[BBOX-370] 间及九立 万列晾对称 未触及肿物 引业于活流 小前区子收扣 小小博动\n[BBOX-371] 临时用户\n[BBOX-372] 体格检查\n[BBOX-373] T: 36.5 ℃ P: 74 次/分 R: 12 次/分 BP: 120 / 80 mmHg\n[BBOX-374] 发育正常，营养中等，表情自然，正常面容，自主体位，步入病房，步态正常。\n[BBOX-375] 神志清楚，查体合作。全身皮肤粘膜无黄染、苍白、发绀、出血点、水肿、肝\n[BBOX-376] 掌、溃疡、蜘蛛痣。浅表淋巴结检查详见专科情况。头颅无畸形，双眼睑无水\n[BBOX-377] 肿，眼球无突出及震颤，结膜无苍白、充血、出血或水肿，巩膜无黄染，双侧\n[BBOX-378] 瞳孔等大正圆，对光反射灵敏。耳廓外形正常，外耳道无分泌物，乳突无压痛。\n[BBOX-379] 鼻外形正常，口唇无苍白，咽无充血，颈无抵抗，未见颈动脉异常搏动，未见\n[BBOX-380] 颈静脉怒张。气管居中，甲状腺未触及肿大，质软，未及结节，未及震颤，未\n[BBOX-381] 闻及杂音。双乳腺对称，未触及肿物，乳头无溢液。心前区无隆起，心尖搏动\n[BBOX-382] 位于第5肋间左锁骨中线内0.5cm，未见异常搏动，未触及震颤，无心包摩擦感，\n[BBOX-383] 心界不大，心率74次/分，心律齐，心音正常。P2<A2，未见异常血管征，各瓣\n[BBOX-384] 膜听诊区未闻及杂音及心包摩擦音，腹部平坦，未见胃、肠型及蠕动波，未见\n[BBOX-385] 腹壁静脉曲张，腹软，无压痛、未触及包块，Murphy征阴性，肝脾肋下未及。\n[BBOX-386] 肝区肾区无叩痛，腹部叩诊鼓音，移动性浊音(-)。肠鸣音4次/分。脊柱活动\n[BBOX-387] 度可，生理弯曲存在，四肢无畸形，关节无红肿及压痛，主动活动正常，双下\n[BBOX-388] 129.1.11.73\n[BBOX-389] 临时用户\n[BBOX-390] 第 2 页\n[BBOX-391] 129.1.11.73\n[BBOX-392] 临时用户\n[BBOX-393] 姓名\n[BBOX-394] 肢无水肿。双侧膝腱反射对称引出，双侧Babinski征(-)，脑膜刺激征-，肛门\n[BBOX-395] 及外生殖器未见明显异常。\n[BBOX-396] 专科检查：神志清楚，营养中等。双颈、双锁骨上、双腋窝未触及肿大淋巴\n[BBOX-397] 结。腹部见术痕，愈合好；胸廓无畸形，气管居中；双肺呼吸运动平稳，触\n[BBOX-398] 觉语颤正常对称，叩诊清音，听诊未闻及干湿罗音及胸膜摩擦音，双肺呼吸\n[BBOX-399] 音清晰。\n[BBOX-400] 辅助检查：暂缺。\n[BBOX-401] 出院诊断\n[BBOX-402] 1、手术后恶性肿瘤化学治疗\n[BBOX-403] 2、食管胃连接处隆起型低分化腺\n[BBOX-404] 癌新辅助化疗后术后（\n[BBOX-405] ypT3N1M0 IIIIB期）\n[BBOX-406] 3、尘肺？\n[BBOX-407] 4、右肝囊肿\n[BBOX-408] 5、左肝胆管内结石\n[BBOX-409] 6、左肾囊肿\n[BBOX-410] 7、PICC置入术\n[BBOX-411] 书写医生：\n[BBOX-412] 2025年01月06日\n[BBOX-413] 审核医生：\n[BBOX-414] 2025年01月06日\n[BBOX-415] 初步诊断\n[BBOX-416] 1、食管胃连接处隆起型低分化腺癌新辅\n[BBOX-417] 助化免治疗后术后（ypT3N1M0 IIIIB期）\n[BBOX-418] 2、尘肺？\n[BBOX-419] 3、右肝囊肿\n[BBOX-420] 4、左肝胆管内结石\n[BBOX-421] 5、左肾囊肿\n[BBOX-422] 6、PICC置入术\n[BBOX-423] 书写医生：\n[BBOX-424] 2024年12月31日\n[BBOX-425] 审核医生：\n[BBOX-426] 2024年12月31日\n[BBOX-427] 2026-03-24 15:16\n[BBOX-428] 于2024-09-02以'进行性吞咽困难2个月'为主诉入院。2024-08-23于连江县晓澳卫生院行胃镜示'贲门肿块浸润性癌；食管下段浸润伴狭窄'；胃镜病理示：（贲门）腺癌，多层螺旋CT平扫+增强扫描+MPR：1.考虑贲门-胃体癌伴胃周淋巴结肿大\n[BBOX-429] 胃镜及腹部影像学检查；2.双肺多形性支气管纵隔、双肺门淋巴结钙化，尘肺可能，请结合病史；3.双肺上叶、右肺中叶较大肺大泡；4.扫及肝囊肿，请结合腹部影像学检查；病理会诊报告号(H24-03863)：(贲门)腺癌，相关检查未见明显化疗禁忌\n[BBOX-430] 于2024.09.04、2024.09.27、2024.10.25以'奥沙利铂160mg ivgtt d1+5-FU 4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w'方案行术前第1-3周期化疗，化疗过程顺利，相关检查无手术禁忌症，经充分术前准备后于2024-11-28在全麻下行\n[BBOX-431] 胃镜辅助食管胃交界处癌根治术'，术程顺利，恢复良好，术后病理回报(病理号：24-31776)：下段食管+近端胃切除标本：(食管胃交界)隆起型低分化腺癌(肿物大小8x7cm，L...[未打印]\n[BBOX-432] 姓名\n[BBOX-433] 性别：男 年龄：62岁\n[BBOX-434] 主诉：食管癌术后化疗免疫治疗后1年余。\n[BBOX-435] 现病史：于2024-09-02以'进行性吞咽困难2个月'为主诉入院。2024-08-23\n[BBOX-436] 于连江县晓澳卫生院行胃镜示'贲门肿块浸润性癌；食管下段浸润伴狭窄'；胃\n[BBOX-437] 镜病理示：（贲门）腺癌，多层螺旋CT平扫+增强扫描+MPR：1.考虑贲门-\n[BBOX-438] 胃体癌伴胃周淋巴结肿大，请结合胃镜及腹部影像学检查；2.双肺多形性支气管\n[BBOX-439] 纵隔、双肺门淋巴结钙化，尘肺可能，请结合病史；3.双肺上叶、右肺中叶较\n[BBOX-440] 大肺大泡；4.扫及肝囊肿，请结合腹部影像学检查；病理会诊报告号(H24-\n[BBOX-441] 03863)：(贲门)腺癌，相关检查未见明显化疗禁忌症，遂于2024.09.04、\n[BBOX-442] 2024.09.27、2024.10.25以'奥沙利铂160mg ivgtt d1+5-FU 4.5g 微量泵\n[BBOX-443] 泵入 48h+信迪利单抗 200mg ivgtt q3w'方案行术前第1-3周期化疗，化疗\n[BBOX-444] 过程顺利，相关检查无手术禁忌症，经充分术前准备后于2024-11-28在全麻\n[BBOX-445] 下行'腹腔镜辅助食管胃交界处癌根治术'，术程顺利，恢复良好，术后病理回\n[BBOX-446] 报(病理号：24-31776)：下段食管+近端胃切除标本：(食管胃交界)隆\n[BBOX-447] 起型低分化腺癌(肿物大小8x7cm，Lauren分型：混合型)，伴治疗反应\n[BBOX-448] (TRG：3级，残余肿瘤约占90%)，肿瘤侵犯浆膜下层，脉管内见癌栓，神经\n[BBOX-449] 见癌侵犯。标本上、下切缘及另送'上切缘'未见癌。淋巴结2/35见转移癌\n[BBOX-450] (\"2\" LN1/4、\"7\" LN1/14、胃小弯LN0/6、\"1\" LN0/2、\n[BBOX-451] \"4\" LN0/2、\"8\" LN0/6、\"9\" LN0/1、\"11\" LN0/2、\"3、5\" 未见\n[BBOX-452] LN，\"10\" 查见癌结节1枚)。胃小弯LN1/6、\"7\" LN1/14见治疗后反应。\n[BBOX-453] 肿瘤病理分期：ypT3N1Mx (AJCC 第八版)。免疫组化结果：MSH2\n[BBOX-454] (+)，MSH6 (+)，MLH1 (+)，PMS2 (+)，HER2 (0)，CD34\n[BBOX-455] (血管+)，D2-40 (淋巴管+)，P53 (+)，EGFR (60%强着色，20%中\n[BBOX-456] 等着色，20%弱着色)，KI-67 (80%+)，CD3 (T细胞+)，约占肿瘤区域\n[BBOX-457] 10%)，CD8 (约占CD3阳性细胞数60%)，PD1 (约占CD3阳性细胞数\n[BBOX-458] 20%)，PD-L1 (CPS=5)，PD-L1neg (-)，P40 (-)，Syn (部分+)，\n[BBOX-459] CgA (少量+)，CD56 (-)，CK5/6 (-)。原位杂交EBER (-)。于\n[BBOX-460] 2025.01.02以'紫杉醇 200mg ivgtt d1+奥沙利铂 160mg ivgtt d1+5-FU\n[BBOX-461] 3.4g 微量泵泵入 48h'方案行术后第1周期化疗。后予 '斯鲁利单抗' 免疫治\n[BBOX-462] 疗至今。2026-03-13放射报告：计算机体层成像(CT)增强(胸部+上腹)(故\n[BBOX-463] <\n[BBOX-464] 102床 涂美石\n[BBOX-465] 多重耐药感染上报\n[BBOX-466] 4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w\"方案行术前第1-3周期化疗，化疗过程顺利。相关检\n[BBOX-467] 24-31776）：下段食管+近端胃切除标本：（食管胃交界）隆起型低分化腺癌（肿物大小8x7cm，L...[未\n[BBOX-468] 20%），PD-L1（CPS=5），PD-L1neg（-），P40（-），Syn（部分+），\n[BBOX-469] CgA（少量+），CD56（-），CK5/6（-）。原位杂交EBER（-）。于\n[BBOX-470] 2025.01.02以\"紫杉醇 200mg ivgtt d1+奥沙利铂 160mg ivgtt d1+5-FU\n[BBOX-471] 3.4g 微量泵泵入 48h\"方案行术后第1周期化疗。后予 \"斯鲁利单抗\" 免疫治\n[BBOX-472] 疗至今。2026-03-13放射报告：计算机体层成像（CT）增强(胸部+上腹)(放\n[BBOX-473] 射报告号:CT00333122)1.胃食管交界处癌术后改变，腹腔淋巴结较前相仿，\n[BBOX-474] 腹膜后淋巴结较前增大，转移可能2.双锁骨上区淋巴结，转移可能3.双肺多形\n[BBOX-475] 性变伴纵隔、双肺门淋巴结钙化与前大致相仿，尘肺可能，请结合病史4.双肺\n[BBOX-476] 上叶、右肺中叶肺大泡，较前相仿5.双侧胸腔少量积液较前相仿6.肝囊肿较前\n[BBOX-477] 大致相仿7.左肾囊肿较前相仿。2026-03-18复查PET-CT检查(核医学科报告\n[BBOX-478] 号:P68729) \"胃食管连接处癌术后\"：1、①腹膜后多发肿大淋巴结，代谢增\n[BBOX-479] 高，考虑转移可能；②双侧锁骨区数枚肿大淋巴结，代谢轻度增高，炎性增\n[BBOX-480] 生？转移待排除，请结合临床。2、腹膜稍增厚，低代谢，建议随诊。3、双\n[BBOX-481] 肺多形性改变，纵隔、双侧肺门多发淋巴结，轻微代谢，结合职业史，以上考\n[BBOX-482] 虑炎性肉芽肿性病变，建议随诊；双肺多发肺大泡。4、双侧胸膜稍增厚；双\n[BBOX-483] 侧胸腔少量积液。5、肝囊肿；���肾囊肿。6、左侧肩关节、右侧髋关节炎性\n[BBOX-484] 病变。今日行超声引导下左侧锁骨上淋巴结快速组织活检，今为求进一步诊\n[BBOX-485] 治，再次就诊我院。\n[BBOX-486] 过敏史：未发现。\n[BBOX-487] 体格检查：神志清晰，皮肤色泽正常，淋巴结未触及肿大；心脏：心律齐，心\n[BBOX-488] 音正常；肺：双肺语颤正常、对称，双肺呼吸音清，未闻及异常呼吸音，双肺\n[BBOX-489] 未闻及干湿性啰音；腹部：平软，无压痛、反跳痛，肝脾肋下未触及。\n[BBOX-490] 辅助检查：2026-03-24超声报告：彩超检查（常规）-浅表(超声报告\n[BBOX-491] 号:20260070720)双侧颈部多发淋巴结肿大（倾向淋巴结转移）；\n[BBOX-492] 诊断：\n[BBOX-493] 西医诊断：\n[BBOX-494] 食管恶性肿瘤(ypT3N1M0 III B期)\n[BBOX-495] 中医诊断：\n[BBOX-496] 处理措施：进一步系统治疗。\n[BBOX-497] 药品处方：\n[BBOX-498] 检验检查：\n[BBOX-499] 大致相仿7.左肾囊肿较前相仿。2026-03-18复查PET-CT检查(核医学科报告\n[BBOX-500] 号:P68729)“胃食管连接处癌术后”：1、①腹膜后多发肿大淋巴结，代谢增\n[BBOX-501] 高，考虑转移可能；②双侧锁骨区数枚肿大淋巴结，代谢轻度增高，炎性增\n[BBOX-502] 生？转移待排除，请结合临床。2、腹膜稍增厚，低代谢，建议随诊。3、双\n[BBOX-503] 肺多形性改变，纵隔、双侧肺门多发淋巴结，轻微代谢，结合职业史，以上考\n[BBOX-504] 虑炎性肉芽肿性病变，建议随诊；双肺多发肺大泡。4、双侧胸膜稍增厚；双\n[BBOX-505] 侧胸腔少量积液。5、肝囊肿；左肾囊肿。6、左侧肩关节、右侧髋关节炎性\n[BBOX-506] 病变。今日行超声引导下左侧锁骨上淋巴结快速组织活检，今为求进一步诊\n[BBOX-507] 治，再次就诊我院。\n[BBOX-508] 过敏史：未发现。\n[BBOX-509] 体格检查：神志清晰，皮肤色泽正常，淋巴结未触及肿大；心脏：心律齐，心\n[BBOX-510] 音正常；肺：双肺语颤正常、对称，双肺呼吸音清，未闻及异常呼吸音，双肺\n[BBOX-511] 未闻及干湿性啰音；腹部：平软，无压痛、反跳痛，肝脾肋下未触及。\n[BBOX-512] 辅助检查：2026-03-24超声报告：彩超检查（常规）-浅表(超声报告\n[BBOX-513] 号:20260070720)双侧颈部多发淋巴结肿大（倾向淋巴结转移）；\n[BBOX-514] 诊断：\n[BBOX-515] 西医诊断：\n[BBOX-516] 食管恶性肿瘤(ypT3N1M0 IIIIB期)\n[BBOX-517] 中医诊断：\n[BBOX-518] 处理措施：进一步系统治疗。\n[BBOX-519] 药品处方：\n[BBOX-520] 检验检查：\n[BBOX-521] 医生签名：\n[BBOX-522] 签名时间:2026-03-24 15:16"
  }
]
2026-08-10 16:30:48,094 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:30:48.092+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 74, "failed": 0, "current": {"dca6cdea94d711f1bd9827cf206dfa2d": {"id": "dca6cdea94d711f1bd9827cf206dfa2d", "doc_id": "dbef275894d711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "size": 28457006, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786379026603, "task_type": "dataflow", "root_trace_id": "00f6a24fb6bd4742ba80c2030b932c44", "root_traceparent": "00-00f6a24fb6bd4742ba80c2030b932c44-fbfb6d98b4675b32-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:30:56,781 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:30:56,798 INFO     29 [SmartSplitter] position expansion: 51 blocks → 60 sub-positions
2026-08-10 16:30:56,810 INFO     29 [SmartSplitter] SmartSplitter done: 7 chunks from 7 LLM segments (all bbox_id). Types: {'LabReport': 1, 'ExaminationReport': 4, 'AdmissionRecord': 1, 'OutpatientRecord': 1}
2026-08-10 16:30:56,833 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 16:30:56,833 INFO     29 [Trace] task=dca6cdea | doc=LBZH，男，63岁，胃癌一线(1).pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "523 items", "markdown": "", "text": "", "name": "LBZH，男，63岁，胃癌一线(1).pdf", "output_format": "chunks", "chunks": "7 items, types={'LabReport': 1, 'ExaminationReport': 4, 'AdmissionRecord': 1, 'OutpatientRecord': 1}"}
2026-08-10 16:30:56,833 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 16:30:56,835 INFO     29 [ChunkRouter] Routed 7 chunks into 4 groups: {'chunks_LabExam': 1, 'chunks_Examination': 4, 'chunks_Admission': 1, 'chunks_Clinical': 1}
2026-08-10 16:30:56,848 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 16:30:56,848 INFO     29 [Trace] task=dca6cdea | doc=LBZH，男，63岁，胃癌一线(1).pdf | ChunkRouter:Router | outputs={"html": "", "json": "523 items", "markdown": "", "text": "", "name": "LBZH，男，63岁，胃癌一线(1).pdf", "output_format": "chunks", "chunks": "7 items, types={'LabReport': 1, 'ExaminationReport': 4, 'AdmissionRecord': 1, 'OutpatientRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_LabExam\": 1, \"chunks_Examination\": 4, \"chunks_Admission\": 1, \"chunks_Clinical\": 1}"}
2026-08-10 16:30:56,848 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 16:30:56,855 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:30:56,856 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:30:56,856 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[0, 1, 2, 3, 4, 5, 6]
2026-08-10 16:30:56,856 INFO     29 [qwen-vl-table] positions ： [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:30:57,930 INFO     29 [qwen-vl-table] page=0, rect=3012x1665, img=(8367x4625)
2026-08-10 16:30:59,013 INFO     29 [qwen-vl-table] page=1, rect=3011x1805, img=(8364x5014)
2026-08-10 16:31:00,139 INFO     29 [qwen-vl-table] page=2, rect=3018x1886, img=(8384x5239)
2026-08-10 16:31:01,407 INFO     29 [qwen-vl-table] page=3, rect=3034x2101, img=(8428x5837)
2026-08-10 16:31:02,456 INFO     29 [qwen-vl-table] page=4, rect=3048x1951, img=(8467x5420)
2026-08-10 16:31:03,562 INFO     29 [qwen-vl-table] page=5, rect=3000x1983, img=(8334x5509)
2026-08-10 16:31:04,922 INFO     29 [qwen-vl-table] page=6, rect=3054x2143, img=(8484x5953)
2026-08-10 16:31:04,923 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:31:04,923 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 0, \"bbox_end\": 157, \"encounter_dates\": [\"2026-03-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccccc}\n报告时间: 2026-03-23\n\\hline\n类型 & 检查日期 & 检验项目 & 分组 & 样本 & 中文名称 & 英文名称 & 结果 & 定性 & 参考值 & 单位 \\\\\n\\hline\n门诊 & 2026-03-23 18:27 & L,ALT,AST,GGT,ALI & G001 & 血清 & *白蛋白 & ALB & 38.4 & $\\downarrow$ & 40.0-55.0 & g/L \\\\\n门诊 & 2026-03-23 14:29 & TSH,FT3,FT4 & G001 & 血清 & 总胆红素 & TBIL & 9.3 & & 5.0-21.0 & umol/L \\\\\n门诊 & 2026-03-23 12:47 & PCT,CRP,NT-proBNP & G002 & 血清 & 直接胆红素 & DBIL & 1.9 & & 0-8.0 & umol/L \\\\\n门诊 & 2026-03-23 12:49 & 肌钙蛋白T & G002 & 血清 & 间接胆红素 & IBIL & 7.4 & & 0-20.0 & umol/L \\\\\n门诊 & 2026-03-23 12:04 & 血常规(五分类) & G004 & 全血 & *谷丙转氨酶 & ALT & 80 & $\\uparrow$ & 9-50 & U/L \\\\\n门诊 & 2026-03-23 12:43 & PT,APTT & G029 & 血浆 & *谷草转氨酶 & AST & 58 & $\\uparrow$ & 5-40 & U/L \\\\\n\\multicolumn{11}{c}{共6份报告} \\\\\n\\multicolumn{11}{c}{ALT/AST} \\\\\n\\multicolumn{11}{c}{ALT/AST} \\\\\n\\multicolumn{11}{c}{1.38} \\\\\n\\multicolumn{11}{c}{*γ谷氨酰转肽酶} \\\\\n\\multicolumn{11}{c}{GGT} \\\\\n\\multicolumn{11}{c}{50} \\\\\n\\multicolumn{11}{c}{10-60} \\\\\n\\multicolumn{11}{c}{U/L} \\\\\n\\multicolumn{11}{c}{*碱性磷酸酶} \\\\\n\\multicolumn{11}{c}{ALP} \\\\",
    "role": "user"
  }
]
2026-08-10 16:31:09,886 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:31:09,886 INFO     29 [qwen-vl-table] page=0 LLM output (len=1203):
{
  "report_date": "2026-03-23",
  "items": [
    {
      "name": "白蛋白",
      "item_code": "ALB",
      "value": "38.4",
      "unit": "g/L",
      "reference_range": "40.0-55.0",
      "abnormal": true
    },
    {
      "name": "总胆红素",
      "item_code": "TBIL",
      "value": "9.3",
      "unit": "umol/L",
      "reference_range": "5.0-21.0",
      "abnormal": false
    },
    {
      "name": "直接胆红素",
      "item_code": "DBIL",
      "value": "1.9",
      "unit": "umol/L",
      "reference_range": "0-8.0",
      "abnormal": false
    },
    {
      "name": "间接胆红素",
      "item_code": "IBIL",
      "value": "7.4",
      "unit": "umol/L",
      "reference_range": "0-20.0",
      "abnormal": false
    },
    {
      "name": "谷丙转氨酶",
      "item_code": "ALT",
      "value": "80",
      "unit": "U/L",
      "reference_range": "9-50",
      "abnormal": true
    },
    {
      "name": "谷草转氨酶",
      "item_code": "AST",
      "value": "58",
      "unit": "U/L",
      "reference_range": "5-40",
      "abnormal": true
    },
    {
      "name": "γ谷氨酰转肽酶",
      "item_code": "GGT",
      "value": "50",
      "unit": "U/L",
      "reference_range": "10-60",
      "abnormal": false
    }
  ]
}
2026-08-10 16:31:09,886 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:31:09,887 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 0, \"bbox_end\": 157, \"encounter_dates\": [\"2026-03-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\multicolumn{11}{c}{93} \\\\\n\\multicolumn{11}{c}{45-125} \\\\\n\\multicolumn{11}{c}{U/L} \\\\\n\\multicolumn{11}{c}{*乳酸脱氢酶} \\\\\n\\multicolumn{11}{c}{LDH} \\\\\n\\multicolumn{11}{c}{208} \\\\\n\\multicolumn{11}{c}{120-250} \\\\\n\\multicolumn{11}{c}{U/L} \\\\\n\\multicolumn{11}{c}{*尿素} \\\\\n\\multicolumn{11}{c}{Urea} \\\\\n\\multicolumn{11}{c}{3.12} \\\\\n\\multicolumn{11}{c}{$\\downarrow$} \\\\\n\\multicolumn{11}{c}{3.6-9.5} \\\\\n\\multicolumn{11}{c}{mmol/L} \\\\\n\\multicolumn{11}{c}{肌酐} \\\\\n\\multicolumn{11}{c}{Cr} \\\\\n\\multicolumn{11}{c}{62} \\\\\n\\multicolumn{11}{c}{57-111} \\\\\n\\multicolumn{11}{c}{umol/L} \\\\\n\\multicolumn{11}{c}{尿素/肌酐} \\\\\n\\multicolumn{11}{c}{B/C} \\\\\n\\multicolumn{11}{c}{0.050} \\\\",
    "role": "user"
  }
]
2026-08-10 16:31:12,496 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:31:12,496 INFO     29 [qwen-vl-table] page=1 LLM output (len=704):
{
  "report_date": "2026-03-23",
  "items": [
    {
      "name": "乳酸脱氢酶",
      "item_code": "LDH",
      "value": "208",
      "unit": "U/L",
      "reference_range": "120-250",
      "abnormal": false
    },
    {
      "name": "尿素",
      "item_code": "Urea",
      "value": "3.12",
      "unit": "mmol/L",
      "reference_range": "3.6-9.5",
      "abnormal": true
    },
    {
      "name": "肌酐",
      "item_code": "Cr",
      "value": "62",
      "unit": "umol/L",
      "reference_range": "57-111",
      "abnormal": false
    },
    {
      "name": "尿素/肌酐",
      "item_code": "B/C",
      "value": "0.050",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-10 16:31:12,499 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:31:12,499 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 0, \"bbox_end\": 157, \"encounter_dates\": [\"2026-03-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\multicolumn{11}{c}{*尿酸} \\\\\n\\multicolumn{11}{c}{UA} \\\\\n\\multicolumn{11}{c}{354} \\\\\n\\multicolumn{11}{c}{208.3-428.4} \\\\\n\\multicolumn{11}{c}{umol/L} \\\\\n\\multicolumn{11}{c}{*葡萄糖} \\\\\n\\multicolumn{11}{c}{Glu} \\\\\n\\multicolumn{11}{c}{6.39} \\\\\n\\multicolumn{11}{c}{$\\uparrow$} \\\\\n\\multicolumn{11}{c}{3.70-6.10} \\\\\n\\multicolumn{11}{c}{mmol/L} \\\\\n\\hline\n\\end{tabular}\n\\begin{tabular}{ccccccccccc}\n报告时间: 2026-03-23\n\\hline\n类型 & 检查日期 & 检验项目 & 分组 & 样本 & 中文名称 & 英文名称 & 结果 & 定性 & 参考值 & 单位 \\\\\n\\hline\n门诊 & 2026-03-23 18:27 & L,ALT,AST,GGT,ALI & G001 & 血清 & *游离三碘甲状原氨酸 & FT3 & 5.55 & & 3.53-7.37 & pmol/L \\\\\n门诊 & 2026-03-23 14:29 & TSH,FT3,FT4 & G001 & 血清 & *游离甲状腺素 & FT4 & 11.03 & & 7.98-19.24 & pmol/L \\\\\n门诊 & 2026-03-23 12:47 & PCT,CRP,NT-proBNP & G002 & 血清 & *促甲状腺刺激激素 & s-TSH & 1.397 & & 0.340-5.600 & mIU/L \\\\\n门诊 & 2026-03-23 12:49 & 肌钙蛋白T & G002 & 血清 & & & & & & \\\\",
    "role": "user"
  }
]
2026-08-10 16:31:15,799 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:31:15,799 INFO     29 [qwen-vl-table] page=2 LLM output (len=918):
{
  "report_date": "2026-03-23",
  "items": [
    {
      "name": "*尿酸",
      "item_code": "UA",
      "value": "354",
      "unit": "umol/L",
      "reference_range": "208.3-428.4",
      "abnormal": false
    },
    {
      "name": "*葡萄糖",
      "item_code": "Glu",
      "value": "6.39",
      "unit": "mmol/L",
      "reference_range": "3.70-6.10",
      "abnormal": true
    },
    {
      "name": "*游离三碘甲状原氨酸",
      "item_code": "FT3",
      "value": "5.55",
      "unit": "pmol/L",
      "reference_range": "3.53-7.37",
      "abnormal": false
    },
    {
      "name": "*游离甲状腺素",
      "item_code": "FT4",
      "value": "11.03",
      "unit": "pmol/L",
      "reference_range": "7.98-19.24",
      "abnormal": false
    },
    {
      "name": "*促甲状腺刺激激素",
      "item_code": "s-TSH",
      "value": "1.397",
      "unit": "mIU/L",
      "reference_range": "0.340-5.600",
      "abnormal": false
    }
  ]
}
2026-08-10 16:31:15,799 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:31:15,799 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 0, \"bbox_end\": 157, \"encounter_dates\": [\"2026-03-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "门诊 & 2026-03-23 12:04 & 血常规(五分类) & G004 & 全血 & & & & & & \\\\\n门诊 & 2026-03-23 12:43 & PT,APTT & G029 & 血浆 & & & & & & \\\\\n\\multicolumn{11}{c}{共6份报告} \\\\\n\\hline\n\\end{tabular}\n\\begin{tabular}{ccccccccc}\n\\hline\n检验项目 & 分组 & 样本 & 中文名称 & 英文名称 & 结果 & 定性 & 参考值 & 单位 \\\\\n\\hline\nALT, AST, GGT, ALI & G001 & 血清 & N端-B型钠尿肽前体 & NT-proBNP & 191.85 & & <210.64 & ng/L \\\\\nTSH, FT3, FT4 & G001 & 血清 & C反应蛋白 & CRP & 1.15 & & <5.0 & mg/L \\\\\nT, CRP, NT-proBNP & G002 & 血清 & 降钙素原 & PCT & 0.04 & & <0.05 & ng/mL \\\\\n肌钙蛋白T & G002 & 血清 & & & & & & \\\\\n血常规(五分类) & G004 & 全血 & & & & & & \\\\\nPT, APTT & G029 & 血浆 & & & & & & \\\\\n\\hline\n\\end{tabular}\n\\begin{tabular}{cccccccccc}\n\\hline\n检验项目 & 分组 & 样本 & 中文名称 & 英文名称 & 结果 & 定性 & 参考值 & 单位 \\\\\n\\hline\nLT, AST, GGT, ALI & G001 & 血清 & 肌钙蛋白T & TnT & 5 & & $<14$ & ng/L \\\\",
    "role": "user"
  }
]
2026-08-10 16:31:18,482 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:31:18,482 INFO     29 [qwen-vl-table] page=3 LLM output (len=719):
{
  "report_date": "2026-03-23",
  "items": [
    {
      "name": "N端-B型钠尿肽前体",
      "item_code": "NT-proBNP",
      "value": "191.85",
      "unit": "ng/L",
      "reference_range": "<210.64",
      "abnormal": false
    },
    {
      "name": "C反应蛋白",
      "item_code": "CRP",
      "value": "1.15",
      "unit": "mg/L",
      "reference_range": "<5.0",
      "abnormal": false
    },
    {
      "name": "降钙素原",
      "item_code": "PCT",
      "value": "0.04",
      "unit": "ng/mL",
      "reference_range": "<0.05",
      "abnormal": false
    },
    {
      "name": "肌钙蛋白T",
      "item_code": "TnT",
      "value": "5",
      "unit": "ng/L",
      "reference_range": "<14",
      "abnormal": false
    }
  ]
}
2026-08-10 16:31:18,482 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:31:18,483 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 0, \"bbox_end\": 157, \"encounter_dates\": [\"2026-03-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "TSH, FT3, FT4 & G001 & 血清 & & & & & & \\\\\n, CRP, NT-proBNP & G002 & 血清 & & & & & & \\\\\n肌钙蛋白T & G002 & 血清 & & & & & & \\\\\n常规(五分类) & G004 & 全血 & & & & & & \\\\\nPT, APTT & G029 & 血浆 & & & & & & \\\\\n\\hline\n\\end{tabular}\n\\begin{tabular}{ccccccccc}\n\\hline\n检验项目 & 分组 & 样本 & 中文名称 & 英文名称 & 结果 & 定性 & 参考值 & 单位 \\\\\n\\hline\nLT, AST, GGT, ALI & G001 & 血清 & *白细胞计数 & WBC & 6.18 & & 3.5-9.5 & 10E9/L \\\\\nSH, FT3, FT4 & G001 & 血清 & 中性粒细胞百分比 & NE\\% & 64.8 & & 40-75 & \\% \\\\\nCRP, NT-proBNP & G002 & 血清 & 淋巴细胞百分比 & LY\\% & 23.3 & & 20-50 & \\% \\\\\n肌钙蛋白T & G002 & 血清 & 单核细胞百分比 & MO\\% & 7.7 & & 3-10 & \\% \\\\\n常规(五分类) & G004 & 全血 & 嗜酸粒细胞百分比 & EO\\% & 4.1 & & 0.4-8.0 & \\% \\\\\nPT, APTT & G029 & 血浆 & 嗜碱粒细胞百分比 & BA\\% & 0.1 & & 0-1 & \\% \\\\\n共6份报告 & & & 中性粒细胞绝对值 & NE\\# & 4.00 & & 1.8-6.3 & 10E9/L \\\\\n& & & 淋巴细胞绝对值 & LY\\# & 1.44 & & 1.1-3.2 & 10E9/L \\\\\n& & & 单核细胞绝对值 & MO\\# & 0.48 & & 0.1-0.6 & 10E9/L \\\\\n& & & 嗜酸粒细胞绝对值 & EO\\# & 0.25 & & 0.02-0.52 & 10E9/L \\\\\n& & & 嗜碱粒细胞绝对值 & BA\\# & 0.01 & & 0-0.06 & 10E9/L \\\\",
    "role": "user"
  }
]
2026-08-10 16:31:20,033 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:31:20.033+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 74, "failed": 0, "current": {"dca6cdea94d711f1bd9827cf206dfa2d": {"id": "dca6cdea94d711f1bd9827cf206dfa2d", "doc_id": "dbef275894d711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "size": 28457006, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786379026603, "task_type": "dataflow", "root_trace_id": "00f6a24fb6bd4742ba80c2030b932c44", "root_traceparent": "00-00f6a24fb6bd4742ba80c2030b932c44-fbfb6d98b4675b32-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:31:26,587 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:31:26,588 INFO     29 [qwen-vl-table] page=4 LLM output (len=1898):
{
  "report_date": "2026-03-23",
  "items": [
    {
      "name": "*白细胞计数",
      "item_code": "WBC",
      "value": "6.18",
      "unit": "10E9/L",
      "reference_range": "3.5-9.5",
      "abnormal": false
    },
    {
      "name": "中性粒细胞百分比",
      "item_code": "NE%",
      "value": "64.8",
      "unit": "%",
      "reference_range": "40-75",
      "abnormal": false
    },
    {
      "name": "淋巴细胞百分比",
      "item_code": "LY%",
      "value": "23.3",
      "unit": "%",
      "reference_range": "20-50",
      "abnormal": false
    },
    {
      "name": "单核细胞百分比",
      "item_code": "MO%",
      "value": "7.7",
      "unit": "%",
      "reference_range": "3-10",
      "abnormal": false
    },
    {
      "name": "嗜酸粒细胞百分比",
      "item_code": "EO%",
      "value": "4.1",
      "unit": "%",
      "reference_range": "0.4-8.0",
      "abnormal": false
    },
    {
      "name": "嗜碱粒细胞百分比",
      "item_code": "BA%",
      "value": "0.1",
      "unit": "%",
      "reference_range": "0-1",
      "abnormal": false
    },
    {
      "name": "中性粒细胞绝对值",
      "item_code": "NE#",
      "value": "4.00",
      "unit": "10E9/L",
      "reference_range": "1.8-6.3",
      "abnormal": false
    },
    {
      "name": "淋巴细胞绝对值",
      "item_code": "LY#",
      "value": "1.44",
      "unit": "10E9/L",
      "reference_range": "1.1-3.2",
      "abnormal": false
    },
    {
      "name": "单核细胞绝对值",
      "item_code": "MO#",
      "value": "0.48",
      "unit": "10E9/L",
      "reference_range": "0.1-0.6",
      "abnormal": false
    },
    {
      "name": "嗜酸粒细胞绝对值",
      "item_code": "EO#",
      "value": "0.25",
      "unit": "10E9/L",
      "reference_range": "0.02-0.52",
      "abnormal": false
    },
    {
      "name": "嗜碱粒细胞绝对值",
      "item_code": "BA#",
      "value": "0.01",
      "unit": "10E9/L",
      "reference_range": "0-0.06",
      "abnormal": false
    }
  ]
}
2026-08-10 16:31:26,588 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:31:26,588 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 0, \"bbox_end\": 157, \"encounter_dates\": [\"2026-03-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "& & & *红细胞计数 & RBC & 4.26 & $\\downarrow$ & 4.3-5.8 & 10E12/L \\\\\n& & & *血红蛋白 & Hb & 132 & & 130-175 & g/L \\\\\n& & & *红细胞压积 & HCT & 40.6 & & 40-50 & \\% \\\\\n& & & *平均RBC体积 & MCV & 95.2 & & 82-100 & fL \\\\\n& & & 平均RBC血红蛋白含量 & MCH & 30.9 & & 27-34 & pg \\\\\n& & & 平均RBC血红蛋白浓度 & MCHC & 325 & & 316-354 & g/L \\\\\n& & & 红细胞体积分布宽度 & RDW & 12.5 & & $<$15 & \\% \\\\\n\\hline\n\\end{tabular}\n\\begin{tabular}{cccccccccc}\n\\hline\n检验项目 & 分组 & 样本 & 中文名称 & 英文名称 & 结果 & 定性 & 参考值 & 单位 & \\\\\n\\hline\n,AST,GGT,ALI & G001 & 血清 & 嗜酸粒细胞百分比 & E0\\% & 4.1 & & 0.4-8.0 & \\% & \\\\\nH,FT3,FT4 & G001 & 血清 & 嗜碱粒细胞百分比 & BA\\% & 0.1 & & 0-1 & \\% & \\\\\nRP,NT-proBNP & G002 & 血清 & 中性粒细胞绝对值 & NE\\# & 4.00 & & 1.8-6.3 & 10E9/L & \\\\\n肌钙蛋白T & G002 & 血清 & 淋巴细胞绝对值 & LY\\# & 1.44 & & 1.1-3.2 & 10E9/L & \\\\\n规(五分类) & G004 & 全血 & 单核细胞绝对值 & MO\\# & 0.48 & & 0.1-0.6 & 10E9/L & \\\\\nPT,APTT & G029 & 血浆 & 嗜酸粒细胞绝对值 & EO\\# & 0.25 & & 0.02-0.52 & 10E9/L & \\\\\n共6份报告 & & & 嗜碱粒细胞绝对值 & BA\\# & 0.01 & & 0-0.06 & 10E9/L & \\\\\n& & & *红细胞计数 & RBC & 4.26 & $\\downarrow$ & 4.3-5.8 & 10E12/L & \\\\\n& & & *血红蛋白 & Hb & 132 & & 130-175 & g/L & \\\\",
    "role": "user"
  }
]
2026-08-10 16:31:34,223 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:31:34,223 INFO     29 [qwen-vl-table] page=5 LLM output (len=2402):
{
  "report_date": "2026-03-23",
  "items": [
    {
      "name": "红细胞计数",
      "item_code": "RBC",
      "value": "4.26",
      "unit": "10E12/L",
      "reference_range": "4.3-5.8",
      "abnormal": true
    },
    {
      "name": "血红蛋白",
      "item_code": "Hb",
      "value": "132",
      "unit": "g/L",
      "reference_range": "130-175",
      "abnormal": false
    },
    {
      "name": "红细胞压积",
      "item_code": "HCT",
      "value": "40.6",
      "unit": "%",
      "reference_range": "40-50",
      "abnormal": false
    },
    {
      "name": "平均RBC体积",
      "item_code": "MCV",
      "value": "95.2",
      "unit": "fL",
      "reference_range": "82-100",
      "abnormal": false
    },
    {
      "name": "平均RBC血红蛋白含量",
      "item_code": "MCH",
      "value": "30.9",
      "unit": "pg",
      "reference_range": "27-34",
      "abnormal": false
    },
    {
      "name": "平均RBC血红蛋白浓度",
      "item_code": "MCHC",
      "value": "325",
      "unit": "g/L",
      "reference_range": "316-354",
      "abnormal": false
    },
    {
      "name": "红细胞体积分布宽度",
      "item_code": "RDW",
      "value": "12.5",
      "unit": "%",
      "reference_range": "<15",
      "abnormal": false
    },
    {
      "name": "嗜酸粒细胞百分比",
      "item_code": "E0%",
      "value": "4.1",
      "unit": "%",
      "reference_range": "0.4-8.0",
      "abnormal": false
    },
    {
      "name": "嗜碱粒细胞百分比",
      "item_code": "BA%",
      "value": "0.1",
      "unit": "%",
      "reference_range": "0-1",
      "abnormal": false
    },
    {
      "name": "中性粒细胞绝对值",
      "item_code": "NE#",
      "value": "4.00",
      "unit": "10E9/L",
      "reference_range": "1.8-6.3",
      "abnormal": false
    },
    {
      "name": "淋巴细胞绝对值",
      "item_code": "LY#",
      "value": "1.44",
      "unit": "10E9/L",
      "reference_range": "1.1-3.2",
      "abnormal": false
    },
    {
      "name": "单核细胞绝对值",
      "item_code": "MO#",
      "value": "0.48",
      "unit": "10E9/L",
      "reference_range": "0.1-0.6",
      "abnormal": false
    },
    {
      "name": "嗜酸粒细胞绝对值",
      "item_code": "EO#",
      "value": "0.25",
      "unit": "10E9/L",
      "reference_range": "0.02-0.52",
      "abnormal": false
    },
    {
      "name": "嗜碱粒细胞绝对值",
      "item_code": "BA#",
      "value": "0.01",
      "unit": "10E9/L",
      "reference_range": "0-0.06",
      "abnormal": false
    }
  ]
}
2026-08-10 16:31:34,224 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:31:34,224 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 0, \"bbox_end\": 157, \"encounter_dates\": [\"2026-03-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "& & & *红细胞压积 & HCT & 40.6 & & 40-50 & \\% & \\\\\n& & & *平均RBC体积 & MCV & 95.2 & & 82-100 & fL & \\\\\n& & & 平均RBC血红蛋白含量 & MCH & 30.9 & & 27-34 & pg & \\\\\n& & & 平均RBC血红蛋白浓度 & MCHC & 325 & & 316-354 & g/L & \\\\\n\\hline\n\\rowcolor{blue!20}\n红细胞体积分布宽度 & & & & RDW & 12.5 & & $<$15 & \\% & \\\\\n\\hline\n& & & *血小板计数 & PLT & 166 & & 125-350 & 10E9/L & \\\\\n& & & 平均血小板体积 & MPV & 8.90 & & 8.0-15.0 & fL & \\\\\n& & & 血小板压积 & PCT & 0.147 & & 0.100-0.250 & \\% & \\\\\n& & & 血小板体积分布宽度 & PDW & 15.9 & & 14.0-18.0 & \\% & \\\\\n\\hline\n\\end{tabular}\n\\begin{tabular}{llllllllll}\n\\hline\n项目 & 分组 & 样本 & 中文名称 & 英文名称 & 结果 & 定性 & 参考值 & 单位 & \\\\\n\\hline\nT,GGT,ALI & G001 & 血清 & *凝血酶原时间 & PT & 12.3 & & 9.8-12.9 & s & \\\\\nT3,FT4 & G001 & 血清 & PT国际标准化比率 & INR & 1.07 & & 0.82-1.20 & & \\\\\nNT-proBNP & G002 & 血清 & *活化部分凝血酶原时间 & APTT & 28.3 & & 23.3-32.5 & s & \\\\\n蛋白T & G002 & 血清 & & & & & & & \\\\\n(五分类) & G004 & 全血 & & & & & & & \\\\\nAPTT & G029 & 血浆 & & & & & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 16:31:40,757 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:31:40,757 INFO     29 [qwen-vl-table] page=6 LLM output (len=2058):
{
  "report_date": null,
  "items": [
    {
      "name": "红细胞压积",
      "item_code": "HCT",
      "value": "40.6",
      "unit": "%",
      "reference_range": "40-50",
      "abnormal": false
    },
    {
      "name": "平均RBC体积",
      "item_code": "MCV",
      "value": "95.2",
      "unit": "fL",
      "reference_range": "82-100",
      "abnormal": false
    },
    {
      "name": "平均RBC血红蛋白含量",
      "item_code": "MCH",
      "value": "30.9",
      "unit": "pg",
      "reference_range": "27-34",
      "abnormal": false
    },
    {
      "name": "平均RBC血红蛋白浓度",
      "item_code": "MCHC",
      "value": "325",
      "unit": "g/L",
      "reference_range": "316-354",
      "abnormal": false
    },
    {
      "name": "红细胞体积分布宽度",
      "item_code": "RDW",
      "value": "12.5",
      "unit": "%",
      "reference_range": "<15",
      "abnormal": false
    },
    {
      "name": "血小板计数",
      "item_code": "PLT",
      "value": "166",
      "unit": "10E9/L",
      "reference_range": "125-350",
      "abnormal": false
    },
    {
      "name": "平均血小板体积",
      "item_code": "MPV",
      "value": "8.90",
      "unit": "fL",
      "reference_range": "8.0-15.0",
      "abnormal": false
    },
    {
      "name": "血小板压积",
      "item_code": "PCT",
      "value": "0.147",
      "unit": "%",
      "reference_range": "0.100-0.250",
      "abnormal": false
    },
    {
      "name": "血小板体积分布宽度",
      "item_code": "PDW",
      "value": "15.9",
      "unit": "%",
      "reference_range": "14.0-18.0",
      "abnormal": false
    },
    {
      "name": "凝血酶原时间",
      "item_code": "PT",
      "value": "12.3",
      "unit": "s",
      "reference_range": "9.8-12.9",
      "abnormal": false
    },
    {
      "name": "PT国际标准化比率",
      "item_code": "INR",
      "value": "1.07",
      "unit": null,
      "reference_range": "0.82-1.20",
      "abnormal": false
    },
    {
      "name": "活化部分凝血酶原时间",
      "item_code": "APTT",
      "value": "28.3",
      "unit": "s",
      "reference_range": "23.3-32.5",
      "abnormal": false
    }
  ]
}
2026-08-10 16:31:40,757 INFO     29 [qwen-vl-table] coord grouping: {0: 14, 1: 3, 2: 3, 4: 30, 5: 4, 6: 3}
2026-08-10 16:31:40,778 INFO     29 [qwen-vl-table] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=10522495, prompt_len=580
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
白蛋白、总胆红素、直接胆红素、间接胆红素、谷丙转氨酶、谷草转氨酶、γ谷氨酰转肽酶、乳酸脱氢酶、尿素、肌酐、尿素/肌酐、*尿酸、*葡萄糖、肌钙蛋白T

## 规则
1. 对于列表中的每个名称，找到它在图片中出现的位置
2. bbox为该名称文字的最小包围框，坐标归一化到0-1000，格式[x1,y1,x2,y2]
3. 如果某个名称在图片中未找到，可以跳过不输出
4. text字段必须与给定的名称完全一致，不要修改或缩写

## 严格JSON格式要求
直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。
正确示例：
[
  {"text": "C反应蛋白", "bbox": [100, 200, 400, 230]},
  {"text": "白细胞计数", "bbox": [100, 250, 400, 280]}
]
错误示例（禁止额外字段）：
[
  {"text": "C反应蛋白", "bbox": [100, 200, 400, 230], "label": "检验项"}
]
请直接输出纯JSON数组，不要用markdown代码块包裹。
2026-08-10 16:31:52,554 INFO     29 [qwen-vl-table] coord API raw response (len=692):
[
	{"text": "白蛋白", "bbox": [398, 137, 437, 160]},
	{"text": "总胆红素", "bbox": [398, 178, 443, 201]},
	{"text": "直接胆红素", "bbox": [398, 219, 454, 242]},
	{"text": "间接胆红素", "bbox": [398, 259, 454, 282]},
	{"text": "谷丙转氨酶", "bbox": [398, 300, 460, 323]},
	{"text": "谷草转氨酶", "bbox": [398, 340, 460, 363]},
	{"text": "γ谷氨酰转肽酶", "bbox": [398, 419, 483, 442]},
	{"text": "乳酸脱氢酶", "bbox": [398, 497, 460, 520]},
	{"text": "尿素", "bbox": [398, 537, 424, 560]},
	{"text": "肌酐", "bbox": [398, 578, 420, 600]},
	{"text": "尿素/肌酐", "bbox": [398, 618, 448, 641]},
	{"text": "*尿酸", "bbox": [398, 658, 424, 681]},
	{"text": "*葡萄糖", "bbox": [398, 698, 436, 721]},
	{"text": "肌钙蛋白T", "bbox": [206, 259, 263, 282]}
]
2026-08-10 16:31:52,555 INFO     29 [qwen-vl-table] coord API: raw_items=14, valid_items=14, elapsed=11.8s
2026-08-10 16:31:52,555 INFO     29 [qwen-vl-table] coord item[0]: text=白蛋白, bbox=[398, 137, 437, 160]
2026-08-10 16:31:52,555 INFO     29 [qwen-vl-table] coord item[1]: text=总胆红素, bbox=[398, 178, 443, 201]
2026-08-10 16:31:52,555 INFO     29 [qwen-vl-table] coord item[2]: text=直接胆红素, bbox=[398, 219, 454, 242]
2026-08-10 16:31:52,555 INFO     29 [qwen-vl-table] coord item[3]: text=间接胆红素, bbox=[398, 259, 454, 282]
2026-08-10 16:31:52,555 INFO     29 [qwen-vl-table] coord item[4]: text=谷丙转氨酶, bbox=[398, 300, 460, 323]
2026-08-10 16:31:52,555 INFO     29 [qwen-vl-table] coord item[5]: text=谷草转氨酶, bbox=[398, 340, 460, 363]
2026-08-10 16:31:52,555 INFO     29 [qwen-vl-table] coord item[6]: text=γ谷氨酰转肽酶, bbox=[398, 419, 483, 442]
2026-08-10 16:31:52,555 INFO     29 [qwen-vl-table] coord item[7]: text=乳酸脱氢酶, bbox=[398, 497, 460, 520]
2026-08-10 16:31:52,555 INFO     29 [qwen-vl-table] coord item[8]: text=尿素, bbox=[398, 537, 424, 560]
2026-08-10 16:31:52,556 INFO     29 [qwen-vl-table] coord item[9]: text=肌酐, bbox=[398, 578, 420, 600]
2026-08-10 16:31:52,556 INFO     29 [qwen-vl-table] coord item[10]: text=尿素/肌酐, bbox=[398, 618, 448, 641]
2026-08-10 16:31:52,556 INFO     29 [qwen-vl-table] coord item[11]: text=*尿酸, bbox=[398, 658, 424, 681]
2026-08-10 16:31:52,556 INFO     29 [qwen-vl-table] coord item[12]: text=*葡萄糖, bbox=[398, 698, 436, 721]
2026-08-10 16:31:52,556 INFO     29 [qwen-vl-table] coord item[13]: text=肌钙蛋白T, bbox=[206, 259, 263, 282]
2026-08-10 16:31:52,559 INFO     29 [qwen-vl-table] page=0 coord: matched 14/14, time=11.8s
2026-08-10 16:31:52,580 INFO     29 [qwen-vl-table] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=10206893, prompt_len=535
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
*游离三碘甲状原氨酸、*游离甲状腺素、*促甲状腺刺激激素

## 规则
1. 对于列表中的每个名称，找到它在图片中出现的位置
2. bbox为该名称文字的最小包围框，坐标归一化到0-1000，格式[x1,y1,x2,y2]
3. 如果某个名称在图片中未找到，可以跳过不输出
4. text字段必须与给定的名称完全一致，不要修改或缩写

## 严格JSON格式要求
直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。
正确示例：
[
  {"text": "C反应蛋白", "bbox": [100, 200, 400, 230]},
  {"text": "白细胞计数", "bbox": [100, 250, 400, 280]}
]
错误示例（禁止额外字段）：
[
  {"text": "C反应蛋白", "bbox": [100, 200, 400, 230], "label": "检验项"}
]
请直接输出纯JSON数组，不要用markdown代码块包裹。
2026-08-10 16:32:03,806 INFO     29 [qwen-vl-table] coord API raw response (len=163):
[
	{"text": "*游离三碘甲状原氨酸", "bbox": [380, 107, 496, 133]},
	{"text": "*游离甲状腺素", "bbox": [380, 148, 459, 174]},
	{"text": "*促甲状腺刺激激素", "bbox": [380, 188, 483, 214]}
]
2026-08-10 16:32:03,806 INFO     29 [qwen-vl-table] coord API: raw_items=3, valid_items=3, elapsed=11.2s
2026-08-10 16:32:03,806 INFO     29 [qwen-vl-table] coord item[0]: text=*游离三碘甲状原氨酸, bbox=[380, 107, 496, 133]
2026-08-10 16:32:03,806 INFO     29 [qwen-vl-table] coord item[1]: text=*游离甲状腺素, bbox=[380, 148, 459, 174]
2026-08-10 16:32:03,806 INFO     29 [qwen-vl-table] coord item[2]: text=*促甲状腺刺激激素, bbox=[380, 188, 483, 214]
2026-08-10 16:32:03,809 INFO     29 [qwen-vl-table] page=1 coord: matched 3/3, time=11.2s
2026-08-10 16:32:03,841 INFO     29 [qwen-vl-table] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=12383648, prompt_len=528
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
N端-B型钠尿肽前体、C反应蛋白、降钙素原

## 规则
1. 对于列表中的每个名称，找到它在图片中出现的位置
2. bbox为该名称文字的最小包围框，坐标归一化到0-1000，格式[x1,y1,x2,y2]
3. 如果某个名称在图片中未找到，可以跳过不输出
4. text字段必须与给定的名称完全一致，不要修改或缩写

## 严格JSON格式要求
直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。
正确示例：
[
  {"text": "C反应蛋白", "bbox": [100, 200, 400, 230]},
  {"text": "白细胞计数", "bbox": [100, 250, 400, 280]}
]
错误示例（禁止额外字段）：
[
  {"text": "C反应蛋白", "bbox": [100, 200, 400, 230], "label": "检验项"}
]
请直接输出纯JSON数组，不要用markdown代码块包裹。
2026-08-10 16:32:13,599 INFO     29 [qwen-vl-table] coord API raw response (len=156):
[
	{"text": "N端-B型钠尿肽前体", "bbox": [236, 144, 354, 169]},
	{"text": "C反应蛋白", "bbox": [236, 184, 298, 208]},
	{"text": "降钙素原", "bbox": [236, 224, 292, 248]}
]
2026-08-10 16:32:13,599 INFO     29 [qwen-vl-table] coord API: raw_items=3, valid_items=3, elapsed=9.8s
2026-08-10 16:32:13,600 INFO     29 [qwen-vl-table] coord item[0]: text=N端-B型钠尿肽前体, bbox=[236, 144, 354, 169]
2026-08-10 16:32:13,600 INFO     29 [qwen-vl-table] coord item[1]: text=C反应蛋白, bbox=[236, 184, 298, 208]
2026-08-10 16:32:13,600 INFO     29 [qwen-vl-table] coord item[2]: text=降钙素原, bbox=[236, 224, 292, 248]
2026-08-10 16:32:13,603 INFO     29 [qwen-vl-table] page=2 coord: matched 3/3, time=9.8s
2026-08-10 16:32:13,626 INFO     29 [qwen-vl-table] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=10897637, prompt_len=767
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
*白细胞计数、中性粒细胞百分比、淋巴细胞百分比、单核细胞百分比、嗜酸粒细胞百分比、嗜碱粒细胞百分比、中性粒细胞绝对值、淋巴细胞绝对值、单核细胞绝对值、嗜酸粒细胞绝对值、嗜碱粒细胞绝对值、红细胞计数、血红蛋白、红细胞压积、平均RBC体积、平均RBC血红蛋白含量、平均RBC血红蛋白浓度、红细胞体积分布宽度、嗜酸粒细胞百分比、嗜碱粒细胞百分比、中性粒细胞绝对值、淋巴细胞绝对值、单核细胞绝对值、嗜酸粒细胞绝对值、嗜碱粒细胞绝对值、红细胞压积、平均RBC体积、平均RBC血红蛋白含量、平均RBC血红蛋白浓度、红细胞体积分布宽度

## 规则
1. 对于列表中的每个名称，找到它在图片中出现的位置
2. bbox为该名称文字的最小包围框，坐标归一化到0-1000，格式[x1,y1,x2,y2]
3. 如果某个名称在图片中未找到，可以跳过不输出
4. text字段必须与给定的名称完全一致，不要修改或缩写

## 严格JSON格式要求
直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。
正确示例：
[
  {"text": "C反应蛋白", "bbox": [100, 200, 400, 230]},
  {"text": "白细胞计数", "bbox": [100, 250, 400, 280]}
]
错误示例（禁止额外字段）：
[
  {"text": "C反应蛋白", "bbox": [100, 200, 400, 230], "label": "检验项"}
]
请直接输出纯JSON数组，不要用markdown代码块包裹。
2026-08-10 16:32:31,847 INFO     29 [qwen-vl-table] coord API raw response (len=1582):
[
	{"text": "白细胞计数", "bbox": [224, 147, 302, 170]},
	{"text": "中性粒细胞百分比", "bbox": [224, 185, 337, 208]},
	{"text": "淋巴细胞百分比", "bbox": [224, 222, 322, 245]},
	{"text": "单核细胞百分比", "bbox": [224, 260, 322, 283]},
	{"text": "嗜酸粒细胞百分比", "bbox": [224, 300, 337, 323]},
	{"text": "嗜碱粒细胞百分比", "bbox": [224, 338, 337, 361]},
	{"text": "中性粒细胞绝对值", "bbox": [224, 377, 337, 400]},
	{"text": "淋巴细胞绝对值", "bbox": [224, 415, 322, 438]},
	{"text": "单核细胞绝对值", "bbox": [224, 453, 322, 476]},
	{"text": "嗜酸粒细胞绝对值", "bbox": [224, 492, 337, 515]},
	{"text": "嗜碱粒细胞绝对值", "bbox": [224, 530, 337, 553]},
	{"text": "红细胞计数", "bbox": [224, 569, 300, 592]},
	{"text": "血红蛋白", "bbox": [224, 608, 286, 631]},
	{"text": "红细胞压积", "bbox": [224, 647, 299, 670]},
	{"text": "平均RBC体积", "bbox": [224, 686, 305, 709]},
	{"text": "平均RBC血红蛋白含量", "bbox": [224, 724, 353, 747]},
	{"text": "平均RBC血红蛋白浓度", "bbox": [224, 762, 353, 785]},
	{"text": "红细胞体积分布宽度", "bbox": [224, 801, 345, 824]},
	{"text": "嗜酸粒细胞百分比", "bbox": [224, 300, 337, 323]},
	{"text": "嗜碱粒细胞百分比", "bbox": [224, 338, 337, 361]},
	{"text": "中性粒细胞绝对值", "bbox": [224, 377, 337, 400]},
	{"text": "淋巴细胞绝对值", "bbox": [224, 415, 322, 438]},
	{"text": "单核细胞绝对值", "bbox": [224, 453, 322, 476]},
	{"text": "嗜酸粒细胞绝对值", "bbox": [224, 492, 337, 515]},
	{"text": "嗜碱粒细胞绝对值", "bbox": [224, 530, 337, 553]},
	{"text": "红细胞压积", "bbox": [224, 647, 299, 670]},
	{"text": "平均RBC体积", "bbox": [224, 686, 305, 709]},
	{"text": "平均RBC血红蛋白含量", "bbox": [224, 724, 353, 747]},
	{"text": "平均RBC血红蛋白浓度", "bbox": [224, 762, 353, 785]},
	{"text": "红细胞体积分布宽度", "bbox": [224, 801, 345, 824]}
]
2026-08-10 16:32:31,848 INFO     29 [qwen-vl-table] coord API: raw_items=30, valid_items=30, elapsed=18.2s
2026-08-10 16:32:31,848 INFO     29 [qwen-vl-table] coord item[0]: text=白细胞计数, bbox=[224, 147, 302, 170]
2026-08-10 16:32:31,848 INFO     29 [qwen-vl-table] coord item[1]: text=中性粒细胞百分比, bbox=[224, 185, 337, 208]
2026-08-10 16:32:31,848 INFO     29 [qwen-vl-table] coord item[2]: text=淋巴细胞百分比, bbox=[224, 222, 322, 245]
2026-08-10 16:32:31,848 INFO     29 [qwen-vl-table] coord item[3]: text=单核细胞百分比, bbox=[224, 260, 322, 283]
2026-08-10 16:32:31,848 INFO     29 [qwen-vl-table] coord item[4]: text=嗜酸粒细胞百分比, bbox=[224, 300, 337, 323]
2026-08-10 16:32:31,848 INFO     29 [qwen-vl-table] coord item[5]: text=嗜碱粒细胞百分比, bbox=[224, 338, 337, 361]
2026-08-10 16:32:31,848 INFO     29 [qwen-vl-table] coord item[6]: text=中性粒细胞绝对值, bbox=[224, 377, 337, 400]
2026-08-10 16:32:31,848 INFO     29 [qwen-vl-table] coord item[7]: text=淋巴细胞绝对值, bbox=[224, 415, 322, 438]
2026-08-10 16:32:31,848 INFO     29 [qwen-vl-table] coord item[8]: text=单核细胞绝对值, bbox=[224, 453, 322, 476]
2026-08-10 16:32:31,848 INFO     29 [qwen-vl-table] coord item[9]: text=嗜酸粒细胞绝对值, bbox=[224, 492, 337, 515]
2026-08-10 16:32:31,848 INFO     29 [qwen-vl-table] coord item[10]: text=嗜碱粒细胞绝对值, bbox=[224, 530, 337, 553]
2026-08-10 16:32:31,848 INFO     29 [qwen-vl-table] coord item[11]: text=红细胞计数, bbox=[224, 569, 300, 592]
2026-08-10 16:32:31,848 INFO     29 [qwen-vl-table] coord item[12]: text=血红蛋白, bbox=[224, 608, 286, 631]
2026-08-10 16:32:31,848 INFO     29 [qwen-vl-table] coord item[13]: text=红细胞压积, bbox=[224, 647, 299, 670]
2026-08-10 16:32:31,849 INFO     29 [qwen-vl-table] coord item[14]: text=平均RBC体积, bbox=[224, 686, 305, 709]
2026-08-10 16:32:31,849 INFO     29 [qwen-vl-table] coord item[15]: text=平均RBC血红蛋白含量, bbox=[224, 724, 353, 747]
2026-08-10 16:32:31,849 INFO     29 [qwen-vl-table] coord item[16]: text=平均RBC血红蛋白浓度, bbox=[224, 762, 353, 785]
2026-08-10 16:32:31,849 INFO     29 [qwen-vl-table] coord item[17]: text=红细胞体积分布宽度, bbox=[224, 801, 345, 824]
2026-08-10 16:32:31,849 INFO     29 [qwen-vl-table] coord item[18]: text=嗜酸粒细胞百分比, bbox=[224, 300, 337, 323]
2026-08-10 16:32:31,849 INFO     29 [qwen-vl-table] coord item[19]: text=嗜碱粒细胞百分比, bbox=[224, 338, 337, 361]
2026-08-10 16:32:31,849 INFO     29 [qwen-vl-table] coord item[20]: text=中性粒细胞绝对值, bbox=[224, 377, 337, 400]
2026-08-10 16:32:31,849 INFO     29 [qwen-vl-table] coord item[21]: text=淋巴细胞绝对值, bbox=[224, 415, 322, 438]
2026-08-10 16:32:31,849 INFO     29 [qwen-vl-table] coord item[22]: text=单核细胞绝对值, bbox=[224, 453, 322, 476]
2026-08-10 16:32:31,849 INFO     29 [qwen-vl-table] coord item[23]: text=嗜酸粒细胞绝对值, bbox=[224, 492, 337, 515]
2026-08-10 16:32:31,849 INFO     29 [qwen-vl-table] coord item[24]: text=嗜碱粒细胞绝对值, bbox=[224, 530, 337, 553]
2026-08-10 16:32:31,849 INFO     29 [qwen-vl-table] coord item[25]: text=红细胞压积, bbox=[224, 647, 299, 670]
2026-08-10 16:32:31,849 INFO     29 [qwen-vl-table] coord item[26]: text=平均RBC体积, bbox=[224, 686, 305, 709]
2026-08-10 16:32:31,849 INFO     29 [qwen-vl-table] coord item[27]: text=平均RBC血红蛋白含量, bbox=[224, 724, 353, 747]
2026-08-10 16:32:31,849 INFO     29 [qwen-vl-table] coord item[28]: text=平均RBC血红蛋白浓度, bbox=[224, 762, 353, 785]
2026-08-10 16:32:31,849 INFO     29 [qwen-vl-table] coord item[29]: text=红细胞体积分布宽度, bbox=[224, 801, 345, 824]
2026-08-10 16:32:31,851 INFO     29 [qwen-vl-table] page=4 coord: matched 30/30, time=18.2s
2026-08-10 16:32:31,874 INFO     29 [qwen-vl-table] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=11502158, prompt_len=536
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
血小板计数、平均血小板体积、血小板压积、血小板体积分布宽度

## 规则
1. 对于列表中的每个名称，找到它在图片中出现的位置
2. bbox为该名称文字的最小包围框，坐标归一化到0-1000，格式[x1,y1,x2,y2]
3. 如果某个名称在图片中未找到，可以跳过不输出
4. text字段必须与给定的名称完全一致，不要修改或缩写

## 严格JSON格式要求
直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。
正确示例：
[
  {"text": "C反应蛋白", "bbox": [100, 200, 400, 230]},
  {"text": "白细胞计数", "bbox": [100, 250, 400, 280]}
]
错误示例（禁止额外字段）：
[
  {"text": "C反应蛋白", "bbox": [100, 200, 400, 230], "label": "检验项"}
]
请直接输出纯JSON数组，不要用markdown代码块包裹。
2026-08-10 16:32:41,601 INFO     29 [qwen-vl-table] coord API raw response (len=251):
```json
[
	{"text": "血小板计数", "bbox": [228, 667, 311, 692]},
	{"text": "平均血小板体积", "bbox": [228, 708, 333, 732],
	"bbox": [228, 708, 333, 732]},
	{"text": "血小板压积", "bbox": [228, 748, 303, 772]},
	{"text": "血小板体积分布宽度", "bbox": [228, 788, 362, 813]}
]
```
2026-08-10 16:32:41,601 INFO     29 [qwen-vl-table] coord API: raw_items=4, valid_items=4, elapsed=9.7s
2026-08-10 16:32:41,601 INFO     29 [qwen-vl-table] coord item[0]: text=血小板计数, bbox=[228, 667, 311, 692]
2026-08-10 16:32:41,601 INFO     29 [qwen-vl-table] coord item[1]: text=平均血小板体积, bbox=[228, 708, 333, 732]
2026-08-10 16:32:41,601 INFO     29 [qwen-vl-table] coord item[2]: text=血小板压积, bbox=[228, 748, 303, 772]
2026-08-10 16:32:41,601 INFO     29 [qwen-vl-table] coord item[3]: text=血小板体积分布宽度, bbox=[228, 788, 362, 813]
2026-08-10 16:32:41,604 INFO     29 [qwen-vl-table] page=5 coord: matched 4/4, time=9.7s
2026-08-10 16:32:41,633 INFO     29 [qwen-vl-table] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=14037697, prompt_len=534
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
凝血酶原时间、PT国际标准化比率、活化部分凝血酶原时间

## 规则
1. 对于列表中的每个名称，找到它在图片中出现的位置
2. bbox为该名称文字的最小包围框，坐标归一化到0-1000，格式[x1,y1,x2,y2]
3. 如果某个名称在图片中未找到，可以跳过不输出
4. text字段必须与给定的名称完全一致，不要修改或缩写

## 严格JSON格式要求
直接输出JSON数组，每个元素只包含text和bbox两个字段，不要添加任何其他字段。
正确示例：
[
  {"text": "C反应蛋白", "bbox": [100, 200, 400, 230]},
  {"text": "白细胞计数", "bbox": [100, 250, 400, 280]}
]
错误示例（禁止额外字段）：
[
  {"text": "C反应蛋白", "bbox": [100, 200, 400, 230], "label": "检验项"}
]
请直接输出纯JSON数组，不要用markdown代码块包裹。
2026-08-10 16:32:51,680 INFO     29 [qwen-vl-table] coord API raw response (len=162):
[
	{"text": "凝血酶原时间", "bbox": [224, 133, 320, 157]},
	{"text": "PT国际标准化比率", "bbox": [220, 172, 343, 196]},
	{"text": "活化部分凝血酶原时间", "bbox": [222, 210, 380, 234]}
]
2026-08-10 16:32:51,680 INFO     29 [qwen-vl-table] coord API: raw_items=3, valid_items=3, elapsed=10.0s
2026-08-10 16:32:51,680 INFO     29 [qwen-vl-table] coord item[0]: text=凝血酶原时间, bbox=[224, 133, 320, 157]
2026-08-10 16:32:51,680 INFO     29 [qwen-vl-table] coord item[1]: text=PT国际标准化比率, bbox=[220, 172, 343, 196]
2026-08-10 16:32:51,680 INFO     29 [qwen-vl-table] coord item[2]: text=活化部分凝血酶原时间, bbox=[222, 210, 380, 234]
2026-08-10 16:32:51,682 INFO     29 [qwen-vl-table] page=6 coord: matched 3/3, time=10.0s
2026-08-10 16:32:51,682 INFO     29 [qwen-vl-table] new_positions (57):
[[1, 1198.776, 1316.244, 228.10500000000002, 266.4], [1, 1198.776, 1334.316, 296.37, 334.665], [1, 1198.776, 1367.448, 364.635, 402.93], [1, 1198.776, 1367.448, 431.235, 469.53000000000003], [1, 1198.776, 1385.52, 499.5, 537.795], [1, 1198.776, 1385.52, 566.1, 604.395], [1, 1198.776, 1454.796, 697.635, 735.9300000000001], [1, 1198.776, 1385.52, 827.505, 865.8000000000001], [1, 1198.776, 1277.088, 894.105, 932.4], [1, 1198.776, 1265.04, 962.37, 999.0], [1, 1198.776, 1349.376, 1028.97, 1067.265], [1, 1198.776, 1277.088, 1095.57, 1133.865], [1, 1198.776, 1313.232, 1162.17, 1200.465], [1, 620.472, 792.156, 431.235, 469.53000000000003], [2, 1144.18, 1493.4560000000001, 193.135, 240.065], [2, 1144.18, 1382.049, 267.14, 314.07], [2, 1144.18, 1454.313, 339.34, 386.27], [3, 712.2479999999999, 1068.3719999999998, 271.584, 318.734], [3, 712.2479999999999, 899.3639999999999, 347.024, 392.28799999999995], [3, 712.2479999999999, 881.256, 422.464, 467.72799999999995], [5, 682.752, 920.496, 286.797, 331.67], [5, 682.752, 1027.176, 360.935, 405.808], [5, 682.752, 981.456, 433.122, 477.995], [5, 682.752, 981.456, 507.26, 552.133], [5, 682.752, 1027.176, 585.3000000000001, 630.173], [5, 682.752, 1027.176, 659.438, 704.311], [5, 682.752, 1027.176, 735.527, 780.4], [5, 682.752, 981.456, 809.6650000000001, 854.538], [5, 682.752, 981.456, 883.803, 928.676], [5, 682.752, 1027.176, 959.892, 1004.765], [5, 682.752, 1027.176, 1034.03, 1078.903], [5, 682.752, 914.4, 1110.1190000000001, 1154.992], [5, 682.752, 871.7280000000001, 1186.208, 1231.0810000000001], [5, 682.752, 911.352, 1262.297, 1307.17], [5, 682.752, 929.64, 1338.386, 1383.259], [5, 682.752, 1075.944, 1412.5240000000001, 1457.3970000000002], [5, 682.752, 1075.944, 1486.662, 1531.535], [5, 682.752, 1051.56, 1562.751, 1607.624], [5, 682.752, 1027.176, 585.3000000000001, 630.173], [5, 682.752, 1027.176, 659.438, 704.311], [5, 682.752, 1027.176, 735.527, 780.4], [5, 682.752, 981.456, 809.6650000000001, 854.538], [5, 682.752, 981.456, 883.803, 928.676], [5, 682.752, 1027.176, 959.892, 1004.765], [5, 682.752, 1027.176, 1034.03, 1078.903], [5, 682.752, 911.352, 1262.297, 1307.17], [5, 682.752, 929.64, 1338.386, 1383.259], [5, 682.752, 1075.944, 1412.5240000000001, 1457.3970000000002], [5, 682.752, 1075.944, 1486.662, 1531.535], [5, 682.752, 1051.56, 1562.751, 1607.624], [6, 684.0, 933.0, 1322.661, 1372.236], [6, 684.0, 999.0, 1403.9640000000002, 1451.556], [6, 684.0, 909.0, 1483.284, 1530.876], [6, 684.0, 1086.0, 1562.604, 1612.179], [7, 684.096, 977.28, 285.01899999999995, 336.45099999999996], [7, 671.88, 1047.522, 368.59599999999995, 420.02799999999996], [7, 677.9879999999999, 1160.52, 450.03, 501.46199999999993]]
2026-08-10 16:32:51,682 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=57, matched=57, pages=7, time=114.8s
2026-08-10 16:32:51,704 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 16:32:51,704 INFO     29 [Trace] task=dca6cdea | doc=LBZH，男，63岁，胃癌一线(1).pdf | Extractor:LabExam | outputs={"chunks": "1 items, types={'LabReport': 1}", "html": "", "json": "523 items", "markdown": "", "text": "", "name": "LBZH，男，63岁，胃癌一线(1).pdf", "output_format": "chunks", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_LabExam\": 1, \"chunks_Examination\": 4, \"chunks_Admission\": 1, \"chunks_Clinical\": 1}"}
2026-08-10 16:32:51,704 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 16:32:51,705 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:32:51.704+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 74, "failed": 0, "current": {"dca6cdea94d711f1bd9827cf206dfa2d": {"id": "dca6cdea94d711f1bd9827cf206dfa2d", "doc_id": "dbef275894d711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "size": 28457006, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786379026603, "task_type": "dataflow", "root_trace_id": "00f6a24fb6bd4742ba80c2030b932c44", "root_traceparent": "00-00f6a24fb6bd4742ba80c2030b932c44-fbfb6d98b4675b32-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:32:51,712 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:32:51,712 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 16:32:52,575 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:32:52,581 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 16:32:52,581 INFO     29 [Trace] task=dca6cdea | doc=LBZH，男，63岁，胃癌一线(1).pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "523 items", "markdown": "", "text": "", "name": "LBZH，男，63岁，胃癌一线(1).pdf", "output_format": "chunks", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_LabExam\": 1, \"chunks_Examination\": 4, \"chunks_Admission\": 1, \"chunks_Clinical\": 1}"}
2026-08-10 16:32:52,581 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 16:32:52,587 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:32:52,588 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:32:52,588 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 16:32:52,588 INFO     29 [qwen-vl-text] positions(96): [[17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:32:52,588 INFO     29 [qwen-vl-text] page grouping: [17, 18, 19], lines per page: [37, 35, 24]
2026-08-10 16:32:53,203 INFO     29 [qwen-vl-text] page=17, rect=3015x1684, img=(8375x4678), dpi=200
2026-08-10 16:32:54,061 INFO     29 [qwen-vl-text] page=18, rect=2344x3000, img=(6512x8334), dpi=200
2026-08-10 16:32:54,859 INFO     29 [qwen-vl-text] page=19, rect=2369x3000, img=(6581x8334), dpi=200
2026-08-10 16:32:54,866 INFO     29 [qwen-vl-text] LLM extraction start, text_len=3370
2026-08-10 16:32:54,866 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:32:54,866 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 427, \"bbox_end\": 522, \"encounter_dates\": [\"2026-03-24\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "2026-03-24 15:16\n于2024-09-02以'进行性吞咽困难2个月'为主诉入院。2024-08-23于连江县晓澳卫生院行胃镜示'贲门肿块浸润性癌；食管下段浸润伴狭窄'；胃镜病理示：（贲门）腺癌，多层螺旋CT平扫+增强扫描+MPR：1.考虑贲门-胃体癌伴胃周淋巴结肿大\n胃镜及腹部影像学检查；2.双肺多形性支气管纵隔、双肺门淋巴结钙化，尘肺可能，请结合病史；3.双肺上叶、右肺中叶较大肺大泡；4.扫及肝囊肿，请结合腹部影像学检查；病理会诊报告号(H24-03863)：(贲门)腺癌，相关检查未见明显化疗禁忌\n于2024.09.04、2024.09.27、2024.10.25以'奥沙利铂160mg ivgtt d1+5-FU 4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w'方案行术前第1-3周期化疗，化疗过程顺利，相关检查无手术禁忌症，经充分术前准备后于2024-11-28在全麻下行\n胃镜辅助食管胃交界处癌根治术'，术程顺利，恢复良好，术后病理回报(病理号：24-31776)：下段食管+近端胃切除标本：(食管胃交界)隆起型低分化腺癌(肿物大小8x7cm，L...[未打印]\n姓名\n性别：男 年龄：62岁\n主诉：食管癌术后化疗免疫治疗后1年余。\n现病史：于2024-09-02以'进行性吞咽困难2个月'为主诉入院。2024-08-23\n于连江县晓澳卫生院行胃镜示'贲门肿块浸润性癌；食管下段浸润伴狭窄'；胃\n镜病理示：（贲门）腺癌，多层螺旋CT平扫+增强扫描+MPR：1.考虑贲门-\n胃体癌伴胃周淋巴结肿大，请结合胃镜及腹部影像学检查；2.双肺多形性支气管\n纵隔、双肺门淋巴结钙化，尘肺可能，请结合病史；3.双肺上叶、右肺中叶较\n大肺大泡；4.扫及肝囊肿，请结合腹部影像学检查；病理会诊报告号(H24-\n03863)：(贲门)腺癌，相关检查未见明显化疗禁忌症，遂于2024.09.04、\n2024.09.27、2024.10.25以'奥沙利铂160mg ivgtt d1+5-FU 4.5g 微量泵\n泵入 48h+信迪利单抗 200mg ivgtt q3w'方案行术前第1-3周期化疗，化疗\n过程顺利，相关检查无手术禁忌症，经充分术前准备后于2024-11-28在全麻\n下行'腹腔镜辅助食管胃交界处癌根治术'，术程顺利，恢复良好，术后病理回\n报(病理号：24-31776)：下段食管+近端胃切除标本：(食管胃交界)隆\n起型低分化腺癌(肿物大小8x7cm，Lauren分型：混合型)，伴治疗反应\n(TRG：3级，残余肿瘤约占90%)，肿瘤侵犯浆膜下层，脉管内见癌栓，神经\n见癌侵犯。标本上、下切缘及另送'上切缘'未见癌。淋巴结2/35见转移癌\n(\"2\" LN1/4、\"7\" LN1/14、胃小弯LN0/6、\"1\" LN0/2、\n\"4\" LN0/2、\"8\" LN0/6、\"9\" LN0/1、\"11\" LN0/2、\"3、5\" 未见\nLN，\"10\" 查见癌结节1枚)。胃小弯LN1/6、\"7\" LN1/14见治疗后反应。\n肿瘤病理分期：ypT3N1Mx (AJCC 第八版)。免疫组化结果：MSH2\n(+)，MSH6 (+)，MLH1 (+)，PMS2 (+)，HER2 (0)，CD34\n(血管+)，D2-40 (淋巴管+)，P53 (+)，EGFR (60%强着色，20%中\n等着色，20%弱着色)，KI-67 (80%+)，CD3 (T细胞+)，约占肿瘤区域\n10%)，CD8 (约占CD3阳性细胞数60%)，PD1 (约占CD3阳性细胞数\n20%)，PD-L1 (CPS=5)，PD-L1neg (-)，P40 (-)，Syn (部分+)，\nCgA (少量+)，CD56 (-)，CK5/6 (-)。原位杂交EBER (-)。于\n2025.01.02以'紫杉醇 200mg ivgtt d1+奥沙利铂 160mg ivgtt d1+5-FU\n3.4g 微量泵泵入 48h'方案行术后第1周期化疗。后予 '斯鲁利单抗' 免疫治\n疗至今。2026-03-13放射报告：计算机体层成像(CT)增强(胸部+上腹)(故\n<\n102床 涂美石\n多重耐药感染上报\n4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w\"方案行术前第1-3周期化疗，化疗过程顺利。相关检\n24-31776）：下段食管+近端胃切除标本：（食管胃交界）隆起型低分化腺癌（肿物大小8x7cm，L...[未\n20%），PD-L1（CPS=5），PD-L1neg（-），P40（-），Syn（部分+），\nCgA（少量+），CD56（-），CK5/6（-）。原位杂交EBER（-）。于\n2025.01.02以\"紫杉醇 200mg ivgtt d1+奥沙利铂 160mg ivgtt d1+5-FU\n3.4g 微量泵泵入 48h\"方案行术后第1周期化疗。后予 \"斯鲁利单抗\" 免疫治\n疗至今。2026-03-13放射报告：计算机体层成像（CT）增强(胸部+上腹)(放\n射报告号:CT00333122)1.胃食管交界处癌术后改变，腹腔淋巴结较前相仿，\n腹膜后淋巴结较前增大，转移可能2.双锁骨上区淋巴结，转移可能3.双肺多形\n性变伴纵隔、双肺门淋巴结钙化与前大致相仿，尘肺可能，请结合病史4.双肺\n上叶、右肺中叶肺大泡，较前相仿5.双侧胸腔少量积液较前相仿6.肝囊肿较前\n大致相仿7.左肾囊肿较前相仿。2026-03-18复查PET-CT检查(核医学科报告\n号:P68729) \"胃食管连接处癌术后\"：1、①腹膜后多发肿大淋巴结，代谢增\n高，考虑转移可能；②双侧锁骨区数枚肿大淋巴结，代谢轻度增高，炎性增\n生？转移待排除，请结合临床。2、腹膜稍增厚，低代谢，建议随诊。3、双\n肺多形性改变，纵隔、双侧肺门多发淋巴结，轻微代谢，结合职业史，以上考\n虑炎性肉芽肿性病变，建议随诊；双肺多发肺大泡。4、双侧胸膜稍增厚；双\n侧胸腔少量积液。5、肝囊肿；左肾囊肿。6、左侧肩关节、右侧髋关节炎性\n病变。今日行超声引导下左侧锁骨上淋巴结快速组织活检，今为求进一步诊\n治，再次就诊我院。\n过敏史：未发现。\n体格检查：神志清晰，皮肤色泽正常，淋巴结未触及肿大；心脏：心律齐，心\n音正常；肺：双肺语颤正常、对称，双肺呼吸音清，未闻及异常呼吸音，双肺\n未闻及干湿性啰音；腹部：平软，无压痛、反跳痛，肝脾肋下未触及。\n辅助检查：2026-03-24超声报告：彩超检查（常规）-浅表(超声报告\n号:20260070720)双侧颈部多发淋巴结肿大（倾向淋巴结转移）；\n诊断：\n西医诊断：\n食管恶性肿瘤(ypT3N1M0 III B期)\n中医诊断：\n处理措施：进一步系统治疗。\n药品处方：\n检验检查：\n大致相仿7.左肾囊肿较前相仿。2026-03-18复查PET-CT检查(核医学科报告\n号:P68729)“胃食管连接处癌术后”：1、①腹膜后多发肿大淋巴结，代谢增\n高，考虑转移可能；②双侧锁骨区数枚肿大淋巴结，代谢轻度增高，炎性增\n生？转移待排除，请结合临床。2、腹膜稍增厚，低代谢，建议随诊。3、双\n肺多形性改变，纵隔、双侧肺门多发淋巴结，轻微代谢，结合职业史，以上考\n虑炎性肉芽肿性病变，建议随诊；双肺多发肺大泡。4、双侧胸膜稍增厚；双\n侧胸腔少量积液。5、肝囊肿；左肾囊肿。6、左侧肩关节、右侧髋关节炎性\n病变。今日行超声引导下左侧锁骨上淋巴结快速组织活检，今为求进一步诊\n治，再次就诊我院。\n过敏史：未发现。\n体格检查：神志清晰，皮肤色泽正常，淋巴结未触及肿大；心脏：心律齐，心\n音正常；肺：双肺语颤正常、对称，双肺呼吸音清，未闻及异常呼吸音，双肺\n未闻及干湿性啰音；腹部：平软，无压痛、反跳痛，肝脾肋下未触及。\n辅助检查：2026-03-24超声报告：彩超检查（常规）-浅表(超声报告\n号:20260070720)双侧颈部多发淋巴结肿大（倾向淋巴结转移）；\n诊断：\n西医诊断：\n食管恶性肿瘤(ypT3N1M0 IIIIB期)\n中医诊断：\n处理措施：进一步系统治疗。\n药品处方：\n检验检查：\n医生签名：\n签名时间:2026-03-24 15:16",
    "role": "user"
  }
]
2026-08-10 16:33:08,090 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:33:08,090 INFO     29 [qwen-vl-text] LLM output (len=1825):
{
  "encounter_date": "2026-03-24",
  "chief_complaint": "食管癌术后化疗免疫治疗后1年余。",
  "present_illness": "于2024-09-02以'进行性吞咽困难2个月'为主诉入院。2024-08-23于连江县晓澳卫生院行胃镜示'贲门肿块浸润性癌；食管下段浸润伴狭窄'；胃镜病理示：（贲门）腺癌，多层螺旋CT平扫+增强扫描+MPR：1.考虑贲门-胃体癌伴胃周淋巴结肿大，请结合胃镜及腹部影像学检查；2.双肺多形性支气管纵隔、双肺门淋巴结钙化，尘肺可能，请结合病史；3.双肺上叶、右肺中叶较大肺大泡；4.扫及肝囊肿，请结合腹部影像学检查；病理会诊报告号(H24-03863)：(贲门)腺癌，相关检查未见明显化疗禁忌症，遂于2024.09.04、2024.09.27、2024.10.25以'奥沙利铂160mg ivgtt d1+5-FU 4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w'方案行术前第1-3周期化疗，化疗过程顺利，相关检查无手术禁忌症，经充分术前准备后于2024-11-28在全麻下行'腹腔镜辅助食管胃交界处癌根治术'，术程顺利，恢复良好，术后病理回报(病理号：24-31776)：下段食管+近端胃切除标本：(食管胃交界)隆起型低分化腺癌(肿物大小8x7cm，Lauren分型：混合型)，伴治疗反应(TRG：3级，残余肿瘤约占90%)，肿瘤侵犯浆膜下层，脉管内见癌栓，神经见癌侵犯。标本上、下切缘及另送'上切缘'未见癌。淋巴结2/35见转移癌(\"2\" LN1/4、\"7\" LN1/14、胃小弯LN0/6、\"1\" LN0/2、\"4\" LN0/2、\"8\" LN0/6、\"9\" LN0/1、\"11\" LN0/2、\"3、5\" 未见LN，\"10\" 查见癌结节1枚)。胃小弯LN1/6、\"7\" LN1/14见治疗后反应。肿瘤病理分期：ypT3N1Mx (AJCC 第八版)。免疫组化结果：MSH2 (+)，MSH6 (+)，MLH1 (+)，PMS2 (+)，HER2 (0)，CD34 (血管+)，D2-40 (淋巴管+)，P53 (+)，EGFR (60%强着色，20%中等着色，20%弱着色)，KI-67 (80%+)，CD3 (T细胞+)，约占肿瘤区域10%)，CD8 (约占CD3阳性细胞数60%)，PD1 (约占CD3阳性细胞数20%)，PD-L1 (CPS=5)，PD-L1neg (-)，P40 (-)，Syn (部分+)，CgA (少量+)，CD56 (-)，CK5/6 (-)。原位杂交EBER (-)。于2025.01.02以'紫杉醇 200mg ivgtt d1+奥沙利铂 160mg ivgtt d1+5-FU 3.4g 微量泵泵入 48h'方案行术后第1周期化疗。后予 '斯鲁利单抗' 免疫治疗至今。2026-03-13放射报告：计算机体层成像(CT)增强(胸部+上腹)(放射报告号:CT00333122)1.胃食管交界处癌术后改变，腹腔淋巴结较前相仿，腹膜后淋巴结较前增大，转移可能2.双锁骨上区淋巴结，转移可能3.双肺多形性变伴纵隔、双肺门淋巴结钙化与前大致相仿，尘肺可能，请结合病史4.双肺上叶、右肺中叶肺大泡，较前相仿5.双侧胸腔少量积液较前相仿6.肝囊肿较前大致相仿7.左肾囊肿较前相仿。2026-03-18复查PET-CT检查(核医学科报告号:P68729) \"胃食管连接处癌术后\"：1、①腹膜后多发肿大淋巴结，代谢增高，考虑转移可能；②双侧锁骨区数枚肿大淋巴结，代谢轻度增高，炎性增生？转移待排除，请结合临床。2、腹膜稍增厚，低代谢，建议随诊。3、双肺多形性改变，纵隔、双侧肺门多发淋巴结，轻微代谢，结合职业史，以上考虑炎性肉芽肿性病变，建议随诊；双肺多发肺大泡。4、双侧胸膜稍增厚；双侧胸腔少量积液。5、肝囊肿；左肾囊肿。6、左侧肩关节、右侧髋关节炎性病变。今日行超声引导下左侧锁骨上淋巴结快速组织活检，今为求进一步诊治，再次就诊我院。",
  "past_history": "过敏史：未发现。",
  "diagnosis": "西医诊断：食管恶性肿瘤(ypT3N1M0 III B期)",
  "treatment_plan": "进一步系统治疗。"
}
2026-08-10 16:33:08,090 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-03-24]
2026-08-10 16:33:08,098 INFO     29 [qwen-vl-text] coord API call start, page=17, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3028769, prompt_len=2471
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共37行）
["2026-03-24 15:16", "于2024-09-02以'进行性吞咽困难2个月'为主诉入院。2024-08-23于连江县晓澳卫生院行胃镜示'贲门肿块浸润性癌；食管下段浸润伴狭窄'；胃镜病理示：（贲门）腺癌，多层螺旋CT平扫+增强扫描+MPR：1.考虑贲门-胃体癌伴胃周淋巴结肿大", "胃镜及腹部影像学检查；2.双肺多形性支气管纵隔、双肺门淋巴结钙化，尘肺可能，请结合病史；3.双肺上叶、右肺中叶较大肺大泡；4.扫及肝囊肿，请结合腹部影像学检查；病理会诊报告号(H24-03863)：(贲门)腺癌，相关检查未见明显化疗禁忌", "于2024.09.04、2024.09.27、2024.10.25以'奥沙利铂160mg ivgtt d1+5-FU 4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w'方案行术前第1-3周期化疗，化疗过程顺利，相关检查无手术禁忌症，经充分术前准备后于2024-11-28在全麻下行", "胃镜辅助食管胃交界处癌根治术'，术程顺利，恢复良好，术后病理回报(病理号：24-31776)：下段食管+近端胃切除标本：(食管胃交界)隆起型低分化腺癌(肿物大小8x7cm，L...[未打印]", "姓名", "性别：男 年龄：62岁", "主诉：食管癌术后化疗免疫治疗后1年余。", "现病史：于2024-09-02以'进行性吞咽困难2个月'为主诉入院。2024-08-23", "于连江县晓澳卫生院行胃镜示'贲门肿块浸润性癌；食管下段浸润伴狭窄'；胃", "镜病理示：（贲门）腺癌，多层螺旋CT平扫+增强扫描+MPR：1.考虑贲门-", "胃体癌伴胃周淋巴结肿大，请结合胃镜及腹部影像学检查；2.双肺多形性支气管", "纵隔、双肺门淋巴结钙化，尘肺可能，请结合病史；3.双肺上叶、右肺中叶较", "大肺大泡；4.扫及肝囊肿，请结合腹部影像学检查；病理会诊报告号(H24-", "03863)：(贲门)腺癌，相关检查未见明显化疗禁忌症，遂于2024.09.04、", "2024.09.27、2024.10.25以'奥沙利铂160mg ivgtt d1+5-FU 4.5g 微量泵", "泵入 48h+信迪利单抗 200mg ivgtt q3w'方案行术前第1-3周期化疗，化疗", "过程顺利，相关检查无手术禁忌症，经充分术前准备后于2024-11-28在全麻", "下行'腹腔镜辅助食管胃交界处癌根治术'，术程顺利，恢复良好，术后病理回", "报(病理号：24-31776)：下段食管+近端胃切除标本：(食管胃交界)隆", "起型低分化腺癌(肿物大小8x7cm，Lauren分型：混合型)，伴治疗反应", "(TRG：3级，残余肿瘤约占90%)，肿瘤侵犯浆膜下层，脉管内见癌栓，神经", "见癌侵犯。标本上、下切缘及另送'上切缘'未见癌。淋巴结2/35见转移癌", "(\"2\" LN1/4、\"7\" LN1/14、胃小弯LN0/6、\"1\" LN0/2、", "\"4\" LN0/2、\"8\" LN0/6、\"9\" LN0/1、\"11\" LN0/2、\"3、5\" 未见", "LN，\"10\" 查见癌结节1枚)。胃小弯LN1/6、\"7\" LN1/14见治疗后反应。", "肿瘤病理分期：ypT3N1Mx (AJCC 第八版)。免疫组化结果：MSH2", "(+)，MSH6 (+)，MLH1 (+)，PMS2 (+)，HER2 (0)，CD34", "(血管+)，D2-40 (淋巴管+)，P53 (+)，EGFR (60%强着色，20%中", "等着色，20%弱着色)，KI-67 (80%+)，CD3 (T细胞+)，约占肿瘤区域", "10%)，CD8 (约占CD3阳性细胞数60%)，PD1 (约占CD3阳性细胞数", "20%)，PD-L1 (CPS=5)，PD-L1neg (-)，P40 (-)，Syn (部分+)，", "CgA (少量+)，CD56 (-)，CK5/6 (-)。原位杂交EBER (-)。于", "2025.01.02以'紫杉醇 200mg ivgtt d1+奥沙利铂 160mg ivgtt d1+5-FU", "3.4g 微量泵泵入 48h'方案行术后第1周期化疗。后予 '斯鲁利单抗' 免疫治", "疗至今。2026-03-13放射报告：计算机体层成像(CT)增强(胸部+上腹)(故", "<"]

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
2026-08-10 16:33:36,996 INFO     29 [qwen-vl-text] coord API raw response (len=3365):
[
	{"text": "2026-03-24 15:16", "bbox": [39, 69, 114, 87]},
	{"text": "于2024-09-02以'进行性吞咽困难2个月'为主诉入院。2024-08-23于连江县晓澳卫生院行胃镜示'贲门肿块浸润性癌；食管下段浸润伴狭窄'；胃镜病理示：（贲门）腺癌，多层螺旋CT平扫+增强扫描+MPR：1.考虑贲门-胃体癌伴胃周淋巴结肿大", "bbox": [40, 90, 983, 109]},
	{"text": "胃镜及腹部影像学检查；2.双肺多形性支气管纵隔、双肺门淋巴结钙化，尘肺可能，请结合病史；3.双肺上叶、右肺中叶较大肺大泡；4.扫及肝囊肿，请结合腹部影像学检查；病理会诊报告号(H24-03863)：(贲门)腺癌，相关检查未见明显化疗禁忌", "bbox": [40, 111, 983, 130]},
	{"text": "于2024.09.04、2024.09.27、2024.10.25以'奥沙利铂160mg ivgtt d1+5-FU 4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w'方案行术前第1-3周期化疗，化疗过程顺利，相关检查无手术禁忌症，经充分术前准备后于2024-11-28在全麻下行", "bbox": [40, 132, 983, 151]},
	{"text": "胃镜辅助食管胃交界处癌根治术'，术程顺利，恢复良好，术后病理回报(病理号：24-31776)：下段食管+近端胃切除标本：(食管胃交界)隆起型低分化腺癌(肿物大小8x7cm，L...[未打印]", "bbox": [40, 153, 764, 172]},
	{"text": "姓名", "bbox": [40, 233, 56, 249]},
	{"text": "性别：男 年龄：62岁", "bbox": [93, 233, 177, 249]},
	{"text": "主诉：食管癌术后化疗免疫治疗后1年余。", "bbox": [393, 258, 539, 275]},
	{"text": "现病史：于2024-09-02以'进行性吞咽困难2个月'为主诉入院。2024-08-23", "bbox": [393, 283, 664, 300]},
	{"text": "于连江县晓澳卫生院行胃镜示'贲门肿块浸润性癌；食管下段浸润伴狭窄'；胃", "bbox": [393, 308, 668, 325]},
	{"text": "镜病理示：（贲门）腺癌，多层螺旋CT平扫+增强扫描+MPR：1.考虑贲门-", "bbox": [393, 333, 662, 350]},
	{"text": "胃体癌伴胃周淋巴结肿大，请结合胃镜及腹部影像学检查；2.双肺多形性支气管", "bbox": [393, 358, 668, 375]},
	{"text": "纵隔、双肺门淋巴结钙化，尘肺可能，请结合病史；3.双肺上叶、右肺中叶较", "bbox": [393, 383, 668, 400]},
	{"text": "大肺大泡；4.扫及肝囊肿，请结合腹部影像学检查；病理会诊报告号(H24-", "bbox": [393, 408, 662, 425]},
	{"text": "03863)：(贲门)腺癌，相关检查未见明显化疗禁忌症，遂于2024.09.04、", "bbox": [393, 433, 658, 450]},
	{"text": "2024.09.27、2024.10.25以'奥沙利铂160mg ivgtt d1+5-FU 4.5g 微量泵", "bbox": [393, 458, 669, 475]},
	{"text": "泵入 48h+信迪利单抗 200mg ivgtt q3w'方案行术前第1-3周期化疗，化疗", "bbox": [393, 483, 669, 500]},
	{"text": "过程顺利，相关检查无手术禁忌症，经充分术前准备后于2024-11-28在全麻", "bbox": [393, 508, 665, 525]},
	{"text": "下行'腹腔镜辅助食管胃交界处癌根治术'，术程顺利，恢复良好，术后病理回", "bbox": [393, 533, 668, 550]},
	{"text": "报(病理号：24-31776)：下段食管+近端胃切除标本：(食管胃交界)隆", "bbox": [393, 558, 662, 575]},
	{"text": "起型低分化腺癌(肿物大小8x7cm，Lauren分型：混合型)，伴治疗反应", "bbox": [393, 583, 657, 600]},
	{"text": "(TRG：3级，残余肿瘤约占90%)，肿瘤侵犯浆膜下层，脉管内见癌栓，神经", "bbox": [397, 608, 667, 625]},
	{"text": "见癌侵犯。标本上、下切缘及另送'上切缘'未见癌。淋巴结2/35见转移癌", "bbox": [393, 633, 662, 650]},
	{"text": "(\"2\" LN1/4、\"7\" LN1/14、胃小弯LN0/6、\"1\" LN0/2、", "bbox": [397, 658, 613, 675]},
	{"text": "\"4\" LN0/2、\"8\" LN0/6、\"9\" LN0/1、\"11\" LN0/2、\"3、5\" 未见", "bbox": [397, 683, 657, 700]},
	{"text": "LN，\"10\" 查见癌结节1枚)。胃小弯LN1/6、\"7\" LN1/14见治疗后反应。", "bbox": [393, 708, 664, 725]},
	{"text": "肿瘤病理分期：ypT3N1Mx (AJCC 第八版)。免疫组化结果：MSH2", "bbox": [393, 733, 645, 750]},
	{"text": "(+)，MSH6 (+)，MLH1 (+)，PMS2 (+)，HER2 (0)，CD34", "bbox": [397, 758, 654, 775]},
	{"text": "(血管+)，D2-40 (淋巴管+)，P53 (+)，EGFR (60%强着色，20%中", "bbox": [397, 783, 663, 800]},
	{"text": "等着色，20%弱着色)，KI-67 (80%+)，CD3 (T细胞+)，约占肿瘤区域", "bbox": [393, 808, 658, 825]},
	{"text": "10%)，CD8 (约占CD3阳性细胞数60%)，PD1 (约占CD3阳性细胞数", "bbox": [393, 833, 654, 850]},
	{"text": "20%)，PD-L1 (CPS=5)，PD-L1neg (-)，P40 (-)，Syn (部分+)，", "bbox": [393, 858, 664, 875]},
	{"text": "CgA (少量+)，CD56 (-)，CK5/6 (-)。原位杂交EBER (-)。于", "bbox": [393, 883, 644, 900]},
	{"text": "2025.01.02以'紫杉醇 200mg ivgtt d1+奥沙利铂 160mg ivgtt d1+5-FU", "bbox": [393, 908, 664, 925]},
	{"text": "3.4g 微量泵泵入 48h'方案行术后第1周期化疗。后予 '斯鲁利单抗' 免疫治", "bbox": [393, 933, 667, 950]},
	{"text": "疗至今。2026-03-13放射报告：计算机体层成像(CT)增强(胸部+上腹)(故", "bbox": [393, 958, 664, 975]},
	{"text": "<", "bbox": [40, 975, 47, 990]}
]
2026-08-10 16:33:36,996 INFO     29 [qwen-vl-text] coord API: raw_items=37, valid_items=37, elapsed=28.9s
2026-08-10 16:33:36,996 INFO     29 [qwen-vl-text] coord item[0]: text=2026-03-24 15:16, bbox=[39, 69, 114, 87]
2026-08-10 16:33:36,996 INFO     29 [qwen-vl-text] coord item[1]: text=于2024-09-02以'进行性吞咽困难2个月'为主诉入院。2024-08-23于连江县晓澳卫生院行胃镜示'贲门肿块浸润性癌；食管下段浸润伴狭窄'；胃镜病理示：（贲门）腺癌，多层螺旋CT平扫+增强扫描+MPR：1.考虑贲门-胃体癌伴胃周淋巴结肿大, bbox=[40, 90, 983, 109]
2026-08-10 16:33:36,996 INFO     29 [qwen-vl-text] coord item[2]: text=胃镜及腹部影像学检查；2.双肺多形性支气管纵隔、双肺门淋巴结钙化，尘肺可能，请结合病史；3.双肺上叶、右肺中叶较大肺大泡；4.扫及肝囊肿，请结合腹部影像学检查；病理会诊报告号(H24-03863)：(贲门)腺癌，相关检查未见明显化疗禁忌, bbox=[40, 111, 983, 130]
2026-08-10 16:33:36,996 INFO     29 [qwen-vl-text] coord item[3]: text=于2024.09.04、2024.09.27、2024.10.25以'奥沙利铂160mg ivgtt d1+5-FU 4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w'方案行术前第1-3周期化疗，化疗过程顺利，相关检查无手术禁忌症，经充分术前准备后于2024-11-28在全麻下行, bbox=[40, 132, 983, 151]
2026-08-10 16:33:36,996 INFO     29 [qwen-vl-text] coord item[4]: text=胃镜辅助食管胃交界处癌根治术'，术程顺利，恢复良好，术后病理回报(病理号：24-31776)：下段食管+近端胃切除标本：(食管胃交界)隆起型低分化腺癌(肿物大小8x7cm，L...[未打印], bbox=[40, 153, 764, 172]
2026-08-10 16:33:36,996 INFO     29 [qwen-vl-text] coord item[5]: text=姓名, bbox=[40, 233, 56, 249]
2026-08-10 16:33:36,996 INFO     29 [qwen-vl-text] coord item[6]: text=性别：男 年龄：62岁, bbox=[93, 233, 177, 249]
2026-08-10 16:33:36,996 INFO     29 [qwen-vl-text] coord item[7]: text=主诉：食管癌术后化疗免疫治疗后1年余。, bbox=[393, 258, 539, 275]
2026-08-10 16:33:36,996 INFO     29 [qwen-vl-text] coord item[8]: text=现病史：于2024-09-02以'进行性吞咽困难2个月'为主诉入院。2024-08-23, bbox=[393, 283, 664, 300]
2026-08-10 16:33:36,996 INFO     29 [qwen-vl-text] coord item[9]: text=于连江县晓澳卫生院行胃镜示'贲门肿块浸润性癌；食管下段浸润伴狭窄'；胃, bbox=[393, 308, 668, 325]
2026-08-10 16:33:36,996 INFO     29 [qwen-vl-text] coord item[10]: text=镜病理示：（贲门）腺癌，多层螺旋CT平扫+增强扫描+MPR：1.考虑贲门-, bbox=[393, 333, 662, 350]
2026-08-10 16:33:36,996 INFO     29 [qwen-vl-text] coord item[11]: text=胃体癌伴胃周淋巴结肿大，请结合胃镜及腹部影像学检查；2.双肺多形性支气管, bbox=[393, 358, 668, 375]
2026-08-10 16:33:36,996 INFO     29 [qwen-vl-text] coord item[12]: text=纵隔、双肺门淋巴结钙化，尘肺可能，请结合病史；3.双肺上叶、右肺中叶较, bbox=[393, 383, 668, 400]
2026-08-10 16:33:36,996 INFO     29 [qwen-vl-text] coord item[13]: text=大肺大泡；4.扫及肝囊肿，请结合腹部影像学检查；病理会诊报告号(H24-, bbox=[393, 408, 662, 425]
2026-08-10 16:33:36,997 INFO     29 [qwen-vl-text] coord item[14]: text=03863)：(贲门)腺癌，相关检查未见明显化疗禁忌症，遂于2024.09.04、, bbox=[393, 433, 658, 450]
2026-08-10 16:33:36,997 INFO     29 [qwen-vl-text] coord item[15]: text=2024.09.27、2024.10.25以'奥沙利铂160mg ivgtt d1+5-FU 4.5g 微量泵, bbox=[393, 458, 669, 475]
2026-08-10 16:33:36,997 INFO     29 [qwen-vl-text] coord item[16]: text=泵入 48h+信迪利单抗 200mg ivgtt q3w'方案行术前第1-3周期化疗，化疗, bbox=[393, 483, 669, 500]
2026-08-10 16:33:36,997 INFO     29 [qwen-vl-text] coord item[17]: text=过程顺利，相关检查无手术禁忌症，经充分术前准备后于2024-11-28在全麻, bbox=[393, 508, 665, 525]
2026-08-10 16:33:36,997 INFO     29 [qwen-vl-text] coord item[18]: text=下行'腹腔镜辅助食管胃交界处癌根治术'，术程顺利，恢复良好，术后病理回, bbox=[393, 533, 668, 550]
2026-08-10 16:33:36,997 INFO     29 [qwen-vl-text] coord item[19]: text=报(病理号：24-31776)：下段食管+近端胃切除标本：(食管胃交界)隆, bbox=[393, 558, 662, 575]
2026-08-10 16:33:36,997 INFO     29 [qwen-vl-text] coord item[20]: text=起型低分化腺癌(肿物大小8x7cm，Lauren分型：混合型)，伴治疗反应, bbox=[393, 583, 657, 600]
2026-08-10 16:33:36,997 INFO     29 [qwen-vl-text] coord item[21]: text=(TRG：3级，残余肿瘤约占90%)，肿瘤侵犯浆膜下层，脉管内见癌栓，神经, bbox=[397, 608, 667, 625]
2026-08-10 16:33:36,997 INFO     29 [qwen-vl-text] coord item[22]: text=见癌侵犯。标本上、下切缘及另送'上切缘'未见癌。淋巴结2/35见转移癌, bbox=[393, 633, 662, 650]
2026-08-10 16:33:36,997 INFO     29 [qwen-vl-text] coord item[23]: text=("2" LN1/4、"7" LN1/14、胃小弯LN0/6、"1" LN0/2、, bbox=[397, 658, 613, 675]
2026-08-10 16:33:36,997 INFO     29 [qwen-vl-text] coord item[24]: text="4" LN0/2、"8" LN0/6、"9" LN0/1、"11" LN0/2、"3、5" 未见, bbox=[397, 683, 657, 700]
2026-08-10 16:33:36,997 INFO     29 [qwen-vl-text] coord item[25]: text=LN，"10" 查见癌结节1枚)。胃小弯LN1/6、"7" LN1/14见治疗后反应。, bbox=[393, 708, 664, 725]
2026-08-10 16:33:36,997 INFO     29 [qwen-vl-text] coord item[26]: text=肿瘤病理分期：ypT3N1Mx (AJCC 第八版)。免疫组化结果：MSH2, bbox=[393, 733, 645, 750]
2026-08-10 16:33:36,997 INFO     29 [qwen-vl-text] coord item[27]: text=(+)，MSH6 (+)，MLH1 (+)，PMS2 (+)，HER2 (0)，CD34, bbox=[397, 758, 654, 775]
2026-08-10 16:33:36,997 INFO     29 [qwen-vl-text] coord item[28]: text=(血管+)，D2-40 (淋巴管+)，P53 (+)，EGFR (60%强着色，20%中, bbox=[397, 783, 663, 800]
2026-08-10 16:33:36,997 INFO     29 [qwen-vl-text] coord item[29]: text=等着色，20%弱着色)，KI-67 (80%+)，CD3 (T细胞+)，约占肿瘤区域, bbox=[393, 808, 658, 825]
2026-08-10 16:33:36,997 INFO     29 [qwen-vl-text] coord item[30]: text=10%)，CD8 (约占CD3阳性细胞数60%)，PD1 (约占CD3阳性细胞数, bbox=[393, 833, 654, 850]
2026-08-10 16:33:36,997 INFO     29 [qwen-vl-text] coord item[31]: text=20%)，PD-L1 (CPS=5)，PD-L1neg (-)，P40 (-)，Syn (部分+)，, bbox=[393, 858, 664, 875]
2026-08-10 16:33:36,997 INFO     29 [qwen-vl-text] coord item[32]: text=CgA (少量+)，CD56 (-)，CK5/6 (-)。原位杂交EBER (-)。于, bbox=[393, 883, 644, 900]
2026-08-10 16:33:36,997 INFO     29 [qwen-vl-text] coord item[33]: text=2025.01.02以'紫杉醇 200mg ivgtt d1+奥沙利铂 160mg ivgtt d1+5-FU, bbox=[393, 908, 664, 925]
2026-08-10 16:33:36,997 INFO     29 [qwen-vl-text] coord item[34]: text=3.4g 微量泵泵入 48h'方案行术后第1周期化疗。后予 '斯鲁利单抗' 免疫治, bbox=[393, 933, 667, 950]
2026-08-10 16:33:36,997 INFO     29 [qwen-vl-text] coord item[35]: text=疗至今。2026-03-13放射报告：计算机体层成像(CT)增强(胸部+上腹)(故, bbox=[393, 958, 664, 975]
2026-08-10 16:33:36,997 INFO     29 [qwen-vl-text] coord item[36]: text=<, bbox=[40, 975, 47, 990]
2026-08-10 16:33:36,997 INFO     29 [qwen-vl-text] page=17 — 37/37 coords, api_time=28.9s
2026-08-10 16:33:37,003 INFO     29 [qwen-vl-text] coord API call start, page=18, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3691577, prompt_len=1789
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共35行）
["102床 涂美石", "多重耐药感染上报", "4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w\"方案行术前第1-3周期化疗，化疗过程顺利。相关检", "24-31776）：下段食管+近端胃切除标本：（食管胃交界）隆起型低分化腺癌（肿物大小8x7cm，L...[未", "20%），PD-L1（CPS=5），PD-L1neg（-），P40（-），Syn（部分+），", "CgA（少量+），CD56（-），CK5/6（-）。原位杂交EBER（-）。于", "2025.01.02以\"紫杉醇 200mg ivgtt d1+奥沙利铂 160mg ivgtt d1+5-FU", "3.4g 微量泵泵入 48h\"方案行术后第1周期化疗。后予 \"斯鲁利单抗\" 免疫治", "疗至今。2026-03-13放射报告：计算机体层成像（CT）增强(胸部+上腹)(放", "射报告号:CT00333122)1.胃食管交界处癌术后改变，腹腔淋巴结较前相仿，", "腹膜后淋巴结较前增大，转移可能2.双锁骨上区淋巴结，转移可能3.双肺多形", "性变伴纵隔、双肺门淋巴结钙化与前大致相仿，尘肺可能，请结合病史4.双肺", "上叶、右肺中叶肺大泡，较前相仿5.双侧胸腔少量积液较前相仿6.肝囊肿较前", "大致相仿7.左肾囊肿较前相仿。2026-03-18复查PET-CT检查(核医学科报告", "号:P68729) \"胃食管连接处癌术后\"：1、①腹膜后多发肿大淋巴结，代谢增", "高，考虑转移可能；②双侧锁骨区数枚肿大淋巴结，代谢轻度增高，炎性增", "生？转移待排除，请结合临床。2、腹膜稍增厚，低代谢，建议随诊。3、双", "肺多形性改变，纵隔、双侧肺门多发淋巴结，轻微代谢，结合职业史，以上考", "虑炎性肉芽肿性病变，建议随诊；双肺多发肺大泡。4、双侧胸膜稍增厚；双", "侧胸腔少量积液。5、肝囊肿；左肾囊肿。6、左侧肩关节、右侧髋关节炎性", "病变。今日行超声引导下左侧锁骨上淋巴结快速组织活检，今为求进一步诊", "治，再次就诊我院。", "过敏史：未发现。", "体格检查：神志清晰，皮肤色泽正常，淋巴结未触及肿大；心脏：心律齐，心", "音正常；肺：双肺语颤正常、对称，双肺呼吸音清，未闻及异常呼吸音，双肺", "未闻及干湿性啰音；腹部：平软，无压痛、反跳痛，肝脾肋下未触及。", "辅助检查：2026-03-24超声报告：彩超检查（常规）-浅表(超声报告", "号:20260070720)双侧颈部多发淋巴结肿大（倾向淋巴结转移）；", "诊断：", "西医诊断：", "食管恶性肿瘤(ypT3N1M0 III B期)", "中医诊断：", "处理措施：进一步系统治疗。", "药品处方：", "检验检查："]

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
2026-08-10 16:33:59,285 INFO     29 [qwen-vl-text] coord API raw response (len=2607):
[
	{"text": "102床 涂美石", "bbox": [42, 15, 156, 33]},
	{"text": "多重耐药感染上报", "bbox": [218, 15, 351, 33]},
	{"text": "4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w\"方案行术前第1-3周期化疗，化疗过程顺利。相关检", "bbox": [42, 105, 980, 125]},
	{"text": "24-31776）：下段食管+近端胃切除标本：（食管胃交界）隆起型低分化腺癌（肿物大小8x7cm，L...[未", "bbox": [42, 127, 980, 146]},
	{"text": "20%），PD-L1（CPS=5），PD-L1neg（-），P40（-），Syn（部分+），", "bbox": [163, 163, 787, 182]},
	{"text": "CgA（少量+），CD56（-），CK5/6（-）。原位杂交EBER（-）。于", "bbox": [163, 188, 741, 207]},
	{"text": "2025.01.02以\"紫杉醇 200mg ivgtt d1+奥沙利铂 160mg ivgtt d1+5-FU", "bbox": [163, 212, 786, 231]},
	{"text": "3.4g 微量泵泵入 48h\"方案行术后第1周期化疗。后予 \"斯鲁利单抗\" 免疫治", "bbox": [163, 238, 792, 257]},
	{"text": "疗至今。2026-03-13放射报告：计算机体层成像（CT）增强(胸部+上腹)(放", "bbox": [163, 263, 786, 282]},
	{"text": "射报告号:CT00333122)1.胃食管交界处癌术后改变，腹腔淋巴结较前相仿，", "bbox": [163, 288, 768, 307]},
	{"text": "腹膜后淋巴结较前增大，转移可能2.双锁骨上区淋巴结，转移可能3.双肺多形", "bbox": [163, 313, 787, 332]},
	{"text": "性变伴纵隔、双肺门淋巴结钙化与前大致相仿，尘肺可能，请结合病史4.双肺", "bbox": [163, 338, 790, 357]},
	{"text": "上叶、右肺中叶肺大泡，较前相仿5.双侧胸腔少量积液较前相仿6.肝囊肿较前", "bbox": [163, 363, 786, 382]},
	{"text": "大致相仿7.左肾囊肿较前相仿。2026-03-18复查PET-CT检查(核医学科报告", "bbox": [163, 388, 775, 407]},
	{"text": "号:P68729) \"胃食管连接处癌术后\"：1、①腹膜后多发肿大淋巴结，代谢增", "bbox": [163, 413, 786, 432]},
	{"text": "高，考虑转移可能；②双侧锁骨区数枚肿大淋巴结，代谢轻度增高，炎性增", "bbox": [163, 438, 774, 457]},
	{"text": "生？转移待排除，请结合临床。2、腹膜稍增厚，低代谢，建议随诊。3、双", "bbox": [163, 463, 775, 482]},
	{"text": "肺多形性改变，纵隔、双侧肺门多发淋巴结，轻微代谢，结合职业史，以上考", "bbox": [163, 488, 790, 507]},
	{"text": "虑炎性肉芽肿性病变，建议随诊；双肺多发肺大泡。4、双侧胸膜稍增厚；双", "bbox": [163, 513, 782, 532]},
	{"text": "侧胸腔少量积液。5、肝囊肿；左肾囊肿。6、左侧肩关节、右侧髋关节炎性", "bbox": [163, 538, 774, 557]},
	{"text": "病变。今日行超声引导下左侧锁骨上淋巴结快速组织活检，今为求进一步诊", "bbox": [163, 563, 770, 582]},
	{"text": "治，再次就诊我院。", "bbox": [163, 588, 318, 607]},
	{"text": "过敏史：未发现。", "bbox": [163, 613, 299, 631]},
	{"text": "体格检查：神志清晰，皮肤色泽正常，淋巴结未触及肿大；心脏：心律齐，心", "bbox": [163, 638, 787, 657]},
	{"text": "音正常；肺：双肺语颤正常、对称，双肺呼吸音清，未闻及异常呼吸音，双肺", "bbox": [163, 663, 787, 682]},
	{"text": "未闻及干湿性啰音；腹部：平软，无压痛、反跳痛，肝脾肋下未触及。", "bbox": [163, 688, 720, 707]},
	{"text": "辅助检查：2026-03-24超声报告：彩超检查（常规）-浅表(超声报告", "bbox": [163, 713, 717, 732]},
	{"text": "号:20260070720)双侧颈部多发淋巴结肿大（倾向淋巴结转移）；", "bbox": [163, 737, 680, 756]},
	{"text": "诊断：", "bbox": [157, 762, 208, 779]},
	{"text": "西医诊断：", "bbox": [256, 788, 338, 805]},
	{"text": "食管恶性肿瘤(ypT3N1M0 III B期)", "bbox": [257, 813, 528, 831]},
	{"text": "中医诊断：", "bbox": [256, 838, 338, 855]},
	{"text": "处理措施：进一步系统治疗。", "bbox": [165, 886, 390, 903]},
	{"text": "药品处方：", "bbox": [165, 910, 246, 927]},
	{"text": "检验检查：", "bbox": [167, 980, 248, 995]}
]
2026-08-10 16:33:59,285 INFO     29 [qwen-vl-text] coord API: raw_items=35, valid_items=35, elapsed=22.3s
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[0]: text=102床 涂美石, bbox=[42, 15, 156, 33]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[1]: text=多重耐药感染上报, bbox=[218, 15, 351, 33]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[2]: text=4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w"方案行术前第1-3周期化疗，化疗过程顺利。相关检, bbox=[42, 105, 980, 125]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[3]: text=24-31776）：下段食管+近端胃切除标本：（食管胃交界）隆起型低分化腺癌（肿物大小8x7cm，L...[未, bbox=[42, 127, 980, 146]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[4]: text=20%），PD-L1（CPS=5），PD-L1neg（-），P40（-），Syn（部分+），, bbox=[163, 163, 787, 182]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[5]: text=CgA（少量+），CD56（-），CK5/6（-）。原位杂交EBER（-）。于, bbox=[163, 188, 741, 207]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[6]: text=2025.01.02以"紫杉醇 200mg ivgtt d1+奥沙利铂 160mg ivgtt d1+5-FU, bbox=[163, 212, 786, 231]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[7]: text=3.4g 微量泵泵入 48h"方案行术后第1周期化疗。后予 "斯鲁利单抗" 免疫治, bbox=[163, 238, 792, 257]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[8]: text=疗至今。2026-03-13放射报告：计算机体层成像（CT）增强(胸部+上腹)(放, bbox=[163, 263, 786, 282]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[9]: text=射报告号:CT00333122)1.胃食管交界处癌术后改变，腹腔淋巴结较前相仿，, bbox=[163, 288, 768, 307]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[10]: text=腹膜后淋巴结较前增大，转移可能2.双锁骨上区淋巴结，转移可能3.双肺多形, bbox=[163, 313, 787, 332]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[11]: text=性变伴纵隔、双肺门淋巴结钙化与前大致相仿，尘肺可能，请结合病史4.双肺, bbox=[163, 338, 790, 357]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[12]: text=上叶、右肺中叶肺大泡，较前相仿5.双侧胸腔少量积液较前相仿6.肝囊肿较前, bbox=[163, 363, 786, 382]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[13]: text=大致相仿7.左肾囊肿较前相仿。2026-03-18复查PET-CT检查(核医学科报告, bbox=[163, 388, 775, 407]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[14]: text=号:P68729) "胃食管连接处癌术后"：1、①腹膜后多发肿大淋巴结，代谢增, bbox=[163, 413, 786, 432]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[15]: text=高，考虑转移可能；②双侧锁骨区数枚肿大淋巴结，代谢轻度增高，炎性增, bbox=[163, 438, 774, 457]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[16]: text=生？转移待排除，请结合临床。2、腹膜稍增厚，低代谢，建议随诊。3、双, bbox=[163, 463, 775, 482]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[17]: text=肺多形性改变，纵隔、双侧肺门多发淋巴结，轻微代谢，结合职业史，以上考, bbox=[163, 488, 790, 507]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[18]: text=虑炎性肉芽肿性病变，建议随诊；双肺多发肺大泡。4、双侧胸膜稍增厚；双, bbox=[163, 513, 782, 532]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[19]: text=侧胸腔少量积液。5、肝囊肿；左肾囊肿。6、左侧肩关节、右侧髋关节炎性, bbox=[163, 538, 774, 557]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[20]: text=病变。今日行超声引导下左侧锁骨上淋巴结快速组织活检，今为求进一步诊, bbox=[163, 563, 770, 582]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[21]: text=治，再次就诊我院。, bbox=[163, 588, 318, 607]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[22]: text=过敏史：未发现。, bbox=[163, 613, 299, 631]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[23]: text=体格检查：神志清晰，皮肤色泽正常，淋巴结未触及肿大；心脏：心律齐，心, bbox=[163, 638, 787, 657]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[24]: text=音正常；肺：双肺语颤正常、对称，双肺呼吸音清，未闻及异常呼吸音，双肺, bbox=[163, 663, 787, 682]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[25]: text=未闻及干湿性啰音；腹部：平软，无压痛、反跳痛，肝脾肋下未触及。, bbox=[163, 688, 720, 707]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[26]: text=辅助检查：2026-03-24超声报告：彩超检查（常规）-浅表(超声报告, bbox=[163, 713, 717, 732]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[27]: text=号:20260070720)双侧颈部多发淋巴结肿大（倾向淋巴结转移）；, bbox=[163, 737, 680, 756]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[28]: text=诊断：, bbox=[157, 762, 208, 779]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[29]: text=西医诊断：, bbox=[256, 788, 338, 805]
2026-08-10 16:33:59,286 INFO     29 [qwen-vl-text] coord item[30]: text=食管恶性肿瘤(ypT3N1M0 III B期), bbox=[257, 813, 528, 831]
2026-08-10 16:33:59,287 INFO     29 [qwen-vl-text] coord item[31]: text=中医诊断：, bbox=[256, 838, 338, 855]
2026-08-10 16:33:59,287 INFO     29 [qwen-vl-text] coord item[32]: text=处理措施：进一步系统治疗。, bbox=[165, 886, 390, 903]
2026-08-10 16:33:59,287 INFO     29 [qwen-vl-text] coord item[33]: text=药品处方：, bbox=[165, 910, 246, 927]
2026-08-10 16:33:59,287 INFO     29 [qwen-vl-text] coord item[34]: text=检验检查：, bbox=[167, 980, 248, 995]
2026-08-10 16:33:59,288 INFO     29 [qwen-vl-text] page=18 — 35/35 coords, api_time=22.3s
2026-08-10 16:33:59,292 INFO     29 [qwen-vl-text] coord API call start, page=19, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2604039, prompt_len=1262
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共24行）
["大致相仿7.左肾囊肿较前相仿。2026-03-18复查PET-CT检查(核医学科报告", "号:P68729)“胃食管连接处癌术后”：1、①腹膜后多发肿大淋巴结，代谢增", "高，考虑转移可能；②双侧锁骨区数枚肿大淋巴结，代谢轻度增高，炎性增", "生？转移待排除，请结合临床。2、腹膜稍增厚，低代谢，建议随诊。3、双", "肺多形性改变，纵隔、双侧肺门多发淋巴结，轻微代谢，结合职业史，以上考", "虑炎性肉芽肿性病变，建议随诊；双肺多发肺大泡。4、双侧胸膜稍增厚；双", "侧胸腔少量积液。5、肝囊肿；左肾囊肿。6、左侧肩关节、右侧髋关节炎性", "病变。今日行超声引导下左侧锁骨上淋巴结快速组织活检，今为求进一步诊", "治，再次就诊我院。", "过敏史：未发现。", "体格检查：神志清晰，皮肤色泽正常，淋巴结未触及肿大；心脏：心律齐，心", "音正常；肺：双肺语颤正常、对称，双肺呼吸音清，未闻及异常呼吸音，双肺", "未闻及干湿性啰音；腹部：平软，无压痛、反跳痛，肝脾肋下未触及。", "辅助检查：2026-03-24超声报告：彩超检查（常规）-浅表(超声报告", "号:20260070720)双侧颈部多发淋巴结肿大（倾向淋巴结转移）；", "诊断：", "西医诊断：", "食管恶性肿瘤(ypT3N1M0 IIIIB期)", "中医诊断：", "处理措施：进一步系统治疗。", "药品处方：", "检验检查：", "医生签名：", "签名时间:2026-03-24 15:16"]

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
2026-08-10 16:34:18,633 INFO     29 [qwen-vl-text] coord API raw response (len=1633):
[
	{"text": "大致相仿7.左肾囊肿较前相仿。2026-03-18复查PET-CT检查(核医学科报告", "bbox": [154, 58, 888, 80]},
	{"text": "号:P68729)“胃食管连接处癌术后”：1、①腹膜后多发肿大淋巴结，代谢增", "bbox": [154, 90, 901, 110]},
	{"text": "高，考虑转移可能；②双侧锁骨区数枚肿大淋巴结，代谢轻度增高，炎性增", "bbox": [154, 119, 887, 140]},
	{"text": "生？转移待排除，请结合临床。2、腹膜稍增厚，低代谢，建议随诊。3、双", "bbox": [154, 150, 889, 170]},
	{"text": "肺多形性改变，纵隔、双侧肺门多发淋巴结，轻微代谢，结合职业史，以上考", "bbox": [154, 180, 906, 200]},
	{"text": "虑炎性肉芽肿性病变，建议随诊；双肺多发肺大泡。4、双侧胸膜稍增厚；双", "bbox": [154, 209, 897, 230]},
	{"text": "侧胸腔少量积液。5、肝囊肿；左肾囊肿。6、左侧肩关节、右侧髋关节炎性", "bbox": [154, 240, 888, 260]},
	{"text": "病变。今日行超声引导下左侧锁骨上淋巴结快速组织活检，今为求进一步诊", "bbox": [154, 270, 884, 290]},
	{"text": "治，再次就诊我院。", "bbox": [154, 300, 343, 320]},
	{"text": "过敏史：未发现。", "bbox": [154, 330, 321, 350]},
	{"text": "体格检查：神志清晰，皮肤色泽正常，淋巴结未触及肿大；心脏：心律齐，心", "bbox": [154, 360, 904, 380]},
	{"text": "音正常；肺：双肺语颤正常、对称，双肺呼吸音清，未闻及异常呼吸音，双肺", "bbox": [154, 390, 904, 410]},
	{"text": "未闻及干湿性啰音；腹部：平软，无压痛、反跳痛，肝脾肋下未触及。", "bbox": [154, 420, 823, 440]},
	{"text": "辅助检查：2026-03-24超声报告：彩超检查（常规）-浅表(超声报告", "bbox": [154, 450, 819, 470]},
	{"text": "号:20260070720)双侧颈部多发淋巴结肿大（倾向淋巴结转移）；", "bbox": [154, 479, 776, 499]},
	{"text": "诊断：", "bbox": [154, 510, 210, 528]},
	{"text": "西医诊断：", "bbox": [268, 539, 367, 558]},
	{"text": "食管恶性肿瘤(ypT3N1M0 IIIIB期)", "bbox": [268, 568, 593, 588]},
	{"text": "中医诊断：", "bbox": [268, 598, 367, 617]},
	{"text": "处理措施：进一步系统治疗。", "bbox": [154, 658, 428, 677]},
	{"text": "药品处方：", "bbox": [154, 687, 254, 706]},
	{"text": "检验检查：", "bbox": [154, 772, 254, 790]},
	{"text": "医生签名：", "bbox": [307, 884, 399, 901]},
	{"text": "签名时间:2026-03-24 15:16", "bbox": [550, 884, 823, 901]}
]
2026-08-10 16:34:18,634 INFO     29 [qwen-vl-text] coord API: raw_items=24, valid_items=24, elapsed=19.3s
2026-08-10 16:34:18,634 INFO     29 [qwen-vl-text] coord item[0]: text=大致相仿7.左肾囊肿较前相仿。2026-03-18复查PET-CT检查(核医学科报告, bbox=[154, 58, 888, 80]
2026-08-10 16:34:18,634 INFO     29 [qwen-vl-text] coord item[1]: text=号:P68729)“胃食管连接处癌术后”：1、①腹膜后多发肿大淋巴结，代谢增, bbox=[154, 90, 901, 110]
2026-08-10 16:34:18,634 INFO     29 [qwen-vl-text] coord item[2]: text=高，考虑转移可能；②双侧锁骨区数枚肿大淋巴结，代谢轻度增高，炎性增, bbox=[154, 119, 887, 140]
2026-08-10 16:34:18,634 INFO     29 [qwen-vl-text] coord item[3]: text=生？转移待排除，请结合临床。2、腹膜稍增厚，低代谢，建议随诊。3、双, bbox=[154, 150, 889, 170]
2026-08-10 16:34:18,634 INFO     29 [qwen-vl-text] coord item[4]: text=肺多形性改变，纵隔、双侧肺门多发淋巴结，轻微代谢，结合职业史，以上考, bbox=[154, 180, 906, 200]
2026-08-10 16:34:18,634 INFO     29 [qwen-vl-text] coord item[5]: text=虑炎性肉芽肿性病变，建议随诊；双肺多发肺大泡。4、双侧胸膜稍增厚；双, bbox=[154, 209, 897, 230]
2026-08-10 16:34:18,634 INFO     29 [qwen-vl-text] coord item[6]: text=侧胸腔少量积液。5、肝囊肿；左肾囊肿。6、左侧肩关节、右侧髋关节炎性, bbox=[154, 240, 888, 260]
2026-08-10 16:34:18,635 INFO     29 [qwen-vl-text] coord item[7]: text=病变。今日行超声引导下左侧锁骨上淋巴结快速组织活检，今为求进一步诊, bbox=[154, 270, 884, 290]
2026-08-10 16:34:18,635 INFO     29 [qwen-vl-text] coord item[8]: text=治，再次就诊我院。, bbox=[154, 300, 343, 320]
2026-08-10 16:34:18,635 INFO     29 [qwen-vl-text] coord item[9]: text=过敏史：未发现。, bbox=[154, 330, 321, 350]
2026-08-10 16:34:18,635 INFO     29 [qwen-vl-text] coord item[10]: text=体格检查：神志清晰，皮肤色泽正常，淋巴结未触及肿大；心脏：心律齐，心, bbox=[154, 360, 904, 380]
2026-08-10 16:34:18,635 INFO     29 [qwen-vl-text] coord item[11]: text=音正常；肺：双肺语颤正常、对称，双肺呼吸音清，未闻及异常呼吸音，双肺, bbox=[154, 390, 904, 410]
2026-08-10 16:34:18,635 INFO     29 [qwen-vl-text] coord item[12]: text=未闻及干湿性啰音；腹部：平软，无压痛、反跳痛，肝脾肋下未触及。, bbox=[154, 420, 823, 440]
2026-08-10 16:34:18,635 INFO     29 [qwen-vl-text] coord item[13]: text=辅助检查：2026-03-24超声报告：彩超检查（常规）-浅表(超声报告, bbox=[154, 450, 819, 470]
2026-08-10 16:34:18,635 INFO     29 [qwen-vl-text] coord item[14]: text=号:20260070720)双侧颈部多发淋巴结肿大（倾向淋巴结转移）；, bbox=[154, 479, 776, 499]
2026-08-10 16:34:18,635 INFO     29 [qwen-vl-text] coord item[15]: text=诊断：, bbox=[154, 510, 210, 528]
2026-08-10 16:34:18,635 INFO     29 [qwen-vl-text] coord item[16]: text=西医诊断：, bbox=[268, 539, 367, 558]
2026-08-10 16:34:18,635 INFO     29 [qwen-vl-text] coord item[17]: text=食管恶性肿瘤(ypT3N1M0 IIIIB期), bbox=[268, 568, 593, 588]
2026-08-10 16:34:18,636 INFO     29 [qwen-vl-text] coord item[18]: text=中医诊断：, bbox=[268, 598, 367, 617]
2026-08-10 16:34:18,636 INFO     29 [qwen-vl-text] coord item[19]: text=处理措施：进一步系统治疗。, bbox=[154, 658, 428, 677]
2026-08-10 16:34:18,636 INFO     29 [qwen-vl-text] coord item[20]: text=药品处方：, bbox=[154, 687, 254, 706]
2026-08-10 16:34:18,636 INFO     29 [qwen-vl-text] coord item[21]: text=检验检查：, bbox=[154, 772, 254, 790]
2026-08-10 16:34:18,636 INFO     29 [qwen-vl-text] coord item[22]: text=医生签名：, bbox=[307, 884, 399, 901]
2026-08-10 16:34:18,636 INFO     29 [qwen-vl-text] coord item[23]: text=签名时间:2026-03-24 15:16, bbox=[550, 884, 823, 901]
2026-08-10 16:34:18,637 INFO     29 [qwen-vl-text] page=19 — 24/24 coords, api_time=19.3s
2026-08-10 16:34:18,638 INFO     29 [qwen-vl-text] new_positions (96):
[[17, 117.58500000000001, 343.71000000000004, 116.196, 146.50799999999998], [17, 120.60000000000001, 2963.7450000000003, 151.56, 183.55599999999998], [17, 120.60000000000001, 2963.7450000000003, 186.924, 218.92], [17, 120.60000000000001, 2963.7450000000003, 222.28799999999998, 254.284], [17, 120.60000000000001, 2303.46, 257.652, 289.64799999999997], [17, 120.60000000000001, 168.84, 392.372, 419.316], [17, 280.39500000000004, 533.655, 392.372, 419.316], [17, 1184.895, 1625.085, 434.472, 463.09999999999997], [17, 1184.895, 2001.96, 476.572, 505.2], [17, 1184.895, 2014.02, 518.672, 547.3], [17, 1184.895, 1995.93, 560.7719999999999, 589.4], [17, 1184.895, 2014.02, 602.872, 631.5], [17, 1184.895, 2014.02, 644.972, 673.6], [17, 1184.895, 1995.93, 687.072, 715.6999999999999], [17, 1184.895, 1983.8700000000001, 729.172, 757.8], [17, 1184.895, 2017.035, 771.2719999999999, 799.9], [17, 1184.895, 2017.035, 813.372, 842.0], [17, 1184.895, 2004.9750000000001, 855.472, 884.1], [17, 1184.895, 2014.02, 897.572, 926.1999999999999], [17, 1184.895, 1995.93, 939.6719999999999, 968.3], [17, 1184.895, 1980.855, 981.7719999999999, 1010.4], [17, 1196.9550000000002, 2011.005, 1023.872, 1052.5], [17, 1184.895, 1995.93, 1065.972, 1094.6], [17, 1196.9550000000002, 1848.1950000000002, 1108.072, 1136.7], [17, 1196.9550000000002, 1980.855, 1150.172, 1178.8], [17, 1184.895, 2001.96, 1192.272, 1220.8999999999999], [17, 1184.895, 1944.6750000000002, 1234.3719999999998, 1263.0], [17, 1196.9550000000002, 1971.8100000000002, 1276.472, 1305.1], [17, 1196.9550000000002, 1998.9450000000002, 1318.572, 1347.2], [17, 1184.895, 1983.8700000000001, 1360.672, 1389.3], [17, 1184.895, 1971.8100000000002, 1402.772, 1431.3999999999999], [17, 1184.895, 2001.96, 1444.8719999999998, 1473.5], [17, 1184.895, 1941.66, 1486.972, 1515.6], [17, 1184.895, 2001.96, 1529.072, 1557.7], [17, 1184.895, 2011.005, 1571.172, 1599.8], [17, 1184.895, 2001.96, 1613.272, 1641.8999999999999], [17, 120.60000000000001, 141.705, 1641.8999999999999, 1667.1599999999999], [18, 98.448, 365.664, 45.0, 99.0], [18, 510.99199999999996, 822.7439999999999, 45.0, 99.0], [18, 98.448, 2297.12, 315.0, 375.0], [18, 98.448, 2297.12, 381.0, 438.0], [18, 382.072, 1844.7279999999998, 489.0, 546.0], [18, 382.072, 1736.904, 564.0, 621.0], [18, 382.072, 1842.3839999999998, 636.0, 693.0], [18, 382.072, 1856.4479999999999, 714.0, 771.0], [18, 382.072, 1842.3839999999998, 789.0, 846.0], [18, 382.072, 1800.192, 864.0, 921.0], [18, 382.072, 1844.7279999999998, 939.0, 996.0], [18, 382.072, 1851.76, 1014.0, 1071.0], [18, 382.072, 1842.3839999999998, 1089.0, 1146.0], [18, 382.072, 1816.6, 1164.0, 1221.0], [18, 382.072, 1842.3839999999998, 1239.0, 1296.0], [18, 382.072, 1814.2559999999999, 1314.0, 1371.0], [18, 382.072, 1816.6, 1389.0, 1446.0], [18, 382.072, 1851.76, 1464.0, 1521.0], [18, 382.072, 1833.0079999999998, 1539.0, 1596.0], [18, 382.072, 1814.2559999999999, 1614.0, 1671.0], [18, 382.072, 1804.8799999999999, 1689.0, 1746.0], [18, 382.072, 745.3919999999999, 1764.0, 1821.0], [18, 382.072, 700.856, 1839.0, 1893.0], [18, 382.072, 1844.7279999999998, 1914.0, 1971.0], [18, 382.072, 1844.7279999999998, 1989.0, 2046.0], [18, 382.072, 1687.6799999999998, 2064.0, 2121.0], [18, 382.072, 1680.648, 2139.0, 2196.0], [18, 382.072, 1593.9199999999998, 2211.0, 2268.0], [18, 368.008, 487.55199999999996, 2286.0, 2337.0], [18, 600.064, 792.2719999999999, 2364.0, 2415.0], [18, 602.408, 1237.6319999999998, 2439.0, 2493.0], [18, 600.064, 792.2719999999999, 2514.0, 2565.0], [18, 386.76, 914.16, 2658.0, 2709.0], [18, 386.76, 576.6239999999999, 2730.0, 2781.0], [18, 391.448, 581.312, 2940.0, 2985.0], [19, 364.826, 2103.672, 174.0, 240.0], [19, 364.826, 2134.469, 270.0, 330.0], [19, 364.826, 2101.3030000000003, 357.0, 420.0], [19, 364.826, 2106.041, 450.0, 510.0], [19, 364.826, 2146.3140000000003, 540.0, 600.0], [19, 364.826, 2124.9930000000004, 627.0, 690.0], [19, 364.826, 2103.672, 720.0, 780.0], [19, 364.826, 2094.1960000000004, 810.0, 870.0], [19, 364.826, 812.5670000000001, 900.0, 960.0], [19, 364.826, 760.4490000000001, 990.0, 1050.0], [19, 364.826, 2141.576, 1080.0, 1140.0], [19, 364.826, 2141.576, 1170.0, 1230.0], [19, 364.826, 1949.6870000000001, 1260.0, 1320.0], [19, 364.826, 1940.2110000000002, 1350.0, 1410.0], [19, 364.826, 1838.3440000000003, 1437.0, 1497.0], [19, 364.826, 497.49000000000007, 1530.0, 1584.0], [19, 634.892, 869.4230000000001, 1617.0, 1674.0], [19, 634.892, 1404.8170000000002, 1704.0, 1764.0], [19, 634.892, 869.4230000000001, 1794.0, 1851.0], [19, 364.826, 1013.9320000000001, 1974.0, 2031.0], [19, 364.826, 601.726, 2061.0, 2118.0], [19, 364.826, 601.726, 2316.0, 2370.0], [19, 727.283, 945.2310000000001, 2652.0, 2703.0], [19, 1302.95, 1949.6870000000001, 2652.0, 2703.0]]
2026-08-10 16:34:18,638 INFO     29 [qwen-vl-text] ═══ DONE ═══ 96 positions, pages=3, time=86.1s
2026-08-10 16:34:18,658 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 16:34:18,658 INFO     29 [Trace] task=dca6cdea | doc=LBZH，男，63岁，胃癌一线(1).pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "523 items", "markdown": "", "text": "", "name": "LBZH，男，63岁，胃癌一线(1).pdf", "output_format": "chunks", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_LabExam\": 1, \"chunks_Examination\": 4, \"chunks_Admission\": 1, \"chunks_Clinical\": 1}"}
2026-08-10 16:34:18,658 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 16:34:18,660 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:34:18.658+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 74, "failed": 0, "current": {"dca6cdea94d711f1bd9827cf206dfa2d": {"id": "dca6cdea94d711f1bd9827cf206dfa2d", "doc_id": "dbef275894d711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "size": 28457006, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786379026603, "task_type": "dataflow", "root_trace_id": "00f6a24fb6bd4742ba80c2030b932c44", "root_traceparent": "00-00f6a24fb6bd4742ba80c2030b932c44-fbfb6d98b4675b32-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:34:18,669 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:34:18,669 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 16:34:19,777 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:34:19,790 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 16:34:19,791 INFO     29 [Trace] task=dca6cdea | doc=LBZH，男，63岁，胃癌一线(1).pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "523 items", "markdown": "", "text": "", "name": "LBZH，男，63岁，胃癌一线(1).pdf", "output_format": "chunks", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_LabExam\": 1, \"chunks_Examination\": 4, \"chunks_Admission\": 1, \"chunks_Clinical\": 1}"}
2026-08-10 16:34:19,791 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 16:34:19,800 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:34:19,801 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 16:34:20,294 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:34:20,305 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 16:34:20,305 INFO     29 [Trace] task=dca6cdea | doc=LBZH，男，63岁，胃癌一线(1).pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "523 items", "markdown": "", "text": "", "name": "LBZH，男，63岁，胃癌一线(1).pdf", "output_format": "chunks", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_LabExam\": 1, \"chunks_Examination\": 4, \"chunks_Admission\": 1, \"chunks_Clinical\": 1}"}
2026-08-10 16:34:20,305 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 16:34:20,316 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:34:20,316 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 16:34:20,777 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:34:20,788 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 16:34:20,788 INFO     29 [Trace] task=dca6cdea | doc=LBZH，男，63岁，胃癌一线(1).pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "523 items", "markdown": "", "text": "", "name": "LBZH，男，63岁，胃癌一线(1).pdf", "output_format": "chunks", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_LabExam\": 1, \"chunks_Examination\": 4, \"chunks_Admission\": 1, \"chunks_Clinical\": 1}"}
2026-08-10 16:34:20,788 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 16:34:20,796 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:34:20,797 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:34:20,797 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-10 16:34:20,797 INFO     29 [qwen-vl-text] positions(131): [[12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:34:20,797 INFO     29 [qwen-vl-text] page grouping: [12, 13, 14, 15, 16], lines per page: [33, 20, 22, 22, 34]
2026-08-10 16:34:22,278 INFO     29 [qwen-vl-text] page=12, rect=3004x2652, img=(8345x7367), dpi=200
2026-08-10 16:34:23,776 INFO     29 [qwen-vl-text] page=13, rect=3013x2214, img=(8370x6150), dpi=200
2026-08-10 16:34:25,373 INFO     29 [qwen-vl-text] page=14, rect=3008x2963, img=(8356x8231), dpi=200
2026-08-10 16:34:26,652 INFO     29 [qwen-vl-text] page=15, rect=3006x2169, img=(8350x6025), dpi=200
2026-08-10 16:34:28,304 INFO     29 [qwen-vl-text] page=16, rect=3026x2667, img=(8406x7409), dpi=200
2026-08-10 16:34:28,310 INFO     29 [qwen-vl-text] LLM extraction start, text_len=3007
2026-08-10 16:34:28,310 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:34:28,311 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 296, \"bbox_end\": 426, \"encounter_dates\": [\"2024-12-31\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "29.11.11.73\n临时用户\n福建省肿瘤医院病历记录\n姓名\n入院记录\n姓\n出生地：福建省福\n性\n别：男\n职业：无职业\n年\n龄：61岁\n病史陈述者：患者本人\n民\n族：汉族\n可靠程度：基本可靠\n婚\n姻：已婚\n入院时间：2024年12月31日08时12分\n过敏史：未发现\n记录时间：2024年12月31日08时36分\n主诉：食管胃连接处腺癌新辅助化免治疗后术后1月余。\n现病史：患者于2024-09-02以\"进行性吞咽困难2个月\"为主诉入院。2024-08-\n23于连江县晓澳卫生院行胃镜示\"贲门肿块浸润性癌；食管下段浸润伴狭窄\"；\n胃镜病理示：（贲门）腺癌。多层螺旋CT平扫+增强扫描+MPR：1.考虑贲门-\n胃体癌伴胃周淋巴结肿大，请结合胃镜及腹部影像学检查；2.双肺多形性变\n伴纵隔、双肺门淋巴结钙化，尘肺可能，请结合病史；3.双肺上叶、右肺中\n叶较大肺大泡；4.扫及肝囊肿，请结合腹部影像学检查；病理会诊报告号（\nH24-03863）：（贲门）腺癌。相关检查未见明显化疗禁忌症，遂于\n2024.09.04、2024.09.27、2024.10.25以\"奥沙利铂 160mg ivgtt d1+5-FU\n4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w\"方案行术前第1-3周期\n129.11.11.73\n临时用户\nT牧入肿入泡；4.扫及肝囊肿，有结台腹部影像子检查；病理会诊报告号（\nH24-03863）：（贲门）腺癌。相关检查未见明显化疗禁忌症，遂于\n2024.09.04、2024.09.27、2024.10.25以\"奥沙利铂 160mg ivgtt d1+5-FU\n4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w\"方案行术前第1-3周期\n化疗，化疗过程顺利。相关检查无手术禁忌症，经充分术前准备后于2024-11\n-28在全麻下行\"腹腔镜辅助食管胃交界处癌根治术\"，术程顺利，恢复良好。\n术后病理回报（病理号：24-31776）：下段食管+近端胃切除标本：（食管胃\n交界）隆起型低分化腺癌（肿物大小8x7cm，Lauren分型：混合型），伴治疗\n反应（TRG：3级，残余肿瘤约占90%），肿瘤侵犯浆膜下层，脉管内见癌栓，\n神经见癌侵犯。标本上、下切端及另送“上切端”未见癌。淋巴结2/35见转\n移癌（“2”LN1/4、“7”LN1/14、胃小弯LN0/6、“1”LN0/2、“4”LN0/2、\n“8”LN0/6、“9”LN0/1、“11”LN0/2，“3、5”未见LN，“10”查见癌结\n节1枚）。胃小弯LN1/6、“7”LN1/14见治疗后反应。肿瘤病理分期：\nypT3N1Mx（AJCC 第八版）。免疫组化结果：MSH2（+），MSH6（+），\nMLH1（+），PMS2（+），HER2（0），CD34（血管+），D2-40（淋巴管+），\n129.1.11.73\n临时用户\n第 1 页\n129.1.11.73\n临时用户\nP53（+），EGFR（60%强着色，20%中等着色，20%弱着色），Ki-67（80% +），CD3（T细胞+，约占肿瘤区域10%），CD8（约占CD3阳性细胞数60%），\nPD1（约占CD3阳性细胞数20%），PD-L1（CPS=5），PD-L1neg（-），P40（ -），Syn（部分+），CgA（少量+），CD56（-），CK5/6（-）。原位杂交\nEBER（-）。患者无咯血丝痰；无咳嗽、盗汗，无胸痛、心悸、头晕、头痛，\n无寒战、发热，无声音嘶哑、饮水呛咳、眼睑下垂，无血尿、少尿、腰背酸\n痛。今为求进一步治疗就诊我院，门诊拟\"食管胃连接处癌新辅助化免治疗后\n术后\"收入院。发病以来精神睡眠尚可，食欲欠佳，大小便正常，体力、体重\n无明显下降。\n既往史：详见旧病历（住院号：\n个人史：详见旧病历（住院号.\n婚育史：详见旧病历（住院号：\n家族史：详见旧病历（住院号：\n73\n体格检查\nT: 36.5 ℃ P: 74 次/分 R: 12 次/分 BP: 120 / 80 mmHg\n发育正常，营养中等，表情自然，正常面容，自主体位，步入病房，步态正常。\n神志清楚，查体合作。全身皮肤粘膜无黄染、苍白、发绀、出血点、水肿、肝\n掌、溃疡、蜘蛛痣。浅表淋巴结检查详见专科情况。头颅无畸形，双眼睑无水\n肿，眼球无突出及震颤，结膜无苍白、充血、出血或水肿，巩膜无黄染，双侧\n瞳孔等大正圆，对光反射灵敏。耳廓外形正常，外耳道无分泌物，乳突无压痛。\n鼻外形正常，口唇无苍白，咽无充血，颈无抵抗，未见颈动脉异常搏动，未见\n颈静脉怒张。气管居中，甲状腺未触及肿大，质软，未及结节，未及震颤，\n间及九立 万列晾对称 未触及肿物 引业于活流 小前区子收扣 小小博动\n临时用户\n体格检查\nT: 36.5 ℃ P: 74 次/分 R: 12 次/分 BP: 120 / 80 mmHg\n发育正常，营养中等，表情自然，正常面容，自主体位，步入病房，步态正常。\n神志清楚，查体合作。全身皮肤粘膜无黄染、苍白、发绀、出血点、水肿、肝\n掌、溃疡、蜘蛛痣。浅表淋巴结检查详见专科情况。头颅无畸形，双眼睑无水\n肿，眼球无突出及震颤，结膜无苍白、充血、出血或水肿，巩膜无黄染，双侧\n瞳孔等大正圆，对光反射灵敏。耳廓外形正常，外耳道无分泌物，乳突无压痛。\n鼻外形正常，口唇无苍白，咽无充血，颈无抵抗，未见颈动脉异常搏动，未见\n颈静脉怒张。气管居中，甲状腺未触及肿大，质软，未及结节，未及震颤，未\n闻及杂音。双乳腺对称，未触及肿物，乳头无溢液。心前区无隆起，心尖搏动\n位于第5肋间左锁骨中线内0.5cm，未见异常搏动，未触及震颤，无心包摩擦感，\n心界不大，心率74次/分，心律齐，心音正常。P2<A2，未见异常血管征，各瓣\n膜听诊区未闻及杂音及心包摩擦音，腹部平坦，未见胃、肠型及蠕动波，未见\n腹壁静脉曲张，腹软，无压痛、未触及包块，Murphy征阴性，肝脾肋下未及。\n肝区肾区无叩痛，腹部叩诊鼓音，移动性浊音(-)。肠鸣音4次/分。脊柱活动\n度可，生理弯曲存在，四肢无畸形，关节无红肿及压痛，主动活动正常，双下\n129.1.11.73\n临时用户\n第 2 页\n129.1.11.73\n临时用户\n姓名\n肢无水肿。双侧膝腱反射对称引出，双侧Babinski征(-)，脑膜刺激征-，肛门\n及外生殖器未见明显异常。\n专科检查：神志清楚，营养中等。双颈、双锁骨上、双腋窝未触及肿大淋巴\n结。腹部见术痕，愈合好；胸廓无畸形，气管居中；双肺呼吸运动平稳，触\n觉语颤正常对称，叩诊清音，听诊未闻及干湿罗音及胸膜摩擦音，双肺呼吸\n音清晰。\n辅助检查：暂缺。\n出院诊断\n1、手术后恶性肿瘤化学治疗\n2、食管胃连接处隆起型低分化腺\n癌新辅助化疗后术后（\nypT3N1M0 IIIIB期）\n3、尘肺？\n4、右肝囊肿\n5、左肝胆管内结石\n6、左肾囊肿\n7、PICC置入术\n书写医生：\n2025年01月06日\n审核医生：\n2025年01月06日\n初步诊断\n1、食管胃连接处隆起型低分化腺癌新辅\n助化免治疗后术后（ypT3N1M0 IIIIB期）\n2、尘肺？\n3、右肝囊肿\n4、左肝胆管内结石\n5、左肾囊肿\n6、PICC置入术\n书写医生：\n2024年12月31日\n审核医生：\n2024年12月31日",
    "role": "user"
  }
]
2026-08-10 16:34:47,005 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:34:47,005 INFO     29 [qwen-vl-text] LLM output (len=3403):
{
  "encounter_date": "2024-12-31",
  "dm_name": null,
  "dm_gender": "男",
  "dm_age": 61,
  "dm_ethnicity": "汉族",
  "dm_marital_status": "已婚",
  "dm_occupation": "无职业",
  "dm_admission_time": "2024-12-31 08:12",
  "dm_record_time": "2024-12-31 08:36",
  "dm_history_provider": "患者本人",
  "cc_text": "食管胃连接处腺癌新辅助化免治疗后术后1月余。",
  "cc_main_symptoms": [
    "食管胃连接处腺癌新辅助化免治疗后术后"
  ],
  "cc_duration": "1月余",
  "pi_text": "患者于2024-09-02以\"进行性吞咽困难2个月\"为主诉入院。2024-08-23于连江县晓澳卫生院行胃镜示\"贲门肿块浸润性癌；食管下段浸润伴狭窄\"；胃镜病理示：（贲门）腺癌。多层螺旋CT平扫+增强扫描+MPR：1.考虑贲门-胃体癌伴胃周淋巴结肿大，请结合胃镜及腹部影像学检查；2.双肺多形性变伴纵隔、双肺门淋巴结钙化，尘肺可能，请结合病史；3.双肺上叶、右肺中叶较大肺大泡；4.扫及肝囊肿，请结合腹部影像学检查；病理会诊报告号（H24-03863）：（贲门）腺癌。相关检查未见明显化疗禁忌症，遂于2024.09.04、2024.09.27、2024.10.25以\"奥沙利铂 160mg ivgtt d1+5-FU 4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w\"方案行术前第1-3周期化疗，化疗过程顺利。相关检查无手术禁忌症，经充分术前准备后于2024-11-28在全麻下行\"腹腔镜辅助食管胃交界处癌根治术\"，术程顺利，恢复良好。术后病理回报（病理号：24-31776）：下段食管+近端胃切除标本：（食管胃交界）隆起型低分化腺癌（肿物大小8x7cm，Lauren分型：混合型），伴治疗反应（TRG：3级，残余肿瘤约占90%），肿瘤侵犯浆膜下层，脉管内见癌栓，神经见癌侵犯。标本上、下切端及另送“上切端”未见癌。淋巴结2/35见转移癌（“2”LN1/4、“7”LN1/14、胃小弯LN0/6、“1”LN0/2、“4”LN0/2、“8”LN0/6、“9”LN0/1、“11”LN0/2，“3、5”未见LN，“10”查见癌结节1枚）。胃小弯LN1/6、“7”LN1/14见治疗后反应。肿瘤病理分期：ypT3N1Mx（AJCC 第八版）。免疫组化结果：MSH2（+），MSH6（+），MLH1（+），PMS2（+），HER2（0），CD34（血管+），D2-40（淋巴管+），P53（+），EGFR（60%强着色，20%中等着色，20%弱着色），Ki-67（80% +），CD3（T细胞+，约占肿瘤区域10%），CD8（约占CD3阳性细胞数60%），PD1（约占CD3阳性细胞数20%），PD-L1（CPS=5），PD-L1neg（-），P40（ -），Syn（部分+），CgA（少量+），CD56（-），CK5/6（-）。原位杂交EBER（-）。患者无咯血丝痰；无咳嗽、盗汗，无胸痛、心悸、头晕、头痛，无寒战、发热，无声音嘶哑、饮水呛咳、眼睑下垂，无血尿、少尿、腰背酸痛。今为求进一步治疗就诊我院，门诊拟\"食管胃连接处癌新辅助化免治疗后术后\"收入院。发病以来精神睡眠尚可，食欲欠佳，大小便正常，体力、体重无明显下降。",
  "pmh_disease_history": [],
  "pmh_allergy_history": [
    "未发现"
  ],
  "pmh_surgery_trauma_history": [],
  "ph_smoking": null,
  "ph_drinking": null,
  "oh_menarche_age": null,
  "oh_menopause_age": null,
  "oh_pregnancies": null,
  "fh_text": "详见旧病历（住院号：",
  "fh_hereditary_diseases": [],
  "vs_temperature_c": 36.5,
  "vs_pulse_bpm": 74,
  "vs_respiration_rpm": 12,
  "vs_systolic_bp_mmhg": 120,
  "vs_diastolic_bp_mmhg": 80,
  "pe_general_condition": "发育正常，营养中等，表情自然，正常面容，自主体位，步入病房，步态正常。神志清楚，查体合作。",
  "pe_skin_mucosa": "全身皮肤粘膜无黄染、苍白、发绀、出血点、水肿、肝掌、溃疡、蜘蛛痣。",
  "pe_lymph_nodes": "浅表淋巴结检查详见专科情况。",
  "pe_lungs": "双肺呼吸运动平稳，触觉语颤正常对称，叩诊清音，听诊未闻及干湿罗音及胸膜摩擦音，双肺呼吸音清晰。",
  "pe_heart": "心前区无隆起，心尖搏动位于第5肋间左锁骨中线内0.5cm，未见异常搏动，未触及震颤，无心包摩擦感，心界不大，心率74次/分，心律齐，心音正常。P2<A2，未见异常血管征，各瓣膜听诊区未闻及杂音及心包摩擦音。",
  "pe_abdomen": "腹部平坦，未见胃、肠型及蠕动波，未见腹壁静脉曲张，腹软，无压痛、未触及包块，Murphy征阴性，肝脾肋下未及。肝区肾区无叩痛，腹部叩诊鼓音，移动性浊音(-)。肠鸣音4次/分。",
  "pe_extremities": "脊柱活动度可，生理弯曲存在，四肢无畸形，关节无红肿及压痛，主动活动正常，双下肢无水肿。",
  "pe_nervous_system": "双侧膝腱反射对称引出，双侧Babinski征(-)，脑膜刺激征-。",
  "pe_specialist_exam": "神志清楚，营养中等。双颈、双锁骨上、双腋窝未触及肿大淋巴结。腹部见术痕，愈合好；胸廓无畸形，气管居中；双肺呼吸运动平稳，触觉语颤正常对称，叩诊清音，听诊未闻及干湿罗音及胸膜摩擦音，双肺呼吸音清晰。",
  "pe_ecog_score": null,
  "pat_text": "暂缺。",
  "pat_items": [],
  "preliminary_diagnoses": [
    {
      "name": "食管胃连接处隆起型低分化腺癌新辅助化免治疗后术后（ypT3N1M0 IIIIB期）",
      "diagnosis_type": "西医",
      "is_primary": true
    },
    {
      "name": "尘肺？",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "右肝囊肿",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "左肝胆管内结石",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "左肾囊肿",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "PICC置入术",
      "diagnosis_type": "西医",
      "is_primary": false
    }
  ],
  "department": null
}
2026-08-10 16:34:47,005 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-12-31]
2026-08-10 16:34:47,036 INFO     29 [qwen-vl-text] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=14792985, prompt_len=1288
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["29.11.11.73", "临时用户", "福建省肿瘤医院病历记录", "姓名", "入院记录", "姓", "出生地：福建省福", "性", "别：男", "职业：无职业", "年", "龄：61岁", "病史陈述者：患者本人", "民", "族：汉族", "可靠程度：基本可靠", "婚", "姻：已婚", "入院时间：2024年12月31日08时12分", "过敏史：未发现", "记录时间：2024年12月31日08时36分", "主诉：食管胃连接处腺癌新辅助化免治疗后术后1月余。", "现病史：患者于2024-09-02以\"进行性吞咽困难2个月\"为主诉入院。2024-08-", "23于连江县晓澳卫生院行胃镜示\"贲门肿块浸润性癌；食管下段浸润伴狭窄\"；", "胃镜病理示：（贲门）腺癌。多层螺旋CT平扫+增强扫描+MPR：1.考虑贲门-", "胃体癌伴胃周淋巴结肿大，请结合胃镜及腹部影像学检查；2.双肺多形性变", "伴纵隔、双肺门淋巴结钙化，尘肺可能，请结合病史；3.双肺上叶、右肺中", "叶较大肺大泡；4.扫及肝囊肿，请结合腹部影像学检查；病理会诊报告号（", "H24-03863）：（贲门）腺癌。相关检查未见明显化疗禁忌症，遂于", "2024.09.04、2024.09.27、2024.10.25以\"奥沙利铂 160mg ivgtt d1+5-FU", "4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w\"方案行术前第1-3周期", "129.11.11.73", "临时用户"]

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
2026-08-10 16:35:09,511 INFO     29 [qwen-vl-text] coord API raw response (len=2020):
[
	{"text": "29.11.11.73", "bbox": [0, 0, 304, 43]},
	{"text": "临时用户", "bbox": [36, 48, 262, 112]},
	{"text": "福建省肿瘤医院病历记录", "bbox": [313, 88, 725, 131]},
	{"text": "姓名", "bbox": [113, 169, 158, 198]},
	{"text": "入院记录", "bbox": [385, 230, 664, 261]},
	{"text": "姓", "bbox": [125, 277, 150, 305]},
	{"text": "出生地：福建省福", "bbox": [447, 277, 635, 305]},
	{"text": "性", "bbox": [128, 320, 152, 348]},
	{"text": "别：男", "bbox": [175, 320, 243, 348]},
	{"text": "职业：无职业", "bbox": [446, 320, 587, 348]},
	{"text": "年", "bbox": [129, 363, 153, 391]},
	{"text": "龄：61岁", "bbox": [176, 363, 269, 391]},
	{"text": "病史陈述者：患者本人", "bbox": [445, 363, 690, 391]},
	{"text": "民", "bbox": [132, 406, 154, 434]},
	{"text": "族：汉族", "bbox": [177, 406, 272, 434]},
	{"text": "可靠程度：基本可靠", "bbox": [446, 406, 667, 434]},
	{"text": "婚", "bbox": [131, 448, 156, 476]},
	{"text": "姻：已婚", "bbox": [178, 448, 274, 476]},
	{"text": "入院时间：2024年12月31日08时12分", "bbox": [447, 450, 834, 478]},
	{"text": "过敏史：未发现", "bbox": [132, 491, 312, 520]},
	{"text": "记录时间：2024年12月31日08时36分", "bbox": [447, 493, 834, 521]},
	{"text": "主诉：食管胃连接处腺癌新辅助化免治疗后术后1月余。", "bbox": [125, 580, 738, 612]},
	{"text": "现病史：患者于2024-09-02以\"进行性吞咽困难2个月\"为主诉入院。2024-08-", "bbox": [125, 623, 927, 655]},
	{"text": "23于连江县晓澳卫生院行胃镜示\"贲门肿块浸润性癌；食管下段浸润伴狭窄\"；", "bbox": [125, 666, 910, 697]},
	{"text": "胃镜病理示：（贲门）腺癌。多层螺旋CT平扫+增强扫描+MPR：1.考虑贲门-", "bbox": [128, 708, 924, 739]},
	{"text": "胃体癌伴胃周淋巴结肿大，请结合胃镜及腹部影像学检查；2.双肺多形性变", "bbox": [128, 750, 922, 781]},
	{"text": "伴纵隔、双肺门淋巴结钙化，尘肺可能，请结合病史；3.双肺上叶、右肺中", "bbox": [128, 792, 920, 823]},
	{"text": "叶较大肺大泡；4.扫及肝囊肿，请结合腹部影像学检查；病理会诊报告号（", "bbox": [128, 834, 918, 865]},
	{"text": "H24-03863）：（贲门）腺癌。相关检查未见明显化疗禁忌症，遂于", "bbox": [128, 876, 918, 907]},
	{"text": "2024.09.04、2024.09.27、2024.10.25以\"奥沙利铂 160mg ivgtt d1+5-FU", "bbox": [128, 918, 910, 948]},
	{"text": "4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w\"方案行术前第1-3周期", "bbox": [128, 960, 920, 990]},
	{"text": "129.11.11.73", "bbox": [685, 0, 1000, 35]},
	{"text": "临时用户", "bbox": [723, 44, 952, 107]}
]
2026-08-10 16:35:09,511 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=22.5s
2026-08-10 16:35:09,511 INFO     29 [qwen-vl-text] coord item[0]: text=29.11.11.73, bbox=[0, 0, 304, 43]
2026-08-10 16:35:09,511 INFO     29 [qwen-vl-text] coord item[1]: text=临时用户, bbox=[36, 48, 262, 112]
2026-08-10 16:35:09,511 INFO     29 [qwen-vl-text] coord item[2]: text=福建省肿瘤医院病历记录, bbox=[313, 88, 725, 131]
2026-08-10 16:35:09,511 INFO     29 [qwen-vl-text] coord item[3]: text=姓名, bbox=[113, 169, 158, 198]
2026-08-10 16:35:09,511 INFO     29 [qwen-vl-text] coord item[4]: text=入院记录, bbox=[385, 230, 664, 261]
2026-08-10 16:35:09,511 INFO     29 [qwen-vl-text] coord item[5]: text=姓, bbox=[125, 277, 150, 305]
2026-08-10 16:35:09,511 INFO     29 [qwen-vl-text] coord item[6]: text=出生地：福建省福, bbox=[447, 277, 635, 305]
2026-08-10 16:35:09,511 INFO     29 [qwen-vl-text] coord item[7]: text=性, bbox=[128, 320, 152, 348]
2026-08-10 16:35:09,511 INFO     29 [qwen-vl-text] coord item[8]: text=别：男, bbox=[175, 320, 243, 348]
2026-08-10 16:35:09,511 INFO     29 [qwen-vl-text] coord item[9]: text=职业：无职业, bbox=[446, 320, 587, 348]
2026-08-10 16:35:09,512 INFO     29 [qwen-vl-text] coord item[10]: text=年, bbox=[129, 363, 153, 391]
2026-08-10 16:35:09,512 INFO     29 [qwen-vl-text] coord item[11]: text=龄：61岁, bbox=[176, 363, 269, 391]
2026-08-10 16:35:09,512 INFO     29 [qwen-vl-text] coord item[12]: text=病史陈述者：患者本人, bbox=[445, 363, 690, 391]
2026-08-10 16:35:09,512 INFO     29 [qwen-vl-text] coord item[13]: text=民, bbox=[132, 406, 154, 434]
2026-08-10 16:35:09,512 INFO     29 [qwen-vl-text] coord item[14]: text=族：汉族, bbox=[177, 406, 272, 434]
2026-08-10 16:35:09,512 INFO     29 [qwen-vl-text] coord item[15]: text=可靠程度：基本可靠, bbox=[446, 406, 667, 434]
2026-08-10 16:35:09,512 INFO     29 [qwen-vl-text] coord item[16]: text=婚, bbox=[131, 448, 156, 476]
2026-08-10 16:35:09,512 INFO     29 [qwen-vl-text] coord item[17]: text=姻：已婚, bbox=[178, 448, 274, 476]
2026-08-10 16:35:09,512 INFO     29 [qwen-vl-text] coord item[18]: text=入院时间：2024年12月31日08时12分, bbox=[447, 450, 834, 478]
2026-08-10 16:35:09,512 INFO     29 [qwen-vl-text] coord item[19]: text=过敏史：未发现, bbox=[132, 491, 312, 520]
2026-08-10 16:35:09,512 INFO     29 [qwen-vl-text] coord item[20]: text=记录时间：2024年12月31日08时36分, bbox=[447, 493, 834, 521]
2026-08-10 16:35:09,512 INFO     29 [qwen-vl-text] coord item[21]: text=主诉：食管胃连接处腺癌新辅助化免治疗后术后1月余。, bbox=[125, 580, 738, 612]
2026-08-10 16:35:09,512 INFO     29 [qwen-vl-text] coord item[22]: text=现病史：患者于2024-09-02以"进行性吞咽困难2个月"为主诉入院。2024-08-, bbox=[125, 623, 927, 655]
2026-08-10 16:35:09,512 INFO     29 [qwen-vl-text] coord item[23]: text=23于连江县晓澳卫生院行胃镜示"贲门肿块浸润性癌；食管下段浸润伴狭窄"；, bbox=[125, 666, 910, 697]
2026-08-10 16:35:09,512 INFO     29 [qwen-vl-text] coord item[24]: text=胃镜病理示：（贲门）腺癌。多层螺旋CT平扫+增强扫描+MPR：1.考虑贲门-, bbox=[128, 708, 924, 739]
2026-08-10 16:35:09,512 INFO     29 [qwen-vl-text] coord item[25]: text=胃体癌伴胃周淋巴结肿大，请结合胃镜及腹部影像学检查；2.双肺多形性变, bbox=[128, 750, 922, 781]
2026-08-10 16:35:09,512 INFO     29 [qwen-vl-text] coord item[26]: text=伴纵隔、双肺门淋巴结钙化，尘肺可能，请结合病史；3.双肺上叶、右肺中, bbox=[128, 792, 920, 823]
2026-08-10 16:35:09,512 INFO     29 [qwen-vl-text] coord item[27]: text=叶较大肺大泡；4.扫及肝囊肿，请结合腹部影像学检查；病理会诊报告号（, bbox=[128, 834, 918, 865]
2026-08-10 16:35:09,512 INFO     29 [qwen-vl-text] coord item[28]: text=H24-03863）：（贲门）腺癌。相关检查未见明显化疗禁忌症，遂于, bbox=[128, 876, 918, 907]
2026-08-10 16:35:09,512 INFO     29 [qwen-vl-text] coord item[29]: text=2024.09.04、2024.09.27、2024.10.25以"奥沙利铂 160mg ivgtt d1+5-FU, bbox=[128, 918, 910, 948]
2026-08-10 16:35:09,512 INFO     29 [qwen-vl-text] coord item[30]: text=4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w"方案行术前第1-3周期, bbox=[128, 960, 920, 990]
2026-08-10 16:35:09,512 INFO     29 [qwen-vl-text] coord item[31]: text=129.11.11.73, bbox=[685, 0, 1000, 35]
2026-08-10 16:35:09,512 INFO     29 [qwen-vl-text] coord item[32]: text=临时用户, bbox=[723, 44, 952, 107]
2026-08-10 16:35:09,514 INFO     29 [qwen-vl-text] page=12 — 33/33 coords, api_time=22.5s
2026-08-10 16:35:09,541 INFO     29 [qwen-vl-text] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=13610082, prompt_len=1347
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共20行）
["T牧入肿入泡；4.扫及肝囊肿，有结台腹部影像子检查；病理会诊报告号（", "H24-03863）：（贲门）腺癌。相关检查未见明显化疗禁忌症，遂于", "2024.09.04、2024.09.27、2024.10.25以\"奥沙利铂 160mg ivgtt d1+5-FU", "4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w\"方案行术前第1-3周期", "化疗，化疗过程顺利。相关检查无手术禁忌症，经充分术前准备后于2024-11", "-28在全麻下行\"腹腔镜辅助食管胃交界处癌根治术\"，术程顺利，恢复良好。", "术后病理回报（病理号：24-31776）：下段食管+近端胃切除标本：（食管胃", "交界）隆起型低分化腺癌（肿物大小8x7cm，Lauren分型：混合型），伴治疗", "反应（TRG：3级，残余肿瘤约占90%），肿瘤侵犯浆膜下层，脉管内见癌栓，", "神经见癌侵犯。标本上、下切端及另送“上切端”未见癌。淋巴结2/35见转", "移癌（“2”LN1/4、“7”LN1/14、胃小弯LN0/6、“1”LN0/2、“4”LN0/2、", "“8”LN0/6、“9”LN0/1、“11”LN0/2，“3、5”未见LN，“10”查见癌结", "节1枚）。胃小弯LN1/6、“7”LN1/14见治疗后反应。肿瘤病理分期：", "ypT3N1Mx（AJCC 第八版）。免疫组化结果：MSH2（+），MSH6（+），", "MLH1（+），PMS2（+），HER2（0），CD34（血管+），D2-40（淋巴管+），", "129.1.11.73", "临时用户", "第 1 页", "129.1.11.73", "临时用户"]

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
2026-08-10 16:35:26,972 INFO     29 [qwen-vl-text] coord API raw response (len=1553):
[
	{"text": "T牧入肿入泡；4.扫及肝囊肿，有结台腹部影像子检查；病理会诊报告号（", "bbox": [124, 48, 909, 79]},
	{"text": "H24-03863）：（贲门）腺癌。相关检查未见明显化疗禁忌症，遂于", "bbox": [122, 90, 909, 127]},
	{"text": "2024.09.04、2024.09.27、2024.10.25以\"奥沙利铂 160mg ivgtt d1+5-FU", "bbox": [122, 139, 909, 177]},
	{"text": "4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w\"方案行术前第1-3周期", "bbox": [122, 190, 911, 227]},
	{"text": "化疗，化疗过程顺利。相关检查无手术禁忌症，经充分术前准备后于2024-11", "bbox": [122, 240, 911, 277]},
	{"text": "-28在全麻下行\"腹腔镜辅助食管胃交界处癌根治术\"，术程顺利，恢复良好。", "bbox": [122, 290, 901, 327]},
	{"text": "术后病理回报（病理号：24-31776）：下段食管+近端胃切除标本：（食管胃", "bbox": [122, 341, 911, 378]},
	{"text": "交界）隆起型低分化腺癌（肿物大小8x7cm，Lauren分型：混合型），伴治疗", "bbox": [122, 392, 911, 429]},
	{"text": "反应（TRG：3级，残余肿瘤约占90%），肿瘤侵犯浆膜下层，脉管内见癌栓，", "bbox": [122, 443, 901, 480]},
	{"text": "神经见癌侵犯。标本上、下切端及另送“上切端”未见癌。淋巴结2/35见转", "bbox": [122, 494, 911, 531]},
	{"text": "移癌（“2”LN1/4、“7”LN1/14、胃小弯LN0/6、“1”LN0/2、“4”LN0/2、", "bbox": [122, 545, 901, 582]},
	{"text": "“8”LN0/6、“9”LN0/1、“11”LN0/2，“3、5”未见LN，“10”查见癌结", "bbox": [132, 596, 911, 633]},
	{"text": "节1枚）。胃小弯LN1/6、“7”LN1/14见治疗后反应。肿瘤病理分期：", "bbox": [122, 647, 901, 684]},
	{"text": "ypT3N1Mx（AJCC 第八版）。免疫组化结果：MSH2（+），MSH6（+），", "bbox": [122, 698, 901, 735]},
	{"text": "MLH1（+），PMS2（+），HER2（0），CD34（血管+），D2-40（淋巴管+），", "bbox": [122, 749, 901, 786]},
	{"text": "129.1.11.73", "bbox": [678, 765, 978, 830]},
	{"text": "临时用户", "bbox": [45, 838, 267, 913]},
	{"text": "第 1 页", "bbox": [474, 814, 575, 849]},
	{"text": "129.1.11.73", "bbox": [678, 765, 978, 830]},
	{"text": "临时用户", "bbox": [718, 838, 937, 913]}
]
2026-08-10 16:35:26,972 INFO     29 [qwen-vl-text] coord API: raw_items=20, valid_items=20, elapsed=17.4s
2026-08-10 16:35:26,972 INFO     29 [qwen-vl-text] coord item[0]: text=T牧入肿入泡；4.扫及肝囊肿，有结台腹部影像子检查；病理会诊报告号（, bbox=[124, 48, 909, 79]
2026-08-10 16:35:26,972 INFO     29 [qwen-vl-text] coord item[1]: text=H24-03863）：（贲门）腺癌。相关检查未见明显化疗禁忌症，遂于, bbox=[122, 90, 909, 127]
2026-08-10 16:35:26,972 INFO     29 [qwen-vl-text] coord item[2]: text=2024.09.04、2024.09.27、2024.10.25以"奥沙利铂 160mg ivgtt d1+5-FU, bbox=[122, 139, 909, 177]
2026-08-10 16:35:26,972 INFO     29 [qwen-vl-text] coord item[3]: text=4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w"方案行术前第1-3周期, bbox=[122, 190, 911, 227]
2026-08-10 16:35:26,972 INFO     29 [qwen-vl-text] coord item[4]: text=化疗，化疗过程顺利。相关检查无手术禁忌症，经充分术前准备后于2024-11, bbox=[122, 240, 911, 277]
2026-08-10 16:35:26,972 INFO     29 [qwen-vl-text] coord item[5]: text=-28在全麻下行"腹腔镜辅助食管胃交界处癌根治术"，术程顺利，恢复良好。, bbox=[122, 290, 901, 327]
2026-08-10 16:35:26,972 INFO     29 [qwen-vl-text] coord item[6]: text=术后病理回报（病理号：24-31776）：下段食管+近端胃切除标本：（食管胃, bbox=[122, 341, 911, 378]
2026-08-10 16:35:26,972 INFO     29 [qwen-vl-text] coord item[7]: text=交界）隆起型低分化腺癌（肿物大小8x7cm，Lauren分型：混合型），伴治疗, bbox=[122, 392, 911, 429]
2026-08-10 16:35:26,972 INFO     29 [qwen-vl-text] coord item[8]: text=反应（TRG：3级，残余肿瘤约占90%），肿瘤侵犯浆膜下层，脉管内见癌栓，, bbox=[122, 443, 901, 480]
2026-08-10 16:35:26,972 INFO     29 [qwen-vl-text] coord item[9]: text=神经见癌侵犯。标本上、下切端及另送“上切端”未见癌。淋巴结2/35见转, bbox=[122, 494, 911, 531]
2026-08-10 16:35:26,972 INFO     29 [qwen-vl-text] coord item[10]: text=移癌（“2”LN1/4、“7”LN1/14、胃小弯LN0/6、“1”LN0/2、“4”LN0/2、, bbox=[122, 545, 901, 582]
2026-08-10 16:35:26,972 INFO     29 [qwen-vl-text] coord item[11]: text=“8”LN0/6、“9”LN0/1、“11”LN0/2，“3、5”未见LN，“10”查见癌结, bbox=[132, 596, 911, 633]
2026-08-10 16:35:26,972 INFO     29 [qwen-vl-text] coord item[12]: text=节1枚）。胃小弯LN1/6、“7”LN1/14见治疗后反应。肿瘤病理分期：, bbox=[122, 647, 901, 684]
2026-08-10 16:35:26,972 INFO     29 [qwen-vl-text] coord item[13]: text=ypT3N1Mx（AJCC 第八版）。免疫组化结果：MSH2（+），MSH6（+），, bbox=[122, 698, 901, 735]
2026-08-10 16:35:26,972 INFO     29 [qwen-vl-text] coord item[14]: text=MLH1（+），PMS2（+），HER2（0），CD34（血管+），D2-40（淋巴管+），, bbox=[122, 749, 901, 786]
2026-08-10 16:35:26,972 INFO     29 [qwen-vl-text] coord item[15]: text=129.1.11.73, bbox=[678, 765, 978, 830]
2026-08-10 16:35:26,972 INFO     29 [qwen-vl-text] coord item[16]: text=临时用户, bbox=[45, 838, 267, 913]
2026-08-10 16:35:26,972 INFO     29 [qwen-vl-text] coord item[17]: text=第 1 页, bbox=[474, 814, 575, 849]
2026-08-10 16:35:26,972 INFO     29 [qwen-vl-text] coord item[18]: text=129.1.11.73, bbox=[678, 765, 978, 830]
2026-08-10 16:35:26,972 INFO     29 [qwen-vl-text] coord item[19]: text=临时用户, bbox=[718, 838, 937, 913]
2026-08-10 16:35:26,974 INFO     29 [qwen-vl-text] page=13 — 20/20 coords, api_time=17.4s
2026-08-10 16:35:27,004 INFO     29 [qwen-vl-text] coord API call start, page=14, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=15397364, prompt_len=1405
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["P53（+），EGFR（60%强着色，20%中等着色，20%弱着色），Ki-67（80% +），CD3（T细胞+，约占肿瘤区域10%），CD8（约占CD3阳性细胞数60%），", "PD1（约占CD3阳性细胞数20%），PD-L1（CPS=5），PD-L1neg（-），P40（ -），Syn（部分+），CgA（少量+），CD56（-），CK5/6（-）。原位杂交", "EBER（-）。患者无咯血丝痰；无咳嗽、盗汗，无胸痛、心悸、头晕、头痛，", "无寒战、发热，无声音嘶哑、饮水呛咳、眼睑下垂，无血尿、少尿、腰背酸", "痛。今为求进一步治疗就诊我院，门诊拟\"食管胃连接处癌新辅助化免治疗后", "术后\"收入院。发病以来精神睡眠尚可，食欲欠佳，大小便正常，体力、体重", "无明显下降。", "既往史：详见旧病历（住院号：", "个人史：详见旧病历（住院号.", "婚育史：详见旧病历（住院号：", "家族史：详见旧病历（住院号：", "73", "体格检查", "T: 36.5 ℃ P: 74 次/分 R: 12 次/分 BP: 120 / 80 mmHg", "发育正常，营养中等，表情自然，正常面容，自主体位，步入病房，步态正常。", "神志清楚，查体合作。全身皮肤粘膜无黄染、苍白、发绀、出血点、水肿、肝", "掌、溃疡、蜘蛛痣。浅表淋巴结检查详见专科情况。头颅无畸形，双眼睑无水", "肿，眼球无突出及震颤，结膜无苍白、充血、出血或水肿，巩膜无黄染，双侧", "瞳孔等大正圆，对光反射灵敏。耳廓外形正常，外耳道无分泌物，乳突无压痛。", "鼻外形正常，口唇无苍白，咽无充血，颈无抵抗，未见颈动脉异常搏动，未见", "颈静脉怒张。气管居中，甲状腺未触及肿大，质软，未及结节，未及震颤，", "间及九立 万列晾对称 未触及肿物 引业于活流 小前区子收扣 小小博动"]

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
2026-08-10 16:35:47,584 INFO     29 [qwen-vl-text] coord API raw response (len=1693):
[
	{"text": "P53（+），EGFR（60%强着色，20%中等着色，20%弱着色），Ki-67（80% +），CD3（T细胞+，约占肿瘤区域10%），CD8（约占CD3阳性细胞数60%），", "bbox": [98, 85, 912, 118]},
	{"text": "PD1（约占CD3阳性细胞数20%），PD-L1（CPS=5），PD-L1neg（-），P40（ -），Syn（部分+），CgA（少量+），CD56（-），CK5/6（-）。原位杂交", "bbox": [98, 158, 912, 192]},
	{"text": "EBER（-）。患者无咯血丝痰；无咳嗽、盗汗，无胸痛、心悸、头晕、头痛，", "bbox": [98, 215, 908, 248]},
	{"text": "无寒战、发热，无声音嘶哑、饮水呛咳、眼睑下垂，无血尿、少尿、腰背酸", "bbox": [100, 280, 912, 313]},
	{"text": "痛。今为求进一步治疗就诊我院，门诊拟\"食管胃连接处癌新辅助化免治疗后", "bbox": [100, 321, 912, 353]},
	{"text": "术后\"收入院。发病以来精神睡眠尚可，食欲欠佳，大小便正常，体力、体重", "bbox": [100, 362, 912, 393]},
	{"text": "无明显下降。", "bbox": [100, 398, 260, 427]},
	{"text": "既往史：详见旧病历（住院号：", "bbox": [102, 437, 428, 466]},
	{"text": "个人史：详见旧病历（住院号.", "bbox": [102, 475, 428, 504]},
	{"text": "婚育史：详见旧病历（住院号：", "bbox": [102, 514, 428, 543]},
	{"text": "家族史：详见旧病历（住院号：", "bbox": [102, 551, 428, 583]},
	{"text": "73", "bbox": [591, 545, 642, 588]},
	{"text": "体格检查", "bbox": [445, 592, 578, 619]},
	{"text": "T: 36.5 ℃ P: 74 次/分 R: 12 次/分 BP: 120 / 80 mmHg", "bbox": [102, 624, 874, 655]},
	{"text": "发育正常，营养中等，表情自然，正常面容，自主体位，步入病房，步态正常。", "bbox": [102, 663, 900, 692]},
	{"text": "神志清楚，查体合作。全身皮肤粘膜无黄染、苍白、发绀、出血点、水肿、肝", "bbox": [102, 701, 912, 730]},
	{"text": "掌、溃疡、蜘蛛痣。浅表淋巴结检查详见专科情况。头颅无畸形，双眼睑无水", "bbox": [102, 738, 912, 768]},
	{"text": "肿，眼球无突出及震颤，结膜无苍白、充血、出血或水肿，巩膜无黄染，双侧", "bbox": [102, 777, 912, 807]},
	{"text": "瞳孔等大正圆，对光反射灵敏。耳廓外形正常，外耳道无分泌物，乳突无压痛。", "bbox": [102, 815, 900, 845]},
	{"text": "鼻外形正常，口唇无苍白，咽无充血，颈无抵抗，未见颈动脉异常搏动，未见", "bbox": [102, 854, 912, 884]},
	{"text": "颈静脉怒张。气管居中，甲状腺未触及肿大，质软，未及结节，未及震颤，", "bbox": [102, 892, 920, 922]},
	{"text": "间及九立 万列晾对称 未触及肿物 引业于活流 小前区子收扣 小小博动", "bbox": [102, 930, 912, 950]}
]
2026-08-10 16:35:47,584 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=20.6s
2026-08-10 16:35:47,584 INFO     29 [qwen-vl-text] coord item[0]: text=P53（+），EGFR（60%强着色，20%中等着色，20%弱着色），Ki-67（80% +），CD3（T细胞+，约占肿瘤区域10%），CD8（约占CD3阳性细胞数60%），, bbox=[98, 85, 912, 118]
2026-08-10 16:35:47,584 INFO     29 [qwen-vl-text] coord item[1]: text=PD1（约占CD3阳性细胞数20%），PD-L1（CPS=5），PD-L1neg（-），P40（ -），Syn（部分+），CgA（少量+），CD56（-），CK5/6（-）。原位杂交, bbox=[98, 158, 912, 192]
2026-08-10 16:35:47,584 INFO     29 [qwen-vl-text] coord item[2]: text=EBER（-）。患者无咯血丝痰；无咳嗽、盗汗，无胸痛、心悸、头晕、头痛，, bbox=[98, 215, 908, 248]
2026-08-10 16:35:47,584 INFO     29 [qwen-vl-text] coord item[3]: text=无寒战、发热，无声音嘶哑、饮水呛咳、眼睑下垂，无血尿、少尿、腰背酸, bbox=[100, 280, 912, 313]
2026-08-10 16:35:47,584 INFO     29 [qwen-vl-text] coord item[4]: text=痛。今为求进一步治疗就诊我院，门诊拟"食管胃连接处癌新辅助化免治疗后, bbox=[100, 321, 912, 353]
2026-08-10 16:35:47,584 INFO     29 [qwen-vl-text] coord item[5]: text=术后"收入院。发病以来精神睡眠尚可，食欲欠佳，大小便正常，体力、体重, bbox=[100, 362, 912, 393]
2026-08-10 16:35:47,584 INFO     29 [qwen-vl-text] coord item[6]: text=无明显下降。, bbox=[100, 398, 260, 427]
2026-08-10 16:35:47,584 INFO     29 [qwen-vl-text] coord item[7]: text=既往史：详见旧病历（住院号：, bbox=[102, 437, 428, 466]
2026-08-10 16:35:47,584 INFO     29 [qwen-vl-text] coord item[8]: text=个人史：详见旧病历（住院号., bbox=[102, 475, 428, 504]
2026-08-10 16:35:47,584 INFO     29 [qwen-vl-text] coord item[9]: text=婚育史：详见旧病历（住院号：, bbox=[102, 514, 428, 543]
2026-08-10 16:35:47,584 INFO     29 [qwen-vl-text] coord item[10]: text=家族史：详见旧病历（住院号：, bbox=[102, 551, 428, 583]
2026-08-10 16:35:47,584 INFO     29 [qwen-vl-text] coord item[11]: text=73, bbox=[591, 545, 642, 588]
2026-08-10 16:35:47,584 INFO     29 [qwen-vl-text] coord item[12]: text=体格检查, bbox=[445, 592, 578, 619]
2026-08-10 16:35:47,584 INFO     29 [qwen-vl-text] coord item[13]: text=T: 36.5 ℃ P: 74 次/分 R: 12 次/分 BP: 120 / 80 mmHg, bbox=[102, 624, 874, 655]
2026-08-10 16:35:47,584 INFO     29 [qwen-vl-text] coord item[14]: text=发育正常，营养中等，表情自然，正常面容，自主体位，步入病房，步态正常。, bbox=[102, 663, 900, 692]
2026-08-10 16:35:47,584 INFO     29 [qwen-vl-text] coord item[15]: text=神志清楚，查体合作。全身皮肤粘膜无黄染、苍白、发绀、出血点、水肿、肝, bbox=[102, 701, 912, 730]
2026-08-10 16:35:47,584 INFO     29 [qwen-vl-text] coord item[16]: text=掌、溃疡、蜘蛛痣。浅表淋巴结检查详见专科情况。头颅无畸形，双眼睑无水, bbox=[102, 738, 912, 768]
2026-08-10 16:35:47,584 INFO     29 [qwen-vl-text] coord item[17]: text=肿，眼球无突出及震颤，结膜无苍白、充血、出血或水肿，巩膜无黄染，双侧, bbox=[102, 777, 912, 807]
2026-08-10 16:35:47,584 INFO     29 [qwen-vl-text] coord item[18]: text=瞳孔等大正圆，对光反射灵敏。耳廓外形正常，外耳道无分泌物，乳突无压痛。, bbox=[102, 815, 900, 845]
2026-08-10 16:35:47,584 INFO     29 [qwen-vl-text] coord item[19]: text=鼻外形正常，口唇无苍白，咽无充血，颈无抵抗，未见颈动脉异常搏动，未见, bbox=[102, 854, 912, 884]
2026-08-10 16:35:47,584 INFO     29 [qwen-vl-text] coord item[20]: text=颈静脉怒张。气管居中，甲状腺未触及肿大，质软，未及结节，未及震颤，, bbox=[102, 892, 920, 922]
2026-08-10 16:35:47,584 INFO     29 [qwen-vl-text] coord item[21]: text=间及九立 万列晾对称 未触及肿物 引业于活流 小前区子收扣 小小博动, bbox=[102, 930, 912, 950]
2026-08-10 16:35:47,587 INFO     29 [qwen-vl-text] page=14 — 22/22 coords, api_time=20.6s
2026-08-10 16:35:47,613 INFO     29 [qwen-vl-text] coord API call start, page=15, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=13190189, prompt_len=1281
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["临时用户", "体格检查", "T: 36.5 ℃ P: 74 次/分 R: 12 次/分 BP: 120 / 80 mmHg", "发育正常，营养中等，表情自然，正常面容，自主体位，步入病房，步态正常。", "神志清楚，查体合作。全身皮肤粘膜无黄染、苍白、发绀、出血点、水肿、肝", "掌、溃疡、蜘蛛痣。浅表淋巴结检查详见专科情况。头颅无畸形，双眼睑无水", "肿，眼球无突出及震颤，结膜无苍白、充血、出血或水肿，巩膜无黄染，双侧", "瞳孔等大正圆，对光反射灵敏。耳廓外形正常，外耳道无分泌物，乳突无压痛。", "鼻外形正常，口唇无苍白，咽无充血，颈无抵抗，未见颈动脉异常搏动，未见", "颈静脉怒张。气管居中，甲状腺未触及肿大，质软，未及结节，未及震颤，未", "闻及杂音。双乳腺对称，未触及肿物，乳头无溢液。心前区无隆起，心尖搏动", "位于第5肋间左锁骨中线内0.5cm，未见异常搏动，未触及震颤，无心包摩擦感，", "心界不大，心率74次/分，心律齐，心音正常。P2<A2，未见异常血管征，各瓣", "膜听诊区未闻及杂音及心包摩擦音，腹部平坦，未见胃、肠型及蠕动波，未见", "腹壁静脉曲张，腹软，无压痛、未触及包块，Murphy征阴性，肝脾肋下未及。", "肝区肾区无叩痛，腹部叩诊鼓音，移动性浊音(-)。肠鸣音4次/分。脊柱活动", "度可，生理弯曲存在，四肢无畸形，关节无红肿及压痛，主动活动正常，双下", "129.1.11.73", "临时用户", "第 2 页", "129.1.11.73", "临时用户"]

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
2026-08-10 16:36:04,614 INFO     29 [qwen-vl-text] coord API raw response (len=1567):
[
	{"text": "临时用户", "bbox": [375, 35, 605, 111]},
	{"text": "体格检查", "bbox": [450, 30, 585, 65]},
	{"text": "T: 36.5 ℃ P: 74 次/分 R: 12 次/分 BP: 120 / 80 mmHg", "bbox": [118, 74, 888, 113]},
	{"text": "发育正常，营养中等，表情自然，正常面容，自主体位，步入病房，步态正常。", "bbox": [113, 128, 914, 168]},
	{"text": "神志清楚，查体合作。全身皮肤粘膜无黄染、苍白、发绀、出血点、水肿、肝", "bbox": [114, 181, 927, 220]},
	{"text": "掌、溃疡、蜘蛛痣。浅表淋巴结检查详见专科情况。头颅无畸形，双眼睑无水", "bbox": [115, 234, 928, 273]},
	{"text": "肿，眼球无突出及震颤，结膜无苍白、充血、出血或水肿，巩膜无黄染，双侧", "bbox": [115, 287, 927, 326]},
	{"text": "瞳孔等大正圆，对光反射灵敏。耳廓外形正常，外耳道无分泌物，乳突无压痛。", "bbox": [117, 339, 914, 378]},
	{"text": "鼻外形正常，口唇无苍白，咽无充血，颈无抵抗，未见颈动脉异常搏动，未见", "bbox": [119, 392, 927, 431]},
	{"text": "颈静脉怒张。气管居中，甲状腺未触及肿大，质软，未及结节，未及震颤，未", "bbox": [120, 444, 927, 483]},
	{"text": "闻及杂音。双乳腺对称，未触及肿物，乳头无溢液。心前区无隆起，心尖搏动", "bbox": [122, 496, 926, 535]},
	{"text": "位于第5肋间左锁骨中线内0.5cm，未见异常搏动，未触及震颤，无心包摩擦感，", "bbox": [123, 548, 914, 587]},
	{"text": "心界不大，心率74次/分，心律齐，心音正常。P2<A2，未见异常血管征，各瓣", "bbox": [125, 599, 925, 638]},
	{"text": "膜听诊区未闻及杂音及心包摩擦音，腹部平坦，未见胃、肠型及蠕动波，未见", "bbox": [127, 651, 925, 689]},
	{"text": "腹壁静脉曲张，腹软，无压痛、未触及包块，Murphy征阴性，肝脾肋下未及。", "bbox": [129, 703, 912, 740]},
	{"text": "肝区肾区无叩痛，腹部叩诊鼓音，移动性浊音(-)。肠鸣音4次/分。脊柱活动", "bbox": [130, 753, 923, 791]},
	{"text": "度可，生理弯曲存在，四肢无畸形，关节无红肿及压痛，主动活动正常，双下", "bbox": [132, 803, 923, 841]},
	{"text": "129.1.11.73", "bbox": [20, 841, 326, 898]},
	{"text": "临时用户", "bbox": [62, 907, 282, 982]},
	{"text": "第 2 页", "bbox": [487, 879, 587, 913]},
	{"text": "129.1.11.73", "bbox": [690, 841, 988, 898]},
	{"text": "临时用户", "bbox": [728, 907, 945, 977]}
]
2026-08-10 16:36:04,614 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=17.0s
2026-08-10 16:36:04,614 INFO     29 [qwen-vl-text] coord item[0]: text=临时用户, bbox=[375, 35, 605, 111]
2026-08-10 16:36:04,614 INFO     29 [qwen-vl-text] coord item[1]: text=体格检查, bbox=[450, 30, 585, 65]
2026-08-10 16:36:04,614 INFO     29 [qwen-vl-text] coord item[2]: text=T: 36.5 ℃ P: 74 次/分 R: 12 次/分 BP: 120 / 80 mmHg, bbox=[118, 74, 888, 113]
2026-08-10 16:36:04,614 INFO     29 [qwen-vl-text] coord item[3]: text=发育正常，营养中等，表情自然，正常面容，自主体位，步入病房，步态正常。, bbox=[113, 128, 914, 168]
2026-08-10 16:36:04,614 INFO     29 [qwen-vl-text] coord item[4]: text=神志清楚，查体合作。全身皮肤粘膜无黄染、苍白、发绀、出血点、水肿、肝, bbox=[114, 181, 927, 220]
2026-08-10 16:36:04,614 INFO     29 [qwen-vl-text] coord item[5]: text=掌、溃疡、蜘蛛痣。浅表淋巴结检查详见专科情况。头颅无畸形，双眼睑无水, bbox=[115, 234, 928, 273]
2026-08-10 16:36:04,614 INFO     29 [qwen-vl-text] coord item[6]: text=肿，眼球无突出及震颤，结膜无苍白、充血、出血或水肿，巩膜无黄染，双侧, bbox=[115, 287, 927, 326]
2026-08-10 16:36:04,614 INFO     29 [qwen-vl-text] coord item[7]: text=瞳孔等大正圆，对光反射灵敏。耳廓外形正常，外耳道无分泌物，乳突无压痛。, bbox=[117, 339, 914, 378]
2026-08-10 16:36:04,614 INFO     29 [qwen-vl-text] coord item[8]: text=鼻外形正常，口唇无苍白，咽无充血，颈无抵抗，未见颈动脉异常搏动，未见, bbox=[119, 392, 927, 431]
2026-08-10 16:36:04,614 INFO     29 [qwen-vl-text] coord item[9]: text=颈静脉怒张。气管居中，甲状腺未触及肿大，质软，未及结节，未及震颤，未, bbox=[120, 444, 927, 483]
2026-08-10 16:36:04,614 INFO     29 [qwen-vl-text] coord item[10]: text=闻及杂音。双乳腺对称，未触及肿物，乳头无溢液。心前区无隆起，心尖搏动, bbox=[122, 496, 926, 535]
2026-08-10 16:36:04,614 INFO     29 [qwen-vl-text] coord item[11]: text=位于第5肋间左锁骨中线内0.5cm，未见异常搏动，未触及震颤，无心包摩擦感，, bbox=[123, 548, 914, 587]
2026-08-10 16:36:04,614 INFO     29 [qwen-vl-text] coord item[12]: text=心界不大，心率74次/分，心律齐，心音正常。P2<A2，未见异常血管征，各瓣, bbox=[125, 599, 925, 638]
2026-08-10 16:36:04,614 INFO     29 [qwen-vl-text] coord item[13]: text=膜听诊区未闻及杂音及心包摩擦音，腹部平坦，未见胃、肠型及蠕动波，未见, bbox=[127, 651, 925, 689]
2026-08-10 16:36:04,615 INFO     29 [qwen-vl-text] coord item[14]: text=腹壁静脉曲张，腹软，无压痛、未触及包块，Murphy征阴性，肝脾肋下未及。, bbox=[129, 703, 912, 740]
2026-08-10 16:36:04,615 INFO     29 [qwen-vl-text] coord item[15]: text=肝区肾区无叩痛，腹部叩诊鼓音，移动性浊音(-)。肠鸣音4次/分。脊柱活动, bbox=[130, 753, 923, 791]
2026-08-10 16:36:04,615 INFO     29 [qwen-vl-text] coord item[16]: text=度可，生理弯曲存在，四肢无畸形，关节无红肿及压痛，主动活动正常，双下, bbox=[132, 803, 923, 841]
2026-08-10 16:36:04,615 INFO     29 [qwen-vl-text] coord item[17]: text=129.1.11.73, bbox=[20, 841, 326, 898]
2026-08-10 16:36:04,615 INFO     29 [qwen-vl-text] coord item[18]: text=临时用户, bbox=[62, 907, 282, 982]
2026-08-10 16:36:04,615 INFO     29 [qwen-vl-text] coord item[19]: text=第 2 页, bbox=[487, 879, 587, 913]
2026-08-10 16:36:04,615 INFO     29 [qwen-vl-text] coord item[20]: text=129.1.11.73, bbox=[690, 841, 988, 898]
2026-08-10 16:36:04,615 INFO     29 [qwen-vl-text] coord item[21]: text=临时用户, bbox=[728, 907, 945, 977]
2026-08-10 16:36:04,617 INFO     29 [qwen-vl-text] page=15 — 22/22 coords, api_time=17.0s
2026-08-10 16:36:04,648 INFO     29 [qwen-vl-text] coord API call start, page=16, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=15415311, prompt_len=1152
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共34行）
["姓名", "肢无水肿。双侧膝腱反射对称引出，双侧Babinski征(-)，脑膜刺激征-，肛门", "及外生殖器未见明显异常。", "专科检查：神志清楚，营养中等。双颈、双锁骨上、双腋窝未触及肿大淋巴", "结。腹部见术痕，愈合好；胸廓无畸形，气管居中；双肺呼吸运动平稳，触", "觉语颤正常对称，叩诊清音，听诊未闻及干湿罗音及胸膜摩擦音，双肺呼吸", "音清晰。", "辅助检查：暂缺。", "出院诊断", "1、手术后恶性肿瘤化学治疗", "2、食管胃连接处隆起型低分化腺", "癌新辅助化疗后术后（", "ypT3N1M0 IIIIB期）", "3、尘肺？", "4、右肝囊肿", "5、左肝胆管内结石", "6、左肾囊肿", "7、PICC置入术", "书写医生：", "2025年01月06日", "审核医生：", "2025年01月06日", "初步诊断", "1、食管胃连接处隆起型低分化腺癌新辅", "助化免治疗后术后（ypT3N1M0 IIIIB期）", "2、尘肺？", "3、右肝囊肿", "4、左肝胆管内结石", "5、左肾囊肿", "6、PICC置入术", "书写医生：", "2024年12月31日", "审核医生：", "2024年12月31日"]

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
2026-08-10 16:36:25,752 INFO     29 [qwen-vl-text] coord API raw response (len=1933):
[
	{"text": "姓名", "bbox": [133, 34, 176, 62]},
	{"text": "肢无水肿。双侧膝腱反射对称引出，双侧Babinski征(-)，脑膜刺激征-，肛门", "bbox": [133, 89, 935, 123]},
	{"text": "及外生殖器未见明显异常。", "bbox": [133, 133, 424, 163]},
	{"text": "专科检查：神志清楚，营养中等。双颈、双锁骨上、双腋窝未触及肿大淋巴", "bbox": [133, 175, 935, 207]},
	{"text": "结。腹部见术痕，愈合好；胸廓无畸形，气管居中；双肺呼吸运动平稳，触", "bbox": [133, 216, 935, 248]},
	{"text": "觉语颤正常对称，叩诊清音，听诊未闻及干湿罗音及胸膜摩擦音，双肺呼吸", "bbox": [133, 259, 935, 291]},
	{"text": "音清晰。", "bbox": [133, 302, 237, 332]},
	{"text": "辅助检查：暂缺。", "bbox": [133, 343, 334, 373]},
	{"text": "出院诊断", "bbox": [139, 391, 241, 420]},
	{"text": "1、手术后恶性肿瘤化学治疗", "bbox": [137, 429, 444, 460]},
	{"text": "2、食管胃连接处隆起型低分化腺", "bbox": [137, 471, 500, 502]},
	{"text": "癌新辅助化疗后术后（", "bbox": [137, 512, 494, 543]},
	{"text": "ypT3N1M0 IIIIB期）", "bbox": [137, 555, 334, 585]},
	{"text": "3、尘肺？", "bbox": [139, 597, 234, 627]},
	{"text": "4、右肝囊肿", "bbox": [139, 638, 269, 668]},
	{"text": "5、左肝胆管内结石", "bbox": [139, 680, 342, 710]},
	{"text": "6、左肾囊肿", "bbox": [139, 721, 269, 751]},
	{"text": "7、PICC置入术", "bbox": [139, 762, 291, 792]},
	{"text": "书写医生：", "bbox": [141, 831, 224, 855]},
	{"text": "2025年01月06日", "bbox": [278, 834, 412, 858]},
	{"text": "审核医生：", "bbox": [141, 885, 224, 909]},
	{"text": "2025年01月06日", "bbox": [278, 888, 412, 912]},
	{"text": "初步诊断", "bbox": [511, 394, 614, 423]},
	{"text": "1、食管胃连接处隆起型低分化腺癌新辅", "bbox": [511, 431, 926, 462]},
	{"text": "助化免治疗后术后（ypT3N1M0 IIIIB期）", "bbox": [511, 474, 926, 504]},
	{"text": "2、尘肺？", "bbox": [511, 515, 624, 545]},
	{"text": "3、右肝囊肿", "bbox": [511, 557, 638, 587]},
	{"text": "4、左肝胆管内结石", "bbox": [511, 597, 714, 629]},
	{"text": "5、左肾囊肿", "bbox": [511, 640, 644, 670]},
	{"text": "6、PICC置入术", "bbox": [511, 681, 661, 712]},
	{"text": "书写医生：", "bbox": [511, 753, 594, 777]},
	{"text": "2024年12月31日", "bbox": [727, 757, 868, 781]},
	{"text": "审核医生：", "bbox": [519, 811, 603, 836]},
	{"text": "2024年12月31日", "bbox": [677, 815, 814, 839]}
]
2026-08-10 16:36:25,753 INFO     29 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=21.1s
2026-08-10 16:36:25,753 INFO     29 [qwen-vl-text] coord item[0]: text=姓名, bbox=[133, 34, 176, 62]
2026-08-10 16:36:25,753 INFO     29 [qwen-vl-text] coord item[1]: text=肢无水肿。双侧膝腱反射对称引出，双侧Babinski征(-)，脑膜刺激征-，肛门, bbox=[133, 89, 935, 123]
2026-08-10 16:36:25,753 INFO     29 [qwen-vl-text] coord item[2]: text=及外生殖器未见明显异常。, bbox=[133, 133, 424, 163]
2026-08-10 16:36:25,753 INFO     29 [qwen-vl-text] coord item[3]: text=专科检查：神志清楚，营养中等。双颈、双锁骨上、双腋窝未触及肿大淋巴, bbox=[133, 175, 935, 207]
2026-08-10 16:36:25,753 INFO     29 [qwen-vl-text] coord item[4]: text=结。腹部见术痕，愈合好；胸廓无畸形，气管居中；双肺呼吸运动平稳，触, bbox=[133, 216, 935, 248]
2026-08-10 16:36:25,753 INFO     29 [qwen-vl-text] coord item[5]: text=觉语颤正常对称，叩诊清音，听诊未闻及干湿罗音及胸膜摩擦音，双肺呼吸, bbox=[133, 259, 935, 291]
2026-08-10 16:36:25,754 INFO     29 [qwen-vl-text] coord item[6]: text=音清晰。, bbox=[133, 302, 237, 332]
2026-08-10 16:36:25,754 INFO     29 [qwen-vl-text] coord item[7]: text=辅助检查：暂缺。, bbox=[133, 343, 334, 373]
2026-08-10 16:36:25,754 INFO     29 [qwen-vl-text] coord item[8]: text=出院诊断, bbox=[139, 391, 241, 420]
2026-08-10 16:36:25,754 INFO     29 [qwen-vl-text] coord item[9]: text=1、手术后恶性肿瘤化学治疗, bbox=[137, 429, 444, 460]
2026-08-10 16:36:25,754 INFO     29 [qwen-vl-text] coord item[10]: text=2、食管胃连接处隆起型低分化腺, bbox=[137, 471, 500, 502]
2026-08-10 16:36:25,754 INFO     29 [qwen-vl-text] coord item[11]: text=癌新辅助化疗后术后（, bbox=[137, 512, 494, 543]
2026-08-10 16:36:25,754 INFO     29 [qwen-vl-text] coord item[12]: text=ypT3N1M0 IIIIB期）, bbox=[137, 555, 334, 585]
2026-08-10 16:36:25,754 INFO     29 [qwen-vl-text] coord item[13]: text=3、尘肺？, bbox=[139, 597, 234, 627]
2026-08-10 16:36:25,754 INFO     29 [qwen-vl-text] coord item[14]: text=4、右肝囊肿, bbox=[139, 638, 269, 668]
2026-08-10 16:36:25,754 INFO     29 [qwen-vl-text] coord item[15]: text=5、左肝胆管内结石, bbox=[139, 680, 342, 710]
2026-08-10 16:36:25,754 INFO     29 [qwen-vl-text] coord item[16]: text=6、左肾囊肿, bbox=[139, 721, 269, 751]
2026-08-10 16:36:25,755 INFO     29 [qwen-vl-text] coord item[17]: text=7、PICC置入术, bbox=[139, 762, 291, 792]
2026-08-10 16:36:25,755 INFO     29 [qwen-vl-text] coord item[18]: text=书写医生：, bbox=[141, 831, 224, 855]
2026-08-10 16:36:25,755 INFO     29 [qwen-vl-text] coord item[19]: text=2025年01月06日, bbox=[278, 834, 412, 858]
2026-08-10 16:36:25,755 INFO     29 [qwen-vl-text] coord item[20]: text=审核医生：, bbox=[141, 885, 224, 909]
2026-08-10 16:36:25,755 INFO     29 [qwen-vl-text] coord item[21]: text=2025年01月06日, bbox=[278, 888, 412, 912]
2026-08-10 16:36:25,755 INFO     29 [qwen-vl-text] coord item[22]: text=初步诊断, bbox=[511, 394, 614, 423]
2026-08-10 16:36:25,755 INFO     29 [qwen-vl-text] coord item[23]: text=1、食管胃连接处隆起型低分化腺癌新辅, bbox=[511, 431, 926, 462]
2026-08-10 16:36:25,755 INFO     29 [qwen-vl-text] coord item[24]: text=助化免治疗后术后（ypT3N1M0 IIIIB期）, bbox=[511, 474, 926, 504]
2026-08-10 16:36:25,755 INFO     29 [qwen-vl-text] coord item[25]: text=2、尘肺？, bbox=[511, 515, 624, 545]
2026-08-10 16:36:25,755 INFO     29 [qwen-vl-text] coord item[26]: text=3、右肝囊肿, bbox=[511, 557, 638, 587]
2026-08-10 16:36:25,755 INFO     29 [qwen-vl-text] coord item[27]: text=4、左肝胆管内结石, bbox=[511, 597, 714, 629]
2026-08-10 16:36:25,755 INFO     29 [qwen-vl-text] coord item[28]: text=5、左肾囊肿, bbox=[511, 640, 644, 670]
2026-08-10 16:36:25,755 INFO     29 [qwen-vl-text] coord item[29]: text=6、PICC置入术, bbox=[511, 681, 661, 712]
2026-08-10 16:36:25,755 INFO     29 [qwen-vl-text] coord item[30]: text=书写医生：, bbox=[511, 753, 594, 777]
2026-08-10 16:36:25,755 INFO     29 [qwen-vl-text] coord item[31]: text=2024年12月31日, bbox=[727, 757, 868, 781]
2026-08-10 16:36:25,756 INFO     29 [qwen-vl-text] coord item[32]: text=审核医生：, bbox=[519, 811, 603, 836]
2026-08-10 16:36:25,756 INFO     29 [qwen-vl-text] coord item[33]: text=2024年12月31日, bbox=[677, 815, 814, 839]
2026-08-10 16:36:25,760 INFO     29 [qwen-vl-text] page=16 — 34/34 coords, api_time=21.1s
2026-08-10 16:36:25,761 INFO     29 [qwen-vl-text] new_positions (131):
[[12, 0.0, 913.216, 0.0, 114.036], [12, 108.144, 787.048, 127.296, 297.024], [12, 940.252, 2177.9, 233.376, 347.41200000000003], [12, 339.452, 474.632, 448.18800000000005, 525.096], [12, 1156.54, 1994.656, 609.96, 692.172], [12, 375.5, 450.6, 734.604, 808.86], [12, 1342.788, 1907.54, 734.604, 808.86], [12, 384.512, 456.608, 848.6400000000001, 922.8960000000001], [12, 525.7, 729.972, 848.6400000000001, 922.8960000000001], [12, 1339.784, 1763.348, 848.6400000000001, 922.8960000000001], [12, 387.516, 459.612, 962.676, 1036.932], [12, 528.704, 808.076, 962.676, 1036.932], [12, 1336.78, 2072.76, 962.676, 1036.932], [12, 396.528, 462.616, 1076.712, 1150.968], [12, 531.708, 817.088, 1076.712, 1150.968], [12, 1339.784, 2003.668, 1076.712, 1150.968], [12, 393.524, 468.624, 1188.096, 1262.352], [12, 534.712, 823.096, 1188.096, 1262.352], [12, 1342.788, 2505.336, 1193.4, 1267.6560000000002], [12, 396.528, 937.248, 1302.132, 1379.04], [12, 1342.788, 2505.336, 1307.4360000000001, 1381.692], [12, 375.5, 2216.952, 1538.16, 1623.0240000000001], [12, 375.5, 2784.708, 1652.1960000000001, 1737.0600000000002], [12, 375.5, 2733.64, 1766.2320000000002, 1848.4440000000002], [12, 384.512, 2775.696, 1877.616, 1959.8280000000002], [12, 384.512, 2769.688, 1989.0, 2071.212], [12, 384.512, 2763.68, 2100.384, 2182.596], [12, 384.512, 2757.672, 2211.768, 2293.98], [12, 384.512, 2757.672, 2323.152, 2405.364], [12, 384.512, 2733.64, 2434.536, 2514.096], [12, 384.512, 2763.68, 2545.92, 2625.48], [12, 2057.74, 3004.0, 0.0, 92.82000000000001], [12, 2171.892, 2859.808, 116.688, 283.764], [13, 373.61199999999997, 2738.817, 106.27199999999999, 174.906], [13, 367.586, 2738.817, 199.26, 281.178], [13, 367.586, 2738.817, 307.746, 391.878], [13, 367.586, 2744.843, 420.65999999999997, 502.578], [13, 367.586, 2744.843, 531.36, 613.278], [13, 367.586, 2714.7129999999997, 642.06, 723.978], [13, 367.586, 2744.843, 754.9739999999999, 836.8919999999999], [13, 367.586, 2744.843, 867.888, 949.806], [13, 367.586, 2714.7129999999997, 980.802, 1062.72], [13, 367.586, 2744.843, 1093.716, 1175.634], [13, 367.586, 2714.7129999999997, 1206.6299999999999, 1288.548], [13, 397.716, 2744.843, 1319.5439999999999, 1401.462], [13, 367.586, 2714.7129999999997, 1432.458, 1514.376], [13, 367.586, 2714.7129999999997, 1545.372, 1627.29], [13, 367.586, 2714.7129999999997, 1658.286, 1740.204], [13, 2042.8139999999999, 2946.714, 1693.71, 1837.62], [13, 135.585, 804.471, 1855.3319999999999, 2021.382], [13, 1428.162, 1732.475, 1802.196, 1879.686], [13, 2042.8139999999999, 2946.714, 1693.71, 1837.62], [13, 2163.334, 2823.181, 1855.3319999999999, 2021.382], [14, 294.784, 2743.296, 251.85500000000002, 349.634], [14, 294.784, 2743.296, 468.154, 568.896], [14, 294.784, 2731.264, 637.0450000000001, 734.8240000000001], [14, 300.8, 2743.296, 829.64, 927.419], [14, 300.8, 2743.296, 951.123, 1045.939], [14, 300.8, 2743.296, 1072.606, 1164.459], [14, 300.8, 782.08, 1179.2740000000001, 1265.201], [14, 306.816, 1287.424, 1294.8310000000001, 1380.758], [14, 306.816, 1287.424, 1407.425, 1493.352], [14, 306.816, 1287.424, 1522.982, 1608.909], [14, 306.816, 1287.424, 1632.613, 1727.429], [14, 1777.728, 1931.136, 1614.835, 1742.2440000000001], [14, 1338.56, 1738.624, 1754.096, 1834.097], [14, 306.816, 2628.992, 1848.912, 1940.765], [14, 306.816, 2707.2, 1964.469, 2050.396], [14, 306.816, 2743.296, 2077.063, 2162.9900000000002], [14, 306.816, 2743.296, 2186.694, 2275.584], [14, 306.816, 2743.296, 2302.251, 2391.141], [14, 306.816, 2707.2, 2414.8450000000003, 2503.735], [14, 306.816, 2743.296, 2530.402, 2619.292], [14, 306.816, 2767.36, 2642.996, 2731.886], [14, 306.816, 2743.296, 2755.59, 2814.85], [15, 1127.25, 1818.6299999999999, 75.915, 240.75900000000001], [15, 1352.6999999999998, 1758.5099999999998, 65.07000000000001, 140.985], [15, 354.70799999999997, 2669.328, 160.506, 245.097], [15, 339.678, 2747.484, 277.632, 364.392], [15, 342.68399999999997, 2786.562, 392.589, 477.18], [15, 345.69, 2789.5679999999998, 507.546, 592.1370000000001], [15, 345.69, 2786.562, 622.503, 707.094], [15, 351.702, 2747.484, 735.291, 819.8820000000001], [15, 357.714, 2786.562, 850.248, 934.839], [15, 360.71999999999997, 2786.562, 963.0360000000001, 1047.627], [15, 366.73199999999997, 2783.5559999999996, 1075.824, 1160.415], [15, 369.738, 2747.484, 1188.612, 1273.203], [15, 375.75, 2780.5499999999997, 1299.231, 1383.8220000000001], [15, 381.762, 2780.5499999999997, 1412.019, 1494.441], [15, 387.77399999999994, 2741.4719999999998, 1524.807, 1605.06], [15, 390.78, 2774.538, 1633.257, 1715.679], [15, 396.792, 2774.538, 1741.707, 1824.1290000000001], [15, 60.12, 979.9559999999999, 1824.1290000000001, 1947.762], [15, 186.37199999999999, 847.6919999999999, 1967.2830000000001, 2129.958], [15, 1463.9219999999998, 1764.522, 1906.551, 1980.297], [15, 2074.14, 2969.928, 1824.1290000000001, 1947.762], [15, 2188.368, 2840.6699999999996, 1967.2830000000001, 2119.113], [16, 402.45799999999997, 532.576, 90.678, 165.35399999999998], [16, 402.45799999999997, 2829.31, 237.36299999999997, 328.041], [16, 402.45799999999997, 1283.024, 354.71099999999996, 434.72099999999995], [16, 402.45799999999997, 2829.31, 466.72499999999997, 552.069], [16, 402.45799999999997, 2829.31, 576.072, 661.4159999999999], [16, 402.45799999999997, 2829.31, 690.7529999999999, 776.097], [16, 402.45799999999997, 717.1619999999999, 805.434, 885.444], [16, 402.45799999999997, 1010.684, 914.781, 994.7909999999999], [16, 420.614, 729.266, 1042.797, 1120.1399999999999], [16, 414.56199999999995, 1343.5439999999999, 1144.143, 1226.82], [16, 414.56199999999995, 1513.0, 1256.157, 1338.8339999999998], [16, 414.56199999999995, 1494.8439999999998, 1365.504, 1448.1809999999998], [16, 414.56199999999995, 1010.684, 1480.185, 1560.195], [16, 420.614, 708.084, 1592.1989999999998, 1672.2089999999998], [16, 420.614, 813.9939999999999, 1701.5459999999998, 1781.5559999999998], [16, 420.614, 1034.8919999999998, 1813.56, 1893.57], [16, 420.614, 813.9939999999999, 1922.907, 2002.917], [16, 420.614, 880.5659999999999, 2032.254, 2112.2639999999997], [16, 426.666, 677.824, 2216.277, 2280.285], [16, 841.228, 1246.712, 2224.278, 2288.286], [16, 426.666, 677.824, 2360.2949999999996, 2424.303], [16, 841.228, 1246.712, 2368.296, 2432.3039999999996], [16, 1546.2859999999998, 1857.964, 1050.798, 1128.1409999999998], [16, 1546.2859999999998, 2802.076, 1149.4769999999999, 1232.154], [16, 1546.2859999999998, 2802.076, 1264.158, 1344.168], [16, 1546.2859999999998, 1888.224, 1373.5049999999999, 1453.5149999999999], [16, 1546.2859999999998, 1930.588, 1485.519, 1565.529], [16, 1546.2859999999998, 2160.564, 1592.1989999999998, 1677.543], [16, 1546.2859999999998, 1948.744, 1706.8799999999999, 1786.8899999999999], [16, 1546.2859999999998, 2000.186, 1816.2269999999999, 1898.9039999999998], [16, 1546.2859999999998, 1797.444, 2008.2509999999997, 2072.259], [16, 2199.902, 2626.5679999999998, 2018.9189999999999, 2082.9269999999997], [16, 1570.494, 1824.6779999999999, 2162.937, 2229.6119999999996], [16, 2048.602, 2463.1639999999998, 2173.605, 2237.613]]
2026-08-10 16:36:25,761 INFO     29 [qwen-vl-text] ═══ DONE ═══ 131 positions, pages=5, time=125.0s
2026-08-10 16:36:25,782 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 16:36:25,782 INFO     29 [Trace] task=dca6cdea | doc=LBZH，男，63岁，胃癌一线(1).pdf | Extractor:Admission | outputs={"chunks": "1 items, types={'AdmissionRecord': 1}", "html": "", "json": "523 items", "markdown": "", "text": "", "name": "LBZH，男，63岁，胃癌一线(1).pdf", "output_format": "chunks", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_LabExam\": 1, \"chunks_Examination\": 4, \"chunks_Admission\": 1, \"chunks_Clinical\": 1}"}
2026-08-10 16:36:25,782 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 16:36:25,783 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:36:25.782+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 74, "failed": 0, "current": {"dca6cdea94d711f1bd9827cf206dfa2d": {"id": "dca6cdea94d711f1bd9827cf206dfa2d", "doc_id": "dbef275894d711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "size": 28457006, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786379026603, "task_type": "dataflow", "root_trace_id": "00f6a24fb6bd4742ba80c2030b932c44", "root_traceparent": "00-00f6a24fb6bd4742ba80c2030b932c44-fbfb6d98b4675b32-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:36:25,794 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:36:25,795 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:36:25,795 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 16:36:25,795 INFO     29 [qwen-vl-text] positions(29): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:36:25,796 INFO     29 [qwen-vl-text] page grouping: [7, 8], lines per page: [7, 22]
2026-08-10 16:36:27,110 INFO     29 [qwen-vl-text] page=7, rect=3008x1850, img=(8356x5139), dpi=200
2026-08-10 16:36:28,669 INFO     29 [qwen-vl-text] page=8, rect=3005x2308, img=(8348x6412), dpi=200
2026-08-10 16:36:28,675 INFO     29 [qwen-vl-text] LLM extraction start, text_len=462
2026-08-10 16:36:28,675 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:36:28,675 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 158, \"bbox_end\": 186, \"encounter_dates\": [\"2026-03-24\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "双侧颈部4区探及数个淋巴结，大者分别约1.7cm×1.2cm（左）、1.6cm×0.7cm（右），边界尚清，形\n态饱满，淋巴结门消失，CDFI示：内部及周边见有血流信号；余颈部未见明显异常肿大淋巴结。\n检查所见\n双侧颈部多发淋巴结肿大（倾向淋巴结转移）\n检查提示\n手术过程\n阳性 阳性\n病理报告\n骨髓报告\n检查申请\n检验申请\n输血申请\n手术申请单\n感染报告\n传染报告\n死亡报告\n浏览超声报告文件\n检查(检验)结果比较\n影像分析处理\n超声报告\n超声影像\n穿刺活检前超声检查（仅对穿刺活检淋巴结描述）：左侧锁骨上见肿大淋巴结，大小约1.8cm×1.1cm，\n边界尚清，内部未见淋巴门回声，CDFI：淋巴结内可见血流信号。\n今日15：00-15:08在彩超引导下，常规消毒、铺巾、局麻后，用16G半自动快速组织活检枪，由左下颈分别\n进针约2.8cm、2.7cm，达左侧锁骨上淋巴结内缘后，按压快门，接着迅速拔针，可见短条状组织块送细胞及组织病\n理检查。\n穿刺过程顺利，患者无不适。\n彩超引导下左侧锁骨上淋巴结快速组织活检\n检查提示",
    "role": "user"
  }
]
2026-08-10 16:36:31,969 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:36:31,969 INFO     29 [qwen-vl-text] LLM output (len=643):
{
  "exam_date": null,
  "report_date": null,
  "exam_name": "彩超引导下左侧锁骨上淋巴结快速组织活检",
  "exam_category": "other",
  "body_part": "左侧锁骨上淋巴结",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "双侧颈部4区探及数个淋巴结，大者分别约1.7cm×1.2cm（左）、1.6cm×0.7cm（右），边界尚清，形态饱满，淋巴结门消失，CDFI示：内部及周边见有血流信号；余颈部未见明显异常肿大淋巴结。\n穿刺活检前超声检查（仅对穿刺活检淋巴结描述）：左侧锁骨上见肿大淋巴结，大小约1.8cm×1.1cm，边界尚清，内部未见淋巴门回声，CDFI：淋巴结内可见血流信号。\n今日15：00-15:08在彩超引导下，常规消毒、铺巾、局麻后，用16G半自动快速组织活检枪，由左下颈分别进针约2.8cm、2.7cm，达左侧锁骨上淋巴结内缘后，按压快门，接着迅速拔针，可见短条状组织块送细胞及组织病理检查。\n穿刺过程顺利，患者无不适。",
  "conclusion": "双侧颈部多发淋巴结肿大（倾向淋巴结转移）",
  "physician": null,
  "reviewer": null
}
2026-08-10 16:36:31,998 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=10123260, prompt_len=775
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共7行）
["双侧颈部4区探及数个淋巴结，大者分别约1.7cm×1.2cm（左）、1.6cm×0.7cm（右），边界尚清，形", "态饱满，淋巴结门消失，CDFI示：内部及周边见有血流信号；余颈部未见明显异常肿大淋巴结。", "检查所见", "双侧颈部多发淋巴结肿大（倾向淋巴结转移）", "检查提示", "手术过程", "阳性 阳性"]

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
2026-08-10 16:36:45,669 INFO     29 [qwen-vl-text] coord API raw response (len=446):
[
	{"text": "双侧颈部4区探及数个淋巴结，大者分别约1.7cm×1.2cm（左）、1.6cm×0.7cm（右），边界尚清，形", "bbox": [191, 3, 919, 39]},
	{"text": "态饱满，淋巴结门消失，CDFI示：内部及周边见有血流信号；余颈部未见明显异常肿大淋巴结。", "bbox": [124, 28, 795, 65]},
	{"text": "检查所见", "bbox": [100, 65, 118, 170]},
	{"text": "双侧颈部多发淋巴结肿大（倾向淋巴结转移）", "bbox": [121, 487, 438, 515]},
	{"text": "检查提示", "bbox": [104, 535, 120, 640]},
	{"text": "手术过程", "bbox": [98, 716, 116, 821]},
	{"text": "阳性 阳性", "bbox": [109, 877, 184, 907]}
]
2026-08-10 16:36:45,669 INFO     29 [qwen-vl-text] coord API: raw_items=7, valid_items=7, elapsed=13.7s
2026-08-10 16:36:45,669 INFO     29 [qwen-vl-text] coord item[0]: text=双侧颈部4区探及数个淋巴结，大者分别约1.7cm×1.2cm（左）、1.6cm×0.7cm（右），边界尚清，形, bbox=[191, 3, 919, 39]
2026-08-10 16:36:45,669 INFO     29 [qwen-vl-text] coord item[1]: text=态饱满，淋巴结门消失，CDFI示：内部及周边见有血流信号；余颈部未见明显异常肿大淋巴结。, bbox=[124, 28, 795, 65]
2026-08-10 16:36:45,669 INFO     29 [qwen-vl-text] coord item[2]: text=检查所见, bbox=[100, 65, 118, 170]
2026-08-10 16:36:45,669 INFO     29 [qwen-vl-text] coord item[3]: text=双侧颈部多发淋巴结肿大（倾向淋巴结转移）, bbox=[121, 487, 438, 515]
2026-08-10 16:36:45,670 INFO     29 [qwen-vl-text] coord item[4]: text=检查提示, bbox=[104, 535, 120, 640]
2026-08-10 16:36:45,670 INFO     29 [qwen-vl-text] coord item[5]: text=手术过程, bbox=[98, 716, 116, 821]
2026-08-10 16:36:45,670 INFO     29 [qwen-vl-text] coord item[6]: text=阳性 阳性, bbox=[109, 877, 184, 907]
2026-08-10 16:36:45,673 INFO     29 [qwen-vl-text] page=7 — 7/7 coords, api_time=13.7s
2026-08-10 16:36:45,701 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=12675209, prompt_len=998
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["病理报告", "骨髓报告", "检查申请", "检验申请", "输血申请", "手术申请单", "感染报告", "传染报告", "死亡报告", "浏览超声报告文件", "检查(检验)结果比较", "影像分析处理", "超声报告", "超声影像", "穿刺活检前超声检查（仅对穿刺活检淋巴结描述）：左侧锁骨上见肿大淋巴结，大小约1.8cm×1.1cm，", "边界尚清，内部未见淋巴门回声，CDFI：淋巴结内可见血流信号。", "今日15：00-15:08在彩超引导下，常规消毒、铺巾、局麻后，用16G半自动快速组织活检枪，由左下颈分别", "进针约2.8cm、2.7cm，达左侧锁骨上淋巴结内缘后，按压快门，接着迅速拔针，可见短条状组织块送细胞及组织病", "理检查。", "穿刺过程顺利，患者无不适。", "彩超引导下左侧锁骨上淋巴结快速组织活检", "检查提示"]

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
2026-08-10 16:37:00,561 INFO     29 [qwen-vl-text] coord API raw response (len=1262):
[
	{"text": "病理报告", "bbox": [33, 48, 65, 93]},
	{"text": "骨髓报告", "bbox": [77, 48, 107, 93]},
	{"text": "检查申请", "bbox": [118, 48, 148, 93]},
	{"text": "检验申请", "bbox": [160, 48, 190, 93]},
	{"text": "输血申请", "bbox": [202, 48, 232, 93]},
	{"text": "手术申请单", "bbox": [245, 57, 320, 83]},
	{"text": "感染报告", "bbox": [333, 48, 363, 93]},
	{"text": "传染报告", "bbox": [375, 48, 405, 93]},
	{"text": "死亡报告", "bbox": [417, 48, 448, 93]},
	{"text": "浏览超声报告文件", "bbox": [523, 57, 641, 80]},
	{"text": "检查(检验)结果比较", "bbox": [671, 57, 816, 80]},
	{"text": "影像分析处理", "bbox": [846, 55, 943, 78]},
	{"text": "超声报告", "bbox": [100, 105, 153, 127]},
	{"text": "超声影像", "bbox": [167, 108, 228, 130]},
	{"text": "穿刺活检前超声检查（仅对穿刺活检淋巴结描述）：左侧锁骨上见肿大淋巴结，大小约1.8cm×1.1cm，", "bbox": [177, 149, 887, 173]},
	{"text": "边界尚清，内部未见淋巴门回声，CDFI：淋巴结内可见血流信号。", "bbox": [112, 171, 560, 195]},
	{"text": "今日15：00-15:08在彩超引导下，常规消毒、铺巾、局麻后，用16G半自动快速组织活检枪，由左下颈分别", "bbox": [153, 193, 895, 216]},
	{"text": "进针约2.8cm、2.7cm，达左侧锁骨上淋巴结内缘后，按压快门，接着迅速拔针，可见短条状组织块送细胞及组织病", "bbox": [112, 214, 906, 238]},
	{"text": "理检查。", "bbox": [112, 236, 167, 258]},
	{"text": "穿刺过程顺利，患者无不适。", "bbox": [144, 257, 342, 280]},
	{"text": "彩超引导下左侧锁骨上淋巴结快速组织活检", "bbox": [144, 546, 442, 570]},
	{"text": "检查提示", "bbox": [96, 588, 112, 675]}
]
2026-08-10 16:37:00,561 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=14.9s
2026-08-10 16:37:00,561 INFO     29 [qwen-vl-text] coord item[0]: text=病理报告, bbox=[33, 48, 65, 93]
2026-08-10 16:37:00,561 INFO     29 [qwen-vl-text] coord item[1]: text=骨髓报告, bbox=[77, 48, 107, 93]
2026-08-10 16:37:00,561 INFO     29 [qwen-vl-text] coord item[2]: text=检查申请, bbox=[118, 48, 148, 93]
2026-08-10 16:37:00,561 INFO     29 [qwen-vl-text] coord item[3]: text=检验申请, bbox=[160, 48, 190, 93]
2026-08-10 16:37:00,561 INFO     29 [qwen-vl-text] coord item[4]: text=输血申请, bbox=[202, 48, 232, 93]
2026-08-10 16:37:00,561 INFO     29 [qwen-vl-text] coord item[5]: text=手术申请单, bbox=[245, 57, 320, 83]
2026-08-10 16:37:00,561 INFO     29 [qwen-vl-text] coord item[6]: text=感染报告, bbox=[333, 48, 363, 93]
2026-08-10 16:37:00,561 INFO     29 [qwen-vl-text] coord item[7]: text=传染报告, bbox=[375, 48, 405, 93]
2026-08-10 16:37:00,561 INFO     29 [qwen-vl-text] coord item[8]: text=死亡报告, bbox=[417, 48, 448, 93]
2026-08-10 16:37:00,561 INFO     29 [qwen-vl-text] coord item[9]: text=浏览超声报告文件, bbox=[523, 57, 641, 80]
2026-08-10 16:37:00,562 INFO     29 [qwen-vl-text] coord item[10]: text=检查(检验)结果比较, bbox=[671, 57, 816, 80]
2026-08-10 16:37:00,562 INFO     29 [qwen-vl-text] coord item[11]: text=影像分析处理, bbox=[846, 55, 943, 78]
2026-08-10 16:37:00,562 INFO     29 [qwen-vl-text] coord item[12]: text=超声报告, bbox=[100, 105, 153, 127]
2026-08-10 16:37:00,562 INFO     29 [qwen-vl-text] coord item[13]: text=超声影像, bbox=[167, 108, 228, 130]
2026-08-10 16:37:00,562 INFO     29 [qwen-vl-text] coord item[14]: text=穿刺活检前超声检查（仅对穿刺活检淋巴结描述）：左侧锁骨上见肿大淋巴结，大小约1.8cm×1.1cm，, bbox=[177, 149, 887, 173]
2026-08-10 16:37:00,562 INFO     29 [qwen-vl-text] coord item[15]: text=边界尚清，内部未见淋巴门回声，CDFI：淋巴结内可见血流信号。, bbox=[112, 171, 560, 195]
2026-08-10 16:37:00,562 INFO     29 [qwen-vl-text] coord item[16]: text=今日15：00-15:08在彩超引导下，常规消毒、铺巾、局麻后，用16G半自动快速组织活检枪，由左下颈分别, bbox=[153, 193, 895, 216]
2026-08-10 16:37:00,562 INFO     29 [qwen-vl-text] coord item[17]: text=进针约2.8cm、2.7cm，达左侧锁骨上淋巴结内缘后，按压快门，接着迅速拔针，可见短条状组织块送细胞及组织病, bbox=[112, 214, 906, 238]
2026-08-10 16:37:00,562 INFO     29 [qwen-vl-text] coord item[18]: text=理检查。, bbox=[112, 236, 167, 258]
2026-08-10 16:37:00,562 INFO     29 [qwen-vl-text] coord item[19]: text=穿刺过程顺利，患者无不适。, bbox=[144, 257, 342, 280]
2026-08-10 16:37:00,562 INFO     29 [qwen-vl-text] coord item[20]: text=彩超引导下左侧锁骨上淋巴结快速组织活检, bbox=[144, 546, 442, 570]
2026-08-10 16:37:00,562 INFO     29 [qwen-vl-text] coord item[21]: text=检查提示, bbox=[96, 588, 112, 675]
2026-08-10 16:37:00,564 INFO     29 [qwen-vl-text] page=8 — 22/22 coords, api_time=14.9s
2026-08-10 16:37:00,564 INFO     29 [qwen-vl-text] new_positions (29):
[[7, 574.528, 2764.352, 5.550000000000001, 72.15], [7, 372.992, 2391.36, 51.800000000000004, 120.25], [7, 300.8, 354.944, 120.25, 314.5], [7, 363.968, 1317.504, 900.95, 952.75], [7, 312.832, 360.96, 989.75, 1184.0], [7, 294.784, 348.928, 1324.6000000000001, 1518.8500000000001], [7, 327.872, 553.472, 1622.45, 1677.95], [8, 99.16499999999999, 195.325, 110.78399999999999, 214.64399999999998], [8, 231.385, 321.53499999999997, 110.78399999999999, 214.64399999999998], [8, 354.59, 444.74, 110.78399999999999, 214.64399999999998], [8, 480.79999999999995, 570.9499999999999, 110.78399999999999, 214.64399999999998], [8, 607.01, 697.16, 110.78399999999999, 214.64399999999998], [8, 736.225, 961.5999999999999, 131.55599999999998, 191.564], [8, 1000.665, 1090.815, 110.78399999999999, 214.64399999999998], [8, 1126.875, 1217.0249999999999, 110.78399999999999, 214.64399999999998], [8, 1253.085, 1346.24, 110.78399999999999, 214.64399999999998], [8, 1571.615, 1926.205, 131.55599999999998, 184.64], [8, 2016.355, 2452.08, 131.55599999999998, 184.64], [8, 2542.23, 2833.7149999999997, 126.94, 180.024], [8, 300.5, 459.765, 242.33999999999997, 293.116], [8, 501.835, 685.14, 249.26399999999998, 300.03999999999996], [8, 531.885, 2665.435, 343.892, 399.284], [8, 336.56, 1682.8, 394.66799999999995, 450.05999999999995], [8, 459.765, 2689.475, 445.44399999999996, 498.52799999999996], [8, 336.56, 2722.5299999999997, 493.912, 549.304], [8, 336.56, 501.835, 544.688, 595.4639999999999], [8, 432.71999999999997, 1027.71, 593.156, 646.24], [8, 432.71999999999997, 1328.21, 1260.168, 1315.56], [8, 288.48, 336.56, 1357.1039999999998, 1557.8999999999999]]
2026-08-10 16:37:00,564 INFO     29 [qwen-vl-text] ═══ DONE ═══ 29 positions, pages=2, time=34.8s
2026-08-10 16:37:00,565 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:37:00,571 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:37:00,571 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 16:37:00,572 INFO     29 [qwen-vl-text] positions(60): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:37:00,572 INFO     29 [qwen-vl-text] page grouping: [8, 9, 10], lines per page: [2, 57, 1]
2026-08-10 16:37:02,132 INFO     29 [qwen-vl-text] page=8, rect=3005x2308, img=(8348x6412), dpi=200
2026-08-10 16:37:03,265 INFO     29 [qwen-vl-text] page=9, rect=3000x2070, img=(8334x5750), dpi=200
2026-08-10 16:37:04,546 INFO     29 [qwen-vl-text] page=10, rect=3004x2070, img=(8345x5750), dpi=200
2026-08-10 16:37:04,553 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1267
2026-08-10 16:37:04,554 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:37:04,554 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 187, \"bbox_end\": 237, \"encounter_dates\": [\"2026-03-18\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "手术过程\n阳性 阳性\n报告\n申请\n申请\n申请\n手术申请单\n报告\n报告\n报告\n浏览影像报告文件\n检查(检验)结果比较\n影像分析处理\n检查部位名称\n检查报告\n影像列表\n4.头颅+躯干(颅底至\n检查序号0005140996\n检查日期2026-03-18 14:04:49\n检查类型PETCT\n检查片号P68729\n检查部位头颅+躯干(颅底到大腿中上 检查方式\n报告医师陈炜佳\n报告时间2026-03-18 14 审核医师刘道佳\n审核时间2026-03-18\n影像所见\n是否异常 是\n“胃食管连接处癌术后”：吻合口壁未见明显增厚及FDG摄取异常增高。腹膜后见多发肿大淋巴\n结，较大者最大横截面约2.1cm×1.1cm，FDG摄取增高，SUVmax5.0。腹膜稍增厚，FDG摄取未见\n明显增高。腹水征阴性。\n大脑各部显像清晰，脑实质密度正常，中线居中，诸脑室系统未见明\n显扩大，脑池、脑沟未见明显增宽。脑皮质及基底节区FDG分布均匀，左右对称，未见明显异常稀\n疏或缺损改变。小脑FDG分布亦未见明显异常。双眼及副鼻窦未见明显异常密度影及异常FDG摄取\n增高。鼻咽部结构对称，两侧未见软组织肿块影，双侧咽隐窝、咽旁间隙存在，咽旁肌群未见FDG\n异常摄取增高，颅底骨质未见破坏。口咽部两侧腺体显影对称。甲状腺两叶不大，形态可，腺实质\n内未见FDG增高灶。颈部未见肿大淋巴结，相应部位未见FDG异常摄取增高。\n双肺见多发不规则\n斑片、条索、结节、粟粒影，部分伴钙化，以双肺上叶为著，FDG摄取轻度增高，SUVmax3.5；双\n肺见多发透亮无肺纹理区，较大者位于右肺尖，最大横截面约8.9cm×5.8cm。双侧锁骨区见数枚\n肿大淋巴结，较大者位于左侧，最大横截面约1.8cm×0.9cm，FDG摄取轻度增高，SUVmax4.0。纵\n隔、双侧肺门见多发肿大淋巴结，伴钙化，较大者短径约1.7cm，FDG摄取轻度增高，SUVmax4.0\n。两侧腋窝未见肿大淋巴结或淋巴结FDG异常摄取增高。心肌显影清晰。气管居中。双侧胸膜稍增\n厚。双侧胸腔少量积液。纵隔大血管本底SUVmax1.4。\n肝脏形态可，轮廓光整，肝叶比例正常，\n肝V段见一囊样低密度影，最大横截面约5.9cm×4.6cm，FDG摄取缺损；余肝实质内FDG分布稍欠\n均匀，SUVmax2.0。肝内外胆管无扩张。胆囊大小正常，密度均匀，胆囊壁无增厚。肝门结构正\n常。胰腺形态FDG分布尚好，胰管不扩张。脾脏轻度显影，FDG分布均匀。两侧肾脏显影可，左肾\n影像诊断\n“胃食管连接处癌术后”：\n1、①腹膜后多发肿大淋巴结，代谢增高，考虑转移可能；②双侧锁\n骨区数枚肿大淋巴结，代谢轻度增高，炎性增生？转移待排除，请结合临床。\n2、腹膜稍增厚，\n低代谢，建议随诊。\n3、双肺多形性改变，纵隔、双侧肺门多发淋巴结，轻微代谢，结合职业\n史，以上考虑炎性肉芽肿性病变，建议随诊；双肺多发肺大泡。\n4、双侧胸膜稍增厚；双侧胸腔\n少量积液。\n5、肝囊肿；左肾囊肿。\n6、左侧肩关节、右侧髋关节炎性病变。\n58 未F",
    "role": "user"
  }
]
2026-08-10 16:37:04,557 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:37:04.556+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 74, "failed": 0, "current": {"dca6cdea94d711f1bd9827cf206dfa2d": {"id": "dca6cdea94d711f1bd9827cf206dfa2d", "doc_id": "dbef275894d711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "size": 28457006, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786379026603, "task_type": "dataflow", "root_trace_id": "00f6a24fb6bd4742ba80c2030b932c44", "root_traceparent": "00-00f6a24fb6bd4742ba80c2030b932c44-fbfb6d98b4675b32-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:37:11,854 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:37:11,854 INFO     29 [qwen-vl-text] LLM output (len=1343):
{
  "exam_date": "2026-03-18",
  "report_date": "2026-03-18",
  "exam_name": "PETCT",
  "exam_category": "imaging",
  "body_part": "头颅+躯干(颅底到大腿中上",
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "是否异常 是\n“胃食管连接处癌术后”：吻合口壁未见明显增厚及FDG摄取异常增高。腹膜后见多发肿大淋巴结，较大者最大横截面约2.1cm×1.1cm，FDG摄取增高，SUVmax5.0。腹膜稍增厚，FDG摄取未见明显增高。腹水征阴性。\n大脑各部显像清晰，脑实质密度正常，中线居中，诸脑室系统未见明显扩大，脑池、脑沟未见明显增宽。脑皮质及基底节区FDG分布均匀，左右对称，未见明显异常稀疏或缺损改变。小脑FDG分布亦未见明显异常。双眼及副鼻窦未见明显异常密度影及异常FDG摄取增高。鼻咽部结构对称，两侧未见软组织肿块影，双侧咽隐窝、咽旁间隙存在，咽旁肌群未见FDG异常摄取增高，颅底骨质未见破坏。口咽部两侧腺体显影对称。甲状腺两叶不大，形态可，腺实质内未见FDG增高灶。颈部未见肿大淋巴结，相应部位未见FDG异常摄取增高。\n双肺见多发不规则斑片、条索、结节、粟粒影，部分伴钙化，以双肺上叶为著，FDG摄取轻度增高，SUVmax3.5；双肺见多发透亮无肺纹理区，较大者位于右肺尖，最大横截面约8.9cm×5.8cm。双侧锁骨区见数枚肿大淋巴结，较大者位于左侧，最大横截面约1.8cm×0.9cm，FDG摄取轻度增高，SUVmax4.0。纵隔、双侧肺门见多发肿大淋巴结，伴钙化，较大者短径约1.7cm，FDG摄取轻度增高，SUVmax4.0。两侧腋窝未见肿大淋巴结或淋巴结FDG异常摄取增高。心肌显影清晰。气管居中。双侧胸膜稍增厚。双侧胸腔少量积液。纵隔大血管本底SUVmax1.4。\n肝脏形态可，轮廓光整，肝叶比例正常，肝V段见一囊样低密度影，最大横截面约5.9cm×4.6cm，FDG摄取缺损；余肝实质内FDG分布稍欠均匀，SUVmax2.0。肝内外胆管无扩张。胆囊大小正常，密度均匀，胆囊壁无增厚。肝门结构正常。胰腺形态FDG分布尚好，胰管不扩张。脾脏轻度显影，FDG分布均匀。两侧肾脏显影可，左肾",
  "conclusion": "影像诊断\n“胃食管连接处癌术后”：\n1、①腹膜后多发肿大淋巴结，代谢增高，考虑转移可能；②双侧锁骨区数枚肿大淋巴结，代谢轻度增高，炎性增生？转移待排除，请结合临床。\n2、腹膜稍增厚，低代谢，建议随诊。\n3、双肺多形性改变，纵隔、双侧肺门多发淋巴结，轻微代谢，结合职业史，以上考虑炎性肉芽肿性病变，建议随诊；双肺多发肺大泡。\n4、双侧胸膜稍增厚；双侧胸腔少量积液。\n5、肝囊肿；左肾囊肿。\n6、左侧肩关节、右侧髋关节炎性病变。",
  "physician": "陈炜佳",
  "reviewer": "刘道佳"
}
2026-08-10 16:37:11,881 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=12675209, prompt_len=628
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共2行）
["手术过程", "阳性 阳性"]

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
2026-08-10 16:37:14,093 INFO     29 [qwen-vl-text] coord API raw response (len=112):
```json
[
	{"text": "手术过程", "bbox": [93, 738, 111, 829]},
	{"text": "阳性 阳性", "bbox": [107, 875, 178, 903]}
]
```
2026-08-10 16:37:14,093 INFO     29 [qwen-vl-text] coord API: raw_items=2, valid_items=2, elapsed=2.2s
2026-08-10 16:37:14,093 INFO     29 [qwen-vl-text] coord item[0]: text=手术过程, bbox=[93, 738, 111, 829]
2026-08-10 16:37:14,093 INFO     29 [qwen-vl-text] coord item[1]: text=阳性 阳性, bbox=[107, 875, 178, 903]
2026-08-10 16:37:14,097 INFO     29 [qwen-vl-text] page=8 — 2/2 coords, api_time=2.2s
2026-08-10 16:37:14,119 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9998124, prompt_len=2034
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共57行）
["报告", "申请", "申请", "申请", "手术申请单", "报告", "报告", "报告", "浏览影像报告文件", "检查(检验)结果比较", "影像分析处理", "检查部位名称", "检查报告", "影像列表", "4.头颅+躯干(颅底至", "检查序号0005140996", "检查日期2026-03-18 14:04:49", "检查类型PETCT", "检查片号P68729", "检查部位头颅+躯干(颅底到大腿中上 检查方式", "报告医师陈炜佳", "报告时间2026-03-18 14 审核医师刘道佳", "审核时间2026-03-18", "影像所见", "是否异常 是", "“胃食管连接处癌术后”：吻合口壁未见明显增厚及FDG摄取异常增高。腹膜后见多发肿大淋巴", "结，较大者最大横截面约2.1cm×1.1cm，FDG摄取增高，SUVmax5.0。腹膜稍增厚，FDG摄取未见", "明显增高。腹水征阴性。", "大脑各部显像清晰，脑实质密度正常，中线居中，诸脑室系统未见明", "显扩大，脑池、脑沟未见明显增宽。脑皮质及基底节区FDG分布均匀，左右对称，未见明显异常稀", "疏或缺损改变。小脑FDG分布亦未见明显异常。双眼及副鼻窦未见明显异常密度影及异常FDG摄取", "增高。鼻咽部结构对称，两侧未见软组织肿块影，双侧咽隐窝、咽旁间隙存在，咽旁肌群未见FDG", "异常摄取增高，颅底骨质未见破坏。口咽部两侧腺体显影对称。甲状腺两叶不大，形态可，腺实质", "内未见FDG增高灶。颈部未见肿大淋巴结，相应部位未见FDG异常摄取增高。", "双肺见多发不规则", "斑片、条索、结节、粟粒影，部分伴钙化，以双肺上叶为著，FDG摄取轻度增高，SUVmax3.5；双", "肺见多发透亮无肺纹理区，较大者位于右肺尖，最大横截面约8.9cm×5.8cm。双侧锁骨区见数枚", "肿大淋巴结，较大者位于左侧，最大横截面约1.8cm×0.9cm，FDG摄取轻度增高，SUVmax4.0。纵", "隔、双侧肺门见多发肿大淋巴结，伴钙化，较大者短径约1.7cm，FDG摄取轻度增高，SUVmax4.0", "。两侧腋窝未见肿大淋巴结或淋巴结FDG异常摄取增高。心肌显影清晰。气管居中。双侧胸膜稍增", "厚。双侧胸腔少量积液。纵隔大血管本底SUVmax1.4。", "肝脏形态可，轮廓光整，肝叶比例正常，", "肝V段见一囊样低密度影，最大横截面约5.9cm×4.6cm，FDG摄取缺损；余肝实质内FDG分布稍欠", "均匀，SUVmax2.0。肝内外胆管无扩张。胆囊大小正常，密度均匀，胆囊壁无增厚。肝门结构正", "常。胰腺形态FDG分布尚好，胰管不扩张。脾脏轻度显影，FDG分布均匀。两侧肾脏显影可，左肾", "影像诊断", "“胃食管连接处癌术后”：", "1、①腹膜后多发肿大淋巴结，代谢增高，考虑转移可能；②双侧锁", "骨区数枚肿大淋巴结，代谢轻度增高，炎性增生？转移待排除，请结合临床。", "2、腹膜稍增厚，", "低代谢，建议随诊。", "3、双肺多形性改变，纵隔、双侧肺门多发淋巴结，轻微代谢，结合职业", "史，以上考虑炎性肉芽肿性病变，建议随诊；双肺多发肺大泡。", "4、双侧胸膜稍增厚；双侧胸腔", "少量积液。", "5、肝囊肿；左肾囊肿。", "6、左侧肩关节、右侧髋关节炎性病变。"]

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
2026-08-10 16:37:43,310 INFO     29 [qwen-vl-text] coord API raw response (len=3339):
[
	{"text": "报告", "bbox": [5, 5, 39, 51]},
	{"text": "申请", "bbox": [55, 5, 88, 51]},
	{"text": "申请", "bbox": [103, 5, 135, 51]},
	{"text": "申请", "bbox": [149, 5, 181, 51]},
	{"text": "手术申请单", "bbox": [195, 13, 275, 41]},
	{"text": "报告", "bbox": [291, 5, 325, 51]},
	{"text": "报告", "bbox": [341, 5, 374, 51]},
	{"text": "报告", "bbox": [389, 5, 422, 51]},
	{"text": "浏览影像报告文件", "bbox": [504, 17, 632, 41]},
	{"text": "检查(检验)结果比较", "bbox": [667, 17, 823, 41]},
	{"text": "影像分析处理", "bbox": [855, 17, 959, 41]},
	{"text": "检查部位名称", "bbox": [47, 65, 149, 90]},
	{"text": "检查报告", "bbox": [176, 67, 240, 91]},
	{"text": "影像列表", "bbox": [256, 71, 322, 95]},
	{"text": "4.头颅+躯干(颅底至", "bbox": [0, 97, 157, 121]},
	{"text": "检查序号0005140996", "bbox": [178, 117, 347, 140]},
	{"text": "检查日期2026-03-18 14:04:49", "bbox": [391, 119, 642, 142]},
	{"text": "检查类型PETCT", "bbox": [678, 119, 796, 142]},
	{"text": "检查片号P68729", "bbox": [178, 160, 309, 183]},
	{"text": "检查部位头颅+躯干(颅底到大腿中上 检查方式", "bbox": [392, 161, 745, 185]},
	{"text": "报告医师陈炜佳", "bbox": [178, 199, 305, 223]},
	{"text": "报告时间2026-03-18 14 审核医师刘道佳", "bbox": [392, 201, 711, 225]},
	{"text": "审核时间2026-03-18", "bbox": [753, 202, 922, 225]},
	{"text": "影像所见", "bbox": [178, 241, 248, 265]},
	{"text": "是否异常 是", "bbox": [753, 238, 846, 262]},
	{"text": "“胃食管连接处癌术后”：吻合口壁未见明显增厚及FDG摄取异常增高。腹膜后见多发肿大淋巴", "bbox": [188, 275, 907, 300]},
	{"text": "结，较大者最大横截面约2.1cm×1.1cm，FDG摄取增高，SUVmax5.0。腹膜稍增厚，FDG摄取未见", "bbox": [184, 300, 921, 325]},
	{"text": "明显增高。腹水征阴性。\\n大脑各部显像清晰，脑实质密度正常，中线居中，诸脑室系统未见明", "bbox": [184, 325, 915, 349]},
	{"text": "显扩大，脑池、脑沟未见明显增宽。脑皮质及基底节区FDG分布均匀，左右对称，未见明显异常稀", "bbox": [184, 349, 924, 373]},
	{"text": "疏或缺损改变。小脑FDG分布亦未见明显异常。双眼及副鼻窦未见明显异常密度影及异常FDG摄取", "bbox": [184, 373, 918, 397]},
	{"text": "增高。鼻咽部结构对称，两侧未见软组织肿块影，双侧咽隐窝、咽旁间隙存在，咽旁肌群未见FDG", "bbox": [184, 397, 924, 421]},
	{"text": "异常摄取增高，颅底骨质未见破坏。口咽部两侧腺体显影对称。甲状腺两叶不大，形态可，腺实质", "bbox": [184, 421, 932, 445]},
	{"text": "内未见FDG增高灶。颈部未见肿大淋巴结，相应部位未见FDG异常摄取增高。\\n双肺见多发不规则", "bbox": [184, 445, 921, 469]},
	{"text": "斑片、条索、结节、粟粒影，部分伴钙化，以双肺上叶为著，FDG摄取轻度增高，SUVmax3.5；双", "bbox": [184, 469, 924, 493]},
	{"text": "肺见多发透亮无肺纹理区，较大者位于右肺尖，最大横截面约8.9cm×5.8cm。双侧锁骨区见数枚", "bbox": [184, 493, 922, 517]},
	{"text": "肿大淋巴结，较大者位于左侧，最大横截面约1.8cm×0.9cm，FDG摄取轻度增高，SUVmax4.0。纵", "bbox": [184, 517, 930, 541]},
	{"text": "隔、双侧肺门见多发肿大淋巴结，伴钙化，较大者短径约1.7cm，FDG摄取轻度增高，SUVmax4.0", "bbox": [184, 541, 920, 565]},
	{"text": "。两侧腋窝未见肿大淋巴结或淋巴结FDG异常摄取增高。心肌显影清晰。气管居中。双侧胸膜稍增", "bbox": [184, 565, 928, 589]},
	{"text": "厚。双侧胸腔少量积液。纵隔大血管本底SUVmax1.4。\\n肝脏形态可，轮廓光整，肝叶比例正常，", "bbox": [184, 589, 926, 613]},
	{"text": "肝V段见一囊样低密度影，最大横截面约5.9cm×4.6cm，FDG摄取缺损；余肝实质内FDG分布稍欠", "bbox": [184, 613, 920, 637]},
	{"text": "均匀，SUVmax2.0。肝内外胆管无扩张。胆囊大小正常，密度均匀，胆囊壁无增厚。肝门结构正", "bbox": [184, 637, 915, 661]},
	{"text": "常。胰腺形态FDG分布尚好，胰管不扩张。脾脏轻度显影，FDG分布均匀。两侧肾脏显影可，左肾", "bbox": [184, 661, 922, 685]},
	{"text": "影像诊断", "bbox": [184, 694, 254, 718]},
	{"text": "“胃食管连接处癌术后”：\\n1、①腹膜后多发肿大淋巴结，代谢增高，考虑转移可能；②双侧锁", "bbox": [192, 733, 930, 758]},
	{"text": "骨区数枚肿大淋巴结，代谢轻度增高，炎性增生？转移待排除，请结合临床。\\n2、腹膜稍增厚，", "bbox": [190, 758, 922, 782]},
	{"text": "低代谢，建议随诊。\\n3、双肺多形性改变，纵隔、双侧肺门多发淋巴结，轻微代谢，结合职业", "bbox": [190, 782, 913, 806]},
	{"text": "史，以上考虑炎性肉芽肿性病变，建议随诊；双肺多发肺大泡。\\n4、双侧胸膜稍增厚；双侧胸腔", "bbox": [190, 806, 931, 830]},
	{"text": "少量积液。\\n5、肝囊肿；左肾囊肿。\\n6、左侧肩关节、右侧髋关节炎性病变。", "bbox": [190, 830, 798, 855]}
]
2026-08-10 16:37:43,310 INFO     29 [qwen-vl-text] coord API: raw_items=48, valid_items=48, elapsed=29.2s
2026-08-10 16:37:43,310 INFO     29 [qwen-vl-text] coord item[0]: text=报告, bbox=[5, 5, 39, 51]
2026-08-10 16:37:43,310 INFO     29 [qwen-vl-text] coord item[1]: text=申请, bbox=[55, 5, 88, 51]
2026-08-10 16:37:43,310 INFO     29 [qwen-vl-text] coord item[2]: text=申请, bbox=[103, 5, 135, 51]
2026-08-10 16:37:43,310 INFO     29 [qwen-vl-text] coord item[3]: text=申请, bbox=[149, 5, 181, 51]
2026-08-10 16:37:43,310 INFO     29 [qwen-vl-text] coord item[4]: text=手术申请单, bbox=[195, 13, 275, 41]
2026-08-10 16:37:43,310 INFO     29 [qwen-vl-text] coord item[5]: text=报告, bbox=[291, 5, 325, 51]
2026-08-10 16:37:43,310 INFO     29 [qwen-vl-text] coord item[6]: text=报告, bbox=[341, 5, 374, 51]
2026-08-10 16:37:43,310 INFO     29 [qwen-vl-text] coord item[7]: text=报告, bbox=[389, 5, 422, 51]
2026-08-10 16:37:43,310 INFO     29 [qwen-vl-text] coord item[8]: text=浏览影像报告文件, bbox=[504, 17, 632, 41]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[9]: text=检查(检验)结果比较, bbox=[667, 17, 823, 41]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[10]: text=影像分析处理, bbox=[855, 17, 959, 41]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[11]: text=检查部位名称, bbox=[47, 65, 149, 90]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[12]: text=检查报告, bbox=[176, 67, 240, 91]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[13]: text=影像列表, bbox=[256, 71, 322, 95]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[14]: text=4.头颅+躯干(颅底至, bbox=[0, 97, 157, 121]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[15]: text=检查序号0005140996, bbox=[178, 117, 347, 140]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[16]: text=检查日期2026-03-18 14:04:49, bbox=[391, 119, 642, 142]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[17]: text=检查类型PETCT, bbox=[678, 119, 796, 142]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[18]: text=检查片号P68729, bbox=[178, 160, 309, 183]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[19]: text=检查部位头颅+躯干(颅底到大腿中上 检查方式, bbox=[392, 161, 745, 185]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[20]: text=报告医师陈炜佳, bbox=[178, 199, 305, 223]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[21]: text=报告时间2026-03-18 14 审核医师刘道佳, bbox=[392, 201, 711, 225]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[22]: text=审核时间2026-03-18, bbox=[753, 202, 922, 225]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[23]: text=影像所见, bbox=[178, 241, 248, 265]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[24]: text=是否异常 是, bbox=[753, 238, 846, 262]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[25]: text=“胃食管连接处癌术后”：吻合口壁未见明显增厚及FDG摄取异常增高。腹膜后见多发肿大淋巴, bbox=[188, 275, 907, 300]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[26]: text=结，较大者最大横截面约2.1cm×1.1cm，FDG摄取增高，SUVmax5.0。腹膜稍增厚，FDG摄取未见, bbox=[184, 300, 921, 325]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[27]: text=明显增高。腹水征阴性。\n大脑各部显像清晰，脑实质密度正常，中线居中，诸脑室系统未见明, bbox=[184, 325, 915, 349]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[28]: text=显扩大，脑池、脑沟未见明显增宽。脑皮质及基底节区FDG分布均匀，左右对称，未见明显异常稀, bbox=[184, 349, 924, 373]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[29]: text=疏或缺损改变。小脑FDG分布亦未见明显异常。双眼及副鼻窦未见明显异常密度影及异常FDG摄取, bbox=[184, 373, 918, 397]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[30]: text=增高。鼻咽部结构对称，两侧未见软组织肿块影，双侧咽隐窝、咽旁间隙存在，咽旁肌群未见FDG, bbox=[184, 397, 924, 421]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[31]: text=异常摄取增高，颅底骨质未见破坏。口咽部两侧腺体显影对称。甲状腺两叶不大，形态可，腺实质, bbox=[184, 421, 932, 445]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[32]: text=内未见FDG增高灶。颈部未见肿大淋巴结，相应部位未见FDG异常摄取增高。\n双肺见多发不规则, bbox=[184, 445, 921, 469]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[33]: text=斑片、条索、结节、粟粒影，部分伴钙化，以双肺上叶为著，FDG摄取轻度增高，SUVmax3.5；双, bbox=[184, 469, 924, 493]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[34]: text=肺见多发透亮无肺纹理区，较大者位于右肺尖，最大横截面约8.9cm×5.8cm。双侧锁骨区见数枚, bbox=[184, 493, 922, 517]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[35]: text=肿大淋巴结，较大者位于左侧，最大横截面约1.8cm×0.9cm，FDG摄取轻度增高，SUVmax4.0。纵, bbox=[184, 517, 930, 541]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[36]: text=隔、双侧肺门见多发肿大淋巴结，伴钙化，较大者短径约1.7cm，FDG摄取轻度增高，SUVmax4.0, bbox=[184, 541, 920, 565]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[37]: text=。两侧腋窝未见肿大淋巴结或淋巴结FDG异常摄取增高。心肌显影清晰。气管居中。双侧胸膜稍增, bbox=[184, 565, 928, 589]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[38]: text=厚。双侧胸腔少量积液。纵隔大血管本底SUVmax1.4。\n肝脏形态可，轮廓光整，肝叶比例正常，, bbox=[184, 589, 926, 613]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[39]: text=肝V段见一囊样低密度影，最大横截面约5.9cm×4.6cm，FDG摄取缺损；余肝实质内FDG分布稍欠, bbox=[184, 613, 920, 637]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[40]: text=均匀，SUVmax2.0。肝内外胆管无扩张。胆囊大小正常，密度均匀，胆囊壁无增厚。肝门结构正, bbox=[184, 637, 915, 661]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[41]: text=常。胰腺形态FDG分布尚好，胰管不扩张。脾脏轻度显影，FDG分布均匀。两侧肾脏显影可，左肾, bbox=[184, 661, 922, 685]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[42]: text=影像诊断, bbox=[184, 694, 254, 718]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[43]: text=“胃食管连接处癌术后”：\n1、①腹膜后多发肿大淋巴结，代谢增高，考虑转移可能；②双侧锁, bbox=[192, 733, 930, 758]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[44]: text=骨区数枚肿大淋巴结，代谢轻度增高，炎性增生？转移待排除，请结合临床。\n2、腹膜稍增厚，, bbox=[190, 758, 922, 782]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[45]: text=低代谢，建议随诊。\n3、双肺多形性改变，纵隔、双侧肺门多发淋巴结，轻微代谢，结合职业, bbox=[190, 782, 913, 806]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[46]: text=史，以上考虑炎性肉芽肿性病变，建议随诊；双肺多发肺大泡。\n4、双侧胸膜稍增厚；双侧胸腔, bbox=[190, 806, 931, 830]
2026-08-10 16:37:43,311 INFO     29 [qwen-vl-text] coord item[47]: text=少量积液。\n5、肝囊肿；左肾囊肿。\n6、左侧肩关节、右侧髋关节炎性病变。, bbox=[190, 830, 798, 855]
2026-08-10 16:37:43,333 INFO     29 [qwen-vl-text] page=9 — 51/57 coords, api_time=29.2s
2026-08-10 16:37:43,358 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=12091449, prompt_len=620
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["58 未F"]

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
2026-08-10 16:37:54,250 INFO     29 [qwen-vl-text] coord API raw response (len=46):
[
	{"text": "58 未F", "bbox": [8, 0, 85, 30]}
]
2026-08-10 16:37:54,250 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=10.9s
2026-08-10 16:37:54,250 INFO     29 [qwen-vl-text] coord item[0]: text=58 未F, bbox=[8, 0, 85, 30]
2026-08-10 16:37:54,253 INFO     29 [qwen-vl-text] page=10 — 1/1 coords, api_time=10.9s
2026-08-10 16:37:54,253 INFO     29 [qwen-vl-text] new_positions (60):
[[8, 279.465, 333.555, 1703.3039999999999, 1913.3319999999999], [8, 321.53499999999997, 534.89, 2019.4999999999998, 2084.124], [9, 15.0, 117.0, 10.35, 105.57], [9, 165.0, 264.0, 10.35, 105.57], [9, 309.0, 405.0, 10.35, 105.57], [9, 447.0, 543.0, 10.35, 105.57], [9, 585.0, 825.0, 26.909999999999997, 84.86999999999999], [9, 873.0, 975.0, 10.35, 105.57], [9, 1023.0, 1122.0, 10.35, 105.57], [9, 1167.0, 1266.0, 10.35, 105.57], [9, 1512.0, 1896.0, 35.19, 84.86999999999999], [9, 2001.0, 2469.0, 35.19, 84.86999999999999], [9, 2565.0, 2877.0, 35.19, 84.86999999999999], [9, 141.0, 447.0, 134.54999999999998, 186.29999999999998], [9, 528.0, 720.0, 138.69, 188.36999999999998], [9, 768.0, 966.0, 146.97, 196.64999999999998], [9, 0.0, 471.0, 200.79, 250.46999999999997], [9, 534.0, 1041.0, 242.18999999999997, 289.79999999999995], [9, 1173.0, 1926.0, 246.32999999999998, 293.94], [9, 2034.0, 2388.0, 246.32999999999998, 293.94], [9, 534.0, 927.0, 331.2, 378.80999999999995], [9, 1176.0, 2235.0, 333.27, 382.95], [9, 534.0, 915.0, 411.92999999999995, 461.60999999999996], [9, 1176.0, 2133.0, 416.07, 465.74999999999994], [9, 2259.0, 2766.0, 418.14, 465.74999999999994], [9, 534.0, 744.0, 498.86999999999995, 548.55], [9, 2259.0, 2538.0, 492.65999999999997, 542.3399999999999], [9, 564.0, 2721.0, 569.25, 621.0], [9, 552.0, 2763.0, 621.0, 672.75], [9, 552.0, 2745.0, 672.75, 722.43], [9, 552.0, 2772.0, 722.43, 772.1099999999999], [9, 552.0, 2754.0, 772.1099999999999, 821.79], [9, 552.0, 2772.0, 821.79, 871.4699999999999], [9, 552.0, 2796.0, 871.4699999999999, 921.15], [9, 552.0, 2763.0, 921.15, 970.8299999999999], [9, 552.0, 2772.0, 970.8299999999999, 1020.5099999999999], [9, 552.0, 2766.0, 1020.5099999999999, 1070.1899999999998], [9, 552.0, 2790.0, 1070.1899999999998, 1119.87], [9, 552.0, 2760.0, 1119.87, 1169.55], [9, 552.0, 2784.0, 1169.55, 1219.23], [9, 552.0, 2778.0, 1219.23, 1268.9099999999999], [9, 552.0, 2760.0, 1268.9099999999999, 1318.59], [9, 552.0, 2745.0, 1318.59, 1368.27], [9, 552.0, 2766.0, 1368.27, 1417.9499999999998], [9, 552.0, 762.0, 1436.58, 1486.26], [9, 576.0, 2790.0, 1517.31, 1569.06], [9, 570.0, 2766.0, 1569.06, 1618.7399999999998], [9, 570.0, 2739.0, 1618.7399999999998, 1668.4199999999998], [9, 570.0, 2793.0, 1668.4199999999998, 1718.1], [9, 570.0, 2394.0, 1718.1, 1769.85], [9, 570.0, 2766.0, 1569.06, 1618.7399999999998], [9, 0, 0, 0, 0], [9, 0, 0, 0, 0], [9, 570.0, 2739.0, 1618.7399999999998, 1668.4199999999998], [9, 570.0, 2793.0, 1668.4199999999998, 1718.1], [9, 0, 0, 0, 0], [9, 0, 0, 0, 0], [9, 0, 0, 0, 0], [9, 0, 0, 0, 0], [10, 24.032, 255.34, 0.0, 62.099999999999994]]
2026-08-10 16:37:54,254 INFO     29 [qwen-vl-text] ═══ DONE ═══ 60 positions, pages=3, time=53.7s
2026-08-10 16:37:54,255 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:37:54,261 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:37:54,262 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 16:37:54,262 INFO     29 [qwen-vl-text] positions(24): [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:37:54,262 INFO     29 [qwen-vl-text] page grouping: [10], lines per page: [24]
2026-08-10 16:37:55,538 INFO     29 [qwen-vl-text] page=10, rect=3004x2070, img=(8345x5750), dpi=200
2026-08-10 16:37:55,545 INFO     29 [qwen-vl-text] LLM extraction start, text_len=197
2026-08-10 16:37:55,545 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:37:55,545 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 238, \"bbox_end\": 261, \"encounter_dates\": [\"2024-09-02\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "863 已F\n76 已F\n病例库 病理会诊\n姓名\n性别 男\n住院号\n年龄 61岁\n病区/\n床号 /\n送检单位 连江县晓澳卫 送检科室 /\n送检医生\n收到日期 2024-08-28\n取材医生\n取材日期 2024-08-28\n标本名称 /\n临床诊断\n肉眼所见\n镜下所见\n病理诊断（贲门）腺癌。\n特殊检查\n未发报告原因\n报告医生 力超\n审核医生 力超\n报告日期 2024-09-02 报告状态 已审核",
    "role": "user"
  }
]
2026-08-10 16:37:55,547 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:37:55.546+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 74, "failed": 0, "current": {"dca6cdea94d711f1bd9827cf206dfa2d": {"id": "dca6cdea94d711f1bd9827cf206dfa2d", "doc_id": "dbef275894d711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "size": 28457006, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786379026603, "task_type": "dataflow", "root_trace_id": "00f6a24fb6bd4742ba80c2030b932c44", "root_traceparent": "00-00f6a24fb6bd4742ba80c2030b932c44-fbfb6d98b4675b32-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:37:57,555 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:37:57,555 INFO     29 [qwen-vl-text] LLM output (len=335):
{
  "exam_date": "2024-08-28",
  "report_date": "2024-09-02",
  "exam_name": "病理会诊",
  "exam_category": "pathology",
  "body_part": "贲门",
  "patient_name": null,
  "patient_gender": "男",
  "department": "连江县晓澳卫",
  "bed_number": null,
  "findings": "肉眼所见\n镜下所见",
  "conclusion": "病理诊断（贲门）腺癌。",
  "physician": "力超",
  "reviewer": "力超"
}
2026-08-10 16:37:57,582 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=12091449, prompt_len=882
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共24行）
["863 已F", "76 已F", "病例库 病理会诊", "姓名", "性别 男", "住院号", "年龄 61岁", "病区/", "床号 /", "送检单位 连江县晓澳卫 送检科室 /", "送检医生", "收到日期 2024-08-28", "取材医生", "取材日期 2024-08-28", "标本名称 /", "临床诊断", "肉眼所见", "镜下所见", "病理诊断（贲门）腺癌。", "特殊检查", "未发报告原因", "报告医生 力超", "审核医生 力超", "报告日期 2024-09-02 报告状态 已审核"]

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
2026-08-10 16:38:05,970 INFO     29 [qwen-vl-text] coord API raw response (len=1325):
[
	{"text": "58 未F", "bbox": [10, 0, 85, 28]},
	{"text": "863 已F", "bbox": [10, 49, 85, 78]},
	{"text": "76 已F", "bbox": [10, 98, 85, 125]},
	{"text": "病例库 病理会诊", "bbox": [123, 15, 264, 47]},
	{"text": "病理", "bbox": [332, 18, 374, 50]},
	{"text": "住院号", "bbox": [540, 20, 602, 52]},
	{"text": "姓名", "bbox": [143, 55, 185, 87]},
	{"text": "性别 男", "bbox": [354, 58, 420, 90]},
	{"text": "年龄 61岁", "bbox": [561, 60, 644, 92]},
	{"text": "病区/", "bbox": [765, 63, 818, 93]},
	{"text": "床号 /", "bbox": [143, 95, 200, 127]},
	{"text": "送检单位 连江县晓澳卫 送检科室 /", "bbox": [311, 97, 617, 129]},
	{"text": "送检医生", "bbox": [724, 100, 806, 131]},
	{"text": "收到日期 2024-08-28", "bbox": [102, 135, 293, 167]},
	{"text": "取材医生", "bbox": [311, 138, 397, 169]},
	{"text": "取材日期 2024-08-28", "bbox": [518, 140, 706, 170]},
	{"text": "标本名称 /", "bbox": [101, 175, 200, 207]},
	{"text": "临床诊断", "bbox": [102, 214, 185, 246]},
	{"text": "肉眼所见", "bbox": [102, 258, 185, 290]},
	{"text": "镜下所见", "bbox": [103, 456, 188, 488]},
	{"text": "病理诊断（贲门）腺癌。", "bbox": [103, 530, 317, 563]},
	{"text": "特殊检查", "bbox": [105, 794, 190, 826]},
	{"text": "未发报告原因", "bbox": [105, 869, 234, 901]},
	{"text": "报告医生 力超", "bbox": [105, 915, 234, 947]},
	{"text": "审核医生 力超", "bbox": [315, 915, 442, 947]},
	{"text": "报告日期 2024-09-02 报告状态 已审核", "bbox": [520, 915, 866, 947]}
]
2026-08-10 16:38:05,971 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=8.4s
2026-08-10 16:38:05,971 INFO     29 [qwen-vl-text] coord item[0]: text=58 未F, bbox=[10, 0, 85, 28]
2026-08-10 16:38:05,971 INFO     29 [qwen-vl-text] coord item[1]: text=863 已F, bbox=[10, 49, 85, 78]
2026-08-10 16:38:05,971 INFO     29 [qwen-vl-text] coord item[2]: text=76 已F, bbox=[10, 98, 85, 125]
2026-08-10 16:38:05,971 INFO     29 [qwen-vl-text] coord item[3]: text=病例库 病理会诊, bbox=[123, 15, 264, 47]
2026-08-10 16:38:05,971 INFO     29 [qwen-vl-text] coord item[4]: text=病理, bbox=[332, 18, 374, 50]
2026-08-10 16:38:05,972 INFO     29 [qwen-vl-text] coord item[5]: text=住院号, bbox=[540, 20, 602, 52]
2026-08-10 16:38:05,972 INFO     29 [qwen-vl-text] coord item[6]: text=姓名, bbox=[143, 55, 185, 87]
2026-08-10 16:38:05,972 INFO     29 [qwen-vl-text] coord item[7]: text=性别 男, bbox=[354, 58, 420, 90]
2026-08-10 16:38:05,972 INFO     29 [qwen-vl-text] coord item[8]: text=年龄 61岁, bbox=[561, 60, 644, 92]
2026-08-10 16:38:05,972 INFO     29 [qwen-vl-text] coord item[9]: text=病区/, bbox=[765, 63, 818, 93]
2026-08-10 16:38:05,972 INFO     29 [qwen-vl-text] coord item[10]: text=床号 /, bbox=[143, 95, 200, 127]
2026-08-10 16:38:05,972 INFO     29 [qwen-vl-text] coord item[11]: text=送检单位 连江县晓澳卫 送检科室 /, bbox=[311, 97, 617, 129]
2026-08-10 16:38:05,972 INFO     29 [qwen-vl-text] coord item[12]: text=送检医生, bbox=[724, 100, 806, 131]
2026-08-10 16:38:05,972 INFO     29 [qwen-vl-text] coord item[13]: text=收到日期 2024-08-28, bbox=[102, 135, 293, 167]
2026-08-10 16:38:05,972 INFO     29 [qwen-vl-text] coord item[14]: text=取材医生, bbox=[311, 138, 397, 169]
2026-08-10 16:38:05,972 INFO     29 [qwen-vl-text] coord item[15]: text=取材日期 2024-08-28, bbox=[518, 140, 706, 170]
2026-08-10 16:38:05,972 INFO     29 [qwen-vl-text] coord item[16]: text=标本名称 /, bbox=[101, 175, 200, 207]
2026-08-10 16:38:05,972 INFO     29 [qwen-vl-text] coord item[17]: text=临床诊断, bbox=[102, 214, 185, 246]
2026-08-10 16:38:05,972 INFO     29 [qwen-vl-text] coord item[18]: text=肉眼所见, bbox=[102, 258, 185, 290]
2026-08-10 16:38:05,973 INFO     29 [qwen-vl-text] coord item[19]: text=镜下所见, bbox=[103, 456, 188, 488]
2026-08-10 16:38:05,973 INFO     29 [qwen-vl-text] coord item[20]: text=病理诊断（贲门）腺癌。, bbox=[103, 530, 317, 563]
2026-08-10 16:38:05,973 INFO     29 [qwen-vl-text] coord item[21]: text=特殊检查, bbox=[105, 794, 190, 826]
2026-08-10 16:38:05,973 INFO     29 [qwen-vl-text] coord item[22]: text=未发报告原因, bbox=[105, 869, 234, 901]
2026-08-10 16:38:05,973 INFO     29 [qwen-vl-text] coord item[23]: text=报告医生 力超, bbox=[105, 915, 234, 947]
2026-08-10 16:38:05,973 INFO     29 [qwen-vl-text] coord item[24]: text=审核医生 力超, bbox=[315, 915, 442, 947]
2026-08-10 16:38:05,973 INFO     29 [qwen-vl-text] coord item[25]: text=报告日期 2024-09-02 报告状态 已审核, bbox=[520, 915, 866, 947]
2026-08-10 16:38:05,977 INFO     29 [qwen-vl-text] page=10 — 24/24 coords, api_time=8.4s
2026-08-10 16:38:05,977 INFO     29 [qwen-vl-text] new_positions (24):
[[10, 30.04, 255.34, 0.0, 57.959999999999994], [10, 30.04, 255.34, 101.42999999999999, 161.45999999999998], [10, 30.04, 255.34, 202.85999999999999, 258.75], [10, 369.492, 793.056, 31.049999999999997, 97.28999999999999], [10, 997.328, 1123.496, 37.26, 103.49999999999999], [10, 1622.16, 1808.408, 41.4, 107.63999999999999], [10, 429.572, 555.74, 113.85, 180.08999999999997], [10, 1063.416, 1261.68, 120.05999999999999, 186.29999999999998], [10, 1685.244, 1934.576, 124.19999999999999, 190.44], [10, 2298.06, 2457.272, 130.41, 192.51], [10, 429.572, 600.8, 196.64999999999998, 262.89], [10, 934.244, 1853.468, 200.79, 267.03], [10, 2174.896, 2421.224, 206.99999999999997, 271.16999999999996], [10, 306.408, 880.172, 279.45, 345.69], [10, 934.244, 1192.588, 285.65999999999997, 349.83], [10, 1556.072, 2120.824, 289.79999999999995, 351.9], [10, 303.404, 600.8, 362.25, 428.48999999999995], [10, 306.408, 555.74, 442.97999999999996, 509.21999999999997], [10, 306.408, 555.74, 534.06, 600.3], [10, 309.412, 564.752, 943.92, 1010.16], [10, 309.412, 952.268, 1097.1, 1165.4099999999999], [10, 315.42, 570.76, 1643.58, 1709.82], [10, 315.42, 702.936, 1798.83, 1865.07], [10, 315.42, 702.936, 1894.05, 1960.2899999999997]]
2026-08-10 16:38:05,977 INFO     29 [qwen-vl-text] ═══ DONE ═══ 24 positions, pages=1, time=11.7s
2026-08-10 16:38:05,978 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:38:05,980 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:38:05,980 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 16:38:05,980 INFO     29 [qwen-vl-text] positions(34): [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:38:05,980 INFO     29 [qwen-vl-text] page grouping: [11], lines per page: [34]
2026-08-10 16:38:07,333 INFO     29 [qwen-vl-text] page=11, rect=3053x2235, img=(8481x6209), dpi=200
2026-08-10 16:38:07,342 INFO     29 [qwen-vl-text] LLM extraction start, text_len=755
2026-08-10 16:38:07,342 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:38:07,342 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 262, \"bbox_end\": 295, \"encounter_dates\": [\"2024-12-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "姓名\n性别男\n年龄01岁\n床号\n送检单位本院\n送检科室\n收到日期2024-11-28\n取材医生\n取材日期2024-11-29\n标本名称下段食管+近端胃\n临床诊断\n肉眼所见小弯LN8个，直径0.1-0.5cm；大弯LN未见；\n1LN2个，直径0.5-1.5cm；2LN2个，直径1.5-2cm；3LN未见；4LN2个，直径0.1-0.2cm；\n5LN未见；7LN6个，直径0.5-2.5cm；8LN1个，直径2.5cm；9LN1个，直径1.5cm；10LN2\n个，直径1-1.5cm；11LN1个，直径1.5cm；\n[肉眼诊断]\n下段食管+近端胃切除标本：上切间距3cm，下切间距10cm，小弯8cm，大弯12cm，紧靠上\n切，距下切1.5cm，于食管胃交界小弯处见一隆起型肿物，大小8x7cm，切面灰白，质硬，\n镜下所见\n病理诊断下段食管+近端胃切除标本：\n（食管胃交界）隆起型低分化腺癌（肿物大小8x7cm，Lauren分型：混合型），伴治疗反\n应（TRG：3级，残余肿瘤约占90%），肿瘤侵犯浆膜下层，脉管内见癌栓，神经见癌侵犯。\n标本上、下切端及另送“上切端”未见癌。淋巴结2/35见转移癌（“\n2”LN1/4、“7”LN1/14、胃小弯LNO/6、“\n1”LNO/2、“4”LNO/2、“8”LNO/6、“9”LNO/1、“11”LNO/2，“3、5”未见LN，\n“10”查见癌结节1枚）。胃小弯LN1/6、“7”LN1/14见治疗后反应。\n肿瘤病理分期：ypT3N1Mx（AJCC第八版）。\n特殊检查\n免疫组化结果：MSH2（+），MSH6（+），MLH1（+），PMS2（+），HER2（0），CD34（血\n未发报告原因\n报告医生陈丽芳\n审核医生陈丽芳\n报告日期2024-12-05\n报告状态已审核",
    "role": "user"
  }
]
2026-08-10 16:38:12,793 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:38:12,793 INFO     29 [qwen-vl-text] LLM output (len=955):
{
  "exam_date": "2024-11-29",
  "report_date": "2024-12-05",
  "exam_name": "病理检查",
  "exam_category": "pathology",
  "body_part": "下段食管+近端胃",
  "patient_name": null,
  "patient_gender": "男",
  "department": "本院",
  "bed_number": null,
  "findings": "肉眼所见小弯LN8个，直径0.1-0.5cm；大弯LN未见；\n1LN2个，直径0.5-1.5cm；2LN2个，直径1.5-2cm；3LN未见；4LN2个，直径0.1-0.2cm；\n5LN未见；7LN6个，直径0.5-2.5cm；8LN1个，直径2.5cm；9LN1个，直径1.5cm；10LN2\n个，直径1-1.5cm；11LN1个，直径1.5cm；\n[肉眼诊断]\n下段食管+近端胃切除标本：上切间距3cm，下切间距10cm，小弯8cm，大弯12cm，紧靠上\n切，距下切1.5cm，于食管胃交界小弯处见一隆起型肿物，大小8x7cm，切面灰白，质硬，",
  "conclusion": "病理诊断下段食管+近端胃切除标本：\n（食管胃交界）隆起型低分化腺癌（肿物大小8x7cm，Lauren分型：混合型），伴治疗反\n应（TRG：3级，残余肿瘤约占90%），肿瘤侵犯浆膜下层，脉管内见癌栓，神经见癌侵犯。\n标本上、下切端及另送“上切端”未见癌。淋巴结2/35见转移癌（“\n2”LN1/4、“7”LN1/14、胃小弯LNO/6、“\n1”LNO/2、“4”LNO/2、“8”LNO/6、“9”LNO/1、“11”LNO/2，“3、5”未见LN，\n“10”查见癌结节1枚）。胃小弯LN1/6、“7”LN1/14见治疗后反应。\n肿瘤病理分期：ypT3N1Mx（AJCC第八版）。\n特殊检查\n免疫组化结果：MSH2（+），MSH6（+），MLH1（+），PMS2（+），HER2（0），CD34（血",
  "physician": "陈丽芳",
  "reviewer": "陈丽芳"
}
2026-08-10 16:38:12,816 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=11145202, prompt_len=1470
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共34行）
["姓名", "性别男", "年龄01岁", "床号", "送检单位本院", "送检科室", "收到日期2024-11-28", "取材医生", "取材日期2024-11-29", "标本名称下段食管+近端胃", "临床诊断", "肉眼所见小弯LN8个，直径0.1-0.5cm；大弯LN未见；", "1LN2个，直径0.5-1.5cm；2LN2个，直径1.5-2cm；3LN未见；4LN2个，直径0.1-0.2cm；", "5LN未见；7LN6个，直径0.5-2.5cm；8LN1个，直径2.5cm；9LN1个，直径1.5cm；10LN2", "个，直径1-1.5cm；11LN1个，直径1.5cm；", "[肉眼诊断]", "下段食管+近端胃切除标本：上切间距3cm，下切间距10cm，小弯8cm，大弯12cm，紧靠上", "切，距下切1.5cm，于食管胃交界小弯处见一隆起型肿物，大小8x7cm，切面灰白，质硬，", "镜下所见", "病理诊断下段食管+近端胃切除标本：", "（食管胃交界）隆起型低分化腺癌（肿物大小8x7cm，Lauren分型：混合型），伴治疗反", "应（TRG：3级，残余肿瘤约占90%），肿瘤侵犯浆膜下层，脉管内见癌栓，神经见癌侵犯。", "标本上、下切端及另送“上切端”未见癌。淋巴结2/35见转移癌（“", "2”LN1/4、“7”LN1/14、胃小弯LNO/6、“", "1”LNO/2、“4”LNO/2、“8”LNO/6、“9”LNO/1、“11”LNO/2，“3、5”未见LN，", "“10”查见癌结节1枚）。胃小弯LN1/6、“7”LN1/14见治疗后反应。", "肿瘤病理分期：ypT3N1Mx（AJCC第八版）。", "特殊检查", "免疫组化结果：MSH2（+），MSH6（+），MLH1（+），PMS2（+），HER2（0），CD34（血", "未发报告原因", "报告医生陈丽芳", "审核医生陈丽芳", "报告日期2024-12-05", "报告状态已审核"]

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
2026-08-10 16:38:36,353 INFO     29 [qwen-vl-text] coord API raw response (len=2234):
[
	{"text": "姓名", "bbox": [83, 32, 108, 62]},
	{"text": "性别男", "bbox": [302, 34, 371, 65]},
	{"text": "年龄01岁", "bbox": [518, 43, 606, 71]},
	{"text": "床号", "bbox": [83, 70, 127, 100]},
	{"text": "送检单位本院", "bbox": [255, 72, 390, 103]},
	{"text": "送检科室", "bbox": [472, 77, 558, 110]},
	{"text": "收到日期2024-11-28", "bbox": [37, 108, 236, 139]},
	{"text": "取材医生", "bbox": [255, 112, 347, 143]},
	{"text": "取材日期2024-11-29", "bbox": [472, 118, 669, 148]},
	{"text": "标本名称下段食管+近端胃", "bbox": [36, 148, 276, 179]},
	{"text": "临床诊断", "bbox": [37, 188, 125, 218]},
	{"text": "肉眼所见小弯LN8个，直径0.1-0.5cm；大弯LN未见；", "bbox": [36, 231, 501, 262]},
	{"text": "1LN2个，直径0.5-1.5cm；2LN2个，直径1.5-2cm；3LN未见；4LN2个，直径0.1-0.2cm；", "bbox": [131, 259, 879, 291]},
	{"text": "5LN未见；7LN6个，直径0.5-2.5cm；8LN1个，直径2.5cm；9LN1个，直径1.5cm；10LN2", "bbox": [130, 285, 879, 318]},
	{"text": "个，直径1-1.5cm；11LN1个，直径1.5cm；", "bbox": [130, 311, 493, 339]},
	{"text": "[肉眼诊断]", "bbox": [131, 335, 224, 360]},
	{"text": "下段食管+近端胃切除标本：上切间距3cm，下切间距10cm，小弯8cm，大弯12cm，紧靠上", "bbox": [130, 360, 880, 393]},
	{"text": "切，距下切1.5cm，于食管胃交界小弯处见一隆起型肿物，大小8x7cm，切面灰白，质硬，", "bbox": [130, 386, 879, 418]},
	{"text": "镜下所见", "bbox": [33, 424, 122, 455]},
	{"text": "病理诊断下段食管+近端胃切除标本：", "bbox": [32, 498, 364, 530]},
	{"text": "（食管胃交界）隆起型低分化腺癌（肿物大小8x7cm，Lauren分型：混合型），伴治疗反", "bbox": [134, 527, 878, 558]},
	{"text": "应（TRG：3级，残余肿瘤约占90%），肿瘤侵犯浆膜下层，脉管内见癌栓，神经见癌侵犯。", "bbox": [127, 552, 878, 584]},
	{"text": "标本上、下切端及另送“上切端”未见癌。淋巴结2/35见转移癌（“", "bbox": [127, 577, 709, 608]},
	{"text": "2”LN1/4、“7”LN1/14、胃小弯LNO/6、“", "bbox": [127, 603, 508, 631]},
	{"text": "1”LNO/2、“4”LNO/2、“8”LNO/6、“9”LNO/1、“11”LNO/2，“3、5”未见LN，", "bbox": [127, 630, 867, 661]},
	{"text": "“10”查见癌结节1枚）。胃小弯LN1/6、“7”LN1/14见治疗后反应。", "bbox": [130, 656, 723, 687]},
	{"text": "肿瘤病理分期：ypT3N1Mx（AJCC第八版）。", "bbox": [126, 681, 509, 711]},
	{"text": "特殊检查", "bbox": [28, 762, 119, 793]},
	{"text": "免疫组化结果：MSH2（+），MSH6（+），MLH1（+），PMS2（+），HER2（0），CD34（血", "bbox": [125, 732, 892, 764]},
	{"text": "未发报告原因", "bbox": [27, 839, 163, 870]},
	{"text": "报告医生陈丽芳", "bbox": [25, 884, 181, 915]},
	{"text": "审核医生陈丽芳", "bbox": [247, 888, 403, 919]},
	{"text": "报告日期2024-12-05", "bbox": [467, 891, 668, 922]},
	{"text": "报告状态已审核", "bbox": [685, 894, 834, 924]}
]
2026-08-10 16:38:36,354 INFO     29 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=23.5s
2026-08-10 16:38:36,354 INFO     29 [qwen-vl-text] coord item[0]: text=姓名, bbox=[83, 32, 108, 62]
2026-08-10 16:38:36,354 INFO     29 [qwen-vl-text] coord item[1]: text=性别男, bbox=[302, 34, 371, 65]
2026-08-10 16:38:36,354 INFO     29 [qwen-vl-text] coord item[2]: text=年龄01岁, bbox=[518, 43, 606, 71]
2026-08-10 16:38:36,354 INFO     29 [qwen-vl-text] coord item[3]: text=床号, bbox=[83, 70, 127, 100]
2026-08-10 16:38:36,354 INFO     29 [qwen-vl-text] coord item[4]: text=送检单位本院, bbox=[255, 72, 390, 103]
2026-08-10 16:38:36,354 INFO     29 [qwen-vl-text] coord item[5]: text=送检科室, bbox=[472, 77, 558, 110]
2026-08-10 16:38:36,354 INFO     29 [qwen-vl-text] coord item[6]: text=收到日期2024-11-28, bbox=[37, 108, 236, 139]
2026-08-10 16:38:36,354 INFO     29 [qwen-vl-text] coord item[7]: text=取材医生, bbox=[255, 112, 347, 143]
2026-08-10 16:38:36,354 INFO     29 [qwen-vl-text] coord item[8]: text=取材日期2024-11-29, bbox=[472, 118, 669, 148]
2026-08-10 16:38:36,354 INFO     29 [qwen-vl-text] coord item[9]: text=标本名称下段食管+近端胃, bbox=[36, 148, 276, 179]
2026-08-10 16:38:36,354 INFO     29 [qwen-vl-text] coord item[10]: text=临床诊断, bbox=[37, 188, 125, 218]
2026-08-10 16:38:36,354 INFO     29 [qwen-vl-text] coord item[11]: text=肉眼所见小弯LN8个，直径0.1-0.5cm；大弯LN未见；, bbox=[36, 231, 501, 262]
2026-08-10 16:38:36,354 INFO     29 [qwen-vl-text] coord item[12]: text=1LN2个，直径0.5-1.5cm；2LN2个，直径1.5-2cm；3LN未见；4LN2个，直径0.1-0.2cm；, bbox=[131, 259, 879, 291]
2026-08-10 16:38:36,354 INFO     29 [qwen-vl-text] coord item[13]: text=5LN未见；7LN6个，直径0.5-2.5cm；8LN1个，直径2.5cm；9LN1个，直径1.5cm；10LN2, bbox=[130, 285, 879, 318]
2026-08-10 16:38:36,354 INFO     29 [qwen-vl-text] coord item[14]: text=个，直径1-1.5cm；11LN1个，直径1.5cm；, bbox=[130, 311, 493, 339]
2026-08-10 16:38:36,354 INFO     29 [qwen-vl-text] coord item[15]: text=[肉眼诊断], bbox=[131, 335, 224, 360]
2026-08-10 16:38:36,354 INFO     29 [qwen-vl-text] coord item[16]: text=下段食管+近端胃切除标本：上切间距3cm，下切间距10cm，小弯8cm，大弯12cm，紧靠上, bbox=[130, 360, 880, 393]
2026-08-10 16:38:36,354 INFO     29 [qwen-vl-text] coord item[17]: text=切，距下切1.5cm，于食管胃交界小弯处见一隆起型肿物，大小8x7cm，切面灰白，质硬，, bbox=[130, 386, 879, 418]
2026-08-10 16:38:36,354 INFO     29 [qwen-vl-text] coord item[18]: text=镜下所见, bbox=[33, 424, 122, 455]
2026-08-10 16:38:36,355 INFO     29 [qwen-vl-text] coord item[19]: text=病理诊断下段食管+近端胃切除标本：, bbox=[32, 498, 364, 530]
2026-08-10 16:38:36,355 INFO     29 [qwen-vl-text] coord item[20]: text=（食管胃交界）隆起型低分化腺癌（肿物大小8x7cm，Lauren分型：混合型），伴治疗反, bbox=[134, 527, 878, 558]
2026-08-10 16:38:36,355 INFO     29 [qwen-vl-text] coord item[21]: text=应（TRG：3级，残余肿瘤约占90%），肿瘤侵犯浆膜下层，脉管内见癌栓，神经见癌侵犯。, bbox=[127, 552, 878, 584]
2026-08-10 16:38:36,355 INFO     29 [qwen-vl-text] coord item[22]: text=标本上、下切端及另送“上切端”未见癌。淋巴结2/35见转移癌（“, bbox=[127, 577, 709, 608]
2026-08-10 16:38:36,355 INFO     29 [qwen-vl-text] coord item[23]: text=2”LN1/4、“7”LN1/14、胃小弯LNO/6、“, bbox=[127, 603, 508, 631]
2026-08-10 16:38:36,355 INFO     29 [qwen-vl-text] coord item[24]: text=1”LNO/2、“4”LNO/2、“8”LNO/6、“9”LNO/1、“11”LNO/2，“3、5”未见LN，, bbox=[127, 630, 867, 661]
2026-08-10 16:38:36,355 INFO     29 [qwen-vl-text] coord item[25]: text=“10”查见癌结节1枚）。胃小弯LN1/6、“7”LN1/14见治疗后反应。, bbox=[130, 656, 723, 687]
2026-08-10 16:38:36,355 INFO     29 [qwen-vl-text] coord item[26]: text=肿瘤病理分期：ypT3N1Mx（AJCC第八版）。, bbox=[126, 681, 509, 711]
2026-08-10 16:38:36,355 INFO     29 [qwen-vl-text] coord item[27]: text=特殊检查, bbox=[28, 762, 119, 793]
2026-08-10 16:38:36,355 INFO     29 [qwen-vl-text] coord item[28]: text=免疫组化结果：MSH2（+），MSH6（+），MLH1（+），PMS2（+），HER2（0），CD34（血, bbox=[125, 732, 892, 764]
2026-08-10 16:38:36,355 INFO     29 [qwen-vl-text] coord item[29]: text=未发报告原因, bbox=[27, 839, 163, 870]
2026-08-10 16:38:36,355 INFO     29 [qwen-vl-text] coord item[30]: text=报告医生陈丽芳, bbox=[25, 884, 181, 915]
2026-08-10 16:38:36,355 INFO     29 [qwen-vl-text] coord item[31]: text=审核医生陈丽芳, bbox=[247, 888, 403, 919]
2026-08-10 16:38:36,355 INFO     29 [qwen-vl-text] coord item[32]: text=报告日期2024-12-05, bbox=[467, 891, 668, 922]
2026-08-10 16:38:36,355 INFO     29 [qwen-vl-text] coord item[33]: text=报告状态已审核, bbox=[685, 894, 834, 924]
2026-08-10 16:38:36,358 INFO     29 [qwen-vl-text] page=11 — 34/34 coords, api_time=23.5s
2026-08-10 16:38:36,358 INFO     29 [qwen-vl-text] new_positions (34):
[[11, 253.399, 329.724, 71.52, 138.57], [11, 922.006, 1132.663, 75.99, 145.275], [11, 1581.454, 1850.118, 96.10499999999999, 158.685], [11, 253.399, 387.731, 156.45, 223.5], [11, 778.515, 1190.67, 160.92, 230.20499999999998], [11, 1441.016, 1703.574, 172.095, 245.85], [11, 112.961, 720.508, 241.38, 310.66499999999996], [11, 778.515, 1059.391, 250.32, 319.60499999999996], [11, 1441.016, 2042.4569999999999, 263.72999999999996, 330.78], [11, 109.908, 842.6279999999999, 330.78, 400.065], [11, 112.961, 381.625, 420.17999999999995, 487.22999999999996], [11, 109.908, 1529.5529999999999, 516.285, 585.5699999999999], [11, 399.943, 2683.587, 578.865, 650.385], [11, 396.89, 2683.587, 636.9749999999999, 710.7299999999999], [11, 396.89, 1505.129, 695.0849999999999, 757.665], [11, 399.943, 683.872, 748.7249999999999, 804.5999999999999], [11, 396.89, 2686.64, 804.5999999999999, 878.3549999999999], [11, 396.89, 2683.587, 862.7099999999999, 934.2299999999999], [11, 100.749, 372.466, 947.64, 1016.925], [11, 97.696, 1111.292, 1113.03, 1184.55], [11, 409.102, 2680.534, 1177.845, 1247.1299999999999], [11, 387.731, 2680.534, 1233.72, 1305.24], [11, 387.731, 2164.5769999999998, 1289.595, 1358.8799999999999], [11, 387.731, 1550.924, 1347.705, 1410.2849999999999], [11, 387.731, 2646.951, 1408.05, 1477.3349999999998], [11, 396.89, 2207.319, 1466.1599999999999, 1535.445], [11, 384.678, 1553.9769999999999, 1522.0349999999999, 1589.0849999999998], [11, 85.484, 363.307, 1703.07, 1772.3549999999998], [11, 381.625, 2723.276, 1636.02, 1707.54], [11, 82.431, 497.639, 1875.165, 1944.4499999999998], [11, 76.325, 552.593, 1975.7399999999998, 2045.0249999999999], [11, 754.091, 1230.359, 1984.6799999999998, 2053.9649999999997], [11, 1425.751, 2039.404, 1991.385, 2060.67], [11, 2091.305, 2546.2019999999998, 1998.09, 2065.14]]
2026-08-10 16:38:36,360 INFO     29 [qwen-vl-text] ═══ DONE ═══ 34 positions, pages=1, time=30.4s
2026-08-10 16:38:36,376 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 16:38:36,376 INFO     29 [Trace] task=dca6cdea | doc=LBZH，男，63岁，胃癌一线(1).pdf | Extractor:ExaminationReport | outputs={"chunks": "4 items, types={'ExaminationReport': 4}", "html": "", "json": "523 items", "markdown": "", "text": "", "name": "LBZH，男，63岁，胃癌一线(1).pdf", "output_format": "chunks", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_LabExam\": 1, \"chunks_Examination\": 4, \"chunks_Admission\": 1, \"chunks_Clinical\": 1}"}
2026-08-10 16:38:36,376 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 16:38:36,377 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:38:36.377+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 74, "failed": 0, "current": {"dca6cdea94d711f1bd9827cf206dfa2d": {"id": "dca6cdea94d711f1bd9827cf206dfa2d", "doc_id": "dbef275894d711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "size": 28457006, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786379026603, "task_type": "dataflow", "root_trace_id": "00f6a24fb6bd4742ba80c2030b932c44", "root_traceparent": "00-00f6a24fb6bd4742ba80c2030b932c44-fbfb6d98b4675b32-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:38:36,385 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:38:36,385 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 16:38:37,313 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:38:37,321 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 16:38:37,321 INFO     29 [Trace] task=dca6cdea | doc=LBZH，男，63岁，胃癌一线(1).pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "523 items", "markdown": "", "text": "", "name": "LBZH，男，63岁，胃癌一线(1).pdf", "output_format": "chunks", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "route_summary": "{\"chunks_LabExam\": 1, \"chunks_Examination\": 4, \"chunks_Admission\": 1, \"chunks_Clinical\": 1}"}
2026-08-10 16:38:37,321 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 16:38:37,323 INFO     29 [ChunkMerger] Merged 7 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 4, 'Extractor:Progress': 1} (filtered 5 noise chunks)
2026-08-10 16:38:37,336 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 16:38:37,336 INFO     29 [Trace] task=dca6cdea | doc=LBZH，男，63岁，胃癌一线(1).pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "7 items, types={'LabReport': 1, 'OutpatientRecord': 1, 'AdmissionRecord': 1, 'ExaminationReport': 4}", "name": "LBZH，男，63岁，胃癌一线(1).pdf"}
2026-08-10 16:38:37,336 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 16:38:38,076 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786379029785, 'update_date': datetime.datetime(2026, 8, 10, 16, 23, 49), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1224536, 'status': '1'}
2026-08-10 16:38:38,401 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   白蛋白  ALB  38.4  g/L  40.0-55.0  True    总胆红素  TBIL  9.3  umol/L  5.0-21.0  False    直接胆红素  DBIL  1.9  umol/L  0-8.0  False    间接胆红素  IBIL  7.4  umol/L  0-20.0  False    谷丙转氨酶  ALT  80  U/L  9-50  True    谷草转氨酶  AST  58  U/L  5-40  True    γ谷氨酰转肽酶  GGT  50  U/L  10-60  False    乳酸脱氢酶  LDH  208  U/L  120-250  False    尿素  Urea  3.12  mmol/L  3.6-9.5  True    肌酐  Cr  62  umol/L  57-111  False    尿素/肌酐  B/C  0.050  None  None  False    *尿酸  UA  354  umol/L  208.3-428.4  False    *葡萄糖  Glu  6.39  mmol/L  3.70-6.10  True    *游离三碘甲状原氨酸  FT3  5.55  pmol/L  3.53-7.37  False    *游离甲状腺素  FT4  11.03  pmol/L  7.98-19.24  False    *促甲状腺刺激激素  s-TSH  1.397  mIU/L  0.340-5.600  False    N端-B型钠尿肽前体  NT-proBNP  191.85  ng/L  <210.64  False    C反应蛋白  CRP  1.15  mg/L  <5.0  False    降钙素原  PCT  0.04  ng/mL  <0.05  False    肌钙蛋白T  TnT  5  ng/L  <14  False    *白细胞计数  WBC  6.18  10E9/L  3.5-9.5  False    中性粒细胞百分比  NE%  64.8  %  40-75  False    淋巴细胞百分比  LY%  23.3  %  20-50  False    单核细胞百分比  MO%  7.7  %  3-10  False    嗜酸粒细胞百分比  EO%  4.1  %  0.4-8.0  False    嗜碱粒细胞百分比  BA%  0.1  %  0-1  False    中性粒细胞绝对值  NE#  4.00  10E9/L  1.8-6.3  False    淋巴细胞绝对值  LY#  1.44  10E9/L  1.1-3.2  False    单核细胞绝对值  MO#  0.48  10E9/L  0.1-0.6  False    嗜酸粒细胞绝对值  EO#  0.25  10E9/L  0.02-0.52  False    嗜碱粒细胞绝对值  BA#  0.01  10E9/L  0-0.06  False    红细胞计数  RBC  4.26  10E12/L  4.3-5.8  True    血红蛋白  Hb  132  g/L  130-175  False    红细胞压积  HCT  40.6  %  40-50  False    平均RBC体积  MCV  95.2  fL  82-100  False    平均RBC血红蛋白含量  MCH  30.9  pg  27-34  False    平均RBC血红蛋白浓度  MCHC  325  g/L  316-354  False    红细胞体积分布宽度  RDW  12.5  %  <15  False    嗜酸粒细胞百分比  E0%  4.1  %  0.4-8.0  False    嗜碱粒细胞百分比  BA%  0.1  %  0-1  False    中性粒细胞绝对值  NE#  4.00  10E9/L  1.8-6.3  False    淋巴细胞绝对值  LY#  1.44  10E9/L  1.1-3.2  False    单核细胞绝对值  MO#  0.48  10E9/L  0.1-0.6  False    嗜酸粒细胞绝对值  EO#  0.25  10E9/L  0.02-0.52  False    嗜碱粒细胞绝对值  BA#  0.01  10E9/L  0-0.06  False    红细胞压积  HCT  40.6  %  40-50  False    平均RBC体积  MCV  95.2  fL  82-100  False    平均RBC血红蛋白含量  MCH  30.9  pg  27-34  False    平均RBC血红蛋白浓度  MCHC  325  g/L  316-354  False    红细胞体积分布宽度  RDW  12.5  %  <15  False    血小板计数  PLT  166  10E9/L  125-350  False    平均血小板体积  MPV  8.90  fL  8.0-15.0  False    血小板压积  PCT  0.147  %  0.100-0.250  False    血小板体积分布宽度  PDW  15.9  %  14.0-18.0  False    凝血酶原时间  PT  12.3  s  9.8-12.9  False    PT国际标准化比率  INR  1.07  None  0.82-1.20  False    活化部分凝血酶原时间  APTT  28.3  s  23.3-32.5  False   
---
2026-03-24 15:16
于2024-09-02以'进行性吞咽困难2个月'为主诉入院。2024-08-23于连江县晓澳卫生院行胃镜示'贲门肿块浸润性癌；食管下段浸润伴狭窄'；胃镜病理示：（贲门）腺癌，多层螺旋CT平扫+增强扫描+MPR：1.考虑贲门-胃体癌伴胃周淋巴结肿大
胃镜及腹部影像学检查；2.双肺多形性支气管纵隔、双肺门淋巴结钙化，尘肺可能，请结合病史；3.双肺上叶、右肺中叶较大肺大泡；4.扫及肝囊肿，请结合腹部影像学检查；病理会诊报告号(H24-03863)：(贲门)腺癌，相关检查未见明显化疗禁忌
于2024.09.04、2024.09.27、2024.10.25以'奥沙利铂160mg ivgtt d1+5-FU 4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w'方案行术前第1-3周期化疗，化疗过程顺利，相关检查无手术禁忌症，经充分术前准备后于2024-11-28在全麻下行
胃镜辅助食管胃交界处癌根治术'，术程顺利，恢复良好，术后病理回报(病理号：24-31776)：下段食管+近端胃切除标本：(食管胃交界)隆起型低分化腺癌(肿物大小8x7cm，L...[未打印]
姓名
性别：男 年龄：62岁
主诉：食管癌术后化疗免疫治疗后1年余。
现病史：于2024-09-02以'进行性吞咽困难2个月'为主诉入院。2024-08-23
于连江县晓澳卫生院行胃镜示'贲门肿块浸润性癌；食管下段浸润伴狭窄'；胃
镜病理示：（贲门）腺癌，多层螺旋CT平扫+增强扫描+MPR：1.考虑贲门-
胃体癌伴胃周淋巴结肿大，请结合胃镜及腹部影像学检查；2.双肺多形性支气管
纵隔、双肺门淋巴结钙化，尘肺可能，请结合病史；3.双肺上叶、右肺中叶较
大肺大泡；4.扫及肝囊肿，请结合腹部影像学检查；病理会诊报告号(H24-
03863)：(贲门)腺癌，相关检查未见明显化疗禁忌症，遂于2024.09.04、
2024.09.27、2024.10.25以'奥沙利铂160mg ivgtt d1+5-FU 4.5g 微量泵
泵入 48h+信迪利单抗 200mg ivgtt q3w'方案行术前第1-3周期化疗，化疗
过程顺利，相关检查无手术禁忌症，经充分术前准备后于2024-11-28在全麻
下行'腹腔镜辅助食管胃交界处癌根治术'，术程顺利，恢复良好，术后病理回
报(病理号：24-31776)：下段食管+近端胃切除标本：(食管胃交界)隆
起型低分化腺癌(肿物大小8x7cm，Lauren分型：混合型)，伴治疗反应
(TRG：3级，残余肿瘤约占90%)，肿瘤侵犯浆膜下层，脉管内见癌栓，神经
见癌侵犯。标本上、下切缘及另送'上切缘'未见癌。淋巴结2/35见转移癌
("2" LN1/4、"7" LN1/14、胃小弯LN0/6、"1" LN0/2、
"4" LN0/2、"8" LN0/6、"9" LN0/1、"11" LN0/2、"3、5" 未见
LN，"10" 查见癌结节1枚)。胃小弯LN1/6、"7" LN1/14见治疗后反应。
肿瘤病理分期：ypT3N1Mx (AJCC 第八版)。免疫组化结果：MSH2
(+)，MSH6 (+)，MLH1 (+)，PMS2 (+)，HER2 (0)，CD34
(血管+)，D2-40 (淋巴管+)，P53 (+)，EGFR (60%强着色，20%中
等着色，20%弱着色)，KI-67 (80%+)，CD3 (T细胞+)，约占肿瘤区域
10%)，CD8 (约占CD3阳性细胞数60%)，PD1 (约占CD3阳性细胞数
20%)，PD-L1 (CPS=5)，PD-L1neg (-)，P40 (-)，Syn (部分+)，
CgA (少量+)，CD56 (-)，CK5/6 (-)。原位杂交EBER (-)。于
2025.01.02以'紫杉醇 200mg ivgtt d1+奥沙利铂 160mg ivgtt d1+5-FU
3.4g 微量泵泵入 48h'方案行术后第1周期化疗。后予 '斯鲁利单抗' 免疫治
疗至今。2026-03-13放射报告：计算机体层成像(CT)增强(胸部+上腹)(故
<
102床 涂美石
多重耐药感染上报
4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w"方案行术前第1-3周期化疗，化疗过程顺利。相关检
24-31776）：下段食管+近端胃切除标本：（食管胃交界）隆起型低分化腺癌（肿物大小8x7cm，L...[未
20%），PD-L1（CPS=5），PD-L1neg（-），P40（-），Syn（部分+），
CgA（少量+），CD56（-），CK5/6（-）。原位杂交EBER（-）。于
2025.01.02以"紫杉醇 200mg ivgtt d1+奥沙利铂 160mg ivgtt d1+5-FU
3.4g 微量泵泵入 48h"方案行术后第1周期化疗。后予 "斯鲁利单抗" 免疫治
疗至今。2026-03-13放射报告：计算机体层成像（CT）增强(胸部+上腹)(放
射报告号:CT00333122)1.胃食管交界处癌术后改变，腹腔淋巴结较前相仿，
腹膜后淋巴结较前增大，转移可能2.双锁骨上区淋巴结，转移可能3.双肺多形
性变伴纵隔、双肺门淋巴结钙化与前大致相仿，尘肺可能，请结合病史4.双肺
上叶、右肺中叶肺大泡，较前相仿5.双侧胸腔少量积液较前相仿6.肝囊肿较前
大致相仿7.左肾囊肿较前相仿。2026-03-18复查PET-CT检查(核医学科报告
号:P68729) "胃食管连接处癌术后"：1、①腹膜后多发肿大淋巴结，代谢增
高，考虑转移可能；②双侧锁骨区数枚肿大淋巴结，代谢轻度增高，炎性增
生？转移待排除，请结合临床。2、腹膜稍增厚，低代谢，建议随诊。3、双
肺多形性改变，纵隔、双侧肺门多发淋巴结，轻微代谢，结合职业史，以上考
虑炎性肉芽肿性病变，建议随诊；双肺多发肺大泡。4、双侧胸膜稍增厚；双
侧胸腔少量积液。5、肝囊肿；左肾囊肿。6、左侧肩关节、右侧髋关节炎性
病变。今日行超声引导下左侧锁骨上淋巴结快速组织活检，今为求进一步诊
治，再次就诊我院。
过敏史：未发现。
体格检查：神志清晰，皮肤色泽正常，淋巴结未触及肿大；心脏：心律齐，心
音正常；肺：双肺语颤正常、对称，双肺呼吸音清，未闻及异常呼吸音，双肺
未闻及干湿性啰音；腹部：平软，无压痛、反跳痛，肝脾肋下未触及。
辅助检查：2026-03-24超声报告：彩超检查（常规）-浅表(超声报告
号:20260070720)双侧颈部多发淋巴结肿大（倾向淋巴结转移）；
诊断：
西医诊断：
食管恶性肿瘤(ypT3N1M0 III B期)
中医诊断：
处理措施：进一步系统治疗。
药品处方：
检验检查：
大致相仿7.左肾囊肿较前相仿。2026-03-18复查PET-CT检查(核医学科报告
号:P68729)“胃食管连接处癌术后”：1、①腹膜后多发肿大淋巴结，代谢增
高，考虑转移可能；②双侧锁骨区数枚肿大淋巴结，代谢轻度增高，炎性增
生？转移待排除，请结合临床。2、腹膜稍增厚，低代谢，建议随诊。3、双
肺多形性改变，纵隔、双侧肺门多发淋巴结，轻微代谢，结合职业史，以上考
虑炎性肉芽肿性病变，建议随诊；双肺多发肺大泡。4、双侧胸膜稍增厚；双
侧胸腔少量积液。5、肝囊肿；左肾囊肿。6、左侧肩关节、右侧髋关节炎性
病变。今日行超声引导下左侧锁骨上淋巴结快速组织活检，今为求进一步诊
治，再次就诊我院。
过敏史：未发现。
体格检查：神志清晰，皮肤色泽正常，淋巴结未触及肿大；心脏：心律齐，心
音正常；肺：双肺语颤正常、对称，双肺呼吸音清，未闻及异常呼吸音，双肺
未闻及干湿性啰音；腹部：平软，无压痛、反跳痛，肝脾肋下未触及。
辅助检查：2026-03-24超声报告：彩超检查（常规）-浅表(超声报告
号:20260070720)双侧颈部多发淋巴结肿大（倾向淋巴结转移）；
诊断：
西医诊断：
食管恶性肿瘤(ypT3N1M0 IIIIB期)
中医诊断：
处理措施：进一步系统治疗。
药品处方：
检验检查：
医生签名：
签名时间:2026-03-24 15:16
---
29.11.11.73
临时用户
福建省肿瘤医院病历记录
姓名
入院记录
姓
出生地：福建省福
性
别：男
职业：无职业
年
龄：61岁
病史陈述者：患者本人
民
族：汉族
可靠程度：基本可靠
婚
姻：已婚
入院时间：2024年12月31日08时12分
过敏史：未发现
记录时间：2024年12月31日08时36分
主诉：食管胃连接处腺癌新辅助化免治疗后术后1月余。
现病史：患者于2024-09-02以"进行性吞咽困难2个月"为主诉入院。2024-08-
23于连江县晓澳卫生院行胃镜示"贲门肿块浸润性癌；食管下段浸润伴狭窄"；
胃镜病理示：（贲门）腺癌。多层螺旋CT平扫+增强扫描+MPR：1.考虑贲门-
胃体癌伴胃周淋巴结肿大，请结合胃镜及腹部影像学检查；2.双肺多形性变
伴纵隔、双肺门淋巴结钙化，尘肺可能，请结合病史；3.双肺上叶、右肺中
叶较大肺大泡；4.扫及肝囊肿，请结合腹部影像学检查；病理会诊报告号（
H24-03863）：（贲门）腺癌。相关检查未见明显化疗禁忌症，遂于
2024.09.04、2024.09.27、2024.10.25以"奥沙利铂 160mg ivgtt d1+5-FU
4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w"方案行术前第1-3周期
129.11.11.73
临时用户
T牧入肿入泡；4.扫及肝囊肿，有结台腹部影像子检查；病理会诊报告号（
H24-03863）：（贲门）腺癌。相关检查未见明显化疗禁忌症，遂于
2024.09.04、2024.09.27、2024.10.25以"奥沙利铂 160mg ivgtt d1+5-FU
4.5g 微量泵泵入 48h+信迪利单抗 200mg ivgtt q3w"方案行术前第1-3周期
化疗，化疗过程顺利。相关检查无手术禁忌症，经充分术前准备后于2024-11
-28在全麻下行"腹腔镜辅助食管胃交界处癌根治术"，术程顺利，恢复良好。
术后病理回报（病理号：24-31776）：下段食管+近端胃切除标本：（食管胃
交界）隆起型低分化腺癌（肿物大小8x7cm，Lauren分型：混合型），伴治疗
反应（TRG：3级，残余肿瘤约占90%），肿瘤侵犯浆膜下层，脉管内见癌栓，
神经见癌侵犯。标本上、下切端及另送“上切端”未见癌。淋巴结2/35见转
移癌（“2”LN1/4、“7”LN1/14、胃小弯LN0/6、“1”LN0/2、“4”LN0/2、
“8”LN0/6、“9”LN0/1、“11”LN0/2，“3、5”未见LN，“10”查见癌结
节1枚）。胃小弯LN1/6、“7”LN1/14见治疗后反应。肿瘤病理分期：
ypT3N1Mx（AJCC 第八版）。免疫组化结果：MSH2（+），MSH6（+），
MLH1（+），PMS2（+），HER2（0），CD34（血管+），D2-40（淋巴管+），
129.1.11.73
临时用户
第 1 页
129.1.11.73
临时用户
P53（+），EGFR（60%强着色，20%中等着色，20%弱着色），Ki-67（80% +），CD3（T细胞+，约占肿瘤区域10%），CD8（约占CD3阳性细胞数60%），
PD1（约占CD3阳性细胞数20%），PD-L1（CPS=5），PD-L1neg（-），P40（ -），Syn（部分+），CgA（少量+），CD56（-），CK5/6（-）。原位杂交
EBER（-）。患者无咯血丝痰；无咳嗽、盗汗，无胸痛、心悸、头晕、头痛，
无寒战、发热，无声音嘶哑、饮水呛咳、眼睑下垂，无血尿、少尿、腰背酸
痛。今为求进一步治疗就诊我院，门诊拟"食管胃连接处癌新辅助化免治疗后
术后"收入院。发病以来精神睡眠尚可，食欲欠佳，大小便正常，体力、体重
无明显下降。
既往史：详见旧病历（住院号：
个人史：详见旧病历（住院号.
婚育史：详见旧病历（住院号：
家族史：详见旧病历（住院号：
73
体格检查
T: 36.5 ℃ P: 74 次/分 R: 12 次/分 BP: 120 / 80 mmHg
发育正常，营养中等，表情自然，正常面容，自主体位，步入病房，步态正常。
神志清楚，查体合作。全身皮肤粘膜无黄染、苍白、发绀、出血点、水肿、肝
掌、溃疡、蜘蛛痣。浅表淋巴结检查详见专科情况。头颅无畸形，双眼睑无水
肿，眼球无突出及震颤，结膜无苍白、充血、出血或水肿，巩膜无黄染，双侧
瞳孔等大正圆，对光反射灵敏。耳廓外形正常，外耳道无分泌物，乳突无压痛。
鼻外形正常，口唇无苍白，咽无充血，颈无抵抗，未见颈动脉异常搏动，未见
颈静脉怒张。气管居中，甲状腺未触及肿大，质软，未及结节，未及震颤，
间及九立 万列晾对称 未触及肿物 引业于活流 小前区子收扣 小小博动
临时用户
体格检查
T: 36.5 ℃ P: 74 次/分 R: 12 次/分 BP: 120 / 80 mmHg
发育正常，营养中等，表情自然，正常面容，自主体位，步入病房，步态正常。
神志清楚，查体合作。全身皮肤粘膜无黄染、苍白、发绀、出血点、水肿、肝
掌、溃疡、蜘蛛痣。浅表淋巴结检查详见专科情况。头颅无畸形，双眼睑无水
肿，眼球无突出及震颤，结膜无苍白、充血、出血或水肿，巩膜无黄染，双侧
瞳孔等大正圆，对光反射灵敏。耳廓外形正常，外耳道无分泌物，乳突无压痛。
鼻外形正常，口唇无苍白，咽无充血，颈无抵抗，未见颈动脉异常搏动，未见
颈静脉怒张。气管居中，甲状腺未触及肿大，质软，未及结节，未及震颤，未
闻及杂音。双乳腺对称，未触及肿物，乳头无溢液。心前区无隆起，心尖搏动
位于第5肋间左锁骨中线内0.5cm，未见异常搏动，未触及震颤，无心包摩擦感，
心界不大，心率74次/分，心律齐，心音正常。P2<A2，未见异常血管征，各瓣
膜听诊区未闻及杂音及心包摩擦音，腹部平坦，未见胃、肠型及蠕动波，未见
腹壁静脉曲张，腹软，无压痛、未触及包块，Murphy征阴性，肝脾肋下未及。
肝区肾区无叩痛，腹部叩诊鼓音，移动性浊音(-)。肠鸣音4次/分。脊柱活动
度可，生理弯曲存在，四肢无畸形，关节无红肿及压痛，主动活动正常，双下
129.1.11.73
临时用户
第 2 页
129.1.11.73
临时用户
姓名
肢无水肿。双侧膝腱反射对称引出，双侧Babinski征(-)，脑膜刺激征-，肛门
及外生殖器未见明显异常。
专科检查：神志清楚，营养中等。双颈、双锁骨上、双腋窝未触及肿大淋巴
结。腹部见术痕，愈合好；胸廓无畸形，气管居中；双肺呼吸运动平稳，触
觉语颤正常对称，叩诊清音，听诊未闻及干湿罗音及胸膜摩擦音，双肺呼吸
音清晰。
辅助检查：暂缺。
出院诊断
1、手术后恶性肿瘤化学治疗
2、食管胃连接处隆起型低分化腺
癌新辅助化疗后术后（
ypT3N1M0 IIIIB期）
3、尘肺？
4、右肝囊肿
5、左肝胆管内结石
6、左肾囊肿
7、PICC置入术
书写医生：
2025年01月06日
审核医生：
2025年01月06日
初步诊断
1、食管胃连接处隆起型低分化腺癌新辅
助化免治疗后术后（ypT3N1M0 IIIIB期）
2、尘肺？
3、右肝囊肿
4、左肝胆管内结石
5、左肾囊肿
6、PICC置入术
书写医生：
2024年12月31日
审核医生：
2024年12月31日
---
双侧颈部4区探及数个淋巴结，大者分别约1.7cm×1.2cm（左）、1.6cm×0.7cm（右），边界尚清，形
态饱满，淋巴结门消失，CDFI示：内部及周边见有血流信号；余颈部未见明显异常肿大淋巴结。
检查所见
双侧颈部多发淋巴结肿大（倾向淋巴结转移）
检查提示
手术过程
阳性 阳性
病理报告
骨髓报告
检查申请
检验申请
输血申请
手术申请单
感染报告
传染报告
死亡报告
浏览超声报告文件
检查(检验)结果比较
影像分析处理
超声报告
超声影像
穿刺活检前超声检查（仅对穿刺活检淋巴结描述）：左侧锁骨上见肿大淋巴结，大小约1.8cm×1.1cm，
边界尚清，内部未见淋巴门回声，CDFI：淋巴结内可见血流信号。
今日15：00-15:08在彩超引导下，常规消毒、铺巾、局麻后，用16G半自动快速组织活检枪，由左下颈分别
进针约2.8cm、2.7cm，达左侧锁骨上淋巴结内缘后，按压快门，接着迅速拔针，可见短条状组织块送细胞及组织病
理检查。
穿刺过程顺利，患者无不适。
彩超引导下左侧锁骨上淋巴结快速组织活检
检查提示
---
手术过程
阳性 阳性
报告
申请
申请
申请
手术申请单
报告
报告
报告
浏览影像报告文件
检查(检验)结果比较
影像分析处理
检查部位名称
检查报告
影像列表
4.头颅+躯干(颅底至
检查序号0005140996
检查日期2026-03-18 14:04:49
检查类型PETCT
检查片号P68729
检查部位头颅+躯干(颅底到大腿中上 检查方式
报告医师陈炜佳
报告时间2026-03-18 14 审核医师刘道佳
审核时间2026-03-18
影像所见
是否异常 是
“胃食管连接处癌术后”：吻合口壁未见明显增厚及FDG摄取异常增高。腹膜后见多发肿大淋巴
结，较大者最大横截面约2.1cm×1.1cm，FDG摄取增高，SUVmax5.0。腹膜稍增厚，FDG摄取未见
明显增高。腹水征阴性。
大脑各部显像清晰，脑实质密度正常，中线居中，诸脑室系统未见明
显扩大，脑池、脑沟未见明显增宽。脑皮质及基底节区FDG分布均匀，左右对称，未见明显异常稀
疏或缺损改变。小脑FDG分布亦未见明显异常。双眼及副鼻窦未见明显异常密度影及异常FDG摄取
增高。鼻咽部结构对称，两侧未见软组织肿块影，双侧咽隐窝、咽旁间隙存在，咽旁肌群未见FDG
异常摄取增高，颅底骨质未见破坏。口咽部两侧腺体显影对称。甲状腺两叶不大，形态可，腺实质
内未见FDG增高灶。颈部未见肿大淋巴结，相应部位未见FDG异常摄取增高。
双肺见多发不规则
斑片、条索、结节、粟粒影，部分伴钙化，以双肺上叶为著，FDG摄取轻度增高，SUVmax3.5；双
肺见多发透亮无肺纹理区，较大者位于右肺尖，最大横截面约8.9cm×5.8cm。双侧锁骨区见数枚
肿大淋巴结，较大者位于左侧，最大横截面约1.8cm×0.9cm，FDG摄取轻度增高，SUVmax4.0。纵
隔、双侧肺门见多发肿大淋巴结，伴钙化，较大者短径约1.7cm，FDG摄取轻度增高，SUVmax4.0
。两侧腋窝未见肿大淋巴结或淋巴结FDG异常摄取增高。心肌显影清晰。气管居中。双侧胸膜稍增
厚。双侧胸腔少量积液。纵隔大血管本底SUVmax1.4。
肝脏形态可，轮廓光整，肝叶比例正常，
肝V段见一囊样低密度影，最大横截面约5.9cm×4.6cm，FDG摄取缺损；余肝实质内FDG分布稍欠
均匀，SUVmax2.0。肝内外胆管无扩张。胆囊大小正常，密度均匀，胆囊壁无增厚。肝门结构正
常。胰腺形态FDG分布尚好，胰管不扩张。脾脏轻度显影，FDG分布均匀。两侧肾脏显影可，左肾
影像诊断
“胃食管连接处癌术后”：
1、①腹膜后多发肿大淋巴结，代谢增高，考虑转移可能；②双侧锁
骨区数枚肿大淋巴结，代谢轻度增高，炎性增生？转移待排除，请结合临床。
2、腹膜稍增厚，
低代谢，建议随诊。
3、双肺多形性改变，纵隔、双侧肺门多发淋巴结，轻微代谢，结合职业
史，以上考虑炎性肉芽肿性病变，建议随诊；双肺多发肺大泡。
4、双侧胸膜稍增厚；双侧胸腔
少量积液。
5、肝囊肿；左肾囊肿。
6、左侧肩关节、右侧髋关节炎性病变。
58 未F
---
863 已F
76 已F
病例库 病理会诊
姓名
性别 男
住院号
年龄 61岁
病区/
床号 /
送检单位 连江县晓澳卫 送检科室 /
送检医生
收到日期 2024-08-28
取材医生
取材日期 2024-08-28
标本名称 /
临床诊断
肉眼所见
镜下所见
病理诊断（贲门）腺癌。
特殊检查
未发报告原因
报告医生 力超
审核医生 力超
报告日期 2024-09-02 报告状态 已审核
---
姓名
性别男
年龄01岁
床号
送检单位本院
送检科室
收到日期2024-11-28
取材医生
取材日期2024-11-29
标本名称下段食管+近端胃
临床诊断
肉眼所见小弯LN8个，直径0.1-0.5cm；大弯LN未见；
1LN2个，直径0.5-1.5cm；2LN2个，直径1.5-2cm；3LN未见；4LN2个，直径0.1-0.2cm；
5LN未见；7LN6个，直径0.5-2.5cm；8LN1个，直径2.5cm；9LN1个，直径1.5cm；10LN2
个，直径1-1.5cm；11LN1个，直径1.5cm；
[肉眼诊断]
下段食管+近端胃切除标本：上切间距3cm，下切间距10cm，小弯8cm，大弯12cm，紧靠上
切，距下切1.5cm，于食管胃交界小弯处见一隆起型肿物，大小8x7cm，切面灰白，质硬，
镜下所见
病理诊断下段食管+近端胃切除标本：
（食管胃交界）隆起型低分化腺癌（肿物大小8x7cm，Lauren分型：混合型），伴治疗反
应（TRG：3级，残余肿瘤约占90%），肿瘤侵犯浆膜下层，脉管内见癌栓，神经见癌侵犯。
标本上、下切端及另送“上切端”未见癌。淋巴结2/35见转移癌（“
2”LN1/4、“7”LN1/14、胃小弯LNO/6、“
1”LNO/2、“4”LNO/2、“8”LNO/6、“9”LNO/1、“11”LNO/2，“3、5”未见LN，
“10”查见癌结节1枚）。胃小弯LN1/6、“7”LN1/14见治疗后反应。
肿瘤病理分期：ypT3N1Mx（AJCC第八版）。
特殊检查
免疫组化结果：MSH2（+），MSH6（+），MLH1（+），PMS2（+），HER2（0），CD34（血
未发报告原因
报告医生陈丽芳
审核医生陈丽芳
报告日期2024-12-05
报告状态已审核
2026-08-10 16:38:39,222 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 16:38:39,222 INFO     29 [Trace] task=dca6cdea | doc=LBZH，男，63岁，胃癌一线(1).pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "7 items, types={'LabReport': 1, 'OutpatientRecord': 1, 'AdmissionRecord': 1, 'ExaminationReport': 4}", "name": "LBZH，男，63岁，胃癌一线(1).pdf", "embedding_token_consumption": 9086}
2026-08-10 16:38:39,222 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 16:38:39,528 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 16:38:39,528 INFO     29 [Trace] task=dca6cdea | doc=LBZH，男，63岁，胃癌一线(1).pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":7,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 16:38:39,533 INFO     29 [DIAG-EXECUTOR] row_position_int len=57 row[0]=(1, 1198, 1316, 228, 266) row[-1]=(7, 677, 1160, 450, 501)
2026-08-10 16:38:39,534 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 16:38:39,535 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 16:38:39,535 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 16:38:39,535 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 16:38:39,535 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 16:38:39,535 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 16:38:39,540 INFO     29 set_progress(dca6cdea94d711f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 16:38:39 [DOC Engine]:
Start to index...
2026-08-10 16:38:39,728 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.175s]
2026-08-10 16:38:39,732 INFO     29 set_progress(dca6cdea94d711f1bd9827cf206dfa2d), progress: 0.8142857142857143, progress_msg: 
2026-08-10 16:38:39,780 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.026s]
2026-08-10 16:38:39,791 INFO     29 set_progress(dca6cdea94d711f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 16:38:39 Indexing done (0.25s). Task done (836.32s)
2026-08-10 16:38:39,799 INFO     29 [Done], chunks(7), token(9086), elapsed:836.32
2026-08-10 16:38:40,082 INFO     29 handle_task done for task {"id": "dca6cdea94d711f1bd9827cf206dfa2d", "doc_id": "dbef275894d711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "type": "pdf", "location": "LBZH\uff0c\u7537\uff0c63\u5c81\uff0c\u80c3\u764c\u4e00\u7ebf(1).pdf", "size": 28457006, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786379026603, "task_type": "dataflow", "root_trace_id": "00f6a24fb6bd4742ba80c2030b932c44", "root_traceparent": "00-00f6a24fb6bd4742ba80c2030b932c44-fbfb6d98b4675b32-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
