# 基准结果：lsju-哮喘-沈阳(1).pdf

## 基本信息

- 文件：`lsju-哮喘-沈阳(1).pdf`
- 大小：6468.1 KB
- PDF 总页数：9
- doc_id：`5ddcc2a094ad11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T19:19:34  完成时间：2026-08-10T19:22:06  耗时：151.9s
- progress_msg：`11:22:02 Indexing done (0.08s). Task done (141.01s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | cc0a66e8 | 1 | 3-3 | 北票成岩中医院 门诊病历 科别：内科门诊 姓名 性别：女 年龄：57岁 门诊号： |
| 2 | 9c98c38c | 2 | 4-5 | 病历记录 以下为中国医科大学附属第一医院门（急）诊病历记录 2021年10月11 |
| 3 | d78a8083 | 1 | 6-6 | 订单详情 完成 建议您关注病情进展并及时复诊 去复诊 > 再次购买 已签收 您的 |
| 4 | 0745d108 | 3 | 6-8 | 查看发票 再次购买 13:19 5G 49 < 哮喘用药热卖榜第4名 85*** |
| 5 | 18fc07d8 | 1 | 9-9 | 芳草大药房(孤岛路店) 欢迎光临 顾客姓名: 流水号: 001LS2025120 |
| 6 | 38c5b15f | 1 | 9-9 | 芳草大药房(孤岛路店) 欢迎光临 顾客姓名: 流水号: 001LS2025123 |

- chunks 总数：6
- 各 chunk 页数合计（含跨页重复）：9
- 页码并集：`[3, 4, 5, 6, 7, 8, 9]`
- 覆盖页数：7 / 9；缺失页：`[1, 2]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：❌ 未完全覆盖：覆盖 7/9 页，缺失 [1, 2]，超范围 []**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 2 | 0 | 2 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 4 | 4 | 4 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 0 | 1 | 0 | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 0 | 0 | 0 | report_time, report_category, report_name | **-** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 2, "MedicationRecord": 4}`
- ChunkMerger：`{"found": true, "merged": 6, "sources": 9, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 2, "Extractor:Medication": 4, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1, "Extractor:Progress": 1}, "filtered_noise": 7}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 11:22:01,224 INFO     29 [ChunkMerger] Merged 6 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 4, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 11:19:35,908 INFO     29 handle_task begin for task {"id": "5e62f0e694ad11f1bd9827cf206dfa2d", "doc_id": "5ddcc2a094ad11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "lsju-\u54ee\u5598-\u6c88\u9633(1).pdf", "type": "pdf", "location": "lsju-\u54ee\u5598-\u6c88\u9633(1).pdf", "size": 3913176, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786360775902, "task_type": "dataflow", "root_trace_id": "7d6dcbad8e7b45c1949a5dd052ab4409", "root_traceparent": "00-7d6dcbad8e7b45c1949a5dd052ab4409-9207ab8c386eb81c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 11:19:36,225 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 11:19:36,352 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 11:19:36,364 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:19:36,364 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 11:19:36,364 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 11:19:36,374 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 11:19:36,374 INFO     29 ============================================================
2026-08-10 11:19:36,374 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 11:19:36,374 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 11:19:36,374 INFO     29 ============================================================
2026-08-10 11:19:36,375 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 11:19:36,375 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 11:19:36,376 INFO     29 No torch found.
2026-08-10 11:19:37,279 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=9
2026-08-10 11:19:37,630 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2491324, prompt_len=764
2026-08-10 11:19:38,891 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:19:38,891 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 11:19:38,901 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2491324, prompt_len=401
2026-08-10 11:19:39,733 INFO     29 [qwen-vl-parser] text API response (len=52):
["病例记录", "科别：", "主诉：", "现病史：一", "既往史：", "体格检查：", ""]
2026-08-10 11:19:39,734 INFO     29 [qwen-vl-parser] page=1 text: 6 lines (bbox 0-5)
2026-08-10 11:19:39,734 INFO     29 [qwen-vl-parser] page=1 text: 6 sections
2026-08-10 11:19:40,121 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2278609, prompt_len=764
2026-08-10 11:19:41,408 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:19:41,409 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 11:19:41,419 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2278609, prompt_len=401
2026-08-10 11:19:42,095 INFO     29 [qwen-vl-parser] text API response (len=51):
["病例记录", "辅助检查：", "诊断：", "处理意见：", "医生签名：", "医生盖章："]
2026-08-10 11:19:42,096 INFO     29 [qwen-vl-parser] page=2 text: 6 lines (bbox 6-11)
2026-08-10 11:19:42,096 INFO     29 [qwen-vl-parser] page=2 text: 6 sections
2026-08-10 11:19:42,257 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1134905, prompt_len=764
2026-08-10 11:19:43,710 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:19:43,711 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 11:19:43,725 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1134905, prompt_len=401
2026-08-10 11:19:48,477 INFO     29 [qwen-vl-parser] text API response (len=566):
["北票成岩中医院", "门诊病历", "科别：内科门诊 姓名", "性别：女 年龄：57岁 门诊号：7260295", "职业：农民 婚姻：已婚", "药物过敏史：无", "住址：辽宁省朝阳市凌源市宋杖子镇马杖子", "纪录时间：2026-02-10 09:15", "主诉：反复发作咳嗽喘息5年余、加重5天", "现病史：患者2020年6月于中国医科大学附属第一医院诊断为支气管哮喘，后规律使用布", "地奈德福莫特罗吸入粉雾剂（II）320μg:9μg，1日/2吸。5天前患者受凉后出", "现咳嗽喘息症状加重，无发热，日常活动受限，为求进一步诊治来我院。", "既往史：支气管哮喘病史5年余。", "过敏史：花粉过敏", "传染病及流行性病史：无", "查体：T36.7℃，P82次/分，R24次/分，BP 125/80 mmHg。双肺呼吸音粗，可闻及广泛呼", "气相哮鸣音，未闻及湿性啰音。", "辅助检查：", "初步诊断：支气管哮喘（急性发作期）", "诊疗意见：1.醋酸泼尼松片20mg日1次口服，连续用5天。", "2.沙丁胺醇气雾剂2喷/次，每4小时1次，症状缓解后改为按需吸入。", "3.布地奈德福莫特罗吸入粉雾剂（II）320μg:9μg,1日/2吸规律吸入", "医师签名：", "日期：2026年"]
2026-08-10 11:19:48,478 INFO     29 [qwen-vl-parser] page=3 text: 24 lines (bbox 12-35)
2026-08-10 11:19:48,478 INFO     29 [qwen-vl-parser] page=3 text: 24 sections
2026-08-10 11:19:48,834 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1981236, prompt_len=764
2026-08-10 11:19:50,119 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2021-10-11"}
```
2026-08-10 11:19:50,119 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=2021-10-11
2026-08-10 11:19:50,128 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1981236, prompt_len=401
2026-08-10 11:19:51,537 INFO     29 [qwen-vl-parser] text API response (len=185):
["病历记录", "以下为中国医科大学附属第一医院门（急）诊病历记录 2021年10月11日 时 分", "主诉：反复喘息3年余", "现病史：曾于2020年6月到我院就诊，诊断“支气管哮喘”，", "目前仍有气短症状，规律使用可必特吸入", "日二次吸入，强的松2片日一次口服", "既往史：花粉过敏", "家庭史：0", "体格检查：2021年0平气相喘鸣(+)"]
2026-08-10 11:19:51,538 INFO     29 [qwen-vl-parser] page=4 text: 9 lines (bbox 36-44)
2026-08-10 11:19:51,538 INFO     29 [qwen-vl-parser] page=4 text: 9 sections
2026-08-10 11:19:51,835 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1852957, prompt_len=764
2026-08-10 11:19:53,066 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:19:53,067 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 11:19:53,086 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1852957, prompt_len=401
2026-08-10 11:19:54,755 INFO     29 [qwen-vl-parser] text API response (len=230):
["病历记录", "胸CT(外院)3.221年较前透亮度降低", "余未见确切异常", "查肺功+舒张+弥散", "血气", "白常规.0嗜碱细胞296", "血气PH7.395.P0266.9P0241.5", "肺功:弥散正常", "FVC48.6%FEV1.301%", "舒张41.6%FEV1.072", "病历记录", "叩诊:支气管哮鸣(重度)", "低氧血症", "建议:住院320ug吸入二次吸入", "待化验结果", "苏新明", "3"]
2026-08-10 11:19:54,755 INFO     29 [qwen-vl-parser] page=5 text: 17 lines (bbox 45-61)
2026-08-10 11:19:54,755 INFO     29 [qwen-vl-parser] page=5 text: 17 sections
2026-08-10 11:19:54,942 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1137821, prompt_len=764
2026-08-10 11:19:56,906 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:19:56,907 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-10 11:19:56,920 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1137821, prompt_len=401
2026-08-10 11:19:59,032 INFO     29 [qwen-vl-parser] text API response (len=363):
["19:01", "5G 28", "订单详情", "完成", "建议您关注病情进展并及时复诊 去复诊 >", "再次购买", "已签收", "您的预约单已签收", "185****3662", "辽宁朝阳市凌源市宋杖子镇马杖子", "京东大药房", "联系", "满意度调研", "药品不支持7天无理由退换货", "京东买药", "仙琚 醋酸泼尼松片 5mg*100片", "数量：1", "¥6.90/件", "品质保障", "多仓发货", "正品好药", "极速发货", "专业药师服务", "用药人信息", "刘素娟 女 57岁", "问诊单", "查看详情 >", "不良反应登记 京东大药房执业药师提示：合格药品在正常", "点击查看您的用药指导", "去看看", "删除订单", "查看发票", "再次购买"]
2026-08-10 11:19:59,033 INFO     29 [qwen-vl-parser] page=6 text: 33 lines (bbox 62-94)
2026-08-10 11:19:59,033 INFO     29 [qwen-vl-parser] page=6 text: 33 sections
2026-08-10 11:19:59,218 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1210601, prompt_len=764
2026-08-10 11:20:01,684 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:20:01,685 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-10 11:20:01,702 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1210601, prompt_len=401
2026-08-10 11:20:02,307 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:20:02.306+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 20, "failed": 0, "current": {"5e62f0e694ad11f1bd9827cf206dfa2d": {"id": "5e62f0e694ad11f1bd9827cf206dfa2d", "doc_id": "5ddcc2a094ad11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "lsju-\u54ee\u5598-\u6c88\u9633(1).pdf", "type": "pdf", "location": "lsju-\u54ee\u5598-\u6c88\u9633(1).pdf", "size": 3913176, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786360775902, "task_type": "dataflow", "root_trace_id": "7d6dcbad8e7b45c1949a5dd052ab4409", "root_traceparent": "00-7d6dcbad8e7b45c1949a5dd052ab4409-9207ab8c386eb81c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:20:04,887 INFO     29 [qwen-vl-parser] text API response (len=579):
["13:19", "5G 49", "<", "哮喘用药热卖榜第4名", "85****3662", "自营 京东自营药房", "普通内科处方单131900332246895 距失效还剩71:59:43", "京东买药 AstraZeneca", "【原研进口】信必可 布地奈德福莫特...", "1", "+", "原研正品", "多仓发货", "品质保障", "适3盒装 有金特贴到手价", "220", "元", "320", "1盒装(体验/应急装)", "不支持7天无理由退货", "¥249", "服务", "可选一年囤货补贴共5项 >", "配送", "京东快递 >", "2月25日 [周三] 09:00-21:00", "收货方式", "送货上门 >", "顺手买更划算 ①", "抑菌洗手液倍护滋润保湿持久留香", "450克*1瓶【体验装】", "80%用户顺手买过", "Weichi", "HAND SANITIZER", "抑菌洗手液", "净含量:450克", "¥2.9 专享价 ¥7.5", "省4.60元", "一键购买", "查看更多推荐 v", "商品金额", "¥249.00", "运费", "¥0.00", "优惠券", "无可用 >", "已隐藏本单不可使用的虚拟资产 v", "提交订单 ¥249.00"]
2026-08-10 11:20:04,888 INFO     29 [qwen-vl-parser] page=7 text: 47 lines (bbox 95-141)
2026-08-10 11:20:04,889 INFO     29 [qwen-vl-parser] page=7 text: 47 sections
2026-08-10 11:20:04,972 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=485362, prompt_len=764
2026-08-10 11:20:06,317 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:20:06,317 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=None
2026-08-10 11:20:06,328 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=485362, prompt_len=401
2026-08-10 11:20:09,087 INFO     29 [qwen-vl-parser] text API response (len=477):
["电子发票(普通发票)", "国家税务总局", "辽宁省税务局", "发票号码: 26217000000097645604", "开票日期: 2026年02月25日", "购买方信息", "名称: 个人", "统一社会信用代码/纳税人识别号:", "销售方信息", "名称: 京东大药房(沈阳)有限公司", "统一社会信用代码/纳税人识别号: 91210112MA10499C0F", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*化学药品制剂*【原研进口】信必可布地奈德福莫特罗吸入粉雾剂(II) 320μg:9μg*60吸/盒", "布地奈德福莫特罗吸入粉雾剂(II)", "盒", "1", "220.35", "220.35", "13%", "28.65", "合计", "¥220.35", "¥28.65", "价税合计(大写)", "贰佰肆拾玖圆整", "(小写) ¥249.00", "备注", "订单号:3419204018592466", "开票人: 王梅"]
2026-08-10 11:20:09,088 INFO     29 [qwen-vl-parser] page=8 text: 36 lines (bbox 142-177)
2026-08-10 11:20:09,088 INFO     29 [qwen-vl-parser] page=8 text: 36 sections
2026-08-10 11:20:09,751 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3738987, prompt_len=764
2026-08-10 11:20:11,338 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:20:11,341 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-10 11:20:11,363 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3738987, prompt_len=401
2026-08-10 11:20:15,223 INFO     29 [qwen-vl-parser] text API response (len=597):
["芳草大药房(孤岛路店)", "欢迎光临", "顾客姓名:", "流水号:", "001LS202512010064", "品名 数量 单价 小计", "布地奈德福莫特罗吸入粉雾剂(Ⅱ)", "1 244.0 244.0", "P202504 2028-03", "规格: 320ug:9ug*60吸", "厂家: AstraZeneca AB", "总计: 244.00 件数: 1", "累计折扣: 0.00", "实收: 244.00", "收来: 250.00 找还: 6.00", "收款人: 00015", "2025/12/01 09:11:26", "除药品质量原因不得退换", "芳草大药房(孤岛路店)", "欢迎光临", "顾客姓名:", "流水号:", "001LS202512301135", "品名 数量 单价 小计", "布地奈德福莫特罗吸入粉雾剂(Ⅱ)", "2 244.0 488.0", "P202504 2028-03", "规格: 320ug:9ug*60吸", "厂家: AstraZeneca AB", "总计: 488.00 件数: 2", "累计折扣: 0.00", "实收: 488.00", "收来: 500.00 找还: 12.00", "收款人: 00015", "2025/12/30 18:04:32", "除药品质量原因不得退换"]
2026-08-10 11:20:15,225 INFO     29 [qwen-vl-parser] page=9 text: 36 lines (bbox 178-213)
2026-08-10 11:20:15,225 INFO     29 [qwen-vl-parser] page=9 text: 36 sections
2026-08-10 11:20:15,225 INFO     29 [qwen-vl-parser] parse_pdf done: 214 sections from 9 pages.
2026-08-10 11:20:15,236 INFO     29 Close text detector.
2026-08-10 11:20:15,678 INFO     29 Close text recognizer.
2026-08-10 11:20:16,095 INFO     29 Close recognizer.
2026-08-10 11:20:16,517 INFO     29 Close recognizer.
2026-08-10 11:20:17,000 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 11:20:17,001 INFO     29 [Trace] task=5e62f0e6 | doc=lsju-哮喘-沈阳(1).pdf | Parser:MedLink | outputs={"html": "", "json": "214 items", "markdown": "", "text": "", "name": "lsju-哮喘-沈阳(1).pdf", "output_format": "json"}
2026-08-10 11:20:17,001 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 11:20:17,047 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:20:17,047 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 病例记录\n[BBOX-1] 科别：\n[BBOX-2] 主诉：\n[BBOX-3] 现病史：一\n[BBOX-4] 既往史：\n[BBOX-5] 体格检查：\n[BBOX-6] 病例记录\n[BBOX-7] 辅助检查：\n[BBOX-8] 诊断：\n[BBOX-9] 处理意见：\n[BBOX-10] 医生签名：\n[BBOX-11] 医生盖章：\n[BBOX-12] 北票成岩中医院\n[BBOX-13] 门诊病历\n[BBOX-14] 科别：内科门诊 姓名\n[BBOX-15] 性别：女 年龄：57岁 门诊号：7260295\n[BBOX-16] 职业：农民 婚姻：已婚\n[BBOX-17] 药物过敏史：无\n[BBOX-18] 住址：辽宁省朝阳市凌源市宋杖子镇马杖子\n[BBOX-19] 纪录时间：2026-02-10 09:15\n[BBOX-20] 主诉：反复发作咳嗽喘息5年余、加重5天\n[BBOX-21] 现病史：患者2020年6月于中国医科大学附属第一医院诊断为支气管哮喘，后规律使用布\n[BBOX-22] 地奈德福莫特罗吸入粉雾剂（II）320μg:9μg，1日/2吸。5天前患者受凉后出\n[BBOX-23] 现咳嗽喘息症状加重，无发热，日常活动受限，为求进一步诊治来我院。\n[BBOX-24] 既往史：支气管哮喘病史5年余。\n[BBOX-25] 过敏史：花粉过敏\n[BBOX-26] 传染病及流行性病史：无\n[BBOX-27] 查体：T36.7℃，P82次/分，R24次/分，BP 125/80 mmHg。双肺呼吸音粗，可闻及广泛呼\n[BBOX-28] 气相哮鸣音，未闻及湿性啰音。\n[BBOX-29] 辅助检查：\n[BBOX-30] 初步诊断：支气管哮喘（急性发作期）\n[BBOX-31] 诊疗意见：1.醋酸泼尼松片20mg日1次口服，连续用5天。\n[BBOX-32] 2.沙丁胺醇气雾剂2喷/次，每4小时1次，症状缓解后改为按需吸入。\n[BBOX-33] 3.布地奈德福莫特罗吸入粉雾剂（II）320μg:9μg,1日/2吸规律吸入\n[BBOX-34] 医师签名：\n[BBOX-35] 日期：2026年\n[BBOX-36] 病历记录\n[BBOX-37] 以下为中国医科大学附属第一医院门（急）诊病历记录 2021年10月11日 时 分\n[BBOX-38] 主诉：反复喘息3年余\n[BBOX-39] 现病史：曾于2020年6月到我院就诊，诊断“支气管哮喘”，\n[BBOX-40] 目前仍有气短症状，规律使用可必特吸入\n[BBOX-41] 日二次吸入，强的松2片日一次口服\n[BBOX-42] 既往史：花粉过敏\n[BBOX-43] 家庭史：0\n[BBOX-44] 体格检查：2021年0平气相喘鸣(+)\n[BBOX-45] 病历记录\n[BBOX-46] 胸CT(外院)3.221年较前透亮度降低\n[BBOX-47] 余未见确切异常\n[BBOX-48] 查肺功+舒张+弥散\n[BBOX-49] 血气\n[BBOX-50] 白常规.0嗜碱细胞296\n[BBOX-51] 血气PH7.395.P0266.9P0241.5\n[BBOX-52] 肺功:弥散正常\n[BBOX-53] FVC48.6%FEV1.301%\n[BBOX-54] 舒张41.6%FEV1.072\n[BBOX-55] 病历记录\n[BBOX-56] 叩诊:支气管哮鸣(重度)\n[BBOX-57] 低氧血症\n[BBOX-58] 建议:住院320ug吸入二次吸入\n[BBOX-59] 待化验结果\n[BBOX-60] 苏新明\n[BBOX-61] 3\n[BBOX-62] 19:01\n[BBOX-63] 5G 28\n[BBOX-64] 订单详情\n[BBOX-65] 完成\n[BBOX-66] 建议您关注病情进展并及时复诊 去复诊 >\n[BBOX-67] 再次购买\n[BBOX-68] 已签收\n[BBOX-69] 您的预约单已签收\n[BBOX-70] 185****3662\n[BBOX-71] 辽宁朝阳市凌源市宋杖子镇马杖子\n[BBOX-72] 京东大药房\n[BBOX-73] 联系\n[BBOX-74] 满意度调研\n[BBOX-75] 药品不支持7天无理由退换货\n[BBOX-76] 京东买药\n[BBOX-77] 仙琚 醋酸泼尼松片 5mg*100片\n[BBOX-78] 数量：1\n[BBOX-79] ¥6.90/件\n[BBOX-80] 品质保障\n[BBOX-81] 多仓发货\n[BBOX-82] 正品好药\n[BBOX-83] 极速发货\n[BBOX-84] 专业药师服务\n[BBOX-85] 用药人信息\n[BBOX-86] 刘素娟 女 57岁\n[BBOX-87] 问诊单\n[BBOX-88] 查看详情 >\n[BBOX-89] 不良反应登记 京东大药房执业药师提示：合格药品在正常\n[BBOX-90] 点击查看您的用药指导\n[BBOX-91] 去看看\n[BBOX-92] 删除订单\n[BBOX-93] 查看发票\n[BBOX-94] 再次购买\n[BBOX-95] 13:19\n[BBOX-96] 5G 49\n[BBOX-97] <\n[BBOX-98] 哮喘用药热卖榜第4名\n[BBOX-99] 85****3662\n[BBOX-100] 自营 京东自营药房\n[BBOX-101] 普通内科处方单131900332246895 距失效还剩71:59:43\n[BBOX-102] 京东买药 AstraZeneca\n[BBOX-103] 【原研进口】信必可 布地奈德福莫特...\n[BBOX-104] 1\n[BBOX-105] 原研正品\n[BBOX-106] 多仓发货\n[BBOX-107] 品质保障\n[BBOX-108] 适3盒装 有金特贴到手价\n[BBOX-109] 220\n[BBOX-110] 元\n[BBOX-111] 320\n[BBOX-112] 1盒装(体验/应急装)\n[BBOX-113] 不支持7天无理由退货\n[BBOX-114] ¥249\n[BBOX-115] 服务\n[BBOX-116] 可选一年囤货补贴共5项 >\n[BBOX-117] 配送\n[BBOX-118] 京东快递 >\n[BBOX-119] 2月25日 [周三] 09:00-21:00\n[BBOX-120] 收货方式\n[BBOX-121] 送货上门 >\n[BBOX-122] 顺手买更划算 ①\n[BBOX-123] 抑菌洗手液倍护滋润保湿持久留香\n[BBOX-124] 450克*1瓶【体验装】\n[BBOX-125] 80%用户顺手买过\n[BBOX-126] Weichi\n[BBOX-127] HAND SANITIZER\n[BBOX-128] 抑菌洗手液\n[BBOX-129] 净含量:450克\n[BBOX-130] ¥2.9 专享价 ¥7.5\n[BBOX-131] 省4.60元\n[BBOX-132] 一键购买\n[BBOX-133] 查看更多推荐 v\n[BBOX-134] 商品金额\n[BBOX-135] ¥249.00\n[BBOX-136] 运费\n[BBOX-137] ¥0.00\n[BBOX-138] 优惠券\n[BBOX-139] 无可用 >\n[BBOX-140] 已隐藏本单不可使用的虚拟资产 v\n[BBOX-141] 提交订单 ¥249.00\n[BBOX-142] 电子发票(普通发票)\n[BBOX-143] 国家税务总局\n[BBOX-144] 辽宁省税务局\n[BBOX-145] 发票号码: 26217000000097645604\n[BBOX-146] 开票日期: 2026年02月25日\n[BBOX-147] 购买方信息\n[BBOX-148] 名称: 个人\n[BBOX-149] 统一社会信用代码/纳税人识别号:\n[BBOX-150] 销售方信息\n[BBOX-151] 名称: 京东大药房(沈阳)有限公司\n[BBOX-152] 统一社会信用代码/纳税人识别号: 91210112MA10499C0F\n[BBOX-153] 项目名称\n[BBOX-154] 规格型号\n[BBOX-155] 单位\n[BBOX-156] 数量\n[BBOX-157] 单价\n[BBOX-158] 金额\n[BBOX-159] 税率/征收率\n[BBOX-160] 税额\n[BBOX-161] *化学药品制剂*【原研进口】信必可布地奈德福莫特罗吸入粉雾剂(II) 320μg:9μg*60吸/盒\n[BBOX-162] 布地奈德福莫特罗吸入粉雾剂(II)\n[BBOX-163] 盒\n[BBOX-164] 1\n[BBOX-165] 220.35\n[BBOX-166] 220.35\n[BBOX-167] 13%\n[BBOX-168] 28.65\n[BBOX-169] 合计\n[BBOX-170] ¥220.35\n[BBOX-171] ¥28.65\n[BBOX-172] 价税合计(大写)\n[BBOX-173] 贰佰肆拾玖圆整\n[BBOX-174] (小写) ¥249.00\n[BBOX-175] 备注\n[BBOX-176] 订单号:3419204018592466\n[BBOX-177] 开票人: 王梅\n[BBOX-178] 芳草大药房(孤岛路店)\n[BBOX-179] 欢迎光临\n[BBOX-180] 顾客姓名:\n[BBOX-181] 流水号:\n[BBOX-182] 001LS202512010064\n[BBOX-183] 品名 数量 单价 小计\n[BBOX-184] 布地奈德福莫特罗吸入粉雾剂(Ⅱ)\n[BBOX-185] 1 244.0 244.0\n[BBOX-186] P202504 2028-03\n[BBOX-187] 规格: 320ug:9ug*60吸\n[BBOX-188] 厂家: AstraZeneca AB\n[BBOX-189] 总计: 244.00 件数: 1\n[BBOX-190] 累计折扣: 0.00\n[BBOX-191] 实收: 244.00\n[BBOX-192] 收来: 250.00 找还: 6.00\n[BBOX-193] 收款人: 00015\n[BBOX-194] 2025/12/01 09:11:26\n[BBOX-195] 除药品质量原因不得退换\n[BBOX-196] 芳草大药房(孤岛路店)\n[BBOX-197] 欢迎光临\n[BBOX-198] 顾客姓名:\n[BBOX-199] 流水号:\n[BBOX-200] 001LS202512301135\n[BBOX-201] 品名 数量 单价 小计\n[BBOX-202] 布地奈德福莫特罗吸入粉雾剂(Ⅱ)\n[BBOX-203] 2 244.0 488.0\n[BBOX-204] P202504 2028-03\n[BBOX-205] 规格: 320ug:9ug*60吸\n[BBOX-206] 厂家: AstraZeneca AB\n[BBOX-207] 总计: 488.00 件数: 2\n[BBOX-208] 累计折扣: 0.00\n[BBOX-209] 实收: 488.00\n[BBOX-210] 收来: 500.00 找还: 12.00\n[BBOX-211] 收款人: 00015\n[BBOX-212] 2025/12/30 18:04:32\n[BBOX-213] 除药品质量原因不得退换"
  }
]
2026-08-10 11:20:23,019 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:20:23,040 INFO     29 [SmartSplitter] SmartSplitter done: 6 chunks from 6 LLM segments (all bbox_id). Types: {'OutpatientRecord': 2, 'MedicationRecord': 4}
2026-08-10 11:20:23,055 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 11:20:23,055 INFO     29 [Trace] task=5e62f0e6 | doc=lsju-哮喘-沈阳(1).pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "214 items", "markdown": "", "text": "", "name": "lsju-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 2, 'MedicationRecord': 4}"}
2026-08-10 11:20:23,055 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 11:20:23,055 INFO     29 [ChunkRouter] Routed 6 chunks into 2 groups: {'chunks_Clinical': 2, 'chunks_Medication': 4}
2026-08-10 11:20:23,064 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 11:20:23,065 INFO     29 [Trace] task=5e62f0e6 | doc=lsju-哮喘-沈阳(1).pdf | ChunkRouter:Router | outputs={"html": "", "json": "214 items", "markdown": "", "text": "", "name": "lsju-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 2, 'MedicationRecord': 4}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-10 11:20:23,065 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 11:20:23,071 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:20:23,071 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:20:23,666 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:20:23,677 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 11:20:23,677 INFO     29 [Trace] task=5e62f0e6 | doc=lsju-哮喘-沈阳(1).pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "214 items", "markdown": "", "text": "", "name": "lsju-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-10 11:20:23,678 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 11:20:23,686 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:20:23,686 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:20:24,136 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:20:24,149 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 11:20:24,150 INFO     29 [Trace] task=5e62f0e6 | doc=lsju-哮喘-沈阳(1).pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "214 items", "markdown": "", "text": "", "name": "lsju-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-10 11:20:24,150 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 11:20:24,168 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:20:24,172 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:20:24,172 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:20:24,172 INFO     29 [qwen-vl-text] positions(24): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:20:24,173 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [24]
2026-08-10 11:20:24,402 INFO     29 [qwen-vl-text] page=2, rect=595x857, img=(1654x2382), dpi=200
2026-08-10 11:20:24,403 INFO     29 [qwen-vl-text] LLM extraction start, text_len=493
2026-08-10 11:20:24,403 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:20:24,403 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 12, \"bbox_end\": 35, \"encounter_dates\": [\"2026-02-10\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "北票成岩中医院\n门诊病历\n科别：内科门诊 姓名\n性别：女 年龄：57岁 门诊号：7260295\n职业：农民 婚姻：已婚\n药物过敏史：无\n住址：辽宁省朝阳市凌源市宋杖子镇马杖子\n纪录时间：2026-02-10 09:15\n主诉：反复发作咳嗽喘息5年余、加重5天\n现病史：患者2020年6月于中国医科大学附属第一医院诊断为支气管哮喘，后规律使用布\n地奈德福莫特罗吸入粉雾剂（II）320μg:9μg，1日/2吸。5天前患者受凉后出\n现咳嗽喘息症状加重，无发热，日常活动受限，为求进一步诊治来我院。\n既往史：支气管哮喘病史5年余。\n过敏史：花粉过敏\n传染病及流行性病史：无\n查体：T36.7℃，P82次/分，R24次/分，BP 125/80 mmHg。双肺呼吸音粗，可闻及广泛呼\n气相哮鸣音，未闻及湿性啰音。\n辅助检查：\n初步诊断：支气管哮喘（急性发作期）\n诊疗意见：1.醋酸泼尼松片20mg日1次口服，连续用5天。\n2.沙丁胺醇气雾剂2喷/次，每4小时1次，症状缓解后改为按需吸入。\n3.布地奈德福莫特罗吸入粉雾剂（II）320μg:9μg,1日/2吸规律吸入\n医师签名：\n日期：2026年",
    "role": "user"
  }
]
2026-08-10 11:20:27,025 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:20:27,025 INFO     29 [qwen-vl-text] LLM output (len=413):
{
  "encounter_date": "2026-02-10",
  "chief_complaint": "反复发作咳嗽喘息5年余、加重5天",
  "present_illness": "患者2020年6月于中国医科大学附属第一医院诊断为支气管哮喘，后规律使用布地奈德福莫特罗吸入粉雾剂（II）320μg:9μg，1日/2吸。5天前患者受凉后出现咳嗽喘息症状加重，无发热，日常活动受限，为求进一步诊治来我院。",
  "past_history": "支气管哮喘病史5年余。",
  "diagnosis": "支气管哮喘（急性发作期）",
  "treatment_plan": [
    "醋酸泼尼松片20mg日1次口服，连续用5天",
    "沙丁胺醇气雾剂2喷/次，每4小时1次，症状缓解后改为按需吸入",
    "布地奈德福莫特罗吸入粉雾剂（II）320μg:9μg,1日/2吸规律吸入"
  ]
}
2026-08-10 11:20:27,025 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-10]
2026-08-10 11:20:27,028 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1066837, prompt_len=1178
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共24行）
["北票成岩中医院", "门诊病历", "科别：内科门诊 姓名", "性别：女 年龄：57岁 门诊号：7260295", "职业：农民 婚姻：已婚", "药物过敏史：无", "住址：辽宁省朝阳市凌源市宋杖子镇马杖子", "纪录时间：2026-02-10 09:15", "主诉：反复发作咳嗽喘息5年余、加重5天", "现病史：患者2020年6月于中国医科大学附属第一医院诊断为支气管哮喘，后规律使用布", "地奈德福莫特罗吸入粉雾剂（II）320μg:9μg，1日/2吸。5天前患者受凉后出", "现咳嗽喘息症状加重，无发热，日常活动受限，为求进一步诊治来我院。", "既往史：支气管哮喘病史5年余。", "过敏史：花粉过敏", "传染病及流行性病史：无", "查体：T36.7℃，P82次/分，R24次/分，BP 125/80 mmHg。双肺呼吸音粗，可闻及广泛呼", "气相哮鸣音，未闻及湿性啰音。", "辅助检查：", "初步诊断：支气管哮喘（急性发作期）", "诊疗意见：1.醋酸泼尼松片20mg日1次口服，连续用5天。", "2.沙丁胺醇气雾剂2喷/次，每4小时1次，症状缓解后改为按需吸入。", "3.布地奈德福莫特罗吸入粉雾剂（II）320μg:9μg,1日/2吸规律吸入", "医师签名：", "日期：2026年"]

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
2026-08-10 11:20:36,751 INFO     29 [qwen-vl-text] coord API raw response (len=1551):
[
	{"text": "北票成岩中医院", "bbox": [375, 99, 620, 124]},
	{"text": "门诊病历", "bbox": [440, 137, 557, 158]},
	{"text": "科别：内科门诊 姓名", "bbox": [151, 201, 337, 217]},
	{"text": "性别：女 年龄：57岁 门诊号：7260295", "bbox": [450, 201, 790, 217]},
	{"text": "职业：农民 婚姻：已婚", "bbox": [151, 225, 474, 240]},
	{"text": "药物过敏史：无", "bbox": [151, 248, 279, 263]},
	{"text": "住址：辽宁省朝阳市凌源市宋杖子镇马杖子", "bbox": [151, 271, 497, 286]},
	{"text": "纪录时间：2026-02-10 09:15", "bbox": [151, 313, 390, 328]},
	{"text": "主诉：反复发作咳嗽喘息5年余、加重5天", "bbox": [151, 338, 473, 353]},
	{"text": "现病史：患者2020年6月于中国医科大学附属第一医院诊断为支气管哮喘，后规律使用布", "bbox": [151, 363, 846, 378]},
	{"text": "地奈德福莫特罗吸入粉雾剂（II）320μg:9μg，1日/2吸。5天前患者受凉后出", "bbox": [214, 388, 846, 403]},
	{"text": "现咳嗽喘息症状加重，无发热，日常活动受限，为求进一步诊治来我院。", "bbox": [214, 413, 794, 428]},
	{"text": "既往史：支气管哮喘病史5年余。", "bbox": [151, 438, 400, 453]},
	{"text": "过敏史：花粉过敏", "bbox": [151, 463, 290, 478]},
	{"text": "传染病及流行性病史：无", "bbox": [151, 488, 345, 503]},
	{"text": "查体：T36.7℃，P82次/分，R24次/分，BP 125/80 mmHg。双肺呼吸音粗，可闻及广泛呼", "bbox": [151, 513, 846, 528]},
	{"text": "气相哮鸣音，未闻及湿性啰音。", "bbox": [188, 537, 436, 552]},
	{"text": "辅助检查：", "bbox": [151, 562, 231, 577]},
	{"text": "初步诊断：支气管哮喘（急性发作期）", "bbox": [151, 587, 433, 602]},
	{"text": "诊疗意见：1.醋酸泼尼松片20mg日1次口服，连续用5天。", "bbox": [151, 612, 590, 627]},
	{"text": "2.沙丁胺醇气雾剂2喷/次，每4小时1次，症状缓解后改为按需吸入。", "bbox": [223, 637, 766, 653]},
	{"text": "3.布地奈德福莫特罗吸入粉雾剂（II）320μg:9μg,1日/2吸规律吸入", "bbox": [227, 662, 790, 678]},
	{"text": "医师签名：", "bbox": [571, 764, 653, 779]},
	{"text": "日期：2026年", "bbox": [572, 789, 682, 804]}
]
2026-08-10 11:20:36,751 INFO     29 [qwen-vl-text] coord API: raw_items=24, valid_items=24, elapsed=9.7s
2026-08-10 11:20:36,751 INFO     29 [qwen-vl-text] coord item[0]: text=北票成岩中医院, bbox=[375, 99, 620, 124]
2026-08-10 11:20:36,752 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[440, 137, 557, 158]
2026-08-10 11:20:36,752 INFO     29 [qwen-vl-text] coord item[2]: text=科别：内科门诊 姓名, bbox=[151, 201, 337, 217]
2026-08-10 11:20:36,752 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女 年龄：57岁 门诊号：7260295, bbox=[450, 201, 790, 217]
2026-08-10 11:20:36,752 INFO     29 [qwen-vl-text] coord item[4]: text=职业：农民 婚姻：已婚, bbox=[151, 225, 474, 240]
2026-08-10 11:20:36,752 INFO     29 [qwen-vl-text] coord item[5]: text=药物过敏史：无, bbox=[151, 248, 279, 263]
2026-08-10 11:20:36,752 INFO     29 [qwen-vl-text] coord item[6]: text=住址：辽宁省朝阳市凌源市宋杖子镇马杖子, bbox=[151, 271, 497, 286]
2026-08-10 11:20:36,752 INFO     29 [qwen-vl-text] coord item[7]: text=纪录时间：2026-02-10 09:15, bbox=[151, 313, 390, 328]
2026-08-10 11:20:36,752 INFO     29 [qwen-vl-text] coord item[8]: text=主诉：反复发作咳嗽喘息5年余、加重5天, bbox=[151, 338, 473, 353]
2026-08-10 11:20:36,752 INFO     29 [qwen-vl-text] coord item[9]: text=现病史：患者2020年6月于中国医科大学附属第一医院诊断为支气管哮喘，后规律使用布, bbox=[151, 363, 846, 378]
2026-08-10 11:20:36,752 INFO     29 [qwen-vl-text] coord item[10]: text=地奈德福莫特罗吸入粉雾剂（II）320μg:9μg，1日/2吸。5天前患者受凉后出, bbox=[214, 388, 846, 403]
2026-08-10 11:20:36,752 INFO     29 [qwen-vl-text] coord item[11]: text=现咳嗽喘息症状加重，无发热，日常活动受限，为求进一步诊治来我院。, bbox=[214, 413, 794, 428]
2026-08-10 11:20:36,752 INFO     29 [qwen-vl-text] coord item[12]: text=既往史：支气管哮喘病史5年余。, bbox=[151, 438, 400, 453]
2026-08-10 11:20:36,752 INFO     29 [qwen-vl-text] coord item[13]: text=过敏史：花粉过敏, bbox=[151, 463, 290, 478]
2026-08-10 11:20:36,752 INFO     29 [qwen-vl-text] coord item[14]: text=传染病及流行性病史：无, bbox=[151, 488, 345, 503]
2026-08-10 11:20:36,752 INFO     29 [qwen-vl-text] coord item[15]: text=查体：T36.7℃，P82次/分，R24次/分，BP 125/80 mmHg。双肺呼吸音粗，可闻及广泛呼, bbox=[151, 513, 846, 528]
2026-08-10 11:20:36,752 INFO     29 [qwen-vl-text] coord item[16]: text=气相哮鸣音，未闻及湿性啰音。, bbox=[188, 537, 436, 552]
2026-08-10 11:20:36,752 INFO     29 [qwen-vl-text] coord item[17]: text=辅助检查：, bbox=[151, 562, 231, 577]
2026-08-10 11:20:36,752 INFO     29 [qwen-vl-text] coord item[18]: text=初步诊断：支气管哮喘（急性发作期）, bbox=[151, 587, 433, 602]
2026-08-10 11:20:36,752 INFO     29 [qwen-vl-text] coord item[19]: text=诊疗意见：1.醋酸泼尼松片20mg日1次口服，连续用5天。, bbox=[151, 612, 590, 627]
2026-08-10 11:20:36,752 INFO     29 [qwen-vl-text] coord item[20]: text=2.沙丁胺醇气雾剂2喷/次，每4小时1次，症状缓解后改为按需吸入。, bbox=[223, 637, 766, 653]
2026-08-10 11:20:36,752 INFO     29 [qwen-vl-text] coord item[21]: text=3.布地奈德福莫特罗吸入粉雾剂（II）320μg:9μg,1日/2吸规律吸入, bbox=[227, 662, 790, 678]
2026-08-10 11:20:36,752 INFO     29 [qwen-vl-text] coord item[22]: text=医师签名：, bbox=[571, 764, 653, 779]
2026-08-10 11:20:36,752 INFO     29 [qwen-vl-text] coord item[23]: text=日期：2026年, bbox=[572, 789, 682, 804]
2026-08-10 11:20:36,752 INFO     29 [qwen-vl-text] page=2 — 24/24 coords, api_time=9.7s
2026-08-10 11:20:36,752 INFO     29 [qwen-vl-text] new_positions (24):
[[2, 223.2300109863281, 369.07361816406245, 84.87764758300781, 106.31139697265625], [2, 261.923212890625, 331.5709763183593, 117.45694665527344, 135.46129614257814], [2, 89.88728442382812, 200.60936987304686, 172.32734509277344, 186.04494470214843], [2, 267.8760131835937, 470.27122314453123, 172.32734509277344, 186.04494470214843], [2, 89.88728442382812, 282.16273388671874, 192.90374450683595, 205.76399414062502], [2, 89.88728442382812, 166.0831281738281, 212.6227939453125, 225.48304357910158], [2, 89.88728442382812, 295.8541745605469, 232.34184338378907, 245.20209301757814], [2, 89.88728442382812, 232.15921142578122, 268.35054235839846, 281.2107919921875], [2, 89.88728442382812, 281.56745385742187, 289.7842917480469, 302.64454138183595], [2, 89.88728442382812, 503.6069047851562, 311.2180411376953, 324.0782907714844], [2, 127.38992626953124, 503.6069047851562, 332.65179052734373, 345.5120401611328], [2, 127.38992626953124, 472.6523432617187, 354.0855399169922, 366.9457895507812], [2, 89.88728442382812, 238.11201171874998, 375.51928930664064, 388.3795389404297], [2, 89.88728442382812, 172.63120849609373, 396.95303869628907, 409.81328833007814], [2, 89.88728442382812, 205.37161010742187, 418.3867880859375, 431.24703771972656], [2, 89.88728442382812, 503.6069047851562, 439.8205374755859, 452.680787109375], [2, 111.9126455078125, 259.5420927734375, 460.39693688964843, 473.2571865234375], [2, 89.88728442382812, 137.5096867675781, 481.83068627929686, 494.6909359130859], [2, 89.88728442382812, 257.7562526855469, 503.26443566894534, 516.1246853027344], [2, 89.88728442382812, 351.2152172851562, 524.6981850585937, 537.5584346923828], [2, 132.74744653320312, 455.9845024414062, 546.1319344482422, 559.8495340576172], [2, 135.1285666503906, 470.27122314453123, 567.5656838378907, 581.2832834472656], [2, 339.9048967285156, 388.7178591308593, 655.0153813476562, 667.8756309814453], [2, 340.5001767578125, 405.9809799804687, 676.4491307373047, 689.3093803710938]]
2026-08-10 11:20:36,753 INFO     29 [qwen-vl-text] ═══ DONE ═══ 24 positions, pages=1, time=12.6s
2026-08-10 11:20:36,753 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:20:36,761 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:20:36,761 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:20:36,761 INFO     29 [qwen-vl-text] positions(25): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:20:36,761 INFO     29 [qwen-vl-text] page grouping: [3, 4], lines per page: [9, 16]
2026-08-10 11:20:37,041 INFO     29 [qwen-vl-text] page=3, rect=842x474, img=(2339x1316), dpi=200
2026-08-10 11:20:37,260 INFO     29 [qwen-vl-text] page=4, rect=842x474, img=(2339x1316), dpi=200
2026-08-10 11:20:37,261 INFO     29 [qwen-vl-text] LLM extraction start, text_len=334
2026-08-10 11:20:37,261 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:20:37,261 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 36, \"bbox_end\": 60, \"encounter_dates\": [\"2021-10-11\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "病历记录\n以下为中国医科大学附属第一医院门（急）诊病历记录 2021年10月11日 时 分\n主诉：反复喘息3年余\n现病史：曾于2020年6月到我院就诊，诊断“支气管哮喘”，\n目前仍有气短症状，规律使用可必特吸入\n日二次吸入，强的松2片日一次口服\n既往史：花粉过敏\n家庭史：0\n体格检查：2021年0平气相喘鸣(+)\n病历记录\n胸CT(外院)3.221年较前透亮度降低\n余未见确切异常\n查肺功+舒张+弥散\n血气\n白常规.0嗜碱细胞296\n血气PH7.395.P0266.9P0241.5\n肺功:弥散正常\nFVC48.6%FEV1.301%\n舒张41.6%FEV1.072\n病历记录\n叩诊:支气管哮鸣(重度)\n低氧血症\n建议:住院320ug吸入二次吸入\n待化验结果\n苏新明",
    "role": "user"
  }
]
2026-08-10 11:20:37,263 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:20:37.262+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 20, "failed": 0, "current": {"5e62f0e694ad11f1bd9827cf206dfa2d": {"id": "5e62f0e694ad11f1bd9827cf206dfa2d", "doc_id": "5ddcc2a094ad11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "lsju-\u54ee\u5598-\u6c88\u9633(1).pdf", "type": "pdf", "location": "lsju-\u54ee\u5598-\u6c88\u9633(1).pdf", "size": 3913176, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786360775902, "task_type": "dataflow", "root_trace_id": "7d6dcbad8e7b45c1949a5dd052ab4409", "root_traceparent": "00-7d6dcbad8e7b45c1949a5dd052ab4409-9207ab8c386eb81c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:20:39,403 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:20:39,403 INFO     29 [qwen-vl-text] LLM output (len=265):
{
  "encounter_date": "2021-10-11",
  "chief_complaint": "反复喘息3年余",
  "present_illness": "曾于2020年6月到我院就诊，诊断“支气管哮喘”，目前仍有气短症状，规律使用可必特吸入日二次吸入，强的松2片日一次口服",
  "past_history": "花粉过敏",
  "diagnosis": "支气管哮喘",
  "treatment_plan": "可必特吸入 日二次吸入; 强的松 2片 日一次口服; 320ug吸入 二次吸入"
}
2026-08-10 11:20:39,403 INFO     29 [qwen-vl-text] Updated encounter_dates=[2021-10-11]
2026-08-10 11:20:39,409 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2781984, prompt_len=796
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共9行）
["病历记录", "以下为中国医科大学附属第一医院门（急）诊病历记录 2021年10月11日 时 分", "主诉：反复喘息3年余", "现病史：曾于2020年6月到我院就诊，诊断“支气管哮喘”，", "目前仍有气短症状，规律使用可必特吸入", "日二次吸入，强的松2片日一次口服", "既往史：花粉过敏", "家庭史：0", "体格检查：2021年0平气相喘鸣(+)"]

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
2026-08-10 11:20:43,359 INFO     29 [qwen-vl-text] coord API raw response (len=555):
[
	{"text": "病历记录", "bbox": [502, 20, 635, 67]},
	{"text": "以下为中国医科大学附属第一医院门（急）诊病历记录 2021年10月11日 时 分", "bbox": [190, 100, 921, 150]},
	{"text": "主诉：反复喘息3年余", "bbox": [188, 177, 534, 264]},
	{"text": "现病史：曾于2020年6月到我院就诊，诊断“支气管哮喘”，", "bbox": [185, 260, 955, 362]},
	{"text": "目前仍有气短症状，规律使用可必特吸入", "bbox": [314, 350, 952, 450]},
	{"text": "日二次吸入，强的松2片日一次口服", "bbox": [355, 448, 887, 538]},
	{"text": "既往史：花粉过敏", "bbox": [176, 550, 438, 635]},
	{"text": "家庭史：0", "bbox": [172, 658, 340, 725]},
	{"text": "体格检查：2021年0平气相喘鸣(+) ", "bbox": [169, 730, 624, 840]}
]
2026-08-10 11:20:43,359 INFO     29 [qwen-vl-text] coord API: raw_items=9, valid_items=9, elapsed=3.9s
2026-08-10 11:20:43,359 INFO     29 [qwen-vl-text] coord item[0]: text=病历记录, bbox=[502, 20, 635, 67]
2026-08-10 11:20:43,359 INFO     29 [qwen-vl-text] coord item[1]: text=以下为中国医科大学附属第一医院门（急）诊病历记录 2021年10月11日 时 分, bbox=[190, 100, 921, 150]
2026-08-10 11:20:43,359 INFO     29 [qwen-vl-text] coord item[2]: text=主诉：反复喘息3年余, bbox=[188, 177, 534, 264]
2026-08-10 11:20:43,359 INFO     29 [qwen-vl-text] coord item[3]: text=现病史：曾于2020年6月到我院就诊，诊断“支气管哮喘”，, bbox=[185, 260, 955, 362]
2026-08-10 11:20:43,359 INFO     29 [qwen-vl-text] coord item[4]: text=目前仍有气短症状，规律使用可必特吸入, bbox=[314, 350, 952, 450]
2026-08-10 11:20:43,359 INFO     29 [qwen-vl-text] coord item[5]: text=日二次吸入，强的松2片日一次口服, bbox=[355, 448, 887, 538]
2026-08-10 11:20:43,360 INFO     29 [qwen-vl-text] coord item[6]: text=既往史：花粉过敏, bbox=[176, 550, 438, 635]
2026-08-10 11:20:43,360 INFO     29 [qwen-vl-text] coord item[7]: text=家庭史：0, bbox=[172, 658, 340, 725]
2026-08-10 11:20:43,360 INFO     29 [qwen-vl-text] coord item[8]: text=体格检查：2021年0平气相喘鸣(+) , bbox=[169, 730, 624, 840]
2026-08-10 11:20:43,361 INFO     29 [qwen-vl-text] page=3 — 9/9 coords, api_time=3.9s
2026-08-10 11:20:43,371 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2853509, prompt_len=837
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共16行）
["病历记录", "胸CT(外院)3.221年较前透亮度降低", "余未见确切异常", "查肺功+舒张+弥散", "血气", "白常规.0嗜碱细胞296", "血气PH7.395.P0266.9P0241.5", "肺功:弥散正常", "FVC48.6%FEV1.301%", "舒张41.6%FEV1.072", "病历记录", "叩诊:支气管哮鸣(重度)", "低氧血症", "建议:住院320ug吸入二次吸入", "待化验结果", "苏新明"]

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
2026-08-10 11:20:50,056 INFO     29 [qwen-vl-text] coord API raw response (len=912):
[
	{"text": "病历记录", "bbox": [253, 149, 350, 187]},
	{"text": "胸CT(外院)3.221年较前透亮度降低", "bbox": [167, 200, 500, 272]},
	{"text": "余未见确切异常", "bbox": [304, 258, 453, 322], "bbox": [304, 258, 453, 322]},
	{"text": "查肺功+舒张+弥散", "bbox": [182, 318, 417, 392]},
	{"text": "血气", "bbox": [243, 387, 297, 437]},
	{"text": "白常规.0嗜碱细胞296", "bbox": [235, 437, 482, 507]},
	{"text": "血气PH7.395.P0266.9P0241.5", "bbox": [93, 507, 440, 582]},
	{"text": "肺功:弥散正常", "bbox": [109, 573, 270, 648]},
	{"text": "FVC48.6%FEV1.301%", "bbox": [315, 548, 530, 620]},
	{"text": "舒张41.6%FEV1.072", "bbox": [322, 607, 536, 684]},
	{"text": "病历记录", "bbox": [736, 195, 813, 225]},
	{"text": "叩诊:支气管哮鸣(重度)", "bbox": [575, 237, 813, 297]},
	{"text": "低氧血症", "bbox": [658, 297, 745, 357]},
	{"text": "建议:住院320ug吸入二次吸入", "bbox": [582, 345, 907, 412]},
	{"text": "待化验结果", "bbox": [801, 407, 922, 457]},
	{"text": "苏新明", "bbox": [930, 397, 970, 475]}
]
2026-08-10 11:20:50,056 INFO     29 [qwen-vl-text] coord API: raw_items=16, valid_items=16, elapsed=6.7s
2026-08-10 11:20:50,056 INFO     29 [qwen-vl-text] coord item[0]: text=病历记录, bbox=[253, 149, 350, 187]
2026-08-10 11:20:50,056 INFO     29 [qwen-vl-text] coord item[1]: text=胸CT(外院)3.221年较前透亮度降低, bbox=[167, 200, 500, 272]
2026-08-10 11:20:50,056 INFO     29 [qwen-vl-text] coord item[2]: text=余未见确切异常, bbox=[304, 258, 453, 322]
2026-08-10 11:20:50,056 INFO     29 [qwen-vl-text] coord item[3]: text=查肺功+舒张+弥散, bbox=[182, 318, 417, 392]
2026-08-10 11:20:50,056 INFO     29 [qwen-vl-text] coord item[4]: text=血气, bbox=[243, 387, 297, 437]
2026-08-10 11:20:50,056 INFO     29 [qwen-vl-text] coord item[5]: text=白常规.0嗜碱细胞296, bbox=[235, 437, 482, 507]
2026-08-10 11:20:50,056 INFO     29 [qwen-vl-text] coord item[6]: text=血气PH7.395.P0266.9P0241.5, bbox=[93, 507, 440, 582]
2026-08-10 11:20:50,056 INFO     29 [qwen-vl-text] coord item[7]: text=肺功:弥散正常, bbox=[109, 573, 270, 648]
2026-08-10 11:20:50,056 INFO     29 [qwen-vl-text] coord item[8]: text=FVC48.6%FEV1.301%, bbox=[315, 548, 530, 620]
2026-08-10 11:20:50,056 INFO     29 [qwen-vl-text] coord item[9]: text=舒张41.6%FEV1.072, bbox=[322, 607, 536, 684]
2026-08-10 11:20:50,056 INFO     29 [qwen-vl-text] coord item[10]: text=病历记录, bbox=[736, 195, 813, 225]
2026-08-10 11:20:50,056 INFO     29 [qwen-vl-text] coord item[11]: text=叩诊:支气管哮鸣(重度), bbox=[575, 237, 813, 297]
2026-08-10 11:20:50,056 INFO     29 [qwen-vl-text] coord item[12]: text=低氧血症, bbox=[658, 297, 745, 357]
2026-08-10 11:20:50,056 INFO     29 [qwen-vl-text] coord item[13]: text=建议:住院320ug吸入二次吸入, bbox=[582, 345, 907, 412]
2026-08-10 11:20:50,056 INFO     29 [qwen-vl-text] coord item[14]: text=待化验结果, bbox=[801, 407, 922, 457]
2026-08-10 11:20:50,056 INFO     29 [qwen-vl-text] coord item[15]: text=苏新明, bbox=[930, 397, 970, 475]
2026-08-10 11:20:50,057 INFO     29 [qwen-vl-text] page=4 — 16/16 coords, api_time=6.7s
2026-08-10 11:20:50,057 INFO     29 [qwen-vl-text] new_positions (25):
[[3, 422.62878735351563, 534.6001593017578, 9.471199951171874, 31.72851983642578], [3, 159.95910278320312, 775.380703491211, 47.35599975585937, 71.03399963378907], [3, 158.27532275390624, 449.5692678222656, 83.82011956787109, 125.01983935546875], [3, 155.74965270996094, 804.0049639892578, 123.12559936523436, 171.42871911621094], [3, 264.35346459960937, 801.4792939453125, 165.7459991455078, 213.10199890136718], [3, 298.8709552001953, 746.756442993164, 212.15487890625, 254.77527868652342], [3, 148.172642578125, 368.74782641601564, 260.45799865722654, 300.71059844970705], [3, 144.80508251953125, 286.24260498046874, 311.6024783935547, 343.3309982299805], [3, 142.27941247558593, 525.339369140625, 345.6987982177734, 397.79039794921874], [4, 212.99817370605467, 294.6615051269531, 70.56043963623047, 88.55571954345703], [4, 140.59563244628907, 420.94500732421875, 94.71199951171874, 128.80831933593748], [4, 255.934564453125, 381.3761766357422, 122.17847937011719, 152.48631921386718], [4, 153.22398266601562, 351.06813610839845, 150.59207922363282, 185.63551904296875], [4, 204.5792735595703, 250.04133435058594, 183.26771905517577, 206.94571893310547], [4, 197.8441534423828, 405.79098706054685, 206.94571893310547, 240.09491876220702], [4, 78.29577136230469, 370.43160644531247, 240.09491876220702, 275.61191857910154], [4, 91.76601159667969, 227.31030395507813, 271.34987860107424, 306.86687841796873], [4, 265.19535461425784, 446.2017077636719, 259.51087866210935, 293.6071984863281], [4, 271.08858471679684, 451.2530478515625, 287.4509185180664, 323.9150383300781], [4, 619.63105078125, 684.4565819091797, 92.34419952392578, 106.55099945068359], [4, 484.0867584228516, 684.4565819091797, 112.23371942138671, 140.64731927490234], [4, 553.9636296386718, 627.2080609130859, 140.64731927490234, 169.06091912841796], [4, 489.97998852539064, 763.5942432861328, 163.37819915771485, 195.1067189941406], [4, 674.3539017333984, 776.2225935058593, 192.73891900634766, 216.41691888427735], [4, 782.9577136230469, 816.6333142089844, 188.0033190307617, 224.940998840332]]
2026-08-10 11:20:50,057 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=2, time=13.3s
2026-08-10 11:20:50,066 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 11:20:50,066 INFO     29 [Trace] task=5e62f0e6 | doc=lsju-哮喘-沈阳(1).pdf | Extractor:Clinical | outputs={"chunks": "2 items, types={'OutpatientRecord': 2}", "html": "", "json": "214 items", "markdown": "", "text": "", "name": "lsju-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-10 11:20:50,067 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 11:20:50,076 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:20:50,077 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:20:50,077 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 11:20:50,077 INFO     29 [qwen-vl-text] positions(29): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:20:50,077 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [29]
2026-08-10 11:20:50,268 INFO     29 [qwen-vl-text] page=5, rect=595x1290, img=(1654x3584), dpi=200
2026-08-10 11:20:50,269 INFO     29 [qwen-vl-text] LLM extraction start, text_len=241
2026-08-10 11:20:50,269 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:20:50,269 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 64, \"bbox_end\": 92, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "订单详情\n完成\n建议您关注病情进展并及时复诊 去复诊 >\n再次购买\n已签收\n您的预约单已签收\n185****3662\n辽宁朝阳市凌源市宋杖子镇马杖子\n京东大药房\n联系\n满意度调研\n药品不支持7天无理由退换货\n京东买药\n仙琚 醋酸泼尼松片 5mg*100片\n数量：1\n¥6.90/件\n品质保障\n多仓发货\n正品好药\n极速发货\n专业药师服务\n用药人信息\n刘素娟 女 57岁\n问诊单\n查看详情 >\n不良反应登记 京东大药房执业药师提示：合格药品在正常\n点击查看您的用药指导\n去看看\n删除订单",
    "role": "user"
  }
]
2026-08-10 11:20:52,247 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:20:52,247 INFO     29 [qwen-vl-text] LLM output (len=400):
{
  "encounter_date": null,
  "pharmacy": "京东大药房",
  "medications": [
    {
      "name": "仙琚 醋酸泼尼松片",
      "specification": "5mg*100片",
      "dosage": null,
      "quantity": 1,
      "unit_price": 6.90,
      "total_price": null,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": null,
  "payment_method": null
}
2026-08-10 11:20:52,251 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1453571, prompt_len=941
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共29行）
["订单详情", "完成", "建议您关注病情进展并及时复诊 去复诊 >", "再次购买", "已签收", "您的预约单已签收", "185****3662", "辽宁朝阳市凌源市宋杖子镇马杖子", "京东大药房", "联系", "满意度调研", "药品不支持7天无理由退换货", "京东买药", "仙琚 醋酸泼尼松片 5mg*100片", "数量：1", "¥6.90/件", "品质保障", "多仓发货", "正品好药", "极速发货", "专业药师服务", "用药人信息", "刘素娟 女 57岁", "问诊单", "查看详情 >", "不良反应登记 京东大药房执业药师提示：合格药品在正常", "点击查看您的用药指导", "去看看", "删除订单"]

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
2026-08-10 11:21:01,377 INFO     29 [qwen-vl-text] coord API raw response (len=1503):
[
	{"text": "订单详情", "bbox": [415, 69, 580, 92]},
	{"text": "完成", "bbox": [476, 113, 593, 141]},
	{"text": "建议您关注病情进展并及时复诊 去复诊 >", "bbox": [156, 153, 837, 173]},
	{"text": "再次购买", "bbox": [423, 197, 572, 217]},
	{"text": "已签收", "bbox": [45, 279, 203, 298]},
	{"text": "您的预约单已签收", "bbox": [88, 307, 343, 323]},
	{"text": "185****3662", "bbox": [217, 369, 418, 387]},
	{"text": "辽宁朝阳市凌源市宋杖子镇马杖子", "bbox": [88, 397, 565, 413]},
	{"text": "京东大药房", "bbox": [92, 483, 305, 504]},
	{"text": "联系", "bbox": [820, 486, 872, 502]},
	{"text": "满意度调研", "bbox": [865, 501, 985, 513]},
	{"text": "药品不支持7天无理由退换货", "bbox": [128, 534, 563, 553]},
	{"text": "京东买药", "bbox": [54, 591, 130, 598]},
	{"text": "仙琚 醋酸泼尼松片 5mg*100片", "bbox": [292, 591, 722, 610]},
	{"text": "数量：1", "bbox": [292, 613, 395, 629]},
	{"text": "¥6.90/件", "bbox": [290, 646, 423, 664]},
	{"text": "品质保障", "bbox": [58, 626, 118, 633]},
	{"text": "多仓发货", "bbox": [58, 633, 118, 640]},
	{"text": "正品好药", "bbox": [62, 643, 114, 650]},
	{"text": "极速发货", "bbox": [62, 650, 114, 657]},
	{"text": "专业药师服务", "bbox": [58, 657, 118, 664]},
	{"text": "用药人信息", "bbox": [45, 736, 218, 754]},
	{"text": "刘素娟 女 57岁", "bbox": [668, 736, 948, 754]},
	{"text": "问诊单", "bbox": [45, 782, 150, 800]},
	{"text": "查看详情 >", "bbox": [773, 782, 939, 800]},
	{"text": "不良反应登记 京东大药房执业药师提示：合格药品在正常", "bbox": [73, 840, 898, 857]},
	{"text": "点击查看您的用药指导", "bbox": [92, 871, 437, 889]},
	{"text": "去看看", "bbox": [833, 871, 967, 889]},
	{"text": "删除订单", "bbox": [24, 921, 152, 939]}
]
2026-08-10 11:21:01,378 INFO     29 [qwen-vl-text] coord API: raw_items=29, valid_items=29, elapsed=9.1s
2026-08-10 11:21:01,378 INFO     29 [qwen-vl-text] coord item[0]: text=订单详情, bbox=[415, 69, 580, 92]
2026-08-10 11:21:01,378 INFO     29 [qwen-vl-text] coord item[1]: text=完成, bbox=[476, 113, 593, 141]
2026-08-10 11:21:01,378 INFO     29 [qwen-vl-text] coord item[2]: text=建议您关注病情进展并及时复诊 去复诊 >, bbox=[156, 153, 837, 173]
2026-08-10 11:21:01,378 INFO     29 [qwen-vl-text] coord item[3]: text=再次购买, bbox=[423, 197, 572, 217]
2026-08-10 11:21:01,378 INFO     29 [qwen-vl-text] coord item[4]: text=已签收, bbox=[45, 279, 203, 298]
2026-08-10 11:21:01,378 INFO     29 [qwen-vl-text] coord item[5]: text=您的预约单已签收, bbox=[88, 307, 343, 323]
2026-08-10 11:21:01,378 INFO     29 [qwen-vl-text] coord item[6]: text=185****3662, bbox=[217, 369, 418, 387]
2026-08-10 11:21:01,378 INFO     29 [qwen-vl-text] coord item[7]: text=辽宁朝阳市凌源市宋杖子镇马杖子, bbox=[88, 397, 565, 413]
2026-08-10 11:21:01,378 INFO     29 [qwen-vl-text] coord item[8]: text=京东大药房, bbox=[92, 483, 305, 504]
2026-08-10 11:21:01,378 INFO     29 [qwen-vl-text] coord item[9]: text=联系, bbox=[820, 486, 872, 502]
2026-08-10 11:21:01,378 INFO     29 [qwen-vl-text] coord item[10]: text=满意度调研, bbox=[865, 501, 985, 513]
2026-08-10 11:21:01,378 INFO     29 [qwen-vl-text] coord item[11]: text=药品不支持7天无理由退换货, bbox=[128, 534, 563, 553]
2026-08-10 11:21:01,378 INFO     29 [qwen-vl-text] coord item[12]: text=京东买药, bbox=[54, 591, 130, 598]
2026-08-10 11:21:01,378 INFO     29 [qwen-vl-text] coord item[13]: text=仙琚 醋酸泼尼松片 5mg*100片, bbox=[292, 591, 722, 610]
2026-08-10 11:21:01,378 INFO     29 [qwen-vl-text] coord item[14]: text=数量：1, bbox=[292, 613, 395, 629]
2026-08-10 11:21:01,378 INFO     29 [qwen-vl-text] coord item[15]: text=¥6.90/件, bbox=[290, 646, 423, 664]
2026-08-10 11:21:01,378 INFO     29 [qwen-vl-text] coord item[16]: text=品质保障, bbox=[58, 626, 118, 633]
2026-08-10 11:21:01,378 INFO     29 [qwen-vl-text] coord item[17]: text=多仓发货, bbox=[58, 633, 118, 640]
2026-08-10 11:21:01,378 INFO     29 [qwen-vl-text] coord item[18]: text=正品好药, bbox=[62, 643, 114, 650]
2026-08-10 11:21:01,379 INFO     29 [qwen-vl-text] coord item[19]: text=极速发货, bbox=[62, 650, 114, 657]
2026-08-10 11:21:01,379 INFO     29 [qwen-vl-text] coord item[20]: text=专业药师服务, bbox=[58, 657, 118, 664]
2026-08-10 11:21:01,379 INFO     29 [qwen-vl-text] coord item[21]: text=用药人信息, bbox=[45, 736, 218, 754]
2026-08-10 11:21:01,379 INFO     29 [qwen-vl-text] coord item[22]: text=刘素娟 女 57岁, bbox=[668, 736, 948, 754]
2026-08-10 11:21:01,379 INFO     29 [qwen-vl-text] coord item[23]: text=问诊单, bbox=[45, 782, 150, 800]
2026-08-10 11:21:01,379 INFO     29 [qwen-vl-text] coord item[24]: text=查看详情 >, bbox=[773, 782, 939, 800]
2026-08-10 11:21:01,379 INFO     29 [qwen-vl-text] coord item[25]: text=不良反应登记 京东大药房执业药师提示：合格药品在正常, bbox=[73, 840, 898, 857]
2026-08-10 11:21:01,379 INFO     29 [qwen-vl-text] coord item[26]: text=点击查看您的用药指导, bbox=[92, 871, 437, 889]
2026-08-10 11:21:01,379 INFO     29 [qwen-vl-text] coord item[27]: text=去看看, bbox=[833, 871, 967, 889]
2026-08-10 11:21:01,379 INFO     29 [qwen-vl-text] coord item[28]: text=删除订单, bbox=[24, 921, 152, 939]
2026-08-10 11:21:01,379 INFO     29 [qwen-vl-text] page=5 — 29/29 coords, api_time=9.1s
2026-08-10 11:21:01,379 INFO     29 [qwen-vl-text] new_positions (29):
[[5, 247.0412121582031, 345.26241699218747, 89.01482629394532, 118.68643505859376], [5, 283.3532939453125, 353.0010573730469, 145.77790393066408, 181.89986242675784], [5, 92.8636845703125, 498.24938452148433, 197.38070178222657, 223.18210070800782], [5, 251.8034523925781, 340.5001767578125, 254.14377941894531, 279.94517834472657], [5, 26.78760131835937, 120.84184594726561, 359.9295150146485, 384.44084399414066], [5, 52.384642578124996, 204.1810500488281, 396.0514735107422, 416.6925926513672], [5, 129.17576635742188, 248.82705224609373, 476.0358101806641, 499.2570692138672], [5, 52.384642578124996, 336.33321655273437, 512.1577686767579, 532.7988878173828], [5, 54.765762695312496, 181.56040893554686, 623.1037840576172, 650.1952529296875], [5, 488.1296240234375, 519.084185546875, 626.9739938964844, 647.6151130371094], [5, 514.9172253417969, 586.3508288574218, 646.3250430908204, 661.805882446289], [5, 76.19584375, 335.1426564941406, 688.8973513183594, 713.4086802978516], [5, 32.14512158203125, 77.38640380859374, 762.4313382568359, 771.4618278808595], [5, 173.82176855468748, 429.79218115234374, 762.4313382568359, 786.9426672363281], [5, 173.82176855468748, 235.13561157226562, 790.8128770751954, 811.4539962158203], [5, 172.63120849609373, 251.8034523925781, 833.3851853027344, 856.6064443359376], [5, 34.526241699218744, 70.24304345703125, 807.5837863769532, 816.6142760009766], [5, 34.526241699218744, 70.24304345703125, 816.6142760009766, 825.644765625], [5, 36.90736181640625, 67.86192333984374, 829.5149754638672, 838.5454650878906], [5, 36.90736181640625, 67.86192333984374, 838.5454650878906, 847.5759547119142], [5, 34.526241699218744, 70.24304345703125, 847.5759547119142, 856.6064443359376], [5, 26.78760131835937, 129.77104638671875, 949.4914804687501, 972.7127395019531], [5, 397.6470595703125, 564.3254677734375, 949.4914804687501, 972.7127395019531], [5, 26.78760131835937, 89.29200439453125, 1008.834697998047, 1032.05595703125], [5, 460.15146264648433, 558.9679475097656, 1008.834697998047, 1032.05595703125], [5, 43.45544213867187, 534.5614663085937, 1083.6587548828127, 1105.5899439697266], [5, 54.765762695312496, 260.1373728027344, 1123.6509232177734, 1146.8721822509767], [5, 495.86826440429684, 575.6357883300781, 1123.6509232177734, 1146.8721822509767], [5, 14.286720703124999, 90.482564453125, 1188.1544205322266, 1211.3756795654297]]
2026-08-10 11:21:01,379 INFO     29 [qwen-vl-text] ═══ DONE ═══ 29 positions, pages=1, time=11.3s
2026-08-10 11:21:01,380 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:21:01,381 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:21:01,381 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 11:21:01,381 INFO     29 [qwen-vl-text] positions(85): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:21:01,381 INFO     29 [qwen-vl-text] page grouping: [5, 6, 7], lines per page: [2, 47, 36]
2026-08-10 11:21:01,571 INFO     29 [qwen-vl-text] page=5, rect=595x1290, img=(1654x3584), dpi=200
2026-08-10 11:21:01,771 INFO     29 [qwen-vl-text] page=6, rect=595x1291, img=(1654x3587), dpi=200
2026-08-10 11:21:01,921 INFO     29 [qwen-vl-text] page=7, rect=842x555, img=(2339x1543), dpi=200
2026-08-10 11:21:01,921 INFO     29 [qwen-vl-text] LLM extraction start, text_len=811
2026-08-10 11:21:01,922 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:21:01,922 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 93, \"bbox_end\": 177, \"encounter_dates\": [\"2026-02-25\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "查看发票\n再次购买\n13:19\n5G 49\n<\n哮喘用药热卖榜第4名\n85****3662\n自营 京东自营药房\n普通内科处方单131900332246895 距失效还剩71:59:43\n京东买药 AstraZeneca\n【原研进口】信必可 布地奈德福莫特...\n1\n原研正品\n多仓发货\n品质保障\n适3盒装 有金特贴到手价\n220\n元\n320\n1盒装(体验/应急装)\n不支持7天无理由退货\n¥249\n服务\n可选一年囤货补贴共5项 >\n配送\n京东快递 >\n2月25日 [周三] 09:00-21:00\n收货方式\n送货上门 >\n顺手买更划算 ①\n抑菌洗手液倍护滋润保湿持久留香\n450克*1瓶【体验装】\n80%用户顺手买过\nWeichi\nHAND SANITIZER\n抑菌洗手液\n净含量:450克\n¥2.9 专享价 ¥7.5\n省4.60元\n一键购买\n查看更多推荐 v\n商品金额\n¥249.00\n运费\n¥0.00\n优惠券\n无可用 >\n已隐藏本单不可使用的虚拟资产 v\n提交订单 ¥249.00\n电子发票(普通发票)\n国家税务总局\n辽宁省税务局\n发票号码: 26217000000097645604\n开票日期: 2026年02月25日\n购买方信息\n名称: 个人\n统一社会信用代码/纳税人识别号:\n销售方信息\n名称: 京东大药房(沈阳)有限公司\n统一社会信用代码/纳税人识别号: 91210112MA10499C0F\n项目名称\n规格型号\n单位\n数量\n单价\n金额\n税率/征收率\n税额\n*化学药品制剂*【原研进口】信必可布地奈德福莫特罗吸入粉雾剂(II) 320μg:9μg*60吸/盒\n布地奈德福莫特罗吸入粉雾剂(II)\n盒\n1\n220.35\n220.35\n13%\n28.65\n合计\n¥220.35\n¥28.65\n价税合计(大写)\n贰佰肆拾玖圆整\n(小写) ¥249.00\n备注\n订单号:3419204018592466\n开票人: 王梅",
    "role": "user"
  }
]
2026-08-10 11:21:04,929 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:21:04,929 INFO     29 [qwen-vl-text] LLM output (len=448):
{
  "encounter_date": "2026-02-25",
  "pharmacy": "京东自营药房",
  "medications": [
    {
      "name": "【原研进口】信必可布地奈德福莫特罗吸入粉雾剂(II)",
      "specification": "320μg:9μg*60吸/盒",
      "dosage": null,
      "quantity": 1,
      "unit_price": 220.35,
      "total_price": 220.35,
      "frequency": null,
      "route": null,
      "manufacturer": "AstraZeneca",
      "approval_number": null
    }
  ],
  "payment_total": 249.00,
  "payment_method": null
}
2026-08-10 11:21:04,929 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-25]
2026-08-10 11:21:04,934 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1453571, prompt_len=627
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共2行）
["查看发票", "再次购买"]

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
2026-08-10 11:21:05,875 INFO     29 [qwen-vl-text] coord API raw response (len=112):
```json
[
	{"text": "查看发票", "bbox": [452, 912, 679, 949]},
	{"text": "再次购买", "bbox": [731, 912, 958, 949]}
]
```
2026-08-10 11:21:05,875 INFO     29 [qwen-vl-text] coord API: raw_items=2, valid_items=2, elapsed=0.9s
2026-08-10 11:21:05,875 INFO     29 [qwen-vl-text] coord item[0]: text=查看发票, bbox=[452, 912, 679, 949]
2026-08-10 11:21:05,875 INFO     29 [qwen-vl-text] coord item[1]: text=再次购买, bbox=[731, 912, 958, 949]
2026-08-10 11:21:05,875 INFO     29 [qwen-vl-text] page=5 — 2/2 coords, api_time=0.9s
2026-08-10 11:21:05,878 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1536281, prompt_len=1186
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共47行）
["13:19", "5G 49", "<", "哮喘用药热卖榜第4名", "85****3662", "自营 京东自营药房", "普通内科处方单131900332246895 距失效还剩71:59:43", "京东买药 AstraZeneca", "【原研进口】信必可 布地奈德福莫特...", "1", "原研正品", "多仓发货", "品质保障", "适3盒装 有金特贴到手价", "220", "元", "320", "1盒装(体验/应急装)", "不支持7天无理由退货", "¥249", "服务", "可选一年囤货补贴共5项 >", "配送", "京东快递 >", "2月25日 [周三] 09:00-21:00", "收货方式", "送货上门 >", "顺手买更划算 ①", "抑菌洗手液倍护滋润保湿持久留香", "450克*1瓶【体验装】", "80%用户顺手买过", "Weichi", "HAND SANITIZER", "抑菌洗手液", "净含量:450克", "¥2.9 专享价 ¥7.5", "省4.60元", "一键购买", "查看更多推荐 v", "商品金额", "¥249.00", "运费", "¥0.00", "优惠券", "无可用 >", "已隐藏本单不可使用的虚拟资产 v", "提交订单 ¥249.00"]

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
2026-08-10 11:21:21,055 INFO     29 [qwen-vl-text] coord API raw response (len=3049):
[
	{"text": "13:19", "bbox": [134, 23, 238, 40]},
	{"text": "5G 49", "bbox": [707, 23, 900, 40]},
	{"text": "<", "bbox": [55, 73, 78, 90]},
	{"text": "哮喘用药热卖榜第4名", "bbox": [373, 73, 683, 90]},
	{"text": "85****3662", "bbox": [164, 163, 342, 177]},
	{"text": "自营 京东自营药房", "bbox": [41, 228, 287, 243]},
	{"text": "普通内科处方单131900332246895 距失效还剩71:59:43", "bbox": [64, 268, 783, 282]},
	{"text": "京东买药 AstraZeneca", "bbox": [41, 301, 150, 308]},
	{"text": "【原研进口】信必可 布地奈德福莫特...", "bbox": [248, 305, 778, 322]},
	{"text": "1", "bbox": [885, 308, 897, 319], "label": "text"},
	{"text": "原研正品", "bbox": [55, 325, 95, 331], "label": "text"},
	{"text": "多仓发货", "bbox": [55, 336, 95, 342], "label": "text"},
	{"text": "品质保障", "bbox": [55, 345, 95, 351], "label": "text"},
	{"text": "适3盒装 有金特贴到手价", "bbox": [55, 354, 95, 360], "label": "text"},
	{"text": "220", "bbox": [57, 360, 88, 367], "label": "text"},
	{"text": "元", "bbox": [91, 363, 98, 367], "label": "text"},
	{"text": "1盒装(体验/应急装)", "bbox": [250, 331, 502, 345], "label": "text"},
	{"text": "不支持7天无理由退货", "bbox": [250, 353, 500, 366], "label": "text"},
	{"text": "¥249", "bbox": [250, 375, 341, 393], "label": "text"},
	{"text": "服务", "bbox": [37, 415, 99, 431], "label": "text"},
	{"text": "可选一年囤货补贴共5项 >", "bbox": [579, 415, 955, 430], "label": "text"},
	{"text": "配送", "bbox": [37, 448, 99, 464], "label": "text"},
	{"text": "京东快递 >", "bbox": [794, 448, 955, 464], "label": "text"},
	{"text": "2月25日 [周三] 09:00-21:00", "bbox": [527, 470, 921, 487], "label": "text"},
	{"text": "收货方式", "bbox": [37, 507, 164, 523], "label": "text"},
	{"text": "送货上门 >", "bbox": [796, 507, 955, 523], "label": "text"},
	{"text": "顺手买更划算 ①", "bbox": [37, 568, 287, 584], "label": "text"},
	{"text": "抑菌洗手液倍护滋润保湿持久留香", "bbox": [273, 598, 754, 614], "label": "text"},
	{"text": "450克*1瓶【体验装】", "bbox": [273, 620, 527, 634], "label": "text"},
	{"text": "80%用户顺手买过", "bbox": [273, 640, 502, 654], "label": "text"},
	{"text": "Weichi", "bbox": [120, 650, 160, 656], "label": "text"},
	{"text": "HAND SANITIZER", "bbox": [141, 664, 181, 668], "label": "text"},
	{"text": "抑菌洗手液", "bbox": [141, 669, 173, 673], "label": "text"},
	{"text": "净含量:450克", "bbox": [141, 674, 167, 677], "label": "text"},
	{"text": "¥2.9 专享价 ¥7.5", "bbox": [273, 673, 505, 689], "label": "text"},
	{"text": "省4.60元", "bbox": [859, 658, 955, 669], "label": "text"},
	{"text": "一键购买", "bbox": [826, 673, 935, 686], "label": "text"},
	{"text": "查看更多推荐 v", "bbox": [400, 712, 596, 726], "label": "text"},
	{"text": "商品金额", "bbox": [37, 772, 164, 788], "label": "text"},
	{"text": "¥249.00", "bbox": [800, 773, 915, 787], "label": "text"},
	{"text": "运费", "bbox": [37, 810, 99, 826], "label": "text"},
	{"text": "¥0.00", "bbox": [835, 811, 915, 825], "label": "text"},
	{"text": "优惠券", "bbox": [37, 847, 131, 863], "label": "text"},
	{"text": "无可用 >", "bbox": [818, 847, 955, 863], "label": "text"},
	{"text": "已隐藏本单不可使用的虚拟资产 v", "bbox": [292, 882, 707, 896], "label": "text"},
	{"text": "提交订单 ¥249.00", "bbox": [355, 925, 640, 944], "label": "text"}
]
2026-08-10 11:21:21,056 INFO     29 [qwen-vl-text] coord API: raw_items=46, valid_items=46, elapsed=15.2s
2026-08-10 11:21:21,056 INFO     29 [qwen-vl-text] coord item[0]: text=13:19, bbox=[134, 23, 238, 40]
2026-08-10 11:21:21,056 INFO     29 [qwen-vl-text] coord item[1]: text=5G 49, bbox=[707, 23, 900, 40]
2026-08-10 11:21:21,056 INFO     29 [qwen-vl-text] coord item[2]: text=<, bbox=[55, 73, 78, 90]
2026-08-10 11:21:21,056 INFO     29 [qwen-vl-text] coord item[3]: text=哮喘用药热卖榜第4名, bbox=[373, 73, 683, 90]
2026-08-10 11:21:21,056 INFO     29 [qwen-vl-text] coord item[4]: text=85****3662, bbox=[164, 163, 342, 177]
2026-08-10 11:21:21,056 INFO     29 [qwen-vl-text] coord item[5]: text=自营 京东自营药房, bbox=[41, 228, 287, 243]
2026-08-10 11:21:21,056 INFO     29 [qwen-vl-text] coord item[6]: text=普通内科处方单131900332246895 距失效还剩71:59:43, bbox=[64, 268, 783, 282]
2026-08-10 11:21:21,056 INFO     29 [qwen-vl-text] coord item[7]: text=京东买药 AstraZeneca, bbox=[41, 301, 150, 308]
2026-08-10 11:21:21,056 INFO     29 [qwen-vl-text] coord item[8]: text=【原研进口】信必可 布地奈德福莫特..., bbox=[248, 305, 778, 322]
2026-08-10 11:21:21,056 INFO     29 [qwen-vl-text] coord item[9]: text=1, bbox=[885, 308, 897, 319]
2026-08-10 11:21:21,056 INFO     29 [qwen-vl-text] coord item[10]: text=原研正品, bbox=[55, 325, 95, 331]
2026-08-10 11:21:21,056 INFO     29 [qwen-vl-text] coord item[11]: text=多仓发货, bbox=[55, 336, 95, 342]
2026-08-10 11:21:21,056 INFO     29 [qwen-vl-text] coord item[12]: text=品质保障, bbox=[55, 345, 95, 351]
2026-08-10 11:21:21,056 INFO     29 [qwen-vl-text] coord item[13]: text=适3盒装 有金特贴到手价, bbox=[55, 354, 95, 360]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[14]: text=220, bbox=[57, 360, 88, 367]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[15]: text=元, bbox=[91, 363, 98, 367]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[16]: text=1盒装(体验/应急装), bbox=[250, 331, 502, 345]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[17]: text=不支持7天无理由退货, bbox=[250, 353, 500, 366]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[18]: text=¥249, bbox=[250, 375, 341, 393]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[19]: text=服务, bbox=[37, 415, 99, 431]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[20]: text=可选一年囤货补贴共5项 >, bbox=[579, 415, 955, 430]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[21]: text=配送, bbox=[37, 448, 99, 464]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[22]: text=京东快递 >, bbox=[794, 448, 955, 464]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[23]: text=2月25日 [周三] 09:00-21:00, bbox=[527, 470, 921, 487]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[24]: text=收货方式, bbox=[37, 507, 164, 523]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[25]: text=送货上门 >, bbox=[796, 507, 955, 523]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[26]: text=顺手买更划算 ①, bbox=[37, 568, 287, 584]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[27]: text=抑菌洗手液倍护滋润保湿持久留香, bbox=[273, 598, 754, 614]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[28]: text=450克*1瓶【体验装】, bbox=[273, 620, 527, 634]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[29]: text=80%用户顺手买过, bbox=[273, 640, 502, 654]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[30]: text=Weichi, bbox=[120, 650, 160, 656]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[31]: text=HAND SANITIZER, bbox=[141, 664, 181, 668]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[32]: text=抑菌洗手液, bbox=[141, 669, 173, 673]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[33]: text=净含量:450克, bbox=[141, 674, 167, 677]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[34]: text=¥2.9 专享价 ¥7.5, bbox=[273, 673, 505, 689]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[35]: text=省4.60元, bbox=[859, 658, 955, 669]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[36]: text=一键购买, bbox=[826, 673, 935, 686]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[37]: text=查看更多推荐 v, bbox=[400, 712, 596, 726]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[38]: text=商品金额, bbox=[37, 772, 164, 788]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[39]: text=¥249.00, bbox=[800, 773, 915, 787]
2026-08-10 11:21:21,057 INFO     29 [qwen-vl-text] coord item[40]: text=运费, bbox=[37, 810, 99, 826]
2026-08-10 11:21:21,058 INFO     29 [qwen-vl-text] coord item[41]: text=¥0.00, bbox=[835, 811, 915, 825]
2026-08-10 11:21:21,058 INFO     29 [qwen-vl-text] coord item[42]: text=优惠券, bbox=[37, 847, 131, 863]
2026-08-10 11:21:21,058 INFO     29 [qwen-vl-text] coord item[43]: text=无可用 >, bbox=[818, 847, 955, 863]
2026-08-10 11:21:21,058 INFO     29 [qwen-vl-text] coord item[44]: text=已隐藏本单不可使用的虚拟资产 v, bbox=[292, 882, 707, 896]
2026-08-10 11:21:21,058 INFO     29 [qwen-vl-text] coord item[45]: text=提交订单 ¥249.00, bbox=[355, 925, 640, 944]
2026-08-10 11:21:21,058 INFO     29 [qwen-vl-text] page=6 — 47/47 coords, api_time=15.2s
2026-08-10 11:21:21,059 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=463899, prompt_len=1089
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共36行）
["电子发票(普通发票)", "国家税务总局", "辽宁省税务局", "发票号码: 26217000000097645604", "开票日期: 2026年02月25日", "购买方信息", "名称: 个人", "统一社会信用代码/纳税人识别号:", "销售方信息", "名称: 京东大药房(沈阳)有限公司", "统一社会信用代码/纳税人识别号: 91210112MA10499C0F", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*化学药品制剂*【原研进口】信必可布地奈德福莫特罗吸入粉雾剂(II) 320μg:9μg*60吸/盒", "布地奈德福莫特罗吸入粉雾剂(II)", "盒", "1", "220.35", "220.35", "13%", "28.65", "合计", "¥220.35", "¥28.65", "价税合计(大写)", "贰佰肆拾玖圆整", "(小写) ¥249.00", "备注", "订单号:3419204018592466", "开票人: 王梅"]

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
2026-08-10 11:21:40,007 INFO     29 [qwen-vl-text] coord API raw response (len=3267):
[
	{"text": "电子发票(普通发票)", "bbox": [356, 67, 663, 122], "bbox_2d": [356, 67, 663, 122]},
	{"text": "国家税务总局", "bbox": [447, 115, 520, 134], "bbox_2d": [447, 115, 520, 134]},
	{"text": "辽宁省税务局", "bbox": [450, 154, 518, 174], "bbox_2d": [450, 154, 518, 174]},
	{"text": "发票号码: 26217000000097645604", "bbox": [742, 64, 944, 85], "bbox_2d": [742, 64, 944, 85]},
	{"text": "开票日期: 2026年02月25日", "bbox": [742, 101, 904, 122], "bbox_2d": [742, 101, 904, 122]},
	{"text": "购买方信息", "bbox": [39, 215, 53, 345], "bbox_2d": [39, 215, 53, 345]},
	{"text": "名称: 个人", "bbox": [64, 241, 139, 262], "bbox_2d": [64, 241, 139, 262]},
	{"text": "统一社会信用代码/纳税人识别号:", "bbox": [64, 308, 285, 330], "bbox_2d": [64, 308, 285, 330]},
	{"text": "销售方信息", "bbox": [508, 215, 522, 345], "bbox_2d": [508, 215, 522, 345]},
	{"text": "名称: 京东大药房(沈阳)有限公司", "bbox": [531, 241, 750, 262], "bbox_2d": [531, 241, 750, 262]},
	{"text": "统一社会信用代码/纳税人识别号: 91210112MA10499C0F", "bbox": [531, 308, 899, 330], "bbox_2d": [531, 308, 899, 330]},
	{"text": "项目名称", "bbox": [92, 364, 151, 384], "bbox_2d": [92, 364, 151, 384]},
	{"text": "规格型号", "bbox": [257, 364, 317, 384], "bbox_2d": [257, 364, 317, 384]},
	{"text": "单位", "bbox": [379, 364, 409, 384], "bbox_2d": [379, 364, 409, 384]},
	{"text": "数量", "bbox": [502, 364, 534, 384], "bbox_2d": [502, 364, 534, 384]},
	{"text": "单价", "bbox": [617, 364, 651, 384], "bbox_2d": [617, 364, 651, 384]},
	{"text": "金额", "bbox": [734, 364, 771, 384], "bbox_2d": [734, 364, 771, 384]},
	{"text": "税率/征收率", "bbox": [780, 364, 861, 384], "bbox_2d": [780, 364, 861, 384]},
	{"text": "税额", "bbox": [927, 364, 964, 384], "bbox_2d": [927, 364, 964, 384]},
	{"text": "*化学药品制剂*【原研进口】信必可布地奈德福莫特罗吸入粉雾剂(II) 320μg:9μg*60吸/盒", "bbox": [37, 386, 250, 418], "bbox_2d": [37, 386, 250, 418]},
	{"text": "布地奈德福莫特罗吸入粉雾剂(II)", "bbox": [256, 386, 353, 406], "bbox_2d": [256, 386, 353, 406]},
	{"text": "盒", "bbox": [386, 386, 400, 406], "bbox_2d": [386, 386, 400, 406]},
	{"text": "1", "bbox": [527, 386, 534, 406], "bbox_2d": [527, 386, 534, 406]},
	{"text": "220.35", "bbox": [610, 386, 651, 406], "bbox_2d": [610, 386, 651, 406]},
	{"text": "220.35", "bbox": [730, 386, 771, 406], "bbox_2d": [730, 386, 771, 406]},
	{"text": "13%", "bbox": [803, 386, 820, 406], "bbox_2d": [803, 386, 820, 406]},
	{"text": "28.65", "bbox": [932, 386, 965, 406], "bbox_2d": [932, 386, 965, 406]},
	{"text": "合计", "bbox": [97, 641, 112, 662], "bbox_2d": [97, 641, 112, 662]},
	{"text": "计", "bbox": [163, 641, 177, 662], "bbox_2d": [163, 641, 177, 662]},
	{"text": "¥220.35", "bbox": [672, 638, 724, 658], "bbox_2d": [672, 638, 724, 658]},
	{"text": "¥28.65", "bbox": [920, 638, 965, 658], "bbox_2d": [920, 638, 965, 658]},
	{"text": "价税合计(大写)", "bbox": [88, 688, 185, 709], "bbox_2d": [88, 688, 185, 709]},
	{"text": "贰佰肆拾玖圆整", "bbox": [289, 685, 394, 708], "bbox_2d": [289, 685, 394, 708]},
	{"text": "(小写) ¥249.00", "bbox": [696, 685, 795, 708], "bbox_2d": [696, 685, 795, 708]},
	{"text": "备注", "bbox": [44, 748, 59, 769], "bbox_2d": [44, 748, 59, 769]},
	{"text": "订单号:3419204018592466", "bbox": [67, 731, 189, 748], "bbox_2d": [67, 731, 189, 748]},
	{"text": "注", "bbox": [44, 824, 59, 845], "bbox_2d": [44, 824, 59, 845]},
	{"text": "开票人: 王梅", "bbox": [74, 894, 154, 915], "bbox_2d": [74, 894, 154, 915]}
]
2026-08-10 11:21:40,007 INFO     29 [qwen-vl-text] coord API: raw_items=38, valid_items=38, elapsed=18.9s
2026-08-10 11:21:40,007 INFO     29 [qwen-vl-text] coord item[0]: text=电子发票(普通发票), bbox=[356, 67, 663, 122]
2026-08-10 11:21:40,007 INFO     29 [qwen-vl-text] coord item[1]: text=国家税务总局, bbox=[447, 115, 520, 134]
2026-08-10 11:21:40,007 INFO     29 [qwen-vl-text] coord item[2]: text=辽宁省税务局, bbox=[450, 154, 518, 174]
2026-08-10 11:21:40,007 INFO     29 [qwen-vl-text] coord item[3]: text=发票号码: 26217000000097645604, bbox=[742, 64, 944, 85]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[4]: text=开票日期: 2026年02月25日, bbox=[742, 101, 904, 122]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[5]: text=购买方信息, bbox=[39, 215, 53, 345]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[6]: text=名称: 个人, bbox=[64, 241, 139, 262]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[7]: text=统一社会信用代码/纳税人识别号:, bbox=[64, 308, 285, 330]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[8]: text=销售方信息, bbox=[508, 215, 522, 345]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[9]: text=名称: 京东大药房(沈阳)有限公司, bbox=[531, 241, 750, 262]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[10]: text=统一社会信用代码/纳税人识别号: 91210112MA10499C0F, bbox=[531, 308, 899, 330]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[11]: text=项目名称, bbox=[92, 364, 151, 384]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[12]: text=规格型号, bbox=[257, 364, 317, 384]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[13]: text=单位, bbox=[379, 364, 409, 384]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[14]: text=数量, bbox=[502, 364, 534, 384]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[15]: text=单价, bbox=[617, 364, 651, 384]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[16]: text=金额, bbox=[734, 364, 771, 384]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[17]: text=税率/征收率, bbox=[780, 364, 861, 384]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[18]: text=税额, bbox=[927, 364, 964, 384]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[19]: text=*化学药品制剂*【原研进口】信必可布地奈德福莫特罗吸入粉雾剂(II) 320μg:9μg*60吸/盒, bbox=[37, 386, 250, 418]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[20]: text=布地奈德福莫特罗吸入粉雾剂(II), bbox=[256, 386, 353, 406]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[21]: text=盒, bbox=[386, 386, 400, 406]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[22]: text=1, bbox=[527, 386, 534, 406]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[23]: text=220.35, bbox=[610, 386, 651, 406]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[24]: text=220.35, bbox=[730, 386, 771, 406]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[25]: text=13%, bbox=[803, 386, 820, 406]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[26]: text=28.65, bbox=[932, 386, 965, 406]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[27]: text=合计, bbox=[97, 641, 112, 662]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[28]: text=计, bbox=[163, 641, 177, 662]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[29]: text=¥220.35, bbox=[672, 638, 724, 658]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[30]: text=¥28.65, bbox=[920, 638, 965, 658]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[31]: text=价税合计(大写), bbox=[88, 688, 185, 709]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[32]: text=贰佰肆拾玖圆整, bbox=[289, 685, 394, 708]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[33]: text=(小写) ¥249.00, bbox=[696, 685, 795, 708]
2026-08-10 11:21:40,008 INFO     29 [qwen-vl-text] coord item[34]: text=备注, bbox=[44, 748, 59, 769]
2026-08-10 11:21:40,009 INFO     29 [qwen-vl-text] coord item[35]: text=订单号:3419204018592466, bbox=[67, 731, 189, 748]
2026-08-10 11:21:40,009 INFO     29 [qwen-vl-text] coord item[36]: text=注, bbox=[44, 824, 59, 845]
2026-08-10 11:21:40,009 INFO     29 [qwen-vl-text] coord item[37]: text=开票人: 王梅, bbox=[74, 894, 154, 915]
2026-08-10 11:21:40,009 INFO     29 [qwen-vl-text] page=7 — 36/36 coords, api_time=18.9s
2026-08-10 11:21:40,009 INFO     29 [qwen-vl-text] new_positions (85):
[[5, 269.0665732421875, 404.1951398925781, 1176.5437910156252, 1224.2763790283204], [5, 435.1497014160156, 570.2782680664062, 1176.5437910156252, 1224.2763790283204], [6, 79.76752392578125, 141.67664697265624, 29.694838989257814, 51.6431982421875], [6, 420.8629807128906, 535.7520263671875, 29.694838989257814, 51.6431982421875], [6, 32.740401611328124, 46.43184228515625, 94.24883679199219, 116.19719604492188], [6, 222.03945092773435, 406.5762600097656, 94.24883679199219, 116.19719604492188], [6, 97.62592480468749, 203.58577001953122, 210.44603283691407, 228.5211522216797], [6, 24.40648120117187, 170.84536840820311, 294.36622998046874, 313.7324293212891], [6, 38.097921875, 466.10426293945306, 346.00942822265625, 364.0845476074219], [6, 24.40648120117187, 89.29200439453125, 388.6150667724609, 397.65262646484376], [6, 147.629447265625, 463.1278627929687, 393.7793865966797, 415.7277458496094], [6, 526.8228259277344, 533.9661862792968, 397.65262646484376, 411.8545059814453], [6, 32.740401611328124, 56.55160278320312, 419.6009857177734, 427.34746545410155], [6, 32.740401611328124, 56.55160278320312, 433.802865234375, 441.54934497070315], [6, 32.740401611328124, 56.55160278320312, 445.4225848388672, 453.1690645751953], [6, 32.740401611328124, 56.55160278320312, 457.0423044433594, 464.7887841796875], [6, 33.93096166992187, 52.384642578124996, 464.7887841796875, 473.8263438720703], [6, 54.17048266601562, 58.33744287109374, 468.66202404785156, 473.8263438720703], [6, 148.82000732421875, 298.83057470703125, 427.34746545410155, 445.4225848388672], [6, 148.82000732421875, 297.6400146484375, 455.7512244873047, 472.53526391601565], [6, 148.82000732421875, 202.99048999023435, 484.1549835205078, 507.3944227294922], [6, 22.02536108398437, 58.93272290039062, 535.7981817626953, 556.4554610595703], [6, 344.6671369628906, 568.4924279785156, 535.7981817626953, 555.1643811035157], [6, 22.02536108398437, 58.93272290039062, 578.4038203125, 599.061099609375], [6, 472.6523432617187, 568.4924279785156, 578.4038203125, 599.061099609375], [6, 313.7125754394531, 548.2529069824218, 606.8075793457032, 628.7559385986328], [6, 22.02536108398437, 97.62592480468749, 654.5775377197266, 675.2348170166016], [6, 473.8429033203125, 568.4924279785156, 654.5775377197266, 675.2348170166016], [6, 22.02536108398437, 170.84536840820311, 733.3334150390625, 753.9906943359375], [6, 162.51144799804686, 448.84114208984374, 772.0658137207031, 792.7230930175781], [6, 162.51144799804686, 313.7125754394531, 800.4695727539063, 818.5446921386718], [6, 162.51144799804686, 298.83057470703125, 826.291171875, 844.3662912597656], [6, 71.433603515625, 95.2448046875, 839.2019714355469, 846.948451171875], [6, 83.93448413085937, 107.74568530273437, 857.2770908203125, 862.4414106445313], [6, 83.93448413085937, 102.98344506835937, 863.732490600586, 868.8968104248047], [6, 83.93448413085937, 99.41176489257812, 870.1878903808594, 874.0611302490234], [6, 162.51144799804686, 300.61641479492187, 868.8968104248047, 889.5540897216797], [6, 511.3455451660156, 568.4924279785156, 849.5306110839844, 863.732490600586], [6, 491.7013041992187, 556.5868273925781, 868.8968104248047, 885.6808498535156], [6, 238.11201171874998, 354.7868974609375, 919.2489287109375, 937.3240480957031], [6, 22.02536108398437, 97.62592480468749, 996.7137260742187, 1017.3710053710937], [6, 476.22402343749997, 544.6812268066406, 998.0048060302735, 1016.079925415039], [6, 22.02536108398437, 58.93272290039062, 1045.7747644042968, 1066.4320437011718], [6, 497.0588244628906, 544.6812268066406, 1047.0658443603515, 1065.1409637451172], [6, 22.02536108398437, 77.98168383789061, 1093.5447227783204, 1114.2020020751954], [6, 486.93906396484374, 568.4924279785156, 1093.5447227783204, 1114.2020020751954], [6, 173.82176855468748, 420.8629807128906, 1138.7325212402343, 1156.807640625], [6, 211.3244104003906, 380.97921875, 1194.248959350586, 1218.779478515625], [6, 211.3244104003906, 380.97921875, 1194.248959350586, 1218.779478515625], [7, 299.71284521484375, 558.173079711914, 37.21180163574219, 67.75880297851563], [7, 376.32483654785153, 437.7828076171875, 63.871002807617195, 74.42360327148438], [7, 378.8505065917969, 436.09902758789065, 85.53160375976563, 96.63960424804688], [7, 624.6823908691406, 794.744173828125, 35.5456015625, 47.209002075195315], [7, 624.6823908691406, 761.0685732421875, 56.09540246582032, 67.75880297851563], [7, 32.83371057128906, 44.62017077636719, 119.41100524902345, 191.61300842285158], [7, 53.8809609375, 117.02271203613282, 133.85140588378908, 145.5148063964844], [7, 53.8809609375, 239.9386541748047, 171.06320751953126, 183.28200805664065], [7, 427.6801274414062, 439.46658764648436, 119.41100524902345, 191.61300842285158], [7, 447.0435977783203, 631.4175109863281, 133.85140588378908, 145.5148063964844], [7, 447.0435977783203, 756.8591231689453, 171.06320751953126, 183.28200805664065], [7, 77.45388134765625, 127.12539221191406, 202.16560888671876, 213.27360937500004], [7, 216.36573376464844, 266.87913464355466, 202.16560888671876, 213.27360937500004], [7, 319.07631555175783, 344.3330159912109, 202.16560888671876, 213.27360937500004], [7, 422.62878735351563, 449.5692678222656, 202.16560888671876, 213.27360937500004], [7, 519.4461390380859, 548.0703995361328, 202.16560888671876, 213.27360937500004], [7, 617.9472707519532, 649.0972012939453, 202.16560888671876, 213.27360937500004], [7, 656.6742114257812, 724.8673026123047, 202.16560888671876, 213.27360937500004], [7, 780.4320435791016, 811.5819741210937, 202.16560888671876, 213.27360937500004], [7, 31.149930541992187, 210.47250366210938, 214.38440942382815, 232.15721020507814], [7, 215.52384375, 297.18717517089846, 214.38440942382815, 225.4924099121094], [7, 324.9695456542969, 336.756005859375, 214.38440942382815, 225.4924099121094], [7, 443.67603771972654, 449.5692678222656, 214.38440942382815, 225.4924099121094], [7, 513.5529089355468, 548.0703995361328, 214.38440942382815, 225.4924099121094], [7, 614.5797106933594, 649.0972012939453, 214.38440942382815, 225.4924099121094], [7, 676.0376817626953, 690.3498120117188, 214.38440942382815, 225.4924099121094], [7, 784.6414936523438, 812.4238641357422, 214.38440942382815, 225.4924099121094], [7, 81.66333142089843, 94.291681640625, 356.0114156494141, 367.67481616210944], [7, 137.2280723876953, 149.01453259277343, 356.0114156494141, 367.67481616210944], [7, 565.75008984375, 609.5283706054687, 354.3452155761719, 365.45321606445316], [7, 774.5388134765625, 812.4238641357422, 354.3452155761719, 365.45321606445316], [7, 74.0863212890625, 155.74965270996094, 382.115216796875, 393.77861730957034], [7, 243.30621423339844, 331.7046657714844, 380.44901672363284, 393.2232172851563], [7, 585.9554501953124, 669.3025616455078, 380.44901672363284, 393.2232172851563], [7, 37.04316064453125, 49.67151086425781, 415.4392182617188, 427.1026187744141], [7, 56.40663098144531, 159.11721276855468, 405.99741784667975, 415.4392182617188]]
2026-08-10 11:21:40,009 INFO     29 [qwen-vl-text] ═══ DONE ═══ 85 positions, pages=3, time=38.6s
2026-08-10 11:21:40,009 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:21:40,016 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:21:40,016 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 11:21:40,016 INFO     29 [qwen-vl-text] positions(18): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:21:40,016 INFO     29 [qwen-vl-text] page grouping: [8], lines per page: [18]
2026-08-10 11:21:40,466 INFO     29 [qwen-vl-text] page=8, rect=595x794, img=(1654x2205), dpi=200
2026-08-10 11:21:40,468 INFO     29 [qwen-vl-text] LLM extraction start, text_len=243
2026-08-10 11:21:40,468 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:21:40,469 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 178, \"bbox_end\": 195, \"encounter_dates\": [\"2025-12-01\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "芳草大药房(孤岛路店)\n欢迎光临\n顾客姓名:\n流水号:\n001LS202512010064\n品名 数量 单价 小计\n布地奈德福莫特罗吸入粉雾剂(Ⅱ)\n1 244.0 244.0\nP202504 2028-03\n规格: 320ug:9ug*60吸\n厂家: AstraZeneca AB\n总计: 244.00 件数: 1\n累计折扣: 0.00\n实收: 244.00\n收来: 250.00 找还: 6.00\n收款人: 00015\n2025/12/01 09:11:26\n除药品质量原因不得退换",
    "role": "user"
  }
]
2026-08-10 11:21:40,474 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:21:40.472+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 20, "failed": 0, "current": {"5e62f0e694ad11f1bd9827cf206dfa2d": {"id": "5e62f0e694ad11f1bd9827cf206dfa2d", "doc_id": "5ddcc2a094ad11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "lsju-\u54ee\u5598-\u6c88\u9633(1).pdf", "type": "pdf", "location": "lsju-\u54ee\u5598-\u6c88\u9633(1).pdf", "size": 3913176, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786360775902, "task_type": "dataflow", "root_trace_id": "7d6dcbad8e7b45c1949a5dd052ab4409", "root_traceparent": "00-7d6dcbad8e7b45c1949a5dd052ab4409-9207ab8c386eb81c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:21:42,664 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:21:42,664 INFO     29 [qwen-vl-text] LLM output (len=441):
{
  "encounter_date": "2025-12-01",
  "pharmacy": "芳草大药房(孤岛路店)",
  "medications": [
    {
      "name": "布地奈德福莫特罗吸入粉雾剂(Ⅱ)",
      "specification": "320ug:9ug*60吸",
      "dosage": null,
      "quantity": 1,
      "unit_price": 244.0,
      "total_price": 244.0,
      "frequency": null,
      "route": null,
      "manufacturer": "AstraZeneca AB",
      "approval_number": null
    }
  ],
  "payment_total": 244.0,
  "payment_method": null
}
2026-08-10 11:21:42,664 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-01]
2026-08-10 11:21:42,676 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4987680, prompt_len=910
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共18行）
["芳草大药房(孤岛路店)", "欢迎光临", "顾客姓名:", "流水号:", "001LS202512010064", "品名 数量 单价 小计", "布地奈德福莫特罗吸入粉雾剂(Ⅱ)", "1 244.0 244.0", "P202504 2028-03", "规格: 320ug:9ug*60吸", "厂家: AstraZeneca AB", "总计: 244.00 件数: 1", "累计折扣: 0.00", "实收: 244.00", "收来: 250.00 找还: 6.00", "收款人: 00015", "2025/12/01 09:11:26", "除药品质量原因不得退换"]

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
2026-08-10 11:21:49,085 INFO     29 [qwen-vl-text] coord API raw response (len=1034):
```json
[
	{"text": "芳草大药房(孤岛路店)", "bbox": [26, 214, 333, 244]},
	{"text": "欢迎光临", "bbox": [134, 269, 299, 293]},
	{"text": "顾客姓名:", "bbox": [32, 318, 132, 341]},
	{"text": "流水号:", "bbox": [36, 354, 112, 376]},
	{"text": "001LS202512010064", "bbox": [38, 390, 225, 408]},
	{"text": "品名 数量 单价 小计", "bbox": [39, 421, 309, 442]},
	{"text": "布地奈德福莫特罗吸入粉雾剂(Ⅱ)", "bbox": [40, 455, 352, 476]},
	{"text": "1 244.0 244.0", "bbox": [154, 490, 310, 508]},
	{"text": "P202504 2028-03", "bbox": [40, 523, 269, 541]},
	{"text": "规格: 320ug:9ug*60吸", "bbox": [40, 555, 256, 576]},
	{"text": "厂家: AstraZeneca AB", "bbox": [40, 588, 254, 609]},
	{"text": "总计: 244.00 件数: 1", "bbox": [41, 619, 309, 642]},
	{"text": "累计折扣: 0.00", "bbox": [41, 656, 195, 679]},
	{"text": "实收: 244.00", "bbox": [39, 690, 173, 714]},
	{"text": "收来: 250.00 找还: 6.00", "bbox": [36, 719, 308, 749]},
	{"text": "收款人: 00015", "bbox": [34, 758, 190, 789]},
	{"text": "2025/12/01 09:11:26", "bbox": [31, 807, 245, 845]},
	{"text": "除药品质量原因不得退换", "bbox": [98, 852, 333, 893]}
]
```
2026-08-10 11:21:49,086 INFO     29 [qwen-vl-text] coord API: raw_items=18, valid_items=18, elapsed=6.4s
2026-08-10 11:21:49,086 INFO     29 [qwen-vl-text] coord item[0]: text=芳草大药房(孤岛路店), bbox=[26, 214, 333, 244]
2026-08-10 11:21:49,086 INFO     29 [qwen-vl-text] coord item[1]: text=欢迎光临, bbox=[134, 269, 299, 293]
2026-08-10 11:21:49,086 INFO     29 [qwen-vl-text] coord item[2]: text=顾客姓名:, bbox=[32, 318, 132, 341]
2026-08-10 11:21:49,086 INFO     29 [qwen-vl-text] coord item[3]: text=流水号:, bbox=[36, 354, 112, 376]
2026-08-10 11:21:49,086 INFO     29 [qwen-vl-text] coord item[4]: text=001LS202512010064, bbox=[38, 390, 225, 408]
2026-08-10 11:21:49,086 INFO     29 [qwen-vl-text] coord item[5]: text=品名 数量 单价 小计, bbox=[39, 421, 309, 442]
2026-08-10 11:21:49,086 INFO     29 [qwen-vl-text] coord item[6]: text=布地奈德福莫特罗吸入粉雾剂(Ⅱ), bbox=[40, 455, 352, 476]
2026-08-10 11:21:49,086 INFO     29 [qwen-vl-text] coord item[7]: text=1 244.0 244.0, bbox=[154, 490, 310, 508]
2026-08-10 11:21:49,086 INFO     29 [qwen-vl-text] coord item[8]: text=P202504 2028-03, bbox=[40, 523, 269, 541]
2026-08-10 11:21:49,086 INFO     29 [qwen-vl-text] coord item[9]: text=规格: 320ug:9ug*60吸, bbox=[40, 555, 256, 576]
2026-08-10 11:21:49,086 INFO     29 [qwen-vl-text] coord item[10]: text=厂家: AstraZeneca AB, bbox=[40, 588, 254, 609]
2026-08-10 11:21:49,086 INFO     29 [qwen-vl-text] coord item[11]: text=总计: 244.00 件数: 1, bbox=[41, 619, 309, 642]
2026-08-10 11:21:49,086 INFO     29 [qwen-vl-text] coord item[12]: text=累计折扣: 0.00, bbox=[41, 656, 195, 679]
2026-08-10 11:21:49,086 INFO     29 [qwen-vl-text] coord item[13]: text=实收: 244.00, bbox=[39, 690, 173, 714]
2026-08-10 11:21:49,086 INFO     29 [qwen-vl-text] coord item[14]: text=收来: 250.00 找还: 6.00, bbox=[36, 719, 308, 749]
2026-08-10 11:21:49,086 INFO     29 [qwen-vl-text] coord item[15]: text=收款人: 00015, bbox=[34, 758, 190, 789]
2026-08-10 11:21:49,086 INFO     29 [qwen-vl-text] coord item[16]: text=2025/12/01 09:11:26, bbox=[31, 807, 245, 845]
2026-08-10 11:21:49,086 INFO     29 [qwen-vl-text] coord item[17]: text=除药品质量原因不得退换, bbox=[98, 852, 333, 893]
2026-08-10 11:21:49,087 INFO     29 [qwen-vl-text] page=8 — 18/18 coords, api_time=6.4s
2026-08-10 11:21:49,087 INFO     29 [qwen-vl-text] new_positions (18):
[[8, 15.477280761718749, 198.22824975585937, 169.85180261230468, 193.66280297851563], [8, 79.76752392578125, 177.98872875976562, 213.5053032836914, 232.55410357666014], [8, 19.0489609375, 78.57696386718749, 252.39660388183594, 270.65170416259764], [8, 21.4300810546875, 66.67136328125, 280.9698043212891, 298.43120458984373], [8, 22.62064111328125, 133.93800659179686, 309.5430047607422, 323.82960498046873], [8, 23.215921142578125, 183.94152905273435, 334.14770513916017, 350.8154053955078], [8, 23.811201171875, 209.53857031249998, 361.1335055541992, 377.8012058105469], [8, 91.67312451171874, 184.53680908203123, 388.9130059814453, 403.1996062011719], [8, 23.811201171875, 160.13032788085937, 415.10510638427735, 429.3917066040039], [8, 23.811201171875, 152.3916875, 440.50350677490235, 457.17120703125], [8, 23.811201171875, 151.20112744140624, 466.69560717773436, 483.363307434082], [8, 24.40648120117187, 183.94152905273435, 491.30030755615235, 509.55540783691407], [8, 24.40648120117187, 116.07960571289061, 520.6672080078125, 538.9223082885742], [8, 23.215921142578125, 102.98344506835937, 547.6530084228516, 566.7018087158203], [8, 21.4300810546875, 183.34624902343748, 570.6703087768554, 594.4813091430664], [8, 20.23952099609375, 113.10320556640625, 601.6246092529296, 626.2293096313476], [8, 18.453680908203125, 145.84360717773436, 640.5159098510742, 670.6765103149414], [8, 58.33744287109374, 198.22824975585937, 676.2324104003906, 708.7741109008789]]
2026-08-10 11:21:49,087 INFO     29 [qwen-vl-text] ═══ DONE ═══ 18 positions, pages=1, time=9.1s
2026-08-10 11:21:49,087 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:21:49,088 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:21:49,088 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 11:21:49,088 INFO     29 [qwen-vl-text] positions(18): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:21:49,088 INFO     29 [qwen-vl-text] page grouping: [8], lines per page: [18]
2026-08-10 11:21:49,538 INFO     29 [qwen-vl-text] page=8, rect=595x794, img=(1654x2205), dpi=200
2026-08-10 11:21:49,539 INFO     29 [qwen-vl-text] LLM extraction start, text_len=244
2026-08-10 11:21:49,539 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:21:49,539 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 196, \"bbox_end\": 213, \"encounter_dates\": [\"2025-12-30\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "芳草大药房(孤岛路店)\n欢迎光临\n顾客姓名:\n流水号:\n001LS202512301135\n品名 数量 单价 小计\n布地奈德福莫特罗吸入粉雾剂(Ⅱ)\n2 244.0 488.0\nP202504 2028-03\n规格: 320ug:9ug*60吸\n厂家: AstraZeneca AB\n总计: 488.00 件数: 2\n累计折扣: 0.00\n实收: 488.00\n收来: 500.00 找还: 12.00\n收款人: 00015\n2025/12/30 18:04:32\n除药品质量原因不得退换",
    "role": "user"
  }
]
2026-08-10 11:21:51,858 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:21:51,858 INFO     29 [qwen-vl-text] LLM output (len=446):
{
  "encounter_date": "2025-12-30",
  "pharmacy": "芳草大药房(孤岛路店)",
  "medications": [
    {
      "name": "布地奈德福莫特罗吸入粉雾剂(Ⅱ)",
      "specification": "320ug:9ug*60吸",
      "dosage": null,
      "quantity": 2,
      "unit_price": 244.0,
      "total_price": 488.0,
      "frequency": null,
      "route": null,
      "manufacturer": "AstraZeneca AB",
      "approval_number": "P202504"
    }
  ],
  "payment_total": 488.0,
  "payment_method": null
}
2026-08-10 11:21:51,858 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-30]
2026-08-10 11:21:51,870 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=4987680, prompt_len=911
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共18行）
["芳草大药房(孤岛路店)", "欢迎光临", "顾客姓名:", "流水号:", "001LS202512301135", "品名 数量 单价 小计", "布地奈德福莫特罗吸入粉雾剂(Ⅱ)", "2 244.0 488.0", "P202504 2028-03", "规格: 320ug:9ug*60吸", "厂家: AstraZeneca AB", "总计: 488.00 件数: 2", "累计折扣: 0.00", "实收: 488.00", "收来: 500.00 找还: 12.00", "收款人: 00015", "2025/12/30 18:04:32", "除药品质量原因不得退换"]

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
2026-08-10 11:21:57,574 INFO     29 [qwen-vl-text] coord API raw response (len=1039):
[
	{"text": "芳草大药房(孤岛路店)", "bbox": [534, 233, 863, 265]},
	{"text": "欢迎光临", "bbox": [629, 283, 818, 309]},
	{"text": "顾客姓名:", "bbox": [518, 331, 618, 355]},
	{"text": "流水号:", "bbox": [517, 367, 592, 390]},
	{"text": "001LS202512301135", "bbox": [515, 404, 711, 427]},
	{"text": "品名 数量 单价 小计", "bbox": [515, 436, 791, 460]},
	{"text": "布地奈德福莫特罗吸入粉雾剂(Ⅱ)", "bbox": [512, 467, 827, 490]},
	{"text": "2 244.0 488.0", "bbox": [618, 503, 785, 521]},
	{"text": "P202504 2028-03", "bbox": [511, 535, 740, 555]},
	{"text": "规格: 320ug:9ug*60吸", "bbox": [513, 567, 723, 590]},
	{"text": "厂家: AstraZeneca AB", "bbox": [518, 597, 723, 624]},
	{"text": "总计: 488.00 件数: 2", "bbox": [520, 630, 781, 662]},
	{"text": "累计折扣: 0.00", "bbox": [520, 667, 671, 692]},
	{"text": "实收: 488.00", "bbox": [521, 701, 660, 721]},
	{"text": "收来: 500.00 找还: 12.00", "bbox": [528, 733, 815, 762]},
	{"text": "收款人: 00015", "bbox": [529, 772, 684, 798]},
	{"text": "2025/12/30 18:04:32", "bbox": [524, 835, 740, 859]},
	{"text": "除药品质量原因不得退换", "bbox": [588, 892, 847, 919]}
]
2026-08-10 11:21:57,574 INFO     29 [qwen-vl-text] coord API: raw_items=18, valid_items=18, elapsed=5.7s
2026-08-10 11:21:57,574 INFO     29 [qwen-vl-text] coord item[0]: text=芳草大药房(孤岛路店), bbox=[534, 233, 863, 265]
2026-08-10 11:21:57,574 INFO     29 [qwen-vl-text] coord item[1]: text=欢迎光临, bbox=[629, 283, 818, 309]
2026-08-10 11:21:57,575 INFO     29 [qwen-vl-text] coord item[2]: text=顾客姓名:, bbox=[518, 331, 618, 355]
2026-08-10 11:21:57,575 INFO     29 [qwen-vl-text] coord item[3]: text=流水号:, bbox=[517, 367, 592, 390]
2026-08-10 11:21:57,575 INFO     29 [qwen-vl-text] coord item[4]: text=001LS202512301135, bbox=[515, 404, 711, 427]
2026-08-10 11:21:57,575 INFO     29 [qwen-vl-text] coord item[5]: text=品名 数量 单价 小计, bbox=[515, 436, 791, 460]
2026-08-10 11:21:57,575 INFO     29 [qwen-vl-text] coord item[6]: text=布地奈德福莫特罗吸入粉雾剂(Ⅱ), bbox=[512, 467, 827, 490]
2026-08-10 11:21:57,575 INFO     29 [qwen-vl-text] coord item[7]: text=2 244.0 488.0, bbox=[618, 503, 785, 521]
2026-08-10 11:21:57,575 INFO     29 [qwen-vl-text] coord item[8]: text=P202504 2028-03, bbox=[511, 535, 740, 555]
2026-08-10 11:21:57,575 INFO     29 [qwen-vl-text] coord item[9]: text=规格: 320ug:9ug*60吸, bbox=[513, 567, 723, 590]
2026-08-10 11:21:57,575 INFO     29 [qwen-vl-text] coord item[10]: text=厂家: AstraZeneca AB, bbox=[518, 597, 723, 624]
2026-08-10 11:21:57,575 INFO     29 [qwen-vl-text] coord item[11]: text=总计: 488.00 件数: 2, bbox=[520, 630, 781, 662]
2026-08-10 11:21:57,575 INFO     29 [qwen-vl-text] coord item[12]: text=累计折扣: 0.00, bbox=[520, 667, 671, 692]
2026-08-10 11:21:57,575 INFO     29 [qwen-vl-text] coord item[13]: text=实收: 488.00, bbox=[521, 701, 660, 721]
2026-08-10 11:21:57,575 INFO     29 [qwen-vl-text] coord item[14]: text=收来: 500.00 找还: 12.00, bbox=[528, 733, 815, 762]
2026-08-10 11:21:57,575 INFO     29 [qwen-vl-text] coord item[15]: text=收款人: 00015, bbox=[529, 772, 684, 798]
2026-08-10 11:21:57,575 INFO     29 [qwen-vl-text] coord item[16]: text=2025/12/30 18:04:32, bbox=[524, 835, 740, 859]
2026-08-10 11:21:57,576 INFO     29 [qwen-vl-text] coord item[17]: text=除药品质量原因不得退换, bbox=[588, 892, 847, 919]
2026-08-10 11:21:57,577 INFO     29 [qwen-vl-text] page=8 — 18/18 coords, api_time=5.7s
2026-08-10 11:21:57,577 INFO     29 [qwen-vl-text] new_positions (18):
[[8, 317.87953564453124, 513.726665283203, 184.93210284423827, 210.33050323486327], [8, 374.43113842773437, 486.93906396484374, 224.61710345458985, 245.25330377197264], [8, 308.3550551757812, 367.8830581054687, 262.71470404052735, 281.7635043334961], [8, 307.75977514648434, 352.40577734374995, 291.28790447998045, 309.5430047607422], [8, 306.5692150878906, 423.2441008300781, 320.6548049316406, 338.90990521240235], [8, 306.5692150878906, 470.8665031738281, 346.0532053222656, 365.10200561523436], [8, 304.783375, 492.2965842285156, 370.6579057006836, 388.9130059814453], [8, 367.8830581054687, 467.29482299804687, 399.2311061401367, 413.51770635986327], [8, 304.1880949707031, 440.50722167968746, 424.6295065307617, 440.50350677490235], [8, 305.37865502929685, 430.3874611816406, 450.0279069213867, 468.28300720214844], [8, 308.3550551757812, 430.3874611816406, 473.83890728759764, 495.26880761718746], [8, 309.54561523437496, 464.9137028808593, 500.0310076904297, 525.4294080810547], [8, 309.54561523437496, 399.4328996582031, 529.3979081420898, 549.2404084472656], [8, 310.14089526367184, 392.8848193359375, 556.3837085571289, 572.2577088012695], [8, 314.30785546874995, 485.15322387695306, 581.7821089477538, 604.7994093017578], [8, 314.9031354980469, 407.17154003906245, 612.7364094238281, 633.3726097412109], [8, 311.92673535156246, 440.50722167968746, 662.7395101928711, 681.7883104858398], [8, 350.02465722656245, 504.20218481445306, 707.9804108886718, 729.4103112182617]]
2026-08-10 11:21:57,577 INFO     29 [qwen-vl-text] ═══ DONE ═══ 18 positions, pages=1, time=8.5s
2026-08-10 11:21:57,591 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 11:21:57,591 INFO     29 [Trace] task=5e62f0e6 | doc=lsju-哮喘-沈阳(1).pdf | Extractor:Medication | outputs={"chunks": "4 items, types={'MedicationRecord': 4}", "html": "", "json": "214 items", "markdown": "", "text": "", "name": "lsju-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-10 11:21:57,591 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 11:21:57,601 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:21:57,601 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:21:58,459 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:21:58,471 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 11:21:58,471 INFO     29 [Trace] task=5e62f0e6 | doc=lsju-哮喘-沈阳(1).pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "214 items", "markdown": "", "text": "", "name": "lsju-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-10 11:21:58,471 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 11:21:58,481 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:21:58,481 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:21:58,944 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:21:58,953 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 11:21:58,953 INFO     29 [Trace] task=5e62f0e6 | doc=lsju-哮喘-沈阳(1).pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "214 items", "markdown": "", "text": "", "name": "lsju-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-10 11:21:58,953 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 11:21:58,960 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:21:58,960 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:21:59,481 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:21:59,497 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 11:21:59,497 INFO     29 [Trace] task=5e62f0e6 | doc=lsju-哮喘-沈阳(1).pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "214 items", "markdown": "", "text": "", "name": "lsju-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-10 11:21:59,497 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 11:21:59,509 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:21:59,509 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:22:00,652 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:22:00,667 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 11:22:00,667 INFO     29 [Trace] task=5e62f0e6 | doc=lsju-哮喘-沈阳(1).pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "214 items", "markdown": "", "text": "", "name": "lsju-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-10 11:22:00,668 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 11:22:00,679 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:22:00,679 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:22:01,215 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:22:01,223 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 11:22:01,223 INFO     29 [Trace] task=5e62f0e6 | doc=lsju-哮喘-沈阳(1).pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "214 items", "markdown": "", "text": "", "name": "lsju-哮喘-沈阳(1).pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Medication": "4 items, types={'MedicationRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Medication\": 4}"}
2026-08-10 11:22:01,223 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 11:22:01,224 INFO     29 [ChunkMerger] Merged 6 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 4, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 7 noise chunks)
2026-08-10 11:22:01,240 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 11:22:01,240 INFO     29 [Trace] task=5e62f0e6 | doc=lsju-哮喘-沈阳(1).pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 2, 'MedicationRecord': 4}", "name": "lsju-哮喘-沈阳(1).pdf"}
2026-08-10 11:22:01,240 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 11:22:01,340 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786360776221, 'update_date': datetime.datetime(2026, 8, 10, 11, 19, 36), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 916338, 'status': '1'}
2026-08-10 11:22:01,546 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=北票成岩中医院
门诊病历
科别：内科门诊 姓名
性别：女 年龄：57岁 门诊号：7260295
职业：农民 婚姻：已婚
药物过敏史：无
住址：辽宁省朝阳市凌源市宋杖子镇马杖子
纪录时间：2026-02-10 09:15
主诉：反复发作咳嗽喘息5年余、加重5天
现病史：患者2020年6月于中国医科大学附属第一医院诊断为支气管哮喘，后规律使用布
地奈德福莫特罗吸入粉雾剂（II）320μg:9μg，1日/2吸。5天前患者受凉后出
现咳嗽喘息症状加重，无发热，日常活动受限，为求进一步诊治来我院。
既往史：支气管哮喘病史5年余。
过敏史：花粉过敏
传染病及流行性病史：无
查体：T36.7℃，P82次/分，R24次/分，BP 125/80 mmHg。双肺呼吸音粗，可闻及广泛呼
气相哮鸣音，未闻及湿性啰音。
辅助检查：
初步诊断：支气管哮喘（急性发作期）
诊疗意见：1.醋酸泼尼松片20mg日1次口服，连续用5天。
2.沙丁胺醇气雾剂2喷/次，每4小时1次，症状缓解后改为按需吸入。
3.布地奈德福莫特罗吸入粉雾剂（II）320μg:9μg,1日/2吸规律吸入
医师签名：
日期：2026年
---
病历记录
以下为中国医科大学附属第一医院门（急）诊病历记录 2021年10月11日 时 分
主诉：反复喘息3年余
现病史：曾于2020年6月到我院就诊，诊断“支气管哮喘”，
目前仍有气短症状，规律使用可必特吸入
日二次吸入，强的松2片日一次口服
既往史：花粉过敏
家庭史：0
体格检查：2021年0平气相喘鸣(+)
病历记录
胸CT(外院)3.221年较前透亮度降低
余未见确切异常
查肺功+舒张+弥散
血气
白常规.0嗜碱细胞296
血气PH7.395.P0266.9P0241.5
肺功:弥散正常
FVC48.6%FEV1.301%
舒张41.6%FEV1.072
病历记录
叩诊:支气管哮鸣(重度)
低氧血症
建议:住院320ug吸入二次吸入
待化验结果
苏新明
---
订单详情
完成
建议您关注病情进展并及时复诊 去复诊 >
再次购买
已签收
您的预约单已签收
185****3662
辽宁朝阳市凌源市宋杖子镇马杖子
京东大药房
联系
满意度调研
药品不支持7天无理由退换货
京东买药
仙琚 醋酸泼尼松片 5mg*100片
数量：1
¥6.90/件
品质保障
多仓发货
正品好药
极速发货
专业药师服务
用药人信息
刘素娟 女 57岁
问诊单
查看详情 >
不良反应登记 京东大药房执业药师提示：合格药品在正常
点击查看您的用药指导
去看看
删除订单
---
查看发票
再次购买
13:19
5G 49
<
哮喘用药热卖榜第4名
85****3662
自营 京东自营药房
普通内科处方单131900332246895 距失效还剩71:59:43
京东买药 AstraZeneca
【原研进口】信必可 布地奈德福莫特...
1
原研正品
多仓发货
品质保障
适3盒装 有金特贴到手价
220
元
320
1盒装(体验/应急装)
不支持7天无理由退货
¥249
服务
可选一年囤货补贴共5项 >
配送
京东快递 >
2月25日 [周三] 09:00-21:00
收货方式
送货上门 >
顺手买更划算 ①
抑菌洗手液倍护滋润保湿持久留香
450克*1瓶【体验装】
80%用户顺手买过
Weichi
HAND SANITIZER
抑菌洗手液
净含量:450克
¥2.9 专享价 ¥7.5
省4.60元
一键购买
查看更多推荐 v
商品金额
¥249.00
运费
¥0.00
优惠券
无可用 >
已隐藏本单不可使用的虚拟资产 v
提交订单 ¥249.00
电子发票(普通发票)
国家税务总局
辽宁省税务局
发票号码: 26217000000097645604
开票日期: 2026年02月25日
购买方信息
名称: 个人
统一社会信用代码/纳税人识别号:
销售方信息
名称: 京东大药房(沈阳)有限公司
统一社会信用代码/纳税人识别号: 91210112MA10499C0F
项目名称
规格型号
单位
数量
单价
金额
税率/征收率
税额
*化学药品制剂*【原研进口】信必可布地奈德福莫特罗吸入粉雾剂(II) 320μg:9μg*60吸/盒
布地奈德福莫特罗吸入粉雾剂(II)
盒
1
220.35
220.35
13%
28.65
合计
¥220.35
¥28.65
价税合计(大写)
贰佰肆拾玖圆整
(小写) ¥249.00
备注
订单号:3419204018592466
开票人: 王梅
---
芳草大药房(孤岛路店)
欢迎光临
顾客姓名:
流水号:
001LS202512010064
品名 数量 单价 小计
布地奈德福莫特罗吸入粉雾剂(Ⅱ)
1 244.0 244.0
P202504 2028-03
规格: 320ug:9ug*60吸
厂家: AstraZeneca AB
总计: 244.00 件数: 1
累计折扣: 0.00
实收: 244.00
收来: 250.00 找还: 6.00
收款人: 00015
2025/12/01 09:11:26
除药品质量原因不得退换
---
芳草大药房(孤岛路店)
欢迎光临
顾客姓名:
流水号:
001LS202512301135
品名 数量 单价 小计
布地奈德福莫特罗吸入粉雾剂(Ⅱ)
2 244.0 488.0
P202504 2028-03
规格: 320ug:9ug*60吸
厂家: AstraZeneca AB
总计: 488.00 件数: 2
累计折扣: 0.00
实收: 488.00
收来: 500.00 找还: 12.00
收款人: 00015
2025/12/30 18:04:32
除药品质量原因不得退换
2026-08-10 11:22:01,904 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 11:22:01,904 INFO     29 [Trace] task=5e62f0e6 | doc=lsju-哮喘-沈阳(1).pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "6 items, types={'OutpatientRecord': 2, 'MedicationRecord': 4}", "name": "lsju-哮喘-沈阳(1).pdf", "embedding_token_consumption": 1938}
2026-08-10 11:22:01,904 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 11:22:02,070 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 11:22:02,070 INFO     29 [Trace] task=5e62f0e6 | doc=lsju-哮喘-沈阳(1).pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":6,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 11:22:02,073 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:22:02,073 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:22:02,073 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:22:02,073 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:22:02,073 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:22:02,073 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:22:02,082 INFO     29 set_progress(5e62f0e694ad11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 11:22:02 [DOC Engine]:
Start to index...
2026-08-10 11:22:02,120 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.034s]
2026-08-10 11:22:02,126 INFO     29 set_progress(5e62f0e694ad11f1bd9827cf206dfa2d), progress: 0.8166666666666668, progress_msg: 
2026-08-10 11:22:02,152 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.021s]
2026-08-10 11:22:02,165 INFO     29 set_progress(5e62f0e694ad11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 11:22:02 Indexing done (0.08s). Task done (141.01s)
2026-08-10 11:22:02,171 INFO     29 [Done], chunks(6), token(1938), elapsed:141.01
2026-08-10 11:22:02,260 INFO     29 handle_task done for task {"id": "5e62f0e694ad11f1bd9827cf206dfa2d", "doc_id": "5ddcc2a094ad11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "lsju-\u54ee\u5598-\u6c88\u9633(1).pdf", "type": "pdf", "location": "lsju-\u54ee\u5598-\u6c88\u9633(1).pdf", "size": 3913176, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786360775902, "task_type": "dataflow", "root_trace_id": "7d6dcbad8e7b45c1949a5dd052ab4409", "root_traceparent": "00-7d6dcbad8e7b45c1949a5dd052ab4409-9207ab8c386eb81c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
