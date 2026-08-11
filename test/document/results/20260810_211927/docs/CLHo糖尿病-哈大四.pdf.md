# 基准结果：CLHo糖尿病-哈大四.pdf

## 基本信息

- 文件：`CLHo糖尿病-哈大四.pdf`
- 大小：1000.5 KB
- PDF 总页数：5
- doc_id：`8c88a43294be11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T21:22:33  完成时间：2026-08-10T21:24:11  耗时：97.9s
- progress_msg：`13:24:07 Indexing done (0.04s). Task done (87.01s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 01a8c669 | 1 | 1-1 | 肇东市维康大药房 有限公司销售单 流水号9999000234562564544  |
| 2 | 5b961218 | 1 | 2-2 | 肇东市永馨福园综合门诊 门诊号：MZ9925103 科室：门诊 接诊日期：202 |
| 3 | 78733dae | 1 | 5-5 | 哈尔滨泽福大药房销售单 NO.98222250454552 2024-12-07 |
| 4 | 840ac06a | 1 | 4-4 | <table><tr><td>葡萄糖</td><td>GLU</td><td>8 |
| 5 | 300d65fe | 1 | 3-3 | <table><tr><td>葡萄糖</td><td>GLU</td><td>1 |
| 6 | a5701b84 | 1 | 4-4 | <table><tr><td>维生素C</td><td>None</td><td |
| 7 | adbcdbc3 | 1 | 4-4 | <table><tr><td>糖化血红蛋白</td><td>None</td>< |

- chunks 总数：7
- 各 chunk 页数合计（含跨页重复）：7
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
| MedicationRecord | 购药 | 2 | 2 | 2 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 0 | 1 | 0 | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 4 | 0 | 4 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"MedicationRecord": 2, "OutpatientRecord": 1, "LabReport": 4}`
- ChunkMerger：`{"found": true, "merged": 7, "sources": 9, "stats": {"Extractor:LabExam": 4, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 2, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1, "Extractor:Progress": 1}, "filtered_noise": 6}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 13:24:06,298 INFO     29 [ChunkMerger] Merged 7 chunks from 9 sources: {'Extractor:LabExam': 4, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 2, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 13:22:35,567 INFO     29 handle_task begin for task {"id": "8cbb752494be11f1bd9827cf206dfa2d", "doc_id": "8c88a43294be11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "CLHo\u7cd6\u5c3f\u75c5-\u54c8\u5927\u56db.pdf", "type": "pdf", "location": "CLHo\u7cd6\u5c3f\u75c5-\u54c8\u5927\u56db.pdf", "size": 1024502, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368155101, "task_type": "dataflow", "root_trace_id": "d96187892a0044bdbc8ca087b3270949", "root_traceparent": "00-d96187892a0044bdbc8ca087b3270949-fa185c031b5a1abd-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 13:22:35,773 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 13:22:35,880 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 13:22:35,888 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:22:35,889 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 13:22:35,889 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 13:22:35,893 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 13:22:35,893 INFO     29 ============================================================
2026-08-10 13:22:35,893 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 13:22:35,893 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 13:22:35,893 INFO     29 ============================================================
2026-08-10 13:22:35,893 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 13:22:35,893 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 13:22:35,895 INFO     29 No torch found.
2026-08-10 13:22:36,246 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=5
2026-08-10 13:22:36,451 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=890976, prompt_len=764
2026-08-10 13:22:38,140 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:22:38,141 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 13:22:38,154 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=890976, prompt_len=401
2026-08-10 13:22:39,850 INFO     29 [qwen-vl-parser] text API response (len=233):
["肇东市维康大药房", "有限公司销售单", "流水号9999000234562564544", "日期2024-09-04 09:27:13", "会员: 积分0.0000", "180245 盐酸二甲双胍片", "规格0.25g*1201 批号24020", "效期2026-01 产地.河北天成", "数量5盒 单价 ￥7.00元", "合计金额: ￥35.00元", "付款方式: 现金01", "健康热线:", "药品为特殊商品,一经售出不", "换"]
2026-08-10 13:22:39,851 INFO     29 [qwen-vl-parser] page=1 text: 14 lines (bbox 0-13)
2026-08-10 13:22:39,851 INFO     29 [qwen-vl-parser] page=1 text: 14 sections
2026-08-10 13:22:40,043 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=781255, prompt_len=764
2026-08-10 13:22:41,655 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:22:41,656 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 13:22:41,665 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=781255, prompt_len=401
2026-08-10 13:22:43,760 INFO     29 [qwen-vl-parser] text API response (len=331):
["肇东市永馨福园综合门诊", "门诊号：MZ9925103", "科室：门诊 接诊日期：2024-09", "姓名：", "病区：/", "接诊医师：/", "性别：女", "年龄：50岁", "住址：/", "临床诊断：2型糖尿病", "主诉：口干渴、出虚汗伴眩晕7日", "现病史：自述确诊2型糖尿病8年余，口干渴、出虚汗伴眩晕7日", "既往史：同现病史", "过敏史：", "查体：体温36.4℃ 血压130/90mmHg (-)", "辅助检查：已回报", "处理意见：", "1、盐酸二甲双胍片 0.5g/3次/日餐前口服；", "2、监测血糖，不适门诊随访；", "打印日期：2024-01-09", "医生签字", "主治医师", "胡维波"]
2026-08-10 13:22:43,761 INFO     29 [qwen-vl-parser] page=2 text: 23 lines (bbox 14-36)
2026-08-10 13:22:43,761 INFO     29 [qwen-vl-parser] page=2 text: 23 sections
2026-08-10 13:22:44,085 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1269819, prompt_len=764
2026-08-10 13:22:46,112 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:22:46.111+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 47, "failed": 0, "current": {"8cbb752494be11f1bd9827cf206dfa2d": {"id": "8cbb752494be11f1bd9827cf206dfa2d", "doc_id": "8c88a43294be11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "CLHo\u7cd6\u5c3f\u75c5-\u54c8\u5927\u56db.pdf", "type": "pdf", "location": "CLHo\u7cd6\u5c3f\u75c5-\u54c8\u5927\u56db.pdf", "size": 1024502, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368155101, "task_type": "dataflow", "root_trace_id": "d96187892a0044bdbc8ca087b3270949", "root_traceparent": "00-d96187892a0044bdbc8ca087b3270949-fa185c031b5a1abd-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:22:47,788 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2024-01-09"
}
```
2026-08-10 13:22:47,789 INFO     29 [qwen-vl-parser] page=3 classify=table report_date=2024-01-09
2026-08-10 13:22:47,812 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1269819, prompt_len=756
2026-08-10 13:22:49,238 INFO     29 [qwen-vl-parser] table API response (len=204):
\begin{tabular}{ccccccccc}
\hline
NO. & 项目名称 & 英文 & 结果 & 单位 & 参考值 & & & \\
\hline
1 & 葡萄糖 & GLU & 13.6 & mmol/L & 4.11-5.90 & & & \\
2 & 糖化血红蛋白 & HbA1c & 9.9 & \% & 3.90-6.11 & & & \\
\hline
\end{tabular}
2026-08-10 13:22:49,240 INFO     29 [qwen-vl-parser] page=3 table: 9 LaTeX lines (bbox 37-45)
2026-08-10 13:22:49,241 INFO     29 [qwen-vl-parser] page=3 table: 9 sections
2026-08-10 13:22:49,407 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=661336, prompt_len=764
2026-08-10 13:22:51,931 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-04-23"
}
```
2026-08-10 13:22:51,932 INFO     29 [qwen-vl-parser] page=4 classify=table report_date=2025-04-23
2026-08-10 13:22:51,946 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=661336, prompt_len=756
2026-08-10 13:22:57,682 INFO     29 [qwen-vl-parser] table API response (len=917):
\begin{tabular}{l c c c c}
\hline
项目名称 & 结果 & 单位 & 参考范围 & 提示 \\
\hline
维生素C & + & & & \\
透明管型 & 0 & /LP & 0 & \\
胆红素(BIL) & & umol/L & 阴性 & \\
结晶检查(X'TAL) & & & & \\
尿潜血(BLD) & & Ery/ul & 阴性 & \\
尿脓细胞 & & & & \\
其他 & 未见 & & & \\
白细胞镜检 & 2-4 & /HP & 0-5 & \\
颗粒管型 & 0 & & 0 & \\
颜色(Colour) & 黄色 & & 黄色 & \\
尿葡萄糖(GLU) & +4 & mmol/ul & 阴性 & \\
酮体(KET) & & mmol/L & 阴性 & \\
比重(SG) & 1.020 & & 1.010-1.030 & \\
酸碱度(PH) & 5.0 & & 4.5-8.0 & \\
尿蛋白质(PRO) & & g/L & 阴性 & \\
尿胆原(UR0) & & umol/L & & \\
亚硝酸盐(NIT) & & & 阴性 & \\
上皮细胞(Epi.cells) & 1-3 & 个/ul & 0-5 & \\
红细胞镜检 & 0 & /ul & 0-3 & \\
白细胞(尿液) & & 1euko/ul & 阴性 & \\
\hline
\end{tabular}

\begin{tabular}{l c c c c}
\hline
项目名称 & 结果 & 单位 & 参考范围 & 提示 \\
\hline
葡萄糖(GLU) & 8.13 & mmol/L & 3.90-6.11 & $\uparrow$ \\
\hline
\end{tabular}

\begin{tabular}{l c c c c}
\hline
项目名称 & 结果 & 单位 & 参考范围 & 提示 \\
\hline
糖化血红蛋白 & 9.8 & \% & 4.2-5.9 & $\uparrow$ \\
\hline
\end{tabular}
2026-08-10 13:22:57,685 INFO     29 [qwen-vl-parser] page=4 table: 43 LaTeX lines (bbox 46-88)
2026-08-10 13:22:57,685 INFO     29 [qwen-vl-parser] page=4 table: 43 sections
2026-08-10 13:22:57,884 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=721220, prompt_len=764
2026-08-10 13:22:59,640 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 13:22:59,640 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 13:22:59,653 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=721220, prompt_len=401
2026-08-10 13:23:01,255 INFO     29 [qwen-vl-parser] text API response (len=211):
["哈尔滨泽福大药房销售单", "NO.98222250454552", "2024-12-07 15:14:48", "会员 卡号：999918", "215114 盐酸二甲双胍片", "0.25gx120片/盒 2406015", "2026/05/30 河北天成药业", "10盒x8.00=80.00", "销售员 韩晶晶 Hlt:03", "金额小计：￥80.00元", "付款方式：现款销售", "健康热线"]
2026-08-10 13:23:01,256 INFO     29 [qwen-vl-parser] page=5 text: 12 lines (bbox 89-100)
2026-08-10 13:23:01,256 INFO     29 [qwen-vl-parser] page=5 text: 12 sections
2026-08-10 13:23:01,256 INFO     29 [qwen-vl-parser] parse_pdf done: 101 sections from 5 pages.
2026-08-10 13:23:01,267 INFO     29 Close text detector.
2026-08-10 13:23:01,722 INFO     29 Close text recognizer.
2026-08-10 13:23:02,125 INFO     29 Close recognizer.
2026-08-10 13:23:02,571 INFO     29 Close recognizer.
2026-08-10 13:23:02,987 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 13:23:02,988 INFO     29 [Trace] task=8cbb7524 | doc=CLHo糖尿病-哈大四.pdf | Parser:MedLink | outputs={"html": "", "json": "101 items", "markdown": "", "text": "", "name": "CLHo糖尿病-哈大四.pdf", "output_format": "json"}
2026-08-10 13:23:02,988 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 13:23:03,011 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:23:03,011 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 肇东市维康大药房\n[BBOX-1] 有限公司销售单\n[BBOX-2] 流水号9999000234562564544\n[BBOX-3] 日期2024-09-04 09:27:13\n[BBOX-4] 会员: 积分0.0000\n[BBOX-5] 180245 盐酸二甲双胍片\n[BBOX-6] 规格0.25g*1201 批号24020\n[BBOX-7] 效期2026-01 产地.河北天成\n[BBOX-8] 数量5盒 单价 ￥7.00元\n[BBOX-9] 合计金额: ￥35.00元\n[BBOX-10] 付款方式: 现金01\n[BBOX-11] 健康热线:\n[BBOX-12] 药品为特殊商品,一经售出不\n[BBOX-13] 换\n[BBOX-14] 肇东市永馨福园综合门诊\n[BBOX-15] 门诊号：MZ9925103\n[BBOX-16] 科室：门诊 接诊日期：2024-09\n[BBOX-17] 姓名：\n[BBOX-18] 病区：/\n[BBOX-19] 接诊医师：/\n[BBOX-20] 性别：女\n[BBOX-21] 年龄：50岁\n[BBOX-22] 住址：/\n[BBOX-23] 临床诊断：2型糖尿病\n[BBOX-24] 主诉：口干渴、出虚汗伴眩晕7日\n[BBOX-25] 现病史：自述确诊2型糖尿病8年余，口干渴、出虚汗伴眩晕7日\n[BBOX-26] 既往史：同现病史\n[BBOX-27] 过敏史：\n[BBOX-28] 查体：体温36.4℃ 血压130/90mmHg (-)\n[BBOX-29] 辅助检查：已回报\n[BBOX-30] 处理意见：\n[BBOX-31] 1、盐酸二甲双胍片 0.5g/3次/日餐前口服；\n[BBOX-32] 2、监测血糖，不适门诊随访；\n[BBOX-33] 打印日期：2024-01-09\n[BBOX-34] 医生签字\n[BBOX-35] 主治医师\n[BBOX-36] 胡维波\n[BBOX-37] \\begin{tabular}{ccccccccc}\n[BBOX-38] 报告时间: 2024-01-09\n[BBOX-39] \\hline\n[BBOX-40] NO. & 项目名称 & 英文 & 结果 & 单位 & 参考值 & & & \\\\\n[BBOX-41] \\hline\n[BBOX-42] 1 & 葡萄糖 & GLU & 13.6 & mmol/L & 4.11-5.90 & & & \\\\\n[BBOX-43] 2 & 糖化血红蛋白 & HbA1c & 9.9 & \\% & 3.90-6.11 & & & \\\\\n[BBOX-44] \\hline\n[BBOX-45] \\end{tabular}\n[BBOX-46] \\begin{tabular}{l c c c c}\n[BBOX-47] 报告时间: 2025-04-23\n[BBOX-48] \\hline\n[BBOX-49] 项目名称 & 结果 & 单位 & 参考范围 & 提示 \\\\\n[BBOX-50] \\hline\n[BBOX-51] 维生素C & + & & & \\\\\n[BBOX-52] 透明管型 & 0 & /LP & 0 & \\\\\n[BBOX-53] 胆红素(BIL) & & umol/L & 阴性 & \\\\\n[BBOX-54] 结晶检查(X'TAL) & & & & \\\\\n[BBOX-55] 尿潜血(BLD) & & Ery/ul & 阴性 & \\\\\n[BBOX-56] 尿脓细胞 & & & & \\\\\n[BBOX-57] 其他 & 未见 & & & \\\\\n[BBOX-58] 白细胞镜检 & 2-4 & /HP & 0-5 & \\\\\n[BBOX-59] 颗粒管型 & 0 & & 0 & \\\\\n[BBOX-60] 颜色(Colour) & 黄色 & & 黄色 & \\\\\n[BBOX-61] 尿葡萄糖(GLU) & +4 & mmol/ul & 阴性 & \\\\\n[BBOX-62] 酮体(KET) & & mmol/L & 阴性 & \\\\\n[BBOX-63] 比重(SG) & 1.020 & & 1.010-1.030 & \\\\\n[BBOX-64] 酸碱度(PH) & 5.0 & & 4.5-8.0 & \\\\\n[BBOX-65] 尿蛋白质(PRO) & & g/L & 阴性 & \\\\\n[BBOX-66] 尿胆原(UR0) & & umol/L & & \\\\\n[BBOX-67] 亚硝酸盐(NIT) & & & 阴性 & \\\\\n[BBOX-68] 上皮细胞(Epi.cells) & 1-3 & 个/ul & 0-5 & \\\\\n[BBOX-69] 红细胞镜检 & 0 & /ul & 0-3 & \\\\\n[BBOX-70] 白细胞(尿液) & & 1euko/ul & 阴性 & \\\\\n[BBOX-71] \\hline\n[BBOX-72] \\end{tabular}\n[BBOX-73] \\begin{tabular}{l c c c c}\n[BBOX-74] 报告时间: 2025-04-23\n[BBOX-75] \\hline\n[BBOX-76] 项目名称 & 结果 & 单位 & 参考范围 & 提示 \\\\\n[BBOX-77] \\hline\n[BBOX-78] 葡萄糖(GLU) & 8.13 & mmol/L & 3.90-6.11 & $\\uparrow$ \\\\\n[BBOX-79] \\hline\n[BBOX-80] \\end{tabular}\n[BBOX-81] \\begin{tabular}{l c c c c}\n[BBOX-82] 报告时间: 2025-04-23\n[BBOX-83] \\hline\n[BBOX-84] 项目名称 & 结果 & 单位 & 参考范围 & 提示 \\\\\n[BBOX-85] \\hline\n[BBOX-86] 糖化血红蛋白 & 9.8 & \\% & 4.2-5.9 & $\\uparrow$ \\\\\n[BBOX-87] \\hline\n[BBOX-88] \\end{tabular}\n[BBOX-89] 哈尔滨泽福大药房销售单\n[BBOX-90] NO.98222250454552\n[BBOX-91] 2024-12-07 15:14:48\n[BBOX-92] 会员 卡号：999918\n[BBOX-93] 215114 盐酸二甲双胍片\n[BBOX-94] 0.25gx120片/盒 2406015\n[BBOX-95] 2026/05/30 河北天成药业\n[BBOX-96] 10盒x8.00=80.00\n[BBOX-97] 销售员 韩晶晶 Hlt:03\n[BBOX-98] 金额小计：￥80.00元\n[BBOX-99] 付款方式：现款销售\n[BBOX-100] 健康热线"
  }
]
2026-08-10 13:23:08,872 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:23:08,969 INFO     29 [SmartSplitter] SmartSplitter done: 7 chunks from 7 LLM segments (all bbox_id). Types: {'MedicationRecord': 2, 'OutpatientRecord': 1, 'LabReport': 4}
2026-08-10 13:23:08,991 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 13:23:08,992 INFO     29 [Trace] task=8cbb7524 | doc=CLHo糖尿病-哈大四.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "101 items", "markdown": "", "text": "", "name": "CLHo糖尿病-哈大四.pdf", "output_format": "chunks", "chunks": "7 items, types={'MedicationRecord': 2, 'OutpatientRecord': 1, 'LabReport': 4}"}
2026-08-10 13:23:08,992 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 13:23:08,993 INFO     29 [ChunkRouter] Routed 7 chunks into 3 groups: {'chunks_Medication': 2, 'chunks_Clinical': 1, 'chunks_LabExam': 4}
2026-08-10 13:23:09,006 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 13:23:09,006 INFO     29 [Trace] task=8cbb7524 | doc=CLHo糖尿病-哈大四.pdf | ChunkRouter:Router | outputs={"html": "", "json": "101 items", "markdown": "", "text": "", "name": "CLHo糖尿病-哈大四.pdf", "output_format": "chunks", "chunks": "7 items, types={'MedicationRecord': 2, 'OutpatientRecord': 1, 'LabReport': 4}", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Medication\": 2, \"chunks_Clinical\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 13:23:09,006 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 13:23:09,012 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:23:09,012 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:23:09,013 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[2]
2026-08-10 13:23:09,013 INFO     29 [qwen-vl-table] positions ： [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:23:09,258 INFO     29 [qwen-vl-table] page=2, rect=810x1440, img=(2250x4000)
2026-08-10 13:23:09,258 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:23:09,258 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 37, \"bbox_end\": 45, \"encounter_dates\": [\"2024-01-09\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2024-01-09\n\\hline\nNO. & 项目名称 & 英文 & 结果 & 单位 & 参考值 & & & \\\\\n\\hline\n1 & 葡萄糖 & GLU & 13.6 & mmol/L & 4.11-5.90 & & & \\\\\n2 & 糖化血红蛋白 & HbA1c & 9.9 & \\% & 3.90-6.11 & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:23:11,010 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:23:11,010 INFO     29 [qwen-vl-table] page=2 LLM output (len=385):
{
  "report_date": "2024-01-09",
  "items": [
    {
      "name": "葡萄糖",
      "item_code": "GLU",
      "value": "13.6",
      "unit": "mmol/L",
      "reference_range": "4.11-5.90",
      "abnormal": true
    },
    {
      "name": "糖化血红蛋白",
      "item_code": "HbA1c",
      "value": "9.9",
      "unit": "%",
      "reference_range": "3.90-6.11",
      "abnormal": true
    }
  ]
}
2026-08-10 13:23:11,010 INFO     29 [qwen-vl-table] coord grouping: {2: 2}
2026-08-10 13:23:11,017 INFO     29 [qwen-vl-table] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1699899, prompt_len=517
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
葡萄糖、糖化血红蛋白

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
2026-08-10 13:23:14,379 INFO     29 [qwen-vl-table] coord API raw response (len=113):
```json
[
	{"text": "葡萄糖", "bbox": [610, 168, 635, 210]},
	{"text": "糖化血红蛋白", "bbox": [552, 167, 578, 252]}
]
```
2026-08-10 13:23:14,379 INFO     29 [qwen-vl-table] coord API: raw_items=2, valid_items=2, elapsed=3.4s
2026-08-10 13:23:14,380 INFO     29 [qwen-vl-table] coord item[0]: text=葡萄糖, bbox=[610, 168, 635, 210]
2026-08-10 13:23:14,380 INFO     29 [qwen-vl-table] coord item[1]: text=糖化血红蛋白, bbox=[552, 167, 578, 252]
2026-08-10 13:23:14,381 INFO     29 [qwen-vl-table] page=2 coord: matched 2/2, time=3.4s
2026-08-10 13:23:14,381 INFO     29 [qwen-vl-table] new_positions (2):
[[3, 494.1, 514.35, 241.92, 302.4], [3, 447.12, 468.18, 240.48, 362.88]]
2026-08-10 13:23:14,381 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=2, matched=2, pages=1, time=5.4s
2026-08-10 13:23:14,384 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:23:14,386 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:23:14,386 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[3]
2026-08-10 13:23:14,386 INFO     29 [qwen-vl-table] positions ： [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:23:14,557 INFO     29 [qwen-vl-table] page=3, rect=840x1120, img=(2334x3113)
2026-08-10 13:23:14,558 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:23:14,558 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 46, \"bbox_end\": 72, \"encounter_dates\": [\"2025-04-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{l c c c c}\n报告时间: 2025-04-23\n\\hline\n项目名称 & 结果 & 单位 & 参考范围 & 提示 \\\\\n\\hline\n维生素C & + & & & \\\\\n透明管型 & 0 & /LP & 0 & \\\\\n胆红素(BIL) & & umol/L & 阴性 & \\\\\n结晶检查(X'TAL) & & & & \\\\\n尿潜血(BLD) & & Ery/ul & 阴性 & \\\\\n尿脓细胞 & & & & \\\\\n其他 & 未见 & & & \\\\\n白细胞镜检 & 2-4 & /HP & 0-5 & \\\\\n颗粒管型 & 0 & & 0 & \\\\\n颜色(Colour) & 黄色 & & 黄色 & \\\\\n尿葡萄糖(GLU) & +4 & mmol/ul & 阴性 & \\\\\n酮体(KET) & & mmol/L & 阴性 & \\\\\n比重(SG) & 1.020 & & 1.010-1.030 & \\\\\n酸碱度(PH) & 5.0 & & 4.5-8.0 & \\\\\n尿蛋白质(PRO) & & g/L & 阴性 & \\\\\n尿胆原(UR0) & & umol/L & & \\\\\n亚硝酸盐(NIT) & & & 阴性 & \\\\\n上皮细胞(Epi.cells) & 1-3 & 个/ul & 0-5 & \\\\\n红细胞镜检 & 0 & /ul & 0-3 & \\\\\n白细胞(尿液) & & 1euko/ul & 阴性 & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:23:17,577 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:23:17.573+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 47, "failed": 0, "current": {"8cbb752494be11f1bd9827cf206dfa2d": {"id": "8cbb752494be11f1bd9827cf206dfa2d", "doc_id": "8c88a43294be11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "CLHo\u7cd6\u5c3f\u75c5-\u54c8\u5927\u56db.pdf", "type": "pdf", "location": "CLHo\u7cd6\u5c3f\u75c5-\u54c8\u5927\u56db.pdf", "size": 1024502, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368155101, "task_type": "dataflow", "root_trace_id": "d96187892a0044bdbc8ca087b3270949", "root_traceparent": "00-d96187892a0044bdbc8ca087b3270949-fa185c031b5a1abd-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:23:23,638 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:23:23,638 INFO     29 [qwen-vl-table] page=3 LLM output (len=3233):
{
  "report_date": "2025-04-23",
  "items": [
    {
      "name": "维生素C",
      "item_code": null,
      "value": "+",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "透明管型",
      "item_code": null,
      "value": "0",
      "unit": "/LP",
      "reference_range": "0",
      "abnormal": false
    },
    {
      "name": "胆红素",
      "item_code": "BIL",
      "value": null,
      "unit": "umol/L",
      "reference_range": "阴性",
      "abnormal": false
    },
    {
      "name": "结晶检查",
      "item_code": "X'TAL",
      "value": null,
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "尿潜血",
      "item_code": "BLD",
      "value": null,
      "unit": "Ery/ul",
      "reference_range": "阴性",
      "abnormal": false
    },
    {
      "name": "尿脓细胞",
      "item_code": null,
      "value": null,
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "其他",
      "item_code": null,
      "value": "未见",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "白细胞镜检",
      "item_code": null,
      "value": "2-4",
      "unit": "/HP",
      "reference_range": "0-5",
      "abnormal": false
    },
    {
      "name": "颗粒管型",
      "item_code": null,
      "value": "0",
      "unit": null,
      "reference_range": "0",
      "abnormal": false
    },
    {
      "name": "颜色",
      "item_code": "Colour",
      "value": "黄色",
      "unit": null,
      "reference_range": "黄色",
      "abnormal": false
    },
    {
      "name": "尿葡萄糖",
      "item_code": "GLU",
      "value": "+4",
      "unit": "mmol/ul",
      "reference_range": "阴性",
      "abnormal": true
    },
    {
      "name": "酮体",
      "item_code": "KET",
      "value": null,
      "unit": "mmol/L",
      "reference_range": "阴性",
      "abnormal": false
    },
    {
      "name": "比重",
      "item_code": "SG",
      "value": "1.020",
      "unit": null,
      "reference_range": "1.010-1.030",
      "abnormal": false
    },
    {
      "name": "酸碱度",
      "item_code": "PH",
      "value": "5.0",
      "unit": null,
      "reference_range": "4.5-8.0",
      "abnormal": false
    },
    {
      "name": "尿蛋白质",
      "item_code": "PRO",
      "value": null,
      "unit": "g/L",
      "reference_range": "阴性",
      "abnormal": false
    },
    {
      "name": "尿胆原",
      "item_code": "URO",
      "value": null,
      "unit": "umol/L",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "亚硝酸盐",
      "item_code": "NIT",
      "value": null,
      "unit": null,
      "reference_range": "阴性",
      "abnormal": false
    },
    {
      "name": "上皮细胞",
      "item_code": "Epi.cells",
      "value": "1-3",
      "unit": "个/ul",
      "reference_range": "0-5",
      "abnormal": false
    },
    {
      "name": "红细胞镜检",
      "item_code": null,
      "value": "0",
      "unit": "/ul",
      "reference_range": "0-3",
      "abnormal": false
    },
    {
      "name": "白细胞(尿液)",
      "item_code": null,
      "value": null,
      "unit": "1euko/ul",
      "reference_range": "阴性",
      "abnormal": false
    }
  ]
}
2026-08-10 13:23:23,639 INFO     29 [qwen-vl-table] coord grouping: {3: 20}
2026-08-10 13:23:23,642 INFO     29 [qwen-vl-table] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=918891, prompt_len=599
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
维生素C、透明管型、胆红素、结晶检查、尿潜血、尿脓细胞、其他、白细胞镜检、颗粒管型、颜色、尿葡萄糖、酮体、比重、酸碱度、尿蛋白质、尿胆原、亚硝酸盐、上皮细胞、红细胞镜检、白细胞(尿液)

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
2026-08-10 13:23:30,974 INFO     29 [qwen-vl-table] coord API raw response (len=955):
[
	{"text": "维生素C", "bbox": [67, 140, 134, 158]},
	{"text": "透明管型", "bbox": [68, 169, 143, 187]},
	{"text": "胆红素", "bbox": [70, 199, 169, 216]},
	{"text": "结晶检查", "bbox": [71, 228, 206, 246]},
	{"text": "尿潜血", "bbox": [73, 257, 170, 275]},
	{"text": "尿脓细胞", "bbox": [75, 287, 150, 304]},
	{"text": "其他", "bbox": [77, 315, 115, 333]},
	{"text": "白细胞镜检", "bbox": [79, 344, 169, 361]},
	{"text": "颗粒管型", "bbox": [80, 372, 153, 389]},
	{"text": "颜色", "bbox": [81, 400, 187, 417]},
	{"text": "尿葡萄糖", "bbox": [83, 428, 197, 445]},
	{"text": "酮体", "bbox": [84, 456, 162, 473]},
	{"text": "比重", "bbox": [85, 483, 154, 499]},
	{"text": "酸碱度", "bbox": [86, 510, 172, 527]},
	{"text": "尿蛋白质", "bbox": [87, 537, 199, 554]},
	{"text": "尿胆原", "bbox": [88, 564, 181, 581]},
	{"text": "亚硝酸盐", "bbox": [89, 591, 199, 608]},
	{"text": "上皮细胞", "bbox": [90, 619, 252, 636]},
	{"text": "红细胞镜检", "bbox": [85, 647, 173, 664]},
	{"text": "白细胞(尿液)", "bbox": [85, 675, 199, 692]}
]
2026-08-10 13:23:30,975 INFO     29 [qwen-vl-table] coord API: raw_items=20, valid_items=20, elapsed=7.3s
2026-08-10 13:23:30,975 INFO     29 [qwen-vl-table] coord item[0]: text=维生素C, bbox=[67, 140, 134, 158]
2026-08-10 13:23:30,975 INFO     29 [qwen-vl-table] coord item[1]: text=透明管型, bbox=[68, 169, 143, 187]
2026-08-10 13:23:30,975 INFO     29 [qwen-vl-table] coord item[2]: text=胆红素, bbox=[70, 199, 169, 216]
2026-08-10 13:23:30,975 INFO     29 [qwen-vl-table] coord item[3]: text=结晶检查, bbox=[71, 228, 206, 246]
2026-08-10 13:23:30,975 INFO     29 [qwen-vl-table] coord item[4]: text=尿潜血, bbox=[73, 257, 170, 275]
2026-08-10 13:23:30,975 INFO     29 [qwen-vl-table] coord item[5]: text=尿脓细胞, bbox=[75, 287, 150, 304]
2026-08-10 13:23:30,975 INFO     29 [qwen-vl-table] coord item[6]: text=其他, bbox=[77, 315, 115, 333]
2026-08-10 13:23:30,975 INFO     29 [qwen-vl-table] coord item[7]: text=白细胞镜检, bbox=[79, 344, 169, 361]
2026-08-10 13:23:30,975 INFO     29 [qwen-vl-table] coord item[8]: text=颗粒管型, bbox=[80, 372, 153, 389]
2026-08-10 13:23:30,975 INFO     29 [qwen-vl-table] coord item[9]: text=颜色, bbox=[81, 400, 187, 417]
2026-08-10 13:23:30,975 INFO     29 [qwen-vl-table] coord item[10]: text=尿葡萄糖, bbox=[83, 428, 197, 445]
2026-08-10 13:23:30,976 INFO     29 [qwen-vl-table] coord item[11]: text=酮体, bbox=[84, 456, 162, 473]
2026-08-10 13:23:30,976 INFO     29 [qwen-vl-table] coord item[12]: text=比重, bbox=[85, 483, 154, 499]
2026-08-10 13:23:30,976 INFO     29 [qwen-vl-table] coord item[13]: text=酸碱度, bbox=[86, 510, 172, 527]
2026-08-10 13:23:30,976 INFO     29 [qwen-vl-table] coord item[14]: text=尿蛋白质, bbox=[87, 537, 199, 554]
2026-08-10 13:23:30,976 INFO     29 [qwen-vl-table] coord item[15]: text=尿胆原, bbox=[88, 564, 181, 581]
2026-08-10 13:23:30,976 INFO     29 [qwen-vl-table] coord item[16]: text=亚硝酸盐, bbox=[89, 591, 199, 608]
2026-08-10 13:23:30,976 INFO     29 [qwen-vl-table] coord item[17]: text=上皮细胞, bbox=[90, 619, 252, 636]
2026-08-10 13:23:30,976 INFO     29 [qwen-vl-table] coord item[18]: text=红细胞镜检, bbox=[85, 647, 173, 664]
2026-08-10 13:23:30,976 INFO     29 [qwen-vl-table] coord item[19]: text=白细胞(尿液), bbox=[85, 675, 199, 692]
2026-08-10 13:23:30,976 INFO     29 [qwen-vl-table] page=3 coord: matched 20/20, time=7.3s
2026-08-10 13:23:30,976 INFO     29 [qwen-vl-table] new_positions (20):
[[4, 56.28, 112.56, 156.87, 177.03900000000002], [4, 57.12, 120.11999999999999, 189.36450000000002, 209.5335], [4, 58.8, 141.96, 222.9795, 242.02800000000002], [4, 59.64, 173.04, 255.47400000000002, 275.64300000000003], [4, 61.32, 142.79999999999998, 287.9685, 308.1375], [4, 63.0, 126.0, 321.5835, 340.632], [4, 64.67999999999999, 96.6, 352.95750000000004, 373.1265], [4, 66.36, 141.96, 385.452, 404.50050000000005], [4, 67.2, 128.51999999999998, 416.826, 435.8745], [4, 68.03999999999999, 157.07999999999998, 448.20000000000005, 467.24850000000004], [4, 69.72, 165.48, 479.574, 498.6225], [4, 70.56, 136.07999999999998, 510.94800000000004, 529.9965], [4, 71.39999999999999, 129.35999999999999, 541.2015, 559.1295], [4, 72.24, 144.48, 571.455, 590.5035], [4, 73.08, 167.16, 601.7085000000001, 620.7570000000001], [4, 73.92, 152.04, 631.962, 651.0105], [4, 74.75999999999999, 167.16, 662.2155, 681.264], [4, 75.6, 211.67999999999998, 693.5895, 712.638], [4, 71.39999999999999, 145.32, 724.9635000000001, 744.0120000000001], [4, 71.39999999999999, 167.16, 756.3375000000001, 775.3860000000001]]
2026-08-10 13:23:30,977 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=20, matched=20, pages=1, time=16.6s
2026-08-10 13:23:30,978 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:23:30,982 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:23:30,982 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[3]
2026-08-10 13:23:30,982 INFO     29 [qwen-vl-table] positions ： [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:23:31,148 INFO     29 [qwen-vl-table] page=3, rect=840x1120, img=(2334x3113)
2026-08-10 13:23:31,149 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:23:31,149 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 73, \"bbox_end\": 80, \"encounter_dates\": [\"2025-04-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{l c c c c}\n报告时间: 2025-04-23\n\\hline\n项目名称 & 结果 & 单位 & 参考范围 & 提示 \\\\\n\\hline\n葡萄糖(GLU) & 8.13 & mmol/L & 3.90-6.11 & $\\uparrow$ \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:23:32,743 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:23:32,743 INFO     29 [qwen-vl-table] page=3 LLM output (len=218):
{
  "report_date": "2025-04-23",
  "items": [
    {
      "name": "葡萄糖",
      "item_code": "GLU",
      "value": "8.13",
      "unit": "mmol/L",
      "reference_range": "3.90-6.11",
      "abnormal": true
    }
  ]
}
2026-08-10 13:23:32,744 INFO     29 [qwen-vl-table] coord grouping: {3: 1}
2026-08-10 13:23:32,745 INFO     29 [qwen-vl-table] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=918891, prompt_len=510
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
葡萄糖

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
2026-08-10 13:23:33,437 INFO     29 [qwen-vl-table] coord API raw response (len=61):
```json
[
	{"text": "葡萄糖", "bbox": [81, 787, 175, 804]}
]
```
2026-08-10 13:23:33,437 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=0.7s
2026-08-10 13:23:33,437 INFO     29 [qwen-vl-table] coord item[0]: text=葡萄糖, bbox=[81, 787, 175, 804]
2026-08-10 13:23:33,437 INFO     29 [qwen-vl-table] page=3 coord: matched 1/1, time=0.7s
2026-08-10 13:23:33,437 INFO     29 [qwen-vl-table] new_positions (1):
[[4, 68.03999999999999, 147.0, 881.8335000000001, 900.8820000000001]]
2026-08-10 13:23:33,437 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=2.5s
2026-08-10 13:23:33,438 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:23:33,439 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:23:33,439 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[3]
2026-08-10 13:23:33,439 INFO     29 [qwen-vl-table] positions ： [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:23:33,603 INFO     29 [qwen-vl-table] page=3, rect=840x1120, img=(2334x3113)
2026-08-10 13:23:33,604 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:23:33,604 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 81, \"bbox_end\": 88, \"encounter_dates\": [\"2025-04-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{l c c c c}\n报告时间: 2025-04-23\n\\hline\n项目名称 & 结果 & 单位 & 参考范围 & 提示 \\\\\n\\hline\n糖化血红蛋白 & 9.8 & \\% & 4.2-5.9 & $\\uparrow$ \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 13:23:34,718 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:23:34,719 INFO     29 [qwen-vl-table] page=3 LLM output (len=212):
{
  "report_date": "2025-04-23",
  "items": [
    {
      "name": "糖化血红蛋白",
      "item_code": null,
      "value": "9.8",
      "unit": "%",
      "reference_range": "4.2-5.9",
      "abnormal": true
    }
  ]
}
2026-08-10 13:23:34,719 INFO     29 [qwen-vl-table] coord grouping: {3: 1}
2026-08-10 13:23:34,722 INFO     29 [qwen-vl-table] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=918891, prompt_len=513
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
2026-08-10 13:23:35,363 INFO     29 [qwen-vl-table] coord API raw response (len=65):
```json
[
	{"text": "糖化血红蛋白", "bbox": [421, 856, 565, 880]}
]
```
2026-08-10 13:23:35,364 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=0.6s
2026-08-10 13:23:35,364 INFO     29 [qwen-vl-table] coord item[0]: text=糖化血红蛋白, bbox=[421, 856, 565, 880]
2026-08-10 13:23:35,365 INFO     29 [qwen-vl-table] page=3 coord: matched 1/1, time=0.6s
2026-08-10 13:23:35,365 INFO     29 [qwen-vl-table] new_positions (1):
[[4, 353.64, 474.59999999999997, 959.148, 986.0400000000001]]
2026-08-10 13:23:35,365 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=1.9s
2026-08-10 13:23:35,378 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 13:23:35,378 INFO     29 [Trace] task=8cbb7524 | doc=CLHo糖尿病-哈大四.pdf | Extractor:LabExam | outputs={"chunks": "4 items, types={'LabReport': 4}", "html": "", "json": "101 items", "markdown": "", "text": "", "name": "CLHo糖尿病-哈大四.pdf", "output_format": "chunks", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Medication\": 2, \"chunks_Clinical\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 13:23:35,378 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 13:23:35,384 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:23:35,384 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:23:35,814 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:23:35,824 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 13:23:35,824 INFO     29 [Trace] task=8cbb7524 | doc=CLHo糖尿病-哈大四.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "101 items", "markdown": "", "text": "", "name": "CLHo糖尿病-哈大四.pdf", "output_format": "chunks", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Medication\": 2, \"chunks_Clinical\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 13:23:35,825 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 13:23:35,830 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:23:35,831 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:23:35,831 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 13:23:35,831 INFO     29 [qwen-vl-text] positions(23): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:23:35,832 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [23]
2026-08-10 13:23:35,974 INFO     29 [qwen-vl-text] page=1, rect=608x1080, img=(1688x3000), dpi=200
2026-08-10 13:23:35,975 INFO     29 [qwen-vl-text] LLM extraction start, text_len=261
2026-08-10 13:23:35,975 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:23:35,975 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 14, \"bbox_end\": 36, \"encounter_dates\": [\"2024-09-04\"], \"department\": \"门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "肇东市永馨福园综合门诊\n门诊号：MZ9925103\n科室：门诊 接诊日期：2024-09\n姓名：\n病区：/\n接诊医师：/\n性别：女\n年龄：50岁\n住址：/\n临床诊断：2型糖尿病\n主诉：口干渴、出虚汗伴眩晕7日\n现病史：自述确诊2型糖尿病8年余，口干渴、出虚汗伴眩晕7日\n既往史：同现病史\n过敏史：\n查体：体温36.4℃ 血压130/90mmHg (-)\n辅助检查：已回报\n处理意见：\n1、盐酸二甲双胍片 0.5g/3次/日餐前口服；\n2、监测血糖，不适门诊随访；\n打印日期：2024-01-09\n医生签字\n主治医师\n胡维波",
    "role": "user"
  }
]
2026-08-10 13:23:37,525 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:23:37,525 INFO     29 [qwen-vl-text] LLM output (len=247):
{
  "encounter_date": "2024-09-04",
  "chief_complaint": "口干渴、出虚汗伴眩晕7日",
  "present_illness": "自述确诊2型糖尿病8年余，口干渴、出虚汗伴眩晕7日",
  "past_history": "同现病史",
  "diagnosis": "2型糖尿病",
  "treatment_plan": [
    "盐酸二甲双胍片 0.5g/3次/日餐前口服",
    "监测血糖，不适门诊随访"
  ]
}
2026-08-10 13:23:37,526 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-09-04]
2026-08-10 13:23:37,531 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1102725, prompt_len=943
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共23行）
["肇东市永馨福园综合门诊", "门诊号：MZ9925103", "科室：门诊 接诊日期：2024-09", "姓名：", "病区：/", "接诊医师：/", "性别：女", "年龄：50岁", "住址：/", "临床诊断：2型糖尿病", "主诉：口干渴、出虚汗伴眩晕7日", "现病史：自述确诊2型糖尿病8年余，口干渴、出虚汗伴眩晕7日", "既往史：同现病史", "过敏史：", "查体：体温36.4℃ 血压130/90mmHg (-)", "辅助检查：已回报", "处理意见：", "1、盐酸二甲双胍片 0.5g/3次/日餐前口服；", "2、监测血糖，不适门诊随访；", "打印日期：2024-01-09", "医生签字", "主治医师", "胡维波"]

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
2026-08-10 13:23:46,714 INFO     29 [qwen-vl-text] coord API raw response (len=1276):
[
	{"text": "肇东市永馨福园综合门诊", "bbox": [268, 192, 675, 223]},
	{"text": "门诊号：MZ9925103", "bbox": [100, 225, 348, 251]},
	{"text": "科室：门诊 接诊日期：2024-09", "bbox": [390, 235, 823, 259]},
	{"text": "姓名：", "bbox": [100, 253, 185, 274]},
	{"text": "病区：/", "bbox": [389, 259, 490, 277]},
	{"text": "接诊医师：/", "bbox": [557, 260, 708, 280]},
	{"text": "性别：女", "bbox": [100, 279, 246, 300]},
	{"text": "年龄：50岁", "bbox": [390, 283, 537, 301]},
	{"text": "住址：/", "bbox": [564, 285, 712, 304]},
	{"text": "临床诊断：2型糖尿病", "bbox": [100, 304, 384, 326]},
	{"text": "主诉：口干渴、出虚汗伴眩晕7日", "bbox": [100, 329, 558, 351]},
	{"text": "现病史：自述确诊2型糖尿病8年余，口干渴、出虚汗伴眩晕7日", "bbox": [100, 355, 829, 377]},
	{"text": "既往史：同现病史", "bbox": [100, 404, 335, 423]},
	{"text": "过敏史：", "bbox": [100, 430, 197, 449]},
	{"text": "查体：体温36.4℃ 血压130/90mmHg (-)", "bbox": [100, 455, 657, 475]},
	{"text": "辅助检查：已回报", "bbox": [100, 480, 335, 500]},
	{"text": "处理意见：", "bbox": [100, 506, 227, 525]},
	{"text": "1、盐酸二甲双胍片 0.5g/3次/日餐前口服；", "bbox": [235, 528, 770, 549]},
	{"text": "2、监测血糖，不适门诊随访；", "bbox": [234, 554, 601, 574]},
	{"text": "打印日期：2024-01-09", "bbox": [105, 840, 405, 866]},
	{"text": "医生签字", "bbox": [574, 827, 681, 848]},
	{"text": "主治医师", "bbox": [700, 802, 823, 833]},
	{"text": "胡维波", "bbox": [702, 837, 824, 873]}
]
2026-08-10 13:23:46,715 INFO     29 [qwen-vl-text] coord API: raw_items=23, valid_items=23, elapsed=9.2s
2026-08-10 13:23:46,715 INFO     29 [qwen-vl-text] coord item[0]: text=肇东市永馨福园综合门诊, bbox=[268, 192, 675, 223]
2026-08-10 13:23:46,715 INFO     29 [qwen-vl-text] coord item[1]: text=门诊号：MZ9925103, bbox=[100, 225, 348, 251]
2026-08-10 13:23:46,715 INFO     29 [qwen-vl-text] coord item[2]: text=科室：门诊 接诊日期：2024-09, bbox=[390, 235, 823, 259]
2026-08-10 13:23:46,715 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[100, 253, 185, 274]
2026-08-10 13:23:46,715 INFO     29 [qwen-vl-text] coord item[4]: text=病区：/, bbox=[389, 259, 490, 277]
2026-08-10 13:23:46,715 INFO     29 [qwen-vl-text] coord item[5]: text=接诊医师：/, bbox=[557, 260, 708, 280]
2026-08-10 13:23:46,715 INFO     29 [qwen-vl-text] coord item[6]: text=性别：女, bbox=[100, 279, 246, 300]
2026-08-10 13:23:46,715 INFO     29 [qwen-vl-text] coord item[7]: text=年龄：50岁, bbox=[390, 283, 537, 301]
2026-08-10 13:23:46,715 INFO     29 [qwen-vl-text] coord item[8]: text=住址：/, bbox=[564, 285, 712, 304]
2026-08-10 13:23:46,716 INFO     29 [qwen-vl-text] coord item[9]: text=临床诊断：2型糖尿病, bbox=[100, 304, 384, 326]
2026-08-10 13:23:46,716 INFO     29 [qwen-vl-text] coord item[10]: text=主诉：口干渴、出虚汗伴眩晕7日, bbox=[100, 329, 558, 351]
2026-08-10 13:23:46,716 INFO     29 [qwen-vl-text] coord item[11]: text=现病史：自述确诊2型糖尿病8年余，口干渴、出虚汗伴眩晕7日, bbox=[100, 355, 829, 377]
2026-08-10 13:23:46,716 INFO     29 [qwen-vl-text] coord item[12]: text=既往史：同现病史, bbox=[100, 404, 335, 423]
2026-08-10 13:23:46,716 INFO     29 [qwen-vl-text] coord item[13]: text=过敏史：, bbox=[100, 430, 197, 449]
2026-08-10 13:23:46,716 INFO     29 [qwen-vl-text] coord item[14]: text=查体：体温36.4℃ 血压130/90mmHg (-), bbox=[100, 455, 657, 475]
2026-08-10 13:23:46,716 INFO     29 [qwen-vl-text] coord item[15]: text=辅助检查：已回报, bbox=[100, 480, 335, 500]
2026-08-10 13:23:46,716 INFO     29 [qwen-vl-text] coord item[16]: text=处理意见：, bbox=[100, 506, 227, 525]
2026-08-10 13:23:46,716 INFO     29 [qwen-vl-text] coord item[17]: text=1、盐酸二甲双胍片 0.5g/3次/日餐前口服；, bbox=[235, 528, 770, 549]
2026-08-10 13:23:46,716 INFO     29 [qwen-vl-text] coord item[18]: text=2、监测血糖，不适门诊随访；, bbox=[234, 554, 601, 574]
2026-08-10 13:23:46,716 INFO     29 [qwen-vl-text] coord item[19]: text=打印日期：2024-01-09, bbox=[105, 840, 405, 866]
2026-08-10 13:23:46,716 INFO     29 [qwen-vl-text] coord item[20]: text=医生签字, bbox=[574, 827, 681, 848]
2026-08-10 13:23:46,716 INFO     29 [qwen-vl-text] coord item[21]: text=主治医师, bbox=[700, 802, 823, 833]
2026-08-10 13:23:46,716 INFO     29 [qwen-vl-text] coord item[22]: text=胡维波, bbox=[702, 837, 824, 873]
2026-08-10 13:23:46,717 INFO     29 [qwen-vl-text] page=1 — 23/23 coords, api_time=9.2s
2026-08-10 13:23:46,717 INFO     29 [qwen-vl-text] new_positions (23):
[[1, 162.81, 410.0625, 207.36, 240.84], [1, 60.75000000000001, 211.41000000000003, 243.00000000000003, 271.08000000000004], [1, 236.925, 499.9725, 253.8, 279.72], [1, 60.75000000000001, 112.3875, 273.24, 295.92], [1, 236.31750000000002, 297.675, 279.72, 299.16], [1, 338.3775, 430.11, 280.8, 302.40000000000003], [1, 60.75000000000001, 149.44500000000002, 301.32, 324.0], [1, 236.925, 326.2275, 305.64000000000004, 325.08000000000004], [1, 342.63, 432.54, 307.8, 328.32000000000005], [1, 60.75000000000001, 233.28000000000003, 328.32000000000005, 352.08000000000004], [1, 60.75000000000001, 338.985, 355.32000000000005, 379.08000000000004], [1, 60.75000000000001, 503.6175, 383.40000000000003, 407.16], [1, 60.75000000000001, 203.51250000000002, 436.32000000000005, 456.84000000000003], [1, 60.75000000000001, 119.67750000000001, 464.40000000000003, 484.92], [1, 60.75000000000001, 399.12750000000005, 491.40000000000003, 513.0], [1, 60.75000000000001, 203.51250000000002, 518.4000000000001, 540.0], [1, 60.75000000000001, 137.9025, 546.48, 567.0], [1, 142.76250000000002, 467.77500000000003, 570.24, 592.9200000000001], [1, 142.155, 365.1075, 598.32, 619.9200000000001], [1, 63.7875, 246.03750000000002, 907.2, 935.2800000000001], [1, 348.70500000000004, 413.70750000000004, 893.1600000000001, 915.84], [1, 425.25, 499.9725, 866.1600000000001, 899.6400000000001], [1, 426.46500000000003, 500.58000000000004, 903.96, 942.84]]
2026-08-10 13:23:46,717 INFO     29 [qwen-vl-text] ═══ DONE ═══ 23 positions, pages=1, time=10.9s
2026-08-10 13:23:46,732 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 13:23:46,732 INFO     29 [Trace] task=8cbb7524 | doc=CLHo糖尿病-哈大四.pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "101 items", "markdown": "", "text": "", "name": "CLHo糖尿病-哈大四.pdf", "output_format": "chunks", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Medication\": 2, \"chunks_Clinical\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 13:23:46,732 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 13:23:46,740 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:23:46,741 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:23:46,741 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 13:23:46,742 INFO     29 [qwen-vl-text] positions(14): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:23:46,742 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [14]
2026-08-10 13:23:46,887 INFO     29 [qwen-vl-text] page=0, rect=608x1080, img=(1688x3000), dpi=200
2026-08-10 13:23:46,888 INFO     29 [qwen-vl-text] LLM extraction start, text_len=190
2026-08-10 13:23:46,888 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:23:46,888 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 0, \"bbox_end\": 13, \"encounter_dates\": [\"2024-09-04\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "肇东市维康大药房\n有限公司销售单\n流水号9999000234562564544\n日期2024-09-04 09:27:13\n会员: 积分0.0000\n180245 盐酸二甲双胍片\n规格0.25g*1201 批号24020\n效期2026-01 产地.河北天成\n数量5盒 单价 ￥7.00元\n合计金额: ￥35.00元\n付款方式: 现金01\n健康热线:\n药品为特殊商品,一经售出不\n换",
    "role": "user"
  }
]
2026-08-10 13:23:49,022 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:23:49,023 INFO     29 [qwen-vl-text] LLM output (len=419):
{
  "encounter_date": "2024-09-04",
  "pharmacy": "肇东市维康大药房有限公司",
  "medications": [
    {
      "name": "盐酸二甲双胍片",
      "specification": "0.25g*120片",
      "dosage": null,
      "quantity": 5,
      "unit_price": 7.00,
      "total_price": 35.00,
      "frequency": null,
      "route": null,
      "manufacturer": "河北天成",
      "approval_number": null
    }
  ],
  "payment_total": 35.00,
  "payment_method": "现金"
}
2026-08-10 13:23:49,023 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-09-04]
2026-08-10 13:23:49,029 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1337159, prompt_len=845
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共14行）
["肇东市维康大药房", "有限公司销售单", "流水号9999000234562564544", "日期2024-09-04 09:27:13", "会员: 积分0.0000", "180245 盐酸二甲双胍片", "规格0.25g*1201 批号24020", "效期2026-01 产地.河北天成", "数量5盒 单价 ￥7.00元", "合计金额: ￥35.00元", "付款方式: 现金01", "健康热线:", "药品为特殊商品,一经售出不", "换"]

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
2026-08-10 13:23:54,663 INFO     29 [qwen-vl-text] coord API raw response (len=809):
[
	{"text": "肇东市维康大药房", "bbox": [192, 104, 642, 147]},
	{"text": "有限公司销售单", "bbox": [188, 162, 580, 202]},
	{"text": "流水号9999000234562564544", "bbox": [181, 214, 862, 260]},
	{"text": "日期2024-09-04 09:27:13", "bbox": [178, 264, 845, 308]},
	{"text": "会员: 积分0.0000", "bbox": [173, 311, 817, 358]},
	{"text": "180245 盐酸二甲双胍片", "bbox": [168, 363, 740, 407]},
	{"text": "规格0.25g*1201 批号24020", "bbox": [156, 411, 845, 458]},
	{"text": "效期2026-01 产地.河北天成", "bbox": [152, 460, 860, 508]},
	{"text": "数量5盒 单价 ￥7.00元", "bbox": [144, 511, 797, 559]},
	{"text": "合计金额: ￥35.00元", "bbox": [140, 563, 692, 609]},
	{"text": "付款方式: 现金01", "bbox": [133, 614, 613, 661]},
	{"text": "健康热线:", "bbox": [128, 668, 373, 707]},
	{"text": "药品为特殊商品,一经售出不", "bbox": [127, 719, 830, 763]},
	{"text": "换", "bbox": [125, 771, 175, 795]}
]
2026-08-10 13:23:54,663 INFO     29 [qwen-vl-text] coord API: raw_items=14, valid_items=14, elapsed=5.6s
2026-08-10 13:23:54,663 INFO     29 [qwen-vl-text] coord item[0]: text=肇东市维康大药房, bbox=[192, 104, 642, 147]
2026-08-10 13:23:54,663 INFO     29 [qwen-vl-text] coord item[1]: text=有限公司销售单, bbox=[188, 162, 580, 202]
2026-08-10 13:23:54,663 INFO     29 [qwen-vl-text] coord item[2]: text=流水号9999000234562564544, bbox=[181, 214, 862, 260]
2026-08-10 13:23:54,664 INFO     29 [qwen-vl-text] coord item[3]: text=日期2024-09-04 09:27:13, bbox=[178, 264, 845, 308]
2026-08-10 13:23:54,664 INFO     29 [qwen-vl-text] coord item[4]: text=会员: 积分0.0000, bbox=[173, 311, 817, 358]
2026-08-10 13:23:54,664 INFO     29 [qwen-vl-text] coord item[5]: text=180245 盐酸二甲双胍片, bbox=[168, 363, 740, 407]
2026-08-10 13:23:54,664 INFO     29 [qwen-vl-text] coord item[6]: text=规格0.25g*1201 批号24020, bbox=[156, 411, 845, 458]
2026-08-10 13:23:54,664 INFO     29 [qwen-vl-text] coord item[7]: text=效期2026-01 产地.河北天成, bbox=[152, 460, 860, 508]
2026-08-10 13:23:54,664 INFO     29 [qwen-vl-text] coord item[8]: text=数量5盒 单价 ￥7.00元, bbox=[144, 511, 797, 559]
2026-08-10 13:23:54,664 INFO     29 [qwen-vl-text] coord item[9]: text=合计金额: ￥35.00元, bbox=[140, 563, 692, 609]
2026-08-10 13:23:54,664 INFO     29 [qwen-vl-text] coord item[10]: text=付款方式: 现金01, bbox=[133, 614, 613, 661]
2026-08-10 13:23:54,664 INFO     29 [qwen-vl-text] coord item[11]: text=健康热线:, bbox=[128, 668, 373, 707]
2026-08-10 13:23:54,664 INFO     29 [qwen-vl-text] coord item[12]: text=药品为特殊商品,一经售出不, bbox=[127, 719, 830, 763]
2026-08-10 13:23:54,664 INFO     29 [qwen-vl-text] coord item[13]: text=换, bbox=[125, 771, 175, 795]
2026-08-10 13:23:54,665 INFO     29 [qwen-vl-text] page=0 — 14/14 coords, api_time=5.6s
2026-08-10 13:23:54,666 INFO     29 [qwen-vl-text] new_positions (14):
[[0, 116.64000000000001, 390.01500000000004, 112.32000000000001, 158.76000000000002], [0, 114.21000000000001, 352.35, 174.96, 218.16000000000003], [0, 109.95750000000001, 523.6650000000001, 231.12, 280.8], [0, 108.135, 513.3375, 285.12, 332.64000000000004], [0, 105.09750000000001, 496.32750000000004, 335.88, 386.64000000000004], [0, 102.06, 449.55, 392.04, 439.56], [0, 94.77000000000001, 513.3375, 443.88000000000005, 494.64000000000004], [0, 92.34, 522.45, 496.8, 548.64], [0, 87.48, 484.1775, 551.88, 603.72], [0, 85.05000000000001, 420.39000000000004, 608.0400000000001, 657.72], [0, 80.7975, 372.39750000000004, 663.12, 713.88], [0, 77.76, 226.59750000000003, 721.44, 763.5600000000001], [0, 77.1525, 504.225, 776.5200000000001, 824.0400000000001], [0, 75.9375, 106.3125, 832.6800000000001, 858.6]]
2026-08-10 13:23:54,666 INFO     29 [qwen-vl-text] ═══ DONE ═══ 14 positions, pages=1, time=7.9s
2026-08-10 13:23:54,666 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 13:23:54,675 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 13:23:54,675 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 13:23:54,675 INFO     29 [qwen-vl-text] positions(12): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 13:23:54,675 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [12]
2026-08-10 13:23:54,841 INFO     29 [qwen-vl-text] page=4, rect=608x1080, img=(1688x3000), dpi=200
2026-08-10 13:23:54,842 INFO     29 [qwen-vl-text] LLM extraction start, text_len=174
2026-08-10 13:23:54,842 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:23:54,843 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 89, \"bbox_end\": 100, \"encounter_dates\": [\"2024-12-07\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "哈尔滨泽福大药房销售单\nNO.98222250454552\n2024-12-07 15:14:48\n会员 卡号：999918\n215114 盐酸二甲双胍片\n0.25gx120片/盒 2406015\n2026/05/30 河北天成药业\n10盒x8.00=80.00\n销售员 韩晶晶 Hlt:03\n金额小计：￥80.00元\n付款方式：现款销售\n健康热线",
    "role": "user"
  }
]
2026-08-10 13:23:54,848 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T13:23:54.847+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 47, "failed": 0, "current": {"8cbb752494be11f1bd9827cf206dfa2d": {"id": "8cbb752494be11f1bd9827cf206dfa2d", "doc_id": "8c88a43294be11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "CLHo\u7cd6\u5c3f\u75c5-\u54c8\u5927\u56db.pdf", "type": "pdf", "location": "CLHo\u7cd6\u5c3f\u75c5-\u54c8\u5927\u56db.pdf", "size": 1024502, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786368155101, "task_type": "dataflow", "root_trace_id": "d96187892a0044bdbc8ca087b3270949", "root_traceparent": "00-d96187892a0044bdbc8ca087b3270949-fa185c031b5a1abd-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 13:23:56,987 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:23:56,987 INFO     29 [qwen-vl-text] LLM output (len=422):
{
  "encounter_date": "2024-12-07",
  "pharmacy": "哈尔滨泽福大药房",
  "medications": [
    {
      "name": "盐酸二甲双胍片",
      "specification": "0.25gx120片/盒",
      "dosage": null,
      "quantity": 10,
      "unit_price": 8.00,
      "total_price": 80.00,
      "frequency": null,
      "route": null,
      "manufacturer": "河北天成药业",
      "approval_number": null
    }
  ],
  "payment_total": 80.00,
  "payment_method": "现款销售"
}
2026-08-10 13:23:56,987 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-12-07]
2026-08-10 13:23:56,989 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1036084, prompt_len=823
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共12行）
["哈尔滨泽福大药房销售单", "NO.98222250454552", "2024-12-07 15:14:48", "会员 卡号：999918", "215114 盐酸二甲双胍片", "0.25gx120片/盒 2406015", "2026/05/30 河北天成药业", "10盒x8.00=80.00", "销售员 韩晶晶 Hlt:03", "金额小计：￥80.00元", "付款方式：现款销售", "健康热线"]

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
2026-08-10 13:24:02,758 INFO     29 [qwen-vl-text] coord API raw response (len=717):
[
  {"text": "哈尔滨泽福大药房销售单", "bbox": [295, 375, 787, 402]},
  {"text": "NO.98222250454552", "bbox": [295, 405, 721, 431]},
  {"text": "2024-12-07 15:14:48", "bbox": [293, 437, 729, 467]},
  {"text": "会员 卡号：999918", "bbox": [295, 470, 873, 504]},
  {"text": "215114 盐酸二甲双胍片", "bbox": [293, 508, 760, 539]},
  {"text": "0.25gx120片/盒 2406015", "bbox": [291, 542, 813, 577]},
  {"text": "2026/05/30 河北天成药业", "bbox": [288, 580, 835, 614]},
  {"text": "10盒x8.00=80.00", "bbox": [312, 618, 755, 650]},
  {"text": "销售员 韩晶晶 Hlt:03", "bbox": [285, 658, 800, 691]},
  {"text": "金额小计：￥80.00元", "bbox": [283, 698, 758, 731]},
  {"text": "付款方式：现款销售", "bbox": [279, 738, 711, 771]},
  {"text": "健康热线", "bbox": [275, 780, 473, 809]}
]
2026-08-10 13:24:02,759 INFO     29 [qwen-vl-text] coord API: raw_items=12, valid_items=12, elapsed=5.8s
2026-08-10 13:24:02,759 INFO     29 [qwen-vl-text] coord item[0]: text=哈尔滨泽福大药房销售单, bbox=[295, 375, 787, 402]
2026-08-10 13:24:02,759 INFO     29 [qwen-vl-text] coord item[1]: text=NO.98222250454552, bbox=[295, 405, 721, 431]
2026-08-10 13:24:02,759 INFO     29 [qwen-vl-text] coord item[2]: text=2024-12-07 15:14:48, bbox=[293, 437, 729, 467]
2026-08-10 13:24:02,759 INFO     29 [qwen-vl-text] coord item[3]: text=会员 卡号：999918, bbox=[295, 470, 873, 504]
2026-08-10 13:24:02,759 INFO     29 [qwen-vl-text] coord item[4]: text=215114 盐酸二甲双胍片, bbox=[293, 508, 760, 539]
2026-08-10 13:24:02,759 INFO     29 [qwen-vl-text] coord item[5]: text=0.25gx120片/盒 2406015, bbox=[291, 542, 813, 577]
2026-08-10 13:24:02,759 INFO     29 [qwen-vl-text] coord item[6]: text=2026/05/30 河北天成药业, bbox=[288, 580, 835, 614]
2026-08-10 13:24:02,759 INFO     29 [qwen-vl-text] coord item[7]: text=10盒x8.00=80.00, bbox=[312, 618, 755, 650]
2026-08-10 13:24:02,759 INFO     29 [qwen-vl-text] coord item[8]: text=销售员 韩晶晶 Hlt:03, bbox=[285, 658, 800, 691]
2026-08-10 13:24:02,759 INFO     29 [qwen-vl-text] coord item[9]: text=金额小计：￥80.00元, bbox=[283, 698, 758, 731]
2026-08-10 13:24:02,759 INFO     29 [qwen-vl-text] coord item[10]: text=付款方式：现款销售, bbox=[279, 738, 711, 771]
2026-08-10 13:24:02,759 INFO     29 [qwen-vl-text] coord item[11]: text=健康热线, bbox=[275, 780, 473, 809]
2026-08-10 13:24:02,759 INFO     29 [qwen-vl-text] page=4 — 12/12 coords, api_time=5.8s
2026-08-10 13:24:02,759 INFO     29 [qwen-vl-text] new_positions (12):
[[4, 179.2125, 478.1025, 405.0, 434.16], [4, 179.2125, 438.00750000000005, 437.40000000000003, 465.48], [4, 177.9975, 442.8675, 471.96000000000004, 504.36], [4, 179.2125, 530.3475000000001, 507.6, 544.32], [4, 177.9975, 461.70000000000005, 548.64, 582.12], [4, 176.7825, 493.89750000000004, 585.36, 623.1600000000001], [4, 174.96, 507.26250000000005, 626.4000000000001, 663.12], [4, 189.54000000000002, 458.6625, 667.44, 702.0], [4, 173.13750000000002, 486.00000000000006, 710.6400000000001, 746.2800000000001], [4, 171.9225, 460.485, 753.84, 789.48], [4, 169.4925, 431.9325, 797.0400000000001, 832.6800000000001], [4, 167.0625, 287.3475, 842.4000000000001, 873.72]]
2026-08-10 13:24:02,759 INFO     29 [qwen-vl-text] ═══ DONE ═══ 12 positions, pages=1, time=8.1s
2026-08-10 13:24:02,765 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 13:24:02,765 INFO     29 [Trace] task=8cbb7524 | doc=CLHo糖尿病-哈大四.pdf | Extractor:Medication | outputs={"chunks": "2 items, types={'MedicationRecord': 2}", "html": "", "json": "101 items", "markdown": "", "text": "", "name": "CLHo糖尿病-哈大四.pdf", "output_format": "chunks", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Medication\": 2, \"chunks_Clinical\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 13:24:02,765 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 13:24:02,770 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:24:02,770 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:24:03,607 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:24:03,613 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 13:24:03,613 INFO     29 [Trace] task=8cbb7524 | doc=CLHo糖尿病-哈大四.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "101 items", "markdown": "", "text": "", "name": "CLHo糖尿病-哈大四.pdf", "output_format": "chunks", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Medication\": 2, \"chunks_Clinical\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 13:24:03,613 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 13:24:03,619 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:24:03,619 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:24:04,165 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:24:04,169 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 13:24:04,169 INFO     29 [Trace] task=8cbb7524 | doc=CLHo糖尿病-哈大四.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "101 items", "markdown": "", "text": "", "name": "CLHo糖尿病-哈大四.pdf", "output_format": "chunks", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Medication\": 2, \"chunks_Clinical\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 13:24:04,169 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 13:24:04,174 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:24:04,174 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:24:04,671 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:24:04,680 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 13:24:04,680 INFO     29 [Trace] task=8cbb7524 | doc=CLHo糖尿病-哈大四.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "101 items", "markdown": "", "text": "", "name": "CLHo糖尿病-哈大四.pdf", "output_format": "chunks", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Medication\": 2, \"chunks_Clinical\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 13:24:04,680 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 13:24:04,691 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:24:04,691 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:24:05,781 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:24:05,792 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 13:24:05,792 INFO     29 [Trace] task=8cbb7524 | doc=CLHo糖尿病-哈大四.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "101 items", "markdown": "", "text": "", "name": "CLHo糖尿病-哈大四.pdf", "output_format": "chunks", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Medication\": 2, \"chunks_Clinical\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 13:24:05,792 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 13:24:05,800 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:24:05,801 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 13:24:06,287 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 13:24:06,297 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 13:24:06,298 INFO     29 [Trace] task=8cbb7524 | doc=CLHo糖尿病-哈大四.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "101 items", "markdown": "", "text": "", "name": "CLHo糖尿病-哈大四.pdf", "output_format": "chunks", "chunks_Medication": "2 items, types={'MedicationRecord': 2}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "4 items, types={'LabReport': 4}", "route_summary": "{\"chunks_Medication\": 2, \"chunks_Clinical\": 1, \"chunks_LabExam\": 4}"}
2026-08-10 13:24:06,298 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 13:24:06,298 INFO     29 [ChunkMerger] Merged 7 chunks from 9 sources: {'Extractor:LabExam': 4, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 2, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 6 noise chunks)
2026-08-10 13:24:06,310 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 13:24:06,310 INFO     29 [Trace] task=8cbb7524 | doc=CLHo糖尿病-哈大四.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "7 items, types={'LabReport': 4, 'OutpatientRecord': 1, 'MedicationRecord': 2}", "name": "CLHo糖尿病-哈大四.pdf"}
2026-08-10 13:24:06,310 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 13:24:06,349 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786368155769, 'update_date': datetime.datetime(2026, 8, 10, 13, 22, 35), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1036250, 'status': '1'}
2026-08-10 13:24:06,539 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   葡萄糖  GLU  13.6  mmol/L  4.11-5.90  True    糖化血红蛋白  HbA1c  9.9  %  3.90-6.11  True   
---
   维生素C  None  +  None  None  False    透明管型  None  0  /LP  0  False    胆红素  BIL  None  umol/L  阴性  False    结晶检查  X'TAL  None  None  None  False    尿潜血  BLD  None  Ery/ul  阴性  False    尿脓细胞  None  None  None  None  False    其他  None  未见  None  None  False    白细胞镜检  None  2-4  /HP  0-5  False    颗粒管型  None  0  None  0  False    颜色  Colour  黄色  None  黄色  False    尿葡萄糖  GLU  +4  mmol/ul  阴性  True    酮体  KET  None  mmol/L  阴性  False    比重  SG  1.020  None  1.010-1.030  False    酸碱度  PH  5.0  None  4.5-8.0  False    尿蛋白质  PRO  None  g/L  阴性  False    尿胆原  URO  None  umol/L  None  False    亚硝酸盐  NIT  None  None  阴性  False    上皮细胞  Epi.cells  1-3  个/ul  0-5  False    红细胞镜检  None  0  /ul  0-3  False    白细胞(尿液)  None  None  1euko/ul  阴性  False   
