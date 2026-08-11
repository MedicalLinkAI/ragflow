# 基准结果：十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf

## 基本信息

- 文件：`十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf`
- 大小：10654.1 KB
- PDF 总页数：12
- doc_id：`37728ffc94d311f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T23:50:30  完成时间：2026-08-10T23:58:23  耗时：472.6s
- progress_msg：`15:58:19 Indexing done (0.10s). Task done (440.08s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 48adf251 | 4 | 1-4 | 2025.1 确诊小细胞癌，已行免疫组化协诊 2025-.2-4给予”EP”化疗 |
| 2 | 2fd75ed1 | 1 | 5-5 | 信阳市中心医院 免疫病理诊断报告 免疫组化号：MT25- 姓名： 性别：女 年龄 |
| 3 | eaf0d8eb | 1 | 6-6 | 信阳市中心医院 病理检查报告单 病理号：D25 姓名： 性别：女 年龄：64岁  |
| 4 | 5d826d63 | 1 | 7-7 | 信阳市中心医院 影像科CT诊断报告书 扫描 获取电子胶 片和报告(试用) 影像号 |
| 5 | 37a3a764 | 1 | 8-8 | 信阳市中心医院 影像科CT诊断报告书 扫描此二维码可 电子胶 片和报告(试用)  |
| 6 | 2917d131 | 1 | 9-9 | 信阳市中心医院心电图报告单 门诊号: 姓名: P波宽度: 141ms 诊断: 1 |
| 7 | d02411ee | 1 | 11-11 | <table><tr><td>谷丙转氨酶</td><td>ALT</td><td |
| 8 | 80642063 | 1 | 10-10 | <table><tr><td>癌胚抗原</td><td>CEA</td><td> |
| 9 | ccff2040 | 1 | 12-12 | <table><tr><td>白细胞</td><td>WBC</td><td>3 |

- chunks 总数：9
- 各 chunk 页数合计（含跨页重复）：12
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]`
- 覆盖页数：12 / 12；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 0 | 0 | 0 | encounter_date, chief_complaint, diagnosis | **-** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 1 | 1 | 1 | admission_date, discharge_date, department, outcome | **OK** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 5 | 5 | 5 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 3 | 0 | 3 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"DischargeRecord": 1, "ExaminationReport": 5, "LabReport": 3}`
- ChunkMerger：`{"found": true, "merged": 9, "sources": 9, "stats": {"Extractor:LabExam": 3, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 5, "Extractor:Progress": 1}, "filtered_noise": 6}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 15:58:18,650 INFO     29 [ChunkMerger] Merged 9 chunks from 9 sources: {'Extractor:LabExam': 3, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 15:50:35,086 INFO     29 handle_task begin for task {"id": "3880a51e94d311f1bd9827cf206dfa2d", "doc_id": "37728ffc94d311f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909800, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377033220, "task_type": "dataflow", "root_trace_id": "4dc9fd8a1d244ef89de3e82f6546943d", "root_traceparent": "00-4dc9fd8a1d244ef89de3e82f6546943d-90143aef6fb19019-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 15:50:35,304 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 15:50:35,430 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 15:50:35,449 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:50:35,449 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 15:50:35,449 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 15:50:35,454 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 15:50:35,454 INFO     29 ============================================================
2026-08-10 15:50:35,454 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 15:50:35,454 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 15:50:35,454 INFO     29 ============================================================
2026-08-10 15:50:35,454 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 15:50:35,454 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 15:50:35,455 INFO     29 No torch found.
2026-08-10 15:50:38,301 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:50:38.299+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 70, "failed": 0, "current": {"3880a51e94d311f1bd9827cf206dfa2d": {"id": "3880a51e94d311f1bd9827cf206dfa2d", "doc_id": "37728ffc94d311f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909800, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377033220, "task_type": "dataflow", "root_trace_id": "4dc9fd8a1d244ef89de3e82f6546943d", "root_traceparent": "00-4dc9fd8a1d244ef89de3e82f6546943d-90143aef6fb19019-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:50:38,722 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=12
2026-08-10 15:50:39,113 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=549369, prompt_len=764
2026-08-10 15:50:47,076 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 15:50:47,076 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 15:50:47,094 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=549369, prompt_len=401
2026-08-10 15:50:49,047 INFO     29 [qwen-vl-parser] text API response (len=205):
["2025.1 确诊小细胞癌，已行免疫组化协诊", "2025-.2-4给予”EP”化疗联合”特瑞普利单抗”免疫治疗3周期，", "2025-04-22给予”EP”方案化疗联合", "“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗", "2025.5-8行“特瑞普利单抗”免疫治疗4周期", "2025.8 PD", "2025.8-2026.2“替雷利珠单抗联合安罗替尼”免疫治疗"]
2026-08-10 15:50:49,047 INFO     29 [qwen-vl-parser] page=1 text: 7 lines (bbox 0-6)
2026-08-10 15:50:49,047 INFO     29 [qwen-vl-parser] page=1 text: 7 sections
2026-08-10 15:50:50,406 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7962152, prompt_len=764
2026-08-10 15:50:58,960 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 15:50:58,962 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 15:50:58,985 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7962152, prompt_len=401
2026-08-10 15:51:06,848 INFO     29 [qwen-vl-parser] text API response (len=797):
["信阳市中心医院", "日间化疗出入院记录", "姓名：", "性别：女年龄：65岁", "科别：日间化疗中心[东院床号：04", "区]", "登记号：0000", "住院号：25", "入院时间：2026年03月23日 08:29:00出院时间：2026年03月23日 11:14:00", "住院天数：1天", "主诉：确诊肺癌1年余", "入院情况：1年余前因“胸闷”就诊我院，2025-01-17CT增强64：1.右肺门占位，考虑恶性病变并", "右肺中下叶不张，右下肺动受侵可能。2.双肺纤维索条灶。双肺多发小结节，转移待排。3.右侧", "胸腔少量积液。4.双肾小囊肿。5.升结肠多发憩室。6.子宫后壁肌瘤可能。7.冠状动脉CTA未见明", "显异常。2025-01-23行纤支镜下肺活检，2025-01-23活体组织病理申请 诊断意见：(右中间段支", "气管)考虑小细胞癌，已行免疫组化协诊。2025-01-26免疫组化申请：CK广谱（点+），CD56（+），", "Syn（+），INSM1（+），CK5/6（-），P40（-），TTF1（+），NapsinA（-），Ki-67（80%+）。结合HE", "及免疫组化结果，（右中间段支气管）肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04", "-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期，2025-04-22给予“EP”方案化疗联合", "“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗。2025-05-19、2025", "-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加增强", "(胸部.上腹部.下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节。"]
2026-08-10 15:51:06,852 INFO     29 [qwen-vl-parser] page=2 text: 22 lines (bbox 7-28)
2026-08-10 15:51:06,852 INFO     29 [qwen-vl-parser] page=2 text: 22 sections
2026-08-10 15:51:07,809 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5188086, prompt_len=764
2026-08-10 15:51:10,028 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:51:10.027+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 70, "failed": 0, "current": {"3880a51e94d311f1bd9827cf206dfa2d": {"id": "3880a51e94d311f1bd9827cf206dfa2d", "doc_id": "37728ffc94d311f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909800, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377033220, "task_type": "dataflow", "root_trace_id": "4dc9fd8a1d244ef89de3e82f6546943d", "root_traceparent": "00-4dc9fd8a1d244ef89de3e82f6546943d-90143aef6fb19019-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:51:15,812 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 15:51:15,813 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 15:51:15,828 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5188086, prompt_len=401
2026-08-10 15:51:22,575 INFO     29 [qwen-vl-parser] text API response (len=892):
["胸腔少量积液。4.双肾小囊肿。5.升结肠多发息室。6.丁台加壁肌瘤可能。冠状动脉CT示无明显异常。2025-01-23行纤支镜下肺活检，2025-01-23活体组织病理申请 诊断意见：(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。2025-01-26免疫组化申请：CK广谱(点+)，CD56(+)，Syn(+)，INSM1(+)，CK5/6(-)，P40(-)，TTF1(+)，NapsinA(-)，Ki-67(80%)。结合HE及免疫组化结果，(右中间段支气管)肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期，2025-04-22给予“EP”方案化疗联合“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗。2025-05-19、2025-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加强(胸部，上腹部，下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节，转移瘤可能；建议追踪复查。2.双肺慢性炎症，右肺中叶局限性支扩，双侧胸腔少量积液。3.脾脏低密度灶，建议追踪复查。4.胆囊可疑小结石。升结肠多发憩室。5.双肾小囊肿。与2025-05-18日片比较：右肺中叶局限性支扩，右肺下叶内基底段结节较前增大，右肺门淋巴结较前增大。考虑病情进展，于2025-08-23给予“安罗替尼12mg”联合“替雷利珠单抗”抗肿瘤治疗1周期。后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-22、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重无明显变化。诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利，予办理出院手续。"]
2026-08-10 15:51:22,576 INFO     29 [qwen-vl-parser] page=3 text: 1 lines (bbox 29-29)
2026-08-10 15:51:22,576 INFO     29 [qwen-vl-parser] page=3 text: 1 sections
2026-08-10 15:51:23,548 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4627238, prompt_len=764
2026-08-10 15:51:31,087 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 15:51:31,087 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-10 15:51:31,107 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4627238, prompt_len=401
2026-08-10 15:51:38,806 INFO     29 [qwen-vl-parser] text API response (len=990):
["国家医保编码：D411502011804 - Internet Explorer", "美系统) 修改患者信息 诊疗与病历 申请单 手术管理 医嘱单 会诊管理 重症管理 需关注医嘱 病情总览 质量管理 更多", "汤光冉 住院医师", "日间化疗中心[东院区]", "0000 床号: 04 住院天数: 1 费别: 全国医保居民 余额: 0.00 诊断: 肺恶性肿瘤,恶性肿瘤... 医疗救助类型: 农村低保", "病人列表 全息视图", "(1) ×", "操作 编辑 功能 表格 其他", "历", "保存 打印 自动续打 预览 单独打印 手工解锁 隐藏留痕 病历参考 更新数据 首页", "记录", "1:09:45 曾庆星", "医师审核", "录单", "1:10:52 曾庆星", "医师审核", "录单", "1:11:53 曾庆星", "医师审核", "11:12:02 曾庆星", "医师审核", "单(日间...", "11:13:02 曾庆星", "医师审核", "已打印", "11:15:03 曾庆星", "医师审核", "评估表", "16:30:58 曾庆星", "院医师审核", "/TE风险评...", "16:32:44 曾庆星", "院医师审核", "后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-2", "2、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我", "院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重", "无明显变化。", "诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利", "，予办理出院手续。", "出院情况：患者未诉不适，神志清，精神可，生命体征平稳。", "出院诊断：", "1.恶性肿瘤免疫治疗", "2.肺恶性肿瘤小细胞肺癌IV期", "3.肺继发恶性肿瘤", "4.冠状动脉粥样硬化性心脏病", "5.胸腔积液", "6.心包积液", "7.肺部感染", "8.腔隙性脑梗死", "9.肾功能检查的异常结果", "1", "100%", "16:57", "2026/3/23"]
2026-08-10 15:51:38,806 INFO     29 [qwen-vl-parser] page=4 text: 54 lines (bbox 30-83)
2026-08-10 15:51:38,806 INFO     29 [qwen-vl-parser] page=4 text: 54 sections
2026-08-10 15:51:39,496 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4388375, prompt_len=764
2026-08-10 15:51:40,758 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:51:40.757+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 70, "failed": 0, "current": {"3880a51e94d311f1bd9827cf206dfa2d": {"id": "3880a51e94d311f1bd9827cf206dfa2d", "doc_id": "37728ffc94d311f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909800, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377033220, "task_type": "dataflow", "root_trace_id": "4dc9fd8a1d244ef89de3e82f6546943d", "root_traceparent": "00-4dc9fd8a1d244ef89de3e82f6546943d-90143aef6fb19019-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:51:47,066 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2025-01-24"
}
```
2026-08-10 15:51:47,067 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=2025-01-24
2026-08-10 15:51:47,083 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4388375, prompt_len=401
2026-08-10 15:51:50,558 INFO     29 [qwen-vl-parser] text API response (len=471):
["信阳市中心医院", "免疫病理诊断报告", "免疫组化号：MT25-", "姓名：", "性别：女", "年龄：64岁", "送检医院：", "病区：肿瘤内科五护理单元[东病理号：D25-01313", "就诊卡号：", "住院号：2", "病区床号：21", "送检标本：肺手术标本", "送检时间：2025-01-24", "临床诊断：", "光镜所见：", "免疫病理诊断：", "CK广谱（点+），CD56（+），Syn（+），INSM1（+），CK5/6（-），P40（-），TTF1（+），", "NapsinA（-），Ki-67（80%+）。", "结合HE及免疫组化结果，（右中间段支气管）肺小细胞神经内分泌癌。", "初诊医师：刘磊", "复诊医师：刘磊", "报告日期：2025-01-26 10:49", "备注：1.本报告单仅供临床参考 2.如临床对报告内容有疑问请与报告医生联系。联系电话：0376-6227723(西院区)，0376-6667570(东院区)。", "3.此报告必须经过病理科医师签字有效。"]
2026-08-10 15:51:50,560 INFO     29 [qwen-vl-parser] page=5 text: 24 lines (bbox 84-107)
2026-08-10 15:51:50,560 INFO     29 [qwen-vl-parser] page=5 text: 24 sections
2026-08-10 15:51:51,233 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4556779, prompt_len=764
2026-08-10 15:51:58,612 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-01-23"}
```
2026-08-10 15:51:58,614 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=2025-01-23
2026-08-10 15:51:58,648 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4556779, prompt_len=401
2026-08-10 15:52:01,528 INFO     29 [qwen-vl-parser] text API response (len=381):
["信阳市中心医院", "病理检查报告单", "病理号：D25", "姓名：", "性别：女", "年龄：64岁", "送检医院：", "送检科室：呼吸与危重症医学科送检日期：2025-01-22", "门诊号：9", "住院号：25", "床号：21", "送检医师：周鹏飞", "送检标本：右中间段支气管", "临床诊断：", "巨检：灰白色碎组织最大径0.3厘米。全取", "病理诊断：", "(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。", "初诊医师：刘晶晶", "复诊医师：刘磊", "报告日期：2025-01-23 19:26", "备注：1.本报告单仅供临床参考 2.如临床对报告内容有疑问请与报告医生联系。联系电话：0376-6227723(西院区)；0376-6667570(东院区)。", "3.此报告必须经过病理科医师签字有效。"]
2026-08-10 15:52:01,529 INFO     29 [qwen-vl-parser] page=6 text: 22 lines (bbox 108-129)
2026-08-10 15:52:01,529 INFO     29 [qwen-vl-parser] page=6 text: 22 sections
2026-08-10 15:52:02,096 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3308277, prompt_len=764
2026-08-10 15:52:11,805 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2025-12-22"
}
```
2026-08-10 15:52:11,807 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=2025-12-22
2026-08-10 15:52:11,823 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3308277, prompt_len=401
2026-08-10 15:52:13,524 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:52:13.521+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 70, "failed": 0, "current": {"3880a51e94d311f1bd9827cf206dfa2d": {"id": "3880a51e94d311f1bd9827cf206dfa2d", "doc_id": "37728ffc94d311f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909800, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377033220, "task_type": "dataflow", "root_trace_id": "4dc9fd8a1d244ef89de3e82f6546943d", "root_traceparent": "00-4dc9fd8a1d244ef89de3e82f6546943d-90143aef6fb19019-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:52:17,775 INFO     29 [qwen-vl-parser] text API response (len=883):
["信阳市中心医院", "影像科CT诊断报告书", "扫描", "获取电子胶", "片和报告(试用)", "影像号: 000", "报告日期: 2025-12-22 16:36", "姓名:", "性别: 女", "年龄: 64岁", "检查日期: 2025-12-22", "科别: 日间化疗中心[东院区]院号: 2", "门诊号:/", "检查时间: 09:53:10", "检查方法: 胸部CT平扫,胸部CT增强,上腹部CT平扫,上腹部CT增强,下腹部CT平扫,下腹部CT增强", "技术参数:", "影像学所见:", "双侧胸廓对称,右肺门增大,可见不规则状软组织密度影,密度不均,边", "界不清,强化不均,右肺中下叶支气管稍变窄,双肺可见条索状及结节状高密", "度影,较大病灶位于右肺下叶内基底段见实性结节,大小约为15.8×15.4mm,", "轻度强化。右肺中叶局限性支扩。气管、支气管通畅,右肺门见明显肿大淋巴", "结,轻度强化,双侧胸膜腔及心包腔可见积液征象。与2025-8-21日片比较:", "双侧胸腔积液增多,心包积液新增,右肺门软组织密度影及淋巴结增大。", "肝脏未见明显异常密度及异常强化征象,胆囊内隐约见斑点状高密度影,", "脾脏见数个小灶状低强化影。胰腺形态、大小、密度正常。双肾见小圆形低密", "度影,边界清,增强未见明显强化。腹膜后未见明显增大淋巴结,腹腔未见明", "显积液征象。升结肠见多发小囊袋状外凸影。与2025-8-21日片比较:大致相", "仿。", "影像学意见:", "1. 右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节,转移瘤可能;建", "议追踪复查:右肺门肿大淋巴结。", "2. 双肺慢性炎症,右肺中叶局限性支扩,双侧胸腔积液,心包积液。", "3. 脾脏低密度灶,建议追踪复查。", "4. 胆囊可疑小结石。升结肠多发憩室。", "5. 双肾小囊肿。", "报告医师:", "审核医师:", "此报告仅供临床医师参考,签字生效", "打印时间: 2025-12-22 16:36:26"]
2026-08-10 15:52:17,778 INFO     29 [qwen-vl-parser] page=7 text: 39 lines (bbox 130-168)
2026-08-10 15:52:17,778 INFO     29 [qwen-vl-parser] page=7 text: 39 sections
2026-08-10 15:52:18,475 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4611687, prompt_len=764
2026-08-10 15:52:26,264 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-02-25"}
```
2026-08-10 15:52:26,266 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=2026-02-25
2026-08-10 15:52:26,288 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4611687, prompt_len=401
2026-08-10 15:52:30,809 INFO     29 [qwen-vl-parser] text API response (len=615):
["信阳市中心医院", "影像科CT诊断报告书", "扫描此二维码可", "电子胶", "片和报告(试用)", "影像号:0000", "报告日期:2026-02-25 15:36", "姓名:", "性别:女", "年龄:65岁", "检查日期:2026-02-25", "科别:肿瘤内科五门诊[东院住院号:/", "门诊号:1", "6", "检查时间:08:57:41", "检查方法:胸部CT平扫加薄层", "技术参数:", "影像学所见:", "双侧胸廓对称,右肺门增大,可见不规则状软组织密度影,密度不均,边", "界不清,右肺中下叶支气管稍变窄,双肺可见条索状及结节状高密度影。右肺", "中叶局限性支扩。气管、支气管通畅,右肺门见明显肿大淋巴结,右侧胸膜局", "部稍厚,双侧胸膜腔及心包腔可见积液征象。与2025-12-22日片比较:右侧胸", "腔积液增多,右肺门软组织密度影及淋巴结进一步增大,右肺结节增大,右侧", "胸膜局部稍增厚。", "影像学意见:", "1.右肺癌并右肺中下叶不张治疗状态。双肺多发结节,转移瘤可能;右肺门", "肿大淋巴结转移。", "2.双肺慢性炎症,双侧胸腔积液,心包积液。", "3.右侧胸膜局部稍厚,不除外转移。", "报告医师:", "肖健", "审核医师:", "贺玲", "此报告仅供临床医师参考,签字生效", "打印时间:2026-02-25 15:36:58"]
2026-08-10 15:52:30,810 INFO     29 [qwen-vl-parser] page=8 text: 35 lines (bbox 169-203)
2026-08-10 15:52:30,810 INFO     29 [qwen-vl-parser] page=8 text: 35 sections
2026-08-10 15:52:31,826 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7005445, prompt_len=764
2026-08-10 15:52:41,782 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-03-23"
}
```
2026-08-10 15:52:41,784 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=2026-03-23
2026-08-10 15:52:41,807 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7005445, prompt_len=401
2026-08-10 15:52:45,160 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:52:45.159+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 70, "failed": 0, "current": {"3880a51e94d311f1bd9827cf206dfa2d": {"id": "3880a51e94d311f1bd9827cf206dfa2d", "doc_id": "37728ffc94d311f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909800, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377033220, "task_type": "dataflow", "root_trace_id": "4dc9fd8a1d244ef89de3e82f6546943d", "root_traceparent": "00-4dc9fd8a1d244ef89de3e82f6546943d-90143aef6fb19019-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:52:45,604 INFO     29 [qwen-vl-parser] text API response (len=491):
["信阳市中心医院心电图报告单", "门诊号:", "姓名:", "P波宽度: 141ms", "诊断: 1.窦性心律", "住院号: 0000", "性别: 女", "P-R间期: 181ms", "【120-200】", "2.低电压", "床位号: 04", "年龄: 65岁", "QRS时限: 101ms", "【60-110】", "科室: 日间化疗中心[心率: 77bpm", "【60-100】", "QT/QTc: 358/406ms", "【360-440】", "东院区]", "电轴: 60°", "【-30-90】", "2026-03-23 08:43:55", "25mm/s 10mm/mV", "I", "V1", "V3R", "II", "V2", "III", "V3", "V4R", "aVR", "V4", "aVL", "V5", "V5R", "aVF", "V6", "II", "检查时间: 2026/3/23 8:43:55", "报告时间: 2026/3/23 8:59:30", "报告医生:", "审核医生:", ""]
2026-08-10 15:52:45,607 INFO     29 [qwen-vl-parser] page=9 text: 43 lines (bbox 204-246)
2026-08-10 15:52:45,607 INFO     29 [qwen-vl-parser] page=9 text: 43 sections
2026-08-10 15:52:46,609 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5483158, prompt_len=764
2026-08-10 15:52:54,333 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-23"
}
```
2026-08-10 15:52:54,335 INFO     29 [qwen-vl-parser] page=10 classify=table report_date=2026-03-23
2026-08-10 15:52:54,375 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5483158, prompt_len=756
2026-08-10 15:52:56,434 INFO     29 [qwen-vl-parser] table API response (len=242):
\begin{tabular}{ccccccccc}
\hline
序号 & 项目代号 & 项目名称 & 结果 & 单位 & 参考值 \\
\hline
1 & CEA & 癌胚抗原 & 5.03 & ng/mL & 0—5.2 \\
2 & CYFRA21-1 & 非小细胞肺癌相关抗原 & 4.60 & ng/ml & 0—3.3 \\
3 & NSE & 神经元特异性烯醇化酶测定 & 10.60 & ng/mL & 0—16.3 \\
\hline
\end{tabular}
2026-08-10 15:52:56,440 INFO     29 [qwen-vl-parser] page=10 table: 10 LaTeX lines (bbox 247-256)
2026-08-10 15:52:56,440 INFO     29 [qwen-vl-parser] page=10 table: 10 sections
2026-08-10 15:52:57,226 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5228539, prompt_len=764
2026-08-10 15:53:05,224 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-23"
}
```
2026-08-10 15:53:05,224 INFO     29 [qwen-vl-parser] page=11 classify=table report_date=2026-03-23
2026-08-10 15:53:05,240 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5228539, prompt_len=756
2026-08-10 15:53:14,429 INFO     29 [qwen-vl-parser] table API response (len=1286):
\begin{tabular}{ccccccccc}
\hline
序 & 代号 & 名称 & 结果 & 参考范围 & 单位 & 序 & 代号 & 名称 & 结果 & 参考范围 & 单位 \\
\hline
1 & ALT & 谷丙转氨酶 & 52 & ↑ 7—40 & U/L & 18 & CK & 肌酸激酶 & 396 & ↑ 26—192 & U/L \\
2 & AST & 谷草转氨酶 & 54 & ↑ 13—35 & U/L & 19 & CK-MB & 肌酸酶同功酶 & 17.70 & 7—25 & U/L \\
3 & TP & 总蛋白 & 69.8 & 65—85 & g/L & 20 & MYO & 肌红蛋白 & 77.4 & ↑ 0—70 & ug/L \\
4 & ALB & 白蛋白 & 48.5 & 40—55 & g/L & 21 & K & 钾 & 3.74 & 3.5—5.3 & mmol/L \\
5 & GLOB & 球蛋白 & 21.3 & 20—40 & g/L & 22 & NA & 钠 & 132 & ↓ 137—147 & mmol/L \\
6 & A/G & 白球比 & 2.3 & 1.2—2.4 & & 23 & CL & 氯 & 96.0 & ↓ 99—110 & mmol/L \\
7 & TBIL & 总胆红素 & 13.6 & 1.7—21 & umol/L & 24 & CA & 钙 & 2.12 & 2.02—2.6 & mmol/L \\
8 & DBIL & 直接胆红素 & 1.7 & 0—6.8 & umol/L & 25 & CRP & C反应蛋白 & 0.41 & 0—5 & mg/L \\
9 & IBIL & 间接胆红素 & 11.9 & 3—13.6 & umol/L & 26 & eGFR & 估算肾小球滤 & 55.02 & & ml/min \\
10 & ALP & 碱性磷酸酶 & 67 & 50—135 & U/L & & & & & & \\
11 & GGT & 谷氨酰转肽酶 & 19 & 7—45 & U/L & & & & & & \\
12 & UREA & 尿素 & 4.15 & 2.76—8.07 & mmol/L & & & & & & \\
13 & CREA & 肌酐 & 94 & ↑ 45—84 & umol/L & & & & & & \\
14 & UA & 尿酸 & 192 & 143—339 & umol/L & & & & & & \\
15 & CO2 & 二氧化碳 & 25.9 & 22—29 & mmol/L & & & & & & \\
16 & GLU & 葡萄糖 & 6.25 & ↑ 3.8—6.1 & mmol/L & & & & & & \\
17 & LDH & 乳酸脱氢酶 & 291 & ↑ 135—214 & U/L & & & & & & \\
\hline
\end{tabular}
2026-08-10 15:53:14,431 INFO     29 [qwen-vl-parser] page=11 table: 24 LaTeX lines (bbox 257-280)
2026-08-10 15:53:14,431 INFO     29 [qwen-vl-parser] page=11 table: 24 sections
2026-08-10 15:53:15,046 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4540538, prompt_len=764
2026-08-10 15:53:16,942 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:53:16.940+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 70, "failed": 0, "current": {"3880a51e94d311f1bd9827cf206dfa2d": {"id": "3880a51e94d311f1bd9827cf206dfa2d", "doc_id": "37728ffc94d311f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909800, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377033220, "task_type": "dataflow", "root_trace_id": "4dc9fd8a1d244ef89de3e82f6546943d", "root_traceparent": "00-4dc9fd8a1d244ef89de3e82f6546943d-90143aef6fb19019-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:53:20,957 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-23"
}
```
2026-08-10 15:53:20,958 INFO     29 [qwen-vl-parser] page=12 classify=table report_date=2026-03-23
2026-08-10 15:53:20,974 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4540538, prompt_len=756
2026-08-10 15:53:29,273 INFO     29 [qwen-vl-parser] table API response (len=1535):
\begin{tabular}{llllllllll}
\hline
\multicolumn{1}{c}{序} & \multicolumn{1}{c}{代号} & \multicolumn{1}{c}{项目名称} & \multicolumn{1}{c}{结果} & \multicolumn{1}{c}{参考范围} & \multicolumn{1}{c}{单位} & \multicolumn{1}{c}{代号} & \multicolumn{1}{c}{项目名称} & \multicolumn{1}{c}{结果} & \multicolumn{1}{c}{参考范围} & \multicolumn{1}{c}{单位} \\
\hline
1 & WBC & 白细胞 & 3.62 & 3.5---9.5 & 10^9/L & 15 & MCV & 红细胞平均体积 & 89.4 & 82---100 & fL \\
2 & NEUT & 中性粒细胞百分比 & 68.80 & 40---75 & \% & 16 & MCH & 平均血红蛋白量 & 30.8 & 27---34 & pg \\
3 & LYMP & 淋巴细胞百分比 & 23.20 & 20---50 & \% & 17 & MCHC & 平均血红蛋白浓度 & 344 & 316---354 & g/L \\
4 & MONO & 单核细胞百分比 & 4.10 & 3---10 & \% & 18 & RDW- & 红细胞分布宽度标准 & 43 & 35---56 & fL \\
5 & EOS\% & 嗜酸性粒细胞百分比 & 2.5 & 0.4---8 & \% & 19 & RDW- & 红细胞分布宽度变异 & 13 & 11---16 & \% \\
6 & BASO & 嗜碱性粒细胞百分比 & 1.40 & 0---1 & \% & 20 & PLT & 血小板 & 155 & 125---350 & 10^9/L \\
7 & NEUT & 中性粒细胞计数 & 2.49 & 1.8---6.3 & 10^9/L & 21 & PDW & 血小板分布宽度 & 10.20 & 9.2---15.6 & fL \\
8 & LYMP & 淋巴细胞计数 & 0.84 & 1.1---3.2 & 10^9/L & 22 & MPV & 平均血小板体积 & 9.90 & 6.5---12 & fL \\
9 & MONO & 单核细胞计数 & 0.15 & 0.1---0.6 & 10^9/L & 23 & PCT & 血小板压积 & 0.150 & 0.108---0.282 & \% \\
10 & EOS\# & 嗜酸性粒细胞计数 & 0.09 & 0.02---0.52 & 10^9/L & 24 & P-LC & 大型血小板比率 & 24.00 & 11---45 & \% \\
11 & BASO & 嗜碱性粒细胞计数 & 0.05 & 0---0.06 & 10^9/L & 25 & PLCC & 大血小板数目 & 37.20 & 30---90 & 10^9/L \\
12 & RBC & 红细胞 & 4.06 & 3.8---5.1 & 10^12/L & & & & & & \\
13 & HGB & 血红蛋白 & 125 & 115---150 & g/L & & & & & & \\
14 & HCT & 红细胞压积 & 36.30 & 35---45 & \% & & & & & & \\
\hline
\end{tabular}
2026-08-10 15:53:29,277 INFO     29 [qwen-vl-parser] page=12 table: 21 LaTeX lines (bbox 281-301)
2026-08-10 15:53:29,277 INFO     29 [qwen-vl-parser] page=12 table: 21 sections
2026-08-10 15:53:29,277 INFO     29 [qwen-vl-parser] parse_pdf done: 302 sections from 12 pages.
2026-08-10 15:53:29,294 INFO     29 Close text detector.
2026-08-10 15:53:30,079 INFO     29 Close text recognizer.
2026-08-10 15:53:30,462 INFO     29 Close recognizer.
2026-08-10 15:53:30,864 INFO     29 Close recognizer.
2026-08-10 15:53:31,354 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 15:53:31,354 INFO     29 [Trace] task=3880a51e | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | Parser:MedLink | outputs={"html": "", "json": "302 items", "markdown": "", "text": "", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf", "output_format": "json"}
2026-08-10 15:53:31,354 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 15:53:31,379 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:53:31,379 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 2025.1 确诊小细胞癌，已行免疫组化协诊\n[BBOX-1] 2025-.2-4给予”EP”化疗联合”特瑞普利单抗”免疫治疗3周期，\n[BBOX-2] 2025-04-22给予”EP”方案化疗联合\n[BBOX-3] “替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗\n[BBOX-4] 2025.5-8行“特瑞普利单抗”免疫治疗4周期\n[BBOX-5] 2025.8 PD\n[BBOX-6] 2025.8-2026.2“替雷利珠单抗联合安罗替尼”免疫治疗\n[BBOX-7] 信阳市中心医院\n[BBOX-8] 日间化疗出入院记录\n[BBOX-9] 姓名：\n[BBOX-10] 性别：女年龄：65岁\n[BBOX-11] 科别：日间化疗中心[东院床号：04\n[BBOX-12] 区]\n[BBOX-13] 登记号：0000\n[BBOX-14] 住院号：25\n[BBOX-15] 入院时间：2026年03月23日 08:29:00出院时间：2026年03月23日 11:14:00\n[BBOX-16] 住院天数：1天\n[BBOX-17] 主诉：确诊肺癌1年余\n[BBOX-18] 入院情况：1年余前因“胸闷”就诊我院，2025-01-17CT增强64：1.右肺门占位，考虑恶性病变并\n[BBOX-19] 右肺中下叶不张，右下肺动受侵可能。2.双肺纤维索条灶。双肺多发小结节，转移待排。3.右侧\n[BBOX-20] 胸腔少量积液。4.双肾小囊肿。5.升结肠多发憩室。6.子宫后壁肌瘤可能。7.冠状动脉CTA未见明\n[BBOX-21] 显异常。2025-01-23行纤支镜下肺活检，2025-01-23活体组织病理申请 诊断意见：(右中间段支\n[BBOX-22] 气管)考虑小细胞癌，已行免疫组化协诊。2025-01-26免疫组化申请：CK广谱（点+），CD56（+），\n[BBOX-23] Syn（+），INSM1（+），CK5/6（-），P40（-），TTF1（+），NapsinA（-），Ki-67（80%+）。结合HE\n[BBOX-24] 及免疫组化结果，（右中间段支气管）肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04\n[BBOX-25] -01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期，2025-04-22给予“EP”方案化疗联合\n[BBOX-26] “替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗。2025-05-19、2025\n[BBOX-27] -06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加增强\n[BBOX-28] (胸部.上腹部.下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节。\n[BBOX-29] 胸腔少量积液。4.双肾小囊肿。5.升结肠多发息室。6.丁台加壁肌瘤可能。冠状动脉CT示无明显异常。2025-01-23行纤支镜下肺活检，2025-01-23活体组织病理申请 诊断意见：(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。2025-01-26免疫组化申请：CK广谱(点+)，CD56(+)，Syn(+)，INSM1(+)，CK5/6(-)，P40(-)，TTF1(+)，NapsinA(-)，Ki-67(80%)。结合HE及免疫组化结果，(右中间段支气管)肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期，2025-04-22给予“EP”方案化疗联合“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗。2025-05-19、2025-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加强(胸部，上腹部，下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节，转移瘤可能；建议追踪复查。2.双肺慢性炎症，右肺中叶局限性支扩，双侧胸腔少量积液。3.脾脏低密度灶，建议追踪复查。4.胆囊可疑小结石。升结肠多发憩室。5.双肾小囊肿。与2025-05-18日片比较：右肺中叶局限性支扩，右肺下叶内基底段结节较前增大，右肺门淋巴结较前增大。考虑病情进展，于2025-08-23给予“安罗替尼12mg”联合“替雷利珠单抗”抗肿瘤治疗1周期。后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-22、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重无明显变化。诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利，予办理出院手续。\n[BBOX-30] 国家医保编码：D411502011804 - Internet Explorer\n[BBOX-31] 美系统) 修改患者信息 诊疗与病历 申请单 手术管理 医嘱单 会诊管理 重症管理 需关注医嘱 病情总览 质量管理 更多\n[BBOX-32] 汤光冉 住院医师\n[BBOX-33] 日间化疗中心[东院区]\n[BBOX-34] 0000 床号: 04 住院天数: 1 费别: 全国医保居民 余额: 0.00 诊断: 肺恶性肿瘤,恶性肿瘤... 医疗救助类型: 农村低保\n[BBOX-35] 病人列表 全息视图\n[BBOX-36] (1) ×\n[BBOX-37] 操作 编辑 功能 表格 其他\n[BBOX-38] 历\n[BBOX-39] 保存 打印 自动续打 预览 单独打印 手工解锁 隐藏留痕 病历参考 更新数据 首页\n[BBOX-40] 记录\n[BBOX-41] 1:09:45 曾庆星\n[BBOX-42] 医师审核\n[BBOX-43] 录单\n[BBOX-44] 1:10:52 曾庆星\n[BBOX-45] 医师审核\n[BBOX-46] 录单\n[BBOX-47] 1:11:53 曾庆星\n[BBOX-48] 医师审核\n[BBOX-49] 11:12:02 曾庆星\n[BBOX-50] 医师审核\n[BBOX-51] 单(日间...\n[BBOX-52] 11:13:02 曾庆星\n[BBOX-53] 医师审核\n[BBOX-54] 已打印\n[BBOX-55] 11:15:03 曾庆星\n[BBOX-56] 医师审核\n[BBOX-57] 评估表\n[BBOX-58] 16:30:58 曾庆星\n[BBOX-59] 院医师审核\n[BBOX-60] /TE风险评...\n[BBOX-61] 16:32:44 曾庆星\n[BBOX-62] 院医师审核\n[BBOX-63] 后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-2\n[BBOX-64] 2、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我\n[BBOX-65] 院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重\n[BBOX-66] 无明显变化。\n[BBOX-67] 诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利\n[BBOX-68] ，予办理出院手续。\n[BBOX-69] 出院情况：患者未诉不适，神志清，精神可，生命体征平稳。\n[BBOX-70] 出院诊断：\n[BBOX-71] 1.恶性肿瘤免疫治疗\n[BBOX-72] 2.肺恶性肿瘤小细胞肺癌IV期\n[BBOX-73] 3.肺继发恶性肿瘤\n[BBOX-74] 4.冠状动脉粥样硬化性心脏病\n[BBOX-75] 5.胸腔积液\n[BBOX-76] 6.心包积液\n[BBOX-77] 7.肺部感染\n[BBOX-78] 8.腔隙性脑梗死\n[BBOX-79] 9.肾功能检查的异常结果\n[BBOX-80] 1\n[BBOX-81] 100%\n[BBOX-82] 16:57\n[BBOX-83] 2026/3/23\n[BBOX-84] 信阳市中心医院\n[BBOX-85] 免疫病理诊断报告\n[BBOX-86] 免疫组化号：MT25-\n[BBOX-87] 姓名：\n[BBOX-88] 性别：女\n[BBOX-89] 年龄：64岁\n[BBOX-90] 送检医院：\n[BBOX-91] 病区：肿瘤内科五护理单元[东病理号：D25-01313\n[BBOX-92] 就诊卡号：\n[BBOX-93] 住院号：2\n[BBOX-94] 病区床号：21\n[BBOX-95] 送检标本：肺手术标本\n[BBOX-96] 送检时间：2025-01-24\n[BBOX-97] 临床诊断：\n[BBOX-98] 光镜所见：\n[BBOX-99] 免疫病理诊断：\n[BBOX-100] CK广谱（点+），CD56（+），Syn（+），INSM1（+），CK5/6（-），P40（-），TTF1（+），\n[BBOX-101] NapsinA（-），Ki-67（80%+）。\n[BBOX-102] 结合HE及免疫组化结果，（右中间段支气管）肺小细胞神经内分泌癌。\n[BBOX-103] 初诊医师：刘磊\n[BBOX-104] 复诊医师：刘磊\n[BBOX-105] 报告日期：2025-01-26 10:49\n[BBOX-106] 备注：1.本报告单仅供临床参考 2.如临床对报告内容有疑问请与报告医生联系。联系电话：0376-6227723(西院区)，0376-6667570(东院区)。\n[BBOX-107] 3.此报告必须经过病理科医师签字有效。\n[BBOX-108] 信阳市中心医院\n[BBOX-109] 病理检查报告单\n[BBOX-110] 病理号：D25\n[BBOX-111] 姓名：\n[BBOX-112] 性别：女\n[BBOX-113] 年龄：64岁\n[BBOX-114] 送检医院：\n[BBOX-115] 送检科室：呼吸与危重症医学科送检日期：2025-01-22\n[BBOX-116] 门诊号：9\n[BBOX-117] 住院号：25\n[BBOX-118] 床号：21\n[BBOX-119] 送检医师：周鹏飞\n[BBOX-120] 送检标本：右中间段支气管\n[BBOX-121] 临床诊断：\n[BBOX-122] 巨检：灰白色碎组织最大径0.3厘米。全取\n[BBOX-123] 病理诊断：\n[BBOX-124] (右中间段支气管)考虑小细胞癌，已行免疫组化协诊。\n[BBOX-125] 初诊医师：刘晶晶\n[BBOX-126] 复诊医师：刘磊\n[BBOX-127] 报告日期：2025-01-23 19:26\n[BBOX-128] 备注：1.本报告单仅供临床参考 2.如临床对报告内容有疑问请与报告医生联系。联系电话：0376-6227723(西院区)；0376-6667570(东院区)。\n[BBOX-129] 3.此报告必须经过病理科医师签字有效。\n[BBOX-130] 信阳市中心医院\n[BBOX-131] 影像科CT诊断报告书\n[BBOX-132] 扫描\n[BBOX-133] 获取电子胶\n[BBOX-134] 片和报告(试用)\n[BBOX-135] 影像号: 000\n[BBOX-136] 报告日期: 2025-12-22 16:36\n[BBOX-137] 姓名:\n[BBOX-138] 性别: 女\n[BBOX-139] 年龄: 64岁\n[BBOX-140] 检查日期: 2025-12-22\n[BBOX-141] 科别: 日间化疗中心[东院区]院号: 2\n[BBOX-142] 门诊号:/\n[BBOX-143] 检查时间: 09:53:10\n[BBOX-144] 检查方法: 胸部CT平扫,胸部CT增强,上腹部CT平扫,上腹部CT增强,下腹部CT平扫,下腹部CT增强\n[BBOX-145] 技术参数:\n[BBOX-146] 影像学所见:\n[BBOX-147] 双侧胸廓对称,右肺门增大,可见不规则状软组织密度影,密度不均,边\n[BBOX-148] 界不清,强化不均,右肺中下叶支气管稍变窄,双肺可见条索状及结节状高密\n[BBOX-149] 度影,较大病灶位于右肺下叶内基底段见实性结节,大小约为15.8×15.4mm,\n[BBOX-150] 轻度强化。右肺中叶局限性支扩。气管、支气管通畅,右肺门见明显肿大淋巴\n[BBOX-151] 结,轻度强化,双侧胸膜腔及心包腔可见积液征象。与2025-8-21日片比较:\n[BBOX-152] 双侧胸腔积液增多,心包积液新增,右肺门软组织密度影及淋巴结增大。\n[BBOX-153] 肝脏未见明显异常密度及异常强化征象,胆囊内隐约见斑点状高密度影,\n[BBOX-154] 脾脏见数个小灶状低强化影。胰腺形态、大小、密度正常。双肾见小圆形低密\n[BBOX-155] 度影,边界清,增强未见明显强化。腹膜后未见明显增大淋巴结,腹腔未见明\n[BBOX-156] 显积液征象。升结肠见多发小囊袋状外凸影。与2025-8-21日片比较:大致相\n[BBOX-157] 仿。\n[BBOX-158] 影像学意见:\n[BBOX-159] 1. 右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节,转移瘤可能;建\n[BBOX-160] 议追踪复查:右肺门肿大淋巴结。\n[BBOX-161] 2. 双肺慢性炎症,右肺中叶局限性支扩,双侧胸腔积液,心包积液。\n[BBOX-162] 3. 脾脏低密度灶,建议追踪复查。\n[BBOX-163] 4. 胆囊可疑小结石。升结肠多发憩室。\n[BBOX-164] 5. 双肾小囊肿。\n[BBOX-165] 报告医师:\n[BBOX-166] 审核医师:\n[BBOX-167] 此报告仅供临床医师参考,签字生效\n[BBOX-168] 打印时间: 2025-12-22 16:36:26\n[BBOX-169] 信阳市中心医院\n[BBOX-170] 影像科CT诊断报告书\n[BBOX-171] 扫描此二维码可\n[BBOX-172] 电子胶\n[BBOX-173] 片和报告(试用)\n[BBOX-174] 影像号:0000\n[BBOX-175] 报告日期:2026-02-25 15:36\n[BBOX-176] 姓名:\n[BBOX-177] 性别:女\n[BBOX-178] 年龄:65岁\n[BBOX-179] 检查日期:2026-02-25\n[BBOX-180] 科别:肿瘤内科五门诊[东院住院号:/\n[BBOX-181] 门诊号:1\n[BBOX-182] 6\n[BBOX-183] 检查时间:08:57:41\n[BBOX-184] 检查方法:胸部CT平扫加薄层\n[BBOX-185] 技术参数:\n[BBOX-186] 影像学所见:\n[BBOX-187] 双侧胸廓对称,右肺门增大,可见不规则状软组织密度影,密度不均,边\n[BBOX-188] 界不清,右肺中下叶支气管稍变窄,双肺可见条索状及结节状高密度影。右肺\n[BBOX-189] 中叶局限性支扩。气管、支气管通畅,右肺门见明显肿大淋巴结,右侧胸膜局\n[BBOX-190] 部稍厚,双侧胸膜腔及心包腔可见积液征象。与2025-12-22日片比较:右侧胸\n[BBOX-191] 腔积液增多,右肺门软组织密度影及淋巴结进一步增大,右肺结节增大,右侧\n[BBOX-192] 胸膜局部稍增厚。\n[BBOX-193] 影像学意见:\n[BBOX-194] 1.右肺癌并右肺中下叶不张治疗状态。双肺多发结节,转移瘤可能;右肺门\n[BBOX-195] 肿大淋巴结转移。\n[BBOX-196] 2.双肺慢性炎症,双侧胸腔积液,心包积液。\n[BBOX-197] 3.右侧胸膜局部稍厚,不除外转移。\n[BBOX-198] 报告医师:\n[BBOX-199] 肖健\n[BBOX-200] 审核医师:\n[BBOX-201] 贺玲\n[BBOX-202] 此报告仅供临床医师参考,签字生效\n[BBOX-203] 打印时间:2026-02-25 15:36:58\n[BBOX-204] 信阳市中心医院心电图报告单\n[BBOX-205] 门诊号:\n[BBOX-206] 姓名:\n[BBOX-207] P波宽度: 141ms\n[BBOX-208] 诊断: 1.窦性心律\n[BBOX-209] 住院号: 0000\n[BBOX-210] 性别: 女\n[BBOX-211] P-R间期: 181ms\n[BBOX-212] 【120-200】\n[BBOX-213] 2.低电压\n[BBOX-214] 床位号: 04\n[BBOX-215] 年龄: 65岁\n[BBOX-216] QRS时限: 101ms\n[BBOX-217] 【60-110】\n[BBOX-218] 科室: 日间化疗中心[心率: 77bpm\n[BBOX-219] 【60-100】\n[BBOX-220] QT/QTc: 358/406ms\n[BBOX-221] 【360-440】\n[BBOX-222] 东院区]\n[BBOX-223] 电轴: 60°\n[BBOX-224] 【-30-90】\n[BBOX-225] 2026-03-23 08:43:55\n[BBOX-226] 25mm/s 10mm/mV\n[BBOX-227] I\n[BBOX-228] V1\n[BBOX-229] V3R\n[BBOX-230] II\n[BBOX-231] V2\n[BBOX-232] III\n[BBOX-233] V3\n[BBOX-234] V4R\n[BBOX-235] aVR\n[BBOX-236] V4\n[BBOX-237] aVL\n[BBOX-238] V5\n[BBOX-239] V5R\n[BBOX-240] aVF\n[BBOX-241] V6\n[BBOX-242] II\n[BBOX-243] 检查时间: 2026/3/23 8:43:55\n[BBOX-244] 报告时间: 2026/3/23 8:59:30\n[BBOX-245] 报告医生:\n[BBOX-246] 审核医生:\n[BBOX-247] \\begin{tabular}{ccccccccc}\n[BBOX-248] 报告时间: 2026-03-23\n[BBOX-249] \\hline\n[BBOX-250] 序号 & 项目代号 & 项目名称 & 结果 & 单位 & 参考值 \\\\\n[BBOX-251] \\hline\n[BBOX-252] 1 & CEA & 癌胚抗原 & 5.03 & ng/mL & 0—5.2 \\\\\n[BBOX-253] 2 & CYFRA21-1 & 非小细胞肺癌相关抗原 & 4.60 & ng/ml & 0—3.3 \\\\\n[BBOX-254] 3 & NSE & 神经元特异性烯醇化酶测定 & 10.60 & ng/mL & 0—16.3 \\\\\n[BBOX-255] \\hline\n[BBOX-256] \\end{tabular}\n[BBOX-257] \\begin{tabular}{ccccccccc}\n[BBOX-258] 报告时间: 2026-03-23\n[BBOX-259] \\hline\n[BBOX-260] 序 & 代号 & 名称 & 结果 & 参考范围 & 单位 & 序 & 代号 & 名称 & 结果 & 参考范围 & 单位 \\\\\n[BBOX-261] \\hline\n[BBOX-262] 1 & ALT & 谷丙转氨酶 & 52 & ↑ 7—40 & U/L & 18 & CK & 肌酸激酶 & 396 & ↑ 26—192 & U/L \\\\\n[BBOX-263] 2 & AST & 谷草转氨酶 & 54 & ↑ 13—35 & U/L & 19 & CK-MB & 肌酸酶同功酶 & 17.70 & 7—25 & U/L \\\\\n[BBOX-264] 3 & TP & 总蛋白 & 69.8 & 65—85 & g/L & 20 & MYO & 肌红蛋白 & 77.4 & ↑ 0—70 & ug/L \\\\\n[BBOX-265] 4 & ALB & 白蛋白 & 48.5 & 40—55 & g/L & 21 & K & 钾 & 3.74 & 3.5—5.3 & mmol/L \\\\\n[BBOX-266] 5 & GLOB & 球蛋白 & 21.3 & 20—40 & g/L & 22 & NA & 钠 & 132 & ↓ 137—147 & mmol/L \\\\\n[BBOX-267] 6 & A/G & 白球比 & 2.3 & 1.2—2.4 & & 23 & CL & 氯 & 96.0 & ↓ 99—110 & mmol/L \\\\\n[BBOX-268] 7 & TBIL & 总胆红素 & 13.6 & 1.7—21 & umol/L & 24 & CA & 钙 & 2.12 & 2.02—2.6 & mmol/L \\\\\n[BBOX-269] 8 & DBIL & 直接胆红素 & 1.7 & 0—6.8 & umol/L & 25 & CRP & C反应蛋白 & 0.41 & 0—5 & mg/L \\\\\n[BBOX-270] 9 & IBIL & 间接胆红素 & 11.9 & 3—13.6 & umol/L & 26 & eGFR & 估算肾小球滤 & 55.02 & & ml/min \\\\\n[BBOX-271] 10 & ALP & 碱性磷酸酶 & 67 & 50—135 & U/L & & & & & & \\\\\n[BBOX-272] 11 & GGT & 谷氨酰转肽酶 & 19 & 7—45 & U/L & & & & & & \\\\\n[BBOX-273] 12 & UREA & 尿素 & 4.15 & 2.76—8.07 & mmol/L & & & & & & \\\\\n[BBOX-274] 13 & CREA & 肌酐 & 94 & ↑ 45—84 & umol/L & & & & & & \\\\\n[BBOX-275] 14 & UA & 尿酸 & 192 & 143—339 & umol/L & & & & & & \\\\\n[BBOX-276] 15 & CO2 & 二氧化碳 & 25.9 & 22—29 & mmol/L & & & & & & \\\\\n[BBOX-277] 16 & GLU & 葡萄糖 & 6.25 & ↑ 3.8—6.1 & mmol/L & & & & & & \\\\\n[BBOX-278] 17 & LDH & 乳酸脱氢酶 & 291 & ↑ 135—214 & U/L & & & & & & \\\\\n[BBOX-279] \\hline\n[BBOX-280] \\end{tabular}\n[BBOX-281] \\begin{tabular}{llllllllll}\n[BBOX-282] 报告时间: 2026-03-23\n[BBOX-283] \\hline\n[BBOX-284] \\multicolumn{1}{c}{序} & \\multicolumn{1}{c}{代号} & \\multicolumn{1}{c}{项目名称} & \\multicolumn{1}{c}{结果} & \\multicolumn{1}{c}{参考范围} & \\multicolumn{1}{c}{单位} & \\multicolumn{1}{c}{代号} & \\multicolumn{1}{c}{项目名称} & \\multicolumn{1}{c}{结果} & \\multicolumn{1}{c}{参考范围} & \\multicolumn{1}{c}{单位} \\\\\n[BBOX-285] \\hline\n[BBOX-286] 1 & WBC & 白细胞 & 3.62 & 3.5---9.5 & 10^9/L & 15 & MCV & 红细胞平均体积 & 89.4 & 82---100 & fL \\\\\n[BBOX-287] 2 & NEUT & 中性粒细胞百分比 & 68.80 & 40---75 & \\% & 16 & MCH & 平均血红蛋白量 & 30.8 & 27---34 & pg \\\\\n[BBOX-288] 3 & LYMP & 淋巴细胞百分比 & 23.20 & 20---50 & \\% & 17 & MCHC & 平均血红蛋白浓度 & 344 & 316---354 & g/L \\\\\n[BBOX-289] 4 & MONO & 单核细胞百分比 & 4.10 & 3---10 & \\% & 18 & RDW- & 红细胞分布宽度标准 & 43 & 35---56 & fL \\\\\n[BBOX-290] 5 & EOS\\% & 嗜酸性粒细胞百分比 & 2.5 & 0.4---8 & \\% & 19 & RDW- & 红细胞分布宽度变异 & 13 & 11---16 & \\% \\\\\n[BBOX-291] 6 & BASO & 嗜碱性粒细胞百分比 & 1.40 & 0---1 & \\% & 20 & PLT & 血小板 & 155 & 125---350 & 10^9/L \\\\\n[BBOX-292] 7 & NEUT & 中性粒细胞计数 & 2.49 & 1.8---6.3 & 10^9/L & 21 & PDW & 血小板分布宽度 & 10.20 & 9.2---15.6 & fL \\\\\n[BBOX-293] 8 & LYMP & 淋巴细胞计数 & 0.84 & 1.1---3.2 & 10^9/L & 22 & MPV & 平均血小板体积 & 9.90 & 6.5---12 & fL \\\\\n[BBOX-294] 9 & MONO & 单核细胞计数 & 0.15 & 0.1---0.6 & 10^9/L & 23 & PCT & 血小板压积 & 0.150 & 0.108---0.282 & \\% \\\\\n[BBOX-295] 10 & EOS\\# & 嗜酸性粒细胞计数 & 0.09 & 0.02---0.52 & 10^9/L & 24 & P-LC & 大型血小板比率 & 24.00 & 11---45 & \\% \\\\\n[BBOX-296] 11 & BASO & 嗜碱性粒细胞计数 & 0.05 & 0---0.06 & 10^9/L & 25 & PLCC & 大血小板数目 & 37.20 & 30---90 & 10^9/L \\\\\n[BBOX-297] 12 & RBC & 红细胞 & 4.06 & 3.8---5.1 & 10^12/L & & & & & & \\\\\n[BBOX-298] 13 & HGB & 血红蛋白 & 125 & 115---150 & g/L & & & & & & \\\\\n[BBOX-299] 14 & HCT & 红细胞压积 & 36.30 & 35---45 & \\% & & & & & & \\\\\n[BBOX-300] \\hline\n[BBOX-301] \\end{tabular}"
  }
]
2026-08-10 15:53:43,216 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:53:43,237 INFO     29 [SmartSplitter] SmartSplitter done: 9 chunks from 9 LLM segments (all bbox_id). Types: {'DischargeRecord': 1, 'ExaminationReport': 5, 'LabReport': 3}
2026-08-10 15:53:43,246 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 15:53:43,247 INFO     29 [Trace] task=3880a51e | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "302 items", "markdown": "", "text": "", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf", "output_format": "chunks", "chunks": "9 items, types={'DischargeRecord': 1, 'ExaminationReport': 5, 'LabReport': 3}"}
2026-08-10 15:53:43,247 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 15:53:43,247 INFO     29 [ChunkRouter] Routed 9 chunks into 3 groups: {'chunks_Discharge': 1, 'chunks_Examination': 5, 'chunks_LabExam': 3}
2026-08-10 15:53:43,260 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 15:53:43,260 INFO     29 [Trace] task=3880a51e | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | ChunkRouter:Router | outputs={"html": "", "json": "302 items", "markdown": "", "text": "", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf", "output_format": "chunks", "chunks": "9 items, types={'DischargeRecord': 1, 'ExaminationReport': 5, 'LabReport': 3}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 5, \"chunks_LabExam\": 3}"}
2026-08-10 15:53:43,260 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 15:53:43,267 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:53:43,268 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:53:43,268 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[9]
2026-08-10 15:53:43,268 INFO     29 [qwen-vl-table] positions ： [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:53:44,108 INFO     29 [qwen-vl-table] page=9, rect=2376x1500, img=(6600x4167)
2026-08-10 15:53:44,108 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:53:44,108 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 247, \"bbox_end\": 256, \"encounter_dates\": [\"2026-03-23\"], \"department\": \"检验科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2026-03-23\n\\hline\n序号 & 项目代号 & 项目名称 & 结果 & 单位 & 参考值 \\\\\n\\hline\n1 & CEA & 癌胚抗原 & 5.03 & ng/mL & 0—5.2 \\\\\n2 & CYFRA21-1 & 非小细胞肺癌相关抗原 & 4.60 & ng/ml & 0—3.3 \\\\\n3 & NSE & 神经元特异性烯醇化酶测定 & 10.60 & ng/mL & 0—16.3 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 15:53:46,321 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:53:46,321 INFO     29 [qwen-vl-table] page=9 LLM output (len=566):
{
  "report_date": "2026-03-23",
  "items": [
    {
      "name": "癌胚抗原",
      "item_code": "CEA",
      "value": "5.03",
      "unit": "ng/mL",
      "reference_range": "0—5.2",
      "abnormal": false
    },
    {
      "name": "非小细胞肺癌相关抗原",
      "item_code": "CYFRA21-1",
      "value": "4.60",
      "unit": "ng/ml",
      "reference_range": "0—3.3",
      "abnormal": true
    },
    {
      "name": "神经元特异性烯醇化酶测定",
      "item_code": "NSE",
      "value": "10.60",
      "unit": "ng/mL",
      "reference_range": "0—16.3",
      "abnormal": false
    }
  ]
}
2026-08-10 15:53:46,321 INFO     29 [qwen-vl-table] coord grouping: {9: 3}
2026-08-10 15:53:46,340 INFO     29 [qwen-vl-table] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=8287882, prompt_len=535
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
癌胚抗原、非小细胞肺癌相关抗原、神经元特异性烯醇化酶测定

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
2026-08-10 15:53:54,910 INFO     29 [qwen-vl-table] coord API raw response (len=163):
[
	{"text": "癌胚抗原", "bbox": [300, 341, 357, 364]},
	{"text": "非小细胞肺癌相关抗原", "bbox": [300, 371, 441, 394]},
	{"text": "神经元特异性烯醇化酶测定", "bbox": [300, 403, 468, 426]}
]
2026-08-10 15:53:54,910 INFO     29 [qwen-vl-table] coord API: raw_items=3, valid_items=3, elapsed=8.6s
2026-08-10 15:53:54,910 INFO     29 [qwen-vl-table] coord item[0]: text=癌胚抗原, bbox=[300, 341, 357, 364]
2026-08-10 15:53:54,910 INFO     29 [qwen-vl-table] coord item[1]: text=非小细胞肺癌相关抗原, bbox=[300, 371, 441, 394]
2026-08-10 15:53:54,910 INFO     29 [qwen-vl-table] coord item[2]: text=神经元特异性烯醇化酶测定, bbox=[300, 403, 468, 426]
2026-08-10 15:53:54,912 INFO     29 [qwen-vl-table] page=9 coord: matched 3/3, time=8.6s
2026-08-10 15:53:54,912 INFO     29 [qwen-vl-table] new_positions (3):
[[10, 712.8, 848.232, 511.5, 546.0], [10, 712.8, 1047.816, 556.5, 591.0], [10, 712.8, 1111.9679999999998, 604.5, 639.0]]
2026-08-10 15:53:54,912 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=3, matched=3, pages=1, time=11.6s
2026-08-10 15:53:54,916 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:53:54,917 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:53:54,917 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[10]
2026-08-10 15:53:54,917 INFO     29 [qwen-vl-table] positions ： [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:53:55,467 INFO     29 [qwen-vl-table] page=10, rect=2000x1128, img=(5556x3134)
2026-08-10 15:53:55,467 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:53:55,467 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 257, \"bbox_end\": 280, \"encounter_dates\": [\"2026-03-23\"], \"department\": \"检验科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2026-03-23\n\\hline\n序 & 代号 & 名称 & 结果 & 参考范围 & 单位 & 序 & 代号 & 名称 & 结果 & 参考范围 & 单位 \\\\\n\\hline\n1 & ALT & 谷丙转氨酶 & 52 & ↑ 7—40 & U/L & 18 & CK & 肌酸激酶 & 396 & ↑ 26—192 & U/L \\\\\n2 & AST & 谷草转氨酶 & 54 & ↑ 13—35 & U/L & 19 & CK-MB & 肌酸酶同功酶 & 17.70 & 7—25 & U/L \\\\\n3 & TP & 总蛋白 & 69.8 & 65—85 & g/L & 20 & MYO & 肌红蛋白 & 77.4 & ↑ 0—70 & ug/L \\\\\n4 & ALB & 白蛋白 & 48.5 & 40—55 & g/L & 21 & K & 钾 & 3.74 & 3.5—5.3 & mmol/L \\\\\n5 & GLOB & 球蛋白 & 21.3 & 20—40 & g/L & 22 & NA & 钠 & 132 & ↓ 137—147 & mmol/L \\\\\n6 & A/G & 白球比 & 2.3 & 1.2—2.4 & & 23 & CL & 氯 & 96.0 & ↓ 99—110 & mmol/L \\\\\n7 & TBIL & 总胆红素 & 13.6 & 1.7—21 & umol/L & 24 & CA & 钙 & 2.12 & 2.02—2.6 & mmol/L \\\\\n8 & DBIL & 直接胆红素 & 1.7 & 0—6.8 & umol/L & 25 & CRP & C反应蛋白 & 0.41 & 0—5 & mg/L \\\\\n9 & IBIL & 间接胆红素 & 11.9 & 3—13.6 & umol/L & 26 & eGFR & 估算肾小球滤 & 55.02 & & ml/min \\\\\n10 & ALP & 碱性磷酸酶 & 67 & 50—135 & U/L & & & & & & \\\\\n11 & GGT & 谷氨酰转肽酶 & 19 & 7—45 & U/L & & & & & & \\\\\n12 & UREA & 尿素 & 4.15 & 2.76—8.07 & mmol/L & & & & & & \\\\\n13 & CREA & 肌酐 & 94 & ↑ 45—84 & umol/L & & & & & & \\\\\n14 & UA & 尿酸 & 192 & 143—339 & umol/L & & & & & & \\\\\n15 & CO2 & 二氧化碳 & 25.9 & 22—29 & mmol/L & & & & & & \\\\\n16 & GLU & 葡萄糖 & 6.25 & ↑ 3.8—6.1 & mmol/L & & & & & & \\\\\n17 & LDH & 乳酸脱氢酶 & 291 & ↑ 135—214 & U/L & & & & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 15:53:55,470 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:53:55.469+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 70, "failed": 0, "current": {"3880a51e94d311f1bd9827cf206dfa2d": {"id": "3880a51e94d311f1bd9827cf206dfa2d", "doc_id": "37728ffc94d311f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909800, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377033220, "task_type": "dataflow", "root_trace_id": "4dc9fd8a1d244ef89de3e82f6546943d", "root_traceparent": "00-4dc9fd8a1d244ef89de3e82f6546943d-90143aef6fb19019-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:54:09,256 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:54:09,256 INFO     29 [qwen-vl-table] page=10 LLM output (len=4311):
{
  "report_date": "2026-03-23",
  "items": [
    {
      "name": "谷丙转氨酶",
      "item_code": "ALT",
      "value": "52",
      "unit": "U/L",
      "reference_range": "7—40",
      "abnormal": true
    },
    {
      "name": "谷草转氨酶",
      "item_code": "AST",
      "value": "54",
      "unit": "U/L",
      "reference_range": "13—35",
      "abnormal": true
    },
    {
      "name": "总蛋白",
      "item_code": "TP",
      "value": "69.8",
      "unit": "g/L",
      "reference_range": "65—85",
      "abnormal": false
    },
    {
      "name": "白蛋白",
      "item_code": "ALB",
      "value": "48.5",
      "unit": "g/L",
      "reference_range": "40—55",
      "abnormal": false
    },
    {
      "name": "球蛋白",
      "item_code": "GLOB",
      "value": "21.3",
      "unit": "g/L",
      "reference_range": "20—40",
      "abnormal": false
    },
    {
      "name": "白球比",
      "item_code": "A/G",
      "value": "2.3",
      "unit": null,
      "reference_range": "1.2—2.4",
      "abnormal": false
    },
    {
      "name": "总胆红素",
      "item_code": "TBIL",
      "value": "13.6",
      "unit": "umol/L",
      "reference_range": "1.7—21",
      "abnormal": false
    },
    {
      "name": "直接胆红素",
      "item_code": "DBIL",
      "value": "1.7",
      "unit": "umol/L",
      "reference_range": "0—6.8",
      "abnormal": false
    },
    {
      "name": "间接胆红素",
      "item_code": "IBIL",
      "value": "11.9",
      "unit": "umol/L",
      "reference_range": "3—13.6",
      "abnormal": false
    },
    {
      "name": "碱性磷酸酶",
      "item_code": "ALP",
      "value": "67",
      "unit": "U/L",
      "reference_range": "50—135",
      "abnormal": false
    },
    {
      "name": "谷氨酰转肽酶",
      "item_code": "GGT",
      "value": "19",
      "unit": "U/L",
      "reference_range": "7—45",
      "abnormal": false
    },
    {
      "name": "尿素",
      "item_code": "UREA",
      "value": "4.15",
      "unit": "mmol/L",
      "reference_range": "2.76—8.07",
      "abnormal": false
    },
    {
      "name": "肌酐",
      "item_code": "CREA",
      "value": "94",
      "unit": "umol/L",
      "reference_range": "45—84",
      "abnormal": true
    },
    {
      "name": "尿酸",
      "item_code": "UA",
      "value": "192",
      "unit": "umol/L",
      "reference_range": "143—339",
      "abnormal": false
    },
    {
      "name": "二氧化碳",
      "item_code": "CO2",
      "value": "25.9",
      "unit": "mmol/L",
      "reference_range": "22—29",
      "abnormal": false
    },
    {
      "name": "葡萄糖",
      "item_code": "GLU",
      "value": "6.25",
      "unit": "mmol/L",
      "reference_range": "3.8—6.1",
      "abnormal": true
    },
    {
      "name": "乳酸脱氢酶",
      "item_code": "LDH",
      "value": "291",
      "unit": "U/L",
      "reference_range": "135—214",
      "abnormal": true
    },
    {
      "name": "肌酸激酶",
      "item_code": "CK",
      "value": "396",
      "unit": "U/L",
      "reference_range": "26—192",
      "abnormal": true
    },
    {
      "name": "肌酸酶同功酶",
      "item_code": "CK-MB",
      "value": "17.70",
      "unit": "U/L",
      "reference_range": "7—25",
      "abnormal": false
    },
    {
      "name": "肌红蛋白",
      "item_code": "MYO",
      "value": "77.4",
      "unit": "ug/L",
      "reference_range": "0—70",
      "abnormal": true
    },
    {
      "name": "钾",
      "item_code": "K",
      "value": "3.74",
      "unit": "mmol/L",
      "reference_range": "3.5—5.3",
      "abnormal": false
    },
    {
      "name": "钠",
      "item_code": "NA",
      "value": "132",
      "unit": "mmol/L",
      "reference_range": "137—147",
      "abnormal": true
    },
    {
      "name": "氯",
      "item_code": "CL",
      "value": "96.0",
      "unit": "mmol/L",
      "reference_range": "99—110",
      "abnormal": true
    },
    {
      "name": "钙",
      "item_code": "CA",
      "value": "2.12",
      "unit": "mmol/L",
      "reference_range": "2.02—2.6",
      "abnormal": false
    },
    {
      "name": "C反应蛋白",
      "item_code": "CRP",
      "value": "0.41",
      "unit": "mg/L",
      "reference_range": "0—5",
      "abnormal": false
    },
    {
      "name": "估算肾小球滤",
      "item_code": "eGFR",
      "value": "55.02",
      "unit": "ml/min",
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-10 15:54:09,256 INFO     29 [qwen-vl-table] coord grouping: {10: 26}
2026-08-10 15:54:09,272 INFO     29 [qwen-vl-table] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=6710078, prompt_len=626
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
谷丙转氨酶、谷草转氨酶、总蛋白、白蛋白、球蛋白、白球比、总胆红素、直接胆红素、间接胆红素、碱性磷酸酶、谷氨酰转肽酶、尿素、肌酐、尿酸、二氧化碳、葡萄糖、乳酸脱氢酶、肌酸激酶、肌酸酶同功酶、肌红蛋白、钾、钠、氯、钙、C反应蛋白、估算肾小球滤

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
2026-08-10 15:54:23,810 INFO     29 [qwen-vl-table] coord API raw response (len=1266):
[
	{"text": "谷丙转氨酶", "bbox": [213, 264, 288, 291]},
	{"text": "谷草转氨酶", "bbox": [213, 300, 288, 327]},
	{"text": "总蛋白", "bbox": [213, 338, 258, 365]},
	{"text": "白蛋白", "bbox": [213, 374, 258, 400]},
	{"text": "球蛋白", "bbox": [213, 412, 258, 438]},
	{"text": "白球比", "bbox": [213, 448, 258, 474]},
	{"text": "总胆红素", "bbox": [213, 485, 274, 511]},
	{"text": "直接胆红素", "bbox": [213, 521, 288, 548]},
	{"text": "间接胆红素", "bbox": [213, 558, 288, 585]},
	{"text": "碱性磷酸酶", "bbox": [213, 595, 288, 621]},
	{"text": "谷氨酰转肽酶", "bbox": [213, 633, 304, 660]},
	{"text": "尿素", "bbox": [213, 670, 245, 696]},
	{"text": "肌酐", "bbox": [213, 707, 245, 733]},
	{"text": "尿酸", "bbox": [213, 743, 245, 770]},
	{"text": "二氧化碳", "bbox": [213, 780, 274, 807]},
	{"text": "葡萄糖", "bbox": [213, 817, 258, 843]},
	{"text": "乳酸脱氢酶", "bbox": [213, 854, 290, 880]},
	{"text": "肌酸激酶", "bbox": [578, 262, 637, 288]},
	{"text": "肌酸酶同功酶", "bbox": [578, 298, 667, 325]},
	{"text": "肌红蛋白", "bbox": [578, 335, 637, 362]},
	{"text": "钾", "bbox": [578, 372, 594, 398]},
	{"text": "钠", "bbox": [578, 409, 594, 435]},
	{"text": "氯", "bbox": [578, 445, 594, 471]},
	{"text": "钙", "bbox": [578, 482, 594, 508]},
	{"text": "C反应蛋白", "bbox": [578, 518, 645, 545]},
	{"text": "估算肾小球滤", "bbox": [578, 555, 667, 581]}
]
2026-08-10 15:54:23,810 INFO     29 [qwen-vl-table] coord API: raw_items=26, valid_items=26, elapsed=14.5s
2026-08-10 15:54:23,810 INFO     29 [qwen-vl-table] coord item[0]: text=谷丙转氨酶, bbox=[213, 264, 288, 291]
2026-08-10 15:54:23,810 INFO     29 [qwen-vl-table] coord item[1]: text=谷草转氨酶, bbox=[213, 300, 288, 327]
2026-08-10 15:54:23,810 INFO     29 [qwen-vl-table] coord item[2]: text=总蛋白, bbox=[213, 338, 258, 365]
2026-08-10 15:54:23,810 INFO     29 [qwen-vl-table] coord item[3]: text=白蛋白, bbox=[213, 374, 258, 400]
2026-08-10 15:54:23,810 INFO     29 [qwen-vl-table] coord item[4]: text=球蛋白, bbox=[213, 412, 258, 438]
2026-08-10 15:54:23,810 INFO     29 [qwen-vl-table] coord item[5]: text=白球比, bbox=[213, 448, 258, 474]
2026-08-10 15:54:23,811 INFO     29 [qwen-vl-table] coord item[6]: text=总胆红素, bbox=[213, 485, 274, 511]
2026-08-10 15:54:23,811 INFO     29 [qwen-vl-table] coord item[7]: text=直接胆红素, bbox=[213, 521, 288, 548]
2026-08-10 15:54:23,811 INFO     29 [qwen-vl-table] coord item[8]: text=间接胆红素, bbox=[213, 558, 288, 585]
2026-08-10 15:54:23,811 INFO     29 [qwen-vl-table] coord item[9]: text=碱性磷酸酶, bbox=[213, 595, 288, 621]
2026-08-10 15:54:23,811 INFO     29 [qwen-vl-table] coord item[10]: text=谷氨酰转肽酶, bbox=[213, 633, 304, 660]
2026-08-10 15:54:23,811 INFO     29 [qwen-vl-table] coord item[11]: text=尿素, bbox=[213, 670, 245, 696]
2026-08-10 15:54:23,811 INFO     29 [qwen-vl-table] coord item[12]: text=肌酐, bbox=[213, 707, 245, 733]
2026-08-10 15:54:23,811 INFO     29 [qwen-vl-table] coord item[13]: text=尿酸, bbox=[213, 743, 245, 770]
2026-08-10 15:54:23,811 INFO     29 [qwen-vl-table] coord item[14]: text=二氧化碳, bbox=[213, 780, 274, 807]
2026-08-10 15:54:23,811 INFO     29 [qwen-vl-table] coord item[15]: text=葡萄糖, bbox=[213, 817, 258, 843]
2026-08-10 15:54:23,811 INFO     29 [qwen-vl-table] coord item[16]: text=乳酸脱氢酶, bbox=[213, 854, 290, 880]
2026-08-10 15:54:23,811 INFO     29 [qwen-vl-table] coord item[17]: text=肌酸激酶, bbox=[578, 262, 637, 288]
2026-08-10 15:54:23,811 INFO     29 [qwen-vl-table] coord item[18]: text=肌酸酶同功酶, bbox=[578, 298, 667, 325]
2026-08-10 15:54:23,811 INFO     29 [qwen-vl-table] coord item[19]: text=肌红蛋白, bbox=[578, 335, 637, 362]
2026-08-10 15:54:23,811 INFO     29 [qwen-vl-table] coord item[20]: text=钾, bbox=[578, 372, 594, 398]
2026-08-10 15:54:23,811 INFO     29 [qwen-vl-table] coord item[21]: text=钠, bbox=[578, 409, 594, 435]
2026-08-10 15:54:23,811 INFO     29 [qwen-vl-table] coord item[22]: text=氯, bbox=[578, 445, 594, 471]
2026-08-10 15:54:23,811 INFO     29 [qwen-vl-table] coord item[23]: text=钙, bbox=[578, 482, 594, 508]
2026-08-10 15:54:23,811 INFO     29 [qwen-vl-table] coord item[24]: text=C反应蛋白, bbox=[578, 518, 645, 545]
2026-08-10 15:54:23,811 INFO     29 [qwen-vl-table] coord item[25]: text=估算肾小球滤, bbox=[578, 555, 667, 581]
2026-08-10 15:54:23,812 INFO     29 [qwen-vl-table] page=10 coord: matched 26/26, time=14.5s
2026-08-10 15:54:23,812 INFO     29 [qwen-vl-table] new_positions (26):
[[11, 426.0, 576.0, 297.792, 328.248], [11, 426.0, 576.0, 338.4, 368.85599999999994], [11, 426.0, 516.0, 381.26399999999995, 411.71999999999997], [11, 426.0, 516.0, 421.87199999999996, 451.19999999999993], [11, 426.0, 516.0, 464.73599999999993, 494.06399999999996], [11, 426.0, 516.0, 505.34399999999994, 534.6719999999999], [11, 426.0, 548.0, 547.0799999999999, 576.4079999999999], [11, 426.0, 576.0, 587.688, 618.1439999999999], [11, 426.0, 576.0, 629.424, 659.8799999999999], [11, 426.0, 576.0, 671.16, 700.4879999999999], [11, 426.0, 608.0, 714.0239999999999, 744.4799999999999], [11, 426.0, 490.0, 755.7599999999999, 785.088], [11, 426.0, 490.0, 797.4959999999999, 826.824], [11, 426.0, 490.0, 838.1039999999999, 868.56], [11, 426.0, 548.0, 879.8399999999999, 910.2959999999999], [11, 426.0, 516.0, 921.5759999999999, 950.9039999999999], [11, 426.0, 580.0, 963.3119999999999, 992.6399999999999], [11, 1156.0, 1274.0, 295.53599999999994, 324.864], [11, 1156.0, 1334.0, 336.14399999999995, 366.59999999999997], [11, 1156.0, 1274.0, 377.87999999999994, 408.33599999999996], [11, 1156.0, 1188.0, 419.616, 448.94399999999996], [11, 1156.0, 1188.0, 461.352, 490.67999999999995], [11, 1156.0, 1188.0, 501.96, 531.2879999999999], [11, 1156.0, 1188.0, 543.6959999999999, 573.024], [11, 1156.0, 1290.0, 584.304, 614.76], [11, 1156.0, 1334.0, 626.04, 655.3679999999999]]
2026-08-10 15:54:23,812 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=26, matched=26, pages=1, time=28.9s
2026-08-10 15:54:23,815 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:54:23,816 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:54:23,816 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[11]
2026-08-10 15:54:23,816 INFO     29 [qwen-vl-table] positions ： [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:54:24,225 INFO     29 [qwen-vl-table] page=11, rect=1572x1104, img=(4367x3067)
2026-08-10 15:54:24,226 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:54:24,227 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 281, \"bbox_end\": 301, \"encounter_dates\": [\"2026-03-23\"], \"department\": \"检验科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllllll}\n报告时间: 2026-03-23\n\\hline\n\\multicolumn{1}{c}{序} & \\multicolumn{1}{c}{代号} & \\multicolumn{1}{c}{项目名称} & \\multicolumn{1}{c}{结果} & \\multicolumn{1}{c}{参考范围} & \\multicolumn{1}{c}{单位} & \\multicolumn{1}{c}{代号} & \\multicolumn{1}{c}{项目名称} & \\multicolumn{1}{c}{结果} & \\multicolumn{1}{c}{参考范围} & \\multicolumn{1}{c}{单位} \\\\\n\\hline\n1 & WBC & 白细胞 & 3.62 & 3.5---9.5 & 10^9/L & 15 & MCV & 红细胞平均体积 & 89.4 & 82---100 & fL \\\\\n2 & NEUT & 中性粒细胞百分比 & 68.80 & 40---75 & \\% & 16 & MCH & 平均血红蛋白量 & 30.8 & 27---34 & pg \\\\\n3 & LYMP & 淋巴细胞百分比 & 23.20 & 20---50 & \\% & 17 & MCHC & 平均血红蛋白浓度 & 344 & 316---354 & g/L \\\\\n4 & MONO & 单核细胞百分比 & 4.10 & 3---10 & \\% & 18 & RDW- & 红细胞分布宽度标准 & 43 & 35---56 & fL \\\\\n5 & EOS\\% & 嗜酸性粒细胞百分比 & 2.5 & 0.4---8 & \\% & 19 & RDW- & 红细胞分布宽度变异 & 13 & 11---16 & \\% \\\\\n6 & BASO & 嗜碱性粒细胞百分比 & 1.40 & 0---1 & \\% & 20 & PLT & 血小板 & 155 & 125---350 & 10^9/L \\\\\n7 & NEUT & 中性粒细胞计数 & 2.49 & 1.8---6.3 & 10^9/L & 21 & PDW & 血小板分布宽度 & 10.20 & 9.2---15.6 & fL \\\\\n8 & LYMP & 淋巴细胞计数 & 0.84 & 1.1---3.2 & 10^9/L & 22 & MPV & 平均血小板体积 & 9.90 & 6.5---12 & fL \\\\\n9 & MONO & 单核细胞计数 & 0.15 & 0.1---0.6 & 10^9/L & 23 & PCT & 血小板压积 & 0.150 & 0.108---0.282 & \\% \\\\\n10 & EOS\\# & 嗜酸性粒细胞计数 & 0.09 & 0.02---0.52 & 10^9/L & 24 & P-LC & 大型血小板比率 & 24.00 & 11---45 & \\% \\\\\n11 & BASO & 嗜碱性粒细胞计数 & 0.05 & 0---0.06 & 10^9/L & 25 & PLCC & 大血小板数目 & 37.20 & 30---90 & 10^9/L \\\\\n12 & RBC & 红细胞 & 4.06 & 3.8---5.1 & 10^12/L & & & & & & \\\\\n13 & HGB & 血红蛋白 & 125 & 115---150 & g/L & & & & & & \\\\\n14 & HCT & 红细胞压积 & 36.30 & 35---45 & \\% & & & & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 15:54:26,255 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:54:26.253+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 70, "failed": 0, "current": {"3880a51e94d311f1bd9827cf206dfa2d": {"id": "3880a51e94d311f1bd9827cf206dfa2d", "doc_id": "37728ffc94d311f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909800, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377033220, "task_type": "dataflow", "root_trace_id": "4dc9fd8a1d244ef89de3e82f6546943d", "root_traceparent": "00-4dc9fd8a1d244ef89de3e82f6546943d-90143aef6fb19019-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:54:39,869 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:54:39,869 INFO     29 [qwen-vl-table] page=11 LLM output (len=4286):
{
  "report_date": "2026-03-23",
  "items": [
    {
      "name": "白细胞",
      "item_code": "WBC",
      "value": "3.62",
      "unit": "10^9/L",
      "reference_range": "3.5---9.5",
      "abnormal": false
    },
    {
      "name": "中性粒细胞百分比",
      "item_code": "NEUT",
      "value": "68.80",
      "unit": "%",
      "reference_range": "40---75",
      "abnormal": false
    },
    {
      "name": "淋巴细胞百分比",
      "item_code": "LYMP",
      "value": "23.20",
      "unit": "%",
      "reference_range": "20---50",
      "abnormal": false
    },
    {
      "name": "单核细胞百分比",
      "item_code": "MONO",
      "value": "4.10",
      "unit": "%",
      "reference_range": "3---10",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞百分比",
      "item_code": "EOS%",
      "value": "2.5",
      "unit": "%",
      "reference_range": "0.4---8",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞百分比",
      "item_code": "BASO",
      "value": "1.40",
      "unit": "%",
      "reference_range": "0---1",
      "abnormal": true
    },
    {
      "name": "中性粒细胞计数",
      "item_code": "NEUT",
      "value": "2.49",
      "unit": "10^9/L",
      "reference_range": "1.8---6.3",
      "abnormal": false
    },
    {
      "name": "淋巴细胞计数",
      "item_code": "LYMP",
      "value": "0.84",
      "unit": "10^9/L",
      "reference_range": "1.1---3.2",
      "abnormal": true
    },
    {
      "name": "单核细胞计数",
      "item_code": "MONO",
      "value": "0.15",
      "unit": "10^9/L",
      "reference_range": "0.1---0.6",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞计数",
      "item_code": "EOS#",
      "value": "0.09",
      "unit": "10^9/L",
      "reference_range": "0.02---0.52",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞计数",
      "item_code": "BASO",
      "value": "0.05",
      "unit": "10^9/L",
      "reference_range": "0---0.06",
      "abnormal": false
    },
    {
      "name": "红细胞",
      "item_code": "RBC",
      "value": "4.06",
      "unit": "10^12/L",
      "reference_range": "3.8---5.1",
      "abnormal": false
    },
    {
      "name": "血红蛋白",
      "item_code": "HGB",
      "value": "125",
      "unit": "g/L",
      "reference_range": "115---150",
      "abnormal": false
    },
    {
      "name": "红细胞压积",
      "item_code": "HCT",
      "value": "36.30",
      "unit": "%",
      "reference_range": "35---45",
      "abnormal": false
    },
    {
      "name": "红细胞平均体积",
      "item_code": "MCV",
      "value": "89.4",
      "unit": "fL",
      "reference_range": "82---100",
      "abnormal": false
    },
    {
      "name": "平均血红蛋白量",
      "item_code": "MCH",
      "value": "30.8",
      "unit": "pg",
      "reference_range": "27---34",
      "abnormal": false
    },
    {
      "name": "平均血红蛋白浓度",
      "item_code": "MCHC",
      "value": "344",
      "unit": "g/L",
      "reference_range": "316---354",
      "abnormal": false
    },
    {
      "name": "红细胞分布宽度标准",
      "item_code": "RDW-",
      "value": "43",
      "unit": "fL",
      "reference_range": "35---56",
      "abnormal": false
    },
    {
      "name": "红细胞分布宽度变异",
      "item_code": "RDW-",
      "value": "13",
      "unit": "%",
      "reference_range": "11---16",
      "abnormal": false
    },
    {
      "name": "血小板",
      "item_code": "PLT",
      "value": "155",
      "unit": "10^9/L",
      "reference_range": "125---350",
      "abnormal": false
    },
    {
      "name": "血小板分布宽度",
      "item_code": "PDW",
      "value": "10.20",
      "unit": "fL",
      "reference_range": "9.2---15.6",
      "abnormal": false
    },
    {
      "name": "平均血小板体积",
      "item_code": "MPV",
      "value": "9.90",
      "unit": "fL",
      "reference_range": "6.5---12",
      "abnormal": false
    },
    {
      "name": "血小板压积",
      "item_code": "PCT",
      "value": "0.150",
      "unit": "%",
      "reference_range": "0.108---0.282",
      "abnormal": false
    },
    {
      "name": "大型血小板比率",
      "item_code": "P-LC",
      "value": "24.00",
      "unit": "%",
      "reference_range": "11---45",
      "abnormal": false
    },
    {
      "name": "大血小板数目",
      "item_code": "PLCC",
      "value": "37.20",
      "unit": "10^9/L",
      "reference_range": "30---90",
      "abnormal": false
    }
  ]
}
2026-08-10 15:54:39,870 INFO     29 [qwen-vl-table] coord grouping: {11: 25}
2026-08-10 15:54:39,884 INFO     29 [qwen-vl-table] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5705072, prompt_len=696
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
白细胞、中性粒细胞百分比、淋巴细胞百分比、单核细胞百分比、嗜酸性粒细胞百分比、嗜碱性粒细胞百分比、中性粒细胞计数、淋巴细胞计数、单核细胞计数、嗜酸性粒细胞计数、嗜碱性粒细胞计数、红细胞、血红蛋白、红细胞压积、红细胞平均体积、平均血红蛋白量、平均血红蛋白浓度、红细胞分布宽度标准、红细胞分布宽度变异、血小板、血小板分布宽度、平均血小板体积、血小板压积、大型血小板比率、大血小板数目

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
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord API raw response (len=1285):
[
	{"text": "白细胞", "bbox": [111, 252, 160, 274]},
	{"text": "中性粒细胞百分比", "bbox": [111, 284, 245, 307]},
	{"text": "淋巴细胞百分比", "bbox": [100, 315, 227, 338]},
	{"text": "单核细胞百分比", "bbox": [99, 346, 227, 369]},
	{"text": "嗜酸性粒细胞百分比", "bbox": [100, 378, 262, 400]},
	{"text": "嗜碱性粒细胞百分比", "bbox": [75, 409, 262, 431]},
	{"text": "中性粒细胞计数", "bbox": [75, 440, 228, 463]},
	{"text": "淋巴细胞计数", "bbox": [75, 471, 211, 493]},
	{"text": "单核细胞计数", "bbox": [75, 502, 211, 524]},
	{"text": "嗜酸性粒细胞计数", "bbox": [75, 533, 245, 555]},
	{"text": "嗜碱性粒细胞计数", "bbox": [75, 564, 245, 586]},
	{"text": "红细胞", "bbox": [111, 595, 160, 617]},
	{"text": "血红蛋白", "bbox": [111, 626, 177, 648]},
	{"text": "红细胞压积", "bbox": [111, 657, 195, 679]},
	{"text": "红细胞平均体积", "bbox": [572, 257, 691, 279]},
	{"text": "平均血红蛋白量", "bbox": [572, 288, 691, 310]},
	{"text": "平均血红蛋白浓度", "bbox": [572, 320, 708, 342]},
	{"text": "红细胞分布宽度标准", "bbox": [572, 351, 724, 373]},
	{"text": "红细胞分布宽度变异", "bbox": [572, 382, 724, 404]},
	{"text": "血小板", "bbox": [572, 413, 622, 435]},
	{"text": "血小板分布宽度", "bbox": [572, 444, 691, 466]},
	{"text": "平均血小板体积", "bbox": [572, 475, 691, 497]},
	{"text": "血小板压积", "bbox": [572, 506, 657, 528]},
	{"text": "大型血小板比率", "bbox": [572, 537, 691, 559]},
	{"text": "大血小板数目", "bbox": [572, 568, 672, 590]}
]
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord API: raw_items=25, valid_items=25, elapsed=11.8s
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord item[0]: text=白细胞, bbox=[111, 252, 160, 274]
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord item[1]: text=中性粒细胞百分比, bbox=[111, 284, 245, 307]
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord item[2]: text=淋巴细胞百分比, bbox=[100, 315, 227, 338]
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord item[3]: text=单核细胞百分比, bbox=[99, 346, 227, 369]
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord item[4]: text=嗜酸性粒细胞百分比, bbox=[100, 378, 262, 400]
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord item[5]: text=嗜碱性粒细胞百分比, bbox=[75, 409, 262, 431]
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord item[6]: text=中性粒细胞计数, bbox=[75, 440, 228, 463]
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord item[7]: text=淋巴细胞计数, bbox=[75, 471, 211, 493]
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord item[8]: text=单核细胞计数, bbox=[75, 502, 211, 524]
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord item[9]: text=嗜酸性粒细胞计数, bbox=[75, 533, 245, 555]
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord item[10]: text=嗜碱性粒细胞计数, bbox=[75, 564, 245, 586]
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord item[11]: text=红细胞, bbox=[111, 595, 160, 617]
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord item[12]: text=血红蛋白, bbox=[111, 626, 177, 648]
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord item[13]: text=红细胞压积, bbox=[111, 657, 195, 679]
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord item[14]: text=红细胞平均体积, bbox=[572, 257, 691, 279]
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord item[15]: text=平均血红蛋白量, bbox=[572, 288, 691, 310]
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord item[16]: text=平均血红蛋白浓度, bbox=[572, 320, 708, 342]
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord item[17]: text=红细胞分布宽度标准, bbox=[572, 351, 724, 373]
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord item[18]: text=红细胞分布宽度变异, bbox=[572, 382, 724, 404]
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord item[19]: text=血小板, bbox=[572, 413, 622, 435]
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord item[20]: text=血小板分布宽度, bbox=[572, 444, 691, 466]
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord item[21]: text=平均血小板体积, bbox=[572, 475, 691, 497]
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord item[22]: text=血小板压积, bbox=[572, 506, 657, 528]
2026-08-10 15:54:51,688 INFO     29 [qwen-vl-table] coord item[23]: text=大型血小板比率, bbox=[572, 537, 691, 559]
2026-08-10 15:54:51,689 INFO     29 [qwen-vl-table] coord item[24]: text=大血小板数目, bbox=[572, 568, 672, 590]
2026-08-10 15:54:51,690 INFO     29 [qwen-vl-table] page=11 coord: matched 25/25, time=11.8s
2026-08-10 15:54:51,690 INFO     29 [qwen-vl-table] new_positions (25):
[[12, 174.49200000000002, 251.52, 278.208, 302.49600000000004], [12, 174.49200000000002, 385.14000000000004, 313.536, 338.92800000000005], [12, 157.20000000000002, 356.844, 347.76000000000005, 373.15200000000004], [12, 155.62800000000001, 356.844, 381.98400000000004, 407.37600000000003], [12, 157.20000000000002, 411.86400000000003, 417.312, 441.6], [12, 117.9, 411.86400000000003, 451.53600000000006, 475.824], [12, 117.9, 358.416, 485.76000000000005, 511.15200000000004], [12, 117.9, 331.692, 519.984, 544.272], [12, 117.9, 331.692, 554.2080000000001, 578.4960000000001], [12, 117.9, 385.14000000000004, 588.432, 612.72], [12, 117.9, 385.14000000000004, 622.6560000000001, 646.9440000000001], [12, 174.49200000000002, 251.52, 656.8800000000001, 681.168], [12, 174.49200000000002, 278.244, 691.104, 715.392], [12, 174.49200000000002, 306.54, 725.3280000000001, 749.6160000000001], [12, 899.1840000000001, 1086.252, 283.728, 308.016], [12, 899.1840000000001, 1086.252, 317.952, 342.24], [12, 899.1840000000001, 1112.976, 353.28000000000003, 377.56800000000004], [12, 899.1840000000001, 1138.1280000000002, 387.504, 411.79200000000003], [12, 899.1840000000001, 1138.1280000000002, 421.728, 446.016], [12, 899.1840000000001, 977.784, 455.95200000000006, 480.24000000000007], [12, 899.1840000000001, 1086.252, 490.17600000000004, 514.464], [12, 899.1840000000001, 1086.252, 524.4000000000001, 548.6880000000001], [12, 899.1840000000001, 1032.804, 558.624, 582.912], [12, 899.1840000000001, 1086.252, 592.8480000000001, 617.1360000000001], [12, 899.1840000000001, 1056.384, 627.072, 651.36]]
2026-08-10 15:54:51,690 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=25, matched=25, pages=1, time=27.9s
2026-08-10 15:54:51,705 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 15:54:51,705 INFO     29 [Trace] task=3880a51e | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | Extractor:LabExam | outputs={"chunks": "3 items, types={'LabReport': 3}", "html": "", "json": "302 items", "markdown": "", "text": "", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 5, \"chunks_LabExam\": 3}"}
2026-08-10 15:54:51,705 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 15:54:51,711 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:54:51,711 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 15:54:52,485 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:54:52,495 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 15:54:52,495 INFO     29 [Trace] task=3880a51e | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "302 items", "markdown": "", "text": "", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 5, \"chunks_LabExam\": 3}"}
2026-08-10 15:54:52,495 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 15:54:52,501 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:54:52,501 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 15:54:52,999 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:54:53,015 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 15:54:53,016 INFO     29 [Trace] task=3880a51e | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | Extractor:Clinical | outputs={"chunks": "1 items", "html": "", "json": "302 items", "markdown": "", "text": "", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 5, \"chunks_LabExam\": 3}"}
2026-08-10 15:54:53,016 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 15:54:53,030 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:54:53,031 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 15:54:53,711 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:54:53,724 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 15:54:53,724 INFO     29 [Trace] task=3880a51e | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "302 items", "markdown": "", "text": "", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 5, \"chunks_LabExam\": 3}"}
2026-08-10 15:54:53,724 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 15:54:53,739 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:54:53,739 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 15:54:54,186 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:54:54,197 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 15:54:54,197 INFO     29 [Trace] task=3880a51e | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "302 items", "markdown": "", "text": "", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 5, \"chunks_LabExam\": 3}"}
2026-08-10 15:54:54,197 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 15:54:54,206 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:54:54,207 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:54:54,207 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 15:54:54,207 INFO     29 [qwen-vl-text] positions(82): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:54:54,207 INFO     29 [qwen-vl-text] page grouping: [0, 1, 2, 3], lines per page: [7, 22, 1, 52]
2026-08-10 15:54:54,675 INFO     29 [qwen-vl-text] page=0, rect=2259x1732, img=(6276x4812), dpi=200
2026-08-10 15:54:55,570 INFO     29 [qwen-vl-text] page=1, rect=2260x1732, img=(6278x4812), dpi=200
2026-08-10 15:54:56,266 INFO     29 [qwen-vl-text] page=2, rect=2196x1384, img=(6100x3845), dpi=200
2026-08-10 15:54:57,082 INFO     29 [qwen-vl-text] page=3, rect=2220x1532, img=(6167x4256), dpi=200
2026-08-10 15:54:57,086 INFO     29 [qwen-vl-text] LLM extraction start, text_len=2615
2026-08-10 15:54:57,086 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:54:57,086 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 0, \"bbox_end\": 81, \"encounter_dates\": [\"2026-03-23\"], \"department\": \"日间化疗中心\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "2025.1 确诊小细胞癌，已行免疫组化协诊\n2025-.2-4给予”EP”化疗联合”特瑞普利单抗”免疫治疗3周期，\n2025-04-22给予”EP”方案化疗联合\n“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗\n2025.5-8行“特瑞普利单抗”免疫治疗4周期\n2025.8 PD\n2025.8-2026.2“替雷利珠单抗联合安罗替尼”免疫治疗\n信阳市中心医院\n日间化疗出入院记录\n姓名：\n性别：女年龄：65岁\n科别：日间化疗中心[东院床号：04\n区]\n登记号：0000\n住院号：25\n入院时间：2026年03月23日 08:29:00出院时间：2026年03月23日 11:14:00\n住院天数：1天\n主诉：确诊肺癌1年余\n入院情况：1年余前因“胸闷”就诊我院，2025-01-17CT增强64：1.右肺门占位，考虑恶性病变并\n右肺中下叶不张，右下肺动受侵可能。2.双肺纤维索条灶。双肺多发小结节，转移待排。3.右侧\n胸腔少量积液。4.双肾小囊肿。5.升结肠多发憩室。6.子宫后壁肌瘤可能。7.冠状动脉CTA未见明\n显异常。2025-01-23行纤支镜下肺活检，2025-01-23活体组织病理申请 诊断意见：(右中间段支\n气管)考虑小细胞癌，已行免疫组化协诊。2025-01-26免疫组化申请：CK广谱（点+），CD56（+），\nSyn（+），INSM1（+），CK5/6（-），P40（-），TTF1（+），NapsinA（-），Ki-67（80%+）。结合HE\n及免疫组化结果，（右中间段支气管）肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04\n-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期，2025-04-22给予“EP”方案化疗联合\n“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗。2025-05-19、2025\n-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加增强\n(胸部.上腹部.下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节。\n胸腔少量积液。4.双肾小囊肿。5.升结肠多发息室。6.丁台加壁肌瘤可能。冠状动脉CT示无明显异常。2025-01-23行纤支镜下肺活检，2025-01-23活体组织病理申请 诊断意见：(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。2025-01-26免疫组化申请：CK广谱(点+)，CD56(+)，Syn(+)，INSM1(+)，CK5/6(-)，P40(-)，TTF1(+)，NapsinA(-)，Ki-67(80%)。结合HE及免疫组化结果，(右中间段支气管)肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期，2025-04-22给予“EP”方案化疗联合“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗。2025-05-19、2025-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加强(胸部，上腹部，下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节，转移瘤可能；建议追踪复查。2.双肺慢性炎症，右肺中叶局限性支扩，双侧胸腔少量积液。3.脾脏低密度灶，建议追踪复查。4.胆囊可疑小结石。升结肠多发憩室。5.双肾小囊肿。与2025-05-18日片比较：右肺中叶局限性支扩，右肺下叶内基底段结节较前增大，右肺门淋巴结较前增大。考虑病情进展，于2025-08-23给予“安罗替尼12mg”联合“替雷利珠单抗”抗肿瘤治疗1周期。后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-22、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重无明显变化。诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利，予办理出院手续。\n国家医保编码：D411502011804 - Internet Explorer\n美系统) 修改患者信息 诊疗与病历 申请单 手术管理 医嘱单 会诊管理 重症管理 需关注医嘱 病情总览 质量管理 更多\n汤光冉 住院医师\n日间化疗中心[东院区]\n0000 床号: 04 住院天数: 1 费别: 全国医保居民 余额: 0.00 诊断: 肺恶性肿瘤,恶性肿瘤... 医疗救助类型: 农村低保\n病人列表 全息视图\n(1) ×\n操作 编辑 功能 表格 其他\n历\n保存 打印 自动续打 预览 单独打印 手工解锁 隐藏留痕 病历参考 更新数据 首页\n记录\n1:09:45 曾庆星\n医师审核\n录单\n1:10:52 曾庆星\n医师审核\n录单\n1:11:53 曾庆星\n医师审核\n11:12:02 曾庆星\n医师审核\n单(日间...\n11:13:02 曾庆星\n医师审核\n已打印\n11:15:03 曾庆星\n医师审核\n评估表\n16:30:58 曾庆星\n院医师审核\n/TE风险评...\n16:32:44 曾庆星\n院医师审核\n后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-2\n2、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我\n院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重\n无明显变化。\n诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利\n，予办理出院手续。\n出院情况：患者未诉不适，神志清，精神可，生命体征平稳。\n出院诊断：\n1.恶性肿瘤免疫治疗\n2.肺恶性肿瘤小细胞肺癌IV期\n3.肺继发恶性肿瘤\n4.冠状动脉粥样硬化性心脏病\n5.胸腔积液\n6.心包积液\n7.肺部感染\n8.腔隙性脑梗死\n9.肾功能检查的异常结果\n1\n100%",
    "role": "user"
  }
]
2026-08-10 15:54:57,968 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:54:57.966+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 70, "failed": 0, "current": {"3880a51e94d311f1bd9827cf206dfa2d": {"id": "3880a51e94d311f1bd9827cf206dfa2d", "doc_id": "37728ffc94d311f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909800, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377033220, "task_type": "dataflow", "root_trace_id": "4dc9fd8a1d244ef89de3e82f6546943d", "root_traceparent": "00-4dc9fd8a1d244ef89de3e82f6546943d-90143aef6fb19019-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:55:16,183 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:55:16,183 INFO     29 [qwen-vl-text] LLM output (len=3349):
{
  "encounter_date": "2026-03-23",
  "admission_date": "2026-03-23",
  "discharge_date": "2026-03-23",
  "hospital_days": 1,
  "department": "日间化疗中心",
  "bed_number": "04",
  "admission_condition": "1年余前因“胸闷”就诊我院，2025-01-17CT增强64：1.右肺门占位，考虑恶性病变并右肺中下叶不张，右下肺动受侵可能。2.双肺纤维索条灶。双肺多发小结节，转移待排。3.右侧胸腔少量积液。4.双肾小囊肿。5.升结肠多发憩室。6.子宫后壁肌瘤可能。7.冠状动脉CTA未见明显异常。2025-01-23行纤支镜下肺活检，2025-01-23活体组织病理申请 诊断意见：(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。2025-01-26免疫组化申请：CK广谱（点+），CD56（+），Syn（+），INSM1（+），CK5/6（-），P40（-），TTF1（+），NapsinA（-），Ki-67（80%+）。结合HE及免疫组化结果，（右中间段支气管）肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期，2025-04-22给予“EP”方案化疗联合“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗。2025-05-19、2025-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加增强(胸部.上腹部.下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节。胸腔少量积液。4.双肾小囊肿。5.升结肠多发息室。6.丁台加壁肌瘤可能。冠状动脉CT示无明显异常。2025-01-23行纤支镜下肺活检，2025-01-23活体组织病理申请 诊断意见：(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。2025-01-26免疫组化申请：CK广谱(点+)，CD56(+)，Syn(+)，INSM1(+)，CK5/6(-)，P40(-)，TTF1(+)，NapsinA(-)，Ki-67(80%)。结合HE及免疫组化结果，(右中间段支气管)肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期，2025-04-22给予“EP”方案化疗联合“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗。2025-05-19、2025-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加强(胸部，上腹部，下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节，转移瘤可能；建议追踪复查。2.双肺慢性炎症，右肺中叶局限性支扩，双侧胸腔少量积液。3.脾脏低密度灶，建议追踪复查。4.胆囊可疑小结石。升结肠多发憩室。5.双肾小囊肿。与2025-05-18日片比较：右肺中叶局限性支扩，右肺下叶内基底段结节较前增大，右肺门淋巴结较前增大。考虑病情进展，于2025-08-23给予“安罗替尼12mg”联合“替雷利珠单抗”抗肿瘤治疗1周期。后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-22、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重无明显变化。",
  "admission_diagnoses": [
    {
      "name": "肺小细胞神经内分泌癌",
      "diagnosis_type": "西医"
    }
  ],
  "treatment_summary": "入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利，予办理出院手续。",
  "auxiliary_exams": null,
  "imaging_findings": "2025-01-17CT增强64：1.右肺门占位，考虑恶性病变并右肺中下叶不张，右下肺动受侵可能。2.双肺纤维索条灶。双肺多发小结节，转移待排。3.右侧胸腔少量积液。4.双肾小囊肿。5.升结肠多发憩室。6.子宫后壁肌瘤可能。7.冠状动脉CTA未见明显异常。2025-08-21CT平扫加增强(胸部.上腹部.下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节。胸腔少量积液。4.双肾小囊肿。5.升结肠多发息室。6.丁台加壁肌瘤可能。冠状动脉CT示无明显异常。2025-08-21CT平扫加强(胸部，上腹部，下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节，转移瘤可能；建议追踪复查。2.双肺慢性炎症，右肺中叶局限性支扩，双侧胸腔少量积液。3.脾脏低密度灶，建议追踪复查。4.胆囊可疑小结石。升结肠多发憩室。5.双肾小囊肿。与2025-05-18日片比较：右肺中叶局限性支扩，右肺下叶内基底段结节较前增大，右肺门淋巴结较前增大。",
  "discharge_diagnoses": [
    {
      "name": "恶性肿瘤免疫治疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "肺恶性肿瘤小细胞肺癌IV期",
      "diagnosis_type": "西医"
    },
    {
      "name": "肺继发恶性肿瘤",
      "diagnosis_type": "西医"
    },
    {
      "name": "冠状动脉粥样硬化性心脏病",
      "diagnosis_type": "西医"
    },
    {
      "name": "胸腔积液",
      "diagnosis_type": "西医"
    },
    {
      "name": "心包积液",
      "diagnosis_type": "西医"
    },
    {
      "name": "肺部感染",
      "diagnosis_type": "西医"
    },
    {
      "name": "腔隙性脑梗死",
      "diagnosis_type": "西医"
    },
    {
      "name": "肾功能检查的异常结果",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": "患者未诉不适，神志清，精神可，生命体征平稳。",
  "outcome": null,
  "discharge_orders": null,
  "do_medications": [],
  "do_follow_up": null,
  "do_precautions": [],
  "next_treatment_date": null,
  "attending_physician": "曾庆星",
  "pe_ecog_score": null,
  "body_surface_area": null,
  "vs_temperature_c": null,
  "vs_pulse_bpm": null,
  "vs_respiration_rpm": null,
  "vs_systolic_bp_mmhg": null,
  "vs_diastolic_bp_mmhg": null
}
2026-08-10 15:55:16,183 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-03-23]
2026-08-10 15:55:16,184 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=449344, prompt_len=816
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共7行）
["2025.1 确诊小细胞癌，已行免疫组化协诊", "2025-.2-4给予”EP”化疗联合”特瑞普利单抗”免疫治疗3周期，", "2025-04-22给予”EP”方案化疗联合", "“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗", "2025.5-8行“特瑞普利单抗”免疫治疗4周期", "2025.8 PD", "2025.8-2026.2“替雷利珠单抗联合安罗替尼”免疫治疗"]

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
2026-08-10 15:55:26,924 INFO     29 [qwen-vl-text] coord API raw response (len=494):
[
	{"text": "2025.1 确诊小细胞癌，已行免疫组化协诊", "bbox": [173, 302, 323, 313]},
	{"text": "2025-.2-4给予”EP”化疗联合”特瑞普利单抗”免疫治疗3周期，", "bbox": [173, 313, 404, 324]},
	{"text": "2025-04-22给予”EP”方案化疗联合", "bbox": [173, 324, 303, 335]},
	{"text": "“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗", "bbox": [173, 335, 442, 346]},
	{"text": "2025.5-8行“特瑞普利单抗”免疫治疗4周期", "bbox": [173, 346, 335, 357]},
	{"text": "2025.8 PD", "bbox": [173, 357, 210, 367]},
	{"text": "2025.8-2026.2“替雷利珠单抗联合安罗替尼”免疫治疗", "bbox": [173, 367, 374, 378]}
]
2026-08-10 15:55:26,925 INFO     29 [qwen-vl-text] coord API: raw_items=7, valid_items=7, elapsed=10.7s
2026-08-10 15:55:26,925 INFO     29 [qwen-vl-text] coord item[0]: text=2025.1 确诊小细胞癌，已行免疫组化协诊, bbox=[173, 302, 323, 313]
2026-08-10 15:55:26,925 INFO     29 [qwen-vl-text] coord item[1]: text=2025-.2-4给予”EP”化疗联合”特瑞普利单抗”免疫治疗3周期，, bbox=[173, 313, 404, 324]
2026-08-10 15:55:26,925 INFO     29 [qwen-vl-text] coord item[2]: text=2025-04-22给予”EP”方案化疗联合, bbox=[173, 324, 303, 335]
2026-08-10 15:55:26,925 INFO     29 [qwen-vl-text] coord item[3]: text=“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗, bbox=[173, 335, 442, 346]
2026-08-10 15:55:26,925 INFO     29 [qwen-vl-text] coord item[4]: text=2025.5-8行“特瑞普利单抗”免疫治疗4周期, bbox=[173, 346, 335, 357]
2026-08-10 15:55:26,925 INFO     29 [qwen-vl-text] coord item[5]: text=2025.8 PD, bbox=[173, 357, 210, 367]
2026-08-10 15:55:26,925 INFO     29 [qwen-vl-text] coord item[6]: text=2025.8-2026.2“替雷利珠单抗联合安罗替尼”免疫治疗, bbox=[173, 367, 374, 378]
2026-08-10 15:55:26,926 INFO     29 [qwen-vl-text] page=0 — 7/7 coords, api_time=10.7s
2026-08-10 15:55:26,953 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=10857823, prompt_len=1409
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["信阳市中心医院", "日间化疗出入院记录", "姓名：", "性别：女年龄：65岁", "科别：日间化疗中心[东院床号：04", "区]", "登记号：0000", "住院号：25", "入院时间：2026年03月23日 08:29:00出院时间：2026年03月23日 11:14:00", "住院天数：1天", "主诉：确诊肺癌1年余", "入院情况：1年余前因“胸闷”就诊我院，2025-01-17CT增强64：1.右肺门占位，考虑恶性病变并", "右肺中下叶不张，右下肺动受侵可能。2.双肺纤维索条灶。双肺多发小结节，转移待排。3.右侧", "胸腔少量积液。4.双肾小囊肿。5.升结肠多发憩室。6.子宫后壁肌瘤可能。7.冠状动脉CTA未见明", "显异常。2025-01-23行纤支镜下肺活检，2025-01-23活体组织病理申请 诊断意见：(右中间段支", "气管)考虑小细胞癌，已行免疫组化协诊。2025-01-26免疫组化申请：CK广谱（点+），CD56（+），", "Syn（+），INSM1（+），CK5/6（-），P40（-），TTF1（+），NapsinA（-），Ki-67（80%+）。结合HE", "及免疫组化结果，（右中间段支气管）肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04", "-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期，2025-04-22给予“EP”方案化疗联合", "“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗。2025-05-19、2025", "-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加增强", "(胸部.上腹部.下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节。"]

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
2026-08-10 15:55:44,302 INFO     29 [qwen-vl-text] coord API raw response (len=1690):
[
	{"text": "信阳市中心医院", "bbox": [385, 254, 625, 301]},
	{"text": "日间化疗出入院记录", "bbox": [395, 331, 618, 365]},
	{"text": "姓名：", "bbox": [100, 385, 140, 405]},
	{"text": "性别：女年龄：65岁", "bbox": [207, 385, 336, 405]},
	{"text": "科别：日间化疗中心[东院床号：04", "bbox": [378, 387, 617, 407]},
	{"text": "区]", "bbox": [379, 417, 401, 438]},
	{"text": "登记号：0000", "bbox": [645, 387, 731, 407]},
	{"text": "住院号：25", "bbox": [787, 387, 857, 407]},
	{"text": "入院时间：2026年03月23日 08:29:00出院时间：2026年03月23日 11:14:00", "bbox": [97, 458, 730, 484]},
	{"text": "住院天数：1天", "bbox": [749, 458, 874, 484]},
	{"text": "主诉：确诊肺癌1年余", "bbox": [97, 496, 278, 520]},
	{"text": "入院情况：1年余前因“胸闷”就诊我院，2025-01-17CT增强64：1.右肺门占位，考虑恶性病变并", "bbox": [97, 534, 912, 559]},
	{"text": "右肺中下叶不张，右下肺动受侵可能。2.双肺纤维索条灶。双肺多发小结节，转移待排。3.右侧", "bbox": [97, 572, 911, 598]},
	{"text": "胸腔少量积液。4.双肾小囊肿。5.升结肠多发憩室。6.子宫后壁肌瘤可能。7.冠状动脉CTA未见明", "bbox": [97, 610, 911, 636]},
	{"text": "显异常。2025-01-23行纤支镜下肺活检，2025-01-23活体组织病理申请 诊断意见：(右中间段支", "bbox": [97, 648, 911, 674]},
	{"text": "气管)考虑小细胞癌，已行免疫组化协诊。2025-01-26免疫组化申请：CK广谱（点+），CD56（+），", "bbox": [97, 686, 911, 712]},
	{"text": "Syn（+），INSM1（+），CK5/6（-），P40（-），TTF1（+），NapsinA（-），Ki-67（80%+）。结合HE", "bbox": [97, 724, 912, 750]},
	{"text": "及免疫组化结果，（右中间段支气管）肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04", "bbox": [97, 762, 912, 788]},
	{"text": "-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期，2025-04-22给予“EP”方案化疗联合", "bbox": [97, 800, 911, 826]},
	{"text": "“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗。2025-05-19、2025", "bbox": [104, 839, 912, 865]},
	{"text": "-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加增强", "bbox": [97, 877, 912, 903]},
	{"text": "(胸部.上腹部.下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节。", "bbox": [100, 915, 904, 941]}
]
2026-08-10 15:55:44,303 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=17.3s
2026-08-10 15:55:44,303 INFO     29 [qwen-vl-text] coord item[0]: text=信阳市中心医院, bbox=[385, 254, 625, 301]
2026-08-10 15:55:44,303 INFO     29 [qwen-vl-text] coord item[1]: text=日间化疗出入院记录, bbox=[395, 331, 618, 365]
2026-08-10 15:55:44,303 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[100, 385, 140, 405]
2026-08-10 15:55:44,303 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女年龄：65岁, bbox=[207, 385, 336, 405]
2026-08-10 15:55:44,304 INFO     29 [qwen-vl-text] coord item[4]: text=科别：日间化疗中心[东院床号：04, bbox=[378, 387, 617, 407]
2026-08-10 15:55:44,304 INFO     29 [qwen-vl-text] coord item[5]: text=区], bbox=[379, 417, 401, 438]
2026-08-10 15:55:44,304 INFO     29 [qwen-vl-text] coord item[6]: text=登记号：0000, bbox=[645, 387, 731, 407]
2026-08-10 15:55:44,304 INFO     29 [qwen-vl-text] coord item[7]: text=住院号：25, bbox=[787, 387, 857, 407]
2026-08-10 15:55:44,304 INFO     29 [qwen-vl-text] coord item[8]: text=入院时间：2026年03月23日 08:29:00出院时间：2026年03月23日 11:14:00, bbox=[97, 458, 730, 484]
2026-08-10 15:55:44,304 INFO     29 [qwen-vl-text] coord item[9]: text=住院天数：1天, bbox=[749, 458, 874, 484]
2026-08-10 15:55:44,304 INFO     29 [qwen-vl-text] coord item[10]: text=主诉：确诊肺癌1年余, bbox=[97, 496, 278, 520]
2026-08-10 15:55:44,304 INFO     29 [qwen-vl-text] coord item[11]: text=入院情况：1年余前因“胸闷”就诊我院，2025-01-17CT增强64：1.右肺门占位，考虑恶性病变并, bbox=[97, 534, 912, 559]
2026-08-10 15:55:44,304 INFO     29 [qwen-vl-text] coord item[12]: text=右肺中下叶不张，右下肺动受侵可能。2.双肺纤维索条灶。双肺多发小结节，转移待排。3.右侧, bbox=[97, 572, 911, 598]
2026-08-10 15:55:44,304 INFO     29 [qwen-vl-text] coord item[13]: text=胸腔少量积液。4.双肾小囊肿。5.升结肠多发憩室。6.子宫后壁肌瘤可能。7.冠状动脉CTA未见明, bbox=[97, 610, 911, 636]
2026-08-10 15:55:44,304 INFO     29 [qwen-vl-text] coord item[14]: text=显异常。2025-01-23行纤支镜下肺活检，2025-01-23活体组织病理申请 诊断意见：(右中间段支, bbox=[97, 648, 911, 674]
2026-08-10 15:55:44,304 INFO     29 [qwen-vl-text] coord item[15]: text=气管)考虑小细胞癌，已行免疫组化协诊。2025-01-26免疫组化申请：CK广谱（点+），CD56（+），, bbox=[97, 686, 911, 712]
2026-08-10 15:55:44,304 INFO     29 [qwen-vl-text] coord item[16]: text=Syn（+），INSM1（+），CK5/6（-），P40（-），TTF1（+），NapsinA（-），Ki-67（80%+）。结合HE, bbox=[97, 724, 912, 750]
2026-08-10 15:55:44,304 INFO     29 [qwen-vl-text] coord item[17]: text=及免疫组化结果，（右中间段支气管）肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04, bbox=[97, 762, 912, 788]
2026-08-10 15:55:44,304 INFO     29 [qwen-vl-text] coord item[18]: text=-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期，2025-04-22给予“EP”方案化疗联合, bbox=[97, 800, 911, 826]
2026-08-10 15:55:44,304 INFO     29 [qwen-vl-text] coord item[19]: text=“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗。2025-05-19、2025, bbox=[104, 839, 912, 865]
2026-08-10 15:55:44,304 INFO     29 [qwen-vl-text] coord item[20]: text=-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加增强, bbox=[97, 877, 912, 903]
2026-08-10 15:55:44,304 INFO     29 [qwen-vl-text] coord item[21]: text=(胸部.上腹部.下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节。, bbox=[100, 915, 904, 941]
2026-08-10 15:55:44,308 INFO     29 [qwen-vl-text] page=1 — 22/22 coords, api_time=17.3s
2026-08-10 15:55:44,327 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7309712, prompt_len=1503
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["胸腔少量积液。4.双肾小囊肿。5.升结肠多发息室。6.丁台加壁肌瘤可能。冠状动脉CT示无明显异常。2025-01-23行纤支镜下肺活检，2025-01-23活体组织病理申请 诊断意见：(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。2025-01-26免疫组化申请：CK广谱(点+)，CD56(+)，Syn(+)，INSM1(+)，CK5/6(-)，P40(-)，TTF1(+)，NapsinA(-)，Ki-67(80%)。结合HE及免疫组化结果，(右中间段支气管)肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期，2025-04-22给予“EP”方案化疗联合“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗。2025-05-19、2025-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加强(胸部，上腹部，下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节，转移瘤可能；建议追踪复查。2.双肺慢性炎症，右肺中叶局限性支扩，双侧胸腔少量积液。3.脾脏低密度灶，建议追踪复查。4.胆囊可疑小结石。升结肠多发憩室。5.双肾小囊肿。与2025-05-18日片比较：右肺中叶局限性支扩，右肺下叶内基底段结节较前增大，右肺门淋巴结较前增大。考虑病情进展，于2025-08-23给予“安罗替尼12mg”联合“替雷利珠单抗”抗肿瘤治疗1周期。后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-22、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重无明显变化。诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利，予办理出院手续。"]

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
2026-08-10 15:55:59,695 INFO     29 [qwen-vl-text] coord API raw response (len=931):
[
	{"text": "胸腔少量积液。4.双肾小囊肿。5.升结肠多发息室。6.丁台加壁肌瘤可能。冠状动脉CT示无明显异常。2025-01-23行纤支镜下肺活检，2025-01-23活体组织病理申请 诊断意见：(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。2025-01-26免疫组化申请：CK广谱(点+)，CD56(+)，Syn(+)，INSM1(+)，CK5/6(-)，P40(-)，TTF1(+)，NapsinA(-)，Ki-67(80%)。结合HE及免疫组化结果，(右中间段支气管)肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期，2025-04-22给予“EP”方案化疗联合“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗。2025-05-19、2025-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加强(胸部，上腹部，下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节，转移瘤可能；建议追踪复查。2.双肺慢性炎症，右肺中叶局限性支扩，双侧胸腔少量积液。3.脾脏低密度灶，建议追踪复查。4.胆囊可疑小结石。升结肠多发憩室。5.双肾小囊肿。与2025-05-18日片比较：右肺中叶局限性支扩，右肺下叶内基底段结节较前增大，右肺门淋巴结较前增大。考虑病情进展，于2025-08-23给予“安罗替尼12mg”联合“替雷利珠单抗”抗肿瘤治疗1周期。后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-22、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重无明显变化。诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利，予办理出院手续。", "bbox": [0, 0, 924, 984]}
]
2026-08-10 15:55:59,695 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=15.4s
2026-08-10 15:55:59,695 INFO     29 [qwen-vl-text] coord item[0]: text=胸腔少量积液。4.双肾小囊肿。5.升结肠多发息室。6.丁台加壁肌瘤可能。冠状动脉CT示无明显异常。2025-01-23行纤支镜下肺活检，2025-01-23活体组织病理申请 诊断意见：(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。2025-01-26免疫组化申请：CK广谱(点+)，CD56(+)，Syn(+)，INSM1(+)，CK5/6(-)，P40(-)，TTF1(+)，NapsinA(-)，Ki-67(80%)。结合HE及免疫组化结果，(右中间段支气管)肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期，2025-04-22给予“EP”方案化疗联合“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗。2025-05-19、2025-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加强(胸部，上腹部，下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节，转移瘤可能；建议追踪复查。2.双肺慢性炎症，右肺中叶局限性支扩，双侧胸腔少量积液。3.脾脏低密度灶，建议追踪复查。4.胆囊可疑小结石。升结肠多发憩室。5.双肾小囊肿。与2025-05-18日片比较：右肺中叶局限性支扩，右肺下叶内基底段结节较前增大，右肺门淋巴结较前增大。考虑病情进展，于2025-08-23给予“安罗替尼12mg”联合“替雷利珠单抗”抗肿瘤治疗1周期。后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-22、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重无明显变化。诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利，予办理出院手续。, bbox=[0, 0, 924, 984]
2026-08-10 15:55:59,697 INFO     29 [qwen-vl-text] page=2 — 1/1 coords, api_time=15.4s
2026-08-10 15:55:59,716 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=6399521, prompt_len=1580
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共52行）
["国家医保编码：D411502011804 - Internet Explorer", "美系统) 修改患者信息 诊疗与病历 申请单 手术管理 医嘱单 会诊管理 重症管理 需关注医嘱 病情总览 质量管理 更多", "汤光冉 住院医师", "日间化疗中心[东院区]", "0000 床号: 04 住院天数: 1 费别: 全国医保居民 余额: 0.00 诊断: 肺恶性肿瘤,恶性肿瘤... 医疗救助类型: 农村低保", "病人列表 全息视图", "(1) ×", "操作 编辑 功能 表格 其他", "历", "保存 打印 自动续打 预览 单独打印 手工解锁 隐藏留痕 病历参考 更新数据 首页", "记录", "1:09:45 曾庆星", "医师审核", "录单", "1:10:52 曾庆星", "医师审核", "录单", "1:11:53 曾庆星", "医师审核", "11:12:02 曾庆星", "医师审核", "单(日间...", "11:13:02 曾庆星", "医师审核", "已打印", "11:15:03 曾庆星", "医师审核", "评估表", "16:30:58 曾庆星", "院医师审核", "/TE风险评...", "16:32:44 曾庆星", "院医师审核", "后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-2", "2、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我", "院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重", "无明显变化。", "诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利", "，予办理出院手续。", "出院情况：患者未诉不适，神志清，精神可，生命体征平稳。", "出院诊断：", "1.恶性肿瘤免疫治疗", "2.肺恶性肿瘤小细胞肺癌IV期", "3.肺继发恶性肿瘤", "4.冠状动脉粥样硬化性心脏病", "5.胸腔积液", "6.心包积液", "7.肺部感染", "8.腔隙性脑梗死", "9.肾功能检查的异常结果", "1", "100%"]

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
2026-08-10 15:56:24,791 INFO     29 [qwen-vl-text] coord API raw response (len=3031):
[
	{"text": "国家医保编码：D411502011804 - Internet Explorer", "bbox": [24, 5, 215, 18]},
	{"text": "美系统) 修改患者信息 诊疗与病历 申请单 手术管理 医嘱单 会诊管理 重症管理 需关注医嘱 病情总览 质量管理 更多", "bbox": [24, 37, 672, 57]},
	{"text": "汤光冉 住院医师", "bbox": [903, 35, 970, 50]},
	{"text": "日间化疗中心[东院区]", "bbox": [903, 50, 987, 64]},
	{"text": "0000 床号: 04 住院天数: 1 费别: 全国医保居民 余额: 0.00 诊断: 肺恶性肿瘤,恶性肿瘤... 医疗救助类型: 农村低保", "bbox": [27, 77, 575, 93]},
	{"text": "病人列表 全息视图", "bbox": [883, 73, 992, 100]},
	{"text": "(1) ×", "bbox": [20, 113, 55, 128]},
	{"text": "操作 编辑 功能 表格 其他", "bbox": [137, 147, 275, 162]},
	{"text": "历", "bbox": [20, 179, 31, 193]},
	{"text": "保存 打印 自动续打 预览 单独打印 手工解锁 隐藏留痕 病历参考 更新数据 首页", "bbox": [137, 171, 538, 217]},
	{"text": "记录", "bbox": [16, 253, 34, 268]},
	{"text": "1:09:45 曾庆星", "bbox": [16, 279, 78, 294]},
	{"text": "医师审核", "bbox": [16, 300, 47, 314]},
	{"text": "录单", "bbox": [13, 337, 33, 351]},
	{"text": "1:10:52 曾庆星", "bbox": [14, 363, 78, 377]},
	{"text": "医师审核", "bbox": [13, 383, 46, 397]},
	{"text": "录单", "bbox": [13, 419, 33, 433]},
	{"text": "1:11:53 曾庆星", "bbox": [14, 445, 78, 459]},
	{"text": "医师审核", "bbox": [13, 465, 46, 479]},
	{"text": "11:12:02 曾庆星", "bbox": [13, 525, 78, 539]},
	{"text": "医师审核", "bbox": [13, 545, 46, 559]},
	{"text": "单(日间...", "bbox": [8, 582, 51, 597]},
	{"text": "11:13:02 曾庆星", "bbox": [12, 609, 78, 623]},
	{"text": "医师审核", "bbox": [8, 629, 47, 643]},
	{"text": "已打印", "bbox": [72, 665, 100, 679]},
	{"text": "11:15:03 曾庆星", "bbox": [12, 691, 78, 705]},
	{"text": "医师审核", "bbox": [8, 711, 47, 725]},
	{"text": "评估表", "bbox": [8, 748, 36, 762]},
	{"text": "16:30:58 曾庆星", "bbox": [12, 774, 78, 788]},
	{"text": "院医师审核", "bbox": [4, 794, 49, 808]},
	{"text": "/TE风险评...", "bbox": [4, 830, 52, 844]},
	{"text": "16:32:44 曾庆星", "bbox": [12, 856, 78, 870]},
	{"text": "院医师审核", "bbox": [4, 876, 50, 890]},
	{"text": "后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-2", "bbox": [192, 227, 922, 252]},
	{"text": "2、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我", "bbox": [192, 264, 921, 290]},
	{"text": "院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重", "bbox": [192, 302, 921, 329]},
	{"text": "无明显变化。", "bbox": [192, 344, 285, 369]},
	{"text": "诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利", "bbox": [192, 380, 921, 406]},
	{"text": "，予办理出院手续。", "bbox": [192, 420, 338, 445]},
	{"text": "出院情况：患者未诉不适，神志清，精神可，生命体征平稳。", "bbox": [192, 458, 647, 483]},
	{"text": "出院诊断：", "bbox": [192, 497, 267, 521]},
	{"text": "1.恶性肿瘤免疫治疗", "bbox": [226, 535, 382, 560]},
	{"text": "2.肺恶性肿瘤小细胞肺癌IV期", "bbox": [225, 573, 452, 598]},
	{"text": "3.肺继发恶性肿瘤", "bbox": [225, 612, 365, 637]},
	{"text": "4.冠状动脉粥样硬化性心脏病", "bbox": [225, 651, 452, 677]},
	{"text": "5.胸腔积液", "bbox": [225, 690, 313, 715]},
	{"text": "6.心包积液", "bbox": [225, 728, 313, 753]},
	{"text": "7.肺部感染", "bbox": [226, 767, 313, 792]},
	{"text": "8.腔隙性脑梗死", "bbox": [226, 806, 350, 831]},
	{"text": "9.肾功能检查的异常结果", "bbox": [226, 844, 418, 869]},
	{"text": "1", "bbox": [555, 919, 563, 938]},
	{"text": "100%", "bbox": [938, 945, 967, 958]}
]
2026-08-10 15:56:24,791 INFO     29 [qwen-vl-text] coord API: raw_items=52, valid_items=52, elapsed=25.1s
2026-08-10 15:56:24,791 INFO     29 [qwen-vl-text] coord item[0]: text=国家医保编码：D411502011804 - Internet Explorer, bbox=[24, 5, 215, 18]
2026-08-10 15:56:24,791 INFO     29 [qwen-vl-text] coord item[1]: text=美系统) 修改患者信息 诊疗与病历 申请单 手术管理 医嘱单 会诊管理 重症管理 需关注医嘱 病情总览 质量管理 更多, bbox=[24, 37, 672, 57]
2026-08-10 15:56:24,791 INFO     29 [qwen-vl-text] coord item[2]: text=汤光冉 住院医师, bbox=[903, 35, 970, 50]
2026-08-10 15:56:24,791 INFO     29 [qwen-vl-text] coord item[3]: text=日间化疗中心[东院区], bbox=[903, 50, 987, 64]
2026-08-10 15:56:24,791 INFO     29 [qwen-vl-text] coord item[4]: text=0000 床号: 04 住院天数: 1 费别: 全国医保居民 余额: 0.00 诊断: 肺恶性肿瘤,恶性肿瘤... 医疗救助类型: 农村低保, bbox=[27, 77, 575, 93]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[5]: text=病人列表 全息视图, bbox=[883, 73, 992, 100]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[6]: text=(1) ×, bbox=[20, 113, 55, 128]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[7]: text=操作 编辑 功能 表格 其他, bbox=[137, 147, 275, 162]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[8]: text=历, bbox=[20, 179, 31, 193]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[9]: text=保存 打印 自动续打 预览 单独打印 手工解锁 隐藏留痕 病历参考 更新数据 首页, bbox=[137, 171, 538, 217]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[10]: text=记录, bbox=[16, 253, 34, 268]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[11]: text=1:09:45 曾庆星, bbox=[16, 279, 78, 294]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[12]: text=医师审核, bbox=[16, 300, 47, 314]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[13]: text=录单, bbox=[13, 337, 33, 351]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[14]: text=1:10:52 曾庆星, bbox=[14, 363, 78, 377]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[15]: text=医师审核, bbox=[13, 383, 46, 397]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[16]: text=录单, bbox=[13, 419, 33, 433]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[17]: text=1:11:53 曾庆星, bbox=[14, 445, 78, 459]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[18]: text=医师审核, bbox=[13, 465, 46, 479]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[19]: text=11:12:02 曾庆星, bbox=[13, 525, 78, 539]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[20]: text=医师审核, bbox=[13, 545, 46, 559]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[21]: text=单(日间..., bbox=[8, 582, 51, 597]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[22]: text=11:13:02 曾庆星, bbox=[12, 609, 78, 623]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[23]: text=医师审核, bbox=[8, 629, 47, 643]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[24]: text=已打印, bbox=[72, 665, 100, 679]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[25]: text=11:15:03 曾庆星, bbox=[12, 691, 78, 705]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[26]: text=医师审核, bbox=[8, 711, 47, 725]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[27]: text=评估表, bbox=[8, 748, 36, 762]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[28]: text=16:30:58 曾庆星, bbox=[12, 774, 78, 788]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[29]: text=院医师审核, bbox=[4, 794, 49, 808]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[30]: text=/TE风险评..., bbox=[4, 830, 52, 844]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[31]: text=16:32:44 曾庆星, bbox=[12, 856, 78, 870]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[32]: text=院医师审核, bbox=[4, 876, 50, 890]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[33]: text=后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-2, bbox=[192, 227, 922, 252]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[34]: text=2、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我, bbox=[192, 264, 921, 290]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[35]: text=院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重, bbox=[192, 302, 921, 329]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[36]: text=无明显变化。, bbox=[192, 344, 285, 369]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[37]: text=诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利, bbox=[192, 380, 921, 406]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[38]: text=，予办理出院手续。, bbox=[192, 420, 338, 445]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[39]: text=出院情况：患者未诉不适，神志清，精神可，生命体征平稳。, bbox=[192, 458, 647, 483]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[40]: text=出院诊断：, bbox=[192, 497, 267, 521]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[41]: text=1.恶性肿瘤免疫治疗, bbox=[226, 535, 382, 560]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[42]: text=2.肺恶性肿瘤小细胞肺癌IV期, bbox=[225, 573, 452, 598]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[43]: text=3.肺继发恶性肿瘤, bbox=[225, 612, 365, 637]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[44]: text=4.冠状动脉粥样硬化性心脏病, bbox=[225, 651, 452, 677]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[45]: text=5.胸腔积液, bbox=[225, 690, 313, 715]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[46]: text=6.心包积液, bbox=[225, 728, 313, 753]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[47]: text=7.肺部感染, bbox=[226, 767, 313, 792]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[48]: text=8.腔隙性脑梗死, bbox=[226, 806, 350, 831]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[49]: text=9.肾功能检查的异常结果, bbox=[226, 844, 418, 869]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[50]: text=1, bbox=[555, 919, 563, 938]
2026-08-10 15:56:24,792 INFO     29 [qwen-vl-text] coord item[51]: text=100%, bbox=[938, 945, 967, 958]
2026-08-10 15:56:24,793 INFO     29 [qwen-vl-text] page=3 — 52/52 coords, api_time=25.1s
2026-08-10 15:56:24,794 INFO     29 [qwen-vl-text] new_positions (82):
[[0, 390.8433232421875, 729.7248173828125, 523.0549311523438, 542.1066008300782], [0, 390.8433232421875, 912.7208242187501, 542.1066008300782, 561.1582705078125], [0, 390.8433232421875, 684.5406181640625, 561.1582705078125, 580.2099401855469], [0, 390.8433232421875, 998.570802734375, 580.2099401855469, 599.2616098632813], [0, 390.8433232421875, 756.8353369140625, 599.2616098632813, 618.3132795410156], [0, 390.8433232421875, 474.434091796875, 618.3132795410156, 635.6329792480469], [0, 390.8433232421875, 844.944525390625, 635.6329792480469, 654.6846489257813], [1, 870.0999999999999, 1412.4999999999998, 439.928, 521.332], [1, 892.6999999999999, 1396.6799999999998, 573.292, 632.18], [1, 225.99999999999997, 316.4, 666.82, 701.46], [1, 467.81999999999994, 759.3599999999999, 666.82, 701.46], [1, 854.28, 1394.4199999999998, 670.284, 704.924], [1, 856.54, 906.2599999999999, 722.244, 758.616], [1, 1457.6999999999998, 1652.06, 670.284, 704.924], [1, 1778.62, 1936.8199999999997, 670.284, 704.924], [1, 219.21999999999997, 1649.8, 793.256, 838.288], [1, 1692.7399999999998, 1975.2399999999998, 793.256, 838.288], [1, 219.21999999999997, 628.28, 859.072, 900.64], [1, 219.21999999999997, 2061.12, 924.888, 968.188], [1, 219.21999999999997, 2058.8599999999997, 990.704, 1035.736], [1, 219.21999999999997, 2058.8599999999997, 1056.52, 1101.552], [1, 219.21999999999997, 2058.8599999999997, 1122.336, 1167.368], [1, 219.21999999999997, 2058.8599999999997, 1188.152, 1233.184], [1, 219.21999999999997, 2061.12, 1253.968, 1299.0], [1, 219.21999999999997, 2061.12, 1319.7839999999999, 1364.816], [1, 219.21999999999997, 2058.8599999999997, 1385.6, 1430.632], [1, 235.03999999999996, 2061.12, 1453.148, 1498.18], [1, 219.21999999999997, 2061.12, 1518.964, 1563.996], [1, 225.99999999999997, 2043.0399999999997, 1584.78, 1629.812], [2, 0.0, 2029.1040000000003, 0.0, 1361.856], [3, 53.28, 477.30000000000007, 7.66, 27.576], [3, 53.28, 1491.8400000000001, 56.684, 87.324], [3, 2004.66, 2153.4, 53.620000000000005, 76.6], [3, 2004.66, 2191.1400000000003, 76.6, 98.048], [3, 59.940000000000005, 1276.5, 117.964, 142.476], [3, 1960.2600000000002, 2202.2400000000002, 111.836, 153.2], [3, 44.400000000000006, 122.10000000000001, 173.116, 196.096], [3, 304.14000000000004, 610.5, 225.204, 248.184], [3, 44.400000000000006, 68.82000000000001, 274.228, 295.676], [3, 304.14000000000004, 1194.3600000000001, 261.972, 332.444], [3, 35.52, 75.48, 387.596, 410.576], [3, 35.52, 173.16000000000003, 427.428, 450.408], [3, 35.52, 104.34, 459.6, 481.048], [3, 28.860000000000003, 73.26, 516.284, 537.732], [3, 31.080000000000002, 173.16000000000003, 556.116, 577.564], [3, 28.860000000000003, 102.12, 586.756, 608.2040000000001], [3, 28.860000000000003, 73.26, 641.908, 663.356], [3, 31.080000000000002, 173.16000000000003, 681.74, 703.188], [3, 28.860000000000003, 102.12, 712.38, 733.828], [3, 28.860000000000003, 173.16000000000003, 804.3000000000001, 825.748], [3, 28.860000000000003, 102.12, 834.94, 856.388], [3, 17.76, 113.22000000000001, 891.624, 914.604], [3, 26.64, 173.16000000000003, 932.988, 954.436], [3, 17.76, 104.34, 963.628, 985.076], [3, 159.84, 222.00000000000003, 1018.78, 1040.228], [3, 26.64, 173.16000000000003, 1058.612, 1080.06], [3, 17.76, 104.34, 1089.252, 1110.7], [3, 17.76, 79.92, 1145.936, 1167.384], [3, 26.64, 173.16000000000003, 1185.768, 1207.2160000000001], [3, 8.88, 108.78000000000002, 1216.4080000000001, 1237.856], [3, 8.88, 115.44000000000001, 1271.56, 1293.008], [3, 26.64, 173.16000000000003, 1311.392, 1332.84], [3, 8.88, 111.00000000000001, 1342.032, 1363.48], [3, 426.24, 2046.8400000000001, 347.764, 386.064], [3, 426.24, 2044.6200000000001, 404.448, 444.28000000000003], [3, 426.24, 2044.6200000000001, 462.664, 504.028], [3, 426.24, 632.7, 527.008, 565.308], [3, 426.24, 2044.6200000000001, 582.16, 621.992], [3, 426.24, 750.36, 643.44, 681.74], [3, 426.24, 1436.3400000000001, 701.6560000000001, 739.956], [3, 426.24, 592.74, 761.404, 798.172], [3, 501.72, 848.0400000000001, 819.62, 857.9200000000001], [3, 499.50000000000006, 1003.44, 877.836, 916.136], [3, 499.50000000000006, 810.3000000000001, 937.5840000000001, 975.884], [3, 499.50000000000006, 1003.44, 997.332, 1037.164], [3, 499.50000000000006, 694.86, 1057.08, 1095.38], [3, 499.50000000000006, 694.86, 1115.296, 1153.596], [3, 501.72, 694.86, 1175.044, 1213.344], [3, 501.72, 777.0000000000001, 1234.792, 1273.092], [3, 501.72, 927.96, 1293.008, 1331.308], [3, 1232.1000000000001, 1249.8600000000001, 1407.9080000000001, 1437.016], [3, 2082.36, 2146.7400000000002, 1447.74, 1467.656]]
2026-08-10 15:56:24,794 INFO     29 [qwen-vl-text] ═══ DONE ═══ 82 positions, pages=4, time=90.6s
2026-08-10 15:56:24,808 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 15:56:24,808 INFO     29 [Trace] task=3880a51e | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | Extractor:Discharge | outputs={"chunks": "1 items, types={'DischargeRecord': 1}", "html": "", "json": "302 items", "markdown": "", "text": "", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 5, \"chunks_LabExam\": 3}"}
2026-08-10 15:56:24,808 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 15:56:24,809 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:56:24.808+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 70, "failed": 0, "current": {"3880a51e94d311f1bd9827cf206dfa2d": {"id": "3880a51e94d311f1bd9827cf206dfa2d", "doc_id": "37728ffc94d311f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909800, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377033220, "task_type": "dataflow", "root_trace_id": "4dc9fd8a1d244ef89de3e82f6546943d", "root_traceparent": "00-4dc9fd8a1d244ef89de3e82f6546943d-90143aef6fb19019-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:56:24,817 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:56:24,817 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 15:56:25,788 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:56:25,796 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 15:56:25,797 INFO     29 [Trace] task=3880a51e | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "302 items", "markdown": "", "text": "", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 5, \"chunks_LabExam\": 3}"}
2026-08-10 15:56:25,797 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 15:56:25,803 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:56:25,804 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:56:25,804 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 15:56:25,804 INFO     29 [qwen-vl-text] positions(24): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:56:25,804 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [24]
2026-08-10 15:56:26,345 INFO     29 [qwen-vl-text] page=4, rect=1292x1840, img=(3589x5112), dpi=200
2026-08-10 15:56:26,348 INFO     29 [qwen-vl-text] LLM extraction start, text_len=398
2026-08-10 15:56:26,348 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:56:26,348 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 84, \"bbox_end\": 107, \"encounter_dates\": [\"2025-01-26\"], \"department\": \"病理科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "信阳市中心医院\n免疫病理诊断报告\n免疫组化号：MT25-\n姓名：\n性别：女\n年龄：64岁\n送检医院：\n病区：肿瘤内科五护理单元[东病理号：D25-01313\n就诊卡号：\n住院号：2\n病区床号：21\n送检标本：肺手术标本\n送检时间：2025-01-24\n临床诊断：\n光镜所见：\n免疫病理诊断：\nCK广谱（点+），CD56（+），Syn（+），INSM1（+），CK5/6（-），P40（-），TTF1（+），\nNapsinA（-），Ki-67（80%+）。\n结合HE及免疫组化结果，（右中间段支气管）肺小细胞神经内分泌癌。\n初诊医师：刘磊\n复诊医师：刘磊\n报告日期：2025-01-26 10:49\n备注：1.本报告单仅供临床参考 2.如临床对报告内容有疑问请与报告医生联系。联系电话：0376-6227723(西院区)，0376-6667570(东院区)。\n3.此报告必须经过病理科医师签字有效。",
    "role": "user"
  }
]
2026-08-10 15:56:28,555 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:56:28,556 INFO     29 [qwen-vl-text] LLM output (len=448):
{
  "exam_date": "2025-01-24",
  "report_date": "2025-01-26",
  "exam_name": "免疫病理诊断",
  "exam_category": "pathology",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": "肿瘤内科五护理单元",
  "bed_number": "21",
  "findings": "光镜所见：",
  "conclusion": "免疫病理诊断：\nCK广谱（点+），CD56（+），Syn（+），INSM1（+），CK5/6（-），P40（-），TTF1（+），\nNapsinA（-），Ki-67（80%+）。\n结合HE及免疫组化结果，（右中间段支气管）肺小细胞神经内分泌癌。",
  "physician": "刘磊",
  "reviewer": "刘磊"
}
2026-08-10 15:56:28,570 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=6377978, prompt_len=1083
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共24行）
["信阳市中心医院", "免疫病理诊断报告", "免疫组化号：MT25-", "姓名：", "性别：女", "年龄：64岁", "送检医院：", "病区：肿瘤内科五护理单元[东病理号：D25-01313", "就诊卡号：", "住院号：2", "病区床号：21", "送检标本：肺手术标本", "送检时间：2025-01-24", "临床诊断：", "光镜所见：", "免疫病理诊断：", "CK广谱（点+），CD56（+），Syn（+），INSM1（+），CK5/6（-），P40（-），TTF1（+），", "NapsinA（-），Ki-67（80%+）。", "结合HE及免疫组化结果，（右中间段支气管）肺小细胞神经内分泌癌。", "初诊医师：刘磊", "复诊医师：刘磊", "报告日期：2025-01-26 10:49", "备注：1.本报告单仅供临床参考 2.如临床对报告内容有疑问请与报告医生联系。联系电话：0376-6227723(西院区)，0376-6667570(东院区)。", "3.此报告必须经过病理科医师签字有效。"]

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
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord API raw response (len=1439):
[
	{"text": "信阳市中心医院", "bbox": [355, 24, 609, 51]},
	{"text": "免疫病理诊断报告", "bbox": [376, 65, 595, 84]},
	{"text": "免疫组化号：MT25-", "bbox": [620, 98, 802, 113]},
	{"text": "姓名：", "bbox": [58, 127, 130, 144]},
	{"text": "性别：女", "bbox": [348, 126, 467, 143]},
	{"text": "年龄：64岁", "bbox": [640, 125, 792, 141]},
	{"text": "送检医院：", "bbox": [58, 156, 150, 173]},
	{"text": "病区：肿瘤内科五护理单元[东病理号：D25-01313", "bbox": [348, 154, 828, 170]},
	{"text": "就诊卡号：", "bbox": [58, 184, 150, 201]},
	{"text": "住院号：2", "bbox": [348, 183, 442, 200]},
	{"text": "病区床号：21", "bbox": [640, 183, 759, 199]},
	{"text": "送检标本：肺手术标本", "bbox": [58, 212, 252, 228]},
	{"text": "送检时间：2025-01-24", "bbox": [327, 212, 530, 228]},
	{"text": "临床诊断：", "bbox": [58, 241, 150, 258]},
	{"text": "光镜所见：", "bbox": [57, 295, 153, 312]},
	{"text": "免疫病理诊断：", "bbox": [60, 567, 200, 583]},
	{"text": "CK广谱（点+），CD56（+），Syn（+），INSM1（+），CK5/6（-），P40（-），TTF1（+），", "bbox": [74, 599, 807, 615]},
	{"text": "NapsinA（-），Ki-67（80%+）。", "bbox": [74, 614, 360, 629]},
	{"text": "结合HE及免疫组化结果，（右中间段支气管）肺小细胞神经内分泌癌。", "bbox": [74, 628, 670, 645]},
	{"text": "初诊医师：刘磊", "bbox": [58, 803, 197, 820]},
	{"text": "复诊医师：刘磊", "bbox": [333, 803, 468, 820]},
	{"text": "报告日期：2025-01-26 10:49", "bbox": [615, 803, 870, 820]},
	{"text": "备注：1.本报告单仅供临床参考 2.如临床对报告内容有疑问请与报告医生联系。联系电话：0376-6227723(西院区)，0376-6667570(东院区)。", "bbox": [64, 872, 962, 887]},
	{"text": "3.此报告必须经过病理科医师签字有效。", "bbox": [98, 896, 363, 909]}
]
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord API: raw_items=24, valid_items=24, elapsed=15.2s
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord item[0]: text=信阳市中心医院, bbox=[355, 24, 609, 51]
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord item[1]: text=免疫病理诊断报告, bbox=[376, 65, 595, 84]
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord item[2]: text=免疫组化号：MT25-, bbox=[620, 98, 802, 113]
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[58, 127, 130, 144]
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord item[4]: text=性别：女, bbox=[348, 126, 467, 143]
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：64岁, bbox=[640, 125, 792, 141]
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord item[6]: text=送检医院：, bbox=[58, 156, 150, 173]
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord item[7]: text=病区：肿瘤内科五护理单元[东病理号：D25-01313, bbox=[348, 154, 828, 170]
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord item[8]: text=就诊卡号：, bbox=[58, 184, 150, 201]
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord item[9]: text=住院号：2, bbox=[348, 183, 442, 200]
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord item[10]: text=病区床号：21, bbox=[640, 183, 759, 199]
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord item[11]: text=送检标本：肺手术标本, bbox=[58, 212, 252, 228]
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord item[12]: text=送检时间：2025-01-24, bbox=[327, 212, 530, 228]
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord item[13]: text=临床诊断：, bbox=[58, 241, 150, 258]
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord item[14]: text=光镜所见：, bbox=[57, 295, 153, 312]
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord item[15]: text=免疫病理诊断：, bbox=[60, 567, 200, 583]
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord item[16]: text=CK广谱（点+），CD56（+），Syn（+），INSM1（+），CK5/6（-），P40（-），TTF1（+），, bbox=[74, 599, 807, 615]
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord item[17]: text=NapsinA（-），Ki-67（80%+）。, bbox=[74, 614, 360, 629]
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord item[18]: text=结合HE及免疫组化结果，（右中间段支气管）肺小细胞神经内分泌癌。, bbox=[74, 628, 670, 645]
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord item[19]: text=初诊医师：刘磊, bbox=[58, 803, 197, 820]
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord item[20]: text=复诊医师：刘磊, bbox=[333, 803, 468, 820]
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord item[21]: text=报告日期：2025-01-26 10:49, bbox=[615, 803, 870, 820]
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord item[22]: text=备注：1.本报告单仅供临床参考 2.如临床对报告内容有疑问请与报告医生联系。联系电话：0376-6227723(西院区)，0376-6667570(东院区)。, bbox=[64, 872, 962, 887]
2026-08-10 15:56:43,787 INFO     29 [qwen-vl-text] coord item[23]: text=3.此报告必须经过病理科医师签字有效。, bbox=[98, 896, 363, 909]
2026-08-10 15:56:43,789 INFO     29 [qwen-vl-text] page=4 — 24/24 coords, api_time=15.2s
2026-08-10 15:56:43,789 INFO     29 [qwen-vl-text] new_positions (24):
[[4, 458.66, 786.828, 44.160000000000004, 93.84], [4, 485.79200000000003, 768.74, 119.60000000000001, 154.56], [4, 801.0400000000001, 1036.184, 180.32000000000002, 207.92000000000002], [4, 74.936, 167.96, 233.68, 264.96000000000004], [4, 449.616, 603.364, 231.84, 263.12], [4, 826.88, 1023.264, 230.0, 259.44], [4, 74.936, 193.8, 287.04, 318.32], [4, 449.616, 1069.776, 283.36, 312.8], [4, 74.936, 193.8, 338.56, 369.84000000000003], [4, 449.616, 571.064, 336.72, 368.0], [4, 826.88, 980.628, 336.72, 366.16], [4, 74.936, 325.584, 390.08000000000004, 419.52000000000004], [4, 422.48400000000004, 684.76, 390.08000000000004, 419.52000000000004], [4, 74.936, 193.8, 443.44, 474.72], [4, 73.644, 197.67600000000002, 542.8000000000001, 574.08], [4, 77.52, 258.40000000000003, 1043.28, 1072.72], [4, 95.608, 1042.644, 1102.16, 1131.6000000000001], [4, 95.608, 465.12, 1129.76, 1157.3600000000001], [4, 95.608, 865.64, 1155.52, 1186.8], [4, 74.936, 254.524, 1477.52, 1508.8], [4, 430.236, 604.6560000000001, 1477.52, 1508.8], [4, 794.58, 1124.04, 1477.52, 1508.8], [4, 82.688, 1242.904, 1604.48, 1632.0800000000002], [4, 126.616, 468.99600000000004, 1648.64, 1672.5600000000002]]
2026-08-10 15:56:43,789 INFO     29 [qwen-vl-text] ═══ DONE ═══ 24 positions, pages=1, time=18.0s
2026-08-10 15:56:43,789 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:56:43,790 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:56:43,790 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 15:56:43,790 INFO     29 [qwen-vl-text] positions(22): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:56:43,790 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [22]
2026-08-10 15:56:44,260 INFO     29 [qwen-vl-text] page=5, rect=1232x1744, img=(3423x4845), dpi=200
2026-08-10 15:56:44,264 INFO     29 [qwen-vl-text] LLM extraction start, text_len=314
2026-08-10 15:56:44,264 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:56:44,264 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 108, \"bbox_end\": 129, \"encounter_dates\": [\"2025-01-23\"], \"department\": \"病理科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "信阳市中心医院\n病理检查报告单\n病理号：D25\n姓名：\n性别：女\n年龄：64岁\n送检医院：\n送检科室：呼吸与危重症医学科送检日期：2025-01-22\n门诊号：9\n住院号：25\n床号：21\n送检医师：周鹏飞\n送检标本：右中间段支气管\n临床诊断：\n巨检：灰白色碎组织最大径0.3厘米。全取\n病理诊断：\n(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。\n初诊医师：刘晶晶\n复诊医师：刘磊\n报告日期：2025-01-23 19:26\n备注：1.本报告单仅供临床参考 2.如临床对报告内容有疑问请与报告医生联系。联系电话：0376-6227723(西院区)；0376-6667570(东院区)。\n3.此报告必须经过病理科医师签字有效。",
    "role": "user"
  }
]
2026-08-10 15:56:46,375 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:56:46,376 INFO     29 [qwen-vl-text] LLM output (len=375):
{
  "exam_date": "2025-01-22",
  "report_date": "2025-01-23",
  "exam_name": "病理检查",
  "exam_category": "pathology",
  "body_part": "右中间段支气管",
  "patient_name": null,
  "patient_gender": "女",
  "department": "呼吸与危重症医学科",
  "bed_number": "21",
  "findings": "巨检：灰白色碎组织最大径0.3厘米。全取",
  "conclusion": "病理诊断：\n(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。",
  "physician": "刘晶晶",
  "reviewer": "刘磊"
}
2026-08-10 15:56:46,389 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=6423871, prompt_len=993
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["信阳市中心医院", "病理检查报告单", "病理号：D25", "姓名：", "性别：女", "年龄：64岁", "送检医院：", "送检科室：呼吸与危重症医学科送检日期：2025-01-22", "门诊号：9", "住院号：25", "床号：21", "送检医师：周鹏飞", "送检标本：右中间段支气管", "临床诊断：", "巨检：灰白色碎组织最大径0.3厘米。全取", "病理诊断：", "(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。", "初诊医师：刘晶晶", "复诊医师：刘磊", "报告日期：2025-01-23 19:26", "备注：1.本报告单仅供临床参考 2.如临床对报告内容有疑问请与报告医生联系。联系电话：0376-6227723(西院区)；0376-6667570(东院区)。", "3.此报告必须经过病理科医师签字有效。"]

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
2026-08-10 15:57:02,208 INFO     29 [qwen-vl-text] coord API raw response (len=1279):
[
	{"text": "信阳市中心医院", "bbox": [380, 28, 638, 56]},
	{"text": "病理检查报告单", "bbox": [409, 64, 607, 84]},
	{"text": "病理号：D25", "bbox": [705, 98, 820, 115]},
	{"text": "姓名：", "bbox": [100, 128, 182, 146]},
	{"text": "性别：女", "bbox": [392, 126, 514, 144]},
	{"text": "年龄：64岁", "bbox": [693, 126, 841, 143]},
	{"text": "送检医院：", "bbox": [100, 153, 190, 170]},
	{"text": "送检科室：呼吸与危重症医学科送检日期：2025-01-22", "bbox": [392, 151, 902, 168]},
	{"text": "门诊号：9", "bbox": [100, 177, 220, 195]},
	{"text": "住院号：25", "bbox": [392, 176, 514, 193]},
	{"text": "床号：21", "bbox": [691, 176, 798, 192]},
	{"text": "送检医师：周鹏飞", "bbox": [100, 204, 264, 221]},
	{"text": "送检标本：右中间段支气管", "bbox": [392, 202, 633, 219]},
	{"text": "临床诊断：", "bbox": [100, 229, 190, 246]},
	{"text": "巨检：灰白色碎组织最大径0.3厘米。全取", "bbox": [103, 276, 473, 294]},
	{"text": "病理诊断：", "bbox": [113, 573, 208, 590]},
	{"text": "(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。", "bbox": [154, 589, 622, 607]},
	{"text": "初诊医师：刘晶晶", "bbox": [102, 860, 256, 878]},
	{"text": "复诊医师：刘磊", "bbox": [379, 859, 505, 876]},
	{"text": "报告日期：2025-01-23 19:26", "bbox": [656, 859, 920, 876]},
	{"text": "备注：1.本报告单仅供临床参考 2.如临床对报告内容有疑问请与报告医生联系。联系电话：0376-6227723(西院区)；0376-6667570(东院区)。", "bbox": [99, 900, 997, 914]},
	{"text": "3.此报告必须经过病理科医师签字有效。", "bbox": [144, 915, 407, 929]}
]
2026-08-10 15:57:02,208 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=15.8s
2026-08-10 15:57:02,208 INFO     29 [qwen-vl-text] coord item[0]: text=信阳市中心医院, bbox=[380, 28, 638, 56]
2026-08-10 15:57:02,208 INFO     29 [qwen-vl-text] coord item[1]: text=病理检查报告单, bbox=[409, 64, 607, 84]
2026-08-10 15:57:02,208 INFO     29 [qwen-vl-text] coord item[2]: text=病理号：D25, bbox=[705, 98, 820, 115]
2026-08-10 15:57:02,208 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[100, 128, 182, 146]
2026-08-10 15:57:02,208 INFO     29 [qwen-vl-text] coord item[4]: text=性别：女, bbox=[392, 126, 514, 144]
2026-08-10 15:57:02,208 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：64岁, bbox=[693, 126, 841, 143]
2026-08-10 15:57:02,208 INFO     29 [qwen-vl-text] coord item[6]: text=送检医院：, bbox=[100, 153, 190, 170]
2026-08-10 15:57:02,208 INFO     29 [qwen-vl-text] coord item[7]: text=送检科室：呼吸与危重症医学科送检日期：2025-01-22, bbox=[392, 151, 902, 168]
2026-08-10 15:57:02,208 INFO     29 [qwen-vl-text] coord item[8]: text=门诊号：9, bbox=[100, 177, 220, 195]
2026-08-10 15:57:02,209 INFO     29 [qwen-vl-text] coord item[9]: text=住院号：25, bbox=[392, 176, 514, 193]
2026-08-10 15:57:02,209 INFO     29 [qwen-vl-text] coord item[10]: text=床号：21, bbox=[691, 176, 798, 192]
2026-08-10 15:57:02,209 INFO     29 [qwen-vl-text] coord item[11]: text=送检医师：周鹏飞, bbox=[100, 204, 264, 221]
2026-08-10 15:57:02,209 INFO     29 [qwen-vl-text] coord item[12]: text=送检标本：右中间段支气管, bbox=[392, 202, 633, 219]
2026-08-10 15:57:02,209 INFO     29 [qwen-vl-text] coord item[13]: text=临床诊断：, bbox=[100, 229, 190, 246]
2026-08-10 15:57:02,209 INFO     29 [qwen-vl-text] coord item[14]: text=巨检：灰白色碎组织最大径0.3厘米。全取, bbox=[103, 276, 473, 294]
2026-08-10 15:57:02,209 INFO     29 [qwen-vl-text] coord item[15]: text=病理诊断：, bbox=[113, 573, 208, 590]
2026-08-10 15:57:02,209 INFO     29 [qwen-vl-text] coord item[16]: text=(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。, bbox=[154, 589, 622, 607]
2026-08-10 15:57:02,209 INFO     29 [qwen-vl-text] coord item[17]: text=初诊医师：刘晶晶, bbox=[102, 860, 256, 878]
2026-08-10 15:57:02,209 INFO     29 [qwen-vl-text] coord item[18]: text=复诊医师：刘磊, bbox=[379, 859, 505, 876]
2026-08-10 15:57:02,209 INFO     29 [qwen-vl-text] coord item[19]: text=报告日期：2025-01-23 19:26, bbox=[656, 859, 920, 876]
2026-08-10 15:57:02,209 INFO     29 [qwen-vl-text] coord item[20]: text=备注：1.本报告单仅供临床参考 2.如临床对报告内容有疑问请与报告医生联系。联系电话：0376-6227723(西院区)；0376-6667570(东院区)。, bbox=[99, 900, 997, 914]
2026-08-10 15:57:02,209 INFO     29 [qwen-vl-text] coord item[21]: text=3.此报告必须经过病理科医师签字有效。, bbox=[144, 915, 407, 929]
2026-08-10 15:57:02,210 INFO     29 [qwen-vl-text] page=5 — 22/22 coords, api_time=15.8s
2026-08-10 15:57:02,210 INFO     29 [qwen-vl-text] new_positions (22):
[[5, 468.15999999999997, 786.016, 48.832, 97.664], [5, 503.888, 747.824, 111.616, 146.496], [5, 868.56, 1010.24, 170.912, 200.56], [5, 123.2, 224.224, 223.232, 254.624], [5, 482.944, 633.248, 219.744, 251.136], [5, 853.776, 1036.112, 219.744, 249.392], [5, 123.2, 234.07999999999998, 266.832, 296.48], [5, 482.944, 1111.264, 263.344, 292.992], [5, 123.2, 271.04, 308.688, 340.08], [5, 482.944, 633.248, 306.944, 336.592], [5, 851.312, 983.136, 306.944, 334.848], [5, 123.2, 325.248, 355.776, 385.424], [5, 482.944, 779.856, 352.288, 381.936], [5, 123.2, 234.07999999999998, 399.376, 429.024], [5, 126.896, 582.736, 481.344, 512.736], [5, 139.216, 256.256, 999.312, 1028.96], [5, 189.728, 766.304, 1027.216, 1058.608], [5, 125.664, 315.392, 1499.84, 1531.232], [5, 466.928, 622.16, 1498.096, 1527.744], [5, 808.192, 1133.44, 1498.096, 1527.744], [5, 121.968, 1228.304, 1569.6, 1594.016], [5, 177.408, 501.424, 1595.76, 1620.176]]
2026-08-10 15:57:02,210 INFO     29 [qwen-vl-text] ═══ DONE ═══ 22 positions, pages=1, time=18.4s
2026-08-10 15:57:02,210 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:57:02,216 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:57:02,216 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 15:57:02,216 INFO     29 [qwen-vl-text] positions(39): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:57:02,216 INFO     29 [qwen-vl-text] page grouping: [6], lines per page: [39]
2026-08-10 15:57:02,714 INFO     29 [qwen-vl-text] page=6, rect=1220x1696, img=(3389x4712), dpi=200
2026-08-10 15:57:02,716 INFO     29 [qwen-vl-text] LLM extraction start, text_len=765
2026-08-10 15:57:02,716 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:57:02,716 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 130, \"bbox_end\": 168, \"encounter_dates\": [\"2025-12-22\"], \"department\": \"影像科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "信阳市中心医院\n影像科CT诊断报告书\n扫描\n获取电子胶\n片和报告(试用)\n影像号: 000\n报告日期: 2025-12-22 16:36\n姓名:\n性别: 女\n年龄: 64岁\n检查日期: 2025-12-22\n科别: 日间化疗中心[东院区]院号: 2\n门诊号:/\n检查时间: 09:53:10\n检查方法: 胸部CT平扫,胸部CT增强,上腹部CT平扫,上腹部CT增强,下腹部CT平扫,下腹部CT增强\n技术参数:\n影像学所见:\n双侧胸廓对称,右肺门增大,可见不规则状软组织密度影,密度不均,边\n界不清,强化不均,右肺中下叶支气管稍变窄,双肺可见条索状及结节状高密\n度影,较大病灶位于右肺下叶内基底段见实性结节,大小约为15.8×15.4mm,\n轻度强化。右肺中叶局限性支扩。气管、支气管通畅,右肺门见明显肿大淋巴\n结,轻度强化,双侧胸膜腔及心包腔可见积液征象。与2025-8-21日片比较:\n双侧胸腔积液增多,心包积液新增,右肺门软组织密度影及淋巴结增大。\n肝脏未见明显异常密度及异常强化征象,胆囊内隐约见斑点状高密度影,\n脾脏见数个小灶状低强化影。胰腺形态、大小、密度正常。双肾见小圆形低密\n度影,边界清,增强未见明显强化。腹膜后未见明显增大淋巴结,腹腔未见明\n显积液征象。升结肠见多发小囊袋状外凸影。与2025-8-21日片比较:大致相\n仿。\n影像学意见:\n1. 右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节,转移瘤可能;建\n议追踪复查:右肺门肿大淋巴结。\n2. 双肺慢性炎症,右肺中叶局限性支扩,双侧胸腔积液,心包积液。\n3. 脾脏低密度灶,建议追踪复查。\n4. 胆囊可疑小结石。升结肠多发憩室。\n5. 双肾小囊肿。\n报告医师:\n审核医师:\n此报告仅供临床医师参考,签字生效\n打印时间: 2025-12-22 16:36:26",
    "role": "user"
  }
]
2026-08-10 15:57:02,718 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:57:02.718+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 70, "failed": 0, "current": {"3880a51e94d311f1bd9827cf206dfa2d": {"id": "3880a51e94d311f1bd9827cf206dfa2d", "doc_id": "37728ffc94d311f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909800, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377033220, "task_type": "dataflow", "root_trace_id": "4dc9fd8a1d244ef89de3e82f6546943d", "root_traceparent": "00-4dc9fd8a1d244ef89de3e82f6546943d-90143aef6fb19019-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:57:07,337 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:57:07,337 INFO     29 [qwen-vl-text] LLM output (len=852):
{
  "exam_date": "2025-12-22",
  "report_date": "2025-12-22",
  "exam_name": "胸部CT平扫,胸部CT增强,上腹部CT平扫,上腹部CT增强,下腹部CT平扫,下腹部CT增强",
  "exam_category": "imaging",
  "body_part": "胸部,上腹部,下腹部",
  "patient_name": null,
  "patient_gender": "女",
  "department": "日间化疗中心[东院区]",
  "bed_number": null,
  "findings": "双侧胸廓对称,右肺门增大,可见不规则状软组织密度影,密度不均,边界不清,强化不均,右肺中下叶支气管稍变窄,双肺可见条索状及结节状高密度影,较大病灶位于右肺下叶内基底段见实性结节,大小约为15.8×15.4mm,轻度强化。右肺中叶局限性支扩。气管、支气管通畅,右肺门见明显肿大淋巴结,轻度强化,双侧胸膜腔及心包腔可见积液征象。与2025-8-21日片比较:双侧胸腔积液增多,心包积液新增,右肺门软组织密度影及淋巴结增大。\n肝脏未见明显异常密度及异常强化征象,胆囊内隐约见斑点状高密度影,脾脏见数个小灶状低强化影。胰腺形态、大小、密度正常。双肾见小圆形低密度影,边界清,增强未见明显强化。腹膜后未见明显增大淋巴结,腹腔未见明显积液征象。升结肠见多发小囊袋状外凸影。与2025-8-21日片比较:大致相仿。",
  "conclusion": "1. 右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节,转移瘤可能;建议追踪复查:右肺门肿大淋巴结。\n2. 双肺慢性炎症,右肺中叶局限性支扩,双侧胸腔积液,心包积液。\n3. 脾脏低密度灶,建议追踪复查。\n4. 胆囊可疑小结石。升结肠多发憩室。\n5. 双肾小囊肿。",
  "physician": null,
  "reviewer": null
}
2026-08-10 15:57:07,349 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5385022, prompt_len=1495
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共39行）
["信阳市中心医院", "影像科CT诊断报告书", "扫描", "获取电子胶", "片和报告(试用)", "影像号: 000", "报告日期: 2025-12-22 16:36", "姓名:", "性别: 女", "年龄: 64岁", "检查日期: 2025-12-22", "科别: 日间化疗中心[东院区]院号: 2", "门诊号:/", "检查时间: 09:53:10", "检查方法: 胸部CT平扫,胸部CT增强,上腹部CT平扫,上腹部CT增强,下腹部CT平扫,下腹部CT增强", "技术参数:", "影像学所见:", "双侧胸廓对称,右肺门增大,可见不规则状软组织密度影,密度不均,边", "界不清,强化不均,右肺中下叶支气管稍变窄,双肺可见条索状及结节状高密", "度影,较大病灶位于右肺下叶内基底段见实性结节,大小约为15.8×15.4mm,", "轻度强化。右肺中叶局限性支扩。气管、支气管通畅,右肺门见明显肿大淋巴", "结,轻度强化,双侧胸膜腔及心包腔可见积液征象。与2025-8-21日片比较:", "双侧胸腔积液增多,心包积液新增,右肺门软组织密度影及淋巴结增大。", "肝脏未见明显异常密度及异常强化征象,胆囊内隐约见斑点状高密度影,", "脾脏见数个小灶状低强化影。胰腺形态、大小、密度正常。双肾见小圆形低密", "度影,边界清,增强未见明显强化。腹膜后未见明显增大淋巴结,腹腔未见明", "显积液征象。升结肠见多发小囊袋状外凸影。与2025-8-21日片比较:大致相", "仿。", "影像学意见:", "1. 右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节,转移瘤可能;建", "议追踪复查:右肺门肿大淋巴结。", "2. 双肺慢性炎症,右肺中叶局限性支扩,双侧胸腔积液,心包积液。", "3. 脾脏低密度灶,建议追踪复查。", "4. 胆囊可疑小结石。升结肠多发憩室。", "5. 双肾小囊肿。", "报告医师:", "审核医师:", "此报告仅供临床医师参考,签字生效", "打印时间: 2025-12-22 16:36:26"]

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
2026-08-10 15:57:29,479 INFO     29 [qwen-vl-text] coord API raw response (len=2475):
[
	{"text": "信阳市中心医院", "bbox": [401, 76, 610, 100]},
	{"text": "影像科CT诊断报告书", "bbox": [371, 116, 640, 139]},
	{"text": "扫描", "bbox": [703, 143, 734, 155]},
	{"text": "获取电子胶", "bbox": [837, 141, 902, 154]},
	{"text": "片和报告(试用)", "bbox": [703, 155, 807, 168]},
	{"text": "影像号: 000", "bbox": [92, 179, 204, 194]},
	{"text": "报告日期: 2025-12-22 16:36", "bbox": [501, 173, 744, 189]},
	{"text": "姓名:", "bbox": [96, 203, 140, 218]},
	{"text": "性别: 女", "bbox": [328, 201, 400, 216]},
	{"text": "年龄: 64岁", "bbox": [444, 200, 535, 215]},
	{"text": "检查日期: 2025-12-22", "bbox": [651, 199, 843, 214]},
	{"text": "科别: 日间化疗中心[东院区]院号: 2", "bbox": [96, 225, 405, 241]},
	{"text": "门诊号:/", "bbox": [463, 223, 538, 239]},
	{"text": "检查时间: 09:53:10", "bbox": [655, 222, 827, 238]},
	{"text": "检查方法: 胸部CT平扫,胸部CT增强,上腹部CT平扫,上腹部CT增强,下腹部CT平扫,下腹部CT增强", "bbox": [96, 251, 889, 268]},
	{"text": "技术参数:", "bbox": [96, 280, 197, 298]},
	{"text": "影像学所见:", "bbox": [96, 306, 221, 324]},
	{"text": "双侧胸廓对称,右肺门增大,可见不规则状软组织密度影,密度不均,边", "bbox": [170, 326, 930, 345]},
	{"text": "界不清,强化不均,右肺中下叶支气管稍变窄,双肺可见条索状及结节状高密", "bbox": [134, 348, 929, 367]},
	{"text": "度影,较大病灶位于右肺下叶内基底段见实性结节,大小约为15.8×15.4mm,", "bbox": [134, 369, 915, 388]},
	{"text": "轻度强化。右肺中叶局限性支扩。气管、支气管通畅,右肺门见明显肿大淋巴", "bbox": [134, 390, 929, 409]},
	{"text": "结,轻度强化,双侧胸膜腔及心包腔可见积液征象。与2025-8-21日片比较:", "bbox": [134, 411, 903, 430]},
	{"text": "双侧胸腔积液增多,心包积液新增,右肺门软组织密度影及淋巴结增大。", "bbox": [134, 433, 868, 452]},
	{"text": "肝脏未见明显异常密度及异常强化征象,胆囊内隐约见斑点状高密度影,", "bbox": [180, 454, 914, 473]},
	{"text": "脾脏见数个小灶状低强化影。胰腺形态、大小、密度正常。双肾见小圆形低密", "bbox": [134, 475, 928, 494]},
	{"text": "度影,边界清,增强未见明显强化。腹膜后未见明显增大淋巴结,腹腔未见明", "bbox": [134, 496, 927, 515]},
	{"text": "显积液征象。升结肠见多发小囊袋状外凸影。与2025-8-21日片比较:大致相", "bbox": [134, 517, 917, 536]},
	{"text": "仿。", "bbox": [134, 540, 167, 558]},
	{"text": "影像学意见:", "bbox": [100, 714, 225, 731]},
	{"text": "1. 右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节,转移瘤可能;建", "bbox": [134, 732, 917, 750]},
	{"text": "议追踪复查:右肺门肿大淋巴结。", "bbox": [134, 752, 467, 770]},
	{"text": "2. 双肺慢性炎症,右肺中叶局限性支扩,双侧胸腔积液,心包积液。", "bbox": [131, 773, 832, 792]},
	{"text": "3. 脾脏低密度灶,建议追踪复查。", "bbox": [131, 795, 478, 813]},
	{"text": "4. 胆囊可疑小结石。升结肠多发憩室。", "bbox": [131, 816, 524, 835]},
	{"text": "5. 双肾小囊肿。", "bbox": [131, 838, 293, 857]},
	{"text": "报告医师:", "bbox": [94, 902, 165, 916]},
	{"text": "审核医师:", "bbox": [667, 905, 740, 918]},
	{"text": "此报告仅供临床医师参考,签字生效", "bbox": [94, 943, 375, 959]},
	{"text": "打印时间: 2025-12-22 16:36:26", "bbox": [625, 954, 900, 969]}
]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord API: raw_items=39, valid_items=39, elapsed=22.1s
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[0]: text=信阳市中心医院, bbox=[401, 76, 610, 100]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[1]: text=影像科CT诊断报告书, bbox=[371, 116, 640, 139]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[2]: text=扫描, bbox=[703, 143, 734, 155]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[3]: text=获取电子胶, bbox=[837, 141, 902, 154]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[4]: text=片和报告(试用), bbox=[703, 155, 807, 168]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[5]: text=影像号: 000, bbox=[92, 179, 204, 194]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[6]: text=报告日期: 2025-12-22 16:36, bbox=[501, 173, 744, 189]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[7]: text=姓名:, bbox=[96, 203, 140, 218]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[8]: text=性别: 女, bbox=[328, 201, 400, 216]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[9]: text=年龄: 64岁, bbox=[444, 200, 535, 215]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[10]: text=检查日期: 2025-12-22, bbox=[651, 199, 843, 214]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[11]: text=科别: 日间化疗中心[东院区]院号: 2, bbox=[96, 225, 405, 241]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[12]: text=门诊号:/, bbox=[463, 223, 538, 239]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[13]: text=检查时间: 09:53:10, bbox=[655, 222, 827, 238]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[14]: text=检查方法: 胸部CT平扫,胸部CT增强,上腹部CT平扫,上腹部CT增强,下腹部CT平扫,下腹部CT增强, bbox=[96, 251, 889, 268]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[15]: text=技术参数:, bbox=[96, 280, 197, 298]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[16]: text=影像学所见:, bbox=[96, 306, 221, 324]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[17]: text=双侧胸廓对称,右肺门增大,可见不规则状软组织密度影,密度不均,边, bbox=[170, 326, 930, 345]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[18]: text=界不清,强化不均,右肺中下叶支气管稍变窄,双肺可见条索状及结节状高密, bbox=[134, 348, 929, 367]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[19]: text=度影,较大病灶位于右肺下叶内基底段见实性结节,大小约为15.8×15.4mm,, bbox=[134, 369, 915, 388]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[20]: text=轻度强化。右肺中叶局限性支扩。气管、支气管通畅,右肺门见明显肿大淋巴, bbox=[134, 390, 929, 409]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[21]: text=结,轻度强化,双侧胸膜腔及心包腔可见积液征象。与2025-8-21日片比较:, bbox=[134, 411, 903, 430]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[22]: text=双侧胸腔积液增多,心包积液新增,右肺门软组织密度影及淋巴结增大。, bbox=[134, 433, 868, 452]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[23]: text=肝脏未见明显异常密度及异常强化征象,胆囊内隐约见斑点状高密度影,, bbox=[180, 454, 914, 473]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[24]: text=脾脏见数个小灶状低强化影。胰腺形态、大小、密度正常。双肾见小圆形低密, bbox=[134, 475, 928, 494]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[25]: text=度影,边界清,增强未见明显强化。腹膜后未见明显增大淋巴结,腹腔未见明, bbox=[134, 496, 927, 515]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[26]: text=显积液征象。升结肠见多发小囊袋状外凸影。与2025-8-21日片比较:大致相, bbox=[134, 517, 917, 536]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[27]: text=仿。, bbox=[134, 540, 167, 558]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[28]: text=影像学意见:, bbox=[100, 714, 225, 731]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[29]: text=1. 右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节,转移瘤可能;建, bbox=[134, 732, 917, 750]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[30]: text=议追踪复查:右肺门肿大淋巴结。, bbox=[134, 752, 467, 770]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[31]: text=2. 双肺慢性炎症,右肺中叶局限性支扩,双侧胸腔积液,心包积液。, bbox=[131, 773, 832, 792]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[32]: text=3. 脾脏低密度灶,建议追踪复查。, bbox=[131, 795, 478, 813]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[33]: text=4. 胆囊可疑小结石。升结肠多发憩室。, bbox=[131, 816, 524, 835]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[34]: text=5. 双肾小囊肿。, bbox=[131, 838, 293, 857]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[35]: text=报告医师:, bbox=[94, 902, 165, 916]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[36]: text=审核医师:, bbox=[667, 905, 740, 918]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[37]: text=此报告仅供临床医师参考,签字生效, bbox=[94, 943, 375, 959]
2026-08-10 15:57:29,480 INFO     29 [qwen-vl-text] coord item[38]: text=打印时间: 2025-12-22 16:36:26, bbox=[625, 954, 900, 969]
2026-08-10 15:57:29,481 INFO     29 [qwen-vl-text] page=6 — 39/39 coords, api_time=22.1s
2026-08-10 15:57:29,481 INFO     29 [qwen-vl-text] new_positions (39):
[[6, 489.21999999999997, 744.1999999999999, 128.896, 169.6], [6, 452.62, 780.8, 196.736, 235.744], [6, 857.66, 895.48, 242.528, 262.88], [6, 1021.14, 1100.44, 239.136, 261.18399999999997], [6, 857.66, 984.54, 262.88, 284.928], [6, 112.24, 248.88, 303.584, 329.024], [6, 611.22, 907.68, 293.408, 320.544], [6, 117.12, 170.79999999999998, 344.288, 369.728], [6, 400.15999999999997, 488.0, 340.896, 366.336], [6, 541.68, 652.6999999999999, 339.2, 364.64], [6, 794.22, 1028.46, 337.50399999999996, 362.944], [6, 117.12, 494.09999999999997, 381.59999999999997, 408.736], [6, 564.86, 656.36, 378.20799999999997, 405.344], [6, 799.1, 1008.9399999999999, 376.512, 403.64799999999997], [6, 117.12, 1084.58, 425.69599999999997, 454.52799999999996], [6, 117.12, 240.34, 474.88, 505.40799999999996], [6, 117.12, 269.62, 518.976, 549.504], [6, 207.4, 1134.6, 552.896, 585.12], [6, 163.48, 1133.3799999999999, 590.208, 622.432], [6, 163.48, 1116.3, 625.824, 658.048], [6, 163.48, 1133.3799999999999, 661.4399999999999, 693.664], [6, 163.48, 1101.66, 697.0559999999999, 729.28], [6, 163.48, 1058.96, 734.3679999999999, 766.592], [6, 219.6, 1115.08, 769.9839999999999, 802.208], [6, 163.48, 1132.16, 805.6, 837.824], [6, 163.48, 1130.94, 841.216, 873.4399999999999], [6, 163.48, 1118.74, 876.832, 909.0559999999999], [6, 163.48, 203.74, 915.8399999999999, 946.3679999999999], [6, 122.0, 274.5, 1210.944, 1239.776], [6, 163.48, 1118.74, 1241.472, 1272.0], [6, 163.48, 569.74, 1275.392, 1305.92], [6, 159.82, 1015.04, 1311.008, 1343.232], [6, 159.82, 583.16, 1348.32, 1378.848], [6, 159.82, 639.28, 1383.936, 1416.1599999999999], [6, 159.82, 357.46, 1421.248, 1453.472], [6, 114.67999999999999, 201.29999999999998, 1529.792, 1553.536], [6, 813.74, 902.8, 1534.8799999999999, 1556.9279999999999], [6, 114.67999999999999, 457.5, 1599.328, 1626.464], [6, 762.5, 1098.0, 1617.984, 1643.424]]
2026-08-10 15:57:29,481 INFO     29 [qwen-vl-text] ═══ DONE ═══ 39 positions, pages=1, time=27.3s
2026-08-10 15:57:29,481 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:57:29,482 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:57:29,482 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 15:57:29,482 INFO     29 [qwen-vl-text] positions(35): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:57:29,483 INFO     29 [qwen-vl-text] page grouping: [7], lines per page: [35]
2026-08-10 15:57:29,986 INFO     29 [qwen-vl-text] page=7, rect=1260x1776, img=(3500x4934), dpi=200
2026-08-10 15:57:29,990 INFO     29 [qwen-vl-text] LLM extraction start, text_len=509
2026-08-10 15:57:29,990 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:57:29,990 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 169, \"bbox_end\": 203, \"encounter_dates\": [\"2026-02-25\"], \"department\": \"影像科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "信阳市中心医院\n影像科CT诊断报告书\n扫描此二维码可\n电子胶\n片和报告(试用)\n影像号:0000\n报告日期:2026-02-25 15:36\n姓名:\n性别:女\n年龄:65岁\n检查日期:2026-02-25\n科别:肿瘤内科五门诊[东院住院号:/\n门诊号:1\n6\n检查时间:08:57:41\n检查方法:胸部CT平扫加薄层\n技术参数:\n影像学所见:\n双侧胸廓对称,右肺门增大,可见不规则状软组织密度影,密度不均,边\n界不清,右肺中下叶支气管稍变窄,双肺可见条索状及结节状高密度影。右肺\n中叶局限性支扩。气管、支气管通畅,右肺门见明显肿大淋巴结,右侧胸膜局\n部稍厚,双侧胸膜腔及心包腔可见积液征象。与2025-12-22日片比较:右侧胸\n腔积液增多,右肺门软组织密度影及淋巴结进一步增大,右肺结节增大,右侧\n胸膜局部稍增厚。\n影像学意见:\n1.右肺癌并右肺中下叶不张治疗状态。双肺多发结节,转移瘤可能;右肺门\n肿大淋巴结转移。\n2.双肺慢性炎症,双侧胸腔积液,心包积液。\n3.右侧胸膜局部稍厚,不除外转移。\n报告医师:\n肖健\n审核医师:\n贺玲\n此报告仅供临床医师参考,签字生效\n打印时间:2026-02-25 15:36:58",
    "role": "user"
  }
]
2026-08-10 15:57:33,306 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:57:33,306 INFO     29 [qwen-vl-text] LLM output (len=583):
{
  "exam_date": "2026-02-25",
  "report_date": "2026-02-25",
  "exam_name": "胸部CT平扫加薄层",
  "exam_category": "imaging",
  "body_part": "胸部",
  "patient_name": null,
  "patient_gender": "女",
  "department": "肿瘤内科五门诊",
  "bed_number": null,
  "findings": "双侧胸廓对称,右肺门增大,可见不规则状软组织密度影,密度不均,边界不清,右肺中下叶支气管稍变窄,双肺可见条索状及结节状高密度影。右肺中叶局限性支扩。气管、支气管通畅,右肺门见明显肿大淋巴结,右侧胸膜局部稍厚,双侧胸膜腔及心包腔可见积液征象。与2025-12-22日片比较:右侧胸腔积液增多,右肺门软组织密度影及淋巴结进一步增大,右肺结节增大,右侧胸膜局部稍增厚。",
  "conclusion": "1.右肺癌并右肺中下叶不张治疗状态。双肺多发结节,转移瘤可能;右肺门肿大淋巴结转移。\n2.双肺慢性炎症,双侧胸腔积液,心包积液。\n3.右侧胸膜局部稍厚,不除外转移。",
  "physician": "肖健",
  "reviewer": "贺玲"
}
2026-08-10 15:57:33,324 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=6567477, prompt_len=1227
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共35行）
["信阳市中心医院", "影像科CT诊断报告书", "扫描此二维码可", "电子胶", "片和报告(试用)", "影像号:0000", "报告日期:2026-02-25 15:36", "姓名:", "性别:女", "年龄:65岁", "检查日期:2026-02-25", "科别:肿瘤内科五门诊[东院住院号:/", "门诊号:1", "6", "检查时间:08:57:41", "检查方法:胸部CT平扫加薄层", "技术参数:", "影像学所见:", "双侧胸廓对称,右肺门增大,可见不规则状软组织密度影,密度不均,边", "界不清,右肺中下叶支气管稍变窄,双肺可见条索状及结节状高密度影。右肺", "中叶局限性支扩。气管、支气管通畅,右肺门见明显肿大淋巴结,右侧胸膜局", "部稍厚,双侧胸膜腔及心包腔可见积液征象。与2025-12-22日片比较:右侧胸", "腔积液增多,右肺门软组织密度影及淋巴结进一步增大,右肺结节增大,右侧", "胸膜局部稍增厚。", "影像学意见:", "1.右肺癌并右肺中下叶不张治疗状态。双肺多发结节,转移瘤可能;右肺门", "肿大淋巴结转移。", "2.双肺慢性炎症,双侧胸腔积液,心包积液。", "3.右侧胸膜局部稍厚,不除外转移。", "报告医师:", "肖健", "审核医师:", "贺玲", "此报告仅供临床医师参考,签字生效", "打印时间:2026-02-25 15:36:58"]

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
2026-08-10 15:57:51,956 INFO     29 [qwen-vl-text] coord API raw response (len=2049):
[
	{"text": "信阳市中心医院", "bbox": [412, 73, 620, 97]},
	{"text": "影像科CT诊断报告书", "bbox": [381, 114, 650, 137]},
	{"text": "扫描此二维码可", "bbox": [712, 143, 814, 155]},
	{"text": "电子胶", "bbox": [850, 143, 905, 155]},
	{"text": "片和报告(试用)", "bbox": [712, 155, 814, 167]},
	{"text": "影像号:0000", "bbox": [96, 171, 208, 187]},
	{"text": "报告日期:2026-02-25 15:36", "bbox": [512, 171, 753, 187]},
	{"text": "姓名:", "bbox": [100, 196, 145, 211]},
	{"text": "性别:女", "bbox": [338, 197, 410, 213]},
	{"text": "年龄:65岁", "bbox": [455, 197, 547, 213]},
	{"text": "检查日期:2026-02-25", "bbox": [661, 197, 850, 213]},
	{"text": "科别:肿瘤内科五门诊[东院住院号:/", "bbox": [100, 219, 412, 236]},
	{"text": "门诊号:1", "bbox": [474, 220, 547, 236]},
	{"text": "6", "bbox": [610, 222, 618, 235]},
	{"text": "检查时间:08:57:41", "bbox": [666, 220, 833, 236]},
	{"text": "检查方法:胸部CT平扫加薄层", "bbox": [100, 248, 373, 266]},
	{"text": "技术参数:", "bbox": [100, 274, 205, 292]},
	{"text": "影像学所见:", "bbox": [100, 300, 228, 318]},
	{"text": "双侧胸廓对称,右肺门增大,可见不规则状软组织密度影,密度不均,边", "bbox": [185, 325, 935, 344]},
	{"text": "界不清,右肺中下叶支气管稍变窄,双肺可见条索状及结节状高密度影。右肺", "bbox": [140, 347, 935, 366]},
	{"text": "中叶局限性支扩。气管、支气管通畅,右肺门见明显肿大淋巴结,右侧胸膜局", "bbox": [140, 369, 935, 388]},
	{"text": "部稍厚,双侧胸膜腔及心包腔可见积液征象。与2025-12-22日片比较:右侧胸", "bbox": [140, 390, 935, 409]},
	{"text": "腔积液增多,右肺门软组织密度影及淋巴结进一步增大,右肺结节增大,右侧", "bbox": [140, 412, 935, 431]},
	{"text": "胸膜局部稍增厚。", "bbox": [140, 434, 315, 452]},
	{"text": "影像学意见:", "bbox": [104, 719, 233, 736]},
	{"text": "1.右肺癌并右肺中下叶不张治疗状态。双肺多发结节,转移瘤可能;右肺门", "bbox": [138, 738, 922, 756]},
	{"text": "肿大淋巴结转移。", "bbox": [138, 759, 315, 777]},
	{"text": "2.双肺慢性炎症,双侧胸腔积液,心包积液。", "bbox": [138, 781, 607, 799]},
	{"text": "3.右侧胸膜局部稍厚,不除外转移。", "bbox": [138, 803, 514, 821]},
	{"text": "报告医师:", "bbox": [100, 910, 173, 924]},
	{"text": "肖健", "bbox": [205, 910, 294, 937]},
	{"text": "审核医师:", "bbox": [678, 910, 750, 924]},
	{"text": "贺玲", "bbox": [798, 910, 857, 937]},
	{"text": "此报告仅供临床医师参考,签字生效", "bbox": [100, 952, 388, 967]},
	{"text": "打印时间:2026-02-25 15:36:58", "bbox": [638, 958, 905, 972]}
]
2026-08-10 15:57:51,956 INFO     29 [qwen-vl-text] coord API: raw_items=35, valid_items=35, elapsed=18.6s
2026-08-10 15:57:51,957 INFO     29 [qwen-vl-text] coord item[0]: text=信阳市中心医院, bbox=[412, 73, 620, 97]
2026-08-10 15:57:51,957 INFO     29 [qwen-vl-text] coord item[1]: text=影像科CT诊断报告书, bbox=[381, 114, 650, 137]
2026-08-10 15:57:51,957 INFO     29 [qwen-vl-text] coord item[2]: text=扫描此二维码可, bbox=[712, 143, 814, 155]
2026-08-10 15:57:51,957 INFO     29 [qwen-vl-text] coord item[3]: text=电子胶, bbox=[850, 143, 905, 155]
2026-08-10 15:57:51,957 INFO     29 [qwen-vl-text] coord item[4]: text=片和报告(试用), bbox=[712, 155, 814, 167]
2026-08-10 15:57:51,957 INFO     29 [qwen-vl-text] coord item[5]: text=影像号:0000, bbox=[96, 171, 208, 187]
2026-08-10 15:57:51,957 INFO     29 [qwen-vl-text] coord item[6]: text=报告日期:2026-02-25 15:36, bbox=[512, 171, 753, 187]
2026-08-10 15:57:51,957 INFO     29 [qwen-vl-text] coord item[7]: text=姓名:, bbox=[100, 196, 145, 211]
2026-08-10 15:57:51,957 INFO     29 [qwen-vl-text] coord item[8]: text=性别:女, bbox=[338, 197, 410, 213]
2026-08-10 15:57:51,957 INFO     29 [qwen-vl-text] coord item[9]: text=年龄:65岁, bbox=[455, 197, 547, 213]
2026-08-10 15:57:51,957 INFO     29 [qwen-vl-text] coord item[10]: text=检查日期:2026-02-25, bbox=[661, 197, 850, 213]
2026-08-10 15:57:51,957 INFO     29 [qwen-vl-text] coord item[11]: text=科别:肿瘤内科五门诊[东院住院号:/, bbox=[100, 219, 412, 236]
2026-08-10 15:57:51,958 INFO     29 [qwen-vl-text] coord item[12]: text=门诊号:1, bbox=[474, 220, 547, 236]
2026-08-10 15:57:51,958 INFO     29 [qwen-vl-text] coord item[13]: text=6, bbox=[610, 222, 618, 235]
2026-08-10 15:57:51,958 INFO     29 [qwen-vl-text] coord item[14]: text=检查时间:08:57:41, bbox=[666, 220, 833, 236]
2026-08-10 15:57:51,958 INFO     29 [qwen-vl-text] coord item[15]: text=检查方法:胸部CT平扫加薄层, bbox=[100, 248, 373, 266]
2026-08-10 15:57:51,958 INFO     29 [qwen-vl-text] coord item[16]: text=技术参数:, bbox=[100, 274, 205, 292]
2026-08-10 15:57:51,958 INFO     29 [qwen-vl-text] coord item[17]: text=影像学所见:, bbox=[100, 300, 228, 318]
2026-08-10 15:57:51,958 INFO     29 [qwen-vl-text] coord item[18]: text=双侧胸廓对称,右肺门增大,可见不规则状软组织密度影,密度不均,边, bbox=[185, 325, 935, 344]
2026-08-10 15:57:51,958 INFO     29 [qwen-vl-text] coord item[19]: text=界不清,右肺中下叶支气管稍变窄,双肺可见条索状及结节状高密度影。右肺, bbox=[140, 347, 935, 366]
2026-08-10 15:57:51,958 INFO     29 [qwen-vl-text] coord item[20]: text=中叶局限性支扩。气管、支气管通畅,右肺门见明显肿大淋巴结,右侧胸膜局, bbox=[140, 369, 935, 388]
2026-08-10 15:57:51,958 INFO     29 [qwen-vl-text] coord item[21]: text=部稍厚,双侧胸膜腔及心包腔可见积液征象。与2025-12-22日片比较:右侧胸, bbox=[140, 390, 935, 409]
2026-08-10 15:57:51,958 INFO     29 [qwen-vl-text] coord item[22]: text=腔积液增多,右肺门软组织密度影及淋巴结进一步增大,右肺结节增大,右侧, bbox=[140, 412, 935, 431]
2026-08-10 15:57:51,958 INFO     29 [qwen-vl-text] coord item[23]: text=胸膜局部稍增厚。, bbox=[140, 434, 315, 452]
2026-08-10 15:57:51,958 INFO     29 [qwen-vl-text] coord item[24]: text=影像学意见:, bbox=[104, 719, 233, 736]
2026-08-10 15:57:51,958 INFO     29 [qwen-vl-text] coord item[25]: text=1.右肺癌并右肺中下叶不张治疗状态。双肺多发结节,转移瘤可能;右肺门, bbox=[138, 738, 922, 756]
2026-08-10 15:57:51,958 INFO     29 [qwen-vl-text] coord item[26]: text=肿大淋巴结转移。, bbox=[138, 759, 315, 777]
2026-08-10 15:57:51,958 INFO     29 [qwen-vl-text] coord item[27]: text=2.双肺慢性炎症,双侧胸腔积液,心包积液。, bbox=[138, 781, 607, 799]
2026-08-10 15:57:51,958 INFO     29 [qwen-vl-text] coord item[28]: text=3.右侧胸膜局部稍厚,不除外转移。, bbox=[138, 803, 514, 821]
2026-08-10 15:57:51,958 INFO     29 [qwen-vl-text] coord item[29]: text=报告医师:, bbox=[100, 910, 173, 924]
2026-08-10 15:57:51,958 INFO     29 [qwen-vl-text] coord item[30]: text=肖健, bbox=[205, 910, 294, 937]
2026-08-10 15:57:51,958 INFO     29 [qwen-vl-text] coord item[31]: text=审核医师:, bbox=[678, 910, 750, 924]
2026-08-10 15:57:51,958 INFO     29 [qwen-vl-text] coord item[32]: text=贺玲, bbox=[798, 910, 857, 937]
2026-08-10 15:57:51,958 INFO     29 [qwen-vl-text] coord item[33]: text=此报告仅供临床医师参考,签字生效, bbox=[100, 952, 388, 967]
2026-08-10 15:57:51,958 INFO     29 [qwen-vl-text] coord item[34]: text=打印时间:2026-02-25 15:36:58, bbox=[638, 958, 905, 972]
2026-08-10 15:57:51,960 INFO     29 [qwen-vl-text] page=7 — 35/35 coords, api_time=18.6s
2026-08-10 15:57:51,960 INFO     29 [qwen-vl-text] new_positions (35):
[[7, 519.12, 781.2, 129.648, 172.272], [7, 480.06, 819.0, 202.464, 243.312], [7, 897.12, 1025.64, 253.968, 275.28000000000003], [7, 1071.0, 1140.3, 253.968, 275.28000000000003], [7, 897.12, 1025.64, 275.28000000000003, 296.592], [7, 120.96000000000001, 262.08, 303.696, 332.112], [7, 645.12, 948.78, 303.696, 332.112], [7, 126.0, 182.7, 348.096, 374.736], [7, 425.88, 516.6, 349.872, 378.288], [7, 573.3, 689.22, 349.872, 378.288], [7, 832.86, 1071.0, 349.872, 378.288], [7, 126.0, 519.12, 388.944, 419.136], [7, 597.24, 689.22, 390.72, 419.136], [7, 768.6, 778.68, 394.272, 417.36], [7, 839.16, 1049.58, 390.72, 419.136], [7, 126.0, 469.98, 440.448, 472.416], [7, 126.0, 258.3, 486.624, 518.592], [7, 126.0, 287.28000000000003, 532.8, 564.768], [7, 233.1, 1178.1, 577.2, 610.944], [7, 176.4, 1178.1, 616.272, 650.016], [7, 176.4, 1178.1, 655.344, 689.088], [7, 176.4, 1178.1, 692.64, 726.384], [7, 176.4, 1178.1, 731.712, 765.456], [7, 176.4, 396.9, 770.784, 802.7520000000001], [7, 131.04, 293.58, 1276.944, 1307.136], [7, 173.88, 1161.72, 1310.688, 1342.656], [7, 173.88, 396.9, 1347.984, 1379.952], [7, 173.88, 764.82, 1387.056, 1419.0240000000001], [7, 173.88, 647.64, 1426.128, 1458.096], [7, 126.0, 217.98, 1616.16, 1641.0240000000001], [7, 258.3, 370.44, 1616.16, 1664.112], [7, 854.28, 945.0, 1616.16, 1641.0240000000001], [7, 1005.48, 1079.82, 1616.16, 1664.112], [7, 126.0, 488.88, 1690.752, 1717.392], [7, 803.88, 1140.3, 1701.4080000000001, 1726.272]]
2026-08-10 15:57:51,960 INFO     29 [qwen-vl-text] ═══ DONE ═══ 35 positions, pages=1, time=22.5s
2026-08-10 15:57:51,960 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:57:51,961 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:57:51,961 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 15:57:51,961 INFO     29 [qwen-vl-text] positions(43): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:57:51,961 INFO     29 [qwen-vl-text] page grouping: [8], lines per page: [43]
2026-08-10 15:57:52,799 INFO     29 [qwen-vl-text] page=8, rect=2188x1632, img=(6078x4534), dpi=200
2026-08-10 15:57:52,803 INFO     29 [qwen-vl-text] LLM extraction start, text_len=357
2026-08-10 15:57:52,803 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:57:52,803 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 204, \"bbox_end\": 246, \"encounter_dates\": [\"2026-03-23\"], \"department\": \"心电图室\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "信阳市中心医院心电图报告单\n门诊号:\n姓名:\nP波宽度: 141ms\n诊断: 1.窦性心律\n住院号: 0000\n性别: 女\nP-R间期: 181ms\n【120-200】\n2.低电压\n床位号: 04\n年龄: 65岁\nQRS时限: 101ms\n【60-110】\n科室: 日间化疗中心[心率: 77bpm\n【60-100】\nQT/QTc: 358/406ms\n【360-440】\n东院区]\n电轴: 60°\n【-30-90】\n2026-03-23 08:43:55\n25mm/s 10mm/mV\nI\nV1\nV3R\nII\nV2\nIII\nV3\nV4R\naVR\nV4\naVL\nV5\nV5R\naVF\nV6\nII\n检查时间: 2026/3/23 8:43:55\n报告时间: 2026/3/23 8:59:30\n报告医生:\n审核医生:",
    "role": "user"
  }
]
2026-08-10 15:57:52,805 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:57:52.804+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 70, "failed": 0, "current": {"3880a51e94d311f1bd9827cf206dfa2d": {"id": "3880a51e94d311f1bd9827cf206dfa2d", "doc_id": "37728ffc94d311f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909800, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786377033220, "task_type": "dataflow", "root_trace_id": "4dc9fd8a1d244ef89de3e82f6546943d", "root_traceparent": "00-4dc9fd8a1d244ef89de3e82f6546943d-90143aef6fb19019-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:57:58,128 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:57:58,128 INFO     29 [qwen-vl-text] LLM output (len=531):
{
  "exam_date": "2026-03-23",
  "report_date": "2026-03-23",
  "exam_name": "心电图",
  "exam_category": "other",
  "body_part": "心脏",
  "patient_name": null,
  "patient_gender": "女",
  "department": "日间化疗中心[东院区]",
  "bed_number": "04",
  "findings": "P波宽度: 141ms\nP-R间期: 181ms 【120-200】\nQRS时限: 101ms 【60-110】\n[心率: 77bpm 【60-100】\nQT/QTc: 358/406ms 【360-440】\n电轴: 60° 【-30-90】\n25mm/s 10mm/mV\nI V1 V3R\nII V2 III V3 V4R\naVR V4 aVL V5 V5R\naVF V6 II",
  "conclusion": "诊断: 1.窦性心律\n2.低电压",
  "physician": null,
  "reviewer": null
}
2026-08-10 15:57:58,150 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9895249, prompt_len=1099
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共43行）
["信阳市中心医院心电图报告单", "门诊号:", "姓名:", "P波宽度: 141ms", "诊断: 1.窦性心律", "住院号: 0000", "性别: 女", "P-R间期: 181ms", "【120-200】", "2.低电压", "床位号: 04", "年龄: 65岁", "QRS时限: 101ms", "【60-110】", "科室: 日间化疗中心[心率: 77bpm", "【60-100】", "QT/QTc: 358/406ms", "【360-440】", "东院区]", "电轴: 60°", "【-30-90】", "2026-03-23 08:43:55", "25mm/s 10mm/mV", "I", "V1", "V3R", "II", "V2", "III", "V3", "V4R", "aVR", "V4", "aVL", "V5", "V5R", "aVF", "V6", "II", "检查时间: 2026/3/23 8:43:55", "报告时间: 2026/3/23 8:59:30", "报告医生:", "审核医生:"]

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
2026-08-10 15:58:17,333 INFO     29 [qwen-vl-text] coord API raw response (len=2227):
[
	{"text": "信阳市中心医院心电图报告单", "bbox": [388, 24, 636, 52]},
	{"text": "门诊号:", "bbox": [58, 85, 104, 105]},
	{"text": "姓名:", "bbox": [208, 84, 254, 104]},
	{"text": "P波宽度: 141ms", "bbox": [408, 82, 513, 102]},
	{"text": "诊断: 1.窦性心律", "bbox": [664, 70, 773, 92]},
	{"text": "住院号: 0000", "bbox": [58, 117, 144, 137]},
	{"text": "性别: 女", "bbox": [208, 115, 284, 135]},
	{"text": "P-R间期: 181ms", "bbox": [408, 107, 513, 127]},
	{"text": "【120-200】", "bbox": [582, 107, 645, 126]},
	{"text": "2.低电压", "bbox": [707, 91, 760, 110]},
	{"text": "床位号: 04", "bbox": [58, 150, 136, 170]},
	{"text": "年龄: 65岁", "bbox": [208, 148, 296, 168]},
	{"text": "QRS时限: 101ms", "bbox": [408, 132, 513, 151]},
	{"text": "【60-110】", "bbox": [582, 134, 639, 152]},
	{"text": "科室: 日间化疗中心[心率: 77bpm", "bbox": [58, 181, 304, 201]},
	{"text": "【60-100】", "bbox": [337, 181, 392, 200]},
	{"text": "QT/QTc: 358/406ms", "bbox": [408, 155, 539, 175]},
	{"text": "【360-440】", "bbox": [582, 157, 645, 175]},
	{"text": "东院区]", "bbox": [117, 196, 161, 215]},
	{"text": "电轴: 60°", "bbox": [411, 182, 497, 202]},
	{"text": "【-30-90】", "bbox": [582, 183, 639, 201]},
	{"text": "2026-03-23 08:43:55", "bbox": [86, 235, 203, 253]},
	{"text": "25mm/s 10mm/mV", "bbox": [824, 234, 940, 253]},
	{"text": "I", "bbox": [87, 278, 97, 295]},
	{"text": "V1", "bbox": [367, 277, 383, 295]},
	{"text": "V3R", "bbox": [650, 277, 676, 294]},
	{"text": "II", "bbox": [87, 372, 98, 389]},
	{"text": "V2", "bbox": [367, 372, 385, 390]},
	{"text": "III", "bbox": [86, 467, 98, 484]},
	{"text": "V3", "bbox": [367, 467, 385, 485]},
	{"text": "V4R", "bbox": [650, 467, 676, 485]},
	{"text": "aVR", "bbox": [85, 561, 109, 578]},
	{"text": "V4", "bbox": [367, 561, 385, 579]},
	{"text": "aVL", "bbox": [85, 656, 108, 673]},
	{"text": "V5", "bbox": [367, 656, 385, 674]},
	{"text": "V5R", "bbox": [650, 656, 676, 674]},
	{"text": "aVF", "bbox": [85, 750, 108, 768]},
	{"text": "V6", "bbox": [367, 750, 385, 768]},
	{"text": "II", "bbox": [86, 845, 98, 862]},
	{"text": "检查时间: 2026/3/23 8:43:55", "bbox": [58, 945, 238, 965]},
	{"text": "报告时间: 2026/3/23 8:59:30", "bbox": [297, 944, 486, 964]},
	{"text": "报告医生:", "bbox": [563, 943, 620, 963]},
	{"text": "审核医生:", "bbox": [751, 944, 809, 964]}
]
2026-08-10 15:58:17,334 INFO     29 [qwen-vl-text] coord API: raw_items=43, valid_items=43, elapsed=19.2s
2026-08-10 15:58:17,334 INFO     29 [qwen-vl-text] coord item[0]: text=信阳市中心医院心电图报告单, bbox=[388, 24, 636, 52]
2026-08-10 15:58:17,334 INFO     29 [qwen-vl-text] coord item[1]: text=门诊号:, bbox=[58, 85, 104, 105]
2026-08-10 15:58:17,334 INFO     29 [qwen-vl-text] coord item[2]: text=姓名:, bbox=[208, 84, 254, 104]
2026-08-10 15:58:17,334 INFO     29 [qwen-vl-text] coord item[3]: text=P波宽度: 141ms, bbox=[408, 82, 513, 102]
2026-08-10 15:58:17,334 INFO     29 [qwen-vl-text] coord item[4]: text=诊断: 1.窦性心律, bbox=[664, 70, 773, 92]
2026-08-10 15:58:17,334 INFO     29 [qwen-vl-text] coord item[5]: text=住院号: 0000, bbox=[58, 117, 144, 137]
2026-08-10 15:58:17,334 INFO     29 [qwen-vl-text] coord item[6]: text=性别: 女, bbox=[208, 115, 284, 135]
2026-08-10 15:58:17,334 INFO     29 [qwen-vl-text] coord item[7]: text=P-R间期: 181ms, bbox=[408, 107, 513, 127]
2026-08-10 15:58:17,334 INFO     29 [qwen-vl-text] coord item[8]: text=【120-200】, bbox=[582, 107, 645, 126]
2026-08-10 15:58:17,335 INFO     29 [qwen-vl-text] coord item[9]: text=2.低电压, bbox=[707, 91, 760, 110]
2026-08-10 15:58:17,335 INFO     29 [qwen-vl-text] coord item[10]: text=床位号: 04, bbox=[58, 150, 136, 170]
2026-08-10 15:58:17,335 INFO     29 [qwen-vl-text] coord item[11]: text=年龄: 65岁, bbox=[208, 148, 296, 168]
2026-08-10 15:58:17,335 INFO     29 [qwen-vl-text] coord item[12]: text=QRS时限: 101ms, bbox=[408, 132, 513, 151]
2026-08-10 15:58:17,335 INFO     29 [qwen-vl-text] coord item[13]: text=【60-110】, bbox=[582, 134, 639, 152]
2026-08-10 15:58:17,335 INFO     29 [qwen-vl-text] coord item[14]: text=科室: 日间化疗中心[心率: 77bpm, bbox=[58, 181, 304, 201]
2026-08-10 15:58:17,335 INFO     29 [qwen-vl-text] coord item[15]: text=【60-100】, bbox=[337, 181, 392, 200]
2026-08-10 15:58:17,335 INFO     29 [qwen-vl-text] coord item[16]: text=QT/QTc: 358/406ms, bbox=[408, 155, 539, 175]
2026-08-10 15:58:17,335 INFO     29 [qwen-vl-text] coord item[17]: text=【360-440】, bbox=[582, 157, 645, 175]
2026-08-10 15:58:17,335 INFO     29 [qwen-vl-text] coord item[18]: text=东院区], bbox=[117, 196, 161, 215]
2026-08-10 15:58:17,335 INFO     29 [qwen-vl-text] coord item[19]: text=电轴: 60°, bbox=[411, 182, 497, 202]
2026-08-10 15:58:17,335 INFO     29 [qwen-vl-text] coord item[20]: text=【-30-90】, bbox=[582, 183, 639, 201]
2026-08-10 15:58:17,335 INFO     29 [qwen-vl-text] coord item[21]: text=2026-03-23 08:43:55, bbox=[86, 235, 203, 253]
2026-08-10 15:58:17,335 INFO     29 [qwen-vl-text] coord item[22]: text=25mm/s 10mm/mV, bbox=[824, 234, 940, 253]
2026-08-10 15:58:17,336 INFO     29 [qwen-vl-text] coord item[23]: text=I, bbox=[87, 278, 97, 295]
2026-08-10 15:58:17,336 INFO     29 [qwen-vl-text] coord item[24]: text=V1, bbox=[367, 277, 383, 295]
2026-08-10 15:58:17,336 INFO     29 [qwen-vl-text] coord item[25]: text=V3R, bbox=[650, 277, 676, 294]
2026-08-10 15:58:17,336 INFO     29 [qwen-vl-text] coord item[26]: text=II, bbox=[87, 372, 98, 389]
2026-08-10 15:58:17,336 INFO     29 [qwen-vl-text] coord item[27]: text=V2, bbox=[367, 372, 385, 390]
2026-08-10 15:58:17,336 INFO     29 [qwen-vl-text] coord item[28]: text=III, bbox=[86, 467, 98, 484]
2026-08-10 15:58:17,336 INFO     29 [qwen-vl-text] coord item[29]: text=V3, bbox=[367, 467, 385, 485]
2026-08-10 15:58:17,336 INFO     29 [qwen-vl-text] coord item[30]: text=V4R, bbox=[650, 467, 676, 485]
2026-08-10 15:58:17,336 INFO     29 [qwen-vl-text] coord item[31]: text=aVR, bbox=[85, 561, 109, 578]
2026-08-10 15:58:17,336 INFO     29 [qwen-vl-text] coord item[32]: text=V4, bbox=[367, 561, 385, 579]
2026-08-10 15:58:17,336 INFO     29 [qwen-vl-text] coord item[33]: text=aVL, bbox=[85, 656, 108, 673]
2026-08-10 15:58:17,336 INFO     29 [qwen-vl-text] coord item[34]: text=V5, bbox=[367, 656, 385, 674]
2026-08-10 15:58:17,336 INFO     29 [qwen-vl-text] coord item[35]: text=V5R, bbox=[650, 656, 676, 674]
2026-08-10 15:58:17,336 INFO     29 [qwen-vl-text] coord item[36]: text=aVF, bbox=[85, 750, 108, 768]
2026-08-10 15:58:17,336 INFO     29 [qwen-vl-text] coord item[37]: text=V6, bbox=[367, 750, 385, 768]
2026-08-10 15:58:17,336 INFO     29 [qwen-vl-text] coord item[38]: text=II, bbox=[86, 845, 98, 862]
2026-08-10 15:58:17,336 INFO     29 [qwen-vl-text] coord item[39]: text=检查时间: 2026/3/23 8:43:55, bbox=[58, 945, 238, 965]
2026-08-10 15:58:17,337 INFO     29 [qwen-vl-text] coord item[40]: text=报告时间: 2026/3/23 8:59:30, bbox=[297, 944, 486, 964]
2026-08-10 15:58:17,337 INFO     29 [qwen-vl-text] coord item[41]: text=报告医生:, bbox=[563, 943, 620, 963]
2026-08-10 15:58:17,337 INFO     29 [qwen-vl-text] coord item[42]: text=审核医生:, bbox=[751, 944, 809, 964]
2026-08-10 15:58:17,341 INFO     29 [qwen-vl-text] page=8 — 43/43 coords, api_time=19.2s
2026-08-10 15:58:17,342 INFO     29 [qwen-vl-text] new_positions (43):
[[8, 848.9440000000001, 1391.5680000000002, 39.168, 84.86399999999999], [8, 126.90400000000001, 227.55200000000002, 138.72, 171.35999999999999], [8, 455.10400000000004, 555.7520000000001, 137.088, 169.72799999999998], [8, 892.7040000000001, 1122.4440000000002, 133.82399999999998, 166.464], [8, 1452.832, 1691.324, 114.24, 150.14399999999998], [8, 126.90400000000001, 315.072, 190.944, 223.58399999999997], [8, 455.10400000000004, 621.392, 187.67999999999998, 220.32], [8, 892.7040000000001, 1122.4440000000002, 174.624, 207.26399999999998], [8, 1273.4160000000002, 1411.2600000000002, 174.624, 205.63199999999998], [8, 1546.9160000000002, 1662.88, 148.512, 179.51999999999998], [8, 126.90400000000001, 297.56800000000004, 244.79999999999998, 277.44], [8, 455.10400000000004, 647.648, 241.53599999999997, 274.176], [8, 892.7040000000001, 1122.4440000000002, 215.42399999999998, 246.432], [8, 1273.4160000000002, 1398.132, 218.688, 248.064], [8, 126.90400000000001, 665.152, 295.392, 328.032], [8, 737.3560000000001, 857.696, 295.392, 326.4], [8, 892.7040000000001, 1179.332, 252.95999999999998, 285.59999999999997], [8, 1273.4160000000002, 1411.2600000000002, 256.224, 285.59999999999997], [8, 255.996, 352.26800000000003, 319.87199999999996, 350.88], [8, 899.268, 1087.4360000000001, 297.024, 329.664], [8, 1273.4160000000002, 1398.132, 298.656, 328.032], [8, 188.168, 444.16400000000004, 383.52, 412.89599999999996], [8, 1802.912, 2056.7200000000003, 381.888, 412.89599999999996], [8, 190.35600000000002, 212.23600000000002, 453.69599999999997, 481.43999999999994], [8, 802.9960000000001, 838.004, 452.06399999999996, 481.43999999999994], [8, 1422.2, 1479.0880000000002, 452.06399999999996, 479.808], [8, 190.35600000000002, 214.424, 607.1039999999999, 634.848], [8, 802.9960000000001, 842.3800000000001, 607.1039999999999, 636.4799999999999], [8, 188.168, 214.424, 762.144, 789.8879999999999], [8, 802.9960000000001, 842.3800000000001, 762.144, 791.52], [8, 1422.2, 1479.0880000000002, 762.144, 791.52], [8, 185.98000000000002, 238.49200000000002, 915.5519999999999, 943.2959999999999], [8, 802.9960000000001, 842.3800000000001, 915.5519999999999, 944.9279999999999], [8, 185.98000000000002, 236.30400000000003, 1070.5919999999999, 1098.336], [8, 802.9960000000001, 842.3800000000001, 1070.5919999999999, 1099.9679999999998], [8, 1422.2, 1479.0880000000002, 1070.5919999999999, 1099.9679999999998], [8, 185.98000000000002, 236.30400000000003, 1224.0, 1253.376], [8, 802.9960000000001, 842.3800000000001, 1224.0, 1253.376], [8, 188.168, 214.424, 1379.04, 1406.7839999999999], [8, 126.90400000000001, 520.744, 1542.24, 1574.8799999999999], [8, 649.836, 1063.3680000000002, 1540.608, 1573.2479999999998], [8, 1231.844, 1356.5600000000002, 1538.9759999999999, 1571.616], [8, 1643.188, 1770.092, 1540.608, 1573.2479999999998]]
2026-08-10 15:58:17,342 INFO     29 [qwen-vl-text] ═══ DONE ═══ 43 positions, pages=1, time=25.4s
2026-08-10 15:58:17,370 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 15:58:17,371 INFO     29 [Trace] task=3880a51e | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | Extractor:ExaminationReport | outputs={"chunks": "5 items, types={'ExaminationReport': 5}", "html": "", "json": "302 items", "markdown": "", "text": "", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 5, \"chunks_LabExam\": 3}"}
2026-08-10 15:58:17,371 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 15:58:17,380 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:58:17,381 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 15:58:18,632 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:58:18,647 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 15:58:18,647 INFO     29 [Trace] task=3880a51e | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "302 items", "markdown": "", "text": "", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 5, \"chunks_LabExam\": 3}"}
2026-08-10 15:58:18,648 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 15:58:18,650 INFO     29 [ChunkMerger] Merged 9 chunks from 9 sources: {'Extractor:LabExam': 3, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 5, 'Extractor:Progress': 1} (filtered 6 noise chunks)
2026-08-10 15:58:18,667 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 15:58:18,667 INFO     29 [Trace] task=3880a51e | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "9 items, types={'LabReport': 3, 'DischargeRecord': 1, 'ExaminationReport': 5}", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf"}
2026-08-10 15:58:18,667 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 15:58:18,781 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786377035299, 'update_date': datetime.datetime(2026, 8, 10, 15, 50, 35), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1189781, 'status': '1'}
2026-08-10 15:58:19,004 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   癌胚抗原  CEA  5.03  ng/mL  0—5.2  False    非小细胞肺癌相关抗原  CYFRA21-1  4.60  ng/ml  0—3.3  True    神经元特异性烯醇化酶测定  NSE  10.60  ng/mL  0—16.3  False   
---
   谷丙转氨酶  ALT  52  U/L  7—40  True    谷草转氨酶  AST  54  U/L  13—35  True    总蛋白  TP  69.8  g/L  65—85  False    白蛋白  ALB  48.5  g/L  40—55  False    球蛋白  GLOB  21.3  g/L  20—40  False    白球比  A/G  2.3  None  1.2—2.4  False    总胆红素  TBIL  13.6  umol/L  1.7—21  False    直接胆红素  DBIL  1.7  umol/L  0—6.8  False    间接胆红素  IBIL  11.9  umol/L  3—13.6  False    碱性磷酸酶  ALP  67  U/L  50—135  False    谷氨酰转肽酶  GGT  19  U/L  7—45  False    尿素  UREA  4.15  mmol/L  2.76—8.07  False    肌酐  CREA  94  umol/L  45—84  True    尿酸  UA  192  umol/L  143—339  False    二氧化碳  CO2  25.9  mmol/L  22—29  False    葡萄糖  GLU  6.25  mmol/L  3.8—6.1  True    乳酸脱氢酶  LDH  291  U/L  135—214  True    肌酸激酶  CK  396  U/L  26—192  True    肌酸酶同功酶  CK-MB  17.70  U/L  7—25  False    肌红蛋白  MYO  77.4  ug/L  0—70  True    钾  K  3.74  mmol/L  3.5—5.3  False    钠  NA  132  mmol/L  137—147  True    氯  CL  96.0  mmol/L  99—110  True    钙  CA  2.12  mmol/L  2.02—2.6  False    C反应蛋白  CRP  0.41  mg/L  0—5  False    估算肾小球滤  eGFR  55.02  ml/min  None  False   
---
   白细胞  WBC  3.62  10^9/L  3.5---9.5  False    中性粒细胞百分比  NEUT  68.80  %  40---75  False    淋巴细胞百分比  LYMP  23.20  %  20---50  False    单核细胞百分比  MONO  4.10  %  3---10  False    嗜酸性粒细胞百分比  EOS%  2.5  %  0.4---8  False    嗜碱性粒细胞百分比  BASO  1.40  %  0---1  True    中性粒细胞计数  NEUT  2.49  10^9/L  1.8---6.3  False    淋巴细胞计数  LYMP  0.84  10^9/L  1.1---3.2  True    单核细胞计数  MONO  0.15  10^9/L  0.1---0.6  False    嗜酸性粒细胞计数  EOS#  0.09  10^9/L  0.02---0.52  False    嗜碱性粒细胞计数  BASO  0.05  10^9/L  0---0.06  False    红细胞  RBC  4.06  10^12/L  3.8---5.1  False    血红蛋白  HGB  125  g/L  115---150  False    红细胞压积  HCT  36.30  %  35---45  False    红细胞平均体积  MCV  89.4  fL  82---100  False    平均血红蛋白量  MCH  30.8  pg  27---34  False    平均血红蛋白浓度  MCHC  344  g/L  316---354  False    红细胞分布宽度标准  RDW-  43  fL  35---56  False    红细胞分布宽度变异  RDW-  13  %  11---16  False    血小板  PLT  155  10^9/L  125---350  False    血小板分布宽度  PDW  10.20  fL  9.2---15.6  False    平均血小板体积  MPV  9.90  fL  6.5---12  False    血小板压积  PCT  0.150  %  0.108---0.282  False    大型血小板比率  P-LC  24.00  %  11---45  False    大血小板数目  PLCC  37.20  10^9/L  30---90  False   
---
2025.1 确诊小细胞癌，已行免疫组化协诊
2025-.2-4给予”EP”化疗联合”特瑞普利单抗”免疫治疗3周期，
2025-04-22给予”EP”方案化疗联合
“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗
2025.5-8行“特瑞普利单抗”免疫治疗4周期
2025.8 PD
2025.8-2026.2“替雷利珠单抗联合安罗替尼”免疫治疗
信阳市中心医院
日间化疗出入院记录
姓名：
性别：女年龄：65岁
科别：日间化疗中心[东院床号：04
区]
登记号：0000
住院号：25
入院时间：2026年03月23日 08:29:00出院时间：2026年03月23日 11:14:00
住院天数：1天
主诉：确诊肺癌1年余
入院情况：1年余前因“胸闷”就诊我院，2025-01-17CT增强64：1.右肺门占位，考虑恶性病变并
右肺中下叶不张，右下肺动受侵可能。2.双肺纤维索条灶。双肺多发小结节，转移待排。3.右侧
胸腔少量积液。4.双肾小囊肿。5.升结肠多发憩室。6.子宫后壁肌瘤可能。7.冠状动脉CTA未见明
显异常。2025-01-23行纤支镜下肺活检，2025-01-23活体组织病理申请 诊断意见：(右中间段支
气管)考虑小细胞癌，已行免疫组化协诊。2025-01-26免疫组化申请：CK广谱（点+），CD56（+），
Syn（+），INSM1（+），CK5/6（-），P40（-），TTF1（+），NapsinA（-），Ki-67（80%+）。结合HE
及免疫组化结果，（右中间段支气管）肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04
-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期，2025-04-22给予“EP”方案化疗联合
“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗。2025-05-19、2025
-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加增强
(胸部.上腹部.下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节。
胸腔少量积液。4.双肾小囊肿。5.升结肠多发息室。6.丁台加壁肌瘤可能。冠状动脉CT示无明显异常。2025-01-23行纤支镜下肺活检，2025-01-23活体组织病理申请 诊断意见：(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。2025-01-26免疫组化申请：CK广谱(点+)，CD56(+)，Syn(+)，INSM1(+)，CK5/6(-)，P40(-)，TTF1(+)，NapsinA(-)，Ki-67(80%)。结合HE及免疫组化结果，(右中间段支气管)肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期，2025-04-22给予“EP”方案化疗联合“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗。2025-05-19、2025-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加强(胸部，上腹部，下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节，转移瘤可能；建议追踪复查。2.双肺慢性炎症，右肺中叶局限性支扩，双侧胸腔少量积液。3.脾脏低密度灶，建议追踪复查。4.胆囊可疑小结石。升结肠多发憩室。5.双肾小囊肿。与2025-05-18日片比较：右肺中叶局限性支扩，右肺下叶内基底段结节较前增大，右肺门淋巴结较前增大。考虑病情进展，于2025-08-23给予“安罗替尼12mg”联合“替雷利珠单抗”抗肿瘤治疗1周期。后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-22、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重无明显变化。诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利，予办理出院手续。
国家医保编码：D411502011804 - Internet Explorer
美系统) 修改患者信息 诊疗与病历 申请单 手术管理 医嘱单 会诊管理 重症管理 需关注医嘱 病情总览 质量管理 更多
汤光冉 住院医师
日间化疗中心[东院区]
0000 床号: 04 住院天数: 1 费别: 全国医保居民 余额: 0.00 诊断: 肺恶性肿瘤,恶性肿瘤... 医疗救助类型: 农村低保
病人列表 全息视图
(1) ×
操作 编辑 功能 表格 其他
历
保存 打印 自动续打 预览 单独打印 手工解锁 隐藏留痕 病历参考 更新数据 首页
记录
1:09:45 曾庆星
医师审核
录单
1:10:52 曾庆星
医师审核
录单
1:11:53 曾庆星
医师审核
11:12:02 曾庆星
医师审核
单(日间...
11:13:02 曾庆星
医师审核
已打印
11:15:03 曾庆星
医师审核
评估表
16:30:58 曾庆星
院医师审核
/TE风险评...
16:32:44 曾庆星
院医师审核
后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-2
2、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我
院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重
无明显变化。
诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利
，予办理出院手续。
出院情况：患者未诉不适，神志清，精神可，生命体征平稳。
出院诊断：
1.恶性肿瘤免疫治疗
2.肺恶性肿瘤小细胞肺癌IV期
3.肺继发恶性肿瘤
4.冠状动脉粥样硬化性心脏病
5.胸腔积液
6.心包积液
7.肺部感染
8.腔隙性脑梗死
9.肾功能检查的异常结果
1
100%
---
信阳市中心医院
免疫病理诊断报告
免疫组化号：MT25-
姓名：
性别：女
年龄：64岁
送检医院：
病区：肿瘤内科五护理单元[东病理号：D25-01313
就诊卡号：
住院号：2
病区床号：21
送检标本：肺手术标本
送检时间：2025-01-24
临床诊断：
光镜所见：
免疫病理诊断：
CK广谱（点+），CD56（+），Syn（+），INSM1（+），CK5/6（-），P40（-），TTF1（+），
NapsinA（-），Ki-67（80%+）。
结合HE及免疫组化结果，（右中间段支气管）肺小细胞神经内分泌癌。
初诊医师：刘磊
复诊医师：刘磊
报告日期：2025-01-26 10:49
备注：1.本报告单仅供临床参考 2.如临床对报告内容有疑问请与报告医生联系。联系电话：0376-6227723(西院区)，0376-6667570(东院区)。
3.此报告必须经过病理科医师签字有效。
---
信阳市中心医院
病理检查报告单
病理号：D25
姓名：
性别：女
年龄：64岁
送检医院：
送检科室：呼吸与危重症医学科送检日期：2025-01-22
门诊号：9
住院号：25
床号：21
送检医师：周鹏飞
送检标本：右中间段支气管
临床诊断：
巨检：灰白色碎组织最大径0.3厘米。全取
病理诊断：
(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。
初诊医师：刘晶晶
复诊医师：刘磊
报告日期：2025-01-23 19:26
备注：1.本报告单仅供临床参考 2.如临床对报告内容有疑问请与报告医生联系。联系电话：0376-6227723(西院区)；0376-6667570(东院区)。
3.此报告必须经过病理科医师签字有效。
---
信阳市中心医院
影像科CT诊断报告书
扫描
获取电子胶
片和报告(试用)
影像号: 000
报告日期: 2025-12-22 16:36
姓名:
性别: 女
年龄: 64岁
检查日期: 2025-12-22
科别: 日间化疗中心[东院区]院号: 2
门诊号:/
检查时间: 09:53:10
检查方法: 胸部CT平扫,胸部CT增强,上腹部CT平扫,上腹部CT增强,下腹部CT平扫,下腹部CT增强
技术参数:
影像学所见:
双侧胸廓对称,右肺门增大,可见不规则状软组织密度影,密度不均,边
界不清,强化不均,右肺中下叶支气管稍变窄,双肺可见条索状及结节状高密
度影,较大病灶位于右肺下叶内基底段见实性结节,大小约为15.8×15.4mm,
轻度强化。右肺中叶局限性支扩。气管、支气管通畅,右肺门见明显肿大淋巴
结,轻度强化,双侧胸膜腔及心包腔可见积液征象。与2025-8-21日片比较:
双侧胸腔积液增多,心包积液新增,右肺门软组织密度影及淋巴结增大。
肝脏未见明显异常密度及异常强化征象,胆囊内隐约见斑点状高密度影,
脾脏见数个小灶状低强化影。胰腺形态、大小、密度正常。双肾见小圆形低密
度影,边界清,增强未见明显强化。腹膜后未见明显增大淋巴结,腹腔未见明
显积液征象。升结肠见多发小囊袋状外凸影。与2025-8-21日片比较:大致相
仿。
影像学意见:
1. 右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节,转移瘤可能;建
议追踪复查:右肺门肿大淋巴结。
2. 双肺慢性炎症,右肺中叶局限性支扩,双侧胸腔积液,心包积液。
3. 脾脏低密度灶,建议追踪复查。
4. 胆囊可疑小结石。升结肠多发憩室。
5. 双肾小囊肿。
报告医师:
审核医师:
此报告仅供临床医师参考,签字生效
打印时间: 2025-12-22 16:36:26
---
信阳市中心医院
影像科CT诊断报告书
扫描此二维码可
电子胶
片和报告(试用)
影像号:0000
报告日期:2026-02-25 15:36
姓名:
性别:女
年龄:65岁
检查日期:2026-02-25
科别:肿瘤内科五门诊[东院住院号:/
门诊号:1
6
检查时间:08:57:41
检查方法:胸部CT平扫加薄层
技术参数:
影像学所见:
双侧胸廓对称,右肺门增大,可见不规则状软组织密度影,密度不均,边
界不清,右肺中下叶支气管稍变窄,双肺可见条索状及结节状高密度影。右肺
中叶局限性支扩。气管、支气管通畅,右肺门见明显肿大淋巴结,右侧胸膜局
部稍厚,双侧胸膜腔及心包腔可见积液征象。与2025-12-22日片比较:右侧胸
腔积液增多,右肺门软组织密度影及淋巴结进一步增大,右肺结节增大,右侧
胸膜局部稍增厚。
影像学意见:
1.右肺癌并右肺中下叶不张治疗状态。双肺多发结节,转移瘤可能;右肺门
肿大淋巴结转移。
2.双肺慢性炎症,双侧胸腔积液,心包积液。
3.右侧胸膜局部稍厚,不除外转移。
报告医师:
肖健
审核医师:
贺玲
此报告仅供临床医师参考,签字生效
打印时间:2026-02-25 15:36:58
---
信阳市中心医院心电图报告单
门诊号:
姓名:
P波宽度: 141ms
诊断: 1.窦性心律
住院号: 0000
性别: 女
P-R间期: 181ms
【120-200】
2.低电压
床位号: 04
年龄: 65岁
QRS时限: 101ms
【60-110】
科室: 日间化疗中心[心率: 77bpm
【60-100】
QT/QTc: 358/406ms
【360-440】
东院区]
电轴: 60°
【-30-90】
2026-03-23 08:43:55
25mm/s 10mm/mV
I
V1
V3R
II
V2
III
V3
V4R
aVR
V4
aVL
V5
V5R
aVF
V6
II
检查时间: 2026/3/23 8:43:55
报告时间: 2026/3/23 8:59:30
报告医生:
审核医生:
2026-08-10 15:58:19,620 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 15:58:19,621 INFO     29 [Trace] task=3880a51e | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "9 items, types={'LabReport': 3, 'DischargeRecord': 1, 'ExaminationReport': 5}", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf", "embedding_token_consumption": 5653}
2026-08-10 15:58:19,621 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 15:58:19,819 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 15:58:19,819 INFO     29 [Trace] task=3880a51e | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":9,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 15:58:19,823 INFO     29 [DIAG-EXECUTOR] row_position_int len=3 row[0]=(10, 712, 848, 511, 546) row[-1]=(10, 712, 1111, 604, 639)
2026-08-10 15:58:19,823 INFO     29 [DIAG-EXECUTOR] row_position_int len=26 row[0]=(11, 426, 576, 297, 328) row[-1]=(11, 1156, 1334, 626, 655)
2026-08-10 15:58:19,823 INFO     29 [DIAG-EXECUTOR] row_position_int len=25 row[0]=(12, 174, 251, 278, 302) row[-1]=(12, 899, 1056, 627, 651)
2026-08-10 15:58:19,823 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:58:19,823 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:58:19,824 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:58:19,824 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:58:19,824 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:58:19,824 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:58:19,829 INFO     29 set_progress(3880a51e94d311f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 15:58:19 [DOC Engine]:
Start to index...
2026-08-10 15:58:19,866 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.030s]
2026-08-10 15:58:19,871 INFO     29 set_progress(3880a51e94d311f1bd9827cf206dfa2d), progress: 0.8111111111111111, progress_msg: 
2026-08-10 15:58:19,899 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.020s]
2026-08-10 15:58:19,918 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.013s]
2026-08-10 15:58:19,930 INFO     29 set_progress(3880a51e94d311f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 15:58:19 Indexing done (0.10s). Task done (440.08s)
2026-08-10 15:58:19,934 INFO     29 [Done], chunks(9), token(5653), elapsed:440.08
2026-08-10 15:58:20,068 INFO     29 handle_task done for task {"id": "3880a51e94d311f1bd9827cf206dfa2d", "doc_id": "37728ffc94d311f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909800, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786377033220, "task_type": "dataflow", "root_trace_id": "4dc9fd8a1d244ef89de3e82f6546943d", "root_traceparent": "00-4dc9fd8a1d244ef89de3e82f6546943d-90143aef6fb19019-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
