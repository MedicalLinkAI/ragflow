# 基准结果：DAXI-哮喘.pdf

## 基本信息

- 文件：`DAXI-哮喘.pdf`
- 大小：24796.9 KB
- PDF 总页数：52
- doc_id：`399fea9890bb11f1a3da71efcdd7cc1f`
- 上传方式：upload_file+upload
- 状态：run=RUNNING (code=RUNNING)  progress=0.40066665
- 开始时间：2026-08-05T18:48:40  完成时间：2026-08-05T19:04:34  耗时：953.9s
- progress_msg：`10:48:35 Indexing done (0.09s). Task done (299.02s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

**该文档没有任何 chunk（文档级被过滤或解析失败）**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 14 | 0 | 2 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 1 | 0 | 0 | encounter_date, dm_admission_time, cc_text, department | **LOST** |
| DischargeRecord | 出院 | 1 | 0 | 0 | admission_date, discharge_date, department, outcome | **LOST** |
| MedicationRecord | 购药 | 0 | 0 | 3 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 1 | 0 | 4 | encounter_date, prescriber, diagnosis | **OK** |
| ExaminationReport | 检查报告 | 5 | 0 | 2 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 15 | 0 | 1 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"ExaminationReport": 5, "AdmissionRecord": 1, "DischargeRecord": 1, "OutpatientRecord": 14, "LabReport": 15, "PrescriptionRecord": 1}`
- ChunkMerger：`{}`
- Extractor skip 证据：4 条
  - `[no_items_extracted] 2026-08-05 10:59:59,706 WARNING  29 [qwen-vl-table] page=42 no items extracted`
  - `[no_items_extracted] 2026-08-05 10:59:59,706 WARNING  29 [qwen-vl-table] No items extracted from any page`
  - `[no_items_extracted] 2026-08-05 11:00:00,586 WARNING  29 [qwen-vl-table] page=42 no items extracted`
  - `[no_items_extracted] 2026-08-05 11:00:00,586 WARNING  29 [qwen-vl-table] No items extracted from any page`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
6.59
6.83
103.5
MEF 75
[L/s]
5.80
3.41
58.8
MEF 50
[L/s]
4.10
2.30
56.2
MEF 25
[L/s]
1.77
0.45
25.4
MMEF 75/25
[L/s]
3.53
0.95
26.9
MVV
[L/min]
103.77
FEV 1*30
[L/min]
103.77
63.70
61.4
RV-SB
[L]
1.62
2.06
127.2
RV%TLC-SB
[%]
33.24
40.20
120.9
TLC-SB
[L]
4.97
5.13
103.3
FRC-SB
[L]
2.69
2.97
110.3
FRC%TLC-SB
[%]
51.82
57.88
111.7
DLCO SB
[mmol/min/kPa]
8.54
5.51
(64.6)
医生意见：
阻塞型轻度通气功能障碍，小气道功能障碍。
弥散功能降低。残总比 40.20 %。
vivo X80 · ZEISS
2025/09/19 18:09
操作者：
Vol [L]
6
6
TLC
FRC
R
0
Pred
0.5
1.0
1.5
2.0
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
100
Vol [L]
Vol [L]
10
80
60
40
20
0
0
2
4
6
8
10
Time [s]
Volume [L]
4
2
0
0
2
4
10
20
30
40
Time [s]
2026-08-05 10:48:34,552 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-05 10:48:34,553 INFO     29 [Trace] task=8196e73a | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "12 items, types={'LabReport': 1, 'OutpatientRecord': 2, 'MedicationRecord': 3, 'PrescriptionRecord': 4, 'ExaminationReport': 2}", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "embedding_token_consumption": 4262}
2026-08-05 10:48:34,553 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-05 10:48:34,979 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-05 10:48:34,979 INFO     29 [Trace] task=8196e73a | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":12,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-05 10:48:34,985 INFO     29 [DIAG-EXECUTOR] row_position_int len=32 row[0]=(4, 118, 167, 385, 403) row[-1]=(5, 117, 192, 817, 836)
2026-08-05 10:48:34,985 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 10:48:34,985 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 10:48:34,985 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 10:48:34,985 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 10:48:34,985 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 10:48:34,985 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 10:48:34,985 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 10:48:34,985 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 10:48:34,985 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 10:48:34,985 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 10:48:34,985 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 10:48:34,993 INFO     29 set_progress(8196e73a90ba11f1a3da71efcdd7cc1f), progress: 0.82, progress_msg: 10:48:34 [DOC Engine]:
Start to index...
2026-08-05 10:48:35,017 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.018s]
2026-08-05 10:48:35,023 INFO     29 set_progress(8196e73a90ba11f1a3da71efcdd7cc1f), progress: 0.8083333333333333, progress_msg: 
2026-08-05 10:48:35,047 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.016s]
2026-08-05 10:48:35,069 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.013s]
2026-08-05 10:48:35,078 INFO     29 set_progress(8196e73a90ba11f1a3da71efcdd7cc1f), progress: 1.0, progress_msg: 10:48:35 Indexing done (0.09s). Task done (299.02s)
2026-08-05 10:48:35,084 INFO     29 [Done], chunks(12), token(4262), elapsed:299.02
2026-08-05 10:48:35,241 INFO     29 handle_task done for task {"id": "8196e73a90ba11f1a3da71efcdd7cc1f", "doc_id": "814bf36a90ba11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "type": "pdf", "location": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "size": 8973761, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1785926613770, "task_type": "dataflow", "root_trace_id": "12c4871fceee431eb158a2d467b8983b", "root_traceparent": "00-12c4871fceee431eb158a2d467b8983b-61cb8da4a51075eb-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-05 10:48:43,128 INFO     29 [DEBUG-COLLECT] got redis_msg, msg_id=1785926923060-0
2026-08-05 10:48:43,128 INFO     29 [DEBUG-COLLECT] msg keys=['id', 'doc_id', 'from_page', 'to_page', 'task_type', 'priority', 'begin_at', 'create_time', 'create_date', 'update_time', 'update_date', 'root_trace_id', 'root_traceparent', 'trace_source', 'kb_id', 'tenant_id', 'dataflow_id', 'file'], task_type=dataflow, id=39f0723890bb11f1a3da71efcdd7cc1f
2026-08-05 10:48:43,129 INFO     29 [DEBUG-COLLECT] normal branch, calling TaskService.get_task(39f0723890bb11f1a3da71efcdd7cc1f)
2026-08-05 10:48:43,134 INFO     29 [DEBUG-COLLECT] get_task returned: <class 'dict'>, is_none=False
2026-08-05 10:48:43,135 INFO     29 handle_task begin for task {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-05 10:48:43,340 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.002s]
2026-08-05 10:48:43,398 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-05 10:48:43,433 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-05 10:48:43,433 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-05 10:48:43,457 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-05 10:48:43,457 INFO     29 ============================================================
2026-08-05 10:48:43,457 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-05 10:48:43,457 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-05 10:48:43,457 INFO     29 ============================================================
2026-08-05 10:48:43,457 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-05 10:48:43,457 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-05 10:48:43,459 INFO     29 No torch found.
2026-08-05 10:48:48,863 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=52
2026-08-05 10:48:49,007 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1118960, prompt_len=764
2026-08-05 10:48:50,603 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-01-29"
}
```
2026-08-05 10:48:50,603 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=2026-01-29
2026-08-05 10:48:50,616 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1118960, prompt_len=401
2026-08-05 10:48:56,127 INFO     29 [qwen-vl-parser] text API response (len=983):
["呼出气一氧化氮测定报告单", "病人信息：", "编号：482", "姓名：", "年龄：41岁9月27天", "性别：女", "科室：普通儿科一区", "出生日期：1984-04-02", "测定时间：2026/1/29 11:02:42", "测定信息：", "一小时内禁止饮食：■是", "一小时内禁止剧烈运动：■是", "三小时内禁止食用特殊食品*：■是", "一小时内禁止抽烟：■是", "三天内使用激素类药物：■是 □否", "三天内使用抗生素：□是 ■否", "症状：□咳嗽 □喘息 □鼻塞 □喷嚏 ■其他", "病史：□过敏史 □其它", "*是指西兰花、芥蓝、生菜、莴苣、芹菜、水萝卜、熏制、腌制类食品。", "测定项目：", "呼气方式：■在线 □离线 □潮气", "呼气温度：20.1℃", "呼气压力：13.6cmH20", "呼气平均流速：48ml/s", "呼气NO浓度：", "32.7,31.0,32.0,31.8,32.1,31.7ppb", "呼气NO浓度均值：32ppb", "呼气方式：■在线 □离线 □潮气", "呼气温度：20.3℃", "呼气压力：7.9cmH20", "呼气平均流速：207ml/s", "呼气NO浓度：", "11.7,11.9,11.3,11.6,11.6,11.6ppb", "呼气NO浓度均值：12ppb", "测定结果：", "FeNO50：32ppb", "FeNO200：12ppb", "CaNO：3.6ppb", "测定意义：", "测定浓度", "参考值", "炎症鉴别诊断", ">12岁", "≤12岁", "FeNO50", "<25ppb", "<20ppb*", "非嗜酸性气道炎症", "25-50ppb", "20-35ppb*", "混合型气道炎症", "≥50ppb", "≥35ppb*", "嗜酸性气道炎症", "FeNO200", ">10ppb", ">8ppb", "小气道炎症", "CaNO", ">5ppb", ">3ppb", "肺泡炎症", "(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)", "复查时间：", "操作员：赵彩红", "医生：马春英", "电", "告", "单", "更", ""]
2026-08-05 10:48:56,127 INFO     29 [qwen-vl-parser] page=1 text: 70 lines (bbox 0-69)
2026-08-05 10:48:56,127 INFO     29 [qwen-vl-parser] page=1 text: 70 sections
2026-08-05 10:48:56,273 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1156349, prompt_len=764
2026-08-05 10:48:57,839 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-01-15"
}
```
2026-08-05 10:48:57,839 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=2026-01-15
2026-08-05 10:48:57,852 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1156349, prompt_len=401
2026-08-05 10:49:02,844 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T10:49:02.844+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 10:49:07,257 INFO     29 [qwen-vl-parser] text API response (len=1845):
["肺功能检查报告单", "姓名：", "测试号：", "住院号：", "身高：", "160 cm", "年龄：", "41 岁", "体重：", "48 kg", "性别：", "女", "身份证号：", "科别：", "联系电话：", "预计值", "Bst % (Bst/", "A1", "A2", "A3", "FVC", "[L]", "3.13", "3.15", "100.54", "3.15", "3.08", "3.07", "FEV 1", "[L]", "2.70", "1.99", "73.90", "1.99", "1.85", "1.96", "FEV6", "[L]", "3.13", "3.13", "3.05", "FEV 1 % FVC", "[%]", "83.98", "63.25", "75.31", "63.25", "60.02", "63.82", "FEV 1 % VC MAX", "[%]", "81.31", "63.25", "77.78", "63.25", "58.74", "62.12", "FIF 50", "[L/s]", "5.84", "5.77", "5.84", "5.48", "FEV3 % FVC", "[%]", "89.30", "89.30", "87.11", "88.97", "VC MAX", "[L]", "3.19", "3.15", "98.65", "2.99", "PEF", "[L/s]", "6.46", "6.33", "97.97", "6.33", "5.90", "5.95", "MMEF 75/25", "[L/s]", "3.53", "1.06", "30.03", "1.06", "0.89", "0.99", "MEF 25", "[L/s]", "1.77", "0.46", "26.28", "0.46", "0.38", "0.40", "MEF 50", "[L/s]", "4.06", "1.25", "30.90", "1.25", "1.13", "1.24", "MEF 75", "[L/s]", "5.73", "3.01", "52.56", "3.01", "2.22", "2.68", "V backextrapolation [B]", "0.06", "0.06", "0.05", "0.06", "V backextrapol. % FVC", "1.86", "1.86", "1.52", "1.82", "FET", "[s]", "8.73", "8.73", "5.99", "6.71", "FEF 200-1200", "[L/s]", "3.07", "3.07", "2.51", "2.98", "FVC IN", "[L]", "3.19", "2.99", "93.64", "2.26", "2.99", "2.94", "FIV1", "[L]", "2.96", "2.24", "2.96", "2.92", "FIV1 % FVC", "[%]", "99.14", "99.32", "99.14", "99.48", "FEF50 % FIF50", "[%]", "21.46", "21.72", "19.34", "22.60", "PIF", "[L/s]", "6.10", "5.87", "6.10", "5.50", "MVV", "[L/min]", "101.9", "91.45", "89.73", "91.45", "BF MVV", "[1/min]", "75.65", "75.65", "Flow [L/s]", "F/V ex", "Vol [L]", "Vol%VCmax", "Vol [L]", "Time [s]", "Vol [L]", "Time [s]", "意见：", "1.轻度阻塞性通气功能障碍。", "检查质量：FVC：A级。 FEV1：A级。", "备注：受检者检查配合佳。结果仅供参考，请结合临床分析。", "2.最大自主分钟通气量（MVV）在正常范围。", "备注：患者MVV配合佳。结果仅供参考，请结合临床分析。", "审核医生：孙帅森", "检测技师：韦龙华", "2026/1/15", ""]
2026-08-05 10:49:07,257 INFO     29 [qwen-vl-parser] page=2 text: 196 lines (bbox 70-265)
2026-08-05 10:49:07,258 INFO     29 [qwen-vl-parser] page=2 text: 196 sections
2026-08-05 10:49:07,372 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=812029, prompt_len=764
2026-08-05 10:49:08,724 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-05 10:49:08,725 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-05 10:49:08,746 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=812029, prompt_len=401
2026-08-05 10:49:14,962 INFO     29 [qwen-vl-parser] text API response (len=1176):
["肺功能报告单", "姓名：", "性别：女", "出生日期：1984/11/02", "年龄：41岁", "住院号：", "测试号：", "身高：160 cm", "体重：48 kg", "身份证号：", "预计", "实1 %(实1/预)", "实2 %(实2/预)", "变异率", "测试日期", "26/1/15", "26/1/15", "测试时间", "9:51:00上午", "10:14:56上午", "FVC", "[L]", "3.13", "3.15", "100.5", "3.25", "103.9", "3.3", "FEV 1", "[L]", "2.70", "1.99", "73.9", "2.26", "83.8", "13.4", "FEV 1 % FVC", "[%]", "83.98", "63.25", "75.3", "69.40", "82.6", "9.7", "FEV 1 % VC MAX", "[%]", "81.31", "63.25", "77.8", "69.40", "85.4", "9.7", "PEF", "[L/s]", "6.46", "6.33", "98.0", "7.25", "112.2", "14.5", "MEF 75", "[L/s]", "5.73", "3.01", "52.6", "3.73", "65.1", "23.8", "MEF 50", "[L/s]", "4.06", "1.25", "30.9", "1.67", "41.2", "33.3", "MEF 25", "[L/s]", "1.77", "0.46", "26.3", "0.59", "33.6", "27.7", "MMEF 75/25", "[L/s]", "3.53", "1.06", "30.0", "1.46", "41.3", "37.6", "FET", "[s]", "8.73", "4.94", "-43.4", "V backextrapolation ex [L]", "0.06", "0.07", "20.1", "V backextrapol. % FVC [%]", "1.86", "2.17", "16.3", "Flow [L/s]", "F/V ex", "10", "5", "0", "1", "2", "3", "4", "5", "6", "7", "10", "F/V In", "医生意见：", "支气管舒张试验阳性。", "(通过储雾罐吸入硫酸沙丁胺醇气雾剂400ug20分钟后。", "FEV1较基线增加大于12 %，且绝对值增加大于200 ml。", "审核医生：孙帅森", "检测技师：朱龙华", ""]
2026-08-05 10:49:14,962 INFO     29 [qwen-vl-parser] page=3 text: 125 lines (bbox 266-390)
2026-08-05 10:49:14,963 INFO     29 [qwen-vl-parser] page=3 text: 125 sections
2026-08-05 10:49:15,109 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1188351, prompt_len=764
2026-08-05 10:49:16,526 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2025-04-11"
}
```
2026-08-05 10:49:16,526 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=2025-04-11
2026-08-05 10:49:16,535 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1188351, prompt_len=401
2026-08-05 10:49:25,645 INFO     29 [qwen-vl-parser] text API response (len=1859):
["肺功能报告单", "姓名：", "出生日期：1984/4/02", "门诊/住院/体检：", "身高：160 cm", "身份证号：", "性别：女", "年龄：41岁", "测试号：", "体重：50 kg", "测试日期", "测试时间", "预计", "实测 % (实/预)", "25/4/11", "14:56:4", "VT", "[L]", "0.36", "0.41", "114.9", "BF", "[1/min]", "20.00", "20.79", "104.0", "MV", "[L/min]", "7.14", "8.54", "119.5", "ERV", "[L]", "1.07", "1.07", "99.4", "VC MAX", "[L]", "3.19", "2.84", "88.9", "FVC", "[L]", "3.13", "2.84", "90.6", "FEV 1", "[L]", "2.70", "1.53", "56.9", "FEV 1 % FVC", "[%]", "83.98", "54.07", "64.4", "FEV 1 % VC MAX", "[%]", "81.31", "54.07", "66.5", "PEF", "[L/s]", "6.46", "4.56", "70.7", "MEF 75", "[L/s]", "5.73", "1.84", "32.1", "MEF 50", "[L/s]", "4.06", "0.84", "20.7", "MEF 25", "[L/s]", "1.77", "0.28", "15.6", "MMEF 75/25", "[L/s]", "3.53", "0.65", "18.3", "FET", "[s]", "8.46", "V backextrapolation ex", "[L]", "0.03", "V backextrapol. % FVC", "[%]", "1.23", "MVV", "[L/min]", "101.93", "75.75", "74.3", "FEV 1*30", "[L/min]", "101.93", "46.03", "45.2", "RV-SB", "[L]", "1.55", "2.56", "164.9", "RV%TLC-SB", "[%]", "32.90", "47.52", "144.4", "TLC-SB", "[L]", "4.77", "5.39", "112.9", "FRC-SB", "[L]", "2.63", "3.31", "126.0", "FRC%TLC-SB", "[%]", "51.66", "61.42", "118.9", "DLCOc SB", "[mmol/min/kPa]", "8.34", "6.95", "83.4", "DLCO SB", "[mmol/min/kPa]", "8.34", "6.95", "83.4", "医生意见：", "1.中重度阻塞性通气功能障碍。", "检查质量：FVC：A级。 FEV1：A级。", "备注：受检者检查配合佳。 结果仅供参考，请结合临床分析。", "2.最大自主分钟通气量（MVV）轻度下降。", "备注：患者MVV配合佳。结果仅供参考，请结合临床分析。", "3.弥散功能在正常范围。4.残总比中度增高。", "审核医生：孙帅森", "检测技师：张青苹", "通气弥散B", "2025/4/11 15:18", "1/1", "布地奈德 4ml Bid 3天", "喷 3个月后复查肺功能。", "Vol [L]", "PredA0.0", "0.2", "0.4", "0.6", "0.8", "1.0", "Time [min]", "Flow [L/s]", "F/V ex", "10", "5", "0", "2", "4", "6", "F/V in", "10", "Vol [L]", "Vol [L]", "100", "10", "50", "Time [s]", "0", "1", "2", "3", "4", "5", "Volume [L]", "4", "2", "0", "M", "0", "2", "4", "Time [s]", "20", "40", "60", "80"]
2026-08-05 10:49:25,645 INFO     29 [qwen-vl-parser] page=4 text: 197 lines (bbox 391-587)
2026-08-05 10:49:25,645 INFO     29 [qwen-vl-parser] page=4 text: 197 sections
2026-08-05 10:49:25,756 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=801179, prompt_len=764
2026-08-05 10:49:27,246 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-05 10:49:27,246 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-05 10:49:27,256 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=801179, prompt_len=401
2026-08-05 10:49:32,875 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T10:49:32.874+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 10:49:33,526 INFO     29 [qwen-vl-parser] text API response (len=1203):
["肺功能报告单", "姓名：", "性别：女", "出生日期：1984/4/02", "年龄：41岁", "门诊/住院/体检：", "测试号：", "身高：160 cm", "体重：50 kg", "身份证号：", "预计", "实1 %(实1/预)", "实2 %(实2/预)", "变异率", "测试日期", "25/4/11", "25/4/11", "测试时间", "14:56:47下午", "15:14:32下午", "FVC", "[L]", "3.13", "2.84", "90.6", "3.05", "97.4", "7.5", "FEV 1", "[L]", "2.70", "1.53", "56.9", "1.91", "71.0", "24.7", "FEV 1 % FVC", "[%]", "83.98", "54.07", "64.4", "62.70", "74.7", "16.0", "FEV 1 % VC MAX", "[%]", "81.31", "54.07", "66.5", "62.70", "77.1", "16.0", "PEF", "[L/s]", "6.46", "4.56", "70.7", "5.64", "87.3", "23.6", "MEF 75", "[L/s]", "5.73", "1.84", "32.1", "2.65", "46.3", "44.3", "MEF 50", "[L/s]", "4.06", "0.84", "20.7", "1.23", "30.4", "47.0", "MEF 25", "[L/s]", "1.77", "0.28", "15.6", "0.44", "25.0", "60.2", "MMEF 75/25", "[L/s]", "3.53", "0.65", "18.3", "1.02", "29.1", "58.8", "FET", "[s]", "8.46", "6.41", "-24.2", "V backextrapolation ex [L]", "0.03", "0.06", "71.7", "V backextrapol. % FVC [%]", "1.23", "1.96", "59.6", "Flow [L/s]", "F/V ex", "10", "5", "0", "1", "2", "3", "4", "5", "6", "7", "10", "F/V In", "医生意见：", "支气管舒张试验阳性。", "（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后。", "FEV1较基线增加大于12%，且绝对值增加大于200ml。）", "审核医生：孙帅森", "检测技师：张青苹", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 10:49:33,526 INFO     29 [qwen-vl-parser] page=5 text: 127 lines (bbox 588-714)
2026-08-05 10:49:33,526 INFO     29 [qwen-vl-parser] page=5 text: 127 sections
2026-08-05 10:49:33,703 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1461935, prompt_len=764
2026-08-05 10:49:35,087 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-05 10:49:35,088 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-05 10:49:35,102 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1461935, prompt_len=401
2026-08-05 10:49:41,595 INFO     29 [qwen-vl-parser] text API response (len=1085):
["院", "入院记录", "姓名：", "科室：产科二区", "床号：", "科室：产科二区", "第(1)次入院记录", "过敏史：无", "姓名：", "性别：女", "年龄：36岁", "身份证号", "职业：", "婚姻：已婚", "民族：汉族", "出生地：", "现住址：", "入院日期：2020-07-08 08:36:09", "邮编", "病史采集时间：2020-07-08 08:36:09", "联系人：", "与病人关系：夫妻", "病史叙述者：本人", "联系人地址：同上地址", "电话.", "可靠程度：可靠", "主诉：停经39周，要求住院待产。", "现病史：平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日（阳历），预产", "期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单活胎，发育符合", "孕周。孕早期无早孕反应，孕早期无腹痛、出立，阴道流液，出血史，无放射线、有害物质接", "触史。孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正常，孕中期行无创DNA", "结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正常，未行糖耐量筛", "查，未查B族链球菌。孕期经过顺利，孕晚期无头痛、头晕、眼花等症状，无皮肤黄染及痰", "痒。现停经39周，无腹痛，未见红及破水，遂入院要求住院待产，门诊以“足月妊娠、瘢痕子", "宫”收住院。自孕以来精神好，饮食、睡眠好，大小便正常，体重增加约10KG。", "既往史：患者平素体健；否认有“心脏病、高血压、糖尿病、肾病”等慢性病史，否认有", "“肝炎、结核”等传染性疾病。于2016.08行剖宫产手术，否认余手术及外伤史。否认有输血", "史，有献血史，否认食物及药物过敏史。预防接种随社会进行。", "个人史：出生于原籍，护士，本科文化，工作于三门峡市中心医院。否认长期外地居住", "史，无疫区居住史，无烟酒等不良嗜好。生长环境一般，否认有冶游史。", "婚育史：31岁结婚，爱人", "现年37岁，职员，工作于三门峡市党校，身体健康，无吸", "烟史，有饮酒史，否认“肝炎、结核”病史，夫妻感情好。孕;产;，2016年足月剖宫产1活男", "婴，现体健，否认产后出血及产褥感染史，否认不良孕产史。", "月经史：平素月经规律，12岁，5-7天/30-35天，末次月经为：2019年10月08日（阳", "历），量中等，色暗红，偶有血块，无痛经。", "页", "书写者签名：", "总第 页"]
2026-08-05 10:49:41,596 INFO     29 [qwen-vl-parser] page=6 text: 49 lines (bbox 715-763)
2026-08-05 10:49:41,596 INFO     29 [qwen-vl-parser] page=6 text: 49 sections
2026-08-05 10:49:41,766 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1364661, prompt_len=764
2026-08-05 10:49:43,135 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 10:49:43,136 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-05 10:49:43,160 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1364661, prompt_len=401
2026-08-05 10:49:48,784 INFO     29 [qwen-vl-parser] text API response (len=932):
["院", "入院记录", "姓名:", "科室:产科二区", "床号:", "生.", "家族史:父母亲体健,1弟1妹均体健,1子体健,否认家族中有遗传性及传染性疾病史。", "体格检查", "体温:36.5℃", "脉搏:78次/分", "呼吸:18次/分", "血压:98/64mmHg", "身高160cm", "体重:60Kg", "一般状况:发育正常;营养中等;自动体位:面色红润;面容及表情自如;神志清晰;言", "语状态流利;检查时能合作等。", "皮肤:色泽正常,弹性正常,无水肿、出汗、紫癜、皮疹、色素沉着、蜘蛛痣、瘢痕、创", "伤、溃疡、结节。", "淋巴结:全身或局部表浅淋巴结未触及肿大;局部皮肤无红热、瘘管、瘢痕。", "头部:", "头颅:大小无异常、外形无异常;眉发分布正常;无疖、痈、外伤、瘢痕、肿块。", "眼部:双眼裂正常,双眼睑无水肿,眼球运动正常。瞳孔:左3.0mm直接对光反应灵敏,", "间接对光反应灵敏;右3.0mm直接对光反应灵敏,间接对光反应灵敏。视力粗测正常。", "耳部:耳廓无畸形,外耳道无分泌物,乳突无压痛,听力粗测5米。", "鼻部:无畸形、鼻翼扇动、阻塞、分泌物、鼻中隔异常、嗅觉障碍、鼻窦压痛等。", "口腔:口唇红润,无畸形、疱疹、微血管搏动、口角皲裂;牙齿无缺损、龋病、镶补等异", "常;牙龈无溢血、溢脓、萎缩、色素沉着;口腔粘膜无溃疡、假膜、色素沉着;扁桃体无肿", "大、分泌物;咽部无充血、分泌物。", "颈部:对称,无强直、压痛、运动受限、颈静脉怒张、颈动脉明显搏动、肿块,气管居", "中,甲状腺无肿大。", "胸部", "胸廓:形状正常,对称,运动程度正常,肋间正常,胸壁无水肿、皮下气肿、肿块、静脉", "曲张,肋骨及肋软骨无压痛、凹陷等异常。乳头,正常。", "肺脏:视诊:腹式呼吸,呼吸节律正常,呼吸深度正常,两侧呼吸运动对称。", "触诊:语音震颤两侧相等,无摩擦感。", "叩诊:叩诊声响清音,肺下界肩胛线在第10肋间,呼吸移动度6cm,", "听诊:呼吸音性质为肺泡呼吸音,强度正常,语音传导正常,无摩擦音、哮鸣音、", "第页", "书写者签名:", "总第页"]
2026-08-05 10:49:48,784 INFO     29 [qwen-vl-parser] page=7 text: 40 lines (bbox 764-803)
2026-08-05 10:49:48,787 INFO     29 [qwen-vl-parser] page=7 text: 40 sections
2026-08-05 10:49:48,958 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1258831, prompt_len=764
2026-08-05 10:49:50,441 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 10:49:50,441 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=None
2026-08-05 10:49:50,451 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1258831, prompt_len=401
2026-08-05 10:49:55,680 INFO     29 [qwen-vl-parser] text API response (len=817):
["院", "入院记录", "姓名：", "科室：产科二区", "床号", "病号：", "干啰音、湿啰音。", "心脏：视诊：心尖搏动的位置在左侧锁骨中线内第4肋间，范围为2.5cm，强度正常，心前", "区无异常搏动、局限性膨隆。", "触诊：心尖搏动最强部位在左侧锁骨中线第4肋间，范围为2.5cm，无抬举性搏动、", "震颤、摩擦感。", "叩诊：左右心界线以每肋间距胸骨中线的cm数记载。", "右cm", "肋间", "左cm", "2", "Ⅱ", "2.5", "2", "Ⅲ", "4", "3", "Ⅳ", "5.5", "V", "8", "左锁骨中线至前正中线的距离9cm。", "听诊：心率78次/分，心律整齐，无心脏杂音，无第三心音、第四心音、心音分", "裂，P2<A2。", "血管：桡动脉搏动正常，血管壁硬度正常。", "周围血管征：无毛细血管搏动征、水冲脉、枪击音、动脉异常搏动。", "腹部：", "视诊：腹部膨隆，晓孕腹型，腹壁对称，无凹陷、膨隆、静脉曲张、蠕动波、局限性隆", "起，下腹可见一长约15cm横行手术疤痕。", "触诊：腹壁柔软，无压痛，无反跳痛；未触及肿块，无搏动、波动感等。肝脏：肋缘下未", "触及，无压痛。胆囊：未触及，无压痛。脾脏：肋缘下未触及。肾：未触及，无压痛等。", "叩诊：肝上界位于第5肋间，肝浊音界正常，肝区无叩击痛、脾区无叩击痛、腹部无过度", "鼓音，移动性浊音阴性。", "听诊：肠蠕动音正常，频率4次/分，胃区无振水声，肝区无摩擦音、脾区无摩擦音，无血", "管杂音。", "外阴及肛门：阴毛分布正常；外生殖器发育正常，肛门检查：无外痔、肛裂、肛瘘、脱", "肛、湿疣等。", "脊柱：脊柱无畸形、压痛、叩击痛；脊柱两侧肌肉无紧张、压痛；肋脊角无压痛、叩痛。", "四肢：无畸形、杵状指（趾）、静脉曲张、外伤、骨折；肌肉张力正常与肌力5级，无萎"]
2026-08-05 10:49:55,681 INFO     29 [qwen-vl-parser] page=8 text: 44 lines (bbox 804-847)
2026-08-05 10:49:55,681 INFO     29 [qwen-vl-parser] page=8 text: 44 sections
2026-08-05 10:49:55,783 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=640502, prompt_len=764
2026-08-05 10:49:57,089 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 10:49:57,089 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-05 10:49:57,098 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=640502, prompt_len=401
2026-08-05 10:49:59,874 INFO     29 [qwen-vl-parser] text API response (len=428):
["院", "入院记录", "姓名.", "科室:产科二区", "床号", "住院号.", "缩;关节无红肿、畸形、运动障碍,双下肢水肿。", "神经反射:膝腱反射正常、跟腱反射正常、肱二头肌腱反射正常、肱三头肌腱反射正常、", "腹壁反射正常、巴彬斯基征阴性、克尼格征阴性等。", "专科情况", "宫高34CM,腹围102CM,估计胎儿体重:3200g,胎位:头位,胎心152次/分,律齐,无", "宫缩,未见红,未破水,骨盆外测量及内诊:未做。", "辅助检查", "B超(2020.07.02 本院):晓孕宫内单活胎头位(双顶径9.4cm,股骨长7.0cm羊水指", "数8.5cm),胎盘成熟度II°.", "初步诊断:", "1.妊娠合并子宫瘢痕;", "3.孕2产,宫内孕39周头位待产。", "主治医师:", "孙小丹", "副主任医师:", "彭琼玉", "2020.07.08", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 10:49:59,874 INFO     29 [qwen-vl-parser] page=9 text: 25 lines (bbox 848-872)
2026-08-05 10:49:59,874 INFO     29 [qwen-vl-parser] page=9 text: 25 sections
2026-08-05 10:50:00,071 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1627445, prompt_len=764
2026-08-05 10:50:01,490 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-05 10:50:01,490 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=None
2026-08-05 10:50:01,508 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1627445, prompt_len=401
2026-08-05 10:50:02,894 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T10:50:02.892+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 10:50:09,370 INFO     29 [qwen-vl-parser] text API response (len=1235):
["姓名：", "科室：产科二区", "床号", "住院号.", "2020年07月08日 09时22分", "首次病程记录", "患", "女，36岁，汉族，-以“停经39周，要求住院待产”为主诉于", "2020-07-08 08:36:09入院。一、病例特点：1、已婚育龄妇女，孕₂产₁，否认产后出血及产褥", "感染史，否认不良孕产史；2、平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日", "(阳历)，预产期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单", "活胎，发育符合孕周。3、孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正", "常，孕中期行无创DNA结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正", "常，未行糖耐量筛查，未查B族链球菌。4、现停经39周，无腹痛，未见红及破水，遂入院要求", "住院待产。5.入院查体：T：36.5℃，P：78次/分，R：18次/分，BP：98/64mmHg。神志清楚，", "精神好，全身皮肤粘膜无黄染，浅表淋巴结未触及，心肺听诊未闻及明显异常，腹膨隆。6、", "专科检查：宫高34CM，腹围102CM，估计胎儿体重：3200g，胎位：头位，胎心152次/分，律", "齐，无宫缩，未见红，未破水，骨盆外测量及内诊：未做。7、辅助检查：B超（2020.07.02", "本院）：晚孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度", "II°。二、拟诊讨论：（一）初步诊断：1.妊娠合并子宫瘢痕；2.孕₂产；宫内孕39周头位", "待产。（二）诊断依据：1、患者有停经史，平素月经规律，平素月经规律，5-7天/35-36天，", "末次月经为：2019年10月08日（阳历），预产期为2020年07月15日（阳历），停经后有自觉胎", "动，产前检查可同及胎心；2、专科检查：宫高34CM，腹围102CM，估计胎儿体重：3200g，胎", "位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水。骨盆外测量及内诊：未做。3、", "辅助检查：B超（2020.07.02本院）：晚孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm", "羊水指数8.5cm)，胎盘成熟度II°。（三）鉴别诊断：根据据病史、查体及辅助检查，目前诊", "断明确。三、诊疗计划：完善各项检查：心电图、彩超、血常规、血型、凝血五项、输血前检", "查、尿常规、心电图、肝功、肾功、血糖、电解质等；2、向患者及家属交代病情，围生期相", "关危险因素；3，给予巡视病房、监测胎心、心理疏导，消除围产期恐惧心理等产前护理；4、", "患者要求明日剖宫产，纳入剖宫产临床路径。", "主治医师：孙州", "2020年07月08日 10时22分", "科主任宋瑞香主治医师查房记录", "第页", "总第页"]
2026-08-05 10:50:09,370 INFO     29 [qwen-vl-parser] page=10 text: 35 lines (bbox 873-907)
2026-08-05 10:50:09,370 INFO     29 [qwen-vl-parser] page=10 text: 35 sections
2026-08-05 10:50:09,580 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1704714, prompt_len=764
2026-08-05 10:50:11,107 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-05 10:50:11,108 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=None
2026-08-05 10:50:11,120 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1704714, prompt_len=401
2026-08-05 10:50:17,781 INFO     29 [qwen-vl-parser] text API response (len=1066):
["姓名：", "科室：产科二区", "床号：", "住院号", "今日随科主任宋瑞香主治医师查房，患者精神好，饮食及夜眠可，大小便正常，未破", "水，未见红，无腹痛。查体：生命体征平稳，心肺听诊未闻及明显异常，胎心波动于正常范", "围，无宫缩。目前诊断：1.妊娠合并于宫瘢痕；2.孕2产；宫内孕39周头位待产。诊断依", "据：1.停经后有自觉胎动，产前检查可闻及胎心。2、查体：宫高34CM，腹围102CM，估计胎儿", "体重：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水。骨盆外测量及", "内诊：未做。3、辅助检查：B超（2020.07.02 本院）：晓孕宫内单活胎头位(双顶径", "9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。科主任宋瑞香主治医师查房指示：", "患者孕足月、瘢痕子宫，若阴道分娩易出现先兆子宫破裂、子宫破裂、胎死宫内等情况，患者", "及其家属表示理解，要求明日剖宫产终止妊娠，完善术前谈话，积极术前准备，严密监测胎心", "变化。以上医嘱已执行。", "主治医师：主治医师：", "孙丹", "2020年07月08日 10：20", "术前小结", "姓名：", "性别：女，年龄：36岁；", "病历摘要：以“伴经39周，要求住院待产”为主诉入院。孕2产，否认产后出血及产褥感", "染史，否认不良孕产史。查体：生命体征平稳，心肺听诊未闻及异常。腹隆，晚孕腹型。肝脾", "肋下未触及，下腹部可见一长约15cm的横行手术瘢痕。双下肢无水肿；专科检查：宫高34CM，", "腹围102CM，估计胎儿体重：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未", "破水。骨盆外测量及内诊：未做。辅助检查：B超（2020.07.02 本院）：晓孕宫内单活胎", "头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。入院后要求剖宫产终止", "妊娠，手术相关风险已向其讲明，并在手术同意书上签字。请示科主任宋瑞香副主任医师，同", "意安排手术，手术医师宋瑞香主治医师查看病人，生命体征平稳，无手术禁忌，积极术前准", "备。", "术前诊断：1.妊娠合并子宫瘢痕；2.孕2产；宫内孕39周头位待产。", "手术指证：足月妊娠，瘢痕子宫，患者及家属要求，无手术禁忌症：", "拟施手术名称和方式：拟定于明日07：30行二次子宫下段剖宫产术；", "拟施麻醉：椎管内麻醉；", "第 页", "总第 页"]
2026-08-05 10:50:17,782 INFO     29 [qwen-vl-parser] page=11 text: 35 lines (bbox 908-942)
2026-08-05 10:50:17,782 INFO     29 [qwen-vl-parser] page=11 text: 35 sections
2026-08-05 10:50:17,854 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=223732, prompt_len=764
2026-08-05 10:50:19,236 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 10:50:19,237 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=None
2026-08-05 10:50:19,255 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=223732, prompt_len=401
2026-08-05 10:50:20,108 INFO     29 [qwen-vl-parser] text API response (len=107):
["姓名：", "科室：产科二区", "床号：", "注意事项：规范操作，彻底止血，待新生儿娩出后，给予“缩宫素针”促宫缩治疗，做好", "新生儿复苏工作。", "主治医师：孙丹丹", "第 页", "总第 页"]
2026-08-05 10:50:20,109 INFO     29 [qwen-vl-parser] page=12 text: 8 lines (bbox 943-950)
2026-08-05 10:50:20,109 INFO     29 [qwen-vl-parser] page=12 text: 8 sections
2026-08-05 10:50:20,318 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1680903, prompt_len=764
2026-08-05 10:50:21,830 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-05 10:50:21,830 INFO     29 [qwen-vl-parser] page=13 classify=text report_date=None
2026-08-05 10:50:21,843 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1680903, prompt_len=401
2026-08-05 10:50:28,428 INFO     29 [qwen-vl-parser] text API response (len=1078):
["院", "姓名：", "科室：产科二区", "床：", "住院号：", "2020年07月09日 09时47分", "术后首次病程记录", "患者术前测胎心150次/分，于今日08：29-09：30在腰硬联合麻醉+基础麻醉下行二次子宫", "下段剖宫产术+子宫修补术，取下腹原横切口，剔除原瘢痕，逐层进腹，膀下指膀胱，暴露子", "宫下段，可见于宫下段肌层较薄，胎儿头发及胎脂漂浮，切开子宫后见羊水清，约600ml，吸", "净后以头位助娩一活男婴，出生1-10分钟均评10分，胎盘胎膜自娩完整，子宫收缩可，纱布球", "擦拭子宫腔，可见子宫下段肌层断裂，用可吸收线间断缝合子宫下段肌层，断裂的血管给予缝", "合，以恰桥可吸收线分两层连续缝合子宫切口。探查子宫切口无活动性出血，双侧附件外观正", "常，关腹。术程顺利，术中麻醉好，呼吸血压平稳，输入晶体液800ml，胶体液0ml，出血不", "多，约200ml，尿色清，量约100ml，术中诊断：1.妊娠合并子宫瘢痕；2.孕2产：宫内孕39*1周", "头位剖宫产；术后安返病房，测P：64次/分，R：18次/分，Bp：84/54mmHg，术后给予“头", "孢唑林钠针”预防感染、加强宫缩、会阴冲洗、尿管护理及支持对症等治疗，并嘱其按摩双下", "肢预防下肢静脉血栓形成，注意观察生命体征、子宫收缩及阴道出血情况。", "住院医师：冯雪云", "2020年07月10日 09时00分", "彭琼玉副主任医师查房记录", "今日为剖宫产术后一天，患者精神、睡眠好，无特殊不适，未排气。彭琼玉副主任医师", "查房：查体：生命体征平稳，双乳不胀，无泌乳，心肺未闻及异常，腹软，腹部切口皮肤对合", "好，未见红肿、硬结等异常，宫底平脐，子宫收缩好，阴道出血不多，尿管畅，尿色清，尿量", "正常，余查无特殊，查房意见：现术后一天，未排气，流食，体温正常，切口无感染迹象，病", "情无特殊，继续抗炎补液加强宫缩等治疗；嘱患者床上多翻身并按摩双下肢，以防术后肠粘连", "及栓塞性疾病发生，给予肌注缩宫素10uBID促进子宫收缩，给予子宫复旧磁疗促进产后子宫", "恢复，嘱保持乳房畅通，并给予泌乳磁疗促进乳汁分泌，输完液体后拔除尿管，适当下床活", "动，注意监测血糖情况，上述指示已执行。", "副主任医师：马", "住院医师：冯雪云", "2020年07月11日 08时06分", "术后第二天，患者无发热，已排气，尿管拔除后排尿畅。查体：生命体征平稳，心肺听诊", "第 页", "总第 页"]
2026-08-05 10:50:28,429 INFO     29 [qwen-vl-parser] page=13 text: 35 lines (bbox 951-985)
2026-08-05 10:50:28,429 INFO     29 [qwen-vl-parser] page=13 text: 35 sections
2026-08-05 10:50:28,576 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1041724, prompt_len=764
2026-08-05 10:50:29,961 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-05 10:50:29,961 INFO     29 [qwen-vl-parser] page=14 classify=text report_date=None
2026-08-05 10:50:29,975 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1041724, prompt_len=401
2026-08-05 10:50:32,928 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T10:50:32.927+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 10:50:33,767 INFO     29 [qwen-vl-parser] text API response (len=629):
["出院", "姓名：", "科室：产科二区", "床号", "住院", "未闻及异常，双乳泌乳量不多，腹软，子宫收缩好，宫底位于脐下两横指，无压痛，阴道出血", "不多，暗红色，无异味，腹部切口换药见切口皮缘对合好，未见红肿、硬结及渗液等异常，双", "下肢无水肿，现术后第二天，病情稳定，改为II级护理，已排气给予昔食，注意体温变化及切", "口情况；继续予子宫复旧磁疗促进产后子宫恢复，加用腹部切口红外线治疗促进伤口愈合，加", "益宫颗粒(自各药物)促宫缩治疗，观察体温及阴道恶露情况。", "主治医师：孙丹丹", "2020年07月12日10时00分", "彭琼玉副主任医师查房记录", "今日查房，患者剖宫产术后三天，患者未诉不适，精神好，饮食、睡眠正常，查体：生", "命体征平稳，心肺听诊未闻及异常，双乳泌乳量多，腹软，腹部切口无红肿、硬结、渗液等异", "常，子宫收缩好，阴道出血不多，余查无特殊，再次复查血常规：白细胞10.59×10⁹/L，中性", "粒细胞86.3%，偏高，血红蛋白100g/L，患者复查白细胞正常，中性粒细胞偏高，体温正常，", "切口无感染迹象，考虑术后炎性反应，暂不特殊处理，嘱加强营养，加强运动。彭琼玉副主任", "医师查房指示：患者现病情稳定，腹部伤口皮内结合，无需拆线，达临床治愈，顺利完成剖宫", "产临床路径管理，今日办理出院。指示已执行。", "副主任医师：彭琼玉", "主治医师：孙丹丹", ""]
2026-08-05 10:50:33,768 INFO     29 [qwen-vl-parser] page=14 text: 22 lines (bbox 986-1007)
2026-08-05 10:50:33,768 INFO     29 [qwen-vl-parser] page=14 text: 22 sections
2026-08-05 10:50:33,943 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1460379, prompt_len=764
2026-08-05 10:50:35,359 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-05 10:50:35,359 INFO     29 [qwen-vl-parser] page=15 classify=text report_date=None
2026-08-05 10:50:35,377 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1460379, prompt_len=401
2026-08-05 10:50:42,063 INFO     29 [qwen-vl-parser] text API response (len=1064):
["出院记录", "姓名", "科室：产科二区", "床号.", "住院号.", "2020年07月12日", "出院记录", "患者.", "36岁", "住院号：", "入院日期：2020-07-08 08:36:09", "出院日期：2020年07月12日", "住院天数：4天", "入院情况：以“停经39周，要求住院待产”为主诉入院。入院查体：生命体征平稳，心肺", "听诊未闻及异常。腹隆，晚孕腹型，肝脾肋下未触及。专科检查：宫高34CM，腹围102CM，估", "计胎儿体宣：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水，骨盆外", "测量及内诊：未做。辅助检查：B超（2020.07.02 本院）：晚孕宫内单活胎头位(双顶径", "9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。", "入院诊断：1.妊娠合并子宫瘢痕；2.孕产：宫内孕39周头位待产。", "诊疗经过：患者入院后完善相关检查，要求剖宫产，于2020年07月09日 08：29-09：30在", "腰硬联合麻醉+基础麻醉下行二次于宫下段剖宫产术+子宫修补术。取下腹原横切口，剔除原瘢", "痕，逐层进腹，膀下指膀胱，暴露子宫下段，可见子宫下段肌层较薄，胎儿头发及胎脂漂浮，", "切开子宫后见羊水清，约600ml，吸净后以头位助娩一活男婴，出生1-10分钟均评10分，胎盘", "胎膜自娩完整，子宫收缩可，纱布球擦拭子宫腔，可见子宫下段肌层断裂，用可吸收线间断缝", "合子宫下段肌层，断裂的立皆给予缝合，以伦桥可吸收线分两层连续缝合子宫切口。探查子宫", "切口无活动性出血，双侧附件外观正常，关腹，术程顺利，术中出血不多，术后予以降压、抗", "感染、加强宫缩支持及对症治疗。", "出院诊断：1.妊娠合并子宫瘢痕；2.孕产：宫内孕39+周头位剖宫产：", "出院情况：患者精神、饮食好，无特殊不适。查体：生命体征平稳，心肺听诊未闻及明显", "异常，双乳泌乳量可，双乳稍涨，腹部平软，切口无红肿、渗出、硬结等愈合良好，子宫收缩", "好，宫底约脐耻之间，宫体无压痛，恶露呈淡红色，量少，无异味。现患者一般情况好，双乳", "泌乳量多，子宫复旧好，腹部切口愈合良好，无需拆线，达临床治愈，于今日出院。完成计划", "性剖宫产临床路径。", "出院医嘱：1.注意休息，合理营养；", "2.禁性生活、盆浴及重体力劳动2个月；", "3.坚持纯母乳喂养大于4-6月；", "第 页", "总第 页"]
2026-08-05 10:50:42,064 INFO     29 [qwen-vl-parser] page=15 text: 38 lines (bbox 1008-1045)
2026-08-05 10:50:42,064 INFO     29 [qwen-vl-parser] page=15 text: 38 sections
2026-08-05 10:50:42,185 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=642933, prompt_len=764
2026-08-05 10:50:43,551 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 10:50:43,551 INFO     29 [qwen-vl-parser] page=16 classify=text report_date=None
2026-08-05 10:50:43,566 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=642933, prompt_len=401
2026-08-05 10:50:46,054 INFO     29 [qwen-vl-parser] text API response (len=416):
["医院", "出院记录", "姓名：", "科室：产科二区", "床号：", "住院号：2", "4.产后42天门诊复查，如出院后出现任何异常情况请立即就诊，注意产妇心理", "状态，必要时心理咨询门诊就诊；若阴道出血淋漓不尽持续1月或阴道出血量多于平素月经", "量、腹痛、发热等，及时就诊：（每周二、周六门诊326彭琼玉副主任医师坐诊）", "5.严格避孕，术后六个月可安环避孕，术后2年以上方可再次妊娠：", "6.新生儿乙肝疫苗第一针，卡介苗已接种，新生儿生后10天补充维生素AD滴剂", "1粒/次，一次/日（至2岁），出院后新生儿每日测胆红素值，黄疸加重或持续14天未消退，或", "出院后有不适，可直接到1号楼9楼新生儿科探视大厅就诊（携带宝宝就诊卡）；", "7.咨询电话产科：", "，新生儿科：0398-3118382。母乳咨询电话：", "0398-3118618.", "主治医师：", "孙州", ""]
2026-08-05 10:50:46,055 INFO     29 [qwen-vl-parser] page=16 text: 18 lines (bbox 1046-1063)
2026-08-05 10:50:46,056 INFO     29 [qwen-vl-parser] page=16 text: 18 sections
2026-08-05 10:50:46,207 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=913014, prompt_len=764
2026-08-05 10:50:47,764 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2023-08-14"}
```
2026-08-05 10:50:47,765 INFO     29 [qwen-vl-parser] page=17 classify=text report_date=2023-08-14
2026-08-05 10:50:47,780 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=913014, prompt_len=401
2026-08-05 10:50:53,173 INFO     29 [qwen-vl-parser] text API response (len=887):
["临床数据中心-患者360视图", "返回患者查询", "患者姓名", "女 出生日", "首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>", "就诊时间轴", "门诊号", "诊时间：2023-08-14 15:29:02 接诊科室：普通儿科三组（门） 接诊医生：谭真真", "全部", "近一月", "近三月", "近半年", "近一年", "近五年", "门诊39 住院1", "总览", "就诊列表", "2024-04-24 普通儿科一组（...", "2024-04-19 普通儿科一组（...", "2024-04-08 妇科门诊", "2024-04-08 妇科一病区(门)", "2024-01-05 妇科一病区(门)", "2023-08-14 普通儿科三组（...", "2023-07-06 普通儿科三组（...", "2023-06-26 普通儿科三组（...", "2023-05-08 普通儿科三组（...", "2023-05-08 普通儿科一组（...", "2023-04-18 普通儿科三组（...", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告", "1.", "门诊号.", "姓名：", "性别：女", "年龄：39岁", "民族：汉族", "身份证", "现住址：", "就诊类型：初诊", "就诊科室：普通儿科三组（门）", "就诊日期：2023-08-14 15:29", "联系电", "主诉：咽峡炎购药", "现病史：咽峡炎购药", "既往史：平素体健，无肝炎、结核类传染病史", "过敏史：无", "体格检查：发育正常，营养良好，精神一般，口唇红润，双侧扁桃体无肿大，无充血、分泌物。咽腔黏膜无充", "血、红肿、疱疹，双肺呼吸音清，听诊心律齐，无杂音，腹平软，无压痛、反跳痛", "辅助检查：", "初步印象：急性咽峡炎", "处理意见：门诊", "备注：", "医师签名：谭真真", "第1页"]
2026-08-05 10:50:53,173 INFO     29 [qwen-vl-parser] page=17 text: 53 lines (bbox 1064-1116)
2026-08-05 10:50:53,173 INFO     29 [qwen-vl-parser] page=17 text: 53 sections
2026-08-05 10:50:53,281 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=669524, prompt_len=764
2026-08-05 10:50:54,779 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-01-05"}
```
2026-08-05 10:50:54,779 INFO     29 [qwen-vl-parser] page=18 classify=text report_date=2024-01-05
2026-08-05 10:50:54,796 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=669524, prompt_len=401
2026-08-05 10:50:57,211 INFO     29 [qwen-vl-parser] text API response (len=407):
["门诊病历", "门诊号：", "姓名", "性别：女", "年龄：39岁", "民族：汉族", "身份证号", "现住址：", "就诊类型：急诊", "就诊科室：妇科一病区(门)", "就诊日期：2024-01-05 10:32", "联系电话", "主诉：下腹痛2小时", "现病史：患者月经第二天，无明显诱因出现下腹持续疼痛", "既往史：平素体健，无高血压、冠心病、糖尿病病史，无肝炎、结核等传染病史，无手术史", "婚育史：", "月经史：患者平素月经规律，量中等，色正常，无痛经。", "过敏史：无", "专科检查：外阴：发育正常，阴毛呈女性分布；阴道：通畅，粘膜红润，未见异常分泌物；宫颈：光滑，大小正常，宫体：正常大小，无压痛。附件：左侧附件区压痛明显。", "辅助检查：", "初步印象：女性盆腔炎性疾病", "处理意见：门诊治疗", "备注：", "医师签名：汪会芳", "第1页", ""]
2026-08-05 10:50:57,211 INFO     29 [qwen-vl-parser] page=18 text: 25 lines (bbox 1117-1141)
2026-08-05 10:50:57,212 INFO     29 [qwen-vl-parser] page=18 text: 25 sections
2026-08-05 10:50:57,350 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=908963, prompt_len=764
2026-08-05 10:50:58,739 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-04-08"}
```
2026-08-05 10:50:58,739 INFO     29 [qwen-vl-parser] page=19 classify=text report_date=2024-04-08
2026-08-05 10:50:58,749 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=908963, prompt_len=401
2026-08-05 10:51:02,953 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T10:51:02.952+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 10:51:05,185 INFO     29 [qwen-vl-parser] text API response (len=1137):
["三门峡市中心医院门户-患者360 ×", "← → C ① 不安全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView", "临床数据中心-患者360视图", "返回患者查询 患者姓名:", "女 出", "期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>", "就诊时间轴", "门诊号", "就诊时间: 2024-04-08 09 44 02 接诊科室: 妇科一病区(门) 接诊医生: 权丽丽", "全部 近一月 近三月 近半年 近一年", "近五年", "门诊39 住院1", "总览 就诊列表", "2025-04-11 哮喘危重—病达(I J)", "2025-01-06 普通儿科三组 (...", "2024-12-30 普通儿科三组 (...", "2024-07-05 普通儿科一组 (...", "2024-04-24 普通儿科一组 (...", "2024-04-19 普通儿科一组 (...", "2024-04-08 妇科门诊", "2024-04-08 妇科一病区(门)", "2024-01-05 妇科一病区(门)", "2023-08-14 普通儿科三组 (...", "2023-07-06 普通儿科三组 (...", "集放视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告", "检验报告", "门诊号:", "姓名", "性别: 女", "年龄:40岁", "民族: 汉族", "身份证号", "现住址:", "就诊类型:初诊", "就诊科室:妇科一病区(门)", "就诊日期: 2024-04-08 09:44", "联系电话", "主诉:月经期下腹间断疼痛2个月", "现病史:2024.1月经第3天左侧附件区疼痛,超声提示无异常,输消炎药后好转,2024.2无异常,2024.3月经第3天下腹疼痛但是疼痛程度较前减轻,", "既往史:平素体健,无高血压、冠心病、糖尿病病史,无肝炎、结核等传染病史,无手术史", "婚育史:", "月经史:患者平素月经规律,量中等,色正常,无痛经。", "过敏史:无", "专科检查:外阴:发育正常,阴毛呈女性分布;阴道:通畅,粘膜红润,未见异常分泌物;宫颈:光滑,大小正常,宫体:正常大小,无压痛。附件:双侧附件区未触及明显异常。", "辅助检查:", "初步印象:女性盆腔炎性疾病", "处理意见:门诊检查", "备注:", "医师签名:权丽丽", "第1页", ""]
2026-08-05 10:51:05,185 INFO     29 [qwen-vl-parser] page=19 text: 50 lines (bbox 1142-1191)
2026-08-05 10:51:05,185 INFO     29 [qwen-vl-parser] page=19 text: 50 sections
2026-08-05 10:51:05,332 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=986739, prompt_len=764
2026-08-05 10:51:06,717 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 10:51:06,717 INFO     29 [qwen-vl-parser] page=20 classify=text report_date=None
2026-08-05 10:51:06,730 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=986739, prompt_len=401
2026-08-05 10:51:12,732 INFO     29 [qwen-vl-parser] text API response (len=1060):
["三门峡市中心医院门户-患者360 ×", "临床数据中心-患者360视图", "返回患者查询", "患者姓", "出生", "期：2020-07-08", "最近诊疗日期：2026-02-12", "当前在院状态：出院", "过敏：无", "详情>>", "就诊时间抽", "1J号：", "就诊时间：2024-04-08 11:32:46", "接诊科室：妇科门诊", "接诊医生：曲丽霞", "全部", "近一月", "近三月", "近半年", "近一年", "近五年", "门诊诊39", "住院1", "总览", "就诊列表", "2025-04-11 收敛厄重_病区(1)", "2025-01-06 普通儿科三组(...", "2024-12-30 普通儿科三组(...", "2024-07-05 普通儿科一组(...", "2024-04-24 普通儿科一组(...", "2024-04-19 普通儿科一组(...", "2024-04-08 妇科门诊", "2024-04-08 妇科一病区(门)", "2024-01-05 妇科一病区(门)", "2023-08-14 普通儿科三组(...", "2023-07-06 普通儿科三组(...", "集成视图", "诊断", "病历文书", "处方", "检验", "检查", "处置", "肺功能检查", "单机报告", "体检报告", "门诊号", "姓名", "性别：女", "年龄：40岁", "民族：汉族", "身份证号", "现住址：", "就诊类型：初诊", "就诊科室：妇科门诊", "就诊日期：2024-04-08 11:32", "联系电话", "主诉：月经期下腹间断疼痛2个月", "现病史：2024.1月经第3天左侧附件区疼痛，超声提示无异常，输消炎药后好转，2024.2无异常，2024.3月经", "第3天下腹疼痛但是疼痛程度较前减轻，", "既往史：平素体健，无高血压、冠心病、糖尿病病史，无肝炎、结核等传染病史，无手术史", "婚育史：", "月经史：患者平素月经规律，量中等，色正常，无痛经。", "过敏史：无", "专科检查：外阴：发育正常，阴毛呈女性分布；阴道：通畅，粘膜红润，未见异常分泌物；宫颈：光滑，大小", "正常，宫体：正常大小，无压痛。附件：双侧附件区未触及明显异常。", "辅助检查：", "初步印象：女性盆腔炎性疾病", "处理意见：门诊检查", "备注：", "医师签名：", "第1页"]
2026-08-05 10:51:12,733 INFO     29 [qwen-vl-parser] page=20 text: 72 lines (bbox 1192-1263)
2026-08-05 10:51:12,733 INFO     29 [qwen-vl-parser] page=20 text: 72 sections
2026-08-05 10:51:12,860 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=802759, prompt_len=764
2026-08-05 10:51:14,393 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-04-19"}
```
2026-08-05 10:51:14,393 INFO     29 [qwen-vl-parser] page=21 classify=text report_date=2024-04-19
2026-08-05 10:51:14,401 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=802759, prompt_len=401
2026-08-05 10:51:20,035 INFO     29 [qwen-vl-parser] text API response (len=1051):
["<", "→", "C", "① 不安全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView", "临床数据中心-患者360视图", "返回患者查询", "患者姓", "女", "出生日期", "首诊日期：2020-07-08", "最近诊疗日期：2026-02-12", "当前在院状态：出院", "过敏：无", "详情>>", "就诊时间抽", "门诊号", "就诊时间：2024-04-19 08.07.40", "接诊科室：普通儿科一组(门)", "接诊医生：李婉莹", "全部", "近一月", "近三月", "近半年", "近一年", "近五年", "■ 门诊诊39", "住院1", "总览", "就诊列表", "2025-04-11 宁波危重—病区(IJ)", "2025-01-06 普通儿科三组(...", "2024-12-30 普通儿科三组(...", "2024-07-05 普通儿科一组(...", "2024-04-24 普通儿科一组(...", "2024-04-19 普通儿科一组(...", "2024-04-08 妇科门诊", "2024-04-08 妇科一病区(门)", "2024-01-05 妇科一病区(门)", "2023-08-14 普通儿科三组(...", "2023-07-06 普通儿科三组(...", "集成视图", "诊断", "病历文书", "处方", "检验", "检查", "处置", "肺功能检查", "单机报告", "体检报告", "门诊号", "姓", "性别：女", "年龄：40岁", "民族：汉族", "身份证号：", "现住址：", "就诊类型：急诊", "就诊科室：普通儿科一组(门)", "就诊日期：2024-04-19 08:07", "联系电话", "主诉：因呼吸道感染）不适要求开药", "现病史：患者因（呼吸道感染）不适，要求开药（家属代开）。", "既往史：既往体质一般", "过敏史：无", "体格检查：神志清晰，精神一般，自主体位，查体合作", "辅助检查：", "初步印象：1、急性上呼吸道感染.2、维生素A缺乏伴夜盲症", "处理意见：开立药品", "备注：", "医师签名：李婉莹", "第1页", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 10:51:20,036 INFO     29 [qwen-vl-parser] page=21 text: 74 lines (bbox 1264-1337)
2026-08-05 10:51:20,036 INFO     29 [qwen-vl-parser] page=21 text: 74 sections
2026-08-05 10:51:20,177 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=986805, prompt_len=764
2026-08-05 10:51:21,598 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-04-11"}
```
2026-08-05 10:51:21,599 INFO     29 [qwen-vl-parser] page=22 classify=text report_date=2025-04-11
2026-08-05 10:51:21,610 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=986805, prompt_len=401
2026-08-05 10:51:27,399 INFO     29 [qwen-vl-parser] text API response (len=1026):
["临床数据中心-患者360视图", "返回患者查询", "患者姓", "别：女", "出生日期：", "就诊日期：2020-07-08", "最近诊疗日期：2026-02-12", "当前在院状态：出院", "过敏：无", "详情>>", "就诊时间：2025-04-11 14:47:07", "接诊科室：呼吸危重二病区(门)", "接诊医生：段竹云", "全部", "近一月", "近三月", "近半年", "近一年", "近五年", "门诊39", "住院1", "总览", "就诊列表", "2025-06-23 普通儿科三组 (...", "2025-05-09 呼吸危重二病区(门)", "2025-04-11 耳鼻咽喉头颈外...", "2025-04-11 呼吸危重二病区(门)", "2025-01-06 普通儿科三组 (...", "2024-12-30 普通儿科三组 (...", "2024-07-05 普通儿科一组 (...", "2024-04-24 普通儿科一组 (...", "2024-04-19 普通儿科一组 (...", "2024-04-08 妇科门诊", "2024-04-08 妇科一病区(门)", "集成视图", "诊断", "病历文书", "处方", "检验", "检查", "处置", "肺功能检查", "单机报告", "透析治疗", "费用", "体检报告", "（总）诊病历", "门诊号：", "姓", "性别：女", "年龄：41岁", "民族：汉族", "婚姻状况：已婚", "身份证", "职业：专业技术人员", "现住址：", "就诊类型：初诊", "就诊科室：呼吸危重二病区(门)", "就诊日期：2025-04-11", "14:47", "联系电话：", "主诉：咳嗽憋气一周", "现病史：患者无发热，感冒后咳嗽、憋气一周，间断治疗，时轻时重，今日来诊", "既往史：平素体健，无高血压、冠心病、糖尿病病史", "个人史：无吸烟史", "过敏史：无", "体格检查：呼吸平稳，口唇无紫绀，听诊：双肺呼吸音清，未闻及干、湿性啰音", "辅助检查：肺功能检查提示中重度阻塞性肺通气功能障碍，支气管舒张试验阳性。", "初步印象：1、支气管哮喘(急性发作期).2、过敏性鼻炎[变应性鼻炎]", "处理意见：坚持门诊治疗，定期复查", "备注：", "医师签名：段竹云", "第1页"]
2026-08-05 10:51:27,401 INFO     29 [qwen-vl-parser] page=22 text: 73 lines (bbox 1338-1410)
2026-08-05 10:51:27,401 INFO     29 [qwen-vl-parser] page=22 text: 73 sections
2026-08-05 10:51:27,543 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=935536, prompt_len=764
2026-08-05 10:51:29,222 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-04-11"}
```
2026-08-05 10:51:29,222 INFO     29 [qwen-vl-parser] page=23 classify=text report_date=2025-04-11
2026-08-05 10:51:29,240 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=935536, prompt_len=401
2026-08-05 10:51:32,976 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T10:51:32.974+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 10:51:34,811 INFO     29 [qwen-vl-parser] text API response (len=911):
["临床数据中心-患者360视图", "返回患者查询", "就诊时间抽", "近五年", "门诊39 住院1", "就诊列表", "2025-06-23 普通儿科三组 (...", "2025-05-09 呼吸危重二病区(门)", "2025-04-11 耳鼻咽喉头颈外", "2025-04-11 呼吸危重二病区(门)", "2025-01-06 普通儿科三组 (...", "2024-12-30 普通儿科三组 (...", "2024-07-05 普通儿科一组 (...", "2024-04-24 普通儿科一组 (...", "2024-04-19 普通儿科一组 (...", "2024-04-08 妇科门诊", "2024-04-08 妇科一病区(门)", "]: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>", "就诊时间: 2025-04-11 15:43:29 接诊科室: 耳鼻咽喉头颈外科(门) 接诊医生: 刘秀层", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 报告", "门诊病历", "门诊号", "姓名", "性别: 女", "年龄:41岁", "民族: 汉族", "婚姻状况: 已婚", "身份证号", "职业: 职员", "现住址:", "就诊类型: 初诊", "就诊科室:耳鼻咽喉头颈外科", "就诊日期: 2025-04-11 15:43", "联系电", "主诉:鼻塞流涕,咳嗽憋气1周", "现病史:1周前发现鼻塞流涕,患者无发热,感冒后咳嗽、憋气,间断治疗,时轻时重,今日来诊", "既往史:平素体健,无高血压、冠心病、糖尿病病史", "家族史:无家族遗传病史", "过敏史:无", "体格检查:鼻腔粘膜充血,水肿,水样分泌物附着", "辅助检查:肺功能检查提示中重度阻塞性肺通气功能障碍,支气管舒张试验阳性。", "初步印象:1、支气管哮喘(急性发作期)2、过敏性鼻炎[变应性鼻炎]", "处理意见:坚持门诊治疗,定期复查", "备注:", "医师签名:刘秀层", "第1页"]
2026-08-05 10:51:34,811 INFO     29 [qwen-vl-parser] page=23 text: 46 lines (bbox 1411-1456)
2026-08-05 10:51:34,811 INFO     29 [qwen-vl-parser] page=23 text: 46 sections
2026-08-05 10:51:34,953 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=969703, prompt_len=764
2026-08-05 10:51:36,471 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-05-09"}
```
2026-08-05 10:51:36,472 INFO     29 [qwen-vl-parser] page=24 classify=text report_date=2025-05-09
2026-08-05 10:51:36,488 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=969703, prompt_len=401
2026-08-05 10:51:42,728 INFO     29 [qwen-vl-parser] text API response (len=1061):
["三门峡市中心医院门户-患者360 ×", "+", "← → C ① 不安全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView", "临床数据中心-患者360视图", "返回患者查询 患者姓名 : 女 出生日期", "日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>", "就诊时间抽 门诊号", "就诊时间: 2025-05-09 17 00 57 接诊科室: 呼吸危重二病区(门) 接诊医生: 段竹云", "全部 近一月 近三月 近半年 近一年", "近五年", "■ 门急诊39 住院1", "总览 就诊列表", "2025-11-27 普通儿科二区(...", "2025-11-24 普通儿科二区(...", "2025-09-18 普通儿科二区(...", "2025-07-11 普通儿科一组(...", "2025-06-23 普通儿科三组(...", "2025-05-09 呼吸危重二病区(门)", "2025-04-11 耳鼻咽喉头颈外...", "2025-04-11 呼吸危重二病区(门)", "2025-01-06 普通儿科三组(...", "2024-12-30 普通儿科三组(...", "2024-07-05 普通儿科一组(...", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 体检报告", "门诊号:", "11(急)诊病历", "性别:女 年龄:41岁 民族:汉族", "婚姻状况:已婚 身份证 业:专业技术人员", "现住址:", "就诊类型:复诊", "就诊科室:呼吸危重二病区(门) 就诊日期:2025-05-09 17:00 联系电", "主诉:咳嗽憋气一周", "现病史:患者无发热,感冒后咳嗽、憋气一周,间断治疗,时轻时重,今日来诊", "既往史:平素体健,无高血压、冠心病、糖尿病病史", "个人史:无吸烟史", "过敏史:无", "体格检查:听诊:双肺呼吸音清,未闻及干、湿性啰音", "辅助检查:肺功能检查提示中重度阻塞性肺通气功能障碍,支气管舒张试验阳性。", "初步印象:1、支气管哮喘.2、过敏性鼻炎[变应性鼻炎]", "处理意见:坚持门诊治疗,定期复查", "备注:", "医师签名:段竹云", "第1页", ""]
2026-08-05 10:51:42,728 INFO     29 [qwen-vl-parser] page=24 text: 42 lines (bbox 1457-1498)
2026-08-05 10:51:42,728 INFO     29 [qwen-vl-parser] page=24 text: 42 sections
2026-08-05 10:51:42,846 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=735011, prompt_len=764
2026-08-05 10:51:44,351 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-06-23"}
```
2026-08-05 10:51:44,351 INFO     29 [qwen-vl-parser] page=25 classify=text report_date=2025-06-23
2026-08-05 10:51:44,365 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=735011, prompt_len=401
2026-08-05 10:51:50,609 INFO     29 [qwen-vl-parser] text API response (len=1071):
["三门峡市中心医院门户-惠睿360 ×", "← → ① 不安全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView", "临床数据中心-患者360视图", "返回患者查询 患者姓名:", "出生日期:", "日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>", "就诊时间轴", "门诊号:", "就诊时间: 2025-06-23 10:49:50 接诊科室: 普通儿科三组(门) 接诊医生: 谭真真", "全部 近一月 近三月 近半年 近一年", "近五年", "门诊39 住院1", "总览 就诊列表", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 体检报告", "2025-11-27 普通儿科二区(...", "2025-11-24 普通儿科二区(...", "2025-09-18 普通儿科二区(...", "2025-07-11 普通儿科一组(...", "2025-06-23 普通儿科三组(...", "2025-05-09 呼吸危重二病区(门)", "2025-04-11 耳鼻咽喉头颈外...", "2025-04-11 呼吸危重二病区(门)", "2025-01-06 普通儿科三组(...", "2024-12-30 普通儿科三组(...", "2024-07-05 普通儿科一组(...", "门诊号:", "姓名", "性别: 女", "年龄:41岁", "民族: 汉族", "婚姻状况: 小组", "身份证号:", "职业: 专业技术人员", "现住址:", "就诊类型:初诊", "就诊科室:普通儿科三组(门)", "就诊日期: 2025-06-23 10:49", "联系电话", "主诉: 呼吸道感染购药", "现病史: 呼吸道感染购药", "既往史: 平素体健, 无肝炎、结核类传染病史", "过敏史: 无", "体格检查: 发育正常, 营养良好, 精神一般, 口唇红润, 双侧扁桃体无肿大, 无充血、分泌物。咽腔黏膜有充", "血, 无红肿、疱疹, 双肺呼吸音清, 听诊心律齐, 无杂音, 腹平软, 无压痛、反跳痛", "辅助检查:", "初步印象: 上呼吸道感染", "处理意见: 门诊药物治疗", "备注:", "医师签名: 谭真真", "第1页"]
2026-08-05 10:51:50,609 INFO     29 [qwen-vl-parser] page=25 text: 50 lines (bbox 1499-1548)
2026-08-05 10:51:50,609 INFO     29 [qwen-vl-parser] page=25 text: 50 sections
2026-08-05 10:51:50,750 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=881541, prompt_len=764
2026-08-05 10:51:52,081 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 10:51:52,081 INFO     29 [qwen-vl-parser] page=26 classify=text report_date=None
2026-08-05 10:51:52,095 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=881541, prompt_len=401
2026-08-05 10:51:58,168 INFO     29 [qwen-vl-parser] text API response (len=1050):
["<->C ① 不安全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView", "临床数据中心-患者360视图", "返回患者查询 患者姓 出生日期", "就诊日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>", "就诊时间始 门诊号", "就诊时间: 2025-07-11 10:02:50 接诊科室: 普通儿科一组(门) 接诊医生: 赵艳", "全部 近一月 近三月 近半年 近一年", "近五年", "■ 门急诊39 住院1", "总览 就诊列表", "2025-11-27 普通儿科二区(...", "2025-11-24 普通儿科二区(...", "2025-09-18 普通儿科二区(...", "2025-07-11 普通儿科一组(...", "2025-06-23 普通儿科三组(...", "2025-05-09 呼吸危重二病区(门)", "2025-04-11 耳鼻咽喉头颈外...", "2025-04-11 呼吸危重二病区(门)", "2025-01-06 普通儿科三组(...", "2024-12-30 普通儿科三组(...", "2024-07-05 普通儿科一组(...", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 体检报告", "门诊号", "1. 病历", "姓名", "性别: 女", "年龄:41岁", "民族: 汉族", "婚姻状况: 未婚", "身份证", "职业: 专业技术人员", "现住址:", "就诊类型:初诊", "就诊科室:普通儿科一组(门)", "就诊日期: 2025-07-11 10:02", "联系电话", "主诉:呼吸道感染购药", "现病史:呼吸道感染购药", "既往史:平素体健,无肝炎、结核类传染病史", "过敏史:无", "体格检查:发育正常,营养良好,精神一般,口唇红润,双侧扁桃体无肿大,无充血、分泌物。咽腔黏膜无充血、红肿、疱疹,双肺呼吸音清,听诊心律齐,无杂音,腹平软,无压痛、反跳痛", "辅助检查:", "初步印象:支气管炎", "处理意见:门诊药物治疗", "备注:", "医师签名:赵艳", "第1页", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 10:51:58,168 INFO     29 [qwen-vl-parser] page=26 text: 49 lines (bbox 1549-1597)
2026-08-05 10:51:58,168 INFO     29 [qwen-vl-parser] page=26 text: 49 sections
2026-08-05 10:51:58,332 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=992751, prompt_len=764
2026-08-05 10:51:59,822 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-09-18"}
```
2026-08-05 10:51:59,823 INFO     29 [qwen-vl-parser] page=27 classify=text report_date=2025-09-18
2026-08-05 10:51:59,850 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=992751, prompt_len=401
2026-08-05 10:52:03,006 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T10:52:03.005+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 10:52:06,253 INFO     29 [qwen-vl-parser] text API response (len=1059):
["临床数据中心-患者360视图", "返回患者查询", "患者姓名:", "：女 出生日期:", "首诊日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>", "就诊时间抽", "门诊号:", "就诊时间: 2025-09-18 15:22:06 接诊科室: 普通儿科二区(门) 接诊医生: 赵艳", "全部", "近一月", "近三月", "近半年", "近一年", "近五年", "门诊39 住院1", "总览", "就诊列表", "2025-12-09 普通儿科二区(...", "2025-12-07 普通儿科二区(...", "2025-12-01 普通儿科二区(...", "2025-11-27 普通儿科二区(...", "2025-11-24 普通儿科二区(...", "2025-09-18 普通儿科二区(...", "2025-07-11 普通儿科一组(...", "2025-06-23 普通儿科三组(...", "2025-05-09 呼吸危重二病区(门)", "2025-04-11 耳鼻咽喉头颈外...", "2025-04-11 呼吸危重二病区(门)", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 请价治疗 费用 体检报告", "门诊病历", "门诊", "姓名:", "性别: 女", "年龄:41岁", "民族: 汉族", "婚姻状况: 未婚", "身份证", "职业: 职员", "现住址:", "就诊类型:初诊", "就诊科室:普通儿科二区(门)", "就诊日期: 2025-09-18 15:22", "联系电话", "主诉:咽部疼痛伴眼部不适4天", "现病史:4天前无明显诱因出现咽部疼痛,伴鼻塞,伴眼部不适,无发热、呕吐、腹泻、皮疹等不适,病后精神、食欲欠佳,大小便正常。", "既往史:无特殊。", "过敏史:无", "体格检查:发育正常,营养良好,精神一般,呼吸平稳,双眼睑结膜充血,口唇红润,咽腔充血,无疱疹,双侧扁桃体I°,充血,无分泌物,双肺呼吸音清,未闻及干湿性啰音,听诊心律齐,无杂音,腹平软,无压痛、反跳痛,未触及包块,肠鸣音活跃,神经系统未见阳性体征。", "辅助检查:无", "初步印象:1.急性咽峡炎.2.急性变应性结膜炎", "处理意见:门诊治疗,动态观察病情变化,不适及时随诊。", "备注:", "医师签名:赵艳", "第1页", "Le coo"]
2026-08-05 10:52:06,253 INFO     29 [qwen-vl-parser] page=27 text: 55 lines (bbox 1598-1652)
2026-08-05 10:52:06,253 INFO     29 [qwen-vl-parser] page=27 text: 55 sections
2026-08-05 10:52:06,386 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=923208, prompt_len=764
2026-08-05 10:52:08,704 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-12-01"}
```
2026-08-05 10:52:08,704 INFO     29 [qwen-vl-parser] page=28 classify=text report_date=2025-12-01
2026-08-05 10:52:08,715 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=923208, prompt_len=401
2026-08-05 10:52:15,018 INFO     29 [qwen-vl-parser] text API response (len=1124):
["全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView", "临床数据中心", "0视图", "返回患者查询", "患者", "女 出生F", "就诊日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>", "就诊时间轴", "门诊", "诊时间: 2025-12-01 15:28:03 接诊科室: 普通儿科二区(门) 接诊医生: 赵海国", "全季", "近一月", "近三月", "近半年", "近一年", "近五年", "门诊急诊39 住院1", "总览", "就诊列表", "集成视图", "诊断", "病历文书", "处方", "检验", "检查", "处置", "肺功能检查", "单机报告", "透析治疗", "费用", "体检报告", "门诊", "1.1、心/诊病历", "门诊", "2026-01-15 呼吸危重二病区(门)", "2026-01-06 妇科一病区(门)", "2025-12-09 普通儿科二区(...", "2025-12-07 普通儿科二区(...", "2025-12-01 普通儿科二区(...", "2025-11-27 普通儿科二区(...", "2025-11-24 普通儿科二区(...", "2025-09-18 普通儿科二区(...", "2025-07-11 普通儿科一组(...", "2025-06-23 普通儿科三组(...", "2025-05-09 呼吸危重二病区(门)", "姓名:", "性别: 女", "年龄:41岁", "民族: 汉族", "婚姻状况: 未...", "身份证:", "职业: 专业技术人员", "现住址:", "就诊类型:初诊", "就诊科室:普通儿科二区(门)", "就诊日期: 2025-12-01 15:28", "联系电", "主诉: 发热半天。", "现病史: 半天前出现发热,最高体温38.0℃,口服药物治疗1次,无咳嗽,无喘息,无呼吸困难,无咯血,无腹泻、呕吐等。精神食欲一般,大小便正常。", "既往史: 无。", "过敏史: 无", "体格检查: 神志清,精神一般,呼吸浅快,咽充血,扁桃体二度大,充血,无疱疹,无脓点,双肺呼吸音清,", "心音有力,律齐,腹软。", "辅助检查:", "初步印象: 急性上呼吸道感染", "处理意见: 口服药物,动态观察,不适随诊。", "备注:", "医师签名: 赵海国", "第1页"]
2026-08-05 10:52:15,018 INFO     29 [qwen-vl-parser] page=28 text: 69 lines (bbox 1653-1721)
2026-08-05 10:52:15,018 INFO     29 [qwen-vl-parser] page=28 text: 69 sections
2026-08-05 10:52:15,281 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2164311, prompt_len=764
2026-08-05 10:52:16,783 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-05 10:52:16,784 INFO     29 [qwen-vl-parser] page=29 classify=text report_date=None
2026-08-05 10:52:16,798 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2164311, prompt_len=401
2026-08-05 10:52:25,482 INFO     29 [qwen-vl-parser] text API response (len=1489):
["姓名：", "性别：女", "年龄：41岁", "民族：汉族", "婚姻状况：已婚", "身份证号", "职业：专业技术人员", "现住址", "就诊类型：初诊", "就诊科室：妇科一病区(门)", "就诊日期：2026-01-06 08:36", "联系电话.", "主诉：左下腹间断疼痛1年左右来诊", "现病史：患者诉于2024年01月05日无明显诱因出现下腹持续疼痛行相关检查后诊断为盆腔炎性疾病后遗症，", "慢性盆腔痛，药物治疗后好转，慢性盆腔痛病程12月，目前疾病状态持续，未治疗。", "既往史：2025年11月24日-2025年12月12日本院儿科门诊就诊代家属开药，否认3个月内其他病史及合并用药/", "非药物治疗，现患者无盆腔炎性疾病急性发作，否认既往有子宫肌瘤、子宫内膜异位症、子宫腺肌病、结核性", "盆腔炎、间质性膀胱炎、异常子宫出血、盆腔淤血综合征、子宫颈高级别上皮内病变等其他病症引起相关症状", "者；未放置宫内节育器；无子宫及双侧附件缺如；近2周内未使用过本方案规定研究期间禁止使用的治疗（包括", "药物和非药物治疗）；无控制不稳定的心血管、肝、肾和血液系统、糖尿病、甲状腺疾病等严重原发性疾病；", "获得知情同意书前5年内未患有恶性肿瘤；否认对试验用药品过敏，包括对本品成分或者药物辅料有过敏史；否", "认长期酗酒、药物滥用史；无智力障碍或精神障碍；近1个月内未参加过任何干预性临床试验；患者当前不在妊", "娠期、哺乳期，同意在试验期间及试验结束后3个月内采取有效避孕措施。", "婚育史：已婚已育，孕2产2，有性生活史", "手术史：2016年8月31日、2020年7月9日因生产行剖宫产手术", "月经史：初潮12岁，既往月经周期规律，经量中，色红，无痛经，末次月经2025.12.29-2025.1.2，周期26-", "28天，经期5天，经量较前不变", "过敏史：无", "生命体征：2026.1.6测量身高：160.0cm 体重：51.0kg 体温：36.4℃ 脉搏：76次/分 呼吸：18次/分 血压：", "98/76mmHg", "体格检查：淋巴结、头颈部、胸部、脊柱/四肢/关节、神经系统未见异常，腹部异常（左下腹压痛，CS，研究", "疾病相关），皮肤黏膜异常（腹部皮肤约5-6cm剖宫产手术瘢痕，NCS），其他未查。", "专科检查：外阴已婚型，阴道畅，宫颈光滑，无摇举痛，有宫体压痛，无子宫活动受限或粘连固定，左侧附件", "区、右侧附件区压痛，无宫骶韧带增粗、变硬、触痛。", "辅助检查：今日按方案要求开具血常规、尿沉渣（含尿常规）、肝功八项、肾功两项、血妊娠、血沉、血清C&-", "125、妇科微生态、十二导联心电图、妇科阴道彩色B超检查，结果详见检查单。", "初步印象：盆腔痛中医辨证：主症：下腹胀痛，腰骶部胀痛、带下量多；次症：神疲乏力、口苦口腻、小便", "黄；舌象：舌质红、苔黄腻；脉象：脉弦滑；2026年01月06日由张丹丹医生辨证为湿热瘀阻症。 西医：盆腔炎", "性疾病后遗症，慢性盆腔痛", "处理意见：根据目前临床表现及患者情况，权丽丽医生于2026年01月06日08时38分在9号楼4楼医患沟通室向患", "绍“妇科千金片治疗盆腔炎性疾病后遗症（湿热瘀阻证）的随机、双盲、安慰剂平行对照、多中心临", "床试验”及知情同意书内容，已告知参加试验可能的风险与获益，患者已充分理解并同意参加该研究，未提出", "门", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 10:52:25,482 INFO     29 [qwen-vl-parser] page=29 text: 45 lines (bbox 1722-1766)
2026-08-05 10:52:25,483 INFO     29 [qwen-vl-parser] page=29 text: 45 sections
2026-08-05 10:52:25,788 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2496910, prompt_len=764
2026-08-05 10:52:27,397 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-05 10:52:27,398 INFO     29 [qwen-vl-parser] page=30 classify=text report_date=None
2026-08-05 10:52:27,410 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2496910, prompt_len=401
2026-08-05 10:52:33,040 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T10:52:33.039+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 10:52:37,188 INFO     29 [qwen-vl-parser] text API response (len=1669):
["既往史：2025年11月24日-2025年12月12日本院儿科门诊就诊代家属开药，否认3个月内其他病史及合并用药/", "非药物治疗，现患者无盆腔炎性疾病急性发作，否认既往有子宫肌瘤、子宫内膜异位症、子宫腺肌病、结核性", "盆腔炎、间质性膀胱炎、异常子宫出血、盆腔淤血综合征、子宫颈高级别上皮内病变等其他病症引起相关症状", "者；未放置宫内节育器；无子宫及双侧附件缺如；近2周内未使用过本方案规定研究期间禁止使用的治疗（包括", "药物和非药物治疗）；无控制不稳定的心血管、肝、肾和血液系统、糖尿病、甲状腺疾病等严重原发性疾病；", "获得知情同意书前5年内未患有恶性肿瘤；否认对试验用药品过敏，包括对本品成分或者药物辅料有过敏史；否", "认长期酗酒、药物滥用史；无智力障碍或精神障碍；近1个月内未参加过任何干预性临床试验；患者当前不在妊", "娠期、哺乳期，同意在试验期间及试验结束后3个月内采取有效避孕措施。", "婚育史：已婚已育，孕2产2，有性生活史", "手术史：2016年8月31日、2020年7月9日因生产行剖宫产手术", "月经史：初潮12岁，既往月经周期规律，经量中，色红，无痛经，末次月经2025.12.29-2025.1.2，周期26-", "28天，经期5天，经量较前不变", "过敏史：无", "生命体征：2026.1.6测量身高：160.0cm 体重：51.0kg 体温：36.4℃ 脉搏：76次/分 呼吸：18次/分 血压：", "98/76mmHg", "体格检查：淋巴结、头颈部、胸部、脊柱/四肢/关节、神经系统未见异常，腹部异常（左下腹压痛，CS，研究", "疾病相关），皮肤黏膜异常（腹部皮肤约5-6cm剖宫产手术瘢痕，NCS），其他未查。", "专科检查：外阴已婚型，阴道畅，宫颈光滑，无摇举痛，有宫体压痛，无子宫活动受限或粘连固定，左侧附件", "区、右侧附件区压痛，无宫骶韧带增粗、变硬、触痛。", "辅助检查：今日按方案要求开具血常规、尿沉渣（含尿常规）、肝功八项、肾功两项、血妊娠、血沉、血清CA-", "125、妇科微生态、十二导联心电图、妇科阴道彩色B超检查，结果详见检查单。", "初步印象：盆腔痛中医辨证：主症：下腹胀痛，腰骶部胀痛、带下量多；次症：神疲乏力、口苦口腻、小便", "黄；舌象：舌质红、苔黄腻；脉象：脉弦滑；2026年01月06日由张丹丹医生辨证为湿热瘀阻症。 西医：盆腔炎", "性疾病后遗症，慢性盆腔痛", "从细之间、根据目前临床表现及患者情况，权丽丽医生于2026年01月06日08时38分在9号楼4楼医患沟通室向患", "者", "引“妇科千金片治疗盆腔炎性疾病后遗症（湿热瘀阻证）的随机、双盲、安慰剂平行对照、多中心临", "床试验”及知情同意书内容，已告知参加试验可能的风险与获益，患者已充分理解并同意参加该研究，未提出", "问题，患者本人于2026年01月06日08时58分签署知情同意书（版本号：V1.0 三门峡市中心医院专用版，版本日", "期：2025年08月05日），权丽丽医生于2026年01月06日08时59分签署知情同意书（版本号：V1.0 三门峡市中心", "医院专用版，版本日期：2025年08月05日），知情同意书原件一份保存于受试者文件夹，一份交给患者本人，", "确定患者筛选号为04011，进入试验筛选，根据方案要求，收集受试者的试验相关资料，并于今日开始进行筛选", "期相关检查。", "1.已完成体征McCormack量表评分，总分8分，回顾近1周非经期腹痛/腰骶疼痛NRS平均分为5分。", "2.嘱受试者合理饮食，避免过度劳累；避免盆浴和坐浴，避免穿紧身衣物和化纤内裤；注意经期卫生。", "3.今日结合受试者情况，2026年1月6日血清CA-125示：59.70（0.00-35.00）U/mL，符合排除标准第（8）条，", "筛选失败，告知受试者转为门诊常规诊疗。", "备注：", "医师签名："]
2026-08-05 10:52:37,189 INFO     29 [qwen-vl-parser] page=30 text: 39 lines (bbox 1767-1805)
2026-08-05 10:52:37,189 INFO     29 [qwen-vl-parser] page=30 text: 39 sections
2026-08-05 10:52:37,332 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=937019, prompt_len=764
2026-08-05 10:52:38,856 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 10:52:38,856 INFO     29 [qwen-vl-parser] page=31 classify=text report_date=None
2026-08-05 10:52:38,871 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=937019, prompt_len=401
2026-08-05 10:52:44,517 INFO     29 [qwen-vl-parser] text API response (len=996):
["临床数据中心-患者360视图", "返回患者查询", "患者", "日期：2020-07-08", "最近诊疗日期：2026-02-12", "当前在院状态：出院", "过敏：无", "详情>>", "就诊时间轴", "门诊号", "时间：2026-01-15 10:56:28", "接诊科室：呼吸危重三病区(门)", "接诊医生：王辉", "全部", "近一月", "近三月", "近半年", "近一年", "近五年", "门诊39-住院1", "就诊列表", "总览", "2026-02-12 呼吸危重三病区(门)", "2026-01-15 呼吸危重三病区(门)", "2026-01-06 妇科一病区(门)", "2025-12-09 普通儿科二区 (...", "2025-12-07 普通儿科二区 (...", "2025-12-01 普通儿科二区 (...", "2025-11-27 普通儿科二区 (...", "2025-11-24 普通儿科二区 (...", "2025-09-18 普通儿科二区 (...", "2025-07-11 普通儿科一组 (...", "2025-06-23 普通儿科三组 (...", "集成视图", "诊断", "病历文书", "处方", "检验", "检查", "处置", "肺功能检查", "单机报告", "透析治疗", "费用", "体检报告", "门诊", "姓名", "性别：女", "年龄：41岁", "民族：汉族", "婚姻状况：已婚", "身份证号", "职业：其他", "现住址", "就诊类型：复诊", "就诊科室：呼吸危重三病区(门)", "就诊日期：2026-01-15", "10:56", "联系电话", "主诉：咳嗽憋气一周", "现病史：患者无发热，感冒后咳嗽、憋气一周，间断治疗，时轻时重，今日来诊", "既往史：平素体健，无高血压、冠心病、糖尿病病史", "个人史：无吸烟史", "过敏史：无", "体格检查：听诊：双肺呼吸音清，未闻及干、湿性啰音", "辅助检查：肺功能检查提示中重度阻塞性肺通气功能障碍，支气管舒张试验阳性。", "初步印象：1、支气管哮喘(急性发作期).2、过敏性鼻炎[变应性鼻炎]", "处理意见：坚持门诊治疗，定期复查", "备注", "医师签名：王辉", "第1页"]
2026-08-05 10:52:44,517 INFO     29 [qwen-vl-parser] page=31 text: 71 lines (bbox 1806-1876)
2026-08-05 10:52:44,517 INFO     29 [qwen-vl-parser] page=31 text: 71 sections
2026-08-05 10:52:44,641 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=797442, prompt_len=764
2026-08-05 10:52:45,982 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 10:52:45,983 INFO     29 [qwen-vl-parser] page=32 classify=text report_date=None
2026-08-05 10:52:45,998 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=797442, prompt_len=401
2026-08-05 10:52:53,436 INFO     29 [qwen-vl-parser] text API response (len=1091):
["984-04-02 首诊日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>", "返回概览视图", "门诊号: 2", "时间: 2026-02-12 11.40.02 接诊科室: 呼吸危重三病区(门) 接诊医生: 孙帅森", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告", "请输入药品内容,按回车键检索", "查询全部", "类型 组 药品名称[规格] 用法 频率 实际用量 总量 开立时间 开立医师", "药品 (320ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 320ug 1 2026-02-25 07:47:00 赵海国", "药品 鼻渊通窍颗粒 口服 tid 1袋 3 2026-02-12 09:40:21 谭真真", "药品 阿莫西林克拉维酸钾片(选) 口服(继续用药) tid 0.375g 24 2026-02-12 09:40:21 谭真真", "药品 (160ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 160ug 1 2026-01-17 08:04:36 彭文娟", "药品 (320ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 320ug 1 2026-01-17 08:04:36 彭文娟", "药品 磷酸奥司他韦胶囊(东阳光) 口服 bid 75mg 10 2025-12-07 10:50:33 彭文娟", "药品 鼻渊通窍颗粒 口服 bid 1袋 2 2025-11-27 15:02:43 烟海丽", "药品 盐酸氮卓斯丁滴眼液 滴眼 qid 0.01ml 1 2025-09-18 15:29:34 赵艳", "药品 阿莫西林克拉维酸钾片(选) 口服(继续用药) tid 0.375g 24 2025-09-18 15:25:48 赵艳", "药品 (成人)双黄连口服液(选) 口服 tid 20ml 2 2025-09-18 15:25:48 赵艳", "药品 (160ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 160ug 1 2025-07-11 10:07:36 赵艳", "药品 (小儿)双黄连口服液(选) 口服 tid 20ml 2 2025-06-23 10:52:35 谭真真", "药品 (倾尔宁片)孟鲁司特钠片(选) 口服 qn 10mg 30 2025-05-09 17:04:48 段竹云", "共70页 2026-02-12 1 2 3 4 > 前往 1 页"]
2026-08-05 10:52:53,436 INFO     29 [qwen-vl-parser] page=32 text: 22 lines (bbox 1877-1898)
2026-08-05 10:52:53,436 INFO     29 [qwen-vl-parser] page=32 text: 22 sections
2026-08-05 10:52:53,590 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1002302, prompt_len=764
2026-08-05 10:52:55,074 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 10:52:55,075 INFO     29 [qwen-vl-parser] page=33 classify=text report_date=None
2026-08-05 10:52:55,087 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1002302, prompt_len=401
2026-08-05 10:53:02,790 INFO     29 [qwen-vl-parser] text API response (len=1176):
["50/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView", "984-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>", "时间：2026-02-12 11:40.02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森", "返回概览视图", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告", "请输入药品内容，按回车键检索", "查询全部", "类型 组 药品名称(规格) 用法 频率 实际用量 总量 开立时间 开立医师", "药品 鼻渊通窍颗粒 口服 bid 1袋 2 2025-11-27 15:02.43 烟海丽", "药品 盐酸氮卓斯丁滴眼液 滴眼 qid 0.01ml 1 2025-09-18 15:29.34 赵艳", "药品 阿莫西林克拉维酸钾片(选) 口服(继续用药) tid 0.375g 24 2025-09-18 15:25.48 赵艳", "药品 (成人)双黄连口服液(选) 口服 tid 20ml 2 2025-09-18 15:25.48 赵艳", "药品 (160ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 160ug 1 2025-07-11 10:07.36 赵艳", "药品 (小儿)双黄连口服液(选) 口服 tid 20ml 2 2025-06-23 10:52.35 谭真真", "药品 (顺尔宁片)孟鲁司特钠片(选) 口服 qn 10mg 30 2025-05-09 17:04.48 段竹云", "药品 (320ug)布地奈德福莫特罗粉吸入剂 吸入 bid 320ug 2 2025-05-09 17:04.48 段竹云", "药品 醋酸泼尼松片 口服 qm 30mg 36 2025-04-11 15:46.53 刘秀层", "药品 鼻炎康莫米松鼻喷雾剂(选) 喷鼻 bid 100ug 1 2025-04-11 15:31.05 段竹云", "药品 (顺尔宁片)孟鲁司特钠片(选) 口服 qn 10mg 5 2025-04-11 15:31.05 段竹云", "药品 (320ug)布地奈德福莫特罗粉吸入剂 吸入 bid 320ug 1 2025-04-11 15:31.05 段竹云", "药品 磷酸奥司他韦胶囊(东阳光) 口服 bid 75mg 10 2025-01-06 17:15.28 谭真真", "药品 氯雷他定颗粒 口服 qd 10mg 1 2024-12-30 10:40:10 谭真真", "共70条 20条/页 < 1 2 3 4 > 前往 1", ""]
2026-08-05 10:53:02,790 INFO     29 [qwen-vl-parser] page=33 text: 23 lines (bbox 1899-1921)
2026-08-05 10:53:02,790 INFO     29 [qwen-vl-parser] page=33 text: 23 sections
2026-08-05 10:53:02,934 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=859617, prompt_len=764
2026-08-05 10:53:03,066 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T10:53:03.065+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 10:53:04,265 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 10:53:04,265 INFO     29 [qwen-vl-parser] page=34 classify=text report_date=None
2026-08-05 10:53:04,275 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=859617, prompt_len=401
2026-08-05 10:53:11,238 INFO     29 [qwen-vl-parser] text API response (len=1080):
["/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView", "84-04-02", "最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>", "返回概览视图", "门诊时间: 2026-02-12 11:40:02 接诊科室: 呼吸危重三病区(门) 接诊医生: 孙帅森", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告", "请输入药品内容, 按回车键检索", "查询全部", "类型 组 药品名称[规格] 用法 频率 实际用量 总量 开立时间 开立医师", "药品 (大伊可新)维生素AD滴剂 口服 qd 2000u 3 2024-07-05 09:30:58 李婉莹", "药品 (普米克令舒)吸入用布地奈德混悬液 压缩雾化吸入 tid 2ml 20 2024-07-05 09:30:58 李婉莹", "药品 小儿豉翘清热颗粒 口服 tid 6g 3 2024-04-24 11:59:55 赵艳", "药品 (成人)双黄连口服液(基选) 口服 tid 20ml 3 2024-04-19 08:14:06 李婉莹", "药品 (强力)阿莫西林克拉维酸钾干混悬剂(选) 口服(继续用药) bid 0.457g 2 2024-04-19 08:14:06 李婉莹", "药品 (大伊可新)维生素AD滴剂 口服 qd 2000u 3 2024-04-19 08:14:06 李婉莹", "药品 (普米克令舒)吸入用布地奈德混悬液 压缩雾化吸入 tid 2ml 20 2024-04-19 08:14:06 李婉莹", "药品 替硝唑氯化钠注射液 静滴 qd 200ml 6 2024-01-05 10:37:47 程会芳", "药品 左氧氟沙星氯化钠注射液(选) 静滴 qd 0.5g 3 2024-01-05 10:37:47 程会芳", "药品 蒲地蓝消炎口服液 口服 tid 10ml 2 2023-08-14 15:30:23 谭真真", "药品 (盖克)小儿氨酚黄那敏颗粒 口服 tid 12g 2 2023-07-06 20:00:14 谭真真", "药品 蒲地蓝消炎口服液 口服 tid 10ml 2 2023-07-06 20:00:14 谭真真", "共70条 20条/页 < 1 2 3 4 > 前往 2 页", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 10:53:11,238 INFO     29 [qwen-vl-parser] page=34 text: 24 lines (bbox 1922-1945)
2026-08-05 10:53:11,238 INFO     29 [qwen-vl-parser] page=34 text: 24 sections
2026-08-05 10:53:11,988 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3967233, prompt_len=764
2026-08-05 10:53:13,586 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 10:53:13,587 INFO     29 [qwen-vl-parser] page=35 classify=text report_date=None
2026-08-05 10:53:13,610 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3967233, prompt_len=401
2026-08-05 10:53:21,144 INFO     29 [qwen-vl-parser] text API response (len=1155):
["50/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView", "984-04-02 首诊日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>", "返回概览视图", "门诊", "2026-02-12 11:40:02 接诊科室: 呼吸危重三病区(门) 接诊医生: 孙帅森", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告", "请输入药品内容,按回车键检索", "查询全部", "类型 组 药品名称[规格]", "药品 替硝唑氯化钠注射液", "药品 左氧氟沙星氯化钠注射液(选)", "药品 蒲地蓝消炎口服液", "药品 (盖克)小儿氨酚黄那敏颗粒", "药品 蒲地蓝消炎口服液", "药品 (小儿)双黄连口服液(选)", "药品 地塞米松磷酸钠注射液(选)", "药品 5ml灭菌注射用水", "药品 (扑尔敏针)马来酸氯苯那敏注射液", "药品 消旋山莨菪碱注射液", "药品 头孢克肟颗粒(选)", "药品 (天晴速畅)吸入用布地奈德混悬液(选)", "药品 (大伊可新)维生素AD滴剂", "用法 频率 实际用量 总量 开立时间 开立医师", "入", "静滴 qd 200ml 6 2024-01-05 10:37:47 程会芳", "静滴 qd 0.5g 3 2024-01-05 10:37:47 程会芳", "口服 tid 10ml 2 2023-08-14 15:30:23 谭真真", "口服 tid 12g 2 2023-07-06 20:00:14 谭真真", "口服 tid 10ml 2 2023-07-06 20:00:14 谭真真", "口服 tid 20ml 2 2023-07-06 20:00:14 谭真真", "外用 bid 10mg 2 2023-06-26 15:19:59 谭真真", "外用 bid 5ml 4 2023-06-26 15:19:59 谭真真", "外用 bid 20mg 2 2023-06-26 15:19:59 谭真真", "外用 bid 20mg 2 2023-06-26 15:19:59 谭真真", "口服 bid 100mg 30 2023-05-08 19:56:47 陈音", "压缩雾化吸入 bid 2ml 10 2023-05-08 19:52:42 段艳霞", "口服 qd 2000u 2 2023-05-08 19:52:42 段艳霞", "共70条 20条/页 < 1 2 3 4 > 前往: 2 页", ""]
2026-08-05 10:53:21,145 INFO     29 [qwen-vl-parser] page=35 text: 38 lines (bbox 1946-1983)
2026-08-05 10:53:21,145 INFO     29 [qwen-vl-parser] page=35 text: 38 sections
2026-08-05 10:53:21,293 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=900365, prompt_len=764
2026-08-05 10:53:22,762 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 10:53:22,762 INFO     29 [qwen-vl-parser] page=36 classify=text report_date=None
2026-08-05 10:53:22,772 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=900365, prompt_len=401
2026-08-05 10:53:29,933 INFO     29 [qwen-vl-parser] text API response (len=1073):
["返回概览视图", "11.40.02 接诊科室: 呼吸危重三病区(门) 接诊医生: 孙帅森", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告", "请输入药品内容,按回车键检索", "查询全部", "类型 组 药品名称|规格 用法 频率 实际用量 总量 开立时间 开立医师", "药品 *乙2)(大伊可新)维生素AD滴剂 口服 qd 2000u 2 2023-04-07 16:29.03 陈音", "药品 乙1)头孢克肟颗粒(选) 口服 bid 100mg 30 2023-04-07 16:28.02 陈音", "药品 乙0)阿奇霉素干混悬剂 口服 qd 0.25g 1 2023-04-07 16:27:17 陈音", "药品 乙2)三拗片 口服 tid 2片 1 2023-04-07 16:27:17 陈音", "药品 乙0)富马酸酮替芬片 口服 bid 1mg 6 2023-04-07 16:27:17 陈音", "药品 蒲地蓝消炎口服液 口服 tid 10ml 2 2022-08-08 15:40.53 王晶", "药品 乙1)盐酸氨溴索口服溶液(基) 口服 bid 5ml 1 2022-05-09 19:49:32 赵海国", "药品 赖氨肌醇维B12口服溶液 口服 bid 10ml 3 2022-05-09 19:49:32 赵海国", "药品 乙0)5ml灭菌注射用水 外用 bid 20ml 4 2022-05-05 09:58:24 李凌蔚", "药品 乙1)(扑尔敏针)马来酸氯苯那敏注射液 外用 bid 20mg 2 2022-05-05 09:58:24 李凌蔚", "药品 甲)地塞米松磷酸钠注射液(基) 外用 bid 10mg 2 2022-05-05 09:58:24 李凌蔚", "药品 乙1)消旋山莨菪碱注射液(基) 外用 bid 20mg 2 2022-05-05 09:58:24 李凌蔚", "药品 赖氨肌醇维B12口服溶液 口服 bid 10ml 1 2022-05-05 09:57:04 李凌蔚", "药品 乙1)复合维生素B片 口服 tid 1片 100 2022-05-05 09:56:29 李凌蔚", "药品 用维生素004/基 口服 4 100 2022-05-05 09:56:29 李凌蔚", "共70条 20条/页 < 1 2 3 4 > 前往 3 页", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 10:53:29,933 INFO     29 [qwen-vl-parser] page=36 text: 24 lines (bbox 1984-2007)
2026-08-05 10:53:29,933 INFO     29 [qwen-vl-parser] page=36 text: 24 sections
2026-08-05 10:53:30,093 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1008988, prompt_len=764
2026-08-05 10:53:31,574 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 10:53:31,575 INFO     29 [qwen-vl-parser] page=37 classify=text report_date=None
2026-08-05 10:53:31,593 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1008988, prompt_len=401
2026-08-05 10:53:33,102 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T10:53:33.099+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 10:53:38,824 INFO     29 [qwen-vl-parser] text API response (len=1136):
["50/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView", "984-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>", "返回概览视图", "门.", "J26-02-12 11.40.02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告", "请输入药品内容，按回车键检索", "查询全部", "类型 组 药品名称/规格 用法 频率 实际用量 总量 开立时间 开立医师", "药品 口服 bid 5ml 1 2022-05-09 19.49.32 赵海国", "药品 赖氨肌醇维B12口服溶液 口服 bid 10ml 3 2022-05-09 19.49.32 赵海国", "药品 乙0)5ml灭菌注射用水 外用 bid 20ml 4 2022-05-05 09.58.24 李凌蔚", "药品 乙1)(扑尔敏针)马来酸氯苯那敏注射液 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚", "药品 甲)地塞米松磷酸钠注射液(基) 外用 bid 10mg 2 2022-05-05 09.58.24 李凌蔚", "药品 乙1)消旋山莨菪碱注射液(基) 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚", "药品 赖氨肌醇维B12口服溶液 口服 bid 10ml 1 2022-05-05 09.57.04 李凌蔚", "药品 乙1)复合维生素B片 口服 tid 1片 100 2022-05-05 09.56.29 李凌蔚", "药品 甲)维生素B2片(基) 口服 tid 5mg 100 2022-05-05 09.56.29 李凌蔚", "药品 乙1)头孢克肟颗粒 口服 bid 50mg 2 2022-05-05 09.54.38 李凌蔚", "药品 乙1)金振口服液(基) 口服 bid 10ml 1 2022-05-05 09.54.38 李凌蔚", "药品 (盖克)小儿氨酚黄那敏颗粒 口服 tid 3g 2 2022-04-19 16.05.18 陈媛", "药品 乙1)美敏伪麻口服溶液 口服 tid 4ml 1 2022-04-19 16.05.18 陈媛", "药品 复方氨酚甲麻口服液 口服 qid 5ml 1 2022-04-19 16.05.18 陈媛", "共70条 20条/页 < 1 2 3 4 > 前往 3 页"]
2026-08-05 10:53:38,824 INFO     29 [qwen-vl-parser] page=37 text: 24 lines (bbox 2008-2031)
2026-08-05 10:53:38,825 INFO     29 [qwen-vl-parser] page=37 text: 24 sections
2026-08-05 10:53:38,957 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=767247, prompt_len=764
2026-08-05 10:53:40,263 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 10:53:40,264 INFO     29 [qwen-vl-parser] page=38 classify=text report_date=None
2026-08-05 10:53:40,276 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=767247, prompt_len=401
2026-08-05 10:53:46,466 INFO     29 [qwen-vl-parser] text API response (len=950):
["184-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>", "返回概览视图", "2026-02-12 11:40:02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告", "请输入药品内容,按回车键检索", "查询全部", "类型 组 药品名称(规格)", "药品 甲)(小儿)双黄连口服液(基)", "药品 (盖克)小儿氨酚黄那敏颗粒", "药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(基)", "药品 蒲地蓝消炎口服液", "药品 复方氨酚甲麻口服液", "药品 (盖克)小儿氨酚黄那敏颗粒", "药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(国基)", "药品 乙0)(普米克令舒)吸入用布地奈德混悬液(国基)", "药品 右旋糖酐铁颗粒", "药品 盐酸氨卓斯丁滴眼液", "用法 频率 实际用量 总量 开立时间 开立医师", "口服 tid 10ml 1 2022-03-26 19:51:46 谭真真", "口服 tid 6g 2 2022-03-26 19:51:18 谭真真", "口服(继续 用药) bid 0.228g 2 2022-03-26 19:51:18 谭真真", "口服 bid 10ml 1 2022-03-26 19:51:18 谭真真", "口服 q6h 10ml 2 2021-11-04 17:18:07 宁秀琴", "口服 tid 12g 2 2021-11-04 17:18:07 宁秀琴", "口服(继续 用药) q12h 0.45g 2 2021-11-04 17:18:07 宁秀琴", "压缩雾化 bid 2ml 5 2021-10-11 10:07:54 张冬梅", "口服 tid 1袋 80 2021-09-28 15:12:34 党建华", "滴双眼 bid 0.1ml 1 2021-09-09 15:18:56 史艳艳", "共70条 20条/页 < 1 2 3 4 > 前往 4 页", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 10:53:46,467 INFO     29 [qwen-vl-parser] page=38 text: 31 lines (bbox 2032-2062)
2026-08-05 10:53:46,467 INFO     29 [qwen-vl-parser] page=38 text: 31 sections
2026-08-05 10:53:46,638 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1417972, prompt_len=764
2026-08-05 10:53:48,082 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-06"
}
```
2026-08-05 10:53:48,083 INFO     29 [qwen-vl-parser] page=39 classify=table report_date=2026-01-06
2026-08-05 10:53:48,100 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1417972, prompt_len=756
2026-08-05 10:53:53,904 INFO     29 [qwen-vl-parser] table API response (len=1084):
\begin{tabular}{llllllllll}
\hline
英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 & 提示 \\
\hline
[WBC]白细胞数目 & & 4.28 & & 3.5~9.5 & 10^9/L & [HCT]红细胞压积 & & 37.8 & \\
[Lym\%]淋巴细胞百分比 & & 28.4 & & 20~50 & \% & [MCV]平均红细胞体积 & & 80.4 & $\downarrow$ \\
[Mon\%]单核细胞百分比 & & 4.7 & & 3~10 & \% & [MCH]平均红细胞血红蛋白含量 & & 26.0 & $\downarrow$ \\
[Neu\%]中性粒细胞百分比 & & 64.4 & & 40~75 & \% & [MCHC]平均红细胞血红蛋白浓度 & & 323 & \\
[Eos\%]嗜酸性细胞百分比 & & 2.4 & & 0.4~8 & \% & [RDW-CV]红细胞分布宽度变异系数 & & 15.2 & \\
[Bas\%]嗜碱性细胞百分比 & & 0.1 & & 0.0~1.0 & \% & [RDW-SD]红细胞分布宽度标准差 & & 43.0 & \\
[Lym\#]淋巴细胞数目 & & 1.22 & & 1.1~3.2 & 10^9/L & [PLT]血小板数目 & & 224 & \\
[Mon\#]单核细胞数目 & & 0.20 & & 0.1~0.6 & 10^9/L & [MPV]平均血小板体积 & & 8.0 & \\
[Neu\#]中性粒细胞数目 & & 2.76 & & 1.8~6.3 & 10^9/L & [PDW]血小板分布宽度 & & 16.0 & \\
[Eos\#]嗜酸性细胞数目 & & 0.10 & & 0.02~0.52 & 10^9/L & [PCT]血小板压积 & & 0.180 & \\
[Bas\#]嗜碱性细胞数目 & & 0.00 & & 0.00~0.06 & 10^9/L & [P-LCR]大型血小板比率 & & 15.8 & \\
[RBC]红细胞数目 & & 4.70 & & 3.8~5.1 & 10^12/L & [IG\%]未成熟粒细胞百分比 & & 0.4 & \\
[HGB]血红蛋白 & & 122 & & 115~150 & g/L & [IG\#]未成熟粒细胞计数 & & 0.02 & \\
\hline
\end{tabular}
2026-08-05 10:53:53,906 INFO     29 [qwen-vl-parser] page=39 table: 20 LaTeX lines (bbox 2063-2082)
2026-08-05 10:53:53,906 INFO     29 [qwen-vl-parser] page=39 table: 20 sections
2026-08-05 10:53:54,020 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=700044, prompt_len=764
2026-08-05 10:53:55,553 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-06"
}
```
2026-08-05 10:53:55,553 INFO     29 [qwen-vl-parser] page=40 classify=table report_date=2026-01-06
2026-08-05 10:53:55,562 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=700044, prompt_len=756
2026-08-05 10:53:56,480 INFO     29 [qwen-vl-parser] table API response (len=131):
\begin{tabular}{ccccccc}
\hline
英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\
\hline
{[}ESR{]}血沉 & & 7 & & 0~20 & mm/h \\
\hline
\end{tabular}
2026-08-05 10:53:56,481 INFO     29 [qwen-vl-parser] page=40 table: 8 LaTeX lines (bbox 2083-2090)
2026-08-05 10:53:56,481 INFO     29 [qwen-vl-parser] page=40 table: 8 sections
2026-08-05 10:53:56,624 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1083410, prompt_len=764
2026-08-05 10:53:58,186 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-06"
}
```
2026-08-05 10:53:58,186 INFO     29 [qwen-vl-parser] page=41 classify=table report_date=2026-01-06
2026-08-05 10:53:58,196 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1083410, prompt_len=756
2026-08-05 10:54:01,938 INFO     29 [qwen-vl-parser] table API response (len=675):
\begin{tabular}{ccccccl}
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
2026-08-05 10:54:01,939 INFO     29 [qwen-vl-parser] page=41 table: 21 LaTeX lines (bbox 2091-2111)
2026-08-05 10:54:01,939 INFO     29 [qwen-vl-parser] page=41 table: 21 sections
2026-08-05 10:54:02,122 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1288667, prompt_len=764
2026-08-05 10:54:03,119 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T10:54:03.117+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 10:54:03,668 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-06"
}
```
2026-08-05 10:54:03,668 INFO     29 [qwen-vl-parser] page=42 classify=table report_date=2026-01-06
2026-08-05 10:54:03,678 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1288667, prompt_len=756
2026-08-05 10:54:13,745 INFO     29 [qwen-vl-parser] table API response (len=2380):
\begin{tabular}{lllll}
\hline
\multicolumn{2}{l}{\textbf{瑞图RT-F600}} & \multicolumn{3}{c}{\textbf{医学检验科检验报告单}} \\
\multicolumn{2}{l}{\textbf{白带分析仪}} & \multicolumn{3}{c}{} \\
\multicolumn{2}{l}{\textbf{姓 名:}} & \multicolumn{2}{l}{\textbf{送检科室: 妇科一病区(门)}} & \multicolumn{1}{l}{\textbf{床 号:}} \\
\multicolumn{2}{l}{\textbf{住院(门诊)号:}} & \multicolumn{2}{l}{\textbf{性 别: 女}} & \multicolumn{1}{l}{\textbf{年 龄: 41岁}} \\
\multicolumn{2}{l}{\textbf{检验项目: 妇科微生态}} & \multicolumn{3}{l}{\textbf{样本类型: 阴道分泌物}} \\
\multicolumn{2}{l}{\textbf{疾病诊断: 慢性盆腔痛}} & \multicolumn{3}{l}{\textbf{样本状态: 正常}} \\
\hline
\multicolumn{5}{l}{\textbf{形态学检测项目:}} \\
\multicolumn{2}{l}{细胞情况} & \textbf{结果} & \textbf{正常值范围} & \textbf{镜下所见:} \\
\multicolumn{2}{l}{清洁度} & Ⅱ & $\sim \le$II & \\
\multicolumn{2}{l}{白细胞} & 5-15 & $\le$15/HP & \\
\multicolumn{2}{l}{红细胞} & 未检出 & $\sim$未检出 & \\
\multicolumn{2}{l}{线索细胞} & 未检出 & $\sim$未检出 & \\
\multicolumn{2}{l}{上皮细胞} & 10-15 & $\sim$满视野 & \\
\multicolumn{5}{l}{} \\
\multicolumn{2}{l}{病原体情况:} & & & \\
\multicolumn{2}{l}{滴虫} & 未检出 & $\sim$未检出 & \\
\multicolumn{2}{l}{菌丝} & 未检出 & $\sim$未检出 & \\
\multicolumn{2}{l}{孢子} & 未检出 & $\sim$未检出 & \\
\multicolumn{2}{l}{芽生孢子} & 未检出 & $\sim$未检出 & \\
\multicolumn{5}{l}{} \\
\multicolumn{2}{l}{菌群情况:} & & & \\
\multicolumn{2}{l}{菌群密集度} & ++ & $\sim$++ & \\
\multicolumn{2}{l}{多样性} & + & $\sim$++ & \\
\multicolumn{2}{l}{优势菌} & G+杆菌 & $\sim$G阳性杆菌 & \\
\multicolumn{2}{l}{$\beta$-N-乙酰氨基葡萄糖苷酶(NAG)} & - & $\sim$- & \\
\multicolumn{5}{l}{} \\
\multicolumn{2}{l}{功能学分析:} & & & \\
\multicolumn{2}{l}{唾液酸苷酶} & - & $\sim$- & \\
\multicolumn{2}{l}{白细胞酯酶} & - & $\sim$- & \\
\multicolumn{2}{l}{胺试验} & - & $\sim$- & \\
\multicolumn{2}{l}{脯氨酸氨基肽酶PIP} & - & $\sim$- & \\
\multicolumn{2}{l}{过氧化氢(H2O2)} & + & $\sim$- & \\
\multicolumn{2}{l}{pH值} & 3.8 & 3.8 $\sim$ 4.5 & \\
\multicolumn{2}{l}{Nugent评分2} & \multicolumn{2}{l}{AV评分1} & \\
\hline
\multicolumn{5}{l}{※ 备注:阴道微生态未见明显异常!} \\
\hline
\multicolumn{2}{l}{采集时间: 2026-01-06} & \multicolumn{2}{l}{接收时间: 2026-01-06} & \multicolumn{1}{l}{审核时间: 2026-01-06} \\
\multicolumn{2}{l}{09:15} & \multicolumn{2}{l}{09:22} & \multicolumn{1}{l}{10:59} \\
\multicolumn{2}{l}{送检医生: 权丽丽} & \multicolumn{2}{l}{检验者: 伊原原} & \multicolumn{1}{l}{审核者: 介倩倩} \\
\multicolumn{5}{l}{打印时间: 2026/2/26 下午 3:59:58} \\
\multicolumn{5}{l}{打印者: 网页打印} \\
\multicolumn{5}{l}{※本报告检查结果实行互认制度,如有疑问,请在三天内和我们联系,电} \\
\hline
\end{tabular}
2026-08-05 10:54:13,746 INFO     29 [qwen-vl-parser] page=42 table: 49 LaTeX lines (bbox 2112-2160)
2026-08-05 10:54:13,746 INFO     29 [qwen-vl-parser] page=42 table: 49 sections
2026-08-05 10:54:13,886 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=906578, prompt_len=764
2026-08-05 10:54:15,450 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-06"
}
```
2026-08-05 10:54:15,450 INFO     29 [qwen-vl-parser] page=43 classify=table report_date=2026-01-06
2026-08-05 10:54:15,456 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=906578, prompt_len=756
2026-08-05 10:54:19,611 INFO     29 [qwen-vl-parser] table API response (len=791):
\begin{tabular}{cccccc}
\hline
英文 & 项目名称 & 结果 & 参考范围 & 单位 & \\
\hline
\multicolumn{2}{l}{[\beta-HCG]人绒毛膜促性腺激素} & 0.40 & \begin{tabular}[c]{@{}c@{}}非孕期 0~2.9 \\ 0.2-1周 5~50 \\ 1-2周 50~500 \\ 2-3周 100~5000 \\ 3-4周 500~10000 \\ 4-5周 1000~50000 \\ 5-6周 10000~100000 \\ 6-8周 15000~200000\end{tabular} & \multicolumn{2}{c}{mIU/ml} \\
\hline
\end{tabular}

\begin{tabular}{llllll}
\hline
采集时间: & 2026-01-06 & 接收时间: & 2026-01-06 & 审核时间: & 2026-01-06 \\
& 09:15 & & 10:03 & & 11:06 \\
送检医生: & 权丽丽 & 检验者: & 秦淑云 & 审核者: & 薛轩 \\
\hline
\end{tabular}

\begin{tabular}{llllll}
\hline
\multicolumn{6}{l}{\textbf{※本报告检查结果实行互认制度，如有疑问，请在三天内和我们联系，电话：}} \\
\multicolumn{6}{l}{\textbf{打印时间: 2026/2/26 下午 4:00:10}} \\
\multicolumn{6}{l}{\textbf{打印者: 网页打印}} \\
\multicolumn{6}{l}{\textbf{※}} \\
\hline
\end{tabular}
2026-08-05 10:54:19,613 INFO     29 [qwen-vl-parser] page=43 table: 26 LaTeX lines (bbox 2161-2186)
2026-08-05 10:54:19,613 INFO     29 [qwen-vl-parser] page=43 table: 26 sections
2026-08-05 10:54:19,726 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=740740, prompt_len=764
2026-08-05 10:54:21,258 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-06"
}
```
2026-08-05 10:54:21,259 INFO     29 [qwen-vl-parser] page=44 classify=table report_date=2026-01-06
2026-08-05 10:54:21,279 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=740740, prompt_len=756
2026-08-05 10:54:22,328 INFO     29 [qwen-vl-parser] table API response (len=156):
\begin{tabular}{ccccccc}
\hline
英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\
\hline
[OV125Ag]CA-125 & & 59.70 & $\uparrow$ & 0.00~35.00 & U/ml \\
\hline
\end{tabular}
2026-08-05 10:54:22,329 INFO     29 [qwen-vl-parser] page=44 table: 8 LaTeX lines (bbox 2187-2194)
2026-08-05 10:54:22,329 INFO     29 [qwen-vl-parser] page=44 table: 8 sections
2026-08-05 10:54:22,495 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1364813, prompt_len=764
2026-08-05 10:54:24,056 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-06"
}
```
2026-08-05 10:54:24,056 INFO     29 [qwen-vl-parser] page=45 classify=table report_date=2026-01-06
2026-08-05 10:54:24,067 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1364813, prompt_len=756
2026-08-05 10:54:30,014 INFO     29 [qwen-vl-parser] table API response (len=1135):
\begin{tabular}{ccccccccc}
\hline
英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\
\hline
[颜色]颜色 & & 黄色 & & 清 & & [尿酸结晶]尿酸结晶 & & 0 & & 0~15 & 个/ul \\
[浊度]浊度 & & 清亮 & & 清 & & [草酸钙结晶]草酸钙结晶 & & 0 & & 0~30 & 个/ul \\
[GLU]葡萄糖 & & - & & 阴性 & & [上皮细胞]上皮细胞 & & 14 & & 0~20 & 个/ul \\
[BLD]潜血 & & - & & 阴性 & & [粘液丝]粘液丝 & & 5 & & 0~20 & 个/ul \\
[LEU]白细胞 & & 2+ & & 阴性 & & [酵母菌]酵母菌 & & 6 & $\uparrow$ & 0~0 & 个/ul \\
[PRO]蛋白质 & & - & & 阴性 & & [透明管型]透明管型 & & 0 & & 0~1 & 个/ul \\
[NIT]亚硝酸盐 & & + & & 阴性 & & [颗粒管型]颗粒管型 & & 0 & & 0~0 & 个/ul \\
[URO]尿胆素原 & & - & & 阴性 & & [小圆上皮]小圆上皮 & & 0 & & 0~3 & 个/ul \\
[BIL]胆红素 & & - & & 阴性 & & [其他管型]其他管型 & & 0 & & 0~0 & 个/ul \\
[KET]酮体 & & - & & 阴性 & & [其他上皮]其他上皮 & & 0 & & 0~10 & 个/ul \\
[Vc]维生素C & & - & & - & & [异常红细胞]异常红细胞 & & 0 & & 0~5 & 个/ul \\
[pH]酸碱性 & & 6.0 & & 5.0~8.5 & & [细菌]细菌 & & 1072 & $\uparrow$ & 0~50 & 个/ul \\
[SG]比重 & & 1.020 & & 1.010~ & & [尿沉渣镜检]尿沉渣镜检 & & : & & & \\
& & & & 1.025 & & [白细胞]白细胞 & & +++/HP & & $\le$5/HP & \\
[红细胞]红细胞 & & 0 & & 0~5 & 个/ul & [红细胞]红细胞 & & 未查见 & & $\le$3/HP & \\
[白细胞]白细胞 & & 218 & $\uparrow$ & 0~7 & 个/ul & & & & & & \\
\hline
\end{tabular}
2026-08-05 10:54:30,016 INFO     29 [qwen-vl-parser] page=45 table: 23 LaTeX lines (bbox 2195-2217)
2026-08-05 10:54:30,016 INFO     29 [qwen-vl-parser] page=45 table: 23 sections
2026-08-05 10:54:30,146 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=871040, prompt_len=764
2026-08-05 10:54:31,699 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-15"
}
```
2026-08-05 10:54:31,699 INFO     29 [qwen-vl-parser] page=46 classify=table report_date=2026-01-15
2026-08-05 10:54:31,719 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=871040, prompt_len=756
2026-08-05 10:54:33,150 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T10:54:33.148+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 10:54:33,984 INFO     29 [qwen-vl-parser] table API response (len=377):
\begin{tabular}{ccccccl}
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
2026-08-05 10:54:33,985 INFO     29 [qwen-vl-parser] page=46 table: 13 LaTeX lines (bbox 2218-2230)
2026-08-05 10:54:33,985 INFO     29 [qwen-vl-parser] page=46 table: 13 sections
2026-08-05 10:54:34,160 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1420685, prompt_len=764
2026-08-05 10:54:35,736 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-15"
}
```
2026-08-05 10:54:35,736 INFO     29 [qwen-vl-parser] page=47 classify=table report_date=2026-01-15
2026-08-05 10:54:35,749 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1420685, prompt_len=756
2026-08-05 10:54:43,363 INFO     29 [qwen-vl-parser] table API response (len=1412):
\begin{tabular}{ccccccccc}
\hline
英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\
\hline
{[}WBC{]}白细胞数目 & & 4.20 & & 3.5~9.5 & 10^9/L & {[}HCT{]}红细胞压积 & & 38.3 & & 35~45 & \% \\
{[}Lym\%{]}淋巴细胞百分比 & & 28.6 & & 20~50 & \% & {[}MCV{]}平均红细胞体积 & & 81.3 & $\downarrow$ & 82~100 & fL \\
{[}Mon\%{]}单核细胞百分比 & & 5.0 & & 3~10 & \% & {[}MCH{]}平均红细胞血红蛋白含量 & & 25.6 & $\downarrow$ & 27~34 & pg \\
{[}Neu\%{]}中性粒细胞百分比 & & 64.5 & & 40~75 & \% & {[}MCHC{]}平均红细胞血红蛋白浓度 & & 313 & $\downarrow$ & 316~354 & g/L \\
{[}Eos\%{]}嗜酸性细胞百分比 & & 1.7 & & 0.4~8 & \% & {[}RDW-CV{]}红细胞分布宽度变异系数 & & 14.9 & & 11~16 & \% \\
{[}Bas\%{]}嗜碱性细胞百分比 & & 0.2 & & 0.0~1.0 & \% & {[}RDW-SD{]}红细胞分布宽度标准差 & & 43.2 & & 35.0~56.0 & fL \\
{[}Lym\# {]}淋巴细胞数目 & & 1.20 & & 1.1~3.2 & 10^9/L & {[}PLT{]}血小板数目 & & 288 & & 125~350 & 10^9/L \\
{[}Mon\# {]}单核细胞数目 & & 0.21 & & 0.1~0.6 & 10^9/L & {[}MPV{]}平均血小板体积 & & 9.0 & & 6.5~12 & fL \\
{[}Neu\# {]}中性粒细胞数目 & & 2.71 & & 1.8~6.3 & 10^9/L & {[}PDW{]}血小板分布宽度 & & 15.6 & & 9~17 & fL \\
{[}Eos\# {]}嗜酸性细胞数目 & & 0.07 & & 0.02~0.52 & 10^9/L & {[}PCT{]}血小板压积 & & 0.258 & & 0.108~ & \% \\
{[}Bas\# {]}嗜碱性细胞数目 & & 0.01 & & 0.00~0.06 & 10^9/L & {[}P-LCR{]}大型血小板比率 & & 19.3 & & 11~45 & \% \\
{[}RBC{]}红细胞数目 & & 4.71 & & 3.8~5.1 & 10^12/L & {[}IG\%{]}未成熟粒细胞百分比 & & 0.1 & & 0.0~0.6 & \% \\
{[}HGB{]}血红蛋白 & & 120 & & 115~150 & g/L & {[}IG\# {]}未成熟粒细胞计数 & & 0.00 & & 0.00~0.06 & 10^9/L \\
\hline
\end{tabular}
2026-08-05 10:54:43,364 INFO     29 [qwen-vl-parser] page=47 table: 20 LaTeX lines (bbox 2231-2250)
2026-08-05 10:54:43,364 INFO     29 [qwen-vl-parser] page=47 table: 20 sections
2026-08-05 10:54:43,550 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1427726, prompt_len=764
2026-08-05 10:54:45,188 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-15"
}
```
2026-08-05 10:54:45,188 INFO     29 [qwen-vl-parser] page=48 classify=table report_date=2026-01-15
2026-08-05 10:54:45,201 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1427726, prompt_len=756
2026-08-05 10:55:03,188 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T10:55:03.187+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 10:55:33,214 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T10:55:33.213+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 10:56:03,259 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T10:56:03.258+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 10:56:33,299 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T10:56:33.297+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 10:56:54,477 INFO     29 [qwen-vl-parser] table API response (len=43275):
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
2026-08-05 10:56:54,481 INFO     29 [qwen-vl-parser] page=48 table: 11 LaTeX lines (bbox 2251-2261)
2026-08-05 10:56:54,482 INFO     29 [qwen-vl-parser] page=48 table: 11 sections
2026-08-05 10:56:54,663 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1378163, prompt_len=764
2026-08-05 10:56:56,232 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-15"
}
```
2026-08-05 10:56:56,233 INFO     29 [qwen-vl-parser] page=49 classify=table report_date=2026-01-15
2026-08-05 10:56:56,249 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1378163, prompt_len=756
2026-08-05 10:56:59,815 INFO     29 [qwen-vl-parser] table API response (len=659):
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
2026-08-05 10:56:59,815 INFO     29 [qwen-vl-parser] page=49 table: 18 LaTeX lines (bbox 2262-2279)
2026-08-05 10:56:59,815 INFO     29 [qwen-vl-parser] page=49 table: 18 sections
2026-08-05 10:56:59,940 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=814682, prompt_len=764
2026-08-05 10:57:01,477 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-15"
}
```
2026-08-05 10:57:01,477 INFO     29 [qwen-vl-parser] page=50 classify=table report_date=2026-01-15
2026-08-05 10:57:01,486 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=814682, prompt_len=756
2026-08-05 10:57:02,998 INFO     29 [qwen-vl-parser] table API response (len=244):
\begin{tabular}{ccccccc}
\hline
英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\
\hline
[FT3]游离三碘甲状腺原氨酸 & & 3.11 & & 2.14~4.21 & pg/mL \\
[FRt4]游离甲状腺素 & & 0.76 & & 0.61~1.12 & ng/dL \\
[fTSH3]超敏促甲状腺素 & & 1.350 & & 0.560~5.910 & uIU/ml \\
\hline
\end{tabular}
2026-08-05 10:57:02,999 INFO     29 [qwen-vl-parser] page=50 table: 10 LaTeX lines (bbox 2280-2289)
2026-08-05 10:57:02,999 INFO     29 [qwen-vl-parser] page=50 table: 10 sections
2026-08-05 10:57:03,163 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1044406, prompt_len=764
2026-08-05 10:57:03,317 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T10:57:03.316+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 10:57:04,741 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-15"
}
```
2026-08-05 10:57:04,741 INFO     29 [qwen-vl-parser] page=51 classify=table report_date=2026-01-15
2026-08-05 10:57:04,754 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1044406, prompt_len=756
2026-08-05 10:57:06,643 INFO     29 [qwen-vl-parser] table API response (len=310):
\begin{tabular}{ccccccc}
\hline
英文 & 项目名称 & 结果 & SCO & 提示 & 参考范围 & 单位 \\
\hline
{[HBsAg]}乙肝表面抗原(酶免法) & 阴性 & 0.04 & 阴性 & s/co & & \\
{[抗-HCV]}丙肝抗体(酶免法) & 阴性 & 0.15 & 阴性 & s/co & & \\
{[抗-HIV]}人免疫缺陷病毒抗体(酶免法) & 阴性 & 0.06 & 阴性 & s/co & & \\
{[TP-Ab]}梅毒螺旋体抗体(酶免法) & 阴性 & 0.07 & 阴性 & s/co & & \\
\hline
\end{tabular}
2026-08-05 10:57:06,644 INFO     29 [qwen-vl-parser] page=51 table: 11 LaTeX lines (bbox 2290-2300)
2026-08-05 10:57:06,644 INFO     29 [qwen-vl-parser] page=51 table: 11 sections
2026-08-05 10:57:06,845 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1042924, prompt_len=764
2026-08-05 10:57:09,746 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 10:57:09,747 INFO     29 [qwen-vl-parser] page=52 classify=text report_date=None
2026-08-05 10:57:09,759 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1042924, prompt_len=401
2026-08-05 10:57:11,217 INFO     29 [qwen-vl-parser] text API response (len=169):
["处方笺", "4970401", "姓名：", "性别：□男 □女 年龄：60岁", "科别： 费别： 电话/住址：", "过敏史：无 开具日期：2021年2月16日", "临床诊断：支气管哮喘", "Rp", "孟鲁司特钠片 10mg 2板", "用法：二天一次 1片", "审核： 调配： 医师：", "核对： 发药： 金额："]
2026-08-05 10:57:11,217 INFO     29 [qwen-vl-parser] page=52 text: 12 lines (bbox 2301-2312)
2026-08-05 10:57:11,217 INFO     29 [qwen-vl-parser] page=52 text: 12 sections
2026-08-05 10:57:11,217 INFO     29 [qwen-vl-parser] parse_pdf done: 2313 sections from 52 pages.
2026-08-05 10:57:11,232 INFO     29 Close text detector.
2026-08-05 10:57:11,631 INFO     29 Close text recognizer.
2026-08-05 10:57:12,017 INFO     29 Close recognizer.
2026-08-05 10:57:12,387 INFO     29 Close recognizer.
2026-08-05 10:57:12,911 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-05 10:57:12,912 INFO     29 [Trace] task=39f07238 | doc=DAXI-哮喘.pdf | Parser:MedLink | outputs={"html": "", "json": "2313 items", "markdown": "", "text": "", "name": "DAXI-哮喘.pdf", "output_format": "json"}
2026-08-05 10:57:12,912 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-05 10:57:12,949 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 10:57:12,950 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。只有主诉，病史的也属于OutpatientRecord（门诊病历）\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 呼出气一氧化氮测定报告单\n[BBOX-1] 病人信息：\n[BBOX-2] 编号：482\n[BBOX-3] 姓名：\n[BBOX-4] 年龄：41岁9月27天\n[BBOX-5] 性别：女\n[BBOX-6] 科室：普通儿科一区\n[BBOX-7] 出生日期：1984-04-02\n[BBOX-8] 测定时间：2026/1/29 11:02:42\n[BBOX-9] 测定信息：\n[BBOX-10] 一小时内禁止饮食：■是\n[BBOX-11] 一小时内禁止剧烈运动：■是\n[BBOX-12] 三小时内禁止食用特殊食品*：■是\n[BBOX-13] 一小时内禁止抽烟：■是\n[BBOX-14] 三天内使用激素类药物：■是 □否\n[BBOX-15] 三天内使用抗生素：□是 ■否\n[BBOX-16] 症状：□咳嗽 □喘息 □鼻塞 □喷嚏 ■其他\n[BBOX-17] 病史：□过敏史 □其它\n[BBOX-18] *是指西兰花、芥蓝、生菜、莴苣、芹菜、水萝卜、熏制、腌制类食品。\n[BBOX-19] 测定项目：\n[BBOX-20] 呼气方式：■在线 □离线 □潮气\n[BBOX-21] 呼气温度：20.1℃\n[BBOX-22] 呼气压力：13.6cmH20\n[BBOX-23] 呼气平均流速：48ml/s\n[BBOX-24] 呼气NO浓度：\n[BBOX-25] 32.7,31.0,32.0,31.8,32.1,31.7ppb\n[BBOX-26] 呼气NO浓度均值：32ppb\n[BBOX-27] 呼气方式：■在线 □离线 □潮气\n[BBOX-28] 呼气温度：20.3℃\n[BBOX-29] 呼气压力：7.9cmH20\n[BBOX-30] 呼气平均流速：207ml/s\n[BBOX-31] 呼气NO浓度：\n[BBOX-32] 11.7,11.9,11.3,11.6,11.6,11.6ppb\n[BBOX-33] 呼气NO浓度均值：12ppb\n[BBOX-34] 测定结果：\n[BBOX-35] FeNO50：32ppb\n[BBOX-36] FeNO200：12ppb\n[BBOX-37] CaNO：3.6ppb\n[BBOX-38] 测定意义：\n[BBOX-39] 测定浓度\n[BBOX-40] 参考值\n[BBOX-41] 炎症鉴别诊断\n[BBOX-42] >12岁\n[BBOX-43] ≤12岁\n[BBOX-44] FeNO50\n[BBOX-45] <25ppb\n[BBOX-46] <20ppb*\n[BBOX-47] 非嗜酸性气道炎症\n[BBOX-48] 25-50ppb\n[BBOX-49] 20-35ppb*\n[BBOX-50] 混合型气道炎症\n[BBOX-51] ≥50ppb\n[BBOX-52] ≥35ppb*\n[BBOX-53] 嗜酸性气道炎症\n[BBOX-54] FeNO200\n[BBOX-55] >10ppb\n[BBOX-56] >8ppb\n[BBOX-57] 小气道炎症\n[BBOX-58] CaNO\n[BBOX-59] >5ppb\n[BBOX-60] >3ppb\n[BBOX-61] 肺泡炎症\n[BBOX-62] (*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)\n[BBOX-63] 复查时间：\n[BBOX-64] 操作员：赵彩红\n[BBOX-65] 医生：马春英\n[BBOX-66] 电\n[BBOX-67] 告\n[BBOX-68] 单\n[BBOX-69] 更\n[BBOX-70] 肺功能检查报告单\n[BBOX-71] 姓名：\n[BBOX-72] 测试号：\n[BBOX-73] 住院号：\n[BBOX-74] 身高：\n[BBOX-75] 160 cm\n[BBOX-76] 年龄：\n[BBOX-77] 41 岁\n[BBOX-78] 体重：\n[BBOX-79] 48 kg\n[BBOX-80] 性别：\n[BBOX-81] 女\n[BBOX-82] 身份证号：\n[BBOX-83] 科别：\n[BBOX-84] 联系电话：\n[BBOX-85] 预计值\n[BBOX-86] Bst % (Bst/\n[BBOX-87] A1\n[BBOX-88] A2\n[BBOX-89] A3\n[BBOX-90] FVC\n[BBOX-91] [L]\n[BBOX-92] 3.13\n[BBOX-93] 3.15\n[BBOX-94] 100.54\n[BBOX-95] 3.15\n[BBOX-96] 3.08\n[BBOX-97] 3.07\n[BBOX-98] FEV 1\n[BBOX-99] [L]\n[BBOX-100] 2.70\n[BBOX-101] 1.99\n[BBOX-102] 73.90\n[BBOX-103] 1.99\n[BBOX-104] 1.85\n[BBOX-105] 1.96\n[BBOX-106] FEV6\n[BBOX-107] [L]\n[BBOX-108] 3.13\n[BBOX-109] 3.13\n[BBOX-110] 3.05\n[BBOX-111] FEV 1 % FVC\n[BBOX-112] [%]\n[BBOX-113] 83.98\n[BBOX-114] 63.25\n[BBOX-115] 75.31\n[BBOX-116] 63.25\n[BBOX-117] 60.02\n[BBOX-118] 63.82\n[BBOX-119] FEV 1 % VC MAX\n[BBOX-120] [%]\n[BBOX-121] 81.31\n[BBOX-122] 63.25\n[BBOX-123] 77.78\n[BBOX-124] 63.25\n[BBOX-125] 58.74\n[BBOX-126] 62.12\n[BBOX-127] FIF 50\n[BBOX-128] [L/s]\n[BBOX-129] 5.84\n[BBOX-130] 5.77\n[BBOX-131] 5.84\n[BBOX-132] 5.48\n[BBOX-133] FEV3 % FVC\n[BBOX-134] [%]\n[BBOX-135] 89.30\n[BBOX-136] 89.30\n[BBOX-137] 87.11\n[BBOX-138] 88.97\n[BBOX-139] VC MAX\n[BBOX-140] [L]\n[BBOX-141] 3.19\n[BBOX-142] 3.15\n[BBOX-143] 98.65\n[BBOX-144] 2.99\n[BBOX-145] PEF\n[BBOX-146] [L/s]\n[BBOX-147] 6.46\n[BBOX-148] 6.33\n[BBOX-149] 97.97\n[BBOX-150] 6.33\n[BBOX-151] 5.90\n[BBOX-152] 5.95\n[BBOX-153] MMEF 75/25\n[BBOX-154] [L/s]\n[BBOX-155] 3.53\n[BBOX-156] 1.06\n[BBOX-157] 30.03\n[BBOX-158] 1.06\n[BBOX-159] 0.89\n[BBOX-160] 0.99\n[BBOX-161] MEF 25\n[BBOX-162] [L/s]\n[BBOX-163] 1.77\n[BBOX-164] 0.46\n[BBOX-165] 26.28\n[BBOX-166] 0.46\n[BBOX-167] 0.38\n[BBOX-168] 0.40\n[BBOX-169] MEF 50\n[BBOX-170] [L/s]\n[BBOX-171] 4.06\n[BBOX-172] 1.25\n[BBOX-173] 30.90\n[BBOX-174] 1.25\n[BBOX-175] 1.13\n[BBOX-176] 1.24\n[BBOX-177] MEF 75\n[BBOX-178] [L/s]\n[BBOX-179] 5.73\n[BBOX-180] 3.01\n[BBOX-181] 52.56\n[BBOX-182] 3.01\n[BBOX-183] 2.22\n[BBOX-184] 2.68\n[BBOX-185] V backextrapolation [B]\n[BBOX-186] 0.06\n[BBOX-187] 0.06\n[BBOX-188] 0.05\n[BBOX-189] 0.06\n[BBOX-190] V backextrapol. % FVC\n[BBOX-191] 1.86\n[BBOX-192] 1.86\n[BBOX-193] 1.52\n[BBOX-194] 1.82\n[BBOX-195] FET\n[BBOX-196] [s]\n[BBOX-197] 8.73\n[BBOX-198] 8.73\n[BBOX-199] 5.99\n[BBOX-200] 6.71\n[BBOX-201] FEF 200-1200\n[BBOX-202] [L/s]\n[BBOX-203] 3.07\n[BBOX-204] 3.07\n[BBOX-205] 2.51\n[BBOX-206] 2.98\n[BBOX-207] FVC IN\n[BBOX-208] [L]\n[BBOX-209] 3.19\n[BBOX-210] 2.99\n[BBOX-211] 93.64\n[BBOX-212] 2.26\n[BBOX-213] 2.99\n[BBOX-214] 2.94\n[BBOX-215] FIV1\n[BBOX-216] [L]\n[BBOX-217] 2.96\n[BBOX-218] 2.24\n[BBOX-219] 2.96\n[BBOX-220] 2.92\n[BBOX-221] FIV1 % FVC\n[BBOX-222] [%]\n[BBOX-223] 99.14\n[BBOX-224] 99.32\n[BBOX-225] 99.14\n[BBOX-226] 99.48\n[BBOX-227] FEF50 % FIF50\n[BBOX-228] [%]\n[BBOX-229] 21.46\n[BBOX-230] 21.72\n[BBOX-231] 19.34\n[BBOX-232] 22.60\n[BBOX-233] PIF\n[BBOX-234] [L/s]\n[BBOX-235] 6.10\n[BBOX-236] 5.87\n[BBOX-237] 6.10\n[BBOX-238] 5.50\n[BBOX-239] MVV\n[BBOX-240] [L/min]\n[BBOX-241] 101.9\n[BBOX-242] 91.45\n[BBOX-243] 89.73\n[BBOX-244] 91.45\n[BBOX-245] BF MVV\n[BBOX-246] [1/min]\n[BBOX-247] 75.65\n[BBOX-248] 75.65\n[BBOX-249] Flow [L/s]\n[BBOX-250] F/V ex\n[BBOX-251] Vol [L]\n[BBOX-252] Vol%VCmax\n[BBOX-253] Vol [L]\n[BBOX-254] Time [s]\n[BBOX-255] Vol [L]\n[BBOX-256] Time [s]\n[BBOX-257] 意见：\n[BBOX-258] 1.轻度阻塞性通气功能障碍。\n[BBOX-259] 检查质量：FVC：A级。 FEV1：A级。\n[BBOX-260] 备注：受检者检查配合佳。结果仅供参考，请结合临床分析。\n[BBOX-261] 2.最大自主分钟通气量（MVV）在正常范围。\n[BBOX-262] 备注：患者MVV配合佳。结果仅供参考，请结合临床分析。\n[BBOX-263] 审核医生：孙帅森\n[BBOX-264] 检测技师：韦龙华\n[BBOX-265] 2026/1/15\n[BBOX-266] 肺功能报告单\n[BBOX-267] 姓名：\n[BBOX-268] 性别：女\n[BBOX-269] 出生日期：1984/11/02\n[BBOX-270] 年龄：41岁\n[BBOX-271] 住院号：\n[BBOX-272] 测试号：\n[BBOX-273] 身高：160 cm\n[BBOX-274] 体重：48 kg\n[BBOX-275] 身份证号：\n[BBOX-276] 预计\n[BBOX-277] 实1 %(实1/预)\n[BBOX-278] 实2 %(实2/预)\n[BBOX-279] 变异率\n[BBOX-280] 测试日期\n[BBOX-281] 26/1/15\n[BBOX-282] 26/1/15\n[BBOX-283] 测试时间\n[BBOX-284] 9:51:00上午\n[BBOX-285] 10:14:56上午\n[BBOX-286] FVC\n[BBOX-287] [L]\n[BBOX-288] 3.13\n[BBOX-289] 3.15\n[BBOX-290] 100.5\n[BBOX-291] 3.25\n[BBOX-292] 103.9\n[BBOX-293] 3.3\n[BBOX-294] FEV 1\n[BBOX-295] [L]\n[BBOX-296] 2.70\n[BBOX-297] 1.99\n[BBOX-298] 73.9\n[BBOX-299] 2.26\n[BBOX-300] 83.8\n[BBOX-301] 13.4\n[BBOX-302] FEV 1 % FVC\n[BBOX-303] [%]\n[BBOX-304] 83.98\n[BBOX-305] 63.25\n[BBOX-306] 75.3\n[BBOX-307] 69.40\n[BBOX-308] 82.6\n[BBOX-309] 9.7\n[BBOX-310] FEV 1 % VC MAX\n[BBOX-311] [%]\n[BBOX-312] 81.31\n[BBOX-313] 63.25\n[BBOX-314] 77.8\n[BBOX-315] 69.40\n[BBOX-316] 85.4\n[BBOX-317] 9.7\n[BBOX-318] PEF\n[BBOX-319] [L/s]\n[BBOX-320] 6.46\n[BBOX-321] 6.33\n[BBOX-322] 98.0\n[BBOX-323] 7.25\n[BBOX-324] 112.2\n[BBOX-325] 14.5\n[BBOX-326] MEF 75\n[BBOX-327] [L/s]\n[BBOX-328] 5.73\n[BBOX-329] 3.01\n[BBOX-330] 52.6\n[BBOX-331] 3.73\n[BBOX-332] 65.1\n[BBOX-333] 23.8\n[BBOX-334] MEF 50\n[BBOX-335] [L/s]\n[BBOX-336] 4.06\n[BBOX-337] 1.25\n[BBOX-338] 30.9\n[BBOX-339] 1.67\n[BBOX-340] 41.2\n[BBOX-341] 33.3\n[BBOX-342] MEF 25\n[BBOX-343] [L/s]\n[BBOX-344] 1.77\n[BBOX-345] 0.46\n[BBOX-346] 26.3\n[BBOX-347] 0.59\n[BBOX-348] 33.6\n[BBOX-349] 27.7\n[BBOX-350] MMEF 75/25\n[BBOX-351] [L/s]\n[BBOX-352] 3.53\n[BBOX-353] 1.06\n[BBOX-354] 30.0\n[BBOX-355] 1.46\n[BBOX-356] 41.3\n[BBOX-357] 37.6\n[BBOX-358] FET\n[BBOX-359] [s]\n[BBOX-360] 8.73\n[BBOX-361] 4.94\n[BBOX-362] -43.4\n[BBOX-363] V backextrapolation ex [L]\n[BBOX-364] 0.06\n[BBOX-365] 0.07\n[BBOX-366] 20.1\n[BBOX-367] V backextrapol. % FVC [%]\n[BBOX-368] 1.86\n[BBOX-369] 2.17\n[BBOX-370] 16.3\n[BBOX-371] Flow [L/s]\n[BBOX-372] F/V ex\n[BBOX-373] 10\n[BBOX-374] 5\n[BBOX-375] 0\n[BBOX-376] 1\n[BBOX-377] 2\n[BBOX-378] 3\n[BBOX-379] 4\n[BBOX-380] 5\n[BBOX-381] 6\n[BBOX-382] 7\n[BBOX-383] 10\n[BBOX-384] F/V In\n[BBOX-385] 医生意见：\n[BBOX-386] 支气管舒张试验阳性。\n[BBOX-387] (通过储雾罐吸入硫酸沙丁胺醇气雾剂400ug20分钟后。\n[BBOX-388] FEV1较基线增加大于12 %，且绝对值增加大于200 ml。\n[BBOX-389] 审核医生：孙帅森\n[BBOX-390] 检测技师：朱龙华\n[BBOX-391] 肺功能报告单\n[BBOX-392] 姓名：\n[BBOX-393] 出生日期：1984/4/02\n[BBOX-394] 门诊/住院/体检：\n[BBOX-395] 身高：160 cm\n[BBOX-396] 身份证号：\n[BBOX-397] 性别：女\n[BBOX-398] 年龄：41岁\n[BBOX-399] 测试号：\n[BBOX-400] 体重：50 kg\n[BBOX-401] 测试日期\n[BBOX-402] 测试时间\n[BBOX-403] 预计\n[BBOX-404] 实测 % (实/预)\n[BBOX-405] 25/4/11\n[BBOX-406] 14:56:4\n[BBOX-407] VT\n[BBOX-408] [L]\n[BBOX-409] 0.36\n[BBOX-410] 0.41\n[BBOX-411] 114.9\n[BBOX-412] BF\n[BBOX-413] [1/min]\n[BBOX-414] 20.00\n[BBOX-415] 20.79\n[BBOX-416] 104.0\n[BBOX-417] MV\n[BBOX-418] [L/min]\n[BBOX-419] 7.14\n[BBOX-420] 8.54\n[BBOX-421] 119.5\n[BBOX-422] ERV\n[BBOX-423] [L]\n[BBOX-424] 1.07\n[BBOX-425] 1.07\n[BBOX-426] 99.4\n[BBOX-427] VC MAX\n[BBOX-428] [L]\n[BBOX-429] 3.19\n[BBOX-430] 2.84\n[BBOX-431] 88.9\n[BBOX-432] FVC\n[BBOX-433] [L]\n[BBOX-434] 3.13\n[BBOX-435] 2.84\n[BBOX-436] 90.6\n[BBOX-437] FEV 1\n[BBOX-438] [L]\n[BBOX-439] 2.70\n[BBOX-440] 1.53\n[BBOX-441] 56.9\n[BBOX-442] FEV 1 % FVC\n[BBOX-443] [%]\n[BBOX-444] 83.98\n[BBOX-445] 54.07\n[BBOX-446] 64.4\n[BBOX-447] FEV 1 % VC MAX\n[BBOX-448] [%]\n[BBOX-449] 81.31\n[BBOX-450] 54.07\n[BBOX-451] 66.5\n[BBOX-452] PEF\n[BBOX-453] [L/s]\n[BBOX-454] 6.46\n[BBOX-455] 4.56\n[BBOX-456] 70.7\n[BBOX-457] MEF 75\n[BBOX-458] [L/s]\n[BBOX-459] 5.73\n[BBOX-460] 1.84\n[BBOX-461] 32.1\n[BBOX-462] MEF 50\n[BBOX-463] [L/s]\n[BBOX-464] 4.06\n[BBOX-465] 0.84\n[BBOX-466] 20.7\n[BBOX-467] MEF 25\n[BBOX-468] [L/s]\n[BBOX-469] 1.77\n[BBOX-470] 0.28\n[BBOX-471] 15.6\n[BBOX-472] MMEF 75/25\n[BBOX-473] [L/s]\n[BBOX-474] 3.53\n[BBOX-475] 0.65\n[BBOX-476] 18.3\n[BBOX-477] FET\n[BBOX-478] [s]\n[BBOX-479] 8.46\n[BBOX-480] V backextrapolation ex\n[BBOX-481] [L]\n[BBOX-482] 0.03\n[BBOX-483] V backextrapol. % FVC\n[BBOX-484] [%]\n[BBOX-485] 1.23\n[BBOX-486] MVV\n[BBOX-487] [L/min]\n[BBOX-488] 101.93\n[BBOX-489] 75.75\n[BBOX-490] 74.3\n[BBOX-491] FEV 1*30\n[BBOX-492] [L/min]\n[BBOX-493] 101.93\n[BBOX-494] 46.03\n[BBOX-495] 45.2\n[BBOX-496] RV-SB\n[BBOX-497] [L]\n[BBOX-498] 1.55\n[BBOX-499] 2.56\n[BBOX-500] 164.9\n[BBOX-501] RV%TLC-SB\n[BBOX-502] [%]\n[BBOX-503] 32.90\n[BBOX-504] 47.52\n[BBOX-505] 144.4\n[BBOX-506] TLC-SB\n[BBOX-507] [L]\n[BBOX-508] 4.77\n[BBOX-509] 5.39\n[BBOX-510] 112.9\n[BBOX-511] FRC-SB\n[BBOX-512] [L]\n[BBOX-513] 2.63\n[BBOX-514] 3.31\n[BBOX-515] 126.0\n[BBOX-516] FRC%TLC-SB\n[BBOX-517] [%]\n[BBOX-518] 51.66\n[BBOX-519] 61.42\n[BBOX-520] 118.9\n[BBOX-521] DLCOc SB\n[BBOX-522] [mmol/min/kPa]\n[BBOX-523] 8.34\n[BBOX-524] 6.95\n[BBOX-525] 83.4\n[BBOX-526] DLCO SB\n[BBOX-527] [mmol/min/kPa]\n[BBOX-528] 8.34\n[BBOX-529] 6.95\n[BBOX-530] 83.4\n[BBOX-531] 医生意见：\n[BBOX-532] 1.中重度阻塞性通气功能障碍。\n[BBOX-533] 检查质量：FVC：A级。 FEV1：A级。\n[BBOX-534] 备注：受检者检查配合佳。 结果仅供参考，请结合临床分析。\n[BBOX-535] 2.最大自主分钟通气量（MVV）轻度下降。\n[BBOX-536] 备注：患者MVV配合佳。结果仅供参考，请结合临床分析。\n[BBOX-537] 3.弥散功能在正常范围。4.残总比中度增高。\n[BBOX-538] 审核医生：孙帅森\n[BBOX-539] 检测技师：张青苹\n[BBOX-540] 通气弥散B\n[BBOX-541] 2025/4/11 15:18\n[BBOX-542] 1/1\n[BBOX-543] 布地奈德 4ml Bid 3天\n[BBOX-544] 喷 3个月后复查肺功能。\n[BBOX-545] Vol [L]\n[BBOX-546] PredA0.0\n[BBOX-547] 0.2\n[BBOX-548] 0.4\n[BBOX-549] 0.6\n[BBOX-550] 0.8\n[BBOX-551] 1.0\n[BBOX-552] Time [min]\n[BBOX-553] Flow [L/s]\n[BBOX-554] F/V ex\n[BBOX-555] 10\n[BBOX-556] 5\n[BBOX-557] 0\n[BBOX-558] 2\n[BBOX-559] 4\n[BBOX-560] 6\n[BBOX-561] F/V in\n[BBOX-562] 10\n[BBOX-563] Vol [L]\n[BBOX-564] Vol [L]\n[BBOX-565] 100\n[BBOX-566] 10\n[BBOX-567] 50\n[BBOX-568] Time [s]\n[BBOX-569] 0\n[BBOX-570] 1\n[BBOX-571] 2\n[BBOX-572] 3\n[BBOX-573] 4\n[BBOX-574] 5\n[BBOX-575] Volume [L]\n[BBOX-576] 4\n[BBOX-577] 2\n[BBOX-578] 0\n[BBOX-579] M\n[BBOX-580] 0\n[BBOX-581] 2\n[BBOX-582] 4\n[BBOX-583] Time [s]\n[BBOX-584] 20\n[BBOX-585] 40\n[BBOX-586] 60\n[BBOX-587] 80\n[BBOX-588] 肺功能报告单\n[BBOX-589] 姓名：\n[BBOX-590] 性别：女\n[BBOX-591] 出生日期：1984/4/02\n[BBOX-592] 年龄：41岁\n[BBOX-593] 门诊/住院/体检：\n[BBOX-594] 测试号：\n[BBOX-595] 身高：160 cm\n[BBOX-596] 体重：50 kg\n[BBOX-597] 身份证号：\n[BBOX-598] 预计\n[BBOX-599] 实1 %(实1/预)\n[BBOX-600] 实2 %(实2/预)\n[BBOX-601] 变异率\n[BBOX-602] 测试日期\n[BBOX-603] 25/4/11\n[BBOX-604] 25/4/11\n[BBOX-605] 测试时间\n[BBOX-606] 14:56:47下午\n[BBOX-607] 15:14:32下午\n[BBOX-608] FVC\n[BBOX-609] [L]\n[BBOX-610] 3.13\n[BBOX-611] 2.84\n[BBOX-612] 90.6\n[BBOX-613] 3.05\n[BBOX-614] 97.4\n[BBOX-615] 7.5\n[BBOX-616] FEV 1\n[BBOX-617] [L]\n[BBOX-618] 2.70\n[BBOX-619] 1.53\n[BBOX-620] 56.9\n[BBOX-621] 1.91\n[BBOX-622] 71.0\n[BBOX-623] 24.7\n[BBOX-624] FEV 1 % FVC\n[BBOX-625] [%]\n[BBOX-626] 83.98\n[BBOX-627] 54.07\n[BBOX-628] 64.4\n[BBOX-629] 62.70\n[BBOX-630] 74.7\n[BBOX-631] 16.0\n[BBOX-632] FEV 1 % VC MAX\n[BBOX-633] [%]\n[BBOX-634] 81.31\n[BBOX-635] 54.07\n[BBOX-636] 66.5\n[BBOX-637] 62.70\n[BBOX-638] 77.1\n[BBOX-639] 16.0\n[BBOX-640] PEF\n[BBOX-641] [L/s]\n[BBOX-642] 6.46\n[BBOX-643] 4.56\n[BBOX-644] 70.7\n[BBOX-645] 5.64\n[BBOX-646] 87.3\n[BBOX-647] 23.6\n[BBOX-648] MEF 75\n[BBOX-649] [L/s]\n[BBOX-650] 5.73\n[BBOX-651] 1.84\n[BBOX-652] 32.1\n[BBOX-653] 2.65\n[BBOX-654] 46.3\n[BBOX-655] 44.3\n[BBOX-656] MEF 50\n[BBOX-657] [L/s]\n[BBOX-658] 4.06\n[BBOX-659] 0.84\n[BBOX-660] 20.7\n[BBOX-661] 1.23\n[BBOX-662] 30.4\n[BBOX-663] 47.0\n[BBOX-664] MEF 25\n[BBOX-665] [L/s]\n[BBOX-666] 1.77\n[BBOX-667] 0.28\n[BBOX-668] 15.6\n[BBOX-669] 0.44\n[BBOX-670] 25.0\n[BBOX-671] 60.2\n[BBOX-672] MMEF 75/25\n[BBOX-673] [L/s]\n[BBOX-674] 3.53\n[BBOX-675] 0.65\n[BBOX-676] 18.3\n[BBOX-677] 1.02\n[BBOX-678] 29.1\n[BBOX-679] 58.8\n[BBOX-680] FET\n[BBOX-681] [s]\n[BBOX-682] 8.46\n[BBOX-683] 6.41\n[BBOX-684] -24.2\n[BBOX-685] V backextrapolation ex [L]\n[BBOX-686] 0.03\n[BBOX-687] 0.06\n[BBOX-688] 71.7\n[BBOX-689] V backextrapol. % FVC [%]\n[BBOX-690] 1.23\n[BBOX-691] 1.96\n[BBOX-692] 59.6\n[BBOX-693] Flow [L/s]\n[BBOX-694] F/V ex\n[BBOX-695] 10\n[BBOX-696] 5\n[BBOX-697] 0\n[BBOX-698] 1\n[BBOX-699] 2\n[BBOX-700] 3\n[BBOX-701] 4\n[BBOX-702] 5\n[BBOX-703] 6\n[BBOX-704] 7\n[BBOX-705] 10\n[BBOX-706] F/V In\n[BBOX-707] 医生意见：\n[BBOX-708] 支气管舒张试验阳性。\n[BBOX-709] （通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后。\n[BBOX-710] FEV1较基线增加大于12%，且绝对值增加大于200ml。）\n[BBOX-711] 审核医生：孙帅森\n[BBOX-712] 检测技师：张青苹\n[BBOX-713] CS 扫描全能王\n[BBOX-714] 3亿人都在用的扫描App\n[BBOX-715] 院\n[BBOX-716] 入院记录\n[BBOX-717] 姓名：\n[BBOX-718] 科室：产科二区\n[BBOX-719] 床号：\n[BBOX-720] 科室：产科二区\n[BBOX-721] 第(1)次入院记录\n[BBOX-722] 过敏史：无\n[BBOX-723] 姓名：\n[BBOX-724] 性别：女\n[BBOX-725] 年龄：36岁\n[BBOX-726] 身份证号\n[BBOX-727] 职业：\n[BBOX-728] 婚姻：已婚\n[BBOX-729] 民族：汉族\n[BBOX-730] 出生地：\n[BBOX-731] 现住址：\n[BBOX-732] 入院日期：2020-07-08 08:36:09\n[BBOX-733] 邮编\n[BBOX-734] 病史采集时间：2020-07-08 08:36:09\n[BBOX-735] 联系人：\n[BBOX-736] 与病人关系：夫妻\n[BBOX-737] 病史叙述者：本人\n[BBOX-738] 联系人地址：同上地址\n[BBOX-739] 电话.\n[BBOX-740] 可靠程度：可靠\n[BBOX-741] 主诉：停经39周，要求住院待产。\n[BBOX-742] 现病史：平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日（阳历），预产\n[BBOX-743] 期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单活胎，发育符合\n[BBOX-744] 孕周。孕早期无早孕反应，孕早期无腹痛、出立，阴道流液，出血史，无放射线、有害物质接\n[BBOX-745] 触史。孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正常，孕中期行无创DNA\n[BBOX-746] 结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正常，未行糖耐量筛\n[BBOX-747] 查，未查B族链球菌。孕期经过顺利，孕晚期无头痛、头晕、眼花等症状，无皮肤黄染及痰\n[BBOX-748] 痒。现停经39周，无腹痛，未见红及破水，遂入院要求住院待产，门诊以“足月妊娠、瘢痕子\n[BBOX-749] 宫”收住院。自孕以来精神好，饮食、睡眠好，大小便正常，体重增加约10KG。\n[BBOX-750] 既往史：患者平素体健；否认有“心脏病、高血压、糖尿病、肾病”等慢性病史，否认有\n[BBOX-751] “肝炎、结核”等传染性疾病。于2016.08行剖宫产手术，否认余手术及外伤史。否认有输血\n[BBOX-752] 史，有献血史，否认食物及药物过敏史。预防接种随社会进行。\n[BBOX-753] 个人史：出生于原籍，护士，本科文化，工作于三门峡市中心医院。否认长期外地居住\n[BBOX-754] 史，无疫区居住史，无烟酒等不良嗜好。生长环境一般，否认有冶游史。\n[BBOX-755] 婚育史：31岁结婚，爱人\n[BBOX-756] 现年37岁，职员，工作于三门峡市党校，身体健康，无吸\n[BBOX-757] 烟史，有饮酒史，否认“肝炎、结核”病史，夫妻感情好。孕;产;，2016年足月剖宫产1活男\n[BBOX-758] 婴，现体健，否认产后出血及产褥感染史，否认不良孕产史。\n[BBOX-759] 月经史：平素月经规律，12岁，5-7天/30-35天，末次月经为：2019年10月08日（阳\n[BBOX-760] 历），量中等，色暗红，偶有血块，无痛经。\n[BBOX-761] 页\n[BBOX-762] 书写者签名：\n[BBOX-763] 总第 页\n[BBOX-764] 院\n[BBOX-765] 入院记录\n[BBOX-766] 姓名:\n[BBOX-767] 科室:产科二区\n[BBOX-768] 床号:\n[BBOX-769] 生.\n[BBOX-770] 家族史:父母亲体健,1弟1妹均体健,1子体健,否认家族中有遗传性及传染性疾病史。\n[BBOX-771] 体格检查\n[BBOX-772] 体温:36.5℃\n[BBOX-773] 脉搏:78次/分\n[BBOX-774] 呼吸:18次/分\n[BBOX-775] 血压:98/64mmHg\n[BBOX-776] 身高160cm\n[BBOX-777] 体重:60Kg\n[BBOX-778] 一般状况:发育正常;营养中等;自动体位:面色红润;面容及表情自如;神志清晰;言\n[BBOX-779] 语状态流利;检查时能合作等。\n[BBOX-780] 皮肤:色泽正常,弹性正常,无水肿、出汗、紫癜、皮疹、色素沉着、蜘蛛痣、瘢痕、创\n[BBOX-781] 伤、溃疡、结节。\n[BBOX-782] 淋巴结:全身或局部表浅淋巴结未触及肿大;局部皮肤无红热、瘘管、瘢痕。\n[BBOX-783] 头部:\n[BBOX-784] 头颅:大小无异常、外形无异常;眉发分布正常;无疖、痈、外伤、瘢痕、肿块。\n[BBOX-785] 眼部:双眼裂正常,双眼睑无水肿,眼球运动正常。瞳孔:左3.0mm直接对光反应灵敏,\n[BBOX-786] 间接对光反应灵敏;右3.0mm直接对光反应灵敏,间接对光反应灵敏。视力粗测正常。\n[BBOX-787] 耳部:耳廓无畸形,外耳道无分泌物,乳突无压痛,听力粗测5米。\n[BBOX-788] 鼻部:无畸形、鼻翼扇动、阻塞、分泌物、鼻中隔异常、嗅觉障碍、鼻窦压痛等。\n[BBOX-789] 口腔:口唇红润,无畸形、疱疹、微血管搏动、口角皲裂;牙齿无缺损、龋病、镶补等异\n[BBOX-790] 常;牙龈无溢血、溢脓、萎缩、色素沉着;口腔粘膜无溃疡、假膜、色素沉着;扁桃体无肿\n[BBOX-791] 大、分泌物;咽部无充血、分泌物。\n[BBOX-792] 颈部:对称,无强直、压痛、运动受限、颈静脉怒张、颈动脉明显搏动、肿块,气管居\n[BBOX-793] 中,甲状腺无肿大。\n[BBOX-794] 胸部\n[BBOX-795] 胸廓:形状正常,对称,运动程度正常,肋间正常,胸壁无水肿、皮下气肿、肿块、静脉\n[BBOX-796] 曲张,肋骨及肋软骨无压痛、凹陷等异常。乳头,正常。\n[BBOX-797] 肺脏:视诊:腹式呼吸,呼吸节律正常,呼吸深度正常,两侧呼吸运动对称。\n[BBOX-798] 触诊:语音震颤两侧相等,无摩擦感。\n[BBOX-799] 叩诊:叩诊声响清音,肺下界肩胛线在第10肋间,呼吸移动度6cm,\n[BBOX-800] 听诊:呼吸音性质为肺泡呼吸音,强度正常,语音传导正常,无摩擦音、哮鸣音、\n[BBOX-801] 第页\n[BBOX-802] 书写者签名:\n[BBOX-803] 总第页\n[BBOX-804] 院\n[BBOX-805] 入院记录\n[BBOX-806] 姓名：\n[BBOX-807] 科室：产科二区\n[BBOX-808] 床号\n[BBOX-809] 病号：\n[BBOX-810] 干啰音、湿啰音。\n[BBOX-811] 心脏：视诊：心尖搏动的位置在左侧锁骨中线内第4肋间，范围为2.5cm，强度正常，心前\n[BBOX-812] 区无异常搏动、局限性膨隆。\n[BBOX-813] 触诊：心尖搏动最强部位在左侧锁骨中线第4肋间，范围为2.5cm，无抬举性搏动、\n[BBOX-814] 震颤、摩擦感。\n[BBOX-815] 叩诊：左右心界线以每肋间距胸骨中线的cm数记载。\n[BBOX-816] 右cm\n[BBOX-817] 肋间\n[BBOX-818] 左cm\n[BBOX-819] 2\n[BBOX-820] Ⅱ\n[BBOX-821] 2.5\n[BBOX-822] 2\n[BBOX-823] Ⅲ\n[BBOX-824] 4\n[BBOX-825] 3\n[BBOX-826] Ⅳ\n[BBOX-827] 5.5\n[BBOX-828] V\n[BBOX-829] 8\n[BBOX-830] 左锁骨中线至前正中线的距离9cm。\n[BBOX-831] 听诊：心率78次/分，心律整齐，无心脏杂音，无第三心音、第四心音、心音分\n[BBOX-832] 裂，P2<A2。\n[BBOX-833] 血管：桡动脉搏动正常，血管壁硬度正常。\n[BBOX-834] 周围血管征：无毛细血管搏动征、水冲脉、枪击音、动脉异常搏动。\n[BBOX-835] 腹部：\n[BBOX-836] 视诊：腹部膨隆，晓孕腹型，腹壁对称，无凹陷、膨隆、静脉曲张、蠕动波、局限性隆\n[BBOX-837] 起，下腹可见一长约15cm横行手术疤痕。\n[BBOX-838] 触诊：腹壁柔软，无压痛，无反跳痛；未触及肿块，无搏动、波动感等。肝脏：肋缘下未\n[BBOX-839] 触及，无压痛。胆囊：未触及，无压痛。脾脏：肋缘下未触及。肾：未触及，无压痛等。\n[BBOX-840] 叩诊：肝上界位于第5肋间，肝浊音界正常，肝区无叩击痛、脾区无叩击痛、腹部无过度\n[BBOX-841] 鼓音，移动性浊音阴性。\n[BBOX-842] 听诊：肠蠕动音正常，频率4次/分，胃区无振水声，肝区无摩擦音、脾区无摩擦音，无血\n[BBOX-843] 管杂音。\n[BBOX-844] 外阴及肛门：阴毛分布正常；外生殖器发育正常，肛门检查：无外痔、肛裂、肛瘘、脱\n[BBOX-845] 肛、湿疣等。\n[BBOX-846] 脊柱：脊柱无畸形、压痛、叩击痛；脊柱两侧肌肉无紧张、压痛；肋脊角无压痛、叩痛。\n[BBOX-847] 四肢：无畸形、杵状指（趾）、静脉曲张、外伤、骨折；肌肉张力正常与肌力5级，无萎\n[BBOX-848] 院\n[BBOX-849] 入院记录\n[BBOX-850] 姓名.\n[BBOX-851] 科室:产科二区\n[BBOX-852] 床号\n[BBOX-853] 住院号.\n[BBOX-854] 缩;关节无红肿、畸形、运动障碍,双下肢水肿。\n[BBOX-855] 神经反射:膝腱反射正常、跟腱反射正常、肱二头肌腱反射正常、肱三头肌腱反射正常、\n[BBOX-856] 腹壁反射正常、巴彬斯基征阴性、克尼格征阴性等。\n[BBOX-857] 专科情况\n[BBOX-858] 宫高34CM,腹围102CM,估计胎儿体重:3200g,胎位:头位,胎心152次/分,律齐,无\n[BBOX-859] 宫缩,未见红,未破水,骨盆外测量及内诊:未做。\n[BBOX-860] 辅助检查\n[BBOX-861] B超(2020.07.02 本院):晓孕宫内单活胎头位(双顶径9.4cm,股骨长7.0cm羊水指\n[BBOX-862] 数8.5cm),胎盘成熟度II°.\n[BBOX-863] 初步诊断:\n[BBOX-864] 1.妊娠合并子宫瘢痕;\n[BBOX-865] 3.孕2产,宫内孕39周头位待产。\n[BBOX-866] 主治医师:\n[BBOX-867] 孙小丹\n[BBOX-868] 副主任医师:\n[BBOX-869] 彭琼玉\n[BBOX-870] 2020.07.08\n[BBOX-871] CS 扫描全能王\n[BBOX-872] 3亿人都在用的扫描App\n[BBOX-873] 姓名：\n[BBOX-874] 科室：产科二区\n[BBOX-875] 床号\n[BBOX-876] 住院号.\n[BBOX-877] 2020年07月08日 09时22分\n[BBOX-878] 首次病程记录\n[BBOX-879] 患\n[BBOX-880] 女，36岁，汉族，-以“停经39周，要求住院待产”为主诉于\n[BBOX-881] 2020-07-08 08:36:09入院。一、病例特点：1、已婚育龄妇女，孕₂产₁，否认产后出血及产褥\n[BBOX-882] 感染史，否认不良孕产史；2、平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日\n[BBOX-883] (阳历)，预产期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单\n[BBOX-884] 活胎，发育符合孕周。3、孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正\n[BBOX-885] 常，孕中期行无创DNA结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正\n[BBOX-886] 常，未行糖耐量筛查，未查B族链球菌。4、现停经39周，无腹痛，未见红及破水，遂入院要求\n[BBOX-887] 住院待产。5.入院查体：T：36.5℃，P：78次/分，R：18次/分，BP：98/64mmHg。神志清楚，\n[BBOX-888] 精神好，全身皮肤粘膜无黄染，浅表淋巴结未触及，心肺听诊未闻及明显异常，腹膨隆。6、\n[BBOX-889] 专科检查：宫高34CM，腹围102CM，估计胎儿体重：3200g，胎位：头位，胎心152次/分，律\n[BBOX-890] 齐，无宫缩，未见红，未破水，骨盆外测量及内诊：未做。7、辅助检查：B超（2020.07.02\n[BBOX-891] 本院）：晚孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度\n[BBOX-892] II°。二、拟诊讨论：（一）初步诊断：1.妊娠合并子宫瘢痕；2.孕₂产；宫内孕39周头位\n[BBOX-893] 待产。（二）诊断依据：1、患者有停经史，平素月经规律，平素月经规律，5-7天/35-36天，\n[BBOX-894] 末次月经为：2019年10月08日（阳历），预产期为2020年07月15日（阳历），停经后有自觉胎\n[BBOX-895] 动，产前检查可同及胎心；2、专科检查：宫高34CM，腹围102CM，估计胎儿体重：3200g，胎\n[BBOX-896] 位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水。骨盆外测量及内诊：未做。3、\n[BBOX-897] 辅助检查：B超（2020.07.02本院）：晚孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm\n[BBOX-898] 羊水指数8.5cm)，胎盘成熟度II°。（三）鉴别诊断：根据据病史、查体及辅助检查，目前诊\n[BBOX-899] 断明确。三、诊疗计划：完善各项检查：心电图、彩超、血常规、血型、凝血五项、输血前检\n[BBOX-900] 查、尿常规、心电图、肝功、肾功、血糖、电解质等；2、向患者及家属交代病情，围生期相\n[BBOX-901] 关危险因素；3，给予巡视病房、监测胎心、心理疏导，消除围产期恐惧心理等产前护理；4、\n[BBOX-902] 患者要求明日剖宫产，纳入剖宫产临床路径。\n[BBOX-903] 主治医师：孙州\n[BBOX-904] 2020年07月08日 10时22分\n[BBOX-905] 科主任宋瑞香主治医师查房记录\n[BBOX-906] 第页\n[BBOX-907] 总第页\n[BBOX-908] 姓名：\n[BBOX-909] 科室：产科二区\n[BBOX-910] 床号：\n[BBOX-911] 住院号\n[BBOX-912] 今日随科主任宋瑞香主治医师查房，患者精神好，饮食及夜眠可，大小便正常，未破\n[BBOX-913] 水，未见红，无腹痛。查体：生命体征平稳，心肺听诊未闻及明显异常，胎心波动于正常范\n[BBOX-914] 围，无宫缩。目前诊断：1.妊娠合并于宫瘢痕；2.孕2产；宫内孕39周头位待产。诊断依\n[BBOX-915] 据：1.停经后有自觉胎动，产前检查可闻及胎心。2、查体：宫高34CM，腹围102CM，估计胎儿\n[BBOX-916] 体重：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水。骨盆外测量及\n[BBOX-917] 内诊：未做。3、辅助检查：B超（2020.07.02 本院）：晓孕宫内单活胎头位(双顶径\n[BBOX-918] 9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。科主任宋瑞香主治医师查房指示：\n[BBOX-919] 患者孕足月、瘢痕子宫，若阴道分娩易出现先兆子宫破裂、子宫破裂、胎死宫内等情况，患者\n[BBOX-920] 及其家属表示理解，要求明日剖宫产终止妊娠，完善术前谈话，积极术前准备，严密监测胎心\n[BBOX-921] 变化。以上医嘱已执行。\n[BBOX-922] 主治医师：主治医师：\n[BBOX-923] 孙丹\n[BBOX-924] 2020年07月08日 10：20\n[BBOX-925] 术前小结\n[BBOX-926] 姓名：\n[BBOX-927] 性别：女，年龄：36岁；\n[BBOX-928] 病历摘要：以“伴经39周，要求住院待产”为主诉入院。孕2产，否认产后出血及产褥感\n[BBOX-929] 染史，否认不良孕产史。查体：生命体征平稳，心肺听诊未闻及异常。腹隆，晚孕腹型。肝脾\n[BBOX-930] 肋下未触及，下腹部可见一长约15cm的横行手术瘢痕。双下肢无水肿；专科检查：宫高34CM，\n[BBOX-931] 腹围102CM，估计胎儿体重：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未\n[BBOX-932] 破水。骨盆外测量及内诊：未做。辅助检查：B超（2020.07.02 本院）：晓孕宫内单活胎\n[BBOX-933] 头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。入院后要求剖宫产终止\n[BBOX-934] 妊娠，手术相关风险已向其讲明，并在手术同意书上签字。请示科主任宋瑞香副主任医师，同\n[BBOX-935] 意安排手术，手术医师宋瑞香主治医师查看病人，生命体征平稳，无手术禁忌，积极术前准\n[BBOX-936] 备。\n[BBOX-937] 术前诊断：1.妊娠合并子宫瘢痕；2.孕2产；宫内孕39周头位待产。\n[BBOX-938] 手术指证：足月妊娠，瘢痕子宫，患者及家属要求，无手术禁忌症：\n[BBOX-939] 拟施手术名称和方式：拟定于明日07：30行二次子宫下段剖宫产术；\n[BBOX-940] 拟施麻醉：椎管内麻醉；\n[BBOX-941] 第 页\n[BBOX-942] 总第 页\n[BBOX-943] 姓名：\n[BBOX-944] 科室：产科二区\n[BBOX-945] 床号：\n[BBOX-946] 注意事项：规范操作，彻底止血，待新生儿娩出后，给予“缩宫素针”促宫缩治疗，做好\n[BBOX-947] 新生儿复苏工作。\n[BBOX-948] 主治医师：孙丹丹\n[BBOX-949] 第 页\n[BBOX-950] 总第 页\n[BBOX-951] 院\n[BBOX-952] 姓名：\n[BBOX-953] 科室：产科二区\n[BBOX-954] 床：\n[BBOX-955] 住院号：\n[BBOX-956] 2020年07月09日 09时47分\n[BBOX-957] 术后首次病程记录\n[BBOX-958] 患者术前测胎心150次/分，于今日08：29-09：30在腰硬联合麻醉+基础麻醉下行二次子宫\n[BBOX-959] 下段剖宫产术+子宫修补术，取下腹原横切口，剔除原瘢痕，逐层进腹，膀下指膀胱，暴露子\n[BBOX-960] 宫下段，可见于宫下段肌层较薄，胎儿头发及胎脂漂浮，切开子宫后见羊水清，约600ml，吸\n[BBOX-961] 净后以头位助娩一活男婴，出生1-10分钟均评10分，胎盘胎膜自娩完整，子宫收缩可，纱布球\n[BBOX-962] 擦拭子宫腔，可见子宫下段肌层断裂，用可吸收线间断缝合子宫下段肌层，断裂的血管给予缝\n[BBOX-963] 合，以恰桥可吸收线分两层连续缝合子宫切口。探查子宫切口无活动性出血，双侧附件外观正\n[BBOX-964] 常，关腹。术程顺利，术中麻醉好，呼吸血压平稳，输入晶体液800ml，胶体液0ml，出血不\n[BBOX-965] 多，约200ml，尿色清，量约100ml，术中诊断：1.妊娠合并子宫瘢痕；2.孕2产：宫内孕39*1周\n[BBOX-966] 头位剖宫产；术后安返病房，测P：64次/分，R：18次/分，Bp：84/54mmHg，术后给予“头\n[BBOX-967] 孢唑林钠针”预防感染、加强宫缩、会阴冲洗、尿管护理及支持对症等治疗，并嘱其按摩双下\n[BBOX-968] 肢预防下肢静脉血栓形成，注意观察生命体征、子宫收缩及阴道出血情况。\n[BBOX-969] 住院医师：冯雪云\n[BBOX-970] 2020年07月10日 09时00分\n[BBOX-971] 彭琼玉副主任医师查房记录\n[BBOX-972] 今日为剖宫产术后一天，患者精神、睡眠好，无特殊不适，未排气。彭琼玉副主任医师\n[BBOX-973] 查房：查体：生命体征平稳，双乳不胀，无泌乳，心肺未闻及异常，腹软，腹部切口皮肤对合\n[BBOX-974] 好，未见红肿、硬结等异常，宫底平脐，子宫收缩好，阴道出血不多，尿管畅，尿色清，尿量\n[BBOX-975] 正常，余查无特殊，查房意见：现术后一天，未排气，流食，体温正常，切口无感染迹象，病\n[BBOX-976] 情无特殊，继续抗炎补液加强宫缩等治疗；嘱患者床上多翻身并按摩双下肢，以防术后肠粘连\n[BBOX-977] 及栓塞性疾病发生，给予肌注缩宫素10uBID促进子宫收缩，给予子宫复旧磁疗促进产后子宫\n[BBOX-978] 恢复，嘱保持乳房畅通，并给予泌乳磁疗促进乳汁分泌，输完液体后拔除尿管，适当下床活\n[BBOX-979] 动，注意监测血糖情况，上述指示已执行。\n[BBOX-980] 副主任医师：马\n[BBOX-981] 住院医师：冯雪云\n[BBOX-982] 2020年07月11日 08时06分\n[BBOX-983] 术后第二天，患者无发热，已排气，尿管拔除后排尿畅。查体：生命体征平稳，心肺听诊\n[BBOX-984] 第 页\n[BBOX-985] 总第 页\n[BBOX-986] 出院\n[BBOX-987] 姓名：\n[BBOX-988] 科室：产科二区\n[BBOX-989] 床号\n[BBOX-990] 住院\n[BBOX-991] 未闻及异常，双乳泌乳量不多，腹软，子宫收缩好，宫底位于脐下两横指，无压痛，阴道出血\n[BBOX-992] 不多，暗红色，无异味，腹部切口换药见切口皮缘对合好，未见红肿、硬结及渗液等异常，双\n[BBOX-993] 下肢无水肿，现术后第二天，病情稳定，改为II级护理，已排气给予昔食，注意体温变化及切\n[BBOX-994] 口情况；继续予子宫复旧磁疗促进产后子宫恢复，加用腹部切口红外线治疗促进伤口愈合，加\n[BBOX-995] 益宫颗粒(自各药物)促宫缩治疗，观察体温及阴道恶露情况。\n[BBOX-996] 主治医师：孙丹丹\n[BBOX-997] 2020年07月12日10时00分\n[BBOX-998] 彭琼玉副主任医师查房记录\n[BBOX-999] 今日查房，患者剖宫产术后三天，患者未诉不适，精神好，饮食、睡眠正常，查体：生\n[BBOX-1000] 命体征平稳，心肺听诊未闻及异常，双乳泌乳量多，腹软，腹部切口无红肿、硬结、渗液等异\n[BBOX-1001] 常，子宫收缩好，阴道出血不多，余查无特殊，再次复查血常规：白细胞10.59×10⁹/L，中性\n[BBOX-1002] 粒细胞86.3%，偏高，血红蛋白100g/L，患者复查白细胞正常，中性粒细胞偏高，体温正常，\n[BBOX-1003] 切口无感染迹象，考虑术后炎性反应，暂不特殊处理，嘱加强营养，加强运动。彭琼玉副主任\n[BBOX-1004] 医师查房指示：患者现病情稳定，腹部伤口皮内结合，无需拆线，达临床治愈，顺利完成剖宫\n[BBOX-1005] 产临床路径管理，今日办理出院。指示已执行。\n[BBOX-1006] 副主任医师：彭琼玉\n[BBOX-1007] 主治医师：孙丹丹\n[BBOX-1008] 出院记录\n[BBOX-1009] 姓名\n[BBOX-1010] 科室：产科二区\n[BBOX-1011] 床号.\n[BBOX-1012] 住院号.\n[BBOX-1013] 2020年07月12日\n[BBOX-1014] 出院记录\n[BBOX-1015] 患者.\n[BBOX-1016] 36岁\n[BBOX-1017] 住院号：\n[BBOX-1018] 入院日期：2020-07-08 08:36:09\n[BBOX-1019] 出院日期：2020年07月12日\n[BBOX-1020] 住院天数：4天\n[BBOX-1021] 入院情况：以“停经39周，要求住院待产”为主诉入院。入院查体：生命体征平稳，心肺\n[BBOX-1022] 听诊未闻及异常。腹隆，晚孕腹型，肝脾肋下未触及。专科检查：宫高34CM，腹围102CM，估\n[BBOX-1023] 计胎儿体宣：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水，骨盆外\n[BBOX-1024] 测量及内诊：未做。辅助检查：B超（2020.07.02 本院）：晚孕宫内单活胎头位(双顶径\n[BBOX-1025] 9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。\n[BBOX-1026] 入院诊断：1.妊娠合并子宫瘢痕；2.孕产：宫内孕39周头位待产。\n[BBOX-1027] 诊疗经过：患者入院后完善相关检查，要求剖宫产，于2020年07月09日 08：29-09：30在\n[BBOX-1028] 腰硬联合麻醉+基础麻醉下行二次于宫下段剖宫产术+子宫修补术。取下腹原横切口，剔除原瘢\n[BBOX-1029] 痕，逐层进腹，膀下指膀胱，暴露子宫下段，可见子宫下段肌层较薄，胎儿头发及胎脂漂浮，\n[BBOX-1030] 切开子宫后见羊水清，约600ml，吸净后以头位助娩一活男婴，出生1-10分钟均评10分，胎盘\n[BBOX-1031] 胎膜自娩完整，子宫收缩可，纱布球擦拭子宫腔，可见子宫下段肌层断裂，用可吸收线间断缝\n[BBOX-1032] 合子宫下段肌层，断裂的立皆给予缝合，以伦桥可吸收线分两层连续缝合子宫切口。探查子宫\n[BBOX-1033] 切口无活动性出血，双侧附件外观正常，关腹，术程顺利，术中出血不多，术后予以降压、抗\n[BBOX-1034] 感染、加强宫缩支持及对症治疗。\n[BBOX-1035] 出院诊断：1.妊娠合并子宫瘢痕；2.孕产：宫内孕39+周头位剖宫产：\n[BBOX-1036] 出院情况：患者精神、饮食好，无特殊不适。查体：生命体征平稳，心肺听诊未闻及明显\n[BBOX-1037] 异常，双乳泌乳量可，双乳稍涨，腹部平软，切口无红肿、渗出、硬结等愈合良好，子宫收缩\n[BBOX-1038] 好，宫底约脐耻之间，宫体无压痛，恶露呈淡红色，量少，无异味。现患者一般情况好，双乳\n[BBOX-1039] 泌乳量多，子宫复旧好，腹部切口愈合良好，无需拆线，达临床治愈，于今日出院。完成计划\n[BBOX-1040] 性剖宫产临床路径。\n[BBOX-1041] 出院医嘱：1.注意休息，合理营养；\n[BBOX-1042] 2.禁性生活、盆浴及重体力劳动2个月；\n[BBOX-1043] 3.坚持纯母乳喂养大于4-6月；\n[BBOX-1044] 第 页\n[BBOX-1045] 总第 页\n[BBOX-1046] 医院\n[BBOX-1047] 出院记录\n[BBOX-1048] 姓名：\n[BBOX-1049] 科室：产科二区\n[BBOX-1050] 床号：\n[BBOX-1051] 住院号：2\n[BBOX-1052] 4.产后42天门诊复查，如出院后出现任何异常情况请立即就诊，注意产妇心理\n[BBOX-1053] 状态，必要时心理咨询门诊就诊；若阴道出血淋漓不尽持续1月或阴道出血量多于平素月经\n[BBOX-1054] 量、腹痛、发热等，及时就诊：（每周二、周六门诊326彭琼玉副主任医师坐诊）\n[BBOX-1055] 5.严格避孕，术后六个月可安环避孕，术后2年以上方可再次妊娠：\n[BBOX-1056] 6.新生儿乙肝疫苗第一针，卡介苗已接种，新生儿生后10天补充维生素AD滴剂\n[BBOX-1057] 1粒/次，一次/日（至2岁），出院后新生儿每日测胆红素值，黄疸加重或持续14天未消退，或\n[BBOX-1058] 出院后有不适，可直接到1号楼9楼新生儿科探视大厅就诊（携带宝宝就诊卡）；\n[BBOX-1059] 7.咨询电话产科：\n[BBOX-1060] ，新生儿科：0398-3118382。母乳咨询电话：\n[BBOX-1061] 0398-3118618.\n[BBOX-1062] 主治医师：\n[BBOX-1063] 孙州\n[BBOX-1064] 临床数据中心-患者360视图\n[BBOX-1065] 返回患者查询\n[BBOX-1066] 患者姓名\n[BBOX-1067] 女 出生日\n[BBOX-1068] 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>\n[BBOX-1069] 就诊时间轴\n[BBOX-1070] 门诊号\n[BBOX-1071] 诊时间：2023-08-14 15:29:02 接诊科室：普通儿科三组（门） 接诊医生：谭真真\n[BBOX-1072] 全部\n[BBOX-1073] 近一月\n[BBOX-1074] 近三月\n[BBOX-1075] 近半年\n[BBOX-1076] 近一年\n[BBOX-1077] 近五年\n[BBOX-1078] 门诊39 住院1\n[BBOX-1079] 总览\n[BBOX-1080] 就诊列表\n[BBOX-1081] 2024-04-24 普通儿科一组（...\n[BBOX-1082] 2024-04-19 普通儿科一组（...\n[BBOX-1083] 2024-04-08 妇科门诊\n[BBOX-1084] 2024-04-08 妇科一病区(门)\n[BBOX-1085] 2024-01-05 妇科一病区(门)\n[BBOX-1086] 2023-08-14 普通儿科三组（...\n[BBOX-1087] 2023-07-06 普通儿科三组（...\n[BBOX-1088] 2023-06-26 普通儿科三组（...\n[BBOX-1089] 2023-05-08 普通儿科三组（...\n[BBOX-1090] 2023-05-08 普通儿科一组（...\n[BBOX-1091] 2023-04-18 普通儿科三组（...\n[BBOX-1092] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告\n[BBOX-1093] 1.\n[BBOX-1094] 门诊号.\n[BBOX-1095] 姓名：\n[BBOX-1096] 性别：女\n[BBOX-1097] 年龄：39岁\n[BBOX-1098] 民族：汉族\n[BBOX-1099] 身份证\n[BBOX-1100] 现住址：\n[BBOX-1101] 就诊类型：初诊\n[BBOX-1102] 就诊科室：普通儿科三组（门）\n[BBOX-1103] 就诊日期：2023-08-14 15:29\n[BBOX-1104] 联系电\n[BBOX-1105] 主诉：咽峡炎购药\n[BBOX-1106] 现病史：咽峡炎购药\n[BBOX-1107] 既往史：平素体健，无肝炎、结核类传染病史\n[BBOX-1108] 过敏史：无\n[BBOX-1109] 体格检查：发育正常，营养良好，精神一般，口唇红润，双侧扁桃体无肿大，无充血、分泌物。咽腔黏膜无充\n[BBOX-1110] 血、红肿、疱疹，双肺呼吸音清，听诊心律齐，无杂音，腹平软，无压痛、反跳痛\n[BBOX-1111] 辅助检查：\n[BBOX-1112] 初步印象：急性咽峡炎\n[BBOX-1113] 处理意见：门诊\n[BBOX-1114] 备注：\n[BBOX-1115] 医师签名：谭真真\n[BBOX-1116] 第1页\n[BBOX-1117] 门诊病历\n[BBOX-1118] 门诊号：\n[BBOX-1119] 姓名\n[BBOX-1120] 性别：女\n[BBOX-1121] 年龄：39岁\n[BBOX-1122] 民族：汉族\n[BBOX-1123] 身份证号\n[BBOX-1124] 现住址：\n[BBOX-1125] 就诊类型：急诊\n[BBOX-1126] 就诊科室：妇科一病区(门)\n[BBOX-1127] 就诊日期：2024-01-05 10:32\n[BBOX-1128] 联系电话\n[BBOX-1129] 主诉：下腹痛2小时\n[BBOX-1130] 现病史：患者月经第二天，无明显诱因出现下腹持续疼痛\n[BBOX-1131] 既往史：平素体健，无高血压、冠心病、糖尿病病史，无肝炎、结核等传染病史，无手术史\n[BBOX-1132] 婚育史：\n[BBOX-1133] 月经史：患者平素月经规律，量中等，色正常，无痛经。\n[BBOX-1134] 过敏史：无\n[BBOX-1135] 专科检查：外阴：发育正常，阴毛呈女性分布；阴道：通畅，粘膜红润，未见异常分泌物；宫颈：光滑，大小正常，宫体：正常大小，无压痛。附件：左侧附件区压痛明显。\n[BBOX-1136] 辅助检查：\n[BBOX-1137] 初步印象：女性盆腔炎性疾病\n[BBOX-1138] 处理意见：门诊治疗\n[BBOX-1139] 备注：\n[BBOX-1140] 医师签名：汪会芳\n[BBOX-1141] 第1页\n[BBOX-1142] 三门峡市中心医院门户-患者360 ×\n[BBOX-1143] ← → C ① 不安全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-1144] 临床数据中心-患者360视图\n[BBOX-1145] 返回患者查询 患者姓名:\n[BBOX-1146] 女 出\n[BBOX-1147] 期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>\n[BBOX-1148] 就诊时间轴\n[BBOX-1149] 门诊号\n[BBOX-1150] 就诊时间: 2024-04-08 09 44 02 接诊科室: 妇科一病区(门) 接诊医生: 权丽丽\n[BBOX-1151] 全部 近一月 近三月 近半年 近一年\n[BBOX-1152] 近五年\n[BBOX-1153] 门诊39 住院1\n[BBOX-1154] 总览 就诊列表\n[BBOX-1155] 2025-04-11 哮喘危重—病达(I J)\n[BBOX-1156] 2025-01-06 普通儿科三组 (...\n[BBOX-1157] 2024-12-30 普通儿科三组 (...\n[BBOX-1158] 2024-07-05 普通儿科一组 (...\n[BBOX-1159] 2024-04-24 普通儿科一组 (...\n[BBOX-1160] 2024-04-19 普通儿科一组 (...\n[BBOX-1161] 2024-04-08 妇科门诊\n[BBOX-1162] 2024-04-08 妇科一病区(门)\n[BBOX-1163] 2024-01-05 妇科一病区(门)\n[BBOX-1164] 2023-08-14 普通儿科三组 (...\n[BBOX-1165] 2023-07-06 普通儿科三组 (...\n[BBOX-1166] 集放视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告\n[BBOX-1167] 检验报告\n[BBOX-1168] 门诊号:\n[BBOX-1169] 姓名\n[BBOX-1170] 性别: 女\n[BBOX-1171] 年龄:40岁\n[BBOX-1172] 民族: 汉族\n[BBOX-1173] 身份证号\n[BBOX-1174] 现住址:\n[BBOX-1175] 就诊类型:初诊\n[BBOX-1176] 就诊科室:妇科一病区(门)\n[BBOX-1177] 就诊日期: 2024-04-08 09:44\n[BBOX-1178] 联系电话\n[BBOX-1179] 主诉:月经期下腹间断疼痛2个月\n[BBOX-1180] 现病史:2024.1月经第3天左侧附件区疼痛,超声提示无异常,输消炎药后好转,2024.2无异常,2024.3月经第3天下腹疼痛但是疼痛程度较前减轻,\n[BBOX-1181] 既往史:平素体健,无高血压、冠心病、糖尿病病史,无肝炎、结核等传染病史,无手术史\n[BBOX-1182] 婚育史:\n[BBOX-1183] 月经史:患者平素月经规律,量中等,色正常,无痛经。\n[BBOX-1184] 过敏史:无\n[BBOX-1185] 专科检查:外阴:发育正常,阴毛呈女性分布;阴道:通畅,粘膜红润,未见异常分泌物;宫颈:光滑,大小正常,宫体:正常大小,无压痛。附件:双侧附件区未触及明显异常。\n[BBOX-1186] 辅助检查:\n[BBOX-1187] 初步印象:女性盆腔炎性疾病\n[BBOX-1188] 处理意见:门诊检查\n[BBOX-1189] 备注:\n[BBOX-1190] 医师签名:权丽丽\n[BBOX-1191] 第1页\n[BBOX-1192] 三门峡市中心医院门户-患者360 ×\n[BBOX-1193] 临床数据中心-患者360视图\n[BBOX-1194] 返回患者查询\n[BBOX-1195] 患者姓\n[BBOX-1196] 出生\n[BBOX-1197] 期：2020-07-08\n[BBOX-1198] 最近诊疗日期：2026-02-12\n[BBOX-1199] 当前在院状态：出院\n[BBOX-1200] 过敏：无\n[BBOX-1201] 详情>>\n[BBOX-1202] 就诊时间抽\n[BBOX-1203] 1J号：\n[BBOX-1204] 就诊时间：2024-04-08 11:32:46\n[BBOX-1205] 接诊科室：妇科门诊\n[BBOX-1206] 接诊医生：曲丽霞\n[BBOX-1207] 全部\n[BBOX-1208] 近一月\n[BBOX-1209] 近三月\n[BBOX-1210] 近半年\n[BBOX-1211] 近一年\n[BBOX-1212] 近五年\n[BBOX-1213] 门诊诊39\n[BBOX-1214] 住院1\n[BBOX-1215] 总览\n[BBOX-1216] 就诊列表\n[BBOX-1217] 2025-04-11 收敛厄重_病区(1)\n[BBOX-1218] 2025-01-06 普通儿科三组(...\n[BBOX-1219] 2024-12-30 普通儿科三组(...\n[BBOX-1220] 2024-07-05 普通儿科一组(...\n[BBOX-1221] 2024-04-24 普通儿科一组(...\n[BBOX-1222] 2024-04-19 普通儿科一组(...\n[BBOX-1223] 2024-04-08 妇科门诊\n[BBOX-1224] 2024-04-08 妇科一病区(门)\n[BBOX-1225] 2024-01-05 妇科一病区(门)\n[BBOX-1226] 2023-08-14 普通儿科三组(...\n[BBOX-1227] 2023-07-06 普通儿科三组(...\n[BBOX-1228] 集成视图\n[BBOX-1229] 诊断\n[BBOX-1230] 病历文书\n[BBOX-1231] 处方\n[BBOX-1232] 检验\n[BBOX-1233] 检查\n[BBOX-1234] 处置\n[BBOX-1235] 肺功能检查\n[BBOX-1236] 单机报告\n[BBOX-1237] 体检报告\n[BBOX-1238] 门诊号\n[BBOX-1239] 姓名\n[BBOX-1240] 性别：女\n[BBOX-1241] 年龄：40岁\n[BBOX-1242] 民族：汉族\n[BBOX-1243] 身份证号\n[BBOX-1244] 现住址：\n[BBOX-1245] 就诊类型：初诊\n[BBOX-1246] 就诊科室：妇科门诊\n[BBOX-1247] 就诊日期：2024-04-08 11:32\n[BBOX-1248] 联系电话\n[BBOX-1249] 主诉：月经期下腹间断疼痛2个月\n[BBOX-1250] 现病史：2024.1月经第3天左侧附件区疼痛，超声提示无异常，输消炎药后好转，2024.2无异常，2024.3月经\n[BBOX-1251] 第3天下腹疼痛但是疼痛程度较前减轻，\n[BBOX-1252] 既往史：平素体健，无高血压、冠心病、糖尿病病史，无肝炎、结核等传染病史，无手术史\n[BBOX-1253] 婚育史：\n[BBOX-1254] 月经史：患者平素月经规律，量中等，色正常，无痛经。\n[BBOX-1255] 过敏史：无\n[BBOX-1256] 专科检查：外阴：发育正常，阴毛呈女性分布；阴道：通畅，粘膜红润，未见异常分泌物；宫颈：光滑，大小\n[BBOX-1257] 正常，宫体：正常大小，无压痛。附件：双侧附件区未触及明显异常。\n[BBOX-1258] 辅助检查：\n[BBOX-1259] 初步印象：女性盆腔炎性疾病\n[BBOX-1260] 处理意见：门诊检查\n[BBOX-1261] 备注：\n[BBOX-1262] 医师签名：\n[BBOX-1263] 第1页\n[BBOX-1264] <\n[BBOX-1265] →\n[BBOX-1266] C\n[BBOX-1267] ① 不安全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-1268] 临床数据中心-患者360视图\n[BBOX-1269] 返回患者查询\n[BBOX-1270] 患者姓\n[BBOX-1271] 女\n[BBOX-1272] 出生日期\n[BBOX-1273] 首诊日期：2020-07-08\n[BBOX-1274] 最近诊疗日期：2026-02-12\n[BBOX-1275] 当前在院状态：出院\n[BBOX-1276] 过敏：无\n[BBOX-1277] 详情>>\n[BBOX-1278] 就诊时间抽\n[BBOX-1279] 门诊号\n[BBOX-1280] 就诊时间：2024-04-19 08.07.40\n[BBOX-1281] 接诊科室：普通儿科一组(门)\n[BBOX-1282] 接诊医生：李婉莹\n[BBOX-1283] 全部\n[BBOX-1284] 近一月\n[BBOX-1285] 近三月\n[BBOX-1286] 近半年\n[BBOX-1287] 近一年\n[BBOX-1288] 近五年\n[BBOX-1289] ■ 门诊诊39\n[BBOX-1290] 住院1\n[BBOX-1291] 总览\n[BBOX-1292] 就诊列表\n[BBOX-1293] 2025-04-11 宁波危重—病区(IJ)\n[BBOX-1294] 2025-01-06 普通儿科三组(...\n[BBOX-1295] 2024-12-30 普通儿科三组(...\n[BBOX-1296] 2024-07-05 普通儿科一组(...\n[BBOX-1297] 2024-04-24 普通儿科一组(...\n[BBOX-1298] 2024-04-19 普通儿科一组(...\n[BBOX-1299] 2024-04-08 妇科门诊\n[BBOX-1300] 2024-04-08 妇科一病区(门)\n[BBOX-1301] 2024-01-05 妇科一病区(门)\n[BBOX-1302] 2023-08-14 普通儿科三组(...\n[BBOX-1303] 2023-07-06 普通儿科三组(...\n[BBOX-1304] 集成视图\n[BBOX-1305] 诊断\n[BBOX-1306] 病历文书\n[BBOX-1307] 处方\n[BBOX-1308] 检验\n[BBOX-1309] 检查\n[BBOX-1310] 处置\n[BBOX-1311] 肺功能检查\n[BBOX-1312] 单机报告\n[BBOX-1313] 体检报告\n[BBOX-1314] 门诊号\n[BBOX-1315] 姓\n[BBOX-1316] 性别：女\n[BBOX-1317] 年龄：40岁\n[BBOX-1318] 民族：汉族\n[BBOX-1319] 身份证号：\n[BBOX-1320] 现住址：\n[BBOX-1321] 就诊类型：急诊\n[BBOX-1322] 就诊科室：普通儿科一组(门)\n[BBOX-1323] 就诊日期：2024-04-19 08:07\n[BBOX-1324] 联系电话\n[BBOX-1325] 主诉：因呼吸道感染）不适要求开药\n[BBOX-1326] 现病史：患者因（呼吸道感染）不适，要求开药（家属代开）。\n[BBOX-1327] 既往史：既往体质一般\n[BBOX-1328] 过敏史：无\n[BBOX-1329] 体格检查：神志清晰，精神一般，自主体位，查体合作\n[BBOX-1330] 辅助检查：\n[BBOX-1331] 初步印象：1、急性上呼吸道感染.2、维生素A缺乏伴夜盲症\n[BBOX-1332] 处理意见：开立药品\n[BBOX-1333] 备注：\n[BBOX-1334] 医师签名：李婉莹\n[BBOX-1335] 第1页\n[BBOX-1336] CS 扫描全能王\n[BBOX-1337] 3亿人都在用的扫描App\n[BBOX-1338] 临床数据中心-患者360视图\n[BBOX-1339] 返回患者查询\n[BBOX-1340] 患者姓\n[BBOX-1341] 别：女\n[BBOX-1342] 出生日期：\n[BBOX-1343] 就诊日期：2020-07-08\n[BBOX-1344] 最近诊疗日期：2026-02-12\n[BBOX-1345] 当前在院状态：出院\n[BBOX-1346] 过敏：无\n[BBOX-1347] 详情>>\n[BBOX-1348] 就诊时间：2025-04-11 14:47:07\n[BBOX-1349] 接诊科室：呼吸危重二病区(门)\n[BBOX-1350] 接诊医生：段竹云\n[BBOX-1351] 全部\n[BBOX-1352] 近一月\n[BBOX-1353] 近三月\n[BBOX-1354] 近半年\n[BBOX-1355] 近一年\n[BBOX-1356] 近五年\n[BBOX-1357] 门诊39\n[BBOX-1358] 住院1\n[BBOX-1359] 总览\n[BBOX-1360] 就诊列表\n[BBOX-1361] 2025-06-23 普通儿科三组 (...\n[BBOX-1362] 2025-05-09 呼吸危重二病区(门)\n[BBOX-1363] 2025-04-11 耳鼻咽喉头颈外...\n[BBOX-1364] 2025-04-11 呼吸危重二病区(门)\n[BBOX-1365] 2025-01-06 普通儿科三组 (...\n[BBOX-1366] 2024-12-30 普通儿科三组 (...\n[BBOX-1367] 2024-07-05 普通儿科一组 (...\n[BBOX-1368] 2024-04-24 普通儿科一组 (...\n[BBOX-1369] 2024-04-19 普通儿科一组 (...\n[BBOX-1370] 2024-04-08 妇科门诊\n[BBOX-1371] 2024-04-08 妇科一病区(门)\n[BBOX-1372] 集成视图\n[BBOX-1373] 诊断\n[BBOX-1374] 病历文书\n[BBOX-1375] 处方\n[BBOX-1376] 检验\n[BBOX-1377] 检查\n[BBOX-1378] 处置\n[BBOX-1379] 肺功能检查\n[BBOX-1380] 单机报告\n[BBOX-1381] 透析治疗\n[BBOX-1382] 费用\n[BBOX-1383] 体检报告\n[BBOX-1384] （总）诊病历\n[BBOX-1385] 门诊号：\n[BBOX-1386] 姓\n[BBOX-1387] 性别：女\n[BBOX-1388] 年龄：41岁\n[BBOX-1389] 民族：汉族\n[BBOX-1390] 婚姻状况：已婚\n[BBOX-1391] 身份证\n[BBOX-1392] 职业：专业技术人员\n[BBOX-1393] 现住址：\n[BBOX-1394] 就诊类型：初诊\n[BBOX-1395] 就诊科室：呼吸危重二病区(门)\n[BBOX-1396] 就诊日期：2025-04-11\n[BBOX-1397] 14:47\n[BBOX-1398] 联系电话：\n[BBOX-1399] 主诉：咳嗽憋气一周\n[BBOX-1400] 现病史：患者无发热，感冒后咳嗽、憋气一周，间断治疗，时轻时重，今日来诊\n[BBOX-1401] 既往史：平素体健，无高血压、冠心病、糖尿病病史\n[BBOX-1402] 个人史：无吸烟史\n[BBOX-1403] 过敏史：无\n[BBOX-1404] 体格检查：呼吸平稳，口唇无紫绀，听诊：双肺呼吸音清，未闻及干、湿性啰音\n[BBOX-1405] 辅助检查：肺功能检查提示中重度阻塞性肺通气功能障碍，支气管舒张试验阳性。\n[BBOX-1406] 初步印象：1、支气管哮喘(急性发作期).2、过敏性鼻炎[变应性鼻炎]\n[BBOX-1407] 处理意见：坚持门诊治疗，定期复查\n[BBOX-1408] 备注：\n[BBOX-1409] 医师签名：段竹云\n[BBOX-1410] 第1页\n[BBOX-1411] 临床数据中心-患者360视图\n[BBOX-1412] 返回患者查询\n[BBOX-1413] 就诊时间抽\n[BBOX-1414] 近五年\n[BBOX-1415] 门诊39 住院1\n[BBOX-1416] 就诊列表\n[BBOX-1417] 2025-06-23 普通儿科三组 (...\n[BBOX-1418] 2025-05-09 呼吸危重二病区(门)\n[BBOX-1419] 2025-04-11 耳鼻咽喉头颈外\n[BBOX-1420] 2025-04-11 呼吸危重二病区(门)\n[BBOX-1421] 2025-01-06 普通儿科三组 (...\n[BBOX-1422] 2024-12-30 普通儿科三组 (...\n[BBOX-1423] 2024-07-05 普通儿科一组 (...\n[BBOX-1424] 2024-04-24 普通儿科一组 (...\n[BBOX-1425] 2024-04-19 普通儿科一组 (...\n[BBOX-1426] 2024-04-08 妇科门诊\n[BBOX-1427] 2024-04-08 妇科一病区(门)\n[BBOX-1428] ]: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>\n[BBOX-1429] 就诊时间: 2025-04-11 15:43:29 接诊科室: 耳鼻咽喉头颈外科(门) 接诊医生: 刘秀层\n[BBOX-1430] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 报告\n[BBOX-1431] 门诊病历\n[BBOX-1432] 门诊号\n[BBOX-1433] 姓名\n[BBOX-1434] 性别: 女\n[BBOX-1435] 年龄:41岁\n[BBOX-1436] 民族: 汉族\n[BBOX-1437] 婚姻状况: 已婚\n[BBOX-1438] 身份证号\n[BBOX-1439] 职业: 职员\n[BBOX-1440] 现住址:\n[BBOX-1441] 就诊类型: 初诊\n[BBOX-1442] 就诊科室:耳鼻咽喉头颈外科\n[BBOX-1443] 就诊日期: 2025-04-11 15:43\n[BBOX-1444] 联系电\n[BBOX-1445] 主诉:鼻塞流涕,咳嗽憋气1周\n[BBOX-1446] 现病史:1周前发现鼻塞流涕,患者无发热,感冒后咳嗽、憋气,间断治疗,时轻时重,今日来诊\n[BBOX-1447] 既往史:平素体健,无高血压、冠心病、糖尿病病史\n[BBOX-1448] 家族史:无家族遗传病史\n[BBOX-1449] 过敏史:无\n[BBOX-1450] 体格检查:鼻腔粘膜充血,水肿,水样分泌物附着\n[BBOX-1451] 辅助检查:肺功能检查提示中重度阻塞性肺通气功能障碍,支气管舒张试验阳性。\n[BBOX-1452] 初步印象:1、支气管哮喘(急性发作期)2、过敏性鼻炎[变应性鼻炎]\n[BBOX-1453] 处理意见:坚持门诊治疗,定期复查\n[BBOX-1454] 备注:\n[BBOX-1455] 医师签名:刘秀层\n[BBOX-1456] 第1页\n[BBOX-1457] 三门峡市中心医院门户-患者360 ×\n[BBOX-1458] ← → C ① 不安全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-1459] 临床数据中心-患者360视图\n[BBOX-1460] 返回患者查询 患者姓名 : 女 出生日期\n[BBOX-1461] 日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>\n[BBOX-1462] 就诊时间抽 门诊号\n[BBOX-1463] 就诊时间: 2025-05-09 17 00 57 接诊科室: 呼吸危重二病区(门) 接诊医生: 段竹云\n[BBOX-1464] 全部 近一月 近三月 近半年 近一年\n[BBOX-1465] 近五年\n[BBOX-1466] ■ 门急诊39 住院1\n[BBOX-1467] 总览 就诊列表\n[BBOX-1468] 2025-11-27 普通儿科二区(...\n[BBOX-1469] 2025-11-24 普通儿科二区(...\n[BBOX-1470] 2025-09-18 普通儿科二区(...\n[BBOX-1471] 2025-07-11 普通儿科一组(...\n[BBOX-1472] 2025-06-23 普通儿科三组(...\n[BBOX-1473] 2025-05-09 呼吸危重二病区(门)\n[BBOX-1474] 2025-04-11 耳鼻咽喉头颈外...\n[BBOX-1475] 2025-04-11 呼吸危重二病区(门)\n[BBOX-1476] 2025-01-06 普通儿科三组(...\n[BBOX-1477] 2024-12-30 普通儿科三组(...\n[BBOX-1478] 2024-07-05 普通儿科一组(...\n[BBOX-1479] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 体检报告\n[BBOX-1480] 门诊号:\n[BBOX-1481] 11(急)诊病历\n[BBOX-1482] 性别:女 年龄:41岁 民族:汉族\n[BBOX-1483] 婚姻状况:已婚 身份证 业:专业技术人员\n[BBOX-1484] 现住址:\n[BBOX-1485] 就诊类型:复诊\n[BBOX-1486] 就诊科室:呼吸危重二病区(门) 就诊日期:2025-05-09 17:00 联系电\n[BBOX-1487] 主诉:咳嗽憋气一周\n[BBOX-1488] 现病史:患者无发热,感冒后咳嗽、憋气一周,间断治疗,时轻时重,今日来诊\n[BBOX-1489] 既往史:平素体健,无高血压、冠心病、糖尿病病史\n[BBOX-1490] 个人史:无吸烟史\n[BBOX-1491] 过敏史:无\n[BBOX-1492] 体格检查:听诊:双肺呼吸音清,未闻及干、湿性啰音\n[BBOX-1493] 辅助检查:肺功能检查提示中重度阻塞性肺通气功能障碍,支气管舒张试验阳性。\n[BBOX-1494] 初步印象:1、支气管哮喘.2、过敏性鼻炎[变应性鼻炎]\n[BBOX-1495] 处理意见:坚持门诊治疗,定期复查\n[BBOX-1496] 备注:\n[BBOX-1497] 医师签名:段竹云\n[BBOX-1498] 第1页\n[BBOX-1499] 三门峡市中心医院门户-惠睿360 ×\n[BBOX-1500] ← → ① 不安全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-1501] 临床数据中心-患者360视图\n[BBOX-1502] 返回患者查询 患者姓名:\n[BBOX-1503] 出生日期:\n[BBOX-1504] 日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>\n[BBOX-1505] 就诊时间轴\n[BBOX-1506] 门诊号:\n[BBOX-1507] 就诊时间: 2025-06-23 10:49:50 接诊科室: 普通儿科三组(门) 接诊医生: 谭真真\n[BBOX-1508] 全部 近一月 近三月 近半年 近一年\n[BBOX-1509] 近五年\n[BBOX-1510] 门诊39 住院1\n[BBOX-1511] 总览 就诊列表\n[BBOX-1512] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 体检报告\n[BBOX-1513] 2025-11-27 普通儿科二区(...\n[BBOX-1514] 2025-11-24 普通儿科二区(...\n[BBOX-1515] 2025-09-18 普通儿科二区(...\n[BBOX-1516] 2025-07-11 普通儿科一组(...\n[BBOX-1517] 2025-06-23 普通儿科三组(...\n[BBOX-1518] 2025-05-09 呼吸危重二病区(门)\n[BBOX-1519] 2025-04-11 耳鼻咽喉头颈外...\n[BBOX-1520] 2025-04-11 呼吸危重二病区(门)\n[BBOX-1521] 2025-01-06 普通儿科三组(...\n[BBOX-1522] 2024-12-30 普通儿科三组(...\n[BBOX-1523] 2024-07-05 普通儿科一组(...\n[BBOX-1524] 门诊号:\n[BBOX-1525] 姓名\n[BBOX-1526] 性别: 女\n[BBOX-1527] 年龄:41岁\n[BBOX-1528] 民族: 汉族\n[BBOX-1529] 婚姻状况: 小组\n[BBOX-1530] 身份证号:\n[BBOX-1531] 职业: 专业技术人员\n[BBOX-1532] 现住址:\n[BBOX-1533] 就诊类型:初诊\n[BBOX-1534] 就诊科室:普通儿科三组(门)\n[BBOX-1535] 就诊日期: 2025-06-23 10:49\n[BBOX-1536] 联系电话\n[BBOX-1537] 主诉: 呼吸道感染购药\n[BBOX-1538] 现病史: 呼吸道感染购药\n[BBOX-1539] 既往史: 平素体健, 无肝炎、结核类传染病史\n[BBOX-1540] 过敏史: 无\n[BBOX-1541] 体格检查: 发育正常, 营养良好, 精神一般, 口唇红润, 双侧扁桃体无肿大, 无充血、分泌物。咽腔黏膜有充\n[BBOX-1542] 血, 无红肿、疱疹, 双肺呼吸音清, 听诊心律齐, 无杂音, 腹平软, 无压痛、反跳痛\n[BBOX-1543] 辅助检查:\n[BBOX-1544] 初步印象: 上呼吸道感染\n[BBOX-1545] 处理意见: 门诊药物治疗\n[BBOX-1546] 备注:\n[BBOX-1547] 医师签名: 谭真真\n[BBOX-1548] 第1页\n[BBOX-1549] <->C ① 不安全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-1550] 临床数据中心-患者360视图\n[BBOX-1551] 返回患者查询 患者姓 出生日期\n[BBOX-1552] 就诊日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>\n[BBOX-1553] 就诊时间始 门诊号\n[BBOX-1554] 就诊时间: 2025-07-11 10:02:50 接诊科室: 普通儿科一组(门) 接诊医生: 赵艳\n[BBOX-1555] 全部 近一月 近三月 近半年 近一年\n[BBOX-1556] 近五年\n[BBOX-1557] ■ 门急诊39 住院1\n[BBOX-1558] 总览 就诊列表\n[BBOX-1559] 2025-11-27 普通儿科二区(...\n[BBOX-1560] 2025-11-24 普通儿科二区(...\n[BBOX-1561] 2025-09-18 普通儿科二区(...\n[BBOX-1562] 2025-07-11 普通儿科一组(...\n[BBOX-1563] 2025-06-23 普通儿科三组(...\n[BBOX-1564] 2025-05-09 呼吸危重二病区(门)\n[BBOX-1565] 2025-04-11 耳鼻咽喉头颈外...\n[BBOX-1566] 2025-04-11 呼吸危重二病区(门)\n[BBOX-1567] 2025-01-06 普通儿科三组(...\n[BBOX-1568] 2024-12-30 普通儿科三组(...\n[BBOX-1569] 2024-07-05 普通儿科一组(...\n[BBOX-1570] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 体检报告\n[BBOX-1571] 门诊号\n[BBOX-1572] 1. 病历\n[BBOX-1573] 姓名\n[BBOX-1574] 性别: 女\n[BBOX-1575] 年龄:41岁\n[BBOX-1576] 民族: 汉族\n[BBOX-1577] 婚姻状况: 未婚\n[BBOX-1578] 身份证\n[BBOX-1579] 职业: 专业技术人员\n[BBOX-1580] 现住址:\n[BBOX-1581] 就诊类型:初诊\n[BBOX-1582] 就诊科室:普通儿科一组(门)\n[BBOX-1583] 就诊日期: 2025-07-11 10:02\n[BBOX-1584] 联系电话\n[BBOX-1585] 主诉:呼吸道感染购药\n[BBOX-1586] 现病史:呼吸道感染购药\n[BBOX-1587] 既往史:平素体健,无肝炎、结核类传染病史\n[BBOX-1588] 过敏史:无\n[BBOX-1589] 体格检查:发育正常,营养良好,精神一般,口唇红润,双侧扁桃体无肿大,无充血、分泌物。咽腔黏膜无充血、红肿、疱疹,双肺呼吸音清,听诊心律齐,无杂音,腹平软,无压痛、反跳痛\n[BBOX-1590] 辅助检查:\n[BBOX-1591] 初步印象:支气管炎\n[BBOX-1592] 处理意见:门诊药物治疗\n[BBOX-1593] 备注:\n[BBOX-1594] 医师签名:赵艳\n[BBOX-1595] 第1页\n[BBOX-1596] CS 扫描全能王\n[BBOX-1597] 3亿人都在用的扫描App\n[BBOX-1598] 临床数据中心-患者360视图\n[BBOX-1599] 返回患者查询\n[BBOX-1600] 患者姓名:\n[BBOX-1601] ：女 出生日期:\n[BBOX-1602] 首诊日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>\n[BBOX-1603] 就诊时间抽\n[BBOX-1604] 门诊号:\n[BBOX-1605] 就诊时间: 2025-09-18 15:22:06 接诊科室: 普通儿科二区(门) 接诊医生: 赵艳\n[BBOX-1606] 全部\n[BBOX-1607] 近一月\n[BBOX-1608] 近三月\n[BBOX-1609] 近半年\n[BBOX-1610] 近一年\n[BBOX-1611] 近五年\n[BBOX-1612] 门诊39 住院1\n[BBOX-1613] 总览\n[BBOX-1614] 就诊列表\n[BBOX-1615] 2025-12-09 普通儿科二区(...\n[BBOX-1616] 2025-12-07 普通儿科二区(...\n[BBOX-1617] 2025-12-01 普通儿科二区(...\n[BBOX-1618] 2025-11-27 普通儿科二区(...\n[BBOX-1619] 2025-11-24 普通儿科二区(...\n[BBOX-1620] 2025-09-18 普通儿科二区(...\n[BBOX-1621] 2025-07-11 普通儿科一组(...\n[BBOX-1622] 2025-06-23 普通儿科三组(...\n[BBOX-1623] 2025-05-09 呼吸危重二病区(门)\n[BBOX-1624] 2025-04-11 耳鼻咽喉头颈外...\n[BBOX-1625] 2025-04-11 呼吸危重二病区(门)\n[BBOX-1626] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 请价治疗 费用 体检报告\n[BBOX-1627] 门诊病历\n[BBOX-1628] 门诊\n[BBOX-1629] 姓名:\n[BBOX-1630] 性别: 女\n[BBOX-1631] 年龄:41岁\n[BBOX-1632] 民族: 汉族\n[BBOX-1633] 婚姻状况: 未婚\n[BBOX-1634] 身份证\n[BBOX-1635] 职业: 职员\n[BBOX-1636] 现住址:\n[BBOX-1637] 就诊类型:初诊\n[BBOX-1638] 就诊科室:普通儿科二区(门)\n[BBOX-1639] 就诊日期: 2025-09-18 15:22\n[BBOX-1640] 联系电话\n[BBOX-1641] 主诉:咽部疼痛伴眼部不适4天\n[BBOX-1642] 现病史:4天前无明显诱因出现咽部疼痛,伴鼻塞,伴眼部不适,无发热、呕吐、腹泻、皮疹等不适,病后精神、食欲欠佳,大小便正常。\n[BBOX-1643] 既往史:无特殊。\n[BBOX-1644] 过敏史:无\n[BBOX-1645] 体格检查:发育正常,营养良好,精神一般,呼吸平稳,双眼睑结膜充血,口唇红润,咽腔充血,无疱疹,双侧扁桃体I°,充血,无分泌物,双肺呼吸音清,未闻及干湿性啰音,听诊心律齐,无杂音,腹平软,无压痛、反跳痛,未触及包块,肠鸣音活跃,神经系统未见阳性体征。\n[BBOX-1646] 辅助检查:无\n[BBOX-1647] 初步印象:1.急性咽峡炎.2.急性变应性结膜炎\n[BBOX-1648] 处理意见:门诊治疗,动态观察病情变化,不适及时随诊。\n[BBOX-1649] 备注:\n[BBOX-1650] 医师签名:赵艳\n[BBOX-1651] 第1页\n[BBOX-1652] Le coo\n[BBOX-1653] 全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-1654] 临床数据中心\n[BBOX-1655] 0视图\n[BBOX-1656] 返回患者查询\n[BBOX-1657] 患者\n[BBOX-1658] 女 出生F\n[BBOX-1659] 就诊日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>\n[BBOX-1660] 就诊时间轴\n[BBOX-1661] 门诊\n[BBOX-1662] 诊时间: 2025-12-01 15:28:03 接诊科室: 普通儿科二区(门) 接诊医生: 赵海国\n[BBOX-1663] 全季\n[BBOX-1664] 近一月\n[BBOX-1665] 近三月\n[BBOX-1666] 近半年\n[BBOX-1667] 近一年\n[BBOX-1668] 近五年\n[BBOX-1669] 门诊急诊39 住院1\n[BBOX-1670] 总览\n[BBOX-1671] 就诊列表\n[BBOX-1672] 集成视图\n[BBOX-1673] 诊断\n[BBOX-1674] 病历文书\n[BBOX-1675] 处方\n[BBOX-1676] 检验\n[BBOX-1677] 检查\n[BBOX-1678] 处置\n[BBOX-1679] 肺功能检查\n[BBOX-1680] 单机报告\n[BBOX-1681] 透析治疗\n[BBOX-1682] 费用\n[BBOX-1683] 体检报告\n[BBOX-1684] 门诊\n[BBOX-1685] 1.1、心/诊病历\n[BBOX-1686] 门诊\n[BBOX-1687] 2026-01-15 呼吸危重二病区(门)\n[BBOX-1688] 2026-01-06 妇科一病区(门)\n[BBOX-1689] 2025-12-09 普通儿科二区(...\n[BBOX-1690] 2025-12-07 普通儿科二区(...\n[BBOX-1691] 2025-12-01 普通儿科二区(...\n[BBOX-1692] 2025-11-27 普通儿科二区(...\n[BBOX-1693] 2025-11-24 普通儿科二区(...\n[BBOX-1694] 2025-09-18 普通儿科二区(...\n[BBOX-1695] 2025-07-11 普通儿科一组(...\n[BBOX-1696] 2025-06-23 普通儿科三组(...\n[BBOX-1697] 2025-05-09 呼吸危重二病区(门)\n[BBOX-1698] 姓名:\n[BBOX-1699] 性别: 女\n[BBOX-1700] 年龄:41岁\n[BBOX-1701] 民族: 汉族\n[BBOX-1702] 婚姻状况: 未...\n[BBOX-1703] 身份证:\n[BBOX-1704] 职业: 专业技术人员\n[BBOX-1705] 现住址:\n[BBOX-1706] 就诊类型:初诊\n[BBOX-1707] 就诊科室:普通儿科二区(门)\n[BBOX-1708] 就诊日期: 2025-12-01 15:28\n[BBOX-1709] 联系电\n[BBOX-1710] 主诉: 发热半天。\n[BBOX-1711] 现病史: 半天前出现发热,最高体温38.0℃,口服药物治疗1次,无咳嗽,无喘息,无呼吸困难,无咯血,无腹泻、呕吐等。精神食欲一般,大小便正常。\n[BBOX-1712] 既往史: 无。\n[BBOX-1713] 过敏史: 无\n[BBOX-1714] 体格检查: 神志清,精神一般,呼吸浅快,咽充血,扁桃体二度大,充血,无疱疹,无脓点,双肺呼吸音清,\n[BBOX-1715] 心音有力,律齐,腹软。\n[BBOX-1716] 辅助检查:\n[BBOX-1717] 初步印象: 急性上呼吸道感染\n[BBOX-1718] 处理意见: 口服药物,动态观察,不适随诊。\n[BBOX-1719] 备注:\n[BBOX-1720] 医师签名: 赵海国\n[BBOX-1721] 第1页\n[BBOX-1722] 姓名：\n[BBOX-1723] 性别：女\n[BBOX-1724] 年龄：41岁\n[BBOX-1725] 民族：汉族\n[BBOX-1726] 婚姻状况：已婚\n[BBOX-1727] 身份证号\n[BBOX-1728] 职业：专业技术人员\n[BBOX-1729] 现住址\n[BBOX-1730] 就诊类型：初诊\n[BBOX-1731] 就诊科室：妇科一病区(门)\n[BBOX-1732] 就诊日期：2026-01-06 08:36\n[BBOX-1733] 联系电话.\n[BBOX-1734] 主诉：左下腹间断疼痛1年左右来诊\n[BBOX-1735] 现病史：患者诉于2024年01月05日无明显诱因出现下腹持续疼痛行相关检查后诊断为盆腔炎性疾病后遗症，\n[BBOX-1736] 慢性盆腔痛，药物治疗后好转，慢性盆腔痛病程12月，目前疾病状态持续，未治疗。\n[BBOX-1737] 既往史：2025年11月24日-2025年12月12日本院儿科门诊就诊代家属开药，否认3个月内其他病史及合并用药/\n[BBOX-1738] 非药物治疗，现患者无盆腔炎性疾病急性发作，否认既往有子宫肌瘤、子宫内膜异位症、子宫腺肌病、结核性\n[BBOX-1739] 盆腔炎、间质性膀胱炎、异常子宫出血、盆腔淤血综合征、子宫颈高级别上皮内病变等其他病症引起相关症状\n[BBOX-1740] 者；未放置宫内节育器；无子宫及双侧附件缺如；近2周内未使用过本方案规定研究期间禁止使用的治疗（包括\n[BBOX-1741] 药物和非药物治疗）；无控制不稳定的心血管、肝、肾和血液系统、糖尿病、甲状腺疾病等严重原发性疾病；\n[BBOX-1742] 获得知情同意书前5年内未患有恶性肿瘤；否认对试验用药品过敏，包括对本品成分或者药物辅料有过敏史；否\n[BBOX-1743] 认长期酗酒、药物滥用史；无智力障碍或精神障碍；近1个月内未参加过任何干预性临床试验；患者当前不在妊\n[BBOX-1744] 娠期、哺乳期，同意在试验期间及试验结束后3个月内采取有效避孕措施。\n[BBOX-1745] 婚育史：已婚已育，孕2产2，有性生活史\n[BBOX-1746] 手术史：2016年8月31日、2020年7月9日因生产行剖宫产手术\n[BBOX-1747] 月经史：初潮12岁，既往月经周期规律，经量中，色红，无痛经，末次月经2025.12.29-2025.1.2，周期26-\n[BBOX-1748] 28天，经期5天，经量较前不变\n[BBOX-1749] 过敏史：无\n[BBOX-1750] 生命体征：2026.1.6测量身高：160.0cm 体重：51.0kg 体温：36.4℃ 脉搏：76次/分 呼吸：18次/分 血压：\n[BBOX-1751] 98/76mmHg\n[BBOX-1752] 体格检查：淋巴结、头颈部、胸部、脊柱/四肢/关节、神经系统未见异常，腹部异常（左下腹压痛，CS，研究\n[BBOX-1753] 疾病相关），皮肤黏膜异常（腹部皮肤约5-6cm剖宫产手术瘢痕，NCS），其他未查。\n[BBOX-1754] 专科检查：外阴已婚型，阴道畅，宫颈光滑，无摇举痛，有宫体压痛，无子宫活动受限或粘连固定，左侧附件\n[BBOX-1755] 区、右侧附件区压痛，无宫骶韧带增粗、变硬、触痛。\n[BBOX-1756] 辅助检查：今日按方案要求开具血常规、尿沉渣（含尿常规）、肝功八项、肾功两项、血妊娠、血沉、血清C&-\n[BBOX-1757] 125、妇科微生态、十二导联心电图、妇科阴道彩色B超检查，结果详见检查单。\n[BBOX-1758] 初步印象：盆腔痛中医辨证：主症：下腹胀痛，腰骶部胀痛、带下量多；次症：神疲乏力、口苦口腻、小便\n[BBOX-1759] 黄；舌象：舌质红、苔黄腻；脉象：脉弦滑；2026年01月06日由张丹丹医生辨证为湿热瘀阻症。 西医：盆腔炎\n[BBOX-1760] 性疾病后遗症，慢性盆腔痛\n[BBOX-1761] 处理意见：根据目前临床表现及患者情况，权丽丽医生于2026年01月06日08时38分在9号楼4楼医患沟通室向患\n[BBOX-1762] 绍“妇科千金片治疗盆腔炎性疾病后遗症（湿热瘀阻证）的随机、双盲、安慰剂平行对照、多中心临\n[BBOX-1763] 床试验”及知情同意书内容，已告知参加试验可能的风险与获益，患者已充分理解并同意参加该研究，未提出\n[BBOX-1764] 门\n[BBOX-1765] CS 扫描全能王\n[BBOX-1766] 3亿人都在用的扫描App\n[BBOX-1767] 既往史：2025年11月24日-2025年12月12日本院儿科门诊就诊代家属开药，否认3个月内其他病史及合并用药/\n[BBOX-1768] 非药物治疗，现患者无盆腔炎性疾病急性发作，否认既往有子宫肌瘤、子宫内膜异位症、子宫腺肌病、结核性\n[BBOX-1769] 盆腔炎、间质性膀胱炎、异常子宫出血、盆腔淤血综合征、子宫颈高级别上皮内病变等其他病症引起相关症状\n[BBOX-1770] 者；未放置宫内节育器；无子宫及双侧附件缺如；近2周内未使用过本方案规定研究期间禁止使用的治疗（包括\n[BBOX-1771] 药物和非药物治疗）；无控制不稳定的心血管、肝、肾和血液系统、糖尿病、甲状腺疾病等严重原发性疾病；\n[BBOX-1772] 获得知情同意书前5年内未患有恶性肿瘤；否认对试验用药品过敏，包括对本品成分或者药物辅料有过敏史；否\n[BBOX-1773] 认长期酗酒、药物滥用史；无智力障碍或精神障碍；近1个月内未参加过任何干预性临床试验；患者当前不在妊\n[BBOX-1774] 娠期、哺乳期，同意在试验期间及试验结束后3个月内采取有效避孕措施。\n[BBOX-1775] 婚育史：已婚已育，孕2产2，有性生活史\n[BBOX-1776] 手术史：2016年8月31日、2020年7月9日因生产行剖宫产手术\n[BBOX-1777] 月经史：初潮12岁，既往月经周期规律，经量中，色红，无痛经，末次月经2025.12.29-2025.1.2，周期26-\n[BBOX-1778] 28天，经期5天，经量较前不变\n[BBOX-1779] 过敏史：无\n[BBOX-1780] 生命体征：2026.1.6测量身高：160.0cm 体重：51.0kg 体温：36.4℃ 脉搏：76次/分 呼吸：18次/分 血压：\n[BBOX-1781] 98/76mmHg\n[BBOX-1782] 体格检查：淋巴结、头颈部、胸部、脊柱/四肢/关节、神经系统未见异常，腹部异常（左下腹压痛，CS，研究\n[BBOX-1783] 疾病相关），皮肤黏膜异常（腹部皮肤约5-6cm剖宫产手术瘢痕，NCS），其他未查。\n[BBOX-1784] 专科检查：外阴已婚型，阴道畅，宫颈光滑，无摇举痛，有宫体压痛，无子宫活动受限或粘连固定，左侧附件\n[BBOX-1785] 区、右侧附件区压痛，无宫骶韧带增粗、变硬、触痛。\n[BBOX-1786] 辅助检查：今日按方案要求开具血常规、尿沉渣（含尿常规）、肝功八项、肾功两项、血妊娠、血沉、血清CA-\n[BBOX-1787] 125、妇科微生态、十二导联心电图、妇科阴道彩色B超检查，结果详见检查单。\n[BBOX-1788] 初步印象：盆腔痛中医辨证：主症：下腹胀痛，腰骶部胀痛、带下量多；次症：神疲乏力、口苦口腻、小便\n[BBOX-1789] 黄；舌象：舌质红、苔黄腻；脉象：脉弦滑；2026年01月06日由张丹丹医生辨证为湿热瘀阻症。 西医：盆腔炎\n[BBOX-1790] 性疾病后遗症，慢性盆腔痛\n[BBOX-1791] 从细之间、根据目前临床表现及患者情况，权丽丽医生于2026年01月06日08时38分在9号楼4楼医患沟通室向患\n[BBOX-1792] 者\n[BBOX-1793] 引“妇科千金片治疗盆腔炎性疾病后遗症（湿热瘀阻证）的随机、双盲、安慰剂平行对照、多中心临\n[BBOX-1794] 床试验”及知情同意书内容，已告知参加试验可能的风险与获益，患者已充分理解并同意参加该研究，未提出\n[BBOX-1795] 问题，患者本人于2026年01月06日08时58分签署知情同意书（版本号：V1.0 三门峡市中心医院专用版，版本日\n[BBOX-1796] 期：2025年08月05日），权丽丽医生于2026年01月06日08时59分签署知情同意书（版本号：V1.0 三门峡市中心\n[BBOX-1797] 医院专用版，版本日期：2025年08月05日），知情同意书原件一份保存于受试者文件夹，一份交给患者本人，\n[BBOX-1798] 确定患者筛选号为04011，进入试验筛选，根据方案要求，收集受试者的试验相关资料，并于今日开始进行筛选\n[BBOX-1799] 期相关检查。\n[BBOX-1800] 1.已完成体征McCormack量表评分，总分8分，回顾近1周非经期腹痛/腰骶疼痛NRS平均分为5分。\n[BBOX-1801] 2.嘱受试者合理饮食，避免过度劳累；避免盆浴和坐浴，避免穿紧身衣物和化纤内裤；注意经期卫生。\n[BBOX-1802] 3.今日结合受试者情况，2026年1月6日血清CA-125示：59.70（0.00-35.00）U/mL，符合排除标准第（8）条，\n[BBOX-1803] 筛选失败，告知受试者转为门诊常规诊疗。\n[BBOX-1804] 备注：\n[BBOX-1805] 医师签名：\n[BBOX-1806] 临床数据中心-患者360视图\n[BBOX-1807] 返回患者查询\n[BBOX-1808] 患者\n[BBOX-1809] 日期：2020-07-08\n[BBOX-1810] 最近诊疗日期：2026-02-12\n[BBOX-1811] 当前在院状态：出院\n[BBOX-1812] 过敏：无\n[BBOX-1813] 详情>>\n[BBOX-1814] 就诊时间轴\n[BBOX-1815] 门诊号\n[BBOX-1816] 时间：2026-01-15 10:56:28\n[BBOX-1817] 接诊科室：呼吸危重三病区(门)\n[BBOX-1818] 接诊医生：王辉\n[BBOX-1819] 全部\n[BBOX-1820] 近一月\n[BBOX-1821] 近三月\n[BBOX-1822] 近半年\n[BBOX-1823] 近一年\n[BBOX-1824] 近五年\n[BBOX-1825] 门诊39-住院1\n[BBOX-1826] 就诊列表\n[BBOX-1827] 总览\n[BBOX-1828] 2026-02-12 呼吸危重三病区(门)\n[BBOX-1829] 2026-01-15 呼吸危重三病区(门)\n[BBOX-1830] 2026-01-06 妇科一病区(门)\n[BBOX-1831] 2025-12-09 普通儿科二区 (...\n[BBOX-1832] 2025-12-07 普通儿科二区 (...\n[BBOX-1833] 2025-12-01 普通儿科二区 (...\n[BBOX-1834] 2025-11-27 普通儿科二区 (...\n[BBOX-1835] 2025-11-24 普通儿科二区 (...\n[BBOX-1836] 2025-09-18 普通儿科二区 (...\n[BBOX-1837] 2025-07-11 普通儿科一组 (...\n[BBOX-1838] 2025-06-23 普通儿科三组 (...\n[BBOX-1839] 集成视图\n[BBOX-1840] 诊断\n[BBOX-1841] 病历文书\n[BBOX-1842] 处方\n[BBOX-1843] 检验\n[BBOX-1844] 检查\n[BBOX-1845] 处置\n[BBOX-1846] 肺功能检查\n[BBOX-1847] 单机报告\n[BBOX-1848] 透析治疗\n[BBOX-1849] 费用\n[BBOX-1850] 体检报告\n[BBOX-1851] 门诊\n[BBOX-1852] 姓名\n[BBOX-1853] 性别：女\n[BBOX-1854] 年龄：41岁\n[BBOX-1855] 民族：汉族\n[BBOX-1856] 婚姻状况：已婚\n[BBOX-1857] 身份证号\n[BBOX-1858] 职业：其他\n[BBOX-1859] 现住址\n[BBOX-1860] 就诊类型：复诊\n[BBOX-1861] 就诊科室：呼吸危重三病区(门)\n[BBOX-1862] 就诊日期：2026-01-15\n[BBOX-1863] 10:56\n[BBOX-1864] 联系电话\n[BBOX-1865] 主诉：咳嗽憋气一周\n[BBOX-1866] 现病史：患者无发热，感冒后咳嗽、憋气一周，间断治疗，时轻时重，今日来诊\n[BBOX-1867] 既往史：平素体健，无高血压、冠心病、糖尿病病史\n[BBOX-1868] 个人史：无吸烟史\n[BBOX-1869] 过敏史：无\n[BBOX-1870] 体格检查：听诊：双肺呼吸音清，未闻及干、湿性啰音\n[BBOX-1871] 辅助检查：肺功能检查提示中重度阻塞性肺通气功能障碍，支气管舒张试验阳性。\n[BBOX-1872] 初步印象：1、支气管哮喘(急性发作期).2、过敏性鼻炎[变应性鼻炎]\n[BBOX-1873] 处理意见：坚持门诊治疗，定期复查\n[BBOX-1874] 备注\n[BBOX-1875] 医师签名：王辉\n[BBOX-1876] 第1页\n[BBOX-1877] 984-04-02 首诊日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>\n[BBOX-1878] 返回概览视图\n[BBOX-1879] 门诊号: 2\n[BBOX-1880] 时间: 2026-02-12 11.40.02 接诊科室: 呼吸危重三病区(门) 接诊医生: 孙帅森\n[BBOX-1881] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告\n[BBOX-1882] 请输入药品内容,按回车键检索\n[BBOX-1883] 查询全部\n[BBOX-1884] 类型 组 药品名称[规格] 用法 频率 实际用量 总量 开立时间 开立医师\n[BBOX-1885] 药品 (320ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 320ug 1 2026-02-25 07:47:00 赵海国\n[BBOX-1886] 药品 鼻渊通窍颗粒 口服 tid 1袋 3 2026-02-12 09:40:21 谭真真\n[BBOX-1887] 药品 阿莫西林克拉维酸钾片(选) 口服(继续用药) tid 0.375g 24 2026-02-12 09:40:21 谭真真\n[BBOX-1888] 药品 (160ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 160ug 1 2026-01-17 08:04:36 彭文娟\n[BBOX-1889] 药品 (320ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 320ug 1 2026-01-17 08:04:36 彭文娟\n[BBOX-1890] 药品 磷酸奥司他韦胶囊(东阳光) 口服 bid 75mg 10 2025-12-07 10:50:33 彭文娟\n[BBOX-1891] 药品 鼻渊通窍颗粒 口服 bid 1袋 2 2025-11-27 15:02:43 烟海丽\n[BBOX-1892] 药品 盐酸氮卓斯丁滴眼液 滴眼 qid 0.01ml 1 2025-09-18 15:29:34 赵艳\n[BBOX-1893] 药品 阿莫西林克拉维酸钾片(选) 口服(继续用药) tid 0.375g 24 2025-09-18 15:25:48 赵艳\n[BBOX-1894] 药品 (成人)双黄连口服液(选) 口服 tid 20ml 2 2025-09-18 15:25:48 赵艳\n[BBOX-1895] 药品 (160ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 160ug 1 2025-07-11 10:07:36 赵艳\n[BBOX-1896] 药品 (小儿)双黄连口服液(选) 口服 tid 20ml 2 2025-06-23 10:52:35 谭真真\n[BBOX-1897] 药品 (倾尔宁片)孟鲁司特钠片(选) 口服 qn 10mg 30 2025-05-09 17:04:48 段竹云\n[BBOX-1898] 共70页 2026-02-12 1 2 3 4 > 前往 1 页\n[BBOX-1899] 50/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-1900] 984-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>\n[BBOX-1901] 时间：2026-02-12 11:40.02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森\n[BBOX-1902] 返回概览视图\n[BBOX-1903] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告\n[BBOX-1904] 请输入药品内容，按回车键检索\n[BBOX-1905] 查询全部\n[BBOX-1906] 类型 组 药品名称(规格) 用法 频率 实际用量 总量 开立时间 开立医师\n[BBOX-1907] 药品 鼻渊通窍颗粒 口服 bid 1袋 2 2025-11-27 15:02.43 烟海丽\n[BBOX-1908] 药品 盐酸氮卓斯丁滴眼液 滴眼 qid 0.01ml 1 2025-09-18 15:29.34 赵艳\n[BBOX-1909] 药品 阿莫西林克拉维酸钾片(选) 口服(继续用药) tid 0.375g 24 2025-09-18 15:25.48 赵艳\n[BBOX-1910] 药品 (成人)双黄连口服液(选) 口服 tid 20ml 2 2025-09-18 15:25.48 赵艳\n[BBOX-1911] 药品 (160ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 160ug 1 2025-07-11 10:07.36 赵艳\n[BBOX-1912] 药品 (小儿)双黄连口服液(选) 口服 tid 20ml 2 2025-06-23 10:52.35 谭真真\n[BBOX-1913] 药品 (顺尔宁片)孟鲁司特钠片(选) 口服 qn 10mg 30 2025-05-09 17:04.48 段竹云\n[BBOX-1914] 药品 (320ug)布地奈德福莫特罗粉吸入剂 吸入 bid 320ug 2 2025-05-09 17:04.48 段竹云\n[BBOX-1915] 药品 醋酸泼尼松片 口服 qm 30mg 36 2025-04-11 15:46.53 刘秀层\n[BBOX-1916] 药品 鼻炎康莫米松鼻喷雾剂(选) 喷鼻 bid 100ug 1 2025-04-11 15:31.05 段竹云\n[BBOX-1917] 药品 (顺尔宁片)孟鲁司特钠片(选) 口服 qn 10mg 5 2025-04-11 15:31.05 段竹云\n[BBOX-1918] 药品 (320ug)布地奈德福莫特罗粉吸入剂 吸入 bid 320ug 1 2025-04-11 15:31.05 段竹云\n[BBOX-1919] 药品 磷酸奥司他韦胶囊(东阳光) 口服 bid 75mg 10 2025-01-06 17:15.28 谭真真\n[BBOX-1920] 药品 氯雷他定颗粒 口服 qd 10mg 1 2024-12-30 10:40:10 谭真真\n[BBOX-1921] 共70条 20条/页 < 1 2 3 4 > 前往 1\n[BBOX-1922] /patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-1923] 84-04-02\n[BBOX-1924] 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>\n[BBOX-1925] 返回概览视图\n[BBOX-1926] 门诊时间: 2026-02-12 11:40:02 接诊科室: 呼吸危重三病区(门) 接诊医生: 孙帅森\n[BBOX-1927] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告\n[BBOX-1928] 请输入药品内容, 按回车键检索\n[BBOX-1929] 查询全部\n[BBOX-1930] 类型 组 药品名称[规格] 用法 频率 实际用量 总量 开立时间 开立医师\n[BBOX-1931] 药品 (大伊可新)维生素AD滴剂 口服 qd 2000u 3 2024-07-05 09:30:58 李婉莹\n[BBOX-1932] 药品 (普米克令舒)吸入用布地奈德混悬液 压缩雾化吸入 tid 2ml 20 2024-07-05 09:30:58 李婉莹\n[BBOX-1933] 药品 小儿豉翘清热颗粒 口服 tid 6g 3 2024-04-24 11:59:55 赵艳\n[BBOX-1934] 药品 (成人)双黄连口服液(基选) 口服 tid 20ml 3 2024-04-19 08:14:06 李婉莹\n[BBOX-1935] 药品 (强力)阿莫西林克拉维酸钾干混悬剂(选) 口服(继续用药) bid 0.457g 2 2024-04-19 08:14:06 李婉莹\n[BBOX-1936] 药品 (大伊可新)维生素AD滴剂 口服 qd 2000u 3 2024-04-19 08:14:06 李婉莹\n[BBOX-1937] 药品 (普米克令舒)吸入用布地奈德混悬液 压缩雾化吸入 tid 2ml 20 2024-04-19 08:14:06 李婉莹\n[BBOX-1938] 药品 替硝唑氯化钠注射液 静滴 qd 200ml 6 2024-01-05 10:37:47 程会芳\n[BBOX-1939] 药品 左氧氟沙星氯化钠注射液(选) 静滴 qd 0.5g 3 2024-01-05 10:37:47 程会芳\n[BBOX-1940] 药品 蒲地蓝消炎口服液 口服 tid 10ml 2 2023-08-14 15:30:23 谭真真\n[BBOX-1941] 药品 (盖克)小儿氨酚黄那敏颗粒 口服 tid 12g 2 2023-07-06 20:00:14 谭真真\n[BBOX-1942] 药品 蒲地蓝消炎口服液 口服 tid 10ml 2 2023-07-06 20:00:14 谭真真\n[BBOX-1943] 共70条 20条/页 < 1 2 3 4 > 前往 2 页\n[BBOX-1944] CS 扫描全能王\n[BBOX-1945] 3亿人都在用的扫描App\n[BBOX-1946] 50/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-1947] 984-04-02 首诊日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>\n[BBOX-1948] 返回概览视图\n[BBOX-1949] 门诊\n[BBOX-1950] 2026-02-12 11:40:02 接诊科室: 呼吸危重三病区(门) 接诊医生: 孙帅森\n[BBOX-1951] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告\n[BBOX-1952] 请输入药品内容,按回车键检索\n[BBOX-1953] 查询全部\n[BBOX-1954] 类型 组 药品名称[规格]\n[BBOX-1955] 药品 替硝唑氯化钠注射液\n[BBOX-1956] 药品 左氧氟沙星氯化钠注射液(选)\n[BBOX-1957] 药品 蒲地蓝消炎口服液\n[BBOX-1958] 药品 (盖克)小儿氨酚黄那敏颗粒\n[BBOX-1959] 药品 蒲地蓝消炎口服液\n[BBOX-1960] 药品 (小儿)双黄连口服液(选)\n[BBOX-1961] 药品 地塞米松磷酸钠注射液(选)\n[BBOX-1962] 药品 5ml灭菌注射用水\n[BBOX-1963] 药品 (扑尔敏针)马来酸氯苯那敏注射液\n[BBOX-1964] 药品 消旋山莨菪碱注射液\n[BBOX-1965] 药品 头孢克肟颗粒(选)\n[BBOX-1966] 药品 (天晴速畅)吸入用布地奈德混悬液(选)\n[BBOX-1967] 药品 (大伊可新)维生素AD滴剂\n[BBOX-1968] 用法 频率 实际用量 总量 开立时间 开立医师\n[BBOX-1969] 入\n[BBOX-1970] 静滴 qd 200ml 6 2024-01-05 10:37:47 程会芳\n[BBOX-1971] 静滴 qd 0.5g 3 2024-01-05 10:37:47 程会芳\n[BBOX-1972] 口服 tid 10ml 2 2023-08-14 15:30:23 谭真真\n[BBOX-1973] 口服 tid 12g 2 2023-07-06 20:00:14 谭真真\n[BBOX-1974] 口服 tid 10ml 2 2023-07-06 20:00:14 谭真真\n[BBOX-1975] 口服 tid 20ml 2 2023-07-06 20:00:14 谭真真\n[BBOX-1976] 外用 bid 10mg 2 2023-06-26 15:19:59 谭真真\n[BBOX-1977] 外用 bid 5ml 4 2023-06-26 15:19:59 谭真真\n[BBOX-1978] 外用 bid 20mg 2 2023-06-26 15:19:59 谭真真\n[BBOX-1979] 外用 bid 20mg 2 2023-06-26 15:19:59 谭真真\n[BBOX-1980] 口服 bid 100mg 30 2023-05-08 19:56:47 陈音\n[BBOX-1981] 压缩雾化吸入 bid 2ml 10 2023-05-08 19:52:42 段艳霞\n[BBOX-1982] 口服 qd 2000u 2 2023-05-08 19:52:42 段艳霞\n[BBOX-1983] 共70条 20条/页 < 1 2 3 4 > 前往: 2 页\n[BBOX-1984] 返回概览视图\n[BBOX-1985] 11.40.02 接诊科室: 呼吸危重三病区(门) 接诊医生: 孙帅森\n[BBOX-1986] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告\n[BBOX-1987] 请输入药品内容,按回车键检索\n[BBOX-1988] 查询全部\n[BBOX-1989] 类型 组 药品名称|规格 用法 频率 实际用量 总量 开立时间 开立医师\n[BBOX-1990] 药品 *乙2)(大伊可新)维生素AD滴剂 口服 qd 2000u 2 2023-04-07 16:29.03 陈音\n[BBOX-1991] 药品 乙1)头孢克肟颗粒(选) 口服 bid 100mg 30 2023-04-07 16:28.02 陈音\n[BBOX-1992] 药品 乙0)阿奇霉素干混悬剂 口服 qd 0.25g 1 2023-04-07 16:27:17 陈音\n[BBOX-1993] 药品 乙2)三拗片 口服 tid 2片 1 2023-04-07 16:27:17 陈音\n[BBOX-1994] 药品 乙0)富马酸酮替芬片 口服 bid 1mg 6 2023-04-07 16:27:17 陈音\n[BBOX-1995] 药品 蒲地蓝消炎口服液 口服 tid 10ml 2 2022-08-08 15:40.53 王晶\n[BBOX-1996] 药品 乙1)盐酸氨溴索口服溶液(基) 口服 bid 5ml 1 2022-05-09 19:49:32 赵海国\n[BBOX-1997] 药品 赖氨肌醇维B12口服溶液 口服 bid 10ml 3 2022-05-09 19:49:32 赵海国\n[BBOX-1998] 药品 乙0)5ml灭菌注射用水 外用 bid 20ml 4 2022-05-05 09:58:24 李凌蔚\n[BBOX-1999] 药品 乙1)(扑尔敏针)马来酸氯苯那敏注射液 外用 bid 20mg 2 2022-05-05 09:58:24 李凌蔚\n[BBOX-2000] 药品 甲)地塞米松磷酸钠注射液(基) 外用 bid 10mg 2 2022-05-05 09:58:24 李凌蔚\n[BBOX-2001] 药品 乙1)消旋山莨菪碱注射液(基) 外用 bid 20mg 2 2022-05-05 09:58:24 李凌蔚\n[BBOX-2002] 药品 赖氨肌醇维B12口服溶液 口服 bid 10ml 1 2022-05-05 09:57:04 李凌蔚\n[BBOX-2003] 药品 乙1)复合维生素B片 口服 tid 1片 100 2022-05-05 09:56:29 李凌蔚\n[BBOX-2004] 药品 用维生素004/基 口服 4 100 2022-05-05 09:56:29 李凌蔚\n[BBOX-2005] 共70条 20条/页 < 1 2 3 4 > 前往 3 页\n[BBOX-2006] CS 扫描全能王\n[BBOX-2007] 3亿人都在用的扫描App\n[BBOX-2008] 50/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-2009] 984-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>\n[BBOX-2010] 返回概览视图\n[BBOX-2011] 门.\n[BBOX-2012] J26-02-12 11.40.02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森\n[BBOX-2013] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告\n[BBOX-2014] 请输入药品内容，按回车键检索\n[BBOX-2015] 查询全部\n[BBOX-2016] 类型 组 药品名称/规格 用法 频率 实际用量 总量 开立时间 开立医师\n[BBOX-2017] 药品 口服 bid 5ml 1 2022-05-09 19.49.32 赵海国\n[BBOX-2018] 药品 赖氨肌醇维B12口服溶液 口服 bid 10ml 3 2022-05-09 19.49.32 赵海国\n[BBOX-2019] 药品 乙0)5ml灭菌注射用水 外用 bid 20ml 4 2022-05-05 09.58.24 李凌蔚\n[BBOX-2020] 药品 乙1)(扑尔敏针)马来酸氯苯那敏注射液 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚\n[BBOX-2021] 药品 甲)地塞米松磷酸钠注射液(基) 外用 bid 10mg 2 2022-05-05 09.58.24 李凌蔚\n[BBOX-2022] 药品 乙1)消旋山莨菪碱注射液(基) 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚\n[BBOX-2023] 药品 赖氨肌醇维B12口服溶液 口服 bid 10ml 1 2022-05-05 09.57.04 李凌蔚\n[BBOX-2024] 药品 乙1)复合维生素B片 口服 tid 1片 100 2022-05-05 09.56.29 李凌蔚\n[BBOX-2025] 药品 甲)维生素B2片(基) 口服 tid 5mg 100 2022-05-05 09.56.29 李凌蔚\n[BBOX-2026] 药品 乙1)头孢克肟颗粒 口服 bid 50mg 2 2022-05-05 09.54.38 李凌蔚\n[BBOX-2027] 药品 乙1)金振口服液(基) 口服 bid 10ml 1 2022-05-05 09.54.38 李凌蔚\n[BBOX-2028] 药品 (盖克)小儿氨酚黄那敏颗粒 口服 tid 3g 2 2022-04-19 16.05.18 陈媛\n[BBOX-2029] 药品 乙1)美敏伪麻口服溶液 口服 tid 4ml 1 2022-04-19 16.05.18 陈媛\n[BBOX-2030] 药品 复方氨酚甲麻口服液 口服 qid 5ml 1 2022-04-19 16.05.18 陈媛\n[BBOX-2031] 共70条 20条/页 < 1 2 3 4 > 前往 3 页\n[BBOX-2032] 184-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>\n[BBOX-2033] 返回概览视图\n[BBOX-2034] 2026-02-12 11:40:02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森\n[BBOX-2035] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告\n[BBOX-2036] 请输入药品内容,按回车键检索\n[BBOX-2037] 查询全部\n[BBOX-2038] 类型 组 药品名称(规格)\n[BBOX-2039] 药品 甲)(小儿)双黄连口服液(基)\n[BBOX-2040] 药品 (盖克)小儿氨酚黄那敏颗粒\n[BBOX-2041] 药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(基)\n[BBOX-2042] 药品 蒲地蓝消炎口服液\n[BBOX-2043] 药品 复方氨酚甲麻口服液\n[BBOX-2044] 药品 (盖克)小儿氨酚黄那敏颗粒\n[BBOX-2045] 药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(国基)\n[BBOX-2046] 药品 乙0)(普米克令舒)吸入用布地奈德混悬液(国基)\n[BBOX-2047] 药品 右旋糖酐铁颗粒\n[BBOX-2048] 药品 盐酸氨卓斯丁滴眼液\n[BBOX-2049] 用法 频率 实际用量 总量 开立时间 开立医师\n[BBOX-2050] 口服 tid 10ml 1 2022-03-26 19:51:46 谭真真\n[BBOX-2051] 口服 tid 6g 2 2022-03-26 19:51:18 谭真真\n[BBOX-2052] 口服(继续 用药) bid 0.228g 2 2022-03-26 19:51:18 谭真真\n[BBOX-2053] 口服 bid 10ml 1 2022-03-26 19:51:18 谭真真\n[BBOX-2054] 口服 q6h 10ml 2 2021-11-04 17:18:07 宁秀琴\n[BBOX-2055] 口服 tid 12g 2 2021-11-04 17:18:07 宁秀琴\n[BBOX-2056] 口服(继续 用药) q12h 0.45g 2 2021-11-04 17:18:07 宁秀琴\n[BBOX-2057] 压缩雾化 bid 2ml 5 2021-10-11 10:07:54 张冬梅\n[BBOX-2058] 口服 tid 1袋 80 2021-09-28 15:12:34 党建华\n[BBOX-2059] 滴双眼 bid 0.1ml 1 2021-09-09 15:18:56 史艳艳\n[BBOX-2060] 共70条 20条/页 < 1 2 3 4 > 前往 4 页\n[BBOX-2061] CS 扫描全能王\n[BBOX-2062] 3亿人都在用的扫描App\n[BBOX-2063] \\begin{tabular}{llllllllll}\n[BBOX-2064] 报告时间: 2026-01-06\n[BBOX-2065] \\hline\n[BBOX-2066] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 & 提示 \\\\\n[BBOX-2067] \\hline\n[BBOX-2068] [WBC]白细胞数目 & & 4.28 & & 3.5~9.5 & 10^9/L & [HCT]红细胞压积 & & 37.8 & \\\\\n[BBOX-2069] [Lym\\%]淋巴细胞百分比 & & 28.4 & & 20~50 & \\% & [MCV]平均红细胞体积 & & 80.4 & $\\downarrow$ \\\\\n[BBOX-2070] [Mon\\%]单核细胞百分比 & & 4.7 & & 3~10 & \\% & [MCH]平均红细胞血红蛋白含量 & & 26.0 & $\\downarrow$ \\\\\n[BBOX-2071] [Neu\\%]中性粒细胞百分比 & & 64.4 & & 40~75 & \\% & [MCHC]平均红细胞血红蛋白浓度 & & 323 & \\\\\n[BBOX-2072] [Eos\\%]嗜酸性细胞百分比 & & 2.4 & & 0.4~8 & \\% & [RDW-CV]红细胞分布宽度变异系数 & & 15.2 & \\\\\n[BBOX-2073] [Bas\\%]嗜碱性细胞百分比 & & 0.1 & & 0.0~1.0 & \\% & [RDW-SD]红细胞分布宽度标准差 & & 43.0 & \\\\\n[BBOX-2074] [Lym\\#]淋巴细胞数目 & & 1.22 & & 1.1~3.2 & 10^9/L & [PLT]血小板数目 & & 224 & \\\\\n[BBOX-2075] [Mon\\#]单核细胞数目 & & 0.20 & & 0.1~0.6 & 10^9/L & [MPV]平均血小板体积 & & 8.0 & \\\\\n[BBOX-2076] [Neu\\#]中性粒细胞数目 & & 2.76 & & 1.8~6.3 & 10^9/L & [PDW]血小板分布宽度 & & 16.0 & \\\\\n[BBOX-2077] [Eos\\#]嗜酸性细胞数目 & & 0.10 & & 0.02~0.52 & 10^9/L & [PCT]血小板压积 & & 0.180 & \\\\\n[BBOX-2078] [Bas\\#]嗜碱性细胞数目 & & 0.00 & & 0.00~0.06 & 10^9/L & [P-LCR]大型血小板比率 & & 15.8 & \\\\\n[BBOX-2079] [RBC]红细胞数目 & & 4.70 & & 3.8~5.1 & 10^12/L & [IG\\%]未成熟粒细胞百分比 & & 0.4 & \\\\\n[BBOX-2080] [HGB]血红蛋白 & & 122 & & 115~150 & g/L & [IG\\#]未成熟粒细胞计数 & & 0.02 & \\\\\n[BBOX-2081] \\hline\n[BBOX-2082] \\end{tabular}\n[BBOX-2083] \\begin{tabular}{ccccccc}\n[BBOX-2084] 报告时间: 2026-01-06\n[BBOX-2085] \\hline\n[BBOX-2086] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n[BBOX-2087] \\hline\n[BBOX-2088] {[}ESR{]}血沉 & & 7 & & 0~20 & mm/h \\\\\n[BBOX-2089] \\hline\n[BBOX-2090] \\end{tabular}\n[BBOX-2091] \\begin{tabular}{ccccccl}\n[BBOX-2092] 报告时间: 2026-01-06\n[BBOX-2093] \\hline\n[BBOX-2094] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n[BBOX-2095] \\hline\n[BBOX-2096] [TBIL]总胆红素 & & 8.5 & & 0.0~21.0 & $\\mu$mol/L \\\\\n[BBOX-2097] [DBIL]直接胆红素 & & 2.3 & & 0.0~8.0 & $\\mu$mol/L \\\\\n[BBOX-2098] [IBIL]间接胆红素 & & 6.2 & & 0.0~13.0 & $\\mu$mol/L \\\\\n[BBOX-2099] [ALT]谷丙转氨酶 & & 12.2 & & 7~40 & U/L \\\\\n[BBOX-2100] [AST]谷草转氨酶 & & 18 & & 13~35 & U/L \\\\\n[BBOX-2101] [AST/ALT]谷草/谷丙 & & 1.48 & & 0.8~1.5 & \\\\\n[BBOX-2102] [TP]总蛋白 & & 73.6 & & 65.0~85.0 & g/L \\\\\n[BBOX-2103] [ALB]白蛋白 & & 46.0 & & 40.0~55.0 & g/L \\\\\n[BBOX-2104] [GLB]球蛋白 & & 27.6 & & 20.0~40.0 & g/L \\\\\n[BBOX-2105] [A/G]白球比值 & & 1.67 & & 1.20~2.4 & \\\\\n[BBOX-2106] [GGT]谷氨酰转肽酶 & & 9.0 & & 7~45 & U/L \\\\\n[BBOX-2107] [ALP]碱性磷酸酶 & & 66 & & 40~150 & U/L \\\\\n[BBOX-2108] [Urea]尿素 & & 4.27 & & 2.6~7.5 & mmol/L \\\\\n[BBOX-2109] [CRE]肌酐 & & 49.9 & & 41~73 & $\\mu$mol/L \\\\\n[BBOX-2110] \\hline\n[BBOX-2111] \\end{tabular}\n[BBOX-2112] \\begin{tabular}{lllll}\n[BBOX-2113] 报告时间: 2026-01-06\n[BBOX-2114] \\hline\n[BBOX-2115] \\multicolumn{2}{l}{\\textbf{瑞图RT-F600}} & \\multicolumn{3}{c}{\\textbf{医学检验科检验报告单}} \\\\\n[BBOX-2116] \\multicolumn{2}{l}{\\textbf{白带分析仪}} & \\multicolumn{3}{c}{} \\\\\n[BBOX-2117] \\multicolumn{2}{l}{\\textbf{姓 名:}} & \\multicolumn{2}{l}{\\textbf{送检科室: 妇科一病区(门)}} & \\multicolumn{1}{l}{\\textbf{床 号:}} \\\\\n[BBOX-2118] \\multicolumn{2}{l}{\\textbf{住院(门诊)号:}} & \\multicolumn{2}{l}{\\textbf{性 别: 女}} & \\multicolumn{1}{l}{\\textbf{年 龄: 41岁}} \\\\\n[BBOX-2119] \\multicolumn{2}{l}{\\textbf{检验项目: 妇科微生态}} & \\multicolumn{3}{l}{\\textbf{样本类型: 阴道分泌物}} \\\\\n[BBOX-2120] \\multicolumn{2}{l}{\\textbf{疾病诊断: 慢性盆腔痛}} & \\multicolumn{3}{l}{\\textbf{样本状态: 正常}} \\\\\n[BBOX-2121] \\hline\n[BBOX-2122] \\multicolumn{5}{l}{\\textbf{形态学检测项目:}} \\\\\n[BBOX-2123] \\multicolumn{2}{l}{细胞情况} & \\textbf{结果} & \\textbf{正常值范围} & \\textbf{镜下所见:} \\\\\n[BBOX-2124] \\multicolumn{2}{l}{清洁度} & Ⅱ & $\\sim \\le$II & \\\\\n[BBOX-2125] \\multicolumn{2}{l}{白细胞} & 5-15 & $\\le$15/HP & \\\\\n[BBOX-2126] \\multicolumn{2}{l}{红细胞} & 未检出 & $\\sim$未检出 & \\\\\n[BBOX-2127] \\multicolumn{2}{l}{线索细胞} & 未检出 & $\\sim$未检出 & \\\\\n[BBOX-2128] \\multicolumn{2}{l}{上皮细胞} & 10-15 & $\\sim$满视野 & \\\\\n[BBOX-2129] \\multicolumn{5}{l}{} \\\\\n[BBOX-2130] \\multicolumn{2}{l}{病原体情况:} & & & \\\\\n[BBOX-2131] \\multicolumn{2}{l}{滴虫} & 未检出 & $\\sim$未检出 & \\\\\n[BBOX-2132] \\multicolumn{2}{l}{菌丝} & 未检出 & $\\sim$未检出 & \\\\\n[BBOX-2133] \\multicolumn{2}{l}{孢子} & 未检出 & $\\sim$未检出 & \\\\\n[BBOX-2134] \\multicolumn{2}{l}{芽生孢子} & 未检出 & $\\sim$未检出 & \\\\\n[BBOX-2135] \\multicolumn{5}{l}{} \\\\\n[BBOX-2136] \\multicolumn{2}{l}{菌群情况:} & & & \\\\\n[BBOX-2137] \\multicolumn{2}{l}{菌群密集度} & ++ & $\\sim$++ & \\\\\n[BBOX-2138] \\multicolumn{2}{l}{多样性} & + & $\\sim$++ & \\\\\n[BBOX-2139] \\multicolumn{2}{l}{优势菌} & G+杆菌 & $\\sim$G阳性杆菌 & \\\\\n[BBOX-2140] \\multicolumn{2}{l}{$\\beta$-N-乙酰氨基葡萄糖苷酶(NAG)} & - & $\\sim$- & \\\\\n[BBOX-2141] \\multicolumn{5}{l}{} \\\\\n[BBOX-2142] \\multicolumn{2}{l}{功能学分析:} & & & \\\\\n[BBOX-2143] \\multicolumn{2}{l}{唾液酸苷酶} & - & $\\sim$- & \\\\\n[BBOX-2144] \\multicolumn{2}{l}{白细胞酯酶} & - & $\\sim$- & \\\\\n[BBOX-2145] \\multicolumn{2}{l}{胺试验} & - & $\\sim$- & \\\\\n[BBOX-2146] \\multicolumn{2}{l}{脯氨酸氨基肽酶PIP} & - & $\\sim$- & \\\\\n[BBOX-2147] \\multicolumn{2}{l}{过氧化氢(H2O2)} & + & $\\sim$- & \\\\\n[BBOX-2148] \\multicolumn{2}{l}{pH值} & 3.8 & 3.8 $\\sim$ 4.5 & \\\\\n[BBOX-2149] \\multicolumn{2}{l}{Nugent评分2} & \\multicolumn{2}{l}{AV评分1} & \\\\\n[BBOX-2150] \\hline\n[BBOX-2151] \\multicolumn{5}{l}{※ 备注:阴道微生态未见明显异常!} \\\\\n[BBOX-2152] \\hline\n[BBOX-2153] \\multicolumn{2}{l}{采集时间: 2026-01-06} & \\multicolumn{2}{l}{接收时间: 2026-01-06} & \\multicolumn{1}{l}{审核时间: 2026-01-06} \\\\\n[BBOX-2154] \\multicolumn{2}{l}{09:15} & \\multicolumn{2}{l}{09:22} & \\multicolumn{1}{l}{10:59} \\\\\n[BBOX-2155] \\multicolumn{2}{l}{送检医生: 权丽丽} & \\multicolumn{2}{l}{检验者: 伊原原} & \\multicolumn{1}{l}{审核者: 介倩倩} \\\\\n[BBOX-2156] \\multicolumn{5}{l}{打印时间: 2026/2/26 下午 3:59:58} \\\\\n[BBOX-2157] \\multicolumn{5}{l}{打印者: 网页打印} \\\\\n[BBOX-2158] \\multicolumn{5}{l}{※本报告检查结果实行互认制度,如有疑问,请在三天内和我们联系,电} \\\\\n[BBOX-2159] \\hline\n[BBOX-2160] \\end{tabular}\n[BBOX-2161] \\begin{tabular}{cccccc}\n[BBOX-2162] 报告时间: 2026-01-06\n[BBOX-2163] \\hline\n[BBOX-2164] 英文 & 项目名称 & 结果 & 参考范围 & 单位 & \\\\\n[BBOX-2165] \\hline\n[BBOX-2166] \\multicolumn{2}{l}{[\\beta-HCG]人绒毛膜促性腺激素} & 0.40 & \\begin{tabular}[c]{@{}c@{}}非孕期 0~2.9 \\\\ 0.2-1周 5~50 \\\\ 1-2周 50~500 \\\\ 2-3周 100~5000 \\\\ 3-4周 500~10000 \\\\ 4-5周 1000~50000 \\\\ 5-6周 10000~100000 \\\\ 6-8周 15000~200000\\end{tabular} & \\multicolumn{2}{c}{mIU/ml} \\\\\n[BBOX-2167] 报告时间: 2026-01-06\n[BBOX-2168] \\hline\n[BBOX-2169] \\end{tabular}\n[BBOX-2170] \\begin{tabular}{llllll}\n[BBOX-2171] 报告时间: 2026-01-06\n[BBOX-2172] \\hline\n[BBOX-2173] 采集时间: & 2026-01-06 & 接收时间: & 2026-01-06 & 审核时间: & 2026-01-06 \\\\\n[BBOX-2174] & 09:15 & & 10:03 & & 11:06 \\\\\n[BBOX-2175] 送检医生: & 权丽丽 & 检验者: & 秦淑云 & 审核者: & 薛轩 \\\\\n[BBOX-2176] \\hline\n[BBOX-2177] \\end{tabular}\n[BBOX-2178] \\begin{tabular}{llllll}\n[BBOX-2179] 报告时间: 2026-01-06\n[BBOX-2180] \\hline\n[BBOX-2181] \\multicolumn{6}{l}{\\textbf{※本报告检查结果实行互认制度，如有疑问，请在三天内和我们联系，电话：}} \\\\\n[BBOX-2182] \\multicolumn{6}{l}{\\textbf{打印时间: 2026/2/26 下午 4:00:10}} \\\\\n[BBOX-2183] \\multicolumn{6}{l}{\\textbf{打印者: 网页打印}} \\\\\n[BBOX-2184] \\multicolumn{6}{l}{\\textbf{※}} \\\\\n[BBOX-2185] \\hline\n[BBOX-2186] \\end{tabular}\n[BBOX-2187] \\begin{tabular}{ccccccc}\n[BBOX-2188] 报告时间: 2026-01-06\n[BBOX-2189] \\hline\n[BBOX-2190] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n[BBOX-2191] \\hline\n[BBOX-2192] [OV125Ag]CA-125 & & 59.70 & $\\uparrow$ & 0.00~35.00 & U/ml \\\\\n[BBOX-2193] \\hline\n[BBOX-2194] \\end{tabular}\n[BBOX-2195] \\begin{tabular}{ccccccccc}\n[BBOX-2196] 报告时间: 2026-01-06\n[BBOX-2197] \\hline\n[BBOX-2198] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n[BBOX-2199] \\hline\n[BBOX-2200] [颜色]颜色 & & 黄色 & & 清 & & [尿酸结晶]尿酸结晶 & & 0 & & 0~15 & 个/ul \\\\\n[BBOX-2201] [浊度]浊度 & & 清亮 & & 清 & & [草酸钙结晶]草酸钙结晶 & & 0 & & 0~30 & 个/ul \\\\\n[BBOX-2202] [GLU]葡萄糖 & & - & & 阴性 & & [上皮细胞]上皮细胞 & & 14 & & 0~20 & 个/ul \\\\\n[BBOX-2203] [BLD]潜血 & & - & & 阴性 & & [粘液丝]粘液丝 & & 5 & & 0~20 & 个/ul \\\\\n[BBOX-2204] [LEU]白细胞 & & 2+ & & 阴性 & & [酵母菌]酵母菌 & & 6 & $\\uparrow$ & 0~0 & 个/ul \\\\\n[BBOX-2205] [PRO]蛋白质 & & - & & 阴性 & & [透明管型]透明管型 & & 0 & & 0~1 & 个/ul \\\\\n[BBOX-2206] [NIT]亚硝酸盐 & & + & & 阴性 & & [颗粒管型]颗粒管型 & & 0 & & 0~0 & 个/ul \\\\\n[BBOX-2207] [URO]尿胆素原 & & - & & 阴性 & & [小圆上皮]小圆上皮 & & 0 & & 0~3 & 个/ul \\\\\n[BBOX-2208] [BIL]胆红素 & & - & & 阴性 & & [其他管型]其他管型 & & 0 & & 0~0 & 个/ul \\\\\n[BBOX-2209] [KET]酮体 & & - & & 阴性 & & [其他上皮]其他上皮 & & 0 & & 0~10 & 个/ul \\\\\n[BBOX-2210] [Vc]维生素C & & - & & - & & [异常红细胞]异常红细胞 & & 0 & & 0~5 & 个/ul \\\\\n[BBOX-2211] [pH]酸碱性 & & 6.0 & & 5.0~8.5 & & [细菌]细菌 & & 1072 & $\\uparrow$ & 0~50 & 个/ul \\\\\n[BBOX-2212] [SG]比重 & & 1.020 & & 1.010~ & & [尿沉渣镜检]尿沉渣镜检 & & : & & & \\\\\n[BBOX-2213] & & & & 1.025 & & [白细胞]白细胞 & & +++/HP & & $\\le$5/HP & \\\\\n[BBOX-2214] [红细胞]红细胞 & & 0 & & 0~5 & 个/ul & [红细胞]红细胞 & & 未查见 & & $\\le$3/HP & \\\\\n[BBOX-2215] [白细胞]白细胞 & & 218 & $\\uparrow$ & 0~7 & 个/ul & & & & & & \\\\\n[BBOX-2216] \\hline\n[BBOX-2217] \\end{tabular}\n[BBOX-2218] \\begin{tabular}{ccccccl}\n[BBOX-2219] 报告时间: 2026-01-15\n[BBOX-2220] \\hline\n[BBOX-2221] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n[BBOX-2222] \\hline\n[BBOX-2223] {[}PT{]}凝血酶原时间 & & 11.0 & & 9.4~12.5 & s \\\\\n[BBOX-2224] {[}INR{]}国际标准化比例 & & 0.98 & & 0.8~1.2 & INR \\\\\n[BBOX-2225] {[}HDD{]}凝血酶原活动度 & & 103.00 & & 70~130 & \\% \\\\\n[BBOX-2226] {[}APTT{]}部分凝血活酶时间(胶质硅) & & 33.7 & & 25.1~36.5 & s \\\\\n[BBOX-2227] {[}Fib{]}纤维蛋白原 & & 2.65 & & 2.00~4.00 & g/L \\\\\n[BBOX-2228] {[}TT{]}凝血酶时间 & & 15.1 & & 10.3~16.6 & s \\\\\n[BBOX-2229] \\hline\n[BBOX-2230] \\end{tabular}\n[BBOX-2231] \\begin{tabular}{ccccccccc}\n[BBOX-2232] 报告时间: 2026-01-15\n[BBOX-2233] \\hline\n[BBOX-2234] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n[BBOX-2235] \\hline\n[BBOX-2236] {[}WBC{]}白细胞数目 & & 4.20 & & 3.5~9.5 & 10^9/L & {[}HCT{]}红细胞压积 & & 38.3 & & 35~45 & \\% \\\\\n[BBOX-2237] {[}Lym\\%{]}淋巴细胞百分比 & & 28.6 & & 20~50 & \\% & {[}MCV{]}平均红细胞体积 & & 81.3 & $\\downarrow$ & 82~100 & fL \\\\\n[BBOX-2238] {[}Mon\\%{]}单核细胞百分比 & & 5.0 & & 3~10 & \\% & {[}MCH{]}平均红细胞血红蛋白含量 & & 25.6 & $\\downarrow$ & 27~34 & pg \\\\\n[BBOX-2239] {[}Neu\\%{]}中性粒细胞百分比 & & 64.5 & & 40~75 & \\% & {[}MCHC{]}平均红细胞血红蛋白浓度 & & 313 & $\\downarrow$ & 316~354 & g/L \\\\\n[BBOX-2240] {[}Eos\\%{]}嗜酸性细胞百分比 & & 1.7 & & 0.4~8 & \\% & {[}RDW-CV{]}红细胞分布宽度变异系数 & & 14.9 & & 11~16 & \\% \\\\\n[BBOX-2241] {[}Bas\\%{]}嗜碱性细胞百分比 & & 0.2 & & 0.0~1.0 & \\% & {[}RDW-SD{]}红细胞分布宽度标准差 & & 43.2 & & 35.0~56.0 & fL \\\\\n[BBOX-2242] {[}Lym\\# {]}淋巴细胞数目 & & 1.20 & & 1.1~3.2 & 10^9/L & {[}PLT{]}血小板数目 & & 288 & & 125~350 & 10^9/L \\\\\n[BBOX-2243] {[}Mon\\# {]}单核细胞数目 & & 0.21 & & 0.1~0.6 & 10^9/L & {[}MPV{]}平均血小板体积 & & 9.0 & & 6.5~12 & fL \\\\\n[BBOX-2244] {[}Neu\\# {]}中性粒细胞数目 & & 2.71 & & 1.8~6.3 & 10^9/L & {[}PDW{]}血小板分布宽度 & & 15.6 & & 9~17 & fL \\\\\n[BBOX-2245] {[}Eos\\# {]}嗜酸性细胞数目 & & 0.07 & & 0.02~0.52 & 10^9/L & {[}PCT{]}血小板压积 & & 0.258 & & 0.108~ & \\% \\\\\n[BBOX-2246] {[}Bas\\# {]}嗜碱性细胞数目 & & 0.01 & & 0.00~0.06 & 10^9/L & {[}P-LCR{]}大型血小板比率 & & 19.3 & & 11~45 & \\% \\\\\n[BBOX-2247] {[}RBC{]}红细胞数目 & & 4.71 & & 3.8~5.1 & 10^12/L & {[}IG\\%{]}未成熟粒细胞百分比 & & 0.1 & & 0.0~0.6 & \\% \\\\\n[BBOX-2248] {[}HGB{]}血红蛋白 & & 120 & & 115~150 & g/L & {[}IG\\# {]}未成熟粒细胞计数 & & 0.00 & & 0.00~0.06 & 10^9/L \\\\\n[BBOX-2249] \\hline\n[BBOX-2250] \\end{tabular}\n[BBOX-2251] \\begin{tabular}{ccccccccc}\n[BBOX-2252] 报告时间: 2026-01-15\n[BBOX-2253] \\hline\n[BBOX-2254] \\textbf{英文} & \\textbf{项目名称} & \\textbf{结果} & \\textbf{提示} & \\textbf{参考范围} & \\textbf{单位} & \\textbf{英文} & \\textbf{项目名称} & \\textbf{结果} & \\textbf{提示} & \\textbf{参考范围} & \\textbf{单位} \\\\\n[BBOX-2255] \\hline\n[BBOX-2256] {[TBIL]}总胆红素 & & 8.7 & & 0.0~21.0 & \\textmu mol/L & {[Cl]}氯 & & 105 & & 99~110 & mmol/L \\\\\n[BBOX-2257] {[DBIL]}直接胆红素 & & 3.5 & & 0.0~8.0 & \\textmu mol/L & {[Ca]}钙 & & 2.38 & & 2.11~2.52 & mmol/L \\\\\n[BBOX-2258] {[IBIL]}间接胆红素 & & 5.2 & & 0.0~13.0 & \\textmu mol/L & {[CO2cp]}二氧化碳结合力 & & 27.6 & & 21.0~31.0 & mmol/L \\\\\n[BBOX-2259] {[ALT]}谷丙转氨酶 & & 7.0 & & 7~40 & U/L & {[m-AST]}谷草转氨酶线粒体同工酶 & & 2.0 & & 0~18 & U/L \\\\\n[BBOX-2260] {[AST]}谷草转氨酶 & & 15 & & 13~35 & U/L & {[CK]}肌酸激酶 & & 37 & & 24~200 & U/L \\\\\n[BBOX-2261] {[AST/ALT]}谷草/谷丙 & 2.14 & & \\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\\n[BBOX-2262] \\begin{tabular}{ccccccccc}\n[BBOX-2263] 报告时间: 2026-01-15\n[BBOX-2264] \\hline\n[BBOX-2265] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 \\\\\n[BBOX-2266] \\hline\n[BBOX-2267] [颜色]颜色 & 黄色 & & & 黄、淡黄 & & [SG]尿比重 & 1.020 & 1.003~ \\\\\n[BBOX-2268] [浊度]浊度 & 清亮 & & & 清 & & [VC]维生素C & 0.0 & - \\\\\n[BBOX-2269] [GLU]葡萄糖 & - & & & - & & [WBC]白细胞 & 28.00 & 0~28 \\\\\n[BBOX-2270] [NQX]尿潜血 & - & & & - & mg/l & [RBC]红细胞 & 6.00 & 0~17 \\\\\n[BBOX-2271] [LEU]白细胞 & - & & & - & & [粘液丝]粘液丝 & 11 & 0~28 \\\\\n[BBOX-2272] [PRO]尿蛋白 & - & & & - & & [结晶]结晶 & 0.0 & 0~28 \\\\\n[BBOX-2273] [NIT]亚硝酸盐 & + & & & - & & [管型]管型 & 0 & 0~2 \\\\\n[BBOX-2274] [URO]尿胆原 & - & & & - & & [EC]上皮细胞 & 39.00 & 0~34 \\\\\n[BBOX-2275] [BIL]胆红素 & - & & & - & & [BACT细菌]细菌 & 163.00 & 0~7 \\\\\n[BBOX-2276] [KET]尿酮体 & - & & & - & & [BYST真菌]真菌 & 0 & 0~1 \\\\\n[BBOX-2277] [pH]pH值 & 6.0 & & & 4.5~8.0 & & & & \\\\\n[BBOX-2278] \\hline\n[BBOX-2279] \\end{tabular}\n[BBOX-2280] \\begin{tabular}{ccccccc}\n[BBOX-2281] 报告时间: 2026-01-15\n[BBOX-2282] \\hline\n[BBOX-2283] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n[BBOX-2284] \\hline\n[BBOX-2285] [FT3]游离三碘甲状腺原氨酸 & & 3.11 & & 2.14~4.21 & pg/mL \\\\\n[BBOX-2286] [FRt4]游离甲状腺素 & & 0.76 & & 0.61~1.12 & ng/dL \\\\\n[BBOX-2287] [fTSH3]超敏促甲状腺素 & & 1.350 & & 0.560~5.910 & uIU/ml \\\\\n[BBOX-2288] \\hline\n[BBOX-2289] \\end{tabular}\n[BBOX-2290] \\begin{tabular}{ccccccc}\n[BBOX-2291] 报告时间: 2026-01-15\n[BBOX-2292] \\hline\n[BBOX-2293] 英文 & 项目名称 & 结果 & SCO & 提示 & 参考范围 & 单位 \\\\\n[BBOX-2294] \\hline\n[BBOX-2295] {[HBsAg]}乙肝表面抗原(酶免法) & 阴性 & 0.04 & 阴性 & s/co & & \\\\\n[BBOX-2296] {[抗-HCV]}丙肝抗体(酶免法) & 阴性 & 0.15 & 阴性 & s/co & & \\\\\n[BBOX-2297] {[抗-HIV]}人免疫缺陷病毒抗体(酶免法) & 阴性 & 0.06 & 阴性 & s/co & & \\\\\n[BBOX-2298] {[TP-Ab]}梅毒螺旋体抗体(酶免法) & 阴性 & 0.07 & 阴性 & s/co & & \\\\\n[BBOX-2299] \\hline\n[BBOX-2300] \\end{tabular}\n[BBOX-2301] 处方笺\n[BBOX-2302] 4970401\n[BBOX-2303] 姓名：\n[BBOX-2304] 性别：□男 □女 年龄：60岁\n[BBOX-2305] 科别： 费别： 电话/住址：\n[BBOX-2306] 过敏史：无 开具日期：2021年2月16日\n[BBOX-2307] 临床诊断：支气管哮喘\n[BBOX-2308] Rp\n[BBOX-2309] 孟鲁司特钠片 10mg 2板\n[BBOX-2310] 用法：二天一次 1片\n[BBOX-2311] 审核： 调配： 医师：\n[BBOX-2312] 核对： 发药： 金额："
  }
]
2026-08-05 10:57:33,346 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T10:57:33.344+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 10:58:03,389 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T10:58:03.387+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 10:58:33,419 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T10:58:33.418+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 10:58:47,104 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 10:58:47,135 INFO     29 [SmartSplitter] SmartSplitter done: 37 chunks from 37 LLM segments (all bbox_id). Types: {'ExaminationReport': 5, 'AdmissionRecord': 1, 'DischargeRecord': 1, 'OutpatientRecord': 14, 'LabReport': 15, 'PrescriptionRecord': 1}
2026-08-05 10:58:47,148 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-05 10:58:47,148 INFO     29 [Trace] task=39f07238 | doc=DAXI-哮喘.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "2313 items", "markdown": "", "text": "", "name": "DAXI-哮喘.pdf", "output_format": "chunks", "chunks": "37 items, types={'ExaminationReport': 5, 'AdmissionRecord': 1, 'DischargeRecord': 1, 'OutpatientRecord': 14, 'LabReport': 15, 'PrescriptionRecord': 1}"}
2026-08-05 10:58:47,149 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-05 10:58:47,151 INFO     29 [ChunkRouter] Routed 37 chunks into 6 groups: {'chunks_Examination': 5, 'chunks_Admission': 1, 'chunks_Discharge': 1, 'chunks_Clinical': 14, 'chunks_LabExam': 15, 'chunks_Prescription': 1}
2026-08-05 10:58:47,167 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-05 10:58:47,168 INFO     29 [Trace] task=39f07238 | doc=DAXI-哮喘.pdf | ChunkRouter:Router | outputs={"html": "", "json": "2313 items", "markdown": "", "text": "", "name": "DAXI-哮喘.pdf", "output_format": "chunks", "chunks": "37 items, types={'ExaminationReport': 5, 'AdmissionRecord': 1, 'DischargeRecord': 1, 'OutpatientRecord': 14, 'LabReport': 15, 'PrescriptionRecord': 1}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "14 items, types={'OutpatientRecord': 14}", "chunks_LabExam": "15 items, types={'LabReport': 15}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 14, \"chunks_LabExam\": 15, \"chunks_Prescription\": 1}"}
2026-08-05 10:58:47,168 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-05 10:58:47,176 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 10:58:47,176 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[38]
2026-08-05 10:58:47,176 INFO     29 [qwen-vl-table] positions ： [[38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0], [38, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 10:58:47,409 INFO     29 [qwen-vl-table] page=38, rect=842x595, img=(2339x1653)
2026-08-05 10:58:47,409 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 10:58:47,409 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2063, \"bbox_end\": 2082, \"encounter_dates\": [\"2026-01-06\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllllll}\n报告时间: 2026-01-06\n\\hline\n英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 & 提示 \\\\\n\\hline\n[WBC]白细胞数目 & & 4.28 & & 3.5~9.5 & 10^9/L & [HCT]红细胞压积 & & 37.8 & \\\\\n[Lym\\%]淋巴细胞百分比 & & 28.4 & & 20~50 & \\% & [MCV]平均红细胞体积 & & 80.4 & $\\downarrow$ \\\\\n[Mon\\%]单核细胞百分比 & & 4.7 & & 3~10 & \\% & [MCH]平均红细胞血红蛋白含量 & & 26.0 & $\\downarrow$ \\\\\n[Neu\\%]中性粒细胞百分比 & & 64.4 & & 40~75 & \\% & [MCHC]平均红细胞血红蛋白浓度 & & 323 & \\\\\n[Eos\\%]嗜酸性细胞百分比 & & 2.4 & & 0.4~8 & \\% & [RDW-CV]红细胞分布宽度变异系数 & & 15.2 & \\\\\n[Bas\\%]嗜碱性细胞百分比 & & 0.1 & & 0.0~1.0 & \\% & [RDW-SD]红细胞分布宽度标准差 & & 43.0 & \\\\\n[Lym\\#]淋巴细胞数目 & & 1.22 & & 1.1~3.2 & 10^9/L & [PLT]血小板数目 & & 224 & \\\\\n[Mon\\#]单核细胞数目 & & 0.20 & & 0.1~0.6 & 10^9/L & [MPV]平均血小板体积 & & 8.0 & \\\\\n[Neu\\#]中性粒细胞数目 & & 2.76 & & 1.8~6.3 & 10^9/L & [PDW]血小板分布宽度 & & 16.0 & \\\\\n[Eos\\#]嗜酸性细胞数目 & & 0.10 & & 0.02~0.52 & 10^9/L & [PCT]血小板压积 & & 0.180 & \\\\\n[Bas\\#]嗜碱性细胞数目 & & 0.00 & & 0.00~0.06 & 10^9/L & [P-LCR]大型血小板比率 & & 15.8 & \\\\\n[RBC]红细胞数目 & & 4.70 & & 3.8~5.1 & 10^12/L & [IG\\%]未成熟粒细胞百分比 & & 0.4 & \\\\\n[HGB]血红蛋白 & & 122 & & 115~150 & g/L & [IG\\#]未成熟粒细胞计数 & & 0.02 & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
[92m10:58:47 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 10:58:47,410 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 10:59:03,438 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T10:59:03.438+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 10:59:06,088 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 10:59:06,088 INFO     29 [qwen-vl-table] page=38 LLM output (len=4363):
{
  "report_date": "2026-01-06",
  "items": [
    {
      "name": "白细胞数目",
      "item_code": "WBC",
      "value": "4.28",
      "unit": "10^9/L",
      "reference_range": "3.5~9.5",
      "abnormal": false
    },
    {
      "name": "淋巴细胞百分比",
      "item_code": "Lym%",
      "value": "28.4",
      "unit": "%",
      "reference_range": "20~50",
      "abnormal": false
    },
    {
      "name": "单核细胞百分比",
      "item_code": "Mon%",
      "value": "4.7",
      "unit": "%",
      "reference_range": "3~10",
      "abnormal": false
    },
    {
      "name": "中性粒细胞百分比",
      "item_code": "Neu%",
      "value": "64.4",
      "unit": "%",
      "reference_range": "40~75",
      "abnormal": false
    },
    {
      "name": "嗜酸性细胞百分比",
      "item_code": "Eos%",
      "value": "2.4",
      "unit": "%",
      "reference_range": "0.4~8",
      "abnormal": false
    },
    {
      "name": "嗜碱性细胞百分比",
      "item_code": "Bas%",
      "value": "0.1",
      "unit": "%",
      "reference_range": "0.0~1.0",
      "abnormal": false
    },
    {
      "name": "淋巴细胞数目",
      "item_code": "Lym#",
      "value": "1.22",
      "unit": "10^9/L",
      "reference_range": "1.1~3.2",
      "abnormal": false
    },
    {
      "name": "单核细胞数目",
      "item_code": "Mon#",
      "value": "0.20",
      "unit": "10^9/L",
      "reference_range": "0.1~0.6",
      "abnormal": false
    },
    {
      "name": "中性粒细胞数目",
      "item_code": "Neu#",
      "value": "2.76",
      "unit": "10^9/L",
      "reference_range": "1.8~6.3",
      "abnormal": false
    },
    {
      "name": "嗜酸性细胞数目",
      "item_code": "Eos#",
      "value": "0.10",
      "unit": "10^9/L",
      "reference_range": "0.02~0.52",
      "abnormal": false
    },
    {
      "name": "嗜碱性细胞数目",
      "item_code": "Bas#",
      "value": "0.00",
      "unit": "10^9/L",
      "reference_range": "0.00~0.06",
      "abnormal": false
    },
    {
      "name": "红细胞数目",
      "item_code": "RBC",
      "value": "4.70",
      "unit": "10^12/L",
      "reference_range": "3.8~5.1",
      "abnormal": false
    },
    {
      "name": "血红蛋白",
      "item_code": "HGB",
      "value": "122",
      "unit": "g/L",
      "reference_range": "115~150",
      "abnormal": false
    },
    {
      "name": "红细胞压积",
      "item_code": "HCT",
      "value": "37.8",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "平均红细胞体积",
      "item_code": "MCV",
      "value": "80.4",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "平均红细胞血红蛋白含量",
      "item_code": "MCH",
      "value": "26.0",
      "unit": null,
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "平均红细胞血红蛋白浓度",
      "item_code": "MCHC",
      "value": "323",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "红细胞分布宽度变异系数",
      "item_code": "RDW-CV",
      "value": "15.2",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "红细胞分布宽度标准差",
      "item_code": "RDW-SD",
      "value": "43.0",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "血小板数目",
      "item_code": "PLT",
      "value": "224",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "平均血小板体积",
      "item_code": "MPV",
      "value": "8.0",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "血小板分布宽度",
      "item_code": "PDW",
      "value": "16.0",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "血小板压积",
      "item_code": "PCT",
      "value": "0.180",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "大型血小板比率",
      "item_code": "P-LCR",
      "value": "15.8",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "未成熟粒细胞百分比",
      "item_code": "IG%",
      "value": "0.4",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "未成熟粒细胞计数",
      "item_code": "IG#",
      "value": "0.02",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-05 10:59:06,088 INFO     29 [qwen-vl-table] coord grouping: {38: 26}
2026-08-05 10:59:06,091 INFO     29 [qwen-vl-table] coord API call start, page=38, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1409516, prompt_len=720
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
白细胞数目、淋巴细胞百分比、单核细胞百分比、中性粒细胞百分比、嗜酸性细胞百分比、嗜碱性细胞百分比、淋巴细胞数目、单核细胞数目、中性粒细胞数目、嗜酸性细胞数目、嗜碱性细胞数目、红细胞数目、血红蛋白、红细胞压积、平均红细胞体积、平均红细胞血红蛋白含量、平均红细胞血红蛋白浓度、红细胞分布宽度变异系数、红细胞分布宽度标准差、血小板数目、平均血小板体积、血小板分布宽度、血小板压积、大型血小板比率、未成熟粒细胞百分比、未成熟粒细胞计数

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
2026-08-05 10:59:14,073 INFO     29 [qwen-vl-table] coord API raw response (len=1360):
[
	{"text": "白细胞数目", "bbox": [157, 279, 262, 300]},
	{"text": "淋巴细胞百分比", "bbox": [157, 307, 298, 328]},
	{"text": "单核细胞百分比", "bbox": [157, 335, 301, 356]},
	{"text": "中性粒细胞百分比", "bbox": [157, 362, 298, 383]},
	{"text": "嗜酸性细胞百分比", "bbox": [157, 409, 293, 430]},
	{"text": "嗜碱性细胞百分比", "bbox": [157, 457, 293, 478]},
	{"text": "淋巴细胞数目", "bbox": [157, 507, 280, 528]},
	{"text": "单核细胞数目", "bbox": [157, 534, 283, 555]},
	{"text": "中性粒细胞数目", "bbox": [157, 562, 293, 583]},
	{"text": "嗜酸性细胞数目", "bbox": [157, 590, 289, 611]},
	{"text": "嗜碱性细胞数目", "bbox": [157, 617, 289, 638]},
	{"text": "红细胞数目", "bbox": [157, 645, 257, 666]},
	{"text": "血红蛋白", "bbox": [157, 673, 247, 694]},
	{"text": "红细胞压积", "bbox": [505, 279, 607, 300]},
	{"text": "平均红细胞体积", "bbox": [505, 307, 638, 328]},
	{"text": "平均红细胞血红蛋白含量", "bbox": [505, 335, 651, 356]},
	{"text": "平均红细胞血红蛋白浓度", "bbox": [505, 383, 648, 404]},
	{"text": "红细胞分布宽度变异系数", "bbox": [505, 430, 650, 451]},
	{"text": "红细胞分布宽度标准差", "bbox": [505, 478, 650, 500]},
	{"text": "血小板数目", "bbox": [505, 528, 602, 549]},
	{"text": "平均血小板体积", "bbox": [505, 555, 637, 576]},
	{"text": "血小板分布宽度", "bbox": [505, 583, 638, 604]},
	{"text": "血小板压积", "bbox": [505, 621, 604, 642]},
	{"text": "大型血小板比率", "bbox": [505, 660, 644, 681]},
	{"text": "未成熟粒细胞百分比", "bbox": [505, 687, 644, 708]},
	{"text": "未成熟粒细胞计数", "bbox": [505, 736, 643, 757]}
]
2026-08-05 10:59:14,073 INFO     29 [qwen-vl-table] coord API: raw_items=26, valid_items=26, elapsed=8.0s
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[0]: text=白细胞数目, bbox=[157, 279, 262, 300]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[1]: text=淋巴细胞百分比, bbox=[157, 307, 298, 328]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[2]: text=单核细胞百分比, bbox=[157, 335, 301, 356]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[3]: text=中性粒细胞百分比, bbox=[157, 362, 298, 383]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[4]: text=嗜酸性细胞百分比, bbox=[157, 409, 293, 430]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[5]: text=嗜碱性细胞百分比, bbox=[157, 457, 293, 478]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[6]: text=淋巴细胞数目, bbox=[157, 507, 280, 528]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[7]: text=单核细胞数目, bbox=[157, 534, 283, 555]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[8]: text=中性粒细胞数目, bbox=[157, 562, 293, 583]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[9]: text=嗜酸性细胞数目, bbox=[157, 590, 289, 611]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[10]: text=嗜碱性细胞数目, bbox=[157, 617, 289, 638]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[11]: text=红细胞数目, bbox=[157, 645, 257, 666]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[12]: text=血红蛋白, bbox=[157, 673, 247, 694]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[13]: text=红细胞压积, bbox=[505, 279, 607, 300]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[14]: text=平均红细胞体积, bbox=[505, 307, 638, 328]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[15]: text=平均红细胞血红蛋白含量, bbox=[505, 335, 651, 356]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[16]: text=平均红细胞血红蛋白浓度, bbox=[505, 383, 648, 404]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[17]: text=红细胞分布宽度变异系数, bbox=[505, 430, 650, 451]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[18]: text=红细胞分布宽度标准差, bbox=[505, 478, 650, 500]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[19]: text=血小板数目, bbox=[505, 528, 602, 549]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[20]: text=平均血小板体积, bbox=[505, 555, 637, 576]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[21]: text=血小板分布宽度, bbox=[505, 583, 638, 604]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[22]: text=血小板压积, bbox=[505, 621, 604, 642]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[23]: text=大型血小板比率, bbox=[505, 660, 644, 681]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[24]: text=未成熟粒细胞百分比, bbox=[505, 687, 644, 708]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] coord item[25]: text=未成熟粒细胞计数, bbox=[505, 736, 643, 757]
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] page=38 coord: matched 26/26, time=8.0s
2026-08-05 10:59:14,074 INFO     29 [qwen-vl-table] new_positions (26):
[[39, 132.194, 220.60399999999998, 166.005, 178.5], [39, 132.194, 250.916, 182.665, 195.16], [39, 132.194, 253.44199999999998, 199.325, 211.82], [39, 132.194, 250.916, 215.39, 227.885], [39, 132.194, 246.706, 243.355, 255.85], [39, 132.194, 246.706, 271.91499999999996, 284.40999999999997], [39, 132.194, 235.76, 301.66499999999996, 314.15999999999997], [39, 132.194, 238.286, 317.72999999999996, 330.22499999999997], [39, 132.194, 246.706, 334.39, 346.885], [39, 132.194, 243.338, 351.05, 363.54499999999996], [39, 132.194, 243.338, 367.115, 379.60999999999996], [39, 132.194, 216.394, 383.775, 396.27], [39, 132.194, 207.974, 400.435, 412.93], [39, 425.21, 511.094, 166.005, 178.5], [39, 425.21, 537.196, 182.665, 195.16], [39, 425.21, 548.1419999999999, 199.325, 211.82], [39, 425.21, 545.616, 227.885, 240.38], [39, 425.21, 547.3, 255.85, 268.34499999999997], [39, 425.21, 547.3, 284.40999999999997, 297.5], [39, 425.21, 506.88399999999996, 314.15999999999997, 326.655], [39, 425.21, 536.3539999999999, 330.22499999999997, 342.71999999999997], [39, 425.21, 537.196, 346.885, 359.38], [39, 425.21, 508.568, 369.495, 381.99], [39, 425.21, 542.2479999999999, 392.7, 405.195], [39, 425.21, 542.2479999999999, 408.765, 421.26], [39, 425.21, 541.406, 437.91999999999996, 450.41499999999996]]
2026-08-05 10:59:14,075 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=26, matched=26, pages=1, time=26.9s
2026-08-05 10:59:14,076 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 10:59:14,077 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[39]
2026-08-05 10:59:14,077 INFO     29 [qwen-vl-table] positions ： [[39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0], [39, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 10:59:14,246 INFO     29 [qwen-vl-table] page=39, rect=842x595, img=(2339x1653)
2026-08-05 10:59:14,247 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 10:59:14,247 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2083, \"bbox_end\": 2090, \"encounter_dates\": [\"2026-01-06\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccc}\n报告时间: 2026-01-06\n\\hline\n英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n\\hline\n{[}ESR{]}血沉 & & 7 & & 0~20 & mm/h \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
[92m10:59:14 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 10:59:14,250 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 10:59:16,114 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 10:59:16,114 INFO     29 [qwen-vl-table] page=39 LLM output (len=208):
{
  "report_date": "2026-01-06",
  "items": [
    {
      "name": "血沉",
      "item_code": "ESR",
      "value": "7",
      "unit": "mm/h",
      "reference_range": "0~20",
      "abnormal": false
    }
  ]
}
2026-08-05 10:59:16,114 INFO     29 [qwen-vl-table] coord grouping: {39: 1}
2026-08-05 10:59:16,116 INFO     29 [qwen-vl-table] coord API call start, page=39, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=711709, prompt_len=509
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
血沉

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
2026-08-05 10:59:17,723 INFO     29 [qwen-vl-table] coord API raw response (len=61):
```json
[
	{"text": "血沉", "bbox": [188, 210, 260, 234]}
]
```
2026-08-05 10:59:17,724 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=1.6s
2026-08-05 10:59:17,724 INFO     29 [qwen-vl-table] coord item[0]: text=血沉, bbox=[188, 210, 260, 234]
2026-08-05 10:59:17,724 INFO     29 [qwen-vl-table] page=39 coord: matched 1/1, time=1.6s
2026-08-05 10:59:17,724 INFO     29 [qwen-vl-table] new_positions (1):
[[40, 158.296, 218.92, 124.94999999999999, 139.23]]
2026-08-05 10:59:17,724 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=3.6s
2026-08-05 10:59:17,726 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 10:59:17,726 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[40]
2026-08-05 10:59:17,726 INFO     29 [qwen-vl-table] positions ： [[40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0], [40, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 10:59:17,927 INFO     29 [qwen-vl-table] page=40, rect=842x595, img=(2339x1653)
2026-08-05 10:59:17,927 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 10:59:17,927 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2091, \"bbox_end\": 2111, \"encounter_dates\": [\"2026-01-06\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccl}\n报告时间: 2026-01-06\n\\hline\n英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n\\hline\n[TBIL]总胆红素 & & 8.5 & & 0.0~21.0 & $\\mu$mol/L \\\\\n[DBIL]直接胆红素 & & 2.3 & & 0.0~8.0 & $\\mu$mol/L \\\\\n[IBIL]间接胆红素 & & 6.2 & & 0.0~13.0 & $\\mu$mol/L \\\\\n[ALT]谷丙转氨酶 & & 12.2 & & 7~40 & U/L \\\\\n[AST]谷草转氨酶 & & 18 & & 13~35 & U/L \\\\\n[AST/ALT]谷草/谷丙 & & 1.48 & & 0.8~1.5 & \\\\\n[TP]总蛋白 & & 73.6 & & 65.0~85.0 & g/L \\\\\n[ALB]白蛋白 & & 46.0 & & 40.0~55.0 & g/L \\\\\n[GLB]球蛋白 & & 27.6 & & 20.0~40.0 & g/L \\\\\n[A/G]白球比值 & & 1.67 & & 1.20~2.4 & \\\\\n[GGT]谷氨酰转肽酶 & & 9.0 & & 7~45 & U/L \\\\\n[ALP]碱性磷酸酶 & & 66 & & 40~150 & U/L \\\\\n[Urea]尿素 & & 4.27 & & 2.6~7.5 & mmol/L \\\\\n[CRE]肌酐 & & 49.9 & & 41~73 & $\\mu$mol/L \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
[92m10:59:17 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 10:59:17,928 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 10:59:28,257 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 10:59:28,257 INFO     29 [qwen-vl-table] page=40 LLM output (len=2371):
{
  "report_date": "2026-01-06",
  "items": [
    {
      "name": "总胆红素",
      "item_code": "TBIL",
      "value": "8.5",
      "unit": "μmol/L",
      "reference_range": "0.0~21.0",
      "abnormal": false
    },
    {
      "name": "直接胆红素",
      "item_code": "DBIL",
      "value": "2.3",
      "unit": "μmol/L",
      "reference_range": "0.0~8.0",
      "abnormal": false
    },
    {
      "name": "间接胆红素",
      "item_code": "IBIL",
      "value": "6.2",
      "unit": "μmol/L",
      "reference_range": "0.0~13.0",
      "abnormal": false
    },
    {
      "name": "谷丙转氨酶",
      "item_code": "ALT",
      "value": "12.2",
      "unit": "U/L",
      "reference_range": "7~40",
      "abnormal": false
    },
    {
      "name": "谷草转氨酶",
      "item_code": "AST",
      "value": "18",
      "unit": "U/L",
      "reference_range": "13~35",
      "abnormal": false
    },
    {
      "name": "谷草/谷丙",
      "item_code": "AST/ALT",
      "value": "1.48",
      "unit": null,
      "reference_range": "0.8~1.5",
      "abnormal": false
    },
    {
      "name": "总蛋白",
      "item_code": "TP",
      "value": "73.6",
      "unit": "g/L",
      "reference_range": "65.0~85.0",
      "abnormal": false
    },
    {
      "name": "白蛋白",
      "item_code": "ALB",
      "value": "46.0",
      "unit": "g/L",
      "reference_range": "40.0~55.0",
      "abnormal": false
    },
    {
      "name": "球蛋白",
      "item_code": "GLB",
      "value": "27.6",
      "unit": "g/L",
      "reference_range": "20.0~40.0",
      "abnormal": false
    },
    {
      "name": "白球比值",
      "item_code": "A/G",
      "value": "1.67",
      "unit": null,
      "reference_range": "1.20~2.4",
      "abnormal": false
    },
    {
      "name": "谷氨酰转肽酶",
      "item_code": "GGT",
      "value": "9.0",
      "unit": "U/L",
      "reference_range": "7~45",
      "abnormal": false
    },
    {
      "name": "碱性磷酸酶",
      "item_code": "ALP",
      "value": "66",
      "unit": "U/L",
      "reference_range": "40~150",
      "abnormal": false
    },
    {
      "name": "尿素",
      "item_code": "Urea",
      "value": "4.27",
      "unit": "mmol/L",
      "reference_range": "2.6~7.5",
      "abnormal": false
    },
    {
      "name": "肌酐",
      "item_code": "CRE",
      "value": "49.9",
      "unit": "μmol/L",
      "reference_range": "41~73",
      "abnormal": false
    }
  ]
}
2026-08-05 10:59:28,257 INFO     29 [qwen-vl-table] coord grouping: {40: 14}
2026-08-05 10:59:28,260 INFO     29 [qwen-vl-table] coord API call start, page=40, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1082685, prompt_len=577
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
总胆红素、直接胆红素、间接胆红素、谷丙转氨酶、谷草转氨酶、谷草/谷丙、总蛋白、白蛋白、球蛋白、白球比值、谷氨酰转肽酶、碱性磷酸酶、尿素、肌酐

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
2026-08-05 10:59:33,051 INFO     29 [qwen-vl-table] coord API raw response (len=701):
```json
[
	{"text": "总胆红素", "bbox": [109, 309, 210, 334]},
	{"text": "直接胆红素", "bbox": [109, 340, 227, 365]},
	{"text": "间接胆红素", "bbox": [109, 370, 220, 395]},
	{"text": "谷丙转氨酶", "bbox": [109, 401, 220, 426]},
	{"text": "谷草转氨酶", "bbox": [109, 432, 220, 457]},
	{"text": "谷草/谷丙", "bbox": [109, 463, 247, 488]},
	{"text": "总蛋白", "bbox": [109, 494, 180, 519]},
	{"text": "白蛋白", "bbox": [109, 525, 190, 550]},
	{"text": "球蛋白", "bbox": [109, 556, 190, 581]},
	{"text": "白球比值", "bbox": [109, 587, 207, 612]},
	{"text": "谷氨酰转肽酶", "bbox": [109, 618, 240, 643]},
	{"text": "碱性磷酸酶", "bbox": [109, 650, 220, 675]},
	{"text": "尿素", "bbox": [109, 681, 182, 706]},
	{"text": "肌酐", "bbox": [109, 712, 177, 737]}
]
```
2026-08-05 10:59:33,051 INFO     29 [qwen-vl-table] coord API: raw_items=14, valid_items=14, elapsed=4.8s
2026-08-05 10:59:33,051 INFO     29 [qwen-vl-table] coord item[0]: text=总胆红素, bbox=[109, 309, 210, 334]
2026-08-05 10:59:33,051 INFO     29 [qwen-vl-table] coord item[1]: text=直接胆红素, bbox=[109, 340, 227, 365]
2026-08-05 10:59:33,051 INFO     29 [qwen-vl-table] coord item[2]: text=间接胆红素, bbox=[109, 370, 220, 395]
2026-08-05 10:59:33,051 INFO     29 [qwen-vl-table] coord item[3]: text=谷丙转氨酶, bbox=[109, 401, 220, 426]
2026-08-05 10:59:33,051 INFO     29 [qwen-vl-table] coord item[4]: text=谷草转氨酶, bbox=[109, 432, 220, 457]
2026-08-05 10:59:33,051 INFO     29 [qwen-vl-table] coord item[5]: text=谷草/谷丙, bbox=[109, 463, 247, 488]
2026-08-05 10:59:33,051 INFO     29 [qwen-vl-table] coord item[6]: text=总蛋白, bbox=[109, 494, 180, 519]
2026-08-05 10:59:33,051 INFO     29 [qwen-vl-table] coord item[7]: text=白蛋白, bbox=[109, 525, 190, 550]
2026-08-05 10:59:33,051 INFO     29 [qwen-vl-table] coord item[8]: text=球蛋白, bbox=[109, 556, 190, 581]
2026-08-05 10:59:33,051 INFO     29 [qwen-vl-table] coord item[9]: text=白球比值, bbox=[109, 587, 207, 612]
2026-08-05 10:59:33,051 INFO     29 [qwen-vl-table] coord item[10]: text=谷氨酰转肽酶, bbox=[109, 618, 240, 643]
2026-08-05 10:59:33,051 INFO     29 [qwen-vl-table] coord item[11]: text=碱性磷酸酶, bbox=[109, 650, 220, 675]
2026-08-05 10:59:33,051 INFO     29 [qwen-vl-table] coord item[12]: text=尿素, bbox=[109, 681, 182, 706]
2026-08-05 10:59:33,051 INFO     29 [qwen-vl-table] coord item[13]: text=肌酐, bbox=[109, 712, 177, 737]
2026-08-05 10:59:33,052 INFO     29 [qwen-vl-table] page=40 coord: matched 14/14, time=4.8s
2026-08-05 10:59:33,052 INFO     29 [qwen-vl-table] new_positions (14):
[[41, 91.77799999999999, 176.82, 183.855, 198.73], [41, 91.77799999999999, 191.134, 202.29999999999998, 217.17499999999998], [41, 91.77799999999999, 185.23999999999998, 220.14999999999998, 235.02499999999998], [41, 91.77799999999999, 185.23999999999998, 238.595, 253.47], [41, 91.77799999999999, 185.23999999999998, 257.03999999999996, 271.91499999999996], [41, 91.77799999999999, 207.974, 275.485, 290.36], [41, 91.77799999999999, 151.56, 293.93, 308.805], [41, 91.77799999999999, 159.98, 312.375, 327.25], [41, 91.77799999999999, 159.98, 330.82, 345.695], [41, 91.77799999999999, 174.29399999999998, 349.265, 364.14], [41, 91.77799999999999, 202.07999999999998, 367.71, 382.585], [41, 91.77799999999999, 185.23999999999998, 386.75, 401.625], [41, 91.77799999999999, 153.244, 405.195, 420.07], [41, 91.77799999999999, 149.034, 423.64, 438.515]]
2026-08-05 10:59:33,052 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=14, matched=14, pages=1, time=15.3s
2026-08-05 10:59:33,053 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 10:59:33,054 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[41]
2026-08-05 10:59:33,054 INFO     29 [qwen-vl-table] positions ： [[41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0], [41, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 10:59:33,298 INFO     29 [qwen-vl-table] page=41, rect=595x842, img=(1653x2339)
2026-08-05 10:59:33,299 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 10:59:33,299 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2112, \"bbox_end\": 2160, \"encounter_dates\": [\"2026-01-06\"], \"department\": \"妇科一病区(门)\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{lllll}\n报告时间: 2026-01-06\n\\hline\n\\multicolumn{2}{l}{\\textbf{瑞图RT-F600}} & \\multicolumn{3}{c}{\\textbf{医学检验科检验报告单}} \\\\\n\\multicolumn{2}{l}{\\textbf{白带分析仪}} & \\multicolumn{3}{c}{} \\\\\n\\multicolumn{2}{l}{\\textbf{姓 名:}} & \\multicolumn{2}{l}{\\textbf{送检科室: 妇科一病区(门)}} & \\multicolumn{1}{l}{\\textbf{床 号:}} \\\\\n\\multicolumn{2}{l}{\\textbf{住院(门诊)号:}} & \\multicolumn{2}{l}{\\textbf{性 别: 女}} & \\multicolumn{1}{l}{\\textbf{年 龄: 41岁}} \\\\\n\\multicolumn{2}{l}{\\textbf{检验项目: 妇科微生态}} & \\multicolumn{3}{l}{\\textbf{样本类型: 阴道分泌物}} \\\\\n\\multicolumn{2}{l}{\\textbf{疾病诊断: 慢性盆腔痛}} & \\multicolumn{3}{l}{\\textbf{样本状态: 正常}} \\\\\n\\hline\n\\multicolumn{5}{l}{\\textbf{形态学检测项目:}} \\\\\n\\multicolumn{2}{l}{细胞情况} & \\textbf{结果} & \\textbf{正常值范围} & \\textbf{镜下所见:} \\\\\n\\multicolumn{2}{l}{清洁度} & Ⅱ & $\\sim \\le$II & \\\\\n\\multicolumn{2}{l}{白细胞} & 5-15 & $\\le$15/HP & \\\\\n\\multicolumn{2}{l}{红细胞} & 未检出 & $\\sim$未检出 & \\\\\n\\multicolumn{2}{l}{线索细胞} & 未检出 & $\\sim$未检出 & \\\\\n\\multicolumn{2}{l}{上皮细胞} & 10-15 & $\\sim$满视野 & \\\\\n\\multicolumn{5}{l}{} \\\\\n\\multicolumn{2}{l}{病原体情况:} & & & \\\\\n\\multicolumn{2}{l}{滴虫} & 未检出 & $\\sim$未检出 & \\\\\n\\multicolumn{2}{l}{菌丝} & 未检出 & $\\sim$未检出 & \\\\\n\\multicolumn{2}{l}{孢子} & 未检出 & $\\sim$未检出 & \\\\\n\\multicolumn{2}{l}{芽生孢子} & 未检出 & $\\sim$未检出 & \\\\\n\\multicolumn{5}{l}{} \\\\\n\\multicolumn{2}{l}{菌群情况:} & & & \\\\\n\\multicolumn{2}{l}{菌群密集度} & ++ & $\\sim$++ & \\\\\n\\multicolumn{2}{l}{多样性} & + & $\\sim$++ & \\\\\n\\multicolumn{2}{l}{优势菌} & G+杆菌 & $\\sim$G阳性杆菌 & \\\\\n\\multicolumn{2}{l}{$\\beta$-N-乙酰氨基葡萄糖苷酶(NAG)} & - & $\\sim$- & \\\\\n\\multicolumn{5}{l}{} \\\\\n\\multicolumn{2}{l}{功能学分析:} & & & \\\\\n\\multicolumn{2}{l}{唾液酸苷酶} & - & $\\sim$- & \\\\\n\\multicolumn{2}{l}{白细胞酯酶} & - & $\\sim$- & \\\\\n\\multicolumn{2}{l}{胺试验} & - & $\\sim$- & \\\\\n\\multicolumn{2}{l}{脯氨酸氨基肽酶PIP} & - & $\\sim$- & \\\\\n\\multicolumn{2}{l}{过氧化氢(H2O2)} & + & $\\sim$- & \\\\\n\\multicolumn{2}{l}{pH值} & 3.8 & 3.8 $\\sim$ 4.5 & \\\\\n\\multicolumn{2}{l}{Nugent评分2} & \\multicolumn{2}{l}{AV评分1} & \\\\\n\\hline\n\\multicolumn{5}{l}{※ 备注:阴道微生态未见明显异常!} \\\\\n\\hline\n\\multicolumn{2}{l}{采集时间: 2026-01-06} & \\multicolumn{2}{l}{接收时间: 2026-01-06} & \\multicolumn{1}{l}{审核时间: 2026-01-06} \\\\\n\\multicolumn{2}{l}{09:15} & \\multicolumn{2}{l}{09:22} & \\multicolumn{1}{l}{10:59} \\\\\n\\multicolumn{2}{l}{送检医生: 权丽丽} & \\multicolumn{2}{l}{检验者: 伊原原} & \\multicolumn{1}{l}{审核者: 介倩倩} \\\\\n\\multicolumn{5}{l}{打印时间: 2026/2/26 下午 3:59:58} \\\\\n\\multicolumn{5}{l}{打印者: 网页打印} \\\\\n\\multicolumn{5}{l}{※本报告检查结果实行互认制度,如有疑问,请在三天内和我们联系,电} \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
[92m10:59:33 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 10:59:33,300 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 10:59:34,094 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T10:59:34.093+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 10:59:46,937 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 10:59:46,937 INFO     29 [qwen-vl-table] page=41 LLM output (len=3371):
{
  "report_date": "2026-01-06",
  "items": [
    {
      "name": "清洁度",
      "item_code": null,
      "value": "Ⅱ",
      "unit": null,
      "reference_range": "~≤II",
      "abnormal": false
    },
    {
      "name": "白细胞",
      "item_code": null,
      "value": "5-15",
      "unit": "/HP",
      "reference_range": "≤15/HP",
      "abnormal": false
    },
    {
      "name": "红细胞",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": "~未检出",
      "abnormal": false
    },
    {
      "name": "线索细胞",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": "~未检出",
      "abnormal": false
    },
    {
      "name": "上皮细胞",
      "item_code": null,
      "value": "10-15",
      "unit": null,
      "reference_range": "~满视野",
      "abnormal": false
    },
    {
      "name": "滴虫",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": "~未检出",
      "abnormal": false
    },
    {
      "name": "菌丝",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": "~未检出",
      "abnormal": false
    },
    {
      "name": "孢子",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": "~未检出",
      "abnormal": false
    },
    {
      "name": "芽生孢子",
      "item_code": null,
      "value": "未检出",
      "unit": null,
      "reference_range": "~未检出",
      "abnormal": false
    },
    {
      "name": "菌群密集度",
      "item_code": null,
      "value": "++",
      "unit": null,
      "reference_range": "~++",
      "abnormal": false
    },
    {
      "name": "多样性",
      "item_code": null,
      "value": "+",
      "unit": null,
      "reference_range": "~++",
      "abnormal": false
    },
    {
      "name": "优势菌",
      "item_code": null,
      "value": "G+杆菌",
      "unit": null,
      "reference_range": "~G阳性杆菌",
      "abnormal": false
    },
    {
      "name": "β-N-乙酰氨基葡萄糖苷酶",
      "item_code": "NAG",
      "value": "-",
      "unit": null,
      "reference_range": "~-",
      "abnormal": false
    },
    {
      "name": "唾液酸苷酶",
      "item_code": null,
      "value": "-",
      "unit": null,
      "reference_range": "~-",
      "abnormal": false
    },
    {
      "name": "白细胞酯酶",
      "item_code": null,
      "value": "-",
      "unit": null,
      "reference_range": "~-",
      "abnormal": false
    },
    {
      "name": "胺试验",
      "item_code": null,
      "value": "-",
      "unit": null,
      "reference_range": "~-",
      "abnormal": false
    },
    {
      "name": "脯氨酸氨基肽酶",
      "item_code": "PIP",
      "value": "-",
      "unit": null,
      "reference_range": "~-",
      "abnormal": false
    },
    {
      "name": "过氧化氢",
      "item_code": "H2O2",
      "value": "+",
      "unit": null,
      "reference_range": "~-",
      "abnormal": true
    },
    {
      "name": "pH值",
      "item_code": null,
      "value": "3.8",
      "unit": null,
      "reference_range": "3.8~4.5",
      "abnormal": false
    },
    {
      "name": "Nugent评分",
      "item_code": null,
      "value": "2",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "AV评分",
      "item_code": null,
      "value": "1",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-05 10:59:46,937 INFO     29 [qwen-vl-table] coord grouping: {41: 21}
2026-08-05 10:59:46,942 INFO     29 [qwen-vl-table] coord API call start, page=41, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1412308, prompt_len=617
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
清洁度、白细胞、红细胞、线索细胞、上皮细胞、滴虫、菌丝、孢子、芽生孢子、菌群密集度、多样性、优势菌、β-N-乙酰氨基葡萄糖苷酶、唾液酸苷酶、白细胞酯酶、胺试验、脯氨酸氨基肽酶、过氧化氢、pH值、Nugent评分、AV评分

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
2026-08-05 10:59:53,329 INFO     29 [qwen-vl-table] coord API raw response (len=1037):
[
	{"text": "清洁度", "bbox": [100, 232, 158, 248]},
	{"text": "白细胞", "bbox": [100, 252, 158, 268]},
	{"text": "红细胞", "bbox": [100, 271, 158, 287]},
	{"text": "线索细胞", "bbox": [100, 291, 177, 307]},
	{"text": "上皮细胞", "bbox": [100, 310, 177, 326]},
	{"text": "滴虫", "bbox": [100, 389, 139, 404]},
	{"text": "菌丝", "bbox": [100, 408, 139, 423]},
	{"text": "孢子", "bbox": [100, 427, 139, 443]},
	{"text": "芽生孢子", "bbox": [100, 446, 177, 462]},
	{"text": "菌群密集度", "bbox": [100, 523, 197, 538]},
	{"text": "多样性", "bbox": [100, 542, 158, 558]},
	{"text": "优势菌", "bbox": [100, 561, 158, 577]},
	{"text": "β-N-乙酰氨基葡萄糖苷酶", "bbox": [100, 580, 372, 597]},
	{"text": "唾液酸苷酶", "bbox": [100, 659, 197, 674]},
	{"text": "白细胞酯酶", "bbox": [100, 678, 197, 694]},
	{"text": "胺试验", "bbox": [100, 697, 158, 713]},
	{"text": "脯氨酸氨基肽酶", "bbox": [100, 716, 263, 732]},
	{"text": "过氧化氢", "bbox": [100, 735, 242, 751]},
	{"text": "pH值", "bbox": [100, 755, 148, 771]},
	{"text": "Nugent评分", "bbox": [100, 774, 219, 790]},
	{"text": "AV评分", "bbox": [396, 774, 471, 790]}
]
2026-08-05 10:59:53,329 INFO     29 [qwen-vl-table] coord API: raw_items=21, valid_items=21, elapsed=6.4s
2026-08-05 10:59:53,329 INFO     29 [qwen-vl-table] coord item[0]: text=清洁度, bbox=[100, 232, 158, 248]
2026-08-05 10:59:53,329 INFO     29 [qwen-vl-table] coord item[1]: text=白细胞, bbox=[100, 252, 158, 268]
2026-08-05 10:59:53,329 INFO     29 [qwen-vl-table] coord item[2]: text=红细胞, bbox=[100, 271, 158, 287]
2026-08-05 10:59:53,330 INFO     29 [qwen-vl-table] coord item[3]: text=线索细胞, bbox=[100, 291, 177, 307]
2026-08-05 10:59:53,330 INFO     29 [qwen-vl-table] coord item[4]: text=上皮细胞, bbox=[100, 310, 177, 326]
2026-08-05 10:59:53,330 INFO     29 [qwen-vl-table] coord item[5]: text=滴虫, bbox=[100, 389, 139, 404]
2026-08-05 10:59:53,330 INFO     29 [qwen-vl-table] coord item[6]: text=菌丝, bbox=[100, 408, 139, 423]
2026-08-05 10:59:53,330 INFO     29 [qwen-vl-table] coord item[7]: text=孢子, bbox=[100, 427, 139, 443]
2026-08-05 10:59:53,330 INFO     29 [qwen-vl-table] coord item[8]: text=芽生孢子, bbox=[100, 446, 177, 462]
2026-08-05 10:59:53,330 INFO     29 [qwen-vl-table] coord item[9]: text=菌群密集度, bbox=[100, 523, 197, 538]
2026-08-05 10:59:53,330 INFO     29 [qwen-vl-table] coord item[10]: text=多样性, bbox=[100, 542, 158, 558]
2026-08-05 10:59:53,330 INFO     29 [qwen-vl-table] coord item[11]: text=优势菌, bbox=[100, 561, 158, 577]
2026-08-05 10:59:53,330 INFO     29 [qwen-vl-table] coord item[12]: text=β-N-乙酰氨基葡萄糖苷酶, bbox=[100, 580, 372, 597]
2026-08-05 10:59:53,330 INFO     29 [qwen-vl-table] coord item[13]: text=唾液酸苷酶, bbox=[100, 659, 197, 674]
2026-08-05 10:59:53,330 INFO     29 [qwen-vl-table] coord item[14]: text=白细胞酯酶, bbox=[100, 678, 197, 694]
2026-08-05 10:59:53,330 INFO     29 [qwen-vl-table] coord item[15]: text=胺试验, bbox=[100, 697, 158, 713]
2026-08-05 10:59:53,330 INFO     29 [qwen-vl-table] coord item[16]: text=脯氨酸氨基肽酶, bbox=[100, 716, 263, 732]
2026-08-05 10:59:53,330 INFO     29 [qwen-vl-table] coord item[17]: text=过氧化氢, bbox=[100, 735, 242, 751]
2026-08-05 10:59:53,330 INFO     29 [qwen-vl-table] coord item[18]: text=pH值, bbox=[100, 755, 148, 771]
2026-08-05 10:59:53,330 INFO     29 [qwen-vl-table] coord item[19]: text=Nugent评分, bbox=[100, 774, 219, 790]
2026-08-05 10:59:53,330 INFO     29 [qwen-vl-table] coord item[20]: text=AV评分, bbox=[396, 774, 471, 790]
2026-08-05 10:59:53,330 INFO     29 [qwen-vl-table] page=41 coord: matched 21/21, time=6.4s
2026-08-05 10:59:53,330 INFO     29 [qwen-vl-table] new_positions (21):
[[42, 59.5, 94.00999999999999, 195.344, 208.816], [42, 59.5, 94.00999999999999, 212.184, 225.656], [42, 59.5, 94.00999999999999, 228.182, 241.654], [42, 59.5, 105.315, 245.022, 258.49399999999997], [42, 59.5, 105.315, 261.02, 274.492], [42, 59.5, 82.705, 327.538, 340.168], [42, 59.5, 82.705, 343.536, 356.166], [42, 59.5, 82.705, 359.534, 373.006], [42, 59.5, 105.315, 375.532, 389.00399999999996], [42, 59.5, 117.21499999999999, 440.366, 452.996], [42, 59.5, 94.00999999999999, 456.364, 469.83599999999996], [42, 59.5, 94.00999999999999, 472.36199999999997, 485.834], [42, 59.5, 221.34, 488.35999999999996, 502.674], [42, 59.5, 117.21499999999999, 554.8779999999999, 567.5079999999999], [42, 59.5, 117.21499999999999, 570.876, 584.348], [42, 59.5, 94.00999999999999, 586.874, 600.346], [42, 59.5, 156.48499999999999, 602.872, 616.3439999999999], [42, 59.5, 143.98999999999998, 618.87, 632.342], [42, 59.5, 88.06, 635.7099999999999, 649.182], [42, 59.5, 130.305, 651.708, 665.18], [42, 235.61999999999998, 280.245, 651.708, 665.18]]
2026-08-05 10:59:53,330 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=21, matched=21, pages=1, time=20.3s
2026-08-05 10:59:53,332 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 10:59:53,332 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[42]
2026-08-05 10:59:53,332 INFO     29 [qwen-vl-table] positions ： [[42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 10:59:53,521 INFO     29 [qwen-vl-table] page=42, rect=842x595, img=(2339x1653)
2026-08-05 10:59:53,521 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 10:59:53,521 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2161, \"bbox_end\": 2169, \"encounter_dates\": [\"2026-01-06\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{cccccc}\n报告时间: 2026-01-06\n\\hline\n英文 & 项目名称 & 结果 & 参考范围 & 单位 & \\\\\n\\hline\n\\multicolumn{2}{l}{[\\beta-HCG]人绒毛膜促性腺激素} & 0.40 & \\begin{tabular}[c]{@{}c@{}}非孕期 0~2.9 \\\\ 0.2-1周 5~50 \\\\ 1-2周 50~500 \\\\ 2-3周 100~5000 \\\\ 3-4周 500~10000 \\\\ 4-5周 1000~50000 \\\\ 5-6周 10000~100000 \\\\ 6-8周 15000~200000\\end{tabular} & \\multicolumn{2}{c}{mIU/ml} \\\\\n报告时间: 2026-01-06\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
[92m10:59:53 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 10:59:53,523 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 10:59:56,987 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 10:59:56,988 INFO     29 [qwen-vl-table] page=42 LLM output (len=339):
{
  "report_date": "2026-01-06",
  "items": [
    {
      "name": "人绒毛膜促性腺激素",
      "item_code": "β-HCG",
      "value": "0.40",
      "unit": "mIU/ml",
      "reference_range": "非孕期 0~2.9; 0.2-1周 5~50; 1-2周 50~500; 2-3周 100~5000; 3-4周 500~10000; 4-5周 1000~50000; 5-6周 10000~100000; 6-8周 15000~200000",
      "abnormal": false
    }
  ]
}
2026-08-05 10:59:56,988 INFO     29 [qwen-vl-table] coord grouping: {42: 1}
2026-08-05 10:59:56,990 INFO     29 [qwen-vl-table] coord API call start, page=42, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=898079, prompt_len=516
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
人绒毛膜促性腺激素

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
2026-08-05 10:59:58,536 INFO     29 [qwen-vl-table] coord API raw response (len=68):
```json
[
	{"text": "人绒毛膜促性腺激素", "bbox": [192, 223, 414, 250]}
]
```
2026-08-05 10:59:58,536 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=1.5s
2026-08-05 10:59:58,536 INFO     29 [qwen-vl-table] coord item[0]: text=人绒毛膜促性腺激素, bbox=[192, 223, 414, 250]
2026-08-05 10:59:58,537 INFO     29 [qwen-vl-table] page=42 coord: matched 1/1, time=1.5s
2026-08-05 10:59:58,537 INFO     29 [qwen-vl-table] new_positions (1):
[[43, 161.664, 348.58799999999997, 132.685, 148.75]]
2026-08-05 10:59:58,537 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=5.2s
2026-08-05 10:59:58,539 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 10:59:58,539 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[42]
2026-08-05 10:59:58,539 INFO     29 [qwen-vl-table] positions ： [[42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 10:59:58,723 INFO     29 [qwen-vl-table] page=42, rect=842x595, img=(2339x1653)
2026-08-05 10:59:58,723 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 10:59:58,724 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2170, \"bbox_end\": 2177, \"encounter_dates\": [\"2026-01-06\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllll}\n报告时间: 2026-01-06\n\\hline\n采集时间: & 2026-01-06 & 接收时间: & 2026-01-06 & 审核时间: & 2026-01-06 \\\\\n& 09:15 & & 10:03 & & 11:06 \\\\\n送检医生: & 权丽丽 & 检验者: & 秦淑云 & 审核者: & 薛轩 \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
[92m10:59:58 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 10:59:58,725 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 10:59:59,706 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 10:59:59,706 INFO     29 [qwen-vl-table] page=42 LLM output (len=48):
{
  "report_date": "2026-01-06",
  "items": []
}
2026-08-05 10:59:59,706 WARNING  29 [qwen-vl-table] page=42 no items extracted
2026-08-05 10:59:59,706 INFO     29 [qwen-vl-table] coord grouping: {}
2026-08-05 10:59:59,706 INFO     29 [qwen-vl-table] new_positions (0):
[]
2026-08-05 10:59:59,706 WARNING  29 [qwen-vl-table] No items extracted from any page
2026-08-05 10:59:59,707 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 10:59:59,708 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[42]
2026-08-05 10:59:59,708 INFO     29 [qwen-vl-table] positions ： [[42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0], [42, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 10:59:59,894 INFO     29 [qwen-vl-table] page=42, rect=842x595, img=(2339x1653)
2026-08-05 10:59:59,894 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 10:59:59,895 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2178, \"bbox_end\": 2186, \"encounter_dates\": [\"2026-01-06\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllll}\n报告时间: 2026-01-06\n\\hline\n\\multicolumn{6}{l}{\\textbf{※本报告检查结果实行互认制度，如有疑问，请在三天内和我们联系，电话：}} \\\\\n\\multicolumn{6}{l}{\\textbf{打印时间: 2026/2/26 下午 4:00:10}} \\\\\n\\multicolumn{6}{l}{\\textbf{打印者: 网页打印}} \\\\\n\\multicolumn{6}{l}{\\textbf{※}} \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
[92m10:59:59 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 10:59:59,896 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:00:00,586 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:00:00,586 INFO     29 [qwen-vl-table] page=42 LLM output (len=48):
{
  "report_date": "2026-01-06",
  "items": []
}
2026-08-05 11:00:00,586 WARNING  29 [qwen-vl-table] page=42 no items extracted
2026-08-05 11:00:00,586 INFO     29 [qwen-vl-table] coord grouping: {}
2026-08-05 11:00:00,586 INFO     29 [qwen-vl-table] new_positions (0):
[]
2026-08-05 11:00:00,586 WARNING  29 [qwen-vl-table] No items extracted from any page
2026-08-05 11:00:00,587 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 11:00:00,588 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[43]
2026-08-05 11:00:00,588 INFO     29 [qwen-vl-table] positions ： [[43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0], [43, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 11:00:00,762 INFO     29 [qwen-vl-table] page=43, rect=842x595, img=(2339x1653)
2026-08-05 11:00:00,763 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 11:00:00,763 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2187, \"bbox_end\": 2194, \"encounter_dates\": [\"2026-01-06\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccc}\n报告时间: 2026-01-06\n\\hline\n英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n\\hline\n[OV125Ag]CA-125 & & 59.70 & $\\uparrow$ & 0.00~35.00 & U/ml \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
[92m11:00:00 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:00:00,765 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:00:02,309 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:00:02,309 INFO     29 [qwen-vl-table] page=43 LLM output (len=225):
{
  "report_date": "2026-01-06",
  "items": [
    {
      "name": "CA-125",
      "item_code": "OV125Ag",
      "value": "59.70",
      "unit": "U/ml",
      "reference_range": "0.00~35.00",
      "abnormal": true
    }
  ]
}
2026-08-05 11:00:02,310 INFO     29 [qwen-vl-table] coord grouping: {43: 1}
2026-08-05 11:00:02,312 INFO     29 [qwen-vl-table] coord API call start, page=43, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=758998, prompt_len=513
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
CA-125

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
2026-08-05 11:00:03,822 INFO     29 [qwen-vl-table] coord API raw response (len=65):
```json
[
	{"text": "CA-125", "bbox": [188, 211, 241, 233]}
]
```
2026-08-05 11:00:03,822 INFO     29 [qwen-vl-table] coord API: raw_items=1, valid_items=1, elapsed=1.5s
2026-08-05 11:00:03,825 INFO     29 [qwen-vl-table] coord item[0]: text=CA-125, bbox=[188, 211, 241, 233]
2026-08-05 11:00:03,825 INFO     29 [qwen-vl-table] page=43 coord: matched 1/1, time=1.5s
2026-08-05 11:00:03,825 INFO     29 [qwen-vl-table] new_positions (1):
[[44, 158.296, 202.922, 125.54499999999999, 138.635]]
2026-08-05 11:00:03,825 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=1, matched=1, pages=1, time=3.2s
2026-08-05 11:00:03,826 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 11:00:03,827 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[44]
2026-08-05 11:00:03,827 INFO     29 [qwen-vl-table] positions ： [[44, 0.0, 0.0, 0.0, 0.0], [44, 0.0, 0.0, 0.0, 0.0], [44, 0.0, 0.0, 0.0, 0.0], [44, 0.0, 0.0, 0.0, 0.0], [44, 0.0, 0.0, 0.0, 0.0], [44, 0.0, 0.0, 0.0, 0.0], [44, 0.0, 0.0, 0.0, 0.0], [44, 0.0, 0.0, 0.0, 0.0], [44, 0.0, 0.0, 0.0, 0.0], [44, 0.0, 0.0, 0.0, 0.0], [44, 0.0, 0.0, 0.0, 0.0], [44, 0.0, 0.0, 0.0, 0.0], [44, 0.0, 0.0, 0.0, 0.0], [44, 0.0, 0.0, 0.0, 0.0], [44, 0.0, 0.0, 0.0, 0.0], [44, 0.0, 0.0, 0.0, 0.0], [44, 0.0, 0.0, 0.0, 0.0], [44, 0.0, 0.0, 0.0, 0.0], [44, 0.0, 0.0, 0.0, 0.0], [44, 0.0, 0.0, 0.0, 0.0], [44, 0.0, 0.0, 0.0, 0.0], [44, 0.0, 0.0, 0.0, 0.0], [44, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 11:00:04,040 INFO     29 [qwen-vl-table] page=44, rect=842x595, img=(2339x1653)
2026-08-05 11:00:04,041 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 11:00:04,041 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2195, \"bbox_end\": 2217, \"encounter_dates\": [\"2026-01-06\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2026-01-06\n\\hline\n英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n\\hline\n[颜色]颜色 & & 黄色 & & 清 & & [尿酸结晶]尿酸结晶 & & 0 & & 0~15 & 个/ul \\\\\n[浊度]浊度 & & 清亮 & & 清 & & [草酸钙结晶]草酸钙结晶 & & 0 & & 0~30 & 个/ul \\\\\n[GLU]葡萄糖 & & - & & 阴性 & & [上皮细胞]上皮细胞 & & 14 & & 0~20 & 个/ul \\\\\n[BLD]潜血 & & - & & 阴性 & & [粘液丝]粘液丝 & & 5 & & 0~20 & 个/ul \\\\\n[LEU]白细胞 & & 2+ & & 阴性 & & [酵母菌]酵母菌 & & 6 & $\\uparrow$ & 0~0 & 个/ul \\\\\n[PRO]蛋白质 & & - & & 阴性 & & [透明管型]透明管型 & & 0 & & 0~1 & 个/ul \\\\\n[NIT]亚硝酸盐 & & + & & 阴性 & & [颗粒管型]颗粒管型 & & 0 & & 0~0 & 个/ul \\\\\n[URO]尿胆素原 & & - & & 阴性 & & [小圆上皮]小圆上皮 & & 0 & & 0~3 & 个/ul \\\\\n[BIL]胆红素 & & - & & 阴性 & & [其他管型]其他管型 & & 0 & & 0~0 & 个/ul \\\\\n[KET]酮体 & & - & & 阴性 & & [其他上皮]其他上皮 & & 0 & & 0~10 & 个/ul \\\\\n[Vc]维生素C & & - & & - & & [异常红细胞]异常红细胞 & & 0 & & 0~5 & 个/ul \\\\\n[pH]酸碱性 & & 6.0 & & 5.0~8.5 & & [细菌]细菌 & & 1072 & $\\uparrow$ & 0~50 & 个/ul \\\\\n[SG]比重 & & 1.020 & & 1.010~ & & [尿沉渣镜检]尿沉渣镜检 & & : & & & \\\\\n& & & & 1.025 & & [白细胞]白细胞 & & +++/HP & & $\\le$5/HP & \\\\\n[红细胞]红细胞 & & 0 & & 0~5 & 个/ul & [红细胞]红细胞 & & 未查见 & & $\\le$3/HP & \\\\\n[白细胞]白细胞 & & 218 & $\\uparrow$ & 0~7 & 个/ul & & & & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
[92m11:00:04 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:00:04,042 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:00:04,251 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T11:00:04.250+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 11:00:24,041 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:00:24,041 INFO     29 [qwen-vl-table] page=44 LLM output (len=4771):
{
  "report_date": "2026-01-06",
  "items": [
    {
      "name": "颜色",
      "item_code": null,
      "value": "黄色",
      "unit": null,
      "reference_range": "清",
      "abnormal": false
    },
    {
      "name": "浊度",
      "item_code": null,
      "value": "清亮",
      "unit": null,
      "reference_range": "清",
      "abnormal": false
    },
    {
      "name": "葡萄糖",
      "item_code": "GLU",
      "value": "-",
      "unit": null,
      "reference_range": "阴性",
      "abnormal": false
    },
    {
      "name": "潜血",
      "item_code": "BLD",
      "value": "-",
      "unit": null,
      "reference_range": "阴性",
      "abnormal": false
    },
    {
      "name": "白细胞",
      "item_code": "LEU",
      "value": "2+",
      "unit": null,
      "reference_range": "阴性",
      "abnormal": true
    },
    {
      "name": "蛋白质",
      "item_code": "PRO",
      "value": "-",
      "unit": null,
      "reference_range": "阴性",
      "abnormal": false
    },
    {
      "name": "亚硝酸盐",
      "item_code": "NIT",
      "value": "+",
      "unit": null,
      "reference_range": "阴性",
      "abnormal": true
    },
    {
      "name": "尿胆素原",
      "item_code": "URO",
      "value": "-",
      "unit": null,
      "reference_range": "阴性",
      "abnormal": false
    },
    {
      "name": "胆红素",
      "item_code": "BIL",
      "value": "-",
      "unit": null,
      "reference_range": "阴性",
      "abnormal": false
    },
    {
      "name": "酮体",
      "item_code": "KET",
      "value": "-",
      "unit": null,
      "reference_range": "阴性",
      "abnormal": false
    },
    {
      "name": "维生素C",
      "item_code": "Vc",
      "value": "-",
      "unit": null,
      "reference_range": "-",
      "abnormal": false
    },
    {
      "name": "酸碱性",
      "item_code": "pH",
      "value": "6.0",
      "unit": null,
      "reference_range": "5.0~8.5",
      "abnormal": false
    },
    {
      "name": "比重",
      "item_code": "SG",
      "value": "1.020",
      "unit": null,
      "reference_range": "1.010~1.025",
      "abnormal": false
    },
    {
      "name": "红细胞",
      "item_code": null,
      "value": "0",
      "unit": "个/ul",
      "reference_range": "0~5",
      "abnormal": false
    },
    {
      "name": "白细胞",
      "item_code": null,
      "value": "218",
      "unit": "个/ul",
      "reference_range": "0~7",
      "abnormal": true
    },
    {
      "name": "尿酸结晶",
      "item_code": null,
      "value": "0",
      "unit": "个/ul",
      "reference_range": "0~15",
      "abnormal": false
    },
    {
      "name": "草酸钙结晶",
      "item_code": null,
      "value": "0",
      "unit": "个/ul",
      "reference_range": "0~30",
      "abnormal": false
    },
    {
      "name": "上皮细胞",
      "item_code": null,
      "value": "14",
      "unit": "个/ul",
      "reference_range": "0~20",
      "abnormal": false
    },
    {
      "name": "粘液丝",
      "item_code": null,
      "value": "5",
      "unit": "个/ul",
      "reference_range": "0~20",
      "abnormal": false
    },
    {
      "name": "酵母菌",
      "item_code": null,
      "value": "6",
      "unit": "个/ul",
      "reference_range": "0~0",
      "abnormal": true
    },
    {
      "name": "透明管型",
      "item_code": null,
      "value": "0",
      "unit": "个/ul",
      "reference_range": "0~1",
      "abnormal": false
    },
    {
      "name": "颗粒管型",
      "item_code": null,
      "value": "0",
      "unit": "个/ul",
      "reference_range": "0~0",
      "abnormal": false
    },
    {
      "name": "小圆上皮",
      "item_code": null,
      "value": "0",
      "unit": "个/ul",
      "reference_range": "0~3",
      "abnormal": false
    },
    {
      "name": "其他管型",
      "item_code": null,
      "value": "0",
      "unit": "个/ul",
      "reference_range": "0~0",
      "abnormal": false
    },
    {
      "name": "其他上皮",
      "item_code": null,
      "value": "0",
      "unit": "个/ul",
      "reference_range": "0~10",
      "abnormal": false
    },
    {
      "name": "异常红细胞",
      "item_code": null,
      "value": "0",
      "unit": "个/ul",
      "reference_range": "0~5",
      "abnormal": false
    },
    {
      "name": "细菌",
      "item_code": null,
      "value": "1072",
      "unit": "个/ul",
      "reference_range": "0~50",
      "abnormal": true
    },
    {
      "name": "尿沉渣镜检",
      "item_code": null,
      "value": ":",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "白细胞",
      "item_code": null,
      "value": "+++/HP",
      "unit": "/HP",
      "reference_range": "≤5/HP",
      "abnormal": true
    },
    {
      "name": "红细胞",
      "item_code": null,
      "value": "未查见",
      "unit": "/HP",
      "reference_range": "≤3/HP",
      "abnormal": false
    }
  ]
}
2026-08-05 11:00:24,041 INFO     29 [qwen-vl-table] coord grouping: {44: 30}
2026-08-05 11:00:24,044 INFO     29 [qwen-vl-table] coord API call start, page=44, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1378835, prompt_len=636
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
颜色、浊度、葡萄糖、潜血、白细胞、蛋白质、亚硝酸盐、尿胆素原、胆红素、酮体、维生素C、酸碱性、比重、红细胞、白细胞、尿酸结晶、草酸钙结晶、上皮细胞、粘液丝、酵母菌、透明管型、颗粒管型、小圆上皮、其他管型、其他上皮、异常红细胞、细菌、尿沉渣镜检、白细胞、红细胞

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
2026-08-05 11:00:32,315 INFO     29 [qwen-vl-table] coord API raw response (len=1452):
[
	{"text": "颜色", "bbox": [127, 293, 193, 315]},
	{"text": "浊度", "bbox": [127, 323, 193, 345]},
	{"text": "葡萄糖", "bbox": [127, 353, 207, 375]},
	{"text": "潜血", "bbox": [127, 382, 191, 404]},
	{"text": "白细胞", "bbox": [127, 411, 204, 433]},
	{"text": "蛋白质", "bbox": [127, 441, 208, 463]},
	{"text": "亚硝酸盐", "bbox": [127, 470, 217, 492]},
	{"text": "尿胆素原", "bbox": [127, 500, 225, 522]},
	{"text": "胆红素", "bbox": [127, 529, 199, 551]},
	{"text": "酮体", "bbox": [127, 558, 190, 580]},
	{"text": "维生素C", "bbox": [127, 588, 205, 610]},
	{"text": "酸碱性", "bbox": [127, 617, 199, 639]},
	{"text": "比重", "bbox": [127, 659, 184, 681]},
	{"text": "红细胞", "bbox": [127, 701, 222, 723]},
	{"text": "白细胞", "bbox": [127, 730, 222, 752]},
	{"text": "尿酸结晶", "bbox": [502, 293, 624, 315]},
	{"text": "草酸钙结晶", "bbox": [502, 323, 652, 345]},
	{"text": "上皮细胞", "bbox": [502, 353, 624, 375]},
	{"text": "粘液丝", "bbox": [502, 382, 596, 404]},
	{"text": "酵母菌", "bbox": [502, 411, 596, 433]},
	{"text": "透明管型", "bbox": [502, 441, 624, 463]},
	{"text": "颗粒管型", "bbox": [502, 470, 624, 492]},
	{"text": "小圆上皮", "bbox": [502, 500, 624, 522]},
	{"text": "其他管型", "bbox": [502, 529, 624, 551]},
	{"text": "其他上皮", "bbox": [502, 558, 624, 580]},
	{"text": "异常红细胞", "bbox": [502, 588, 652, 610]},
	{"text": "细菌", "bbox": [502, 617, 567, 639]},
	{"text": "尿沉渣镜检", "bbox": [502, 647, 652, 669]},
	{"text": "白细胞", "bbox": [502, 677, 596, 699]},
	{"text": "红细胞", "bbox": [502, 706, 596, 728]}
]
2026-08-05 11:00:32,316 INFO     29 [qwen-vl-table] coord API: raw_items=30, valid_items=30, elapsed=8.3s
2026-08-05 11:00:32,316 INFO     29 [qwen-vl-table] coord item[0]: text=颜色, bbox=[127, 293, 193, 315]
2026-08-05 11:00:32,316 INFO     29 [qwen-vl-table] coord item[1]: text=浊度, bbox=[127, 323, 193, 345]
2026-08-05 11:00:32,316 INFO     29 [qwen-vl-table] coord item[2]: text=葡萄糖, bbox=[127, 353, 207, 375]
2026-08-05 11:00:32,316 INFO     29 [qwen-vl-table] coord item[3]: text=潜血, bbox=[127, 382, 191, 404]
2026-08-05 11:00:32,316 INFO     29 [qwen-vl-table] coord item[4]: text=白细胞, bbox=[127, 411, 204, 433]
2026-08-05 11:00:32,316 INFO     29 [qwen-vl-table] coord item[5]: text=蛋白质, bbox=[127, 441, 208, 463]
2026-08-05 11:00:32,316 INFO     29 [qwen-vl-table] coord item[6]: text=亚硝酸盐, bbox=[127, 470, 217, 492]
2026-08-05 11:00:32,316 INFO     29 [qwen-vl-table] coord item[7]: text=尿胆素原, bbox=[127, 500, 225, 522]
2026-08-05 11:00:32,316 INFO     29 [qwen-vl-table] coord item[8]: text=胆红素, bbox=[127, 529, 199, 551]
2026-08-05 11:00:32,316 INFO     29 [qwen-vl-table] coord item[9]: text=酮体, bbox=[127, 558, 190, 580]
2026-08-05 11:00:32,316 INFO     29 [qwen-vl-table] coord item[10]: text=维生素C, bbox=[127, 588, 205, 610]
2026-08-05 11:00:32,316 INFO     29 [qwen-vl-table] coord item[11]: text=酸碱性, bbox=[127, 617, 199, 639]
2026-08-05 11:00:32,316 INFO     29 [qwen-vl-table] coord item[12]: text=比重, bbox=[127, 659, 184, 681]
2026-08-05 11:00:32,316 INFO     29 [qwen-vl-table] coord item[13]: text=红细胞, bbox=[127, 701, 222, 723]
2026-08-05 11:00:32,316 INFO     29 [qwen-vl-table] coord item[14]: text=白细胞, bbox=[127, 730, 222, 752]
2026-08-05 11:00:32,316 INFO     29 [qwen-vl-table] coord item[15]: text=尿酸结晶, bbox=[502, 293, 624, 315]
2026-08-05 11:00:32,316 INFO     29 [qwen-vl-table] coord item[16]: text=草酸钙结晶, bbox=[502, 323, 652, 345]
2026-08-05 11:00:32,316 INFO     29 [qwen-vl-table] coord item[17]: text=上皮细胞, bbox=[502, 353, 624, 375]
2026-08-05 11:00:32,316 INFO     29 [qwen-vl-table] coord item[18]: text=粘液丝, bbox=[502, 382, 596, 404]
2026-08-05 11:00:32,316 INFO     29 [qwen-vl-table] coord item[19]: text=酵母菌, bbox=[502, 411, 596, 433]
2026-08-05 11:00:32,316 INFO     29 [qwen-vl-table] coord item[20]: text=透明管型, bbox=[502, 441, 624, 463]
2026-08-05 11:00:32,316 INFO     29 [qwen-vl-table] coord item[21]: text=颗粒管型, bbox=[502, 470, 624, 492]
2026-08-05 11:00:32,316 INFO     29 [qwen-vl-table] coord item[22]: text=小圆上皮, bbox=[502, 500, 624, 522]
2026-08-05 11:00:32,316 INFO     29 [qwen-vl-table] coord item[23]: text=其他管型, bbox=[502, 529, 624, 551]
2026-08-05 11:00:32,317 INFO     29 [qwen-vl-table] coord item[24]: text=其他上皮, bbox=[502, 558, 624, 580]
2026-08-05 11:00:32,317 INFO     29 [qwen-vl-table] coord item[25]: text=异常红细胞, bbox=[502, 588, 652, 610]
2026-08-05 11:00:32,317 INFO     29 [qwen-vl-table] coord item[26]: text=细菌, bbox=[502, 617, 567, 639]
2026-08-05 11:00:32,317 INFO     29 [qwen-vl-table] coord item[27]: text=尿沉渣镜检, bbox=[502, 647, 652, 669]
2026-08-05 11:00:32,317 INFO     29 [qwen-vl-table] coord item[28]: text=白细胞, bbox=[502, 677, 596, 699]
2026-08-05 11:00:32,317 INFO     29 [qwen-vl-table] coord item[29]: text=红细胞, bbox=[502, 706, 596, 728]
2026-08-05 11:00:32,317 INFO     29 [qwen-vl-table] page=44 coord: matched 30/30, time=8.3s
2026-08-05 11:00:32,317 INFO     29 [qwen-vl-table] new_positions (30):
[[45, 106.934, 162.506, 174.33499999999998, 187.42499999999998], [45, 106.934, 162.506, 192.185, 205.27499999999998], [45, 106.934, 174.29399999999998, 210.035, 223.125], [45, 106.934, 160.822, 227.29, 240.38], [45, 422.68399999999997, 501.832, 402.815, 415.905], [45, 106.934, 175.136, 262.395, 275.485], [45, 106.934, 182.714, 279.65, 292.74], [45, 106.934, 189.45, 297.5, 310.59], [45, 106.934, 167.558, 314.755, 327.84499999999997], [45, 106.934, 159.98, 332.01, 345.09999999999997], [45, 106.934, 172.60999999999999, 349.85999999999996, 362.95], [45, 106.934, 167.558, 367.115, 380.205], [45, 106.934, 154.928, 392.10499999999996, 405.195], [45, 422.68399999999997, 501.832, 420.07, 433.15999999999997], [45, 422.68399999999997, 501.832, 402.815, 415.905], [45, 422.68399999999997, 525.408, 174.33499999999998, 187.42499999999998], [45, 422.68399999999997, 548.984, 192.185, 205.27499999999998], [45, 422.68399999999997, 525.408, 210.035, 223.125], [45, 422.68399999999997, 501.832, 227.29, 240.38], [45, 422.68399999999997, 501.832, 244.545, 257.635], [45, 422.68399999999997, 525.408, 262.395, 275.485], [45, 422.68399999999997, 525.408, 279.65, 292.74], [45, 422.68399999999997, 525.408, 297.5, 310.59], [45, 422.68399999999997, 525.408, 314.755, 327.84499999999997], [45, 422.68399999999997, 525.408, 332.01, 345.09999999999997], [45, 422.68399999999997, 548.984, 349.85999999999996, 362.95], [45, 422.68399999999997, 477.414, 367.115, 380.205], [45, 422.68399999999997, 548.984, 384.965, 398.055], [45, 422.68399999999997, 501.832, 402.815, 415.905], [45, 422.68399999999997, 501.832, 420.07, 433.15999999999997]]
2026-08-05 11:00:32,317 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=30, matched=30, pages=1, time=28.5s
2026-08-05 11:00:32,319 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 11:00:32,319 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[45]
2026-08-05 11:00:32,319 INFO     29 [qwen-vl-table] positions ： [[45, 0.0, 0.0, 0.0, 0.0], [45, 0.0, 0.0, 0.0, 0.0], [45, 0.0, 0.0, 0.0, 0.0], [45, 0.0, 0.0, 0.0, 0.0], [45, 0.0, 0.0, 0.0, 0.0], [45, 0.0, 0.0, 0.0, 0.0], [45, 0.0, 0.0, 0.0, 0.0], [45, 0.0, 0.0, 0.0, 0.0], [45, 0.0, 0.0, 0.0, 0.0], [45, 0.0, 0.0, 0.0, 0.0], [45, 0.0, 0.0, 0.0, 0.0], [45, 0.0, 0.0, 0.0, 0.0], [45, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 11:00:32,503 INFO     29 [qwen-vl-table] page=45, rect=842x595, img=(2339x1653)
2026-08-05 11:00:32,504 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 11:00:32,504 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2218, \"bbox_end\": 2230, \"encounter_dates\": [\"2026-01-15\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccl}\n报告时间: 2026-01-15\n\\hline\n英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n\\hline\n{[}PT{]}凝血酶原时间 & & 11.0 & & 9.4~12.5 & s \\\\\n{[}INR{]}国际标准化比例 & & 0.98 & & 0.8~1.2 & INR \\\\\n{[}HDD{]}凝血酶原活动度 & & 103.00 & & 70~130 & \\% \\\\\n{[}APTT{]}部分凝血活酶时间(胶质硅) & & 33.7 & & 25.1~36.5 & s \\\\\n{[}Fib{]}纤维蛋白原 & & 2.65 & & 2.00~4.00 & g/L \\\\\n{[}TT{]}凝血酶时间 & & 15.1 & & 10.3~16.6 & s \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
[92m11:00:32 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:00:32,505 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:00:34,277 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T11:00:34.276+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 11:00:38,404 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:00:38,404 INFO     29 [qwen-vl-table] page=45 LLM output (len=1058):
{
  "report_date": "2026-01-15",
  "items": [
    {
      "name": "凝血酶原时间",
      "item_code": "PT",
      "value": "11.0",
      "unit": "s",
      "reference_range": "9.4~12.5",
      "abnormal": false
    },
    {
      "name": "国际标准化比例",
      "item_code": "INR",
      "value": "0.98",
      "unit": "INR",
      "reference_range": "0.8~1.2",
      "abnormal": false
    },
    {
      "name": "凝血酶原活动度",
      "item_code": "HDD",
      "value": "103.00",
      "unit": "%",
      "reference_range": "70~130",
      "abnormal": false
    },
    {
      "name": "部分凝血活酶时间(胶质硅)",
      "item_code": "APTT",
      "value": "33.7",
      "unit": "s",
      "reference_range": "25.1~36.5",
      "abnormal": false
    },
    {
      "name": "纤维蛋白原",
      "item_code": "Fib",
      "value": "2.65",
      "unit": "g/L",
      "reference_range": "2.00~4.00",
      "abnormal": false
    },
    {
      "name": "凝血酶时间",
      "item_code": "TT",
      "value": "15.1",
      "unit": "s",
      "reference_range": "10.3~16.6",
      "abnormal": false
    }
  ]
}
2026-08-05 11:00:38,404 INFO     29 [qwen-vl-table] coord grouping: {45: 6}
2026-08-05 11:00:38,407 INFO     29 [qwen-vl-table] coord API call start, page=45, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=866049, prompt_len=555
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
凝血酶原时间、国际标准化比例、凝血酶原活动度、部分凝血活酶时间(胶质硅)、纤维蛋白原、凝血酶时间

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
2026-08-05 11:00:41,118 INFO     29 [qwen-vl-table] coord API raw response (len=309):
[
	{"text": "凝血酶原时间", "bbox": [93, 315, 216, 340]},
	{"text": "国际标准化比例", "bbox": [93, 348, 241, 373]},
	{"text": "凝血酶原活动度", "bbox": [93, 380, 250, 405]},
	{"text": "部分凝血活酶时间(胶质硅)", "bbox": [93, 412, 326, 437]},
	{"text": "纤维蛋白原", "bbox": [93, 445, 204, 470]},
	{"text": "凝血酶时间", "bbox": [93, 477, 200, 502]}
]
2026-08-05 11:00:41,119 INFO     29 [qwen-vl-table] coord API: raw_items=6, valid_items=6, elapsed=2.7s
2026-08-05 11:00:41,119 INFO     29 [qwen-vl-table] coord item[0]: text=凝血酶原时间, bbox=[93, 315, 216, 340]
2026-08-05 11:00:41,119 INFO     29 [qwen-vl-table] coord item[1]: text=国际标准化比例, bbox=[93, 348, 241, 373]
2026-08-05 11:00:41,119 INFO     29 [qwen-vl-table] coord item[2]: text=凝血酶原活动度, bbox=[93, 380, 250, 405]
2026-08-05 11:00:41,119 INFO     29 [qwen-vl-table] coord item[3]: text=部分凝血活酶时间(胶质硅), bbox=[93, 412, 326, 437]
2026-08-05 11:00:41,119 INFO     29 [qwen-vl-table] coord item[4]: text=纤维蛋白原, bbox=[93, 445, 204, 470]
2026-08-05 11:00:41,119 INFO     29 [qwen-vl-table] coord item[5]: text=凝血酶时间, bbox=[93, 477, 200, 502]
2026-08-05 11:00:41,119 INFO     29 [qwen-vl-table] page=45 coord: matched 6/6, time=2.7s
2026-08-05 11:00:41,119 INFO     29 [qwen-vl-table] new_positions (6):
[[46, 78.306, 181.87199999999999, 187.42499999999998, 202.29999999999998], [46, 78.306, 202.922, 207.06, 221.935], [46, 78.306, 210.5, 226.1, 240.975], [46, 78.306, 274.492, 245.14, 260.015], [46, 78.306, 171.768, 264.775, 279.65], [46, 78.306, 168.4, 283.815, 298.69]]
2026-08-05 11:00:41,120 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=6, matched=6, pages=1, time=8.8s
2026-08-05 11:00:41,122 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 11:00:41,122 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[46]
2026-08-05 11:00:41,122 INFO     29 [qwen-vl-table] positions ： [[46, 0.0, 0.0, 0.0, 0.0], [46, 0.0, 0.0, 0.0, 0.0], [46, 0.0, 0.0, 0.0, 0.0], [46, 0.0, 0.0, 0.0, 0.0], [46, 0.0, 0.0, 0.0, 0.0], [46, 0.0, 0.0, 0.0, 0.0], [46, 0.0, 0.0, 0.0, 0.0], [46, 0.0, 0.0, 0.0, 0.0], [46, 0.0, 0.0, 0.0, 0.0], [46, 0.0, 0.0, 0.0, 0.0], [46, 0.0, 0.0, 0.0, 0.0], [46, 0.0, 0.0, 0.0, 0.0], [46, 0.0, 0.0, 0.0, 0.0], [46, 0.0, 0.0, 0.0, 0.0], [46, 0.0, 0.0, 0.0, 0.0], [46, 0.0, 0.0, 0.0, 0.0], [46, 0.0, 0.0, 0.0, 0.0], [46, 0.0, 0.0, 0.0, 0.0], [46, 0.0, 0.0, 0.0, 0.0], [46, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 11:00:41,340 INFO     29 [qwen-vl-table] page=46, rect=842x595, img=(2339x1653)
2026-08-05 11:00:41,341 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 11:00:41,341 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2231, \"bbox_end\": 2250, \"encounter_dates\": [\"2026-01-15\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2026-01-15\n\\hline\n英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n\\hline\n{[}WBC{]}白细胞数目 & & 4.20 & & 3.5~9.5 & 10^9/L & {[}HCT{]}红细胞压积 & & 38.3 & & 35~45 & \\% \\\\\n{[}Lym\\%{]}淋巴细胞百分比 & & 28.6 & & 20~50 & \\% & {[}MCV{]}平均红细胞体积 & & 81.3 & $\\downarrow$ & 82~100 & fL \\\\\n{[}Mon\\%{]}单核细胞百分比 & & 5.0 & & 3~10 & \\% & {[}MCH{]}平均红细胞血红蛋白含量 & & 25.6 & $\\downarrow$ & 27~34 & pg \\\\\n{[}Neu\\%{]}中性粒细胞百分比 & & 64.5 & & 40~75 & \\% & {[}MCHC{]}平均红细胞血红蛋白浓度 & & 313 & $\\downarrow$ & 316~354 & g/L \\\\\n{[}Eos\\%{]}嗜酸性细胞百分比 & & 1.7 & & 0.4~8 & \\% & {[}RDW-CV{]}红细胞分布宽度变异系数 & & 14.9 & & 11~16 & \\% \\\\\n{[}Bas\\%{]}嗜碱性细胞百分比 & & 0.2 & & 0.0~1.0 & \\% & {[}RDW-SD{]}红细胞分布宽度标准差 & & 43.2 & & 35.0~56.0 & fL \\\\\n{[}Lym\\# {]}淋巴细胞数目 & & 1.20 & & 1.1~3.2 & 10^9/L & {[}PLT{]}血小板数目 & & 288 & & 125~350 & 10^9/L \\\\\n{[}Mon\\# {]}单核细胞数目 & & 0.21 & & 0.1~0.6 & 10^9/L & {[}MPV{]}平均血小板体积 & & 9.0 & & 6.5~12 & fL \\\\\n{[}Neu\\# {]}中性粒细胞数目 & & 2.71 & & 1.8~6.3 & 10^9/L & {[}PDW{]}血小板分布宽度 & & 15.6 & & 9~17 & fL \\\\\n{[}Eos\\# {]}嗜酸性细胞数目 & & 0.07 & & 0.02~0.52 & 10^9/L & {[}PCT{]}血小板压积 & & 0.258 & & 0.108~ & \\% \\\\\n{[}Bas\\# {]}嗜碱性细胞数目 & & 0.01 & & 0.00~0.06 & 10^9/L & {[}P-LCR{]}大型血小板比率 & & 19.3 & & 11~45 & \\% \\\\\n{[}RBC{]}红细胞数目 & & 4.71 & & 3.8~5.1 & 10^12/L & {[}IG\\%{]}未成熟粒细胞百分比 & & 0.1 & & 0.0~0.6 & \\% \\\\\n{[}HGB{]}血红蛋白 & & 120 & & 115~150 & g/L & {[}IG\\# {]}未成熟粒细胞计数 & & 0.00 & & 0.00~0.06 & 10^9/L \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
[92m11:00:41 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:00:41,342 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:01:00,921 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:01:00,921 INFO     29 [qwen-vl-table] page=46 LLM output (len=4421):
{
  "report_date": "2026-01-15",
  "items": [
    {
      "name": "白细胞数目",
      "item_code": "WBC",
      "value": "4.20",
      "unit": "10^9/L",
      "reference_range": "3.5~9.5",
      "abnormal": false
    },
    {
      "name": "淋巴细胞百分比",
      "item_code": "Lym%",
      "value": "28.6",
      "unit": "%",
      "reference_range": "20~50",
      "abnormal": false
    },
    {
      "name": "单核细胞百分比",
      "item_code": "Mon%",
      "value": "5.0",
      "unit": "%",
      "reference_range": "3~10",
      "abnormal": false
    },
    {
      "name": "中性粒细胞百分比",
      "item_code": "Neu%",
      "value": "64.5",
      "unit": "%",
      "reference_range": "40~75",
      "abnormal": false
    },
    {
      "name": "嗜酸性细胞百分比",
      "item_code": "Eos%",
      "value": "1.7",
      "unit": "%",
      "reference_range": "0.4~8",
      "abnormal": false
    },
    {
      "name": "嗜碱性细胞百分比",
      "item_code": "Bas%",
      "value": "0.2",
      "unit": "%",
      "reference_range": "0.0~1.0",
      "abnormal": false
    },
    {
      "name": "淋巴细胞数目",
      "item_code": "Lym#",
      "value": "1.20",
      "unit": "10^9/L",
      "reference_range": "1.1~3.2",
      "abnormal": false
    },
    {
      "name": "单核细胞数目",
      "item_code": "Mon#",
      "value": "0.21",
      "unit": "10^9/L",
      "reference_range": "0.1~0.6",
      "abnormal": false
    },
    {
      "name": "中性粒细胞数目",
      "item_code": "Neu#",
      "value": "2.71",
      "unit": "10^9/L",
      "reference_range": "1.8~6.3",
      "abnormal": false
    },
    {
      "name": "嗜酸性细胞数目",
      "item_code": "Eos#",
      "value": "0.07",
      "unit": "10^9/L",
      "reference_range": "0.02~0.52",
      "abnormal": false
    },
    {
      "name": "嗜碱性细胞数目",
      "item_code": "Bas#",
      "value": "0.01",
      "unit": "10^9/L",
      "reference_range": "0.00~0.06",
      "abnormal": false
    },
    {
      "name": "红细胞数目",
      "item_code": "RBC",
      "value": "4.71",
      "unit": "10^12/L",
      "reference_range": "3.8~5.1",
      "abnormal": false
    },
    {
      "name": "血红蛋白",
      "item_code": "HGB",
      "value": "120",
      "unit": "g/L",
      "reference_range": "115~150",
      "abnormal": false
    },
    {
      "name": "红细胞压积",
      "item_code": "HCT",
      "value": "38.3",
      "unit": "%",
      "reference_range": "35~45",
      "abnormal": false
    },
    {
      "name": "平均红细胞体积",
      "item_code": "MCV",
      "value": "81.3",
      "unit": "fL",
      "reference_range": "82~100",
      "abnormal": true
    },
    {
      "name": "平均红细胞血红蛋白含量",
      "item_code": "MCH",
      "value": "25.6",
      "unit": "pg",
      "reference_range": "27~34",
      "abnormal": true
    },
    {
      "name": "平均红细胞血红蛋白浓度",
      "item_code": "MCHC",
      "value": "313",
      "unit": "g/L",
      "reference_range": "316~354",
      "abnormal": true
    },
    {
      "name": "红细胞分布宽度变异系数",
      "item_code": "RDW-CV",
      "value": "14.9",
      "unit": "%",
      "reference_range": "11~16",
      "abnormal": false
    },
    {
      "name": "红细胞分布宽度标准差",
      "item_code": "RDW-SD",
      "value": "43.2",
      "unit": "fL",
      "reference_range": "35.0~56.0",
      "abnormal": false
    },
    {
      "name": "血小板数目",
      "item_code": "PLT",
      "value": "288",
      "unit": "10^9/L",
      "reference_range": "125~350",
      "abnormal": false
    },
    {
      "name": "平均血小板体积",
      "item_code": "MPV",
      "value": "9.0",
      "unit": "fL",
      "reference_range": "6.5~12",
      "abnormal": false
    },
    {
      "name": "血小板分布宽度",
      "item_code": "PDW",
      "value": "15.6",
      "unit": "fL",
      "reference_range": "9~17",
      "abnormal": false
    },
    {
      "name": "血小板压积",
      "item_code": "PCT",
      "value": "0.258",
      "unit": "%",
      "reference_range": "0.108~",
      "abnormal": false
    },
    {
      "name": "大型血小板比率",
      "item_code": "P-LCR",
      "value": "19.3",
      "unit": "%",
      "reference_range": "11~45",
      "abnormal": false
    },
    {
      "name": "未成熟粒细胞百分比",
      "item_code": "IG%",
      "value": "0.1",
      "unit": "%",
      "reference_range": "0.0~0.6",
      "abnormal": false
    },
    {
      "name": "未成熟粒细胞计数",
      "item_code": "IG#",
      "value": "0.00",
      "unit": "10^9/L",
      "reference_range": "0.00~0.06",
      "abnormal": false
    }
  ]
}
2026-08-05 11:01:00,921 INFO     29 [qwen-vl-table] coord grouping: {46: 26}
2026-08-05 11:01:00,924 INFO     29 [qwen-vl-table] coord API call start, page=46, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1400057, prompt_len=720
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
白细胞数目、淋巴细胞百分比、单核细胞百分比、中性粒细胞百分比、嗜酸性细胞百分比、嗜碱性细胞百分比、淋巴细胞数目、单核细胞数目、中性粒细胞数目、嗜酸性细胞数目、嗜碱性细胞数目、红细胞数目、血红蛋白、红细胞压积、平均红细胞体积、平均红细胞血红蛋白含量、平均红细胞血红蛋白浓度、红细胞分布宽度变异系数、红细胞分布宽度标准差、血小板数目、平均血小板体积、血小板分布宽度、血小板压积、大型血小板比率、未成熟粒细胞百分比、未成熟粒细胞计数

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
2026-08-05 11:01:08,726 INFO     29 [qwen-vl-table] coord API raw response (len=1360):
[
	{"text": "白细胞数目", "bbox": [144, 275, 252, 295]},
	{"text": "淋巴细胞百分比", "bbox": [144, 303, 288, 323]},
	{"text": "单核细胞百分比", "bbox": [144, 330, 291, 350]},
	{"text": "中性粒细胞百分比", "bbox": [144, 357, 288, 377]},
	{"text": "嗜酸性细胞百分比", "bbox": [144, 405, 283, 425]},
	{"text": "嗜碱性细胞百分比", "bbox": [144, 455, 283, 475]},
	{"text": "淋巴细胞数目", "bbox": [144, 505, 270, 525]},
	{"text": "单核细胞数目", "bbox": [144, 532, 274, 552]},
	{"text": "中性粒细胞数目", "bbox": [144, 560, 284, 580]},
	{"text": "嗜酸性细胞数目", "bbox": [144, 587, 280, 607]},
	{"text": "嗜碱性细胞数目", "bbox": [144, 615, 280, 635]},
	{"text": "红细胞数目", "bbox": [144, 643, 248, 663]},
	{"text": "血红蛋白", "bbox": [144, 671, 237, 691]},
	{"text": "红细胞压积", "bbox": [504, 275, 608, 295]},
	{"text": "平均红细胞体积", "bbox": [504, 303, 640, 323]},
	{"text": "平均红细胞血红蛋白含量", "bbox": [504, 330, 655, 350]},
	{"text": "平均红细胞血红蛋白浓度", "bbox": [504, 379, 651, 399]},
	{"text": "红细胞分布宽度变异系数", "bbox": [504, 428, 653, 448]},
	{"text": "红细胞分布宽度标准差", "bbox": [504, 478, 653, 498]},
	{"text": "血小板数目", "bbox": [504, 528, 604, 548]},
	{"text": "平均血小板体积", "bbox": [504, 555, 640, 575]},
	{"text": "血小板分布宽度", "bbox": [504, 583, 641, 603]},
	{"text": "血小板压积", "bbox": [504, 621, 608, 641]},
	{"text": "大型血小板比率", "bbox": [504, 660, 649, 680]},
	{"text": "未成熟粒细胞百分比", "bbox": [504, 687, 650, 707]},
	{"text": "未成熟粒细胞计数", "bbox": [504, 736, 648, 756]}
]
2026-08-05 11:01:08,726 INFO     29 [qwen-vl-table] coord API: raw_items=26, valid_items=26, elapsed=7.8s
2026-08-05 11:01:08,726 INFO     29 [qwen-vl-table] coord item[0]: text=白细胞数目, bbox=[144, 275, 252, 295]
2026-08-05 11:01:08,726 INFO     29 [qwen-vl-table] coord item[1]: text=淋巴细胞百分比, bbox=[144, 303, 288, 323]
2026-08-05 11:01:08,726 INFO     29 [qwen-vl-table] coord item[2]: text=单核细胞百分比, bbox=[144, 330, 291, 350]
2026-08-05 11:01:08,726 INFO     29 [qwen-vl-table] coord item[3]: text=中性粒细胞百分比, bbox=[144, 357, 288, 377]
2026-08-05 11:01:08,726 INFO     29 [qwen-vl-table] coord item[4]: text=嗜酸性细胞百分比, bbox=[144, 405, 283, 425]
2026-08-05 11:01:08,726 INFO     29 [qwen-vl-table] coord item[5]: text=嗜碱性细胞百分比, bbox=[144, 455, 283, 475]
2026-08-05 11:01:08,726 INFO     29 [qwen-vl-table] coord item[6]: text=淋巴细胞数目, bbox=[144, 505, 270, 525]
2026-08-05 11:01:08,726 INFO     29 [qwen-vl-table] coord item[7]: text=单核细胞数目, bbox=[144, 532, 274, 552]
2026-08-05 11:01:08,726 INFO     29 [qwen-vl-table] coord item[8]: text=中性粒细胞数目, bbox=[144, 560, 284, 580]
2026-08-05 11:01:08,726 INFO     29 [qwen-vl-table] coord item[9]: text=嗜酸性细胞数目, bbox=[144, 587, 280, 607]
2026-08-05 11:01:08,726 INFO     29 [qwen-vl-table] coord item[10]: text=嗜碱性细胞数目, bbox=[144, 615, 280, 635]
2026-08-05 11:01:08,727 INFO     29 [qwen-vl-table] coord item[11]: text=红细胞数目, bbox=[144, 643, 248, 663]
2026-08-05 11:01:08,727 INFO     29 [qwen-vl-table] coord item[12]: text=血红蛋白, bbox=[144, 671, 237, 691]
2026-08-05 11:01:08,727 INFO     29 [qwen-vl-table] coord item[13]: text=红细胞压积, bbox=[504, 275, 608, 295]
2026-08-05 11:01:08,727 INFO     29 [qwen-vl-table] coord item[14]: text=平均红细胞体积, bbox=[504, 303, 640, 323]
2026-08-05 11:01:08,727 INFO     29 [qwen-vl-table] coord item[15]: text=平均红细胞血红蛋白含量, bbox=[504, 330, 655, 350]
2026-08-05 11:01:08,727 INFO     29 [qwen-vl-table] coord item[16]: text=平均红细胞血红蛋白浓度, bbox=[504, 379, 651, 399]
2026-08-05 11:01:08,727 INFO     29 [qwen-vl-table] coord item[17]: text=红细胞分布宽度变异系数, bbox=[504, 428, 653, 448]
2026-08-05 11:01:08,727 INFO     29 [qwen-vl-table] coord item[18]: text=红细胞分布宽度标准差, bbox=[504, 478, 653, 498]
2026-08-05 11:01:08,727 INFO     29 [qwen-vl-table] coord item[19]: text=血小板数目, bbox=[504, 528, 604, 548]
2026-08-05 11:01:08,727 INFO     29 [qwen-vl-table] coord item[20]: text=平均血小板体积, bbox=[504, 555, 640, 575]
2026-08-05 11:01:08,727 INFO     29 [qwen-vl-table] coord item[21]: text=血小板分布宽度, bbox=[504, 583, 641, 603]
2026-08-05 11:01:08,727 INFO     29 [qwen-vl-table] coord item[22]: text=血小板压积, bbox=[504, 621, 608, 641]
2026-08-05 11:01:08,727 INFO     29 [qwen-vl-table] coord item[23]: text=大型血小板比率, bbox=[504, 660, 649, 680]
2026-08-05 11:01:08,727 INFO     29 [qwen-vl-table] coord item[24]: text=未成熟粒细胞百分比, bbox=[504, 687, 650, 707]
2026-08-05 11:01:08,727 INFO     29 [qwen-vl-table] coord item[25]: text=未成熟粒细胞计数, bbox=[504, 736, 648, 756]
2026-08-05 11:01:08,727 INFO     29 [qwen-vl-table] page=46 coord: matched 26/26, time=7.8s
2026-08-05 11:01:08,727 INFO     29 [qwen-vl-table] new_positions (26):
[[47, 121.24799999999999, 212.184, 163.625, 175.525], [47, 121.24799999999999, 242.49599999999998, 180.285, 192.185], [47, 121.24799999999999, 245.022, 196.35, 208.25], [47, 121.24799999999999, 242.49599999999998, 212.415, 224.315], [47, 121.24799999999999, 238.286, 240.975, 252.875], [47, 121.24799999999999, 238.286, 270.72499999999997, 282.625], [47, 121.24799999999999, 227.34, 300.47499999999997, 312.375], [47, 121.24799999999999, 230.708, 316.53999999999996, 328.44], [47, 121.24799999999999, 239.128, 333.2, 345.09999999999997], [47, 121.24799999999999, 235.76, 349.265, 361.16499999999996], [47, 121.24799999999999, 235.76, 365.925, 377.825], [47, 121.24799999999999, 208.816, 382.585, 394.48499999999996], [47, 121.24799999999999, 199.554, 399.245, 411.145], [47, 424.368, 511.936, 163.625, 175.525], [47, 424.368, 538.88, 180.285, 192.185], [47, 424.368, 551.51, 196.35, 208.25], [47, 424.368, 548.1419999999999, 225.505, 237.405], [47, 424.368, 549.826, 254.66, 266.56], [47, 424.368, 549.826, 284.40999999999997, 296.31], [47, 424.368, 508.568, 314.15999999999997, 326.06], [47, 424.368, 538.88, 330.22499999999997, 342.125], [47, 424.368, 539.722, 346.885, 358.78499999999997], [47, 424.368, 511.936, 369.495, 381.395], [47, 424.368, 546.458, 392.7, 404.59999999999997], [47, 424.368, 547.3, 408.765, 420.66499999999996], [47, 424.368, 545.616, 437.91999999999996, 449.82]]
2026-08-05 11:01:08,727 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=26, matched=26, pages=1, time=27.6s
2026-08-05 11:01:08,729 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 11:01:08,729 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[47]
2026-08-05 11:01:08,729 INFO     29 [qwen-vl-table] positions ： [[47, 0.0, 0.0, 0.0, 0.0], [47, 0.0, 0.0, 0.0, 0.0], [47, 0.0, 0.0, 0.0, 0.0], [47, 0.0, 0.0, 0.0, 0.0], [47, 0.0, 0.0, 0.0, 0.0], [47, 0.0, 0.0, 0.0, 0.0], [47, 0.0, 0.0, 0.0, 0.0], [47, 0.0, 0.0, 0.0, 0.0], [47, 0.0, 0.0, 0.0, 0.0], [47, 0.0, 0.0, 0.0, 0.0], [47, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 11:01:08,954 INFO     29 [qwen-vl-table] page=47, rect=842x595, img=(2339x1653)
2026-08-05 11:01:08,955 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 11:01:08,955 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2251, \"bbox_end\": 2261, \"encounter_dates\": [\"2026-01-15\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2026-01-15\n\\hline\n\\textbf{英文} & \\textbf{项目名称} & \\textbf{结果} & \\textbf{提示} & \\textbf{参考范围} & \\textbf{单位} & \\textbf{英文} & \\textbf{项目名称} & \\textbf{结果} & \\textbf{提示} & \\textbf{参考范围} & \\textbf{单位} \\\\\n\\hline\n{[TBIL]}总胆红素 & & 8.7 & & 0.0~21.0 & \\textmu mol/L & {[Cl]}氯 & & 105 & & 99~110 & mmol/L \\\\\n{[DBIL]}直接胆红素 & & 3.5 & & 0.0~8.0 & \\textmu mol/L & {[Ca]}钙 & & 2.38 & & 2.11~2.52 & mmol/L \\\\\n{[IBIL]}间接胆红素 & & 5.2 & & 0.0~13.0 & \\textmu mol/L & {[CO2cp]}二氧化碳结合力 & & 27.6 & & 21.0~31.0 & mmol/L \\\\\n{[ALT]}谷丙转氨酶 & & 7.0 & & 7~40 & U/L & {[m-AST]}谷草转氨酶线粒体同工酶 & & 2.0 & & 0~18 & U/L \\\\\n{[AST]}谷草转氨酶 & & 15 & & 13~35 & U/L & {[CK]}肌酸激酶 & & 37 & & 24~200 & U/L \\\\\n{[AST/ALT]}谷草/谷丙 & 2.14 & & \\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\",
    "role": "user"
  }
]
[92m11:01:08 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:01:08,957 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:01:08,958 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T11:01:08.957+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 11:01:21,116 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:01:21,116 INFO     29 [qwen-vl-table] page=47 LLM output (len=1880):
{
  "report_date": "2026-01-15",
  "items": [
    {
      "name": "总胆红素",
      "item_code": "TBIL",
      "value": "8.7",
      "unit": "μmol/L",
      "reference_range": "0.0~21.0",
      "abnormal": false
    },
    {
      "name": "直接胆红素",
      "item_code": "DBIL",
      "value": "3.5",
      "unit": "μmol/L",
      "reference_range": "0.0~8.0",
      "abnormal": false
    },
    {
      "name": "间接胆红素",
      "item_code": "IBIL",
      "value": "5.2",
      "unit": "μmol/L",
      "reference_range": "0.0~13.0",
      "abnormal": false
    },
    {
      "name": "谷丙转氨酶",
      "item_code": "ALT",
      "value": "7.0",
      "unit": "U/L",
      "reference_range": "7~40",
      "abnormal": false
    },
    {
      "name": "谷草转氨酶",
      "item_code": "AST",
      "value": "15",
      "unit": "U/L",
      "reference_range": "13~35",
      "abnormal": false
    },
    {
      "name": "谷草/谷丙",
      "item_code": "AST/ALT",
      "value": "2.14",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "氯",
      "item_code": "Cl",
      "value": "105",
      "unit": "mmol/L",
      "reference_range": "99~110",
      "abnormal": false
    },
    {
      "name": "钙",
      "item_code": "Ca",
      "value": "2.38",
      "unit": "mmol/L",
      "reference_range": "2.11~2.52",
      "abnormal": false
    },
    {
      "name": "二氧化碳结合力",
      "item_code": "CO2cp",
      "value": "27.6",
      "unit": "mmol/L",
      "reference_range": "21.0~31.0",
      "abnormal": false
    },
    {
      "name": "谷草转氨酶线粒体同工酶",
      "item_code": "m-AST",
      "value": "2.0",
      "unit": "U/L",
      "reference_range": "0~18",
      "abnormal": false
    },
    {
      "name": "肌酸激酶",
      "item_code": "CK",
      "value": "37",
      "unit": "U/L",
      "reference_range": "24~200",
      "abnormal": false
    }
  ]
}
2026-08-05 11:01:21,116 INFO     29 [qwen-vl-table] coord grouping: {47: 11}
2026-08-05 11:01:21,119 INFO     29 [qwen-vl-table] coord API call start, page=47, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1414856, prompt_len=570
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
总胆红素、直接胆红素、间接胆红素、谷丙转氨酶、谷草转氨酶、谷草/谷丙、氯、钙、二氧化碳结合力、谷草转氨酶线粒体同工酶、肌酸激酶

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
2026-08-05 11:01:25,188 INFO     29 [qwen-vl-table] coord API raw response (len=562):
```json
[
	{"text": "总胆红素", "bbox": [127, 318, 222, 341]},
	{"text": "直接胆红素", "bbox": [127, 347, 239, 370]},
	{"text": "间接胆红素", "bbox": [127, 375, 232, 398]},
	{"text": "谷丙转氨酶", "bbox": [127, 404, 232, 427]},
	{"text": "谷草转氨酶", "bbox": [127, 433, 232, 456]},
	{"text": "谷草/谷丙", "bbox": [127, 462, 257, 485]},
	{"text": "氯", "bbox": [504, 318, 540, 341]},
	{"text": "钙", "bbox": [504, 347, 544, 370]},
	{"text": "二氧化碳结合力", "bbox": [504, 375, 657, 398]},
	{"text": "谷草转氨酶线粒体同工酶", "bbox": [504, 404, 657, 427]},
	{"text": "肌酸激酶", "bbox": [504, 456, 588, 479]}
]
```
2026-08-05 11:01:25,188 INFO     29 [qwen-vl-table] coord API: raw_items=11, valid_items=11, elapsed=4.1s
2026-08-05 11:01:25,188 INFO     29 [qwen-vl-table] coord item[0]: text=总胆红素, bbox=[127, 318, 222, 341]
2026-08-05 11:01:25,188 INFO     29 [qwen-vl-table] coord item[1]: text=直接胆红素, bbox=[127, 347, 239, 370]
2026-08-05 11:01:25,188 INFO     29 [qwen-vl-table] coord item[2]: text=间接胆红素, bbox=[127, 375, 232, 398]
2026-08-05 11:01:25,189 INFO     29 [qwen-vl-table] coord item[3]: text=谷丙转氨酶, bbox=[127, 404, 232, 427]
2026-08-05 11:01:25,189 INFO     29 [qwen-vl-table] coord item[4]: text=谷草转氨酶, bbox=[127, 433, 232, 456]
2026-08-05 11:01:25,189 INFO     29 [qwen-vl-table] coord item[5]: text=谷草/谷丙, bbox=[127, 462, 257, 485]
2026-08-05 11:01:25,189 INFO     29 [qwen-vl-table] coord item[6]: text=氯, bbox=[504, 318, 540, 341]
2026-08-05 11:01:25,189 INFO     29 [qwen-vl-table] coord item[7]: text=钙, bbox=[504, 347, 544, 370]
2026-08-05 11:01:25,189 INFO     29 [qwen-vl-table] coord item[8]: text=二氧化碳结合力, bbox=[504, 375, 657, 398]
2026-08-05 11:01:25,189 INFO     29 [qwen-vl-table] coord item[9]: text=谷草转氨酶线粒体同工酶, bbox=[504, 404, 657, 427]
2026-08-05 11:01:25,189 INFO     29 [qwen-vl-table] coord item[10]: text=肌酸激酶, bbox=[504, 456, 588, 479]
2026-08-05 11:01:25,189 INFO     29 [qwen-vl-table] page=47 coord: matched 11/11, time=4.1s
2026-08-05 11:01:25,189 INFO     29 [qwen-vl-table] new_positions (11):
[[48, 106.934, 186.924, 189.20999999999998, 202.89499999999998], [48, 106.934, 201.238, 206.465, 220.14999999999998], [48, 106.934, 195.344, 223.125, 236.81], [48, 106.934, 195.344, 240.38, 254.065], [48, 106.934, 195.344, 257.635, 271.32], [48, 106.934, 216.394, 274.89, 288.575], [48, 424.368, 454.68, 189.20999999999998, 202.89499999999998], [48, 424.368, 458.048, 206.465, 220.14999999999998], [48, 424.368, 553.194, 223.125, 236.81], [48, 424.368, 553.194, 240.38, 254.065], [48, 424.368, 495.096, 271.32, 285.005]]
2026-08-05 11:01:25,189 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=11, matched=11, pages=1, time=16.5s
2026-08-05 11:01:25,190 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 11:01:25,191 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[48]
2026-08-05 11:01:25,191 INFO     29 [qwen-vl-table] positions ： [[48, 0.0, 0.0, 0.0, 0.0], [48, 0.0, 0.0, 0.0, 0.0], [48, 0.0, 0.0, 0.0, 0.0], [48, 0.0, 0.0, 0.0, 0.0], [48, 0.0, 0.0, 0.0, 0.0], [48, 0.0, 0.0, 0.0, 0.0], [48, 0.0, 0.0, 0.0, 0.0], [48, 0.0, 0.0, 0.0, 0.0], [48, 0.0, 0.0, 0.0, 0.0], [48, 0.0, 0.0, 0.0, 0.0], [48, 0.0, 0.0, 0.0, 0.0], [48, 0.0, 0.0, 0.0, 0.0], [48, 0.0, 0.0, 0.0, 0.0], [48, 0.0, 0.0, 0.0, 0.0], [48, 0.0, 0.0, 0.0, 0.0], [48, 0.0, 0.0, 0.0, 0.0], [48, 0.0, 0.0, 0.0, 0.0], [48, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 11:01:25,419 INFO     29 [qwen-vl-table] page=48, rect=842x595, img=(2339x1653)
2026-08-05 11:01:25,420 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 11:01:25,420 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2262, \"bbox_end\": 2279, \"encounter_dates\": [\"2026-01-15\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccccc}\n报告时间: 2026-01-15\n\\hline\n英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 \\\\\n\\hline\n[颜色]颜色 & 黄色 & & & 黄、淡黄 & & [SG]尿比重 & 1.020 & 1.003~ \\\\\n[浊度]浊度 & 清亮 & & & 清 & & [VC]维生素C & 0.0 & - \\\\\n[GLU]葡萄糖 & - & & & - & & [WBC]白细胞 & 28.00 & 0~28 \\\\\n[NQX]尿潜血 & - & & & - & mg/l & [RBC]红细胞 & 6.00 & 0~17 \\\\\n[LEU]白细胞 & - & & & - & & [粘液丝]粘液丝 & 11 & 0~28 \\\\\n[PRO]尿蛋白 & - & & & - & & [结晶]结晶 & 0.0 & 0~28 \\\\\n[NIT]亚硝酸盐 & + & & & - & & [管型]管型 & 0 & 0~2 \\\\\n[URO]尿胆原 & - & & & - & & [EC]上皮细胞 & 39.00 & 0~34 \\\\\n[BIL]胆红素 & - & & & - & & [BACT细菌]细菌 & 163.00 & 0~7 \\\\\n[KET]尿酮体 & - & & & - & & [BYST真菌]真菌 & 0 & 0~1 \\\\\n[pH]pH值 & 6.0 & & & 4.5~8.0 & & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
[92m11:01:25 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:01:25,421 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:01:38,994 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T11:01:38.994+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 11:01:39,393 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:01:39,393 INFO     29 [qwen-vl-table] page=48 LLM output (len=3337):
{
  "report_date": "2026-01-15",
  "items": [
    {
      "name": "颜色",
      "item_code": null,
      "value": "黄色",
      "unit": null,
      "reference_range": "黄、淡黄",
      "abnormal": false
    },
    {
      "name": "浊度",
      "item_code": null,
      "value": "清亮",
      "unit": null,
      "reference_range": "清",
      "abnormal": false
    },
    {
      "name": "葡萄糖",
      "item_code": "GLU",
      "value": "-",
      "unit": null,
      "reference_range": "-",
      "abnormal": false
    },
    {
      "name": "尿潜血",
      "item_code": "NQX",
      "value": "-",
      "unit": "mg/l",
      "reference_range": "-",
      "abnormal": false
    },
    {
      "name": "白细胞",
      "item_code": "LEU",
      "value": "-",
      "unit": null,
      "reference_range": "-",
      "abnormal": false
    },
    {
      "name": "尿蛋白",
      "item_code": "PRO",
      "value": "-",
      "unit": null,
      "reference_range": "-",
      "abnormal": false
    },
    {
      "name": "亚硝酸盐",
      "item_code": "NIT",
      "value": "+",
      "unit": null,
      "reference_range": "-",
      "abnormal": true
    },
    {
      "name": "尿胆原",
      "item_code": "URO",
      "value": "-",
      "unit": null,
      "reference_range": "-",
      "abnormal": false
    },
    {
      "name": "胆红素",
      "item_code": "BIL",
      "value": "-",
      "unit": null,
      "reference_range": "-",
      "abnormal": false
    },
    {
      "name": "尿酮体",
      "item_code": "KET",
      "value": "-",
      "unit": null,
      "reference_range": "-",
      "abnormal": false
    },
    {
      "name": "pH值",
      "item_code": "pH",
      "value": "6.0",
      "unit": null,
      "reference_range": "4.5~8.0",
      "abnormal": false
    },
    {
      "name": "尿比重",
      "item_code": "SG",
      "value": "1.020",
      "unit": null,
      "reference_range": "1.003~",
      "abnormal": false
    },
    {
      "name": "维生素C",
      "item_code": "VC",
      "value": "0.0",
      "unit": null,
      "reference_range": "-",
      "abnormal": false
    },
    {
      "name": "白细胞",
      "item_code": "WBC",
      "value": "28.00",
      "unit": null,
      "reference_range": "0~28",
      "abnormal": false
    },
    {
      "name": "红细胞",
      "item_code": "RBC",
      "value": "6.00",
      "unit": null,
      "reference_range": "0~17",
      "abnormal": false
    },
    {
      "name": "粘液丝",
      "item_code": null,
      "value": "11",
      "unit": null,
      "reference_range": "0~28",
      "abnormal": false
    },
    {
      "name": "结晶",
      "item_code": null,
      "value": "0.0",
      "unit": null,
      "reference_range": "0~28",
      "abnormal": false
    },
    {
      "name": "管型",
      "item_code": null,
      "value": "0",
      "unit": null,
      "reference_range": "0~2",
      "abnormal": false
    },
    {
      "name": "上皮细胞",
      "item_code": "EC",
      "value": "39.00",
      "unit": null,
      "reference_range": "0~34",
      "abnormal": true
    },
    {
      "name": "细菌",
      "item_code": "BACT",
      "value": "163.00",
      "unit": null,
      "reference_range": "0~7",
      "abnormal": true
    },
    {
      "name": "真菌",
      "item_code": "BYST",
      "value": "0",
      "unit": null,
      "reference_range": "0~1",
      "abnormal": false
    }
  ]
}
2026-08-05 11:01:39,393 INFO     29 [qwen-vl-table] coord grouping: {48: 21}
2026-08-05 11:01:39,400 INFO     29 [qwen-vl-table] coord API call start, page=48, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1458490, prompt_len=587
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
颜色、浊度、葡萄糖、尿潜血、白细胞、尿蛋白、亚硝酸盐、尿胆原、胆红素、尿酮体、pH值、尿比重、维生素C、白细胞、红细胞、粘液丝、结晶、管型、上皮细胞、细菌、真菌

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
2026-08-05 11:01:45,630 INFO     29 [qwen-vl-table] coord API raw response (len=996):
[
	{"text": "颜色", "bbox": [58, 342, 137, 367]},
	{"text": "浊度", "bbox": [58, 377, 137, 402]},
	{"text": "葡萄糖", "bbox": [58, 412, 153, 437]},
	{"text": "尿潜血", "bbox": [58, 446, 157, 471]},
	{"text": "白细胞", "bbox": [58, 479, 149, 504]},
	{"text": "尿蛋白", "bbox": [58, 513, 153, 538]},
	{"text": "亚硝酸盐", "bbox": [58, 547, 164, 572]},
	{"text": "尿胆原", "bbox": [58, 582, 157, 607]},
	{"text": "胆红素", "bbox": [58, 616, 143, 641]},
	{"text": "尿酮体", "bbox": [58, 651, 148, 676]},
	{"text": "pH值", "bbox": [58, 685, 132, 711]},
	{"text": "尿比重", "bbox": [507, 357, 593, 382]},
	{"text": "维生素C", "bbox": [507, 404, 604, 429]},
	{"text": "白细胞", "bbox": [507, 440, 608, 465]},
	{"text": "红细胞", "bbox": [507, 473, 602, 498]},
	{"text": "粘液丝", "bbox": [507, 507, 620, 532]},
	{"text": "结晶", "bbox": [507, 541, 585, 566]},
	{"text": "管型", "bbox": [507, 576, 585, 601]},
	{"text": "上皮细胞", "bbox": [507, 610, 606, 635]},
	{"text": "细菌", "bbox": [507, 645, 629, 670]},
	{"text": "真菌", "bbox": [507, 679, 626, 704]}
]
2026-08-05 11:01:45,631 INFO     29 [qwen-vl-table] coord API: raw_items=21, valid_items=21, elapsed=6.2s
2026-08-05 11:01:45,631 INFO     29 [qwen-vl-table] coord item[0]: text=颜色, bbox=[58, 342, 137, 367]
2026-08-05 11:01:45,631 INFO     29 [qwen-vl-table] coord item[1]: text=浊度, bbox=[58, 377, 137, 402]
2026-08-05 11:01:45,631 INFO     29 [qwen-vl-table] coord item[2]: text=葡萄糖, bbox=[58, 412, 153, 437]
2026-08-05 11:01:45,631 INFO     29 [qwen-vl-table] coord item[3]: text=尿潜血, bbox=[58, 446, 157, 471]
2026-08-05 11:01:45,631 INFO     29 [qwen-vl-table] coord item[4]: text=白细胞, bbox=[58, 479, 149, 504]
2026-08-05 11:01:45,631 INFO     29 [qwen-vl-table] coord item[5]: text=尿蛋白, bbox=[58, 513, 153, 538]
2026-08-05 11:01:45,631 INFO     29 [qwen-vl-table] coord item[6]: text=亚硝酸盐, bbox=[58, 547, 164, 572]
2026-08-05 11:01:45,631 INFO     29 [qwen-vl-table] coord item[7]: text=尿胆原, bbox=[58, 582, 157, 607]
2026-08-05 11:01:45,631 INFO     29 [qwen-vl-table] coord item[8]: text=胆红素, bbox=[58, 616, 143, 641]
2026-08-05 11:01:45,631 INFO     29 [qwen-vl-table] coord item[9]: text=尿酮体, bbox=[58, 651, 148, 676]
2026-08-05 11:01:45,631 INFO     29 [qwen-vl-table] coord item[10]: text=pH值, bbox=[58, 685, 132, 711]
2026-08-05 11:01:45,631 INFO     29 [qwen-vl-table] coord item[11]: text=尿比重, bbox=[507, 357, 593, 382]
2026-08-05 11:01:45,631 INFO     29 [qwen-vl-table] coord item[12]: text=维生素C, bbox=[507, 404, 604, 429]
2026-08-05 11:01:45,631 INFO     29 [qwen-vl-table] coord item[13]: text=白细胞, bbox=[507, 440, 608, 465]
2026-08-05 11:01:45,631 INFO     29 [qwen-vl-table] coord item[14]: text=红细胞, bbox=[507, 473, 602, 498]
2026-08-05 11:01:45,631 INFO     29 [qwen-vl-table] coord item[15]: text=粘液丝, bbox=[507, 507, 620, 532]
2026-08-05 11:01:45,631 INFO     29 [qwen-vl-table] coord item[16]: text=结晶, bbox=[507, 541, 585, 566]
2026-08-05 11:01:45,631 INFO     29 [qwen-vl-table] coord item[17]: text=管型, bbox=[507, 576, 585, 601]
2026-08-05 11:01:45,631 INFO     29 [qwen-vl-table] coord item[18]: text=上皮细胞, bbox=[507, 610, 606, 635]
2026-08-05 11:01:45,631 INFO     29 [qwen-vl-table] coord item[19]: text=细菌, bbox=[507, 645, 629, 670]
2026-08-05 11:01:45,631 INFO     29 [qwen-vl-table] coord item[20]: text=真菌, bbox=[507, 679, 626, 704]
2026-08-05 11:01:45,631 INFO     29 [qwen-vl-table] page=48 coord: matched 21/21, time=6.2s
2026-08-05 11:01:45,631 INFO     29 [qwen-vl-table] new_positions (21):
[[49, 48.836, 115.354, 203.48999999999998, 218.36499999999998], [49, 48.836, 115.354, 224.315, 239.19], [49, 48.836, 128.826, 245.14, 260.015], [49, 48.836, 132.194, 265.37, 280.245], [49, 426.894, 511.936, 261.8, 276.675], [49, 48.836, 128.826, 305.235, 320.11], [49, 48.836, 138.088, 325.465, 340.34], [49, 48.836, 132.194, 346.28999999999996, 361.16499999999996], [49, 48.836, 120.40599999999999, 366.52, 381.395], [49, 48.836, 124.616, 387.34499999999997, 402.21999999999997], [49, 48.836, 111.14399999999999, 407.575, 423.04499999999996], [49, 426.894, 499.306, 212.415, 227.29], [49, 426.894, 508.568, 240.38, 255.255], [49, 426.894, 511.936, 261.8, 276.675], [49, 426.894, 506.88399999999996, 281.435, 296.31], [49, 426.894, 522.04, 301.66499999999996, 316.53999999999996], [49, 426.894, 492.57, 321.895, 336.77], [49, 426.894, 492.57, 342.71999999999997, 357.59499999999997], [49, 426.894, 510.252, 362.95, 377.825], [49, 426.894, 529.6179999999999, 383.775, 398.65], [49, 426.894, 527.092, 404.005, 418.88]]
2026-08-05 11:01:45,631 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=21, matched=21, pages=1, time=20.4s
2026-08-05 11:01:45,633 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 11:01:45,633 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[49]
2026-08-05 11:01:45,633 INFO     29 [qwen-vl-table] positions ： [[49, 0.0, 0.0, 0.0, 0.0], [49, 0.0, 0.0, 0.0, 0.0], [49, 0.0, 0.0, 0.0, 0.0], [49, 0.0, 0.0, 0.0, 0.0], [49, 0.0, 0.0, 0.0, 0.0], [49, 0.0, 0.0, 0.0, 0.0], [49, 0.0, 0.0, 0.0, 0.0], [49, 0.0, 0.0, 0.0, 0.0], [49, 0.0, 0.0, 0.0, 0.0], [49, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 11:01:45,814 INFO     29 [qwen-vl-table] page=49, rect=842x595, img=(2339x1653)
2026-08-05 11:01:45,814 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 11:01:45,815 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2280, \"bbox_end\": 2289, \"encounter_dates\": [\"2026-01-15\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccc}\n报告时间: 2026-01-15\n\\hline\n英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n\\hline\n[FT3]游离三碘甲状腺原氨酸 & & 3.11 & & 2.14~4.21 & pg/mL \\\\\n[FRt4]游离甲状腺素 & & 0.76 & & 0.61~1.12 & ng/dL \\\\\n[fTSH3]超敏促甲状腺素 & & 1.350 & & 0.560~5.910 & uIU/ml \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
[92m11:01:45 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:01:45,816 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:01:50,020 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:01:50,020 INFO     29 [qwen-vl-table] page=49 LLM output (len=575):
{
  "report_date": "2026-01-15",
  "items": [
    {
      "name": "游离三碘甲状腺原氨酸",
      "item_code": "FT3",
      "value": "3.11",
      "unit": "pg/mL",
      "reference_range": "2.14~4.21",
      "abnormal": false
    },
    {
      "name": "游离甲状腺素",
      "item_code": "FRt4",
      "value": "0.76",
      "unit": "ng/dL",
      "reference_range": "0.61~1.12",
      "abnormal": false
    },
    {
      "name": "超敏促甲状腺素",
      "item_code": "fTSH3",
      "value": "1.350",
      "unit": "uIU/ml",
      "reference_range": "0.560~5.910",
      "abnormal": false
    }
  ]
}
2026-08-05 11:01:50,020 INFO     29 [qwen-vl-table] coord grouping: {49: 3}
2026-08-05 11:01:50,021 INFO     29 [qwen-vl-table] coord API call start, page=49, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=793452, prompt_len=532
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
游离三碘甲状腺原氨酸、游离甲状腺素、超敏促甲状腺素

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
2026-08-05 11:01:52,044 INFO     29 [qwen-vl-table] coord API raw response (len=157):
[
	{"text": "游离三碘甲状腺原氨酸", "bbox": [78, 332, 276, 355]},
	{"text": "游离甲状腺素", "bbox": [78, 363, 220, 386]},
	{"text": "超敏促甲状腺素", "bbox": [78, 394, 244, 417]}
]
2026-08-05 11:01:52,044 INFO     29 [qwen-vl-table] coord API: raw_items=3, valid_items=3, elapsed=2.0s
2026-08-05 11:01:52,044 INFO     29 [qwen-vl-table] coord item[0]: text=游离三碘甲状腺原氨酸, bbox=[78, 332, 276, 355]
2026-08-05 11:01:52,045 INFO     29 [qwen-vl-table] coord item[1]: text=游离甲状腺素, bbox=[78, 363, 220, 386]
2026-08-05 11:01:52,045 INFO     29 [qwen-vl-table] coord item[2]: text=超敏促甲状腺素, bbox=[78, 394, 244, 417]
2026-08-05 11:01:52,045 INFO     29 [qwen-vl-table] page=49 coord: matched 3/3, time=2.0s
2026-08-05 11:01:52,045 INFO     29 [qwen-vl-table] new_positions (3):
[[50, 65.676, 232.392, 197.54, 211.225], [50, 65.676, 185.23999999999998, 215.98499999999999, 229.67], [50, 65.676, 205.44799999999998, 234.42999999999998, 248.11499999999998]]
2026-08-05 11:01:52,045 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=3, matched=3, pages=1, time=6.4s
2026-08-05 11:01:52,047 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 11:01:52,047 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[50]
2026-08-05 11:01:52,047 INFO     29 [qwen-vl-table] positions ： [[50, 0.0, 0.0, 0.0, 0.0], [50, 0.0, 0.0, 0.0, 0.0], [50, 0.0, 0.0, 0.0, 0.0], [50, 0.0, 0.0, 0.0, 0.0], [50, 0.0, 0.0, 0.0, 0.0], [50, 0.0, 0.0, 0.0, 0.0], [50, 0.0, 0.0, 0.0, 0.0], [50, 0.0, 0.0, 0.0, 0.0], [50, 0.0, 0.0, 0.0, 0.0], [50, 0.0, 0.0, 0.0, 0.0], [50, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 11:01:52,246 INFO     29 [qwen-vl-table] page=50, rect=842x595, img=(2339x1653)
2026-08-05 11:01:52,247 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 11:01:52,248 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 2290, \"bbox_end\": 2300, \"encounter_dates\": [\"2026-01-15\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccc}\n报告时间: 2026-01-15\n\\hline\n英文 & 项目名称 & 结果 & SCO & 提示 & 参考范围 & 单位 \\\\\n\\hline\n{[HBsAg]}乙肝表面抗原(酶免法) & 阴性 & 0.04 & 阴性 & s/co & & \\\\\n{[抗-HCV]}丙肝抗体(酶免法) & 阴性 & 0.15 & 阴性 & s/co & & \\\\\n{[抗-HIV]}人免疫缺陷病毒抗体(酶免法) & 阴性 & 0.06 & 阴性 & s/co & & \\\\\n{[TP-Ab]}梅毒螺旋体抗体(酶免法) & 阴性 & 0.07 & 阴性 & s/co & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
[92m11:01:52 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:01:52,249 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:01:55,997 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:01:55,997 INFO     29 [qwen-vl-table] page=50 LLM output (len=732):
{
  "report_date": "2026-01-15",
  "items": [
    {
      "name": "乙肝表面抗原(酶免法)",
      "item_code": "HBsAg",
      "value": "0.04",
      "unit": "s/co",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "丙肝抗体(酶免法)",
      "item_code": "抗-HCV",
      "value": "0.15",
      "unit": "s/co",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "人免疫缺陷病毒抗体(酶免法)",
      "item_code": "抗-HIV",
      "value": "0.06",
      "unit": "s/co",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "梅毒螺旋体抗体(酶免法)",
      "item_code": "TP-Ab",
      "value": "0.07",
      "unit": "s/co",
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-05 11:01:55,998 INFO     29 [qwen-vl-table] coord grouping: {50: 4}
2026-08-05 11:01:56,001 INFO     29 [qwen-vl-table] coord API call start, page=50, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1034944, prompt_len=556
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
乙肝表面抗原(酶免法)、丙肝抗体(酶免法)、人免疫缺陷病毒抗体(酶免法)、梅毒螺旋体抗体(酶免法)

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
2026-08-05 11:01:58,458 INFO     29 [qwen-vl-table] coord API raw response (len=224):
[
	{"text": "乙肝表面抗原(酶免法)", "bbox": [10, 373, 268, 403]},
	{"text": "丙肝抗体(酶免法)", "bbox": [10, 411, 237, 441]},
	{"text": "人免疫缺陷病毒抗体(酶免法)", "bbox": [10, 448, 324, 478]},
	{"text": "梅毒螺旋体抗体(酶免法)", "bbox": [10, 486, 282, 516]}
]
2026-08-05 11:01:58,458 INFO     29 [qwen-vl-table] coord API: raw_items=4, valid_items=4, elapsed=2.5s
2026-08-05 11:01:58,458 INFO     29 [qwen-vl-table] coord item[0]: text=乙肝表面抗原(酶免法), bbox=[10, 373, 268, 403]
2026-08-05 11:01:58,458 INFO     29 [qwen-vl-table] coord item[1]: text=丙肝抗体(酶免法), bbox=[10, 411, 237, 441]
2026-08-05 11:01:58,458 INFO     29 [qwen-vl-table] coord item[2]: text=人免疫缺陷病毒抗体(酶免法), bbox=[10, 448, 324, 478]
2026-08-05 11:01:58,458 INFO     29 [qwen-vl-table] coord item[3]: text=梅毒螺旋体抗体(酶免法), bbox=[10, 486, 282, 516]
2026-08-05 11:01:58,458 INFO     29 [qwen-vl-table] page=50 coord: matched 4/4, time=2.5s
2026-08-05 11:01:58,458 INFO     29 [qwen-vl-table] new_positions (4):
[[51, 8.42, 225.656, 221.935, 239.785], [51, 8.42, 199.554, 244.545, 262.395], [51, 8.42, 272.808, 266.56, 284.40999999999997], [51, 8.42, 237.444, 289.16999999999996, 307.02]]
2026-08-05 11:01:58,458 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=4, matched=4, pages=1, time=6.4s
2026-08-05 11:01:58,470 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-05 11:01:58,471 INFO     29 [Trace] task=39f07238 | doc=DAXI-哮喘.pdf | Extractor:LabExam | outputs={"chunks": "15 items, types={'LabReport': 15}", "html": "", "json": "2313 items", "markdown": "", "text": "", "name": "DAXI-哮喘.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "14 items, types={'OutpatientRecord': 14}", "chunks_LabExam": "15 items, types={'LabReport': 15}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 14, \"chunks_LabExam\": 15, \"chunks_Prescription\": 1}"}
2026-08-05 11:01:58,471 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-05 11:01:58,479 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 11:01:58,479 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m11:01:58 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:01:58,481 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:01:59,869 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:01:59,881 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-05 11:01:59,882 INFO     29 [Trace] task=39f07238 | doc=DAXI-哮喘.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "2313 items", "markdown": "", "text": "", "name": "DAXI-哮喘.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "14 items, types={'OutpatientRecord': 14}", "chunks_LabExam": "15 items, types={'LabReport': 15}", "chunks_Prescription": "1 items, types={'PrescriptionRecord': 1}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Admission\": 1, \"chunks_Discharge\": 1, \"chunks_Clinical\": 14, \"chunks_LabExam\": 15, \"chunks_Prescription\": 1}"}
2026-08-05 11:01:59,882 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-05 11:01:59,892 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 11:01:59,892 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 11:01:59,893 INFO     29 [qwen-vl-text] positions(23): [[16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 11:01:59,893 INFO     29 [qwen-vl-text] page grouping: [16], lines per page: [23]
2026-08-05 11:02:00,102 INFO     29 [qwen-vl-text] page=16, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 11:02:00,104 INFO     29 [qwen-vl-text] LLM extraction start, text_len=258
2026-08-05 11:02:00,104 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 11:02:00,104 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 1094, \"bbox_end\": 1116, \"encounter_dates\": [\"2023-08-14\"], \"department\": \"普通儿科三组（门）\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊号.\n姓名：\n性别：女\n年龄：39岁\n民族：汉族\n身份证\n现住址：\n就诊类型：初诊\n就诊科室：普通儿科三组（门）\n就诊日期：2023-08-14 15:29\n联系电\n主诉：咽峡炎购药\n现病史：咽峡炎购药\n既往史：平素体健，无肝炎、结核类传染病史\n过敏史：无\n体格检查：发育正常，营养良好，精神一般，口唇红润，双侧扁桃体无肿大，无充血、分泌物。咽腔黏膜无充\n血、红肿、疱疹，双肺呼吸音清，听诊心律齐，无杂音，腹平软，无压痛、反跳痛\n辅助检查：\n初步印象：急性咽峡炎\n处理意见：门诊\n备注：\n医师签名：谭真真\n第1页",
    "role": "user"
  }
]
[92m11:02:00 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:02:00,105 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:02:01,633 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:02:01,633 INFO     29 [qwen-vl-text] LLM output (len=184):
{
  "encounter_date": "2023-08-14",
  "chief_complaint": "咽峡炎购药",
  "present_illness": "咽峡炎购药",
  "past_history": "平素体健，无肝炎、结核类传染病史",
  "diagnosis": "急性咽峡炎",
  "treatment_plan": "门诊"
}
2026-08-05 11:02:01,633 INFO     29 [qwen-vl-text] Updated encounter_dates=[2023-08-14]
2026-08-05 11:02:01,634 INFO     29 [qwen-vl-text] coord API call start, page=16, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1007108, prompt_len=940
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共23行）
["门诊号.", "姓名：", "性别：女", "年龄：39岁", "民族：汉族", "身份证", "现住址：", "就诊类型：初诊", "就诊科室：普通儿科三组（门）", "就诊日期：2023-08-14 15:29", "联系电", "主诉：咽峡炎购药", "现病史：咽峡炎购药", "既往史：平素体健，无肝炎、结核类传染病史", "过敏史：无", "体格检查：发育正常，营养良好，精神一般，口唇红润，双侧扁桃体无肿大，无充血、分泌物。咽腔黏膜无充", "血、红肿、疱疹，双肺呼吸音清，听诊心律齐，无杂音，腹平软，无压痛、反跳痛", "辅助检查：", "初步印象：急性咽峡炎", "处理意见：门诊", "备注：", "医师签名：谭真真", "第1页"]

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
2026-08-05 11:02:09,403 INFO     29 [qwen-vl-text] coord API raw response (len=1273):
[
	{"text": "门诊号.", "bbox": [803, 237, 833, 250]},
	{"text": "姓名：", "bbox": [467, 303, 498, 317]},
	{"text": "性别：女", "bbox": [595, 303, 631, 317]},
	{"text": "年龄：39岁", "bbox": [673, 303, 712, 317]},
	{"text": "民族：汉族", "bbox": [768, 303, 811, 317]},
	{"text": "身份证", "bbox": [467, 329, 495, 343]},
	{"text": "现住址：", "bbox": [467, 354, 500, 368]},
	{"text": "就诊类型：初诊", "bbox": [768, 354, 823, 368]},
	{"text": "就诊科室：普通儿科三组（门）", "bbox": [467, 378, 580, 392]},
	{"text": "就诊日期：2023-08-14 15:29", "bbox": [595, 378, 708, 392]},
	{"text": "联系电", "bbox": [739, 378, 771, 392]},
	{"text": "主诉：咽峡炎购药", "bbox": [467, 403, 541, 417]},
	{"text": "现病史：咽峡炎购药", "bbox": [467, 428, 554, 442]},
	{"text": "既往史：平素体健，无肝炎、结核类传染病史", "bbox": [467, 453, 648, 467]},
	{"text": "过敏史：无", "bbox": [467, 477, 520, 491]},
	{"text": "体格检查：发育正常，营养良好，精神一般，口唇红润，双侧扁桃体无肿大，无充血、分泌物。咽腔黏膜无充", "bbox": [467, 502, 872, 516]},
	{"text": "血、红肿、疱疹，双肺呼吸音清，听诊心律齐，无杂音，腹平软，无压痛、反跳痛", "bbox": [467, 516, 762, 529]},
	{"text": "辅助检查：", "bbox": [467, 539, 511, 553]},
	{"text": "初步印象：急性咽峡炎", "bbox": [467, 564, 552, 578]},
	{"text": "处理意见：门诊", "bbox": [467, 588, 527, 602]},
	{"text": "备注：", "bbox": [467, 613, 498, 626]},
	{"text": "医师签名：谭真真", "bbox": [807, 638, 882, 655]},
	{"text": "第1页", "bbox": [664, 708, 687, 719]}
]
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] coord API: raw_items=23, valid_items=23, elapsed=7.8s
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] coord item[0]: text=门诊号., bbox=[803, 237, 833, 250]
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[467, 303, 498, 317]
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] coord item[2]: text=性别：女, bbox=[595, 303, 631, 317]
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：39岁, bbox=[673, 303, 712, 317]
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] coord item[4]: text=民族：汉族, bbox=[768, 303, 811, 317]
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] coord item[5]: text=身份证, bbox=[467, 329, 495, 343]
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] coord item[6]: text=现住址：, bbox=[467, 354, 500, 368]
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] coord item[7]: text=就诊类型：初诊, bbox=[768, 354, 823, 368]
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] coord item[8]: text=就诊科室：普通儿科三组（门）, bbox=[467, 378, 580, 392]
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] coord item[9]: text=就诊日期：2023-08-14 15:29, bbox=[595, 378, 708, 392]
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] coord item[10]: text=联系电, bbox=[739, 378, 771, 392]
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] coord item[11]: text=主诉：咽峡炎购药, bbox=[467, 403, 541, 417]
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] coord item[12]: text=现病史：咽峡炎购药, bbox=[467, 428, 554, 442]
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] coord item[13]: text=既往史：平素体健，无肝炎、结核类传染病史, bbox=[467, 453, 648, 467]
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] coord item[14]: text=过敏史：无, bbox=[467, 477, 520, 491]
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] coord item[15]: text=体格检查：发育正常，营养良好，精神一般，口唇红润，双侧扁桃体无肿大，无充血、分泌物。咽腔黏膜无充, bbox=[467, 502, 872, 516]
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] coord item[16]: text=血、红肿、疱疹，双肺呼吸音清，听诊心律齐，无杂音，腹平软，无压痛、反跳痛, bbox=[467, 516, 762, 529]
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] coord item[17]: text=辅助检查：, bbox=[467, 539, 511, 553]
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] coord item[18]: text=初步印象：急性咽峡炎, bbox=[467, 564, 552, 578]
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] coord item[19]: text=处理意见：门诊, bbox=[467, 588, 527, 602]
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] coord item[20]: text=备注：, bbox=[467, 613, 498, 626]
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] coord item[21]: text=医师签名：谭真真, bbox=[807, 638, 882, 655]
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] coord item[22]: text=第1页, bbox=[664, 708, 687, 719]
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] page=16 — 23/23 coords, api_time=7.8s
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] new_positions (23):
[[16, 676.126, 701.386, 141.015, 148.75], [16, 393.214, 419.316, 180.285, 188.61499999999998], [16, 500.99, 531.302, 180.285, 188.61499999999998], [16, 566.6659999999999, 599.504, 180.285, 188.61499999999998], [16, 646.656, 682.862, 180.285, 188.61499999999998], [16, 393.214, 416.78999999999996, 195.755, 204.08499999999998], [16, 393.214, 421.0, 210.63, 218.95999999999998], [16, 646.656, 692.966, 210.63, 218.95999999999998], [16, 393.214, 488.35999999999996, 224.91, 233.23999999999998], [16, 500.99, 596.136, 224.91, 233.23999999999998], [16, 622.2379999999999, 649.182, 224.91, 233.23999999999998], [16, 393.214, 455.522, 239.785, 248.11499999999998], [16, 393.214, 466.46799999999996, 254.66, 262.99], [16, 393.214, 545.616, 269.53499999999997, 277.865], [16, 393.214, 437.84, 283.815, 292.145], [16, 393.214, 734.2239999999999, 298.69, 307.02], [16, 393.214, 641.6039999999999, 307.02, 314.755], [16, 393.214, 430.262, 320.705, 329.03499999999997], [16, 393.214, 464.784, 335.58, 343.90999999999997], [16, 393.214, 443.734, 349.85999999999996, 358.19], [16, 393.214, 419.316, 364.73499999999996, 372.46999999999997], [16, 679.494, 742.644, 379.60999999999996, 389.72499999999997], [16, 559.088, 578.454, 421.26, 427.805]]
2026-08-05 11:02:09,404 INFO     29 [qwen-vl-text] ═══ DONE ═══ 23 positions, pages=1, time=9.5s
2026-08-05 11:02:09,405 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 11:02:09,405 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 11:02:09,405 INFO     29 [qwen-vl-text] positions(25): [[17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 11:02:09,405 INFO     29 [qwen-vl-text] page grouping: [17], lines per page: [25]
2026-08-05 11:02:09,567 INFO     29 [qwen-vl-text] page=17, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 11:02:09,569 INFO     29 [qwen-vl-text] LLM extraction start, text_len=327
2026-08-05 11:02:09,569 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 11:02:09,569 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 1117, \"bbox_end\": 1141, \"encounter_dates\": [\"2024-01-05\"], \"department\": \"妇科一病区(门)\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊病历\n门诊号：\n姓名\n性别：女\n年龄：39岁\n民族：汉族\n身份证号\n现住址：\n就诊类型：急诊\n就诊科室：妇科一病区(门)\n就诊日期：2024-01-05 10:32\n联系电话\n主诉：下腹痛2小时\n现病史：患者月经第二天，无明显诱因出现下腹持续疼痛\n既往史：平素体健，无高血压、冠心病、糖尿病病史，无肝炎、结核等传染病史，无手术史\n婚育史：\n月经史：患者平素月经规律，量中等，色正常，无痛经。\n过敏史：无\n专科检查：外阴：发育正常，阴毛呈女性分布；阴道：通畅，粘膜红润，未见异常分泌物；宫颈：光滑，大小正常，宫体：正常大小，无压痛。附件：左侧附件区压痛明显。\n辅助检查：\n初步印象：女性盆腔炎性疾病\n处理意见：门诊治疗\n备注：\n医师签名：汪会芳\n第1页",
    "role": "user"
  }
]
[92m11:02:09 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:02:09,570 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:02:09,571 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T11:02:09.570+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 11:02:12,126 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:02:12,126 INFO     29 [qwen-vl-text] LLM output (len=226):
{
  "encounter_date": "2024-01-05",
  "chief_complaint": "下腹痛2小时",
  "present_illness": "患者月经第二天，无明显诱因出现下腹持续疼痛",
  "past_history": "平素体健，无高血压、冠心病、糖尿病病史，无肝炎、结核等传染病史，无手术史",
  "diagnosis": "女性盆腔炎性疾病",
  "treatment_plan": "门诊治疗"
}
2026-08-05 11:02:12,126 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-01-05]
2026-08-05 11:02:12,128 INFO     29 [qwen-vl-text] coord API call start, page=17, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=689236, prompt_len=1015
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["门诊病历", "门诊号：", "姓名", "性别：女", "年龄：39岁", "民族：汉族", "身份证号", "现住址：", "就诊类型：急诊", "就诊科室：妇科一病区(门)", "就诊日期：2024-01-05 10:32", "联系电话", "主诉：下腹痛2小时", "现病史：患者月经第二天，无明显诱因出现下腹持续疼痛", "既往史：平素体健，无高血压、冠心病、糖尿病病史，无肝炎、结核等传染病史，无手术史", "婚育史：", "月经史：患者平素月经规律，量中等，色正常，无痛经。", "过敏史：无", "专科检查：外阴：发育正常，阴毛呈女性分布；阴道：通畅，粘膜红润，未见异常分泌物；宫颈：光滑，大小正常，宫体：正常大小，无压痛。附件：左侧附件区压痛明显。", "辅助检查：", "初步印象：女性盆腔炎性疾病", "处理意见：门诊治疗", "备注：", "医师签名：汪会芳", "第1页"]

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
2026-08-05 11:02:20,547 INFO     29 [qwen-vl-text] coord API raw response (len=1428):
[
	{"text": "门诊病历", "bbox": [625, 55, 715, 77]},
	{"text": "门诊号：", "bbox": [849, 100, 904, 118]},
	{"text": "姓名", "bbox": [368, 198, 394, 217]},
	{"text": "性别：女", "bbox": [545, 198, 595, 217]},
	{"text": "年龄：39岁", "bbox": [662, 198, 716, 217]},
	{"text": "民族：汉族", "bbox": [794, 198, 855, 217]},
	{"text": "身份证号", "bbox": [368, 235, 415, 254]},
	{"text": "现住址：", "bbox": [368, 273, 414, 292]},
	{"text": "就诊类型：急诊", "bbox": [794, 273, 874, 292]},
	{"text": "就诊科室：妇科一病区(门)", "bbox": [368, 310, 509, 329]},
	{"text": "就诊日期：2024-01-05 10:32", "bbox": [545, 310, 706, 329]},
	{"text": "联系电话", "bbox": [764, 310, 813, 329]},
	{"text": "主诉：下腹痛2小时", "bbox": [368, 348, 470, 367]},
	{"text": "现病史：患者月经第二天，无明显诱因出现下腹持续疼痛", "bbox": [368, 385, 690, 404]},
	{"text": "既往史：平素体健，无高血压、冠心病、糖尿病病史，无肝炎、结核等传染病史，无手术史", "bbox": [368, 421, 872, 440]},
	{"text": "婚育史：", "bbox": [368, 457, 431, 476]},
	{"text": "月经史：患者平素月经规律，量中等，色正常，无痛经。", "bbox": [368, 494, 683, 513]},
	{"text": "过敏史：无", "bbox": [368, 529, 445, 548]},
	{"text": "专科检查：外阴：发育正常，阴毛呈女性分布；阴道：通畅，粘膜红润，未见异常分泌物；宫颈：光滑，大小正常，宫体：正常大小，无压痛。附件：左侧附件区压痛明显。", "bbox": [368, 566, 958, 603]},
	{"text": "辅助检查：", "bbox": [368, 621, 431, 640]},
	{"text": "初步印象：女性盆腔炎性疾病", "bbox": [368, 657, 529, 676]},
	{"text": "处理意见：门诊治疗", "bbox": [368, 693, 480, 712]},
	{"text": "备注：", "bbox": [368, 728, 414, 747]},
	{"text": "医师签名：汪会芳", "bbox": [866, 769, 959, 788]},
	{"text": "第1页", "bbox": [653, 872, 686, 888]}
]
2026-08-05 11:02:20,547 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=8.4s
2026-08-05 11:02:20,547 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[625, 55, 715, 77]
2026-08-05 11:02:20,547 INFO     29 [qwen-vl-text] coord item[1]: text=门诊号：, bbox=[849, 100, 904, 118]
2026-08-05 11:02:20,547 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[368, 198, 394, 217]
2026-08-05 11:02:20,547 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女, bbox=[545, 198, 595, 217]
2026-08-05 11:02:20,547 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：39岁, bbox=[662, 198, 716, 217]
2026-08-05 11:02:20,547 INFO     29 [qwen-vl-text] coord item[5]: text=民族：汉族, bbox=[794, 198, 855, 217]
2026-08-05 11:02:20,547 INFO     29 [qwen-vl-text] coord item[6]: text=身份证号, bbox=[368, 235, 415, 254]
2026-08-05 11:02:20,547 INFO     29 [qwen-vl-text] coord item[7]: text=现住址：, bbox=[368, 273, 414, 292]
2026-08-05 11:02:20,547 INFO     29 [qwen-vl-text] coord item[8]: text=就诊类型：急诊, bbox=[794, 273, 874, 292]
2026-08-05 11:02:20,547 INFO     29 [qwen-vl-text] coord item[9]: text=就诊科室：妇科一病区(门), bbox=[368, 310, 509, 329]
2026-08-05 11:02:20,547 INFO     29 [qwen-vl-text] coord item[10]: text=就诊日期：2024-01-05 10:32, bbox=[545, 310, 706, 329]
2026-08-05 11:02:20,547 INFO     29 [qwen-vl-text] coord item[11]: text=联系电话, bbox=[764, 310, 813, 329]
2026-08-05 11:02:20,547 INFO     29 [qwen-vl-text] coord item[12]: text=主诉：下腹痛2小时, bbox=[368, 348, 470, 367]
2026-08-05 11:02:20,547 INFO     29 [qwen-vl-text] coord item[13]: text=现病史：患者月经第二天，无明显诱因出现下腹持续疼痛, bbox=[368, 385, 690, 404]
2026-08-05 11:02:20,548 INFO     29 [qwen-vl-text] coord item[14]: text=既往史：平素体健，无高血压、冠心病、糖尿病病史，无肝炎、结核等传染病史，无手术史, bbox=[368, 421, 872, 440]
2026-08-05 11:02:20,548 INFO     29 [qwen-vl-text] coord item[15]: text=婚育史：, bbox=[368, 457, 431, 476]
2026-08-05 11:02:20,548 INFO     29 [qwen-vl-text] coord item[16]: text=月经史：患者平素月经规律，量中等，色正常，无痛经。, bbox=[368, 494, 683, 513]
2026-08-05 11:02:20,548 INFO     29 [qwen-vl-text] coord item[17]: text=过敏史：无, bbox=[368, 529, 445, 548]
2026-08-05 11:02:20,548 INFO     29 [qwen-vl-text] coord item[18]: text=专科检查：外阴：发育正常，阴毛呈女性分布；阴道：通畅，粘膜红润，未见异常分泌物；宫颈：光滑，大小正常，宫体：正常大小，无压痛。附件：左侧附件区压痛明显。, bbox=[368, 566, 958, 603]
2026-08-05 11:02:20,548 INFO     29 [qwen-vl-text] coord item[19]: text=辅助检查：, bbox=[368, 621, 431, 640]
2026-08-05 11:02:20,548 INFO     29 [qwen-vl-text] coord item[20]: text=初步印象：女性盆腔炎性疾病, bbox=[368, 657, 529, 676]
2026-08-05 11:02:20,548 INFO     29 [qwen-vl-text] coord item[21]: text=处理意见：门诊治疗, bbox=[368, 693, 480, 712]
2026-08-05 11:02:20,548 INFO     29 [qwen-vl-text] coord item[22]: text=备注：, bbox=[368, 728, 414, 747]
2026-08-05 11:02:20,548 INFO     29 [qwen-vl-text] coord item[23]: text=医师签名：汪会芳, bbox=[866, 769, 959, 788]
2026-08-05 11:02:20,548 INFO     29 [qwen-vl-text] coord item[24]: text=第1页, bbox=[653, 872, 686, 888]
2026-08-05 11:02:20,548 INFO     29 [qwen-vl-text] page=17 — 25/25 coords, api_time=8.4s
2026-08-05 11:02:20,548 INFO     29 [qwen-vl-text] new_positions (25):
[[17, 526.25, 602.03, 32.725, 45.815], [17, 714.858, 761.168, 59.5, 70.21], [17, 309.856, 331.748, 117.80999999999999, 129.11499999999998], [17, 458.89, 500.99, 117.80999999999999, 129.11499999999998], [17, 557.404, 602.872, 117.80999999999999, 129.11499999999998], [17, 668.548, 719.91, 117.80999999999999, 129.11499999999998], [17, 309.856, 349.43, 139.825, 151.13], [17, 309.856, 348.58799999999997, 162.435, 173.73999999999998], [17, 668.548, 735.908, 162.435, 173.73999999999998], [17, 309.856, 428.578, 184.45, 195.755], [17, 458.89, 594.452, 184.45, 195.755], [17, 643.288, 684.5459999999999, 184.45, 195.755], [17, 309.856, 395.74, 207.06, 218.36499999999998], [17, 309.856, 580.98, 229.075, 240.38], [17, 309.856, 734.2239999999999, 250.49499999999998, 261.8], [17, 309.856, 362.902, 271.91499999999996, 283.21999999999997], [17, 309.856, 575.086, 293.93, 305.235], [17, 309.856, 374.69, 314.755, 326.06], [17, 309.856, 806.636, 336.77, 358.78499999999997], [17, 309.856, 362.902, 369.495, 380.79999999999995], [17, 309.856, 445.418, 390.91499999999996, 402.21999999999997], [17, 309.856, 404.15999999999997, 412.335, 423.64], [17, 309.856, 348.58799999999997, 433.15999999999997, 444.465], [17, 729.172, 807.478, 457.555, 468.85999999999996], [17, 549.826, 577.612, 518.84, 528.36]]
2026-08-05 11:02:20,548 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=11.1s
2026-08-05 11:02:20,548 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 11:02:20,548 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 11:02:20,549 INFO     29 [qwen-vl-text] positions(25): [[18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 11:02:20,549 INFO     29 [qwen-vl-text] page grouping: [18], lines per page: [25]
2026-08-05 11:02:20,775 INFO     29 [qwen-vl-text] page=18, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 11:02:20,777 INFO     29 [qwen-vl-text] LLM extraction start, text_len=389
2026-08-05 11:02:20,777 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 11:02:20,777 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 1167, \"bbox_end\": 1191, \"encounter_dates\": [\"2024-04-08\"], \"department\": \"妇科一病区(门)\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "检验报告\n门诊号:\n姓名\n性别: 女\n年龄:40岁\n民族: 汉族\n身份证号\n现住址:\n就诊类型:初诊\n就诊科室:妇科一病区(门)\n就诊日期: 2024-04-08 09:44\n联系电话\n主诉:月经期下腹间断疼痛2个月\n现病史:2024.1月经第3天左侧附件区疼痛,超声提示无异常,输消炎药后好转,2024.2无异常,2024.3月经第3天下腹疼痛但是疼痛程度较前减轻,\n既往史:平素体健,无高血压、冠心病、糖尿病病史,无肝炎、结核等传染病史,无手术史\n婚育史:\n月经史:患者平素月经规律,量中等,色正常,无痛经。\n过敏史:无\n专科检查:外阴:发育正常,阴毛呈女性分布;阴道:通畅,粘膜红润,未见异常分泌物;宫颈:光滑,大小正常,宫体:正常大小,无压痛。附件:双侧附件区未触及明显异常。\n辅助检查:\n初步印象:女性盆腔炎性疾病\n处理意见:门诊检查\n备注:\n医师签名:权丽丽\n第1页",
    "role": "user"
  }
]
[92m11:02:20 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:02:20,778 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:02:23,423 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:02:23,423 INFO     29 [qwen-vl-text] LLM output (len=281):
{
  "encounter_date": "2024-04-08",
  "chief_complaint": "月经期下腹间断疼痛2个月",
  "present_illness": "2024.1月经第3天左侧附件区疼痛,超声提示无异常,输消炎药后好转,2024.2无异常,2024.3月经第3天下腹疼痛但是疼痛程度较前减轻",
  "past_history": "平素体健,无高血压、冠心病、糖尿病病史,无肝炎、结核等传染病史,无手术史",
  "diagnosis": "女性盆腔炎性疾病",
  "treatment_plan": "门诊检查"
}
2026-08-05 11:02:23,423 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-04-08]
2026-08-05 11:02:23,426 INFO     29 [qwen-vl-text] coord API call start, page=18, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=982353, prompt_len=1077
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["检验报告", "门诊号:", "姓名", "性别: 女", "年龄:40岁", "民族: 汉族", "身份证号", "现住址:", "就诊类型:初诊", "就诊科室:妇科一病区(门)", "就诊日期: 2024-04-08 09:44", "联系电话", "主诉:月经期下腹间断疼痛2个月", "现病史:2024.1月经第3天左侧附件区疼痛,超声提示无异常,输消炎药后好转,2024.2无异常,2024.3月经第3天下腹疼痛但是疼痛程度较前减轻,", "既往史:平素体健,无高血压、冠心病、糖尿病病史,无肝炎、结核等传染病史,无手术史", "婚育史:", "月经史:患者平素月经规律,量中等,色正常,无痛经。", "过敏史:无", "专科检查:外阴:发育正常,阴毛呈女性分布;阴道:通畅,粘膜红润,未见异常分泌物;宫颈:光滑,大小正常,宫体:正常大小,无压痛。附件:双侧附件区未触及明显异常。", "辅助检查:", "初步印象:女性盆腔炎性疾病", "处理意见:门诊检查", "备注:", "医师签名:权丽丽", "第1页"]

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
2026-08-05 11:02:32,522 INFO     29 [qwen-vl-text] coord API raw response (len=1492):
[
	{"text": "检验报告", "bbox": [714, 170, 741, 181]},
	{"text": "门诊号:", "bbox": [783, 252, 811, 265]},
	{"text": "姓名", "bbox": [455, 316, 474, 330]},
	{"text": "性别: 女", "bbox": [575, 316, 610, 330]},
	{"text": "年龄:40岁", "bbox": [655, 316, 693, 329]},
	{"text": "民族: 汉族", "bbox": [744, 316, 786, 329]},
	{"text": "身份证号", "bbox": [455, 341, 487, 354]},
	{"text": "现住址:", "bbox": [455, 365, 487, 378]},
	{"text": "就诊类型:初诊", "bbox": [744, 365, 798, 378]},
	{"text": "就诊科室:妇科一病区(门)", "bbox": [455, 388, 551, 401]},
	{"text": "就诊日期: 2024-04-08 09:44", "bbox": [575, 388, 685, 401]},
	{"text": "联系电话", "bbox": [723, 388, 758, 401]},
	{"text": "主诉:月经期下腹间断疼痛2个月", "bbox": [455, 412, 565, 424]},
	{"text": "现病史:2024.1月经第3天左侧附件区疼痛,超声提示无异常,输消炎药后好转,2024.2无异常,2024.3月经第3天下腹疼痛但是疼痛程度较前减轻,", "bbox": [455, 435, 857, 460]},
	{"text": "既往史:平素体健,无高血压、冠心病、糖尿病病史,无肝炎、结核等传染病史,无手术史", "bbox": [455, 470, 796, 483]},
	{"text": "婚育史:", "bbox": [455, 493, 498, 505]},
	{"text": "月经史:患者平素月经规律,量中等,色正常,无痛经。", "bbox": [455, 517, 668, 529]},
	{"text": "过敏史:无", "bbox": [455, 540, 507, 552]},
	{"text": "专科检查:外阴:发育正常,阴毛呈女性分布;阴道:通畅,粘膜红润,未见异常分泌物;宫颈:光滑,大小正常,宫体:正常大小,无压痛。附件:双侧附件区未触及明显异常。", "bbox": [455, 563, 853, 588]},
	{"text": "辅助检查:", "bbox": [455, 598, 498, 610]},
	{"text": "初步印象:女性盆腔炎性疾病", "bbox": [455, 621, 563, 633]},
	{"text": "处理意见:门诊检查", "bbox": [455, 645, 530, 657]},
	{"text": "备注:", "bbox": [455, 668, 485, 680]},
	{"text": "医师签名:权丽丽", "bbox": [790, 693, 859, 708]},
	{"text": "第1页", "bbox": [647, 760, 669, 770]}
]
2026-08-05 11:02:32,522 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=9.1s
2026-08-05 11:02:32,522 INFO     29 [qwen-vl-text] coord item[0]: text=检验报告, bbox=[714, 170, 741, 181]
2026-08-05 11:02:32,522 INFO     29 [qwen-vl-text] coord item[1]: text=门诊号:, bbox=[783, 252, 811, 265]
2026-08-05 11:02:32,522 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[455, 316, 474, 330]
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] coord item[3]: text=性别: 女, bbox=[575, 316, 610, 330]
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] coord item[4]: text=年龄:40岁, bbox=[655, 316, 693, 329]
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] coord item[5]: text=民族: 汉族, bbox=[744, 316, 786, 329]
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] coord item[6]: text=身份证号, bbox=[455, 341, 487, 354]
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] coord item[7]: text=现住址:, bbox=[455, 365, 487, 378]
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] coord item[8]: text=就诊类型:初诊, bbox=[744, 365, 798, 378]
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] coord item[9]: text=就诊科室:妇科一病区(门), bbox=[455, 388, 551, 401]
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] coord item[10]: text=就诊日期: 2024-04-08 09:44, bbox=[575, 388, 685, 401]
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] coord item[11]: text=联系电话, bbox=[723, 388, 758, 401]
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] coord item[12]: text=主诉:月经期下腹间断疼痛2个月, bbox=[455, 412, 565, 424]
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] coord item[13]: text=现病史:2024.1月经第3天左侧附件区疼痛,超声提示无异常,输消炎药后好转,2024.2无异常,2024.3月经第3天下腹疼痛但是疼痛程度较前减轻,, bbox=[455, 435, 857, 460]
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] coord item[14]: text=既往史:平素体健,无高血压、冠心病、糖尿病病史,无肝炎、结核等传染病史,无手术史, bbox=[455, 470, 796, 483]
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] coord item[15]: text=婚育史:, bbox=[455, 493, 498, 505]
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] coord item[16]: text=月经史:患者平素月经规律,量中等,色正常,无痛经。, bbox=[455, 517, 668, 529]
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] coord item[17]: text=过敏史:无, bbox=[455, 540, 507, 552]
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] coord item[18]: text=专科检查:外阴:发育正常,阴毛呈女性分布;阴道:通畅,粘膜红润,未见异常分泌物;宫颈:光滑,大小正常,宫体:正常大小,无压痛。附件:双侧附件区未触及明显异常。, bbox=[455, 563, 853, 588]
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] coord item[19]: text=辅助检查:, bbox=[455, 598, 498, 610]
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] coord item[20]: text=初步印象:女性盆腔炎性疾病, bbox=[455, 621, 563, 633]
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] coord item[21]: text=处理意见:门诊检查, bbox=[455, 645, 530, 657]
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] coord item[22]: text=备注:, bbox=[455, 668, 485, 680]
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] coord item[23]: text=医师签名:权丽丽, bbox=[790, 693, 859, 708]
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] coord item[24]: text=第1页, bbox=[647, 760, 669, 770]
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] page=18 — 25/25 coords, api_time=9.1s
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] new_positions (25):
[[18, 601.188, 623.922, 101.14999999999999, 107.695], [18, 659.286, 682.862, 149.94, 157.67499999999998], [18, 383.11, 399.108, 188.01999999999998, 196.35], [18, 484.15, 513.62, 188.01999999999998, 196.35], [18, 551.51, 583.506, 188.01999999999998, 195.755], [18, 626.448, 661.812, 188.01999999999998, 195.755], [18, 383.11, 410.054, 202.89499999999998, 210.63], [18, 383.11, 410.054, 217.17499999999998, 224.91], [18, 626.448, 671.9159999999999, 217.17499999999998, 224.91], [18, 383.11, 463.942, 230.85999999999999, 238.595], [18, 484.15, 576.77, 230.85999999999999, 238.595], [18, 608.766, 638.236, 230.85999999999999, 238.595], [18, 383.11, 475.72999999999996, 245.14, 252.28], [18, 383.11, 721.5939999999999, 258.825, 273.7], [18, 383.11, 670.232, 279.65, 287.385], [18, 383.11, 419.316, 293.335, 300.47499999999997], [18, 383.11, 562.456, 307.615, 314.755], [18, 383.11, 426.894, 321.3, 328.44], [18, 383.11, 718.226, 334.98499999999996, 349.85999999999996], [18, 383.11, 419.316, 355.81, 362.95], [18, 383.11, 474.046, 369.495, 376.635], [18, 383.11, 446.26, 383.775, 390.91499999999996], [18, 383.11, 408.37, 397.46, 404.59999999999997], [18, 665.18, 723.278, 412.335, 421.26], [18, 544.774, 563.298, 452.2, 458.15]]
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=12.0s
2026-08-05 11:02:32,523 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 11:02:32,523 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 11:02:32,524 INFO     29 [qwen-vl-text] positions(26): [[19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 11:02:32,524 INFO     29 [qwen-vl-text] page grouping: [19], lines per page: [26]
2026-08-05 11:02:32,756 INFO     29 [qwen-vl-text] page=19, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 11:02:32,758 INFO     29 [qwen-vl-text] LLM extraction start, text_len=375
2026-08-05 11:02:32,758 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 11:02:32,758 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 1238, \"bbox_end\": 1263, \"encounter_dates\": [\"2024-04-08\"], \"department\": \"妇科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊号\n姓名\n性别：女\n年龄：40岁\n民族：汉族\n身份证号\n现住址：\n就诊类型：初诊\n就诊科室：妇科门诊\n就诊日期：2024-04-08 11:32\n联系电话\n主诉：月经期下腹间断疼痛2个月\n现病史：2024.1月经第3天左侧附件区疼痛，超声提示无异常，输消炎药后好转，2024.2无异常，2024.3月经\n第3天下腹疼痛但是疼痛程度较前减轻，\n既往史：平素体健，无高血压、冠心病、糖尿病病史，无肝炎、结核等传染病史，无手术史\n婚育史：\n月经史：患者平素月经规律，量中等，色正常，无痛经。\n过敏史：无\n专科检查：外阴：发育正常，阴毛呈女性分布；阴道：通畅，粘膜红润，未见异常分泌物；宫颈：光滑，大小\n正常，宫体：正常大小，无压痛。附件：双侧附件区未触及明显异常。\n辅助检查：\n初步印象：女性盆腔炎性疾病\n处理意见：门诊检查\n备注：\n医师签名：\n第1页",
    "role": "user"
  }
]
[92m11:02:32 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:02:32,759 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:02:35,373 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:02:35,373 INFO     29 [qwen-vl-text] LLM output (len=281):
{
  "encounter_date": "2024-04-08",
  "chief_complaint": "月经期下腹间断疼痛2个月",
  "present_illness": "2024.1月经第3天左侧附件区疼痛，超声提示无异常，输消炎药后好转，2024.2无异常，2024.3月经第3天下腹疼痛但是疼痛程度较前减轻",
  "past_history": "平素体健，无高血压、冠心病、糖尿病病史，无肝炎、结核等传染病史，无手术史",
  "diagnosis": "女性盆腔炎性疾病",
  "treatment_plan": "门诊检查"
}
2026-08-05 11:02:35,373 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-04-08]
2026-08-05 11:02:35,376 INFO     29 [qwen-vl-text] coord API call start, page=19, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1065280, prompt_len=1066
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["门诊号", "姓名", "性别：女", "年龄：40岁", "民族：汉族", "身份证号", "现住址：", "就诊类型：初诊", "就诊科室：妇科门诊", "就诊日期：2024-04-08 11:32", "联系电话", "主诉：月经期下腹间断疼痛2个月", "现病史：2024.1月经第3天左侧附件区疼痛，超声提示无异常，输消炎药后好转，2024.2无异常，2024.3月经", "第3天下腹疼痛但是疼痛程度较前减轻，", "既往史：平素体健，无高血压、冠心病、糖尿病病史，无肝炎、结核等传染病史，无手术史", "婚育史：", "月经史：患者平素月经规律，量中等，色正常，无痛经。", "过敏史：无", "专科检查：外阴：发育正常，阴毛呈女性分布；阴道：通畅，粘膜红润，未见异常分泌物；宫颈：光滑，大小", "正常，宫体：正常大小，无压痛。附件：双侧附件区未触及明显异常。", "辅助检查：", "初步印象：女性盆腔炎性疾病", "处理意见：门诊检查", "备注：", "医师签名：", "第1页"]

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
2026-08-05 11:02:44,306 INFO     29 [qwen-vl-text] coord API raw response (len=1522):
[
	{"text": "门诊号", "bbox": [816, 238, 844, 252]},
	{"text": "姓名", "bbox": [475, 304, 492, 318]},
	{"text": "性别：女", "bbox": [598, 304, 637, 318]},
	{"text": "年龄：40岁", "bbox": [684, 304, 723, 318]},
	{"text": "民族：汉族", "bbox": [777, 304, 821, 318]},
	{"text": "身份证号", "bbox": [475, 330, 512, 344]},
	{"text": "现住址：", "bbox": [475, 354, 508, 368]},
	{"text": "就诊类型：初诊", "bbox": [777, 354, 834, 368]},
	{"text": "就诊科室：妇科门诊", "bbox": [475, 378, 550, 392]},
	{"text": "就诊日期：2024-04-08 11:32", "bbox": [600, 378, 716, 392]},
	{"text": "联系电话", "bbox": [757, 378, 789, 392]},
	{"text": "主诉：月经期下腹间断疼痛2个月", "bbox": [475, 403, 590, 417]},
	{"text": "现病史：2024.1月经第3天左侧附件区疼痛，超声提示无异常，输消炎药后好转，2024.2无异常，2024.3月经", "bbox": [475, 428, 898, 442]},
	{"text": "第3天下腹疼痛但是疼痛程度较前减轻，", "bbox": [475, 442, 623, 456]},
	{"text": "既往史：平素体健，无高血压、冠心病、糖尿病病史，无肝炎、结核等传染病史，无手术史", "bbox": [475, 465, 834, 479]},
	{"text": "婚育史：", "bbox": [475, 489, 519, 503]},
	{"text": "月经史：患者平素月经规律，量中等，色正常，无痛经。", "bbox": [475, 513, 700, 527]},
	{"text": "过敏史：无", "bbox": [475, 537, 528, 551]},
	{"text": "专科检查：外阴：发育正常，阴毛呈女性分布；阴道：通畅，粘膜红润，未见异常分泌物；宫颈：光滑，大小", "bbox": [475, 561, 894, 575]},
	{"text": "正常，宫体：正常大小，无压痛。附件：双侧附件区未触及明显异常。", "bbox": [475, 575, 742, 589]},
	{"text": "辅助检查：", "bbox": [475, 598, 519, 612]},
	{"text": "初步印象：女性盆腔炎性疾病", "bbox": [475, 622, 590, 636]},
	{"text": "处理意见：门诊检查", "bbox": [475, 646, 554, 660]},
	{"text": "备注：", "bbox": [475, 670, 507, 684]},
	{"text": "医师签名：", "bbox": [829, 697, 901, 711]},
	{"text": "第1页", "bbox": [679, 767, 702, 778]}
]
2026-08-05 11:02:44,306 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=8.9s
2026-08-05 11:02:44,306 INFO     29 [qwen-vl-text] coord item[0]: text=门诊号, bbox=[816, 238, 844, 252]
2026-08-05 11:02:44,306 INFO     29 [qwen-vl-text] coord item[1]: text=姓名, bbox=[475, 304, 492, 318]
2026-08-05 11:02:44,306 INFO     29 [qwen-vl-text] coord item[2]: text=性别：女, bbox=[598, 304, 637, 318]
2026-08-05 11:02:44,306 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：40岁, bbox=[684, 304, 723, 318]
2026-08-05 11:02:44,306 INFO     29 [qwen-vl-text] coord item[4]: text=民族：汉族, bbox=[777, 304, 821, 318]
2026-08-05 11:02:44,306 INFO     29 [qwen-vl-text] coord item[5]: text=身份证号, bbox=[475, 330, 512, 344]
2026-08-05 11:02:44,306 INFO     29 [qwen-vl-text] coord item[6]: text=现住址：, bbox=[475, 354, 508, 368]
2026-08-05 11:02:44,306 INFO     29 [qwen-vl-text] coord item[7]: text=就诊类型：初诊, bbox=[777, 354, 834, 368]
2026-08-05 11:02:44,306 INFO     29 [qwen-vl-text] coord item[8]: text=就诊科室：妇科门诊, bbox=[475, 378, 550, 392]
2026-08-05 11:02:44,306 INFO     29 [qwen-vl-text] coord item[9]: text=就诊日期：2024-04-08 11:32, bbox=[600, 378, 716, 392]
2026-08-05 11:02:44,306 INFO     29 [qwen-vl-text] coord item[10]: text=联系电话, bbox=[757, 378, 789, 392]
2026-08-05 11:02:44,306 INFO     29 [qwen-vl-text] coord item[11]: text=主诉：月经期下腹间断疼痛2个月, bbox=[475, 403, 590, 417]
2026-08-05 11:02:44,306 INFO     29 [qwen-vl-text] coord item[12]: text=现病史：2024.1月经第3天左侧附件区疼痛，超声提示无异常，输消炎药后好转，2024.2无异常，2024.3月经, bbox=[475, 428, 898, 442]
2026-08-05 11:02:44,306 INFO     29 [qwen-vl-text] coord item[13]: text=第3天下腹疼痛但是疼痛程度较前减轻，, bbox=[475, 442, 623, 456]
2026-08-05 11:02:44,306 INFO     29 [qwen-vl-text] coord item[14]: text=既往史：平素体健，无高血压、冠心病、糖尿病病史，无肝炎、结核等传染病史，无手术史, bbox=[475, 465, 834, 479]
2026-08-05 11:02:44,306 INFO     29 [qwen-vl-text] coord item[15]: text=婚育史：, bbox=[475, 489, 519, 503]
2026-08-05 11:02:44,306 INFO     29 [qwen-vl-text] coord item[16]: text=月经史：患者平素月经规律，量中等，色正常，无痛经。, bbox=[475, 513, 700, 527]
2026-08-05 11:02:44,306 INFO     29 [qwen-vl-text] coord item[17]: text=过敏史：无, bbox=[475, 537, 528, 551]
2026-08-05 11:02:44,306 INFO     29 [qwen-vl-text] coord item[18]: text=专科检查：外阴：发育正常，阴毛呈女性分布；阴道：通畅，粘膜红润，未见异常分泌物；宫颈：光滑，大小, bbox=[475, 561, 894, 575]
2026-08-05 11:02:44,306 INFO     29 [qwen-vl-text] coord item[19]: text=正常，宫体：正常大小，无压痛。附件：双侧附件区未触及明显异常。, bbox=[475, 575, 742, 589]
2026-08-05 11:02:44,307 INFO     29 [qwen-vl-text] coord item[20]: text=辅助检查：, bbox=[475, 598, 519, 612]
2026-08-05 11:02:44,307 INFO     29 [qwen-vl-text] coord item[21]: text=初步印象：女性盆腔炎性疾病, bbox=[475, 622, 590, 636]
2026-08-05 11:02:44,307 INFO     29 [qwen-vl-text] coord item[22]: text=处理意见：门诊检查, bbox=[475, 646, 554, 660]
2026-08-05 11:02:44,307 INFO     29 [qwen-vl-text] coord item[23]: text=备注：, bbox=[475, 670, 507, 684]
2026-08-05 11:02:44,307 INFO     29 [qwen-vl-text] coord item[24]: text=医师签名：, bbox=[829, 697, 901, 711]
2026-08-05 11:02:44,307 INFO     29 [qwen-vl-text] coord item[25]: text=第1页, bbox=[679, 767, 702, 778]
2026-08-05 11:02:44,307 INFO     29 [qwen-vl-text] page=19 — 26/26 coords, api_time=8.9s
2026-08-05 11:02:44,307 INFO     29 [qwen-vl-text] new_positions (26):
[[19, 687.072, 710.648, 141.60999999999999, 149.94], [19, 399.95, 414.264, 180.88, 189.20999999999998], [19, 503.51599999999996, 536.3539999999999, 180.88, 189.20999999999998], [19, 575.928, 608.766, 180.88, 189.20999999999998], [19, 654.2339999999999, 691.2819999999999, 180.88, 189.20999999999998], [19, 399.95, 431.104, 196.35, 204.67999999999998], [19, 399.95, 427.736, 210.63, 218.95999999999998], [19, 654.2339999999999, 702.228, 210.63, 218.95999999999998], [19, 399.95, 463.09999999999997, 224.91, 233.23999999999998], [19, 505.2, 602.872, 224.91, 233.23999999999998], [19, 637.394, 664.338, 224.91, 233.23999999999998], [19, 399.95, 496.78, 239.785, 248.11499999999998], [19, 399.95, 756.116, 254.66, 262.99], [19, 399.95, 524.566, 262.99, 271.32], [19, 399.95, 702.228, 276.675, 285.005], [19, 399.95, 436.998, 290.955, 299.28499999999997], [19, 399.95, 589.4, 305.235, 313.565], [19, 399.95, 444.57599999999996, 319.515, 327.84499999999997], [19, 399.95, 752.7479999999999, 333.79499999999996, 342.125], [19, 399.95, 624.764, 342.125, 350.455], [19, 399.95, 436.998, 355.81, 364.14], [19, 399.95, 496.78, 370.09, 378.41999999999996], [19, 399.95, 466.46799999999996, 384.37, 392.7], [19, 399.95, 426.894, 398.65, 406.97999999999996], [19, 698.018, 758.6419999999999, 414.715, 423.04499999999996], [19, 571.718, 591.084, 456.36499999999995, 462.90999999999997]]
2026-08-05 11:02:44,307 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=11.8s
2026-08-05 11:02:44,307 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 11:02:44,307 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 11:02:44,307 INFO     29 [qwen-vl-text] positions(22): [[20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0], [20, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 11:02:44,308 INFO     29 [qwen-vl-text] page grouping: [20], lines per page: [22]
2026-08-05 11:02:44,510 INFO     29 [qwen-vl-text] page=20, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 11:02:44,512 INFO     29 [qwen-vl-text] LLM extraction start, text_len=234
2026-08-05 11:02:44,512 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 11:02:44,512 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 1314, \"bbox_end\": 1335, \"encounter_dates\": [\"2024-04-19\"], \"department\": \"普通儿科一组(门)\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊号\n姓\n性别：女\n年龄：40岁\n民族：汉族\n身份证号：\n现住址：\n就诊类型：急诊\n就诊科室：普通儿科一组(门)\n就诊日期：2024-04-19 08:07\n联系电话\n主诉：因呼吸道感染）不适要求开药\n现病史：患者因（呼吸道感染）不适，要求开药（家属代开）。\n既往史：既往体质一般\n过敏史：无\n体格检查：神志清晰，精神一般，自主体位，查体合作\n辅助检查：\n初步印象：1、急性上呼吸道感染.2、维生素A缺乏伴夜盲症\n处理意见：开立药品\n备注：\n医师签名：李婉莹\n第1页",
    "role": "user"
  }
]
[92m11:02:44 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:02:44,513 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:02:44,514 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T11:02:44.513+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 11:02:46,771 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:02:46,771 INFO     29 [qwen-vl-text] LLM output (len=221):
{
  "encounter_date": "2024-04-19",
  "chief_complaint": "因呼吸道感染）不适要求开药",
  "present_illness": "患者因（呼吸道感染）不适，要求开药（家属代开）。",
  "past_history": "既往体质一般",
  "diagnosis": "1、急性上呼吸道感染.2、维生素A缺乏伴夜盲症",
  "treatment_plan": "开立药品"
}
2026-08-05 11:02:46,771 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-04-19]
2026-08-05 11:02:46,772 INFO     29 [qwen-vl-text] coord API call start, page=20, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=871631, prompt_len=913
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["门诊号", "姓", "性别：女", "年龄：40岁", "民族：汉族", "身份证号：", "现住址：", "就诊类型：急诊", "就诊科室：普通儿科一组(门)", "就诊日期：2024-04-19 08:07", "联系电话", "主诉：因呼吸道感染）不适要求开药", "现病史：患者因（呼吸道感染）不适，要求开药（家属代开）。", "既往史：既往体质一般", "过敏史：无", "体格检查：神志清晰，精神一般，自主体位，查体合作", "辅助检查：", "初步印象：1、急性上呼吸道感染.2、维生素A缺乏伴夜盲症", "处理意见：开立药品", "备注：", "医师签名：李婉莹", "第1页"]

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
2026-08-05 11:02:54,058 INFO     29 [qwen-vl-text] coord API raw response (len=1217):
```json
[
	{"text": "门诊号", "bbox": [812, 240, 839, 253]},
	{"text": "姓", "bbox": [472, 308, 484, 323]},
	{"text": "性别：女", "bbox": [602, 308, 638, 323]},
	{"text": "年龄：40岁", "bbox": [680, 308, 719, 323]},
	{"text": "民族：汉族", "bbox": [777, 308, 820, 323]},
	{"text": "身份证号：", "bbox": [472, 334, 513, 349]},
	{"text": "现住址：", "bbox": [472, 360, 504, 374]},
	{"text": "就诊类型：急诊", "bbox": [777, 360, 833, 374]},
	{"text": "就诊科室：普通儿科一组(门)", "bbox": [472, 385, 585, 400]},
	{"text": "就诊日期：2024-04-19 08:07", "bbox": [601, 385, 715, 400]},
	{"text": "联系电话", "bbox": [747, 385, 785, 400]},
	{"text": "主诉：因呼吸道感染）不适要求开药", "bbox": [472, 410, 624, 425]},
	{"text": "现病史：患者因（呼吸道感染）不适，要求开药（家属代开）。", "bbox": [472, 436, 725, 451]},
	{"text": "既往史：既往体质一般", "bbox": [472, 461, 567, 476]},
	{"text": "过敏史：无", "bbox": [472, 486, 525, 501]},
	{"text": "体格检查：神志清晰，精神一般，自主体位，查体合作", "bbox": [472, 511, 680, 526]},
	{"text": "辅助检查：", "bbox": [472, 536, 515, 551]},
	{"text": "初步印象：1、急性上呼吸道感染.2、维生素A缺乏伴夜盲症", "bbox": [472, 562, 698, 576]},
	{"text": "处理意见：开立药品", "bbox": [472, 587, 549, 601]},
	{"text": "备注：", "bbox": [472, 612, 502, 626]},
	{"text": "医师签名：李婉莹", "bbox": [818, 640, 889, 654]},
	{"text": "第1页", "bbox": [672, 709, 695, 720]}
]
```
2026-08-05 11:02:54,058 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=7.3s
2026-08-05 11:02:54,058 INFO     29 [qwen-vl-text] coord item[0]: text=门诊号, bbox=[812, 240, 839, 253]
2026-08-05 11:02:54,058 INFO     29 [qwen-vl-text] coord item[1]: text=姓, bbox=[472, 308, 484, 323]
2026-08-05 11:02:54,058 INFO     29 [qwen-vl-text] coord item[2]: text=性别：女, bbox=[602, 308, 638, 323]
2026-08-05 11:02:54,058 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：40岁, bbox=[680, 308, 719, 323]
2026-08-05 11:02:54,058 INFO     29 [qwen-vl-text] coord item[4]: text=民族：汉族, bbox=[777, 308, 820, 323]
2026-08-05 11:02:54,058 INFO     29 [qwen-vl-text] coord item[5]: text=身份证号：, bbox=[472, 334, 513, 349]
2026-08-05 11:02:54,058 INFO     29 [qwen-vl-text] coord item[6]: text=现住址：, bbox=[472, 360, 504, 374]
2026-08-05 11:02:54,058 INFO     29 [qwen-vl-text] coord item[7]: text=就诊类型：急诊, bbox=[777, 360, 833, 374]
2026-08-05 11:02:54,058 INFO     29 [qwen-vl-text] coord item[8]: text=就诊科室：普通儿科一组(门), bbox=[472, 385, 585, 400]
2026-08-05 11:02:54,058 INFO     29 [qwen-vl-text] coord item[9]: text=就诊日期：2024-04-19 08:07, bbox=[601, 385, 715, 400]
2026-08-05 11:02:54,059 INFO     29 [qwen-vl-text] coord item[10]: text=联系电话, bbox=[747, 385, 785, 400]
2026-08-05 11:02:54,059 INFO     29 [qwen-vl-text] coord item[11]: text=主诉：因呼吸道感染）不适要求开药, bbox=[472, 410, 624, 425]
2026-08-05 11:02:54,059 INFO     29 [qwen-vl-text] coord item[12]: text=现病史：患者因（呼吸道感染）不适，要求开药（家属代开）。, bbox=[472, 436, 725, 451]
2026-08-05 11:02:54,059 INFO     29 [qwen-vl-text] coord item[13]: text=既往史：既往体质一般, bbox=[472, 461, 567, 476]
2026-08-05 11:02:54,059 INFO     29 [qwen-vl-text] coord item[14]: text=过敏史：无, bbox=[472, 486, 525, 501]
2026-08-05 11:02:54,059 INFO     29 [qwen-vl-text] coord item[15]: text=体格检查：神志清晰，精神一般，自主体位，查体合作, bbox=[472, 511, 680, 526]
2026-08-05 11:02:54,059 INFO     29 [qwen-vl-text] coord item[16]: text=辅助检查：, bbox=[472, 536, 515, 551]
2026-08-05 11:02:54,059 INFO     29 [qwen-vl-text] coord item[17]: text=初步印象：1、急性上呼吸道感染.2、维生素A缺乏伴夜盲症, bbox=[472, 562, 698, 576]
2026-08-05 11:02:54,059 INFO     29 [qwen-vl-text] coord item[18]: text=处理意见：开立药品, bbox=[472, 587, 549, 601]
2026-08-05 11:02:54,059 INFO     29 [qwen-vl-text] coord item[19]: text=备注：, bbox=[472, 612, 502, 626]
2026-08-05 11:02:54,059 INFO     29 [qwen-vl-text] coord item[20]: text=医师签名：李婉莹, bbox=[818, 640, 889, 654]
2026-08-05 11:02:54,059 INFO     29 [qwen-vl-text] coord item[21]: text=第1页, bbox=[672, 709, 695, 720]
2026-08-05 11:02:54,059 INFO     29 [qwen-vl-text] page=20 — 22/22 coords, api_time=7.3s
2026-08-05 11:02:54,059 INFO     29 [qwen-vl-text] new_positions (22):
[[20, 683.704, 706.438, 142.79999999999998, 150.535], [20, 397.424, 407.52799999999996, 183.26, 192.185], [20, 506.88399999999996, 537.196, 183.26, 192.185], [20, 572.56, 605.398, 183.26, 192.185], [20, 654.2339999999999, 690.4399999999999, 183.26, 192.185], [20, 397.424, 431.94599999999997, 198.73, 207.655], [20, 397.424, 424.368, 214.2, 222.53], [20, 654.2339999999999, 701.386, 214.2, 222.53], [20, 397.424, 492.57, 229.075, 238.0], [20, 506.042, 602.03, 229.075, 238.0], [20, 628.9739999999999, 660.97, 229.075, 238.0], [20, 397.424, 525.408, 243.95, 252.875], [20, 397.424, 610.4499999999999, 259.42, 268.34499999999997], [20, 397.424, 477.414, 274.295, 283.21999999999997], [20, 397.424, 442.05, 289.16999999999996, 298.09499999999997], [20, 397.424, 572.56, 304.04499999999996, 312.96999999999997], [20, 397.424, 433.63, 318.91999999999996, 327.84499999999997], [20, 397.424, 587.716, 334.39, 342.71999999999997], [20, 397.424, 462.258, 349.265, 357.59499999999997], [20, 397.424, 422.68399999999997, 364.14, 372.46999999999997], [20, 688.756, 748.538, 380.79999999999995, 389.13], [20, 565.824, 585.1899999999999, 421.85499999999996, 428.4]]
2026-08-05 11:02:54,059 INFO     29 [qwen-vl-text] ═══ DONE ═══ 22 positions, pages=1, time=9.8s
2026-08-05 11:02:54,059 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 11:02:54,059 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 11:02:54,059 INFO     29 [qwen-vl-text] positions(27): [[21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 11:02:54,059 INFO     29 [qwen-vl-text] page grouping: [21], lines per page: [27]
2026-08-05 11:02:54,277 INFO     29 [qwen-vl-text] page=21, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 11:02:54,279 INFO     29 [qwen-vl-text] LLM extraction start, text_len=337
2026-08-05 11:02:54,279 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 11:02:54,279 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 1384, \"bbox_end\": 1410, \"encounter_dates\": [\"2025-04-11\"], \"department\": \"呼吸危重二病区(门)\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "（总）诊病历\n门诊号：\n姓\n性别：女\n年龄：41岁\n民族：汉族\n婚姻状况：已婚\n身份证\n职业：专业技术人员\n现住址：\n就诊类型：初诊\n就诊科室：呼吸危重二病区(门)\n就诊日期：2025-04-11\n14:47\n联系电话：\n主诉：咳嗽憋气一周\n现病史：患者无发热，感冒后咳嗽、憋气一周，间断治疗，时轻时重，今日来诊\n既往史：平素体健，无高血压、冠心病、糖尿病病史\n个人史：无吸烟史\n过敏史：无\n体格检查：呼吸平稳，口唇无紫绀，听诊：双肺呼吸音清，未闻及干、湿性啰音\n辅助检查：肺功能检查提示中重度阻塞性肺通气功能障碍，支气管舒张试验阳性。\n初步印象：1、支气管哮喘(急性发作期).2、过敏性鼻炎[变应性鼻炎]\n处理意见：坚持门诊治疗，定期复查\n备注：\n医师签名：段竹云\n第1页",
    "role": "user"
  }
]
[92m11:02:54 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:02:54,281 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:02:57,108 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:02:57,109 INFO     29 [qwen-vl-text] LLM output (len=247):
{
  "encounter_date": "2025-04-11",
  "chief_complaint": "咳嗽憋气一周",
  "present_illness": "患者无发热，感冒后咳嗽、憋气一周，间断治疗，时轻时重，今日来诊",
  "past_history": "平素体健，无高血压、冠心病、糖尿病病史",
  "diagnosis": "1、支气管哮喘(急性发作期).2、过敏性鼻炎[变应性鼻炎]",
  "treatment_plan": "坚持门诊治疗，定期复查"
}
2026-08-05 11:02:57,109 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-04-11]
2026-08-05 11:02:57,111 INFO     29 [qwen-vl-text] coord API call start, page=21, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1054029, prompt_len=1031
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共27行）
["（总）诊病历", "门诊号：", "姓", "性别：女", "年龄：41岁", "民族：汉族", "婚姻状况：已婚", "身份证", "职业：专业技术人员", "现住址：", "就诊类型：初诊", "就诊科室：呼吸危重二病区(门)", "就诊日期：2025-04-11", "14:47", "联系电话：", "主诉：咳嗽憋气一周", "现病史：患者无发热，感冒后咳嗽、憋气一周，间断治疗，时轻时重，今日来诊", "既往史：平素体健，无高血压、冠心病、糖尿病病史", "个人史：无吸烟史", "过敏史：无", "体格检查：呼吸平稳，口唇无紫绀，听诊：双肺呼吸音清，未闻及干、湿性啰音", "辅助检查：肺功能检查提示中重度阻塞性肺通气功能障碍，支气管舒张试验阳性。", "初步印象：1、支气管哮喘(急性发作期).2、过敏性鼻炎[变应性鼻炎]", "处理意见：坚持门诊治疗，定期复查", "备注：", "医师签名：段竹云", "第1页"]

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
2026-08-05 11:03:08,806 INFO     29 [qwen-vl-text] coord API raw response (len=2170):
[
	{"text": "（总）诊病历", "bbox": [681, 216, 771, 234]},
	{"text": "门诊号：", "bbox": [853, 247, 885, 262], "label": "门诊号"},
	{"text": "姓", "bbox": [498, 318, 509, 334], "label": "姓"},
	{"text": "性别：女", "bbox": [602, 318, 640, 334], "label": "性别：女"},
	{"text": "年龄：41岁", "bbox": [664, 318, 706, 334], "label": "年龄：41岁"},
	{"text": "民族：汉族", "bbox": [734, 318, 782, 334], "label": "民族：汉族"},
	{"text": "婚姻状况：已婚", "bbox": [498, 345, 562, 360], "label": "婚姻状况：已婚"},
	{"text": "身份证", "bbox": [602, 345, 630, 360], "label": "身份证"},
	{"text": "职业：专业技术人员", "bbox": [738, 345, 817, 360], "label": "职业：专业技术人员"},
	{"text": "现住址：", "bbox": [498, 371, 531, 386], "label": "现住址："},
	{"text": "就诊类型：初诊", "bbox": [735, 371, 795, 386], "label": "就诊类型：初诊"},
	{"text": "就诊科室：呼吸危重二病区(门)", "bbox": [498, 397, 594, 425], "label": "就诊科室：呼吸危重二病区(门)"},
	{"text": "就诊日期：2025-04-11", "bbox": [602, 397, 695, 411], "label": "就诊日期：2025-04-11"},
	{"text": "14:47", "bbox": [602, 411, 625, 424], "label": "14:47"},
	{"text": "联系电话：", "bbox": [718, 404, 760, 418], "label": "联系电话："},
	{"text": "主诉：咳嗽憋气一周", "bbox": [498, 437, 585, 452], "label": "主诉：咳嗽憋气一周"},
	{"text": "现病史：患者无发热，感冒后咳嗽、憋气一周，间断治疗，时轻时重，今日来诊", "bbox": [498, 464, 825, 479], "label": "现病史：患者无发热，感冒后咳嗽、憋气一周，间断治疗，时轻时重，今日来诊"},
	{"text": "既往史：平素体健，无高血压、冠心病、糖尿病病史", "bbox": [498, 490, 717, 504], "label": "既往史：平素体健，无高血压、冠心病、糖尿病病史"},
	{"text": "个人史：无吸烟史", "bbox": [498, 515, 584, 529], "label": "个人史：无吸烟史"},
	{"text": "过敏史：无", "bbox": [498, 541, 554, 555], "label": "过敏史：无"},
	{"text": "体格检查：呼吸平稳，口唇无紫绀，听诊：双肺呼吸音清，未闻及干、湿性啰音", "bbox": [498, 567, 815, 581], "label": "体格检查：呼吸平稳，口唇无紫绀，听诊：双肺呼吸音清，未闻及干、湿性啰音"},
	{"text": "辅助检查：肺功能检查提示中重度阻塞性肺通气功能障碍，支气管舒张试验阳性。", "bbox": [498, 593, 820, 607], "label": "辅助检查：肺功能检查提示中重度阻塞性肺通气功能障碍，支气管舒张试验阳性。"},
	{"text": "初步印象：1、支气管哮喘(急性发作期).2、过敏性鼻炎[变应性鼻炎]", "bbox": [498, 618, 775, 633], "label": "初步印象：1、支气管哮喘(急性发作期).2、过敏性鼻炎[变应性鼻炎]"},
	{"text": "处理意见：坚持门诊治疗，定期复查", "bbox": [498, 644, 644, 658], "label": "处理意见：坚持门诊治疗，定期复查"},
	{"text": "备注：", "bbox": [498, 670, 530, 684], "label": "备注："},
	{"text": "医师签名：段竹云", "bbox": [753, 699, 832, 713], "label": "医师签名：段竹云"},
	{"text": "第1页", "bbox": [709, 774, 733, 785], "label": "第1页"}
]
2026-08-05 11:03:08,806 INFO     29 [qwen-vl-text] coord API: raw_items=27, valid_items=27, elapsed=11.7s
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[0]: text=（总）诊病历, bbox=[681, 216, 771, 234]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[1]: text=门诊号：, bbox=[853, 247, 885, 262]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[2]: text=姓, bbox=[498, 318, 509, 334]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女, bbox=[602, 318, 640, 334]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：41岁, bbox=[664, 318, 706, 334]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[5]: text=民族：汉族, bbox=[734, 318, 782, 334]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[6]: text=婚姻状况：已婚, bbox=[498, 345, 562, 360]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[7]: text=身份证, bbox=[602, 345, 630, 360]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[8]: text=职业：专业技术人员, bbox=[738, 345, 817, 360]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[9]: text=现住址：, bbox=[498, 371, 531, 386]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[10]: text=就诊类型：初诊, bbox=[735, 371, 795, 386]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[11]: text=就诊科室：呼吸危重二病区(门), bbox=[498, 397, 594, 425]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[12]: text=就诊日期：2025-04-11, bbox=[602, 397, 695, 411]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[13]: text=14:47, bbox=[602, 411, 625, 424]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[14]: text=联系电话：, bbox=[718, 404, 760, 418]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[15]: text=主诉：咳嗽憋气一周, bbox=[498, 437, 585, 452]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[16]: text=现病史：患者无发热，感冒后咳嗽、憋气一周，间断治疗，时轻时重，今日来诊, bbox=[498, 464, 825, 479]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[17]: text=既往史：平素体健，无高血压、冠心病、糖尿病病史, bbox=[498, 490, 717, 504]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[18]: text=个人史：无吸烟史, bbox=[498, 515, 584, 529]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[19]: text=过敏史：无, bbox=[498, 541, 554, 555]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[20]: text=体格检查：呼吸平稳，口唇无紫绀，听诊：双肺呼吸音清，未闻及干、湿性啰音, bbox=[498, 567, 815, 581]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[21]: text=辅助检查：肺功能检查提示中重度阻塞性肺通气功能障碍，支气管舒张试验阳性。, bbox=[498, 593, 820, 607]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[22]: text=初步印象：1、支气管哮喘(急性发作期).2、过敏性鼻炎[变应性鼻炎], bbox=[498, 618, 775, 633]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[23]: text=处理意见：坚持门诊治疗，定期复查, bbox=[498, 644, 644, 658]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[24]: text=备注：, bbox=[498, 670, 530, 684]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[25]: text=医师签名：段竹云, bbox=[753, 699, 832, 713]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] coord item[26]: text=第1页, bbox=[709, 774, 733, 785]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] page=21 — 27/27 coords, api_time=11.7s
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] new_positions (27):
[[21, 573.4019999999999, 649.182, 128.51999999999998, 139.23], [21, 718.226, 745.17, 146.965, 155.89], [21, 419.316, 428.578, 189.20999999999998, 198.73], [21, 506.88399999999996, 538.88, 189.20999999999998, 198.73], [21, 559.088, 594.452, 189.20999999999998, 198.73], [21, 618.028, 658.444, 189.20999999999998, 198.73], [21, 419.316, 473.204, 205.27499999999998, 214.2], [21, 506.88399999999996, 530.46, 205.27499999999998, 214.2], [21, 621.396, 687.914, 205.27499999999998, 214.2], [21, 419.316, 447.102, 220.74499999999998, 229.67], [21, 618.87, 669.39, 220.74499999999998, 229.67], [21, 419.316, 500.14799999999997, 236.215, 252.875], [21, 506.88399999999996, 585.1899999999999, 236.215, 244.545], [21, 506.88399999999996, 526.25, 244.545, 252.28], [21, 604.5559999999999, 639.92, 240.38, 248.70999999999998], [21, 419.316, 492.57, 260.015, 268.94], [21, 419.316, 694.65, 276.08, 285.005], [21, 419.316, 603.7139999999999, 291.55, 299.88], [21, 419.316, 491.728, 306.425, 314.755], [21, 419.316, 466.46799999999996, 321.895, 330.22499999999997], [21, 419.316, 686.23, 337.365, 345.695], [21, 419.316, 690.4399999999999, 352.835, 361.16499999999996], [21, 419.316, 652.55, 367.71, 376.635], [21, 419.316, 542.2479999999999, 383.18, 391.51], [21, 419.316, 446.26, 398.65, 406.97999999999996], [21, 634.026, 700.544, 415.905, 424.23499999999996], [21, 596.978, 617.1859999999999, 460.53, 467.075]]
2026-08-05 11:03:08,807 INFO     29 [qwen-vl-text] ═══ DONE ═══ 27 positions, pages=1, time=14.7s
2026-08-05 11:03:08,808 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 11:03:08,808 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 11:03:08,808 INFO     29 [qwen-vl-text] positions(26): [[22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 11:03:08,808 INFO     29 [qwen-vl-text] page grouping: [22], lines per page: [26]
2026-08-05 11:03:09,011 INFO     29 [qwen-vl-text] page=22, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 11:03:09,013 INFO     29 [qwen-vl-text] LLM extraction start, text_len=336
2026-08-05 11:03:09,013 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 11:03:09,014 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 1431, \"bbox_end\": 1456, \"encounter_dates\": [\"2025-04-11\"], \"department\": \"耳鼻咽喉头颈外科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊病历\n门诊号\n姓名\n性别: 女\n年龄:41岁\n民族: 汉族\n婚姻状况: 已婚\n身份证号\n职业: 职员\n现住址:\n就诊类型: 初诊\n就诊科室:耳鼻咽喉头颈外科\n就诊日期: 2025-04-11 15:43\n联系电\n主诉:鼻塞流涕,咳嗽憋气1周\n现病史:1周前发现鼻塞流涕,患者无发热,感冒后咳嗽、憋气,间断治疗,时轻时重,今日来诊\n既往史:平素体健,无高血压、冠心病、糖尿病病史\n家族史:无家族遗传病史\n过敏史:无\n体格检查:鼻腔粘膜充血,水肿,水样分泌物附着\n辅助检查:肺功能检查提示中重度阻塞性肺通气功能障碍,支气管舒张试验阳性。\n初步印象:1、支气管哮喘(急性发作期)2、过敏性鼻炎[变应性鼻炎]\n处理意见:坚持门诊治疗,定期复查\n备注:\n医师签名:刘秀层\n第1页",
    "role": "user"
  }
]
[92m11:03:09 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:03:09,015 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:03:12,002 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:03:12,002 INFO     29 [qwen-vl-text] LLM output (len=259):
{
  "encounter_date": "2025-04-11",
  "chief_complaint": "鼻塞流涕,咳嗽憋气1周",
  "present_illness": "1周前发现鼻塞流涕,患者无发热,感冒后咳嗽、憋气,间断治疗,时轻时重,今日来诊",
  "past_history": "平素体健,无高血压、冠心病、糖尿病病史",
  "diagnosis": "1、支气管哮喘(急性发作期)2、过敏性鼻炎[变应性鼻炎]",
  "treatment_plan": "坚持门诊治疗,定期复查"
}
2026-08-05 11:03:12,003 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-04-11]
2026-08-05 11:03:12,004 INFO     29 [qwen-vl-text] coord API call start, page=22, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1006276, prompt_len=1027
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["门诊病历", "门诊号", "姓名", "性别: 女", "年龄:41岁", "民族: 汉族", "婚姻状况: 已婚", "身份证号", "职业: 职员", "现住址:", "就诊类型: 初诊", "就诊科室:耳鼻咽喉头颈外科", "就诊日期: 2025-04-11 15:43", "联系电", "主诉:鼻塞流涕,咳嗽憋气1周", "现病史:1周前发现鼻塞流涕,患者无发热,感冒后咳嗽、憋气,间断治疗,时轻时重,今日来诊", "既往史:平素体健,无高血压、冠心病、糖尿病病史", "家族史:无家族遗传病史", "过敏史:无", "体格检查:鼻腔粘膜充血,水肿,水样分泌物附着", "辅助检查:肺功能检查提示中重度阻塞性肺通气功能障碍,支气管舒张试验阳性。", "初步印象:1、支气管哮喘(急性发作期)2、过敏性鼻炎[变应性鼻炎]", "处理意见:坚持门诊治疗,定期复查", "备注:", "医师签名:刘秀层", "第1页"]

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
2026-08-05 11:03:25,122 INFO     29 [qwen-vl-text] coord API raw response (len=2233):
[
	{"text": "门诊病历", "bbox": [644, 222, 737, 238]},
	{"text": "门诊号", "bbox": [816, 250, 841, 263], "bbox": [816, 250, 841, 263]},
	{"text": "姓名", "bbox": [476, 315, 495, 329], "bbox": [476, 315, 495, 329]},
	{"text": "性别: 女", "bbox": [606, 315, 643, 329], "bbox": [606, 315, 643, 329]},
	{"text": "年龄:41岁", "bbox": [684, 315, 723, 329], "bbox": [684, 315, 723, 329]},
	{"text": "民族: 汉族", "bbox": [772, 315, 816, 329], "bbox": [772, 315, 816, 329]},
	{"text": "婚姻状况: 已婚", "bbox": [476, 339, 538, 353], "bbox": [476, 339, 538, 353]},
	{"text": "身份证号", "bbox": [606, 339, 643, 353], "bbox": [606, 339, 643, 353]},
	{"text": "职业: 职员", "bbox": [772, 339, 816, 353], "bbox": [772, 339, 816, 353]},
	{"text": "现住址:", "bbox": [476, 364, 508, 377], "bbox": [476, 364, 508, 377]},
	{"text": "就诊类型: 初诊", "bbox": [772, 364, 833, 377], "bbox": [772, 364, 833, 377]},
	{"text": "就诊科室:耳鼻咽喉头颈外科", "bbox": [476, 387, 585, 401], "bbox": [476, 387, 585, 401]},
	{"text": "就诊日期: 2025-04-11 15:43", "bbox": [606, 393, 720, 406], "bbox": [606, 393, 720, 406]},
	{"text": "联系电", "bbox": [751, 393, 779, 406], "bbox": [751, 393, 779, 406]},
	{"text": "主诉:鼻塞流涕,咳嗽憋气1周", "bbox": [476, 423, 599, 437], "bbox": [476, 423, 599, 437]},
	{"text": "现病史:1周前发现鼻塞流涕,患者无发热,感冒后咳嗽、憋气,间断治疗,时轻时重,今日来诊", "bbox": [476, 447, 852, 461], "bbox": [476, 447, 852, 461]},
	{"text": "既往史:平素体健,无高血压、冠心病、糖尿病病史", "bbox": [476, 470, 687, 484], "bbox": [476, 470, 687, 484]},
	{"text": "家族史:无家族遗传病史", "bbox": [476, 493, 580, 507], "bbox": [476, 493, 580, 507]},
	{"text": "过敏史:无", "bbox": [476, 517, 529, 530], "bbox": [476, 517, 529, 530]},
	{"text": "体格检查:鼻腔粘膜充血,水肿,水样分泌物附着", "bbox": [476, 541, 668, 555], "bbox": [476, 541, 668, 555]},
	{"text": "辅助检查:肺功能检查提示中重度阻塞性肺通气功能障碍,支气管舒张试验阳性。", "bbox": [476, 565, 786, 579], "bbox": [476, 565, 786, 579]},
	{"text": "初步印象:1、支气管哮喘(急性发作期)2、过敏性鼻炎[变应性鼻炎]", "bbox": [476, 589, 741, 603], "bbox": [476, 589, 741, 603]},
	{"text": "处理意见:坚持门诊治疗,定期复查", "bbox": [476, 612, 616, 626], "bbox": [476, 612, 616, 626]},
	{"text": "备注:", "bbox": [476, 636, 508, 650], "bbox": [476, 636, 508, 650]},
	{"text": "医师签名:刘秀层", "bbox": [827, 663, 897, 677], "bbox": [827, 663, 897, 677]},
	{"text": "第1页", "bbox": [679, 728, 701, 740], "bbox": [679, 728, 701, 740]}
]
2026-08-05 11:03:25,123 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=13.1s
2026-08-05 11:03:25,123 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[644, 222, 737, 238]
2026-08-05 11:03:25,123 INFO     29 [qwen-vl-text] coord item[1]: text=门诊号, bbox=[816, 250, 841, 263]
2026-08-05 11:03:25,123 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[476, 315, 495, 329]
2026-08-05 11:03:25,123 INFO     29 [qwen-vl-text] coord item[3]: text=性别: 女, bbox=[606, 315, 643, 329]
2026-08-05 11:03:25,123 INFO     29 [qwen-vl-text] coord item[4]: text=年龄:41岁, bbox=[684, 315, 723, 329]
2026-08-05 11:03:25,124 INFO     29 [qwen-vl-text] coord item[5]: text=民族: 汉族, bbox=[772, 315, 816, 329]
2026-08-05 11:03:25,124 INFO     29 [qwen-vl-text] coord item[6]: text=婚姻状况: 已婚, bbox=[476, 339, 538, 353]
2026-08-05 11:03:25,124 INFO     29 [qwen-vl-text] coord item[7]: text=身份证号, bbox=[606, 339, 643, 353]
2026-08-05 11:03:25,124 INFO     29 [qwen-vl-text] coord item[8]: text=职业: 职员, bbox=[772, 339, 816, 353]
2026-08-05 11:03:25,124 INFO     29 [qwen-vl-text] coord item[9]: text=现住址:, bbox=[476, 364, 508, 377]
2026-08-05 11:03:25,124 INFO     29 [qwen-vl-text] coord item[10]: text=就诊类型: 初诊, bbox=[772, 364, 833, 377]
2026-08-05 11:03:25,124 INFO     29 [qwen-vl-text] coord item[11]: text=就诊科室:耳鼻咽喉头颈外科, bbox=[476, 387, 585, 401]
2026-08-05 11:03:25,124 INFO     29 [qwen-vl-text] coord item[12]: text=就诊日期: 2025-04-11 15:43, bbox=[606, 393, 720, 406]
2026-08-05 11:03:25,124 INFO     29 [qwen-vl-text] coord item[13]: text=联系电, bbox=[751, 393, 779, 406]
2026-08-05 11:03:25,124 INFO     29 [qwen-vl-text] coord item[14]: text=主诉:鼻塞流涕,咳嗽憋气1周, bbox=[476, 423, 599, 437]
2026-08-05 11:03:25,124 INFO     29 [qwen-vl-text] coord item[15]: text=现病史:1周前发现鼻塞流涕,患者无发热,感冒后咳嗽、憋气,间断治疗,时轻时重,今日来诊, bbox=[476, 447, 852, 461]
2026-08-05 11:03:25,124 INFO     29 [qwen-vl-text] coord item[16]: text=既往史:平素体健,无高血压、冠心病、糖尿病病史, bbox=[476, 470, 687, 484]
2026-08-05 11:03:25,124 INFO     29 [qwen-vl-text] coord item[17]: text=家族史:无家族遗传病史, bbox=[476, 493, 580, 507]
2026-08-05 11:03:25,124 INFO     29 [qwen-vl-text] coord item[18]: text=过敏史:无, bbox=[476, 517, 529, 530]
2026-08-05 11:03:25,124 INFO     29 [qwen-vl-text] coord item[19]: text=体格检查:鼻腔粘膜充血,水肿,水样分泌物附着, bbox=[476, 541, 668, 555]
2026-08-05 11:03:25,125 INFO     29 [qwen-vl-text] coord item[20]: text=辅助检查:肺功能检查提示中重度阻塞性肺通气功能障碍,支气管舒张试验阳性。, bbox=[476, 565, 786, 579]
2026-08-05 11:03:25,125 INFO     29 [qwen-vl-text] coord item[21]: text=初步印象:1、支气管哮喘(急性发作期)2、过敏性鼻炎[变应性鼻炎], bbox=[476, 589, 741, 603]
2026-08-05 11:03:25,125 INFO     29 [qwen-vl-text] coord item[22]: text=处理意见:坚持门诊治疗,定期复查, bbox=[476, 612, 616, 626]
2026-08-05 11:03:25,125 INFO     29 [qwen-vl-text] coord item[23]: text=备注:, bbox=[476, 636, 508, 650]
2026-08-05 11:03:25,125 INFO     29 [qwen-vl-text] coord item[24]: text=医师签名:刘秀层, bbox=[827, 663, 897, 677]
2026-08-05 11:03:25,125 INFO     29 [qwen-vl-text] coord item[25]: text=第1页, bbox=[679, 728, 701, 740]
2026-08-05 11:03:25,125 INFO     29 [qwen-vl-text] page=22 — 26/26 coords, api_time=13.1s
2026-08-05 11:03:25,126 INFO     29 [qwen-vl-text] new_positions (26):
[[22, 542.2479999999999, 620.554, 132.09, 141.60999999999999], [22, 687.072, 708.122, 148.75, 156.48499999999999], [22, 400.792, 416.78999999999996, 187.42499999999998, 195.755], [22, 510.252, 541.406, 187.42499999999998, 195.755], [22, 575.928, 608.766, 187.42499999999998, 195.755], [22, 650.024, 687.072, 187.42499999999998, 195.755], [22, 400.792, 452.996, 201.70499999999998, 210.035], [22, 510.252, 541.406, 201.70499999999998, 210.035], [22, 650.024, 687.072, 201.70499999999998, 210.035], [22, 400.792, 427.736, 216.57999999999998, 224.315], [22, 650.024, 701.386, 216.57999999999998, 224.315], [22, 400.792, 492.57, 230.265, 238.595], [22, 510.252, 606.24, 233.83499999999998, 241.57], [22, 632.342, 655.918, 233.83499999999998, 241.57], [22, 400.792, 504.358, 251.685, 260.015], [22, 400.792, 717.384, 265.965, 274.295], [22, 400.792, 578.454, 279.65, 287.97999999999996], [22, 400.792, 488.35999999999996, 293.335, 301.66499999999996], [22, 400.792, 445.418, 307.615, 315.34999999999997], [22, 400.792, 562.456, 321.895, 330.22499999999997], [22, 400.792, 661.812, 336.175, 344.505], [22, 400.792, 623.922, 350.455, 358.78499999999997], [22, 400.792, 518.672, 364.14, 372.46999999999997], [22, 400.792, 427.736, 378.41999999999996, 386.75], [22, 696.334, 755.274, 394.48499999999996, 402.815], [22, 571.718, 590.242, 433.15999999999997, 440.29999999999995]]
2026-08-05 11:03:25,126 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=16.3s
2026-08-05 11:03:25,126 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 11:03:25,126 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 11:03:25,127 INFO     29 [qwen-vl-text] positions(19): [[23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0], [23, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 11:03:25,127 INFO     29 [qwen-vl-text] page grouping: [23], lines per page: [19]
2026-08-05 11:03:25,347 INFO     29 [qwen-vl-text] page=23, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 11:03:25,349 INFO     29 [qwen-vl-text] LLM extraction start, text_len=316
2026-08-05 11:03:25,349 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 11:03:25,349 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 1480, \"bbox_end\": 1498, \"encounter_dates\": [\"2025-05-09\"], \"department\": \"呼吸危重二病区(门)\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊号:\n11(急)诊病历\n性别:女 年龄:41岁 民族:汉族\n婚姻状况:已婚 身份证 业:专业技术人员\n现住址:\n就诊类型:复诊\n就诊科室:呼吸危重二病区(门) 就诊日期:2025-05-09 17:00 联系电\n主诉:咳嗽憋气一周\n现病史:患者无发热,感冒后咳嗽、憋气一周,间断治疗,时轻时重,今日来诊\n既往史:平素体健,无高血压、冠心病、糖尿病病史\n个人史:无吸烟史\n过敏史:无\n体格检查:听诊:双肺呼吸音清,未闻及干、湿性啰音\n辅助检查:肺功能检查提示中重度阻塞性肺通气功能障碍,支气管舒张试验阳性。\n初步印象:1、支气管哮喘.2、过敏性鼻炎[变应性鼻炎]\n处理意见:坚持门诊治疗,定期复查\n备注:\n医师签名:段竹云\n第1页",
    "role": "user"
  }
]
[92m11:03:25 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:03:25,350 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:03:25,351 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T11:03:25.350+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 11:03:27,971 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:03:27,971 INFO     29 [qwen-vl-text] LLM output (len=240):
{
  "encounter_date": "2025-05-09",
  "chief_complaint": "咳嗽憋气一周",
  "present_illness": "患者无发热,感冒后咳嗽、憋气一周,间断治疗,时轻时重,今日来诊",
  "past_history": "平素体健,无高血压、冠心病、糖尿病病史",
  "diagnosis": "1、支气管哮喘.2、过敏性鼻炎[变应性鼻炎]",
  "treatment_plan": "坚持门诊治疗,定期复查"
}
2026-08-05 11:03:27,971 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-05-09]
2026-08-05 11:03:27,974 INFO     29 [qwen-vl-text] coord API call start, page=23, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1033231, prompt_len=986
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共19行）
["门诊号:", "11(急)诊病历", "性别:女 年龄:41岁 民族:汉族", "婚姻状况:已婚 身份证 业:专业技术人员", "现住址:", "就诊类型:复诊", "就诊科室:呼吸危重二病区(门) 就诊日期:2025-05-09 17:00 联系电", "主诉:咳嗽憋气一周", "现病史:患者无发热,感冒后咳嗽、憋气一周,间断治疗,时轻时重,今日来诊", "既往史:平素体健,无高血压、冠心病、糖尿病病史", "个人史:无吸烟史", "过敏史:无", "体格检查:听诊:双肺呼吸音清,未闻及干、湿性啰音", "辅助检查:肺功能检查提示中重度阻塞性肺通气功能障碍,支气管舒张试验阳性。", "初步印象:1、支气管哮喘.2、过敏性鼻炎[变应性鼻炎]", "处理意见:坚持门诊治疗,定期复查", "备注:", "医师签名:段竹云", "第1页"]

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
2026-08-05 11:03:35,393 INFO     29 [qwen-vl-text] coord API raw response (len=1167):
```json
[
	{"text": "门诊号:", "bbox": [855, 228, 887, 244]},
	{"text": "11(急)诊病历", "bbox": [677, 196, 773, 214]},
	{"text": "性别:女 年龄:41岁 民族:汉族", "bbox": [608, 297, 786, 314]},
	{"text": "婚姻状况:已婚 身份证 业:专业技术人员", "bbox": [507, 323, 819, 341]},
	{"text": "现住址:", "bbox": [507, 351, 540, 366]},
	{"text": "就诊类型:复诊", "bbox": [739, 350, 798, 365]},
	{"text": "就诊科室:呼吸危重二病区(门) 就诊日期:2025-05-09 17:00 联系电", "bbox": [507, 375, 758, 405]},
	{"text": "主诉:咳嗽憋气一周", "bbox": [507, 416, 592, 431]},
	{"text": "现病史:患者无发热,感冒后咳嗽、憋气一周,间断治疗,时轻时重,今日来诊", "bbox": [507, 442, 827, 457]},
	{"text": "既往史:平素体健,无高血压、冠心病、糖尿病病史", "bbox": [507, 467, 721, 482]},
	{"text": "个人史:无吸烟史", "bbox": [507, 492, 592, 507]},
	{"text": "过敏史:无", "bbox": [507, 518, 561, 533]},
	{"text": "体格检查:听诊:双肺呼吸音清,未闻及干、湿性啰音", "bbox": [507, 543, 721, 558]},
	{"text": "辅助检查:肺功能检查提示中重度阻塞性肺通气功能障碍,支气管舒张试验阳性。", "bbox": [507, 569, 823, 584]},
	{"text": "初步印象:1、支气管哮喘.2、过敏性鼻炎[变应性鼻炎]", "bbox": [507, 594, 724, 609]},
	{"text": "处理意见:坚持门诊治疗,定期复查", "bbox": [507, 619, 650, 634]},
	{"text": "备注:", "bbox": [507, 646, 538, 660]},
	{"text": "医师签名:段竹云", "bbox": [756, 675, 834, 690]},
	{"text": "第1页", "bbox": [712, 747, 736, 759]}
]
```
2026-08-05 11:03:35,393 INFO     29 [qwen-vl-text] coord API: raw_items=19, valid_items=19, elapsed=7.4s
2026-08-05 11:03:35,394 INFO     29 [qwen-vl-text] coord item[0]: text=门诊号:, bbox=[855, 228, 887, 244]
2026-08-05 11:03:35,394 INFO     29 [qwen-vl-text] coord item[1]: text=11(急)诊病历, bbox=[677, 196, 773, 214]
2026-08-05 11:03:35,394 INFO     29 [qwen-vl-text] coord item[2]: text=性别:女 年龄:41岁 民族:汉族, bbox=[608, 297, 786, 314]
2026-08-05 11:03:35,394 INFO     29 [qwen-vl-text] coord item[3]: text=婚姻状况:已婚 身份证 业:专业技术人员, bbox=[507, 323, 819, 341]
2026-08-05 11:03:35,394 INFO     29 [qwen-vl-text] coord item[4]: text=现住址:, bbox=[507, 351, 540, 366]
2026-08-05 11:03:35,394 INFO     29 [qwen-vl-text] coord item[5]: text=就诊类型:复诊, bbox=[739, 350, 798, 365]
2026-08-05 11:03:35,394 INFO     29 [qwen-vl-text] coord item[6]: text=就诊科室:呼吸危重二病区(门) 就诊日期:2025-05-09 17:00 联系电, bbox=[507, 375, 758, 405]
2026-08-05 11:03:35,394 INFO     29 [qwen-vl-text] coord item[7]: text=主诉:咳嗽憋气一周, bbox=[507, 416, 592, 431]
2026-08-05 11:03:35,394 INFO     29 [qwen-vl-text] coord item[8]: text=现病史:患者无发热,感冒后咳嗽、憋气一周,间断治疗,时轻时重,今日来诊, bbox=[507, 442, 827, 457]
2026-08-05 11:03:35,394 INFO     29 [qwen-vl-text] coord item[9]: text=既往史:平素体健,无高血压、冠心病、糖尿病病史, bbox=[507, 467, 721, 482]
2026-08-05 11:03:35,394 INFO     29 [qwen-vl-text] coord item[10]: text=个人史:无吸烟史, bbox=[507, 492, 592, 507]
2026-08-05 11:03:35,394 INFO     29 [qwen-vl-text] coord item[11]: text=过敏史:无, bbox=[507, 518, 561, 533]
2026-08-05 11:03:35,394 INFO     29 [qwen-vl-text] coord item[12]: text=体格检查:听诊:双肺呼吸音清,未闻及干、湿性啰音, bbox=[507, 543, 721, 558]
2026-08-05 11:03:35,394 INFO     29 [qwen-vl-text] coord item[13]: text=辅助检查:肺功能检查提示中重度阻塞性肺通气功能障碍,支气管舒张试验阳性。, bbox=[507, 569, 823, 584]
2026-08-05 11:03:35,394 INFO     29 [qwen-vl-text] coord item[14]: text=初步印象:1、支气管哮喘.2、过敏性鼻炎[变应性鼻炎], bbox=[507, 594, 724, 609]
2026-08-05 11:03:35,394 INFO     29 [qwen-vl-text] coord item[15]: text=处理意见:坚持门诊治疗,定期复查, bbox=[507, 619, 650, 634]
2026-08-05 11:03:35,394 INFO     29 [qwen-vl-text] coord item[16]: text=备注:, bbox=[507, 646, 538, 660]
2026-08-05 11:03:35,394 INFO     29 [qwen-vl-text] coord item[17]: text=医师签名:段竹云, bbox=[756, 675, 834, 690]
2026-08-05 11:03:35,394 INFO     29 [qwen-vl-text] coord item[18]: text=第1页, bbox=[712, 747, 736, 759]
2026-08-05 11:03:35,395 INFO     29 [qwen-vl-text] page=23 — 19/19 coords, api_time=7.4s
2026-08-05 11:03:35,395 INFO     29 [qwen-vl-text] new_positions (19):
[[23, 719.91, 746.8539999999999, 135.66, 145.18], [23, 570.034, 650.866, 116.61999999999999, 127.33], [23, 511.936, 661.812, 176.715, 186.82999999999998], [23, 426.894, 689.598, 192.185, 202.89499999999998], [23, 426.894, 454.68, 208.845, 217.76999999999998], [23, 622.2379999999999, 671.9159999999999, 208.25, 217.17499999999998], [23, 426.894, 638.236, 223.125, 240.975], [23, 426.894, 498.464, 247.51999999999998, 256.445], [23, 426.894, 696.334, 262.99, 271.91499999999996], [23, 426.894, 607.082, 277.865, 286.78999999999996], [23, 426.894, 498.464, 292.74, 301.66499999999996], [23, 426.894, 472.36199999999997, 308.21, 317.135], [23, 426.894, 607.082, 323.085, 332.01], [23, 426.894, 692.966, 338.555, 347.47999999999996], [23, 426.894, 609.608, 353.43, 362.35499999999996], [23, 426.894, 547.3, 368.305, 377.22999999999996], [23, 426.894, 452.996, 384.37, 392.7], [23, 636.552, 702.228, 401.625, 410.54999999999995], [23, 599.504, 619.712, 444.465, 451.60499999999996]]
2026-08-05 11:03:35,395 INFO     29 [qwen-vl-text] ═══ DONE ═══ 19 positions, pages=1, time=10.3s
2026-08-05 11:03:35,395 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 11:03:35,395 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 11:03:35,395 INFO     29 [qwen-vl-text] positions(25): [[24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0], [24, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 11:03:35,395 INFO     29 [qwen-vl-text] page grouping: [24], lines per page: [25]
2026-08-05 11:03:35,577 INFO     29 [qwen-vl-text] page=24, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 11:03:35,579 INFO     29 [qwen-vl-text] LLM extraction start, text_len=313
2026-08-05 11:03:35,579 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 11:03:35,579 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 1524, \"bbox_end\": 1548, \"encounter_dates\": [\"2025-06-23\"], \"department\": \"普通儿科三组(门)\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊号:\n姓名\n性别: 女\n年龄:41岁\n民族: 汉族\n婚姻状况: 小组\n身份证号:\n职业: 专业技术人员\n现住址:\n就诊类型:初诊\n就诊科室:普通儿科三组(门)\n就诊日期: 2025-06-23 10:49\n联系电话\n主诉: 呼吸道感染购药\n现病史: 呼吸道感染购药\n既往史: 平素体健, 无肝炎、结核类传染病史\n过敏史: 无\n体格检查: 发育正常, 营养良好, 精神一般, 口唇红润, 双侧扁桃体无肿大, 无充血、分泌物。咽腔黏膜有充\n血, 无红肿、疱疹, 双肺呼吸音清, 听诊心律齐, 无杂音, 腹平软, 无压痛、反跳痛\n辅助检查:\n初步印象: 上呼吸道感染\n处理意见: 门诊药物治疗\n备注:\n医师签名: 谭真真\n第1页",
    "role": "user"
  }
]
[92m11:03:35 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:03:35,581 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:03:37,725 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:03:37,725 INFO     29 [qwen-vl-text] LLM output (len=194):
{
  "encounter_date": "2025-06-23",
  "chief_complaint": "呼吸道感染购药",
  "present_illness": "呼吸道感染购药",
  "past_history": "平素体健, 无肝炎、结核类传染病史",
  "diagnosis": "上呼吸道感染",
  "treatment_plan": "门诊药物治疗"
}
2026-08-05 11:03:37,725 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-06-23]
2026-08-05 11:03:37,727 INFO     29 [qwen-vl-text] coord API call start, page=24, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=759111, prompt_len=1001
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["门诊号:", "姓名", "性别: 女", "年龄:41岁", "民族: 汉族", "婚姻状况: 小组", "身份证号:", "职业: 专业技术人员", "现住址:", "就诊类型:初诊", "就诊科室:普通儿科三组(门)", "就诊日期: 2025-06-23 10:49", "联系电话", "主诉: 呼吸道感染购药", "现病史: 呼吸道感染购药", "既往史: 平素体健, 无肝炎、结核类传染病史", "过敏史: 无", "体格检查: 发育正常, 营养良好, 精神一般, 口唇红润, 双侧扁桃体无肿大, 无充血、分泌物。咽腔黏膜有充", "血, 无红肿、疱疹, 双肺呼吸音清, 听诊心律齐, 无杂音, 腹平软, 无压痛、反跳痛", "辅助检查:", "初步印象: 上呼吸道感染", "处理意见: 门诊药物治疗", "备注:", "医师签名: 谭真真", "第1页"]

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
2026-08-05 11:03:46,107 INFO     29 [qwen-vl-text] coord API raw response (len=1416):
[
	{"text": "门诊号:", "bbox": [774, 317, 805, 330]},
	{"text": "姓名", "bbox": [446, 376, 464, 389]},
	{"text": "性别: 女", "bbox": [570, 376, 605, 389]},
	{"text": "年龄:41岁", "bbox": [645, 376, 684, 389]},
	{"text": "民族: 汉族", "bbox": [740, 376, 783, 389]},
	{"text": "婚姻状况: 小组", "bbox": [446, 398, 506, 411]},
	{"text": "身份证号:", "bbox": [570, 398, 609, 411]},
	{"text": "职业: 专业技术人员", "bbox": [740, 398, 816, 411]},
	{"text": "现住址:", "bbox": [446, 420, 477, 433]},
	{"text": "就诊类型:初诊", "bbox": [740, 420, 796, 433]},
	{"text": "就诊科室:普通儿科三组(门)", "bbox": [446, 442, 555, 455]},
	{"text": "就诊日期: 2025-06-23 10:49", "bbox": [570, 442, 680, 455]},
	{"text": "联系电话", "bbox": [716, 442, 750, 455]},
	{"text": "主诉: 呼吸道感染购药", "bbox": [446, 464, 535, 477]},
	{"text": "现病史: 呼吸道感染购药", "bbox": [446, 485, 548, 498]},
	{"text": "既往史: 平素体健, 无肝炎、结核类传染病史", "bbox": [446, 507, 622, 520]},
	{"text": "过敏史: 无", "bbox": [446, 528, 499, 541]},
	{"text": "体格检查: 发育正常, 营养良好, 精神一般, 口唇红润, 双侧扁桃体无肿大, 无充血、分泌物。咽腔黏膜有充", "bbox": [446, 550, 845, 563]},
	{"text": "血, 无红肿、疱疹, 双肺呼吸音清, 听诊心律齐, 无杂音, 腹平软, 无压痛、反跳痛", "bbox": [446, 561, 744, 574]},
	{"text": "辅助检查:", "bbox": [446, 582, 486, 595]},
	{"text": "初步印象: 上呼吸道感染", "bbox": [446, 604, 539, 617]},
	{"text": "处理意见: 门诊药物治疗", "bbox": [446, 625, 539, 638]},
	{"text": "备注:", "bbox": [446, 647, 474, 660]},
	{"text": "医师签名: 谭真真", "bbox": [782, 670, 854, 683]},
	{"text": "第1页", "bbox": [641, 730, 664, 742]}
]
2026-08-05 11:03:46,107 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=8.4s
2026-08-05 11:03:46,107 INFO     29 [qwen-vl-text] coord item[0]: text=门诊号:, bbox=[774, 317, 805, 330]
2026-08-05 11:03:46,107 INFO     29 [qwen-vl-text] coord item[1]: text=姓名, bbox=[446, 376, 464, 389]
2026-08-05 11:03:46,108 INFO     29 [qwen-vl-text] coord item[2]: text=性别: 女, bbox=[570, 376, 605, 389]
2026-08-05 11:03:46,108 INFO     29 [qwen-vl-text] coord item[3]: text=年龄:41岁, bbox=[645, 376, 684, 389]
2026-08-05 11:03:46,108 INFO     29 [qwen-vl-text] coord item[4]: text=民族: 汉族, bbox=[740, 376, 783, 389]
2026-08-05 11:03:46,108 INFO     29 [qwen-vl-text] coord item[5]: text=婚姻状况: 小组, bbox=[446, 398, 506, 411]
2026-08-05 11:03:46,108 INFO     29 [qwen-vl-text] coord item[6]: text=身份证号:, bbox=[570, 398, 609, 411]
2026-08-05 11:03:46,108 INFO     29 [qwen-vl-text] coord item[7]: text=职业: 专业技术人员, bbox=[740, 398, 816, 411]
2026-08-05 11:03:46,108 INFO     29 [qwen-vl-text] coord item[8]: text=现住址:, bbox=[446, 420, 477, 433]
2026-08-05 11:03:46,108 INFO     29 [qwen-vl-text] coord item[9]: text=就诊类型:初诊, bbox=[740, 420, 796, 433]
2026-08-05 11:03:46,108 INFO     29 [qwen-vl-text] coord item[10]: text=就诊科室:普通儿科三组(门), bbox=[446, 442, 555, 455]
2026-08-05 11:03:46,108 INFO     29 [qwen-vl-text] coord item[11]: text=就诊日期: 2025-06-23 10:49, bbox=[570, 442, 680, 455]
2026-08-05 11:03:46,108 INFO     29 [qwen-vl-text] coord item[12]: text=联系电话, bbox=[716, 442, 750, 455]
2026-08-05 11:03:46,108 INFO     29 [qwen-vl-text] coord item[13]: text=主诉: 呼吸道感染购药, bbox=[446, 464, 535, 477]
2026-08-05 11:03:46,108 INFO     29 [qwen-vl-text] coord item[14]: text=现病史: 呼吸道感染购药, bbox=[446, 485, 548, 498]
2026-08-05 11:03:46,108 INFO     29 [qwen-vl-text] coord item[15]: text=既往史: 平素体健, 无肝炎、结核类传染病史, bbox=[446, 507, 622, 520]
2026-08-05 11:03:46,108 INFO     29 [qwen-vl-text] coord item[16]: text=过敏史: 无, bbox=[446, 528, 499, 541]
2026-08-05 11:03:46,109 INFO     29 [qwen-vl-text] coord item[17]: text=体格检查: 发育正常, 营养良好, 精神一般, 口唇红润, 双侧扁桃体无肿大, 无充血、分泌物。咽腔黏膜有充, bbox=[446, 550, 845, 563]
2026-08-05 11:03:46,109 INFO     29 [qwen-vl-text] coord item[18]: text=血, 无红肿、疱疹, 双肺呼吸音清, 听诊心律齐, 无杂音, 腹平软, 无压痛、反跳痛, bbox=[446, 561, 744, 574]
2026-08-05 11:03:46,109 INFO     29 [qwen-vl-text] coord item[19]: text=辅助检查:, bbox=[446, 582, 486, 595]
2026-08-05 11:03:46,109 INFO     29 [qwen-vl-text] coord item[20]: text=初步印象: 上呼吸道感染, bbox=[446, 604, 539, 617]
2026-08-05 11:03:46,109 INFO     29 [qwen-vl-text] coord item[21]: text=处理意见: 门诊药物治疗, bbox=[446, 625, 539, 638]
2026-08-05 11:03:46,109 INFO     29 [qwen-vl-text] coord item[22]: text=备注:, bbox=[446, 647, 474, 660]
2026-08-05 11:03:46,109 INFO     29 [qwen-vl-text] coord item[23]: text=医师签名: 谭真真, bbox=[782, 670, 854, 683]
2026-08-05 11:03:46,109 INFO     29 [qwen-vl-text] coord item[24]: text=第1页, bbox=[641, 730, 664, 742]
2026-08-05 11:03:46,109 INFO     29 [qwen-vl-text] page=24 — 25/25 coords, api_time=8.4s
2026-08-05 11:03:46,110 INFO     29 [qwen-vl-text] new_positions (25):
[[24, 651.708, 677.81, 188.61499999999998, 196.35], [24, 375.532, 390.688, 223.72, 231.45499999999998], [24, 479.94, 509.40999999999997, 223.72, 231.45499999999998], [24, 543.09, 575.928, 223.72, 231.45499999999998], [24, 623.0799999999999, 659.286, 223.72, 231.45499999999998], [24, 375.532, 426.05199999999996, 236.81, 244.545], [24, 479.94, 512.778, 236.81, 244.545], [24, 623.0799999999999, 687.072, 236.81, 244.545], [24, 375.532, 401.63399999999996, 249.89999999999998, 257.635], [24, 623.0799999999999, 670.232, 249.89999999999998, 257.635], [24, 375.532, 467.31, 262.99, 270.72499999999997], [24, 479.94, 572.56, 262.99, 270.72499999999997], [24, 602.872, 631.5, 262.99, 270.72499999999997], [24, 375.532, 450.46999999999997, 276.08, 283.815], [24, 375.532, 461.416, 288.575, 296.31], [24, 375.532, 523.7239999999999, 301.66499999999996, 309.4], [24, 375.532, 420.15799999999996, 314.15999999999997, 321.895], [24, 375.532, 711.49, 327.25, 334.98499999999996], [24, 375.532, 626.448, 333.79499999999996, 341.53], [24, 375.532, 409.212, 346.28999999999996, 354.025], [24, 375.532, 453.83799999999997, 359.38, 367.115], [24, 375.532, 453.83799999999997, 371.875, 379.60999999999996], [24, 375.532, 399.108, 384.965, 392.7], [24, 658.444, 719.068, 398.65, 406.385], [24, 539.722, 559.088, 434.34999999999997, 441.48999999999995]]
2026-08-05 11:03:46,110 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=10.7s
2026-08-05 11:03:46,110 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 11:03:46,110 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 11:03:46,110 INFO     29 [qwen-vl-text] positions(25): [[25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0], [25, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 11:03:46,111 INFO     29 [qwen-vl-text] page grouping: [25], lines per page: [25]
2026-08-05 11:03:46,316 INFO     29 [qwen-vl-text] page=25, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 11:03:46,318 INFO     29 [qwen-vl-text] LLM extraction start, text_len=291
2026-08-05 11:03:46,318 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 11:03:46,318 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 1571, \"bbox_end\": 1595, \"encounter_dates\": [\"2025-07-11\"], \"department\": \"普通儿科一组(门)\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊号\n1. 病历\n姓名\n性别: 女\n年龄:41岁\n民族: 汉族\n婚姻状况: 未婚\n身份证\n职业: 专业技术人员\n现住址:\n就诊类型:初诊\n就诊科室:普通儿科一组(门)\n就诊日期: 2025-07-11 10:02\n联系电话\n主诉:呼吸道感染购药\n现病史:呼吸道感染购药\n既往史:平素体健,无肝炎、结核类传染病史\n过敏史:无\n体格检查:发育正常,营养良好,精神一般,口唇红润,双侧扁桃体无肿大,无充血、分泌物。咽腔黏膜无充血、红肿、疱疹,双肺呼吸音清,听诊心律齐,无杂音,腹平软,无压痛、反跳痛\n辅助检查:\n初步印象:支气管炎\n处理意见:门诊药物治疗\n备注:\n医师签名:赵艳\n第1页",
    "role": "user"
  }
]
[92m11:03:46 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:03:46,320 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:03:48,492 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:03:48,492 INFO     29 [qwen-vl-text] LLM output (len=191):
{
  "encounter_date": "2025-07-11",
  "chief_complaint": "呼吸道感染购药",
  "present_illness": "呼吸道感染购药",
  "past_history": "平素体健,无肝炎、结核类传染病史",
  "diagnosis": "支气管炎",
  "treatment_plan": "门诊药物治疗"
}
2026-08-05 11:03:48,493 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-07-11]
2026-08-05 11:03:48,495 INFO     29 [qwen-vl-text] coord API call start, page=25, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=941020, prompt_len=979
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["门诊号", "1. 病历", "姓名", "性别: 女", "年龄:41岁", "民族: 汉族", "婚姻状况: 未婚", "身份证", "职业: 专业技术人员", "现住址:", "就诊类型:初诊", "就诊科室:普通儿科一组(门)", "就诊日期: 2025-07-11 10:02", "联系电话", "主诉:呼吸道感染购药", "现病史:呼吸道感染购药", "既往史:平素体健,无肝炎、结核类传染病史", "过敏史:无", "体格检查:发育正常,营养良好,精神一般,口唇红润,双侧扁桃体无肿大,无充血、分泌物。咽腔黏膜无充血、红肿、疱疹,双肺呼吸音清,听诊心律齐,无杂音,腹平软,无压痛、反跳痛", "辅助检查:", "初步印象:支气管炎", "处理意见:门诊药物治疗", "备注:", "医师签名:赵艳", "第1页"]

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
2026-08-05 11:03:56,798 INFO     29 [qwen-vl-text] coord API raw response (len=1394):
[
	{"text": "门诊号", "bbox": [810, 235, 837, 248]},
	{"text": "1. 病历", "bbox": [639, 204, 731, 221]},
	{"text": "姓名", "bbox": [472, 300, 490, 313]},
	{"text": "性别: 女", "bbox": [601, 300, 637, 313]},
	{"text": "年龄:41岁", "bbox": [679, 300, 718, 313]},
	{"text": "民族: 汉族", "bbox": [776, 300, 818, 313]},
	{"text": "婚姻状况: 未婚", "bbox": [472, 325, 534, 338]},
	{"text": "身份证", "bbox": [601, 325, 630, 338]},
	{"text": "职业: 专业技术人员", "bbox": [776, 325, 853, 338]},
	{"text": "现住址:", "bbox": [472, 350, 504, 363]},
	{"text": "就诊类型:初诊", "bbox": [776, 350, 832, 363]},
	{"text": "就诊科室:普通儿科一组(门)", "bbox": [472, 374, 585, 387]},
	{"text": "就诊日期: 2025-07-11 10:02", "bbox": [601, 374, 715, 387]},
	{"text": "联系电话", "bbox": [751, 374, 781, 387]},
	{"text": "主诉:呼吸道感染购药", "bbox": [472, 399, 564, 412]},
	{"text": "现病史:呼吸道感染购药", "bbox": [472, 423, 577, 436]},
	{"text": "既往史:平素体健,无肝炎、结核类传染病史", "bbox": [472, 448, 655, 461]},
	{"text": "过敏史:无", "bbox": [472, 471, 526, 484]},
	{"text": "体格检查:发育正常,营养良好,精神一般,口唇红润,双侧扁桃体无肿大,无充血、分泌物。咽腔黏膜无充血、红肿、疱疹,双肺呼吸音清,听诊心律齐,无杂音,腹平软,无压痛、反跳痛", "bbox": [472, 496, 882, 521]},
	{"text": "辅助检查:", "bbox": [472, 532, 517, 545]},
	{"text": "初步印象:支气管炎", "bbox": [472, 557, 550, 570]},
	{"text": "处理意见:门诊药物治疗", "bbox": [472, 581, 567, 594]},
	{"text": "备注:", "bbox": [472, 605, 504, 618]},
	{"text": "医师签名:赵艳", "bbox": [818, 632, 890, 647]},
	{"text": "第1页", "bbox": [673, 700, 696, 711]}
]
2026-08-05 11:03:56,799 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=8.3s
2026-08-05 11:03:56,799 INFO     29 [qwen-vl-text] coord item[0]: text=门诊号, bbox=[810, 235, 837, 248]
2026-08-05 11:03:56,799 INFO     29 [qwen-vl-text] coord item[1]: text=1. 病历, bbox=[639, 204, 731, 221]
2026-08-05 11:03:56,799 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[472, 300, 490, 313]
2026-08-05 11:03:56,799 INFO     29 [qwen-vl-text] coord item[3]: text=性别: 女, bbox=[601, 300, 637, 313]
2026-08-05 11:03:56,799 INFO     29 [qwen-vl-text] coord item[4]: text=年龄:41岁, bbox=[679, 300, 718, 313]
2026-08-05 11:03:56,799 INFO     29 [qwen-vl-text] coord item[5]: text=民族: 汉族, bbox=[776, 300, 818, 313]
2026-08-05 11:03:56,799 INFO     29 [qwen-vl-text] coord item[6]: text=婚姻状况: 未婚, bbox=[472, 325, 534, 338]
2026-08-05 11:03:56,799 INFO     29 [qwen-vl-text] coord item[7]: text=身份证, bbox=[601, 325, 630, 338]
2026-08-05 11:03:56,799 INFO     29 [qwen-vl-text] coord item[8]: text=职业: 专业技术人员, bbox=[776, 325, 853, 338]
2026-08-05 11:03:56,799 INFO     29 [qwen-vl-text] coord item[9]: text=现住址:, bbox=[472, 350, 504, 363]
2026-08-05 11:03:56,799 INFO     29 [qwen-vl-text] coord item[10]: text=就诊类型:初诊, bbox=[776, 350, 832, 363]
2026-08-05 11:03:56,800 INFO     29 [qwen-vl-text] coord item[11]: text=就诊科室:普通儿科一组(门), bbox=[472, 374, 585, 387]
2026-08-05 11:03:56,800 INFO     29 [qwen-vl-text] coord item[12]: text=就诊日期: 2025-07-11 10:02, bbox=[601, 374, 715, 387]
2026-08-05 11:03:56,800 INFO     29 [qwen-vl-text] coord item[13]: text=联系电话, bbox=[751, 374, 781, 387]
2026-08-05 11:03:56,800 INFO     29 [qwen-vl-text] coord item[14]: text=主诉:呼吸道感染购药, bbox=[472, 399, 564, 412]
2026-08-05 11:03:56,800 INFO     29 [qwen-vl-text] coord item[15]: text=现病史:呼吸道感染购药, bbox=[472, 423, 577, 436]
2026-08-05 11:03:56,800 INFO     29 [qwen-vl-text] coord item[16]: text=既往史:平素体健,无肝炎、结核类传染病史, bbox=[472, 448, 655, 461]
2026-08-05 11:03:56,800 INFO     29 [qwen-vl-text] coord item[17]: text=过敏史:无, bbox=[472, 471, 526, 484]
2026-08-05 11:03:56,800 INFO     29 [qwen-vl-text] coord item[18]: text=体格检查:发育正常,营养良好,精神一般,口唇红润,双侧扁桃体无肿大,无充血、分泌物。咽腔黏膜无充血、红肿、疱疹,双肺呼吸音清,听诊心律齐,无杂音,腹平软,无压痛、反跳痛, bbox=[472, 496, 882, 521]
2026-08-05 11:03:56,800 INFO     29 [qwen-vl-text] coord item[19]: text=辅助检查:, bbox=[472, 532, 517, 545]
2026-08-05 11:03:56,800 INFO     29 [qwen-vl-text] coord item[20]: text=初步印象:支气管炎, bbox=[472, 557, 550, 570]
2026-08-05 11:03:56,800 INFO     29 [qwen-vl-text] coord item[21]: text=处理意见:门诊药物治疗, bbox=[472, 581, 567, 594]
2026-08-05 11:03:56,800 INFO     29 [qwen-vl-text] coord item[22]: text=备注:, bbox=[472, 605, 504, 618]
2026-08-05 11:03:56,800 INFO     29 [qwen-vl-text] coord item[23]: text=医师签名:赵艳, bbox=[818, 632, 890, 647]
2026-08-05 11:03:56,800 INFO     29 [qwen-vl-text] coord item[24]: text=第1页, bbox=[673, 700, 696, 711]
2026-08-05 11:03:56,800 INFO     29 [qwen-vl-text] page=25 — 25/25 coords, api_time=8.3s
2026-08-05 11:03:56,800 INFO     29 [qwen-vl-text] new_positions (25):
[[25, 682.02, 704.754, 139.825, 147.56], [25, 538.038, 615.502, 121.38, 131.495], [25, 397.424, 412.58, 178.5, 186.23499999999999], [25, 506.042, 536.3539999999999, 178.5, 186.23499999999999], [25, 571.718, 604.5559999999999, 178.5, 186.23499999999999], [25, 653.3919999999999, 688.756, 178.5, 186.23499999999999], [25, 397.424, 449.628, 193.375, 201.10999999999999], [25, 506.042, 530.46, 193.375, 201.10999999999999], [25, 653.3919999999999, 718.226, 193.375, 201.10999999999999], [25, 397.424, 424.368, 208.25, 215.98499999999999], [25, 653.3919999999999, 700.544, 208.25, 215.98499999999999], [25, 397.424, 492.57, 222.53, 230.265], [25, 506.042, 602.03, 222.53, 230.265], [25, 632.342, 657.602, 222.53, 230.265], [25, 397.424, 474.888, 237.405, 245.14], [25, 397.424, 485.834, 251.685, 259.42], [25, 397.424, 551.51, 266.56, 274.295], [25, 397.424, 442.892, 280.245, 287.97999999999996], [25, 397.424, 742.644, 295.12, 309.995], [25, 397.424, 435.31399999999996, 316.53999999999996, 324.275], [25, 397.424, 463.09999999999997, 331.41499999999996, 339.15], [25, 397.424, 477.414, 345.695, 353.43], [25, 397.424, 424.368, 359.97499999999997, 367.71], [25, 688.756, 749.38, 376.03999999999996, 384.965], [25, 566.6659999999999, 586.0319999999999, 416.5, 423.04499999999996]]
2026-08-05 11:03:56,801 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=10.7s
2026-08-05 11:03:56,801 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 11:03:56,801 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 11:03:56,801 INFO     29 [qwen-vl-text] positions(25): [[26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0], [26, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 11:03:56,801 INFO     29 [qwen-vl-text] page grouping: [26], lines per page: [25]
2026-08-05 11:03:57,033 INFO     29 [qwen-vl-text] page=26, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 11:03:57,036 INFO     29 [qwen-vl-text] LLM extraction start, text_len=398
2026-08-05 11:03:57,036 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 11:03:57,036 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 1627, \"bbox_end\": 1651, \"encounter_dates\": [\"2025-09-18\"], \"department\": \"普通儿科二区(门)\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊病历\n门诊\n姓名:\n性别: 女\n年龄:41岁\n民族: 汉族\n婚姻状况: 未婚\n身份证\n职业: 职员\n现住址:\n就诊类型:初诊\n就诊科室:普通儿科二区(门)\n就诊日期: 2025-09-18 15:22\n联系电话\n主诉:咽部疼痛伴眼部不适4天\n现病史:4天前无明显诱因出现咽部疼痛,伴鼻塞,伴眼部不适,无发热、呕吐、腹泻、皮疹等不适,病后精神、食欲欠佳,大小便正常。\n既往史:无特殊。\n过敏史:无\n体格检查:发育正常,营养良好,精神一般,呼吸平稳,双眼睑结膜充血,口唇红润,咽腔充血,无疱疹,双侧扁桃体I°,充血,无分泌物,双肺呼吸音清,未闻及干湿性啰音,听诊心律齐,无杂音,腹平软,无压痛、反跳痛,未触及包块,肠鸣音活跃,神经系统未见阳性体征。\n辅助检查:无\n初步印象:1.急性咽峡炎.2.急性变应性结膜炎\n处理意见:门诊治疗,动态观察病情变化,不适及时随诊。\n备注:\n医师签名:赵艳\n第1页",
    "role": "user"
  }
]
[92m11:03:57 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:03:57,037 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:03:57,038 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T11:03:57.036+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 11:03:59,660 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:03:59,660 INFO     29 [qwen-vl-text] LLM output (len=262):
{
  "encounter_date": "2025-09-18",
  "chief_complaint": "咽部疼痛伴眼部不适4天",
  "present_illness": "4天前无明显诱因出现咽部疼痛,伴鼻塞,伴眼部不适,无发热、呕吐、腹泻、皮疹等不适,病后精神、食欲欠佳,大小便正常。",
  "past_history": "无特殊。",
  "diagnosis": "1.急性咽峡炎.2.急性变应性结膜炎",
  "treatment_plan": "门诊治疗,动态观察病情变化,不适及时随诊。"
}
2026-08-05 11:03:59,660 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-09-18]
2026-08-05 11:03:59,662 INFO     29 [qwen-vl-text] coord API call start, page=26, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1131082, prompt_len=1086
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["门诊病历", "门诊", "姓名:", "性别: 女", "年龄:41岁", "民族: 汉族", "婚姻状况: 未婚", "身份证", "职业: 职员", "现住址:", "就诊类型:初诊", "就诊科室:普通儿科二区(门)", "就诊日期: 2025-09-18 15:22", "联系电话", "主诉:咽部疼痛伴眼部不适4天", "现病史:4天前无明显诱因出现咽部疼痛,伴鼻塞,伴眼部不适,无发热、呕吐、腹泻、皮疹等不适,病后精神、食欲欠佳,大小便正常。", "既往史:无特殊。", "过敏史:无", "体格检查:发育正常,营养良好,精神一般,呼吸平稳,双眼睑结膜充血,口唇红润,咽腔充血,无疱疹,双侧扁桃体I°,充血,无分泌物,双肺呼吸音清,未闻及干湿性啰音,听诊心律齐,无杂音,腹平软,无压痛、反跳痛,未触及包块,肠鸣音活跃,神经系统未见阳性体征。", "辅助检查:无", "初步印象:1.急性咽峡炎.2.急性变应性结膜炎", "处理意见:门诊治疗,动态观察病情变化,不适及时随诊。", "备注:", "医师签名:赵艳", "第1页"]

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
2026-08-05 11:04:08,606 INFO     29 [qwen-vl-text] coord API raw response (len=1501):
[
	{"text": "门诊病历", "bbox": [621, 175, 702, 191]},
	{"text": "门诊", "bbox": [769, 203, 790, 215]},
	{"text": "姓名:", "bbox": [475, 265, 496, 278]},
	{"text": "性别: 女", "bbox": [589, 265, 620, 278]},
	{"text": "年龄:41岁", "bbox": [657, 265, 691, 278]},
	{"text": "民族: 汉族", "bbox": [739, 265, 776, 278]},
	{"text": "婚姻状况: 未婚", "bbox": [475, 288, 529, 301]},
	{"text": "身份证", "bbox": [589, 288, 612, 301]},
	{"text": "职业: 职员", "bbox": [739, 288, 776, 301]},
	{"text": "现住址:", "bbox": [475, 312, 503, 324]},
	{"text": "就诊类型:初诊", "bbox": [739, 312, 787, 324]},
	{"text": "就诊科室:普通儿科二区(门)", "bbox": [475, 335, 574, 348]},
	{"text": "就诊日期: 2025-09-18 15:22", "bbox": [588, 335, 688, 348]},
	{"text": "联系电话", "bbox": [718, 335, 749, 348]},
	{"text": "主诉:咽部疼痛伴眼部不适4天", "bbox": [475, 358, 582, 370]},
	{"text": "现病史:4天前无明显诱因出现咽部疼痛,伴鼻塞,伴眼部不适,无发热、呕吐、腹泻、皮疹等不适,病后精神、食欲欠佳,大小便正常。", "bbox": [475, 380, 837, 403]},
	{"text": "既往史:无特殊。", "bbox": [475, 413, 541, 426]},
	{"text": "过敏史:无", "bbox": [475, 435, 522, 448]},
	{"text": "体格检查:发育正常,营养良好,精神一般,呼吸平稳,双眼睑结膜充血,口唇红润,咽腔充血,无疱疹,双侧扁桃体I°,充血,无分泌物,双肺呼吸音清,未闻及干湿性啰音,听诊心律齐,无杂音,腹平软,无压痛、反跳痛,未触及包块,肠鸣音活跃,神经系统未见阳性体征。", "bbox": [475, 457, 837, 492]},
	{"text": "辅助检查:无", "bbox": [475, 502, 522, 514]},
	{"text": "初步印象:1.急性咽峡炎.2.急性变应性结膜炎", "bbox": [475, 524, 638, 537]},
	{"text": "处理意见:门诊治疗,动态观察病情变化,不适及时随诊。", "bbox": [475, 546, 669, 559]},
	{"text": "备注:", "bbox": [475, 567, 500, 580]},
	{"text": "医师签名:赵艳", "bbox": [776, 591, 837, 604]},
	{"text": "第1页", "bbox": [651, 653, 671, 663]}
]
2026-08-05 11:04:08,606 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=8.9s
2026-08-05 11:04:08,606 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[621, 175, 702, 191]
2026-08-05 11:04:08,606 INFO     29 [qwen-vl-text] coord item[1]: text=门诊, bbox=[769, 203, 790, 215]
2026-08-05 11:04:08,606 INFO     29 [qwen-vl-text] coord item[2]: text=姓名:, bbox=[475, 265, 496, 278]
2026-08-05 11:04:08,606 INFO     29 [qwen-vl-text] coord item[3]: text=性别: 女, bbox=[589, 265, 620, 278]
2026-08-05 11:04:08,606 INFO     29 [qwen-vl-text] coord item[4]: text=年龄:41岁, bbox=[657, 265, 691, 278]
2026-08-05 11:04:08,606 INFO     29 [qwen-vl-text] coord item[5]: text=民族: 汉族, bbox=[739, 265, 776, 278]
2026-08-05 11:04:08,607 INFO     29 [qwen-vl-text] coord item[6]: text=婚姻状况: 未婚, bbox=[475, 288, 529, 301]
2026-08-05 11:04:08,607 INFO     29 [qwen-vl-text] coord item[7]: text=身份证, bbox=[589, 288, 612, 301]
2026-08-05 11:04:08,607 INFO     29 [qwen-vl-text] coord item[8]: text=职业: 职员, bbox=[739, 288, 776, 301]
2026-08-05 11:04:08,607 INFO     29 [qwen-vl-text] coord item[9]: text=现住址:, bbox=[475, 312, 503, 324]
2026-08-05 11:04:08,607 INFO     29 [qwen-vl-text] coord item[10]: text=就诊类型:初诊, bbox=[739, 312, 787, 324]
2026-08-05 11:04:08,607 INFO     29 [qwen-vl-text] coord item[11]: text=就诊科室:普通儿科二区(门), bbox=[475, 335, 574, 348]
2026-08-05 11:04:08,607 INFO     29 [qwen-vl-text] coord item[12]: text=就诊日期: 2025-09-18 15:22, bbox=[588, 335, 688, 348]
2026-08-05 11:04:08,607 INFO     29 [qwen-vl-text] coord item[13]: text=联系电话, bbox=[718, 335, 749, 348]
2026-08-05 11:04:08,607 INFO     29 [qwen-vl-text] coord item[14]: text=主诉:咽部疼痛伴眼部不适4天, bbox=[475, 358, 582, 370]
2026-08-05 11:04:08,607 INFO     29 [qwen-vl-text] coord item[15]: text=现病史:4天前无明显诱因出现咽部疼痛,伴鼻塞,伴眼部不适,无发热、呕吐、腹泻、皮疹等不适,病后精神、食欲欠佳,大小便正常。, bbox=[475, 380, 837, 403]
2026-08-05 11:04:08,607 INFO     29 [qwen-vl-text] coord item[16]: text=既往史:无特殊。, bbox=[475, 413, 541, 426]
2026-08-05 11:04:08,607 INFO     29 [qwen-vl-text] coord item[17]: text=过敏史:无, bbox=[475, 435, 522, 448]
2026-08-05 11:04:08,607 INFO     29 [qwen-vl-text] coord item[18]: text=体格检查:发育正常,营养良好,精神一般,呼吸平稳,双眼睑结膜充血,口唇红润,咽腔充血,无疱疹,双侧扁桃体I°,充血,无分泌物,双肺呼吸音清,未闻及干湿性啰音,听诊心律齐,无杂音,腹平软,无压痛、反跳痛,未触及包块,肠鸣音活跃,神经系统未见阳性体征。, bbox=[475, 457, 837, 492]
2026-08-05 11:04:08,607 INFO     29 [qwen-vl-text] coord item[19]: text=辅助检查:无, bbox=[475, 502, 522, 514]
2026-08-05 11:04:08,607 INFO     29 [qwen-vl-text] coord item[20]: text=初步印象:1.急性咽峡炎.2.急性变应性结膜炎, bbox=[475, 524, 638, 537]
2026-08-05 11:04:08,607 INFO     29 [qwen-vl-text] coord item[21]: text=处理意见:门诊治疗,动态观察病情变化,不适及时随诊。, bbox=[475, 546, 669, 559]
2026-08-05 11:04:08,607 INFO     29 [qwen-vl-text] coord item[22]: text=备注:, bbox=[475, 567, 500, 580]
2026-08-05 11:04:08,607 INFO     29 [qwen-vl-text] coord item[23]: text=医师签名:赵艳, bbox=[776, 591, 837, 604]
2026-08-05 11:04:08,608 INFO     29 [qwen-vl-text] coord item[24]: text=第1页, bbox=[651, 653, 671, 663]
2026-08-05 11:04:08,608 INFO     29 [qwen-vl-text] page=26 — 25/25 coords, api_time=8.9s
2026-08-05 11:04:08,608 INFO     29 [qwen-vl-text] new_positions (25):
[[26, 522.882, 591.084, 104.125, 113.645], [26, 647.4979999999999, 665.18, 120.785, 127.925], [26, 399.95, 417.632, 157.67499999999998, 165.41], [26, 495.938, 522.04, 157.67499999999998, 165.41], [26, 553.194, 581.822, 157.67499999999998, 165.41], [26, 622.2379999999999, 653.3919999999999, 157.67499999999998, 165.41], [26, 399.95, 445.418, 171.35999999999999, 179.095], [26, 495.938, 515.304, 171.35999999999999, 179.095], [26, 622.2379999999999, 653.3919999999999, 171.35999999999999, 179.095], [26, 399.95, 423.526, 185.64, 192.78], [26, 622.2379999999999, 662.654, 185.64, 192.78], [26, 399.95, 483.308, 199.325, 207.06], [26, 495.096, 579.2959999999999, 199.325, 207.06], [26, 604.5559999999999, 630.658, 199.325, 207.06], [26, 399.95, 490.044, 213.01, 220.14999999999998], [26, 399.95, 704.754, 226.1, 239.785], [26, 399.95, 455.522, 245.73499999999999, 253.47], [26, 399.95, 439.524, 258.825, 266.56], [26, 399.95, 704.754, 271.91499999999996, 292.74], [26, 399.95, 439.524, 298.69, 305.83], [26, 399.95, 537.196, 311.78, 319.515], [26, 399.95, 563.298, 324.87, 332.60499999999996], [26, 399.95, 421.0, 337.365, 345.09999999999997], [26, 653.3919999999999, 704.754, 351.645, 359.38], [26, 548.1419999999999, 564.982, 388.53499999999997, 394.48499999999996]]
2026-08-05 11:04:08,608 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=11.8s
2026-08-05 11:04:08,608 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 11:04:08,608 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 11:04:08,608 INFO     29 [qwen-vl-text] positions(38): [[27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0], [27, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 11:04:08,609 INFO     29 [qwen-vl-text] page grouping: [27], lines per page: [38]
2026-08-05 11:04:08,814 INFO     29 [qwen-vl-text] page=27, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 11:04:08,816 INFO     29 [qwen-vl-text] LLM extraction start, text_len=581
2026-08-05 11:04:08,817 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 11:04:08,817 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 1684, \"bbox_end\": 1721, \"encounter_dates\": [\"2025-12-01\"], \"department\": \"普通儿科二区(门)\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊\n1.1、心/诊病历\n门诊\n2026-01-15 呼吸危重二病区(门)\n2026-01-06 妇科一病区(门)\n2025-12-09 普通儿科二区(...\n2025-12-07 普通儿科二区(...\n2025-12-01 普通儿科二区(...\n2025-11-27 普通儿科二区(...\n2025-11-24 普通儿科二区(...\n2025-09-18 普通儿科二区(...\n2025-07-11 普通儿科一组(...\n2025-06-23 普通儿科三组(...\n2025-05-09 呼吸危重二病区(门)\n姓名:\n性别: 女\n年龄:41岁\n民族: 汉族\n婚姻状况: 未...\n身份证:\n职业: 专业技术人员\n现住址:\n就诊类型:初诊\n就诊科室:普通儿科二区(门)\n就诊日期: 2025-12-01 15:28\n联系电\n主诉: 发热半天。\n现病史: 半天前出现发热,最高体温38.0℃,口服药物治疗1次,无咳嗽,无喘息,无呼吸困难,无咯血,无腹泻、呕吐等。精神食欲一般,大小便正常。\n既往史: 无。\n过敏史: 无\n体格检查: 神志清,精神一般,呼吸浅快,咽充血,扁桃体二度大,充血,无疱疹,无脓点,双肺呼吸音清,\n心音有力,律齐,腹软。\n辅助检查:\n初步印象: 急性上呼吸道感染\n处理意见: 口服药物,动态观察,不适随诊。\n备注:\n医师签名: 赵海国\n第1页",
    "role": "user"
  }
]
[92m11:04:08 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:04:08,818 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:04:11,261 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:04:11,262 INFO     29 [qwen-vl-text] LLM output (len=247):
{
  "encounter_date": "2025-12-01",
  "chief_complaint": "发热半天。",
  "present_illness": "半天前出现发热,最高体温38.0℃,口服药物治疗1次,无咳嗽,无喘息,无呼吸困难,无咯血,无腹泻、呕吐等。精神食欲一般,大小便正常。",
  "past_history": "无。",
  "diagnosis": "急性上呼吸道感染",
  "treatment_plan": "口服药物,动态观察,不适随诊。"
}
2026-08-05 11:04:11,262 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-01]
2026-08-05 11:04:11,265 INFO     29 [qwen-vl-text] coord API call start, page=27, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1002526, prompt_len=1308
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共38行）
["门诊", "1.1、心/诊病历", "门诊", "2026-01-15 呼吸危重二病区(门)", "2026-01-06 妇科一病区(门)", "2025-12-09 普通儿科二区(...", "2025-12-07 普通儿科二区(...", "2025-12-01 普通儿科二区(...", "2025-11-27 普通儿科二区(...", "2025-11-24 普通儿科二区(...", "2025-09-18 普通儿科二区(...", "2025-07-11 普通儿科一组(...", "2025-06-23 普通儿科三组(...", "2025-05-09 呼吸危重二病区(门)", "姓名:", "性别: 女", "年龄:41岁", "民族: 汉族", "婚姻状况: 未...", "身份证:", "职业: 专业技术人员", "现住址:", "就诊类型:初诊", "就诊科室:普通儿科二区(门)", "就诊日期: 2025-12-01 15:28", "联系电", "主诉: 发热半天。", "现病史: 半天前出现发热,最高体温38.0℃,口服药物治疗1次,无咳嗽,无喘息,无呼吸困难,无咯血,无腹泻、呕吐等。精神食欲一般,大小便正常。", "既往史: 无。", "过敏史: 无", "体格检查: 神志清,精神一般,呼吸浅快,咽充血,扁桃体二度大,充血,无疱疹,无脓点,双肺呼吸音清,", "心音有力,律齐,腹软。", "辅助检查:", "初步印象: 急性上呼吸道感染", "处理意见: 口服药物,动态观察,不适随诊。", "备注:", "医师签名: 赵海国", "第1页"]

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
2026-08-05 11:04:24,052 INFO     29 [qwen-vl-text] coord API raw response (len=2253):
[
	{"text": "门诊", "bbox": [834, 248, 852, 264]},
	{"text": "1.1、心/诊病历", "bbox": [656, 217, 752, 234]},
	{"text": "门诊", "bbox": [237, 129, 257, 142]},
	{"text": "2026-01-15 呼吸危重二病区(门)", "bbox": [65, 272, 175, 287]},
	{"text": "2026-01-06 妇科一病区(门)", "bbox": [65, 319, 159, 334]},
	{"text": "2025-12-09 普通儿科二区 (...", "bbox": [65, 367, 167, 381]},
	{"text": "2025-12-07 普通儿科二区 (...", "bbox": [65, 414, 167, 429]},
	{"text": "2025-12-01 普通儿科二区 (...", "bbox": [65, 462, 165, 477]},
	{"text": "2025-11-27 普通儿科二区 (...", "bbox": [65, 510, 167, 524]},
	{"text": "2025-11-24 普通儿科二区 (...", "bbox": [65, 557, 165, 571]},
	{"text": "2025-09-18 普通儿科二区 (...", "bbox": [65, 605, 167, 619]},
	{"text": "2025-07-11 普通儿科一组 (...", "bbox": [65, 652, 165, 667]},
	{"text": "2025-06-23 普通儿科三组 (...", "bbox": [65, 700, 167, 714]},
	{"text": "2025-05-09 呼吸危重二病区(门)", "bbox": [65, 746, 173, 761]},
	{"text": "姓名:", "bbox": [485, 318, 508, 333]},
	{"text": "性别: 女", "bbox": [618, 318, 654, 333]},
	{"text": "年龄:41岁", "bbox": [697, 318, 737, 333]},
	{"text": "民族: 汉族", "bbox": [797, 318, 842, 333]},
	{"text": "婚姻状况: 未...", "bbox": [485, 344, 548, 359]},
	{"text": "身份证:", "bbox": [618, 344, 650, 359]},
	{"text": "职业: 专业技术人员", "bbox": [797, 344, 876, 359]},
	{"text": "现住址:", "bbox": [485, 370, 517, 385]},
	{"text": "就诊类型:初诊", "bbox": [797, 370, 854, 385]},
	{"text": "就诊科室:普通儿科二区(门)", "bbox": [485, 396, 600, 411]},
	{"text": "就诊日期: 2025-12-01 15:28", "bbox": [618, 396, 733, 411]},
	{"text": "联系电", "bbox": [771, 396, 797, 411]},
	{"text": "主诉: 发热半天。", "bbox": [485, 422, 557, 437]},
	{"text": "现病史: 半天前出现发热,最高体温38.0℃,口服药物治疗1次,无咳嗽,无喘息,无呼吸困难,无咯血,无腹泻、呕吐等。精神食欲一般,大小便正常。", "bbox": [485, 448, 914, 475]},
	{"text": "既往史: 无。", "bbox": [485, 487, 543, 501]},
	{"text": "过敏史: 无", "bbox": [485, 512, 538, 527]},
	{"text": "体格检查: 神志清,精神一般,呼吸浅快,咽充血,扁桃体二度大,充血,无疱疹,无脓点,双肺呼吸音清,", "bbox": [485, 537, 909, 552]},
	{"text": "心音有力,律齐,腹软。", "bbox": [485, 551, 580, 566]},
	{"text": "辅助检查:", "bbox": [485, 576, 527, 591]},
	{"text": "初步印象: 急性上呼吸道感染", "bbox": [485, 603, 599, 617]},
	{"text": "处理意见: 口服药物,动态观察,不适随诊。", "bbox": [485, 628, 658, 643]},
	{"text": "备注:", "bbox": [485, 654, 514, 668]},
	{"text": "医师签名: 赵海国", "bbox": [840, 682, 916, 697]},
	{"text": "第1页", "bbox": [690, 754, 713, 767]}
]
2026-08-05 11:04:24,053 INFO     29 [qwen-vl-text] coord API: raw_items=38, valid_items=38, elapsed=12.8s
2026-08-05 11:04:24,053 INFO     29 [qwen-vl-text] coord item[0]: text=门诊, bbox=[834, 248, 852, 264]
2026-08-05 11:04:24,053 INFO     29 [qwen-vl-text] coord item[1]: text=1.1、心/诊病历, bbox=[656, 217, 752, 234]
2026-08-05 11:04:24,053 INFO     29 [qwen-vl-text] coord item[2]: text=门诊, bbox=[237, 129, 257, 142]
2026-08-05 11:04:24,053 INFO     29 [qwen-vl-text] coord item[3]: text=2026-01-15 呼吸危重二病区(门), bbox=[65, 272, 175, 287]
2026-08-05 11:04:24,053 INFO     29 [qwen-vl-text] coord item[4]: text=2026-01-06 妇科一病区(门), bbox=[65, 319, 159, 334]
2026-08-05 11:04:24,053 INFO     29 [qwen-vl-text] coord item[5]: text=2025-12-09 普通儿科二区 (..., bbox=[65, 367, 167, 381]
2026-08-05 11:04:24,053 INFO     29 [qwen-vl-text] coord item[6]: text=2025-12-07 普通儿科二区 (..., bbox=[65, 414, 167, 429]
2026-08-05 11:04:24,053 INFO     29 [qwen-vl-text] coord item[7]: text=2025-12-01 普通儿科二区 (..., bbox=[65, 462, 165, 477]
2026-08-05 11:04:24,053 INFO     29 [qwen-vl-text] coord item[8]: text=2025-11-27 普通儿科二区 (..., bbox=[65, 510, 167, 524]
2026-08-05 11:04:24,053 INFO     29 [qwen-vl-text] coord item[9]: text=2025-11-24 普通儿科二区 (..., bbox=[65, 557, 165, 571]
2026-08-05 11:04:24,053 INFO     29 [qwen-vl-text] coord item[10]: text=2025-09-18 普通儿科二区 (..., bbox=[65, 605, 167, 619]
2026-08-05 11:04:24,053 INFO     29 [qwen-vl-text] coord item[11]: text=2025-07-11 普通儿科一组 (..., bbox=[65, 652, 165, 667]
2026-08-05 11:04:24,053 INFO     29 [qwen-vl-text] coord item[12]: text=2025-06-23 普通儿科三组 (..., bbox=[65, 700, 167, 714]
2026-08-05 11:04:24,053 INFO     29 [qwen-vl-text] coord item[13]: text=2025-05-09 呼吸危重二病区(门), bbox=[65, 746, 173, 761]
2026-08-05 11:04:24,053 INFO     29 [qwen-vl-text] coord item[14]: text=姓名:, bbox=[485, 318, 508, 333]
2026-08-05 11:04:24,054 INFO     29 [qwen-vl-text] coord item[15]: text=性别: 女, bbox=[618, 318, 654, 333]
2026-08-05 11:04:24,054 INFO     29 [qwen-vl-text] coord item[16]: text=年龄:41岁, bbox=[697, 318, 737, 333]
2026-08-05 11:04:24,054 INFO     29 [qwen-vl-text] coord item[17]: text=民族: 汉族, bbox=[797, 318, 842, 333]
2026-08-05 11:04:24,054 INFO     29 [qwen-vl-text] coord item[18]: text=婚姻状况: 未..., bbox=[485, 344, 548, 359]
2026-08-05 11:04:24,054 INFO     29 [qwen-vl-text] coord item[19]: text=身份证:, bbox=[618, 344, 650, 359]
2026-08-05 11:04:24,054 INFO     29 [qwen-vl-text] coord item[20]: text=职业: 专业技术人员, bbox=[797, 344, 876, 359]
2026-08-05 11:04:24,054 INFO     29 [qwen-vl-text] coord item[21]: text=现住址:, bbox=[485, 370, 517, 385]
2026-08-05 11:04:24,054 INFO     29 [qwen-vl-text] coord item[22]: text=就诊类型:初诊, bbox=[797, 370, 854, 385]
2026-08-05 11:04:24,054 INFO     29 [qwen-vl-text] coord item[23]: text=就诊科室:普通儿科二区(门), bbox=[485, 396, 600, 411]
2026-08-05 11:04:24,054 INFO     29 [qwen-vl-text] coord item[24]: text=就诊日期: 2025-12-01 15:28, bbox=[618, 396, 733, 411]
2026-08-05 11:04:24,054 INFO     29 [qwen-vl-text] coord item[25]: text=联系电, bbox=[771, 396, 797, 411]
2026-08-05 11:04:24,054 INFO     29 [qwen-vl-text] coord item[26]: text=主诉: 发热半天。, bbox=[485, 422, 557, 437]
2026-08-05 11:04:24,054 INFO     29 [qwen-vl-text] coord item[27]: text=现病史: 半天前出现发热,最高体温38.0℃,口服药物治疗1次,无咳嗽,无喘息,无呼吸困难,无咯血,无腹泻、呕吐等。精神食欲一般,大小便正常。, bbox=[485, 448, 914, 475]
2026-08-05 11:04:24,054 INFO     29 [qwen-vl-text] coord item[28]: text=既往史: 无。, bbox=[485, 487, 543, 501]
2026-08-05 11:04:24,054 INFO     29 [qwen-vl-text] coord item[29]: text=过敏史: 无, bbox=[485, 512, 538, 527]
2026-08-05 11:04:24,054 INFO     29 [qwen-vl-text] coord item[30]: text=体格检查: 神志清,精神一般,呼吸浅快,咽充血,扁桃体二度大,充血,无疱疹,无脓点,双肺呼吸音清,, bbox=[485, 537, 909, 552]
2026-08-05 11:04:24,054 INFO     29 [qwen-vl-text] coord item[31]: text=心音有力,律齐,腹软。, bbox=[485, 551, 580, 566]
2026-08-05 11:04:24,054 INFO     29 [qwen-vl-text] coord item[32]: text=辅助检查:, bbox=[485, 576, 527, 591]
2026-08-05 11:04:24,054 INFO     29 [qwen-vl-text] coord item[33]: text=初步印象: 急性上呼吸道感染, bbox=[485, 603, 599, 617]
2026-08-05 11:04:24,054 INFO     29 [qwen-vl-text] coord item[34]: text=处理意见: 口服药物,动态观察,不适随诊。, bbox=[485, 628, 658, 643]
2026-08-05 11:04:24,054 INFO     29 [qwen-vl-text] coord item[35]: text=备注:, bbox=[485, 654, 514, 668]
2026-08-05 11:04:24,054 INFO     29 [qwen-vl-text] coord item[36]: text=医师签名: 赵海国, bbox=[840, 682, 916, 697]
2026-08-05 11:04:24,054 INFO     29 [qwen-vl-text] coord item[37]: text=第1页, bbox=[690, 754, 713, 767]
2026-08-05 11:04:24,055 INFO     29 [qwen-vl-text] page=27 — 38/38 coords, api_time=12.8s
2026-08-05 11:04:24,055 INFO     29 [qwen-vl-text] new_positions (38):
[[27, 702.228, 717.384, 147.56, 157.07999999999998], [27, 552.352, 633.184, 129.11499999999998, 139.23], [27, 199.554, 216.394, 76.755, 84.49], [27, 54.73, 147.35, 161.84, 170.765], [27, 54.73, 133.878, 189.80499999999998, 198.73], [27, 54.73, 140.614, 218.36499999999998, 226.695], [27, 54.73, 140.614, 246.32999999999998, 255.255], [27, 54.73, 138.93, 274.89, 283.815], [27, 54.73, 140.614, 303.45, 311.78], [27, 54.73, 138.93, 331.41499999999996, 339.745], [27, 54.73, 140.614, 359.97499999999997, 368.305], [27, 54.73, 138.93, 387.94, 396.865], [27, 54.73, 140.614, 416.5, 424.83], [27, 54.73, 145.666, 443.87, 452.79499999999996], [27, 408.37, 427.736, 189.20999999999998, 198.135], [27, 520.356, 550.668, 189.20999999999998, 198.135], [27, 586.874, 620.554, 189.20999999999998, 198.135], [27, 671.074, 708.9639999999999, 189.20999999999998, 198.135], [27, 408.37, 461.416, 204.67999999999998, 213.605], [27, 520.356, 547.3, 204.67999999999998, 213.605], [27, 671.074, 737.592, 204.67999999999998, 213.605], [27, 408.37, 435.31399999999996, 220.14999999999998, 229.075], [27, 671.074, 719.068, 220.14999999999998, 229.075], [27, 408.37, 505.2, 235.61999999999998, 244.545], [27, 520.356, 617.1859999999999, 235.61999999999998, 244.545], [27, 649.182, 671.074, 235.61999999999998, 244.545], [27, 408.37, 468.99399999999997, 251.08999999999997, 260.015], [27, 408.37, 769.588, 266.56, 282.625], [27, 408.37, 457.20599999999996, 289.765, 298.09499999999997], [27, 408.37, 452.996, 304.64, 313.565], [27, 408.37, 765.3779999999999, 319.515, 328.44], [27, 408.37, 488.35999999999996, 327.84499999999997, 336.77], [27, 408.37, 443.734, 342.71999999999997, 351.645], [27, 408.37, 504.358, 358.78499999999997, 367.115], [27, 408.37, 554.036, 373.65999999999997, 382.585], [27, 408.37, 432.788, 389.13, 397.46], [27, 707.28, 771.2719999999999, 405.78999999999996, 414.715], [27, 580.98, 600.346, 448.63, 456.36499999999995]]
2026-08-05 11:04:24,055 INFO     29 [qwen-vl-text] ═══ DONE ═══ 38 positions, pages=1, time=15.4s
2026-08-05 11:04:24,055 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 11:04:24,055 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 11:04:24,055 INFO     29 [qwen-vl-text] positions(84): [[28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [28, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0], [29, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 11:04:24,056 INFO     29 [qwen-vl-text] page grouping: [28, 29], lines per page: [45, 39]
2026-08-05 11:04:24,380 INFO     29 [qwen-vl-text] page=28, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 11:04:24,750 INFO     29 [qwen-vl-text] page=29, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 11:04:24,752 INFO     29 [qwen-vl-text] LLM extraction start, text_len=2905
2026-08-05 11:04:24,752 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 11:04:24,752 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 1722, \"bbox_end\": 1805, \"encounter_dates\": [\"2026-01-06\"], \"department\": \"妇科一病区(门)\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "姓名：\n性别：女\n年龄：41岁\n民族：汉族\n婚姻状况：已婚\n身份证号\n职业：专业技术人员\n现住址\n就诊类型：初诊\n就诊科室：妇科一病区(门)\n就诊日期：2026-01-06 08:36\n联系电话.\n主诉：左下腹间断疼痛1年左右来诊\n现病史：患者诉于2024年01月05日无明显诱因出现下腹持续疼痛行相关检查后诊断为盆腔炎性疾病后遗症，\n慢性盆腔痛，药物治疗后好转，慢性盆腔痛病程12月，目前疾病状态持续，未治疗。\n既往史：2025年11月24日-2025年12月12日本院儿科门诊就诊代家属开药，否认3个月内其他病史及合并用药/\n非药物治疗，现患者无盆腔炎性疾病急性发作，否认既往有子宫肌瘤、子宫内膜异位症、子宫腺肌病、结核性\n盆腔炎、间质性膀胱炎、异常子宫出血、盆腔淤血综合征、子宫颈高级别上皮内病变等其他病症引起相关症状\n者；未放置宫内节育器；无子宫及双侧附件缺如；近2周内未使用过本方案规定研究期间禁止使用的治疗（包括\n药物和非药物治疗）；无控制不稳定的心血管、肝、肾和血液系统、糖尿病、甲状腺疾病等严重原发性疾病；\n获得知情同意书前5年内未患有恶性肿瘤；否认对试验用药品过敏，包括对本品成分或者药物辅料有过敏史；否\n认长期酗酒、药物滥用史；无智力障碍或精神障碍；近1个月内未参加过任何干预性临床试验；患者当前不在妊\n娠期、哺乳期，同意在试验期间及试验结束后3个月内采取有效避孕措施。\n婚育史：已婚已育，孕2产2，有性生活史\n手术史：2016年8月31日、2020年7月9日因生产行剖宫产手术\n月经史：初潮12岁，既往月经周期规律，经量中，色红，无痛经，末次月经2025.12.29-2025.1.2，周期26-\n28天，经期5天，经量较前不变\n过敏史：无\n生命体征：2026.1.6测量身高：160.0cm 体重：51.0kg 体温：36.4℃ 脉搏：76次/分 呼吸：18次/分 血压：\n98/76mmHg\n体格检查：淋巴结、头颈部、胸部、脊柱/四肢/关节、神经系统未见异常，腹部异常（左下腹压痛，CS，研究\n疾病相关），皮肤黏膜异常（腹部皮肤约5-6cm剖宫产手术瘢痕，NCS），其他未查。\n专科检查：外阴已婚型，阴道畅，宫颈光滑，无摇举痛，有宫体压痛，无子宫活动受限或粘连固定，左侧附件\n区、右侧附件区压痛，无宫骶韧带增粗、变硬、触痛。\n辅助检查：今日按方案要求开具血常规、尿沉渣（含尿常规）、肝功八项、肾功两项、血妊娠、血沉、血清C -\n125、妇科微生态、十二导联心电图、妇科阴道彩色B超检查，结果详见检查单。\n初步印象：盆腔痛中医辨证：主症：下腹胀痛，腰骶部胀痛、带下量多；次症：神疲乏力、口苦口腻、小便\n黄；舌象：舌质红、苔黄腻；脉象：脉弦滑；2026年01月06日由张丹丹医生辨证为湿热瘀阻症。 西医：盆腔炎\n性疾病后遗症，慢性盆腔痛\n处理意见：根据目前临床表现及患者情况，权丽丽医生于2026年01月06日08时38分在9号楼4楼医患沟通室向患\n绍“妇科千金片治疗盆腔炎性疾病后遗症（湿热瘀阻证）的随机、双盲、安慰剂平行对照、多中心临\n床试验”及知情同意书内容，已告知参加试验可能的风险与获益，患者已充分理解并同意参加该研究，未提出\n门\nCS 扫描全能王\n3亿人都在用的扫描App\n既往史：2025年11月24日-2025年12月12日本院儿科门诊就诊代家属开药，否认3个月内其他病史及合并用药/\n非药物治疗，现患者无盆腔炎性疾病急性发作，否认既往有子宫肌瘤、子宫内膜异位症、子宫腺肌病、结核性\n盆腔炎、间质性膀胱炎、异常子宫出血、盆腔淤血综合征、子宫颈高级别上皮内病变等其他病症引起相关症状\n者；未放置宫内节育器；无子宫及双侧附件缺如；近2周内未使用过本方案规定研究期间禁止使用的治疗（包括\n药物和非药物治疗）；无控制不稳定的心血管、肝、肾和血液系统、糖尿病、甲状腺疾病等严重原发性疾病；\n获得知情同意书前5年内未患有恶性肿瘤；否认对试验用药品过敏，包括对本品成分或者药物辅料有过敏史；否\n认长期酗酒、药物滥用史；无智力障碍或精神障碍；近1个月内未参加过任何干预性临床试验；患者当前不在妊\n娠期、哺乳期，同意在试验期间及试验结束后3个月内采取有效避孕措施。\n婚育史：已婚已育，孕2产2，有性生活史\n手术史：2016年8月31日、2020年7月9日因生产行剖宫产手术\n月经史：初潮12岁，既往月经周期规律，经量中，色红，无痛经，末次月经2025.12.29-2025.1.2，周期26-\n28天，经期5天，经量较前不变\n过敏史：无\n生命体征：2026.1.6测量身高：160.0cm 体重：51.0kg 体温：36.4℃ 脉搏：76次/分 呼吸：18次/分 血压：\n98/76mmHg\n体格检查：淋巴结、头颈部、胸部、脊柱/四肢/关节、神经系统未见异常，腹部异常（左下腹压痛，CS，研究\n疾病相关），皮肤黏膜异常（腹部皮肤约5-6cm剖宫产手术瘢痕，NCS），其他未查。\n专科检查：外阴已婚型，阴道畅，宫颈光滑，无摇举痛，有宫体压痛，无子宫活动受限或粘连固定，左侧附件\n区、右侧附件区压痛，无宫骶韧带增粗、变硬、触痛。\n辅助检查：今日按方案要求开具血常规、尿沉渣（含尿常规）、肝功八项、肾功两项、血妊娠、血沉、血清CA-\n125、妇科微生态、十二导联心电图、妇科阴道彩色B超检查，结果详见检查单。\n初步印象：盆腔痛中医辨证：主症：下腹胀痛，腰骶部胀痛、带下量多；次症：神疲乏力、口苦口腻、小便\n黄；舌象：舌质红、苔黄腻；脉象：脉弦滑；2026年01月06日由张丹丹医生辨证为湿热瘀阻症。 西医：盆腔炎\n性疾病后遗症，慢性盆腔痛\n从细之间、根据目前临床表现及患者情况，权丽丽医生于2026年01月06日08时38分在9号楼4楼医患沟通室向患\n者\n引“妇科千金片治疗盆腔炎性疾病后遗症（湿热瘀阻证）的随机、双盲、安慰剂平行对照、多中心临\n床试验”及知情同意书内容，已告知参加试验可能的风险与获益，患者已充分理解并同意参加该研究，未提出\n问题，患者本人于2026年01月06日08时58分签署知情同意书（版本号：V1.0 三门峡市中心医院专用版，版本日\n期：2025年08月05日），权丽丽医生于2026年01月06日08时59分签署知情同意书（版本号：V1.0 三门峡市中心\n医院专用版，版本日期：2025年08月05日），知情同意书原件一份保存于受试者文件夹，一份交给患者本人，\n确定患者筛选号为04011，进入试验筛选，根据方案要求，收集受试者的试验相关资料，并于今日开始进行筛选\n期相关检查。\n1.已完成体征McCormack量表评分，总分8分，回顾近1周非经期腹痛/腰骶疼痛NRS平均分为5分。\n2.嘱受试者合理饮食，避免过度劳累；避免盆浴和坐浴，避免穿紧身衣物和化纤内裤；注意经期卫生。\n3.今日结合受试者情况，2026年1月6日血清CA-125示：59.70（0.00-35.00）U/mL，符合排除标准第（8）条，\n筛选失败，告知受试者转为门诊常规诊疗。\n备注：\n医师签名：",
    "role": "user"
  }
]
[92m11:04:24 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:04:24,754 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 11:04:27,021 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T11:04:27.020+00:00", "boot_at": "2026-08-05T09:49:31.242+00:00", "pending": 7, "lag": 0, "done": 2, "failed": 0, "current": {"39f0723890bb11f1a3da71efcdd7cc1f": {"id": "39f0723890bb11f1a3da71efcdd7cc1f", "doc_id": "399fea9890bb11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785926923057, "task_type": "dataflow", "root_trace_id": "01bb94e6e4fc42e7a4a0ce91ffec33b6", "root_traceparent": "00-01bb94e6e4fc42e7a4a0ce91ffec33b6-2def99fbd844a555-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 11:04:31,596 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 11:04:31,596 INFO     29 [qwen-vl-text] LLM output (len=841):
{
  "encounter_date": "2026-01-06",
  "chief_complaint": "左下腹间断疼痛1年左右来诊",
  "present_illness": "患者诉于2024年01月05日无明显诱因出现下腹持续疼痛行相关检查后诊断为盆腔炎性疾病后遗症，慢性盆腔痛，药物治疗后好转，慢性盆腔痛病程12月，目前疾病状态持续，未治疗。",
  "past_history": "2025年11月24日-2025年12月12日本院儿科门诊就诊代家属开药，否认3个月内其他病史及合并用药/非药物治疗，现患者无盆腔炎性疾病急性发作，否认既往有子宫肌瘤、子宫内膜异位症、子宫腺肌病、结核性盆腔炎、间质性膀胱炎、异常子宫出血、盆腔淤血综合征、子宫颈高级别上皮内病变等其他病症引起相关症状者；未放置宫内节育器；无子宫及双侧附件缺如；近2周内未使用过本方案规定研究期间禁止使用的治疗（包括药物和非药物治疗）；无控制不稳定的心血管、肝、肾和血液系统、糖尿病、甲状腺疾病等严重原发性疾病；获得知情同意书前5年内未患有恶性肿瘤；否认对试验用药品过敏，包括对本品成分或者药物辅料有过敏史；否认长期酗酒、药物滥用史；无智力障碍或精神障碍；近1个月内未参加过任何干预性临床试验；患者当前不在妊娠期、哺乳期，同意在试验期间及试验结束后3个月内采取有效避孕措施。手术史：2016年8月31日、2020年7月9日因生产行剖宫产手术。过敏史：无。",
  "diagnosis": "西医：盆腔炎性疾病后遗症，慢性盆腔痛；中医：湿热瘀阻证",
  "treatment_plan": "患者签署“妇科千金片治疗盆腔炎性疾病后遗症（湿热瘀阻证）的随机、双盲、安慰剂平行对照、多中心临床试验”知情同意书，进入试验筛选。因血清CA-125示59.70U/mL符合排除标准，筛选失败，转为门诊常规诊疗。嘱受试者合理饮食，避免过度劳累；避免盆浴和坐浴，避免穿紧身衣物和化纤内裤；注意经期卫生。"
}
2026-08-05 11:04:31,596 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-06]
2026-08-05 11:04:31,600 INFO     29 [qwen-vl-text] coord API call start, page=28, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1868136, prompt_len=2101
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共45行）
["姓名：", "性别：女", "年龄：41岁", "民族：汉族", "婚姻状况：已婚", "身份证号", "职业：专业技术人员", "现住址", "就诊类型：初诊", "就诊科室：妇科一病区(门)", "就诊日期：2026-01-06 08:36", "联系电话.", "主诉：左下腹间断疼痛1年左右来诊", "现病史：患者诉于2024年01月05日无明显诱因出现下腹持续疼痛行相关检查后诊断为盆腔炎性疾病后遗症，", "慢性盆腔痛，药物治疗后好转，慢性盆腔痛病程12月，目前疾病状态持续，未治疗。", "既往史：2025年11月24日-2025年12月12日本院儿科门诊就诊代家属开药，否认3个月内其他病史及合并用药/", "非药物治疗，现患者无盆腔炎性疾病急性发作，否认既往有子宫肌瘤、子宫内膜异位症、子宫腺肌病、结核性", "盆腔炎、间质性膀胱炎、异常子宫出血、盆腔淤血综合征、子宫颈高级别上皮内病变等其他病症引起相关症状", "者；未放置宫内节育器；无子宫及双侧附件缺如；近2周内未使用过本方案规定研究期间禁止使用的治疗（包括", "药物和非药物治疗）；无控制不稳定的心血管、肝、肾和血液系统、糖尿病、甲状腺疾病等严重原发性疾病；", "获得知情同意书前5年内未患有恶性肿瘤；否认对试验用药品过敏，包括对本品成分或者药物辅料有过敏史；否", "认长期酗酒、药物滥用史；无智力障碍或精神障碍；近1个月内未参加过任何干预性临床试验；患者当前不在妊", "娠期、哺乳期，同意在试验期间及试验结束后3个月内采取有效避孕措施。", "婚育史：已婚已育，孕2产2，有性生活史", "手术史：2016年8月31日、2020年7月9日因生产行剖宫产手术", "月经史：初潮12岁，既往月经周期规律，经量中，色红，无痛经，末次月经2025.12.29-2025.1.2，周期26-", "28天，经期5天，经量较前不变", "过敏史：无", "生命体征：2026.1.6测量身高：160.0cm 体重：51.0kg 体温：36.4℃ 脉搏：76次/分 呼吸：18次/分 血压：", "98/76mmHg", "体格检查：淋巴结、头颈部、胸部、脊柱/四肢/关节、神经系统未见异常，腹部异常（左下腹压痛，CS，研究", "疾病相关），皮肤黏膜异常（腹部皮肤约5-6cm剖宫产手术瘢痕，NCS），其他未查。", "专科检查：外阴已婚型，阴道畅，宫颈光滑，无摇举痛，有宫体压痛，无子宫活动受限或粘连固定，左侧附件", "区、右侧附件区压痛，无宫骶韧带增粗、变硬、触痛。", "辅助检查：今日按方案要求开具血常规、尿沉渣（含尿常规）、肝功八项、肾功两项、血妊娠、血沉、血清C -", "125、妇科微生态、十二导联心电图、妇科阴道彩色B超检查，结果详见检查单。", "初步印象：盆腔痛中医辨证：主症：下腹胀痛，腰骶部胀痛、带下量多；次症：神疲乏力、口苦口腻、小便", "黄；舌象：舌质红、苔黄腻；脉象：脉弦滑；2026年01月06日由张丹丹医生辨证为湿热瘀阻症。 西医：盆腔炎", "性疾病后遗症，慢性盆腔痛", "处理意见：根据目前临床表现及患者情况，权丽丽医生于2026年01月06日08时38分在9号楼4楼医患沟通室向患", "绍“妇科千金片治疗盆腔炎性疾病后遗症（湿热瘀阻证）的随机、双盲、安慰剂平行对照、多中心临", "床试验”及知情同意书内容，已告知参加试验可能的风险与获益，患者已充分理解并同意参加该研究，未提出", "门", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
```
