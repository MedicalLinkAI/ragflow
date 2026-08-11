# 基准结果：WAYA-糖尿病-长春.pdf

## 基本信息

- 文件：`WAYA-糖尿病-长春.pdf`
- 大小：27572.0 KB
- PDF 总页数：8
- doc_id：`47f841b294c111f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T21:42:06  完成时间：2026-08-10T21:44:06  耗时：120.1s
- progress_msg：`13:43:54 Indexing done (0.05s). Task done (98.99s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 5f2d83a7 | 1 | 1-1 | 吉林省人民醫院 门（急）诊病历 姓名： 性别：男 年龄： 时间：2024年3月7 |
| 2 | 3dfb64a4 | 1 | 2-2 | 黑龙江博尚医院 门诊病历 姓名： 门诊号：2403 科室：综合内科门诊 性别：男 |
| 3 | deeb6da6 | 1 | 7-7 | 长春民康利药房 票号：04311228929 收银员：77 会员 交易时间：20 |
| 4 | e695dec7 | 1 | 8-8 | 长春民康利药房 票号：04311345628 收银员：77 会员名 交易时间：2 |
| 5 | 5e694c9e | 1 | 3-3 | <table><tr><td>血糖</td><td>GLU</td><td>10 |
| 6 | 06f03d82 | 1 | 4-4 | <table><tr><td>糖化血红蛋白</td><td>HbA1c</td> |
| 7 | 36772671 | 1 | 5-5 | <table><tr><td>葡萄糖测定(空腹己糖激酶法)</td><td>GL |
| 8 | d630c4bc | 1 | 6-6 | <table><tr><td>糖化血红蛋白（高效液相色谱法）</td><td>0 |

- chunks 总数：8
- 各 chunk 页数合计（含跨页重复）：8
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8]`
- 覆盖页数：8 / 8；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 2 | 0 | 2 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 2 | 2 | 2 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 0 | 1 | 0 | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 4 | 0 | 4 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 2, "LabReport": 4, "MedicationRecord": 2}`
- ChunkMerger：`{"found": true, "merged": 8, "sources": 9, "stats": {"Extractor:LabExam": 4, "Extractor:Imaging": 1, "Extractor:Clinical": 2, "Extractor:Medication": 2, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1, "Extractor:Progress": 1}, "filtered_noise": 6}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 13:43:53,727 INFO     29 [ChunkMerger] Merged 8 chunks from 9 sources: {'Extractor:LabExam': 4, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 2, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 13:42:10,977 INFO     29 handle_task begin for task {"id": "48817b4494c111f1bd9827cf206dfa2d", "doc_id": "47f841b294c111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "WAYA-\u7cd6\u5c3f\u75c5-\u957f\u6625.pdf", "type": "pdf", "location": "WAYA-\u7cd6\u5c3f\u75c5-\u957f\u6625.pdf", "size": 28233765, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786369329126, "task_type": "dataflow", "root_trace_id": "3a85c9850cd6423785dc819c3129b342", "root_traceparent": "00-3a85c9850cd6423785dc819c3129b342-ef8a80a2724cffe2-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 13:42:11,204 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 13:42:11,315 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 13:42:11,341 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:42:11,341 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 13:42:11,342 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 13:42:11,346 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 13:42:11,346 INFO     29 ============================================================
2026-08-10 13:42:11,346 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 13:42:11,346 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 13:42:11,346 INFO     29 ============================================================
2026-08-10 13:42:11,346 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 13:42:11,346 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 13:42:11,348 INFO     29 No torch found.
2026-08-10 13:42:12,365 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=8
2026-08-10 13:42:12,815 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2548661, prompt_len=764
2026-08-10 13:42:14,259 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:42:14,260 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 13:42:14,268 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2548661, prompt_len=401
2026-08-10 13:42:16,844 INFO     29 [qwen-vl-parser] text API response (len=411):
["吉林省人民醫院", "门（急）诊病历", "姓名：", "性别：男", "年龄：", "时间：2024年3月7日", "门诊号：2403070", "婚姻：", "职业：其他", "就诊类型：○初诊○复诊○急诊", "过敏史：否认药物及食品过敏史", "科室：内分泌代谢病二科门诊", "住址：", "主诉：糖尿病开药", "简要病史：糖尿病，要求开二甲双胍。", "既往史和其他病史：", "体格检查（选填项目）：体温：", "；脉搏：次/分；呼", "吸：次/分；血压/mmHg。", "专科检查(必要项目)：", "辅助检查及结果：", "初步诊断：2型糖尿病", "诊疗意见：口服,每天二次,次/次,盐酸二甲双胍缓释片,", "每天二次, 1.00g/次", "签名：蒋立军", "时间：2024年03月07日13时04分39", "秒", "(以上病历交予患者,是否为本次诊疗最终病历无需补充:○是○否)"]
2026-08-10 13:42:16,845 INFO     29 [qwen-vl-parser] page=1 text: 28 lines (bbox 0-27)
2026-08-10 13:42:16,845 INFO     29 [qwen-vl-parser] page=1 text: 28 sections
2026-08-10 13:42:17,052 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1023443, prompt_len=764
2026-08-10 13:42:18,475 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:42:18,475 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 13:42:18,489 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1023443, prompt_len=401
2026-08-10 13:42:22,168 INFO     29 [qwen-vl-parser] text API response (len=317):
["黑龙江博尚医院", "门诊病历", "姓名：", "门诊号：2403", "科室：综合内科门诊", "性别：男", "年龄：43岁", "就诊时间：2024-02-21 10:49", "主诉：", "多饮，多尿，多食，口干，口渴半年，加重一周。", "现病史：", "既往史：", "既往否认重要病史。", "药物过敏史：", "无。", "辅助检查：", "检验结果-2024-02-21 09:51- 空腹血糖16.40mmol/L↑", "检验结果-2024-02-21 09:44- 糖化血红蛋白8.58%↑", "初步诊断：", "2型糖尿病", "处理措施：", "每天2次，每次1.0g", "医师签名：李月菊"]
2026-08-10 13:42:22,168 INFO     29 [qwen-vl-parser] page=2 text: 23 lines (bbox 28-50)
2026-08-10 13:42:22,169 INFO     29 [qwen-vl-parser] page=2 text: 23 sections
2026-08-10 13:42:22,310 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=518563, prompt_len=764
2026-08-10 13:42:23,667 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2024-02-19"
}
```
2026-08-10 13:42:23,667 INFO     29 [qwen-vl-parser] page=3 classify=table report_date=2024-02-19
2026-08-10 13:42:23,676 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=518563, prompt_len=756
2026-08-10 13:42:24,600 INFO     29 [qwen-vl-parser] table API response (len=141):
\begin{tabular}{ccccccc}
\hline
项目名称 & 英文简称 & 结果 & 单位 & 提示 & 参考范围 \\
\hline
血糖 & GLU & 10.46 & mmol/L & H & 3.89-6.11 \\
\hline
\end{tabular}
2026-08-10 13:42:24,601 INFO     29 [qwen-vl-parser] page=3 table: 8 LaTeX lines (bbox 51-58)
2026-08-10 13:42:24,601 INFO     29 [qwen-vl-parser] page=3 table: 8 sections
2026-08-10 13:42:24,755 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=754662, prompt_len=764
2026-08-10 13:42:26,131 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2024-02-19"
}
```
2026-08-10 13:42:26,131 INFO     29 [qwen-vl-parser] page=4 classify=table report_date=2024-02-19
2026-08-10 13:42:26,144 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=754662, prompt_len=756
2026-08-10 13:42:27,083 INFO     29 [qwen-vl-parser] table API response (len=128):
\begin{tabular}{ccccccc}
\hline
检测项目 & 项目简称 & 检测结果 & 单位 & 参考区间 \\
\hline
糖化血红蛋白 & HbA1c & 9.8 & \% & 4-6 \\
\hline
\end{tabular}
2026-08-10 13:42:27,083 INFO     29 [qwen-vl-parser] page=4 table: 8 LaTeX lines (bbox 59-66)
2026-08-10 13:42:27,083 INFO     29 [qwen-vl-parser] page=4 table: 8 sections
2026-08-10 13:42:27,180 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=597165, prompt_len=764
2026-08-10 13:42:28,538 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-04-10"
}
```
2026-08-10 13:42:28,538 INFO     29 [qwen-vl-parser] page=5 classify=table report_date=2025-04-10
2026-08-10 13:42:28,543 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=597165, prompt_len=756
2026-08-10 13:42:29,541 INFO     29 [qwen-vl-parser] table API response (len=153):
\begin{tabular}{ccccccl}
\hline
项目代号 & 项目名称 & 结果 & 单位 & 参考值 & & \\
\hline
GLU & ★*葡萄糖测定(空腹己糖激酶法) & 11.50↑ & mmol/L & 3.9--6.1 & & \\
\hline
\end{tabular}
2026-08-10 13:42:29,543 INFO     29 [qwen-vl-parser] page=5 table: 8 LaTeX lines (bbox 67-74)
2026-08-10 13:42:29,543 INFO     29 [qwen-vl-parser] page=5 table: 8 sections
2026-08-10 13:42:29,639 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=548134, prompt_len=764
2026-08-10 13:42:30,956 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-04-10"
}
```
2026-08-10 13:42:30,957 INFO     29 [qwen-vl-parser] page=6 classify=table report_date=2025-04-10
2026-08-10 13:42:30,964 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=548134, prompt_len=756
2026-08-10 13:42:31,280 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:42:31.279+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 55, "failed": 0, "current": {"48817b4494c111f1bd9827cf206dfa2d": {"id": "48817b4494c111f1bd9827cf206dfa2d", "doc_id": "47f841b294c111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "WAYA-\u7cd6\u5c3f\u75c5-\u957f\u6625.pdf", "type": "pdf", "location": "WAYA-\u7cd6\u5c3f\u75c5-\u957f\u6625.pdf", "size": 28233765, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786369329126, "task_type": "dataflow", "root_trace_id": "3a85c9850cd6423785dc819c3129b342", "root_traceparent": "00-3a85c9850cd6423785dc819c3129b342-ef8a80a2724cffe2-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:42:32,314 INFO     29 [qwen-vl-parser] table API response (len=157):
\begin{tabular}{ccccccl}
\hline
项目代号 & 项目名称 & 结果 & 单位 & 参考值 & & \\
\hline
0101409 & 糖化血红蛋白（高效液相色谱法） & 8.40 $\uparrow$ & \% & 4--6 & & \\
\hline
\end{tabular}
2026-08-10 13:42:32,315 INFO     29 [qwen-vl-parser] page=6 table: 8 LaTeX lines (bbox 75-82)
2026-08-10 13:42:32,316 INFO     29 [qwen-vl-parser] page=6 table: 8 sections
2026-08-10 13:42:32,964 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3680496, prompt_len=764
2026-08-10 13:42:34,411 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:42:34,413 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-10 13:42:34,432 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3680496, prompt_len=401
2026-08-10 13:42:36,713 INFO     29 [qwen-vl-parser] text API response (len=340):
["长春民康利药房", "票号：04311228929", "收银员：77", "会员", "交易时间：2025-1-22", "18:21:22", "品名", "规格", "单位", "内码", "数量", "单价", "金额", "生产企业", "生产批号", "圣邦杰", "盐酸二甲双胍缓释片(山东司邦得", "制药有限公司)", "0.5g*40T", "单价", "4.8", "数量10", "合计48.00", "总页数：1.00", "总折扣：0.00", "合计：48.00", "付款：48.00", "找零：0.00", "*号代表含兴奋剂药品，请运动员慎", "用", "祝您健康！", "请您当日开取发票，如有其他", "原因请在15日内开取发票"]
2026-08-10 13:42:36,713 INFO     29 [qwen-vl-parser] page=7 text: 33 lines (bbox 83-115)
2026-08-10 13:42:36,713 INFO     29 [qwen-vl-parser] page=7 text: 33 sections
2026-08-10 13:42:37,338 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3506598, prompt_len=764
2026-08-10 13:42:38,773 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:42:38,775 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=None
2026-08-10 13:42:38,793 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3506598, prompt_len=401
2026-08-10 13:42:41,143 INFO     29 [qwen-vl-parser] text API response (len=341):
["长春民康利药房", "票号：04311345628", "收银员：77", "会员名", "交易时间：2025-4-29", "12:28:12", "品名", "规格", "单位", "内码", "数量", "单价", "金额", "生产企业", "生产批号", "圣邦杰", "盐酸二甲双胍缓释片(山东司邦得", "制药有限公司)", "0.5g*40T", "单价", "4.8", "数量10", "合计48.00", "总页数：1.00", "总折扣：0.00", "合计：48.00", "付款：48.00", "找零：0.00", "*号代表含兴奋剂药品,请运动员慎", "用", "祝您健康!", "请您当日开取发票，如有其他", "原因请在15日内开取发票"]
2026-08-10 13:42:41,144 INFO     29 [qwen-vl-parser] page=8 text: 33 lines (bbox 116-148)
2026-08-10 13:42:41,144 INFO     29 [qwen-vl-parser] page=8 text: 33 sections
2026-08-10 13:42:41,144 INFO     29 [qwen-vl-parser] parse_pdf done: 149 sections from 8 pages.
2026-08-10 13:42:41,149 INFO     29 Close text detector.
2026-08-10 13:42:41,558 INFO     29 Close text recognizer.
2026-08-10 13:42:41,947 INFO     29 Close recognizer.
2026-08-10 13:42:42,380 INFO     29 Close recognizer.
2026-08-10 13:42:42,848 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 13:42:42,849 INFO     29 [Trace] task=48817b44 | doc=WAYA-糖尿病-长春.pdf | Parser:MedLink | outputs={"html": "", "json": "149 items", "markdown": "", "text": "", "name": "WAYA-糖尿病-长春.pdf", "output_format": "json"}
2026-08-10 13:42:42,849 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 13:42:42,868 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:42:42,868 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 吉林省人民醫院\n[BBOX-1] 门（急）诊病历\n[BBOX-2] 姓名：\n[BBOX-3] 性别：男\n[BBOX-4] 年龄：\n[BBOX-5] 时间：2024年3月7日\n[BBOX-6] 门诊号：2403070\n[BBOX-7] 婚姻：\n[BBOX-8] 职业：其他\n[BBOX-9] 就诊类型：○初诊○复诊○急诊\n[BBOX-10] 过敏史：否认药物及食品过敏史\n[BBOX-11] 科室：内分泌代谢病二科门诊\n[BBOX-12] 住址：\n[BBOX-13] 主诉：糖尿病开药\n[BBOX-14] 简要病史：糖尿病，要求开二甲双胍。\n[BBOX-15] 既往史和其他病史：\n[BBOX-16] 体格检查（选填项目）：体温：\n[BBOX-17] ；脉搏：次/分；呼\n[BBOX-18] 吸：次/分；血压/mmHg。\n[BBOX-19] 专科检查(必要项目)：\n[BBOX-20] 辅助检查及结果：\n[BBOX-21] 初步诊断：2型糖尿病\n[BBOX-22] 诊疗意见：口服,每天二次,次/次,盐酸二甲双胍缓释片,\n[BBOX-23] 每天二次, 1.00g/次\n[BBOX-24] 签名：蒋立军\n[BBOX-25] 时间：2024年03月07日13时04分39\n[BBOX-26] 秒\n[BBOX-27] (以上病历交予患者,是否为本次诊疗最终病历无需补充:○是○否)\n[BBOX-28] 黑龙江博尚医院\n[BBOX-29] 门诊病历\n[BBOX-30] 姓名：\n[BBOX-31] 门诊号：2403\n[BBOX-32] 科室：综合内科门诊\n[BBOX-33] 性别：男\n[BBOX-34] 年龄：43岁\n[BBOX-35] 就诊时间：2024-02-21 10:49\n[BBOX-36] 主诉：\n[BBOX-37] 多饮，多尿，多食，口干，口渴半年，加重一周。\n[BBOX-38] 现病史：\n[BBOX-39] 既往史：\n[BBOX-40] 既往否认重要病史。\n[BBOX-41] 药物过敏史：\n[BBOX-42] 无。\n[BBOX-43] 辅助检查：\n[BBOX-44] 检验结果-2024-02-21 09:51- 空腹血糖16.40mmol/L↑\n[BBOX-45] 检验结果-2024-02-21 09:44- 糖化血红蛋白8.58%↑\n[BBOX-46] 初步诊断：\n[BBOX-47] 2型糖尿病\n[BBOX-48] 处理措施：\n[BBOX-49] 每天2次，每次1.0g\n[BBOX-50] 医师签名：李月菊\n[BBOX-51] \\begin{tabular}{ccccccc}\n[BBOX-52] 报告时间: 2024-02-19\n[BBOX-53] \\hline\n[BBOX-54] 项目名称 & 英文简称 & 结果 & 单位 & 提示 & 参考范围 \\\\\n[BBOX-55] \\hline\n[BBOX-56] 血糖 & GLU & 10.46 & mmol/L & H & 3.89-6.11 \\\\\n[BBOX-57] \\hline\n[BBOX-58] \\end{tabular}\n[BBOX-59] \\begin{tabular}{ccccccc}\n[BBOX-60] 报告时间: 2024-02-19\n[BBOX-61] \\hline\n[BBOX-62] 检测项目 & 项目简称 & 检测结果 & 单位 & 参考区间 \\\\\n[BBOX-63] \\hline\n[BBOX-64] 糖化血红蛋白 & HbA1c & 9.8 & \\% & 4-6 \\\\\n[BBOX-65] \\hline\n[BBOX-66] \\end{tabular}\n[BBOX-67] \\begin{tabular}{ccccccl}\n[BBOX-68] 报告时间: 2025-04-10\n[BBOX-69] \\hline\n[BBOX-70] 项目代号 & 项目名称 & 结果 & 单位 & 参考值 & & \\\\\n[BBOX-71] \\hline\n[BBOX-72] GLU & ★*葡萄糖测定(空腹己糖激酶法) & 11.50↑ & mmol/L & 3.9--6.1 & & \\\\\n[BBOX-73] \\hline\n[BBOX-74] \\end{tabular}\n[BBOX-75] \\begin{tabular}{ccccccl}\n[BBOX-76] 报告时间: 2025-04-10\n[BBOX-77] \\hline\n[BBOX-78] 项目代号 & 项目名称 & 结果 & 单位 & 参考值 & & \\\\\n[BBOX-79] \\hline\n[BBOX-80] 0101409 & 糖化血红蛋白（高效液相色谱法） & 8.40 $\\uparrow$ & \\% & 4--6 & & \\\\\n[BBOX-81] \\hline\n[BBOX-82] \\end{tabular}\n[BBOX-83] 长春民康利药房\n[BBOX-84] 票号：04311228929\n[BBOX-85] 收银员：77\n[BBOX-86] 会员\n[BBOX-87] 交易时间：2025-1-22\n[BBOX-88] 18:21:22\n[BBOX-89] 品名\n[BBOX-90] 规格\n[BBOX-91] 单位\n[BBOX-92] 内码\n[BBOX-93] 数量\n[BBOX-94] 单价\n[BBOX-95] 金额\n[BBOX-96] 生产企业\n[BBOX-97] 生产批号\n[BBOX-98] 圣邦杰\n[BBOX-99] 盐酸二甲双胍缓释片(山东司邦得\n[BBOX-100] 制药有限公司)\n[BBOX-101] 0.5g*40T\n[BBOX-102] 单价\n[BBOX-103] 4.8\n[BBOX-104] 数量10\n[BBOX-105] 合计48.00\n[BBOX-106] 总页数：1.00\n[BBOX-107] 总折扣：0.00\n[BBOX-108] 合计：48.00\n[BBOX-109] 付款：48.00\n[BBOX-110] 找零：0.00\n[BBOX-111] *号代表含兴奋剂药品，请运动员慎\n[BBOX-112] 用\n[BBOX-113] 祝您健康！\n[BBOX-114] 请您当日开取发票，如有其他\n[BBOX-115] 原因请在15日内开取发票\n[BBOX-116] 长春民康利药房\n[BBOX-117] 票号：04311345628\n[BBOX-118] 收银员：77\n[BBOX-119] 会员名\n[BBOX-120] 交易时间：2025-4-29\n[BBOX-121] 12:28:12\n[BBOX-122] 品名\n[BBOX-123] 规格\n[BBOX-124] 单位\n[BBOX-125] 内码\n[BBOX-126] 数量\n[BBOX-127] 单价\n[BBOX-128] 金额\n[BBOX-129] 生产企业\n[BBOX-130] 生产批号\n[BBOX-131] 圣邦杰\n[BBOX-132] 盐酸二甲双胍缓释片(山东司邦得\n[BBOX-133] 制药有限公司)\n[BBOX-134] 0.5g*40T\n[BBOX-135] 单价\n[BBOX-136] 4.8\n[BBOX-137] 数量10\n[BBOX-138] 合计48.00\n[BBOX-139] 总页数：1.00\n[BBOX-140] 总折扣：0.00\n[BBOX-141] 合计：48.00\n[BBOX-142] 付款：48.00\n[BBOX-143] 找零：0.00\n[BBOX-144] *号代表含兴奋剂药品,请运动员慎\n[BBOX-145] 用\n[BBOX-146] 祝您健康!\n[BBOX-147] 请您当日开取发票，如有其他\n[BBOX-148] 原因请在15日内开取发票"
  }
]
2026-08-10 13:42:49,536 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:42:49,554 INFO     29 [SmartSplitter] SmartSplitter done: 8 chunks from 8 LLM segments (all bbox_id). Types: {'OutpatientRecord': 2, 'LabReport': 4, 'MedicationRecord': 2}
2026-08-10 13:42:49,561 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 13:42:49,561 INFO     29 [Trace] task=48817b44 | doc=WAYA-糖尿病-长春.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "149 items", "markdown": "", "text": "", "name": "WAYA-糖尿病-长春.pdf", "output_format": "chunks", "chunks": "8 items, types={'OutpatientRecord': 2, 'LabReport': 4, 'MedicationRecord': 2}"}
2026-08-10 13:42:49,562 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 13:42:49,562 INFO     29 [ChunkRouter] Routed 8 chunks into 3 groups: {'chunks_Clinical': 2, 'chunks_LabExam': 4, 'chunks_Medication': 2}
2026-08-10 13:42:49,570 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 13:42:49,570 INFO     29 [Trace] task=48817b44 | doc=WAYA-糖尿病-长春.pdf | ChunkRouter:Router | outputs={"html": "", "json": "149 items", "markdown": "", "text": "", "name": "WAYA-糖尿病-长春.pdf", "output_format": "chunks", "chunks": "8 items, types={'OutpatientRecord': 2, 'LabReport': 4, 'MedicationRecord': 2}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 4, \"chunks_Medication\": 2}"}
2026-08-10 13:42:49,570 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 13:42:49,575 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:42:49,575 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:42:49,576 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[2]
2026-08-10 13:42:49,576 INFO     29 [qwen-vl-table] positions ： [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:42:49,762 INFO     29 [qwen-vl-table] page=2, rect=595x841, img=(1653x2337)
2026-08-10 13:42:49,762 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:42:49,763 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 51, \"bbox_end\": 58, \"encounter_dates\": [\"2024-02-19\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccc}\n报告时间: 2024-02-19\n\\hline\n项目名称 & 英文简称 & 结果 & 单位 & 提示 & 参考范围 \\\\\n\\hline\n血糖 & GLU & 10.46 & mmol/L & H & 3.89-6.11 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:42:51,004 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:42:51,005 INFO     29 [qwen-vl-table] page=2 LLM output (len=218):
{
  "report_date": "2024-02-19",
  "items": [
    {
      "name": "血糖",
      "item_code": "GLU",
      "value": "10.46",
      "unit": "mmol/L",
      "reference_range": "3.89-6.11",
      "abnormal": true
    }
  ]
}
2026-08-10 13:42:51,005 INFO     29 [qwen-vl-table] coord grouping: {2: 1}
2026-08-10 13:42:51,008 INFO     29 [qwen-vl-table] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=681236, prompt_len=509
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
血糖

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
2026-08-10 13:42:53,998 INFO     29 [qwen-vl-table] coord API raw response (len=60):
```json
[
	{"text": "血糖", "bbox": [73, 167, 102, 180]}
]
```
2026-08-10 13:42:53,998 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=3.0s
2026-08-10 13:42:53,998 INFO     29 [qwen-vl-table] coord item[0]: text=血糖, bbox=[73, 167, 102, 180]
2026-08-10 13:42:53,998 INFO     29 [qwen-vl-table] page=2 coord: matched 1/1, time=3.0s
2026-08-10 13:42:53,998 INFO     29 [qwen-vl-table] new_positions (1):
[[3, 43.434999999999995, 60.69, 140.447, 151.38]]
2026-08-10 13:42:53,998 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=4.4s
2026-08-10 13:42:54,000 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:42:54,002 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:42:54,002 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[3]
2026-08-10 13:42:54,002 INFO     29 [qwen-vl-table] positions ： [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:42:54,171 INFO     29 [qwen-vl-table] page=3, rect=595x841, img=(1653x2337)
2026-08-10 13:42:54,171 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:42:54,172 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 59, \"bbox_end\": 66, \"encounter_dates\": [\"2024-02-19\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccc}\n报告时间: 2024-02-19\n\\hline\n检测项目 & 项目简称 & 检测结果 & 单位 & 参考区间 \\\\\n\\hline\n糖化血红蛋白 & HbA1c & 9.8 & \\% & 4-6 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:42:55,309 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:42:55,309 INFO     29 [qwen-vl-table] page=3 LLM output (len=211):
{
  "report_date": "2024-02-19",
  "items": [
    {
      "name": "糖化血红蛋白",
      "item_code": "HbA1c",
      "value": "9.8",
      "unit": "%",
      "reference_range": "4-6",
      "abnormal": true
    }
  ]
}
2026-08-10 13:42:55,309 INFO     29 [qwen-vl-table] coord grouping: {3: 1}
2026-08-10 13:42:55,313 INFO     29 [qwen-vl-table] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=999411, prompt_len=513
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
糖化血红蛋白

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
2026-08-10 13:42:56,900 INFO     29 [qwen-vl-table] coord API raw response (len=65):
```json
[
	{"text": "糖化血红蛋白", "bbox": [236, 482, 307, 492]}
]
```
2026-08-10 13:42:56,900 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=1.6s
2026-08-10 13:42:56,900 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白, bbox=[236, 482, 307, 492]
2026-08-10 13:42:56,900 INFO     29 [qwen-vl-table] page=3 coord: matched 1/1, time=1.6s
2026-08-10 13:42:56,900 INFO     29 [qwen-vl-table] new_positions (1):
[[4, 140.42, 182.665, 405.36199999999997, 413.772]]
2026-08-10 13:42:56,901 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=2.9s
2026-08-10 13:42:56,902 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:42:56,908 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:42:56,908 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[4]
2026-08-10 13:42:56,908 INFO     29 [qwen-vl-table] positions ： [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:42:57,073 INFO     29 [qwen-vl-table] page=4, rect=595x841, img=(1653x2337)
2026-08-10 13:42:57,074 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:42:57,074 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 67, \"bbox_end\": 74, \"encounter_dates\": [\"2025-04-10\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccl}\n报告时间: 2025-04-10\n\\hline\n项目代号 & 项目名称 & 结果 & 单位 & 参考值 & & \\\\\n\\hline\nGLU & ★*葡萄糖测定(空腹己糖激酶法) & 11.50↑ & mmol/L & 3.9--6.1 & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:42:58,293 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:42:58,294 INFO     29 [qwen-vl-table] page=4 LLM output (len=229):
{
  "report_date": "2025-04-10",
  "items": [
    {
      "name": "葡萄糖测定(空腹己糖激酶法)",
      "item_code": "GLU",
      "value": "11.50",
      "unit": "mmol/L",
      "reference_range": "3.9--6.1",
      "abnormal": true
    }
  ]
}
2026-08-10 13:42:58,294 INFO     29 [qwen-vl-table] coord grouping: {4: 1}
2026-08-10 13:42:58,295 INFO     29 [qwen-vl-table] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=663682, prompt_len=521
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
葡萄糖测定(空腹己糖激酶法)

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
2026-08-10 13:42:59,802 INFO     29 [qwen-vl-table] coord API raw response (len=73):
```json
[
	{"text": "葡萄糖测定(空腹己糖激酶法)", "bbox": [170, 205, 416, 220]}
]
```
2026-08-10 13:42:59,802 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=1.5s
2026-08-10 13:42:59,802 INFO     29 [qwen-vl-table] coord item[0]: text=葡萄糖测定(空腹己糖激酶法), bbox=[170, 205, 416, 220]
2026-08-10 13:42:59,803 INFO     29 [qwen-vl-table] page=4 coord: matched 1/1, time=1.5s
2026-08-10 13:42:59,803 INFO     29 [qwen-vl-table] new_positions (1):
[[5, 101.14999999999999, 247.51999999999998, 172.405, 185.01999999999998]]
2026-08-10 13:42:59,803 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=2.9s
2026-08-10 13:42:59,807 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:42:59,809 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:42:59,809 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[5]
2026-08-10 13:42:59,809 INFO     29 [qwen-vl-table] positions ： [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:42:59,972 INFO     29 [qwen-vl-table] page=5, rect=595x841, img=(1653x2337)
2026-08-10 13:42:59,972 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:42:59,973 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 75, \"bbox_end\": 82, \"encounter_dates\": [\"2025-04-10\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccl}\n报告时间: 2025-04-10\n\\hline\n项目代号 & 项目名称 & 结果 & 单位 & 参考值 & & \\\\\n\\hline\n0101409 & 糖化血红蛋白（高效液相色谱法） & 8.40 $\\uparrow$ & \\% & 4--6 & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:43:01,191 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:43:01,191 INFO     29 [qwen-vl-table] page=5 LLM output (len=224):
{
  "report_date": "2025-04-10",
  "items": [
    {
      "name": "糖化血红蛋白（高效液相色谱法）",
      "item_code": "0101409",
      "value": "8.40",
      "unit": "%",
      "reference_range": "4--6",
      "abnormal": true
    }
  ]
}
2026-08-10 13:43:01,191 INFO     29 [qwen-vl-table] coord grouping: {5: 1}
2026-08-10 13:43:01,192 INFO     29 [qwen-vl-table] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=580707, prompt_len=522
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
糖化血红蛋白（高效液相色谱法）

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
2026-08-10 13:43:02,706 INFO     29 [qwen-vl-table] coord API raw response (len=74):
```json
[
	{"text": "糖化血红蛋白（高效液相色谱法）", "bbox": [169, 200, 418, 214]}
]
```
2026-08-10 13:43:02,706 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=1.5s
2026-08-10 13:43:02,706 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白（高效液相色谱法）, bbox=[169, 200, 418, 214]
2026-08-10 13:43:02,707 INFO     29 [qwen-vl-table] page=5 coord: matched 1/1, time=1.5s
2026-08-10 13:43:02,707 INFO     29 [qwen-vl-table] new_positions (1):
[[6, 100.55499999999999, 248.70999999999998, 168.2, 179.974]]
2026-08-10 13:43:02,707 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=2.9s
2026-08-10 13:43:02,722 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 13:43:02,723 INFO     29 [Trace] task=48817b44 | doc=WAYA-糖尿病-长春.pdf | Extractor:LabExam | outputs={"chunks": "4 items, types={'LabReport': 4}", "html": "", "json": "149 items", "markdown": "", "text": "", "name": "WAYA-糖尿病-长春.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 4, \"chunks_Medication\": 2}"}
2026-08-10 13:43:02,723 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 13:43:02,729 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:43:02,729 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:43:02,847 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:43:02.846+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 55, "failed": 0, "current": {"48817b4494c111f1bd9827cf206dfa2d": {"id": "48817b4494c111f1bd9827cf206dfa2d", "doc_id": "47f841b294c111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "WAYA-\u7cd6\u5c3f\u75c5-\u957f\u6625.pdf", "type": "pdf", "location": "WAYA-\u7cd6\u5c3f\u75c5-\u957f\u6625.pdf", "size": 28233765, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786369329126, "task_type": "dataflow", "root_trace_id": "3a85c9850cd6423785dc819c3129b342", "root_traceparent": "00-3a85c9850cd6423785dc819c3129b342-ef8a80a2724cffe2-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:43:03,541 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:43:03,552 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 13:43:03,552 INFO     29 [Trace] task=48817b44 | doc=WAYA-糖尿病-长春.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "149 items", "markdown": "", "text": "", "name": "WAYA-糖尿病-长春.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 4, \"chunks_Medication\": 2}"}
2026-08-10 13:43:03,552 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 13:43:03,560 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:43:03,560 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:43:03,561 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 13:43:03,561 INFO     29 [qwen-vl-text] positions(28): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:43:03,561 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [28]
2026-08-10 13:43:03,993 INFO     29 [qwen-vl-text] page=0, rect=595x841, img=(1653x2337), dpi=200
2026-08-10 13:43:03,995 INFO     29 [qwen-vl-text] LLM extraction start, text_len=326
2026-08-10 13:43:03,995 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:43:03,996 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 27, \"encounter_dates\": [\"2024-03-07\"], \"department\": \"内分泌代谢病二科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "吉林省人民醫院\n门（急）诊病历\n姓名：\n性别：男\n年龄：\n时间：2024年3月7日\n门诊号：2403070\n婚姻：\n职业：其他\n就诊类型：○初诊○复诊○急诊\n过敏史：否认药物及食品过敏史\n科室：内分泌代谢病二科门诊\n住址：\n主诉：糖尿病开药\n简要病史：糖尿病，要求开二甲双胍。\n既往史和其他病史：\n体格检查（选填项目）：体温：\n；脉搏：次/分；呼\n吸：次/分；血压/mmHg。\n专科检查(必要项目)：\n辅助检查及结果：\n初步诊断：2型糖尿病\n诊疗意见：口服,每天二次,次/次,盐酸二甲双胍缓释片,\n每天二次, 1.00g/次\n签名：蒋立军\n时间：2024年03月07日13时04分39\n秒\n(以上病历交予患者,是否为本次诊疗最终病历无需补充:○是○否)",
    "role": "user"
  }
]
2026-08-10 13:43:05,452 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:43:05,452 INFO     29 [qwen-vl-text] LLM output (len=208):
{
  "encounter_date": "2024-03-07",
  "chief_complaint": "糖尿病开药",
  "present_illness": "糖尿病，要求开二甲双胍。",
  "past_history": "否认药物及食品过敏史",
  "diagnosis": "2型糖尿病",
  "treatment_plan": "盐酸二甲双胍缓释片 1.00g/次 口服 每天二次"
}
2026-08-10 13:43:05,452 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-03-07]
2026-08-10 13:43:05,465 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3406460, prompt_len=1023
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共28行）
["吉林省人民醫院", "门（急）诊病历", "姓名：", "性别：男", "年龄：", "时间：2024年3月7日", "门诊号：2403070", "婚姻：", "职业：其他", "就诊类型：○初诊○复诊○急诊", "过敏史：否认药物及食品过敏史", "科室：内分泌代谢病二科门诊", "住址：", "主诉：糖尿病开药", "简要病史：糖尿病，要求开二甲双胍。", "既往史和其他病史：", "体格检查（选填项目）：体温：", "；脉搏：次/分；呼", "吸：次/分；血压/mmHg。", "专科检查(必要项目)：", "辅助检查及结果：", "初步诊断：2型糖尿病", "诊疗意见：口服,每天二次,次/次,盐酸二甲双胍缓释片,", "每天二次, 1.00g/次", "签名：蒋立军", "时间：2024年03月07日13时04分39", "秒", "(以上病历交予患者,是否为本次诊疗最终病历无需补充:○是○否)"]

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
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord API raw response (len=1557):
[
	{"text": "吉林省人民醫院", "bbox": [360, 33, 693, 65]},
	{"text": "门（急）诊病历", "bbox": [355, 70, 654, 99]},
	{"text": "姓名：", "bbox": [140, 109, 200, 130]},
	{"text": "性别：男", "bbox": [414, 110, 525, 131]},
	{"text": "年龄：", "bbox": [140, 139, 208, 159]},
	{"text": "时间：2024年3月7日", "bbox": [413, 140, 664, 160]},
	{"text": "门诊号：2403070", "bbox": [140, 168, 355, 189]},
	{"text": "婚姻：", "bbox": [514, 169, 595, 190]},
	{"text": "职业：其他", "bbox": [139, 197, 309, 218]},
	{"text": "就诊类型：○初诊○复诊○急诊", "bbox": [354, 198, 726, 219]},
	{"text": "过敏史：否认药物及食品过敏史", "bbox": [138, 232, 541, 254]},
	{"text": "科室：内分泌代谢病二科门诊", "bbox": [138, 262, 541, 284]},
	{"text": "住址：", "bbox": [138, 293, 237, 314]},
	{"text": "主诉：糖尿病开药", "bbox": [139, 338, 372, 360]},
	{"text": "简要病史：糖尿病，要求开二甲双胍。", "bbox": [139, 368, 613, 390]},
	{"text": "既往史和其他病史：", "bbox": [139, 399, 384, 420]},
	{"text": "体格检查（选填项目）：体温：", "bbox": [139, 430, 527, 452]},
	{"text": "；脉搏：次/分；呼", "bbox": [619, 430, 818, 451]},
	{"text": "吸：次/分；血压/mmHg。", "bbox": [139, 460, 458, 482]},
	{"text": "专科检查(必要项目)：", "bbox": [139, 490, 416, 512]},
	{"text": "辅助检查及结果：", "bbox": [138, 521, 355, 543]},
	{"text": "初步诊断：2型糖尿病", "bbox": [138, 551, 416, 573]},
	{"text": "诊疗意见：口服,每天二次,次/次,盐酸二甲双胍缓释片,", "bbox": [136, 581, 849, 604]},
	{"text": "每天二次, 1.00g/次", "bbox": [135, 614, 445, 637]},
	{"text": "签名：蒋立军", "bbox": [144, 691, 355, 729]},
	{"text": "时间：2024年03月07日13时04分39", "bbox": [415, 708, 875, 731]},
	{"text": "秒", "bbox": [144, 744, 173, 765]},
	{"text": "(以上病历交予患者,是否为本次诊疗最终病历无需补充:○是○否)", "bbox": [134, 797, 777, 819]}
]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord API: raw_items=28, valid_items=28, elapsed=8.9s
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[0]: text=吉林省人民醫院, bbox=[360, 33, 693, 65]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[1]: text=门（急）诊病历, bbox=[355, 70, 654, 99]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[140, 109, 200, 130]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[3]: text=性别：男, bbox=[414, 110, 525, 131]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：, bbox=[140, 139, 208, 159]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[5]: text=时间：2024年3月7日, bbox=[413, 140, 664, 160]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[6]: text=门诊号：2403070, bbox=[140, 168, 355, 189]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[7]: text=婚姻：, bbox=[514, 169, 595, 190]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[8]: text=职业：其他, bbox=[139, 197, 309, 218]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[9]: text=就诊类型：○初诊○复诊○急诊, bbox=[354, 198, 726, 219]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[10]: text=过敏史：否认药物及食品过敏史, bbox=[138, 232, 541, 254]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[11]: text=科室：内分泌代谢病二科门诊, bbox=[138, 262, 541, 284]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[12]: text=住址：, bbox=[138, 293, 237, 314]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[13]: text=主诉：糖尿病开药, bbox=[139, 338, 372, 360]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[14]: text=简要病史：糖尿病，要求开二甲双胍。, bbox=[139, 368, 613, 390]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[15]: text=既往史和其他病史：, bbox=[139, 399, 384, 420]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[16]: text=体格检查（选填项目）：体温：, bbox=[139, 430, 527, 452]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[17]: text=；脉搏：次/分；呼, bbox=[619, 430, 818, 451]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[18]: text=吸：次/分；血压/mmHg。, bbox=[139, 460, 458, 482]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[19]: text=专科检查(必要项目)：, bbox=[139, 490, 416, 512]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[20]: text=辅助检查及结果：, bbox=[138, 521, 355, 543]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[21]: text=初步诊断：2型糖尿病, bbox=[138, 551, 416, 573]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[22]: text=诊疗意见：口服,每天二次,次/次,盐酸二甲双胍缓释片,, bbox=[136, 581, 849, 604]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[23]: text=每天二次, 1.00g/次, bbox=[135, 614, 445, 637]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[24]: text=签名：蒋立军, bbox=[144, 691, 355, 729]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[25]: text=时间：2024年03月07日13时04分39, bbox=[415, 708, 875, 731]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[26]: text=秒, bbox=[144, 744, 173, 765]
2026-08-10 13:43:14,355 INFO     29 [qwen-vl-text] coord item[27]: text=(以上病历交予患者,是否为本次诊疗最终病历无需补充:○是○否), bbox=[134, 797, 777, 819]
2026-08-10 13:43:14,356 INFO     29 [qwen-vl-text] page=0 — 28/28 coords, api_time=8.9s
2026-08-10 13:43:14,356 INFO     29 [qwen-vl-text] new_positions (28):
[[0, 214.2, 412.335, 27.753, 54.665], [0, 211.225, 389.13, 58.87, 83.259], [0, 83.3, 119.0, 91.669, 109.33], [0, 246.32999999999998, 312.375, 92.50999999999999, 110.17099999999999], [0, 83.3, 123.75999999999999, 116.899, 133.719], [0, 245.73499999999999, 395.08, 117.74, 134.56], [0, 83.3, 211.225, 141.28799999999998, 158.94899999999998], [0, 305.83, 354.025, 142.129, 159.79], [0, 82.705, 183.855, 165.677, 183.338], [0, 210.63, 431.96999999999997, 166.518, 184.179], [0, 82.11, 321.895, 195.112, 213.614], [0, 82.11, 321.895, 220.34199999999998, 238.844], [0, 82.11, 141.015, 246.41299999999998, 264.074], [0, 82.705, 221.34, 284.258, 302.76], [0, 82.705, 364.73499999999996, 309.488, 327.99], [0, 82.705, 228.48, 335.55899999999997, 353.21999999999997], [0, 82.705, 313.565, 361.63, 380.132], [0, 368.305, 486.71, 361.63, 379.291], [0, 82.705, 272.51, 386.86, 405.36199999999997], [0, 82.705, 247.51999999999998, 412.09, 430.592], [0, 82.11, 211.225, 438.161, 456.663], [0, 82.11, 247.51999999999998, 463.39099999999996, 481.893], [0, 80.92, 505.155, 488.621, 507.964], [0, 80.325, 264.775, 516.374, 535.717], [0, 85.67999999999999, 211.225, 581.131, 613.0889999999999], [0, 246.92499999999998, 520.625, 595.428, 614.771], [0, 85.67999999999999, 102.935, 625.704, 643.365], [0, 79.72999999999999, 462.315, 670.2769999999999, 688.779]]
2026-08-10 13:43:14,356 INFO     29 [qwen-vl-text] ═══ DONE ═══ 28 positions, pages=1, time=10.8s
2026-08-10 13:43:14,356 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:43:14,357 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:43:14,357 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 13:43:14,357 INFO     29 [qwen-vl-text] positions(23): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:43:14,358 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [23]
2026-08-10 13:43:14,586 INFO     29 [qwen-vl-text] page=1, rect=595x841, img=(1653x2337), dpi=200
2026-08-10 13:43:14,589 INFO     29 [qwen-vl-text] LLM extraction start, text_len=247
2026-08-10 13:43:14,589 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:43:14,590 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 28, \"bbox_end\": 50, \"encounter_dates\": [\"2024-02-21\"], \"department\": \"综合内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "黑龙江博尚医院\n门诊病历\n姓名：\n门诊号：2403\n科室：综合内科门诊\n性别：男\n年龄：43岁\n就诊时间：2024-02-21 10:49\n主诉：\n多饮，多尿，多食，口干，口渴半年，加重一周。\n现病史：\n既往史：\n既往否认重要病史。\n药物过敏史：\n无。\n辅助检查：\n检验结果-2024-02-21 09:51- 空腹血糖16.40mmol/L↑\n检验结果-2024-02-21 09:44- 糖化血红蛋白8.58%↑\n初步诊断：\n2型糖尿病\n处理措施：\n每天2次，每次1.0g\n医师签名：李月菊",
    "role": "user"
  }
]
2026-08-10 13:43:16,317 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:43:16,318 INFO     29 [qwen-vl-text] LLM output (len=200):
{
  "encounter_date": "2024-02-21",
  "chief_complaint": "多饮，多尿，多食，口干，口渴半年，加重一周。",
  "present_illness": null,
  "past_history": "既往否认重要病史。",
  "diagnosis": "2型糖尿病",
  "treatment_plan": "每天2次，每次1.0g"
}
2026-08-10 13:43:16,318 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-02-21]
2026-08-10 13:43:16,322 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1341408, prompt_len=929
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共23行）
["黑龙江博尚医院", "门诊病历", "姓名：", "门诊号：2403", "科室：综合内科门诊", "性别：男", "年龄：43岁", "就诊时间：2024-02-21 10:49", "主诉：", "多饮，多尿，多食，口干，口渴半年，加重一周。", "现病史：", "既往史：", "既往否认重要病史。", "药物过敏史：", "无。", "辅助检查：", "检验结果-2024-02-21 09:51- 空腹血糖16.40mmol/L↑", "检验结果-2024-02-21 09:44- 糖化血红蛋白8.58%↑", "初步诊断：", "2型糖尿病", "处理措施：", "每天2次，每次1.0g", "医师签名：李月菊"]

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
2026-08-10 13:43:25,592 INFO     29 [qwen-vl-text] coord API raw response (len=1349):
[
	{"text": "黑龙江博尚医院", "bbox": [395, 63, 555, 80]},
	{"text": "门诊病历", "bbox": [411, 87, 538, 104]},
	{"text": "姓名：", "bbox": [180, 116, 225, 131]},
	{"text": "门诊号：2403", "bbox": [310, 117, 431, 131]},
	{"text": "科室：", "bbox": [507, 115, 555, 130]},
	{"text": "综合内科门诊", "bbox": [603, 115, 724, 130]},
	{"text": "性别：男", "bbox": [180, 144, 259, 158]},
	{"text": "年龄：", "bbox": [310, 144, 359, 158]},
	{"text": "43岁", "bbox": [390, 144, 428, 158]},
	{"text": "就诊时间：2024-02-21 10:49", "bbox": [507, 143, 766, 157]},
	{"text": "主诉：", "bbox": [180, 177, 225, 191]},
	{"text": "多饮，多尿，多食，口干，口渴半年，加重一周。", "bbox": [190, 197, 619, 212]},
	{"text": "现病史：", "bbox": [177, 229, 244, 244]},
	{"text": "既往史：", "bbox": [176, 280, 244, 295]},
	{"text": "既往否认重要病史。", "bbox": [184, 302, 359, 317]},
	{"text": "药物过敏史：", "bbox": [174, 333, 284, 348]},
	{"text": "无。", "bbox": [184, 355, 212, 369]},
	{"text": "辅助检查：", "bbox": [171, 386, 262, 400]},
	{"text": "检验结果-2024-02-21 09:51- 空腹血糖16.40mmol/L↑", "bbox": [180, 407, 668, 422]},
	{"text": "检验结果-2024-02-21 09:44- 糖化血红蛋白8.58%↑", "bbox": [170, 429, 637, 444]},
	{"text": "初步诊断：", "bbox": [169, 461, 259, 476]},
	{"text": "2型糖尿病", "bbox": [177, 483, 272, 498]},
	{"text": "处理措施：", "bbox": [166, 515, 257, 530]},
	{"text": "每天2次，每次1.0g", "bbox": [176, 537, 355, 553]},
	{"text": "医师签名：李月菊", "bbox": [537, 590, 719, 608]}
]
2026-08-10 13:43:25,593 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=9.3s
2026-08-10 13:43:25,593 INFO     29 [qwen-vl-text] coord item[0]: text=黑龙江博尚医院, bbox=[395, 63, 555, 80]
2026-08-10 13:43:25,593 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[411, 87, 538, 104]
2026-08-10 13:43:25,593 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[180, 116, 225, 131]
2026-08-10 13:43:25,593 INFO     29 [qwen-vl-text] coord item[3]: text=门诊号：2403, bbox=[310, 117, 431, 131]
2026-08-10 13:43:25,593 INFO     29 [qwen-vl-text] coord item[4]: text=科室：, bbox=[507, 115, 555, 130]
2026-08-10 13:43:25,593 INFO     29 [qwen-vl-text] coord item[5]: text=综合内科门诊, bbox=[603, 115, 724, 130]
2026-08-10 13:43:25,593 INFO     29 [qwen-vl-text] coord item[6]: text=性别：男, bbox=[180, 144, 259, 158]
2026-08-10 13:43:25,593 INFO     29 [qwen-vl-text] coord item[7]: text=年龄：, bbox=[310, 144, 359, 158]
2026-08-10 13:43:25,593 INFO     29 [qwen-vl-text] coord item[8]: text=43岁, bbox=[390, 144, 428, 158]
2026-08-10 13:43:25,594 INFO     29 [qwen-vl-text] coord item[9]: text=就诊时间：2024-02-21 10:49, bbox=[507, 143, 766, 157]
2026-08-10 13:43:25,594 INFO     29 [qwen-vl-text] coord item[10]: text=主诉：, bbox=[180, 177, 225, 191]
2026-08-10 13:43:25,594 INFO     29 [qwen-vl-text] coord item[11]: text=多饮，多尿，多食，口干，口渴半年，加重一周。, bbox=[190, 197, 619, 212]
2026-08-10 13:43:25,594 INFO     29 [qwen-vl-text] coord item[12]: text=现病史：, bbox=[177, 229, 244, 244]
2026-08-10 13:43:25,594 INFO     29 [qwen-vl-text] coord item[13]: text=既往史：, bbox=[176, 280, 244, 295]
2026-08-10 13:43:25,594 INFO     29 [qwen-vl-text] coord item[14]: text=既往否认重要病史。, bbox=[184, 302, 359, 317]
2026-08-10 13:43:25,594 INFO     29 [qwen-vl-text] coord item[15]: text=药物过敏史：, bbox=[174, 333, 284, 348]
2026-08-10 13:43:25,594 INFO     29 [qwen-vl-text] coord item[16]: text=无。, bbox=[184, 355, 212, 369]
2026-08-10 13:43:25,594 INFO     29 [qwen-vl-text] coord item[17]: text=辅助检查：, bbox=[171, 386, 262, 400]
2026-08-10 13:43:25,594 INFO     29 [qwen-vl-text] coord item[18]: text=检验结果-2024-02-21 09:51- 空腹血糖16.40mmol/L↑, bbox=[180, 407, 668, 422]
2026-08-10 13:43:25,594 INFO     29 [qwen-vl-text] coord item[19]: text=检验结果-2024-02-21 09:44- 糖化血红蛋白8.58%↑, bbox=[170, 429, 637, 444]
2026-08-10 13:43:25,594 INFO     29 [qwen-vl-text] coord item[20]: text=初步诊断：, bbox=[169, 461, 259, 476]
2026-08-10 13:43:25,595 INFO     29 [qwen-vl-text] coord item[21]: text=2型糖尿病, bbox=[177, 483, 272, 498]
2026-08-10 13:43:25,595 INFO     29 [qwen-vl-text] coord item[22]: text=处理措施：, bbox=[166, 515, 257, 530]
2026-08-10 13:43:25,595 INFO     29 [qwen-vl-text] coord item[23]: text=每天2次，每次1.0g, bbox=[176, 537, 355, 553]
2026-08-10 13:43:25,595 INFO     29 [qwen-vl-text] coord item[24]: text=医师签名：李月菊, bbox=[537, 590, 719, 608]
2026-08-10 13:43:25,596 INFO     29 [qwen-vl-text] page=1 — 23/23 coords, api_time=9.3s
2026-08-10 13:43:25,596 INFO     29 [qwen-vl-text] new_positions (23):
[[1, 235.02499999999998, 330.22499999999997, 52.983, 67.28], [1, 244.545, 320.11, 73.167, 87.464], [1, 107.1, 133.875, 97.556, 110.17099999999999], [1, 184.45, 256.445, 98.39699999999999, 110.17099999999999], [1, 301.66499999999996, 330.22499999999997, 96.715, 109.33], [1, 358.78499999999997, 430.78, 96.715, 109.33], [1, 107.1, 154.105, 121.104, 132.878], [1, 184.45, 213.605, 121.104, 132.878], [1, 232.04999999999998, 254.66, 121.104, 132.878], [1, 301.66499999999996, 455.77, 120.26299999999999, 132.037], [1, 107.1, 133.875, 148.857, 160.631], [1, 113.05, 368.305, 165.677, 178.292], [1, 105.315, 145.18, 192.589, 205.20399999999998], [1, 104.72, 145.18, 235.48, 248.095], [1, 109.47999999999999, 213.605, 253.982, 266.597], [1, 103.53, 168.98, 280.053, 292.668], [1, 109.47999999999999, 126.14, 298.555, 310.329], [1, 101.74499999999999, 155.89, 324.626, 336.4], [1, 107.1, 397.46, 342.287, 354.902], [1, 101.14999999999999, 379.015, 360.789, 373.404], [1, 100.55499999999999, 154.105, 387.70099999999996, 400.316], [1, 105.315, 161.84, 406.203, 418.818], [1, 98.77, 152.915, 433.115, 445.72999999999996]]
2026-08-10 13:43:25,596 INFO     29 [qwen-vl-text] ═══ DONE ═══ 23 positions, pages=1, time=11.2s
2026-08-10 13:43:25,607 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 13:43:25,607 INFO     29 [Trace] task=48817b44 | doc=WAYA-糖尿病-长春.pdf | Extractor:Clinical | outputs={"chunks": "2 items, types={'OutpatientRecord': 2}", "html": "", "json": "149 items", "markdown": "", "text": "", "name": "WAYA-糖尿病-长春.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 4, \"chunks_Medication\": 2}"}
2026-08-10 13:43:25,607 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 13:43:25,613 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:43:25,614 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:43:25,614 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 13:43:25,614 INFO     29 [qwen-vl-text] positions(33): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:43:25,614 INFO     29 [qwen-vl-text] page grouping: [6], lines per page: [33]
2026-08-10 13:43:26,057 INFO     29 [qwen-vl-text] page=6, rect=595x841, img=(1653x2337), dpi=200
2026-08-10 13:43:26,059 INFO     29 [qwen-vl-text] LLM extraction start, text_len=240
2026-08-10 13:43:26,060 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:43:26,060 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 83, \"bbox_end\": 115, \"encounter_dates\": [\"2025-01-22\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "长春民康利药房\n票号：04311228929\n收银员：77\n会员\n交易时间：2025-1-22\n18:21:22\n品名\n规格\n单位\n内码\n数量\n单价\n金额\n生产企业\n生产批号\n圣邦杰\n盐酸二甲双胍缓释片(山东司邦得\n制药有限公司)\n0.5g*40T\n单价\n4.8\n数量10\n合计48.00\n总页数：1.00\n总折扣：0.00\n合计：48.00\n付款：48.00\n找零：0.00\n*号代表含兴奋剂药品，请运动员慎\n用\n祝您健康！\n请您当日开取发票，如有其他\n原因请在15日内开取发票",
    "role": "user"
  }
]
2026-08-10 13:43:28,227 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:43:28,227 INFO     29 [qwen-vl-text] LLM output (len=425):
{
  "encounter_date": "2025-01-22",
  "pharmacy": "长春民康利药房",
  "medications": [
    {
      "name": "圣邦杰 盐酸二甲双胍缓释片",
      "specification": "0.5g*40T",
      "dosage": null,
      "quantity": 10,
      "unit_price": 4.8,
      "total_price": 48.00,
      "frequency": null,
      "route": null,
      "manufacturer": "山东司邦得制药有限公司",
      "approval_number": null
    }
  ],
  "payment_total": 48.00,
  "payment_method": null
}
2026-08-10 13:43:28,227 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-01-22]
2026-08-10 13:43:28,240 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5537167, prompt_len=952
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["长春民康利药房", "票号：04311228929", "收银员：77", "会员", "交易时间：2025-1-22", "18:21:22", "品名", "规格", "单位", "内码", "数量", "单价", "金额", "生产企业", "生产批号", "圣邦杰", "盐酸二甲双胍缓释片(山东司邦得", "制药有限公司)", "0.5g*40T", "单价", "4.8", "数量10", "合计48.00", "总页数：1.00", "总折扣：0.00", "合计：48.00", "付款：48.00", "找零：0.00", "*号代表含兴奋剂药品，请运动员慎", "用", "祝您健康！", "请您当日开取发票，如有其他", "原因请在15日内开取发票"]

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
2026-08-10 13:43:37,928 INFO     29 [qwen-vl-text] coord API raw response (len=1695):
[
	{"text": "长春民康利药房", "bbox": [350, 119, 603, 152]},
	{"text": "票号：04311228929", "bbox": [236, 188, 508, 214]},
	{"text": "收银员：77", "bbox": [552, 185, 715, 212]},
	{"text": "会员", "bbox": [236, 228, 324, 253]},
	{"text": "交易时间：2025-1-22", "bbox": [236, 270, 538, 294]},
	{"text": "18:21:22", "bbox": [584, 269, 715, 290]},
	{"text": "品名", "bbox": [238, 338, 300, 361]},
	{"text": "规格", "bbox": [489, 340, 545, 363]},
	{"text": "单位", "bbox": [644, 337, 707, 360]},
	{"text": "内码", "bbox": [272, 377, 334, 400]},
	{"text": "数量", "bbox": [381, 378, 441, 401]},
	{"text": "单价", "bbox": [519, 377, 575, 401]},
	{"text": "金额", "bbox": [625, 377, 689, 400]},
	{"text": "生产企业", "bbox": [272, 416, 395, 439]},
	{"text": "生产批号", "bbox": [577, 416, 701, 439]},
	{"text": "圣邦杰", "bbox": [243, 480, 336, 503]},
	{"text": "盐酸二甲双胍缓释片(山东司邦得", "bbox": [245, 518, 701, 545]},
	{"text": "制药有限公司)", "bbox": [245, 553, 443, 577]},
	{"text": "0.5g*40T", "bbox": [528, 558, 654, 581]},
	{"text": "单价", "bbox": [245, 592, 304, 615]},
	{"text": "4.8", "bbox": [335, 592, 384, 611]},
	{"text": "数量10", "bbox": [412, 590, 502, 612]},
	{"text": "合计48.00", "bbox": [558, 595, 702, 621]},
	{"text": "总页数：1.00", "bbox": [245, 628, 429, 651]},
	{"text": "总折扣：0.00", "bbox": [514, 630, 700, 660]},
	{"text": "合计：48.00", "bbox": [276, 688, 444, 711]},
	{"text": "付款：48.00", "bbox": [484, 689, 651, 720]},
	{"text": "找零：0.00", "bbox": [292, 722, 443, 745]},
	{"text": "*号代表含兴奋剂药品，请运动员慎", "bbox": [247, 753, 692, 791]},
	{"text": "用", "bbox": [248, 785, 278, 805]},
	{"text": "祝您健康！", "bbox": [398, 808, 524, 837]},
	{"text": "请您当日开取发票，如有其他", "bbox": [311, 841, 687, 879]},
	{"text": "原因请在15日内开取发票", "bbox": [252, 873, 564, 905]}
]
2026-08-10 13:43:37,929 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=9.7s
2026-08-10 13:43:37,929 INFO     29 [qwen-vl-text] coord item[0]: text=长春民康利药房, bbox=[350, 119, 603, 152]
2026-08-10 13:43:37,929 INFO     29 [qwen-vl-text] coord item[1]: text=票号：04311228929, bbox=[236, 188, 508, 214]
2026-08-10 13:43:37,929 INFO     29 [qwen-vl-text] coord item[2]: text=收银员：77, bbox=[552, 185, 715, 212]
2026-08-10 13:43:37,929 INFO     29 [qwen-vl-text] coord item[3]: text=会员, bbox=[236, 228, 324, 253]
2026-08-10 13:43:37,929 INFO     29 [qwen-vl-text] coord item[4]: text=交易时间：2025-1-22, bbox=[236, 270, 538, 294]
2026-08-10 13:43:37,929 INFO     29 [qwen-vl-text] coord item[5]: text=18:21:22, bbox=[584, 269, 715, 290]
2026-08-10 13:43:37,929 INFO     29 [qwen-vl-text] coord item[6]: text=品名, bbox=[238, 338, 300, 361]
2026-08-10 13:43:37,929 INFO     29 [qwen-vl-text] coord item[7]: text=规格, bbox=[489, 340, 545, 363]
2026-08-10 13:43:37,929 INFO     29 [qwen-vl-text] coord item[8]: text=单位, bbox=[644, 337, 707, 360]
2026-08-10 13:43:37,930 INFO     29 [qwen-vl-text] coord item[9]: text=内码, bbox=[272, 377, 334, 400]
2026-08-10 13:43:37,930 INFO     29 [qwen-vl-text] coord item[10]: text=数量, bbox=[381, 378, 441, 401]
2026-08-10 13:43:37,930 INFO     29 [qwen-vl-text] coord item[11]: text=单价, bbox=[519, 377, 575, 401]
2026-08-10 13:43:37,930 INFO     29 [qwen-vl-text] coord item[12]: text=金额, bbox=[625, 377, 689, 400]
2026-08-10 13:43:37,930 INFO     29 [qwen-vl-text] coord item[13]: text=生产企业, bbox=[272, 416, 395, 439]
2026-08-10 13:43:37,930 INFO     29 [qwen-vl-text] coord item[14]: text=生产批号, bbox=[577, 416, 701, 439]
2026-08-10 13:43:37,930 INFO     29 [qwen-vl-text] coord item[15]: text=圣邦杰, bbox=[243, 480, 336, 503]
2026-08-10 13:43:37,930 INFO     29 [qwen-vl-text] coord item[16]: text=盐酸二甲双胍缓释片(山东司邦得, bbox=[245, 518, 701, 545]
2026-08-10 13:43:37,930 INFO     29 [qwen-vl-text] coord item[17]: text=制药有限公司), bbox=[245, 553, 443, 577]
2026-08-10 13:43:37,930 INFO     29 [qwen-vl-text] coord item[18]: text=0.5g*40T, bbox=[528, 558, 654, 581]
2026-08-10 13:43:37,930 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[245, 592, 304, 615]
2026-08-10 13:43:37,930 INFO     29 [qwen-vl-text] coord item[20]: text=4.8, bbox=[335, 592, 384, 611]
2026-08-10 13:43:37,930 INFO     29 [qwen-vl-text] coord item[21]: text=数量10, bbox=[412, 590, 502, 612]
2026-08-10 13:43:37,930 INFO     29 [qwen-vl-text] coord item[22]: text=合计48.00, bbox=[558, 595, 702, 621]
2026-08-10 13:43:37,930 INFO     29 [qwen-vl-text] coord item[23]: text=总页数：1.00, bbox=[245, 628, 429, 651]
2026-08-10 13:43:37,930 INFO     29 [qwen-vl-text] coord item[24]: text=总折扣：0.00, bbox=[514, 630, 700, 660]
2026-08-10 13:43:37,931 INFO     29 [qwen-vl-text] coord item[25]: text=合计：48.00, bbox=[276, 688, 444, 711]
2026-08-10 13:43:37,931 INFO     29 [qwen-vl-text] coord item[26]: text=付款：48.00, bbox=[484, 689, 651, 720]
2026-08-10 13:43:37,931 INFO     29 [qwen-vl-text] coord item[27]: text=找零：0.00, bbox=[292, 722, 443, 745]
2026-08-10 13:43:37,931 INFO     29 [qwen-vl-text] coord item[28]: text=*号代表含兴奋剂药品，请运动员慎, bbox=[247, 753, 692, 791]
2026-08-10 13:43:37,931 INFO     29 [qwen-vl-text] coord item[29]: text=用, bbox=[248, 785, 278, 805]
2026-08-10 13:43:37,931 INFO     29 [qwen-vl-text] coord item[30]: text=祝您健康！, bbox=[398, 808, 524, 837]
2026-08-10 13:43:37,931 INFO     29 [qwen-vl-text] coord item[31]: text=请您当日开取发票，如有其他, bbox=[311, 841, 687, 879]
2026-08-10 13:43:37,931 INFO     29 [qwen-vl-text] coord item[32]: text=原因请在15日内开取发票, bbox=[252, 873, 564, 905]
2026-08-10 13:43:37,933 INFO     29 [qwen-vl-text] page=6 — 33/33 coords, api_time=9.7s
2026-08-10 13:43:37,934 INFO     29 [qwen-vl-text] new_positions (33):
[[6, 208.25, 358.78499999999997, 100.079, 127.832], [6, 140.42, 302.26, 158.108, 179.974], [6, 328.44, 425.42499999999995, 155.585, 178.292], [6, 140.42, 192.78, 191.748, 212.773], [6, 140.42, 320.11, 227.07, 247.254], [6, 347.47999999999996, 425.42499999999995, 226.22899999999998, 243.89], [6, 141.60999999999999, 178.5, 284.258, 303.601], [6, 290.955, 324.275, 285.94, 305.283], [6, 383.18, 420.66499999999996, 283.417, 302.76], [6, 161.84, 198.73, 317.057, 336.4], [6, 226.695, 262.395, 317.89799999999997, 337.241], [6, 308.805, 342.125, 317.057, 337.241], [6, 371.875, 409.955, 317.057, 336.4], [6, 161.84, 235.02499999999998, 349.856, 369.199], [6, 343.315, 417.09499999999997, 349.856, 369.199], [6, 144.58499999999998, 199.92, 403.68, 423.02299999999997], [6, 145.775, 417.09499999999997, 435.638, 458.34499999999997], [6, 145.775, 263.585, 465.073, 485.257], [6, 314.15999999999997, 389.13, 469.27799999999996, 488.621], [6, 145.775, 180.88, 497.87199999999996, 517.215], [6, 199.325, 228.48, 497.87199999999996, 513.851], [6, 245.14, 298.69, 496.19, 514.692], [6, 332.01, 417.69, 500.395, 522.261], [6, 145.775, 255.255, 528.148, 547.491], [6, 305.83, 416.5, 529.8299999999999, 555.06], [6, 164.22, 264.18, 578.608, 597.951], [6, 287.97999999999996, 387.34499999999997, 579.449, 605.52], [6, 173.73999999999998, 263.585, 607.202, 626.545], [6, 146.965, 411.74, 633.273, 665.231], [6, 147.56, 165.41, 660.185, 677.005], [6, 236.81, 311.78, 679.528, 703.917], [6, 185.045, 408.765, 707.281, 739.2389999999999], [6, 149.94, 335.58, 734.193, 761.105]]
2026-08-10 13:43:37,935 INFO     29 [qwen-vl-text] ═══ DONE ═══ 33 positions, pages=1, time=12.3s
2026-08-10 13:43:37,935 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:43:37,937 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:43:37,937 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 13:43:37,937 INFO     29 [qwen-vl-text] positions(33): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:43:37,937 INFO     29 [qwen-vl-text] page grouping: [7], lines per page: [33]
2026-08-10 13:43:38,420 INFO     29 [qwen-vl-text] page=7, rect=595x841, img=(1653x2337), dpi=200
2026-08-10 13:43:38,421 INFO     29 [qwen-vl-text] LLM extraction start, text_len=241
2026-08-10 13:43:38,421 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:43:38,422 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 116, \"bbox_end\": 148, \"encounter_dates\": [\"2025-04-29\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "长春民康利药房\n票号：04311345628\n收银员：77\n会员名\n交易时间：2025-4-29\n12:28:12\n品名\n规格\n单位\n内码\n数量\n单价\n金额\n生产企业\n生产批号\n圣邦杰\n盐酸二甲双胍缓释片(山东司邦得\n制药有限公司)\n0.5g*40T\n单价\n4.8\n数量10\n合计48.00\n总页数：1.00\n总折扣：0.00\n合计：48.00\n付款：48.00\n找零：0.00\n*号代表含兴奋剂药品,请运动员慎\n用\n祝您健康!\n请您当日开取发票，如有其他\n原因请在15日内开取发票",
    "role": "user"
  }
]
2026-08-10 13:43:38,424 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:43:38.423+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 55, "failed": 0, "current": {"48817b4494c111f1bd9827cf206dfa2d": {"id": "48817b4494c111f1bd9827cf206dfa2d", "doc_id": "47f841b294c111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "WAYA-\u7cd6\u5c3f\u75c5-\u957f\u6625.pdf", "type": "pdf", "location": "WAYA-\u7cd6\u5c3f\u75c5-\u957f\u6625.pdf", "size": 28233765, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786369329126, "task_type": "dataflow", "root_trace_id": "3a85c9850cd6423785dc819c3129b342", "root_traceparent": "00-3a85c9850cd6423785dc819c3129b342-ef8a80a2724cffe2-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:43:40,688 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:43:40,688 INFO     29 [qwen-vl-text] LLM output (len=425):
{
  "encounter_date": "2025-04-29",
  "pharmacy": "长春民康利药房",
  "medications": [
    {
      "name": "圣邦杰 盐酸二甲双胍缓释片",
      "specification": "0.5g*40T",
      "dosage": null,
      "quantity": 10,
      "unit_price": 4.8,
      "total_price": 48.00,
      "frequency": null,
      "route": null,
      "manufacturer": "山东司邦得制药有限公司",
      "approval_number": null
    }
  ],
  "payment_total": 48.00,
  "payment_method": null
}
2026-08-10 13:43:40,688 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-04-29]
2026-08-10 13:43:40,706 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4660031, prompt_len=953
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["长春民康利药房", "票号：04311345628", "收银员：77", "会员名", "交易时间：2025-4-29", "12:28:12", "品名", "规格", "单位", "内码", "数量", "单价", "金额", "生产企业", "生产批号", "圣邦杰", "盐酸二甲双胍缓释片(山东司邦得", "制药有限公司)", "0.5g*40T", "单价", "4.8", "数量10", "合计48.00", "总页数：1.00", "总折扣：0.00", "合计：48.00", "付款：48.00", "找零：0.00", "*号代表含兴奋剂药品,请运动员慎", "用", "祝您健康!", "请您当日开取发票，如有其他", "原因请在15日内开取发票"]

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
2026-08-10 13:43:50,191 INFO     29 [qwen-vl-text] coord API raw response (len=1696):
[
	{"text": "长春民康利药房", "bbox": [396, 210, 573, 244]},
	{"text": "票号：04311345628", "bbox": [321, 266, 512, 290]},
	{"text": "收银员：77", "bbox": [540, 252, 656, 278]},
	{"text": "会员名", "bbox": [323, 298, 388, 317]},
	{"text": "交易时间：2025-4-29", "bbox": [326, 320, 538, 345]},
	{"text": "12:28:12", "bbox": [569, 309, 663, 330]},
	{"text": "品名", "bbox": [328, 373, 372, 391]},
	{"text": "规格", "bbox": [505, 365, 546, 384]},
	{"text": "单位", "bbox": [616, 355, 660, 374]},
	{"text": "内码", "bbox": [353, 401, 398, 419]},
	{"text": "数量", "bbox": [431, 398, 474, 416]},
	{"text": "单价", "bbox": [527, 391, 569, 410]},
	{"text": "金额", "bbox": [605, 385, 652, 404]},
	{"text": "生产企业", "bbox": [354, 427, 444, 445]},
	{"text": "生产批号", "bbox": [571, 413, 664, 434]},
	{"text": "圣邦杰", "bbox": [336, 473, 403, 491]},
	{"text": "盐酸二甲双胍缓释片(山东司邦得", "bbox": [338, 491, 671, 519]},
	{"text": "制药有限公司)", "bbox": [338, 525, 484, 547]},
	{"text": "0.5g*40T", "bbox": [544, 522, 640, 540]},
	{"text": "单价", "bbox": [341, 558, 384, 576]},
	{"text": "4.8", "bbox": [406, 556, 444, 573]},
	{"text": "数量10", "bbox": [463, 553, 528, 571]},
	{"text": "合计48.00", "bbox": [570, 550, 679, 569]},
	{"text": "总页数：1.00", "bbox": [342, 582, 478, 603]},
	{"text": "总折扣：0.00", "bbox": [539, 578, 680, 597]},
	{"text": "合计：48.00", "bbox": [366, 630, 492, 651]},
	{"text": "付款：48.00", "bbox": [520, 628, 649, 647]},
	{"text": "找零：0.00", "bbox": [378, 658, 493, 678]},
	{"text": "*号代表含兴奋剂药品,请运动员慎", "bbox": [345, 682, 687, 705]},
	{"text": "用", "bbox": [347, 710, 370, 726]},
	{"text": "祝您健康!", "bbox": [462, 728, 561, 747]},
	{"text": "请您当日开取发票，如有其他", "bbox": [397, 756, 692, 778]},
	{"text": "原因请在15日内开取发票", "bbox": [353, 785, 598, 806]}
]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=9.5s
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[0]: text=长春民康利药房, bbox=[396, 210, 573, 244]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[1]: text=票号：04311345628, bbox=[321, 266, 512, 290]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[2]: text=收银员：77, bbox=[540, 252, 656, 278]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[3]: text=会员名, bbox=[323, 298, 388, 317]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[4]: text=交易时间：2025-4-29, bbox=[326, 320, 538, 345]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[5]: text=12:28:12, bbox=[569, 309, 663, 330]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[6]: text=品名, bbox=[328, 373, 372, 391]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[7]: text=规格, bbox=[505, 365, 546, 384]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[8]: text=单位, bbox=[616, 355, 660, 374]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[9]: text=内码, bbox=[353, 401, 398, 419]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[10]: text=数量, bbox=[431, 398, 474, 416]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[11]: text=单价, bbox=[527, 391, 569, 410]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[12]: text=金额, bbox=[605, 385, 652, 404]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[13]: text=生产企业, bbox=[354, 427, 444, 445]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[14]: text=生产批号, bbox=[571, 413, 664, 434]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[15]: text=圣邦杰, bbox=[336, 473, 403, 491]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[16]: text=盐酸二甲双胍缓释片(山东司邦得, bbox=[338, 491, 671, 519]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[17]: text=制药有限公司), bbox=[338, 525, 484, 547]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[18]: text=0.5g*40T, bbox=[544, 522, 640, 540]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[341, 558, 384, 576]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[20]: text=4.8, bbox=[406, 556, 444, 573]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[21]: text=数量10, bbox=[463, 553, 528, 571]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[22]: text=合计48.00, bbox=[570, 550, 679, 569]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[23]: text=总页数：1.00, bbox=[342, 582, 478, 603]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[24]: text=总折扣：0.00, bbox=[539, 578, 680, 597]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[25]: text=合计：48.00, bbox=[366, 630, 492, 651]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[26]: text=付款：48.00, bbox=[520, 628, 649, 647]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[27]: text=找零：0.00, bbox=[378, 658, 493, 678]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[28]: text=*号代表含兴奋剂药品,请运动员慎, bbox=[345, 682, 687, 705]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[29]: text=用, bbox=[347, 710, 370, 726]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[30]: text=祝您健康!, bbox=[462, 728, 561, 747]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[31]: text=请您当日开取发票，如有其他, bbox=[397, 756, 692, 778]
2026-08-10 13:43:50,192 INFO     29 [qwen-vl-text] coord item[32]: text=原因请在15日内开取发票, bbox=[353, 785, 598, 806]
2026-08-10 13:43:50,193 INFO     29 [qwen-vl-text] page=7 — 33/33 coords, api_time=9.5s
2026-08-10 13:43:50,193 INFO     29 [qwen-vl-text] new_positions (33):
[[7, 235.61999999999998, 340.935, 176.60999999999999, 205.20399999999998], [7, 190.995, 304.64, 223.706, 243.89], [7, 321.3, 390.32, 211.932, 233.798], [7, 192.185, 230.85999999999999, 250.618, 266.597], [7, 193.97, 320.11, 269.12, 290.145], [7, 338.555, 394.48499999999996, 259.86899999999997, 277.53], [7, 195.16, 221.34, 313.693, 328.83099999999996], [7, 300.47499999999997, 324.87, 306.965, 322.94399999999996], [7, 366.52, 392.7, 298.555, 314.534], [7, 210.035, 236.81, 337.241, 352.37899999999996], [7, 256.445, 282.03, 334.71799999999996, 349.856], [7, 313.565, 338.555, 328.83099999999996, 344.81], [7, 359.97499999999997, 387.94, 323.78499999999997, 339.764], [7, 210.63, 264.18, 359.10699999999997, 374.245], [7, 339.745, 395.08, 347.33299999999997, 364.99399999999997], [7, 199.92, 239.785, 397.793, 412.931], [7, 201.10999999999999, 399.245, 412.931, 436.479], [7, 201.10999999999999, 287.97999999999996, 441.525, 460.027], [7, 323.68, 380.79999999999995, 439.002, 454.14], [7, 202.89499999999998, 228.48, 469.27799999999996, 484.416], [7, 241.57, 264.18, 467.596, 481.893], [7, 275.485, 314.15999999999997, 465.073, 480.21099999999996], [7, 339.15, 404.005, 462.55, 478.529], [7, 203.48999999999998, 284.40999999999997, 489.462, 507.123], [7, 320.705, 404.59999999999997, 486.09799999999996, 502.077], [7, 217.76999999999998, 292.74, 529.8299999999999, 547.491], [7, 309.4, 386.155, 528.148, 544.127], [7, 224.91, 293.335, 553.3779999999999, 570.198], [7, 205.27499999999998, 408.765, 573.562, 592.905], [7, 206.465, 220.14999999999998, 597.11, 610.566], [7, 274.89, 333.79499999999996, 612.2479999999999, 628.227], [7, 236.215, 411.74, 635.7959999999999, 654.298], [7, 210.035, 355.81, 660.185, 677.846]]
2026-08-10 13:43:50,193 INFO     29 [qwen-vl-text] ═══ DONE ═══ 33 positions, pages=1, time=12.3s
2026-08-10 13:43:50,200 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 13:43:50,200 INFO     29 [Trace] task=48817b44 | doc=WAYA-糖尿病-长春.pdf | Extractor:Medication | outputs={"chunks": "2 items, types={'MedicationRecord': 2}", "html": "", "json": "149 items", "markdown": "", "text": "", "name": "WAYA-糖尿病-长春.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 4, \"chunks_Medication\": 2}"}
2026-08-10 13:43:50,200 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 13:43:50,206 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:43:50,206 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:43:51,033 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:43:51,041 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 13:43:51,041 INFO     29 [Trace] task=48817b44 | doc=WAYA-糖尿病-长春.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "149 items", "markdown": "", "text": "", "name": "WAYA-糖尿病-长春.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 4, \"chunks_Medication\": 2}"}
2026-08-10 13:43:51,042 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 13:43:51,047 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:43:51,047 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:43:51,561 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:43:51,570 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 13:43:51,570 INFO     29 [Trace] task=48817b44 | doc=WAYA-糖尿病-长春.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "149 items", "markdown": "", "text": "", "name": "WAYA-糖尿病-长春.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 4, \"chunks_Medication\": 2}"}
2026-08-10 13:43:51,570 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 13:43:51,576 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:43:51,576 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:43:52,077 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:43:52,083 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 13:43:52,083 INFO     29 [Trace] task=48817b44 | doc=WAYA-糖尿病-长春.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "149 items", "markdown": "", "text": "", "name": "WAYA-糖尿病-长春.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 4, \"chunks_Medication\": 2}"}
2026-08-10 13:43:52,083 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 13:43:52,087 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:43:52,087 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:43:53,188 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:43:53,196 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 13:43:53,196 INFO     29 [Trace] task=48817b44 | doc=WAYA-糖尿病-长春.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "149 items", "markdown": "", "text": "", "name": "WAYA-糖尿病-长春.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 4, \"chunks_Medication\": 2}"}
2026-08-10 13:43:53,196 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 13:43:53,202 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:43:53,202 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:43:53,715 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:43:53,725 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 13:43:53,726 INFO     29 [Trace] task=48817b44 | doc=WAYA-糖尿病-长春.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "149 items", "markdown": "", "text": "", "name": "WAYA-糖尿病-长春.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_LabExam\": 4, \"chunks_Medication\": 2}"}
2026-08-10 13:43:53,726 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 13:43:53,727 INFO     29 [ChunkMerger] Merged 8 chunks from 9 sources: {'Extractor:LabExam': 4, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 2, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 6 noise chunks)
2026-08-10 13:43:53,742 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 13:43:53,742 INFO     29 [Trace] task=48817b44 | doc=WAYA-糖尿病-长春.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "8 items, types={'LabReport': 4, 'OutpatientRecord': 2, 'MedicationRecord': 2}", "name": "WAYA-糖尿病-长春.pdf"}
2026-08-10 13:43:53,742 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 13:43:53,785 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786369331199, 'update_date': datetime.datetime(2026, 8, 10, 13, 42, 11), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1047720, 'status': '1'}
2026-08-10 13:43:54,018 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   血糖  GLU  10.46  mmol/L  3.89-6.11  True   
---
   糖化血红蛋白  HbA1c  9.8  %  4-6  True   
---
   葡萄糖测定(空腹己糖激酶法)  GLU  11.50  mmol/L  3.9--6.1  True   
---
   糖化血红蛋白（高效液相色谱法）  0101409  8.40  %  4--6  True   
---
吉林省人民醫院
门（急）诊病历
姓名：
性别：男
年龄：
时间：2024年3月7日
门诊号：2403070
婚姻：
职业：其他
就诊类型：○初诊○复诊○急诊
过敏史：否认药物及食品过敏史
科室：内分泌代谢病二科门诊
住址：
主诉：糖尿病开药
简要病史：糖尿病，要求开二甲双胍。
既往史和其他病史：
体格检查（选填项目）：体温：
；脉搏：次/分；呼
吸：次/分；血压/mmHg。
专科检查(必要项目)：
辅助检查及结果：
初步诊断：2型糖尿病
诊疗意见：口服,每天二次,次/次,盐酸二甲双胍缓释片,
每天二次, 1.00g/次
签名：蒋立军
时间：2024年03月07日13时04分39
秒
(以上病历交予患者,是否为本次诊疗最终病历无需补充:○是○否)
---
黑龙江博尚医院
门诊病历
姓名：
门诊号：2403
科室：综合内科门诊
性别：男
年龄：43岁
就诊时间：2024-02-21 10:49
主诉：
多饮，多尿，多食，口干，口渴半年，加重一周。
现病史：
既往史：
既往否认重要病史。
药物过敏史：
无。
辅助检查：
检验结果-2024-02-21 09:51- 空腹血糖16.40mmol/L↑
检验结果-2024-02-21 09:44- 糖化血红蛋白8.58%↑
初步诊断：
2型糖尿病
处理措施：
每天2次，每次1.0g
医师签名：李月菊
---
长春民康利药房
票号：04311228929
收银员：77
会员
交易时间：2025-1-22
18:21:22
品名
规格
单位
内码
数量
单价
金额
生产企业
生产批号
圣邦杰
盐酸二甲双胍缓释片(山东司邦得
制药有限公司)
0.5g*40T
单价
4.8
数量10
合计48.00
总页数：1.00
总折扣：0.00
合计：48.00
付款：48.00
找零：0.00
*号代表含兴奋剂药品，请运动员慎
用
祝您健康！
请您当日开取发票，如有其他
原因请在15日内开取发票
---
长春民康利药房
票号：04311345628
收银员：77
会员名
交易时间：2025-4-29
12:28:12
品名
规格
单位
内码
数量
单价
金额
生产企业
生产批号
圣邦杰
盐酸二甲双胍缓释片(山东司邦得
制药有限公司)
0.5g*40T
单价
4.8
数量10
合计48.00
总页数：1.00
总折扣：0.00
合计：48.00
付款：48.00
找零：0.00
*号代表含兴奋剂药品,请运动员慎
用
祝您健康!
请您当日开取发票，如有其他
原因请在15日内开取发票
2026-08-10 13:43:54,386 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 13:43:54,386 INFO     29 [Trace] task=48817b44 | doc=WAYA-糖尿病-长春.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "8 items, types={'LabReport': 4, 'OutpatientRecord': 2, 'MedicationRecord': 2}", "name": "WAYA-糖尿病-长春.pdf", "embedding_token_consumption": 1005}
2026-08-10 13:43:54,386 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 13:43:54,664 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 13:43:54,664 INFO     29 [Trace] task=48817b44 | doc=WAYA-糖尿病-长春.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":8,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 13:43:54,668 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(3, 43, 60, 140, 151) row[-1]=(3, 43, 60, 140, 151)
2026-08-10 13:43:54,668 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(4, 140, 182, 405, 413) row[-1]=(4, 140, 182, 405, 413)
2026-08-10 13:43:54,668 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(5, 101, 247, 172, 185) row[-1]=(5, 101, 247, 172, 185)
2026-08-10 13:43:54,668 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(6, 100, 248, 168, 179) row[-1]=(6, 100, 248, 168, 179)
2026-08-10 13:43:54,668 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:43:54,668 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:43:54,668 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:43:54,669 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:43:54,672 INFO     29 set_progress(48817b4494c111f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 13:43:54 [DOC Engine]:
Start to index...
2026-08-10 13:43:54,690 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.013s]
2026-08-10 13:43:54,695 INFO     29 set_progress(48817b4494c111f1bd9827cf206dfa2d), progress: 0.8125, progress_msg: 
2026-08-10 13:43:54,713 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.011s]
2026-08-10 13:43:54,721 INFO     29 set_progress(48817b4494c111f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 13:43:54 Indexing done (0.05s). Task done (98.99s)
2026-08-10 13:43:54,725 INFO     29 [Done], chunks(8), token(1005), elapsed:98.99
2026-08-10 13:43:55,491 INFO     29 handle_task done for task {"id": "48817b4494c111f1bd9827cf206dfa2d", "doc_id": "47f841b294c111f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "WAYA-\u7cd6\u5c3f\u75c5-\u957f\u6625.pdf", "type": "pdf", "location": "WAYA-\u7cd6\u5c3f\u75c5-\u957f\u6625.pdf", "size": 28233765, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786369329126, "task_type": "dataflow", "root_trace_id": "3a85c9850cd6423785dc819c3129b342", "root_traceparent": "00-3a85c9850cd6423785dc819c3129b342-ef8a80a2724cffe2-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
