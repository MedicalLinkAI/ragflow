# 基准结果：徐州-LIYE-小肺-方穹推荐706-Ia期.pdf

## 基本信息

- 文件：`徐州-LIYE-小肺-方穹推荐706-Ia期.pdf`
- 大小：2804.8 KB
- PDF 总页数：14
- doc_id：`de8a02fc918111f18dbe1f8f96f1c395`
- 上传方式：skip
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-07T12:59:10  完成时间：2026-08-07T12:59:11  耗时：1.1s
- progress_msg：`10:38:16 Indexing done (0.11s). Task done (451.19s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | cc541d82 | 4 | 1-4 | 2025.5.21确诊小细胞肺癌 2025.5.28-2025.7.16 依托泊 |
| 2 | 3bee89a0 | 1 | 5-5 | 河北省人民医院 病理检查报告单 病理号 姓名: 性别: 女 年龄: 74岁 送检 |
| 3 | 39833a50 | 2 | 5-6 | 住院病历 河北省人民医院 病理检查补充报告单 病理号: 姓名: 性别: 女 年龄 |
| 4 | 03b5a25c | 1 | 7-7 | 南京鼓楼医院云胶片 南京鼓楼医院 南京大学医学院附属鼓楼医院 影像检查诊断报告  |
| 5 | 6fcce1c4 | 4 | 8-11 | 南京鼓楼医院云胶片 女/75岁 设备类型 CT 患者类型 无 检查项目 [CT平 |
| 6 | b39333f1 | 1 | 12-12 | 南京鼓楼医院 南京大学医学院附属鼓楼医院 互联网医院 门诊病历 姓名: 性别:女 |
| 7 | f460f05d | 1 | 13-13 | <table><tr><td>白细胞计数</td><td>WBC</td><td |
| 8 | 92cae422 | 1 | 14-14 | <table><tr><td>丙氨酸氨基转移酶</td><td>ALT</td> |

- chunks 总数：8
- 各 chunk 页数合计（含跨页重复）：15
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]`
- 覆盖页数：14 / 14；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 1 | 0 | 1 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 1 | 1 | 1 | admission_date, discharge_date, department, outcome | **OK** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 4 | 4 | 4 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 2 | 0 | 2 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"DischargeRecord": 1, "ExaminationReport": 4, "OutpatientRecord": 1, "LabReport": 2}`
- ChunkMerger：`{"found": true, "merged": 8, "sources": 8, "stats": {"Extractor:LabExam": 2, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 4}, "filtered_noise": 4}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-06 10:38:10,886 INFO     30 [ChunkMerger] Merged 8 chunks from 8 sources: {'Extractor:LabExam': 2, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-06 10:30:41,622 INFO     30 handle_task begin for task {"id": "dfc102e2918111f18dbe1f8f96f1c395", "doc_id": "de8a02fc918111f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786012241604, "task_type": "dataflow", "root_trace_id": "90f550f6b00248c3845d57a8e0bcf6fb", "root_traceparent": "00-90f550f6b00248c3845d57a8e0bcf6fb-5db7fb7d470dfe0d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-06 10:30:41,992 INFO     30 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.004s]
2026-08-06 10:30:42,400 INFO     30 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-06 10:30:42,463 INFO     30 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-06 10:30:42,464 INFO     30 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-06 10:30:42,492 INFO     30 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-06 10:30:42,492 INFO     30 ============================================================
2026-08-06 10:30:42,492 INFO     30 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-06 10:30:42,492 INFO     30    model_dir : /ragflow/rag/res/deepdoc
2026-08-06 10:30:42,492 INFO     30 ============================================================
2026-08-06 10:30:42,492 INFO     30 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-06 10:30:42,492 INFO     30 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-06 10:30:42,497 INFO     30 No torch found.
2026-08-06 10:30:42,912 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:30:42,913 INFO     30 [qwen-vl-parser] page=33 classify=text report_date=None
2026-08-06 10:30:42,946 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1002302, prompt_len=401
2026-08-06 10:30:45,352 INFO     30 [qwen-vl-parser] parse_pdf start, total_pages=14
2026-08-06 10:30:45,479 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=145687, prompt_len=764
2026-08-06 10:30:46,862 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:30:46,863 INFO     30 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-06 10:30:46,882 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=145687, prompt_len=401
2026-08-06 10:30:47,909 INFO     30 [qwen-vl-parser] text API response (len=87):
["2025.5.21确诊小细胞肺癌", "2025.5.28-2025.7.16 依托泊苷+卡铂+斯鲁利", "2025.8.13-2025.11.7 依托泊苷+斯鲁利"]
2026-08-06 10:30:47,910 INFO     30 [qwen-vl-parser] page=1 text: 3 lines (bbox 0-2)
2026-08-06 10:30:47,910 INFO     30 [qwen-vl-parser] page=1 text: 3 sections
2026-08-06 10:30:48,190 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1071362, prompt_len=764
2026-08-06 10:30:49,808 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:30:49,809 INFO     30 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-06 10:30:49,840 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1071362, prompt_len=401
2026-08-06 10:30:50,469 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:30:50.468+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 8, "lag": 0, "done": 1, "failed": 0, "current": {"00b9d592918111f18dbe1f8f96f1c395": {"id": "00b9d592918111f18dbe1f8f96f1c395", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011867426, "task_type": "dataflow", "root_trace_id": "1ab3198c92574fb4b2701d0f5db7322f", "root_traceparent": "00-1ab3198c92574fb4b2701d0f5db7322f-bdaff6f64a5f4a64-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "dfc102e2918111f18dbe1f8f96f1c395": {"id": "dfc102e2918111f18dbe1f8f96f1c395", "doc_id": "de8a02fc918111f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786012241604, "task_type": "dataflow", "root_trace_id": "90f550f6b00248c3845d57a8e0bcf6fb", "root_traceparent": "00-90f550f6b00248c3845d57a8e0bcf6fb-5db7fb7d470dfe0d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:30:52,040 INFO     30 [qwen-vl-parser] text API response (len=1176):
["50/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView", "984-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>", "时间：2026-02-12 11:40.02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森", "返回概览视图", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告", "请输入药品内容，按回车键检索", "查询全部", "类型 组 药品名称(规格) 用法 频率 实际用量 总量 开立时间 开立医师", "药品 鼻渊通窍颗粒 口服 bid 1袋 2 2025-11-27 15:02.43 烟海丽", "药品 盐酸氮卓斯丁滴眼液 滴眼 qid 0.01ml 1 2025-09-18 15:29.34 赵艳", "药品 阿莫西林克拉维酸钾片(选) 口服(继续用药) tid 0.375g 24 2025-09-18 15:25.48 赵艳", "药品 (成人)双黄连口服液(选) 口服 tid 20ml 2 2025-09-18 15:25.48 赵艳", "药品 (160ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 160ug 1 2025-07-11 10:07.36 赵艳", "药品 (小儿)双黄连口服液(选) 口服 tid 20ml 2 2025-06-23 10:52.35 谭真真", "药品 (顺尔宁片)孟鲁司特钠片(选) 口服 qn 10mg 30 2025-05-09 17:04.48 段竹云", "药品 (320ug)布地奈德福莫特罗粉吸入剂 吸入 bid 320ug 2 2025-05-09 17:04.48 段竹云", "药品 醋酸泼尼松片 口服 qm 30mg 36 2025-04-11 15:46.53 刘秀层", "药品 鼻炎康莫米松鼻喷雾剂(选) 喷鼻 bid 100ug 1 2025-04-11 15:31.05 段竹云", "药品 (顺尔宁片)孟鲁司特钠片(选) 口服 qn 10mg 5 2025-04-11 15:31.05 段竹云", "药品 (320ug)布地奈德福莫特罗粉吸入剂 吸入 bid 320ug 1 2025-04-11 15:31.05 段竹云", "药品 磷酸奥司他韦胶囊(东阳光) 口服 bid 75mg 10 2025-01-06 17:15.28 谭真真", "药品 氯雷他定颗粒 口服 qd 10mg 1 2024-12-30 10:40:10 谭真真", "共70条 20条/页 < 1 2 3 4 > 前往 1", ""]
2026-08-06 10:30:52,040 INFO     30 [qwen-vl-parser] page=33 text: 23 lines (bbox 1910-1932)
2026-08-06 10:30:52,040 INFO     30 [qwen-vl-parser] page=33 text: 23 sections
2026-08-06 10:30:52,338 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=859617, prompt_len=764
2026-08-06 10:30:53,811 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:30:53,812 INFO     30 [qwen-vl-parser] page=34 classify=text report_date=None
2026-08-06 10:30:53,836 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=859617, prompt_len=401
2026-08-06 10:30:58,928 INFO     30 [qwen-vl-parser] text API response (len=1268):
["南京鼓楼医院", "南京大学医学院附属鼓楼医院", "出院记录", "科别（江北）综合肿瘤中心 病区（江北）B7病区床号07床 姓名", "住院号", "姓名：", "性别：女 年龄：75岁 婚姻：已婚 职业：农民", "入院诊断：1. 肺恶性肿瘤（左肺，小细胞癌广泛期）2. 肥 入院日期： 2025年12月03日", "厚型梗阻性心肌病 3. 纵隔淋巴结肿大 4. 肺门", "淋巴结肿大 5. 锁骨上淋巴结肿大（双侧）6. 腋", "下淋巴结肿大（右）7. 心功能III级（NYHA分级）", "8. 甲状腺功能减退症 9. 高血压2级（极高", "危）10. 肺气肿（局限性）11. 肺诊断性影像检", "查的异常所见（肺结节）12. 二尖瓣反流（重度）", "13. 心包积液（少量）14. 肾上腺结节（左侧）", "手术名称：", "手术日期：", "出院诊断：1. 恶性肿瘤支持治疗 2. 恶性肿瘤免疫治 出院日期： 2025年12月06日", "疗 3. 肺恶性肿瘤（左肺，小细胞癌广泛期）", "4. 肥厚型梗阻性心肌病 5. 纵隔淋巴结肿大", "6. 肺门淋巴结肿大 7. 锁骨上淋巴结肿大", "(双侧) 8. 腋下淋巴结肿大(右) 9. 心功能", "III级(NYHA分级) 10. 甲状腺功能减退症", "11. 高血压2级（极高危）12. 肺气肿(局", "限性) 13. 肺诊断性影像检查的异常所见(肺", "结节) 14. 二尖瓣反流(重度) 15. 心包积", "液(少量) 16. 肾上腺结节(左侧)", "入院时情况（主要症状、体征，有关实验室及器械检查结果）：", "患者因“咳嗽1月余”于2025-05-21至河北省人民医院就诊，查胸部CT：左肺下叶占位性病变，恶性不除", "外，远端阻塞性肺炎，建议完善实验室检查及增强CT。双侧锁骨窝、右侧腋下、纵隔内及双肺门多发肿大", "淋巴结，转移不除外。左侧胸膜结节样增厚，转移不除外。后于2025-05-23行肺穿刺活检术，术后病理回", "示：（左肺）穿刺组织：结合免疫组化染色支持小细胞癌。免疫组化染色： CKpan (+)，Vimentin (-)，", "CK7 (+)，TTF -1(+)，NapsinA (-)，CK5/6(-)，P40(-)，P63(-)，CgA (+)，Syn (+)，CD56(+)。根据患者病情", "于2025-05-28当地医院行依托泊苷+卡铂方案化疗+斯鲁利单抗免疫治疗1周期，过程顺利。于", "2025-06-19、2025-07-16开始行依托泊苷+卡铂化疗+斯鲁利单抗免疫治疗2周期，过程顺利。2025-07-27复", "查血常规示血小板38×10^9/L。予升血小板治疗后。2025-08-13、2025-09-06、2025-10-08、2025-11-07", "行依托泊苷化疗+斯鲁利单抗免疫治疗4周期，期间疗效评价PR。患者为求进一步治疗就诊我科，门诊拟", "第 1 页"]
2026-08-06 10:30:58,929 INFO     30 [qwen-vl-parser] page=2 text: 38 lines (bbox 3-40)
2026-08-06 10:30:58,930 INFO     30 [qwen-vl-parser] page=2 text: 38 sections
2026-08-06 10:30:59,317 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1111275, prompt_len=764
2026-08-06 10:31:00,659 INFO     30 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-06 10:31:00,660 INFO     30 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-06 10:31:00,716 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1111275, prompt_len=401
2026-08-06 10:31:01,815 INFO     30 [qwen-vl-parser] text API response (len=1056):
["/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView", "84-04-02", "最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>", "返回概览视图", "门诊时间: 2026-02-12 11:40:02 接诊科室: 呼吸危重三病区(门) 接诊医生: 孙帅森", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告", "请输入药品内容, 按回车键检索", "查询全部", "类型 组 药品名称[规格] 用法 频率 实际用量 总量 开立时间 开立医师", "药品 (大伊可新)维生素AD滴剂 口服 qd 2000u 3 2024-07-05 09:30:58 李婉莹", "药品 (普米克令舒)吸入用布地奈德混悬液 压缩雾化吸入 tid 2ml 20 2024-07-05 09:30:58 李婉莹", "药品 小儿豉翘清热颗粒 口服 tid 6g 3 2024-04-24 11:59:55 赵艳", "药品 (成人)双黄连口服液(基选) 口服 tid 20ml 3 2024-04-19 08:14:06 李婉莹", "药品 (强力)阿莫西林克拉维酸钾干混悬剂(选) 口服(继续用药) bid 0.457g 2 2024-04-19 08:14:06 李婉莹", "药品 (大伊可新)维生素AD滴剂 口服 qd 2000u 3 2024-04-19 08:14:06 李婉莹", "药品 (普米克令舒)吸入用布地奈德混悬液 压缩雾化吸入 tid 2ml 20 2024-04-19 08:14:06 李婉莹", "药品 替硝唑氯化钠注射液 静滴 qd 200ml 6 2024-01-05 10:37:47 程会芳", "药品 左氧氟沙星氯化钠注射液(选) 静滴 qd 0.5g 3 2024-01-05 10:37:47 程会芳", "药品 蒲地蓝消炎口服液 口服 tid 10ml 2 2023-08-14 15:30:23 谭真真", "药品 (盖克)小儿氨酚黄那敏颗粒 口服 tid 12g 2 2023-07-06 20:00:14 谭真真", "药品 蒲地蓝消炎口服液 口服 tid 10ml 2 2023-07-06 20:00:14 谭真真", "共70条 20条/页 < 1 2 3 4 > 前往 2 页", ""]
2026-08-06 10:31:01,817 INFO     30 [qwen-vl-parser] page=34 text: 22 lines (bbox 1933-1954)
2026-08-06 10:31:01,817 INFO     30 [qwen-vl-parser] page=34 text: 22 sections
2026-08-06 10:31:03,377 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3967233, prompt_len=764
2026-08-06 10:31:05,679 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:31:05,680 INFO     30 [qwen-vl-parser] page=35 classify=text report_date=None
2026-08-06 10:31:05,713 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3967233, prompt_len=401
2026-08-06 10:31:11,445 INFO     30 [qwen-vl-parser] text API response (len=1501):
["南京鼓楼医院", "南京大学医学院附属鼓楼医院", "出院记录", "科别（江北）综合肿瘤中心 病区（江北）B7病区床号 姓名 住院号", "“肺恶性肿瘤”收住入院。病程中，患者神志清，精神可，食纳睡眠可，二便如常，近期体重未见明显变", "化。", "诊疗经过：", "患者入院完善相关检查：", "【检验】", "2025.12.03 12:22 甲功三项：*促甲状腺激素 34.210 mIU/L↑，*游离三碘甲状腺原氨酸 2.60 pmol/L↓，", "*游离甲状腺素 9.58 pmol/L↓。", "2025.12.03 12:22 肺癌六项（江北）：*细胞角蛋白19片段 3.61 ng/mL↑，*神经元特异性烯醇化酶", "26.80 ng/mL↑，胃泌素释放肽前体 243.00 pg/mL↑。", "2025.12.03 13:33 生化全套，心肌酶：*碱性磷酸酶 46.8 U/L↓，*葡萄糖 6.66 mmol/L↑，*甘油三酯", "8.26 mmol/L↑，*总胆固醇 7.14 mmol/L↑，*H-脂蛋白胆固醇 0.90 mmol/L↓，*L-脂蛋白胆固醇 3.51", "mmol/L↑，*载脂蛋白AⅠ 0.79 g/L↓，*载脂蛋白B 1.87 g/L↑，*钠 136.1 mmol/L↓，*氯 97.8", "mmol/L↓，*α羟丁酸脱氢酶 158 U/L↑，eGFR(CKD-EPI) 77.2 ml/min/1.73m^2↓。", "2025.12.03 14:45 血常规：淋巴细胞百分数 19.7 %↓，淋巴细胞绝对值 0.8 ×10^9/L↓，*红细胞计数", "3.30 ×10^12/L↓，*血红蛋白量 108 g/L↓，*红细胞压积 31.8 %↓，红细胞体积分布宽度 15.4 %↑，*", "血小板计数 112 ×10^9/L↓。", "余未见明显异常。", "【检查】", "2025.12.04 15:19 心电图检查（江北）（检查）常规心电图 检查结论 窦性心律一度房室传导阻滞左前分支", "阻滞异常Q波(V1、V2)左心室高电压ST-T改变QTc间期延长", "2025.12.04 16:29（江北）PET/CT(检查) PET/CT全身显像 检查结论 1.“左肺癌化疗后复查”；①左下肺", "门稍大伴葡萄糖代谢增高灶，内部通行支气管狭窄，结合病史考虑符合小细胞癌表现；②左肺下叶两枚软", "组织结节，葡萄糖代谢异常增高；双肺门、纵隔、右侧腋窝多发肿大淋巴结，葡萄糖代谢显著增高；以上", "考虑同侧肺内转移、多发淋巴结转移；2.双肺多发小结节，部分为磨玻璃结节，葡萄糖代谢未见增高，建", "议胸部CT随诊；双肺散在条索及渗出；左肺下叶节段性肺不张；右肺局限性肺气肿；双侧胸膜增厚；3.左", "肾上腺稍低密度结节，葡萄糖代谢未见异常增高，左肾上腺稍增粗，葡萄糖代谢轻度增高，倾向增生伴腺", "瘤形成，请比对老片、密切随诊观察；4.腔隙性脑梗死可能；脑萎缩；副鼻窦炎症；甲状腺左右两叶密度", "欠均，葡萄糖代谢增高，考虑炎性摄取增高，必要时请结合甲功、颈部超声随诊；5.心影偏大，冠状动脉", "及胸部大血管管壁钙化；6.食管中下段管壁似稍增厚，葡萄糖代谢轻度增高，考虑炎性或生理性摄取可", "能，必要时内镜检查；十二指肠憩室可能；轻度脂肪肝；肝囊肿；胆囊饱满；7.慢性膀胱炎症可能；盆腔", "内钙化结节；8.颈椎生理性曲度变直，脊柱退变；右股骨下段低密度伴内部钙化，葡萄糖代谢不高，考虑", "第 2 页"]
2026-08-06 10:31:11,446 INFO     30 [qwen-vl-parser] page=3 text: 36 lines (bbox 41-76)
2026-08-06 10:31:11,447 INFO     30 [qwen-vl-parser] page=3 text: 36 sections
2026-08-06 10:31:11,836 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=885298, prompt_len=764
2026-08-06 10:31:13,442 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:31:13,444 INFO     30 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-06 10:31:13,486 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=885298, prompt_len=401
2026-08-06 10:31:14,383 INFO     30 [qwen-vl-parser] text API response (len=1155):
["50/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView", "984-04-02 首诊日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>", "返回概览视图", "门诊", "2026-02-12 11:40:02 接诊科室: 呼吸危重三病区(门) 接诊医生: 孙帅森", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告", "请输入药品内容,按回车键检索", "查询全部", "类型 组 药品名称[规格]", "药品 替硝唑氯化钠注射液", "药品 左氧氟沙星氯化钠注射液(选)", "药品 蒲地蓝消炎口服液", "药品 (盖克)小儿氨酚黄那敏颗粒", "药品 蒲地蓝消炎口服液", "药品 (小儿)双黄连口服液(选)", "药品 地塞米松磷酸钠注射液(选)", "药品 5ml灭菌注射用水", "药品 (扑尔敏针)马来酸氯苯那敏注射液", "药品 消旋山莨菪碱注射液", "药品 头孢克肟颗粒(选)", "药品 (天晴速畅)吸入用布地奈德混悬液(选)", "药品 (大伊可新)维生素AD滴剂", "用法 频率 实际用量 总量 开立时间 开立医师", "入", "静滴 qd 200ml 6 2024-01-05 10:37:47 程会芳", "静滴 qd 0.5g 3 2024-01-05 10:37:47 程会芳", "口服 tid 10ml 2 2023-08-14 15:30:23 谭真真", "口服 tid 12g 2 2023-07-06 20:00:14 谭真真", "口服 tid 10ml 2 2023-07-06 20:00:14 谭真真", "口服 tid 20ml 2 2023-07-06 20:00:14 谭真真", "外用 bid 10mg 2 2023-06-26 15:19:59 谭真真", "外用 bid 5ml 4 2023-06-26 15:19:59 谭真真", "外用 bid 20mg 2 2023-06-26 15:19:59 谭真真", "外用 bid 20mg 2 2023-06-26 15:19:59 谭真真", "口服 bid 100mg 30 2023-05-08 19:56:47 陈音", "压缩雾化吸入 bid 2ml 10 2023-05-08 19:52:42 段艳霞", "口服 qd 2000u 2 2023-05-08 19:52:42 段艳霞", "共70条 20条/页 < 1 2 3 4 > 前往: 2 页", ""]
2026-08-06 10:31:14,387 INFO     30 [qwen-vl-parser] page=35 text: 38 lines (bbox 1955-1992)
2026-08-06 10:31:14,387 INFO     30 [qwen-vl-parser] page=35 text: 38 sections
2026-08-06 10:31:14,849 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=900365, prompt_len=764
2026-08-06 10:31:16,406 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:31:16,407 INFO     30 [qwen-vl-parser] page=36 classify=text report_date=None
2026-08-06 10:31:16,432 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=900365, prompt_len=401
2026-08-06 10:31:19,841 INFO     30 [qwen-vl-parser] text API response (len=952):
["3/4", "南京鼓楼医院", "南京大学医学院附属鼓楼医院", "出院记录", "科别（江北）综合肿瘤中心 病区（江北）B7病区床号", "姓名 住院号", "良性灶如内生软骨瘤可能，随诊；右肩背部皮下稍低密度结节，葡萄糖代谢未见增高，考虑良性灶，随", "诊。", "【诊疗经过】", "患者入院后完善PET-CT复查，病情较前基本相仿，暂无根治性放疗指征。排除禁忌后，患者于2025-12-05", "行斯鲁利单抗免疫维持治疗1周期。现本周期静脉治疗已结束，现整体病情稳定，一般情况尚可，准予办理", "出院。", "出院情况： 好转", "伤口愈合：-", "ECOG 1分，NRS 0分，神志清，精神可，无贫血貌，全身皮肤巩膜无黄染。胸廓外形正常，无胸壁静脉曲", "张。双侧呼吸运动对称，肋间隙：正常，触觉语颤：对称，皮下捻发感：无，双肺叩诊清音，双肺呼吸音", "稍粗，两肺未闻及明显干湿啰音。心律齐，心脏各瓣膜区未闻及杂音。腹部平坦，腹部无压痛，无反跳", "痛。双下肢无明显水肿。", "出院医嘱：", "1、注意天气变化，注意休息、低脂饮食，避免受凉，避免手足接触冰冷物体，注意皮肤保暖。", "2、出院后继续用药", "左甲状腺素钠片（优甲乐）50微克/片 1片 口服 QD（7点）（每天早餐前半小时服用1片，补充甲状腺激", "素，内分泌科随诊调药）", "3、定期复查血常规（每周1-2次）及生化全套（每周1次），如WBC<3.0×10^9/L、PLT<60×10^9/L或生化", "全套指标异常，请及时当地医院就诊（如有急症或危急值报告，请及时就近正规医院急诊就诊），我科门", "诊随诊。", "4、下次治疗时间：3-4周左右，具体等电话通知。杨阳主任医师专家门诊时间：门诊时间：每周二、周五", "上午，（周二本部，周五江北），（江北肿瘤科医生办公室电话：025-83106666转220717）。如需肿瘤日", "间治疗，请提前一周至杨阳主任医师门诊预约。", "5、不适门诊随诊。", "不存在尚未回归的病理检查结果。", "X光片号：-", "CT号： P049684", "MRI号：-", "病理号：-", "上级医师：", "医师：", "第 3 页"]
2026-08-06 10:31:19,844 INFO     30 [qwen-vl-parser] page=4 text: 38 lines (bbox 77-114)
2026-08-06 10:31:19,844 INFO     30 [qwen-vl-parser] page=4 text: 38 sections
2026-08-06 10:31:20,330 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1051018, prompt_len=764
2026-08-06 10:31:20,919 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:31:20.915+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 8, "lag": 0, "done": 1, "failed": 0, "current": {"00b9d592918111f18dbe1f8f96f1c395": {"id": "00b9d592918111f18dbe1f8f96f1c395", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011867426, "task_type": "dataflow", "root_trace_id": "1ab3198c92574fb4b2701d0f5db7322f", "root_traceparent": "00-1ab3198c92574fb4b2701d0f5db7322f-bdaff6f64a5f4a64-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "dfc102e2918111f18dbe1f8f96f1c395": {"id": "dfc102e2918111f18dbe1f8f96f1c395", "doc_id": "de8a02fc918111f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786012241604, "task_type": "dataflow", "root_trace_id": "90f550f6b00248c3845d57a8e0bcf6fb", "root_traceparent": "00-90f550f6b00248c3845d57a8e0bcf6fb-5db7fb7d470dfe0d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:31:21,950 INFO     30 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-05-23"}
```
2026-08-06 10:31:21,951 INFO     30 [qwen-vl-parser] page=5 classify=text report_date=2025-05-23
2026-08-06 10:31:21,972 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1051018, prompt_len=401
2026-08-06 10:31:24,602 INFO     30 [qwen-vl-parser] text API response (len=1045):
["返回概览视图", "11.40.02 接诊科室: 呼吸危重三病区(门) 接诊医生: 孙帅森", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告", "请输入药品内容,按回车键检索", "查询全部", "类型 组 药品名称|规格 用法 频率 实际用量 总量 开立时间 开立医师", "药品 *乙2)(大伊可新)维生素AD滴剂 口服 qd 2000u 2 2023-04-07 16:29.03 陈音", "药品 乙1)头孢克肟颗粒(选) 口服 bid 100mg 30 2023-04-07 16:28.02 陈音", "药品 乙0)阿奇霉素干混悬剂 口服 qd 0.25g 1 2023-04-07 16:27:17 陈音", "药品 乙2)三拗片 口服 tid 2片 1 2023-04-07 16:27:17 陈音", "药品 乙0)富马酸酮替芬片 口服 bid 1mg 6 2023-04-07 16:27:17 陈音", "药品 蒲地蓝消炎口服液 口服 tid 10ml 2 2022-08-08 15:40.53 王晶", "药品 乙1)盐酸氨溴索口服溶液(基) 口服 bid 5ml 1 2022-05-09 19:49:32 赵海国", "药品 赖氨肌醇维B12口服溶液 口服 bid 10ml 3 2022-05-09 19:49:32 赵海国", "药品 乙0)5ml灭菌注射用水 外用 bid 20ml 4 2022-05-05 09:58:24 李凌蔚", "药品 乙1)(扑尔敏针)马来酸氯苯那敏注射液 外用 bid 20mg 2 2022-05-05 09:58:24 李凌蔚", "药品 甲)地塞米松磷酸钠注射液(基) 外用 bid 10mg 2 2022-05-05 09:58:24 李凌蔚", "药品 乙1)消旋山莨菪碱注射液(基) 外用 bid 20mg 2 2022-05-05 09:58:24 李凌蔚", "药品 赖氨肌醇维B12口服溶液 口服 bid 10ml 1 2022-05-05 09:57:04 李凌蔚", "药品 乙1)复合维生素B片 口服 tid 1片 100 2022-05-05 09:56:29 李凌蔚", "药品 用维生素004/基 口服 4 100 2022-05-05 09:56:29 李凌蔚", "共70条 20条/页 < 1 2 3 4 > 前往 3 页"]
2026-08-06 10:31:24,603 INFO     30 [qwen-vl-parser] page=36 text: 22 lines (bbox 1993-2014)
2026-08-06 10:31:24,604 INFO     30 [qwen-vl-parser] page=36 text: 22 sections
2026-08-06 10:31:24,727 INFO     30 [qwen-vl-parser] text API response (len=410):
["河北省人民医院", "病理检查报告单", "病理号", "姓名:", "性别: 女", "年龄: 74岁", "送检单位: 本院", "科别: 胸外二科病区", "住院号", "床号:", "送检日期: 2025-05-23 16:44", "送检材料: 左肺穿刺数条:", "临床诊断: 左肺占位", "图像:", "大体检查:", "(左肺穿刺数条:)穿刺组织3条, 长共3cm, 直径0.1cm。", "病理诊断:", "(左肺)穿刺组织: 浸润性癌, 类型待免疫组化助诊。", "诊断医师:", "郑国卿 王彤彤", "日期: 2025-05-26 14:23", "注:1.此报告仅供临床医师参考, 如有异议请在两日内与诊断医师联系。 电话: (0311)85988183", "2.国家规定小标本(咬检及穿刺组织)3个工作日内出报告; 其余标本5个工作日内出报告(特殊处理标本除外)。", "住院病历"]
2026-08-06 10:31:24,728 INFO     30 [qwen-vl-parser] page=5 text: 24 lines (bbox 115-138)
2026-08-06 10:31:24,728 INFO     30 [qwen-vl-parser] page=5 text: 24 sections
2026-08-06 10:31:25,026 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1008988, prompt_len=764
2026-08-06 10:31:25,237 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1166882, prompt_len=764
2026-08-06 10:31:27,120 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:31:27,121 INFO     30 [qwen-vl-parser] page=37 classify=text report_date=None
2026-08-06 10:31:27,123 INFO     30 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-05-27"}
```
2026-08-06 10:31:27,124 INFO     30 [qwen-vl-parser] page=6 classify=text report_date=2025-05-27
2026-08-06 10:31:27,154 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1008988, prompt_len=401
2026-08-06 10:31:27,189 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1166882, prompt_len=401
2026-08-06 10:31:30,119 INFO     30 [qwen-vl-parser] text API response (len=457):
["河北省人民医院", "病理检查补充报告单", "病理号:", "姓名:", "性别: 女", "年龄: 74岁", "送检单位: 本院", "科别: 胸外二科病区", "住院号:", "床号:", "送检日期: 2025-05-23 16:44", "送检材料: 左肺穿刺数条:", "临床诊断: 左肺占位", "补充病理诊断:", "(左肺)穿刺组织: 结合免疫组化染色支持小细胞癌。", "免疫组化染色: CKpan (+), Vimentin (-), CK7 (+), TTF-1 (+), NapsinA (-), CK5/6", "(-), P40 (-), P63 (-), CgA (+), Syn (+), CD56 (+), Ki-67 (90%+)。", "诊断医师: 康林 郑国娜", "报告日期: 2025-05-27 16:", "注: 此报告仅供临床医师参考, 如有异议或病情有新变化务请及时与病理诊断医师联系(电话: 85988409)", "河北省人民医院", "住院病历"]
2026-08-06 10:31:30,120 INFO     30 [qwen-vl-parser] page=6 text: 22 lines (bbox 139-160)
2026-08-06 10:31:30,121 INFO     30 [qwen-vl-parser] page=6 text: 22 sections
2026-08-06 10:31:30,382 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=906121, prompt_len=764
2026-08-06 10:31:31,873 INFO     30 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-03-11"}
```
2026-08-06 10:31:31,874 INFO     30 [qwen-vl-parser] page=7 classify=text report_date=2026-03-11
2026-08-06 10:31:31,898 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=906121, prompt_len=401
2026-08-06 10:31:36,239 INFO     30 [qwen-vl-parser] text API response (len=1142):
["50/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView", "984-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>", "返回概览视图", "门.", "J26-02-12 11.40.02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告", "请输入药品内容，按回车键检索", "查询全部", "类型 组 药品名称/规格 用法 频率 实际用量 总量 开立时间 开立医师", "药品 口服 bid 5ml 1 2022-05-09 19.49.32 赵海国", "药品 乙1)盐酸氨溴索口服溶液(基) 口服 bid 10ml 3 2022-05-09 19.49.32 赵海国", "药品 赖氨肌醇维B12口服溶液 口服 bid 20ml 4 2022-05-05 09.58.24 李凌蔚", "药品 乙0)5ml灭菌注射用水 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚", "药品 乙1)(扑尔敏针)马来酸氯苯那敏注射液 外用 bid 10mg 2 2022-05-05 09.58.24 李凌蔚", "药品 甲)地塞米松磷酸钠注射液(基) 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚", "药品 乙1)消旋山莨菪碱注射液(基) 外用 bid 10ml 1 2022-05-05 09.57.04 李凌蔚", "药品 赖氨肌醇维B12口服溶液 口服 bid 1片 100 2022-05-05 09.56.29 李凌蔚", "药品 乙1)复合维生素B片 口服 tid 5mg 100 2022-05-05 09.56.29 李凌蔚", "药品 甲)维生素B2片(基) 口服 tid 50mg 2 2022-05-05 09.54.38 李凌蔚", "药品 乙1)头孢克肟颗粒 口服 bid 10ml 1 2022-05-05 09.54.38 李凌蔚", "药品 乙1)金振口服液(基) 口服 bid 3g 2 2022-04-19 16.05.18 陈媛", "药品 (盖克)小儿氨酚黄那敏颗粒 口服 tid 4ml 1 2022-04-19 16.05.18 陈媛", "药品 乙1)美敏伪麻口服溶液 口服 qid 5ml 1 2022-04-19 16.05.18 陈媛", "共70条 20条/页 < 1 2 3 4 > 前往 3 页"]
2026-08-06 10:31:36,241 INFO     30 [qwen-vl-parser] page=37 text: 24 lines (bbox 2015-2038)
2026-08-06 10:31:36,241 INFO     30 [qwen-vl-parser] page=37 text: 24 sections
2026-08-06 10:31:36,703 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=767247, prompt_len=764
2026-08-06 10:31:38,301 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:31:38,302 INFO     30 [qwen-vl-parser] page=38 classify=text report_date=None
2026-08-06 10:31:38,322 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=767247, prompt_len=401
2026-08-06 10:31:40,132 INFO     30 [qwen-vl-parser] text API response (len=1114):
["<", "南京鼓楼医院云胶片", "南京鼓楼医院", "南京大学医学院附属鼓楼医院", "影像检查诊断报告", "互联网医院", "电子影像", "检查号:", "患者类型: 住院", "患者编号:", "姓名:", "性别: 女", "年龄: 75岁", "科别: (江北)综合肿瘤中心 病区: (江北)B7病区", "病床:", "检查日期: 2026-03-11 13:39:06", "设备类型: CT", "技师: 王雨晓", "检查项目: [CT平扫+增强(颈部、胸部、上腹部、下腹部、盆腔)]", "检查所见:", "颈部软组织CT平扫+增强:", "【所见咽部】所见咽腔结构对称,未见明显异常密度影。增强后未见明显异常强化。", "【喉部及下咽部】喉腔结构对称,会厌、声带、梨状窝形态及密度未见明显异常。增强后未见", "明显异常强化。", "【甲状腺及甲状旁腺区】甲状腺左右叶大小、形态正常,甲状腺双叶低密度结节;甲状旁腺区", "未见明显占位性病变。", "【唾液腺】双侧腮腺、颌下腺形态密度未见明显异常。增强后未见明显异常强化。", "【气管及食管】气管居中,管腔通畅;食管颈段管壁未见明显增厚。", "【颈部间隙】脂肪间隙清晰,未见明显异常密度影。增强后未见明显异常强化。", "【淋巴结】两侧锁骨上窝多发肿大淋巴结。", "【其他】副鼻窦内低密度影。", "胸部CT平扫+增强:", "【肺野】两肺野纹理清晰,左肺下叶见斑片状高密度影。右肺上叶舌段小片状高密度影。两肺", "多发结节,较大者:右肺上叶(Img79)见一实性结节影,大小约5mm×3mm。两肺索条及片絮影;右", "肺上叶局部透亮区。", "【肺门】双肺门多发肿大淋巴结,大者位于左侧,短径约20mm,增强后强化不均。", "【气管及支气管】左下肺支气管闭塞伴阻塞性炎症,病灶周围结节影。", "【纵隔】纵隔居中,纵隔内多发肿大淋巴结,较大者短径约20mm。", "【心脏及大血管】心影增大;主动脉及冠状动脉壁见致密影。", "【胸膜及胸腔】胸膜:两侧胸膜可见增厚;胸腔积液:否。增强后未见明显异常强化。", "【膈肌】光整,未见明显异常抬高。增强后未见明显异常强化。", "【胸壁】胸廓对称,骨质未见明显异常。增强后未见明显异常强化。", "上腹部、下腹部、盆腔CT平扫+增强:", "报告日期: 2026-03-11 15:35:37", "诊断医师: 申欣怡", " / 申欣怡", "审核日期: 2026-03-12 13:17:06", "审核医师: 王国", "（本报告仅供临床医生参考）", "南京市中山路321号"]
2026-08-06 10:31:40,133 INFO     30 [qwen-vl-parser] page=7 text: 50 lines (bbox 161-210)
2026-08-06 10:31:40,133 INFO     30 [qwen-vl-parser] page=7 text: 50 sections
2026-08-06 10:31:40,330 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=533615, prompt_len=764
2026-08-06 10:31:41,874 INFO     30 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-10-08"}
```
2026-08-06 10:31:41,875 INFO     30 [qwen-vl-parser] page=8 classify=text report_date=2025-10-08
2026-08-06 10:31:41,922 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=533615, prompt_len=401
2026-08-06 10:31:45,750 INFO     30 [qwen-vl-parser] text API response (len=542):
["南京鼓楼医院云胶片", "女/75岁", "设备类型 CT 患者类型 无", "检查项目 [CT平扫+增强（颈部、胸部、上腹部、下", "腹部、盆腔）]", "PDF报告 图像 分享", "报告 2025-10-08", "影像描述", "颈部软组织CT平扫+增强：", "【所见咽部】所见咽腔结构对称，未见明显异常", "密度影。增强后未见明显异常强化。", "【喉部及下咽部】喉腔结构对称，会厌、声带、", "梨状窝形态及密度未见明显异常。增强后未见明显", "异常强化。", "【甲状腺及甲状旁腺区】甲状腺左右叶大小、形", "态正常，甲状腺双叶低密度结节；甲状旁腺区未见", "明显占位性病变。", "【唾液腺】双侧腮腺、颌下腺形态密度未见明显", "异常。增强后未见明显异常强化。", "【气管及食管】气管居中，管腔通畅；食管颈段", "管壁未见明显增厚。", "【颈部间隙】脂肪间隙清晰，未见明显异常密度", "影。增强后未见明显异常强化。", "【淋巴结】未见明显肿大淋巴结。", "【其他】副鼻窦内低密度影。", "胸部CT平扫+增强：", "【肺野】两肺野纹理清晰，左肺下叶见斑片状高", "移动影像浏览", "© 2022 南京鼓楼医院影像云平台 V1.0"]
2026-08-06 10:31:45,750 INFO     30 [qwen-vl-parser] page=8 text: 29 lines (bbox 211-239)
2026-08-06 10:31:45,751 INFO     30 [qwen-vl-parser] page=8 text: 29 sections
2026-08-06 10:31:45,885 INFO     30 [qwen-vl-parser] text API response (len=948):
["184-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>", "返回概览视图", "2026-02-12 11:40:02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告", "请输入药品内容,按回车键检索", "查询全部", "类型 组 药品名称(规格)", "药品 甲)(小儿)双黄连口服液(基)", "药品 (盖克)小儿氨酚黄那敏颗粒", "药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(基)", "药品 蒲地蓝消炎口服液", "药品 复方氨酚甲麻口服液", "药品 (盖克)小儿氨酚黄那敏颗粒", "药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(国基)", "药品 乙0)(普米克令舒)吸入用布地奈德混悬液(国基)", "药品 右旋糖酐铁颗粒", "药品 盐酸氨卓斯丁滴眼液", "用法 频率 实际用量 总量 开立时间 开立医师", "口服 tid 10ml 1 2022-03-26 19:51:46 谭真真", "口服 tid 6g 2 2022-03-26 19:51:18 谭真真", "口服(继续用药) bid 0.228g 2 2022-03-26 19:51:18 谭真真", "口服 bid 10ml 1 2022-03-26 19:51:18 谭真真", "口服 q6h 10ml 2 2021-11-04 17:18:07 宁秀琴", "口服 tid 12g 2 2021-11-04 17:18:07 宁秀琴", "口服(继续用药) q12h 0.45g 2 2021-11-04 17:18:07 宁秀琴", "压缩雾化 bid 2ml 5 2021-10-11 10:07:54 张冬梅", "口服 tid 1袋 80 2021-09-28 15:12:34 党建华", "滴双眼 bid 0.1ml 1 2021-09-09 15:18:56 史艳艳", "共70条 20条/页 < 1 2 3 4 > 前往 4 页", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-06 10:31:45,886 INFO     30 [qwen-vl-parser] page=38 text: 31 lines (bbox 2039-2069)
2026-08-06 10:31:45,886 INFO     30 [qwen-vl-parser] page=38 text: 31 sections
2026-08-06 10:31:45,936 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=578473, prompt_len=764
2026-08-06 10:31:46,218 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1417972, prompt_len=764
2026-08-06 10:31:47,925 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:31:47,925 INFO     30 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-06 10:31:47,929 INFO     30 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-06"
}
```
2026-08-06 10:31:47,931 INFO     30 [qwen-vl-parser] page=39 classify=table report_date=2026-01-06
2026-08-06 10:31:47,946 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=578473, prompt_len=401
2026-08-06 10:31:47,970 INFO     30 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1417972, prompt_len=756
2026-08-06 10:31:51,522 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:31:51.519+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 8, "lag": 0, "done": 1, "failed": 0, "current": {"00b9d592918111f18dbe1f8f96f1c395": {"id": "00b9d592918111f18dbe1f8f96f1c395", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011867426, "task_type": "dataflow", "root_trace_id": "1ab3198c92574fb4b2701d0f5db7322f", "root_traceparent": "00-1ab3198c92574fb4b2701d0f5db7322f-bdaff6f64a5f4a64-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "dfc102e2918111f18dbe1f8f96f1c395": {"id": "dfc102e2918111f18dbe1f8f96f1c395", "doc_id": "de8a02fc918111f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786012241604, "task_type": "dataflow", "root_trace_id": "90f550f6b00248c3845d57a8e0bcf6fb", "root_traceparent": "00-90f550f6b00248c3845d57a8e0bcf6fb-5db7fb7d470dfe0d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:31:52,201 INFO     30 [qwen-vl-parser] text API response (len=618):
["南京鼓楼医院云胶片", "女/75岁", "设备类型 CT 患者类型 无", "检查项目 [CT平扫+增强（颈部、胸部、上腹部、下", "腹部、盆腔）]", "PDF报告 图像 分享", "【肺野】两肺野纹理清晰，左肺下叶见斑片状高", "密度影。两肺多发结节，较大者：右肺上叶（Img7", "9）见一实性结节影，大小约5mm×3mm。两肺索", "条及片絮影；右肺上叶局部透亮区。", "【肺门】双肺门多发小淋巴结，部分稍大。", "【气管及支气管】左下肺支气管闭塞伴阻塞性炎", "症，病灶周围结节影。", "【纵隔】纵隔居中，纵隔内多发小淋巴结，部分", "稍大，较大者短径约10mm。", "【心脏及大血管】心影增大；主动脉及冠状动", "脉壁见致密影。", "【胸膜及胸腔】胸膜：两侧胸膜可见增厚；胸腔", "积液：否。增强后未见明显异常强化。", "【膈肌】光整，未见明显异常抬高。增强后未见", "明显异常强化。", "【胸壁】胸廓对称，骨质未见明显异常。增强后", "未见明显异常强化。", "上腹部CT平扫+增强：", "【肝脏】各叶比例在正常范围内，外形轮廓规", "则，肝内小圆形无强化低密度影，较大者长径约6", "mm。静脉期肝左叶小片状稍低密度影（薄层im29", "0）。", "【胆囊及胆管】胆囊形态、大小正常，囊壁未见", "移动影像浏览", "© 2022 南京鼓楼医院影像云平台 V1.0"]
2026-08-06 10:31:52,202 INFO     30 [qwen-vl-parser] page=9 text: 31 lines (bbox 240-270)
2026-08-06 10:31:52,202 INFO     30 [qwen-vl-parser] page=9 text: 31 sections
2026-08-06 10:31:52,392 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=580959, prompt_len=764
2026-08-06 10:31:54,500 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:31:54,501 INFO     30 [qwen-vl-parser] page=10 classify=text report_date=None
2026-08-06 10:31:54,535 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=580959, prompt_len=401
2026-08-06 10:31:57,163 INFO     30 [qwen-vl-parser] table API response (len=1393):
\begin{tabular}{ccccccccc}
\hline
英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\
\hline
{[}WBC{]}白细胞数目 & 4.28 & & & 3.5~9.5 & 10^9/L & {[}HCT{]}红细胞压积 & 37.8 & & & 35~45 & \% \\
{[}Lym\%{]}淋巴细胞百分比 & 28.4 & & & 20~50 & \% & {[}MCV{]}平均红细胞体积 & 80.4 & $\downarrow$ & & 82~100 & fL \\
{[}Mon\%{]}单核细胞百分比 & 4.7 & & & 3~10 & \% & {[}MCH{]}平均红细胞血红蛋白含量 & 26.0 & $\downarrow$ & & 27~34 & pg \\
{[}Neu\%{]}中性粒细胞百分比 & 64.4 & & & 40~75 & \% & {[}MCHC{]}平均红细胞血红蛋白浓度 & 323 & & & 316~354 & g/L \\
{[}Eos\%{]}嗜酸性细胞百分比 & 2.4 & & & 0.4~8 & \% & {[}RDW-CV{]}红细胞分布宽度变异系数 & 15.2 & & & 11~16 & \% \\
{[}Bas\%{]}嗜碱性细胞百分比 & 0.1 & & & 0.0~1.0 & \% & {[}RDW-SD{]}红细胞分布宽度标准差 & 43.0 & & & 35.0~56.0 & fL \\
{[}Lym\#{]}淋巴细胞数目 & 1.22 & & & 1.1~3.2 & 10^9/L & {[}PLT{]}血小板数目 & 224 & & & 125~350 & 10^9/L \\
{[}Mon\#{]}单核细胞数目 & 0.20 & & & 0.1~0.6 & 10^9/L & {[}MPV{]}平均血小板体积 & 8.0 & & & 6.5~12 & fL \\
{[}Neu\#{]}中性粒细胞数目 & 2.76 & & & 1.8~6.3 & 10^9/L & {[}PDW{]}血小板分布宽度 & 16.0 & & & 9~17 & fL \\
{[}Eos\#{]}嗜酸性细胞数目 & 0.10 & & & 0.02~0.52 & 10^9/L & {[}PCT{]}血小板压积 & 0.180 & & & 0.108~ & \% \\
{[}Bas\#{]}嗜碱性细胞数目 & 0.00 & & & 0.00~0.06 & 10^9/L & {[}P-LCR{]}大型血小板比率 & 15.8 & & & 11~45 & \% \\
{[}RBC{]}红细胞数目 & 4.70 & & & 3.8~5.1 & 10^12/L & {[}IG\%{]}未成熟粒细胞百分比 & 0.4 & & & 0.0~0.6 & \% \\
{[}HGB{]}血红蛋白 & 122 & & & 115~150 & g/L & {[}IG\#{]}未成熟粒细胞计数 & 0.02 & & & 0.00~0.06 & 10^9/L \\
\hline
\end{tabular}
2026-08-06 10:31:57,168 INFO     30 [qwen-vl-parser] page=39 table: 20 LaTeX lines (bbox 2070-2089)
2026-08-06 10:31:57,168 INFO     30 [qwen-vl-parser] page=39 table: 20 sections
2026-08-06 10:31:57,399 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=700044, prompt_len=764
2026-08-06 10:31:58,967 INFO     30 [qwen-vl-parser] text API response (len=633):
["南京鼓楼医院云胶片", "女/75岁", "设备类型 CT 患者类型 无", "检查项目 [CT平扫+增强（颈部、胸部、上腹部、下", "腹部、盆腔）]", "PDF报告 图像 分享", "【胆囊及胆管】胆囊形态、大小正常，囊壁未见", "增厚，囊内未见明显异常密度影；肝内外胆管轻度", "扩张。", "【胰腺】形态、大小正常，实质内未见明显异常", "密度影；胰管未见明显扩张。增强后未见明显异常", "强化。", "【脾脏】形态、大小正常，实质内未见明显异常", "密度影。增强后未见明显异常强化。", "【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均", "匀，未见明显肿大淋巴结，未见明显渗出及积液。", "增强后未见明显异常强化。", "下腹部CT平扫+增强：", "【肾脏】两侧肾脏大小、形态、位置正常，右肾", "窦点状致密影；肾盂肾盏未见明显扩张。增强后未", "见明显异常强化。", "【肾上腺】双肾上腺增粗，左肾上腺低密度结", "节，长径约12mm,可见强化。", "【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均", "匀，未见明显肿大淋巴结，未见明显渗出及积液。", "增强后未见明显异常强化。", "盆腔CT平扫+增强：", "【膀胱】充盈欠佳，壁未见明显增厚，其内未见", "明显异常密度影。增强后未见明显异常强化。", "【子宫及附件】子宫呈肌组织结构性空扫", "移动影像浏览", "© 2022 南京鼓楼医院影像云平台 V1.0"]
2026-08-06 10:31:58,968 INFO     30 [qwen-vl-parser] page=10 text: 32 lines (bbox 271-302)
2026-08-06 10:31:58,968 INFO     30 [qwen-vl-parser] page=10 text: 32 sections
2026-08-06 10:31:58,971 INFO     30 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-06"
}
```
2026-08-06 10:31:58,971 INFO     30 [qwen-vl-parser] page=40 classify=table report_date=2026-01-06
2026-08-06 10:31:58,994 INFO     30 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=700044, prompt_len=756
2026-08-06 10:31:59,266 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=555271, prompt_len=764
2026-08-06 10:31:59,985 INFO     30 [qwen-vl-parser] table API response (len=131):
\begin{tabular}{ccccccc}
\hline
英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\
\hline
{[}ESR{]}血沉 & & 7 & & 0~20 & mm/h \\
\hline
\end{tabular}
2026-08-06 10:31:59,986 INFO     30 [qwen-vl-parser] page=40 table: 8 LaTeX lines (bbox 2090-2097)
2026-08-06 10:31:59,986 INFO     30 [qwen-vl-parser] page=40 table: 8 sections
2026-08-06 10:32:00,285 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1083410, prompt_len=764
2026-08-06 10:32:00,741 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:32:00,742 INFO     30 [qwen-vl-parser] page=11 classify=text report_date=None
2026-08-06 10:32:00,781 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=555271, prompt_len=401
2026-08-06 10:32:02,075 INFO     30 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-06"
}
```
2026-08-06 10:32:02,077 INFO     30 [qwen-vl-parser] page=41 classify=table report_date=2026-01-06
2026-08-06 10:32:02,109 INFO     30 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1083410, prompt_len=756
2026-08-06 10:32:06,079 INFO     30 [qwen-vl-parser] text API response (len=589):
["南京鼓楼医院云胶片", "女/75岁", "设备类型 CT 患者类型 无", "检查项目 [CT平扫+增强（颈部、胸部、上腹部、下", "腹部、盆腔）]", "PDF报告 图像 分享", "诊断意见", "1.肺癌复查：左肺下叶斑片影较前（2025-07-15）", "明显缩小，左下肺支气管闭塞伴阻塞性炎症，较前", "缓解，密切随诊；双侧纵隔内及双肺门多发稍大淋", "巴结，部分较前稍缩小。", "2.两肺多发结节，较前变化不大，密切随诊。", "3.两侧胸膜增厚；两肺索条及炎性渗出，较前缓", "解；右肺上叶局限性肺气肿。", "4.心影增大；主动脉及冠状动脉壁钙化。", "5.肝脏小囊肿；静脉期肝左叶小片状稍低密度影", "（薄层im290），较前相仿，随诊。", "6.肝内外胆管轻度扩张。", "7.双肾上腺增粗，左肾上腺腺瘤可能，结合专科检", "查；右肾小结石。", "8.子宫肌瘤可能，结合妇科超声；盆腔内钙化结", "节。", "9.下腹腔内肠系膜间隙多发稍大淋巴结。", "10.食管下段壁轻度增厚；乙状结肠迂曲冗长；结肠", "内容物多；十二指肠降部憩室；结合临床体征随", "诊。", "11.右肩部皮下低密度结节，较前相仿，随诊；L4及", "以上椎体I°滑脱。", "移动影像浏览", "© 2022 南京鼓楼医院影像云平台 V1.0"]
2026-08-06 10:32:06,080 INFO     30 [qwen-vl-parser] page=11 text: 30 lines (bbox 303-332)
2026-08-06 10:32:06,081 INFO     30 [qwen-vl-parser] page=11 text: 30 sections
2026-08-06 10:32:06,357 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=645107, prompt_len=764
2026-08-06 10:32:06,659 INFO     30 [qwen-vl-parser] table API response (len=679):
\begin{tabular}{l l c c c c}
\hline
英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\
\hline
[TBIL]总胆红素 & & 8.5 & & 0.0~21.0 & $\mu$mol/L \\
[DBIL]直接胆红素 & & 2.3 & & 0.0~8.0 & $\mu$mol/L \\
[IBIL]间接胆红素 & & 6.2 & & 0.0~13.0 & $\mu$mol/L \\
[ALT]谷丙转氨酶 & & 12.2 & & 7~40 & U/L \\
[AST]谷草转氨酶 & & 18 & & 13~35 & U/L \\
[AST/ALT]谷草/谷丙 & & 1.48 & & 0.8~1.5 & \\
[TP]总蛋白 & & 73.6 & & 65.0~85.0 & g/L \\
[ALB]白蛋白 & & 46.0 & & 40.0~55.0 & g/L \\
[GLB]球蛋白 & & 27.6 & & 20.0~40.0 & g/L \\
[A/G]白球比值 & & 1.67 & & 1.20~2.4 & \\
[GGT]谷氨酰转肽酶 & & 9.0 & & 7~45 & U/L \\
[ALP]碱性磷酸酶 & & 66 & & 40~150 & U/L \\
[Urea]尿素 & & 4.27 & & 2.6~7.5 & mmol/L \\
[CRE]肌酐 & & 49.9 & & 41~73 & $\mu$mol/L \\
\hline
\end{tabular}
2026-08-06 10:32:06,663 INFO     30 [qwen-vl-parser] page=41 table: 21 LaTeX lines (bbox 2098-2118)
2026-08-06 10:32:06,663 INFO     30 [qwen-vl-parser] page=41 table: 21 sections
2026-08-06 10:32:07,032 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1288667, prompt_len=764
2026-08-06 10:32:07,969 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:32:07,970 INFO     30 [qwen-vl-parser] page=12 classify=text report_date=None
2026-08-06 10:32:07,995 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=645107, prompt_len=401
2026-08-06 10:32:08,910 INFO     30 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-06"
}
```
2026-08-06 10:32:08,911 INFO     30 [qwen-vl-parser] page=42 classify=table report_date=2026-01-06
2026-08-06 10:32:08,933 INFO     30 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1288667, prompt_len=756
2026-08-06 10:32:10,278 INFO     30 [qwen-vl-parser] text API response (len=309):
["南京鼓楼医院", "南京大学医学院附属鼓楼医院", "互联网医院", "门诊病历", "姓名:", "性别:女", "年龄:75岁", "ID:", "2026年03月16日15时20分 (江北)心血管内科门诊", "主诉:要求进行心功能分级", "病史:患者平时正常活动不受限。", "过敏史:无吸烟史", "药物过敏史。无流行病学史", "体查:", "级)", "诊断:", "1.心功能I级(NYHA分", "2.高脂血症", "处理:随诊", "1.非诺贝特胶囊(力平之)", "200mg/粒", "用法:1粒", "口服", "一次/日", "x3盒 28天", "医师:", "齐", "第1页"]
2026-08-06 10:32:10,279 INFO     30 [qwen-vl-parser] page=12 text: 28 lines (bbox 333-360)
2026-08-06 10:32:10,279 INFO     30 [qwen-vl-parser] page=12 text: 28 sections
2026-08-06 10:32:10,613 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1057984, prompt_len=764
2026-08-06 10:32:12,207 INFO     30 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-10"
}
```
2026-08-06 10:32:12,208 INFO     30 [qwen-vl-parser] page=13 classify=table report_date=2026-03-10
2026-08-06 10:32:12,231 INFO     30 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1057984, prompt_len=756
2026-08-06 10:32:17,868 INFO     30 [qwen-vl-parser] table API response (len=947):
\begin{tabular}{cccccc}
\hline
\multicolumn{2}{c}{\textbf{检验项目}} & \textbf{结果} & \textbf{参考区间-单位} & \multicolumn{2}{c}{\textbf{检验项目}} & \textbf{结果} & \textbf{参考区间-单位} \\
\hline
*白细胞计数 & & 4.2 & 3.5--9.5 10^9/L & *平均红细胞血红蛋白含量 & & 31.4 & 27--34 pg \\
中性粒细胞百分数 & & 74.5 & 40--75 \% & *平均红细胞血红蛋白浓度 & & 332 & 316--354 g/L \\
淋巴细胞百分数 & & 16.1 & 20--50 \% & 红细胞体积分布宽度 & & 13.6 & 0-14 \% \\
单核细胞百分数 & & 6.9 & 3--10 \% & *血小板计数 & & 179 & 125--350 10^9/L \\
嗜酸性粒细胞百分数 & & 1.7 & 0.4--8 \% & & & & \\
嗜碱性粒细胞百分数 & & 0.8 & 0-1 \% & & & & \\
中性粒细胞绝对值 & & 3.1 & 1.8--6.3 10^9/L & & & & \\
淋巴细胞绝对值 & & 0.7 & 1.1--3.2 10^9/L & & & & \\
单核细胞绝对值 & & 0.3 & 0.1--0.6 10^9/L & & & & \\
嗜酸性粒细胞绝对值 & & 0.07 & 0.02--0.52 10^9/L & & & & \\
嗜碱性粒细胞绝对值 & & 0.03 & 0--0.06 10^9/L & & & & \\
*红细胞计数 & & 4.01 & 3.8-5.1 10^12/L & & & & \\
*血红蛋白量 & & 126 & 115--150 g/L & & & & \\
*红细胞压积 & & 38.0 & 35--45 \% & & & & \\
*平均红细胞体积 & & 94.7 & 82--100 fl & & & & \\
\hline
\end{tabular}
2026-08-06 10:32:17,872 INFO     30 [qwen-vl-parser] page=13 table: 22 LaTeX lines (bbox 361-382)
2026-08-06 10:32:17,872 INFO     30 [qwen-vl-parser] page=13 table: 22 sections
2026-08-06 10:32:18,102 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=892009, prompt_len=764
2026-08-06 10:32:19,647 INFO     30 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-10"
}
```
2026-08-06 10:32:19,647 INFO     30 [qwen-vl-parser] page=14 classify=table report_date=2026-03-10
2026-08-06 10:32:19,684 INFO     30 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=892009, prompt_len=756
2026-08-06 10:32:19,837 INFO     30 [qwen-vl-parser] table API response (len=2079):
\begin{tabular}{lllll}
\hline
\multicolumn{2}{l}{瑞图RT-F600} & \multicolumn{3}{c}{\textbf{医学检验科检验报告单}} \\
\multicolumn{2}{l}{\textbf{白带分析仪}} & & & \\
\hline
\multicolumn{2}{l}{姓 \quad 名:} & 送检科室: \quad 妇科一病区(门) & 床 \quad 号: & 样本类型: 阴道分泌物 \\
\multicolumn{2}{l}{住院(门诊)号:} & 性 \quad 别: \quad 女 & 年 \quad 龄: 41岁 & 样本状态: 正常 \\
\multicolumn{2}{l}{检验项目: \quad 妇科微生态} & & & \\
\multicolumn{2}{l}{疾病诊断: \quad 慢性盆腔痛} & & & \\
\hline
\multicolumn{5}{l}{形态学检测项目:} \\
\multicolumn{2}{l}{细胞情况} & 结果 & 正常值范围 & 镜下所见: \\
\multicolumn{2}{l}{清洁度} & Ⅱ & ~ ≤Ⅱ & \\
\multicolumn{2}{l}{白细胞} & 5-15 & ≤15/HP & \\
\multicolumn{2}{l}{红细胞} & 未检出 & ~ 未检出 & \\
\multicolumn{2}{l}{线索细胞} & 未检出 & ~ 未检出 & \\
\multicolumn{2}{l}{上皮细胞} & 10-15 & ~ 满视野 & \\
\multicolumn{5}{l}{} \\
\multicolumn{2}{l}{病原体情况:} & & & \\
\multicolumn{2}{l}{滴虫} & 未检出 & ~ 未检出 & \\
\multicolumn{2}{l}{菌丝} & 未检出 & ~ 未检出 & \\
\multicolumn{2}{l}{孢子} & 未检出 & ~ 未检出 & \\
\multicolumn{2}{l}{芽生孢子} & 未检出 & ~ 未检出 & \\
\multicolumn{5}{l}{} \\
\multicolumn{2}{l}{菌群情况:} & & & \\
\multicolumn{2}{l}{菌群密集度} & ++ & ~ ++ & \\
\multicolumn{2}{l}{多样性} & + & ~ ++ & \\
\multicolumn{2}{l}{优势菌} & G+杆菌 & ~ G阳性杆菌 & \\
\multicolumn{2}{l}{$\beta$-N-乙酰氨基葡萄糖苷酶(NAG)} & - & ~ - & \\
\multicolumn{5}{l}{} \\
\multicolumn{2}{l}{功能学分析:} & & & \\
\multicolumn{2}{l}{唾液酸苷酶} & - & ~ - & \\
\multicolumn{2}{l}{白细胞酯酶} & - & ~ - & \\
\multicolumn{2}{l}{胺试验} & - & ~ - & \\
\multicolumn{2}{l}{脯氨酸氨基肽酶PIP} & - & ~ - & \\
\multicolumn{2}{l}{过氧化氢(H2O2)} & + & ~ - & \\
\multicolumn{2}{l}{pH值} & 3.8 & 3.8 ~ 4.5 & \\
\multicolumn{2}{l}{Nugent评分2} & AV评分1 & & \\
\hline
\multicolumn{5}{l}{※ 备注:阴道微生态未见明显异常!} \\
\hline
\multicolumn{2}{l}{采集时间: 2026-01-06} & \multicolumn{2}{l}{接收时间: 2026-01-06} & \multicolumn{2}{l}{审核时间: 2026-01-06} \\
\multicolumn{2}{l}{09:15} & \multicolumn{2}{l}{09:22} & \multicolumn{2}{l}{10:59} \\
\multicolumn{2}{l}{送检医生: 权丽丽} & \multicolumn{2}{l}{检验者: 伊原原} & \multicolumn{2}{l}{审核者: 介倩倩} \\
\multicolumn{5}{l}{打印时间: 2026/2/26 下午 3:59:58} \\
\multicolumn{5}{l}{打印者: 网页打印} \\
\multicolumn{5}{l}{※本报告检查结果实行互认制度, 如有疑问, 请在三天内和我们联系, 电} \\
\hline
\end{tabular}
2026-08-06 10:32:19,840 INFO     30 [qwen-vl-parser] page=42 table: 50 LaTeX lines (bbox 2119-2168)
2026-08-06 10:32:19,840 INFO     30 [qwen-vl-parser] page=42 table: 50 sections
2026-08-06 10:32:20,088 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=906578, prompt_len=764
2026-08-06 10:32:21,677 INFO     30 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-06"
}
```
2026-08-06 10:32:21,678 INFO     30 [qwen-vl-parser] page=43 classify=table report_date=2026-01-06
2026-08-06 10:32:21,716 INFO     30 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=906578, prompt_len=756
2026-08-06 10:32:22,098 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:32:22.096+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 8, "lag": 0, "done": 1, "failed": 0, "current": {"00b9d592918111f18dbe1f8f96f1c395": {"id": "00b9d592918111f18dbe1f8f96f1c395", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011867426, "task_type": "dataflow", "root_trace_id": "1ab3198c92574fb4b2701d0f5db7322f", "root_traceparent": "00-1ab3198c92574fb4b2701d0f5db7322f-bdaff6f64a5f4a64-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "dfc102e2918111f18dbe1f8f96f1c395": {"id": "dfc102e2918111f18dbe1f8f96f1c395", "doc_id": "de8a02fc918111f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786012241604, "task_type": "dataflow", "root_trace_id": "90f550f6b00248c3845d57a8e0bcf6fb", "root_traceparent": "00-90f550f6b00248c3845d57a8e0bcf6fb-5db7fb7d470dfe0d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:32:26,421 INFO     30 [qwen-vl-parser] table API response (len=785):
\begin{tabular}{cccccc}
\hline
英文 & 项目名称 & 结果 & 参考范围 & 单位 & \\
\hline
\multicolumn{6}{c}{\textbf{[β-HCG]人绒毛膜促性腺激素}} \\
\multicolumn{6}{c}{0.40} \\
\multicolumn{6}{c}{非孕期 0~2.9} \\
\multicolumn{6}{c}{0.2-1周 5~50} \\
\multicolumn{6}{c}{1-2周 50~500} \\
\multicolumn{6}{c}{2-3周 100~5000} \\
\multicolumn{6}{c}{3-4周 500~10000} \\
\multicolumn{6}{c}{4-5周 1000~50000} \\
\multicolumn{6}{c}{5-6周 10000~100000} \\
\multicolumn{6}{c}{6-8周 15000~200000} \\
\multicolumn{6}{c}{mlU/ml} \\
\hline
\end{tabular}

\begin{tabular}{llllll}
\hline
采集时间: & 2026-01-06 & 接收时间: & 2026-01-06 & 审核时间: & 2026-01-06 \\
& 09:15 & & 10:03 & & 11:06 \\
送检医生: & 权丽丽 & 检验者: & 秦淑云 & 审核者: & 薛轩 \\
\hline
\end{tabular}

\begin{tabular}{ll}
\hline
打印时间: & 2026/2/26 下午 \\
& 4:00:10 \\
打印者: & 网页打印 \\
\hline
\end{tabular}
2026-08-06 10:32:26,424 INFO     30 [qwen-vl-parser] page=43 table: 34 LaTeX lines (bbox 2169-2202)
2026-08-06 10:32:26,424 INFO     30 [qwen-vl-parser] page=43 table: 34 sections
2026-08-06 10:32:26,657 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=740740, prompt_len=764
2026-08-06 10:32:28,164 INFO     30 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-06"
}
```
2026-08-06 10:32:28,164 INFO     30 [qwen-vl-parser] page=44 classify=table report_date=2026-01-06
2026-08-06 10:32:28,180 INFO     30 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=740740, prompt_len=756
2026-08-06 10:32:29,320 INFO     30 [qwen-vl-parser] table API response (len=156):
\begin{tabular}{ccccccc}
\hline
英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\
\hline
[OV125Ag]CA-125 & & 59.70 & $\uparrow$ & 0.00~35.00 & U/ml \\
\hline
\end{tabular}
2026-08-06 10:32:29,324 INFO     30 [qwen-vl-parser] page=44 table: 8 LaTeX lines (bbox 2203-2210)
2026-08-06 10:32:29,325 INFO     30 [qwen-vl-parser] page=44 table: 8 sections
2026-08-06 10:32:29,673 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1364813, prompt_len=764
2026-08-06 10:32:31,315 INFO     30 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-06"
}
```
2026-08-06 10:32:31,316 INFO     30 [qwen-vl-parser] page=45 classify=table report_date=2026-01-06
2026-08-06 10:32:31,344 INFO     30 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1364813, prompt_len=756
2026-08-06 10:32:39,046 INFO     30 [qwen-vl-parser] table API response (len=1224):
\begin{tabular}{ccccccccc}
\hline
英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\
\hline
{[}颜色{]}颜色 & 黄色 & & 清 & & & {[}尿酸结晶{]}尿酸结晶 & 0 & & & 0~15 & 个/ul \\
{[}浊度{]}浊度 & 清亮 & & 清 & & & {[}草酸钙结晶{]}草酸钙结晶 & 0 & & & 0~30 & 个/ul \\
{[}GLU{]}葡萄糖 & - & & 阴性 & & & {[}上皮细胞{]}上皮细胞 & 14 & & & 0~20 & 个/ul \\
{[}BLD{]}潜血 & - & & 阴性 & & & {[}粘液丝{]}粘液丝 & 5 & & & 0~20 & 个/ul \\
{[}LEU{]}白细胞 & 2+ & & 阴性 & & & {[}酵母菌{]}酵母菌 & 6 & $\uparrow$ & & 0~0 & 个/ul \\
{[}PRO{]}蛋白质 & - & & 阴性 & & & {[}透明管型{]}透明管型 & 0 & & & 0~1 & 个/ul \\
{[}NIT{]}亚硝酸盐 & + & & 阴性 & & & {[}颗粒管型{]}颗粒管型 & 0 & & & 0~0 & 个/ul \\
{[}URO{]}尿胆素原 & - & & 阴性 & & & {[}小圆上皮{]}小圆上皮 & 0 & & & 0~3 & 个/ul \\
{[}BIL{]}胆红素 & - & & 阴性 & & & {[}其他管型{]}其他管型 & 0 & & & 0~0 & 个/ul \\
{[}KET{]}酮体 & - & & 阴性 & & & {[}其他上皮{]}其他上皮 & 0 & & & 0~10 & 个/ul \\
{[}Vc{]}维生素C & - & & - & & & {[}异常红细胞{]}异常红细胞 & 0 & & & 0~5 & 个/ul \\
{[}pH{]}酸碱性 & 6.0 & & & 5.0~8.5 & & {[}细菌{]}细菌 & 1072 & $\uparrow$ & & 0~50 & 个/ul \\
{[}SG{]}比重 & 1.020 & & & 1.010~ & & {[}尿沉渣镜检{]}尿沉渣镜检 & : & & & & \\
{[}红细胞{]}红细胞 & 0 & & & 0~5 & 个/ul & {[}白细胞{]}白细胞 & +++/HP & & & $\le$5/HP & \\
{[}白细胞{]}白细胞 & 218 & $\uparrow$ & & 0~7 & 个/ul & {[}红细胞{]}红细胞 & 未查见 & & & $\le$3/HP & \\
\hline
\end{tabular}
2026-08-06 10:32:39,049 INFO     30 [qwen-vl-parser] page=45 table: 22 LaTeX lines (bbox 2211-2232)
2026-08-06 10:32:39,049 INFO     30 [qwen-vl-parser] page=45 table: 22 sections
2026-08-06 10:32:39,320 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=871040, prompt_len=764
2026-08-06 10:32:41,138 INFO     30 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-15"
}
```
2026-08-06 10:32:41,139 INFO     30 [qwen-vl-parser] page=46 classify=table report_date=2026-01-15
2026-08-06 10:32:41,163 INFO     30 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=871040, prompt_len=756
2026-08-06 10:32:41,493 INFO     30 [qwen-vl-parser] table API response (len=4078):
\begin{tabular}{llllllll}
\hline
\multicolumn{8}{c}{\textbf{南京鼓楼医院 检验科报告单}} \\
\multicolumn{8}{c}{南京大学医学院附属鼓楼医院} \\
\multicolumn{8}{c}{苏HR} \\
\hline
\multicolumn{2}{l}{【住院】} & \multicolumn{6}{l}{} \\
\multicolumn{2}{l}{第1页/共2页} & \multicolumn{6}{l}{} \\
\hline
\multicolumn{2}{l}{姓 \quad 名:} & \multicolumn{2}{l}{病 \quad 历 号:} & \multicolumn{4}{l}{临床诊断: 肺恶性肿瘤} \\
\multicolumn{2}{l}{性 \quad 别: 女} & \multicolumn{2}{l}{科 \quad 室: (江北) 综合肿瘤中} & \multicolumn{4}{l}{标本种类: 血液} \\
\multicolumn{2}{l}{年 \quad 龄: 75岁} & \multicolumn{2}{l}{床 \quad 号:} & \multicolumn{4}{l}{病 \quad 区: (江北) B7病区} \\
\multicolumn{8}{l}{申请医嘱: 生化全套, 心肌酶测定} \\
\hline
\multicolumn{2}{c}{检验项目} & \multicolumn{2}{c}{结果} & \multicolumn{2}{c}{参考区间-单位} & \multicolumn{2}{c}{检验项目} & \multicolumn{2}{c}{结果} & \multicolumn{2}{c}{参考区间-单位} \\
\hline
*丙氨酸氨基转移酶 & \uparrow & 50.3 & 7---40 U/L & *肌酐 & 73 & 41---81 umol/L \\
*天门冬氨酸氨基转移酶 & \uparrow & 35.4 & 13---35 U/L & *尿酸 & 221 & 155---357 umol/L \\
*碱性磷酸酶 & \downarrow & 43.2 & 50---135 U/L & 总二氧化碳 & 28.1 & 21---31 mmol/L \\
*γ-谷氨酰基转移酶 & \uparrow & 130.5 & 7---45 U/L & *甘油三酯 & \uparrow & 2.88 & $\le$1.7 mmol/L \\
*乳酸脱氢酶 & 193 & 120---250 U/L & *总胆固醇 & \uparrow & 5.81 & 3---5.7 mmol/L \\
*总胆红素 & 10.2 & $\le$21 umol/L & *H-脂蛋白胆固醇 & 1.26 & 1.03---1.55 mmol/L \\
*直接胆红素 & 3.3 & $\le$4 umol/L & *L-脂蛋白胆固醇 & \uparrow & 3.66 & 健康人<3.4; 不同ASCVD危 \\
*胆碱酯酶 & 8.8 & 5.3---11.3 KU/L & & & & 险人群目标值: 低危<3.4 \\
*总蛋白 & 78.9 & 65---85 g/L & & & & 中高危<2.6; 极高危<1.8 \\
*白蛋白 & 48.8 & 40---55 g/L & & & & 超高危<1.4 mmol/L \\
*球蛋白 & 30.1 & 20---40 g/L & & & & \\
白/球比例 & 1.62 & 1.2---2.4 & *载脂蛋白A I & 1.30 & 1---1.6 g/L \\
*总胆汁酸 & 4.0 & 0---13 umol/L & *载脂蛋白B & \uparrow & 1.15 & 0.6---1.1 g/L \\
亮氨酸氨肽酶 & 35.3 & 12---37 U/L & *总钙 & 2.46 & 2.11---2.52 mmol/L \\
*腺苷脱氨酶 & 21.3 & 0---25 U/L & *磷 & 1.37 & 0.85---1.51 mmol/L \\
*葡萄糖 & \uparrow & 8.35 & 3.9---6.1 mmol/L & *钾 & 4.18 & 3.5---5.3 mmol/L \\
*尿素 & 4.4 & 3.1---8.8 mmol/L & *钠 & 138.3 & 137---147 mmol/L \\
& & & & *氯 & 101.7 & 99---110 mmol/L \\
\hline
\multicolumn{8}{l}{检验意见:} \\
\hline
\multicolumn{4}{l}{送检医生: 杨阳} & \multicolumn{4}{l}{检验者: 柏玉} & \multicolumn{4}{l}{审核者: \underline{余安光}} \\
\multicolumn{4}{l}{采集时间: 2026-03-10 09:20} & \multicolumn{4}{l}{接收时间: 2026-03-10 09:38} & \multicolumn{4}{l}{报告时间: 2026-03-10 12:08} \\
\multicolumn{8}{l}{本报告单结果仅对送检标本负责！如有疑问请于报告时间3日内与检验科210231联系！} & \multicolumn{8}{l}{注: \uparrow-偏高, \downarrow-偏低, ★-危急值结果} \\
\multicolumn{8}{l}{项目名称前注“*”为省内互认项目} & \multicolumn{8}{l}{} \\
\hline
\end{tabular}

\begin{tabular}{llllllll}
\hline
\multicolumn{8}{c}{\textbf{南京鼓楼医院 检验科报告单}} \\
\multicolumn{8}{c}{南京大学医学院附属鼓楼医院} \\
\multicolumn{8}{c}{苏HR} \\
\hline
\multicolumn{2}{l}{【住院】} & \multicolumn{6}{l}{} \\
\multicolumn{2}{l}{第2页/共2页} & \multicolumn{6}{l}{} \\
\hline
\multicolumn{2}{l}{姓 \quad 名:} & \multicolumn{2}{l}{病 \quad 历 号:} & \multicolumn{4}{l}{临床诊断: 肺恶性肿瘤} \\
\multicolumn{2}{l}{性 \quad 别: 女} & \multicolumn{2}{l}{科 \quad 室: (江北) 综合肿瘤中} & \multicolumn{4}{l}{标本种类: 血液} \\
\multicolumn{2}{l}{年 \quad 龄: 75岁} & \multicolumn{2}{l}{床 \quad 号:} & \multicolumn{4}{l}{病 \quad 区: (江北) B7病区} \\
\multicolumn{8}{l}{申请医嘱: 生化全套, 心肌酶测定} \\
\hline
\multicolumn{2}{c}{检验项目} & \multicolumn{2}{c}{结果} & \multicolumn{2}{c}{参考区间-单位} & \multicolumn{2}{c}{检验项目} & \multicolumn{2}{c}{结果} & \multicolumn{2}{c}{参考区间-单位} \\
\hline
*C反应蛋白 & \uparrow & 11.2 & 0---6 mg/L & & & & & & & & \\
*肌酸激酶 & 56 & 40---200 U/L & & & & & & & & & \\
肌酸激酶MB同工酶 & 11 & 0---25 U/L & & & & & & & & & \\
*a 羟丁酸脱氢酶 & 120 & 59---126.4 U/L & & & & & & & & & \\
eGFR (CKD-EPI) & \downarrow & 69.6 & >90 ml/min/1.73m~2 & & & & & & & & \\
\hline
\multicolumn{8}{l}{检验意见:} \\
\hline
\multicolumn{4}{l}{送检医生: 杨阳} & \multicolumn{4}{l}{检验者: 柏玉} & \multicolumn{4}{l}{审核者: \underline{余安光}} \\
\multicolumn{4}{l}{采集时间: 2026-03-10 09:20} & \multicolumn{4}{l}{接收时间: 2026-03-10 09:38} & \multicolumn{4}{l}{报告时间: 2026-03-10 12:08} \\
\multicolumn{8}{l}{本报告单结果仅对送检标本负责！如有疑问请于报告时间3日内与检验科210231联系！} & \multicolumn{8}{l}{注: \uparrow-偏高, \downarrow-偏低, ★-危急值结果} \\
\multicolumn{8}{l}{项目名称前注“*”为省内互认项目} & \multicolumn{8}{l}{} \\
\hline
\end{tabular}
2026-08-06 10:32:41,497 INFO     30 [qwen-vl-parser] page=14 table: 75 LaTeX lines (bbox 383-457)
2026-08-06 10:32:41,499 INFO     30 [qwen-vl-parser] page=14 table: 75 sections
2026-08-06 10:32:41,501 INFO     30 [qwen-vl-parser] parse_pdf done: 458 sections from 14 pages.
2026-08-06 10:32:41,536 INFO     30 Close text detector.
2026-08-06 10:32:42,509 INFO     30 Close text recognizer.
2026-08-06 10:32:43,293 INFO     30 Close recognizer.
2026-08-06 10:32:43,936 INFO     30 [qwen-vl-parser] table API response (len=383):
\begin{tabular}{l l c c c c c}
\hline
英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\
\hline
{[}PT{]}凝血酶原时间 & & 11.0 & & 9.4~12.5 & s \\
{[}INR{]}国际标准化比例 & & 0.98 & & 0.8~1.2 & INR \\
{[}HDD{]}凝血酶原活动度 & & 103.00 & & 70~130 & \% \\
{[}APTT{]}部分凝血活酶时间(胶质硅) & & 33.7 & & 25.1~36.5 & s \\
{[}Fib{]}纤维蛋白原 & & 2.65 & & 2.00~4.00 & g/L \\
{[}TT{]}凝血酶时间 & & 15.1 & & 10.3~16.6 & s \\
\hline
\end{tabular}
2026-08-06 10:32:43,936 INFO     30 Close recognizer.
2026-08-06 10:32:44,734 INFO     30 [qwen-vl-parser] page=46 table: 13 LaTeX lines (bbox 2233-2245)
2026-08-06 10:32:44,734 INFO     30 [qwen-vl-parser] page=46 table: 13 sections
2026-08-06 10:32:44,808 INFO     30 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-06 10:32:44,809 INFO     30 [Trace] task=dfc102e2 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | Parser:MedLink | outputs={"html": "", "json": "458 items", "markdown": "", "text": "", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf", "output_format": "json"}
2026-08-06 10:32:44,809 INFO     30 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-06 10:32:44,906 INFO     30 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:32:44,907 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n⚠️ 住院病程文书归属：病程记录、查房记录、术前小结、术后首次病程记录等住院期间病程文书，与入院记录同属一次住院事件；当它们与入院记录页相邻时，必须合并为一个 AdmissionRecord 片段，不得单独成段、不得归入 DischargeRecord。\n- 病程文书识别特征：标题含\"病程记录\"/\"查房记录\"/\"术前小结\"/\"术后首次病程记录\"，带住院患者信息（科室/床号/住院号），有\"入院时间\"（如\"2020年07月08日 08:36:09入院\"），无\"出院诊断\"/\"出院医嘱\"\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。只有主诉，病史的也属于OutpatientRecord（门诊病历）\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 2025.5.21确诊小细胞肺癌\n[BBOX-1] 2025.5.28-2025.7.16 依托泊苷+卡铂+斯鲁利\n[BBOX-2] 2025.8.13-2025.11.7 依托泊苷+斯鲁利\n[BBOX-3] 南京鼓楼医院\n[BBOX-4] 南京大学医学院附属鼓楼医院\n[BBOX-5] 出院记录\n[BBOX-6] 科别（江北）综合肿瘤中心 病区（江北）B7病区床号07床 姓名\n[BBOX-7] 住院号\n[BBOX-8] 姓名：\n[BBOX-9] 性别：女 年龄：75岁 婚姻：已婚 职业：农民\n[BBOX-10] 入院诊断：1. 肺恶性肿瘤（左肺，小细胞癌广泛期）2. 肥 入院日期： 2025年12月03日\n[BBOX-11] 厚型梗阻性心肌病 3. 纵隔淋巴结肿大 4. 肺门\n[BBOX-12] 淋巴结肿大 5. 锁骨上淋巴结肿大（双侧）6. 腋\n[BBOX-13] 下淋巴结肿大（右）7. 心功能III级（NYHA分级）\n[BBOX-14] 8. 甲状腺功能减退症 9. 高血压2级（极高\n[BBOX-15] 危）10. 肺气肿（局限性）11. 肺诊断性影像检\n[BBOX-16] 查的异常所见（肺结节）12. 二尖瓣反流（重度）\n[BBOX-17] 13. 心包积液（少量）14. 肾上腺结节（左侧）\n[BBOX-18] 手术名称：\n[BBOX-19] 手术日期：\n[BBOX-20] 出院诊断：1. 恶性肿瘤支持治疗 2. 恶性肿瘤免疫治 出院日期： 2025年12月06日\n[BBOX-21] 疗 3. 肺恶性肿瘤（左肺，小细胞癌广泛期）\n[BBOX-22] 4. 肥厚型梗阻性心肌病 5. 纵隔淋巴结肿大\n[BBOX-23] 6. 肺门淋巴结肿大 7. 锁骨上淋巴结肿大\n[BBOX-24] (双侧) 8. 腋下淋巴结肿大(右) 9. 心功能\n[BBOX-25] III级(NYHA分级) 10. 甲状腺功能减退症\n[BBOX-26] 11. 高血压2级（极高危）12. 肺气肿(局\n[BBOX-27] 限性) 13. 肺诊断性影像检查的异常所见(肺\n[BBOX-28] 结节) 14. 二尖瓣反流(重度) 15. 心包积\n[BBOX-29] 液(少量) 16. 肾上腺结节(左侧)\n[BBOX-30] 入院时情况（主要症状、体征，有关实验室及器械检查结果）：\n[BBOX-31] 患者因“咳嗽1月余”于2025-05-21至河北省人民医院就诊，查胸部CT：左肺下叶占位性病变，恶性不除\n[BBOX-32] 外，远端阻塞性肺炎，建议完善实验室检查及增强CT。双侧锁骨窝、右侧腋下、纵隔内及双肺门多发肿大\n[BBOX-33] 淋巴结，转移不除外。左侧胸膜结节样增厚，转移不除外。后于2025-05-23行肺穿刺活检术，术后病理回\n[BBOX-34] 示：（左肺）穿刺组织：结合免疫组化染色支持小细胞癌。免疫组化染色： CKpan (+)，Vimentin (-)，\n[BBOX-35] CK7 (+)，TTF -1(+)，NapsinA (-)，CK5/6(-)，P40(-)，P63(-)，CgA (+)，Syn (+)，CD56(+)。根据患者病情\n[BBOX-36] 于2025-05-28当地医院行依托泊苷+卡铂方案化疗+斯鲁利单抗免疫治疗1周期，过程顺利。于\n[BBOX-37] 2025-06-19、2025-07-16开始行依托泊苷+卡铂化疗+斯鲁利单抗免疫治疗2周期，过程顺利。2025-07-27复\n[BBOX-38] 查血常规示血小板38×10^9/L。予升血小板治疗后。2025-08-13、2025-09-06、2025-10-08、2025-11-07\n[BBOX-39] 行依托泊苷化疗+斯鲁利单抗免疫治疗4周期，期间疗效评价PR。患者为求进一步治疗就诊我科，门诊拟\n[BBOX-40] 第 1 页\n[BBOX-41] 南京鼓楼医院\n[BBOX-42] 南京大学医学院附属鼓楼医院\n[BBOX-43] 出院记录\n[BBOX-44] 科别（江北）综合肿瘤中心 病区（江北）B7病区床号 姓名 住院号\n[BBOX-45] “肺恶性肿瘤”收住入院。病程中，患者神志清，精神可，食纳睡眠可，二便如常，近期体重未见明显变\n[BBOX-46] 化。\n[BBOX-47] 诊疗经过：\n[BBOX-48] 患者入院完善相关检查：\n[BBOX-49] 【检验】\n[BBOX-50] 2025.12.03 12:22 甲功三项：*促甲状腺激素 34.210 mIU/L↑，*游离三碘甲状腺原氨酸 2.60 pmol/L↓，\n[BBOX-51] *游离甲状腺素 9.58 pmol/L↓。\n[BBOX-52] 2025.12.03 12:22 肺癌六项（江北）：*细胞角蛋白19片段 3.61 ng/mL↑，*神经元特异性烯醇化酶\n[BBOX-53] 26.80 ng/mL↑，胃泌素释放肽前体 243.00 pg/mL↑。\n[BBOX-54] 2025.12.03 13:33 生化全套，心肌酶：*碱性磷酸酶 46.8 U/L↓，*葡萄糖 6.66 mmol/L↑，*甘油三酯\n[BBOX-55] 8.26 mmol/L↑，*总胆固醇 7.14 mmol/L↑，*H-脂蛋白胆固醇 0.90 mmol/L↓，*L-脂蛋白胆固醇 3.51\n[BBOX-56] mmol/L↑，*载脂蛋白AⅠ 0.79 g/L↓，*载脂蛋白B 1.87 g/L↑，*钠 136.1 mmol/L↓，*氯 97.8\n[BBOX-57] mmol/L↓，*α羟丁酸脱氢酶 158 U/L↑，eGFR(CKD-EPI) 77.2 ml/min/1.73m^2↓。\n[BBOX-58] 2025.12.03 14:45 血常规：淋巴细胞百分数 19.7 %↓，淋巴细胞绝对值 0.8 ×10^9/L↓，*红细胞计数\n[BBOX-59] 3.30 ×10^12/L↓，*血红蛋白量 108 g/L↓，*红细胞压积 31.8 %↓，红细胞体积分布宽度 15.4 %↑，*\n[BBOX-60] 血小板计数 112 ×10^9/L↓。\n[BBOX-61] 余未见明显异常。\n[BBOX-62] 【检查】\n[BBOX-63] 2025.12.04 15:19 心电图检查（江北）（检查）常规心电图 检查结论 窦性心律一度房室传导阻滞左前分支\n[BBOX-64] 阻滞异常Q波(V1、V2)左心室高电压ST-T改变QTc间期延长\n[BBOX-65] 2025.12.04 16:29（江北）PET/CT(检查) PET/CT全身显像 检查结论 1.“左肺癌化疗后复查”；①左下肺\n[BBOX-66] 门稍大伴葡萄糖代谢增高灶，内部通行支气管狭窄，结合病史考虑符合小细胞癌表现；②左肺下叶两枚软\n[BBOX-67] 组织结节，葡萄糖代谢异常增高；双肺门、纵隔、右侧腋窝多发肿大淋巴结，葡萄糖代谢显著增高；以上\n[BBOX-68] 考虑同侧肺内转移、多发淋巴结转移；2.双肺多发小结节，部分为磨玻璃结节，葡萄糖代谢未见增高，建\n[BBOX-69] 议胸部CT随诊；双肺散在条索及渗出；左肺下叶节段性肺不张；右肺局限性肺气肿；双侧胸膜增厚；3.左\n[BBOX-70] 肾上腺稍低密度结节，葡萄糖代谢未见异常增高，左肾上腺稍增粗，葡萄糖代谢轻度增高，倾向增生伴腺\n[BBOX-71] 瘤形成，请比对老片、密切随诊观察；4.腔隙性脑梗死可能；脑萎缩；副鼻窦炎症；甲状腺左右两叶密度\n[BBOX-72] 欠均，葡萄糖代谢增高，考虑炎性摄取增高，必要时请结合甲功、颈部超声随诊；5.心影偏大，冠状动脉\n[BBOX-73] 及胸部大血管管壁钙化；6.食管中下段管壁似稍增厚，葡萄糖代谢轻度增高，考虑炎性或生理性摄取可\n[BBOX-74] 能，必要时内镜检查；十二指肠憩室可能；轻度脂肪肝；肝囊肿；胆囊饱满；7.慢性膀胱炎症可能；盆腔\n[BBOX-75] 内钙化结节；8.颈椎生理性曲度变直，脊柱退变；右股骨下段低密度伴内部钙化，葡萄糖代谢不高，考虑\n[BBOX-76] 第 2 页\n[BBOX-77] 3/4\n[BBOX-78] 南京鼓楼医院\n[BBOX-79] 南京大学医学院附属鼓楼医院\n[BBOX-80] 出院记录\n[BBOX-81] 科别（江北）综合肿瘤中心 病区（江北）B7病区床号\n[BBOX-82] 姓名 住院号\n[BBOX-83] 良性灶如内生软骨瘤可能，随诊；右肩背部皮下稍低密度结节，葡萄糖代谢未见增高，考虑良性灶，随\n[BBOX-84] 诊。\n[BBOX-85] 【诊疗经过】\n[BBOX-86] 患者入院后完善PET-CT复查，病情较前基本相仿，暂无根治性放疗指征。排除禁忌后，患者于2025-12-05\n[BBOX-87] 行斯鲁利单抗免疫维持治疗1周期。现本周期静脉治疗已结束，现整体病情稳定，一般情况尚可，准予办理\n[BBOX-88] 出院。\n[BBOX-89] 出院情况： 好转\n[BBOX-90] 伤口愈合：-\n[BBOX-91] ECOG 1分，NRS 0分，神志清，精神可，无贫血貌，全身皮肤巩膜无黄染。胸廓外形正常，无胸壁静脉曲\n[BBOX-92] 张。双侧呼吸运动对称，肋间隙：正常，触觉语颤：对称，皮下捻发感：无，双肺叩诊清音，双肺呼吸音\n[BBOX-93] 稍粗，两肺未闻及明显干湿啰音。心律齐，心脏各瓣膜区未闻及杂音。腹部平坦，腹部无压痛，无反跳\n[BBOX-94] 痛。双下肢无明显水肿。\n[BBOX-95] 出院医嘱：\n[BBOX-96] 1、注意天气变化，注意休息、低脂饮食，避免受凉，避免手足接触冰冷物体，注意皮肤保暖。\n[BBOX-97] 2、出院后继续用药\n[BBOX-98] 左甲状腺素钠片（优甲乐）50微克/片 1片 口服 QD（7点）（每天早餐前半小时服用1片，补充甲状腺激\n[BBOX-99] 素，内分泌科随诊调药）\n[BBOX-100] 3、定期复查血常规（每周1-2次）及生化全套（每周1次），如WBC<3.0×10^9/L、PLT<60×10^9/L或生化\n[BBOX-101] 全套指标异常，请及时当地医院就诊（如有急症或危急值报告，请及时就近正规医院急诊就诊），我科门\n[BBOX-102] 诊随诊。\n[BBOX-103] 4、下次治疗时间：3-4周左右，具体等电话通知。杨阳主任医师专家门诊时间：门诊时间：每周二、周五\n[BBOX-104] 上午，（周二本部，周五江北），（江北肿瘤科医生办公室电话：025-83106666转220717）。如需肿瘤日\n[BBOX-105] 间治疗，请提前一周至杨阳主任医师门诊预约。\n[BBOX-106] 5、不适门诊随诊。\n[BBOX-107] 不存在尚未回归的病理检查结果。\n[BBOX-108] X光片号：-\n[BBOX-109] CT号： P049684\n[BBOX-110] MRI号：-\n[BBOX-111] 病理号：-\n[BBOX-112] 上级医师：\n[BBOX-113] 医师：\n[BBOX-114] 第 3 页\n[BBOX-115] 河北省人民医院\n[BBOX-116] 病理检查报告单\n[BBOX-117] 病理号\n[BBOX-118] 姓名:\n[BBOX-119] 性别: 女\n[BBOX-120] 年龄: 74岁\n[BBOX-121] 送检单位: 本院\n[BBOX-122] 科别: 胸外二科病区\n[BBOX-123] 住院号\n[BBOX-124] 床号:\n[BBOX-125] 送检日期: 2025-05-23 16:44\n[BBOX-126] 送检材料: 左肺穿刺数条:\n[BBOX-127] 临床诊断: 左肺占位\n[BBOX-128] 图像:\n[BBOX-129] 大体检查:\n[BBOX-130] (左肺穿刺数条:)穿刺组织3条, 长共3cm, 直径0.1cm。\n[BBOX-131] 病理诊断:\n[BBOX-132] (左肺)穿刺组织: 浸润性癌, 类型待免疫组化助诊。\n[BBOX-133] 诊断医师:\n[BBOX-134] 郑国卿 王彤彤\n[BBOX-135] 日期: 2025-05-26 14:23\n[BBOX-136] 注:1.此报告仅供临床医师参考, 如有异议请在两日内与诊断医师联系。 电话: (0311)85988183\n[BBOX-137] 2.国家规定小标本(咬检及穿刺组织)3个工作日内出报告; 其余标本5个工作日内出报告(特殊处理标本除外)。\n[BBOX-138] 住院病历\n[BBOX-139] 河北省人民医院\n[BBOX-140] 病理检查补充报告单\n[BBOX-141] 病理号:\n[BBOX-142] 姓名:\n[BBOX-143] 性别: 女\n[BBOX-144] 年龄: 74岁\n[BBOX-145] 送检单位: 本院\n[BBOX-146] 科别: 胸外二科病区\n[BBOX-147] 住院号:\n[BBOX-148] 床号:\n[BBOX-149] 送检日期: 2025-05-23 16:44\n[BBOX-150] 送检材料: 左肺穿刺数条:\n[BBOX-151] 临床诊断: 左肺占位\n[BBOX-152] 补充病理诊断:\n[BBOX-153] (左肺)穿刺组织: 结合免疫组化染色支持小细胞癌。\n[BBOX-154] 免疫组化染色: CKpan (+), Vimentin (-), CK7 (+), TTF-1 (+), NapsinA (-), CK5/6\n[BBOX-155] (-), P40 (-), P63 (-), CgA (+), Syn (+), CD56 (+), Ki-67 (90%+)。\n[BBOX-156] 诊断医师: 康林 郑国娜\n[BBOX-157] 报告日期: 2025-05-27 16:\n[BBOX-158] 注: 此报告仅供临床医师参考, 如有异议或病情有新变化务请及时与病理诊断医师联系(电话: 85988409)\n[BBOX-159] 河北省人民医院\n[BBOX-160] 住院病历\n[BBOX-161] <\n[BBOX-162] 南京鼓楼医院云胶片\n[BBOX-163] 南京鼓楼医院\n[BBOX-164] 南京大学医学院附属鼓楼医院\n[BBOX-165] 影像检查诊断报告\n[BBOX-166] 互联网医院\n[BBOX-167] 电子影像\n[BBOX-168] 检查号:\n[BBOX-169] 患者类型: 住院\n[BBOX-170] 患者编号:\n[BBOX-171] 姓名:\n[BBOX-172] 性别: 女\n[BBOX-173] 年龄: 75岁\n[BBOX-174] 科别: (江北)综合肿瘤中心 病区: (江北)B7病区\n[BBOX-175] 病床:\n[BBOX-176] 检查日期: 2026-03-11 13:39:06\n[BBOX-177] 设备类型: CT\n[BBOX-178] 技师: 王雨晓\n[BBOX-179] 检查项目: [CT平扫+增强(颈部、胸部、上腹部、下腹部、盆腔)]\n[BBOX-180] 检查所见:\n[BBOX-181] 颈部软组织CT平扫+增强:\n[BBOX-182] 【所见咽部】所见咽腔结构对称,未见明显异常密度影。增强后未见明显异常强化。\n[BBOX-183] 【喉部及下咽部】喉腔结构对称,会厌、声带、梨状窝形态及密度未见明显异常。增强后未见\n[BBOX-184] 明显异常强化。\n[BBOX-185] 【甲状腺及甲状旁腺区】甲状腺左右叶大小、形态正常,甲状腺双叶低密度结节;甲状旁腺区\n[BBOX-186] 未见明显占位性病变。\n[BBOX-187] 【唾液腺】双侧腮腺、颌下腺形态密度未见明显异常。增强后未见明显异常强化。\n[BBOX-188] 【气管及食管】气管居中,管腔通畅;食管颈段管壁未见明显增厚。\n[BBOX-189] 【颈部间隙】脂肪间隙清晰,未见明显异常密度影。增强后未见明显异常强化。\n[BBOX-190] 【淋巴结】两侧锁骨上窝多发肿大淋巴结。\n[BBOX-191] 【其他】副鼻窦内低密度影。\n[BBOX-192] 胸部CT平扫+增强:\n[BBOX-193] 【肺野】两肺野纹理清晰,左肺下叶见斑片状高密度影。右肺上叶舌段小片状高密度影。两肺\n[BBOX-194] 多发结节,较大者:右肺上叶(Img79)见一实性结节影,大小约5mm×3mm。两肺索条及片絮影;右\n[BBOX-195] 肺上叶局部透亮区。\n[BBOX-196] 【肺门】双肺门多发肿大淋巴结,大者位于左侧,短径约20mm,增强后强化不均。\n[BBOX-197] 【气管及支气管】左下肺支气管闭塞伴阻塞性炎症,病灶周围结节影。\n[BBOX-198] 【纵隔】纵隔居中,纵隔内多发肿大淋巴结,较大者短径约20mm。\n[BBOX-199] 【心脏及大血管】心影增大;主动脉及冠状动脉壁见致密影。\n[BBOX-200] 【胸膜及胸腔】胸膜:两侧胸膜可见增厚;胸腔积液:否。增强后未见明显异常强化。\n[BBOX-201] 【膈肌】光整,未见明显异常抬高。增强后未见明显异常强化。\n[BBOX-202] 【胸壁】胸廓对称,骨质未见明显异常。增强后未见明显异常强化。\n[BBOX-203] 上腹部、下腹部、盆腔CT平扫+增强:\n[BBOX-204] 报告日期: 2026-03-11 15:35:37\n[BBOX-205] 诊断医师: 申欣怡\n[BBOX-206] / 申欣怡\n[BBOX-207] 审核日期: 2026-03-12 13:17:06\n[BBOX-208] 审核医师: 王国\n[BBOX-209] （本报告仅供临床医生参考）\n[BBOX-210] 南京市中山路321号\n[BBOX-211] 南京鼓楼医院云胶片\n[BBOX-212] 女/75岁\n[BBOX-213] 设备类型 CT 患者类型 无\n[BBOX-214] 检查项目 [CT平扫+增强（颈部、胸部、上腹部、下\n[BBOX-215] 腹部、盆腔）]\n[BBOX-216] PDF报告 图像 分享\n[BBOX-217] 报告 2025-10-08\n[BBOX-218] 影像描述\n[BBOX-219] 颈部软组织CT平扫+增强：\n[BBOX-220] 【所见咽部】所见咽腔结构对称，未见明显异常\n[BBOX-221] 密度影。增强后未见明显异常强化。\n[BBOX-222] 【喉部及下咽部】喉腔结构对称，会厌、声带、\n[BBOX-223] 梨状窝形态及密度未见明显异常。增强后未见明显\n[BBOX-224] 异常强化。\n[BBOX-225] 【甲状腺及甲状旁腺区】甲状腺左右叶大小、形\n[BBOX-226] 态正常，甲状腺双叶低密度结节；甲状旁腺区未见\n[BBOX-227] 明显占位性病变。\n[BBOX-228] 【唾液腺】双侧腮腺、颌下腺形态密度未见明显\n[BBOX-229] 异常。增强后未见明显异常强化。\n[BBOX-230] 【气管及食管】气管居中，管腔通畅；食管颈段\n[BBOX-231] 管壁未见明显增厚。\n[BBOX-232] 【颈部间隙】脂肪间隙清晰，未见明显异常密度\n[BBOX-233] 影。增强后未见明显异常强化。\n[BBOX-234] 【淋巴结】未见明显肿大淋巴结。\n[BBOX-235] 【其他】副鼻窦内低密度影。\n[BBOX-236] 胸部CT平扫+增强：\n[BBOX-237] 【肺野】两肺野纹理清晰，左肺下叶见斑片状高\n[BBOX-238] 移动影像浏览\n[BBOX-239] © 2022 南京鼓楼医院影像云平台 V1.0\n[BBOX-240] 南京鼓楼医院云胶片\n[BBOX-241] 女/75岁\n[BBOX-242] 设备类型 CT 患者类型 无\n[BBOX-243] 检查项目 [CT平扫+增强（颈部、胸部、上腹部、下\n[BBOX-244] 腹部、盆腔）]\n[BBOX-245] PDF报告 图像 分享\n[BBOX-246] 【肺野】两肺野纹理清晰，左肺下叶见斑片状高\n[BBOX-247] 密度影。两肺多发结节，较大者：右肺上叶（Img7\n[BBOX-248] 9）见一实性结节影，大小约5mm×3mm。两肺索\n[BBOX-249] 条及片絮影；右肺上叶局部透亮区。\n[BBOX-250] 【肺门】双肺门多发小淋巴结，部分稍大。\n[BBOX-251] 【气管及支气管】左下肺支气管闭塞伴阻塞性炎\n[BBOX-252] 症，病灶周围结节影。\n[BBOX-253] 【纵隔】纵隔居中，纵隔内多发小淋巴结，部分\n[BBOX-254] 稍大，较大者短径约10mm。\n[BBOX-255] 【心脏及大血管】心影增大；主动脉及冠状动\n[BBOX-256] 脉壁见致密影。\n[BBOX-257] 【胸膜及胸腔】胸膜：两侧胸膜可见增厚；胸腔\n[BBOX-258] 积液：否。增强后未见明显异常强化。\n[BBOX-259] 【膈肌】光整，未见明显异常抬高。增强后未见\n[BBOX-260] 明显异常强化。\n[BBOX-261] 【胸壁】胸廓对称，骨质未见明显异常。增强后\n[BBOX-262] 未见明显异常强化。\n[BBOX-263] 上腹部CT平扫+增强：\n[BBOX-264] 【肝脏】各叶比例在正常范围内，外形轮廓规\n[BBOX-265] 则，肝内小圆形无强化低密度影，较大者长径约6\n[BBOX-266] mm。静脉期肝左叶小片状稍低密度影（薄层im29\n[BBOX-267] 0）。\n[BBOX-268] 【胆囊及胆管】胆囊形态、大小正常，囊壁未见\n[BBOX-269] 移动影像浏览\n[BBOX-270] © 2022 南京鼓楼医院影像云平台 V1.0\n[BBOX-271] 南京鼓楼医院云胶片\n[BBOX-272] 女/75岁\n[BBOX-273] 设备类型 CT 患者类型 无\n[BBOX-274] 检查项目 [CT平扫+增强（颈部、胸部、上腹部、下\n[BBOX-275] 腹部、盆腔）]\n[BBOX-276] PDF报告 图像 分享\n[BBOX-277] 【胆囊及胆管】胆囊形态、大小正常，囊壁未见\n[BBOX-278] 增厚，囊内未见明显异常密度影；肝内外胆管轻度\n[BBOX-279] 扩张。\n[BBOX-280] 【胰腺】形态、大小正常，实质内未见明显异常\n[BBOX-281] 密度影；胰管未见明显扩张。增强后未见明显异常\n[BBOX-282] 强化。\n[BBOX-283] 【脾脏】形态、大小正常，实质内未见明显异常\n[BBOX-284] 密度影。增强后未见明显异常强化。\n[BBOX-285] 【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均\n[BBOX-286] 匀，未见明显肿大淋巴结，未见明显渗出及积液。\n[BBOX-287] 增强后未见明显异常强化。\n[BBOX-288] 下腹部CT平扫+增强：\n[BBOX-289] 【肾脏】两侧肾脏大小、形态、位置正常，右肾\n[BBOX-290] 窦点状致密影；肾盂肾盏未见明显扩张。增强后未\n[BBOX-291] 见明显异常强化。\n[BBOX-292] 【肾上腺】双肾上腺增粗，左肾上腺低密度结\n[BBOX-293] 节，长径约12mm,可见强化。\n[BBOX-294] 【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均\n[BBOX-295] 匀，未见明显肿大淋巴结，未见明显渗出及积液。\n[BBOX-296] 增强后未见明显异常强化。\n[BBOX-297] 盆腔CT平扫+增强：\n[BBOX-298] 【膀胱】充盈欠佳，壁未见明显增厚，其内未见\n[BBOX-299] 明显异常密度影。增强后未见明显异常强化。\n[BBOX-300] 【子宫及附件】子宫呈肌组织结构性空扫\n[BBOX-301] 移动影像浏览\n[BBOX-302] © 2022 南京鼓楼医院影像云平台 V1.0\n[BBOX-303] 南京鼓楼医院云胶片\n[BBOX-304] 女/75岁\n[BBOX-305] 设备类型 CT 患者类型 无\n[BBOX-306] 检查项目 [CT平扫+增强（颈部、胸部、上腹部、下\n[BBOX-307] 腹部、盆腔）]\n[BBOX-308] PDF报告 图像 分享\n[BBOX-309] 诊断意见\n[BBOX-310] 1.肺癌复查：左肺下叶斑片影较前（2025-07-15）\n[BBOX-311] 明显缩小，左下肺支气管闭塞伴阻塞性炎症，较前\n[BBOX-312] 缓解，密切随诊；双侧纵隔内及双肺门多发稍大淋\n[BBOX-313] 巴结，部分较前稍缩小。\n[BBOX-314] 2.两肺多发结节，较前变化不大，密切随诊。\n[BBOX-315] 3.两侧胸膜增厚；两肺索条及炎性渗出，较前缓\n[BBOX-316] 解；右肺上叶局限性肺气肿。\n[BBOX-317] 4.心影增大；主动脉及冠状动脉壁钙化。\n[BBOX-318] 5.肝脏小囊肿；静脉期肝左叶小片状稍低密度影\n[BBOX-319] （薄层im290），较前相仿，随诊。\n[BBOX-320] 6.肝内外胆管轻度扩张。\n[BBOX-321] 7.双肾上腺增粗，左肾上腺腺瘤可能，结合专科检\n[BBOX-322] 查；右肾小结石。\n[BBOX-323] 8.子宫肌瘤可能，结合妇科超声；盆腔内钙化结\n[BBOX-324] 节。\n[BBOX-325] 9.下腹腔内肠系膜间隙多发稍大淋巴结。\n[BBOX-326] 10.食管下段壁轻度增厚；乙状结肠迂曲冗长；结肠\n[BBOX-327] 内容物多；十二指肠降部憩室；结合临床体征随\n[BBOX-328] 诊。\n[BBOX-329] 11.右肩部皮下低密度结节，较前相仿，随诊；L4及\n[BBOX-330] 以上椎体I°滑脱。\n[BBOX-331] 移动影像浏览\n[BBOX-332] © 2022 南京鼓楼医院影像云平台 V1.0\n[BBOX-333] 南京鼓楼医院\n[BBOX-334] 南京大学医学院附属鼓楼医院\n[BBOX-335] 互联网医院\n[BBOX-336] 门诊病历\n[BBOX-337] 姓名:\n[BBOX-338] 性别:女\n[BBOX-339] 年龄:75岁\n[BBOX-340] ID:\n[BBOX-341] 2026年03月16日15时20分 (江北)心血管内科门诊\n[BBOX-342] 主诉:要求进行心功能分级\n[BBOX-343] 病史:患者平时正常活动不受限。\n[BBOX-344] 过敏史:无吸烟史\n[BBOX-345] 药物过敏史。无流行病学史\n[BBOX-346] 体查:\n[BBOX-347] 级)\n[BBOX-348] 诊断:\n[BBOX-349] 1.心功能I级(NYHA分\n[BBOX-350] 2.高脂血症\n[BBOX-351] 处理:随诊\n[BBOX-352] 1.非诺贝特胶囊(力平之)\n[BBOX-353] 200mg/粒\n[BBOX-354] 用法:1粒\n[BBOX-355] 口服\n[BBOX-356] 一次/日\n[BBOX-357] x3盒 28天\n[BBOX-358] 医师:\n[BBOX-359] 齐\n[BBOX-360] 第1页\n[BBOX-361] \\begin{tabular}{cccccc}\n[BBOX-362] 报告时间: 2026-03-10\n[BBOX-363] \\hline\n[BBOX-364] \\multicolumn{2}{c}{\\textbf{检验项目}} & \\textbf{结果} & \\textbf{参考区间-单位} & \\multicolumn{2}{c}{\\textbf{检验项目}} & \\textbf{结果} & \\textbf{参考区间-单位} \\\\\n[BBOX-365] \\hline\n[BBOX-366] *白细胞计数 & & 4.2 & 3.5--9.5 10^9/L & *平均红细胞血红蛋白含量 & & 31.4 & 27--34 pg \\\\\n[BBOX-367] 中性粒细胞百分数 & & 74.5 & 40--75 \\% & *平均红细胞血红蛋白浓度 & & 332 & 316--354 g/L \\\\\n[BBOX-368] 淋巴细胞百分数 & & 16.1 & 20--50 \\% & 红细胞体积分布宽度 & & 13.6 & 0-14 \\% \\\\\n[BBOX-369] 单核细胞百分数 & & 6.9 & 3--10 \\% & *血小板计数 & & 179 & 125--350 10^9/L \\\\\n[BBOX-370] 嗜酸性粒细胞百分数 & & 1.7 & 0.4--8 \\% & & & & \\\\\n[BBOX-371] 嗜碱性粒细胞百分数 & & 0.8 & 0-1 \\% & & & & \\\\\n[BBOX-372] 中性粒细胞绝对值 & & 3.1 & 1.8--6.3 10^9/L & & & & \\\\\n[BBOX-373] 淋巴细胞绝对值 & & 0.7 & 1.1--3.2 10^9/L & & & & \\\\\n[BBOX-374] 单核细胞绝对值 & & 0.3 & 0.1--0.6 10^9/L & & & & \\\\\n[BBOX-375] 嗜酸性粒细胞绝对值 & & 0.07 & 0.02--0.52 10^9/L & & & & \\\\\n[BBOX-376] 嗜碱性粒细胞绝对值 & & 0.03 & 0--0.06 10^9/L & & & & \\\\\n[BBOX-377] *红细胞计数 & & 4.01 & 3.8-5.1 10^12/L & & & & \\\\\n[BBOX-378] *血红蛋白量 & & 126 & 115--150 g/L & & & & \\\\\n[BBOX-379] *红细胞压积 & & 38.0 & 35--45 \\% & & & & \\\\\n[BBOX-380] *平均红细胞体积 & & 94.7 & 82--100 fl & & & & \\\\\n[BBOX-381] \\hline\n[BBOX-382] \\end{tabular}\n[BBOX-383] \\begin{tabular}{llllllll}\n[BBOX-384] 报告时间: 2026-03-10\n[BBOX-385] \\hline\n[BBOX-386] \\multicolumn{8}{c}{\\textbf{南京鼓楼医院 检验科报告单}} \\\\\n[BBOX-387] \\multicolumn{8}{c}{南京大学医学院附属鼓楼医院} \\\\\n[BBOX-388] \\multicolumn{8}{c}{苏HR} \\\\\n[BBOX-389] \\hline\n[BBOX-390] \\multicolumn{2}{l}{【住院】} & \\multicolumn{6}{l}{} \\\\\n[BBOX-391] \\multicolumn{2}{l}{第1页/共2页} & \\multicolumn{6}{l}{} \\\\\n[BBOX-392] \\hline\n[BBOX-393] \\multicolumn{2}{l}{姓 \\quad 名:} & \\multicolumn{2}{l}{病 \\quad 历 号:} & \\multicolumn{4}{l}{临床诊断: 肺恶性肿瘤} \\\\\n[BBOX-394] \\multicolumn{2}{l}{性 \\quad 别: 女} & \\multicolumn{2}{l}{科 \\quad 室: (江北) 综合肿瘤中} & \\multicolumn{4}{l}{标本种类: 血液} \\\\\n[BBOX-395] \\multicolumn{2}{l}{年 \\quad 龄: 75岁} & \\multicolumn{2}{l}{床 \\quad 号:} & \\multicolumn{4}{l}{病 \\quad 区: (江北) B7病区} \\\\\n[BBOX-396] \\multicolumn{8}{l}{申请医嘱: 生化全套, 心肌酶测定} \\\\\n[BBOX-397] \\hline\n[BBOX-398] \\multicolumn{2}{c}{检验项目} & \\multicolumn{2}{c}{结果} & \\multicolumn{2}{c}{参考区间-单位} & \\multicolumn{2}{c}{检验项目} & \\multicolumn{2}{c}{结果} & \\multicolumn{2}{c}{参考区间-单位} \\\\\n[BBOX-399] \\hline\n[BBOX-400] *丙氨酸氨基转移酶 & \\uparrow & 50.3 & 7---40 U/L & *肌酐 & 73 & 41---81 umol/L \\\\\n[BBOX-401] *天门冬氨酸氨基转移酶 & \\uparrow & 35.4 & 13---35 U/L & *尿酸 & 221 & 155---357 umol/L \\\\\n[BBOX-402] *碱性磷酸酶 & \\downarrow & 43.2 & 50---135 U/L & 总二氧化碳 & 28.1 & 21---31 mmol/L \\\\\n[BBOX-403] *γ-谷氨酰基转移酶 & \\uparrow & 130.5 & 7---45 U/L & *甘油三酯 & \\uparrow & 2.88 & $\\le$1.7 mmol/L \\\\\n[BBOX-404] *乳酸脱氢酶 & 193 & 120---250 U/L & *总胆固醇 & \\uparrow & 5.81 & 3---5.7 mmol/L \\\\\n[BBOX-405] *总胆红素 & 10.2 & $\\le$21 umol/L & *H-脂蛋白胆固醇 & 1.26 & 1.03---1.55 mmol/L \\\\\n[BBOX-406] *直接胆红素 & 3.3 & $\\le$4 umol/L & *L-脂蛋白胆固醇 & \\uparrow & 3.66 & 健康人<3.4; 不同ASCVD危 \\\\\n[BBOX-407] *胆碱酯酶 & 8.8 & 5.3---11.3 KU/L & & & & 险人群目标值: 低危<3.4 \\\\\n[BBOX-408] *总蛋白 & 78.9 & 65---85 g/L & & & & 中高危<2.6; 极高危<1.8 \\\\\n[BBOX-409] *白蛋白 & 48.8 & 40---55 g/L & & & & 超高危<1.4 mmol/L \\\\\n[BBOX-410] *球蛋白 & 30.1 & 20---40 g/L & & & & \\\\\n[BBOX-411] 白/球比例 & 1.62 & 1.2---2.4 & *载脂蛋白A I & 1.30 & 1---1.6 g/L \\\\\n[BBOX-412] *总胆汁酸 & 4.0 & 0---13 umol/L & *载脂蛋白B & \\uparrow & 1.15 & 0.6---1.1 g/L \\\\\n[BBOX-413] 亮氨酸氨肽酶 & 35.3 & 12---37 U/L & *总钙 & 2.46 & 2.11---2.52 mmol/L \\\\\n[BBOX-414] *腺苷脱氨酶 & 21.3 & 0---25 U/L & *磷 & 1.37 & 0.85---1.51 mmol/L \\\\\n[BBOX-415] *葡萄糖 & \\uparrow & 8.35 & 3.9---6.1 mmol/L & *钾 & 4.18 & 3.5---5.3 mmol/L \\\\\n[BBOX-416] *尿素 & 4.4 & 3.1---8.8 mmol/L & *钠 & 138.3 & 137---147 mmol/L \\\\\n[BBOX-417] & & & & *氯 & 101.7 & 99---110 mmol/L \\\\\n[BBOX-418] \\hline\n[BBOX-419] \\multicolumn{8}{l}{检验意见:} \\\\\n[BBOX-420] \\hline\n[BBOX-421] \\multicolumn{4}{l}{送检医生: 杨阳} & \\multicolumn{4}{l}{检验者: 柏玉} & \\multicolumn{4}{l}{审核者: \\underline{余安光}} \\\\\n[BBOX-422] \\multicolumn{4}{l}{采集时间: 2026-03-10 09:20} & \\multicolumn{4}{l}{接收时间: 2026-03-10 09:38} & \\multicolumn{4}{l}{报告时间: 2026-03-10 12:08} \\\\\n[BBOX-423] \\multicolumn{8}{l}{本报告单结果仅对送检标本负责！如有疑问请于报告时间3日内与检验科210231联系！} & \\multicolumn{8}{l}{注: \\uparrow-偏高, \\downarrow-偏低, ★-危急值结果} \\\\\n[BBOX-424] \\multicolumn{8}{l}{项目名称前注“*”为省内互认项目} & \\multicolumn{8}{l}{} \\\\\n[BBOX-425] \\hline\n[BBOX-426] \\end{tabular}\n[BBOX-427] \\begin{tabular}{llllllll}\n[BBOX-428] 报告时间: 2026-03-10\n[BBOX-429] \\hline\n[BBOX-430] \\multicolumn{8}{c}{\\textbf{南京鼓楼医院 检验科报告单}} \\\\\n[BBOX-431] \\multicolumn{8}{c}{南京大学医学院附属鼓楼医院} \\\\\n[BBOX-432] \\multicolumn{8}{c}{苏HR} \\\\\n[BBOX-433] \\hline\n[BBOX-434] \\multicolumn{2}{l}{【住院】} & \\multicolumn{6}{l}{} \\\\\n[BBOX-435] \\multicolumn{2}{l}{第2页/共2页} & \\multicolumn{6}{l}{} \\\\\n[BBOX-436] \\hline\n[BBOX-437] \\multicolumn{2}{l}{姓 \\quad 名:} & \\multicolumn{2}{l}{病 \\quad 历 号:} & \\multicolumn{4}{l}{临床诊断: 肺恶性肿瘤} \\\\\n[BBOX-438] \\multicolumn{2}{l}{性 \\quad 别: 女} & \\multicolumn{2}{l}{科 \\quad 室: (江北) 综合肿瘤中} & \\multicolumn{4}{l}{标本种类: 血液} \\\\\n[BBOX-439] \\multicolumn{2}{l}{年 \\quad 龄: 75岁} & \\multicolumn{2}{l}{床 \\quad 号:} & \\multicolumn{4}{l}{病 \\quad 区: (江北) B7病区} \\\\\n[BBOX-440] \\multicolumn{8}{l}{申请医嘱: 生化全套, 心肌酶测定} \\\\\n[BBOX-441] \\hline\n[BBOX-442] \\multicolumn{2}{c}{检验项目} & \\multicolumn{2}{c}{结果} & \\multicolumn{2}{c}{参考区间-单位} & \\multicolumn{2}{c}{检验项目} & \\multicolumn{2}{c}{结果} & \\multicolumn{2}{c}{参考区间-单位} \\\\\n[BBOX-443] \\hline\n[BBOX-444] *C反应蛋白 & \\uparrow & 11.2 & 0---6 mg/L & & & & & & & & \\\\\n[BBOX-445] *肌酸激酶 & 56 & 40---200 U/L & & & & & & & & & \\\\\n[BBOX-446] 肌酸激酶MB同工酶 & 11 & 0---25 U/L & & & & & & & & & \\\\\n[BBOX-447] *a 羟丁酸脱氢酶 & 120 & 59---126.4 U/L & & & & & & & & & \\\\\n[BBOX-448] eGFR (CKD-EPI) & \\downarrow & 69.6 & >90 ml/min/1.73m~2 & & & & & & & & \\\\\n[BBOX-449] \\hline\n[BBOX-450] \\multicolumn{8}{l}{检验意见:} \\\\\n[BBOX-451] \\hline\n[BBOX-452] \\multicolumn{4}{l}{送检医生: 杨阳} & \\multicolumn{4}{l}{检验者: 柏玉} & \\multicolumn{4}{l}{审核者: \\underline{余安光}} \\\\\n[BBOX-453] \\multicolumn{4}{l}{采集时间: 2026-03-10 09:20} & \\multicolumn{4}{l}{接收时间: 2026-03-10 09:38} & \\multicolumn{4}{l}{报告时间: 2026-03-10 12:08} \\\\\n[BBOX-454] \\multicolumn{8}{l}{本报告单结果仅对送检标本负责！如有疑问请于报告时间3日内与检验科210231联系！} & \\multicolumn{8}{l}{注: \\uparrow-偏高, \\downarrow-偏低, ★-危急值结果} \\\\\n[BBOX-455] \\multicolumn{8}{l}{项目名称前注“*”为省内互认项目} & \\multicolumn{8}{l}{} \\\\\n[BBOX-456] \\hline\n[BBOX-457] \\end{tabular}"
  }
]
2026-08-06 10:32:45,202 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1420685, prompt_len=764
2026-08-06 10:32:46,717 INFO     30 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-15"
}
```
2026-08-06 10:32:46,718 INFO     30 [qwen-vl-parser] page=47 classify=table report_date=2026-01-15
2026-08-06 10:32:46,737 INFO     30 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1420685, prompt_len=756
2026-08-06 10:32:52,493 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:32:52.490+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 8, "lag": 0, "done": 1, "failed": 0, "current": {"00b9d592918111f18dbe1f8f96f1c395": {"id": "00b9d592918111f18dbe1f8f96f1c395", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011867426, "task_type": "dataflow", "root_trace_id": "1ab3198c92574fb4b2701d0f5db7322f", "root_traceparent": "00-1ab3198c92574fb4b2701d0f5db7322f-bdaff6f64a5f4a64-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "dfc102e2918111f18dbe1f8f96f1c395": {"id": "dfc102e2918111f18dbe1f8f96f1c395", "doc_id": "de8a02fc918111f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786012241604, "task_type": "dataflow", "root_trace_id": "90f550f6b00248c3845d57a8e0bcf6fb", "root_traceparent": "00-90f550f6b00248c3845d57a8e0bcf6fb-5db7fb7d470dfe0d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:32:54,381 INFO     30 [qwen-vl-parser] table API response (len=1412):
\begin{tabular}{ccccccccc}
\hline
英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\
\hline
{[}WBC{]}白细胞数目 & 4.20 & & & 3.5~9.5 & 10^9/L & {[}HCT{]}红细胞压积 & 38.3 & & & 35~45 & \% \\
{[}Lym\%{]}淋巴细胞百分比 & 28.6 & & & 20~50 & \% & {[}MCV{]}平均红细胞体积 & 81.3 & $\downarrow$ & & 82~100 & fL \\
{[}Mon\%{]}单核细胞百分比 & 5.0 & & & 3~10 & \% & {[}MCH{]}平均红细胞血红蛋白含量 & 25.6 & $\downarrow$ & & 27~34 & pg \\
{[}Neu\%{]}中性粒细胞百分比 & 64.5 & & & 40~75 & \% & {[}MCHC{]}平均红细胞血红蛋白浓度 & 313 & $\downarrow$ & & 316~354 & g/L \\
{[}Eos\%{]}嗜酸性细胞百分比 & 1.7 & & & 0.4~8 & \% & {[}RDW-CV{]}红细胞分布宽度变异系数 & 14.9 & & & 11~16 & \% \\
{[}Bas\%{]}嗜碱性细胞百分比 & 0.2 & & & 0.0~1.0 & \% & {[}RDW-SD{]}红细胞分布宽度标准差 & 43.2 & & & 35.0~56.0 & fL \\
{[}Lym\# {]}淋巴细胞数目 & 1.20 & & & 1.1~3.2 & 10^9/L & {[}PLT{]}血小板数目 & 288 & & & 125~350 & 10^9/L \\
{[}Mon\# {]}单核细胞数目 & 0.21 & & & 0.1~0.6 & 10^9/L & {[}MPV{]}平均血小板体积 & 9.0 & & & 6.5~12 & fL \\
{[}Neu\# {]}中性粒细胞数目 & 2.71 & & & 1.8~6.3 & 10^9/L & {[}PDW{]}血小板分布宽度 & 15.6 & & & 9~17 & fL \\
{[}Eos\# {]}嗜酸性细胞数目 & 0.07 & & & 0.02~0.52 & 10^9/L & {[}PCT{]}血小板压积 & 0.258 & & & 0.108~ & \% \\
{[}Bas\# {]}嗜碱性细胞数目 & 0.01 & & & 0.00~0.06 & 10^9/L & {[}P-LCR{]}大型血小板比率 & 19.3 & & & 11~45 & \% \\
{[}RBC{]}红细胞数目 & 4.71 & & & 3.8~5.1 & 10^12/L & {[}IG\%{]}未成熟粒细胞百分比 & 0.1 & & & 0.0~0.6 & \% \\
{[}HGB{]}血红蛋白 & 120 & & & 115~150 & g/L & {[}IG\# {]}未成熟粒细胞计数 & 0.00 & & & 0.00~0.06 & 10^9/L \\
\hline
\end{tabular}
2026-08-06 10:32:54,385 INFO     30 [qwen-vl-parser] page=47 table: 20 LaTeX lines (bbox 2246-2265)
2026-08-06 10:32:54,386 INFO     30 [qwen-vl-parser] page=47 table: 20 sections
2026-08-06 10:32:54,945 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1427726, prompt_len=764
2026-08-06 10:32:56,727 INFO     30 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-15"
}
```
2026-08-06 10:32:56,728 INFO     30 [qwen-vl-parser] page=48 classify=table report_date=2026-01-15
2026-08-06 10:32:56,790 INFO     30 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1427726, prompt_len=756
2026-08-06 10:32:56,906 INFO     30 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:32:57,019 INFO     30 [SmartSplitter] SmartSplitter done: 8 chunks from 8 LLM segments (all bbox_id). Types: {'DischargeRecord': 1, 'ExaminationReport': 4, 'OutpatientRecord': 1, 'LabReport': 2}
2026-08-06 10:32:57,075 INFO     30 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-06 10:32:57,076 INFO     30 [Trace] task=dfc102e2 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "458 items", "markdown": "", "text": "", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf", "output_format": "chunks", "chunks": "8 items, types={'DischargeRecord': 1, 'ExaminationReport': 4, 'OutpatientRecord': 1, 'LabReport': 2}"}
2026-08-06 10:32:57,077 INFO     30 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-06 10:32:57,082 INFO     30 [ChunkRouter] Routed 8 chunks into 4 groups: {'chunks_Discharge': 1, 'chunks_Examination': 4, 'chunks_Clinical': 1, 'chunks_LabExam': 2}
2026-08-06 10:32:57,139 INFO     30 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-06 10:32:57,140 INFO     30 [Trace] task=dfc102e2 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | ChunkRouter:Router | outputs={"html": "", "json": "458 items", "markdown": "", "text": "", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf", "output_format": "chunks", "chunks": "8 items, types={'DischargeRecord': 1, 'ExaminationReport': 4, 'OutpatientRecord': 1, 'LabReport': 2}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 4, \"chunks_Clinical\": 1, \"chunks_LabExam\": 2}"}
2026-08-06 10:32:57,141 INFO     30 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-06 10:32:57,185 INFO     30 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 10:32:57,186 INFO     30 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[12]
2026-08-06 10:32:57,186 INFO     30 [qwen-vl-table] positions ： [[12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 10:32:57,615 INFO     30 [qwen-vl-table] page=12, rect=842x595, img=(2339x1654)
2026-08-06 10:32:57,615 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:32:57,616 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 361, \"bbox_end\": 382, \"encounter_dates\": [\"2026-03-10\"], \"department\": \"(江北)综合肿瘤中心\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{cccccc}\n报告时间: 2026-03-10\n\\hline\n\\multicolumn{2}{c}{\\textbf{检验项目}} & \\textbf{结果} & \\textbf{参考区间-单位} & \\multicolumn{2}{c}{\\textbf{检验项目}} & \\textbf{结果} & \\textbf{参考区间-单位} \\\\\n\\hline\n*白细胞计数 & & 4.2 & 3.5--9.5 10^9/L & *平均红细胞血红蛋白含量 & & 31.4 & 27--34 pg \\\\\n中性粒细胞百分数 & & 74.5 & 40--75 \\% & *平均红细胞血红蛋白浓度 & & 332 & 316--354 g/L \\\\\n淋巴细胞百分数 & & 16.1 & 20--50 \\% & 红细胞体积分布宽度 & & 13.6 & 0-14 \\% \\\\\n单核细胞百分数 & & 6.9 & 3--10 \\% & *血小板计数 & & 179 & 125--350 10^9/L \\\\\n嗜酸性粒细胞百分数 & & 1.7 & 0.4--8 \\% & & & & \\\\\n嗜碱性粒细胞百分数 & & 0.8 & 0-1 \\% & & & & \\\\\n中性粒细胞绝对值 & & 3.1 & 1.8--6.3 10^9/L & & & & \\\\\n淋巴细胞绝对值 & & 0.7 & 1.1--3.2 10^9/L & & & & \\\\\n单核细胞绝对值 & & 0.3 & 0.1--0.6 10^9/L & & & & \\\\\n嗜酸性粒细胞绝对值 & & 0.07 & 0.02--0.52 10^9/L & & & & \\\\\n嗜碱性粒细胞绝对值 & & 0.03 & 0--0.06 10^9/L & & & & \\\\\n*红细胞计数 & & 4.01 & 3.8-5.1 10^12/L & & & & \\\\\n*血红蛋白量 & & 126 & 115--150 g/L & & & & \\\\\n*红细胞压积 & & 38.0 & 35--45 \\% & & & & \\\\\n*平均红细胞体积 & & 94.7 & 82--100 fl & & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-06 10:33:09,717 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:33:09,717 INFO     30 [qwen-vl-table] page=12 LLM output (len=3347):
{
  "report_date": "2026-03-10",
  "items": [
    {
      "name": "白细胞计数",
      "item_code": "WBC",
      "value": "4.2",
      "unit": "10^9/L",
      "reference_range": "3.5--9.5 10^9/L",
      "abnormal": false
    },
    {
      "name": "中性粒细胞百分数",
      "item_code": "NEUT%",
      "value": "74.5",
      "unit": "%",
      "reference_range": "40--75 %",
      "abnormal": false
    },
    {
      "name": "淋巴细胞百分数",
      "item_code": "LYM%",
      "value": "16.1",
      "unit": "%",
      "reference_range": "20--50 %",
      "abnormal": true
    },
    {
      "name": "单核细胞百分数",
      "item_code": "MONO%",
      "value": "6.9",
      "unit": "%",
      "reference_range": "3--10 %",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞百分数",
      "item_code": "EOS%",
      "value": "1.7",
      "unit": "%",
      "reference_range": "0.4--8 %",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞百分数",
      "item_code": "BASO%",
      "value": "0.8",
      "unit": "%",
      "reference_range": "0-1 %",
      "abnormal": false
    },
    {
      "name": "中性粒细胞绝对值",
      "item_code": "NEUT#",
      "value": "3.1",
      "unit": "10^9/L",
      "reference_range": "1.8--6.3 10^9/L",
      "abnormal": false
    },
    {
      "name": "淋巴细胞绝对值",
      "item_code": "LYM#",
      "value": "0.7",
      "unit": "10^9/L",
      "reference_range": "1.1--3.2 10^9/L",
      "abnormal": true
    },
    {
      "name": "单核细胞绝对值",
      "item_code": "MONO#",
      "value": "0.3",
      "unit": "10^9/L",
      "reference_range": "0.1--0.6 10^9/L",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞绝对值",
      "item_code": "EOS#",
      "value": "0.07",
      "unit": "10^9/L",
      "reference_range": "0.02--0.52 10^9/L",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞绝对值",
      "item_code": "BASO#",
      "value": "0.03",
      "unit": "10^9/L",
      "reference_range": "0--0.06 10^9/L",
      "abnormal": false
    },
    {
      "name": "红细胞计数",
      "item_code": "RBC",
      "value": "4.01",
      "unit": "10^12/L",
      "reference_range": "3.8-5.1 10^12/L",
      "abnormal": false
    },
    {
      "name": "血红蛋白量",
      "item_code": "HGB",
      "value": "126",
      "unit": "g/L",
      "reference_range": "115--150 g/L",
      "abnormal": false
    },
    {
      "name": "红细胞压积",
      "item_code": "HCT",
      "value": "38.0",
      "unit": "%",
      "reference_range": "35--45 %",
      "abnormal": false
    },
    {
      "name": "平均红细胞体积",
      "item_code": "MCV",
      "value": "94.7",
      "unit": "fl",
      "reference_range": "82--100 fl",
      "abnormal": false
    },
    {
      "name": "平均红细胞血红蛋白含量",
      "item_code": "MCH",
      "value": "31.4",
      "unit": "pg",
      "reference_range": "27--34 pg",
      "abnormal": false
    },
    {
      "name": "平均红细胞血红蛋白浓度",
      "item_code": "MCHC",
      "value": "332",
      "unit": "g/L",
      "reference_range": "316--354 g/L",
      "abnormal": false
    },
    {
      "name": "红细胞体积分布宽度",
      "item_code": "RDW",
      "value": "13.6",
      "unit": "%",
      "reference_range": "0-14 %",
      "abnormal": false
    },
    {
      "name": "血小板计数",
      "item_code": "PLT",
      "value": "179",
      "unit": "10^9/L",
      "reference_range": "125--350 10^9/L",
      "abnormal": false
    }
  ]
}
2026-08-06 10:33:09,717 INFO     30 [qwen-vl-table] coord grouping: {12: 19}
2026-08-06 10:33:09,723 INFO     30 [qwen-vl-table] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1145232, prompt_len=668
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
白细胞计数、中性粒细胞百分数、淋巴细胞百分数、单核细胞百分数、嗜酸性粒细胞百分数、嗜碱性粒细胞百分数、中性粒细胞绝对值、淋巴细胞绝对值、单核细胞绝对值、嗜酸性粒细胞绝对值、嗜碱性粒细胞绝对值、红细胞计数、血红蛋白量、红细胞压积、平均红细胞体积、平均红细胞血红蛋白含量、平均红细胞血红蛋白浓度、红细胞体积分布宽度、血小板计数

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
2026-08-06 10:33:16,759 INFO     30 [qwen-vl-table] coord API raw response (len=1000):
[
	{"text": "白细胞计数", "bbox": [146, 331, 212, 348]},
	{"text": "中性粒细胞百分数", "bbox": [146, 354, 241, 371]},
	{"text": "淋巴细胞百分数", "bbox": [146, 377, 229, 394]},
	{"text": "单核细胞百分数", "bbox": [146, 400, 229, 417]},
	{"text": "嗜酸性粒细胞百分数", "bbox": [146, 423, 252, 440]},
	{"text": "嗜碱性粒细胞百分数", "bbox": [146, 446, 252, 463]},
	{"text": "中性粒细胞绝对值", "bbox": [146, 469, 241, 486]},
	{"text": "淋巴细胞绝对值", "bbox": [146, 492, 229, 509]},
	{"text": "单核细胞绝对值", "bbox": [146, 515, 229, 532]},
	{"text": "嗜酸性粒细胞绝对值", "bbox": [146, 538, 252, 555]},
	{"text": "嗜碱性粒细胞绝对值", "bbox": [146, 561, 252, 578]},
	{"text": "红细胞计数", "bbox": [146, 584, 212, 601]},
	{"text": "血红蛋白量", "bbox": [146, 607, 212, 624]},
	{"text": "红细胞压积", "bbox": [146, 630, 212, 647]},
	{"text": "平均红细胞体积", "bbox": [146, 653, 235, 670]},
	{"text": "平均红细胞血红蛋白含量", "bbox": [518, 331, 655, 348]},
	{"text": "平均红细胞血红蛋白浓度", "bbox": [518, 354, 655, 371]},
	{"text": "红细胞体积分布宽度", "bbox": [518, 377, 625, 394]},
	{"text": "血小板计数", "bbox": [518, 400, 585, 417]}
]
2026-08-06 10:33:16,759 INFO     30 [qwen-vl-table] coord API: raw_items=19, valid_items=19, elapsed=7.0s
2026-08-06 10:33:16,760 INFO     30 [qwen-vl-table] coord item[0]: text=白细胞计数, bbox=[146, 331, 212, 348]
2026-08-06 10:33:16,760 INFO     30 [qwen-vl-table] coord item[1]: text=中性粒细胞百分数, bbox=[146, 354, 241, 371]
2026-08-06 10:33:16,760 INFO     30 [qwen-vl-table] coord item[2]: text=淋巴细胞百分数, bbox=[146, 377, 229, 394]
2026-08-06 10:33:16,760 INFO     30 [qwen-vl-table] coord item[3]: text=单核细胞百分数, bbox=[146, 400, 229, 417]
2026-08-06 10:33:16,760 INFO     30 [qwen-vl-table] coord item[4]: text=嗜酸性粒细胞百分数, bbox=[146, 423, 252, 440]
2026-08-06 10:33:16,760 INFO     30 [qwen-vl-table] coord item[5]: text=嗜碱性粒细胞百分数, bbox=[146, 446, 252, 463]
2026-08-06 10:33:16,760 INFO     30 [qwen-vl-table] coord item[6]: text=中性粒细胞绝对值, bbox=[146, 469, 241, 486]
2026-08-06 10:33:16,760 INFO     30 [qwen-vl-table] coord item[7]: text=淋巴细胞绝对值, bbox=[146, 492, 229, 509]
2026-08-06 10:33:16,760 INFO     30 [qwen-vl-table] coord item[8]: text=单核细胞绝对值, bbox=[146, 515, 229, 532]
2026-08-06 10:33:16,760 INFO     30 [qwen-vl-table] coord item[9]: text=嗜酸性粒细胞绝对值, bbox=[146, 538, 252, 555]
2026-08-06 10:33:16,761 INFO     30 [qwen-vl-table] coord item[10]: text=嗜碱性粒细胞绝对值, bbox=[146, 561, 252, 578]
2026-08-06 10:33:16,761 INFO     30 [qwen-vl-table] coord item[11]: text=红细胞计数, bbox=[146, 584, 212, 601]
2026-08-06 10:33:16,761 INFO     30 [qwen-vl-table] coord item[12]: text=血红蛋白量, bbox=[146, 607, 212, 624]
2026-08-06 10:33:16,761 INFO     30 [qwen-vl-table] coord item[13]: text=红细胞压积, bbox=[146, 630, 212, 647]
2026-08-06 10:33:16,761 INFO     30 [qwen-vl-table] coord item[14]: text=平均红细胞体积, bbox=[146, 653, 235, 670]
2026-08-06 10:33:16,761 INFO     30 [qwen-vl-table] coord item[15]: text=平均红细胞血红蛋白含量, bbox=[518, 331, 655, 348]
2026-08-06 10:33:16,761 INFO     30 [qwen-vl-table] coord item[16]: text=平均红细胞血红蛋白浓度, bbox=[518, 354, 655, 371]
2026-08-06 10:33:16,761 INFO     30 [qwen-vl-table] coord item[17]: text=红细胞体积分布宽度, bbox=[518, 377, 625, 394]
2026-08-06 10:33:16,761 INFO     30 [qwen-vl-table] coord item[18]: text=血小板计数, bbox=[518, 400, 585, 417]
2026-08-06 10:33:16,762 INFO     30 [qwen-vl-table] page=12 coord: matched 19/19, time=7.0s
2026-08-06 10:33:16,762 INFO     30 [qwen-vl-table] new_positions (19):
[[13, 122.91594213867188, 178.48068310546876, 197.0363563232422, 207.15604833984375], [13, 122.91594213867188, 202.89549353027343, 210.72770434570313, 220.8473963623047], [13, 122.91594213867188, 192.79281335449218, 224.41905236816407, 234.53874438476564], [13, 122.91594213867188, 192.79281335449218, 238.11040039062502, 248.23009240722658], [13, 122.91594213867188, 212.15628369140626, 251.80174841308596, 261.9214404296875], [13, 122.91594213867188, 212.15628369140626, 265.4930964355469, 275.61278845214844], [13, 122.91594213867188, 202.89549353027343, 279.1844444580078, 289.3041364746094], [13, 122.91594213867188, 192.79281335449218, 292.87579248046876, 302.9954844970703], [13, 122.91594213867188, 192.79281335449218, 306.5671405029297, 316.68683251953127], [13, 122.91594213867188, 212.15628369140626, 320.25848852539065, 330.3781805419922], [13, 122.91594213867188, 212.15628369140626, 333.9498365478516, 344.06952856445315], [13, 122.91594213867188, 178.48068310546876, 347.64118457031253, 357.7608765869141], [13, 122.91594213867188, 178.48068310546876, 361.3325325927735, 371.45222460937504], [13, 122.91594213867188, 178.48068310546876, 375.0238806152344, 385.143572631836], [13, 122.91594213867188, 197.8441534423828, 388.7152286376953, 398.83492065429687], [13, 436.09902758789065, 551.4379595947265, 197.0363563232422, 207.15604833984375], [13, 436.09902758789065, 551.4379595947265, 210.72770434570313, 220.8473963623047], [13, 436.09902758789065, 526.1812591552734, 224.41905236816407, 234.53874438476564], [13, 436.09902758789065, 492.50565856933594, 238.11040039062502, 248.23009240722658]]
2026-08-06 10:33:16,763 INFO     30 [qwen-vl-table] ═══ DONE ═══ items=19, matched=19, pages=1, time=19.6s
2026-08-06 10:33:16,766 INFO     30 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 10:33:16,767 INFO     30 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[13]
2026-08-06 10:33:16,767 INFO     30 [qwen-vl-table] positions ： [[13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 10:33:17,021 INFO     30 [qwen-vl-table] page=13, rect=842x595, img=(2339x1654)
2026-08-06 10:33:17,022 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:33:17,022 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 383, \"bbox_end\": 457, \"encounter_dates\": [\"2026-03-10\"], \"department\": \"(江北)综合肿瘤中心\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllll}\n报告时间: 2026-03-10\n\\hline\n\\multicolumn{8}{c}{\\textbf{南京鼓楼医院 检验科报告单}} \\\\\n\\multicolumn{8}{c}{南京大学医学院附属鼓楼医院} \\\\\n\\multicolumn{8}{c}{苏HR} \\\\\n\\hline\n\\multicolumn{2}{l}{【住院】} & \\multicolumn{6}{l}{} \\\\\n\\multicolumn{2}{l}{第1页/共2页} & \\multicolumn{6}{l}{} \\\\\n\\hline\n\\multicolumn{2}{l}{姓 \\quad 名:} & \\multicolumn{2}{l}{病 \\quad 历 号:} & \\multicolumn{4}{l}{临床诊断: 肺恶性肿瘤} \\\\\n\\multicolumn{2}{l}{性 \\quad 别: 女} & \\multicolumn{2}{l}{科 \\quad 室: (江北) 综合肿瘤中} & \\multicolumn{4}{l}{标本种类: 血液} \\\\\n\\multicolumn{2}{l}{年 \\quad 龄: 75岁} & \\multicolumn{2}{l}{床 \\quad 号:} & \\multicolumn{4}{l}{病 \\quad 区: (江北) B7病区} \\\\\n\\multicolumn{8}{l}{申请医嘱: 生化全套, 心肌酶测定} \\\\\n\\hline\n\\multicolumn{2}{c}{检验项目} & \\multicolumn{2}{c}{结果} & \\multicolumn{2}{c}{参考区间-单位} & \\multicolumn{2}{c}{检验项目} & \\multicolumn{2}{c}{结果} & \\multicolumn{2}{c}{参考区间-单位} \\\\\n\\hline\n*丙氨酸氨基转移酶 & \\uparrow & 50.3 & 7---40 U/L & *肌酐 & 73 & 41---81 umol/L \\\\\n*天门冬氨酸氨基转移酶 & \\uparrow & 35.4 & 13---35 U/L & *尿酸 & 221 & 155---357 umol/L \\\\\n*碱性磷酸酶 & \\downarrow & 43.2 & 50---135 U/L & 总二氧化碳 & 28.1 & 21---31 mmol/L \\\\\n*γ-谷氨酰基转移酶 & \\uparrow & 130.5 & 7---45 U/L & *甘油三酯 & \\uparrow & 2.88 & $\\le$1.7 mmol/L \\\\\n*乳酸脱氢酶 & 193 & 120---250 U/L & *总胆固醇 & \\uparrow & 5.81 & 3---5.7 mmol/L \\\\\n*总胆红素 & 10.2 & $\\le$21 umol/L & *H-脂蛋白胆固醇 & 1.26 & 1.03---1.55 mmol/L \\\\\n*直接胆红素 & 3.3 & $\\le$4 umol/L & *L-脂蛋白胆固醇 & \\uparrow & 3.66 & 健康人<3.4; 不同ASCVD危 \\\\\n*胆碱酯酶 & 8.8 & 5.3---11.3 KU/L & & & & 险人群目标值: 低危<3.4 \\\\\n*总蛋白 & 78.9 & 65---85 g/L & & & & 中高危<2.6; 极高危<1.8 \\\\\n*白蛋白 & 48.8 & 40---55 g/L & & & & 超高危<1.4 mmol/L \\\\\n*球蛋白 & 30.1 & 20---40 g/L & & & & \\\\\n白/球比例 & 1.62 & 1.2---2.4 & *载脂蛋白A I & 1.30 & 1---1.6 g/L \\\\\n*总胆汁酸 & 4.0 & 0---13 umol/L & *载脂蛋白B & \\uparrow & 1.15 & 0.6---1.1 g/L \\\\\n亮氨酸氨肽酶 & 35.3 & 12---37 U/L & *总钙 & 2.46 & 2.11---2.52 mmol/L \\\\\n*腺苷脱氨酶 & 21.3 & 0---25 U/L & *磷 & 1.37 & 0.85---1.51 mmol/L \\\\\n*葡萄糖 & \\uparrow & 8.35 & 3.9---6.1 mmol/L & *钾 & 4.18 & 3.5---5.3 mmol/L \\\\\n*尿素 & 4.4 & 3.1---8.8 mmol/L & *钠 & 138.3 & 137---147 mmol/L \\\\\n& & & & *氯 & 101.7 & 99---110 mmol/L \\\\\n\\hline\n\\multicolumn{8}{l}{检验意见:} \\\\\n\\hline\n\\multicolumn{4}{l}{送检医生: 杨阳} & \\multicolumn{4}{l}{检验者: 柏玉} & \\multicolumn{4}{l}{审核者: \\underline{余安光}} \\\\\n\\multicolumn{4}{l}{采集时间: 2026-03-10 09:20} & \\multicolumn{4}{l}{接收时间: 2026-03-10 09:38} & \\multicolumn{4}{l}{报告时间: 2026-03-10 12:08} \\\\\n\\multicolumn{8}{l}{本报告单结果仅对送检标本负责！如有疑问请于报告时间3日内与检验科210231联系！} & \\multicolumn{8}{l}{注: \\uparrow-偏高, \\downarrow-偏低, ★-危急值结果} \\\\\n\\multicolumn{8}{l}{项目名称前注“*”为省内互认项目} & \\multicolumn{8}{l}{} \\\\\n\\hline\n\\end{tabular}\n\\begin{tabular}{llllllll}\n报告时间: 2026-03-10\n\\hline\n\\multicolumn{8}{c}{\\textbf{南京鼓楼医院 检验科报告单}} \\\\\n\\multicolumn{8}{c}{南京大学医学院附属鼓楼医院} \\\\\n\\multicolumn{8}{c}{苏HR} \\\\\n\\hline\n\\multicolumn{2}{l}{【住院】} & \\multicolumn{6}{l}{} \\\\\n\\multicolumn{2}{l}{第2页/共2页} & \\multicolumn{6}{l}{} \\\\\n\\hline\n\\multicolumn{2}{l}{姓 \\quad 名:} & \\multicolumn{2}{l}{病 \\quad 历 号:} & \\multicolumn{4}{l}{临床诊断: 肺恶性肿瘤} \\\\\n\\multicolumn{2}{l}{性 \\quad 别: 女} & \\multicolumn{2}{l}{科 \\quad 室: (江北) 综合肿瘤中} & \\multicolumn{4}{l}{标本种类: 血液} \\\\\n\\multicolumn{2}{l}{年 \\quad 龄: 75岁} & \\multicolumn{2}{l}{床 \\quad 号:} & \\multicolumn{4}{l}{病 \\quad 区: (江北) B7病区} \\\\\n\\multicolumn{8}{l}{申请医嘱: 生化全套, 心肌酶测定} \\\\\n\\hline\n\\multicolumn{2}{c}{检验项目} & \\multicolumn{2}{c}{结果} & \\multicolumn{2}{c}{参考区间-单位} & \\multicolumn{2}{c}{检验项目} & \\multicolumn{2}{c}{结果} & \\multicolumn{2}{c}{参考区间-单位} \\\\\n\\hline\n*C反应蛋白 & \\uparrow & 11.2 & 0---6 mg/L & & & & & & & & \\\\\n*肌酸激酶 & 56 & 40---200 U/L & & & & & & & & & \\\\\n肌酸激酶MB同工酶 & 11 & 0---25 U/L & & & & & & & & & \\\\\n*a 羟丁酸脱氢酶 & 120 & 59---126.4 U/L & & & & & & & & & \\\\\neGFR (CKD-EPI) & \\downarrow & 69.6 & >90 ml/min/1.73m~2 & & & & & & & & \\\\\n\\hline\n\\multicolumn{8}{l}{检验意见:} \\\\\n\\hline\n\\multicolumn{4}{l}{送检医生: 杨阳} & \\multicolumn{4}{l}{检验者: 柏玉} & \\multicolumn{4}{l}{审核者: \\underline{余安光}} \\\\\n\\multicolumn{4}{l}{采集时间: 2026-03-10 09:20} & \\multicolumn{4}{l}{接收时间: 2026-03-10 09:38} & \\multicolumn{4}{l}{报告时间: 2026-03-10 12:08} \\\\\n\\multicolumn{8}{l}{本报告单结果仅对送检标本负责！如有疑问请于报告时间3日内与检验科210231联系！} & \\multicolumn{8}{l}{注: \\uparrow-偏高, \\downarrow-偏低, ★-危急值结果} \\\\\n\\multicolumn{8}{l}{项目名称前注“*”为省内互认项目} & \\multicolumn{8}{l}{} \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-06 10:33:22,730 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:33:22.727+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 8, "lag": 0, "done": 1, "failed": 0, "current": {"00b9d592918111f18dbe1f8f96f1c395": {"id": "00b9d592918111f18dbe1f8f96f1c395", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011867426, "task_type": "dataflow", "root_trace_id": "1ab3198c92574fb4b2701d0f5db7322f", "root_traceparent": "00-1ab3198c92574fb4b2701d0f5db7322f-bdaff6f64a5f4a64-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "dfc102e2918111f18dbe1f8f96f1c395": {"id": "dfc102e2918111f18dbe1f8f96f1c395", "doc_id": "de8a02fc918111f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786012241604, "task_type": "dataflow", "root_trace_id": "90f550f6b00248c3845d57a8e0bcf6fb", "root_traceparent": "00-90f550f6b00248c3845d57a8e0bcf6fb-5db7fb7d470dfe0d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:33:41,246 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:33:41,247 INFO     30 [qwen-vl-table] page=13 LLM output (len=6336):
{
  "report_date": "2026-03-10",
  "items": [
    {
      "name": "丙氨酸氨基转移酶",
      "item_code": "ALT",
      "value": "50.3",
      "unit": "U/L",
      "reference_range": "7---40 U/L",
      "abnormal": true
    },
    {
      "name": "天门冬氨酸氨基转移酶",
      "item_code": "AST",
      "value": "35.4",
      "unit": "U/L",
      "reference_range": "13---35 U/L",
      "abnormal": true
    },
    {
      "name": "碱性磷酸酶",
      "item_code": "ALP",
      "value": "43.2",
      "unit": "U/L",
      "reference_range": "50---135 U/L",
      "abnormal": true
    },
    {
      "name": "γ-谷氨酰基转移酶",
      "item_code": "GGT",
      "value": "130.5",
      "unit": "U/L",
      "reference_range": "7---45 U/L",
      "abnormal": true
    },
    {
      "name": "乳酸脱氢酶",
      "item_code": "LDH",
      "value": "193",
      "unit": "U/L",
      "reference_range": "120---250 U/L",
      "abnormal": false
    },
    {
      "name": "总胆红素",
      "item_code": "TBIL",
      "value": "10.2",
      "unit": "umol/L",
      "reference_range": "≤21 umol/L",
      "abnormal": false
    },
    {
      "name": "直接胆红素",
      "item_code": "DBIL",
      "value": "3.3",
      "unit": "umol/L",
      "reference_range": "≤4 umol/L",
      "abnormal": false
    },
    {
      "name": "胆碱酯酶",
      "item_code": "CHE",
      "value": "8.8",
      "unit": "KU/L",
      "reference_range": "5.3---11.3 KU/L",
      "abnormal": false
    },
    {
      "name": "总蛋白",
      "item_code": "TP",
      "value": "78.9",
      "unit": "g/L",
      "reference_range": "65---85 g/L",
      "abnormal": false
    },
    {
      "name": "白蛋白",
      "item_code": "ALB",
      "value": "48.8",
      "unit": "g/L",
      "reference_range": "40---55 g/L",
      "abnormal": false
    },
    {
      "name": "球蛋白",
      "item_code": "GLB",
      "value": "30.1",
      "unit": "g/L",
      "reference_range": "20---40 g/L",
      "abnormal": false
    },
    {
      "name": "白/球比例",
      "item_code": "A/G",
      "value": "1.62",
      "unit": null,
      "reference_range": "1.2---2.4",
      "abnormal": false
    },
    {
      "name": "总胆汁酸",
      "item_code": "TBA",
      "value": "4.0",
      "unit": "umol/L",
      "reference_range": "0---13 umol/L",
      "abnormal": false
    },
    {
      "name": "亮氨酸氨肽酶",
      "item_code": "LAP",
      "value": "35.3",
      "unit": "U/L",
      "reference_range": "12---37 U/L",
      "abnormal": false
    },
    {
      "name": "腺苷脱氨酶",
      "item_code": "ADA",
      "value": "21.3",
      "unit": "U/L",
      "reference_range": "0---25 U/L",
      "abnormal": false
    },
    {
      "name": "葡萄糖",
      "item_code": "GLU",
      "value": "8.35",
      "unit": "mmol/L",
      "reference_range": "3.9---6.1 mmol/L",
      "abnormal": true
    },
    {
      "name": "尿素",
      "item_code": "UREA",
      "value": "4.4",
      "unit": "mmol/L",
      "reference_range": "3.1---8.8 mmol/L",
      "abnormal": false
    },
    {
      "name": "肌酐",
      "item_code": "CREA",
      "value": "73",
      "unit": "umol/L",
      "reference_range": "41---81 umol/L",
      "abnormal": false
    },
    {
      "name": "尿酸",
      "item_code": "UA",
      "value": "221",
      "unit": "umol/L",
      "reference_range": "155---357 umol/L",
      "abnormal": false
    },
    {
      "name": "总二氧化碳",
      "item_code": "TCO2",
      "value": "28.1",
      "unit": "mmol/L",
      "reference_range": "21---31 mmol/L",
      "abnormal": false
    },
    {
      "name": "甘油三酯",
      "item_code": "TG",
      "value": "2.88",
      "unit": "mmol/L",
      "reference_range": "≤1.7 mmol/L",
      "abnormal": true
    },
    {
      "name": "总胆固醇",
      "item_code": "TC",
      "value": "5.81",
      "unit": "mmol/L",
      "reference_range": "3---5.7 mmol/L",
      "abnormal": true
    },
    {
      "name": "H-脂蛋白胆固醇",
      "item_code": "HDL-C",
      "value": "1.26",
      "unit": "mmol/L",
      "reference_range": "1.03---1.55 mmol/L",
      "abnormal": false
    },
    {
      "name": "L-脂蛋白胆固醇",
      "item_code": "LDL-C",
      "value": "3.66",
      "unit": "mmol/L",
      "reference_range": "健康人<3.4; 不同ASCVD危险人群目标值: 低危<3.4 中高危<2.6; 极高危<1.8 超高危<1.4 mmol/L",
      "abnormal": true
    },
    {
      "name": "载脂蛋白A I",
      "item_code": "ApoA1",
      "value": "1.30",
      "unit": "g/L",
      "reference_range": "1---1.6 g/L",
      "abnormal": false
    },
    {
      "name": "载脂蛋白B",
      "item_code": "ApoB",
      "value": "1.15",
      "unit": "g/L",
      "reference_range": "0.6---1.1 g/L",
      "abnormal": true
    },
    {
      "name": "总钙",
      "item_code": "Ca",
      "value": "2.46",
      "unit": "mmol/L",
      "reference_range": "2.11---2.52 mmol/L",
      "abnormal": false
    },
    {
      "name": "磷",
      "item_code": "P",
      "value": "1.37",
      "unit": "mmol/L",
      "reference_range": "0.85---1.51 mmol/L",
      "abnormal": false
    },
    {
      "name": "钾",
      "item_code": "K",
      "value": "4.18",
      "unit": "mmol/L",
      "reference_range": "3.5---5.3 mmol/L",
      "abnormal": false
    },
    {
      "name": "钠",
      "item_code": "Na",
      "value": "138.3",
      "unit": "mmol/L",
      "reference_range": "137---147 mmol/L",
      "abnormal": false
    },
    {
      "name": "氯",
      "item_code": "Cl",
      "value": "101.7",
      "unit": "mmol/L",
      "reference_range": "99---110 mmol/L",
      "abnormal": false
    },
    {
      "name": "C反应蛋白",
      "item_code": "CRP",
      "value": "11.2",
      "unit": "mg/L",
      "reference_range": "0---6 mg/L",
      "abnormal": true
    },
    {
      "name": "肌酸激酶",
      "item_code": "CK",
      "value": "56",
      "unit": "U/L",
      "reference_range": "40---200 U/L",
      "abnormal": false
    },
    {
      "name": "肌酸激酶MB同工酶",
      "item_code": "CK-MB",
      "value": "11",
      "unit": "U/L",
      "reference_range": "0---25 U/L",
      "abnormal": false
    },
    {
      "name": "α-羟丁酸脱氢酶",
      "item_code": "α-HBDH",
      "value": "120",
      "unit": "U/L",
      "reference_range": "59---126.4 U/L",
      "abnormal": false
    },
    {
      "name": "eGFR (CKD-EPI)",
      "item_code": "eGFR",
      "value": "69.6",
      "unit": "ml/min/1.73m~2",
      "reference_range": ">90 ml/min/1.73m~2",
      "abnormal": true
    }
  ]
}
2026-08-06 10:33:41,248 INFO     30 [qwen-vl-table] coord grouping: {13: 36}
2026-08-06 10:33:41,255 INFO     30 [qwen-vl-table] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=822902, prompt_len=717
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
丙氨酸氨基转移酶、天门冬氨酸氨基转移酶、碱性磷酸酶、γ-谷氨酰基转移酶、乳酸脱氢酶、总胆红素、直接胆红素、胆碱酯酶、总蛋白、白蛋白、球蛋白、白/球比例、总胆汁酸、亮氨酸氨肽酶、腺苷脱氨酶、葡萄糖、尿素、肌酐、尿酸、总二氧化碳、甘油三酯、总胆固醇、H-脂蛋白胆固醇、L-脂蛋白胆固醇、载脂蛋白A I、载脂蛋白B、总钙、磷、钾、钠、氯、C反应蛋白、肌酸激酶、肌酸激酶MB同工酶、α-羟丁酸脱氢酶、eGFR (CKD-EPI)

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
2026-08-06 10:33:53,102 INFO     30 [qwen-vl-table] coord API raw response (len=1797):
[
	{"text": "丙氨酸氨基转移酶", "bbox": [305, 187, 360, 196]},
	{"text": "天门冬氨酸氨基转移酶", "bbox": [305, 199, 373, 208]},
	{"text": "碱性磷酸酶", "bbox": [305, 211, 342, 220]},
	{"text": "γ-谷氨酰基转移酶", "bbox": [305, 224, 364, 233]},
	{"text": "乳酸脱氢酶", "bbox": [305, 237, 342, 246]},
	{"text": "总胆红素", "bbox": [305, 249, 337, 258]},
	{"text": "直接胆红素", "bbox": [305, 262, 340, 271]},
	{"text": "胆碱酯酶", "bbox": [305, 275, 335, 284]},
	{"text": "总蛋白", "bbox": [305, 287, 328, 296]},
	{"text": "白蛋白", "bbox": [305, 300, 328, 309]},
	{"text": "球蛋白", "bbox": [305, 313, 328, 322]},
	{"text": "白/球比例", "bbox": [305, 326, 336, 335]},
	{"text": "总胆汁酸", "bbox": [305, 339, 336, 348]},
	{"text": "亮氨酸氨肽酶", "bbox": [305, 352, 344, 361]},
	{"text": "腺苷脱氨酶", "bbox": [305, 365, 342, 374]},
	{"text": "葡萄糖", "bbox": [305, 378, 328, 387]},
	{"text": "尿素", "bbox": [305, 390, 322, 399]},
	{"text": "肌酐", "bbox": [510, 187, 526, 196]},
	{"text": "尿酸", "bbox": [510, 200, 526, 209]},
	{"text": "总二氧化碳", "bbox": [510, 212, 542, 221]},
	{"text": "甘油三酯", "bbox": [510, 225, 538, 234]},
	{"text": "总胆固醇", "bbox": [510, 238, 538, 247]},
	{"text": "H-脂蛋白胆固醇", "bbox": [510, 250, 559, 259]},
	{"text": "L-脂蛋白胆固醇", "bbox": [510, 263, 559, 272]},
	{"text": "载脂蛋白A I", "bbox": [510, 317, 548, 326]},
	{"text": "载脂蛋白B", "bbox": [510, 330, 544, 339]},
	{"text": "总钙", "bbox": [510, 343, 526, 352]},
	{"text": "磷", "bbox": [510, 356, 520, 365]},
	{"text": "钾", "bbox": [510, 369, 520, 378]},
	{"text": "钠", "bbox": [510, 381, 520, 390]},
	{"text": "氯", "bbox": [510, 394, 520, 403]},
	{"text": "C反应蛋白", "bbox": [305, 612, 337, 621]},
	{"text": "肌酸激酶", "bbox": [305, 625, 335, 634]},
	{"text": "肌酸激酶MB同工酶", "bbox": [305, 638, 358, 647]},
	{"text": "α-羟丁酸脱氢酶", "bbox": [305, 651, 354, 660]},
	{"text": "eGFR (CKD-EPI)", "bbox": [305, 664, 347, 673]}
]
2026-08-06 10:33:53,102 INFO     30 [qwen-vl-table] coord API: raw_items=36, valid_items=36, elapsed=11.8s
2026-08-06 10:33:53,103 INFO     30 [qwen-vl-table] coord item[0]: text=丙氨酸氨基转移酶, bbox=[305, 187, 360, 196]
2026-08-06 10:33:53,103 INFO     30 [qwen-vl-table] coord item[1]: text=天门冬氨酸氨基转移酶, bbox=[305, 199, 373, 208]
2026-08-06 10:33:53,103 INFO     30 [qwen-vl-table] coord item[2]: text=碱性磷酸酶, bbox=[305, 211, 342, 220]
2026-08-06 10:33:53,103 INFO     30 [qwen-vl-table] coord item[3]: text=γ-谷氨酰基转移酶, bbox=[305, 224, 364, 233]
2026-08-06 10:33:53,103 INFO     30 [qwen-vl-table] coord item[4]: text=乳酸脱氢酶, bbox=[305, 237, 342, 246]
2026-08-06 10:33:53,103 INFO     30 [qwen-vl-table] coord item[5]: text=总胆红素, bbox=[305, 249, 337, 258]
2026-08-06 10:33:53,104 INFO     30 [qwen-vl-table] coord item[6]: text=直接胆红素, bbox=[305, 262, 340, 271]
2026-08-06 10:33:53,104 INFO     30 [qwen-vl-table] coord item[7]: text=胆碱酯酶, bbox=[305, 275, 335, 284]
2026-08-06 10:33:53,104 INFO     30 [qwen-vl-table] coord item[8]: text=总蛋白, bbox=[305, 287, 328, 296]
2026-08-06 10:33:53,104 INFO     30 [qwen-vl-table] coord item[9]: text=白蛋白, bbox=[305, 300, 328, 309]
2026-08-06 10:33:53,104 INFO     30 [qwen-vl-table] coord item[10]: text=球蛋白, bbox=[305, 313, 328, 322]
2026-08-06 10:33:53,104 INFO     30 [qwen-vl-table] coord item[11]: text=白/球比例, bbox=[305, 326, 336, 335]
2026-08-06 10:33:53,104 INFO     30 [qwen-vl-table] coord item[12]: text=总胆汁酸, bbox=[305, 339, 336, 348]
2026-08-06 10:33:53,105 INFO     30 [qwen-vl-table] coord item[13]: text=亮氨酸氨肽酶, bbox=[305, 352, 344, 361]
2026-08-06 10:33:53,105 INFO     30 [qwen-vl-table] coord item[14]: text=腺苷脱氨酶, bbox=[305, 365, 342, 374]
2026-08-06 10:33:53,105 INFO     30 [qwen-vl-table] coord item[15]: text=葡萄糖, bbox=[305, 378, 328, 387]
2026-08-06 10:33:53,105 INFO     30 [qwen-vl-table] coord item[16]: text=尿素, bbox=[305, 390, 322, 399]
2026-08-06 10:33:53,105 INFO     30 [qwen-vl-table] coord item[17]: text=肌酐, bbox=[510, 187, 526, 196]
2026-08-06 10:33:53,105 INFO     30 [qwen-vl-table] coord item[18]: text=尿酸, bbox=[510, 200, 526, 209]
2026-08-06 10:33:53,105 INFO     30 [qwen-vl-table] coord item[19]: text=总二氧化碳, bbox=[510, 212, 542, 221]
2026-08-06 10:33:53,105 INFO     30 [qwen-vl-table] coord item[20]: text=甘油三酯, bbox=[510, 225, 538, 234]
2026-08-06 10:33:53,105 INFO     30 [qwen-vl-table] coord item[21]: text=总胆固醇, bbox=[510, 238, 538, 247]
2026-08-06 10:33:53,105 INFO     30 [qwen-vl-table] coord item[22]: text=H-脂蛋白胆固醇, bbox=[510, 250, 559, 259]
2026-08-06 10:33:53,105 INFO     30 [qwen-vl-table] coord item[23]: text=L-脂蛋白胆固醇, bbox=[510, 263, 559, 272]
2026-08-06 10:33:53,105 INFO     30 [qwen-vl-table] coord item[24]: text=载脂蛋白A I, bbox=[510, 317, 548, 326]
2026-08-06 10:33:53,105 INFO     30 [qwen-vl-table] coord item[25]: text=载脂蛋白B, bbox=[510, 330, 544, 339]
2026-08-06 10:33:53,105 INFO     30 [qwen-vl-table] coord item[26]: text=总钙, bbox=[510, 343, 526, 352]
2026-08-06 10:33:53,105 INFO     30 [qwen-vl-table] coord item[27]: text=磷, bbox=[510, 356, 520, 365]
2026-08-06 10:33:53,105 INFO     30 [qwen-vl-table] coord item[28]: text=钾, bbox=[510, 369, 520, 378]
2026-08-06 10:33:53,105 INFO     30 [qwen-vl-table] coord item[29]: text=钠, bbox=[510, 381, 520, 390]
2026-08-06 10:33:53,105 INFO     30 [qwen-vl-table] coord item[30]: text=氯, bbox=[510, 394, 520, 403]
2026-08-06 10:33:53,105 INFO     30 [qwen-vl-table] coord item[31]: text=C反应蛋白, bbox=[305, 612, 337, 621]
2026-08-06 10:33:53,106 INFO     30 [qwen-vl-table] coord item[32]: text=肌酸激酶, bbox=[305, 625, 335, 634]
2026-08-06 10:33:53,106 INFO     30 [qwen-vl-table] coord item[33]: text=肌酸激酶MB同工酶, bbox=[305, 638, 358, 647]
2026-08-06 10:33:53,106 INFO     30 [qwen-vl-table] coord item[34]: text=α-羟丁酸脱氢酶, bbox=[305, 651, 354, 660]
2026-08-06 10:33:53,106 INFO     30 [qwen-vl-table] coord item[35]: text=eGFR (CKD-EPI), bbox=[305, 664, 347, 673]
2026-08-06 10:33:53,106 INFO     30 [qwen-vl-table] page=13 coord: matched 36/36, time=11.8s
2026-08-06 10:33:53,106 INFO     30 [qwen-vl-table] new_positions (36):
[[14, 256.7764544677734, 303.0804052734375, 111.31661218261719, 116.67409619140625], [14, 256.7764544677734, 314.0249754638672, 118.45992419433594, 123.81740820312501], [14, 256.7764544677734, 287.9263850097656, 125.60323620605469, 130.96072021484375], [14, 256.7764544677734, 306.44796533203123, 133.34182421875, 138.69930822753906], [14, 256.7764544677734, 287.9263850097656, 141.0804122314453, 146.43789624023438], [14, 256.7764544677734, 283.71693493652344, 148.22372424316407, 153.58120825195314], [14, 256.7764544677734, 286.24260498046874, 155.9623122558594, 161.31979626464843], [14, 256.7764544677734, 282.03315490722656, 163.7009002685547, 169.05838427734375], [14, 256.7764544677734, 276.1399248046875, 170.84421228027344, 176.2016962890625], [14, 256.7764544677734, 276.1399248046875, 178.58280029296876, 183.94028430175783], [14, 256.7764544677734, 276.1399248046875, 186.32138830566407, 191.67887231445314], [14, 256.7764544677734, 282.875044921875, 194.0599763183594, 199.41746032714843], [14, 256.7764544677734, 282.875044921875, 201.7985643310547, 207.15604833984375], [14, 256.7764544677734, 289.6101650390625, 209.53715234375, 214.89463635253907], [14, 256.7764544677734, 287.9263850097656, 217.2757403564453, 222.63322436523438], [14, 256.7764544677734, 276.1399248046875, 225.01432836914063, 230.3718123779297], [14, 256.7764544677734, 271.08858471679684, 232.1576403808594, 237.51512438964843], [14, 429.3639074707031, 442.8341477050781, 111.31661218261719, 116.67409619140625], [14, 429.3639074707031, 442.8341477050781, 119.05520019531251, 124.41268420410157], [14, 429.3639074707031, 456.30438793945314, 126.19851220703126, 131.55599621582033], [14, 429.3639074707031, 452.93682788085937, 133.93710021972657, 139.29458422851562], [14, 429.3639074707031, 452.93682788085937, 141.6756882324219, 147.03317224121093], [14, 429.3639074707031, 470.61651818847656, 148.81900024414062, 154.1764842529297], [14, 429.3639074707031, 470.61651818847656, 156.55758825683594, 161.915072265625], [14, 429.3639074707031, 461.35572802734373, 188.70249230957032, 194.0599763183594], [14, 429.3639074707031, 457.98816796875, 196.44108032226563, 201.7985643310547], [14, 429.3639074707031, 442.8341477050781, 204.17966833496095, 209.53715234375], [14, 429.3639074707031, 437.7828076171875, 211.91825634765627, 217.2757403564453], [14, 429.3639074707031, 437.7828076171875, 219.65684436035158, 225.01432836914063], [14, 429.3639074707031, 437.7828076171875, 226.80015637207032, 232.1576403808594], [14, 429.3639074707031, 437.7828076171875, 234.53874438476564, 239.8962283935547], [14, 256.7764544677734, 283.71693493652344, 364.3089125976563, 369.66639660644535], [14, 256.7764544677734, 282.03315490722656, 372.04750061035156, 377.40498461914063], [14, 256.7764544677734, 301.39662524414064, 379.7860886230469, 385.143572631836], [14, 256.7764544677734, 298.02906518554687, 387.5246766357422, 392.88216064453127], [14, 256.7764544677734, 292.1358350830078, 395.26326464843754, 400.62074865722656]]
2026-08-06 10:33:53,107 INFO     30 [qwen-vl-table] ═══ DONE ═══ items=36, matched=36, pages=1, time=36.3s
2026-08-06 10:33:53,127 INFO     30 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-06 10:33:53,127 INFO     30 [Trace] task=dfc102e2 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | Extractor:LabExam | outputs={"chunks": "2 items, types={'LabReport': 2}", "html": "", "json": "458 items", "markdown": "", "text": "", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 4, \"chunks_Clinical\": 1, \"chunks_LabExam\": 2}"}
2026-08-06 10:33:53,127 INFO     30 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-06 10:33:53,129 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:33:53.127+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 8, "lag": 0, "done": 1, "failed": 0, "current": {"00b9d592918111f18dbe1f8f96f1c395": {"id": "00b9d592918111f18dbe1f8f96f1c395", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011867426, "task_type": "dataflow", "root_trace_id": "1ab3198c92574fb4b2701d0f5db7322f", "root_traceparent": "00-1ab3198c92574fb4b2701d0f5db7322f-bdaff6f64a5f4a64-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "dfc102e2918111f18dbe1f8f96f1c395": {"id": "dfc102e2918111f18dbe1f8f96f1c395", "doc_id": "de8a02fc918111f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786012241604, "task_type": "dataflow", "root_trace_id": "90f550f6b00248c3845d57a8e0bcf6fb", "root_traceparent": "00-90f550f6b00248c3845d57a8e0bcf6fb-5db7fb7d470dfe0d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:33:53,148 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:33:53,148 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-06 10:33:54,250 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:33:54,273 INFO     30 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-06 10:33:54,275 INFO     30 [Trace] task=dfc102e2 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "458 items", "markdown": "", "text": "", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 4, \"chunks_Clinical\": 1, \"chunks_LabExam\": 2}"}
2026-08-06 10:33:54,275 INFO     30 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-06 10:33:54,300 INFO     30 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 10:33:54,300 INFO     30 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-06 10:33:54,300 INFO     30 [qwen-vl-text] positions(28): [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 10:33:54,301 INFO     30 [qwen-vl-text] page grouping: [11], lines per page: [28]
2026-08-06 10:33:54,795 INFO     30 [qwen-vl-text] page=11, rect=842x595, img=(2339x1654), dpi=200
2026-08-06 10:33:54,797 INFO     30 [qwen-vl-text] LLM extraction start, text_len=224
2026-08-06 10:33:54,798 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:33:54,799 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 333, \"bbox_end\": 360, \"encounter_dates\": [\"2026-03-16\"], \"department\": \"(江北)心血管内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "南京鼓楼医院\n南京大学医学院附属鼓楼医院\n互联网医院\n门诊病历\n姓名:\n性别:女\n年龄:75岁\nID:\n2026年03月16日15时20分 (江北)心血管内科门诊\n主诉:要求进行心功能分级\n病史:患者平时正常活动不受限。\n过敏史:无吸烟史\n药物过敏史。无流行病学史\n体查:\n级)\n诊断:\n1.心功能I级(NYHA分\n2.高脂血症\n处理:随诊\n1.非诺贝特胶囊(力平之)\n200mg/粒\n用法:1粒\n口服\n一次/日\nx3盒 28天\n医师:\n齐\n第1页",
    "role": "user"
  }
]
2026-08-06 10:33:56,697 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:33:56,697 INFO     30 [qwen-vl-text] LLM output (len=255):
{
  "encounter_date": "2026-03-16",
  "chief_complaint": "要求进行心功能分级",
  "present_illness": "患者平时正常活动不受限。",
  "past_history": "无吸烟史,无药物过敏史,无流行病学史",
  "diagnosis": "1.心功能I级(NYHA分级) 2.高脂血症",
  "treatment_plan": "1.非诺贝特胶囊(力平之) 200mg 口服 1粒 一次/日 x3盒 28天 2.随诊"
}
2026-08-06 10:33:56,698 INFO     30 [qwen-vl-text] Updated encounter_dates=[2026-03-16]
2026-08-06 10:33:56,702 INFO     30 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=808447, prompt_len=921
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共28行）
["南京鼓楼医院", "南京大学医学院附属鼓楼医院", "互联网医院", "门诊病历", "姓名:", "性别:女", "年龄:75岁", "ID:", "2026年03月16日15时20分 (江北)心血管内科门诊", "主诉:要求进行心功能分级", "病史:患者平时正常活动不受限。", "过敏史:无吸烟史", "药物过敏史。无流行病学史", "体查:", "级)", "诊断:", "1.心功能I级(NYHA分", "2.高脂血症", "处理:随诊", "1.非诺贝特胶囊(力平之)", "200mg/粒", "用法:1粒", "口服", "一次/日", "x3盒 28天", "医师:", "齐", "第1页"]

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
2026-08-06 10:34:06,649 INFO     30 [qwen-vl-text] coord API raw response (len=1459):
[
	{"text": "南京鼓楼医院", "bbox": [444, 203, 579, 236]},
	{"text": "南京大学医学院附属鼓楼医院", "bbox": [408, 227, 613, 266]},
	{"text": "互联网医院", "bbox": [336, 261, 388, 280]},
	{"text": "门诊病历", "bbox": [470, 261, 550, 293]},
	{"text": "姓名:", "bbox": [331, 287, 360, 305]},
	{"text": "性别:女", "bbox": [424, 294, 463, 312]},
	{"text": "年龄:75岁", "bbox": [509, 300, 553, 318]},
	{"text": "ID:", "bbox": [593, 308, 608, 323]},
	{"text": "2026年03月16日15时20分 (江北)心血管内科门诊", "bbox": [328, 317, 556, 348]},
	{"text": "主诉:要求进行心功能分级", "bbox": [328, 349, 453, 370]},
	{"text": "病史:患者平时正常活动不受限。", "bbox": [327, 378, 478, 400]},
	{"text": "过敏史:无吸烟史", "bbox": [326, 408, 413, 426]},
	{"text": "药物过敏史。无流行病学史", "bbox": [367, 434, 497, 456]},
	{"text": "体查:", "bbox": [324, 463, 350, 478]},
	{"text": "级)", "bbox": [322, 514, 338, 529]},
	{"text": "诊断:", "bbox": [489, 500, 514, 514]},
	{"text": "1.心功能I级(NYHA分", "bbox": [568, 503, 666, 521]},
	{"text": "2.高脂血症", "bbox": [566, 553, 624, 569]},
	{"text": "处理:随诊", "bbox": [321, 569, 371, 584]},
	{"text": "1.非诺贝特胶囊(力平之)", "bbox": [340, 624, 468, 645]},
	{"text": "200mg/粒", "bbox": [485, 631, 527, 648]},
	{"text": "用法:1粒", "bbox": [371, 652, 416, 669]},
	{"text": "口服", "bbox": [442, 655, 464, 670]},
	{"text": "一次/日", "bbox": [489, 657, 527, 673]},
	{"text": "x3盒 28天", "bbox": [548, 660, 595, 675]},
	{"text": "医师:", "bbox": [512, 714, 536, 728]},
	{"text": "齐", "bbox": [580, 706, 620, 731]},
	{"text": "第1页", "bbox": [470, 909, 509, 926]}
]
2026-08-06 10:34:06,649 INFO     30 [qwen-vl-text] coord API: raw_items=28, valid_items=28, elapsed=9.9s
2026-08-06 10:34:06,649 INFO     30 [qwen-vl-text] coord item[0]: text=南京鼓楼医院, bbox=[444, 203, 579, 236]
2026-08-06 10:34:06,649 INFO     30 [qwen-vl-text] coord item[1]: text=南京大学医学院附属鼓楼医院, bbox=[408, 227, 613, 266]
2026-08-06 10:34:06,649 INFO     30 [qwen-vl-text] coord item[2]: text=互联网医院, bbox=[336, 261, 388, 280]
2026-08-06 10:34:06,649 INFO     30 [qwen-vl-text] coord item[3]: text=门诊病历, bbox=[470, 261, 550, 293]
2026-08-06 10:34:06,649 INFO     30 [qwen-vl-text] coord item[4]: text=姓名:, bbox=[331, 287, 360, 305]
2026-08-06 10:34:06,649 INFO     30 [qwen-vl-text] coord item[5]: text=性别:女, bbox=[424, 294, 463, 312]
2026-08-06 10:34:06,649 INFO     30 [qwen-vl-text] coord item[6]: text=年龄:75岁, bbox=[509, 300, 553, 318]
2026-08-06 10:34:06,649 INFO     30 [qwen-vl-text] coord item[7]: text=ID:, bbox=[593, 308, 608, 323]
2026-08-06 10:34:06,649 INFO     30 [qwen-vl-text] coord item[8]: text=2026年03月16日15时20分 (江北)心血管内科门诊, bbox=[328, 317, 556, 348]
2026-08-06 10:34:06,650 INFO     30 [qwen-vl-text] coord item[9]: text=主诉:要求进行心功能分级, bbox=[328, 349, 453, 370]
2026-08-06 10:34:06,650 INFO     30 [qwen-vl-text] coord item[10]: text=病史:患者平时正常活动不受限。, bbox=[327, 378, 478, 400]
2026-08-06 10:34:06,650 INFO     30 [qwen-vl-text] coord item[11]: text=过敏史:无吸烟史, bbox=[326, 408, 413, 426]
2026-08-06 10:34:06,651 INFO     30 [qwen-vl-text] coord item[12]: text=药物过敏史。无流行病学史, bbox=[367, 434, 497, 456]
2026-08-06 10:34:06,651 INFO     30 [qwen-vl-text] coord item[13]: text=体查:, bbox=[324, 463, 350, 478]
2026-08-06 10:34:06,651 INFO     30 [qwen-vl-text] coord item[14]: text=级), bbox=[322, 514, 338, 529]
2026-08-06 10:34:06,651 INFO     30 [qwen-vl-text] coord item[15]: text=诊断:, bbox=[489, 500, 514, 514]
2026-08-06 10:34:06,651 INFO     30 [qwen-vl-text] coord item[16]: text=1.心功能I级(NYHA分, bbox=[568, 503, 666, 521]
2026-08-06 10:34:06,651 INFO     30 [qwen-vl-text] coord item[17]: text=2.高脂血症, bbox=[566, 553, 624, 569]
2026-08-06 10:34:06,651 INFO     30 [qwen-vl-text] coord item[18]: text=处理:随诊, bbox=[321, 569, 371, 584]
2026-08-06 10:34:06,651 INFO     30 [qwen-vl-text] coord item[19]: text=1.非诺贝特胶囊(力平之), bbox=[340, 624, 468, 645]
2026-08-06 10:34:06,651 INFO     30 [qwen-vl-text] coord item[20]: text=200mg/粒, bbox=[485, 631, 527, 648]
2026-08-06 10:34:06,651 INFO     30 [qwen-vl-text] coord item[21]: text=用法:1粒, bbox=[371, 652, 416, 669]
2026-08-06 10:34:06,651 INFO     30 [qwen-vl-text] coord item[22]: text=口服, bbox=[442, 655, 464, 670]
2026-08-06 10:34:06,651 INFO     30 [qwen-vl-text] coord item[23]: text=一次/日, bbox=[489, 657, 527, 673]
2026-08-06 10:34:06,651 INFO     30 [qwen-vl-text] coord item[24]: text=x3盒 28天, bbox=[548, 660, 595, 675]
2026-08-06 10:34:06,651 INFO     30 [qwen-vl-text] coord item[25]: text=医师:, bbox=[512, 714, 536, 728]
2026-08-06 10:34:06,651 INFO     30 [qwen-vl-text] coord item[26]: text=齐, bbox=[580, 706, 620, 731]
2026-08-06 10:34:06,652 INFO     30 [qwen-vl-text] coord item[27]: text=第1页, bbox=[470, 909, 509, 926]
2026-08-06 10:34:06,652 INFO     30 [qwen-vl-text] page=11 — 28/28 coords, api_time=9.9s
2026-08-06 10:34:06,652 INFO     30 [qwen-vl-text] new_positions (28):
[[11, 373.79916650390624, 487.4543184814453, 120.8410281982422, 140.48513623046875], [11, 343.4911259765625, 516.0785789794921, 135.12765222167968, 158.34341625976563], [11, 282.875044921875, 326.6533256835937, 155.3670362548828, 166.6772802734375], [11, 395.6883068847656, 463.0395080566406, 155.3670362548828, 174.41586828613282], [11, 278.6655948486328, 303.0804052734375, 170.84421228027344, 181.55918029785158], [11, 356.9613662109375, 389.79507678222654, 175.01114428710937, 185.72611230468752], [11, 428.5220174560547, 465.5651781005859, 178.58280029296876, 189.29776831054687], [11, 499.2407786865234, 511.86912890625, 183.34500830078125, 192.2741483154297], [11, 276.1399248046875, 468.09084814453126, 188.70249230957032, 207.15604833984375], [11, 276.1399248046875, 381.3761766357422, 207.75132434082033, 220.25212036132814], [11, 275.2980347900391, 402.42342700195314, 225.01432836914063, 238.11040039062502], [11, 274.4561447753906, 347.7005760498047, 242.8726083984375, 253.58757641601562], [11, 308.9736353759766, 418.41933728027345, 258.3497844238281, 271.44585644531253], [11, 272.77236474609373, 294.6615051269531, 275.61278845214844, 284.5419284667969], [11, 271.08858471679684, 284.55882495117186, 305.9718645019531, 314.9010045166016], [11, 411.6842171630859, 432.7314675292969, 297.63800048828125, 305.9718645019531], [11, 478.1935283203125, 560.6987497558594, 299.42382849121094, 310.1387965087891], [11, 476.5097482910156, 525.339369140625, 329.1876285400391, 338.7120445556641], [11, 270.24669470214843, 312.3411954345703, 338.7120445556641, 347.64118457031253], [11, 286.24260498046874, 394.0045268554687, 371.45222460937504, 383.9530206298828], [11, 408.3166571044922, 443.67603771972654, 375.61915661621094, 385.7388486328125], [11, 312.3411954345703, 350.22624609375, 388.1199526367188, 398.23964465332034], [11, 372.11538647460935, 390.636966796875, 389.90578063964847, 398.83492065429687], [11, 411.6842171630859, 443.67603771972654, 391.0963326416016, 400.62074865722656], [11, 461.35572802734373, 500.9245587158203, 392.88216064453127, 401.8113006591797], [11, 431.0476875, 451.2530478515625, 425.02706469726564, 433.3609287109375], [11, 488.29620849609375, 521.9718090820312, 420.26485668945315, 435.1467567138672], [11, 395.6883068847656, 428.5220174560547, 541.1058848876953, 551.2255769042969]]
2026-08-06 10:34:06,653 INFO     30 [qwen-vl-text] ═══ DONE ═══ 28 positions, pages=1, time=12.4s
2026-08-06 10:34:06,670 INFO     30 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-06 10:34:06,670 INFO     30 [Trace] task=dfc102e2 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "458 items", "markdown": "", "text": "", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 4, \"chunks_Clinical\": 1, \"chunks_LabExam\": 2}"}
2026-08-06 10:34:06,670 INFO     30 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-06 10:34:06,686 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:34:06,687 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-06 10:34:08,061 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:34:08,074 INFO     30 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-06 10:34:08,075 INFO     30 [Trace] task=dfc102e2 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "458 items", "markdown": "", "text": "", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 4, \"chunks_Clinical\": 1, \"chunks_LabExam\": 2}"}
2026-08-06 10:34:08,075 INFO     30 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-06 10:34:08,090 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:34:08,091 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-06 10:34:08,771 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:34:08,787 INFO     30 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-06 10:34:08,787 INFO     30 [Trace] task=dfc102e2 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "458 items", "markdown": "", "text": "", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 4, \"chunks_Clinical\": 1, \"chunks_LabExam\": 2}"}
2026-08-06 10:34:08,787 INFO     30 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-06 10:34:08,802 INFO     30 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 10:34:08,802 INFO     30 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-06 10:34:08,802 INFO     30 [qwen-vl-text] positions(115): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 10:34:08,802 INFO     30 [qwen-vl-text] page grouping: [0, 1, 2, 3], lines per page: [3, 38, 36, 38]
2026-08-06 10:34:08,951 INFO     30 [qwen-vl-text] page=0, rect=842x595, img=(2339x1654), dpi=200
2026-08-06 10:34:09,253 INFO     30 [qwen-vl-text] page=1, rect=842x595, img=(2339x1654), dpi=200
2026-08-06 10:34:09,539 INFO     30 [qwen-vl-text] page=2, rect=842x595, img=(2339x1654), dpi=200
2026-08-06 10:34:09,892 INFO     30 [qwen-vl-text] page=3, rect=842x595, img=(2339x1654), dpi=200
2026-08-06 10:34:09,893 INFO     30 [qwen-vl-text] LLM extraction start, text_len=3462
2026-08-06 10:34:09,893 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:34:09,893 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 0, \"bbox_end\": 114, \"encounter_dates\": [\"2025-12-03\", \"2025-12-06\"], \"department\": \"(江北)综合肿瘤中心\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "2025.5.21确诊小细胞肺癌\n2025.5.28-2025.7.16 依托泊苷+卡铂+斯鲁利\n2025.8.13-2025.11.7 依托泊苷+斯鲁利\n南京鼓楼医院\n南京大学医学院附属鼓楼医院\n出院记录\n科别（江北）综合肿瘤中心 病区（江北）B7病区床号07床 姓名\n住院号\n姓名：\n性别：女 年龄：75岁 婚姻：已婚 职业：农民\n入院诊断：1. 肺恶性肿瘤（左肺，小细胞癌广泛期）2. 肥 入院日期： 2025年12月03日\n厚型梗阻性心肌病 3. 纵隔淋巴结肿大 4. 肺门\n淋巴结肿大 5. 锁骨上淋巴结肿大（双侧）6. 腋\n下淋巴结肿大（右）7. 心功能III级（NYHA分级）\n8. 甲状腺功能减退症 9. 高血压2级（极高\n危）10. 肺气肿（局限性）11. 肺诊断性影像检\n查的异常所见（肺结节）12. 二尖瓣反流（重度）\n13. 心包积液（少量）14. 肾上腺结节（左侧）\n手术名称：\n手术日期：\n出院诊断：1. 恶性肿瘤支持治疗 2. 恶性肿瘤免疫治 出院日期： 2025年12月06日\n疗 3. 肺恶性肿瘤（左肺，小细胞癌广泛期）\n4. 肥厚型梗阻性心肌病 5. 纵隔淋巴结肿大\n6. 肺门淋巴结肿大 7. 锁骨上淋巴结肿大\n(双侧) 8. 腋下淋巴结肿大(右) 9. 心功能\nIII级(NYHA分级) 10. 甲状腺功能减退症\n11. 高血压2级（极高危）12. 肺气肿(局\n限性) 13. 肺诊断性影像检查的异常所见(肺\n结节) 14. 二尖瓣反流(重度) 15. 心包积\n液(少量) 16. 肾上腺结节(左侧)\n入院时情况（主要症状、体征，有关实验室及器械检查结果）：\n患者因“咳嗽1月余”于2025-05-21至河北省人民医院就诊，查胸部CT：左肺下叶占位性病变，恶性不除\n外，远端阻塞性肺炎，建议完善实验室检查及增强CT。双侧锁骨窝、右侧腋下、纵隔内及双肺门多发肿大\n淋巴结，转移不除外。左侧胸膜结节样增厚，转移不除外。后于2025-05-23行肺穿刺活检术，术后病理回\n示：（左肺）穿刺组织：结合免疫组化染色支持小细胞癌。免疫组化染色： CKpan (+)，Vimentin (-)，\nCK7 (+)，TTF -1(+)，NapsinA (-)，CK5/6(-)，P40(-)，P63(-)，CgA (+)，Syn (+)，CD56(+)。根据患者病情\n于2025-05-28当地医院行依托泊苷+卡铂方案化疗+斯鲁利单抗免疫治疗1周期，过程顺利。于\n2025-06-19、2025-07-16开始行依托泊苷+卡铂化疗+斯鲁利单抗免疫治疗2周期，过程顺利。2025-07-27复\n查血常规示血小板38×10^9/L。予升血小板治疗后。2025-08-13、2025-09-06、2025-10-08、2025-11-07\n行依托泊苷化疗+斯鲁利单抗免疫治疗4周期，期间疗效评价PR。患者为求进一步治疗就诊我科，门诊拟\n第 1 页\n南京鼓楼医院\n南京大学医学院附属鼓楼医院\n出院记录\n科别（江北）综合肿瘤中心 病区（江北）B7病区床号 姓名 住院号\n“肺恶性肿瘤”收住入院。病程中，患者神志清，精神可，食纳睡眠可，二便如常，近期体重未见明显变\n化。\n诊疗经过：\n患者入院完善相关检查：\n【检验】\n2025.12.03 12:22 甲功三项：*促甲状腺激素 34.210 mIU/L↑，*游离三碘甲状腺原氨酸 2.60 pmol/L↓，\n*游离甲状腺素 9.58 pmol/L↓。\n2025.12.03 12:22 肺癌六项（江北）：*细胞角蛋白19片段 3.61 ng/mL↑，*神经元特异性烯醇化酶\n26.80 ng/mL↑，胃泌素释放肽前体 243.00 pg/mL↑。\n2025.12.03 13:33 生化全套，心肌酶：*碱性磷酸酶 46.8 U/L↓，*葡萄糖 6.66 mmol/L↑，*甘油三酯\n8.26 mmol/L↑，*总胆固醇 7.14 mmol/L↑，*H-脂蛋白胆固醇 0.90 mmol/L↓，*L-脂蛋白胆固醇 3.51\nmmol/L↑，*载脂蛋白AⅠ 0.79 g/L↓，*载脂蛋白B 1.87 g/L↑，*钠 136.1 mmol/L↓，*氯 97.8\nmmol/L↓，*α羟丁酸脱氢酶 158 U/L↑，eGFR(CKD-EPI) 77.2 ml/min/1.73m^2↓。\n2025.12.03 14:45 血常规：淋巴细胞百分数 19.7 %↓，淋巴细胞绝对值 0.8 ×10^9/L↓，*红细胞计数\n3.30 ×10^12/L↓，*血红蛋白量 108 g/L↓，*红细胞压积 31.8 %↓，红细胞体积分布宽度 15.4 %↑，*\n血小板计数 112 ×10^9/L↓。\n余未见明显异常。\n【检查】\n2025.12.04 15:19 心电图检查（江北）（检查）常规心电图 检查结论 窦性心律一度房室传导阻滞左前分支\n阻滞异常Q波(V1、V2)左心室高电压ST-T改变QTc间期延长\n2025.12.04 16:29（江北）PET/CT(检查) PET/CT全身显像 检查结论 1.“左肺癌化疗后复查”；①左下肺\n门稍大伴葡萄糖代谢增高灶，内部通行支气管狭窄，结合病史考虑符合小细胞癌表现；②左肺下叶两枚软\n组织结节，葡萄糖代谢异常增高；双肺门、纵隔、右侧腋窝多发肿大淋巴结，葡萄糖代谢显著增高；以上\n考虑同侧肺内转移、多发淋巴结转移；2.双肺多发小结节，部分为磨玻璃结节，葡萄糖代谢未见增高，建\n议胸部CT随诊；双肺散在条索及渗出；左肺下叶节段性肺不张；右肺局限性肺气肿；双侧胸膜增厚；3.左\n肾上腺稍低密度结节，葡萄糖代谢未见异常增高，左肾上腺稍增粗，葡萄糖代谢轻度增高，倾向增生伴腺\n瘤形成，请比对老片、密切随诊观察；4.腔隙性脑梗死可能；脑萎缩；副鼻窦炎症；甲状腺左右两叶密度\n欠均，葡萄糖代谢增高，考虑炎性摄取增高，必要时请结合甲功、颈部超声随诊；5.心影偏大，冠状动脉\n及胸部大血管管壁钙化；6.食管中下段管壁似稍增厚，葡萄糖代谢轻度增高，考虑炎性或生理性摄取可\n能，必要时内镜检查；十二指肠憩室可能；轻度脂肪肝；肝囊肿；胆囊饱满；7.慢性膀胱炎症可能；盆腔\n内钙化结节；8.颈椎生理性曲度变直，脊柱退变；右股骨下段低密度伴内部钙化，葡萄糖代谢不高，考虑\n第 2 页\n3/4\n南京鼓楼医院\n南京大学医学院附属鼓楼医院\n出院记录\n科别（江北）综合肿瘤中心 病区（江北）B7病区床号\n姓名 住院号\n良性灶如内生软骨瘤可能，随诊；右肩背部皮下稍低密度结节，葡萄糖代谢未见增高，考虑良性灶，随\n诊。\n【诊疗经过】\n患者入院后完善PET-CT复查，病情较前基本相仿，暂无根治性放疗指征。排除禁忌后，患者于2025-12-05\n行斯鲁利单抗免疫维持治疗1周期。现本周期静脉治疗已结束，现整体病情稳定，一般情况尚可，准予办理\n出院。\n出院情况： 好转\n伤口愈合：-\nECOG 1分，NRS 0分，神志清，精神可，无贫血貌，全身皮肤巩膜无黄染。胸廓外形正常，无胸壁静脉曲\n张。双侧呼吸运动对称，肋间隙：正常，触觉语颤：对称，皮下捻发感：无，双肺叩诊清音，双肺呼吸音\n稍粗，两肺未闻及明显干湿啰音。心律齐，心脏各瓣膜区未闻及杂音。腹部平坦，腹部无压痛，无反跳\n痛。双下肢无明显水肿。\n出院医嘱：\n1、注意天气变化，注意休息、低脂饮食，避免受凉，避免手足接触冰冷物体，注意皮肤保暖。\n2、出院后继续用药\n左甲状腺素钠片（优甲乐）50微克/片 1片 口服 QD（7点）（每天早餐前半小时服用1片，补充甲状腺激\n素，内分泌科随诊调药）\n3、定期复查血常规（每周1-2次）及生化全套（每周1次），如WBC<3.0×10^9/L、PLT<60×10^9/L或生化\n全套指标异常，请及时当地医院就诊（如有急症或危急值报告，请及时就近正规医院急诊就诊），我科门\n诊随诊。\n4、下次治疗时间：3-4周左右，具体等电话通知。杨阳主任医师专家门诊时间：门诊时间：每周二、周五\n上午，（周二本部，周五江北），（江北肿瘤科医生办公室电话：025-83106666转220717）。如需肿瘤日\n间治疗，请提前一周至杨阳主任医师门诊预约。\n5、不适门诊随诊。\n不存在尚未回归的病理检查结果。\nX光片号：-\nCT号： P049684\nMRI号：-\n病理号：-\n上级医师：\n医师：\n第 3 页",
    "role": "user"
  }
]
2026-08-06 10:34:23,326 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:34:23.324+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 8, "lag": 0, "done": 1, "failed": 0, "current": {"00b9d592918111f18dbe1f8f96f1c395": {"id": "00b9d592918111f18dbe1f8f96f1c395", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011867426, "task_type": "dataflow", "root_trace_id": "1ab3198c92574fb4b2701d0f5db7322f", "root_traceparent": "00-1ab3198c92574fb4b2701d0f5db7322f-bdaff6f64a5f4a64-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "dfc102e2918111f18dbe1f8f96f1c395": {"id": "dfc102e2918111f18dbe1f8f96f1c395", "doc_id": "de8a02fc918111f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786012241604, "task_type": "dataflow", "root_trace_id": "90f550f6b00248c3845d57a8e0bcf6fb", "root_traceparent": "00-90f550f6b00248c3845d57a8e0bcf6fb-5db7fb7d470dfe0d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:34:46,182 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:34:46,183 INFO     30 [qwen-vl-text] LLM output (len=6860):
{
  "encounter_date": "2025-12-06",
  "admission_date": "2025-12-03",
  "discharge_date": "2025-12-06",
  "hospital_days": 3,
  "department": "(江北)综合肿瘤中心",
  "bed_number": "07床",
  "admission_condition": "患者因“咳嗽1月余”于2025-05-21至河北省人民医院就诊，查胸部CT：左肺下叶占位性病变，恶性不除外，远端阻塞性肺炎，建议完善实验室检查及增强CT。双侧锁骨窝、右侧腋下、纵隔内及双肺门多发肿大淋巴结，转移不除外。左侧胸膜结节样增厚，转移不除外。后于2025-05-23行肺穿刺活检术，术后病理回示：（左肺）穿刺组织：结合免疫组化染色支持小细胞癌。免疫组化染色： CKpan (+)，Vimentin (-)，CK7 (+)，TTF -1(+)，NapsinA (-)，CK5/6(-)，P40(-)，P63(-)，CgA (+)，Syn (+)，CD56(+)。根据患者病情于2025-05-28当地医院行依托泊苷+卡铂方案化疗+斯鲁利单抗免疫治疗1周期，过程顺利。于2025-06-19、2025-07-16开始行依托泊苷+卡铂化疗+斯鲁利单抗免疫治疗2周期，过程顺利。2025-07-27复查血常规示血小板38×10^9/L。予升血小板治疗后。2025-08-13、2025-09-06、2025-10-08、2025-11-07行依托泊苷化疗+斯鲁利单抗免疫治疗4周期，期间疗效评价PR。患者为求进一步治疗就诊我科，门诊拟“肺恶性肿瘤”收住入院。病程中，患者神志清，精神可，食纳睡眠可，二便如常，近期体重未见明显变化。",
  "admission_diagnoses": [
    {
      "name": "肺恶性肿瘤（左肺，小细胞癌广泛期）",
      "diagnosis_type": "西医"
    },
    {
      "name": "肥厚型梗阻性心肌病",
      "diagnosis_type": "西医"
    },
    {
      "name": "纵隔淋巴结肿大",
      "diagnosis_type": "西医"
    },
    {
      "name": "肺门淋巴结肿大",
      "diagnosis_type": "西医"
    },
    {
      "name": "锁骨上淋巴结肿大（双侧）",
      "diagnosis_type": "西医"
    },
    {
      "name": "腋下淋巴结肿大（右）",
      "diagnosis_type": "西医"
    },
    {
      "name": "心功能III级（NYHA分级）",
      "diagnosis_type": "西医"
    },
    {
      "name": "甲状腺功能减退症",
      "diagnosis_type": "西医"
    },
    {
      "name": "高血压2级（极高危）",
      "diagnosis_type": "西医"
    },
    {
      "name": "肺气肿（局限性）",
      "diagnosis_type": "西医"
    },
    {
      "name": "肺诊断性影像检查的异常所见（肺结节）",
      "diagnosis_type": "西医"
    },
    {
      "name": "二尖瓣反流（重度）",
      "diagnosis_type": "西医"
    },
    {
      "name": "心包积液（少量）",
      "diagnosis_type": "西医"
    },
    {
      "name": "肾上腺结节（左侧）",
      "diagnosis_type": "西医"
    }
  ],
  "treatment_summary": "患者入院完善相关检查：【检验】2025.12.03 12:22 甲功三项：*促甲状腺激素 34.210 mIU/L↑，*游离三碘甲状腺原氨酸 2.60 pmol/L↓，*游离甲状腺素 9.58 pmol/L↓。2025.12.03 12:22 肺癌六项（江北）：*细胞角蛋白19片段 3.61 ng/mL↑，*神经元特异性烯醇化酶 26.80 ng/mL↑，胃泌素释放肽前体 243.00 pg/mL↑。2025.12.03 13:33 生化全套，心肌酶：*碱性磷酸酶 46.8 U/L↓，*葡萄糖 6.66 mmol/L↑，*甘油三酯 8.26 mmol/L↑，*总胆固醇 7.14 mmol/L↑，*H-脂蛋白胆固醇 0.90 mmol/L↓，*L-脂蛋白胆固醇 3.51 mmol/L↑，*载脂蛋白AⅠ 0.79 g/L↓，*载脂蛋白B 1.87 g/L↑，*钠 136.1 mmol/L↓，*氯 97.8 mmol/L↓，*α羟丁酸脱氢酶 158 U/L↑，eGFR(CKD-EPI) 77.2 ml/min/1.73m^2↓。2025.12.03 14:45 血常规：淋巴细胞百分数 19.7 %↓，淋巴细胞绝对值 0.8 ×10^9/L↓，*红细胞计数 3.30 ×10^12/L↓，*血红蛋白量 108 g/L↓，*红细胞压积 31.8 %↓，红细胞体积分布宽度 15.4 %↑，*血小板计数 112 ×10^9/L↓。余未见明显异常。【检查】2025.12.04 15:19 心电图检查（江北）（检查）常规心电图 检查结论 窦性心律一度房室传导阻滞左前分支阻滞异常Q波(V1、V2)左心室高电压ST-T改变QTc间期延长。2025.12.04 16:29（江北）PET/CT(检查) PET/CT全身显像 检查结论 1.“左肺癌化疗后复查”；①左下肺门稍大伴葡萄糖代谢增高灶，内部通行支气管狭窄，结合病史考虑符合小细胞癌表现；②左肺下叶两枚软组织结节，葡萄糖代谢异常增高；双肺门、纵隔、右侧腋窝多发肿大淋巴结，葡萄糖代谢显著增高；以上考虑同侧肺内转移、多发淋巴结转移；2.双肺多发小结节，部分为磨玻璃结节，葡萄糖代谢未见增高，建议胸部CT随诊；双肺散在条索及渗出；左肺下叶节段性肺不张；右肺局限性肺气肿；双侧胸膜增厚；3.左肾上腺稍低密度结节，葡萄糖代谢未见异常增高，左肾上腺稍增粗，葡萄糖代谢轻度增高，倾向增生伴腺瘤形成，请比对老片、密切随诊观察；4.腔隙性脑梗死可能；脑萎缩；副鼻窦炎症；甲状腺左右两叶密度欠均，葡萄糖代谢增高，考虑炎性摄取增高，必要时请结合甲功、颈部超声随诊；5.心影偏大，冠状动脉及胸部大血管管壁钙化；6.食管中下段管壁似稍增厚，葡萄糖代谢轻度增高，考虑炎性或生理性摄取可能，必要时内镜检查；十二指肠憩室可能；轻度脂肪肝；肝囊肿；胆囊饱满；7.慢性膀胱炎症可能；盆腔内钙化结节；8.颈椎生理性曲度变直，脊柱退变；右股骨下段低密度伴内部钙化，葡萄糖代谢不高，考虑良性灶如内生软骨瘤可能，随诊；右肩背部皮下稍低密度结节，葡萄糖代谢未见增高，考虑良性灶，随诊。【诊疗经过】患者入院后完善PET-CT复查，病情较前基本相仿，暂无根治性放疗指征。排除禁忌后，患者于2025-12-05行斯鲁利单抗免疫维持治疗1周期。现本周期静脉治疗已结束，现整体病情稳定，一般情况尚可，准予办理出院。",
  "auxiliary_exams": "2025.12.03 12:22 甲功三项：*促甲状腺激素 34.210 mIU/L↑，*游离三碘甲状腺原氨酸 2.60 pmol/L↓，*游离甲状腺素 9.58 pmol/L↓。2025.12.03 12:22 肺癌六项（江北）：*细胞角蛋白19片段 3.61 ng/mL↑，*神经元特异性烯醇化酶 26.80 ng/mL↑，胃泌素释放肽前体 243.00 pg/mL↑。2025.12.03 13:33 生化全套，心肌酶：*碱性磷酸酶 46.8 U/L↓，*葡萄糖 6.66 mmol/L↑，*甘油三酯 8.26 mmol/L↑，*总胆固醇 7.14 mmol/L↑，*H-脂蛋白胆固醇 0.90 mmol/L↓，*L-脂蛋白胆固醇 3.51 mmol/L↑，*载脂蛋白AⅠ 0.79 g/L↓，*载脂蛋白B 1.87 g/L↑，*钠 136.1 mmol/L↓，*氯 97.8 mmol/L↓，*α羟丁酸脱氢酶 158 U/L↑，eGFR(CKD-EPI) 77.2 ml/min/1.73m^2↓。2025.12.03 14:45 血常规：淋巴细胞百分数 19.7 %↓，淋巴细胞绝对值 0.8 ×10^9/L↓，*红细胞计数 3.30 ×10^12/L↓，*血红蛋白量 108 g/L↓，*红细胞压积 31.8 %↓，红细胞体积分布宽度 15.4 %↑，*血小板计数 112 ×10^9/L↓。",
  "imaging_findings": "2025.12.04 15:19 心电图检查（江北）（检查）常规心电图 检查结论 窦性心律一度房室传导阻滞左前分支阻滞异常Q波(V1、V2)左心室高电压ST-T改变QTc间期延长。2025.12.04 16:29（江北）PET/CT(检查) PET/CT全身显像 检查结论 1.“左肺癌化疗后复查”；①左下肺门稍大伴葡萄糖代谢增高灶，内部通行支气管狭窄，结合病史考虑符合小细胞癌表现；②左肺下叶两枚软组织结节，葡萄糖代谢异常增高；双肺门、纵隔、右侧腋窝多发肿大淋巴结，葡萄糖代谢显著增高；以上考虑同侧肺内转移、多发淋巴结转移；2.双肺多发小结节，部分为磨玻璃结节，葡萄糖代谢未见增高，建议胸部CT随诊；双肺散在条索及渗出；左肺下叶节段性肺不张；右肺局限性肺气肿；双侧胸膜增厚；3.左肾上腺稍低密度结节，葡萄糖代谢未见异常增高，左肾上腺稍增粗，葡萄糖代谢轻度增高，倾向增生伴腺瘤形成，请比对老片、密切随诊观察；4.腔隙性脑梗死可能；脑萎缩；副鼻窦炎症；甲状腺左右两叶密度欠均，葡萄糖代谢增高，考虑炎性摄取增高，必要时请结合甲功、颈部超声随诊；5.心影偏大，冠状动脉及胸部大血管管壁钙化；6.食管中下段管壁似稍增厚，葡萄糖代谢轻度增高，考虑炎性或生理性摄取可能，必要时内镜检查；十二指肠憩室可能；轻度脂肪肝；肝囊肿；胆囊饱满；7.慢性膀胱炎症可能；盆腔内钙化结节；8.颈椎生理性曲度变直，脊柱退变；右股骨下段低密度伴内部钙化，葡萄糖代谢不高，考虑良性灶如内生软骨瘤可能，随诊；右肩背部皮下稍低密度结节，葡萄糖代谢未见增高，考虑良性灶，随诊。",
  "discharge_diagnoses": [
    {
      "name": "恶性肿瘤支持治疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "恶性肿瘤免疫治疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "肺恶性肿瘤（左肺，小细胞癌广泛期）",
      "diagnosis_type": "西医"
    },
    {
      "name": "肥厚型梗阻性心肌病",
      "diagnosis_type": "西医"
    },
    {
      "name": "纵隔淋巴结肿大",
      "diagnosis_type": "西医"
    },
    {
      "name": "肺门淋巴结肿大",
      "diagnosis_type": "西医"
    },
    {
      "name": "锁骨上淋巴结肿大(双侧)",
      "diagnosis_type": "西医"
    },
    {
      "name": "腋下淋巴结肿大(右)",
      "diagnosis_type": "西医"
    },
    {
      "name": "心功能III级(NYHA分级)",
      "diagnosis_type": "西医"
    },
    {
      "name": "甲状腺功能减退症",
      "diagnosis_type": "西医"
    },
    {
      "name": "高血压2级（极高危）",
      "diagnosis_type": "西医"
    },
    {
      "name": "肺气肿(局限性)",
      "diagnosis_type": "西医"
    },
    {
      "name": "肺诊断性影像检查的异常所见(肺结节)",
      "diagnosis_type": "西医"
    },
    {
      "name": "二尖瓣反流(重度)",
      "diagnosis_type": "西医"
    },
    {
      "name": "心包积液(少量)",
      "diagnosis_type": "西医"
    },
    {
      "name": "肾上腺结节(左侧)",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": "好转",
  "outcome": "好转",
  "discharge_orders": "1、注意天气变化，注意休息、低脂饮食，避免受凉，避免手足接触冰冷物体，注意皮肤保暖。\n2、出院后继续用药\n左甲状腺素钠片（优甲乐）50微克/片 1片 口服 QD（7点）（每天早餐前半小时服用1片，补充甲状腺激素，内分泌科随诊调药）\n3、定期复查血常规（每周1-2次）及生化全套（每周1次），如WBC<3.0×10^9/L、PLT<60×10^9/L或生化全套指标异常，请及时当地医院就诊（如有急症或危急值报告，请及时就近正规医院急诊就诊），我科门诊随诊。\n4、下次治疗时间：3-4周左右，具体等电话通知。杨阳主任医师专家门诊时间：门诊时间：每周二、周五上午，（周二本部，周五江北），（江北肿瘤科医生办公室电话：025-83106666转220717）。如需肿瘤日间治疗，请提前一周至杨阳主任医师门诊预约。\n5、不适门诊随诊。\n不存在尚未回归的病理检查结果。",
  "do_medications": [
    "左甲状腺素钠片（优甲乐） 50微克/片 1片 口服 QD"
  ],
  "do_follow_up": "定期复查血常规（每周1-2次）及生化全套（每周1次），如WBC<3.0×10^9/L、PLT<60×10^9/L或生化全套指标异常，请及时当地医院就诊（如有急症或危急值报告，请及时就近正规医院急诊就诊），我科门诊随诊。杨阳主任医师专家门诊时间：门诊时间：每周二、周五上午，（周二本部，周五江北）。",
  "do_precautions": [
    "注意天气变化，注意休息、低脂饮食，避免受凉，避免手足接触冰冷物体，注意皮肤保暖。",
    "定期复查血常规（每周1-2次）及生化全套（每周1次），如WBC<3.0×10^9/L、PLT<60×10^9/L或生化全套指标异常，请及时当地医院就诊",
    "如有急症或危急值报告，请及时就近正规医院急诊就诊",
    "不适门诊随诊"
  ],
  "next_treatment_date": "3-4周左右",
  "attending_physician": "杨阳",
  "pe_ecog_score": 1,
  "body_surface_area": null,
  "vs_temperature_c": null,
  "vs_pulse_bpm": null,
  "vs_respiration_rpm": null,
  "vs_systolic_bp_mmhg": null,
  "vs_diastolic_bp_mmhg": null
}
2026-08-06 10:34:46,183 INFO     30 [qwen-vl-text] Updated encounter_dates=[2025-12-06]
2026-08-06 10:34:46,184 INFO     30 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=120172, prompt_len=698
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共3行）
["2025.5.21确诊小细胞肺癌", "2025.5.28-2025.7.16 依托泊苷+卡铂+斯鲁利", "2025.8.13-2025.11.7 依托泊苷+斯鲁利"]

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
2026-08-06 10:34:48,873 INFO     30 [qwen-vl-text] coord API raw response (len=212):
[
	{"text": "2025.5.21确诊小细胞肺癌", "bbox": [305, 253, 470, 273]},
	{"text": "2025.5.28-2025.7.16 依托泊苷+卡铂+斯鲁利", "bbox": [305, 273, 590, 293]},
	{"text": "2025.8.13-2025.11.7 依托泊苷+斯鲁利", "bbox": [305, 293, 555, 313]}
]
2026-08-06 10:34:48,874 INFO     30 [qwen-vl-text] coord API: raw_items=3, valid_items=3, elapsed=2.7s
2026-08-06 10:34:48,874 INFO     30 [qwen-vl-text] coord item[0]: text=2025.5.21确诊小细胞肺癌, bbox=[305, 253, 470, 273]
2026-08-06 10:34:48,874 INFO     30 [qwen-vl-text] coord item[1]: text=2025.5.28-2025.7.16 依托泊苷+卡铂+斯鲁利, bbox=[305, 273, 590, 293]
2026-08-06 10:34:48,874 INFO     30 [qwen-vl-text] coord item[2]: text=2025.8.13-2025.11.7 依托泊苷+斯鲁利, bbox=[305, 293, 555, 313]
2026-08-06 10:34:48,875 INFO     30 [qwen-vl-text] page=0 — 3/3 coords, api_time=2.7s
2026-08-06 10:34:48,881 INFO     30 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1026668, prompt_len=1880
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共38行）
["南京鼓楼医院", "南京大学医学院附属鼓楼医院", "出院记录", "科别（江北）综合肿瘤中心 病区（江北）B7病区床号07床 姓名", "住院号", "姓名：", "性别：女 年龄：75岁 婚姻：已婚 职业：农民", "入院诊断：1. 肺恶性肿瘤（左肺，小细胞癌广泛期）2. 肥 入院日期： 2025年12月03日", "厚型梗阻性心肌病 3. 纵隔淋巴结肿大 4. 肺门", "淋巴结肿大 5. 锁骨上淋巴结肿大（双侧）6. 腋", "下淋巴结肿大（右）7. 心功能III级（NYHA分级）", "8. 甲状腺功能减退症 9. 高血压2级（极高", "危）10. 肺气肿（局限性）11. 肺诊断性影像检", "查的异常所见（肺结节）12. 二尖瓣反流（重度）", "13. 心包积液（少量）14. 肾上腺结节（左侧）", "手术名称：", "手术日期：", "出院诊断：1. 恶性肿瘤支持治疗 2. 恶性肿瘤免疫治 出院日期： 2025年12月06日", "疗 3. 肺恶性肿瘤（左肺，小细胞癌广泛期）", "4. 肥厚型梗阻性心肌病 5. 纵隔淋巴结肿大", "6. 肺门淋巴结肿大 7. 锁骨上淋巴结肿大", "(双侧) 8. 腋下淋巴结肿大(右) 9. 心功能", "III级(NYHA分级) 10. 甲状腺功能减退症", "11. 高血压2级（极高危）12. 肺气肿(局", "限性) 13. 肺诊断性影像检查的异常所见(肺", "结节) 14. 二尖瓣反流(重度) 15. 心包积", "液(少量) 16. 肾上腺结节(左侧)", "入院时情况（主要症状、体征，有关实验室及器械检查结果）：", "患者因“咳嗽1月余”于2025-05-21至河北省人民医院就诊，查胸部CT：左肺下叶占位性病变，恶性不除", "外，远端阻塞性肺炎，建议完善实验室检查及增强CT。双侧锁骨窝、右侧腋下、纵隔内及双肺门多发肿大", "淋巴结，转移不除外。左侧胸膜结节样增厚，转移不除外。后于2025-05-23行肺穿刺活检术，术后病理回", "示：（左肺）穿刺组织：结合免疫组化染色支持小细胞癌。免疫组化染色： CKpan (+)，Vimentin (-)，", "CK7 (+)，TTF -1(+)，NapsinA (-)，CK5/6(-)，P40(-)，P63(-)，CgA (+)，Syn (+)，CD56(+)。根据患者病情", "于2025-05-28当地医院行依托泊苷+卡铂方案化疗+斯鲁利单抗免疫治疗1周期，过程顺利。于", "2025-06-19、2025-07-16开始行依托泊苷+卡铂化疗+斯鲁利单抗免疫治疗2周期，过程顺利。2025-07-27复", "查血常规示血小板38×10^9/L。予升血小板治疗后。2025-08-13、2025-09-06、2025-10-08、2025-11-07", "行依托泊苷化疗+斯鲁利单抗免疫治疗4周期，期间疗效评价PR。患者为求进一步治疗就诊我科，门诊拟", "第 1 页"]

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
2026-08-06 10:35:09,862 INFO     30 [qwen-vl-text] coord API raw response (len=2827):
[
	{"text": "南京鼓楼医院", "bbox": [460, 94, 538, 111]},
	{"text": "南京大学医学院附属鼓楼医院", "bbox": [415, 117, 584, 134]},
	{"text": "出院记录", "bbox": [436, 139, 562, 164]},
	{"text": "科别（江北）综合肿瘤中心 病区（江北）B7病区床号07床 姓名", "bbox": [295, 170, 561, 184]},
	{"text": "住院号", "bbox": [609, 170, 638, 184]},
	{"text": "姓名：", "bbox": [295, 198, 318, 211]},
	{"text": "性别：女 年龄：75岁 婚姻：已婚 职业：农民", "bbox": [365, 198, 602, 211]},
	{"text": "入院诊断：1. 肺恶性肿瘤（左肺，小细胞癌广泛期）2. 肥 入院日期： 2025年12月03日", "bbox": [298, 227, 640, 241]},
	{"text": "厚型梗阻性心肌病 3. 纵隔淋巴结肿大 4. 肺门", "bbox": [343, 250, 527, 264]},
	{"text": "淋巴结肿大 5. 锁骨上淋巴结肿大（双侧）6. 腋", "bbox": [343, 273, 527, 287]},
	{"text": "下淋巴结肿大（右）7. 心功能III级（NYHA分级）", "bbox": [343, 296, 526, 310]},
	{"text": "8. 甲状腺功能减退症 9. 高血压2级（极高", "bbox": [343, 319, 527, 333]},
	{"text": "危）10. 肺气肿（局限性）11. 肺诊断性影像检", "bbox": [343, 342, 527, 356]},
	{"text": "查的异常所见（肺结节）12. 二尖瓣反流（重度）", "bbox": [343, 365, 527, 379]},
	{"text": "13. 心包积液（少量）14. 肾上腺结节（左侧）", "bbox": [343, 388, 511, 402]},
	{"text": "手术名称：", "bbox": [298, 415, 338, 428]},
	{"text": "手术日期：", "bbox": [531, 415, 567, 428]},
	{"text": "出院诊断：1. 恶性肿瘤支持治疗 2. 恶性肿瘤免疫治 出院日期： 2025年12月06日", "bbox": [298, 442, 640, 456]},
	{"text": "疗 3. 肺恶性肿瘤（左肺，小细胞癌广泛期）", "bbox": [343, 464, 520, 478]},
	{"text": "4. 肥厚型梗阻性心肌病 5. 纵隔淋巴结肿大", "bbox": [343, 487, 527, 501]},
	{"text": "6. 肺门淋巴结肿大 7. 锁骨上淋巴结肿大", "bbox": [343, 510, 517, 524]},
	{"text": "(双侧) 8. 腋下淋巴结肿大(右) 9. 心功能", "bbox": [343, 533, 523, 547]},
	{"text": "III级(NYHA分级) 10. 甲状腺功能减退症", "bbox": [343, 556, 514, 570]},
	{"text": "11. 高血压2级（极高危）12. 肺气肿(局", "bbox": [343, 578, 527, 592]},
	{"text": "限性) 13. 肺诊断性影像检查的异常所见(肺", "bbox": [343, 601, 527, 615]},
	{"text": "结节) 14. 二尖瓣反流(重度) 15. 心包积", "bbox": [343, 624, 520, 638]},
	{"text": "液(少量) 16. 肾上腺结节(左侧)", "bbox": [343, 647, 480, 661]},
	{"text": "入院时情况（主要症状、体征，有关实验室及器械检查结果）：", "bbox": [298, 661, 523, 675]},
	{"text": "患者因“咳嗽1月余”于2025-05-21至河北省人民医院就诊，查胸部CT：左肺下叶占位性病变，恶性不除", "bbox": [295, 678, 701, 692]},
	{"text": "外，远端阻塞性肺炎，建议完善实验室检查及增强CT。双侧锁骨窝、右侧腋下、纵隔内及双肺门多发肿大", "bbox": [295, 701, 701, 715]},
	{"text": "淋巴结，转移不除外。左侧胸膜结节样增厚，转移不除外。后于2025-05-23行肺穿刺活检术，术后病理回", "bbox": [295, 724, 701, 738]},
	{"text": "示：（左肺）穿刺组织：结合免疫组化染色支持小细胞癌。免疫组化染色： CKpan (+)，Vimentin (-)，", "bbox": [295, 747, 701, 761]},
	{"text": "CK7 (+)，TTF -1(+)，NapsinA (-)，CK5/6(-)，P40(-)，P63(-)，CgA (+)，Syn (+)，CD56(+)。根据患者病情", "bbox": [295, 770, 701, 784]},
	{"text": "于2025-05-28当地医院行依托泊苷+卡铂方案化疗+斯鲁利单抗免疫治疗1周期，过程顺利。于", "bbox": [295, 793, 701, 807]},
	{"text": "2025-06-19、2025-07-16开始行依托泊苷+卡铂化疗+斯鲁利单抗免疫治疗2周期，过程顺利。2025-07-27复", "bbox": [295, 816, 701, 830]},
	{"text": "查血常规示血小板38×10^9/L。予升血小板治疗后。2025-08-13、2025-09-06、2025-10-08、2025-11-07", "bbox": [295, 839, 701, 853]},
	{"text": "行依托泊苷化疗+斯鲁利单抗免疫治疗4周期，期间疗效评价PR。患者为求进一步治疗就诊我科，门诊拟", "bbox": [295, 861, 701, 875]},
	{"text": "第 1 页", "bbox": [471, 912, 515, 924]}
]
2026-08-06 10:35:09,862 INFO     30 [qwen-vl-text] coord API: raw_items=38, valid_items=38, elapsed=21.0s
2026-08-06 10:35:09,862 INFO     30 [qwen-vl-text] coord item[0]: text=南京鼓楼医院, bbox=[460, 94, 538, 111]
2026-08-06 10:35:09,863 INFO     30 [qwen-vl-text] coord item[1]: text=南京大学医学院附属鼓楼医院, bbox=[415, 117, 584, 134]
2026-08-06 10:35:09,863 INFO     30 [qwen-vl-text] coord item[2]: text=出院记录, bbox=[436, 139, 562, 164]
2026-08-06 10:35:09,863 INFO     30 [qwen-vl-text] coord item[3]: text=科别（江北）综合肿瘤中心 病区（江北）B7病区床号07床 姓名, bbox=[295, 170, 561, 184]
2026-08-06 10:35:09,863 INFO     30 [qwen-vl-text] coord item[4]: text=住院号, bbox=[609, 170, 638, 184]
2026-08-06 10:35:09,863 INFO     30 [qwen-vl-text] coord item[5]: text=姓名：, bbox=[295, 198, 318, 211]
2026-08-06 10:35:09,863 INFO     30 [qwen-vl-text] coord item[6]: text=性别：女 年龄：75岁 婚姻：已婚 职业：农民, bbox=[365, 198, 602, 211]
2026-08-06 10:35:09,863 INFO     30 [qwen-vl-text] coord item[7]: text=入院诊断：1. 肺恶性肿瘤（左肺，小细胞癌广泛期）2. 肥 入院日期： 2025年12月03日, bbox=[298, 227, 640, 241]
2026-08-06 10:35:09,863 INFO     30 [qwen-vl-text] coord item[8]: text=厚型梗阻性心肌病 3. 纵隔淋巴结肿大 4. 肺门, bbox=[343, 250, 527, 264]
2026-08-06 10:35:09,863 INFO     30 [qwen-vl-text] coord item[9]: text=淋巴结肿大 5. 锁骨上淋巴结肿大（双侧）6. 腋, bbox=[343, 273, 527, 287]
2026-08-06 10:35:09,863 INFO     30 [qwen-vl-text] coord item[10]: text=下淋巴结肿大（右）7. 心功能III级（NYHA分级）, bbox=[343, 296, 526, 310]
2026-08-06 10:35:09,864 INFO     30 [qwen-vl-text] coord item[11]: text=8. 甲状腺功能减退症 9. 高血压2级（极高, bbox=[343, 319, 527, 333]
2026-08-06 10:35:09,864 INFO     30 [qwen-vl-text] coord item[12]: text=危）10. 肺气肿（局限性）11. 肺诊断性影像检, bbox=[343, 342, 527, 356]
2026-08-06 10:35:09,864 INFO     30 [qwen-vl-text] coord item[13]: text=查的异常所见（肺结节）12. 二尖瓣反流（重度）, bbox=[343, 365, 527, 379]
2026-08-06 10:35:09,864 INFO     30 [qwen-vl-text] coord item[14]: text=13. 心包积液（少量）14. 肾上腺结节（左侧）, bbox=[343, 388, 511, 402]
2026-08-06 10:35:09,864 INFO     30 [qwen-vl-text] coord item[15]: text=手术名称：, bbox=[298, 415, 338, 428]
2026-08-06 10:35:09,864 INFO     30 [qwen-vl-text] coord item[16]: text=手术日期：, bbox=[531, 415, 567, 428]
2026-08-06 10:35:09,864 INFO     30 [qwen-vl-text] coord item[17]: text=出院诊断：1. 恶性肿瘤支持治疗 2. 恶性肿瘤免疫治 出院日期： 2025年12月06日, bbox=[298, 442, 640, 456]
2026-08-06 10:35:09,864 INFO     30 [qwen-vl-text] coord item[18]: text=疗 3. 肺恶性肿瘤（左肺，小细胞癌广泛期）, bbox=[343, 464, 520, 478]
2026-08-06 10:35:09,864 INFO     30 [qwen-vl-text] coord item[19]: text=4. 肥厚型梗阻性心肌病 5. 纵隔淋巴结肿大, bbox=[343, 487, 527, 501]
2026-08-06 10:35:09,865 INFO     30 [qwen-vl-text] coord item[20]: text=6. 肺门淋巴结肿大 7. 锁骨上淋巴结肿大, bbox=[343, 510, 517, 524]
2026-08-06 10:35:09,865 INFO     30 [qwen-vl-text] coord item[21]: text=(双侧) 8. 腋下淋巴结肿大(右) 9. 心功能, bbox=[343, 533, 523, 547]
2026-08-06 10:35:09,865 INFO     30 [qwen-vl-text] coord item[22]: text=III级(NYHA分级) 10. 甲状腺功能减退症, bbox=[343, 556, 514, 570]
2026-08-06 10:35:09,865 INFO     30 [qwen-vl-text] coord item[23]: text=11. 高血压2级（极高危）12. 肺气肿(局, bbox=[343, 578, 527, 592]
2026-08-06 10:35:09,865 INFO     30 [qwen-vl-text] coord item[24]: text=限性) 13. 肺诊断性影像检查的异常所见(肺, bbox=[343, 601, 527, 615]
2026-08-06 10:35:09,865 INFO     30 [qwen-vl-text] coord item[25]: text=结节) 14. 二尖瓣反流(重度) 15. 心包积, bbox=[343, 624, 520, 638]
2026-08-06 10:35:09,865 INFO     30 [qwen-vl-text] coord item[26]: text=液(少量) 16. 肾上腺结节(左侧), bbox=[343, 647, 480, 661]
2026-08-06 10:35:09,865 INFO     30 [qwen-vl-text] coord item[27]: text=入院时情况（主要症状、体征，有关实验室及器械检查结果）：, bbox=[298, 661, 523, 675]
2026-08-06 10:35:09,865 INFO     30 [qwen-vl-text] coord item[28]: text=患者因“咳嗽1月余”于2025-05-21至河北省人民医院就诊，查胸部CT：左肺下叶占位性病变，恶性不除, bbox=[295, 678, 701, 692]
2026-08-06 10:35:09,865 INFO     30 [qwen-vl-text] coord item[29]: text=外，远端阻塞性肺炎，建议完善实验室检查及增强CT。双侧锁骨窝、右侧腋下、纵隔内及双肺门多发肿大, bbox=[295, 701, 701, 715]
2026-08-06 10:35:09,865 INFO     30 [qwen-vl-text] coord item[30]: text=淋巴结，转移不除外。左侧胸膜结节样增厚，转移不除外。后于2025-05-23行肺穿刺活检术，术后病理回, bbox=[295, 724, 701, 738]
2026-08-06 10:35:09,865 INFO     30 [qwen-vl-text] coord item[31]: text=示：（左肺）穿刺组织：结合免疫组化染色支持小细胞癌。免疫组化染色： CKpan (+)，Vimentin (-)，, bbox=[295, 747, 701, 761]
2026-08-06 10:35:09,865 INFO     30 [qwen-vl-text] coord item[32]: text=CK7 (+)，TTF -1(+)，NapsinA (-)，CK5/6(-)，P40(-)，P63(-)，CgA (+)，Syn (+)，CD56(+)。根据患者病情, bbox=[295, 770, 701, 784]
2026-08-06 10:35:09,865 INFO     30 [qwen-vl-text] coord item[33]: text=于2025-05-28当地医院行依托泊苷+卡铂方案化疗+斯鲁利单抗免疫治疗1周期，过程顺利。于, bbox=[295, 793, 701, 807]
2026-08-06 10:35:09,865 INFO     30 [qwen-vl-text] coord item[34]: text=2025-06-19、2025-07-16开始行依托泊苷+卡铂化疗+斯鲁利单抗免疫治疗2周期，过程顺利。2025-07-27复, bbox=[295, 816, 701, 830]
2026-08-06 10:35:09,865 INFO     30 [qwen-vl-text] coord item[35]: text=查血常规示血小板38×10^9/L。予升血小板治疗后。2025-08-13、2025-09-06、2025-10-08、2025-11-07, bbox=[295, 839, 701, 853]
2026-08-06 10:35:09,866 INFO     30 [qwen-vl-text] coord item[36]: text=行依托泊苷化疗+斯鲁利单抗免疫治疗4周期，期间疗效评价PR。患者为求进一步治疗就诊我科，门诊拟, bbox=[295, 861, 701, 875]
2026-08-06 10:35:09,866 INFO     30 [qwen-vl-text] coord item[37]: text=第 1 页, bbox=[471, 912, 515, 924]
2026-08-06 10:35:09,866 INFO     30 [qwen-vl-text] page=1 — 38/38 coords, api_time=21.0s
2026-08-06 10:35:09,870 INFO     30 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1058415, prompt_len=2113
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共36行）
["南京鼓楼医院", "南京大学医学院附属鼓楼医院", "出院记录", "科别（江北）综合肿瘤中心 病区（江北）B7病区床号 姓名 住院号", "“肺恶性肿瘤”收住入院。病程中，患者神志清，精神可，食纳睡眠可，二便如常，近期体重未见明显变", "化。", "诊疗经过：", "患者入院完善相关检查：", "【检验】", "2025.12.03 12:22 甲功三项：*促甲状腺激素 34.210 mIU/L↑，*游离三碘甲状腺原氨酸 2.60 pmol/L↓，", "*游离甲状腺素 9.58 pmol/L↓。", "2025.12.03 12:22 肺癌六项（江北）：*细胞角蛋白19片段 3.61 ng/mL↑，*神经元特异性烯醇化酶", "26.80 ng/mL↑，胃泌素释放肽前体 243.00 pg/mL↑。", "2025.12.03 13:33 生化全套，心肌酶：*碱性磷酸酶 46.8 U/L↓，*葡萄糖 6.66 mmol/L↑，*甘油三酯", "8.26 mmol/L↑，*总胆固醇 7.14 mmol/L↑，*H-脂蛋白胆固醇 0.90 mmol/L↓，*L-脂蛋白胆固醇 3.51", "mmol/L↑，*载脂蛋白AⅠ 0.79 g/L↓，*载脂蛋白B 1.87 g/L↑，*钠 136.1 mmol/L↓，*氯 97.8", "mmol/L↓，*α羟丁酸脱氢酶 158 U/L↑，eGFR(CKD-EPI) 77.2 ml/min/1.73m^2↓。", "2025.12.03 14:45 血常规：淋巴细胞百分数 19.7 %↓，淋巴细胞绝对值 0.8 ×10^9/L↓，*红细胞计数", "3.30 ×10^12/L↓，*血红蛋白量 108 g/L↓，*红细胞压积 31.8 %↓，红细胞体积分布宽度 15.4 %↑，*", "血小板计数 112 ×10^9/L↓。", "余未见明显异常。", "【检查】", "2025.12.04 15:19 心电图检查（江北）（检查）常规心电图 检查结论 窦性心律一度房室传导阻滞左前分支", "阻滞异常Q波(V1、V2)左心室高电压ST-T改变QTc间期延长", "2025.12.04 16:29（江北）PET/CT(检查) PET/CT全身显像 检查结论 1.“左肺癌化疗后复查”；①左下肺", "门稍大伴葡萄糖代谢增高灶，内部通行支气管狭窄，结合病史考虑符合小细胞癌表现；②左肺下叶两枚软", "组织结节，葡萄糖代谢异常增高；双肺门、纵隔、右侧腋窝多发肿大淋巴结，葡萄糖代谢显著增高；以上", "考虑同侧肺内转移、多发淋巴结转移；2.双肺多发小结节，部分为磨玻璃结节，葡萄糖代谢未见增高，建", "议胸部CT随诊；双肺散在条索及渗出；左肺下叶节段性肺不张；右肺局限性肺气肿；双侧胸膜增厚；3.左", "肾上腺稍低密度结节，葡萄糖代谢未见异常增高，左肾上腺稍增粗，葡萄糖代谢轻度增高，倾向增生伴腺", "瘤形成，请比对老片、密切随诊观察；4.腔隙性脑梗死可能；脑萎缩；副鼻窦炎症；甲状腺左右两叶密度", "欠均，葡萄糖代谢增高，考虑炎性摄取增高，必要时请结合甲功、颈部超声随诊；5.心影偏大，冠状动脉", "及胸部大血管管壁钙化；6.食管中下段管壁似稍增厚，葡萄糖代谢轻度增高，考虑炎性或生理性摄取可", "能，必要时内镜检查；十二指肠憩室可能；轻度脂肪肝；肝囊肿；胆囊饱满；7.慢性膀胱炎症可能；盆腔", "内钙化结节；8.颈椎生理性曲度变直，脊柱退变；右股骨下段低密度伴内部钙化，葡萄糖代谢不高，考虑", "第 2 页"]

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
2026-08-06 10:35:16,675 INFO     30 [qwen-vl-parser] table API response (len=43275):
\begin{tabular}{ccccccccc}
\hline
\textbf{英文} & \textbf{项目名称} & \textbf{结果} & \textbf{提示} & \textbf{参考范围} & \textbf{单位} & \textbf{英文} & \textbf{项目名称} & \textbf{结果} & \textbf{提示} & \textbf{参考范围} & \textbf{单位} \\
\hline
{[TBIL]}总胆红素 & & 8.7 & & 0.0~21.0 & \textmu mol/L & {[Cl]}氯 & & 105 & & 99~110 & mmol/L \\
{[DBIL]}直接胆红素 & & 3.5 & & 0.0~8.0 & \textmu mol/L & {[Ca]}钙 & & 2.38 & & 2.11~2.52 & mmol/L \\
{[IBIL]}间接胆红素 & & 5.2 & & 0.0~13.0 & \textmu mol/L & {[CO2cp]}二氧化碳结合力 & & 27.6 & & 21.0~31.0 & mmol/L \\
{[ALT]}谷丙转氨酶 & & 7.0 & & 7~40 & U/L & {[m-AST]}谷草转氨酶线粒体同工酶 & & 2.0 & & 0~18 & U/L \\
{[AST]}谷草转氨酶 & & 15 & & 13~35 & U/L & {[CK]}肌酸激酶 & & 37 & & 24~200 & U/L \\
{[AST/ALT]}谷草/谷丙 & 2.14 & & \textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\
2026-08-06 10:35:16,679 INFO     30 [qwen-vl-parser] page=48 table: 11 LaTeX lines (bbox 2266-2276)
2026-08-06 10:35:16,679 INFO     30 [qwen-vl-parser] page=48 table: 11 sections
2026-08-06 10:35:17,034 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1378163, prompt_len=764
2026-08-06 10:35:18,938 INFO     30 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-15"
}
```
2026-08-06 10:35:18,939 INFO     30 [qwen-vl-parser] page=49 classify=table report_date=2026-01-15
2026-08-06 10:35:18,973 INFO     30 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1378163, prompt_len=756
2026-08-06 10:35:23,353 INFO     30 [qwen-vl-parser] table API response (len=659):
\begin{tabular}{ccccccccc}
\hline
英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 \\
\hline
[颜色]颜色 & 黄色 & & & 黄、淡黄 & & [SG]尿比重 & 1.020 & 1.003~ \\
[浊度]浊度 & 清亮 & & & 清 & & [VC]维生素C & 0.0 & - \\
[GLU]葡萄糖 & - & & & - & & [WBC]白细胞 & 28.00 & 0~28 \\
[NQX]尿潜血 & - & & & - & mg/l & [RBC]红细胞 & 6.00 & 0~17 \\
[LEU]白细胞 & - & & & - & & [粘液丝]粘液丝 & 11 & 0~28 \\
[PRO]尿蛋白 & - & & & - & & [结晶]结晶 & 0.0 & 0~28 \\
[NIT]亚硝酸盐 & + & & & - & & [管型]管型 & 0 & 0~2 \\
[URO]尿胆原 & - & & & - & & [EC]上皮细胞 & 39.00 & 0~34 \\
[BIL]胆红素 & - & & & - & & [BACT细菌]细菌 & 163.00 & 0~7 \\
[KET]尿酮体 & - & & & - & & [BYST真菌]真菌 & 0 & 0~1 \\
[pH]pH值 & 6.0 & & & 4.5~8.0 & & & & \\
\hline
\end{tabular}
2026-08-06 10:35:23,355 INFO     30 [qwen-vl-parser] page=49 table: 18 LaTeX lines (bbox 2277-2294)
2026-08-06 10:35:23,355 INFO     30 [qwen-vl-parser] page=49 table: 18 sections
2026-08-06 10:35:23,642 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=814682, prompt_len=764
2026-08-06 10:35:25,150 INFO     30 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-15"
}
```
2026-08-06 10:35:25,151 INFO     30 [qwen-vl-parser] page=50 classify=table report_date=2026-01-15
2026-08-06 10:35:25,197 INFO     30 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=814682, prompt_len=756
2026-08-06 10:35:26,931 INFO     30 [qwen-vl-parser] table API response (len=245):
\begin{tabular}{ccccccc}
\hline
英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\
\hline
[FT3]游离三碘甲状腺原氨酸 & & 3.11 & & 2.14~4.21 & pg/mL \\
[FR T4]游离甲状腺素 & & 0.76 & & 0.61~1.12 & ng/dL \\
[fTSH3]超敏促甲状腺素 & & 1.350 & & 0.560~5.910 & uIU/ml \\
\hline
\end{tabular}
2026-08-06 10:35:26,932 INFO     30 [qwen-vl-parser] page=50 table: 10 LaTeX lines (bbox 2295-2304)
2026-08-06 10:35:26,932 INFO     30 [qwen-vl-parser] page=50 table: 10 sections
2026-08-06 10:35:27,221 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1044406, prompt_len=764
2026-08-06 10:35:28,842 INFO     30 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-15"
}
```
2026-08-06 10:35:28,843 INFO     30 [qwen-vl-parser] page=51 classify=table report_date=2026-01-15
2026-08-06 10:35:28,862 INFO     30 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1044406, prompt_len=756
2026-08-06 10:35:31,047 INFO     30 [qwen-vl-text] coord API raw response (len=2979):
[
	{"text": "南京鼓楼医院", "bbox": [462, 109, 536, 125]},
	{"text": "南京大学医学院附属鼓楼医院", "bbox": [420, 132, 579, 148]},
	{"text": "出院记录", "bbox": [440, 152, 558, 175]},
	{"text": "科别（江北）综合肿瘤中心 病区（江北）B7病区床号 姓名 住院号", "bbox": [307, 180, 631, 195]},
	{"text": "“肺恶性肿瘤”收住入院。病程中，患者神志清，精神可，食纳睡眠可，二便如常，近期体重未见明显变", "bbox": [307, 207, 690, 221]},
	{"text": "化。", "bbox": [307, 230, 320, 243]},
	{"text": "诊疗经过：", "bbox": [307, 245, 343, 258]},
	{"text": "患者入院完善相关检查：", "bbox": [307, 264, 392, 277]},
	{"text": "【检验】", "bbox": [307, 285, 337, 298]},
	{"text": "2025.12.03 12:22 甲功三项：*促甲状腺激素 34.210 mIU/L↑，*游离三碘甲状腺原氨酸 2.60 pmol/L↓，", "bbox": [307, 306, 690, 319]},
	{"text": "*游离甲状腺素 9.58 pmol/L↓。", "bbox": [307, 328, 423, 341]},
	{"text": "2025.12.03 12:22 肺癌六项（江北）：*细胞角蛋白19片段 3.61 ng/mL↑，*神经元特异性烯醇化酶", "bbox": [307, 349, 690, 363]},
	{"text": "26.80 ng/mL↑，胃泌素释放肽前体 243.00 pg/mL↑。", "bbox": [307, 371, 500, 384]},
	{"text": "2025.12.03 13:33 生化全套，心肌酶：*碱性磷酸酶 46.8 U/L↓，*葡萄糖 6.66 mmol/L↑，*甘油三酯", "bbox": [307, 392, 690, 405]},
	{"text": "8.26 mmol/L↑，*总胆固醇 7.14 mmol/L↑，*H-脂蛋白胆固醇 0.90 mmol/L↓，*L-脂蛋白胆固醇 3.51", "bbox": [307, 414, 690, 427]},
	{"text": "mmol/L↑，*载脂蛋白AⅠ 0.79 g/L↓，*载脂蛋白B 1.87 g/L↑，*钠 136.1 mmol/L↓，*氯 97.8", "bbox": [307, 435, 690, 448]},
	{"text": "mmol/L↓，*α羟丁酸脱氢酶 158 U/L↑，eGFR(CKD-EPI) 77.2 ml/min/1.73m^2↓。", "bbox": [307, 457, 605, 470]},
	{"text": "2025.12.03 14:45 血常规：淋巴细胞百分数 19.7 %↓，淋巴细胞绝对值 0.8 ×10^9/L↓，*红细胞计数", "bbox": [307, 478, 690, 491]},
	{"text": "3.30 ×10^12/L↓，*血红蛋白量 108 g/L↓，*红细胞压积 31.8 %↓，红细胞体积分布宽度 15.4 %↑，*", "bbox": [307, 499, 690, 512]},
	{"text": "血小板计数 112 ×10^9/L↓。", "bbox": [307, 520, 414, 533]},
	{"text": "余未见明显异常。", "bbox": [307, 541, 369, 554]},
	{"text": "【检查】", "bbox": [307, 563, 337, 576]},
	{"text": "2025.12.04 15:19 心电图检查（江北）（检查）常规心电图 检查结论 窦性心律一度房室传导阻滞左前分支", "bbox": [307, 584, 690, 597]},
	{"text": "阻滞异常Q波(V1、V2)左心室高电压ST-T改变QTc间期延长", "bbox": [307, 605, 511, 618]},
	{"text": "2025.12.04 16:29（江北）PET/CT(检查) PET/CT全身显像 检查结论 1.“左肺癌化疗后复查”；①左下肺", "bbox": [307, 627, 690, 640]},
	{"text": "门稍大伴葡萄糖代谢增高灶，内部通行支气管狭窄，结合病史考虑符合小细胞癌表现；②左肺下叶两枚软", "bbox": [307, 648, 690, 661]},
	{"text": "组织结节，葡萄糖代谢异常增高；双肺门、纵隔、右侧腋窝多发肿大淋巴结，葡萄糖代谢显著增高；以上", "bbox": [307, 670, 690, 683]},
	{"text": "考虑同侧肺内转移、多发淋巴结转移；2.双肺多发小结节，部分为磨玻璃结节，葡萄糖代谢未见增高，建", "bbox": [307, 691, 690, 704]},
	{"text": "议胸部CT随诊；双肺散在条索及渗出；左肺下叶节段性肺不张；右肺局限性肺气肿；双侧胸膜增厚；3.左", "bbox": [307, 712, 690, 725]},
	{"text": "肾上腺稍低密度结节，葡萄糖代谢未见异常增高，左肾上腺稍增粗，葡萄糖代谢轻度增高，倾向增生伴腺", "bbox": [307, 734, 690, 747]},
	{"text": "瘤形成，请比对老片、密切随诊观察；4.腔隙性脑梗死可能；脑萎缩；副鼻窦炎症；甲状腺左右两叶密度", "bbox": [307, 755, 690, 768]},
	{"text": "欠均，葡萄糖代谢增高，考虑炎性摄取增高，必要时请结合甲功、颈部超声随诊；5.心影偏大，冠状动脉", "bbox": [307, 777, 690, 790]},
	{"text": "及胸部大血管管壁钙化；6.食管中下段管壁似稍增厚，葡萄糖代谢轻度增高，考虑炎性或生理性摄取可", "bbox": [307, 798, 690, 811]},
	{"text": "能，必要时内镜检查；十二指肠憩室可能；轻度脂肪肝；肝囊肿；胆囊饱满；7.慢性膀胱炎症可能；盆腔", "bbox": [307, 819, 690, 832]},
	{"text": "内钙化结节；8.颈椎生理性曲度变直，脊柱退变；右股骨下段低密度伴内部钙化，葡萄糖代谢不高，考虑", "bbox": [307, 841, 690, 854]},
	{"text": "第 2 页", "bbox": [473, 879, 514, 891]}
]
2026-08-06 10:35:31,048 INFO     30 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=21.2s
2026-08-06 10:35:31,048 INFO     30 [qwen-vl-text] coord item[0]: text=南京鼓楼医院, bbox=[462, 109, 536, 125]
2026-08-06 10:35:31,049 INFO     30 [qwen-vl-parser] table API response (len=294):
\begin{tabular}{ccccccc}
\hline
英文 & 项目名称 & 结果 & SCO & 提示 & 参考范围 & 单位 \\
\hline
{[HBsAg]}乙肝表面抗原(酶免法) & 阴性 & 0.04 & 阴性 & s/co \\
{[抗-HCV]}丙肝抗体(酶免法) & 阴性 & 0.15 & 阴性 & s/co \\
{[抗-HIV]}人免疫缺陷病毒抗体(酶免法) & 阴性 & 0.06 & 阴性 & s/co \\
{[TP-Ab]}梅毒螺旋体抗体(酶免法) & 阴性 & 0.07 & 阴性 & s/co \\
\hline
\end{tabular}
2026-08-06 10:35:31,050 INFO     30 [qwen-vl-text] coord item[1]: text=南京大学医学院附属鼓楼医院, bbox=[420, 132, 579, 148]
2026-08-06 10:35:31,050 INFO     30 [qwen-vl-text] coord item[2]: text=出院记录, bbox=[440, 152, 558, 175]
2026-08-06 10:35:31,052 INFO     30 [qwen-vl-parser] page=51 table: 11 LaTeX lines (bbox 2305-2315)
2026-08-06 10:35:31,053 INFO     30 [qwen-vl-text] coord item[3]: text=科别（江北）综合肿瘤中心 病区（江北）B7病区床号 姓名 住院号, bbox=[307, 180, 631, 195]
2026-08-06 10:35:31,053 INFO     30 [qwen-vl-parser] page=51 table: 11 sections
2026-08-06 10:35:31,053 INFO     30 [qwen-vl-text] coord item[4]: text=“肺恶性肿瘤”收住入院。病程中，患者神志清，精神可，食纳睡眠可，二便如常，近期体重未见明显变, bbox=[307, 207, 690, 221]
2026-08-06 10:35:31,055 INFO     30 [qwen-vl-text] coord item[5]: text=化。, bbox=[307, 230, 320, 243]
2026-08-06 10:35:31,055 INFO     30 [qwen-vl-text] coord item[6]: text=诊疗经过：, bbox=[307, 245, 343, 258]
2026-08-06 10:35:31,055 INFO     30 [qwen-vl-text] coord item[7]: text=患者入院完善相关检查：, bbox=[307, 264, 392, 277]
2026-08-06 10:35:31,055 INFO     30 [qwen-vl-text] coord item[8]: text=【检验】, bbox=[307, 285, 337, 298]
2026-08-06 10:35:31,056 INFO     30 [qwen-vl-text] coord item[9]: text=2025.12.03 12:22 甲功三项：*促甲状腺激素 34.210 mIU/L↑，*游离三碘甲状腺原氨酸 2.60 pmol/L↓，, bbox=[307, 306, 690, 319]
2026-08-06 10:35:31,056 INFO     30 [qwen-vl-text] coord item[10]: text=*游离甲状腺素 9.58 pmol/L↓。, bbox=[307, 328, 423, 341]
2026-08-06 10:35:31,056 INFO     30 [qwen-vl-text] coord item[11]: text=2025.12.03 12:22 肺癌六项（江北）：*细胞角蛋白19片段 3.61 ng/mL↑，*神经元特异性烯醇化酶, bbox=[307, 349, 690, 363]
2026-08-06 10:35:31,056 INFO     30 [qwen-vl-text] coord item[12]: text=26.80 ng/mL↑，胃泌素释放肽前体 243.00 pg/mL↑。, bbox=[307, 371, 500, 384]
2026-08-06 10:35:31,056 INFO     30 [qwen-vl-text] coord item[13]: text=2025.12.03 13:33 生化全套，心肌酶：*碱性磷酸酶 46.8 U/L↓，*葡萄糖 6.66 mmol/L↑，*甘油三酯, bbox=[307, 392, 690, 405]
2026-08-06 10:35:31,056 INFO     30 [qwen-vl-text] coord item[14]: text=8.26 mmol/L↑，*总胆固醇 7.14 mmol/L↑，*H-脂蛋白胆固醇 0.90 mmol/L↓，*L-脂蛋白胆固醇 3.51, bbox=[307, 414, 690, 427]
2026-08-06 10:35:31,056 INFO     30 [qwen-vl-text] coord item[15]: text=mmol/L↑，*载脂蛋白AⅠ 0.79 g/L↓，*载脂蛋白B 1.87 g/L↑，*钠 136.1 mmol/L↓，*氯 97.8, bbox=[307, 435, 690, 448]
2026-08-06 10:35:31,057 INFO     30 [qwen-vl-text] coord item[16]: text=mmol/L↓，*α羟丁酸脱氢酶 158 U/L↑，eGFR(CKD-EPI) 77.2 ml/min/1.73m^2↓。, bbox=[307, 457, 605, 470]
2026-08-06 10:35:31,057 INFO     30 [qwen-vl-text] coord item[17]: text=2025.12.03 14:45 血常规：淋巴细胞百分数 19.7 %↓，淋巴细胞绝对值 0.8 ×10^9/L↓，*红细胞计数, bbox=[307, 478, 690, 491]
2026-08-06 10:35:31,057 INFO     30 [qwen-vl-text] coord item[18]: text=3.30 ×10^12/L↓，*血红蛋白量 108 g/L↓，*红细胞压积 31.8 %↓，红细胞体积分布宽度 15.4 %↑，*, bbox=[307, 499, 690, 512]
2026-08-06 10:35:31,057 INFO     30 [qwen-vl-text] coord item[19]: text=血小板计数 112 ×10^9/L↓。, bbox=[307, 520, 414, 533]
2026-08-06 10:35:31,057 INFO     30 [qwen-vl-text] coord item[20]: text=余未见明显异常。, bbox=[307, 541, 369, 554]
2026-08-06 10:35:31,057 INFO     30 [qwen-vl-text] coord item[21]: text=【检查】, bbox=[307, 563, 337, 576]
2026-08-06 10:35:31,057 INFO     30 [qwen-vl-text] coord item[22]: text=2025.12.04 15:19 心电图检查（江北）（检查）常规心电图 检查结论 窦性心律一度房室传导阻滞左前分支, bbox=[307, 584, 690, 597]
2026-08-06 10:35:31,057 INFO     30 [qwen-vl-text] coord item[23]: text=阻滞异常Q波(V1、V2)左心室高电压ST-T改变QTc间期延长, bbox=[307, 605, 511, 618]
2026-08-06 10:35:31,057 INFO     30 [qwen-vl-text] coord item[24]: text=2025.12.04 16:29（江北）PET/CT(检查) PET/CT全身显像 检查结论 1.“左肺癌化疗后复查”；①左下肺, bbox=[307, 627, 690, 640]
2026-08-06 10:35:31,057 INFO     30 [qwen-vl-text] coord item[25]: text=门稍大伴葡萄糖代谢增高灶，内部通行支气管狭窄，结合病史考虑符合小细胞癌表现；②左肺下叶两枚软, bbox=[307, 648, 690, 661]
2026-08-06 10:35:31,057 INFO     30 [qwen-vl-text] coord item[26]: text=组织结节，葡萄糖代谢异常增高；双肺门、纵隔、右侧腋窝多发肿大淋巴结，葡萄糖代谢显著增高；以上, bbox=[307, 670, 690, 683]
2026-08-06 10:35:31,057 INFO     30 [qwen-vl-text] coord item[27]: text=考虑同侧肺内转移、多发淋巴结转移；2.双肺多发小结节，部分为磨玻璃结节，葡萄糖代谢未见增高，建, bbox=[307, 691, 690, 704]
2026-08-06 10:35:31,057 INFO     30 [qwen-vl-text] coord item[28]: text=议胸部CT随诊；双肺散在条索及渗出；左肺下叶节段性肺不张；右肺局限性肺气肿；双侧胸膜增厚；3.左, bbox=[307, 712, 690, 725]
2026-08-06 10:35:31,057 INFO     30 [qwen-vl-text] coord item[29]: text=肾上腺稍低密度结节，葡萄糖代谢未见异常增高，左肾上腺稍增粗，葡萄糖代谢轻度增高，倾向增生伴腺, bbox=[307, 734, 690, 747]
2026-08-06 10:35:31,057 INFO     30 [qwen-vl-text] coord item[30]: text=瘤形成，请比对老片、密切随诊观察；4.腔隙性脑梗死可能；脑萎缩；副鼻窦炎症；甲状腺左右两叶密度, bbox=[307, 755, 690, 768]
2026-08-06 10:35:31,057 INFO     30 [qwen-vl-text] coord item[31]: text=欠均，葡萄糖代谢增高，考虑炎性摄取增高，必要时请结合甲功、颈部超声随诊；5.心影偏大，冠状动脉, bbox=[307, 777, 690, 790]
2026-08-06 10:35:31,057 INFO     30 [qwen-vl-text] coord item[32]: text=及胸部大血管管壁钙化；6.食管中下段管壁似稍增厚，葡萄糖代谢轻度增高，考虑炎性或生理性摄取可, bbox=[307, 798, 690, 811]
2026-08-06 10:35:31,057 INFO     30 [qwen-vl-text] coord item[33]: text=能，必要时内镜检查；十二指肠憩室可能；轻度脂肪肝；肝囊肿；胆囊饱满；7.慢性膀胱炎症可能；盆腔, bbox=[307, 819, 690, 832]
2026-08-06 10:35:31,057 INFO     30 [qwen-vl-text] coord item[34]: text=内钙化结节；8.颈椎生理性曲度变直，脊柱退变；右股骨下段低密度伴内部钙化，葡萄糖代谢不高，考虑, bbox=[307, 841, 690, 854]
2026-08-06 10:35:31,057 INFO     30 [qwen-vl-text] coord item[35]: text=第 2 页, bbox=[473, 879, 514, 891]
2026-08-06 10:35:31,058 INFO     30 [qwen-vl-text] page=2 — 36/36 coords, api_time=21.2s
2026-08-06 10:35:31,061 INFO     30 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=854444, prompt_len=1564
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共38行）
["3/4", "南京鼓楼医院", "南京大学医学院附属鼓楼医院", "出院记录", "科别（江北）综合肿瘤中心 病区（江北）B7病区床号", "姓名 住院号", "良性灶如内生软骨瘤可能，随诊；右肩背部皮下稍低密度结节，葡萄糖代谢未见增高，考虑良性灶，随", "诊。", "【诊疗经过】", "患者入院后完善PET-CT复查，病情较前基本相仿，暂无根治性放疗指征。排除禁忌后，患者于2025-12-05", "行斯鲁利单抗免疫维持治疗1周期。现本周期静脉治疗已结束，现整体病情稳定，一般情况尚可，准予办理", "出院。", "出院情况： 好转", "伤口愈合：-", "ECOG 1分，NRS 0分，神志清，精神可，无贫血貌，全身皮肤巩膜无黄染。胸廓外形正常，无胸壁静脉曲", "张。双侧呼吸运动对称，肋间隙：正常，触觉语颤：对称，皮下捻发感：无，双肺叩诊清音，双肺呼吸音", "稍粗，两肺未闻及明显干湿啰音。心律齐，心脏各瓣膜区未闻及杂音。腹部平坦，腹部无压痛，无反跳", "痛。双下肢无明显水肿。", "出院医嘱：", "1、注意天气变化，注意休息、低脂饮食，避免受凉，避免手足接触冰冷物体，注意皮肤保暖。", "2、出院后继续用药", "左甲状腺素钠片（优甲乐）50微克/片 1片 口服 QD（7点）（每天早餐前半小时服用1片，补充甲状腺激", "素，内分泌科随诊调药）", "3、定期复查血常规（每周1-2次）及生化全套（每周1次），如WBC<3.0×10^9/L、PLT<60×10^9/L或生化", "全套指标异常，请及时当地医院就诊（如有急症或危急值报告，请及时就近正规医院急诊就诊），我科门", "诊随诊。", "4、下次治疗时间：3-4周左右，具体等电话通知。杨阳主任医师专家门诊时间：门诊时间：每周二、周五", "上午，（周二本部，周五江北），（江北肿瘤科医生办公室电话：025-83106666转220717）。如需肿瘤日", "间治疗，请提前一周至杨阳主任医师门诊预约。", "5、不适门诊随诊。", "不存在尚未回归的病理检查结果。", "X光片号：-", "CT号： P049684", "MRI号：-", "病理号：-", "上级医师：", "医师：", "第 3 页"]

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
2026-08-06 10:35:31,554 INFO     30 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1042924, prompt_len=764
2026-08-06 10:35:34,373 INFO     30 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-06 10:35:34,373 INFO     30 [qwen-vl-parser] page=52 classify=text report_date=None
2026-08-06 10:35:34,391 INFO     30 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1042924, prompt_len=401
2026-08-06 10:35:36,085 INFO     30 [qwen-vl-parser] text API response (len=169):
["处方笺", "4970401", "姓名：", "性别：□男 □女 年龄：60岁", "科别： 费别： 电话/住址：", "过敏史：无 开具日期：2021年2月16日", "临床诊断：支气管哮喘", "Rp", "孟鲁司特钠片 10mg 2板", "用法：二天一次 1片", "审核： 调配： 医师：", "核对： 发药： 金额："]
2026-08-06 10:35:36,085 INFO     30 [qwen-vl-parser] page=52 text: 12 lines (bbox 2316-2327)
2026-08-06 10:35:36,085 INFO     30 [qwen-vl-parser] page=52 text: 12 sections
2026-08-06 10:35:36,086 INFO     30 [qwen-vl-parser] parse_pdf done: 2328 sections from 52 pages.
2026-08-06 10:35:36,109 INFO     30 Close text detector.
2026-08-06 10:35:37,081 INFO     30 Close text recognizer.
2026-08-06 10:35:38,245 INFO     30 Close recognizer.
2026-08-06 10:35:39,289 INFO     30 Close recognizer.
2026-08-06 10:35:46,742 INFO     30 [qwen-vl-text] coord API raw response (len=2512):
[
	{"text": "3/4", "bbox": [315, 101, 340, 121]},
	{"text": "南京鼓楼医院", "bbox": [462, 102, 537, 118]},
	{"text": "南京大学医学院附属鼓楼医院", "bbox": [418, 124, 582, 141]},
	{"text": "出院记录", "bbox": [439, 145, 561, 169]},
	{"text": "科别（江北）综合肿瘤中心 病区（江北）B7病区床号", "bbox": [303, 176, 510, 190]},
	{"text": "姓名 住院号", "bbox": [544, 176, 635, 190]},
	{"text": "良性灶如内生软骨瘤可能，随诊；右肩背部皮下稍低密度结节，葡萄糖代谢未见增高，考虑良性灶，随", "bbox": [303, 204, 696, 217]},
	{"text": "诊。", "bbox": [303, 226, 316, 239]},
	{"text": "【诊疗经过】", "bbox": [306, 248, 350, 261]},
	{"text": "患者入院后完善PET-CT复查，病情较前基本相仿，暂无根治性放疗指征。排除禁忌后，患者于2025-12-05", "bbox": [303, 270, 696, 283]},
	{"text": "行斯鲁利单抗免疫维持治疗1周期。现本周期静脉治疗已结束，现整体病情稳定，一般情况尚可，准予办理", "bbox": [303, 293, 696, 306]},
	{"text": "出院。", "bbox": [303, 315, 324, 328]},
	{"text": "出院情况： 好转", "bbox": [303, 338, 365, 351]},
	{"text": "伤口愈合：-", "bbox": [515, 338, 562, 351]},
	{"text": "ECOG 1分，NRS 0分，神志清，精神可，无贫血貌，全身皮肤巩膜无黄染。胸廓外形正常，无胸壁静脉曲", "bbox": [303, 360, 696, 373]},
	{"text": "张。双侧呼吸运动对称，肋间隙：正常，触觉语颤：对称，皮下捻发感：无，双肺叩诊清音，双肺呼吸音", "bbox": [303, 382, 696, 395]},
	{"text": "稍粗，两肺未闻及明显干湿啰音。心律齐，心脏各瓣膜区未闻及杂音。腹部平坦，腹部无压痛，无反跳", "bbox": [303, 405, 696, 418]},
	{"text": "痛。双下肢无明显水肿。", "bbox": [303, 427, 392, 440]},
	{"text": "出院医嘱：", "bbox": [304, 444, 340, 456]},
	{"text": "1、注意天气变化，注意休息、低脂饮食，避免受凉，避免手足接触冰冷物体，注意皮肤保暖。", "bbox": [303, 478, 645, 491]},
	{"text": "2、出院后继续用药", "bbox": [303, 501, 374, 514]},
	{"text": "左甲状腺素钠片（优甲乐）50微克/片 1片 口服 QD（7点）（每天早餐前半小时服用1片，补充甲状腺激", "bbox": [303, 523, 696, 536]},
	{"text": "素，内分泌科随诊调药）", "bbox": [303, 545, 391, 558]},
	{"text": "3、定期复查血常规（每周1-2次）及生化全套（每周1次），如WBC<3.0×10^9/L、PLT<60×10^9/L或生化", "bbox": [303, 567, 696, 580]},
	{"text": "全套指标异常，请及时当地医院就诊（如有急症或危急值报告，请及时就近正规医院急诊就诊），我科门", "bbox": [303, 589, 696, 602]},
	{"text": "诊随诊。", "bbox": [303, 612, 332, 625]},
	{"text": "4、下次治疗时间：3-4周左右，具体等电话通知。杨阳主任医师专家门诊时间：门诊时间：每周二、周五", "bbox": [303, 634, 696, 647]},
	{"text": "上午，（周二本部，周五江北），（江北肿瘤科医生办公室电话：025-83106666转220717）。如需肿瘤日", "bbox": [303, 656, 696, 669]},
	{"text": "间治疗，请提前一周至杨阳主任医师门诊预约。", "bbox": [303, 678, 475, 691]},
	{"text": "5、不适门诊随诊。", "bbox": [303, 700, 378, 713]},
	{"text": "不存在尚未回归的病理检查结果。", "bbox": [303, 722, 424, 735]},
	{"text": "X光片号：-", "bbox": [519, 746, 563, 758]},
	{"text": "CT号： P049684", "bbox": [519, 770, 588, 782]},
	{"text": "MRI号：-", "bbox": [519, 792, 563, 805]},
	{"text": "病理号：-", "bbox": [519, 816, 563, 828]},
	{"text": "上级医师：", "bbox": [303, 860, 344, 873]},
	{"text": "医师：", "bbox": [497, 858, 558, 874]},
	{"text": "第 3 页", "bbox": [473, 895, 515, 907]}
]
2026-08-06 10:35:46,743 INFO     30 [qwen-vl-text] coord API: raw_items=38, valid_items=38, elapsed=15.7s
2026-08-06 10:35:46,743 INFO     30 [qwen-vl-text] coord item[0]: text=3/4, bbox=[315, 101, 340, 121]
2026-08-06 10:35:46,744 INFO     30 [qwen-vl-text] coord item[1]: text=南京鼓楼医院, bbox=[462, 102, 537, 118]
2026-08-06 10:35:46,744 INFO     30 [qwen-vl-text] coord item[2]: text=南京大学医学院附属鼓楼医院, bbox=[418, 124, 582, 141]
2026-08-06 10:35:46,744 INFO     30 [qwen-vl-text] coord item[3]: text=出院记录, bbox=[439, 145, 561, 169]
2026-08-06 10:35:46,744 INFO     30 [qwen-vl-text] coord item[4]: text=科别（江北）综合肿瘤中心 病区（江北）B7病区床号, bbox=[303, 176, 510, 190]
2026-08-06 10:35:46,744 INFO     30 [qwen-vl-text] coord item[5]: text=姓名 住院号, bbox=[544, 176, 635, 190]
2026-08-06 10:35:46,744 INFO     30 [qwen-vl-text] coord item[6]: text=良性灶如内生软骨瘤可能，随诊；右肩背部皮下稍低密度结节，葡萄糖代谢未见增高，考虑良性灶，随, bbox=[303, 204, 696, 217]
2026-08-06 10:35:46,744 INFO     30 [qwen-vl-text] coord item[7]: text=诊。, bbox=[303, 226, 316, 239]
2026-08-06 10:35:46,745 INFO     30 [qwen-vl-text] coord item[8]: text=【诊疗经过】, bbox=[306, 248, 350, 261]
2026-08-06 10:35:46,745 INFO     30 [qwen-vl-text] coord item[9]: text=患者入院后完善PET-CT复查，病情较前基本相仿，暂无根治性放疗指征。排除禁忌后，患者于2025-12-05, bbox=[303, 270, 696, 283]
2026-08-06 10:35:46,745 INFO     30 [qwen-vl-text] coord item[10]: text=行斯鲁利单抗免疫维持治疗1周期。现本周期静脉治疗已结束，现整体病情稳定，一般情况尚可，准予办理, bbox=[303, 293, 696, 306]
2026-08-06 10:35:46,745 INFO     30 [qwen-vl-text] coord item[11]: text=出院。, bbox=[303, 315, 324, 328]
2026-08-06 10:35:46,745 INFO     30 [qwen-vl-text] coord item[12]: text=出院情况： 好转, bbox=[303, 338, 365, 351]
2026-08-06 10:35:46,746 INFO     30 [qwen-vl-text] coord item[13]: text=伤口愈合：-, bbox=[515, 338, 562, 351]
2026-08-06 10:35:46,746 INFO     30 [qwen-vl-text] coord item[14]: text=ECOG 1分，NRS 0分，神志清，精神可，无贫血貌，全身皮肤巩膜无黄染。胸廓外形正常，无胸壁静脉曲, bbox=[303, 360, 696, 373]
2026-08-06 10:35:46,746 INFO     30 [qwen-vl-text] coord item[15]: text=张。双侧呼吸运动对称，肋间隙：正常，触觉语颤：对称，皮下捻发感：无，双肺叩诊清音，双肺呼吸音, bbox=[303, 382, 696, 395]
2026-08-06 10:35:46,746 INFO     30 [qwen-vl-text] coord item[16]: text=稍粗，两肺未闻及明显干湿啰音。心律齐，心脏各瓣膜区未闻及杂音。腹部平坦，腹部无压痛，无反跳, bbox=[303, 405, 696, 418]
2026-08-06 10:35:46,746 INFO     30 [qwen-vl-text] coord item[17]: text=痛。双下肢无明显水肿。, bbox=[303, 427, 392, 440]
2026-08-06 10:35:46,746 INFO     30 [qwen-vl-text] coord item[18]: text=出院医嘱：, bbox=[304, 444, 340, 456]
2026-08-06 10:35:46,746 INFO     30 [qwen-vl-text] coord item[19]: text=1、注意天气变化，注意休息、低脂饮食，避免受凉，避免手足接触冰冷物体，注意皮肤保暖。, bbox=[303, 478, 645, 491]
2026-08-06 10:35:46,746 INFO     30 [qwen-vl-text] coord item[20]: text=2、出院后继续用药, bbox=[303, 501, 374, 514]
2026-08-06 10:35:46,746 INFO     30 [qwen-vl-text] coord item[21]: text=左甲状腺素钠片（优甲乐）50微克/片 1片 口服 QD（7点）（每天早餐前半小时服用1片，补充甲状腺激, bbox=[303, 523, 696, 536]
2026-08-06 10:35:46,746 INFO     30 [qwen-vl-text] coord item[22]: text=素，内分泌科随诊调药）, bbox=[303, 545, 391, 558]
2026-08-06 10:35:46,746 INFO     30 [qwen-vl-text] coord item[23]: text=3、定期复查血常规（每周1-2次）及生化全套（每周1次），如WBC<3.0×10^9/L、PLT<60×10^9/L或生化, bbox=[303, 567, 696, 580]
2026-08-06 10:35:46,746 INFO     30 [qwen-vl-text] coord item[24]: text=全套指标异常，请及时当地医院就诊（如有急症或危急值报告，请及时就近正规医院急诊就诊），我科门, bbox=[303, 589, 696, 602]
2026-08-06 10:35:46,746 INFO     30 [qwen-vl-text] coord item[25]: text=诊随诊。, bbox=[303, 612, 332, 625]
2026-08-06 10:35:46,746 INFO     30 [qwen-vl-text] coord item[26]: text=4、下次治疗时间：3-4周左右，具体等电话通知。杨阳主任医师专家门诊时间：门诊时间：每周二、周五, bbox=[303, 634, 696, 647]
2026-08-06 10:35:46,746 INFO     30 [qwen-vl-text] coord item[27]: text=上午，（周二本部，周五江北），（江北肿瘤科医生办公室电话：025-83106666转220717）。如需肿瘤日, bbox=[303, 656, 696, 669]
2026-08-06 10:35:46,747 INFO     30 [qwen-vl-text] coord item[28]: text=间治疗，请提前一周至杨阳主任医师门诊预约。, bbox=[303, 678, 475, 691]
2026-08-06 10:35:46,747 INFO     30 [qwen-vl-text] coord item[29]: text=5、不适门诊随诊。, bbox=[303, 700, 378, 713]
2026-08-06 10:35:46,747 INFO     30 [qwen-vl-text] coord item[30]: text=不存在尚未回归的病理检查结果。, bbox=[303, 722, 424, 735]
2026-08-06 10:35:46,747 INFO     30 [qwen-vl-text] coord item[31]: text=X光片号：-, bbox=[519, 746, 563, 758]
2026-08-06 10:35:46,747 INFO     30 [qwen-vl-text] coord item[32]: text=CT号： P049684, bbox=[519, 770, 588, 782]
2026-08-06 10:35:46,747 INFO     30 [qwen-vl-text] coord item[33]: text=MRI号：-, bbox=[519, 792, 563, 805]
2026-08-06 10:35:46,747 INFO     30 [qwen-vl-text] coord item[34]: text=病理号：-, bbox=[519, 816, 563, 828]
2026-08-06 10:35:46,747 INFO     30 [qwen-vl-text] coord item[35]: text=上级医师：, bbox=[303, 860, 344, 873]
2026-08-06 10:35:46,747 INFO     30 [qwen-vl-text] coord item[36]: text=医师：, bbox=[497, 858, 558, 874]
2026-08-06 10:35:46,747 INFO     30 [qwen-vl-text] coord item[37]: text=第 3 页, bbox=[473, 895, 515, 907]
2026-08-06 10:35:46,748 INFO     30 [qwen-vl-text] page=3 — 38/38 coords, api_time=15.7s
2026-08-06 10:35:46,749 INFO     30 [qwen-vl-text] new_positions (115):
[[0, 256.7764544677734, 395.6883068847656, 150.60482824707032, 162.51034826660157], [0, 256.7764544677734, 496.7151086425781, 162.51034826660157, 174.41586828613282], [0, 256.7764544677734, 467.2489581298828, 174.41586828613282, 186.32138830566407], [1, 387.26940673828125, 452.93682788085937, 55.95594409179688, 66.07563610839844], [1, 349.38435607910156, 491.6637685546875, 69.64729211425781, 79.76698413085938], [1, 367.06404638671876, 473.14218823242186, 82.7433641357422, 97.62526416015625], [1, 248.35755432128906, 472.30029821777345, 101.19692016601563, 109.5307841796875], [1, 512.7110189208985, 537.1258293457031, 101.19692016601563, 109.5307841796875], [1, 248.35755432128906, 267.72102465820313, 117.86464819335939, 125.60323620605469], [1, 307.2898553466797, 506.81778881835936, 117.86464819335939, 125.60323620605469], [1, 250.88322436523438, 538.809609375, 135.12765222167968, 143.46151623535158], [1, 288.76827502441404, 443.67603771972654, 148.81900024414062, 157.1528642578125], [1, 288.76827502441404, 443.67603771972654, 162.51034826660157, 170.84421228027344], [1, 288.76827502441404, 442.8341477050781, 176.2016962890625, 184.53556030273438], [1, 288.76827502441404, 443.67603771972654, 189.89304431152345, 198.22690832519532], [1, 288.76827502441404, 443.67603771972654, 203.5843923339844, 211.91825634765627], [1, 288.76827502441404, 443.67603771972654, 217.2757403564453, 225.6096043701172], [1, 288.76827502441404, 430.2057974853516, 230.96708837890625, 239.30095239257813], [1, 250.88322436523438, 284.55882495117186, 247.03954040527344, 254.77812841796876], [1, 447.0435977783203, 477.35163830566404, 247.03954040527344, 254.77812841796876], [1, 250.88322436523438, 538.809609375, 263.11199243164066, 271.44585644531253], [1, 288.76827502441404, 437.7828076171875, 276.208064453125, 284.5419284667969], [1, 288.76827502441404, 443.67603771972654, 289.89941247558596, 298.23327648925783], [1, 288.76827502441404, 435.2571375732422, 303.5907604980469, 311.9246245117188], [1, 288.76827502441404, 440.3084776611328, 317.28210852050785, 325.6159725341797], [1, 288.76827502441404, 432.7314675292969, 330.9734565429688, 339.30732055664066], [1, 288.76827502441404, 443.67603771972654, 344.06952856445315, 352.403392578125], [1, 288.76827502441404, 443.67603771972654, 357.7608765869141, 366.09474060058596], [1, 288.76827502441404, 437.7828076171875, 371.45222460937504, 379.7860886230469], [1, 288.76827502441404, 404.10720703124997, 385.143572631836, 393.47743664550785], [1, 250.88322436523438, 440.3084776611328, 393.47743664550785, 401.8113006591797], [1, 248.35755432128906, 590.1649002685547, 403.5971286621094, 411.9309926757813], [1, 248.35755432128906, 590.1649002685547, 417.28847668457036, 425.6223406982422], [1, 248.35755432128906, 590.1649002685547, 430.97982470703124, 439.31368872070317], [1, 248.35755432128906, 590.1649002685547, 444.6711727294922, 453.00503674316406], [1, 248.35755432128906, 590.1649002685547, 458.3625207519531, 466.696384765625], [1, 248.35755432128906, 590.1649002685547, 472.05386877441407, 480.38773278808594], [1, 248.35755432128906, 590.1649002685547, 485.745216796875, 494.0790808105469], [1, 248.35755432128906, 590.1649002685547, 499.43656481933596, 507.7704288330078], [1, 248.35755432128906, 590.1649002685547, 512.5326368408204, 520.8665008544922], [1, 396.5301968994141, 433.5733575439453, 542.8917128906251, 550.0350249023438], [2, 388.95318676757813, 451.2530478515625, 64.88508410644532, 74.40950012207031], [2, 353.59380615234375, 487.4543184814453, 78.57643212890625, 88.10084814453126], [2, 370.43160644531247, 469.7746281738281, 90.4819521484375, 104.17330017089844], [2, 258.4602344970703, 531.232599243164, 107.14968017578126, 116.0788201904297], [2, 258.4602344970703, 580.9041101074218, 123.22213220214844, 131.55599621582033], [2, 258.4602344970703, 269.4048046875, 136.91348022460937, 144.6520682373047], [2, 258.4602344970703, 288.76827502441404, 145.84262023925783, 153.58120825195314], [2, 258.4602344970703, 330.0208857421875, 157.1528642578125, 164.8914522705078], [2, 258.4602344970703, 283.71693493652344, 169.65366027832033, 177.39224829101562], [2, 258.4602344970703, 580.9041101074218, 182.15445629882814, 189.89304431152345], [2, 258.4602344970703, 356.11947619628904, 195.2505283203125, 202.98911633300781], [2, 258.4602344970703, 580.9041101074218, 207.75132434082033, 216.0851883544922], [2, 258.4602344970703, 420.94500732421875, 220.8473963623047, 228.585984375], [2, 258.4602344970703, 580.9041101074218, 233.3481923828125, 241.08678039550782], [2, 258.4602344970703, 580.9041101074218, 246.4442644042969, 254.1828524169922], [2, 258.4602344970703, 580.9041101074218, 258.9450604248047, 266.6836484375], [2, 258.4602344970703, 509.34345886230466, 272.04113244628905, 279.7797204589844], [2, 258.4602344970703, 580.9041101074218, 284.5419284667969, 292.2805164794922], [2, 258.4602344970703, 580.9041101074218, 297.0427244873047, 304.7813125], [2, 258.4602344970703, 348.5424660644531, 309.5435205078125, 317.28210852050785], [2, 258.4602344970703, 310.6574154052734, 322.04431652832034, 329.7829045410156], [2, 258.4602344970703, 283.71693493652344, 335.1403885498047, 342.87897656250004], [2, 258.4602344970703, 580.9041101074218, 347.64118457031253, 355.3797725830078], [2, 258.4602344970703, 430.2057974853516, 360.1419805908203, 367.88056860351566], [2, 258.4602344970703, 580.9041101074218, 373.2380526123047, 380.976640625], [2, 258.4602344970703, 580.9041101074218, 385.7388486328125, 393.47743664550785], [2, 258.4602344970703, 580.9041101074218, 398.83492065429687, 406.5735086669922], [2, 258.4602344970703, 580.9041101074218, 411.3357166748047, 419.0743046875], [2, 258.4602344970703, 580.9041101074218, 423.83651269531254, 431.5751007080078], [2, 258.4602344970703, 580.9041101074218, 436.9325847167969, 444.6711727294922], [2, 258.4602344970703, 580.9041101074218, 449.43338073730473, 457.17196875], [2, 258.4602344970703, 580.9041101074218, 462.5294527587891, 470.2680407714844], [2, 258.4602344970703, 580.9041101074218, 475.03024877929687, 482.7688367919922], [2, 258.4602344970703, 580.9041101074218, 487.5310447998047, 495.26963281250005], [2, 258.4602344970703, 580.9041101074218, 500.62711682128906, 508.3657048339844], [2, 398.2139769287109, 432.7314675292969, 523.2476048583984, 530.3909168701172], [3, 265.19535461425784, 286.24260498046874, 60.122876098632815, 72.02839611816407], [3, 388.95318676757813, 452.09493786621096, 60.71815209960938, 70.24256811523438], [3, 351.91002612304686, 489.97998852539064, 73.81422412109376, 83.93391613769532], [3, 369.58971643066405, 472.30029821777345, 86.31502014160156, 100.60164416503906], [3, 255.09267443847656, 429.3639074707031, 104.768576171875, 113.10244018554688], [3, 457.98816796875, 534.6001593017578, 104.768576171875, 113.10244018554688], [3, 255.09267443847656, 585.9554501953124, 121.43630419921875, 129.17489221191406], [3, 255.09267443847656, 266.03724462890625, 134.53237622070313, 142.27096423339844], [3, 257.6183444824219, 294.6615051269531, 147.62844824218752, 155.3670362548828], [3, 255.09267443847656, 585.9554501953124, 160.72452026367188, 168.4631082763672], [3, 255.09267443847656, 585.9554501953124, 174.41586828613282, 182.15445629882814], [3, 255.09267443847656, 272.77236474609373, 187.5119403076172, 195.2505283203125], [3, 255.09267443847656, 307.2898553466797, 201.20328833007812, 208.94187634277344], [3, 433.5733575439453, 473.14218823242186, 201.20328833007812, 208.94187634277344], [3, 255.09267443847656, 585.9554501953124, 214.2993603515625, 222.03794836425783], [3, 255.09267443847656, 585.9554501953124, 227.39543237304687, 235.1340203857422], [3, 255.09267443847656, 585.9554501953124, 241.08678039550782, 248.82536840820313], [3, 255.09267443847656, 330.0208857421875, 254.1828524169922, 261.9214404296875], [3, 255.934564453125, 286.24260498046874, 264.30254443359377, 271.44585644531253], [3, 255.09267443847656, 543.0190594482422, 284.5419284667969, 292.2805164794922], [3, 255.09267443847656, 314.86686547851565, 298.23327648925783, 305.9718645019531], [3, 255.09267443847656, 585.9554501953124, 311.3293485107422, 319.06793652343754], [3, 255.09267443847656, 329.1789957275391, 324.42542053222655, 332.1640085449219], [3, 255.09267443847656, 585.9554501953124, 337.52149255371097, 345.26008056640626], [3, 255.09267443847656, 585.9554501953124, 350.61756457519533, 358.3561525878906], [3, 255.09267443847656, 279.50748486328126, 364.3089125976563, 372.04750061035156], [3, 255.09267443847656, 585.9554501953124, 377.40498461914063, 385.143572631836], [3, 255.09267443847656, 585.9554501953124, 390.501056640625, 398.23964465332034], [3, 255.09267443847656, 399.8977569580078, 403.5971286621094, 411.3357166748047], [3, 255.09267443847656, 318.23442553710936, 416.6932006835938, 424.43178869628906], [3, 255.09267443847656, 356.9613662109375, 429.78927270507813, 437.5278607177735], [3, 436.94091760253906, 473.98407824707033, 444.07589672851566, 451.2192087402344], [3, 436.94091760253906, 495.03132861328123, 458.3625207519531, 465.5058327636719], [3, 436.94091760253906, 473.98407824707033, 471.45859277343754, 479.19718078613283], [3, 436.94091760253906, 473.98407824707033, 485.745216796875, 492.8885288085938], [3, 255.09267443847656, 289.6101650390625, 511.9373608398438, 519.6759488525391], [3, 418.41933728027345, 469.7746281738281, 510.7468088378906, 520.2712248535156], [3, 398.2139769287109, 433.5733575439453, 532.7720208740235, 539.9153328857423]]
2026-08-06 10:35:46,749 INFO     30 [qwen-vl-text] ═══ DONE ═══ 115 positions, pages=4, time=97.9s
2026-08-06 10:35:46,807 INFO     30 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-06 10:35:46,807 INFO     30 [Trace] task=dfc102e2 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | Extractor:Discharge | outputs={"chunks": "1 items, types={'DischargeRecord': 1}", "html": "", "json": "458 items", "markdown": "", "text": "", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 4, \"chunks_Clinical\": 1, \"chunks_LabExam\": 2}"}
2026-08-06 10:35:46,808 INFO     30 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-06 10:35:46,810 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:35:46.808+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 8, "lag": 0, "done": 1, "failed": 0, "current": {"00b9d592918111f18dbe1f8f96f1c395": {"id": "00b9d592918111f18dbe1f8f96f1c395", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011867426, "task_type": "dataflow", "root_trace_id": "1ab3198c92574fb4b2701d0f5db7322f", "root_traceparent": "00-1ab3198c92574fb4b2701d0f5db7322f-bdaff6f64a5f4a64-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "dfc102e2918111f18dbe1f8f96f1c395": {"id": "dfc102e2918111f18dbe1f8f96f1c395", "doc_id": "de8a02fc918111f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786012241604, "task_type": "dataflow", "root_trace_id": "90f550f6b00248c3845d57a8e0bcf6fb", "root_traceparent": "00-90f550f6b00248c3845d57a8e0bcf6fb-5db7fb7d470dfe0d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:35:46,830 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:35:46,830 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-06 10:35:47,167 INFO     30 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-06 10:35:47,168 INFO     30 [Trace] task=00b9d592 | doc=DAXI-哮喘.pdf | Parser:MedLink | outputs={"html": "", "json": "2328 items", "markdown": "", "text": "", "name": "DAXI-哮喘.pdf", "output_format": "json"}
2026-08-06 10:35:47,168 INFO     30 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-06 10:35:47,239 INFO     30 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:35:47,241 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n⚠️ 住院病程文书归属：病程记录、查房记录、术前小结、术后首次病程记录等住院期间病程文书，与入院记录同属一次住院事件；当它们与入院记录页相邻时，必须合并为一个 AdmissionRecord 片段，不得单独成段、不得归入 DischargeRecord。\n- 病程文书识别特征：标题含\"病程记录\"/\"查房记录\"/\"术前小结\"/\"术后首次病程记录\"，带住院患者信息（科室/床号/住院号），有\"入院时间\"（如\"2020年07月08日 08:36:09入院\"），无\"出院诊断\"/\"出院医嘱\"\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。只有主诉，病史的也属于OutpatientRecord（门诊病历）\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 呼出气一氧化氮测定报告单\n[BBOX-1] 病人信息：\n[BBOX-2] 编号：482\n[BBOX-3] 姓名：\n[BBOX-4] 年龄：41岁9月27天\n[BBOX-5] 性别：女\n[BBOX-6] 科室：普通儿科一区\n[BBOX-7] 出生日期：1984-04-02\n[BBOX-8] 测定时间：2026/1/29 11:02:42\n[BBOX-9] 测定信息：\n[BBOX-10] 一小时内禁止饮食：■是\n[BBOX-11] 一小时内禁止剧烈运动：■是\n[BBOX-12] 三小时内禁止食用特殊食品*：■是\n[BBOX-13] 一小时内禁止抽烟：■是\n[BBOX-14] 三天内使用激素类药物：■是 □否\n[BBOX-15] 三天内使用抗生素：□是 ■否\n[BBOX-16] 症状：□咳嗽 □喘息 □鼻塞 □喷嚏 ■其他\n[BBOX-17] 病史：□过敏史 □其它\n[BBOX-18] *是指西兰花、芥蓝、生菜、莴苣、芹菜、水萝卜、熏制、腌制类食品。\n[BBOX-19] 测定项目：\n[BBOX-20] 呼气方式：■在线 □离线 □潮气\n[BBOX-21] 呼气温度：20.1℃\n[BBOX-22] 呼气压力：13.6cmH20\n[BBOX-23] 呼气平均流速：48ml/s\n[BBOX-24] 呼气NO浓度：\n[BBOX-25] 32.7,31.0,32.0,31.8,32.1,31.7ppb\n[BBOX-26] 呼气NO浓度均值:32ppb\n[BBOX-27] 呼气方式：■在线 □离线 □潮气\n[BBOX-28] 呼气温度：20.3℃\n[BBOX-29] 呼气压力：7.9cmH20\n[BBOX-30] 呼气平均流速：207ml/s\n[BBOX-31] 呼气NO浓度：\n[BBOX-32] 11.7,11.9,11.3,11.6,11.6,11.6ppb\n[BBOX-33] 呼气NO浓度均值:12ppb\n[BBOX-34] 测定结果：\n[BBOX-35] FeNO50：32ppb\n[BBOX-36] FeNO200：12ppb\n[BBOX-37] CaNO：3.6ppb\n[BBOX-38] 测定意义：\n[BBOX-39] 测定浓度\n[BBOX-40] 参考值\n[BBOX-41] 炎症鉴别诊断\n[BBOX-42] >12岁\n[BBOX-43] ≤12岁\n[BBOX-44] FeNO50\n[BBOX-45] <25ppb\n[BBOX-46] <20ppb*\n[BBOX-47] 非嗜酸性气道炎症\n[BBOX-48] 25-50ppb\n[BBOX-49] 20-35ppb*\n[BBOX-50] 混合型气道炎症\n[BBOX-51] ≥50ppb\n[BBOX-52] ≥35ppb*\n[BBOX-53] 嗜酸性气道炎症\n[BBOX-54] FeNO200\n[BBOX-55] >10ppb\n[BBOX-56] >8ppb\n[BBOX-57] 小气道炎症\n[BBOX-58] CaNO\n[BBOX-59] >5ppb\n[BBOX-60] >3ppb\n[BBOX-61] 肺泡炎症\n[BBOX-62] (*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)\n[BBOX-63] 复查时间：\n[BBOX-64] 操作员：赵彩红\n[BBOX-65] 医生：马春英\n[BBOX-66] 电\n[BBOX-67] 告\n[BBOX-68] 单\n[BBOX-69] 更\n[BBOX-70] 肺功能检查报告单\n[BBOX-71] 姓名：\n[BBOX-72] 测试号：\n[BBOX-73] 身高：160 cm\n[BBOX-74] 体重：48 kg\n[BBOX-75] 身份证号：\n[BBOX-76] 住院号：\n[BBOX-77] 年龄：41 岁\n[BBOX-78] 性别：女\n[BBOX-79] 科别：--\n[BBOX-80] 联系电话：\n[BBOX-81] 预计值 Bbt % (Bbt/\n[BBOX-82] A1\n[BBOX-83] A2\n[BBOX-84] A3\n[BBOX-85] FVC\n[BBOX-86] [L]\n[BBOX-87] 3.13\n[BBOX-88] 3.15\n[BBOX-89] 100.54\n[BBOX-90] 3.15\n[BBOX-91] 3.08\n[BBOX-92] 3.07\n[BBOX-93] FEV 1\n[BBOX-94] [L]\n[BBOX-95] 2.70\n[BBOX-96] 1.99\n[BBOX-97] 73.90\n[BBOX-98] 1.99\n[BBOX-99] 1.85\n[BBOX-100] 1.96\n[BBOX-101] FEV6\n[BBOX-102] [L]\n[BBOX-103] 3.13\n[BBOX-104] 3.13\n[BBOX-105] 3.05\n[BBOX-106] FEV 1 % FVC\n[BBOX-107] [%]\n[BBOX-108] 83.98\n[BBOX-109] 63.25\n[BBOX-110] 75.31\n[BBOX-111] 63.25\n[BBOX-112] 60.02\n[BBOX-113] 63.82\n[BBOX-114] FEV 1 % VC MAX\n[BBOX-115] [%]\n[BBOX-116] 81.31\n[BBOX-117] 63.25\n[BBOX-118] 77.78\n[BBOX-119] 63.25\n[BBOX-120] 58.74\n[BBOX-121] 62.12\n[BBOX-122] FIF 50\n[BBOX-123] [L/s]\n[BBOX-124] 5.84\n[BBOX-125] 5.77\n[BBOX-126] 5.84\n[BBOX-127] 5.48\n[BBOX-128] FEV3 % FVC\n[BBOX-129] [%]\n[BBOX-130] 89.30\n[BBOX-131] 89.30\n[BBOX-132] 87.11\n[BBOX-133] 88.97\n[BBOX-134] VC MAX\n[BBOX-135] [L]\n[BBOX-136] 3.19\n[BBOX-137] 3.15\n[BBOX-138] 98.65\n[BBOX-139] 2.99\n[BBOX-140] PEF\n[BBOX-141] [L/s]\n[BBOX-142] 6.46\n[BBOX-143] 6.33\n[BBOX-144] 97.97\n[BBOX-145] 6.33\n[BBOX-146] 5.90\n[BBOX-147] 5.95\n[BBOX-148] MMEF 75/25\n[BBOX-149] [L/s]\n[BBOX-150] 3.53\n[BBOX-151] 1.06\n[BBOX-152] 30.03\n[BBOX-153] 1.06\n[BBOX-154] 0.89\n[BBOX-155] 0.99\n[BBOX-156] MEF 25\n[BBOX-157] [L/s]\n[BBOX-158] 1.77\n[BBOX-159] 0.46\n[BBOX-160] 26.28\n[BBOX-161] 0.46\n[BBOX-162] 0.38\n[BBOX-163] 0.40\n[BBOX-164] MEF 50\n[BBOX-165] [L/s]\n[BBOX-166] 4.06\n[BBOX-167] 1.25\n[BBOX-168] 30.90\n[BBOX-169] 1.25\n[BBOX-170] 1.13\n[BBOX-171] 1.24\n[BBOX-172] MEF 75\n[BBOX-173] [L/s]\n[BBOX-174] 5.73\n[BBOX-175] 3.01\n[BBOX-176] 52.56\n[BBOX-177] 3.01\n[BBOX-178] 2.22\n[BBOX-179] 2.68\n[BBOX-180] V backextrapolation [B]\n[BBOX-181] 0.06\n[BBOX-182] 0.06\n[BBOX-183] 0.05\n[BBOX-184] 0.06\n[BBOX-185] V backextrapol. % FVC\n[BBOX-186] 1.86\n[BBOX-187] 1.86\n[BBOX-188] 1.52\n[BBOX-189] 1.82\n[BBOX-190] FET\n[BBOX-191] [s]\n[BBOX-192] 8.73\n[BBOX-193] 8.73\n[BBOX-194] 5.99\n[BBOX-195] 6.71\n[BBOX-196] FEF 200-1200\n[BBOX-197] [L/s]\n[BBOX-198] 3.07\n[BBOX-199] 3.07\n[BBOX-200] 2.51\n[BBOX-201] 2.98\n[BBOX-202] FVC IN\n[BBOX-203] [L]\n[BBOX-204] 3.19\n[BBOX-205] 2.99\n[BBOX-206] 93.64\n[BBOX-207] 2.26\n[BBOX-208] 2.99\n[BBOX-209] 2.94\n[BBOX-210] FIV1\n[BBOX-211] [L]\n[BBOX-212] 2.96\n[BBOX-213] 2.24\n[BBOX-214] 2.96\n[BBOX-215] 2.92\n[BBOX-216] FIV1 % FVC\n[BBOX-217] [%]\n[BBOX-218] 99.14\n[BBOX-219] 99.32\n[BBOX-220] 99.14\n[BBOX-221] 99.48\n[BBOX-222] FEF50 % FIF50\n[BBOX-223] [%]\n[BBOX-224] 21.46\n[BBOX-225] 21.72\n[BBOX-226] 19.34\n[BBOX-227] 22.60\n[BBOX-228] PIF\n[BBOX-229] [L/s]\n[BBOX-230] 6.10\n[BBOX-231] 5.87\n[BBOX-232] 6.10\n[BBOX-233] 5.50\n[BBOX-234] MVV\n[BBOX-235] [L/min]\n[BBOX-236] 101.9\n[BBOX-237] 91.45\n[BBOX-238] 89.73\n[BBOX-239] 91.45\n[BBOX-240] BF MVV\n[BBOX-241] [1/min]\n[BBOX-242] 75.65\n[BBOX-243] 75.65\n[BBOX-244] 10\n[BBOX-245] Flow [L/s]\n[BBOX-246] F/V ex\n[BBOX-247] Vol [L]\n[BBOX-248] Vol%VCmax\n[BBOX-249] Time [s]\n[BBOX-250] Vol [L]\n[BBOX-251] F/V In\n[BBOX-252] Vol [L]\n[BBOX-253] Time [s]\n[BBOX-254] 意见：\n[BBOX-255] 1.轻度阻塞性通气功能障碍。\n[BBOX-256] 检查质量：FVC：A级。 FEV1：A级。\n[BBOX-257] 备注：受检者检查配合佳。结果仅供参考，请结合临床分析。\n[BBOX-258] 2.最大自主分钟通气量（MVV）在正常范围。\n[BBOX-259] 备注：患者MVV配合佳。结果仅供参考，请结合临床分析。\n[BBOX-260] 审核医生：孙帅森\n[BBOX-261] 检测技师：韦龙华\n[BBOX-262] 2026/1/15\n[BBOX-263] 1604g\n[BBOX-264] 小气道阻解\n[BBOX-265] 不明显。\n[BBOX-266] 米 B\n[BBOX-267] 日 1\n[BBOX-268] △ 2\n[BBOX-269] ○ 3\n[BBOX-270] 米 B\n[BBOX-271] 日 1\n[BBOX-272] △ 2\n[BBOX-273] ○ 3\n[BBOX-274] CS 扫描全能王\n[BBOX-275] 3亿人都在用的扫描App\n[BBOX-276] 肺功能报告单\n[BBOX-277] 姓名：\n[BBOX-278] 性别：女\n[BBOX-279] 出生日期：1984/11/00\n[BBOX-280] 年龄：41岁\n[BBOX-281] 住院号：\n[BBOX-282] 测试号：\n[BBOX-283] 身高：160 cm\n[BBOX-284] 体重：48 kg\n[BBOX-285] 身份证号：\n[BBOX-286] 预计\n[BBOX-287] 实1 %(实1/预)\n[BBOX-288] 实2 %(实2/预)\n[BBOX-289] 变异率\n[BBOX-290] 测试日期\n[BBOX-291] 26/1/15\n[BBOX-292] 26/1/15\n[BBOX-293] 测试时间\n[BBOX-294] 9:51:00上午\n[BBOX-295] 10:14:56上午\n[BBOX-296] FVC\n[BBOX-297] [L]\n[BBOX-298] 3.13\n[BBOX-299] 3.15\n[BBOX-300] 100.5\n[BBOX-301] 3.25\n[BBOX-302] 103.9\n[BBOX-303] 3.3\n[BBOX-304] FEV 1\n[BBOX-305] [L]\n[BBOX-306] 2.70\n[BBOX-307] 1.99\n[BBOX-308] 73.9\n[BBOX-309] 2.26\n[BBOX-310] 83.8\n[BBOX-311] 13.4\n[BBOX-312] FEV 1 % FVC\n[BBOX-313] [%]\n[BBOX-314] 83.98\n[BBOX-315] 63.25\n[BBOX-316] 75.3\n[BBOX-317] 69.40\n[BBOX-318] 82.6\n[BBOX-319] 9.7\n[BBOX-320] FEV 1 % VC MAX\n[BBOX-321] [%]\n[BBOX-322] 81.31\n[BBOX-323] 63.25\n[BBOX-324] 77.8\n[BBOX-325] 69.40\n[BBOX-326] 85.4\n[BBOX-327] 9.7\n[BBOX-328] PEF\n[BBOX-329] [L/s]\n[BBOX-330] 6.46\n[BBOX-331] 6.33\n[BBOX-332] 98.0\n[BBOX-333] 7.25\n[BBOX-334] 112.2\n[BBOX-335] 14.5\n[BBOX-336] MEF 75\n[BBOX-337] [L/s]\n[BBOX-338] 5.73\n[BBOX-339] 3.01\n[BBOX-340] 52.6\n[BBOX-341] 3.73\n[BBOX-342] 65.1\n[BBOX-343] 23.8\n[BBOX-344] MEF 50\n[BBOX-345] [L/s]\n[BBOX-346] 4.06\n[BBOX-347] 1.25\n[BBOX-348] 30.9\n[BBOX-349] 1.67\n[BBOX-350] 41.2\n[BBOX-351] 33.3\n[BBOX-352] MEF 25\n[BBOX-353] [L/s]\n[BBOX-354] 1.77\n[BBOX-355] 0.46\n[BBOX-356] 26.3\n[BBOX-357] 0.59\n[BBOX-358] 33.6\n[BBOX-359] 27.7\n[BBOX-360] MMEF 75/25\n[BBOX-361] [L/s]\n[BBOX-362] 3.53\n[BBOX-363] 1.06\n[BBOX-364] 30.0\n[BBOX-365] 1.46\n[BBOX-366] 41.3\n[BBOX-367] 37.6\n[BBOX-368] FET\n[BBOX-369] [s]\n[BBOX-370] 8.73\n[BBOX-371] 4.94\n[BBOX-372] -43.4\n[BBOX-373] V backextrapolation ex [L]\n[BBOX-374] 0.06\n[BBOX-375] 0.07\n[BBOX-376] 20.1\n[BBOX-377] V backextrapol. % FVC [%]\n[BBOX-378] 1.86\n[BBOX-379] 2.17\n[BBOX-380] 16.3\n[BBOX-381] Flow [L/s]\n[BBOX-382] F/V ex\n[BBOX-383] 10\n[BBOX-384] 5\n[BBOX-385] 0\n[BBOX-386] 1\n[BBOX-387] 2\n[BBOX-388] 3\n[BBOX-389] 4\n[BBOX-390] 5\n[BBOX-391] 6\n[BBOX-392] 7\n[BBOX-393] 10\n[BBOX-394] F/V In\n[BBOX-395] 医生意见：\n[BBOX-396] 支气管舒张试验阳性。\n[BBOX-397] （通过储雾罐吸入硫酸沙丁胺醇气雾剂400ug20分钟后。\n[BBOX-398] FEV1较基线增加大于12 %，且绝对值增加大于200 ml。\n[BBOX-399] 审核医生：孙帅森\n[BBOX-400] 检测技师：朱龙华\n[BBOX-401] CS 扫描全能王\n[BBOX-402] 3亿人都在用的扫描App\n[BBOX-403] 肺功能报告单\n[BBOX-404] 姓名：\n[BBOX-405] 出生日期：1984/4/02\n[BBOX-406] 门诊/住院/体检：\n[BBOX-407] 身高：160 cm\n[BBOX-408] 身份证号：\n[BBOX-409] 性别：女\n[BBOX-410] 年龄：41岁\n[BBOX-411] 测试号：\n[BBOX-412] 体重：50 kg\n[BBOX-413] 测试日期\n[BBOX-414] 测试时间\n[BBOX-415] 预计\n[BBOX-416] 实测 % (实/预)\n[BBOX-417] 25/4/11\n[BBOX-418] 14:56:4\n[BBOX-419] VT\n[BBOX-420] [L]\n[BBOX-421] 0.36\n[BBOX-422] 0.41\n[BBOX-423] 114.9\n[BBOX-424] BF\n[BBOX-425] [1/min]\n[BBOX-426] 20.00\n[BBOX-427] 20.79\n[BBOX-428] 104.0\n[BBOX-429] MV\n[BBOX-430] [L/min]\n[BBOX-431] 7.14\n[BBOX-432] 8.54\n[BBOX-433] 119.5\n[BBOX-434] ERV\n[BBOX-435] [L]\n[BBOX-436] 1.07\n[BBOX-437] 1.07\n[BBOX-438] 99.4\n[BBOX-439] VC MAX\n[BBOX-440] [L]\n[BBOX-441] 3.19\n[BBOX-442] 2.84\n[BBOX-443] 88.9\n[BBOX-444] FVC\n[BBOX-445] [L]\n[BBOX-446] 3.13\n[BBOX-447] 2.84\n[BBOX-448] 90.6\n[BBOX-449] FEV 1\n[BBOX-450] [L]\n[BBOX-451] 2.70\n[BBOX-452] 1.53\n[BBOX-453] 56.9\n[BBOX-454] FEV 1 % FVC\n[BBOX-455] [%]\n[BBOX-456] 83.98\n[BBOX-457] 54.07\n[BBOX-458] 64.4\n[BBOX-459] FEV 1 % VC MAX\n[BBOX-460] [%]\n[BBOX-461] 81.31\n[BBOX-462] 54.07\n[BBOX-463] 66.5\n[BBOX-464] PEF\n[BBOX-465] [L/s]\n[BBOX-466] 6.46\n[BBOX-467] 4.56\n[BBOX-468] 70.7\n[BBOX-469] MEF 75\n[BBOX-470] [L/s]\n[BBOX-471] 5.73\n[BBOX-472] 1.84\n[BBOX-473] 32.1\n[BBOX-474] MEF 50\n[BBOX-475] [L/s]\n[BBOX-476] 4.06\n[BBOX-477] 0.84\n[BBOX-478] 20.7\n[BBOX-479] MEF 25\n[BBOX-480] [L/s]\n[BBOX-481] 1.77\n[BBOX-482] 0.28\n[BBOX-483] 15.6\n[BBOX-484] MMEF 75/25\n[BBOX-485] [L/s]\n[BBOX-486] 3.53\n[BBOX-487] 0.65\n[BBOX-488] 18.3\n[BBOX-489] FET\n[BBOX-490] [s]\n[BBOX-491] 8.46\n[BBOX-492] V backextrapolation ex\n[BBOX-493] [L]\n[BBOX-494] 0.03\n[BBOX-495] V backextrapol. % FVC\n[BBOX-496] [%]\n[BBOX-497] 1.23\n[BBOX-498] MVV\n[BBOX-499] [L/min]\n[BBOX-500] 101.93\n[BBOX-501] 75.75\n[BBOX-502] 74.3\n[BBOX-503] FEV 1*30\n[BBOX-504] [L/min]\n[BBOX-505] 101.93\n[BBOX-506] 46.03\n[BBOX-507] 45.2\n[BBOX-508] RV-SB\n[BBOX-509] [L]\n[BBOX-510] 1.55\n[BBOX-511] 2.56\n[BBOX-512] 164.9\n[BBOX-513] RV%TLC-SB\n[BBOX-514] [%]\n[BBOX-515] 32.90\n[BBOX-516] 47.52\n[BBOX-517] 144.4\n[BBOX-518] TLC-SB\n[BBOX-519] [L]\n[BBOX-520] 4.77\n[BBOX-521] 5.39\n[BBOX-522] 112.9\n[BBOX-523] FRC-SB\n[BBOX-524] [L]\n[BBOX-525] 2.63\n[BBOX-526] 3.31\n[BBOX-527] 126.0\n[BBOX-528] FRC%TLC-SB\n[BBOX-529] [%]\n[BBOX-530] 51.66\n[BBOX-531] 61.42\n[BBOX-532] 118.9\n[BBOX-533] DLCOc SB\n[BBOX-534] [mmol/min/kPa]\n[BBOX-535] 8.34\n[BBOX-536] 6.95\n[BBOX-537] 83.4\n[BBOX-538] DLCO SB\n[BBOX-539] [mmol/min/kPa]\n[BBOX-540] 8.34\n[BBOX-541] 6.95\n[BBOX-542] 83.4\n[BBOX-543] 医生意见：\n[BBOX-544] 1.中重度阻塞性通气功能障碍。\n[BBOX-545] 检查质量：FVC：A级。 FEV1：A级。\n[BBOX-546] 备注：受检者检查配合佳。 结果仅供参考，请结合临床分析。\n[BBOX-547] 2.最大自主分钟通气量（MVV）轻度下降。\n[BBOX-548] 备注：患者MVV配合佳。结果仅供参考，请结合临床分析。\n[BBOX-549] 3.弥散功能在正常范围。4.残总比中度增高。\n[BBOX-550] 审核医生：孙帅森\n[BBOX-551] 检测技师：张青苹\n[BBOX-552] 通气弥散B\n[BBOX-553] 2025/4/11 15:18\n[BBOX-554] 1/1\n[BBOX-555] 布地奈德 4ml Bid 3天\n[BBOX-556] 喷 3个月 后复查肺功能。\n[BBOX-557] Vol [L]\n[BBOX-558] PredA0.0\n[BBOX-559] 0.2\n[BBOX-560] 0.4\n[BBOX-561] 0.6\n[BBOX-562] 0.8\n[BBOX-563] 1.0\n[BBOX-564] Time [min]\n[BBOX-565] Flow [L/s]\n[BBOX-566] F/V ex\n[BBOX-567] 10\n[BBOX-568] 5\n[BBOX-569] 0\n[BBOX-570] 2\n[BBOX-571] 4\n[BBOX-572] 6\n[BBOX-573] F/V in\n[BBOX-574] 10\n[BBOX-575] Vol [L]\n[BBOX-576] Vol [L]\n[BBOX-577] 100\n[BBOX-578] 10\n[BBOX-579] 50\n[BBOX-580] Time [s]\n[BBOX-581] 0\n[BBOX-582] 1\n[BBOX-583] 2\n[BBOX-584] 3\n[BBOX-585] 4\n[BBOX-586] 5\n[BBOX-587] Volume [L]\n[BBOX-588] 4\n[BBOX-589] 2\n[BBOX-590] 0\n[BBOX-591] M\n[BBOX-592] 1\n[BBOX-593] 2\n[BBOX-594] 4\n[BBOX-595] Time [s]\n[BBOX-596] 0\n[BBOX-597] 20\n[BBOX-598] 40\n[BBOX-599] 60\n[BBOX-600] 80\n[BBOX-601] 肺功能报告单\n[BBOX-602] 姓名：\n[BBOX-603] 出生日期：1984/4/02\n[BBOX-604] 性别：女\n[BBOX-605] 年龄：41岁\n[BBOX-606] 门诊/住院/体检：\n[BBOX-607] 测试号：\n[BBOX-608] 身高：160 cm\n[BBOX-609] 体重：50 kg\n[BBOX-610] 身份证号：\n[BBOX-611] 预计\n[BBOX-612] 实1 %(实1/预)\n[BBOX-613] 实2 %(实2/预)\n[BBOX-614] 变异率\n[BBOX-615] 测试日期\n[BBOX-616] 25/4/11\n[BBOX-617] 25/4/11\n[BBOX-618] 测试时间\n[BBOX-619] 14:56:47下午\n[BBOX-620] 15:14:32下午\n[BBOX-621] FVC\n[BBOX-622] [L]\n[BBOX-623] 3.13\n[BBOX-624] 2.84\n[BBOX-625] 90.6\n[BBOX-626] 3.05\n[BBOX-627] 97.4\n[BBOX-628] 7.5\n[BBOX-629] FEV 1\n[BBOX-630] [L]\n[BBOX-631] 2.70\n[BBOX-632] 1.53\n[BBOX-633] 56.9\n[BBOX-634] 1.91\n[BBOX-635] 71.0\n[BBOX-636] 24.7\n[BBOX-637] FEV 1 % FVC\n[BBOX-638] [%]\n[BBOX-639] 83.98\n[BBOX-640] 54.07\n[BBOX-641] 64.4\n[BBOX-642] 62.70\n[BBOX-643] 74.7\n[BBOX-644] 16.0\n[BBOX-645] FEV 1 % VC MAX\n[BBOX-646] [%]\n[BBOX-647] 81.31\n[BBOX-648] 54.07\n[BBOX-649] 66.5\n[BBOX-650] 62.70\n[BBOX-651] 77.1\n[BBOX-652] 16.0\n[BBOX-653] PEF\n[BBOX-654] [L/s]\n[BBOX-655] 6.46\n[BBOX-656] 4.56\n[BBOX-657] 70.7\n[BBOX-658] 5.64\n[BBOX-659] 87.3\n[BBOX-660] 23.6\n[BBOX-661] MEF 75\n[BBOX-662] [L/s]\n[BBOX-663] 5.73\n[BBOX-664] 1.84\n[BBOX-665] 32.1\n[BBOX-666] 2.65\n[BBOX-667] 46.3\n[BBOX-668] 44.3\n[BBOX-669] MEF 50\n[BBOX-670] [L/s]\n[BBOX-671] 4.06\n[BBOX-672] 0.84\n[BBOX-673] 20.7\n[BBOX-674] 1.23\n[BBOX-675] 30.4\n[BBOX-676] 47.0\n[BBOX-677] MEF 25\n[BBOX-678] [L/s]\n[BBOX-679] 1.77\n[BBOX-680] 0.28\n[BBOX-681] 15.6\n[BBOX-682] 0.44\n[BBOX-683] 25.0\n[BBOX-684] 60.2\n[BBOX-685] MMEF 75/25\n[BBOX-686] [L/s]\n[BBOX-687] 3.53\n[BBOX-688] 0.65\n[BBOX-689] 18.3\n[BBOX-690] 1.02\n[BBOX-691] 29.1\n[BBOX-692] 58.8\n[BBOX-693] FET\n[BBOX-694] [s]\n[BBOX-695] 8.46\n[BBOX-696] 6.41\n[BBOX-697] -24.2\n[BBOX-698] V backextrapolation ex [L]\n[BBOX-699] 0.03\n[BBOX-700] 0.06\n[BBOX-701] 71.7\n[BBOX-702] V backextrapol. % FVC [%]\n[BBOX-703] 1.23\n[BBOX-704] 1.96\n[BBOX-705] 59.6\n[BBOX-706] Flow [L/s]\n[BBOX-707] F/V ex\n[BBOX-708] 10\n[BBOX-709] 5\n[BBOX-710] 0\n[BBOX-711] 1\n[BBOX-712] 2\n[BBOX-713] 3\n[BBOX-714] 4\n[BBOX-715] 5\n[BBOX-716] 6\n[BBOX-717] 7\n[BBOX-718] 10\n[BBOX-719] F/V In\n[BBOX-720] 医生意见：\n[BBOX-721] 支气管舒张试验阳性。\n[BBOX-722] （通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后。\n[BBOX-723] FEV1较基线增加大于12%，且绝对值增加大于200ml。）\n[BBOX-724] 审核医生：孙帅森\n[BBOX-725] 检测技师：张青苹\n[BBOX-726] CS 扫描全能王\n[BBOX-727] 3亿人都在用的扫描App\n[BBOX-728] 院\n[BBOX-729] 入院记录\n[BBOX-730] 姓名：\n[BBOX-731] 科室：产科二区\n[BBOX-732] 床号：\n[BBOX-733] 科室：产科二区\n[BBOX-734] 第(1)次入院记录\n[BBOX-735] 过敏史：无\n[BBOX-736] 姓名：\n[BBOX-737] 性别：女\n[BBOX-738] 年龄：36岁\n[BBOX-739] 身份证号\n[BBOX-740] 职业：\n[BBOX-741] 婚姻：已婚\n[BBOX-742] 民族：汉族\n[BBOX-743] 出生地：\n[BBOX-744] 现住址：\n[BBOX-745] 入院日期：2020-07-08 08:36:09\n[BBOX-746] 邮编\n[BBOX-747] 病史采集时间：2020-07-08 08:36:09\n[BBOX-748] 联系人：\n[BBOX-749] 与病人关系：夫妻\n[BBOX-750] 病史叙述者：本人\n[BBOX-751] 联系人地址：同上地址\n[BBOX-752] 电话.\n[BBOX-753] 可靠程度：可靠\n[BBOX-754] 主诉：停经39周，要求住院待产。\n[BBOX-755] 现病史：平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日（阳历），预产\n[BBOX-756] 期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单活胎，发育符合\n[BBOX-757] 孕周。孕早期无早孕反应，孕早期无腹痛、出血，阴道流液，出血史，无放射线、有害物质接\n[BBOX-758] 触史。孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正常，孕中期行无创DNA\n[BBOX-759] 结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正常，未行糖耐量筛\n[BBOX-760] 查，未查B族链球菌。孕期经过顺利，孕晚期无头痛、头晕、眼花等症状，无皮肤黄染及痰\n[BBOX-761] 痒。现停经39周，无腹痛，未见红及破水，遂入院要求住院待产，门诊以“足月妊娠、瘢痕子\n[BBOX-762] 宫”收住院。自孕以来精神好，饮食、睡眠好，大小便正常，体重增加约10KG。\n[BBOX-763] 既往史：患者平素体健；否认有“心脏病、高血压、糖尿病、肾病”等慢性病史，否认有\n[BBOX-764] “肝炎、结核”等传染性疾病。于2016.08行剖宫产手术，否认余手术及外伤史。否认有输血\n[BBOX-765] 史，有献血史，否认食物及药物过敏史。预防接种随社会进行。\n[BBOX-766] 个人史：出生于原籍，护士，本科文化，工作于三门峡市中心医院。否认长期外地居住\n[BBOX-767] 史，无疫区居住史，无烟酒等不良嗜好。生长环境一般，否认有冶游史。\n[BBOX-768] 婚育史：31岁结婚，爱人\n[BBOX-769] 现年37岁，职员，工作于三门峡市党校，身体健康，无吸\n[BBOX-770] 烟史，有饮酒史，否认“肝炎、结核”病史，夫妻感情好。孕;产;，2016年足月剖宫产1活男\n[BBOX-771] 婴，现体健，否认产后出血及产褥感染史，否认不良孕产史。\n[BBOX-772] 月经史：平素月经规律，12岁，5-7天/30-35天，末次月经为：2019年10月08日（阳\n[BBOX-773] 历），量中等，色暗红，偶有血块，无痛经。\n[BBOX-774] 页\n[BBOX-775] 书写者签名：\n[BBOX-776] 总第 页\n[BBOX-777] 院\n[BBOX-778] 入院记录\n[BBOX-779] 姓名：\n[BBOX-780] 科室：产科二区\n[BBOX-781] 床号：\n[BBOX-782] 生。\n[BBOX-783] 家族史：父母亲体健，1弟1妹均体健，1子体健。否认家族中有遗传性及传染性疾病史。\n[BBOX-784] 体格检查\n[BBOX-785] 体温：36.5℃\n[BBOX-786] 脉搏：78次/分\n[BBOX-787] 呼吸：18次/分\n[BBOX-788] 血压：98/64mmHg\n[BBOX-789] 身高160cm\n[BBOX-790] 体重：60Kg\n[BBOX-791] 一般状况：发育正常；营养中等；自动体位：面色红润；面容及表情自如；神志清晰；言\n[BBOX-792] 语状态流利；检查时能合作等。\n[BBOX-793] 皮肤：色泽正常，弹性正常，无水肿、出汗、紫癜、皮疹、色素沉着、蜘蛛痣、瘢痕、创\n[BBOX-794] 伤、溃疡、结节。\n[BBOX-795] 淋巴结：全身或局部表浅淋巴结未触及肿大；局部皮肤无红热、瘘管、瘢痕。\n[BBOX-796] 头部：\n[BBOX-797] 头颅：大小无异常、外形无异常；眉发分布正常；无疖、痈、外伤、瘢痕、肿块。\n[BBOX-798] 眼部：双眼裂正常，双眼睑无水肿，眼球运动正常。瞳孔：左3.0mm 直接对光反应灵敏，\n[BBOX-799] 间接对光反应灵敏；右3.0mm 直接对光反应灵敏，间接对光反应灵敏。视力粗测正常。\n[BBOX-800] 耳部：耳廓无畸形，外耳道无分泌物，乳突无压痛，听力粗测5米。\n[BBOX-801] 鼻部：无畸形、鼻翼扇动、阻塞、分泌物、鼻中隔异常、嗅觉障碍、鼻窦压痛等。\n[BBOX-802] 口腔：口唇红润，无畸形、疱疹、微血管搏动、口角皲裂；牙齿无缺损、龋病、镶补等异\n[BBOX-803] 常；牙龈无溢血、溢脓、萎缩、色素沉着；口腔粘膜无溃疡、假膜、色素沉着；扁桃体无肿\n[BBOX-804] 大、分泌物；咽部无充血、分泌物。\n[BBOX-805] 颈部：对称，无强直、压痛、运动受限、颈静脉怒张、颈动脉明显搏动、肿块，气管居\n[BBOX-806] 中，甲状腺无肿大。\n[BBOX-807] 胸部\n[BBOX-808] 胸廓：形状正常，对称，运动程度正常，肋间正常，胸壁无水肿、皮下气肿、肿块、静脉\n[BBOX-809] 曲张，肋骨及肋软骨无压痛、凹陷等异常。乳头，正常。\n[BBOX-810] 肺脏：视诊：腹式呼吸，呼吸节律正常，呼吸深度正常，两侧呼吸运动对称。\n[BBOX-811] 触诊：语音震颤两侧相等，无摩擦感。\n[BBOX-812] 叩诊：叩诊声响清音，肺下界肩胛线在第10肋间，呼吸移动度6cm，\n[BBOX-813] 听诊：呼吸音性质为肺泡呼吸音，强度正常，语音传导正常，无摩擦音、哮鸣音、\n[BBOX-814] 第页\n[BBOX-815] 书写者签名：\n[BBOX-816] 总第页\n[BBOX-817] 院\n[BBOX-818] 入院记录\n[BBOX-819] 姓名：\n[BBOX-820] 科室：产科二区\n[BBOX-821] 床号\n[BBOX-822] 病号：\n[BBOX-823] 干啰音、湿啰音。\n[BBOX-824] 心脏：视诊：心尖搏动的位置在左侧锁骨中线内第4肋间，范围为2.5cm，强度正常，心前\n[BBOX-825] 区无异常搏动、局限性膨隆。\n[BBOX-826] 触诊：心尖搏动最强部位在左侧锁骨中线第4肋间，范围为2.5cm，无抬举性搏动、\n[BBOX-827] 震颤、摩擦感。\n[BBOX-828] 叩诊：左右心界线以每肋间距胸骨中线的cm数记载。\n[BBOX-829] 右cm\n[BBOX-830] 肋间\n[BBOX-831] 左cm\n[BBOX-832] 2\n[BBOX-833] Ⅱ\n[BBOX-834] 2.5\n[BBOX-835] 2\n[BBOX-836] Ⅲ\n[BBOX-837] 4\n[BBOX-838] 3\n[BBOX-839] Ⅳ\n[BBOX-840] 5.5\n[BBOX-841] V\n[BBOX-842] 8\n[BBOX-843] 左锁骨中线至前正中线的距离9cm。\n[BBOX-844] 听诊：心率78次/分，心律整齐，无心脏杂音，无第三心音、第四心音、心音分\n[BBOX-845] 裂，P2<A2。\n[BBOX-846] 血管：桡动脉搏动正常，血管壁硬度正常。\n[BBOX-847] 周围血管征：无毛细血管搏动征、水冲脉、枪击音、动脉异常搏动。\n[BBOX-848] 腹部：\n[BBOX-849] 视诊：腹部膨隆，晓孕腹型，腹壁对称，无凹陷、膨隆、静脉曲张、蠕动波、局限性隆\n[BBOX-850] 起，下腹可见一长约15cm横行手术疤痕。\n[BBOX-851] 触诊：腹壁柔软，无压痛，无反跳痛；未触及肿块，无搏动、波动感等。肝脏：肋缘下未\n[BBOX-852] 触及，无压痛。胆囊：未触及，无压痛。脾脏：肋缘下未触及。肾：未触及，无压痛等。\n[BBOX-853] 叩诊：肝上界位于第5肋间，肝浊音界正常，肝区无叩击痛、脾区无叩击痛、腹部无过度\n[BBOX-854] 鼓音，移动性浊音阴性。\n[BBOX-855] 听诊：肠蠕动音正常，频率4次/分，胃区无振水声，肝区无摩擦音、脾区无摩擦音，无血\n[BBOX-856] 管杂音。\n[BBOX-857] 外阴及肛门：阴毛分布正常；外生殖器发育正常，肛门检查：无外痔、肛裂、肛瘘、脱\n[BBOX-858] 肛、湿疣等。\n[BBOX-859] 脊柱：脊柱无畸形、压痛、叩击痛；脊柱两侧肌肉无紧张、压痛；肋脊角无压痛、叩痛。\n[BBOX-860] 四肢：无畸形、杵状指（趾）、静脉曲张、外伤、骨折；肌肉张力正常与肌力5级，无萎\n[BBOX-861] 院\n[BBOX-862] 入院记录\n[BBOX-863] 姓名.\n[BBOX-864] 科室:产科二区\n[BBOX-865] 床号\n[BBOX-866] 住院号.\n[BBOX-867] 缩;关节无红肿、畸形、运动障碍,双下肢水肿。\n[BBOX-868] 神经反射:膝腱反射正常、跟腱反射正常、肱二头肌腱反射正常、肱三头肌腱反射正常、\n[BBOX-869] 腹壁反射正常、巴彬斯基征阴性、克尼格征阴性等。\n[BBOX-870] 专科情况\n[BBOX-871] 宫高34CM,腹围102CM,估计胎儿体重:3200g,胎位:头位,胎心152次/分,律齐,无\n[BBOX-872] 宫缩,未见红,未破水,骨盆外测量及内诊:未做。\n[BBOX-873] 辅助检查\n[BBOX-874] B超(2020.07.02 本院):晓孕宫内单活胎头位(双顶径9.4cm,股骨长7.0cm羊水指\n[BBOX-875] 数8.5cm),胎盘成熟度II°.\n[BBOX-876] 初步诊断:\n[BBOX-877] 1.妊娠合并子宫瘢痕;\n[BBOX-878] 3.孕2产,宫内孕39周头位待产。\n[BBOX-879] 主治医师:\n[BBOX-880] 孙小丹\n[BBOX-881] 副主任医师:\n[BBOX-882] 彭琼玉\n[BBOX-883] 2020.07.08\n[BBOX-884] CS 扫描全能王\n[BBOX-885] 3亿人都在用的扫描App\n[BBOX-886] 姓名：\n[BBOX-887] 科室：产科二区\n[BBOX-888] 床号\n[BBOX-889] 住院号.\n[BBOX-890] 2020年07月08日 09时22分\n[BBOX-891] 首次病程记录\n[BBOX-892] 患\n[BBOX-893] 女，36岁，汉族，-以“停经39周，要求住院待产”为主诉于\n[BBOX-894] 2020-07-08 08:36:09入院。一、病例特点：1、已婚育龄妇女，孕₂产₁，否认产后出血及产褥\n[BBOX-895] 感染史，否认不良孕产史；2、平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日\n[BBOX-896] (阳历)，预产期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单\n[BBOX-897] 活胎，发育符合孕周。3、孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正\n[BBOX-898] 常，孕中期行无创DNA结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正\n[BBOX-899] 常，未行糖耐量筛查，未查B族链球菌。4、现停经39周，无腹痛，未见红及破水，遂入院要求\n[BBOX-900] 住院待产。5.入院查体：T：36.5℃，P：78次/分，R：18次/分，BP：98/64mmHg。神志清楚，\n[BBOX-901] 精神好，全身皮肤黏膜无黄染，浅表淋巴结未触及，心肺听诊未闻及明显异常，腹膨隆。6、\n[BBOX-902] 专科检查：宫高34CM，腹围102CM，估计胎儿体重：3200g，胎位：头位，胎心152次/分，律\n[BBOX-903] 齐，无宫缩，未见红，未破水，骨盆外测量及内诊：未做。7、辅助检查：B超（2020.07.02\n[BBOX-904] 本院）：晚孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度\n[BBOX-905] II°。二、拟诊讨论：（一）初步诊断：1.妊娠合并子宫瘢痕；2.孕₂产；宫内孕39周头位\n[BBOX-906] 待产。（二）诊断依据：1、患者有停经史，平素月经规律，平素月经规律，5-7天/35-36天，\n[BBOX-907] 末次月经为：2019年10月08日（阳历），预产期为2020年07月15日（阳历），停经后有自觉胎\n[BBOX-908] 动，产前检查可同及胎心；2、专科检查：宫高34CM，腹围102CM，估计胎儿体重：3200g，胎\n[BBOX-909] 位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水。骨盆外测量及内诊：未做。3、\n[BBOX-910] 辅助检查：B超（2020.07.02本院）：晚孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm\n[BBOX-911] 羊水指数8.5cm)，胎盘成熟度II°。（三）鉴别诊断：根据据病史、查体及辅助检查，目前诊\n[BBOX-912] 断明确。三、诊疗计划：完善各项检查：心电图、彩超、血常规、血型、凝血五项、输血前检\n[BBOX-913] 查、尿常规、心电图、肝功、肾功、血糖、电解质等；2、向患者及家属交代病情，围生期相\n[BBOX-914] 关危险因素；3、给予巡视病房、监测胎心、心理疏导，消除围产期恐惧心理等产前护理；4、\n[BBOX-915] 患者要求明日剖宫产，纳入剖宫产临床路径。\n[BBOX-916] 主治医师：孙州\n[BBOX-917] 2020年07月08日 10时22分\n[BBOX-918] 科主任宋瑞香主治医师查房记录\n[BBOX-919] 第页\n[BBOX-920] 总第页\n[BBOX-921] 姓名：\n[BBOX-922] 科室：产科二区\n[BBOX-923] 床号：\n[BBOX-924] 住院号\n[BBOX-925] 今日随科主任宋瑞香主治医师查房，患者精神好，饮食及睡眠可，大小便正常，未破\n[BBOX-926] 水，未见红，无腹痛。查体：生命体征平稳，心肺听诊未闻及明显异常，胎心波动于正常范\n[BBOX-927] 围，无宫缩。目前诊断：1.妊娠合并于宫瘢痕；2.孕2产；宫内孕39周头位待产。诊断依\n[BBOX-928] 据：1.停经后有自觉胎动，产前检查可闻及胎心。2、查体：宫高34CM，腹围102CM，估计胎儿\n[BBOX-929] 体重：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水。骨盆外测量及\n[BBOX-930] 内诊：未做。3、辅助检查：B超（2020.07.02 本院）：晓孕宫内单活胎头位(双顶径\n[BBOX-931] 9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。科主任宋瑞香主治医师查房指示：\n[BBOX-932] 患者孕足月、瘢痕子宫，若阴道分娩易出现先兆子宫破裂、子宫破裂、胎死宫内等情况，患者\n[BBOX-933] 及其家属表示理解，要求明日剖宫产终止妊娠，完善术前谈话，积极术前准备，严密监测胎心\n[BBOX-934] 变化。以上医嘱已执行。\n[BBOX-935] 主治医师：主治医师：\n[BBOX-936] 孙丹\n[BBOX-937] 2020年07月08日 10：20\n[BBOX-938] 术前小结\n[BBOX-939] 姓名：\n[BBOX-940] 性别：女，年龄：36岁；\n[BBOX-941] 病历摘要：以“伴经39周，要求住院待产”为主诉入院。孕2产，否认产后出血及产褥感\n[BBOX-942] 染史，否认不良孕产史。查体：生命体征平稳，心肺听诊未闻及异常。腹隆，晚孕腹型。肝脾\n[BBOX-943] 肋下未触及，下腹部可见一长约15cm的横行手术瘢痕。双下肢无水肿；专科检查：宫高34CM，\n[BBOX-944] 腹围102CM，估计胎儿体重：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未\n[BBOX-945] 破水。骨盆外测量及内诊：未做。辅助检查：B超（2020.07.02 本院）：晓孕宫内单活胎\n[BBOX-946] 头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。入院后要求剖宫产终止\n[BBOX-947] 妊娠，手术相关风险已向其讲明，并在手术同意书上签字。请示科主任宋瑞香副主任医师，同\n[BBOX-948] 意安排手术，手术医师宋瑞香主治医师查看病人，生命体征平稳，无手术禁忌，积极术前准\n[BBOX-949] 备。\n[BBOX-950] 术前诊断：1.妊娠合并子宫瘢痕；2.孕2产；宫内孕39周头位待产。\n[BBOX-951] 手术指证：足月妊娠，瘢痕子宫，患者及家属要求，无手术禁忌症：\n[BBOX-952] 拟施手术名称和方式：拟定于明日07：30行二次子宫下段剖宫产术；\n[BBOX-953] 拟施麻醉：椎管内麻醉；\n[BBOX-954] 第 页\n[BBOX-955] 总第 页\n[BBOX-956] CS 扫描全能王\n[BBOX-957] 3亿人都在用的扫描App\n[BBOX-958] 一\n[BBOX-959] 院\n[BBOX-960] 姓名：\n[BBOX-961] 科室：产科二区\n[BBOX-962] 床号：\n[BBOX-963] 注意事项：规范操作，彻底止血，待新生儿娩出后，给予“缩宫素针”促宫缩治疗，做好\n[BBOX-964] 新生儿复苏工作。\n[BBOX-965] 主治医师：\n[BBOX-966] 孙丹丹\n[BBOX-967] 第 页\n[BBOX-968] 总第 页\n[BBOX-969] 院\n[BBOX-970] 姓名：\n[BBOX-971] 科室：产科二区\n[BBOX-972] 床：\n[BBOX-973] 住院号：\n[BBOX-974] 2020年07月09日 09时47分\n[BBOX-975] 术后首次病程记录\n[BBOX-976] 患者术前测胎心150次/分，于今日08：29-09：30在腰硬联合麻醉+基础麻醉下行二次子宫\n[BBOX-977] 下段剖宫产术+子宫修补术，取下腹原横切口，剔除原瘢痕，逐层进腹，膀下指膀胱，暴露子\n[BBOX-978] 宫下段，可见于宫下段肌层较薄，胎儿头发及胎脂漂浮，切开子宫后见羊水清，约600ml，吸\n[BBOX-979] 净后以头位助娩一活男婴，出生1-10分钟均评10分，胎盘胎膜自娩完整，子宫收缩可，纱布球\n[BBOX-980] 擦拭子宫腔，可见子宫下段肌层断裂，用可吸收线间断缝合子宫下段肌层，断裂的血管给予缝\n[BBOX-981] 合，以恰桥可吸收线分两层连续缝合子宫切口。探查子宫切口无活动性出血，双侧附件外观正\n[BBOX-982] 常，关腹。术程顺利，术中麻���好，呼吸血压平稳，输入晶体液800ml，胶体液0ml，出血不\n[BBOX-983] 多，约200ml，尿色清，量约100ml，术中诊断：1.妊娠合并子宫瘢痕；2.孕2产：宫内孕39*1周\n[BBOX-984] 头位剖宫产；术后安返病房，测P：64次/分，R：18次/分，Bp：84/54mmHg，术后给予“头\n[BBOX-985] 孢唑林钠针”预防感染、加强宫缩、会阴冲洗、尿管护理及支持对症等治疗，并嘱其按摩双下\n[BBOX-986] 肢预防下肢静脉血栓形成，注意观察生命体征、子宫收缩及阴道出血情况。\n[BBOX-987] 住院医师：冯雪云\n[BBOX-988] 2020年07月10日 09时00分\n[BBOX-989] 彭琼玉副主任医师查房记录\n[BBOX-990] 今日为剖宫产术后一天，患者精神、睡眠好，无特殊不适，未排气。彭琼玉副主任医师\n[BBOX-991] 查房：查体：生命体征平稳，双乳不胀，无泌乳，心肺未闻及异常，腹软，腹部切口皮肤对合\n[BBOX-992] 好，未见红肿、硬结等异常，宫底平脐，子宫收缩好，阴道出血不多，尿管畅，尿色清，尿量\n[BBOX-993] 正常，余查无特殊，查房意见：现术后一天，未排气，流食，体温正常，切口无感染迹象，病\n[BBOX-994] 情无特殊，继续抗炎补液加强宫缩等治疗；嘱患者床上多翻身并按摩双下肢，以防术后肠粘连\n[BBOX-995] 及栓塞性疾病发生，给予肌注缩宫素10uBID促进子宫收缩，给予子宫复旧磁疗促进产后子宫\n[BBOX-996] 恢复，嘱保持乳房畅通，并给予泌乳磁疗促进乳汁分泌，输完液体后拔除尿管，适当下床活\n[BBOX-997] 动，注意监测血糖情况，上述指示已执行。\n[BBOX-998] 副主任医师：马\n[BBOX-999] 住院医师：冯雪云\n[BBOX-1000] 2020年07月11日 08时06分\n[BBOX-1001] 术后第二天，患者无发热，已排气，尿管拔除后排尿畅。查体：生命体征平稳，心肺听诊\n[BBOX-1002] 第 页\n[BBOX-1003] 总第 页\n[BBOX-1004] 出院\n[BBOX-1005] 姓名：\n[BBOX-1006] 科室：产科二区\n[BBOX-1007] 床号\n[BBOX-1008] 住院\n[BBOX-1009] 未闻及异常，双乳泌乳量不多，腹软，子宫收缩好，宫底位于脐下两横指，无压痛，阴道出血\n[BBOX-1010] 不多，暗红色，无异味，腹部切口换药见切口皮缘对合好，未见红肿、硬结及渗液等异常，双\n[BBOX-1011] 下肢无水肿，现术后第二天，病情稳定，改为II级护理，已排气给予苔含，注意体温变化及切\n[BBOX-1012] 口情况；继续予子宫复旧磁疗促进产后子宫恢复，加用腹部切口红外线治疗促进伤口愈合，加\n[BBOX-1013] 益宫颗粒(自各药物)促宫缩治疗，观察体温及阴道恶露情况。\n[BBOX-1014] 主治医师：孙丹丹\n[BBOX-1015] 2020年07月12日 10时00分\n[BBOX-1016] 彭琼玉副主任医师查房记录\n[BBOX-1017] 今日查房，患者剖宫产术后三天，患者未诉不适，精神好，饮食、睡眠正常，查体：生\n[BBOX-1018] 命体征平稳，心肺听诊未闻及异常，双乳泌乳量多，腹软，腹部切口无红肿、硬结、渗液等异\n[BBOX-1019] 常，子宫收缩好，阴道出血不多，余查无特殊，再次复查血常规：白细胞10.59×10⁹/L,中性\n[BBOX-1020] 粒细胞86.3%，偏高，血红蛋白100g/L，患者复查白细胞正常，中性粒细胞偏高，体温正常，\n[BBOX-1021] 切口无感染迹象，考虑术后炎性反应，暂不特殊处理，嘱加强营养，加强运动。彭琼玉副主任\n[BBOX-1022] 医师查房指示：患者现病情稳定，腹部伤口皮内结合，无需拆线，达临床治愈，顺利完成剖宫\n[BBOX-1023] 产临床路径管理，今日办理出院。指示已执行。\n[BBOX-1024] 副主任医师：彭琼玉\n[BBOX-1025] 主治医师：孙丹丹\n[BBOX-1026] 出院记录\n[BBOX-1027] 姓名\n[BBOX-1028] 科室：产科二区\n[BBOX-1029] 床号.\n[BBOX-1030] 住院\n[BBOX-1031] 2020年07月12日\n[BBOX-1032] 出院记录\n[BBOX-1033] 患者.\n[BBOX-1034] 36岁\n[BBOX-1035] 住院号：\n[BBOX-1036] 入院日期：2020-07-08 08:36:09\n[BBOX-1037] 出院日期：2020年07月12日\n[BBOX-1038] 住院天数：4天\n[BBOX-1039] 入院情况：以“停经39周，要求住院待产”为主诉入院。入院查体：生命体征平稳，心肺\n[BBOX-1040] 听诊未闻及异常。腹隆，晚孕腹型，肝脾肋下未触及。专科检查：宫高34CM，腹围102CM，估\n[BBOX-1041] 计胎儿体宣：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水，骨盆外\n[BBOX-1042] 测量及内诊：未做。辅助检查：B超（2020.07.02 本院）：晚孕宫内单活胎头位(双顶径\n[BBOX-1043] 9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。\n[BBOX-1044] 入院诊断：1.妊娠合并子宫瘢痕；2.孕产：宫内孕39周头位待产。\n[BBOX-1045] 诊疗经过：患者入院后完善相关检查，要求剖宫产，于2020年07月09日 08：29-09：30在\n[BBOX-1046] 腰硬联合麻醉+基础麻醉下行二次于宫下段剖宫产术+子宫修补术。取下腹原横切口，剔除原瘢\n[BBOX-1047] 痕，逐层进腹，膀下指膀胱，暴露子宫下段，可见子宫下段肌层较薄，胎儿头发及胎脂漂浮，\n[BBOX-1048] 切开子宫后见羊水清，约600ml，吸净后以头位助娩一活男婴，出生1-10分钟均评10分，胎盘\n[BBOX-1049] 胎膜自娩完整，子宫收缩可，纱布球擦拭子宫腔，可见子宫下段肌层断裂，用可吸收线间断缝\n[BBOX-1050] 合子宫下段肌层，断裂的立皆给予缝合，以伦桥可吸收线分两层连续缝合子宫切口。探查子宫\n[BBOX-1051] 切口无活动性出血，双侧附件外观正常，关腹，术程顺利，术中出血不多，术后予以降压、抗\n[BBOX-1052] 感染、加强宫缩支持及对症治疗。\n[BBOX-1053] 出院诊断：1.妊娠合并子宫瘢痕；2.孕产：宫内孕39+周头位剖宫产：\n[BBOX-1054] 出院情况：患者精神、饮食好，无特殊不适。查体：生命体征平稳，心肺听诊未闻及明显\n[BBOX-1055] 异常，双乳泌乳量可，双乳稍涨，腹部平软，切口无红肿、渗出、硬结等愈合良好，子宫收缩\n[BBOX-1056] 好，宫底约脐耻之间，宫体无压痛，恶露呈淡红色，量少，无异味。现患者一般情况好，双乳\n[BBOX-1057] 泌乳量多，子宫复旧好，腹部切口愈合良好，无需拆线，达临床治愈，于今日出院。完成计划\n[BBOX-1058] 性剖宫产临床路径。\n[BBOX-1059] 出院医嘱：1.注意休息，合理营养；\n[BBOX-1060] 2.禁性生活、盆浴及重体力劳动2个月；\n[BBOX-1061] 3.坚持纯母乳喂养大于4-6月；\n[BBOX-1062] 第 页\n[BBOX-1063] 总第 页\n[BBOX-1064] 医院\n[BBOX-1065] 出院记录\n[BBOX-1066] 姓名：\n[BBOX-1067] 科室：产科二区\n[BBOX-1068] 床号：\n[BBOX-1069] 住院号：2\n[BBOX-1070] 4.产后42天门诊复查，如出院后出现任何异常情况请立即就诊，注意产妇心理\n[BBOX-1071] 状态，必要时心理咨询门诊就诊；若阴道出血淋漓不尽持续1月或阴道出血量多于平素月经\n[BBOX-1072] 量、腹痛、发热等，及时就诊：（每周二、周六门诊326彭琼玉副主任医师坐诊）\n[BBOX-1073] 5.严格避孕，术后六个月可安环避孕，术后2年以上方可再次妊娠：\n[BBOX-1074] 6.新生儿乙肝疫苗第一针，卡介苗已接种，新生儿生后10天补充维生素AD滴剂\n[BBOX-1075] 1粒/次，一次/日（至2岁），出院后新生儿每日测胆红素值，黄疸加重或持续14天未消退，或\n[BBOX-1076] 出院后有不适，可直接到1号楼9楼新生儿科探视大厅就诊（携带宝宝就诊卡）；\n[BBOX-1077] 7.咨询电话产科：\n[BBOX-1078] ，新生儿科：0398-3118382。母乳咨询电话：\n[BBOX-1079] 0398-3118618.\n[BBOX-1080] 主治医师：\n[BBOX-1081] 孙州\n[BBOX-1082] 临床数据中心-患者360视图\n[BBOX-1083] 返回患者查询\n[BBOX-1084] 患者姓名\n[BBOX-1085] 女 出生日\n[BBOX-1086] 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>\n[BBOX-1087] 就诊时间轴\n[BBOX-1088] 门诊号\n[BBOX-1089] 诊时间：2023-08-14 15:29:02 接诊科室：普通儿科三组（门） 接诊医生：谭真真\n[BBOX-1090] 全部\n[BBOX-1091] 近一月\n[BBOX-1092] 近三月\n[BBOX-1093] 近半年\n[BBOX-1094] 近一年\n[BBOX-1095] 近五年\n[BBOX-1096] 门诊39 住院1\n[BBOX-1097] 总览\n[BBOX-1098] 就诊列表\n[BBOX-1099] 集成视图\n[BBOX-1100] 诊断\n[BBOX-1101] 病历文书\n[BBOX-1102] 处方\n[BBOX-1103] 检验\n[BBOX-1104] 检查\n[BBOX-1105] 处置\n[BBOX-1106] 肺功能检查\n[BBOX-1107] 单机报告\n[BBOX-1108] 透析治疗\n[BBOX-1109] 费用\n[BBOX-1110] 体检报告\n[BBOX-1111] 1.\n[BBOX-1112] 门诊号.\n[BBOX-1113] 2024-04-24 普通儿科一组（...\n[BBOX-1114] 2024-04-19 普通儿科一组（...\n[BBOX-1115] 2024-04-08 妇科门诊\n[BBOX-1116] 2024-04-08 妇科一病区(门)\n[BBOX-1117] 2024-01-05 妇科一病区(门)\n[BBOX-1118] 2023-08-14 普通儿科三组（...\n[BBOX-1119] 2023-07-06 普通儿科三组（...\n[BBOX-1120] 2023-06-26 普通儿科三组（...\n[BBOX-1121] 2023-05-08 普通儿科三组（...\n[BBOX-1122] 2023-05-08 普通儿科一组（...\n[BBOX-1123] 2023-04-18 普通儿科三组（...\n[BBOX-1124] 姓名：\n[BBOX-1125] 性别：女\n[BBOX-1126] 年龄：39岁\n[BBOX-1127] 民族：汉族\n[BBOX-1128] 身份证\n[BBOX-1129] 现住址：\n[BBOX-1130] 就诊类型：初诊\n[BBOX-1131] 就诊科室：普通儿科三组（门）\n[BBOX-1132] 就诊日期：2023-08-14 15:29\n[BBOX-1133] 联系电话\n[BBOX-1134] 主诉：咽峡炎购药\n[BBOX-1135] 现病史：咽峡炎购药\n[BBOX-1136] 既往史：平素体健，无肝炎、结核类传染病史\n[BBOX-1137] 过敏史：无\n[BBOX-1138] 体格检查：发育正常，营养良好，精神一般，口唇红润，双侧扁桃体无肿大，无充血、分泌物。咽腔黏膜无充\n[BBOX-1139] 血、红肿、疱疹，双肺呼吸音清，听诊心律齐，无杂音，腹平软，无压痛、反跳痛\n[BBOX-1140] 辅助检查：\n[BBOX-1141] 初步印象：急性咽峡炎\n[BBOX-1142] 处理意见：门诊\n[BBOX-1143] 备注：\n[BBOX-1144] 医师签名：谭真真\n[BBOX-1145] 第1页\n[BBOX-1146] 门诊病历\n[BBOX-1147] 门诊号：\n[BBOX-1148] 姓名\n[BBOX-1149] 性别：女\n[BBOX-1150] 年龄：39岁\n[BBOX-1151] 民族：汉族\n[BBOX-1152] 身份证号\n[BBOX-1153] 现住址：\n[BBOX-1154] 就诊类型：急诊\n[BBOX-1155] 就诊科室：妇科一病区(门)\n[BBOX-1156] 就诊日期：2024-01-05 10:32\n[BBOX-1157] 联系电话\n[BBOX-1158] 主诉：下腹痛2小时\n[BBOX-1159] 现病史：患者月经第二天，无明显诱因出现下腹持续疼痛\n[BBOX-1160] 既往史：平素体健，无高血压、冠心病、糖尿病病史，无肝炎、结核等传染病史，无手术史\n[BBOX-1161] 婚育史：\n[BBOX-1162] 月经史：患者平素月经规律，量中等，色正常，无痛经。\n[BBOX-1163] 过敏史：无\n[BBOX-1164] 专科检查：外阴：发育正常，阴毛呈女性分布；阴道：通畅，粘膜红润，未见异常分泌物；宫颈：光滑，大小正常，宫体：正常大小，无压痛。附件：左侧附件区压痛明显。\n[BBOX-1165] 辅助检查：\n[BBOX-1166] 初步印象：女性盆腔炎性疾病\n[BBOX-1167] 处理意见：门诊治疗\n[BBOX-1168] 备注：\n[BBOX-1169] 医师签名：汪会芳\n[BBOX-1170] 第1页\n[BBOX-1171] 三门峡市中心医院门户-患者360 ×\n[BBOX-1172] ← → C ① 不安全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-1173] 临床数据中心-患者360视图\n[BBOX-1174] 返回患者查询 患者姓名:\n[BBOX-1175] 女 出\n[BBOX-1176] 期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>\n[BBOX-1177] 就诊时间轴\n[BBOX-1178] 门诊号\n[BBOX-1179] 就诊时间: 2024-04-08 09 44 02 接诊科室: 妇科一病区(门) 接诊医生: 权丽丽\n[BBOX-1180] 全部 近一月 近三月 近半年 近一年\n[BBOX-1181] 近五年\n[BBOX-1182] 门诊 39 住院1\n[BBOX-1183] 总览 就诊列表\n[BBOX-1184] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告\n[BBOX-1185] 检验报告\n[BBOX-1186] 2025-04-11 哮喘危重—病达(I J)\n[BBOX-1187] 门诊号:\n[BBOX-1188] 2025-01-06 普通儿科三组 (...\n[BBOX-1189] 2024-12-30 普通儿科三组 (...\n[BBOX-1190] 2024-07-05 普通儿科一组 (...\n[BBOX-1191] 2024-04-24 普通儿科一组 (...\n[BBOX-1192] 2024-04-19 普通儿科一组 (...\n[BBOX-1193] 2024-04-08 妇科门诊\n[BBOX-1194] 2024-04-08 妇科一病区(门)\n[BBOX-1195] 2024-01-05 妇科一病区(门)\n[BBOX-1196] 2023-08-14 普通儿科三组 (...\n[BBOX-1197] 2023-07-06 普通儿科三组 (...\n[BBOX-1198] 姓名\n[BBOX-1199] 性别: 女\n[BBOX-1200] 年龄:40岁\n[BBOX-1201] 民族: 汉族\n[BBOX-1202] 身份证号\n[BBOX-1203] 现住址:\n[BBOX-1204] 就诊类型:初诊\n[BBOX-1205] 就诊科室:妇科一病区(门)\n[BBOX-1206] 就诊日期: 2024-04-08 09:44\n[BBOX-1207] 联系电话\n[BBOX-1208] 主诉: 月经期下腹间断疼痛2个月\n[BBOX-1209] 现病史: 2024.1月经第3天左侧附件区疼痛,超声提示无异常,输消炎药后好转,2024.2无异常,2024.3月经\n[BBOX-1210] 第3天下腹疼痛但是疼痛程度较前减轻,\n[BBOX-1211] 既往史: 平素体健,无高血压、冠心病、糖尿病病史,无肝炎、结核等传染病史,无手术史\n[BBOX-1212] 婚育史:\n[BBOX-1213] 月经史: 患者平素月经规律,量中等,色正常,无痛经。\n[BBOX-1214] 过敏史: 无\n[BBOX-1215] 专科检查: 外阴:发育正常,阴毛呈女性分布;阴道:通畅,粘膜红润,未见异常分泌物;宫颈:光滑,大小\n[BBOX-1216] 正常,宫体:正常大小,无压痛。附件:双侧附件区未触及明显异常。\n[BBOX-1217] 辅助检查:\n[BBOX-1218] 初步印象: 女性盆腔炎性疾病\n[BBOX-1219] 处理意见: 门诊检查\n[BBOX-1220] 备注:\n[BBOX-1221] 医师签名: 权丽丽\n[BBOX-1222] 第1页\n[BBOX-1223] 三门峡市中心医院门户-患者360 ×\n[BBOX-1224] 临床数据中心-患者360视图\n[BBOX-1225] 返回患者查询\n[BBOX-1226] 患者姓\n[BBOX-1227] 出生\n[BBOX-1228] 期：2020-07-08\n[BBOX-1229] 最近诊疗日期：2026-02-12\n[BBOX-1230] 当前在院状态：出院\n[BBOX-1231] 过敏：无\n[BBOX-1232] 详情>>\n[BBOX-1233] 就诊时间抽\n[BBOX-1234] 1门诊号：\n[BBOX-1235] 就诊时间：2024-04-08 11:32:46\n[BBOX-1236] 接诊科室：妇科门诊\n[BBOX-1237] 接诊医生：曲丽霞\n[BBOX-1238] 全部\n[BBOX-1239] 近一月\n[BBOX-1240] 近三月\n[BBOX-1241] 近半年\n[BBOX-1242] 近一年\n[BBOX-1243] 近五年\n[BBOX-1244] 门诊诊39\n[BBOX-1245] 住院1\n[BBOX-1246] 就诊列表\n[BBOX-1247] 总览\n[BBOX-1248] 2025-04-11 收敛厄重—病区(1)\n[BBOX-1249] 2025-01-06 普通儿科三组 (\n[BBOX-1250] 2024-12-30 普通儿科三组 (\n[BBOX-1251] 2024-07-05 普通儿科一组 (\n[BBOX-1252] 2024-04-24 普通儿科一组 (\n[BBOX-1253] 2024-04-19 普通儿科一组 (\n[BBOX-1254] 2024-04-08 妇科门诊\n[BBOX-1255] 2024-04-08 妇科—病区(门)\n[BBOX-1256] 2024-01-05 妇科—病区(门)\n[BBOX-1257] 2023-08-14 普通儿科三组 (\n[BBOX-1258] 2023-07-06 普通儿科三组 (\n[BBOX-1259] 集成视图\n[BBOX-1260] 诊断\n[BBOX-1261] 病历文书\n[BBOX-1262] 处方\n[BBOX-1263] 检验\n[BBOX-1264] 检查\n[BBOX-1265] 处置\n[BBOX-1266] 肺功能检查\n[BBOX-1267] 单机报告\n[BBOX-1268] 体检报告\n[BBOX-1269] 门诊号\n[BBOX-1270] 姓名\n[BBOX-1271] 性别：女\n[BBOX-1272] 年龄：40岁\n[BBOX-1273] 民族：汉族\n[BBOX-1274] 身份证号\n[BBOX-1275] 现住址：\n[BBOX-1276] 就诊类型：初诊\n[BBOX-1277] 就诊科室：妇科门诊\n[BBOX-1278] 就诊日期：2024-04-08 11:32\n[BBOX-1279] 联系电话\n[BBOX-1280] 主诉：月经期下腹间断疼痛2个月\n[BBOX-1281] 现病史：2024.1月经第3天左侧附件区疼痛，超声提示无异常，输消炎药后好转，2024.2无异常，2024.3月经\n[BBOX-1282] 第3天下腹疼痛但是疼痛程度较前减轻，\n[BBOX-1283] 既往史：平素体健，无高血压、冠心病、糖尿病病史，无肝炎、结核等传染病史，无手术史\n[BBOX-1284] 婚育史：\n[BBOX-1285] 月经史：患者平素月经规律，量中等，色正常，无痛经。\n[BBOX-1286] 过敏史：无\n[BBOX-1287] 专科检查：外阴：发育正常，阴毛呈女性分布；阴道：通畅，粘膜红润，未见异常分泌物；宫颈：光滑，大小\n[BBOX-1288] 正常，宫体：正常大小，无压痛。附件：双侧附件区未触及明显异常。\n[BBOX-1289] 辅助检查：\n[BBOX-1290] 初步印象：女性盆腔炎性疾病\n[BBOX-1291] 处理意见：门诊检查\n[BBOX-1292] 备注：\n[BBOX-1293] 医师签名：\n[BBOX-1294] 第1页\n[BBOX-1295] <\n[BBOX-1296] →\n[BBOX-1297] C\n[BBOX-1298] ① 不安全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-1299] 临床数据中心-患者360视图\n[BBOX-1300] 返回患者查询\n[BBOX-1301] 患者姓\n[BBOX-1302] 女\n[BBOX-1303] 出生日期\n[BBOX-1304] 首诊日期：2020-07-08\n[BBOX-1305] 最近诊疗日期：2026-02-12\n[BBOX-1306] 当前在院状态：出院\n[BBOX-1307] 过敏：无\n[BBOX-1308] 详情>>\n[BBOX-1309] 就诊时间抽\n[BBOX-1310] 门诊号\n[BBOX-1311] 就诊时间：2024-04-19 08.07.40\n[BBOX-1312] 接诊科室：普通儿科一组(门)\n[BBOX-1313] 接诊医生：李婉莹\n[BBOX-1314] 全部\n[BBOX-1315] 近一月\n[BBOX-1316] 近三月\n[BBOX-1317] 近半年\n[BBOX-1318] 近一年\n[BBOX-1319] 近五年\n[BBOX-1320] ■ 门诊诊39\n[BBOX-1321] 住院1\n[BBOX-1322] 总览\n[BBOX-1323] 就诊列表\n[BBOX-1324] 2025-04-11 守议危重_病区(IJ)\n[BBOX-1325] 2025-01-06 普通儿科三组(...\n[BBOX-1326] 2024-12-30 普通儿科三组(...\n[BBOX-1327] 2024-07-05 普通儿科一组(...\n[BBOX-1328] 2024-04-24 普通儿科一组(...\n[BBOX-1329] 2024-04-19 普通儿科一组(...\n[BBOX-1330] 2024-04-08 妇科门诊\n[BBOX-1331] 2024-04-08 妇科一病区(门)\n[BBOX-1332] 2024-01-05 妇科一病区(门)\n[BBOX-1333] 2023-08-14 普通儿科三组(...\n[BBOX-1334] 2023-07-06 普通儿科三组(...\n[BBOX-1335] 集成视图\n[BBOX-1336] 诊断\n[BBOX-1337] 病历文书\n[BBOX-1338] 处方\n[BBOX-1339] 检验\n[BBOX-1340] 检查\n[BBOX-1341] 处置\n[BBOX-1342] 肺功能检查\n[BBOX-1343] 单机报告\n[BBOX-1344] 体检报告\n[BBOX-1345] 门诊号\n[BBOX-1346] 姓\n[BBOX-1347] 性别：女\n[BBOX-1348] 年龄：40岁\n[BBOX-1349] 民族：汉族\n[BBOX-1350] 身份证号：\n[BBOX-1351] 现住址：\n[BBOX-1352] 就诊类型：急诊\n[BBOX-1353] 就诊科室：普通儿科一组(门)\n[BBOX-1354] 就诊日期：2024-04-19 08:07\n[BBOX-1355] 联系电话\n[BBOX-1356] 主诉：因呼吸道感染）不适要求开药\n[BBOX-1357] 现病史：患者因（呼吸道感染）不适，要求开药（家属代开）。\n[BBOX-1358] 既往史：既往体质一般\n[BBOX-1359] 过敏史：无\n[BBOX-1360] 体格检查：神志清晰，精神一般，自主体位，查体合作\n[BBOX-1361] 辅助检查：\n[BBOX-1362] 初步印象：1、急性上呼吸道感染.2、维生素A缺乏伴夜盲症\n[BBOX-1363] 处理意见：开立药品\n[BBOX-1364] 备注：\n[BBOX-1365] 医师签名：李婉莹\n[BBOX-1366] 第1页\n[BBOX-1367] CS 扫描全能王\n[BBOX-1368] 3亿人都在用的扫描App\n[BBOX-1369] 临床数据中心-患者360视图\n[BBOX-1370] 返回患者查询\n[BBOX-1371] 患者姓\n[BBOX-1372] 别：女\n[BBOX-1373] 出生日期：\n[BBOX-1374] 就诊日期：2020-07-08\n[BBOX-1375] 最近诊疗日期：2026-02-12\n[BBOX-1376] 当前在院状态：出院\n[BBOX-1377] 过敏：无\n[BBOX-1378] 详情>>\n[BBOX-1379] 就诊时间：2025-04-11 14:47:07\n[BBOX-1380] 接诊科室：呼吸危重二病区(门)\n[BBOX-1381] 接诊医生：段竹云\n[BBOX-1382] 全部\n[BBOX-1383] 近一月\n[BBOX-1384] 近三月\n[BBOX-1385] 近半年\n[BBOX-1386] 近一年\n[BBOX-1387] 近五年\n[BBOX-1388] 门诊39\n[BBOX-1389] 住院1\n[BBOX-1390] 总览\n[BBOX-1391] 就诊列表\n[BBOX-1392] 2025-06-23 普通儿科三组 (...\n[BBOX-1393] 2025-05-09 呼吸危重二病区(门)\n[BBOX-1394] 2025-04-11 耳鼻咽喉头颈外...\n[BBOX-1395] 2025-04-11 呼吸危重二病区(门)\n[BBOX-1396] 2025-01-06 普通儿科三组 (...\n[BBOX-1397] 2024-12-30 普通儿科三组 (...\n[BBOX-1398] 2024-07-05 普通儿科一组 (...\n[BBOX-1399] 2024-04-24 普通儿科一组 (...\n[BBOX-1400] 2024-04-19 普通儿科一组 (...\n[BBOX-1401] 2024-04-08 妇科门诊\n[BBOX-1402] 2024-04-08 妇科一病区(门)\n[BBOX-1403] 集成视图\n[BBOX-1404] 诊断\n[BBOX-1405] 病历文书\n[BBOX-1406] 处方\n[BBOX-1407] 检验\n[BBOX-1408] 检查\n[BBOX-1409] 处置\n[BBOX-1410] 肺功能检查\n[BBOX-1411] 单机报告\n[BBOX-1412] 透析治疗\n[BBOX-1413] 费用\n[BBOX-1414] 体检报告\n[BBOX-1415] （总）诊病历\n[BBOX-1416] 门诊号：\n[BBOX-1417] 姓\n[BBOX-1418] 性别：女\n[BBOX-1419] 年龄：41岁\n[BBOX-1420] 民族：汉族\n[BBOX-1421] 婚姻状况：已婚\n[BBOX-1422] 身份证\n[BBOX-1423] 职业：专业技术人员\n[BBOX-1424] 现住址：\n[BBOX-1425] 就诊类型：初诊\n[BBOX-1426] 就诊科室：呼吸危重二病区(门)\n[BBOX-1427] 就诊日期：2025-04-11\n[BBOX-1428] 14:47\n[BBOX-1429] 联系电话：\n[BBOX-1430] 主诉：咳嗽憋气一周\n[BBOX-1431] 现病史：患者无发热，感冒后咳嗽、憋气一周，间断治疗，时轻时重，今日来诊\n[BBOX-1432] 既往史：平素体健，无高血压、冠心病、糖尿病病史\n[BBOX-1433] 个人史：无吸烟史\n[BBOX-1434] 过敏史：无\n[BBOX-1435] 体格检查：呼吸平稳，口唇无紫绀，听诊：双肺呼吸音清，未闻及干、湿性啰音\n[BBOX-1436] 辅助检查：肺功能检查提示中重度阻塞性肺通气功能障碍，支气管舒张试验阳性。\n[BBOX-1437] 初步印象：1、支气管哮喘(急性发作期).2、过敏性鼻炎[变应性鼻炎]\n[BBOX-1438] 处理意见：坚持门诊治疗，定期复查\n[BBOX-1439] 备注：\n[BBOX-1440] 医师签名：段竹云\n[BBOX-1441] 第1页\n[BBOX-1442] 临床数据中心-患者360视图\n[BBOX-1443] 返回患者查询\n[BBOX-1444] 就诊时间抽\n[BBOX-1445] 近五年\n[BBOX-1446] 门诊39 住院1\n[BBOX-1447] 就诊列表\n[BBOX-1448] 2025-06-23 普通儿科三组 (...\n[BBOX-1449] 2025-05-09 呼吸危重二病区(门)\n[BBOX-1450] 2025-04-11 耳鼻咽喉头颈外\n[BBOX-1451] 2025-04-11 呼吸危重二病区(门)\n[BBOX-1452] 2025-01-06 普通儿科三组 (...\n[BBOX-1453] 2024-12-30 普通儿科三组 (...\n[BBOX-1454] 2024-07-05 普通儿科一组 (...\n[BBOX-1455] 2024-04-24 普通儿科一组 (...\n[BBOX-1456] 2024-04-19 普通儿科一组 (...\n[BBOX-1457] 2024-04-08 妇科门诊\n[BBOX-1458] 2024-04-08 妇科一病区(门)\n[BBOX-1459] ]: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>\n[BBOX-1460] 就诊时间: 2025-04-11 15:43:29 接诊科室: 耳鼻咽喉头颈外科(门) 接诊医生: 刘秀层\n[BBOX-1461] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 报告\n[BBOX-1462] 门诊病历\n[BBOX-1463] 门诊号\n[BBOX-1464] 姓名\n[BBOX-1465] 性别: 女\n[BBOX-1466] 年龄:41岁\n[BBOX-1467] 民族: 汉族\n[BBOX-1468] 婚姻状况: 已婚\n[BBOX-1469] 身份证号\n[BBOX-1470] 职业: 职员\n[BBOX-1471] 现住址:\n[BBOX-1472] 就诊类型: 初诊\n[BBOX-1473] 就诊科室:耳鼻咽喉头颈外科\n[BBOX-1474] 就诊日期: 2025-04-11 15:43\n[BBOX-1475] 联系电\n[BBOX-1476] 主诉:鼻塞流涕,咳嗽憋气1周\n[BBOX-1477] 现病史:1周前发现鼻塞流涕,患者无发热,感冒后咳嗽、憋气,间断治疗,时轻时重,今日来诊\n[BBOX-1478] 既往史:平素体健,无高血压、冠心病、糖尿病病史\n[BBOX-1479] 家族史:无家族遗传病史\n[BBOX-1480] 过敏史:无\n[BBOX-1481] 体格检查:鼻腔粘膜充血,水肿,水样分泌物附着\n[BBOX-1482] 辅助检查:肺功能检查提示中重度阻塞性肺通气功能障碍,支气管舒张试验阳性。\n[BBOX-1483] 初步印象:1、支气管哮喘(急性发作期)2、过敏性鼻炎[变应性鼻炎]\n[BBOX-1484] 处理意见:坚持门诊治疗,定期复查\n[BBOX-1485] 备注:\n[BBOX-1486] 医师签名:刘秀层\n[BBOX-1487] 第1页\n[BBOX-1488] 三门峡市中心医院门户-患者360 ×\n[BBOX-1489] ← → C ① 不安全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-1490] 临床数据中心-患者360视图\n[BBOX-1491] 返回患者查询 患者姓名 : 女 出生日期\n[BBOX-1492] 日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>\n[BBOX-1493] 就诊时间轴 门诊号\n[BBOX-1494] 就诊时间: 2025-05-09 17 00 57 接诊科室: 呼吸危重二病区(门) 接诊医生: 段竹云\n[BBOX-1495] 全部 近一月 近三月 近半年 近一年\n[BBOX-1496] 近五年\n[BBOX-1497] ■ 门急诊39 住院1\n[BBOX-1498] 总览 就诊列表\n[BBOX-1499] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 体检报告\n[BBOX-1500] 11(急)诊病历\n[BBOX-1501] 门诊号:\n[BBOX-1502] 2025-11-27 普通儿科二区(...\n[BBOX-1503] 2025-11-24 普通儿科二区(...\n[BBOX-1504] 2025-09-18 普通儿科二区(...\n[BBOX-1505] 2025-07-11 普通儿科一组(...\n[BBOX-1506] 2025-06-23 普通儿科三组(...\n[BBOX-1507] 2025-05-09 呼吸危重二病区(门)\n[BBOX-1508] 2025-04-11 耳鼻咽喉头颈外...\n[BBOX-1509] 2025-04-11 呼吸危重二病区(门)\n[BBOX-1510] 2025-01-06 普通儿科三组(...\n[BBOX-1511] 2024-12-30 普通儿科三组(...\n[BBOX-1512] 2024-07-05 普通儿科一组(...\n[BBOX-1513] 性别:女\n[BBOX-1514] 年龄:41岁\n[BBOX-1515] 民族:汉族\n[BBOX-1516] 婚姻状况:已婚\n[BBOX-1517] 身份证\n[BBOX-1518] 业:专业技术人员\n[BBOX-1519] 现住址:\n[BBOX-1520] 就诊类型:复诊\n[BBOX-1521] 就诊科室:呼吸危重二病区(门)\n[BBOX-1522] 就诊日期:2025-05-09\n[BBOX-1523] 17:00\n[BBOX-1524] 联系电话\n[BBOX-1525] 主诉:咳嗽憋气一周\n[BBOX-1526] 现病史:患者无发热,感冒后咳嗽、憋气一周,间断治疗,时轻时重,今日来诊\n[BBOX-1527] 既往史:平素体健,无高血压、冠心病、糖尿病病史\n[BBOX-1528] 个人史:无吸烟史\n[BBOX-1529] 过敏史:无\n[BBOX-1530] 体格检查:听诊:双肺呼吸音清,未闻及干、湿性啰音\n[BBOX-1531] 辅助检查:肺功能检查提示中重度阻塞性肺通气功能障碍,支气管舒张试验阳性。\n[BBOX-1532] 初步印象:1、支气管哮喘.2、过敏性鼻炎[变应性鼻炎]\n[BBOX-1533] 处理意见:坚持门诊治疗,定期复查\n[BBOX-1534] 备注:\n[BBOX-1535] 医师签名:段竹云\n[BBOX-1536] 第1页\n[BBOX-1537] 三门峡市中心医院门户-惠睿360 ×\n[BBOX-1538] ← → ① 不安全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-1539] 临床数据中心-患者360视图\n[BBOX-1540] 返回患者查询 患者姓名:\n[BBOX-1541] 出生日期:\n[BBOX-1542] 期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>\n[BBOX-1543] 就诊时间轴\n[BBOX-1544] 门诊号:\n[BBOX-1545] 就诊时间: 2025-06-23 10:49:50 接诊科室: 普通儿科三组(门) 接诊医生: 谭真真\n[BBOX-1546] 全部 近一月 近三月 近半年 近一年\n[BBOX-1547] 近五年\n[BBOX-1548] 门诊39 住院1\n[BBOX-1549] 总览 就诊列表\n[BBOX-1550] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 体检报告\n[BBOX-1551] 2025-11-27 普通儿科二区 (..\n[BBOX-1552] 2025-11-24 普通儿科二区 (..\n[BBOX-1553] 2025-09-18 普通儿科二区 (..\n[BBOX-1554] 2025-07-11 普通儿科一组 (..\n[BBOX-1555] 2025-06-23 普通儿科三组 (\n[BBOX-1556] 2025-05-09 呼吸危重二病区(门)\n[BBOX-1557] 2025-04-11 耳鼻咽喉头颈外\n[BBOX-1558] 2025-04-11 呼吸危重二病区(门)\n[BBOX-1559] 2025-01-06 普通儿科三组 (..\n[BBOX-1560] 2024-12-30 普通儿科三组 (..\n[BBOX-1561] 2024-07-05 普通儿科一组 (..\n[BBOX-1562] 门诊号:\n[BBOX-1563] 姓名\n[BBOX-1564] 性别: 女\n[BBOX-1565] 年龄:41岁\n[BBOX-1566] 民族: 汉族\n[BBOX-1567] 婚姻状况: 小组\n[BBOX-1568] 身份证号:\n[BBOX-1569] 职业: 专业技术人员\n[BBOX-1570] 现住址:\n[BBOX-1571] 就诊类型:初诊\n[BBOX-1572] 就诊科室:普通儿科三组(门)\n[BBOX-1573] 就诊日期: 2025-06-23 10:49\n[BBOX-1574] 联系电话\n[BBOX-1575] 主诉: 呼吸道感染购药\n[BBOX-1576] 现病史: 呼吸道感染购药\n[BBOX-1577] 既往史: 平素体健, 无肝炎、结核类传染病史\n[BBOX-1578] 过敏史: 无\n[BBOX-1579] 体格检查: 发育正常, 营养良好, 精神一般, 口唇红润, 双侧扁桃体无肿大, 无充血、分泌物。咽腔黏膜有充\n[BBOX-1580] 血, 无红肿、疱疹, 双肺呼吸音清, 听诊心律齐, 无杂音, 腹平软, 无压痛、反跳痛\n[BBOX-1581] 辅助检查:\n[BBOX-1582] 初步印象: 上呼吸道感染\n[BBOX-1583] 处理意见: 门诊药物治疗\n[BBOX-1584] 备注:\n[BBOX-1585] 医师签名: 谭真真\n[BBOX-1586] 第1页\n[BBOX-1587] <->C ①不安全|192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-1588] 临床数据中心-患者360视图\n[BBOX-1589] 返回患者查询 患者姓 出生日期\n[BBOX-1590] 就诊日期:2020-07-08 最近诊疗日期:2026-02-12 当前在院状态:出院 过敏:无 详情>>\n[BBOX-1591] 就诊时间始 门诊号\n[BBOX-1592] 就诊时间:2025-07-1110:02:50 接诊科室:普通儿科一组(门) 接诊医生:赵艳\n[BBOX-1593] 全部 近一月 近三月 近半年 近一年\n[BBOX-1594] 近五年\n[BBOX-1595] ■ 门急诊39 住院1\n[BBOX-1596] 总览 就诊列表\n[BBOX-1597] 2025-11-27普通儿科二区(...\n[BBOX-1598] 2025-11-24普通儿科二区(...\n[BBOX-1599] 2025-09-18普通儿科二区(...\n[BBOX-1600] 2025-07-11普通儿科一组(...\n[BBOX-1601] 2025-06-23普通儿科三组(...\n[BBOX-1602] 2025-05-09呼吸危重二病区(门)\n[BBOX-1603] 2025-04-11耳鼻咽喉头颈外...\n[BBOX-1604] 2025-04-11呼吸危重二病区(门)\n[BBOX-1605] 2025-01-06普通儿科三组(...\n[BBOX-1606] 2024-12-30普通儿科三组(...\n[BBOX-1607] 2024-07-05普通儿科一组(...\n[BBOX-1608] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 体检报告\n[BBOX-1609] 一\n[BBOX-1610] 门诊号\n[BBOX-1611] 病历\n[BBOX-1612] 姓名\n[BBOX-1613] 性别:女\n[BBOX-1614] 年龄:41岁\n[BBOX-1615] 民族:汉族\n[BBOX-1616] 婚姻状况:未婚\n[BBOX-1617] 身份证\n[BBOX-1618] 职业:专业技术人员\n[BBOX-1619] 现住址:\n[BBOX-1620] 就诊类型:初诊\n[BBOX-1621] 就诊科室:普通儿科一组(门)\n[BBOX-1622] 就诊日期:2025-07-1110:02\n[BBOX-1623] 联系电话\n[BBOX-1624] 主诉:呼吸道感染购药\n[BBOX-1625] 现病史:呼吸道感染购药\n[BBOX-1626] 既往史:平素体健,无肝炎、结核类传染病史\n[BBOX-1627] 过敏史:无\n[BBOX-1628] 体格检查:发育正常,营养良好,精神一般,口唇红润,双侧扁桃体无肿大,无充血、分泌物。咽腔黏膜无充\n[BBOX-1629] 血、红肿、疱疹,双肺呼吸音清,听诊心律齐,无杂音,腹平软,无压痛、反跳痛\n[BBOX-1630] 辅助检查:\n[BBOX-1631] 初步印象:支气管炎\n[BBOX-1632] 处理意见:门诊药物治疗\n[BBOX-1633] 备注:\n[BBOX-1634] 医师签名:赵艳\n[BBOX-1635] 第1页\n[BBOX-1636] 临床数据中心-患者360视图\n[BBOX-1637] 返回患者查询\n[BBOX-1638] 患者姓名:\n[BBOX-1639] ：女 出生日期.\n[BBOX-1640] 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>\n[BBOX-1641] 就诊时间抽\n[BBOX-1642] 门诊号:\n[BBOX-1643] 就诊时间：2025-09-18 15:22:06 接诊科室：普通儿科二区（门） 接诊医生：赵艳\n[BBOX-1644] 全部 近一月 近三月 近半年 近一年\n[BBOX-1645] 近五年\n[BBOX-1646] ■ 门诊诊39 住院1\n[BBOX-1647] 总览 就诊列表\n[BBOX-1648] 2025-12-09 普通儿科二区（...\n[BBOX-1649] 2025-12-07 普通儿科二区（...\n[BBOX-1650] 2025-12-01 普通儿科二区（...\n[BBOX-1651] 2025-11-27 普通儿科二区（...\n[BBOX-1652] 2025-11-24 普通儿科二区（...\n[BBOX-1653] 2025-09-18 普通儿科二区（...\n[BBOX-1654] 2025-07-11 普通儿科一组（...\n[BBOX-1655] 2025-06-23 普通儿科三组（...\n[BBOX-1656] 2025-05-09 呼吸危重二病区(门)\n[BBOX-1657] 2025-04-11 耳鼻咽喉头颈外...\n[BBOX-1658] 2025-04-11 呼吸危重二病区(门)\n[BBOX-1659] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 请价治疗 费用 体检报告\n[BBOX-1660] 门诊病历\n[BBOX-1661] 门诊\n[BBOX-1662] 姓名:\n[BBOX-1663] 性别：女\n[BBOX-1664] 年龄:41岁\n[BBOX-1665] 民族：汉族\n[BBOX-1666] 婚姻状况：未婚\n[BBOX-1667] 身份证\n[BBOX-1668] 职业：职员\n[BBOX-1669] 现住址：\n[BBOX-1670] 就诊类型:初诊\n[BBOX-1671] 就诊科室:普通儿科二区（门）\n[BBOX-1672] 就诊日期：2025-09-18 15:22\n[BBOX-1673] 联系电话\n[BBOX-1674] 主诉：咽部疼痛伴眼部不适4天\n[BBOX-1675] 现病史：4天前无明显诱因出现咽部疼痛，伴鼻塞，伴眼部不适，无发热、呕吐、腹泻、皮疹等不适。病后精神、食欲欠佳，大小便正常。\n[BBOX-1676] 既往史：无特殊。\n[BBOX-1677] 过敏史：无\n[BBOX-1678] 体格检查：发育正常，营养良好，精神一般，呼吸平稳，双眼睑结膜充血，口唇红润，咽腔充血，无疱疹，双侧扁桃体I°，充血，无分泌物，双肺呼吸音清，未闻及干湿性啰音，听诊心律齐，无杂音，腹平软，无压痛、反跳痛，未触及包块，肠鸣音活跃，神经系统未见阳性体征。\n[BBOX-1679] 辅助检查：无\n[BBOX-1680] 初步印象：1.急性咽峡炎.2.急性变应性结膜炎\n[BBOX-1681] 处理意见：门诊治疗，动态观察病情变化，不适及时随诊。\n[BBOX-1682] 备注：\n[BBOX-1683] 医师签名：赵艳\n[BBOX-1684] 第1页\n[BBOX-1685] Le coo\n[BBOX-1686] CS 扫描全能王\n[BBOX-1687] 3亿人都在用的扫描App\n[BBOX-1688] 全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-1689] 临床数据中心\n[BBOX-1690] 0视图\n[BBOX-1691] 返回患者查询\n[BBOX-1692] 患者\n[BBOX-1693] 女 出生F\n[BBOX-1694] 就诊日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>\n[BBOX-1695] 就诊时间轴\n[BBOX-1696] 门诊\n[BBOX-1697] 诊时间: 2025-12-01 15:28:03 接诊科室: 普通儿科二区(门) 接诊医生: 赵海国\n[BBOX-1698] 全季\n[BBOX-1699] 近一月\n[BBOX-1700] 近三月\n[BBOX-1701] 近半年\n[BBOX-1702] 近一年\n[BBOX-1703] 近五年\n[BBOX-1704] 门诊急诊39 住院1\n[BBOX-1705] 总览\n[BBOX-1706] 就诊列表\n[BBOX-1707] 集成视图\n[BBOX-1708] 诊断\n[BBOX-1709] 病历文书\n[BBOX-1710] 处方\n[BBOX-1711] 检验\n[BBOX-1712] 检查\n[BBOX-1713] 处置\n[BBOX-1714] 肺功能检查\n[BBOX-1715] 单机报告\n[BBOX-1716] 透析治疗\n[BBOX-1717] 费用\n[BBOX-1718] 体检报告\n[BBOX-1719] 门诊\n[BBOX-1720] 1. 门诊病历\n[BBOX-1721] 2026-01-15 呼吸危重三病区(门)\n[BBOX-1722] 2026-01-06 妇科一病区(门)\n[BBOX-1723] 2025-12-09 普通儿科二区(...\n[BBOX-1724] 2025-12-07 普通儿科二区(...\n[BBOX-1725] 2025-12-01 普通儿科二区(...\n[BBOX-1726] 2025-11-27 普通儿科二区(...\n[BBOX-1727] 2025-11-24 普通儿科二区(...\n[BBOX-1728] 2025-09-18 普通儿科二区(...\n[BBOX-1729] 2025-07-11 普通儿科一组(...\n[BBOX-1730] 2025-06-23 普通儿科三组(...\n[BBOX-1731] 2025-05-09 呼吸危重二病区(门)\n[BBOX-1732] 姓名:\n[BBOX-1733] 性别: 女\n[BBOX-1734] 年龄:41岁\n[BBOX-1735] 民族: 汉族\n[BBOX-1736] 婚姻状况: 未...\n[BBOX-1737] 身份证:\n[BBOX-1738] 职业: 专业技术人员\n[BBOX-1739] 现住址:\n[BBOX-1740] 就诊类型:初诊\n[BBOX-1741] 就诊科室:普通儿科二区(门)\n[BBOX-1742] 就诊日期: 2025-12-01 15:28\n[BBOX-1743] 联系电\n[BBOX-1744] 主诉: 发热半天。\n[BBOX-1745] 现病史: 半天前出现发热, 最高体温38.0℃, 口服药物治疗1次, 无咳嗽, 无喘息, 无呼吸困难, 无咯血, 无腹泻、呕吐等。精神食欲一般, 大小便正常。\n[BBOX-1746] 既往史: 无。\n[BBOX-1747] 过敏史: 无\n[BBOX-1748] 体格检查: 神志清, 精神一般, 呼吸浅快, 咽充血, 扁桃体二度大, 充血, 无疱疹, 无脓点, 双肺呼吸音清,\n[BBOX-1749] 心音有力, 律齐, 腹软。\n[BBOX-1750] 辅助检查:\n[BBOX-1751] 初步印象: 急性上呼吸道感染\n[BBOX-1752] 处理意见: 口服药物, 动态观察, 不适随诊。\n[BBOX-1753] 备注:\n[BBOX-1754] 医师签名: 赵海国\n[BBOX-1755] 第1页\n[BBOX-1756] 姓名：\n[BBOX-1757] 性别：女\n[BBOX-1758] 年龄：41岁\n[BBOX-1759] 民族：汉族\n[BBOX-1760] 婚姻状况：已婚\n[BBOX-1761] 身份证号\n[BBOX-1762] 职业：专业技术人员\n[BBOX-1763] 现住址\n[BBOX-1764] 就诊类型：初诊\n[BBOX-1765] 就诊科室：妇科一病区(门)\n[BBOX-1766] 就诊日期：2026-01-06 08:36\n[BBOX-1767] 联系电话.\n[BBOX-1768] 主诉：左下腹间断疼痛1年左右来诊\n[BBOX-1769] 现病史：患者诉于2024年01月05日无明显诱因出现下腹持续疼痛行相关检查后诊断为盆腔炎性疾病后遗症，\n[BBOX-1770] 慢性盆腔痛，药物治疗后好转，慢性盆腔痛病程12月，目前疾病状态持续，未治疗。\n[BBOX-1771] 既往史：2025年11月24日-2025年12月12日本院儿科门诊就诊代家属开药，否认3个月内其他病史及合并用药/\n[BBOX-1772] 非药物治疗，现患者无盆腔炎性疾病急性发作，否认既往有子宫肌瘤、子宫内膜异位症、子宫腺肌病、结核性\n[BBOX-1773] 盆腔炎、间质性膀胱炎、异常子宫出血、盆腔淤血综合征、子宫颈高级别上皮内病变等其他病症引起相关症状\n[BBOX-1774] 者；未放置宫内节育器；无子宫及双侧附件缺如；近2周内未使用过本方案规定研究期间禁止使用的治疗（包括\n[BBOX-1775] 药物和非药物治疗）；无控制不稳定的心血管、肝、肾和血液系统、糖尿病、甲状腺疾病等严重原发性疾病；\n[BBOX-1776] 获得知情同意书前5年内未患有恶性肿瘤；否认对试验用药品过敏，包括对本品成分或者药物辅料有过敏史；否\n[BBOX-1777] 认长期酗酒、药物滥用史；无智力障碍或精神障碍；近1个月内未参加过任何干预性临床试验；患者当前不在妊\n[BBOX-1778] 娠期、哺乳期，同意在试验期间及试验结束后3个月内采取有效避孕措施。\n[BBOX-1779] 婚育史：已婚已育，孕2产2，有性生活史\n[BBOX-1780] 手术史：2016年8月31日、2020年7月9日因生产行剖宫产手术\n[BBOX-1781] 月经史：初潮12岁，既往月经周期规律，经量中，色红，无痛经，末次月经2025.12.29-2025.1.2，周期26-\n[BBOX-1782] 28天，经期5天，经量较前不变\n[BBOX-1783] 过敏史：无\n[BBOX-1784] 生命体征：2026.1.6测量身高：160.0cm 体重：51.0kg 体温：36.4℃ 脉搏：76次/分 呼吸：18次/分 血压：\n[BBOX-1785] 98/76mmHg\n[BBOX-1786] 体格检查：淋巴结、头颈部、胸部、脊柱/四肢/关节、神经系统未见异常，腹部异常（左下腹压痛，CS，研究\n[BBOX-1787] 疾病相关），皮肤黏膜异常（腹部皮肤约5-6cm剖宫产手术瘢痕，NCS），其他未查。\n[BBOX-1788] 专科检查：外阴已婚型，阴道畅，宫颈光滑，无摇举痛，有宫体压痛，无子宫活动受限或粘连固定，左侧附件\n[BBOX-1789] 区、右侧附件区压痛，无宫骶韧带增粗、变硬、触痛。\n[BBOX-1790] 辅助检查：今日按方案要求开具血常规、尿沉渣（含尿常规）、肝功八项、肾功两项、血妊娠、血沉、血清C&-\n[BBOX-1791] 125、妇科微生态、十二导联心电图、妇科阴道彩色B超检查，结果详见检查单。\n[BBOX-1792] 初步印象：盆腔痛中医辨证：主症：下腹胀痛，腰骶部胀痛、带下量多；次症：神疲乏力、口苦口腻、小便\n[BBOX-1793] 黄；舌象：舌质红、苔黄腻；脉象：脉弦滑；2026年01月06日由张丹丹医生辨证为湿热瘀阻症。 西医：盆腔炎\n[BBOX-1794] 性疾病后遗症，慢性盆腔痛\n[BBOX-1795] 处理意见：根据目前临床表现及患者情况，权丽丽医生于2026年01月06日08时38分在9号楼4楼医患沟通室向患\n[BBOX-1796] 绍“妇科千金片治疗盆腔炎性疾病后遗症（湿热瘀阻证）的随机、双盲、安慰剂平行对照、多中心临\n[BBOX-1797] 床试验”及知情同意书内容，已告知参加试验可能的风险与获益，患者已充分理解并同意参加该研究，未提出\n[BBOX-1798] 门\n[BBOX-1799] CS 扫描全能王\n[BBOX-1800] 3亿人都在用的扫描App\n[BBOX-1801] 既往史：2025年11月24日-2025年12月12日本院儿科门诊就诊代家属开药，否认3个月内其他病史及合并用药/非药物治疗，现患者无盆腔炎性疾病急性发作，否认既往有子宫肌瘤、子宫内膜异位症、子宫腺肌病、结核性盆腔炎、间质性膀胱炎、异常子宫出血、盆腔淤血综合征、子宫颈高级别上皮内病变等其他病症引起相关症状者；未放置宫内节育器；无子宫及双侧附件缺如；近2周内未使用过本方案规定研究期间禁止使用的治疗（包括药物和非药物治疗）；无控制不稳定的心血管、肝、肾和血液系统、糖尿病、甲状腺疾病等严重原发性疾病；获得知情同意书前5年内未患有恶性肿瘤；否认对试验用药品过敏，包括对本品成分或者药物辅料有过敏史；否认长期酗酒、药物滥用史；无智力障碍或精神障碍；近1个月内未参加过任何干预性临床试验；患者当前不在妊娠期、哺乳期，同意在试验期间及试验结束后3个月内采取有效避孕措施。\n[BBOX-1802] 婚育史：已婚已育，孕2产2，有性生活史\n[BBOX-1803] 手术史：2016年8月31日、2020年7月9日因生产行剖宫产手术\n[BBOX-1804] 月经史：初潮12岁，既往月经周期规律，经量中，色红，无痛经，末次月经2025.12.29-2025.1.2，周期26-28天，经期5天，经量较前不变\n[BBOX-1805] 过敏史：无\n[BBOX-1806] 生命体征：2026.1.6测量身高：160.0cm 体重：51.0kg 体温：36.4℃ 脉搏：76次/分 呼吸：18次/分 血压：98/76mmHg\n[BBOX-1807] 体格检查：淋巴结、头颈部、胸部、脊柱/四肢/关节、神经系统未见异常，腹部异常（左下腹压痛，CS，研究疾病相关），皮肤黏膜异常（腹部皮肤约5-6cm剖宫产手术瘢痕，NCS），其他未查。\n[BBOX-1808] 专科检查：外阴已婚型，阴道畅，宫颈光滑，无摇举痛，有宫体压痛，无子宫活动受限或粘连固定，左侧附件区、右侧附件区压痛，无宫骶韧带增粗、变硬、触痛。\n[BBOX-1809] 辅助检查：今日按方案要求开具血常规、尿沉渣（含尿常规）、肝功八项、肾功两项、血妊娠、血沉、血清CA-125、妇科微生态、十二导联心电图、妇科阴道彩色B超检查，结果详见检查单。\n[BBOX-1810] 初步印象：盆腔痛中医辨证：主症：下腹胀痛，腰骶部胀痛、带下量多；次症：神疲乏力、口苦口腻、小便黄；舌象：舌质红、苔黄腻；脉象：脉弦滑；2026年01月06日由张丹丹医生辨证为湿热瘀阻症。 西医：盆腔炎性疾病后遗症，慢性盆腔痛\n[BBOX-1811] 从细之间、根据目前临床表现及患者情况，权丽丽医生于2026年01月06日08时38分在9号楼4楼医患沟通室向患者“妇科千金片治疗盆腔炎性疾病后遗症（湿热瘀阻证）的随机、双盲、安慰剂平行对照、多中心临床试验”及知情同意书内容，已告知参加试验可能的风险与获益，患者已充分理解并同意参加该研究，未提出问题，患者本人于2026年01月06日08时58分签署知情同意书（版本号：V1.0 三门峡市中心医院专用版，版本日期：2025年08月05日），权丽丽医生于2026年01月06日08时59分签署知情同意书（版本号：V1.0 三门峡市中心医院专用版，版本日期：2025年08月05日），知情同意书原件一份保存于受试者文件夹，一份交给患者本人，确定患者筛选号为04011，进入试验筛选，根据方案要求，收集受试者的试验相关资料，并于今日开始进行筛选期相关检查。\n[BBOX-1812] 1.已完成体征McCormack量表评分，总分8分，回顾近1周非经期腹痛/腰骶疼痛NRS平均分为5分。\n[BBOX-1813] 2.嘱受试者合理饮食，避免过度劳累；避免盆浴和坐浴，避免穿紧身衣物和化纤内裤；注意经期卫生。\n[BBOX-1814] 3.今日结合受试者情况，2026年1月6日血清CA-125示：59.70（0.00-35.00）U/mL，符合排除标准第（8）条，筛选失败，告知受试者转为门诊常规诊疗。\n[BBOX-1815] 备注：\n[BBOX-1816] 医师签名：\n[BBOX-1817] 临床数据中心-患者360视图\n[BBOX-1818] 返回患者查询\n[BBOX-1819] 患者\n[BBOX-1820] 日期：2020-07-08\n[BBOX-1821] 最近诊疗日期：2026-02-12\n[BBOX-1822] 当前在院状态：出院\n[BBOX-1823] 过敏：无\n[BBOX-1824] 详情>>\n[BBOX-1825] 就诊时间轴\n[BBOX-1826] 门诊号\n[BBOX-1827] 时间：2026-01-15 10:56:28\n[BBOX-1828] 接诊科室：呼吸危重三病区(门)\n[BBOX-1829] 接诊医生：王辉\n[BBOX-1830] 全部\n[BBOX-1831] 近一月\n[BBOX-1832] 近三月\n[BBOX-1833] 近半年\n[BBOX-1834] 近一年\n[BBOX-1835] 近五年\n[BBOX-1836] 门诊39-住院1\n[BBOX-1837] 就诊列表\n[BBOX-1838] 总览\n[BBOX-1839] 2026-02-12 呼吸危重三病区(门)\n[BBOX-1840] 2026-01-15 呼吸危重三病区(门)\n[BBOX-1841] 2026-01-06 妇科一病区(门)\n[BBOX-1842] 2025-12-09 普通儿科二区 (...\n[BBOX-1843] 2025-12-07 普通儿科二区 (...\n[BBOX-1844] 2025-12-01 普通儿科二区 (...\n[BBOX-1845] 2025-11-27 普通儿科二区 (...\n[BBOX-1846] 2025-11-24 普通儿科二区 (...\n[BBOX-1847] 2025-09-18 普通儿科二区 (...\n[BBOX-1848] 2025-07-11 普通儿科一组 (...\n[BBOX-1849] 2025-06-23 普通儿科三组 (...\n[BBOX-1850] 集成视图\n[BBOX-1851] 诊断\n[BBOX-1852] 病历文书\n[BBOX-1853] 处方\n[BBOX-1854] 检验\n[BBOX-1855] 检查\n[BBOX-1856] 处置\n[BBOX-1857] 肺功能检查\n[BBOX-1858] 单机报告\n[BBOX-1859] 透析治疗\n[BBOX-1860] 费用\n[BBOX-1861] 体检报告\n[BBOX-1862] 门诊\n[BBOX-1863] 姓名\n[BBOX-1864] 性别：女\n[BBOX-1865] 年龄：41岁\n[BBOX-1866] 民族：汉族\n[BBOX-1867] 婚姻状况：已婚\n[BBOX-1868] 身份证号\n[BBOX-1869] 职业：其他\n[BBOX-1870] 现住址\n[BBOX-1871] 就诊类型：复诊\n[BBOX-1872] 就诊科室：呼吸危重三病区(门)\n[BBOX-1873] 就诊日期：2026-01-15\n[BBOX-1874] 10:56\n[BBOX-1875] 联系电话\n[BBOX-1876] 主诉：咳嗽憋气一周\n[BBOX-1877] 现病史：患者无发热，感冒后咳嗽、憋气一周，间断治疗，时轻时重，今日来诊\n[BBOX-1878] 既往史：平素体健，无高血压、冠心病、糖尿病病史\n[BBOX-1879] 个人史：无吸烟史\n[BBOX-1880] 过敏史：无\n[BBOX-1881] 体格检查：听诊：双肺呼吸音清，未闻及干、湿性啰音\n[BBOX-1882] 辅助检查：肺功能检查提示中重度阻塞性肺通气功能障碍，支气管舒张试验阳性。\n[BBOX-1883] 初步印象：1、支气管哮喘(急性发作期).2、过敏性鼻炎[变应性鼻炎]\n[BBOX-1884] 处理意见：坚持门诊治疗，定期复查\n[BBOX-1885] 备注\n[BBOX-1886] 医师签名：王辉\n[BBOX-1887] 第1页\n[BBOX-1888] 984-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>\n[BBOX-1889] 返回概览视图\n[BBOX-1890] 门诊号：2\n[BBOX-1891] 时间：2026-02-12 11.40.02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森\n[BBOX-1892] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告\n[BBOX-1893] 请输入药品内容，按回车键检索\n[BBOX-1894] 查询全部\n[BBOX-1895] 类型 组 药品名称[规格] 用法 频率 实际用量 总量 开立时间 开立医师\n[BBOX-1896] 药品 (320ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 320ug 1 2026-02-25 07:47:00 赵海国\n[BBOX-1897] 药品 鼻渊通窍颗粒 口服 tid 1袋 3 2026-02-12 09:40:21 谭真真\n[BBOX-1898] 药品 阿莫西林克拉维酸钾片(选) 口服(继续用药) tid 0.375g 24 2026-02-12 09:40:21 谭真真\n[BBOX-1899] 药品 (160ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 160ug 1 2026-01-17 08:04:36 彭文娟\n[BBOX-1900] 药品 (320ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 320ug 1 2026-01-17 08:04:36 彭文娟\n[BBOX-1901] 药品 磷酸奥司他韦胶囊(东阳光) 口服 bid 75mg 10 2025-12-07 10:50:33 彭文娟\n[BBOX-1902] 药品 鼻渊通窍颗粒 口服 bid 1袋 2 2025-11-27 15:02:43 烟海丽\n[BBOX-1903] 药品 盐酸氮卓斯丁滴眼液 滴眼 qid 0.01ml 1 2025-09-18 15:29:34 赵艳\n[BBOX-1904] 药品 阿莫西林克拉维酸钾片(选) 口服(继续用药) tid 0.375g 24 2025-09-18 15:25:48 赵艳\n[BBOX-1905] 药品 (成人)双黄连口服液(选) 口服 tid 20ml 2 2025-09-18 15:25:48 赵艳\n[BBOX-1906] 药品 (160ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 160ug 1 2025-07-11 10:07:36 赵艳\n[BBOX-1907] 药品 (小儿)双黄连口服液(选) 口服 tid 20ml 2 2025-06-23 10:52:35 谭真真\n[BBOX-1908] 药品 (倾尔宁片)孟鲁司特钠片(选) 口服 qn 10mg 30 2025-05-09 17:04:48 段竹云\n[BBOX-1909] 共10页 2026-02-12 1 2 3 4 > 前往 1 页\n[BBOX-1910] 50/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-1911] 984-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>\n[BBOX-1912] 时间：2026-02-12 11:40.02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森\n[BBOX-1913] 返回概览视图\n[BBOX-1914] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告\n[BBOX-1915] 请输入药品内容，按回车键检索\n[BBOX-1916] 查询全部\n[BBOX-1917] 类型 组 药品名称(规格) 用法 频率 实际用量 总量 开立时间 开立医师\n[BBOX-1918] 药品 鼻渊通窍颗粒 口服 bid 1袋 2 2025-11-27 15:02.43 烟海丽\n[BBOX-1919] 药品 盐酸氮卓斯丁滴眼液 滴眼 qid 0.01ml 1 2025-09-18 15:29.34 赵艳\n[BBOX-1920] 药品 阿莫西林克拉维酸钾片(选) 口服(继续用药) tid 0.375g 24 2025-09-18 15:25.48 赵艳\n[BBOX-1921] 药品 (成人)双黄连口服液(选) 口服 tid 20ml 2 2025-09-18 15:25.48 赵艳\n[BBOX-1922] 药品 (160ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 160ug 1 2025-07-11 10:07.36 赵艳\n[BBOX-1923] 药品 (小儿)双黄连口服液(选) 口服 tid 20ml 2 2025-06-23 10:52.35 谭真真\n[BBOX-1924] 药品 (顺尔宁片)孟鲁司特钠片(选) 口服 qn 10mg 30 2025-05-09 17:04.48 段竹云\n[BBOX-1925] 药品 (320ug)布地奈德福莫特罗粉吸入剂 吸入 bid 320ug 2 2025-05-09 17:04.48 段竹云\n[BBOX-1926] 药品 醋酸泼尼松片 口服 qm 30mg 36 2025-04-11 15:46.53 刘秀层\n[BBOX-1927] 药品 鼻炎康莫米松鼻喷雾剂(选) 喷鼻 bid 100ug 1 2025-04-11 15:31.05 段竹云\n[BBOX-1928] 药品 (顺尔宁片)孟鲁司特钠片(选) 口服 qn 10mg 5 2025-04-11 15:31.05 段竹云\n[BBOX-1929] 药品 (320ug)布地奈德福莫特罗粉吸入剂 吸入 bid 320ug 1 2025-04-11 15:31.05 段竹云\n[BBOX-1930] 药品 磷酸奥司他韦胶囊(东阳光) 口服 bid 75mg 10 2025-01-06 17:15.28 谭真真\n[BBOX-1931] 药品 氯雷他定颗粒 口服 qd 10mg 1 2024-12-30 10:40:10 谭真真\n[BBOX-1932] 共70条 20条/页 < 1 2 3 4 > 前往 1\n[BBOX-1933] /patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-1934] 84-04-02\n[BBOX-1935] 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>\n[BBOX-1936] 返回概览视图\n[BBOX-1937] 门诊时间: 2026-02-12 11:40:02 接诊科室: 呼吸危重三病区(门) 接诊医生: 孙帅森\n[BBOX-1938] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告\n[BBOX-1939] 请输入药品内容, 按回车键检索\n[BBOX-1940] 查询全部\n[BBOX-1941] 类型 组 药品名称[规格] 用法 频率 实际用量 总量 开立时间 开立医师\n[BBOX-1942] 药品 (大伊可新)维生素AD滴剂 口服 qd 2000u 3 2024-07-05 09:30:58 李婉莹\n[BBOX-1943] 药品 (普米克令舒)吸入用布地奈德混悬液 压缩雾化吸入 tid 2ml 20 2024-07-05 09:30:58 李婉莹\n[BBOX-1944] 药品 小儿豉翘清热颗粒 口服 tid 6g 3 2024-04-24 11:59:55 赵艳\n[BBOX-1945] 药品 (成人)双黄连口服液(基选) 口服 tid 20ml 3 2024-04-19 08:14:06 李婉莹\n[BBOX-1946] 药品 (强力)阿莫西林克拉维酸钾干混悬剂(选) 口服(继续用药) bid 0.457g 2 2024-04-19 08:14:06 李婉莹\n[BBOX-1947] 药品 (大伊可新)维生素AD滴剂 口服 qd 2000u 3 2024-04-19 08:14:06 李婉莹\n[BBOX-1948] 药品 (普米克令舒)吸入用布地奈德混悬液 压缩雾化吸入 tid 2ml 20 2024-04-19 08:14:06 李婉莹\n[BBOX-1949] 药品 替硝唑氯化钠注射液 静滴 qd 200ml 6 2024-01-05 10:37:47 程会芳\n[BBOX-1950] 药品 左氧氟沙星氯化钠注射液(选) 静滴 qd 0.5g 3 2024-01-05 10:37:47 程会芳\n[BBOX-1951] 药品 蒲地蓝消炎口服液 口服 tid 10ml 2 2023-08-14 15:30:23 谭真真\n[BBOX-1952] 药品 (盖克)小儿氨酚黄那敏颗粒 口服 tid 12g 2 2023-07-06 20:00:14 谭真真\n[BBOX-1953] 药品 蒲地蓝消炎口服液 口服 tid 10ml 2 2023-07-06 20:00:14 谭真真\n[BBOX-1954] 共70条 20条/页 < 1 2 3 4 > 前往 2 页\n[BBOX-1955] 50/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-1956] 984-04-02 首诊日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>\n[BBOX-1957] 返回概览视图\n[BBOX-1958] 门诊\n[BBOX-1959] 2026-02-12 11:40:02 接诊科室: 呼吸危重三病区(门) 接诊医生: 孙帅森\n[BBOX-1960] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告\n[BBOX-1961] 请输入药品内容,按回车键检索\n[BBOX-1962] 查询全部\n[BBOX-1963] 类型 组 药品名称[规格]\n[BBOX-1964] 药品 替硝唑氯化钠注射液\n[BBOX-1965] 药品 左氧氟沙星氯化钠注射液(选)\n[BBOX-1966] 药品 蒲地蓝消炎口服液\n[BBOX-1967] 药品 (盖克)小儿氨酚黄那敏颗粒\n[BBOX-1968] 药品 蒲地蓝消炎口服液\n[BBOX-1969] 药品 (小儿)双黄连口服液(选)\n[BBOX-1970] 药品 地塞米松磷酸钠注射液(选)\n[BBOX-1971] 药品 5ml灭菌注射用水\n[BBOX-1972] 药品 (扑尔敏针)马来酸氯苯那敏注射液\n[BBOX-1973] 药品 消旋山莨菪碱注射液\n[BBOX-1974] 药品 头孢克肟颗粒(选)\n[BBOX-1975] 药品 (天晴速畅)吸入用布地奈德混悬液(选)\n[BBOX-1976] 药品 (大伊可新)维生素AD滴剂\n[BBOX-1977] 用法 频率 实际用量 总量 开立时间 开立医师\n[BBOX-1978] 入\n[BBOX-1979] 静滴 qd 200ml 6 2024-01-05 10:37:47 程会芳\n[BBOX-1980] 静滴 qd 0.5g 3 2024-01-05 10:37:47 程会芳\n[BBOX-1981] 口服 tid 10ml 2 2023-08-14 15:30:23 谭真真\n[BBOX-1982] 口服 tid 12g 2 2023-07-06 20:00:14 谭真真\n[BBOX-1983] 口服 tid 10ml 2 2023-07-06 20:00:14 谭真真\n[BBOX-1984] 口服 tid 20ml 2 2023-07-06 20:00:14 谭真真\n[BBOX-1985] 外用 bid 10mg 2 2023-06-26 15:19:59 谭真真\n[BBOX-1986] 外用 bid 5ml 4 2023-06-26 15:19:59 谭真真\n[BBOX-1987] 外用 bid 20mg 2 2023-06-26 15:19:59 谭真真\n[BBOX-1988] 外用 bid 20mg 2 2023-06-26 15:19:59 谭真真\n[BBOX-1989] 口服 bid 100mg 30 2023-05-08 19:56:47 陈音\n[BBOX-1990] 压缩雾化吸入 bid 2ml 10 2023-05-08 19:52:42 段艳霞\n[BBOX-1991] 口服 qd 2000u 2 2023-05-08 19:52:42 段艳霞\n[BBOX-1992] 共70条 20条/页 < 1 2 3 4 > 前往: 2 页\n[BBOX-1993] 返回概览视图\n[BBOX-1994] 11.40.02 接诊科室: 呼吸危重三病区(门) 接诊医生: 孙帅森\n[BBOX-1995] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告\n[BBOX-1996] 请输入药品内容,按回车键检索\n[BBOX-1997] 查询全部\n[BBOX-1998] 类型 组 药品名称|规格 用法 频率 实际用量 总量 开立时间 开立医师\n[BBOX-1999] 药品 *乙2)(大伊可新)维生素AD滴剂 口服 qd 2000u 2 2023-04-07 16:29.03 陈音\n[BBOX-2000] 药品 乙1)头孢克肟颗粒(选) 口服 bid 100mg 30 2023-04-07 16:28.02 陈音\n[BBOX-2001] 药品 乙0)阿奇霉素干混悬剂 口服 qd 0.25g 1 2023-04-07 16:27:17 陈音\n[BBOX-2002] 药品 乙2)三拗片 口服 tid 2片 1 2023-04-07 16:27:17 陈音\n[BBOX-2003] 药品 乙0)富马酸酮替芬片 口服 bid 1mg 6 2023-04-07 16:27:17 陈音\n[BBOX-2004] 药品 蒲地蓝消炎口服液 口服 tid 10ml 2 2022-08-08 15:40.53 王晶\n[BBOX-2005] 药品 乙1)盐酸氨溴索口服溶液(基) 口服 bid 5ml 1 2022-05-09 19:49:32 赵海国\n[BBOX-2006] 药品 赖氨肌醇维B12口服溶液 口服 bid 10ml 3 2022-05-09 19:49:32 赵海国\n[BBOX-2007] 药品 乙0)5ml灭菌注射用水 外用 bid 20ml 4 2022-05-05 09:58:24 李凌蔚\n[BBOX-2008] 药品 乙1)(扑尔敏针)马来酸氯苯那敏注射液 外用 bid 20mg 2 2022-05-05 09:58:24 李凌蔚\n[BBOX-2009] 药品 甲)地塞米松磷酸钠注射液(基) 外用 bid 10mg 2 2022-05-05 09:58:24 李凌蔚\n[BBOX-2010] 药品 乙1)消旋山莨菪碱注射液(基) 外用 bid 20mg 2 2022-05-05 09:58:24 李凌蔚\n[BBOX-2011] 药品 赖氨肌醇维B12口服溶液 口服 bid 10ml 1 2022-05-05 09:57:04 李凌蔚\n[BBOX-2012] 药品 乙1)复合维生素B片 口服 tid 1片 100 2022-05-05 09:56:29 李凌蔚\n[BBOX-2013] 药品 用维生素004/基 口服 4 100 2022-05-05 09:56:29 李凌蔚\n[BBOX-2014] 共70条 20条/页 < 1 2 3 4 > 前往 3 页\n[BBOX-2015] 50/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-2016] 984-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>\n[BBOX-2017] 返回概览视图\n[BBOX-2018] 门.\n[BBOX-2019] J26-02-12 11.40.02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森\n[BBOX-2020] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告\n[BBOX-2021] 请输入药品内容，按回车键检索\n[BBOX-2022] 查询全部\n[BBOX-2023] 类型 组 药品名称/规格 用法 频率 实际用量 总量 开立时间 开立医师\n[BBOX-2024] 药品 口服 bid 5ml 1 2022-05-09 19.49.32 赵海国\n[BBOX-2025] 药品 乙1)盐酸氨溴索口服溶液(基) 口服 bid 10ml 3 2022-05-09 19.49.32 赵海国\n[BBOX-2026] 药品 赖氨肌醇维B12口服溶液 口服 bid 20ml 4 2022-05-05 09.58.24 李凌蔚\n[BBOX-2027] 药品 乙0)5ml灭菌注射用水 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚\n[BBOX-2028] 药品 乙1)(扑尔敏针)马来酸氯苯那敏注射液 外用 bid 10mg 2 2022-05-05 09.58.24 李凌蔚\n[BBOX-2029] 药品 甲)地塞米松磷酸钠注射液(基) 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚\n[BBOX-2030] 药品 乙1)消旋山莨菪碱注射液(基) 外用 bid 10ml 1 2022-05-05 09.57.04 李凌蔚\n[BBOX-2031] 药品 赖氨肌醇维B12口服溶液 口服 bid 1片 100 2022-05-05 09.56.29 李凌蔚\n[BBOX-2032] 药品 乙1)复合维生素B片 口服 tid 5mg 100 2022-05-05 09.56.29 李凌蔚\n[BBOX-2033] 药品 甲)维生素B2片(基) 口服 tid 50mg 2 2022-05-05 09.54.38 李凌蔚\n[BBOX-2034] 药品 乙1)头孢克肟颗粒 口服 bid 10ml 1 2022-05-05 09.54.38 李凌蔚\n[BBOX-2035] 药品 乙1)金振口服液(基) 口服 bid 3g 2 2022-04-19 16.05.18 陈媛\n[BBOX-2036] 药品 (盖克)小儿氨酚黄那敏颗粒 口服 tid 4ml 1 2022-04-19 16.05.18 陈媛\n[BBOX-2037] 药品 乙1)美敏伪麻口服溶液 口服 qid 5ml 1 2022-04-19 16.05.18 陈媛\n[BBOX-2038] 共70条 20条/页 < 1 2 3 4 > 前往 3 页\n[BBOX-2039] 184-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>\n[BBOX-2040] 返回概览视图\n[BBOX-2041] 2026-02-12 11:40:02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森\n[BBOX-2042] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告\n[BBOX-2043] 请输入药品内容,按回车键检索\n[BBOX-2044] 查询全部\n[BBOX-2045] 类型 组 药品名称(规格)\n[BBOX-2046] 药品 甲)(小儿)双黄连口服液(基)\n[BBOX-2047] 药品 (盖克)小儿氨酚黄那敏颗粒\n[BBOX-2048] 药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(基)\n[BBOX-2049] 药品 蒲地蓝消炎口服液\n[BBOX-2050] 药品 复方氨酚甲麻口服液\n[BBOX-2051] 药品 (盖克)小儿氨酚黄那敏颗粒\n[BBOX-2052] 药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(国基)\n[BBOX-2053] 药品 乙0)(普米克令舒)吸入用布地奈德混悬液(国基)\n[BBOX-2054] 药品 右旋糖酐铁颗粒\n[BBOX-2055] 药品 盐酸氨卓斯丁滴眼液\n[BBOX-2056] 用法 频率 实际用量 总量 开立时间 开立医师\n[BBOX-2057] 口服 tid 10ml 1 2022-03-26 19:51:46 谭真真\n[BBOX-2058] 口服 tid 6g 2 2022-03-26 19:51:18 谭真真\n[BBOX-2059] 口服(继续用药) bid 0.228g 2 2022-03-26 19:51:18 谭真真\n[BBOX-2060] 口服 bid 10ml 1 2022-03-26 19:51:18 谭真真\n[BBOX-2061] 口服 q6h 10ml 2 2021-11-04 17:18:07 宁秀琴\n[BBOX-2062] 口服 tid 12g 2 2021-11-04 17:18:07 宁秀琴\n[BBOX-2063] 口服(继续用药) q12h 0.45g 2 2021-11-04 17:18:07 宁秀琴\n[BBOX-2064] 压缩雾化 bid 2ml 5 2021-10-11 10:07:54 张冬梅\n[BBOX-2065] 口服 tid 1袋 80 2021-09-28 15:12:34 党建华\n[BBOX-2066] 滴双眼 bid 0.1ml 1 2021-09-09 15:18:56 史艳艳\n[BBOX-2067] 共70条 20条/页 < 1 2 3 4 > 前往 4 页\n[BBOX-2068] CS 扫描全能王\n[BBOX-2069] 3亿人都在用的扫描App\n[BBOX-2070] \\begin{tabular}{ccccccccc}\n[BBOX-2071] 报告时间: 2026-01-06\n[BBOX-2072] \\hline\n[BBOX-2073] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n[BBOX-2074] \\hline\n[BBOX-2075] {[}WBC{]}白细胞数目 & 4.28 & & & 3.5~9.5 & 10^9/L & {[}HCT{]}红细胞压积 & 37.8 & & & 35~45 & \\% \\\\\n[BBOX-2076] {[}Lym\\%{]}淋巴细胞百分比 & 28.4 & & & 20~50 & \\% & {[}MCV{]}平均红细胞体积 & 80.4 & $\\downarrow$ & & 82~100 & fL \\\\\n[BBOX-2077] {[}Mon\\%{]}单核细胞百分比 & 4.7 & & & 3~10 & \\% & {[}MCH{]}平均红细胞血红蛋白含量 & 26.0 & $\\downarrow$ & & 27~34 & pg \\\\\n[BBOX-2078] {[}Neu\\%{]}中性粒细胞百分比 & 64.4 & & & 40~75 & \\% & {[}MCHC{]}平均红细胞血红蛋白浓度 & 323 & & & 316~354 & g/L \\\\\n[BBOX-2079] {[}Eos\\%{]}嗜酸性细胞百分比 & 2.4 & & & 0.4~8 & \\% & {[}RDW-CV{]}红细胞分布宽度变异系数 & 15.2 & & & 11~16 & \\% \\\\\n[BBOX-2080] {[}Bas\\%{]}嗜碱性细胞百分比 & 0.1 & & & 0.0~1.0 & \\% & {[}RDW-SD{]}红细胞分布宽度标准差 & 43.0 & & & 35.0~56.0 & fL \\\\\n[BBOX-2081] {[}Lym\\#{]}淋巴细胞数目 & 1.22 & & & 1.1~3.2 & 10^9/L & {[}PLT{]}血小板数目 & 224 & & & 125~350 & 10^9/L \\\\\n[BBOX-2082] {[}Mon\\#{]}单核细胞数目 & 0.20 & & & 0.1~0.6 & 10^9/L & {[}MPV{]}平均血小板体积 & 8.0 & & & 6.5~12 & fL \\\\\n[BBOX-2083] {[}Neu\\#{]}中性粒细胞数目 & 2.76 & & & 1.8~6.3 & 10^9/L & {[}PDW{]}血小板分布宽度 & 16.0 & & & 9~17 & fL \\\\\n[BBOX-2084] {[}Eos\\#{]}嗜酸性细胞数目 & 0.10 & & & 0.02~0.52 & 10^9/L & {[}PCT{]}血小板压积 & 0.180 & & & 0.108~ & \\% \\\\\n[BBOX-2085] {[}Bas\\#{]}嗜碱性细胞数目 & 0.00 & & & 0.00~0.06 & 10^9/L & {[}P-LCR{]}大型血小板比率 & 15.8 & & & 11~45 & \\% \\\\\n[BBOX-2086] {[}RBC{]}红细胞数目 & 4.70 & & & 3.8~5.1 & 10^12/L & {[}IG\\%{]}未成熟粒细胞百分比 & 0.4 & & & 0.0~0.6 & \\% \\\\\n[BBOX-2087] {[}HGB{]}血红蛋白 & 122 & & & 115~150 & g/L & {[}IG\\#{]}未成熟粒细胞计数 & 0.02 & & & 0.00~0.06 & 10^9/L \\\\\n[BBOX-2088] \\hline\n[BBOX-2089] \\end{tabular}\n[BBOX-2090] \\begin{tabular}{ccccccc}\n[BBOX-2091] 报告时间: 2026-01-06\n[BBOX-2092] \\hline\n[BBOX-2093] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n[BBOX-2094] \\hline\n[BBOX-2095] {[}ESR{]}血沉 & & 7 & & 0~20 & mm/h \\\\\n[BBOX-2096] \\hline\n[BBOX-2097] \\end{tabular}\n[BBOX-2098] \\begin{tabular}{l l c c c c}\n[BBOX-2099] 报告时间: 2026-01-06\n[BBOX-2100] \\hline\n[BBOX-2101] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n[BBOX-2102] \\hline\n[BBOX-2103] [TBIL]总胆红素 & & 8.5 & & 0.0~21.0 & $\\mu$mol/L \\\\\n[BBOX-2104] [DBIL]直接胆红素 & & 2.3 & & 0.0~8.0 & $\\mu$mol/L \\\\\n[BBOX-2105] [IBIL]间接胆红素 & & 6.2 & & 0.0~13.0 & $\\mu$mol/L \\\\\n[BBOX-2106] [ALT]谷丙转氨酶 & & 12.2 & & 7~40 & U/L \\\\\n[BBOX-2107] [AST]谷草转氨酶 & & 18 & & 13~35 & U/L \\\\\n[BBOX-2108] [AST/ALT]谷草/谷丙 & & 1.48 & & 0.8~1.5 & \\\\\n[BBOX-2109] [TP]总蛋白 & & 73.6 & & 65.0~85.0 & g/L \\\\\n[BBOX-2110] [ALB]白蛋白 & & 46.0 & & 40.0~55.0 & g/L \\\\\n[BBOX-2111] [GLB]球蛋白 & & 27.6 & & 20.0~40.0 & g/L \\\\\n[BBOX-2112] [A/G]白球比值 & & 1.67 & & 1.20~2.4 & \\\\\n[BBOX-2113] [GGT]谷氨酰转肽酶 & & 9.0 & & 7~45 & U/L \\\\\n[BBOX-2114] [ALP]碱性磷酸酶 & & 66 & & 40~150 & U/L \\\\\n[BBOX-2115] [Urea]尿素 & & 4.27 & & 2.6~7.5 & mmol/L \\\\\n[BBOX-2116] [CRE]肌酐 & & 49.9 & & 41~73 & $\\mu$mol/L \\\\\n[BBOX-2117] \\hline\n[BBOX-2118] \\end{tabular}\n[BBOX-2119] \\begin{tabular}{lllll}\n[BBOX-2120] 报告时间: 2026-01-06\n[BBOX-2121] \\hline\n[BBOX-2122] \\multicolumn{2}{l}{瑞图RT-F600} & \\multicolumn{3}{c}{\\textbf{医学检验科检验报告单}} \\\\\n[BBOX-2123] \\multicolumn{2}{l}{\\textbf{白带分析仪}} & & & \\\\\n[BBOX-2124] \\hline\n[BBOX-2125] \\multicolumn{2}{l}{姓 \\quad 名:} & 送检科室: \\quad 妇科一病区(门) & 床 \\quad 号: & 样本类型: 阴道分泌物 \\\\\n[BBOX-2126] \\multicolumn{2}{l}{住院(门诊)号:} & 性 \\quad 别: \\quad 女 & 年 \\quad 龄: 41岁 & 样本状态: 正常 \\\\\n[BBOX-2127] \\multicolumn{2}{l}{检验项目: \\quad 妇科微生态} & & & \\\\\n[BBOX-2128] \\multicolumn{2}{l}{疾病诊断: \\quad 慢性盆腔痛} & & & \\\\\n[BBOX-2129] \\hline\n[BBOX-2130] \\multicolumn{5}{l}{形态学检测项目:} \\\\\n[BBOX-2131] \\multicolumn{2}{l}{细胞情况} & 结果 & 正常值范围 & 镜下所见: \\\\\n[BBOX-2132] \\multicolumn{2}{l}{清洁度} & Ⅱ & ~ ≤Ⅱ & \\\\\n[BBOX-2133] \\multicolumn{2}{l}{白细胞} & 5-15 & ≤15/HP & \\\\\n[BBOX-2134] \\multicolumn{2}{l}{红细胞} & 未检出 & ~ 未检出 & \\\\\n[BBOX-2135] \\multicolumn{2}{l}{线索细胞} & 未检出 & ~ 未检出 & \\\\\n[BBOX-2136] \\multicolumn{2}{l}{上皮细胞} & 10-15 & ~ 满视野 & \\\\\n[BBOX-2137] \\multicolumn{5}{l}{} \\\\\n[BBOX-2138] \\multicolumn{2}{l}{病原体情况:} & & & \\\\\n[BBOX-2139] \\multicolumn{2}{l}{滴虫} & 未检出 & ~ 未检出 & \\\\\n[BBOX-2140] \\multicolumn{2}{l}{菌丝} & 未检出 & ~ 未检出 & \\\\\n[BBOX-2141] \\multicolumn{2}{l}{孢子} & 未检出 & ~ 未检出 & \\\\\n[BBOX-2142] \\multicolumn{2}{l}{芽生孢子} & 未检出 & ~ 未检出 & \\\\\n[BBOX-2143] \\multicolumn{5}{l}{} \\\\\n[BBOX-2144] \\multicolumn{2}{l}{菌群情况:} & & & \\\\\n[BBOX-2145] \\multicolumn{2}{l}{菌群密集度} & ++ & ~ ++ & \\\\\n[BBOX-2146] \\multicolumn{2}{l}{多样性} & + & ~ ++ & \\\\\n[BBOX-2147] \\multicolumn{2}{l}{优势菌} & G+杆菌 & ~ G阳性杆菌 & \\\\\n[BBOX-2148] \\multicolumn{2}{l}{$\\beta$-N-乙酰氨基葡萄糖苷酶(NAG)} & - & ~ - & \\\\\n[BBOX-2149] \\multicolumn{5}{l}{} \\\\\n[BBOX-2150] \\multicolumn{2}{l}{功能学分析:} & & & \\\\\n[BBOX-2151] \\multicolumn{2}{l}{唾液酸苷酶} & - & ~ - & \\\\\n[BBOX-2152] \\multicolumn{2}{l}{白细胞酯酶} & - & ~ - & \\\\\n[BBOX-2153] \\multicolumn{2}{l}{胺试验} & - & ~ - & \\\\\n[BBOX-2154] \\multicolumn{2}{l}{脯氨酸氨基肽酶PIP} & - & ~ - & \\\\\n[BBOX-2155] \\multicolumn{2}{l}{过氧化氢(H2O2)} & + & ~ - & \\\\\n[BBOX-2156] \\multicolumn{2}{l}{pH值} & 3.8 & 3.8 ~ 4.5 & \\\\\n[BBOX-2157] \\multicolumn{2}{l}{Nugent评分2} & AV评分1 & & \\\\\n[BBOX-2158] \\hline\n[BBOX-2159] \\multicolumn{5}{l}{※ 备注:阴道微生态未见明显异常!} \\\\\n[BBOX-2160] \\hline\n[BBOX-2161] \\multicolumn{2}{l}{采集时间: 2026-01-06} & \\multicolumn{2}{l}{接收时间: 2026-01-06} & \\multicolumn{2}{l}{审核时间: 2026-01-06} \\\\\n[BBOX-2162] \\multicolumn{2}{l}{09:15} & \\multicolumn{2}{l}{09:22} & \\multicolumn{2}{l}{10:59} \\\\\n[BBOX-2163] \\multicolumn{2}{l}{送检医生: 权丽丽} & \\multicolumn{2}{l}{检验者: 伊原原} & \\multicolumn{2}{l}{审核者: 介倩倩} \\\\\n[BBOX-2164] \\multicolumn{5}{l}{打印时间: 2026/2/26 下午 3:59:58} \\\\\n[BBOX-2165] \\multicolumn{5}{l}{打印者: 网页打印} \\\\\n[BBOX-2166] \\multicolumn{5}{l}{※本报告检查结果实行互认制度, 如有疑问, 请在三天内和我们联系, 电} \\\\\n[BBOX-2167] \\hline\n[BBOX-2168] \\end{tabular}\n[BBOX-2169] \\begin{tabular}{cccccc}\n[BBOX-2170] 报告时间: 2026-01-06\n[BBOX-2171] \\hline\n[BBOX-2172] 英文 & 项目名称 & 结果 & 参考范围 & 单位 & \\\\\n[BBOX-2173] \\hline\n[BBOX-2174] \\multicolumn{6}{c}{\\textbf{[β-HCG]人绒毛膜促性腺激素}} \\\\\n[BBOX-2175] \\multicolumn{6}{c}{0.40} \\\\\n[BBOX-2176] \\multicolumn{6}{c}{非孕期 0~2.9} \\\\\n[BBOX-2177] \\multicolumn{6}{c}{0.2-1周 5~50} \\\\\n[BBOX-2178] \\multicolumn{6}{c}{1-2周 50~500} \\\\\n[BBOX-2179] \\multicolumn{6}{c}{2-3周 100~5000} \\\\\n[BBOX-2180] \\multicolumn{6}{c}{3-4周 500~10000} \\\\\n[BBOX-2181] \\multicolumn{6}{c}{4-5周 1000~50000} \\\\\n[BBOX-2182] \\multicolumn{6}{c}{5-6周 10000~100000} \\\\\n[BBOX-2183] \\multicolumn{6}{c}{6-8周 15000~200000} \\\\\n[BBOX-2184] \\multicolumn{6}{c}{mlU/ml} \\\\\n[BBOX-2185] \\hline\n[BBOX-2186] \\end{tabular}\n[BBOX-2187] \\begin{tabular}{llllll}\n[BBOX-2188] 报告时间: 2026-01-06\n[BBOX-2189] \\hline\n[BBOX-2190] 采集时间: & 2026-01-06 & 接收时间: & 2026-01-06 & 审核时间: & 2026-01-06 \\\\\n[BBOX-2191] & 09:15 & & 10:03 & & 11:06 \\\\\n[BBOX-2192] 送检医生: & 权丽丽 & 检验者: & 秦淑云 & 审核者: & 薛轩 \\\\\n[BBOX-2193] \\hline\n[BBOX-2194] \\end{tabular}\n[BBOX-2195] \\begin{tabular}{ll}\n[BBOX-2196] 报告时间: 2026-01-06\n[BBOX-2197] \\hline\n[BBOX-2198] 打印时间: & 2026/2/26 下午 \\\\\n[BBOX-2199] & 4:00:10 \\\\\n[BBOX-2200] 打印者: & 网页打印 \\\\\n[BBOX-2201] \\hline\n[BBOX-2202] \\end{tabular}\n[BBOX-2203] \\begin{tabular}{ccccccc}\n[BBOX-2204] 报告时间: 2026-01-06\n[BBOX-2205] \\hline\n[BBOX-2206] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n[BBOX-2207] \\hline\n[BBOX-2208] [OV125Ag]CA-125 & & 59.70 & $\\uparrow$ & 0.00~35.00 & U/ml \\\\\n[BBOX-2209] \\hline\n[BBOX-2210] \\end{tabular}\n[BBOX-2211] \\begin{tabular}{ccccccccc}\n[BBOX-2212] 报告时间: 2026-01-06\n[BBOX-2213] \\hline\n[BBOX-2214] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n[BBOX-2215] \\hline\n[BBOX-2216] {[}颜色{]}颜色 & 黄色 & & 清 & & & {[}尿酸结晶{]}尿酸结晶 & 0 & & & 0~15 & 个/ul \\\\\n[BBOX-2217] {[}浊度{]}浊度 & 清亮 & & 清 & & & {[}草酸钙结晶{]}草酸钙结晶 & 0 & & & 0~30 & 个/ul \\\\\n[BBOX-2218] {[}GLU{]}葡萄糖 & - & & 阴性 & & & {[}上皮细胞{]}上皮细胞 & 14 & & & 0~20 & 个/ul \\\\\n[BBOX-2219] {[}BLD{]}潜血 & - & & 阴性 & & & {[}粘液丝{]}粘液丝 & 5 & & & 0~20 & 个/ul \\\\\n[BBOX-2220] {[}LEU{]}白细胞 & 2+ & & 阴性 & & & {[}酵母菌{]}酵母菌 & 6 & $\\uparrow$ & & 0~0 & 个/ul \\\\\n[BBOX-2221] {[}PRO{]}蛋白质 & - & & 阴性 & & & {[}透明管型{]}透明管型 & 0 & & & 0~1 & 个/ul \\\\\n[BBOX-2222] {[}NIT{]}亚硝酸盐 & + & & 阴性 & & & {[}颗粒管型{]}颗粒管型 & 0 & & & 0~0 & 个/ul \\\\\n[BBOX-2223] {[}URO{]}尿胆素原 & - & & 阴性 & & & {[}小圆上皮{]}小圆上皮 & 0 & & & 0~3 & 个/ul \\\\\n[BBOX-2224] {[}BIL{]}胆红素 & - & & 阴性 & & & {[}其他管型{]}其他管型 & 0 & & & 0~0 & 个/ul \\\\\n[BBOX-2225] {[}KET{]}酮体 & - & & 阴性 & & & {[}其他上皮{]}其他上皮 & 0 & & & 0~10 & 个/ul \\\\\n[BBOX-2226] {[}Vc{]}维生素C & - & & - & & & {[}异常红细胞{]}异常红细胞 & 0 & & & 0~5 & 个/ul \\\\\n[BBOX-2227] {[}pH{]}酸碱性 & 6.0 & & & 5.0~8.5 & & {[}细菌{]}细菌 & 1072 & $\\uparrow$ & & 0~50 & 个/ul \\\\\n[BBOX-2228] {[}SG{]}比重 & 1.020 & & & 1.010~ & & {[}尿沉渣镜检{]}尿沉渣镜检 & : & & & & \\\\\n[BBOX-2229] {[}红细胞{]}红细胞 & 0 & & & 0~5 & 个/ul & {[}白细胞{]}白细胞 & +++/HP & & & $\\le$5/HP & \\\\\n[BBOX-2230] {[}白细胞{]}白细胞 & 218 & $\\uparrow$ & & 0~7 & 个/ul & {[}红细胞{]}红细胞 & 未查见 & & & $\\le$3/HP & \\\\\n[BBOX-2231] \\hline\n[BBOX-2232] \\end{tabular}\n[BBOX-2233] \\begin{tabular}{l l c c c c c}\n[BBOX-2234] 报告时间: 2026-01-15\n[BBOX-2235] \\hline\n[BBOX-2236] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n[BBOX-2237] \\hline\n[BBOX-2238] {[}PT{]}凝血酶原时间 & & 11.0 & & 9.4~12.5 & s \\\\\n[BBOX-2239] {[}INR{]}国际标准化比例 & & 0.98 & & 0.8~1.2 & INR \\\\\n[BBOX-2240] {[}HDD{]}凝血酶原活动度 & & 103.00 & & 70~130 & \\% \\\\\n[BBOX-2241] {[}APTT{]}部分凝血活酶时间(胶质硅) & & 33.7 & & 25.1~36.5 & s \\\\\n[BBOX-2242] {[}Fib{]}纤维蛋白原 & & 2.65 & & 2.00~4.00 & g/L \\\\\n[BBOX-2243] {[}TT{]}凝血酶时间 & & 15.1 & & 10.3~16.6 & s \\\\\n[BBOX-2244] \\hline\n[BBOX-2245] \\end{tabular}\n[BBOX-2246] \\begin{tabular}{ccccccccc}\n[BBOX-2247] 报告时间: 2026-01-15\n[BBOX-2248] \\hline\n[BBOX-2249] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n[BBOX-2250] \\hline\n[BBOX-2251] {[}WBC{]}白细胞数目 & 4.20 & & & 3.5~9.5 & 10^9/L & {[}HCT{]}红细胞压积 & 38.3 & & & 35~45 & \\% \\\\\n[BBOX-2252] {[}Lym\\%{]}淋巴细胞百分比 & 28.6 & & & 20~50 & \\% & {[}MCV{]}平均红细胞体积 & 81.3 & $\\downarrow$ & & 82~100 & fL \\\\\n[BBOX-2253] {[}Mon\\%{]}单核细胞百分比 & 5.0 & & & 3~10 & \\% & {[}MCH{]}平均红细胞血红蛋白含量 & 25.6 & $\\downarrow$ & & 27~34 & pg \\\\\n[BBOX-2254] {[}Neu\\%{]}中性粒细胞百分比 & 64.5 & & & 40~75 & \\% & {[}MCHC{]}平均红细胞血红蛋白浓度 & 313 & $\\downarrow$ & & 316~354 & g/L \\\\\n[BBOX-2255] {[}Eos\\%{]}嗜酸性细胞百分比 & 1.7 & & & 0.4~8 & \\% & {[}RDW-CV{]}红细胞分布宽度变异系数 & 14.9 & & & 11~16 & \\% \\\\\n[BBOX-2256] {[}Bas\\%{]}嗜碱性细胞百分比 & 0.2 & & & 0.0~1.0 & \\% & {[}RDW-SD{]}红细胞分布宽度标准差 & 43.2 & & & 35.0~56.0 & fL \\\\\n[BBOX-2257] {[}Lym\\# {]}淋巴细胞数目 & 1.20 & & & 1.1~3.2 & 10^9/L & {[}PLT{]}血小板数目 & 288 & & & 125~350 & 10^9/L \\\\\n[BBOX-2258] {[}Mon\\# {]}单核细胞数目 & 0.21 & & & 0.1~0.6 & 10^9/L & {[}MPV{]}平均血小板体积 & 9.0 & & & 6.5~12 & fL \\\\\n[BBOX-2259] {[}Neu\\# {]}中性粒细胞数目 & 2.71 & & & 1.8~6.3 & 10^9/L & {[}PDW{]}血小板分布宽度 & 15.6 & & & 9~17 & fL \\\\\n[BBOX-2260] {[}Eos\\# {]}嗜酸性细胞数目 & 0.07 & & & 0.02~0.52 & 10^9/L & {[}PCT{]}血小板压积 & 0.258 & & & 0.108~ & \\% \\\\\n[BBOX-2261] {[}Bas\\# {]}嗜碱性细胞数目 & 0.01 & & & 0.00~0.06 & 10^9/L & {[}P-LCR{]}大型血小板比率 & 19.3 & & & 11~45 & \\% \\\\\n[BBOX-2262] {[}RBC{]}红细胞数目 & 4.71 & & & 3.8~5.1 & 10^12/L & {[}IG\\%{]}未成熟粒细胞百分比 & 0.1 & & & 0.0~0.6 & \\% \\\\\n[BBOX-2263] {[}HGB{]}血红蛋白 & 120 & & & 115~150 & g/L & {[}IG\\# {]}未成熟粒细胞计数 & 0.00 & & & 0.00~0.06 & 10^9/L \\\\\n[BBOX-2264] \\hline\n[BBOX-2265] \\end{tabular}\n[BBOX-2266] \\begin{tabular}{ccccccccc}\n[BBOX-2267] 报告时间: 2026-01-15\n[BBOX-2268] \\hline\n[BBOX-2269] \\textbf{英文} & \\textbf{项目名称} & \\textbf{结果} & \\textbf{提示} & \\textbf{参考范围} & \\textbf{单位} & \\textbf{英文} & \\textbf{项目名称} & \\textbf{结果} & \\textbf{提示} & \\textbf{参考范围} & \\textbf{单位} \\\\\n[BBOX-2270] \\hline\n[BBOX-2271] {[TBIL]}总胆红素 & & 8.7 & & 0.0~21.0 & \\textmu mol/L & {[Cl]}氯 & & 105 & & 99~110 & mmol/L \\\\\n[BBOX-2272] {[DBIL]}直接胆红素 & & 3.5 & & 0.0~8.0 & \\textmu mol/L & {[Ca]}钙 & & 2.38 & & 2.11~2.52 & mmol/L \\\\\n[BBOX-2273] {[IBIL]}间接胆红素 & & 5.2 & & 0.0~13.0 & \\textmu mol/L & {[CO2cp]}二氧化碳结合力 & & 27.6 & & 21.0~31.0 & mmol/L \\\\\n[BBOX-2274] {[ALT]}谷丙转氨酶 & & 7.0 & & 7~40 & U/L & {[m-AST]}谷草转氨酶线粒体同工酶 & & 2.0 & & 0~18 & U/L \\\\\n[BBOX-2275] {[AST]}谷草转氨酶 & & 15 & & 13~35 & U/L & {[CK]}肌酸激酶 & & 37 & & 24~200 & U/L \\\\\n[BBOX-2276] {[AST/ALT]}谷草/谷丙 & 2.14 & & \\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\\n[BBOX-2277] \\begin{tabular}{ccccccccc}\n[BBOX-2278] 报告时间: 2026-01-15\n[BBOX-2279] \\hline\n[BBOX-2280] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 \\\\\n[BBOX-2281] \\hline\n[BBOX-2282] [颜色]颜色 & 黄色 & & & 黄、淡黄 & & [SG]尿比重 & 1.020 & 1.003~ \\\\\n[BBOX-2283] [浊度]浊度 & 清亮 & & & 清 & & [VC]维生素C & 0.0 & - \\\\\n[BBOX-2284] [GLU]葡萄糖 & - & & & - & & [WBC]白细胞 & 28.00 & 0~28 \\\\\n[BBOX-2285] [NQX]尿潜血 & - & & & - & mg/l & [RBC]红细胞 & 6.00 & 0~17 \\\\\n[BBOX-2286] [LEU]白细胞 & - & & & - & & [粘液丝]粘液丝 & 11 & 0~28 \\\\\n[BBOX-2287] [PRO]尿蛋白 & - & & & - & & [结晶]结晶 & 0.0 & 0~28 \\\\\n[BBOX-2288] [NIT]亚硝酸盐 & + & & & - & & [管型]管型 & 0 & 0~2 \\\\\n[BBOX-2289] [URO]尿胆原 & - & & & - & & [EC]上皮细胞 & 39.00 & 0~34 \\\\\n[BBOX-2290] [BIL]胆红素 & - & & & - & & [BACT细菌]细菌 & 163.00 & 0~7 \\\\\n[BBOX-2291] [KET]尿酮体 & - & & & - & & [BYST真菌]真菌 & 0 & 0~1 \\\\\n[BBOX-2292] [pH]pH值 & 6.0 & & & 4.5~8.0 & & & & \\\\\n[BBOX-2293] \\hline\n[BBOX-2294] \\end{tabular}\n[BBOX-2295] \\begin{tabular}{ccccccc}\n[BBOX-2296] 报告时间: 2026-01-15\n[BBOX-2297] \\hline\n[BBOX-2298] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n[BBOX-2299] \\hline\n[BBOX-2300] [FT3]游离三碘甲状腺原氨酸 & & 3.11 & & 2.14~4.21 & pg/mL \\\\\n[BBOX-2301] [FR T4]游离甲状腺素 & & 0.76 & & 0.61~1.12 & ng/dL \\\\\n[BBOX-2302] [fTSH3]超敏促甲状腺素 & & 1.350 & & 0.560~5.910 & uIU/ml \\\\\n[BBOX-2303] \\hline\n[BBOX-2304] \\end{tabular}\n[BBOX-2305] \\begin{tabular}{ccccccc}\n[BBOX-2306] 报告时间: 2026-01-15\n[BBOX-2307] \\hline\n[BBOX-2308] 英文 & 项目名称 & 结果 & SCO & 提示 & 参考范围 & 单位 \\\\\n[BBOX-2309] \\hline\n[BBOX-2310] {[HBsAg]}乙肝表面抗原(酶免法) & 阴性 & 0.04 & 阴性 & s/co \\\\\n[BBOX-2311] {[抗-HCV]}丙肝抗体(酶免法) & 阴性 & 0.15 & 阴性 & s/co \\\\\n[BBOX-2312] {[抗-HIV]}人免疫缺陷病毒抗体(酶免法) & 阴性 & 0.06 & 阴性 & s/co \\\\\n[BBOX-2313] {[TP-Ab]}梅毒螺旋体抗体(酶免法) & 阴性 & 0.07 & 阴性 & s/co \\\\\n[BBOX-2314] \\hline\n[BBOX-2315] \\end{tabular}\n[BBOX-2316] 处方笺\n[BBOX-2317] 4970401\n[BBOX-2318] 姓名：\n[BBOX-2319] 性别：□男 □女 年龄：60岁\n[BBOX-2320] 科别： 费别： 电话/住址：\n[BBOX-2321] 过敏史：无 开具日期：2021年2月16日\n[BBOX-2322] 临床诊断：支气管哮喘\n[BBOX-2323] Rp\n[BBOX-2324] 孟鲁司特钠片 10mg 2板\n[BBOX-2325] 用法：二天一次 1片\n[BBOX-2326] 审核： 调配： 医师：\n[BBOX-2327] 核对： 发药： 金额："
  }
]
2026-08-06 10:35:50,003 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:35:50,036 INFO     30 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-06 10:35:50,037 INFO     30 [Trace] task=dfc102e2 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "458 items", "markdown": "", "text": "", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 4, \"chunks_Clinical\": 1, \"chunks_LabExam\": 2}"}
2026-08-06 10:35:50,037 INFO     30 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-06 10:35:50,065 INFO     30 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 10:35:50,066 INFO     30 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-06 10:35:50,066 INFO     30 [qwen-vl-text] positions(23): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 10:35:50,066 INFO     30 [qwen-vl-text] page grouping: [4], lines per page: [23]
2026-08-06 10:35:50,465 INFO     30 [qwen-vl-text] page=4, rect=842x595, img=(2339x1654), dpi=200
2026-08-06 10:35:50,467 INFO     30 [qwen-vl-text] LLM extraction start, text_len=332
2026-08-06 10:35:50,467 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:35:50,467 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 115, \"bbox_end\": 137, \"encounter_dates\": [\"2025-05-23\"], \"department\": \"胸外二科病区\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "河北省人民医院\n病理检查报告单\n病理号\n姓名:\n性别: 女\n年龄: 74岁\n送检单位: 本院\n科别: 胸外二科病区\n住院号\n床号:\n送检日期: 2025-05-23 16:44\n送检材料: 左肺穿刺数条:\n临床诊断: 左肺占位\n图像:\n大体检查:\n(左肺穿刺数条:)穿刺组织3条, 长共3cm, 直径0.1cm。\n病理诊断:\n(左肺)穿刺组织: 浸润性癌, 类型待免疫组化助诊。\n诊断医师:\n郑国卿 王彤彤\n日期: 2025-05-26 14:23\n注:1.此报告仅供临床医师参考, 如有异议请在两日内与诊断医师联系。 电话: (0311)85988183\n2.国家规定小标本(咬检及穿刺组织)3个工作日内出报告; 其余标本5个工作日内出报告(特殊处理标本除外)。",
    "role": "user"
  }
]
2026-08-06 10:35:52,621 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:35:52,622 INFO     30 [qwen-vl-text] LLM output (len=391):
{
  "exam_date": "2025-05-23",
  "report_date": "2025-05-26",
  "exam_name": "病理检查",
  "exam_category": "pathology",
  "body_part": "左肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": "胸外二科病区",
  "bed_number": null,
  "findings": "大体检查:\n(左肺穿刺数条:)穿刺组织3条, 长共3cm, 直径0.1cm。",
  "conclusion": "病理诊断:\n(左肺)穿刺组织: 浸润性癌, 类型待免疫组化助诊。",
  "physician": "郑国卿 王彤彤",
  "reviewer": null
}
2026-08-06 10:35:52,632 INFO     30 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1228635, prompt_len=1014
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共23行）
["河北省人民医院", "病理检查报告单", "病理号", "姓名:", "性别: 女", "年龄: 74岁", "送检单位: 本院", "科别: 胸外二科病区", "住院号", "床号:", "送检日期: 2025-05-23 16:44", "送检材料: 左肺穿刺数条:", "临床诊断: 左肺占位", "图像:", "大体检查:", "(左肺穿刺数条:)穿刺组织3条, 长共3cm, 直径0.1cm。", "病理诊断:", "(左肺)穿刺组织: 浸润性癌, 类型待免疫组化助诊。", "诊断医师:", "郑国卿 王彤彤", "日期: 2025-05-26 14:23", "注:1.此报告仅供临床医师参考, 如有异议请在两日内与诊断医师联系。 电话: (0311)85988183", "2.国家规定小标本(咬检及穿刺组织)3个工作日内出报告; 其余标本5个工作日内出报告(特殊处理标本除外)。"]

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
2026-08-06 10:36:01,035 INFO     30 [qwen-vl-text] coord API raw response (len=1347):
[
	{"text": "河北省人民医院", "bbox": [431, 113, 554, 131]},
	{"text": "病理检查报告单", "bbox": [435, 147, 548, 169]},
	{"text": "病理号", "bbox": [325, 189, 350, 201]},
	{"text": "姓名:", "bbox": [325, 211, 346, 224]},
	{"text": "性别: 女", "bbox": [427, 211, 460, 224]},
	{"text": "年龄: 74岁", "bbox": [505, 211, 544, 224]},
	{"text": "送检单位: 本院", "bbox": [561, 211, 618, 224]},
	{"text": "科别: 胸外二科病区", "bbox": [325, 233, 398, 246]},
	{"text": "住院号", "bbox": [427, 233, 451, 246]},
	{"text": "床号:", "bbox": [505, 233, 524, 246]},
	{"text": "送检日期: 2025-05-23 16:44", "bbox": [561, 233, 667, 246]},
	{"text": "送检材料: 左肺穿刺数条:", "bbox": [325, 254, 419, 267]},
	{"text": "临床诊断: 左肺占位", "bbox": [505, 254, 578, 267]},
	{"text": "图像:", "bbox": [325, 280, 346, 292]},
	{"text": "大体检查:", "bbox": [325, 465, 361, 478]},
	{"text": "(左肺穿刺数条:)穿刺组织3条, 长共3cm, 直径0.1cm。", "bbox": [329, 485, 555, 499]},
	{"text": "病理诊断:", "bbox": [325, 528, 364, 541]},
	{"text": "(左肺)穿刺组织: 浸润性癌, 类型待免疫组化助诊。", "bbox": [329, 549, 545, 563]},
	{"text": "诊断医师:", "bbox": [322, 805, 359, 818]},
	{"text": "郑国卿 王彤彤", "bbox": [371, 785, 459, 817]},
	{"text": "日期: 2025-05-26 14:23", "bbox": [575, 805, 670, 819]},
	{"text": "注:1.此报告仅供临床医师参考, 如有异议请在两日内与诊断医师联系。 电话: (0311)85988183", "bbox": [322, 828, 592, 840]},
	{"text": "2.国家规定小标本(咬检及穿刺组织)3个工作日内出报告; 其余标本5个工作日内出报告(特殊处理标本除外)。", "bbox": [330, 839, 640, 851]}
]
2026-08-06 10:36:01,036 INFO     30 [qwen-vl-text] coord API: raw_items=23, valid_items=23, elapsed=8.4s
2026-08-06 10:36:01,036 INFO     30 [qwen-vl-text] coord item[0]: text=河北省人民医院, bbox=[431, 113, 554, 131]
2026-08-06 10:36:01,036 INFO     30 [qwen-vl-text] coord item[1]: text=病理检查报告单, bbox=[435, 147, 548, 169]
2026-08-06 10:36:01,036 INFO     30 [qwen-vl-text] coord item[2]: text=病理号, bbox=[325, 189, 350, 201]
2026-08-06 10:36:01,036 INFO     30 [qwen-vl-text] coord item[3]: text=姓名:, bbox=[325, 211, 346, 224]
2026-08-06 10:36:01,036 INFO     30 [qwen-vl-text] coord item[4]: text=性别: 女, bbox=[427, 211, 460, 224]
2026-08-06 10:36:01,037 INFO     30 [qwen-vl-text] coord item[5]: text=年龄: 74岁, bbox=[505, 211, 544, 224]
2026-08-06 10:36:01,037 INFO     30 [qwen-vl-text] coord item[6]: text=送检单位: 本院, bbox=[561, 211, 618, 224]
2026-08-06 10:36:01,037 INFO     30 [qwen-vl-text] coord item[7]: text=科别: 胸外二科病区, bbox=[325, 233, 398, 246]
2026-08-06 10:36:01,037 INFO     30 [qwen-vl-text] coord item[8]: text=住院号, bbox=[427, 233, 451, 246]
2026-08-06 10:36:01,038 INFO     30 [qwen-vl-text] coord item[9]: text=床号:, bbox=[505, 233, 524, 246]
2026-08-06 10:36:01,038 INFO     30 [qwen-vl-text] coord item[10]: text=送检日期: 2025-05-23 16:44, bbox=[561, 233, 667, 246]
2026-08-06 10:36:01,038 INFO     30 [qwen-vl-text] coord item[11]: text=送检材料: 左肺穿刺数条:, bbox=[325, 254, 419, 267]
2026-08-06 10:36:01,039 INFO     30 [qwen-vl-text] coord item[12]: text=临床诊断: 左肺占位, bbox=[505, 254, 578, 267]
2026-08-06 10:36:01,039 INFO     30 [qwen-vl-text] coord item[13]: text=图像:, bbox=[325, 280, 346, 292]
2026-08-06 10:36:01,039 INFO     30 [qwen-vl-text] coord item[14]: text=大体检查:, bbox=[325, 465, 361, 478]
2026-08-06 10:36:01,039 INFO     30 [qwen-vl-text] coord item[15]: text=(左肺穿刺数条:)穿刺组织3条, 长共3cm, 直径0.1cm。, bbox=[329, 485, 555, 499]
2026-08-06 10:36:01,039 INFO     30 [qwen-vl-text] coord item[16]: text=病理诊断:, bbox=[325, 528, 364, 541]
2026-08-06 10:36:01,039 INFO     30 [qwen-vl-text] coord item[17]: text=(左肺)穿刺组织: 浸润性癌, 类型待免疫组化助诊。, bbox=[329, 549, 545, 563]
2026-08-06 10:36:01,040 INFO     30 [qwen-vl-text] coord item[18]: text=诊断医师:, bbox=[322, 805, 359, 818]
2026-08-06 10:36:01,040 INFO     30 [qwen-vl-text] coord item[19]: text=郑国卿 王彤彤, bbox=[371, 785, 459, 817]
2026-08-06 10:36:01,040 INFO     30 [qwen-vl-text] coord item[20]: text=日期: 2025-05-26 14:23, bbox=[575, 805, 670, 819]
2026-08-06 10:36:01,040 INFO     30 [qwen-vl-text] coord item[21]: text=注:1.此报告仅供临床医师参考, 如有异议请在两日内与诊断医师联系。 电话: (0311)85988183, bbox=[322, 828, 592, 840]
2026-08-06 10:36:01,040 INFO     30 [qwen-vl-text] coord item[22]: text=2.国家规定小标本(咬检及穿刺组织)3个工作日内出报告; 其余标本5个工作日内出报告(特殊处理标本除外)。, bbox=[330, 839, 640, 851]
2026-08-06 10:36:01,041 INFO     30 [qwen-vl-text] page=4 — 23/23 coords, api_time=8.4s
2026-08-06 10:36:01,041 INFO     30 [qwen-vl-text] new_positions (23):
[[4, 362.8545963134766, 466.4070681152344, 67.26618811035156, 77.9811561279297], [4, 366.2221563720703, 461.35572802734373, 87.50557214355469, 100.60164416503906], [4, 273.6142547607422, 294.6615051269531, 112.50716418457031, 119.65047619628906], [4, 273.6142547607422, 291.2939450683594, 125.60323620605469, 133.34182421875], [4, 359.4870362548828, 387.26940673828125, 125.60323620605469, 133.34182421875], [4, 425.15445739746093, 457.98816796875, 125.60323620605469, 133.34182421875], [4, 472.30029821777345, 520.2880290527344, 125.60323620605469, 133.34182421875], [4, 273.6142547607422, 335.07222583007814, 138.69930822753906, 146.43789624023438], [4, 359.4870362548828, 379.6923966064453, 138.69930822753906, 146.43789624023438], [4, 425.15445739746093, 441.15036767578124, 138.69930822753906, 146.43789624023438], [4, 472.30029821777345, 561.5406397705078, 138.69930822753906, 146.43789624023438], [4, 273.6142547607422, 352.75191613769533, 151.20010424804687, 158.9386922607422], [4, 425.15445739746093, 486.61242846679687, 151.20010424804687, 158.9386922607422], [4, 273.6142547607422, 291.2939450683594, 166.6772802734375, 173.82059228515627], [4, 273.6142547607422, 303.92229528808593, 276.8033404541016, 284.5419284667969], [4, 276.9818148193359, 467.2489581298828, 288.7088604736328, 297.0427244873047], [4, 273.6142547607422, 306.44796533203123, 314.305728515625, 322.04431652832034], [4, 276.9818148193359, 458.83005798339843, 326.8065245361328, 335.1403885498047], [4, 271.08858471679684, 302.23851525878905, 479.19718078613283, 486.9357687988281], [4, 312.3411954345703, 386.42751672363283, 467.2916607666016, 486.3404927978516], [4, 484.0867584228516, 564.0663098144531, 479.19718078613283, 487.5310447998047], [4, 271.08858471679684, 498.398888671875, 492.8885288085938, 500.03184082031254], [4, 277.8237048339844, 538.809609375, 499.43656481933596, 506.5798768310547]]
2026-08-06 10:36:01,042 INFO     30 [qwen-vl-text] ═══ DONE ═══ 23 positions, pages=1, time=11.0s
2026-08-06 10:36:01,042 INFO     30 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 10:36:01,042 INFO     30 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-06 10:36:01,043 INFO     30 [qwen-vl-text] positions(21): [[4, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 10:36:01,043 INFO     30 [qwen-vl-text] page grouping: [4, 5], lines per page: [1, 20]
2026-08-06 10:36:01,459 INFO     30 [qwen-vl-text] page=4, rect=842x595, img=(2339x1654), dpi=200
2026-08-06 10:36:01,928 INFO     30 [qwen-vl-text] page=5, rect=842x595, img=(2339x1654), dpi=200
2026-08-06 10:36:01,930 INFO     30 [qwen-vl-text] LLM extraction start, text_len=382
2026-08-06 10:36:01,930 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:36:01,930 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 138, \"bbox_end\": 158, \"encounter_dates\": [\"2025-05-23\"], \"department\": \"胸外二科病区\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "住院病历\n河北省人民医院\n病理检查补充报告单\n病理号:\n姓名:\n性别: 女\n年龄: 74岁\n送检单位: 本院\n科别: 胸外二科病区\n住院号:\n床号:\n送检日期: 2025-05-23 16:44\n送检材料: 左肺穿刺数条:\n临床诊断: 左肺占位\n补充病理诊断:\n(左肺)穿刺组织: 结合免疫组化染色支持小细胞癌。\n免疫组化染色: CKpan (+), Vimentin (-), CK7 (+), TTF-1 (+), NapsinA (-), CK5/6\n(-), P40 (-), P63 (-), CgA (+), Syn (+), CD56 (+), Ki-67 (90%+)。\n诊断医师: 康林 郑国娜\n报告日期: 2025-05-27 16:\n注: 此报告仅供临床医师参考, 如有异议或病情有新变化务请及时与病理诊断医师联系(电话: 85988409)",
    "role": "user"
  }
]
2026-08-06 10:36:04,516 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:36:04,517 INFO     30 [qwen-vl-text] LLM output (len=483):
{
  "exam_date": "2025-05-23",
  "report_date": "2025-05-27",
  "exam_name": "病理检查补充报告",
  "exam_category": "pathology",
  "body_part": "左肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": "胸外二科病区",
  "bed_number": null,
  "findings": "(左肺)穿刺组织: 结合免疫组化染色支持小细胞癌。",
  "conclusion": "免疫组化染色: CKpan (+), Vimentin (-), CK7 (+), TTF-1 (+), NapsinA (-), CK5/6 (-), P40 (-), P63 (-), CgA (+), Syn (+), CD56 (+), Ki-67 (90%+)。",
  "physician": "康林 郑国娜",
  "reviewer": null
}
2026-08-06 10:36:04,523 INFO     30 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1228635, prompt_len=619
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["住院病历"]

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
2026-08-06 10:36:05,412 INFO     30 [qwen-vl-text] coord API raw response (len=63):
```json
[
	{"text": "住院病历", "bbox": [547, 840, 584, 855]}
]
```
2026-08-06 10:36:05,413 INFO     30 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=0.9s
2026-08-06 10:36:05,413 INFO     30 [qwen-vl-text] coord item[0]: text=住院病历, bbox=[547, 840, 584, 855]
2026-08-06 10:36:05,413 INFO     30 [qwen-vl-text] page=4 — 1/1 coords, api_time=0.9s
2026-08-06 10:36:05,418 INFO     30 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1426754, prompt_len=1050
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共20行）
["河北省人民医院", "病理检查补充报告单", "病理号:", "姓名:", "性别: 女", "年龄: 74岁", "送检单位: 本院", "科别: 胸外二科病区", "住院号:", "床号:", "送检日期: 2025-05-23 16:44", "送检材料: 左肺穿刺数条:", "临床诊断: 左肺占位", "补充病理诊断:", "(左肺)穿刺组织: 结合免疫组化染色支持小细胞癌。", "免疫组化染色: CKpan (+), Vimentin (-), CK7 (+), TTF-1 (+), NapsinA (-), CK5/6", "(-), P40 (-), P63 (-), CgA (+), Syn (+), CD56 (+), Ki-67 (90%+)。", "诊断医师: 康林 郑国娜", "报告日期: 2025-05-27 16:", "注: 此报告仅供临床医师参考, 如有异议或病情有新变化务请及时与病理诊断医师联系(电话: 85988409)"]

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
2026-08-06 10:36:13,052 INFO     30 [qwen-vl-text] coord API raw response (len=1260):
[
	{"text": "河北省人民医院", "bbox": [421, 152, 552, 171]},
	{"text": "病理检查补充报告单", "bbox": [410, 196, 564, 220]},
	{"text": "病理号:", "bbox": [311, 250, 341, 263]},
	{"text": "姓名:", "bbox": [311, 274, 333, 287]},
	{"text": "性别: 女", "bbox": [412, 273, 454, 287]},
	{"text": "年龄: 74岁", "bbox": [496, 273, 544, 287]},
	{"text": "送检单位: 本院", "bbox": [560, 273, 623, 287]},
	{"text": "科别: 胸外二科病区", "bbox": [311, 296, 393, 309]},
	{"text": "住院号:", "bbox": [412, 296, 443, 309]},
	{"text": "床号:", "bbox": [496, 296, 517, 309]},
	{"text": "送检日期: 2025-05-23 16:44", "bbox": [560, 296, 674, 309]},
	{"text": "送检材料: 左肺穿刺数条:", "bbox": [311, 319, 412, 332]},
	{"text": "临床诊断: 左肺占位", "bbox": [496, 319, 575, 332]},
	{"text": "补充病理诊断:", "bbox": [311, 353, 385, 369]},
	{"text": "(左肺)穿刺组织: 结合免疫组化染色支持小细胞癌。", "bbox": [315, 373, 513, 386]},
	{"text": "免疫组化染色: CKpan (+), Vimentin (-), CK7 (+), TTF-1 (+), NapsinA (-), CK5/6", "bbox": [312, 387, 661, 400]},
	{"text": "(-), P40 (-), P63 (-), CgA (+), Syn (+), CD56 (+), Ki-67 (90%+)。", "bbox": [315, 400, 618, 413]},
	{"text": "诊断医师: 康林 郑国娜", "bbox": [317, 789, 454, 819]},
	{"text": "报告日期: 2025-05-27 16:", "bbox": [545, 797, 663, 813]},
	{"text": "注: 此报告仅供临床医师参考, 如有异议或病情有新变化务请及时与病理诊断医师联系(电话: 85988409)", "bbox": [318, 827, 640, 840]}
]
2026-08-06 10:36:13,053 INFO     30 [qwen-vl-text] coord API: raw_items=20, valid_items=20, elapsed=7.6s
2026-08-06 10:36:13,053 INFO     30 [qwen-vl-text] coord item[0]: text=河北省人民医院, bbox=[421, 152, 552, 171]
2026-08-06 10:36:13,053 INFO     30 [qwen-vl-text] coord item[1]: text=病理检查补充报告单, bbox=[410, 196, 564, 220]
2026-08-06 10:36:13,053 INFO     30 [qwen-vl-text] coord item[2]: text=病理号:, bbox=[311, 250, 341, 263]
2026-08-06 10:36:13,053 INFO     30 [qwen-vl-text] coord item[3]: text=姓名:, bbox=[311, 274, 333, 287]
2026-08-06 10:36:13,054 INFO     30 [qwen-vl-text] coord item[4]: text=性别: 女, bbox=[412, 273, 454, 287]
2026-08-06 10:36:13,054 INFO     30 [qwen-vl-text] coord item[5]: text=年龄: 74岁, bbox=[496, 273, 544, 287]
2026-08-06 10:36:13,054 INFO     30 [qwen-vl-text] coord item[6]: text=送检单位: 本院, bbox=[560, 273, 623, 287]
2026-08-06 10:36:13,054 INFO     30 [qwen-vl-text] coord item[7]: text=科别: 胸外二科病区, bbox=[311, 296, 393, 309]
2026-08-06 10:36:13,054 INFO     30 [qwen-vl-text] coord item[8]: text=住院号:, bbox=[412, 296, 443, 309]
2026-08-06 10:36:13,054 INFO     30 [qwen-vl-text] coord item[9]: text=床号:, bbox=[496, 296, 517, 309]
2026-08-06 10:36:13,054 INFO     30 [qwen-vl-text] coord item[10]: text=送检日期: 2025-05-23 16:44, bbox=[560, 296, 674, 309]
2026-08-06 10:36:13,054 INFO     30 [qwen-vl-text] coord item[11]: text=送检材料: 左肺穿刺数条:, bbox=[311, 319, 412, 332]
2026-08-06 10:36:13,054 INFO     30 [qwen-vl-text] coord item[12]: text=临床诊断: 左肺占位, bbox=[496, 319, 575, 332]
2026-08-06 10:36:13,054 INFO     30 [qwen-vl-text] coord item[13]: text=补充病理诊断:, bbox=[311, 353, 385, 369]
2026-08-06 10:36:13,054 INFO     30 [qwen-vl-text] coord item[14]: text=(左肺)穿刺组织: 结合免疫组化染色支持小细胞癌。, bbox=[315, 373, 513, 386]
2026-08-06 10:36:13,054 INFO     30 [qwen-vl-text] coord item[15]: text=免疫组化染色: CKpan (+), Vimentin (-), CK7 (+), TTF-1 (+), NapsinA (-), CK5/6, bbox=[312, 387, 661, 400]
2026-08-06 10:36:13,054 INFO     30 [qwen-vl-text] coord item[16]: text=(-), P40 (-), P63 (-), CgA (+), Syn (+), CD56 (+), Ki-67 (90%+)。, bbox=[315, 400, 618, 413]
2026-08-06 10:36:13,055 INFO     30 [qwen-vl-text] coord item[17]: text=诊断医师: 康林 郑国娜, bbox=[317, 789, 454, 819]
2026-08-06 10:36:13,055 INFO     30 [qwen-vl-text] coord item[18]: text=报告日期: 2025-05-27 16:, bbox=[545, 797, 663, 813]
2026-08-06 10:36:13,055 INFO     30 [qwen-vl-text] coord item[19]: text=注: 此报告仅供临床医师参考, 如有异议或病情有新变化务请及时与病理诊断医师联系(电话: 85988409), bbox=[318, 827, 640, 840]
2026-08-06 10:36:13,056 INFO     30 [qwen-vl-text] page=5 — 20/20 coords, api_time=7.6s
2026-08-06 10:36:13,056 INFO     30 [qwen-vl-text] new_positions (21):
[[4, 460.5138380126953, 491.6637685546875, 500.03184082031254, 508.96098083496094], [5, 354.43569616699216, 464.7232880859375, 90.4819521484375, 101.7921961669922], [5, 345.1749060058594, 474.82596826171874, 116.67409619140625, 130.96072021484375], [5, 261.82779455566407, 287.0844949951172, 148.81900024414062, 156.55758825683594], [5, 261.82779455566407, 280.3493748779297, 163.10562426757812, 170.84421228027344], [5, 346.85868603515627, 382.2180666503906, 162.51034826660157, 170.84421228027344], [5, 417.577447265625, 457.98816796875, 162.51034826660157, 170.84421228027344], [5, 471.458408203125, 524.4974791259766, 162.51034826660157, 170.84421228027344], [5, 261.82779455566407, 330.86277575683596, 176.2016962890625, 183.94028430175783], [5, 346.85868603515627, 372.9572764892578, 176.2016962890625, 183.94028430175783], [5, 417.577447265625, 435.2571375732422, 176.2016962890625, 183.94028430175783], [5, 471.458408203125, 567.4338698730469, 176.2016962890625, 183.94028430175783], [5, 261.82779455566407, 346.85868603515627, 189.89304431152345, 197.63163232421877], [5, 417.577447265625, 484.0867584228516, 189.89304431152345, 197.63163232421877], [5, 261.82779455566407, 324.1276556396484, 210.13242834472658, 219.65684436035158], [5, 265.19535461425784, 431.8895775146484, 222.03794836425783, 229.77653637695315], [5, 262.6696845703125, 556.4892996826172, 230.3718123779297, 238.11040039062502], [5, 265.19535461425784, 520.2880290527344, 238.11040039062502, 245.84898840332033], [5, 266.87913464355466, 382.2180666503906, 469.67276477050785, 487.5310447998047], [5, 458.83005798339843, 558.173079711914, 474.43497277832034, 483.9593887939453], [5, 267.72102465820313, 538.809609375, 492.2932528076172, 500.03184082031254]]
2026-08-06 10:36:13,056 INFO     30 [qwen-vl-text] ═══ DONE ═══ 21 positions, pages=2, time=12.0s
2026-08-06 10:36:13,056 INFO     30 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 10:36:13,056 INFO     30 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-06 10:36:13,056 INFO     30 [qwen-vl-text] positions(48): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 10:36:13,057 INFO     30 [qwen-vl-text] page grouping: [6], lines per page: [48]
2026-08-06 10:36:13,315 INFO     30 [qwen-vl-text] page=6, rect=842x595, img=(2339x1654), dpi=200
2026-08-06 10:36:13,316 INFO     30 [qwen-vl-text] LLM extraction start, text_len=949
2026-08-06 10:36:13,316 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:36:13,317 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 162, \"bbox_end\": 209, \"encounter_dates\": [\"2026-03-11\"], \"department\": \"(江北)综合肿瘤中心\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "南京鼓楼医院云胶片\n南京鼓楼医院\n南京大学医学院附属鼓楼医院\n影像检查诊断报告\n互联网医院\n电子影像\n检查号:\n患者类型: 住院\n患者编号:\n姓名:\n性别: 女\n年龄: 75岁\n科别: (江北)综合肿瘤中心 病区: (江北)B7病区\n病床:\n检查日期: 2026-03-11 13:39:06\n设备类型: CT\n技师: 王雨晓\n检查项目: [CT平扫+增强(颈部、胸部、上腹部、下腹部、盆腔)]\n检查所见:\n颈部软组织CT平扫+增强:\n【所见咽部】所见咽腔结构对称,未见明显异常密度影。增强后未见明显异常强化。\n【喉部及下咽部】喉腔结构对称,会厌、声带、梨状窝形态及密度未见明显异常。增强后未见\n明显异常强化。\n【甲状腺及甲状旁腺区】甲状腺左右叶大小、形态正常,甲状腺双叶低密度结节;甲状旁腺区\n未见明显占位性病变。\n【唾液腺】双侧腮腺、颌下腺形态密度未见明显异常。增强后未见明显异常强化。\n【气管及食管】气管居中,管腔通畅;食管颈段管壁未见明显增厚。\n【颈部间隙】脂肪间隙清晰,未见明显异常密度影。增强后未见明显异常强化。\n【淋巴结】两侧锁骨上窝多发肿大淋巴结。\n【其他】副鼻窦内低密度影。\n胸部CT平扫+增强:\n【肺野】两肺野纹理清晰,左肺下叶见斑片状高密度影。右肺上叶舌段小片状高密度影。两肺\n多发结节,较大者:右肺上叶(Img79)见一实性结节影,大小约5mm×3mm。两肺索条及片絮影;右\n肺上叶局部透亮区。\n【肺门】双肺门多发肿大淋巴结,大者位于左侧,短径约20mm,增强后强化不均。\n【气管及支气管】左下肺支气管闭塞伴阻塞性炎症,病灶周围结节影。\n【纵隔】纵隔居中,纵隔内多发肿大淋巴结,较大者短径约20mm。\n【心脏及大血管】心影增大;主动脉及冠状动脉壁见致密影。\n【胸膜及胸腔】胸膜:两侧胸膜可见增厚;胸腔积液:否。增强后未见明显异常强化。\n【膈肌】光整,未见明显异常抬高。增强后未见明显异常强化。\n【胸壁】胸廓对称,骨质未见明显异常。增强后未见明显异常强化。\n上腹部、下腹部、盆腔CT平扫+增强:\n报告日期: 2026-03-11 15:35:37\n诊断医师: 申欣怡\n/ 申欣怡\n审核日期: 2026-03-12 13:17:06\n审核医师: 王国\n（本报告仅供临床医生参考）",
    "role": "user"
  }
]
2026-08-06 10:36:16,958 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:36:16.957+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 8, "lag": 0, "done": 1, "failed": 0, "current": {"00b9d592918111f18dbe1f8f96f1c395": {"id": "00b9d592918111f18dbe1f8f96f1c395", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011867426, "task_type": "dataflow", "root_trace_id": "1ab3198c92574fb4b2701d0f5db7322f", "root_traceparent": "00-1ab3198c92574fb4b2701d0f5db7322f-bdaff6f64a5f4a64-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "dfc102e2918111f18dbe1f8f96f1c395": {"id": "dfc102e2918111f18dbe1f8f96f1c395", "doc_id": "de8a02fc918111f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786012241604, "task_type": "dataflow", "root_trace_id": "90f550f6b00248c3845d57a8e0bcf6fb", "root_traceparent": "00-90f550f6b00248c3845d57a8e0bcf6fb-5db7fb7d470dfe0d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:36:31,996 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:36:31,997 INFO     30 [qwen-vl-text] LLM output (len=1030):
{
  "exam_date": "2026-03-11",
  "report_date": "2026-03-11",
  "exam_name": "CT平扫+增强(颈部、胸部、上腹部、下腹部、盆腔)",
  "exam_category": "imaging",
  "body_part": "颈部、胸部、上腹部、下腹部、盆腔",
  "patient_name": null,
  "patient_gender": "女",
  "department": "(江北)综合肿瘤中心",
  "bed_number": null,
  "findings": "颈部软组织CT平扫+增强:\n【所见咽部】所见咽腔结构对称,未见明显异常密度影。增强后未见明显异常强化。\n【喉部及下咽部】喉腔结构对称,会厌、声带、梨状窝形态及密度未见明显异常。增强后未见\n明显异常强化。\n【甲状腺及甲状旁腺区】甲状腺左右叶大小、形态正常,甲状腺双叶低密度结节;甲状旁腺区\n未见明显占位性病变。\n【唾液腺】双侧腮腺、颌下腺形态密度未见明显异常。增强后未见明显异常强化。\n【气管及食管】气管居中,管腔通畅;食管颈段管壁未见明显增厚。\n【颈部间隙】脂肪间隙清晰,未见明显异常密度影。增强后未见明显异常强化。\n【淋巴结】两侧锁骨上窝多发肿大淋巴结。\n【其他】副鼻窦内低密度影。\n胸部CT平扫+增强:\n【肺野】两肺野纹理清晰,左肺下叶见斑片状高密度影。右肺上叶舌段小片状高密度影。两肺\n多发结节,较大者:右肺上叶(Img79)见一实性结节影,大小约5mm×3mm。两肺索条及片絮影;右\n肺上叶局部透亮区。\n【肺门】双肺门多发肿大淋巴结,大者位于左侧,短径约20mm,增强后强化不均。\n【气管及支气管】左下肺支气管闭塞伴阻塞性炎症,病灶周围结节影。\n【纵隔】纵隔居中,纵隔内多发肿大淋巴结,较大者短径约20mm。\n【心脏及大血管】心影增大;主动脉及冠状动脉壁见致密影。\n【胸膜及胸腔】胸膜:两侧胸膜可见增厚;胸腔积液:否。增强后未见明显异常强化。\n【膈肌】光整,未见明显异常抬高。增强后未见明显异常强化。\n【胸壁】胸廓对称,骨质未见明显异常。增强后未见明显异常强化。\n上腹部、下腹部、盆腔CT平扫+增强:",
  "conclusion": null,
  "physician": "申欣怡",
  "reviewer": "王国"
}
2026-08-06 10:36:32,007 INFO     30 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=938136, prompt_len=1706
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共48行）
["南京鼓楼医院云胶片", "南京鼓楼医院", "南京大学医学院附属鼓楼医院", "影像检查诊断报告", "互联网医院", "电子影像", "检查号:", "患者类型: 住院", "患者编号:", "姓名:", "性别: 女", "年龄: 75岁", "科别: (江北)综合肿瘤中心 病区: (江北)B7病区", "病床:", "检查日期: 2026-03-11 13:39:06", "设备类型: CT", "技师: 王雨晓", "检查项目: [CT平扫+增强(颈部、胸部、上腹部、下腹部、盆腔)]", "检查所见:", "颈部软组织CT平扫+增强:", "【所见咽部】所见咽腔结构对称,未见明显异常密度影。增强后未见明显异常强化。", "【喉部及下咽部】喉腔结构对称,会厌、声带、梨状窝形态及密度未见明显异常。增强后未见", "明显异常强化。", "【甲状腺及甲状旁腺区】甲状腺左右叶大小、形态正常,甲状腺双叶低密度结节;甲状旁腺区", "未见明显占位性病变。", "【唾液腺】双侧腮腺、颌下腺形态密度未见明显异常。增强后未见明显异常强化。", "【气管及食管】气管居中,管腔通畅;食管颈段管壁未见明显增厚。", "【颈部间隙】脂肪间隙清晰,未见明显异常密度影。增强后未见明显异常强化。", "【淋巴结】两侧锁骨上窝多发肿大淋巴结。", "【其他】副鼻窦内低密度影。", "胸部CT平扫+增强:", "【肺野】两肺野纹理清晰,左肺下叶见斑片状高密度影。右肺上叶舌段小片状高密度影。两肺", "多发结节,较大者:右肺上叶(Img79)见一实性结节影,大小约5mm×3mm。两肺索条及片絮影;右", "肺上叶局部透亮区。", "【肺门】双肺门多发肿大淋巴结,大者位于左侧,短径约20mm,增强后强化不均。", "【气管及支气管】左下肺支气管闭塞伴阻塞性炎症,病灶周围结节影。", "【纵隔】纵隔居中,纵隔内多发肿大淋巴结,较大者短径约20mm。", "【心脏及大血管】心影增大;主动脉及冠状动脉壁见致密影。", "【胸膜及胸腔】胸膜:两侧胸膜可见增厚;胸腔积液:否。增强后未见明显异常强化。", "【膈肌】光整,未见明显异常抬高。增强后未见明显异常强化。", "【胸壁】胸廓对称,骨质未见明显异常。增强后未见明显异常强化。", "上腹部、下腹部、盆腔CT平扫+增强:", "报告日期: 2026-03-11 15:35:37", "诊断医师: 申欣怡", "/ 申欣怡", "审核日期: 2026-03-12 13:17:06", "审核医师: 王国", "（本报告仅供临床医生参考）"]

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
2026-08-06 10:36:57,385 INFO     30 [qwen-vl-text] coord API raw response (len=4474):
[
	{"text": "南京鼓楼医院云胶片", "bbox": [424, 134, 571, 158]},
	{"text": "南京鼓楼医院", "bbox": [460, 224, 550, 240], "bbox": [460, 224, 550, 240]},
	{"text": "南京大学医学院附属鼓楼医院", "bbox": [435, 240, 571, 255], "bbox": [435, 240, 571, 255]},
	{"text": "影像检查诊断报告", "bbox": [445, 255, 562, 275], "bbox": [445, 255, 562, 275]},
	{"text": "互联网医院", "bbox": [333, 300, 366, 309], "bbox": [333, 300, 366, 309]},
	{"text": "电子影像", "bbox": [622, 300, 650, 309], "bbox": [622, 300, 650, 309]},
	{"text": "检查号:", "bbox": [317, 327, 353, 340], "bbox": [317, 327, 353, 340]},
	{"text": "患者类型: 住院", "bbox": [445, 327, 504, 340], "bbox": [445, 327, 504, 340]},
	{"text": "患者编号:", "bbox": [548, 327, 583, 340], "bbox": [548, 327, 583, 340]},
	{"text": "姓名:", "bbox": [317, 349, 353, 362], "bbox": [317, 349, 353, 362]},
	{"text": "性别: 女", "bbox": [445, 349, 496, 362], "bbox": [445, 349, 496, 362]},
	{"text": "年龄: 75岁", "bbox": [548, 349, 609, 362], "bbox": [548, 349, 609, 362]},
	{"text": "科别: (江北)综合肿瘤中心 病区: (江北)B7病区", "bbox": [317, 368, 535, 381], "bbox": [317, 368, 535, 381]},
	{"text": "病床:", "bbox": [548, 368, 583, 381], "bbox": [548, 368, 583, 381]},
	{"text": "检查日期: 2026-03-11 13:39:06", "bbox": [317, 387, 437, 400], "bbox": [317, 387, 437, 400]},
	{"text": "设备类型: CT", "bbox": [317, 406, 369, 419], "bbox": [317, 406, 369, 419]},
	{"text": "技师: 王雨晓", "bbox": [548, 406, 614, 419], "bbox": [548, 406, 614, 419]},
	{"text": "检查项目: [CT平扫+增强(颈部、胸部、上腹部、下腹部、盆腔)]", "bbox": [317, 425, 555, 438], "bbox": [317, 425, 555, 438]},
	{"text": "检查所见:", "bbox": [317, 443, 353, 456], "bbox": [317, 443, 353, 456]},
	{"text": "颈部软组织CT平扫+增强:", "bbox": [317, 460, 405, 473], "bbox": [317, 460, 405, 473]},
	{"text": "【所见咽部】所见咽腔结构对称,未见明显异常密度影。增强后未见明显异常强化。", "bbox": [337, 477, 623, 489], "bbox": [337, 477, 623, 489]},
	{"text": "【喉部及下咽部】喉腔结构对称,会厌、声带、梨状窝形态及密度未见明显异常。增强后未见", "bbox": [337, 494, 660, 506], "bbox": [337, 494, 660, 506]},
	{"text": "明显异常强化。", "bbox": [317, 511, 370, 523], "bbox": [317, 511, 370, 523]},
	{"text": "【甲状腺及甲状旁腺区】甲状腺左右叶大小、形态正常,甲状腺双叶低密度结节;甲状旁腺区", "bbox": [337, 528, 660, 540], "bbox": [337, 528, 660, 540]},
	{"text": "未见明显占位性病变。", "bbox": [317, 545, 394, 557], "bbox": [317, 545, 394, 557]},
	{"text": "【唾液腺】双侧腮腺、颌下腺形态密度未见明显异常。增强后未见明显异常强化。", "bbox": [337, 562, 616, 574], "bbox": [337, 562, 616, 574]},
	{"text": "【气管及食管】气管居中,管腔通畅;食管颈段管壁未见明显增厚。", "bbox": [337, 579, 567, 591], "bbox": [337, 579, 567, 591]},
	{"text": "【颈部间隙】脂肪间隙清晰,未见明显异常密度影。增强后未见明显异常强化。", "bbox": [337, 596, 607, 608], "bbox": [337, 596, 607, 608]},
	{"text": "【淋巴结】两侧锁骨上窝多发肿大淋巴结。", "bbox": [337, 613, 480, 625], "bbox": [337, 613, 480, 625]},
	{"text": "【其他】副鼻窦内低密度影。", "bbox": [337, 630, 433, 642], "bbox": [337, 630, 433, 642]},
	{"text": "胸部CT平扫+增强:", "bbox": [317, 647, 380, 659], "bbox": [317, 647, 380, 659]},
	{"text": "【肺野】两肺野纹理清晰,左肺下叶见斑片状高密度影。右肺上叶舌段小片状高密度影。两肺", "bbox": [337, 664, 660, 676], "bbox": [337, 664, 660, 676]},
	{"text": "多发结节,较大者:右肺上叶(Img79)见一实性结节影,大小约5mm×3mm。两肺索条及片絮影;右", "bbox": [317, 681, 664, 693], "bbox": [317, 681, 664, 693]},
	{"text": "肺上叶局部透亮区。", "bbox": [317, 698, 386, 710], "bbox": [317, 698, 386, 710]},
	{"text": "【肺门】双肺门多发肿大淋巴结,大者位于左侧,短径约20mm,增强后强化不均。", "bbox": [337, 715, 616, 727], "bbox": [337, 715, 616, 727]},
	{"text": "【气管及支气管】左下肺支气管闭塞伴阻塞性炎症,病灶周围结节影。", "bbox": [337, 732, 576, 744], "bbox": [337, 732, 576, 744]},
	{"text": "【纵隔】纵隔居中,纵隔内多发肿大淋巴结,较大者短径约20mm。", "bbox": [337, 749, 560, 761], "bbox": [337, 749, 560, 761]},
	{"text": "【心脏及大血管】心影增大;主动脉及冠状动脉壁见致密影。", "bbox": [337, 766, 549, 778], "bbox": [337, 766, 549, 778]},
	{"text": "【胸膜及胸腔】胸膜:两侧胸膜可见增厚;胸腔积液:否。增强后未见明显异常强化。", "bbox": [337, 783, 632, 795], "bbox": [337, 783, 632, 795]},
	{"text": "【膈肌】光整,未见明显异常抬高。增强后未见明显异常强化。", "bbox": [337, 800, 553, 812], "bbox": [337, 800, 553, 812]},
	{"text": "【胸壁】胸廓对称,骨质未见明显异常。增强后未见明显异常强化。", "bbox": [337, 817, 568, 829], "bbox": [337, 817, 568, 829]},
	{"text": "上腹部、下腹部、盆腔CT平扫+增强:", "bbox": [317, 834, 444, 846], "bbox": [317, 834, 444, 846]},
	{"text": "报告日期: 2026-03-11 15:35:37", "bbox": [317, 858, 437, 871], "bbox": [317, 858, 437, 871]},
	{"text": "诊断医师: 申欣怡", "bbox": [464, 858, 534, 871], "bbox": [464, 858, 534, 871]},
	{"text": "/ 申欣怡", "bbox": [581, 858, 617, 871], "bbox": [581, 858, 617, 871]},
	{"text": "审核日期: 2026-03-12 13:17:06", "bbox": [317, 890, 437, 903], "bbox": [317, 890, 437, 903]},
	{"text": "审核医师: 王国", "bbox": [464, 888, 537, 906], "bbox": [464, 888, 537, 906]},
	{"text": "（本报告仅供临床医生参考）", "bbox": [377, 913, 449, 922], "bbox": [377, 913, 449, 922]}
]
2026-08-06 10:36:57,386 INFO     30 [qwen-vl-text] coord API: raw_items=48, valid_items=48, elapsed=25.4s
2026-08-06 10:36:57,387 INFO     30 [qwen-vl-text] coord item[0]: text=南京鼓楼医院云胶片, bbox=[424, 134, 571, 158]
2026-08-06 10:36:57,387 INFO     30 [qwen-vl-text] coord item[1]: text=南京鼓楼医院, bbox=[460, 224, 550, 240]
2026-08-06 10:36:57,387 INFO     30 [qwen-vl-text] coord item[2]: text=南京大学医学院附属鼓楼医院, bbox=[435, 240, 571, 255]
2026-08-06 10:36:57,387 INFO     30 [qwen-vl-text] coord item[3]: text=影像检查诊断报告, bbox=[445, 255, 562, 275]
2026-08-06 10:36:57,388 INFO     30 [qwen-vl-text] coord item[4]: text=互联网医院, bbox=[333, 300, 366, 309]
2026-08-06 10:36:57,388 INFO     30 [qwen-vl-text] coord item[5]: text=电子影像, bbox=[622, 300, 650, 309]
2026-08-06 10:36:57,388 INFO     30 [qwen-vl-text] coord item[6]: text=检查号:, bbox=[317, 327, 353, 340]
2026-08-06 10:36:57,388 INFO     30 [qwen-vl-text] coord item[7]: text=患者类型: 住院, bbox=[445, 327, 504, 340]
2026-08-06 10:36:57,388 INFO     30 [qwen-vl-text] coord item[8]: text=患者编号:, bbox=[548, 327, 583, 340]
2026-08-06 10:36:57,388 INFO     30 [qwen-vl-text] coord item[9]: text=姓名:, bbox=[317, 349, 353, 362]
2026-08-06 10:36:57,388 INFO     30 [qwen-vl-text] coord item[10]: text=性别: 女, bbox=[445, 349, 496, 362]
2026-08-06 10:36:57,389 INFO     30 [qwen-vl-text] coord item[11]: text=年龄: 75岁, bbox=[548, 349, 609, 362]
2026-08-06 10:36:57,389 INFO     30 [qwen-vl-text] coord item[12]: text=科别: (江北)综合肿瘤中心 病区: (江北)B7病区, bbox=[317, 368, 535, 381]
2026-08-06 10:36:57,389 INFO     30 [qwen-vl-text] coord item[13]: text=病床:, bbox=[548, 368, 583, 381]
2026-08-06 10:36:57,389 INFO     30 [qwen-vl-text] coord item[14]: text=检查日期: 2026-03-11 13:39:06, bbox=[317, 387, 437, 400]
2026-08-06 10:36:57,389 INFO     30 [qwen-vl-text] coord item[15]: text=设备类型: CT, bbox=[317, 406, 369, 419]
2026-08-06 10:36:57,390 INFO     30 [qwen-vl-text] coord item[16]: text=技师: 王雨晓, bbox=[548, 406, 614, 419]
2026-08-06 10:36:57,390 INFO     30 [qwen-vl-text] coord item[17]: text=检查项目: [CT平扫+增强(颈部、胸部、上腹部、下腹部、盆腔)], bbox=[317, 425, 555, 438]
2026-08-06 10:36:57,390 INFO     30 [qwen-vl-text] coord item[18]: text=检查所见:, bbox=[317, 443, 353, 456]
2026-08-06 10:36:57,390 INFO     30 [qwen-vl-text] coord item[19]: text=颈部软组织CT平扫+增强:, bbox=[317, 460, 405, 473]
2026-08-06 10:36:57,390 INFO     30 [qwen-vl-text] coord item[20]: text=【所见咽部】所见咽腔结构对称,未见明显异常密度影。增强后未见明显异常强化。, bbox=[337, 477, 623, 489]
2026-08-06 10:36:57,391 INFO     30 [qwen-vl-text] coord item[21]: text=【喉部及下咽部】喉腔结构对称,会厌、声带、梨状窝形态及密度未见明显异常。增强后未见, bbox=[337, 494, 660, 506]
2026-08-06 10:36:57,391 INFO     30 [qwen-vl-text] coord item[22]: text=明显异常强化。, bbox=[317, 511, 370, 523]
2026-08-06 10:36:57,391 INFO     30 [qwen-vl-text] coord item[23]: text=【甲状腺及甲状旁腺区】甲状腺左右叶大小、形态正常,甲状腺双叶低密度结节;甲状旁腺区, bbox=[337, 528, 660, 540]
2026-08-06 10:36:57,391 INFO     30 [qwen-vl-text] coord item[24]: text=未见明显占位性病变。, bbox=[317, 545, 394, 557]
2026-08-06 10:36:57,391 INFO     30 [qwen-vl-text] coord item[25]: text=【唾液腺】双侧腮腺、颌下腺形态密度未见明显异常。增强后未见明显异常强化。, bbox=[337, 562, 616, 574]
2026-08-06 10:36:57,391 INFO     30 [qwen-vl-text] coord item[26]: text=【气管及食管】气管居中,管腔通畅;食管颈段管壁未见明显增厚。, bbox=[337, 579, 567, 591]
2026-08-06 10:36:57,392 INFO     30 [qwen-vl-text] coord item[27]: text=【颈部间隙】脂肪间隙清晰,未见明显异常密度影。增强后未见明显异常强化。, bbox=[337, 596, 607, 608]
2026-08-06 10:36:57,392 INFO     30 [qwen-vl-text] coord item[28]: text=【淋巴结】两侧锁骨上窝多发肿大淋巴结。, bbox=[337, 613, 480, 625]
2026-08-06 10:36:57,392 INFO     30 [qwen-vl-text] coord item[29]: text=【其他】副鼻窦内低密度影。, bbox=[337, 630, 433, 642]
2026-08-06 10:36:57,392 INFO     30 [qwen-vl-text] coord item[30]: text=胸部CT平扫+增强:, bbox=[317, 647, 380, 659]
2026-08-06 10:36:57,392 INFO     30 [qwen-vl-text] coord item[31]: text=【肺野】两肺野纹理清晰,左肺下叶见斑片状高密度影。右肺上叶舌段小片状高密度影。两肺, bbox=[337, 664, 660, 676]
2026-08-06 10:36:57,392 INFO     30 [qwen-vl-text] coord item[32]: text=多发结节,较大者:右肺上叶(Img79)见一实性结节影,大小约5mm×3mm。两肺索条及片絮影;右, bbox=[317, 681, 664, 693]
2026-08-06 10:36:57,393 INFO     30 [qwen-vl-text] coord item[33]: text=肺上叶局部透亮区。, bbox=[317, 698, 386, 710]
2026-08-06 10:36:57,393 INFO     30 [qwen-vl-text] coord item[34]: text=【肺门】双肺门多发肿大淋巴结,大者位于左侧,短径约20mm,增强后强化不均。, bbox=[337, 715, 616, 727]
2026-08-06 10:36:57,393 INFO     30 [qwen-vl-text] coord item[35]: text=【气管及支气管】左下肺支气管闭塞伴阻塞性炎症,病灶周围结节影。, bbox=[337, 732, 576, 744]
2026-08-06 10:36:57,393 INFO     30 [qwen-vl-text] coord item[36]: text=【纵隔】纵隔居中,纵隔内多发肿大淋巴结,较大者短径约20mm。, bbox=[337, 749, 560, 761]
2026-08-06 10:36:57,393 INFO     30 [qwen-vl-text] coord item[37]: text=【心脏及大血管】心影增大;主动脉及冠状动脉壁见致密影。, bbox=[337, 766, 549, 778]
2026-08-06 10:36:57,393 INFO     30 [qwen-vl-text] coord item[38]: text=【胸膜及胸腔】胸膜:两侧胸膜可见增厚;胸腔积液:否。增强后未见明显异常强化。, bbox=[337, 783, 632, 795]
2026-08-06 10:36:57,393 INFO     30 [qwen-vl-text] coord item[39]: text=【膈肌】光整,未见明显异常抬高。增强后未见明显异常强化。, bbox=[337, 800, 553, 812]
2026-08-06 10:36:57,393 INFO     30 [qwen-vl-text] coord item[40]: text=【胸壁】胸廓对称,骨质未见明显异常。增强后未见明显异常强化。, bbox=[337, 817, 568, 829]
2026-08-06 10:36:57,393 INFO     30 [qwen-vl-text] coord item[41]: text=上腹部、下腹部、盆腔CT平扫+增强:, bbox=[317, 834, 444, 846]
2026-08-06 10:36:57,393 INFO     30 [qwen-vl-text] coord item[42]: text=报告日期: 2026-03-11 15:35:37, bbox=[317, 858, 437, 871]
2026-08-06 10:36:57,393 INFO     30 [qwen-vl-text] coord item[43]: text=诊断医师: 申欣怡, bbox=[464, 858, 534, 871]
2026-08-06 10:36:57,394 INFO     30 [qwen-vl-text] coord item[44]: text=/ 申欣怡, bbox=[581, 858, 617, 871]
2026-08-06 10:36:57,394 INFO     30 [qwen-vl-text] coord item[45]: text=审核日期: 2026-03-12 13:17:06, bbox=[317, 890, 437, 903]
2026-08-06 10:36:57,394 INFO     30 [qwen-vl-text] coord item[46]: text=审核医师: 王国, bbox=[464, 888, 537, 906]
2026-08-06 10:36:57,394 INFO     30 [qwen-vl-text] coord item[47]: text=（本报告仅供临床医生参考）, bbox=[377, 913, 449, 922]
2026-08-06 10:36:57,395 INFO     30 [qwen-vl-text] page=6 — 48/48 coords, api_time=25.4s
2026-08-06 10:36:57,395 INFO     30 [qwen-vl-text] new_positions (48):
[[6, 356.9613662109375, 480.7191983642578, 79.76698413085938, 94.05360815429688], [6, 387.26940673828125, 463.0395080566406, 133.34182421875, 142.866240234375], [6, 366.2221563720703, 480.7191983642578, 142.866240234375, 151.79538024902345], [6, 374.6410565185547, 473.14218823242186, 151.79538024902345, 163.7009002685547], [6, 280.3493748779297, 308.1317453613281, 178.58280029296876, 183.94028430175783], [6, 523.6555891113281, 547.2285095214844, 178.58280029296876, 183.94028430175783], [6, 266.87913464355466, 297.18717517089846, 194.65525231933594, 202.39384033203126], [6, 374.6410565185547, 424.3125673828125, 194.65525231933594, 202.39384033203126], [6, 461.35572802734373, 490.82187854003905, 194.65525231933594, 202.39384033203126], [6, 266.87913464355466, 297.18717517089846, 207.75132434082033, 215.48991235351562], [6, 374.6410565185547, 417.577447265625, 207.75132434082033, 215.48991235351562], [6, 461.35572802734373, 512.7110189208985, 207.75132434082033, 215.48991235351562], [6, 266.87913464355466, 450.4111578369141, 219.061568359375, 226.80015637207032], [6, 461.35572802734373, 490.82187854003905, 219.061568359375, 226.80015637207032], [6, 266.87913464355466, 367.90593640136717, 230.3718123779297, 238.11040039062502], [6, 266.87913464355466, 310.6574154052734, 241.6820563964844, 249.4206444091797], [6, 461.35572802734373, 516.9204689941406, 241.6820563964844, 249.4206444091797], [6, 266.87913464355466, 467.2489581298828, 252.99230041503907, 260.7308884277344], [6, 266.87913464355466, 297.18717517089846, 263.7072684326172, 271.44585644531253], [6, 266.87913464355466, 340.9654559326172, 273.82696044921875, 281.5655484619141], [6, 283.71693493652344, 524.4974791259766, 283.9466524658203, 291.08996447753907], [6, 283.71693493652344, 555.6474096679688, 294.06634448242187, 301.20965649414063], [6, 266.87913464355466, 311.4993054199219, 304.18603649902343, 311.3293485107422], [6, 283.71693493652344, 555.6474096679688, 314.305728515625, 321.44904052734375], [6, 266.87913464355466, 331.7046657714844, 324.42542053222655, 331.5687325439453], [6, 283.71693493652344, 518.6042490234375, 334.5451125488281, 341.6884245605469], [6, 283.71693493652344, 477.35163830566404, 344.6648045654297, 351.80811657714844], [6, 283.71693493652344, 511.02723889160154, 354.78449658203124, 361.92780859375], [6, 283.71693493652344, 404.10720703124997, 364.9041885986328, 372.04750061035156], [6, 283.71693493652344, 364.53837634277346, 375.0238806152344, 382.1671926269531], [6, 266.87913464355466, 319.91820556640624, 385.143572631836, 392.2868846435547], [6, 283.71693493652344, 555.6474096679688, 395.26326464843754, 402.40657666015625], [6, 266.87913464355466, 559.0149697265625, 405.3829566650391, 412.5262686767578], [6, 266.87913464355466, 324.9695456542969, 415.50264868164066, 422.64596069335937], [6, 283.71693493652344, 518.6042490234375, 425.6223406982422, 432.76565270996093], [6, 283.71693493652344, 484.9286484375, 435.7420327148438, 442.8853447265625], [6, 283.71693493652344, 471.458408203125, 445.86172473144535, 453.00503674316406], [6, 283.71693493652344, 462.1976180419922, 455.9814167480469, 463.1247287597656], [6, 283.71693493652344, 532.0744892578125, 466.1011087646485, 473.24442077636724], [6, 283.71693493652344, 465.5651781005859, 476.22080078125003, 483.3641127929688], [6, 283.71693493652344, 478.1935283203125, 486.3404927978516, 493.48380480957036], [6, 266.87913464355466, 373.79916650390624, 496.46018481445316, 503.6034968261719], [6, 266.87913464355466, 367.90593640136717, 510.7468088378906, 518.485396850586], [6, 390.636966796875, 449.5692678222656, 510.7468088378906, 518.485396850586], [6, 489.13809851074217, 519.4461390380859, 510.7468088378906, 518.485396850586], [6, 266.87913464355466, 367.90593640136717, 529.7956408691407, 537.5342288818359], [6, 390.636966796875, 452.09493786621096, 528.6050888671875, 539.3200568847657], [6, 317.39253552246095, 378.0086165771484, 543.4869888916016, 548.8444729003907]]
2026-08-06 10:36:57,396 INFO     30 [qwen-vl-text] ═══ DONE ═══ 48 positions, pages=1, time=44.3s
2026-08-06 10:36:57,397 INFO     30 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 10:36:57,398 INFO     30 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-06 10:36:57,398 INFO     30 [qwen-vl-text] positions(122): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 10:36:57,399 INFO     30 [qwen-vl-text] page grouping: [7, 8, 9, 10], lines per page: [29, 31, 32, 30]
2026-08-06 10:36:57,815 INFO     30 [qwen-vl-text] page=7, rect=842x595, img=(2339x1654), dpi=200
2026-08-06 10:36:58,075 INFO     30 [qwen-vl-text] page=8, rect=842x595, img=(2339x1654), dpi=200
2026-08-06 10:36:58,362 INFO     30 [qwen-vl-text] page=9, rect=842x595, img=(2339x1654), dpi=200
2026-08-06 10:36:58,598 INFO     30 [qwen-vl-text] page=10, rect=842x595, img=(2339x1654), dpi=200
2026-08-06 10:36:58,600 INFO     30 [qwen-vl-text] LLM extraction start, text_len=2015
2026-08-06 10:36:58,600 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:36:58,600 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 211, \"bbox_end\": 332, \"encounter_dates\": [\"2025-10-08\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "南京鼓楼医院云胶片\n女/75岁\n设备类型 CT 患者类型 无\n检查项目 [CT平扫+增强（颈部、胸部、上腹部、下\n腹部、盆腔）]\nPDF报告 图像 分享\n报告 2025-10-08\n影像描述\n颈部软组织CT平扫+增强：\n【所见咽部】所见咽腔结构对称，未见明显异常\n密度影。增强后未见明显异常强化。\n【喉部及下咽部】喉腔结构对称，会厌、声带、\n梨状窝形态及密度未见明显异常。增强后未见明显\n异常强化。\n【甲状腺及甲状旁腺区】甲状腺左右叶大小、形\n态正常，甲状腺双叶低密度结节；甲状旁腺区未见\n明显占位性病变。\n【唾液腺】双侧腮腺、颌下腺形态密度未见明显\n异常。增强后未见明显异常强化。\n【气管及食管】气管居中，管腔通畅；食管颈段\n管壁未见明显增厚。\n【颈部间隙】脂肪间隙清晰，未见明显异常密度\n影。增强后未见明显异常强化。\n【淋巴结】未见明显肿大淋巴结。\n【其他】副鼻窦内低密度影。\n胸部CT平扫+增强：\n【肺野】两肺野纹理清晰，左肺下叶见斑片状高\n移动影像浏览\n© 2022 南京鼓楼医院影像云平台 V1.0\n南京鼓楼医院云胶片\n女/75岁\n设备类型 CT 患者类型 无\n检查项目 [CT平扫+增强（颈部、胸部、上腹部、下\n腹部、盆腔）]\nPDF报告 图像 分享\n【肺野】两肺野纹理清晰，左肺下叶见斑片状高\n密度影。两肺多发结节，较大者：右肺上叶（Img7\n9）见一实性结节影，大小约5mm×3mm。两肺索\n条及片絮影；右肺上叶局部透亮区。\n【肺门】双肺门多发小淋巴结，部分稍大。\n【气管及支气管】左下肺支气管闭塞伴阻塞性炎\n症，病灶周围结节影。\n【纵隔】纵隔居中，纵隔内多发小淋巴结，部分\n稍大，较大者短径约10mm。\n【心脏及大血管】心影增大；主动脉及冠状动\n脉壁见致密影。\n【胸膜及胸腔】胸膜：两侧胸膜可见增厚；胸腔\n积液：否。增强后未见明显异常强化。\n【膈肌】光整，未见明显异常抬高。增强后未见\n明显异常强化。\n【胸壁】胸廓对称，骨质未见明显异常。增强后\n未见明显异常强化。\n上腹部CT平扫+增强：\n【肝脏】各叶比例在正常范围内，外形轮廓规\n则，肝内小圆形无强化低密度影，较大者长径约6\nmm。静脉期肝左叶小片状稍低密度影（薄层im29\n0）。\n【胆囊及胆管】胆囊形态、大小正常，囊壁未见\n移动影像浏览\n© 2022 南京鼓楼医院影像云平台 V1.0\n南京鼓楼医院云胶片\n女/75岁\n设备类型 CT 患者类型 无\n检查项目 [CT平扫+增强（颈部、胸部、上腹部、下\n腹部、盆腔）]\nPDF报告 图像 分享\n【胆囊及胆管】胆囊形态、大小正常，囊壁未见\n增厚，囊内未见明显异常密度影；肝内外胆管轻度\n扩张。\n【胰腺】形态、大小正常，实质内未见明显异常\n密度影；胰管未见明显扩张。增强后未见明显异常\n强化。\n【脾脏】形态、大小正常，实质内未见明显异常\n密度影。增强后未见明显异常强化。\n【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均\n匀，未见明显肿大淋巴结，未见明显渗出及积液。\n增强后未见明显异常强化。\n下腹部CT平扫+增强：\n【肾脏】两侧肾脏大小、形态、位置正常，右肾\n窦点状致密影；肾盂肾盏未见明显扩张。增强后未\n见明显异常强化。\n【肾上腺】双肾上腺增粗，左肾上腺低密度结\n节，长径约12mm,可见强化。\n【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均\n匀，未见明显肿大淋巴结，未见明显渗出及积液。\n增强后未见明显异常强化。\n盆腔CT平扫+增强：\n【膀胱】充盈欠佳，壁未见明显增厚，其内未见\n明显异常密度影。增强后未见明显异常强化。\n【子宫及附件】子宫呈肌组织结构性空扫\n移动影像浏览\n© 2022 南京鼓楼医院影像云平台 V1.0\n南京鼓楼医院云胶片\n女/75岁\n设备类型 CT 患者类型 无\n检查项目 [CT平扫+增强（颈部、胸部、上腹部、下\n腹部、盆腔）]\nPDF报告 图像 分享\n诊断意见\n1.肺癌复查：左肺下叶斑片影较前（2025-07-15）\n明显缩小，左下肺支气管闭塞伴阻塞性炎症，较前\n缓解，密切随诊；双侧纵隔内及双肺门多发稍大淋\n巴结，部分较前稍缩小。\n2.两肺多发结节，较前变化不大，密切随诊。\n3.两侧胸膜增厚；两肺索条及炎性渗出，较前缓\n解；右肺上叶局限性肺气肿。\n4.心影增大；主动脉及冠状动脉壁钙化。\n5.肝脏小囊肿；静脉期肝左叶小片状稍低密度影\n（薄层im290），较前相仿，随诊。\n6.肝内外胆管轻度扩张。\n7.双肾上腺增粗，左肾上腺腺瘤可能，结合专科检\n查；右肾小结石。\n8.子宫肌瘤可能，结合妇科超声；盆腔内钙化结\n节。\n9.下腹腔内肠系膜间隙多发稍大淋巴结。\n10.食管下段壁轻度增厚；乙状结肠迂曲冗长；结肠\n内容物多；十二指肠降部憩室；结合临床体征随\n诊。\n11.右肩部皮下低密度结节，较前相仿，随诊；L4及\n以上椎体I°滑脱。\n移动影像浏览\n© 2022 南京鼓楼医院影像云平台 V1.0",
    "role": "user"
  }
]
2026-08-06 10:36:58,605 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:36:58.603+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 8, "lag": 0, "done": 1, "failed": 0, "current": {"00b9d592918111f18dbe1f8f96f1c395": {"id": "00b9d592918111f18dbe1f8f96f1c395", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011867426, "task_type": "dataflow", "root_trace_id": "1ab3198c92574fb4b2701d0f5db7322f", "root_traceparent": "00-1ab3198c92574fb4b2701d0f5db7322f-bdaff6f64a5f4a64-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "dfc102e2918111f18dbe1f8f96f1c395": {"id": "dfc102e2918111f18dbe1f8f96f1c395", "doc_id": "de8a02fc918111f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786012241604, "task_type": "dataflow", "root_trace_id": "90f550f6b00248c3845d57a8e0bcf6fb", "root_traceparent": "00-90f550f6b00248c3845d57a8e0bcf6fb-5db7fb7d470dfe0d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:37:27,635 INFO     30 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:37:27,635 INFO     30 [qwen-vl-text] LLM output (len=1862):
{
  "exam_date": "2025-10-08",
  "report_date": "2025-10-08",
  "exam_name": "CT平扫+增强（颈部、胸部、上腹部、下腹部、盆腔）",
  "exam_category": "imaging",
  "body_part": "颈部、胸部、上腹部、下腹部、盆腔",
  "patient_name": null,
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": "颈部软组织CT平扫+增强：\n【所见咽部】所见咽腔结构对称，未见明显异常密度影。增强后未见明显异常强化。\n【喉部及下咽部】喉腔结构对称，会厌、声带、梨状窝形态及密度未见明显异常。增强后未见明显异常强化。\n【甲状腺及甲状旁腺区】甲状腺左右叶大小、形态正常，甲状腺双叶低密度结节；甲状旁腺区未见明显占位性病变。\n【唾液腺】双侧腮腺、颌下腺形态密度未见明显异常。增强后未见明显异常强化。\n【气管及食管】气管居中，管腔通畅；食管颈段管壁未见明显增厚。\n【颈部间隙】脂肪间隙清晰，未见明显异常密度影。增强后未见明显异常强化。\n【淋巴结】未见明显肿大淋巴结。\n【其他】副鼻窦内低密度影。\n\n胸部CT平扫+增强：\n【肺野】两肺野纹理清晰，左肺下叶见斑片状高密度影。两肺多发结节，较大者：右肺上叶（Img79）见一实性结节影，大小约5mm×3mm。两肺索条及片絮影；右肺上叶局部透亮区。\n【肺门】双肺门多发小淋巴结，部分稍大。\n【气管及支气管】左下肺支气管闭塞伴阻塞性炎症，病灶周围结节影。\n【纵隔】纵隔居中，纵隔内多发小淋巴结，部分稍大，较大者短径约10mm。\n【心脏及大血管】心影增大；主动脉及冠状动脉壁见致密影。\n【胸膜及胸腔】胸膜：两侧胸膜可见增厚；胸腔积液：否。增强后未见明显异常强化。\n【膈肌】光整，未见明显异常抬高。增强后未见明显异常强化。\n【胸壁】胸廓对称，骨质未见明显异常。增强后未见明显异常强化。\n\n上腹部CT平扫+增强：\n【肝脏】各叶比例在正常范围内，外形轮廓规则，肝内小圆形无强化低密度影，较大者长径约6mm。静脉期肝左叶小片状稍低密度影（薄层im290）。\n【胆囊及胆管】胆囊形态、大小正常，囊壁未见增厚，囊内未见明显异常密度影；肝内外胆管轻度扩张。\n【胰腺】形态、大小正常，实质内未见明显异常密度影；胰管未见明显扩张。增强后未见明显异常强化。\n【脾脏】形态、大小正常，实质内未见明显异常密度影。增强后未见明显异常强化。\n【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均匀，未见明显肿大淋巴结，未见明显渗出及积液。增强后未见明显异常强化。\n\n下腹部CT平扫+增强：\n【肾脏】两侧肾脏大小、形态、位置正常，右肾窦点状致密影；肾盂肾盏未见明显扩张。增强后未见明显异常强化。\n【肾上腺】双肾上腺增粗，左肾上腺低密度结节，长径约12mm,可见强化。\n【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均匀，未见明显肿大淋巴结，未见明显渗出及积液。增强后未见明显异常强化。\n\n盆腔CT平扫+增强：\n【膀胱】充盈欠佳，壁未见明显增厚，其内未见明显异常密度影。增强后未见明显异常强化。\n【子宫及附件】子宫呈肌组织结构性空扫",
  "conclusion": "1.肺癌复查：左肺下叶斑片影较前（2025-07-15）明显缩小，左下肺支气管闭塞伴阻塞性炎症，较前缓解，密切随诊；双侧纵隔内及双肺门多发稍大淋巴结，部分较前稍缩小。\n2.两肺多发结节，较前变化不大，密切随诊。\n3.两侧胸膜增厚；两肺索条及炎性渗出，较前缓解；右肺上叶局限性肺气肿。\n4.心影增大；主动脉及冠状动脉壁钙化。\n5.肝脏小囊肿；静脉期肝左叶小片状稍低密度影（薄层im290），较前相仿，随诊。\n6.肝内外胆管轻度扩张。\n7.双肾上腺增粗，左肾上腺腺瘤可能，结合专科检查；右肾小结石。\n8.子宫肌瘤可能，结合妇科超声；盆腔内钙化结节。\n9.下腹腔内肠系膜间隙多发稍大淋巴结。\n10.食管下段壁轻度增厚；乙状结肠迂曲冗长；结肠内容物多；十二指肠降部憩室；结合临床体征随诊。\n11.右肩部皮下低密度结节，较前相仿，随诊；L4及以上椎体I°滑脱。",
  "physician": null,
  "reviewer": null
}
2026-08-06 10:37:27,639 INFO     30 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=553741, prompt_len=1154
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共29行）
["南京鼓楼医院云胶片", "女/75岁", "设备类型 CT 患者类型 无", "检查项目 [CT平扫+增强（颈部、胸部、上腹部、下", "腹部、盆腔）]", "PDF报告 图像 分享", "报告 2025-10-08", "影像描述", "颈部软组织CT平扫+增强：", "【所见咽部】所见咽腔结构对称，未见明显异常", "密度影。增强后未见明显异常强化。", "【喉部及下咽部】喉腔结构对称，会厌、声带、", "梨状窝形态及密度未见明显异常。增强后未见明显", "异常强化。", "【甲状腺及甲状旁腺区】甲状腺左右叶大小、形", "态正常，甲状腺双叶低密度结节；甲状旁腺区未见", "明显占位性病变。", "【唾液腺】双侧腮腺、颌下腺形态密度未见明显", "异常。增强后未见明显异常强化。", "【气管及食管】气管居中，管腔通畅；食管颈段", "管壁未见明显增厚。", "【颈部间隙】脂肪间隙清晰，未见明显异常密度", "影。增强后未见明显异常强化。", "【淋巴结】未见明显肿大淋巴结。", "【其他】副鼻窦内低密度影。", "胸部CT平扫+增强：", "【肺野】两肺野纹理清晰，左肺下叶见斑片状高", "移动影像浏览", "© 2022 南京鼓楼医院影像云平台 V1.0"]

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
2026-08-06 10:37:37,870 INFO     30 [qwen-vl-text] coord API raw response (len=1733):
[
	{"text": "南京鼓楼医院云胶片", "bbox": [444, 118, 552, 137]},
	{"text": "女/75岁", "bbox": [588, 163, 629, 178]},
	{"text": "设备类型 CT 患者类型 无", "bbox": [387, 205, 594, 223]},
	{"text": "检查项目 [CT平扫+增强（颈部、胸部、上腹部、下", "bbox": [387, 250, 618, 267]},
	{"text": "腹部、盆腔）]", "bbox": [438, 267, 502, 282]},
	{"text": "PDF报告 图像 分享", "bbox": [396, 315, 588, 337]},
	{"text": "报告 2025-10-08", "bbox": [387, 367, 609, 387]},
	{"text": "影像描述", "bbox": [387, 411, 431, 427]},
	{"text": "颈部软组织CT平扫+增强：", "bbox": [387, 451, 500, 467]},
	{"text": "【所见咽部】所见咽腔结构对称，未见明显异常", "bbox": [405, 472, 608, 488]},
	{"text": "密度影。增强后未见明显异常强化。", "bbox": [387, 493, 540, 508]},
	{"text": "【喉部及下咽部】喉腔结构对称，会厌、声带、", "bbox": [405, 513, 602, 529]},
	{"text": "梨状窝形态及密度未见明显异常。增强后未见明显", "bbox": [387, 534, 608, 550]},
	{"text": "异常强化。", "bbox": [387, 555, 435, 570]},
	{"text": "【甲状腺及甲状旁腺区】甲状腺左右叶大小、形", "bbox": [405, 576, 608, 591]},
	{"text": "态正常，甲状腺双叶低密度结节；甲状旁腺区未见", "bbox": [387, 596, 608, 612]},
	{"text": "明显占位性病变。", "bbox": [387, 617, 464, 633]},
	{"text": "【唾液腺】双侧腮腺、颌下腺形态密度未见明显", "bbox": [405, 638, 608, 654]},
	{"text": "异常。增强后未见明显异常强化。", "bbox": [387, 659, 531, 674]},
	{"text": "【气管及食管】气管居中，管腔通畅；食管颈段", "bbox": [405, 680, 608, 695]},
	{"text": "管壁未见明显增厚。", "bbox": [387, 701, 473, 717]},
	{"text": "【颈部间隙】脂肪间隙清晰，未见明显异常密度", "bbox": [405, 722, 608, 737]},
	{"text": "影。增强后未见明显异常强化。", "bbox": [387, 742, 521, 758]},
	{"text": "【淋巴结】未见明显肿大淋巴结。", "bbox": [405, 763, 543, 779]},
	{"text": "【其他】副鼻窦内低密度影。", "bbox": [405, 784, 524, 800]},
	{"text": "胸部CT平扫+增强：", "bbox": [387, 805, 470, 821]},
	{"text": "【肺野】两肺野纹理清晰，左肺下叶见斑片状高", "bbox": [405, 826, 608, 842]},
	{"text": "移动影像浏览", "bbox": [470, 859, 525, 873]},
	{"text": "© 2022 南京鼓楼医院影像云平台 V1.0", "bbox": [420, 878, 575, 893]}
]
2026-08-06 10:37:37,870 INFO     30 [qwen-vl-text] coord API: raw_items=29, valid_items=29, elapsed=10.2s
2026-08-06 10:37:37,871 INFO     30 [qwen-vl-text] coord item[0]: text=南京鼓楼医院云胶片, bbox=[444, 118, 552, 137]
2026-08-06 10:37:37,871 INFO     30 [qwen-vl-text] coord item[1]: text=女/75岁, bbox=[588, 163, 629, 178]
2026-08-06 10:37:37,871 INFO     30 [qwen-vl-text] coord item[2]: text=设备类型 CT 患者类型 无, bbox=[387, 205, 594, 223]
2026-08-06 10:37:37,871 INFO     30 [qwen-vl-text] coord item[3]: text=检查项目 [CT平扫+增强（颈部、胸部、上腹部、下, bbox=[387, 250, 618, 267]
2026-08-06 10:37:37,871 INFO     30 [qwen-vl-text] coord item[4]: text=腹部、盆腔）], bbox=[438, 267, 502, 282]
2026-08-06 10:37:37,871 INFO     30 [qwen-vl-text] coord item[5]: text=PDF报告 图像 分享, bbox=[396, 315, 588, 337]
2026-08-06 10:37:37,871 INFO     30 [qwen-vl-text] coord item[6]: text=报告 2025-10-08, bbox=[387, 367, 609, 387]
2026-08-06 10:37:37,871 INFO     30 [qwen-vl-text] coord item[7]: text=影像描述, bbox=[387, 411, 431, 427]
2026-08-06 10:37:37,872 INFO     30 [qwen-vl-text] coord item[8]: text=颈部软组织CT平扫+增强：, bbox=[387, 451, 500, 467]
2026-08-06 10:37:37,872 INFO     30 [qwen-vl-text] coord item[9]: text=【所见咽部】所见咽腔结构对称，未见明显异常, bbox=[405, 472, 608, 488]
2026-08-06 10:37:37,872 INFO     30 [qwen-vl-text] coord item[10]: text=密度影。增强后未见明显异常强化。, bbox=[387, 493, 540, 508]
2026-08-06 10:37:37,872 INFO     30 [qwen-vl-text] coord item[11]: text=【喉部及下咽部】喉腔结构对称，会厌、声带、, bbox=[405, 513, 602, 529]
2026-08-06 10:37:37,872 INFO     30 [qwen-vl-text] coord item[12]: text=梨状窝形态及密度未见明显异常。增强后未见明显, bbox=[387, 534, 608, 550]
2026-08-06 10:37:37,872 INFO     30 [qwen-vl-text] coord item[13]: text=异常强化。, bbox=[387, 555, 435, 570]
2026-08-06 10:37:37,873 INFO     30 [qwen-vl-text] coord item[14]: text=【甲状腺及甲状旁腺区】甲状腺左右叶大小、形, bbox=[405, 576, 608, 591]
2026-08-06 10:37:37,873 INFO     30 [qwen-vl-text] coord item[15]: text=态正常，甲状腺双叶低密度结节；甲状旁腺区未见, bbox=[387, 596, 608, 612]
2026-08-06 10:37:37,873 INFO     30 [qwen-vl-text] coord item[16]: text=明显占位性病变。, bbox=[387, 617, 464, 633]
2026-08-06 10:37:37,873 INFO     30 [qwen-vl-text] coord item[17]: text=【唾液腺】双侧腮腺、颌下腺形态密度未见明显, bbox=[405, 638, 608, 654]
2026-08-06 10:37:37,873 INFO     30 [qwen-vl-text] coord item[18]: text=异常。增强后未见明显异常强化。, bbox=[387, 659, 531, 674]
2026-08-06 10:37:37,873 INFO     30 [qwen-vl-text] coord item[19]: text=【气管及食管】气管居中，管腔通畅；食管颈段, bbox=[405, 680, 608, 695]
2026-08-06 10:37:37,874 INFO     30 [qwen-vl-text] coord item[20]: text=管壁未见明显增厚。, bbox=[387, 701, 473, 717]
2026-08-06 10:37:37,874 INFO     30 [qwen-vl-text] coord item[21]: text=【颈部间隙】脂肪间隙清晰，未见明显异常密度, bbox=[405, 722, 608, 737]
2026-08-06 10:37:37,874 INFO     30 [qwen-vl-text] coord item[22]: text=影。增强后未见明显异常强化。, bbox=[387, 742, 521, 758]
2026-08-06 10:37:37,874 INFO     30 [qwen-vl-text] coord item[23]: text=【淋巴结】未见明显肿大淋巴结。, bbox=[405, 763, 543, 779]
2026-08-06 10:37:37,874 INFO     30 [qwen-vl-text] coord item[24]: text=【其他】副鼻窦内低密度影。, bbox=[405, 784, 524, 800]
2026-08-06 10:37:37,874 INFO     30 [qwen-vl-text] coord item[25]: text=胸部CT平扫+增强：, bbox=[387, 805, 470, 821]
2026-08-06 10:37:37,874 INFO     30 [qwen-vl-text] coord item[26]: text=【肺野】两肺野纹理清晰，左肺下叶见斑片状高, bbox=[405, 826, 608, 842]
2026-08-06 10:37:37,874 INFO     30 [qwen-vl-text] coord item[27]: text=移动影像浏览, bbox=[470, 859, 525, 873]
2026-08-06 10:37:37,874 INFO     30 [qwen-vl-text] coord item[28]: text=© 2022 南京鼓楼医院影像云平台 V1.0, bbox=[420, 878, 575, 893]
2026-08-06 10:37:37,875 INFO     30 [qwen-vl-text] page=7 — 29/29 coords, api_time=10.2s
2026-08-06 10:37:37,879 INFO     30 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=590262, prompt_len=1230
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共31行）
["南京鼓楼医院云胶片", "女/75岁", "设备类型 CT 患者类型 无", "检查项目 [CT平扫+增强（颈部、胸部、上腹部、下", "腹部、盆腔）]", "PDF报告 图像 分享", "【肺野】两肺野纹理清晰，左肺下叶见斑片状高", "密度影。两肺多发结节，较大者：右肺上叶（Img7", "9）见一实性结节影，大小约5mm×3mm。两肺索", "条及片絮影；右肺上叶局部透亮区。", "【肺门】双肺门多发小淋巴结，部分稍大。", "【气管及支气管】左下肺支气管闭塞伴阻塞性炎", "症，病灶周围结节影。", "【纵隔】纵隔居中，纵隔内多发小淋巴结，部分", "稍大，较大者短径约10mm。", "【心脏及大血管】心影增大；主动脉及冠状动", "脉壁见致密影。", "【胸膜及胸腔】胸膜：两侧胸膜可见增厚；胸腔", "积液：否。增强后未见明显异常强化。", "【膈肌】光整，未见明显异常抬高。增强后未见", "明显异常强化。", "【胸壁】胸廓对称，骨质未见明显异常。增强后", "未见明显异常强化。", "上腹部CT平扫+增强：", "【肝脏】各叶比例在正常范围内，外形轮廓规", "则，肝内小圆形无强化低密度影，较大者长径约6", "mm。静脉期肝左叶小片状稍低密度影（薄层im29", "0）。", "【胆囊及胆管】胆囊形态、大小正常，囊壁未见", "移动影像浏览", "© 2022 南京鼓楼医院影像云平台 V1.0"]

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
2026-08-06 10:37:49,061 INFO     30 [qwen-vl-text] coord API raw response (len=1891):
[
	{"text": "南京鼓楼医院云胶片", "bbox": [444, 118, 552, 136]},
	{"text": "女/75岁", "bbox": [588, 163, 628, 177]},
	{"text": "设备类型 CT 患者类型 无", "bbox": [387, 205, 594, 222]},
	{"text": "检查项目 [CT平扫+增强（颈部、胸部、上腹部、下", "bbox": [387, 250, 617, 267]},
	{"text": "腹部、盆腔）]", "bbox": [438, 267, 501, 282]},
	{"text": "PDF报告 图像 分享", "bbox": [397, 317, 587, 335]},
	{"text": "【肺野】两肺野纹理清晰，左肺下叶见斑片状高", "bbox": [405, 362, 608, 378]},
	{"text": "密度影。两肺多发结节，较大者：右肺上叶（Img7", "bbox": [387, 382, 608, 398]},
	{"text": "9）见一实性结节影，大小约5mm×3mm。两肺索", "bbox": [387, 402, 608, 418]},
	{"text": "条及片絮影；右肺上叶局部透亮区。", "bbox": [387, 422, 542, 438]},
	{"text": "【肺门】双肺门多发小淋巴结，部分稍大。", "bbox": [405, 444, 581, 459]},
	{"text": "【气管及支气管】左下肺支气管闭塞伴阻塞性炎", "bbox": [405, 464, 608, 480]},
	{"text": "症，病灶周围结节影。", "bbox": [387, 485, 484, 501]},
	{"text": "【纵隔】纵隔居中，纵隔内多发小淋巴结，部分", "bbox": [405, 506, 608, 522]},
	{"text": "稍大，较大者短径约10mm。", "bbox": [387, 527, 509, 543]},
	{"text": "【心脏及大血管】心影增大；主动脉及冠状动", "bbox": [405, 548, 608, 564]},
	{"text": "脉壁见致密影。", "bbox": [387, 569, 453, 585]},
	{"text": "【胸膜及胸腔】胸膜：两侧胸膜可见增厚；胸腔", "bbox": [405, 590, 608, 606]},
	{"text": "积液：否。增强后未见明显异常强化。", "bbox": [387, 611, 551, 627]},
	{"text": "【膈肌】光整，未见明显异常抬高。增强后未见", "bbox": [405, 632, 608, 648]},
	{"text": "明显异常强化。", "bbox": [387, 653, 453, 669]},
	{"text": "【胸壁】胸廓对称，骨质未见明显异常。增强后", "bbox": [405, 674, 608, 690]},
	{"text": "未见明显异常强化。", "bbox": [387, 695, 473, 711]},
	{"text": "上腹部CT平扫+增强：", "bbox": [387, 715, 481, 731]},
	{"text": "【肝脏】各叶比例在正常范围内，外形轮廓规", "bbox": [405, 736, 608, 752]},
	{"text": "则，肝内小圆形无强化低密度影，较大者长径约6", "bbox": [387, 757, 608, 773]},
	{"text": "mm。静脉期肝左叶小片状稍低密度影（薄层im29", "bbox": [387, 777, 608, 793]},
	{"text": "0）。", "bbox": [387, 798, 403, 814]},
	{"text": "【胆囊及胆管】胆囊形态、大小正常，囊壁未见", "bbox": [405, 819, 608, 835]},
	{"text": "移动影像浏览", "bbox": [470, 859, 525, 872]},
	{"text": "© 2022 南京鼓楼医院影像云平台 V1.0", "bbox": [420, 878, 575, 892]}
]
2026-08-06 10:37:49,062 INFO     30 [qwen-vl-text] coord API: raw_items=31, valid_items=31, elapsed=11.2s
2026-08-06 10:37:49,062 INFO     30 [qwen-vl-text] coord item[0]: text=南京鼓楼医院云胶片, bbox=[444, 118, 552, 136]
2026-08-06 10:37:49,062 INFO     30 [qwen-vl-text] coord item[1]: text=女/75岁, bbox=[588, 163, 628, 177]
2026-08-06 10:37:49,062 INFO     30 [qwen-vl-text] coord item[2]: text=设备类型 CT 患者类型 无, bbox=[387, 205, 594, 222]
2026-08-06 10:37:49,062 INFO     30 [qwen-vl-text] coord item[3]: text=检查项目 [CT平扫+增强（颈部、胸部、上腹部、下, bbox=[387, 250, 617, 267]
2026-08-06 10:37:49,062 INFO     30 [qwen-vl-text] coord item[4]: text=腹部、盆腔）], bbox=[438, 267, 501, 282]
2026-08-06 10:37:49,062 INFO     30 [qwen-vl-text] coord item[5]: text=PDF报告 图像 分享, bbox=[397, 317, 587, 335]
2026-08-06 10:37:49,063 INFO     30 [qwen-vl-text] coord item[6]: text=【肺野】两肺野纹理清晰，左肺下叶见斑片状高, bbox=[405, 362, 608, 378]
2026-08-06 10:37:49,063 INFO     30 [qwen-vl-text] coord item[7]: text=密度影。两肺多发结节，较大者：右肺上叶（Img7, bbox=[387, 382, 608, 398]
2026-08-06 10:37:49,063 INFO     30 [qwen-vl-text] coord item[8]: text=9）见一实性结节影，大小约5mm×3mm。两肺索, bbox=[387, 402, 608, 418]
2026-08-06 10:37:49,063 INFO     30 [qwen-vl-text] coord item[9]: text=条及片絮影；右肺上叶局部透亮区。, bbox=[387, 422, 542, 438]
2026-08-06 10:37:49,063 INFO     30 [qwen-vl-text] coord item[10]: text=【肺门】双肺门多发小淋巴结，部分稍大。, bbox=[405, 444, 581, 459]
2026-08-06 10:37:49,063 INFO     30 [qwen-vl-text] coord item[11]: text=【气管及支气管】左下肺支气管闭塞伴阻塞性炎, bbox=[405, 464, 608, 480]
2026-08-06 10:37:49,063 INFO     30 [qwen-vl-text] coord item[12]: text=症，病灶周围结节影。, bbox=[387, 485, 484, 501]
2026-08-06 10:37:49,063 INFO     30 [qwen-vl-text] coord item[13]: text=【纵隔】纵隔居中，纵隔内多发小淋巴结，部分, bbox=[405, 506, 608, 522]
2026-08-06 10:37:49,063 INFO     30 [qwen-vl-text] coord item[14]: text=稍大，较大者短径约10mm。, bbox=[387, 527, 509, 543]
2026-08-06 10:37:49,063 INFO     30 [qwen-vl-text] coord item[15]: text=【心脏及大血管】心影增大；主动脉及冠状动, bbox=[405, 548, 608, 564]
2026-08-06 10:37:49,063 INFO     30 [qwen-vl-text] coord item[16]: text=脉壁见致密影。, bbox=[387, 569, 453, 585]
2026-08-06 10:37:49,063 INFO     30 [qwen-vl-text] coord item[17]: text=【胸膜及胸腔】胸膜：两侧胸膜可见增厚；胸腔, bbox=[405, 590, 608, 606]
2026-08-06 10:37:49,063 INFO     30 [qwen-vl-text] coord item[18]: text=积液：否。增强后未见明显异常强化。, bbox=[387, 611, 551, 627]
2026-08-06 10:37:49,064 INFO     30 [qwen-vl-text] coord item[19]: text=【膈肌】光整，未见明显异常抬高。增强后未见, bbox=[405, 632, 608, 648]
2026-08-06 10:37:49,064 INFO     30 [qwen-vl-text] coord item[20]: text=明显异常强化。, bbox=[387, 653, 453, 669]
2026-08-06 10:37:49,064 INFO     30 [qwen-vl-text] coord item[21]: text=【胸壁】胸廓对称，骨质未见明显异常。增强后, bbox=[405, 674, 608, 690]
2026-08-06 10:37:49,064 INFO     30 [qwen-vl-text] coord item[22]: text=未见明显异常强化。, bbox=[387, 695, 473, 711]
2026-08-06 10:37:49,064 INFO     30 [qwen-vl-text] coord item[23]: text=上腹部CT平扫+增强：, bbox=[387, 715, 481, 731]
2026-08-06 10:37:49,064 INFO     30 [qwen-vl-text] coord item[24]: text=【肝脏】各叶比例在正常范围内，外形轮廓规, bbox=[405, 736, 608, 752]
2026-08-06 10:37:49,064 INFO     30 [qwen-vl-text] coord item[25]: text=则，肝内小圆形无强化低密度影，较大者长径约6, bbox=[387, 757, 608, 773]
2026-08-06 10:37:49,064 INFO     30 [qwen-vl-text] coord item[26]: text=mm。静脉期肝左叶小片状稍低密度影（薄层im29, bbox=[387, 777, 608, 793]
2026-08-06 10:37:49,064 INFO     30 [qwen-vl-text] coord item[27]: text=0）。, bbox=[387, 798, 403, 814]
2026-08-06 10:37:49,064 INFO     30 [qwen-vl-text] coord item[28]: text=【胆囊及胆管】胆囊形态、大小正常，囊壁未见, bbox=[405, 819, 608, 835]
2026-08-06 10:37:49,064 INFO     30 [qwen-vl-text] coord item[29]: text=移动影像浏览, bbox=[470, 859, 525, 872]
2026-08-06 10:37:49,064 INFO     30 [qwen-vl-text] coord item[30]: text=© 2022 南京鼓楼医院影像云平台 V1.0, bbox=[420, 878, 575, 892]
2026-08-06 10:37:49,065 INFO     30 [qwen-vl-text] page=8 — 31/31 coords, api_time=11.2s
2026-08-06 10:37:49,068 INFO     30 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=594901, prompt_len=1245
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共32行）
["南京鼓楼医院云胶片", "女/75岁", "设备类型 CT 患者类型 无", "检查项目 [CT平扫+增强（颈部、胸部、上腹部、下", "腹部、盆腔）]", "PDF报告 图像 分享", "【胆囊及胆管】胆囊形态、大小正常，囊壁未见", "增厚，囊内未见明显异常密度影；肝内外胆管轻度", "扩张。", "【胰腺】形态、大小正常，实质内未见明显异常", "密度影；胰管未见明显扩张。增强后未见明显异常", "强化。", "【脾脏】形态、大小正常，实质内未见明显异常", "密度影。增强后未见明显异常强化。", "【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均", "匀，未见明显肿大淋巴结，未见明显渗出及积液。", "增强后未见明显异常强化。", "下腹部CT平扫+增强：", "【肾脏】两侧肾脏大小、形态、位置正常，右肾", "窦点状致密影；肾盂肾盏未见明显扩张。增强后未", "见明显异常强化。", "【肾上腺】双肾上腺增粗，左肾上腺低密度结", "节，长径约12mm,可见强化。", "【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均", "匀，未见明显肿大淋巴结，未见明显渗出及积液。", "增强后未见明显异常强化。", "盆腔CT平扫+增强：", "【膀胱】充盈欠佳，壁未见明显增厚，其内未见", "明显异常密度影。增强后未见明显异常强化。", "【子宫及附件】子宫呈肌组织结构性空扫", "移动影像浏览", "© 2022 南京鼓楼医院影像云平台 V1.0"]

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
2026-08-06 10:38:00,083 INFO     30 [qwen-vl-text] coord API raw response (len=1947):
[
	{"text": "南京鼓楼医院云胶片", "bbox": [444, 118, 552, 137]},
	{"text": "女/75岁", "bbox": [588, 163, 629, 178]},
	{"text": "设备类型 CT 患者类型 无", "bbox": [387, 205, 594, 223]},
	{"text": "检查项目 [CT平扫+增强（颈部、胸部、上腹部、下", "bbox": [387, 250, 618, 267]},
	{"text": "腹部、盆腔）]", "bbox": [438, 267, 502, 282]},
	{"text": "PDF报告 图像 分享", "bbox": [398, 317, 587, 336]},
	{"text": "【胆囊及胆管】胆囊形态、大小正常，囊壁未见", "bbox": [405, 358, 608, 374]},
	{"text": "增厚，囊内未见明显异常密度影；肝内外胆管轻度", "bbox": [387, 379, 608, 395]},
	{"text": "扩张。", "bbox": [387, 400, 414, 415]},
	{"text": "【胰腺】形态、大小正常，实质内未见明显异常", "bbox": [405, 420, 608, 436]},
	{"text": "密度影；胰管未见明显扩张。增强后未见明显异常", "bbox": [387, 441, 608, 457]},
	{"text": "强化。", "bbox": [387, 462, 414, 477]},
	{"text": "【脾脏】形态、大小正常，实质内未见明显异常", "bbox": [405, 483, 608, 499]},
	{"text": "密度影。增强后未见明显异常强化。", "bbox": [387, 504, 541, 519]},
	{"text": "【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均", "bbox": [405, 524, 608, 540]},
	{"text": "匀，未见明显肿大淋巴结，未见明显渗出及积液。", "bbox": [387, 545, 604, 561]},
	{"text": "增强后未见明显异常强化。", "bbox": [387, 566, 502, 582]},
	{"text": "下腹部CT平扫+增强：", "bbox": [387, 587, 481, 603]},
	{"text": "【肾脏】两侧肾脏大小、形态、位置正常，右肾", "bbox": [405, 608, 608, 624]},
	{"text": "窦点状致密影；肾盂肾盏未见明显扩张。增强后未", "bbox": [387, 629, 608, 645]},
	{"text": "见明显异常强化。", "bbox": [387, 650, 463, 666]},
	{"text": "【肾上腺】双肾上腺增粗，左肾上腺低密度结", "bbox": [405, 670, 608, 686]},
	{"text": "节，长径约12mm,可见强化。", "bbox": [387, 691, 512, 707]},
	{"text": "【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均", "bbox": [405, 712, 608, 728]},
	{"text": "匀，未见明显肿大淋巴结，未见明显渗出及积液。", "bbox": [387, 733, 604, 749]},
	{"text": "增强后未见明显异常强化。", "bbox": [387, 754, 502, 770]},
	{"text": "盆腔CT平扫+增强：", "bbox": [387, 774, 471, 790]},
	{"text": "【膀胱】充盈欠佳，壁未见明显增厚，其内未见", "bbox": [405, 795, 608, 811]},
	{"text": "明显异常密度影。增强后未见明显异常强化。", "bbox": [387, 816, 580, 832]},
	{"text": "【子宫及附件】子宫呈肌组织结构性空扫", "bbox": [405, 837, 598, 852]},
	{"text": "移动影像浏览", "bbox": [470, 859, 525, 873]},
	{"text": "© 2022 南京鼓楼医院影像云平台 V1.0", "bbox": [420, 878, 575, 893]}
]
2026-08-06 10:38:00,084 INFO     30 [qwen-vl-text] coord API: raw_items=32, valid_items=32, elapsed=11.0s
2026-08-06 10:38:00,085 INFO     30 [qwen-vl-text] coord item[0]: text=南京鼓楼医院云胶片, bbox=[444, 118, 552, 137]
2026-08-06 10:38:00,085 INFO     30 [qwen-vl-text] coord item[1]: text=女/75岁, bbox=[588, 163, 629, 178]
2026-08-06 10:38:00,085 INFO     30 [qwen-vl-text] coord item[2]: text=设备类型 CT 患者类型 无, bbox=[387, 205, 594, 223]
2026-08-06 10:38:00,085 INFO     30 [qwen-vl-text] coord item[3]: text=检查项目 [CT平扫+增强（颈部、胸部、上腹部、下, bbox=[387, 250, 618, 267]
2026-08-06 10:38:00,086 INFO     30 [qwen-vl-text] coord item[4]: text=腹部、盆腔）], bbox=[438, 267, 502, 282]
2026-08-06 10:38:00,086 INFO     30 [qwen-vl-text] coord item[5]: text=PDF报告 图像 分享, bbox=[398, 317, 587, 336]
2026-08-06 10:38:00,086 INFO     30 [qwen-vl-text] coord item[6]: text=【胆囊及胆管】胆囊形态、大小正常，囊壁未见, bbox=[405, 358, 608, 374]
2026-08-06 10:38:00,086 INFO     30 [qwen-vl-text] coord item[7]: text=增厚，囊内未见明显异常密度影；肝内外胆管轻度, bbox=[387, 379, 608, 395]
2026-08-06 10:38:00,086 INFO     30 [qwen-vl-text] coord item[8]: text=扩张。, bbox=[387, 400, 414, 415]
2026-08-06 10:38:00,086 INFO     30 [qwen-vl-text] coord item[9]: text=【胰腺】形态、大小正常，实质内未见明显异常, bbox=[405, 420, 608, 436]
2026-08-06 10:38:00,086 INFO     30 [qwen-vl-text] coord item[10]: text=密度影；胰管未见明显扩张。增强后未见明显异常, bbox=[387, 441, 608, 457]
2026-08-06 10:38:00,087 INFO     30 [qwen-vl-text] coord item[11]: text=强化。, bbox=[387, 462, 414, 477]
2026-08-06 10:38:00,087 INFO     30 [qwen-vl-text] coord item[12]: text=【脾脏】形态、大小正常，实质内未见明显异常, bbox=[405, 483, 608, 499]
2026-08-06 10:38:00,087 INFO     30 [qwen-vl-text] coord item[13]: text=密度影。增强后未见明显异常强化。, bbox=[387, 504, 541, 519]
2026-08-06 10:38:00,087 INFO     30 [qwen-vl-text] coord item[14]: text=【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均, bbox=[405, 524, 608, 540]
2026-08-06 10:38:00,087 INFO     30 [qwen-vl-text] coord item[15]: text=匀，未见明显肿大淋巴结，未见明显渗出及积液。, bbox=[387, 545, 604, 561]
2026-08-06 10:38:00,087 INFO     30 [qwen-vl-text] coord item[16]: text=增强后未见明显异常强化。, bbox=[387, 566, 502, 582]
2026-08-06 10:38:00,087 INFO     30 [qwen-vl-text] coord item[17]: text=下腹部CT平扫+增强：, bbox=[387, 587, 481, 603]
2026-08-06 10:38:00,087 INFO     30 [qwen-vl-text] coord item[18]: text=【肾脏】两侧肾脏大小、形态、位置正常，右肾, bbox=[405, 608, 608, 624]
2026-08-06 10:38:00,087 INFO     30 [qwen-vl-text] coord item[19]: text=窦点状致密影；肾盂肾盏未见明显扩张。增强后未, bbox=[387, 629, 608, 645]
2026-08-06 10:38:00,087 INFO     30 [qwen-vl-text] coord item[20]: text=见明显异常强化。, bbox=[387, 650, 463, 666]
2026-08-06 10:38:00,087 INFO     30 [qwen-vl-text] coord item[21]: text=【肾上腺】双肾上腺增粗，左肾上腺低密度结, bbox=[405, 670, 608, 686]
2026-08-06 10:38:00,088 INFO     30 [qwen-vl-text] coord item[22]: text=节，长径约12mm,可见强化。, bbox=[387, 691, 512, 707]
2026-08-06 10:38:00,088 INFO     30 [qwen-vl-text] coord item[23]: text=【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均, bbox=[405, 712, 608, 728]
2026-08-06 10:38:00,088 INFO     30 [qwen-vl-text] coord item[24]: text=匀，未见明显肿大淋巴结，未见明显渗出及积液。, bbox=[387, 733, 604, 749]
2026-08-06 10:38:00,088 INFO     30 [qwen-vl-text] coord item[25]: text=增强后未见明显异常强化。, bbox=[387, 754, 502, 770]
2026-08-06 10:38:00,088 INFO     30 [qwen-vl-text] coord item[26]: text=盆腔CT平扫+增强：, bbox=[387, 774, 471, 790]
2026-08-06 10:38:00,088 INFO     30 [qwen-vl-text] coord item[27]: text=【膀胱】充盈欠佳，壁未见明显增厚，其内未见, bbox=[405, 795, 608, 811]
2026-08-06 10:38:00,088 INFO     30 [qwen-vl-text] coord item[28]: text=明显异常密度影。增强后未见明显异常强化。, bbox=[387, 816, 580, 832]
2026-08-06 10:38:00,088 INFO     30 [qwen-vl-text] coord item[29]: text=【子宫及附件】子宫呈肌组织结构性空扫, bbox=[405, 837, 598, 852]
2026-08-06 10:38:00,088 INFO     30 [qwen-vl-text] coord item[30]: text=移动影像浏览, bbox=[470, 859, 525, 873]
2026-08-06 10:38:00,089 INFO     30 [qwen-vl-text] coord item[31]: text=© 2022 南京鼓楼医院影像云平台 V1.0, bbox=[420, 878, 575, 893]
2026-08-06 10:38:00,090 INFO     30 [qwen-vl-text] page=9 — 32/32 coords, api_time=11.0s
2026-08-06 10:38:00,094 INFO     30 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=566615, prompt_len=1201
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共30行）
["南京鼓楼医院云胶片", "女/75岁", "设备类型 CT 患者类型 无", "检查项目 [CT平扫+增强（颈部、胸部、上腹部、下", "腹部、盆腔）]", "PDF报告 图像 分享", "诊断意见", "1.肺癌复查：左肺下叶斑片影较前（2025-07-15）", "明显缩小，左下肺支气管闭塞伴阻塞性炎症，较前", "缓解，密切随诊；双侧纵隔内及双肺门多发稍大淋", "巴结，部分较前稍缩小。", "2.两肺多发结节，较前变化不大，密切随诊。", "3.两侧胸膜增厚；两肺索条及炎性渗出，较前缓", "解；右肺上叶局限性肺气肿。", "4.心影增大；主动脉及冠状动脉壁钙化。", "5.肝脏小囊肿；静脉期肝左叶小片状稍低密度影", "（薄层im290），较前相仿，随诊。", "6.肝内外胆管轻度扩张。", "7.双肾上腺增粗，左肾上腺腺瘤可能，结合专科检", "查；右肾小结石。", "8.子宫肌瘤可能，结合妇科超声；盆腔内钙化结", "节。", "9.下腹腔内肠系膜间隙多发稍大淋巴结。", "10.食管下段壁轻度增厚；乙状结肠迂曲冗长；结肠", "内容物多；十二指肠降部憩室；结合临床体征随", "诊。", "11.右肩部皮下低密度结节，较前相仿，随诊；L4及", "以上椎体I°滑脱。", "移动影像浏览", "© 2022 南京鼓楼医院影像云平台 V1.0"]

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
2026-08-06 10:38:10,844 INFO     30 [qwen-vl-text] coord API raw response (len=1821):
[
	{"text": "南京鼓楼医院云胶片", "bbox": [444, 118, 552, 136]},
	{"text": "女/75岁", "bbox": [588, 163, 629, 177]},
	{"text": "设备类型 CT 患者类型 无", "bbox": [387, 205, 594, 222]},
	{"text": "检查项目 [CT平扫+增强（颈部、胸部、上腹部、下", "bbox": [387, 250, 618, 267]},
	{"text": "腹部、盆腔）]", "bbox": [438, 267, 502, 282]},
	{"text": "PDF报告 图像 分享", "bbox": [397, 317, 587, 335]},
	{"text": "诊断意见", "bbox": [387, 368, 431, 384]},
	{"text": "1.肺癌复查：左肺下叶斑片影较前（2025-07-15）", "bbox": [387, 407, 603, 423]},
	{"text": "明显缩小，左下肺支气管闭塞伴阻塞性炎症，较前", "bbox": [387, 428, 608, 444]},
	{"text": "缓解，密切随诊；双侧纵隔内及双肺门多发稍大淋", "bbox": [387, 449, 608, 465]},
	{"text": "巴结，部分较前稍缩小。", "bbox": [387, 470, 494, 486]},
	{"text": "2.两肺多发结节，较前变化不大，密切随诊。", "bbox": [387, 491, 578, 507]},
	{"text": "3.两侧胸膜增厚；两肺索条及炎性渗出，较前缓", "bbox": [387, 512, 608, 528]},
	{"text": "解；右肺上叶局限性肺气肿。", "bbox": [387, 532, 515, 548]},
	{"text": "4.心影增大；主动脉及冠状动脉壁钙化。", "bbox": [387, 553, 558, 569]},
	{"text": "5.肝脏小囊肿；静脉期肝左叶小片状稍低密度影", "bbox": [387, 574, 608, 590]},
	{"text": "（薄层im290），较前相仿，随诊。", "bbox": [393, 595, 534, 611]},
	{"text": "6.肝内外胆管轻度扩张。", "bbox": [387, 616, 491, 632]},
	{"text": "7.双肾上腺增粗，左肾上腺腺瘤可能，结合专科检", "bbox": [387, 637, 608, 653]},
	{"text": "查；右肾小结石。", "bbox": [387, 658, 464, 674]},
	{"text": "8.子宫肌瘤可能，结合妇科超声；盆腔内钙化结", "bbox": [387, 678, 608, 694]},
	{"text": "节。", "bbox": [387, 699, 405, 715]},
	{"text": "9.下腹腔内肠系膜间隙多发稍大淋巴结。", "bbox": [387, 720, 559, 736]},
	{"text": "10.食管下段壁轻度增厚；乙状结肠迂曲冗长；结肠", "bbox": [387, 741, 608, 757]},
	{"text": "内容物多；十二指肠降部憩室；结合临床体征随", "bbox": [387, 762, 608, 778]},
	{"text": "诊。", "bbox": [387, 783, 405, 799]},
	{"text": "11.右肩部皮下低密度结节，较前相仿，随诊；L4及", "bbox": [387, 804, 608, 820]},
	{"text": "以上椎体I°滑脱。", "bbox": [387, 825, 460, 841]},
	{"text": "移动影像浏览", "bbox": [470, 860, 525, 873]},
	{"text": "© 2022 南京鼓楼医院影像云平台 V1.0", "bbox": [420, 878, 575, 893]}
]
2026-08-06 10:38:10,845 INFO     30 [qwen-vl-text] coord API: raw_items=30, valid_items=30, elapsed=10.7s
2026-08-06 10:38:10,845 INFO     30 [qwen-vl-text] coord item[0]: text=南京鼓楼医院云胶片, bbox=[444, 118, 552, 136]
2026-08-06 10:38:10,845 INFO     30 [qwen-vl-text] coord item[1]: text=女/75岁, bbox=[588, 163, 629, 177]
2026-08-06 10:38:10,845 INFO     30 [qwen-vl-text] coord item[2]: text=设备类型 CT 患者类型 无, bbox=[387, 205, 594, 222]
2026-08-06 10:38:10,845 INFO     30 [qwen-vl-text] coord item[3]: text=检查项目 [CT平扫+增强（颈部、胸部、上腹部、下, bbox=[387, 250, 618, 267]
2026-08-06 10:38:10,845 INFO     30 [qwen-vl-text] coord item[4]: text=腹部、盆腔）], bbox=[438, 267, 502, 282]
2026-08-06 10:38:10,845 INFO     30 [qwen-vl-text] coord item[5]: text=PDF报告 图像 分享, bbox=[397, 317, 587, 335]
2026-08-06 10:38:10,845 INFO     30 [qwen-vl-text] coord item[6]: text=诊断意见, bbox=[387, 368, 431, 384]
2026-08-06 10:38:10,845 INFO     30 [qwen-vl-text] coord item[7]: text=1.肺癌复查：左肺下叶斑片影较前（2025-07-15）, bbox=[387, 407, 603, 423]
2026-08-06 10:38:10,845 INFO     30 [qwen-vl-text] coord item[8]: text=明显缩小，左下肺支气管闭塞伴阻塞性炎症，较前, bbox=[387, 428, 608, 444]
2026-08-06 10:38:10,845 INFO     30 [qwen-vl-text] coord item[9]: text=缓解，密切随诊；双侧纵隔内及双肺门多发稍大淋, bbox=[387, 449, 608, 465]
2026-08-06 10:38:10,845 INFO     30 [qwen-vl-text] coord item[10]: text=巴结，部分较前稍缩小。, bbox=[387, 470, 494, 486]
2026-08-06 10:38:10,845 INFO     30 [qwen-vl-text] coord item[11]: text=2.两肺多发结节，较前变化不大，密切随诊。, bbox=[387, 491, 578, 507]
2026-08-06 10:38:10,846 INFO     30 [qwen-vl-text] coord item[12]: text=3.两侧胸膜增厚；两肺索条及炎性渗出，较前缓, bbox=[387, 512, 608, 528]
2026-08-06 10:38:10,846 INFO     30 [qwen-vl-text] coord item[13]: text=解；右肺上叶局限性肺气肿。, bbox=[387, 532, 515, 548]
2026-08-06 10:38:10,846 INFO     30 [qwen-vl-text] coord item[14]: text=4.心影增大；主动脉及冠状动脉壁钙化。, bbox=[387, 553, 558, 569]
2026-08-06 10:38:10,846 INFO     30 [qwen-vl-text] coord item[15]: text=5.肝脏小囊肿；静脉期肝左叶小片状稍低密度影, bbox=[387, 574, 608, 590]
2026-08-06 10:38:10,846 INFO     30 [qwen-vl-text] coord item[16]: text=（薄层im290），较前相仿，随诊。, bbox=[393, 595, 534, 611]
2026-08-06 10:38:10,846 INFO     30 [qwen-vl-text] coord item[17]: text=6.肝内外胆管轻度扩张。, bbox=[387, 616, 491, 632]
2026-08-06 10:38:10,846 INFO     30 [qwen-vl-text] coord item[18]: text=7.双肾上腺增粗，左肾上腺腺瘤可能，结合专科检, bbox=[387, 637, 608, 653]
2026-08-06 10:38:10,846 INFO     30 [qwen-vl-text] coord item[19]: text=查；右肾小结石。, bbox=[387, 658, 464, 674]
2026-08-06 10:38:10,846 INFO     30 [qwen-vl-text] coord item[20]: text=8.子宫肌瘤可能，结合妇科超声；盆腔内钙化结, bbox=[387, 678, 608, 694]
2026-08-06 10:38:10,846 INFO     30 [qwen-vl-text] coord item[21]: text=节。, bbox=[387, 699, 405, 715]
2026-08-06 10:38:10,846 INFO     30 [qwen-vl-text] coord item[22]: text=9.下腹腔内肠系膜间隙多发稍大淋巴结。, bbox=[387, 720, 559, 736]
2026-08-06 10:38:10,846 INFO     30 [qwen-vl-text] coord item[23]: text=10.食管下段壁轻度增厚；乙状结肠迂曲冗长；结肠, bbox=[387, 741, 608, 757]
2026-08-06 10:38:10,846 INFO     30 [qwen-vl-text] coord item[24]: text=内容物多；十二指肠降部憩室；结合临床体征随, bbox=[387, 762, 608, 778]
2026-08-06 10:38:10,846 INFO     30 [qwen-vl-text] coord item[25]: text=诊。, bbox=[387, 783, 405, 799]
2026-08-06 10:38:10,847 INFO     30 [qwen-vl-text] coord item[26]: text=11.右肩部皮下低密度结节，较前相仿，随诊；L4及, bbox=[387, 804, 608, 820]
2026-08-06 10:38:10,847 INFO     30 [qwen-vl-text] coord item[27]: text=以上椎体I°滑脱。, bbox=[387, 825, 460, 841]
2026-08-06 10:38:10,847 INFO     30 [qwen-vl-text] coord item[28]: text=移动影像浏览, bbox=[470, 860, 525, 873]
2026-08-06 10:38:10,847 INFO     30 [qwen-vl-text] coord item[29]: text=© 2022 南京鼓楼医院影像云平台 V1.0, bbox=[420, 878, 575, 893]
2026-08-06 10:38:10,847 INFO     30 [qwen-vl-text] page=10 — 30/30 coords, api_time=10.7s
2026-08-06 10:38:10,848 INFO     30 [qwen-vl-text] new_positions (122):
[[7, 373.79916650390624, 464.7232880859375, 70.24256811523438, 81.55281213378906], [7, 495.03132861328123, 529.5488192138672, 97.0299881591797, 105.95912817382813], [7, 325.8114356689453, 500.0826687011719, 122.03158020019532, 132.74654821777344], [7, 325.8114356689453, 520.2880290527344, 148.81900024414062, 158.9386922607422], [7, 368.74782641601564, 422.62878735351563, 158.9386922607422, 167.86783227539064], [7, 333.38844580078126, 495.03132861328123, 187.5119403076172, 200.60801232910157], [7, 325.8114356689453, 512.7110189208985, 218.46629235839845, 230.3718123779297], [7, 325.8114356689453, 362.8545963134766, 244.6584364013672, 254.1828524169922], [7, 325.8114356689453, 420.94500732421875, 268.4694764404297, 277.9938924560547], [7, 340.9654559326172, 511.86912890625, 280.9702724609375, 290.4946884765625], [7, 325.8114356689453, 454.62060791015625, 293.47106848144534, 302.40020849609374], [7, 340.9654559326172, 506.81778881835936, 305.3765885009766, 314.9010045166016], [7, 325.8114356689453, 511.86912890625, 317.8773845214844, 327.4018005371094], [7, 325.8114356689453, 366.2221563720703, 330.3781805419922, 339.30732055664066], [7, 340.9654559326172, 511.86912890625, 342.87897656250004, 351.80811657714844], [7, 325.8114356689453, 511.86912890625, 354.78449658203124, 364.3089125976563], [7, 325.8114356689453, 390.636966796875, 367.2852926025391, 376.80970861816405], [7, 340.9654559326172, 511.86912890625, 379.7860886230469, 389.3105046386719], [7, 325.8114356689453, 447.0435977783203, 392.2868846435547, 401.21602465820314], [7, 340.9654559326172, 511.86912890625, 404.7876806640625, 413.716820678711], [7, 325.8114356689453, 398.2139769287109, 417.28847668457036, 426.81289270019533], [7, 340.9654559326172, 511.86912890625, 429.78927270507813, 438.7184127197266], [7, 325.8114356689453, 438.62469763183594, 441.6947927246094, 451.2192087402344], [7, 340.9654559326172, 457.14627795410155, 454.1955887451172, 463.7200047607422], [7, 340.9654559326172, 441.15036767578124, 466.696384765625, 476.22080078125003], [7, 325.8114356689453, 395.6883068847656, 479.19718078613283, 488.7215968017578], [7, 340.9654559326172, 511.86912890625, 491.69797680664067, 501.22239282226565], [7, 395.6883068847656, 441.9922576904297, 511.3420848388672, 519.6759488525391], [7, 353.59380615234375, 484.0867584228516, 522.6523288574219, 531.5814688720703], [8, 373.79916650390624, 464.7232880859375, 70.24256811523438, 80.9575361328125], [8, 495.03132861328123, 528.7069291992187, 97.0299881591797, 105.36385217285157], [8, 325.8114356689453, 500.0826687011719, 122.03158020019532, 132.15127221679688], [8, 325.8114356689453, 519.4461390380859, 148.81900024414062, 158.9386922607422], [8, 368.74782641601564, 421.78689733886716, 158.9386922607422, 167.86783227539064], [8, 334.23033581542967, 494.1894385986328, 188.70249230957032, 199.41746032714843], [8, 340.9654559326172, 511.86912890625, 215.48991235351562, 225.01432836914063], [8, 325.8114356689453, 511.86912890625, 227.39543237304687, 236.91984838867188], [8, 325.8114356689453, 511.86912890625, 239.30095239257813, 248.82536840820313], [8, 325.8114356689453, 456.30438793945314, 251.20647241210938, 260.7308884277344], [8, 340.9654559326172, 489.13809851074217, 264.30254443359377, 273.2316844482422], [8, 340.9654559326172, 511.86912890625, 276.208064453125, 285.73248046875], [8, 325.8114356689453, 407.47476708984374, 288.7088604736328, 298.23327648925783], [8, 340.9654559326172, 511.86912890625, 301.20965649414063, 310.7340725097656], [8, 325.8114356689453, 428.5220174560547, 313.71045251464847, 323.23486853027345], [8, 340.9654559326172, 511.86912890625, 326.21124853515624, 335.7356645507813], [8, 325.8114356689453, 381.3761766357422, 338.7120445556641, 348.23646057128906], [8, 340.9654559326172, 511.86912890625, 351.2128405761719, 360.7372565917969], [8, 325.8114356689453, 463.8813980712891, 363.7136365966797, 373.2380526123047], [8, 340.9654559326172, 511.86912890625, 376.2144326171875, 385.7388486328125], [8, 325.8114356689453, 381.3761766357422, 388.7152286376953, 398.23964465332034], [8, 340.9654559326172, 511.86912890625, 401.21602465820314, 410.7404406738281], [8, 325.8114356689453, 398.2139769287109, 413.716820678711, 423.24123669433595], [8, 325.8114356689453, 404.94909704589844, 425.6223406982422, 435.1467567138672], [8, 340.9654559326172, 511.86912890625, 438.12313671875, 447.64755273437504], [8, 325.8114356689453, 511.86912890625, 450.62393273925784, 460.1483487548828], [8, 325.8114356689453, 511.86912890625, 462.5294527587891, 472.05386877441407], [8, 325.8114356689453, 339.2816759033203, 475.03024877929687, 484.5546647949219], [8, 340.9654559326172, 511.86912890625, 487.5310447998047, 497.0554608154297], [8, 395.6883068847656, 441.9922576904297, 511.3420848388672, 519.0806728515626], [8, 353.59380615234375, 484.0867584228516, 522.6523288574219, 530.9861928710937], [9, 373.79916650390624, 464.7232880859375, 70.24256811523438, 81.55281213378906], [9, 495.03132861328123, 529.5488192138672, 97.0299881591797, 105.95912817382813], [9, 325.8114356689453, 500.0826687011719, 122.03158020019532, 132.74654821777344], [9, 325.8114356689453, 520.2880290527344, 148.81900024414062, 158.9386922607422], [9, 368.74782641601564, 422.62878735351563, 158.9386922607422, 167.86783227539064], [9, 335.07222583007814, 494.1894385986328, 188.70249230957032, 200.01273632812502], [9, 340.9654559326172, 511.86912890625, 213.10880834960938, 222.63322436523438], [9, 325.8114356689453, 511.86912890625, 225.6096043701172, 235.1340203857422], [9, 325.8114356689453, 348.5424660644531, 238.11040039062502, 247.03954040527344], [9, 340.9654559326172, 511.86912890625, 250.01592041015627, 259.5403364257813], [9, 325.8114356689453, 511.86912890625, 262.5167164306641, 272.04113244628905], [9, 325.8114356689453, 348.5424660644531, 275.0175124511719, 283.9466524658203], [9, 340.9654559326172, 511.86912890625, 287.5183084716797, 297.0427244873047], [9, 325.8114356689453, 455.46249792480467, 300.0191044921875, 308.948244506836], [9, 340.9654559326172, 511.86912890625, 311.9246245117188, 321.44904052734375], [9, 325.8114356689453, 508.50156884765624, 324.42542053222655, 333.9498365478516], [9, 325.8114356689453, 422.62878735351563, 336.9262165527344, 346.45063256835937], [9, 325.8114356689453, 404.94909704589844, 349.4270125732422, 358.9514285888672], [9, 340.9654559326172, 511.86912890625, 361.92780859375, 371.45222460937504], [9, 325.8114356689453, 511.86912890625, 374.42860461425784, 383.9530206298828], [9, 325.8114356689453, 389.79507678222654, 386.9294006347656, 396.45381665039065], [9, 340.9654559326172, 511.86912890625, 398.83492065429687, 408.3593366699219], [9, 325.8114356689453, 431.0476875, 411.3357166748047, 420.8601326904297], [9, 340.9654559326172, 511.86912890625, 423.83651269531254, 433.3609287109375], [9, 325.8114356689453, 508.50156884765624, 436.3373087158203, 445.86172473144535], [9, 325.8114356689453, 422.62878735351563, 448.83810473632815, 458.3625207519531], [9, 325.8114356689453, 396.5301968994141, 460.7436247558594, 470.2680407714844], [9, 340.9654559326172, 511.86912890625, 473.24442077636724, 482.7688367919922], [9, 325.8114356689453, 488.29620849609375, 485.745216796875, 495.26963281250005], [9, 340.9654559326172, 503.4502287597656, 498.24601281738285, 507.17515283203124], [9, 395.6883068847656, 441.9922576904297, 511.3420848388672, 519.6759488525391], [9, 353.59380615234375, 484.0867584228516, 522.6523288574219, 531.5814688720703], [10, 373.79916650390624, 464.7232880859375, 70.24256811523438, 80.9575361328125], [10, 495.03132861328123, 529.5488192138672, 97.0299881591797, 105.36385217285157], [10, 325.8114356689453, 500.0826687011719, 122.03158020019532, 132.15127221679688], [10, 325.8114356689453, 520.2880290527344, 148.81900024414062, 158.9386922607422], [10, 368.74782641601564, 422.62878735351563, 158.9386922607422, 167.86783227539064], [10, 334.23033581542967, 494.1894385986328, 188.70249230957032, 199.41746032714843], [10, 325.8114356689453, 362.8545963134766, 219.061568359375, 228.585984375], [10, 325.8114356689453, 507.65967883300783, 242.27733239746095, 251.80174841308596], [10, 325.8114356689453, 511.86912890625, 254.77812841796876, 264.30254443359377], [10, 325.8114356689453, 511.86912890625, 267.27892443847657, 276.8033404541016], [10, 325.8114356689453, 415.8936672363281, 279.7797204589844, 289.3041364746094], [10, 325.8114356689453, 486.61242846679687, 292.2805164794922, 301.8049324951172], [10, 325.8114356689453, 511.86912890625, 304.7813125, 314.305728515625], [10, 325.8114356689453, 433.5733575439453, 316.68683251953127, 326.21124853515624], [10, 325.8114356689453, 469.7746281738281, 329.1876285400391, 338.7120445556641], [10, 325.8114356689453, 511.86912890625, 341.6884245605469, 351.2128405761719], [10, 330.86277575683596, 449.5692678222656, 354.1892205810547, 363.7136365966797], [10, 325.8114356689453, 413.3679971923828, 366.6900166015625, 376.2144326171875], [10, 325.8114356689453, 511.86912890625, 379.1908126220703, 388.7152286376953], [10, 325.8114356689453, 390.636966796875, 391.69160864257816, 401.21602465820314], [10, 325.8114356689453, 511.86912890625, 403.5971286621094, 413.1215446777344], [10, 325.8114356689453, 340.9654559326172, 416.0979246826172, 425.6223406982422], [10, 325.8114356689453, 470.61651818847656, 428.598720703125, 438.12313671875], [10, 325.8114356689453, 511.86912890625, 441.0995167236328, 450.62393273925784], [10, 325.8114356689453, 511.86912890625, 453.60031274414064, 463.1247287597656], [10, 325.8114356689453, 340.9654559326172, 466.1011087646485, 475.62552478027345], [10, 325.8114356689453, 511.86912890625, 478.60190478515625, 488.1263208007813], [10, 325.8114356689453, 387.26940673828125, 491.1027008056641, 500.62711682128906], [10, 395.6883068847656, 441.9922576904297, 511.9373608398438, 519.6759488525391], [10, 353.59380615234375, 484.0867584228516, 522.6523288574219, 531.5814688720703]]
2026-08-06 10:38:10,848 INFO     30 [qwen-vl-text] ═══ DONE ═══ 122 positions, pages=4, time=73.5s
2026-08-06 10:38:10,877 INFO     30 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-06 10:38:10,877 INFO     30 [Trace] task=dfc102e2 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | Extractor:ExaminationReport | outputs={"chunks": "4 items, types={'ExaminationReport': 4}", "html": "", "json": "458 items", "markdown": "", "text": "", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "2 items, types={'LabReport': 2}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 4, \"chunks_Clinical\": 1, \"chunks_LabExam\": 2}"}
2026-08-06 10:38:10,877 INFO     30 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-06 10:38:10,881 INFO     30 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 30, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-06T10:38:10.880+00:00", "boot_at": "2026-08-06T10:03:12.657+00:00", "pending": 8, "lag": 0, "done": 1, "failed": 0, "current": {"00b9d592918111f18dbe1f8f96f1c395": {"id": "00b9d592918111f18dbe1f8f96f1c395", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786011867426, "task_type": "dataflow", "root_trace_id": "1ab3198c92574fb4b2701d0f5db7322f", "root_traceparent": "00-1ab3198c92574fb4b2701d0f5db7322f-bdaff6f64a5f4a64-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "dfc102e2918111f18dbe1f8f96f1c395": {"id": "dfc102e2918111f18dbe1f8f96f1c395", "doc_id": "de8a02fc918111f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786012241604, "task_type": "dataflow", "root_trace_id": "90f550f6b00248c3845d57a8e0bcf6fb", "root_traceparent": "00-90f550f6b00248c3845d57a8e0bcf6fb-5db7fb7d470dfe0d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-06 10:38:10,886 INFO     30 [ChunkMerger] Merged 8 chunks from 8 sources: {'Extractor:LabExam': 2, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 4} (filtered 4 noise chunks)
2026-08-06 10:38:10,918 INFO     30 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:38:11,212 INFO     30 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-06 10:38:11,212 INFO     30 [Trace] task=dfc102e2 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "8 items, types={'LabReport': 2, 'OutpatientRecord': 1, 'DischargeRecord': 1, 'ExaminationReport': 4}", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf"}
2026-08-06 10:38:11,212 INFO     30 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-06 10:38:13,274 INFO     30 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786012241981, 'update_date': datetime.datetime(2026, 8, 6, 10, 30, 41), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 585203, 'status': '1'}
2026-08-06 10:38:13,539 INFO     30 [EMBED-PIPELINE] batch[0:16] text_for_embed=   白细胞计数  WBC  4.2  10^9/L  3.5--9.5 10^9/L  False    中性粒细胞百分数  NEUT%  74.5  %  40--75 %  False    淋巴细胞百分数  LYM%  16.1  %  20--50 %  True    单核细胞百分数  MONO%  6.9  %  3--10 %  False    嗜酸性粒细胞百分数  EOS%  1.7  %  0.4--8 %  False    嗜碱性粒细胞百分数  BASO%  0.8  %  0-1 %  False    中性粒细胞绝对值  NEUT#  3.1  10^9/L  1.8--6.3 10^9/L  False    淋巴细胞绝对值  LYM#  0.7  10^9/L  1.1--3.2 10^9/L  True    单核细胞绝对值  MONO#  0.3  10^9/L  0.1--0.6 10^9/L  False    嗜酸性粒细胞绝对值  EOS#  0.07  10^9/L  0.02--0.52 10^9/L  False    嗜碱性粒细胞绝对值  BASO#  0.03  10^9/L  0--0.06 10^9/L  False    红细胞计数  RBC  4.01  10^12/L  3.8-5.1 10^12/L  False    血红蛋白量  HGB  126  g/L  115--150 g/L  False    红细胞压积  HCT  38.0  %  35--45 %  False    平均红细胞体积  MCV  94.7  fl  82--100 fl  False    平均红细胞血红蛋白含量  MCH  31.4  pg  27--34 pg  False    平均红细胞血红蛋白浓度  MCHC  332  g/L  316--354 g/L  False    红细胞体积分布宽度  RDW  13.6  %  0-14 %  False    血小板计数  PLT  179  10^9/L  125--350 10^9/L  False   
---
   丙氨酸氨基转移酶  ALT  50.3  U/L  7---40 U/L  True    天门冬氨酸氨基转移酶  AST  35.4  U/L  13---35 U/L  True    碱性磷酸酶  ALP  43.2  U/L  50---135 U/L  True    γ-谷氨酰基转移酶  GGT  130.5  U/L  7---45 U/L  True    乳酸脱氢酶  LDH  193  U/L  120---250 U/L  False    总胆红素  TBIL  10.2  umol/L  ≤21 umol/L  False    直接胆红素  DBIL  3.3  umol/L  ≤4 umol/L  False    胆碱酯酶  CHE  8.8  KU/L  5.3---11.3 KU/L  False    总蛋白  TP  78.9  g/L  65---85 g/L  False    白蛋白  ALB  48.8  g/L  40---55 g/L  False    球蛋白  GLB  30.1  g/L  20---40 g/L  False    白/球比例  A/G  1.62  None  1.2---2.4  False    总胆汁酸  TBA  4.0  umol/L  0---13 umol/L  False    亮氨酸氨肽酶  LAP  35.3  U/L  12---37 U/L  False    腺苷脱氨酶  ADA  21.3  U/L  0---25 U/L  False    葡萄糖  GLU  8.35  mmol/L  3.9---6.1 mmol/L  True    尿素  UREA  4.4  mmol/L  3.1---8.8 mmol/L  False    肌酐  CREA  73  umol/L  41---81 umol/L  False    尿酸  UA  221  umol/L  155---357 umol/L  False    总二氧化碳  TCO2  28.1  mmol/L  21---31 mmol/L  False    甘油三酯  TG  2.88  mmol/L  ≤1.7 mmol/L  True    总胆固醇  TC  5.81  mmol/L  3---5.7 mmol/L  True    H-脂蛋白胆固醇  HDL-C  1.26  mmol/L  1.03---1.55 mmol/L  False    L-脂蛋白胆固醇  LDL-C  3.66  mmol/L  健康人<3.4; 不同ASCVD危险人群目标值: 低危<3.4 中高危<2.6; 极高危<1.8 超高危<1.4 mmol/L  True    载脂蛋白A I  ApoA1  1.30  g/L  1---1.6 g/L  False    载脂蛋白B  ApoB  1.15  g/L  0.6---1.1 g/L  True    总钙  Ca  2.46  mmol/L  2.11---2.52 mmol/L  False    磷  P  1.37  mmol/L  0.85---1.51 mmol/L  False    钾  K  4.18  mmol/L  3.5---5.3 mmol/L  False    钠  Na  138.3  mmol/L  137---147 mmol/L  False    氯  Cl  101.7  mmol/L  99---110 mmol/L  False    C反应蛋白  CRP  11.2  mg/L  0---6 mg/L  True    肌酸激酶  CK  56  U/L  40---200 U/L  False    肌酸激酶MB同工酶  CK-MB  11  U/L  0---25 U/L  False    α-羟丁酸脱氢酶  α-HBDH  120  U/L  59---126.4 U/L  False    eGFR (CKD-EPI)  eGFR  69.6  ml/min/1.73m~2  >90 ml/min/1.73m~2  True   
---
南京鼓楼医院
南京大学医学院附属鼓楼医院
互联网医院
门诊病历
姓名:
性别:女
年龄:75岁
ID:
2026年03月16日15时20分 (江北)心血管内科门诊
主诉:要求进行心功能分级
病史:患者平时正常活动不受限。
过敏史:无吸烟史
药物过敏史。无流行病学史
体查:
级)
诊断:
1.心功能I级(NYHA分
2.高脂血症
处理:随诊
1.非诺贝特胶囊(力平之)
200mg/粒
用法:1粒
口服
一次/日
x3盒 28天
医师:
齐
第1页
---
2025.5.21确诊小细胞肺癌
2025.5.28-2025.7.16 依托泊苷+卡铂+斯鲁利
2025.8.13-2025.11.7 依托泊苷+斯鲁利
南京鼓楼医院
南京大学医学院附属鼓楼医院
出院记录
科别（江北）综合肿瘤中心 病区（江北）B7病区床号07床 姓名
住院号
姓名：
性别：女 年龄：75岁 婚姻：已婚 职业：农民
入院诊断：1. 肺恶性肿瘤（左肺，小细胞癌广泛期）2. 肥 入院日期： 2025年12月03日
厚型梗阻性心肌病 3. 纵隔淋巴结肿大 4. 肺门
淋巴结肿大 5. 锁骨上淋巴结肿大（双侧）6. 腋
下淋巴结肿大（右）7. 心功能III级（NYHA分级）
8. 甲状腺功能减退症 9. 高血压2级（极高
危）10. 肺气肿（局限性）11. 肺诊断性影像检
查的异常所见（肺结节）12. 二尖瓣反流（重度）
13. 心包积液（少量）14. 肾上腺结节（左侧）
手术名称：
手术日期：
出院诊断：1. 恶性肿瘤支持治疗 2. 恶性肿瘤免疫治 出院日期： 2025年12月06日
疗 3. 肺恶性肿瘤（左肺，小细胞癌广泛期）
4. 肥厚型梗阻性心肌病 5. 纵隔淋巴结肿大
6. 肺门淋巴结肿大 7. 锁骨上淋巴结肿大
(双侧) 8. 腋下淋巴结肿大(右) 9. 心功能
III级(NYHA分级) 10. 甲状腺功能减退症
11. 高血压2级（极高危）12. 肺气肿(局
限性) 13. 肺诊断性影像检查的异常所见(肺
结节) 14. 二尖瓣反流(重度) 15. 心包积
液(少量) 16. 肾上腺结节(左侧)
入院时情况（主要症状、体征，有关实验室及器械检查结果）：
患者因“咳嗽1月余”于2025-05-21至河北省人民医院就诊，查胸部CT：左肺下叶占位性病变，恶性不除
外，远端阻塞性肺炎，建议完善实验室检查及增强CT。双侧锁骨窝、右侧腋下、纵隔内及双肺门多发肿大
淋巴结，转移不除外。左侧胸膜结节样增厚，转移不除外。后于2025-05-23行肺穿刺活检术，术后病理回
示：（左肺）穿刺组织：结合免疫组化染色支持小细胞癌。免疫组化染色： CKpan (+)，Vimentin (-)，
CK7 (+)，TTF -1(+)，NapsinA (-)，CK5/6(-)，P40(-)，P63(-)，CgA (+)，Syn (+)，CD56(+)。根据患者病情
于2025-05-28当地医院行依托泊苷+卡铂方案化疗+斯鲁利单抗免疫治疗1周期，过程顺利。于
2025-06-19、2025-07-16开始行依托泊苷+卡铂化疗+斯鲁利单抗免疫治疗2周期，过程顺利。2025-07-27复
查血常规示血小板38×10^9/L。予升血小板治疗后。2025-08-13、2025-09-06、2025-10-08、2025-11-07
行依托泊苷化疗+斯鲁利单抗免疫治疗4周期，期间疗效评价PR。患者为求进一步治疗就诊我科，门诊拟
第 1 页
南京鼓楼医院
南京大学医学院附属鼓楼医院
出院记录
科别（江北）综合肿瘤中心 病区（江北）B7病区床号 姓名 住院号
“肺恶性肿瘤”收住入院。病程中，患者神志清，精神可，食纳睡眠可，二便如常，近期体重未见明显变
化。
诊疗经过：
患者入院完善相关检查：
【检验】
2025.12.03 12:22 甲功三项：*促甲状腺激素 34.210 mIU/L↑，*游离三碘甲状腺原氨酸 2.60 pmol/L↓，
*游离甲状腺素 9.58 pmol/L↓。
2025.12.03 12:22 肺癌六项（江北）：*细胞角蛋白19片段 3.61 ng/mL↑，*神经元特异性烯醇化酶
26.80 ng/mL↑，胃泌素释放肽前体 243.00 pg/mL↑。
2025.12.03 13:33 生化全套，心肌酶：*碱性磷酸酶 46.8 U/L↓，*葡萄糖 6.66 mmol/L↑，*甘油三酯
8.26 mmol/L↑，*总胆固醇 7.14 mmol/L↑，*H-脂蛋白胆固醇 0.90 mmol/L↓，*L-脂蛋白胆固醇 3.51
mmol/L↑，*载脂蛋白AⅠ 0.79 g/L↓，*载脂蛋白B 1.87 g/L↑，*钠 136.1 mmol/L↓，*氯 97.8
mmol/L↓，*α羟丁酸脱氢酶 158 U/L↑，eGFR(CKD-EPI) 77.2 ml/min/1.73m^2↓。
2025.12.03 14:45 血常规：淋巴细胞百分数 19.7 %↓，淋巴细胞绝对值 0.8 ×10^9/L↓，*红细胞计数
3.30 ×10^12/L↓，*血红蛋白量 108 g/L↓，*红细胞压积 31.8 %↓，红细胞体积分布宽度 15.4 %↑，*
血小板计数 112 ×10^9/L↓。
余未见明显异常。
【检查】
2025.12.04 15:19 心电图检查（江北）（检查）常规心电图 检查结论 窦性心律一度房室传导阻滞左前分支
阻滞异常Q波(V1、V2)左心室高电压ST-T改变QTc间期延长
2025.12.04 16:29（江北）PET/CT(检查) PET/CT全身显像 检查结论 1.“左肺癌化疗后复查”；①左下肺
门稍大伴葡萄糖代谢增高灶，内部通行支气管狭窄，结合病史考虑符合小细胞癌表现；②左肺下叶两枚软
组织结节，葡萄糖代谢异常增高；双肺门、纵隔、右侧腋窝多发肿大淋巴结，葡萄糖代谢显著增高；以上
考虑同侧肺内转移、多发淋巴结转移；2.双肺多发小结节，部分为磨玻璃结节，葡萄糖代谢未见增高，建
议胸部CT随诊；双肺散在条索及渗出；左肺下叶节段性肺不张；右肺局限性肺气肿；双侧胸膜增厚；3.左
肾上腺稍低密度结节，葡萄糖代谢未见异常增高，左肾上腺稍增粗，葡萄糖代谢轻度增高，倾向增生伴腺
瘤形成，请比对老片、密切随诊观察；4.腔隙性脑梗死可能；脑萎缩；副鼻窦炎症；甲状腺左右两叶密度
欠均，葡萄糖代谢增高，考虑炎性摄取增高，必要时请结合甲功、颈部超声随诊；5.心影偏大，冠状动脉
及胸部大血管管壁钙化；6.食管中下段管壁似稍增厚，葡萄糖代谢轻度增高，考虑炎性或生理性摄取可
能，必要时内镜检查；十二指肠憩室可能；轻度脂肪肝；肝囊肿；胆囊饱满；7.慢性膀胱炎症可能；盆腔
内钙化结节；8.颈椎生理性曲度变直，脊柱退变；右股骨下段低密度伴内部钙化，葡萄糖代谢不高，考虑
第 2 页
3/4
南京鼓楼医院
南京大学医学院附属鼓楼医院
出院记录
科别（江北）综合肿瘤中心 病区（江北）B7病区床号
姓名 住院号
良性灶如内生软骨瘤可能，随诊；右肩背部皮下稍低密度结节，葡萄糖代谢未见增高，考虑良性灶，随
诊。
【诊疗经过】
患者入院后完善PET-CT复查，病情较前基本相仿，暂无根治性放疗指征。排除禁忌后，患者于2025-12-05
行斯鲁利单抗免疫维持治疗1周期。现本周期静脉治疗已结束，现整体病情稳定，一般情况尚可，准予办理
出院。
出院情况： 好转
伤口愈合：-
ECOG 1分，NRS 0分，神志清，精神可，无贫血貌，全身皮肤巩膜无黄染。胸廓外形正常，无胸壁静脉曲
张。双侧呼吸运动对称，肋间隙：正常，触觉语颤：对称，皮下捻发感：无，双肺叩诊清音，双肺呼吸音
稍粗，两肺未闻及明显干湿啰音。心律齐，心脏各瓣膜区未闻及杂音。腹部平坦，腹部无压痛，无反跳
痛。双下肢无明显水肿。
出院医嘱：
1、注意天气变化，注意休息、低脂饮食，避免受凉，避免手足接触冰冷物体，注意皮肤保暖。
2、出院后继续用药
左甲状腺素钠片（优甲乐）50微克/片 1片 口服 QD（7点）（每天早餐前半小时服用1片，补充甲状腺激
素，内分泌科随诊调药）
3、定期复查血常规（每周1-2次）及生化全套（每周1次），如WBC<3.0×10^9/L、PLT<60×10^9/L或生化
全套指标异常，请及时当地医院就诊（如有急症或危急值报告，请及时就近正规医院急诊就诊），我科门
诊随诊。
4、下次治疗时间：3-4周左右，具体等电话通知。杨阳主任医师专家门诊时间：门诊时间：每周二、周五
上午，（周二本部，周五江北），（江北肿瘤科医生办公室电话：025-83106666转220717）。如需肿瘤日
间治疗，请提前一周至杨阳主任医师门诊预约。
5、不适门诊随诊。
不存在尚未回归的病理检查结果。
X光片号：-
CT号： P049684
MRI号：-
病理号：-
上级医师：
医师：
第 3 页
---
河北省人民医院
病理检查报告单
病理号
姓名:
性别: 女
年龄: 74岁
送检单位: 本院
科别: 胸外二科病区
住院号
床号:
送检日期: 2025-05-23 16:44
送检材料: 左肺穿刺数条:
临床诊断: 左肺占位
图像:
大体检查:
(左肺穿刺数条:)穿刺组织3条, 长共3cm, 直径0.1cm。
病理诊断:
(左肺)穿刺组织: 浸润性癌, 类型待免疫组化助诊。
诊断医师:
郑国卿 王彤彤
日期: 2025-05-26 14:23
注:1.此报告仅供临床医师参考, 如有异议请在两日内与诊断医师联系。 电话: (0311)85988183
2.国家规定小标本(咬检及穿刺组织)3个工作日内出报告; 其余标本5个工作日内出报告(特殊处理标本除外)。
---
住院病历
河北省人民医院
病理检查补充报告单
病理号:
姓名:
性别: 女
年龄: 74岁
送检单位: 本院
科别: 胸外二科病区
住院号:
床号:
送检日期: 2025-05-23 16:44
送检材料: 左肺穿刺数条:
临床诊断: 左肺占位
补充病理诊断:
(左肺)穿刺组织: 结合免疫组化染色支持小细胞癌。
免疫组化染色: CKpan (+), Vimentin (-), CK7 (+), TTF-1 (+), NapsinA (-), CK5/6
(-), P40 (-), P63 (-), CgA (+), Syn (+), CD56 (+), Ki-67 (90%+)。
诊断医师: 康林 郑国娜
报告日期: 2025-05-27 16:
注: 此报告仅供临床医师参考, 如有异议或病情有新变化务请及时与病理诊断医师联系(电话: 85988409)
---
南京鼓楼医院云胶片
南京鼓楼医院
南京大学医学院附属鼓楼医院
影像检查诊断报告
互联网医院
电子影像
检查号:
患者类型: 住院
患者编号:
姓名:
性别: 女
年龄: 75岁
科别: (江北)综合肿瘤中心 病区: (江北)B7病区
病床:
检查日期: 2026-03-11 13:39:06
设备类型: CT
技师: 王雨晓
检查项目: [CT平扫+增强(颈部、胸部、上腹部、下腹部、盆腔)]
检查所见:
颈部软组织CT平扫+增强:
【所见咽部】所见咽腔结构对称,未见明显异常密度影。增强后未见明显异常强化。
【喉部及下咽部】喉腔结构对称,会厌、声带、梨状窝形态及密度未见明显异常。增强后未见
明显异常强化。
【甲状腺及甲状旁腺区】甲状腺左右叶大小、形态正常,甲状腺双叶低密度结节;甲状旁腺区
未见明显占位性病变。
【唾液腺】双侧腮腺、颌下腺形态密度未见明显异常。增强后未见明显异常强化。
【气管及食管】气管居中,管腔通畅;食管颈段管壁未见明显增厚。
【颈部间隙】脂肪间隙清晰,未见明显异常密度影。增强后未见明显异常强化。
【淋巴结】两侧锁骨上窝多发肿大淋巴结。
【其他】副鼻窦内低密度影。
胸部CT平扫+增强:
【肺野】两肺野纹理清晰,左肺下叶见斑片状高密度影。右肺上叶舌段小片状高密度影。两肺
多发结节,较大者:右肺上叶(Img79)见一实性结节影,大小约5mm×3mm。两肺索条及片絮影;右
肺上叶局部透亮区。
【肺门】双肺门多发肿大淋巴结,大者位于左侧,短径约20mm,增强后强化不均。
【气管及支气管】左下肺支气管闭塞伴阻塞性炎症,病灶周围结节影。
【纵隔】纵隔居中,纵隔内多发肿大淋巴结,较大者短径约20mm。
【心脏及大血管】心影增大;主动脉及冠状动脉壁见致密影。
【胸膜及胸腔】胸膜:两侧胸膜可见增厚;胸腔积液:否。增强后未见明显异常强化。
【膈肌】光整,未见明显异常抬高。增强后未见明显异常强化。
【胸壁】胸廓对称,骨质未见明显异常。增强后未见明显异常强化。
上腹部、下腹部、盆腔CT平扫+增强:
报告日期: 2026-03-11 15:35:37
诊断医师: 申欣怡
/ 申欣怡
审核日期: 2026-03-12 13:17:06
审核医师: 王国
（本报告仅供临床医生参考）
---
南京鼓楼医院云胶片
女/75岁
设备类型 CT 患者类型 无
检查项目 [CT平扫+增强（颈部、胸部、上腹部、下
腹部、盆腔）]
PDF报告 图像 分享
报告 2025-10-08
影像描述
颈部软组织CT平扫+增强：
【所见咽部】所见咽腔结构对称，未见明显异常
密度影。增强后未见明显异常强化。
【喉部及下咽部】喉腔结构对称，会厌、声带、
梨状窝形态及密度未见明显异常。增强后未见明显
异常强化。
【甲状腺及甲状旁腺区】甲状腺左右叶大小、形
态正常，甲状腺双叶低密度结节；甲状旁腺区未见
明显占位性病变。
【唾液腺】双侧腮腺、颌下腺形态密度未见明显
异常。增强后未见明显异常强化。
【气管及食管】气管居中，管腔通畅；食管颈段
管壁未见明显增厚。
【颈部间隙】脂肪间隙清晰，未见明显异常密度
影。增强后未见明显异常强化。
【淋巴结】未见明显肿大淋巴结。
【其他】副鼻窦内低密度影。
胸部CT平扫+增强：
【肺野】两肺野纹理清晰，左肺下叶见斑片状高
移动影像浏览
© 2022 南京鼓楼医院影像云平台 V1.0
南京鼓楼医院云胶片
女/75岁
设备类型 CT 患者类型 无
检查项目 [CT平扫+增强（颈部、胸部、上腹部、下
腹部、盆腔）]
PDF报告 图像 分享
【肺野】两肺野纹理清晰，左肺下叶见斑片状高
密度影。两肺多发结节，较大者：右肺上叶（Img7
9）见一实性结节影，大小约5mm×3mm。两肺索
条及片絮影；右肺上叶局部透亮区。
【肺门】双肺门多发小淋巴结，部分稍大。
【气管及支气管】左下肺支气管闭塞伴阻塞性炎
症，病灶周围结节影。
【纵隔】纵隔居中，纵隔内多发小淋巴结，部分
稍大，较大者短径约10mm。
【心脏及大血管】心影增大；主动脉及冠状动
脉壁见致密影。
【胸膜及胸腔】胸膜：两侧胸膜可见增厚；胸腔
积液：否。增强后未见明显异常强化。
【膈肌】光整，未见明显异常抬高。增强后未见
明显异常强化。
【胸壁】胸廓对称，骨质未见明显异常。增强后
未见明显异常强化。
上腹部CT平扫+增强：
【肝脏】各叶比例在正常范围内，外形轮廓规
则，肝内小圆形无强化低密度影，较大者长径约6
mm。静脉期肝左叶小片状稍低密度影（薄层im29
0）。
【胆囊及胆管】胆囊形态、大小正常，囊壁未见
移动影像浏览
© 2022 南京鼓楼医院影像云平台 V1.0
南京鼓楼医院云胶片
女/75岁
设备类型 CT 患者类型 无
检查项目 [CT平扫+增强（颈部、胸部、上腹部、下
腹部、盆腔）]
PDF报告 图像 分享
【胆囊及胆管】胆囊形态、大小正常，囊壁未见
增厚，囊内未见明显异常密度影；肝内外胆管轻度
扩张。
【胰腺】形态、大小正常，实质内未见明显异常
密度影；胰管未见明显扩张。增强后未见明显异常
强化。
【脾脏】形态、大小正常，实质内未见明显异常
密度影。增强后未见明显异常强化。
【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均
匀，未见明显肿大淋巴结，未见明显渗出及积液。
增强后未见明显异常强化。
下腹部CT平扫+增强：
【肾脏】两侧肾脏大小、形态、位置正常，右肾
窦点状致密影；肾盂肾盏未见明显扩张。增强后未
见明显异常强化。
【肾上腺】双肾上腺增粗，左肾上腺低密度结
节，长径约12mm,可见强化。
【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均
匀，未见明显肿大淋巴结，未见明显渗出及积液。
增强后未见明显异常强化。
盆腔CT平扫+增强：
【膀胱】充盈欠佳，壁未见明显增厚，其内未见
明显异常密度影。增强后未见明显异常强化。
【子宫及附件】子宫呈肌组织结构性空扫
移动影像浏览
© 2022 南京鼓楼医院影像云平台 V1.0
南京鼓楼医院云胶片
女/75岁
设备类型 CT 患者类型 无
检查项目 [CT平扫+增强（颈部、胸部、上腹部、下
腹部、盆腔）]
PDF报告 图像 分享
诊断意见
1.肺癌复查：左肺下叶斑片影较前（2025-07-15）
明显缩小，左下肺支气管闭塞伴阻塞性炎症，较前
缓解，密切随诊；双侧纵隔内及双肺门多发稍大淋
巴结，部分较前稍缩小。
2.两肺多发结节，较前变化不大，密切随诊。
3.两侧胸膜增厚；两肺索条及炎性渗出，较前缓
解；右肺上叶局限性肺气肿。
4.心影增大；主动脉及冠状动脉壁钙化。
5.肝脏小囊肿；静脉期肝左叶小片状稍低密度影
（薄层im290），较前相仿，随诊。
6.肝内外胆管轻度扩张。
7.双肾上腺增粗，左肾上腺腺瘤可能，结合专科检
查；右肾小结石。
8.子宫肌瘤可能，结合妇科超声；盆腔内钙化结
节。
9.下腹腔内肠系膜间隙多发稍大淋巴结。
10.食管下段壁轻度增厚；乙状结肠迂曲冗长；结肠
内容物多；十二指肠降部憩室；结合临床体征随
诊。
11.右肩部皮下低密度结节，较前相仿，随诊；L4及
以上椎体I°滑脱。
移动影像浏览
© 2022 南京鼓楼医院影像云平台 V1.0
2026-08-06 10:38:13,540 INFO     30 [SmartSplitter] SmartSplitter done: 38 chunks from 38 LLM segments (all bbox_id). Types: {'ExaminationReport': 5, 'AdmissionRecord': 1, 'DischargeRecord': 1, 'OutpatientRecord': 14, 'PrescriptionRecord': 3, 'LabReport': 14}
2026-08-06 10:38:13,569 INFO     30 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-06 10:38:13,570 INFO     30 [Trace] task=00b9d592 | doc=DAXI-哮喘.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "2328 items", "markdown": "", "text": "", "name": "DAXI-哮喘.pdf", "output_format": "chunks", "chunks": "38 items, types={'ExaminationReport': 5, 'AdmissionRecord': 1, 'DischargeRecord': 1, 'OutpatientRecord': 14, 'PrescriptionRecord': 3, 'LabReport': 14}"}
2026-08-06 10:38:13,570 INFO     30 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-06 10:38:13,576 INFO     30 [ChunkRouter] Routed 38 chunks into 6 groups: {'chunks_Examination': 5, 'chunks_Admission': 1, 'chunks_Discharge': 1, 'chunks_Clinical': 14, 'chunks_Prescription': 3, 'chunks_LabExam': 14}
2026-08-06 10:38:13,605 INFO     30 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-06 10:38:13,606 INFO     30 [Trace] task=00b9d592 | doc=DAXI-哮喘.pdf | ChunkRouter:Router | outputs={"html": "", "json": "2328 items", "markdown": "", "text": "", "name": "DAXI-哮喘.pdf", "output_format": "chunks", "chunks": "38 items, types={'ExaminationReport': 5, 'AdmissionRecord': 1, 'DischargeRecord': 1, 'OutpatientRecord': 14, 'PrescriptionRecord': 3, 'LabReport': 14}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "14 items, types={'OutpatientRecord': 14}", "chunks_Prescription": "3 items, types={'PrescriptionRecord': 3}", "chunks_LabExam": "14 items, types={'LabReport': 14}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 14, \"chunks_Prescription\": 3, \"chunks_LabExam\": 14}"}
2026-08-06 10:38:13,606 INFO     30 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-06 10:38:13,622 INFO     30 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-06 10:38:13,622 INFO     30 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[38]
2026-08-06 10:38:13,622 INFO     30 [qwen-vl-table] positions ： [[38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0]]
2026-08-06 10:38:14,119 INFO     30 [qwen-vl-table] page=38, rect=842x595, img=(2339x1653)
2026-08-06 10:38:14,119 INFO     30 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-06 10:38:14,120 INFO     30 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2070, \"bbox_end\": 2089, \"encounter_dates\": [\"2026-01-06\"], \"department\": \"妇科一病区(门)\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2026-01-06\n\\hline\n英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n\\hline\n{[}WBC{]}白细胞数目 & 4.28 & & & 3.5~9.5 & 10^9/L & {[}HCT{]}红细胞压积 & 37.8 & & & 35~45 & \\% \\\\\n{[}Lym\\%{]}淋巴细胞百分比 & 28.4 & & & 20~50 & \\% & {[}MCV{]}平均红细胞体积 & 80.4 & $\\downarrow$ & & 82~100 & fL \\\\\n{[}Mon\\%{]}单核细胞百分比 & 4.7 & & & 3~10 & \\% & {[}MCH{]}平均红细胞血红蛋白含量 & 26.0 & $\\downarrow$ & & 27~34 & pg \\\\\n{[}Neu\\%{]}中性粒细胞百分比 & 64.4 & & & 40~75 & \\% & {[}MCHC{]}平均红细胞血红蛋白浓度 & 323 & & & 316~354 & g/L \\\\\n{[}Eos\\%{]}嗜酸性细胞百分比 & 2.4 & & & 0.4~8 & \\% & {[}RDW-CV{]}红细胞分布宽度变异系数 & 15.2 & & & 11~16 & \\% \\\\\n{[}Bas\\%{]}嗜碱性细胞百分比 & 0.1 & & & 0.0~1.0 & \\% & {[}RDW-SD{]}红细胞分布宽度标准差 & 43.0 & & & 35.0~56.0 & fL \\\\\n{[}Lym\\#{]}淋巴细胞数目 & 1.22 & & & 1.1~3.2 & 10^9/L & {[}PLT{]}血小板数目 & 224 & & & 125~350 & 10^9/L \\\\\n{[}Mon\\#{]}单核细胞数目 & 0.20 & & & 0.1~0.6 & 10^9/L & {[}MPV{]}平均血小板体积 & 8.0 & & & 6.5~12 & fL \\\\\n{[}Neu\\#{]}中性粒细胞数目 & 2.76 & & & 1.8~6.3 & 10^9/L & {[}PDW{]}血小板分布宽度 & 16.0 & & & 9~17 & fL \\\\\n{[}Eos\\#{]}嗜酸性细胞数目 & 0.10 & & & 0.02~0.52 & 10^9/L & {[}PCT{]}血小板压积 & 0.180 & & & 0.108~ & \\% \\\\\n{[}Bas\\#{]}嗜碱性细胞数目 & 0.00 & & & 0.00~0.06 & 10^9/L & {[}P-LCR{]}大型血小板比率 & 15.8 & & & 11~45 & \\% \\\\\n{[}RBC{]}红细胞数目 & 4.70 & & & 3.8~5.1 & 10^12/L & {[}IG\\%{]}未成熟粒细胞百分比 & 0.4 & & & 0.0~0.6 & \\% \\\\\n{[}HGB{]}血红蛋白 & 122 & & & 115~150 & g/L & {[}IG\\#{]}未成熟粒细胞计数 & 0.02 & & & 0.00~0.06 & 10^9/L \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-06 10:38:14,438 INFO     30 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-06 10:38:14,439 INFO     30 [Trace] task=dfc102e2 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "8 items, types={'LabReport': 2, 'OutpatientRecord': 1, 'DischargeRecord': 1, 'ExaminationReport': 4}", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf", "embedding_token_consumption": 7643}
2026-08-06 10:38:14,439 INFO     30 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-06 10:38:16,649 INFO     30 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-06 10:38:16,649 INFO     30 [Trace] task=dfc102e2 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":8,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-06 10:38:16,661 INFO     30 [DIAG-EXECUTOR] row_position_int len=19 row[0]=(13, 122, 178, 197, 207) row[-1]=(13, 436, 492, 238, 248)
2026-08-06 10:38:16,661 INFO     30 [DIAG-EXECUTOR] row_position_int len=36 row[0]=(14, 256, 303, 111, 116) row[-1]=(14, 256, 292, 395, 400)
2026-08-06 10:38:16,661 INFO     30 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 10:38:16,661 INFO     30 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 10:38:16,661 INFO     30 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 10:38:16,662 INFO     30 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 10:38:16,662 INFO     30 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 10:38:16,662 INFO     30 [DIAG-EXECUTOR] row_position_int is empty
2026-08-06 10:38:16,671 INFO     30 set_progress(dfc102e2918111f18dbe1f8f96f1c395), progress: 0.82, progress_msg: 10:38:16 [DOC Engine]:
Start to index...
2026-08-06 10:38:16,711 INFO     30 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.028s]
2026-08-06 10:38:16,719 INFO     30 set_progress(dfc102e2918111f18dbe1f8f96f1c395), progress: 0.8125, progress_msg: 
2026-08-06 10:38:16,769 INFO     30 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.037s]
2026-08-06 10:38:16,793 INFO     30 set_progress(dfc102e2918111f18dbe1f8f96f1c395), progress: 1.0, progress_msg: 10:38:16 Indexing done (0.11s). Task done (451.19s)
2026-08-06 10:38:16,805 INFO     30 [Done], chunks(8), token(7643), elapsed:451.19
2026-08-06 10:38:17,142 INFO     30 handle_task done for task {"id": "dfc102e2918111f18dbe1f8f96f1c395", "doc_id": "de8a02fc918111f18dbe1f8f96f1c395", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786012241604, "task_type": "dataflow", "root_trace_id": "90f550f6b00248c3845d57a8e0bcf6fb", "root_traceparent": "00-90f550f6b00248c3845d57a8e0bcf6fb-5db7fb7d470dfe0d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
