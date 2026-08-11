# 基准结果：YXHU  62  男  直肠癌肺转移  贵州(2).pdf

## 基本信息

- 文件：`YXHU  62  男  直肠癌肺转移  贵州(2).pdf`
- 大小：5557.9 KB
- PDF 总页数：44
- doc_id：`75fa377494ca11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T22:47:50  完成时间：2026-08-10T23:01:17  耗时：806.7s
- progress_msg：`15:01:14 Indexing done (0.14s). Task done (760.91s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 25b80811 | 1 | 2-2 | 病理诊断报告 病理号: 名: 性 别: 男 年龄: 62岁 收到日期: 2025 |
| 2 | 6a936df4 | 1 | 3-3 | 报告详情 检查 盆腔CT* 姓名 男63岁 检查时间 2026-02-23 11 |
| 3 | 5aee7ff2 | 1 | 4-4 | 报告详情 检查 盆腔CT平扫+增强* 姓名 男63岁 检查时间 2026-02- |
| 4 | 4f5eb823 | 1 | 5-5 | 报告详情 姓名 男63岁 检查时间 2026-02-05 17:02:53 影像 |
| 5 | ebd10e15 | 1 | 6-6 | 报告详情 姓名 男 63岁 检查时间 2026-01-09 11:07:00 影 |
| 6 | 3cff3494 | 1 | 7-7 | 报告详情 姓名 男63岁 检查时间 2026-01-09 09:32:00 影像 |
| 7 | 7862eae5 | 1 | 8-8 | 报告详情 检查 胸部CT平扫+三维重建 姓名 男 63岁 检查时间 2025-0 |
| 8 | a39047de | 3 | 9-11 | 出院记录 姓名： 科室： 住院号： 姓名： 职业：自由职业 性别：男 入院日期： |
| 9 | f74672d2 | 2 | 12-13 | 出院记录 姓名： 科室： 住院号： 姓名： 职业：自由职业 性别：男 入院日期： |
| 10 | eaf50ed2 | 1 | 17-17 | 报告详情 检查 常规心电图 姓名 男 63岁 检查时间 2026-02-05 1 |
| 11 | d61f9629 | 1 | 14-14 | <table><tr><td>白细胞计数</td><td>None</td><t |
| 12 | 8b631616 | 1 | 15-15 | <table><tr><td>谷丙转氨酶</td><td>None</td><t |
| 13 | 1bcfc247 | 1 | 16-16 | <table><tr><td>凝血酶原时间检测</td><td>None</td |
| 14 | c05fd30e | 10 | 0-31 | <table><tr><td>体细胞突变</td><td>None</td><t |
| 15 | e2d7784d | 1 | 16-16 | <table><tr><td>肌红蛋白</td><td>None</td><td |
| 16 | 1100a73e | 1 | 16-16 | <table><tr><td>糖类抗原125</td><td>CA125</td |

- chunks 总数：16
- 各 chunk 页数合计（含跨页重复）：28
- 页码并集：`[0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20, 21, 23, 24, 25, 26, 28, 30, 31]`
- 覆盖页数：26 / 44；缺失页：`[1, 18, 19, 22, 27, 29, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：❌ 未完全覆盖：覆盖 26/44 页，缺失 [1, 18, 19, 22, 27, 29, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]，超范围 []**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 0 | 0 | 0 | encounter_date, chief_complaint, diagnosis | **-** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 2 | 2 | 2 | admission_date, discharge_date, department, outcome | **OK** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 8 | 8 | 8 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 6 | 0 | 6 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"ExaminationReport": 8, "DischargeRecord": 2, "LabReport": 6}`
- ChunkMerger：`{"found": true, "merged": 16, "sources": 9, "stats": {"Extractor:LabExam": 6, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 2, "Extractor:Admission": 1, "Extractor:ExaminationReport": 8, "Extractor:Progress": 1}, "filtered_noise": 6}`
- Extractor skip 证据：22 条
  - `[no_items_extracted] 2026-08-10 14:56:37,516 WARNING  29 [qwen-vl-table] page=20 no items extracted`
  - `[no_items_extracted] 2026-08-10 14:56:51,677 WARNING  29 [qwen-vl-table] page=24 no items extracted`
  - `[no_items_extracted] 2026-08-10 14:56:52,953 WARNING  29 [qwen-vl-table] page=25 no items extracted`
  - `[no_items_extracted] 2026-08-10 14:56:54,256 WARNING  29 [qwen-vl-table] page=26 no items extracted`
  - `[no_items_extracted] 2026-08-10 14:56:55,374 WARNING  29 [qwen-vl-table] page=27 no items extracted`
  - `[no_items_extracted] 2026-08-10 14:56:56,148 WARNING  29 [qwen-vl-table] page=28 no items extracted`
  - `[no_items_extracted] 2026-08-10 14:56:56,781 WARNING  29 [qwen-vl-table] page=29 no items extracted`
  - `[no_items_extracted] 2026-08-10 14:56:57,523 WARNING  29 [qwen-vl-table] page=30 no items extracted`
  - `[no_items_extracted] 2026-08-10 14:56:58,250 WARNING  29 [qwen-vl-table] page=31 no items extracted`
  - `[no_items_extracted] 2026-08-10 14:56:58,878 WARNING  29 [qwen-vl-table] page=32 no items extracted`
  - `[no_items_extracted] 2026-08-10 14:56:59,486 WARNING  29 [qwen-vl-table] page=33 no items extracted`
  - `[no_items_extracted] 2026-08-10 14:57:00,282 WARNING  29 [qwen-vl-table] page=34 no items extracted`
  - `[no_items_extracted] 2026-08-10 14:57:01,073 WARNING  29 [qwen-vl-table] page=35 no items extracted`
  - `[no_items_extracted] 2026-08-10 14:57:01,704 WARNING  29 [qwen-vl-table] page=36 no items extracted`
  - `[no_items_extracted] 2026-08-10 14:57:02,470 WARNING  29 [qwen-vl-table] page=37 no items extracted`
  - `[no_items_extracted] 2026-08-10 14:57:03,255 WARNING  29 [qwen-vl-table] page=38 no items extracted`
  - `[no_items_extracted] 2026-08-10 14:57:03,794 WARNING  29 [qwen-vl-table] page=39 no items extracted`
  - `[no_items_extracted] 2026-08-10 14:57:05,429 WARNING  29 [qwen-vl-table] page=40 no items extracted`
  - `[no_items_extracted] 2026-08-10 14:57:06,150 WARNING  29 [qwen-vl-table] page=41 no items extracted`
  - `[no_items_extracted] 2026-08-10 14:57:06,950 WARNING  29 [qwen-vl-table] page=42 no items extracted`
  - `[no_items_extracted] 2026-08-10 14:57:07,795 WARNING  29 [qwen-vl-table] page=43 no items extracted`
  - `[no_text_noise] 2026-08-10 15:01:12,963 INFO     29 [ChunkMerger] Merged 16 chunks from 9 sources: {'Extractor:LabExam': 6, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Presc`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 14:47:53,177 INFO     29 handle_task begin for task {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 14:47:53,601 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 14:47:53,721 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 14:47:53,736 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 14:47:53,736 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 14:47:53,736 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 14:47:53,744 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 14:47:53,744 INFO     29 ============================================================
2026-08-10 14:47:53,744 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 14:47:53,744 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 14:47:53,744 INFO     29 ============================================================
2026-08-10 14:47:53,744 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 14:47:53,744 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 14:47:53,759 INFO     29 No torch found.
2026-08-10 14:47:55,478 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=44
2026-08-10 14:47:55,520 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=75048, prompt_len=764
2026-08-10 14:47:56,799 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:47:56,799 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 14:47:56,812 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=75048, prompt_len=401
2026-08-10 14:47:58,016 INFO     29 [qwen-vl-parser] text API response (len=148):
["YXHU 62 男 直肠癌肺转移 贵州", "KRAS 基因突变\MWYC 基因扩增\APC 基因突变", "2021 年直肠癌？保肛服用中药", "2025.05-2025.09 奥沙利铂+亚叶酸钙+氟尿嘧啶+贝伐珠单抗 5 周期 26.01pd", "2026.02.07 贝伐珠单抗"]
2026-08-10 14:47:58,016 INFO     29 [qwen-vl-parser] page=1 text: 5 lines (bbox 0-4)
2026-08-10 14:47:58,017 INFO     29 [qwen-vl-parser] page=1 text: 5 sections
2026-08-10 14:47:58,134 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=513587, prompt_len=764
2026-08-10 14:47:58,534 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:47:58.532+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 64, "failed": 0, "current": {"7630dbd094ca11f1bd9827cf206dfa2d": {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:47:59,458 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-08-14"}
```
2026-08-10 14:47:59,459 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=2025-08-14
2026-08-10 14:47:59,476 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=513587, prompt_len=401
2026-08-10 14:48:01,394 INFO     29 [qwen-vl-parser] text API response (len=324):
["病理诊断报告", "病理号:", "名:", "性 别: 男", "年龄: 62岁", "收到日期: 2025-08-1", "医院:", "送检科室:", "送检医生:", "号:", "床 号:", "门诊号:", "临床诊断: 直肠、肛管新生物并狭窄", "肉眼所见:", "直肠、肛管新生物: 灰白色组织多粒, 约0.1-0.2cm, 全。", "镜下所见:", "病理诊断:", "(直肠、肛管新生物) 恶性肿瘤, 建议行免疫组化进一步协助检查。", "报告医", "审核医师", "报告日期: 2025-08-14 11:05:", "须经诊断医师签字方能生效。", "仅反映本次送检样本情况, 若有疑问, 请及时与病理科联系。"]
2026-08-10 14:48:01,395 INFO     29 [qwen-vl-parser] page=2 text: 23 lines (bbox 5-27)
2026-08-10 14:48:01,395 INFO     29 [qwen-vl-parser] page=2 text: 23 sections
2026-08-10 14:48:01,484 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=589160, prompt_len=764
2026-08-10 14:48:02,839 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-02-23"}
```
2026-08-10 14:48:02,839 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=2026-02-23
2026-08-10 14:48:02,854 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=589160, prompt_len=401
2026-08-10 14:48:07,109 INFO     29 [qwen-vl-parser] text API response (len=438):
["3:29", "5G", "5G", "59", "<", "报告详情", "检查", "盆腔CT*", "姓名", "男63岁", "检查时间", "2026-02-23 11:37:59", "影像所见", "对比2026-02-15盆腔CT平扫：阑尾未见增", "粗。直肠下段管壁增厚，浆膜面稍毛糙，直肠", "周围可见肿大淋巴结，较大者大小约", "8mm×5mm。盆腔左份及左侧会阴区见条片状", "低密度影，范围较前缩小，边界不清，其内可", "见引流管影。腹腔未见明显积液及游离气体。", "腹腔及腹膜后未见明显增大淋巴结。腹主动脉", "及双侧髂总动脉壁见斑片状高密度影。腰椎椎", "体边缘变尖。", "诊断意见", "1.直肠下段Ca，累及浆膜面，盆腔多发肿大淋", "巴结，请结合临床及MRI检查。2.盆腔左份及", "左侧会阴区脓肿引流术后，脓肿较前吸收。3.", "前列腺钙化灶。4.腹主动脉及双侧髂总动脉粥", "样硬化。5.腰椎退行性变。"]
2026-08-10 14:48:07,110 INFO     29 [qwen-vl-parser] page=3 text: 28 lines (bbox 28-55)
2026-08-10 14:48:07,110 INFO     29 [qwen-vl-parser] page=3 text: 28 sections
2026-08-10 14:48:07,220 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=763400, prompt_len=764
2026-08-10 14:48:08,629 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-02-08"
}
```
2026-08-10 14:48:08,630 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=2026-02-08
2026-08-10 14:48:08,648 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=763400, prompt_len=401
2026-08-10 14:48:11,907 INFO     29 [qwen-vl-parser] text API response (len=562):
["3:30", "5G", "5G", "59", "<", "报告详情", "检查", "盆腔CT平扫+增强*", "姓名", "男63岁", "检查时间", "2026-02-08 14:55:00", "影像所见", "对比2026-01-09腹部增强：阑尾未见增粗。直", "肠下段管壁增厚，增强扫描不均匀强化，浆膜", "面稍毛糙，周围可见淋巴结显示，较大者大小", "约8mm×5mm。盆腔左份及左侧会阴区见不规", "则团片状密度增高影，局部呈囊性改变，病灶", "边界欠清晰，较大截面大小约", "70mm×34mm×95mm（前后径×左右径×上下", "径），其内见小气泡影，周围脂肪间隙模糊，", "增强病灶边缘轻度强化，病灶与左侧前列腺、", "精囊腺分界欠清晰，前列腺可见结节状高密度", "影。腹腔未见明显积液及游离气体。腹腔及腹", "膜后未见明显增大淋巴结。腹主动脉及双侧髂", "总动脉壁见斑片状高密度影。腰椎椎体边缘变", "尖。", "诊断意见", "1.直肠下段Ca，累及浆膜面，盆腔多发淋巴", "结，请结合临床及MRI检查。2.考虑盆腔左份", "及左侧会阴区脓肿形成，请结合临床并复查。", "3.前列腺钙化灶。4.腹主动脉及双侧髂总动脉", "粥样硬化。5.腰椎退行性变。"]
2026-08-10 14:48:11,908 INFO     29 [qwen-vl-parser] page=4 text: 33 lines (bbox 56-88)
2026-08-10 14:48:11,908 INFO     29 [qwen-vl-parser] page=4 text: 33 sections
2026-08-10 14:48:12,024 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=855394, prompt_len=764
2026-08-10 14:48:13,384 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-02-05"
}
```
2026-08-10 14:48:13,385 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=2026-02-05
2026-08-10 14:48:13,395 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=855394, prompt_len=401
2026-08-10 14:48:17,402 INFO     29 [qwen-vl-parser] text API response (len=667):
["3:30", "5G", "5G", "59", "<", "报告详情", "姓名", "男63岁", "检查时间", "2026-02-05 17:02:53", "影像所见", "对比2026-01-09胸部CT平扫：双肺透亮度增", "高，可见多发囊状透亮影；左肺上叶舌段可见", "两处肿块影，CT值约37-53Hu，分叶状，边界", "清晰，较前稍扩大，较大者大小约", "45mm×38mm×47mm（上下径×左右径×前后", "径），密度不均，其内见结节状高密度影；左", "肺上叶及双肺下叶可见实性结节，较大者位于", "右肺下叶外基底段（IM216），大小约", "11mm×9mm，略呈分叶状；右肺上叶可见结", "节状高密度灶。气管内斑片状密度增高影此次", "未见显示。双肺下叶近胸膜处见絮状密度增高", "影，肺门影不大。纵隔无明显偏移，其内淋巴", "结不大。心脏大小、形态未见明显异常，心腔", "密度减低，主动脉壁见斑片状高密度影，双侧", "胸腔未见积液。肋骨骨质结构未见异常。胸椎", "椎体边缘变尖。", "诊断意见", "1.肺气肿伴双肺多发肺大疱，请结合肺功能检", "查。2.左肺上叶舌段结节及肿块，具恶性征", "象。3.左肺上叶及双肺下叶实性结节，建议随", "诊；右肺上叶钙化灶。4.双肺下叶坠积效应，", "建议复查。5.气管黏液栓较前未见确切显示。", "6.贫血征象，请结合实验室检查；主动脉粥样", "硬化。7.胸椎退行性变。（第1-4、6、7条较前", "大致相仿）"]
2026-08-10 14:48:17,403 INFO     29 [qwen-vl-parser] page=5 text: 36 lines (bbox 89-124)
2026-08-10 14:48:17,403 INFO     29 [qwen-vl-parser] page=5 text: 36 sections
2026-08-10 14:48:17,526 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=948769, prompt_len=764
2026-08-10 14:48:18,877 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-01-09"
}
```
2026-08-10 14:48:18,878 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=2026-01-09
2026-08-10 14:48:18,886 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=948769, prompt_len=401
2026-08-10 14:48:23,052 INFO     29 [qwen-vl-parser] text API response (len=713):
["4:11", "5G", "5G", "29", "<", "报告详情", "姓名", "男 63岁", "检查时间", "2026-01-09 11:07:00", "影像所见", "对比2025-04-14上腹部CT平扫+增强及对比", "2025-04-02下腹部CT平扫+增强：肝脏形", "态、大小未见明显异常；肝内见多枚类圆形低", "密度无强化灶，边界清晰，较大者位于S3，直", "径约13mm；肝内胆管无明显扩张。肝门区结", "构清晰。胆囊不大，壁不厚，腔内未见异常密", "度影。胃、肠管未充盈。胰腺、脾脏及双侧肾", "上腺形态、大小及密度未见明显异常双肾实质", "大小、形态未见异常，双肾可见囊状低密度无", "强化灶，较大者位于左肾，直径约9mm；双侧", "肾盂、肾盏未见扩张。阑尾未见增粗。直肠下", "段管壁增厚，增强扫描不均匀强化，浆膜面稍", "毛糙，周围可见多发淋巴结显示，较大者大小", "约8mm×5mm。前列腺可见结节状高密度影。", "腹腔未见明显积液及游离气体。腹腔及腹膜后", "未见明显增大淋巴结。腹主动脉及双侧髂总动", "脉壁见斑片状高密度影。腰椎椎体边缘变尖。", "诊断意见", "1.直肠下段病变，Ca可能，较前进展，周围多", "发淋巴结，较前稍增多、增大。2.肝内多发囊", "肿。3.双肾周多发渗出，较前已吸收，请结合", "临床。4.双肾多发囊肿。5.考虑升结肠、盲肠", "炎伴周围炎性渗出，较前已吸收。6.前列腺钙", "化灶。7.右侧会阴部积气较前已吸收，请结合", "临床。8.腹主动脉及双侧髂总动脉粥样硬化。", "9.腰椎退行性变。"]
2026-08-10 14:48:23,053 INFO     29 [qwen-vl-parser] page=6 text: 37 lines (bbox 125-161)
2026-08-10 14:48:23,053 INFO     29 [qwen-vl-parser] page=6 text: 37 sections
2026-08-10 14:48:23,173 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=874407, prompt_len=764
2026-08-10 14:48:24,555 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-01-09"
}
```
2026-08-10 14:48:24,556 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=2026-01-09
2026-08-10 14:48:24,573 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=874407, prompt_len=401
2026-08-10 14:48:28,592 INFO     29 [qwen-vl-parser] text API response (len=673):
["4:11", "5G", "5G", "29", "<", "报告详情", "姓名", "男63岁", "检查时间", "2026-01-09 09:32:00", "影像所见", "对比2025-08-11胸部CT平扫：双肺透亮度增", "高，可见多发囊状透亮影；左肺上叶舌段可见", "两处肿块影，CT值约22-61Hu，分叶状，边界", "清晰，较前稍扩大，较大者大小约", "45mm×36mm×42mm（上下径×左右径×前后", "径），密度不均，其内见结节状高密度影；左", "肺上叶及双肺下叶可见实性结节，较大者位于", "右肺下叶，直径约7mm；右肺上叶可见结节状", "高密度灶。新增气管内斑片状密度增高影。双", "肺下叶近胸膜处见絮状密度增高影，肺门影不", "大。纵隔无明显偏移，其内淋巴结不大。心脏", "大小、形态未见明显异常，心腔密度减低，主", "动脉壁见斑片状高密度影，上腔静脉内导管影", "此次未见显示。双侧胸腔未见积液。肋骨骨质", "结构未见异常。胸椎椎体边缘变尖。", "诊断意见", "1.肺气肿伴双肺多发肺大疱，请结合肺功能检", "查。2.左肺上叶舌段结节及肿块，具恶性征", "象，较前增大。3.左肺上叶及双肺下叶实性结", "节，右肺中叶实性结节较前未见确切显示，建", "议随诊；右肺上叶钙化灶。4.新增双肺下叶坠", "积效应，建议复查。5.新增气管黏液栓。6.贫", "血征象，请结合实验室检查；主动脉粥样硬", "化。7.胸椎退行性变。8.PICC管较前未见确切", "显示。"]
2026-08-10 14:48:28,592 INFO     29 [qwen-vl-parser] page=7 text: 36 lines (bbox 162-197)
2026-08-10 14:48:28,592 INFO     29 [qwen-vl-parser] page=7 text: 36 sections
2026-08-10 14:48:28,703 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=791846, prompt_len=764
2026-08-10 14:48:30,058 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2025-06-21"
}
```
2026-08-10 14:48:30,059 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=2025-06-21
2026-08-10 14:48:30,084 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=791846, prompt_len=401
2026-08-10 14:48:30,139 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:48:30.138+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 64, "failed": 0, "current": {"7630dbd094ca11f1bd9827cf206dfa2d": {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:48:33,755 INFO     29 [qwen-vl-parser] text API response (len=615):
["4:19", "5G", "5G", "27", "<", "报告详情", "检查", "胸部CT平扫+三维重建", "姓名", "男 63岁", "检查时间", "2025-06-21 17:57:05", "影像所见", "对比2025-05-26胸部CT平扫：双肺透亮度增高，可见多发囊状透亮影；左肺上叶舌段可见", "两处肿块影，CT值约33-57Hu，分叶状，边界", "清晰，较大者大小约47mm×35mm×43mm", "（上下径×左右径×前后径）；左肺下叶后基底", "段、右肺中叶内侧段、右肺下叶外基底段可见", "实性结节，较大者位于右肺下叶，直径约", "6mm；右肺上叶可见结节状高密度灶。气管内", "斑片状密度增高影未见显示。肺门影不大。纵", "隔无明显偏移，其内淋巴结不大。心脏大小、", "形态未见明显异常，心腔密度减低，主动脉壁", "见斑片状高密度影，上腔静脉内见导管影。双", "侧胸腔未见积液。肋骨骨质结构未见异常。胸", "椎椎体边缘变尖。", "诊断意见", "1.肺气肿伴双肺多发肺大疱，请结合肺功能检", "查。2.左肺上叶舌段肿块，具恶性征象，建议", "复查。3.右肺中叶、双肺下叶实性结节，建议", "随诊；右肺上叶钙化灶。4.贫血征象，请结合", "实验室检查；主动脉粥样硬化。5.胸椎退行性", "变。6.PICC管置入术后。（上述1-5条较前大", "致相仿）"]
2026-08-10 14:48:33,755 INFO     29 [qwen-vl-parser] page=8 text: 34 lines (bbox 198-231)
2026-08-10 14:48:33,755 INFO     29 [qwen-vl-parser] page=8 text: 34 sections
2026-08-10 14:48:33,916 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=972322, prompt_len=764
2026-08-10 14:48:35,186 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:48:35,187 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-10 14:48:35,193 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=972322, prompt_len=401
2026-08-10 14:48:43,894 INFO     29 [qwen-vl-parser] text API response (len=1367):
["出院记录", "姓名：", "科室：", "住院号：", "姓名：", "职业：自由职业", "性别：男", "入院日期：2026-2-5 10:14", "年龄：63岁", "出院日期：2026-2-26 10:25", "民族：汉族", "住院天数：21天", "籍贯：", "科 室：", "入院情况：", "患者男，63岁，因“诊断直肠癌肺转移7+月”入院；既往史：4+年前因“大便不成形伴血", "便”就诊于外院，考虑为“直肠癌”，未明确诊断，自行服用中药治疗；10+月前因“阴囊脓肿”于", "我院局麻下行“阴囊下部脓肿切开引流术”，病理结果回示：“阴囊内容物”检材大部分为变性坏", "死组织，区域见大量中性粒细胞浸润。予换药、抗感染等对症治疗后好转。专科情况：全身皮肤粘", "膜无黄染、出血点及瘀斑，全身浅表淋巴结未扪及肿大，胸廓对称无畸形，肋间隙无明显增宽及凹", "陷，胸骨无压痛，双肺叩诊呈清音，双肺呼吸音粗，双肺可闻及散在湿啰音。腹平软，全腹未见腹", "部静脉曲张、蜘蛛痣，未见胃肠型蠕动波。全腹无压痛、反跳痛及肌紧张，肝脾肋下未扪及，莫菲", "氏征阴性，移动性浊音阴性，双肾区无叩击痛，肠鸣音约4次/分，阴囊及肛周皮肤正常，未见红", "肿、破溃，肛周6点钟方向可扪及一约2*3cm大小包块，质韧，挤压时无明显脓液，肛门括约肌张力", "正常，于直肠距肛门约7cm处可扪及环状肿物，质地硬，表面凹凸不平，活动度差，退出指套可见血", "染。（患者取左侧卧位）辅助检查：病理（病理号：2502456）：“左肺占位”恶性肿瘤，符合腺", "癌，结合免疫组化结果及临床病史考虑肠道来源。ALK（-）、CD56（-）、CDX-2（+）、CK20", "(+）、CK5/6（-）、CK7（局灶弱+）、Ki-67（30%+）、Napsin-A（-）、P40(-)、P53（突变", "型）、P63(-)、SATB2(+)、Syn（-）、TTF-1（+）、CK(AE1/AE3)（+）、Vimentin（-）、Villin", "(+）。基因检测：1.KRAS基因突变；2.MYC基因扩增；3.APC基因突变。胸部CT（本院 2026-01-", "08）：1.肺气肿伴双肺多发肺大疱；2.左肺上叶舌段结节及肿块，具恶性征象，较前增大；3.左肺上", "叶及双肺下叶实性结节，右肺中叶实性结节较前未见确切显示，右肺上叶钙化灶；4.新增双肺下叶", "坠积效应；5.新增气管黏液栓；6.贫血征象，主动脉粥样硬化；7.胸椎退行性变；8.PICC管较前未", "见确切显示。全腹+盆腔增强CT（本院 2026-01-08）：1.直肠下段病变，Ca可能，较前进展，周围", "多发淋巴结，较前稍增多、增大；2.肝内多发囊肿；3.双肾周多发渗出，较前已吸收；4.双肾多发", "囊肿；5.考虑升结肠、盲肠炎伴周围炎性渗出，较前已吸收；6.前列腺钙化灶；7.右侧会阴部积气", "较前已吸收；8.腹主动脉及双侧髂总动脉粥样硬化。9.腰椎退行性变。", "入院诊断：1.直肠腺癌 ycT4bN2M1 IV期（肺转移）；2.肺气肿伴双肺肺大疱；3.混合", "痔；4.肝囊肿；5.双肺结节；6.双肺细菌性肺炎。", "第1页"]
2026-08-10 14:48:43,895 INFO     29 [qwen-vl-parser] page=9 text: 40 lines (bbox 232-271)
2026-08-10 14:48:43,895 INFO     29 [qwen-vl-parser] page=9 text: 40 sections
2026-08-10 14:48:44,066 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1088789, prompt_len=764
2026-08-10 14:48:45,359 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:48:45,360 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=None
2026-08-10 14:48:45,378 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1088789, prompt_len=401
2026-08-10 14:48:52,169 INFO     29 [qwen-vl-parser] text API response (len=1262):
["出院记录", "姓名：", "科室：", "住院号：", "诊疗经过：患者入院后积极完善相关辅助检查，血常规：中性粒细胞绝对值10.57*10^", "9/L，血红蛋白128.00g/L，红细胞比积38.80%，白细胞计数12.28*10^9/L，C反应蛋", "白101.75mg/L。DIC全套：纤维蛋白原检测9.1g/L。大便潜血：阳性。肿瘤标记物：", "癌胚抗原6.84ng/mL，糖类抗原72427.95U/mL。血生化、心肌标记物及心肌酶谱均未", "见明显异常。结合患者病史、体征及相关辅助检查，考虑患者直肠癌肺转移较前进展，", "因患者且合并远处转移，无法行根治性手术切除原发病灶及转移病灶，故建议患者行", "“支气管、肋间、胸廓内外动脉+肠道动脉灌注化疗栓塞术”，提高患者生存周期并改", "善患者生质量，但患者因自身原因拒绝行介入手术治疗，并要求继续使用贝伐珠单抗靶", "向治疗及对症止痛。但因患者目前疗效评估为PD，结合患者原免疫组化，考虑化疗药物", "可能对肿瘤细胞形态及抗原表达产生影响，从而发生免疫组化结果改变，故建议患者再", "次行肠镜检查取病理活检明确免疫组化情况，必要时再次行基因检测指导抗肿瘤药物选", "择。患者及家属拒绝行病理活检，要求暂使用贝伐珠单抗靶向治疗，向患者告知可能因", "免疫组化改变发生耐药，但患者家属仍坚持要求继续使用贝伐珠单抗。后予患者完善盆", "腔MRI平扫，盆腔MRI示：1.直肠下段Ca，累及浆膜面，盆腔多发肿大淋巴结；2.盆腔左", "份脓肿（大小约106×38×29mm）可能；3.骨盆骨质疏松征象。阅片可见患者盆腔左份", "及左侧会阴区见不规则团片状密度增高影，部分呈囊状改变，因病灶范围大与周围临近", "器官组织分界欠清，压迫症状明显，故建议患者行脓肿穿刺置管引流术，缓解压迫症", "状。且阅片可见患者直肠肿瘤较前增大已明显侵犯浆膜面，患者目前已出血肛门坠胀及", "排便困难等症状，考虑为肿瘤进展后体积增大，阻塞肠腔所致，故建议患者可行直肠球", "囊扩张、支架置入或姑息性造瘘术以改善排便困难症状，避免因肠管狭窄出现肠梗阻危", "及生命，向患者及家属交代患者目前病情及后续治疗后，患者及家属表示理解，同意行", "脓肿穿刺引流，但拒绝行直肠球囊扩张、支架置入及姑息性造瘘术，故排除手术禁忌后", "于2026年2月8日在局麻下行“经CT引导下盆腔脓肿穿刺置管引流术”，手术过程顺利，", "术后继予患者抗感染、抑酸护胃等对症支持治疗，后患者肛周皮肤出现破溃流脓，考虑", "为直肠肿瘤进展后肿瘤直接浸润肠壁全层及穿透至肛周组织，导致局部组织坏死流出，", "出现肛周皮肤破溃伴流脓，予患者盐水冲洗创面及加强换药，保持引流通畅，促进创面", "愈合，经治疗患者创面渗出较前已明显减少，但为避免窦道形成，仍建议患者尽快行外", "科手术治疗，患者及家属表示理解，并要求转院行外科手术治疗，请示上级医师后同意", "第2页"]
2026-08-10 14:48:52,170 INFO     29 [qwen-vl-parser] page=10 text: 33 lines (bbox 272-304)
2026-08-10 14:48:52,172 INFO     29 [qwen-vl-parser] page=10 text: 33 sections
2026-08-10 14:48:52,305 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=617177, prompt_len=764
2026-08-10 14:48:55,315 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:48:55,316 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=None
2026-08-10 14:48:55,337 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=617177, prompt_len=401
2026-08-10 14:48:59,808 INFO     29 [qwen-vl-parser] text API response (len=734):
["出院记录", "姓名：", "科室：", "住院号：", "予患者签署自请出院协议后今日出院。", "手术：经CT引导下盐腔脓肿穿刺置管引流术 2026-02-08", "出院情况：患者诉创面渗出较前已明显减少，无恶心、呕吐，无咳嗽、咳痰，无胸痛。", "胸闷、气促、呼吸困难，无腹胀、腹痛，无畏寒、发热等不适，精神、饮食、睡眠尚", "可，小便黄清，大便同前。查体：全身浅表淋巴结未扪及肿大，胸廓对称无畸形，肋间", "隙无明显增宽及凹陷，胸骨无压痛，双肺叩诊呈清音，双肺呼吸音粗，双肺可闻及散在", "湿啰音。腹平软，全腹未见腹部静脉曲张、蜘蛛痣，未见胃肠型蠕动波。全腹无压痛、", "反跳痛及肌紧张，肝脾肋下未扪及，莫菲氏征阴性，移动性浊音阴性，双肾区无叩击", "痛，肠鸣音约4次/分，阴囊皮肤正常，未见红肿、破溃，肛周6点钟方向可见一大小约2", "×1cm不规则皮肤缺损，创面基底呈暗红色可见少量白色脓苔附着，可见少量灰白色恶", "臭味脓性分泌物流出。肛门括约肌张力正常，于直肠距肛门约7cm处可扪及环状肿物，", "质地硬，表面凹凸不平，活动度差，退出指套可见血染。左侧臀部引流管引流通畅，可", "见暗灰色脓性分泌物引出，量约10ml。（患者取左侧卧位）", "出院诊断：1.直肠腺癌 ycT4bN2M1 IV期（肺转移）；2.肺气肿伴双肺肺大疱；3.混合", "痔；4.肝囊肿；5.双肺结节；6.双肺细菌性肺炎；7.轻度贫血；8.盆腔脓肿；9.肛周脓", "肿。", "出院医嘱：院外继续治疗。", "康复指导：嘱患者适当活动，禁忌久卧、久坐，避免深静脉血栓形成", "医生坐诊信息", "医生签名：", "2026-2-26", "第3页"]
2026-08-10 14:48:59,808 INFO     29 [qwen-vl-parser] page=11 text: 26 lines (bbox 305-330)
2026-08-10 14:48:59,808 INFO     29 [qwen-vl-parser] page=11 text: 26 sections
2026-08-10 14:49:00,123 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2029283, prompt_len=764
2026-08-10 14:49:01,574 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:49:01,575 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=None
2026-08-10 14:49:01,594 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2029283, prompt_len=401
2026-08-10 14:49:02,558 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:49:02.557+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 64, "failed": 0, "current": {"7630dbd094ca11f1bd9827cf206dfa2d": {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:49:09,261 INFO     29 [qwen-vl-parser] text API response (len=1406):
["出院记录", "姓名：", "科室：", "住院号：", "姓名：", "职业：自由职业", "性别：男", "入院日期：2025-7-8 09:23", "年龄：62岁", "出院日期：2025-7-14 10:00", "民族：汉族", "住院天数：6天", "籍贯：", "科 室：", "入院情况：", "患者 男，62岁，因“发现左肺占位3+月，诊断肠道肿瘤肺转移2+月”入院；患者3+月前因", "胸闷就诊于我院，行胸部CT提示：左肺上叶舌段周围型肺癌可能性大。后排除手术禁忌后于2025年4", "月16日行“肺穿刺活检”，病理结果提示：“左肺占位”恶性肿瘤，符合腺癌，结合免疫组化结果及", "临床病史考虑肠道来源。P53（突变型）、Syn（-）、TTF-1（+）、P63(-)、CK(AE1/AE3)", "(+)、Vimentin（-）、Villin（+）、CK7（局灶弱+）、CD56（-）、ALK（-）、Napsin-", "A（-）、P40(-)、CDX-2（+）、CK20（+）、Ki-67（30%+）、SATB2(+)、PCK5/6（-）。基因检测：", "1.KRAS基因突变；2.MYC基因扩增；3.APC基因突变。因患者为肠道肿瘤晚期且合并肺转移，可予患者", "行姑息性治疗，提高患者生存期，故排除化疗禁忌后于2025年5月12日至2025年6月22日完成1-3周期", "“FOLFOX+贝伐珠单抗”（奥沙利铂150mg+亚叶酸钙600mg+氟尿嘧啶4500mg+贝伐珠单抗400mg）", "联合治疗，现患者为按计划行下一周期治疗入院，门诊遂以“肠道肿瘤肺转移”收入我科。既往史：", "3+年前因“大便不成形伴血便”就诊于外院，考虑为“直肠癌”，未明确诊断，自行服用中药治疗；", "2+月前因“阴囊脓肿”于我院局麻下行“阴囊下部脓肿切开引流术”，病理结果回示：“阴囊内容", "物”检材大部分为变性坏死组织，区域见大量中性粒细胞浸润。予换药、抗感染等对症治疗后好转。", "专科情况：腹平软，全腹未见腹部静脉曲张、蜘蛛痣，未见胃肠型蠕动波。全腹无压痛、反跳痛及肌", "紧张，肝脾肋下未扪及，莫菲氏征阴性，移动性浊音阴性，双肾区无叩击痛，肠鸣音约4次/分，阴囊", "及肛周皮肤正常，未见红肿、破溃，肛周可扪及一约1*1cm大小包块，质韧，挤压时无明显脓液。辅", "助检查：病理（病理号：2502456）：“左肺占位”恶性肿瘤，符合腺癌，结合免疫组化结果及临床", "病史考虑肠道来源。CD56（-）、CDX-2（+）、CK7（局灶弱+）、ALK（-）、Ki-67（30%", "+）、P63(-)、SATB2(+)、CK20（+）、CK5/6（-）、Napsin-A（-）、P40(-)、P53（突变", "型）、Syn（-）、TTF-1（+）、CK(AE1/AE3)（+）、Vimentin（-）、Villin（+）。基因检测：", "1.KRAS基因突变；2.MYC基因扩增；3.APC基因突变。", "入院诊断：1.姑息性化疗；2.肠道肿瘤肺转移（T4bNxM1 IVa期）；3.肺气肿伴双肺肺大", "疱；4.混合痔；5.肝囊肿；6.双肺结节。", "诊疗经过：患者入院后积极完善相关辅助检查，血常规：中性粒细胞绝对值1.05*10", "第1页"]
2026-08-10 14:49:09,261 INFO     29 [qwen-vl-parser] page=12 text: 40 lines (bbox 331-370)
2026-08-10 14:49:09,261 INFO     29 [qwen-vl-parser] page=12 text: 40 sections
2026-08-10 14:49:10,363 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1063073, prompt_len=764
2026-08-10 14:49:11,642 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:49:11,643 INFO     29 [qwen-vl-parser] page=13 classify=text report_date=None
2026-08-10 14:49:11,661 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1063073, prompt_len=401
2026-08-10 14:49:16,733 INFO     29 [qwen-vl-parser] text API response (len=904):
["出院记录", "姓名：", "科室：", "住院号", "9/L↓，血红蛋白123.00g/L↓，白细胞计数3.16*10^9/L↓。肝肾功、电解质、心肌标", "记物及心肌酶谱均未见明显异常。入院时患者血常规提示白细胞稍低，考虑为化疗后骨", "髓抑制，予患者人粒细胞刺激因子对症治疗后复查血常规未见明显异常。因患者为肠道", "肿瘤晚期且合并肺转移，治疗方式以全身治疗为主的姑息治疗，以延长生命，改善生活", "质量为目的，目前患者已于我科完成3个周期“FOLFOX+贝伐珠单抗”方案治疗，查体可", "见阴囊处皮肤缺损已愈合，肛周肿块较前缩小，行局部疗效评估为PR，后续可继续该方", "案治疗，故排除化疗禁忌后于2025年7月9日至2025年7月13日行第4周期“FOLFOX+贝伐珠", "单抗”（奥沙利铂150mg+亚叶酸钙600mg+氟尿嘧啶4500mg+贝伐珠单抗400mg）方案", "治疗，患者化疗期间出现消化道反应，予止吐、抑酸等对症支持治疗后，消化道症状明", "显好转，复查血常规未见明显骨髓抑制，目前我科已无特殊治疗，请示上级医师后同意", "予患者今日出院。", "手术：无", "出院情况：患者无恶心、呕吐，未诉心慌、胸闷、气促、呼吸困难，无畏寒、发热，无", "腹胀、腹泻等特殊不适；精神、睡眠、饮食尚可，二便如常。查体：生命征平稳，一般", "情况可。心肺腹查体无特殊，专科查体同前。", "出院诊断：1.姑息性化疗；2.肠道肿瘤肺转移（T4bNxM1 IVa期）；3.肺气肿伴双肺肺", "大疱；4.混合痔；5.肝囊肿；6.双肺结节；7.化疗后骨髓抑制。", "出院医嘱：1.注意休息，多饮水，避免剧烈活动，注意加强营养；2.动态监测血常规", "（每周查血常规2次），监测肝功能每周1次，若有异常，及时就诊；3.间隔3周返院按计", "划行下一周期化疗；4.若出现畏寒、发热、乏力、心慌、胸闷等不适立即返院就诊；5.", "耳鼻喉科门诊随诊；6.不适我科随诊。", "康复指导：嘱患者适当活动，禁忌久卧", "医生签名：", "2025-7-14", "第2页"]
2026-08-10 14:49:16,734 INFO     29 [qwen-vl-parser] page=13 text: 29 lines (bbox 371-399)
2026-08-10 14:49:16,734 INFO     29 [qwen-vl-parser] page=13 text: 29 sections
2026-08-10 14:49:16,835 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=546304, prompt_len=764
2026-08-10 14:49:18,171 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2026-02-19"}
```
2026-08-10 14:49:18,171 INFO     29 [qwen-vl-parser] page=14 classify=table report_date=2026-02-19
2026-08-10 14:49:18,186 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=546304, prompt_len=756
2026-08-10 14:49:24,387 INFO     29 [qwen-vl-parser] table API response (len=1206):
\begin{tabular}{llll}
\hline
项目 & 结果 & 参考范围 & \\
\hline
白细胞计数 & 9.23 & 3.90-9.50/10~9/L & \\
中性粒细胞百分率 & 70.50 & 40.00-75.00/\% & \\
淋巴细胞百分率 & 18.60 $\downarrow$ & 20.00-50.00/\% & \\
单核细胞百分率 & 6.90 & 3.00-10.00/\% & \\
嗜酸性粒细胞百分率 & 3.30 & 0.40-8.00/\% & \\
嗜碱性粒细胞百分率 & 0.70 $\uparrow$ & 0.02-0.52/\% & \\
大的未染色细胞计数 & 0.03 & 0.00-0.40/10~9/L & \\
中性粒细胞绝对值 & 6.51 $\uparrow$ & 1.80-6.30/10~9/L & \\
淋巴细胞绝对值 & 1.72 & 1.10-3.20/10~9/L & \\
单核细胞绝对值 & 0.64 $\uparrow$ & 0.10-0.60/10~9/L & \\
嗜酸性粒细胞绝对值 & 0.30 & 0.02-0.52/10~9/L & \\
\hline
\end{tabular}

\begin{tabular}{llll}
\hline
项目 & 结果 & 参考范围 & \\
\hline
嗜碱性粒细胞绝对值 & 0.06 & 0.02-0.06/10~9/L & \\
大的未染色细胞百分率 & 0.30 & 0.00-4.00/\% & \\
红细胞计数 & 4.34 & 4.30-5.80/10~12/L & \\
血红蛋白 & 125.00 $\downarrow$ & 130.00-175.00/g/L & \\
红细胞比积 & 38.60 $\downarrow$ & 40.00-50.00/\% & \\
红细胞平均体积 & 88.90 & 82.00-100.00/fl & \\
红细胞平均血红蛋白量 & 28.70 & 27.00-34.00/pg & \\
红细胞平均血红蛋白浓度 & 324.00 & 316.00-354.00/g/L & \\
红细胞体积分布宽度变异系数 & 14.30 & 12.00-16.00/\% & \\
红细胞体积分布宽度标准差 & 44.90 & 35.00-56.00/fl & \\
血小板计数 & 458.00 $\uparrow$ & 125.00-350.00/10~9/L & \\
血小板平均体积 & 7.10 $\downarrow$ & 8.30-17.40/fl & \\
C反应蛋白 & 18.29 $\uparrow$ & 0.00-10.00/mg/L & \\
\hline
\end{tabular}
2026-08-10 14:49:24,390 INFO     29 [qwen-vl-parser] page=14 table: 38 LaTeX lines (bbox 400-437)
2026-08-10 14:49:24,390 INFO     29 [qwen-vl-parser] page=14 table: 38 sections
2026-08-10 14:49:24,483 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=485987, prompt_len=764
2026-08-10 14:49:25,933 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-02-05"
}
```
2026-08-10 14:49:25,933 INFO     29 [qwen-vl-parser] page=15 classify=table report_date=2026-02-05
2026-08-10 14:49:25,945 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=485987, prompt_len=756
2026-08-10 14:49:32,101 INFO     29 [qwen-vl-parser] table API response (len=1143):
\begin{tabular}{lll}
\hline
检查日期 & 2026-02-05 11:52:00 & \\
\hline
\multicolumn{3}{l}{\textbf{指标结果}} \\
项目 & 结果 & 参考范围 \\
谷丙转氨酶 & 15.40 & 9.00-60.00/U/L \\
谷草转氨酶 & 18.50 & 15.00-45.00/U/L \\
谷草/谷丙 & 1.20 & 0.80-1.40 \\
总胆红素 & 11.90 & 3.40-17.10/μmol/L \\
直接胆红素 & 5.00 \text{↑} & 0.00-4.00/μmol/L \\
间接胆红素 & 6.90 & 3.00-17.00/μmol/L \\
总蛋白 & 69.800 & 65.000-80.000/g/L \\
白蛋白 & 40.50 & 40.00-55.00/g/L \\
碱性磷酸酶 & 87.00 & 45.00-125.00/U/L \\
γ-谷氨酰基转移酶 & 32.00 & 10.00-60.00/U/L \\
总胆汁酸 & 6.47 & 0.00-9.67/μmol/L \\
尿素 & 5.40 & 3.00-9.20/mmol/L \\
肌酐 & 96.00 & 59.00-104.00/μmol/L \\
\hline
\end{tabular}

\begin{tabular}{lll}
\hline
肌酐 & 96.00 & 59.00-104.00/μmol/L \\
尿素/肌酐 & 0.06 & 0.03-0.20 \\
尿酸 & 248.00 & 208.00-428.00/μmol/L \\
葡萄糖 & 7.28 \text{↑} & 3.90-6.10/mmol/L \\
钾 & 3.92 & 3.50-5.50/mmol/L \\
钠 & 141.60 & 135.00-145.00/mmol/L \\
氯 & 102.90 & 96.00-108.00/mmol/L \\
钙 & 2.22 & 2.10-2.60/mmol/L \\
镁 & 0.85 & 0.73-1.35/mmol/L \\
磷 & 0.98 & 0.78-1.65/mmol/L \\
前白蛋白 & 110.00 \text{↓} & 200.00-400.00/mg/L \\
胆碱酯酶 & 5602.00 & 4600.00-11500.00/U/L \\
白蛋白/球蛋白 & 1.38 & 1.20-2.40 \\
球蛋白 & 29.30 & 20.00-40.00/g/L \\
\hline
\end{tabular}
2026-08-10 14:49:32,103 INFO     29 [qwen-vl-parser] page=15 table: 41 LaTeX lines (bbox 438-478)
2026-08-10 14:49:32,103 INFO     29 [qwen-vl-parser] page=15 table: 41 sections
2026-08-10 14:49:32,196 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=597410, prompt_len=764
2026-08-10 14:49:33,340 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:49:33.338+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 64, "failed": 0, "current": {"7630dbd094ca11f1bd9827cf206dfa2d": {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:49:33,681 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-02-05"
}
```
2026-08-10 14:49:33,682 INFO     29 [qwen-vl-parser] page=16 classify=table report_date=2026-02-05
2026-08-10 14:49:33,707 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=597410, prompt_len=756
2026-08-10 14:49:39,292 INFO     29 [qwen-vl-parser] table API response (len=1108):
\begin{tabular}{l c c}
\hline
项目 & 结果 & 参考范围 \\
\hline
凝血酶原时间检测. & 13.3 & 9.8-14.3/s \\
活动度. & 86.4 & 70.0-150.0/\% \\
国际标准化比值. & 1.2 & 0.5-1.5 \\
活化部分凝血活酶时间检测. & 30.0 & 20.0-36.9/S \\
纤维蛋白原检测. & 9.1 $\uparrow$ & 2.0-4.0/g/L \\
凝血酶时间检测. & 16.8 & 14.4-23.4/s \\
D-D二聚体检测. & 0.6 & 0.0-0.6/ug/ml \\
纤维蛋白（原）降解产物检测. & 4.5 & 0.0-5.0/ug/ml \\
\hline
\end{tabular}

\begin{tabular}{l c c}
\hline
项目 & 结果 & 参考范围 \\
\hline
糖类抗原125 & 6.46 & 0.00-24.00/U/ml \\
糖类抗原199 & 8.34 & 0.00-30.00/U/ml \\
糖类抗原153 & 11.70 & 0.00-24.00/U/ml \\
糖类抗原724 & 8.43 $\uparrow$ & 0.00-6.90/U/ml \\
糖类抗原242 & 8.77 & 0.00-20.00/U/ml \\
总前列腺特异性抗原 & 1.12 & 0.00-4.00/ng/ml \\
FPSA/TPSA & 16.96 $\downarrow$ & 25.00-100.00/\% \\
神经元特异性烯醇化酶 & 12.00 & 0.00-17.00/ng/ml \\
细胞角蛋白19片段 & 4.07 $\uparrow$ & 0.00-3.30/ng/ml \\
鳞状细胞癌抗原 & 1.66 & 0.50-3.00/ng/ml \\
甲胎蛋白 & 4.18 & 0.00-7.00/ng/mL \\
癌胚抗原 & 5.27 $\uparrow$ & 0.00-5.00/ng/mL \\
铁蛋白 & 47.50 & 30.00-400.00/ng/ml \\
\hline
\end{tabular}

\begin{tabular}{l c c}
\hline
项目 & 结果 & 参考范围 \\
\hline
肌红蛋白 & 28.530 & 28.000-72.000/ng/ml \\
高敏肌钙蛋白T & 0.012 & 0.000-0.014/ng/ml \\
\hline
\end{tabular}
2026-08-10 14:49:39,295 INFO     29 [qwen-vl-parser] page=16 table: 44 LaTeX lines (bbox 479-522)
2026-08-10 14:49:39,295 INFO     29 [qwen-vl-parser] page=16 table: 44 sections
2026-08-10 14:49:39,350 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=116412, prompt_len=764
2026-08-10 14:49:42,267 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-02-05"}
```
2026-08-10 14:49:42,267 INFO     29 [qwen-vl-parser] page=17 classify=text report_date=2026-02-05
2026-08-10 14:49:42,281 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=116412, prompt_len=401
2026-08-10 14:49:43,211 INFO     29 [qwen-vl-parser] text API response (len=143):
["3:34", "5G", "5G", "58", "<", "报告详情", "检查", "常规心电图", "姓名", "男 63岁", "检查时间", "2026-02-05 11:17:16", "诊断意见", "1.窦性心律2.正常范围心电图", "报告文件", "预览 >"]
2026-08-10 14:49:43,212 INFO     29 [qwen-vl-parser] page=17 text: 16 lines (bbox 523-538)
2026-08-10 14:49:43,212 INFO     29 [qwen-vl-parser] page=17 text: 16 sections
2026-08-10 14:49:43,274 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=228548, prompt_len=764
2026-08-10 14:49:44,660 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2025-05-05"
}
```
2026-08-10 14:49:44,661 INFO     29 [qwen-vl-parser] page=18 classify=text report_date=2025-05-05
2026-08-10 14:49:44,679 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=228548, prompt_len=401
2026-08-10 14:49:47,207 INFO     29 [qwen-vl-parser] text API response (len=495):
["基因检测报告单", "姓名", "年龄：62", "性别：男", "样本编号", "样本类型：白片", "送检医生：", "接收日期：2025-04-30", "报告日期：2025-05-05", "临床诊断：肠癌肺转移", "检测技术：NGS", "备注：", "项目名称：", "本次检测概览", "检测内容", "本产品包含40个与结直肠癌发生、发展相关的基因，其中涵盖NCCN指南中的KRAS、BRAF、NRAS、ERBB2等重要基", "因，以及MLH1、MSH2、MSH6、PMS2、POLE等与PD-1/PD-L1免疫治疗相关基因，同时，还涵盖与化疗药物毒副作用、疗效相关基因。在采用二代测序技术对这些基因进行深度测序后，根据检出的基因状态，为患者的个体化临床治疗方案", "制定提供可靠的参考依据。", "小结", "体细胞突变", "2", "拷贝数变异", "1", "融合变异", "未检出", "微卫星不稳定状态（MSI）", "微卫星稳定（MSS）", "错配修复基因胚系突变（MMR）", "未检出", "化疗药物", "详情见化疗位点及相关药物反应结果"]
2026-08-10 14:49:47,208 INFO     29 [qwen-vl-parser] page=18 text: 31 lines (bbox 539-569)
2026-08-10 14:49:47,209 INFO     29 [qwen-vl-parser] page=18 text: 31 sections
2026-08-10 14:49:47,286 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=494166, prompt_len=764
2026-08-10 14:49:48,563 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 14:49:48,563 INFO     29 [qwen-vl-parser] page=19 classify=text report_date=None
2026-08-10 14:49:48,581 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=494166, prompt_len=401
2026-08-10 14:49:55,000 INFO     29 [qwen-vl-parser] text API response (len=1338):
["用药相关基因变异及其临床意义", "变异", "提示敏感", "提示耐药", "潜在获益的药物", "变异分类", "KRAS", "2 号外显子", "错义突变", "c.34G>A", "p.G12S", "丰度 = 41.62%", "-", "Panitumumab (A 级)", "Tucatinib + 曲妥珠单抗 (A 级)", "西妥昔单抗 (A 级)", "Cobimetinib (D 级 实体瘤; C 级 朗格汉斯细胞组织细胞增多症、埃尔德海姆-", "切斯特病、罗-道病)", "曲美替尼 (D 级 实体瘤; C 级 朗格汉斯细胞组织细胞增多症、埃尔德海姆-切斯特病、罗-道病)", "Binimetinib (D 级 实体瘤)", "RMC-6236 (D 级 实体瘤)", "I 类", "MYC", "拷贝数扩增", "CN=3.42", "-", "-", "Benzosertib (C 级 实体瘤)", "BMS-986158 (D 级 实体瘤)", "II 类", "注:", "1. 药物分级依据参考《二代测序临床报告解读指引》以及 2017 年 AMP/ASCO/CAP 联合制定的体细胞变异解读指南:", "A 级, 美国食品药品监督管理局 (Food and Drug Administration, FDA) , 以及中国国家药品监督管理局 (National Medical Products", "Administration, NMPA) 批准或 NCCN、CSCO、ASCO、ESMO 等专业临床指南推荐;", "B 级, 经具有足够统计学效能的临床研究证实、获得该领域专家共识;", "C 级, 其他癌种中的 A 级证据 (跨适应证用药) 、或已作为临床试验的入组标准;", "D 级, 临床病例报道或临床前证据支持。", "2. 提示敏感的药物来源于 NMPA/FDA 批准或肿瘤临床指南, 以及临床专家达成共识的较大规模临床研究结果 (A 级, B 级) 。", "3. 提示耐药的药物来源于该肿瘤类型 NMPA/FDA 批准或肿瘤临床指南, 及相关文献或临床试验报道。", "4. 潜在获益的药物来源于该肿瘤类型相关文献或临床试验报道, 以及在其他肿瘤类型中已获批的药物 (C 级, D 级) 。", "5. 报告中相同分级药物间先后顺序与优先推荐无关, 按首字母排序列出。", "6. 按照变异的治疗、预后和诊断等临床意义, 体细胞变异分类为: I 类 (A 级、B 级证据) , II 类 (C 级、D 级证据) , III 类 (临床意义未明的变异) , IV 类 (可能无害或无害的变异, 本报告中不予列出) ; 胚系变异分类为: 致病性, 可能致病性, 意义未明, 可能良性 (本报告中不予列出) , 良性 (本报告中不予列出) 。", "NCCN 指南推荐相关基因变异结果", "基因", "变异类型", "变异结果", "丰度", "KRAS", "错义突变", "c.34G>A(p.G12S)", "41.62%", "BRAF", "未检出", "NRAS", "未检出", "注:"]
2026-08-10 14:49:55,000 INFO     29 [qwen-vl-parser] page=19 text: 53 lines (bbox 570-622)
2026-08-10 14:49:55,000 INFO     29 [qwen-vl-parser] page=19 text: 53 sections
2026-08-10 14:49:55,076 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=509704, prompt_len=764
2026-08-10 14:49:56,301 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:49:56,302 INFO     29 [qwen-vl-parser] page=20 classify=text report_date=None
2026-08-10 14:49:56,319 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=509704, prompt_len=401
2026-08-10 14:50:03,631 INFO     29 [qwen-vl-parser] text API response (len=1600):
["1. KRAS、NRAS 和 BRAF 基因的突变与结直肠癌等癌症患者对 EGFR 单抗类药物(西妥昔单抗或帕尼单抗)的耐药有关，但这些基因野生型的患者能从此类药物的治疗中获益。欧洲药监局和美国 FDA 也明确规定了在使用靶向药物西妥昔单抗或帕尼单抗治疗转移性大肠癌前必须检测 KRAS 基因。(NCCN Guideline: Colon (Rectal) Cancer v.1.2023; FDA Druglabel:panitumumab;FDA Druglabel:cetuximab)。", "2. KRAS 基因检测覆盖但不仅限于 G12, G13, Q61, A59, K117, A146 等变异。", "3. BRAF 基因检测覆盖但不仅限于 V600E, G469A/V, G442S, G464V, Y472C, N581S, D594G, L597V/S, K601E 等变异。", "4. NRAS 基因检测覆盖但不仅限于 G12, G13, Q61, A59, A146 等变异。", "其他非用药相关变异", "基因", "外显子", "变异类型", "变异结果", "丰度/基因型", "变异分类", "APC", "16", "移码突变", "c.4257_4263del(p.S1419fs)", "40.08%", "Ⅲ类", "注:", "1. 突变类型：错义突变（missense）、同义突变（synonymous mutation）、非移码插入突变（insertion）、非移码缺失突变（deletion）、移码突变（frameshift）、剪切突变（splice_variant）、起始密码子丢失（start_lost）、无义突变（nonsense）等。", "2. 体细胞突变又称获得性突变，是在生长发育过程中或者环境因素影响下后天获得的突变，通常身上只有部分细胞带有体细胞突变，如癌症组织会出现致病性的突变。此外同义突变因氨基酸不发生改变故未列出。", "3. 胚系变异又称生殖细胞变异，是来源于精子或卵子这些生殖细胞的变异，因此通常身上所有细胞都带有这种变异；这其中绝大多数胚系变异并不致病，构成了人与人之间的遗传多态性，只有少数变异会致病，特别是一些遗传类的疾病。如移码突变、无义突变等，该类可能导致疾病产生的变异结果会在本部分内容中列出。", "微卫星不稳定性（MSI）检测", "本次检测结果", "微卫星稳定（MSS）", "注:", "1. 微卫星不稳定（MSI-H）的患者，可能对 PD-1/PD-L1 等相关免疫疗法敏感。", "2. FDA 已经批准 PD-1 抗体 Keytruda 用于 MSI-H 或者 dMMR 类型的多种实体瘤。", "3. PD-1/PD-L1 抑制剂药物主要有： 可瑞达（Pembrolizumab），欧狄沃（Nivolumab），泰圣奇（Atezolizumab），达伯舒（Sintilimab），百泽安（Tislelizumab），艾瑞卡（Camrelizumab），Imfinzi（Durvalumab），Bavencio（Avelumab）等。", "4. NCCN 指南建议对于 MSI-H 或 MMR 任一蛋白缺失患者，推荐进一步的 MMR 基因胚系突变检测辅助 Lynch 综合征的诊断。", "错配修复基因胚系突变（MMR）", "基因", "变异类型", "变异结果", "基因型", "致病性", "EPCAM", "", "未检出", "", "", "MLH1", "", "未检出", "", "", "MSH2", "", "未检出", "", "", "MSH6", "", "未检出", "", "", "PMS2", "", "未检出", "", "", "注:"]
2026-08-10 14:50:03,632 INFO     29 [qwen-vl-parser] page=20 text: 46 lines (bbox 623-668)
2026-08-10 14:50:03,632 INFO     29 [qwen-vl-parser] page=20 text: 46 sections
2026-08-10 14:50:03,693 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=346649, prompt_len=764
2026-08-10 14:50:04,886 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:50:04,887 INFO     29 [qwen-vl-parser] page=21 classify=text report_date=None
2026-08-10 14:50:04,903 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=346649, prompt_len=401
2026-08-10 14:50:04,973 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:50:04.972+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 64, "failed": 0, "current": {"7630dbd094ca11f1bd9827cf206dfa2d": {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:50:09,945 INFO     29 [qwen-vl-parser] text API response (len=1077):
["奕检医学", "YIJIANMED LABORATORY", "YJ50430012T", "1. 错配修复 (MMR) 基因包含 EPCAM、MLH1、MSH2、MSH6、PMS2 等基因，这些基因突变会导致错配修复基因功能丧失 (dMMR)，如果", "没有发生基因突变，则为正常 (pMMR)。dMMR 导致 MSI-H，但是 MSI-H 的人不一定 dMMR。", "2. 检测 MMR 的必要性如下：(1)辅助临床评判 MSI-H 发生的原因；(2) MMR 基因的胚系突变还与 Lynch 综合征相关，如需进一步判断是否为", "Lynch 综合征还需要结合病史、家族史等具体情况补充其他基因检测进行辅助诊断；(3)预测肿瘤患者能否从抗 PD-1 中获益。", "3. 胚系变异通常会按 ACMG (American College of Medical Genetics and Genomics) 相关指南，分为 “致病性”、“可能致病性”、“意义未", "明”、“可能良性”、“良性”五类。本部分结果只列出“致病性”、“可能致病性”突变。", "基因拷贝数结果", "基因", "染色体位置", "拷贝数变异", "MYC", "chr8", "CN=3.42", "BRAF", "chr7", "未检出", "EGFR", "chr7", "未检出", "ERBB2", "chr17", "未检出", "FGFR1", "chr8", "未检出", "FGFR2", "chr10", "未检出", "FGFR3", "chr4", "未检出", "KRAS", "chr12", "未检出", "MDM2", "chr12", "未检出", "NTRK1", "chr1", "未检出", "PIK3CA", "chr3", "未检出", "注：", "1. 本报告包含以上重要基因的拷贝数变异，但不仅限于以上基因。", "2. 正常细胞的 DNA 可能稀释变异细胞中的 DNA 拷贝数，所以报告中的拷贝数为样本中细胞的平均拷贝数。", "3. 常染色体中基因的正常拷贝数为 2，拷贝数变异为该基因的拷贝数发生改变，CN>2 的拷贝数变异为基因发生扩增，CN<2 的拷贝数变异为基因", "发生缺失。", "融合基因结果", "检测基因", "检测结果", "丰度", "RET", "未检出", "", "NTRK3", "未检出", "", "NTRK2", "未检出", "", "NTRK1", "未检出", ""]
2026-08-10 14:50:09,946 INFO     29 [qwen-vl-parser] page=21 text: 63 lines (bbox 669-731)
2026-08-10 14:50:09,946 INFO     29 [qwen-vl-parser] page=21 text: 63 sections
2026-08-10 14:50:10,023 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=505764, prompt_len=764
2026-08-10 14:50:11,267 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:50:11,267 INFO     29 [qwen-vl-parser] page=22 classify=text report_date=None
2026-08-10 14:50:11,283 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=505764, prompt_len=401
2026-08-10 14:50:18,584 INFO     29 [qwen-vl-parser] text API response (len=1081):
["注：本报告包含以上重要基因的融合变异，但不仅限于以上基因。", "多靶点药物治疗方案", "癌种", "NMPA/FDA/", "指南推荐药物", "治疗方案选择", "药物机制", "使用范围", "结直肠癌", "5-FU + 亚叶酸钙", "+ 贝伐珠单抗", "初始治疗", "化疗+抗血管生成", "晚期/转移性结直肠癌", "FOLFIRI/伊立替康", "+ 贝伐珠单抗（首选）", "初始/后续治疗", "化疗+抗血管生成", "1、无法切除的异时性转移结直肠癌，过去12个月用了FOLFOX/CAPEOX辅助治疗；2、先前接受奥沙利铂治疗而未接受过伊立替康治疗的晚期/转移性结直肠癌；3、先前接受氟尿嘧啶治疗而未接受过伊立替康/奥沙利铂治疗的晚期/转移性结直肠癌", "FOLFOX/CAPEO", "X + 贝伐珠单抗", "后续治疗", "化疗+抗血管生成", "1、先前接受伊立替康治疗而未接受过奥沙利铂治疗的晚期/转移性结直肠癌；2、先前接受氟尿嘧啶治疗而未接受过伊立替康/奥沙利铂治疗的晚期/转移性结直肠癌", "FOLFOX/CAPEO", "X/FOLFIRI/FOLFOXIRI + 贝伐珠单抗", "初始治疗", "化疗+抗血管生成", "晚期/转移性结直肠癌", "伊立替康 + 奥沙利铂 + 贝伐珠单抗", "后续治疗", "化疗+抗血管生成", "先前接受氟尿嘧啶治疗而未接受过伊立替康/奥沙利铂治疗的晚期/转移性结直肠癌", "卡培他滨 + 贝伐珠单抗", "初始治疗", "化疗+抗血管生成", "晚期/转移性结直肠癌", "呋喹替尼", "后续治疗", "抗血管生成", "适用于既往接受过氟尿嘧啶类、奥沙利铂和伊立替康为基础的化疗，以及既往接受过或不适合接受抗 VEGF 治疗、抗EGFR 治疗的 RAS 野生型转移性结直肠癌患者。", "瑞戈非尼", "后续治疗", "抗血管生成", "所有可用方案治疗后进展的晚期/转移性结直肠癌", "(FOLFIRI/伊立替康) + ziv-阿柏西普", "初始/后续治疗", "化疗+抗血管生成", "1、无法切除的异时性转移结直肠癌，过去12个月用了FOLFOX/CAPEOX辅助治疗；2、先前接受奥沙利铂治疗而未接受过伊立替康治疗的晚期/转移性结直肠癌；3、先前接受氟尿嘧啶治疗而未接受过伊立替康/奥沙利铂治疗的晚期/转移性结直肠癌", "(FOLFIRI/伊立替康", "初始/后续治疗", "化疗+抗血管生成", "1、无法切除的异时性转移结直肠癌，过"]
2026-08-10 14:50:18,585 INFO     29 [qwen-vl-parser] page=22 text: 53 lines (bbox 732-784)
2026-08-10 14:50:18,585 INFO     29 [qwen-vl-parser] page=22 text: 53 sections
2026-08-10 14:50:18,659 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=462010, prompt_len=764
2026-08-10 14:50:20,010 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:50:20,011 INFO     29 [qwen-vl-parser] page=23 classify=text report_date=None
2026-08-10 14:50:20,025 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=462010, prompt_len=401
2026-08-10 14:50:25,890 INFO     29 [qwen-vl-parser] text API response (len=1248):
["康）+ 雷莫西尤单", "抗", "去12个月用了FOLFOX/CAPEOX辅助", "治疗；2、先前接受奥沙利铂治疗而未接", "受过伊立替康治疗的晚期/转移性结直", "肠癌；3、先前接受氟尿嘧啶治疗而未接", "受过伊立替康/奥沙利铂治疗的晚期/转", "移性结直肠癌", "注：", "1. 此处内容为 FDA/NMPA 获批，或指南推荐的药物治疗方案。", "2. 该处呈现的治疗方案，旨在为患者的临床治疗提供更多参考信息，但并非该患者的个体化治疗方案。", "3. 治疗方案的选择，请结合患者临床情况参照“使用范围”信息，并遵从临床医师的指导。", "化疗药物相关基因检测结果", "化疗药物", "检测基因", "检测位点", "检测结果", "用药提示", "证据等级", "紫杉醇类", "TP53", "rs1042522", "CG", "药物疗效较好，毒副作用风险较高", "3", "伊立替康", "UGT1A1", "rs8175347", "(TA)6/(TA)7", "毒副作用风险较高", "1A", "rs4148323", "AG", "毒副作用风险较高", "1B", "5-氟尿嘧啶", "DPYD", "rs55886062", "AA", "毒副作用风险低", "1A", "rs67376798", "TT", "毒副作用风险低", "1A", "rs3918290", "CC", "毒副作用风险低", "1A", "卡培他滨", "DPYD", "rs67376798", "TT", "毒副作用风险低", "1A", "rs3918290", "CC", "毒副作用风险低", "1A", "甲氨蝶呤", "MTHFR", "rs1801133", "AG", "毒副作用风险较高", "2A", "注：", "1. 所有检测基因均采用 NCBI-Gene 里的官方命名。", "2. 检测位点均以 rs 号为准：NCBI 里对所有提交的 SNP 进行分类考证后，均会注册一个 rs 号，也称作参考 SNP。", "3. 证据等级的划分：依据 PharmGKB 网站 http://www.pharmgkb.org/page/clinAnnLevels", "Level 1A：注释基于被医学会认可的指南或经某些重大卫生系统的认可；", "Level 1B：注释基于多项有统计显著的研究；", "Level 2A：注释基于多项重复研究，故药效关系很有可能是有意义的；", "Level 2B：注释基于多项重复研究，但某些研究可能无统计显著性或样本数量少；", "Level 3：注释仅基于 1 项有显著差异的研究（未重复）或多项研究但缺乏明显药效关联性。", "4. 影响化疗药物效果的因素较多，如患者临床表现、药物相互作用、给药顺序、剂量差异等，以上检测结果可为化疗药物治疗方案制定提供参考，", "具体用药还请遵循临床指南与医嘱。"]
2026-08-10 14:50:25,891 INFO     29 [qwen-vl-parser] page=23 text: 76 lines (bbox 785-860)
2026-08-10 14:50:25,891 INFO     29 [qwen-vl-parser] page=23 text: 76 sections
2026-08-10 14:50:25,962 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=344823, prompt_len=764
2026-08-10 14:50:27,226 INFO     29 [qwen-vl-parser] classify API response (len=58):
```json
{"type": "table", "report_date": "2025-05-05"}
```
2026-08-10 14:50:27,226 INFO     29 [qwen-vl-parser] page=24 classify=table report_date=2025-05-05
2026-08-10 14:50:27,237 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=344823, prompt_len=756
2026-08-10 14:50:28,680 INFO     29 [qwen-vl-parser] table API response (len=270):
\begin{tabular}{ccc}
\hline
\textbf{质控项目} & \textbf{质控结果} & \textbf{质控标准} \\
\hline
样本量 & 合格 & >30 ng \\
\hline
预文库 & 合格 & >500 ng \\
\hline
靶向捕获 & 合格 & >10 ng \\
\hline
测序质量 & 0.953 & >0.8 \\
\hline
测序深度 & 795.20 & 组织样本$\ge$500X; ctDNA$\ge$5000X \\
\hline
\end{tabular}
2026-08-10 14:50:28,681 INFO     29 [qwen-vl-parser] page=24 table: 16 LaTeX lines (bbox 861-876)
2026-08-10 14:50:28,682 INFO     29 [qwen-vl-parser] page=24 table: 16 sections
2026-08-10 14:50:28,756 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=493293, prompt_len=764
2026-08-10 14:50:30,085 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:50:30,086 INFO     29 [qwen-vl-parser] page=25 classify=text report_date=None
2026-08-10 14:50:30,103 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=493293, prompt_len=401
2026-08-10 14:50:35,313 INFO     29 [qwen-vl-parser] text API response (len=1095):
["奕检医学", "YIJIANMED LABORATORY", "YJ50430012T", "附录", "基因列表", "APC", "DPYD", "FGFR3", "MLH1", "NTRK1", "PTEN", "AKT1", "EGFR", "HRAS", "MSH2", "NTRK2", "RET", "ARID1A", "EPCAM", "KIT", "MSH6", "NTRK3", "SMAD4", "BRAF", "ERBB2", "KRAS", "MTHFR", "PDGFRA", "TP53", "CDH1", "FBXW7", "MAP2K1", "MUTYH", "PIK3CA", "UGT1A1", "CHEK2", "FGFR1", "MDM2", "MYC", "PMS2", "DDR2", "FGFR2", "MDM4", "NRAS", "POLE", "检测方法与技术局限声明", "1. 本检测中点突变与扩增相关基因覆盖了基因全部编码外显子区域，融合基因主要覆盖了常见断裂位点内含子区域，放化疗位点则为 SNP 位点。但由于基因组重复片段与高 GC 区域，导致探针并不能保证 100%（通常大于 98%）覆盖目标区域，存在一定区域探针难以覆盖导致少量罕见位点无法检出。", "2. 本检测是临床诊断与用药决策的有效补充，并不能代替临床其他检测，具体治疗还需医生根据患者其他检测结果与患者病情进展情况做出方案。", "3. 本检测的基因相关解读，主要依据 FDA/NMPA 批准的靶向药物、CSCO、ASCO、NCCN、ESMO 等相关指南，以及相关临床试验与相关临床案例等文献。随着新靶点药物的批准、指南的更新、临床研究的进展，报告内容和相关解读会随相关内容的更新而变化。", "4. 基因点突变、融合基因、拷贝数变异的检出率与肿瘤细胞的含量密切相关，根据 CSCO 肿瘤诊断指南适合于 NGS 检测的组织标本中肿瘤细胞含量建议应达到 20%以上。如果肿瘤细胞占比较低，存在一定未检出的风险，另外 ctDNA 血液样本作为无法取得组织样本的必要补充，建议采血至少 10ml，保证充足的游离 DNA 用于 NGS 检测，如检测结果为阴性，后续如有组织样本，建议进行再次检测。", "5. 未进行白细胞样本对照实验时，无法确认检出变异是否为胚系变异，报告中将以体细胞变异体现。", "— 8 —", "上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com"]
2026-08-10 14:50:35,313 INFO     29 [qwen-vl-parser] page=25 text: 53 lines (bbox 877-929)
2026-08-10 14:50:35,313 INFO     29 [qwen-vl-parser] page=25 text: 53 sections
2026-08-10 14:50:35,424 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=976904, prompt_len=764
2026-08-10 14:50:36,677 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:50:36.676+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 64, "failed": 0, "current": {"7630dbd094ca11f1bd9827cf206dfa2d": {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:50:36,681 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:50:36,682 INFO     29 [qwen-vl-parser] page=26 classify=text report_date=None
2026-08-10 14:50:36,696 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=976904, prompt_len=401
2026-08-10 14:50:51,592 INFO     29 [qwen-vl-parser] text API response (len=2614):
["奕检医学", "YIJIANMED LABORATORY", "YJ50430012T", "变异解析", "变异", "变异解读", "KRAS", "2 号外显子", "错义突变", "c.34G>A", "p.G12S", "丰度 = 41.62%", "I 类", "KRAS 基因第 2 号外显子第 12 位密码子编码的氨基酸由甘氨酸突变为丝氨酸。此变异在 ClinVar 数据库", "中被记录为致病性变异。在 COSMIC 数据库中有 2075 次检出，其中 Large intestine cancer 有 1437", "例，Lung cancer 有 223 例，Pancreas cancer 有 111 例。", "根据 NMPA/FDA 批准、肿瘤临床指南、相关临床研究结果等，该变异对 Panitumumab (A 级)、Tucatinib", "+ 曲妥珠单抗 (A 级) 、西妥昔单抗 (A 级) 等耐药，潜在获益药物为 Cobimetinib (D 级 实体瘤；C", "级 朗格汉斯细胞组织细胞增多症、埃尔德海姆-切斯特病、罗-道病) 、曲美替尼 (D 级 实体瘤；C 级 朗", "格汉斯细胞组织细胞增多症、埃尔德海姆-切斯特病、罗-道病) 、Binimetinib (D 级 实体瘤) 、RMC-6236", "(D 级 实体瘤) 等。", "KRAS 是小型 GTP 酶 RAS 家族的成员,该家族催化 GTP 水解为 GDP。在生理条件下,这些 RAS 蛋白", "在活性(GTP 结合)和非活性(GDP 结合)状态之间循环,以激活受体酪氨酸激酶 (RTK)下游的 MAPK 和", "PI3K 致癌途径信号传导(PMID:22189424)。RAS 酶的功能受鸟嘌 呤核苷酸交换因子(GEF)如 SOS 的", "调节,这些因子可以使 GDP 与 GTP 交换,也可以通过 GTP 酶活化蛋白如 NF1 调节,从而提高 RAS 水", "解 GTP 的能力。一旦被激活,RAS 可通过激活不 同的细胞内信号传导途径(包括 RAF / MEK / ERK 和", "PI3K/AKT/ mTOR 途径)介导细胞增殖和其他细胞功能的调节。KRAS 中的转化突变常见于胰腺癌,结肠", "癌,子宫内膜癌,卵巢癌和胆管癌;几乎所有这些突变都可导致 KRAS 的组成型活化,从而促进细胞增殖", "(PMID:21993244, 24651010)。 KRAS 突变主要发生在三个主要热点 G12,G13 和 Q61 上,前两个发", "生在 GTP-ase 结构域,后者为干扰 NF1 结合和调节 KRAS 的能力(PMID: 22589270, 21993244,", "24651010)。其他不太明确表征的突变如 A146T // P 和 L19F 也已被表征,而且发现较低频率下也可处", "于活化状态(PMID:20147967, 20432530, 20570890)。种系 KRAS 突变可导致 Noonan 综合征(NS)", "和心脏-皮肤-皮肤(CFC)综合征(PMID:16474405, 16474404, 19467855, 17056636),这些疾 病与过度", "活化的 MAPK 途径,独特的临床特征和癌症易感性相关( PMID:19467855,17704260)。", "APC", "16 号外显子", "移码突变", "c.4257_4263del", "p.S1419fs", "丰度 = 40.08%", "III 类", "APC 基因第 16 号外显子发生移码突变。", "APC 是参与 WNT 信号传导的肿瘤抑制基因(PMID: 8259518、8259519)。APC 的主要肿瘤抑制作用是", "调节细胞内β-catenin 水平 (PMID: 11978510)。APC 是破坏复合物的重要成员，该复合物靶向胞质", "β-catenin 泛素化和降解(PMID: 10984057)。当 APC 活性丧失时，WNT 通路活性异常增强，往往导致", "增生，最终导致肿瘤进展(PMID: 8259511)。抑制肿瘤形成需要一个 APC 表达的阈值，并且该水平达到", "了很好的平衡(PMID: 11743581)。APC 基因的胚系突变导致家族腺瘤性息肉病(FAP) (PMID: 1651174,", "1651562)， 95%的患者发展为结直肠癌(PMID: 1528264)。此外，APC 的可遗传变异导致许多相关疾", "病的发生，包括 Turcot 综合征、Gardner 综合征和扁平腺瘤综合征(FAS) (PMID: 8593545)。在 50-80%", "的散发性结直肠癌(PMID: 17143297)中观察到 APC 突变，与 FAS 中的突变很相似。APC 的体细胞突变", "作为肿瘤发生启动事件，在包括乳腺癌、胃癌和前列腺癌在内的许多其他人类癌症中也可观察到(PMID:", "27302369，29316426)。大多数 APC 突变是功能丧失型，主要发生在一个β-catenin 结合的重要区域", "(PMID: 10784639、1338904)。WNT 通路抑制剂目前正在临床研究中(PMID: 24981364)。", "MYC", "拷贝数扩增", "CN=3.42", "II 类", "MYC 的拷贝数扩增变异。", "根据 NMPA/FDA 批准、肿瘤临床指南、相关临床研究结果等，该变异潜在获益药物为 Berzosertib (C", "级 实体瘤) 、BMS-986158 (D 级 实体瘤) 等。", "MYC 编码一个转录因子，该转录因子与蛋白质 MAX 异源二聚化以调控数千个基因的转录，调节参与多", "种细胞过程（包括增殖，分化和凋亡）。 MYC 主要通过基因扩增在多种癌症中被激活。 MYC 通过诱", "导增殖，抑制细胞周期停滞，刺激血管形成和增强基因组不稳定性来促进肿瘤发生 (PMID：", "— 9 —", "上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com"]
2026-08-10 14:50:51,593 INFO     29 [qwen-vl-parser] page=26 text: 65 lines (bbox 930-994)
2026-08-10 14:50:51,593 INFO     29 [qwen-vl-parser] page=26 text: 65 sections
2026-08-10 14:50:51,661 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=315257, prompt_len=764
2026-08-10 14:50:52,972 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:50:52,972 INFO     29 [qwen-vl-parser] page=27 classify=text report_date=None
2026-08-10 14:50:52,980 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=315257, prompt_len=401
2026-08-10 14:50:56,543 INFO     29 [qwen-vl-parser] text API response (len=642):
["奕检医学", "YIJIANMED LABORATORY", "YJ50430012T", "22464321,10378696,16934487,19029958）。 MYC 在癌症中通过多种机制被激活，包括染色体易位", "(通常与血液肿瘤有关，并与组成型过表达有关) 以及基因组扩增和过表达 (PMID: 22446421)。 MYC", "基因发生突变，但频率低于扩增和易位。已知功能性突变位于 T58 残基附近，该残基是 MYC 上的一个", "磷酸化位点，对 MYC 蛋白的泛素化及其降解至关重要 (PMID: 10706881)。 MYC 基因家族由三个", "相关基因组成：（1）c-MYC（在此称为 MYC，由 MYC 基因编码），（2）N-MYC（由 MYCN 基因编", "码）和（3）L-MYC（由基因 MYCL1 编码）(PMID: 16934487)。 MYC 基因位于染色体基因座 8q24", "上，并包含几个不同的结构域，包括一个 N 端转录激活域，一个中央部分和一个 C 端 DNA 结合域，其", "中包含一个基本的螺旋-环-螺旋亮氨酸拉链二级结构域。在这些域中有五个“Myc-boxs”区域，在多个", "物种的 MYC 家族蛋白中高度保守 (PMID: 19029958)。", "—10—", "上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com"]
2026-08-10 14:50:56,543 INFO     29 [qwen-vl-parser] page=27 text: 14 lines (bbox 995-1008)
2026-08-10 14:50:56,543 INFO     29 [qwen-vl-parser] page=27 text: 14 sections
2026-08-10 14:50:56,651 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1051177, prompt_len=764
2026-08-10 14:50:58,127 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:50:58,128 INFO     29 [qwen-vl-parser] page=28 classify=text report_date=None
2026-08-10 14:50:58,137 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1051177, prompt_len=401
2026-08-10 14:51:08,348 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:51:08.347+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 64, "failed": 0, "current": {"7630dbd094ca11f1bd9827cf206dfa2d": {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:51:11,844 INFO     29 [qwen-vl-parser] text API response (len=2638):
["奕检医学", "YIJIANMED LABORATORY", "YJ50430012T", "部分基因简介", "检测基因", "描述", "APC", "APC 编码腺瘤性结肠息肉蛋白,该蛋白是促癌 WNT/β-连环蛋白信号传导通路的负调节因子", "(PMID:8259518,8259519)。APC 的主要肿瘤抑制作用在于其调节细胞内β-连环蛋白水平的能力", "(PMID:11978510)。另外 APC 退出细胞核的能力对其肿瘤抑制功能至关重要(PMID:10984057)。当 APC 的", "活性丧失时,WNT 通路激活异常增加,通常导致增生并最终出现肿瘤进展(PMID:8259511)。有趣的是,抑制肿", "瘤需要 APC 的表达达到一定的阈值,且表达水平也被十分精确的进行调控,因为肿瘤发生需要β-连环蛋白达到", "一定的水平(PMID:11743581)。APC 基因中的突变导致家族性腺瘤性息肉病", "(FAP)(PMID:1651174,1651562),其中 95%的人发展成结直肠癌(PMID:1528264),APC 中的种系突变也导致", "许多相关疾病的发生,包括 Turcot 综合征,加德纳综合征和扁平腺瘤综合征(PMID:8593545)。在 50-80%的", "散发性结肠直肠癌中观察到 APC 突变,就像在 FAS 中发现的突变一样(PMID:17143297),另外在前列腺癌,胃", "癌,皮肤癌,子宫癌,乳腺癌,肺癌,膀胱癌和头颈部癌症中也观察到突变(cBioPortal,MSKCC,2015 年 4 月),大多", "数 APC 突变是截短的,并且大多数 APC 体细胞突变位于蛋白质的突变簇区域(MCR)内,这对于β-连环蛋白结合", "来说是重要的(PMID:10784639,1338904)。", "BRAF", "BRAF 蛋白是在丝裂原活化蛋白激酶(MAPK)级联反应(PMID:15520807)的调节中起关键作用的丝氨酸/苏氨", "酸激酶,其在生理上调节与细胞功能相关的基因的表达,包括增殖等活动(PMID:24202393)。BRAF 的基因改变", "主要见于黑色素瘤和甲状腺癌以及一小部分肺癌和结肠直肠癌中,最常见的 BRAF 点突变是 V600E,它可以调", "节蛋白激酶的活性,从而导致组成型 BRAF 激活,BRAFV600E 可以独立于 RAS 或上游激活而发出单体信号", "(PMID:20179705)。目前已发现其他的 BRAF 突变可以影响蛋白质的二聚化倾向", "(PMID:16858395,26343582,12068308)。这些 BRAF 突变的产物也可以以不受调节的方式激活 MAPK 信", "号传导,并且在某些情况下直接导致肿瘤生长(PMID:15520807)。", "EGFR", "EGFR 编码表皮生长因子受体。EGFR 通过其配体包括表皮生长因子(EGF)和转化生长因子-α(TGF-α)的结合", "激活致癌的 MAPK 和 PI3K/AKT/mTOR 信号级联的下游信号传导途径,最终导致细胞增殖,迁移和分化", "(PMID:18045542)。虽然 EGFR 通常在正常成人组织中以低水平表达,但是在许多癌症类型例如肺癌,脑癌,结", "直肠癌和头颈癌(PMID:10880430)中发现其通过突变和/或扩增使该受体过度激活,而在脑癌和结直肠癌", "中,EGFR 基因的拷贝数增加导致受体过表达(PMID:11426640)。然而,在肺癌中,最普遍的 EGFR 改变是激酶", "结构域中的突变,导致受体的组成性激活(PMID:15329413),但在胰腺癌和结直肠癌中很少发现 EGFR 的激活", "突变(PMID:24827134)。", "ERBB2", "ERBB2(也称 HER2)是受体酪氨酸激酶中表皮生长因子受体(EGFR)家族的成员,在一系列人类癌症(包括乳腺", "癌,胃癌/胃食管癌和子宫内膜癌)中异常扩增和/或过表达(PMID:19536107)。ERBB2/ERBB2 的独特之处在于", "它不直接结合自己的配体。相反,它通过结合(PMID:12620236)增强其他的配体如 EGFR(ERBB1)或 ERBB3", "的活性。事实上,ERBB2 是所有 ERBB 受体同种型(PMID:10220407,9130710)的优选结合配体,ERBB2/ERBB3", "复合物通过激活下游致癌 PI3K 途径(PMID:12853564)显示出高度的有丝分裂活性。或者,ERBB2 可同源二聚", "化并启动细胞内有丝分裂级联,包括 RAS/MAPK,PI3K/AKT/mTOR,SRC 和 STAT 信号传导途径", "(PMID:22785351)。大约 17%至 30%的人类乳腺肿瘤具有 ERBB2 基因扩增,这与患者总体生存率差和肿瘤", "复发的时间相关(PMID:3798106,23000897,9552035,9469329)。扩增的 ERBB2 与 ERBB3 异源二聚化以激", "活 PI3K/AKT/mTOR 信号传导并驱动乳腺癌中的肿瘤发生", "(PMID:12853564,23204226,12124352,18632642)。ERBB2 在约 20%胃或胃食管癌", "(PMID:24943493,21468131)中扩增,并且其过度表达被多种药物(例如曲妥珠单抗,阿托珠单抗,埃克替尼,拉", "帕替尼和培妥珠单抗)靶向(PMID:24799465)。但在非小细胞肺癌,卵巢癌,膀胱癌,子宫颈癌,子宫内膜癌,结肠", "直肠癌,胰腺癌和涎腺癌,软组织肉瘤中及胆管癌中,ERBB2 扩增的发生率很低(PMID:24656976)。最近在包括", "肺腺癌,小叶乳腺癌,膀胱癌,胃癌和子宫内膜癌在内的许多癌症中发现了较低频率的 ERBB2 激活突变,其中细", "胞外和激酶结构域中的反复热点经常出现改变(PMID:23000897,223220880,22908275)。目前有关 ERBB2", "—11—", "上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com"]
2026-08-10 14:51:11,845 INFO     29 [qwen-vl-parser] page=28 text: 53 lines (bbox 1009-1061)
2026-08-10 14:51:11,845 INFO     29 [qwen-vl-parser] page=28 text: 53 sections
2026-08-10 14:51:11,953 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1085191, prompt_len=764
2026-08-10 14:51:13,388 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:51:13,389 INFO     29 [qwen-vl-parser] page=29 classify=text report_date=None
2026-08-10 14:51:13,406 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1085191, prompt_len=401
2026-08-10 14:51:28,547 INFO     29 [qwen-vl-parser] text API response (len=2606):
["奕检医学", "YIJIANMED LABORATORY", "YJ50430012T", "靶向治疗的药物正处于进一步开发中。", "FBXW7 基因编码 SCF(Skp1-Cul1-F-box 蛋白)泛素连接酶复合物识别底物的 F-box 蛋白亚基,在底物鉴定时", "该复合物会修饰底物,使其成为蛋白质降解的靶标。FBXW7 的底物包括蛋白质", "c-MYC,mTOR(PMID:18787170),NOTCH1,cyclin-E 和 JUN,它们在调节细胞分裂,分化和生长中起作用,并且", "在癌症中被不恰当地激活,且由于大多数 FBXW7 底物都是经过 SCF 复合物降解处理的原癌基因,所以 FBXW7", "起着肿瘤抑制剂的作用。突变或拷贝数异常会使 FBXW7 失活并导致癌蛋白的异常积累,随后发生恶性转化", "(PMID:18094723)。此外 FBXW7 中的突变可能对特异性功能如亚基二聚化,蛋白质定位,SCF 组装或底物识", "别产生负面影响。FBXW7 中的大多数突变是破坏底物结合的点突变,而小的缺失突变或插入突变数量则", "<10%(PMID:24853181,17909001)。", "FGFR1 编码成纤维细胞生长因子受体 1,这是一种对有丝分裂和分化过程十分重要的受体酪氨酸激酶。FGFR1", "由三个免疫球蛋白样细胞外结构域组成,其中包含一个跨膜成分和一个通过 MAPK 途径起作用的胞质酪氨酸", "激酶结构域(PMID:8622701)。在与成纤维细胞生长因子配体(主要是 FGF1 和 FGF2)结合后,FGFR1 蛋白迅速", "二聚化并最终内化至细胞核。然而,结合也随组织分布和配体的可用性而变化(PMID:16597617)。FGFR1 在", "组织中广泛表达,并且对于多种功能如胚胎发育,骨骼发生,有丝分裂发生和分化是必需的,而 FGFR1 突变则与", "身体畸形,智力低下和神经缺陷有关(PMID:23812909)。FGFR1 中的扩增或活化突变在包括肺癌,乳腺癌,前列", "腺癌,头颈癌和食道癌在内的多种癌症中发生,但突变频率不同", "(PMID:21160078,0919196,14614009,16807070,12147242)。在转移性肾细胞癌中,FGF 信号传导被怀疑", "是细胞对血管生成逃逸的 VEGF 导向疗法产生获得性耐药的原因(PMID:24387233)。目前,许多 FGFR 蛋白的", "小分子抑制剂正在使用中,其主要的区别在于特异性针对 FGFR 或针对其他受体酪氨酸激酶", "(RTK)(PMID:23696246,24265351)。", "成纤维细胞生长因子受体(FGFR)家族包括 4 种受体酪氨酸激酶(RTK):FGFR1-4。FGFR 的信号发生取决于激", "活酪氨酸激酶结构域的配体依赖性二聚化。由于扩增,突变,易位,选择性剪接或由成纤维细胞生长因子(FGF)", "增加活化而导致的 FGFR 功能失调会促进信号传导,肿瘤发生和细胞迁移(PMID:20094046)。FGFR2 激酶结", "构域突变存在于颅面综合征中,也出现在子宫内膜癌,宫颈癌和鳞状细胞癌中,而 FGFR2 扩增已在大约 10%的", "胃癌患者中发现并与预后不良有关。此外 FGFR2 单核苷酸多态性与 ER 阳性乳腺癌的发展有关,尽管病因尚不", "清楚(PMID:18437204),且成釉细胞瘤中 FGFR2 突变也非常频繁。", "FGFR3 基因编码成纤维细胞生长因子受体 3,这是一种跨膜酪氨酸激酶受体,属于 FGFR 家族(FGFR1-4)。", "FGFR3 蛋白与其同源配体即成纤维细胞生长因子(FGF)的结合会导致受体二聚化,随后激活并调节增殖,分化,", "细胞迁移和凋亡等下游途径(PMID:7542215,20094046)。FGFR3 基因中的可变剪接事件产生两种同种", "型,FGFR3b 和 FGFR3c,其具有独特的组织表达模式和配体结合特异性(PMID:8663044,7512569)。在约 15%", "的多发性骨髓瘤患者中观察到特异性 t(4;14)易位,导致 FGFR3 的组成型表达(PMID:17107900)。此外,在多", "达 70%的膀胱癌中观察到 FGFR3 的激活突变。其中,S249C 突变占所有突变的", "69%(PMID:11395371,12743143,16338952)。", "原癌基因 KIT 编码 3 型跨膜受体酪氨酸激酶,在与其配体干细胞因子(SCF)(也称为肥大细胞生长因子", "(MGF)(PMID:9438854))结合后,受体可通过二聚化和自磷酸化被激活。KIT 活化导致通过几种途径(包括", "PI3K,MAPK 和 STAT)的细胞内信号传导增加,最终导致细胞增殖和存活", "(PMID:17546049,11896121,22089421)。对于患有野生型胃肠间质瘤(GIST;无 KIT 或 PDGFRA 突变)的患", "者,NCCN 建议检测种系琥珀酸脱氢酶(SDH)突变。大约 10-15%的 GIST 是野生型;因此,没有突变并不排除", "GIST 的诊断。在没有 KIT 突变的患者中,具有晚期 GIST 的患者的一部分受益于伊马替尼(0-45%的患", "者)(NCCNSoftTissueSarcomav.2.2017)。KIT 激活突变发生在 80-90%的 GIST 中,分布在不同频率的多个", "外显子上(exon11(66.1%),exon9(13%),exon13(1.2%)和", "exon17(0.6%))(PMID:15365079,17268243,11719439)。至少有八种针对 KIT 的小分子酪氨酸激酶抑制剂", "(TKIs)已被美国食品和药物管理局批准,每种 TKI 的功效取决于激活 KIT 突变的位置", "(PMID:2427414,18955458,19164557)。", "—12—", "上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com"]
2026-08-10 14:51:28,548 INFO     29 [qwen-vl-parser] page=29 text: 49 lines (bbox 1062-1110)
2026-08-10 14:51:28,548 INFO     29 [qwen-vl-parser] page=29 text: 49 sections
2026-08-10 14:51:28,660 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1130929, prompt_len=764
2026-08-10 14:51:29,941 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:51:29,942 INFO     29 [qwen-vl-parser] page=30 classify=text report_date=None
2026-08-10 14:51:29,962 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1130929, prompt_len=401
2026-08-10 14:51:39,958 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:51:39.955+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 64, "failed": 0, "current": {"7630dbd094ca11f1bd9827cf206dfa2d": {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:51:43,686 INFO     29 [qwen-vl-parser] text API response (len=2740):
["奕检医学", "YIJIANMED LABORATORY", "YJ50430012T", "KRAS是小型GTP酶RAS家族的成员,该家族催化GTP水解为GDP。在生理条件下,这些RAS蛋白在活性(GTP", "结合)和非活性(GDP结合)状态之间循环,以激活受体酪氨酸激酶(RTK)下游的MAPK和PI3K致癌途径信号传", "导(PMID:22189424)。RAS酶的功能受鸟嘌呤核苷酸交换因子(GEF)如SOS的调节,这些因子可以使GDP与", "GTP交换,也可以通过GTP酶活化蛋白如NF1调节,从而提高RAS水解GTP的能力。一旦被激活,RAS可通", "过激活不同的细胞内信号传导途径(包括RAF/MEK/ERK和PI3K/AKT/mTOR途径)介导细胞增殖和其他细胞", "功能的调节。KRAS中的转化突变常见于胰腺癌,结肠癌,子宫内膜癌,卵巢癌和胆管癌;几乎所有这些突变都可", "导致KRAS的组成型活化,从而促进细胞增殖(PMID:21993244,24651010)。KRAS突变主要发生在三个主要", "热点G12,G13和Q61上,前两个发生在GTP-ase结构域,后者为干扰NF1结合和调节KRAS的能力", "(PMID:22589270,21993244,24651010)。其他不太明确表征的突变如A146T/V/P和L19F也已被表征,而", "且发现较低频率下也可处于活化状态(PMID:20147967,20432530,20570890)。种系KRAS突变可导致", "Noonan综合征(NS)和心脏-皮肤-皮肤(CFC)综合征(PMID:16474405,16474404,19467855,17056636),这", "些疾病与过度活化的MAPK途径,独特的临床特征和癌症易感性相关(PMID:19467855,17704260)。", "MAP2K1(MEK1)蛋白是一种丝氨酸/苏氨酸激酶,向RAF下游发出信号并激活ERK1/2,因此在MAP激酶", "(MAPK)级联中发挥关键调节作用。MAPK级联反应涉及不同的细胞过程,包括增殖,分化和转录调控,目前已经", "在几种不同的癌症类型中发现级联反应会因为其组分RAS和RAF的遗传突变而产生变化", "MAP2K1", "(PMID:12068308,12509763)。MEK1的突变很少见,但一般发生在携带BRAF或RAS突变的肿瘤类型中,包", "(PMID:22753777)。一些MEK1突变可以赋予细胞对MEK和RAF抑制剂的抗", "括黑色素瘤,结直肠癌和肺癌", "性(PMID:19915144,213383288)。", "MLH1蛋白对于DNA错配修复途径是必不可少的。MLH1与PMS2(最常见),PMS1或MLH3异二聚形成内", "切酶复合物,并切割受损的DNA链,导致其局部切除(PMID:10037723,10542278,10615123)。MLH1中的突", "变导致无法正确修复错配和插入/缺失环,这与微卫星重复序列经常相关,微卫星重复序列的改变可能是特别有", "害的,因为它们可能在其他基因中产生移码突变。MLH1中的突变发生在多种组织类型中,但在散发性结肠癌,", "MLH1", "胃癌和子宫内膜癌的特定子集以及遗传性的犬牙综合征(有时称为遗传性非息肉病性结肠癌(HNPCC))中最常", "见(PMID:8484122,8040889,8261393)。MLH1作为典型的肿瘤抑制基因,由于遗传或体细胞突变导致的一", "个等位基因的功能丧失往往会导致其他等位基因也丧失功能。而在治疗方面,FDA批准了pembrolizumab", "用于治疗错配修复缺陷型(dMMR)和MSI(微卫星不稳定性)肿瘤。", "MSH2(MutS蛋白同系物2)蛋白是参与错配修复的肿瘤抑制因子。MSH2与其他MutS蛋白如MSH6和", "MSH3形成异二聚体,分别形成MutS-α和MutS-β错配修复(MMR)复合物(PMID:8252616,7973733)。两种", "复合物都参与识别错配的碱基对,形成DNA-MutS复合物,该复合物发信号通知MMR机制的其他组分以切除", "异常核苷酸。MSH2和其他MMR基因与遗传性非息肉病性结肠癌(HNPCC),也称为Lynch综合征有关", "MSH2", "(PMID:428275,1648437)。MSH2突变占所有HNPCC病例(PMID:11852992)中的约40%,并且与MSI高", "表型以及MLH1中的突变(PMID:9823339,9354436)相关。尽管最常见于结肠癌,但MSH2突变在许多其他", "癌症类型和综合征中也有报道,包括子宫内膜癌、子宫癌以及皮脂腺肿瘤(PMID:19078925,16826164)。而在", "治疗方面,FDA批准了派姆单抗用于治疗错配修复缺陷型(dMMR)和MSI(微卫星不稳定性)肿瘤。", "MSH6(mutS同系物6)基因编码DNA修复错配蛋白MSH6。MSH6是与MSH2异二聚化形成MutS-α的", "肿瘤抑制剂。该复合物可识别单碱基对错配和二核苷酸插入-删除循环,启动错配修复(MMR)过程", "MSH6", "(PMID:8816473)。MSH6和其他MMR基因与遗传性非息肉病性结肠癌(HNPCC),也称为Lynch综合征有", "关(PMID:428275,1648437)。虽然最常见于结肠癌,但MSH6突变在许多其他癌症类型和综合征(包括子宫内", "膜癌和子宫癌)中也有报道(PMID:19078925,16106253)。而在治疗方面,FDA批准了派姆单抗用于治疗错配", "修复缺陷型(dMMR)和MSI(微卫星不稳定性)肿瘤。", "Ras超家族包含超过150种具有GTP酶活性的小单体蛋白,其基于相似的序列和功能进一步分类为亚家族。", "在Ras亚科内有四个关键成员:K-Ras4a,K-Ras4b,N-Ras和H-Ras。这些蛋白质高度同源,并在所有细胞谱系", "和器官中检测到表达;然而,它们并不完全是多余的。某些成年组织优先表达特异性同种型", "NRAS", "(http://gan.sagepub.com/content/2/3/216.full),并且独特的翻译和修饰将它们分布到不同的亚细胞定位,", "—13—", "上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话:400-004-2111 网址:www.yjmedlab.com"]
2026-08-10 14:51:43,686 INFO     29 [qwen-vl-parser] page=30 text: 55 lines (bbox 1111-1165)
2026-08-10 14:51:43,686 INFO     29 [qwen-vl-parser] page=30 text: 55 sections
2026-08-10 14:51:43,799 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1125928, prompt_len=764
2026-08-10 14:51:45,152 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:51:45,153 INFO     29 [qwen-vl-parser] page=31 classify=text report_date=None
2026-08-10 14:51:45,177 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1125928, prompt_len=401
2026-08-10 14:52:01,446 INFO     29 [qwen-vl-parser] text API response (len=2906):
["奕检医学", "YIJIANMED LABORATORY", "YJ50430012T", "从而激活特异性信号级反应,促进增殖,细胞运动,存活,血管生成,代谢和逃避抗肿瘤免疫应答", "(PMID:15731001;PMID:12728271)。Ras 蛋白在与 GTP 结合时具有活性,并且通过鸟嘌呤核苷酸交换因子", "(GEFs)进行 GDP 与 GTP 的交换。GEFs 通过加速 Ras 介导的 GTP 酶激活蛋白(GAP)平衡使 Ras 蛋白失活。", "Ras是人类癌症中最常见的致癌基因,Ras编码基因NRAS,KRAS和HRAS中的突变常常损害 Ras 介导的GTP-", "水解,导致 Ras 的组成型激活。致癌 Ras 的恶性转化活性也依赖于脱甲基化,(PMID:22020205)。尽管在 Ras", "家族蛋白质中存在高同源性,但不同的 Ras 同种型在特定类型的癌症中优先突变。NRAS 基因与皮肤,造血和", "淋巴组织的癌症有关。", "NTRK1 基因编码原肌球蛋白受体激酶 A(TrkA),是 Trk 受体酪氨酸激酶家族的成员。NTRK1 由位于染色体", "1q21-22 上的 17 个外显子编码(PMID:12652644),并且可以产生三个不同的剪接变体,即 TrkAI,TrkAll 和", "TrkAIII。TrkAI 和 TrkAll 剪接变体具有高度的相似性,仅在 TrkAll1296 处插入 18 个核苷酸才有所不同", "(PMID:8325889)。在生物学上,TrkAI 被认为是神经母细胞瘤中的肿瘤抑制因子(PMID:19734938),而 TrkAll", "的特征在于增强与神经营养因子的亲和力(PMID:7972023)。通过 NTRK1 的外显子 6,7 和 9 缺失产生 TrkAIII", "变体,导致细胞外免疫球蛋白 C1 结构域的缺失。因此,TrkAIII 蛋白中缺失了几个 N-糖基化位点,限制了其对胞", "内膜隔室的表达,并诱导 PI3K/AKT/NF-κB 信号传导的组成型激活(Farina 等,2009)。重要的是要注意,TrkAIII", "剪接变体被认为是神经母细胞瘤中的致癌基因(PMID:19564412),并促进遗传不稳定性(PMID:19564412)。", "NTRK1", "TrkA 在神经,内分泌和免疫系统的细胞上表达,响应配体结合控制细胞增殖,分化,凋亡和细胞存活", "(PMID:25527197)。尽管神经营养因子 3(NT-3)和 4(NT-4)也可以激活 TrkA,但是它最常被神经生长因子", "(NGF)激活(PMID:18289031)。受体同二聚化后,下游信号级联,最常见的 RAS/MAPK,PI3K/AKT 和 PLCγ", "/PKC 通路被激活(PMID:25527197)。相反,在不存在配体的情况下,TrkA 可通过抑制 PI3K/AKT 信号启动促", "凋亡信号级联,导致 Bad 的去抑制,并激活 JNK 介导的促凋亡转录调节因子,如 Bim 和", "Puma(PMID:22465479)。NTRK1 重排发生在 12%的乳头状甲状腺癌中,3.3%的肺癌和近 1%的多形性恶性", "胶质瘤中。目前在胆道癌中也发现了 RABGAP1L-NTRK1 融合。在结直肠癌和甲状腺癌中,融合的伴侣基因", "包括 TPM3,TFG 和 TPR,而肺癌中检测到 MPRIP 和 CD74。NTRK1 基因融合了完整的 TRKA 激酶结构域,导", "致了 TRKA 激酶活性组成性激活。", "磷脂酰肌醇-3-激酶(PI3K)由调节亚基(p85α)和催化亚基(p110α)组成,它是由 PIK3CA 基因编码的催化亚基。", "PIK3CA 是癌症中最常见的突变基因之一,PI3K 的异常激活是转化事件(PMID:17376864)。多种受体酪氨酸", "激酶,包括 EGFR,ERBB2(ERBB2),RET,MET 和 VEGFR 等均可将细胞外信号转化为细胞内信号,并通过支架蛋白", "如 IRS1 或通过激活 RAS 将 PI3K 募集至质膜。刺激后,PI3K-110α将其脂质底物 PIP2(磷脂酰肌醇-4,5-二磷", "酸)转化为 PIP3(磷脂酰肌醇-3,4,5-二磷酸),激活几个信号级联反应,包括充分表征的 AKT-mTOR 通路。一旦", "被激活,AKT-mTOR 下游信号传导可促进细胞存活,增殖,生长和运动(PMID:16341083)。长期暴露于一些", "PI3K/mTOR 途径靶向药物可以减轻癌细胞 PI3K-AKT-mTOR 途径固有的自我调节特性,从而促进肿瘤对这", "PIK3CA", "些药物的耐药性(PMID:22576208)。", "PMS2 是一种内切核酸酶,在错配修复(MMR)途径中起重要作用。具体而言,PMS2 切割 DNA 以启动错配链", "的切除(PMID:20624957)。PMS2 突变导致不能正确修复 DNA 的错配和插入/缺失环,这导致肿瘤超突变增", "加和微卫星不稳定性高(MSI-H)表型(PMID:14871975)。PMS2 的种系突变可引起 Lynch 综合征,其易患某些", "PMS2", "癌症,包括结肠癌,子宫内膜癌和卵巢癌,并暗示 PMS2 为肿瘤抑制因子(PMID:16472587)。在来自多种组织类", "型的癌症中也报道了散发性 PMS2 突变(PMID:16472587)。肿瘤超突变与某些免疫疗法的反应有关。具体而", "言,pembrolizumab 已被 FDA 批准用于所有 MMR 缺陷和 MSI 肿瘤,不论特定肿瘤病因", "(PMID:25409260,26028255)", "PTEN 编码肿瘤抑制因子,其是人癌症中最频繁突变的基因之一(PMID:9072974,9090379,22473468)。PTEN", "具有几种生理功能,最显着的是在细胞膜上将磷脂酰肌醇(3,4,5)-三磷酸(PIP3)转化为磷脂酰肌醇(4,5)-三磷酸", "(PIP2)(PMID:18767981)。PTEN 功能的损害可导致 PIP3 积累和分解代谢下游 AKT/mTOR 信号传导的组成", "型激活。因此,PTEN 失活可促进细胞生长,增殖和存活(PMID:12040186)。另外,核 PTEN 被认为可调节 RAD51", "PTEN", "表达,与 DNA 链断裂的同源重组和修复相关(PMID:17218262,23888040)。因此,PTEN 的丧失也可能导致更", "严重的基因组不稳定性并为其他有害突变的积累提供帮助。PTEN 经常在许多类型的人类癌症中发生突变", "—14—", "上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com"]
2026-08-10 14:52:01,448 INFO     29 [qwen-vl-parser] page=31 text: 54 lines (bbox 1166-1219)
2026-08-10 14:52:01,448 INFO     29 [qwen-vl-parser] page=31 text: 54 sections
2026-08-10 14:52:01,523 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=508942, prompt_len=764
2026-08-10 14:52:02,827 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:52:02,827 INFO     29 [qwen-vl-parser] page=32 classify=text report_date=None
2026-08-10 14:52:02,836 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=508942, prompt_len=401
2026-08-10 14:52:08,449 INFO     29 [qwen-vl-parser] text API response (len=1046):
["奕检医学", "YIJIANMED LABORATORY", "YJ50430012T", "(PMID:15254063),PTEN 种系功能丧失突变发生在约80%的癌症易感性综合征 Cowden 病患者中,其与高外", "显率乳腺癌和甲状腺癌相关(PMID:9467011,24136893,21430697)。", "RET 是一种受体酪氨酸激酶,可与神经胶质细胞系衍生的神经营养因子(GDNF)家族的配体结合,并通过促癌基", "因丝裂原活化蛋白激酶(MAPK)和磷酸肌醇 3-激酶(PI3K)途径传递细胞内信号(PMID:24561444)。RET 通常", "在发育中的胚胎中表达,在神经和神经内分泌中起着特别重要的作用(PMID:8306871)。在癌症中,RET 可以通", "过点突变或基因重排与多种易位配体融合,产生组成型活性胞质癌蛋白(PMID:24561444)。RET 中可遗传的激", "活突变导致高度渗透性家族性癌症综合征多发性内分泌腺癌 2A 型(MEN2A:甲状腺髓样癌,嗜铬细胞瘤,甲状", "旁腺功能亢进),多发性内分泌腺瘤 2B 型(MEN2B:甲状腺髓样癌,嗜铬细胞瘤,多发性粘膜神经瘤和肠神经节细", "胞瘤)和家族性甲状腺髓样癌(FMTC)(PMID:15322516)。致癌体细胞突变包括 RET 基因座的点突变和基因组", "重排。已经在各种癌症中鉴定出这些变异,包括乳头状甲状腺癌,肺腺癌和慢性髓单核细胞白血病(CMML)。此", "外,野生型 RET 的异常表达或活化与胰腺癌中的肿瘤侵袭和转移以及乳腺癌中的内分泌治疗抗性相关", "(PMID:24561444)。", "TP53 编码 p53 肿瘤抑制蛋白,这是一种转录因子,可通过诱导下游抗肿瘤反应如 DNA 修复和凋亡", "(PMID:11099028)来响应细胞应激,包括 DNA 损伤和致癌活化。TP53 是人类癌症中最常见的突变基因,并且", "在癌症易感性综合征 Li-Fraumeni 中可发生种系突变(PMID:22713868,21765642)。p53 蛋白由 N-末端反", "式激活结构域,中心 DNA 结合结构域,寡聚化结构域和 C-末端调节结构域组成(PMID:22713868)。", "— 15 —", "上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com"]
2026-08-10 14:52:08,450 INFO     29 [qwen-vl-parser] page=32 text: 21 lines (bbox 1220-1240)
2026-08-10 14:52:08,450 INFO     29 [qwen-vl-parser] page=32 text: 21 sections
2026-08-10 14:52:08,547 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=760093, prompt_len=764
2026-08-10 14:52:09,928 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:52:09,929 INFO     29 [qwen-vl-parser] page=33 classify=text report_date=None
2026-08-10 14:52:09,939 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=760093, prompt_len=401
2026-08-10 14:52:11,638 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:52:11.637+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 64, "failed": 0, "current": {"7630dbd094ca11f1bd9827cf206dfa2d": {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:52:20,203 INFO     29 [qwen-vl-parser] text API response (len=1757):
["奕检医学", "YIJIANMED LABORATORY", "YJ50430012T", "常见靶向药物说明", "药物", "中文", "药物说明", "FDA", "NPMA", "Trametinib", "曲美替尼", "曲美替尼", "(Trametinib) 是一", "种口服生物可利用的", "丝裂原激活的细胞外", "信号调节激酶 1", "(MEK1) 和 MEK2", "抑制剂。它于 2013", "年 5 月首次被 FDA", "批准用于治疗黑色素", "瘤。", "FDA 批准：1. 曲美替尼联合达拉非尼用", "于 BRAF V600E 或 V600K 突变的不可切", "除或转移性黑色素瘤患者的治疗；2. 曲", "美替尼联合达拉非尼用于 BRAF V600E", "或 V600K 突变且累及淋巴结的黑色素瘤", "患者术后的辅助治疗；3. 曲美替尼联合", "达拉非尼治疗 BRAF V600E 突变的转移", "性非小细胞肺癌(NSCLC)患者；4. 曲美", "替尼联合达拉非尼治疗 BRAF V600E 突", "变的局部晚期或转移性甲状腺未分化癌", "(ATC)患者，无令人满意的局部区域治疗", "选择；5. 曲美替尼联合达拉非尼用于治", "疗 1 岁及以上 BRAF V600E 突变的不可", "切除或转移性实体瘤的成人和儿童患者，", "这些患者在先前的治疗后已经进展，并且", "没有令人满意的替代治疗方案。6. 曲美", "替尼联合达拉非尼治疗 1 岁以上 BRAF", "V600E 突变的低级别胶质瘤(LGG)患", "儿，需要全身治疗。", "NMPA 批准:1. 联合甲磺酸", "达拉非尼适用于治疗 BRAF", "V600 突变阳性的不可切除", "或转移性黑色素瘤患者；2.", "联合甲磺酸达拉非尼适用于", "BRAF V600 突变阳性的 III", "期黑色素瘤患者完全切除后", "的辅助治疗；3. 联合甲磺酸", "达拉非尼适用于治疗 BRAF", "V600 突变阳性的转移性非", "小细胞肺癌患者。", "Encorafenib", "Encorafenib 是一种", "口服 Raf 激酶抑制", "剂，具有潜在的抗肿", "瘤活性，特异性抑制", "Raf 激酶（RAF/丝裂", "原活化蛋白激酶激酶", "(MEK)/细胞外信号", "相关激酶（ERK）信", "号通路中的一种丝氨", "酸/苏氨酸酶）。", "FDA 批准：1. 与 binimetinib 联合，用", "于治疗经 FDA 批准的试验检测为 BRAF", "V600E 或 V600K 突变的不可切除或转移", "性黑色素瘤患者；2. 联合 binimetinib", "治疗经 FDA 批准试验检测为 BRAF", "V600E 突变的转移性非小细胞肺癌成年", "患者；3. 联合西妥昔单抗，用于既往治", "疗后经 FDA 批准试验检测为 BRAF", "V600E 突变的成人转移性结直肠癌患者", "的治疗。", "无", "Tucatinib", "Tucatinib 是一种酪", "氨酸激酶抑制剂，靶", "向人表皮生长因子受", "体 2 （HER2），与", "其他抗肿瘤药联合用", "于治疗难治性、晚期", "或转移性 HER2 阳", "性乳腺癌和结直肠", "癌。", "FDA 批准：1. Tucatinib 联合曲妥珠单", "抗和卡培他滨用于晚期不可切除或转移", "性 HER2 阳性乳腺癌成年患者，包括脑", "转移患者，他们在转移性情况下既往接受", "过一种或多种基于抗 HER2 的治疗方", "案；2. Tucatinib 与曲妥珠单抗联合用于", "治疗 RAS 野生型 HER2 阳性不可切除或", "转移性结直肠癌的成年患者，这些患者在", "氟尿嘧啶、奥沙利铂和伊立替康为基础的", "化疗后进展。", "无", "— 16 —", "上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com"]
2026-08-10 14:52:20,204 INFO     29 [qwen-vl-parser] page=33 text: 96 lines (bbox 1241-1336)
2026-08-10 14:52:20,204 INFO     29 [qwen-vl-parser] page=33 text: 96 sections
2026-08-10 14:52:20,309 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=890577, prompt_len=764
2026-08-10 14:52:21,668 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:52:21,669 INFO     29 [qwen-vl-parser] page=34 classify=text report_date=None
2026-08-10 14:52:21,696 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=890577, prompt_len=401
2026-08-10 14:52:32,435 INFO     29 [qwen-vl-parser] text API response (len=2125):
["奕检医学", "YIJIANMED LABORATORY", "YJ50430012T", "Dabrafenib", "达拉非尼", "达拉非尼", "(Dabrafenib) 是一", "种有机氟化合物和抗", "肿瘤剂, 用作其甲磺", "酸盐治疗转移性黑色", "素瘤。它具有抗肿瘤", "剂、B-Raf 抑制剂和", "抗冠状病毒剂的作", "用。它是一种磺胺类", "化合物, 一种有机氟", "化合物, 是 1,3-噻唑", "类和氨基嘧啶的成", "员。达拉非尼是一种", "可逆的 ATP 竞争性", "激酶抑制剂, 靶向", "MAPK 通路。", "FDA 批准: 1. 作为单一药物, 用于治疗", "经 FDA 批准的检测检测到的具有", "BRAF V600E 突变的不可切除或转移性", "黑色素瘤患者; 2. 与曲美替尼联合用于:", "a. FDA 批准的检测检测到 BRAF V600E", "或 V600K 突变的不可切除或转移性黑色", "素瘤患者的治疗; b. 通过 FDA 批准的试", "验检测出具有 BRAF V600E 或 V600K 突", "变的黑色素瘤患者的辅助治疗, 以及在完", "整切除后累及淋巴结的患者; c. 治疗经", "FDA 批准的检测检测到的具有 BRAF", "V600E 突变的转移性非小细胞肺癌", "(NSCLC) 患者; d. 治疗 BRAF V600E", "突变的无满意的局部区域治疗方案的局", "部晚期或转移性未分化甲状腺癌患者; e.", "1 岁及以上的成人和儿童 BRAF V600E", "突变不可切除或转移性实体瘤患者的治", "疗, 这些患者在先前治疗后进展, 没有令", "人满意的替代治疗方案; f. 治疗 1 岁及", "以上患有具有 BRAF V600E 突变且需", "要全身治疗的低级别胶质瘤 (LGG) 的", "儿科患者。(由于已知 BRAF 抑制的内在", "抗性, TAFINLAR 不适合用于结直肠癌患", "者的治疗; 并且不用于 BRAF 野生型实体", "瘤患者的治疗)", "NMPA 批准用于:1. 联合曲", "美替尼用于治疗 BRAF", "V600 突变阳性的不可切除", "或转移性黑色素瘤患者; 2.", "联合曲美替尼用于 BRAF", "V600 突变阳性的 III 期黑色", "素瘤患者完全切除后的辅助", "治疗; 3. 联合曲美替尼用于", "治疗 BRAF V600 突变阳性", "的转移性非小细胞肺癌患", "者。", "Regorafenib", "瑞戈非尼", "瑞戈非尼", "(Regorafenib) 是一", "种激酶抑制剂。用于", "治疗既往接受过化", "疗、抗 EGFR 或抗", "VEGF 治疗的转移性", "结直肠癌患者。它具", "有抗肿瘤药、酪氨酸", "激酶抑制剂和肝毒性", "药物的作用。", "FDA 批准: 1. 用于先前接受索拉非尼治", "疗的肝癌 (HCC) 患者; 2. 用于治疗转", "移性结直肠癌 (mCRC) 的患者, 之前曾", "接受氟嘧啶, 奥沙利铂和伊立替康为基础", "的化疗、抗 VEGF 治疗, 以及 KRAS 野生", "型的抗 EGFR 治疗; 3. 用于既往接受甲", "磺酸伊马替尼和苹果酸舒尼替尼治疗的", "局部晚期、不可切除或转移性胃肠道间质", "瘤 (GIST) 患者的治疗。", "NMPA 批准:1. 用于治疗既", "往接受过索拉非尼治疗的肝", "细胞癌 (HCC) 患者; 2. 用", "于治疗既往接受过以氟尿嘧", "啶、奥沙利铂和伊立替康为", "基础的化疗, 以及既往接受", "过或不适合接受抗 VEGF 治", "疗、抗 EGFR 治疗 (KRAS", "野生型) 的转移性结直肠癌", "(mCRC) 患者; 3. 用于既", "往接受过甲磺酸伊马替尼及", "苹果酸舒尼替尼治疗的局部", "晚期的、无法手术切除的或", "转移性的胃肠道间质瘤", "(GIST) 患者。", "Fruquintinib", "呋喹替尼", "呋喹替尼", "呋喹替尼是一个喹唑", "啉类小分子血管生成", "抑制剂, 主要作用靶", "点是 VEGFR 激酶家族", "(VEGFR1、2 和 3)。", "FDA 批准: 适用于既往接受过氟尿嘧啶", "类、奥沙利铂和伊立替康为基础的化疗,", "以及既往接受过或不适合接受抗血管内", "皮生长因子 (VEGF) 治疗、抗表皮生长", "因子受体 (EGFR) 治疗 (RAS 野生型)", "NMPA 批准: 呋喹替尼胶囊", "单药适用于既往接受过氟尿", "嘧啶类、奥沙利铂和伊立替", "康为基础的化疗, 以及既往", "接受过或不适合接受抗血管", "— 17 —", "上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话: 400-004-2111 网址: www.yjmedlab.com"]
2026-08-10 14:52:32,436 INFO     29 [qwen-vl-parser] page=34 text: 113 lines (bbox 1337-1449)
2026-08-10 14:52:32,437 INFO     29 [qwen-vl-parser] page=34 text: 113 sections
2026-08-10 14:52:32,544 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=874013, prompt_len=764
2026-08-10 14:52:33,882 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:52:33,883 INFO     29 [qwen-vl-parser] page=35 classify=text report_date=None
2026-08-10 14:52:33,901 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=874013, prompt_len=401
2026-08-10 14:52:43,234 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:52:43.233+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 64, "failed": 0, "current": {"7630dbd094ca11f1bd9827cf206dfa2d": {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:52:43,598 INFO     29 [qwen-vl-parser] text API response (len=2032):
["奕检医学", "YIJIANMED LABORATORY", "YJ50430012T", "通过抑制血管内皮细", "胞表面的 VEGFR 磷酸", "化及下游信号转导,", "抑制血管内皮细胞的", "增殖、迁移和管腔形", "成，从而抑制肿瘤新", "生血管的形成，最终", "发挥肿瘤生长抑制效", "应。", "的转移性结直肠癌患者。", "内皮生长因子 (VEGF) 治疗、", "抗表皮生长因子受体", "(EGFR) 治疗 (RAS 野生型)", "的转移性结直肠癌患者。", "Selpercatinib", "塞普替尼", "塞普替尼", "(Selpercatinib) 是", "一种选择性 RET 激酶", "抑制剂, 能够阻断 RET", "激酶, 并阻止癌细胞", "生长。", "FDA 批准: 1. 用于治疗局部晚期或转移", "性非小细胞肺癌的成年患者, 经 FDA 批", "准的试验检测到 RET 基因融合; 2. 适用", "于 2 岁及以上的成人和儿童晚期或转移", "性甲状腺髓样癌 (MTC) 患者, 经 FDA 批", "准的试验检测出 RET 突变, 需要系统性", "治疗; 3. 用于治疗 2 岁及以上的, 经 FDA", "批准的试验检测具有 RET 基因融合的晚", "期或转移性甲状腺癌的成人和儿童患者,", "这些患者需要系统性治疗, 并且是放射性", "碘难治性 (如果放射性碘是合适的); 4. 适", "用于经 FDA 批准的试验检测为 RET 基因", "融合的局部晚期或转移性实体肿瘤的 2", "岁及以上的成人和儿童患者, 这些患者在", "接受系统性之前或之后有进展, 或者没有", "令人满意的替代治疗方案。", "NMPA 批准: 塞普替尼用于", "治疗 RET 基因融合阳性的局", "部晚期或转移性非小细胞肺", "癌成人患者; 2. 需要系统性", "治疗的晚期或转移性 RET 突", "变型甲状腺髓样癌成人和", "12 岁及以上儿童患者、以及", "需要系统性治疗且放射性碘", "难治 (如果放射性碘适用)", "的晚期或转移性 RET 融合阳", "性甲状腺癌成人和 12 岁及", "以上儿童患者。", "Repotrectinib", "瑞普替尼", "瑞普替尼", "(Repotrectinib) 是", "一种酪氨酸蛋白激酶", "原癌基因 ROS1 和原", "肌球蛋白受体酪氨酸", "激酶 (TRKs) TRKA、", "TRKB 及 TRKC 的抑制", "剂。", "FDA 批准: 1. 用于治疗 ROS1 阳性的局", "部晚期或转移性非小细胞肺癌成人患者;", "2. 用于治疗 12 岁及以上具有神经营养", "性酪氨酸受体激酶 (NTRK) 基因融合的局", "部晚期、转移性或手术切除可能导致严重", "疾病、治疗后病情进展或没有令人满意的", "替代疗法的成人和儿童实体瘤患者。", "NMPA 批准: 适用于 ROS1", "阳性的局部晚期或转移性非", "小细胞肺癌 (NSCLC) 成人", "患者。", "Entrectinib", "恩曲替尼", "恩曲替尼", "(Entrectinib) 是一", "种原肌球蛋白受体酪", "氨酸激酶 (TRK)", "TRKA、TRKB、TRKC、", "原癌基因酪氨酸蛋白", "激酶 ROS1 和间变", "性淋巴瘤激酶 (ALK)", "抑制剂。它于 2019", "年 8 月获得 FDA", "批准用于治疗 ROS1", "阳性转移性非小细胞", "FDA 批准: 1. 用于治疗 ROS1 阳性的转", "移性非小细胞肺癌 (NSCLC) 成人患者;", "2. 用于治疗年龄大于 1 个月的儿童和成人", "实体瘤患者: a. 具有经 FDA 批准的试验", "检测到神经营养性酪氨酸受体激酶", "(NTRK) 基因融合, 没有已知的获得性", "抗性突变; b. 转移或手术切除可能导致严", "重的并发症; c. 治疗后进展或没有令人", "满意的替代疗法。", "NMPA 批准: 1. ROS1 阳性", "的局部晚期或转移性非小细", "胞肺癌 (NSCLC) 成人患者;", "2. 用于符合下列条件的成", "人和 1 月龄以上儿童实体", "瘤患者: a. 经充分验证的检", "测方法诊断为携带神经营养", "酪氨酸受体激酶 (NTRK) 融", "合基因且不包括已知获得性", "耐药突变; b. 患有局部晚", "期、转移性疾病或手术切除", "可能导致严重并发症的患", "— 18 —", "上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com"]
2026-08-10 14:52:43,599 INFO     29 [qwen-vl-parser] page=35 text: 111 lines (bbox 1450-1560)
2026-08-10 14:52:43,599 INFO     29 [qwen-vl-parser] page=35 text: 111 sections
2026-08-10 14:52:43,696 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=747753, prompt_len=764
2026-08-10 14:52:44,987 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:52:44,988 INFO     29 [qwen-vl-parser] page=36 classify=text report_date=None
2026-08-10 14:52:45,001 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=747753, prompt_len=401
2026-08-10 14:52:55,358 INFO     29 [qwen-vl-parser] text API response (len=1771):
["奕检医学", "YIJIANMED LABORATORY", "YJ50430012T", "肺癌和 NTRK 基因", "融合阳性实体瘤。", "者；c. 无满意替代治疗或既", "往治疗失败的患者。", "Larotrectinib", "拉罗替尼", "拉罗替尼", "(Larotrectinib) 是", "一种原肌球蛋白受体", "激酶(TRK), TRKA、", "TRKB、TRKC 的抑制", "剂。TRKA、TRKB 和", "TRKC 由 NTRK1、", "NTRK2 和 NTRK3 基", "因编码。这些基因与", "不同配体基因间的框", "架内融合导致的染色", "体重排可产生组成性", "激活嵌合 TRK 融合蛋", "白, 其可作为致癌驱", "动因子, 促进肿瘤细", "胞系中的细胞增殖和", "存活。", "FDA 批准: 用于治疗具备以下条件的成", "人和儿童实体瘤患者: 1. 具有神经营养", "性受体酪氨酸激酶 (NTRK) 基因融合,", "但没有已知的获得性抗性突变; 2. 转移", "或手术切除可能导致严重的发病率; 3.", "没有令人满意的替代治疗或治疗后进展。", "NMPA 批准: 用于治疗符合", "下列条件的成人和儿童实体", "瘤患者: 1. 经充分验证的检", "测方法诊断为携带神经营养", "酪氨酸受体激酶 (NTRK) 融", "合基因且不包括已知获得性", "耐药突变; 2. 患有局部晚", "期、转移性疾病或手术切除", "可能导致严重并发症的患", "者; 3. 无满意替代治疗或既", "往治疗失败的患者。", "Cetuximab", "西妥昔单抗", "西妥昔单抗", "(Cetuximab) 是一", "种重组嵌合人/小鼠", "IgG1 单克隆抗体, 与", "表皮生长因子受体", "(EGFR) 竞争性结", "合, 并竞争性抑制表", "皮生长因子 (EGF)", "的结合。EGFR 是受体", "酪氨酸激酶 ErbB 家", "族的一员, 存在于正", "常细胞和肿瘤细胞", "中; 它负责调节上皮", "组织的发育和体内平", "衡。EGFR 与各种类型", "的癌症有关, 因为它", "通常在恶性细胞中过", "表达, 并且 EGFR 过", "表达与更晚期的疾病", "和不良预后有关。", "EGFR 在某些类型的", "癌症中经常发生突", "FDA 批准: 1. 用于经 FDA 批准的检测", "检测到 KRAS 突变阴性 (野生型)、EGFR", "表达阳性的转移性结直肠癌患者 (使用限", "制: 不适用于 RAS 突变或 RAS 突变未知", "的结直肠癌患者) : a.作为单药治疗, 用", "于既往经历奥沙利铂或伊立替康为基础", "的化疗方案并失败以及对伊立替康不耐", "受的患者; b.与 FOLFIRI 联合用于一线", "治疗; c.与伊立替康联合用于伊立替康为", "基础的化疗难治的患者; 2. 用于治疗头", "颈癌: a.局部或区域晚期头颈部鳞状细胞", "癌联合放射治疗; b.复发性局部区域疾病", "或头颈部转移性鳞状细胞癌联合氟尿嘧", "啶铂类治疗; c.铂类治疗后进展的头颈部", "复发性或转移性鳞状细胞癌; 3. 与", "Encorafenib 联合用于治疗经 fda 批准的", "试验检测出 BRAF V600E 突变的转移性", "结直肠癌(CRC)成人患者。", "NMPA 批准: 1. 用于治疗", "RAS 基因野生型的转移性", "结直肠癌:a.与 FOLFOX 或", "FOLFIRI 方案联合用于一线", "治疗; b. 与伊立替康联合用", "于经含伊立替康治疗失败后", "的患者; 2. 用于治疗头颈部", "鳞状细胞癌: a. 与铂类和氟", "尿嘧啶化疗联合用于一线治", "疗复发和/或转移性疾病; b.", "与放疗联合用于治疗局部晚", "期疾病。", "—19—", "上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话: 400-004-2111 网址: www.yjmedlab.com"]
2026-08-10 14:52:55,359 INFO     29 [qwen-vl-parser] page=36 text: 99 lines (bbox 1561-1659)
2026-08-10 14:52:55,359 INFO     29 [qwen-vl-parser] page=36 text: 99 sections
2026-08-10 14:52:55,453 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=765815, prompt_len=764
2026-08-10 14:52:56,790 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:52:56,790 INFO     29 [qwen-vl-parser] page=37 classify=text report_date=None
2026-08-10 14:52:56,806 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=765815, prompt_len=401
2026-08-10 14:53:05,839 INFO     29 [qwen-vl-parser] text API response (len=1736):
["奕检医学", "YIJIANMED LABORATORY", "YJ50430012T", "变，并作为肿瘤发生", "的驱动因素。在体外,", "西妥昔单抗被证明在", "许多癌细胞系和人肿", "瘤异种移植物中具有", "抗肿瘤作用。", "Panitumumab 是一", "种对表皮生长因子受", "体 （EGFR） 具有特", "异性的人", "lgG2kappa 单克隆", "抗体。单克隆抗体", "E7.6.3 与 EGFR 结", "合，阻断表皮生长因", "子的结合并将生长因", "子 α 转化为表达", "EGFR 的癌细胞,并最", "终抑制 EGFR 依赖性", "细胞活化和增殖。", "FDA 批准：用于 RAS 野生型 (定义为", "KRAS 和 NRAS 中的野生型) 转移性结直", "肠癌 (mCRC) 患者：1. 单药治疗既往", "经过氟嘧啶, 奥沙利铂, 和伊立替康化疗", "方案后疾病进展的转移性结直肠癌; 2.", "与 FOLFOX 联合用于一线治疗。（使用", "限制：携带 RAS 基因突变或者 RAS 突变", "状态不明的结直肠癌的治疗不建议使用", "帕尼单抗）。", "无", "Panitumumab", "贝伐珠单抗是利用重", "组 DNA 技术制备的", "一种人源化单克隆抗", "体 IgG1, 通过与人血", "管内皮生长因子", "(VEGF) 结合, 抑制", "VEGF 与其受体结合,", "阻断血管生成的信号", "传导途径, 抑制肿瘤", "细胞生长。作为抗肿", "瘤血管生成的重要药", "物之一, 贝伐珠单抗", "被应用于多种恶性肿", "瘤的治疗。", "FDA 批准:1. 转移性结直肠癌:a. 与 5-", "氟尿嘧啶化疗联合作为转移性结直肠癌", "的一线或二线治疗方案; b. 与氟尿嘧啶", "-伊立替康或氟尿嘧啶 -奥沙利铂为基础", "的化疗联合用于经贝伐单抗一线治疗后", "出现疾病进展的转移结直肠癌的二线治", "疗; c. 贝伐单抗联合曲氟尿苷和替吉奥", "用于转移性结直肠癌的治疗, 此前使用氟", "尿嘧啶、奥沙利铂和伊立替康为基础的化", "疗, 抗 VEGF 生物治疗, 如果 RAS 野生", "型, 抗 EGFR 治疗; 2. 非小细胞肺癌:", "a. 贝伐珠单抗联合紫杉醇和卡铂一线治", "疗不可切除的局部晚期、复发性或转移性", "非鳞状非小细胞肺癌; b. 贝伐单抗联合", "阿替利珠单抗、紫杉醇和卡铂一线治疗无", "EGFR 或 ALK 基因组肿瘤畸变的转移性", "非鳞非小细胞肺癌; 3. 贝伐珠单抗治疗", "成人复发性胶质母细胞瘤; 4. 贝伐珠单", "抗联合干扰素α治疗转移性肾细胞癌; 5.", "贝伐珠单抗联合紫杉醇和顺铂, 或紫杉醇", "和拓扑替康治疗持续性、复发性或转移性", "宫颈癌; 6. 上皮性卵巢癌、输卵管癌或", "NMPA 批准:1. 转移性结直", "肠癌: 贝伐珠单抗联合以氟", "嘧啶为基础的化疗适用于转", "移性结直肠癌患者的治疗;", "2. 晚期、转移性或复发性非", "小细胞肺癌: 贝伐珠单抗联", "合以铂类为基础的化疗用于", "不可切除的晚期、转移性或", "复发性非鳞状细胞非小细胞", "肺癌患者的一线治疗; 3. 复", "发性胶质母细胞瘤: 贝伐珠", "单抗用于成人复发性胶质母", "细胞瘤患者的治疗; 4. 肝细", "胞癌: 贝伐珠单抗联合阿替", "利珠单抗治疗既往未接受过", "全身系统性治疗的不可切除", "肝细胞癌患者; 5. 上皮性卵", "巢癌、输卵管癌或原发性腹", "膜癌: 贝伐珠单抗联合卡铂", "和紫杉醇用于初次手术切除", "后的 III 期或 IV 期上皮性", "卵巢癌、输卵管癌或原发性", "Bevacizumab", "贝伐珠单抗", "— 20 —", "上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com"]
2026-08-10 14:53:05,839 INFO     29 [qwen-vl-parser] page=37 text: 95 lines (bbox 1660-1754)
2026-08-10 14:53:05,839 INFO     29 [qwen-vl-parser] page=37 text: 95 sections
2026-08-10 14:53:05,940 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=994460, prompt_len=764
2026-08-10 14:53:07,324 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:53:07,325 INFO     29 [qwen-vl-parser] page=38 classify=text report_date=None
2026-08-10 14:53:07,343 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=994460, prompt_len=401
2026-08-10 14:53:14,878 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:53:14.877+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 64, "failed": 0, "current": {"7630dbd094ca11f1bd9827cf206dfa2d": {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:53:19,030 INFO     29 [qwen-vl-parser] text API response (len=2305):
["奕检医学", "YIJIANMED LABORATORY", "YJ50430012T", "原发性腹膜癌：a. 贝伐珠单抗与卡铂和", "紫杉醇联合使用，随后以贝伐珠单抗作为", "单一药物，用于初始手术切除后的 III 期", "或 IV 期上皮性卵巢癌、输卵管癌或原发", "性腹膜癌；b.贝伐珠单抗联合紫杉醇、聚", "乙二醇脂质体多柔比星或拓扑替康治疗", "既往接受化疗方案不超过 2 种的铂类耐", "药复发的上皮性卵巢癌、输卵管癌或原发", "性腹膜癌；c. 贝伐珠单抗联合卡铂和紫", "杉醇或卡铂和吉西他滨，随后以贝伐单抗", "作为单药，用于铂类敏感的复发的上皮性", "卵巢癌、输卵管癌或原发性腹膜癌；d. 贝", "伐珠单抗与奥拉帕利联合用于晚期上皮", "性卵巢癌、输卵管癌或原发性腹膜癌成年", "患者的一线维持治疗，这些患者对一线铂", "类化疗完全或部分应答，且其癌症与同源", "重组缺失阳性状态有关，即有害或疑似有", "害 BRCA 基因突变和/或基因组不稳定；", "7. 贝伐珠单抗与阿替利珠单抗联合治", "疗既往未接受过系统治疗的不可切除性", "或转移性肝细胞癌患者。", "腹膜癌患者的一线治疗；6.", "宫颈癌：贝伐珠单抗联合紫", "杉醇和顺铂或紫杉醇和托泊", "替康用于持续性、复发性或", "转移性宫颈癌患者的治疗；", "7. 不可切除或转移性肝细", "胞癌：贝伐珠单抗联合信迪", "利单抗，用于既往未接受过", "系统治疗的不可切除或转移", "性肝细胞癌的一线治疗；8.", "晚期非鳞状非小细胞肺癌：", "贝伐珠单抗联合信迪利单", "抗、培美曲塞和顺铂，用于", "经表皮生长因子受体酪氨酸", "激酶抑制剂（EGFR-TKI）治", "疗失败的 EGFR 基因突变", "阳性的局部晚期或转移性非", "鳞状非小细胞肺癌", "(NSCLC) 患者的治疗。", "纳武利尤单抗", "(Nivolumab) 是一", "种全人源免疫球蛋白", "( Ig ) G4 单克隆抗体，", "针对人细胞表面负性", "免疫调节受体程序性", "死亡受体- 1 ( PD -", "1、PCD - 1)，具有免", "疫检查点抑制和抗肿", "瘤活性。给药后，纳", "武单抗通过其配体程", "序性细胞死亡配体 1", "( PD-L1 )和程序性细", "胞死亡配体 2", "( PD-L2 )结合并阻断", "免疫球蛋白超家族", "( IgSF )跨膜蛋白 PD -", "1 的活化。PD - 1 和", "PD - L1 在某些癌细", "胞上过表达，PD - L2", "主要表达于抗原呈递", "细胞( APC )。这导致", "了 T 细胞的激活和细", "胞介导的针对肿瘤细", "FDA 批准：1. 用于黑色素瘤患者：a. 单", "药或联合伊匹木单抗，用于成人和儿童", "(12 岁及以上)不可切除或转移性黑色素", "瘤患者；b. 用于完全切除 IIB 期、IIC 期、", "III 期或 IV 期黑色素瘤的 12 岁及以上儿", "童和成人患者的辅助治疗；2. 用于非小", "细胞肺癌患者：a. 联合含铂双药化疗，", "用于在新辅助环境下可切除(肿瘤≥4cm", "或淋巴结阳性)的非小细胞肺癌的成年患", "者；b. 联合伊匹木单抗作为一线治疗，", "经 FDA 批准的试验检测到 D-L1 表达阳", "性（定义为表达 PD-L1 的肿瘤细胞≥", "1%) 无 EGFR 或 ALK 基因突变的转移性", "非小细胞肺癌成年患者；c. 联合伊匹木", "单抗和 2 周期铂双药化疗作为一线治疗，", "无 EGFR 或 ALK 基因突变的转移性或复", "发性非小细胞肺癌成年患者；d. 用于在", "铂类化疗中或化疗后进展转移性非小细", "胞肺癌的成人患者。对于 EGFR 或 ALK", "基因突变的患者，在接受 OPDIVO 之前，", "应在 FDA 批准的针对这些突变的治疗中", "出现疾病进展；3. 联合伊匹木单抗作为", "一线治疗不可切除的成人恶性胸膜间皮", "瘤；4. 用于肾细胞癌患者：a. 联合伊匹", "NMPA 批准:1. 用于治疗表", "皮生长因子受体 (EGFR) 基", "因突变阴性和间变性淋巴瘤", "激酶 (ALK) 阴性、既往接", "受过含铂方案化疗后疾病进", "展或不可耐受的局部晚期或", "转移性非小细胞肺癌", "(NSCLC) 成人患者；2. 联", "合含铂双药化疗适用于新辅", "助治疗可切除的 (肿瘤直径", "≥4cm 或淋巴结阳性) 非小", "细胞肺癌 (NSCLC) 成人患", "者；3. 单药适用于治疗接受", "含铂类方案治疗期间或之后", "出现疾病进展且肿瘤", "PD-L1 表达阳性（定义为表", "达 PD-L1 的肿瘤细胞≥", "1%) 的复发性或转移性头颈", "部鳞状细胞癌 (SCCHN) 患", "者；4. 用于治疗既往接受过", "两种或两种以上全身性治疗", "方案的晚期或复发性胃或胃", "食管连接部腺癌患者；5. 联", "合含氟尿嘧啶和铂类药物化", "Nivolumab", "纳武利尤单", "抗", "— 21 —", "上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com"]
2026-08-10 14:53:19,030 INFO     29 [qwen-vl-parser] page=38 text: 120 lines (bbox 1755-1874)
2026-08-10 14:53:19,030 INFO     29 [qwen-vl-parser] page=38 text: 120 sections
2026-08-10 14:53:19,113 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=654695, prompt_len=764
2026-08-10 14:53:20,446 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:53:20,446 INFO     29 [qwen-vl-parser] page=39 classify=text report_date=None
2026-08-10 14:53:20,462 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=654695, prompt_len=401
2026-08-10 14:53:28,587 INFO     29 [qwen-vl-parser] text API response (len=1230):
["奕检医学", "YIJIANMED LABORATORY", "YJ50430012T", "胞的免疫反应。活化的 PD - 1 负性调节 T", "细胞活化，在肿瘤逃", "避宿主免疫中发挥关", "键作用。", "木单抗作为一线治疗，成人中低风险晚期", "肾细胞癌患者；b. 联合卡博替尼作为一", "线治疗，成人晚期肾细胞癌患者；c. 已", "接受过抗血管生成治疗的成年晚期肾细", "胞癌患者；5. 用于经自体造血干细胞移", "植(HSCT)和贝伦妥单抗-维多汀治疗后或", "包括自体 HSCT 在内的 3 种或 3 种", "以上系统疗法治疗的复发或进展的经典", "霍奇金淋巴瘤成人患者；6. 用于既往接", "受含铂类化疗方案治疗时或治疗后疾病", "进展的复发性或转移性头颈部鳞状细胞", "癌的成人患者；7. 用于尿路上皮癌患者：", "a. 根治术后复发风险高的成人患者的辅", "助治疗；b. 在含铂化疗期间或之后出现", "疾病进展或新辅助治疗或辅助治疗 12 个", "月内疾病进展的局部晚期或转移性尿路", "上皮癌的成年患者；8. 单用或与伊匹木", "单抗联用于既往接受氟尿嘧啶、奥沙利", "铂、伊立替康治疗后疾病进展的微卫星高", "度不稳定（MSI-H）或错配修复缺陷", "(dMMR) 的转移性结直肠癌成人和儿", "童患者(12 岁及以上)；9. 用于既往接受", "索拉非尼联合伊匹木单抗治疗的肝细胞", "癌成人患者；10. 用于食道癌患者：a.", "用于经新辅助放化疗（CRT）及完全手术", "切除后仍有病理学残留的食管癌或胃食", "管连接部癌的成人患者；b. 联合含氟尿", "嘧啶和含铂化疗作为一线治疗不能切除", "的晚期或转移性食管鳞状细胞癌的成人", "患者；c. 联合伊匹单抗作为一线治疗不", "可切除的晚期或转移性食管鳞状细胞癌", "成人患者；c. 用于先前以氟尿嘧啶和铂", "为基础的化疗后无法切除的晚期、复发或", "转移性食管鳞状细胞癌(ESCC)的成人患", "者；11. 联合含氟尿嘧啶和铂类药物化疗", "适用于晚期或转移性胃癌、胃食管连接部", "癌或食管腺癌成人患者。", "疗适用于一线治疗晚期或转", "移性胃癌、胃食管连接部癌", "或食管腺癌患者；6. 联合伊", "匹木单抗用于不可手术切除", "的、初治的非上皮样恶性胸", "膜间皮瘤成人患者；7. 用于", "经新辅助放化疗（CRT）及", "完全手术切除后仍有病理学", "残留的食管癌或胃食管连接", "部癌患者的辅助治疗；8. 联", "合含氟嘧啶类和铂类化疗用", "于晚期或转移性食管鳞癌患", "者的一线治疗。", "— 22 —", "上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com"]
2026-08-10 14:53:28,587 INFO     29 [qwen-vl-parser] page=39 text: 59 lines (bbox 1875-1933)
2026-08-10 14:53:28,587 INFO     29 [qwen-vl-parser] page=39 text: 59 sections
2026-08-10 14:53:28,688 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1019706, prompt_len=764
2026-08-10 14:53:30,067 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:53:30,068 INFO     29 [qwen-vl-parser] page=40 classify=text report_date=None
2026-08-10 14:53:30,096 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1019706, prompt_len=401
2026-08-10 14:53:42,961 INFO     29 [qwen-vl-parser] text API response (len=2510):
["奕检医学", "YIJIANMED LABORATORY", "YJ50430012T", "Pembrolizumab", "帕博利珠单抗", "帕博利珠单抗", "(Pembrolizumab)", "是一种针对人细胞表", "面受体 PD-1 (程序性", "死亡-1 或程序性细", "胞死亡-1) 的人源化", "单克隆免疫球蛋白", "(Ig) G4 抗体，具", "有潜在的免疫检查点", "抑制和抗肿瘤活性。", "给药后，帕博利珠单", "抗与 PD-1 结合，", "PD-1 是一种在活化", "的 T 细胞表面表达", "的抑制性信号受体，", "并阻断其配体对", "PD-1 的结合和激活，", "从而导致 T 细胞介", "导的针对肿瘤细胞的", "免疫反应的激活。", "PD-1 的配体包括在", "某些癌细胞上过表达", "的程序性细胞死亡配", "体 1 (PD-L1) 和主", "要在 APC 上表达的", "程序性细胞死亡配体", "2 (PD-L2) 。激活的", "PD-1 负向调节 T 细", "胞活化，并在肿瘤逃", "避宿主免疫中发挥关", "键作用。", "FDA 批准：1. 黑色素瘤：a. 用于无法切", "除或转移性黑色素瘤患者；b. 用于完全", "切除后淋巴结受累黑色素瘤患者的辅助", "治疗；2. 非小细胞肺癌： a. 联合培美曲", "塞和铂类化疗用于无 EGFR 突变或 ALK", "重排转移性非鳞状 NSCLC 患者的一线治", "疗；b. 联合卡铂+紫杉醇或白蛋白紫杉醇", "用于转移性鳞状 NSCLC 患者的一线治", "疗；c. 单药用于 PD-L1 TPS≥1% (经 FDA", "批准的检测) 且无 EGFR 突变或 ALK 重", "排的转移性非小细胞肺癌的一线治疗，不", "适合手术切除或根治性放化疗或转移的", "III 期患者；d. 单药用于 PD-L1 TPS≥1%、", "铂类化疗期间或之后进展的转移性非小", "细胞肺癌；携带 EGFR 或 ALK 突变的患", "者在接受 FDA 批准疗法后仍出现疾病进", "展的非小细胞肺癌；e. 作为手术切除和", "铂类化疗后的辅助治疗，用于 IB 期 (T2a", "≥4 厘米) 、II 期或 IIIA 期非小细胞肺", "癌 (NSCLC) 患者；3. 小细胞肺癌：", "单药用于铂类期间或之后且既往至少一", "种其他治疗后进展的转移性小细胞肺癌", "(SCLC) 患者；4. 头颈癌：a. 联合铂类", "+5-FU 用于转移性或不可切除复发的头", "颈部鳞癌 (HNSCC) 的一线治疗；b. 单", "药用于 PD-L1 CPS≥1 (FDA 批准的检测", "方法) 的转移性或不可切除的复发性", "HNSCC 患者的一线治疗；c. 单药用于铂", "类化疗期间或之后进展的复发或转移性", "头颈部鳞癌；5. 霍奇金淋巴瘤：用于难", "治性经典霍奇金淋巴瘤 (cHL) 的成人及", "儿童患者，或经过 3 种及以上前线治疗后", "复发的 cHL 患者的单一疗法；6. 原发性", "纵隔大 B 细胞淋巴瘤 (PMBCL) ：用于", "治疗难治性成人和儿童原发性纵隔大 B", "细胞淋巴瘤 (PMBCL) 患者，或两线及", "以上治疗后复发的患者；7. 尿路上皮癌：", "a. 单药用于不适合铂类为基础的化疗方", "案的 PD-L1 CPS≥10 的局部晚期或转移", "性尿路上皮癌或不论 PD-L1 状态如何，", "不适合任何含铂方案的患者；b. 单药用", "于含铂化疗期间或之后进展、或经含铂新", "辅助或辅助化疗后 12 月内疾病进展的局", "部晚期或转移性尿路上皮癌；c. 联合", "enfortumab vedotin-ejfv 治疗不符合", "NMPA 批准：1. 用于经一线", "治疗失败的不可切除或转移", "性黑色素瘤的治疗；2. 非小", "细胞肺癌：a. 用于由国家药", "品监督管理局批准的检测评", "估为 PD-L1 肿瘤比例分数", "(TPS) ≥1%的表皮生长因", "子受体 (EGFR) 基因突变阴", "性和间变性淋巴瘤激酶", "(ALK) 阴性的局部晚期或", "转移性非小细胞肺癌一线单", "药治疗；b. 联合培美曲塞和", "铂类化疗适用于表皮生长因", "子受体 (EGFR) 基因突变阴", "性和间变性淋巴瘤激酶", "(ALK) 阴性的转移性非鳞", "状非小细胞肺癌 (NSCLC)", "的一线治疗；c. 抗联合卡铂", "和紫杉醇适用于转移性鳞状", "非小细胞肺癌 (NSCLC) 患", "者的一线治疗；3. 食管癌：", "a. 联合铂类和氟尿嘧啶类", "化疗药物用于局部晚期不可", "切除或转移性食管或胃食管", "结合部癌患者的一线治疗；", "b. 单药用于由国家药品监", "督管理局批准的检测评估肿", "瘤表达 PD-L1 (综合阳性评", "分 (CPS) ≥10) 的、既往", "一线全身治疗失败的、局部", "晚期或转移性食管鳞状细胞", "癌 (ESCC) 患者的治疗；4.", "单药用于通过充分验证的检", "测评估肿瘤表达 PD-L1 (综", "合阳性评分 (CPS) ≥20)", "的转移性或不可切除的复发", "性头颈部鳞状细胞癌", "(HNSCC) 患者的一线治", "疗；5. 单药用于 KRAS、", "NRAS 和 BRAF 基因均为野", "生型，不可切除或转移性微", "卫星高度不稳定型 (MSI-H)", "或错配修复基因缺陷型", "(dMMR) 结直肠癌 (CRC)", "患者的一线治疗；6. 单药用", "— 23 —", "上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com"]
2026-08-10 14:53:42,962 INFO     29 [qwen-vl-parser] page=40 text: 128 lines (bbox 1934-2061)
2026-08-10 14:53:42,962 INFO     29 [qwen-vl-parser] page=40 text: 128 sections
2026-08-10 14:53:43,059 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=778357, prompt_len=764
2026-08-10 14:53:44,300 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:53:44,301 INFO     29 [qwen-vl-parser] page=41 classify=text report_date=None
2026-08-10 14:53:44,316 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=778357, prompt_len=401
2026-08-10 14:53:46,502 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:53:46.501+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 64, "failed": 0, "current": {"7630dbd094ca11f1bd9827cf206dfa2d": {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:53:52,887 INFO     29 [qwen-vl-parser] text API response (len=1680):
["奕检医学", "YIJIANMED LABORATORY", "YJ50430012T", "含顺铂化疗条件的局部晚期或转移性尿", "路上皮癌（la/mUC）成年患者；8. 乳腺", "癌：a. 与化疗联合用于治疗局部复发的", "不可切除或转移性三阴性乳腺癌患者", "(TNBC)，其肿瘤表达 PD-L1（由 FDA", "批准的测试确定的综合阳性评分[CPS]≥", "10）；b. 联合化疗作为新辅助治疗治疗", "高危早期三阴性乳腺癌患者，然后继续作", "为手术后的单药辅助治疗；9. 胃癌：a. 单", "药用于经 2 种及以上前线治疗（包括含氟", "尿嘧啶和含铂类化疗方案）进展、PD-L1", "CPS≥1 的复发性局部晚期或转移性胃癌", "/胃食管结合部腺癌（GEJ）患者；b. 联", "合曲妥珠单抗、含氟嘧啶和含铂化疗，用", "于局部晚期不可切除或转移性 HER2 阳", "性胃癌或胃食管交界处（GEJ）腺癌患者", "的一线治疗；10. 食管癌：a. 单药用于", "经一种及以上全身治疗进展、PD-L1 CPS", "≥10 的复发性局部晚期或转移性食管鳞", "状细胞癌患者；b. 用于治疗局部晚期或", "转移性食管或胃食管交界处（GEJ）（震", "中在 GEJ 上方 1 至 5 厘米的肿瘤）癌患", "者，不适合手术切除或最终放化疗联合铂", "和氟嘧啶化疗；11. 宫颈癌：a. 单药用", "于化疗期间或之后进展、PD-L1 CPS≥1", "的复发或转移性宫颈癌患者；b. 加化疗，", "联合或不联合贝伐珠单抗，用于治疗肿瘤", "表达 PD-L1 的持续性，复发性或转移性", "宫颈癌患者（CPS ≥1）；12. 肝细胞癌", "(HCC)：单药用于索拉非尼治疗后进展", "的 HCC 患者；13. Merkel 细胞癌", "(MCC)：单药用于复发局部晚期或转", "移性 MCC 成人和儿童患者；14. 肾细胞", "癌：a. 帕博利珠单抗联合阿西替尼用于", "晚期肾细胞癌（RCC）患者的一线治疗；", "b. 联合 lenvatinib 用于晚期肾细胞癌", "(RCC) 成人患者的一线治疗；c. 用于", "肾切除术后或肾切除术和转移性病变切", "除术后复发风险为中高或高风险的 RCC", "患者的辅助治疗；15. 子宫内膜癌：联合", "lenvatinib 治疗非微卫星不稳定性高", "(MSI-H) 或错配修复缺陷 (dMMR)", "的晚期子宫内膜癌患者，他们在既往全身", "治疗后有疾病进展，不适合根治性手术或", "放疗；16. 膀胱癌：作为单药治疗卡介苗", "于既往接受过索拉非尼或含", "奥沙利铂化疗的肝细胞癌", "(HCC) 患者的治疗；7. 联", "合吉西他滨和顺铂用于局部", "晚期或转移性胆道癌 (BTC)", "患者的一线治疗；8. 联合化", "疗新辅助治疗并在手术后继", "续帕博利珠单抗单药辅助治", "疗，用于经充分验证的检测", "评估肿瘤表达 PD-L1（综合", "阳性评分（CPS）≥20）的", "早期高危三阴性乳腺癌", "(TNBC) 患者的治疗；9. 抗", "单药用于不可切除或转移性", "微卫星高度不稳定型", "(MSI-H) 或错配修复基因", "缺陷型 (dMMR) 成人晚期", "实体瘤患者：a. 既往接受过", "氟尿嘧啶类、奥沙利铂和伊", "立替康治疗后疾病进展的结", "直肠癌患者；b. 既往治疗后", "疾病进展且无满意替代治疗", "方案的其他实体瘤；10. 联", "合含氟尿嘧啶类和铂类药物", "化疗用于局部晚期不可切除", "或转移性 HER2-阴性胃或胃", "食管结合部腺癌患者的一线", "治疗。", "— 24 —", "上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com"]
2026-08-10 14:53:52,887 INFO     29 [qwen-vl-parser] page=41 text: 78 lines (bbox 2062-2139)
2026-08-10 14:53:52,887 INFO     29 [qwen-vl-parser] page=41 text: 78 sections
2026-08-10 14:53:52,984 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=700999, prompt_len=764
2026-08-10 14:53:55,948 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:53:55,948 INFO     29 [qwen-vl-parser] page=42 classify=text report_date=None
2026-08-10 14:53:55,958 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=700999, prompt_len=401
2026-08-10 14:54:03,447 INFO     29 [qwen-vl-parser] text API response (len=1474):
["奕检医学", "YIJIANMED LABORATORY", "YJ50430012T", "(BCG) 无反应、高风险、非肌肉浸润性", "膀胱癌 (NMIBC) 合并原位癌 (CIS) 伴", "或不伴乳头状肿瘤且不适合或选择不接", "受膀胱切除术的患者；17. 皮肤鳞状细胞", "癌：作为单药用于治疗无法通过手术或放", "疗治愈的复发性或转移性皮肤鳞状细胞", "癌 (cSCC) 患者；18. 用于治疗成人和", "儿童患者不可切除或转移性肿瘤突变负", "荷高 (TMB-H) [≥10 个突变/兆碱基", "(mut/Mb)] 实体瘤；19. 单药用于治", "疗无法切除或转移性的 MSI-H 或错配修", "复缺陷 (dMMR) 的成人和儿童患者，实", "体肿瘤经先前治疗进展、并且没有令人满", "意的替代治疗方案的实体瘤患者，氟尿嘧", "啶，奥沙利铂和伊立替康治疗后进展的结", "直肠癌，用于不可切除或转移性 MSI-H", "或 dMMR 结直肠癌患者的一线治疗（帕", "博利珠单抗 MSI-H 中枢神经系统肿瘤的", "儿童患者中的安全性和有效性尚未确定）；", "20. 用于治疗成人和儿童患者不可切除", "或转移性微卫星不稳定性高 (MSI-H) 或", "错配修复缺陷 (dMMR) 实体瘤。", "Ramucirumab", "雷莫西尤单抗", "雷莫西尤单抗", "(Ramucirumab) 是", "VEGFR-2 拮抗剂。", "NCCN 指南推荐雷莫", "西尤单抗作为单药或", "联合紫杉醇作为晚期", "或转移性胃腺癌患者", "二线或后续治疗的选", "择。转移性结直肠癌", "经贝伐珠单抗联合奥", "沙利铂和 5-Fu 一线治", "疗失败后，二线雷莫", "西尤单抗联合", "FOLFIRI 方案可以提", "供一定的临床获益。", "FDA 批准：1. 作为单药或与紫杉醇联合", "用于治疗铂或氟嘧啶一线化疗难治或进", "展的晚期胃癌或 EGJ 腺癌患者；2. 作为", "单药治疗甲胎蛋白 (AFP) ≥400 ng/mL", "且既往接受过索拉非尼治疗的肝细胞癌", "(HCC) 患者；3. 与厄洛替尼联合用于", "表皮生长因子受体 (EGFR) 19 号外显子", "缺失或 21 号外显子突变 (L858R) 的转", "移性非小细胞肺癌 (NSCLC) 的一线治", "疗。4. 联合多西他赛，用于治疗铂类化", "疗上或化疗后疾病进展的转移性非小细", "胞肺癌。对于 EGFR 或 ALK 基因异常的", "患者，在接受 CYRAMZA 治疗之前，FDA", "批准的针对 EGFR 或 ALK 基因异常的治", "疗应该有疾病进展。5. 与 FOLFIRI 联合，", "用于治疗在贝伐单抗、奥沙利铂和氟嘧啶", "治疗期间或之后疾病进展的转移性结直", "肠癌。", "NMPA 批准：1. 与紫杉醇", "联合用于在含氟尿嘧啶类或", "含铂类化疗期间或化疗后出", "现疾病进展的晚期胃或胃食", "管结合部腺癌患者的治疗；", "2. 用于既往接受过索拉非", "尼治疗且甲胎蛋白 (AFP) ≥", "400 ng/mL 的肝细胞癌", "(HCC) 患者的治疗。", "— 25 —", "上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com"]
2026-08-10 14:54:03,448 INFO     29 [qwen-vl-parser] page=42 text: 71 lines (bbox 2140-2210)
2026-08-10 14:54:03,448 INFO     29 [qwen-vl-parser] page=42 text: 71 sections
2026-08-10 14:54:03,524 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=497426, prompt_len=764
2026-08-10 14:54:04,890 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:54:04,890 INFO     29 [qwen-vl-parser] page=43 classify=text report_date=None
2026-08-10 14:54:04,907 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=497426, prompt_len=401
2026-08-10 14:54:10,151 INFO     29 [qwen-vl-parser] text API response (len=1084):
["奕检医学", "YIJIANMED LABORATORY", "YJ50430012T", "Dostarlimab-gxly", "Dostarlimab-gxly 是", "一种针对阴性免疫调", "节性人细胞表面受体", "程序性细胞死亡 1", "(PD-1;程序性死亡", "-1) 的人源化单克隆", "抗体，具有潜在的免", "疫检查点抑制和抗肿", "瘤活性。给药后，", "dostarlimab 结合并", "抑制 PD-1 及其下游", "信号通路。这可能通", "过激活 T 细胞来恢", "复免疫功能。PD-1 是", "一种在 T 细胞上表", "达的 Ig 超家族中的", "跨膜蛋白，当被其配", "体程序性细胞死亡受", "体配体 1 （PD-L1）", "或 2（PD-L2）激活", "时，它作为免疫检查", "点蛋白发挥作用，负", "向调节 T 细胞活化", "和 T 细胞介导的免", "疫反应；它在肿瘤逃", "避宿主免疫中起重要", "作用。", "FDA 批准：1. 用于治疗复发或晚期错配", "修复缺陷(dMMR)的成年患者：a. 经", "FDA 批准的试验确定的子宫内膜癌，在", "接受含铂方案治疗后或在接受含铂方案", "治疗后进展，不适合进行治疗性手术或放", "疗；b. 经 FDA 批准的试验确定的实体肿", "瘤，在之前的治疗中或之后已经进展，并", "且没有令人满意的替代治疗方案；2. 与", "卡铂和紫杉醇联合使用，随后作为单一药", "物用于治疗原发性晚期或复发性子宫内", "膜癌成年患者。", "无", "Ziv-aflibercept", "Ziv-aflibercept 是一", "种重组蛋白。", "Afilbercept 作为可", "溶性诱饵受体，与促", "血管生成血管内皮生", "长因子 （VEGF） 结", "合，从而阻止 VEGF", "与其内源性受体结", "合。破坏 VEGF 与其", "细胞受体的结合可能", "导致肿瘤血管生成、", "转移和最终肿瘤消退", "的抑制。", "FDA 批准：ziv-afliberept 与氟尿嘧啶,", "亚叶酸钙，伊立替康（FOLFIRI）联合使", "用，用于治疗奥沙利铂治疗方案耐药或进", "展的转移性结直肠癌（mCRC）患者。", "无", "— 26 —", "上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com"]
2026-08-10 14:54:10,151 INFO     29 [qwen-vl-parser] page=43 text: 64 lines (bbox 2211-2274)
2026-08-10 14:54:10,151 INFO     29 [qwen-vl-parser] page=43 text: 64 sections
2026-08-10 14:54:10,239 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=595190, prompt_len=764
2026-08-10 14:54:11,587 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:54:11,588 INFO     29 [qwen-vl-parser] page=44 classify=text report_date=None
2026-08-10 14:54:11,604 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=595190, prompt_len=401
2026-08-10 14:54:18,129 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:54:18.129+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 64, "failed": 0, "current": {"7630dbd094ca11f1bd9827cf206dfa2d": {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:54:18,433 INFO     29 [qwen-vl-parser] text API response (len=2123):
["奕检医学", "YIJIANMED LABORATORY", "YJ50430012T", "参考文献", "临床指南与共识", "1) NCCN Guideline: Colon Cancer (Version: 5.2024).", "2) NCCN Guideline: Rectal Cancer (Version: 4.2024).", "3) A framework to rank genomic alterations as targets for cancer precision medicine: the ESMO Scale", "for Clinical Actionability of molecular Targets (ESCAT). PMID: 30137196.", "4) Recommendations for the use of next-generation sequencing (NGS) for patients with advanced", "cancer in 2024: a report from the ESMO Precision Medicine Working Group. PMID: 38834388.", "5) A Canadian guideline on the use of next-generation sequencing in oncology. Curr Oncol. PMID:", "31043833.", "6) Therapeutic landscape and future direction of metastatic colorectal cancer. PMID: 36670267.", "7) Targeting BRAF and RAS in Colorectal Cancer. PMID: 34063682.", "8) BRAF and KRAS mutations in metastatic colorectal cancer: future perspectives for personalized", "therapy. PMID: 32665851.", "9) RAS genes in colorectal carcinoma: pathogenesis, testing guidelines and treatment implications.", "PMID: 30425122.", "10) BRAF Mutated Colorectal Cancer: New Treatment Approaches. PMID: 32545884.", "11) Exploring the best treatment options for BRAF-mutant metastatic colon cancer. PMID: 31353365.", "12) Mismatch repair deficiency testing in colorectal cancer and factors associated with nonadherence", "to guidelines. https://doi.org/10.1200/JCO.2020.38.15_suppl.e16069.", "13) Molecular and clinical characteristics of POLE/POLD1 alterations among patients with colorectal", "cancer. https://doi.org/10.1200/JCO.2024.42.3_suppl.184.", "14) 中国临床肿瘤学会 (CSCO) 结直肠癌诊疗指南 2024.", "15) 中国临床肿瘤学会 (CSCO) 免疫检查点抑制剂临床应用指南 2024.", "16) 中国临床肿瘤学会 (CSCO) 免疫检查点抑制剂相关的毒性管理指南 2023.", "17) 《肿瘤二代测序临床报告解读共识》, 循证医学 2022 年第 22 卷第 2 期.", "18) 《ctDNA 高通量测序临床实践专家共识 (2022 年版)》, 中国癌症防治杂志 2022 年 6 月第 14 卷第 3 期.", "19) 《二代测序技术在肿瘤精准医学诊断中的应用专家共识 (2018)》,中华医学杂志 2018 年 7 月 10 日第 98", "卷第 26 期.", "20) 《结直肠癌分子标志物临床检测中国专家共识》, 中华胃肠外科杂志 2021 年 3 月第 24 卷第 3 期.", "21) 《结直肠癌分子检测高通量测序中国专家共识》, 临床肿瘤学杂志 2021 年 3 月第 26 卷第 3 期.", "— 27 —", "上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com"]
2026-08-10 14:54:18,435 INFO     29 [qwen-vl-parser] page=44 text: 36 lines (bbox 2275-2310)
2026-08-10 14:54:18,435 INFO     29 [qwen-vl-parser] page=44 text: 36 sections
2026-08-10 14:54:18,435 INFO     29 [qwen-vl-parser] parse_pdf done: 2311 sections from 44 pages.
2026-08-10 14:54:18,455 INFO     29 Close text detector.
2026-08-10 14:54:18,865 INFO     29 Close text recognizer.
2026-08-10 14:54:19,280 INFO     29 Close recognizer.
2026-08-10 14:54:19,703 INFO     29 Close recognizer.
2026-08-10 14:54:20,564 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 14:54:20,564 INFO     29 [Trace] task=7630dbd0 | doc=YXHU  62  男  直肠癌肺转移  贵州(2).pdf | Parser:MedLink | outputs={"html": "", "json": "2311 items", "markdown": "", "text": "", "name": "YXHU  62  男  直肠癌肺转移  贵州(2).pdf", "output_format": "json"}
2026-08-10 14:54:20,564 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 14:54:20,607 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:54:20,607 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] YXHU 62 男 直肠癌肺转移 贵州\n[BBOX-1] KRAS 基因突变\\MWYC 基因扩增\\APC 基因突变\n[BBOX-2] 2021 年直肠癌？保肛服用中药\n[BBOX-3] 2025.05-2025.09 奥沙利铂+亚叶酸钙+氟尿嘧啶+贝伐珠单抗 5 周期 26.01pd\n[BBOX-4] 2026.02.07 贝伐珠单抗\n[BBOX-5] 病理诊断报告\n[BBOX-6] 病理号:\n[BBOX-7] 名:\n[BBOX-8] 性 别: 男\n[BBOX-9] 年龄: 62岁\n[BBOX-10] 收到日期: 2025-08-1\n[BBOX-11] 医院:\n[BBOX-12] 送检科室:\n[BBOX-13] 送检医生:\n[BBOX-14] 号:\n[BBOX-15] 床 号:\n[BBOX-16] 门诊号:\n[BBOX-17] 临床诊断: 直肠、肛管新生物并狭窄\n[BBOX-18] 肉眼所见:\n[BBOX-19] 直肠、肛管新生物: 灰白色组织多粒, 约0.1-0.2cm, 全。\n[BBOX-20] 镜下所见:\n[BBOX-21] 病理诊断:\n[BBOX-22] (直肠、肛管新生物) 恶性肿瘤, 建议行免疫组化进一步协助检查。\n[BBOX-23] 报告医\n[BBOX-24] 审核医师\n[BBOX-25] 报告日期: 2025-08-14 11:05:\n[BBOX-26] 须经诊断医师签字方能生效。\n[BBOX-27] 仅反映本次送检样本情况, 若有疑问, 请及时与病理科联系。\n[BBOX-28] 3:29\n[BBOX-29] 5G\n[BBOX-30] 5G\n[BBOX-31] 59\n[BBOX-32] <\n[BBOX-33] 报告详情\n[BBOX-34] 检查\n[BBOX-35] 盆腔CT*\n[BBOX-36] 姓名\n[BBOX-37] 男63岁\n[BBOX-38] 检查时间\n[BBOX-39] 2026-02-23 11:37:59\n[BBOX-40] 影像所见\n[BBOX-41] 对比2026-02-15盆腔CT平扫：阑尾未见增\n[BBOX-42] 粗。直肠下段管壁增厚，浆膜面稍毛糙，直肠\n[BBOX-43] 周围可见肿大淋巴结，较大者大小约\n[BBOX-44] 8mm×5mm。盆腔左份及左侧会阴区见条片状\n[BBOX-45] 低密度影，范围较前缩小，边界不清，其内可\n[BBOX-46] 见引流管影。腹腔未见明显积液及游离气体。\n[BBOX-47] 腹腔及腹膜后未见明显增大淋巴结。腹主动脉\n[BBOX-48] 及双侧髂总动脉壁见斑片状高密度影。腰椎椎\n[BBOX-49] 体边缘变尖。\n[BBOX-50] 诊断意见\n[BBOX-51] 1.直肠下段Ca，累及浆膜面，盆腔多发肿大淋\n[BBOX-52] 巴结，请结合临床及MRI检查。2.盆腔左份及\n[BBOX-53] 左侧会阴区脓肿引流术后，脓肿较前吸收。3.\n[BBOX-54] 前列腺钙化灶。4.腹主动脉及双侧髂总动脉粥\n[BBOX-55] 样硬化。5.腰椎退行性变。\n[BBOX-56] 3:30\n[BBOX-57] 5G\n[BBOX-58] 5G\n[BBOX-59] 59\n[BBOX-60] <\n[BBOX-61] 报告详情\n[BBOX-62] 检查\n[BBOX-63] 盆腔CT平扫+增强*\n[BBOX-64] 姓名\n[BBOX-65] 男63岁\n[BBOX-66] 检查时间\n[BBOX-67] 2026-02-08 14:55:00\n[BBOX-68] 影像所见\n[BBOX-69] 对比2026-01-09腹部增强：阑尾未见增粗。直\n[BBOX-70] 肠下段管壁增厚，增强扫描不均匀强化，浆膜\n[BBOX-71] 面稍毛糙，周围可见淋巴结显示，较大者大小\n[BBOX-72] 约8mm×5mm。盆腔左份及左侧会阴区见不规\n[BBOX-73] 则团片状密度增高影，局部呈囊性改变，病灶\n[BBOX-74] 边界欠清晰，较大截面大小约\n[BBOX-75] 70mm×34mm×95mm（前后径×左右径×上下\n[BBOX-76] 径），其内见小气泡影，周围脂肪间隙模糊，\n[BBOX-77] 增强病灶边缘轻度强化，病灶与左侧前列腺、\n[BBOX-78] 精囊腺分界欠清晰，前列腺可见结节状高密度\n[BBOX-79] 影。腹腔未见明显积液及游离气体。腹腔及腹\n[BBOX-80] 膜后未见明显增大淋巴结。腹主动脉及双侧髂\n[BBOX-81] 总动脉壁见斑片状高密度影。腰椎椎体边缘变\n[BBOX-82] 尖。\n[BBOX-83] 诊断意见\n[BBOX-84] 1.直肠下段Ca，累及浆膜面，盆腔多发淋巴\n[BBOX-85] 结，请结合临床及MRI检查。2.考虑盆腔左份\n[BBOX-86] 及左侧会阴区脓肿形成，请结合临床并复查。\n[BBOX-87] 3.前列腺钙化灶。4.腹主动脉及双侧髂总动脉\n[BBOX-88] 粥样硬化。5.腰椎退行性变。\n[BBOX-89] 3:30\n[BBOX-90] 5G\n[BBOX-91] 5G\n[BBOX-92] 59\n[BBOX-93] <\n[BBOX-94] 报告详情\n[BBOX-95] 姓名\n[BBOX-96] 男63岁\n[BBOX-97] 检查时间\n[BBOX-98] 2026-02-05 17:02:53\n[BBOX-99] 影像所见\n[BBOX-100] 对比2026-01-09胸部CT平扫：双肺透亮度增\n[BBOX-101] 高，可见多发囊状透亮影；左肺上叶舌段可见\n[BBOX-102] 两处肿块影，CT值约37-53Hu，分叶状，边界\n[BBOX-103] 清晰，较前稍扩大，较大者大小约\n[BBOX-104] 45mm×38mm×47mm（上下径×左右径×前后\n[BBOX-105] 径），密度不均，其内见结节状高密度影；左\n[BBOX-106] 肺上叶及双肺下叶可见实性结节，较大者位于\n[BBOX-107] 右肺下叶外基底段（IM216），大小约\n[BBOX-108] 11mm×9mm，略呈分叶状；右肺上叶可见结\n[BBOX-109] 节状高密度灶。气管内斑片状密度增高影此次\n[BBOX-110] 未见显示。双肺下叶近胸膜处见絮状密度增高\n[BBOX-111] 影，肺门影不大。纵隔无明显偏移，其内淋巴\n[BBOX-112] 结不大。心脏大小、形态未见明显异常，心腔\n[BBOX-113] 密度减低，主动脉壁见斑片状高密度影，双侧\n[BBOX-114] 胸腔未见积液。肋骨骨质结构未见异常。胸椎\n[BBOX-115] 椎体边缘变尖。\n[BBOX-116] 诊断意见\n[BBOX-117] 1.肺气肿伴双肺多发肺大疱，请结合肺功能检\n[BBOX-118] 查。2.左肺上叶舌段结节及肿块，具恶性征\n[BBOX-119] 象。3.左肺上叶及双肺下叶实性结节，建议随\n[BBOX-120] 诊；右肺上叶钙化灶。4.双肺下叶坠积效应，\n[BBOX-121] 建议复查。5.气管黏液栓较前未见确切显示。\n[BBOX-122] 6.贫血征象，请结合实验室检查；主动脉粥样\n[BBOX-123] 硬化。7.胸椎退行性变。（第1-4、6、7条较前\n[BBOX-124] 大致相仿）\n[BBOX-125] 4:11\n[BBOX-126] 5G\n[BBOX-127] 5G\n[BBOX-128] 29\n[BBOX-129] <\n[BBOX-130] 报告详情\n[BBOX-131] 姓名\n[BBOX-132] 男 63岁\n[BBOX-133] 检查时间\n[BBOX-134] 2026-01-09 11:07:00\n[BBOX-135] 影像所见\n[BBOX-136] 对比2025-04-14上腹部CT平扫+增强及对比\n[BBOX-137] 2025-04-02下腹部CT平扫+增强：肝脏形\n[BBOX-138] 态、大小未见明显异常；肝内见多枚类圆形低\n[BBOX-139] 密度无强化灶，边界清晰，较大者位于S3，直\n[BBOX-140] 径约13mm；肝内胆管无明显扩张。肝门区结\n[BBOX-141] 构清晰。胆囊不大，壁不厚，腔内未见异常密\n[BBOX-142] 度影。胃、肠管未充盈。胰腺、脾脏及双侧肾\n[BBOX-143] 上腺形态、大小及密度未见明显异常双肾实质\n[BBOX-144] 大小、形态未见异常，双肾可见囊状低密度无\n[BBOX-145] 强化灶，较大者位于左肾，直径约9mm；双侧\n[BBOX-146] 肾盂、肾盏未见扩张。阑尾未见增粗。直肠下\n[BBOX-147] 段管壁增厚，增强扫描不均匀强化，浆膜面稍\n[BBOX-148] 毛糙，周围可见多发淋巴结显示，较大者大小\n[BBOX-149] 约8mm×5mm。前列腺可见结节状高密度影。\n[BBOX-150] 腹腔未见明显积液及游离气体。腹腔及腹膜后\n[BBOX-151] 未见明显增大淋巴结。腹主动脉及双侧髂总动\n[BBOX-152] 脉壁见斑片状高密度影。腰椎椎体边缘变尖。\n[BBOX-153] 诊断意见\n[BBOX-154] 1.直肠下段病变，Ca可能，较前进展，周围多\n[BBOX-155] 发淋巴结，较前稍增多、增大。2.肝内多发囊\n[BBOX-156] 肿。3.双肾周多发渗出，较前已吸收，请结合\n[BBOX-157] 临床。4.双肾多发囊肿。5.考虑升结肠、盲肠\n[BBOX-158] 炎伴周围炎性渗出，较前已吸收。6.前列腺钙\n[BBOX-159] 化灶。7.右侧会阴部积气较前已吸收，请结合\n[BBOX-160] 临床。8.腹主动脉及双侧髂总动脉粥样硬化。\n[BBOX-161] 9.腰椎退行性变。\n[BBOX-162] 4:11\n[BBOX-163] 5G\n[BBOX-164] 5G\n[BBOX-165] 29\n[BBOX-166] <\n[BBOX-167] 报告详情\n[BBOX-168] 姓名\n[BBOX-169] 男63岁\n[BBOX-170] 检查时间\n[BBOX-171] 2026-01-09 09:32:00\n[BBOX-172] 影像所见\n[BBOX-173] 对比2025-08-11胸部CT平扫：双肺透亮度增\n[BBOX-174] 高，可见多发囊状透亮影；左肺上叶舌段可见\n[BBOX-175] 两处肿块影，CT值约22-61Hu，分叶状，边界\n[BBOX-176] 清晰，较前稍扩大，较大者大小约\n[BBOX-177] 45mm×36mm×42mm（上下径×左右径×前后\n[BBOX-178] 径），密度不均，其内见结节状高密度影；左\n[BBOX-179] 肺上叶及双肺下叶可见实性结节，较大者位于\n[BBOX-180] 右肺下叶，直径约7mm；右肺上叶可见结节状\n[BBOX-181] 高密度灶。新增气管内斑片状密度增高影。双\n[BBOX-182] 肺下叶近胸膜处见絮状密度增高影，肺门影不\n[BBOX-183] 大。纵隔无明显偏移，其内淋巴结不大。心脏\n[BBOX-184] 大小、形态未见明显异常，心腔密度减低，主\n[BBOX-185] 动脉壁见斑片状高密度影，上腔静脉内导管影\n[BBOX-186] 此次未见显示。双侧胸腔未见积液。肋骨骨质\n[BBOX-187] 结构未见异常。胸椎椎体边缘变尖。\n[BBOX-188] 诊断意见\n[BBOX-189] 1.肺气肿伴双肺多发肺大疱，请结合肺功能检\n[BBOX-190] 查。2.左肺上叶舌段结节及肿块，具恶性征\n[BBOX-191] 象，较前增大。3.左肺上叶及双肺下叶实性结\n[BBOX-192] 节，右肺中叶实性结节较前未见确切显示，建\n[BBOX-193] 议随诊；右肺上叶钙化灶。4.新增双肺下叶坠\n[BBOX-194] 积效应，建议复查。5.新增气管黏液栓。6.贫\n[BBOX-195] 血征象，请结合实验室检查；主动脉粥样硬\n[BBOX-196] 化。7.胸椎退行性变。8.PICC管较前未见确切\n[BBOX-197] 显示。\n[BBOX-198] 4:19\n[BBOX-199] 5G\n[BBOX-200] 5G\n[BBOX-201] 27\n[BBOX-202] <\n[BBOX-203] 报告详情\n[BBOX-204] 检查\n[BBOX-205] 胸部CT平扫+三维重建\n[BBOX-206] 姓名\n[BBOX-207] 男 63岁\n[BBOX-208] 检查时间\n[BBOX-209] 2025-06-21 17:57:05\n[BBOX-210] 影像所见\n[BBOX-211] 对比2025-05-26胸部CT平扫：双肺透亮度增高，可见多发囊状透亮影；左肺上叶舌段可见\n[BBOX-212] 两处肿块影，CT值约33-57Hu，分叶状，边界\n[BBOX-213] 清晰，较大者大小约47mm×35mm×43mm\n[BBOX-214] （上下径×左右径×前后径）；左肺下叶后基底\n[BBOX-215] 段、右肺中叶内侧段、右肺下叶外基底段可见\n[BBOX-216] 实性结节，较大者位于右肺下叶，直径约\n[BBOX-217] 6mm；右肺上叶可见结节状高密度灶。气管内\n[BBOX-218] 斑片状密度增高影未见显示。肺门影不大。纵\n[BBOX-219] 隔无明显偏移，其内淋巴结不大。心脏大小、\n[BBOX-220] 形态未见明显异常，心腔密度减低，主动脉壁\n[BBOX-221] 见斑片状高密度影，上腔静脉内见导管影。双\n[BBOX-222] 侧胸腔未见积液。肋骨骨质结构未见异常。胸\n[BBOX-223] 椎椎体边缘变尖。\n[BBOX-224] 诊断意见\n[BBOX-225] 1.肺气肿伴双肺多发肺大疱，请结合肺功能检\n[BBOX-226] 查。2.左肺上叶舌段肿块，具恶性征象，建议\n[BBOX-227] 复查。3.右肺中叶、双肺下叶实性结节，建议\n[BBOX-228] 随诊；右肺上叶钙化灶。4.贫血征象，请结合\n[BBOX-229] 实验室检查；主动脉粥样硬化。5.胸椎退行性\n[BBOX-230] 变。6.PICC管置入术后。（上述1-5条较前大\n[BBOX-231] 致相仿）\n[BBOX-232] 出院记录\n[BBOX-233] 姓名：\n[BBOX-234] 科室：\n[BBOX-235] 住院号：\n[BBOX-236] 姓名：\n[BBOX-237] 职业：自由职业\n[BBOX-238] 性别：男\n[BBOX-239] 入院日期：2026-2-5 10:14\n[BBOX-240] 年龄：63岁\n[BBOX-241] 出院日期：2026-2-26 10:25\n[BBOX-242] 民族：汉族\n[BBOX-243] 住院天数：21天\n[BBOX-244] 籍贯：\n[BBOX-245] 科 室：\n[BBOX-246] 入院情况：\n[BBOX-247] 患者男，63岁，因“诊断直肠癌肺转移7+月”入院；既往史：4+年前因“大便不成形伴血\n[BBOX-248] 便”就诊于外院，考虑为“直肠癌”，未明确诊断，自行服用中药治疗；10+月前因“阴囊脓肿”于\n[BBOX-249] 我院局麻下行“阴囊下部脓肿切开引流术”，病理结果回示：“阴囊内容物”检材大部分为变性坏\n[BBOX-250] 死组织，区域见大量中性粒细胞浸润。予换药、抗感染等对症治疗后好转。专科情况：全身皮肤粘\n[BBOX-251] 膜无黄染、出血点及瘀斑，全身浅表淋巴结未扪及肿大，胸廓对称无畸形，肋间隙无明显增宽及凹\n[BBOX-252] 陷，胸骨无压痛，双肺叩诊呈清音，双肺呼吸音粗，双肺可闻及散在湿啰音。腹平软，全腹未见腹\n[BBOX-253] 部静脉曲张、蜘蛛痣，未见胃肠型蠕动波。全腹无压痛、反跳痛及肌紧张，肝脾肋下未扪及，莫菲\n[BBOX-254] 氏征阴性，移动性浊音阴性，双肾区无叩击痛，肠鸣音约4次/分，阴囊及肛周皮肤正常，未见红\n[BBOX-255] 肿、破溃，肛周6点钟方向可扪及一约2*3cm大小包块，质韧，挤压时无明显脓液，肛门括约肌张力\n[BBOX-256] 正常，于直肠距肛门约7cm处可扪及环状肿物，质地硬，表面凹凸不平，活动度差，退出指套可见血\n[BBOX-257] 染。（患者取左侧卧位）辅助检查：病理（病理号：2502456）：“左肺占位”恶性肿瘤，符合腺\n[BBOX-258] 癌，结合免疫组化结果及临床病史考虑肠道来源。ALK（-）、CD56（-）、CDX-2（+）、CK20\n[BBOX-259] (+）、CK5/6（-）、CK7（局灶弱+）、Ki-67（30%+）、Napsin-A（-）、P40(-)、P53（突变\n[BBOX-260] 型）、P63(-)、SATB2(+)、Syn（-）、TTF-1（+）、CK(AE1/AE3)（+）、Vimentin（-）、Villin\n[BBOX-261] (+）。基因检测：1.KRAS基因突变；2.MYC基因扩增；3.APC基因突变。胸部CT（本院 2026-01-\n[BBOX-262] 08）：1.肺气肿伴双肺多发肺大疱；2.左肺上叶舌段结节及肿块，具恶性征象，较前增大；3.左肺上\n[BBOX-263] 叶及双肺下叶实性结节，右肺中叶实性结节较前未见确切显示，右肺上叶钙化灶；4.新增双肺下叶\n[BBOX-264] 坠积效应；5.新增气管黏液栓；6.贫血征象，主动脉粥样硬化；7.胸椎退行性变；8.PICC管较前未\n[BBOX-265] 见确切显示。全腹+盆腔增强CT（本院 2026-01-08）：1.直肠下段病变，Ca可能，较前进展，周围\n[BBOX-266] 多发淋巴结，较前稍增多、增大；2.肝内多发囊肿；3.双肾周多发渗出，较前已吸收；4.双肾多发\n[BBOX-267] 囊肿；5.考虑升结肠、盲肠炎伴周围炎性渗出，较前已吸收；6.前列腺钙化灶；7.右侧会阴部积气\n[BBOX-268] 较前已吸收；8.腹主动脉及双侧髂总动脉粥样硬化。9.腰椎退行性变。\n[BBOX-269] 入院诊断：1.直肠腺癌 ycT4bN2M1 IV期（肺转移）；2.肺气肿伴双肺肺大疱；3.混合\n[BBOX-270] 痔；4.肝囊肿；5.双肺结节；6.双肺细菌性肺炎。\n[BBOX-271] 第1页\n[BBOX-272] 出院记录\n[BBOX-273] 姓名：\n[BBOX-274] 科室：\n[BBOX-275] 住院号：\n[BBOX-276] 诊疗经过：患者入院后积极完善相关辅助检查，血常规：中性粒细胞绝对值10.57*10^\n[BBOX-277] 9/L，血红蛋白128.00g/L，红细胞比积38.80%，白细胞计数12.28*10^9/L，C反应蛋\n[BBOX-278] 白101.75mg/L。DIC全套：纤维蛋白原检测9.1g/L。大便潜血：阳性。肿瘤标记物：\n[BBOX-279] 癌胚抗原6.84ng/mL，糖类抗原72427.95U/mL。血生化、心肌标记物及心肌酶谱均未\n[BBOX-280] 见明显异常。结合患者病史、体征及相关辅助检查，考虑患者直肠癌肺转移较前进展，\n[BBOX-281] 因患者且合并远处转移，无法行根治性手术切除原发病灶及转移病灶，故建议患者行\n[BBOX-282] “支气管、肋间、胸廓内外动脉+肠道动脉灌注化疗栓塞术”，提高患者生存周期并改\n[BBOX-283] 善患者生质量，但患者因自身原因拒绝行介入手术治疗，并要求继续使用贝伐珠单抗靶\n[BBOX-284] 向治疗及对症止痛。但因患者目前疗效评估为PD，结合患者原免疫组化，考虑化疗药物\n[BBOX-285] 可能对肿瘤细胞形态及抗原表达产生影响，从而发生免疫组化结果改变，故建议患者再\n[BBOX-286] 次行肠镜检查取病理活检明确免疫组化情况，必要时再次行基因检测指导抗肿瘤药物选\n[BBOX-287] 择。患者及家属拒绝行病理活检，要求暂使用贝伐珠单抗靶向治疗，向患者告知可能因\n[BBOX-288] 免疫组化改变发���耐药，但患者家属仍坚持要求继续使用贝伐珠单抗。后予患者完善盆\n[BBOX-289] 腔MRI平扫，盆腔MRI示：1.直肠下段Ca，累及浆膜面，盆腔多发肿大淋巴结；2.盆腔左\n[BBOX-290] 份脓肿（大小约106×38×29mm）可能；3.骨盆骨质疏松征象。阅片可见患者盆腔左份\n[BBOX-291] 及左侧会阴区见不规则团片状密度增高影，部分呈囊状改变，因病灶范围大与周围临近\n[BBOX-292] 器官组织分界欠清，压迫症状明显，故建议患者行脓肿穿刺置管引流术，缓解压迫症\n[BBOX-293] 状。且阅片可见患者直肠肿瘤较前增大已明显侵犯浆膜面，患者目前已出血肛门坠胀及\n[BBOX-294] 排便困难等症状，考虑为肿瘤进展后体积增大，阻塞肠腔所致，故建议患者可行直肠球\n[BBOX-295] 囊扩张、支架置入或姑息性造瘘术以改善排便困难症状，避免因肠管狭窄出现肠梗阻危\n[BBOX-296] 及生命，向患者及家属交代患者目前病情及后续治疗后，患者及家属表示理解，同意行\n[BBOX-297] 脓肿穿刺引流，但拒绝行直肠球囊扩张、支架置入及姑息性造瘘术，故排除手术禁忌后\n[BBOX-298] 于2026年2月8日在局麻下行“经CT引导下盆腔脓肿穿刺置管引流术”，手术过程顺利，\n[BBOX-299] 术后继予患者抗感染、抑酸护胃等对症支持治疗，后患者肛周皮肤出现破溃流脓，考虑\n[BBOX-300] 为直肠肿瘤进展后肿瘤直接浸润肠壁全层及穿透至肛周组织，导致局部组织坏死流出，\n[BBOX-301] 出现肛周皮肤破溃伴流脓，予患者盐水冲洗创面及加强换药，保持引流通畅，促进创面\n[BBOX-302] 愈合，经治疗患者创面渗出较前已明显减少，但为避免窦道形成，仍建议患者尽快行外\n[BBOX-303] 科手术治疗，患者及家属表示理解，并要求转院行外科手术治疗，请示上级医师后同意\n[BBOX-304] 第2页\n[BBOX-305] 出院记录\n[BBOX-306] 姓名：\n[BBOX-307] 科室：\n[BBOX-308] 住院号：\n[BBOX-309] 予患者签署自请出院协议后今日出院。\n[BBOX-310] 手术：经CT引导下盐腔脓肿穿刺置管引流术 2026-02-08\n[BBOX-311] 出院情况：患者诉创面渗出较前已明显减少，无恶心、呕吐，无咳嗽、咳痰，无胸痛。\n[BBOX-312] 胸闷、气促、呼吸困难，无腹胀、腹痛，无畏寒、发热等不适，精神、饮食、睡眠尚\n[BBOX-313] 可，小便黄清，大便同前。查体：全身浅表淋巴结未扪及肿大，胸廓对称无畸形，肋间\n[BBOX-314] 隙无明显增宽及凹陷，胸骨无压痛，双肺叩诊呈清音，双肺呼吸音粗，双肺可闻及散在\n[BBOX-315] 湿啰音。腹平软，全腹未见腹部静脉曲张、蜘蛛痣，未见胃肠型蠕动波。全腹无压痛、\n[BBOX-316] 反跳痛及肌紧张，肝脾肋下未扪及，莫菲氏征阴性，移动性浊音阴性，双肾区无叩击\n[BBOX-317] 痛，肠鸣音约4次/分，阴囊皮肤正常，未见红肿、破溃，肛周6点钟方向可见一大小约2\n[BBOX-318] ×1cm不规则皮肤缺损，创面基底呈暗红色可见少量白色脓苔附着，可见少量灰白色恶\n[BBOX-319] 臭味脓性分泌物流出。肛门括约肌张力正常，于直肠距肛门约7cm处可扪及环状肿物，\n[BBOX-320] 质地硬，表面凹凸不平，活动度差，退出指套可见血染。左侧臀部引流管引流通畅，可\n[BBOX-321] 见暗灰色脓性分泌物引出，量约10ml。（患者取左侧卧位）\n[BBOX-322] 出院诊断：1.直肠腺癌 ycT4bN2M1 IV期（肺转移）；2.肺气肿伴双肺肺大疱；3.混合\n[BBOX-323] 痔；4.肝囊肿；5.双肺结节；6.双肺细菌性肺炎；7.轻度贫血；8.盆腔脓肿；9.肛周脓\n[BBOX-324] 肿。\n[BBOX-325] 出院医嘱：院外继续治疗。\n[BBOX-326] 康复指导：嘱患者适当活动，禁忌久卧、久坐，避免深静脉血栓形成\n[BBOX-327] 医生坐诊信息\n[BBOX-328] 医生签名：\n[BBOX-329] 2026-2-26\n[BBOX-330] 第3页\n[BBOX-331] 出院记录\n[BBOX-332] 姓名：\n[BBOX-333] 科室：\n[BBOX-334] 住院号：\n[BBOX-335] 姓名：\n[BBOX-336] 职业：自由职业\n[BBOX-337] 性别：男\n[BBOX-338] 入院日期：2025-7-8 09:23\n[BBOX-339] 年龄：62岁\n[BBOX-340] 出院日期：2025-7-14 10:00\n[BBOX-341] 民族：汉族\n[BBOX-342] 住院天数：6天\n[BBOX-343] 籍贯：\n[BBOX-344] 科 室：\n[BBOX-345] 入院情况：\n[BBOX-346] 患者 男，62岁，因“发现左肺占位3+月，诊断肠道肿瘤肺转移2+月”入院；患者3+月前因\n[BBOX-347] 胸闷就诊于我院，行胸部CT提示：左肺上叶舌段周围型肺癌可能性大。后排除手术禁忌后于2025年4\n[BBOX-348] 月16日行“肺穿刺活检”，病理结果提示：“左肺占位”恶性肿瘤，符合腺癌，结合免疫组化结果及\n[BBOX-349] 临床病史考虑肠道来源。P53（突变型）、Syn（-）、TTF-1（+）、P63(-)、CK(AE1/AE3)\n[BBOX-350] (+)、Vimentin（-）、Villin（+）、CK7（局灶弱+）、CD56（-）、ALK（-）、Napsin-\n[BBOX-351] A（-）、P40(-)、CDX-2（+）、CK20（+）、Ki-67（30%+）、SATB2(+)、PCK5/6（-）。基因检测：\n[BBOX-352] 1.KRAS基因突变；2.MYC基因扩增；3.APC基因突变。因患者为肠道肿瘤晚期且合并肺转移，可予患者\n[BBOX-353] 行姑息性治疗，提高患者生存期，故排除化疗禁忌后于2025年5月12日至2025年6月22日完成1-3周期\n[BBOX-354] “FOLFOX+贝伐珠单抗”（奥沙利铂150mg+亚叶酸钙600mg+氟尿嘧啶4500mg+贝伐珠单抗400mg）\n[BBOX-355] 联合治疗，现患者为按计划行下一周期治疗入院，门诊遂以“肠道肿瘤肺转移”收入我科。既往史：\n[BBOX-356] 3+年前因“大便不成形伴血便”就诊于外院，考虑为“直肠癌”，未明确诊断，自行服用中药治疗；\n[BBOX-357] 2+月前因“阴囊脓肿”于我院局麻下行“阴囊下部脓肿切开引流术”，病理结果回示：“阴囊内容\n[BBOX-358] 物”检材大部分为变性坏死组织，区域见大量中性粒细胞浸润。予换药、抗感染等对症治疗后好转。\n[BBOX-359] 专科情况：腹平软，全腹未见腹部静脉曲张、蜘蛛痣，未见胃肠型蠕动波。全腹无压痛、反跳痛及肌\n[BBOX-360] 紧张，肝脾肋下未扪及，莫菲氏征阴性，移动性浊音阴性，双肾区无叩击痛，肠鸣音约4次/分，阴囊\n[BBOX-361] 及肛周皮肤正常，未见红肿、破溃，肛周可扪及一约1*1cm大小包块，质韧，挤压时无明显脓液。辅\n[BBOX-362] 助检查：病理（病理号：2502456）：“左肺占位”恶性肿瘤，符合腺癌，结合免疫组化结果及临床\n[BBOX-363] 病史考虑肠道来源。CD56（-）、CDX-2（+）、CK7（局灶弱+）、ALK（-）、Ki-67（30%\n[BBOX-364] +）、P63(-)、SATB2(+)、CK20（+）、CK5/6（-）、Napsin-A（-）、P40(-)、P53（突变\n[BBOX-365] 型）、Syn（-）、TTF-1（+）、CK(AE1/AE3)（+）、Vimentin（-）、Villin（+）。基因检测：\n[BBOX-366] 1.KRAS基因突变；2.MYC基因扩增；3.APC基因突变。\n[BBOX-367] 入院诊断：1.姑息性化疗；2.肠道肿瘤肺转移（T4bNxM1 IVa期）；3.肺气肿伴双肺肺大\n[BBOX-368] 疱；4.混合痔；5.肝囊肿；6.双肺结节。\n[BBOX-369] 诊疗经过：患者入院后积极完善相关辅助检查，血常规：中性粒细胞绝对值1.05*10\n[BBOX-370] 第1页\n[BBOX-371] 出院记录\n[BBOX-372] 姓名：\n[BBOX-373] 科室：\n[BBOX-374] 住院号\n[BBOX-375] 9/L↓，血红蛋白123.00g/L↓，白细胞计数3.16*10^9/L↓。肝肾功、电解质、心肌标\n[BBOX-376] 记物及心肌酶谱均未见明显异常。入院时患者血常规提示白细胞稍低，考虑为化疗后骨\n[BBOX-377] 髓抑制，予患者人粒细胞刺激因子对症治疗后复查血常规未见明显异常。因患者为肠道\n[BBOX-378] 肿瘤晚期且合并肺转移，治疗方式以全身治疗为主的姑息治疗，以延长生命，改善生活\n[BBOX-379] 质量为目的，目前患者已于我科完成3个周期“FOLFOX+贝伐珠单抗”方案治疗，查体可\n[BBOX-380] 见阴囊处皮肤缺损已愈合，肛周肿块较前缩小，行局部疗效评估为PR，后续可继续该方\n[BBOX-381] 案治疗，故排除化疗禁忌后于2025年7月9日至2025年7月13日行第4周期“FOLFOX+贝伐珠\n[BBOX-382] 单抗”（奥沙利铂150mg+亚叶酸钙600mg+氟尿嘧啶4500mg+贝伐珠单抗400mg）方案\n[BBOX-383] 治疗，患者化疗期间出现消化道反应，予止吐、抑酸等对症支持治疗后，消化道症状明\n[BBOX-384] 显好转，复查血常规未见明显骨髓抑制，目前我科已无特殊治疗，请示上级医师后同意\n[BBOX-385] 予患者今日出院。\n[BBOX-386] 手术：无\n[BBOX-387] 出院情况：患者无恶心、呕吐，未诉心慌、胸闷、气促、呼吸困难，无畏寒、发热，无\n[BBOX-388] 腹胀、腹泻等特殊不适；精神、睡眠、饮食尚可，二便如常。查体：生命征平稳，一般\n[BBOX-389] 情况可。心肺腹查体无特殊，专科查体同前。\n[BBOX-390] 出院诊断：1.姑息性化疗；2.肠道肿瘤肺转移（T4bNxM1 IVa期）；3.肺气肿伴双肺肺\n[BBOX-391] 大疱；4.混合痔；5.肝囊肿；6.双肺结节；7.化疗后骨髓抑制。\n[BBOX-392] 出院医嘱：1.注意休息，多饮水，避免剧烈活动，注意加强营养；2.动态监测血常规\n[BBOX-393] （每周查血常规2次），监测肝功能每周1次，若有异常，及时就诊；3.间隔3周返院按计\n[BBOX-394] 划行下一周期化疗；4.若出现畏寒、发热、乏力、心慌、胸闷等不适立即返院就诊；5.\n[BBOX-395] 耳鼻喉科门诊随诊；6.不适我科随诊。\n[BBOX-396] 康复指导：嘱患者适当活动，禁忌久卧\n[BBOX-397] 医生签名：\n[BBOX-398] 2025-7-14\n[BBOX-399] 第2页\n[BBOX-400] \\begin{tabular}{llll}\n[BBOX-401] 报告时间: 2026-02-19\n[BBOX-402] \\hline\n[BBOX-403] 项目 & 结果 & 参考范围 & \\\\\n[BBOX-404] \\hline\n[BBOX-405] 白细胞计数 & 9.23 & 3.90-9.50/10~9/L & \\\\\n[BBOX-406] 中性粒细胞百分率 & 70.50 & 40.00-75.00/\\% & \\\\\n[BBOX-407] 淋巴细胞百分率 & 18.60 $\\downarrow$ & 20.00-50.00/\\% & \\\\\n[BBOX-408] 单核细胞百分率 & 6.90 & 3.00-10.00/\\% & \\\\\n[BBOX-409] 嗜酸性粒细胞百分率 & 3.30 & 0.40-8.00/\\% & \\\\\n[BBOX-410] 嗜碱性粒细胞百分率 & 0.70 $\\uparrow$ & 0.02-0.52/\\% & \\\\\n[BBOX-411] 大的未染色细胞计数 & 0.03 & 0.00-0.40/10~9/L & \\\\\n[BBOX-412] 中性粒细胞绝对值 & 6.51 $\\uparrow$ & 1.80-6.30/10~9/L & \\\\\n[BBOX-413] 淋巴细胞绝对值 & 1.72 & 1.10-3.20/10~9/L & \\\\\n[BBOX-414] 单核细胞绝对值 & 0.64 $\\uparrow$ & 0.10-0.60/10~9/L & \\\\\n[BBOX-415] 嗜酸性粒细胞绝对值 & 0.30 & 0.02-0.52/10~9/L & \\\\\n[BBOX-416] \\hline\n[BBOX-417] \\end{tabular}\n[BBOX-418] \\begin{tabular}{llll}\n[BBOX-419] 报告时间: 2026-02-19\n[BBOX-420] \\hline\n[BBOX-421] 项目 & 结果 & 参考范围 & \\\\\n[BBOX-422] \\hline\n[BBOX-423] 嗜碱性粒细胞绝对值 & 0.06 & 0.02-0.06/10~9/L & \\\\\n[BBOX-424] 大的未染色细胞百分率 & 0.30 & 0.00-4.00/\\% & \\\\\n[BBOX-425] 红细胞计数 & 4.34 & 4.30-5.80/10~12/L & \\\\\n[BBOX-426] 血红蛋白 & 125.00 $\\downarrow$ & 130.00-175.00/g/L & \\\\\n[BBOX-427] 红细胞比积 & 38.60 $\\downarrow$ & 40.00-50.00/\\% & \\\\\n[BBOX-428] 红细胞平均体积 & 88.90 & 82.00-100.00/fl & \\\\\n[BBOX-429] 红细胞平均血红蛋白量 & 28.70 & 27.00-34.00/pg & \\\\\n[BBOX-430] 红细胞平均血红蛋白浓度 & 324.00 & 316.00-354.00/g/L & \\\\\n[BBOX-431] 红细胞体积分布宽度变异系数 & 14.30 & 12.00-16.00/\\% & \\\\\n[BBOX-432] 红细胞体积分布宽度标准差 & 44.90 & 35.00-56.00/fl & \\\\\n[BBOX-433] 血小板计数 & 458.00 $\\uparrow$ & 125.00-350.00/10~9/L & \\\\\n[BBOX-434] 血小板平均体积 & 7.10 $\\downarrow$ & 8.30-17.40/fl & \\\\\n[BBOX-435] C反应蛋白 & 18.29 $\\uparrow$ & 0.00-10.00/mg/L & \\\\\n[BBOX-436] \\hline\n[BBOX-437] \\end{tabular}\n[BBOX-438] \\begin{tabular}{lll}\n[BBOX-439] 报告时间: 2026-02-05\n[BBOX-440] \\hline\n[BBOX-441] 检查日期 & 2026-02-05 11:52:00 & \\\\\n[BBOX-442] \\hline\n[BBOX-443] \\multicolumn{3}{l}{\\textbf{指标结果}} \\\\\n[BBOX-444] 项目 & 结果 & 参考范围 \\\\\n[BBOX-445] 谷丙转氨酶 & 15.40 & 9.00-60.00/U/L \\\\\n[BBOX-446] 谷草转氨酶 & 18.50 & 15.00-45.00/U/L \\\\\n[BBOX-447] 谷草/谷丙 & 1.20 & 0.80-1.40 \\\\\n[BBOX-448] 总胆红素 & 11.90 & 3.40-17.10/μmol/L \\\\\n[BBOX-449] 直接胆红素 & 5.00 \\text{↑} & 0.00-4.00/μmol/L \\\\\n[BBOX-450] 间接胆红素 & 6.90 & 3.00-17.00/μmol/L \\\\\n[BBOX-451] 总蛋白 & 69.800 & 65.000-80.000/g/L \\\\\n[BBOX-452] 白蛋白 & 40.50 & 40.00-55.00/g/L \\\\\n[BBOX-453] 碱性磷酸酶 & 87.00 & 45.00-125.00/U/L \\\\\n[BBOX-454] γ-谷氨酰基转移酶 & 32.00 & 10.00-60.00/U/L \\\\\n[BBOX-455] 总胆汁酸 & 6.47 & 0.00-9.67/μmol/L \\\\\n[BBOX-456] 尿素 & 5.40 & 3.00-9.20/mmol/L \\\\\n[BBOX-457] 肌酐 & 96.00 & 59.00-104.00/μmol/L \\\\\n[BBOX-458] \\hline\n[BBOX-459] \\end{tabular}\n[BBOX-460] \\begin{tabular}{lll}\n[BBOX-461] 报告时间: 2026-02-05\n[BBOX-462] \\hline\n[BBOX-463] 肌酐 & 96.00 & 59.00-104.00/μmol/L \\\\\n[BBOX-464] 尿素/肌酐 & 0.06 & 0.03-0.20 \\\\\n[BBOX-465] 尿酸 & 248.00 & 208.00-428.00/μmol/L \\\\\n[BBOX-466] 葡萄糖 & 7.28 \\text{↑} & 3.90-6.10/mmol/L \\\\\n[BBOX-467] 钾 & 3.92 & 3.50-5.50/mmol/L \\\\\n[BBOX-468] 钠 & 141.60 & 135.00-145.00/mmol/L \\\\\n[BBOX-469] 氯 & 102.90 & 96.00-108.00/mmol/L \\\\\n[BBOX-470] 钙 & 2.22 & 2.10-2.60/mmol/L \\\\\n[BBOX-471] 镁 & 0.85 & 0.73-1.35/mmol/L \\\\\n[BBOX-472] 磷 & 0.98 & 0.78-1.65/mmol/L \\\\\n[BBOX-473] 前白蛋白 & 110.00 \\text{↓} & 200.00-400.00/mg/L \\\\\n[BBOX-474] 胆碱酯酶 & 5602.00 & 4600.00-11500.00/U/L \\\\\n[BBOX-475] 白蛋白/球蛋白 & 1.38 & 1.20-2.40 \\\\\n[BBOX-476] 球蛋白 & 29.30 & 20.00-40.00/g/L \\\\\n[BBOX-477] \\hline\n[BBOX-478] \\end{tabular}\n[BBOX-479] \\begin{tabular}{l c c}\n[BBOX-480] 报告时间: 2026-02-05\n[BBOX-481] \\hline\n[BBOX-482] 项目 & 结果 & 参考范围 \\\\\n[BBOX-483] \\hline\n[BBOX-484] 凝血酶原时间检测. & 13.3 & 9.8-14.3/s \\\\\n[BBOX-485] 活动度. & 86.4 & 70.0-150.0/\\% \\\\\n[BBOX-486] 国际标准化比值. & 1.2 & 0.5-1.5 \\\\\n[BBOX-487] 活化部分凝血活酶时间检测. & 30.0 & 20.0-36.9/S \\\\\n[BBOX-488] 纤维蛋白原检测. & 9.1 $\\uparrow$ & 2.0-4.0/g/L \\\\\n[BBOX-489] 凝血酶时间检测. & 16.8 & 14.4-23.4/s \\\\\n[BBOX-490] D-D二聚体检测. & 0.6 & 0.0-0.6/ug/ml \\\\\n[BBOX-491] 纤维蛋白（原）降解产物检测. & 4.5 & 0.0-5.0/ug/ml \\\\\n[BBOX-492] \\hline\n[BBOX-493] \\end{tabular}\n[BBOX-494] \\begin{tabular}{l c c}\n[BBOX-495] 报告时间: 2026-02-05\n[BBOX-496] \\hline\n[BBOX-497] 项目 & 结果 & 参考范围 \\\\\n[BBOX-498] \\hline\n[BBOX-499] 糖类抗原125 & 6.46 & 0.00-24.00/U/ml \\\\\n[BBOX-500] 糖类抗原199 & 8.34 & 0.00-30.00/U/ml \\\\\n[BBOX-501] 糖类抗原153 & 11.70 & 0.00-24.00/U/ml \\\\\n[BBOX-502] 糖类抗原724 & 8.43 $\\uparrow$ & 0.00-6.90/U/ml \\\\\n[BBOX-503] 糖类抗原242 & 8.77 & 0.00-20.00/U/ml \\\\\n[BBOX-504] 总前列腺特异性抗原 & 1.12 & 0.00-4.00/ng/ml \\\\\n[BBOX-505] FPSA/TPSA & 16.96 $\\downarrow$ & 25.00-100.00/\\% \\\\\n[BBOX-506] 神经元特异性烯醇化酶 & 12.00 & 0.00-17.00/ng/ml \\\\\n[BBOX-507] 细胞角蛋白19片段 & 4.07 $\\uparrow$ & 0.00-3.30/ng/ml \\\\\n[BBOX-508] 鳞状细胞癌抗原 & 1.66 & 0.50-3.00/ng/ml \\\\\n[BBOX-509] 甲胎蛋白 & 4.18 & 0.00-7.00/ng/mL \\\\\n[BBOX-510] 癌胚抗原 & 5.27 $\\uparrow$ & 0.00-5.00/ng/mL \\\\\n[BBOX-511] 铁蛋白 & 47.50 & 30.00-400.00/ng/ml \\\\\n[BBOX-512] \\hline\n[BBOX-513] \\end{tabular}\n[BBOX-514] \\begin{tabular}{l c c}\n[BBOX-515] 报告时间: 2026-02-05\n[BBOX-516] \\hline\n[BBOX-517] 项目 & 结果 & 参考范围 \\\\\n[BBOX-518] \\hline\n[BBOX-519] 肌红蛋白 & 28.530 & 28.000-72.000/ng/ml \\\\\n[BBOX-520] 高敏肌钙蛋白T & 0.012 & 0.000-0.014/ng/ml \\\\\n[BBOX-521] \\hline\n[BBOX-522] \\end{tabular}\n[BBOX-523] 3:34\n[BBOX-524] 5G\n[BBOX-525] 5G\n[BBOX-526] 58\n[BBOX-527] <\n[BBOX-528] 报告详情\n[BBOX-529] 检查\n[BBOX-530] 常规心电图\n[BBOX-531] 姓名\n[BBOX-532] 男 63岁\n[BBOX-533] 检查时间\n[BBOX-534] 2026-02-05 11:17:16\n[BBOX-535] 诊断意见\n[BBOX-536] 1.窦性心律2.正常范围心电图\n[BBOX-537] 报告文件\n[BBOX-538] 预览 >\n[BBOX-539] 基因检测报告单\n[BBOX-540] 姓名\n[BBOX-541] 年龄：62\n[BBOX-542] 性别：男\n[BBOX-543] 样本编号\n[BBOX-544] 样本类型：白片\n[BBOX-545] 送检医生：\n[BBOX-546] 接收日期：2025-04-30\n[BBOX-547] 报告日期：2025-05-05\n[BBOX-548] 临床诊断：肠癌肺转移\n[BBOX-549] 检测技术：NGS\n[BBOX-550] 备注：\n[BBOX-551] 项目名称：\n[BBOX-552] 本次检测概览\n[BBOX-553] 检测内容\n[BBOX-554] 本产品包含40个与结直肠癌发生、发展相关的基因，其中涵盖NCCN指南中的KRAS、BRAF、NRAS、ERBB2等重要基\n[BBOX-555] 因，以及MLH1、MSH2、MSH6、PMS2、POLE等与PD-1/PD-L1免疫治疗相关基因，同时，还涵盖与化疗药物毒副作用、疗效相关基因。在采用二代测序技术对这些基因进行深度测序后，根据检出的基因状态，为患者的个体化临床治疗方案\n[BBOX-556] 制定提供可靠的参考依据。\n[BBOX-557] 小结\n[BBOX-558] 体细胞突变\n[BBOX-559] 2\n[BBOX-560] 拷贝数变异\n[BBOX-561] 1\n[BBOX-562] 融合变异\n[BBOX-563] 未检出\n[BBOX-564] 微卫星不稳定状态（MSI）\n[BBOX-565] 微卫星稳定（MSS）\n[BBOX-566] 错配修复基因胚系突变（MMR）\n[BBOX-567] 未检出\n[BBOX-568] 化疗药物\n[BBOX-569] 详情见化疗位点及相关药物反应结果\n[BBOX-570] 用药相关基因变异及其临床意义\n[BBOX-571] 变异\n[BBOX-572] 提示敏感\n[BBOX-573] 提示耐药\n[BBOX-574] 潜在获益的药物\n[BBOX-575] 变异分类\n[BBOX-576] KRAS\n[BBOX-577] 2 号外显子\n[BBOX-578] 错义突变\n[BBOX-579] c.34G>A\n[BBOX-580] p.G12S\n[BBOX-581] 丰度 = 41.62%\n[BBOX-582] Panitumumab (A 级)\n[BBOX-583] Tucatinib + 曲妥珠单抗 (A 级)\n[BBOX-584] 西妥昔单抗 (A 级)\n[BBOX-585] Cobimetinib (D 级 实体瘤; C 级 朗格汉斯细胞组织细胞增多症、埃尔德海姆-\n[BBOX-586] 切斯特病、罗-道病)\n[BBOX-587] 曲美替尼 (D 级 实体瘤; C 级 朗格汉斯细胞组织细胞增多症、埃尔德海姆-切斯特病、罗-道病)\n[BBOX-588] Binimetinib (D 级 实体瘤)\n[BBOX-589] RMC-6236 (D 级 实体瘤)\n[BBOX-590] I 类\n[BBOX-591] MYC\n[BBOX-592] 拷贝数扩增\n[BBOX-593] CN=3.42\n[BBOX-594] Benzosertib (C 级 实体瘤)\n[BBOX-595] BMS-986158 (D 级 实体瘤)\n[BBOX-596] II 类\n[BBOX-597] 注:\n[BBOX-598] 1. 药物分级依据参考《二代测序临床报告解读指引》以及 2017 年 AMP/ASCO/CAP 联合制定的体细胞变异解读指南:\n[BBOX-599] A 级, 美国食品药品监督管理局 (Food and Drug Administration, FDA) , 以及中国国家药品监督管理局 (National Medical Products\n[BBOX-600] Administration, NMPA) 批准或 NCCN、CSCO、ASCO、ESMO 等专业临床指南推荐;\n[BBOX-601] B 级, 经具有足够统计学效能的临床研究证实、获得该领域专家共识;\n[BBOX-602] C 级, 其他癌种中的 A 级证据 (跨适应证用药) 、或已作为临床试验的入组标准;\n[BBOX-603] D 级, 临床病例报道或临床前证据支持。\n[BBOX-604] 2. 提示敏感的药物来源于 NMPA/FDA 批准或肿瘤临床指南, 以及临床专家达成共识的较大规模临床研究结果 (A 级, B 级) 。\n[BBOX-605] 3. 提示耐药的药物来源于该肿瘤类型 NMPA/FDA 批准或肿瘤临床指南, 及相关文献或临床试验报道。\n[BBOX-606] 4. 潜在获益的药物来源于该肿瘤类型相关文献或临床试验报道, 以及在其他肿瘤类型中已获批的药物 (C 级, D 级) 。\n[BBOX-607] 5. 报告中相同分级药物间先后顺序与优先推荐无关, 按首字母排序列出。\n[BBOX-608] 6. 按照变异的治疗、预后和诊断等临床意义, 体细胞变异分类为: I 类 (A 级、B 级证据) , II 类 (C 级、D 级证据) , III 类 (临床意义未明的变异) , IV 类 (可能无害或无害的变异, 本报告中不予列出) ; 胚系变异分类为: 致病性, 可能致病性, 意义未明, 可能良性 (本报告中不予列出) , 良性 (本报告中不予列出) 。\n[BBOX-609] NCCN 指南推荐相关基因变异结果\n[BBOX-610] 基因\n[BBOX-611] 变异类型\n[BBOX-612] 变异结果\n[BBOX-613] 丰度\n[BBOX-614] KRAS\n[BBOX-615] 错义突变\n[BBOX-616] c.34G>A(p.G12S)\n[BBOX-617] 41.62%\n[BBOX-618] BRAF\n[BBOX-619] 未检出\n[BBOX-620] NRAS\n[BBOX-621] 未检出\n[BBOX-622] 注:\n[BBOX-623] 1. KRAS、NRAS 和 BRAF 基因的突变与结直肠癌等癌症患者对 EGFR 单抗类药物(西妥昔单抗或帕尼单抗)的耐药有关，但这些基因野生型的患者能从此类药物的治疗中获益。欧洲药监局和美国 FDA 也明确规定了在使用靶向药物西妥昔单抗或帕尼单抗治疗转移性大肠癌前必须检测 KRAS 基因。(NCCN Guideline: Colon (Rectal) Cancer v.1.2023; FDA Druglabel:panitumumab;FDA Druglabel:cetuximab)。\n[BBOX-624] 2. KRAS 基因检测覆盖但不仅限于 G12, G13, Q61, A59, K117, A146 等变异。\n[BBOX-625] 3. BRAF 基因检测覆盖但不仅限于 V600E, G469A/V, G442S, G464V, Y472C, N581S, D594G, L597V/S, K601E 等变异。\n[BBOX-626] 4. NRAS 基因检测覆盖但不仅限于 G12, G13, Q61, A59, A146 等变异。\n[BBOX-627] 其他非用药相关变异\n[BBOX-628] 基因\n[BBOX-629] 外显子\n[BBOX-630] 变异类型\n[BBOX-631] 变异结果\n[BBOX-632] 丰度/基因型\n[BBOX-633] 变异分类\n[BBOX-634] APC\n[BBOX-635] 16\n[BBOX-636] 移码突变\n[BBOX-637] c.4257_4263del(p.S1419fs)\n[BBOX-638] 40.08%\n[BBOX-639] Ⅲ类\n[BBOX-640] 注:\n[BBOX-641] 1. 突变类型：错义突变（missense）、同义突变（synonymous mutation）、非移码插入突变（insertion）、非移码缺失突变（deletion）、移码突变（frameshift）、剪切突变（splice_variant）、起始密码子丢失（start_lost）、无义突变（nonsense）等。\n[BBOX-642] 2. 体细胞突变又称获得性突变，是在生长发育过程中或者环境因素影响下后天获得的突变，通常身上只有部分细胞带有体细胞突变，如癌症组织会出现致病性的突变。此外同义突变因氨基酸不发生改变故未列出。\n[BBOX-643] 3. 胚系变异又称生殖细胞变异，是来源于精子或卵子这些生殖细胞的变异，因此通常身上所有细胞都带有这种变异；这其中绝大多数胚系变异并不致病，构成了人与人之间的遗传多态性，只有少数变异会致病，特别是一些遗传类的疾病。如移码突变、无义突变等，该类可能导致疾病产生的变异结果会在本部分内容中列出。\n[BBOX-644] 微卫星不稳定性（MSI）检测\n[BBOX-645] 本次检测结果\n[BBOX-646] 微卫星稳定（MSS）\n[BBOX-647] 注:\n[BBOX-648] 1. 微卫星不稳定（MSI-H）的患者，可能对 PD-1/PD-L1 等相关免疫疗法敏感。\n[BBOX-649] 2. FDA 已经批准 PD-1 抗体 Keytruda 用于 MSI-H 或者 dMMR 类型的多种实体瘤。\n[BBOX-650] 3. PD-1/PD-L1 抑制剂药物主要有： 可瑞达（Pembrolizumab），欧狄沃（Nivolumab），泰圣奇（Atezolizumab），达伯舒（Sintilimab），百泽安（Tislelizumab），艾瑞卡（Camrelizumab），Imfinzi（Durvalumab），Bavencio（Avelumab）等。\n[BBOX-651] 4. NCCN 指南建议对于 MSI-H 或 MMR 任一蛋白缺失患者，推荐进一步的 MMR 基因胚系突变检测辅助 Lynch 综合征的诊断。\n[BBOX-652] 错配修复基因胚系突变（MMR）\n[BBOX-653] 基因\n[BBOX-654] 变异类型\n[BBOX-655] 变异结果\n[BBOX-656] 基因型\n[BBOX-657] 致病性\n[BBOX-658] EPCAM\n[BBOX-659] 未检出\n[BBOX-660] MLH1\n[BBOX-661] 未检出\n[BBOX-662] MSH2\n[BBOX-663] 未检出\n[BBOX-664] MSH6\n[BBOX-665] 未检出\n[BBOX-666] PMS2\n[BBOX-667] 未检出\n[BBOX-668] 注:\n[BBOX-669] 奕检医学\n[BBOX-670] YIJIANMED LABORATORY\n[BBOX-671] YJ50430012T\n[BBOX-672] 1. 错配修复 (MMR) 基因包含 EPCAM、MLH1、MSH2、MSH6、PMS2 等基因，这些基因突变会导致错配修复基因功能丧失 (dMMR)，如果\n[BBOX-673] 没有发生基因突变，则为正常 (pMMR)。dMMR 导致 MSI-H，但是 MSI-H 的人不一定 dMMR。\n[BBOX-674] 2. 检测 MMR 的必要性如下：(1)辅助临床评判 MSI-H 发生的原因；(2) MMR 基因的胚系突变还与 Lynch 综合征相关，如需进一步判断是否为\n[BBOX-675] Lynch 综合征还需要结合病史、家族史等具体情况补充其他基因检测进行辅助诊断；(3)预测肿瘤患者能否从抗 PD-1 中获益。\n[BBOX-676] 3. 胚系变异通常会按 ACMG (American College of Medical Genetics and Genomics) 相关指南，分为 “致病性”、“可能致病性”、“意义未\n[BBOX-677] 明”、“可能良性”、“良性”五类。本部分结果只列出“致病性”、“可能致病性”突变。\n[BBOX-678] 基因拷贝数结果\n[BBOX-679] 基因\n[BBOX-680] 染色体位置\n[BBOX-681] 拷贝数变异\n[BBOX-682] MYC\n[BBOX-683] chr8\n[BBOX-684] CN=3.42\n[BBOX-685] BRAF\n[BBOX-686] chr7\n[BBOX-687] 未检出\n[BBOX-688] EGFR\n[BBOX-689] chr7\n[BBOX-690] 未检出\n[BBOX-691] ERBB2\n[BBOX-692] chr17\n[BBOX-693] 未检出\n[BBOX-694] FGFR1\n[BBOX-695] chr8\n[BBOX-696] 未检出\n[BBOX-697] FGFR2\n[BBOX-698] chr10\n[BBOX-699] 未检出\n[BBOX-700] FGFR3\n[BBOX-701] chr4\n[BBOX-702] 未检出\n[BBOX-703] KRAS\n[BBOX-704] chr12\n[BBOX-705] 未检出\n[BBOX-706] MDM2\n[BBOX-707] chr12\n[BBOX-708] 未检出\n[BBOX-709] NTRK1\n[BBOX-710] chr1\n[BBOX-711] 未检出\n[BBOX-712] PIK3CA\n[BBOX-713] chr3\n[BBOX-714] 未检出\n[BBOX-715] 注：\n[BBOX-716] 1. 本报告包含以上重要基因的拷贝数变异，但不仅限于以上基因。\n[BBOX-717] 2. 正常细胞的 DNA 可能稀释变异细胞中的 DNA 拷贝数，所以报告中的拷贝数为样本中细胞的平均拷贝数。\n[BBOX-718] 3. 常染色体中基因的正常拷贝数为 2，拷贝数变异为该基因的拷贝数发生改变，CN>2 的拷贝数变异为基因发生扩增，CN<2 的拷贝数变异为基因\n[BBOX-719] 发生缺失。\n[BBOX-720] 融合基因结果\n[BBOX-721] 检测基因\n[BBOX-722] 检测结果\n[BBOX-723] 丰度\n[BBOX-724] RET\n[BBOX-725] 未检出\n[BBOX-726] NTRK3\n[BBOX-727] 未检出\n[BBOX-728] NTRK2\n[BBOX-729] 未检出\n[BBOX-730] NTRK1\n[BBOX-731] 未检出\n[BBOX-732] 注：本报告包含以上重要基因的融合变异，但不仅限于以上基因。\n[BBOX-733] 多靶点药物治疗方案\n[BBOX-734] 癌种\n[BBOX-735] NMPA/FDA/\n[BBOX-736] 指南推荐药物\n[BBOX-737] 治疗方案选择\n[BBOX-738] 药物机制\n[BBOX-739] 使用范围\n[BBOX-740] 结直肠癌\n[BBOX-741] 5-FU + 亚叶酸钙\n[BBOX-742] + 贝伐珠单抗\n[BBOX-743] 初始治疗\n[BBOX-744] 化疗+抗血管生成\n[BBOX-745] 晚期/转移性结直肠癌\n[BBOX-746] FOLFIRI/伊立替康\n[BBOX-747] + 贝伐珠单抗（首选）\n[BBOX-748] 初始/后续治疗\n[BBOX-749] 化疗+抗血管生成\n[BBOX-750] 1、无法切除的异时性转移结直肠癌，过去12个月用了FOLFOX/CAPEOX辅助治疗；2、先前接受奥沙利铂治疗而未接受过伊立替康治疗的晚期/转移性结直肠癌；3、先前接受氟尿嘧啶治疗而未接受过伊立替康/奥沙利铂治疗的晚期/转移性结直肠癌\n[BBOX-751] FOLFOX/CAPEO\n[BBOX-752] X + 贝伐珠单抗\n[BBOX-753] 后续治疗\n[BBOX-754] 化疗+抗血管生成\n[BBOX-755] 1、先前接受伊立替康治疗而未接受过奥沙利铂治疗的晚期/转移性结直肠癌；2、先前接受氟尿嘧啶治疗而未接受过伊立替康/奥沙利铂治疗的晚期/转移性结直肠癌\n[BBOX-756] FOLFOX/CAPEO\n[BBOX-757] X/FOLFIRI/FOLFOXIRI + 贝伐珠单抗\n[BBOX-758] 初始治疗\n[BBOX-759] 化疗+抗血管生成\n[BBOX-760] 晚期/转移性结直肠癌\n[BBOX-761] 伊立替康 + 奥沙利铂 + 贝伐珠单抗\n[BBOX-762] 后续治疗\n[BBOX-763] 化疗+抗血管生成\n[BBOX-764] 先前接受氟尿嘧啶治疗而未接受过伊立替康/奥沙利铂治疗的晚期/转移性结直肠癌\n[BBOX-765] 卡培他滨 + 贝伐珠单抗\n[BBOX-766] 初始治疗\n[BBOX-767] 化疗+抗血管生成\n[BBOX-768] 晚期/转移性结直肠癌\n[BBOX-769] 呋喹替尼\n[BBOX-770] 后续治疗\n[BBOX-771] 抗血管生成\n[BBOX-772] 适用于既往接受过氟尿嘧啶类、奥沙利铂和伊立替康为基础的化疗，以及既往接受过或不适合接受抗 VEGF 治疗、抗EGFR 治疗的 RAS 野生型转移性结直肠癌患者。\n[BBOX-773] 瑞戈非尼\n[BBOX-774] 后续治疗\n[BBOX-775] 抗血管生成\n[BBOX-776] 所有可用方案治疗后进展的晚期/转移性结直肠癌\n[BBOX-777] (FOLFIRI/伊立替康) + ziv-阿柏西普\n[BBOX-778] 初始/后续治疗\n[BBOX-779] 化疗+抗血管生成\n[BBOX-780] 1、无法切除的异时性转移结直肠癌，过去12个月用了FOLFOX/CAPEOX辅助治疗；2、先前接受奥沙利铂治疗而未接受过伊立替康治疗的晚期/转移性结直肠癌；3、先前接受氟尿嘧啶治疗而未接受过伊立替康/奥沙利铂治疗的晚期/转移性结直肠癌\n[BBOX-781] (FOLFIRI/伊立替康\n[BBOX-782] 初始/后续治疗\n[BBOX-783] 化疗+抗血管生成\n[BBOX-784] 1、无法切除的异时性转移结直肠癌，过\n[BBOX-785] 康）+ 雷莫西尤单\n[BBOX-786] 抗\n[BBOX-787] 去12个月用了FOLFOX/CAPEOX辅助\n[BBOX-788] 治疗；2、先前接受奥沙利铂治疗而未接\n[BBOX-789] 受过伊立替康治疗的晚期/转移性结直\n[BBOX-790] 肠癌；3、先前接受氟尿嘧啶治疗而未接\n[BBOX-791] 受过伊立替康/奥沙利铂治疗的晚期/转\n[BBOX-792] 移性结直肠癌\n[BBOX-793] 注：\n[BBOX-794] 1. 此处内容为 FDA/NMPA 获批，或指南推荐的药物治疗方案。\n[BBOX-795] 2. 该处呈现的治疗方案，旨在为患者的临床治疗提供更多参考信息，但并非该患者的个体化治疗方案。\n[BBOX-796] 3. 治疗方案的选择，请结合患者临床情况参照“使用范围”信息，并遵从临床医师的指导。\n[BBOX-797] 化疗药物相关基因检测结果\n[BBOX-798] 化疗药物\n[BBOX-799] 检测基因\n[BBOX-800] 检测位点\n[BBOX-801] 检测结果\n[BBOX-802] 用药提示\n[BBOX-803] 证据等级\n[BBOX-804] 紫杉醇类\n[BBOX-805] TP53\n[BBOX-806] rs1042522\n[BBOX-807] CG\n[BBOX-808] 药物疗效较好，毒副作用风险较高\n[BBOX-809] 3\n[BBOX-810] 伊立替康\n[BBOX-811] UGT1A1\n[BBOX-812] rs8175347\n[BBOX-813] (TA)6/(TA)7\n[BBOX-814] 毒副作用风险较高\n[BBOX-815] 1A\n[BBOX-816] rs4148323\n[BBOX-817] AG\n[BBOX-818] 毒副作用风险较高\n[BBOX-819] 1B\n[BBOX-820] 5-氟尿嘧啶\n[BBOX-821] DPYD\n[BBOX-822] rs55886062\n[BBOX-823] AA\n[BBOX-824] 毒副作用风险低\n[BBOX-825] 1A\n[BBOX-826] rs67376798\n[BBOX-827] TT\n[BBOX-828] 毒副作用风险低\n[BBOX-829] 1A\n[BBOX-830] rs3918290\n[BBOX-831] CC\n[BBOX-832] 毒副作用风险低\n[BBOX-833] 1A\n[BBOX-834] 卡培他滨\n[BBOX-835] DPYD\n[BBOX-836] rs67376798\n[BBOX-837] TT\n[BBOX-838] 毒副作用风险低\n[BBOX-839] 1A\n[BBOX-840] rs3918290\n[BBOX-841] CC\n[BBOX-842] 毒副作用风险低\n[BBOX-843] 1A\n[BBOX-844] 甲氨蝶呤\n[BBOX-845] MTHFR\n[BBOX-846] rs1801133\n[BBOX-847] AG\n[BBOX-848] 毒副作用风险较高\n[BBOX-849] 2A\n[BBOX-850] 注：\n[BBOX-851] 1. 所有检测基因均采用 NCBI-Gene 里的官方命名。\n[BBOX-852] 2. 检测位点均以 rs 号为准：NCBI 里对所有提交的 SNP 进行分类考证后，均会注册一个 rs 号，也称作参考 SNP。\n[BBOX-853] 3. 证据等级的划分：依据 PharmGKB 网站 http://www.pharmgkb.org/page/clinAnnLevels\n[BBOX-854] Level 1A：注释基于被医学会认可的指南或经某些重大卫生系统的认可；\n[BBOX-855] Level 1B：注释基于多项有统计显著的研究；\n[BBOX-856] Level 2A：注释基于多项重复研究，故药效关系很有可能是有意义的；\n[BBOX-857] Level 2B：注释基于多项重复研究，但某些研究可能无统计显著性或样本数量少；\n[BBOX-858] Level 3：注释仅基于 1 项有显著差异的研究（未重复）或多项研究但缺乏明显药效关联性。\n[BBOX-859] 4. 影响化疗药物效果的因素较多，如患者临床表现、���物相互作用、给药顺序、剂量差异等，以上检测结果可为化疗药物治疗方案制定提供参考，\n[BBOX-860] 具体用药还请遵循临床指南与医嘱。\n[BBOX-861] \\begin{tabular}{ccc}\n[BBOX-862] 报告时间: 2025-05-05\n[BBOX-863] \\hline\n[BBOX-864] \\textbf{质控项目} & \\textbf{质控结果} & \\textbf{质控标准} \\\\\n[BBOX-865] \\hline\n[BBOX-866] 样本量 & 合格 & >30 ng \\\\\n[BBOX-867] \\hline\n[BBOX-868] 预文库 & 合格 & >500 ng \\\\\n[BBOX-869] \\hline\n[BBOX-870] 靶向捕获 & 合格 & >10 ng \\\\\n[BBOX-871] \\hline\n[BBOX-872] 测序质量 & 0.953 & >0.8 \\\\\n[BBOX-873] \\hline\n[BBOX-874] 测序深度 & 795.20 & 组织样本$\\ge$500X; ctDNA$\\ge$5000X \\\\\n[BBOX-875] \\hline\n[BBOX-876] \\end{tabular}\n[BBOX-877] 奕检医学\n[BBOX-878] YIJIANMED LABORATORY\n[BBOX-879] YJ50430012T\n[BBOX-880] 附录\n[BBOX-881] 基因列表\n[BBOX-882] APC\n[BBOX-883] DPYD\n[BBOX-884] FGFR3\n[BBOX-885] MLH1\n[BBOX-886] NTRK1\n[BBOX-887] PTEN\n[BBOX-888] AKT1\n[BBOX-889] EGFR\n[BBOX-890] HRAS\n[BBOX-891] MSH2\n[BBOX-892] NTRK2\n[BBOX-893] RET\n[BBOX-894] ARID1A\n[BBOX-895] EPCAM\n[BBOX-896] KIT\n[BBOX-897] MSH6\n[BBOX-898] NTRK3\n[BBOX-899] SMAD4\n[BBOX-900] BRAF\n[BBOX-901] ERBB2\n[BBOX-902] KRAS\n[BBOX-903] MTHFR\n[BBOX-904] PDGFRA\n[BBOX-905] TP53\n[BBOX-906] CDH1\n[BBOX-907] FBXW7\n[BBOX-908] MAP2K1\n[BBOX-909] MUTYH\n[BBOX-910] PIK3CA\n[BBOX-911] UGT1A1\n[BBOX-912] CHEK2\n[BBOX-913] FGFR1\n[BBOX-914] MDM2\n[BBOX-915] MYC\n[BBOX-916] PMS2\n[BBOX-917] DDR2\n[BBOX-918] FGFR2\n[BBOX-919] MDM4\n[BBOX-920] NRAS\n[BBOX-921] POLE\n[BBOX-922] 检测方法与技术局限声明\n[BBOX-923] 1. 本检测中点突变与扩增相关基因覆盖了基因全部编码外显子区域，融合基因主要覆盖了常见断裂位点内含子区域，放化疗位点则为 SNP 位点。但由于基因组重复片段与高 GC 区域，导致探针并不能保证 100%（通常大于 98%）覆盖目标区域，存在一定区域探针难以覆盖导致少量罕见位点无法检出。\n[BBOX-924] 2. 本检测是临床诊断与用药决策的有效补充，并不能代替临床其他检测，具体治疗还需医生根据患者其他检测结果与患者病情进展情况做出方案。\n[BBOX-925] 3. 本检测的基因相关解读，主要依据 FDA/NMPA 批准的靶向药物、CSCO、ASCO、NCCN、ESMO 等相关指南，以及相关临床试验与相关临床案例等文献。随着新靶点药物的批准、指南的更新、临床研究的进展，报告内容和相关解读会随相关内容的更新而变化。\n[BBOX-926] 4. 基因点突变、融合基因、拷贝数变异的检出率与肿瘤细胞的含量密切相关，根据 CSCO 肿瘤诊断指南适合于 NGS 检测的组织标本中肿瘤细胞含量建议应达到 20%以上。如果肿瘤细胞占比较低，存在一定未检出的风险，另外 ctDNA 血液样本作为无法取得组织样本的必要补充，建议采血至少 10ml，保证充足的游离 DNA 用于 NGS 检测，如检测结果为阴性，后续如有组织样本，建议进行再次检测。\n[BBOX-927] 5. 未进行白细胞样本对照实验时，无法确认检出变异是否为胚系变异，报告中将以体细胞变异体现。\n[BBOX-928] — 8 —\n[BBOX-929] 上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n[BBOX-930] 奕检医学\n[BBOX-931] YIJIANMED LABORATORY\n[BBOX-932] YJ50430012T\n[BBOX-933] 变异解析\n[BBOX-934] 变异\n[BBOX-935] 变异解读\n[BBOX-936] KRAS\n[BBOX-937] 2 号外显子\n[BBOX-938] 错义突变\n[BBOX-939] c.34G>A\n[BBOX-940] p.G12S\n[BBOX-941] 丰度 = 41.62%\n[BBOX-942] I 类\n[BBOX-943] KRAS 基因第 2 号外显子第 12 位密码子编码的氨基酸由甘氨酸突变为丝氨酸。此变异在 ClinVar 数据库\n[BBOX-944] 中被记录为致病性变异。在 COSMIC 数据库中有 2075 次检出，其中 Large intestine cancer 有 1437\n[BBOX-945] 例，Lung cancer 有 223 例，Pancreas cancer 有 111 例。\n[BBOX-946] 根据 NMPA/FDA 批准、肿瘤临床指南、相关临床研究结果等，该变异对 Panitumumab (A 级)、Tucatinib\n[BBOX-947] + 曲妥珠单抗 (A 级) 、西妥昔单抗 (A 级) 等耐药，潜在获益药物为 Cobimetinib (D 级 实体瘤；C\n[BBOX-948] 级 朗格汉斯细胞组织细胞增多症、埃尔德海姆-切斯特病、罗-道病) 、曲美替尼 (D 级 实体瘤；C 级 朗\n[BBOX-949] 格汉斯细胞组织细胞增多症、埃尔德海姆-切斯特病、罗-道病) 、Binimetinib (D 级 实体瘤) 、RMC-6236\n[BBOX-950] (D 级 实体瘤) 等。\n[BBOX-951] KRAS 是小型 GTP 酶 RAS 家族的成员,该家族催化 GTP 水解为 GDP。在生理条件下,这些 RAS 蛋白\n[BBOX-952] 在活性(GTP 结合)和非活性(GDP 结合)状态之间循环,以激活受体酪氨酸激酶 (RTK)下游的 MAPK 和\n[BBOX-953] PI3K 致癌途径信号传导(PMID:22189424)。RAS 酶的功能受鸟嘌 呤核苷酸交换因子(GEF)如 SOS 的\n[BBOX-954] 调节,这些因子可以使 GDP 与 GTP 交换,也可以通过 GTP 酶活化蛋白如 NF1 调节,从而提高 RAS 水\n[BBOX-955] 解 GTP 的能力。一旦被激活,RAS 可通过激活不 同的细胞内信号传导途径(包括 RAF / MEK / ERK 和\n[BBOX-956] PI3K/AKT/ mTOR 途径)介导细胞增殖和其他细胞功能的调节。KRAS 中的转化突变常见于胰腺癌,结肠\n[BBOX-957] 癌,子宫内膜癌,卵巢癌和胆管癌;几乎所有这些突变都可导致 KRAS 的组成型活化,从而促进细胞增殖\n[BBOX-958] (PMID:21993244, 24651010)。 KRAS 突变主要发生在三个主要热点 G12,G13 和 Q61 上,前两个发\n[BBOX-959] 生在 GTP-ase 结构域,后者为干扰 NF1 结合和调节 KRAS 的能力(PMID: 22589270, 21993244,\n[BBOX-960] 24651010)。其他不太明确表征的突变如 A146T // P 和 L19F 也已被表征,而且发现较低频率下也可处\n[BBOX-961] 于活化状态(PMID:20147967, 20432530, 20570890)。种系 KRAS 突变可导致 Noonan 综合征(NS)\n[BBOX-962] 和心脏-皮肤-皮肤(CFC)综合征(PMID:16474405, 16474404, 19467855, 17056636),这些疾 病与过度\n[BBOX-963] 活化的 MAPK 途径,独特的临床特征和癌症易感性相关( PMID:19467855,17704260)。\n[BBOX-964] APC\n[BBOX-965] 16 号外显子\n[BBOX-966] 移码突变\n[BBOX-967] c.4257_4263del\n[BBOX-968] p.S1419fs\n[BBOX-969] 丰度 = 40.08%\n[BBOX-970] III 类\n[BBOX-971] APC 基因第 16 号外显子发生移码突变。\n[BBOX-972] APC 是参与 WNT 信号传导的肿瘤抑制基因(PMID: 8259518、8259519)。APC 的主要肿瘤抑制作用是\n[BBOX-973] 调节细胞内β-catenin 水平 (PMID: 11978510)。APC 是破坏复合物的重要成员，该复合物靶向胞质\n[BBOX-974] β-catenin 泛素化和降解(PMID: 10984057)。当 APC 活性丧失时，WNT 通路活性异常增强，往往导致\n[BBOX-975] 增生，最终导致肿瘤进展(PMID: 8259511)。抑制肿瘤形成需要一个 APC 表达的阈值，并且该水平达到\n[BBOX-976] 了很好的平衡(PMID: 11743581)。APC 基因的胚系突变导致家族腺瘤性息肉病(FAP) (PMID: 1651174,\n[BBOX-977] 1651562)， 95%的患者发展为结直肠癌(PMID: 1528264)。此外，APC 的可遗传变异导致许多相关疾\n[BBOX-978] 病的发生，包括 Turcot 综合征、Gardner 综合征和扁平腺瘤综合征(FAS) (PMID: 8593545)。在 50-80%\n[BBOX-979] 的散发性结直肠癌(PMID: 17143297)中观察到 APC 突变，与 FAS 中的突变很相似。APC 的体细胞突变\n[BBOX-980] 作为肿瘤发生启动事件，在包括乳腺癌、胃癌和前列腺癌在内的许多其他人类癌症中也可观察到(PMID:\n[BBOX-981] 27302369，29316426)。大多数 APC 突变是功能丧失型，主要发生在一个β-catenin 结合的重要区域\n[BBOX-982] (PMID: 10784639、1338904)。WNT 通路抑制剂目前正在临床研究中(PMID: 24981364)。\n[BBOX-983] MYC\n[BBOX-984] 拷贝数扩增\n[BBOX-985] CN=3.42\n[BBOX-986] II 类\n[BBOX-987] MYC 的拷贝数扩增变异。\n[BBOX-988] 根据 NMPA/FDA 批准、肿瘤临床指南、相关临床研究结果等，该变异潜在获益药物为 Berzosertib (C\n[BBOX-989] 级 实体瘤) 、BMS-986158 (D 级 实体瘤) 等。\n[BBOX-990] MYC 编码一个转录因子，该转录因子与蛋白质 MAX 异源二聚化以调控数千个基因的转录，调节参与多\n[BBOX-991] 种细胞过程（包括增殖，分化和凋亡）。 MYC 主要通过基因扩增在多种癌症中被激活。 MYC 通过诱\n[BBOX-992] 导增殖，抑制细胞周期停滞，刺激血管形成和增强基因组不稳定性来促进肿瘤发生 (PMID：\n[BBOX-993] — 9 —\n[BBOX-994] 上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n[BBOX-995] 奕检医学\n[BBOX-996] YIJIANMED LABORATORY\n[BBOX-997] YJ50430012T\n[BBOX-998] 22464321,10378696,16934487,19029958）。 MYC 在癌症中通过多种机制被激活，包括染色体易位\n[BBOX-999] (通常与血液肿瘤有关，并与组成型过表达有关) 以及基因组扩增和过表达 (PMID: 22446421)。 MYC\n[BBOX-1000] 基因发生突变，但频率低于扩增和易位。已知功能性突变位于 T58 残基附近，该残基是 MYC 上的一个\n[BBOX-1001] 磷酸化位点，对 MYC 蛋白的泛素化及其降解至关重要 (PMID: 10706881)。 MYC 基因家族由三个\n[BBOX-1002] 相关基因组成：（1）c-MYC（在此称为 MYC，由 MYC 基因编码），（2）N-MYC（由 MYCN 基因编\n[BBOX-1003] 码）和（3）L-MYC（由基因 MYCL1 编码）(PMID: 16934487)。 MYC 基因位于染色体基因座 8q24\n[BBOX-1004] 上，并包含几个不同的结构域，包括一个 N 端转录激活域，一个中央部分和一个 C 端 DNA 结合域，其\n[BBOX-1005] 中包含一个基本的螺旋-环-螺旋亮氨酸拉链二级结构域。在这些域中有五个“Myc-boxs”区域，在多个\n[BBOX-1006] 物种的 MYC 家族蛋白中高度保守 (PMID: 19029958)。\n[BBOX-1007] —10—\n[BBOX-1008] 上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n[BBOX-1009] 奕检医学\n[BBOX-1010] YIJIANMED LABORATORY\n[BBOX-1011] YJ50430012T\n[BBOX-1012] 部分基因简介\n[BBOX-1013] 检测基因\n[BBOX-1014] 描述\n[BBOX-1015] APC\n[BBOX-1016] APC 编码腺瘤性结肠息肉蛋白,该蛋白是促癌 WNT/β-连环蛋白信号传导通路的负调节因子\n[BBOX-1017] (PMID:8259518,8259519)。APC 的主要肿瘤抑制作用在于其调节细胞内β-连环蛋白水平的能力\n[BBOX-1018] (PMID:11978510)。另外 APC 退出细胞核的能力对其肿瘤抑制功能至关重要(PMID:10984057)。当 APC 的\n[BBOX-1019] 活性丧失时,WNT 通路激活异常增加,通常导致增生并最终出现肿瘤进展(PMID:8259511)。有趣的是,抑制肿\n[BBOX-1020] 瘤需要 APC 的表达达到一定的阈值,且表达水平也被十分精确的进行调控,因为肿瘤发生需要β-连环蛋白达到\n[BBOX-1021] 一定的水平(PMID:11743581)。APC 基因中的突变导致家族性腺瘤性息肉病\n[BBOX-1022] (FAP)(PMID:1651174,1651562),其中 95%的人发展成结直肠癌(PMID:1528264),APC 中的种系突变也导致\n[BBOX-1023] 许多相关疾病的发生,包括 Turcot 综合征,加德纳综合征和扁平腺瘤综合征(PMID:8593545)。在 50-80%的\n[BBOX-1024] 散发性结肠直肠癌中观察到 APC 突变,就像在 FAS 中发现的突变一样(PMID:17143297),另外在前列腺癌,胃\n[BBOX-1025] 癌,皮肤癌,子宫癌,乳腺癌,肺癌,膀胱癌和头颈部癌症中也观察到突变(cBioPortal,MSKCC,2015 年 4 月),大多\n[BBOX-1026] 数 APC 突变是截短的,并且大多数 APC 体细胞突变位于蛋白质的突变簇区域(MCR)内,这对于β-连环蛋白结合\n[BBOX-1027] 来说是重要的(PMID:10784639,1338904)。\n[BBOX-1028] BRAF\n[BBOX-1029] BRAF 蛋白是在丝裂原活化蛋白激酶(MAPK)级联反应(PMID:15520807)的调节中起关键作用的丝氨酸/苏氨\n[BBOX-1030] 酸激酶,其在生理上调节与细胞功能相关的基因的表达,包括增殖等活动(PMID:24202393)。BRAF 的基因改变\n[BBOX-1031] 主要见于黑色素瘤和甲状腺癌以及一小部分肺癌和结肠直肠癌中,最常见的 BRAF 点突变是 V600E,它可以调\n[BBOX-1032] 节蛋白激酶的活性,从而导致组成型 BRAF 激活,BRAFV600E 可以独立于 RAS 或上游激活而发出单体信号\n[BBOX-1033] (PMID:20179705)。目前已发现其他的 BRAF 突变可以影响蛋白质的二聚化倾向\n[BBOX-1034] (PMID:16858395,26343582,12068308)。这些 BRAF 突变的产物也可以以不受调节的方式激活 MAPK 信\n[BBOX-1035] 号传导,并且在某些情况下直接导致肿瘤生长(PMID:15520807)。\n[BBOX-1036] EGFR\n[BBOX-1037] EGFR 编码表皮生长因子受体。EGFR 通过其配体包括表皮生长因子(EGF)和转化生长因子-α(TGF-α)的结合\n[BBOX-1038] 激活致癌的 MAPK 和 PI3K/AKT/mTOR 信号级联的下游信号传导途径,最终导致细胞增殖,迁移和分化\n[BBOX-1039] (PMID:18045542)。虽然 EGFR 通常在正常成人组织中以低水平表达,但是在许多癌症类型例如肺癌,脑癌,结\n[BBOX-1040] 直肠癌和头颈癌(PMID:10880430)中发现其通过突变和/或扩增使该受体过度激活,而在脑癌和结直肠癌\n[BBOX-1041] 中,EGFR 基因的拷贝数增加导致受体过表达(PMID:11426640)。然而,在肺癌中,最普遍的 EGFR 改变是激酶\n[BBOX-1042] 结构域中的突变,导致受体的组成性激活(PMID:15329413),但在胰腺癌和结直肠癌中很少发现 EGFR 的激活\n[BBOX-1043] 突变(PMID:24827134)。\n[BBOX-1044] ERBB2\n[BBOX-1045] ERBB2(也称 HER2)是受体酪氨酸激酶中表皮生长因子受体(EGFR)家族的成员,在一系列人类癌症(包括乳腺\n[BBOX-1046] 癌,胃癌/胃食管癌和子宫内膜癌)中异常扩增和/或过表达(PMID:19536107)。ERBB2/ERBB2 的独特之处在于\n[BBOX-1047] 它不直接结合自己的配体。相反,它通过结合(PMID:12620236)增强其他的配体如 EGFR(ERBB1)或 ERBB3\n[BBOX-1048] 的活性。事实上,ERBB2 是所有 ERBB 受体同种型(PMID:10220407,9130710)的优选结合配体,ERBB2/ERBB3\n[BBOX-1049] 复合物通过激活下游致癌 PI3K 途径(PMID:12853564)显示出高度的有丝分裂活性。或者,ERBB2 可同源二聚\n[BBOX-1050] 化并启动细胞内有丝分裂级联,包括 RAS/MAPK,PI3K/AKT/mTOR,SRC 和 STAT 信号传导途径\n[BBOX-1051] (PMID:22785351)。大约 17%至 30%的人类乳腺肿瘤具有 ERBB2 基因扩增,这与患者总体生存率差和肿瘤\n[BBOX-1052] 复发的时间相关(PMID:3798106,23000897,9552035,9469329)。扩增的 ERBB2 与 ERBB3 异源二聚化以激\n[BBOX-1053] 活 PI3K/AKT/mTOR 信号传导并驱动乳腺癌中的肿瘤发生\n[BBOX-1054] (PMID:12853564,23204226,12124352,18632642)。ERBB2 在约 20%胃或胃食管癌\n[BBOX-1055] (PMID:24943493,21468131)中扩增,并且其过度表达被多种药物(例如曲妥珠单抗,阿托珠单抗,埃克替尼,拉\n[BBOX-1056] 帕替尼和培妥珠单抗)靶向(PMID:24799465)。但在非小细胞肺癌,卵巢癌,膀胱癌,子宫颈癌,子宫内膜癌,结肠\n[BBOX-1057] 直肠癌,胰腺癌和涎腺癌,软组织肉瘤中及胆管癌中,ERBB2 扩增的发生率很低(PMID:24656976)。最近在包括\n[BBOX-1058] 肺腺癌,小叶乳腺癌,膀胱癌,胃癌和子宫内膜癌在内的许多癌症中发现了较低频率的 ERBB2 激活突变,其中细\n[BBOX-1059] 胞外和激酶结构域中的反复热点经常出现改变(PMID:23000897,223220880,22908275)。目前有关 ERBB2\n[BBOX-1060] —11—\n[BBOX-1061] 上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n[BBOX-1062] 奕检医学\n[BBOX-1063] YIJIANMED LABORATORY\n[BBOX-1064] YJ50430012T\n[BBOX-1065] 靶向治疗的药物正处于进一步开发中。\n[BBOX-1066] FBXW7 基因编码 SCF(Skp1-Cul1-F-box 蛋白)泛素连接酶复合物识别底物的 F-box 蛋白亚基,在底物鉴定时\n[BBOX-1067] 该复合物会修饰底物,使其成为蛋白质降解的靶标。FBXW7 的底物包括蛋白质\n[BBOX-1068] c-MYC,mTOR(PMID:18787170),NOTCH1,cyclin-E 和 JUN,它们在调节细胞分裂,分化和生长中���作用,并且\n[BBOX-1069] 在癌症中被不恰当地激活,且由于大多数 FBXW7 底物都是经过 SCF 复合物降解处理的原癌基因,所以 FBXW7\n[BBOX-1070] 起着肿瘤抑制剂的作用。突变或拷贝数异常会使 FBXW7 失活并导致癌蛋白的异常积累,随后发生恶性转化\n[BBOX-1071] (PMID:18094723)。此外 FBXW7 中的突变可能对特异性功能如亚基二聚化,蛋白质定位,SCF 组装或底物识\n[BBOX-1072] 别产生负面影响。FBXW7 中的大多数突变是破坏底物结合的点突变,而小的缺失突变或插入突变数量则\n[BBOX-1073] <10%(PMID:24853181,17909001)。\n[BBOX-1074] FGFR1 编码成纤维细胞生长因子受体 1,这是一种对有丝分裂和分化过程十分重要的受体酪氨酸激酶。FGFR1\n[BBOX-1075] 由三个免疫球蛋白样细胞外结构域组成,其中包含一个跨膜成分和一个通过 MAPK 途径起作用的胞质酪氨酸\n[BBOX-1076] 激酶结构域(PMID:8622701)。在与成纤维细胞生长因子配体(主要是 FGF1 和 FGF2)结合后,FGFR1 蛋白迅速\n[BBOX-1077] 二聚化并最终内化至细胞核。然而,结合也随组织分布和配体的可用性而变化(PMID:16597617)。FGFR1 在\n[BBOX-1078] 组织中广泛表达,并且对于多种功能如胚胎发育,骨骼发生,有丝分裂发生和分化是必需的,而 FGFR1 突变则与\n[BBOX-1079] 身体畸形,智力低下和神经缺陷有关(PMID:23812909)。FGFR1 中的扩增或活化突变在包括肺癌,乳腺癌,前列\n[BBOX-1080] 腺癌,头颈癌和食道癌在内的多种癌症中发生,但突变频率不同\n[BBOX-1081] (PMID:21160078,0919196,14614009,16807070,12147242)。在转移性肾细胞癌中,FGF 信号传导被怀疑\n[BBOX-1082] 是细胞对血管生成逃逸的 VEGF 导向疗法产生获得性耐药的原因(PMID:24387233)。目前,许多 FGFR 蛋白的\n[BBOX-1083] 小分子抑制剂正在使用中,其主要的区别在于特异性针对 FGFR 或针对其他受体酪氨酸激酶\n[BBOX-1084] (RTK)(PMID:23696246,24265351)。\n[BBOX-1085] 成纤维细胞生长因子受体(FGFR)家族包括 4 种受体酪氨酸激酶(RTK):FGFR1-4。FGFR 的信号发生取决于激\n[BBOX-1086] 活酪氨酸激酶结构域的配体依赖性二聚化。由于扩增,突变,易位,选择性剪接或由成纤维细胞生长因子(FGF)\n[BBOX-1087] 增加活化而导致的 FGFR 功能失调会促进信号传导,肿瘤发生和细胞迁移(PMID:20094046)。FGFR2 激酶结\n[BBOX-1088] 构域突变存在于颅面综合征中,也出现在子宫内膜癌,宫颈癌和鳞状细胞癌中,而 FGFR2 扩增已在大约 10%的\n[BBOX-1089] 胃癌患者中发现并与预后不良有关。此外 FGFR2 单核苷酸多态性与 ER 阳性乳腺癌的发展有关,尽管病因尚不\n[BBOX-1090] 清楚(PMID:18437204),且成釉细胞瘤中 FGFR2 突变也非常频繁。\n[BBOX-1091] FGFR3 基因编码成纤维细胞生长因子受体 3,这是一种跨膜酪氨酸激酶受体,属于 FGFR 家族(FGFR1-4)。\n[BBOX-1092] FGFR3 蛋白与其同源配体即成纤维细胞生长因子(FGF)的结合会导致受体二聚化,随后激活并调节增殖,分化,\n[BBOX-1093] 细胞迁移和凋亡等下游途径(PMID:7542215,20094046)。FGFR3 基因中的可变剪接事件产生两种同种\n[BBOX-1094] 型,FGFR3b 和 FGFR3c,其具有独特的组织表达模式和配体结合特异性(PMID:8663044,7512569)。在约 15%\n[BBOX-1095] 的多发性骨髓瘤患者中观察到特异性 t(4;14)易位,导致 FGFR3 的组成型表达(PMID:17107900)。此外,在多\n[BBOX-1096] 达 70%的膀胱癌中观察到 FGFR3 的激活突变。其中,S249C 突变占所有突变的\n[BBOX-1097] 69%(PMID:11395371,12743143,16338952)。\n[BBOX-1098] 原癌基因 KIT 编码 3 型跨膜受体酪氨酸激酶,在与其配体干细胞因子(SCF)(也称为肥大细胞生长因子\n[BBOX-1099] (MGF)(PMID:9438854))结合后,受体可通过二聚化和自磷酸化被激活。KIT 活化导致通过几种途径(包括\n[BBOX-1100] PI3K,MAPK 和 STAT)的细胞内信号传导增加,最终导致细胞增殖和存活\n[BBOX-1101] (PMID:17546049,11896121,22089421)。对于患有野生型胃肠间质瘤(GIST;无 KIT 或 PDGFRA 突变)的患\n[BBOX-1102] 者,NCCN 建议检测种系琥珀酸脱氢酶(SDH)突变。大约 10-15%的 GIST 是野生型;因此,没有突变并不排除\n[BBOX-1103] GIST 的诊断。在没有 KIT 突变的患者中,具有晚期 GIST 的患者的一部分受益于伊马替尼(0-45%的患\n[BBOX-1104] 者)(NCCNSoftTissueSarcomav.2.2017)。KIT 激活突变发生在 80-90%的 GIST 中,分布在不同频率的多个\n[BBOX-1105] 外显子上(exon11(66.1%),exon9(13%),exon13(1.2%)和\n[BBOX-1106] exon17(0.6%))(PMID:15365079,17268243,11719439)。至少有八种针对 KIT 的小分子酪氨酸激酶抑制剂\n[BBOX-1107] (TKIs)已被美国食品和药物管理局批准,每种 TKI 的功效取决于激活 KIT 突变的位置\n[BBOX-1108] (PMID:2427414,18955458,19164557)。\n[BBOX-1109] —12—\n[BBOX-1110] 上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n[BBOX-1111] 奕检医学\n[BBOX-1112] YIJIANMED LABORATORY\n[BBOX-1113] YJ50430012T\n[BBOX-1114] KRAS是小型GTP酶RAS家族的成员,该家族催化GTP水解为GDP。在生理条件下,这些RAS蛋白在活性(GTP\n[BBOX-1115] 结合)和非活性(GDP结合)状态之间循环,以激活受体酪氨酸激酶(RTK)下游的MAPK和PI3K致癌途径信号传\n[BBOX-1116] 导(PMID:22189424)。RAS酶的功能受鸟嘌呤核苷酸交换因子(GEF)如SOS的调节,这些因子可以使GDP与\n[BBOX-1117] GTP交换,也可以通过GTP酶活化蛋白如NF1调节,从而提高RAS水解GTP的能力。一旦被激活,RAS可通\n[BBOX-1118] 过激活不同的细胞内信号传导途径(包括RAF/MEK/ERK和PI3K/AKT/mTOR途径)介导细胞增殖和其他细胞\n[BBOX-1119] 功能的调节。KRAS中的转化突变常见于胰腺癌,结肠癌,子宫内膜癌,卵巢癌和胆管癌;几乎所有这些突变都可\n[BBOX-1120] 导致KRAS的组成型活化,从而促进细胞增殖(PMID:21993244,24651010)。KRAS突变主要发生在三个主要\n[BBOX-1121] 热点G12,G13和Q61上,前两个发生在GTP-ase结构域,后者为干扰NF1结合和调节KRAS的能力\n[BBOX-1122] (PMID:22589270,21993244,24651010)。其他不太明确表征的突变如A146T/V/P和L19F也已被表征,而\n[BBOX-1123] 且发现较低频率下也可处于活化状态(PMID:20147967,20432530,20570890)。种系KRAS突变可导致\n[BBOX-1124] Noonan综合征(NS)和心脏-皮肤-皮肤(CFC)综合征(PMID:16474405,16474404,19467855,17056636),这\n[BBOX-1125] 些疾病与过度活化的MAPK途径,独特的临床特征和癌症易感性相关(PMID:19467855,17704260)。\n[BBOX-1126] MAP2K1(MEK1)蛋白是一种丝氨酸/苏氨酸激酶,向RAF下游发出信号并激活ERK1/2,因此在MAP激酶\n[BBOX-1127] (MAPK)级联中发挥关键调节作用。MAPK级联反应涉及不同的细胞过程,包括增殖,分化和转录调控,目前已经\n[BBOX-1128] 在几种不同的癌症类型中发现级联反应会因为其组分RAS和RAF的遗传突变而产生变化\n[BBOX-1129] MAP2K1\n[BBOX-1130] (PMID:12068308,12509763)。MEK1的突变很少见,但一般发生在携带BRAF或RAS突变的肿瘤类型中,包\n[BBOX-1131] (PMID:22753777)。一些MEK1突变可以赋予细胞对MEK和RAF抑制剂的抗\n[BBOX-1132] 括黑色素瘤,结直肠癌和肺癌\n[BBOX-1133] 性(PMID:19915144,213383288)。\n[BBOX-1134] MLH1蛋白对于DNA错配修复途径是必不可少的。MLH1与PMS2(最常见),PMS1或MLH3异二聚形成内\n[BBOX-1135] 切酶复合物,并切割受损的DNA链,导致其局部切除(PMID:10037723,10542278,10615123)。MLH1中的突\n[BBOX-1136] 变导致无法正确修复错配和插入/缺失环,这与微卫星重复序列经常相关,微卫星重复序列的改变可能是特别有\n[BBOX-1137] 害的,因为它们可能在其他基因中产生移码突变。MLH1中的突变发生在多种组织类型中,但在散发性结肠癌,\n[BBOX-1138] MLH1\n[BBOX-1139] 胃癌和子宫内膜癌的特定子集以及遗传性的犬牙综合征(有时称为遗传性非息肉病性结肠癌(HNPCC))中最常\n[BBOX-1140] 见(PMID:8484122,8040889,8261393)。MLH1作为典型的肿瘤抑制基因,由于遗传或体细胞突变导致的一\n[BBOX-1141] 个等位基因的功能丧失往往会导致其他等位基因也丧失功能。而在治疗方面,FDA批准了pembrolizumab\n[BBOX-1142] 用于治疗错配修复缺陷型(dMMR)和MSI(微卫星不稳定性)肿瘤。\n[BBOX-1143] MSH2(MutS蛋白同系物2)蛋白是参与错配修复的肿瘤抑制因子。MSH2与其他MutS蛋白如MSH6和\n[BBOX-1144] MSH3形成异二聚体,分别形成MutS-α和MutS-β错配修复(MMR)复合物(PMID:8252616,7973733)。两种\n[BBOX-1145] 复合物都参与识别错配的碱基对,形成DNA-MutS复合物,该复合物发信号通知MMR机制的其他组分以切除\n[BBOX-1146] 异常核苷酸。MSH2和其他MMR基因与遗传性非息肉病性结肠癌(HNPCC),也称为Lynch综合征有关\n[BBOX-1147] MSH2\n[BBOX-1148] (PMID:428275,1648437)。MSH2突变占所有HNPCC病例(PMID:11852992)中的约40%,并且与MSI高\n[BBOX-1149] 表型以及MLH1中的突变(PMID:9823339,9354436)相关。尽管最常见于结肠癌,但MSH2突变在许多其他\n[BBOX-1150] 癌症类型和综合征中也有报道,包括子宫内膜癌、子宫癌以及皮脂腺肿瘤(PMID:19078925,16826164)。而在\n[BBOX-1151] 治疗方面,FDA批准了派姆单抗用于治疗错配修复缺陷型(dMMR)和MSI(微卫星不稳定性)肿瘤。\n[BBOX-1152] MSH6(mutS同系物6)基因编码DNA修复错配蛋白MSH6。MSH6是与MSH2异二聚化形成MutS-α的\n[BBOX-1153] 肿瘤抑制剂。该复合物可识别单碱基对错配和二核苷酸插入-删除循环,启动错配修复(MMR)过程\n[BBOX-1154] MSH6\n[BBOX-1155] (PMID:8816473)。MSH6和其他MMR基因与遗传性非息肉病性结肠癌(HNPCC),也称为Lynch综合征有\n[BBOX-1156] 关(PMID:428275,1648437)。虽然最常见于结肠癌,但MSH6突变在许多其他癌症类型和综合征(包括子宫内\n[BBOX-1157] 膜癌和子宫癌)中也有报道(PMID:19078925,16106253)。而在治疗方面,FDA批准了派姆单抗用于治疗错配\n[BBOX-1158] 修复缺陷型(dMMR)和MSI(微卫星不稳定性)肿瘤。\n[BBOX-1159] Ras超家族包含超过150种具有GTP酶活性的小单体蛋白,其基于相似的序列和功能进一步分类为亚家族。\n[BBOX-1160] 在Ras亚科内有四个关键成员:K-Ras4a,K-Ras4b,N-Ras和H-Ras。这些蛋白质高度同源,并在所有细胞谱系\n[BBOX-1161] 和器官中检测到表达;然而,它们并不完全是多余的。某些成年组织优先表达特异性同种型\n[BBOX-1162] NRAS\n[BBOX-1163] (http://gan.sagepub.com/content/2/3/216.full),并且独特的翻译和修饰将它们分布到不同的亚细胞定位,\n[BBOX-1164] —13—\n[BBOX-1165] 上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话:400-004-2111 网址:www.yjmedlab.com\n[BBOX-1166] 奕检医学\n[BBOX-1167] YIJIANMED LABORATORY\n[BBOX-1168] YJ50430012T\n[BBOX-1169] 从而激活特异性信号级反应,促进增殖,细胞运动,存活,血管生成,代谢和逃避抗肿瘤免疫应答\n[BBOX-1170] (PMID:15731001;PMID:12728271)。Ras 蛋白在与 GTP 结合时具有活性,并且通过鸟嘌呤核苷酸交换因子\n[BBOX-1171] (GEFs)进行 GDP 与 GTP 的交换。GEFs 通过加速 Ras 介导的 GTP 酶激活蛋白(GAP)平衡使 Ras 蛋白失活。\n[BBOX-1172] Ras是人类癌症中最常见的致癌基因,Ras编码基因NRAS,KRAS和HRAS中的突变常常损害 Ras 介导的GTP-\n[BBOX-1173] 水解,导致 Ras 的组成型激活。致癌 Ras 的恶性转化活性也依赖于脱甲基化,(PMID:22020205)。尽管在 Ras\n[BBOX-1174] 家族蛋白质中存在高同源性,但不同的 Ras 同种型在特定类型的癌症中优先突变。NRAS 基因与皮肤,造血和\n[BBOX-1175] 淋巴组织的癌症有关。\n[BBOX-1176] NTRK1 基因编码原肌球蛋白受体激酶 A(TrkA),是 Trk 受体酪氨酸激酶家族的成员。NTRK1 由位于染色体\n[BBOX-1177] 1q21-22 上的 17 个外显子编码(PMID:12652644),并且可以产生三个不同的剪接变体,即 TrkAI,TrkAll 和\n[BBOX-1178] TrkAIII。TrkAI 和 TrkAll 剪接变体具有高度的相似性,仅在 TrkAll1296 处插入 18 个核苷酸才有所不同\n[BBOX-1179] (PMID:8325889)。在生物学上,TrkAI 被认为是神经母细胞瘤中的肿瘤抑制因子(PMID:19734938),而 TrkAll\n[BBOX-1180] 的特征在于增强与神经营养因子的亲和力(PMID:7972023)。通过 NTRK1 的外显子 6,7 和 9 缺失产生 TrkAIII\n[BBOX-1181] 变体,导致细胞外免疫球蛋白 C1 结构域的缺失。因此,TrkAIII 蛋白中缺失了几个 N-糖基化位点,限制了其对胞\n[BBOX-1182] 内膜隔室的表达,并诱导 PI3K/AKT/NF-κB 信号传导的组成型激活(Farina 等,2009)。重要的是要注意,TrkAIII\n[BBOX-1183] 剪接变体被认为是神经母细胞瘤中的致癌基因(PMID:19564412),并促进遗传不稳定性(PMID:19564412)。\n[BBOX-1184] NTRK1\n[BBOX-1185] TrkA 在神经,内分泌和免疫系统的细胞上表达,响应配体结合控制细胞增殖,分化,凋亡和细胞存活\n[BBOX-1186] (PMID:25527197)。尽管神经营养因子 3(NT-3)和 4(NT-4)也可以激活 TrkA,但是它最常被神经生长因子\n[BBOX-1187] (NGF)激活(PMID:18289031)。受体同二聚化后,下游信号级联,最常见的 RAS/MAPK,PI3K/AKT 和 PLCγ\n[BBOX-1188] /PKC 通路被激活(PMID:25527197)。相反,在不存在配体的情况下,TrkA 可通过抑制 PI3K/AKT 信号启动促\n[BBOX-1189] 凋亡信号级联,导致 Bad 的去抑制,并激活 JNK 介导的促凋亡转录调节因子,如 Bim 和\n[BBOX-1190] Puma(PMID:22465479)。NTRK1 重排发生在 12%的乳头状甲状腺癌中,3.3%的肺癌和近 1%的多形性恶性\n[BBOX-1191] 胶质瘤中。目前在胆道癌中也发现了 RABGAP1L-NTRK1 融合。在结直肠癌和甲状腺癌中,融合的伴侣基因\n[BBOX-1192] 包括 TPM3,TFG 和 TPR,而肺癌中检测到 MPRIP 和 CD74。NTRK1 基因融合了完整的 TRKA 激酶结构域,导\n[BBOX-1193] 致了 TRKA 激酶活性组成性激活。\n[BBOX-1194] 磷脂酰肌醇-3-激酶(PI3K)由调节亚基(p85α)和催化亚基(p110α)组成,它是由 PIK3CA 基因编码的催化亚基。\n[BBOX-1195] PIK3CA 是癌症中最常见的突变基因之一,PI3K 的异常激活是转化事件(PMID:17376864)。多种受体酪氨酸\n[BBOX-1196] 激酶,包括 EGFR,ERBB2(ERBB2),RET,MET 和 VEGFR 等均可将细胞外信号转化为细胞内信号,并通过支架蛋白\n[BBOX-1197] 如 IRS1 或通过激活 RAS 将 PI3K 募集至质膜。刺激后,PI3K-110α将其脂质底物 PIP2(磷脂酰肌醇-4,5-二磷\n[BBOX-1198] 酸)转化为 PIP3(磷脂酰肌醇-3,4,5-二磷酸),激活几个信号级联反应,包括充分表征的 AKT-mTOR 通路。一旦\n[BBOX-1199] 被激活,AKT-mTOR 下游信号传导可促进细胞存活,增殖,生长和运动(PMID:16341083)。长期暴露于一些\n[BBOX-1200] PI3K/mTOR 途径靶向药物可以减轻癌细胞 PI3K-AKT-mTOR 途径固有的自我调节特性,从而促进肿瘤对这\n[BBOX-1201] PIK3CA\n[BBOX-1202] 些药物的耐药性(PMID:22576208)。\n[BBOX-1203] PMS2 是一种内切核酸酶,在错配修复(MMR)途径中起重要作用。具体而言,PMS2 切割 DNA 以启动错配链\n[BBOX-1204] 的切除(PMID:20624957)。PMS2 突变导致不能正确修复 DNA 的错配和插入/缺失环,这导致肿瘤超突变增\n[BBOX-1205] 加和微卫星不稳定性高(MSI-H)表型(PMID:14871975)。PMS2 的种系突变可引起 Lynch 综合征,其易患某些\n[BBOX-1206] PMS2\n[BBOX-1207] 癌症,包括结肠癌,子宫内膜癌和卵巢癌,并暗示 PMS2 为肿瘤抑制因子(PMID:16472587)。在来自多种组织类\n[BBOX-1208] 型的癌症中也报道了散发性 PMS2 突变(PMID:16472587)。肿瘤超突变与某些免疫疗法的反应有关。具体而\n[BBOX-1209] 言,pembrolizumab 已被 FDA 批准用于所有 MMR 缺陷和 MSI 肿瘤,不论特定肿瘤病因\n[BBOX-1210] (PMID:25409260,26028255)\n[BBOX-1211] PTEN 编码肿瘤抑制因子,其是人癌症中最频繁突变的基因之一(PMID:9072974,9090379,22473468)。PTEN\n[BBOX-1212] 具有几种生理功能,最显着的是在细胞膜上将磷脂酰肌醇(3,4,5)-三磷酸(PIP3)转化为磷脂酰肌醇(4,5)-三磷酸\n[BBOX-1213] (PIP2)(PMID:18767981)。PTEN 功能的损害可导致 PIP3 积累和分解代谢下游 AKT/mTOR 信号传导的组成\n[BBOX-1214] 型激活。因此,PTEN 失活可促进细胞生长,增殖和存活(PMID:12040186)。另外,核 PTEN 被认为可调节 RAD51\n[BBOX-1215] PTEN\n[BBOX-1216] 表达,与 DNA 链断裂的同源重组和修复相关(PMID:17218262,23888040)。因此,PTEN 的丧失也可能导致更\n[BBOX-1217] 严重的基因组不稳定性并为其他有害突变的积累提供帮助。PTEN 经常在许多类型的人类癌症中发生突变\n[BBOX-1218] —14—\n[BBOX-1219] 上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n[BBOX-1220] 奕检医学\n[BBOX-1221] YIJIANMED LABORATORY\n[BBOX-1222] YJ50430012T\n[BBOX-1223] (PMID:15254063),PTEN 种系功能丧失突变发生在约80%的癌症易感性综合征 Cowden 病患者中,其与高外\n[BBOX-1224] 显率乳腺癌和甲状腺癌相关(PMID:9467011,24136893,21430697)。\n[BBOX-1225] RET 是一种受体酪氨酸激酶,可与神经胶质细胞系衍生的神经营养因子(GDNF)家族的配体结合,并通过促癌基\n[BBOX-1226] 因丝裂原活化蛋白激酶(MAPK)和磷酸肌醇 3-激酶(PI3K)途径传递细胞内信号(PMID:24561444)。RET 通常\n[BBOX-1227] 在发育中的胚胎中表达,在神经和神经内分泌中起着特别重要的作用(PMID:8306871)。在癌症中,RET 可以通\n[BBOX-1228] 过点突变或基因重排与多种易位配体融合,产生组成型活性胞质癌蛋白(PMID:24561444)。RET 中可遗传的激\n[BBOX-1229] 活突变导致高度渗透性家族性癌症综合征多发性内分泌腺癌 2A 型(MEN2A:甲状腺髓样癌,嗜铬细胞瘤,甲状\n[BBOX-1230] 旁腺功能亢进),多发性内分泌腺瘤 2B 型(MEN2B:甲状腺髓样癌,嗜铬细胞瘤,多发性粘膜神经瘤和肠神经节细\n[BBOX-1231] 胞瘤)和家族性甲状腺髓样癌(FMTC)(PMID:15322516)。致癌体细胞突变包括 RET 基因座的点突变和基因组\n[BBOX-1232] 重排。已经在各种癌症中鉴定出这些变异,包括乳头状甲状腺癌,肺腺癌和慢性髓单核细胞白血病(CMML)。此\n[BBOX-1233] 外,野生型 RET 的异常表达或活化与胰腺癌中的肿瘤侵袭和转移以及乳腺癌中的内分泌治疗抗性相关\n[BBOX-1234] (PMID:24561444)。\n[BBOX-1235] TP53 编码 p53 肿瘤抑制蛋白,这是一种转录因子,可通过诱导下游抗肿瘤反应如 DNA 修复和凋亡\n[BBOX-1236] (PMID:11099028)来响应细胞应激,包括 DNA 损伤和致癌活化。TP53 是人类癌症中最常见的突变基因,并且\n[BBOX-1237] 在癌症易感性综合征 Li-Fraumeni 中可发生种系突变(PMID:22713868,21765642)。p53 蛋白由 N-末端反\n[BBOX-1238] 式激活结构域,中心 DNA 结合结构域,寡聚化结构域和 C-末端调节结构域组成(PMID:22713868)。\n[BBOX-1239] — 15 —\n[BBOX-1240] 上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n[BBOX-1241] 奕检医学\n[BBOX-1242] YIJIANMED LABORATORY\n[BBOX-1243] YJ50430012T\n[BBOX-1244] 常见靶向药物说明\n[BBOX-1245] 药物\n[BBOX-1246] 中文\n[BBOX-1247] 药物说明\n[BBOX-1248] FDA\n[BBOX-1249] NPMA\n[BBOX-1250] Trametinib\n[BBOX-1251] 曲美替尼\n[BBOX-1252] 曲美替尼\n[BBOX-1253] (Trametinib) 是一\n[BBOX-1254] 种口服生物可利用的\n[BBOX-1255] 丝裂原激活的细胞外\n[BBOX-1256] 信号调节激酶 1\n[BBOX-1257] (MEK1) 和 MEK2\n[BBOX-1258] 抑制剂。它于 2013\n[BBOX-1259] 年 5 月首次被 FDA\n[BBOX-1260] 批准用于治疗黑色素\n[BBOX-1261] 瘤。\n[BBOX-1262] FDA 批准：1. 曲美替尼联合达拉非尼用\n[BBOX-1263] 于 BRAF V600E 或 V600K 突变的不可切\n[BBOX-1264] 除或转移性黑色素瘤患者的治疗；2. 曲\n[BBOX-1265] 美替尼联合达拉非尼用于 BRAF V600E\n[BBOX-1266] 或 V600K 突变且累及淋巴结的黑色素瘤\n[BBOX-1267] 患者术后的辅助治疗；3. 曲美替尼联合\n[BBOX-1268] 达拉非尼治疗 BRAF V600E 突变的转移\n[BBOX-1269] 性非小细胞肺癌(NSCLC)患者；4. 曲美\n[BBOX-1270] 替尼联合达拉非尼治疗 BRAF V600E 突\n[BBOX-1271] 变的局部晚期或转移性甲状腺未分化癌\n[BBOX-1272] (ATC)患者，无令人满意的局部区域治疗\n[BBOX-1273] 选择；5. 曲美替尼联合达拉非尼用于治\n[BBOX-1274] 疗 1 岁及以上 BRAF V600E 突变的不可\n[BBOX-1275] 切除或转移性实体瘤的成人和儿童患者，\n[BBOX-1276] 这些患者在先前的治疗后已经进展，并且\n[BBOX-1277] 没有令人满意的替代治疗方案。6. 曲美\n[BBOX-1278] 替尼联合达拉非尼治疗 1 岁以上 BRAF\n[BBOX-1279] V600E 突变的低级别胶质瘤(LGG)患\n[BBOX-1280] 儿，需要全身治疗。\n[BBOX-1281] NMPA 批准:1. 联合甲磺酸\n[BBOX-1282] 达拉非尼适用于治疗 BRAF\n[BBOX-1283] V600 突变阳性的不可切除\n[BBOX-1284] 或转移性黑色素瘤患者；2.\n[BBOX-1285] 联合甲磺酸达拉非尼适用于\n[BBOX-1286] BRAF V600 突变阳性的 III\n[BBOX-1287] 期黑色素瘤患者完全切除后\n[BBOX-1288] 的辅助治疗；3. 联合甲磺酸\n[BBOX-1289] 达拉非尼适用于治疗 BRAF\n[BBOX-1290] V600 突变阳性的转移性非\n[BBOX-1291] 小细胞肺癌患者。\n[BBOX-1292] Encorafenib\n[BBOX-1293] Encorafenib 是一种\n[BBOX-1294] 口服 Raf 激酶抑制\n[BBOX-1295] 剂，具有潜在的抗肿\n[BBOX-1296] 瘤活性，特异性抑制\n[BBOX-1297] Raf 激酶（RAF/丝裂\n[BBOX-1298] 原活化蛋白激酶激酶\n[BBOX-1299] (MEK)/细胞外信号\n[BBOX-1300] 相关激酶（ERK）信\n[BBOX-1301] 号通路中的一种丝氨\n[BBOX-1302] 酸/苏氨酸酶）。\n[BBOX-1303] FDA 批准：1. 与 binimetinib 联合，用\n[BBOX-1304] 于治疗经 FDA 批准的试验检测为 BRAF\n[BBOX-1305] V600E 或 V600K 突变的不可切除或转移\n[BBOX-1306] 性黑色素瘤患者；2. 联合 binimetinib\n[BBOX-1307] 治疗经 FDA 批准试验检测为 BRAF\n[BBOX-1308] V600E 突变的转移性非小细胞肺癌成年\n[BBOX-1309] 患者；3. 联合西妥昔单抗，用于既往治\n[BBOX-1310] 疗后经 FDA 批准试验检测为 BRAF\n[BBOX-1311] V600E 突变的成人转移性结直肠癌患者\n[BBOX-1312] 的治疗。\n[BBOX-1313] 无\n[BBOX-1314] Tucatinib\n[BBOX-1315] Tucatinib 是一种酪\n[BBOX-1316] 氨酸激酶抑制剂，靶\n[BBOX-1317] 向人表皮生长因子受\n[BBOX-1318] 体 2 （HER2），与\n[BBOX-1319] 其他抗肿瘤药联合用\n[BBOX-1320] 于治疗难治性、晚期\n[BBOX-1321] 或转移性 HER2 阳\n[BBOX-1322] 性乳腺癌和结直肠\n[BBOX-1323] 癌。\n[BBOX-1324] FDA 批准：1. Tucatinib 联合曲妥珠单\n[BBOX-1325] 抗和卡培他滨用于晚期不可切除或转移\n[BBOX-1326] 性 HER2 阳性乳腺癌成年患者，包括脑\n[BBOX-1327] 转移患者，他们在转移性情况下既往接受\n[BBOX-1328] 过一种或多种基于抗 HER2 的治疗方\n[BBOX-1329] 案；2. Tucatinib 与曲妥珠单抗联合用于\n[BBOX-1330] 治疗 RAS 野生型 HER2 阳性不可切除或\n[BBOX-1331] 转移性结直肠癌的成年患者，这些患者在\n[BBOX-1332] 氟尿嘧啶、奥沙利铂和伊立替康为基础的\n[BBOX-1333] 化疗后进展。\n[BBOX-1334] 无\n[BBOX-1335] — 16 —\n[BBOX-1336] 上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n[BBOX-1337] 奕检医学\n[BBOX-1338] YIJIANMED LABORATORY\n[BBOX-1339] YJ50430012T\n[BBOX-1340] Dabrafenib\n[BBOX-1341] 达拉非尼\n[BBOX-1342] 达拉非尼\n[BBOX-1343] (Dabrafenib) 是一\n[BBOX-1344] 种有机氟化合物和抗\n[BBOX-1345] 肿瘤剂, 用作其甲磺\n[BBOX-1346] 酸盐治疗转移性黑色\n[BBOX-1347] 素瘤。它具有抗肿瘤\n[BBOX-1348] 剂、B-Raf 抑制剂和\n[BBOX-1349] 抗冠状病毒剂的作\n[BBOX-1350] 用。它是一种磺胺类\n[BBOX-1351] 化合物, 一种有机氟\n[BBOX-1352] 化合物, 是 1,3-噻唑\n[BBOX-1353] 类和氨基嘧啶的成\n[BBOX-1354] 员。达拉非尼是一种\n[BBOX-1355] 可逆的 ATP 竞争性\n[BBOX-1356] 激酶抑制剂, 靶向\n[BBOX-1357] MAPK 通路。\n[BBOX-1358] FDA 批准: 1. 作为单一药物, 用于治疗\n[BBOX-1359] 经 FDA 批准的检测检测到的具有\n[BBOX-1360] BRAF V600E 突变的不可切除或转移性\n[BBOX-1361] 黑色素瘤患者; 2. 与曲美替尼联合用于:\n[BBOX-1362] a. FDA 批准的检测检测到 BRAF V600E\n[BBOX-1363] 或 V600K 突变的不可切除或转移性黑色\n[BBOX-1364] 素瘤患者的治疗; b. 通过 FDA 批准的试\n[BBOX-1365] 验检测出具有 BRAF V600E 或 V600K 突\n[BBOX-1366] 变的黑色素瘤患者的辅助治疗, 以及在完\n[BBOX-1367] 整切除后累及淋巴结的患者; c. 治疗经\n[BBOX-1368] FDA 批准的检测检测到的具有 BRAF\n[BBOX-1369] V600E 突变的转移性非小细胞肺癌\n[BBOX-1370] (NSCLC) 患者; d. 治疗 BRAF V600E\n[BBOX-1371] 突变的无满意的局部区域治疗方案的局\n[BBOX-1372] 部晚期或转移性未分化甲状腺癌患者; e.\n[BBOX-1373] 1 岁及以上的成人和儿童 BRAF V600E\n[BBOX-1374] 突变不可切除或转移性实体瘤患者的治\n[BBOX-1375] 疗, 这些患者在先前治疗后进展, 没有令\n[BBOX-1376] 人满意的替代治疗方案; f. 治疗 1 岁及\n[BBOX-1377] 以上患有具有 BRAF V600E 突变且需\n[BBOX-1378] 要全身治疗的低级别胶质瘤 (LGG) 的\n[BBOX-1379] 儿科患者。(由于已知 BRAF 抑制的内在\n[BBOX-1380] 抗性, TAFINLAR 不适合用于结直肠癌患\n[BBOX-1381] 者的治疗; 并且不用于 BRAF 野生型实体\n[BBOX-1382] 瘤患者的治疗)\n[BBOX-1383] NMPA 批准用于:1. 联合曲\n[BBOX-1384] 美替尼用于治疗 BRAF\n[BBOX-1385] V600 突变阳性的不可切除\n[BBOX-1386] 或转移性黑色素瘤患者; 2.\n[BBOX-1387] 联合曲美替尼用于 BRAF\n[BBOX-1388] V600 突变阳性的 III 期黑色\n[BBOX-1389] 素瘤患者完全切除后的辅助\n[BBOX-1390] 治疗; 3. 联合曲美替尼用于\n[BBOX-1391] 治疗 BRAF V600 突变阳性\n[BBOX-1392] 的转移性非小细胞肺癌患\n[BBOX-1393] 者。\n[BBOX-1394] Regorafenib\n[BBOX-1395] 瑞戈非尼\n[BBOX-1396] 瑞戈非尼\n[BBOX-1397] (Regorafenib) 是一\n[BBOX-1398] 种激酶抑制剂。用于\n[BBOX-1399] 治疗既往接受过化\n[BBOX-1400] 疗、抗 EGFR 或抗\n[BBOX-1401] VEGF 治疗的转移性\n[BBOX-1402] 结直肠癌患者。它具\n[BBOX-1403] 有抗肿瘤药、酪氨酸\n[BBOX-1404] 激酶抑制剂和肝毒性\n[BBOX-1405] 药物的作用。\n[BBOX-1406] FDA 批准: 1. 用于先前接受索拉非尼治\n[BBOX-1407] 疗的肝癌 (HCC) 患者; 2. 用于治疗转\n[BBOX-1408] 移性结直肠癌 (mCRC) 的患者, 之前曾\n[BBOX-1409] 接受氟嘧啶, 奥沙利铂和伊立替康为基础\n[BBOX-1410] 的化疗、抗 VEGF 治疗, 以及 KRAS 野生\n[BBOX-1411] 型的抗 EGFR 治疗; 3. 用于既往接受甲\n[BBOX-1412] 磺酸伊马替尼和苹果酸舒尼替尼治疗的\n[BBOX-1413] 局部晚期、不可切除或转移性胃肠道间质\n[BBOX-1414] 瘤 (GIST) 患者的治疗。\n[BBOX-1415] NMPA 批准:1. 用于治疗既\n[BBOX-1416] 往接受过索拉非尼治疗的肝\n[BBOX-1417] 细胞癌 (HCC) 患者; 2. 用\n[BBOX-1418] 于治疗既往接受过以氟尿嘧\n[BBOX-1419] 啶、奥沙利铂和伊立替康为\n[BBOX-1420] 基础的化疗, 以及既往接受\n[BBOX-1421] 过或不适合接受抗 VEGF 治\n[BBOX-1422] 疗、抗 EGFR 治疗 (KRAS\n[BBOX-1423] 野生型) 的转移性结直肠癌\n[BBOX-1424] (mCRC) 患者; 3. 用于既\n[BBOX-1425] 往接受过甲磺酸伊马替尼及\n[BBOX-1426] 苹果酸舒尼替尼治疗的局部\n[BBOX-1427] 晚期的、无法手术切除的或\n[BBOX-1428] 转移性的胃肠道间质瘤\n[BBOX-1429] (GIST) 患者。\n[BBOX-1430] Fruquintinib\n[BBOX-1431] 呋喹替尼\n[BBOX-1432] 呋喹替尼\n[BBOX-1433] 呋喹替尼是一个喹唑\n[BBOX-1434] 啉类小分子血管生成\n[BBOX-1435] 抑制剂, 主要作用靶\n[BBOX-1436] 点是 VEGFR 激酶家族\n[BBOX-1437] (VEGFR1、2 和 3)。\n[BBOX-1438] FDA 批准: 适用于既往接受过氟尿嘧啶\n[BBOX-1439] 类、奥沙利铂和伊立替康为基础的化疗,\n[BBOX-1440] 以及既往接受过或不适合接受抗血管内\n[BBOX-1441] 皮生长因子 (VEGF) 治疗、抗表皮生长\n[BBOX-1442] 因子受体 (EGFR) 治疗 (RAS 野生型)\n[BBOX-1443] NMPA 批准: 呋喹替尼胶囊\n[BBOX-1444] 单药适用于既往接受过氟尿\n[BBOX-1445] 嘧啶类、奥沙利铂和伊立替\n[BBOX-1446] 康为基础的化疗, 以及既往\n[BBOX-1447] 接受过或不适合接受抗血管\n[BBOX-1448] — 17 —\n[BBOX-1449] 上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话: 400-004-2111 网址: www.yjmedlab.com\n[BBOX-1450] 奕检医学\n[BBOX-1451] YIJIANMED LABORATORY\n[BBOX-1452] YJ50430012T\n[BBOX-1453] 通过抑制血管内皮细\n[BBOX-1454] 胞表面的 VEGFR 磷酸\n[BBOX-1455] 化及下游信号转导,\n[BBOX-1456] 抑制血管内皮细胞的\n[BBOX-1457] 增殖、迁移和管腔形\n[BBOX-1458] 成，从而抑制肿瘤新\n[BBOX-1459] 生血管的形成，最终\n[BBOX-1460] 发挥肿瘤生长抑制效\n[BBOX-1461] 应。\n[BBOX-1462] 的转移性结直肠癌患者。\n[BBOX-1463] 内皮生长因子 (VEGF) 治疗、\n[BBOX-1464] 抗表皮生长因子受体\n[BBOX-1465] (EGFR) 治疗 (RAS 野生型)\n[BBOX-1466] 的转移性结直肠癌患者。\n[BBOX-1467] Selpercatinib\n[BBOX-1468] 塞普替尼\n[BBOX-1469] 塞普替尼\n[BBOX-1470] (Selpercatinib) 是\n[BBOX-1471] 一种选择性 RET 激酶\n[BBOX-1472] 抑制剂, 能够阻断 RET\n[BBOX-1473] 激酶, 并阻止癌细胞\n[BBOX-1474] 生长。\n[BBOX-1475] FDA 批准: 1. 用于治疗局部晚期或转移\n[BBOX-1476] 性非小细胞肺癌的成年患者, 经 FDA 批\n[BBOX-1477] 准的试验检测到 RET 基因融合; 2. 适用\n[BBOX-1478] 于 2 岁及以上的成人和儿童晚期或转移\n[BBOX-1479] 性甲状腺髓样癌 (MTC) 患者, 经 FDA 批\n[BBOX-1480] 准的试验检测出 RET 突变, 需要系统性\n[BBOX-1481] 治疗; 3. 用于治疗 2 岁及以上的, 经 FDA\n[BBOX-1482] 批准的试验检测具有 RET 基因融合的晚\n[BBOX-1483] 期或转移性甲状腺癌的成人和儿童患者,\n[BBOX-1484] 这些患者需要系统性治疗, 并且是放射性\n[BBOX-1485] 碘难治性 (如果放射性碘是合适的); 4. 适\n[BBOX-1486] 用于经 FDA 批准的试验检测为 RET 基因\n[BBOX-1487] 融合的局部晚期或转移性实体肿瘤的 2\n[BBOX-1488] 岁及以上的成人和儿童患者, 这些患者在\n[BBOX-1489] 接受系统性之前或之后有进展, 或者没有\n[BBOX-1490] 令人满意的替代治疗方案。\n[BBOX-1491] NMPA 批准: 塞普替尼用于\n[BBOX-1492] 治疗 RET 基因融合阳性的局\n[BBOX-1493] 部晚期或转移性非小细胞肺\n[BBOX-1494] 癌成人患者; 2. 需要系统性\n[BBOX-1495] 治疗的晚期或转移性 RET 突\n[BBOX-1496] 变型甲状腺髓样癌成人和\n[BBOX-1497] 12 岁及以上儿童患者、以及\n[BBOX-1498] 需要系统性治疗且放射性碘\n[BBOX-1499] 难治 (如果放射性碘适用)\n[BBOX-1500] 的晚期或转移性 RET 融合阳\n[BBOX-1501] 性甲状腺癌成人和 12 岁及\n[BBOX-1502] 以上儿童患者。\n[BBOX-1503] Repotrectinib\n[BBOX-1504] 瑞普替尼\n[BBOX-1505] 瑞普替尼\n[BBOX-1506] (Repotrectinib) 是\n[BBOX-1507] 一种酪氨酸蛋白激酶\n[BBOX-1508] 原癌基因 ROS1 和原\n[BBOX-1509] 肌球蛋白受体酪氨酸\n[BBOX-1510] 激酶 (TRKs) TRKA、\n[BBOX-1511] TRKB 及 TRKC 的抑制\n[BBOX-1512] 剂。\n[BBOX-1513] FDA 批准: 1. 用于治疗 ROS1 阳性的局\n[BBOX-1514] 部晚期或转移性非小细胞肺癌成人患者;\n[BBOX-1515] 2. 用于治疗 12 岁及以上具有神经营养\n[BBOX-1516] 性酪氨酸受体激酶 (NTRK) 基因融合的局\n[BBOX-1517] 部晚期、转移性或手术切除可能导致严重\n[BBOX-1518] 疾病、治疗后病情进展或没有令人满意的\n[BBOX-1519] 替代疗法的成人和儿童实体瘤患者。\n[BBOX-1520] NMPA 批准: 适用于 ROS1\n[BBOX-1521] 阳性的局部晚期或转移性非\n[BBOX-1522] 小细胞肺癌 (NSCLC) 成人\n[BBOX-1523] 患者。\n[BBOX-1524] Entrectinib\n[BBOX-1525] 恩曲替尼\n[BBOX-1526] 恩曲替尼\n[BBOX-1527] (Entrectinib) 是一\n[BBOX-1528] 种原肌球蛋白受体酪\n[BBOX-1529] 氨酸激酶 (TRK)\n[BBOX-1530] TRKA、TRKB、TRKC、\n[BBOX-1531] 原癌基因酪氨酸蛋白\n[BBOX-1532] 激酶 ROS1 和间变\n[BBOX-1533] 性淋巴瘤激酶 (ALK)\n[BBOX-1534] 抑制剂。它于 2019\n[BBOX-1535] 年 8 月获得 FDA\n[BBOX-1536] 批准用于治疗 ROS1\n[BBOX-1537] 阳性转移性非小细胞\n[BBOX-1538] FDA 批准: 1. 用于治疗 ROS1 阳性的转\n[BBOX-1539] 移性非小细胞肺癌 (NSCLC) 成人患者;\n[BBOX-1540] 2. 用于治疗年龄大于 1 个月的儿童和成人\n[BBOX-1541] 实体瘤患者: a. 具有经 FDA 批准的试验\n[BBOX-1542] 检测到神经营养性酪氨酸受体激酶\n[BBOX-1543] (NTRK) 基因融合, 没有已知的获得性\n[BBOX-1544] 抗性突变; b. 转移或手术切除可能导致严\n[BBOX-1545] 重的并发症; c. 治疗后进展或没有令人\n[BBOX-1546] 满意的替代疗法。\n[BBOX-1547] NMPA 批准: 1. ROS1 阳性\n[BBOX-1548] 的局部晚期或转移性非小细\n[BBOX-1549] 胞肺癌 (NSCLC) 成人患者;\n[BBOX-1550] 2. 用于符合下列条件的成\n[BBOX-1551] 人和 1 月龄以上儿童实体\n[BBOX-1552] 瘤患者: a. 经充分验证的检\n[BBOX-1553] 测方法诊断为携带神经营养\n[BBOX-1554] 酪氨酸受体激酶 (NTRK) 融\n[BBOX-1555] 合基因且不包括已知获得性\n[BBOX-1556] 耐药突变; b. 患有局部晚\n[BBOX-1557] 期、转移性疾病或手术切除\n[BBOX-1558] 可能导致严重并发症的患\n[BBOX-1559] — 18 —\n[BBOX-1560] 上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n[BBOX-1561] 奕检医学\n[BBOX-1562] YIJIANMED LABORATORY\n[BBOX-1563] YJ50430012T\n[BBOX-1564] 肺癌和 NTRK 基因\n[BBOX-1565] 融合阳性实体瘤。\n[BBOX-1566] 者；c. 无满意替代治疗或既\n[BBOX-1567] 往治疗失败的患者。\n[BBOX-1568] Larotrectinib\n[BBOX-1569] 拉罗替尼\n[BBOX-1570] 拉罗替尼\n[BBOX-1571] (Larotrectinib) 是\n[BBOX-1572] 一种原肌球蛋白受体\n[BBOX-1573] 激酶(TRK), TRKA、\n[BBOX-1574] TRKB、TRKC 的抑制\n[BBOX-1575] 剂。TRKA、TRKB 和\n[BBOX-1576] TRKC 由 NTRK1、\n[BBOX-1577] NTRK2 和 NTRK3 基\n[BBOX-1578] 因编码。这些基因与\n[BBOX-1579] 不同配体基因间的框\n[BBOX-1580] 架内融合导致的染色\n[BBOX-1581] 体重排可产生组成性\n[BBOX-1582] 激活嵌合 TRK 融合蛋\n[BBOX-1583] 白, 其可作为致癌驱\n[BBOX-1584] 动因子, 促进肿瘤细\n[BBOX-1585] 胞系中的细胞增殖和\n[BBOX-1586] 存活。\n[BBOX-1587] FDA 批准: 用于治疗具备以下条件的成\n[BBOX-1588] 人和儿童实体瘤患者: 1. 具有神经营养\n[BBOX-1589] 性受体酪氨酸激酶 (NTRK) 基因融合,\n[BBOX-1590] 但没有已知的获得性抗性突变; 2. 转移\n[BBOX-1591] 或手术切除可能导致严重的发病率; 3.\n[BBOX-1592] 没有令人满意的替代治疗或治疗后进展。\n[BBOX-1593] NMPA 批准: 用于治疗符合\n[BBOX-1594] 下列条件的成人和儿童实体\n[BBOX-1595] 瘤患者: 1. 经充分验证的检\n[BBOX-1596] 测方法诊断为携带神经营养\n[BBOX-1597] 酪氨酸受体激酶 (NTRK) 融\n[BBOX-1598] 合基因且不包括已知获得性\n[BBOX-1599] 耐药突变; 2. 患有局部晚\n[BBOX-1600] 期、转移性疾病或手术切除\n[BBOX-1601] 可能导致严重并发症的患\n[BBOX-1602] 者; 3. 无满意替代治疗或既\n[BBOX-1603] 往治疗失败的患者。\n[BBOX-1604] Cetuximab\n[BBOX-1605] 西妥昔单抗\n[BBOX-1606] 西妥昔单抗\n[BBOX-1607] (Cetuximab) 是一\n[BBOX-1608] 种重组嵌合人/小鼠\n[BBOX-1609] IgG1 单克隆抗体, 与\n[BBOX-1610] 表皮生长因子受体\n[BBOX-1611] (EGFR) 竞争性结\n[BBOX-1612] 合, 并竞争性抑制表\n[BBOX-1613] 皮生长因子 (EGF)\n[BBOX-1614] 的结合。EGFR 是受体\n[BBOX-1615] 酪氨酸激酶 ErbB 家\n[BBOX-1616] 族的一员, 存在于正\n[BBOX-1617] 常细胞和肿瘤细胞\n[BBOX-1618] 中; 它负责调节上皮\n[BBOX-1619] 组织的发育和体内平\n[BBOX-1620] 衡。EGFR 与各种类型\n[BBOX-1621] 的癌症有关, 因为它\n[BBOX-1622] 通常在恶性细胞中过\n[BBOX-1623] 表达, 并且 EGFR 过\n[BBOX-1624] 表达与更晚期的疾病\n[BBOX-1625] 和不良预后有关。\n[BBOX-1626] EGFR 在某些类型的\n[BBOX-1627] 癌症中经常发生突\n[BBOX-1628] FDA 批准: 1. 用于经 FDA 批准的检测\n[BBOX-1629] 检测到 KRAS 突变阴性 (野生型)、EGFR\n[BBOX-1630] 表达阳性的转移性结直肠癌患者 (使用限\n[BBOX-1631] 制: 不适用于 RAS 突变或 RAS 突变未知\n[BBOX-1632] 的结直肠癌患者) : a.作为单药治疗, 用\n[BBOX-1633] 于既往经历奥沙利铂或伊立替康为基础\n[BBOX-1634] 的化疗方案并失败以及对伊立替康不耐\n[BBOX-1635] 受的患者; b.与 FOLFIRI 联合用于一线\n[BBOX-1636] 治疗; c.与伊立替康联合用于伊立替康为\n[BBOX-1637] 基础的化疗难治的患者; 2. 用于治疗头\n[BBOX-1638] 颈癌: a.局部或区域晚期头颈部鳞状细胞\n[BBOX-1639] 癌联合放射治疗; b.复发性局部区域疾病\n[BBOX-1640] 或头颈部转移性鳞状细胞癌联合氟尿嘧\n[BBOX-1641] 啶铂类治疗; c.铂类治疗后进展的头颈部\n[BBOX-1642] 复发性或转移性鳞状细胞癌; 3. 与\n[BBOX-1643] Encorafenib 联合用于治疗经 fda 批准的\n[BBOX-1644] 试验检测出 BRAF V600E 突变的转移性\n[BBOX-1645] 结直肠癌(CRC)成人患者。\n[BBOX-1646] NMPA 批准: 1. 用于治疗\n[BBOX-1647] RAS 基因野生型的转移性\n[BBOX-1648] 结直肠癌:a.与 FOLFOX 或\n[BBOX-1649] FOLFIRI 方案联合用于一线\n[BBOX-1650] 治疗; b. 与伊立替康联合用\n[BBOX-1651] 于经含伊立替康治疗失败后\n[BBOX-1652] 的患者; 2. 用于治疗头颈部\n[BBOX-1653] 鳞状细胞癌: a. 与铂类和氟\n[BBOX-1654] 尿嘧啶化疗联合用于一线治\n[BBOX-1655] 疗复发和/或转移性疾病; b.\n[BBOX-1656] 与放疗联合用于治疗局部晚\n[BBOX-1657] 期疾病。\n[BBOX-1658] —19—\n[BBOX-1659] 上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话: 400-004-2111 网址: www.yjmedlab.com\n[BBOX-1660] 奕检医学\n[BBOX-1661] YIJIANMED LABORATORY\n[BBOX-1662] YJ50430012T\n[BBOX-1663] 变，并作为肿瘤发生\n[BBOX-1664] 的驱动因素。在体外,\n[BBOX-1665] 西妥昔单抗被证明在\n[BBOX-1666] 许多癌细胞系和人肿\n[BBOX-1667] 瘤异种移植物中具有\n[BBOX-1668] 抗肿瘤作用。\n[BBOX-1669] Panitumumab 是一\n[BBOX-1670] 种对表皮生长因子受\n[BBOX-1671] 体 （EGFR） 具有特\n[BBOX-1672] 异性的人\n[BBOX-1673] lgG2kappa 单克隆\n[BBOX-1674] 抗体。单克隆抗体\n[BBOX-1675] E7.6.3 与 EGFR 结\n[BBOX-1676] 合，阻断表皮生长因\n[BBOX-1677] 子的结合并将生长因\n[BBOX-1678] 子 α 转化为表达\n[BBOX-1679] EGFR 的癌细胞,并最\n[BBOX-1680] 终抑制 EGFR 依赖性\n[BBOX-1681] 细胞活化和增殖。\n[BBOX-1682] FDA 批准：用于 RAS 野生型 (定义为\n[BBOX-1683] KRAS 和 NRAS 中的野生型) 转移性结直\n[BBOX-1684] 肠癌 (mCRC) 患者：1. 单药治疗既往\n[BBOX-1685] 经过氟嘧啶, 奥沙利铂, 和伊立替康化疗\n[BBOX-1686] 方案后疾病进展的转移性结直肠癌; 2.\n[BBOX-1687] 与 FOLFOX 联合用于一线治疗。（使用\n[BBOX-1688] 限制：携带 RAS 基因突变或者 RAS 突变\n[BBOX-1689] 状态不明的结直肠癌的治疗不建议使用\n[BBOX-1690] 帕尼单抗）。\n[BBOX-1691] 无\n[BBOX-1692] Panitumumab\n[BBOX-1693] 贝伐珠单抗是利用重\n[BBOX-1694] 组 DNA 技术制备的\n[BBOX-1695] 一种人源化单克隆抗\n[BBOX-1696] 体 IgG1, 通过与人血\n[BBOX-1697] 管内皮生长因子\n[BBOX-1698] (VEGF) 结合, 抑制\n[BBOX-1699] VEGF 与其受体结合,\n[BBOX-1700] 阻断血管生成的信号\n[BBOX-1701] 传导途径, 抑制肿瘤\n[BBOX-1702] 细胞生长。作为抗肿\n[BBOX-1703] 瘤血管生成的重要药\n[BBOX-1704] 物之一, 贝伐珠单抗\n[BBOX-1705] 被应用于多种恶性肿\n[BBOX-1706] 瘤的治疗。\n[BBOX-1707] FDA 批准:1. 转移性结直肠癌:a. 与 5-\n[BBOX-1708] 氟尿嘧啶化疗联合作为转移性结直肠癌\n[BBOX-1709] 的一线或二线治疗方案; b. 与氟尿嘧啶\n[BBOX-1710] -伊立替康或氟尿嘧啶 -奥沙利铂为基础\n[BBOX-1711] 的化疗联合用于经贝伐单抗一线治疗后\n[BBOX-1712] 出现疾病进展的转移结直肠癌的二线治\n[BBOX-1713] 疗; c. 贝伐单抗联合曲氟尿苷和替吉奥\n[BBOX-1714] 用于转移性结直肠癌的治疗, 此前使用氟\n[BBOX-1715] 尿嘧啶、奥沙利铂和伊立替康为基础的化\n[BBOX-1716] 疗, 抗 VEGF 生物治疗, 如果 RAS 野生\n[BBOX-1717] 型, 抗 EGFR 治疗; 2. 非小细胞肺癌:\n[BBOX-1718] a. 贝伐珠单抗联合紫杉醇和卡铂一线治\n[BBOX-1719] 疗不可切除的局部晚期、复发性或转移性\n[BBOX-1720] 非鳞状非小细胞肺癌; b. 贝伐单抗联合\n[BBOX-1721] 阿替利珠单抗、紫杉醇和卡铂一线治疗无\n[BBOX-1722] EGFR 或 ALK 基因组肿瘤畸变的转移性\n[BBOX-1723] 非鳞非小细胞肺癌; 3. 贝伐珠单抗治疗\n[BBOX-1724] 成人复发性胶质母细胞瘤; 4. 贝伐珠单\n[BBOX-1725] 抗联合干扰素α治疗转移性肾细胞癌; 5.\n[BBOX-1726] 贝伐珠单抗联合紫杉醇和顺铂, 或紫杉醇\n[BBOX-1727] 和拓扑替康治疗持续性、复发性或转移性\n[BBOX-1728] 宫颈癌; 6. 上皮性卵巢癌、输卵管癌或\n[BBOX-1729] NMPA 批准:1. 转移性结直\n[BBOX-1730] 肠癌: 贝伐珠单抗联合以氟\n[BBOX-1731] 嘧啶为基础的化疗适用于转\n[BBOX-1732] 移性结直肠癌患者的治疗;\n[BBOX-1733] 2. 晚期、转移性或复发性非\n[BBOX-1734] 小细胞肺癌: 贝伐珠单抗联\n[BBOX-1735] 合以铂类为基础的化疗用于\n[BBOX-1736] 不可切除的晚期、转移性或\n[BBOX-1737] 复发性非鳞状细胞非小细胞\n[BBOX-1738] 肺癌患者的一线治疗; 3. 复\n[BBOX-1739] 发性胶质母细胞瘤: 贝伐珠\n[BBOX-1740] 单抗用于成人复发性胶质母\n[BBOX-1741] 细胞瘤患者的治疗; 4. 肝细\n[BBOX-1742] 胞癌: 贝伐珠单抗联合阿替\n[BBOX-1743] 利珠单抗治疗既往未接受过\n[BBOX-1744] 全身系统性治疗的不可切除\n[BBOX-1745] 肝细胞癌患者; 5. 上皮性卵\n[BBOX-1746] 巢癌、输卵管癌或原发性腹\n[BBOX-1747] 膜癌: 贝伐珠单抗联合卡铂\n[BBOX-1748] 和紫杉醇用于初次手术切除\n[BBOX-1749] 后的 III 期或 IV 期上皮性\n[BBOX-1750] 卵巢癌、输卵管癌或原发性\n[BBOX-1751] Bevacizumab\n[BBOX-1752] 贝伐珠单抗\n[BBOX-1753] — 20 —\n[BBOX-1754] 上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n[BBOX-1755] 奕检医学\n[BBOX-1756] YIJIANMED LABORATORY\n[BBOX-1757] YJ50430012T\n[BBOX-1758] 原发性腹膜癌：a. 贝伐珠单抗与卡铂和\n[BBOX-1759] 紫杉醇联合使用，随后以贝伐珠单抗作为\n[BBOX-1760] 单一药物，用于初始手术切除后的 III 期\n[BBOX-1761] 或 IV 期上皮性卵巢癌、输卵管癌或原发\n[BBOX-1762] 性腹膜癌；b.贝伐珠单抗联合紫杉醇、聚\n[BBOX-1763] 乙二醇脂质体多柔比星或拓扑替康治疗\n[BBOX-1764] 既往接受化疗方案不超过 2 种的铂类耐\n[BBOX-1765] 药复发的上皮性卵巢癌、输卵管癌或原发\n[BBOX-1766] 性腹膜癌；c. 贝伐珠单抗联合卡铂和紫\n[BBOX-1767] 杉醇或卡铂和吉西他滨，随后以贝伐单抗\n[BBOX-1768] 作为单药，用于铂类敏感的复发的上皮性\n[BBOX-1769] 卵巢癌、输卵管癌或原发性腹膜癌；d. 贝\n[BBOX-1770] 伐珠单抗与奥拉帕利联合用于晚期上皮\n[BBOX-1771] 性卵巢癌、输卵管癌或原发性腹膜癌成年\n[BBOX-1772] 患者的一线维持治疗，这些患者对一线铂\n[BBOX-1773] 类化疗完全或部分应答，且其癌症与同源\n[BBOX-1774] 重组缺失阳性状态有关，即有害或疑似有\n[BBOX-1775] 害 BRCA 基因突变和/或基因组不稳定；\n[BBOX-1776] 7. 贝伐珠单抗与阿替利珠单抗联合治\n[BBOX-1777] 疗既往未接受过系统治疗的不可切除性\n[BBOX-1778] 或转移性肝细胞癌患者。\n[BBOX-1779] 腹膜癌患者的一线治疗；6.\n[BBOX-1780] 宫颈癌：贝伐珠单抗联合紫\n[BBOX-1781] 杉醇和顺铂或紫杉醇和托泊\n[BBOX-1782] 替康用于持续性、复发性或\n[BBOX-1783] 转移性宫颈癌患者的治疗；\n[BBOX-1784] 7. 不可切除或转移性肝细\n[BBOX-1785] 胞癌：贝伐珠单抗联合信迪\n[BBOX-1786] 利单抗，用于既往未接受过\n[BBOX-1787] 系统治疗的不可切除或转移\n[BBOX-1788] 性肝细胞癌的一线治疗；8.\n[BBOX-1789] 晚期非鳞状非小细胞肺癌：\n[BBOX-1790] 贝伐珠单抗联合信迪利单\n[BBOX-1791] 抗、培美曲塞和顺铂，用于\n[BBOX-1792] 经表皮生长因子受体酪氨酸\n[BBOX-1793] 激酶抑制剂（EGFR-TKI）治\n[BBOX-1794] 疗失败的 EGFR 基因突变\n[BBOX-1795] 阳性的局部晚期或转移性非\n[BBOX-1796] 鳞状非小细胞肺癌\n[BBOX-1797] (NSCLC) 患者的治疗。\n[BBOX-1798] 纳武利尤单抗\n[BBOX-1799] (Nivolumab) 是一\n[BBOX-1800] 种全人源免疫球蛋白\n[BBOX-1801] ( Ig ) G4 单克隆抗体，\n[BBOX-1802] 针对人细胞表面负性\n[BBOX-1803] 免疫调节受体程序性\n[BBOX-1804] 死亡受体- 1 ( PD -\n[BBOX-1805] 1、PCD - 1)，具有免\n[BBOX-1806] 疫检查点抑制和抗肿\n[BBOX-1807] 瘤活性。给药后，纳\n[BBOX-1808] 武单抗通过其配体程\n[BBOX-1809] 序性细胞死亡配体 1\n[BBOX-1810] ( PD-L1 )和程序性细\n[BBOX-1811] 胞死亡配体 2\n[BBOX-1812] ( PD-L2 )结合并阻断\n[BBOX-1813] 免疫球蛋白超家族\n[BBOX-1814] ( IgSF )跨膜蛋白 PD -\n[BBOX-1815] 1 的活化。PD - 1 和\n[BBOX-1816] PD - L1 在某些癌细\n[BBOX-1817] 胞上过表达，PD - L2\n[BBOX-1818] 主要表达于抗原呈递\n[BBOX-1819] 细胞( APC )。这导致\n[BBOX-1820] 了 T 细胞的激活和细\n[BBOX-1821] 胞介导的针对肿瘤细\n[BBOX-1822] FDA 批准：1. 用于黑色素瘤患者：a. 单\n[BBOX-1823] 药或联合伊匹木单抗，用于成人和儿童\n[BBOX-1824] (12 岁及以上)不可切除或转移性黑色素\n[BBOX-1825] 瘤患者；b. 用于完全切除 IIB 期、IIC 期、\n[BBOX-1826] III 期或 IV 期黑色素瘤的 12 岁及以上儿\n[BBOX-1827] 童和成人患者的辅助治疗；2. 用于非小\n[BBOX-1828] 细胞肺癌患者：a. 联合含铂双药化疗，\n[BBOX-1829] 用于在新辅助环境下可切除(肿瘤≥4cm\n[BBOX-1830] 或淋巴结阳性)的非小细胞肺癌的成年患\n[BBOX-1831] 者；b. 联合伊匹木单抗作为一线治疗，\n[BBOX-1832] 经 FDA 批准的试验检测到 D-L1 表达阳\n[BBOX-1833] 性（定义为表达 PD-L1 的肿瘤细胞≥\n[BBOX-1834] 1%) 无 EGFR 或 ALK 基因突变的转移性\n[BBOX-1835] 非小细胞肺癌成年患者；c. 联合伊匹木\n[BBOX-1836] 单抗和 2 周期铂双药化疗作为一线治疗，\n[BBOX-1837] 无 EGFR 或 ALK 基因突变的转移性或复\n[BBOX-1838] 发性非小细胞肺癌成年患者；d. 用于在\n[BBOX-1839] 铂类化疗中或化疗后进展转移性非小细\n[BBOX-1840] 胞肺癌的成人患者。对于 EGFR 或 ALK\n[BBOX-1841] 基因突变的患者，在接受 OPDIVO 之前，\n[BBOX-1842] 应在 FDA 批准的针对这些突变的治疗中\n[BBOX-1843] 出现疾病进展；3. 联合伊匹木单抗作为\n[BBOX-1844] 一线治疗不可切除的成人恶性胸膜间皮\n[BBOX-1845] 瘤；4. 用于肾细胞癌患者：a. 联合伊匹\n[BBOX-1846] NMPA 批准:1. 用于治疗表\n[BBOX-1847] 皮生长因子受体 (EGFR) 基\n[BBOX-1848] 因突变阴性和间变性淋巴瘤\n[BBOX-1849] 激酶 (ALK) 阴性、既往接\n[BBOX-1850] 受过含铂方案化疗后疾病进\n[BBOX-1851] 展或不可耐受的局部晚期或\n[BBOX-1852] 转移性非小细胞肺癌\n[BBOX-1853] (NSCLC) 成人患者；2. 联\n[BBOX-1854] 合含铂双药化疗适用于新辅\n[BBOX-1855] 助治疗可切除的 (肿瘤直径\n[BBOX-1856] ≥4cm 或淋巴结阳性) 非小\n[BBOX-1857] 细胞肺癌 (NSCLC) 成人患\n[BBOX-1858] 者；3. 单药适用于治疗接受\n[BBOX-1859] 含铂类方案治疗期间或之后\n[BBOX-1860] 出现疾病进���且肿瘤\n[BBOX-1861] PD-L1 表达阳性（定义为表\n[BBOX-1862] 达 PD-L1 的肿瘤细胞≥\n[BBOX-1863] 1%) 的复发性或转移性头颈\n[BBOX-1864] 部鳞状细胞癌 (SCCHN) 患\n[BBOX-1865] 者；4. 用于治疗既往接受过\n[BBOX-1866] 两种或两种以上全身性治疗\n[BBOX-1867] 方案的晚期或复发性胃或胃\n[BBOX-1868] 食管连接部腺癌患者；5. 联\n[BBOX-1869] 合含氟尿嘧啶和铂类药物化\n[BBOX-1870] Nivolumab\n[BBOX-1871] 纳武利尤单\n[BBOX-1872] 抗\n[BBOX-1873] — 21 —\n[BBOX-1874] 上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n[BBOX-1875] 奕检医学\n[BBOX-1876] YIJIANMED LABORATORY\n[BBOX-1877] YJ50430012T\n[BBOX-1878] 胞的免疫反应。活化的 PD - 1 负性调节 T\n[BBOX-1879] 细胞活化，在肿瘤逃\n[BBOX-1880] 避宿主免疫中发挥关\n[BBOX-1881] 键作用。\n[BBOX-1882] 木单抗作为一线治疗，成人中低风险晚期\n[BBOX-1883] 肾细胞癌患者；b. 联合卡博替尼作为一\n[BBOX-1884] 线治疗，成人晚期肾细胞癌患者；c. 已\n[BBOX-1885] 接受过抗血管生成治疗的成年晚期肾细\n[BBOX-1886] 胞癌患者；5. 用于经自体造血干细胞移\n[BBOX-1887] 植(HSCT)和贝伦妥单抗-维多汀治疗后或\n[BBOX-1888] 包括自体 HSCT 在内的 3 种或 3 种\n[BBOX-1889] 以上系统疗法治疗的复发或进展的经典\n[BBOX-1890] 霍奇金淋巴瘤成人患者；6. 用于既往接\n[BBOX-1891] 受含铂类化疗方案治疗时或治疗后疾病\n[BBOX-1892] 进展的复发性或转移性头颈部鳞状细胞\n[BBOX-1893] 癌的成人患者；7. 用于尿路上皮癌患者：\n[BBOX-1894] a. 根治术后复发风险高的成人患者的辅\n[BBOX-1895] 助治疗；b. 在含铂化疗期间或之后出现\n[BBOX-1896] 疾病进展或新辅助治疗或辅助治疗 12 个\n[BBOX-1897] 月内疾病进展的局部晚期或转移性尿路\n[BBOX-1898] 上皮癌的成年患者；8. 单用或与伊匹木\n[BBOX-1899] 单抗联用于既往接受氟尿嘧啶、奥沙利\n[BBOX-1900] 铂、伊立替康治疗后疾病进展的微卫星高\n[BBOX-1901] 度不稳定（MSI-H）或错配修复缺陷\n[BBOX-1902] (dMMR) 的转移性结直肠癌成人和儿\n[BBOX-1903] 童患者(12 岁及以上)；9. 用于既往接受\n[BBOX-1904] 索拉非尼联合伊匹木单抗治疗的肝细胞\n[BBOX-1905] 癌成人患者；10. 用于食道癌患者：a.\n[BBOX-1906] 用于经新辅助放化疗（CRT）及完全手术\n[BBOX-1907] 切除后仍有病理学残留的食管癌或胃食\n[BBOX-1908] 管连接部癌的成人患者；b. 联合含氟尿\n[BBOX-1909] 嘧啶和含铂化疗作为一线治疗不能切除\n[BBOX-1910] 的晚期或转移性食管鳞状细胞癌的成人\n[BBOX-1911] 患者；c. 联合伊匹单抗作为一线治疗不\n[BBOX-1912] 可切除的晚期或转移性食管鳞状细胞癌\n[BBOX-1913] 成人患者；c. 用于先前以氟尿嘧啶和铂\n[BBOX-1914] 为基础的化疗后无法切除的晚期、复发或\n[BBOX-1915] 转移性食管鳞状细胞癌(ESCC)的成人患\n[BBOX-1916] 者；11. 联合含氟尿嘧啶和铂类药物化疗\n[BBOX-1917] 适用于晚期或转移性胃癌、胃食管连接部\n[BBOX-1918] 癌或食管腺癌成人患者。\n[BBOX-1919] 疗适用于一线治疗晚期或转\n[BBOX-1920] 移性胃癌、胃食管连接部癌\n[BBOX-1921] 或食管腺癌患者；6. 联合伊\n[BBOX-1922] 匹木单抗用于不可手术切除\n[BBOX-1923] 的、初治的非上皮样恶性胸\n[BBOX-1924] 膜间皮瘤成人患者；7. 用于\n[BBOX-1925] 经新辅助放化疗（CRT）及\n[BBOX-1926] 完全手术切除后仍有病理学\n[BBOX-1927] 残留的食管癌或胃食管连接\n[BBOX-1928] 部癌患者的辅助治疗；8. 联\n[BBOX-1929] 合含氟嘧啶类和铂类化疗用\n[BBOX-1930] 于晚期或转移性食管鳞癌患\n[BBOX-1931] 者的一线治疗。\n[BBOX-1932] — 22 —\n[BBOX-1933] 上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n[BBOX-1934] 奕检医学\n[BBOX-1935] YIJIANMED LABORATORY\n[BBOX-1936] YJ50430012T\n[BBOX-1937] Pembrolizumab\n[BBOX-1938] 帕博利珠单抗\n[BBOX-1939] 帕博利珠单抗\n[BBOX-1940] (Pembrolizumab)\n[BBOX-1941] 是一种针对人细胞表\n[BBOX-1942] 面受体 PD-1 (程序性\n[BBOX-1943] 死亡-1 或程序性细\n[BBOX-1944] 胞死亡-1) 的人源化\n[BBOX-1945] 单克隆免疫球蛋白\n[BBOX-1946] (Ig) G4 抗体，具\n[BBOX-1947] 有潜在的免疫检查点\n[BBOX-1948] 抑制和抗肿瘤活性。\n[BBOX-1949] 给药后，帕博利珠单\n[BBOX-1950] 抗与 PD-1 结合，\n[BBOX-1951] PD-1 是一种在活化\n[BBOX-1952] 的 T 细胞表面表达\n[BBOX-1953] 的抑制性信号受体，\n[BBOX-1954] 并阻断其配体对\n[BBOX-1955] PD-1 的结合和激活，\n[BBOX-1956] 从而导致 T 细胞介\n[BBOX-1957] 导的针对肿瘤细胞的\n[BBOX-1958] 免疫反应的激活。\n[BBOX-1959] PD-1 的配体包括在\n[BBOX-1960] 某些癌细胞上过表达\n[BBOX-1961] 的程序性细胞死亡配\n[BBOX-1962] 体 1 (PD-L1) 和主\n[BBOX-1963] 要在 APC 上表达的\n[BBOX-1964] 程序性细胞死亡配体\n[BBOX-1965] 2 (PD-L2) 。激活的\n[BBOX-1966] PD-1 负向调节 T 细\n[BBOX-1967] 胞活化，并在肿瘤逃\n[BBOX-1968] 避宿主免疫中发挥关\n[BBOX-1969] 键作用。\n[BBOX-1970] FDA 批准：1. 黑色素瘤：a. 用于无法切\n[BBOX-1971] 除或转移性黑色素瘤患者；b. 用于完全\n[BBOX-1972] 切除后淋巴结受累黑色素瘤患者的辅助\n[BBOX-1973] 治疗；2. 非小细胞肺癌： a. 联合培美曲\n[BBOX-1974] 塞和铂类化疗用于无 EGFR 突变或 ALK\n[BBOX-1975] 重排转移性非鳞状 NSCLC 患者的一线治\n[BBOX-1976] 疗；b. 联合卡铂+紫杉醇或白蛋白紫杉醇\n[BBOX-1977] 用于转移性鳞状 NSCLC 患者的一线治\n[BBOX-1978] 疗；c. 单药用于 PD-L1 TPS≥1% (经 FDA\n[BBOX-1979] 批准的检测) 且无 EGFR 突变或 ALK 重\n[BBOX-1980] 排的转移性非小细胞肺癌的一线治疗，不\n[BBOX-1981] 适合手术切除或根治性放化疗或转移的\n[BBOX-1982] III 期患者；d. 单药用于 PD-L1 TPS≥1%、\n[BBOX-1983] 铂类化疗期间或之后进展的转移性非小\n[BBOX-1984] 细胞肺癌；携带 EGFR 或 ALK 突变的患\n[BBOX-1985] 者在接受 FDA 批准疗法后仍出现疾病进\n[BBOX-1986] 展的非小细胞肺癌；e. 作为手术切除和\n[BBOX-1987] 铂类化疗后的辅助治疗，用于 IB 期 (T2a\n[BBOX-1988] ≥4 厘米) 、II 期或 IIIA 期非小细胞肺\n[BBOX-1989] 癌 (NSCLC) 患者；3. 小细胞肺癌：\n[BBOX-1990] 单药用于铂类期间或之后且既往至少一\n[BBOX-1991] 种其他治疗后进展的转移性小细胞肺癌\n[BBOX-1992] (SCLC) 患者；4. 头颈癌：a. 联合铂类\n[BBOX-1993] +5-FU 用于转移性或不可切除复发的头\n[BBOX-1994] 颈部鳞癌 (HNSCC) 的一线治疗；b. 单\n[BBOX-1995] 药用于 PD-L1 CPS≥1 (FDA 批准的检测\n[BBOX-1996] 方法) 的转移性或不可切除的复发性\n[BBOX-1997] HNSCC 患者的一线治疗；c. 单药用于铂\n[BBOX-1998] 类化疗期间或之后进展的复发或转移性\n[BBOX-1999] 头颈部鳞癌；5. 霍奇金淋巴瘤：用于难\n[BBOX-2000] 治性经典霍奇金淋巴瘤 (cHL) 的成人及\n[BBOX-2001] 儿童患者，或经过 3 种及以上前线治疗后\n[BBOX-2002] 复发的 cHL 患者的单一疗法；6. 原发性\n[BBOX-2003] 纵隔大 B 细胞淋巴瘤 (PMBCL) ：用于\n[BBOX-2004] 治疗难治性成人和儿童原发性纵隔大 B\n[BBOX-2005] 细胞淋巴瘤 (PMBCL) 患者，或两线及\n[BBOX-2006] 以上治疗后复发的患者；7. 尿路上皮癌：\n[BBOX-2007] a. 单药用于不适合铂类为基础的化疗方\n[BBOX-2008] 案的 PD-L1 CPS≥10 的局部晚期或转移\n[BBOX-2009] 性尿路上皮癌或不论 PD-L1 状态如何，\n[BBOX-2010] 不适合任何含铂方案的患者；b. 单药用\n[BBOX-2011] 于含铂化疗期间或之后进展、或经含铂新\n[BBOX-2012] 辅助或辅助化疗后 12 月内疾病进展的局\n[BBOX-2013] 部晚期或转移性尿路上皮癌；c. 联合\n[BBOX-2014] enfortumab vedotin-ejfv 治疗不符合\n[BBOX-2015] NMPA 批准：1. 用于经一线\n[BBOX-2016] 治疗失败的不可切除或转移\n[BBOX-2017] 性黑色素瘤的治疗；2. 非小\n[BBOX-2018] 细胞肺癌：a. 用于由国家药\n[BBOX-2019] 品监督管理局批准的检测评\n[BBOX-2020] 估为 PD-L1 肿瘤比例分数\n[BBOX-2021] (TPS) ≥1%的表皮生长因\n[BBOX-2022] 子受体 (EGFR) 基因突变阴\n[BBOX-2023] 性和间变性淋巴瘤激酶\n[BBOX-2024] (ALK) 阴性的局部晚期或\n[BBOX-2025] 转移性非小细胞肺癌一线单\n[BBOX-2026] 药治疗；b. 联合培美曲塞和\n[BBOX-2027] 铂类化疗适用于表皮生长因\n[BBOX-2028] 子受体 (EGFR) 基因突变阴\n[BBOX-2029] 性和间变性淋巴瘤激酶\n[BBOX-2030] (ALK) 阴性的转移性非鳞\n[BBOX-2031] 状非小细胞肺癌 (NSCLC)\n[BBOX-2032] 的一线治疗；c. 抗联合卡铂\n[BBOX-2033] 和紫杉醇适用于转移性鳞状\n[BBOX-2034] 非小细胞肺癌 (NSCLC) 患\n[BBOX-2035] 者的一线治疗；3. 食管癌：\n[BBOX-2036] a. 联合铂类和氟尿嘧啶类\n[BBOX-2037] 化疗药物用于局部晚期不可\n[BBOX-2038] 切除或转移性食管或胃食管\n[BBOX-2039] 结合部癌患者的一线治疗；\n[BBOX-2040] b. 单药用于由国家药品监\n[BBOX-2041] 督管理局批准的检测评估肿\n[BBOX-2042] 瘤表达 PD-L1 (综合阳性评\n[BBOX-2043] 分 (CPS) ≥10) 的、既往\n[BBOX-2044] 一线全身治疗失败的、局部\n[BBOX-2045] 晚期或转移性食管鳞状细胞\n[BBOX-2046] 癌 (ESCC) 患者的治疗；4.\n[BBOX-2047] 单药用于通过充分验证的检\n[BBOX-2048] 测评估肿瘤表达 PD-L1 (综\n[BBOX-2049] 合阳性评分 (CPS) ≥20)\n[BBOX-2050] 的转移性或不可切除的复发\n[BBOX-2051] 性头颈部鳞状细胞癌\n[BBOX-2052] (HNSCC) 患者的一线治\n[BBOX-2053] 疗；5. 单药用于 KRAS、\n[BBOX-2054] NRAS 和 BRAF 基因均为野\n[BBOX-2055] 生型，不可切除或转移性微\n[BBOX-2056] 卫星高度不稳定型 (MSI-H)\n[BBOX-2057] 或错配修复基因缺陷型\n[BBOX-2058] (dMMR) 结直肠癌 (CRC)\n[BBOX-2059] 患者的一线治疗；6. 单药用\n[BBOX-2060] — 23 —\n[BBOX-2061] 上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n[BBOX-2062] 奕检医学\n[BBOX-2063] YIJIANMED LABORATORY\n[BBOX-2064] YJ50430012T\n[BBOX-2065] 含顺铂化疗条件的局部晚期或转移性尿\n[BBOX-2066] 路上皮癌（la/mUC）成年患者；8. 乳腺\n[BBOX-2067] 癌：a. 与化疗联合用于治疗局部复发的\n[BBOX-2068] 不可切除或转移性三阴性乳腺癌患者\n[BBOX-2069] (TNBC)，其肿瘤表达 PD-L1（由 FDA\n[BBOX-2070] 批准的测试确定的综合阳性评分[CPS]≥\n[BBOX-2071] 10）；b. 联合化疗作为新辅助治疗治疗\n[BBOX-2072] 高危早期三阴性乳腺癌患者，然后继续作\n[BBOX-2073] 为手术后的单药辅助治疗；9. 胃癌：a. 单\n[BBOX-2074] 药用于经 2 种及以上前线治疗（包括含氟\n[BBOX-2075] 尿嘧啶和含铂类化疗方案）进展、PD-L1\n[BBOX-2076] CPS≥1 的复发性局部晚期或转移性胃癌\n[BBOX-2077] /胃食管结合部腺癌（GEJ）患者；b. 联\n[BBOX-2078] 合曲妥珠单抗、含氟嘧啶和含铂化疗，用\n[BBOX-2079] 于局部晚期不可切除或转移性 HER2 阳\n[BBOX-2080] 性胃癌或胃食管交界处（GEJ）腺癌患者\n[BBOX-2081] 的一线治疗；10. 食管癌：a. 单药用于\n[BBOX-2082] 经一种及以上全身治疗进展、PD-L1 CPS\n[BBOX-2083] ≥10 的复发性局部晚期或转移性食管鳞\n[BBOX-2084] 状细胞癌患者；b. 用于治疗局部晚期或\n[BBOX-2085] 转移性食管或胃食管交界处（GEJ）（震\n[BBOX-2086] 中在 GEJ 上方 1 至 5 厘米的肿瘤）癌患\n[BBOX-2087] 者，不适合手术切除或最终放化疗联合铂\n[BBOX-2088] 和氟嘧啶化疗；11. 宫颈癌：a. 单药用\n[BBOX-2089] 于化疗期间或之后进展、PD-L1 CPS≥1\n[BBOX-2090] 的复发或转移性宫颈癌患者；b. 加化疗，\n[BBOX-2091] 联合或不联合贝伐珠单抗，用于治疗肿瘤\n[BBOX-2092] 表达 PD-L1 的持续性，复发性或转移性\n[BBOX-2093] 宫颈癌患者（CPS ≥1）；12. 肝细胞癌\n[BBOX-2094] (HCC)：单药用于索拉非尼治疗后进展\n[BBOX-2095] 的 HCC 患者；13. Merkel 细胞癌\n[BBOX-2096] (MCC)：单药用于复发局部晚期或转\n[BBOX-2097] 移性 MCC 成人和儿童患者；14. 肾细胞\n[BBOX-2098] 癌：a. 帕博利珠单抗联合阿西替尼用于\n[BBOX-2099] 晚期肾细胞癌（RCC）患者的一线治疗；\n[BBOX-2100] b. 联合 lenvatinib 用于晚期肾细胞癌\n[BBOX-2101] (RCC) 成人患者的一线治疗；c. 用于\n[BBOX-2102] 肾切除术后或肾切除术和转移性病变切\n[BBOX-2103] 除术后复发风险为中高或高风险的 RCC\n[BBOX-2104] 患者的辅助治疗；15. 子宫内膜癌：联合\n[BBOX-2105] lenvatinib 治疗非微卫星不稳定性高\n[BBOX-2106] (MSI-H) 或错配修复缺陷 (dMMR)\n[BBOX-2107] 的晚期子宫内膜癌患者，他们在既往全身\n[BBOX-2108] 治疗后有疾病进展，不适合根治性手术或\n[BBOX-2109] 放疗；16. 膀胱癌：作为单药治疗卡介苗\n[BBOX-2110] 于既往接受过索拉非尼或含\n[BBOX-2111] 奥沙利铂化疗的肝细胞癌\n[BBOX-2112] (HCC) 患者的治疗；7. 联\n[BBOX-2113] 合吉西他滨和顺铂用于局部\n[BBOX-2114] 晚期或转移性胆道癌 (BTC)\n[BBOX-2115] 患者的一线治疗；8. 联合化\n[BBOX-2116] 疗新辅助治疗并在手术后继\n[BBOX-2117] 续帕博利珠单抗单药辅助治\n[BBOX-2118] 疗，用于经充分验证的检测\n[BBOX-2119] 评估肿瘤表达 PD-L1（综合\n[BBOX-2120] 阳性评分（CPS）≥20）的\n[BBOX-2121] 早期高危三阴性乳腺癌\n[BBOX-2122] (TNBC) 患者的治疗；9. 抗\n[BBOX-2123] 单药用于不可切除或转移性\n[BBOX-2124] 微卫星高度不稳定型\n[BBOX-2125] (MSI-H) 或错配修复基因\n[BBOX-2126] 缺陷型 (dMMR) 成人晚期\n[BBOX-2127] 实体瘤患者：a. 既往接受过\n[BBOX-2128] 氟尿嘧啶类、奥沙利铂和伊\n[BBOX-2129] 立替康治疗后疾病进展的结\n[BBOX-2130] 直肠癌患者；b. 既往治疗后\n[BBOX-2131] 疾病进展且无满意替代治疗\n[BBOX-2132] 方案的其他实体瘤；10. 联\n[BBOX-2133] 合含氟尿嘧啶类和铂类药物\n[BBOX-2134] 化疗用于局部晚期不可切除\n[BBOX-2135] 或转移性 HER2-阴性胃或胃\n[BBOX-2136] 食管结合部腺癌患者的一线\n[BBOX-2137] 治疗。\n[BBOX-2138] — 24 —\n[BBOX-2139] 上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n[BBOX-2140] 奕检医学\n[BBOX-2141] YIJIANMED LABORATORY\n[BBOX-2142] YJ50430012T\n[BBOX-2143] (BCG) 无反应、高风险、非肌肉浸润性\n[BBOX-2144] 膀胱癌 (NMIBC) 合并原位癌 (CIS) 伴\n[BBOX-2145] 或不伴乳头状肿瘤且不适合或选择不接\n[BBOX-2146] 受膀胱切除术的患者；17. 皮肤鳞状细胞\n[BBOX-2147] 癌：作为单药用于治疗无法通过手术或放\n[BBOX-2148] 疗治愈的复发性或转移性皮肤鳞状细胞\n[BBOX-2149] 癌 (cSCC) 患者；18. 用于治疗成人和\n[BBOX-2150] 儿童患者不可切除或转移性肿瘤突变负\n[BBOX-2151] 荷高 (TMB-H) [≥10 个突变/兆碱基\n[BBOX-2152] (mut/Mb)] 实体瘤；19. 单药用于治\n[BBOX-2153] 疗无法切除或转移性的 MSI-H 或错配修\n[BBOX-2154] 复缺陷 (dMMR) 的成人和儿童患者，实\n[BBOX-2155] 体肿瘤经先前治疗进展、并且没有令人满\n[BBOX-2156] 意的替代治疗方案的实体瘤患者，氟尿嘧\n[BBOX-2157] 啶，奥沙利铂和伊立替康治疗后进展的结\n[BBOX-2158] 直肠癌，用于不可切除或转移性 MSI-H\n[BBOX-2159] 或 dMMR 结直肠癌患者的一线治疗（帕\n[BBOX-2160] 博利珠单抗 MSI-H 中枢神经系统肿瘤的\n[BBOX-2161] 儿童患者中的安全性和有效性尚未确定）；\n[BBOX-2162] 20. 用于治疗成人和儿童患者不可切除\n[BBOX-2163] 或转移性微卫星不稳定性高 (MSI-H) 或\n[BBOX-2164] 错配修复缺陷 (dMMR) 实体瘤。\n[BBOX-2165] Ramucirumab\n[BBOX-2166] 雷莫西尤单抗\n[BBOX-2167] 雷莫西尤单抗\n[BBOX-2168] (Ramucirumab) 是\n[BBOX-2169] VEGFR-2 拮抗剂。\n[BBOX-2170] NCCN 指南推荐雷莫\n[BBOX-2171] 西尤单抗作为单药或\n[BBOX-2172] 联合紫杉醇作为晚期\n[BBOX-2173] 或转移性胃腺癌患者\n[BBOX-2174] 二线或后续治疗的选\n[BBOX-2175] 择。转移性结直肠癌\n[BBOX-2176] 经贝伐珠单抗联合奥\n[BBOX-2177] 沙利铂和 5-Fu 一线治\n[BBOX-2178] 疗失败后，二线雷莫\n[BBOX-2179] 西尤单抗联合\n[BBOX-2180] FOLFIRI 方案可以提\n[BBOX-2181] 供一定的临床获益。\n[BBOX-2182] FDA 批准：1. 作为单药或与紫杉醇联合\n[BBOX-2183] 用于治疗铂或氟嘧啶一线化疗难治或进\n[BBOX-2184] 展的晚期胃癌或 EGJ 腺癌患者；2. 作为\n[BBOX-2185] 单药治疗甲胎蛋白 (AFP) ≥400 ng/mL\n[BBOX-2186] 且既往接受过索拉非尼治疗的肝细胞癌\n[BBOX-2187] (HCC) 患者；3. 与厄洛替尼联合用于\n[BBOX-2188] 表皮生长因子受体 (EGFR) 19 号外显子\n[BBOX-2189] 缺失或 21 号外显子突变 (L858R) 的转\n[BBOX-2190] 移性非小细胞肺癌 (NSCLC) 的一线治\n[BBOX-2191] 疗。4. 联合多西他赛，用于治疗铂类化\n[BBOX-2192] 疗上或化疗后疾病进展的转移性非小细\n[BBOX-2193] 胞肺癌。对于 EGFR 或 ALK 基因异常的\n[BBOX-2194] 患者，在接受 CYRAMZA 治疗之前，FDA\n[BBOX-2195] 批准的针对 EGFR 或 ALK 基因异常的治\n[BBOX-2196] 疗应该有疾病进展。5. 与 FOLFIRI 联合，\n[BBOX-2197] 用于治疗在贝伐单抗、奥沙利铂和氟嘧啶\n[BBOX-2198] 治疗期间或之后疾病进展的转移性结直\n[BBOX-2199] 肠癌。\n[BBOX-2200] NMPA 批准：1. 与紫杉醇\n[BBOX-2201] 联合用于在含氟尿嘧啶类或\n[BBOX-2202] 含铂类化疗期间或化疗后出\n[BBOX-2203] 现疾病进展的晚期胃或胃食\n[BBOX-2204] 管结合部腺癌患者的治疗；\n[BBOX-2205] 2. 用于既往接受过索拉非\n[BBOX-2206] 尼治疗且甲胎蛋白 (AFP) ≥\n[BBOX-2207] 400 ng/mL 的肝细胞癌\n[BBOX-2208] (HCC) 患者的治疗。\n[BBOX-2209] — 25 —\n[BBOX-2210] 上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n[BBOX-2211] 奕检医学\n[BBOX-2212] YIJIANMED LABORATORY\n[BBOX-2213] YJ50430012T\n[BBOX-2214] Dostarlimab-gxly\n[BBOX-2215] Dostarlimab-gxly 是\n[BBOX-2216] 一种针对阴性免疫调\n[BBOX-2217] 节性人细胞表面受体\n[BBOX-2218] 程序性细胞死亡 1\n[BBOX-2219] (PD-1;程序性死亡\n[BBOX-2220] -1) 的人源化单克隆\n[BBOX-2221] 抗体，具有潜在的免\n[BBOX-2222] 疫检查点抑制和抗肿\n[BBOX-2223] 瘤活性。给药后，\n[BBOX-2224] dostarlimab 结合并\n[BBOX-2225] 抑制 PD-1 及其下游\n[BBOX-2226] 信号通路。这可能通\n[BBOX-2227] 过激活 T 细胞来恢\n[BBOX-2228] 复免疫功能。PD-1 是\n[BBOX-2229] 一种在 T 细胞上表\n[BBOX-2230] 达的 Ig 超家族中的\n[BBOX-2231] 跨膜蛋白，当被其配\n[BBOX-2232] 体程序性细胞死亡受\n[BBOX-2233] 体配体 1 （PD-L1）\n[BBOX-2234] 或 2（PD-L2）激活\n[BBOX-2235] 时，它作为免疫检查\n[BBOX-2236] 点蛋白发挥作用，负\n[BBOX-2237] 向调节 T 细胞活化\n[BBOX-2238] 和 T 细胞介导的免\n[BBOX-2239] 疫反应；它在肿瘤逃\n[BBOX-2240] 避宿主免疫中起重要\n[BBOX-2241] 作用。\n[BBOX-2242] FDA 批准：1. 用于治疗复发或晚期错配\n[BBOX-2243] 修复缺陷(dMMR)的成年患者：a. 经\n[BBOX-2244] FDA 批准的试验确定的子宫内膜癌，在\n[BBOX-2245] 接受含铂方案治疗后或在接受含铂方案\n[BBOX-2246] 治疗后进展，不适合进行治疗性手术或放\n[BBOX-2247] 疗；b. 经 FDA 批准的试验确定的实体肿\n[BBOX-2248] 瘤，在之前的治疗中或之后已经进展，并\n[BBOX-2249] 且没有令人满意的替代治疗方案；2. 与\n[BBOX-2250] 卡铂和紫杉醇联合使用，随后作为单一药\n[BBOX-2251] 物用于治疗原发性晚期或复发性子宫内\n[BBOX-2252] 膜癌成年患者。\n[BBOX-2253] 无\n[BBOX-2254] Ziv-aflibercept\n[BBOX-2255] Ziv-aflibercept 是一\n[BBOX-2256] 种重组蛋白。\n[BBOX-2257] Afilbercept 作为可\n[BBOX-2258] 溶性诱饵受体，与促\n[BBOX-2259] 血管生成血管内皮生\n[BBOX-2260] 长因子 （VEGF） 结\n[BBOX-2261] 合，从而阻止 VEGF\n[BBOX-2262] 与其内源性受体结\n[BBOX-2263] 合。破坏 VEGF 与其\n[BBOX-2264] 细胞受体的结合可能\n[BBOX-2265] 导致肿瘤血管生成、\n[BBOX-2266] 转移和最终肿瘤消退\n[BBOX-2267] 的抑制。\n[BBOX-2268] FDA 批准：ziv-afliberept 与氟尿嘧啶,\n[BBOX-2269] 亚叶酸钙，伊立替康（FOLFIRI）联合使\n[BBOX-2270] 用，用于治疗奥沙利铂治疗方案耐药或进\n[BBOX-2271] 展的转移性结直肠癌（mCRC）患者。\n[BBOX-2272] 无\n[BBOX-2273] — 26 —\n[BBOX-2274] 上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n[BBOX-2275] 奕检医学\n[BBOX-2276] YIJIANMED LABORATORY\n[BBOX-2277] YJ50430012T\n[BBOX-2278] 参考文献\n[BBOX-2279] 临床指南与共识\n[BBOX-2280] 1) NCCN Guideline: Colon Cancer (Version: 5.2024).\n[BBOX-2281] 2) NCCN Guideline: Rectal Cancer (Version: 4.2024).\n[BBOX-2282] 3) A framework to rank genomic alterations as targets for cancer precision medicine: the ESMO Scale\n[BBOX-2283] for Clinical Actionability of molecular Targets (ESCAT). PMID: 30137196.\n[BBOX-2284] 4) Recommendations for the use of next-generation sequencing (NGS) for patients with advanced\n[BBOX-2285] cancer in 2024: a report from the ESMO Precision Medicine Working Group. PMID: 38834388.\n[BBOX-2286] 5) A Canadian guideline on the use of next-generation sequencing in oncology. Curr Oncol. PMID:\n[BBOX-2287] 31043833.\n[BBOX-2288] 6) Therapeutic landscape and future direction of metastatic colorectal cancer. PMID: 36670267.\n[BBOX-2289] 7) Targeting BRAF and RAS in Colorectal Cancer. PMID: 34063682.\n[BBOX-2290] 8) BRAF and KRAS mutations in metastatic colorectal cancer: future perspectives for personalized\n[BBOX-2291] therapy. PMID: 32665851.\n[BBOX-2292] 9) RAS genes in colorectal carcinoma: pathogenesis, testing guidelines and treatment implications.\n[BBOX-2293] PMID: 30425122.\n[BBOX-2294] 10) BRAF Mutated Colorectal Cancer: New Treatment Approaches. PMID: 32545884.\n[BBOX-2295] 11) Exploring the best treatment options for BRAF-mutant metastatic colon cancer. PMID: 31353365.\n[BBOX-2296] 12) Mismatch repair deficiency testing in colorectal cancer and factors associated with nonadherence\n[BBOX-2297] to guidelines. https://doi.org/10.1200/JCO.2020.38.15_suppl.e16069.\n[BBOX-2298] 13) Molecular and clinical characteristics of POLE/POLD1 alterations among patients with colorectal\n[BBOX-2299] cancer. https://doi.org/10.1200/JCO.2024.42.3_suppl.184.\n[BBOX-2300] 14) 中国临床肿瘤学会 (CSCO) 结直肠癌诊疗指南 2024.\n[BBOX-2301] 15) 中国临床肿瘤学会 (CSCO) 免疫检查点抑制剂临床应用指南 2024.\n[BBOX-2302] 16) 中国临床肿瘤学会 (CSCO) 免疫检查点抑制剂相关的毒性管理指南 2023.\n[BBOX-2303] 17) 《肿瘤二代测序临床报告解读共识》, 循证医学 2022 年第 22 卷第 2 期.\n[BBOX-2304] 18) 《ctDNA 高通量测序临床实践专家共识 (2022 年版)》, 中国癌症防治杂志 2022 年 6 月第 14 卷第 3 期.\n[BBOX-2305] 19) 《二代测序技术在肿瘤精准医学诊断中的应用专家共识 (2018)》,中华医学杂志 2018 年 7 月 10 日第 98\n[BBOX-2306] 卷第 26 期.\n[BBOX-2307] 20) 《结直肠癌分子标志物临床检测中国专家共识》, 中华胃肠外科杂志 2021 年 3 月第 24 卷第 3 期.\n[BBOX-2308] 21) 《结直肠癌分子检测高通量测序中国专家共识》, 临床肿瘤学杂志 2021 年 3 月第 26 卷第 3 期.\n[BBOX-2309] — 27 —\n[BBOX-2310] 上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com"
  }
]
2026-08-10 14:54:50,598 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:54:50.596+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 64, "failed": 0, "current": {"7630dbd094ca11f1bd9827cf206dfa2d": {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:55:08,611 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:55:08,648 INFO     29 [SmartSplitter] SmartSplitter done: 16 chunks from 16 LLM segments (all bbox_id). Types: {'ExaminationReport': 8, 'DischargeRecord': 2, 'LabReport': 6}
2026-08-10 14:55:08,666 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 14:55:08,667 INFO     29 [Trace] task=7630dbd0 | doc=YXHU  62  男  直肠癌肺转移  贵州(2).pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "2311 items", "markdown": "", "text": "", "name": "YXHU  62  男  直肠癌肺转移  贵州(2).pdf", "output_format": "chunks", "chunks": "16 items, types={'ExaminationReport': 8, 'DischargeRecord': 2, 'LabReport': 6}"}
2026-08-10 14:55:08,667 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 14:55:08,672 INFO     29 [ChunkRouter] Routed 16 chunks into 3 groups: {'chunks_Examination': 8, 'chunks_Discharge': 2, 'chunks_LabExam': 6}
2026-08-10 14:55:08,686 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 14:55:08,686 INFO     29 [Trace] task=7630dbd0 | doc=YXHU  62  男  直肠癌肺转移  贵州(2).pdf | ChunkRouter:Router | outputs={"html": "", "json": "2311 items", "markdown": "", "text": "", "name": "YXHU  62  男  直肠癌肺转移  贵州(2).pdf", "output_format": "chunks", "chunks": "16 items, types={'ExaminationReport': 8, 'DischargeRecord': 2, 'LabReport': 6}", "chunks_Examination": "8 items, types={'ExaminationReport': 8}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_LabExam": "6 items, types={'LabReport': 6}", "route_summary": "{\"chunks_Examination\": 8, \"chunks_Discharge\": 2, \"chunks_LabExam\": 6}"}
2026-08-10 14:55:08,686 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 14:55:08,697 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 14:55:08,698 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 14:55:08,698 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[13]
2026-08-10 14:55:08,698 INFO     29 [qwen-vl-table] positions ： [[13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 14:55:08,805 INFO     29 [qwen-vl-table] page=13, rect=842x595, img=(2339x1654)
2026-08-10 14:55:08,805 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:55:08,805 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 400, \"bbox_end\": 437, \"encounter_dates\": [\"2026-02-19\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llll}\n报告时间: 2026-02-19\n\\hline\n项目 & 结果 & 参考范围 & \\\\\n\\hline\n白细胞计数 & 9.23 & 3.90-9.50/10~9/L & \\\\\n中性粒细胞百分率 & 70.50 & 40.00-75.00/\\% & \\\\\n淋巴细胞百分率 & 18.60 $\\downarrow$ & 20.00-50.00/\\% & \\\\\n单核细胞百分率 & 6.90 & 3.00-10.00/\\% & \\\\\n嗜酸性粒细胞百分率 & 3.30 & 0.40-8.00/\\% & \\\\\n嗜碱性粒细胞百分率 & 0.70 $\\uparrow$ & 0.02-0.52/\\% & \\\\\n大的未染色细胞计数 & 0.03 & 0.00-0.40/10~9/L & \\\\\n中性粒细胞绝对值 & 6.51 $\\uparrow$ & 1.80-6.30/10~9/L & \\\\\n淋巴细胞绝对值 & 1.72 & 1.10-3.20/10~9/L & \\\\\n单核细胞绝对值 & 0.64 $\\uparrow$ & 0.10-0.60/10~9/L & \\\\\n嗜酸性粒细胞绝对值 & 0.30 & 0.02-0.52/10~9/L & \\\\\n\\hline\n\\end{tabular}\n\\begin{tabular}{llll}\n报告时间: 2026-02-19\n\\hline\n项目 & 结果 & 参考范围 & \\\\\n\\hline\n嗜碱性粒细胞绝对值 & 0.06 & 0.02-0.06/10~9/L & \\\\\n大的未染色细胞百分率 & 0.30 & 0.00-4.00/\\% & \\\\\n红细胞计数 & 4.34 & 4.30-5.80/10~12/L & \\\\\n血红蛋白 & 125.00 $\\downarrow$ & 130.00-175.00/g/L & \\\\\n红细胞比积 & 38.60 $\\downarrow$ & 40.00-50.00/\\% & \\\\\n红细胞平均体积 & 88.90 & 82.00-100.00/fl & \\\\\n红细胞平均血红蛋白量 & 28.70 & 27.00-34.00/pg & \\\\\n红细胞平均血红蛋白浓度 & 324.00 & 316.00-354.00/g/L & \\\\\n红细胞体积分布宽度变异系数 & 14.30 & 12.00-16.00/\\% & \\\\\n红细胞体积分布宽度标准差 & 44.90 & 35.00-56.00/fl & \\\\\n血小板计数 & 458.00 $\\uparrow$ & 125.00-350.00/10~9/L & \\\\\n血小板平均体积 & 7.10 $\\downarrow$ & 8.30-17.40/fl & \\\\\nC反应蛋白 & 18.29 $\\uparrow$ & 0.00-10.00/mg/L & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 14:55:21,395 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:55:21.392+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 64, "failed": 0, "current": {"7630dbd094ca11f1bd9827cf206dfa2d": {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:55:22,258 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:55:22,258 INFO     29 [qwen-vl-table] page=13 LLM output (len=4170):
{
  "report_date": "2026-02-19",
  "items": [
    {
      "name": "白细胞计数",
      "item_code": null,
      "value": "9.23",
      "unit": "10^9/L",
      "reference_range": "3.90-9.50",
      "abnormal": false
    },
    {
      "name": "中性粒细胞百分率",
      "item_code": null,
      "value": "70.50",
      "unit": "%",
      "reference_range": "40.00-75.00",
      "abnormal": false
    },
    {
      "name": "淋巴细胞百分率",
      "item_code": null,
      "value": "18.60",
      "unit": "%",
      "reference_range": "20.00-50.00",
      "abnormal": true
    },
    {
      "name": "单核细胞百分率",
      "item_code": null,
      "value": "6.90",
      "unit": "%",
      "reference_range": "3.00-10.00",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞百分率",
      "item_code": null,
      "value": "3.30",
      "unit": "%",
      "reference_range": "0.40-8.00",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞百分率",
      "item_code": null,
      "value": "0.70",
      "unit": "%",
      "reference_range": "0.02-0.52",
      "abnormal": true
    },
    {
      "name": "大的未染色细胞计数",
      "item_code": null,
      "value": "0.03",
      "unit": "10^9/L",
      "reference_range": "0.00-0.40",
      "abnormal": false
    },
    {
      "name": "中性粒细胞绝对值",
      "item_code": null,
      "value": "6.51",
      "unit": "10^9/L",
      "reference_range": "1.80-6.30",
      "abnormal": true
    },
    {
      "name": "淋巴细胞绝对值",
      "item_code": null,
      "value": "1.72",
      "unit": "10^9/L",
      "reference_range": "1.10-3.20",
      "abnormal": false
    },
    {
      "name": "单核细胞绝对值",
      "item_code": null,
      "value": "0.64",
      "unit": "10^9/L",
      "reference_range": "0.10-0.60",
      "abnormal": true
    },
    {
      "name": "嗜酸性粒细胞绝对值",
      "item_code": null,
      "value": "0.30",
      "unit": "10^9/L",
      "reference_range": "0.02-0.52",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞绝对值",
      "item_code": null,
      "value": "0.06",
      "unit": "10^9/L",
      "reference_range": "0.02-0.06",
      "abnormal": false
    },
    {
      "name": "大的未染色细胞百分率",
      "item_code": null,
      "value": "0.30",
      "unit": "%",
      "reference_range": "0.00-4.00",
      "abnormal": false
    },
    {
      "name": "红细胞计数",
      "item_code": null,
      "value": "4.34",
      "unit": "10^12/L",
      "reference_range": "4.30-5.80",
      "abnormal": false
    },
    {
      "name": "血红蛋白",
      "item_code": null,
      "value": "125.00",
      "unit": "g/L",
      "reference_range": "130.00-175.00",
      "abnormal": true
    },
    {
      "name": "红细胞比积",
      "item_code": null,
      "value": "38.60",
      "unit": "%",
      "reference_range": "40.00-50.00",
      "abnormal": true
    },
    {
      "name": "红细胞平均体积",
      "item_code": null,
      "value": "88.90",
      "unit": "fl",
      "reference_range": "82.00-100.00",
      "abnormal": false
    },
    {
      "name": "红细胞平均血红蛋白量",
      "item_code": null,
      "value": "28.70",
      "unit": "pg",
      "reference_range": "27.00-34.00",
      "abnormal": false
    },
    {
      "name": "红细胞平均血红蛋白浓度",
      "item_code": null,
      "value": "324.00",
      "unit": "g/L",
      "reference_range": "316.00-354.00",
      "abnormal": false
    },
    {
      "name": "红细胞体积分布宽度变异系数",
      "item_code": null,
      "value": "14.30",
      "unit": "%",
      "reference_range": "12.00-16.00",
      "abnormal": false
    },
    {
      "name": "红细胞体积分布宽度标准差",
      "item_code": null,
      "value": "44.90",
      "unit": "fl",
      "reference_range": "35.00-56.00",
      "abnormal": false
    },
    {
      "name": "血小板计数",
      "item_code": null,
      "value": "458.00",
      "unit": "10^9/L",
      "reference_range": "125.00-350.00",
      "abnormal": true
    },
    {
      "name": "血小板平均体积",
      "item_code": null,
      "value": "7.10",
      "unit": "fl",
      "reference_range": "8.30-17.40",
      "abnormal": true
    },
    {
      "name": "C反应蛋白",
      "item_code": null,
      "value": "18.29",
      "unit": "mg/L",
      "reference_range": "0.00-10.00",
      "abnormal": true
    }
  ]
}
2026-08-10 14:55:22,259 INFO     29 [qwen-vl-table] coord grouping: {13: 24}
2026-08-10 14:55:22,261 INFO     29 [qwen-vl-table] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=614290, prompt_len=718
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
白细胞计数、中性粒细胞百分率、淋巴细胞百分率、单核细胞百分率、嗜酸性粒细胞百分率、嗜碱性粒细胞百分率、大的未染色细胞计数、中性粒细胞绝对值、淋巴细胞绝对值、单核细胞绝对值、嗜酸性粒细胞绝对值、嗜碱性粒细胞绝对值、大的未染色细胞百分率、红细胞计数、血红蛋白、红细胞比积、红细胞平均体积、红细胞平均血红蛋白量、红细胞平均血红蛋白浓度、红细胞体积分布宽度变异系数、红细胞体积分布宽度标准差、血小板计数、血小板平均体积、C反应蛋白

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
2026-08-10 14:55:31,013 INFO     29 [qwen-vl-table] coord API raw response (len=1270):
[
	{"text": "白细胞计数", "bbox": [118, 360, 174, 380]},
	{"text": "中性粒细胞百分率", "bbox": [118, 407, 207, 427]},
	{"text": "淋巴细胞百分率", "bbox": [118, 454, 196, 474]},
	{"text": "单核细胞百分率", "bbox": [118, 500, 196, 520]},
	{"text": "嗜酸性粒细胞百分率", "bbox": [118, 547, 207, 567]},
	{"text": "嗜碱性粒细胞百分率", "bbox": [118, 615, 207, 635]},
	{"text": "大的未染色细胞计数", "bbox": [118, 682, 207, 702]},
	{"text": "中性粒细胞绝对值", "bbox": [118, 749, 207, 769]},
	{"text": "淋巴细胞绝对值", "bbox": [118, 796, 196, 816]},
	{"text": "单核细胞绝对值", "bbox": [118, 843, 196, 863]},
	{"text": "嗜酸性粒细胞绝对值", "bbox": [118, 890, 207, 910]},
	{"text": "嗜碱性粒细胞绝对值", "bbox": [478, 203, 564, 223]},
	{"text": "大的未染色细胞百分率", "bbox": [478, 268, 564, 288]},
	{"text": "红细胞计数", "bbox": [478, 333, 532, 353]},
	{"text": "血红蛋白", "bbox": [478, 378, 521, 398]},
	{"text": "红细胞比积", "bbox": [478, 424, 532, 444]},
	{"text": "红细胞平均体积", "bbox": [478, 469, 554, 489]},
	{"text": "红细胞平均血红蛋白量", "bbox": [478, 514, 564, 534]},
	{"text": "红细胞平均血红蛋白浓度", "bbox": [478, 579, 564, 599]},
	{"text": "红细胞体积分布宽度变异系数", "bbox": [478, 645, 564, 665]},
	{"text": "红细胞体积分布宽度标准差", "bbox": [478, 709, 564, 729]},
	{"text": "血小板计数", "bbox": [478, 774, 532, 794]},
	{"text": "血小板平均体积", "bbox": [478, 839, 554, 859]},
	{"text": "C反应蛋白", "bbox": [478, 885, 528, 905]}
]
2026-08-10 14:55:31,013 INFO     29 [qwen-vl-table] coord API: raw_items=24, valid_items=24, elapsed=8.8s
2026-08-10 14:55:31,013 INFO     29 [qwen-vl-table] coord item[0]: text=白细胞计数, bbox=[118, 360, 174, 380]
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] coord item[1]: text=中性粒细胞百分率, bbox=[118, 407, 207, 427]
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] coord item[2]: text=淋巴细胞百分率, bbox=[118, 454, 196, 474]
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] coord item[3]: text=单核细胞百分率, bbox=[118, 500, 196, 520]
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] coord item[4]: text=嗜酸性粒细胞百分率, bbox=[118, 547, 207, 567]
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] coord item[5]: text=嗜碱性粒细胞百分率, bbox=[118, 615, 207, 635]
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] coord item[6]: text=大的未染色细胞计数, bbox=[118, 682, 207, 702]
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] coord item[7]: text=中性粒细胞绝对值, bbox=[118, 749, 207, 769]
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] coord item[8]: text=淋巴细胞绝对值, bbox=[118, 796, 196, 816]
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] coord item[9]: text=单核细胞绝对值, bbox=[118, 843, 196, 863]
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] coord item[10]: text=嗜酸性粒细胞绝对值, bbox=[118, 890, 207, 910]
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] coord item[11]: text=嗜碱性粒细胞绝对值, bbox=[478, 203, 564, 223]
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] coord item[12]: text=大的未染色细胞百分率, bbox=[478, 268, 564, 288]
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] coord item[13]: text=红细胞计数, bbox=[478, 333, 532, 353]
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] coord item[14]: text=血红蛋白, bbox=[478, 378, 521, 398]
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] coord item[15]: text=红细胞比积, bbox=[478, 424, 532, 444]
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] coord item[16]: text=红细胞平均体积, bbox=[478, 469, 554, 489]
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] coord item[17]: text=红细胞平均血红蛋白量, bbox=[478, 514, 564, 534]
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] coord item[18]: text=红细胞平均血红蛋白浓度, bbox=[478, 579, 564, 599]
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] coord item[19]: text=红细胞体积分布宽度变异系数, bbox=[478, 645, 564, 665]
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] coord item[20]: text=红细胞体积分布宽度标准差, bbox=[478, 709, 564, 729]
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] coord item[21]: text=血小板计数, bbox=[478, 774, 532, 794]
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] coord item[22]: text=血小板平均体积, bbox=[478, 839, 554, 859]
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] coord item[23]: text=C反应蛋白, bbox=[478, 885, 528, 905]
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] page=13 coord: matched 24/24, time=8.8s
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] new_positions (24):
[[14, 99.34420288085938, 146.49060424804688, 214.30799560546876, 226.21399536132813], [14, 99.34420288085938, 174.27330505371094, 242.2870950317383, 254.19309478759766], [14, 99.34420288085938, 165.01240478515626, 270.2661944580078, 282.1721942138672], [14, 99.34420288085938, 165.01240478515626, 297.6499938964844, 309.5559936523438], [14, 99.34420288085938, 174.27330505371094, 325.62909332275393, 337.5350930786133], [14, 99.34420288085938, 174.27330505371094, 366.10949249267577, 378.01549224853517], [14, 99.34420288085938, 174.27330505371094, 405.9945916748047, 417.90059143066406], [14, 99.34420288085938, 174.27330505371094, 445.8796908569336, 457.78569061279296], [14, 99.34420288085938, 165.01240478515626, 473.8587902832031, 485.7647900390625], [14, 99.34420288085938, 165.01240478515626, 501.8378897094727, 513.743889465332], [14, 99.34420288085938, 174.27330505371094, 529.8169891357422, 541.7229888916016], [14, 402.4282116699219, 474.83161376953126, 120.84589752197266, 132.75189727783203], [14, 402.4282116699219, 474.83161376953126, 159.54039672851565, 171.44639648437501], [14, 402.4282116699219, 447.89081298828125, 198.2348959350586, 210.14089569091797], [14, 402.4282116699219, 438.6299127197266, 225.0233953857422, 236.92939514160156], [14, 402.4282116699219, 447.89081298828125, 252.40719482421875, 264.3131945800781], [14, 402.4282116699219, 466.41261352539067, 279.19569427490234, 291.10169403076173], [14, 402.4282116699219, 474.83161376953126, 305.98419372558595, 317.89019348144535], [14, 402.4282116699219, 474.83161376953126, 344.6786929321289, 356.5846926879883], [14, 402.4282116699219, 474.83161376953126, 383.96849212646487, 395.87449188232426], [14, 402.4282116699219, 474.83161376953126, 422.0676913452149, 433.9736911010742], [14, 402.4282116699219, 447.89081298828125, 460.76219055175784, 472.6681903076172], [14, 402.4282116699219, 466.41261352539067, 499.4566897583008, 511.3626895141602], [14, 402.4282116699219, 444.523212890625, 526.8404891967774, 538.7464889526367]]
2026-08-10 14:55:31,014 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=24, matched=24, pages=1, time=22.3s
2026-08-10 14:55:31,015 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 14:55:31,016 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 14:55:31,016 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[14]
2026-08-10 14:55:31,016 INFO     29 [qwen-vl-table] positions ： [[14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 14:55:31,113 INFO     29 [qwen-vl-table] page=14, rect=842x595, img=(2339x1654)
2026-08-10 14:55:31,113 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:55:31,113 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 438, \"bbox_end\": 478, \"encounter_dates\": [\"2026-02-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{lll}\n报告时间: 2026-02-05\n\\hline\n检查日期 & 2026-02-05 11:52:00 & \\\\\n\\hline\n\\multicolumn{3}{l}{\\textbf{指标结果}} \\\\\n项目 & 结果 & 参考范围 \\\\\n谷丙转氨酶 & 15.40 & 9.00-60.00/U/L \\\\\n谷草转氨酶 & 18.50 & 15.00-45.00/U/L \\\\\n谷草/谷丙 & 1.20 & 0.80-1.40 \\\\\n总胆红素 & 11.90 & 3.40-17.10/μmol/L \\\\\n直接胆红素 & 5.00 \\text{↑} & 0.00-4.00/μmol/L \\\\\n间接胆红素 & 6.90 & 3.00-17.00/μmol/L \\\\\n总蛋白 & 69.800 & 65.000-80.000/g/L \\\\\n白蛋白 & 40.50 & 40.00-55.00/g/L \\\\\n碱性磷酸酶 & 87.00 & 45.00-125.00/U/L \\\\\nγ-谷氨酰基转移酶 & 32.00 & 10.00-60.00/U/L \\\\\n总胆汁酸 & 6.47 & 0.00-9.67/μmol/L \\\\\n尿素 & 5.40 & 3.00-9.20/mmol/L \\\\\n肌酐 & 96.00 & 59.00-104.00/μmol/L \\\\\n\\hline\n\\end{tabular}\n\\begin{tabular}{lll}\n报告时间: 2026-02-05\n\\hline\n肌酐 & 96.00 & 59.00-104.00/μmol/L \\\\\n尿素/肌酐 & 0.06 & 0.03-0.20 \\\\\n尿酸 & 248.00 & 208.00-428.00/μmol/L \\\\\n葡萄糖 & 7.28 \\text{↑} & 3.90-6.10/mmol/L \\\\\n钾 & 3.92 & 3.50-5.50/mmol/L \\\\\n钠 & 141.60 & 135.00-145.00/mmol/L \\\\\n氯 & 102.90 & 96.00-108.00/mmol/L \\\\\n钙 & 2.22 & 2.10-2.60/mmol/L \\\\\n镁 & 0.85 & 0.73-1.35/mmol/L \\\\\n磷 & 0.98 & 0.78-1.65/mmol/L \\\\\n前白蛋白 & 110.00 \\text{↓} & 200.00-400.00/mg/L \\\\\n胆碱酯酶 & 5602.00 & 4600.00-11500.00/U/L \\\\\n白蛋白/球蛋白 & 1.38 & 1.20-2.40 \\\\\n球蛋白 & 29.30 & 20.00-40.00/g/L \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 14:55:46,318 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:55:46,318 INFO     29 [qwen-vl-table] page=14 LLM output (len=4454):
{
  "report_date": "2026-02-05",
  "items": [
    {
      "name": "谷丙转氨酶",
      "item_code": null,
      "value": "15.40",
      "unit": "U/L",
      "reference_range": "9.00-60.00",
      "abnormal": false
    },
    {
      "name": "谷草转氨酶",
      "item_code": null,
      "value": "18.50",
      "unit": "U/L",
      "reference_range": "15.00-45.00",
      "abnormal": false
    },
    {
      "name": "谷草/谷丙",
      "item_code": null,
      "value": "1.20",
      "unit": null,
      "reference_range": "0.80-1.40",
      "abnormal": false
    },
    {
      "name": "总胆红素",
      "item_code": null,
      "value": "11.90",
      "unit": "μmol/L",
      "reference_range": "3.40-17.10",
      "abnormal": false
    },
    {
      "name": "直接胆红素",
      "item_code": null,
      "value": "5.00",
      "unit": "μmol/L",
      "reference_range": "0.00-4.00",
      "abnormal": true
    },
    {
      "name": "间接胆红素",
      "item_code": null,
      "value": "6.90",
      "unit": "μmol/L",
      "reference_range": "3.00-17.00",
      "abnormal": false
    },
    {
      "name": "总蛋白",
      "item_code": null,
      "value": "69.800",
      "unit": "g/L",
      "reference_range": "65.000-80.000",
      "abnormal": false
    },
    {
      "name": "白蛋白",
      "item_code": null,
      "value": "40.50",
      "unit": "g/L",
      "reference_range": "40.00-55.00",
      "abnormal": false
    },
    {
      "name": "碱性磷酸酶",
      "item_code": null,
      "value": "87.00",
      "unit": "U/L",
      "reference_range": "45.00-125.00",
      "abnormal": false
    },
    {
      "name": "γ-谷氨酰基转移酶",
      "item_code": null,
      "value": "32.00",
      "unit": "U/L",
      "reference_range": "10.00-60.00",
      "abnormal": false
    },
    {
      "name": "总胆汁酸",
      "item_code": null,
      "value": "6.47",
      "unit": "μmol/L",
      "reference_range": "0.00-9.67",
      "abnormal": false
    },
    {
      "name": "尿素",
      "item_code": null,
      "value": "5.40",
      "unit": "mmol/L",
      "reference_range": "3.00-9.20",
      "abnormal": false
    },
    {
      "name": "肌酐",
      "item_code": null,
      "value": "96.00",
      "unit": "μmol/L",
      "reference_range": "59.00-104.00",
      "abnormal": false
    },
    {
      "name": "尿素/肌酐",
      "item_code": null,
      "value": "0.06",
      "unit": null,
      "reference_range": "0.03-0.20",
      "abnormal": false
    },
    {
      "name": "尿酸",
      "item_code": null,
      "value": "248.00",
      "unit": "μmol/L",
      "reference_range": "208.00-428.00",
      "abnormal": false
    },
    {
      "name": "葡萄糖",
      "item_code": null,
      "value": "7.28",
      "unit": "mmol/L",
      "reference_range": "3.90-6.10",
      "abnormal": true
    },
    {
      "name": "钾",
      "item_code": null,
      "value": "3.92",
      "unit": "mmol/L",
      "reference_range": "3.50-5.50",
      "abnormal": false
    },
    {
      "name": "钠",
      "item_code": null,
      "value": "141.60",
      "unit": "mmol/L",
      "reference_range": "135.00-145.00",
      "abnormal": false
    },
    {
      "name": "氯",
      "item_code": null,
      "value": "102.90",
      "unit": "mmol/L",
      "reference_range": "96.00-108.00",
      "abnormal": false
    },
    {
      "name": "钙",
      "item_code": null,
      "value": "2.22",
      "unit": "mmol/L",
      "reference_range": "2.10-2.60",
      "abnormal": false
    },
    {
      "name": "镁",
      "item_code": null,
      "value": "0.85",
      "unit": "mmol/L",
      "reference_range": "0.73-1.35",
      "abnormal": false
    },
    {
      "name": "磷",
      "item_code": null,
      "value": "0.98",
      "unit": "mmol/L",
      "reference_range": "0.78-1.65",
      "abnormal": false
    },
    {
      "name": "前白蛋白",
      "item_code": null,
      "value": "110.00",
      "unit": "mg/L",
      "reference_range": "200.00-400.00",
      "abnormal": true
    },
    {
      "name": "胆碱酯酶",
      "item_code": null,
      "value": "5602.00",
      "unit": "U/L",
      "reference_range": "4600.00-11500.00",
      "abnormal": false
    },
    {
      "name": "白蛋白/球蛋白",
      "item_code": null,
      "value": "1.38",
      "unit": null,
      "reference_range": "1.20-2.40",
      "abnormal": false
    },
    {
      "name": "球蛋白",
      "item_code": null,
      "value": "29.30",
      "unit": "g/L",
      "reference_range": "20.00-40.00",
      "abnormal": false
    }
  ]
}
2026-08-10 14:55:46,318 INFO     29 [qwen-vl-table] coord grouping: {14: 26}
2026-08-10 14:55:46,319 INFO     29 [qwen-vl-table] coord API call start, page=14, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=551214, prompt_len=623
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
谷丙转氨酶、谷草转氨酶、谷草/谷丙、总胆红素、直接胆红素、间接胆红素、总蛋白、白蛋白、碱性磷酸酶、γ-谷氨酰基转移酶、总胆汁酸、尿素、肌酐、尿素/肌酐、尿酸、葡萄糖、钾、钠、氯、钙、镁、磷、前白蛋白、胆碱酯酶、白蛋白/球蛋白、球蛋白

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
2026-08-10 14:55:53,350 INFO     29 [qwen-vl-table] coord API raw response (len=1263):
[
	{"text": "谷丙转氨酶", "bbox": [118, 292, 173, 309]},
	{"text": "谷草转氨酶", "bbox": [118, 338, 173, 355]},
	{"text": "谷草/谷丙", "bbox": [118, 384, 167, 401]},
	{"text": "总胆红素", "bbox": [118, 430, 162, 447]},
	{"text": "直接胆红素", "bbox": [118, 476, 173, 493]},
	{"text": "间接胆红素", "bbox": [118, 522, 173, 539]},
	{"text": "总蛋白", "bbox": [118, 568, 151, 585]},
	{"text": "白蛋白", "bbox": [118, 614, 151, 631]},
	{"text": "碱性磷酸酶", "bbox": [118, 660, 173, 677]},
	{"text": "γ-谷氨酰基转移酶", "bbox": [118, 706, 205, 723]},
	{"text": "总胆汁酸", "bbox": [118, 752, 162, 769]},
	{"text": "尿素", "bbox": [118, 800, 140, 817]},
	{"text": "肌酐", "bbox": [118, 845, 140, 862]},
	{"text": "尿素/肌酐", "bbox": [413, 192, 462, 209]},
	{"text": "尿酸", "bbox": [413, 239, 435, 256]},
	{"text": "葡萄糖", "bbox": [413, 304, 446, 321]},
	{"text": "钾", "bbox": [413, 351, 424, 368]},
	{"text": "钠", "bbox": [413, 397, 424, 414]},
	{"text": "氯", "bbox": [413, 463, 424, 480]},
	{"text": "钙", "bbox": [413, 528, 424, 545]},
	{"text": "镁", "bbox": [413, 575, 424, 592]},
	{"text": "磷", "bbox": [413, 621, 424, 638]},
	{"text": "前白蛋白", "bbox": [413, 667, 457, 684]},
	{"text": "胆碱酯酶", "bbox": [413, 732, 457, 749]},
	{"text": "白蛋白/球蛋白", "bbox": [413, 798, 484, 815]},
	{"text": "球蛋白", "bbox": [413, 845, 446, 862]}
]
2026-08-10 14:55:53,350 INFO     29 [qwen-vl-table] coord API: raw_items=26, valid_items=26, elapsed=7.0s
2026-08-10 14:55:53,350 INFO     29 [qwen-vl-table] coord item[0]: text=谷丙转氨酶, bbox=[118, 292, 173, 309]
2026-08-10 14:55:53,350 INFO     29 [qwen-vl-table] coord item[1]: text=谷草转氨酶, bbox=[118, 338, 173, 355]
2026-08-10 14:55:53,350 INFO     29 [qwen-vl-table] coord item[2]: text=谷草/谷丙, bbox=[118, 384, 167, 401]
2026-08-10 14:55:53,351 INFO     29 [qwen-vl-table] coord item[3]: text=总胆红素, bbox=[118, 430, 162, 447]
2026-08-10 14:55:53,351 INFO     29 [qwen-vl-table] coord item[4]: text=直接胆红素, bbox=[118, 476, 173, 493]
2026-08-10 14:55:53,351 INFO     29 [qwen-vl-table] coord item[5]: text=间接胆红素, bbox=[118, 522, 173, 539]
2026-08-10 14:55:53,351 INFO     29 [qwen-vl-table] coord item[6]: text=总蛋白, bbox=[118, 568, 151, 585]
2026-08-10 14:55:53,351 INFO     29 [qwen-vl-table] coord item[7]: text=白蛋白, bbox=[118, 614, 151, 631]
2026-08-10 14:55:53,351 INFO     29 [qwen-vl-table] coord item[8]: text=碱性磷酸酶, bbox=[118, 660, 173, 677]
2026-08-10 14:55:53,351 INFO     29 [qwen-vl-table] coord item[9]: text=γ-谷氨酰基转移酶, bbox=[118, 706, 205, 723]
2026-08-10 14:55:53,351 INFO     29 [qwen-vl-table] coord item[10]: text=总胆汁酸, bbox=[118, 752, 162, 769]
2026-08-10 14:55:53,351 INFO     29 [qwen-vl-table] coord item[11]: text=尿素, bbox=[118, 800, 140, 817]
2026-08-10 14:55:53,351 INFO     29 [qwen-vl-table] coord item[12]: text=肌酐, bbox=[118, 845, 140, 862]
2026-08-10 14:55:53,351 INFO     29 [qwen-vl-table] coord item[13]: text=尿素/肌酐, bbox=[413, 192, 462, 209]
2026-08-10 14:55:53,351 INFO     29 [qwen-vl-table] coord item[14]: text=尿酸, bbox=[413, 239, 435, 256]
2026-08-10 14:55:53,351 INFO     29 [qwen-vl-table] coord item[15]: text=葡萄糖, bbox=[413, 304, 446, 321]
2026-08-10 14:55:53,351 INFO     29 [qwen-vl-table] coord item[16]: text=钾, bbox=[413, 351, 424, 368]
2026-08-10 14:55:53,351 INFO     29 [qwen-vl-table] coord item[17]: text=钠, bbox=[413, 397, 424, 414]
2026-08-10 14:55:53,351 INFO     29 [qwen-vl-table] coord item[18]: text=氯, bbox=[413, 463, 424, 480]
2026-08-10 14:55:53,351 INFO     29 [qwen-vl-table] coord item[19]: text=钙, bbox=[413, 528, 424, 545]
2026-08-10 14:55:53,351 INFO     29 [qwen-vl-table] coord item[20]: text=镁, bbox=[413, 575, 424, 592]
2026-08-10 14:55:53,351 INFO     29 [qwen-vl-table] coord item[21]: text=磷, bbox=[413, 621, 424, 638]
2026-08-10 14:55:53,351 INFO     29 [qwen-vl-table] coord item[22]: text=前白蛋白, bbox=[413, 667, 457, 684]
2026-08-10 14:55:53,351 INFO     29 [qwen-vl-table] coord item[23]: text=胆碱酯酶, bbox=[413, 732, 457, 749]
2026-08-10 14:55:53,351 INFO     29 [qwen-vl-table] coord item[24]: text=白蛋白/球蛋白, bbox=[413, 798, 484, 815]
2026-08-10 14:55:53,351 INFO     29 [qwen-vl-table] coord item[25]: text=球蛋白, bbox=[413, 845, 446, 862]
2026-08-10 14:55:53,351 INFO     29 [qwen-vl-table] page=14 coord: matched 26/26, time=7.0s
2026-08-10 14:55:53,351 INFO     29 [qwen-vl-table] new_positions (26):
[[15, 99.34420288085938, 145.64870422363282, 173.8275964355469, 183.94769622802735], [15, 99.34420288085938, 145.64870422363282, 201.21139587402345, 211.3314956665039], [15, 99.34420288085938, 140.59730407714844, 228.5951953125, 238.71529510498047], [15, 99.34420288085938, 136.38780395507814, 255.97899475097657, 266.09909454345706], [15, 99.34420288085938, 145.64870422363282, 283.36279418945315, 293.4828939819336], [15, 99.34420288085938, 145.64870422363282, 310.7465936279297, 320.8666934204102], [15, 99.34420288085938, 127.12690368652345, 338.13039306640627, 348.25049285888673], [15, 99.34420288085938, 127.12690368652345, 365.5141925048828, 375.6342922973633], [15, 99.34420288085938, 145.64870422363282, 392.8979919433594, 403.01809173583985], [15, 99.34420288085938, 172.58950500488282, 420.28179138183594, 430.4018911743164], [15, 99.34420288085938, 136.38780395507814, 447.6655908203125, 457.78569061279296], [15, 99.34420288085938, 117.86600341796876, 476.239990234375, 486.3600900268555], [15, 99.34420288085938, 117.86600341796876, 503.0284896850586, 513.1485894775391], [15, 347.70471008300785, 388.9578112792969, 114.29759765625, 124.41769744873048], [15, 347.70471008300785, 366.2265106201172, 142.27669708251955, 152.396796875], [15, 347.70471008300785, 375.4874108886719, 180.9711962890625, 191.09129608154296], [15, 347.70471008300785, 356.96561035156253, 208.95029571533203, 219.07039550781252], [15, 347.70471008300785, 356.96561035156253, 236.3340951538086, 246.45419494628908], [15, 347.70471008300785, 356.96561035156253, 275.6238943481445, 285.74399414062503], [15, 347.70471008300785, 356.96561035156253, 314.31839355468753, 324.438493347168], [15, 347.70471008300785, 356.96561035156253, 342.29749298095703, 352.4175927734375], [15, 347.70471008300785, 356.96561035156253, 369.6812924194336, 379.8013922119141], [15, 347.70471008300785, 384.74831115722657, 397.06509185791015, 407.18519165039066], [15, 347.70471008300785, 384.74831115722657, 435.75959106445316, 445.8796908569336], [15, 347.70471008300785, 407.47961181640625, 475.04939025878906, 485.1694900512696], [15, 347.70471008300785, 375.4874108886719, 503.0284896850586, 513.1485894775391]]
2026-08-10 14:55:53,352 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=26, matched=26, pages=1, time=22.3s
2026-08-10 14:55:53,352 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 14:55:53,353 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 14:55:53,353 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[15]
2026-08-10 14:55:53,353 INFO     29 [qwen-vl-table] positions ： [[15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 14:55:53,511 INFO     29 [qwen-vl-table] page=15, rect=842x595, img=(2339x1654)
2026-08-10 14:55:53,511 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:55:53,512 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 479, \"bbox_end\": 493, \"encounter_dates\": [\"2026-02-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{l c c}\n报告时间: 2026-02-05\n\\hline\n项目 & 结果 & 参考范围 \\\\\n\\hline\n凝血酶原时间检测. & 13.3 & 9.8-14.3/s \\\\\n活动度. & 86.4 & 70.0-150.0/\\% \\\\\n国际标准化比值. & 1.2 & 0.5-1.5 \\\\\n活化部分凝血活酶时间检测. & 30.0 & 20.0-36.9/S \\\\\n纤维蛋白原检测. & 9.1 $\\uparrow$ & 2.0-4.0/g/L \\\\\n凝血酶时间检测. & 16.8 & 14.4-23.4/s \\\\\nD-D二聚体检测. & 0.6 & 0.0-0.6/ug/ml \\\\\n纤维蛋白（原）降解产物检测. & 4.5 & 0.0-5.0/ug/ml \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 14:55:53,514 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:55:53.513+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 64, "failed": 0, "current": {"7630dbd094ca11f1bd9827cf206dfa2d": {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:55:58,850 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:55:58,850 INFO     29 [qwen-vl-table] page=15 LLM output (len=1393):
{
  "report_date": "2026-02-05",
  "items": [
    {
      "name": "凝血酶原时间检测",
      "item_code": null,
      "value": "13.3",
      "unit": "s",
      "reference_range": "9.8-14.3",
      "abnormal": false
    },
    {
      "name": "活动度",
      "item_code": null,
      "value": "86.4",
      "unit": "%",
      "reference_range": "70.0-150.0",
      "abnormal": false
    },
    {
      "name": "国际标准化比值",
      "item_code": null,
      "value": "1.2",
      "unit": null,
      "reference_range": "0.5-1.5",
      "abnormal": false
    },
    {
      "name": "活化部分凝血活酶时间检测",
      "item_code": null,
      "value": "30.0",
      "unit": "s",
      "reference_range": "20.0-36.9",
      "abnormal": false
    },
    {
      "name": "纤维蛋白原检测",
      "item_code": null,
      "value": "9.1",
      "unit": "g/L",
      "reference_range": "2.0-4.0",
      "abnormal": true
    },
    {
      "name": "凝血酶时间检测",
      "item_code": null,
      "value": "16.8",
      "unit": "s",
      "reference_range": "14.4-23.4",
      "abnormal": false
    },
    {
      "name": "D-D二聚体检测",
      "item_code": null,
      "value": "0.6",
      "unit": "ug/ml",
      "reference_range": "0.0-0.6",
      "abnormal": false
    },
    {
      "name": "纤维蛋白（原）降解产物检测",
      "item_code": null,
      "value": "4.5",
      "unit": "ug/ml",
      "reference_range": "0.0-5.0",
      "abnormal": false
    }
  ]
}
2026-08-10 14:55:58,851 INFO     29 [qwen-vl-table] coord grouping: {15: 8}
2026-08-10 14:55:58,852 INFO     29 [qwen-vl-table] coord API call start, page=15, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=575754, prompt_len=579
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
凝血酶原时间检测、活动度、国际标准化比值、活化部分凝血活酶时间检测、纤维蛋白原检测、凝血酶时间检测、D-D二聚体检测、纤维蛋白（原）降解产物检测

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
2026-08-10 14:56:03,550 INFO     29 [qwen-vl-table] coord API raw response (len=419):
[
	{"text": "凝血酶原时间检测", "bbox": [91, 423, 163, 439]},
	{"text": "活动度", "bbox": [91, 487, 124, 502]},
	{"text": "国际标准化比值", "bbox": [91, 530, 163, 545]},
	{"text": "活化部分凝血活酶时间检测", "bbox": [91, 574, 172, 589]},
	{"text": "纤维蛋白原检测", "bbox": [91, 637, 163, 653]},
	{"text": "凝血酶时间检测", "bbox": [91, 681, 163, 697]},
	{"text": "D-D二聚体检测", "bbox": [91, 725, 163, 740]},
	{"text": "纤维蛋白（原）降解产物检测", "bbox": [91, 769, 172, 784]}
]
2026-08-10 14:56:03,550 INFO     29 [qwen-vl-table] coord API: raw_items=8, valid_items=8, elapsed=4.7s
2026-08-10 14:56:03,550 INFO     29 [qwen-vl-table] coord item[0]: text=凝血酶原时间检测, bbox=[91, 423, 163, 439]
2026-08-10 14:56:03,550 INFO     29 [qwen-vl-table] coord item[1]: text=活动度, bbox=[91, 487, 124, 502]
2026-08-10 14:56:03,550 INFO     29 [qwen-vl-table] coord item[2]: text=国际标准化比值, bbox=[91, 530, 163, 545]
2026-08-10 14:56:03,550 INFO     29 [qwen-vl-table] coord item[3]: text=活化部分凝血活酶时间检测, bbox=[91, 574, 172, 589]
2026-08-10 14:56:03,550 INFO     29 [qwen-vl-table] coord item[4]: text=纤维蛋白原检测, bbox=[91, 637, 163, 653]
2026-08-10 14:56:03,550 INFO     29 [qwen-vl-table] coord item[5]: text=凝血酶时间检测, bbox=[91, 681, 163, 697]
2026-08-10 14:56:03,550 INFO     29 [qwen-vl-table] coord item[6]: text=D-D二聚体检测, bbox=[91, 725, 163, 740]
2026-08-10 14:56:03,550 INFO     29 [qwen-vl-table] coord item[7]: text=纤维蛋白（原）降解产物检测, bbox=[91, 769, 172, 784]
2026-08-10 14:56:03,550 INFO     29 [qwen-vl-table] page=15 coord: matched 8/8, time=4.7s
2026-08-10 14:56:03,550 INFO     29 [qwen-vl-table] new_positions (8):
[[16, 76.61290222167969, 137.2297039794922, 251.81189483642578, 261.3366946411133], [16, 76.61290222167969, 104.39560302734375, 289.9110940551758, 298.8405938720703], [16, 76.61290222167969, 137.2297039794922, 315.5089935302735, 324.438493347168], [16, 76.61290222167969, 144.80680419921876, 341.7021929931641, 350.6316928100586], [16, 76.61290222167969, 137.2297039794922, 379.2060922241211, 388.7308920288086], [16, 76.61290222167969, 137.2297039794922, 405.3992916870117, 414.92409149169924], [16, 76.61290222167969, 137.2297039794922, 431.59249114990234, 440.5219909667969], [16, 76.61290222167969, 144.80680419921876, 457.78569061279296, 466.71519042968754]]
2026-08-10 14:56:03,550 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=8, matched=8, pages=1, time=10.2s
2026-08-10 14:56:03,551 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 14:56:03,552 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 14:56:03,552 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[15]
2026-08-10 14:56:03,552 INFO     29 [qwen-vl-table] positions ： [[15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 14:56:03,707 INFO     29 [qwen-vl-table] page=15, rect=842x595, img=(2339x1654)
2026-08-10 14:56:03,708 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:03,708 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 494, \"bbox_end\": 513, \"encounter_dates\": [\"2026-02-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{l c c}\n报告时间: 2026-02-05\n\\hline\n项目 & 结果 & 参考范围 \\\\\n\\hline\n糖类抗原125 & 6.46 & 0.00-24.00/U/ml \\\\\n糖类抗原199 & 8.34 & 0.00-30.00/U/ml \\\\\n糖类抗原153 & 11.70 & 0.00-24.00/U/ml \\\\\n糖类抗原724 & 8.43 $\\uparrow$ & 0.00-6.90/U/ml \\\\\n糖类抗原242 & 8.77 & 0.00-20.00/U/ml \\\\\n总前列腺特异性抗原 & 1.12 & 0.00-4.00/ng/ml \\\\\nFPSA/TPSA & 16.96 $\\downarrow$ & 25.00-100.00/\\% \\\\\n神经元特异性烯醇化酶 & 12.00 & 0.00-17.00/ng/ml \\\\\n细胞角蛋白19片段 & 4.07 $\\uparrow$ & 0.00-3.30/ng/ml \\\\\n鳞状细胞癌抗原 & 1.66 & 0.50-3.00/ng/ml \\\\\n甲胎蛋白 & 4.18 & 0.00-7.00/ng/mL \\\\\n癌胚抗原 & 5.27 $\\uparrow$ & 0.00-5.00/ng/mL \\\\\n铁蛋白 & 47.50 & 30.00-400.00/ng/ml \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 14:56:11,371 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:11,372 INFO     29 [qwen-vl-table] page=15 LLM output (len=2315):
{
  "report_date": "2026-02-05",
  "items": [
    {
      "name": "糖类抗原125",
      "item_code": "CA125",
      "value": "6.46",
      "unit": "U/ml",
      "reference_range": "0.00-24.00",
      "abnormal": false
    },
    {
      "name": "糖类抗原199",
      "item_code": "CA199",
      "value": "8.34",
      "unit": "U/ml",
      "reference_range": "0.00-30.00",
      "abnormal": false
    },
    {
      "name": "糖类抗原153",
      "item_code": "CA153",
      "value": "11.70",
      "unit": "U/ml",
      "reference_range": "0.00-24.00",
      "abnormal": false
    },
    {
      "name": "糖类抗原724",
      "item_code": "CA724",
      "value": "8.43",
      "unit": "U/ml",
      "reference_range": "0.00-6.90",
      "abnormal": true
    },
    {
      "name": "糖类抗原242",
      "item_code": "CA242",
      "value": "8.77",
      "unit": "U/ml",
      "reference_range": "0.00-20.00",
      "abnormal": false
    },
    {
      "name": "总前列腺特异性抗原",
      "item_code": "TPSA",
      "value": "1.12",
      "unit": "ng/ml",
      "reference_range": "0.00-4.00",
      "abnormal": false
    },
    {
      "name": "FPSA/TPSA",
      "item_code": "FPSA/TPSA",
      "value": "16.96",
      "unit": "%",
      "reference_range": "25.00-100.00",
      "abnormal": true
    },
    {
      "name": "神经元特异性烯醇化酶",
      "item_code": "NSE",
      "value": "12.00",
      "unit": "ng/ml",
      "reference_range": "0.00-17.00",
      "abnormal": false
    },
    {
      "name": "细胞角蛋白19片段",
      "item_code": "CYFRA21-1",
      "value": "4.07",
      "unit": "ng/ml",
      "reference_range": "0.00-3.30",
      "abnormal": true
    },
    {
      "name": "鳞状细胞癌抗原",
      "item_code": "SCC",
      "value": "1.66",
      "unit": "ng/ml",
      "reference_range": "0.50-3.00",
      "abnormal": false
    },
    {
      "name": "甲胎蛋白",
      "item_code": "AFP",
      "value": "4.18",
      "unit": "ng/mL",
      "reference_range": "0.00-7.00",
      "abnormal": false
    },
    {
      "name": "癌胚抗原",
      "item_code": "CEA",
      "value": "5.27",
      "unit": "ng/mL",
      "reference_range": "0.00-5.00",
      "abnormal": true
    },
    {
      "name": "铁蛋白",
      "item_code": "Ferritin",
      "value": "47.50",
      "unit": "ng/ml",
      "reference_range": "30.00-400.00",
      "abnormal": false
    }
  ]
}
2026-08-10 14:56:11,372 INFO     29 [qwen-vl-table] coord grouping: {15: 13}
2026-08-10 14:56:11,374 INFO     29 [qwen-vl-table] coord API call start, page=15, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=575754, prompt_len=609
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
糖类抗原125、糖类抗原199、糖类抗原153、糖类抗原724、糖类抗原242、总前列腺特异性抗原、FPSA/TPSA、神经元特异性烯醇化酶、细胞角蛋白19片段、鳞状细胞癌抗原、甲胎蛋白、癌胚抗原、铁蛋白

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
2026-08-10 14:56:14,953 INFO     29 [qwen-vl-table] coord API raw response (len=677):
[
	{"text": "糖类抗原125", "bbox": [373, 305, 431, 323]},
	{"text": "糖类抗原199", "bbox": [373, 348, 431, 366]},
	{"text": "糖类抗原153", "bbox": [373, 391, 431, 409]},
	{"text": "糖类抗原724", "bbox": [373, 434, 431, 452]},
	{"text": "糖类抗原242", "bbox": [373, 477, 431, 495]},
	{"text": "总前列腺特异性抗原", "bbox": [373, 520, 455, 556]},
	{"text": "FPSA/TPSA", "bbox": [373, 582, 428, 600]},
	{"text": "神经元特异性烯醇化酶", "bbox": [373, 625, 455, 662]},
	{"text": "细胞角蛋白19片段", "bbox": [373, 687, 455, 705]},
	{"text": "鳞状细胞癌抗原", "bbox": [373, 730, 445, 748]},
	{"text": "甲胎蛋白", "bbox": [373, 773, 415, 791]},
	{"text": "癌胚抗原", "bbox": [373, 817, 415, 835]},
	{"text": "铁蛋白", "bbox": [373, 860, 405, 878]}
]
2026-08-10 14:56:14,953 INFO     29 [qwen-vl-table] coord API: raw_items=13, valid_items=13, elapsed=3.6s
2026-08-10 14:56:14,954 INFO     29 [qwen-vl-table] coord item[0]: text=糖类抗原125, bbox=[373, 305, 431, 323]
2026-08-10 14:56:14,954 INFO     29 [qwen-vl-table] coord item[1]: text=糖类抗原199, bbox=[373, 348, 431, 366]
2026-08-10 14:56:14,954 INFO     29 [qwen-vl-table] coord item[2]: text=糖类抗原153, bbox=[373, 391, 431, 409]
2026-08-10 14:56:14,954 INFO     29 [qwen-vl-table] coord item[3]: text=糖类抗原724, bbox=[373, 434, 431, 452]
2026-08-10 14:56:14,954 INFO     29 [qwen-vl-table] coord item[4]: text=糖类抗原242, bbox=[373, 477, 431, 495]
2026-08-10 14:56:14,954 INFO     29 [qwen-vl-table] coord item[5]: text=总前列腺特异性抗原, bbox=[373, 520, 455, 556]
2026-08-10 14:56:14,954 INFO     29 [qwen-vl-table] coord item[6]: text=FPSA/TPSA, bbox=[373, 582, 428, 600]
2026-08-10 14:56:14,954 INFO     29 [qwen-vl-table] coord item[7]: text=神经元特异性烯醇化酶, bbox=[373, 625, 455, 662]
2026-08-10 14:56:14,954 INFO     29 [qwen-vl-table] coord item[8]: text=细胞角蛋白19片段, bbox=[373, 687, 455, 705]
2026-08-10 14:56:14,954 INFO     29 [qwen-vl-table] coord item[9]: text=鳞状细胞癌抗原, bbox=[373, 730, 445, 748]
2026-08-10 14:56:14,954 INFO     29 [qwen-vl-table] coord item[10]: text=甲胎蛋白, bbox=[373, 773, 415, 791]
2026-08-10 14:56:14,955 INFO     29 [qwen-vl-table] coord item[11]: text=癌胚抗原, bbox=[373, 817, 415, 835]
2026-08-10 14:56:14,955 INFO     29 [qwen-vl-table] coord item[12]: text=铁蛋白, bbox=[373, 860, 405, 878]
2026-08-10 14:56:14,955 INFO     29 [qwen-vl-table] page=15 coord: matched 13/13, time=3.6s
2026-08-10 14:56:14,955 INFO     29 [qwen-vl-table] new_positions (13):
[[16, 314.0287091064453, 362.858910522461, 181.56649627685547, 192.2818960571289], [16, 314.0287091064453, 362.858910522461, 207.16439575195312, 217.87979553222658], [16, 314.0287091064453, 362.858910522461, 232.7622952270508, 243.47769500732423], [16, 314.0287091064453, 362.858910522461, 258.3601947021485, 269.0755944824219], [16, 314.0287091064453, 362.858910522461, 283.9580941772461, 294.67349395751955], [16, 314.0287091064453, 383.06451110839845, 309.5559936523438, 330.98679321289063], [16, 314.0287091064453, 360.33321044921877, 346.46459289550785, 357.17999267578125], [16, 314.0287091064453, 383.06451110839845, 372.06249237060547, 394.0885919189453], [16, 314.0287091064453, 383.06451110839845, 408.97109161376954, 419.686491394043], [16, 314.0287091064453, 374.6455108642578, 434.5689910888672, 445.2843908691406], [16, 314.0287091064453, 349.388510131836, 460.16689056396484, 470.8822903442383], [16, 314.0287091064453, 349.388510131836, 486.3600900268555, 497.0754898071289], [16, 314.0287091064453, 340.9695098876953, 511.95798950195314, 522.6733892822266]]
2026-08-10 14:56:14,956 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=13, matched=13, pages=1, time=11.4s
2026-08-10 14:56:14,957 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 14:56:14,959 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 14:56:14,959 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[15]
2026-08-10 14:56:14,959 INFO     29 [qwen-vl-table] positions ： [[15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 14:56:15,131 INFO     29 [qwen-vl-table] page=15, rect=842x595, img=(2339x1654)
2026-08-10 14:56:15,132 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:15,132 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 514, \"bbox_end\": 522, \"encounter_dates\": [\"2026-02-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{l c c}\n报告时间: 2026-02-05\n\\hline\n项目 & 结果 & 参考范围 \\\\\n\\hline\n肌红蛋白 & 28.530 & 28.000-72.000/ng/ml \\\\\n高敏肌钙蛋白T & 0.012 & 0.000-0.014/ng/ml \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 14:56:16,852 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:16,852 INFO     29 [qwen-vl-table] page=15 LLM output (len=398):
{
  "report_date": "2026-02-05",
  "items": [
    {
      "name": "肌红蛋白",
      "item_code": null,
      "value": "28.530",
      "unit": "ng/ml",
      "reference_range": "28.000-72.000",
      "abnormal": false
    },
    {
      "name": "高敏肌钙蛋白T",
      "item_code": null,
      "value": "0.012",
      "unit": "ng/ml",
      "reference_range": "0.000-0.014",
      "abnormal": false
    }
  ]
}
2026-08-10 14:56:16,853 INFO     29 [qwen-vl-table] coord grouping: {15: 2}
2026-08-10 14:56:16,854 INFO     29 [qwen-vl-table] coord API call start, page=15, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=575754, prompt_len=519
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
肌红蛋白、高敏肌钙蛋白T

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
2026-08-10 14:56:17,761 INFO     29 [qwen-vl-table] coord API raw response (len=115):
```json
[
	{"text": "肌红蛋白", "bbox": [689, 495, 727, 510]},
	{"text": "高敏肌钙蛋白T", "bbox": [689, 555, 753, 570]}
]
```
2026-08-10 14:56:17,761 INFO     29 [qwen-vl-table] coord API: raw_items=2, valid_items=2, elapsed=0.9s
2026-08-10 14:56:17,761 INFO     29 [qwen-vl-table] coord item[0]: text=肌红蛋白, bbox=[689, 495, 727, 510]
2026-08-10 14:56:17,761 INFO     29 [qwen-vl-table] coord item[1]: text=高敏肌钙蛋白T, bbox=[689, 555, 753, 570]
2026-08-10 14:56:17,761 INFO     29 [qwen-vl-table] page=15 coord: matched 2/2, time=0.9s
2026-08-10 14:56:17,761 INFO     29 [qwen-vl-table] new_positions (2):
[[16, 580.0691168212891, 612.0613177490235, 294.67349395751955, 303.6029937744141], [16, 580.0691168212891, 633.9507183837891, 330.3914932250977, 339.3209930419922]]
2026-08-10 14:56:17,761 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=2, matched=2, pages=1, time=2.8s
2026-08-10 14:56:17,762 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 14:56:17,763 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 14:56:17,763 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]
2026-08-10 14:56:17,764 INFO     29 [qwen-vl-table] positions ： [[17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [30, 0.0, 0.0, 0.0, 0.0], [31, 0.0, 0.0, 0.0, 0.0], [31, 0.0, 0.0, 0.0, 0.0], [31, 0.0, 0.0, 0.0, 0.0], [31, 0.0, 0.0, 0.0, 0.0], [31, 0.0, 0.0, 0.0, 0.0], [31, 0.0, 0.0, 0.0, 0.0], [31, 0.0, 0.0, 0.0, 0.0], [31, 0.0, 0.0, 0.0, 0.0], [31, 0.0, 0.0, 0.0, 0.0], [31, 0.0, 0.0, 0.0, 0.0], [31, 0.0, 0.0, 0.0, 0.0], [31, 0.0, 0.0, 0.0, 0.0], [31, 0.0, 0.0, 0.0, 0.0], [31, 0.0, 0.0, 0.0, 0.0], [31, 0.0, 0.0, 0.0, 0.0], [31, 0.0, 0.0, 0.0, 0.0], [31, 0.0, 0.0, 0.0, 0.0], [31, 0.0, 0.0, 0.0, 0.0], [31, 0.0, 0.0, 0.0, 0.0], [31, 0.0, 0.0, 0.0, 0.0], [31, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [32, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [33, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [34, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [35, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [36, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 14:56:17,831 INFO     29 [qwen-vl-table] page=17, rect=595x842, img=(1653x2339)
2026-08-10 14:56:17,898 INFO     29 [qwen-vl-table] page=18, rect=595x842, img=(1653x2339)
2026-08-10 14:56:17,975 INFO     29 [qwen-vl-table] page=19, rect=595x842, img=(1653x2339)
2026-08-10 14:56:18,032 INFO     29 [qwen-vl-table] page=20, rect=595x842, img=(1653x2339)
2026-08-10 14:56:18,097 INFO     29 [qwen-vl-table] page=21, rect=595x842, img=(1653x2339)
2026-08-10 14:56:18,161 INFO     29 [qwen-vl-table] page=22, rect=595x842, img=(1653x2339)
2026-08-10 14:56:18,231 INFO     29 [qwen-vl-table] page=23, rect=595x842, img=(1653x2339)
2026-08-10 14:56:18,294 INFO     29 [qwen-vl-table] page=24, rect=595x842, img=(1653x2339)
2026-08-10 14:56:18,385 INFO     29 [qwen-vl-table] page=25, rect=595x842, img=(1653x2339)
2026-08-10 14:56:18,439 INFO     29 [qwen-vl-table] page=26, rect=595x842, img=(1653x2339)
2026-08-10 14:56:18,524 INFO     29 [qwen-vl-table] page=27, rect=595x842, img=(1653x2339)
2026-08-10 14:56:18,619 INFO     29 [qwen-vl-table] page=28, rect=595x842, img=(1653x2339)
2026-08-10 14:56:18,721 INFO     29 [qwen-vl-table] page=29, rect=595x842, img=(1653x2339)
2026-08-10 14:56:18,810 INFO     29 [qwen-vl-table] page=30, rect=595x842, img=(1653x2339)
2026-08-10 14:56:18,871 INFO     29 [qwen-vl-table] page=31, rect=595x842, img=(1653x2339)
2026-08-10 14:56:18,941 INFO     29 [qwen-vl-table] page=32, rect=595x842, img=(1653x2339)
2026-08-10 14:56:19,017 INFO     29 [qwen-vl-table] page=33, rect=595x842, img=(1653x2339)
2026-08-10 14:56:19,095 INFO     29 [qwen-vl-table] page=34, rect=595x842, img=(1653x2339)
2026-08-10 14:56:19,166 INFO     29 [qwen-vl-table] page=35, rect=595x842, img=(1653x2339)
2026-08-10 14:56:19,238 INFO     29 [qwen-vl-table] page=36, rect=595x842, img=(1653x2339)
2026-08-10 14:56:19,320 INFO     29 [qwen-vl-table] page=37, rect=595x842, img=(1653x2339)
2026-08-10 14:56:19,385 INFO     29 [qwen-vl-table] page=38, rect=595x842, img=(1653x2339)
2026-08-10 14:56:19,468 INFO     29 [qwen-vl-table] page=39, rect=595x842, img=(1653x2339)
2026-08-10 14:56:19,540 INFO     29 [qwen-vl-table] page=40, rect=595x842, img=(1653x2339)
2026-08-10 14:56:19,615 INFO     29 [qwen-vl-table] page=41, rect=595x842, img=(1653x2339)
2026-08-10 14:56:19,679 INFO     29 [qwen-vl-table] page=42, rect=595x842, img=(1653x2339)
2026-08-10 14:56:19,749 INFO     29 [qwen-vl-table] page=43, rect=595x842, img=(1653x2339)
2026-08-10 14:56:19,754 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:19,754 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "基因检测报告单\n姓名\n年龄：62\n性别：男\n样本编号\n样本类型：白片\n送检医生：\n接收日期：2025-04-30\n报告日期：2025-05-05\n临床诊断：肠癌肺转移\n检测技术：NGS\n备注：\n项目名称：\n本次检测概览\n检测内容\n本产品包含40个与结直肠癌发生、发展相关的基因，其中涵盖NCCN指南中的KRAS、BRAF、NRAS、ERBB2等重要基\n因，以及MLH1、MSH2、MSH6、PMS2、POLE等与PD-1/PD-L1免疫治疗相关基因，同时，还涵盖与化疗药物毒副作用、疗效相关基因。在采用二代测序技术对这些基因进行深度测序后，根据检出的基因状态，为患者的个体化临床治疗方案\n制定提供可靠的参考依据。\n小结\n体细胞突变\n2\n拷贝数变异\n1\n融合变异\n未检出\n微卫星不稳定状态（MSI）\n微卫星稳定（MSS）\n错配修复基因胚系突变（MMR）\n未检出\n化疗药物\n详情见化疗位点及相关药物反应结果\n用药相关基因变异及其临床意义\n变异\n提示敏感\n提示耐药\n潜在获益的药物\n变异分类\nKRAS\n2 号外显子\n错义突变\nc.34G>A\np.G12S\n丰度 = 41.62%\nPanitumumab (A 级)\nTucatinib + 曲妥珠单抗 (A 级)\n西妥昔单抗 (A 级)\nCobimetinib (D 级 实体瘤; C 级 朗格汉斯细胞组织细胞增多症、埃尔德海姆-\n切斯特病、罗-道病)\n曲美替尼 (D 级 实体瘤; C 级 朗格汉斯细胞组织细胞增多症、埃尔德海姆-切斯特病、罗-道病)\nBinimetinib (D 级 实体瘤)\nRMC-6236 (D 级 实体瘤)\nI 类\nMYC\n拷贝数扩增\nCN=3.42\nBenzosertib (C 级 实体瘤)\nBMS-986158 (D 级 实体瘤)\nII 类\n注:\n1. 药物分级依据参考《二代测序临床报告解读指引》以及 2017 年 AMP/ASCO/CAP 联合制定的体细胞变异解读指南:\nA 级, 美国食品药品监督管理局 (Food and Drug Administration, FDA) , 以及中国国家药品监督管理局 (National Medical Products\nAdministration, NMPA) 批准或 NCCN、CSCO、ASCO、ESMO 等专业临床指南推荐;\nB 级, 经具有足够统计学效能的临床研究证实、获得该领域专家共识;\nC 级, 其他癌种中的 A 级证据 (跨适应证用药) 、或已作为临床试验的入组标准;\nD 级, 临床病例报道或临床前证据支持。",
    "role": "user"
  }
]
2026-08-10 14:56:23,813 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:23,813 INFO     29 [qwen-vl-table] page=17 LLM output (len=1216):
{
  "report_date": "2025-05-05",
  "items": [
    {
      "name": "体细胞突变",
      "item_code": null,
      "value": "2",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "拷贝数变异",
      "item_code": null,
      "value": "1",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "融合变异",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "微卫星不稳定状态（MSI）",
      "item_code": "MSI",
      "value": "微卫星稳定（MSS）",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "错配修复基因胚系突变（MMR）",
      "item_code": "MMR",
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "KRAS 2号外显子",
      "item_code": "KRAS",
      "value": "错义突变 c.34G>A p.G12S 丰度=41.62%",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "MYC",
      "item_code": "MYC",
      "value": "拷贝数扩增 CN=3.42",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    }
  ]
}
2026-08-10 14:56:23,813 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:23,814 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "2. 提示敏感的药物来源于 NMPA/FDA 批准或肿瘤临床指南, 以及临床专家达成共识的较大规模临床研究结果 (A 级, B 级) 。\n3. 提示耐药的药物来源于该肿瘤类型 NMPA/FDA 批准或肿瘤临床指南, 及相关文献或临床试验报道。\n4. 潜在获益的药物来源于该肿瘤类型相关文献或临床试验报道, 以及在其他肿瘤类型中已获批的药物 (C 级, D 级) 。\n5. 报告中相同分级药物间先后顺序与优先推荐无关, 按首字母排序列出。\n6. 按照变异的治疗、预后和诊断等临床意义, 体细胞变异分类为: I 类 (A 级、B 级证据) , II 类 (C 级、D 级证据) , III 类 (临床意义未明的变异) , IV 类 (可能无害或无害的变异, 本报告中不予列出) ; 胚系变异分类为: 致病性, 可能致病性, 意义未明, 可能良性 (本报告中不予列出) , 良性 (本报告中不予列出) 。\nNCCN 指南推荐相关基因变异结果\n基因\n变异类型\n变异结果\n丰度\nKRAS\n错义突变\nc.34G>A(p.G12S)\n41.62%\nBRAF\n未检出\nNRAS\n未检出\n注:\n1. KRAS、NRAS 和 BRAF 基因的突变与结直肠癌等癌症患者对 EGFR 单抗类药物(西妥昔单抗或帕尼单抗)的耐药有关，但这些基因野生型的患者能从此类药物的治疗中获益。欧洲药监局和美国 FDA 也明确规定了在使用靶向药物西妥昔单抗或帕尼单抗治疗转移性大肠癌前必须检测 KRAS 基因。(NCCN Guideline: Colon (Rectal) Cancer v.1.2023; FDA Druglabel:panitumumab;FDA Druglabel:cetuximab)。\n2. KRAS 基因检测覆盖但不仅限于 G12, G13, Q61, A59, K117, A146 等变异。\n3. BRAF 基因检测覆盖但不仅限于 V600E, G469A/V, G442S, G464V, Y472C, N581S, D594G, L597V/S, K601E 等变异。\n4. NRAS 基因检测覆盖但不仅限于 G12, G13, Q61, A59, A146 等变异。\n其他非用药相关变异\n基因\n外显子\n变异类型\n变异结果\n丰度/基因型\n变异分类\nAPC\n16\n移码突变\nc.4257_4263del(p.S1419fs)\n40.08%\nⅢ类\n注:\n1. 突变类型：错义突变（missense）、同义突变（synonymous mutation）、非移码插入突变（insertion）、非移码缺失突变（deletion）、移码突变（frameshift）、剪切突变（splice_variant）、起始密码子丢失（start_lost）、无义突变（nonsense）等。\n2. 体细胞突变又称获得性突变，是在生长发育过程中或者环境因素影响下后天获得的突变，通常身上只有部分细胞带有体细胞突变，如癌症组织会出现致病性的突变。此外同义突变因氨基酸不发生改变故未列出。\n3. 胚系变异又称生殖细胞变异，是来源于精子或卵子这些生殖细胞的变异，因此通常身上所有细胞都带有这种变异；这其中绝大多数胚系变异并不致病，构成了人与人之间的遗传多态性，只有少数变异会致病，特别是一些遗传类的疾病。如移码突变、无义突变等，该类可能导致疾病产生的变异结果会在本部分内容中列出。\n微卫星不稳定性（MSI）检测\n本次检测结果\n微卫星稳定（MSS）\n注:\n1. 微卫星不稳定（MSI-H）的患者，可能对 PD-1/PD-L1 等相关免疫疗法敏感。\n2. FDA 已经批准 PD-1 抗体 Keytruda 用于 MSI-H 或者 dMMR 类型的多种实体瘤。\n3. PD-1/PD-L1 抑制剂药物主要有： 可瑞达（Pembrolizumab），欧狄沃（Nivolumab），泰圣奇（Atezolizumab），达伯舒（Sintilimab），百泽安（Tislelizumab），艾瑞卡（Camrelizumab），Imfinzi（Durvalumab），Bavencio（Avelumab）等。\n4. NCCN 指南建议对于 MSI-H 或 MMR 任一蛋白缺失患者，推荐进一步的 MMR 基因胚系突变检测辅助 Lynch 综合征的诊断。\n错配修复基因胚系突变（MMR）\n基因\n变异类型\n变异结果\n基因型\n致病性\nEPCAM\n未检出\nMLH1\n未检出\nMSH2\n未检出\nMSH6\n未检出\nPMS2\n未检出\n注:",
    "role": "user"
  }
]
2026-08-10 14:56:25,150 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:56:25.149+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 64, "failed": 0, "current": {"7630dbd094ca11f1bd9827cf206dfa2d": {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:56:29,123 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:29,123 INFO     29 [qwen-vl-table] page=18 LLM output (len=1668):
{
  "report_date": "2025-05-05",
  "items": [
    {
      "name": "KRAS",
      "item_code": null,
      "value": "c.34G>A(p.G12S)",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "BRAF",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "NRAS",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "APC",
      "item_code": null,
      "value": "c.4257_4263del(p.S1419fs)",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "微卫星不稳定性（MSI）",
      "item_code": "MSI",
      "value": "微卫星稳定（MSS）",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "EPCAM",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "MLH1",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "MSH2",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "MSH6",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "PMS2",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-10 14:56:29,124 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:29,124 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "奕检医学\nYIJIANMED LABORATORY\nYJ50430012T\n1. 错配修复 (MMR) 基因包含 EPCAM、MLH1、MSH2、MSH6、PMS2 等基因，这些基因突变会导致错配修复基因功能丧失 (dMMR)，如果\n没有发生基因突变，则为正常 (pMMR)。dMMR 导致 MSI-H，但是 MSI-H 的人不一定 dMMR。\n2. 检测 MMR 的必要性如下：(1)辅助临床评判 MSI-H 发生的原因；(2) MMR 基因的胚系突变还与 Lynch 综合征相关，如需进一步判断是否为\nLynch 综合征还需要结合病史、家族史等具体情况补充其他基因检测进行辅助诊断；(3)预测肿瘤患者能否从抗 PD-1 中获益。\n3. 胚系变异通常会按 ACMG (American College of Medical Genetics and Genomics) 相关指南，分为 “致病性”、“可能致病性”、“意义未\n明”、“可能良性”、“良性”五类。本部分结果只列出“致病性”、“可能致病性”突变。\n基因拷贝数结果\n基因\n染色体位置\n拷贝数变异\nMYC\nchr8\nCN=3.42\nBRAF\nchr7\n未检出\nEGFR\nchr7\n未检出\nERBB2\nchr17\n未检出\nFGFR1\nchr8\n未检出\nFGFR2\nchr10\n未检出\nFGFR3\nchr4\n未检出\nKRAS\nchr12\n未检出\nMDM2\nchr12\n未检出\nNTRK1\nchr1\n未检出\nPIK3CA\nchr3\n未检出\n注：\n1. 本报告包含以上重要基因的拷贝数变异，但不仅限于以上基因。\n2. 正常细胞的 DNA 可能稀释变异细胞中的 DNA 拷贝数，所以报告中的拷贝数为样本中细胞的平均拷贝数。\n3. 常染色体中基因的正常拷贝数为 2，拷贝数变异为该基因的拷贝数发生改变，CN>2 的拷贝数变异为基因发生扩增，CN<2 的拷贝数变异为基因\n发生缺失。\n融合基因结果\n检测基因\n检测结果\n丰度\nRET\n未检出\nNTRK3\n未检出\nNTRK2\n未检出\nNTRK1\n未检出\n注：本报告包含以上重要基因的融合变异，但不仅限于以上基因。\n多靶点药物治疗方案",
    "role": "user"
  }
]
2026-08-10 14:56:36,702 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:36,703 INFO     29 [qwen-vl-table] page=19 LLM output (len=2416):
{
  "report_date": "2025-05-05",
  "items": [
    {
      "name": "MYC",
      "item_code": null,
      "value": "CN=3.42",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "BRAF",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "EGFR",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "ERBB2",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "FGFR1",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "FGFR2",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "FGFR3",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "KRAS",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "MDM2",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "NTRK1",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "PIK3CA",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "RET",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "NTRK3",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "NTRK2",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "NTRK1",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-10 14:56:36,703 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:36,704 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "癌种\nNMPA/FDA/\n指南推荐药物\n治疗方案选择\n药物机制\n使用范围\n结直肠癌\n5-FU + 亚叶酸钙\n+ 贝伐珠单抗\n初始治疗\n化疗+抗血管生成\n晚期/转移性结直肠癌\nFOLFIRI/伊立替康\n+ 贝伐珠单抗（首选）\n初始/后续治疗\n化疗+抗血管生成\n1、无法切除的异时性转移结直肠癌，过去12个月用了FOLFOX/CAPEOX辅助治疗；2、先前接受奥沙利铂治疗而未接受过伊立替康治疗的晚期/转移性结直肠癌；3、先前接受氟尿嘧啶治疗而未接受过伊立替康/奥沙利铂治疗的晚期/转移性结直肠癌\nFOLFOX/CAPEO\nX + 贝伐珠单抗\n后续治疗\n化疗+抗血管生成\n1、先前接受伊立替康治疗而未接受过奥沙利铂治疗的晚期/转移性结直肠癌；2、先前接受氟尿嘧啶治疗而未接受过伊立替康/奥沙利铂治疗的晚期/转移性结直肠癌\nFOLFOX/CAPEO\nX/FOLFIRI/FOLFOXIRI + 贝伐珠单抗\n初始治疗\n化疗+抗血管生成\n晚期/转移性结直肠癌\n伊立替康 + 奥沙利铂 + 贝伐珠单抗\n后续治疗\n化疗+抗血管生成\n先前接受氟尿嘧啶治疗而未接受过伊立替康/奥沙利铂治疗的晚期/转移性结直肠癌\n卡培他滨 + 贝伐珠单抗\n初始治疗\n化疗+抗血管生成\n晚期/转移性结直肠癌\n呋喹替尼\n后续治疗\n抗血管生成\n适用于既往接受过氟尿嘧啶类、奥沙利铂和伊立替康为基础的化疗，以及既往接受过或不适合接受抗 VEGF 治疗、抗EGFR 治疗的 RAS 野生型转移性结直肠癌患者。\n瑞戈非尼\n后续治疗\n抗血管生成\n所有可用方案治疗后进展的晚期/转移性结直肠癌\n(FOLFIRI/伊立替康) + ziv-阿柏西普\n初始/后续治疗\n化疗+抗血管生成\n1、无法切除的异时性转移结直肠癌，过去12个月用了FOLFOX/CAPEOX辅助治疗；2、先前接受奥沙利铂治疗而未接受过伊立替康治疗的晚期/转移性结直肠癌；3、先前接受氟尿嘧啶治疗而未接受过伊立替康/奥沙利铂治疗的晚期/转移性结直肠癌\n(FOLFIRI/伊立替康\n初始/后续治疗\n化疗+抗血管生成\n1、无法切除的异时性转移结直肠癌，过\n康）+ 雷莫西尤单\n抗\n去12个月用了FOLFOX/CAPEOX辅助\n治疗；2、先前接受奥沙利铂治疗而未接\n受过伊立替康治疗的晚期/转移性结直\n肠癌；3、先前接受氟尿嘧啶治疗而未接\n受过伊立替康/奥沙利铂治疗的晚期/转\n移性结直肠癌\n注：\n1. 此处内容为 FDA/NMPA 获批，或指南推荐的药物治疗方案。\n2. 该处呈现的治疗方案，旨在为患者的临床治疗提供更多参考信息，但并非该患者的个体化治疗方案。\n3. 治疗方案的选择，请结合患者临床情况参照“使用范围”信息，并遵从临床医师的指导。\n化疗药物相关基因检测结果\n化疗药物",
    "role": "user"
  }
]
2026-08-10 14:56:37,516 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:37,516 INFO     29 [qwen-vl-table] page=20 LLM output (len=40):
{
  "report_date": null,
  "items": []
}
2026-08-10 14:56:37,516 WARNING  29 [qwen-vl-table] page=20 no items extracted
2026-08-10 14:56:37,516 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:37,517 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "检测基因\n检测位点\n检测结果\n用药提示\n证据等级\n紫杉醇类\nTP53\nrs1042522\nCG\n药物疗效较好，毒副作用风险较高\n3\n伊立替康\nUGT1A1\nrs8175347\n(TA)6/(TA)7\n毒副作用风险较高\n1A\nrs4148323\nAG\n毒副作用风险较高\n1B\n5-氟尿嘧啶\nDPYD\nrs55886062\nAA\n毒副作用风险低\n1A\nrs67376798\nTT\n毒副作用风险低\n1A\nrs3918290\nCC\n毒副作用风险低\n1A\n卡培他滨\nDPYD\nrs67376798\nTT\n毒副作用风险低\n1A\nrs3918290\nCC\n毒副作用风险低\n1A\n甲氨蝶呤\nMTHFR\nrs1801133\nAG\n毒副作用风险较高\n2A\n注：\n1. 所有检测基因均采用 NCBI-Gene 里的官方命名。\n2. 检测位点均以 rs 号为准：NCBI 里对所有提交的 SNP 进行分类考证后，均会注册一个 rs 号，也称作参考 SNP。\n3. 证据等级的划分：依据 PharmGKB 网站 http://www.pharmgkb.org/page/clinAnnLevels\nLevel 1A：注释基于被医学会认可的指南或经某些重大卫生系统的认可；\nLevel 1B：注释基于多项有统计显著的研究；\nLevel 2A：注释基于多项重复研究，故药效关系很有可能是有意义的；\nLevel 2B：注释基于多项重复研究，但某些研究可能无统计显著性或样本数量少；\nLevel 3：注释仅基于 1 项有显著差异的研究（未重复）或多项研究但缺乏明显药效关联性。\n4. 影响化疗药物效果的因素较多，如患者临床表现、药物相互作用、给药顺序、剂量差异等，以上检测结果可为化疗药物治疗方案制定提供参考，\n具体用药还请遵循临床指南与医嘱。\n\\begin{tabular}{ccc}\n报告时间: 2025-05-05\n\\hline",
    "role": "user"
  }
]
2026-08-10 14:56:42,815 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:42,815 INFO     29 [qwen-vl-table] page=21 LLM output (len=1582):
{
  "report_date": "2025-05-05",
  "items": [
    {
      "name": "紫杉醇类",
      "item_code": "TP53 rs1042522",
      "value": "CG",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "伊立替康",
      "item_code": "UGT1A1 rs8175347",
      "value": "(TA)6/(TA)7",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "伊立替康",
      "item_code": "UGT1A1 rs4148323",
      "value": "AG",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "5-氟尿嘧啶",
      "item_code": "DPYD rs55886062",
      "value": "AA",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "5-氟尿嘧啶",
      "item_code": "DPYD rs67376798",
      "value": "TT",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "5-氟尿嘧啶",
      "item_code": "DPYD rs3918290",
      "value": "CC",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "卡培他滨",
      "item_code": "DPYD rs67376798",
      "value": "TT",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "卡培他滨",
      "item_code": "DPYD rs3918290",
      "value": "CC",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "甲氨蝶呤",
      "item_code": "MTHFR rs1801133",
      "value": "AG",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    }
  ]
}
2026-08-10 14:56:42,815 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:42,816 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\textbf{质控项目} & \\textbf{质控结果} & \\textbf{质控标准} \\\\\n\\hline\n样本量 & 合格 & >30 ng \\\\\n\\hline\n预文库 & 合格 & >500 ng \\\\\n\\hline\n靶向捕获 & 合格 & >10 ng \\\\\n\\hline\n测序质量 & 0.953 & >0.8 \\\\\n\\hline\n测序深度 & 795.20 & 组织样本$\\ge$500X; ctDNA$\\ge$5000X \\\\\n\\hline\n\\end{tabular}\n奕检医学\nYIJIANMED LABORATORY\nYJ50430012T\n附录\n基因列表\nAPC\nDPYD\nFGFR3\nMLH1\nNTRK1\nPTEN\nAKT1\nEGFR\nHRAS\nMSH2\nNTRK2\nRET\nARID1A\nEPCAM\nKIT\nMSH6\nNTRK3\nSMAD4\nBRAF\nERBB2\nKRAS\nMTHFR\nPDGFRA\nTP53\nCDH1\nFBXW7\nMAP2K1\nMUTYH\nPIK3CA\nUGT1A1\nCHEK2\nFGFR1\nMDM2\nMYC\nPMS2\nDDR2\nFGFR2\nMDM4\nNRAS\nPOLE\n检测方法与技术局限声明\n1. 本检测中点突变与扩增相关基因覆盖了基因全部编码外显子区域，融合基因主要覆盖了常见断裂位点内含子区域，放化疗位点则为 SNP 位点。但由于基因组重复片段与高 GC 区域，导致探针并不能保证 100%（通常大于 98%）覆盖目标区域，存在一定区域探针难以覆盖导致少量罕见位点无法检出。\n2. 本检测是临床诊断与用药决策的有效补充，并不能代替临床其他检测，具体治疗还需医生根据患者其他检测结果与患者病情进展情况做出方案。\n3. 本检测的基因相关解读，主要依据 FDA/NMPA 批准的靶向药物、CSCO、ASCO、NCCN、ESMO 等相关指南，以及相关临床试验与相关临床案例等文献。随着新靶点药物的批准、指南的更新、临床研究的进展，报告内容和相关解读会随相关内容的更新而变化。\n4. 基因点突变、融合基因、拷贝数变异的检出率与肿瘤细胞的含量密切相关，根据 CSCO 肿瘤诊断指南适合于 NGS 检测的组织标本中肿瘤细胞含量建议应达到 20%以上。如果肿瘤细胞占比较低，存在一定未检出的风险，另外 ctDNA 血液样本作为无法取得组织样本的必要补充，建议采血至少 10ml，保证充足的游离 DNA 用于 NGS 检测，如检测结果为阴性，后续如有组织样本，建议进行再次检测。\n5. 未进行白细胞样本对照实验时，无法确认检出变异是否为胚系变异，报告中将以体细胞变异体现。\n— 8 —",
    "role": "user"
  }
]
2026-08-10 14:56:45,877 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:45,877 INFO     29 [qwen-vl-table] page=22 LLM output (len=869):
{
  "report_date": "2025-05-05",
  "items": [
    {
      "name": "样本量",
      "item_code": null,
      "value": "合格",
      "unit": null,
      "reference_range": ">30 ng",
      "abnormal": false
    },
    {
      "name": "预文库",
      "item_code": null,
      "value": "合格",
      "unit": null,
      "reference_range": ">500 ng",
      "abnormal": false
    },
    {
      "name": "靶向捕获",
      "item_code": null,
      "value": "合格",
      "unit": null,
      "reference_range": ">10 ng",
      "abnormal": false
    },
    {
      "name": "测序质量",
      "item_code": null,
      "value": "0.953",
      "unit": null,
      "reference_range": ">0.8",
      "abnormal": false
    },
    {
      "name": "测序深度",
      "item_code": null,
      "value": "795.20",
      "unit": "X",
      "reference_range": "组织样本≥500X; ctDNA≥5000X",
      "abnormal": false
    }
  ]
}
2026-08-10 14:56:45,878 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:45,878 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n奕检医学\nYIJIANMED LABORATORY\nYJ50430012T\n变异解析\n变异\n变异解读\nKRAS\n2 号外显子\n错义突变\nc.34G>A\np.G12S\n丰度 = 41.62%\nI 类\nKRAS 基因第 2 号外显子第 12 位密码子编码的氨基酸由甘氨酸突变为丝氨酸。此变异在 ClinVar 数据库\n中被记录为致病性变异。在 COSMIC 数据库中有 2075 次检出，其中 Large intestine cancer 有 1437\n例，Lung cancer 有 223 例，Pancreas cancer 有 111 例。\n根据 NMPA/FDA 批准、肿瘤临床指南、相关临床研究结果等，该变异对 Panitumumab (A 级)、Tucatinib\n+ 曲妥珠单抗 (A 级) 、西妥昔单抗 (A 级) 等耐药，潜在获益药物为 Cobimetinib (D 级 实体瘤；C\n级 朗格汉斯细胞组织细胞增多症、埃尔德海姆-切斯特病、罗-道病) 、曲美替尼 (D 级 实体瘤；C 级 朗\n格汉斯细胞组织细胞增多症、埃尔德海姆-切斯特病、罗-道病) 、Binimetinib (D 级 实体瘤) 、RMC-6236\n(D 级 实体瘤) 等。\nKRAS 是小型 GTP 酶 RAS 家族的成员,该家族催化 GTP 水解为 GDP。在生理条件下,这些 RAS 蛋白\n在活性(GTP 结合)和非活性(GDP 结合)状态之间循环,以激活受体酪氨酸激酶 (RTK)下游的 MAPK 和\nPI3K 致癌途径信号传导(PMID:22189424)。RAS 酶的功能受鸟嘌 呤核苷酸交换因子(GEF)如 SOS 的\n调节,这些因子可以使 GDP 与 GTP 交换,也可以通过 GTP 酶活化蛋白如 NF1 调节,从而提高 RAS 水\n解 GTP 的能力。一旦被激活,RAS 可通过激活不 同的细胞内信号传导途径(包括 RAF / MEK / ERK 和\nPI3K/AKT/ mTOR 途径)介导细胞增殖和其他细胞功能的调节。KRAS 中的转化突变常见于胰腺癌,结肠\n癌,子宫内膜癌,卵巢癌和胆管癌;几乎所有这些突变都可导致 KRAS 的组成型活化,从而促进细胞增殖\n(PMID:21993244, 24651010)。 KRAS 突变主要发生在三个主要热点 G12,G13 和 Q61 上,前两个发\n生在 GTP-ase 结构域,后者为干扰 NF1 结合和调节 KRAS 的能力(PMID: 22589270, 21993244,\n24651010)。其他不太明确表征的突变如 A146T // P 和 L19F 也已被表征,而且发现较低频率下也可处\n于活化状态(PMID:20147967, 20432530, 20570890)。种系 KRAS 突变可导致 Noonan 综合征(NS)\n和心脏-皮肤-皮肤(CFC)综合征(PMID:16474405, 16474404, 19467855, 17056636),这些疾 病与过度\n活化的 MAPK 途径,独特的临床特征和癌症易感性相关( PMID:19467855,17704260)。\nAPC\n16 号外显子\n移码突变\nc.4257_4263del\np.S1419fs\n丰度 = 40.08%\nIII 类\nAPC 基因第 16 号外显子发生移码突变。\nAPC 是参与 WNT 信号传导的肿瘤抑制基因(PMID: 8259518、8259519)。APC 的主要肿瘤抑制作用是\n调节细胞内β-catenin 水平 (PMID: 11978510)。APC 是破坏复合物的重要成员，该复合物靶向胞质\nβ-catenin 泛素化和降解(PMID: 10984057)。当 APC 活性丧失时，WNT 通路活性异常增强，往往导致\n增生，最终导致肿瘤进展(PMID: 8259511)。抑制肿瘤形成需要一个 APC 表达的阈值，并且该水平达到\n了很好的平衡(PMID: 11743581)。APC 基因的胚系突变导致家族腺瘤性息肉病(FAP) (PMID: 1651174,\n1651562)， 95%的患者发展为结直肠癌(PMID: 1528264)。此外，APC 的可遗传变异导致许多相关疾\n病的发生，包括 Turcot 综合征、Gardner 综合征和扁平腺瘤综合征(FAS) (PMID: 8593545)。在 50-80%\n的散发性结直肠癌(PMID: 17143297)中观察到 APC 突变，与 FAS 中的突变很相似。APC 的体细胞突变\n作为肿瘤发生启动事件，在包括乳腺癌、胃癌和前列腺癌在内的许多其他人类癌症中也可观察到(PMID:\n27302369，29316426)。大多数 APC 突变是功能丧失型，主要发生在一个β-catenin 结合的重要区域\n(PMID: 10784639、1338904)。WNT 通路抑制剂目前正在临床研究中(PMID: 24981364)。\nMYC\n拷贝数扩增\nCN=3.42\nII 类\nMYC 的拷贝数扩增变异。\n根据 NMPA/FDA 批准、肿瘤临床指南、相关临床研究结果等，该变异潜在获益药物为 Berzosertib (C\n级 实体瘤) 、BMS-986158 (D 级 实体瘤) 等。\nMYC 编码一个转录因子，该转录因子与蛋白质 MAX 异源二聚化以调控数千个基因的转录，调节参与多\n种细胞过程（包括增殖，分化和凋亡）。 MYC 主要通过基因扩增在多种癌症中被激活。 MYC 通过诱\n导增殖，抑制细胞周期停滞，刺激血管形成和增强基因组不稳定性来促进肿瘤发生 (PMID：\n— 9 —",
    "role": "user"
  }
]
2026-08-10 14:56:50,441 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:50,441 INFO     29 [qwen-vl-table] page=23 LLM output (len=582):
{
  "report_date": "2025-05-05",
  "items": [
    {
      "name": "KRAS 2号外显子 c.34G>A p.G12S",
      "item_code": "KRAS",
      "value": "41.62%",
      "unit": "%",
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "APC 16号外显子 c.4257_4263del p.S1419fs",
      "item_code": "APC",
      "value": "40.08%",
      "unit": "%",
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "MYC 拷贝数",
      "item_code": "MYC",
      "value": "3.42",
      "unit": "CN",
      "reference_range": null,
      "abnormal": true
    }
  ]
}
2026-08-10 14:56:50,441 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:50,441 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n奕检医学\nYIJIANMED LABORATORY\nYJ50430012T\n22464321,10378696,16934487,19029958）。 MYC 在癌症中通过多种机制被激活，包括染色体易位\n(通常与血液肿瘤有关，并与组成型过表达有关) 以及基因组扩增和过表达 (PMID: 22446421)。 MYC\n基因发生突变，但频率低于扩增和易位。已知功能性突变位于 T58 残基附近，该残基是 MYC 上的一个\n磷酸化位点，对 MYC 蛋白的泛素化及其降解至关重要 (PMID: 10706881)。 MYC 基因家族由三个\n相关基因组成：（1）c-MYC（在此称为 MYC，由 MYC 基因编码），（2）N-MYC（由 MYCN 基因编\n码）和（3）L-MYC（由基因 MYCL1 编码）(PMID: 16934487)。 MYC 基因位于染色体基因座 8q24\n上，并包含几个不同的结构域，包括一个 N 端转录激活域，一个中央部分和一个 C 端 DNA 结合域，其\n中包含一个基本的螺旋-环-螺旋亮氨酸拉链二级结构域。在这些域中有五个“Myc-boxs”区域，在多个\n物种的 MYC 家族蛋白中高度保守 (PMID: 19029958)。\n—10—\n上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n奕检医学\nYIJIANMED LABORATORY\nYJ50430012T\n部分基因简介\n检测基因\n描述\nAPC\nAPC 编码腺瘤性结肠息肉蛋白,该蛋白是促癌 WNT/β-连环蛋白信号传导通路的负调节因子\n(PMID:8259518,8259519)。APC 的主要肿瘤抑制作用在于其调节细胞内β-连环蛋白水平的能力\n(PMID:11978510)。另外 APC 退出细胞核的能力对其肿瘤抑制功能至关重要(PMID:10984057)。当 APC 的\n活性丧失时,WNT 通路激活异常增加,通常导致增生并最终出现肿瘤进展(PMID:8259511)。有趣的是,抑制肿\n瘤需要 APC 的表达达到一定的阈值,且表达水平也被十分精确的进行调控,因为肿瘤发生需要β-连环蛋白达到\n一定的水平(PMID:11743581)。APC 基因中的突变导致家族性腺瘤性息肉病\n(FAP)(PMID:1651174,1651562),其中 95%的人发展成结直肠癌(PMID:1528264),APC 中的种系突变也导致\n许多相关疾病的发生,包括 Turcot 综合征,加德纳综合征和扁平腺瘤综合征(PMID:8593545)。在 50-80%的\n散发性结肠直肠癌中观察到 APC 突变,就像在 FAS 中发现的突变一样(PMID:17143297),另外在前列腺癌,胃\n癌,皮肤癌,子宫癌,乳腺癌,肺癌,膀胱癌和头颈部癌症中也观察到突变(cBioPortal,MSKCC,2015 年 4 月),大多\n数 APC 突变是截短的,并且大多数 APC 体细胞突变位于蛋白质的突变簇区域(MCR)内,这对于β-连环蛋白结合\n来说是重要的(PMID:10784639,1338904)。\nBRAF\nBRAF 蛋白是在丝裂原活化蛋白激酶(MAPK)级联反应(PMID:15520807)的调节中起关键作用的丝氨酸/苏氨\n酸激酶,其在生理上调节与细胞功能相关的基因的表达,包括增殖等活动(PMID:24202393)。BRAF 的基因改变\n主要见于黑色素瘤和甲状腺癌以及一小部分肺癌和结肠直肠癌中,最常见的 BRAF 点突变是 V600E,它可以调\n节蛋白激酶的活性,从而导致组成型 BRAF 激活,BRAFV600E 可以独立于 RAS 或上游激活而发出单体信号\n(PMID:20179705)。目前已发现其他的 BRAF 突变可以影响蛋白质的二聚化倾向\n(PMID:16858395,26343582,12068308)。这些 BRAF 突变的产物也可以以不受调节的方式激活 MAPK 信\n号传导,并且在某些情况下直接导致肿瘤生长(PMID:15520807)。\nEGFR\nEGFR 编码表皮生长因子受体。EGFR 通过其配体包括表皮生长因子(EGF)和转化生长因子-α(TGF-α)的结合\n激活致癌的 MAPK 和 PI3K/AKT/mTOR 信号级联的下游信号传导途径,最终导致细胞增殖,迁移和分化\n(PMID:18045542)。虽然 EGFR 通常在正常成人组织中以低水平表达,但是在许多癌症类型例如肺癌,脑癌,结\n直肠癌和头颈癌(PMID:10880430)中发现其通过突变和/或扩增使该受体过度激活,而在脑癌和结直肠癌\n中,EGFR 基因的拷贝数增加导致受体过表达(PMID:11426640)。然而,在肺癌中,最普遍的 EGFR 改变是激酶\n结构域中的突变,导致受体的组成性激活(PMID:15329413),但在胰腺癌和结直肠癌中很少发现 EGFR 的激活\n突变(PMID:24827134)。\nERBB2\nERBB2(也称 HER2)是受体酪氨酸激酶中表皮生长因子受体(EGFR)家族的成员,在一系列人类癌症(包括乳腺\n癌,胃癌/胃食管癌和子宫内膜癌)中异常扩增和/或过表达(PMID:19536107)。ERBB2/ERBB2 的独特之处在于\n它不直接结合自己的配体。相反,它通过结合(PMID:12620236)增强其他的配体如 EGFR(ERBB1)或 ERBB3\n的活性。事实上,ERBB2 是所有 ERBB 受体同种型(PMID:10220407,9130710)的优选结合配体,ERBB2/ERBB3\n复合物通过激活下游致癌 PI3K 途径(PMID:12853564)显示出高度的有丝分裂活性。或者,ERBB2 可同源二聚\n化并启动细胞内有丝分裂级联,包括 RAS/MAPK,PI3K/AKT/mTOR,SRC 和 STAT 信号传导途径\n(PMID:22785351)。大约 17%至 30%的人类乳腺肿瘤具有 ERBB2 基因扩增,这与患者总体生存率差和肿瘤\n复发的时间相关(PMID:3798106,23000897,9552035,9469329)。扩增的 ERBB2 与 ERBB3 异源二聚化以激\n活 PI3K/AKT/mTOR 信号传导并驱动乳腺癌中的肿瘤发生\n(PMID:12853564,23204226,12124352,18632642)。ERBB2 在约 20%胃或胃食管癌\n(PMID:24943493,21468131)中扩增,并且其过度表达被多种药物(例如曲妥珠单抗,阿托珠单抗,埃克替尼,拉\n帕替尼和培妥珠单抗)靶向(PMID:24799465)。但在非小细胞肺癌,卵巢癌,膀胱癌,子宫颈癌,子宫内膜癌,结肠\n直肠癌,胰腺癌和涎腺癌,软组织肉瘤中及胆管癌中,ERBB2 扩增的发生率很低(PMID:24656976)。最近在包括\n肺腺癌,小叶乳腺癌,膀胱癌,胃癌和子宫内膜癌在内的许多癌症中发现了较低频率的 ERBB2 激活突变,其中细",
    "role": "user"
  }
]
2026-08-10 14:56:51,676 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:51,676 INFO     29 [qwen-vl-table] page=24 LLM output (len=48):
{
  "report_date": "2025-05-05",
  "items": []
}
2026-08-10 14:56:51,677 WARNING  29 [qwen-vl-table] page=24 no items extracted
2026-08-10 14:56:51,677 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:51,678 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "胞外和激酶结构域中的反复热点经常出现改变(PMID:23000897,223220880,22908275)。目前有关 ERBB2\n—11—\n上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n奕检医学\nYIJIANMED LABORATORY\nYJ50430012T\n靶向治疗的药物正处于进一步开发中。\nFBXW7 基因编码 SCF(Skp1-Cul1-F-box 蛋白)泛素连接酶复合物识别底物的 F-box 蛋白亚基,在底物鉴定时\n该复合物会修饰底物,使其成为蛋白质降解的靶标。FBXW7 的底物包括蛋白质\nc-MYC,mTOR(PMID:18787170),NOTCH1,cyclin-E 和 JUN,它们在调节细胞分裂,分化和生长中起作用,并且\n在癌症中被不恰当地激活,且由于大多数 FBXW7 底物都是经过 SCF 复合物降解处理的原癌基因,所以 FBXW7\n起着肿瘤抑制剂的作用。突变或拷贝数异常会使 FBXW7 失活并导致癌蛋白的异常积累,随后发生恶性转化\n(PMID:18094723)。此外 FBXW7 中的突变可能对特异性功能如亚基二聚化,蛋白质定位,SCF 组装或底物识\n别产生负面影响。FBXW7 中的大多数突变是破坏底物结合的点突变,而小的缺失突变或插入突变数量则\n<10%(PMID:24853181,17909001)。\nFGFR1 编码成纤维细胞生长因子受体 1,这是一种对有丝分裂和分化过程十分重要的受体酪氨酸激酶。FGFR1\n由三个免疫球蛋白样细胞外结构域组成,其中包含一个跨膜成分和一个通过 MAPK 途径起作用的胞质酪氨酸\n激酶结构域(PMID:8622701)。在与成纤维细胞生长因子配体(主要是 FGF1 和 FGF2)结合后,FGFR1 蛋白迅速\n二聚化并最终内化至细胞核。然而,结合也随组织分布和配体的可用性而变化(PMID:16597617)。FGFR1 在\n组织中广泛表达,并且对于多种功能如胚胎发育,骨骼发生,有丝分裂发生和分化是必需的,而 FGFR1 突变则与\n身体畸形,智力低下和神经缺陷有关(PMID:23812909)。FGFR1 中的扩增或活化突变在包括肺癌,乳腺癌,前列\n腺癌,头颈癌和食道癌在内的多种癌症中发生,但突变频率不同\n(PMID:21160078,0919196,14614009,16807070,12147242)。在转移性肾细胞癌中,FGF 信号传导被怀疑\n是细胞对血管生成逃逸的 VEGF 导向疗法产生获得性耐药的原因(PMID:24387233)。目前,许多 FGFR 蛋白的\n小分子抑制剂正在使用中,其主要的区别在于特异性针对 FGFR 或针对其他受体酪氨酸激酶\n(RTK)(PMID:23696246,24265351)。\n成纤维细胞生长因子受体(FGFR)家族包括 4 种受体酪氨酸激酶(RTK):FGFR1-4。FGFR 的信号发生取决于激\n活酪氨酸激酶结构域的配体依赖性二聚化。由于扩增,突变,易位,选择性剪接或由成纤维细胞生长因子(FGF)\n增加活化而导致的 FGFR 功能失调会促进信号传导,肿瘤发生和细胞迁移(PMID:20094046)。FGFR2 激酶结\n构域突变存在于颅面综合征中,也出现在子宫内膜癌,宫颈癌和鳞状细胞癌中,而 FGFR2 扩增已在大约 10%的\n胃癌患者中发现并与预后不良有关。此外 FGFR2 单核苷酸多态性与 ER 阳性乳腺癌的发展有关,尽管病因尚不\n清楚(PMID:18437204),且成釉细胞瘤中 FGFR2 突变也非常频繁。\nFGFR3 基因编码成纤维细胞生长因子受体 3,这是一种跨膜酪氨酸激酶受体,属于 FGFR 家族(FGFR1-4)。\nFGFR3 蛋白与其同源配体即成纤维细胞生长因子(FGF)的结合会导致受体二聚化,随后激活并调节增殖,分化,\n细胞迁移和凋亡等下游途径(PMID:7542215,20094046)。FGFR3 基因中的可变剪接事件产生两种同种\n型,FGFR3b 和 FGFR3c,其具有独特的组织表达模式和配体结合特异性(PMID:8663044,7512569)。在约 15%\n的多发性骨髓瘤患者中观察到特异性 t(4;14)易位,导致 FGFR3 的组成型表达(PMID:17107900)。此外,在多\n达 70%的膀胱癌中观察到 FGFR3 的激活突变。其中,S249C 突变占所有突变的\n69%(PMID:11395371,12743143,16338952)。\n原癌基因 KIT 编码 3 型跨膜受体酪氨酸激酶,在与其配体干细胞因子(SCF)(也称为肥大细胞生长因子\n(MGF)(PMID:9438854))结合后,受体可通过二聚化和自磷酸化被激活。KIT 活化导致通过几种途径(包括\nPI3K,MAPK 和 STAT)的细胞内信号传导增加,最终导致细胞增殖和存活\n(PMID:17546049,11896121,22089421)。对于患有野生型胃肠间质瘤(GIST;无 KIT 或 PDGFRA 突变)的患\n者,NCCN 建议检测种系琥珀酸脱氢酶(SDH)突变。大约 10-15%的 GIST 是野生型;因此,没有突变并不排除\nGIST 的诊断。在没有 KIT 突变的患者中,具有晚期 GIST 的患者的一部分受益于伊马替尼(0-45%的患\n者)(NCCNSoftTissueSarcomav.2.2017)。KIT 激活突变发生在 80-90%的 GIST 中,分布在不同频率的多个\n外显子上(exon11(66.1%),exon9(13%),exon13(1.2%)和\nexon17(0.6%))(PMID:15365079,17268243,11719439)。至少有八种针对 KIT 的小分子酪氨酸激酶抑制剂\n(TKIs)已被美国食品和药物管理局批准,每种 TKI 的功效取决于激活 KIT 突变的位置\n(PMID:2427414,18955458,19164557)。\n—12—\n上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n奕检医学\nYIJIANMED LABORATORY\nYJ50430012T\nKRAS是小型GTP酶RAS家族的成员,该家族催化GTP水解为GDP。在生理条件下,这些RAS蛋白在活性(GTP\n结合)和非活性(GDP结合)状态之间循环,以激活受体酪氨酸激酶(RTK)下游的MAPK和PI3K致癌途径信号传\n导(PMID:22189424)。RAS酶的功能受鸟嘌呤核苷酸交换因子(GEF)如SOS的调节,这些因子可以使GDP与\nGTP交换,也可以通过GTP酶活化蛋白如NF1调节,从而提高RAS水解GTP的能力。一旦被激活,RAS可通\n过激活不同的细胞内信号传导途径(包括RAF/MEK/ERK和PI3K/AKT/mTOR途径)介导细胞增殖和其他细胞\n功能的调节。KRAS中的转化突变常见于胰腺癌,结肠癌,子宫内膜癌,卵巢癌和胆管癌;几乎所有这些突变都可\n导致KRAS的组成型活化,从而促进细胞增殖(PMID:21993244,24651010)。KRAS突变主要发生在三个主要\n热点G12,G13和Q61上,前两个发生在GTP-ase结构域,后者为干扰NF1结合和调节KRAS的能力\n(PMID:22589270,21993244,24651010)。其他不太明确表征的突变如A146T/V/P和L19F也已被表征,而\n且发现较低频率下也可处于活化状态(PMID:20147967,20432530,20570890)。种系KRAS突变可导致",
    "role": "user"
  }
]
2026-08-10 14:56:52,953 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:52,953 INFO     29 [qwen-vl-table] page=25 LLM output (len=48):
{
  "report_date": "2025-05-05",
  "items": []
}
2026-08-10 14:56:52,953 WARNING  29 [qwen-vl-table] page=25 no items extracted
2026-08-10 14:56:52,953 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:52,954 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "Noonan综合征(NS)和心脏-皮肤-皮肤(CFC)综合征(PMID:16474405,16474404,19467855,17056636),这\n些疾病与过度活化的MAPK途径,独特的临床特征和癌症易感性相关(PMID:19467855,17704260)。\nMAP2K1(MEK1)蛋白是一种丝氨酸/苏氨酸激酶,向RAF下游发出信号并激活ERK1/2,因此在MAP激酶\n(MAPK)级联中发挥关键调节作用。MAPK级联反应涉及不同的细胞过程,包括增殖,分化和转录调控,目前已经\n在几种不同的癌症类型中发现级联反应会因为其组分RAS和RAF的遗传突变而产生变化\nMAP2K1\n(PMID:12068308,12509763)。MEK1的突变很少见,但一般发生在携带BRAF或RAS突变的肿瘤类型中,包\n(PMID:22753777)。一些MEK1突变可以赋予细胞对MEK和RAF抑制剂的抗\n括黑色素瘤,结直肠癌和肺癌\n性(PMID:19915144,213383288)。\nMLH1蛋白对于DNA错配修复途径是必不可少的。MLH1与PMS2(最常见),PMS1或MLH3异二聚形成内\n切酶复合物,并切割受损的DNA链,导致其局部切除(PMID:10037723,10542278,10615123)。MLH1中的突\n变导致无法正确修复错配和插入/缺失环,这与微卫星重复序列经常相关,微卫星重复序列的改变可能是特别有\n害的,因为它们可能在其他基因中产生移码突变。MLH1中的突变发生在多种组织类型中,但在散发性结肠癌,\nMLH1\n胃癌和子宫内膜癌的特定子集以及遗传性的犬牙综合征(有时称为遗传性非息肉病性结肠癌(HNPCC))中最常\n见(PMID:8484122,8040889,8261393)。MLH1作为典型的肿瘤抑制基因,由于遗传或体细胞突变导致的一\n个等位基因的功能丧失往往会导致其他等位基因也丧失功能。而在治疗方面,FDA批准了pembrolizumab\n用于治疗错配修复缺陷型(dMMR)和MSI(微卫星不稳定性)肿瘤。\nMSH2(MutS蛋白同系物2)蛋白是参与错配修复的肿瘤抑制因子。MSH2与其他MutS蛋白如MSH6和\nMSH3形成异二聚体,分别形成MutS-α和MutS-β错配修复(MMR)复合物(PMID:8252616,7973733)。两种\n复合物都参与识别错配的碱基对,形成DNA-MutS复合物,该复合物发信号通知MMR机制的其他组分以切除\n异常核苷酸。MSH2和其他MMR基因与遗传性非息肉病性结肠癌(HNPCC),也称为Lynch综合征有关\nMSH2\n(PMID:428275,1648437)。MSH2突变占所有HNPCC病例(PMID:11852992)中的约40%,并且与MSI高\n表型以及MLH1中的突变(PMID:9823339,9354436)相关。尽管最常见于结肠癌,但MSH2突变在许多其他\n癌症类型和综合征中也有报道,包括子宫内膜癌、子宫癌以及皮脂腺肿瘤(PMID:19078925,16826164)。而在\n治疗方面,FDA批准了派姆单抗用于治疗错配修复缺陷型(dMMR)和MSI(微卫星不稳定性)肿瘤。\nMSH6(mutS同系物6)基因编码DNA修复错配蛋白MSH6。MSH6是与MSH2异二聚化形成MutS-α的\n肿瘤抑制剂。该复合物可识别单碱基对错配和二核苷酸插入-删除循环,启动错配修复(MMR)过程\nMSH6\n(PMID:8816473)。MSH6和其他MMR基因与遗传性非息肉病性结肠癌(HNPCC),也称为Lynch综合征有\n关(PMID:428275,1648437)。虽然最常见于结肠癌,但MSH6突变在许多其他癌症类型和综合征(包括子宫内\n膜癌和子宫癌)中也有报道(PMID:19078925,16106253)。而在治疗方面,FDA批准了派姆单抗用于治疗错配\n修复缺陷型(dMMR)和MSI(微卫星不稳定性)肿瘤。\nRas超家族包含超过150种具有GTP酶活性的小单体蛋白,其基于相似的序列和功能进一步分类为亚家族。\n在Ras亚科内有四个关键成员:K-Ras4a,K-Ras4b,N-Ras和H-Ras。这些蛋白质高度同源,并在所有细胞谱系\n和器官中检测到表达;然而,它们并不完全是多余的。某些成年组织优先表达特异性同种型\nNRAS\n(http://gan.sagepub.com/content/2/3/216.full),并且独特的翻译和修饰将它们分布到不同的亚细胞定位,\n—13—\n上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话:400-004-2111 网址:www.yjmedlab.com\n奕检医学\nYIJIANMED LABORATORY\nYJ50430012T\n从而激活特异性信号级反应,促进增殖,细胞运动,存活,血管生成,代谢和逃避抗肿瘤免疫应答\n(PMID:15731001;PMID:12728271)。Ras 蛋白在与 GTP 结合时具有活性,并且通过鸟嘌呤核苷酸交换因子\n(GEFs)进行 GDP 与 GTP 的交换。GEFs 通过加速 Ras 介导的 GTP 酶激活蛋白(GAP)平衡使 Ras 蛋白失活。\nRas是人类癌症中最常见的致癌基因,Ras编码基因NRAS,KRAS和HRAS中的突变常常损害 Ras 介导的GTP-\n水解,导致 Ras 的组成型激活。致癌 Ras 的恶性转化活性也依赖于脱甲基化,(PMID:22020205)。尽管在 Ras\n家族蛋白质中存在高同源性,但不同的 Ras 同种型在特定类型的癌症中优先突变。NRAS 基因与皮肤,造血和\n淋巴组织的癌症有关。\nNTRK1 基因编码原肌球蛋白受体激酶 A(TrkA),是 Trk 受体酪氨酸激酶家族的成员。NTRK1 由位于染色体\n1q21-22 上的 17 个外显子编码(PMID:12652644),并且可以产生三个不同的剪接变体,即 TrkAI,TrkAll 和\nTrkAIII。TrkAI 和 TrkAll 剪接变体具有高度的相似性,仅在 TrkAll1296 处插入 18 个核苷酸才有所不同\n(PMID:8325889)。在生物学上,TrkAI 被认为是神经母细胞瘤中的肿瘤抑制因子(PMID:19734938),而 TrkAll\n的特征在于增强与神经营养因子的亲和力(PMID:7972023)。通过 NTRK1 的外显子 6,7 和 9 缺失产生 TrkAIII\n变体,导致细胞外免疫球蛋白 C1 结构域的缺失。因此,TrkAIII 蛋白中缺失了几个 N-糖基化位点,限制了其对胞\n内膜隔室的表达,并诱导 PI3K/AKT/NF-κB 信号传导的组成型激活(Farina 等,2009)。重要的是要注意,TrkAIII\n剪接变体被认为是神经母细胞瘤中的致癌基因(PMID:19564412),并促进遗传不稳定性(PMID:19564412)。\nNTRK1\nTrkA 在神经,内分泌和免疫系统的细胞上表达,响应配体结合控制细胞增殖,分化,凋亡和细胞存活\n(PMID:25527197)。尽管神经营养因子 3(NT-3)和 4(NT-4)也可以激活 TrkA,但是它最常被神经生长因子\n(NGF)激活(PMID:18289031)。受体同二聚化后,下游信号级联,最常见的 RAS/MAPK,PI3K/AKT 和 PLCγ\n/PKC 通路被激活(PMID:25527197)。相反,在不存在配体的情况下,TrkA 可通过抑制 PI3K/AKT 信号启动促",
    "role": "user"
  }
]
2026-08-10 14:56:54,256 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:54,256 INFO     29 [qwen-vl-table] page=26 LLM output (len=48):
{
  "report_date": "2025-05-05",
  "items": []
}
2026-08-10 14:56:54,256 WARNING  29 [qwen-vl-table] page=26 no items extracted
2026-08-10 14:56:54,256 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:54,256 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "凋亡信号级联,导致 Bad 的去抑制,并激活 JNK 介导的促凋亡转录调节因子,如 Bim 和\nPuma(PMID:22465479)。NTRK1 重排发生在 12%的乳头状甲状腺癌中,3.3%的肺癌和近 1%的多形性恶性\n胶质瘤中。目前在胆道癌中也发现了 RABGAP1L-NTRK1 融合。在结直肠癌和甲状腺癌中,融合的伴侣基因\n包括 TPM3,TFG 和 TPR,而肺癌中检测到 MPRIP 和 CD74。NTRK1 基因融合了完整的 TRKA 激酶结构域,导\n致了 TRKA 激酶活性组成性激活。\n磷脂酰肌醇-3-激酶(PI3K)由调节亚基(p85α)和催化亚基(p110α)组成,它是由 PIK3CA 基因编码的催化亚基。\nPIK3CA 是癌症中最常见的突变基因之一,PI3K 的异常激活是转化事件(PMID:17376864)。多种受体酪氨酸\n激酶,包括 EGFR,ERBB2(ERBB2),RET,MET 和 VEGFR 等均可将细胞外信号转化为细胞内信号,并通过支架蛋白\n如 IRS1 或通过激活 RAS 将 PI3K 募集至质膜。刺激后,PI3K-110α将其脂质底物 PIP2(磷脂酰肌醇-4,5-二磷\n酸)转化为 PIP3(磷脂酰肌醇-3,4,5-二磷酸),激活几个信号级联反应,包括充分表征的 AKT-mTOR 通路。一旦\n被激活,AKT-mTOR 下游信号传导可促进细胞存活,增殖,生长和运动(PMID:16341083)。长期暴露于一些\nPI3K/mTOR 途径靶向药物可以减轻癌细胞 PI3K-AKT-mTOR 途径固有的自我调节特性,从而促进肿瘤对这\nPIK3CA\n些药物的耐药性(PMID:22576208)。\nPMS2 是一种内切核酸酶,在错配修复(MMR)途径中起重要作用。具体而言,PMS2 切割 DNA 以启动错配链\n的切除(PMID:20624957)。PMS2 突变导致不能正确修复 DNA 的错配和插入/缺失环,这导致肿瘤超突变增\n加和微卫星不稳定性高(MSI-H)表型(PMID:14871975)。PMS2 的种系突变可引起 Lynch 综合征,其易患某些\nPMS2\n癌症,包括结肠癌,子宫内膜癌和卵巢癌,并暗示 PMS2 为肿瘤抑制因子(PMID:16472587)。在来自多种组织类\n型的癌症中也报道了散发性 PMS2 突变(PMID:16472587)。肿瘤超突变与某些免疫疗法的反应有关。具体而\n言,pembrolizumab 已被 FDA 批准用于所有 MMR 缺陷和 MSI 肿瘤,不论特定肿瘤病因\n(PMID:25409260,26028255)\nPTEN 编码肿瘤抑制因子,其是人癌症中最频繁突变的基因之一(PMID:9072974,9090379,22473468)。PTEN\n具有几种生理功能,最显着的是在细胞膜上将磷脂酰肌醇(3,4,5)-三磷酸(PIP3)转化为磷脂酰肌醇(4,5)-三磷酸\n(PIP2)(PMID:18767981)。PTEN 功能的损害可导致 PIP3 积累和分解代谢下游 AKT/mTOR 信号传导的组成\n型激活。因此,PTEN 失活可促进细胞生长,增殖和存活(PMID:12040186)。另外,核 PTEN 被认为可调节 RAD51\nPTEN\n表达,与 DNA 链断裂的同源重组和修复相关(PMID:17218262,23888040)。因此,PTEN 的丧失也可能导致更\n严重的基因组不稳定性并为其他有害突变的积累提供帮助。PTEN 经常在许多类型的人类癌症中发生突变\n—14—\n上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n奕检医学\nYIJIANMED LABORATORY\nYJ50430012T\n(PMID:15254063),PTEN 种系功能丧失突变发生在约80%的癌症易感性综合征 Cowden 病患者中,其与高外\n显率乳腺癌和甲状腺癌相关(PMID:9467011,24136893,21430697)。\nRET 是一种受体酪氨酸激酶,可与神经胶质细胞系衍生的神经营养因子(GDNF)家族的配体结合,并通过促癌基\n因丝裂原活化蛋白激酶(MAPK)和磷酸肌醇 3-激酶(PI3K)途径传递细胞内信号(PMID:24561444)。RET 通常\n在发育中的胚胎中表达,在神经和神经内分泌中起着特别重要的作用(PMID:8306871)。在癌症中,RET 可以通\n过点突变或基因重排与多种易位配体融合,产生组成型活性胞质癌蛋白(PMID:24561444)。RET 中可遗传的激\n活突变导致高度渗透性家族性癌症综合征多发性内分泌腺癌 2A 型(MEN2A:甲状腺髓样癌,嗜铬细胞瘤,甲状\n旁腺功能亢进),多发性内分泌腺瘤 2B 型(MEN2B:甲状腺髓样癌,嗜铬细胞瘤,多发性粘膜神经瘤和肠神经节细\n胞瘤)和家族性甲状腺髓样癌(FMTC)(PMID:15322516)。致癌体细胞突变包括 RET 基因座的点突变和基因组\n重排。已经在各种癌症中鉴定出这些变异,包括乳头状甲状腺癌,肺腺癌和慢性髓单核细胞白血病(CMML)。此\n外,野生型 RET 的异常表达或活化与胰腺癌中的肿瘤侵袭和转移以及乳腺癌中的内分泌治疗抗性相关\n(PMID:24561444)。\nTP53 编码 p53 肿瘤抑制蛋白,这是一种转录因子,可通过诱导下游抗肿瘤反应如 DNA 修复和凋亡\n(PMID:11099028)来响应细胞应激,包括 DNA 损伤和致癌活化。TP53 是人类癌症中最常见的突变基因,并且\n在癌症易感性综合征 Li-Fraumeni 中可发生种系突变(PMID:22713868,21765642)。p53 蛋白由 N-末端反\n式激活结构域,中心 DNA 结合结构域,寡聚化结构域和 C-末端调节结构域组成(PMID:22713868)。\n— 15 —\n上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n奕检医学\nYIJIANMED LABORATORY\nYJ50430012T\n常见靶向药物说明\n药物\n中文\n药物说明\nFDA\nNPMA\nTrametinib\n曲美替尼\n曲美替尼\n(Trametinib) 是一",
    "role": "user"
  }
]
2026-08-10 14:56:55,374 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:55,374 INFO     29 [qwen-vl-table] page=27 LLM output (len=40):
{
  "report_date": null,
  "items": []
}
2026-08-10 14:56:55,374 WARNING  29 [qwen-vl-table] page=27 no items extracted
2026-08-10 14:56:55,375 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:55,375 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "种口服生物可利用的\n丝裂原激活的细胞外\n信号调节激酶 1\n(MEK1) 和 MEK2\n抑制剂。它于 2013\n年 5 月首次被 FDA\n批准用于治疗黑色素\n瘤。\nFDA 批准：1. 曲美替尼联合达拉非尼用\n于 BRAF V600E 或 V600K 突变的不可切\n除或转移性黑色素瘤患者的治疗；2. 曲\n美替尼联合达拉非尼用于 BRAF V600E\n或 V600K 突变且累及淋巴结的黑色素瘤\n患者术后的辅助治疗；3. 曲美替尼联合\n达拉非尼治疗 BRAF V600E 突变的转移\n性非小细胞肺癌(NSCLC)患者；4. 曲美\n替尼联合达拉非尼治疗 BRAF V600E 突\n变的局部晚期或转移性甲状腺未分化癌\n(ATC)患者，无令人满意的局部区域治疗\n选择；5. 曲美替尼联合达拉非尼用于治\n疗 1 岁及以上 BRAF V600E 突变的不可\n切除或转移性实体瘤的成人和儿童患者，\n这些患者在先前的治疗后已经进展，并且\n没有令人满意的替代治疗方案。6. 曲美\n替尼联合达拉非尼治疗 1 岁以上 BRAF\nV600E 突变的低级别胶质瘤(LGG)患\n儿，需要全身治疗。\nNMPA 批准:1. 联合甲磺酸\n达拉非尼适用于治疗 BRAF\nV600 突变阳性的不可切除\n或转移性黑色素瘤患者；2.\n联合甲磺酸达拉非尼适用于\nBRAF V600 突变阳性的 III\n期黑色素瘤患者完全切除后\n的辅助治疗；3. 联合甲磺酸\n达拉非尼适用于治疗 BRAF\nV600 突变阳性的转移性非\n小细胞肺癌患者。\nEncorafenib\nEncorafenib 是一种\n口服 Raf 激酶抑制\n剂，具有潜在的抗肿\n瘤活性，特异性抑制\nRaf 激酶（RAF/丝裂\n原活化蛋白激酶激酶\n(MEK)/细胞外信号\n相关激酶（ERK）信\n号通路中的一种丝氨\n酸/苏氨酸酶）。\nFDA 批准：1. 与 binimetinib 联合，用\n于治疗经 FDA 批准的试验检测为 BRAF\nV600E 或 V600K 突变的不可切除或转移\n性黑色素瘤患者；2. 联合 binimetinib\n治疗经 FDA 批准试验检测为 BRAF\nV600E 突变的转移性非小细胞肺癌成年\n患者；3. 联合西妥昔单抗，用于既往治\n疗后经 FDA 批准试验检测为 BRAF\nV600E 突变的成人转移性结直肠癌患者\n的治疗。\n无\nTucatinib\nTucatinib 是一种酪\n氨酸激酶抑制剂，靶\n向人表皮生长因子受\n体 2 （HER2），与",
    "role": "user"
  }
]
2026-08-10 14:56:56,148 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:56,148 INFO     29 [qwen-vl-table] page=28 LLM output (len=40):
{
  "report_date": null,
  "items": []
}
2026-08-10 14:56:56,148 WARNING  29 [qwen-vl-table] page=28 no items extracted
2026-08-10 14:56:56,148 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:56,149 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "其他抗肿瘤药联合用\n于治疗难治性、晚期\n或转移性 HER2 阳\n性乳腺癌和结直肠\n癌。\nFDA 批准：1. Tucatinib 联合曲妥珠单\n抗和卡培他滨用于晚期不可切除或转移\n性 HER2 阳性乳腺癌成年患者，包括脑\n转移患者，他们在转移性情况下既往接受\n过一种或多种基于抗 HER2 的治疗方\n案；2. Tucatinib 与曲妥珠单抗联合用于\n治疗 RAS 野生型 HER2 阳性不可切除或\n转移性结直肠癌的成年患者，这些患者在\n氟尿嘧啶、奥沙利铂和伊立替康为基础的\n化疗后进展。\n无\n— 16 —\n上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n奕检医学\nYIJIANMED LABORATORY\nYJ50430012T\nDabrafenib\n达拉非尼\n达拉非尼\n(Dabrafenib) 是一\n种有机氟化合物和抗\n肿瘤剂, 用作其甲磺\n酸盐治疗转移性黑色\n素瘤。它具有抗肿瘤\n剂、B-Raf 抑制剂和\n抗冠状病毒剂的作\n用。它是一种磺胺类\n化合物, 一种有机氟\n化合物, 是 1,3-噻唑\n类和氨基嘧啶的成\n员。达拉非尼是一种\n可逆的 ATP 竞争性\n激酶抑制剂, 靶向\nMAPK 通路。\nFDA 批准: 1. 作为单一药物, 用于治疗\n经 FDA 批准的检测检测到的具有\nBRAF V600E 突变的不可切除或转移性\n黑色素瘤患者; 2. 与曲美替尼联合用于:\na. FDA 批准的检测检测到 BRAF V600E\n或 V600K 突变的不可切除或转移性黑色\n素瘤患者的治疗; b. 通过 FDA 批准的试\n验检测出具有 BRAF V600E 或 V600K 突\n变的黑色素瘤患者的辅助治疗, 以及在完\n整切除后累及淋巴结的患者; c. 治疗经\nFDA 批准的检测检测到的具有 BRAF\nV600E 突变的转移性非小细胞肺癌\n(NSCLC) 患者; d. 治疗 BRAF V600E\n突变的无满意的局部区域治疗方案的局\n部晚期或转移性未分化甲状腺癌患者; e.\n1 岁及以上的成人和儿童 BRAF V600E\n突变不可切除或转移性实体瘤患者的治\n疗, 这些患者在先前治疗后进展, 没有令\n人满意的替代治疗方案; f. 治疗 1 岁及\n以上患有具有 BRAF V600E 突变且需\n要全身治疗的低级别胶质瘤 (LGG) 的\n儿科患者。(由于已知 BRAF 抑制的内在\n抗性, TAFINLAR 不适合用于结直肠癌患\n者的治疗; 并且不用于 BRAF 野生型实体\n瘤患者的治疗)\nNMPA 批准用于:1. 联合曲",
    "role": "user"
  }
]
2026-08-10 14:56:56,781 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:56,781 INFO     29 [qwen-vl-table] page=29 LLM output (len=2):
{}
2026-08-10 14:56:56,781 WARNING  29 [qwen-vl-table] page=29 no items extracted
2026-08-10 14:56:56,781 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:56,781 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "美替尼用于治疗 BRAF\nV600 突变阳性的不可切除\n或转移性黑色素瘤患者; 2.\n联合曲美替尼用于 BRAF\nV600 突变阳性的 III 期黑色\n素瘤患者完全切除后的辅助\n治疗; 3. 联合曲美替尼用于\n治疗 BRAF V600 突变阳性\n的转移性非小细胞肺癌患\n者。\nRegorafenib\n瑞戈非尼\n瑞戈非尼\n(Regorafenib) 是一\n种激酶抑制剂。用于\n治疗既往接受过化\n疗、抗 EGFR 或抗\nVEGF 治疗的转移性\n结直肠癌患者。它具\n有抗肿瘤药、酪氨酸\n激酶抑制剂和肝毒性\n药物的作用。\nFDA 批准: 1. 用于先前接受索拉非尼治\n疗的肝癌 (HCC) 患者; 2. 用于治疗转\n移性结直肠癌 (mCRC) 的患者, 之前曾\n接受氟嘧啶, 奥沙利铂和伊立替康为基础\n的化疗、抗 VEGF 治疗, 以及 KRAS 野生\n型的抗 EGFR 治疗; 3. 用于既往接受甲\n磺酸伊马替尼和苹果酸舒尼替尼治疗的\n局部晚期、不可切除或转移性胃肠道间质\n瘤 (GIST) 患者的治疗。\nNMPA 批准:1. 用于治疗既\n往接受过索拉非尼治疗的肝\n细胞癌 (HCC) 患者; 2. 用\n于治疗既往接受过以氟尿嘧\n啶、奥沙利铂和伊立替康为\n基础的化疗, 以及既往接受\n过或不适合接受抗 VEGF 治\n疗、抗 EGFR 治疗 (KRAS\n野生型) 的转移性结直肠癌\n(mCRC) 患者; 3. 用于既\n往接受过甲磺酸伊马替尼及\n苹果酸舒尼替尼治疗的局部\n晚期的、无法手术切除的或\n转移性的胃肠道间质瘤\n(GIST) 患者。\nFruquintinib\n呋喹替尼\n呋喹替尼\n呋喹替尼是一个喹唑\n啉类小分子血管生成\n抑制剂, 主要作用靶\n点是 VEGFR 激酶家族\n(VEGFR1、2 和 3)。\nFDA 批准: 适用于既往接受过氟尿嘧啶\n类、奥沙利铂和伊立替康为基础的化疗,\n以及既往接受过或不适合接受抗血管内\n皮生长因子 (VEGF) 治疗、抗表皮生长\n因子受体 (EGFR) 治疗 (RAS 野生型)\nNMPA 批准: 呋喹替尼胶囊\n单药适用于既往接受过氟尿\n嘧啶类、奥沙利铂和伊立替\n康为基础的化疗, 以及既往\n接受过或不适合接受抗血管\n— 17 —",
    "role": "user"
  }
]
2026-08-10 14:56:57,523 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:57,523 INFO     29 [qwen-vl-table] page=30 LLM output (len=40):
{
  "report_date": null,
  "items": []
}
2026-08-10 14:56:57,523 WARNING  29 [qwen-vl-table] page=30 no items extracted
2026-08-10 14:56:57,523 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:57,524 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话: 400-004-2111 网址: www.yjmedlab.com\n奕检医学\nYIJIANMED LABORATORY\nYJ50430012T\n通过抑制血管内皮细\n胞表面的 VEGFR 磷酸\n化及下游信号转导,\n抑制血管内皮细胞的\n增殖、迁移和管腔形\n成，从而抑制肿瘤新\n生血管的形成，最终\n发挥肿瘤生长抑制效\n应。\n的转移性结直肠癌患者。\n内皮生长因子 (VEGF) 治疗、\n抗表皮生长因子受体\n(EGFR) 治疗 (RAS 野生型)\n的转移性结直肠癌患者。\nSelpercatinib\n塞普替尼\n塞普替尼\n(Selpercatinib) 是\n一种选择性 RET 激酶\n抑制剂, 能够阻断 RET\n激酶, 并阻止癌细胞\n生长。\nFDA 批准: 1. 用于治疗局部晚期或转移\n性非小细胞肺癌的成年患者, 经 FDA 批\n准的试验检测到 RET 基因融合; 2. 适用\n于 2 岁及以上的成人和儿童晚期或转移\n性甲状腺髓样癌 (MTC) 患者, 经 FDA 批\n准的试验检测出 RET 突变, 需要系统性\n治疗; 3. 用于治疗 2 岁及以上的, 经 FDA\n批准的试验检测具有 RET 基因融合的晚\n期或转移性甲状腺癌的成人和儿童患者,\n这些患者需要系统性治疗, 并且是放射性\n碘难治性 (如果放射性碘是合适的); 4. 适\n用于经 FDA 批准的试验检测为 RET 基因\n融合的局部晚期或转移性实体肿瘤的 2\n岁及以上的成人和儿童患者, 这些患者在\n接受系统性之前或之后有进展, 或者没有\n令人满意的替代治疗方案。\nNMPA 批准: 塞普替尼用于\n治疗 RET 基因融合阳性的局\n部晚期或转移性非小细胞肺\n癌成人患者; 2. 需要系统性\n治疗的晚期或转移性 RET 突\n变型甲状腺髓样癌成人和\n12 岁及以上儿童患者、以及\n需要系统性治疗且放射性碘\n难治 (如果放射性碘适用)\n的晚期或转移性 RET 融合阳\n性甲状腺癌成人和 12 岁及\n以上儿童患者。\nRepotrectinib\n瑞普替尼\n瑞普替尼\n(Repotrectinib) 是\n一种酪氨酸蛋白激酶\n原癌基因 ROS1 和原\n肌球蛋白受体酪氨酸\n激酶 (TRKs) TRKA、\nTRKB 及 TRKC 的抑制\n剂。\nFDA 批准: 1. 用于治疗 ROS1 阳性的局",
    "role": "user"
  }
]
2026-08-10 14:56:57,598 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:56:57.597+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 64, "failed": 0, "current": {"7630dbd094ca11f1bd9827cf206dfa2d": {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:56:58,250 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:58,250 INFO     29 [qwen-vl-table] page=31 LLM output (len=40):
{
  "report_date": null,
  "items": []
}
2026-08-10 14:56:58,250 WARNING  29 [qwen-vl-table] page=31 no items extracted
2026-08-10 14:56:58,251 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:58,251 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "部晚期或转移性非小细胞肺癌成人患者;\n2. 用于治疗 12 岁及以上具有神经营养\n性酪氨酸受体激酶 (NTRK) 基因融合的局\n部晚期、转移性或手术切除可能导致严重\n疾病、治疗后病情进展或没有令人满意的\n替代疗法的成人和儿童实体瘤患者。\nNMPA 批准: 适用于 ROS1\n阳性的局部晚期或转移性非\n小细胞肺癌 (NSCLC) 成人\n患者。\nEntrectinib\n恩曲替尼\n恩曲替尼\n(Entrectinib) 是一\n种原肌球蛋白受体酪\n氨酸激酶 (TRK)\nTRKA、TRKB、TRKC、\n原癌基因酪氨酸蛋白\n激酶 ROS1 和间变\n性淋巴瘤激酶 (ALK)\n抑制剂。它于 2019\n年 8 月获得 FDA\n批准用于治疗 ROS1\n阳性转移性非小细胞\nFDA 批准: 1. 用于治疗 ROS1 阳性的转\n移性非小细胞肺癌 (NSCLC) 成人患者;\n2. 用于治疗年龄大于 1 个月的儿童和成人\n实体瘤患者: a. 具有经 FDA 批准的试验\n检测到神经营养性酪氨酸受体激酶\n(NTRK) 基因融合, 没有已知的获得性\n抗性突变; b. 转移或手术切除可能导致严\n重的并发症; c. 治疗后进展或没有令人\n满意的替代疗法。\nNMPA 批准: 1. ROS1 阳性\n的局部晚期或转移性非小细\n胞肺癌 (NSCLC) 成人患者;\n2. 用于符合下列条件的成\n人和 1 月龄以上儿童实体\n瘤患者: a. 经充分验证的检\n测方法诊断为携带神经营养\n酪氨酸受体激酶 (NTRK) 融\n合基因且不包括已知获得性\n耐药突变; b. 患有局部晚\n期、转移性疾病或手术切除\n可能导致严重并发症的患\n— 18 —\n上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n奕检医学\nYIJIANMED LABORATORY\nYJ50430012T\n肺癌和 NTRK 基因\n融合阳性实体瘤。\n者；c. 无满意替代治疗或既\n往治疗失败的患者。\nLarotrectinib\n拉罗替尼\n拉罗替尼\n(Larotrectinib) 是\n一种原肌球蛋白受体\n激酶(TRK), TRKA、\nTRKB、TRKC 的抑制\n剂。TRKA、TRKB 和\nTRKC 由 NTRK1、\nNTRK2 和 NTRK3 基\n因编码。这些基因与",
    "role": "user"
  }
]
2026-08-10 14:56:58,878 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:58,878 INFO     29 [qwen-vl-table] page=32 LLM output (len=2):
{}
2026-08-10 14:56:58,878 WARNING  29 [qwen-vl-table] page=32 no items extracted
2026-08-10 14:56:58,879 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:58,879 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "不同配体基因间的框\n架内融合导致的染色\n体重排可产生组成性\n激活嵌合 TRK 融合蛋\n白, 其可作为致癌驱\n动因子, 促进肿瘤细\n胞系中的细胞增殖和\n存活。\nFDA 批准: 用于治疗具备以下条件的成\n人和儿童实体瘤患者: 1. 具有神经营养\n性受体酪氨酸激酶 (NTRK) 基因融合,\n但没有已知的获得性抗性突变; 2. 转移\n或手术切除可能导致严重的发病率; 3.\n没有令人满意的替代治疗或治疗后进展。\nNMPA 批准: 用于治疗符合\n下列条件的成人和儿童实体\n瘤患者: 1. 经充分验证的检\n测方法诊断为携带神经营养\n酪氨酸受体激酶 (NTRK) 融\n合基因且不包括已知获得性\n耐药突变; 2. 患有局部晚\n期、转移性疾病或手术切除\n可能导致严重并发症的患\n者; 3. 无满意替代治疗或既\n往治疗失败的患者。\nCetuximab\n西妥昔单抗\n西妥昔单抗\n(Cetuximab) 是一\n种重组嵌合人/小鼠\nIgG1 单克隆抗体, 与\n表皮生长因子受体\n(EGFR) 竞争性结\n合, 并竞争性抑制表\n皮生长因子 (EGF)\n的结合。EGFR 是受体\n酪氨酸激酶 ErbB 家\n族的一员, 存在于正\n常细胞和肿瘤细胞\n中; 它负责调节上皮\n组织的发育和体内平\n衡。EGFR 与各种类型\n的癌症有关, 因为它\n通常在恶性细胞中过\n表达, 并且 EGFR 过\n表达与更晚期的疾病\n和不良预后有关。\nEGFR 在某些类型的\n癌症中经常发生突\nFDA 批准: 1. 用于经 FDA 批准的检测\n检测到 KRAS 突变阴性 (野生型)、EGFR\n表达阳性的转移性结直肠癌患者 (使用限\n制: 不适用于 RAS 突变或 RAS 突变未知\n的结直肠癌患者) : a.作为单药治疗, 用\n于既往经历奥沙利铂或伊立替康为基础\n的化疗方案并失败以及对伊立替康不耐\n受的患者; b.与 FOLFIRI 联合用于一线\n治疗; c.与伊立替康联合用于伊立替康为\n基础的化疗难治的患者; 2. 用于治疗头\n颈癌: a.局部或区域晚期头颈部鳞状细胞\n癌联合放射治疗; b.复发性局部区域疾病\n或头颈部转移性鳞状细胞癌联合氟尿嘧\n啶铂类治疗; c.铂类治疗后进展的头颈部\n复发性或转移性鳞状细胞癌; 3. 与\nEncorafenib 联合用于治疗经 fda 批准的",
    "role": "user"
  }
]
2026-08-10 14:56:59,485 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:59,486 INFO     29 [qwen-vl-table] page=33 LLM output (len=2):
{}
2026-08-10 14:56:59,486 WARNING  29 [qwen-vl-table] page=33 no items extracted
2026-08-10 14:56:59,486 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:56:59,486 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "试验检测出 BRAF V600E 突变的转移性\n结直肠癌(CRC)成人患者。\nNMPA 批准: 1. 用于治疗\nRAS 基因野生型的转移性\n结直肠癌:a.与 FOLFOX 或\nFOLFIRI 方案联合用于一线\n治疗; b. 与伊立替康联合用\n于经含伊立替康治疗失败后\n的患者; 2. 用于治疗头颈部\n鳞状细胞癌: a. 与铂类和氟\n尿嘧啶化疗联合用于一线治\n疗复发和/或转移性疾病; b.\n与放疗联合用于治疗局部晚\n期疾病。\n—19—\n上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话: 400-004-2111 网址: www.yjmedlab.com\n奕检医学\nYIJIANMED LABORATORY\nYJ50430012T\n变，并作为肿瘤发生\n的驱动因素。在体外,\n西妥昔单抗被证明在\n许多癌细胞系和人肿\n瘤异种移植物中具有\n抗肿瘤作用。\nPanitumumab 是一\n种对表皮生长因子受\n体 （EGFR） 具有特\n异性的人\nlgG2kappa 单克隆\n抗体。单克隆抗体\nE7.6.3 与 EGFR 结\n合，阻断表皮生长因\n子的结合并将生长因\n子 α 转化为表达\nEGFR 的癌细胞,并最\n终抑制 EGFR 依赖性\n细胞活化和增殖。\nFDA 批准：用于 RAS 野生型 (定义为\nKRAS 和 NRAS 中的野生型) 转移性结直\n肠癌 (mCRC) 患者：1. 单药治疗既往\n经过氟嘧啶, 奥沙利铂, 和伊立替康化疗\n方案后疾病进展的转移性结直肠癌; 2.\n与 FOLFOX 联合用于一线治疗。（使用\n限制：携带 RAS 基因突变或者 RAS 突变\n状态不明的结直肠癌的治疗不建议使用\n帕尼单抗）。\n无\nPanitumumab\n贝伐珠单抗是利用重\n组 DNA 技术制备的\n一种人源化单克隆抗\n体 IgG1, 通过与人血\n管内皮生长因子\n(VEGF) 结合, 抑制\nVEGF 与其受体结合,\n阻断血管生成的信号\n传导途径, 抑制肿瘤\n细胞生长。作为抗肿\n瘤血管生成的重要药\n物之一, 贝伐珠单抗\n被应用于多种恶性肿\n瘤的治疗。\nFDA 批准:1. 转移性结直肠癌:a. 与 5-\n氟尿嘧啶化疗联合作为转移性结直肠癌",
    "role": "user"
  }
]
2026-08-10 14:57:00,281 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:00,282 INFO     29 [qwen-vl-table] page=34 LLM output (len=48):
{
  "report_date": "2025-05-05",
  "items": []
}
2026-08-10 14:57:00,282 WARNING  29 [qwen-vl-table] page=34 no items extracted
2026-08-10 14:57:00,282 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:00,282 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "的一线或二线治疗方案; b. 与氟尿嘧啶\n-伊立替康或氟尿嘧啶 -奥沙利铂为基础\n的化疗联合用于经贝伐单抗一线治疗后\n出现疾病进展的转移结直肠癌的二线治\n疗; c. 贝伐单抗联合曲氟尿苷和替吉奥\n用于转移性结直肠癌的治疗, 此前使用氟\n尿嘧啶、奥沙利铂和伊立替康为基础的化\n疗, 抗 VEGF 生物治疗, 如果 RAS 野生\n型, 抗 EGFR 治疗; 2. 非小细胞肺癌:\na. 贝伐珠单抗联合紫杉醇和卡铂一线治\n疗不可切除的局部晚期、复发性或转移性\n非鳞状非小细胞肺癌; b. 贝伐单抗联合\n阿替利珠单抗、紫杉醇和卡铂一线治疗无\nEGFR 或 ALK 基因组肿瘤畸变的转移性\n非鳞非小细胞肺癌; 3. 贝伐珠单抗治疗\n成人复发性胶质母细胞瘤; 4. 贝伐珠单\n抗联合干扰素α治疗转移性肾细胞癌; 5.\n贝伐珠单抗联合紫杉醇和顺铂, 或紫杉醇\n和拓扑替康治疗持续性、复发性或转移性\n宫颈癌; 6. 上皮性卵巢癌、输卵管癌或\nNMPA 批准:1. 转移性结直\n肠癌: 贝伐珠单抗联合以氟\n嘧啶为基础的化疗适用于转\n移性结直肠癌患者的治疗;\n2. 晚期、转移性或复发性非\n小细胞肺癌: 贝伐珠单抗联\n合以铂类为基础的化疗用于\n不可切除的晚期、转移性或\n复发性非鳞状细胞非小细胞\n肺癌患者的一线治疗; 3. 复\n发性胶质母细胞瘤: 贝伐珠\n单抗用于成人复发性胶质母\n细胞瘤患者的治疗; 4. 肝细\n胞癌: 贝伐珠单抗联合阿替\n利珠单抗治疗既往未接受过\n全身系统性治疗的不可切除\n肝细胞癌患者; 5. 上皮性卵\n巢癌、输卵管癌或原发性腹\n膜癌: 贝伐珠单抗联合卡铂\n和紫杉醇用于初次手术切除\n后的 III 期或 IV 期上皮性\n卵巢癌、输卵管癌或原发性\nBevacizumab\n贝伐珠单抗\n— 20 —\n上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n奕检医学\nYIJIANMED LABORATORY\nYJ50430012T\n原发性腹膜癌：a. 贝伐珠单抗与卡铂和\n紫杉醇联合使用，随后以贝伐珠单抗作为\n单一药物，用于初始手术切除后的 III 期\n或 IV 期上皮性卵巢癌、输卵管癌或原发\n性腹膜癌；b.贝伐珠单抗联合紫杉醇、聚\n乙二醇脂质体多柔比星或拓扑替康治疗\n既往接受化疗方案不超过 2 种的铂类耐\n药复发的上皮性卵巢癌、输卵管癌或原发\n性腹膜癌；c. 贝伐珠单抗联合卡铂和紫\n杉醇或卡铂和吉西他滨，随后以贝伐单抗\n作为单药，用于铂类敏感的复发的上皮性\n卵巢癌、输卵管癌或原发性腹膜癌；d. 贝\n伐珠单抗与奥拉帕利联合用于晚期上皮\n性卵巢癌、输卵管癌或原发性腹膜癌成年\n患者的一线维持治疗，这些患者对一线铂\n类化疗完全或部分应答，且其癌症与同源",
    "role": "user"
  }
]
2026-08-10 14:57:01,072 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:01,072 INFO     29 [qwen-vl-table] page=35 LLM output (len=2):
{}
2026-08-10 14:57:01,073 WARNING  29 [qwen-vl-table] page=35 no items extracted
2026-08-10 14:57:01,073 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:01,074 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "重组缺失阳性状态有关，即有害或疑似有\n害 BRCA 基因突变和/或基因组不稳定；\n7. 贝伐珠单抗与阿替利珠单抗联合治\n疗既往未接受过系统治疗的不可切除性\n或转移性肝细胞癌患者。\n腹膜癌患者的一线治疗；6.\n宫颈癌：贝伐珠单抗联合紫\n杉醇和顺铂或紫杉醇和托泊\n替康用于持续性、复发性或\n转移性宫颈癌患者的治疗；\n7. 不可切除或转移性肝细\n胞癌：贝伐珠单抗联合信迪\n利单抗，用于既往未接受过\n系统治疗的不可切除或转移\n性肝细胞癌的一线治疗；8.\n晚期非鳞状非小细胞肺癌：\n贝伐珠单抗联合信迪利单\n抗、培美曲塞和顺铂，用于\n经表皮生长因子受体酪氨酸\n激酶抑制剂（EGFR-TKI）治\n疗失败的 EGFR 基因突变\n阳性的局部晚期或转移性非\n鳞状非小细胞肺癌\n(NSCLC) 患者的治疗。\n纳武利尤单抗\n(Nivolumab) 是一\n种全人源免疫球蛋白\n( Ig ) G4 单克隆抗体，\n针对人细胞表面负性\n免疫调节受体程序性\n死亡受体- 1 ( PD -\n1、PCD - 1)，具有免\n疫检查点抑制和抗肿\n瘤活性。给药后，纳\n武单抗通过其配体程\n序性细胞死亡配体 1\n( PD-L1 )和程序性细\n胞死亡配体 2\n( PD-L2 )结合并阻断\n免疫球蛋白超家族\n( IgSF )跨膜蛋白 PD -\n1 的活化。PD - 1 和\nPD - L1 在某些癌细\n胞上过表达，PD - L2\n主要表达于抗原呈递\n细胞( APC )。这导致\n了 T 细胞的激活和细\n胞介导的针对肿瘤细\nFDA 批准：1. 用于黑色素瘤患者：a. 单\n药或联合伊匹木单抗，用于成人和儿童\n(12 岁及以上)不可切除或转移性黑色素\n瘤患者；b. 用于完全切除 IIB 期、IIC 期、\nIII 期或 IV 期黑色素瘤的 12 岁及以上儿\n童和成人患者的辅助治疗；2. 用于非小\n细胞肺癌患者：a. 联合含铂双药化疗，\n用于在新辅助环境下可切除(肿瘤≥4cm\n或淋巴结阳性)的非小细胞肺癌的成年患\n者；b. 联合伊匹木单抗作为一线治疗，\n经 FDA 批准的试验检测到 D-L1 表达阳\n性（定义为表达 PD-L1 的肿瘤细胞≥\n1%) 无 EGFR 或 ALK 基因突变的转移性\n非小细胞肺癌成年患者；c. 联合伊匹木\n单抗和 2 周期铂双药化疗作为一线治疗，\n无 EGFR 或 ALK 基因突变的转移性或复\n发性非小细胞肺癌成年患者；d. 用于在",
    "role": "user"
  }
]
2026-08-10 14:57:01,704 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:01,704 INFO     29 [qwen-vl-table] page=36 LLM output (len=2):
{}
2026-08-10 14:57:01,704 WARNING  29 [qwen-vl-table] page=36 no items extracted
2026-08-10 14:57:01,704 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:01,705 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "铂类化疗中或化疗后进展转移性非小细\n胞肺癌的成人患者。对于 EGFR 或 ALK\n基因突变的患者，在接受 OPDIVO 之前，\n应在 FDA 批准的针对这些突变的治疗中\n出现疾病进展；3. 联合伊匹木单抗作为\n一线治疗不可切除的成人恶性胸膜间皮\n瘤；4. 用于肾细胞癌患者：a. 联合伊匹\nNMPA 批准:1. 用于治疗表\n皮生长因子受体 (EGFR) 基\n因突变阴性和间变性淋巴瘤\n激酶 (ALK) 阴性、既往接\n受过含铂方案化疗后疾病进\n展或不可耐受的局部晚期或\n转移性非小细胞肺癌\n(NSCLC) 成人患者；2. 联\n合含铂双药化疗适用于新辅\n助治疗可切除的 (肿瘤直径\n≥4cm 或淋巴结阳性) 非小\n细胞肺癌 (NSCLC) 成人患\n者；3. 单药适用于治疗接受\n含铂类方案治疗期间或之后\n出现疾病进展且肿瘤\nPD-L1 表达阳性（定义为表\n达 PD-L1 的肿瘤细胞≥\n1%) 的复发性或转移性头颈\n部鳞状细胞癌 (SCCHN) 患\n者；4. 用于治疗既往接受过\n两种或两种以上全身性治疗\n方案的晚期或复发性胃或胃\n食管连接部腺癌患者；5. 联\n合含氟尿嘧啶和铂类药物化\nNivolumab\n纳武利尤单\n抗\n— 21 —\n上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n奕检医学\nYIJIANMED LABORATORY\nYJ50430012T\n胞的免疫反应。活化的 PD - 1 负性调节 T\n细胞活化，在肿瘤逃\n避宿主免疫中发挥关\n键作用。\n木单抗作为一线治疗，成人中低风险晚期\n肾细胞癌患者；b. 联合卡博替尼作为一\n线治疗，成人晚期肾细胞癌患者；c. 已\n接受过抗血管生成治疗的成年晚期肾细\n胞癌患者；5. 用于经自体造血干细胞移\n植(HSCT)和贝伦妥单抗-维多汀治疗后或\n包括自体 HSCT 在内的 3 种或 3 种\n以上系统疗法治疗的复发或进展的经典\n霍奇金淋巴瘤成人患者；6. 用于既往接\n受含铂类化疗方案治疗时或治疗后疾病\n进展的复发性或转移性头颈部鳞状细胞\n癌的成人患者；7. 用于尿路上皮癌患者：\na. 根治术后复发风险高的成人患者的辅\n助治疗；b. 在含铂化疗期间或之后出现\n疾病进展或新辅助治疗或辅助治疗 12 个\n月内疾病进展的局部晚期或转移性尿路\n上皮癌的成年患者；8. 单用或与伊匹木\n单抗联用于既往接受氟尿嘧啶、奥沙利\n铂、伊立替康治疗后疾病进展的微卫星高\n度不稳定（MSI-H）或错配修复缺陷\n(dMMR) 的转移性结直肠癌成人和儿\n童患者(12 岁及以上)；9. 用于既往接受",
    "role": "user"
  }
]
2026-08-10 14:57:02,469 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:02,469 INFO     29 [qwen-vl-table] page=37 LLM output (len=40):
{
  "report_date": null,
  "items": []
}
2026-08-10 14:57:02,470 WARNING  29 [qwen-vl-table] page=37 no items extracted
2026-08-10 14:57:02,470 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:02,470 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "索拉非尼联合伊匹木单抗治疗的肝细胞\n癌成人患者；10. 用于食道癌患者：a.\n用于经新辅助放化疗（CRT）及完全手术\n切除后仍有病理学残留的食管癌或胃食\n管连接部癌的成人患者；b. 联合含氟尿\n嘧啶和含铂化疗作为一线治疗不能切除\n的晚期或转移性食管鳞状细胞癌的成人\n患者；c. 联合伊匹单抗作为一线治疗不\n可切除的晚期或转移性食管鳞状细胞癌\n成人患者；c. 用于先前以氟尿嘧啶和铂\n为基础的化疗后无法切除的晚期、复发或\n转移性食管鳞状细胞癌(ESCC)的成人患\n者；11. 联合含氟尿嘧啶和铂类药物化疗\n适用于晚期或转移性胃癌、胃食管连接部\n癌或食管腺癌成人患者。\n疗适用于一线治疗晚期或转\n移性胃癌、胃食管连接部癌\n或食管腺癌患者；6. 联合伊\n匹木单抗用于不可手术切除\n的、初治的非上皮样恶性胸\n膜间皮瘤成人患者；7. 用于\n经新辅助放化疗（CRT）及\n完全手术切除后仍有病理学\n残留的食管癌或胃食管连接\n部癌患者的辅助治疗；8. 联\n合含氟嘧啶类和铂类化疗用\n于晚期或转移性食管鳞癌患\n者的一线治疗。\n— 22 —\n上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n奕检医学\nYIJIANMED LABORATORY\nYJ50430012T\nPembrolizumab\n帕博利珠单抗\n帕博利珠单抗\n(Pembrolizumab)\n是一种针对人细胞表\n面受体 PD-1 (程序性\n死亡-1 或程序性细\n胞死亡-1) 的人源化\n单克隆免疫球蛋白\n(Ig) G4 抗体，具\n有潜在的免疫检查点\n抑制和抗肿瘤活性。\n给药后，帕博利珠单\n抗与 PD-1 结合，\nPD-1 是一种在活化\n的 T 细胞表面表达\n的抑制性信号受体，\n并阻断其配体对\nPD-1 的结合和激活，\n从而导致 T 细胞介\n导的针对肿瘤细胞的\n免疫反应的激活。\nPD-1 的配体包括在\n某些癌细胞上过表达\n的程序性细胞死亡配\n体 1 (PD-L1) 和主\n要在 APC 上表达的\n程序性细胞死亡配体\n2 (PD-L2) 。激活的\nPD-1 负向调节 T 细\n胞活化，并在肿瘤逃\n避宿主免疫中发挥关",
    "role": "user"
  }
]
2026-08-10 14:57:03,254 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:03,255 INFO     29 [qwen-vl-table] page=38 LLM output (len=48):
{
  "report_date": "2025-05-05",
  "items": []
}
2026-08-10 14:57:03,255 WARNING  29 [qwen-vl-table] page=38 no items extracted
2026-08-10 14:57:03,255 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:03,255 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "键作用。\nFDA 批准：1. 黑色素瘤：a. 用于无法切\n除或转移性黑色素瘤患者；b. 用于完全\n切除后淋巴结受累黑色素瘤患者的辅助\n治疗；2. 非小细胞肺癌： a. 联合培美曲\n塞和铂类化疗用于无 EGFR 突变或 ALK\n重排转移性非鳞状 NSCLC 患者的一线治\n疗；b. 联合卡铂+紫杉醇或白蛋白紫杉醇\n用于转移性鳞状 NSCLC 患者的一线治\n疗；c. 单药用于 PD-L1 TPS≥1% (经 FDA\n批准的检测) 且无 EGFR 突变或 ALK 重\n排的转移性非小细胞肺癌的一线治疗，不\n适合手术切除或根治性放化疗或转移的\nIII 期患者；d. 单药用于 PD-L1 TPS≥1%、\n铂类化疗期间或之后进展的转移性非小\n细胞肺癌；携带 EGFR 或 ALK 突变的患\n者在接受 FDA 批准疗法后仍出现疾病进\n展的非小细胞肺癌；e. 作为手术切除和\n铂类化疗后的辅助治疗，用于 IB 期 (T2a\n≥4 厘米) 、II 期或 IIIA 期非小细胞肺\n癌 (NSCLC) 患者；3. 小细胞肺癌：\n单药用于铂类期间或之后且既往至少一\n种其他治疗后进展的转移性小细胞肺癌\n(SCLC) 患者；4. 头颈癌：a. 联合铂类\n+5-FU 用于转移性或不可切除复发的头\n颈部鳞癌 (HNSCC) 的一线治疗；b. 单\n药用于 PD-L1 CPS≥1 (FDA 批准的检测\n方法) 的转移性或不可切除的复发性\nHNSCC 患者的一线治疗；c. 单药用于铂\n类化疗期间或之后进展的复发或转移性\n头颈部鳞癌；5. 霍奇金淋巴瘤：用于难\n治性经典霍奇金淋巴瘤 (cHL) 的成人及\n儿童患者，或经过 3 种及以上前线治疗后\n复发的 cHL 患者的单一疗法；6. 原发性\n纵隔大 B 细胞淋巴瘤 (PMBCL) ：用于\n治疗难治性成人和儿童原发性纵隔大 B\n细胞淋巴瘤 (PMBCL) 患者，或两线及\n以上治疗后复发的患者；7. 尿路上皮癌：\na. 单药用于不适合铂类为基础的化疗方\n案的 PD-L1 CPS≥10 的局部晚期或转移\n性尿路上皮癌或不论 PD-L1 状态如何，\n不适合任何含铂方案的患者；b. 单药用\n于含铂化疗期间或之后进展、或经含铂新\n辅助或辅助化疗后 12 月内疾病进展的局\n部晚期或转移性尿路上皮癌；c. 联合\nenfortumab vedotin-ejfv 治疗不符合\nNMPA 批准：1. 用于经一线\n治疗失败的不可切除或转移\n性黑色素瘤的治疗；2. 非小\n细胞肺癌：a. 用于由国家药\n品监督管理局批准的检测评\n估为 PD-L1 肿瘤比例分数\n(TPS) ≥1%的表皮生长因\n子受体 (EGFR) 基因突变阴\n性和间变性淋巴瘤激酶\n(ALK) 阴性的局部晚期或\n转移性非小细胞肺癌一线单\n药治疗；b. 联合培美曲塞和\n铂类化疗适用于表皮生长因\n子受体 (EGFR) 基因突变阴\n性和间变性淋巴瘤激酶\n(ALK) 阴性的转移性非鳞\n状非小细胞肺癌 (NSCLC)\n的一线治疗；c. 抗联合卡铂\n和紫杉醇适用于转移性鳞状",
    "role": "user"
  }
]
2026-08-10 14:57:03,794 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:03,794 INFO     29 [qwen-vl-table] page=39 LLM output (len=2):
{}
2026-08-10 14:57:03,794 WARNING  29 [qwen-vl-table] page=39 no items extracted
2026-08-10 14:57:03,794 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:03,795 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "非小细胞肺癌 (NSCLC) 患\n者的一线治疗；3. 食管癌：\na. 联合铂类和氟尿嘧啶类\n化疗药物用于局部晚期不可\n切除或转移性食管或胃食管\n结合部癌患者的一线治疗；\nb. 单药用于由国家药品监\n督管理局批准的检测评估肿\n瘤表达 PD-L1 (综合阳性评\n分 (CPS) ≥10) 的、既往\n一线全身治疗失败的、局部\n晚期或转移性食管鳞状细胞\n癌 (ESCC) 患者的治疗；4.\n单药用于通过充分验证的检\n测评估肿瘤表达 PD-L1 (综\n合阳性评分 (CPS) ≥20)\n的转移性或不可切除的复发\n性头颈部鳞状细胞癌\n(HNSCC) 患者的一线治\n疗；5. 单药用于 KRAS、\nNRAS 和 BRAF 基因均为野\n生型，不可切除或转移性微\n卫星高度不稳定型 (MSI-H)\n或错配修复基因缺陷型\n(dMMR) 结直肠癌 (CRC)\n患者的一线治疗；6. 单药用\n— 23 —\n上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n奕检医学\nYIJIANMED LABORATORY\nYJ50430012T\n含顺铂化疗条件的局部晚期或转移性尿\n路上皮癌（la/mUC）成年患者；8. 乳腺\n癌：a. 与化疗联合用于治疗局部复发的\n不可切除或转移性三阴性乳腺癌患者\n(TNBC)，其肿瘤表达 PD-L1（由 FDA\n批准的测试确定的综合阳性评分[CPS]≥\n10）；b. 联合化疗作为新辅助治疗治疗\n高危早期三阴性乳腺癌患者，然后继续作\n为手术后的单药辅助治疗；9. 胃癌：a. 单\n药用于经 2 种及以上前线治疗（包括含氟\n尿嘧啶和含铂类化疗方案）进展、PD-L1\nCPS≥1 的复发性局部晚期或转移性胃癌\n/胃食管结合部腺癌（GEJ）患者；b. 联\n合曲妥珠单抗、含氟嘧啶和含铂化疗，用\n于局部晚期不可切除或转移性 HER2 阳\n性胃癌或胃食管交界处（GEJ）腺癌患者\n的一线治疗；10. 食管癌：a. 单药用于\n经一种及以上全身治疗进展、PD-L1 CPS\n≥10 的复发性局部晚期或转移性食管鳞\n状细胞癌患者；b. 用于治疗局部晚期或\n转移性食管或胃食管交界处（GEJ）（震\n中在 GEJ 上方 1 至 5 厘米的肿瘤）癌患\n者，不适合手术切除或最终放化疗联合铂\n和氟嘧啶化疗；11. 宫颈癌：a. 单药用\n于化疗期间或之后进展、PD-L1 CPS≥1\n的复发或转移性宫颈癌患者；b. 加化疗，\n联合或不联合贝伐珠单抗，用于治疗肿瘤\n表达 PD-L1 的持续性，复发性或转移性\n宫颈癌患者（CPS ≥1）；12. 肝细胞癌\n(HCC)：单药用于索拉非尼治疗后进展\n的 HCC 患者；13. Merkel 细胞癌\n(MCC)：单药用于复发局部晚期或转\n移性 MCC 成人和儿童患者；14. 肾细胞\n癌：a. 帕博利珠单抗联合阿西替尼用于",
    "role": "user"
  }
]
2026-08-10 14:57:05,428 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:05,428 INFO     29 [qwen-vl-table] page=40 LLM output (len=2):
{}
2026-08-10 14:57:05,429 WARNING  29 [qwen-vl-table] page=40 no items extracted
2026-08-10 14:57:05,429 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:05,429 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "晚期肾细胞癌（RCC）患者的一线治疗；\nb. 联合 lenvatinib 用于晚期肾细胞癌\n(RCC) 成人患者的一线治疗；c. 用于\n肾切除术后或肾切除术和转移性病变切\n除术后复发风险为中高或高风险的 RCC\n患者的辅助治疗；15. 子宫内膜癌：联合\nlenvatinib 治疗非微卫星不稳定性高\n(MSI-H) 或错配修复缺陷 (dMMR)\n的晚期子宫内膜癌患者，他们在既往全身\n治疗后有疾病进展，不适合根治性手术或\n放疗；16. 膀胱癌：作为单药治疗卡介苗\n于既往接受过索拉非尼或含\n奥沙利铂化疗的肝细胞癌\n(HCC) 患者的治疗；7. 联\n合吉西他滨和顺铂用于局部\n晚期或转移性胆道癌 (BTC)\n患者的一线治疗；8. 联合化\n疗新辅助治疗并在手术后继\n续帕博利珠单抗单药辅助治\n疗，用于经充分验证的检测\n评估肿瘤表达 PD-L1（综合\n阳性评分（CPS）≥20）的\n早期高危三阴性乳腺癌\n(TNBC) 患者的治疗；9. 抗\n单药用于不可切除或转移性\n微卫星高度不稳定型\n(MSI-H) 或错配修复基因\n缺陷型 (dMMR) 成人晚期\n实体瘤患者：a. 既往接受过\n氟尿嘧啶类、奥沙利铂和伊\n立替康治疗后疾病进展的结\n直肠癌患者；b. 既往治疗后\n疾病进展且无满意替代治疗\n方案的其他实体瘤；10. 联\n合含氟尿嘧啶类和铂类药物\n化疗用于局部晚期不可切除\n或转移性 HER2-阴性胃或胃\n食管结合部腺癌患者的一线\n治疗。\n— 24 —\n上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n奕检医学\nYIJIANMED LABORATORY\nYJ50430012T\n(BCG) 无反应、高风险、非肌肉浸润性\n膀胱癌 (NMIBC) 合并原位癌 (CIS) 伴\n或不伴乳头状肿瘤且不适合或选择不接\n受膀胱切除术的患者；17. 皮肤鳞状细胞\n癌：作为单药用于治疗无法通过手术或放\n疗治愈的复发性或转移性皮肤鳞状细胞\n癌 (cSCC) 患者；18. 用于治疗成人和\n儿童患者不可切除或转移性肿瘤突变负\n荷高 (TMB-H) [≥10 个突变/兆碱基\n(mut/Mb)] 实体瘤；19. 单药用于治\n疗无法切除或转移性的 MSI-H 或错配修\n复缺陷 (dMMR) 的成人和儿童患者，实\n体肿瘤经先前治疗进展、并且没有令人满\n意的替代治疗方案的实体瘤患者，氟尿嘧\n啶，奥沙利铂和伊立替康治疗后进展的结\n直肠癌，用于不可切除或转移性 MSI-H\n或 dMMR 结直肠癌患者的一线治疗（帕\n博利珠单抗 MSI-H 中枢神经系统肿瘤的\n儿童患者中的安全性和有效性尚未确定）；\n20. 用于治疗成人和儿童患者不可切除\n或转移性微卫星不稳定性高 (MSI-H) 或",
    "role": "user"
  }
]
2026-08-10 14:57:06,149 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:06,150 INFO     29 [qwen-vl-table] page=41 LLM output (len=2):
{}
2026-08-10 14:57:06,150 WARNING  29 [qwen-vl-table] page=41 no items extracted
2026-08-10 14:57:06,150 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:06,151 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "错配修复缺陷 (dMMR) 实体瘤。\nRamucirumab\n雷莫西尤单抗\n雷莫西尤单抗\n(Ramucirumab) 是\nVEGFR-2 拮抗剂。\nNCCN 指南推荐雷莫\n西尤单抗作为单药或\n联合紫杉醇作为晚期\n或转移性胃腺癌患者\n二线或后续治疗的选\n择。转移性结直肠癌\n经贝伐珠单抗联合奥\n沙利铂和 5-Fu 一线治\n疗失败后，二线雷莫\n西尤单抗联合\nFOLFIRI 方案可以提\n供一定的临床获益。\nFDA 批准：1. 作为单药或与紫杉醇联合\n用于治疗铂或氟嘧啶一线化疗难治或进\n展的晚期胃癌或 EGJ 腺癌患者；2. 作为\n单药治疗甲胎蛋白 (AFP) ≥400 ng/mL\n且既往接受过索拉非尼治疗的肝细胞癌\n(HCC) 患者；3. 与厄洛替尼联合用于\n表皮生长因子受体 (EGFR) 19 号外显子\n缺失或 21 号外显子突变 (L858R) 的转\n移性非小细胞肺癌 (NSCLC) 的一线治\n疗。4. 联合多西他赛，用于治疗铂类化\n疗上或化疗后疾病进展的转移性非小细\n胞肺癌。对于 EGFR 或 ALK 基因异常的\n患者，在接受 CYRAMZA 治疗之前，FDA\n批准的针对 EGFR 或 ALK 基因异常的治\n疗应该有疾病进展。5. 与 FOLFIRI 联合，\n用于治疗在贝伐单抗、奥沙利铂和氟嘧啶\n治疗期间或之后疾病进展的转移性结直\n肠癌。\nNMPA 批准：1. 与紫杉醇\n联合用于在含氟尿嘧啶类或\n含铂类化疗期间或化疗后出\n现疾病进展的晚期胃或胃食\n管结合部腺癌患者的治疗；\n2. 用于既往接受过索拉非\n尼治疗且甲胎蛋白 (AFP) ≥\n400 ng/mL 的肝细胞癌\n(HCC) 患者的治疗。\n— 25 —\n上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n奕检医学\nYIJIANMED LABORATORY\nYJ50430012T\nDostarlimab-gxly\nDostarlimab-gxly 是\n一种针对阴性免疫调\n节性人细胞表面受体\n程序性细胞死亡 1\n(PD-1;程序性死亡\n-1) 的人源化单克隆\n抗体，具有潜在的免\n疫检查点抑制和抗肿\n瘤活性。给药后，\ndostarlimab 结合并\n抑制 PD-1 及其下游\n信号通路。这可能通\n过激活 T 细胞来恢\n复免疫功能。PD-1 是",
    "role": "user"
  }
]
2026-08-10 14:57:06,950 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:06,950 INFO     29 [qwen-vl-table] page=42 LLM output (len=48):
{
  "report_date": "2025-05-05",
  "items": []
}
2026-08-10 14:57:06,950 WARNING  29 [qwen-vl-table] page=42 no items extracted
2026-08-10 14:57:06,950 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:06,950 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 539, \"bbox_end\": 2310, \"encounter_dates\": [\"2025-05-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "一种在 T 细胞上表\n达的 Ig 超家族中的\n跨膜蛋白，当被其配\n体程序性细胞死亡受\n体配体 1 （PD-L1）\n或 2（PD-L2）激活\n时，它作为免疫检查\n点蛋白发挥作用，负\n向调节 T 细胞活化\n和 T 细胞介导的免\n疫反应；它在肿瘤逃\n避宿主免疫中起重要\n作用。\nFDA 批准：1. 用于治疗复发或晚期错配\n修复缺陷(dMMR)的成年患者：a. 经\nFDA 批准的试验确定的子宫内膜癌，在\n接受含铂方案治疗后或在接受含铂方案\n治疗后进展，不适合进行治疗性手术或放\n疗；b. 经 FDA 批准的试验确定的实体肿\n瘤，在之前的治疗中或之后已经进展，并\n且没有令人满意的替代治疗方案；2. 与\n卡铂和紫杉醇联合使用，随后作为单一药\n物用于治疗原发性晚期或复发性子宫内\n膜癌成年患者。\n无\nZiv-aflibercept\nZiv-aflibercept 是一\n种重组蛋白。\nAfilbercept 作为可\n溶性诱饵受体，与促\n血管生成血管内皮生\n长因子 （VEGF） 结\n合，从而阻止 VEGF\n与其内源性受体结\n合。破坏 VEGF 与其\n细胞受体的结合可能\n导致肿瘤血管生成、\n转移和最终肿瘤消退\n的抑制。\nFDA 批准：ziv-afliberept 与氟尿嘧啶,\n亚叶酸钙，伊立替康（FOLFIRI）联合使\n用，用于治疗奥沙利铂治疗方案耐药或进\n展的转移性结直肠癌（mCRC）患者。\n无\n— 26 —\n上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com\n奕检医学\nYIJIANMED LABORATORY\nYJ50430012T\n参考文献\n临床指南与共识\n1) NCCN Guideline: Colon Cancer (Version: 5.2024).\n2) NCCN Guideline: Rectal Cancer (Version: 4.2024).\n3) A framework to rank genomic alterations as targets for cancer precision medicine: the ESMO Scale\nfor Clinical Actionability of molecular Targets (ESCAT). PMID: 30137196.\n4) Recommendations for the use of next-generation sequencing (NGS) for patients with advanced\ncancer in 2024: a report from the ESMO Precision Medicine Working Group. PMID: 38834388.\n5) A Canadian guideline on the use of next-generation sequencing in oncology. Curr Oncol. PMID:\n31043833.\n6) Therapeutic landscape and future direction of metastatic colorectal cancer. PMID: 36670267.\n7) Targeting BRAF and RAS in Colorectal Cancer. PMID: 34063682.\n8) BRAF and KRAS mutations in metastatic colorectal cancer: future perspectives for personalized\ntherapy. PMID: 32665851.\n9) RAS genes in colorectal carcinoma: pathogenesis, testing guidelines and treatment implications.\nPMID: 30425122.\n10) BRAF Mutated Colorectal Cancer: New Treatment Approaches. PMID: 32545884.\n11) Exploring the best treatment options for BRAF-mutant metastatic colon cancer. PMID: 31353365.\n12) Mismatch repair deficiency testing in colorectal cancer and factors associated with nonadherence\nto guidelines. https://doi.org/10.1200/JCO.2020.38.15_suppl.e16069.\n13) Molecular and clinical characteristics of POLE/POLD1 alterations among patients with colorectal\ncancer. https://doi.org/10.1200/JCO.2024.42.3_suppl.184.\n14) 中国临床肿瘤学会 (CSCO) 结直肠癌诊疗指南 2024.\n15) 中国临床肿瘤学会 (CSCO) 免疫检查点抑制剂临床应用指南 2024.\n16) 中国临床肿瘤学会 (CSCO) 免疫检查点抑制剂相关的毒性管理指南 2023.\n17) 《肿瘤二代测序临床报告解读共识》, 循证医学 2022 年第 22 卷第 2 期.\n18) 《ctDNA 高通量测序临床实践专家共识 (2022 年版)》, 中国癌症防治杂志 2022 年 6 月第 14 卷第 3 期.\n19) 《二代测序技术在肿瘤精准医学诊断中的应用专家共识 (2018)》,中华医学杂志 2018 年 7 月 10 日第 98\n卷第 26 期.\n20) 《结直肠癌分子标志物临床检测中国专家共识》, 中华胃肠外科杂志 2021 年 3 月第 24 卷第 3 期.\n21) 《结直肠癌分子检测高通量测序中国专家共识》, 临床肿瘤学杂志 2021 年 3 月第 26 卷第 3 期.\n— 27 —\n上海奕检医学检验实验室 上海市嘉定区南翔镇惠平路801号4幢1层 电话：400-004-2111 网址：www.yjmedlab.com",
    "role": "user"
  }
]
2026-08-10 14:57:07,795 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:07,795 INFO     29 [qwen-vl-table] page=43 LLM output (len=2):
{}
2026-08-10 14:57:07,795 WARNING  29 [qwen-vl-table] page=43 no items extracted
2026-08-10 14:57:07,796 INFO     29 [qwen-vl-table] coord grouping: {17: 6, 20: 1, 19: 2, 25: 5, 27: 5, 29: 4, 24: 8, 30: 4, 22: 9, 23: 5}
2026-08-10 14:57:07,797 INFO     29 [qwen-vl-table] coord API call start, page=17, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=174995, prompt_len=604
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
体细胞突变、融合变异、微卫星不稳定状态（MSI）、KRAS 2号外显子、KRAS 2号外显子 c.34G>A p.G12S、APC 16号外显子 c.4257_4263del p.S1419fs

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
2026-08-10 14:57:08,874 INFO     29 [qwen-vl-table] coord API raw response (len=2):
[]
2026-08-10 14:57:08,874 INFO     29 [qwen-vl-table] coord API: raw_items=0, valid_items=0, elapsed=1.1s
2026-08-10 14:57:08,875 WARNING  29 [qwen-vl-table] page=17 coord failed: ok
2026-08-10 14:57:08,876 INFO     29 [qwen-vl-table] coord API call start, page=20, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=271979, prompt_len=512
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
拷贝数变异

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
2026-08-10 14:57:10,211 INFO     29 [qwen-vl-table] coord API raw response (len=64):
```json
[
	{"text": "拷贝数变异", "bbox": [723, 271, 812, 287]}
]
```
2026-08-10 14:57:10,211 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=1.3s
2026-08-10 14:57:10,212 INFO     29 [qwen-vl-table] coord item[0]: text=拷贝数变异, bbox=[723, 271, 812, 287]
2026-08-10 14:57:10,212 INFO     29 [qwen-vl-table] page=20 coord: matched 1/1, time=1.3s
2026-08-10 14:57:10,213 INFO     29 [qwen-vl-table] coord API call start, page=19, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=375289, prompt_len=535
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
错配修复基因胚系突变（MMR）、微卫星不稳定性（MSI）

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
2026-08-10 14:57:11,824 INFO     29 [qwen-vl-table] coord API raw response (len=119):
[
	{"text": "错配修复基因胚系突变（MMR）", "bbox": [100, 717, 388, 735]},
	{"text": "微卫星不稳定性（MSI）", "bbox": [100, 501, 363, 519]}
]
2026-08-10 14:57:11,825 INFO     29 [qwen-vl-table] coord API: raw_items=2, valid_items=2, elapsed=1.6s
2026-08-10 14:57:11,825 INFO     29 [qwen-vl-table] coord item[0]: text=错配修复基因胚系突变（MMR）, bbox=[100, 717, 388, 735]
2026-08-10 14:57:11,825 INFO     29 [qwen-vl-table] coord item[1]: text=微卫星不稳定性（MSI）, bbox=[100, 501, 363, 519]
2026-08-10 14:57:11,825 INFO     29 [qwen-vl-table] page=19 coord: matched 2/2, time=1.6s
2026-08-10 14:57:11,829 INFO     29 [qwen-vl-table] coord API call start, page=25, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=776814, prompt_len=532
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
MYC、KRAS、MYC、KRAS、MYC 拷贝数

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
2026-08-10 14:57:14,105 INFO     29 [qwen-vl-table] coord API raw response (len=260):
```json
[
	{"text": "MYC", "bbox": [131, 803, 165, 816]},
	{"text": "KRAS", "bbox": [129, 294, 167, 306]},
	{"text": "MYC", "bbox": [231, 785, 260, 797]},
	{"text": "KRAS", "bbox": [231, 166, 260, 178]},
	{"text": "MYC 拷贝数", "bbox": [110, 822, 186, 835]}
]
```
2026-08-10 14:57:14,105 INFO     29 [qwen-vl-table] coord API: raw_items=5, valid_items=5, elapsed=2.3s
2026-08-10 14:57:14,105 INFO     29 [qwen-vl-table] coord item[0]: text=MYC, bbox=[131, 803, 165, 816]
2026-08-10 14:57:14,105 INFO     29 [qwen-vl-table] coord item[1]: text=KRAS, bbox=[129, 294, 167, 306]
2026-08-10 14:57:14,105 INFO     29 [qwen-vl-table] coord item[2]: text=MYC, bbox=[231, 785, 260, 797]
2026-08-10 14:57:14,106 INFO     29 [qwen-vl-table] coord item[3]: text=KRAS, bbox=[231, 166, 260, 178]
2026-08-10 14:57:14,106 INFO     29 [qwen-vl-table] coord item[4]: text=MYC 拷贝数, bbox=[110, 822, 186, 835]
2026-08-10 14:57:14,106 INFO     29 [qwen-vl-table] page=25 coord: matched 5/5, time=2.3s
2026-08-10 14:57:14,108 INFO     29 [qwen-vl-table] coord API call start, page=27, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=828038, prompt_len=531
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
BRAF、APC、BRAF、EGFR、ERBB2

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
2026-08-10 14:57:16,381 INFO     29 [qwen-vl-table] coord API raw response (len=259):
```json
[
	{"text": "BRAF", "bbox": [115, 432, 154, 445]},
	{"text": "APC", "bbox": [118, 257, 150, 269]},
	{"text": "BRAF", "bbox": [115, 432, 154, 445]},
	{"text": "EGFR", "bbox": [115, 560, 154, 573]},
	{"text": "ERBB2", "bbox": [111, 762, 157, 775]}
]
```
2026-08-10 14:57:16,381 INFO     29 [qwen-vl-table] coord API: raw_items=5, valid_items=5, elapsed=2.3s
2026-08-10 14:57:16,381 INFO     29 [qwen-vl-table] coord item[0]: text=BRAF, bbox=[115, 432, 154, 445]
2026-08-10 14:57:16,381 INFO     29 [qwen-vl-table] coord item[1]: text=APC, bbox=[118, 257, 150, 269]
2026-08-10 14:57:16,382 INFO     29 [qwen-vl-table] coord item[2]: text=BRAF, bbox=[115, 432, 154, 445]
2026-08-10 14:57:16,382 INFO     29 [qwen-vl-table] coord item[3]: text=EGFR, bbox=[115, 560, 154, 573]
2026-08-10 14:57:16,382 INFO     29 [qwen-vl-table] coord item[4]: text=ERBB2, bbox=[111, 762, 157, 775]
2026-08-10 14:57:16,382 INFO     29 [qwen-vl-table] page=27 coord: matched 5/5, time=2.3s
2026-08-10 14:57:16,386 INFO     29 [qwen-vl-table] coord API call start, page=29, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=885957, prompt_len=526
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
NRAS、MLH1、MSH2、MSH6

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
2026-08-10 14:57:18,512 INFO     29 [qwen-vl-table] coord API raw response (len=210):
```json
[
	{"text": "NRAS", "bbox": [113, 851, 155, 864]},
	{"text": "MLH1", "bbox": [113, 483, 155, 496]},
	{"text": "MSH2", "bbox": [113, 630, 155, 643]},
	{"text": "MSH6", "bbox": [113, 758, 155, 771]}
]
```
2026-08-10 14:57:18,513 INFO     29 [qwen-vl-table] coord API: raw_items=4, valid_items=4, elapsed=2.1s
2026-08-10 14:57:18,513 INFO     29 [qwen-vl-table] coord item[0]: text=NRAS, bbox=[113, 851, 155, 864]
2026-08-10 14:57:18,513 INFO     29 [qwen-vl-table] coord item[1]: text=MLH1, bbox=[113, 483, 155, 496]
2026-08-10 14:57:18,513 INFO     29 [qwen-vl-table] coord item[2]: text=MSH2, bbox=[113, 630, 155, 643]
2026-08-10 14:57:18,513 INFO     29 [qwen-vl-table] coord item[3]: text=MSH6, bbox=[113, 758, 155, 771]
2026-08-10 14:57:18,514 INFO     29 [qwen-vl-table] page=29 coord: matched 4/4, time=2.1s
2026-08-10 14:57:18,515 INFO     29 [qwen-vl-table] coord API call start, page=24, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=414384, prompt_len=551
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
EPCAM、FGFR1、FGFR2、FGFR3、MDM2、RET、NTRK3、NTRK2

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
2026-08-10 14:57:21,545 INFO     29 [qwen-vl-table] coord API raw response (len=411):
```json
[
	{"text": "EPCAM", "bbox": [267, 238, 321, 251]},
	{"text": "FGFR1", "bbox": [270, 329, 316, 342]},
	{"text": "FGFR2", "bbox": [270, 360, 318, 372]},
	{"text": "FGFR3", "bbox": [410, 177, 457, 189]},
	{"text": "MDM2", "bbox": [407, 329, 458, 342]},
	{"text": "RET", "bbox": [835, 208, 862, 220]},
	{"text": "NTRK3", "bbox": [687, 238, 735, 251]},
	{"text": "NTRK2", "bbox": [687, 208, 735, 220]}
]
```
2026-08-10 14:57:21,545 INFO     29 [qwen-vl-table] coord API: raw_items=8, valid_items=8, elapsed=3.0s
2026-08-10 14:57:21,545 INFO     29 [qwen-vl-table] coord item[0]: text=EPCAM, bbox=[267, 238, 321, 251]
2026-08-10 14:57:21,546 INFO     29 [qwen-vl-table] coord item[1]: text=FGFR1, bbox=[270, 329, 316, 342]
2026-08-10 14:57:21,546 INFO     29 [qwen-vl-table] coord item[2]: text=FGFR2, bbox=[270, 360, 318, 372]
2026-08-10 14:57:21,546 INFO     29 [qwen-vl-table] coord item[3]: text=FGFR3, bbox=[410, 177, 457, 189]
2026-08-10 14:57:21,546 INFO     29 [qwen-vl-table] coord item[4]: text=MDM2, bbox=[407, 329, 458, 342]
2026-08-10 14:57:21,546 INFO     29 [qwen-vl-table] coord item[5]: text=RET, bbox=[835, 208, 862, 220]
2026-08-10 14:57:21,546 INFO     29 [qwen-vl-table] coord item[6]: text=NTRK3, bbox=[687, 238, 735, 251]
2026-08-10 14:57:21,546 INFO     29 [qwen-vl-table] coord item[7]: text=NTRK2, bbox=[687, 208, 735, 220]
2026-08-10 14:57:21,546 INFO     29 [qwen-vl-table] page=24 coord: matched 8/8, time=3.0s
2026-08-10 14:57:21,547 INFO     29 [qwen-vl-table] coord API call start, page=30, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=876553, prompt_len=530
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
PMS2、NTRK1、PIK3CA、NTRK1

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
2026-08-10 14:57:23,738 INFO     29 [qwen-vl-table] coord API raw response (len=214):
```json
[
	{"text": "PMS2", "bbox": [113, 730, 155, 744]},
	{"text": "NTRK1", "bbox": [109, 364, 157, 377]},
	{"text": "PIK3CA", "bbox": [107, 593, 161, 606]},
	{"text": "NTRK1", "bbox": [109, 364, 157, 377]}
]
```
2026-08-10 14:57:23,738 INFO     29 [qwen-vl-table] coord API: raw_items=4, valid_items=4, elapsed=2.2s
2026-08-10 14:57:23,738 INFO     29 [qwen-vl-table] coord item[0]: text=PMS2, bbox=[113, 730, 155, 744]
2026-08-10 14:57:23,738 INFO     29 [qwen-vl-table] coord item[1]: text=NTRK1, bbox=[109, 364, 157, 377]
2026-08-10 14:57:23,738 INFO     29 [qwen-vl-table] coord item[2]: text=PIK3CA, bbox=[107, 593, 161, 606]
2026-08-10 14:57:23,738 INFO     29 [qwen-vl-table] coord item[3]: text=NTRK1, bbox=[109, 364, 157, 377]
2026-08-10 14:57:23,738 INFO     29 [qwen-vl-table] page=30 coord: matched 4/4, time=2.2s
2026-08-10 14:57:23,739 INFO     29 [qwen-vl-table] coord API call start, page=22, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=349650, prompt_len=557
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
紫杉醇类、伊立替康、伊立替康、5-氟尿嘧啶、5-氟尿嘧啶、5-氟尿嘧啶、卡培他滨、卡培他滨、甲氨蝶呤

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
2026-08-10 14:57:26,968 INFO     29 [qwen-vl-table] coord API raw response (len=449):
[
	{"text": "紫杉醇类", "bbox": [133, 371, 194, 384]},
	{"text": "伊立替康", "bbox": [133, 402, 194, 415]},
	{"text": "伊立替康", "bbox": [255, 402, 314, 415]},
	{"text": "5-氟尿嘧啶", "bbox": [125, 453, 202, 466]},
	{"text": "5-氟尿嘧啶", "bbox": [264, 453, 305, 466]},
	{"text": "5-氟尿嘧啶", "bbox": [350, 453, 436, 466]},
	{"text": "卡培他滨", "bbox": [134, 504, 194, 517]},
	{"text": "卡培他滨", "bbox": [264, 504, 305, 517]},
	{"text": "甲氨蝶呤", "bbox": [133, 535, 194, 548]}
]
2026-08-10 14:57:26,968 INFO     29 [qwen-vl-table] coord API: raw_items=9, valid_items=9, elapsed=3.2s
2026-08-10 14:57:26,968 INFO     29 [qwen-vl-table] coord item[0]: text=紫杉醇类, bbox=[133, 371, 194, 384]
2026-08-10 14:57:26,969 INFO     29 [qwen-vl-table] coord item[1]: text=伊立替康, bbox=[133, 402, 194, 415]
2026-08-10 14:57:26,969 INFO     29 [qwen-vl-table] coord item[2]: text=伊立替康, bbox=[255, 402, 314, 415]
2026-08-10 14:57:26,969 INFO     29 [qwen-vl-table] coord item[3]: text=5-氟尿嘧啶, bbox=[125, 453, 202, 466]
2026-08-10 14:57:26,969 INFO     29 [qwen-vl-table] coord item[4]: text=5-氟尿嘧啶, bbox=[264, 453, 305, 466]
2026-08-10 14:57:26,969 INFO     29 [qwen-vl-table] coord item[5]: text=5-氟尿嘧啶, bbox=[350, 453, 436, 466]
2026-08-10 14:57:26,969 INFO     29 [qwen-vl-table] coord item[6]: text=卡培他滨, bbox=[134, 504, 194, 517]
2026-08-10 14:57:26,969 INFO     29 [qwen-vl-table] coord item[7]: text=卡培他滨, bbox=[264, 504, 305, 517]
2026-08-10 14:57:26,969 INFO     29 [qwen-vl-table] coord item[8]: text=甲氨蝶呤, bbox=[133, 535, 194, 548]
2026-08-10 14:57:26,969 INFO     29 [qwen-vl-table] page=22 coord: matched 9/9, time=3.2s
2026-08-10 14:57:26,969 INFO     29 [qwen-vl-table] coord API call start, page=23, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=309213, prompt_len=529
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
样本量、预文库、靶向捕获、测序质量、测序深度

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
2026-08-10 14:57:29,210 INFO     29 [qwen-vl-table] coord API raw response (len=257):
```json
[
	{"text": "样本量", "bbox": [156, 167, 202, 180]},
	{"text": "预文库", "bbox": [156, 194, 202, 206]},
	{"text": "靶向捕获", "bbox": [150, 221, 210, 234]},
	{"text": "测序质量", "bbox": [150, 249, 210, 261]},
	{"text": "测序深度", "bbox": [150, 276, 210, 289]}
]
```
2026-08-10 14:57:29,211 INFO     29 [qwen-vl-table] coord API: raw_items=5, valid_items=5, elapsed=2.2s
2026-08-10 14:57:29,211 INFO     29 [qwen-vl-table] coord item[0]: text=样本量, bbox=[156, 167, 202, 180]
2026-08-10 14:57:29,211 INFO     29 [qwen-vl-table] coord item[1]: text=预文库, bbox=[156, 194, 202, 206]
2026-08-10 14:57:29,211 INFO     29 [qwen-vl-table] coord item[2]: text=靶向捕获, bbox=[150, 221, 210, 234]
2026-08-10 14:57:29,211 INFO     29 [qwen-vl-table] coord item[3]: text=测序质量, bbox=[150, 249, 210, 261]
2026-08-10 14:57:29,211 INFO     29 [qwen-vl-table] coord item[4]: text=测序深度, bbox=[150, 276, 210, 289]
2026-08-10 14:57:29,211 INFO     29 [qwen-vl-table] page=23 coord: matched 5/5, time=2.2s
2026-08-10 14:57:29,212 INFO     29 [qwen-vl-table] new_positions (49):
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [21, 430.185, 483.14, 228.182, 241.654], [20, 59.5, 230.85999999999999, 603.7139999999999, 618.87], [20, 59.5, 215.98499999999999, 421.842, 436.998], [26, 137.445, 154.7, 660.97, 671.074], [26, 137.445, 154.7, 139.772, 149.876], [26, 137.445, 154.7, 660.97, 671.074], [26, 137.445, 154.7, 139.772, 149.876], [26, 65.45, 110.67, 692.124, 703.0699999999999], [28, 68.425, 91.63, 363.74399999999997, 374.69], [28, 70.21, 89.25, 216.394, 226.498], [28, 68.425, 91.63, 363.74399999999997, 374.69], [28, 68.425, 91.63, 471.52, 482.466], [28, 66.045, 93.41499999999999, 641.6039999999999, 652.55], [30, 67.235, 92.225, 716.542, 727.4879999999999], [30, 67.235, 92.225, 406.686, 417.632], [30, 67.235, 92.225, 530.46, 541.406], [30, 67.235, 92.225, 638.236, 649.182], [25, 158.86499999999998, 190.995, 200.396, 211.34199999999998], [25, 160.65, 188.01999999999998, 277.018, 287.964], [25, 160.65, 189.20999999999998, 303.12, 313.224], [25, 243.95, 271.91499999999996, 149.034, 159.138], [25, 242.165, 272.51, 277.018, 287.964], [25, 496.825, 512.89, 175.136, 185.23999999999998], [25, 408.765, 437.325, 200.396, 211.34199999999998], [25, 408.765, 437.325, 175.136, 185.23999999999998], [31, 67.235, 92.225, 614.66, 626.448], [31, 64.855, 93.41499999999999, 306.488, 317.43399999999997], [31, 63.665, 95.795, 499.306, 510.252], [31, 64.855, 93.41499999999999, 306.488, 317.43399999999997], [23, 79.13499999999999, 115.42999999999999, 312.382, 323.328], [23, 151.725, 186.82999999999998, 338.484, 349.43], [23, 151.725, 186.82999999999998, 338.484, 349.43], [23, 208.25, 259.42, 381.426, 392.372], [23, 208.25, 259.42, 381.426, 392.372], [23, 208.25, 259.42, 381.426, 392.372], [23, 157.07999999999998, 181.475, 424.368, 435.31399999999996], [23, 157.07999999999998, 181.475, 424.368, 435.31399999999996], [23, 79.13499999999999, 115.42999999999999, 450.46999999999997, 461.416], [24, 92.82, 120.19, 140.614, 151.56], [24, 92.82, 120.19, 163.34799999999998, 173.452], [24, 89.25, 124.94999999999999, 186.082, 197.028], [24, 89.25, 124.94999999999999, 209.658, 219.762], [24, 89.25, 124.94999999999999, 232.392, 243.338]]
2026-08-10 14:57:29,212 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=49, matched=43, pages=27, time=71.5s
2026-08-10 14:57:29,231 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 14:57:29,232 INFO     29 [Trace] task=7630dbd0 | doc=YXHU  62  男  直肠癌肺转移  贵州(2).pdf | Extractor:LabExam | outputs={"chunks": "6 items, types={'LabReport': 6}", "html": "", "json": "2311 items", "markdown": "", "text": "", "name": "YXHU  62  男  直肠癌肺转移  贵州(2).pdf", "output_format": "chunks", "chunks_Examination": "8 items, types={'ExaminationReport': 8}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_LabExam": "6 items, types={'LabReport': 6}", "route_summary": "{\"chunks_Examination\": 8, \"chunks_Discharge\": 2, \"chunks_LabExam\": 6}"}
2026-08-10 14:57:29,232 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 14:57:29,233 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:57:29.232+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 64, "failed": 0, "current": {"7630dbd094ca11f1bd9827cf206dfa2d": {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:57:29,239 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:29,240 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 14:57:30,023 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:30,034 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 14:57:30,035 INFO     29 [Trace] task=7630dbd0 | doc=YXHU  62  男  直肠癌肺转移  贵州(2).pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "2311 items", "markdown": "", "text": "", "name": "YXHU  62  男  直肠癌肺转移  贵州(2).pdf", "output_format": "chunks", "chunks_Examination": "8 items, types={'ExaminationReport': 8}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_LabExam": "6 items, types={'LabReport': 6}", "route_summary": "{\"chunks_Examination\": 8, \"chunks_Discharge\": 2, \"chunks_LabExam\": 6}"}
2026-08-10 14:57:30,035 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 14:57:30,042 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:30,043 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 14:57:30,588 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:30,600 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 14:57:30,600 INFO     29 [Trace] task=7630dbd0 | doc=YXHU  62  男  直肠癌肺转移  贵州(2).pdf | Extractor:Clinical | outputs={"chunks": "1 items", "html": "", "json": "2311 items", "markdown": "", "text": "", "name": "YXHU  62  男  直肠癌肺转移  贵州(2).pdf", "output_format": "chunks", "chunks_Examination": "8 items, types={'ExaminationReport': 8}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_LabExam": "6 items, types={'LabReport': 6}", "route_summary": "{\"chunks_Examination\": 8, \"chunks_Discharge\": 2, \"chunks_LabExam\": 6}"}
2026-08-10 14:57:30,600 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 14:57:30,611 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:30,611 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 14:57:31,295 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:31,303 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 14:57:31,304 INFO     29 [Trace] task=7630dbd0 | doc=YXHU  62  男  直肠癌肺转移  贵州(2).pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "2311 items", "markdown": "", "text": "", "name": "YXHU  62  男  直肠癌肺转移  贵州(2).pdf", "output_format": "chunks", "chunks_Examination": "8 items, types={'ExaminationReport': 8}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_LabExam": "6 items, types={'LabReport': 6}", "route_summary": "{\"chunks_Examination\": 8, \"chunks_Discharge\": 2, \"chunks_LabExam\": 6}"}
2026-08-10 14:57:31,304 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 14:57:31,310 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:31,310 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 14:57:31,729 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:31,734 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 14:57:31,735 INFO     29 [Trace] task=7630dbd0 | doc=YXHU  62  男  直肠癌肺转移  贵州(2).pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "2311 items", "markdown": "", "text": "", "name": "YXHU  62  男  直肠癌肺转移  贵州(2).pdf", "output_format": "chunks", "chunks_Examination": "8 items, types={'ExaminationReport': 8}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_LabExam": "6 items, types={'LabReport': 6}", "route_summary": "{\"chunks_Examination\": 8, \"chunks_Discharge\": 2, \"chunks_LabExam\": 6}"}
2026-08-10 14:57:31,735 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 14:57:31,742 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 14:57:31,743 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 14:57:31,743 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 14:57:31,743 INFO     29 [qwen-vl-text] positions(99): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 14:57:31,743 INFO     29 [qwen-vl-text] page grouping: [8, 9, 10], lines per page: [40, 33, 26]
2026-08-10 14:57:31,889 INFO     29 [qwen-vl-text] page=8, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 14:57:32,049 INFO     29 [qwen-vl-text] page=9, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 14:57:32,178 INFO     29 [qwen-vl-text] page=10, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 14:57:32,178 INFO     29 [qwen-vl-text] LLM extraction start, text_len=3065
2026-08-10 14:57:32,178 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:32,178 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 232, \"bbox_end\": 330, \"encounter_dates\": [\"2026-02-05\", \"2026-02-26\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "出院记录\n姓名：\n科室：\n住院号：\n姓名：\n职业：自由职业\n性别：男\n入院日期：2026-2-5 10:14\n年龄：63岁\n出院日期：2026-2-26 10:25\n民族：汉族\n住院天数：21天\n籍贯：\n科 室：\n入院情况：\n患者男，63岁，因“诊断直肠癌肺转移7+月”入院；既往史：4+年前因“大便不成形伴血\n便”就诊于外院，考虑为“直肠癌”，未明确诊断，自行服用中药治疗；10+月前因“阴囊脓肿”于\n我院局麻下行“阴囊下部脓肿切开引流术”，病理结果回示：“阴囊内容物”检材大部分为变性坏\n死组织，区域见大量中性粒细胞浸润。予换药、抗感染等对症治疗后好转。专科情况：全身皮肤粘\n膜无黄染、出血点及瘀斑，全身浅表淋巴结未扪及肿大，胸廓对称无畸形，肋间隙无明显增宽及凹\n陷，胸骨无压痛，双肺叩诊呈清音，双肺呼吸音粗，双肺可闻及散在湿啰音。腹平软，全腹未见腹\n部静脉曲张、蜘蛛痣，未见胃肠型蠕动波。全腹无压痛、反跳痛及肌紧张，肝脾肋下未扪及，莫菲\n氏征阴性，移动性浊音阴性，双肾区无叩击痛，肠鸣音约4次/分，阴囊及肛周皮肤正常，未见红\n肿、破溃，肛周6点钟方向可扪及一约2*3cm大小包块，质韧，挤压时无明显脓液，肛门括约肌张力\n正常，于直肠距肛门约7cm处可扪及环状肿物，质地硬，表面凹凸不平，活动度差，退出指套可见血\n染。（患者取左侧卧位）辅助检查：病理（病理号：2502456）：“左肺占位”恶性肿瘤，符合腺\n癌，结合免疫组化结果及临床病史考虑肠道来源。ALK（-）、CD56（-）、CDX-2（+）、CK20\n(+）、CK5/6（-）、CK7（局灶弱+）、Ki-67（30%+）、Napsin-A（-）、P40(-)、P53（突变\n型）、P63(-)、SATB2(+)、Syn（-）、TTF-1（+）、CK(AE1/AE3)（+）、Vimentin（-）、Villin\n(+）。基因检测：1.KRAS基因突变；2.MYC基因扩增；3.APC基因突变。胸部CT（本院 2026-01-\n08）：1.肺气肿伴双肺多发肺大疱；2.左肺上叶舌段结节及肿块，具恶性征象，较前增大；3.左肺上\n叶及双肺下叶实性结节，右肺中叶实性结节较前未见确切显示，右肺上叶钙化灶；4.新增双肺下叶\n坠积效应；5.新增气管黏液栓；6.贫血征象，主动脉粥样硬化；7.胸椎退行性变；8.PICC管较前未\n见确切显示。全腹+盆腔增强CT（本院 2026-01-08）：1.直肠下段病变，Ca可能，较前进展，周围\n多发淋巴结，较前稍增多、增大；2.肝内多发囊肿；3.双肾周多发渗出，较前已吸收；4.双肾多发\n囊肿；5.考虑升结肠、盲肠炎伴周围炎性渗出，较前已吸收；6.前列腺钙化灶；7.右侧会阴部积气\n较前已吸收；8.腹主动脉及双侧髂总动脉粥样硬化。9.腰椎退行性变。\n入院诊断：1.直肠腺癌 ycT4bN2M1 IV期（肺转移）；2.肺气肿伴双肺肺大疱；3.混合\n痔；4.肝囊肿；5.双肺结节；6.双肺细菌性肺炎。\n第1页\n出院记录\n姓名：\n科室：\n住院号：\n诊疗经过：患者入院后积极完善相关辅助检查，血常规：中性粒细胞绝对值10.57*10^\n9/L，血红蛋白128.00g/L，红细胞比积38.80%，白细胞计数12.28*10^9/L，C反应蛋\n白101.75mg/L。DIC全套：纤维蛋白原检测9.1g/L。大便潜血：阳性。肿瘤标记物：\n癌胚抗原6.84ng/mL，糖类抗原72427.95U/mL。血生化、心肌标记物及心肌酶谱均未\n见明显异常。结合患者病史、体征及相关辅助检查，考虑患者直肠癌肺转移较前进展，\n因患者且合并远处转移，无法行根治性手术切除原发病灶及转移病灶，故建议患者行\n“支气管、肋间、胸廓内外动脉+肠道动脉灌注化疗栓塞术”，提高患者生存周期并改\n善患者生质量，但患者因自身原因拒绝行介入手术治疗，并要求继续使用贝伐珠单抗靶\n向治疗及对症止痛。但因患者目前疗效评估为PD，结合患者原免疫组化，考虑化疗药物\n可能对肿瘤细胞形态及抗原表达产生影响，从而发生免疫组化结果改变，故建议患者再\n次行肠镜检查取病理活检明确免疫组化情况，必要时再次行基因检测指导抗肿瘤药物选\n择。患者及家属拒绝行病理活检，要求暂使用贝伐珠单抗靶向治疗，向患者告知可能因\n免疫组化改变发生耐药，但患者家属仍坚持要求继续使用贝伐珠单抗。后予患者完善盆\n腔MRI平扫，盆腔MRI示：1.直肠下段Ca，累及浆膜面，盆腔多发肿大淋巴结；2.盆腔左\n份脓肿（大小约106×38×29mm）可能；3.骨盆骨质疏松征象。阅片可见患者盆腔左份\n及左侧会阴区见不规则团片状密度增高影，部分呈囊状改变，因病灶范围大与周围临近\n器官组织分界欠清，压迫症状明显，故建议患者行脓肿穿刺置管引流术，缓解压迫症\n状。且阅片可见患者直肠肿瘤较前增大已明显侵犯浆膜面，患者目前已出血肛门坠胀及\n排便困难等症状，考虑为肿瘤进展后体积增大，阻塞肠腔所致，故建议患者可行直肠球\n囊扩张、支架置入或姑息性造瘘术以改善排便困难症状，避免因肠管狭窄出现肠梗阻危\n及生命，向患者及家属交代患者目前病情及后续治疗后，患者及家属表示理解，同意行\n脓肿穿刺引流，但拒绝行直肠球囊扩张、支架置入及姑息性造瘘术，故排除手术禁忌后\n于2026年2月8日在局麻下行“经CT引导下盆腔脓肿穿刺置管引流术”，手术过程顺利，\n术后继予患者抗感染、抑酸护胃等对症支持治疗，后患者肛周皮肤出现破溃流脓，考虑\n为直肠肿瘤进展后肿瘤直接浸润肠壁全层及穿透至肛周组织，导致局部组织坏死流出，\n出现肛周皮肤破溃伴流脓，予患者盐水冲洗创面及加强换药，保持引流通畅，促进创面\n愈合，经治疗患者创面渗出较前已明显减少，但为避免窦道形成，仍建议患者尽快行外\n科手术治疗，患者及家属表示理解，并要求转院行外科手术治疗，请示上级医师后同意\n第2页\n出院记录\n姓名：\n科室：\n住院号：\n予患者签署自请出院协议后今日出院。\n手术：经CT引导下盐腔脓肿穿刺置管引流术 2026-02-08\n出院情况：患者诉创面渗出较前已明显减少，无恶心、呕吐，无咳嗽、咳痰，无胸痛。\n胸闷、气促、呼吸困难，无腹胀、腹痛，无畏寒、发热等不适，精神、饮食、睡眠尚\n可，小便黄清，大便同前。查体：全身浅表淋巴结未扪及肿大，胸廓对称无畸形，肋间\n隙无明显增宽及凹陷，胸骨无压痛，双肺叩诊呈清音，双肺呼吸音粗，双肺可闻及散在\n湿啰音。腹平软，全腹未见腹部静脉曲张、蜘蛛痣，未见胃肠型蠕动波。全腹无压痛、\n反跳痛及肌紧张，肝脾肋下未扪及，莫菲氏征阴性，移动性浊音阴性，双肾区无叩击\n痛，肠鸣音约4次/分，阴囊皮肤正常，未见红肿、破溃，肛周6点钟方向可见一大小约2\n×1cm不规则皮肤缺损，创面基底呈暗红色可见少量白色脓苔附着，可见少量灰白色恶\n臭味脓性分泌物流出。肛门括约肌张力正常，于直肠距肛门约7cm处可扪及环状肿物，\n质地硬，表面凹凸不平，活动度差，退出指套可见血染。左侧臀部引流管引流通畅，可\n见暗灰色脓性分泌物引出，量约10ml。（患者取左侧卧位）\n出院诊断：1.直肠腺癌 ycT4bN2M1 IV期（肺转移）；2.肺气肿伴双肺肺大疱；3.混合\n痔；4.肝囊肿；5.双肺结节；6.双肺细菌性肺炎；7.轻度贫血；8.盆腔脓肿；9.肛周脓\n肿。\n出院医嘱：院外继续治疗。\n康复指导：嘱患者适当活动，禁忌久卧、久坐，避免深静脉血栓形成\n医生坐诊信息\n医生签名：\n2026-2-26\n第3页",
    "role": "user"
  }
]
2026-08-10 14:57:57,374 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:57:57,374 INFO     29 [qwen-vl-text] LLM output (len=4654):
{
  "encounter_date": "2026-02-26",
  "admission_date": "2026-02-05",
  "discharge_date": "2026-02-26",
  "hospital_days": 21,
  "department": null,
  "bed_number": null,
  "admission_condition": "患者男，63岁，因“诊断直肠癌肺转移7+月”入院；既往史：4+年前因“大便不成形伴血便”就诊于外院，考虑为“直肠癌”，未明确诊断，自行服用中药治疗；10+月前因“阴囊脓肿”于我院局麻下行“阴囊下部脓肿切开引流术”，病理结果回示：“阴囊内容物”检材大部分为变性坏死组织，区域见大量中性粒细胞浸润。予换药、抗感染等对症治疗后好转。专科情况：全身皮肤粘膜无黄染、出血点及瘀斑，全身浅表淋巴结未扪及肿大，胸廓对称无畸形，肋间隙无明显增宽及凹陷，胸骨无压痛，双肺叩诊呈清音，双肺呼吸音粗，双肺可闻及散在湿啰音。腹平软，全腹未见腹部静脉曲张、蜘蛛痣，未见胃肠型蠕动波。全腹无压痛、反跳痛及肌紧张，肝脾肋下未扪及，莫菲氏征阴性，移动性浊音阴性，双肾区无叩击痛，肠鸣音约4次/分，阴囊及肛周皮肤正常，未见红肿、破溃，肛周6点钟方向可扪及一约2*3cm大小包块，质韧，挤压时无明显脓液，肛门括约肌张力正常，于直肠距肛门约7cm处可扪及环状肿物，质地硬，表面凹凸不平，活动度差，退出指套可见血染。（患者取左侧卧位）",
  "admission_diagnoses": [
    {
      "name": "直肠腺癌 ycT4bN2M1 IV期（肺转移）",
      "diagnosis_type": "西医"
    },
    {
      "name": "肺气肿伴双肺肺大疱",
      "diagnosis_type": "西医"
    },
    {
      "name": "混合痔",
      "diagnosis_type": "西医"
    },
    {
      "name": "肝囊肿",
      "diagnosis_type": "西医"
    },
    {
      "name": "双肺结节",
      "diagnosis_type": "西医"
    },
    {
      "name": "双肺细菌性肺炎",
      "diagnosis_type": "西医"
    }
  ],
  "treatment_summary": "患者入院后积极完善相关辅助检查，血常规：中性粒细胞绝对值10.57*10^9/L，血红蛋白128.00g/L，红细胞比积38.80%，白细胞计数12.28*10^9/L，C反应蛋白101.75mg/L。DIC全套：纤维蛋白原检测9.1g/L。大便潜血：阳性。肿瘤标记物：癌胚抗原6.84ng/mL，糖类抗原72427.95U/mL。血生化、心肌标记物及心肌酶谱均未见明显异常。结合患者病史、体征及相关辅助检查，考虑患者直肠癌肺转移较前进展，因患者且合并远处转移，无法行根治性手术切除原发病灶及转移病灶，故建议患者行“支气管、肋间、胸廓内外动脉+肠道动脉灌注化疗栓塞术”，提高患者生存周期并改善患者生质量，但患者因自身原因拒绝行介入手术治疗，并要求继续使用贝伐珠单抗靶向治疗及对症止痛。但因患者目前疗效评估为PD，结合患者原免疫组化，考虑化疗药物可能对肿瘤细胞形态及抗原表达产生影响，从而发生免疫组化结果改变，故建议患者再次行肠镜检查取病理活检明确免疫组化情况，必要时再次行基因检测指导抗肿瘤药物选择。患者及家属拒绝行病理活检，要求暂使用贝伐珠单抗靶向治疗，向患者告知可能因免疫组化改变发生耐药，但患者家属仍坚持要求继续使用贝伐珠单抗。后予患者完善盆腔MRI平扫，盆腔MRI示：1.直肠下段Ca，累及浆膜面，盆腔多发肿大淋巴结；2.盆腔左份脓肿（大小约106×38×29mm）可能；3.骨盆骨质疏松征象。阅片可见患者盆腔左份及左侧会阴区见不规则团片状密度增高影，部分呈囊状改变，因病灶范围大与周围临近器官组织分界欠清，压迫症状明显，故建议患者行脓肿穿刺置管引流术，缓解压迫症状。且阅片可见患者直肠肿瘤较前增大已明显侵犯浆膜面，患者目前已出血肛门坠胀及排便困难等症状，考虑为肿瘤进展后体积增大，阻塞肠腔所致，故建议患者可行直肠球囊扩张、支架置入或姑息性造瘘术以改善排便困难症状，避免因肠管狭窄出现肠梗阻危及生命，向患者及家属交代患者目前病情及后续治疗后，患者及家属表示理解，同意行脓肿穿刺引流，但拒绝行直肠球囊扩张、支架置入及姑息性造瘘术，故排除手术禁忌后于2026年2月8日在局麻下行“经CT引导下盆腔脓肿穿刺置管引流术”，手术过程顺利，术后继予患者抗感染、抑酸护胃等对症支持治疗，后患者肛周皮肤出现破溃流脓，考虑为直肠肿瘤进展后肿瘤直接浸润肠壁全层及穿透至肛周组织，导致局部组织坏死流出，出现肛周皮肤破溃伴流脓，予患者盐水冲洗创面及加强换药，保持引流通畅，促进创面愈合，经治疗患者创面渗出较前已明显减少，但为避免窦道形成，仍建议患者尽快行外科手术治疗，患者及家属表示理解，并要求转院行外科手术治疗，请示上级医师后同意予患者签署自请出院协议后今日出院。手术：经CT引导下盐腔脓肿穿刺置管引流术 2026-02-08",
  "auxiliary_exams": "病理（病理号：2502456）：“左肺占位”恶性肿瘤，符合腺癌，结合免疫组化结果及临床病史考虑肠道来源。ALK（-）、CD56（-）、CDX-2（+）、CK20(+）、CK5/6（-）、CK7（局灶弱+）、Ki-67（30%+）、Napsin-A（-）、P40(-)、P53（突变型）、P63(-)、SATB2(+)、Syn（-）、TTF-1（+）、CK(AE1/AE3)（+）、Vimentin（-）、Villin(+)。基因检测：1.KRAS基因突变；2.MYC基因扩增；3.APC基因突变。血常规：中性粒细胞绝对值10.57*10^9/L，血红蛋白128.00g/L，红细胞比积38.80%，白细胞计数12.28*10^9/L，C反应蛋白101.75mg/L。DIC全套：纤维蛋白原检测9.1g/L。大便潜血：阳性。肿瘤标记物：癌胚抗原6.84ng/mL，糖类抗原72427.95U/mL。",
  "imaging_findings": "胸部CT（本院 2026-01-08）：1.肺气肿伴双肺多发肺大疱；2.左肺上叶舌段结节及肿块，具恶性征象，较前增大；3.左肺上叶及双肺下叶实性结节，右肺中叶实性结节较前未见确切显示，右肺上叶钙化灶；4.新增双肺下叶坠积效应；5.新增气管黏液栓；6.贫血征象，主动脉粥样硬化；7.胸椎退行性变；8.PICC管较前未见确切显示。全腹+盆腔增强CT（本院 2026-01-08）：1.直肠下段病变，Ca可能，较前进展，周围多发淋巴结，较前稍增多、增大；2.肝内多发囊肿；3.双肾周多发渗出，较前已吸收；4.双肾多发囊肿；5.考虑升结肠、盲肠炎伴周围炎性渗出，较前已吸收；6.前列腺钙化灶；7.右侧会阴部积气较前已吸收；8.腹主动脉及双侧髂总动脉粥样硬化。9.腰椎退行性变。盆腔MRI平扫：1.直肠下段Ca，累及浆膜面，盆腔多发肿大淋巴结；2.盆腔左份脓肿（大小约106×38×29mm）可能；3.骨盆骨质疏松征象。",
  "discharge_diagnoses": [
    {
      "name": "直肠腺癌 ycT4bN2M1 IV期（肺转移）",
      "diagnosis_type": "西医"
    },
    {
      "name": "肺气肿伴双肺肺大疱",
      "diagnosis_type": "西医"
    },
    {
      "name": "混合痔",
      "diagnosis_type": "西医"
    },
    {
      "name": "肝囊肿",
      "diagnosis_type": "西医"
    },
    {
      "name": "双肺结节",
      "diagnosis_type": "西医"
    },
    {
      "name": "双肺细菌性肺炎",
      "diagnosis_type": "西医"
    },
    {
      "name": "轻度贫血",
      "diagnosis_type": "西医"
    },
    {
      "name": "盆腔脓肿",
      "diagnosis_type": "西医"
    },
    {
      "name": "肛周脓肿",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": "患者诉创面渗出较前已明显减少，无恶心、呕吐，无咳嗽、咳痰，无胸痛。胸闷、气促、呼吸困难，无腹胀、腹痛，无畏寒、发热等不适，精神、饮食、睡眠尚可，小便黄清，大便同前。查体：全身浅表淋巴结未扪及肿大，胸廓对称无畸形，肋间隙无明显增宽及凹陷，胸骨无压痛，双肺叩诊呈清音，双肺呼吸音粗，双肺可闻及散在湿啰音。腹平软，全腹未见腹部静脉曲张、蜘蛛痣，未见胃肠型蠕动波。全腹无压痛、反跳痛及肌紧张，肝脾肋下未扪及，莫菲氏征阴性，移动性浊音阴性，双肾区无叩击痛，肠鸣音约4次/分，阴囊皮肤正常，未见红肿、破溃，肛周6点钟方向可见一大小约2×1cm不规则皮肤缺损，创面基底呈暗红色可见少量白色脓苔附着，可见少量灰白色恶臭味脓性分泌物流出。肛门括约肌张力正常，于直肠距肛门约7cm处可扪及环状肿物，质地硬，表面凹凸不平，活动度差，退出指套可见血染。左侧臀部引流管引流通畅，可见暗灰色脓性分泌物引出，量约10ml。（患者取左侧卧位）",
  "outcome": null,
  "discharge_orders": "院外继续治疗。康复指导：嘱患者适当活动，禁忌久卧、久坐，避免深静脉血栓形成",
  "do_medications": [],
  "do_follow_up": null,
  "do_precautions": [
    "适当活动",
    "禁忌久卧、久坐",
    "避免深静脉血栓形成"
  ],
  "next_treatment_date": null,
  "attending_physician": null,
  "pe_ecog_score": null,
  "body_surface_area": null,
  "vs_temperature_c": null,
  "vs_pulse_bpm": null,
  "vs_respiration_rpm": null,
  "vs_systolic_bp_mmhg": null,
  "vs_diastolic_bp_mmhg": null
}
2026-08-10 14:57:57,374 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-26]
2026-08-10 14:57:57,376 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1215829, prompt_len=1979
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共40行）
["出院记录", "姓名：", "科室：", "住院号：", "姓名：", "职业：自由职业", "性别：男", "入院日期：2026-2-5 10:14", "年龄：63岁", "出院日期：2026-2-26 10:25", "民族：汉族", "住院天数：21天", "籍贯：", "科 室：", "入院情况：", "患者男，63岁，因“诊断直肠癌肺转移7+月”入院；既往史：4+年前因“大便不成形伴血", "便”就诊于外院，考虑为“直肠癌”，未明确诊断，自行服用中药治疗；10+月前因“阴囊脓肿”于", "我院局麻下行“阴囊下部脓肿切开引流术”，病理结果回示：“阴囊内容物”检材大部分为变性坏", "死组织，区域见大量中性粒细胞浸润。予换药、抗感染等对症治疗后好转。专科情况：全身皮肤粘", "膜无黄染、出血点及瘀斑，全身浅表淋巴结未扪及肿大，胸廓对称无畸形，肋间隙无明显增宽及凹", "陷，胸骨无压痛，双肺叩诊呈清音，双肺呼吸音粗，双肺可闻及散在湿啰音。腹平软，全腹未见腹", "部静脉曲张、蜘蛛痣，未见胃肠型蠕动波。全腹无压痛、反跳痛及肌紧张，肝脾肋下未扪及，莫菲", "氏征阴性，移动性浊音阴性，双肾区无叩击痛，肠鸣音约4次/分，阴囊及肛周皮肤正常，未见红", "肿、破溃，肛周6点钟方向可扪及一约2*3cm大小包块，质韧，挤压时无明显脓液，肛门括约肌张力", "正常，于直肠距肛门约7cm处可扪及环状肿物，质地硬，表面凹凸不平，活动度差，退出指套可见血", "染。（患者取左侧卧位）辅助检查：病理（病理号：2502456）：“左肺占位”恶性肿瘤，符合腺", "癌，结合免疫组化结果及临床病史考虑肠道来源。ALK（-）、CD56（-）、CDX-2（+）、CK20", "(+）、CK5/6（-）、CK7（局灶弱+）、Ki-67（30%+）、Napsin-A（-）、P40(-)、P53（突变", "型）、P63(-)、SATB2(+)、Syn（-）、TTF-1（+）、CK(AE1/AE3)（+）、Vimentin（-）、Villin", "(+）。基因检测：1.KRAS基因突变；2.MYC基因扩增；3.APC基因突变。胸部CT（本院 2026-01-", "08）：1.肺气肿伴双肺多发肺大疱；2.左肺上叶舌段结节及肿块，具恶性征象，较前增大；3.左肺上", "叶及双肺下叶实性结节，右肺中叶实性结节较前未见确切显示，右肺上叶钙化灶；4.新增双肺下叶", "坠积效应；5.新增气管黏液栓；6.贫血征象，主动脉粥样硬化；7.胸椎退行性变；8.PICC管较前未", "见确切显示。全腹+盆腔增强CT（本院 2026-01-08）：1.直肠下段病变，Ca可能，较前进展，周围", "多发淋巴结，较前稍增多、增大；2.肝内多发囊肿；3.双肾周多发渗出，较前已吸收；4.双肾多发", "囊肿；5.考虑升结肠、盲肠炎伴周围炎性渗出，较前已吸收；6.前列腺钙化灶；7.右侧会阴部积气", "较前已吸收；8.腹主动脉及双侧髂总动脉粥样硬化。9.腰椎退行性变。", "入院诊断：1.直肠腺癌 ycT4bN2M1 IV期（肺转移）；2.肺气肿伴双肺肺大疱；3.混合", "痔；4.肝囊肿；5.双肺结节；6.双肺细菌性肺炎。", "第1页"]

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
2026-08-10 14:58:14,779 INFO     29 [qwen-vl-text] coord API raw response (len=3009):
[
	{"text": "出院记录", "bbox": [370, 257, 476, 273]},
	{"text": "姓名：", "bbox": [174, 273, 209, 284]},
	{"text": "科室：", "bbox": [325, 274, 358, 285]},
	{"text": "住院号：", "bbox": [552, 280, 595, 290]},
	{"text": "姓名：", "bbox": [174, 290, 209, 301]},
	{"text": "职业：自由职业", "bbox": [426, 292, 551, 303]},
	{"text": "性别：男", "bbox": [174, 306, 247, 317]},
	{"text": "入院日期：2026-2-5 10:14", "bbox": [426, 308, 591, 319]},
	{"text": "年龄：63岁", "bbox": [174, 322, 268, 333]},
	{"text": "出院日期：2026-2-26 10:25", "bbox": [426, 324, 599, 335]},
	{"text": "民族：汉族", "bbox": [174, 339, 261, 350]},
	{"text": "住院天数：21天", "bbox": [426, 340, 542, 351]},
	{"text": "籍贯：", "bbox": [174, 355, 205, 366]},
	{"text": "科 室：", "bbox": [426, 357, 488, 368]},
	{"text": "入院情况：", "bbox": [167, 371, 230, 382]},
	{"text": "患者男，63岁，因“诊断直肠癌肺转移7+月”入院；既往史：4+年前因“大便不成形伴血", "bbox": [164, 386, 690, 397]},
	{"text": "便”就诊于外院，考虑为“直肠癌”，未明确诊断，自行服用中药治疗；10+月前因“阴囊脓肿”于", "bbox": [164, 402, 692, 413]},
	{"text": "我院局麻下行“阴囊下部脓肿切开引流术”，病理结果回示：“阴囊内容物”检材大部分为变性坏", "bbox": [164, 418, 689, 429]},
	{"text": "死组织，区域见大量中性粒细胞浸润。予换药、抗感染等对症治疗后好转。专科情况：全身皮肤粘", "bbox": [162, 434, 690, 445]},
	{"text": "膜无黄染、出血点及瘀斑，全身浅表淋巴结未扪及肿大，胸廓对称无畸形，肋间隙无明显增宽及凹", "bbox": [161, 450, 692, 461]},
	{"text": "陷，胸骨无压痛，双肺叩诊呈清音，双肺呼吸音粗，双肺可闻及散在湿啰音。腹平软，全腹未见腹", "bbox": [159, 466, 694, 477]},
	{"text": "部静脉曲张、蜘蛛痣，未见胃肠型蠕动波。全腹无压痛、反跳痛及肌紧张，肝脾肋下未扪及，莫菲", "bbox": [159, 482, 696, 493]},
	{"text": "氏征阴性，移动性浊音阴性，双肾区无叩击痛，肠鸣音约4次/分，阴囊及肛周皮肤正常，未见红", "bbox": [158, 498, 687, 509]},
	{"text": "肿、破溃，肛周6点钟方向可扪及一约2*3cm大小包块，质韧，挤压时无明显脓液，肛门括约肌张力", "bbox": [156, 514, 700, 525]},
	{"text": "正常，于直肠距肛门约7cm处可扪及环状肿物，质地硬，表面凹凸不平，活动度差，退出指套可见血", "bbox": [156, 530, 709, 541]},
	{"text": "染。（患者取左侧卧位）辅助检查：病理（病理号：2502456）：“左肺占位”恶性肿瘤，符合腺", "bbox": [153, 546, 700, 558]},
	{"text": "癌，结合免疫组化结果及临床病史考虑肠道来源。ALK（-）、CD56（-）、CDX-2（+）、CK20", "bbox": [151, 563, 677, 575]},
	{"text": "(+）、CK5/6（-）、CK7（局灶弱+）、Ki-67（30%+）、Napsin-A（-）、P40(-)、P53（突变", "bbox": [156, 579, 686, 591]},
	{"text": "型）、P63(-)、SATB2(+)、Syn（-）、TTF-1（+）、CK(AE1/AE3)（+）、Vimentin（-）、Villin", "bbox": [150, 596, 707, 608]},
	{"text": "(+）。基因检测：1.KRAS基因突变；2.MYC基因扩增；3.APC基因突变。胸部CT（本院 2026-01-", "bbox": [153, 613, 703, 625]},
	{"text": "08）：1.肺气肿伴双肺多发肺大疱；2.左肺上叶舌段结节及肿块，具恶性征象，较前增大；3.左肺上", "bbox": [145, 630, 725, 648]},
	{"text": "叶及双肺下叶实性结节，右肺中叶实性结节较前未见确切显示，右肺上叶钙化灶；4.新增双肺下叶", "bbox": [144, 650, 721, 668]},
	{"text": "坠积效应；5.新增气管黏液栓；6.贫血征象，主动脉粥样硬化；7.胸椎退行性变；8.PICC管较前未", "bbox": [143, 669, 724, 688]},
	{"text": "见确切显示。全腹+盆腔增强CT（本院 2026-01-08）：1.直肠下段病变，Ca可能，较前进展，周围", "bbox": [142, 688, 727, 708]},
	{"text": "多发淋巴结，较前稍增多、增大；2.肝内多发囊肿；3.双肾周多发渗出，较前已吸收；4.双肾多发", "bbox": [141, 708, 731, 727]},
	{"text": "囊肿；5.考虑升结肠、盲肠炎伴周围炎性渗出，较前已吸收；6.前列腺钙化灶；7.右侧会阴部积气", "bbox": [140, 727, 734, 747]},
	{"text": "较前已吸收；8.腹主动脉及双侧髂总动脉粥样硬化。9.腰椎退行性变。", "bbox": [140, 749, 564, 767]},
	{"text": "入院诊断：1.直肠腺癌 ycT4bN2M1 IV期（肺转移）；2.肺气肿伴双肺肺大疱；3.混合", "bbox": [139, 768, 727, 788]},
	{"text": "痔；4.肝囊肿；5.双肺结节；6.双肺细菌性肺炎。", "bbox": [138, 794, 482, 812]},
	{"text": "第1页", "bbox": [418, 820, 458, 834]}
]
2026-08-10 14:58:14,779 INFO     29 [qwen-vl-text] coord API: raw_items=40, valid_items=40, elapsed=17.4s
2026-08-10 14:58:14,780 INFO     29 [qwen-vl-text] coord item[0]: text=出院记录, bbox=[370, 257, 476, 273]
2026-08-10 14:58:14,780 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[174, 273, 209, 284]
2026-08-10 14:58:14,780 INFO     29 [qwen-vl-text] coord item[2]: text=科室：, bbox=[325, 274, 358, 285]
2026-08-10 14:58:14,780 INFO     29 [qwen-vl-text] coord item[3]: text=住院号：, bbox=[552, 280, 595, 290]
2026-08-10 14:58:14,780 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[174, 290, 209, 301]
2026-08-10 14:58:14,780 INFO     29 [qwen-vl-text] coord item[5]: text=职业：自由职业, bbox=[426, 292, 551, 303]
2026-08-10 14:58:14,780 INFO     29 [qwen-vl-text] coord item[6]: text=性别：男, bbox=[174, 306, 247, 317]
2026-08-10 14:58:14,780 INFO     29 [qwen-vl-text] coord item[7]: text=入院日期：2026-2-5 10:14, bbox=[426, 308, 591, 319]
2026-08-10 14:58:14,780 INFO     29 [qwen-vl-text] coord item[8]: text=年龄：63岁, bbox=[174, 322, 268, 333]
2026-08-10 14:58:14,780 INFO     29 [qwen-vl-text] coord item[9]: text=出院日期：2026-2-26 10:25, bbox=[426, 324, 599, 335]
2026-08-10 14:58:14,780 INFO     29 [qwen-vl-text] coord item[10]: text=民族：汉族, bbox=[174, 339, 261, 350]
2026-08-10 14:58:14,780 INFO     29 [qwen-vl-text] coord item[11]: text=住院天数：21天, bbox=[426, 340, 542, 351]
2026-08-10 14:58:14,780 INFO     29 [qwen-vl-text] coord item[12]: text=籍贯：, bbox=[174, 355, 205, 366]
2026-08-10 14:58:14,780 INFO     29 [qwen-vl-text] coord item[13]: text=科 室：, bbox=[426, 357, 488, 368]
2026-08-10 14:58:14,780 INFO     29 [qwen-vl-text] coord item[14]: text=入院情况：, bbox=[167, 371, 230, 382]
2026-08-10 14:58:14,781 INFO     29 [qwen-vl-text] coord item[15]: text=患者男，63岁，因“诊断直肠癌肺转移7+月”入院；既往史：4+年前因“大便不成形伴血, bbox=[164, 386, 690, 397]
2026-08-10 14:58:14,781 INFO     29 [qwen-vl-text] coord item[16]: text=便”就诊于外院，考虑为“直肠癌”，未明确诊断，自行服用中药治疗；10+月前因“阴囊脓肿”于, bbox=[164, 402, 692, 413]
2026-08-10 14:58:14,781 INFO     29 [qwen-vl-text] coord item[17]: text=我院局麻下行“阴囊下部脓肿切开引流术”，病理结果回示：“阴囊内容物”检材大部分为变性坏, bbox=[164, 418, 689, 429]
2026-08-10 14:58:14,781 INFO     29 [qwen-vl-text] coord item[18]: text=死组织，区域见大量中性粒细胞浸润。予换药、抗感染等对症治疗后好转。专科情况：全身皮肤粘, bbox=[162, 434, 690, 445]
2026-08-10 14:58:14,781 INFO     29 [qwen-vl-text] coord item[19]: text=膜无黄染、出血点及瘀斑，全身浅表淋巴结未扪及肿大，胸廓对称无畸形，肋间隙无明显增宽及凹, bbox=[161, 450, 692, 461]
2026-08-10 14:58:14,781 INFO     29 [qwen-vl-text] coord item[20]: text=陷，胸骨无压痛，双肺叩诊呈清音，双肺呼吸音粗，双肺可闻及散在湿啰音。腹平软，全腹未见腹, bbox=[159, 466, 694, 477]
2026-08-10 14:58:14,781 INFO     29 [qwen-vl-text] coord item[21]: text=部静脉曲张、蜘蛛痣，未见胃肠型蠕动波。全腹无压痛、反跳痛及肌紧张，肝脾肋下未扪及，莫菲, bbox=[159, 482, 696, 493]
2026-08-10 14:58:14,781 INFO     29 [qwen-vl-text] coord item[22]: text=氏征阴性，移动性浊音阴性，双肾区无叩击痛，肠鸣音约4次/分，阴囊及肛周皮肤正常，未见红, bbox=[158, 498, 687, 509]
2026-08-10 14:58:14,781 INFO     29 [qwen-vl-text] coord item[23]: text=肿、破溃，肛周6点钟方向可扪及一约2*3cm大小包块，质韧，挤压时无明显脓液，肛门括约肌张力, bbox=[156, 514, 700, 525]
2026-08-10 14:58:14,781 INFO     29 [qwen-vl-text] coord item[24]: text=正常，于直肠距肛门约7cm处可扪及环状肿物，质地硬，表面凹凸不平，活动度差，退出指套可见血, bbox=[156, 530, 709, 541]
2026-08-10 14:58:14,781 INFO     29 [qwen-vl-text] coord item[25]: text=染。（患者取左侧卧位）辅助检查：病理（病理号：2502456）：“左肺占位”恶性肿瘤，符合腺, bbox=[153, 546, 700, 558]
2026-08-10 14:58:14,781 INFO     29 [qwen-vl-text] coord item[26]: text=癌，结合免疫组化结果及临床病史考虑肠道来源。ALK（-）、CD56（-）、CDX-2（+）、CK20, bbox=[151, 563, 677, 575]
2026-08-10 14:58:14,781 INFO     29 [qwen-vl-text] coord item[27]: text=(+）、CK5/6（-）、CK7（局灶弱+）、Ki-67（30%+）、Napsin-A（-）、P40(-)、P53（突变, bbox=[156, 579, 686, 591]
2026-08-10 14:58:14,781 INFO     29 [qwen-vl-text] coord item[28]: text=型）、P63(-)、SATB2(+)、Syn（-）、TTF-1（+）、CK(AE1/AE3)（+）、Vimentin（-）、Villin, bbox=[150, 596, 707, 608]
2026-08-10 14:58:14,781 INFO     29 [qwen-vl-text] coord item[29]: text=(+）。基因检测：1.KRAS基因突变；2.MYC基因扩增；3.APC基因突变。胸部CT（本院 2026-01-, bbox=[153, 613, 703, 625]
2026-08-10 14:58:14,781 INFO     29 [qwen-vl-text] coord item[30]: text=08）：1.肺气肿伴双肺多发肺大疱；2.左肺上叶舌段结节及肿块，具恶性征象，较前增大；3.左肺上, bbox=[145, 630, 725, 648]
2026-08-10 14:58:14,781 INFO     29 [qwen-vl-text] coord item[31]: text=叶及双肺下叶实性结节，右肺中叶实性结节较前未见确切显示，右肺上叶钙化灶；4.新增双肺下叶, bbox=[144, 650, 721, 668]
2026-08-10 14:58:14,781 INFO     29 [qwen-vl-text] coord item[32]: text=坠积效应；5.新增气管黏液栓；6.贫血征象，主动脉粥样硬化；7.胸椎退行性变；8.PICC管较前未, bbox=[143, 669, 724, 688]
2026-08-10 14:58:14,781 INFO     29 [qwen-vl-text] coord item[33]: text=见确切显示。全腹+盆腔增强CT（本院 2026-01-08）：1.直肠下段病变，Ca可能，较前进展，周围, bbox=[142, 688, 727, 708]
2026-08-10 14:58:14,781 INFO     29 [qwen-vl-text] coord item[34]: text=多发淋巴结，较前稍增多、增大；2.肝内多发囊肿；3.双肾周多发渗出，较前已吸收；4.双肾多发, bbox=[141, 708, 731, 727]
2026-08-10 14:58:14,781 INFO     29 [qwen-vl-text] coord item[35]: text=囊肿；5.考虑升结肠、盲肠炎伴周围炎性渗出，较前已吸收；6.前列腺钙化灶；7.右侧会阴部积气, bbox=[140, 727, 734, 747]
2026-08-10 14:58:14,781 INFO     29 [qwen-vl-text] coord item[36]: text=较前已吸收；8.腹主动脉及双侧髂总动脉粥样硬化。9.腰椎退行性变。, bbox=[140, 749, 564, 767]
2026-08-10 14:58:14,781 INFO     29 [qwen-vl-text] coord item[37]: text=入院诊断：1.直肠腺癌 ycT4bN2M1 IV期（肺转移）；2.肺气肿伴双肺肺大疱；3.混合, bbox=[139, 768, 727, 788]
2026-08-10 14:58:14,781 INFO     29 [qwen-vl-text] coord item[38]: text=痔；4.肝囊肿；5.双肺结节；6.双肺细菌性肺炎。, bbox=[138, 794, 482, 812]
2026-08-10 14:58:14,782 INFO     29 [qwen-vl-text] coord item[39]: text=第1页, bbox=[418, 820, 458, 834]
2026-08-10 14:58:14,782 INFO     29 [qwen-vl-text] page=8 — 40/40 coords, api_time=17.4s
2026-08-10 14:58:14,784 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1422312, prompt_len=1874
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["出院记录", "姓名：", "科室：", "住院号：", "诊疗经过：患者入院后积极完善相关辅助检查，血常规：中性粒细胞绝对值10.57*10^", "9/L，血红蛋白128.00g/L，红细胞比积38.80%，白细胞计数12.28*10^9/L，C反应蛋", "白101.75mg/L。DIC全套：纤维蛋白原检测9.1g/L。大便潜血：阳性。肿瘤标记物：", "癌胚抗原6.84ng/mL，糖类抗原72427.95U/mL。血生化、心肌标记物及心肌酶谱均未", "见明显异常。结合患者病史、体征及相关辅助检查，考虑患者直肠癌肺转移较前进展，", "因患者且合并远处转移，无法行根治性手术切除原发病灶及转移病灶，故建议患者行", "“支气管、肋间、胸廓内外动脉+肠道动脉灌注化疗栓塞术”，提高患者生存周期并改", "善患者生质量，但患者因自身原因拒绝行介入手术治疗，并要求继续使用贝伐珠单抗靶", "向治疗及对症止痛。但因患者目前疗效评估为PD，结合患者原免疫组化，考虑化疗药物", "可能对肿瘤细胞形态及抗原表达产生影响，从而发生免疫组化结果改变，故建议患者再", "次行肠镜检查取病理活检明确免疫组化情况，必要时再次行基因检测指导抗肿瘤药物选", "择。患者及家属拒绝行病理活检，要求暂使用贝伐珠单抗靶向治疗，向患者告知可能因", "免疫组化改变发生耐药，但患者家属仍坚持要求继续使用贝伐珠单抗。后予患者完善盆", "腔MRI平扫，盆腔MRI示：1.直肠下段Ca，累及浆膜面，盆腔多发肿大淋巴结；2.盆腔左", "份脓肿（大小约106×38×29mm）可能；3.骨盆骨质疏松征象。阅片可见患者盆腔左份", "及左侧会阴区见不规则团片状密度增高影，部分呈囊状改变，因病灶范围大与周围临近", "器官组织分界欠清，压迫症状明显，故建议患者行脓肿穿刺置管引流术，缓解压迫症", "状。且阅片可见患者直肠肿瘤较前增大已明显侵犯浆膜面，患者目前已出血肛门坠胀及", "排便困难等症状，考虑为肿瘤进展后体积增大，阻塞肠腔所致，故建议患者可行直肠球", "囊扩张、支架置入或姑息性造瘘术以改善排便困难症状，避免因肠管狭窄出现肠梗阻危", "及生命，向患者及家属交代患者目前病情及后续治疗后，患者及家属表示理解，同意行", "脓肿穿刺引流，但拒绝行直肠球囊扩张、支架置入及姑息性造瘘术，故排除手术禁忌后", "于2026年2月8日在局麻下行“经CT引导下盆腔脓肿穿刺置管引流术”，手术过程顺利，", "术后继予患者抗感染、抑酸护胃等对症支持治疗，后患者肛周皮肤出现破溃流脓，考虑", "为直肠肿瘤进展后肿瘤直接浸润肠壁全层及穿透至肛周组织，导致局部组织坏死流出，", "出现肛周皮肤破溃伴流脓，予患者盐水冲洗创面及加强换药，保持引流通畅，促进创面", "愈合，经治疗患者创面渗出较前已明显减少，但为避免窦道形成，仍建议患者尽快行外", "科手术治疗，患者及家属表示理解，并要求转院行外科手术治疗，请示上级医师后同意", "第2页"]

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
2026-08-10 14:58:28,583 INFO     29 [qwen-vl-text] coord API raw response (len=2617):
[
	{"text": "出院记录", "bbox": [363, 212, 473, 229]},
	{"text": "姓名：", "bbox": [160, 228, 196, 240]},
	{"text": "科室：", "bbox": [316, 232, 348, 243]},
	{"text": "住院号：", "bbox": [551, 237, 595, 248]},
	{"text": "诊疗经过：患者入院后积极完善相关辅助检查，血常规：中性粒细胞绝对值10.57*10^", "bbox": [154, 245, 670, 265]},
	{"text": "9/L，血红蛋白128.00g/L，红细胞比积38.80%，白细胞计数12.28*10^9/L，C反应蛋", "bbox": [152, 262, 678, 282]},
	{"text": "白101.75mg/L。DIC全套：纤维蛋白原检测9.1g/L。大便潜血：阳性。肿瘤标记物：", "bbox": [154, 279, 667, 298]},
	{"text": "癌胚抗原6.84ng/mL，糖类抗原72427.95U/mL。血生化、心肌标记物及心肌酶谱均未", "bbox": [152, 296, 676, 314]},
	{"text": "见明显异常。结合患者病史、体征及相关辅助检查，考虑患者直肠癌肺转移较前进展，", "bbox": [152, 313, 678, 331]},
	{"text": "因患者且合并远处转移，无法行根治性手术切除原发病灶及转移病灶，故建议患者行", "bbox": [152, 331, 674, 348]},
	{"text": "“支气管、肋间、胸廓内外动脉+肠道动脉灌注化疗栓塞术”，提高患者生存周期并改", "bbox": [156, 348, 684, 365]},
	{"text": "善患者生质量，但患者因自身原因拒绝行介入手术治疗，并要求继续使用贝伐珠单抗靶", "bbox": [152, 365, 691, 381]},
	{"text": "向治疗及对症止痛。但因患者目前疗效评估为PD，结合患者原免疫组化，考虑化疗药物", "bbox": [152, 382, 693, 399]},
	{"text": "可能对肿瘤细胞形态及抗原表达产生影响，从而发生免疫组化结果改变，故建议患者再", "bbox": [152, 400, 694, 416]},
	{"text": "次行肠镜检查取病理活检明确免疫组化情况，必要时再次行基因检测指导抗肿瘤药物选", "bbox": [152, 417, 696, 433]},
	{"text": "择。患者及家属拒绝行病理活检，要求暂使用贝伐珠单抗靶向治疗，向患者告知可能因", "bbox": [150, 434, 698, 451]},
	{"text": "免疫组化改变发生耐药，但患者家属仍坚持要求继续使用贝伐珠单抗。后予患者完善盆", "bbox": [150, 451, 700, 469]},
	{"text": "腔MRI平扫，盆腔MRI示：1.直肠下段Ca，累及浆膜面，盆腔多发肿大淋巴结；2.盆腔左", "bbox": [148, 469, 702, 487]},
	{"text": "份脓肿（大小约106×38×29mm）可能；3.骨盆骨质疏松征象。阅片可见患者盆腔左份", "bbox": [148, 486, 699, 505]},
	{"text": "及左侧会阴区见不规则团片状密度增高影，部分呈囊状改变，因病灶范围大与周围临近", "bbox": [148, 504, 708, 523]},
	{"text": "器官组织分界欠清，压迫症状明显，故建议患者行脓肿穿刺置管引流术，缓解压迫症", "bbox": [148, 522, 698, 541]},
	{"text": "状。且阅片可见患者直肠肿瘤较前增大已明显侵犯浆膜面，患者目前已出血肛门坠胀及", "bbox": [146, 539, 714, 560]},
	{"text": "排便困难等症状，考虑为肿瘤进展后体积增大，阻塞肠腔所致，故建议患者可行直肠球", "bbox": [146, 558, 717, 579]},
	{"text": "囊扩张、支架置入或姑息性造瘘术以改善排便困难症状，避免因肠管狭窄出现肠梗阻危", "bbox": [146, 576, 720, 600]},
	{"text": "及生命，向患者及家属交代患者目前病情及后续治疗后，患者及家属表示理解，同意行", "bbox": [144, 596, 722, 620]},
	{"text": "脓肿穿刺引流，但拒绝行直肠球囊扩张、支架置入及姑息性造瘘术，故排除手术禁忌后", "bbox": [144, 615, 725, 641]},
	{"text": "于2026年2月8日在局麻下行“经CT引导下盆腔脓肿穿刺置管引流术”，手术过程顺利，", "bbox": [144, 635, 720, 663]},
	{"text": "术后继予患者抗感染、抑酸护胃等对症支持治疗，后患者肛周皮肤出现破溃流脓，考虑", "bbox": [142, 656, 733, 685]},
	{"text": "为直肠肿瘤进展后肿瘤直接浸润肠壁全层及穿透至肛周组织，导致局部组织坏死流出，", "bbox": [142, 677, 727, 708]},
	{"text": "出现肛周皮肤破溃伴流脓，予患者盐水冲洗创面及加强换药，保持引流通畅，促进创面", "bbox": [142, 698, 739, 730]},
	{"text": "愈合，经治疗患者创面渗出较前已明显减少，但为避免窦道形成，仍建议患者尽快行外", "bbox": [142, 719, 742, 751]},
	{"text": "科手术治疗，患者及家属表示理解，并要求转院行外科手术治疗，请示上级医师后同意", "bbox": [142, 741, 745, 770]},
	{"text": "第2页", "bbox": [422, 782, 463, 796]}
]
2026-08-10 14:58:28,583 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=13.8s
2026-08-10 14:58:28,583 INFO     29 [qwen-vl-text] coord item[0]: text=出院记录, bbox=[363, 212, 473, 229]
2026-08-10 14:58:28,583 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[160, 228, 196, 240]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[2]: text=科室：, bbox=[316, 232, 348, 243]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[3]: text=住院号：, bbox=[551, 237, 595, 248]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[4]: text=诊疗经过：患者入院后积极完善相关辅助检查，血常规：中性粒细胞绝对值10.57*10^, bbox=[154, 245, 670, 265]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[5]: text=9/L，血红蛋白128.00g/L，红细胞比积38.80%，白细胞计数12.28*10^9/L，C反应蛋, bbox=[152, 262, 678, 282]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[6]: text=白101.75mg/L。DIC全套：纤维蛋白原检测9.1g/L。大便潜血：阳性。肿瘤标记物：, bbox=[154, 279, 667, 298]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[7]: text=癌胚抗原6.84ng/mL，糖类抗原72427.95U/mL。血生化、心肌标记物及心肌酶谱均未, bbox=[152, 296, 676, 314]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[8]: text=见明显异常。结合患者病史、体征及相关辅助检查，考虑患者直肠癌肺转移较前进展，, bbox=[152, 313, 678, 331]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[9]: text=因患者且合并远处转移，无法行根治性手术切除原发病灶及转移病灶，故建议患者行, bbox=[152, 331, 674, 348]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[10]: text=“支气管、肋间、胸廓内外动脉+肠道动脉灌注化疗栓塞术”，提高患者生存周期并改, bbox=[156, 348, 684, 365]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[11]: text=善患者生质量，但患者因自身原因拒绝行介入手术治疗，并要求继续使用贝伐珠单抗靶, bbox=[152, 365, 691, 381]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[12]: text=向治疗及对症止痛。但因患者目前疗效评估为PD，结合患者原免疫组化，考虑化疗药物, bbox=[152, 382, 693, 399]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[13]: text=可能对肿瘤细胞形态及抗原表达产生影响，从而发生免疫组化结果改变，故建议患者再, bbox=[152, 400, 694, 416]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[14]: text=次行肠镜检查取病理活检明确免疫组化情况，必要时再次行基因检测指导抗肿瘤药物选, bbox=[152, 417, 696, 433]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[15]: text=择。患者及家属拒绝行病理活检，要求暂使用贝伐珠单抗靶向治疗，向患者告知可能因, bbox=[150, 434, 698, 451]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[16]: text=免疫组化改变发生耐药，但患者家属仍坚持要求继续使用贝伐珠单抗。后予患者完善盆, bbox=[150, 451, 700, 469]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[17]: text=腔MRI平扫，盆腔MRI示：1.直肠下段Ca，累及浆膜面，盆腔多发肿大淋巴结；2.盆腔左, bbox=[148, 469, 702, 487]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[18]: text=份脓肿（大小约106×38×29mm）可能；3.骨盆骨质疏松征象。阅片可见患者盆腔左份, bbox=[148, 486, 699, 505]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[19]: text=及左侧会阴区见不规则团片状密度增高影，部分呈囊状改变，因病灶范围大与周围临近, bbox=[148, 504, 708, 523]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[20]: text=器官组织分界欠清，压迫症状明显，故建议患者行脓肿穿刺置管引流术，缓解压迫症, bbox=[148, 522, 698, 541]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[21]: text=状。且阅片可见患者直肠肿瘤较前增大已明显侵犯浆膜面，患者目前已出血肛门坠胀及, bbox=[146, 539, 714, 560]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[22]: text=排便困难等症状，考虑为肿瘤进展后体积增大，阻塞肠腔所致，故建议患者可行直肠球, bbox=[146, 558, 717, 579]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[23]: text=囊扩张、支架置入或姑息性造瘘术以改善排便困难症状，避免因肠管狭窄出现肠梗阻危, bbox=[146, 576, 720, 600]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[24]: text=及生命，向患者及家属交代患者目前病情及后续治疗后，患者及家属表示理解，同意行, bbox=[144, 596, 722, 620]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[25]: text=脓肿穿刺引流，但拒绝行直肠球囊扩张、支架置入及姑息性造瘘术，故排除手术禁忌后, bbox=[144, 615, 725, 641]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[26]: text=于2026年2月8日在局麻下行“经CT引导下盆腔脓肿穿刺置管引流术”，手术过程顺利，, bbox=[144, 635, 720, 663]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[27]: text=术后继予患者抗感染、抑酸护胃等对症支持治疗，后患者肛周皮肤出现破溃流脓，考虑, bbox=[142, 656, 733, 685]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[28]: text=为直肠肿瘤进展后肿瘤直接浸润肠壁全层及穿透至肛周组织，导致局部组织坏死流出，, bbox=[142, 677, 727, 708]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[29]: text=出现肛周皮肤破溃伴流脓，予患者盐水冲洗创面及加强换药，保持引流通畅，促进创面, bbox=[142, 698, 739, 730]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[30]: text=愈合，经治疗患者创面渗出较前已明显减少，但为避免窦道形成，仍建议患者尽快行外, bbox=[142, 719, 742, 751]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[31]: text=科手术治疗，患者及家属表示理解，并要求转院行外科手术治疗，请示上级医师后同意, bbox=[142, 741, 745, 770]
2026-08-10 14:58:28,584 INFO     29 [qwen-vl-text] coord item[32]: text=第2页, bbox=[422, 782, 463, 796]
2026-08-10 14:58:28,585 INFO     29 [qwen-vl-text] page=9 — 33/33 coords, api_time=13.8s
2026-08-10 14:58:28,586 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=789063, prompt_len=1346
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["出院记录", "姓名：", "科室：", "住院号：", "予患者签署自请出院协议后今日出院。", "手术：经CT引导下盐腔脓肿穿刺置管引流术 2026-02-08", "出院情况：患者诉创面渗出较前已明显减少，无恶心、呕吐，无咳嗽、咳痰，无胸痛。", "胸闷、气促、呼吸困难，无腹胀、腹痛，无畏寒、发热等不适，精神、饮食、睡眠尚", "可，小便黄清，大便同前。查体：全身浅表淋巴结未扪及肿大，胸廓对称无畸形，肋间", "隙无明显增宽及凹陷，胸骨无压痛，双肺叩诊呈清音，双肺呼吸音粗，双肺可闻及散在", "湿啰音。腹平软，全腹未见腹部静脉曲张、蜘蛛痣，未见胃肠型蠕动波。全腹无压痛、", "反跳痛及肌紧张，肝脾肋下未扪及，莫菲氏征阴性，移动性浊音阴性，双肾区无叩击", "痛，肠鸣音约4次/分，阴囊皮肤正常，未见红肿、破溃，肛周6点钟方向可见一大小约2", "×1cm不规则皮肤缺损，创面基底呈暗红色可见少量白色脓苔附着，可见少量灰白色恶", "臭味脓性分泌物流出。肛门括约肌张力正常，于直肠距肛门约7cm处可扪及环状肿物，", "质地硬，表面凹凸不平，活动度差，退出指套可见血染。左侧臀部引流管引流通畅，可", "见暗灰色脓性分泌物引出，量约10ml。（患者取左侧卧位）", "出院诊断：1.直肠腺癌 ycT4bN2M1 IV期（肺转移）；2.肺气肿伴双肺肺大疱；3.混合", "痔；4.肝囊肿；5.双肺结节；6.双肺细菌性肺炎；7.轻度贫血；8.盆腔脓肿；9.肛周脓", "肿。", "出院医嘱：院外继续治疗。", "康复指导：嘱患者适当活动，禁忌久卧、久坐，避免深静脉血栓形成", "医生坐诊信息", "医生签名：", "2026-2-26", "第3页"]

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
2026-08-10 14:58:40,822 INFO     29 [qwen-vl-text] coord API raw response (len=1802):
[
	{"text": "出院记录", "bbox": [387, 222, 498, 238]},
	{"text": "姓名：", "bbox": [180, 240, 216, 251]},
	{"text": "科室：", "bbox": [341, 240, 375, 252]},
	{"text": "住院号：", "bbox": [578, 247, 623, 258]},
	{"text": "予患者签署自请出院协议后今日出院。", "bbox": [175, 257, 414, 269]},
	{"text": "手术：经CT引导下盐腔脓肿穿刺置管引流术 2026-02-08", "bbox": [175, 274, 550, 287]},
	{"text": "出院情况：患者诉创面渗出较前已明显减少，无恶心、呕吐，无咳嗽、咳痰，无胸痛。", "bbox": [175, 292, 698, 305]},
	{"text": "胸闷、气促、呼吸困难，无腹胀、腹痛，无畏寒、发热等不适，精神、饮食、睡眠尚", "bbox": [175, 310, 700, 323]},
	{"text": "可，小便黄清，大便同前。查体：全身浅表淋巴结未扪及肿大，胸廓对称无畸形，肋间", "bbox": [175, 328, 716, 340]},
	{"text": "隙无明显增宽及凹陷，胸骨无压痛，双肺叩诊呈清音，双肺呼吸音粗，双肺可闻及散在", "bbox": [175, 346, 718, 358]},
	{"text": "湿啰音。腹平软，全腹未见腹部静脉曲张、蜘蛛痣，未见胃肠型蠕动波。全腹无压痛、", "bbox": [175, 363, 714, 375]},
	{"text": "反跳痛及肌紧张，肝脾肋下未扪及，莫菲氏征阴性，移动性浊音阴性，双肾区无叩击", "bbox": [175, 380, 710, 393]},
	{"text": "痛，肠鸣音约4次/分，阴囊皮肤正常，未见红肿、破溃，肛周6点钟方向可见一大小约2", "bbox": [175, 398, 726, 411]},
	{"text": "×1cm不规则皮肤缺损，创面基底呈暗红色可见少量白色脓苔附着，可见少量灰白色恶", "bbox": [175, 415, 721, 428]},
	{"text": "臭味脓性分泌物流出。肛门括约肌张力正常，于直肠距肛门约7cm处可扪及环状肿物，", "bbox": [175, 433, 715, 446]},
	{"text": "质地硬，表面凹凸不平，活动度差，退出指套可见血染。左侧臀部引流管引流通畅，可", "bbox": [175, 450, 732, 464]},
	{"text": "见暗灰色脓性分泌物引出，量约10ml。（患者取左侧卧位）", "bbox": [175, 469, 555, 482]},
	{"text": "出院诊断：1.直肠腺癌 ycT4bN2M1 IV期（肺转移）；2.肺气肿伴双肺肺大疱；3.混合", "bbox": [175, 486, 732, 501]},
	{"text": "痔；4.肝囊肿；5.双肺结节；6.双肺细菌性肺炎；7.轻度贫血；8.盆腔脓肿；9.肛周脓", "bbox": [172, 504, 742, 520]},
	{"text": "肿。", "bbox": [171, 533, 193, 544]},
	{"text": "出院医嘱：院外继续治疗。", "bbox": [171, 550, 352, 564]},
	{"text": "康复指导：嘱患者适当活动，禁忌久卧、久坐，避免深静脉血栓形成", "bbox": [172, 563, 637, 581]},
	{"text": "医生坐诊信息", "bbox": [172, 589, 268, 602]},
	{"text": "医生签名：", "bbox": [467, 623, 535, 636]},
	{"text": "2026-2-26", "bbox": [552, 644, 623, 656]},
	{"text": "第3页", "bbox": [455, 808, 496, 821]}
]
2026-08-10 14:58:40,822 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=12.2s
2026-08-10 14:58:40,823 INFO     29 [qwen-vl-text] coord item[0]: text=出院记录, bbox=[387, 222, 498, 238]
2026-08-10 14:58:40,823 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[180, 240, 216, 251]
2026-08-10 14:58:40,823 INFO     29 [qwen-vl-text] coord item[2]: text=科室：, bbox=[341, 240, 375, 252]
2026-08-10 14:58:40,823 INFO     29 [qwen-vl-text] coord item[3]: text=住院号：, bbox=[578, 247, 623, 258]
2026-08-10 14:58:40,823 INFO     29 [qwen-vl-text] coord item[4]: text=予患者签署自请出院协议后今日出院。, bbox=[175, 257, 414, 269]
2026-08-10 14:58:40,823 INFO     29 [qwen-vl-text] coord item[5]: text=手术：经CT引导下盐腔脓肿穿刺置管引流术 2026-02-08, bbox=[175, 274, 550, 287]
2026-08-10 14:58:40,823 INFO     29 [qwen-vl-text] coord item[6]: text=出院情况：患者诉创面渗出较前已明显减少，无恶心、呕吐，无咳嗽、咳痰，无胸痛。, bbox=[175, 292, 698, 305]
2026-08-10 14:58:40,823 INFO     29 [qwen-vl-text] coord item[7]: text=胸闷、气促、呼吸困难，无腹胀、腹痛，无畏寒、发热等不适，精神、饮食、睡眠尚, bbox=[175, 310, 700, 323]
2026-08-10 14:58:40,823 INFO     29 [qwen-vl-text] coord item[8]: text=可，小便黄清，大便同前。查体：全身浅表淋巴结未扪及肿大，胸廓对称无畸形，肋间, bbox=[175, 328, 716, 340]
2026-08-10 14:58:40,823 INFO     29 [qwen-vl-text] coord item[9]: text=隙无明显增宽及凹陷，胸骨无压痛，双肺叩诊呈清音，双肺呼吸音粗，双肺可闻及散在, bbox=[175, 346, 718, 358]
2026-08-10 14:58:40,823 INFO     29 [qwen-vl-text] coord item[10]: text=湿啰音。腹平软，全腹未见腹部静脉曲张、蜘蛛痣，未见胃肠型蠕动波。全腹无压痛、, bbox=[175, 363, 714, 375]
2026-08-10 14:58:40,823 INFO     29 [qwen-vl-text] coord item[11]: text=反跳痛及肌紧张，肝脾肋下未扪及，莫菲氏征阴性，移动性浊音阴性，双肾区无叩击, bbox=[175, 380, 710, 393]
2026-08-10 14:58:40,824 INFO     29 [qwen-vl-text] coord item[12]: text=痛，肠鸣音约4次/分，阴囊皮肤正常，未见红肿、破溃，肛周6点钟方向可见一大小约2, bbox=[175, 398, 726, 411]
2026-08-10 14:58:40,824 INFO     29 [qwen-vl-text] coord item[13]: text=×1cm不规则皮肤缺损，创面基底呈暗红色可见少量白色脓苔附着，可见少量灰白色恶, bbox=[175, 415, 721, 428]
2026-08-10 14:58:40,824 INFO     29 [qwen-vl-text] coord item[14]: text=臭味脓性分泌物流出。肛门括约肌张力正常，于直肠距肛门约7cm处可扪及环状肿物，, bbox=[175, 433, 715, 446]
2026-08-10 14:58:40,824 INFO     29 [qwen-vl-text] coord item[15]: text=质地硬，表面凹凸不平，活动度差，退出指套可见血染。左侧臀部引流管引流通畅，可, bbox=[175, 450, 732, 464]
2026-08-10 14:58:40,824 INFO     29 [qwen-vl-text] coord item[16]: text=见暗灰色脓性分泌物引出，量约10ml。（患者取左侧卧位）, bbox=[175, 469, 555, 482]
2026-08-10 14:58:40,824 INFO     29 [qwen-vl-text] coord item[17]: text=出院诊断：1.直肠腺癌 ycT4bN2M1 IV期（肺转移）；2.肺气肿伴双肺肺大疱；3.混合, bbox=[175, 486, 732, 501]
2026-08-10 14:58:40,824 INFO     29 [qwen-vl-text] coord item[18]: text=痔；4.肝囊肿；5.双肺结节；6.双肺细菌性肺炎；7.轻度贫血；8.盆腔脓肿；9.肛周脓, bbox=[172, 504, 742, 520]
2026-08-10 14:58:40,824 INFO     29 [qwen-vl-text] coord item[19]: text=肿。, bbox=[171, 533, 193, 544]
2026-08-10 14:58:40,824 INFO     29 [qwen-vl-text] coord item[20]: text=出院医嘱：院外继续治疗。, bbox=[171, 550, 352, 564]
2026-08-10 14:58:40,824 INFO     29 [qwen-vl-text] coord item[21]: text=康复指导：嘱患者适当活动，禁忌久卧、久坐，避免深静脉血栓形成, bbox=[172, 563, 637, 581]
2026-08-10 14:58:40,825 INFO     29 [qwen-vl-text] coord item[22]: text=医生坐诊信息, bbox=[172, 589, 268, 602]
2026-08-10 14:58:40,825 INFO     29 [qwen-vl-text] coord item[23]: text=医生签名：, bbox=[467, 623, 535, 636]
2026-08-10 14:58:40,825 INFO     29 [qwen-vl-text] coord item[24]: text=2026-2-26, bbox=[552, 644, 623, 656]
2026-08-10 14:58:40,825 INFO     29 [qwen-vl-text] coord item[25]: text=第3页, bbox=[455, 808, 496, 821]
2026-08-10 14:58:40,825 INFO     29 [qwen-vl-text] page=10 — 26/26 coords, api_time=12.2s
2026-08-10 14:58:40,826 INFO     29 [qwen-vl-text] new_positions (99):
[[8, 220.26099548339846, 283.36279418945315, 216.36830627441407, 229.83870666503907], [8, 103.58219787597656, 124.41769744873048, 229.83870666503907, 239.09960693359375], [8, 193.47249603271484, 213.11739562988282, 230.68060668945313, 239.94150695800784], [8, 328.60559326171875, 354.20349273681643, 235.7320068359375, 244.15100708007813], [8, 103.58219787597656, 124.41769744873048, 244.15100708007813, 253.4119073486328], [8, 253.5977947998047, 328.0102932739258, 245.83480712890625, 255.09570739746096], [8, 103.58219787597656, 147.03909698486328, 257.62140747070316, 266.88230773925784], [8, 253.5977947998047, 351.82229278564455, 259.3052075195313, 268.56610778808596], [8, 103.58219787597656, 159.54039672851565, 271.0918078613281, 280.35270812988284], [8, 253.5977947998047, 356.5846926879883, 272.7756079101563, 282.03650817871096], [8, 103.58219787597656, 155.37329681396486, 285.4041082763672, 294.6650085449219], [8, 253.5977947998047, 322.65259338378905, 286.2460083007813, 295.50690856933596], [8, 103.58219787597656, 122.0364974975586, 298.8745086669922, 308.1354089355469], [8, 253.5977947998047, 290.50639404296874, 300.5583087158203, 309.819208984375], [8, 99.41509796142579, 136.91899719238282, 312.3449090576172, 321.6058093261719], [8, 97.62919799804688, 410.7569915771485, 324.9734094238281, 334.23430969238285], [8, 97.62919799804688, 411.94759155273437, 338.4438098144531, 347.70471008300785], [8, 97.62919799804688, 410.1616915893555, 351.9142102050781, 361.1751104736328], [8, 96.43859802246094, 410.7569915771485, 365.3846105957031, 374.6455108642578], [8, 95.84329803466797, 411.94759155273437, 378.8550109863281, 388.1159112548828], [8, 94.65269805908204, 413.1381915283203, 392.3254113769531, 401.5863116455078], [8, 94.65269805908204, 414.32879150390625, 405.79581176757813, 415.0567120361328], [8, 94.05739807128907, 408.97109161376954, 419.26621215820313, 428.5271124267578], [8, 92.86679809570313, 416.7099914550781, 432.73661254882813, 441.9975128173828], [8, 92.86679809570313, 422.0676913452149, 446.20701293945314, 455.4679132080078], [8, 91.08089813232422, 416.7099914550781, 459.67741333007814, 469.7802136230469], [8, 89.89029815673828, 403.01809173583985, 473.98971374511723, 484.09251403808594], [8, 92.86679809570313, 408.3757916259766, 487.46011413574223, 497.56291442871094], [8, 89.29499816894531, 420.87709136962894, 501.77241455078126, 511.87521484375003], [8, 91.08089813232422, 418.49589141845706, 516.0847149658204, 526.1875152587891], [8, 86.31849822998048, 431.59249114990234, 530.3970153808594, 545.5512158203126], [8, 85.72319824218751, 429.21129119873046, 547.2350158691406, 562.3892163085937], [8, 85.12789825439454, 430.9971911621094, 563.2311163330079, 579.227216796875], [8, 84.53259826660157, 432.7830911254883, 579.227216796875, 596.0652172851562], [8, 83.9372982788086, 435.16429107666016, 596.0652172851562, 612.0613177490235], [8, 83.34199829101563, 436.9501910400391, 612.0613177490235, 628.8993182373047], [8, 83.34199829101563, 335.7491931152344, 630.5831182861328, 645.737318725586], [8, 82.74669830322266, 432.7830911254883, 646.57921875, 663.4172192382813], [8, 82.15139831542969, 286.934594116211, 668.4686193847657, 683.6228198242188], [8, 248.83539489746096, 272.6473944091797, 690.3580200195313, 702.1446203613282], [9, 216.09389556884767, 281.5768942260742, 178.48280517578127, 192.79510559082033], [9, 95.24799804687501, 116.67879760742188, 191.95320556640627, 202.056005859375], [9, 188.11479614257814, 207.16439575195312, 195.3208056640625, 204.58170593261718], [9, 328.0102932739258, 354.20349273681643, 199.53030578613283, 208.7912060546875], [9, 91.67619812011719, 398.8509918212891, 206.26550598144533, 223.10350646972657], [9, 90.48559814453125, 403.61339172363284, 220.5778063964844, 237.41580688476563], [9, 91.67619812011719, 397.06509185791015, 234.89010681152345, 250.88620727539063], [9, 90.48559814453125, 402.4227917480469, 249.2024072265625, 264.35660766601563], [9, 90.48559814453125, 403.61339172363284, 263.51470764160155, 278.6689080810547], [9, 90.48559814453125, 401.23219177246096, 278.6689080810547, 292.98120849609376], [9, 92.86679809570313, 407.18519165039066, 292.98120849609376, 307.29350891113285], [9, 90.48559814453125, 411.3522915649414, 307.29350891113285, 320.76390930175785], [9, 90.48559814453125, 412.54289154052736, 321.6058093261719, 335.91810974121097], [9, 90.48559814453125, 413.1381915283203, 336.760009765625, 350.23041015625], [9, 90.48559814453125, 414.32879150390625, 351.0723101806641, 364.5427105712891], [9, 89.29499816894531, 415.5193914794922, 365.3846105957031, 379.6969110107422], [9, 89.29499816894531, 416.7099914550781, 379.6969110107422, 394.85111145019533], [9, 88.10439819335937, 417.90059143066406, 394.85111145019533, 410.00531188964845], [9, 88.10439819335937, 416.1146914672852, 409.16341186523437, 425.1595123291016], [9, 88.10439819335937, 421.4723913574219, 424.31761230468754, 440.3137127685547], [9, 88.10439819335937, 415.5193914794922, 439.47181274414066, 455.4679132080078], [9, 86.91379821777345, 425.0441912841797, 453.7841131591797, 471.464013671875], [9, 86.91379821777345, 426.8300912475586, 469.7802136230469, 487.46011413574223], [9, 86.91379821777345, 428.6159912109375, 484.9344140625, 505.1400146484375], [9, 85.72319824218751, 429.80659118652346, 501.77241455078126, 521.9780151367188], [9, 85.72319824218751, 431.59249114990234, 517.7685150146484, 539.6579156494141], [9, 85.72319824218751, 428.6159912109375, 534.6065155029297, 558.1797161865235], [9, 84.53259826660157, 436.3548910522461, 552.286416015625, 576.7015167236328], [9, 84.53259826660157, 432.7830911254883, 569.9663165283204, 596.0652172851562], [9, 84.53259826660157, 439.9266909790039, 587.6462170410157, 614.5870178222657], [9, 84.53259826660157, 441.71259094238286, 605.326117553711, 632.2669183349609], [9, 84.53259826660157, 443.49849090576174, 623.8479180908204, 648.2630187988282], [9, 251.21659484863284, 275.6238943481445, 658.3658190917969, 670.1524194335938], [10, 230.38109527587892, 296.45939392089844, 186.90180541992189, 200.3722058105469], [10, 107.15399780273438, 128.58479736328127, 202.056005859375, 211.31690612792968], [10, 202.99729583740236, 223.23749542236328, 202.056005859375, 212.15880615234377], [10, 344.08339294433597, 370.87189239501953, 207.94930603027345, 217.21020629882813], [10, 104.17749786376953, 246.45419494628908, 216.36830627441407, 226.47110656738283], [10, 104.17749786376953, 327.4149932861328, 230.68060668945313, 241.62530700683595], [10, 104.17749786376953, 415.5193914794922, 245.83480712890625, 256.7795074462891], [10, 104.17749786376953, 416.7099914550781, 260.9890075683594, 271.9337078857422], [10, 104.17749786376953, 426.23479125976564, 276.1432080078125, 286.2460083007813], [10, 104.17749786376953, 427.4253912353516, 291.29740844726564, 301.4002087402344], [10, 104.17749786376953, 425.0441912841797, 305.6097088623047, 315.71250915527344], [10, 104.17749786376953, 422.6629913330078, 319.92200927734376, 330.86670959472656], [10, 104.17749786376953, 432.18779113769534, 335.0762097167969, 346.0209100341797], [10, 104.17749786376953, 429.21129119873046, 349.388510131836, 360.33321044921877], [10, 104.17749786376953, 425.6394912719727, 364.5427105712891, 375.4874108886719], [10, 104.17749786376953, 435.75959106445316, 378.8550109863281, 390.641611328125], [10, 104.17749786376953, 330.3914932250977, 394.85111145019533, 405.79581176757813], [10, 104.17749786376953, 435.75959106445316, 409.16341186523437, 421.79191223144534], [10, 102.39159790039064, 441.71259094238286, 424.31761230468754, 437.7880126953125], [10, 101.79629791259767, 114.89289764404298, 448.73271301269534, 457.99361328125], [10, 101.79629791259767, 209.545595703125, 463.0450134277344, 474.83161376953126], [10, 102.39159790039064, 379.2060922241211, 473.98971374511723, 489.14391418457035], [10, 102.39159790039064, 159.54039672851565, 495.8791143798828, 506.8238146972656], [10, 278.0050942993164, 318.4854934692383, 524.503715209961, 535.4484155273437], [10, 328.60559326171875, 370.87189239501953, 542.1836157226562, 552.286416015625], [10, 270.8614944458008, 295.2687939453125, 680.2552197265625, 691.1999200439453]]
2026-08-10 14:58:40,826 INFO     29 [qwen-vl-text] ═══ DONE ═══ 99 positions, pages=3, time=69.1s
2026-08-10 14:58:40,826 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 14:58:40,833 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 14:58:40,834 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 14:58:40,834 INFO     29 [qwen-vl-text] positions(69): [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 14:58:40,834 INFO     29 [qwen-vl-text] page grouping: [11, 12], lines per page: [40, 29]
2026-08-10 14:58:41,188 INFO     29 [qwen-vl-text] page=11, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 14:58:41,353 INFO     29 [qwen-vl-text] page=12, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 14:58:41,354 INFO     29 [qwen-vl-text] LLM extraction start, text_len=2102
2026-08-10 14:58:41,354 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:58:41,355 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 331, \"bbox_end\": 399, \"encounter_dates\": [\"2025-07-08\", \"2025-07-14\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "出院记录\n姓名：\n科室：\n住院号：\n姓名：\n职业：自由职业\n性别：男\n入院日期：2025-7-8 09:23\n年龄：62岁\n出院日期：2025-7-14 10:00\n民族：汉族\n住院天数：6天\n籍贯：\n科 室：\n入院情况：\n患者 男，62岁，因“发现左肺占位3+月，诊断肠道肿瘤肺转移2+月”入院；患者3+月前因\n胸闷就诊于我院，行胸部CT提示：左肺上叶舌段周围型肺癌可能性大。后排除手术禁忌后于2025年4\n月16日行“肺穿刺活检”，病理结果提示：“左肺占位”恶性肿瘤，符合腺癌，结合免疫组化结果及\n临床病史考虑肠道来源。P53（突变型）、Syn（-）、TTF-1（+）、P63(-)、CK(AE1/AE3)\n(+)、Vimentin（-）、Villin（+）、CK7（局灶弱+）、CD56（-）、ALK（-）、Napsin-\nA（-）、P40(-)、CDX-2（+）、CK20（+）、Ki-67（30%+）、SATB2(+)、PCK5/6（-）。基因检测：\n1.KRAS基因突变；2.MYC基因扩增；3.APC基因突变。因患者为肠道肿瘤晚期且合并肺转移，可予患者\n行姑息性治疗，提高患者生存期，故排除化疗禁忌后于2025年5月12日至2025年6月22日完成1-3周期\n“FOLFOX+贝伐珠单抗”（奥沙利铂150mg+亚叶酸钙600mg+氟尿嘧啶4500mg+贝伐珠单抗400mg）\n联合治疗，现患者为按计划行下一周期治疗入院，门诊遂以“肠道肿瘤肺转移”收入我科。既往史：\n3+年前因“大便不成形伴血便”就诊于外院，考虑为“直肠癌”，未明确诊断，自行服用中药治疗；\n2+月前因“阴囊脓肿”于我院局麻下行“阴囊下部脓肿切开引流术”，病理结果回示：“阴囊内容\n物”检材大部分为变性坏死组织，区域见大量中性粒细胞浸润。予换药、抗感染等对症治疗后好转。\n专科情况：腹平软，全腹未见腹部静脉曲张、蜘蛛痣，未见胃肠型蠕动波。全腹无压痛、反跳痛及肌\n紧张，肝脾肋下未扪及，莫菲氏征阴性，移动性浊音阴性，双肾区无叩击痛，肠鸣音约4次/分，阴囊\n及肛周皮肤正常，未见红肿、破溃，肛周可扪及一约1*1cm大小包块，质韧，挤压时无明显脓液。辅\n助检查：病理（病理号：2502456）：“左肺占位”恶性肿瘤，符合腺癌，结合免疫组化结果及临床\n病史考虑肠道来源。CD56（-）、CDX-2（+）、CK7（局灶弱+）、ALK（-）、Ki-67（30%\n+）、P63(-)、SATB2(+)、CK20（+）、CK5/6（-）、Napsin-A（-）、P40(-)、P53（突变\n型）、Syn（-）、TTF-1（+）、CK(AE1/AE3)（+）、Vimentin（-）、Villin（+）。基因检测：\n1.KRAS基因突变；2.MYC基因扩增；3.APC基因突变。\n入院诊断：1.姑息性化疗；2.肠道肿瘤肺转移（T4bNxM1 IVa期）；3.肺气肿伴双肺肺大\n疱；4.混合痔；5.肝囊肿；6.双肺结节。\n诊疗经过：患者入院后积极完善相关辅助检查，血常规：中性粒细胞绝对值1.05*10\n第1页\n出院记录\n姓名：\n科室：\n住院号\n9/L↓，血红蛋白123.00g/L↓，白细胞计数3.16*10^9/L↓。肝肾功、电解质、心肌标\n记物及心肌酶谱均未见明显异常。入院时患者血常规提示白细胞稍低，考虑为化疗后骨\n髓抑制，予患者人粒细胞刺激因子对症治疗后复查血常规未见明显异常。因患者为肠道\n肿瘤晚期且合并肺转移，治疗方式以全身治疗为主的姑息治疗，以延长生命，改善生活\n质量为目的，目前患者已于我科完成3个周期“FOLFOX+贝伐珠单抗”方案治疗，查体可\n见阴囊处皮肤缺损已愈合，肛周肿块较前缩小，行局部疗效评估为PR，后续可继续该方\n案治疗，故排除化疗禁忌后于2025年7月9日至2025年7月13日行第4周期“FOLFOX+贝伐珠\n单抗”（奥沙利铂150mg+亚叶酸钙600mg+氟尿嘧啶4500mg+贝伐珠单抗400mg）方案\n治疗，患者化疗期间出现消化道反应，予止吐、抑酸等对症支持治疗后，消化道症状明\n显好转，复查血常规未见明显骨髓抑制，目前我科已无特殊治疗，请示上级医师后同意\n予患者今日出院。\n手术：无\n出院情况：患者无恶心、呕吐，未诉心慌、胸闷、气促、呼吸困难，无畏寒、发热，无\n腹胀、腹泻等特殊不适；精神、睡眠、饮食尚可，二便如常。查体：生命征平稳，一般\n情况可。心肺腹查体无特殊，专科查体同前。\n出院诊断：1.姑息性化疗；2.肠道肿瘤肺转移（T4bNxM1 IVa期）；3.肺气肿伴双肺肺\n大疱；4.混合痔；5.肝囊肿；6.双肺结节；7.化疗后骨髓抑制。\n出院医嘱：1.注意休息，多饮水，避免剧烈活动，注意加强营养；2.动态监测血常规\n（每周查血常规2次），监测肝功能每周1次，若有异常，及时就诊；3.间隔3周返院按计\n划行下一周期化疗；4.若出现畏寒、发热、乏力、心慌、胸闷等不适立即返院就诊；5.\n耳鼻喉科门诊随诊；6.不适我科随诊。\n康复指导：嘱患者适当活动，禁忌久卧\n医生签名：\n2025-7-14\n第2页",
    "role": "user"
  }
]
2026-08-10 14:58:41,357 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:58:41.356+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 64, "failed": 0, "current": {"7630dbd094ca11f1bd9827cf206dfa2d": {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:58:57,995 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:58:57,995 INFO     29 [qwen-vl-text] LLM output (len=3610):
{
  "encounter_date": "2025-07-14",
  "admission_date": "2025-07-08",
  "discharge_date": "2025-07-14",
  "hospital_days": 6,
  "department": null,
  "bed_number": null,
  "admission_condition": "患者 男，62岁，因“发现左肺占位3+月，诊断肠道肿瘤肺转移2+月”入院；患者3+月前因胸闷就诊于我院，行胸部CT提示：左肺上叶舌段周围型肺癌可能性大。后排除手术禁忌后于2025年4月16日行“肺穿刺活检”，病理结果提示：“左肺占位”恶性肿瘤，符合腺癌，结合免疫组化结果及临床病史考虑肠道来源。P53（突变型）、Syn（-）、TTF-1（+）、P63(-)、CK(AE1/AE3)(+)、Vimentin（-）、Villin（+）、CK7（局灶弱+）、CD56（-）、ALK（-）、Napsin-A（-）、P40(-)、CDX-2（+）、CK20（+）、Ki-67（30%+）、SATB2(+)、PCK5/6（-）。基因检测：1.KRAS基因突变；2.MYC基因扩增；3.APC基因突变。因患者为肠道肿瘤晚期且合并肺转移，可予患者行姑息性治疗，提高患者生存期，故排除化疗禁忌后于2025年5月12日至2025年6月22日完成1-3周期“FOLFOX+贝伐珠单抗”（奥沙利铂150mg+亚叶酸钙600mg+氟尿嘧啶4500mg+贝伐珠单抗400mg）联合治疗，现患者为按计划行下一周期治疗入院，门诊遂以“肠道肿瘤肺转移”收入我科。既往史：3+年前因“大便不成形伴血便”就诊于外院，考虑为“直肠癌”，未明确诊断，自行服用中药治疗；2+月前因“阴囊脓肿”于我院局麻下行“阴囊下部脓肿切开引流术”，病理结果回示：“阴囊内容物”检材大部分为变性坏死组织，区域见大量中性粒细胞浸润。予换药、抗感染等对症治疗后好转。专科情况：腹平软，全腹未见腹部静脉曲张、蜘蛛痣，未见胃肠型蠕动波。全腹无压痛、反跳痛及肌紧张，肝脾肋下未扪及，莫菲氏征阴性，移动性浊音阴性，双肾区无叩击痛，肠鸣音约4次/分，阴囊及肛周皮肤正常，未见红肿、破溃，肛周可扪及一约1*1cm大小包块，质韧，挤压时无明显脓液。",
  "admission_diagnoses": [
    {
      "name": "姑息性化疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "肠道肿瘤肺转移（T4bNxM1 IVa期）",
      "diagnosis_type": "西医"
    },
    {
      "name": "肺气肿伴双肺肺大疱",
      "diagnosis_type": "西医"
    },
    {
      "name": "混合痔",
      "diagnosis_type": "西医"
    },
    {
      "name": "肝囊肿",
      "diagnosis_type": "西医"
    },
    {
      "name": "双肺结节",
      "diagnosis_type": "西医"
    }
  ],
  "treatment_summary": "患者入院后积极完善相关辅助检查，血常规：中性粒细胞绝对值1.05*10^9/L↓，血红蛋白123.00g/L↓，白细胞计数3.16*10^9/L↓。肝肾功、电解质、心肌标记物及心肌酶谱均未见明显异常。入院时患者血常规提示白细胞稍低，考虑为化疗后骨髓抑制，予患者人粒细胞刺激因子对症治疗后复查血常规未见明显异常。因患者为肠道肿瘤晚期且合并肺转移，治疗方式以全身治疗为主的姑息治疗，以延长生命，改善生活质量为目的，目前患者已于我科完成3个周期“FOLFOX+贝伐珠单抗”方案治疗，查体可见阴囊处皮肤缺损已愈合，肛周肿块较前缩小，行局部疗效评估为PR，后续可继续该方案治疗，故排除化疗禁忌后于2025年7月9日至2025年7月13日行第4周期“FOLFOX+贝伐珠单抗”（奥沙利铂150mg+亚叶酸钙600mg+氟尿嘧啶4500mg+贝伐珠单抗400mg）方案治疗，患者化疗期间出现消化道反应，予止吐、抑酸等对症支持治疗后，消化道症状明显好转，复查血常规未见明显骨髓抑制，目前我科已无特殊治疗，请示上级医师后同意予患者今日出院。",
  "auxiliary_exams": "血常规：中性粒细胞绝对值1.05*10^9/L↓，血红蛋白123.00g/L↓，白细胞计数3.16*10^9/L↓。肝肾功、电解质、心肌标记物及心肌酶谱均未见明显异常。病理（病理号：2502456）：“左肺占位”恶性肿瘤，符合腺癌，结合免疫组化结果及临床病史考虑肠道来源。CD56（-）、CDX-2（+）、CK7（局灶弱+）、ALK（-）、Ki-67（30%+）、P63(-)、SATB2(+)、CK20（+）、CK5/6（-）、Napsin-A（-）、P40(-)、P53（突变型）、Syn（-）、TTF-1（+）、CK(AE1/AE3)（+）、Vimentin（-）、Villin（+）。基因检测：1.KRAS基因突变；2.MYC基因扩增；3.APC基因突变。",
  "imaging_findings": "胸部CT提示：左肺上叶舌段周围型肺癌可能性大。",
  "discharge_diagnoses": [
    {
      "name": "姑息性化疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "肠道肿瘤肺转移（T4bNxM1 IVa期）",
      "diagnosis_type": "西医"
    },
    {
      "name": "肺气肿伴双肺肺大疱",
      "diagnosis_type": "西医"
    },
    {
      "name": "混合痔",
      "diagnosis_type": "西医"
    },
    {
      "name": "肝囊肿",
      "diagnosis_type": "西医"
    },
    {
      "name": "双肺结节",
      "diagnosis_type": "西医"
    },
    {
      "name": "化疗后骨髓抑制",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": "患者无恶心、呕吐，未诉心慌、胸闷、气促、呼吸困难，无畏寒、发热，无腹胀、腹泻等特殊不适；精神、睡眠、饮食尚可，二便如常。查体：生命征平稳，一般情况可。心肺腹查体无特殊，专科查体同前。",
  "outcome": "好转",
  "discharge_orders": "1.注意休息，多饮水，避免剧烈活动，注意加强营养；2.动态监测血常规（每周查血常规2次），监测肝功能每周1次，若有异常，及时就诊；3.间隔3周返院按计划行下一周期化疗；4.若出现畏寒、发热、乏力、心慌、胸闷等不适立即返院就诊；5.耳鼻喉科门诊随诊；6.不适我科随诊。",
  "do_medications": [],
  "do_follow_up": "间隔3周返院按计划行下一周期化疗；耳鼻喉科门诊随诊；不适我科随诊。",
  "do_precautions": [
    "注意休息，多饮水，避免剧烈活动，注意加强营养",
    "动态监测血常规（每周查血常规2次），监测肝功能每周1次，若有异常，及时就诊",
    "若出现畏寒、发热、乏力、心慌、胸闷等不适立即返院就诊",
    "适当活动，禁忌久卧"
  ],
  "next_treatment_date": null,
  "attending_physician": null,
  "pe_ecog_score": null,
  "body_surface_area": null,
  "vs_temperature_c": null,
  "vs_pulse_bpm": null,
  "vs_respiration_rpm": null,
  "vs_systolic_bp_mmhg": null,
  "vs_diastolic_bp_mmhg": null
}
2026-08-10 14:58:57,995 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-07-14]
2026-08-10 14:58:58,002 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2254039, prompt_len=2018
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共40行）
["出院记录", "姓名：", "科室：", "住院号：", "姓名：", "职业：自由职业", "性别：男", "入院日期：2025-7-8 09:23", "年龄：62岁", "出院日期：2025-7-14 10:00", "民族：汉族", "住院天数：6天", "籍贯：", "科 室：", "入院情况：", "患者 男，62岁，因“发现左肺占位3+月，诊断肠道肿瘤肺转移2+月”入院；患者3+月前因", "胸闷就诊于我院，行胸部CT提示：左肺上叶舌段周围型肺癌可能性大。后排除手术禁忌后于2025年4", "月16日行“肺穿刺活检”，病理结果提示：“左肺占位”恶性肿瘤，符合腺癌，结合免疫组化结果及", "临床病史考虑肠道来源。P53（突变型）、Syn（-）、TTF-1（+）、P63(-)、CK(AE1/AE3)", "(+)、Vimentin（-）、Villin（+）、CK7（局灶弱+）、CD56（-）、ALK（-）、Napsin-", "A（-）、P40(-)、CDX-2（+）、CK20（+）、Ki-67（30%+）、SATB2(+)、PCK5/6（-）。基因检测：", "1.KRAS基因突变；2.MYC基因扩增；3.APC基因突变。因患者为肠道肿瘤晚期且合并肺转移，可予患者", "行姑息性治疗，提高患者生存期，故排除化疗禁忌后于2025年5月12日至2025年6月22日完成1-3周期", "“FOLFOX+贝伐珠单抗”（奥沙利铂150mg+亚叶酸钙600mg+氟尿嘧啶4500mg+贝伐珠单抗400mg）", "联合治疗，现患者为按计划行下一周期治疗入院，门诊遂以“肠道肿瘤肺转移”收入我科。既往史：", "3+年前因“大便不成形伴血便”就诊于外院，考虑为“直肠癌”，未明确诊断，自行服用中药治疗；", "2+月前因“阴囊脓肿”于我院局麻下行“阴囊下部脓肿切开引流术”，病理结果回示：“阴囊内容", "物”检材大部分为变性坏死组织，区域见大量中性粒细胞浸润。予换药、抗感染等对症治疗后好转。", "专科情况：腹平软，全腹未见腹部静脉曲张、蜘蛛痣，未见胃肠型蠕动波。全腹无压痛、反跳痛及肌", "紧张，肝脾肋下未扪及，莫菲氏征阴性，移动性浊音阴性，双肾区无叩击痛，肠鸣音约4次/分，阴囊", "及肛周皮肤正常，未见红肿、破溃，肛周可扪及一约1*1cm大小包块，质韧，挤压时无明显脓液。辅", "助检查：病理（病理号：2502456）：“左肺占位”恶性肿瘤，符合腺癌，结合免疫组化结果及临床", "病史考虑肠道来源。CD56（-）、CDX-2（+）、CK7（局灶弱+）、ALK（-）、Ki-67（30%", "+）、P63(-)、SATB2(+)、CK20（+）、CK5/6（-）、Napsin-A（-）、P40(-)、P53（突变", "型）、Syn（-）、TTF-1（+）、CK(AE1/AE3)（+）、Vimentin（-）、Villin（+）。基因检测：", "1.KRAS基因突变；2.MYC基因扩增；3.APC基因突变。", "入院诊断：1.姑息性化疗；2.肠道肿瘤肺转移（T4bNxM1 IVa期）；3.肺气肿伴双肺肺大", "疱；4.混合痔；5.肝囊肿；6.双肺结节。", "诊疗经过：患者入院后积极完善相关辅助检查，血常规：中性粒细胞绝对值1.05*10", "第1页"]

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
2026-08-10 14:59:15,144 INFO     29 [qwen-vl-text] coord API raw response (len=3048):
[
	{"text": "出院记录", "bbox": [432, 160, 547, 178]},
	{"text": "姓名：", "bbox": [220, 176, 258, 188]},
	{"text": "科室：", "bbox": [383, 180, 419, 191]},
	{"text": "住院号：", "bbox": [630, 186, 678, 197]},
	{"text": "姓名：", "bbox": [220, 194, 258, 206]},
	{"text": "职业：自由职业", "bbox": [492, 202, 626, 214]},
	{"text": "性别：男", "bbox": [220, 212, 300, 224]},
	{"text": "入院日期：2025-7-8 09:23", "bbox": [492, 220, 669, 233]},
	{"text": "年龄：62岁", "bbox": [220, 230, 322, 243]},
	{"text": "出院日期：2025-7-14 10:00", "bbox": [492, 238, 676, 251]},
	{"text": "民族：汉族", "bbox": [220, 248, 315, 261]},
	{"text": "住院天数：6天", "bbox": [492, 256, 605, 269]},
	{"text": "籍贯：", "bbox": [218, 266, 254, 278]},
	{"text": "科 室：", "bbox": [492, 274, 554, 287]},
	{"text": "入院情况：", "bbox": [214, 284, 280, 296]},
	{"text": "患者 男，62岁，因“发现左肺占位3+月，诊断肠道肿瘤肺转移2+月”入院；患者3+月前因", "bbox": [211, 302, 768, 320]},
	{"text": "胸闷就诊于我院，行胸部CT提示：左肺上叶舌段周围型肺癌可能性大。后排除手术禁忌后于2025年4", "bbox": [211, 319, 768, 338]},
	{"text": "月16日行“肺穿刺活检”，病理结果提示：“左肺占位”恶性肿瘤，符合腺癌，结合免疫组化结果及", "bbox": [211, 337, 773, 355]},
	{"text": "临床病史考虑肠道来源。P53（突变型）、Syn（-）、TTF-1（+）、P63(-)、CK(AE1/AE3)", "bbox": [211, 355, 709, 372]},
	{"text": "(+)、Vimentin（-）、Villin（+）、CK7（局灶弱+）、CD56（-）、ALK（-）、Napsin-", "bbox": [218, 372, 717, 389]},
	{"text": "A（-）、P40(-)、CDX-2（+）、CK20（+）、Ki-67（30%+）、SATB2(+)、PCK5/6（-）。基因检测：", "bbox": [211, 389, 759, 405]},
	{"text": "1.KRAS基因突变；2.MYC基因扩增；3.APC基因突变。因患者为肠道肿瘤晚期且合并肺转移，可予患者", "bbox": [211, 406, 773, 422]},
	{"text": "行姑息性治疗，提高患者生存期，故排除化疗禁忌后于2025年5月12日至2025年6月22日完成1-3周期", "bbox": [210, 422, 771, 438]},
	{"text": "“FOLFOX+贝伐珠单抗”（奥沙利铂150mg+亚叶酸钙600mg+氟尿嘧啶4500mg+贝伐珠单抗400mg）", "bbox": [211, 439, 768, 455]},
	{"text": "联合治疗，现患者为按计划行下一周期治疗入院，门诊遂以“肠道肿瘤肺转移”收入我科。既往史：", "bbox": [204, 456, 775, 471]},
	{"text": "3+年前因“大便不成形伴血便”就诊于外院，考虑为“直肠癌”，未明确诊断，自行服用中药治疗；", "bbox": [201, 473, 777, 488]},
	{"text": "2+月前因“阴囊脓肿”于我院局麻下行“阴囊下部脓肿切开引流术”，病理结果回示：“阴囊内容", "bbox": [200, 490, 775, 505]},
	{"text": "物”检材大部分为变性坏死组织，区域见大量中性粒细胞浸润。予换药、抗感染等对症治疗后好转。", "bbox": [198, 508, 784, 522]},
	{"text": "专科情况：腹平软，全腹未见腹部静脉曲张、蜘蛛痣，未见胃肠型蠕动波。全腹无压痛、反跳痛及肌", "bbox": [197, 525, 793, 539]},
	{"text": "紧张，肝脾肋下未扪及，莫菲氏征阴性，移动性浊音阴性，双肾区无叩击痛，肠鸣音约4次/分，阴囊", "bbox": [196, 543, 795, 557]},
	{"text": "及肛周皮肤正常，未见红肿、破溃，肛周可扪及一约1*1cm大小包块，质韧，挤压时无明显脓液。辅", "bbox": [194, 561, 791, 576]},
	{"text": "助检查：病理（病理号：2502456）：“左肺占位”恶性肿瘤，符合腺癌，结合免疫组化结果及临床", "bbox": [192, 579, 793, 594]},
	{"text": "病史考虑肠道来源。CD56（-）、CDX-2（+）、CK7（局灶弱+）、ALK（-）、Ki-67（30%", "bbox": [191, 598, 729, 614]},
	{"text": "+）、P63(-)、SATB2(+)、CK20（+）、CK5/6（-）、Napsin-A（-）、P40(-)、P53（突变", "bbox": [190, 618, 736, 635]},
	{"text": "型）、Syn（-）、TTF-1（+）、CK(AE1/AE3)（+）、Vimentin（-）、Villin（+）。基因检测：", "bbox": [190, 638, 770, 655]},
	{"text": "1.KRAS基因突变；2.MYC基因扩增；3.APC基因突变。", "bbox": [190, 659, 508, 675]},
	{"text": "入院诊断：1.姑息性化疗；2.肠道肿瘤肺转移（T4bNxM1 IVa期）；3.肺气肿伴双肺肺大", "bbox": [187, 678, 797, 696]},
	{"text": "疱；4.混合痔；5.肝囊肿；6.双肺结节。", "bbox": [187, 702, 473, 718]},
	{"text": "诊疗经过：患者入院后积极完善相关辅助检查，血常规：中性粒细胞绝对值1.05*10", "bbox": [187, 721, 778, 738]},
	{"text": "第1页", "bbox": [472, 745, 512, 758]}
]
2026-08-10 14:59:15,144 INFO     29 [qwen-vl-text] coord API: raw_items=40, valid_items=40, elapsed=17.1s
2026-08-10 14:59:15,144 INFO     29 [qwen-vl-text] coord item[0]: text=出院记录, bbox=[432, 160, 547, 178]
2026-08-10 14:59:15,144 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[220, 176, 258, 188]
2026-08-10 14:59:15,144 INFO     29 [qwen-vl-text] coord item[2]: text=科室：, bbox=[383, 180, 419, 191]
2026-08-10 14:59:15,144 INFO     29 [qwen-vl-text] coord item[3]: text=住院号：, bbox=[630, 186, 678, 197]
2026-08-10 14:59:15,144 INFO     29 [qwen-vl-text] coord item[4]: text=姓名：, bbox=[220, 194, 258, 206]
2026-08-10 14:59:15,144 INFO     29 [qwen-vl-text] coord item[5]: text=职业：自由职业, bbox=[492, 202, 626, 214]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[6]: text=性别：男, bbox=[220, 212, 300, 224]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[7]: text=入院日期：2025-7-8 09:23, bbox=[492, 220, 669, 233]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[8]: text=年龄：62岁, bbox=[220, 230, 322, 243]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[9]: text=出院日期：2025-7-14 10:00, bbox=[492, 238, 676, 251]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[10]: text=民族：汉族, bbox=[220, 248, 315, 261]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[11]: text=住院天数：6天, bbox=[492, 256, 605, 269]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[12]: text=籍贯：, bbox=[218, 266, 254, 278]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[13]: text=科 室：, bbox=[492, 274, 554, 287]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[14]: text=入院情况：, bbox=[214, 284, 280, 296]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[15]: text=患者 男，62岁，因“发现左肺占位3+月，诊断肠道肿瘤肺转移2+月”入院；患者3+月前因, bbox=[211, 302, 768, 320]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[16]: text=胸闷就诊于我院，行胸部CT提示：左肺上叶舌段周围型肺癌可能性大。后排除手术禁忌后于2025年4, bbox=[211, 319, 768, 338]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[17]: text=月16日行“肺穿刺活检”，病理结果提示：“左肺占位”恶性肿瘤，符合腺癌，结合免疫组化结果及, bbox=[211, 337, 773, 355]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[18]: text=临床病史考虑肠道来源。P53（突变型）、Syn（-）、TTF-1（+）、P63(-)、CK(AE1/AE3), bbox=[211, 355, 709, 372]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[19]: text=(+)、Vimentin（-）、Villin（+）、CK7（局灶弱+）、CD56（-）、ALK（-）、Napsin-, bbox=[218, 372, 717, 389]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[20]: text=A（-）、P40(-)、CDX-2（+）、CK20（+）、Ki-67（30%+）、SATB2(+)、PCK5/6（-）。基因检测：, bbox=[211, 389, 759, 405]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[21]: text=1.KRAS基因突变；2.MYC基因扩增；3.APC基因突变。因患者为肠道肿瘤晚期且合并肺转移，可予患者, bbox=[211, 406, 773, 422]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[22]: text=行姑息性治疗，提高患者生存期，故排除化疗禁忌后于2025年5月12日至2025年6月22日完成1-3周期, bbox=[210, 422, 771, 438]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[23]: text=“FOLFOX+贝伐珠单抗”（奥沙利铂150mg+亚叶酸钙600mg+氟尿嘧啶4500mg+贝伐珠单抗400mg）, bbox=[211, 439, 768, 455]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[24]: text=联合治疗，现患者为按计划行下一周期治疗入院，门诊遂以“肠道肿瘤肺转移”收入我科。既往史：, bbox=[204, 456, 775, 471]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[25]: text=3+年前因“大便不成形伴血便”就诊于外院，考虑为“直肠癌”，未明确诊断，自行服用中药治疗；, bbox=[201, 473, 777, 488]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[26]: text=2+月前因“阴囊脓肿”于我院局麻下行“阴囊下部脓肿切开引流术”，病理结果回示：“阴囊内容, bbox=[200, 490, 775, 505]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[27]: text=物”检材大部分为变性坏死组织，区域见大量中性粒细胞浸润。予换药、抗感染等对症治疗后好转。, bbox=[198, 508, 784, 522]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[28]: text=专科情况：腹平软，全腹未见腹部静脉曲张、蜘蛛痣，未见胃肠型蠕动波。全腹无压痛、反跳痛及肌, bbox=[197, 525, 793, 539]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[29]: text=紧张，肝脾肋下未扪及，莫菲氏征阴性，移动性浊音阴性，双肾区无叩击痛，肠鸣音约4次/分，阴囊, bbox=[196, 543, 795, 557]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[30]: text=及肛周皮肤正常，未见红肿、破溃，肛周可扪及一约1*1cm大小包块，质韧，挤压时无明显脓液。辅, bbox=[194, 561, 791, 576]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[31]: text=助检查：病理（病理号：2502456）：“左肺占位”恶性肿瘤，符合腺癌，结合免疫组化结果及临床, bbox=[192, 579, 793, 594]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[32]: text=病史考虑肠道来源。CD56（-）、CDX-2（+）、CK7（局灶弱+）、ALK（-）、Ki-67（30%, bbox=[191, 598, 729, 614]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[33]: text=+）、P63(-)、SATB2(+)、CK20（+）、CK5/6（-）、Napsin-A（-）、P40(-)、P53（突变, bbox=[190, 618, 736, 635]
2026-08-10 14:59:15,145 INFO     29 [qwen-vl-text] coord item[34]: text=型）、Syn（-）、TTF-1（+）、CK(AE1/AE3)（+）、Vimentin（-）、Villin（+）。基因检测：, bbox=[190, 638, 770, 655]
2026-08-10 14:59:15,146 INFO     29 [qwen-vl-text] coord item[35]: text=1.KRAS基因突变；2.MYC基因扩增；3.APC基因突变。, bbox=[190, 659, 508, 675]
2026-08-10 14:59:15,146 INFO     29 [qwen-vl-text] coord item[36]: text=入院诊断：1.姑息性化疗；2.肠道肿瘤肺转移（T4bNxM1 IVa期）；3.肺气肿伴双肺肺大, bbox=[187, 678, 797, 696]
2026-08-10 14:59:15,146 INFO     29 [qwen-vl-text] coord item[37]: text=疱；4.混合痔；5.肝囊肿；6.双肺结节。, bbox=[187, 702, 473, 718]
2026-08-10 14:59:15,146 INFO     29 [qwen-vl-text] coord item[38]: text=诊疗经过：患者入院后积极完善相关辅助检查，血常规：中性粒细胞绝对值1.05*10, bbox=[187, 721, 778, 738]
2026-08-10 14:59:15,146 INFO     29 [qwen-vl-text] coord item[39]: text=第1页, bbox=[472, 745, 512, 758]
2026-08-10 14:59:15,146 INFO     29 [qwen-vl-text] page=11 — 40/40 coords, api_time=17.1s
2026-08-10 14:59:15,148 INFO     29 [qwen-vl-text] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1204025, prompt_len=1516
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共29行）
["出院记录", "姓名：", "科室：", "住院号", "9/L↓，血红蛋白123.00g/L↓，白细胞计数3.16*10^9/L↓。肝肾功、电解质、心肌标", "记物及心肌酶谱均未见明显异常。入院时患者血常规提示白细胞稍低，考虑为化疗后骨", "髓抑制，予患者人粒细胞刺激因子对症治疗后复查血常规未见明显异常。因患者为肠道", "肿瘤晚期且合并肺转移，治疗方式以全身治疗为主的姑息治疗，以延长生命，改善生活", "质量为目的，目前患者已于我科完成3个周期“FOLFOX+贝伐珠单抗”方案治疗，查体可", "见阴囊处皮肤缺损已愈合，肛周肿块较前缩小，行局部疗效评估为PR，后续可继续该方", "案治疗，故排除化疗禁忌后于2025年7月9日至2025年7月13日行第4周期“FOLFOX+贝伐珠", "单抗”（奥沙利铂150mg+亚叶酸钙600mg+氟尿嘧啶4500mg+贝伐珠单抗400mg）方案", "治疗，患者化疗期间出现消化道反应，予止吐、抑酸等对症支持治疗后，消化道症状明", "显好转，复查血常规未见明显骨髓抑制，目前我科已无特殊治疗，请示上级医师后同意", "予患者今日出院。", "手术：无", "出院情况：患者无恶心、呕吐，未诉心慌、胸闷、气促、呼吸困难，无畏寒、发热，无", "腹胀、腹泻等特殊不适；精神、睡眠、饮食尚可，二便如常。查体：生命征平稳，一般", "情况可。心肺腹查体无特殊，专科查体同前。", "出院诊断：1.姑息性化疗；2.肠道肿瘤肺转移（T4bNxM1 IVa期）；3.肺气肿伴双肺肺", "大疱；4.混合痔；5.肝囊肿；6.双肺结节；7.化疗后骨髓抑制。", "出院医嘱：1.注意休息，多饮水，避免剧烈活动，注意加强营养；2.动态监测血常规", "（每周查血常规2次），监测肝功能每周1次，若有异常，及时就诊；3.间隔3周返院按计", "划行下一周期化疗；4.若出现畏寒、发热、乏力、心慌、胸闷等不适立即返院就诊；5.", "耳鼻喉科门诊随诊；6.不适我科随诊。", "康复指导：嘱患者适当活动，禁忌久卧", "医生签名：", "2025-7-14", "第2页"]

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
2026-08-10 14:59:28,299 INFO     29 [qwen-vl-text] coord API raw response (len=2095):
[
	{"text": "出院记录", "bbox": [436, 143, 566, 160]},
	{"text": "姓名：", "bbox": [207, 166, 245, 178]},
	{"text": "科室：", "bbox": [379, 168, 418, 180]},
	{"text": "住院号", "bbox": [664, 169, 714, 181]},
	{"text": "9/L↓，血红蛋白123.00g/L↓，白细胞计数3.16*10^9/L↓。肝肾功、电解质、心肌标", "bbox": [198, 186, 832, 206]},
	{"text": "记物及心肌酶谱均未见明显异常。入院时患者血常规提示白细胞稍低，考虑为化疗后骨", "bbox": [197, 205, 820, 228]},
	{"text": "髓抑制，予患者人粒细胞刺激因子对症治疗后复查血常规未见明显异常。因患者为肠道", "bbox": [195, 225, 819, 249]},
	{"text": "肿瘤晚期且合并肺转移，治疗方式以全身治疗为主的姑息治疗，以延长生命，改善生活", "bbox": [192, 245, 817, 270]},
	{"text": "质量为目的，目前患者已于我科完成3个周期“FOLFOX+贝伐珠单抗”方案治疗，查体可", "bbox": [190, 265, 814, 291]},
	{"text": "见阴囊处皮肤缺损已愈合，肛周肿块较前缩小，行局部疗效评估为PR，后续可继续该方", "bbox": [190, 286, 812, 313]},
	{"text": "案治疗，故排除化疗禁忌后于2025年7月9日至2025年7月13日行第4周期“FOLFOX+贝伐珠", "bbox": [188, 306, 817, 335]},
	{"text": "单抗”（奥沙利铂150mg+亚叶酸钙600mg+氟尿嘧啶4500mg+贝伐珠单抗400mg）方案", "bbox": [187, 327, 806, 357]},
	{"text": "治疗，患者化疗期间出现消化道反应，予止吐、抑酸等对症支持治疗后，消化道症状明", "bbox": [186, 348, 802, 378]},
	{"text": "显好转，复查血常规未见明显骨髓抑制，目前我科已无特殊治疗，请示上级医师后同意", "bbox": [186, 369, 800, 399]},
	{"text": "予患者今日出院。", "bbox": [188, 389, 305, 404]},
	{"text": "手术：无", "bbox": [188, 409, 275, 423]},
	{"text": "出院情况：患者无恶心、呕吐，未诉心慌、胸闷、气促、呼吸困难，无畏寒、发热，无", "bbox": [183, 428, 790, 460]},
	{"text": "腹胀、腹泻等特殊不适；精神、睡眠、饮食尚可，二便如常。查体：生命征平稳，一般", "bbox": [177, 448, 797, 481]},
	{"text": "情况可。心肺腹查体无特殊，专科查体同前。", "bbox": [174, 468, 492, 490]},
	{"text": "出院诊断：1.姑息性化疗；2.肠道肿瘤肺转移（T4bNxM1 IVa期）；3.肺气肿伴双肺肺", "bbox": [170, 488, 790, 521]},
	{"text": "大疱；4.混合痔；5.肝囊肿；6.双肺结节；7.化疗后骨髓抑制。", "bbox": [167, 509, 620, 536]},
	{"text": "出院医嘱：1.注意休息，多饮水，避免剧烈活动，注意加强营养；2.动态监测血常规", "bbox": [165, 530, 781, 565]},
	{"text": "（每周查血常规2次），监测肝功能每周1次，若有异常，及时就诊；3.间隔3周返院按计", "bbox": [168, 552, 802, 588]},
	{"text": "划行下一周期化疗；4.若出现畏寒、发热、乏力、心慌、胸闷等不适立即返院就诊；5.", "bbox": [158, 574, 791, 609]},
	{"text": "耳鼻喉科门诊随诊；6.不适我科随诊。", "bbox": [157, 595, 433, 618]},
	{"text": "康复指导：嘱患者适当活动，禁忌久卧", "bbox": [159, 617, 445, 635]},
	{"text": "医生签名：", "bbox": [467, 692, 539, 708]},
	{"text": "2025-7-14", "bbox": [555, 718, 634, 733]},
	{"text": "第2页", "bbox": [438, 787, 479, 800]}
]
2026-08-10 14:59:28,300 INFO     29 [qwen-vl-text] coord API: raw_items=29, valid_items=29, elapsed=13.2s
2026-08-10 14:59:28,300 INFO     29 [qwen-vl-text] coord item[0]: text=出院记录, bbox=[436, 143, 566, 160]
2026-08-10 14:59:28,300 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[207, 166, 245, 178]
2026-08-10 14:59:28,300 INFO     29 [qwen-vl-text] coord item[2]: text=科室：, bbox=[379, 168, 418, 180]
2026-08-10 14:59:28,300 INFO     29 [qwen-vl-text] coord item[3]: text=住院号, bbox=[664, 169, 714, 181]
2026-08-10 14:59:28,300 INFO     29 [qwen-vl-text] coord item[4]: text=9/L↓，血红蛋白123.00g/L↓，白细胞计数3.16*10^9/L↓。肝肾功、电解质、心肌标, bbox=[198, 186, 832, 206]
2026-08-10 14:59:28,300 INFO     29 [qwen-vl-text] coord item[5]: text=记物及心肌酶谱均未见明显异常。入院时患者血常规提示白细胞稍低，考虑为化疗后骨, bbox=[197, 205, 820, 228]
2026-08-10 14:59:28,300 INFO     29 [qwen-vl-text] coord item[6]: text=髓抑制，予患者人粒细胞刺激因子对症治疗后复查血常规未见明显异常。因患者为肠道, bbox=[195, 225, 819, 249]
2026-08-10 14:59:28,300 INFO     29 [qwen-vl-text] coord item[7]: text=肿瘤晚期且合并肺转移，治疗方式以全身治疗为主的姑息治疗，以延长生命，改善生活, bbox=[192, 245, 817, 270]
2026-08-10 14:59:28,300 INFO     29 [qwen-vl-text] coord item[8]: text=质量为目的，目前患者已于我科完成3个周期“FOLFOX+贝伐珠单抗”方案治疗，查体可, bbox=[190, 265, 814, 291]
2026-08-10 14:59:28,300 INFO     29 [qwen-vl-text] coord item[9]: text=见阴囊处皮肤缺损已愈合，肛周肿块较前缩小，行局部疗效评估为PR，后续可继续该方, bbox=[190, 286, 812, 313]
2026-08-10 14:59:28,300 INFO     29 [qwen-vl-text] coord item[10]: text=案治疗，故排除化疗禁忌后于2025年7月9日至2025年7月13日行第4周期“FOLFOX+贝伐珠, bbox=[188, 306, 817, 335]
2026-08-10 14:59:28,300 INFO     29 [qwen-vl-text] coord item[11]: text=单抗”（奥沙利铂150mg+亚叶酸钙600mg+氟尿嘧啶4500mg+贝伐珠单抗400mg）方案, bbox=[187, 327, 806, 357]
2026-08-10 14:59:28,300 INFO     29 [qwen-vl-text] coord item[12]: text=治疗，患者化疗期间出现消化道反应，予止吐、抑酸等对症支持治疗后，消化道症状明, bbox=[186, 348, 802, 378]
2026-08-10 14:59:28,300 INFO     29 [qwen-vl-text] coord item[13]: text=显好转，复查血常规未见明显骨髓抑制，目前我科已无特殊治疗，请示上级医师后同意, bbox=[186, 369, 800, 399]
2026-08-10 14:59:28,300 INFO     29 [qwen-vl-text] coord item[14]: text=予患者今日出院。, bbox=[188, 389, 305, 404]
2026-08-10 14:59:28,300 INFO     29 [qwen-vl-text] coord item[15]: text=手术：无, bbox=[188, 409, 275, 423]
2026-08-10 14:59:28,301 INFO     29 [qwen-vl-text] coord item[16]: text=出院情况：患者无恶心、呕吐，未诉心慌、胸闷、气促、呼吸困难，无畏寒、发热，无, bbox=[183, 428, 790, 460]
2026-08-10 14:59:28,301 INFO     29 [qwen-vl-text] coord item[17]: text=腹胀、腹泻等特殊不适；精神、睡眠、饮食尚可，二便如常。查体：生命征平稳，一般, bbox=[177, 448, 797, 481]
2026-08-10 14:59:28,301 INFO     29 [qwen-vl-text] coord item[18]: text=情况可。心肺腹查体无特殊，专科查体同前。, bbox=[174, 468, 492, 490]
2026-08-10 14:59:28,301 INFO     29 [qwen-vl-text] coord item[19]: text=出院诊断：1.姑息性化疗；2.肠道肿瘤肺转移（T4bNxM1 IVa期）；3.肺气肿伴双肺肺, bbox=[170, 488, 790, 521]
2026-08-10 14:59:28,301 INFO     29 [qwen-vl-text] coord item[20]: text=大疱；4.混合痔；5.肝囊肿；6.双肺结节；7.化疗后骨髓抑制。, bbox=[167, 509, 620, 536]
2026-08-10 14:59:28,301 INFO     29 [qwen-vl-text] coord item[21]: text=出院医嘱：1.注意休息，多饮水，避免剧烈活动，注意加强营养；2.动态监测血常规, bbox=[165, 530, 781, 565]
2026-08-10 14:59:28,301 INFO     29 [qwen-vl-text] coord item[22]: text=（每周查血常规2次），监测肝功能每周1次，若有异常，及时就诊；3.间隔3周返院按计, bbox=[168, 552, 802, 588]
2026-08-10 14:59:28,301 INFO     29 [qwen-vl-text] coord item[23]: text=划行下一周期化疗；4.若出现畏寒、发热、乏力、心慌、胸闷等不适立即返院就诊；5., bbox=[158, 574, 791, 609]
2026-08-10 14:59:28,301 INFO     29 [qwen-vl-text] coord item[24]: text=耳鼻喉科门诊随诊；6.不适我科随诊。, bbox=[157, 595, 433, 618]
2026-08-10 14:59:28,301 INFO     29 [qwen-vl-text] coord item[25]: text=康复指导：嘱患者适当活动，禁忌久卧, bbox=[159, 617, 445, 635]
2026-08-10 14:59:28,301 INFO     29 [qwen-vl-text] coord item[26]: text=医生签名：, bbox=[467, 692, 539, 708]
2026-08-10 14:59:28,301 INFO     29 [qwen-vl-text] coord item[27]: text=2025-7-14, bbox=[555, 718, 634, 733]
2026-08-10 14:59:28,301 INFO     29 [qwen-vl-text] coord item[28]: text=第2页, bbox=[438, 787, 479, 800]
2026-08-10 14:59:28,302 INFO     29 [qwen-vl-text] page=12 — 29/29 coords, api_time=13.2s
2026-08-10 14:59:28,302 INFO     29 [qwen-vl-text] new_positions (69):
[[11, 257.16959472656254, 325.62909332275393, 134.70400390625, 149.85820434570314], [11, 130.96599731445312, 153.58739685058595, 148.174404296875, 158.27720458984376], [11, 227.99989532470704, 249.43069488525393, 151.54200439453126, 160.80290466308594], [11, 375.03899230957035, 403.61339172363284, 156.59340454101564, 165.85430480957032], [11, 130.96599731445312, 153.58739685058595, 163.32860473632812, 173.43140502929688], [11, 292.8875939941406, 372.65779235839847, 170.06380493164062, 180.16660522460938], [11, 130.96599731445312, 178.58999633789062, 178.48280517578127, 188.58560546875], [11, 292.8875939941406, 398.2556918334961, 185.21800537109377, 196.16270568847656], [11, 130.96599731445312, 191.68659606933593, 193.6370056152344, 204.58170593261718], [11, 292.8875939941406, 402.4227917480469, 200.3722058105469, 211.31690612792968], [11, 130.96599731445312, 187.51949615478517, 208.7912060546875, 219.73590637207033], [11, 292.8875939941406, 360.1564926147461, 215.52640625, 226.47110656738283], [11, 129.77539733886718, 151.20619689941407, 223.94540649414063, 234.0482067871094], [11, 292.8875939941406, 329.7961932373047, 230.68060668945313, 241.62530700683595], [11, 127.39419738769531, 166.68399658203126, 239.09960693359375, 249.2024072265625], [11, 125.60829742431642, 457.190390625, 254.2538073730469, 269.4080078125], [11, 125.60829742431642, 457.190390625, 268.56610778808596, 284.5622082519531], [11, 125.60829742431642, 460.16689056396484, 283.7203082275391, 298.8745086669922], [11, 125.60829742431642, 422.0676913452149, 298.8745086669922, 313.1868090820313], [11, 129.77539733886718, 426.8300912475586, 313.1868090820313, 327.4991094970703], [11, 125.60829742431642, 451.8326907348633, 327.4991094970703, 340.9695098876953], [11, 125.60829742431642, 460.16689056396484, 341.8114099121094, 355.2818103027344], [11, 125.01299743652345, 458.9762905883789, 355.2818103027344, 368.7522106933594], [11, 125.60829742431642, 457.190390625, 369.59411071777345, 383.06451110839845], [11, 121.44119750976563, 461.3574905395508, 383.90641113281254, 396.53491149902345], [11, 119.65529754638672, 462.5480905151367, 398.21871154785157, 410.84721191406254], [11, 119.05999755859375, 461.3574905395508, 412.53101196289066, 425.1595123291016], [11, 117.86939758300782, 466.71519042968754, 427.6852124023438, 439.47181274414066], [11, 117.27409759521485, 472.07289031982424, 441.9975128173828, 453.7841131591797], [11, 116.67879760742188, 473.2634902954102, 457.15171325683593, 468.9383135986328], [11, 115.48819763183594, 470.8822903442383, 472.30591369628905, 484.9344140625], [11, 114.29759765625, 472.07289031982424, 487.46011413574223, 500.08861450195315], [11, 113.70229766845704, 433.9736911010742, 503.4562145996094, 516.9266149902344], [11, 113.10699768066407, 438.14079101562504, 520.2942150878906, 534.6065155029297], [11, 113.10699768066407, 458.38099060058596, 537.1322155761719, 551.444515991211], [11, 113.10699768066407, 302.41239379882813, 554.8121160888672, 568.2825164794922], [11, 111.32109771728516, 474.4540902709961, 570.8082165527344, 585.9624169921875], [11, 111.32109771728516, 281.5768942260742, 591.0138171386719, 604.4842175292969], [11, 111.32109771728516, 463.1433905029297, 607.0099176025391, 621.3222180175782], [11, 280.9815942382813, 304.79359375, 627.2155181884766, 638.1602185058593], [12, 259.55079467773436, 336.93979309082033, 120.39170349121095, 134.70400390625], [12, 123.22709747314454, 145.84849700927734, 139.75540405273438, 149.85820434570314], [12, 225.61869537353516, 248.83539489746096, 141.4392041015625, 151.54200439453126], [12, 395.27919189453127, 425.0441912841797, 142.28110412597655, 152.38390441894532], [12, 117.86939758300782, 495.28958984375004, 156.59340454101564, 173.43140502929688], [12, 117.27409759521485, 488.1459899902344, 172.58950500488282, 191.95320556640627], [12, 116.08349761962891, 487.55069000244146, 189.42750549316406, 209.63310607910157], [12, 114.29759765625, 486.3600900268555, 206.26550598144533, 227.3130065917969], [12, 113.10699768066407, 484.5741900634766, 223.10350646972657, 244.9929071044922], [12, 113.10699768066407, 483.38359008789064, 240.7834069824219, 263.51470764160155], [12, 111.91639770507813, 486.3600900268555, 257.62140747070316, 282.03650817871096], [12, 111.32109771728516, 479.8117901611328, 275.30130798339843, 300.5583087158203], [12, 110.72579772949219, 477.43059020996094, 292.98120849609376, 318.23820922851564], [12, 110.72579772949219, 476.239990234375, 310.6611090087891, 335.91810974121097], [12, 111.91639770507813, 181.56649627685547, 327.4991094970703, 340.12760986328124], [12, 111.91639770507813, 163.7074966430664, 344.33710998535156, 356.12371032714844], [12, 108.93989776611329, 470.28699035644536, 360.33321044921877, 387.2740112304688], [12, 105.36809783935547, 474.4540902709961, 377.1712109375, 404.9539117431641], [12, 103.58219787597656, 292.8875939941406, 394.00921142578125, 412.53101196289066], [12, 101.2009979248047, 470.28699035644536, 410.84721191406254, 438.6299127197266], [12, 99.41509796142579, 369.08599243164065, 428.5271124267578, 451.2584130859375], [12, 98.22449798583985, 464.9292904663086, 446.20701293945314, 475.67351379394535], [12, 100.01039794921876, 477.43059020996094, 464.7288134765625, 495.0372143554688], [12, 94.05739807128907, 470.8822903442383, 483.2506140136719, 512.7171148681641], [12, 93.4620980834961, 257.7648947143555, 500.93051452636723, 520.2942150878906], [12, 94.65269805908204, 264.9084945678711, 519.4523150634766, 534.6065155029297], [12, 278.0050942993164, 320.8666934204102, 582.5948168945313, 596.0652172851562], [12, 330.3914932250977, 377.4201922607422, 604.4842175292969, 617.1127178955078], [12, 260.7413946533203, 285.14869415283204, 662.5753192138673, 673.52001953125]]
2026-08-10 14:59:28,302 INFO     29 [qwen-vl-text] ═══ DONE ═══ 69 positions, pages=2, time=47.5s
2026-08-10 14:59:28,330 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 14:59:28,331 INFO     29 [Trace] task=7630dbd0 | doc=YXHU  62  男  直肠癌肺转移  贵州(2).pdf | Extractor:Discharge | outputs={"chunks": "2 items, types={'DischargeRecord': 2}", "html": "", "json": "2311 items", "markdown": "", "text": "", "name": "YXHU  62  男  直肠癌肺转移  贵州(2).pdf", "output_format": "chunks", "chunks_Examination": "8 items, types={'ExaminationReport': 8}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_LabExam": "6 items, types={'LabReport': 6}", "route_summary": "{\"chunks_Examination\": 8, \"chunks_Discharge\": 2, \"chunks_LabExam\": 6}"}
2026-08-10 14:59:28,331 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 14:59:28,332 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:59:28.331+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 64, "failed": 0, "current": {"7630dbd094ca11f1bd9827cf206dfa2d": {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:59:28,341 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:59:28,341 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 14:59:29,270 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:59:29,286 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 14:59:29,287 INFO     29 [Trace] task=7630dbd0 | doc=YXHU  62  男  直肠癌肺转移  贵州(2).pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "2311 items", "markdown": "", "text": "", "name": "YXHU  62  男  直肠癌肺转移  贵州(2).pdf", "output_format": "chunks", "chunks_Examination": "8 items, types={'ExaminationReport': 8}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_LabExam": "6 items, types={'LabReport': 6}", "route_summary": "{\"chunks_Examination\": 8, \"chunks_Discharge\": 2, \"chunks_LabExam\": 6}"}
2026-08-10 14:59:29,287 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 14:59:29,298 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 14:59:29,299 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 14:59:29,299 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 14:59:29,299 INFO     29 [qwen-vl-text] positions(23): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 14:59:29,299 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [23]
2026-08-10 14:59:29,399 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 14:59:29,400 INFO     29 [qwen-vl-text] LLM extraction start, text_len=254
2026-08-10 14:59:29,400 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:59:29,400 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 5, \"bbox_end\": 27, \"encounter_dates\": [\"2025-08-14\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "病理诊断报告\n病理号:\n名:\n性 别: 男\n年龄: 62岁\n收到日期: 2025-08-1\n医院:\n送检科室:\n送检医生:\n号:\n床 号:\n门诊号:\n临床诊断: 直肠、肛管新生物并狭窄\n肉眼所见:\n直肠、肛管新生物: 灰白色组织多粒, 约0.1-0.2cm, 全。\n镜下所见:\n病理诊断:\n(直肠、肛管新生物) 恶性肿瘤, 建议行免疫组化进一步协助检查。\n报告医\n审核医师\n报告日期: 2025-08-14 11:05:\n须经诊断医师签字方能生效。\n仅反映本次送检样本情况, 若有疑问, 请及时与病理科联系。",
    "role": "user"
  }
]
2026-08-10 14:59:31,213 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:59:31,213 INFO     29 [qwen-vl-text] LLM output (len=392):
{
  "exam_date": "2025-08-01",
  "report_date": "2025-08-14",
  "exam_name": "病理检查",
  "exam_category": "pathology",
  "body_part": "直肠、肛管",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "肉眼所见:\n直肠、肛管新生物: 灰白色组织多粒, 约0.1-0.2cm, 全。",
  "conclusion": "病理诊断:\n(直肠、肛管新生物) 恶性肿瘤, 建议行免疫组化进一步协助检查。",
  "physician": null,
  "reviewer": null
}
2026-08-10 14:59:31,215 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=829179, prompt_len=936
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共23行）
["病理诊断报告", "病理号:", "名:", "性 别: 男", "年龄: 62岁", "收到日期: 2025-08-1", "医院:", "送检科室:", "送检医生:", "号:", "床 号:", "门诊号:", "临床诊断: 直肠、肛管新生物并狭窄", "肉眼所见:", "直肠、肛管新生物: 灰白色组织多粒, 约0.1-0.2cm, 全。", "镜下所见:", "病理诊断:", "(直肠、肛管新生物) 恶性肿瘤, 建议行免疫组化进一步协助检查。", "报告医", "审核医师", "报告日期: 2025-08-14 11:05:", "须经诊断医师签字方能生效。", "仅反映本次送检样本情况, 若有疑问, 请及时与病理科联系。"]

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
2026-08-10 14:59:38,402 INFO     29 [qwen-vl-text] coord API raw response (len=1269):
[
	{"text": "病理诊断报告", "bbox": [372, 169, 517, 189]},
	{"text": "病理号:", "bbox": [615, 197, 687, 210]},
	{"text": "名:", "bbox": [130, 219, 144, 233]},
	{"text": "性 别: 男", "bbox": [324, 219, 417, 233]},
	{"text": "年龄: 62岁", "bbox": [465, 219, 541, 232]},
	{"text": "收到日期: 2025-08-1", "bbox": [615, 218, 770, 231]},
	{"text": "医院:", "bbox": [112, 239, 148, 252]},
	{"text": "送检科室:", "bbox": [324, 238, 395, 252]},
	{"text": "送检医生:", "bbox": [614, 237, 687, 250]},
	{"text": "号:", "bbox": [112, 255, 148, 268]},
	{"text": "床 号:", "bbox": [324, 256, 395, 270]},
	{"text": "门诊号:", "bbox": [614, 255, 687, 269]},
	{"text": "临床诊断: 直肠、肛管新生物并狭窄", "bbox": [112, 282, 354, 295]},
	{"text": "肉眼所见:", "bbox": [112, 318, 176, 331]},
	{"text": "直肠、肛管新生物: 灰白色组织多粒, 约0.1-0.2cm, 全。", "bbox": [127, 335, 518, 348]},
	{"text": "镜下所见:", "bbox": [112, 374, 176, 387]},
	{"text": "病理诊断:", "bbox": [112, 578, 176, 590]},
	{"text": "(直肠、肛管新生物) 恶性肿瘤, 建议行免疫组化进一步协助检查。", "bbox": [135, 594, 570, 610]},
	{"text": "报告医", "bbox": [112, 836, 154, 850]},
	{"text": "审核医师", "bbox": [339, 842, 400, 856]},
	{"text": "报告日期: 2025-08-14 11:05:", "bbox": [567, 848, 770, 862]},
	{"text": "须经诊断医师签字方能生效。", "bbox": [113, 852, 266, 867]},
	{"text": "仅反映本次送检样本情况, 若有疑问, 请及时与病理科联系。", "bbox": [113, 865, 445, 884]}
]
2026-08-10 14:59:38,402 INFO     29 [qwen-vl-text] coord API: raw_items=23, valid_items=23, elapsed=7.2s
2026-08-10 14:59:38,403 INFO     29 [qwen-vl-text] coord item[0]: text=病理诊断报告, bbox=[372, 169, 517, 189]
2026-08-10 14:59:38,403 INFO     29 [qwen-vl-text] coord item[1]: text=病理号:, bbox=[615, 197, 687, 210]
2026-08-10 14:59:38,403 INFO     29 [qwen-vl-text] coord item[2]: text=名:, bbox=[130, 219, 144, 233]
2026-08-10 14:59:38,403 INFO     29 [qwen-vl-text] coord item[3]: text=性 别: 男, bbox=[324, 219, 417, 233]
2026-08-10 14:59:38,403 INFO     29 [qwen-vl-text] coord item[4]: text=年龄: 62岁, bbox=[465, 219, 541, 232]
2026-08-10 14:59:38,403 INFO     29 [qwen-vl-text] coord item[5]: text=收到日期: 2025-08-1, bbox=[615, 218, 770, 231]
2026-08-10 14:59:38,403 INFO     29 [qwen-vl-text] coord item[6]: text=医院:, bbox=[112, 239, 148, 252]
2026-08-10 14:59:38,403 INFO     29 [qwen-vl-text] coord item[7]: text=送检科室:, bbox=[324, 238, 395, 252]
2026-08-10 14:59:38,403 INFO     29 [qwen-vl-text] coord item[8]: text=送检医生:, bbox=[614, 237, 687, 250]
2026-08-10 14:59:38,403 INFO     29 [qwen-vl-text] coord item[9]: text=号:, bbox=[112, 255, 148, 268]
2026-08-10 14:59:38,403 INFO     29 [qwen-vl-text] coord item[10]: text=床 号:, bbox=[324, 256, 395, 270]
2026-08-10 14:59:38,403 INFO     29 [qwen-vl-text] coord item[11]: text=门诊号:, bbox=[614, 255, 687, 269]
2026-08-10 14:59:38,403 INFO     29 [qwen-vl-text] coord item[12]: text=临床诊断: 直肠、肛管新生物并狭窄, bbox=[112, 282, 354, 295]
2026-08-10 14:59:38,403 INFO     29 [qwen-vl-text] coord item[13]: text=肉眼所见:, bbox=[112, 318, 176, 331]
2026-08-10 14:59:38,403 INFO     29 [qwen-vl-text] coord item[14]: text=直肠、肛管新生物: 灰白色组织多粒, 约0.1-0.2cm, 全。, bbox=[127, 335, 518, 348]
2026-08-10 14:59:38,403 INFO     29 [qwen-vl-text] coord item[15]: text=镜下所见:, bbox=[112, 374, 176, 387]
2026-08-10 14:59:38,403 INFO     29 [qwen-vl-text] coord item[16]: text=病理诊断:, bbox=[112, 578, 176, 590]
2026-08-10 14:59:38,403 INFO     29 [qwen-vl-text] coord item[17]: text=(直肠、肛管新生物) 恶性肿瘤, 建议行免疫组化进一步协助检查。, bbox=[135, 594, 570, 610]
2026-08-10 14:59:38,403 INFO     29 [qwen-vl-text] coord item[18]: text=报告医, bbox=[112, 836, 154, 850]
2026-08-10 14:59:38,403 INFO     29 [qwen-vl-text] coord item[19]: text=审核医师, bbox=[339, 842, 400, 856]
2026-08-10 14:59:38,404 INFO     29 [qwen-vl-text] coord item[20]: text=报告日期: 2025-08-14 11:05:, bbox=[567, 848, 770, 862]
2026-08-10 14:59:38,404 INFO     29 [qwen-vl-text] coord item[21]: text=须经诊断医师签字方能生效。, bbox=[113, 852, 266, 867]
2026-08-10 14:59:38,404 INFO     29 [qwen-vl-text] coord item[22]: text=仅反映本次送检样本情况, 若有疑问, 请及时与病理科联系。, bbox=[113, 865, 445, 884]
2026-08-10 14:59:38,404 INFO     29 [qwen-vl-text] page=1 — 23/23 coords, api_time=7.2s
2026-08-10 14:59:38,404 INFO     29 [qwen-vl-text] new_positions (23):
[[1, 221.45159545898437, 307.77009368896483, 142.28110412597655, 159.11910461425782], [1, 366.10949249267577, 408.97109161376954, 165.85430480957032, 176.79900512695312], [1, 77.38899841308594, 85.72319824218751, 184.3761053466797, 196.16270568847656], [1, 192.87719604492187, 248.240094909668, 184.3761053466797, 196.16270568847656], [1, 276.81449432373046, 322.0572933959961, 184.3761053466797, 195.3208056640625], [1, 366.10949249267577, 458.38099060058596, 183.53420532226562, 194.47890563964845], [1, 66.6735986328125, 88.10439819335937, 201.21410583496095, 212.15880615234377], [1, 192.87719604492187, 235.14349517822268, 200.3722058105469, 212.15880615234377], [1, 365.5141925048828, 408.97109161376954, 199.53030578613283, 210.47500610351562], [1, 66.6735986328125, 88.10439819335937, 214.68450622558595, 225.62920654296875], [1, 192.87719604492187, 235.14349517822268, 215.52640625, 227.3130065917969], [1, 365.5141925048828, 408.97109161376954, 214.68450622558595, 226.47110656738283], [1, 66.6735986328125, 210.73619567871094, 237.41580688476563, 248.36050720214845], [1, 66.6735986328125, 104.7727978515625, 267.72420776367187, 278.6689080810547], [1, 75.60309844970703, 308.36539367675783, 282.03650817871096, 292.98120849609376], [1, 66.6735986328125, 104.7727978515625, 314.8706091308594, 325.8153094482422], [1, 66.6735986328125, 104.7727978515625, 486.61821411132814, 496.7210144042969], [1, 80.36549835205078, 339.3209930419922, 500.08861450195315, 513.5590148925781], [1, 66.6735986328125, 91.67619812011719, 703.8284204101562, 715.6150207519531], [1, 201.80669586181642, 238.1199951171875, 708.8798205566407, 720.6664208984375], [1, 337.5350930786133, 458.38099060058596, 713.9312207031251, 725.717821044922], [1, 67.26889862060547, 158.3497967529297, 717.2988208007813, 729.9273211669922], [1, 67.26889862060547, 264.9084945678711, 728.243521118164, 744.2396215820313]]
2026-08-10 14:59:38,405 INFO     29 [qwen-vl-text] ═══ DONE ═══ 23 positions, pages=1, time=9.1s
2026-08-10 14:59:38,405 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 14:59:38,407 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 14:59:38,407 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 14:59:38,407 INFO     29 [qwen-vl-text] positions(23): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 14:59:38,407 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [23]
2026-08-10 14:59:38,520 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 14:59:38,521 INFO     29 [qwen-vl-text] LLM extraction start, text_len=337
2026-08-10 14:59:38,521 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:59:38,521 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 33, \"bbox_end\": 55, \"encounter_dates\": [\"2026-02-23\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "报告详情\n检查\n盆腔CT*\n姓名\n男63岁\n检查时间\n2026-02-23 11:37:59\n影像所见\n对比2026-02-15盆腔CT平扫：阑尾未见增\n粗。直肠下段管壁增厚，浆膜面稍毛糙，直肠\n周围可见肿大淋巴结，较大者大小约\n8mm×5mm。盆腔左份及左侧会阴区见条片状\n低密度影，范围较前缩小，边界不清，其内可\n见引流管影。腹腔未见明显积液及游离气体。\n腹腔及腹膜后未见明显增大淋巴结。腹主动脉\n及双侧髂总动脉壁见斑片状高密度影。腰椎椎\n体边缘变尖。\n诊断意见\n1.直肠下段Ca，累及浆膜面，盆腔多发肿大淋\n巴结，请结合临床及MRI检查。2.盆腔左份及\n左侧会阴区脓肿引流术后，脓肿较前吸收。3.\n前列腺钙化灶。4.腹主动脉及双侧髂总动脉粥\n样硬化。5.腰椎退行性变。",
    "role": "user"
  }
]
2026-08-10 14:59:41,670 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:59:41,670 INFO     29 [qwen-vl-text] LLM output (len=567):
{
  "exam_date": "2026-02-23",
  "report_date": null,
  "exam_name": "盆腔CT",
  "exam_category": "imaging",
  "body_part": "盆腔",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "对比2026-02-15盆腔CT平扫：阑尾未见增粗。直肠下段管壁增厚，浆膜面稍毛糙，直肠周围可见肿大淋巴结，较大者大小约8mm×5mm。盆腔左份及左侧会阴区见条片状低密度影，范围较前缩小，边界不清，其内可见引流管影。腹腔未见明显积液及游离气体。腹腔及腹膜后未见明显增大淋巴结。腹主动脉及双侧髂总动脉壁见斑片状高密度影。腰椎椎体边缘变尖。",
  "conclusion": "1.直肠下段Ca，累及浆膜面，盆腔多发肿大淋巴结，请结合临床及MRI检查。2.盆腔左份及左侧会阴区脓肿引流术后，脓肿较前吸收。3.前列腺钙化灶。4.腹主动脉及双侧髂总动脉粥样硬化。5.腰椎退行性变。",
  "physician": null,
  "reviewer": null
}
2026-08-10 14:59:41,672 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=554809, prompt_len=1019
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共23行）
["报告详情", "检查", "盆腔CT*", "姓名", "男63岁", "检查时间", "2026-02-23 11:37:59", "影像所见", "对比2026-02-15盆腔CT平扫：阑尾未见增", "粗。直肠下段管壁增厚，浆膜面稍毛糙，直肠", "周围可见肿大淋巴结，较大者大小约", "8mm×5mm。盆腔左份及左侧会阴区见条片状", "低密度影，范围较前缩小，边界不清，其内可", "见引流管影。腹腔未见明显积液及游离气体。", "腹腔及腹膜后未见明显增大淋巴结。腹主动脉", "及双侧髂总动脉壁见斑片状高密度影。腰椎椎", "体边缘变尖。", "诊断意见", "1.直肠下段Ca，累及浆膜面，盆腔多发肿大淋", "巴结，请结合临床及MRI检查。2.盆腔左份及", "左侧会阴区脓肿引流术后，脓肿较前吸收。3.", "前列腺钙化灶。4.腹主动脉及双侧髂总动脉粥", "样硬化。5.腰椎退行性变。"]

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
2026-08-10 14:59:50,175 INFO     29 [qwen-vl-text] coord API raw response (len=1352):
[
	{"text": "报告详情", "bbox": [328, 142, 422, 160]},
	{"text": "检查", "bbox": [150, 201, 227, 220]},
	{"text": "盆腔CT*", "bbox": [150, 229, 241, 247]},
	{"text": "姓名", "bbox": [150, 293, 193, 310]},
	{"text": "男63岁", "bbox": [523, 293, 598, 310]},
	{"text": "检查时间", "bbox": [150, 335, 237, 352]},
	{"text": "2026-02-23 11:37:59", "bbox": [392, 335, 599, 352]},
	{"text": "影像所见", "bbox": [150, 401, 237, 418]},
	{"text": "对比2026-02-15盆腔CT平扫：阑尾未见增", "bbox": [150, 429, 558, 446]},
	{"text": "粗。直肠下段管壁增厚，浆膜面稍毛糙，直肠", "bbox": [150, 450, 588, 467]},
	{"text": "周围可见肿大淋巴结，较大者大小约", "bbox": [150, 470, 500, 487]},
	{"text": "8mm×5mm。盆腔左份及左侧会阴区见条片状", "bbox": [150, 490, 596, 507]},
	{"text": "低密度影，范围较前缩小，边界不清，其内可", "bbox": [150, 510, 588, 527]},
	{"text": "见引流管影。腹腔未见明显积液及游离气体。", "bbox": [150, 530, 578, 547]},
	{"text": "腹腔及腹膜后未见明显增大淋巴结。腹主动脉", "bbox": [150, 550, 588, 567]},
	{"text": "及双侧髂总动脉壁见斑片状高密度影。腰椎椎", "bbox": [150, 570, 588, 587]},
	{"text": "体边缘变尖。", "bbox": [150, 590, 270, 607]},
	{"text": "诊断意见", "bbox": [150, 632, 237, 649]},
	{"text": "1.直肠下段Ca，累及浆膜面，盆腔多发肿大淋", "bbox": [150, 660, 591, 677]},
	{"text": "巴结，请结合临床及MRI检查。2.盆腔左份及", "bbox": [150, 680, 585, 697]},
	{"text": "左侧会阴区脓肿引流术后，脓肿较前吸收。3.", "bbox": [150, 700, 585, 717]},
	{"text": "前列腺钙化灶。4.腹主动脉及双侧髂总动脉粥", "bbox": [150, 720, 591, 737]},
	{"text": "样硬化。5.腰椎退行性变。", "bbox": [150, 740, 406, 757]}
]
2026-08-10 14:59:50,176 INFO     29 [qwen-vl-text] coord API: raw_items=23, valid_items=23, elapsed=8.5s
2026-08-10 14:59:50,176 INFO     29 [qwen-vl-text] coord item[0]: text=报告详情, bbox=[328, 142, 422, 160]
2026-08-10 14:59:50,176 INFO     29 [qwen-vl-text] coord item[1]: text=检查, bbox=[150, 201, 227, 220]
2026-08-10 14:59:50,176 INFO     29 [qwen-vl-text] coord item[2]: text=盆腔CT*, bbox=[150, 229, 241, 247]
2026-08-10 14:59:50,176 INFO     29 [qwen-vl-text] coord item[3]: text=姓名, bbox=[150, 293, 193, 310]
2026-08-10 14:59:50,176 INFO     29 [qwen-vl-text] coord item[4]: text=男63岁, bbox=[523, 293, 598, 310]
2026-08-10 14:59:50,176 INFO     29 [qwen-vl-text] coord item[5]: text=检查时间, bbox=[150, 335, 237, 352]
2026-08-10 14:59:50,176 INFO     29 [qwen-vl-text] coord item[6]: text=2026-02-23 11:37:59, bbox=[392, 335, 599, 352]
2026-08-10 14:59:50,176 INFO     29 [qwen-vl-text] coord item[7]: text=影像所见, bbox=[150, 401, 237, 418]
2026-08-10 14:59:50,176 INFO     29 [qwen-vl-text] coord item[8]: text=对比2026-02-15盆腔CT平扫：阑尾未见增, bbox=[150, 429, 558, 446]
2026-08-10 14:59:50,176 INFO     29 [qwen-vl-text] coord item[9]: text=粗。直肠下段管壁增厚，浆膜面稍毛糙，直肠, bbox=[150, 450, 588, 467]
2026-08-10 14:59:50,176 INFO     29 [qwen-vl-text] coord item[10]: text=周围可见肿大淋巴结，较大者大小约, bbox=[150, 470, 500, 487]
2026-08-10 14:59:50,176 INFO     29 [qwen-vl-text] coord item[11]: text=8mm×5mm。盆腔左份及左侧会阴区见条片状, bbox=[150, 490, 596, 507]
2026-08-10 14:59:50,176 INFO     29 [qwen-vl-text] coord item[12]: text=低密度影，范围较前缩小，边界不清，其内可, bbox=[150, 510, 588, 527]
2026-08-10 14:59:50,176 INFO     29 [qwen-vl-text] coord item[13]: text=见引流管影。腹腔未见明显积液及游离气体。, bbox=[150, 530, 578, 547]
2026-08-10 14:59:50,176 INFO     29 [qwen-vl-text] coord item[14]: text=腹腔及腹膜后未见明显增大淋巴结。腹主动脉, bbox=[150, 550, 588, 567]
2026-08-10 14:59:50,176 INFO     29 [qwen-vl-text] coord item[15]: text=及双侧髂总动脉壁见斑片状高密度影。腰椎椎, bbox=[150, 570, 588, 587]
2026-08-10 14:59:50,176 INFO     29 [qwen-vl-text] coord item[16]: text=体边缘变尖。, bbox=[150, 590, 270, 607]
2026-08-10 14:59:50,176 INFO     29 [qwen-vl-text] coord item[17]: text=诊断意见, bbox=[150, 632, 237, 649]
2026-08-10 14:59:50,176 INFO     29 [qwen-vl-text] coord item[18]: text=1.直肠下段Ca，累及浆膜面，盆腔多发肿大淋, bbox=[150, 660, 591, 677]
2026-08-10 14:59:50,176 INFO     29 [qwen-vl-text] coord item[19]: text=巴结，请结合临床及MRI检查。2.盆腔左份及, bbox=[150, 680, 585, 697]
2026-08-10 14:59:50,176 INFO     29 [qwen-vl-text] coord item[20]: text=左侧会阴区脓肿引流术后，脓肿较前吸收。3., bbox=[150, 700, 585, 717]
2026-08-10 14:59:50,176 INFO     29 [qwen-vl-text] coord item[21]: text=前列腺钙化灶。4.腹主动脉及双侧髂总动脉粥, bbox=[150, 720, 591, 737]
2026-08-10 14:59:50,176 INFO     29 [qwen-vl-text] coord item[22]: text=样硬化。5.腰椎退行性变。, bbox=[150, 740, 406, 757]
2026-08-10 14:59:50,176 INFO     29 [qwen-vl-text] page=2 — 23/23 coords, api_time=8.5s
2026-08-10 14:59:50,177 INFO     29 [qwen-vl-text] new_positions (23):
[[2, 195.25839599609375, 251.21659484863284, 119.54980346679687, 134.70400390625], [2, 89.29499816894531, 135.1330972290039, 169.22190490722656, 185.21800537109377], [2, 89.29499816894531, 143.4672970581055, 192.79510559082033, 207.94930603027345], [2, 89.29499816894531, 114.89289764404298, 246.6767071533203, 260.9890075683594], [2, 311.34189361572265, 355.9893927001953, 246.6767071533203, 260.9890075683594], [2, 89.29499816894531, 141.0860971069336, 282.03650817871096, 296.34880859375], [2, 233.35759521484377, 356.5846926879883, 282.03650817871096, 296.34880859375], [2, 89.29499816894531, 141.0860971069336, 337.6019097900391, 351.9142102050781], [2, 89.29499816894531, 332.1773931884766, 361.1751104736328, 375.4874108886719], [2, 89.29499816894531, 350.03639282226567, 378.8550109863281, 393.1673114013672], [2, 89.29499816894531, 297.6499938964844, 395.69301147460936, 410.00531188964845], [2, 89.29499816894531, 354.79879272460937, 412.53101196289066, 426.8433123779297], [2, 89.29499816894531, 350.03639282226567, 429.3690124511719, 443.68131286621093], [2, 89.29499816894531, 344.08339294433597, 446.20701293945314, 460.5193133544922], [2, 89.29499816894531, 350.03639282226567, 463.0450134277344, 477.35731384277346], [2, 89.29499816894531, 350.03639282226567, 479.88301391601567, 494.1953143310547], [2, 89.29499816894531, 160.73099670410156, 496.7210144042969, 511.03331481933594], [2, 89.29499816894531, 141.0860971069336, 532.0808154296875, 546.3931158447266], [2, 89.29499816894531, 351.82229278564455, 555.6540161132813, 569.9663165283204], [2, 89.29499816894531, 348.25049285888673, 572.4920166015626, 586.8043170166015], [2, 89.29499816894531, 348.25049285888673, 589.3300170898438, 603.6423175048828], [2, 89.29499816894531, 351.82229278564455, 606.168017578125, 620.4803179931641], [2, 89.29499816894531, 241.69179504394532, 623.0060180664062, 637.3183184814453]]
2026-08-10 14:59:50,177 INFO     29 [qwen-vl-text] ═══ DONE ═══ 23 positions, pages=1, time=11.8s
2026-08-10 14:59:50,177 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 14:59:50,178 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 14:59:50,178 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 14:59:50,178 INFO     29 [qwen-vl-text] positions(28): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 14:59:50,178 INFO     29 [qwen-vl-text] page grouping: [3], lines per page: [28]
2026-08-10 14:59:50,304 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 14:59:50,305 INFO     29 [qwen-vl-text] LLM extraction start, text_len=446
2026-08-10 14:59:50,305 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:59:50,305 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 61, \"bbox_end\": 88, \"encounter_dates\": [\"2026-02-08\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "报告详情\n检查\n盆腔CT平扫+增强*\n姓名\n男63岁\n检查时间\n2026-02-08 14:55:00\n影像所见\n对比2026-01-09腹部增强：阑尾未见增粗。直\n肠下段管壁增厚，增强扫描不均匀强化，浆膜\n面稍毛糙，周围可见淋巴结显示，较大者大小\n约8mm×5mm。盆腔左份及左侧会阴区见不规\n则团片状密度增高影，局部呈囊性改变，病灶\n边界欠清晰，较大截面大小约\n70mm×34mm×95mm（前后径×左右径×上下\n径），其内见小气泡影，周围脂肪间隙模糊，\n增强病灶边缘轻度强化，病灶与左侧前列腺、\n精囊腺分界欠清晰，前列腺可见结节状高密度\n影。腹腔未见明显积液及游离气体。腹腔及腹\n膜后未见明显增大淋巴结。腹主动脉及双侧髂\n总动脉壁见斑片状高密度影。腰椎椎体边缘变\n尖。\n诊断意见\n1.直肠下段Ca，累及浆膜面，盆腔多发淋巴\n结，请结合临床及MRI检查。2.考虑盆腔左份\n及左侧会阴区脓肿形成，请结合临床并复查。\n3.前列腺钙化灶。4.腹主动脉及双侧髂总动脉\n粥样硬化。5.腰椎退行性变。",
    "role": "user"
  }
]
2026-08-10 14:59:53,899 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:59:53,899 INFO     29 [qwen-vl-text] LLM output (len=671):
{
  "exam_date": "2026-02-08",
  "report_date": null,
  "exam_name": "盆腔CT平扫+增强",
  "exam_category": "imaging",
  "body_part": "盆腔",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "对比2026-01-09腹部增强：阑尾未见增粗。直肠下段管壁增厚，增强扫描不均匀强化，浆膜面稍毛糙，周围可见淋巴结显示，较大者大小约8mm×5mm。盆腔左份及左侧会阴区见不规则团片状密度增高影，局部呈囊性改变，病灶边界欠清晰，较大截面大小约70mm×34mm×95mm（前后径×左右径×上下径），其内见小气泡影，周围脂肪间隙模糊，增强病灶边缘轻度强化，病灶与左侧前列腺、精囊腺分界欠清晰，前列腺可见结节状高密度影。腹腔未见明显积液及游离气体。腹腔及腹膜后未见明显增大淋巴结。腹主动脉及双侧髂总动脉壁见斑片状高密度影。腰椎椎体边缘变尖。",
  "conclusion": "1.直肠下段Ca，累及浆膜面，盆腔多发淋巴结，请结合临床及MRI检查。2.考虑盆腔左份及左侧会阴区脓肿形成，请结合临床并复查。3.前列腺钙化灶。4.腹主动脉及双侧髂总动脉粥样硬化。5.腰椎退行性变。",
  "physician": null,
  "reviewer": null
}
2026-08-10 14:59:53,900 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=713794, prompt_len=1143
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共28行）
["报告详情", "检查", "盆腔CT平扫+增强*", "姓名", "男63岁", "检查时间", "2026-02-08 14:55:00", "影像所见", "对比2026-01-09腹部增强：阑尾未见增粗。直", "肠下段管壁增厚，增强扫描不均匀强化，浆膜", "面稍毛糙，周围可见淋巴结显示，较大者大小", "约8mm×5mm。盆腔左份及左侧会阴区见不规", "则团片状密度增高影，局部呈囊性改变，病灶", "边界欠清晰，较大截面大小约", "70mm×34mm×95mm（前后径×左右径×上下", "径），其内见小气泡影，周围脂肪间隙模糊，", "增强病灶边缘轻度强化，病灶与左侧前列腺、", "精囊腺分界欠清晰，前列腺可见结节状高密度", "影。腹腔未见明显积液及游离气体。腹腔及腹", "膜后未见明显增大淋巴结。腹主动脉及双侧髂", "总动脉壁见斑片状高密度影。腰椎椎体边缘变", "尖。", "诊断意见", "1.直肠下段Ca，累及浆膜面，盆腔多发淋巴", "结，请结合临床及MRI检查。2.考虑盆腔左份", "及左侧会阴区脓肿形成，请结合临床并复查。", "3.前列腺钙化灶。4.腹主动脉及双侧髂总动脉", "粥样硬化。5.腰椎退行性变。"]

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
2026-08-10 15:00:03,202 INFO     29 [qwen-vl-text] coord API raw response (len=1681):
[
	{"text": "报告详情", "bbox": [328, 142, 422, 160]},
	{"text": "检查", "bbox": [150, 202, 227, 220]},
	{"text": "盆腔CT平扫+增强*", "bbox": [150, 230, 354, 248]},
	{"text": "姓名", "bbox": [150, 294, 193, 310]},
	{"text": "男63岁", "bbox": [523, 294, 598, 310]},
	{"text": "检查时间", "bbox": [150, 336, 237, 352]},
	{"text": "2026-02-08 14:55:00", "bbox": [382, 336, 600, 352]},
	{"text": "影像所见", "bbox": [150, 402, 237, 418]},
	{"text": "对比2026-01-09腹部增强：阑尾未见增粗。直", "bbox": [150, 430, 598, 447]},
	{"text": "肠下段管壁增厚，增强扫描不均匀强化，浆膜", "bbox": [150, 450, 589, 467]},
	{"text": "面稍毛糙，周围可见淋巴结显示，较大者大小", "bbox": [150, 470, 588, 487]},
	{"text": "约8mm×5mm。盆腔左份及左侧会阴区见不规", "bbox": [150, 490, 596, 507]},
	{"text": "则团片状密度增高影，局部呈囊性改变，病灶", "bbox": [150, 510, 588, 527]},
	{"text": "边界欠清晰，较大截面大小约", "bbox": [150, 530, 435, 547]},
	{"text": "70mm×34mm×95mm（前后径×左右径×上下", "bbox": [150, 550, 592, 567]},
	{"text": "径），其内见小气泡影，周围脂肪间隙模糊，", "bbox": [150, 570, 577, 587]},
	{"text": "增强病灶边缘轻度强化，病灶与左侧前列腺、", "bbox": [150, 590, 577, 607]},
	{"text": "精囊腺分界欠清晰，前列腺可见结节状高密度", "bbox": [150, 610, 588, 627]},
	{"text": "影。腹腔未见明显积液及游离气体。腹腔及腹", "bbox": [150, 630, 588, 647]},
	{"text": "膜后未见明显增大淋巴结。腹主动脉及双侧髂", "bbox": [150, 650, 588, 667]},
	{"text": "总动脉壁见斑片状高密度影。腰椎椎体边缘变", "bbox": [150, 670, 588, 687]},
	{"text": "尖。", "bbox": [150, 690, 182, 707]},
	{"text": "诊断意见", "bbox": [150, 732, 237, 749]},
	{"text": "1.直肠下段Ca，累及浆膜面，盆腔多发淋巴", "bbox": [150, 760, 570, 777]},
	{"text": "结，请结合临床及MRI检查。2.考虑盆腔左份", "bbox": [150, 780, 585, 797]},
	{"text": "及左侧会阴区脓肿形成，请结合临床并复查。", "bbox": [150, 800, 585, 817]},
	{"text": "3.前列腺钙化灶。4.腹主动脉及双侧髂总动脉", "bbox": [150, 820, 592, 837]},
	{"text": "粥样硬化。5.腰椎退行性变。", "bbox": [150, 840, 428, 857]}
]
2026-08-10 15:00:03,203 INFO     29 [qwen-vl-text] coord API: raw_items=28, valid_items=28, elapsed=9.3s
2026-08-10 15:00:03,203 INFO     29 [qwen-vl-text] coord item[0]: text=报告详情, bbox=[328, 142, 422, 160]
2026-08-10 15:00:03,203 INFO     29 [qwen-vl-text] coord item[1]: text=检查, bbox=[150, 202, 227, 220]
2026-08-10 15:00:03,203 INFO     29 [qwen-vl-text] coord item[2]: text=盆腔CT平扫+增强*, bbox=[150, 230, 354, 248]
2026-08-10 15:00:03,203 INFO     29 [qwen-vl-text] coord item[3]: text=姓名, bbox=[150, 294, 193, 310]
2026-08-10 15:00:03,203 INFO     29 [qwen-vl-text] coord item[4]: text=男63岁, bbox=[523, 294, 598, 310]
2026-08-10 15:00:03,203 INFO     29 [qwen-vl-text] coord item[5]: text=检查时间, bbox=[150, 336, 237, 352]
2026-08-10 15:00:03,203 INFO     29 [qwen-vl-text] coord item[6]: text=2026-02-08 14:55:00, bbox=[382, 336, 600, 352]
2026-08-10 15:00:03,203 INFO     29 [qwen-vl-text] coord item[7]: text=影像所见, bbox=[150, 402, 237, 418]
2026-08-10 15:00:03,203 INFO     29 [qwen-vl-text] coord item[8]: text=对比2026-01-09腹部增强：阑尾未见增粗。直, bbox=[150, 430, 598, 447]
2026-08-10 15:00:03,203 INFO     29 [qwen-vl-text] coord item[9]: text=肠下段管壁增厚，增强扫描不均匀强化，浆膜, bbox=[150, 450, 589, 467]
2026-08-10 15:00:03,203 INFO     29 [qwen-vl-text] coord item[10]: text=面稍毛糙，周围可见淋巴结显示，较大者大小, bbox=[150, 470, 588, 487]
2026-08-10 15:00:03,203 INFO     29 [qwen-vl-text] coord item[11]: text=约8mm×5mm。盆腔左份及左侧会阴区见不规, bbox=[150, 490, 596, 507]
2026-08-10 15:00:03,204 INFO     29 [qwen-vl-text] coord item[12]: text=则团片状密度增高影，局部呈囊性改变，病灶, bbox=[150, 510, 588, 527]
2026-08-10 15:00:03,204 INFO     29 [qwen-vl-text] coord item[13]: text=边界欠清晰，较大截面大小约, bbox=[150, 530, 435, 547]
2026-08-10 15:00:03,204 INFO     29 [qwen-vl-text] coord item[14]: text=70mm×34mm×95mm（前后径×左右径×上下, bbox=[150, 550, 592, 567]
2026-08-10 15:00:03,204 INFO     29 [qwen-vl-text] coord item[15]: text=径），其内见小气泡影，周围脂肪间隙模糊，, bbox=[150, 570, 577, 587]
2026-08-10 15:00:03,204 INFO     29 [qwen-vl-text] coord item[16]: text=增强病灶边缘轻度强化，病灶与左侧前列腺、, bbox=[150, 590, 577, 607]
2026-08-10 15:00:03,204 INFO     29 [qwen-vl-text] coord item[17]: text=精囊腺分界欠清晰，前列腺可见结节状高密度, bbox=[150, 610, 588, 627]
2026-08-10 15:00:03,204 INFO     29 [qwen-vl-text] coord item[18]: text=影。腹腔未见明显积液及游离气体。腹腔及腹, bbox=[150, 630, 588, 647]
2026-08-10 15:00:03,204 INFO     29 [qwen-vl-text] coord item[19]: text=膜后未见明显增大淋巴结。腹主动脉及双侧髂, bbox=[150, 650, 588, 667]
2026-08-10 15:00:03,204 INFO     29 [qwen-vl-text] coord item[20]: text=总动脉壁见斑片状高密度影。腰椎椎体边缘变, bbox=[150, 670, 588, 687]
2026-08-10 15:00:03,204 INFO     29 [qwen-vl-text] coord item[21]: text=尖。, bbox=[150, 690, 182, 707]
2026-08-10 15:00:03,204 INFO     29 [qwen-vl-text] coord item[22]: text=诊断意见, bbox=[150, 732, 237, 749]
2026-08-10 15:00:03,204 INFO     29 [qwen-vl-text] coord item[23]: text=1.直肠下段Ca，累及浆膜面，盆腔多发淋巴, bbox=[150, 760, 570, 777]
2026-08-10 15:00:03,204 INFO     29 [qwen-vl-text] coord item[24]: text=结，请结合临床及MRI检查。2.考虑盆腔左份, bbox=[150, 780, 585, 797]
2026-08-10 15:00:03,204 INFO     29 [qwen-vl-text] coord item[25]: text=及左侧会阴区脓肿形成，请结合临床并复查。, bbox=[150, 800, 585, 817]
2026-08-10 15:00:03,205 INFO     29 [qwen-vl-text] coord item[26]: text=3.前列腺钙化灶。4.腹主动脉及双侧髂总动脉, bbox=[150, 820, 592, 837]
2026-08-10 15:00:03,205 INFO     29 [qwen-vl-text] coord item[27]: text=粥样硬化。5.腰椎退行性变。, bbox=[150, 840, 428, 857]
2026-08-10 15:00:03,205 INFO     29 [qwen-vl-text] page=3 — 28/28 coords, api_time=9.3s
2026-08-10 15:00:03,205 INFO     29 [qwen-vl-text] new_positions (28):
[[3, 195.25839599609375, 251.21659484863284, 119.54980346679687, 134.70400390625], [3, 89.29499816894531, 135.1330972290039, 170.06380493164062, 185.21800537109377], [3, 89.29499816894531, 210.73619567871094, 193.6370056152344, 208.7912060546875], [3, 89.29499816894531, 114.89289764404298, 247.5186071777344, 260.9890075683594], [3, 311.34189361572265, 355.9893927001953, 247.5186071777344, 260.9890075683594], [3, 89.29499816894531, 141.0860971069336, 282.878408203125, 296.34880859375], [3, 227.40459533691407, 357.17999267578125, 282.878408203125, 296.34880859375], [3, 89.29499816894531, 141.0860971069336, 338.4438098144531, 351.9142102050781], [3, 89.29499816894531, 355.9893927001953, 362.0170104980469, 376.329310913086], [3, 89.29499816894531, 350.6316928100586, 378.8550109863281, 393.1673114013672], [3, 89.29499816894531, 350.03639282226567, 395.69301147460936, 410.00531188964845], [3, 89.29499816894531, 354.79879272460937, 412.53101196289066, 426.8433123779297], [3, 89.29499816894531, 350.03639282226567, 429.3690124511719, 443.68131286621093], [3, 89.29499816894531, 258.9554946899414, 446.20701293945314, 460.5193133544922], [3, 89.29499816894531, 352.4175927734375, 463.0450134277344, 477.35731384277346], [3, 89.29499816894531, 343.48809295654297, 479.88301391601567, 494.1953143310547], [3, 89.29499816894531, 343.48809295654297, 496.7210144042969, 511.03331481933594], [3, 89.29499816894531, 350.03639282226567, 513.5590148925781, 527.8713153076172], [3, 89.29499816894531, 350.03639282226567, 530.3970153808594, 544.7093157958984], [3, 89.29499816894531, 350.03639282226567, 547.2350158691406, 561.5473162841797], [3, 89.29499816894531, 350.03639282226567, 564.0730163574219, 578.385316772461], [3, 89.29499816894531, 108.34459777832032, 580.9110168457031, 595.2233172607422], [3, 89.29499816894531, 141.0860971069336, 616.2708178710938, 630.5831182861328], [3, 89.29499816894531, 339.3209930419922, 639.8440185546875, 654.1563189697266], [3, 89.29499816894531, 348.25049285888673, 656.6820190429688, 670.9943194580078], [3, 89.29499816894531, 348.25049285888673, 673.52001953125, 687.8323199462891], [3, 89.29499816894531, 352.4175927734375, 690.3580200195313, 704.6703204345704], [3, 89.29499816894531, 254.78839477539063, 707.1960205078125, 721.5083209228516]]
2026-08-10 15:00:03,205 INFO     29 [qwen-vl-text] ═══ DONE ═══ 28 positions, pages=1, time=13.0s
2026-08-10 15:00:03,206 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:00:03,216 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:00:03,217 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 15:00:03,217 INFO     29 [qwen-vl-text] positions(31): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:00:03,217 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [31]
2026-08-10 15:00:03,347 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 15:00:03,348 INFO     29 [qwen-vl-text] LLM extraction start, text_len=542
2026-08-10 15:00:03,348 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:00:03,349 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 94, \"bbox_end\": 124, \"encounter_dates\": [\"2026-02-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "报告详情\n姓名\n男63岁\n检查时间\n2026-02-05 17:02:53\n影像所见\n对比2026-01-09胸部CT平扫：双肺透亮度增\n高，可见多发囊状透亮影；左肺上叶舌段可见\n两处肿块影，CT值约37-53Hu，分叶状，边界\n清晰，较前稍扩大，较大者大小约\n45mm×38mm×47mm（上下径×左右径×前后\n径），密度不均，其内见结节状高密度影；左\n肺上叶及双肺下叶可见实性结节，较大者位于\n右肺下叶外基底段（IM216），大小约\n11mm×9mm，略呈分叶状；右肺上叶可见结\n节状高密度灶。气管内斑片状密度增高影此次\n未见显示。双肺下叶近胸膜处见絮状密度增高\n影，肺门影不大。纵隔无明显偏移，其内淋巴\n结不大。心脏大小、形态未见明显异常，心腔\n密度减低，主动脉壁见斑片状高密度影，双侧\n胸腔未见积液。肋骨骨质结构未见异常。胸椎\n椎体边缘变尖。\n诊断意见\n1.肺气肿伴双肺多发肺大疱，请结合肺功能检\n查。2.左肺上叶舌段结节及肿块，具恶性征\n象。3.左肺上叶及双肺下叶实性结节，建议随\n诊；右肺上叶钙化灶。4.双肺下叶坠积效应，\n建议复查。5.气管黏液栓较前未见确切显示。\n6.贫血征象，请结合实验室检查；主动脉粥样\n硬化。7.胸椎退行性变。（第1-4、6、7条较前\n大致相仿）",
    "role": "user"
  }
]
2026-08-10 15:00:03,351 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:00:03.351+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 64, "failed": 0, "current": {"7630dbd094ca11f1bd9827cf206dfa2d": {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:00:07,747 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:00:07,747 INFO     29 [qwen-vl-text] LLM output (len=771):
{
  "exam_date": "2026-02-05",
  "report_date": null,
  "exam_name": "胸部CT",
  "exam_category": "imaging",
  "body_part": "胸部",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "对比2026-01-09胸部CT平扫：双肺透亮度增高，可见多发囊状透亮影；左肺上叶舌段可见两处肿块影，CT值约37-53Hu，分叶状，边界清晰，较前稍扩大，较大者大小约45mm×38mm×47mm（上下径×左右径×前后径），密度不均，其内见结节状高密度影；左肺上叶及双肺下叶可见实性结节，较大者位于右肺下叶外基底段（IM216），大小约11mm×9mm，略呈分叶状；右肺上叶可见结节状高密度灶。气管内斑片状密度增高影此次未见显示。双肺下叶近胸膜处见絮状密度增高影，肺门影不大。纵隔无明显偏移，其内淋巴结不大。心脏大小、形态未见明显异常，心腔密度减低，主动脉壁见斑片状高密度影，双侧胸腔未见积液。肋骨骨质结构未见异常。胸椎椎体边缘变尖。",
  "conclusion": "1.肺气肿伴双肺多发肺大疱，请结合肺功能检查。2.左肺上叶舌段结节及肿块，具恶性征象。3.左肺上叶及双肺下叶实性结节，建议随诊；右肺上叶钙化灶。4.双肺下叶坠积效应，建议复查。5.气管黏液栓较前未见确切显示。6.贫血征象，请结合实验室检查；主动脉粥样硬化。7.胸椎退行性变。（第1-4、6、7条较前大致相仿）",
  "physician": null,
  "reviewer": null
}
2026-08-10 15:00:07,748 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=798045, prompt_len=1248
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共31行）
["报告详情", "姓名", "男63岁", "检查时间", "2026-02-05 17:02:53", "影像所见", "对比2026-01-09胸部CT平扫：双肺透亮度增", "高，可见多发囊状透亮影；左肺上叶舌段可见", "两处肿块影，CT值约37-53Hu，分叶状，边界", "清晰，较前稍扩大，较大者大小约", "45mm×38mm×47mm（上下径×左右径×前后", "径），密度不均，其内见结节状高密度影；左", "肺上叶及双肺下叶可见实性结节，较大者位于", "右肺下叶外基底段（IM216），大小约", "11mm×9mm，略呈分叶状；右肺上叶可见结", "节状高密度灶。气管内斑片状密度增高影此次", "未见显示。双肺下叶近胸膜处见絮状密度增高", "影，肺门影不大。纵隔无明显偏移，其内淋巴", "结不大。心脏大小、形态未见明显异常，心腔", "密度减低，主动脉壁见斑片状高密度影，双侧", "胸腔未见积液。肋骨骨质结构未见异常。胸椎", "椎体边缘变尖。", "诊断意见", "1.肺气肿伴双肺多发肺大疱，请结合肺功能检", "查。2.左肺上叶舌段结节及肿块，具恶性征", "象。3.左肺上叶及双肺下叶实性结节，建议随", "诊；右肺上叶钙化灶。4.双肺下叶坠积效应，", "建议复查。5.气管黏液栓较前未见确切显示。", "6.贫血征象，请结合实验室检查；主动脉粥样", "硬化。7.胸椎退行性变。（第1-4、6、7条较前", "大致相仿）"]

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
2026-08-10 15:00:19,960 INFO     29 [qwen-vl-text] coord API raw response (len=1909):
[
	{"text": "报告详情", "bbox": [328, 142, 422, 160]},
	{"text": "姓名", "bbox": [150, 200, 193, 217]},
	{"text": "男63岁", "bbox": [515, 200, 598, 217]},
	{"text": "检查时间", "bbox": [150, 242, 237, 259]},
	{"text": "2026-02-05 17:02:53", "bbox": [387, 242, 599, 259]},
	{"text": "影像所见", "bbox": [150, 308, 237, 325]},
	{"text": "对比2026-01-09胸部CT平扫：双肺透亮度增", "bbox": [150, 337, 583, 354]},
	{"text": "高，可见多发囊状透亮影；左肺上叶舌段可见", "bbox": [150, 357, 588, 374]},
	{"text": "两处肿块影，CT值约37-53Hu，分叶状，边界", "bbox": [150, 377, 595, 394]},
	{"text": "清晰，较前稍扩大，较大者大小约", "bbox": [150, 397, 479, 414]},
	{"text": "45mm×38mm×47mm（上下径×左右径×前后", "bbox": [150, 417, 592, 434]},
	{"text": "径），密度不均，其内见结节状高密度影；左", "bbox": [150, 437, 589, 454]},
	{"text": "肺上叶及双肺下叶可见实性结节，较大者位于", "bbox": [150, 457, 588, 474]},
	{"text": "右肺下叶外基底段（IM216），大小约", "bbox": [150, 477, 515, 494]},
	{"text": "11mm×9mm，略呈分叶状；右肺上叶可见结", "bbox": [150, 497, 578, 514]},
	{"text": "节状高密度灶。气管内斑片状密度增高影此次", "bbox": [150, 517, 588, 534]},
	{"text": "未见显示。双肺下叶近胸膜处见絮状密度增高", "bbox": [150, 537, 588, 554]},
	{"text": "影，肺门影不大。纵隔无明显偏移，其内淋巴", "bbox": [150, 557, 588, 574]},
	{"text": "结不大。心脏大小、形态未见明显异常，心腔", "bbox": [150, 577, 588, 594]},
	{"text": "密度减低，主动脉壁见斑片状高密度影，双侧", "bbox": [150, 597, 588, 614]},
	{"text": "胸腔未见积液。肋骨骨质结构未见异常。胸椎", "bbox": [150, 617, 588, 634]},
	{"text": "椎体边缘变尖。", "bbox": [150, 637, 300, 654]},
	{"text": "诊断意见", "bbox": [150, 680, 237, 697]},
	{"text": "1.肺气肿伴双肺多发肺大疱，请结合肺功能检", "bbox": [150, 708, 588, 725]},
	{"text": "查。2.左肺上叶舌段结节及肿块，具恶性征", "bbox": [150, 728, 568, 745]},
	{"text": "象。3.左肺上叶及双肺下叶实性结节，建议随", "bbox": [150, 748, 590, 765]},
	{"text": "诊；右肺上叶钙化灶。4.双肺下叶坠积效应，", "bbox": [150, 768, 578, 785]},
	{"text": "建议复查。5.气管黏液栓较前未见确切显示。", "bbox": [150, 788, 588, 805]},
	{"text": "6.贫血征象，请结合实验室检查；主动脉粥样", "bbox": [150, 808, 590, 825]},
	{"text": "硬化。7.胸椎退行性变。（第1-4、6、7条较前", "bbox": [150, 828, 598, 845]},
	{"text": "大致相仿）", "bbox": [150, 848, 247, 865]}
]
2026-08-10 15:00:19,960 INFO     29 [qwen-vl-text] coord API: raw_items=31, valid_items=31, elapsed=12.2s
2026-08-10 15:00:19,960 INFO     29 [qwen-vl-text] coord item[0]: text=报告详情, bbox=[328, 142, 422, 160]
2026-08-10 15:00:19,960 INFO     29 [qwen-vl-text] coord item[1]: text=姓名, bbox=[150, 200, 193, 217]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[2]: text=男63岁, bbox=[515, 200, 598, 217]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[3]: text=检查时间, bbox=[150, 242, 237, 259]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[4]: text=2026-02-05 17:02:53, bbox=[387, 242, 599, 259]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[5]: text=影像所见, bbox=[150, 308, 237, 325]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[6]: text=对比2026-01-09胸部CT平扫：双肺透亮度增, bbox=[150, 337, 583, 354]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[7]: text=高，可见多发囊状透亮影；左肺上叶舌段可见, bbox=[150, 357, 588, 374]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[8]: text=两处肿块影，CT值约37-53Hu，分叶状，边界, bbox=[150, 377, 595, 394]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[9]: text=清晰，较前稍扩大，较大者大小约, bbox=[150, 397, 479, 414]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[10]: text=45mm×38mm×47mm（上下径×左右径×前后, bbox=[150, 417, 592, 434]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[11]: text=径），密度不均，其内见结节状高密度影；左, bbox=[150, 437, 589, 454]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[12]: text=肺上叶及双肺下叶可见实性结节，较大者位于, bbox=[150, 457, 588, 474]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[13]: text=右肺下叶外基底段（IM216），大小约, bbox=[150, 477, 515, 494]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[14]: text=11mm×9mm，略呈分叶状；右肺上叶可见结, bbox=[150, 497, 578, 514]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[15]: text=节状高密度灶。气管内斑片状密度增高影此次, bbox=[150, 517, 588, 534]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[16]: text=未见显示。双肺下叶近胸膜处见絮状密度增高, bbox=[150, 537, 588, 554]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[17]: text=影，肺门影不大。纵隔无明显偏移，其内淋巴, bbox=[150, 557, 588, 574]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[18]: text=结不大。心脏大小、形态未见明显异常，心腔, bbox=[150, 577, 588, 594]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[19]: text=密度减低，主动脉壁见斑片状高密度影，双侧, bbox=[150, 597, 588, 614]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[20]: text=胸腔未见积液。肋骨骨质结构未见异常。胸椎, bbox=[150, 617, 588, 634]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[21]: text=椎体边缘变尖。, bbox=[150, 637, 300, 654]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[22]: text=诊断意见, bbox=[150, 680, 237, 697]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[23]: text=1.肺气肿伴双肺多发肺大疱，请结合肺功能检, bbox=[150, 708, 588, 725]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[24]: text=查。2.左肺上叶舌段结节及肿块，具恶性征, bbox=[150, 728, 568, 745]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[25]: text=象。3.左肺上叶及双肺下叶实性结节，建议随, bbox=[150, 748, 590, 765]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[26]: text=诊；右肺上叶钙化灶。4.双肺下叶坠积效应，, bbox=[150, 768, 578, 785]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[27]: text=建议复查。5.气管黏液栓较前未见确切显示。, bbox=[150, 788, 588, 805]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[28]: text=6.贫血征象，请结合实验室检查；主动脉粥样, bbox=[150, 808, 590, 825]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[29]: text=硬化。7.胸椎退行性变。（第1-4、6、7条较前, bbox=[150, 828, 598, 845]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] coord item[30]: text=大致相仿）, bbox=[150, 848, 247, 865]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] page=4 — 31/31 coords, api_time=12.2s
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] new_positions (31):
[[4, 195.25839599609375, 251.21659484863284, 119.54980346679687, 134.70400390625], [4, 89.29499816894531, 114.89289764404298, 168.3800048828125, 182.69230529785156], [4, 306.5794937133789, 355.9893927001953, 168.3800048828125, 182.69230529785156], [4, 89.29499816894531, 141.0860971069336, 203.73980590820312, 218.05210632324219], [4, 230.38109527587892, 356.5846926879883, 203.73980590820312, 218.05210632324219], [4, 89.29499816894531, 141.0860971069336, 259.3052075195313, 273.6175079345703], [4, 89.29499816894531, 347.0598928833008, 283.7203082275391, 298.0326086425781], [4, 89.29499816894531, 350.03639282226567, 300.5583087158203, 314.8706091308594], [4, 89.29499816894531, 354.20349273681643, 317.39630920410156, 331.70860961914065], [4, 89.29499816894531, 285.14869415283204, 334.23430969238285, 348.5466101074219], [4, 89.29499816894531, 352.4175927734375, 351.0723101806641, 365.3846105957031], [4, 89.29499816894531, 350.6316928100586, 367.9103106689453, 382.22261108398436], [4, 89.29499816894531, 350.03639282226567, 384.74831115722657, 399.06061157226566], [4, 89.29499816894531, 306.5794937133789, 401.5863116455078, 415.8986120605469], [4, 89.29499816894531, 344.08339294433597, 418.4243121337891, 432.73661254882813], [4, 89.29499816894531, 350.03639282226567, 435.26231262207034, 449.5746130371094], [4, 89.29499816894531, 350.03639282226567, 452.1003131103516, 466.41261352539067], [4, 89.29499816894531, 350.03639282226567, 468.9383135986328, 483.2506140136719], [4, 89.29499816894531, 350.03639282226567, 485.77631408691406, 500.08861450195315], [4, 89.29499816894531, 350.03639282226567, 502.61431457519535, 516.9266149902344], [4, 89.29499816894531, 350.03639282226567, 519.4523150634766, 533.7646154785157], [4, 89.29499816894531, 178.58999633789062, 536.2903155517579, 550.6026159667969], [4, 89.29499816894531, 141.0860971069336, 572.4920166015626, 586.8043170166015], [4, 89.29499816894531, 350.03639282226567, 596.0652172851562, 610.3775177001953], [4, 89.29499816894531, 338.13039306640627, 612.9032177734375, 627.2155181884766], [4, 89.29499816894531, 351.22699279785155, 629.7412182617188, 644.0535186767578], [4, 89.29499816894531, 344.08339294433597, 646.57921875, 660.8915191650391], [4, 89.29499816894531, 350.03639282226567, 663.4172192382813, 677.7295196533204], [4, 89.29499816894531, 351.22699279785155, 680.2552197265625, 694.5675201416016], [4, 89.29499816894531, 355.9893927001953, 697.0932202148438, 711.4055206298829], [4, 89.29499816894531, 147.03909698486328, 713.9312207031251, 728.243521118164]]
2026-08-10 15:00:19,961 INFO     29 [qwen-vl-text] ═══ DONE ═══ 31 positions, pages=1, time=16.8s
2026-08-10 15:00:19,961 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:00:19,962 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:00:19,962 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 15:00:19,962 INFO     29 [qwen-vl-text] positions(32): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:00:19,962 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [32]
2026-08-10 15:00:20,096 INFO     29 [qwen-vl-text] page=5, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 15:00:20,097 INFO     29 [qwen-vl-text] LLM extraction start, text_len=585
2026-08-10 15:00:20,097 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:00:20,097 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 130, \"bbox_end\": 161, \"encounter_dates\": [\"2026-01-09\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "报告详情\n姓名\n男 63岁\n检查时间\n2026-01-09 11:07:00\n影像所见\n对比2025-04-14上腹部CT平扫+增强及对比\n2025-04-02下腹部CT平扫+增强：肝脏形\n态、大小未见明显异常；肝内见多枚类圆形低\n密度无强化灶，边界清晰，较大者位于S3，直\n径约13mm；肝内胆管无明显扩张。肝门区结\n构清晰。胆囊不大，壁不厚，腔内未见异常密\n度影。胃、肠管未充盈。胰腺、脾脏及双侧肾\n上腺形态、大小及密度未见明显异常双肾实质\n大小、形态未见异常，双肾可见囊状低密度无\n强化灶，较大者位于左肾，直径约9mm；双侧\n肾盂、肾盏未见扩张。阑尾未见增粗。直肠下\n段管壁增厚，增强扫描不均匀强化，浆膜面稍\n毛糙，周围可见多发淋巴结显示，较大者大小\n约8mm×5mm。前列腺可见结节状高密度影。\n腹腔未见明显积液及游离气体。腹腔及腹膜后\n未见明显增大淋巴结。腹主动脉及双侧髂总动\n脉壁见斑片状高密度影。腰椎椎体边缘变尖。\n诊断意见\n1.直肠下段病变，Ca可能，较前进展，周围多\n发淋巴结，较前稍增多、增大。2.肝内多发囊\n肿。3.双肾周多发渗出，较前已吸收，请结合\n临床。4.双肾多发囊肿。5.考虑升结肠、盲肠\n炎伴周围炎性渗出，较前已吸收。6.前列腺钙\n化灶。7.右侧会阴部积气较前已吸收，请结合\n临床。8.腹主动脉及双侧髂总动脉粥样硬化。\n9.腰椎退行性变。",
    "role": "user"
  }
]
2026-08-10 15:00:24,641 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:00:24,642 INFO     29 [qwen-vl-text] LLM output (len=817):
{
  "exam_date": "2026-01-09",
  "report_date": null,
  "exam_name": "腹部CT平扫+增强",
  "exam_category": "imaging",
  "body_part": "腹部",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "对比2025-04-14上腹部CT平扫+增强及对比2025-04-02下腹部CT平扫+增强：肝脏形态、大小未见明显异常；肝内见多枚类圆形低密度无强化灶，边界清晰，较大者位于S3，直径约13mm；肝内胆管无明显扩张。肝门区结构清晰。胆囊不大，壁不厚，腔内未见异常密度影。胃、肠管未充盈。胰腺、脾脏及双侧肾上腺形态、大小及密度未见明显异常双肾实质大小、形态未见异常，双肾可见囊状低密度无强化灶，较大者位于左肾，直径约9mm；双侧肾盂、肾盏未见扩张。阑尾未见增粗。直肠下段管壁增厚，增强扫描不均匀强化，浆膜面稍毛糙，周围可见多发淋巴结显示，较大者大小约8mm×5mm。前列腺可见结节状高密度影。腹腔未见明显积液及游离气体。腹腔及腹膜后未见明显增大淋巴结。腹主动脉及双侧髂总动脉壁见斑片状高密度影。腰椎椎体边缘变尖。",
  "conclusion": "1.直肠下段病变，Ca可能，较前进展，周围多发淋巴结，较前稍增多、增大。2.肝内多发囊肿。3.双肾周多发渗出，较前已吸收，请结合临床。4.双肾多发囊肿。5.考虑升结肠、盲肠炎伴周围炎性渗出，较前已吸收。6.前列腺钙化灶。7.右侧会阴部积气较前已吸收，请结合临床。8.腹主动脉及双侧髂总动脉粥样硬化。9.腰椎退行性变。",
  "physician": null,
  "reviewer": null
}
2026-08-10 15:00:24,646 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=878884, prompt_len=1294
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共32行）
["报告详情", "姓名", "男 63岁", "检查时间", "2026-01-09 11:07:00", "影像所见", "对比2025-04-14上腹部CT平扫+增强及对比", "2025-04-02下腹部CT平扫+增强：肝脏形", "态、大小未见明显异常；肝内见多枚类圆形低", "密度无强化灶，边界清晰，较大者位于S3，直", "径约13mm；肝内胆管无明显扩张。肝门区结", "构清晰。胆囊不大，壁不厚，腔内未见异常密", "度影。胃、肠管未充盈。胰腺、脾脏及双侧肾", "上腺形态、大小及密度未见明显异常双肾实质", "大小、形态未见异常，双肾可见囊状低密度无", "强化灶，较大者位于左肾，直径约9mm；双侧", "肾盂、肾盏未见扩张。阑尾未见增粗。直肠下", "段管壁增厚，增强扫描不均匀强化，浆膜面稍", "毛糙，周围可见多发淋巴结显示，较大者大小", "约8mm×5mm。前列腺可见结节状高密度影。", "腹腔未见明显积液及游离气体。腹腔及腹膜后", "未见明显增大淋巴结。腹主动脉及双侧髂总动", "脉壁见斑片状高密度影。腰椎椎体边缘变尖。", "诊断意见", "1.直肠下段病变，Ca可能，较前进展，周围多", "发淋巴结，较前稍增多、增大。2.肝内多发囊", "肿。3.双肾周多发渗出，较前已吸收，请结合", "临床。4.双肾多发囊肿。5.考虑升结肠、盲肠", "炎伴周围炎性渗出，较前已吸收。6.前列腺钙", "化灶。7.右侧会阴部积气较前已吸收，请结合", "临床。8.腹主动脉及双侧髂总动脉粥样硬化。", "9.腰椎退行性变。"]

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
2026-08-10 15:00:35,702 INFO     29 [qwen-vl-text] coord API raw response (len=1996):
[
	{"text": "报告详情", "bbox": [328, 142, 422, 160]},
	{"text": "姓名", "bbox": [150, 180, 193, 197]},
	{"text": "男 63岁", "bbox": [523, 180, 598, 197]},
	{"text": "检查时间", "bbox": [150, 221, 237, 238]},
	{"text": "2026-01-09 11:07:00", "bbox": [390, 221, 599, 238]},
	{"text": "影像所见", "bbox": [150, 289, 237, 306]},
	{"text": "对比2025-04-14上腹部CT平扫+增强及对比", "bbox": [150, 317, 574, 334]},
	{"text": "2025-04-02下腹部CT平扫+增强：肝脏形", "bbox": [150, 337, 556, 354]},
	{"text": "态、大小未见明显异常；肝内见多枚类圆形低", "bbox": [150, 357, 588, 374]},
	{"text": "密度无强化灶，边界清晰，较大者位于S3，直", "bbox": [150, 377, 592, 394]},
	{"text": "径约13mm；肝内胆管无明显扩张。肝门区结", "bbox": [150, 397, 584, 414]},
	{"text": "构清晰。胆囊不大，壁不厚，腔内未见异常密", "bbox": [150, 417, 588, 434]},
	{"text": "度影。胃、肠管未充盈。胰腺、脾脏及双侧肾", "bbox": [150, 437, 588, 454]},
	{"text": "上腺形态、大小及密度未见明显异常双肾实质", "bbox": [150, 457, 588, 474]},
	{"text": "大小、形态未见异常，双肾可见囊状低密度无", "bbox": [150, 477, 588, 494]},
	{"text": "强化灶，较大者位于左肾，直径约9mm；双侧", "bbox": [150, 497, 595, 514]},
	{"text": "肾盂、肾盏未见扩张。阑尾未见增粗。直肠下", "bbox": [150, 517, 588, 534]},
	{"text": "段管壁增厚，增强扫描不均匀强化，浆膜面稍", "bbox": [150, 537, 588, 554]},
	{"text": "毛糙，周围可见多发淋巴结显示，较大者大小", "bbox": [150, 557, 588, 574]},
	{"text": "约8mm×5mm。前列腺可见结节状高密度影。", "bbox": [150, 577, 588, 594]},
	{"text": "腹腔未见明显积液及游离气体。腹腔及腹膜后", "bbox": [150, 597, 588, 614]},
	{"text": "未见明显增大淋巴结。腹主动脉及双侧髂总动", "bbox": [150, 617, 588, 634]},
	{"text": "脉壁见斑片状高密度影。腰椎椎体边缘变尖。", "bbox": [150, 637, 588, 654]},
	{"text": "诊断意见", "bbox": [150, 680, 237, 697]},
	{"text": "1.直肠下段病变，Ca可能，较前进展，周围多", "bbox": [150, 708, 590, 725]},
	{"text": "发淋巴结，较前稍增多、增大。2.肝内多发囊", "bbox": [150, 728, 590, 745]},
	{"text": "肿。3.双肾周多发渗出，较前已吸收，请结合", "bbox": [150, 748, 590, 765]},
	{"text": "临床。4.双肾多发囊肿。5.考虑升结肠、盲肠", "bbox": [150, 768, 592, 785]},
	{"text": "炎伴周围炎性渗出，较前已吸收。6.前列腺钙", "bbox": [150, 788, 590, 805]},
	{"text": "化灶。7.右侧会阴部积气较前已吸收，请结合", "bbox": [150, 808, 588, 825]},
	{"text": "临床。8.腹主动脉及双侧髂总动脉粥样硬化。", "bbox": [150, 828, 588, 845]},
	{"text": "9.腰椎退行性变。", "bbox": [150, 848, 324, 865]}
]
2026-08-10 15:00:35,702 INFO     29 [qwen-vl-text] coord API: raw_items=32, valid_items=32, elapsed=11.1s
2026-08-10 15:00:35,702 INFO     29 [qwen-vl-text] coord item[0]: text=报告详情, bbox=[328, 142, 422, 160]
2026-08-10 15:00:35,702 INFO     29 [qwen-vl-text] coord item[1]: text=姓名, bbox=[150, 180, 193, 197]
2026-08-10 15:00:35,702 INFO     29 [qwen-vl-text] coord item[2]: text=男 63岁, bbox=[523, 180, 598, 197]
2026-08-10 15:00:35,702 INFO     29 [qwen-vl-text] coord item[3]: text=检查时间, bbox=[150, 221, 237, 238]
2026-08-10 15:00:35,702 INFO     29 [qwen-vl-text] coord item[4]: text=2026-01-09 11:07:00, bbox=[390, 221, 599, 238]
2026-08-10 15:00:35,702 INFO     29 [qwen-vl-text] coord item[5]: text=影像所见, bbox=[150, 289, 237, 306]
2026-08-10 15:00:35,702 INFO     29 [qwen-vl-text] coord item[6]: text=对比2025-04-14上腹部CT平扫+增强及对比, bbox=[150, 317, 574, 334]
2026-08-10 15:00:35,702 INFO     29 [qwen-vl-text] coord item[7]: text=2025-04-02下腹部CT平扫+增强：肝脏形, bbox=[150, 337, 556, 354]
2026-08-10 15:00:35,702 INFO     29 [qwen-vl-text] coord item[8]: text=态、大小未见明显异常；肝内见多枚类圆形低, bbox=[150, 357, 588, 374]
2026-08-10 15:00:35,702 INFO     29 [qwen-vl-text] coord item[9]: text=密度无强化灶，边界清晰，较大者位于S3，直, bbox=[150, 377, 592, 394]
2026-08-10 15:00:35,703 INFO     29 [qwen-vl-text] coord item[10]: text=径约13mm；肝内胆管无明显扩张。肝门区结, bbox=[150, 397, 584, 414]
2026-08-10 15:00:35,703 INFO     29 [qwen-vl-text] coord item[11]: text=构清晰。胆囊不大，壁不厚，腔内未见异常密, bbox=[150, 417, 588, 434]
2026-08-10 15:00:35,703 INFO     29 [qwen-vl-text] coord item[12]: text=度影。胃、肠管未充盈。胰腺、脾脏及双侧肾, bbox=[150, 437, 588, 454]
2026-08-10 15:00:35,703 INFO     29 [qwen-vl-text] coord item[13]: text=上腺形态、大小及密度未见明显异常双肾实质, bbox=[150, 457, 588, 474]
2026-08-10 15:00:35,703 INFO     29 [qwen-vl-text] coord item[14]: text=大小、形态未见异常，双肾可见囊状低密度无, bbox=[150, 477, 588, 494]
2026-08-10 15:00:35,703 INFO     29 [qwen-vl-text] coord item[15]: text=强化灶，较大者位于左肾，直径约9mm；双侧, bbox=[150, 497, 595, 514]
2026-08-10 15:00:35,703 INFO     29 [qwen-vl-text] coord item[16]: text=肾盂、肾盏未见扩张。阑尾未见增粗。直肠下, bbox=[150, 517, 588, 534]
2026-08-10 15:00:35,703 INFO     29 [qwen-vl-text] coord item[17]: text=段管壁增厚，增强扫描不均匀强化，浆膜面稍, bbox=[150, 537, 588, 554]
2026-08-10 15:00:35,703 INFO     29 [qwen-vl-text] coord item[18]: text=毛糙，周围可见多发淋巴结显示，较大者大小, bbox=[150, 557, 588, 574]
2026-08-10 15:00:35,703 INFO     29 [qwen-vl-text] coord item[19]: text=约8mm×5mm。前列腺可见结节状高密度影。, bbox=[150, 577, 588, 594]
2026-08-10 15:00:35,703 INFO     29 [qwen-vl-text] coord item[20]: text=腹腔未见明显积液及游离气体。腹腔及腹膜后, bbox=[150, 597, 588, 614]
2026-08-10 15:00:35,703 INFO     29 [qwen-vl-text] coord item[21]: text=未见明显增大淋巴结。腹主动脉及双侧髂总动, bbox=[150, 617, 588, 634]
2026-08-10 15:00:35,703 INFO     29 [qwen-vl-text] coord item[22]: text=脉壁见斑片状高密度影。腰椎椎体边缘变尖。, bbox=[150, 637, 588, 654]
2026-08-10 15:00:35,703 INFO     29 [qwen-vl-text] coord item[23]: text=诊断意见, bbox=[150, 680, 237, 697]
2026-08-10 15:00:35,703 INFO     29 [qwen-vl-text] coord item[24]: text=1.直肠下段病变，Ca可能，较前进展，周围多, bbox=[150, 708, 590, 725]
2026-08-10 15:00:35,703 INFO     29 [qwen-vl-text] coord item[25]: text=发淋巴结，较前稍增多、增大。2.肝内多发囊, bbox=[150, 728, 590, 745]
2026-08-10 15:00:35,703 INFO     29 [qwen-vl-text] coord item[26]: text=肿。3.双肾周多发渗出，较前已吸收，请结合, bbox=[150, 748, 590, 765]
2026-08-10 15:00:35,703 INFO     29 [qwen-vl-text] coord item[27]: text=临床。4.双肾多发囊肿。5.考虑升结肠、盲肠, bbox=[150, 768, 592, 785]
2026-08-10 15:00:35,703 INFO     29 [qwen-vl-text] coord item[28]: text=炎伴周围炎性渗出，较前已吸收。6.前列腺钙, bbox=[150, 788, 590, 805]
2026-08-10 15:00:35,703 INFO     29 [qwen-vl-text] coord item[29]: text=化灶。7.右侧会阴部积气较前已吸收，请结合, bbox=[150, 808, 588, 825]
2026-08-10 15:00:35,703 INFO     29 [qwen-vl-text] coord item[30]: text=临床。8.腹主动脉及双侧髂总动脉粥样硬化。, bbox=[150, 828, 588, 845]
2026-08-10 15:00:35,703 INFO     29 [qwen-vl-text] coord item[31]: text=9.腰椎退行性变。, bbox=[150, 848, 324, 865]
2026-08-10 15:00:35,703 INFO     29 [qwen-vl-text] page=5 — 32/32 coords, api_time=11.1s
2026-08-10 15:00:35,703 INFO     29 [qwen-vl-text] new_positions (32):
[[5, 195.25839599609375, 251.21659484863284, 119.54980346679687, 134.70400390625], [5, 89.29499816894531, 114.89289764404298, 151.54200439453126, 165.85430480957032], [5, 311.34189361572265, 355.9893927001953, 151.54200439453126, 165.85430480957032], [5, 89.29499816894531, 141.0860971069336, 186.05990539550783, 200.3722058105469], [5, 232.16699523925783, 356.5846926879883, 186.05990539550783, 200.3722058105469], [5, 89.29499816894531, 141.0860971069336, 243.30910705566407, 257.62140747070316], [5, 89.29499816894531, 341.7021929931641, 266.88230773925784, 281.1946081542969], [5, 89.29499816894531, 330.98679321289063, 283.7203082275391, 298.0326086425781], [5, 89.29499816894531, 350.03639282226567, 300.5583087158203, 314.8706091308594], [5, 89.29499816894531, 352.4175927734375, 317.39630920410156, 331.70860961914065], [5, 89.29499816894531, 347.6551928710938, 334.23430969238285, 348.5466101074219], [5, 89.29499816894531, 350.03639282226567, 351.0723101806641, 365.3846105957031], [5, 89.29499816894531, 350.03639282226567, 367.9103106689453, 382.22261108398436], [5, 89.29499816894531, 350.03639282226567, 384.74831115722657, 399.06061157226566], [5, 89.29499816894531, 350.03639282226567, 401.5863116455078, 415.8986120605469], [5, 89.29499816894531, 354.20349273681643, 418.4243121337891, 432.73661254882813], [5, 89.29499816894531, 350.03639282226567, 435.26231262207034, 449.5746130371094], [5, 89.29499816894531, 350.03639282226567, 452.1003131103516, 466.41261352539067], [5, 89.29499816894531, 350.03639282226567, 468.9383135986328, 483.2506140136719], [5, 89.29499816894531, 350.03639282226567, 485.77631408691406, 500.08861450195315], [5, 89.29499816894531, 350.03639282226567, 502.61431457519535, 516.9266149902344], [5, 89.29499816894531, 350.03639282226567, 519.4523150634766, 533.7646154785157], [5, 89.29499816894531, 350.03639282226567, 536.2903155517579, 550.6026159667969], [5, 89.29499816894531, 141.0860971069336, 572.4920166015626, 586.8043170166015], [5, 89.29499816894531, 351.22699279785155, 596.0652172851562, 610.3775177001953], [5, 89.29499816894531, 351.22699279785155, 612.9032177734375, 627.2155181884766], [5, 89.29499816894531, 351.22699279785155, 629.7412182617188, 644.0535186767578], [5, 89.29499816894531, 352.4175927734375, 646.57921875, 660.8915191650391], [5, 89.29499816894531, 351.22699279785155, 663.4172192382813, 677.7295196533204], [5, 89.29499816894531, 350.03639282226567, 680.2552197265625, 694.5675201416016], [5, 89.29499816894531, 350.03639282226567, 697.0932202148438, 711.4055206298829], [5, 89.29499816894531, 192.87719604492187, 713.9312207031251, 728.243521118164]]
2026-08-10 15:00:35,703 INFO     29 [qwen-vl-text] ═══ DONE ═══ 32 positions, pages=1, time=15.7s
2026-08-10 15:00:35,703 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:00:35,709 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:00:35,709 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 15:00:35,709 INFO     29 [qwen-vl-text] positions(31): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:00:35,709 INFO     29 [qwen-vl-text] page grouping: [6], lines per page: [31]
2026-08-10 15:00:35,839 INFO     29 [qwen-vl-text] page=6, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 15:00:35,839 INFO     29 [qwen-vl-text] LLM extraction start, text_len=548
2026-08-10 15:00:35,839 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:00:35,840 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 167, \"bbox_end\": 197, \"encounter_dates\": [\"2026-01-09\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "报告详情\n姓名\n男63岁\n检查时间\n2026-01-09 09:32:00\n影像所见\n对比2025-08-11胸部CT平扫：双肺透亮度增\n高，可见多发囊状透亮影；左肺上叶舌段可见\n两处肿块影，CT值约22-61Hu，分叶状，边界\n清晰，较前稍扩大，较大者大小约\n45mm×36mm×42mm（上下径×左右径×前后\n径），密度不均，其内见结节状高密度影；左\n肺上叶及双肺下叶可见实性结节，较大者位于\n右肺下叶，直径约7mm；右肺上叶可见结节状\n高密度灶。新增气管内斑片状密度增高影。双\n肺下叶近胸膜处见絮状密度增高影，肺门影不\n大。纵隔无明显偏移，其内淋巴结不大。心脏\n大小、形态未见明显异常，心腔密度减低，主\n动脉壁见斑片状高密度影，上腔静脉内导管影\n此次未见显示。双侧胸腔未见积液。肋骨骨质\n结构未见异常。胸椎椎体边缘变尖。\n诊断意见\n1.肺气肿伴双肺多发肺大疱，请结合肺功能检\n查。2.左肺上叶舌段结节及肿块，具恶性征\n象，较前增大。3.左肺上叶及双肺下叶实性结\n节，右肺中叶实性结节较前未见确切显示，建\n议随诊；右肺上叶钙化灶。4.新增双肺下叶坠\n积效应，建议复查。5.新增气管黏液栓。6.贫\n血征象，请结合实验室检查；主动脉粥样硬\n化。7.胸椎退行性变。8.PICC管较前未见确切\n显示。",
    "role": "user"
  }
]
2026-08-10 15:00:35,842 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:00:35.841+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 64, "failed": 0, "current": {"7630dbd094ca11f1bd9827cf206dfa2d": {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:00:40,189 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:00:40,190 INFO     29 [qwen-vl-text] LLM output (len=777):
{
  "exam_date": "2026-01-09",
  "report_date": null,
  "exam_name": "胸部CT",
  "exam_category": "imaging",
  "body_part": "胸部",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "对比2025-08-11胸部CT平扫：双肺透亮度增高，可见多发囊状透亮影；左肺上叶舌段可见两处肿块影，CT值约22-61Hu，分叶状，边界清晰，较前稍扩大，较大者大小约45mm×36mm×42mm（上下径×左右径×前后径），密度不均，其内见结节状高密度影；左肺上叶及双肺下叶可见实性结节，较大者位于右肺下叶，直径约7mm；右肺上叶可见结节状高密度灶。新增气管内斑片状密度增高影。双肺下叶近胸膜处见絮状密度增高影，肺门影不大。纵隔无明显偏移，其内淋巴结不大。心脏大小、形态未见明显异常，心腔密度减低，主动脉壁见斑片状高密度影，上腔静脉内导管影此次未见显示。双侧胸腔未见积液。肋骨骨质结构未见异常。胸椎椎体边缘变尖。",
  "conclusion": "1.肺气肿伴双肺多发肺大疱，请结合肺功能检查。2.左肺上叶舌段结节及肿块，具恶性征象，较前增大。3.左肺上叶及双肺下叶实性结节，右肺中叶实性结节较前未见确切显示，建议随诊；右肺上叶钙化灶。4.新增双肺下叶坠积效应，建议复查。5.新增气管黏液栓。6.贫血征象，请结合实验室检查；主动脉粥样硬化。7.胸椎退行性变。8.PICC管较前未见确切显示。",
  "physician": null,
  "reviewer": null
}
2026-08-10 15:00:40,193 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=816663, prompt_len=1254
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共31行）
["报告详情", "姓名", "男63岁", "检查时间", "2026-01-09 09:32:00", "影像所见", "对比2025-08-11胸部CT平扫：双肺透亮度增", "高，可见多发囊状透亮影；左肺上叶舌段可见", "两处肿块影，CT值约22-61Hu，分叶状，边界", "清晰，较前稍扩大，较大者大小约", "45mm×36mm×42mm（上下径×左右径×前后", "径），密度不均，其内见结节状高密度影；左", "肺上叶及双肺下叶可见实性结节，较大者位于", "右肺下叶，直径约7mm；右肺上叶可见结节状", "高密度灶。新增气管内斑片状密度增高影。双", "肺下叶近胸膜处见絮状密度增高影，肺门影不", "大。纵隔无明显偏移，其内淋巴结不大。心脏", "大小、形态未见明显异常，心腔密度减低，主", "动脉壁见斑片状高密度影，上腔静脉内导管影", "此次未见显示。双侧胸腔未见积液。肋骨骨质", "结构未见异常。胸椎椎体边缘变尖。", "诊断意见", "1.肺气肿伴双肺多发肺大疱，请结合肺功能检", "查。2.左肺上叶舌段结节及肿块，具恶性征", "象，较前增大。3.左肺上叶及双肺下叶实性结", "节，右肺中叶实性结节较前未见确切显示，建", "议随诊；右肺上叶钙化灶。4.新增双肺下叶坠", "积效应，建议复查。5.新增气管黏液栓。6.贫", "血征象，请结合实验室检查；主动脉粥样硬", "化。7.胸椎退行性变。8.PICC管较前未见确切", "显示。"]

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
2026-08-10 15:00:51,693 INFO     29 [qwen-vl-text] coord API raw response (len=1915):
[
	{"text": "报告详情", "bbox": [328, 142, 422, 160]},
	{"text": "姓名", "bbox": [150, 200, 193, 217]},
	{"text": "男63岁", "bbox": [523, 200, 598, 217]},
	{"text": "检查时间", "bbox": [150, 242, 237, 259]},
	{"text": "2026-01-09 09:32:00", "bbox": [381, 242, 599, 259]},
	{"text": "影像所见", "bbox": [150, 308, 237, 325]},
	{"text": "对比2025-08-11胸部CT平扫：双肺透亮度增", "bbox": [150, 337, 579, 354]},
	{"text": "高，可见多发囊状透亮影；左肺上叶舌段可见", "bbox": [150, 357, 588, 374]},
	{"text": "两处肿块影，CT值约22-61Hu，分叶状，边界", "bbox": [150, 377, 590, 394]},
	{"text": "清晰，较前稍扩大，较大者大小约", "bbox": [150, 397, 479, 414]},
	{"text": "45mm×36mm×42mm（上下径×左右径×前后", "bbox": [150, 417, 593, 434]},
	{"text": "径），密度不均，其内见结节状高密度影；左", "bbox": [150, 437, 589, 454]},
	{"text": "肺上叶及双肺下叶可见实性结节，较大者位于", "bbox": [150, 457, 589, 474]},
	{"text": "右肺下叶，直径约7mm；右肺上叶可见结节状", "bbox": [150, 477, 594, 494]},
	{"text": "高密度灶。新增气管内斑片状密度增高影。双", "bbox": [150, 497, 588, 514]},
	{"text": "肺下叶近胸膜处见絮状密度增高影，肺门影不", "bbox": [150, 517, 588, 534]},
	{"text": "大。纵隔无明显偏移，其内淋巴结不大。心脏", "bbox": [150, 537, 588, 554]},
	{"text": "大小、形态未见明显异常，心腔密度减低，主", "bbox": [150, 557, 588, 574]},
	{"text": "动脉壁见斑片状高密度影，上腔静脉内导管影", "bbox": [150, 577, 588, 594]},
	{"text": "此次未见显示。双侧胸腔未见积液。肋骨骨质", "bbox": [150, 597, 588, 614]},
	{"text": "结构未见异常。胸椎椎体边缘变尖。", "bbox": [150, 617, 491, 634]},
	{"text": "诊断意见", "bbox": [150, 660, 237, 677]},
	{"text": "1.肺气肿伴双肺多发肺大疱，请结合肺功能检", "bbox": [150, 688, 587, 705]},
	{"text": "查。2.左肺上叶舌段结节及肿块，具恶性征", "bbox": [150, 708, 569, 725]},
	{"text": "象，较前增大。3.左肺上叶及双肺下叶实性结", "bbox": [150, 728, 590, 745]},
	{"text": "节，右肺中叶实性结节较前未见确切显示，建", "bbox": [150, 748, 588, 765]},
	{"text": "议随诊；右肺上叶钙化灶。4.新增双肺下叶坠", "bbox": [150, 768, 590, 785]},
	{"text": "积效应，建议复查。5.新增气管黏液栓。6.贫", "bbox": [150, 788, 592, 805]},
	{"text": "血征象，请结合实验室检查；主动脉粥样硬", "bbox": [150, 808, 566, 825]},
	{"text": "化。7.胸椎退行性变。8.PICC管较前未见确切", "bbox": [150, 828, 594, 845]},
	{"text": "显示。", "bbox": [150, 848, 204, 865]}
]
2026-08-10 15:00:51,693 INFO     29 [qwen-vl-text] coord API: raw_items=31, valid_items=31, elapsed=11.5s
2026-08-10 15:00:51,693 INFO     29 [qwen-vl-text] coord item[0]: text=报告详情, bbox=[328, 142, 422, 160]
2026-08-10 15:00:51,694 INFO     29 [qwen-vl-text] coord item[1]: text=姓名, bbox=[150, 200, 193, 217]
2026-08-10 15:00:51,694 INFO     29 [qwen-vl-text] coord item[2]: text=男63岁, bbox=[523, 200, 598, 217]
2026-08-10 15:00:51,694 INFO     29 [qwen-vl-text] coord item[3]: text=检查时间, bbox=[150, 242, 237, 259]
2026-08-10 15:00:51,694 INFO     29 [qwen-vl-text] coord item[4]: text=2026-01-09 09:32:00, bbox=[381, 242, 599, 259]
2026-08-10 15:00:51,694 INFO     29 [qwen-vl-text] coord item[5]: text=影像所见, bbox=[150, 308, 237, 325]
2026-08-10 15:00:51,694 INFO     29 [qwen-vl-text] coord item[6]: text=对比2025-08-11胸部CT平扫：双肺透亮度增, bbox=[150, 337, 579, 354]
2026-08-10 15:00:51,694 INFO     29 [qwen-vl-text] coord item[7]: text=高，可见多发囊状透亮影；左肺上叶舌段可见, bbox=[150, 357, 588, 374]
2026-08-10 15:00:51,694 INFO     29 [qwen-vl-text] coord item[8]: text=两处肿块影，CT值约22-61Hu，分叶状，边界, bbox=[150, 377, 590, 394]
2026-08-10 15:00:51,694 INFO     29 [qwen-vl-text] coord item[9]: text=清晰，较前稍扩大，较大者大小约, bbox=[150, 397, 479, 414]
2026-08-10 15:00:51,694 INFO     29 [qwen-vl-text] coord item[10]: text=45mm×36mm×42mm（上下径×左右径×前后, bbox=[150, 417, 593, 434]
2026-08-10 15:00:51,694 INFO     29 [qwen-vl-text] coord item[11]: text=径），密度不均，其内见结节状高密度影；左, bbox=[150, 437, 589, 454]
2026-08-10 15:00:51,694 INFO     29 [qwen-vl-text] coord item[12]: text=肺上叶及双肺下叶可见实性结节，较大者位于, bbox=[150, 457, 589, 474]
2026-08-10 15:00:51,694 INFO     29 [qwen-vl-text] coord item[13]: text=右肺下叶，直径约7mm；右肺上叶可见结节状, bbox=[150, 477, 594, 494]
2026-08-10 15:00:51,694 INFO     29 [qwen-vl-text] coord item[14]: text=高密度灶。新增气管内斑片状密度增高影。双, bbox=[150, 497, 588, 514]
2026-08-10 15:00:51,694 INFO     29 [qwen-vl-text] coord item[15]: text=肺下叶近胸膜处见絮状密度增高影，肺门影不, bbox=[150, 517, 588, 534]
2026-08-10 15:00:51,694 INFO     29 [qwen-vl-text] coord item[16]: text=大。纵隔无明显偏移，其内淋巴结不大。心脏, bbox=[150, 537, 588, 554]
2026-08-10 15:00:51,694 INFO     29 [qwen-vl-text] coord item[17]: text=大小、形态未见明显异常，心腔密度减低，主, bbox=[150, 557, 588, 574]
2026-08-10 15:00:51,694 INFO     29 [qwen-vl-text] coord item[18]: text=动脉壁见斑片状高密度影，上腔静脉内导管影, bbox=[150, 577, 588, 594]
2026-08-10 15:00:51,694 INFO     29 [qwen-vl-text] coord item[19]: text=此次未见显示。双侧胸腔未见积液。肋骨骨质, bbox=[150, 597, 588, 614]
2026-08-10 15:00:51,694 INFO     29 [qwen-vl-text] coord item[20]: text=结构未见异常。胸椎椎体边缘变尖。, bbox=[150, 617, 491, 634]
2026-08-10 15:00:51,694 INFO     29 [qwen-vl-text] coord item[21]: text=诊断意见, bbox=[150, 660, 237, 677]
2026-08-10 15:00:51,694 INFO     29 [qwen-vl-text] coord item[22]: text=1.肺气肿伴双肺多发肺大疱，请结合肺功能检, bbox=[150, 688, 587, 705]
2026-08-10 15:00:51,694 INFO     29 [qwen-vl-text] coord item[23]: text=查。2.左肺上叶舌段结节及肿块，具恶性征, bbox=[150, 708, 569, 725]
2026-08-10 15:00:51,694 INFO     29 [qwen-vl-text] coord item[24]: text=象，较前增大。3.左肺上叶及双肺下叶实性结, bbox=[150, 728, 590, 745]
2026-08-10 15:00:51,695 INFO     29 [qwen-vl-text] coord item[25]: text=节，右肺中叶实性结节较前未见确切显示，建, bbox=[150, 748, 588, 765]
2026-08-10 15:00:51,695 INFO     29 [qwen-vl-text] coord item[26]: text=议随诊；右肺上叶钙化灶。4.新增双肺下叶坠, bbox=[150, 768, 590, 785]
2026-08-10 15:00:51,695 INFO     29 [qwen-vl-text] coord item[27]: text=积效应，建议复查。5.新增气管黏液栓。6.贫, bbox=[150, 788, 592, 805]
2026-08-10 15:00:51,695 INFO     29 [qwen-vl-text] coord item[28]: text=血征象，请结合实验室检查；主动脉粥样硬, bbox=[150, 808, 566, 825]
2026-08-10 15:00:51,695 INFO     29 [qwen-vl-text] coord item[29]: text=化。7.胸椎退行性变。8.PICC管较前未见确切, bbox=[150, 828, 594, 845]
2026-08-10 15:00:51,695 INFO     29 [qwen-vl-text] coord item[30]: text=显示。, bbox=[150, 848, 204, 865]
2026-08-10 15:00:51,695 INFO     29 [qwen-vl-text] page=6 — 31/31 coords, api_time=11.5s
2026-08-10 15:00:51,695 INFO     29 [qwen-vl-text] new_positions (31):
[[6, 195.25839599609375, 251.21659484863284, 119.54980346679687, 134.70400390625], [6, 89.29499816894531, 114.89289764404298, 168.3800048828125, 182.69230529785156], [6, 311.34189361572265, 355.9893927001953, 168.3800048828125, 182.69230529785156], [6, 89.29499816894531, 141.0860971069336, 203.73980590820312, 218.05210632324219], [6, 226.8092953491211, 356.5846926879883, 203.73980590820312, 218.05210632324219], [6, 89.29499816894531, 141.0860971069336, 259.3052075195313, 273.6175079345703], [6, 89.29499816894531, 344.6786929321289, 283.7203082275391, 298.0326086425781], [6, 89.29499816894531, 350.03639282226567, 300.5583087158203, 314.8706091308594], [6, 89.29499816894531, 351.22699279785155, 317.39630920410156, 331.70860961914065], [6, 89.29499816894531, 285.14869415283204, 334.23430969238285, 348.5466101074219], [6, 89.29499816894531, 353.0128927612305, 351.0723101806641, 365.3846105957031], [6, 89.29499816894531, 350.6316928100586, 367.9103106689453, 382.22261108398436], [6, 89.29499816894531, 350.6316928100586, 384.74831115722657, 399.06061157226566], [6, 89.29499816894531, 353.60819274902343, 401.5863116455078, 415.8986120605469], [6, 89.29499816894531, 350.03639282226567, 418.4243121337891, 432.73661254882813], [6, 89.29499816894531, 350.03639282226567, 435.26231262207034, 449.5746130371094], [6, 89.29499816894531, 350.03639282226567, 452.1003131103516, 466.41261352539067], [6, 89.29499816894531, 350.03639282226567, 468.9383135986328, 483.2506140136719], [6, 89.29499816894531, 350.03639282226567, 485.77631408691406, 500.08861450195315], [6, 89.29499816894531, 350.03639282226567, 502.61431457519535, 516.9266149902344], [6, 89.29499816894531, 292.2922940063477, 519.4523150634766, 533.7646154785157], [6, 89.29499816894531, 141.0860971069336, 555.6540161132813, 569.9663165283204], [6, 89.29499816894531, 349.44109283447267, 579.227216796875, 593.5395172119141], [6, 89.29499816894531, 338.7256930541992, 596.0652172851562, 610.3775177001953], [6, 89.29499816894531, 351.22699279785155, 612.9032177734375, 627.2155181884766], [6, 89.29499816894531, 350.03639282226567, 629.7412182617188, 644.0535186767578], [6, 89.29499816894531, 351.22699279785155, 646.57921875, 660.8915191650391], [6, 89.29499816894531, 352.4175927734375, 663.4172192382813, 677.7295196533204], [6, 89.29499816894531, 336.93979309082033, 680.2552197265625, 694.5675201416016], [6, 89.29499816894531, 353.60819274902343, 697.0932202148438, 711.4055206298829], [6, 89.29499816894531, 121.44119750976563, 713.9312207031251, 728.243521118164]]
2026-08-10 15:00:51,695 INFO     29 [qwen-vl-text] ═══ DONE ═══ 31 positions, pages=1, time=16.0s
2026-08-10 15:00:51,695 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:00:51,697 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:00:51,697 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 15:00:51,697 INFO     29 [qwen-vl-text] positions(29): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:00:51,697 INFO     29 [qwen-vl-text] page grouping: [7], lines per page: [29]
2026-08-10 15:00:51,823 INFO     29 [qwen-vl-text] page=7, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 15:00:51,823 INFO     29 [qwen-vl-text] LLM extraction start, text_len=496
2026-08-10 15:00:51,823 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:00:51,823 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 203, \"bbox_end\": 231, \"encounter_dates\": [\"2025-06-21\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "报告详情\n检查\n胸部CT平扫+三维重建\n姓名\n男 63岁\n检查时间\n2025-06-21 17:57:05\n影像所见\n对比2025-05-26胸部CT平扫：双肺透亮度增高，可见多发囊状透亮影；左肺上叶舌段可见\n两处肿块影，CT值约33-57Hu，分叶状，边界\n清晰，较大者大小约47mm×35mm×43mm\n（上下径×左右径×前后径）；左肺下叶后基底\n段、右肺中叶内侧段、右肺下叶外基底段可见\n实性结节，较大者位于右肺下叶，直径约\n6mm；右肺上叶可见结节状高密度灶。气管内\n斑片状密度增高影未见显示。肺门影不大。纵\n隔无明显偏移，其内淋巴结不大。心脏大小、\n形态未见明显异常，心腔密度减低，主动脉壁\n见斑片状高密度影，上腔静脉内见导管影。双\n侧胸腔未见积液。肋骨骨质结构未见异常。胸\n椎椎体边缘变尖。\n诊断意见\n1.肺气肿伴双肺多发肺大疱，请结合肺功能检\n查。2.左肺上叶舌段肿块，具恶性征象，建议\n复查。3.右肺中叶、双肺下叶实性结节，建议\n随诊；右肺上叶钙化灶。4.贫血征象，请结合\n实验室检查；主动脉粥样硬化。5.胸椎退行性\n变。6.PICC管置入术后。（上述1-5条较前大\n致相仿）",
    "role": "user"
  }
]
2026-08-10 15:00:55,907 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:00:55,907 INFO     29 [qwen-vl-text] LLM output (len=720):
{
  "exam_date": "2025-06-21",
  "report_date": null,
  "exam_name": "胸部CT平扫+三维重建",
  "exam_category": "imaging",
  "body_part": "胸部",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": "对比2025-05-26胸部CT平扫：双肺透亮度增高，可见多发囊状透亮影；左肺上叶舌段可见两处肿块影，CT值约33-57Hu，分叶状，边界清晰，较大者大小约47mm×35mm×43mm（上下径×左右径×前后径）；左肺下叶后基底段、右肺中叶内侧段、右肺下叶外基底段可见实性结节，较大者位于右肺下叶，直径约6mm；右肺上叶可见结节状高密度灶。气管内斑片状密度增高影未见显示。肺门影不大。纵隔无明显偏移，其内淋巴结不大。心脏大小、形态未见明显异常，心腔密度减低，主动脉壁见斑片状高密度影，上腔静脉内见导管影。双侧胸腔未见积液。肋骨骨质结构未见异常。胸椎椎体边缘变尖。",
  "conclusion": "1.肺气肿伴双肺多发肺大疱，请结合肺功能检查。2.左肺上叶舌段肿块，具恶性征象，建议复查。3.右肺中叶、双肺下叶实性结节，建议随诊；右肺上叶钙化灶。4.贫血征象，请结合实验室检查；主动脉粥样硬化。5.胸椎退行性变。6.PICC管置入术后。（上述1-5条较前大致相仿）",
  "physician": null,
  "reviewer": null
}
2026-08-10 15:00:55,908 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=743706, prompt_len=1196
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共29行）
["报告详情", "检查", "胸部CT平扫+三维重建", "姓名", "男 63岁", "检查时间", "2025-06-21 17:57:05", "影像所见", "对比2025-05-26胸部CT平扫：双肺透亮度增高，可见多发囊状透亮影；左肺上叶舌段可见", "两处肿块影，CT值约33-57Hu，分叶状，边界", "清晰，较大者大小约47mm×35mm×43mm", "（上下径×左右径×前后径）；左肺下叶后基底", "段、右肺中叶内侧段、右肺下叶外基底段可见", "实性结节，较大者位于右肺下叶，直径约", "6mm；右肺上叶可见结节状高密度灶。气管内", "斑片状密度增高影未见显示。肺门影不大。纵", "隔无明显偏移，其内淋巴结不大。心脏大小、", "形态未见明显异常，心腔密度减低，主动脉壁", "见斑片状高密度影，上腔静脉内见导管影。双", "侧胸腔未见积液。肋骨骨质结构未见异常。胸", "椎椎体边缘变尖。", "诊断意见", "1.肺气肿伴双肺多发肺大疱，请结合肺功能检", "查。2.左肺上叶舌段肿块，具恶性征象，建议", "复查。3.右肺中叶、双肺下叶实性结节，建议", "随诊；右肺上叶钙化灶。4.贫血征象，请结合", "实验室检查；主动脉粥样硬化。5.胸椎退行性", "变。6.PICC管置入术后。（上述1-5条较前大", "致相仿）"]

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
2026-08-10 15:01:05,999 INFO     29 [qwen-vl-text] coord API raw response (len=1775):
[
	{"text": "报告详情", "bbox": [328, 142, 422, 160]},
	{"text": "检查", "bbox": [150, 171, 226, 187]},
	{"text": "胸部CT平扫+三维重建", "bbox": [150, 196, 392, 214]},
	{"text": "姓名", "bbox": [150, 260, 193, 277]},
	{"text": "男 63岁", "bbox": [523, 260, 598, 277]},
	{"text": "检查时间", "bbox": [150, 302, 237, 319]},
	{"text": "2025-06-21 17:57:05", "bbox": [391, 302, 600, 319]},
	{"text": "影像所见", "bbox": [150, 368, 237, 385]},
	{"text": "对比2025-05-26胸部CT平扫：双肺透亮度增高，可见多发囊状透亮影；左肺上叶舌段可见", "bbox": [150, 397, 588, 433]},
	{"text": "两处肿块影，CT值约33-57Hu，分叶状，边界", "bbox": [150, 436, 595, 454]},
	{"text": "清晰，较大者大小约47mm×35mm×43mm", "bbox": [150, 457, 565, 474]},
	{"text": "（上下径×左右径×前后径）；左肺下叶后基底", "bbox": [162, 477, 593, 495]},
	{"text": "段、右肺中叶内侧段、右肺下叶外基底段可见", "bbox": [150, 497, 588, 515]},
	{"text": "实性结节，较大者位于右肺下叶，直径约", "bbox": [150, 517, 543, 535]},
	{"text": "6mm；右肺上叶可见结节状高密度灶。气管内", "bbox": [150, 537, 595, 555]},
	{"text": "斑片状密度增高影未见显示。肺门影不大。纵", "bbox": [150, 557, 588, 575]},
	{"text": "隔无明显偏移，其内淋巴结不大。心脏大小、", "bbox": [150, 577, 577, 595]},
	{"text": "形态未见明显异常，心腔密度减低，主动脉壁", "bbox": [150, 597, 588, 615]},
	{"text": "见斑片状高密度影，上腔静脉内见导管影。双", "bbox": [150, 617, 588, 635]},
	{"text": "侧胸腔未见积液。肋骨骨质结构未见异常。胸", "bbox": [150, 637, 588, 655]},
	{"text": "椎椎体边缘变尖。", "bbox": [150, 658, 315, 675]},
	{"text": "诊断意见", "bbox": [150, 700, 237, 717]},
	{"text": "1.肺气肿伴双肺多发肺大疱，请结合肺功能检", "bbox": [150, 727, 588, 745]},
	{"text": "查。2.左肺上叶舌段肿块，具恶性征象，建议", "bbox": [150, 747, 590, 765]},
	{"text": "复查。3.右肺中叶、双肺下叶实性结节，建议", "bbox": [150, 767, 590, 785]},
	{"text": "随诊；右肺上叶钙化灶。4.贫血征象，请结合", "bbox": [150, 787, 590, 805]},
	{"text": "实验室检查；主动脉粥样硬化。5.胸椎退行性", "bbox": [150, 807, 590, 825]},
	{"text": "变。6.PICC管置入术后。（上述1-5条较前大", "bbox": [150, 827, 583, 845]},
	{"text": "致相仿）", "bbox": [150, 848, 224, 865]}
]
2026-08-10 15:01:06,001 INFO     29 [qwen-vl-text] coord API: raw_items=29, valid_items=29, elapsed=10.1s
2026-08-10 15:01:06,001 INFO     29 [qwen-vl-text] coord item[0]: text=报告详情, bbox=[328, 142, 422, 160]
2026-08-10 15:01:06,001 INFO     29 [qwen-vl-text] coord item[1]: text=检查, bbox=[150, 171, 226, 187]
2026-08-10 15:01:06,001 INFO     29 [qwen-vl-text] coord item[2]: text=胸部CT平扫+三维重建, bbox=[150, 196, 392, 214]
2026-08-10 15:01:06,001 INFO     29 [qwen-vl-text] coord item[3]: text=姓名, bbox=[150, 260, 193, 277]
2026-08-10 15:01:06,001 INFO     29 [qwen-vl-text] coord item[4]: text=男 63岁, bbox=[523, 260, 598, 277]
2026-08-10 15:01:06,001 INFO     29 [qwen-vl-text] coord item[5]: text=检查时间, bbox=[150, 302, 237, 319]
2026-08-10 15:01:06,001 INFO     29 [qwen-vl-text] coord item[6]: text=2025-06-21 17:57:05, bbox=[391, 302, 600, 319]
2026-08-10 15:01:06,002 INFO     29 [qwen-vl-text] coord item[7]: text=影像所见, bbox=[150, 368, 237, 385]
2026-08-10 15:01:06,002 INFO     29 [qwen-vl-text] coord item[8]: text=对比2025-05-26胸部CT平扫：双肺透亮度增高，可见多发囊状透亮影；左肺上叶舌段可见, bbox=[150, 397, 588, 433]
2026-08-10 15:01:06,002 INFO     29 [qwen-vl-text] coord item[9]: text=两处肿块影，CT值约33-57Hu，分叶状，边界, bbox=[150, 436, 595, 454]
2026-08-10 15:01:06,002 INFO     29 [qwen-vl-text] coord item[10]: text=清晰，较大者大小约47mm×35mm×43mm, bbox=[150, 457, 565, 474]
2026-08-10 15:01:06,002 INFO     29 [qwen-vl-text] coord item[11]: text=（上下径×左右径×前后径）；左肺下叶后基底, bbox=[162, 477, 593, 495]
2026-08-10 15:01:06,002 INFO     29 [qwen-vl-text] coord item[12]: text=段、右肺中叶内侧段、右肺下叶外基底段可见, bbox=[150, 497, 588, 515]
2026-08-10 15:01:06,002 INFO     29 [qwen-vl-text] coord item[13]: text=实性结节，较大者位于右肺下叶，直径约, bbox=[150, 517, 543, 535]
2026-08-10 15:01:06,002 INFO     29 [qwen-vl-text] coord item[14]: text=6mm；右肺上叶可见结节状高密度灶。气管内, bbox=[150, 537, 595, 555]
2026-08-10 15:01:06,002 INFO     29 [qwen-vl-text] coord item[15]: text=斑片状密度增高影未见显示。肺门影不大。纵, bbox=[150, 557, 588, 575]
2026-08-10 15:01:06,003 INFO     29 [qwen-vl-text] coord item[16]: text=隔无明显偏移，其内淋巴结不大。心脏大小、, bbox=[150, 577, 577, 595]
2026-08-10 15:01:06,003 INFO     29 [qwen-vl-text] coord item[17]: text=形态未见明显异常，心腔密度减低，主动脉壁, bbox=[150, 597, 588, 615]
2026-08-10 15:01:06,003 INFO     29 [qwen-vl-text] coord item[18]: text=见斑片状高密度影，上腔静脉内见导管影。双, bbox=[150, 617, 588, 635]
2026-08-10 15:01:06,003 INFO     29 [qwen-vl-text] coord item[19]: text=侧胸腔未见积液。肋骨骨质结构未见异常。胸, bbox=[150, 637, 588, 655]
2026-08-10 15:01:06,003 INFO     29 [qwen-vl-text] coord item[20]: text=椎椎体边缘变尖。, bbox=[150, 658, 315, 675]
2026-08-10 15:01:06,003 INFO     29 [qwen-vl-text] coord item[21]: text=诊断意见, bbox=[150, 700, 237, 717]
2026-08-10 15:01:06,003 INFO     29 [qwen-vl-text] coord item[22]: text=1.肺气肿伴双肺多发肺大疱，请结合肺功能检, bbox=[150, 727, 588, 745]
2026-08-10 15:01:06,003 INFO     29 [qwen-vl-text] coord item[23]: text=查。2.左肺上叶舌段肿块，具恶性征象，建议, bbox=[150, 747, 590, 765]
2026-08-10 15:01:06,003 INFO     29 [qwen-vl-text] coord item[24]: text=复查。3.右肺中叶、双肺下叶实性结节，建议, bbox=[150, 767, 590, 785]
2026-08-10 15:01:06,003 INFO     29 [qwen-vl-text] coord item[25]: text=随诊；右肺上叶钙化灶。4.贫血征象，请结合, bbox=[150, 787, 590, 805]
2026-08-10 15:01:06,003 INFO     29 [qwen-vl-text] coord item[26]: text=实验室检查；主动脉粥样硬化。5.胸椎退行性, bbox=[150, 807, 590, 825]
2026-08-10 15:01:06,003 INFO     29 [qwen-vl-text] coord item[27]: text=变。6.PICC管置入术后。（上述1-5条较前大, bbox=[150, 827, 583, 845]
2026-08-10 15:01:06,003 INFO     29 [qwen-vl-text] coord item[28]: text=致相仿）, bbox=[150, 848, 224, 865]
2026-08-10 15:01:06,003 INFO     29 [qwen-vl-text] page=7 — 29/29 coords, api_time=10.1s
2026-08-10 15:01:06,004 INFO     29 [qwen-vl-text] new_positions (29):
[[7, 195.25839599609375, 251.21659484863284, 119.54980346679687, 134.70400390625], [7, 89.29499816894531, 134.53779724121094, 143.9649041748047, 157.4353045654297], [7, 89.29499816894531, 233.35759521484377, 165.01240478515626, 180.16660522460938], [7, 89.29499816894531, 114.89289764404298, 218.89400634765624, 233.20630676269533], [7, 311.34189361572265, 355.9893927001953, 218.89400634765624, 233.20630676269533], [7, 89.29499816894531, 141.0860971069336, 254.2538073730469, 268.56610778808596], [7, 232.7622952270508, 357.17999267578125, 254.2538073730469, 268.56610778808596], [7, 89.29499816894531, 141.0860971069336, 309.819208984375, 324.1315093994141], [7, 89.29499816894531, 350.03639282226567, 334.23430969238285, 364.5427105712891], [7, 89.29499816894531, 354.20349273681643, 367.06841064453124, 382.22261108398436], [7, 89.29499816894531, 336.34449310302733, 384.74831115722657, 399.06061157226566], [7, 96.43859802246094, 353.0128927612305, 401.5863116455078, 416.7405120849609], [7, 89.29499816894531, 350.03639282226567, 418.4243121337891, 433.5785125732422], [7, 89.29499816894531, 323.24789337158205, 435.26231262207034, 450.41651306152346], [7, 89.29499816894531, 354.20349273681643, 452.1003131103516, 467.2545135498047], [7, 89.29499816894531, 350.03639282226567, 468.9383135986328, 484.09251403808594], [7, 89.29499816894531, 343.48809295654297, 485.77631408691406, 500.93051452636723], [7, 89.29499816894531, 350.03639282226567, 502.61431457519535, 517.7685150146484], [7, 89.29499816894531, 350.03639282226567, 519.4523150634766, 534.6065155029297], [7, 89.29499816894531, 350.03639282226567, 536.2903155517579, 551.444515991211], [7, 89.29499816894531, 187.51949615478517, 553.9702160644531, 568.2825164794922], [7, 89.29499816894531, 141.0860971069336, 589.3300170898438, 603.6423175048828], [7, 89.29499816894531, 350.03639282226567, 612.0613177490235, 627.2155181884766], [7, 89.29499816894531, 351.22699279785155, 628.8993182373047, 644.0535186767578], [7, 89.29499816894531, 351.22699279785155, 645.737318725586, 660.8915191650391], [7, 89.29499816894531, 351.22699279785155, 662.5753192138673, 677.7295196533204], [7, 89.29499816894531, 351.22699279785155, 679.4133197021484, 694.5675201416016], [7, 89.29499816894531, 347.0598928833008, 696.2513201904297, 711.4055206298829], [7, 89.29499816894531, 133.347197265625, 713.9312207031251, 728.243521118164]]
2026-08-10 15:01:06,004 INFO     29 [qwen-vl-text] ═══ DONE ═══ 29 positions, pages=1, time=14.3s
2026-08-10 15:01:06,004 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 15:01:06,013 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 15:01:06,014 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 15:01:06,014 INFO     29 [qwen-vl-text] positions(11): [[16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 15:01:06,014 INFO     29 [qwen-vl-text] page grouping: [16], lines per page: [11]
2026-08-10 15:01:06,092 INFO     29 [qwen-vl-text] page=16, rect=595x842, img=(1654x2339), dpi=200
2026-08-10 15:01:06,093 INFO     29 [qwen-vl-text] LLM extraction start, text_len=78
2026-08-10 15:01:06,093 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:01:06,093 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 528, \"bbox_end\": 538, \"encounter_dates\": [\"2026-02-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "报告详情\n检查\n常规心电图\n姓名\n男 63岁\n检查时间\n2026-02-05 11:17:16\n诊断意见\n1.窦性心律2.正常范围心电图\n报告文件\n预览 >",
    "role": "user"
  }
]
2026-08-10 15:01:06,635 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T15:01:06.634+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 64, "failed": 0, "current": {"7630dbd094ca11f1bd9827cf206dfa2d": {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 15:01:07,887 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:01:07,887 INFO     29 [qwen-vl-text] LLM output (len=316):
{
  "exam_date": "2026-02-05",
  "report_date": null,
  "exam_name": "常规心电图",
  "exam_category": "other",
  "body_part": null,
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": null,
  "findings": null,
  "conclusion": "1.窦性心律2.正常范围心电图",
  "physician": null,
  "reviewer": null
}
2026-08-10 15:01:07,888 INFO     29 [qwen-vl-text] coord API call start, page=16, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=122427, prompt_len=724
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共11行）
["报告详情", "检查", "常规心电图", "姓名", "男 63岁", "检查时间", "2026-02-05 11:17:16", "诊断意见", "1.窦性心律2.正常范围心电图", "报告文件", "预览 >"]

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
2026-08-10 15:01:11,899 INFO     29 [qwen-vl-text] coord API raw response (len=565):
[
	{"text": "报告详情", "bbox": [317, 109, 390, 123]},
	{"text": "检查", "bbox": [180, 155, 240, 169]},
	{"text": "常规心电图", "bbox": [180, 175, 272, 189]},
	{"text": "姓名", "bbox": [180, 225, 214, 239]},
	{"text": "男 63岁", "bbox": [467, 225, 525, 239]},
	{"text": "检查时间", "bbox": [180, 257, 248, 270]},
	{"text": "2026-02-05 11:17:16", "bbox": [371, 257, 526, 270]},
	{"text": "诊断意见", "bbox": [180, 308, 248, 322]},
	{"text": "1.窦性心律2.正常范围心电图", "bbox": [316, 308, 525, 322]},
	{"text": "报告文件", "bbox": [180, 360, 248, 373]},
	{"text": "预览 >", "bbox": [470, 360, 522, 373]}
]
2026-08-10 15:01:11,900 INFO     29 [qwen-vl-text] coord API: raw_items=11, valid_items=11, elapsed=4.0s
2026-08-10 15:01:11,900 INFO     29 [qwen-vl-text] coord item[0]: text=报告详情, bbox=[317, 109, 390, 123]
2026-08-10 15:01:11,900 INFO     29 [qwen-vl-text] coord item[1]: text=检查, bbox=[180, 155, 240, 169]
2026-08-10 15:01:11,900 INFO     29 [qwen-vl-text] coord item[2]: text=常规心电图, bbox=[180, 175, 272, 189]
2026-08-10 15:01:11,900 INFO     29 [qwen-vl-text] coord item[3]: text=姓名, bbox=[180, 225, 214, 239]
2026-08-10 15:01:11,900 INFO     29 [qwen-vl-text] coord item[4]: text=男 63岁, bbox=[467, 225, 525, 239]
2026-08-10 15:01:11,900 INFO     29 [qwen-vl-text] coord item[5]: text=检查时间, bbox=[180, 257, 248, 270]
2026-08-10 15:01:11,900 INFO     29 [qwen-vl-text] coord item[6]: text=2026-02-05 11:17:16, bbox=[371, 257, 526, 270]
2026-08-10 15:01:11,900 INFO     29 [qwen-vl-text] coord item[7]: text=诊断意见, bbox=[180, 308, 248, 322]
2026-08-10 15:01:11,900 INFO     29 [qwen-vl-text] coord item[8]: text=1.窦性心律2.正常范围心电图, bbox=[316, 308, 525, 322]
2026-08-10 15:01:11,901 INFO     29 [qwen-vl-text] coord item[9]: text=报告文件, bbox=[180, 360, 248, 373]
2026-08-10 15:01:11,901 INFO     29 [qwen-vl-text] coord item[10]: text=预览 >, bbox=[470, 360, 522, 373]
2026-08-10 15:01:11,901 INFO     29 [qwen-vl-text] page=16 — 11/11 coords, api_time=4.0s
2026-08-10 15:01:11,901 INFO     29 [qwen-vl-text] new_positions (11):
[[16, 188.7100961303711, 232.16699523925783, 91.76710266113281, 103.5537030029297], [16, 107.15399780273438, 142.87199707031252, 130.4945037841797, 142.28110412597655], [16, 107.15399780273438, 161.9215966796875, 147.33250427246094, 159.11910461425782], [16, 107.15399780273438, 127.39419738769531, 189.42750549316406, 201.21410583496095], [16, 278.0050942993164, 312.5324935913086, 189.42750549316406, 201.21410583496095], [16, 107.15399780273438, 147.63439697265625, 216.36830627441407, 227.3130065917969], [16, 220.85629547119143, 313.1277935791016, 216.36830627441407, 227.3130065917969], [16, 107.15399780273438, 147.63439697265625, 259.3052075195313, 271.0918078613281], [16, 188.11479614257814, 312.5324935913086, 259.3052075195313, 271.0918078613281], [16, 107.15399780273438, 147.63439697265625, 303.0840087890625, 314.0287091064453], [16, 279.79099426269534, 310.7465936279297, 303.0840087890625, 314.0287091064453]]
2026-08-10 15:01:11,901 INFO     29 [qwen-vl-text] ═══ DONE ═══ 11 positions, pages=1, time=5.9s
2026-08-10 15:01:11,916 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 15:01:11,917 INFO     29 [Trace] task=7630dbd0 | doc=YXHU  62  男  直肠癌肺转移  贵州(2).pdf | Extractor:ExaminationReport | outputs={"chunks": "8 items, types={'ExaminationReport': 8}", "html": "", "json": "2311 items", "markdown": "", "text": "", "name": "YXHU  62  男  直肠癌肺转移  贵州(2).pdf", "output_format": "chunks", "chunks_Examination": "8 items, types={'ExaminationReport': 8}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_LabExam": "6 items, types={'LabReport': 6}", "route_summary": "{\"chunks_Examination\": 8, \"chunks_Discharge\": 2, \"chunks_LabExam\": 6}"}
2026-08-10 15:01:11,917 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 15:01:11,926 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:01:11,926 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 15:01:12,943 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 15:01:12,959 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 15:01:12,960 INFO     29 [Trace] task=7630dbd0 | doc=YXHU  62  男  直肠癌肺转移  贵州(2).pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "2311 items", "markdown": "", "text": "", "name": "YXHU  62  男  直肠癌肺转移  贵州(2).pdf", "output_format": "chunks", "chunks_Examination": "8 items, types={'ExaminationReport': 8}", "chunks_Discharge": "2 items, types={'DischargeRecord': 2}", "chunks_LabExam": "6 items, types={'LabReport': 6}", "route_summary": "{\"chunks_Examination\": 8, \"chunks_Discharge\": 2, \"chunks_LabExam\": 6}"}
2026-08-10 15:01:12,960 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 15:01:12,963 INFO     29 [ChunkMerger] Merged 16 chunks from 9 sources: {'Extractor:LabExam': 6, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 2, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 8, 'Extractor:Progress': 1} (filtered 6 noise chunks)
2026-08-10 15:01:12,976 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 15:01:12,977 INFO     29 [Trace] task=7630dbd0 | doc=YXHU  62  男  直肠癌肺转移  贵州(2).pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "16 items, types={'LabReport': 6, 'DischargeRecord': 2, 'ExaminationReport': 8}", "name": "YXHU  62  男  直肠癌肺转移  贵州(2).pdf"}
2026-08-10 15:01:12,977 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 15:01:13,233 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786373273597, 'update_date': datetime.datetime(2026, 8, 10, 14, 47, 53), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1119126, 'status': '1'}
2026-08-10 15:01:13,452 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   白细胞计数  None  9.23  10^9/L  3.90-9.50  False    中性粒细胞百分率  None  70.50  %  40.00-75.00  False    淋巴细胞百分率  None  18.60  %  20.00-50.00  True    单核细胞百分率  None  6.90  %  3.00-10.00  False    嗜酸性粒细胞百分率  None  3.30  %  0.40-8.00  False    嗜碱性粒细胞百分率  None  0.70  %  0.02-0.52  True    大的未染色细胞计数  None  0.03  10^9/L  0.00-0.40  False    中性粒细胞绝对值  None  6.51  10^9/L  1.80-6.30  True    淋巴细胞绝对值  None  1.72  10^9/L  1.10-3.20  False    单核细胞绝对值  None  0.64  10^9/L  0.10-0.60  True    嗜酸性粒细胞绝对值  None  0.30  10^9/L  0.02-0.52  False    嗜碱性粒细胞绝对值  None  0.06  10^9/L  0.02-0.06  False    大的未染色细胞百分率  None  0.30  %  0.00-4.00  False    红细胞计数  None  4.34  10^12/L  4.30-5.80  False    血红蛋白  None  125.00  g/L  130.00-175.00  True    红细胞比积  None  38.60  %  40.00-50.00  True    红细胞平均体积  None  88.90  fl  82.00-100.00  False    红细胞平均血红蛋白量  None  28.70  pg  27.00-34.00  False    红细胞平均血红蛋白浓度  None  324.00  g/L  316.00-354.00  False    红细胞体积分布宽度变异系数  None  14.30  %  12.00-16.00  False    红细胞体积分布宽度标准差  None  44.90  fl  35.00-56.00  False    血小板计数  None  458.00  10^9/L  125.00-350.00  True    血小板平均体积  None  7.10  fl  8.30-17.40  True    C反应蛋白  None  18.29  mg/L  0.00-10.00  True   
---
   谷丙转氨酶  None  15.40  U/L  9.00-60.00  False    谷草转氨酶  None  18.50  U/L  15.00-45.00  False    谷草/谷丙  None  1.20  None  0.80-1.40  False    总胆红素  None  11.90  μmol/L  3.40-17.10  False    直接胆红素  None  5.00  μmol/L  0.00-4.00  True    间接胆红素  None  6.90  μmol/L  3.00-17.00  False    总蛋白  None  69.800  g/L  65.000-80.000  False    白蛋白  None  40.50  g/L  40.00-55.00  False    碱性磷酸酶  None  87.00  U/L  45.00-125.00  False    γ-谷氨酰基转移酶  None  32.00  U/L  10.00-60.00  False    总胆汁酸  None  6.47  μmol/L  0.00-9.67  False    尿素  None  5.40  mmol/L  3.00-9.20  False    肌酐  None  96.00  μmol/L  59.00-104.00  False    尿素/肌酐  None  0.06  None  0.03-0.20  False    尿酸  None  248.00  μmol/L  208.00-428.00  False    葡萄糖  None  7.28  mmol/L  3.90-6.10  True    钾  None  3.92  mmol/L  3.50-5.50  False    钠  None  141.60  mmol/L  135.00-145.00  False    氯  None  102.90  mmol/L  96.00-108.00  False    钙  None  2.22  mmol/L  2.10-2.60  False    镁  None  0.85  mmol/L  0.73-1.35  False    磷  None  0.98  mmol/L  0.78-1.65  False    前白蛋白  None  110.00  mg/L  200.00-400.00  True    胆碱酯酶  None  5602.00  U/L  4600.00-11500.00  False    白蛋白/球蛋白  None  1.38  None  1.20-2.40  False    球蛋白  None  29.30  g/L  20.00-40.00  False   
---
   凝血酶原时间检测  None  13.3  s  9.8-14.3  False    活动度  None  86.4  %  70.0-150.0  False    国际标准化比值  None  1.2  None  0.5-1.5  False    活化部分凝血活酶时间检测  None  30.0  s  20.0-36.9  False    纤维蛋白原检测  None  9.1  g/L  2.0-4.0  True    凝血酶时间检测  None  16.8  s  14.4-23.4  False    D-D二聚体检测  None  0.6  ug/ml  0.0-0.6  False    纤维蛋白（原）降解产物检测  None  4.5  ug/ml  0.0-5.0  False   
---
   糖类抗原125  CA125  6.46  U/ml  0.00-24.00  False    糖类抗原199  CA199  8.34  U/ml  0.00-30.00  False    糖类抗原153  CA153  11.70  U/ml  0.00-24.00  False    糖类抗原724  CA724  8.43  U/ml  0.00-6.90  True    糖类抗原242  CA242  8.77  U/ml  0.00-20.00  False    总前列腺特异性抗原  TPSA  1.12  ng/ml  0.00-4.00  False    FPSA/TPSA  FPSA/TPSA  16.96  %  25.00-100.00  True    神经元特异性烯醇化酶  NSE  12.00  ng/ml  0.00-17.00  False    细胞角蛋白19片段  CYFRA21-1  4.07  ng/ml  0.00-3.30  True    鳞状细胞癌抗原  SCC  1.66  ng/ml  0.50-3.00  False    甲胎蛋白  AFP  4.18  ng/mL  0.00-7.00  False    癌胚抗原  CEA  5.27  ng/mL  0.00-5.00  True    铁蛋白  Ferritin  47.50  ng/ml  30.00-400.00  False   
---
   肌红蛋白  None  28.530  ng/ml  28.000-72.000  False    高敏肌钙蛋白T  None  0.012  ng/ml  0.000-0.014  False   
---
   体细胞突变  None  2  None  None  True    拷贝数变异  None  1  None  None  True    融合变异  None  未检出  None  None  False    微卫星不稳定状态（MSI）  MSI  微卫星稳定（MSS）  None  None  False    错配修复基因胚系突变（MMR）  MMR  未检出  None  None  False    KRAS 2号外显子  KRAS  错义突变 c.34G>A p.G12S 丰度=41.62%  None  None  True    MYC  MYC  拷贝数扩增 CN=3.42  None  None  True    KRAS  None  c.34G>A(p.G12S)  None  None  True    BRAF  None  未检出  None  None  False    NRAS  None  未检出  None  None  False    APC  None  c.4257_4263del(p.S1419fs)  None  None  True    微卫星不稳定性（MSI）  MSI  微卫星稳定（MSS）  None  None  False    EPCAM  None  未检出  None  None  False    MLH1  None  未检出  None  None  False    MSH2  None  未检出  None  None  False    MSH6  None  未检出  None  None  False    PMS2  None  未检出  None  None  False    MYC  None  CN=3.42  None  None  True    BRAF  None  未检出  None  None  False    EGFR  None  未检出  None  None  False    ERBB2  None  未检出  None  None  False    FGFR1  None  未检出  None  None  False    FGFR2  None  未检出  None  None  False    FGFR3  None  未检出  None  None  False    KRAS  None  未检出  None  None  False    MDM2  None  未检出  None  None  False    NTRK1  None  未检出  None  None  False    PIK3CA  None  未检出  None  None  False    RET  None  未检出  None  None  False    NTRK3  None  未检出  None  None  False    NTRK2  None  未检出  None  None  False    NTRK1  None  未检出  None  None  False    紫杉醇类  TP53 rs1042522  CG  None  None  False    伊立替康  UGT1A1 rs8175347  (TA)6/(TA)7  None  None  True    伊立替康  UGT1A1 rs4148323  AG  None  None  True    5-氟尿嘧啶  DPYD rs55886062  AA  None  None  False    5-氟尿嘧啶  DPYD rs67376798  TT  None  None  False    5-氟尿嘧啶  DPYD rs3918290  CC  None  None  False    卡培他滨  DPYD rs67376798  TT  None  None  False    卡培他滨  DPYD rs3918290  CC  None  None  False    甲氨蝶呤  MTHFR rs1801133  AG  None  None  True    样本量  None  合格  None  >30 ng  False    预文库  None  合格  None  >500 ng  False    靶向捕获  None  合格  None  >10 ng  False    测序质量  None  0.953  None  >0.8  False    测序深度  None  795.20  X  组织样本≥500X; ctDNA≥5000X  False    KRAS 2号外显子 c.34G>A p.G12S  KRAS  41.62%  %  None  True    APC 16号外显子 c.4257_4263del p.S1419fs  APC  40.08%  %  None  True    MYC 拷贝数  MYC  3.42  CN  None  True   
---
出院记录
姓名：
科室：
住院号：
姓名：
职业：自由职业
性别：男
入院日期：2026-2-5 10:14
年龄：63岁
出院日期：2026-2-26 10:25
民族：汉族
住院天数：21天
籍贯：
科 室：
入院情况：
患者男，63岁，因“诊断直肠癌肺转移7+月”入院；既往史：4+年前因“大便不成形伴血
便”就诊于外院，考虑为“直肠癌”，未明确诊断，自行服用中药治疗；10+月前因“阴囊脓肿”于
我院局麻下行“阴囊下部脓肿切开引流术”，病理结果回示：“阴囊内容物”检材大部分为变性坏
死组织，区域见大量中性粒细胞浸润。予换药、抗感染等对症治疗后好转。专科情况：全身皮肤粘
膜无黄染、出血点及瘀斑，全身浅表淋巴结未扪及肿大，胸廓对称无畸形，肋间隙无明显增宽及凹
陷，胸骨无压痛，双肺叩诊呈清音，双肺呼吸音粗，双肺可闻及散在湿啰音。腹平软，全腹未见腹
部静脉曲张、蜘蛛痣，未见胃肠型蠕动波。全腹无压痛、反跳痛及肌紧张，肝脾肋下未扪及，莫菲
氏征阴性，移动性浊音阴性，双肾区无叩击痛，肠鸣音约4次/分，阴囊及肛周皮肤正常，未见红
肿、破溃，肛周6点钟方向可扪及一约2*3cm大小包块，质韧，挤压时无明显脓液，肛门括约肌张力
正常，于直肠距肛门约7cm处可扪及环状肿物，质地硬，表面凹凸不平，活动度差，退出指套可见血
染。（患者取左侧卧位）辅助检查：病理（病理号：2502456）：“左肺占位”恶性肿瘤，符合腺
癌，结合免疫组化结果及临床病史考虑肠道来源。ALK（-）、CD56（-）、CDX-2（+）、CK20
(+）、CK5/6（-）、CK7（局灶弱+）、Ki-67（30%+）、Napsin-A（-）、P40(-)、P53（突变
型）、P63(-)、SATB2(+)、Syn（-）、TTF-1（+）、CK(AE1/AE3)（+）、Vimentin（-）、Villin
(+）。基因检测：1.KRAS基因突变；2.MYC基因扩增；3.APC基因突变。胸部CT（本院 2026-01-
08）：1.肺气肿伴双肺多发肺大疱；2.左肺上叶舌段结节及肿块，具恶性征象，较前增大；3.左肺上
叶及双肺下叶实性结节，右肺中叶实性结节较前未见确切显示，右肺上叶钙化灶；4.新增双肺下叶
坠积效应；5.新增气管黏液栓；6.贫血征象，主动脉粥样硬化；7.胸椎退行性变；8.PICC管较前未
见确切显示。全腹+盆腔增强CT（本院 2026-01-08）：1.直肠下段病变，Ca可能，较前进展，周围
多发淋巴结，较前稍增多、增大；2.肝内多发囊肿；3.双肾周多发渗出，较前已吸收；4.双肾多发
囊肿；5.考虑升结肠、盲肠炎伴周围炎性渗出，较前已吸收；6.前列腺钙化灶；7.右侧会阴部积气
较前已吸收；8.腹主动脉及双侧髂总动脉粥样硬化。9.腰椎退行性变。
入院诊断：1.直肠腺癌 ycT4bN2M1 IV期（肺转移）；2.肺气肿伴双肺肺大疱；3.混合
痔；4.肝囊肿；5.双肺结节；6.双肺细菌性肺炎。
第1页
出院记录
姓名：
科室：
住院号：
诊疗经过：患者入院后积极完善相关辅助检查，血常规：中性粒细胞绝对值10.57*10^
9/L，血红蛋白128.00g/L，红细胞比积38.80%，白细胞计数12.28*10^9/L，C反应蛋
白101.75mg/L。DIC全套：纤维蛋白原检测9.1g/L。大便潜血：阳性。肿瘤标记物：
癌胚抗原6.84ng/mL，糖类抗原72427.95U/mL。血生化、心肌标记物及心肌酶谱均未
见明显异常。结合患者病史、体征及相关辅助检查，考虑患者直肠癌肺转移较前进展，
因患者且合并远处转移，无法行根治性手术切除原发病灶及转移病灶，故建议患者行
“支气管、肋间、胸廓内外动脉+肠道动脉灌注化疗栓塞术”，提高患者生存周期并改
善患者生质量，但患者因自身原因拒绝行介入手术治疗，并要求继续使用贝伐珠单抗靶
向治疗及对症止痛。但因患者目前疗效评估为PD，结合患者原免疫组化，考虑化疗药物
可能对肿瘤细胞形态及抗原表达产生影响，从而发生免疫组化结果改变，故建议患者再
次行肠镜检查取病理活检明确免疫组化情况，必要时再次行基因检测指导抗肿瘤药物选
择。患者及家属拒绝行病理活检，要求暂使用贝伐珠单抗靶向治疗，向患者告知可能因
免疫组化改变发生耐药，但患者家属仍坚持要求继续使用贝伐珠单抗。后予患者完善盆
腔MRI平扫，盆腔MRI示：1.直肠下段Ca，累及浆膜面，盆腔多发肿大淋巴结；2.盆腔左
份脓肿（大小约106×38×29mm）可能；3.骨盆骨质疏松征象。阅片可见患者盆腔左份
及左侧会阴区见不规则团片状密度增高影，部分呈囊状改变，因病灶范围大与周围临近
器官组织分界欠清，压迫症状明显，故建议患者行脓肿穿刺置管引流术，缓解压迫症
状。且阅片可见患者直肠肿瘤较前增大已明显侵犯浆膜面，患者目前已出血肛门坠胀及
排便困难等症状，考虑为肿瘤进展后体积增大，阻塞肠腔所致，故建议患者可行直肠球
囊扩张、支架置入或姑息性造瘘术以改善排便困难症状，避免因肠管狭窄出现肠梗阻危
及生命，向患者及家属交代患者目前病情及后续治疗后，患者及家属表示理解，同意行
脓肿穿刺引流，但拒绝行直肠球囊扩张、支架置入及姑息性造瘘术，故排除手术禁忌后
于2026年2月8日在局麻下行“经CT引导下盆腔脓肿穿刺置管引流术”，手术过程顺利，
术后继予患者抗感染、抑酸护胃等对症支持治疗，后患者肛周皮肤出现破溃流脓，考虑
为直肠肿瘤进展后肿瘤直接浸润肠壁全层及穿透至肛周组织，导致局部组织坏死流出，
出现肛周皮肤破溃伴流脓，予患者盐水冲洗创面及加强换药，保持引流通畅，促进创面
愈合，经治疗患者创面渗出较前已明显减少，但为避免窦道形成，仍建议患者尽快行外
科手术治疗，患者及家属表示理解，并要求转院行外科手术治疗，请示上级医师后同意
第2页
出院记录
姓名：
科室：
住院号：
予患者签署自请出院协议后今日出院。
手术：经CT引导下盐腔脓肿穿刺置管引流术 2026-02-08
出院情况：患者诉创面渗出较前已明显减少，无恶心、呕吐，无咳嗽、咳痰，无胸痛。
胸闷、气促、呼吸困难，无腹胀、腹痛，无畏寒、发热等不适，精神、饮食、睡眠尚
可，小便黄清，大便同前。查体：全身浅表淋巴结未扪及肿大，胸廓对称无畸形，肋间
隙无明显增宽及凹陷，胸骨无压痛，双肺叩诊呈清音，双肺呼吸音粗，双肺可闻及散在
湿啰音。腹平软，全腹未见腹部静脉曲张、蜘蛛痣，未见胃肠型蠕动波。全腹无压痛、
反跳痛及肌紧张，肝脾肋下未扪及，莫菲氏征阴性，移动性浊音阴性，双肾区无叩击
痛，肠鸣音约4次/分，阴囊皮肤正常，未见红肿、破溃，肛周6点钟方向可见一大小约2
×1cm不规则皮肤缺损，创面基底呈暗红色可见少量白色脓苔附着，可见少量灰白色恶
臭味脓性分泌物流出。肛门括约肌张力正常，于直肠距肛门约7cm处可扪及环状肿物，
质地硬，表面凹凸不平，活动度差，退出指套可见血染。左侧臀部引流管引流通畅，可
见暗灰色脓性分泌物引出，量约10ml。（患者取左侧卧位）
出院诊断：1.直肠腺癌 ycT4bN2M1 IV期（肺转移）；2.肺气肿伴双肺肺大疱；3.混合
痔；4.肝囊肿；5.双肺结节；6.双肺细菌性肺炎；7.轻度贫血；8.盆腔脓肿；9.肛周脓
肿。
出院医嘱：院外继续治疗。
康复指导：嘱患者适当活动，禁忌久卧、久坐，避免深静脉血栓形成
医生坐诊信息
医生签名：
2026-2-26
第3页
---
出院记录
姓名：
科室：
住院号：
姓名：
职业：自由职业
性别：男
入院日期：2025-7-8 09:23
年龄：62岁
出院日期：2025-7-14 10:00
民族：汉族
住院天数：6天
籍贯：
科 室：
入院情况：
患者 男，62岁，因“发现左肺占位3+月，诊断肠道肿瘤肺转移2+月”入院；患者3+月前因
胸闷就诊于我院，行胸部CT提示：左肺上叶舌段周围型肺癌可能性大。后排除手术禁忌后于2025年4
月16日行“肺穿刺活检”，病理结果提示：“左肺占位”恶性肿瘤，符合腺癌，结合免疫组化结果及
临床病史考虑肠道来源。P53（突变型）、Syn（-）、TTF-1（+）、P63(-)、CK(AE1/AE3)
(+)、Vimentin（-）、Villin（+）、CK7（局灶弱+）、CD56（-）、ALK（-）、Napsin-
A（-）、P40(-)、CDX-2（+）、CK20（+）、Ki-67（30%+）、SATB2(+)、PCK5/6（-）。基因检测：
1.KRAS基因突变；2.MYC基因扩增；3.APC基因突变。因患者为肠道肿瘤晚期且合并肺转移，可予患者
行姑息性治疗，提高患者生存期，故排除化疗禁忌后于2025年5月12日至2025年6月22日完成1-3周期
“FOLFOX+贝伐珠单抗”（奥沙利铂150mg+亚叶酸钙600mg+氟尿嘧啶4500mg+贝伐珠单抗400mg）
联合治疗，现患者为按计划行下一周期治疗入院，门诊遂以“肠道肿瘤肺转移”收入我科。既往史：
3+年前因“大便不成形伴血便”就诊于外院，考虑为“直肠癌”，未明确诊断，自行服用中药治疗；
2+月前因“阴囊脓肿”于我院局麻下行“阴囊下部脓肿切开引流术”，病理结果回示：“阴囊内容
物”检材大部分为变性坏死组织，区域见大量中性粒细胞浸润。予换药、抗感染等对症治疗后好转。
专科情况：腹平软，全腹未见腹部静脉曲张、蜘蛛痣，未见胃肠型蠕动波。全腹无压痛、反跳痛及肌
紧张，肝脾肋下未扪及，莫菲氏征阴性，移动性浊音阴性，双肾区无叩击痛，肠鸣音约4次/分，阴囊
及肛周皮肤正常，未见红肿、破溃，肛周可扪及一约1*1cm大小包块，质韧，挤压时无明显脓液。辅
助检查：病理（病理号：2502456）：“左肺占位”恶性肿瘤，符合腺癌，结合免疫组化结果及临床
病史考虑肠道来源。CD56（-）、CDX-2（+）、CK7（局灶弱+）、ALK（-）、Ki-67（30%
+）、P63(-)、SATB2(+)、CK20（+）、CK5/6（-）、Napsin-A（-）、P40(-)、P53（突变
型）、Syn（-）、TTF-1（+）、CK(AE1/AE3)（+）、Vimentin（-）、Villin（+）。基因检测：
1.KRAS基因突变；2.MYC基因扩增；3.APC基因突变。
入院诊断：1.姑息性化疗；2.肠道肿瘤肺转移（T4bNxM1 IVa期）；3.肺气肿伴双肺肺大
疱；4.混合痔；5.肝囊肿；6.双肺结节。
诊疗经过：患者入院后积极完善相关辅助检查，血常规：中性粒细胞绝对值1.05*10
第1页
出院记录
姓名：
科室：
住院号
9/L↓，血红蛋白123.00g/L↓，白细胞计数3.16*10^9/L↓。肝肾功、电解质、心肌标
记物及心肌酶谱均未见明显异常。入院时患者血常规提示白细胞稍低，考虑为化疗后骨
髓抑制，予患者人粒细胞刺激因子对症治疗后复查血常规未见明显异常。因患者为肠道
肿瘤晚期且合并肺转移，治疗方式以全身治疗为主的姑息治疗，以延长生命，改善生活
质量为目的，目前患者已于我科完成3个周期“FOLFOX+贝伐珠单抗”方案治疗，查体可
见阴囊处皮肤缺损已愈合，肛周肿块较前缩小，行局部疗效评估为PR，后续可继续该方
案治疗，故排除化疗禁忌后于2025年7月9日至2025年7月13日行第4周期“FOLFOX+贝伐珠
单抗”（奥沙利铂150mg+亚叶酸钙600mg+氟尿嘧啶4500mg+贝伐珠单抗400mg）方案
治疗，患者化疗期间出现消化道反应，予止吐、抑酸等对症支持治疗后，消化道症状明
显好转，复查血常规未见明显骨髓抑制，目前我科已无特殊治疗，请示上级医师后同意
予患者今日出院。
手术：无
出院情况：患者无恶心、呕吐，未诉心慌、胸闷、气促、呼吸困难，无畏寒、发热，无
腹胀、腹泻等特殊不适；精神、睡眠、饮食尚可，二便如常。查体：生命征平稳，一般
情况可。心肺腹查体无特殊，专科查体同前。
出院诊断：1.姑息性化疗；2.肠道肿瘤肺转移（T4bNxM1 IVa期）；3.肺气肿伴双肺肺
大疱；4.混合痔；5.肝囊肿；6.双肺结节；7.化疗后骨髓抑制。
出院医嘱：1.注意休息，多饮水，避免剧烈活动，注意加强营养；2.动态监测血常规
（每周查血常规2次），监测肝功能每周1次，若有异常，及时就诊；3.间隔3周返院按计
划行下一周期化疗；4.若出现畏寒、发热、乏力、心慌、胸闷等不适立即返院就诊；5.
耳鼻喉科门诊随诊；6.不适我科随诊。
康复指导：嘱患者适当活动，禁忌久卧
医生签名：
2025-7-14
第2页
---
病理诊断报告
病理号:
名:
性 别: 男
年龄: 62岁
收到日期: 2025-08-1
医院:
送检科室:
送检医生:
号:
床 号:
门诊号:
临床诊断: 直肠、肛管新生物并狭窄
肉眼所见:
直肠、肛管新生物: 灰白色组织多粒, 约0.1-0.2cm, 全。
镜下所见:
病理诊断:
(直肠、肛管新生物) 恶性肿瘤, 建议行免疫组化进一步协助检查。
报告医
审核医师
报告日期: 2025-08-14 11:05:
须经诊断医师签字方能生效。
仅反映本次送检样本情况, 若有疑问, 请及时与病理科联系。
---
报告详情
检查
盆腔CT*
姓名
男63岁
检查时间
2026-02-23 11:37:59
影像所见
对比2026-02-15盆腔CT平扫：阑尾未见增
粗。直肠下段管壁增厚，浆膜面稍毛糙，直肠
周围可见肿大淋巴结，较大者大小约
8mm×5mm。盆腔左份及左侧会阴区见条片状
低密度影，范围较前缩小，边界不清，其内可
见引流管影。腹腔未见明显积液及游离气体。
腹腔及腹膜后未见明显增大淋巴结。腹主动脉
及双侧髂总动脉壁见斑片状高密度影。腰椎椎
体边缘变尖。
诊断意见
1.直肠下段Ca，累及浆膜面，盆腔多发肿大淋
巴结，请结合临床及MRI检查。2.盆腔左份及
左侧会阴区脓肿引流术后，脓肿较前吸收。3.
前列腺钙化灶。4.腹主动脉及双侧髂总动脉粥
样硬化。5.腰椎退行性变。
---
报告详情
检查
盆腔CT平扫+增强*
姓名
男63岁
检查时间
2026-02-08 14:55:00
影像所见
对比2026-01-09腹部增强：阑尾未见增粗。直
肠下段管壁增厚，增强扫描不均匀强化，浆膜
面稍毛糙，周围可见淋巴结显示，较大者大小
约8mm×5mm。盆腔左份及左侧会阴区见不规
则团片状密度增高影，局部呈囊性改变，病灶
边界欠清晰，较大截面大小约
70mm×34mm×95mm（前后径×左右径×上下
径），其内见小气泡影，周围脂肪间隙模糊，
增强病灶边缘轻度强化，病灶与左侧前列腺、
精囊腺分界欠清晰，前列腺可见结节状高密度
影。腹腔未见明显积液及游离气体。腹腔及腹
膜后未见明显增大淋巴结。腹主动脉及双侧髂
总动脉壁见斑片状高密度影。腰椎椎体边缘变
尖。
诊断意见
1.直肠下段Ca，累及浆膜面，盆腔多发淋巴
结，请结合临床及MRI检查。2.考虑盆腔左份
及左侧会阴区脓肿形成，请结合临床并复查。
3.前列腺钙化灶。4.腹主动脉及双侧髂总动脉
粥样硬化。5.腰椎退行性变。
---
报告详情
姓名
男63岁
检查时间
2026-02-05 17:02:53
影像所见
对比2026-01-09胸部CT平扫：双肺透亮度增
高，可见多发囊状透亮影；左肺上叶舌段可见
两处肿块影，CT值约37-53Hu，分叶状，边界
清晰，较前稍扩大，较大者大小约
45mm×38mm×47mm（上下径×左右径×前后
径），密度不均，其内见结节状高密度影；左
肺上叶及双肺下叶可见实性结节，较大者位于
右肺下叶外基底段（IM216），大小约
11mm×9mm，略呈分叶状；右肺上叶可见结
节状高密度灶。气管内斑片状密度增高影此次
未见显示。双肺下叶近胸膜处见絮状密度增高
影，肺门影不大。纵隔无明显偏移，其内淋巴
结不大。心脏大小、形态未见明显异常，心腔
密度减低，主动脉壁见斑片状高密度影，双侧
胸腔未见积液。肋骨骨质结构未见异常。胸椎
椎体边缘变尖。
诊断意见
1.肺气肿伴双肺多发肺大疱，请结合肺功能检
查。2.左肺上叶舌段结节及肿块，具恶性征
象。3.左肺上叶及双肺下叶实性结节，建议随
诊；右肺上叶钙化灶。4.双肺下叶坠积效应，
建议复查。5.气管黏液栓较前未见确切显示。
6.贫血征象，请结合实验室检查；主动脉粥样
硬化。7.胸椎退行性变。（第1-4、6、7条较前
大致相仿）
---
报告详情
姓名
男 63岁
检查时间
2026-01-09 11:07:00
影像所见
对比2025-04-14上腹部CT平扫+增强及对比
2025-04-02下腹部CT平扫+增强：肝脏形
态、大小未见明显异常；肝内见多枚类圆形低
密度无强化灶，边界清晰，较大者位于S3，直
径约13mm；肝内胆管无明显扩张。肝门区结
构清晰。胆囊不大，壁不厚，腔内未见异常密
度影。胃、肠管未充盈。胰腺、脾脏及双侧肾
上腺形态、大小及密度未见明显异常双肾实质
大小、形态未见异常，双肾可见囊状低密度无
强化灶，较大者位于左肾，直径约9mm；双侧
肾盂、肾盏未见扩张。阑尾未见增粗。直肠下
段管壁增厚，增强扫描不均匀强化，浆膜面稍
毛糙，周围可见多发淋巴结显示，较大者大小
约8mm×5mm。前列腺可见结节状高密度影。
腹腔未见明显积液及游离气体。腹腔及腹膜后
未见明显增大淋巴结。腹主动脉及双侧髂总动
脉壁见斑片状高密度影。腰椎椎体边缘变尖。
诊断意见
1.直肠下段病变，Ca可能，较前进展，周围多
发淋巴结，较前稍增多、增大。2.肝内多发囊
肿。3.双肾周多发渗出，较前已吸收，请结合
临床。4.双肾多发囊肿。5.考虑升结肠、盲肠
炎伴周围炎性渗出，较前已吸收。6.前列腺钙
化灶。7.右侧会阴部积气较前已吸收，请结合
临床。8.腹主动脉及双侧髂总动脉粥样硬化。
9.腰椎退行性变。
---
报告详情
姓名
男63岁
检查时间
2026-01-09 09:32:00
影像所见
对比2025-08-11胸部CT平扫：双肺透亮度增
高，可见多发囊状透亮影；左肺上叶舌段可见
两处肿块影，CT值约22-61Hu，分叶状，边界
清晰，较前稍扩大，较大者大小约
45mm×36mm×42mm（上下径×左右径×前后
径），密度不均，其内见结节状高密度影；左
肺上叶及双肺下叶可见实性结节，较大者位于
右肺下叶，直径约7mm；右肺上叶可见结节状
高密度灶。新增气管内斑片状密度增高影。双
肺下叶近胸膜处见絮状密度增高影，肺门影不
大。纵隔无明显偏移，其内淋巴结不大。心脏
大小、形态未见明显异常，心腔密度减低，主
动脉壁见斑片状高密度影，上腔静脉内导管影
此次未见显示。双侧胸腔未见积液。肋骨骨质
结构未见异常。胸椎椎体边缘变尖。
诊断意见
1.肺气肿伴双肺多发肺大疱，请结合肺功能检
查。2.左肺上叶舌段结节及肿块，具恶性征
象，较前增大。3.左肺上叶及双肺下叶实性结
节，右肺中叶实性结节较前未见确切显示，建
议随诊；右肺上叶钙化灶。4.新增双肺下叶坠
积效应，建议复查。5.新增气管黏液栓。6.贫
血征象，请结合实验室检查；主动脉粥样硬
化。7.胸椎退行性变。8.PICC管较前未见确切
显示。
---
报告详情
检查
胸部CT平扫+三维重建
姓名
男 63岁
检查时间
2025-06-21 17:57:05
影像所见
对比2025-05-26胸部CT平扫：双肺透亮度增高，可见多发囊状透亮影；左肺上叶舌段可见
两处肿块影，CT值约33-57Hu，分叶状，边界
清晰，较大者大小约47mm×35mm×43mm
（上下径×左右径×前后径）；左肺下叶后基底
段、右肺中叶内侧段、右肺下叶外基底段可见
实性结节，较大者位于右肺下叶，直径约
6mm；右肺上叶可见结节状高密度灶。气管内
斑片状密度增高影未见显示。肺门影不大。纵
隔无明显偏移，其内淋巴结不大。心脏大小、
形态未见明显异常，心腔密度减低，主动脉壁
见斑片状高密度影，上腔静脉内见导管影。双
侧胸腔未见积液。肋骨骨质结构未见异常。胸
椎椎体边缘变尖。
诊断意见
1.肺气肿伴双肺多发肺大疱，请结合肺功能检
查。2.左肺上叶舌段肿块，具恶性征象，建议
复查。3.右肺中叶、双肺下叶实性结节，建议
随诊；右肺上叶钙化灶。4.贫血征象，请结合
实验室检查；主动脉粥样硬化。5.胸椎退行性
变。6.PICC管置入术后。（上述1-5条较前大
致相仿）
---
报告详情
检查
常规心电图
姓名
男 63岁
检查时间
2026-02-05 11:17:16
诊断意见
1.窦性心律2.正常范围心电图
报告文件
预览 >
2026-08-10 15:01:14,429 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 15:01:14,429 INFO     29 [Trace] task=7630dbd0 | doc=YXHU  62  男  直肠癌肺转移  贵州(2).pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "16 items, types={'LabReport': 6, 'DischargeRecord': 2, 'ExaminationReport': 8}", "name": "YXHU  62  男  直肠癌肺转移  贵州(2).pdf", "embedding_token_consumption": 10414}
2026-08-10 15:01:14,429 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 15:01:14,780 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 15:01:14,780 INFO     29 [Trace] task=7630dbd0 | doc=YXHU  62  男  直肠癌肺转移  贵州(2).pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":16,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 15:01:14,787 INFO     29 [DIAG-EXECUTOR] row_position_int len=24 row[0]=(14, 99, 146, 214, 226) row[-1]=(14, 402, 444, 526, 538)
2026-08-10 15:01:14,788 INFO     29 [DIAG-EXECUTOR] row_position_int len=26 row[0]=(15, 99, 145, 173, 183) row[-1]=(15, 347, 375, 503, 513)
2026-08-10 15:01:14,788 INFO     29 [DIAG-EXECUTOR] row_position_int len=8 row[0]=(16, 76, 137, 251, 261) row[-1]=(16, 76, 144, 457, 466)
2026-08-10 15:01:14,788 INFO     29 [DIAG-EXECUTOR] row_position_int len=13 row[0]=(16, 314, 362, 181, 192) row[-1]=(16, 314, 340, 511, 522)
2026-08-10 15:01:14,788 INFO     29 [DIAG-EXECUTOR] row_position_int len=2 row[0]=(16, 580, 612, 294, 303) row[-1]=(16, 580, 633, 330, 339)
2026-08-10 15:01:14,788 INFO     29 [DIAG-EXECUTOR] row_position_int len=49 row[0]=(0, 0, 0, 0, 0) row[-1]=(24, 89, 124, 232, 243)
2026-08-10 15:01:14,788 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:01:14,788 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:01:14,788 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:01:14,789 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:01:14,789 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:01:14,789 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:01:14,789 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:01:14,789 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:01:14,789 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:01:14,789 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 15:01:14,798 INFO     29 set_progress(7630dbd094ca11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 15:01:14 [DOC Engine]:
Start to index...
2026-08-10 15:01:14,829 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.025s]
2026-08-10 15:01:14,834 INFO     29 set_progress(7630dbd094ca11f1bd9827cf206dfa2d), progress: 0.80625, progress_msg: 
2026-08-10 15:01:14,862 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.018s]
2026-08-10 15:01:14,889 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.014s]
2026-08-10 15:01:14,927 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.026s]
2026-08-10 15:01:14,935 INFO     29 set_progress(7630dbd094ca11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 15:01:14 Indexing done (0.14s). Task done (760.91s)
2026-08-10 15:01:14,940 INFO     29 [Done], chunks(16), token(10414), elapsed:760.91
2026-08-10 15:01:15,485 INFO     29 handle_task done for task {"id": "7630dbd094ca11f1bd9827cf206dfa2d", "doc_id": "75fa377494ca11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "type": "pdf", "location": "YXHU  62  \u7537  \u76f4\u80a0\u764c\u80ba\u8f6c\u79fb  \u8d35\u5dde(2).pdf", "size": 5691282, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786373271245, "task_type": "dataflow", "root_trace_id": "f73917484d364912b0e50a69ca4ff02e", "root_traceparent": "00-f73917484d364912b0e50a69ca4ff02e-968d29691f13ac73-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
