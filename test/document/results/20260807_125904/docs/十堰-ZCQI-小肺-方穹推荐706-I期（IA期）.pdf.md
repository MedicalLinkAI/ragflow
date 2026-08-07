# 基准结果：十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf

## 基本信息

- 文件：`十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf`
- 大小：10654.1 KB
- PDF 总页数：12
- doc_id：`688aee0a918011f18dbe1f8f96f1c395`
- 上传方式：skip
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-07T12:59:07  完成时间：2026-08-07T12:59:08  耗时：1.5s
- progress_msg：`10:30:25 Indexing done (0.34s). Task done (574.05s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 01bfddf6 | 4 | 1-4 | 2025.1 确诊小细胞癌，已行免疫组化协诊 2025-.2-4给予" EP"  |
| 2 | e8bad4cd | 1 | 5-5 | 信阳市中心医院 免疫病理诊断报告 免疫组化号：MT25- 姓名： 性别：女 年龄 |
| 3 | 92f8d872 | 1 | 6-6 | 信阳市中心医院 病理检查报告单 病理号：D25 姓名： 性别：女 年龄：64岁  |
| 4 | b0922a74 | 1 | 7-7 | 信阳市中心医院 影像科CT诊断报告书 扫描 获取电子胶 片和报告(试用) 影像号 |
| 5 | 2ad33362 | 1 | 8-8 | 信阳市中心医院 影像科CT诊断报告书 扫描此二维码可 以电子胶 片和报告(试用) |
| 6 | 257a936c | 1 | 9-9 | 信阳市中心医院心电图报告单 门诊号: 姓名: P波宽度: 141ms 诊断: 1 |
| 7 | 397b561b | 1 | 10-10 | <table><tr><td>癌胚抗原</td><td>CEA</td><td> |
| 8 | 39cb18dd | 1 | 11-11 | <table><tr><td>谷丙转氨酶</td><td>ALT</td><td |
| 9 | cc08101e | 1 | 12-12 | <table><tr><td>白细胞</td><td>WBC</td><td>3 |

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
| AdmissionRecord | 入院 | 1 | 1 | 1 | encounter_date, dm_admission_time, cc_text, department | **OK** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 5 | 5 | 5 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 3 | 0 | 3 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"AdmissionRecord": 1, "ExaminationReport": 5, "LabReport": 3}`
- ChunkMerger：`{"found": true, "merged": 9, "sources": 8, "stats": {"Extractor:LabExam": 3, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 5}, "filtered_noise": 5}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-06 10:30:14,973 INFO     30 [ChunkMerger] Merged 9 chunks from 8 sources: {'Extractor:LabExam': 3, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-06 10:20:19,000 INFO     30 handle_task begin for task {"id": "6a97f83c918011f18dbe1f8f96f1c395", "doc_id": "688aee0a918011f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909798, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011615561, "task_type": "dataflow", "root_trace_id": "d05a3d8d0d6c4aa38394753a3ea0008c", "root_traceparent": "00-d05a3d8d0d6c4aa38394753a3ea0008c-2c380740bfb060e1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-06 10:20:20,044 INFO     30 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.002s]
2026-08-06 10:20:22,588 INFO     30 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-06 10:20:23,572 INFO     30 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-06 10:20:23,572 INFO     30 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-06 10:20:23,643 INFO     30 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-06 10:20:23,643 INFO     30 ============================================================
2026-08-06 10:20:23,643 INFO     30 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-06 10:20:23,643 INFO     30    model_dir : /ragflow/rag/res/deepdoc
2026-08-06 10:20:23,643 INFO     30 ============================================================
2026-08-06 10:20:25,844 INFO     30 load_model /ragflow/rag/res/deepdoc/layout.onnx uses CPU
2026-08-06 10:20:26,244 INFO     30 load_model /ragflow/rag/res/deepdoc/tsr.onnx uses CPU
2026-08-06 10:20:26,260 INFO     30 No torch found.
2026-08-06 10:20:26,321 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:20:26.318+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"6a97f83c918011f18dbe1f8f96f1c395": {"id": "6a97f83c918011f18dbe1f8f96f1c395", "doc_id": "688aee0a918011f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909798, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011615561, "task_type": "dataflow", "root_trace_id": "d05a3d8d0d6c4aa38394753a3ea0008c", "root_traceparent": "00-d05a3d8d0d6c4aa38394753a3ea0008c-2c380740bfb060e1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:20:34,107 INFO     30 [qwen-vl-parser] parse_pdf start, total_pages=12
2026-08-06 10:20:35,052 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=549369, prompt_len=764
2026-08-06 10:20:46,292 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:20:46,292 INFO     30 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-06 10:20:46,308 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=549369, prompt_len=401
2026-08-06 10:20:48,308 INFO     30 [qwen-vl-parser] text API response (len=231):
["2025.1 确诊小细胞癌，已行免疫组化协诊", "2025-.2-4给予\" EP\" 化疗联合\" 特瑞普利单抗\" 免疫治疗3周期，", "2025-04-22给予\" EP\" 方案化疗联合", "\" 替雷利珠单抗\" 免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗", "2025.5-8 行\" 特瑞普利单抗\" 免疫治疗4周期", "2025.8 PD", "2025.8-2026.2 \" 替雷利珠单抗联合安罗替尼\" 免疫治疗"]
2026-08-06 10:20:48,311 INFO     30 [qwen-vl-parser] page=1 text: 7 lines (bbox 0-6)
2026-08-06 10:20:48,311 INFO     30 [qwen-vl-parser] page=1 text: 7 sections
2026-08-06 10:20:51,031 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7962152, prompt_len=764
2026-08-06 10:20:58,729 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:20:58,735 INFO     30 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-06 10:20:58,819 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7962152, prompt_len=401
2026-08-06 10:20:59,669 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:20:59.667+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"6a97f83c918011f18dbe1f8f96f1c395": {"id": "6a97f83c918011f18dbe1f8f96f1c395", "doc_id": "688aee0a918011f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909798, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011615561, "task_type": "dataflow", "root_trace_id": "d05a3d8d0d6c4aa38394753a3ea0008c", "root_traceparent": "00-d05a3d8d0d6c4aa38394753a3ea0008c-2c380740bfb060e1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:21:06,562 INFO     30 [qwen-vl-parser] text API response (len=1096):
["1804 - Internet Explorer", "诊疗与病历 申请单 手术管理 医嘱单 会诊管理 重症管理 需关注医嘱 病情总览 质量管理 更多", "汤光冉 住院医师", "日间化疗中心[东院区]", "住院天数: 1 费别: 全国医保居民 余额: 0.00 诊断: 肺恶性肿瘤,恶性肿瘤... 医疗救助类型: 农村低保", "病人列表 全息视图", "操作 编辑 功能 表格 其他", "保存 打印 自动续打 预览 单独打印 手工解锁 隐藏留痕 病历参考 更新数据 首页", "信阳市中心医院", "日间化疗出入院记录", "姓名: 性别:女年龄:65岁 科别:日间化疗中心[东院床号:04 登记号:0000 住院号:25", "区]", "入院时间: 2026年03月23日 08:29:00出院时间: 2026年03月23日 11:14:00 住院天数: 1天", "主诉: 确诊肺癌1年余", "入院情况: 1年余前因“胸闷”就诊我院, 2025-01-17CT增强64: 1.右肺门占位, 考虑恶性病变并", "右肺中下叶不张, 右下肺动受侵可能。2. 双肺纤维索条灶。双肺多发小结节, 转移待排。3.右侧", "胸腔少量积液。4.双肾小囊肿。5.升结肠多发憩室。6.子宫后壁肌瘤可能。7.冠状动脉CTA未见明", "显异常。2025-01-23行纤支镜下肺活检, 2025-01-23 活体组织病理申请 诊断意见: (右中间段支", "气管)考虑小细胞癌, 已行免疫组化协诊。2025-01-26 免疫组化申请: CK广谱 (点+), CD56 (+),", "Syn (+), INSM1 (+), CK5/6 (-), P40 (-), TTF1 (+), NapsinA (-), Ki-67 (80%+)。结合HE", "及免疫组化结果, (右中间段支气管)肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04", "-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期, 2025-04-22给予“EP”方案化疗联合", "“替雷利珠单抗”免疫治疗1周期, 化疗后呕吐反应较重, 予以对症支持治疗。2025-05-19、2025", "-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加增强", "(胸部,上腹部,下腹部) 诊断意见: 1. 右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节。", "100%", "16:56", "2026/3/23"]
2026-08-06 10:21:06,565 INFO     30 [qwen-vl-parser] page=2 text: 28 lines (bbox 7-34)
2026-08-06 10:21:06,565 INFO     30 [qwen-vl-parser] page=2 text: 28 sections
2026-08-06 10:21:08,366 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5188086, prompt_len=764
2026-08-06 10:21:18,991 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:21:18,993 INFO     30 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-06 10:21:19,043 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5188086, prompt_len=401
2026-08-06 10:21:25,446 INFO     30 [qwen-vl-parser] text API response (len=893):
["胸腔少量积液。4.双肾小囊肿。5.升结肠多发息室。6.丁台加壁肌瘤可能。冠状动脉CT示无明显异常。2025-01-23行纤支镜下肺活检，2025-01-23活体组织病理申请 诊断意见：(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。2025-01-26免疫组化申请：CK广谱(点+)，CD56(+)，Syn(+)，INSM1(+)，CK5/6(-)，P40(-)，TTF1(+),NapsinA(-)，Ki-67(80%+)。结合HE及免疫组化结果，(右中间段支气管)肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期，2025-04-22给予“EP”方案化疗联合“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗。2025-05-19、2025-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加强(胸部，上腹部，下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节，转移瘤可能；建议追踪复查。2.双肺慢性炎症，右肺中叶局限性支扩，双侧胸腔少量积液。3.脾脏低密度灶，建议追踪复查。4.胆囊可疑小结石。升结肠多发憩室。5.双肾小囊肿。与2025-05-18日片比较：右肺中叶局限性支扩，右肺下叶内基底段结节较前增大，右肺门淋巴结较前增大。考虑病情进展，于2025-08-23给予“安罗替尼12mg”联合“替雷利珠单抗”抗肿瘤治疗1周期。后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-22、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重无明显变化。诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利，予办理出院手续。"]
2026-08-06 10:21:25,448 INFO     30 [qwen-vl-parser] page=3 text: 1 lines (bbox 35-35)
2026-08-06 10:21:25,449 INFO     30 [qwen-vl-parser] page=3 text: 1 sections
2026-08-06 10:21:27,545 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4627238, prompt_len=764
2026-08-06 10:21:32,891 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:21:32.889+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"6a97f83c918011f18dbe1f8f96f1c395": {"id": "6a97f83c918011f18dbe1f8f96f1c395", "doc_id": "688aee0a918011f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909798, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011615561, "task_type": "dataflow", "root_trace_id": "d05a3d8d0d6c4aa38394753a3ea0008c", "root_traceparent": "00-d05a3d8d0d6c4aa38394753a3ea0008c-2c380740bfb060e1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:21:36,518 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:21:36,523 INFO     30 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-06 10:21:36,600 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4627238, prompt_len=401
2026-08-06 10:21:47,673 INFO     30 [qwen-vl-parser] text API response (len=990):
["国家医保编码：D411502011804 - Internet Explorer", "美系统) 修改患者信息 诊疗与病历 申请单 手术管理 医嘱单 会诊管理 重症管理 需关注医嘱 病情总览 质量管理 更多", "汤光冉 住院医师", "日间化疗中心[东院区]", "0000 床号: 04 住院天数: 1 费别: 全国医保居民 余额: 0.00 诊断: 肺恶性肿瘤,恶性肿瘤... 医疗救助类型: 农村低保", "病人列表 全息视图", "(1) ×", "操作 编辑 功能 表格 其他", "历", "保存 打印 自动续打 预览 单独打印 手工解锁 隐藏留痕 病历参考 更新数据 首页", "记录", "1:09:45 曾庆星", "医师审核", "录单", "1:10:52 曾庆星", "医师审核", "录单", "1:11:53 曾庆星", "医师审核", "11:12:02 曾庆星", "医师审核", "单(日间...", "11:13:02 曾庆星", "医师审核", "已打印", "11:15:03 曾庆星", "医师审核", "评估表", "16:30:58 曾庆星", "院医师审核", "/TE风险评...", "16:32:44 曾庆星", "院医师审核", "后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-2", "2、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我", "院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重", "无明显变化。", "诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利", "，予办理出院手续。", "出院情况：患者未诉不适，神志清，精神可，生命体征平稳。", "出院诊断：", "1.恶性肿瘤免疫治疗", "2.肺恶性肿瘤小细胞肺癌IV期", "3.肺继发恶性肿瘤", "4.冠状动脉粥样硬化性心脏病", "5.胸腔积液", "6.心包积液", "7.肺部感染", "8.腔隙性脑梗死", "9.肾功能检查的异常结果", "1", "100%", "16:57", "2026/3/23"]
2026-08-06 10:21:47,678 INFO     30 [qwen-vl-parser] page=4 text: 54 lines (bbox 36-89)
2026-08-06 10:21:47,678 INFO     30 [qwen-vl-parser] page=4 text: 54 sections
2026-08-06 10:21:49,653 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4388375, prompt_len=764
2026-08-06 10:21:58,847 INFO     30 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2025-01-24"
}
```
2026-08-06 10:21:58,850 INFO     30 [qwen-vl-parser] page=5 classify=text report_date=2025-01-24
2026-08-06 10:21:58,906 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4388375, prompt_len=401
2026-08-06 10:22:03,641 INFO     30 [qwen-vl-parser] text API response (len=471):
["信阳市中心医院", "免疫病理诊断报告", "免疫组化号：MT25-", "姓名：", "性别：女", "年龄：64岁", "送检医院：", "病区：肿瘤内科五护理单元[东病理号：D25-01313", "就诊卡号：", "住院号：2", "病区床号：21", "送检标本：肺手术标本", "送检时间：2025-01-24", "临床诊断：", "光镜所见：", "免疫病理诊断：", "CK广谱（点+），CD56（+），Syn（+），INSM1（+），CK5/6（-），P40（-），TTF1（+），", "NapsinA（-），Ki-67（80%+）。", "结合HE及免疫组化结果，（右中间段支气管）肺小细胞神经内分泌癌。", "初诊医师：刘磊", "复诊医师：刘磊", "报告日期：2025-01-26 10:49", "备注：1.本报告单仅供临床参考 2.如临床对报告内容有疑问请与报告医生联系。联系电话：0376-6227723(西院区)，0376-6667570(东院区)。", "3.此报告必须经过病理科医师签字有效。"]
2026-08-06 10:22:03,644 INFO     30 [qwen-vl-parser] page=5 text: 24 lines (bbox 90-113)
2026-08-06 10:22:03,644 INFO     30 [qwen-vl-parser] page=5 text: 24 sections
2026-08-06 10:22:05,438 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4556779, prompt_len=764
2026-08-06 10:22:06,207 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:22:06.205+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"6a97f83c918011f18dbe1f8f96f1c395": {"id": "6a97f83c918011f18dbe1f8f96f1c395", "doc_id": "688aee0a918011f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909798, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011615561, "task_type": "dataflow", "root_trace_id": "d05a3d8d0d6c4aa38394753a3ea0008c", "root_traceparent": "00-d05a3d8d0d6c4aa38394753a3ea0008c-2c380740bfb060e1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:22:14,562 INFO     30 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-01-23"}
```
2026-08-06 10:22:14,566 INFO     30 [qwen-vl-parser] page=6 classify=text report_date=2025-01-23
2026-08-06 10:22:14,637 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4556779, prompt_len=401
2026-08-06 10:22:22,058 INFO     30 [qwen-vl-parser] text API response (len=381):
["信阳市中心医院", "病理检查报告单", "病理号：D25", "姓名：", "性别：女", "年龄：64岁", "送检医院：", "送检科室：呼吸与危重症医学科送检日期：2025-01-22", "门诊号：9", "住院号：25", "床号：21", "送检医师：周鹏飞", "送检标本：右中间段支气管", "临床诊断：", "巨检：灰白色碎组织最大径0.3厘米。全取", "病理诊断：", "(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。", "初诊医师：刘晶晶", "复诊医师：刘磊", "报告日期：2025-01-23 19:26", "备注：1.本报告单仅供临床参考 2.如临床对报告内容有疑问请与报告医生联系。联系电话：0376-6227723(西院区)；0376-6667570(东院区)。", "3.此报告必须经过病理科医师签字有效。"]
2026-08-06 10:22:22,062 INFO     30 [qwen-vl-parser] page=6 text: 22 lines (bbox 114-135)
2026-08-06 10:22:22,063 INFO     30 [qwen-vl-parser] page=6 text: 22 sections
2026-08-06 10:22:23,628 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3308277, prompt_len=764
2026-08-06 10:22:31,421 INFO     30 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2025-12-22"
}
```
2026-08-06 10:22:31,424 INFO     30 [qwen-vl-parser] page=7 classify=text report_date=2025-12-22
2026-08-06 10:22:31,490 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3308277, prompt_len=401
2026-08-06 10:22:38,382 INFO     30 [qwen-vl-parser] text API response (len=883):
["信阳市中心医院", "影像科CT诊断报告书", "扫描", "获取电子胶", "片和报告(试用)", "影像号: 000", "报告日期: 2025-12-22 16:36", "姓名:", "性别: 女", "年龄: 64岁", "检查日期: 2025-12-22", "科别: 日间化疗中心[东院区]院号: 2", "门诊号:/", "检查时间: 09:53:10", "检查方法: 胸部CT平扫,胸部CT增强,上腹部CT平扫,上腹部CT增强,下腹部CT平扫,下腹部CT增强", "技术参数:", "影像学所见:", "双侧胸廓对称,右肺门增大,可见不规则状软组织密度影,密度不均,边", "界不清,强化不均,右肺中下叶支气管稍变窄,双肺可见条索状及结节状高密", "度影,较大病灶位于右肺下叶内基底段见实性结节,大小约为15.8×15.4mm,", "轻度强化。右肺中叶局限性支扩。气管、支气管通畅,右肺门见明显肿大淋巴", "结,轻度强化,双侧胸膜腔及心包腔可见积液征象。与2025-8-21日片比较:", "双侧胸腔积液增多,心包积液新增,右肺门软组织密度影及淋巴结增大。", "肝脏未见明显异常密度及异常强化征象,胆囊内隐约见斑点状高密度影,", "脾脏见数个小灶状低强化影。胰腺形态、大小、密度正常。双肾见小圆形低密", "度影,边界清,增强未见明显强化。腹膜后未见明显增大淋巴结,腹腔未见明", "显积液征象。升结肠见多发小囊袋状外凸影。与2025-8-21日片比较:大致相", "仿。", "影像学意见:", "1. 右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节,转移瘤可能;建", "议追踪复查:右肺门肿大淋巴结。", "2. 双肺慢性炎症,右肺中叶局限性支扩,双侧胸腔积液,心包积液。", "3. 脾脏低密度灶,建议追踪复查。", "4. 胆囊可疑小结石。升结肠多发憩室。", "5. 双肾小囊肿。", "报告医师:", "审核医师:", "此报告仅供临床医师参考,签字生效", "打印时间: 2025-12-22 16:36:26"]
2026-08-06 10:22:38,383 INFO     30 [qwen-vl-parser] page=7 text: 39 lines (bbox 136-174)
2026-08-06 10:22:38,384 INFO     30 [qwen-vl-parser] page=7 text: 39 sections
2026-08-06 10:22:39,147 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:22:39.144+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"6a97f83c918011f18dbe1f8f96f1c395": {"id": "6a97f83c918011f18dbe1f8f96f1c395", "doc_id": "688aee0a918011f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909798, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011615561, "task_type": "dataflow", "root_trace_id": "d05a3d8d0d6c4aa38394753a3ea0008c", "root_traceparent": "00-d05a3d8d0d6c4aa38394753a3ea0008c-2c380740bfb060e1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:22:40,221 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4611687, prompt_len=764
2026-08-06 10:22:52,191 INFO     30 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-02-25"
}
```
2026-08-06 10:22:52,196 INFO     30 [qwen-vl-parser] page=8 classify=text report_date=2026-02-25
2026-08-06 10:22:52,303 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4611687, prompt_len=401
2026-08-06 10:22:58,405 INFO     30 [qwen-vl-parser] text API response (len=653):
["信阳市中心医院", "影像科CT诊断报告书", "扫描此二维码可", "以电子胶", "片和报告(试用)", "影像号: 0000", "报告日期: 2026-02-25 15:36", "姓名:", "性别: 女", "年龄: 65岁", "检查日期: 2026-02-25", "科别: 肿瘤内科五门诊[东院", "住院号: /", "门诊号: 1", "6", "检查时间: 08:57:41", "检查方法: 胸部CT平扫加薄层", "技术参数:", "影像学所见:", "双侧胸廓对称, 右肺门增大, 可见不规则状软组织密度影, 密度不均, 边", "界不清, 右肺中下叶支气管稍变窄, 双肺可见条索状及结节状高密度影。右肺", "中叶局限性支扩。气管、支气管通畅, 右肺门见明显肿大淋巴结, 右侧胸膜局", "部稍厚, 双侧胸膜腔及心包腔可见积液征象。与2025-12-22日片比较: 右侧胸", "腔积液增多, 右肺门软组织密度影及淋巴结进一步增大, 右肺结节增大, 右侧", "胸膜局部稍增厚。", "影像学意见:", "1. 右肺癌并右肺中下叶不张治疗状态。双肺多发结节, 转移瘤可能; 右肺门", "肿大淋巴结转移。", "2. 双肺慢性炎症, 双侧胸腔积液, 心包积液。", "3. 右侧胸膜局部稍厚, 不除外转移。", "报告医师:", "肖健", "审核医师:", "贺玲", "此报告仅供临床医师参考, 签字生效", "打印时间: 2026-02-25 15:36:58"]
2026-08-06 10:22:58,408 INFO     30 [qwen-vl-parser] page=8 text: 36 lines (bbox 175-210)
2026-08-06 10:22:58,409 INFO     30 [qwen-vl-parser] page=8 text: 36 sections
2026-08-06 10:23:00,895 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7005445, prompt_len=764
2026-08-06 10:23:11,136 INFO     30 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-03-23"
}
```
2026-08-06 10:23:11,139 INFO     30 [qwen-vl-parser] page=9 classify=text report_date=2026-03-23
2026-08-06 10:23:11,191 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7005445, prompt_len=401
2026-08-06 10:23:12,408 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:23:12.406+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"6a97f83c918011f18dbe1f8f96f1c395": {"id": "6a97f83c918011f18dbe1f8f96f1c395", "doc_id": "688aee0a918011f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909798, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011615561, "task_type": "dataflow", "root_trace_id": "d05a3d8d0d6c4aa38394753a3ea0008c", "root_traceparent": "00-d05a3d8d0d6c4aa38394753a3ea0008c-2c380740bfb060e1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:23:17,108 INFO     30 [qwen-vl-parser] text API response (len=491):
["信阳市中心医院心电图报告单", "门诊号:", "姓名:", "P波宽度: 141ms", "诊断: 1.窦性心律", "住院号: 0000", "性别: 女", "P-R间期: 181ms", "【120-200】", "2.低电压", "床位号: 04", "年龄: 65岁", "QRS时限: 101ms", "【60-110】", "科室: 日间化疗中心[心率: 77bpm", "【60-100】", "QT/QTc: 358/406ms", "【360-440】", "东院区]", "电轴: 60°", "【-30-90】", "2026-03-23 08:43:55", "25mm/s 10mm/mV", "I", "V1", "V3R", "II", "V2", "III", "V3", "V4R", "aVR", "V4", "aVL", "V5", "V5R", "aVF", "V6", "II", "检查时间: 2026/3/23 8:43:55", "报告时间: 2026/3/23 8:59:30", "报告医生:", "审核医生:", ""]
2026-08-06 10:23:17,110 INFO     30 [qwen-vl-parser] page=9 text: 43 lines (bbox 211-253)
2026-08-06 10:23:17,110 INFO     30 [qwen-vl-parser] page=9 text: 43 sections
2026-08-06 10:23:19,828 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5483158, prompt_len=764
2026-08-06 10:23:32,245 INFO     30 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-23"
}
```
2026-08-06 10:23:32,248 INFO     30 [qwen-vl-parser] page=10 classify=table report_date=2026-03-23
2026-08-06 10:23:32,346 INFO     30 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5483158, prompt_len=756
2026-08-06 10:23:36,306 INFO     30 [qwen-vl-parser] table API response (len=242):
\begin{tabular}{ccccccccc}
\hline
序号 & 项目代号 & 项目名称 & 结果 & 单位 & 参考值 \\
\hline
1 & CEA & 癌胚抗原 & 5.03 & ng/mL & 0—5.2 \\
2 & CYFRA21-1 & 非小细胞肺癌相关抗原 & 4.60 & ng/ml & 0—3.3 \\
3 & NSE & 神经元特异性烯醇化酶测定 & 10.60 & ng/mL & 0—16.3 \\
\hline
\end{tabular}
2026-08-06 10:23:36,317 INFO     30 [qwen-vl-parser] page=10 table: 10 LaTeX lines (bbox 254-263)
2026-08-06 10:23:36,317 INFO     30 [qwen-vl-parser] page=10 table: 10 sections
2026-08-06 10:23:38,340 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5228539, prompt_len=764
2026-08-06 10:23:45,425 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:23:45.422+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"6a97f83c918011f18dbe1f8f96f1c395": {"id": "6a97f83c918011f18dbe1f8f96f1c395", "doc_id": "688aee0a918011f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909798, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011615561, "task_type": "dataflow", "root_trace_id": "d05a3d8d0d6c4aa38394753a3ea0008c", "root_traceparent": "00-d05a3d8d0d6c4aa38394753a3ea0008c-2c380740bfb060e1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:23:47,865 INFO     30 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-23"
}
```
2026-08-06 10:23:47,866 INFO     30 [qwen-vl-parser] page=11 classify=table report_date=2026-03-23
2026-08-06 10:23:47,899 INFO     30 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5228539, prompt_len=756
2026-08-06 10:23:59,098 INFO     30 [qwen-vl-parser] table API response (len=1286):
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
2026-08-06 10:23:59,104 INFO     30 [qwen-vl-parser] page=11 table: 24 LaTeX lines (bbox 264-287)
2026-08-06 10:23:59,105 INFO     30 [qwen-vl-parser] page=11 table: 24 sections
2026-08-06 10:24:00,838 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4540538, prompt_len=764
2026-08-06 10:24:08,224 INFO     30 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-23"
}
```
2026-08-06 10:24:08,227 INFO     30 [qwen-vl-parser] page=12 classify=table report_date=2026-03-23
2026-08-06 10:24:08,330 INFO     30 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4540538, prompt_len=756
2026-08-06 10:24:16,503 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:24:16.501+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 7, "lag": 0, "done": 0, "failed": 0, "current": {"6a97f83c918011f18dbe1f8f96f1c395": {"id": "6a97f83c918011f18dbe1f8f96f1c395", "doc_id": "688aee0a918011f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909798, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011615561, "task_type": "dataflow", "root_trace_id": "d05a3d8d0d6c4aa38394753a3ea0008c", "root_traceparent": "00-d05a3d8d0d6c4aa38394753a3ea0008c-2c380740bfb060e1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:24:19,251 INFO     30 [qwen-vl-parser] table API response (len=1530):
\begin{tabular}{llllllllll}
\hline
\multicolumn{1}{c}{序} & \multicolumn{1}{c}{代号} & \multicolumn{1}{c}{项目名称} & \multicolumn{1}{c}{结果} & \multicolumn{1}{c}{参考范围} & \multicolumn{1}{c}{单位} & \multicolumn{1}{c}{代号} & \multicolumn{1}{c}{项目名称} & \multicolumn{1}{c}{结果} & \multicolumn{1}{c}{参考范围} & \multicolumn{1}{c}{单位} \\
\hline
1 & WBC & 白细胞 & 3.62 & 3.5--9.5 & 10$^9$/L & 15 & MCV & 红细胞平均体积 & 89.4 & 82--100 & fL \\
2 & NEUT & 中性粒细胞百分比 & 68.80 & 40--75 & \% & 16 & MCH & 平均血红蛋白量 & 30.8 & 27--34 & pg \\
3 & LYMP & 淋巴细胞百分比 & 23.20 & 20--50 & \% & 17 & MCHC & 平均血红蛋白浓度 & 344 & 316--354 & g/L \\
4 & MONO & 单核细胞百分比 & 4.10 & 3--10 & \% & 18 & RDW- & 红细胞分布宽度标准 & 43 & 35--56 & fL \\
5 & EOS\% & 嗜酸性粒细胞百分比 & 2.5 & 0.4--8 & \% & 19 & RDW- & 红细胞分布宽度变异 & 13 & 11--16 & \% \\
6 & BASO & 嗜碱性粒细胞百分比 & 1.40 & ↑0--1 & \% & 20 & PLT & 血小板 & 155 & 125--350 & 10$^9$/L \\
7 & NEUT & 中性粒细胞计数 & 2.49 & 1.8--6.3 & 10$^9$/L & 21 & PDW & 血小板分布宽度 & 10.20 & 9.2--15.6 & fL \\
8 & LYMP & 淋巴细胞计数 & 0.84 & ↓1.1--3.2 & 10$^9$/L & 22 & MPV & 平均血小板体积 & 9.90 & 6.5--12 & fL \\
9 & MONO & 单核细胞计数 & 0.15 & 0.1--0.6 & 10$^9$/L & 23 & PCT & 血小板压积 & 0.150 & 0.108--0.282 & \% \\
10 & EOS\# & 嗜酸性粒细胞计数 & 0.09 & 0.02--0.52 & 10$^9$/L & 24 & P-LC & 大型血小板比率 & 24.00 & 11--45 & \% \\
11 & BASO & 嗜碱性粒细胞计数 & 0.05 & 0--0.06 & 10$^9$/L & 25 & PLCC & 大血小板数目 & 37.20 & 30--90 & 10$^9$/L \\
12 & RBC & 红细胞 & 4.06 & 3.8--5.1 & 10$^12$/L & & & & & & \\
13 & HGB & 血红蛋白 & 125 & 115--150 & g/L & & & & & & \\
14 & HCT & 红细胞压积 & 36.30 & 35--45 & \% & & & & & & \\
\hline
\end{tabular}
2026-08-06 10:24:19,253 INFO     30 [qwen-vl-parser] page=12 table: 21 LaTeX lines (bbox 288-308)
2026-08-06 10:24:19,253 INFO     30 [qwen-vl-parser] page=12 table: 21 sections
2026-08-06 10:24:19,253 INFO     30 [qwen-vl-parser] parse_pdf done: 309 sections from 12 pages.
2026-08-06 10:24:19,268 INFO     30 Close text detector.
2026-08-06 10:24:21,055 INFO     30 Close text recognizer.
2026-08-06 10:24:21,582 INFO     30 Close recognizer.
2026-08-06 10:24:22,465 INFO     30 Close recognizer.
2026-08-06 10:24:23,563 INFO     30 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-06 10:24:23,563 INFO     30 [Trace] task=6a97f83c | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | Parser:MedLink | outputs={"html": "", "json": "309 items", "markdown": "", "text": "", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf", "output_format": "json"}
2026-08-06 10:24:23,563 INFO     30 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-06 10:24:23,665 INFO     30 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:24:23,666 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n⚠️ 住院病程文书归属：病程记录、查房记录、术前小结、术后首次病程记录等住院期间病程文书，与入院记录同属一次住院事件；当它们与入院记录页相邻时，必须合并为一个 AdmissionRecord 片段，不得单独成段、不得归入 DischargeRecord。\n- 病程文书识别特征：标题含\"病程记录\"/\"查房记录\"/\"术前小结\"/\"术后首次病程记录\"，带住院患者信息（科室/床号/住院号），有\"入院时间\"（如\"2020年07月08日 08:36:09入院\"），无\"出院诊断\"/\"出院医嘱\"\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。只有主诉，病史的也属于OutpatientRecord（门诊病历）\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 2025.1 确诊小细胞癌，已行免疫组化协诊\n[BBOX-1] 2025-.2-4给予\" EP\" 化疗联合\" 特瑞普利单抗\" 免疫治疗3周期，\n[BBOX-2] 2025-04-22给予\" EP\" 方案化疗联合\n[BBOX-3] \" 替雷利珠单抗\" 免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗\n[BBOX-4] 2025.5-8 行\" 特瑞普利单抗\" 免疫治疗4周期\n[BBOX-5] 2025.8 PD\n[BBOX-6] 2025.8-2026.2 \" 替雷利珠单抗联合安罗替尼\" 免疫治疗\n[BBOX-7] 1804 - Internet Explorer\n[BBOX-8] 诊疗与病历 申请单 手术管理 医嘱单 会诊管理 重症管理 需关注医嘱 病情总览 质量管理 更多\n[BBOX-9] 汤光冉 住院医师\n[BBOX-10] 日间化疗中心[东院区]\n[BBOX-11] 住院天数: 1 费别: 全国医保居民 余额: 0.00 诊断: 肺恶性肿瘤,恶性肿瘤... 医疗救助类型: 农村低保\n[BBOX-12] 病人列表 全息视图\n[BBOX-13] 操作 编辑 功能 表格 其他\n[BBOX-14] 保存 打印 自动续打 预览 单独打印 手工解锁 隐藏留痕 病历参考 更新数据 首页\n[BBOX-15] 信阳市中心医院\n[BBOX-16] 日间化疗出入院记录\n[BBOX-17] 姓名: 性别:女年龄:65岁 科别:日间化疗中心[东院床号:04 登记号:0000 住院号:25\n[BBOX-18] 区]\n[BBOX-19] 入院时间: 2026年03月23日 08:29:00出院时间: 2026年03月23日 11:14:00 住院天数: 1天\n[BBOX-20] 主诉: 确诊肺癌1年余\n[BBOX-21] 入院情况: 1年余前因“胸闷”就诊我院, 2025-01-17CT增强64: 1.右肺门占位, 考虑恶性病变并\n[BBOX-22] 右肺中下叶不张, 右下肺动受侵可能。2. 双肺纤维索条灶。双肺多发小结节, 转移待排。3.右侧\n[BBOX-23] 胸腔少量积液。4.双肾小囊肿。5.升结肠多发憩室。6.子宫后壁肌瘤可能。7.冠状动脉CTA未见明\n[BBOX-24] 显异常。2025-01-23行纤支镜下肺活检, 2025-01-23 活体组织病理申请 诊断意见: (右中间段支\n[BBOX-25] 气管)考虑小细胞癌, 已行免疫组化协诊。2025-01-26 免疫组化申请: CK广谱 (点+), CD56 (+),\n[BBOX-26] Syn (+), INSM1 (+), CK5/6 (-), P40 (-), TTF1 (+), NapsinA (-), Ki-67 (80%+)。结合HE\n[BBOX-27] 及免疫组化结果, (右中间段支气管)肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04\n[BBOX-28] -01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期, 2025-04-22给予“EP”方案化疗联合\n[BBOX-29] “替雷利珠单抗”免疫治疗1周期, 化疗后呕吐反应较重, 予以对症支持治疗。2025-05-19、2025\n[BBOX-30] -06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加增强\n[BBOX-31] (胸部,上腹部,下腹部) 诊断意见: 1. 右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节。\n[BBOX-32] 100%\n[BBOX-33] 16:56\n[BBOX-34] 2026/3/23\n[BBOX-35] 胸腔少量积液。4.双肾小囊肿。5.升结肠多发息室。6.丁台加壁肌瘤可能。冠状动脉CT示无明显异常。2025-01-23行纤支镜下肺活检，2025-01-23活体组织病理申请 诊断意见：(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。2025-01-26免疫组化申请：CK广谱(点+)，CD56(+)，Syn(+)，INSM1(+)，CK5/6(-)，P40(-)，TTF1(+),NapsinA(-)，Ki-67(80%+)。结合HE及免疫组化结果，(右中间段支气管)肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期，2025-04-22给予“EP”方案化疗联合“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗。2025-05-19、2025-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加强(胸部，上腹部，下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节，转移瘤可能；建议追踪复查。2.双肺慢性炎症，右肺中叶局限性支扩，双侧胸腔少量积液。3.脾脏低密度灶，建议追踪复查。4.胆囊可疑小结石。升结肠多发憩室。5.双肾小囊肿。与2025-05-18日片比较：右肺中叶局限性支扩，右肺下叶内基底段结节较前增大，右肺门淋巴结较前增大。考虑病情进展，于2025-08-23给予“安罗替尼12mg”联合“替雷利珠单抗”抗肿瘤治疗1周期。后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-22、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重无明显变化。诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利，予办理出院手续。\n[BBOX-36] 国家医保编码：D411502011804 - Internet Explorer\n[BBOX-37] 美系统) 修改患者信息 诊疗与病历 申请单 手术管理 医嘱单 会诊管理 重症管理 需关注医嘱 病情总览 质量管理 更多\n[BBOX-38] 汤光冉 住院医师\n[BBOX-39] 日间化疗中心[东院区]\n[BBOX-40] 0000 床号: 04 住院天数: 1 费别: 全国医保居民 余额: 0.00 诊断: 肺恶性肿瘤,恶性肿瘤... 医疗救助类型: 农村低保\n[BBOX-41] 病人列表 全息视图\n[BBOX-42] (1) ×\n[BBOX-43] 操作 编辑 功能 表格 其他\n[BBOX-44] 历\n[BBOX-45] 保存 打印 自动续打 预览 单独打印 手工解锁 隐藏留痕 病历参考 更新数据 首页\n[BBOX-46] 记录\n[BBOX-47] 1:09:45 曾庆星\n[BBOX-48] 医师审核\n[BBOX-49] 录单\n[BBOX-50] 1:10:52 曾庆星\n[BBOX-51] 医师审核\n[BBOX-52] 录单\n[BBOX-53] 1:11:53 曾庆星\n[BBOX-54] 医师审核\n[BBOX-55] 11:12:02 曾庆星\n[BBOX-56] 医师审核\n[BBOX-57] 单(日间...\n[BBOX-58] 11:13:02 曾庆星\n[BBOX-59] 医师审核\n[BBOX-60] 已打印\n[BBOX-61] 11:15:03 曾庆星\n[BBOX-62] 医师审核\n[BBOX-63] 评估表\n[BBOX-64] 16:30:58 曾庆星\n[BBOX-65] 院医师审核\n[BBOX-66] /TE风险评...\n[BBOX-67] 16:32:44 曾庆星\n[BBOX-68] 院医师审核\n[BBOX-69] 后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-2\n[BBOX-70] 2、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我\n[BBOX-71] 院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重\n[BBOX-72] 无明显变化。\n[BBOX-73] 诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利\n[BBOX-74] ，予办理出院手续。\n[BBOX-75] 出院情况：患者未诉不适，神志清，精神可，生命体征平稳。\n[BBOX-76] 出院诊断：\n[BBOX-77] 1.恶性肿瘤免疫治疗\n[BBOX-78] 2.肺恶性肿瘤小细胞肺癌IV期\n[BBOX-79] 3.肺继发恶性肿瘤\n[BBOX-80] 4.冠状动脉粥样硬化性心脏病\n[BBOX-81] 5.胸腔积液\n[BBOX-82] 6.心包积液\n[BBOX-83] 7.肺部感染\n[BBOX-84] 8.腔隙性脑梗死\n[BBOX-85] 9.肾功能检查的异常结果\n[BBOX-86] 1\n[BBOX-87] 100%\n[BBOX-88] 16:57\n[BBOX-89] 2026/3/23\n[BBOX-90] 信阳市中心医院\n[BBOX-91] 免疫病理诊断报告\n[BBOX-92] 免疫组化号：MT25-\n[BBOX-93] 姓名：\n[BBOX-94] 性别：女\n[BBOX-95] 年龄：64岁\n[BBOX-96] 送检医院：\n[BBOX-97] 病区：肿瘤内科五护理单元[东病理号：D25-01313\n[BBOX-98] 就诊卡号：\n[BBOX-99] 住院号：2\n[BBOX-100] 病区床号：21\n[BBOX-101] 送检标本：肺手术标本\n[BBOX-102] 送检时间：2025-01-24\n[BBOX-103] 临床诊断：\n[BBOX-104] 光镜所见：\n[BBOX-105] 免疫病理诊断：\n[BBOX-106] CK广谱（点+），CD56（+），Syn（+），INSM1（+），CK5/6（-），P40（-），TTF1（+），\n[BBOX-107] NapsinA（-），Ki-67（80%+）。\n[BBOX-108] 结合HE及免疫组化结果，（右中间段支气管）肺小细胞神经内分泌癌。\n[BBOX-109] 初诊医师：刘磊\n[BBOX-110] 复诊医师：刘磊\n[BBOX-111] 报告日期：2025-01-26 10:49\n[BBOX-112] 备注：1.本报告单仅供临床参考 2.如临床对报告内容有疑问请与报告医生联系。联系电话：0376-6227723(西院区)，0376-6667570(东院区)。\n[BBOX-113] 3.此报告必须经过病理科医师签字有效。\n[BBOX-114] 信阳市中心医院\n[BBOX-115] 病理检查报告单\n[BBOX-116] 病理号：D25\n[BBOX-117] 姓名：\n[BBOX-118] 性别：女\n[BBOX-119] 年龄：64岁\n[BBOX-120] 送检医院：\n[BBOX-121] 送检科室：呼吸与危重症医学科送检日期：2025-01-22\n[BBOX-122] 门诊号：9\n[BBOX-123] 住院号：25\n[BBOX-124] 床号：21\n[BBOX-125] 送检医师：周鹏飞\n[BBOX-126] 送检标本：右中间段支气管\n[BBOX-127] 临床诊断：\n[BBOX-128] 巨检：灰白色碎组织最大径0.3厘米。全取\n[BBOX-129] 病理诊断：\n[BBOX-130] (右中间段支气管)考虑小细胞癌，已行免疫组化协诊。\n[BBOX-131] 初诊医师：刘晶晶\n[BBOX-132] 复诊医师：刘磊\n[BBOX-133] 报告日期：2025-01-23 19:26\n[BBOX-134] 备注：1.本报告单仅供临床参考 2.如临床对报告内容有疑问请与报告医生联系。联系电话：0376-6227723(西院区)；0376-6667570(东院区)。\n[BBOX-135] 3.此报告必须经过病理科医师签字有效。\n[BBOX-136] 信阳市中心医院\n[BBOX-137] 影像科CT诊断报告书\n[BBOX-138] 扫描\n[BBOX-139] 获取电子胶\n[BBOX-140] 片和报告(试用)\n[BBOX-141] 影像号: 000\n[BBOX-142] 报告日期: 2025-12-22 16:36\n[BBOX-143] 姓名:\n[BBOX-144] 性别: 女\n[BBOX-145] 年龄: 64岁\n[BBOX-146] 检查日期: 2025-12-22\n[BBOX-147] 科别: 日间化疗中心[东院区]院号: 2\n[BBOX-148] 门诊号:/\n[BBOX-149] 检查时间: 09:53:10\n[BBOX-150] 检查方法: 胸部CT平扫,胸部CT增强,上腹部CT平扫,上腹部CT增强,下腹部CT平扫,下腹部CT增强\n[BBOX-151] 技术参数:\n[BBOX-152] 影像学所见:\n[BBOX-153] 双侧胸廓对称,右肺门增大,可见不规则状软组织密度影,密度不均,边\n[BBOX-154] 界不清,强化不均,右肺中下叶支气管稍变窄,双肺可见条索状及结节状高密\n[BBOX-155] 度影,较大病灶位于右肺下叶内基底段见实性结节,大小约为15.8×15.4mm,\n[BBOX-156] 轻度强化。右肺中叶局限性支扩。气管、支气管通畅,右肺门见明显肿大淋巴\n[BBOX-157] 结,轻度强化,双侧胸膜腔及心包腔可见积液征象。与2025-8-21日片比较:\n[BBOX-158] 双侧胸腔积液增多,心包积液新增,右肺门软组织密度影及淋巴结增大。\n[BBOX-159] 肝脏未见明显异常密度及异常强化征象,胆囊内隐约见斑点状高密度影,\n[BBOX-160] 脾脏见数个小灶状低强化影。胰腺形态、大小、密度正常。双肾见小圆形低密\n[BBOX-161] 度影,边界清,增强未见明显强化。腹膜后未见明显增大淋巴结,腹腔未见明\n[BBOX-162] 显积液征象。升结肠见多发小囊袋状外凸影。与2025-8-21日片比较:大致相\n[BBOX-163] 仿。\n[BBOX-164] 影像学意见:\n[BBOX-165] 1. 右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节,转移瘤可能;建\n[BBOX-166] 议追踪复查:右肺门肿大淋巴结。\n[BBOX-167] 2. 双肺慢性炎症,右肺中叶局限性支扩,双侧胸腔积液,心包积液。\n[BBOX-168] 3. 脾脏低密度灶,建议追踪复查。\n[BBOX-169] 4. 胆囊可疑小结石。升结肠多发憩室。\n[BBOX-170] 5. 双肾小囊肿。\n[BBOX-171] 报告医师:\n[BBOX-172] 审核医师:\n[BBOX-173] 此报告仅供临床医师参考,签字生效\n[BBOX-174] 打印时间: 2025-12-22 16:36:26\n[BBOX-175] 信阳市中心医院\n[BBOX-176] 影像科CT诊断报告书\n[BBOX-177] 扫描此二维码可\n[BBOX-178] 以电子胶\n[BBOX-179] 片和报告(试用)\n[BBOX-180] 影像号: 0000\n[BBOX-181] 报告日期: 2026-02-25 15:36\n[BBOX-182] 姓名:\n[BBOX-183] 性别: 女\n[BBOX-184] 年龄: 65岁\n[BBOX-185] 检查日期: 2026-02-25\n[BBOX-186] 科别: 肿瘤内科五门诊[东院\n[BBOX-187] 住院号: /\n[BBOX-188] 门诊号: 1\n[BBOX-189] 6\n[BBOX-190] 检查时间: 08:57:41\n[BBOX-191] 检查方法: 胸部CT平扫加薄层\n[BBOX-192] 技术参数:\n[BBOX-193] 影像学所见:\n[BBOX-194] 双侧胸廓对称, 右肺门增大, 可见不规则状软组织密度影, 密度不均, 边\n[BBOX-195] 界不清, 右肺中下叶支气管稍变窄, 双肺可见条索状及结节状高密度影。右肺\n[BBOX-196] 中叶局限性支扩。气管、支气管通畅, 右肺门见明显肿大淋巴结, 右侧胸膜局\n[BBOX-197] 部稍厚, 双侧胸膜腔及心包腔可见积液征象。与2025-12-22日片比较: 右侧胸\n[BBOX-198] 腔积液增多, 右肺门软组织密度影及淋巴结进一步增大, 右肺结节增大, 右侧\n[BBOX-199] 胸膜局部稍增厚。\n[BBOX-200] 影像学意见:\n[BBOX-201] 1. 右肺癌并右肺中下叶不张治疗状态。双肺多发结节, 转移瘤可能; 右肺门\n[BBOX-202] 肿大淋巴结转移。\n[BBOX-203] 2. 双肺慢性炎症, 双侧胸腔积液, 心包积液。\n[BBOX-204] 3. 右侧胸膜局部稍厚, 不除外转移。\n[BBOX-205] 报告医师:\n[BBOX-206] 肖健\n[BBOX-207] 审核医师:\n[BBOX-208] 贺玲\n[BBOX-209] 此报告仅供临床医师参考, 签字生效\n[BBOX-210] 打印时间: 2026-02-25 15:36:58\n[BBOX-211] 信阳市中心医院心电图报告单\n[BBOX-212] 门诊号:\n[BBOX-213] 姓名:\n[BBOX-214] P波宽度: 141ms\n[BBOX-215] 诊断: 1.窦性心律\n[BBOX-216] 住院号: 0000\n[BBOX-217] 性别: 女\n[BBOX-218] P-R间期: 181ms\n[BBOX-219] 【120-200】\n[BBOX-220] 2.低电压\n[BBOX-221] 床位号: 04\n[BBOX-222] 年龄: 65岁\n[BBOX-223] QRS时限: 101ms\n[BBOX-224] 【60-110】\n[BBOX-225] 科室: 日间化疗中心[心率: 77bpm\n[BBOX-226] 【60-100】\n[BBOX-227] QT/QTc: 358/406ms\n[BBOX-228] 【360-440】\n[BBOX-229] 东院区]\n[BBOX-230] 电轴: 60°\n[BBOX-231] 【-30-90】\n[BBOX-232] 2026-03-23 08:43:55\n[BBOX-233] 25mm/s 10mm/mV\n[BBOX-234] I\n[BBOX-235] V1\n[BBOX-236] V3R\n[BBOX-237] II\n[BBOX-238] V2\n[BBOX-239] III\n[BBOX-240] V3\n[BBOX-241] V4R\n[BBOX-242] aVR\n[BBOX-243] V4\n[BBOX-244] aVL\n[BBOX-245] V5\n[BBOX-246] V5R\n[BBOX-247] aVF\n[BBOX-248] V6\n[BBOX-249] II\n[BBOX-250] 检查时间: 2026/3/23 8:43:55\n[BBOX-251] 报告时间: 2026/3/23 8:59:30\n[BBOX-252] 报告医生:\n[BBOX-253] 审核医生:\n[BBOX-254] \\begin{tabular}{ccccccccc}\n[BBOX-255] 报告时间: 2026-03-23\n[BBOX-256] \\hline\n[BBOX-257] 序号 & 项目代号 & 项目名称 & 结果 & 单位 & 参考值 \\\\\n[BBOX-258] \\hline\n[BBOX-259] 1 & CEA & 癌胚抗原 & 5.03 & ng/mL & 0—5.2 \\\\\n[BBOX-260] 2 & CYFRA21-1 & 非小细胞肺癌相关抗原 & 4.60 & ng/ml & 0—3.3 \\\\\n[BBOX-261] 3 & NSE & 神经元特异性烯醇化酶测定 & 10.60 & ng/mL & 0—16.3 \\\\\n[BBOX-262] \\hline\n[BBOX-263] \\end{tabular}\n[BBOX-264] \\begin{tabular}{ccccccccc}\n[BBOX-265] 报告时间: 2026-03-23\n[BBOX-266] \\hline\n[BBOX-267] 序 & 代号 & 名称 & 结果 & 参考范围 & 单位 & 序 & 代号 & 名称 & 结果 & 参考范围 & 单位 \\\\\n[BBOX-268] \\hline\n[BBOX-269] 1 & ALT & 谷丙转氨酶 & 52 & ↑ 7—40 & U/L & 18 & CK & 肌酸激酶 & 396 & ↑ 26—192 & U/L \\\\\n[BBOX-270] 2 & AST & 谷草转氨酶 & 54 & ↑ 13—35 & U/L & 19 & CK-MB & 肌酸酶同功酶 & 17.70 & 7—25 & U/L \\\\\n[BBOX-271] 3 & TP & 总蛋白 & 69.8 & 65—85 & g/L & 20 & MYO & 肌红蛋白 & 77.4 & ↑ 0—70 & ug/L \\\\\n[BBOX-272] 4 & ALB & 白蛋白 & 48.5 & 40—55 & g/L & 21 & K & 钾 & 3.74 & 3.5—5.3 & mmol/L \\\\\n[BBOX-273] 5 & GLOB & 球蛋白 & 21.3 & 20—40 & g/L & 22 & NA & 钠 & 132 & ↓ 137—147 & mmol/L \\\\\n[BBOX-274] 6 & A/G & 白球比 & 2.3 & 1.2—2.4 & & 23 & CL & 氯 & 96.0 & ↓ 99—110 & mmol/L \\\\\n[BBOX-275] 7 & TBIL & 总胆红素 & 13.6 & 1.7—21 & umol/L & 24 & CA & 钙 & 2.12 & 2.02—2.6 & mmol/L \\\\\n[BBOX-276] 8 & DBIL & 直接胆红素 & 1.7 & 0—6.8 & umol/L & 25 & CRP & C反应蛋白 & 0.41 & 0—5 & mg/L \\\\\n[BBOX-277] 9 & IBIL & 间接胆红素 & 11.9 & 3—13.6 & umol/L & 26 & eGFR & 估算肾小球滤 & 55.02 & & ml/min \\\\\n[BBOX-278] 10 & ALP & 碱性磷酸酶 & 67 & 50—135 & U/L & & & & & & \\\\\n[BBOX-279] 11 & GGT & 谷氨酰转肽酶 & 19 & 7—45 & U/L & & & & & & \\\\\n[BBOX-280] 12 & UREA & 尿素 & 4.15 & 2.76—8.07 & mmol/L & & & & & & \\\\\n[BBOX-281] 13 & CREA & 肌酐 & 94 & ↑ 45—84 & umol/L & & & & & & \\\\\n[BBOX-282] 14 & UA & 尿酸 & 192 & 143—339 & umol/L & & & & & & \\\\\n[BBOX-283] 15 & CO2 & 二氧化碳 & 25.9 & 22—29 & mmol/L & & & & & & \\\\\n[BBOX-284] 16 & GLU & 葡萄糖 & 6.25 & ↑ 3.8—6.1 & mmol/L & & & & & & \\\\\n[BBOX-285] 17 & LDH & 乳酸脱氢酶 & 291 & ↑ 135—214 & U/L & & & & & & \\\\\n[BBOX-286] \\hline\n[BBOX-287] \\end{tabular}\n[BBOX-288] \\begin{tabular}{llllllllll}\n[BBOX-289] 报告时间: 2026-03-23\n[BBOX-290] \\hline\n[BBOX-291] \\multicolumn{1}{c}{序} & \\multicolumn{1}{c}{代号} & \\multicolumn{1}{c}{项目名称} & \\multicolumn{1}{c}{结果} & \\multicolumn{1}{c}{参考范围} & \\multicolumn{1}{c}{单位} & \\multicolumn{1}{c}{代号} & \\multicolumn{1}{c}{项目名称} & \\multicolumn{1}{c}{结果} & \\multicolumn{1}{c}{参考范围} & \\multicolumn{1}{c}{单位} \\\\\n[BBOX-292] \\hline\n[BBOX-293] 1 & WBC & 白细胞 & 3.62 & 3.5--9.5 & 10$^9$/L & 15 & MCV & 红细胞平均体积 & 89.4 & 82--100 & fL \\\\\n[BBOX-294] 2 & NEUT & 中性粒细胞百分比 & 68.80 & 40--75 & \\% & 16 & MCH & 平均血红蛋白量 & 30.8 & 27--34 & pg \\\\\n[BBOX-295] 3 & LYMP & 淋巴细胞百分比 & 23.20 & 20--50 & \\% & 17 & MCHC & 平均血红蛋白浓度 & 344 & 316--354 & g/L \\\\\n[BBOX-296] 4 & MONO & 单核细胞百分比 & 4.10 & 3--10 & \\% & 18 & RDW- & 红细胞分布宽度标准 & 43 & 35--56 & fL \\\\\n[BBOX-297] 5 & EOS\\% & 嗜酸性粒细胞百分比 & 2.5 & 0.4--8 & \\% & 19 & RDW- & 红细胞分布宽度变异 & 13 & 11--16 & \\% \\\\\n[BBOX-298] 6 & BASO & 嗜碱性粒细胞百分比 & 1.40 & ↑0--1 & \\% & 20 & PLT & 血小板 & 155 & 125--350 & 10$^9$/L \\\\\n[BBOX-299] 7 & NEUT & 中性粒细胞计数 & 2.49 & 1.8--6.3 & 10$^9$/L & 21 & PDW & 血小板分布宽度 & 10.20 & 9.2--15.6 & fL \\\\\n[BBOX-300] 8 & LYMP & 淋巴细胞计数 & 0.84 & ↓1.1--3.2 & 10$^9$/L & 22 & MPV & 平均血小板体积 & 9.90 & 6.5--12 & fL \\\\\n[BBOX-301] 9 & MONO & 单核细胞计数 & 0.15 & 0.1--0.6 & 10$^9$/L & 23 & PCT & 血小板压积 & 0.150 & 0.108--0.282 & \\% \\\\\n[BBOX-302] 10 & EOS\\# & 嗜酸性粒细胞计数 & 0.09 & 0.02--0.52 & 10$^9$/L & 24 & P-LC & 大型血小板比率 & 24.00 & 11--45 & \\% \\\\\n[BBOX-303] 11 & BASO & 嗜碱性粒细胞计数 & 0.05 & 0--0.06 & 10$^9$/L & 25 & PLCC & 大血小板数目 & 37.20 & 30--90 & 10$^9$/L \\\\\n[BBOX-304] 12 & RBC & 红细胞 & 4.06 & 3.8--5.1 & 10$^12$/L & & & & & & \\\\\n[BBOX-305] 13 & HGB & 血红蛋白 & 125 & 115--150 & g/L & & & & & & \\\\\n[BBOX-306] 14 & HCT & 红细胞压积 & 36.30 & 35--45 & \\% & & & & & & \\\\\n[BBOX-307] \\hline\n[BBOX-308] \\end{tabular}"
  }
]
2026-08-06 10:24:29,892 INFO     30 [DEBUG-COLLECT] got redis_msg, msg_id=1786011867431-0
2026-08-06 10:24:29,893 INFO     30 [DEBUG-COLLECT] msg keys=['id', 'doc_id', 'from_page', 'to_page', 'task_type', 'priority', 'begin_at', 'create_time', 'create_date', 'update_time', 'update_date', 'root_trace_id', 'root_traceparent', 'trace_source', 'kb_id', 'tenant_id', 'dataflow_id', 'file'], task_type=dataflow, id=00b9d592918111f18dbe1f8f96f1c395
2026-08-06 10:24:29,893 INFO     30 [DEBUG-COLLECT] normal branch, calling TaskService.get_task(00b9d592918111f18dbe1f8f96f1c395)
2026-08-06 10:24:29,918 INFO     30 [DEBUG-COLLECT] get_task returned: <class 'dict'>, is_none=False
2026-08-06 10:24:29,920 INFO     30 handle_task begin for task {"id": "00b9d592918111f18dbe1f8f96f1c395", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011867426, "task_type": "dataflow", "root_trace_id": "1ab3198c92574fb4b2701d0f5db7322f", "root_traceparent": "00-1ab3198c92574fb4b2701d0f5db7322f-bdaff6f64a5f4a64-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-06 10:24:30,198 INFO     30 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.004s]
2026-08-06 10:24:30,487 INFO     30 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-06 10:24:30,573 INFO     30 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-06 10:24:30,574 INFO     30 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-06 10:24:30,594 INFO     30 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-06 10:24:30,595 INFO     30 ============================================================
2026-08-06 10:24:30,595 INFO     30 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-06 10:24:30,595 INFO     30    model_dir : /ragflow/rag/res/deepdoc
2026-08-06 10:24:30,595 INFO     30 ============================================================
2026-08-06 10:24:30,595 INFO     30 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-06 10:24:30,595 INFO     30 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-06 10:24:30,599 INFO     30 No torch found.
2026-08-06 10:24:35,549 INFO     30 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:24:36,110 INFO     30 [SmartSplitter] SmartSplitter done: 9 chunks from 9 LLM segments (all bbox_id). Types: {'AdmissionRecord': 1, 'ExaminationReport': 5, 'LabReport': 3}
2026-08-06 10:24:37,266 INFO     30 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-06 10:24:37,274 INFO     30 [Trace] task=6a97f83c | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "309 items", "markdown": "", "text": "", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf", "output_format": "chunks", "chunks": "9 items, types={'AdmissionRecord': 1, 'ExaminationReport': 5, 'LabReport': 3}"}
2026-08-06 10:24:37,274 INFO     30 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-06 10:24:37,275 INFO     30 [ChunkRouter] Routed 9 chunks into 3 groups: {'chunks_Admission': 1, 'chunks_Examination': 5, 'chunks_LabExam': 3}
2026-08-06 10:24:37,650 INFO     30 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-06 10:24:37,650 INFO     30 [Trace] task=6a97f83c | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | ChunkRouter:Router | outputs={"html": "", "json": "309 items", "markdown": "", "text": "", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf", "output_format": "chunks", "chunks": "9 items, types={'AdmissionRecord': 1, 'ExaminationReport': 5, 'LabReport': 3}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 5, \"chunks_LabExam\": 3}"}
2026-08-06 10:24:37,651 INFO     30 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-06 10:24:37,839 INFO     30 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 10:24:37,839 INFO     30 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[9]
2026-08-06 10:24:37,840 INFO     30 [qwen-vl-table] positions ： [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 10:24:40,545 INFO     30 [qwen-vl-table] page=9, rect=2376x1500, img=(6600x4167)
2026-08-06 10:24:40,546 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:24:40,547 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 254, \"bbox_end\": 263, \"encounter_dates\": [\"2026-03-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2026-03-23\n\\hline\n序号 & 项目代号 & 项目名称 & 结果 & 单位 & 参考值 \\\\\n\\hline\n1 & CEA & 癌胚抗原 & 5.03 & ng/mL & 0—5.2 \\\\\n2 & CYFRA21-1 & 非小细胞肺癌相关抗原 & 4.60 & ng/ml & 0—3.3 \\\\\n3 & NSE & 神经元特异性烯醇化酶测定 & 10.60 & ng/mL & 0—16.3 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-06 10:24:43,746 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:24:43,760 INFO     30 [qwen-vl-table] page=9 LLM output (len=566):
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
2026-08-06 10:24:43,761 INFO     30 [qwen-vl-table] coord grouping: {9: 3}
2026-08-06 10:24:43,836 INFO     30 [qwen-vl-table] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=8287882, prompt_len=535
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
2026-08-06 10:24:45,759 INFO     30 [qwen-vl-parser] parse_pdf start, total_pages=52
2026-08-06 10:24:46,072 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1118960, prompt_len=764
2026-08-06 10:24:48,079 INFO     30 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-01-29"
}
```
2026-08-06 10:24:48,080 INFO     30 [qwen-vl-parser] page=1 classify=text report_date=2026-01-29
2026-08-06 10:24:48,118 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1118960, prompt_len=401
2026-08-06 10:24:58,714 INFO     30 [qwen-vl-table] coord API raw response (len=163):
[
	{"text": "癌胚抗原", "bbox": [300, 341, 357, 364]},
	{"text": "非小细胞肺癌相关抗原", "bbox": [300, 371, 441, 394]},
	{"text": "神经元特异性烯醇化酶测定", "bbox": [300, 403, 468, 426]}
]
2026-08-06 10:24:58,715 INFO     30 [qwen-vl-table] coord API: raw_items=3, valid_items=3, elapsed=14.7s
2026-08-06 10:24:58,716 INFO     30 [qwen-vl-table] coord item[0]: text=癌胚抗原, bbox=[300, 341, 357, 364]
2026-08-06 10:24:58,716 INFO     30 [qwen-vl-table] coord item[1]: text=非小细胞肺癌相关抗原, bbox=[300, 371, 441, 394]
2026-08-06 10:24:58,716 INFO     30 [qwen-vl-table] coord item[2]: text=神经元特异性烯醇化酶测定, bbox=[300, 403, 468, 426]
2026-08-06 10:24:58,723 INFO     30 [qwen-vl-table] page=9 coord: matched 3/3, time=14.7s
2026-08-06 10:24:58,724 INFO     30 [qwen-vl-table] new_positions (3):
[[10, 712.8, 848.232, 511.5, 546.0], [10, 712.8, 1047.816, 556.5, 591.0], [10, 712.8, 1111.9679999999998, 604.5, 639.0]]
2026-08-06 10:24:58,725 INFO     30 [qwen-vl-table] ═══ DONE ═══ items=3, matched=3, pages=1, time=20.9s
2026-08-06 10:24:58,746 INFO     30 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 10:24:58,747 INFO     30 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[10]
2026-08-06 10:24:58,748 INFO     30 [qwen-vl-table] positions ： [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 10:25:00,610 INFO     30 [qwen-vl-table] page=10, rect=2000x1128, img=(5556x3134)
2026-08-06 10:25:00,611 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:25:00,611 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 264, \"bbox_end\": 287, \"encounter_dates\": [\"2026-03-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2026-03-23\n\\hline\n序 & 代号 & 名称 & 结果 & 参考范围 & 单位 & 序 & 代号 & 名称 & 结果 & 参考范围 & 单位 \\\\\n\\hline\n1 & ALT & 谷丙转氨酶 & 52 & ↑ 7—40 & U/L & 18 & CK & 肌酸激酶 & 396 & ↑ 26—192 & U/L \\\\\n2 & AST & 谷草转氨酶 & 54 & ↑ 13—35 & U/L & 19 & CK-MB & 肌酸酶同功酶 & 17.70 & 7—25 & U/L \\\\\n3 & TP & 总蛋白 & 69.8 & 65—85 & g/L & 20 & MYO & 肌红蛋白 & 77.4 & ↑ 0—70 & ug/L \\\\\n4 & ALB & 白蛋白 & 48.5 & 40—55 & g/L & 21 & K & 钾 & 3.74 & 3.5—5.3 & mmol/L \\\\\n5 & GLOB & 球蛋白 & 21.3 & 20—40 & g/L & 22 & NA & 钠 & 132 & ↓ 137—147 & mmol/L \\\\\n6 & A/G & 白球比 & 2.3 & 1.2—2.4 & & 23 & CL & 氯 & 96.0 & ↓ 99—110 & mmol/L \\\\\n7 & TBIL & 总胆红素 & 13.6 & 1.7—21 & umol/L & 24 & CA & 钙 & 2.12 & 2.02—2.6 & mmol/L \\\\\n8 & DBIL & 直接胆红素 & 1.7 & 0—6.8 & umol/L & 25 & CRP & C反应蛋白 & 0.41 & 0—5 & mg/L \\\\\n9 & IBIL & 间接胆红素 & 11.9 & 3—13.6 & umol/L & 26 & eGFR & 估算肾小球滤 & 55.02 & & ml/min \\\\\n10 & ALP & 碱性磷酸酶 & 67 & 50—135 & U/L & & & & & & \\\\\n11 & GGT & 谷氨酰转肽酶 & 19 & 7—45 & U/L & & & & & & \\\\\n12 & UREA & 尿素 & 4.15 & 2.76—8.07 & mmol/L & & & & & & \\\\\n13 & CREA & 肌酐 & 94 & ↑ 45—84 & umol/L & & & & & & \\\\\n14 & UA & 尿酸 & 192 & 143—339 & umol/L & & & & & & \\\\\n15 & CO2 & 二氧化碳 & 25.9 & 22—29 & mmol/L & & & & & & \\\\\n16 & GLU & 葡萄糖 & 6.25 & ↑ 3.8—6.1 & mmol/L & & & & & & \\\\\n17 & LDH & 乳酸脱氢酶 & 291 & ↑ 135—214 & U/L & & & & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-06 10:25:00,621 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:25:00.617+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 8, "lag": 0, "done": 0, "failed": 0, "current": {"6a97f83c918011f18dbe1f8f96f1c395": {"id": "6a97f83c918011f18dbe1f8f96f1c395", "doc_id": "688aee0a918011f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909798, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011615561, "task_type": "dataflow", "root_trace_id": "d05a3d8d0d6c4aa38394753a3ea0008c", "root_traceparent": "00-d05a3d8d0d6c4aa38394753a3ea0008c-2c380740bfb060e1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "00b9d592918111f18dbe1f8f96f1c395": {"id": "00b9d592918111f18dbe1f8f96f1c395", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011867426, "task_type": "dataflow", "root_trace_id": "1ab3198c92574fb4b2701d0f5db7322f", "root_traceparent": "00-1ab3198c92574fb4b2701d0f5db7322f-bdaff6f64a5f4a64-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:25:03,026 INFO     30 [qwen-vl-parser] text API response (len=983):
["呼出气一氧化氮测定报告单", "病人信息：", "编号：482", "姓名：", "年龄：41岁9月27天", "性别：女", "科室：普通儿科一区", "出生日期：1984-04-02", "测定时间：2026/1/29 11:02:42", "测定信息：", "一小时内禁止饮食：■是", "一小时内禁止剧烈运动：■是", "三小时内禁止食用特殊食品*：■是", "一小时内禁止抽烟：■是", "三天内使用激素类药物：■是 □否", "三天内使用抗生素：□是 ■否", "症状：□咳嗽 □喘息 □鼻塞 □喷嚏 ■其他", "病史：□过敏史 □其它", "*是指西兰花、芥蓝、生菜、莴苣、芹菜、水萝卜、熏制、腌制类食品。", "测定项目：", "呼气方式：■在线 □离线 □潮气", "呼气温度：20.1℃", "呼气压力：13.6cmH20", "呼气平均流速：48ml/s", "呼气NO浓度：", "32.7,31.0,32.0,31.8,32.1,31.7ppb", "呼气NO浓度均值:32ppb", "呼气方式：■在线 □离线 □潮气", "呼气温度：20.3℃", "呼气压力：7.9cmH20", "呼气平均流速：207ml/s", "呼气NO浓度：", "11.7,11.9,11.3,11.6,11.6,11.6ppb", "呼气NO浓度均值:12ppb", "测定结果：", "FeNO50：32ppb", "FeNO200：12ppb", "CaNO：3.6ppb", "测定意义：", "测定浓度", "参考值", "炎症鉴别诊断", ">12岁", "≤12岁", "FeNO50", "<25ppb", "<20ppb*", "非嗜酸性气道炎症", "25-50ppb", "20-35ppb*", "混合型气道炎症", "≥50ppb", "≥35ppb*", "嗜酸性气道炎症", "FeNO200", ">10ppb", ">8ppb", "小气道炎症", "CaNO", ">5ppb", ">3ppb", "肺泡炎症", "(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)", "复查时间：", "操作员：赵彩红", "医生：马春英", "电", "告", "单", "更", ""]
2026-08-06 10:25:03,027 INFO     30 [qwen-vl-parser] page=1 text: 70 lines (bbox 0-69)
2026-08-06 10:25:03,027 INFO     30 [qwen-vl-parser] page=1 text: 70 sections
2026-08-06 10:25:03,357 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1156349, prompt_len=764
2026-08-06 10:25:05,221 INFO     30 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-01-15"
}
```
2026-08-06 10:25:05,223 INFO     30 [qwen-vl-parser] page=2 classify=text report_date=2026-01-15
2026-08-06 10:25:05,257 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1156349, prompt_len=401
2026-08-06 10:25:15,116 INFO     30 [qwen-vl-parser] text API response (len=1950):
["肺功能检查报告单", "姓名：", "测试号：", "身高：160 cm", "体重：48 kg", "身份证号：", "住院号：", "年龄：41 岁", "性别：女", "科别：--", "联系电话：", "预计值 Bbt % (Bbt/", "A1", "A2", "A3", "FVC", "[L]", "3.13", "3.15", "100.54", "3.15", "3.08", "3.07", "FEV 1", "[L]", "2.70", "1.99", "73.90", "1.99", "1.85", "1.96", "FEV6", "[L]", "3.13", "3.13", "3.05", "FEV 1 % FVC", "[%]", "83.98", "63.25", "75.31", "63.25", "60.02", "63.82", "FEV 1 % VC MAX", "[%]", "81.31", "63.25", "77.78", "63.25", "58.74", "62.12", "FIF 50", "[L/s]", "5.84", "5.77", "5.84", "5.48", "FEV3 % FVC", "[%]", "89.30", "89.30", "87.11", "88.97", "VC MAX", "[L]", "3.19", "3.15", "98.65", "2.99", "PEF", "[L/s]", "6.46", "6.33", "97.97", "6.33", "5.90", "5.95", "MMEF 75/25", "[L/s]", "3.53", "1.06", "30.03", "1.06", "0.89", "0.99", "MEF 25", "[L/s]", "1.77", "0.46", "26.28", "0.46", "0.38", "0.40", "MEF 50", "[L/s]", "4.06", "1.25", "30.90", "1.25", "1.13", "1.24", "MEF 75", "[L/s]", "5.73", "3.01", "52.56", "3.01", "2.22", "2.68", "V backextrapolation [B]", "0.06", "0.06", "0.05", "0.06", "V backextrapol. % FVC", "1.86", "1.86", "1.52", "1.82", "FET", "[s]", "8.73", "8.73", "5.99", "6.71", "FEF 200-1200", "[L/s]", "3.07", "3.07", "2.51", "2.98", "FVC IN", "[L]", "3.19", "2.99", "93.64", "2.26", "2.99", "2.94", "FIV1", "[L]", "2.96", "2.24", "2.96", "2.92", "FIV1 % FVC", "[%]", "99.14", "99.32", "99.14", "99.48", "FEF50 % FIF50", "[%]", "21.46", "21.72", "19.34", "22.60", "PIF", "[L/s]", "6.10", "5.87", "6.10", "5.50", "MVV", "[L/min]", "101.9", "91.45", "89.73", "91.45", "BF MVV", "[1/min]", "75.65", "75.65", "10", "Flow [L/s]", "F/V ex", "Vol [L]", "Vol%VCmax", "Time [s]", "Vol [L]", "F/V In", "Vol [L]", "Time [s]", "意见：", "1.轻度阻塞性通气功能障碍。", "检查质量：FVC：A级。 FEV1：A级。", "备注：受检者检查配合佳。结果仅供参考，请结合临床分析。", "2.最大自主分钟通气量（MVV）在正常范围。", "备注：患者MVV配合佳。结果仅供参考，请结合临床分析。", "审核医生：孙帅森", "检测技师：韦龙华", "2026/1/15", "1604g", "小气道阻解", "不明显。", "米 B", "日 1", "△ 2", "○ 3", "米 B", "日 1", "△ 2", "○ 3", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-06 10:25:15,118 INFO     30 [qwen-vl-parser] page=2 text: 206 lines (bbox 70-275)
2026-08-06 10:25:15,119 INFO     30 [qwen-vl-parser] page=2 text: 206 sections
2026-08-06 10:25:15,386 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:25:15,386 INFO     30 [qwen-vl-table] page=10 LLM output (len=4311):
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
2026-08-06 10:25:15,387 INFO     30 [qwen-vl-table] coord grouping: {10: 26}
2026-08-06 10:25:15,406 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=812029, prompt_len=764
2026-08-06 10:25:15,420 INFO     30 [qwen-vl-table] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=6710078, prompt_len=626
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
2026-08-06 10:25:17,045 INFO     30 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-06 10:25:17,046 INFO     30 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-06 10:25:17,079 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=812029, prompt_len=401
2026-08-06 10:25:30,114 INFO     30 [qwen-vl-parser] text API response (len=1200):
["肺功能报告单", "姓名：", "性别：女", "出生日期：1984/11/00", "年龄：41岁", "住院号：", "测试号：", "身高：160 cm", "体重：48 kg", "身份证号：", "预计", "实1 %(实1/预)", "实2 %(实2/预)", "变异率", "测试日期", "26/1/15", "26/1/15", "测试时间", "9:51:00上午", "10:14:56上午", "FVC", "[L]", "3.13", "3.15", "100.5", "3.25", "103.9", "3.3", "FEV 1", "[L]", "2.70", "1.99", "73.9", "2.26", "83.8", "13.4", "FEV 1 % FVC", "[%]", "83.98", "63.25", "75.3", "69.40", "82.6", "9.7", "FEV 1 % VC MAX", "[%]", "81.31", "63.25", "77.8", "69.40", "85.4", "9.7", "PEF", "[L/s]", "6.46", "6.33", "98.0", "7.25", "112.2", "14.5", "MEF 75", "[L/s]", "5.73", "3.01", "52.6", "3.73", "65.1", "23.8", "MEF 50", "[L/s]", "4.06", "1.25", "30.9", "1.67", "41.2", "33.3", "MEF 25", "[L/s]", "1.77", "0.46", "26.3", "0.59", "33.6", "27.7", "MMEF 75/25", "[L/s]", "3.53", "1.06", "30.0", "1.46", "41.3", "37.6", "FET", "[s]", "8.73", "4.94", "-43.4", "V backextrapolation ex [L]", "0.06", "0.07", "20.1", "V backextrapol. % FVC [%]", "1.86", "2.17", "16.3", "Flow [L/s]", "F/V ex", "10", "5", "0", "1", "2", "3", "4", "5", "6", "7", "10", "F/V In", "医生意见：", "支气管舒张试验阳性。", "（通过储雾罐吸入硫酸沙丁胺醇气雾剂400ug20分钟后。", "FEV1较基线增加大于12 %，且绝对值增加大于200 ml。", "审核医生：孙帅森", "检测技师：朱龙华", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-06 10:25:30,115 INFO     30 [qwen-vl-parser] page=3 text: 127 lines (bbox 276-402)
2026-08-06 10:25:30,115 INFO     30 [qwen-vl-parser] page=3 text: 127 sections
2026-08-06 10:25:30,470 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1188351, prompt_len=764
2026-08-06 10:25:32,570 INFO     30 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2025-04-11"
}
```
2026-08-06 10:25:32,570 INFO     30 [qwen-vl-parser] page=4 classify=text report_date=2025-04-11
2026-08-06 10:25:32,589 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1188351, prompt_len=401
2026-08-06 10:25:34,598 INFO     30 [qwen-vl-table] coord API raw response (len=1266):
[
	{"text": "谷丙转氨酶", "bbox": [213, 264, 288, 290]},
	{"text": "谷草转氨酶", "bbox": [213, 301, 288, 327]},
	{"text": "总蛋白", "bbox": [213, 339, 258, 365]},
	{"text": "白蛋白", "bbox": [213, 375, 258, 400]},
	{"text": "球蛋白", "bbox": [213, 413, 258, 438]},
	{"text": "白球比", "bbox": [213, 450, 258, 475]},
	{"text": "总胆红素", "bbox": [213, 487, 274, 512]},
	{"text": "直接胆红素", "bbox": [213, 523, 288, 548]},
	{"text": "间接胆红素", "bbox": [213, 560, 288, 585]},
	{"text": "碱性磷酸酶", "bbox": [213, 597, 288, 622]},
	{"text": "谷氨酰转肽酶", "bbox": [213, 634, 304, 660]},
	{"text": "尿素", "bbox": [213, 671, 245, 697]},
	{"text": "肌酐", "bbox": [213, 708, 245, 733]},
	{"text": "尿酸", "bbox": [213, 745, 245, 770]},
	{"text": "二氧化碳", "bbox": [213, 782, 274, 807]},
	{"text": "葡萄糖", "bbox": [213, 819, 258, 844]},
	{"text": "乳酸脱氢酶", "bbox": [213, 856, 290, 881]},
	{"text": "肌酸激酶", "bbox": [579, 263, 637, 289]},
	{"text": "肌酸酶同功酶", "bbox": [579, 299, 667, 325]},
	{"text": "肌红蛋白", "bbox": [579, 337, 637, 362]},
	{"text": "钾", "bbox": [579, 374, 594, 399]},
	{"text": "钠", "bbox": [579, 411, 594, 436]},
	{"text": "氯", "bbox": [579, 448, 594, 473]},
	{"text": "钙", "bbox": [579, 484, 594, 509]},
	{"text": "C反应蛋白", "bbox": [579, 520, 645, 545]},
	{"text": "估算肾小球滤", "bbox": [579, 557, 667, 582]}
]
2026-08-06 10:25:34,599 INFO     30 [qwen-vl-table] coord API: raw_items=26, valid_items=26, elapsed=19.2s
2026-08-06 10:25:34,599 INFO     30 [qwen-vl-table] coord item[0]: text=谷丙转氨酶, bbox=[213, 264, 288, 290]
2026-08-06 10:25:34,599 INFO     30 [qwen-vl-table] coord item[1]: text=谷草转氨酶, bbox=[213, 301, 288, 327]
2026-08-06 10:25:34,599 INFO     30 [qwen-vl-table] coord item[2]: text=总蛋白, bbox=[213, 339, 258, 365]
2026-08-06 10:25:34,599 INFO     30 [qwen-vl-table] coord item[3]: text=白蛋白, bbox=[213, 375, 258, 400]
2026-08-06 10:25:34,599 INFO     30 [qwen-vl-table] coord item[4]: text=球蛋白, bbox=[213, 413, 258, 438]
2026-08-06 10:25:34,599 INFO     30 [qwen-vl-table] coord item[5]: text=白球比, bbox=[213, 450, 258, 475]
2026-08-06 10:25:34,599 INFO     30 [qwen-vl-table] coord item[6]: text=总胆红素, bbox=[213, 487, 274, 512]
2026-08-06 10:25:34,599 INFO     30 [qwen-vl-table] coord item[7]: text=直接胆红素, bbox=[213, 523, 288, 548]
2026-08-06 10:25:34,599 INFO     30 [qwen-vl-table] coord item[8]: text=间接胆红素, bbox=[213, 560, 288, 585]
2026-08-06 10:25:34,599 INFO     30 [qwen-vl-table] coord item[9]: text=碱性磷酸酶, bbox=[213, 597, 288, 622]
2026-08-06 10:25:34,599 INFO     30 [qwen-vl-table] coord item[10]: text=谷氨酰转肽酶, bbox=[213, 634, 304, 660]
2026-08-06 10:25:34,599 INFO     30 [qwen-vl-table] coord item[11]: text=尿素, bbox=[213, 671, 245, 697]
2026-08-06 10:25:34,599 INFO     30 [qwen-vl-table] coord item[12]: text=肌酐, bbox=[213, 708, 245, 733]
2026-08-06 10:25:34,599 INFO     30 [qwen-vl-table] coord item[13]: text=尿酸, bbox=[213, 745, 245, 770]
2026-08-06 10:25:34,599 INFO     30 [qwen-vl-table] coord item[14]: text=二氧化碳, bbox=[213, 782, 274, 807]
2026-08-06 10:25:34,599 INFO     30 [qwen-vl-table] coord item[15]: text=葡萄糖, bbox=[213, 819, 258, 844]
2026-08-06 10:25:34,600 INFO     30 [qwen-vl-table] coord item[16]: text=乳酸脱氢酶, bbox=[213, 856, 290, 881]
2026-08-06 10:25:34,600 INFO     30 [qwen-vl-table] coord item[17]: text=肌酸激酶, bbox=[579, 263, 637, 289]
2026-08-06 10:25:34,600 INFO     30 [qwen-vl-table] coord item[18]: text=肌酸酶同功酶, bbox=[579, 299, 667, 325]
2026-08-06 10:25:34,600 INFO     30 [qwen-vl-table] coord item[19]: text=肌红蛋白, bbox=[579, 337, 637, 362]
2026-08-06 10:25:34,600 INFO     30 [qwen-vl-table] coord item[20]: text=钾, bbox=[579, 374, 594, 399]
2026-08-06 10:25:34,600 INFO     30 [qwen-vl-table] coord item[21]: text=钠, bbox=[579, 411, 594, 436]
2026-08-06 10:25:34,600 INFO     30 [qwen-vl-table] coord item[22]: text=氯, bbox=[579, 448, 594, 473]
2026-08-06 10:25:34,600 INFO     30 [qwen-vl-table] coord item[23]: text=钙, bbox=[579, 484, 594, 509]
2026-08-06 10:25:34,600 INFO     30 [qwen-vl-table] coord item[24]: text=C反应蛋白, bbox=[579, 520, 645, 545]
2026-08-06 10:25:34,600 INFO     30 [qwen-vl-table] coord item[25]: text=估算肾小球滤, bbox=[579, 557, 667, 582]
2026-08-06 10:25:34,609 INFO     30 [qwen-vl-table] page=10 coord: matched 26/26, time=19.2s
2026-08-06 10:25:34,610 INFO     30 [qwen-vl-table] new_positions (26):
[[11, 426.0, 576.0, 297.792, 327.11999999999995], [11, 426.0, 576.0, 339.52799999999996, 368.85599999999994], [11, 426.0, 516.0, 382.39199999999994, 411.71999999999997], [11, 426.0, 516.0, 422.99999999999994, 451.19999999999993], [11, 426.0, 516.0, 465.864, 494.06399999999996], [11, 426.0, 516.0, 507.59999999999997, 535.8], [11, 426.0, 548.0, 549.3359999999999, 577.536], [11, 426.0, 576.0, 589.944, 618.1439999999999], [11, 426.0, 576.0, 631.68, 659.8799999999999], [11, 426.0, 576.0, 673.4159999999999, 701.616], [11, 426.0, 608.0, 715.1519999999999, 744.4799999999999], [11, 426.0, 490.0, 756.8879999999999, 786.2159999999999], [11, 426.0, 490.0, 798.6239999999999, 826.824], [11, 426.0, 490.0, 840.3599999999999, 868.56], [11, 426.0, 548.0, 882.0959999999999, 910.2959999999999], [11, 426.0, 516.0, 923.8319999999999, 952.0319999999999], [11, 426.0, 580.0, 965.5679999999999, 993.7679999999999], [11, 1158.0, 1274.0, 296.664, 325.99199999999996], [11, 1158.0, 1334.0, 337.272, 366.59999999999997], [11, 1158.0, 1274.0, 380.13599999999997, 408.33599999999996], [11, 1158.0, 1188.0, 421.87199999999996, 450.07199999999995], [11, 1158.0, 1188.0, 463.60799999999995, 491.80799999999994], [11, 1158.0, 1188.0, 505.34399999999994, 533.544], [11, 1158.0, 1188.0, 545.952, 574.1519999999999], [11, 1158.0, 1290.0, 586.56, 614.76], [11, 1158.0, 1334.0, 628.2959999999999, 656.496]]
2026-08-06 10:25:34,611 INFO     30 [qwen-vl-table] ═══ DONE ═══ items=26, matched=26, pages=1, time=35.9s
2026-08-06 10:25:34,617 INFO     30 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 10:25:34,619 INFO     30 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[11]
2026-08-06 10:25:34,620 INFO     30 [qwen-vl-table] positions ： [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 10:25:35,775 INFO     30 [qwen-vl-table] page=11, rect=1572x1104, img=(4367x3067)
2026-08-06 10:25:35,776 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:25:35,776 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 288, \"bbox_end\": 308, \"encounter_dates\": [\"2026-03-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllllll}\n报告时间: 2026-03-23\n\\hline\n\\multicolumn{1}{c}{序} & \\multicolumn{1}{c}{代号} & \\multicolumn{1}{c}{项目名称} & \\multicolumn{1}{c}{结果} & \\multicolumn{1}{c}{参考范围} & \\multicolumn{1}{c}{单位} & \\multicolumn{1}{c}{代号} & \\multicolumn{1}{c}{项目名称} & \\multicolumn{1}{c}{结果} & \\multicolumn{1}{c}{参考范围} & \\multicolumn{1}{c}{单位} \\\\\n\\hline\n1 & WBC & 白细胞 & 3.62 & 3.5--9.5 & 10$^9$/L & 15 & MCV & 红细胞平均体积 & 89.4 & 82--100 & fL \\\\\n2 & NEUT & 中性粒细胞百分比 & 68.80 & 40--75 & \\% & 16 & MCH & 平均血红蛋白量 & 30.8 & 27--34 & pg \\\\\n3 & LYMP & 淋巴细胞百分比 & 23.20 & 20--50 & \\% & 17 & MCHC & 平均血红蛋白浓度 & 344 & 316--354 & g/L \\\\\n4 & MONO & 单核细胞百分比 & 4.10 & 3--10 & \\% & 18 & RDW- & 红细胞分布宽度标准 & 43 & 35--56 & fL \\\\\n5 & EOS\\% & 嗜酸性粒细胞百分比 & 2.5 & 0.4--8 & \\% & 19 & RDW- & 红细胞分布宽度变异 & 13 & 11--16 & \\% \\\\\n6 & BASO & 嗜碱性粒细胞百分比 & 1.40 & ↑0--1 & \\% & 20 & PLT & 血小板 & 155 & 125--350 & 10$^9$/L \\\\\n7 & NEUT & 中性粒细胞计数 & 2.49 & 1.8--6.3 & 10$^9$/L & 21 & PDW & 血小板分布宽度 & 10.20 & 9.2--15.6 & fL \\\\\n8 & LYMP & 淋巴细胞计数 & 0.84 & ↓1.1--3.2 & 10$^9$/L & 22 & MPV & 平均血小板体积 & 9.90 & 6.5--12 & fL \\\\\n9 & MONO & 单核细胞计数 & 0.15 & 0.1--0.6 & 10$^9$/L & 23 & PCT & 血小板压积 & 0.150 & 0.108--0.282 & \\% \\\\\n10 & EOS\\# & 嗜酸性粒细胞计数 & 0.09 & 0.02--0.52 & 10$^9$/L & 24 & P-LC & 大型血小板比率 & 24.00 & 11--45 & \\% \\\\\n11 & BASO & 嗜碱性粒细胞计数 & 0.05 & 0--0.06 & 10$^9$/L & 25 & PLCC & 大血小板数目 & 37.20 & 30--90 & 10$^9$/L \\\\\n12 & RBC & 红细胞 & 4.06 & 3.8--5.1 & 10$^12$/L & & & & & & \\\\\n13 & HGB & 血红蛋白 & 125 & 115--150 & g/L & & & & & & \\\\\n14 & HCT & 红细胞压积 & 36.30 & 35--45 & \\% & & & & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-06 10:25:35,780 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:25:35.778+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 8, "lag": 0, "done": 0, "failed": 0, "current": {"6a97f83c918011f18dbe1f8f96f1c395": {"id": "6a97f83c918011f18dbe1f8f96f1c395", "doc_id": "688aee0a918011f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909798, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011615561, "task_type": "dataflow", "root_trace_id": "d05a3d8d0d6c4aa38394753a3ea0008c", "root_traceparent": "00-d05a3d8d0d6c4aa38394753a3ea0008c-2c380740bfb060e1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "00b9d592918111f18dbe1f8f96f1c395": {"id": "00b9d592918111f18dbe1f8f96f1c395", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011867426, "task_type": "dataflow", "root_trace_id": "1ab3198c92574fb4b2701d0f5db7322f", "root_traceparent": "00-1ab3198c92574fb4b2701d0f5db7322f-bdaff6f64a5f4a64-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:25:41,895 INFO     30 [qwen-vl-parser] text API response (len=1865):
["肺功能报告单", "姓名：", "出生日期：1984/4/02", "门诊/住院/体检：", "身高：160 cm", "身份证号：", "性别：女", "年龄：41岁", "测试号：", "体重：50 kg", "测试日期", "测试时间", "预计", "实测 % (实/预)", "25/4/11", "14:56:4", "VT", "[L]", "0.36", "0.41", "114.9", "BF", "[1/min]", "20.00", "20.79", "104.0", "MV", "[L/min]", "7.14", "8.54", "119.5", "ERV", "[L]", "1.07", "1.07", "99.4", "VC MAX", "[L]", "3.19", "2.84", "88.9", "FVC", "[L]", "3.13", "2.84", "90.6", "FEV 1", "[L]", "2.70", "1.53", "56.9", "FEV 1 % FVC", "[%]", "83.98", "54.07", "64.4", "FEV 1 % VC MAX", "[%]", "81.31", "54.07", "66.5", "PEF", "[L/s]", "6.46", "4.56", "70.7", "MEF 75", "[L/s]", "5.73", "1.84", "32.1", "MEF 50", "[L/s]", "4.06", "0.84", "20.7", "MEF 25", "[L/s]", "1.77", "0.28", "15.6", "MMEF 75/25", "[L/s]", "3.53", "0.65", "18.3", "FET", "[s]", "8.46", "V backextrapolation ex", "[L]", "0.03", "V backextrapol. % FVC", "[%]", "1.23", "MVV", "[L/min]", "101.93", "75.75", "74.3", "FEV 1*30", "[L/min]", "101.93", "46.03", "45.2", "RV-SB", "[L]", "1.55", "2.56", "164.9", "RV%TLC-SB", "[%]", "32.90", "47.52", "144.4", "TLC-SB", "[L]", "4.77", "5.39", "112.9", "FRC-SB", "[L]", "2.63", "3.31", "126.0", "FRC%TLC-SB", "[%]", "51.66", "61.42", "118.9", "DLCOc SB", "[mmol/min/kPa]", "8.34", "6.95", "83.4", "DLCO SB", "[mmol/min/kPa]", "8.34", "6.95", "83.4", "医生意见：", "1.中重度阻塞性通气功能障碍。", "检查质量：FVC：A级。 FEV1：A级。", "备注：受检者检查配合佳。 结果仅供参考，请结合临床分析。", "2.最大自主分钟通气量（MVV）轻度下降。", "备注：患者MVV配合佳。结果仅供参考，请结合临床分析。", "3.弥散功能在正常范围。4.残总比中度增高。", "审核医生：孙帅森", "检测技师：张青苹", "通气弥散B", "2025/4/11 15:18", "1/1", "布地奈德 4ml Bid 3天", "喷 3个月 后复查肺功能。", "Vol [L]", "PredA0.0", "0.2", "0.4", "0.6", "0.8", "1.0", "Time [min]", "Flow [L/s]", "F/V ex", "10", "5", "0", "2", "4", "6", "F/V in", "10", "Vol [L]", "Vol [L]", "100", "10", "50", "Time [s]", "0", "1", "2", "3", "4", "5", "Volume [L]", "4", "2", "0", "M", "1", "2", "4", "Time [s]", "0", "20", "40", "60", "80"]
2026-08-06 10:25:41,896 INFO     30 [qwen-vl-parser] page=4 text: 198 lines (bbox 403-600)
2026-08-06 10:25:41,896 INFO     30 [qwen-vl-parser] page=4 text: 198 sections
2026-08-06 10:25:42,130 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=801179, prompt_len=764
2026-08-06 10:25:43,682 INFO     30 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-06 10:25:43,683 INFO     30 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-06 10:25:43,723 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=801179, prompt_len=401
2026-08-06 10:25:50,217 INFO     30 [qwen-vl-parser] text API response (len=1203):
["肺功能报告单", "姓名：", "出生日期：1984/4/02", "性别：女", "年龄：41岁", "门诊/住院/体检：", "测试号：", "身高：160 cm", "体重：50 kg", "身份证号：", "预计", "实1 %(实1/预)", "实2 %(实2/预)", "变异率", "测试日期", "25/4/11", "25/4/11", "测试时间", "14:56:47下午", "15:14:32下午", "FVC", "[L]", "3.13", "2.84", "90.6", "3.05", "97.4", "7.5", "FEV 1", "[L]", "2.70", "1.53", "56.9", "1.91", "71.0", "24.7", "FEV 1 % FVC", "[%]", "83.98", "54.07", "64.4", "62.70", "74.7", "16.0", "FEV 1 % VC MAX", "[%]", "81.31", "54.07", "66.5", "62.70", "77.1", "16.0", "PEF", "[L/s]", "6.46", "4.56", "70.7", "5.64", "87.3", "23.6", "MEF 75", "[L/s]", "5.73", "1.84", "32.1", "2.65", "46.3", "44.3", "MEF 50", "[L/s]", "4.06", "0.84", "20.7", "1.23", "30.4", "47.0", "MEF 25", "[L/s]", "1.77", "0.28", "15.6", "0.44", "25.0", "60.2", "MMEF 75/25", "[L/s]", "3.53", "0.65", "18.3", "1.02", "29.1", "58.8", "FET", "[s]", "8.46", "6.41", "-24.2", "V backextrapolation ex [L]", "0.03", "0.06", "71.7", "V backextrapol. % FVC [%]", "1.23", "1.96", "59.6", "Flow [L/s]", "F/V ex", "10", "5", "0", "1", "2", "3", "4", "5", "6", "7", "10", "F/V In", "医生意见：", "支气管舒张试验阳性。", "（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后。", "FEV1较基线增加大于12%，且绝对值增加大于200ml。）", "审核医生：孙帅森", "检测技师：张青苹", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-06 10:25:50,219 INFO     30 [qwen-vl-parser] page=5 text: 127 lines (bbox 601-727)
2026-08-06 10:25:50,219 INFO     30 [qwen-vl-parser] page=5 text: 127 sections
2026-08-06 10:25:50,425 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:25:50,425 INFO     30 [qwen-vl-table] page=11 LLM output (len=4261):
{
  "report_date": "2026-03-23",
  "items": [
    {
      "name": "白细胞",
      "item_code": "WBC",
      "value": "3.62",
      "unit": "10^9/L",
      "reference_range": "3.5--9.5",
      "abnormal": false
    },
    {
      "name": "中性粒细胞百分比",
      "item_code": "NEUT",
      "value": "68.80",
      "unit": "%",
      "reference_range": "40--75",
      "abnormal": false
    },
    {
      "name": "淋巴细胞百分比",
      "item_code": "LYMP",
      "value": "23.20",
      "unit": "%",
      "reference_range": "20--50",
      "abnormal": false
    },
    {
      "name": "单核细胞百分比",
      "item_code": "MONO",
      "value": "4.10",
      "unit": "%",
      "reference_range": "3--10",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞百分比",
      "item_code": "EOS%",
      "value": "2.5",
      "unit": "%",
      "reference_range": "0.4--8",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞百分比",
      "item_code": "BASO",
      "value": "1.40",
      "unit": "%",
      "reference_range": "0--1",
      "abnormal": true
    },
    {
      "name": "中性粒细胞计数",
      "item_code": "NEUT",
      "value": "2.49",
      "unit": "10^9/L",
      "reference_range": "1.8--6.3",
      "abnormal": false
    },
    {
      "name": "淋巴细胞计数",
      "item_code": "LYMP",
      "value": "0.84",
      "unit": "10^9/L",
      "reference_range": "1.1--3.2",
      "abnormal": true
    },
    {
      "name": "单核细胞计数",
      "item_code": "MONO",
      "value": "0.15",
      "unit": "10^9/L",
      "reference_range": "0.1--0.6",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞计数",
      "item_code": "EOS#",
      "value": "0.09",
      "unit": "10^9/L",
      "reference_range": "0.02--0.52",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞计数",
      "item_code": "BASO",
      "value": "0.05",
      "unit": "10^9/L",
      "reference_range": "0--0.06",
      "abnormal": false
    },
    {
      "name": "红细胞",
      "item_code": "RBC",
      "value": "4.06",
      "unit": "10^12/L",
      "reference_range": "3.8--5.1",
      "abnormal": false
    },
    {
      "name": "血红蛋白",
      "item_code": "HGB",
      "value": "125",
      "unit": "g/L",
      "reference_range": "115--150",
      "abnormal": false
    },
    {
      "name": "红细胞压积",
      "item_code": "HCT",
      "value": "36.30",
      "unit": "%",
      "reference_range": "35--45",
      "abnormal": false
    },
    {
      "name": "红细胞平均体积",
      "item_code": "MCV",
      "value": "89.4",
      "unit": "fL",
      "reference_range": "82--100",
      "abnormal": false
    },
    {
      "name": "平均血红蛋白量",
      "item_code": "MCH",
      "value": "30.8",
      "unit": "pg",
      "reference_range": "27--34",
      "abnormal": false
    },
    {
      "name": "平均血红蛋白浓度",
      "item_code": "MCHC",
      "value": "344",
      "unit": "g/L",
      "reference_range": "316--354",
      "abnormal": false
    },
    {
      "name": "红细胞分布宽度标准",
      "item_code": "RDW-",
      "value": "43",
      "unit": "fL",
      "reference_range": "35--56",
      "abnormal": false
    },
    {
      "name": "红细胞分布宽度变异",
      "item_code": "RDW-",
      "value": "13",
      "unit": "%",
      "reference_range": "11--16",
      "abnormal": false
    },
    {
      "name": "血小板",
      "item_code": "PLT",
      "value": "155",
      "unit": "10^9/L",
      "reference_range": "125--350",
      "abnormal": false
    },
    {
      "name": "血小板分布宽度",
      "item_code": "PDW",
      "value": "10.20",
      "unit": "fL",
      "reference_range": "9.2--15.6",
      "abnormal": false
    },
    {
      "name": "平均血小板体积",
      "item_code": "MPV",
      "value": "9.90",
      "unit": "fL",
      "reference_range": "6.5--12",
      "abnormal": false
    },
    {
      "name": "血小板压积",
      "item_code": "PCT",
      "value": "0.150",
      "unit": "%",
      "reference_range": "0.108--0.282",
      "abnormal": false
    },
    {
      "name": "大型血小板比率",
      "item_code": "P-LC",
      "value": "24.00",
      "unit": "%",
      "reference_range": "11--45",
      "abnormal": false
    },
    {
      "name": "大血小板数目",
      "item_code": "PLCC",
      "value": "37.20",
      "unit": "10^9/L",
      "reference_range": "30--90",
      "abnormal": false
    }
  ]
}
2026-08-06 10:25:50,425 INFO     30 [qwen-vl-table] coord grouping: {11: 25}
2026-08-06 10:25:50,457 INFO     30 [qwen-vl-table] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5705072, prompt_len=696
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
2026-08-06 10:25:50,844 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1461935, prompt_len=764
2026-08-06 10:25:52,843 INFO     30 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-06 10:25:52,844 INFO     30 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-06 10:25:52,890 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1461935, prompt_len=401
2026-08-06 10:26:06,600 INFO     30 [qwen-vl-parser] text API response (len=1085):
["院", "入院记录", "姓名：", "科室：产科二区", "床号：", "科室：产科二区", "第(1)次入院记录", "过敏史：无", "姓名：", "性别：女", "年龄：36岁", "身份证号", "职业：", "婚姻：已婚", "民族：汉族", "出生地：", "现住址：", "入院日期：2020-07-08 08:36:09", "邮编", "病史采集时间：2020-07-08 08:36:09", "联系人：", "与病人关系：夫妻", "病史叙述者：本人", "联系人地址：同上地址", "电话.", "可靠程度：可靠", "主诉：停经39周，要求住院待产。", "现病史：平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日（阳历），预产", "期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单活胎，发育符合", "孕周。孕早期无早孕反应，孕早期无腹痛、出血，阴道流液，出血史，无放射线、有害物质接", "触史。孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正常，孕中期行无创DNA", "结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正常，未行糖耐量筛", "查，未查B族链球菌。孕期经过顺利，孕晚期无头痛、头晕、眼花等症状，无皮肤黄染及痰", "痒。现停经39周，无腹痛，未见红及破水，遂入院要求住院待产，门诊以“足月妊娠、瘢痕子", "宫”收住院。自孕以来精神好，饮食、睡眠好，大小便正常，体重增加约10KG。", "既往史：患者平素体健；否认有“心脏病、高血压、糖尿病、肾病”等慢性病史，否认有", "“肝炎、结核”等传染性疾病。于2016.08行剖宫产手术，否认余手术及外伤史。否认有输血", "史，有献血史，否认食物及药物过敏史。预防接种随社会进行。", "个人史：出生于原籍，护士，本科文化，工作于三门峡市中心医院。否认长期外地居住", "史，无疫区居住史，无烟酒等不良嗜好。生长环境一般，否认有冶游史。", "婚育史：31岁结婚，爱人", "现年37岁，职员，工作于三门峡市党校，身体健康，无吸", "烟史，有饮酒史，否认“肝炎、结核”病史，夫妻感情好。孕;产;，2016年足月剖宫产1活男", "婴，现体健，否认产后出血及产褥感染史，否认不良孕产史。", "月经史：平素月经规律，12岁，5-7天/30-35天，末次月经为：2019年10月08日（阳", "历），量中等，色暗红，偶有血块，无痛经。", "页", "书写者签名：", "总第 页"]
2026-08-06 10:26:06,602 INFO     30 [qwen-vl-parser] page=6 text: 49 lines (bbox 728-776)
2026-08-06 10:26:06,602 INFO     30 [qwen-vl-parser] page=6 text: 49 sections
2026-08-06 10:26:06,895 INFO     30 [qwen-vl-table] coord API raw response (len=1292):
[
	{"text": "白细胞", "bbox": [111, 252, 160, 274]},
	{"text": "中性粒细胞百分比", "bbox": [111, 284, 245, 307]},
	{"text": "淋巴细胞百分比", "bbox": [111, 315, 227, 338]},
	{"text": "单核细胞百分比", "bbox": [111, 346, 227, 369]},
	{"text": "嗜酸性粒细胞百分比", "bbox": [111, 378, 262, 400]},
	{"text": "嗜碱性粒细胞百分比", "bbox": [111, 409, 262, 431]},
	{"text": "中性粒细胞计数", "bbox": [111, 440, 227, 462]},
	{"text": "淋巴细胞计数", "bbox": [111, 470, 211, 493]},
	{"text": "单核细胞计数", "bbox": [111, 501, 211, 524]},
	{"text": "嗜酸性粒细胞计数", "bbox": [111, 532, 245, 555]},
	{"text": "嗜碱性粒细胞计数", "bbox": [111, 563, 245, 586]},
	{"text": "红细胞", "bbox": [111, 594, 160, 617]},
	{"text": "血红蛋白", "bbox": [111, 625, 176, 648]},
	{"text": "红细胞压积", "bbox": [111, 656, 195, 679]},
	{"text": "红细胞平均体积", "bbox": [572, 256, 691, 279]},
	{"text": "平均血红蛋白量", "bbox": [572, 288, 691, 311]},
	{"text": "平均血红蛋白浓度", "bbox": [572, 320, 708, 343]},
	{"text": "红细胞分布宽度标准", "bbox": [572, 351, 724, 374]},
	{"text": "红细胞分布宽度变异", "bbox": [572, 382, 724, 405]},
	{"text": "血小板", "bbox": [572, 413, 623, 436]},
	{"text": "血小板分布宽度", "bbox": [572, 444, 691, 467]},
	{"text": "平均血小板体积", "bbox": [572, 475, 691, 498]},
	{"text": "血小板压积", "bbox": [572, 506, 657, 529]},
	{"text": "大型血小板比率", "bbox": [572, 537, 691, 560]},
	{"text": "大血小板数目", "bbox": [572, 568, 672, 591]}
]
2026-08-06 10:26:06,896 INFO     30 [qwen-vl-table] coord API: raw_items=25, valid_items=25, elapsed=16.4s
2026-08-06 10:26:06,896 INFO     30 [qwen-vl-table] coord item[0]: text=白细胞, bbox=[111, 252, 160, 274]
2026-08-06 10:26:06,896 INFO     30 [qwen-vl-table] coord item[1]: text=中性粒细胞百分比, bbox=[111, 284, 245, 307]
2026-08-06 10:26:06,896 INFO     30 [qwen-vl-table] coord item[2]: text=淋巴细胞百分比, bbox=[111, 315, 227, 338]
2026-08-06 10:26:06,896 INFO     30 [qwen-vl-table] coord item[3]: text=单核细胞百分比, bbox=[111, 346, 227, 369]
2026-08-06 10:26:06,896 INFO     30 [qwen-vl-table] coord item[4]: text=嗜酸性粒细胞百分比, bbox=[111, 378, 262, 400]
2026-08-06 10:26:06,896 INFO     30 [qwen-vl-table] coord item[5]: text=嗜碱性粒细胞百分比, bbox=[111, 409, 262, 431]
2026-08-06 10:26:06,896 INFO     30 [qwen-vl-table] coord item[6]: text=中性粒细胞计数, bbox=[111, 440, 227, 462]
2026-08-06 10:26:06,896 INFO     30 [qwen-vl-table] coord item[7]: text=淋巴细胞计数, bbox=[111, 470, 211, 493]
2026-08-06 10:26:06,896 INFO     30 [qwen-vl-table] coord item[8]: text=单核细胞计数, bbox=[111, 501, 211, 524]
2026-08-06 10:26:06,896 INFO     30 [qwen-vl-table] coord item[9]: text=嗜酸性粒细胞计数, bbox=[111, 532, 245, 555]
2026-08-06 10:26:06,896 INFO     30 [qwen-vl-table] coord item[10]: text=嗜碱性粒细胞计数, bbox=[111, 563, 245, 586]
2026-08-06 10:26:06,896 INFO     30 [qwen-vl-table] coord item[11]: text=红细胞, bbox=[111, 594, 160, 617]
2026-08-06 10:26:06,896 INFO     30 [qwen-vl-table] coord item[12]: text=血红蛋白, bbox=[111, 625, 176, 648]
2026-08-06 10:26:06,896 INFO     30 [qwen-vl-table] coord item[13]: text=红细胞压积, bbox=[111, 656, 195, 679]
2026-08-06 10:26:06,897 INFO     30 [qwen-vl-table] coord item[14]: text=红细胞平均体积, bbox=[572, 256, 691, 279]
2026-08-06 10:26:06,897 INFO     30 [qwen-vl-table] coord item[15]: text=平均血红蛋白量, bbox=[572, 288, 691, 311]
2026-08-06 10:26:06,897 INFO     30 [qwen-vl-table] coord item[16]: text=平均血红蛋白浓度, bbox=[572, 320, 708, 343]
2026-08-06 10:26:06,897 INFO     30 [qwen-vl-table] coord item[17]: text=红细胞分布宽度标准, bbox=[572, 351, 724, 374]
2026-08-06 10:26:06,897 INFO     30 [qwen-vl-table] coord item[18]: text=红细胞分布宽度变异, bbox=[572, 382, 724, 405]
2026-08-06 10:26:06,897 INFO     30 [qwen-vl-table] coord item[19]: text=血小板, bbox=[572, 413, 623, 436]
2026-08-06 10:26:06,897 INFO     30 [qwen-vl-table] coord item[20]: text=血小板分布宽度, bbox=[572, 444, 691, 467]
2026-08-06 10:26:06,897 INFO     30 [qwen-vl-table] coord item[21]: text=平均血小板体积, bbox=[572, 475, 691, 498]
2026-08-06 10:26:06,897 INFO     30 [qwen-vl-table] coord item[22]: text=血小板压积, bbox=[572, 506, 657, 529]
2026-08-06 10:26:06,897 INFO     30 [qwen-vl-table] coord item[23]: text=大型血小板比率, bbox=[572, 537, 691, 560]
2026-08-06 10:26:06,897 INFO     30 [qwen-vl-table] coord item[24]: text=大血小板数目, bbox=[572, 568, 672, 591]
2026-08-06 10:26:06,899 INFO     30 [qwen-vl-table] page=11 coord: matched 25/25, time=16.4s
2026-08-06 10:26:06,899 INFO     30 [qwen-vl-table] new_positions (25):
[[12, 174.49200000000002, 251.52, 278.208, 302.49600000000004], [12, 174.49200000000002, 385.14000000000004, 313.536, 338.92800000000005], [12, 174.49200000000002, 356.844, 347.76000000000005, 373.15200000000004], [12, 174.49200000000002, 356.844, 381.98400000000004, 407.37600000000003], [12, 174.49200000000002, 411.86400000000003, 417.312, 441.6], [12, 174.49200000000002, 411.86400000000003, 451.53600000000006, 475.824], [12, 174.49200000000002, 356.844, 485.76000000000005, 510.04800000000006], [12, 174.49200000000002, 331.692, 518.88, 544.272], [12, 174.49200000000002, 331.692, 553.104, 578.4960000000001], [12, 174.49200000000002, 385.14000000000004, 587.3280000000001, 612.72], [12, 174.49200000000002, 385.14000000000004, 621.552, 646.9440000000001], [12, 174.49200000000002, 251.52, 655.7760000000001, 681.168], [12, 174.49200000000002, 276.672, 690.0000000000001, 715.392], [12, 174.49200000000002, 306.54, 724.224, 749.6160000000001], [12, 899.1840000000001, 1086.252, 282.624, 308.016], [12, 899.1840000000001, 1086.252, 317.952, 343.34400000000005], [12, 899.1840000000001, 1112.976, 353.28000000000003, 378.672], [12, 899.1840000000001, 1138.1280000000002, 387.504, 412.896], [12, 899.1840000000001, 1138.1280000000002, 421.728, 447.12000000000006], [12, 899.1840000000001, 979.356, 455.95200000000006, 481.34400000000005], [12, 899.1840000000001, 1086.252, 490.17600000000004, 515.5680000000001], [12, 899.1840000000001, 1086.252, 524.4000000000001, 549.792], [12, 899.1840000000001, 1032.804, 558.624, 584.0160000000001], [12, 899.1840000000001, 1086.252, 592.8480000000001, 618.24], [12, 899.1840000000001, 1056.384, 627.072, 652.464]]
2026-08-06 10:26:06,899 INFO     30 [qwen-vl-table] ═══ DONE ═══ items=25, matched=25, pages=1, time=32.3s
2026-08-06 10:26:06,918 INFO     30 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-06 10:26:06,918 INFO     30 [Trace] task=6a97f83c | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | Extractor:LabExam | outputs={"chunks": "3 items, types={'LabReport': 3}", "html": "", "json": "309 items", "markdown": "", "text": "", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 5, \"chunks_LabExam\": 3}"}
2026-08-06 10:26:06,919 INFO     30 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-06 10:26:06,921 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:26:06.919+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 8, "lag": 0, "done": 0, "failed": 0, "current": {"6a97f83c918011f18dbe1f8f96f1c395": {"id": "6a97f83c918011f18dbe1f8f96f1c395", "doc_id": "688aee0a918011f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909798, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011615561, "task_type": "dataflow", "root_trace_id": "d05a3d8d0d6c4aa38394753a3ea0008c", "root_traceparent": "00-d05a3d8d0d6c4aa38394753a3ea0008c-2c380740bfb060e1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "00b9d592918111f18dbe1f8f96f1c395": {"id": "00b9d592918111f18dbe1f8f96f1c395", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011867426, "task_type": "dataflow", "root_trace_id": "1ab3198c92574fb4b2701d0f5db7322f", "root_traceparent": "00-1ab3198c92574fb4b2701d0f5db7322f-bdaff6f64a5f4a64-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:26:06,948 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:26:06,948 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-06 10:26:07,071 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1364661, prompt_len=764
2026-08-06 10:26:07,595 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:26:07,620 INFO     30 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-06 10:26:07,621 INFO     30 [Trace] task=6a97f83c | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "309 items", "markdown": "", "text": "", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 5, \"chunks_LabExam\": 3}"}
2026-08-06 10:26:07,621 INFO     30 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-06 10:26:07,646 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:26:07,647 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-06 10:26:08,274 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:26:08,301 INFO     30 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-06 10:26:08,302 INFO     30 [Trace] task=6a97f83c | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | Extractor:Clinical | outputs={"chunks": "1 items", "html": "", "json": "309 items", "markdown": "", "text": "", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 5, \"chunks_LabExam\": 3}"}
2026-08-06 10:26:08,303 INFO     30 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-06 10:26:08,327 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:26:08,328 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-06 10:26:08,956 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:26:08,957 INFO     30 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-06 10:26:08,992 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1364661, prompt_len=401
2026-08-06 10:26:09,095 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:26:09,126 INFO     30 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-06 10:26:09,127 INFO     30 [Trace] task=6a97f83c | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "309 items", "markdown": "", "text": "", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 5, \"chunks_LabExam\": 3}"}
2026-08-06 10:26:09,128 INFO     30 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-06 10:26:09,156 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:26:09,157 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-06 10:26:10,133 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:26:10,151 INFO     30 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-06 10:26:10,152 INFO     30 [Trace] task=6a97f83c | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "309 items", "markdown": "", "text": "", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 5, \"chunks_LabExam\": 3}"}
2026-08-06 10:26:10,152 INFO     30 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-06 10:26:10,170 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:26:10,171 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-06 10:26:12,759 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:26:12,784 INFO     30 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-06 10:26:12,786 INFO     30 [Trace] task=6a97f83c | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "309 items", "markdown": "", "text": "", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 5, \"chunks_LabExam\": 3}"}
2026-08-06 10:26:12,786 INFO     30 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-06 10:26:12,836 INFO     30 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 10:26:12,837 INFO     30 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-06 10:26:12,838 INFO     30 [qwen-vl-text] positions(87): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 10:26:12,839 INFO     30 [qwen-vl-text] page grouping: [0, 1, 2, 3], lines per page: [7, 28, 1, 51]
2026-08-06 10:26:14,000 INFO     30 [qwen-vl-text] page=0, rect=2259x1732, img=(6276x4812), dpi=200
2026-08-06 10:26:16,524 INFO     30 [qwen-vl-parser] text API response (len=934):
["院", "入院记录", "姓名：", "科室：产科二区", "床号：", "生。", "家族史：父母亲体健，1弟1妹均体健，1子体健。否认家族中有遗传性及传染性疾病史。", "体格检查", "体温：36.5℃", "脉搏：78次/分", "呼吸：18次/分", "血压：98/64mmHg", "身高160cm", "体重：60Kg", "一般状况：发育正常；营养中等；自动体位：面色红润；面容及表情自如；神志清晰；言", "语状态流利；检查时能合作等。", "皮肤：色泽正常，弹性正常，无水肿、出汗、紫癜、皮疹、色素沉着、蜘蛛痣、瘢痕、创", "伤、溃疡、结节。", "淋巴结：全身或局部表浅淋巴结未触及肿大；局部皮肤无红热、瘘管、瘢痕。", "头部：", "头颅：大小无异常、外形无异常；眉发分布正常；无疖、痈、外伤、瘢痕、肿块。", "眼部：双眼裂正常，双眼睑无水肿，眼球运动正常。瞳孔：左3.0mm 直接对光反应灵敏，", "间接对光反应灵敏；右3.0mm 直接对光反应灵敏，间接对光反应灵敏。视力粗测正常。", "耳部：耳廓无畸形，外耳道无分泌物，乳突无压痛，听力粗测5米。", "鼻部：无畸形、鼻翼扇动、阻塞、分泌物、鼻中隔异常、嗅觉障碍、鼻窦压痛等。", "口腔：口唇红润，无畸形、疱疹、微血管搏动、口角皲裂；牙齿无缺损、龋病、镶补等异", "常；牙龈无溢血、溢脓、萎缩、色素沉着；口腔粘膜无溃疡、假膜、色素沉着；扁桃体无肿", "大、分泌物；咽部无充血、分泌物。", "颈部：对称，无强直、压痛、运动受限、颈静脉怒张、颈动脉明显搏动、肿块，气管居", "中，甲状腺无肿大。", "胸部", "胸廓：形状正常，对称，运动程度正常，肋间正常，胸壁无水肿、皮下气肿、肿块、静脉", "曲张，肋骨及肋软骨无压痛、凹陷等异常。乳头，正常。", "肺脏：视诊：腹式呼吸，呼吸节律正常，呼吸深度正常，两侧呼吸运动对称。", "触诊：语音震颤两侧相等，无摩擦感。", "叩诊：叩诊声响清音，肺下界肩胛线在第10肋间，呼吸移动度6cm，", "听诊：呼吸音性质为肺泡呼吸音，强度正常，语音传导正常，无摩擦音、哮鸣音、", "第页", "书写者签名：", "总第页"]
2026-08-06 10:26:16,525 INFO     30 [qwen-vl-parser] page=7 text: 40 lines (bbox 777-816)
2026-08-06 10:26:16,533 INFO     30 [qwen-vl-parser] page=7 text: 40 sections
2026-08-06 10:26:16,535 INFO     30 [qwen-vl-text] page=1, rect=2260x1732, img=(6278x4812), dpi=200
2026-08-06 10:26:18,359 INFO     30 [qwen-vl-text] page=2, rect=2196x1384, img=(6100x3845), dpi=200
2026-08-06 10:26:20,720 INFO     30 [qwen-vl-text] page=3, rect=2220x1532, img=(6167x4256), dpi=200
2026-08-06 10:26:20,728 INFO     30 [qwen-vl-text] LLM extraction start, text_len=2906
2026-08-06 10:26:20,729 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:26:20,729 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 0, \"bbox_end\": 86, \"encounter_dates\": [\"2026-03-23\"], \"department\": \"日间化疗中心[东院区]\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "2025.1 确诊小细胞癌，已行免疫组化协诊\n2025-.2-4给予\" EP\" 化疗联合\" 特瑞普利单抗\" 免疫治疗3周期，\n2025-04-22给予\" EP\" 方案化疗联合\n\" 替雷利珠单抗\" 免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗\n2025.5-8 行\" 特瑞普利单抗\" 免疫治疗4周期\n2025.8 PD\n2025.8-2026.2 \" 替雷利珠单抗联合安罗替尼\" 免疫治疗\n1804 - Internet Explorer\n诊疗与病历 申请单 手术管理 医嘱单 会诊管理 重症管理 需关注医嘱 病情总览 质量管理 更多\n汤光冉 住院医师\n日间化疗中心[东院区]\n住院天数: 1 费别: 全国医保居民 余额: 0.00 诊断: 肺恶性肿瘤,恶性肿瘤... 医疗救助类型: 农村低保\n病人列表 全息视图\n操作 编辑 功能 表格 其他\n保存 打印 自动续打 预览 单独打印 手工解锁 隐藏留痕 病历参考 更新数据 首页\n信阳市中心医院\n日间化疗出入院记录\n姓名: 性别:女年龄:65岁 科别:日间化疗中心[东院床号:04 登记号:0000 住院号:25\n区]\n入院时间: 2026年03月23日 08:29:00出院时间: 2026年03月23日 11:14:00 住院天数: 1天\n主诉: 确诊肺癌1年余\n入院情况: 1年余前因“胸闷”就诊我院, 2025-01-17CT增强64: 1.右肺门占位, 考虑恶性病变并\n右肺中下叶不张, 右下肺动受侵可能。2. 双肺纤维索条灶。双肺多发小结节, 转移待排。3.右侧\n胸腔少量积液。4.双肾小囊肿。5.升结肠多发憩室。6.子宫后壁肌瘤可能。7.冠状动脉CTA未见明\n显异常。2025-01-23行纤支镜下肺活检, 2025-01-23 活体组织病理申请 诊断意见: (右中间段支\n气管)考虑小细胞癌, 已行免疫组化协诊。2025-01-26 免疫组化申请: CK广谱 (点+), CD56 (+),\nSyn (+), INSM1 (+), CK5/6 (-), P40 (-), TTF1 (+), NapsinA (-), Ki-67 (80%+)。结合HE\n及免疫组化结果, (右中间段支气管)肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04\n-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期, 2025-04-22给予“EP”方案化疗联合\n“替雷利珠单抗”免疫治疗1周期, 化疗后呕吐反应较重, 予以对症支持治疗。2025-05-19、2025\n-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加增强\n(胸部,上腹部,下腹部) 诊断意见: 1. 右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节。\n100%\n16:56\n2026/3/23\n胸腔少量积液。4.双肾小囊肿。5.升结肠多发息室。6.丁台加壁肌瘤可能。冠状动脉CT示无明显异常。2025-01-23行纤支镜下肺活检，2025-01-23活体组织病理申请 诊断意见：(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。2025-01-26免疫组化申请：CK广谱(点+)，CD56(+)，Syn(+)，INSM1(+)，CK5/6(-)，P40(-)，TTF1(+),NapsinA(-)，Ki-67(80%+)。结合HE及免疫组化结果，(右中间段支气管)肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期，2025-04-22给予“EP”方案化疗联合“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗。2025-05-19、2025-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加强(胸部，上腹部，下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节，转移瘤可能；建议追踪复查。2.双肺慢性炎症，右肺中叶局限性支扩，双侧胸腔少量积液。3.脾脏低密度灶，建议追踪复查。4.胆囊可疑小结石。升结肠多发憩室。5.双肾小囊肿。与2025-05-18日片比较：右肺中叶局限性支扩，右肺下叶内基底段结节较前增大，右肺门淋巴结较前增大。考虑病情进展，于2025-08-23给予“安罗替尼12mg”联合“替雷利珠单抗”抗肿瘤治疗1周期。后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-22、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重无明显变化。诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利，予办理出院手续。\n国家医保编码：D411502011804 - Internet Explorer\n美系统) 修改患者信息 诊疗与病历 申请单 手术管理 医嘱单 会诊管理 重症管理 需关注医嘱 病情总览 质量管理 更多\n汤光冉 住院医师\n日间化疗中心[东院区]\n0000 床号: 04 住院天数: 1 费别: 全国医保居民 余额: 0.00 诊断: 肺恶性肿瘤,恶性肿瘤... 医疗救助类型: 农村低保\n病人列表 全息视图\n(1) ×\n操作 编辑 功能 表格 其他\n历\n保存 打印 自动续打 预览 单独打印 手工解锁 隐藏留痕 病历参考 更新数据 首页\n记录\n1:09:45 曾庆星\n医师审核\n录单\n1:10:52 曾庆星\n医师审核\n录单\n1:11:53 曾庆星\n医师审核\n11:12:02 曾庆星\n医师审核\n单(日间...\n11:13:02 曾庆星\n医师审核\n已打印\n11:15:03 曾庆星\n医师审核\n评估表\n16:30:58 曾庆星\n院医师审核\n/TE风险评...\n16:32:44 曾庆星\n院医师审核\n后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-2\n2、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我\n院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重\n无明显变化。\n诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利\n，予办理出院手续。\n出院情况：患者未诉不适，神志清，精神可，生命体征平稳。\n出院诊断：\n1.恶性肿瘤免疫治疗\n2.肺恶性肿瘤小细胞肺癌IV期\n3.肺继发恶性肿瘤\n4.冠状动脉粥样硬化性心脏病\n5.胸腔积液\n6.心包积液\n7.肺部感染\n8.腔隙性脑梗死\n9.肾功能检查的异常结果\n1",
    "role": "user"
  }
]
2026-08-06 10:26:21,123 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1258831, prompt_len=764
2026-08-06 10:26:22,657 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:26:22,658 INFO     30 [qwen-vl-parser] page=8 classify=text report_date=None
2026-08-06 10:26:22,720 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1258831, prompt_len=401
2026-08-06 10:26:28,095 INFO     30 [qwen-vl-parser] text API response (len=817):
["院", "入院记录", "姓名：", "科室：产科二区", "床号", "病号：", "干啰音、湿啰音。", "心脏：视诊：心尖搏动的位置在左侧锁骨中线内第4肋间，范围为2.5cm，强度正常，心前", "区无异常搏动、局限性膨隆。", "触诊：心尖搏动最强部位在左侧锁骨中线第4肋间，范围为2.5cm，无抬举性搏动、", "震颤、摩擦感。", "叩诊：左右心界线以每肋间距胸骨中线的cm数记载。", "右cm", "肋间", "左cm", "2", "Ⅱ", "2.5", "2", "Ⅲ", "4", "3", "Ⅳ", "5.5", "V", "8", "左锁骨中线至前正中线的距离9cm。", "听诊：心率78次/分，心律整齐，无心脏杂音，无第三心音、第四心音、心音分", "裂，P2<A2。", "血管：桡动脉搏动正常，血管壁硬度正常。", "周围血管征：无毛细血管搏动征、水冲脉、枪击音、动脉异常搏动。", "腹部：", "视诊：腹部膨隆，晓孕腹型，腹壁对称，无凹陷、膨隆、静脉曲张、蠕动波、局限性隆", "起，下腹可见一长约15cm横行手术疤痕。", "触诊：腹壁柔软，无压痛，无反跳痛；未触及肿块，无搏动、波动感等。肝脏：肋缘下未", "触及，无压痛。胆囊：未触及，无压痛。脾脏：肋缘下未触及。肾：未触及，无压痛等。", "叩诊：肝上界位于第5肋间，肝浊音界正常，肝区无叩击痛、脾区无叩击痛、腹部无过度", "鼓音，移动性浊音阴性。", "听诊：肠蠕动音正常，频率4次/分，胃区无振水声，肝区无摩擦音、脾区无摩擦音，无血", "管杂音。", "外阴及肛门：阴毛分布正常；外生殖器发育正常，肛门检查：无外痔、肛裂、肛瘘、脱", "肛、湿疣等。", "脊柱：脊柱无畸形、压痛、叩击痛；脊柱两侧肌肉无紧张、压痛；肋脊角无压痛、叩痛。", "四肢：无畸形、杵状指（趾）、静脉曲张、外伤、骨折；肌肉张力正常与肌力5级，无萎"]
2026-08-06 10:26:28,096 INFO     30 [qwen-vl-parser] page=8 text: 44 lines (bbox 817-860)
2026-08-06 10:26:28,097 INFO     30 [qwen-vl-parser] page=8 text: 44 sections
2026-08-06 10:26:28,320 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=640502, prompt_len=764
2026-08-06 10:26:29,573 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:26:29,573 INFO     30 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-06 10:26:29,593 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=640502, prompt_len=401
2026-08-06 10:26:32,817 INFO     30 [qwen-vl-parser] text API response (len=428):
["院", "入院记录", "姓名.", "科室:产科二区", "床号", "住院号.", "缩;关节无红肿、畸形、运动障碍,双下肢水肿。", "神经反射:膝腱反射正常、跟腱反射正常、肱二头肌腱反射正常、肱三头肌腱反射正常、", "腹壁反射正常、巴彬斯基征阴性、克尼格征阴性等。", "专科情况", "宫高34CM,腹围102CM,估计胎儿体重:3200g,胎位:头位,胎心152次/分,律齐,无", "宫缩,未见红,未破水,骨盆外测量及内诊:未做。", "辅助检查", "B超(2020.07.02 本院):晓孕宫内单活胎头位(双顶径9.4cm,股骨长7.0cm羊水指", "数8.5cm),胎盘成熟度II°.", "初步诊断:", "1.妊娠合并子宫瘢痕;", "3.孕2产,宫内孕39周头位待产。", "主治医师:", "孙小丹", "副主任医师:", "彭琼玉", "2020.07.08", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-06 10:26:32,819 INFO     30 [qwen-vl-parser] page=9 text: 25 lines (bbox 861-885)
2026-08-06 10:26:32,820 INFO     30 [qwen-vl-parser] page=9 text: 25 sections
2026-08-06 10:26:33,442 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1627445, prompt_len=764
2026-08-06 10:26:35,094 INFO     30 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-06 10:26:35,095 INFO     30 [qwen-vl-parser] page=10 classify=text report_date=None
2026-08-06 10:26:35,130 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1627445, prompt_len=401
2026-08-06 10:26:37,546 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:26:37.542+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 8, "lag": 0, "done": 0, "failed": 0, "current": {"6a97f83c918011f18dbe1f8f96f1c395": {"id": "6a97f83c918011f18dbe1f8f96f1c395", "doc_id": "688aee0a918011f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909798, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011615561, "task_type": "dataflow", "root_trace_id": "d05a3d8d0d6c4aa38394753a3ea0008c", "root_traceparent": "00-d05a3d8d0d6c4aa38394753a3ea0008c-2c380740bfb060e1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "00b9d592918111f18dbe1f8f96f1c395": {"id": "00b9d592918111f18dbe1f8f96f1c395", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011867426, "task_type": "dataflow", "root_trace_id": "1ab3198c92574fb4b2701d0f5db7322f", "root_traceparent": "00-1ab3198c92574fb4b2701d0f5db7322f-bdaff6f64a5f4a64-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:26:42,969 INFO     30 [qwen-vl-parser] text API response (len=1235):
["姓名：", "科室：产科二区", "床号", "住院号.", "2020年07月08日 09时22分", "首次病程记录", "患", "女，36岁，汉族，-以“停经39周，要求住院待产”为主诉于", "2020-07-08 08:36:09入院。一、病例特点：1、已婚育龄妇女，孕₂产₁，否认产后出血及产褥", "感染史，否认不良孕产史；2、平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日", "(阳历)，预产期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单", "活胎，发育符合孕周。3、孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正", "常，孕中期行无创DNA结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正", "常，未行糖耐量筛查，未查B族链球菌。4、现停经39周，无腹痛，未见红及破水，遂入院要求", "住院待产。5.入院查体：T：36.5℃，P：78次/分，R：18次/分，BP：98/64mmHg。神志清楚，", "精神好，全身皮肤黏膜无黄染，浅表淋巴结未触及，心肺听诊未闻及明显异常，腹膨隆。6、", "专科检查：宫高34CM，腹围102CM，估计胎儿体重：3200g，胎位：头位，胎心152次/分，律", "齐，无宫缩，未见红，未破水，骨盆外测量及内诊：未做。7、辅助检查：B超（2020.07.02", "本院）：晚孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度", "II°。二、拟诊讨论：（一）初步诊断：1.妊娠合并子宫瘢痕；2.孕₂产；宫内孕39周头位", "待产。（二）诊断依据：1、患者有停经史，平素月经规律，平素月经规律，5-7天/35-36天，", "末次月经为：2019年10月08日（阳历），预产期为2020年07月15日（阳历），停经后有自觉胎", "动，产前检查可同及胎心；2、专科检查：宫高34CM，腹围102CM，估计胎儿体重：3200g，胎", "位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水。骨盆外测量及内诊：未做。3、", "辅助检查：B超（2020.07.02本院）：晚孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm", "羊水指数8.5cm)，胎盘成熟度II°。（三）鉴别诊断：根据据病史、查体及辅助检查，目前诊", "断明确。三、诊疗计划：完善各项检查：心电图、彩超、血常规、血型、凝血五项、输血前检", "查、尿常规、心电图、肝功、肾功、血糖、电解质等；2、向患者及家属交代病情，围生期相", "关危险因素；3、给予巡视病房、监测胎心、心理疏导，消除围产期恐惧心理等产前护理；4、", "患者要求明日剖宫产，纳入剖宫产临床路径。", "主治医师：孙州", "2020年07月08日 10时22分", "科主任宋瑞香主治医师查房记录", "第页", "总第页"]
2026-08-06 10:26:42,971 INFO     30 [qwen-vl-parser] page=10 text: 35 lines (bbox 886-920)
2026-08-06 10:26:42,971 INFO     30 [qwen-vl-parser] page=10 text: 35 sections
2026-08-06 10:26:43,493 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1704714, prompt_len=764
2026-08-06 10:26:43,843 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:26:43,844 INFO     30 [qwen-vl-text] LLM output (len=4470):
{
  "encounter_date": "2026-03-23",
  "dm_name": null,
  "dm_gender": "女",
  "dm_age": 65,
  "dm_ethnicity": null,
  "dm_marital_status": null,
  "dm_occupation": null,
  "dm_admission_time": "2026-03-23 08:29",
  "dm_record_time": "2026-03-23 16:32",
  "dm_history_provider": null,
  "cc_text": "确诊肺癌1年余",
  "cc_main_symptoms": [
    "确诊肺癌"
  ],
  "cc_duration": "1年余",
  "pi_text": "1年余前因“胸闷”就诊我院, 2025-01-17CT增强64: 1.右肺门占位, 考虑恶性病变并右肺中下叶不张, 右下肺动受侵可能。2. 双肺纤维索条灶。双肺多发小结节, 转移待排。3.右侧胸腔少量积液。4.双肾小囊肿。5.升结肠多发憩室。6.子宫后壁肌瘤可能。7.冠状动脉CTA未见明显异常。2025-01-23行纤支镜下肺活检, 2025-01-23 活体组织病理申请 诊断意见: (右中间段支气管)考虑小细胞癌, 已行免疫组化协诊。2025-01-26 免疫组化申请: CK广谱 (点+), CD56 (+), Syn (+), INSM1 (+), CK5/6 (-), P40 (-), TTF1 (+), NapsinA (-), Ki-67 (80%+)。结合HE及免疫组化结果, (右中间段支气管)肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期, 2025-04-22给予“EP”方案化疗联合“替雷利珠单抗”免疫治疗1周期, 化疗后呕吐反应较重, 予以对症支持治疗。2025-05-19、2025-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加增强(胸部,上腹部,下腹部) 诊断意见: 1. 右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节。胸腔少量积液。4.双肾小囊肿。5.升结肠多发息室。6.丁台加壁肌瘤可能。冠状动脉CT示无明显异常。2025-01-23行纤支镜下肺活检，2025-01-23活体组织病理申请 诊断意见：(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。2025-01-26免疫组化申请：CK广谱(点+)，CD56(+)，Syn(+)，INSM1(+)，CK5/6(-)，P40(-)，TTF1(+),NapsinA(-)，Ki-67(80%+)。结合HE及免疫组化结果，(右中间段支气管)肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期，2025-04-22给予“EP”方案化疗联合“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗。2025-05-19、2025-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加强(胸部，上腹部，下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节，转移瘤可能；建议追踪复查。2.双肺慢性炎症，右肺中叶局限性支扩，双侧胸腔少量积液。3.脾脏低密度灶，建议追踪复查。4.胆囊可疑小结石。升结肠多发憩室。5.双肾小囊肿。与2025-05-18日片比较：右肺中叶局限性支扩，右肺下叶内基底段结节较前增大，右肺门淋巴结较前增大。考虑病情进展，于2025-08-23给予“安罗替尼12mg”联合“替雷利珠单抗”抗肿瘤治疗1周期。后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-22、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重无明显变化。诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利，予办理出院手续。",
  "pmh_disease_history": [
    "冠状动脉粥样硬化性心脏病",
    "腔隙性脑梗死",
    "肾功能检查的异常结果"
  ],
  "pmh_allergy_history": [],
  "pmh_surgery_trauma_history": [],
  "ph_smoking": null,
  "ph_drinking": null,
  "oh_menarche_age": null,
  "oh_menopause_age": null,
  "oh_pregnancies": null,
  "fh_text": null,
  "fh_hereditary_diseases": [],
  "vs_temperature_c": null,
  "vs_pulse_bpm": null,
  "vs_respiration_rpm": null,
  "vs_systolic_bp_mmhg": null,
  "vs_diastolic_bp_mmhg": null,
  "pe_general_condition": "神志清，精神可，饮食、睡眠可，大小便可，体重无明显变化",
  "pe_skin_mucosa": null,
  "pe_lymph_nodes": null,
  "pe_lungs": null,
  "pe_heart": null,
  "pe_abdomen": null,
  "pe_extremities": null,
  "pe_nervous_system": null,
  "pe_specialist_exam": null,
  "pe_ecog_score": null,
  "pat_text": "2025-01-17CT增强64: 1.右肺门占位, 考虑恶性病变并右肺中下叶不张, 右下肺动受侵可能。2. 双肺纤维索条灶。双肺多发小结节, 转移待排。3.右侧胸腔少量积液。4.双肾小囊肿。5.升结肠多发憩室。6.子宫后壁肌瘤可能。7.冠状动脉CTA未见明显异常。2025-01-23 活体组织病理申请 诊断意见: (右中间段支气管)考虑小细胞癌。2025-01-26 免疫组化申请: CK广谱 (点+), CD56 (+), Syn (+), INSM1 (+), CK5/6 (-), P40 (-), TTF1 (+), NapsinA (-), Ki-67 (80%+)。2025-08-21CT平扫加增强(胸部,上腹部,下腹部) 诊断意见: 1. 右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节，转移瘤可能。2.双肺慢性炎症，右肺中叶局限性支扩，双侧胸腔少量积液。3.脾脏低密度灶。4.胆囊可疑小结石。升结肠多发憩室。5.双肾小囊肿。",
  "pat_items": [
    "2025-01-17CT增强64: 1.右肺门占位, 考虑恶性病变并右肺中下叶不张, 右下肺动受侵可能。2. 双肺纤维索条灶。双肺多发小结节, 转移待排。3.右侧胸腔少量积液。4.双肾小囊肿。5.升结肠多发憩室。6.子宫后壁肌瘤可能。7.冠状动脉CTA未见明显异常。",
    "2025-01-23 活体组织病理申请 诊断意见: (右中间段支气管)考虑小细胞癌",
    "2025-01-26 免疫组化申请: CK广谱 (点+), CD56 (+), Syn (+), INSM1 (+), CK5/6 (-), P40 (-), TTF1 (+), NapsinA (-), Ki-67 (80%+)",
    "2025-08-21CT平扫加增强(胸部,上腹部,下腹部) 诊断意见: 1. 右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节，转移瘤可能。2.双肺慢性炎症，右肺中叶局限性支扩，双侧胸腔少量积液。3.脾脏低密度灶。4.胆囊可疑小结石。升结肠多发憩室。5.双肾小囊肿。"
  ],
  "preliminary_diagnoses": [
    {
      "name": "恶性肿瘤免疫治疗",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "肺恶性肿瘤小细胞肺癌IV期",
      "diagnosis_type": "西医",
      "is_primary": true
    },
    {
      "name": "肺继发恶性肿瘤",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "冠状动脉粥样硬化性心脏病",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "胸腔积液",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "心包积液",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "肺部感染",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "腔隙性脑梗死",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "肾功能检查的异常结果",
      "diagnosis_type": "西医",
      "is_primary": false
    }
  ],
  "department": "日间化疗中心[东院区]"
}
2026-08-06 10:26:43,845 INFO     30 [qwen-vl-text] Updated encounter_dates=[2026-03-23]
2026-08-06 10:26:43,848 INFO     30 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=449344, prompt_len=842
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共7行）
["2025.1 确诊小细胞癌，已行免疫组化协诊", "2025-.2-4给予\" EP\" 化疗联合\" 特瑞普利单抗\" 免疫治疗3周期，", "2025-04-22给予\" EP\" 方案化疗联合", "\" 替雷利珠单抗\" 免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗", "2025.5-8 行\" 特瑞普利单抗\" 免疫治疗4周期", "2025.8 PD", "2025.8-2026.2 \" 替雷利珠单抗联合安罗替尼\" 免疫治疗"]

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
2026-08-06 10:26:44,999 INFO     30 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-06 10:26:45,000 INFO     30 [qwen-vl-parser] page=11 classify=text report_date=None
2026-08-06 10:26:45,030 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1704714, prompt_len=401
2026-08-06 10:26:55,094 INFO     30 [qwen-vl-text] coord API raw response (len=520):
[
	{"text": "2025.1 确诊小细胞癌，已行免疫组化协诊", "bbox": [173, 302, 323, 313]},
	{"text": "2025-.2-4给予\" EP\" 化疗联合\" 特瑞普利单抗\" 免疫治疗3周期，", "bbox": [173, 313, 404, 324]},
	{"text": "2025-04-22给予\" EP\" 方案化疗联合", "bbox": [173, 324, 303, 335]},
	{"text": "\" 替雷利珠单抗\" 免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗", "bbox": [173, 335, 442, 346]},
	{"text": "2025.5-8 行\" 特瑞普利单抗\" 免疫治疗4周期", "bbox": [173, 346, 335, 357]},
	{"text": "2025.8 PD", "bbox": [173, 357, 210, 367]},
	{"text": "2025.8-2026.2 \" 替雷利珠单抗联合安罗替尼\" 免疫治疗", "bbox": [173, 367, 374, 378]}
]
2026-08-06 10:26:55,096 INFO     30 [qwen-vl-text] coord API: raw_items=7, valid_items=7, elapsed=11.2s
2026-08-06 10:26:55,096 INFO     30 [qwen-vl-text] coord item[0]: text=2025.1 确诊小细胞癌，已行免疫组化协诊, bbox=[173, 302, 323, 313]
2026-08-06 10:26:55,097 INFO     30 [qwen-vl-text] coord item[1]: text=2025-.2-4给予" EP" 化疗联合" 特瑞普利单抗" 免疫治疗3周期，, bbox=[173, 313, 404, 324]
2026-08-06 10:26:55,097 INFO     30 [qwen-vl-text] coord item[2]: text=2025-04-22给予" EP" 方案化疗联合, bbox=[173, 324, 303, 335]
2026-08-06 10:26:55,097 INFO     30 [qwen-vl-text] coord item[3]: text=" 替雷利珠单抗" 免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗, bbox=[173, 335, 442, 346]
2026-08-06 10:26:55,098 INFO     30 [qwen-vl-text] coord item[4]: text=2025.5-8 行" 特瑞普利单抗" 免疫治疗4周期, bbox=[173, 346, 335, 357]
2026-08-06 10:26:55,098 INFO     30 [qwen-vl-text] coord item[5]: text=2025.8 PD, bbox=[173, 357, 210, 367]
2026-08-06 10:26:55,098 INFO     30 [qwen-vl-text] coord item[6]: text=2025.8-2026.2 " 替雷利珠单抗联合安罗替尼" 免疫治疗, bbox=[173, 367, 374, 378]
2026-08-06 10:26:55,099 INFO     30 [qwen-vl-text] page=0 — 7/7 coords, api_time=11.2s
2026-08-06 10:26:55,208 INFO     30 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=10857823, prompt_len=1708
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共28行）
["1804 - Internet Explorer", "诊疗与病历 申请单 手术管理 医嘱单 会诊管理 重症管理 需关注医嘱 病情总览 质量管理 更多", "汤光冉 住院医师", "日间化疗中心[东院区]", "住院天数: 1 费别: 全国医保居民 余额: 0.00 诊断: 肺恶性肿瘤,恶性肿瘤... 医疗救助类型: 农村低保", "病人列表 全息视图", "操作 编辑 功能 表格 其他", "保存 打印 自动续打 预览 单独打印 手工解锁 隐藏留痕 病历参考 更新数据 首页", "信阳市中心医院", "日间化疗出入院记录", "姓名: 性别:女年龄:65岁 科别:日间化疗中心[东院床号:04 登记号:0000 住院号:25", "区]", "入院时间: 2026年03月23日 08:29:00出院时间: 2026年03月23日 11:14:00 住院天数: 1天", "主诉: 确诊肺癌1年余", "入院情况: 1年余前因“胸闷”就诊我院, 2025-01-17CT增强64: 1.右肺门占位, 考虑恶性病变并", "右肺中下叶不张, 右下肺动受侵可能。2. 双肺纤维索条灶。双肺多发小结节, 转移待排。3.右侧", "胸腔少量积液。4.双肾小囊肿。5.升结肠多发憩室。6.子宫后壁肌瘤可能。7.冠状动脉CTA未见明", "显异常。2025-01-23行纤支镜下肺活检, 2025-01-23 活体组织病理申请 诊断意见: (右中间段支", "气管)考虑小细胞癌, 已行免疫组化协诊。2025-01-26 免疫组化申请: CK广谱 (点+), CD56 (+),", "Syn (+), INSM1 (+), CK5/6 (-), P40 (-), TTF1 (+), NapsinA (-), Ki-67 (80%+)。结合HE", "及免疫组化结果, (右中间段支气管)肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04", "-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期, 2025-04-22给予“EP”方案化疗联合", "“替雷利珠单抗”免疫治疗1周期, 化疗后呕吐反应较重, 予以对症支持治疗。2025-05-19、2025", "-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加增强", "(胸部,上腹部,下腹部) 诊断意见: 1. 右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节。", "100%", "16:56", "2026/3/23"]

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
2026-08-06 10:27:04,374 INFO     30 [qwen-vl-parser] text API response (len=1094):
["姓名：", "科室：产科二区", "床号：", "住院号", "今日随科主任宋瑞香主治医师查房，患者精神好，饮食及睡眠可，大小便正常，未破", "水，未见红，无腹痛。查体：生命体征平稳，心肺听诊未闻及明显异常，胎心波动于正常范", "围，无宫缩。目前诊断：1.妊娠合并于宫瘢痕；2.孕2产；宫内孕39周头位待产。诊断依", "据：1.停经后有自觉胎动，产前检查可闻及胎心。2、查体：宫高34CM，腹围102CM，估计胎儿", "体重：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水。骨盆外测量及", "内诊：未做。3、辅助检查：B超（2020.07.02 本院）：晓孕宫内单活胎头位(双顶径", "9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。科主任宋瑞香主治医师查房指示：", "患者孕足月、瘢痕子宫，若阴道分娩易出现先兆子宫破裂、子宫破裂、胎死宫内等情况，患者", "及其家属表示理解，要求明日剖宫产终止妊娠，完善术前谈话，积极术前准备，严密监测胎心", "变化。以上医嘱已执行。", "主治医师：主治医师：", "孙丹", "2020年07月08日 10：20", "术前小结", "姓名：", "性别：女，年龄：36岁；", "病历摘要：以“伴经39周，要求住院待产”为主诉入院。孕2产，否认产后出血及产褥感", "染史，否认不良孕产史。查体：生命体征平稳，心肺听诊未闻及异常。腹隆，晚孕腹型。肝脾", "肋下未触及，下腹部可见一长约15cm的横行手术瘢痕。双下肢无水肿；专科检查：宫高34CM，", "腹围102CM，估计胎儿体重：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未", "破水。骨盆外测量及内诊：未做。辅助检查：B超（2020.07.02 本院）：晓孕宫内单活胎", "头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。入院后要求剖宫产终止", "妊娠，手术相关风险已向其讲明，并在手术同意书上签字。请示科主任宋瑞香副主任医师，同", "意安排手术，手术医师宋瑞香主治医师查看病人，生命体征平稳，无手术禁忌，积极术前准", "备。", "术前诊断：1.妊娠合并子宫瘢痕；2.孕2产；宫内孕39周头位待产。", "手术指证：足月妊娠，瘢痕子宫，患者及家属要求，无手术禁忌症：", "拟施手术名称和方式：拟定于明日07：30行二次子宫下段剖宫产术；", "拟施麻醉：椎管内麻醉；", "第 页", "总第 页", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-06 10:27:04,376 INFO     30 [qwen-vl-parser] page=11 text: 37 lines (bbox 921-957)
2026-08-06 10:27:04,377 INFO     30 [qwen-vl-parser] page=11 text: 37 sections
2026-08-06 10:27:04,533 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=223732, prompt_len=764
2026-08-06 10:27:05,785 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:27:05,786 INFO     30 [qwen-vl-parser] page=12 classify=text report_date=None
2026-08-06 10:27:05,853 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=223732, prompt_len=401
2026-08-06 10:27:07,116 INFO     30 [qwen-vl-parser] text API response (len=121):
["一", "院", "姓名：", "科室：产科二区", "床号：", "注意事项：规范操作，彻底止血，待新生儿娩出后，给予“缩宫素针”促宫缩治疗，做好", "新生儿复苏工作。", "主治医师：", "孙丹丹", "第 页", "总第 页"]
2026-08-06 10:27:07,117 INFO     30 [qwen-vl-parser] page=12 text: 11 lines (bbox 958-968)
2026-08-06 10:27:07,117 INFO     30 [qwen-vl-parser] page=12 text: 11 sections
2026-08-06 10:27:07,541 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1680903, prompt_len=764
2026-08-06 10:27:08,941 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:27:08,942 INFO     30 [qwen-vl-parser] page=13 classify=text report_date=None
2026-08-06 10:27:08,970 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1680903, prompt_len=401
2026-08-06 10:27:17,127 INFO     30 [qwen-vl-parser] text API response (len=1078):
["院", "姓名：", "科室：产科二区", "床：", "住院号：", "2020年07月09日 09时47分", "术后首次病程记录", "患者术前测胎心150次/分，于今日08：29-09：30在腰硬联合麻醉+基础麻醉下行二次子宫", "下段剖宫产术+子宫修补术，取下腹原横切口，剔除原瘢痕，逐层进腹，膀下指膀胱，暴露子", "宫下段，可见于宫下段肌层较薄，胎儿头发及胎脂漂浮，切开子宫后见羊水清，约600ml，吸", "净后以头位助娩一活男婴，出生1-10分钟均评10分，胎盘胎膜自娩完整，子宫收缩可，纱布球", "擦拭子宫腔，可见子宫下段肌层断裂，用可吸收线间断缝合子宫下段肌层，断裂的血管给予缝", "合，以恰桥可吸收线分两层连续缝合子宫切口。探查子宫切口无活动性出血，双侧附件外观正", "常，关腹。术程顺利，术中麻醉好，呼吸血压平稳，输入晶体液800ml，胶体液0ml，出血不", "多，约200ml，尿色清，量约100ml，术中诊断：1.妊娠合并子宫瘢痕；2.孕2产：宫内孕39*1周", "头位剖宫产；术后安返病房，测P：64次/分，R：18次/分，Bp：84/54mmHg，术后给予“头", "孢唑林钠针”预防感染、加强宫缩、会阴冲洗、尿管护理及支持对症等治疗，并嘱其按摩双下", "肢预防下肢静脉血栓形成，注意观察生命体征、子宫收缩及阴道出血情况。", "住院医师：冯雪云", "2020年07月10日 09时00分", "彭琼玉副主任医师查房记录", "今日为剖宫产术后一天，患者精神、睡眠好，无特殊不适，未排气。彭琼玉副主任医师", "查房：查体：生命体征平稳，双乳不胀，无泌乳，心肺未闻及异常，腹软，腹部切口皮肤对合", "好，未见红肿、硬结等异常，宫底平脐，子宫收缩好，阴道出血不多，尿管畅，尿色清，尿量", "正常，余查无特殊，查房意见：现术后一天，未排气，流食，体温正常，切口无感染迹象，病", "情无特殊，继续抗炎补液加强宫缩等治疗；嘱患者床上多翻身并按摩双下肢，以防术后肠粘连", "及栓塞性疾病发生，给予肌注缩宫素10uBID促进子宫收缩，给予子宫复旧磁疗促进产后子宫", "恢复，嘱保持乳房畅通，并给予泌乳磁疗促进乳汁分泌，输完液体后拔除尿管，适当下床活", "动，注意监测血糖情况，上述指示已执行。", "副主任医师：马", "住院医师：冯雪云", "2020年07月11日 08时06分", "术后第二天，患者无发热，已排气，尿管拔除后排尿畅。查体：生命体征平稳，心肺听诊", "第 页", "总第 页"]
2026-08-06 10:27:17,128 INFO     30 [qwen-vl-parser] page=13 text: 35 lines (bbox 969-1003)
2026-08-06 10:27:17,128 INFO     30 [qwen-vl-parser] page=13 text: 35 sections
2026-08-06 10:27:17,411 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1041724, prompt_len=764
2026-08-06 10:27:18,756 INFO     30 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-06 10:27:18,757 INFO     30 [qwen-vl-parser] page=14 classify=text report_date=None
2026-08-06 10:27:18,794 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1041724, prompt_len=401
2026-08-06 10:27:20,026 INFO     30 [qwen-vl-text] coord API raw response (len=2215):
[
	{"text": "1804 - Internet Explorer", "bbox": [28, 7, 127, 21]},
	{"text": "诊疗与病历 申请单 手术管理 医嘱单 会诊管理 重症管理 需关注医嘱 病情总览 质量管理 更多", "bbox": [43, 39, 634, 58]},
	{"text": "汤光冉 住院医师", "bbox": [893, 37, 970, 52]},
	{"text": "日间化疗中心[东院区]", "bbox": [893, 52, 988, 66]},
	{"text": "住院天数: 1 费别: 全国医保居民 余额: 0.00 诊断: 肺恶性肿瘤,恶性肿瘤... 医疗救助类型: 农村低保", "bbox": [39, 80, 526, 95]},
	{"text": "病人列表 全息视图", "bbox": [878, 80, 983, 99]},
	{"text": "操作 编辑 功能 表格 其他", "bbox": [36, 148, 191, 165]},
	{"text": "保存 打印 自动续打 预览 单独打印 手工解锁 隐藏留痕 病历参考 更新数据 首页", "bbox": [36, 174, 484, 222]},
	{"text": "信阳市中心医院", "bbox": [385, 255, 625, 300],
	"text": "日间化疗出入院记录", "bbox": [395, 332, 618, 365]},
	{"text": "姓名: 性别:女年龄:65岁 科别:日间化疗中心[东院床号:04 登记号:0000 住院号:25", "bbox": [100, 385, 857, 407]},
	{"text": "区]", "bbox": [379, 418, 402, 438]},
	{"text": "入院时间: 2026年03月23日 08:29:00出院时间: 2026年03月23日 11:14:00 住院天数: 1天", "bbox": [97, 458, 875, 484]},
	{"text": "主诉: 确诊肺癌1年余", "bbox": [97, 496, 279, 520]},
	{"text": "入院情况: 1年余前因“胸闷”就诊我院, 2025-01-17CT增强64: 1.右肺门占位, 考虑恶性病变并", "bbox": [97, 535, 912, 560]},
	{"text": "右肺中下叶不张, 右下肺动受侵可能。2. 双肺纤维索条灶。双肺多发小结节, 转移待排。3.右侧", "bbox": [97, 572, 912, 598]},
	{"text": "胸腔少量积液。4.双肾小囊肿。5.升结肠多发憩室。6.子宫后壁肌瘤可能。7.冠状动脉CTA未见明", "bbox": [97, 610, 912, 636]},
	{"text": "显异常。2025-01-23行纤支镜下肺活检, 2025-01-23 活体组织病理申请 诊断意见: (右中间段支", "bbox": [97, 649, 912, 675]},
	{"text": "气管)考虑小细胞癌, 已行免疫组化协诊。2025-01-26 免疫组化申请: CK广谱 (点+), CD56 (+),", "bbox": [97, 687, 912, 713]},
	{"text": "Syn (+), INSM1 (+), CK5/6 (-), P40 (-), TTF1 (+), NapsinA (-), Ki-67 (80%+)。结合HE", "bbox": [97, 725, 912, 751]},
	{"text": "及免疫组化结果, (右中间段支气管)肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04", "bbox": [97, 763, 912, 789]},
	{"text": "-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期, 2025-04-22给予“EP”方案化疗联合", "bbox": [97, 801, 912, 827]},
	{"text": "“替雷利珠单抗”免疫治疗1周期, 化疗后呕吐反应较重, 予以对症支持治疗。2025-05-19、2025", "bbox": [100, 840, 912, 866]},
	{"text": "-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加增强", "bbox": [97, 878, 912, 904]},
	{"text": "(胸部,上腹部,下腹部) 诊断意见: 1. 右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节。", "bbox": [100, 916, 904, 942]},
	{"text": "100%", "bbox": [932, 945, 963, 958]},
	{"text": "16:56", "bbox": [925, 964, 948, 977]},
	{"text": "2026/3/23", "bbox": [915, 981, 956, 994]}
]
2026-08-06 10:27:20,026 INFO     30 [qwen-vl-text] coord API: raw_items=27, valid_items=27, elapsed=24.8s
2026-08-06 10:27:20,026 INFO     30 [qwen-vl-text] coord item[0]: text=1804 - Internet Explorer, bbox=[28, 7, 127, 21]
2026-08-06 10:27:20,026 INFO     30 [qwen-vl-text] coord item[1]: text=诊疗与病历 申请单 手术管理 医嘱单 会诊管理 重症管理 需关注医嘱 病情总览 质量管理 更多, bbox=[43, 39, 634, 58]
2026-08-06 10:27:20,027 INFO     30 [qwen-vl-text] coord item[2]: text=汤光冉 住院医师, bbox=[893, 37, 970, 52]
2026-08-06 10:27:20,027 INFO     30 [qwen-vl-text] coord item[3]: text=日间化疗中心[东院区], bbox=[893, 52, 988, 66]
2026-08-06 10:27:20,027 INFO     30 [qwen-vl-text] coord item[4]: text=住院天数: 1 费别: 全国医保居民 余额: 0.00 诊断: 肺恶性肿瘤,恶性肿瘤... 医疗救助类型: 农村低保, bbox=[39, 80, 526, 95]
2026-08-06 10:27:20,027 INFO     30 [qwen-vl-text] coord item[5]: text=病人列表 全息视图, bbox=[878, 80, 983, 99]
2026-08-06 10:27:20,027 INFO     30 [qwen-vl-text] coord item[6]: text=操作 编辑 功能 表格 其他, bbox=[36, 148, 191, 165]
2026-08-06 10:27:20,027 INFO     30 [qwen-vl-text] coord item[7]: text=保存 打印 自动续打 预览 单独打印 手工解锁 隐藏留痕 病历参考 更新数据 首页, bbox=[36, 174, 484, 222]
2026-08-06 10:27:20,027 INFO     30 [qwen-vl-text] coord item[8]: text=日间化疗出入院记录, bbox=[395, 332, 618, 365]
2026-08-06 10:27:20,027 INFO     30 [qwen-vl-text] coord item[9]: text=姓名: 性别:女年龄:65岁 科别:日间化疗中心[东院床号:04 登记号:0000 住院号:25, bbox=[100, 385, 857, 407]
2026-08-06 10:27:20,027 INFO     30 [qwen-vl-text] coord item[10]: text=区], bbox=[379, 418, 402, 438]
2026-08-06 10:27:20,028 INFO     30 [qwen-vl-text] coord item[11]: text=入院时间: 2026年03月23日 08:29:00出院时间: 2026年03月23日 11:14:00 住院天数: 1天, bbox=[97, 458, 875, 484]
2026-08-06 10:27:20,028 INFO     30 [qwen-vl-text] coord item[12]: text=主诉: 确诊肺癌1年余, bbox=[97, 496, 279, 520]
2026-08-06 10:27:20,028 INFO     30 [qwen-vl-text] coord item[13]: text=入院情况: 1年余前因“胸闷”就诊我院, 2025-01-17CT增强64: 1.右肺门占位, 考虑恶性病变并, bbox=[97, 535, 912, 560]
2026-08-06 10:27:20,028 INFO     30 [qwen-vl-text] coord item[14]: text=右肺中下叶不张, 右下肺动受侵可能。2. 双肺纤维索条灶。双肺多发小结节, 转移待排。3.右侧, bbox=[97, 572, 912, 598]
2026-08-06 10:27:20,028 INFO     30 [qwen-vl-text] coord item[15]: text=胸腔少量积液。4.双肾小囊肿。5.升结肠多发憩室。6.子宫后壁肌瘤可能。7.冠状动脉CTA未见明, bbox=[97, 610, 912, 636]
2026-08-06 10:27:20,028 INFO     30 [qwen-vl-text] coord item[16]: text=显异常。2025-01-23行纤支镜下肺活检, 2025-01-23 活体组织病理申请 诊断意见: (右中间段支, bbox=[97, 649, 912, 675]
2026-08-06 10:27:20,028 INFO     30 [qwen-vl-text] coord item[17]: text=气管)考虑小细胞癌, 已行免疫组化协诊。2025-01-26 免疫组化申请: CK广谱 (点+), CD56 (+),, bbox=[97, 687, 912, 713]
2026-08-06 10:27:20,028 INFO     30 [qwen-vl-text] coord item[18]: text=Syn (+), INSM1 (+), CK5/6 (-), P40 (-), TTF1 (+), NapsinA (-), Ki-67 (80%+)。结合HE, bbox=[97, 725, 912, 751]
2026-08-06 10:27:20,028 INFO     30 [qwen-vl-text] coord item[19]: text=及免疫组化结果, (右中间段支气管)肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04, bbox=[97, 763, 912, 789]
2026-08-06 10:27:20,028 INFO     30 [qwen-vl-text] coord item[20]: text=-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期, 2025-04-22给予“EP”方案化疗联合, bbox=[97, 801, 912, 827]
2026-08-06 10:27:20,029 INFO     30 [qwen-vl-text] coord item[21]: text=“替雷利珠单抗”免疫治疗1周期, 化疗后呕吐反应较重, 予以对症支持治疗。2025-05-19、2025, bbox=[100, 840, 912, 866]
2026-08-06 10:27:20,029 INFO     30 [qwen-vl-text] coord item[22]: text=-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加增强, bbox=[97, 878, 912, 904]
2026-08-06 10:27:20,029 INFO     30 [qwen-vl-text] coord item[23]: text=(胸部,上腹部,下腹部) 诊断意见: 1. 右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节。, bbox=[100, 916, 904, 942]
2026-08-06 10:27:20,029 INFO     30 [qwen-vl-text] coord item[24]: text=100%, bbox=[932, 945, 963, 958]
2026-08-06 10:27:20,029 INFO     30 [qwen-vl-text] coord item[25]: text=16:56, bbox=[925, 964, 948, 977]
2026-08-06 10:27:20,029 INFO     30 [qwen-vl-text] coord item[26]: text=2026/3/23, bbox=[915, 981, 956, 994]
2026-08-06 10:27:20,033 INFO     30 [qwen-vl-text] page=1 — 28/28 coords, api_time=24.8s
2026-08-06 10:27:20,076 INFO     30 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=7309712, prompt_len=1504
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["胸腔少量积液。4.双肾小囊肿。5.升结肠多发息室。6.丁台加壁肌瘤可能。冠状动脉CT示无明显异常。2025-01-23行纤支镜下肺活检，2025-01-23活体组织病理申请 诊断意见：(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。2025-01-26免疫组化申请：CK广谱(点+)，CD56(+)，Syn(+)，INSM1(+)，CK5/6(-)，P40(-)，TTF1(+),NapsinA(-)，Ki-67(80%+)。结合HE及免疫组化结果，(右中间段支气管)肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期，2025-04-22给予“EP”方案化疗联合“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗。2025-05-19、2025-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加强(胸部，上腹部，下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节，转移瘤可能；建议追踪复查。2.双肺慢性炎症，右肺中叶局限性支扩，双侧胸腔少量积液。3.脾脏低密度灶，建议追踪复查。4.胆囊可疑小结石。升结肠多发憩室。5.双肾小囊肿。与2025-05-18日片比较：右肺中叶局限性支扩，右肺下叶内基底段结节较前增大，右肺门淋巴结较前增大。考虑病情进展，于2025-08-23给予“安罗替尼12mg”联合“替雷利珠单抗”抗肿瘤治疗1周期。后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-22、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重无明显变化。诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利，予办理出院手续。"]

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
2026-08-06 10:27:28,052 INFO     30 [qwen-vl-parser] text API response (len=630):
["出院", "姓名：", "科室：产科二区", "床号", "住院", "未闻及异常，双乳泌乳量不多，腹软，子宫收缩好，宫底位于脐下两横指，无压痛，阴道出血", "不多，暗红色，无异味，腹部切口换药见切口皮缘对合好，未见红肿、硬结及渗液等异常，双", "下肢无水肿，现术后第二天，病情稳定，改为II级护理，已排气给予苔含，注意体温变化及切", "口情况；继续予子宫复旧磁疗促进产后子宫恢复，加用腹部切口红外线治疗促进伤口愈合，加", "益宫颗粒(自各药物)促宫缩治疗，观察体温及阴道恶露情况。", "主治医师：孙丹丹", "2020年07月12日 10时00分", "彭琼玉副主任医师查房记录", "今日查房，患者剖宫产术后三天，患者未诉不适，精神好，饮食、睡眠正常，查体：生", "命体征平稳，心肺听诊未闻及异常，双乳泌乳量多，腹软，腹部切口无红肿、硬结、渗液等异", "常，子宫收缩好，阴道出血不多，余查无特殊，再次复查血常规：白细胞10.59×10⁹/L,中性", "粒细胞86.3%，偏高，血红蛋白100g/L，患者复查白细胞正常，中性粒细胞偏高，体温正常，", "切口无感染迹象，考虑术后炎性反应，暂不特殊处理，嘱加强营养，加强运动。彭琼玉副主任", "医师查房指示：患者现病情稳定，腹部伤口皮内结合，无需拆线，达临床治愈，顺利完成剖宫", "产临床路径管理，今日办理出院。指示已执行。", "副主任医师：彭琼玉", "主治医师：孙丹丹", ""]
2026-08-06 10:27:28,053 INFO     30 [qwen-vl-parser] page=14 text: 22 lines (bbox 1004-1025)
2026-08-06 10:27:28,053 INFO     30 [qwen-vl-parser] page=14 text: 22 sections
2026-08-06 10:27:28,465 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1460379, prompt_len=764
2026-08-06 10:27:29,929 INFO     30 [qwen-vl-parser] classify API response (len=59):
```json
{
    "type": "text",
    "report_date": null
}
```
2026-08-06 10:27:29,930 INFO     30 [qwen-vl-parser] page=15 classify=text report_date=None
2026-08-06 10:27:29,959 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1460379, prompt_len=401
2026-08-06 10:27:35,710 INFO     30 [qwen-vl-text] coord API raw response (len=932):
[
	{"text": "胸腔少量积液。4.双肾小囊肿。5.升结肠多发息室。6.丁台加壁肌瘤可能。冠状动脉CT示无明显异常。2025-01-23行纤支镜下肺活检，2025-01-23活体组织病理申请 诊断意见：(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。2025-01-26免疫组化申请：CK广谱(点+)，CD56(+)，Syn(+)，INSM1(+)，CK5/6(-)，P40(-)，TTF1(+),NapsinA(-)，Ki-67(80%+)。结合HE及免疫组化结果，(右中间段支气管)肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期，2025-04-22给予“EP”方案化疗联合“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗。2025-05-19、2025-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加强(胸部，上腹部，下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节，转移瘤可能；建议追踪复查。2.双肺慢性炎症，右肺中叶局限性支扩，双侧胸腔少量积液。3.脾脏低密度灶，建议追踪复查。4.胆囊可疑小结石。升结肠多发憩室。5.双肾小囊肿。与2025-05-18日片比较：右肺中叶局限性支扩，右肺下叶内基底段结节较前增大，右肺门淋巴结较前增大。考虑病情进展，于2025-08-23给予“安罗替尼12mg”联合“替雷利珠单抗”抗肿瘤治疗1周期。后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-22、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重无明显变化。诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利，予办理出院手续。", "bbox": [5, 0, 923, 984]}
]
2026-08-06 10:27:35,710 INFO     30 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=15.6s
2026-08-06 10:27:35,711 INFO     30 [qwen-vl-text] coord item[0]: text=胸腔少量积液。4.双肾小囊肿。5.升结肠多发息室。6.丁台加壁肌瘤可能。冠状动脉CT示无明显异常。2025-01-23行纤支镜下肺活检，2025-01-23活体组织病理申请 诊断意见：(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。2025-01-26免疫组化申请：CK广谱(点+)，CD56(+)，Syn(+)，INSM1(+)，CK5/6(-)，P40(-)，TTF1(+),NapsinA(-)，Ki-67(80%+)。结合HE及免疫组化结果，(右中间段支气管)肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期，2025-04-22给予“EP”方案化疗联合“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗。2025-05-19、2025-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加强(胸部，上腹部，下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节，转移瘤可能；建议追踪复查。2.双肺慢性炎症，右肺中叶局限性支扩，双侧胸腔少量积液。3.脾脏低密度灶，建议追踪复查。4.胆囊可疑小结石。升结肠多发憩室。5.双肾小囊肿。与2025-05-18日片比较：右肺中叶局限性支扩，右肺下叶内基底段结节较前增大，右肺门淋巴结较前增大。考虑病情进展，于2025-08-23给予“安罗替尼12mg”联合“替雷利珠单抗”抗肿瘤治疗1周期。后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-22、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重无明显变化。诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利，予办理出院手续。, bbox=[5, 0, 923, 984]
2026-08-06 10:27:35,721 INFO     30 [qwen-vl-text] page=2 — 1/1 coords, api_time=15.6s
2026-08-06 10:27:35,799 INFO     30 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=6399521, prompt_len=1572
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共51行）
["国家医保编码：D411502011804 - Internet Explorer", "美系统) 修改患者信息 诊疗与病历 申请单 手术管理 医嘱单 会诊管理 重症管理 需关注医嘱 病情总览 质量管理 更多", "汤光冉 住院医师", "日间化疗中心[东院区]", "0000 床号: 04 住院天数: 1 费别: 全国医保居民 余额: 0.00 诊断: 肺恶性肿瘤,恶性肿瘤... 医疗救助类型: 农村低保", "病人列表 全息视图", "(1) ×", "操作 编辑 功能 表格 其他", "历", "保存 打印 自动续打 预览 单独打印 手工解锁 隐藏留痕 病历参考 更新数据 首页", "记录", "1:09:45 曾庆星", "医师审核", "录单", "1:10:52 曾庆星", "医师审核", "录单", "1:11:53 曾庆星", "医师审核", "11:12:02 曾庆星", "医师审核", "单(日间...", "11:13:02 曾庆星", "医师审核", "已打印", "11:15:03 曾庆星", "医师审核", "评估表", "16:30:58 曾庆星", "院医师审核", "/TE风险评...", "16:32:44 曾庆星", "院医师审核", "后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-2", "2、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我", "院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重", "无明显变化。", "诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利", "，予办理出院手续。", "出院情况：患者未诉不适，神志清，精神可，生命体征平稳。", "出院诊断：", "1.恶性肿瘤免疫治疗", "2.肺恶性肿瘤小细胞肺癌IV期", "3.肺继发恶性肿瘤", "4.冠状动脉粥样硬化性心脏病", "5.胸腔积液", "6.心包积液", "7.肺部感染", "8.腔隙性脑梗死", "9.肾功能检查的异常结果", "1"]

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
2026-08-06 10:27:38,043 INFO     30 [qwen-vl-parser] text API response (len=1062):
["出院记录", "姓名", "科室：产科二区", "床号.", "住院", "2020年07月12日", "出院记录", "患者.", "36岁", "住院号：", "入院日期：2020-07-08 08:36:09", "出院日期：2020年07月12日", "住院天数：4天", "入院情况：以“停经39周，要求住院待产”为主诉入院。入院查体：生命体征平稳，心肺", "听诊未闻及异常。腹隆，晚孕腹型，肝脾肋下未触及。专科检查：宫高34CM，腹围102CM，估", "计胎儿体宣：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水，骨盆外", "测量及内诊：未做。辅助检查：B超（2020.07.02 本院）：晚孕宫内单活胎头位(双顶径", "9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。", "入院诊断：1.妊娠合并子宫瘢痕；2.孕产：宫内孕39周头位待产。", "诊疗经过：患者入院后完善相关检查，要求剖宫产，于2020年07月09日 08：29-09：30在", "腰硬联合麻醉+基础麻醉下行二次于宫下段剖宫产术+子宫修补术。取下腹原横切口，剔除原瘢", "痕，逐层进腹，膀下指膀胱，暴露子宫下段，可见子宫下段肌层较薄，胎儿头发及胎脂漂浮，", "切开子宫后见羊水清，约600ml，吸净后以头位助娩一活男婴，出生1-10分钟均评10分，胎盘", "胎膜自娩完整，子宫收缩可，纱布球擦拭子宫腔，可见子宫下段肌层断裂，用可吸收线间断缝", "合子宫下段肌层，断裂的立皆给予缝合，以伦桥可吸收线分两层连续缝合子宫切口。探查子宫", "切口无活动性出血，双侧附件外观正常，关腹，术程顺利，术中出血不多，术后予以降压、抗", "感染、加强宫缩支持及对症治疗。", "出院诊断：1.妊娠合并子宫瘢痕；2.孕产：宫内孕39+周头位剖宫产：", "出院情况：患者精神、饮食好，无特殊不适。查体：生命体征平稳，心肺听诊未闻及明显", "异常，双乳泌乳量可，双乳稍涨，腹部平软，切口无红肿、渗出、硬结等愈合良好，子宫收缩", "好，宫底约脐耻之间，宫体无压痛，恶露呈淡红色，量少，无异味。现患者一般情况好，双乳", "泌乳量多，子宫复旧好，腹部切口愈合良好，无需拆线，达临床治愈，于今日出院。完成计划", "性剖宫产临床路径。", "出院医嘱：1.注意休息，合理营养；", "2.禁性生活、盆浴及重体力劳动2个月；", "3.坚持纯母乳喂养大于4-6月；", "第 页", "总第 页"]
2026-08-06 10:27:38,044 INFO     30 [qwen-vl-parser] page=15 text: 38 lines (bbox 1026-1063)
2026-08-06 10:27:38,044 INFO     30 [qwen-vl-parser] page=15 text: 38 sections
2026-08-06 10:27:38,270 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=642933, prompt_len=764
2026-08-06 10:27:44,008 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:27:44,009 INFO     30 [qwen-vl-parser] page=16 classify=text report_date=None
2026-08-06 10:27:44,058 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=642933, prompt_len=401
2026-08-06 10:27:47,189 INFO     30 [qwen-vl-parser] text API response (len=416):
["医院", "出院记录", "姓名：", "科室：产科二区", "床号：", "住院号：2", "4.产后42天门诊复查，如出院后出现任何异常情况请立即就诊，注意产妇心理", "状态，必要时心理咨询门诊就诊；若阴道出血淋漓不尽持续1月或阴道出血量多于平素月经", "量、腹痛、发热等，及时就诊：（每周二、周六门诊326彭琼玉副主任医师坐诊）", "5.严格避孕，术后六个月可安环避孕，术后2年以上方可再次妊娠：", "6.新生儿乙肝疫苗第一针，卡介苗已接种，新生儿生后10天补充维生素AD滴剂", "1粒/次，一次/日（至2岁），出院后新生儿每日测胆红素值，黄疸加重或持续14天未消退，或", "出院后有不适，可直接到1号楼9楼新生儿科探视大厅就诊（携带宝宝就诊卡）；", "7.咨询电话产科：", "，新生儿科：0398-3118382。母乳咨询电话：", "0398-3118618.", "主治医师：", "孙州", ""]
2026-08-06 10:27:47,190 INFO     30 [qwen-vl-parser] page=16 text: 18 lines (bbox 1064-1081)
2026-08-06 10:27:47,191 INFO     30 [qwen-vl-parser] page=16 text: 18 sections
2026-08-06 10:27:47,587 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=913014, prompt_len=764
2026-08-06 10:27:49,140 INFO     30 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2023-08-14"}
```
2026-08-06 10:27:49,141 INFO     30 [qwen-vl-parser] page=17 classify=text report_date=2023-08-14
2026-08-06 10:27:49,158 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=913014, prompt_len=401
2026-08-06 10:27:55,755 INFO     30 [qwen-vl-parser] text API response (len=921):
["临床数据中心-患者360视图", "返回患者查询", "患者姓名", "女 出生日", "首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>", "就诊时间轴", "门诊号", "诊时间：2023-08-14 15:29:02 接诊科室：普通儿科三组（门） 接诊医生：谭真真", "全部", "近一月", "近三月", "近半年", "近一年", "近五年", "门诊39 住院1", "总览", "就诊列表", "集成视图", "诊断", "病历文书", "处方", "检验", "检查", "处置", "肺功能检查", "单机报告", "透析治疗", "费用", "体检报告", "1.", "门诊号.", "2024-04-24 普通儿科一组（...", "2024-04-19 普通儿科一组（...", "2024-04-08 妇科门诊", "2024-04-08 妇科一病区(门)", "2024-01-05 妇科一病区(门)", "2023-08-14 普通儿科三组（...", "2023-07-06 普通儿科三组（...", "2023-06-26 普通儿科三组（...", "2023-05-08 普通儿科三组（...", "2023-05-08 普通儿科一组（...", "2023-04-18 普通儿科三组（...", "姓名：", "性别：女", "年龄：39岁", "民族：汉族", "身份证", "现住址：", "就诊类型：初诊", "就诊科室：普通儿科三组（门）", "就诊日期：2023-08-14 15:29", "联系电话", "主诉：咽峡炎购药", "现病史：咽峡炎购药", "既往史：平素体健，无肝炎、结核类传染病史", "过敏史：无", "体格检查：发育正常，营养良好，精神一般，口唇红润，双侧扁桃体无肿大，无充血、分泌物。咽腔黏膜无充", "血、红肿、疱疹，双肺呼吸音清，听诊心律齐，无杂音，腹平软，无压痛、反跳痛", "辅助检查：", "初步印象：急性咽峡炎", "处理意见：门诊", "备注：", "医师签名：谭真真", "第1页"]
2026-08-06 10:27:55,756 INFO     30 [qwen-vl-parser] page=17 text: 64 lines (bbox 1082-1145)
2026-08-06 10:27:55,756 INFO     30 [qwen-vl-parser] page=17 text: 64 sections
2026-08-06 10:27:56,016 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=669524, prompt_len=764
2026-08-06 10:27:57,686 INFO     30 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-01-05"}
```
2026-08-06 10:27:57,687 INFO     30 [qwen-vl-parser] page=18 classify=text report_date=2024-01-05
2026-08-06 10:27:57,720 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=669524, prompt_len=401
2026-08-06 10:28:00,649 INFO     30 [qwen-vl-parser] text API response (len=407):
["门诊病历", "门诊号：", "姓名", "性别：女", "年龄：39岁", "民族：汉族", "身份证号", "现住址：", "就诊类型：急诊", "就诊科室：妇科一病区(门)", "就诊日期：2024-01-05 10:32", "联系电话", "主诉：下腹痛2小时", "现病史：患者月经第二天，无明显诱因出现下腹持续疼痛", "既往史：平素体健，无高血压、冠心病、糖尿病病史，无肝炎、结核等传染病史，无手术史", "婚育史：", "月经史：患者平素月经规律，量中等，色正常，无痛经。", "过敏史：无", "专科检查：外阴：发育正常，阴毛呈女性分布；阴道：通畅，粘膜红润，未见异常分泌物；宫颈：光滑，大小正常，宫体：正常大小，无压痛。附件：左侧附件区压痛明显。", "辅助检查：", "初步印象：女性盆腔炎性疾病", "处理意见：门诊治疗", "备注：", "医师签名：汪会芳", "第1页", ""]
2026-08-06 10:28:00,650 INFO     30 [qwen-vl-parser] page=18 text: 25 lines (bbox 1146-1170)
2026-08-06 10:28:00,650 INFO     30 [qwen-vl-parser] page=18 text: 25 sections
2026-08-06 10:28:00,926 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=908963, prompt_len=764
2026-08-06 10:28:03,078 INFO     30 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-04-08"}
```
2026-08-06 10:28:03,079 INFO     30 [qwen-vl-parser] page=19 classify=text report_date=2024-04-08
2026-08-06 10:28:03,115 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=908963, prompt_len=401
2026-08-06 10:28:04,287 INFO     30 [qwen-vl-text] coord API raw response (len=2982):
[
	{"text": "国家医保编码：D411502011804 - Internet Explorer", "bbox": [24, 5, 215, 18]},
	{"text": "美系统) 修改患者信息 诊疗与病历 申请单 手术管理 医嘱单 会诊管理 重症管理 需关注医嘱 病情总览 质量管理 更多", "bbox": [24, 37, 672, 56]},
	{"text": "汤光冉 住院医师", "bbox": [903, 36, 970, 50]},
	{"text": "日间化疗中心[东院区]", "bbox": [903, 50, 987, 64]},
	{"text": "0000 床号: 04 住院天数: 1 费别: 全国医保居民 余额: 0.00 诊断: 肺恶性肿瘤,恶性肿瘤... 医疗救助类型: 农村低保", "bbox": [27, 77, 575, 93]},
	{"text": "病人列表 全息视图", "bbox": [883, 73, 992, 100]},
	{"text": "(1) ×", "bbox": [20, 112, 55, 128]},
	{"text": "操作 编辑 功能 表格 其他", "bbox": [137, 146, 275, 162]},
	{"text": "历", "bbox": [20, 179, 31, 193]},
	{"text": "保存 打印 自动续打 预览 单独打印 手工解锁 隐藏留痕 病历参考 更新数据 首页", "bbox": [137, 171, 538, 217]},
	{"text": "记录", "bbox": [16, 253, 34, 267]},
	{"text": "1:09:45 曾庆星", "bbox": [16, 279, 78, 293]},
	{"text": "医师审核", "bbox": [16, 300, 47, 313]},
	{"text": "录单", "bbox": [13, 337, 33, 350]},
	{"text": "1:10:52 曾庆星", "bbox": [14, 363, 78, 376]},
	{"text": "医师审核", "bbox": [13, 383, 46, 396]},
	{"text": "录单", "bbox": [13, 419, 33, 432]},
	{"text": "1:11:53 曾庆星", "bbox": [14, 445, 78, 458]},
	{"text": "医师审核", "bbox": [13, 465, 46, 478]},
	{"text": "11:12:02 曾庆星", "bbox": [13, 525, 78, 538]},
	{"text": "医师审核", "bbox": [13, 545, 46, 558]},
	{"text": "单(日间...", "bbox": [8, 582, 51, 596]},
	{"text": "11:13:02 曾庆星", "bbox": [12, 608, 78, 622]},
	{"text": "医师审核", "bbox": [8, 629, 47, 642]},
	{"text": "已打印", "bbox": [72, 665, 100, 679]},
	{"text": "11:15:03 曾庆星", "bbox": [12, 691, 78, 705]},
	{"text": "医师审核", "bbox": [8, 712, 47, 725]},
	{"text": "评估表", "bbox": [8, 748, 36, 761]},
	{"text": "16:30:58 曾庆星", "bbox": [12, 774, 78, 787]},
	{"text": "院医师审核", "bbox": [4, 794, 49, 807]},
	{"text": "/TE风险评...", "bbox": [4, 830, 52, 843]},
	{"text": "16:32:44 曾庆星", "bbox": [12, 856, 78, 869]},
	{"text": "院医师审核", "bbox": [4, 876, 49, 889]},
	{"text": "后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-2", "bbox": [192, 227, 922, 251]},
	{"text": "2、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我", "bbox": [192, 264, 920, 290]},
	{"text": "院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重", "bbox": [192, 302, 920, 328]},
	{"text": "无明显变化。", "bbox": [192, 343, 285, 368]},
	{"text": "诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利", "bbox": [192, 380, 920, 406]},
	{"text": "，予办理出院手续。", "bbox": [192, 419, 339, 444]},
	{"text": "出院情况：患者未诉不适，神志清，精神可，生命体征平稳。", "bbox": [192, 457, 647, 482]},
	{"text": "出院诊断：", "bbox": [192, 496, 267, 520]},
	{"text": "1.恶性肿瘤免疫治疗", "bbox": [226, 534, 382, 559]},
	{"text": "2.肺恶性肿瘤小细胞肺癌IV期", "bbox": [225, 572, 452, 598]},
	{"text": "3.肺继发恶性肿瘤", "bbox": [225, 611, 365, 637]},
	{"text": "4.冠状动脉粥样硬化性心脏病", "bbox": [225, 650, 452, 676]},
	{"text": "5.胸腔积液", "bbox": [225, 689, 313, 714]},
	{"text": "6.心包积液", "bbox": [225, 727, 313, 752]},
	{"text": "7.肺部感染", "bbox": [226, 766, 313, 791]},
	{"text": "8.腔隙性脑梗死", "bbox": [226, 805, 350, 830]},
	{"text": "9.肾功能检查的异常结果", "bbox": [226, 843, 418, 869]},
	{"text": "1", "bbox": [555, 918, 563, 938]}
]
2026-08-06 10:28:04,289 INFO     30 [qwen-vl-text] coord API: raw_items=51, valid_items=51, elapsed=28.5s
2026-08-06 10:28:04,290 INFO     30 [qwen-vl-text] coord item[0]: text=国家医保编码：D411502011804 - Internet Explorer, bbox=[24, 5, 215, 18]
2026-08-06 10:28:04,290 INFO     30 [qwen-vl-text] coord item[1]: text=美系统) 修改患者信息 诊疗与病历 申请单 手术管理 医嘱单 会诊管理 重症管理 需关注医嘱 病情总览 质量管理 更多, bbox=[24, 37, 672, 56]
2026-08-06 10:28:04,291 INFO     30 [qwen-vl-text] coord item[2]: text=汤光冉 住院医师, bbox=[903, 36, 970, 50]
2026-08-06 10:28:04,291 INFO     30 [qwen-vl-text] coord item[3]: text=日间化疗中心[东院区], bbox=[903, 50, 987, 64]
2026-08-06 10:28:04,291 INFO     30 [qwen-vl-text] coord item[4]: text=0000 床号: 04 住院天数: 1 费别: 全国医保居民 余额: 0.00 诊断: 肺恶性肿瘤,恶性肿瘤... 医疗救助类型: 农村低保, bbox=[27, 77, 575, 93]
2026-08-06 10:28:04,292 INFO     30 [qwen-vl-text] coord item[5]: text=病人列表 全息视图, bbox=[883, 73, 992, 100]
2026-08-06 10:28:04,292 INFO     30 [qwen-vl-text] coord item[6]: text=(1) ×, bbox=[20, 112, 55, 128]
2026-08-06 10:28:04,292 INFO     30 [qwen-vl-text] coord item[7]: text=操作 编辑 功能 表格 其他, bbox=[137, 146, 275, 162]
2026-08-06 10:28:04,292 INFO     30 [qwen-vl-text] coord item[8]: text=历, bbox=[20, 179, 31, 193]
2026-08-06 10:28:04,293 INFO     30 [qwen-vl-text] coord item[9]: text=保存 打印 自动续打 预览 单独打印 手工解锁 隐藏留痕 病历参考 更新数据 首页, bbox=[137, 171, 538, 217]
2026-08-06 10:28:04,293 INFO     30 [qwen-vl-text] coord item[10]: text=记录, bbox=[16, 253, 34, 267]
2026-08-06 10:28:04,294 INFO     30 [qwen-vl-text] coord item[11]: text=1:09:45 曾庆星, bbox=[16, 279, 78, 293]
2026-08-06 10:28:04,295 INFO     30 [qwen-vl-text] coord item[12]: text=医师审核, bbox=[16, 300, 47, 313]
2026-08-06 10:28:04,295 INFO     30 [qwen-vl-text] coord item[13]: text=录单, bbox=[13, 337, 33, 350]
2026-08-06 10:28:04,295 INFO     30 [qwen-vl-text] coord item[14]: text=1:10:52 曾庆星, bbox=[14, 363, 78, 376]
2026-08-06 10:28:04,296 INFO     30 [qwen-vl-text] coord item[15]: text=医师审核, bbox=[13, 383, 46, 396]
2026-08-06 10:28:04,296 INFO     30 [qwen-vl-text] coord item[16]: text=录单, bbox=[13, 419, 33, 432]
2026-08-06 10:28:04,297 INFO     30 [qwen-vl-text] coord item[17]: text=1:11:53 曾庆星, bbox=[14, 445, 78, 458]
2026-08-06 10:28:04,297 INFO     30 [qwen-vl-text] coord item[18]: text=医师审核, bbox=[13, 465, 46, 478]
2026-08-06 10:28:04,298 INFO     30 [qwen-vl-text] coord item[19]: text=11:12:02 曾庆星, bbox=[13, 525, 78, 538]
2026-08-06 10:28:04,298 INFO     30 [qwen-vl-text] coord item[20]: text=医师审核, bbox=[13, 545, 46, 558]
2026-08-06 10:28:04,299 INFO     30 [qwen-vl-text] coord item[21]: text=单(日间..., bbox=[8, 582, 51, 596]
2026-08-06 10:28:04,299 INFO     30 [qwen-vl-text] coord item[22]: text=11:13:02 曾庆星, bbox=[12, 608, 78, 622]
2026-08-06 10:28:04,299 INFO     30 [qwen-vl-text] coord item[23]: text=医师审核, bbox=[8, 629, 47, 642]
2026-08-06 10:28:04,300 INFO     30 [qwen-vl-text] coord item[24]: text=已打印, bbox=[72, 665, 100, 679]
2026-08-06 10:28:04,300 INFO     30 [qwen-vl-text] coord item[25]: text=11:15:03 曾庆星, bbox=[12, 691, 78, 705]
2026-08-06 10:28:04,301 INFO     30 [qwen-vl-text] coord item[26]: text=医师审核, bbox=[8, 712, 47, 725]
2026-08-06 10:28:04,302 INFO     30 [qwen-vl-text] coord item[27]: text=评估表, bbox=[8, 748, 36, 761]
2026-08-06 10:28:04,303 INFO     30 [qwen-vl-text] coord item[28]: text=16:30:58 曾庆星, bbox=[12, 774, 78, 787]
2026-08-06 10:28:04,303 INFO     30 [qwen-vl-text] coord item[29]: text=院医师审核, bbox=[4, 794, 49, 807]
2026-08-06 10:28:04,303 INFO     30 [qwen-vl-text] coord item[30]: text=/TE风险评..., bbox=[4, 830, 52, 843]
2026-08-06 10:28:04,303 INFO     30 [qwen-vl-text] coord item[31]: text=16:32:44 曾庆星, bbox=[12, 856, 78, 869]
2026-08-06 10:28:04,303 INFO     30 [qwen-vl-text] coord item[32]: text=院医师审核, bbox=[4, 876, 49, 889]
2026-08-06 10:28:04,304 INFO     30 [qwen-vl-text] coord item[33]: text=后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-2, bbox=[192, 227, 922, 251]
2026-08-06 10:28:04,304 INFO     30 [qwen-vl-text] coord item[34]: text=2、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我, bbox=[192, 264, 920, 290]
2026-08-06 10:28:04,304 INFO     30 [qwen-vl-text] coord item[35]: text=院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重, bbox=[192, 302, 920, 328]
2026-08-06 10:28:04,305 INFO     30 [qwen-vl-text] coord item[36]: text=无明显变化。, bbox=[192, 343, 285, 368]
2026-08-06 10:28:04,305 INFO     30 [qwen-vl-text] coord item[37]: text=诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利, bbox=[192, 380, 920, 406]
2026-08-06 10:28:04,305 INFO     30 [qwen-vl-text] coord item[38]: text=，予办理出院手续。, bbox=[192, 419, 339, 444]
2026-08-06 10:28:04,305 INFO     30 [qwen-vl-text] coord item[39]: text=出院情况：患者未诉不适，神志清，精神可，生命体征平稳。, bbox=[192, 457, 647, 482]
2026-08-06 10:28:04,306 INFO     30 [qwen-vl-text] coord item[40]: text=出院诊断：, bbox=[192, 496, 267, 520]
2026-08-06 10:28:04,306 INFO     30 [qwen-vl-text] coord item[41]: text=1.恶性肿瘤免疫治疗, bbox=[226, 534, 382, 559]
2026-08-06 10:28:04,306 INFO     30 [qwen-vl-text] coord item[42]: text=2.肺恶性肿瘤小细胞肺癌IV期, bbox=[225, 572, 452, 598]
2026-08-06 10:28:04,306 INFO     30 [qwen-vl-text] coord item[43]: text=3.肺继发恶性肿瘤, bbox=[225, 611, 365, 637]
2026-08-06 10:28:04,306 INFO     30 [qwen-vl-text] coord item[44]: text=4.冠状动脉粥样硬化性心脏病, bbox=[225, 650, 452, 676]
2026-08-06 10:28:04,306 INFO     30 [qwen-vl-text] coord item[45]: text=5.胸腔积液, bbox=[225, 689, 313, 714]
2026-08-06 10:28:04,306 INFO     30 [qwen-vl-text] coord item[46]: text=6.心包积液, bbox=[225, 727, 313, 752]
2026-08-06 10:28:04,306 INFO     30 [qwen-vl-text] coord item[47]: text=7.肺部感染, bbox=[226, 766, 313, 791]
2026-08-06 10:28:04,307 INFO     30 [qwen-vl-text] coord item[48]: text=8.腔隙性脑梗死, bbox=[226, 805, 350, 830]
2026-08-06 10:28:04,307 INFO     30 [qwen-vl-text] coord item[49]: text=9.肾功能检查的异常结果, bbox=[226, 843, 418, 869]
2026-08-06 10:28:04,307 INFO     30 [qwen-vl-text] coord item[50]: text=1, bbox=[555, 918, 563, 938]
2026-08-06 10:28:04,312 INFO     30 [qwen-vl-text] page=3 — 51/51 coords, api_time=28.5s
2026-08-06 10:28:04,313 INFO     30 [qwen-vl-text] new_positions (87):
[[0, 390.8433232421875, 729.7248173828125, 523.0549311523438, 542.1066008300782], [0, 390.8433232421875, 912.7208242187501, 542.1066008300782, 561.1582705078125], [0, 390.8433232421875, 684.5406181640625, 561.1582705078125, 580.2099401855469], [0, 390.8433232421875, 998.570802734375, 580.2099401855469, 599.2616098632813], [0, 390.8433232421875, 756.8353369140625, 599.2616098632813, 618.3132795410156], [0, 390.8433232421875, 474.434091796875, 618.3132795410156, 635.6329792480469], [0, 390.8433232421875, 844.944525390625, 635.6329792480469, 654.6846489257813], [1, 63.279999999999994, 287.02, 12.124, 36.372], [1, 97.17999999999999, 1432.84, 67.548, 100.456], [1, 2018.1799999999998, 2192.2, 64.084, 90.064], [1, 2018.1799999999998, 2232.8799999999997, 90.064, 114.312], [1, 88.13999999999999, 1188.76, 138.56, 164.54], [1, 1984.2799999999997, 2221.58, 138.56, 171.468], [1, 81.35999999999999, 431.65999999999997, 256.336, 285.78], [1, 81.35999999999999, 1093.84, 301.368, 384.504], [1, 892.6999999999999, 1396.6799999999998, 575.024, 632.18], [1, 225.99999999999997, 1936.8199999999997, 666.82, 704.924], [1, 856.54, 908.5199999999999, 723.976, 758.616], [1, 219.21999999999997, 1977.4999999999998, 793.256, 838.288], [1, 219.21999999999997, 630.54, 859.072, 900.64], [1, 219.21999999999997, 2061.12, 926.62, 969.92], [1, 219.21999999999997, 2061.12, 990.704, 1035.736], [1, 219.21999999999997, 2061.12, 1056.52, 1101.552], [1, 219.21999999999997, 2061.12, 1124.068, 1169.1], [1, 219.21999999999997, 2061.12, 1189.884, 1234.916], [1, 219.21999999999997, 2061.12, 1255.7, 1300.732], [1, 219.21999999999997, 2061.12, 1321.516, 1366.548], [1, 219.21999999999997, 2061.12, 1387.3319999999999, 1432.364], [1, 225.99999999999997, 2061.12, 1454.8799999999999, 1499.912], [1, 219.21999999999997, 2061.12, 1520.696, 1565.728], [1, 225.99999999999997, 2043.0399999999997, 1586.512, 1631.544], [1, 2106.3199999999997, 2176.3799999999997, 1636.74, 1659.256], [1, 2090.5, 2142.48, 1669.648, 1692.164], [1, 2067.8999999999996, 2160.56, 1699.0919999999999, 1721.608], [1, 2067.8999999999996, 2160.56, 1699.0919999999999, 1721.608], [2, 10.98, 2026.9080000000001, 0.0, 1361.856], [3, 53.28, 477.30000000000007, 7.66, 27.576], [3, 53.28, 1491.8400000000001, 56.684, 85.792], [3, 2004.66, 2153.4, 55.152, 76.6], [3, 2004.66, 2191.1400000000003, 76.6, 98.048], [3, 59.940000000000005, 1276.5, 117.964, 142.476], [3, 1960.2600000000002, 2202.2400000000002, 111.836, 153.2], [3, 44.400000000000006, 122.10000000000001, 171.584, 196.096], [3, 304.14000000000004, 610.5, 223.672, 248.184], [3, 44.400000000000006, 68.82000000000001, 274.228, 295.676], [3, 304.14000000000004, 1194.3600000000001, 261.972, 332.444], [3, 35.52, 75.48, 387.596, 409.044], [3, 35.52, 173.16000000000003, 427.428, 448.87600000000003], [3, 35.52, 104.34, 459.6, 479.516], [3, 28.860000000000003, 73.26, 516.284, 536.2], [3, 31.080000000000002, 173.16000000000003, 556.116, 576.032], [3, 28.860000000000003, 102.12, 586.756, 606.672], [3, 28.860000000000003, 73.26, 641.908, 661.8240000000001], [3, 31.080000000000002, 173.16000000000003, 681.74, 701.6560000000001], [3, 28.860000000000003, 102.12, 712.38, 732.296], [3, 28.860000000000003, 173.16000000000003, 804.3000000000001, 824.216], [3, 28.860000000000003, 102.12, 834.94, 854.856], [3, 17.76, 113.22000000000001, 891.624, 913.072], [3, 26.64, 173.16000000000003, 931.456, 952.904], [3, 17.76, 104.34, 963.628, 983.544], [3, 159.84, 222.00000000000003, 1018.78, 1040.228], [3, 26.64, 173.16000000000003, 1058.612, 1080.06], [3, 17.76, 104.34, 1090.784, 1110.7], [3, 17.76, 79.92, 1145.936, 1165.852], [3, 26.64, 173.16000000000003, 1185.768, 1205.684], [3, 8.88, 108.78000000000002, 1216.4080000000001, 1236.324], [3, 8.88, 115.44000000000001, 1271.56, 1291.476], [3, 26.64, 173.16000000000003, 1311.392, 1331.308], [3, 8.88, 108.78000000000002, 1342.032, 1361.948], [3, 426.24, 2046.8400000000001, 347.764, 384.532], [3, 426.24, 2042.4, 404.448, 444.28000000000003], [3, 426.24, 2042.4, 462.664, 502.496], [3, 426.24, 632.7, 525.476, 563.7760000000001], [3, 426.24, 2042.4, 582.16, 621.992], [3, 426.24, 752.58, 641.908, 680.208], [3, 426.24, 1436.3400000000001, 700.124, 738.424], [3, 426.24, 592.74, 759.8720000000001, 796.64], [3, 501.72, 848.0400000000001, 818.088, 856.388], [3, 499.50000000000006, 1003.44, 876.304, 916.136], [3, 499.50000000000006, 810.3000000000001, 936.052, 975.884], [3, 499.50000000000006, 1003.44, 995.8000000000001, 1035.632], [3, 499.50000000000006, 694.86, 1055.548, 1093.848], [3, 499.50000000000006, 694.86, 1113.7640000000001, 1152.064], [3, 501.72, 694.86, 1173.512, 1211.8120000000001], [3, 501.72, 777.0000000000001, 1233.26, 1271.56], [3, 501.72, 927.96, 1291.476, 1331.308], [3, 1232.1000000000001, 1249.8600000000001, 1406.376, 1437.016]]
2026-08-06 10:28:04,313 INFO     30 [qwen-vl-text] ═══ DONE ═══ 87 positions, pages=4, time=111.5s
2026-08-06 10:28:04,346 INFO     30 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-06 10:28:04,348 INFO     30 [Trace] task=6a97f83c | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | Extractor:Admission | outputs={"chunks": "1 items, types={'AdmissionRecord': 1}", "html": "", "json": "309 items", "markdown": "", "text": "", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 5, \"chunks_LabExam\": 3}"}
2026-08-06 10:28:04,348 INFO     30 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-06 10:28:04,351 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:28:04.348+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 8, "lag": 0, "done": 0, "failed": 0, "current": {"6a97f83c918011f18dbe1f8f96f1c395": {"id": "6a97f83c918011f18dbe1f8f96f1c395", "doc_id": "688aee0a918011f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909798, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011615561, "task_type": "dataflow", "root_trace_id": "d05a3d8d0d6c4aa38394753a3ea0008c", "root_traceparent": "00-d05a3d8d0d6c4aa38394753a3ea0008c-2c380740bfb060e1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "00b9d592918111f18dbe1f8f96f1c395": {"id": "00b9d592918111f18dbe1f8f96f1c395", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011867426, "task_type": "dataflow", "root_trace_id": "1ab3198c92574fb4b2701d0f5db7322f", "root_traceparent": "00-1ab3198c92574fb4b2701d0f5db7322f-bdaff6f64a5f4a64-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:28:04,368 INFO     30 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 10:28:04,368 INFO     30 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-06 10:28:04,369 INFO     30 [qwen-vl-text] positions(24): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 10:28:04,369 INFO     30 [qwen-vl-text] page grouping: [4], lines per page: [24]
2026-08-06 10:28:05,712 INFO     30 [qwen-vl-text] page=4, rect=1292x1840, img=(3589x5112), dpi=200
2026-08-06 10:28:05,716 INFO     30 [qwen-vl-text] LLM extraction start, text_len=398
2026-08-06 10:28:05,717 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:28:05,717 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 90, \"bbox_end\": 113, \"encounter_dates\": [\"2025-01-26\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "信阳市中心医院\n免疫病理诊断报告\n免疫组化号：MT25-\n姓名：\n性别：女\n年龄：64岁\n送检医院：\n病区：肿瘤内科五护理单元[东病理号：D25-01313\n就诊卡号：\n住院号：2\n病区床号：21\n送检标本：肺手术标本\n送检时间：2025-01-24\n临床诊断：\n光镜所见：\n免疫病理诊断：\nCK广谱（点+），CD56（+），Syn（+），INSM1（+），CK5/6（-），P40（-），TTF1（+），\nNapsinA（-），Ki-67（80%+）。\n结合HE及免疫组化结果，（右中间段支气管）肺小细胞神经内分泌癌。\n初诊医师：刘磊\n复诊医师：刘磊\n报告日期：2025-01-26 10:49\n备注：1.本报告单仅供临床参考 2.如临床对报告内容有疑问请与报告医生联系。联系电话：0376-6227723(西院区)，0376-6667570(东院区)。\n3.此报告必须经过病理科医师签字有效。",
    "role": "user"
  }
]
2026-08-06 10:28:08,575 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:28:08,575 INFO     30 [qwen-vl-text] LLM output (len=469):
{
  "exam_date": "2025-01-24",
  "report_date": "2025-01-26",
  "exam_name": "免疫病理诊断报告",
  "exam_category": "pathology",
  "body_part": "右中间段支气管",
  "patient_name": null,
  "patient_gender": "女",
  "department": "肿瘤内科五护理单元",
  "bed_number": "21",
  "findings": "光镜所见：\n（原文此处无具体描述）",
  "conclusion": "免疫病理诊断：\nCK广谱（点+），CD56（+），Syn（+），INSM1（+），CK5/6（-），P40（-），TTF1（+），\nNapsinA（-），Ki-67（80%+）。\n结合HE及免疫组化结果，（右中间段支气管）肺小细胞神经内分泌癌。",
  "physician": "刘磊",
  "reviewer": "刘磊"
}
2026-08-06 10:28:08,602 INFO     30 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=6377978, prompt_len=1083
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
2026-08-06 10:28:09,925 INFO     30 [qwen-vl-parser] text API response (len=1155):
["三门峡市中心医院门户-患者360 ×", "← → C ① 不安全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView", "临床数据中心-患者360视图", "返回患者查询 患者姓名:", "女 出", "期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>", "就诊时间轴", "门诊号", "就诊时间: 2024-04-08 09 44 02 接诊科室: 妇科一病区(门) 接诊医生: 权丽丽", "全部 近一月 近三月 近半年 近一年", "近五年", "门诊 39 住院1", "总览 就诊列表", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告", "检验报告", "2025-04-11 哮喘危重—病达(I J)", "门诊号:", "2025-01-06 普通儿科三组 (...", "2024-12-30 普通儿科三组 (...", "2024-07-05 普通儿科一组 (...", "2024-04-24 普通儿科一组 (...", "2024-04-19 普通儿科一组 (...", "2024-04-08 妇科门诊", "2024-04-08 妇科一病区(门)", "2024-01-05 妇科一病区(门)", "2023-08-14 普通儿科三组 (...", "2023-07-06 普通儿科三组 (...", "姓名", "性别: 女", "年龄:40岁", "民族: 汉族", "身份证号", "现住址:", "就诊类型:初诊", "就诊科室:妇科一病区(门)", "就诊日期: 2024-04-08 09:44", "联系电话", "主诉: 月经期下腹间断疼痛2个月", "现病史: 2024.1月经第3天左侧附件区疼痛,超声提示无异常,输消炎药后好转,2024.2无异常,2024.3月经", "第3天下腹疼痛但是疼痛程度较前减轻,", "既往史: 平素体健,无高血压、冠心病、糖尿病病史,无肝炎、结核等传染病史,无手术史", "婚育史:", "月经史: 患者平素月经规律,量中等,色正常,无痛经。", "过敏史: 无", "专科检查: 外阴:发育正常,阴毛呈女性分布;阴道:通畅,粘膜红润,未见异常分泌物;宫颈:光滑,大小", "正常,宫体:正常大小,无压痛。附件:双侧附件区未触及明显异常。", "辅助检查:", "初步印象: 女性盆腔炎性疾病", "处理意见: 门诊检查", "备注:", "医师签名: 权丽丽", "第1页", ""]
2026-08-06 10:28:09,925 INFO     30 [qwen-vl-parser] page=19 text: 52 lines (bbox 1171-1222)
2026-08-06 10:28:09,925 INFO     30 [qwen-vl-parser] page=19 text: 52 sections
2026-08-06 10:28:10,210 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=986739, prompt_len=764
2026-08-06 10:28:17,292 INFO     30 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-04-08"}
```
2026-08-06 10:28:17,292 INFO     30 [qwen-vl-parser] page=20 classify=text report_date=2024-04-08
2026-08-06 10:28:17,319 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=986739, prompt_len=401
2026-08-06 10:28:25,170 INFO     30 [qwen-vl-parser] text API response (len=1047):
["三门峡市中心医院门户-患者360 ×", "临床数据中心-患者360视图", "返回患者查询", "患者姓", "出生", "期：2020-07-08", "最近诊疗日期：2026-02-12", "当前在院状态：出院", "过敏：无", "详情>>", "就诊时间抽", "1门诊号：", "就诊时间：2024-04-08 11:32:46", "接诊科室：妇科门诊", "接诊医生：曲丽霞", "全部", "近一月", "近三月", "近半年", "近一年", "近五年", "门诊诊39", "住院1", "就诊列表", "总览", "2025-04-11 收敛厄重—病区(1)", "2025-01-06 普通儿科三组 (", "2024-12-30 普通儿科三组 (", "2024-07-05 普通儿科一组 (", "2024-04-24 普通儿科一组 (", "2024-04-19 普通儿科一组 (", "2024-04-08 妇科门诊", "2024-04-08 妇科—病区(门)", "2024-01-05 妇科—病区(门)", "2023-08-14 普通儿科三组 (", "2023-07-06 普通儿科三组 (", "集成视图", "诊断", "病历文书", "处方", "检验", "检查", "处置", "肺功能检查", "单机报告", "体检报告", "门诊号", "姓名", "性别：女", "年龄：40岁", "民族：汉族", "身份证号", "现住址：", "就诊类型：初诊", "就诊科室：妇科门诊", "就诊日期：2024-04-08 11:32", "联系电话", "主诉：月经期下腹间断疼痛2个月", "现病史：2024.1月经第3天左侧附件区疼痛，超声提示无异常，输消炎药后好转，2024.2无异常，2024.3月经", "第3天下腹疼痛但是疼痛程度较前减轻，", "既往史：平素体健，无高血压、冠心病、糖尿病病史，无肝炎、结核等传染病史，无手术史", "婚育史：", "月经史：患者平素月经规律，量中等，色正常，无痛经。", "过敏史：无", "专科检查：外阴：发育正常，阴毛呈女性分布；阴道：通畅，粘膜红润，未见异常分泌物；宫颈：光滑，大小", "正常，宫体：正常大小，无压痛。附件：双侧附件区未触及明显异常。", "辅助检查：", "初步印象：女性盆腔炎性疾病", "处理意见：门诊检查", "备注：", "医师签名：", "第1页"]
2026-08-06 10:28:25,172 INFO     30 [qwen-vl-parser] page=20 text: 72 lines (bbox 1223-1294)
2026-08-06 10:28:25,172 INFO     30 [qwen-vl-parser] page=20 text: 72 sections
2026-08-06 10:28:25,500 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=802759, prompt_len=764
2026-08-06 10:28:25,793 INFO     30 [qwen-vl-text] coord API raw response (len=1439):
[
	{"text": "信阳市中心医院", "bbox": [355, 24, 609, 51]},
	{"text": "免疫病理诊断报告", "bbox": [376, 65, 595, 85]},
	{"text": "免疫组化号：MT25-", "bbox": [620, 98, 803, 114]},
	{"text": "姓名：", "bbox": [58, 127, 130, 144]},
	{"text": "性别：女", "bbox": [348, 126, 467, 143]},
	{"text": "年龄：64岁", "bbox": [641, 125, 792, 141]},
	{"text": "送检医院：", "bbox": [58, 156, 150, 173]},
	{"text": "病区：肿瘤内科五护理单元[东病理号：D25-01313", "bbox": [348, 154, 828, 171]},
	{"text": "就诊卡号：", "bbox": [58, 184, 150, 201]},
	{"text": "住院号：2", "bbox": [348, 183, 442, 200]},
	{"text": "病区床号：21", "bbox": [641, 183, 759, 199]},
	{"text": "送检标本：肺手术标本", "bbox": [58, 212, 252, 229]},
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
2026-08-06 10:28:25,794 INFO     30 [qwen-vl-text] coord API: raw_items=24, valid_items=24, elapsed=17.2s
2026-08-06 10:28:25,794 INFO     30 [qwen-vl-text] coord item[0]: text=信阳市中心医院, bbox=[355, 24, 609, 51]
2026-08-06 10:28:25,794 INFO     30 [qwen-vl-text] coord item[1]: text=免疫病理诊断报告, bbox=[376, 65, 595, 85]
2026-08-06 10:28:25,794 INFO     30 [qwen-vl-text] coord item[2]: text=免疫组化号：MT25-, bbox=[620, 98, 803, 114]
2026-08-06 10:28:25,794 INFO     30 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[58, 127, 130, 144]
2026-08-06 10:28:25,795 INFO     30 [qwen-vl-text] coord item[4]: text=性别：女, bbox=[348, 126, 467, 143]
2026-08-06 10:28:25,795 INFO     30 [qwen-vl-text] coord item[5]: text=年龄：64岁, bbox=[641, 125, 792, 141]
2026-08-06 10:28:25,795 INFO     30 [qwen-vl-text] coord item[6]: text=送检医院：, bbox=[58, 156, 150, 173]
2026-08-06 10:28:25,795 INFO     30 [qwen-vl-text] coord item[7]: text=病区：肿瘤内科五护理单元[东病理号：D25-01313, bbox=[348, 154, 828, 171]
2026-08-06 10:28:25,795 INFO     30 [qwen-vl-text] coord item[8]: text=就诊卡号：, bbox=[58, 184, 150, 201]
2026-08-06 10:28:25,795 INFO     30 [qwen-vl-text] coord item[9]: text=住院号：2, bbox=[348, 183, 442, 200]
2026-08-06 10:28:25,796 INFO     30 [qwen-vl-text] coord item[10]: text=病区床号：21, bbox=[641, 183, 759, 199]
2026-08-06 10:28:25,796 INFO     30 [qwen-vl-text] coord item[11]: text=送检标本：肺手术标本, bbox=[58, 212, 252, 229]
2026-08-06 10:28:25,796 INFO     30 [qwen-vl-text] coord item[12]: text=送检时间：2025-01-24, bbox=[327, 212, 530, 228]
2026-08-06 10:28:25,796 INFO     30 [qwen-vl-text] coord item[13]: text=临床诊断：, bbox=[58, 241, 150, 258]
2026-08-06 10:28:25,796 INFO     30 [qwen-vl-text] coord item[14]: text=光镜所见：, bbox=[57, 295, 153, 312]
2026-08-06 10:28:25,796 INFO     30 [qwen-vl-text] coord item[15]: text=免疫病理诊断：, bbox=[60, 567, 200, 583]
2026-08-06 10:28:25,797 INFO     30 [qwen-vl-text] coord item[16]: text=CK广谱（点+），CD56（+），Syn（+），INSM1（+），CK5/6（-），P40（-），TTF1（+），, bbox=[74, 599, 807, 615]
2026-08-06 10:28:25,797 INFO     30 [qwen-vl-text] coord item[17]: text=NapsinA（-），Ki-67（80%+）。, bbox=[74, 614, 360, 629]
2026-08-06 10:28:25,797 INFO     30 [qwen-vl-text] coord item[18]: text=结合HE及免疫组化结果，（右中间段支气管）肺小细胞神经内分泌癌。, bbox=[74, 628, 670, 645]
2026-08-06 10:28:25,797 INFO     30 [qwen-vl-text] coord item[19]: text=初诊医师：刘磊, bbox=[58, 803, 197, 820]
2026-08-06 10:28:25,797 INFO     30 [qwen-vl-text] coord item[20]: text=复诊医师：刘磊, bbox=[333, 803, 468, 820]
2026-08-06 10:28:25,797 INFO     30 [qwen-vl-text] coord item[21]: text=报告日期：2025-01-26 10:49, bbox=[615, 803, 870, 820]
2026-08-06 10:28:25,797 INFO     30 [qwen-vl-text] coord item[22]: text=备注：1.本报告单仅供临床参考 2.如临床对报告内容有疑问请与报告医生联系。联系电话：0376-6227723(西院区)，0376-6667570(东院区)。, bbox=[64, 872, 962, 887]
2026-08-06 10:28:25,798 INFO     30 [qwen-vl-text] coord item[23]: text=3.此报告必须经过病理科医师签字有效。, bbox=[98, 896, 363, 909]
2026-08-06 10:28:25,804 INFO     30 [qwen-vl-text] page=4 — 24/24 coords, api_time=17.2s
2026-08-06 10:28:25,805 INFO     30 [qwen-vl-text] new_positions (24):
[[4, 458.66, 786.828, 44.160000000000004, 93.84], [4, 485.79200000000003, 768.74, 119.60000000000001, 156.4], [4, 801.0400000000001, 1037.476, 180.32000000000002, 209.76000000000002], [4, 74.936, 167.96, 233.68, 264.96000000000004], [4, 449.616, 603.364, 231.84, 263.12], [4, 828.172, 1023.264, 230.0, 259.44], [4, 74.936, 193.8, 287.04, 318.32], [4, 449.616, 1069.776, 283.36, 314.64], [4, 74.936, 193.8, 338.56, 369.84000000000003], [4, 449.616, 571.064, 336.72, 368.0], [4, 828.172, 980.628, 336.72, 366.16], [4, 74.936, 325.584, 390.08000000000004, 421.36], [4, 422.48400000000004, 684.76, 390.08000000000004, 419.52000000000004], [4, 74.936, 193.8, 443.44, 474.72], [4, 73.644, 197.67600000000002, 542.8000000000001, 574.08], [4, 77.52, 258.40000000000003, 1043.28, 1072.72], [4, 95.608, 1042.644, 1102.16, 1131.6000000000001], [4, 95.608, 465.12, 1129.76, 1157.3600000000001], [4, 95.608, 865.64, 1155.52, 1186.8], [4, 74.936, 254.524, 1477.52, 1508.8], [4, 430.236, 604.6560000000001, 1477.52, 1508.8], [4, 794.58, 1124.04, 1477.52, 1508.8], [4, 82.688, 1242.904, 1604.48, 1632.0800000000002], [4, 126.616, 468.99600000000004, 1648.64, 1672.5600000000002]]
2026-08-06 10:28:25,805 INFO     30 [qwen-vl-text] ═══ DONE ═══ 24 positions, pages=1, time=21.4s
2026-08-06 10:28:25,806 INFO     30 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 10:28:25,806 INFO     30 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-06 10:28:25,807 INFO     30 [qwen-vl-text] positions(22): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 10:28:25,807 INFO     30 [qwen-vl-text] page grouping: [5], lines per page: [22]
2026-08-06 10:28:26,885 INFO     30 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-04-19"}
```
2026-08-06 10:28:26,891 INFO     30 [qwen-vl-parser] page=21 classify=text report_date=2024-04-19
2026-08-06 10:28:26,892 INFO     30 [qwen-vl-text] page=5, rect=1232x1744, img=(3423x4845), dpi=200
2026-08-06 10:28:26,895 INFO     30 [qwen-vl-text] LLM extraction start, text_len=314
2026-08-06 10:28:26,895 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:28:26,896 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 114, \"bbox_end\": 135, \"encounter_dates\": [\"2025-01-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "信阳市中心医院\n病理检查报告单\n病理号：D25\n姓名：\n性别：女\n年龄：64岁\n送检医院：\n送检科室：呼吸与危重症医学科送检日期：2025-01-22\n门诊号：9\n住院号：25\n床号：21\n送检医师：周鹏飞\n送检标本：右中间段支气管\n临床诊断：\n巨检：灰白色碎组织最大径0.3厘米。全取\n病理诊断：\n(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。\n初诊医师：刘晶晶\n复诊医师：刘磊\n报告日期：2025-01-23 19:26\n备注：1.本报告单仅供临床参考 2.如临床对报告内容有疑问请与报告医生联系。联系电话：0376-6227723(西院区)；0376-6667570(东院区)。\n3.此报告必须经过病理科医师签字有效。",
    "role": "user"
  }
]
2026-08-06 10:28:26,922 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=802759, prompt_len=401
2026-08-06 10:28:29,132 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:28:29,132 INFO     30 [qwen-vl-text] LLM output (len=378):
{
  "exam_date": "2025-01-22",
  "report_date": "2025-01-23",
  "exam_name": "病理检查报告单",
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
2026-08-06 10:28:29,195 INFO     30 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=6423871, prompt_len=993
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
2026-08-06 10:28:32,816 INFO     30 [qwen-vl-parser] text API response (len=1051):
["<", "→", "C", "① 不安全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView", "临床数据中心-患者360视图", "返回患者查询", "患者姓", "女", "出生日期", "首诊日期：2020-07-08", "最近诊疗日期：2026-02-12", "当前在院状态：出院", "过敏：无", "详情>>", "就诊时间抽", "门诊号", "就诊时间：2024-04-19 08.07.40", "接诊科室：普通儿科一组(门)", "接诊医生：李婉莹", "全部", "近一月", "近三月", "近半年", "近一年", "近五年", "■ 门诊诊39", "住院1", "总览", "就诊列表", "2025-04-11 守议危重_病区(IJ)", "2025-01-06 普通儿科三组(...", "2024-12-30 普通儿科三组(...", "2024-07-05 普通儿科一组(...", "2024-04-24 普通儿科一组(...", "2024-04-19 普通儿科一组(...", "2024-04-08 妇科门诊", "2024-04-08 妇科一病区(门)", "2024-01-05 妇科一病区(门)", "2023-08-14 普通儿科三组(...", "2023-07-06 普通儿科三组(...", "集成视图", "诊断", "病历文书", "处方", "检验", "检查", "处置", "肺功能检查", "单机报告", "体检报告", "门诊号", "姓", "性别：女", "年龄：40岁", "民族：汉族", "身份证号：", "现住址：", "就诊类型：急诊", "就诊科室：普通儿科一组(门)", "就诊日期：2024-04-19 08:07", "联系电话", "主诉：因呼吸道感染）不适要求开药", "现病史：患者因（呼吸道感染）不适，要求开药（家属代开）。", "既往史：既往体质一般", "过敏史：无", "体格检查：神志清晰，精神一般，自主体位，查体合作", "辅助检查：", "初步印象：1、急性上呼吸道感染.2、维生素A缺乏伴夜盲症", "处理意见：开立药品", "备注：", "医师签名：李婉莹", "第1页", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-06 10:28:32,816 INFO     30 [qwen-vl-parser] page=21 text: 74 lines (bbox 1295-1368)
2026-08-06 10:28:32,817 INFO     30 [qwen-vl-parser] page=21 text: 74 sections
2026-08-06 10:28:33,124 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=986805, prompt_len=764
2026-08-06 10:28:38,923 INFO     30 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-04-11"}
```
2026-08-06 10:28:38,924 INFO     30 [qwen-vl-parser] page=22 classify=text report_date=2025-04-11
2026-08-06 10:28:38,961 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=986805, prompt_len=401
2026-08-06 10:28:46,011 INFO     30 [qwen-vl-parser] text API response (len=1026):
["临床数据中心-患者360视图", "返回患者查询", "患者姓", "别：女", "出生日期：", "就诊日期：2020-07-08", "最近诊疗日期：2026-02-12", "当前在院状态：出院", "过敏：无", "详情>>", "就诊时间：2025-04-11 14:47:07", "接诊科室：呼吸危重二病区(门)", "接诊医生：段竹云", "全部", "近一月", "近三月", "近半年", "近一年", "近五年", "门诊39", "住院1", "总览", "就诊列表", "2025-06-23 普通儿科三组 (...", "2025-05-09 呼吸危重二病区(门)", "2025-04-11 耳鼻咽喉头颈外...", "2025-04-11 呼吸危重二病区(门)", "2025-01-06 普通儿科三组 (...", "2024-12-30 普通儿科三组 (...", "2024-07-05 普通儿科一组 (...", "2024-04-24 普通儿科一组 (...", "2024-04-19 普通儿科一组 (...", "2024-04-08 妇科门诊", "2024-04-08 妇科一病区(门)", "集成视图", "诊断", "病历文书", "处方", "检验", "检查", "处置", "肺功能检查", "单机报告", "透析治疗", "费用", "体检报告", "（总）诊病历", "门诊号：", "姓", "性别：女", "年龄：41岁", "民族：汉族", "婚姻状况：已婚", "身份证", "职业：专业技术人员", "现住址：", "就诊类型：初诊", "就诊科室：呼吸危重二病区(门)", "就诊日期：2025-04-11", "14:47", "联系电话：", "主诉：咳嗽憋气一周", "现病史：患者无发热，感冒后咳嗽、憋气一周，间断治疗，时轻时重，今日来诊", "既往史：平素体健，无高血压、冠心病、糖尿病病史", "个人史：无吸烟史", "过敏史：无", "体格检查：呼吸平稳，口唇无紫绀，听诊：双肺呼吸音清，未闻及干、湿性啰音", "辅助检查：肺功能检查提示中重度阻塞性肺通气功能障碍，支气管舒张试验阳性。", "初步印象：1、支气管哮喘(急性发作期).2、过敏性鼻炎[变应性鼻炎]", "处理意见：坚持门诊治疗，定期复查", "备注：", "医师签名：段竹云", "第1页"]
2026-08-06 10:28:46,013 INFO     30 [qwen-vl-parser] page=22 text: 73 lines (bbox 1369-1441)
2026-08-06 10:28:46,013 INFO     30 [qwen-vl-parser] page=22 text: 73 sections
2026-08-06 10:28:46,331 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=935536, prompt_len=764
2026-08-06 10:28:46,514 INFO     30 [qwen-vl-text] coord API raw response (len=1279):
[
	{"text": "信阳市中心医院", "bbox": [380, 28, 638, 56]},
	{"text": "病理检查报告单", "bbox": [409, 63, 607, 84]},
	{"text": "病理号：D25", "bbox": [705, 98, 820, 115]},
	{"text": "姓名：", "bbox": [100, 128, 182, 146]},
	{"text": "性别：女", "bbox": [392, 126, 514, 144]},
	{"text": "年龄：64岁", "bbox": [693, 125, 841, 143]},
	{"text": "送检医院：", "bbox": [100, 153, 190, 170]},
	{"text": "送检科室：呼吸与危重症医学科送检日期：2025-01-22", "bbox": [392, 150, 902, 168]},
	{"text": "门诊号：9", "bbox": [100, 177, 218, 195]},
	{"text": "住院号：25", "bbox": [392, 175, 514, 193]},
	{"text": "床号：21", "bbox": [691, 175, 798, 192]},
	{"text": "送检医师：周鹏飞", "bbox": [100, 203, 264, 221]},
	{"text": "送检标本：右中间段支气管", "bbox": [392, 202, 633, 220]},
	{"text": "临床诊断：", "bbox": [100, 228, 190, 246]},
	{"text": "巨检：灰白色碎组织最大径0.3厘米。全取", "bbox": [103, 276, 474, 294]},
	{"text": "病理诊断：", "bbox": [113, 572, 208, 589]},
	{"text": "(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。", "bbox": [154, 588, 622, 606]},
	{"text": "初诊医师：刘晶晶", "bbox": [102, 860, 256, 878]},
	{"text": "复诊医师：刘磊", "bbox": [379, 859, 505, 876]},
	{"text": "报告日期：2025-01-23 19:26", "bbox": [656, 858, 920, 876]},
	{"text": "备注：1.本报告单仅供临床参考 2.如临床对报告内容有疑问请与报告医生联系。联系电话：0376-6227723(西院区)；0376-6667570(东院区)。", "bbox": [99, 899, 997, 914]},
	{"text": "3.此报告必须经过病理科医师签字有效。", "bbox": [144, 915, 407, 929]}
]
2026-08-06 10:28:46,515 INFO     30 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=17.3s
2026-08-06 10:28:46,515 INFO     30 [qwen-vl-text] coord item[0]: text=信阳市中心医院, bbox=[380, 28, 638, 56]
2026-08-06 10:28:46,516 INFO     30 [qwen-vl-text] coord item[1]: text=病理检查报告单, bbox=[409, 63, 607, 84]
2026-08-06 10:28:46,516 INFO     30 [qwen-vl-text] coord item[2]: text=病理号：D25, bbox=[705, 98, 820, 115]
2026-08-06 10:28:46,516 INFO     30 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[100, 128, 182, 146]
2026-08-06 10:28:46,516 INFO     30 [qwen-vl-text] coord item[4]: text=性别：女, bbox=[392, 126, 514, 144]
2026-08-06 10:28:46,517 INFO     30 [qwen-vl-text] coord item[5]: text=年龄：64岁, bbox=[693, 125, 841, 143]
2026-08-06 10:28:46,517 INFO     30 [qwen-vl-text] coord item[6]: text=送检医院：, bbox=[100, 153, 190, 170]
2026-08-06 10:28:46,517 INFO     30 [qwen-vl-text] coord item[7]: text=送检科室：呼吸与危重症医学科送检日期：2025-01-22, bbox=[392, 150, 902, 168]
2026-08-06 10:28:46,517 INFO     30 [qwen-vl-text] coord item[8]: text=门诊号：9, bbox=[100, 177, 218, 195]
2026-08-06 10:28:46,517 INFO     30 [qwen-vl-text] coord item[9]: text=住院号：25, bbox=[392, 175, 514, 193]
2026-08-06 10:28:46,517 INFO     30 [qwen-vl-text] coord item[10]: text=床号：21, bbox=[691, 175, 798, 192]
2026-08-06 10:28:46,517 INFO     30 [qwen-vl-text] coord item[11]: text=送检医师：周鹏飞, bbox=[100, 203, 264, 221]
2026-08-06 10:28:46,517 INFO     30 [qwen-vl-text] coord item[12]: text=送检标本：右中间段支气管, bbox=[392, 202, 633, 220]
2026-08-06 10:28:46,518 INFO     30 [qwen-vl-text] coord item[13]: text=临床诊断：, bbox=[100, 228, 190, 246]
2026-08-06 10:28:46,518 INFO     30 [qwen-vl-text] coord item[14]: text=巨检：灰白色碎组织最大径0.3厘米。全取, bbox=[103, 276, 474, 294]
2026-08-06 10:28:46,518 INFO     30 [qwen-vl-text] coord item[15]: text=病理诊断：, bbox=[113, 572, 208, 589]
2026-08-06 10:28:46,518 INFO     30 [qwen-vl-text] coord item[16]: text=(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。, bbox=[154, 588, 622, 606]
2026-08-06 10:28:46,518 INFO     30 [qwen-vl-text] coord item[17]: text=初诊医师：刘晶晶, bbox=[102, 860, 256, 878]
2026-08-06 10:28:46,518 INFO     30 [qwen-vl-text] coord item[18]: text=复诊医师：刘磊, bbox=[379, 859, 505, 876]
2026-08-06 10:28:46,518 INFO     30 [qwen-vl-text] coord item[19]: text=报告日期：2025-01-23 19:26, bbox=[656, 858, 920, 876]
2026-08-06 10:28:46,518 INFO     30 [qwen-vl-text] coord item[20]: text=备注：1.本报告单仅供临床参考 2.如临床对报告内容有疑问请与报告医生联系。联系电话：0376-6227723(西院区)；0376-6667570(东院区)。, bbox=[99, 899, 997, 914]
2026-08-06 10:28:46,518 INFO     30 [qwen-vl-text] coord item[21]: text=3.此报告必须经过病理科医师签字有效。, bbox=[144, 915, 407, 929]
2026-08-06 10:28:46,523 INFO     30 [qwen-vl-text] page=5 — 22/22 coords, api_time=17.3s
2026-08-06 10:28:46,524 INFO     30 [qwen-vl-text] new_positions (22):
[[5, 468.15999999999997, 786.016, 48.832, 97.664], [5, 503.888, 747.824, 109.872, 146.496], [5, 868.56, 1010.24, 170.912, 200.56], [5, 123.2, 224.224, 223.232, 254.624], [5, 482.944, 633.248, 219.744, 251.136], [5, 853.776, 1036.112, 218.0, 249.392], [5, 123.2, 234.07999999999998, 266.832, 296.48], [5, 482.944, 1111.264, 261.6, 292.992], [5, 123.2, 268.576, 308.688, 340.08], [5, 482.944, 633.248, 305.2, 336.592], [5, 851.312, 983.136, 305.2, 334.848], [5, 123.2, 325.248, 354.032, 385.424], [5, 482.944, 779.856, 352.288, 383.68], [5, 123.2, 234.07999999999998, 397.632, 429.024], [5, 126.896, 583.968, 481.344, 512.736], [5, 139.216, 256.256, 997.568, 1027.216], [5, 189.728, 766.304, 1025.472, 1056.864], [5, 125.664, 315.392, 1499.84, 1531.232], [5, 466.928, 622.16, 1498.096, 1527.744], [5, 808.192, 1133.44, 1496.352, 1527.744], [5, 121.968, 1228.304, 1567.856, 1594.016], [5, 177.408, 501.424, 1595.76, 1620.176]]
2026-08-06 10:28:46,524 INFO     30 [qwen-vl-text] ═══ DONE ═══ 22 positions, pages=1, time=20.7s
2026-08-06 10:28:46,524 INFO     30 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 10:28:46,525 INFO     30 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-06 10:28:46,525 INFO     30 [qwen-vl-text] positions(39): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 10:28:46,525 INFO     30 [qwen-vl-text] page grouping: [6], lines per page: [39]
2026-08-06 10:28:47,758 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:28:47,762 INFO     30 [qwen-vl-text] page=6, rect=1220x1696, img=(3389x4712), dpi=200
2026-08-06 10:28:47,762 INFO     30 [qwen-vl-parser] page=23 classify=text report_date=None
2026-08-06 10:28:47,776 INFO     30 [qwen-vl-text] LLM extraction start, text_len=765
2026-08-06 10:28:47,777 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:28:47,778 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 136, \"bbox_end\": 174, \"encounter_dates\": [\"2025-12-22\"], \"department\": \"日间化疗中心[东院区]\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "信阳市中心医院\n影像科CT诊断报告书\n扫描\n获取电子胶\n片和报告(试用)\n影像号: 000\n报告日期: 2025-12-22 16:36\n姓名:\n性别: 女\n年龄: 64岁\n检查日期: 2025-12-22\n科别: 日间化疗中心[东院区]院号: 2\n门诊号:/\n检查时间: 09:53:10\n检查方法: 胸部CT平扫,胸部CT增强,上腹部CT平扫,上腹部CT增强,下腹部CT平扫,下腹部CT增强\n技术参数:\n影像学所见:\n双侧胸廓对称,右肺门增大,可见不规则状软组织密度影,密度不均,边\n界不清,强化不均,右肺中下叶支气管稍变窄,双肺可见条索状及结节状高密\n度影,较大病灶位于右肺下叶内基底段见实性结节,大小约为15.8×15.4mm,\n轻度强化。右肺中叶局限性支扩。气管、支气管通畅,右肺门见明显肿大淋巴\n结,轻度强化,双侧胸膜腔及心包腔可见积液征象。与2025-8-21日片比较:\n双侧胸腔积液增多,心包积液新增,右肺门软组织密度影及淋巴结增大。\n肝脏未见明显异常密度及异常强化征象,胆囊内隐约见斑点状高密度影,\n脾脏见数个小灶状低强化影。胰腺形态、大小、密度正常。双肾见小圆形低密\n度影,边界清,增强未见明显强化。腹膜后未见明显增大淋巴结,腹腔未见明\n显积液征象。升结肠见多发小囊袋状外凸影。与2025-8-21日片比较:大致相\n仿。\n影像学意见:\n1. 右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节,转移瘤可能;建\n议追踪复查:右肺门肿大淋巴结。\n2. 双肺慢性炎症,右肺中叶局限性支扩,双侧胸腔积液,心包积液。\n3. 脾脏低密度灶,建议追踪复查。\n4. 胆囊可疑小结石。升结肠多发憩室。\n5. 双肾小囊肿。\n报告医师:\n审核医师:\n此报告仅供临床医师参考,签字生效\n打印时间: 2025-12-22 16:36:26",
    "role": "user"
  }
]
2026-08-06 10:28:47,793 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:28:47.788+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 8, "lag": 0, "done": 0, "failed": 0, "current": {"6a97f83c918011f18dbe1f8f96f1c395": {"id": "6a97f83c918011f18dbe1f8f96f1c395", "doc_id": "688aee0a918011f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909798, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011615561, "task_type": "dataflow", "root_trace_id": "d05a3d8d0d6c4aa38394753a3ea0008c", "root_traceparent": "00-d05a3d8d0d6c4aa38394753a3ea0008c-2c380740bfb060e1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "00b9d592918111f18dbe1f8f96f1c395": {"id": "00b9d592918111f18dbe1f8f96f1c395", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011867426, "task_type": "dataflow", "root_trace_id": "1ab3198c92574fb4b2701d0f5db7322f", "root_traceparent": "00-1ab3198c92574fb4b2701d0f5db7322f-bdaff6f64a5f4a64-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:28:47,863 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=935536, prompt_len=401
2026-08-06 10:28:52,978 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:28:52,979 INFO     30 [qwen-vl-text] LLM output (len=872):
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
  "findings": "双侧胸廓对称,右肺门增大,可见不规则状软组织密度影,密度不均,边\n界不清,强化不均,右肺中下叶支气管稍变窄,双肺可见条索状及结节状高密\n度影,较大病灶位于右肺下叶内基底段见实性结节,大小约为15.8×15.4mm,\n轻度强化。右肺中叶局限性支扩。气管、支气管通畅,右肺门见明显肿大淋巴\n结,轻度强化,双侧胸膜腔及心包腔可见积液征象。与2025-8-21日片比较:\n双侧胸腔积液增多,心包积液新增,右肺门软组织密度影及淋巴结增大。\n肝脏未见明显异常密度及异常强化征象,胆囊内隐约见斑点状高密度影,\n脾脏见数个小灶状低强化影。胰腺形态、大小、密度正常。双肾见小圆形低密\n度影,边界清,增强未见明显强化。腹膜后未见明显增大淋巴结,腹腔未见明\n显积液征象。升结肠见多发小囊袋状外凸影。与2025-8-21日片比较:大致相\n仿。",
  "conclusion": "1. 右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节,转移瘤可能;建\n议追踪复查:右肺门肿大淋巴结。\n2. 双肺慢性炎症,右肺中叶局限性支扩,双侧胸腔积液,心包积液。\n3. 脾脏低密度灶,建议追踪复查。\n4. 胆囊可疑小结石。升结肠多发憩室。\n5. 双肾小囊肿。",
  "physician": null,
  "reviewer": null
}
2026-08-06 10:28:53,037 INFO     30 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=5385022, prompt_len=1495
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
2026-08-06 10:28:53,378 INFO     30 [qwen-vl-parser] text API response (len=911):
["临床数据中心-患者360视图", "返回患者查询", "就诊时间抽", "近五年", "门诊39 住院1", "就诊列表", "2025-06-23 普通儿科三组 (...", "2025-05-09 呼吸危重二病区(门)", "2025-04-11 耳鼻咽喉头颈外", "2025-04-11 呼吸危重二病区(门)", "2025-01-06 普通儿科三组 (...", "2024-12-30 普通儿科三组 (...", "2024-07-05 普通儿科一组 (...", "2024-04-24 普通儿科一组 (...", "2024-04-19 普通儿科一组 (...", "2024-04-08 妇科门诊", "2024-04-08 妇科一病区(门)", "]: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>", "就诊时间: 2025-04-11 15:43:29 接诊科室: 耳鼻咽喉头颈外科(门) 接诊医生: 刘秀层", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 报告", "门诊病历", "门诊号", "姓名", "性别: 女", "年龄:41岁", "民族: 汉族", "婚姻状况: 已婚", "身份证号", "职业: 职员", "现住址:", "就诊类型: 初诊", "就诊科室:耳鼻咽喉头颈外科", "就诊日期: 2025-04-11 15:43", "联系电", "主诉:鼻塞流涕,咳嗽憋气1周", "现病史:1周前发现鼻塞流涕,患者无发热,感冒后咳嗽、憋气,间断治疗,时轻时重,今日来诊", "既往史:平素体健,无高血压、冠心病、糖尿病病史", "家族史:无家族遗传病史", "过敏史:无", "体格检查:鼻腔粘膜充血,水肿,水样分泌物附着", "辅助检查:肺功能检查提示中重度阻塞性肺通气功能障碍,支气管舒张试验阳性。", "初步印象:1、支气管哮喘(急性发作期)2、过敏性鼻炎[变应性鼻炎]", "处理意见:坚持门诊治疗,定期复查", "备注:", "医师签名:刘秀层", "第1页"]
2026-08-06 10:28:53,381 INFO     30 [qwen-vl-parser] page=23 text: 46 lines (bbox 1442-1487)
2026-08-06 10:28:53,381 INFO     30 [qwen-vl-parser] page=23 text: 46 sections
2026-08-06 10:28:53,773 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=969703, prompt_len=764
2026-08-06 10:29:00,988 INFO     30 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-05-09"}
```
2026-08-06 10:29:00,989 INFO     30 [qwen-vl-parser] page=24 classify=text report_date=2025-05-09
2026-08-06 10:29:01,009 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=969703, prompt_len=401
2026-08-06 10:29:09,027 INFO     30 [qwen-vl-parser] text API response (len=1079):
["三门峡市中心医院门户-患者360 ×", "+", "← → C ① 不安全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView", "临床数据中心-患者360视图", "返回患者查询 患者姓名 : 女 出生日期", "日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>", "就诊时间轴 门诊号", "就诊时间: 2025-05-09 17 00 57 接诊科室: 呼吸危重二病区(门) 接诊医生: 段竹云", "全部 近一月 近三月 近半年 近一年", "近五年", "■ 门急诊39 住院1", "总览 就诊列表", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 体检报告", "11(急)诊病历", "门诊号:", "2025-11-27 普通儿科二区(...", "2025-11-24 普通儿科二区(...", "2025-09-18 普通儿科二区(...", "2025-07-11 普通儿科一组(...", "2025-06-23 普通儿科三组(...", "2025-05-09 呼吸危重二病区(门)", "2025-04-11 耳鼻咽喉头颈外...", "2025-04-11 呼吸危重二病区(门)", "2025-01-06 普通儿科三组(...", "2024-12-30 普通儿科三组(...", "2024-07-05 普通儿科一组(...", "性别:女", "年龄:41岁", "民族:汉族", "婚姻状况:已婚", "身份证", "业:专业技术人员", "现住址:", "就诊类型:复诊", "就诊科室:呼吸危重二病区(门)", "就诊日期:2025-05-09", "17:00", "联系电话", "主诉:咳嗽憋气一周", "现病史:患者无发热,感冒后咳嗽、憋气一周,间断治疗,时轻时重,今日来诊", "既往史:平素体健,无高血压、冠心病、糖尿病病史", "个人史:无吸烟史", "过敏史:无", "体格检查:听诊:双肺呼吸音清,未闻及干、湿性啰音", "辅助检查:肺功能检查提示中重度阻塞性肺通气功能障碍,支气管舒张试验阳性。", "初步印象:1、支气管哮喘.2、过敏性鼻炎[变应性鼻炎]", "处理意见:坚持门诊治疗,定期复查", "备注:", "医师签名:段竹云", "第1页"]
2026-08-06 10:29:09,028 INFO     30 [qwen-vl-parser] page=24 text: 49 lines (bbox 1488-1536)
2026-08-06 10:29:09,029 INFO     30 [qwen-vl-parser] page=24 text: 49 sections
2026-08-06 10:29:09,366 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=735011, prompt_len=764
2026-08-06 10:29:10,882 INFO     30 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-06-23"}
```
2026-08-06 10:29:10,883 INFO     30 [qwen-vl-parser] page=25 classify=text report_date=2025-06-23
2026-08-06 10:29:10,919 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=735011, prompt_len=401
2026-08-06 10:29:17,263 INFO     30 [qwen-vl-text] coord API raw response (len=2475):
[
	{"text": "信阳市中心医院", "bbox": [401, 76, 610, 100]},
	{"text": "影像科CT诊断报告书", "bbox": [371, 116, 640, 139]},
	{"text": "扫描", "bbox": [703, 143, 735, 155]},
	{"text": "获取电子胶", "bbox": [837, 141, 902, 154]},
	{"text": "片和报告(试用)", "bbox": [703, 155, 807, 168]},
	{"text": "影像号: 000", "bbox": [92, 179, 204, 193]},
	{"text": "报告日期: 2025-12-22 16:36", "bbox": [502, 173, 744, 188]},
	{"text": "姓名:", "bbox": [96, 203, 140, 217]},
	{"text": "性别: 女", "bbox": [328, 202, 400, 216]},
	{"text": "年龄: 64岁", "bbox": [444, 200, 535, 214]},
	{"text": "检查日期: 2025-12-22", "bbox": [651, 199, 843, 213]},
	{"text": "科别: 日间化疗中心[东院区]院号: 2", "bbox": [96, 225, 405, 241]},
	{"text": "门诊号:/", "bbox": [464, 223, 538, 238]},
	{"text": "检查时间: 09:53:10", "bbox": [655, 222, 827, 237]},
	{"text": "检查方法: 胸部CT平扫,胸部CT增强,上腹部CT平扫,上腹部CT增强,下腹部CT平扫,下腹部CT增强", "bbox": [96, 251, 889, 268]},
	{"text": "技术参数:", "bbox": [96, 280, 197, 298]},
	{"text": "影像学所见:", "bbox": [96, 306, 221, 324]},
	{"text": "双侧胸廓对称,右肺门增大,可见不规则状软组织密度影,密度不均,边", "bbox": [135, 326, 930, 345]},
	{"text": "界不清,强化不均,右肺中下叶支气管稍变窄,双肺可见条索状及结节状高密", "bbox": [135, 348, 929, 367]},
	{"text": "度影,较大病灶位于右肺下叶内基底段见实性结节,大小约为15.8×15.4mm,", "bbox": [135, 369, 915, 388]},
	{"text": "轻度强化。右肺中叶局限性支扩。气管、支气管通畅,右肺门见明显肿大淋巴", "bbox": [135, 390, 929, 409]},
	{"text": "结,轻度强化,双侧胸膜腔及心包腔可见积液征象。与2025-8-21日片比较:", "bbox": [135, 411, 904, 430]},
	{"text": "双侧胸腔积液增多,心包积液新增,右肺门软组织密度影及淋巴结增大。", "bbox": [135, 433, 868, 452]},
	{"text": "肝脏未见明显异常密度及异常强化征象,胆囊内隐约见斑点状高密度影,", "bbox": [135, 454, 915, 473]},
	{"text": "脾脏见数个小灶状低强化影。胰腺形态、大小、密度正常。双肾见小圆形低密", "bbox": [135, 475, 928, 494]},
	{"text": "度影,边界清,增强未见明显强化。腹膜后未见明显增大淋巴结,腹腔未见明", "bbox": [135, 496, 928, 515]},
	{"text": "显积液征象。升结肠见多发小囊袋状外凸影。与2025-8-21日片比较:大致相", "bbox": [135, 517, 917, 536]},
	{"text": "仿。", "bbox": [135, 540, 167, 558]},
	{"text": "影像学意见:", "bbox": [100, 714, 225, 731]},
	{"text": "1. 右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节,转移瘤可能;建", "bbox": [135, 732, 917, 750]},
	{"text": "议追踪复查:右肺门肿大淋巴结。", "bbox": [135, 752, 467, 770]},
	{"text": "2. 双肺慢性炎症,右肺中叶局限性支扩,双侧胸腔积液,心包积液。", "bbox": [132, 773, 832, 792]},
	{"text": "3. 脾脏低密度灶,建议追踪复查。", "bbox": [132, 795, 478, 813]},
	{"text": "4. 胆囊可疑小结石。升结肠多发憩室。", "bbox": [132, 816, 524, 835]},
	{"text": "5. 双肾小囊肿。", "bbox": [132, 838, 293, 857]},
	{"text": "报告医师:", "bbox": [94, 902, 166, 916]},
	{"text": "审核医师:", "bbox": [667, 905, 740, 918]},
	{"text": "此报告仅供临床医师参考,签字生效", "bbox": [94, 943, 375, 959]},
	{"text": "打印时间: 2025-12-22 16:36:26", "bbox": [625, 954, 900, 969]}
]
2026-08-06 10:29:17,264 INFO     30 [qwen-vl-text] coord API: raw_items=39, valid_items=39, elapsed=24.2s
2026-08-06 10:29:17,264 INFO     30 [qwen-vl-text] coord item[0]: text=信阳市中心医院, bbox=[401, 76, 610, 100]
2026-08-06 10:29:17,264 INFO     30 [qwen-vl-text] coord item[1]: text=影像科CT诊断报告书, bbox=[371, 116, 640, 139]
2026-08-06 10:29:17,264 INFO     30 [qwen-vl-text] coord item[2]: text=扫描, bbox=[703, 143, 735, 155]
2026-08-06 10:29:17,264 INFO     30 [qwen-vl-text] coord item[3]: text=获取电子胶, bbox=[837, 141, 902, 154]
2026-08-06 10:29:17,265 INFO     30 [qwen-vl-text] coord item[4]: text=片和报告(试用), bbox=[703, 155, 807, 168]
2026-08-06 10:29:17,265 INFO     30 [qwen-vl-text] coord item[5]: text=影像号: 000, bbox=[92, 179, 204, 193]
2026-08-06 10:29:17,265 INFO     30 [qwen-vl-text] coord item[6]: text=报告日期: 2025-12-22 16:36, bbox=[502, 173, 744, 188]
2026-08-06 10:29:17,265 INFO     30 [qwen-vl-text] coord item[7]: text=姓名:, bbox=[96, 203, 140, 217]
2026-08-06 10:29:17,265 INFO     30 [qwen-vl-text] coord item[8]: text=性别: 女, bbox=[328, 202, 400, 216]
2026-08-06 10:29:17,265 INFO     30 [qwen-vl-text] coord item[9]: text=年龄: 64岁, bbox=[444, 200, 535, 214]
2026-08-06 10:29:17,265 INFO     30 [qwen-vl-text] coord item[10]: text=检查日期: 2025-12-22, bbox=[651, 199, 843, 213]
2026-08-06 10:29:17,265 INFO     30 [qwen-vl-text] coord item[11]: text=科别: 日间化疗中心[东院区]院号: 2, bbox=[96, 225, 405, 241]
2026-08-06 10:29:17,265 INFO     30 [qwen-vl-text] coord item[12]: text=门诊号:/, bbox=[464, 223, 538, 238]
2026-08-06 10:29:17,266 INFO     30 [qwen-vl-text] coord item[13]: text=检查时间: 09:53:10, bbox=[655, 222, 827, 237]
2026-08-06 10:29:17,266 INFO     30 [qwen-vl-text] coord item[14]: text=检查方法: 胸部CT平扫,胸部CT增强,上腹部CT平扫,上腹部CT增强,下腹部CT平扫,下腹部CT增强, bbox=[96, 251, 889, 268]
2026-08-06 10:29:17,266 INFO     30 [qwen-vl-text] coord item[15]: text=技术参数:, bbox=[96, 280, 197, 298]
2026-08-06 10:29:17,266 INFO     30 [qwen-vl-text] coord item[16]: text=影像学所见:, bbox=[96, 306, 221, 324]
2026-08-06 10:29:17,266 INFO     30 [qwen-vl-text] coord item[17]: text=双侧胸廓对称,右肺门增大,可见不规则状软组织密度影,密度不均,边, bbox=[135, 326, 930, 345]
2026-08-06 10:29:17,266 INFO     30 [qwen-vl-text] coord item[18]: text=界不清,强化不均,右肺中下叶支气管稍变窄,双肺可见条索状及结节状高密, bbox=[135, 348, 929, 367]
2026-08-06 10:29:17,266 INFO     30 [qwen-vl-text] coord item[19]: text=度影,较大病灶位于右肺下叶内基底段见实性结节,大小约为15.8×15.4mm,, bbox=[135, 369, 915, 388]
2026-08-06 10:29:17,266 INFO     30 [qwen-vl-text] coord item[20]: text=轻度强化。右肺中叶局限性支扩。气管、支气管通畅,右肺门见明显肿大淋巴, bbox=[135, 390, 929, 409]
2026-08-06 10:29:17,266 INFO     30 [qwen-vl-text] coord item[21]: text=结,轻度强化,双侧胸膜腔及心包腔可见积液征象。与2025-8-21日片比较:, bbox=[135, 411, 904, 430]
2026-08-06 10:29:17,267 INFO     30 [qwen-vl-text] coord item[22]: text=双侧胸腔积液增多,心包积液新增,右肺门软组织密度影及淋巴结增大。, bbox=[135, 433, 868, 452]
2026-08-06 10:29:17,267 INFO     30 [qwen-vl-text] coord item[23]: text=肝脏未见明显异常密度及异常强化征象,胆囊内隐约见斑点状高密度影,, bbox=[135, 454, 915, 473]
2026-08-06 10:29:17,267 INFO     30 [qwen-vl-text] coord item[24]: text=脾脏见数个小灶状低强化影。胰腺形态、大小、密度正常。双肾见小圆形低密, bbox=[135, 475, 928, 494]
2026-08-06 10:29:17,267 INFO     30 [qwen-vl-text] coord item[25]: text=度影,边界清,增强未见明显强化。腹膜后未见明显增大淋巴结,腹腔未见明, bbox=[135, 496, 928, 515]
2026-08-06 10:29:17,267 INFO     30 [qwen-vl-text] coord item[26]: text=显积液征象。升结肠见多发小囊袋状外凸影。与2025-8-21日片比较:大致相, bbox=[135, 517, 917, 536]
2026-08-06 10:29:17,267 INFO     30 [qwen-vl-text] coord item[27]: text=仿。, bbox=[135, 540, 167, 558]
2026-08-06 10:29:17,267 INFO     30 [qwen-vl-text] coord item[28]: text=影像学意见:, bbox=[100, 714, 225, 731]
2026-08-06 10:29:17,267 INFO     30 [qwen-vl-text] coord item[29]: text=1. 右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节,转移瘤可能;建, bbox=[135, 732, 917, 750]
2026-08-06 10:29:17,267 INFO     30 [qwen-vl-text] coord item[30]: text=议追踪复查:右肺门肿大淋巴结。, bbox=[135, 752, 467, 770]
2026-08-06 10:29:17,267 INFO     30 [qwen-vl-text] coord item[31]: text=2. 双肺慢性炎症,右肺中叶局限性支扩,双侧胸腔积液,心包积液。, bbox=[132, 773, 832, 792]
2026-08-06 10:29:17,268 INFO     30 [qwen-vl-text] coord item[32]: text=3. 脾脏低密度灶,建议追踪复查。, bbox=[132, 795, 478, 813]
2026-08-06 10:29:17,268 INFO     30 [qwen-vl-text] coord item[33]: text=4. 胆囊可疑小结石。升结肠多发憩室。, bbox=[132, 816, 524, 835]
2026-08-06 10:29:17,268 INFO     30 [qwen-vl-text] coord item[34]: text=5. 双肾小囊肿。, bbox=[132, 838, 293, 857]
2026-08-06 10:29:17,268 INFO     30 [qwen-vl-text] coord item[35]: text=报告医师:, bbox=[94, 902, 166, 916]
2026-08-06 10:29:17,268 INFO     30 [qwen-vl-text] coord item[36]: text=审核医师:, bbox=[667, 905, 740, 918]
2026-08-06 10:29:17,268 INFO     30 [qwen-vl-text] coord item[37]: text=此报告仅供临床医师参考,签字生效, bbox=[94, 943, 375, 959]
2026-08-06 10:29:17,268 INFO     30 [qwen-vl-text] coord item[38]: text=打印时间: 2025-12-22 16:36:26, bbox=[625, 954, 900, 969]
2026-08-06 10:29:17,271 INFO     30 [qwen-vl-text] page=6 — 39/39 coords, api_time=24.2s
2026-08-06 10:29:17,271 INFO     30 [qwen-vl-text] new_positions (39):
[[6, 489.21999999999997, 744.1999999999999, 128.896, 169.6], [6, 452.62, 780.8, 196.736, 235.744], [6, 857.66, 896.6999999999999, 242.528, 262.88], [6, 1021.14, 1100.44, 239.136, 261.18399999999997], [6, 857.66, 984.54, 262.88, 284.928], [6, 112.24, 248.88, 303.584, 327.328], [6, 612.4399999999999, 907.68, 293.408, 318.848], [6, 117.12, 170.79999999999998, 344.288, 368.032], [6, 400.15999999999997, 488.0, 342.592, 366.336], [6, 541.68, 652.6999999999999, 339.2, 362.944], [6, 794.22, 1028.46, 337.50399999999996, 361.248], [6, 117.12, 494.09999999999997, 381.59999999999997, 408.736], [6, 566.08, 656.36, 378.20799999999997, 403.64799999999997], [6, 799.1, 1008.9399999999999, 376.512, 401.952], [6, 117.12, 1084.58, 425.69599999999997, 454.52799999999996], [6, 117.12, 240.34, 474.88, 505.40799999999996], [6, 117.12, 269.62, 518.976, 549.504], [6, 164.7, 1134.6, 552.896, 585.12], [6, 164.7, 1133.3799999999999, 590.208, 622.432], [6, 164.7, 1116.3, 625.824, 658.048], [6, 164.7, 1133.3799999999999, 661.4399999999999, 693.664], [6, 164.7, 1102.8799999999999, 697.0559999999999, 729.28], [6, 164.7, 1058.96, 734.3679999999999, 766.592], [6, 164.7, 1116.3, 769.9839999999999, 802.208], [6, 164.7, 1132.16, 805.6, 837.824], [6, 164.7, 1132.16, 841.216, 873.4399999999999], [6, 164.7, 1118.74, 876.832, 909.0559999999999], [6, 164.7, 203.74, 915.8399999999999, 946.3679999999999], [6, 122.0, 274.5, 1210.944, 1239.776], [6, 164.7, 1118.74, 1241.472, 1272.0], [6, 164.7, 569.74, 1275.392, 1305.92], [6, 161.04, 1015.04, 1311.008, 1343.232], [6, 161.04, 583.16, 1348.32, 1378.848], [6, 161.04, 639.28, 1383.936, 1416.1599999999999], [6, 161.04, 357.46, 1421.248, 1453.472], [6, 114.67999999999999, 202.51999999999998, 1529.792, 1553.536], [6, 813.74, 902.8, 1534.8799999999999, 1556.9279999999999], [6, 114.67999999999999, 457.5, 1599.328, 1626.464], [6, 762.5, 1098.0, 1617.984, 1643.424]]
2026-08-06 10:29:17,272 INFO     30 [qwen-vl-text] ═══ DONE ═══ 39 positions, pages=1, time=30.7s
2026-08-06 10:29:17,274 INFO     30 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 10:29:17,275 INFO     30 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-06 10:29:17,275 INFO     30 [qwen-vl-text] positions(36): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 10:29:17,276 INFO     30 [qwen-vl-text] page grouping: [7], lines per page: [36]
2026-08-06 10:29:18,798 INFO     30 [qwen-vl-parser] text API response (len=1065):
["三门峡市中心医院门户-惠睿360 ×", "← → ① 不安全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView", "临床数据中心-患者360视图", "返回患者查询 患者姓名:", "出生日期:", "期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>", "就诊时间轴", "门诊号:", "就诊时间: 2025-06-23 10:49:50 接诊科室: 普通儿科三组(门) 接诊医生: 谭真真", "全部 近一月 近三月 近半年 近一年", "近五年", "门诊39 住院1", "总览 就诊列表", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 体检报告", "2025-11-27 普通儿科二区 (..", "2025-11-24 普通儿科二区 (..", "2025-09-18 普通儿科二区 (..", "2025-07-11 普通儿科一组 (..", "2025-06-23 普通儿科三组 (", "2025-05-09 呼吸危重二病区(门)", "2025-04-11 耳鼻咽喉头颈外", "2025-04-11 呼吸危重二病区(门)", "2025-01-06 普通儿科三组 (..", "2024-12-30 普通儿科三组 (..", "2024-07-05 普通儿科一组 (..", "门诊号:", "姓名", "性别: 女", "年龄:41岁", "民族: 汉族", "婚姻状况: 小组", "身份证号:", "职业: 专业技术人员", "现住址:", "就诊类型:初诊", "就诊科室:普通儿科三组(门)", "就诊日期: 2025-06-23 10:49", "联系电话", "主诉: 呼吸道感染购药", "现病史: 呼吸道感染购药", "既往史: 平素体健, 无肝炎、结核类传染病史", "过敏史: 无", "体格检查: 发育正常, 营养良好, 精神一般, 口唇红润, 双侧扁桃体无肿大, 无充血、分泌物。咽腔黏膜有充", "血, 无红肿、疱疹, 双肺呼吸音清, 听诊心律齐, 无杂音, 腹平软, 无压痛、反跳痛", "辅助检查:", "初步印象: 上呼吸道感染", "处理意见: 门诊药物治疗", "备注:", "医师签名: 谭真真", "第1页"]
2026-08-06 10:29:18,800 INFO     30 [qwen-vl-text] page=7, rect=1260x1776, img=(3500x4934), dpi=200
2026-08-06 10:29:18,811 INFO     30 [qwen-vl-parser] page=25 text: 50 lines (bbox 1537-1586)
2026-08-06 10:29:18,812 INFO     30 [qwen-vl-text] LLM extraction start, text_len=544
2026-08-06 10:29:18,813 INFO     30 [qwen-vl-parser] page=25 text: 50 sections
2026-08-06 10:29:18,814 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:29:18,816 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 175, \"bbox_end\": 210, \"encounter_dates\": [\"2026-02-25\"], \"department\": \"肿瘤内科五门诊[东院\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "信阳市中心医院\n影像科CT诊断报告书\n扫描此二维码可\n以电子胶\n片和报告(试用)\n影像号: 0000\n报告日期: 2026-02-25 15:36\n姓名:\n性别: 女\n年龄: 65岁\n检查日期: 2026-02-25\n科别: 肿瘤内科五门诊[东院\n住院号: /\n门诊号: 1\n6\n检查时间: 08:57:41\n检查方法: 胸部CT平扫加薄层\n技术参数:\n影像学所见:\n双侧胸廓对称, 右肺门增大, 可见不规则状软组织密度影, 密度不均, 边\n界不清, 右肺中下叶支气管稍变窄, 双肺可见条索状及结节状高密度影。右肺\n中叶局限性支扩。气管、支气管通畅, 右肺门见明显肿大淋巴结, 右侧胸膜局\n部稍厚, 双侧胸膜腔及心包腔可见积液征象。与2025-12-22日片比较: 右侧胸\n腔积液增多, 右肺门软组织密度影及淋巴结进一步增大, 右肺结节增大, 右侧\n胸膜局部稍增厚。\n影像学意见:\n1. 右肺癌并右肺中下叶不张治疗状态。双肺多发结节, 转移瘤可能; 右肺门\n肿大淋巴结转移。\n2. 双肺慢性炎症, 双侧胸腔积液, 心包积液。\n3. 右侧胸膜局部稍厚, 不除外转移。\n报告医师:\n肖健\n审核医师:\n贺玲\n此报告仅供临床医师参考, 签字生效\n打印时间: 2026-02-25 15:36:58",
    "role": "user"
  }
]
2026-08-06 10:29:18,919 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:29:18.918+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 8, "lag": 0, "done": 0, "failed": 0, "current": {"6a97f83c918011f18dbe1f8f96f1c395": {"id": "6a97f83c918011f18dbe1f8f96f1c395", "doc_id": "688aee0a918011f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909798, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011615561, "task_type": "dataflow", "root_trace_id": "d05a3d8d0d6c4aa38394753a3ea0008c", "root_traceparent": "00-d05a3d8d0d6c4aa38394753a3ea0008c-2c380740bfb060e1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "00b9d592918111f18dbe1f8f96f1c395": {"id": "00b9d592918111f18dbe1f8f96f1c395", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011867426, "task_type": "dataflow", "root_trace_id": "1ab3198c92574fb4b2701d0f5db7322f", "root_traceparent": "00-1ab3198c92574fb4b2701d0f5db7322f-bdaff6f64a5f4a64-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:29:19,400 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=881541, prompt_len=764
2026-08-06 10:29:20,863 INFO     30 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-07-11"}
```
2026-08-06 10:29:20,864 INFO     30 [qwen-vl-parser] page=26 classify=text report_date=2025-07-11
2026-08-06 10:29:20,920 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=881541, prompt_len=401
2026-08-06 10:29:22,394 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:29:22,395 INFO     30 [qwen-vl-text] LLM output (len=607):
{
  "exam_date": "2026-02-25",
  "report_date": "2026-02-25",
  "exam_name": "胸部CT平扫加薄层",
  "exam_category": "imaging",
  "body_part": "胸部",
  "patient_name": null,
  "patient_gender": "女",
  "department": "肿瘤内科五门诊[东院",
  "bed_number": null,
  "findings": "双侧胸廓对称, 右肺门增大, 可见不规则状软组织密度影, 密度不均, 边界不清, 右肺中下叶支气管稍变窄, 双肺可见条索状及结节状高密度影。右肺中叶局限性支扩。气管、支气管通畅, 右肺门见明显肿大淋巴结, 右侧胸膜局部稍厚, 双侧胸膜腔及心包腔可见积液征象。与2025-12-22日片比较: 右侧胸腔积液增多, 右肺门软组织密度影及淋巴结进一步增大, 右肺结节增大, 右侧胸膜局部稍增厚。",
  "conclusion": "1. 右肺癌并右肺中下叶不张治疗状态。双肺多发结节, 转移瘤可能; 右肺门肿大淋巴结转移。\n2. 双肺慢性炎症, 双侧胸腔积液, 心包积液。\n3. 右侧胸膜局部稍厚, 不除外转移。",
  "physician": "肖健",
  "reviewer": "贺玲"
}
2026-08-06 10:29:22,430 INFO     30 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=6567477, prompt_len=1265
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共36行）
["信阳市中心医院", "影像科CT诊断报告书", "扫描此二维码可", "以电子胶", "片和报告(试用)", "影像号: 0000", "报告日期: 2026-02-25 15:36", "姓名:", "性别: 女", "年龄: 65岁", "检查日期: 2026-02-25", "科别: 肿瘤内科五门诊[东院", "住院号: /", "门诊号: 1", "6", "检查时间: 08:57:41", "检查方法: 胸部CT平扫加薄层", "技术参数:", "影像学所见:", "双侧胸廓对称, 右肺门增大, 可见不规则状软组织密度影, 密度不均, 边", "界不清, 右肺中下叶支气管稍变窄, 双肺可见条索状及结节状高密度影。右肺", "中叶局限性支扩。气管、支气管通畅, 右肺门见明显肿大淋巴结, 右侧胸膜局", "部稍厚, 双侧胸膜腔及心包腔可见积液征象。与2025-12-22日片比较: 右侧胸", "腔积液增多, 右肺门软组织密度影及淋巴结进一步增大, 右肺结节增大, 右侧", "胸膜局部稍增厚。", "影像学意见:", "1. 右肺癌并右肺中下叶不张治疗状态。双肺多发结节, 转移瘤可能; 右肺门", "肿大淋巴结转移。", "2. 双肺慢性炎症, 双侧胸腔积液, 心包积液。", "3. 右侧胸膜局部稍厚, 不除外转移。", "报告医师:", "肖健", "审核医师:", "贺玲", "此报告仅供临床医师参考, 签字生效", "打印时间: 2026-02-25 15:36:58"]

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
2026-08-06 10:29:31,876 INFO     30 [qwen-vl-parser] text API response (len=1004):
["<->C ①不安全|192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView", "临床数据中心-患者360视图", "返回患者查询 患者姓 出生日期", "就诊日期:2020-07-08 最近诊疗日期:2026-02-12 当前在院状态:出院 过敏:无 详情>>", "就诊时间始 门诊号", "就诊时间:2025-07-1110:02:50 接诊科室:普通儿科一组(门) 接诊医生:赵艳", "全部 近一月 近三月 近半年 近一年", "近五年", "■ 门急诊39 住院1", "总览 就诊列表", "2025-11-27普通儿科二区(...", "2025-11-24普通儿科二区(...", "2025-09-18普通儿科二区(...", "2025-07-11普通儿科一组(...", "2025-06-23普通儿科三组(...", "2025-05-09呼吸危重二病区(门)", "2025-04-11耳鼻咽喉头颈外...", "2025-04-11呼吸危重二病区(门)", "2025-01-06普通儿科三组(...", "2024-12-30普通儿科三组(...", "2024-07-05普通儿科一组(...", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 体检报告", "一", "门诊号", "病历", "姓名", "性别:女", "年龄:41岁", "民族:汉族", "婚姻状况:未婚", "身份证", "职业:专业技术人员", "现住址:", "就诊类型:初诊", "就诊科室:普通儿科一组(门)", "就诊日期:2025-07-1110:02", "联系电话", "主诉:呼吸道感染购药", "现病史:呼吸道感染购药", "既往史:平素体健,无肝炎、结核类传染病史", "过敏史:无", "体格检查:发育正常,营养良好,精神一般,口唇红润,双侧扁桃体无肿大,无充血、分泌物。咽腔黏膜无充", "血、红肿、疱疹,双肺呼吸音清,听诊心律齐,无杂音,腹平软,无压痛、反跳痛", "辅助检查:", "初步印象:支气管炎", "处理意见:门诊药物治疗", "备注:", "医师签名:赵艳", "第1页", ""]
2026-08-06 10:29:31,877 INFO     30 [qwen-vl-parser] page=26 text: 49 lines (bbox 1587-1635)
2026-08-06 10:29:31,878 INFO     30 [qwen-vl-parser] page=26 text: 49 sections
2026-08-06 10:29:32,366 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=992751, prompt_len=764
2026-08-06 10:29:34,439 INFO     30 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-09-18"}
```
2026-08-06 10:29:34,440 INFO     30 [qwen-vl-parser] page=27 classify=text report_date=2025-09-18
2026-08-06 10:29:34,478 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=992751, prompt_len=401
2026-08-06 10:29:42,296 INFO     30 [qwen-vl-parser] text API response (len=1063):
["临床数据中心-患者360视图", "返回患者查询", "患者姓名:", "：女 出生日期.", "首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>", "就诊时间抽", "门诊号:", "就诊时间：2025-09-18 15:22:06 接诊科室：普通儿科二区（门） 接诊医生：赵艳", "全部 近一月 近三月 近半年 近一年", "近五年", "■ 门诊诊39 住院1", "总览 就诊列表", "2025-12-09 普通儿科二区（...", "2025-12-07 普通儿科二区（...", "2025-12-01 普通儿科二区（...", "2025-11-27 普通儿科二区（...", "2025-11-24 普通儿科二区（...", "2025-09-18 普通儿科二区（...", "2025-07-11 普通儿科一组（...", "2025-06-23 普通儿科三组（...", "2025-05-09 呼吸危重二病区(门)", "2025-04-11 耳鼻咽喉头颈外...", "2025-04-11 呼吸危重二病区(门)", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 请价治疗 费用 体检报告", "门诊病历", "门诊", "姓名:", "性别：女", "年龄:41岁", "民族：汉族", "婚姻状况：未婚", "身份证", "职业：职员", "现住址：", "就诊类型:初诊", "就诊科室:普通儿科二区（门）", "就诊日期：2025-09-18 15:22", "联系电话", "主诉：咽部疼痛伴眼部不适4天", "现病史：4天前无明显诱因出现咽部疼痛，伴鼻塞，伴眼部不适，无发热、呕吐、腹泻、皮疹等不适。病后精神、食欲欠佳，大小便正常。", "既往史：无特殊。", "过敏史：无", "体格检查：发育正常，营养良好，精神一般，呼吸平稳，双眼睑结膜充血，口唇红润，咽腔充血，无疱疹，双侧扁桃体I°，充血，无分泌物，双肺呼吸音清，未闻及干湿性啰音，听诊心律齐，无杂音，腹平软，无压痛、反跳痛，未触及包块，肠鸣音活跃，神经系统未见阳性体征。", "辅助检查：无", "初步印象：1.急性咽峡炎.2.急性变应性结膜炎", "处理意见：门诊治疗，动态观察病情变化，不适及时随诊。", "备注：", "医师签名：赵艳", "第1页", "Le coo", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-06 10:29:42,297 INFO     30 [qwen-vl-parser] page=27 text: 52 lines (bbox 1636-1687)
2026-08-06 10:29:42,298 INFO     30 [qwen-vl-parser] page=27 text: 52 sections
2026-08-06 10:29:42,634 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=923208, prompt_len=764
2026-08-06 10:29:44,065 INFO     30 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-12-01"}
```
2026-08-06 10:29:44,067 INFO     30 [qwen-vl-parser] page=28 classify=text report_date=2025-12-01
2026-08-06 10:29:44,102 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=923208, prompt_len=401
2026-08-06 10:29:44,830 INFO     30 [qwen-vl-text] coord API raw response (len=2128):
[
	{"text": "信阳市中心医院", "bbox": [412, 73, 620, 97]},
	{"text": "影像科CT诊断报告书", "bbox": [381, 114, 650, 137]},
	{"text": "扫描此二维码可", "bbox": [712, 142, 814, 155]},
	{"text": "以电子胶", "bbox": [850, 143, 906, 155]},
	{"text": "片和报告(试用)", "bbox": [712, 155, 814, 167]},
	{"text": "影像号: 0000", "bbox": [96, 171, 208, 186]},
	{"text": "报告日期: 2026-02-25 15:36", "bbox": [512, 171, 753, 186]},
	{"text": "姓名:", "bbox": [100, 196, 145, 210]},
	{"text": "性别: 女", "bbox": [338, 197, 410, 212]},
	{"text": "年龄: 65岁", "bbox": [455, 197, 547, 212]},
	{"text": "检查日期: 2026-02-25", "bbox": [661, 197, 850, 212]},
	{"text": "科别: 肿瘤内科五门诊[东院", "bbox": [100, 219, 325, 235]},
	{"text": "住院号: /", "bbox": [330, 220, 412, 235]},
	{"text": "门诊号: 1", "bbox": [474, 220, 547, 235]},
	{"text": "6", "bbox": [610, 222, 619, 235]},
	{"text": "检查时间: 08:57:41", "bbox": [666, 220, 833, 235]},
	{"text": "检查方法: 胸部CT平扫加薄层", "bbox": [100, 248, 373, 266]},
	{"text": "技术参数:", "bbox": [100, 274, 204, 292]},
	{"text": "影像学所见:", "bbox": [100, 300, 228, 318]},
	{"text": "双侧胸廓对称, 右肺门增大, 可见不规则状软组织密度影, 密度不均, 边", "bbox": [185, 325, 935, 344]},
	{"text": "界不清, 右肺中下叶支气管稍变窄, 双肺可见条索状及结节状高密度影。右肺", "bbox": [140, 347, 935, 366]},
	{"text": "中叶局限性支扩。气管、支气管通畅, 右肺门见明显肿大淋巴结, 右侧胸膜局", "bbox": [140, 369, 935, 388]},
	{"text": "部稍厚, 双侧胸膜腔及心包腔可见积液征象。与2025-12-22日片比较: 右侧胸", "bbox": [140, 390, 935, 409]},
	{"text": "腔积液增多, 右肺门软组织密度影及淋巴结进一步增大, 右肺结节增大, 右侧", "bbox": [140, 412, 935, 431]},
	{"text": "胸膜局部稍增厚。", "bbox": [140, 434, 315, 452]},
	{"text": "影像学意见:", "bbox": [104, 719, 233, 736]},
	{"text": "1. 右肺癌并右肺中下叶不张治疗状态。双肺多发结节, 转移瘤可能; 右肺门", "bbox": [138, 738, 923, 756]},
	{"text": "肿大淋巴结转移。", "bbox": [138, 759, 315, 777]},
	{"text": "2. 双肺慢性炎症, 双侧胸腔积液, 心包积液。", "bbox": [138, 781, 607, 800]},
	{"text": "3. 右侧胸膜局部稍厚, 不除外转移。", "bbox": [138, 803, 514, 821]},
	{"text": "报告医师:", "bbox": [100, 910, 173, 924]},
	{"text": "肖健", "bbox": [204, 910, 294, 937]},
	{"text": "审核医师:", "bbox": [678, 910, 750, 924]},
	{"text": "贺玲", "bbox": [798, 910, 858, 937]},
	{"text": "此报告仅供临床医师参考, 签字生效", "bbox": [100, 952, 388, 967]},
	{"text": "打印时间: 2026-02-25 15:36:58", "bbox": [638, 958, 906, 973]}
]
2026-08-06 10:29:44,831 INFO     30 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=22.4s
2026-08-06 10:29:44,831 INFO     30 [qwen-vl-text] coord item[0]: text=信阳市中心医院, bbox=[412, 73, 620, 97]
2026-08-06 10:29:44,831 INFO     30 [qwen-vl-text] coord item[1]: text=影像科CT诊断报告书, bbox=[381, 114, 650, 137]
2026-08-06 10:29:44,831 INFO     30 [qwen-vl-text] coord item[2]: text=扫描此二维码可, bbox=[712, 142, 814, 155]
2026-08-06 10:29:44,832 INFO     30 [qwen-vl-text] coord item[3]: text=以电子胶, bbox=[850, 143, 906, 155]
2026-08-06 10:29:44,832 INFO     30 [qwen-vl-text] coord item[4]: text=片和报告(试用), bbox=[712, 155, 814, 167]
2026-08-06 10:29:44,832 INFO     30 [qwen-vl-text] coord item[5]: text=影像号: 0000, bbox=[96, 171, 208, 186]
2026-08-06 10:29:44,832 INFO     30 [qwen-vl-text] coord item[6]: text=报告日期: 2026-02-25 15:36, bbox=[512, 171, 753, 186]
2026-08-06 10:29:44,833 INFO     30 [qwen-vl-text] coord item[7]: text=姓名:, bbox=[100, 196, 145, 210]
2026-08-06 10:29:44,833 INFO     30 [qwen-vl-text] coord item[8]: text=性别: 女, bbox=[338, 197, 410, 212]
2026-08-06 10:29:44,833 INFO     30 [qwen-vl-text] coord item[9]: text=年龄: 65岁, bbox=[455, 197, 547, 212]
2026-08-06 10:29:44,833 INFO     30 [qwen-vl-text] coord item[10]: text=检查日期: 2026-02-25, bbox=[661, 197, 850, 212]
2026-08-06 10:29:44,834 INFO     30 [qwen-vl-text] coord item[11]: text=科别: 肿瘤内科五门诊[东院, bbox=[100, 219, 325, 235]
2026-08-06 10:29:44,834 INFO     30 [qwen-vl-text] coord item[12]: text=住院号: /, bbox=[330, 220, 412, 235]
2026-08-06 10:29:44,834 INFO     30 [qwen-vl-text] coord item[13]: text=门诊号: 1, bbox=[474, 220, 547, 235]
2026-08-06 10:29:44,834 INFO     30 [qwen-vl-text] coord item[14]: text=6, bbox=[610, 222, 619, 235]
2026-08-06 10:29:44,835 INFO     30 [qwen-vl-text] coord item[15]: text=检查时间: 08:57:41, bbox=[666, 220, 833, 235]
2026-08-06 10:29:44,835 INFO     30 [qwen-vl-text] coord item[16]: text=检查方法: 胸部CT平扫加薄层, bbox=[100, 248, 373, 266]
2026-08-06 10:29:44,835 INFO     30 [qwen-vl-text] coord item[17]: text=技术参数:, bbox=[100, 274, 204, 292]
2026-08-06 10:29:44,836 INFO     30 [qwen-vl-text] coord item[18]: text=影像学所见:, bbox=[100, 300, 228, 318]
2026-08-06 10:29:44,837 INFO     30 [qwen-vl-text] coord item[19]: text=双侧胸廓对称, 右肺门增大, 可见不规则状软组织密度影, 密度不均, 边, bbox=[185, 325, 935, 344]
2026-08-06 10:29:44,837 INFO     30 [qwen-vl-text] coord item[20]: text=界不清, 右肺中下叶支气管稍变窄, 双肺可见条索状及结节状高密度影。右肺, bbox=[140, 347, 935, 366]
2026-08-06 10:29:44,838 INFO     30 [qwen-vl-text] coord item[21]: text=中叶局限性支扩。气管、支气管通畅, 右肺门见明显肿大淋巴结, 右侧胸膜局, bbox=[140, 369, 935, 388]
2026-08-06 10:29:44,838 INFO     30 [qwen-vl-text] coord item[22]: text=部稍厚, 双侧胸膜腔及心包腔可见积液征象。与2025-12-22日片比较: 右侧胸, bbox=[140, 390, 935, 409]
2026-08-06 10:29:44,839 INFO     30 [qwen-vl-text] coord item[23]: text=腔积液增多, 右肺门软组织密度影及淋巴结进一步增大, 右肺结节增大, 右侧, bbox=[140, 412, 935, 431]
2026-08-06 10:29:44,840 INFO     30 [qwen-vl-text] coord item[24]: text=胸膜局部稍增厚。, bbox=[140, 434, 315, 452]
2026-08-06 10:29:44,840 INFO     30 [qwen-vl-text] coord item[25]: text=影像学意见:, bbox=[104, 719, 233, 736]
2026-08-06 10:29:44,842 INFO     30 [qwen-vl-text] coord item[26]: text=1. 右肺癌并右肺中下叶不张治疗状态。双肺多发结节, 转移瘤可能; 右肺门, bbox=[138, 738, 923, 756]
2026-08-06 10:29:44,843 INFO     30 [qwen-vl-text] coord item[27]: text=肿大淋巴结转移。, bbox=[138, 759, 315, 777]
2026-08-06 10:29:44,843 INFO     30 [qwen-vl-text] coord item[28]: text=2. 双肺慢性炎症, 双侧胸腔积液, 心包积液。, bbox=[138, 781, 607, 800]
2026-08-06 10:29:44,844 INFO     30 [qwen-vl-text] coord item[29]: text=3. 右侧胸膜局部稍厚, 不除外转移。, bbox=[138, 803, 514, 821]
2026-08-06 10:29:44,844 INFO     30 [qwen-vl-text] coord item[30]: text=报告医师:, bbox=[100, 910, 173, 924]
2026-08-06 10:29:44,844 INFO     30 [qwen-vl-text] coord item[31]: text=肖健, bbox=[204, 910, 294, 937]
2026-08-06 10:29:44,844 INFO     30 [qwen-vl-text] coord item[32]: text=审核医师:, bbox=[678, 910, 750, 924]
2026-08-06 10:29:44,845 INFO     30 [qwen-vl-text] coord item[33]: text=贺玲, bbox=[798, 910, 858, 937]
2026-08-06 10:29:44,845 INFO     30 [qwen-vl-text] coord item[34]: text=此报告仅供临床医师参考, 签字生效, bbox=[100, 952, 388, 967]
2026-08-06 10:29:44,845 INFO     30 [qwen-vl-text] coord item[35]: text=打印时间: 2026-02-25 15:36:58, bbox=[638, 958, 906, 973]
2026-08-06 10:29:44,851 INFO     30 [qwen-vl-text] page=7 — 36/36 coords, api_time=22.4s
2026-08-06 10:29:44,852 INFO     30 [qwen-vl-text] new_positions (36):
[[7, 519.12, 781.2, 129.648, 172.272], [7, 480.06, 819.0, 202.464, 243.312], [7, 897.12, 1025.64, 252.192, 275.28000000000003], [7, 1071.0, 1141.56, 253.968, 275.28000000000003], [7, 897.12, 1025.64, 275.28000000000003, 296.592], [7, 120.96000000000001, 262.08, 303.696, 330.336], [7, 645.12, 948.78, 303.696, 330.336], [7, 126.0, 182.7, 348.096, 372.96], [7, 425.88, 516.6, 349.872, 376.512], [7, 573.3, 689.22, 349.872, 376.512], [7, 832.86, 1071.0, 349.872, 376.512], [7, 126.0, 409.5, 388.944, 417.36], [7, 415.8, 519.12, 390.72, 417.36], [7, 597.24, 689.22, 390.72, 417.36], [7, 768.6, 779.94, 394.272, 417.36], [7, 839.16, 1049.58, 390.72, 417.36], [7, 126.0, 469.98, 440.448, 472.416], [7, 126.0, 257.04, 486.624, 518.592], [7, 126.0, 287.28000000000003, 532.8, 564.768], [7, 233.1, 1178.1, 577.2, 610.944], [7, 176.4, 1178.1, 616.272, 650.016], [7, 176.4, 1178.1, 655.344, 689.088], [7, 176.4, 1178.1, 692.64, 726.384], [7, 176.4, 1178.1, 731.712, 765.456], [7, 176.4, 396.9, 770.784, 802.7520000000001], [7, 131.04, 293.58, 1276.944, 1307.136], [7, 173.88, 1162.98, 1310.688, 1342.656], [7, 173.88, 396.9, 1347.984, 1379.952], [7, 173.88, 764.82, 1387.056, 1420.8], [7, 173.88, 647.64, 1426.128, 1458.096], [7, 126.0, 217.98, 1616.16, 1641.0240000000001], [7, 257.04, 370.44, 1616.16, 1664.112], [7, 854.28, 945.0, 1616.16, 1641.0240000000001], [7, 1005.48, 1081.08, 1616.16, 1664.112], [7, 126.0, 488.88, 1690.752, 1717.392], [7, 803.88, 1141.56, 1701.4080000000001, 1728.048]]
2026-08-06 10:29:44,853 INFO     30 [qwen-vl-text] ═══ DONE ═══ 36 positions, pages=1, time=27.6s
2026-08-06 10:29:44,854 INFO     30 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 10:29:44,855 INFO     30 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-06 10:29:44,855 INFO     30 [qwen-vl-text] positions(43): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 10:29:44,857 INFO     30 [qwen-vl-text] page grouping: [8], lines per page: [43]
2026-08-06 10:29:47,346 INFO     30 [qwen-vl-text] page=8, rect=2188x1632, img=(6078x4534), dpi=200
2026-08-06 10:29:47,353 INFO     30 [qwen-vl-text] LLM extraction start, text_len=357
2026-08-06 10:29:47,353 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:29:47,353 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 211, \"bbox_end\": 253, \"encounter_dates\": [\"2026-03-23\"], \"department\": \"日间化疗中心[东院区]\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "信阳市中心医院心电图报告单\n门诊号:\n姓名:\nP波宽度: 141ms\n诊断: 1.窦性心律\n住院号: 0000\n性别: 女\nP-R间期: 181ms\n【120-200】\n2.低电压\n床位号: 04\n年龄: 65岁\nQRS时限: 101ms\n【60-110】\n科室: 日间化疗中心[心率: 77bpm\n【60-100】\nQT/QTc: 358/406ms\n【360-440】\n东院区]\n电轴: 60°\n【-30-90】\n2026-03-23 08:43:55\n25mm/s 10mm/mV\nI\nV1\nV3R\nII\nV2\nIII\nV3\nV4R\naVR\nV4\naVL\nV5\nV5R\naVF\nV6\nII\n检查时间: 2026/3/23 8:43:55\n报告时间: 2026/3/23 8:59:30\n报告医生:\n审核医生:",
    "role": "user"
  }
]
2026-08-06 10:29:49,484 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:29:49.481+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 8, "lag": 0, "done": 0, "failed": 0, "current": {"6a97f83c918011f18dbe1f8f96f1c395": {"id": "6a97f83c918011f18dbe1f8f96f1c395", "doc_id": "688aee0a918011f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909798, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011615561, "task_type": "dataflow", "root_trace_id": "d05a3d8d0d6c4aa38394753a3ea0008c", "root_traceparent": "00-d05a3d8d0d6c4aa38394753a3ea0008c-2c380740bfb060e1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "00b9d592918111f18dbe1f8f96f1c395": {"id": "00b9d592918111f18dbe1f8f96f1c395", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011867426, "task_type": "dataflow", "root_trace_id": "1ab3198c92574fb4b2701d0f5db7322f", "root_traceparent": "00-1ab3198c92574fb4b2701d0f5db7322f-bdaff6f64a5f4a64-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:29:50,542 INFO     30 [qwen-vl-parser] text API response (len=1136):
["全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView", "临床数据中心", "0视图", "返回患者查询", "患者", "女 出生F", "就诊日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>", "就诊时间轴", "门诊", "诊时间: 2025-12-01 15:28:03 接诊科室: 普通儿科二区(门) 接诊医生: 赵海国", "全季", "近一月", "近三月", "近半年", "近一年", "近五年", "门诊急诊39 住院1", "总览", "就诊列表", "集成视图", "诊断", "病历文书", "处方", "检验", "检查", "处置", "肺功能检查", "单机报告", "透析治疗", "费用", "体检报告", "门诊", "1. 门诊病历", "2026-01-15 呼吸危重三病区(门)", "2026-01-06 妇科一病区(门)", "2025-12-09 普通儿科二区(...", "2025-12-07 普通儿科二区(...", "2025-12-01 普通儿科二区(...", "2025-11-27 普通儿科二区(...", "2025-11-24 普通儿科二区(...", "2025-09-18 普通儿科二区(...", "2025-07-11 普通儿科一组(...", "2025-06-23 普通儿科三组(...", "2025-05-09 呼吸危重二病区(门)", "姓名:", "性别: 女", "年龄:41岁", "民族: 汉族", "婚姻状况: 未...", "身份证:", "职业: 专业技术人员", "现住址:", "就诊类型:初诊", "就诊科室:普通儿科二区(门)", "就诊日期: 2025-12-01 15:28", "联系电", "主诉: 发热半天。", "现病史: 半天前出现发热, 最高体温38.0℃, 口服药物治疗1次, 无咳嗽, 无喘息, 无呼吸困难, 无咯血, 无腹泻、呕吐等。精神食欲一般, 大小便正常。", "既往史: 无。", "过敏史: 无", "体格检查: 神志清, 精神一般, 呼吸浅快, 咽充血, 扁桃体二度大, 充血, 无疱疹, 无脓点, 双肺呼吸音清,", "心音有力, 律齐, 腹软。", "辅助检查:", "初步印象: 急性上呼吸道感染", "处理意见: 口服药物, 动态观察, 不适随诊。", "备注:", "医师签名: 赵海国", "第1页"]
2026-08-06 10:29:50,543 INFO     30 [qwen-vl-parser] page=28 text: 68 lines (bbox 1688-1755)
2026-08-06 10:29:50,543 INFO     30 [qwen-vl-parser] page=28 text: 68 sections
2026-08-06 10:29:50,927 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:29:50,927 INFO     30 [qwen-vl-text] LLM output (len=541):
{
  "exam_date": "2026-03-23",
  "report_date": "2026-03-23",
  "exam_name": "心电图",
  "exam_category": "other",
  "body_part": null,
  "patient_name": null,
  "patient_gender": "女",
  "department": "日间化疗中心[东院区]",
  "bed_number": "04",
  "findings": "P波宽度: 141ms\nP-R间期: 181ms 【120-200】\nQRS时限: 101ms 【60-110】\n心率: 77bpm 【60-100】\nQT/QTc: 358/406ms 【360-440】\n电轴: 60° 【-30-90】\n25mm/s 10mm/mV\n导联: I, V1, V3R, II, V2, III, V3, V4R, aVR, V4, aVL, V5, V5R, aVF, V6",
  "conclusion": "诊断: 1.窦性心律 2.低电压",
  "physician": null,
  "reviewer": null
}
2026-08-06 10:29:51,016 INFO     30 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=9895249, prompt_len=1099
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
2026-08-06 10:29:51,437 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2164311, prompt_len=764
2026-08-06 10:29:53,426 INFO     30 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-06 10:29:53,428 INFO     30 [qwen-vl-parser] page=29 classify=text report_date=None
2026-08-06 10:29:53,470 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2164311, prompt_len=401
2026-08-06 10:30:11,101 INFO     30 [qwen-vl-parser] text API response (len=1489):
["姓名：", "性别：女", "年龄：41岁", "民族：汉族", "婚姻状况：已婚", "身份证号", "职业：专业技术人员", "现住址", "就诊类型：初诊", "就诊科室：妇科一病区(门)", "就诊日期：2026-01-06 08:36", "联系电话.", "主诉：左下腹间断疼痛1年左右来诊", "现病史：患者诉于2024年01月05日无明显诱因出现下腹持续疼痛行相关检查后诊断为盆腔炎性疾病后遗症，", "慢性盆腔痛，药物治疗后好转，慢性盆腔痛病程12月，目前疾病状态持续，未治疗。", "既往史：2025年11月24日-2025年12月12日本院儿科门诊就诊代家属开药，否认3个月内其他病史及合并用药/", "非药物治疗，现患者无盆腔炎性疾病急性发作，否认既往有子宫肌瘤、子宫内膜异位症、子宫腺肌病、结核性", "盆腔炎、间质性膀胱炎、异常子宫出血、盆腔淤血综合征、子宫颈高级别上皮内病变等其他病症引起相关症状", "者；未放置宫内节育器；无子宫及双侧附件缺如；近2周内未使用过本方案规定研究期间禁止使用的治疗（包括", "药物和非药物治疗）；无控制不稳定的心血管、肝、肾和血液系统、糖尿病、甲状腺疾病等严重原发性疾病；", "获得知情同意书前5年内未患有恶性肿瘤；否认对试验用药品过敏，包括对本品成分或者药物辅料有过敏史；否", "认长期酗酒、药物滥用史；无智力障碍或精神障碍；近1个月内未参加过任何干预性临床试验；患者当前不在妊", "娠期、哺乳期，同意在试验期间及试验结束后3个月内采取有效避孕措施。", "婚育史：已婚已育，孕2产2，有性生活史", "手术史：2016年8月31日、2020年7月9日因生产行剖宫产手术", "月经史：初潮12岁，既往月经周期规律，经量中，色红，无痛经，末次月经2025.12.29-2025.1.2，周期26-", "28天，经期5天，经量较前不变", "过敏史：无", "生命体征：2026.1.6测量身高：160.0cm 体重：51.0kg 体温：36.4℃ 脉搏：76次/分 呼吸：18次/分 血压：", "98/76mmHg", "体格检查：淋巴结、头颈部、胸部、脊柱/四肢/关节、神经系统未见异常，腹部异常（左下腹压痛，CS，研究", "疾病相关），皮肤黏膜异常（腹部皮肤约5-6cm剖宫产手术瘢痕，NCS），其他未查。", "专科检查：外阴已婚型，阴道畅，宫颈光滑，无摇举痛，有宫体压痛，无子宫活动受限或粘连固定，左侧附件", "区、右侧附件区压痛，无宫骶韧带增粗、变硬、触痛。", "辅助检查：今日按方案要求开具血常规、尿沉渣（含尿常规）、肝功八项、肾功两项、血妊娠、血沉、血清C&-", "125、妇科微生态、十二导联心电图、妇科阴道彩色B超检查，结果详见检查单。", "初步印象：盆腔痛中医辨证：主症：下腹胀痛，腰骶部胀痛、带下量多；次症：神疲乏力、口苦口腻、小便", "黄；舌象：舌质红、苔黄腻；脉象：脉弦滑；2026年01月06日由张丹丹医生辨证为湿热瘀阻症。 西医：盆腔炎", "性疾病后遗症，慢性盆腔痛", "处理意见：根据目前临床表现及患者情况，权丽丽医生于2026年01月06日08时38分在9号楼4楼医患沟通室向患", "绍“妇科千金片治疗盆腔炎性疾病后遗症（湿热瘀阻证）的随机、双盲、安慰剂平行对照、多中心临", "床试验”及知情同意书内容，已告知参加试验可能的风险与获益，患者已充分理解并同意参加该研究，未提出", "门", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-06 10:30:11,102 INFO     30 [qwen-vl-parser] page=29 text: 45 lines (bbox 1756-1800)
2026-08-06 10:30:11,102 INFO     30 [qwen-vl-parser] page=29 text: 45 sections
2026-08-06 10:30:12,012 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2496910, prompt_len=764
2026-08-06 10:30:13,808 INFO     30 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-06 10:30:13,809 INFO     30 [qwen-vl-parser] page=30 classify=text report_date=None
2026-08-06 10:30:13,856 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2496910, prompt_len=401
2026-08-06 10:30:14,908 INFO     30 [qwen-vl-text] coord API raw response (len=2227):
[
	{"text": "信阳市中心医院心电图报告单", "bbox": [388, 24, 636, 52]},
	{"text": "门诊号:", "bbox": [58, 85, 104, 105]},
	{"text": "姓名:", "bbox": [208, 84, 254, 104]},
	{"text": "P波宽度: 141ms", "bbox": [407, 82, 513, 102]},
	{"text": "诊断: 1.窦性心律", "bbox": [663, 70, 773, 92]},
	{"text": "住院号: 0000", "bbox": [58, 117, 144, 137]},
	{"text": "性别: 女", "bbox": [208, 115, 284, 135]},
	{"text": "P-R间期: 181ms", "bbox": [407, 107, 513, 127]},
	{"text": "【120-200】", "bbox": [582, 107, 645, 126]},
	{"text": "2.低电压", "bbox": [707, 91, 760, 110]},
	{"text": "床位号: 04", "bbox": [58, 150, 136, 170]},
	{"text": "年龄: 65岁", "bbox": [208, 148, 296, 168]},
	{"text": "QRS时限: 101ms", "bbox": [407, 132, 513, 151]},
	{"text": "【60-110】", "bbox": [582, 134, 639, 152]},
	{"text": "科室: 日间化疗中心[心率: 77bpm", "bbox": [58, 181, 304, 201]},
	{"text": "【60-100】", "bbox": [337, 181, 392, 200]},
	{"text": "QT/QTc: 358/406ms", "bbox": [407, 155, 539, 175]},
	{"text": "【360-440】", "bbox": [582, 157, 645, 175]},
	{"text": "东院区]", "bbox": [117, 196, 160, 215]},
	{"text": "电轴: 60°", "bbox": [411, 182, 498, 202]},
	{"text": "【-30-90】", "bbox": [582, 183, 638, 202]},
	{"text": "2026-03-23 08:43:55", "bbox": [86, 235, 203, 254]},
	{"text": "25mm/s 10mm/mV", "bbox": [824, 234, 940, 253]},
	{"text": "I", "bbox": [87, 278, 97, 295]},
	{"text": "V1", "bbox": [366, 277, 383, 295]},
	{"text": "V3R", "bbox": [650, 277, 676, 294]},
	{"text": "II", "bbox": [86, 372, 98, 389]},
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
2026-08-06 10:30:14,909 INFO     30 [qwen-vl-text] coord API: raw_items=43, valid_items=43, elapsed=23.9s
2026-08-06 10:30:14,910 INFO     30 [qwen-vl-text] coord item[0]: text=信阳市中心医院心电图报告单, bbox=[388, 24, 636, 52]
2026-08-06 10:30:14,910 INFO     30 [qwen-vl-text] coord item[1]: text=门诊号:, bbox=[58, 85, 104, 105]
2026-08-06 10:30:14,910 INFO     30 [qwen-vl-text] coord item[2]: text=姓名:, bbox=[208, 84, 254, 104]
2026-08-06 10:30:14,910 INFO     30 [qwen-vl-text] coord item[3]: text=P波宽度: 141ms, bbox=[407, 82, 513, 102]
2026-08-06 10:30:14,910 INFO     30 [qwen-vl-text] coord item[4]: text=诊断: 1.窦性心律, bbox=[663, 70, 773, 92]
2026-08-06 10:30:14,910 INFO     30 [qwen-vl-text] coord item[5]: text=住院号: 0000, bbox=[58, 117, 144, 137]
2026-08-06 10:30:14,911 INFO     30 [qwen-vl-text] coord item[6]: text=性别: 女, bbox=[208, 115, 284, 135]
2026-08-06 10:30:14,911 INFO     30 [qwen-vl-text] coord item[7]: text=P-R间期: 181ms, bbox=[407, 107, 513, 127]
2026-08-06 10:30:14,912 INFO     30 [qwen-vl-text] coord item[8]: text=【120-200】, bbox=[582, 107, 645, 126]
2026-08-06 10:30:14,912 INFO     30 [qwen-vl-text] coord item[9]: text=2.低电压, bbox=[707, 91, 760, 110]
2026-08-06 10:30:14,912 INFO     30 [qwen-vl-text] coord item[10]: text=床位号: 04, bbox=[58, 150, 136, 170]
2026-08-06 10:30:14,912 INFO     30 [qwen-vl-text] coord item[11]: text=年龄: 65岁, bbox=[208, 148, 296, 168]
2026-08-06 10:30:14,913 INFO     30 [qwen-vl-text] coord item[12]: text=QRS时限: 101ms, bbox=[407, 132, 513, 151]
2026-08-06 10:30:14,913 INFO     30 [qwen-vl-text] coord item[13]: text=【60-110】, bbox=[582, 134, 639, 152]
2026-08-06 10:30:14,913 INFO     30 [qwen-vl-text] coord item[14]: text=科室: 日间化疗中心[心率: 77bpm, bbox=[58, 181, 304, 201]
2026-08-06 10:30:14,913 INFO     30 [qwen-vl-text] coord item[15]: text=【60-100】, bbox=[337, 181, 392, 200]
2026-08-06 10:30:14,913 INFO     30 [qwen-vl-text] coord item[16]: text=QT/QTc: 358/406ms, bbox=[407, 155, 539, 175]
2026-08-06 10:30:14,913 INFO     30 [qwen-vl-text] coord item[17]: text=【360-440】, bbox=[582, 157, 645, 175]
2026-08-06 10:30:14,913 INFO     30 [qwen-vl-text] coord item[18]: text=东院区], bbox=[117, 196, 160, 215]
2026-08-06 10:30:14,913 INFO     30 [qwen-vl-text] coord item[19]: text=电轴: 60°, bbox=[411, 182, 498, 202]
2026-08-06 10:30:14,913 INFO     30 [qwen-vl-text] coord item[20]: text=【-30-90】, bbox=[582, 183, 638, 202]
2026-08-06 10:30:14,913 INFO     30 [qwen-vl-text] coord item[21]: text=2026-03-23 08:43:55, bbox=[86, 235, 203, 254]
2026-08-06 10:30:14,913 INFO     30 [qwen-vl-text] coord item[22]: text=25mm/s 10mm/mV, bbox=[824, 234, 940, 253]
2026-08-06 10:30:14,913 INFO     30 [qwen-vl-text] coord item[23]: text=I, bbox=[87, 278, 97, 295]
2026-08-06 10:30:14,913 INFO     30 [qwen-vl-text] coord item[24]: text=V1, bbox=[366, 277, 383, 295]
2026-08-06 10:30:14,914 INFO     30 [qwen-vl-text] coord item[25]: text=V3R, bbox=[650, 277, 676, 294]
2026-08-06 10:30:14,914 INFO     30 [qwen-vl-text] coord item[26]: text=II, bbox=[86, 372, 98, 389]
2026-08-06 10:30:14,914 INFO     30 [qwen-vl-text] coord item[27]: text=V2, bbox=[367, 372, 385, 390]
2026-08-06 10:30:14,914 INFO     30 [qwen-vl-text] coord item[28]: text=III, bbox=[86, 467, 98, 484]
2026-08-06 10:30:14,914 INFO     30 [qwen-vl-text] coord item[29]: text=V3, bbox=[367, 467, 385, 485]
2026-08-06 10:30:14,914 INFO     30 [qwen-vl-text] coord item[30]: text=V4R, bbox=[650, 467, 676, 485]
2026-08-06 10:30:14,914 INFO     30 [qwen-vl-text] coord item[31]: text=aVR, bbox=[85, 561, 109, 578]
2026-08-06 10:30:14,914 INFO     30 [qwen-vl-text] coord item[32]: text=V4, bbox=[367, 561, 385, 579]
2026-08-06 10:30:14,914 INFO     30 [qwen-vl-text] coord item[33]: text=aVL, bbox=[85, 656, 108, 673]
2026-08-06 10:30:14,914 INFO     30 [qwen-vl-text] coord item[34]: text=V5, bbox=[367, 656, 385, 674]
2026-08-06 10:30:14,914 INFO     30 [qwen-vl-text] coord item[35]: text=V5R, bbox=[650, 656, 676, 674]
2026-08-06 10:30:14,915 INFO     30 [qwen-vl-text] coord item[36]: text=aVF, bbox=[85, 750, 108, 768]
2026-08-06 10:30:14,915 INFO     30 [qwen-vl-text] coord item[37]: text=V6, bbox=[367, 750, 385, 768]
2026-08-06 10:30:14,916 INFO     30 [qwen-vl-text] coord item[38]: text=II, bbox=[86, 845, 98, 862]
2026-08-06 10:30:14,916 INFO     30 [qwen-vl-text] coord item[39]: text=检查时间: 2026/3/23 8:43:55, bbox=[58, 945, 238, 965]
2026-08-06 10:30:14,916 INFO     30 [qwen-vl-text] coord item[40]: text=报告时间: 2026/3/23 8:59:30, bbox=[297, 944, 486, 964]
2026-08-06 10:30:14,916 INFO     30 [qwen-vl-text] coord item[41]: text=报告医生:, bbox=[563, 943, 620, 963]
2026-08-06 10:30:14,917 INFO     30 [qwen-vl-text] coord item[42]: text=审核医生:, bbox=[751, 944, 809, 964]
2026-08-06 10:30:14,925 INFO     30 [qwen-vl-text] page=8 — 43/43 coords, api_time=23.9s
2026-08-06 10:30:14,926 INFO     30 [qwen-vl-text] new_positions (43):
[[8, 848.9440000000001, 1391.5680000000002, 39.168, 84.86399999999999], [8, 126.90400000000001, 227.55200000000002, 138.72, 171.35999999999999], [8, 455.10400000000004, 555.7520000000001, 137.088, 169.72799999999998], [8, 890.5160000000001, 1122.4440000000002, 133.82399999999998, 166.464], [8, 1450.644, 1691.324, 114.24, 150.14399999999998], [8, 126.90400000000001, 315.072, 190.944, 223.58399999999997], [8, 455.10400000000004, 621.392, 187.67999999999998, 220.32], [8, 890.5160000000001, 1122.4440000000002, 174.624, 207.26399999999998], [8, 1273.4160000000002, 1411.2600000000002, 174.624, 205.63199999999998], [8, 1546.9160000000002, 1662.88, 148.512, 179.51999999999998], [8, 126.90400000000001, 297.56800000000004, 244.79999999999998, 277.44], [8, 455.10400000000004, 647.648, 241.53599999999997, 274.176], [8, 890.5160000000001, 1122.4440000000002, 215.42399999999998, 246.432], [8, 1273.4160000000002, 1398.132, 218.688, 248.064], [8, 126.90400000000001, 665.152, 295.392, 328.032], [8, 737.3560000000001, 857.696, 295.392, 326.4], [8, 890.5160000000001, 1179.332, 252.95999999999998, 285.59999999999997], [8, 1273.4160000000002, 1411.2600000000002, 256.224, 285.59999999999997], [8, 255.996, 350.08000000000004, 319.87199999999996, 350.88], [8, 899.268, 1089.624, 297.024, 329.664], [8, 1273.4160000000002, 1395.9440000000002, 298.656, 329.664], [8, 188.168, 444.16400000000004, 383.52, 414.52799999999996], [8, 1802.912, 2056.7200000000003, 381.888, 412.89599999999996], [8, 190.35600000000002, 212.23600000000002, 453.69599999999997, 481.43999999999994], [8, 800.8080000000001, 838.004, 452.06399999999996, 481.43999999999994], [8, 1422.2, 1479.0880000000002, 452.06399999999996, 479.808], [8, 188.168, 214.424, 607.1039999999999, 634.848], [8, 802.9960000000001, 842.3800000000001, 607.1039999999999, 636.4799999999999], [8, 188.168, 214.424, 762.144, 789.8879999999999], [8, 802.9960000000001, 842.3800000000001, 762.144, 791.52], [8, 1422.2, 1479.0880000000002, 762.144, 791.52], [8, 185.98000000000002, 238.49200000000002, 915.5519999999999, 943.2959999999999], [8, 802.9960000000001, 842.3800000000001, 915.5519999999999, 944.9279999999999], [8, 185.98000000000002, 236.30400000000003, 1070.5919999999999, 1098.336], [8, 802.9960000000001, 842.3800000000001, 1070.5919999999999, 1099.9679999999998], [8, 1422.2, 1479.0880000000002, 1070.5919999999999, 1099.9679999999998], [8, 185.98000000000002, 236.30400000000003, 1224.0, 1253.376], [8, 802.9960000000001, 842.3800000000001, 1224.0, 1253.376], [8, 188.168, 214.424, 1379.04, 1406.7839999999999], [8, 126.90400000000001, 520.744, 1542.24, 1574.8799999999999], [8, 649.836, 1063.3680000000002, 1540.608, 1573.2479999999998], [8, 1231.844, 1356.5600000000002, 1538.9759999999999, 1571.616], [8, 1643.188, 1770.092, 1540.608, 1573.2479999999998]]
2026-08-06 10:30:14,927 INFO     30 [qwen-vl-text] ═══ DONE ═══ 43 positions, pages=1, time=30.1s
2026-08-06 10:30:14,962 INFO     30 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-06 10:30:14,964 INFO     30 [Trace] task=6a97f83c | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | Extractor:ExaminationReport | outputs={"chunks": "5 items, types={'ExaminationReport': 5}", "html": "", "json": "309 items", "markdown": "", "text": "", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf", "output_format": "chunks", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Admission\": 1, \"chunks_Examination\": 5, \"chunks_LabExam\": 3}"}
2026-08-06 10:30:14,964 INFO     30 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-06 10:30:14,973 INFO     30 [ChunkMerger] Merged 9 chunks from 8 sources: {'Extractor:LabExam': 3, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 5} (filtered 5 noise chunks)
2026-08-06 10:30:15,344 INFO     30 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-06 10:30:15,345 INFO     30 [Trace] task=6a97f83c | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "9 items, types={'LabReport': 3, 'AdmissionRecord': 1, 'ExaminationReport': 5}", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf"}
2026-08-06 10:30:15,346 INFO     30 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-06 10:30:19,473 INFO     30 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786011870181, 'update_date': datetime.datetime(2026, 8, 6, 10, 24, 30), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 579274, 'status': '1'}
2026-08-06 10:30:19,851 INFO     30 [EMBED-PIPELINE] batch[0:16] text_for_embed=   癌胚抗原  CEA  5.03  ng/mL  0—5.2  False    非小细胞肺癌相关抗原  CYFRA21-1  4.60  ng/ml  0—3.3  True    神经元特异性烯醇化酶测定  NSE  10.60  ng/mL  0—16.3  False   
---
   谷丙转氨酶  ALT  52  U/L  7—40  True    谷草转氨酶  AST  54  U/L  13—35  True    总蛋白  TP  69.8  g/L  65—85  False    白蛋白  ALB  48.5  g/L  40—55  False    球蛋白  GLOB  21.3  g/L  20—40  False    白球比  A/G  2.3  None  1.2—2.4  False    总胆红素  TBIL  13.6  umol/L  1.7—21  False    直接胆红素  DBIL  1.7  umol/L  0—6.8  False    间接胆红素  IBIL  11.9  umol/L  3—13.6  False    碱性磷酸酶  ALP  67  U/L  50—135  False    谷氨酰转肽酶  GGT  19  U/L  7—45  False    尿素  UREA  4.15  mmol/L  2.76—8.07  False    肌酐  CREA  94  umol/L  45—84  True    尿酸  UA  192  umol/L  143—339  False    二氧化碳  CO2  25.9  mmol/L  22—29  False    葡萄糖  GLU  6.25  mmol/L  3.8—6.1  True    乳酸脱氢酶  LDH  291  U/L  135—214  True    肌酸激酶  CK  396  U/L  26—192  True    肌酸酶同功酶  CK-MB  17.70  U/L  7—25  False    肌红蛋白  MYO  77.4  ug/L  0—70  True    钾  K  3.74  mmol/L  3.5—5.3  False    钠  NA  132  mmol/L  137—147  True    氯  CL  96.0  mmol/L  99—110  True    钙  CA  2.12  mmol/L  2.02—2.6  False    C反应蛋白  CRP  0.41  mg/L  0—5  False    估算肾小球滤  eGFR  55.02  ml/min  None  False   
---
   白细胞  WBC  3.62  10^9/L  3.5--9.5  False    中性粒细胞百分比  NEUT  68.80  %  40--75  False    淋巴细胞百分比  LYMP  23.20  %  20--50  False    单核细胞百分比  MONO  4.10  %  3--10  False    嗜酸性粒细胞百分比  EOS%  2.5  %  0.4--8  False    嗜碱性粒细胞百分比  BASO  1.40  %  0--1  True    中性粒细胞计数  NEUT  2.49  10^9/L  1.8--6.3  False    淋巴细胞计数  LYMP  0.84  10^9/L  1.1--3.2  True    单核细胞计数  MONO  0.15  10^9/L  0.1--0.6  False    嗜酸性粒细胞计数  EOS#  0.09  10^9/L  0.02--0.52  False    嗜碱性粒细胞计数  BASO  0.05  10^9/L  0--0.06  False    红细胞  RBC  4.06  10^12/L  3.8--5.1  False    血红蛋白  HGB  125  g/L  115--150  False    红细胞压积  HCT  36.30  %  35--45  False    红细胞平均体积  MCV  89.4  fL  82--100  False    平均血红蛋白量  MCH  30.8  pg  27--34  False    平均血红蛋白浓度  MCHC  344  g/L  316--354  False    红细胞分布宽度标准  RDW-  43  fL  35--56  False    红细胞分布宽度变异  RDW-  13  %  11--16  False    血小板  PLT  155  10^9/L  125--350  False    血小板分布宽度  PDW  10.20  fL  9.2--15.6  False    平均血小板体积  MPV  9.90  fL  6.5--12  False    血小板压积  PCT  0.150  %  0.108--0.282  False    大型血小板比率  P-LC  24.00  %  11--45  False    大血小板数目  PLCC  37.20  10^9/L  30--90  False   
---
2025.1 确诊小细胞癌，已行免疫组化协诊
2025-.2-4给予" EP" 化疗联合" 特瑞普利单抗" 免疫治疗3周期，
2025-04-22给予" EP" 方案化疗联合
" 替雷利珠单抗" 免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗
2025.5-8 行" 特瑞普利单抗" 免疫治疗4周期
2025.8 PD
2025.8-2026.2 " 替雷利珠单抗联合安罗替尼" 免疫治疗
1804 - Internet Explorer
诊疗与病历 申请单 手术管理 医嘱单 会诊管理 重症管理 需关注医嘱 病情总览 质量管理 更多
汤光冉 住院医师
日间化疗中心[东院区]
住院天数: 1 费别: 全国医保居民 余额: 0.00 诊断: 肺恶性肿瘤,恶性肿瘤... 医疗救助类型: 农村低保
病人列表 全息视图
操作 编辑 功能 表格 其他
保存 打印 自动续打 预览 单独打印 手工解锁 隐藏留痕 病历参考 更新数据 首页
信阳市中心医院
日间化疗出入院记录
姓名: 性别:女年龄:65岁 科别:日间化疗中心[东院床号:04 登记号:0000 住院号:25
区]
入院时间: 2026年03月23日 08:29:00出院时间: 2026年03月23日 11:14:00 住院天数: 1天
主诉: 确诊肺癌1年余
入院情况: 1年余前因“胸闷”就诊我院, 2025-01-17CT增强64: 1.右肺门占位, 考虑恶性病变并
右肺中下叶不张, 右下肺动受侵可能。2. 双肺纤维索条灶。双肺多发小结节, 转移待排。3.右侧
胸腔少量积液。4.双肾小囊肿。5.升结肠多发憩室。6.子宫后壁肌瘤可能。7.冠状动脉CTA未见明
显异常。2025-01-23行纤支镜下肺活检, 2025-01-23 活体组织病理申请 诊断意见: (右中间段支
气管)考虑小细胞癌, 已行免疫组化协诊。2025-01-26 免疫组化申请: CK广谱 (点+), CD56 (+),
Syn (+), INSM1 (+), CK5/6 (-), P40 (-), TTF1 (+), NapsinA (-), Ki-67 (80%+)。结合HE
及免疫组化结果, (右中间段支气管)肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04
-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期, 2025-04-22给予“EP”方案化疗联合
“替雷利珠单抗”免疫治疗1周期, 化疗后呕吐反应较重, 予以对症支持治疗。2025-05-19、2025
-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加增强
(胸部,上腹部,下腹部) 诊断意见: 1. 右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节。
100%
16:56
2026/3/23
胸腔少量积液。4.双肾小囊肿。5.升结肠多发息室。6.丁台加壁肌瘤可能。冠状动脉CT示无明显异常。2025-01-23行纤支镜下肺活检，2025-01-23活体组织病理申请 诊断意见：(右中间段支气管)考虑小细胞癌，已行免疫组化协诊。2025-01-26免疫组化申请：CK广谱(点+)，CD56(+)，Syn(+)，INSM1(+)，CK5/6(-)，P40(-)，TTF1(+),NapsinA(-)，Ki-67(80%+)。结合HE及免疫组化结果，(右中间段支气管)肺小细胞神经内分泌癌。2025-02-05、2025-02-28、2025-04-01给予“EP”化疗联合“特瑞普利单抗”免疫治疗3周期，2025-04-22给予“EP”方案化疗联合“替雷利珠单抗”免疫治疗1周期，化疗后呕吐反应较重，予以对症支持治疗。2025-05-19、2025-06-09、2025-07-03、2025-08-01行“特瑞普利单抗”免疫治疗4周期。2025-08-21CT平扫加强(胸部，上腹部，下腹部)诊断意见：1.右肺癌并右肺中下叶不张治疗后改变。双肺多发小结节，转移瘤可能；建议追踪复查。2.双肺慢性炎症，右肺中叶局限性支扩，双侧胸腔少量积液。3.脾脏低密度灶，建议追踪复查。4.胆囊可疑小结石。升结肠多发憩室。5.双肾小囊肿。与2025-05-18日片比较：右肺中叶局限性支扩，右肺下叶内基底段结节较前增大，右肺门淋巴结较前增大。考虑病情进展，于2025-08-23给予“安罗替尼12mg”联合“替雷利珠单抗”抗肿瘤治疗1周期。后于2025-08-25、2025-09-17、2025-10-11、2025-11-04、2025-12-02、2025-12-22、2026-01-22、2026-02-22行“替雷利珠单抗联合安罗替尼”免疫治疗8周期，今为行下周期抗肿瘤治疗来我院。门诊以“肺癌”收入我科。自发病以来，神志清，精神可，饮食、睡眠可，大小便可，体重无明显变化。诊疗经过：入院后完善相关检查，无禁忌行本周期“替雷利珠单抗”免疫抗肿瘤治疗。过程顺利，予办理出院手续。
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
以电子胶
片和报告(试用)
影像号: 0000
报告日期: 2026-02-25 15:36
姓名:
性别: 女
年龄: 65岁
检查日期: 2026-02-25
科别: 肿瘤内科五门诊[东院
住院号: /
门诊号: 1
6
检查时间: 08:57:41
检查方法: 胸部CT平扫加薄层
技术参数:
影像学所见:
双侧胸廓对称, 右肺门增大, 可见不规则状软组织密度影, 密度不均, 边
界不清, 右肺中下叶支气管稍变窄, 双肺可见条索状及结节状高密度影。右肺
中叶局限性支扩。气管、支气管通畅, 右肺门见明显肿大淋巴结, 右侧胸膜局
部稍厚, 双侧胸膜腔及心包腔可见积液征象。与2025-12-22日片比较: 右侧胸
腔积液增多, 右肺门软组织密度影及淋巴结进一步增大, 右肺结节增大, 右侧
胸膜局部稍增厚。
影像学意见:
1. 右肺癌并右肺中下叶不张治疗状态。双肺多发结节, 转移瘤可能; 右肺门
肿大淋巴结转移。
2. 双肺慢性炎症, 双侧胸腔积液, 心包积液。
3. 右侧胸膜局部稍厚, 不除外转移。
报告医师:
肖健
审核医师:
贺玲
此报告仅供临床医师参考, 签字生效
打印时间: 2026-02-25 15:36:58
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
2026-08-06 10:30:20,048 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:30:20.045+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 8, "lag": 0, "done": 0, "failed": 0, "current": {"6a97f83c918011f18dbe1f8f96f1c395": {"id": "6a97f83c918011f18dbe1f8f96f1c395", "doc_id": "688aee0a918011f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909798, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011615561, "task_type": "dataflow", "root_trace_id": "d05a3d8d0d6c4aa38394753a3ea0008c", "root_traceparent": "00-d05a3d8d0d6c4aa38394753a3ea0008c-2c380740bfb060e1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "00b9d592918111f18dbe1f8f96f1c395": {"id": "00b9d592918111f18dbe1f8f96f1c395", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011867426, "task_type": "dataflow", "root_trace_id": "1ab3198c92574fb4b2701d0f5db7322f", "root_traceparent": "00-1ab3198c92574fb4b2701d0f5db7322f-bdaff6f64a5f4a64-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:30:21,749 INFO     30 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-06 10:30:21,750 INFO     30 [Trace] task=6a97f83c | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "9 items, types={'LabReport': 3, 'AdmissionRecord': 1, 'ExaminationReport': 5}", "name": "十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf", "embedding_token_consumption": 5927}
2026-08-06 10:30:21,750 INFO     30 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-06 10:30:23,353 INFO     30 [qwen-vl-parser] text API response (len=1576):
["既往史：2025年11月24日-2025年12月12日本院儿科门诊就诊代家属开药，否认3个月内其他病史及合并用药/非药物治疗，现患者无盆腔炎性疾病急性发作，否认既往有子宫肌瘤、子宫内膜异位症、子宫腺肌病、结核性盆腔炎、间质性膀胱炎、异常子宫出血、盆腔淤血综合征、子宫颈高级别上皮内病变等其他病症引起相关症状者；未放置宫内节育器；无子宫及双侧附件缺如；近2周内未使用过本方案规定研究期间禁止使用的治疗（包括药物和非药物治疗）；无控制不稳定的心血管、肝、肾和血液系统、糖尿病、甲状腺疾病等严重原发性疾病；获得知情同意书前5年内未患有恶性肿瘤；否认对试验用药品过敏，包括对本品成分或者药物辅料有过敏史；否认长期酗酒、药物滥用史；无智力障碍或精神障碍；近1个月内未参加过任何干预性临床试验；患者当前不在妊娠期、哺乳期，同意在试验期间及试验结束后3个月内采取有效避孕措施。", "婚育史：已婚已育，孕2产2，有性生活史", "手术史：2016年8月31日、2020年7月9日因生产行剖宫产手术", "月经史：初潮12岁，既往月经周期规律，经量中，色红，无痛经，末次月经2025.12.29-2025.1.2，周期26-28天，经期5天，经量较前不变", "过敏史：无", "生命体征：2026.1.6测量身高：160.0cm 体重：51.0kg 体温：36.4℃ 脉搏：76次/分 呼吸：18次/分 血压：98/76mmHg", "体格检查：淋巴结、头颈部、胸部、脊柱/四肢/关节、神经系统未见异常，腹部异常（左下腹压痛，CS，研究疾病相关），皮肤黏膜异常（腹部皮肤约5-6cm剖宫产手术瘢痕，NCS），其他未查。", "专科检查：外阴已婚型，阴道畅，宫颈光滑，无摇举痛，有宫体压痛，无子宫活动受限或粘连固定，左侧附件区、右侧附件区压痛，无宫骶韧带增粗、变硬、触痛。", "辅助检查：今日按方案要求开具血常规、尿沉渣（含尿常规）、肝功八项、肾功两项、血妊娠、血沉、血清CA-125、妇科微生态、十二导联心电图、妇科阴道彩色B超检查，结果详见检查单。", "初步印象：盆腔痛中医辨证：主症：下腹胀痛，腰骶部胀痛、带下量多；次症：神疲乏力、口苦口腻、小便黄；舌象：舌质红、苔黄腻；脉象：脉弦滑；2026年01月06日由张丹丹医生辨证为湿热瘀阻症。 西医：盆腔炎性疾病后遗症，慢性盆腔痛", "从细之间、根据目前临床表现及患者情况，权丽丽医生于2026年01月06日08时38分在9号楼4楼医患沟通室向患者“妇科千金片治疗盆腔炎性疾病后遗症（湿热瘀阻证）的随机、双盲、安慰剂平行对照、多中心临床试验”及知情同意书内容，已告知参加试验可能的风险与获益，患者已充分理解并同意参加该研究，未提出问题，患者本人于2026年01月06日08时58分签署知情同意书（版本号：V1.0 三门峡市中心医院专用版，版本日期：2025年08月05日），权丽丽医生于2026年01月06日08时59分签署知情同意书（版本号：V1.0 三门峡市中心医院专用版，版本日期：2025年08月05日），知情同意书原件一份保存于受试者文件夹，一份交给患者本人，确定患者筛选号为04011，进入试验筛选，根据方案要求，收集受试者的试验相关资料，并于今日开始进行筛选期相关检查。", "1.已完成体征McCormack量表评分，总分8分，回顾近1周非经期腹痛/腰骶疼痛NRS平均分为5分。", "2.嘱受试者合理饮食，避免过度劳累；避免盆浴和坐浴，避免穿紧身衣物和化纤内裤；注意经期卫生。", "3.今日结合受试者情况，2026年1月6日血清CA-125示：59.70（0.00-35.00）U/mL，符合排除标准第（8）条，筛选失败，告知受试者转为门诊常规诊疗。", "备注：", "医师签名："]
2026-08-06 10:30:23,355 INFO     30 [qwen-vl-parser] page=30 text: 16 lines (bbox 1801-1816)
2026-08-06 10:30:23,356 INFO     30 [qwen-vl-parser] page=30 text: 16 sections
2026-08-06 10:30:24,022 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=937019, prompt_len=764
2026-08-06 10:30:24,767 INFO     30 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-06 10:30:24,768 INFO     30 [Trace] task=6a97f83c | doc=十堰-ZCQI-小肺-方穹推荐706-I期（IA期）.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":9,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-06 10:30:24,801 INFO     30 [DIAG-EXECUTOR] row_position_int len=3 row[0]=(10, 712, 848, 511, 546) row[-1]=(10, 712, 1111, 604, 639)
2026-08-06 10:30:24,802 INFO     30 [DIAG-EXECUTOR] row_position_int len=26 row[0]=(11, 426, 576, 297, 327) row[-1]=(11, 1158, 1334, 628, 656)
2026-08-06 10:30:24,802 INFO     30 [DIAG-EXECUTOR] row_position_int len=25 row[0]=(12, 174, 251, 278, 302) row[-1]=(12, 899, 1056, 627, 652)
2026-08-06 10:30:24,803 INFO     30 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 10:30:24,804 INFO     30 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 10:30:24,804 INFO     30 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 10:30:24,805 INFO     30 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 10:30:24,805 INFO     30 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 10:30:24,806 INFO     30 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 10:30:24,834 INFO     30 set_progress(6a97f83c918011f18dbe1f8f96f1c395), progress: 0.82, progress_msg: 10:30:24 [DOC Engine]:
Start to index...
2026-08-06 10:30:24,983 INFO     30 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.118s]
2026-08-06 10:30:24,999 INFO     30 set_progress(6a97f83c918011f18dbe1f8f96f1c395), progress: 0.8111111111111111, progress_msg: 
2026-08-06 10:30:25,076 INFO     30 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.044s]
2026-08-06 10:30:25,134 INFO     30 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.042s]
2026-08-06 10:30:25,193 INFO     30 set_progress(6a97f83c918011f18dbe1f8f96f1c395), progress: 1.0, progress_msg: 10:30:25 Indexing done (0.34s). Task done (574.05s)
2026-08-06 10:30:25,217 INFO     30 [Done], chunks(9), token(5927), elapsed:574.05
2026-08-06 10:30:25,525 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:30:25,526 INFO     30 [qwen-vl-parser] page=31 classify=text report_date=None
2026-08-06 10:30:25,582 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=937019, prompt_len=401
2026-08-06 10:30:25,885 INFO     30 handle_task done for task {"id": "6a97f83c918011f18dbe1f8f96f1c395", "doc_id": "688aee0a918011f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "type": "pdf", "location": "\u5341\u5830-ZCQI-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-I\u671f\uff08IA\u671f\uff09.pdf", "size": 10909798, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786011615561, "task_type": "dataflow", "root_trace_id": "d05a3d8d0d6c4aa38394753a3ea0008c", "root_traceparent": "00-d05a3d8d0d6c4aa38394753a3ea0008c-2c380740bfb060e1-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