---
   葡萄糖  GLU  8.13  mmol/L  3.90-6.11  True   
---
   糖化血红蛋白  None  9.8  %  4.2-5.9  True   
---
肇东市永馨福园综合门诊
门诊号：MZ9925103
科室：门诊 接诊日期：2024-09
姓名：
病区：/
接诊医师：/
性别：女
年龄：50岁
住址：/
临床诊断：2型糖尿病
主诉：口干渴、出虚汗伴眩晕7日
现病史：自述确诊2型糖尿病8年余，口干渴、出虚汗伴眩晕7日
既往史：同现病史
过敏史：
查体：体温36.4℃ 血压130/90mmHg (-)
辅助检查：已回报
处理意见：
1、盐酸二甲双胍片 0.5g/3次/日餐前口服；
2、监测血糖，不适门诊随访；
打印日期：2024-01-09
医生签字
主治医师
胡维波
---
肇东市维康大药房
有限公司销售单
流水号9999000234562564544
日期2024-09-04 09:27:13
会员: 积分0.0000
180245 盐酸二甲双胍片
规格0.25g*1201 批号24020
效期2026-01 产地.河北天成
数量5盒 单价 ￥7.00元
合计金额: ￥35.00元
付款方式: 现金01
健康热线:
药品为特殊商品,一经售出不
换
---
哈尔滨泽福大药房销售单
NO.98222250454552
2024-12-07 15:14:48
会员 卡号：999918
215114 盐酸二甲双胍片
0.25gx120片/盒 2406015
2026/05/30 河北天成药业
10盒x8.00=80.00
销售员 韩晶晶 Hlt:03
金额小计：￥80.00元
付款方式：现款销售
健康热线
2026-08-10 13:24:06,854 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 13:24:06,854 INFO     29 [Trace] task=8cbb7524 | doc=CLHo糖尿病-哈大四.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "7 items, types={'LabReport': 4, 'OutpatientRecord': 1, 'MedicationRecord': 2}", "name": "CLHo糖尿病-哈大四.pdf", "embedding_token_consumption": 1102}
2026-08-10 13:24:06,854 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 13:24:07,015 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 13:24:07,015 INFO     29 [Trace] task=8cbb7524 | doc=CLHo糖尿病-哈大四.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":7,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 13:24:07,018 INFO     29 [DIAG-EXECUTOR] row_position_int len=2 row[0]=(3, 494, 514, 241, 302) row[-1]=(3, 447, 468, 240, 362)
2026-08-10 13:24:07,019 INFO     29 [DIAG-EXECUTOR] row_position_int len=20 row[0]=(4, 56, 112, 156, 177) row[-1]=(4, 71, 167, 756, 775)
2026-08-10 13:24:07,019 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(4, 68, 147, 881, 900) row[-1]=(4, 68, 147, 881, 900)
2026-08-10 13:24:07,019 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(4, 353, 474, 959, 986) row[-1]=(4, 353, 474, 959, 986)
2026-08-10 13:24:07,019 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:24:07,019 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:24:07,019 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 13:24:07,023 INFO     29 set_progress(8cbb752494be11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 13:24:07 [DOC Engine]:
Start to index...
2026-08-10 13:24:07,041 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.013s]
2026-08-10 13:24:07,045 INFO     29 set_progress(8cbb752494be11f1bd9827cf206dfa2d), progress: 0.8142857142857143, progress_msg: 
2026-08-10 13:24:07,057 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.007s]
2026-08-10 13:24:07,064 INFO     29 set_progress(8cbb752494be11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 13:24:07 Indexing done (0.04s). Task done (87.01s)
2026-08-10 13:24:07,068 INFO     29 [Done], chunks(7), token(1102), elapsed:87.01
2026-08-10 13:24:07,143 INFO     29 handle_task done for task {"id": "8cbb752494be11f1bd9827cf206dfa2d", "doc_id": "8c88a43294be11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "CLHo\u7cd6\u5c3f\u75c5-\u54c8\u5927\u56db.pdf", "type": "pdf", "location": "CLHo\u7cd6\u5c3f\u75c5-\u54c8\u5927\u56db.pdf", "size": 1024502, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786368155101, "task_type": "dataflow", "root_trace_id": "d96187892a0044bdbc8ca087b3270949", "root_traceparent": "00-d96187892a0044bdbc8ca087b3270949-fa185c031b5a1abd-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
