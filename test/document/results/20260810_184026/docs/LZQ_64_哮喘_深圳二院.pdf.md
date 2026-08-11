# 基准结果：LZQ 64 哮喘 深圳二院.pdf

## 基本信息

- 文件：`LZQ 64 哮喘 深圳二院.pdf`
- 大小：50273.2 KB
- PDF 总页数：20
- doc_id：`370244ae94b011f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T19:39:55  完成时间：2026-08-10T19:47:45  耗时：469.6s
- progress_msg：`11:47:40 Indexing done (0.10s). Task done (440.99s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 41b52c08 | 4 | 1-4 | 门诊病历 科室:呼吸与危重症医学科 门 联系人 性别:女 年龄:62岁 婚姻状况 |
| 2 | e3eda498 | 3 | 5-7 | 门诊病历 科室:呼吸与危重症医学科 姓名: 性别:女 门诊 联系方 年龄:62岁 |
| 3 | adda658e | 3 | 8-10 | 科室:呼吸与危重症医学科 门诊 姓名 联系 性别:女 年龄:63岁 婚姻状况:其 |
| 4 | 473cff89 | 3 | 11-13 | 门诊病历 科室:呼吸与危重症医学科 姓名 性别:女 门诊 联系方式 年龄:63岁 |
| 5 | a57f673e | 1 | 14-14 | 门诊 姓名： 门(急)诊初诊病历 性别：女 科室：呼吸内科门诊 年龄：63岁 就 |
| 6 | 4d6775b5 | 1 | 15-15 | 广东省医疗门诊收费票据（电子） 广东省 财政部监制 票据代码：44060125  |
| 7 | 737dd314 | 1 | 16-16 | 电子发票(普通发票) 发票号码：25447000001429974977 开票日 |
| 8 | 997546d5 | 1 | 17-17 | 门诊号 姓名 科室:呼吸内科门诊 门(急)诊初诊病历 电话 性别:女 年龄:63 |
| 9 | 6ba89570 | 1 | 18-18 | 广东省医疗门诊收费票据（电子） 广东省 财政部监制 票据代码：44 票据号码：9 |
| 10 | 29f855ed | 1 | 19-19 | 10:15 淘 交易成功 医药仁康堂医药专营店> 【信必可】布地奈德福莫特罗[  |
| 11 | dac7bce7 | 1 | 20-20 | 电子发票(普通发票) 发票号码：26322000000914042776 开票日 |

- chunks 总数：11
- 各 chunk 页数合计（含跨页重复）：20
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]`
- 覆盖页数：20 / 20；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 6 | 0 | 6 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 5 | 5 | 5 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 0 | 1 | 0 | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 0 | 0 | 0 | report_time, report_category, report_name | **-** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 6, "MedicationRecord": 5}`
- ChunkMerger：`{"found": true, "merged": 11, "sources": 9, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 6, "Extractor:Medication": 5, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1, "Extractor:Progress": 1}, "filtered_noise": 7}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 11:47:38,398 INFO     29 [ChunkMerger] Merged 11 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 6, 'Extractor:Medication': 5, 'Extractor:Presc`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 11:40:02,050 INFO     29 handle_task begin for task {"id": "38277e3a94b011f1bd9827cf206dfa2d", "doc_id": "370244ae94b011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479740, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362000249, "task_type": "dataflow", "root_trace_id": "96cd8dab6bb7455194a762d3f16e1d52", "root_traceparent": "00-96cd8dab6bb7455194a762d3f16e1d52-1e133766dfd81337-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 11:40:02,267 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 11:40:02,382 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 11:40:02,422 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:40:02,422 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 11:40:02,422 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 11:40:02,432 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 11:40:02,432 INFO     29 ============================================================
2026-08-10 11:40:02,432 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 11:40:02,432 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 11:40:02,432 INFO     29 ============================================================
2026-08-10 11:40:02,432 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 11:40:02,432 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 11:40:02,436 INFO     29 No torch found.
2026-08-10 11:40:04,841 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=20
2026-08-10 11:40:05,002 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1272276, prompt_len=764
2026-08-10 11:40:06,496 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:40:06,496 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 11:40:06,505 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1272276, prompt_len=401
2026-08-10 11:40:11,763 INFO     29 [qwen-vl-parser] text API response (len=870):
["门诊病历", "科室:呼吸与危重症医学科", "门", "联系人", "性别:女", "年龄:62岁", "婚姻状况:其他", "2024-01-10 10:27 初诊记录", "主诉:发作性喘息12年余", "现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年", "余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现", "气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行", "听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并", "规律使用信必可320ug bid后症状缓解。近日活动后气促再发,否认喘", "鸣音。无发热、胸痛。", "既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。", "既往病史:", "1.2022.12.10肝囊肿,持续;", "2.2023.10.31鼻窦炎,持续;", "3.2023.10.31双肺良性小结节,持续;", "4.2023.11.03-2023.12.13,肺肺部感染;", "一年内支气管哮喘急性发作病史:", "12023.11.03-2023.11.08,支气管哮喘急性发作,8mg、4mg甲泼尼龙qd", "各服用3天;", "22023.12.13-2023.12.15,支气管哮喘急性发作,4mg甲泼尼龙片qd,服用", "3天。", "一年内合并用药:", "1.左氧氟沙星片,2023.11.03-2023.12.01,0.5g,qd,po,用于治疗肺部感染", "2.甲泼尼龙片,2023.11.03-2023.11.05,8mg,qd,po,用于治疗支气管哮喘急", "性发作。", "3.甲泼尼龙片,2023.11.06-2023.11.08,4mg,qd,po,用于治疗支气管哮喘急", "性发作。", "4.孟鲁司特钠片,2023.11.03-2023.11.12,10mg,qn,po,用于治疗支气管哮喘", "急性发作。", "第1页"]
2026-08-10 11:40:11,763 INFO     29 [qwen-vl-parser] page=1 text: 35 lines (bbox 0-34)
2026-08-10 11:40:11,763 INFO     29 [qwen-vl-parser] page=1 text: 35 sections
2026-08-10 11:40:11,934 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1361374, prompt_len=764
2026-08-10 11:40:13,383 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:40:13,383 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 11:40:13,391 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1361374, prompt_len=401
2026-08-10 11:40:19,430 INFO     29 [qwen-vl-parser] text API response (len=913):
["门诊病历", "科室:呼吸与危重症医学科", "姓名", "性别:女", "年龄:62岁", "婚姻状况:其他", "联系方式", "2024-01-10 10:27 初诊记录", "5.桉柠蒎肠溶软胶囊,2023.11.03-2023.11.15,0.3g,tid,po,用于治疗肺部感", "染。", "7.甲泼尼龙片,2023.12.13-2023.12.15,4mg,qd,po,用于治疗支气管哮喘急", "性发作。", "8.布地奈德福莫特罗粉吸入剂,2022.11.27开始,持续使用,", "320ug,bid,经口腔吸入,用于控制哮喘。", "过敏史:否认食物、药物过敏史。", "体格检查 收缩压（mmHg）:107;舒张压（mmHg）:75", "其他体格检查:身高:153cm,体重:48.5kg,", "09:50进行生命体征测量:体温:36.4℃,血压:107/75mmHg,呼吸:19", "次/分,脉搏:78次/分;", "查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见", "皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅", "大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。", "耳廓正常无畸形,外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无", "鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿", "大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中", "肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动", "正常,双肺呼吸音粗,未闻及干湿罗音。心律齐。双下肢无水肿。心率", "78次/分,心音正常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛", "反跳痛,无液波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触", "及,肾脏未触及,Murphy征阴性,移动性浊音阴性,肠鸣音正常。外生殖", "器未查、肛门直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无", "异常,其他无异常。", "第2页", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 11:40:19,430 INFO     29 [qwen-vl-parser] page=2 text: 35 lines (bbox 35-69)
2026-08-10 11:40:19,430 INFO     29 [qwen-vl-parser] page=2 text: 35 sections
2026-08-10 11:40:19,627 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1581395, prompt_len=764
2026-08-10 11:40:21,509 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:40:21,509 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 11:40:21,520 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1581395, prompt_len=401
2026-08-10 11:40:22,401 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:40:22.398+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 24, "failed": 0, "current": {"38277e3a94b011f1bd9827cf206dfa2d": {"id": "38277e3a94b011f1bd9827cf206dfa2d", "doc_id": "370244ae94b011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479740, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362000249, "task_type": "dataflow", "root_trace_id": "96cd8dab6bb7455194a762d3f16e1d52", "root_traceparent": "00-96cd8dab6bb7455194a762d3f16e1d52-1e133766dfd81337-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:40:27,119 INFO     29 [qwen-vl-parser] text API response (len=950):
["科室:呼吸与危重症医学科", "姓名:", "性别:女", "门诊", "联系方式", "596", "年龄:62岁", "婚姻状况:其他", "2024-01-10 10:27 初诊记录", "检验检查:阅片见双肺轻度支气管扩张,未见明显急性炎症病灶,余肺基本同前", "(正式报告为准)", "初步诊断:1.鼻窦炎;2.支气管哮喘;", "处理:药品:", "(省采3)硫酸沙丁胺醇吸入气雾剂200揿(100μg/揿)/瓶(1【瓶】) sig:", "(200【揿】)吸入pm(需要时);", "检查:心脏电生理:心电图(十二导联心电图);CT检查:副鼻窦平扫;", "使用螺旋扫描加收;普放:DR胸部正侧位片*(2);呼吸专科检查:支气管", "舒张试验、流速容量曲线;", "检验:凝血四项、肾功能六项+肝功能八项+血脂六项*+电解质六项+空", "腹血糖(门诊使用)+肝酶学补充7项+心肌损伤六项、血常规5分类、尿", "常规加化学分析、感染八项", "治疗:静脉采血", "根据患者病情,认为患者基本符合“评价SHR-1905注射液在重度未", "控制哮喘患者中的有效性及安全性-多中心、随机、双盲、安慰剂对照", "平行设计II期临床研究(SHR-1905-201)”的筛选要求,2024.01.10 09:15", "生向患者__及其家属详细介绍该试验目的、试验设计、受试", "者风险及受益、受试者义务及研究者义务等。根据方案(版本号:2.0,", "版本日期:2022年8月31日)要求,筛选期所有受试者均进行吸入支气", "管扩张剂前后肺功能检查,若受试者无法提供筛选前一年内气道可逆", "性检测报告(吸入沙丁胺醇后FEV1增加≥12%且FEV1绝对值增加≥", "200mL),则筛选期肺功能检查需要满足吸入沙丁胺醇后FEV1增加≥", "12%且FEV1绝对值增加≥200mL。符合要求后才可以入组,受试者表", "示同意。患者.__及其家属表示已充分了解以上告知内容,同意参加", "该临床试验,", "医生与患者__于2024.01.10 09:47同时签署了知", "情同意书(版本号:2.0,版本日期:2022年08月31日),一式两份,一份", "第3页"]
2026-08-10 11:40:27,120 INFO     29 [qwen-vl-parser] page=3 text: 37 lines (bbox 70-106)
2026-08-10 11:40:27,121 INFO     29 [qwen-vl-parser] page=3 text: 37 sections
2026-08-10 11:40:27,251 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=880816, prompt_len=764
2026-08-10 11:40:28,626 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:40:28,626 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-10 11:40:28,646 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=880816, prompt_len=401
2026-08-10 11:40:32,882 INFO     29 [qwen-vl-parser] text API response (len=536):
["门诊病历", "科室:呼吸与危重症医学科", "姓名:", "性别:女", "门诊", "联系方式", "年龄:62岁", "婚姻状况:其他", "2024-01-10 10:27 初诊记录", "交给患者保存,一份保存在研究中心。签署知情同意书后患者进入筛选", "流程,受试者筛选号为CN..", "新增AE:", "1.高尿酸血症,2024.01.10开始,轻度,持续,与研究药物肯定无关,对研", "究药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。", "2.高脂血症,2024.01.10开始,轻度,持续,与研究药物肯定无关,对研究", "药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。", "3.白细胞计数降低,2024.01.10开始,轻度,持续,与研究药物肯定无关", "对研究药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。此项", "指标与患者临床症状不符,考虑让其一周内复测。", "规律使用吸入药物,用后漱口,定期复诊;避免接触可能过敏原;不用地", "毯,不养动物", "医师签", "门诊病历专用", "※提醒:复诊时,请携带本病历记录,谢谢!※", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 11:40:32,883 INFO     29 [qwen-vl-parser] page=4 text: 26 lines (bbox 107-132)
2026-08-10 11:40:32,883 INFO     29 [qwen-vl-parser] page=4 text: 26 sections
2026-08-10 11:40:33,042 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1312119, prompt_len=764
2026-08-10 11:40:34,426 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:40:34,427 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 11:40:34,446 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1312119, prompt_len=401
2026-08-10 11:40:39,755 INFO     29 [qwen-vl-parser] text API response (len=881):
["门诊病历", "科室:呼吸与危重症医学科", "姓名:", "性别:女", "门诊", "联系方", "年龄:62岁", "婚姻状况:其他", "2024-03-21 08:40 初诊记录", "主诉:SHR-1905-201 试验复筛", "现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年", "余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现", "气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行", "听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并", "规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可", "320ug bid,近日活动后气促再发,否认喘鸣音。无发热、胸痛。", "2024.01.10参加SHR-1905-201临床试验,因白细胞计数<3.0*10^9/L符", "合排除标准第12条筛败,于2024.03.01血液科就诊,无特殊处理,", "2024.03.06进行SHR-1905-201试验二次知情。受试者今日返院完成V3", "访视。", "既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。", "既往病史:", "1.2022.12.10肝囊肿,持续;", "2.2023.10.31鼻窦炎,持续;", "3.2023.10.31双肺良性小结节,持续;", "4.2023.11.03-2023.12.13,肺肺部感染;", "5.2024.03.01开始,白细胞数降低1级;", "6.2024.01.10开始,高脂蛋白a血症,", "过敏史:否认食物、药物过敏史。", "体格检查收缩压(mmHg):113;舒张压(mmHg):76", "其他体格检查:09:37进行生命体征测量:体温:36.5℃,血压:", "113/76mmHg,呼吸:18次/分,脉搏:98次/分;", "查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见", "第1页"]
2026-08-10 11:40:39,756 INFO     29 [qwen-vl-parser] page=5 text: 34 lines (bbox 133-166)
2026-08-10 11:40:39,756 INFO     29 [qwen-vl-parser] page=5 text: 34 sections
2026-08-10 11:40:39,943 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1571361, prompt_len=764
2026-08-10 11:40:41,394 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:40:41,395 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-10 11:40:41,406 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1571361, prompt_len=401
2026-08-10 11:40:46,938 INFO     29 [qwen-vl-parser] text API response (len=850):
["科室:呼吸与危重症医学科", "姓名", "性别:女", "门诊", "联系方", "年龄:62岁", "婚姻状况:其他", "2024-03-21 08:40 初诊记录", "皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅", "大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。", "耳廓正常无畸形,外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无", "鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿", "大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中", "肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动", "正常,双肺呼吸音粗,未闻及干湿罗音。心律齐。双下肢无水肿。心音正", "常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛、反跳痛,无液", "波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触及,肾脏未触", "及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖器未查、肛门", "直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无异常,其他无", "异常。.", "检验检查:无", "初步诊断:支气管哮喘", "处理:", "CM 跟踪:", "1、布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,", "320ug,bid,经口腔吸入,用于控制哮喘。", "处理:", "1、2024.03.14-2024.03.21 家用峰流速仪使用 ePRO 系统填写依从性", "7/7*100%=100%,嘱托患者按照自己实际情况及时填写日志,如有问题", "随时沟通。", "2、无新增 AE,CM,无临床试验安全性事件。", "3、今日回收硫酸沙丁胺醇吸入气雾剂,发放新的硫酸沙丁胺醇吸入气", "雾剂1盒,并嘱托受试者正确保存和使用。", "4、绝经期女性,未做血、尿妊娠检查。", "第2页", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 11:40:46,938 INFO     29 [qwen-vl-parser] page=6 text: 37 lines (bbox 167-203)
2026-08-10 11:40:46,938 INFO     29 [qwen-vl-parser] page=6 text: 37 sections
2026-08-10 11:40:47,039 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=524906, prompt_len=764
2026-08-10 11:40:48,314 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:40:48,314 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-10 11:40:48,334 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=524906, prompt_len=401
2026-08-10 11:40:50,181 INFO     29 [qwen-vl-parser] text API response (len=301):
["科室:呼吸与危重症医学科", "门诊", "姓名", "联系方式", "性别:女", "年龄:62岁", "婚姻状况:其他", "2024-03-21 08:40 初诊记录", "5、受试者所有检查结果经再次核对入排,符合所有入选标准,不符合任", "一排除标准,可随机入组,分配随机号:_,随机分层信息:中剂量", "ICS,嗜酸性粒细胞计数<300/ul,未联合使用LAMA。", "6、嘱托受试者2024.03.22来院行V4随访。", "医师签", "门诊病历专用章", "※提醒:复诊时,请携带本病历记录,谢谢!※", "第3页", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 11:40:50,181 INFO     29 [qwen-vl-parser] page=7 text: 18 lines (bbox 204-221)
2026-08-10 11:40:50,181 INFO     29 [qwen-vl-parser] page=7 text: 18 sections
2026-08-10 11:40:50,345 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1355651, prompt_len=764
2026-08-10 11:40:51,680 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:40:51,680 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=None
2026-08-10 11:40:51,691 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1355651, prompt_len=401
2026-08-10 11:40:54,178 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:40:54.177+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 24, "failed": 0, "current": {"38277e3a94b011f1bd9827cf206dfa2d": {"id": "38277e3a94b011f1bd9827cf206dfa2d", "doc_id": "370244ae94b011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479740, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362000249, "task_type": "dataflow", "root_trace_id": "96cd8dab6bb7455194a762d3f16e1d52", "root_traceparent": "00-96cd8dab6bb7455194a762d3f16e1d52-1e133766dfd81337-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:40:56,514 INFO     29 [qwen-vl-parser] text API response (len=837):
["科室:呼吸与危重症医学科", "门诊", "姓名", "联系", "性别:女", "年龄:63岁", "婚姻状况:其他", "2024-12-12 09:40 初诊记录", "主诉:SHR-1905-201 临床试验 V14", "现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年", "余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现", "气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行", "听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并", "规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可", "320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:", "近日咳嗽咳痰,低烧两天,呼吸道感染。2024.12.02行V14随访", "因患者发热延迟用药。今日回院用药,留院观察1h。", "既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。", "既往病史:", "1.2022.12.10肝囊肿,持续;", "2.2023.10.31鼻窦炎,持续;", "3.2023.10.31双肺良性小结节,持续;", "4.2023.11.03-2023.12.13,肺肺部感染;", "5.2024.03.01开始,白细胞数降低1级,持续;", "6.2024.01.10开始,高脂血症,持续;", "7.十余年前,慢性浅表胃炎,持续中。", "过敏史:否认食物、药物过敏史。", "体格检查收缩压(mmHg):-;舒张压(mmHg):-", "其他体格检查:未行", "检验检查:无", "初步诊断:支气管哮喘", "处理:检查:心脏电生理:心电图(十二导联心电图);", "检验:急诊血常规(五分类)+急诊超敏C反应蛋白、急诊肝功能五项", "治疗:静脉采血", "第1页"]
2026-08-10 11:40:56,515 INFO     29 [qwen-vl-parser] page=8 text: 35 lines (bbox 222-256)
2026-08-10 11:40:56,515 INFO     29 [qwen-vl-parser] page=8 text: 35 sections
2026-08-10 11:40:56,660 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1105548, prompt_len=764
2026-08-10 11:40:57,955 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:40:57,955 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-10 11:40:57,975 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1105548, prompt_len=401
2026-08-10 11:41:02,778 INFO     29 [qwen-vl-parser] text API response (len=803):
["科室:呼吸与危重症医学科", "性别:女", "年龄:63岁", "婚姻状况:其他", "2024-12-12 09:40 初诊记录", "无新增 AE,无新增 CM,无临床试验安全性事件。", "呼吸道感染,2024.11.27-2024.12.11,中度,与试验药物关系为可能无关", "对试验药物采取的措施为延迟用药,对 AE 采取的措施为药物治疗,肺", "SAE,非 SIE,不因此退出临床试验。", "跟踪 CM:", "1.盐酸莫西沙片,2024.12.02-2024.12.11,持续中,0.4g/片,1片/次,", "qd,po,用于治疗 AE 呼吸道感染。", "2.桉柠蒎肠溶胶囊,2024.12.02-2024.12.11 持续中,0.3g/粒,1粒/次,", "tid,po,用于治疗 AE 呼吸道感染。(化痰)", "3.氯苯那敏片,2024.12.02-2024.12.11,持续中,4mg/片,1片/次,", "qn,po,用于治疗 AE 呼吸道感染。", "4.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po,用于治", "疗病史慢性浅表胃炎。", "5.复方氨酚烷胺胶囊,2024.11.27-2024.12.02,持续中,0.25g:0.1g,1粒", "/次,bid,po,用于治疗 AE 呼吸道感染。", "6.吸入沙丁胺醇气雾剂,2024.12.02-2024.12.02,400ug,吸入,once,用于支", "气管扩张检查。", "CM 跟踪:", "1、布地奈德福莫特罗粉吸入剂,2022.11.27 开始,持续使用,", "320ug,bid,经口腔吸入,用于控制哮喘。", "2、硫酸沙丁胺醇气雾剂,2024.03.06 开始,持续中,100ug,pm,经口腔吸", "入,控制哮喘急性发作。", "第2页"]
2026-08-10 11:41:02,779 INFO     29 [qwen-vl-parser] page=9 text: 28 lines (bbox 257-284)
2026-08-10 11:41:02,779 INFO     29 [qwen-vl-parser] page=9 text: 28 sections
2026-08-10 11:41:02,870 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=484906, prompt_len=764
2026-08-10 11:41:04,148 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:41:04,149 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=None
2026-08-10 11:41:04,172 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=484906, prompt_len=401
2026-08-10 11:41:05,739 INFO     29 [qwen-vl-parser] text API response (len=258):
["门诊病历", "科室:呼吸与危重症医学科", "姓名:", "性别:女", "门诊号", "联系方式", "年龄:63岁", "婚姻状况:其他", "2024-12-12 09:40 初诊记录", "处理:", "患者于今日 12:21-12:28 完成临床试验药物的注射,药物编号为", "Y6077Y4950 用药前完善必要检查后随机用药。", "医师", "门诊病历", "※提醒:复诊时,请携带本病历记录,谢谢!※", "“若有高血压糖尿病诊断,建议您到居住地附近社康中心,建立居民健康档案”", ""]
2026-08-10 11:41:05,740 INFO     29 [qwen-vl-parser] page=10 text: 16 lines (bbox 285-300)
2026-08-10 11:41:05,740 INFO     29 [qwen-vl-parser] page=10 text: 16 sections
2026-08-10 11:41:05,946 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1693459, prompt_len=764
2026-08-10 11:41:07,372 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:41:07,373 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=None
2026-08-10 11:41:07,388 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1693459, prompt_len=401
2026-08-10 11:41:12,990 INFO     29 [qwen-vl-parser] text API response (len=939):
["门诊病历", "科室:呼吸与危重症医学科", "姓名", "性别:女", "门诊", "联系方式", "年龄:63岁", "婚姻状况:其他", "2025-07-31 17:13 初诊记录", "主诉:SHR-1905V19随访", "现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年", "余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现", "气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行", "听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并", "规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可", "320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:", "20036.。近日无咳嗽咳痰,无胸闷气喘,无发热,无支气管哮喘急性发作", "今日回院行V19随访。", "既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。", "既往病史:", "1.2022.12.10肝囊肿,持续;", "2.2023.10.31鼻窦炎,持续;", "3.2023.10.31双肺良性小结节,持续;", "4.2023.11.03-2023.12.13,肺肺部感染;", "5.2024.03.01开始,白细胞数降低1级,持续;", "6.2024.01.10高脂血症,持续中", "过敏史:否认食物、药物过敏史。", "体格检查收缩压(mmHg):103;舒张压(mmHg):64", "其他体格检查:进行生命体征测量:体温:36.4℃,血压:", "103/64mmHg,呼吸:18次/分,脉搏:76次/分;", "查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见", "皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅", "大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。", "耳廓正常无畸形外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无", "鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿", "第1页"]
2026-08-10 11:41:12,991 INFO     29 [qwen-vl-parser] page=11 text: 36 lines (bbox 301-336)
2026-08-10 11:41:12,991 INFO     29 [qwen-vl-parser] page=11 text: 36 sections
2026-08-10 11:41:13,175 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1486615, prompt_len=764
2026-08-10 11:41:14,633 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:41:14,634 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=None
2026-08-10 11:41:14,646 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1486615, prompt_len=401
2026-08-10 11:41:20,677 INFO     29 [qwen-vl-parser] text API response (len=848):
["门诊病历", "科室:呼吸与危重症医学科", "性别:女", "门诊", "联系方式:", "年龄:63岁", "婚姻状况:其他", "2025-07-31 17:13 初诊记录", "大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中", "肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动", "正常,左肺呼吸音清,未闻及粗干啰音。心律齐。双下肢无水肿。心音正", "常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛、反跳痛,无液", "波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触及,肾脏未触", "及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖器未查、肛门", "直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无异常,其他无", "异常。", "检验检查:已完善试验相关检验检查", "初步诊断:支气管哮喘", "处理:尿常规检查尿隐血,建议定期检查,必要时肾内科就诊。", "无临床试验安全性事,无新增 AE。", "新增合并用药:硫酸沙丁胺醇吸入气雾剂,2025.07.31-", "2025.078.31,400ug,once,吸入,用于支气管扩张检查。", "CM 跟踪:", "1、布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,", "320ug,bid,经口腔吸入,用于控制哮喘。", "2、硫酸沙丁胺醇气雾剂,2024.03.06开始,持续中,100ug,pm,经口腔吸", "入,控制哮喘急性发作。", "3.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po.用于治", "疗病史慢性浅表胃炎。", "处理:", "12025.05.13-2025.07.31 家用峰流速仪使用 ePRO 系统填写依从性大于", "80%,今日已解绑 ePRO 系统。", "2遵从临床试验方案完成 IgE,PK,ADA 采血,完成 ACQ-6,AQLQ 问卷填", "写。"]
2026-08-10 11:41:20,678 INFO     29 [qwen-vl-parser] page=12 text: 34 lines (bbox 337-370)
2026-08-10 11:41:20,678 INFO     29 [qwen-vl-parser] page=12 text: 34 sections
2026-08-10 11:41:20,806 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=785150, prompt_len=764
2026-08-10 11:41:22,092 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:41:22,093 INFO     29 [qwen-vl-parser] page=13 classify=text report_date=None
2026-08-10 11:41:22,109 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=785150, prompt_len=401
2026-08-10 11:41:24,169 INFO     29 [qwen-vl-parser] text API response (len=341):
["门诊病历", "科室:呼吸与危重症医学科", "姓名", "性别:女", "门诊", "联系", "年龄:63岁", "婚姻状况:其他", "2025-07-31 17:13 初诊记录", "3.患者于今日肺功能检查前已停用基础吸入药物布地奈德福莫特罗粉", "吸入剂大于12h,停药时间2025.07.30上午,具体时间不详。", "4.患者已于今日完成随访期随访。", "5.因患者未找到发放万托林,可能已经丢失故不予回收。", "6.嘱患者规律使用吸入药物布地奈德福莫特罗粉吸入剂,药物自备。", "医师", "门诊病历专用章", "※提醒:复诊时,请携带本病历记录,谢谢!※", "“若有高血压糖尿病诊断,建议您到居住地附近社康中心,建立居民健康档案”", "第3页"]
2026-08-10 11:41:24,170 INFO     29 [qwen-vl-parser] page=13 text: 19 lines (bbox 371-389)
2026-08-10 11:41:24,170 INFO     29 [qwen-vl-parser] page=13 text: 19 sections
2026-08-10 11:41:24,448 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2492696, prompt_len=764
2026-08-10 11:41:25,322 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:41:25.320+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 24, "failed": 0, "current": {"38277e3a94b011f1bd9827cf206dfa2d": {"id": "38277e3a94b011f1bd9827cf206dfa2d", "doc_id": "370244ae94b011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479740, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362000249, "task_type": "dataflow", "root_trace_id": "96cd8dab6bb7455194a762d3f16e1d52", "root_traceparent": "00-96cd8dab6bb7455194a762d3f16e1d52-1e133766dfd81337-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:41:25,816 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:41:25,818 INFO     29 [qwen-vl-parser] page=14 classify=text report_date=None
2026-08-10 11:41:25,836 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2492696, prompt_len=401
2026-08-10 11:41:31,248 INFO     29 [qwen-vl-parser] text API response (len=895):
["门诊", "姓名：", "门(急)诊初诊病历", "性别：女", "科室：呼吸内科门诊", "年龄：63岁", "就诊日期：2025-10-25 15:22", "主诉：支气管哮喘复诊", "现病史：患者支气管哮喘复诊，目前规律吸入布地奈德福莫特罗320ug 一次1吸，", "一天2次。目前诉有咳嗽、咳痰，有气促感，无胸闷，无发热，无鼻塞、流涕，无咯", "血、痰中带血，无头痛、头晕、视物旋转，无饮水呛咳，无咽痛、腹痛、腹胀等不", "适。未予处理及就医。现患者为求进一步诊治，故至我院科门诊就医。", "既往史：否认高血压、否认糖尿病、否认冠心病等慢性疾病病史，否认肝炎、结核", "等传染病史，否认手术外伤输血史 过敏史：无食物、药物过敏史。。否认饮酒史。", "个人史：已婚已育", "家族史：否认家族病史。", "体格检查：T：36.8℃ P：87次/分 R：21次/分 BP：108/73mmHg 指脉氧：", "9%。神志清楚，精神尚可，呼吸平顺，口唇无发绀，咽部无充血，扁桃体无肿大，", "双侧颈静脉无怒张，双肺呼吸音粗，双肺可闻及干啰音，双肺未闻及湿性啰音及胸膜", "摩擦音。心率87次/分，律齐，各瓣膜未闻及明显病理性杂音。腹部平软，全腹部无", "玉痛，反跳痛，肠鸣音正常。四肢运动自如，双下肢无水肿。", "辅助检查：患者自行购买布地奈德福莫特罗320ug 一次1吸，一天2次。", "初步诊断：", "西医诊断：1.支气管哮喘(急性发作期)", "处理意见：", "醋酸泼尼松片（国基）(5mg*100片) 20.000mg", "1次/天 口服", "12.00片", "硫酸沙丁胺醇吸入气雾剂（省3、国基）(200揿：", "100μg) 200.000μg", "1次/天 吸入", "1.00瓶", "建议：建议患者结果回报后请及时至我科门诊复诊，若出现病情变化或病情加重", "无好转等，请及时至急诊科门诊复诊。", "温馨提示：1.请妥善保管好病历及各种检查检验报告单。", "2.复诊时，请携带本病历记录，谢谢！", "第1页(共1页)"]
2026-08-10 11:41:31,249 INFO     29 [qwen-vl-parser] page=14 text: 37 lines (bbox 390-426)
2026-08-10 11:41:31,249 INFO     29 [qwen-vl-parser] page=14 text: 37 sections
2026-08-10 11:41:31,369 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=899102, prompt_len=764
2026-08-10 11:41:32,696 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:41:32,697 INFO     29 [qwen-vl-parser] page=15 classify=text report_date=None
2026-08-10 11:41:32,709 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=899102, prompt_len=401
2026-08-10 11:41:36,634 INFO     29 [qwen-vl-parser] text API response (len=836):
["广东省医疗门诊收费票据（电子）", "广东省", "财政部监制", "票据代码：44060125", "票据号码：9148002082", "校验码： 831306", "开票日期：2025-10-25", "项目名称", "数量/单位", "金额（元）", "备注", "项目名称", "数量/单位", "金额（元）", "备注", "西药费", "1", "13.05", "", "", "", "", "", "以下是清单项", "", "", "", "", "", "", "", "醋酸泼尼松片（国基）", "12", "0.50", "", "硫酸沙丁胺醇吸入气雾剂（省3", "1", "12.55", "", "、国基）", "", "", "", "", "", "", "", "金额合计（大写）壹拾叁元零伍分", "(小写)13.05", "", "", "业务流水号：SF10390911", "门诊", "", "", "就诊日期：20251025", "其他信息", "医疗机构类型：综合医院", "医保类型：现金(自费)", "医保编号：", "性别：女", "医保统筹基金支付：0.00", "其他支付：0.00", "个人账户支付：0.00", "个人现金支付：13.05", "个人自付：0.00", "个人自费：13.05", "", "", "政策性减免：", "", "", "收款单位（章）深圳市龙岗区第人民医院", "复核人：掌上医院", "收款人：掌上医院", "说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。", "单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dzpj.czt.gd.gov.cn/billcheck查验本省财政电子票据。", "CS 扫描全能王", "3 亿人都在用的扫描 App"]
2026-08-10 11:41:36,635 INFO     29 [qwen-vl-parser] page=15 text: 50 lines (bbox 427-476)
2026-08-10 11:41:36,635 INFO     29 [qwen-vl-parser] page=15 text: 50 sections
2026-08-10 11:41:36,759 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=750717, prompt_len=764
2026-08-10 11:41:38,146 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:41:38,146 INFO     29 [qwen-vl-parser] page=16 classify=text report_date=None
2026-08-10 11:41:38,165 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=750717, prompt_len=401
2026-08-10 11:41:40,580 INFO     29 [qwen-vl-parser] text API response (len=419):
["电子发票(普通发票)", "发票号码：25447000001429974977", "开票日期：2025年11月05日", "广东省税务局", "购买方信息", "名称：", "统一社会信用代码/纳税人识别号：", "销售方信息", "名称：阿里健康大药房医药连锁有限公司", "统一社会信用代码/纳税人识别号：91440101681325547Y", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*化学药品制剂*布地奈德", "盒", "3", "176.70", "530.09", "13%", "68.91", "福莫特罗吸入粉雾剂", "合计", "￥530.09", "￥68.91", "价税合计（大写）", "伍佰玖拾玖圆整", "(小写)￥599.00", "备注", "开票人：董茜玲", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 11:41:40,581 INFO     29 [qwen-vl-parser] page=16 text: 36 lines (bbox 477-512)
2026-08-10 11:41:40,581 INFO     29 [qwen-vl-parser] page=16 text: 36 sections
2026-08-10 11:41:40,767 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1499579, prompt_len=764
2026-08-10 11:41:42,206 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:41:42,207 INFO     29 [qwen-vl-parser] page=17 classify=text report_date=None
2026-08-10 11:41:42,224 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1499579, prompt_len=401
2026-08-10 11:41:47,717 INFO     29 [qwen-vl-parser] text API response (len=851):
["门诊号", "姓名", "科室:呼吸内科门诊", "门(急)诊初诊病历", "电话", "性别:女", "年龄:63岁", "就诊日期:2025-11-24 15:01", "主诉:支气管哮喘复诊", "现病史:患者支气管哮喘复诊,目前规律吸入布地奈德福莫特罗320一次1吸,一天2次(患者自行网购药物),目前有咳嗽、咳痰,咳嗽时有气喘感。无胸闷,无发热,无鼻塞、流涕,无咯血、痰中带血,无头痛、头晕、视物旋转,无饮水呛咳,无咽痛、腹痛、腹胀等不适。未予处理及就医。现患者为求进一步诊治,故至我院科门诊就医。", "既往史:否认高血压、否认糖尿病、否认冠心病等慢性疾病病史,否认肝炎、结核等传染病史,否认手术外伤输血史过敏史:无食物、药物过敏史。。否认饮酒史。", "个人史:已婚已育", "家族史:否认家族病史。", "体格检查:T:36.8℃ P:87次/分 R:21次/分 BP:108/73mmHg 指脉氧:", "9%。神志清楚,精神尚可,呼吸平顺,口唇无发绀,咽部无充血,扁桃体无肿大,", "双侧颈静脉无怒张,双肺呼吸音粗,双肺可闻及散在干啰音,双肺未闻及湿性啰音及", "胸膜摩擦音。心率87次/分,律齐,各瓣膜未闻及明显病理性杂音。腹部平软,全腹", "邻无压痛,反跳痛,肠鸣音正常。四肢运动自如,双下肢无水肿。", "辅助检查:", "初步诊断:", "西医诊断:1.支气管哮喘(急性发作期)", "处理意见:自备布地奈德福莫特罗320一次1吸,一天2次", "醋酸泼尼松片(国基)(5mg*100片)10.000mg", "1次/天 口服 6.00片", "建议:建议患者结果回报后请及时至我科门诊复诊,若出现病情变化或病情加重", "无好转等,请及时至急诊科门诊复诊。", "医生签名:", "温馨提示:1.请妥善保管好病历及各种检查检验报告单。", "2.复诊时,请携带本病历记录,谢谢!", "第1页(共1页)", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 11:41:47,718 INFO     29 [qwen-vl-parser] page=17 text: 32 lines (bbox 513-544)
2026-08-10 11:41:47,718 INFO     29 [qwen-vl-parser] page=17 text: 32 sections
2026-08-10 11:41:47,840 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=811880, prompt_len=764
2026-08-10 11:41:49,145 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:41:49,145 INFO     29 [qwen-vl-parser] page=18 classify=text report_date=None
2026-08-10 11:41:49,155 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=811880, prompt_len=401
2026-08-10 11:41:52,551 INFO     29 [qwen-vl-parser] text API response (len=664):
["广东省医疗门诊收费票据（电子）", "广东省", "财政部监制", "票据代码：44", "票据号码：9148286284", "校验码：89a81f", "交款人", "开票日期：2025-11-24", "项目名称", "数量/单位", "金额（元）", "备注", "项目名称", "数量/单位", "金额（元）", "备注", "西药费", "1", "0.25", "以下是清单项", "醋酸泼尼松片（国基）", "6", "0.25", "金额合计（大写）贰角伍分", "(小写)0.25", "业务流水号：SF10481981", "门", "就诊日期：20251124", "其他信息", "医疗机构类型：综合医院", "医保类型：现金(自费)", "医保编号：", "性别：女", "医保统筹基金支付：0.00", "其他支付：0.00", "个人账户支付：0.00", "个人现金支付：0.25", "个人自付：0.00", "个人自费：0.25", "政策性减免：", "收款单位（章）", "人民医院", "复核人：吴亮梅", "收款人：吴亮梅", "说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。", "单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dipj.czt.gd.gov.cn/billcheck查验本省财政电子票据。", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 11:41:52,551 INFO     29 [qwen-vl-parser] page=18 text: 48 lines (bbox 545-592)
2026-08-10 11:41:52,552 INFO     29 [qwen-vl-parser] page=18 text: 48 sections
2026-08-10 11:41:52,660 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=729091, prompt_len=764
2026-08-10 11:41:53,927 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:41:53,928 INFO     29 [qwen-vl-parser] page=19 classify=text report_date=None
2026-08-10 11:41:53,939 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=729091, prompt_len=401
2026-08-10 11:41:55,826 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:41:55.825+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 24, "failed": 0, "current": {"38277e3a94b011f1bd9827cf206dfa2d": {"id": "38277e3a94b011f1bd9827cf206dfa2d", "doc_id": "370244ae94b011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479740, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362000249, "task_type": "dataflow", "root_trace_id": "96cd8dab6bb7455194a762d3f16e1d52", "root_traceparent": "00-96cd8dab6bb7455194a762d3f16e1d52-1e133766dfd81337-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:41:57,144 INFO     29 [qwen-vl-parser] text API response (len=564):
["10:15", "淘", "交易成功", "医药仁康堂医药专营店>", "【信必可】布地奈德福莫特罗[", "¥213", "放心买药", "正品保障", "1盒装", "不支持7天无理由 假一赔四>", "x1", "专业药师在线服务", "上天猫放心买药", "用药小贴士 1.哮喘。2.慢性阻塞性肺疾病(慢阻肺;...", "申请售后", "商品总价", "¥213", "运费(含服务费)", "¥8", "应付款", "¥221^", "订单信息 2026-01-20", "收起^", "订单编号", "4501919772001020746", "交易快照", "发生交易争议时，可作为判断依据>", "成交时间", "2026-01-26 22:25:02", "发货时间", "2026-01-21 12:24:52", "付款时间", "2026-01-20 19:25:06", "创建时间", "2026-01-20 19:24:30", "支付宝交易号", "2026012022001134951454085519", "天猫积分", "获得106点积分>", "客服", "更多", "查看处方", "查看物流", "评价", "扫描全能王", "扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 11:41:57,145 INFO     29 [qwen-vl-parser] page=19 text: 47 lines (bbox 593-639)
2026-08-10 11:41:57,148 INFO     29 [qwen-vl-parser] page=19 text: 47 sections
2026-08-10 11:41:57,282 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=799608, prompt_len=764
2026-08-10 11:41:58,717 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:41:58,718 INFO     29 [qwen-vl-parser] page=20 classify=text report_date=None
2026-08-10 11:41:58,737 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=799608, prompt_len=401
2026-08-10 11:42:01,099 INFO     29 [qwen-vl-parser] text API response (len=412):
["电子发票(普通发票)", "发票号码：26322000000914042776", "开票日期：2026年02月02日", "江苏省税务局", "购买方信息", "名称：", "统一社会信用代码/纳税人识别号：", "销售方信息", "名称：阜宁仁康堂大药房有限公司", "统一社会信用代码/纳税人识别号：91320923MAK1XP619R", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*生物化学药品*其他生物", "1", "218.811881188119", "218.81", "1%", "2.19", "化学药品", "合计", "￥218.81", "￥2.19", "价税合计（大写）", "贰佰贰拾壹圆整", "(小写)￥221.00", "备注", "开票人：杨雪", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 11:42:01,099 INFO     29 [qwen-vl-parser] page=20 text: 35 lines (bbox 640-674)
2026-08-10 11:42:01,100 INFO     29 [qwen-vl-parser] page=20 text: 35 sections
2026-08-10 11:42:01,100 INFO     29 [qwen-vl-parser] parse_pdf done: 675 sections from 20 pages.
2026-08-10 11:42:01,114 INFO     29 Close text detector.
2026-08-10 11:42:01,596 INFO     29 Close text recognizer.
2026-08-10 11:42:01,998 INFO     29 Close recognizer.
2026-08-10 11:42:02,406 INFO     29 Close recognizer.
2026-08-10 11:42:02,907 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 11:42:02,908 INFO     29 [Trace] task=38277e3a | doc=LZQ 64 哮喘 深圳二院.pdf | Parser:MedLink | outputs={"html": "", "json": "675 items", "markdown": "", "text": "", "name": "LZQ 64 哮喘 深圳二院.pdf", "output_format": "json"}
2026-08-10 11:42:02,908 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 11:42:02,944 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:42:02,944 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 门诊病历\n[BBOX-1] 科室:呼吸与危重症医学科\n[BBOX-2] 门\n[BBOX-3] 联系人\n[BBOX-4] 性别:女\n[BBOX-5] 年龄:62岁\n[BBOX-6] 婚姻状况:其他\n[BBOX-7] 2024-01-10 10:27 初诊记录\n[BBOX-8] 主诉:发作性喘息12年余\n[BBOX-9] 现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年\n[BBOX-10] 余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现\n[BBOX-11] 气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行\n[BBOX-12] 听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并\n[BBOX-13] 规律使用信必可320ug bid后症状缓解。近日活动后气促再发,否认喘\n[BBOX-14] 鸣音。无发热、胸痛。\n[BBOX-15] 既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。\n[BBOX-16] 既往病史:\n[BBOX-17] 1.2022.12.10肝囊肿,持续;\n[BBOX-18] 2.2023.10.31鼻窦炎,持续;\n[BBOX-19] 3.2023.10.31双肺良性小结节,持续;\n[BBOX-20] 4.2023.11.03-2023.12.13,肺肺部感染;\n[BBOX-21] 一年内支气管哮喘急性发作病史:\n[BBOX-22] 12023.11.03-2023.11.08,支气管哮喘急性发作,8mg、4mg甲泼尼龙qd\n[BBOX-23] 各服用3天;\n[BBOX-24] 22023.12.13-2023.12.15,支气管哮喘急性发作,4mg甲泼尼龙片qd,服用\n[BBOX-25] 3天。\n[BBOX-26] 一年内合并用药:\n[BBOX-27] 1.左氧氟沙星片,2023.11.03-2023.12.01,0.5g,qd,po,用于治疗肺部感染\n[BBOX-28] 2.甲泼尼龙片,2023.11.03-2023.11.05,8mg,qd,po,用于治疗支气管哮喘急\n[BBOX-29] 性发作。\n[BBOX-30] 3.甲泼尼龙片,2023.11.06-2023.11.08,4mg,qd,po,用于治疗支气管哮喘急\n[BBOX-31] 性发作。\n[BBOX-32] 4.孟鲁司特钠片,2023.11.03-2023.11.12,10mg,qn,po,用于治疗支气管哮喘\n[BBOX-33] 急性发作。\n[BBOX-34] 第1页\n[BBOX-35] 门诊病历\n[BBOX-36] 科室:呼吸与危重症医学科\n[BBOX-37] 姓名\n[BBOX-38] 性别:女\n[BBOX-39] 年龄:62岁\n[BBOX-40] 婚姻状况:其他\n[BBOX-41] 联系方式\n[BBOX-42] 2024-01-10 10:27 初诊记录\n[BBOX-43] 5.桉柠蒎肠溶软胶囊,2023.11.03-2023.11.15,0.3g,tid,po,用于治疗肺部感\n[BBOX-44] 染。\n[BBOX-45] 7.甲泼尼龙片,2023.12.13-2023.12.15,4mg,qd,po,用于治疗支气管哮喘急\n[BBOX-46] 性发作。\n[BBOX-47] 8.布地奈德福莫特罗粉吸入剂,2022.11.27开始,持续使用,\n[BBOX-48] 320ug,bid,经口腔吸入,用于控制哮喘。\n[BBOX-49] 过敏史:否认食物、药物过敏史。\n[BBOX-50] 体格检查 收缩压（mmHg）:107;舒张压（mmHg）:75\n[BBOX-51] 其他体格检查:身高:153cm,体重:48.5kg,\n[BBOX-52] 09:50进行生命体征测量:体温:36.4℃,血压:107/75mmHg,呼吸:19\n[BBOX-53] 次/分,脉搏:78次/分;\n[BBOX-54] 查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见\n[BBOX-55] 皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅\n[BBOX-56] 大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。\n[BBOX-57] 耳廓正常无畸形,外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无\n[BBOX-58] 鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿\n[BBOX-59] 大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中\n[BBOX-60] 肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动\n[BBOX-61] 正常,双肺呼吸音粗,未闻及干湿罗音。心律齐。双下肢无水肿。心率\n[BBOX-62] 78次/分,心音正常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛\n[BBOX-63] 反跳痛,无液波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触\n[BBOX-64] 及,肾脏未触及,Murphy征阴性,移动性浊音阴性,肠鸣音正常。外生殖\n[BBOX-65] 器未查、肛门直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无\n[BBOX-66] 异常,其他无异常。\n[BBOX-67] 第2页\n[BBOX-68] CS 扫描全能王\n[BBOX-69] 3亿人都在用的扫描App\n[BBOX-70] 科室:呼吸与危重症医学科\n[BBOX-71] 姓名:\n[BBOX-72] 性别:女\n[BBOX-73] 门诊\n[BBOX-74] 联系方式\n[BBOX-75] 596\n[BBOX-76] 年龄:62岁\n[BBOX-77] 婚姻状况:其他\n[BBOX-78] 2024-01-10 10:27 初诊记录\n[BBOX-79] 检验检查:阅片见双肺轻度支气管扩张,未见明显急性炎症病灶,余肺基本同前\n[BBOX-80] (正式报告为准)\n[BBOX-81] 初步诊断:1.鼻窦炎;2.支气管哮喘;\n[BBOX-82] 处理:药品:\n[BBOX-83] (省采3)硫酸沙丁胺醇吸入气雾剂200揿(100μg/揿)/瓶(1【瓶】) sig:\n[BBOX-84] (200【揿】)吸入pm(需要时);\n[BBOX-85] 检查:心脏电生理:心电图(十二导联心电图);CT检查:副鼻窦平扫;\n[BBOX-86] 使用螺旋扫描加收;普放:DR胸部正侧位片*(2);呼吸专科检查:支气管\n[BBOX-87] 舒张试验、流速容量曲线;\n[BBOX-88] 检验:凝血四项、肾功能六项+肝功能八项+血脂六项*+电解质六项+空\n[BBOX-89] 腹血糖(门诊使用)+肝酶学补充7项+心肌损伤六项、血常规5分类、尿\n[BBOX-90] 常规加化学分析、感染八项\n[BBOX-91] 治疗:静脉采血\n[BBOX-92] 根据患者病情,认为患者基本符合“评价SHR-1905注射液在重度未\n[BBOX-93] 控制哮喘患者中的有效性及安全性-多中心、随机、双盲、安慰剂对照\n[BBOX-94] 平行设计II期临床研究(SHR-1905-201)”的筛选要求,2024.01.10 09:15\n[BBOX-95] 生向患者__及其家属详细介绍该试验目的、试验设计、受试\n[BBOX-96] 者风险及受益、受试者义务及研究者义务等。根据方案(版本号:2.0,\n[BBOX-97] 版本日期:2022年8月31日)要求,筛选期所有受试者均进行吸入支气\n[BBOX-98] 管扩张剂前后肺功能检查,若受试者无法提供筛选前一年内气道可逆\n[BBOX-99] 性检测报告(吸入沙丁胺醇后FEV1增加≥12%且FEV1绝对值增加≥\n[BBOX-100] 200mL),则筛选期肺功能检查需要满足吸入沙丁胺醇后FEV1增加≥\n[BBOX-101] 12%且FEV1绝对值增加≥200mL。符合要求后才可以入组,受试者表\n[BBOX-102] 示同意。患者.__及其家属表示已充分了解以上告知内容,同意参加\n[BBOX-103] 该临床试验,\n[BBOX-104] 医生与患者__于2024.01.10 09:47同时签署了知\n[BBOX-105] 情同意书(版本号:2.0,版本日期:2022年08月31日),一式两份,一份\n[BBOX-106] 第3页\n[BBOX-107] 门诊病历\n[BBOX-108] 科室:呼吸与危重症医学科\n[BBOX-109] 姓名:\n[BBOX-110] 性别:女\n[BBOX-111] 门诊\n[BBOX-112] 联系方式\n[BBOX-113] 年龄:62岁\n[BBOX-114] 婚姻状况:其他\n[BBOX-115] 2024-01-10 10:27 初诊记录\n[BBOX-116] 交给患者保存,一份保存在研究中心。签署知情同意书后患者进入筛选\n[BBOX-117] 流程,受试者筛选号为CN..\n[BBOX-118] 新增AE:\n[BBOX-119] 1.高尿酸血症,2024.01.10开始,轻度,持续,与研究药物肯定无关,对研\n[BBOX-120] 究药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。\n[BBOX-121] 2.高脂血症,2024.01.10开始,轻度,持续,与研究药物肯定无关,对研究\n[BBOX-122] 药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。\n[BBOX-123] 3.白细胞计数降低,2024.01.10开始,轻度,持续,与研究药物肯定无关\n[BBOX-124] 对研究药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。此项\n[BBOX-125] 指标与患者临床症状不符,考虑让其一周内复测。\n[BBOX-126] 规律使用吸入药物,用后漱口,定期复诊;避免接触可能过敏原;不用地\n[BBOX-127] 毯,不养动物\n[BBOX-128] 医师签\n[BBOX-129] 门诊病历专用\n[BBOX-130] ※提醒:复诊时,请携带本病历记录,谢谢!※\n[BBOX-131] CS 扫描全能王\n[BBOX-132] 3亿人都在用的扫描App\n[BBOX-133] 门诊病历\n[BBOX-134] 科室:呼吸与危重症医学科\n[BBOX-135] 姓名:\n[BBOX-136] 性别:女\n[BBOX-137] 门诊\n[BBOX-138] 联系方\n[BBOX-139] 年龄:62岁\n[BBOX-140] 婚姻状况:其他\n[BBOX-141] 2024-03-21 08:40 初诊记录\n[BBOX-142] 主诉:SHR-1905-201 试验复筛\n[BBOX-143] 现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年\n[BBOX-144] 余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现\n[BBOX-145] 气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行\n[BBOX-146] 听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并\n[BBOX-147] 规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可\n[BBOX-148] 320ug bid,近日活动后气促再发,否认喘鸣音。无发热、胸痛。\n[BBOX-149] 2024.01.10参加SHR-1905-201临床试验,因白细胞计数<3.0*10^9/L符\n[BBOX-150] 合排除标准第12条筛败,于2024.03.01血液科就诊,无特殊处理,\n[BBOX-151] 2024.03.06进行SHR-1905-201试验二次知情。受试者今日返院完成V3\n[BBOX-152] 访视。\n[BBOX-153] 既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。\n[BBOX-154] 既往病史:\n[BBOX-155] 1.2022.12.10肝囊肿,持续;\n[BBOX-156] 2.2023.10.31鼻窦炎,持续;\n[BBOX-157] 3.2023.10.31双肺良性小结节,持续;\n[BBOX-158] 4.2023.11.03-2023.12.13,肺肺部感染;\n[BBOX-159] 5.2024.03.01开始,白细胞数降低1级;\n[BBOX-160] 6.2024.01.10开始,高脂蛋白a血症,\n[BBOX-161] 过敏史:否认食物、药物过敏史。\n[BBOX-162] 体格检查收缩压(mmHg):113;舒张压(mmHg):76\n[BBOX-163] 其他体格检查:09:37进行生命体征测量:体温:36.5℃,血压:\n[BBOX-164] 113/76mmHg,呼吸:18次/分,脉搏:98次/分;\n[BBOX-165] 查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见\n[BBOX-166] 第1页\n[BBOX-167] 科室:呼吸与危重症医学科\n[BBOX-168] 姓名\n[BBOX-169] 性别:女\n[BBOX-170] 门诊\n[BBOX-171] 联系方\n[BBOX-172] 年龄:62岁\n[BBOX-173] 婚姻状况:其他\n[BBOX-174] 2024-03-21 08:40 初诊记录\n[BBOX-175] 皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅\n[BBOX-176] 大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。\n[BBOX-177] 耳廓正常无畸形,外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无\n[BBOX-178] 鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿\n[BBOX-179] 大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中\n[BBOX-180] 肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动\n[BBOX-181] 正常,双肺呼吸音粗,未闻及干湿罗音。心律齐。双下肢无水肿。心音正\n[BBOX-182] 常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛、反跳痛,无液\n[BBOX-183] 波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触及,肾脏未触\n[BBOX-184] 及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖器未查、肛门\n[BBOX-185] 直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无异常,其他无\n[BBOX-186] 异常。.\n[BBOX-187] 检验检查:无\n[BBOX-188] 初步诊断:支气管哮喘\n[BBOX-189] 处理:\n[BBOX-190] CM 跟踪:\n[BBOX-191] 1、布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,\n[BBOX-192] 320ug,bid,经口腔吸入,用于控制哮喘。\n[BBOX-193] 处理:\n[BBOX-194] 1、2024.03.14-2024.03.21 家用峰流速仪使用 ePRO 系统填写依从性\n[BBOX-195] 7/7*100%=100%,嘱托患者按照自己实际情况及时填写日志,如有问题\n[BBOX-196] 随时沟通。\n[BBOX-197] 2、无新增 AE,CM,无临床试验安全性事件。\n[BBOX-198] 3、今日回收硫酸沙丁胺醇吸入气雾剂,发放新的硫酸沙丁胺醇吸入气\n[BBOX-199] 雾剂1盒,并嘱托受试者正确保存和使用。\n[BBOX-200] 4、绝经期女性,未做血、尿妊娠检查。\n[BBOX-201] 第2页\n[BBOX-202] CS 扫描全能王\n[BBOX-203] 3亿人都在用的扫描App\n[BBOX-204] 科室:呼吸与危重症医学科\n[BBOX-205] 门诊\n[BBOX-206] 姓名\n[BBOX-207] 联系方式\n[BBOX-208] 性别:女\n[BBOX-209] 年龄:62岁\n[BBOX-210] 婚姻状况:其他\n[BBOX-211] 2024-03-21 08:40 初诊记录\n[BBOX-212] 5、受试者所有检查结果经再次核对入排,符合所有入选标准,不符合任\n[BBOX-213] 一排除标准,可随机入组,分配随机号:_,随机分层信息:中剂量\n[BBOX-214] ICS,嗜酸性粒细胞计数<300/ul,未联合使用LAMA。\n[BBOX-215] 6、嘱托受试者2024.03.22来院行V4随访。\n[BBOX-216] 医师签\n[BBOX-217] 门诊病历专用章\n[BBOX-218] ※提醒:复诊时,请携带本病历记录,谢谢!※\n[BBOX-219] 第3页\n[BBOX-220] CS 扫描全能王\n[BBOX-221] 3亿人都在用的扫描App\n[BBOX-222] 科室:呼吸与危重症医学科\n[BBOX-223] 门诊\n[BBOX-224] 姓名\n[BBOX-225] 联系\n[BBOX-226] 性别:女\n[BBOX-227] 年龄:63岁\n[BBOX-228] 婚姻状况:其他\n[BBOX-229] 2024-12-12 09:40 初诊记录\n[BBOX-230] 主诉:SHR-1905-201 临床试验 V14\n[BBOX-231] 现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年\n[BBOX-232] 余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现\n[BBOX-233] 气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行\n[BBOX-234] 听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并\n[BBOX-235] 规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可\n[BBOX-236] 320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:\n[BBOX-237] 近日咳嗽咳痰,低烧两天,呼吸道感染。2024.12.02行V14随访\n[BBOX-238] 因患者发热延迟用药。今日回院用药,留院观察1h。\n[BBOX-239] 既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。\n[BBOX-240] 既往病史:\n[BBOX-241] 1.2022.12.10肝囊肿,持续;\n[BBOX-242] 2.2023.10.31鼻窦炎,持续;\n[BBOX-243] 3.2023.10.31双肺良性小结节,持续;\n[BBOX-244] 4.2023.11.03-2023.12.13,肺肺部感染;\n[BBOX-245] 5.2024.03.01开始,白细胞数降低1级,持续;\n[BBOX-246] 6.2024.01.10开始,高脂血症,持续;\n[BBOX-247] 7.十余年前,慢性浅表胃炎,持续中。\n[BBOX-248] 过敏史:否认食物、药物过敏史。\n[BBOX-249] 体格检查收缩压(mmHg):-;舒张压(mmHg):-\n[BBOX-250] 其他体格检查:未行\n[BBOX-251] 检验检查:无\n[BBOX-252] 初步诊断:支气管哮喘\n[BBOX-253] 处理:检查:心脏电生理:心电图(十二导联心电图);\n[BBOX-254] 检验:急诊血常规(五分类)+急诊超敏C反应蛋白、急诊肝功能五项\n[BBOX-255] 治疗:静脉采血\n[BBOX-256] 第1页\n[BBOX-257] 科室:呼吸与危重症医学科\n[BBOX-258] 性别:女\n[BBOX-259] 年龄:63岁\n[BBOX-260] 婚姻状况:其他\n[BBOX-261] 2024-12-12 09:40 初诊记录\n[BBOX-262] 无新增 AE,无新增 CM,无临床试验安全性事件。\n[BBOX-263] 呼吸道感染,2024.11.27-2024.12.11,中度,与试验药物关系为可能无关\n[BBOX-264] 对试验药物采取的措施为延迟用药,对 AE 采取的措施为药物治疗,肺\n[BBOX-265] SAE,非 SIE,不因此退出临床试验。\n[BBOX-266] 跟踪 CM:\n[BBOX-267] 1.盐酸莫西沙片,2024.12.02-2024.12.11,持续中,0.4g/片,1片/次,\n[BBOX-268] qd,po,用于治疗 AE 呼吸道感染。\n[BBOX-269] 2.桉柠蒎肠溶胶囊,2024.12.02-2024.12.11 持续中,0.3g/粒,1粒/次,\n[BBOX-270] tid,po,用于治疗 AE 呼吸道感染。(化痰)\n[BBOX-271] 3.氯苯那敏片,2024.12.02-2024.12.11,持续中,4mg/片,1片/次,\n[BBOX-272] qn,po,用于治疗 AE 呼吸道感染。\n[BBOX-273] 4.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po,用于治\n[BBOX-274] 疗病史慢性浅表胃炎。\n[BBOX-275] 5.复方氨酚烷胺胶囊,2024.11.27-2024.12.02,持续中,0.25g:0.1g,1粒\n[BBOX-276] /次,bid,po,用于治疗 AE 呼吸道感染。\n[BBOX-277] 6.吸入沙丁胺醇气雾剂,2024.12.02-2024.12.02,400ug,吸入,once,用于支\n[BBOX-278] 气管扩张检查。\n[BBOX-279] CM 跟踪:\n[BBOX-280] 1、布地奈德福莫特罗粉吸入剂,2022.11.27 开始,持续使用,\n[BBOX-281] 320ug,bid,经口腔吸入,用于控制哮喘。\n[BBOX-282] 2、硫酸沙丁胺醇气雾剂,2024.03.06 开始,持续中,100ug,pm,经口腔吸\n[BBOX-283] 入,控制哮喘急性发作。\n[BBOX-284] 第2页\n[BBOX-285] 门诊病历\n[BBOX-286] 科室:呼吸与危重症医学科\n[BBOX-287] 姓名:\n[BBOX-288] 性别:女\n[BBOX-289] 门诊号\n[BBOX-290] 联系方式\n[BBOX-291] 年龄:63岁\n[BBOX-292] 婚姻状况:其他\n[BBOX-293] 2024-12-12 09:40 初诊记录\n[BBOX-294] 处理:\n[BBOX-295] 患者于今日 12:21-12:28 完成临床试验药物的注射,药物编号为\n[BBOX-296] Y6077Y4950 用药前完善必要检查后随机用药。\n[BBOX-297] 医师\n[BBOX-298] 门诊病历\n[BBOX-299] ※提醒:复诊时,请携带本病历记录,谢谢!※\n[BBOX-300] “若有高血压糖尿病诊断,建议您到居住地附近社康中心,建立居民健康档案”\n[BBOX-301] 门诊病历\n[BBOX-302] 科室:呼吸与危重症医学科\n[BBOX-303] 姓名\n[BBOX-304] 性别:女\n[BBOX-305] 门诊\n[BBOX-306] 联系方式\n[BBOX-307] 年龄:63岁\n[BBOX-308] 婚姻状况:其他\n[BBOX-309] 2025-07-31 17:13 初诊记录\n[BBOX-310] 主诉:SHR-1905V19随访\n[BBOX-311] 现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年\n[BBOX-312] 余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现\n[BBOX-313] 气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行\n[BBOX-314] 听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并\n[BBOX-315] 规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可\n[BBOX-316] 320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:\n[BBOX-317] 20036.。近日无咳嗽咳痰,无胸闷气喘,无发热,无支气管哮喘急性发作\n[BBOX-318] 今日回院行V19随访。\n[BBOX-319] 既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。\n[BBOX-320] 既往病史:\n[BBOX-321] 1.2022.12.10肝囊肿,持续;\n[BBOX-322] 2.2023.10.31鼻窦炎,持续;\n[BBOX-323] 3.2023.10.31双肺良性小结节,持续;\n[BBOX-324] 4.2023.11.03-2023.12.13,肺肺部感染;\n[BBOX-325] 5.2024.03.01开始,白细胞数降低1级,持续;\n[BBOX-326] 6.2024.01.10高脂血症,持续中\n[BBOX-327] 过敏史:否认食物、药物过敏史。\n[BBOX-328] 体格检查收缩压(mmHg):103;舒张压(mmHg):64\n[BBOX-329] 其他体格检查:进行生命体征测量:体温:36.4℃,血压:\n[BBOX-330] 103/64mmHg,呼吸:18次/分,脉搏:76次/分;\n[BBOX-331] 查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见\n[BBOX-332] 皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅\n[BBOX-333] 大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。\n[BBOX-334] 耳廓正常无畸形外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无\n[BBOX-335] 鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿\n[BBOX-336] 第1页\n[BBOX-337] 门诊病历\n[BBOX-338] 科室:呼吸与危重症医学科\n[BBOX-339] 性别:女\n[BBOX-340] 门诊\n[BBOX-341] 联系方式:\n[BBOX-342] 年龄:63岁\n[BBOX-343] 婚姻状况:其他\n[BBOX-344] 2025-07-31 17:13 初诊记录\n[BBOX-345] 大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中\n[BBOX-346] 肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动\n[BBOX-347] 正常,左肺呼吸音清,未闻及粗干啰音。心律齐。双下肢无水肿。心音正\n[BBOX-348] 常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛、反跳痛,无液\n[BBOX-349] 波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触及,肾脏未触\n[BBOX-350] 及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖器未查、肛门\n[BBOX-351] 直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无异常,其他无\n[BBOX-352] 异常。\n[BBOX-353] 检验检查:已完善试验相关检验检查\n[BBOX-354] 初步诊断:支气管哮喘\n[BBOX-355] 处理:尿常规检查尿隐血,建议定期检查,必要时肾内科就诊。\n[BBOX-356] 无临床试验安全性事,无新增 AE。\n[BBOX-357] 新增合并用药:硫酸沙丁胺醇吸入气雾剂,2025.07.31-\n[BBOX-358] 2025.078.31,400ug,once,吸入,用于支气管扩张检查。\n[BBOX-359] CM 跟踪:\n[BBOX-360] 1、布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,\n[BBOX-361] 320ug,bid,经口腔吸入,用于控制哮喘。\n[BBOX-362] 2、硫酸沙丁胺醇气雾剂,2024.03.06开始,持续中,100ug,pm,经口腔吸\n[BBOX-363] 入,控制哮喘急性发作。\n[BBOX-364] 3.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po.用于治\n[BBOX-365] 疗病史慢性浅表胃炎。\n[BBOX-366] 处理:\n[BBOX-367] 12025.05.13-2025.07.31 家用峰流速仪使用 ePRO 系统填写依从性大于\n[BBOX-368] 80%,今日已解绑 ePRO 系统。\n[BBOX-369] 2遵从临床试验方案完成 IgE,PK,ADA 采血,完成 ACQ-6,AQLQ 问卷填\n[BBOX-370] 写。\n[BBOX-371] 门诊病历\n[BBOX-372] 科室:呼吸与危重症医学科\n[BBOX-373] 姓名\n[BBOX-374] 性别:女\n[BBOX-375] 门诊\n[BBOX-376] 联系\n[BBOX-377] 年龄:63岁\n[BBOX-378] 婚姻状况:其他\n[BBOX-379] 2025-07-31 17:13 初诊记录\n[BBOX-380] 3.患者于今日肺功能检查前已停用基础吸入药物布地奈德福莫特罗粉\n[BBOX-381] 吸入剂大于12h,停药时间2025.07.30上午,具体时间不详。\n[BBOX-382] 4.患者已于今日完成随访期随访。\n[BBOX-383] 5.因患者未找到发放万托林,可能已经丢失故不予回收。\n[BBOX-384] 6.嘱患者规律使用吸入药物布地奈德福莫特罗粉吸入剂,药物自备。\n[BBOX-385] 医师\n[BBOX-386] 门诊病历专用章\n[BBOX-387] ※提醒:复诊时,请携带本病历记录,谢谢!※\n[BBOX-388] “若有高血压糖尿病诊断,建议您到居住地附近社康中心,建立居民健康档案”\n[BBOX-389] 第3页\n[BBOX-390] 门诊\n[BBOX-391] 姓名：\n[BBOX-392] 门(急)诊初诊病历\n[BBOX-393] 性别：女\n[BBOX-394] 科室：呼吸内科门诊\n[BBOX-395] 年龄：63岁\n[BBOX-396] 就诊日期：2025-10-25 15:22\n[BBOX-397] 主诉：支气管哮喘复诊\n[BBOX-398] 现病史：患者支气管哮喘复诊，目前规律吸入布地奈德福莫特罗320ug 一次1吸，\n[BBOX-399] 一天2次。目前诉有咳嗽、咳痰，有气促感，无胸闷，无发热，无鼻塞、流涕，无咯\n[BBOX-400] 血、痰中带血，无头痛、头晕、视物旋转，无饮水呛咳，无咽痛、腹痛、腹胀等不\n[BBOX-401] 适。未予处理及就医。现患者为求进一步诊治，故至我院科门诊就医。\n[BBOX-402] 既往史：否认高血压、否认糖尿病、否认冠心病等慢性疾病病史，否认肝炎、结核\n[BBOX-403] 等传染病史，否认手术外伤输血史 过敏史：无食物、药物过敏史。。否认饮酒史。\n[BBOX-404] 个人史：已婚已育\n[BBOX-405] 家族史：否认家族病史。\n[BBOX-406] 体格检查：T：36.8℃ P：87次/分 R：21次/分 BP：108/73mmHg 指脉氧：\n[BBOX-407] 9%。神志清楚，精神尚可，呼吸平顺，口唇无发绀，咽部无充血，扁桃体无肿大，\n[BBOX-408] 双侧颈静脉无怒张，双肺呼吸音粗，双肺可闻及干啰音，双肺未闻及湿性啰音及胸膜\n[BBOX-409] 摩擦音。心率87次/分，律齐，各瓣膜未闻及明显病理性杂音。腹部平软，全腹部无\n[BBOX-410] 玉痛，反跳痛，肠鸣音正常。四肢运动自如，双下肢无水肿。\n[BBOX-411] 辅助检查：患者自行购买布地奈德福莫特罗320ug 一次1吸，一天2次。\n[BBOX-412] 初步诊断：\n[BBOX-413] 西医诊断：1.支气管哮喘(急性发作期)\n[BBOX-414] 处理意见：\n[BBOX-415] 醋酸泼尼松片（国基）(5mg*100片) 20.000mg\n[BBOX-416] 1次/天 口服\n[BBOX-417] 12.00片\n[BBOX-418] 硫酸沙丁胺醇吸入气雾剂（省3、国基）(200揿：\n[BBOX-419] 100μg) 200.000μg\n[BBOX-420] 1次/天 吸入\n[BBOX-421] 1.00瓶\n[BBOX-422] 建议：建议患者结果回报后请及时至我科门诊复诊，若出现病情变化或病情加重\n[BBOX-423] 无好转等，请及时至急诊科门诊复诊。\n[BBOX-424] 温馨提示：1.请妥善保管好病历及各种检查检验报告单。\n[BBOX-425] 2.复诊时，请携带本病历记录，谢谢！\n[BBOX-426] 第1页(共1页)\n[BBOX-427] 广东省医疗门诊收费票据（电子）\n[BBOX-428] 广东省\n[BBOX-429] 财政部监制\n[BBOX-430] 票据代码：44060125\n[BBOX-431] 票据号码：9148002082\n[BBOX-432] 校验码： 831306\n[BBOX-433] 开票日期：2025-10-25\n[BBOX-434] 项目名称\n[BBOX-435] 数量/单位\n[BBOX-436] 金额（元）\n[BBOX-437] 备注\n[BBOX-438] 项目名称\n[BBOX-439] 数量/单位\n[BBOX-440] 金额（元）\n[BBOX-441] 备注\n[BBOX-442] 西药费\n[BBOX-443] 1\n[BBOX-444] 13.05\n[BBOX-445] 以下是清单项\n[BBOX-446] 醋酸泼尼松片（国基）\n[BBOX-447] 12\n[BBOX-448] 0.50\n[BBOX-449] 硫酸沙丁胺醇吸入气雾剂（省3\n[BBOX-450] 1\n[BBOX-451] 12.55\n[BBOX-452] 、国基）\n[BBOX-453] 金额合计（大写）壹拾叁元零伍分\n[BBOX-454] (小写)13.05\n[BBOX-455] 业务流水号：SF10390911\n[BBOX-456] 门诊\n[BBOX-457] 就诊日期：20251025\n[BBOX-458] 其他信息\n[BBOX-459] 医疗机构类型：综合医院\n[BBOX-460] 医保类型：现金(自费)\n[BBOX-461] 医保编号：\n[BBOX-462] 性别：女\n[BBOX-463] 医保统筹基金支付：0.00\n[BBOX-464] 其他支付：0.00\n[BBOX-465] 个人账户支付：0.00\n[BBOX-466] 个人现金支付：13.05\n[BBOX-467] 个人自付：0.00\n[BBOX-468] 个人自费：13.05\n[BBOX-469] 政策性减免：\n[BBOX-470] 收款单位（章）深圳市龙岗区第人民医院\n[BBOX-471] 复核人：掌上医院\n[BBOX-472] 收款人：掌上医院\n[BBOX-473] 说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。\n[BBOX-474] 单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dzpj.czt.gd.gov.cn/billcheck查验本省财政电子票据。\n[BBOX-475] CS 扫描全能王\n[BBOX-476] 3 亿人都在用的扫描 App\n[BBOX-477] 电子发票(普通发票)\n[BBOX-478] 发票号码：25447000001429974977\n[BBOX-479] 开票日期：2025年11月05日\n[BBOX-480] 广东省税务局\n[BBOX-481] 购买方信息\n[BBOX-482] 名称：\n[BBOX-483] 统一社会信用代码/纳税人识别号：\n[BBOX-484] 销售方信息\n[BBOX-485] 名称：阿里健康大药房医药连锁有限公司\n[BBOX-486] 统一社会信用代码/纳税人识别号：91440101681325547Y\n[BBOX-487] 项目名称\n[BBOX-488] 规格型号\n[BBOX-489] 单位\n[BBOX-490] 数量\n[BBOX-491] 单价\n[BBOX-492] 金额\n[BBOX-493] 税率/征收率\n[BBOX-494] 税额\n[BBOX-495] *化学药品制剂*布地奈德\n[BBOX-496] 盒\n[BBOX-497] 3\n[BBOX-498] 176.70\n[BBOX-499] 530.09\n[BBOX-500] 13%\n[BBOX-501] 68.91\n[BBOX-502] 福莫特罗吸入粉雾剂\n[BBOX-503] 合计\n[BBOX-504] ￥530.09\n[BBOX-505] ￥68.91\n[BBOX-506] 价税合计（大写）\n[BBOX-507] 伍佰玖拾玖圆整\n[BBOX-508] (小写)￥599.00\n[BBOX-509] 备注\n[BBOX-510] 开票人：董茜玲\n[BBOX-511] CS 扫描全能王\n[BBOX-512] 3亿人都在用的扫描App\n[BBOX-513] 门诊号\n[BBOX-514] 姓名\n[BBOX-515] 科室:呼吸内科门诊\n[BBOX-516] 门(急)诊初诊病历\n[BBOX-517] 电话\n[BBOX-518] 性别:女\n[BBOX-519] 年龄:63岁\n[BBOX-520] 就诊日期:2025-11-24 15:01\n[BBOX-521] 主诉:支气管哮喘复诊\n[BBOX-522] 现病史:患者支气管哮喘复诊,目前规律吸入布地奈德福莫特罗320一次1吸,一天2次(患者自行网购药物),目前有咳嗽、咳痰,咳嗽时有气喘感。无胸闷,无发热,无鼻塞、流涕,无咯血、痰中带血,无头痛、头晕、视物旋转,无饮水呛咳,无咽痛、腹痛、腹胀等不适。未予处理及就医。现患者为求进一步诊治,故至我院科门诊就医。\n[BBOX-523] 既往史:否认高血压、否认糖尿病、否认冠心病等慢性疾病病史,否认肝炎、结核等传染病史,否认手术外伤输血史过敏史:无食物、药物过敏史。。否认饮酒史。\n[BBOX-524] 个人史:已婚已育\n[BBOX-525] 家族史:否认家族病史。\n[BBOX-526] 体格检查:T:36.8℃ P:87次/分 R:21次/分 BP:108/73mmHg 指脉氧:\n[BBOX-527] 9%。神志清楚,精神尚可,呼吸平顺,口唇无发绀,咽部无充血,扁桃体无肿大,\n[BBOX-528] 双侧颈静脉无怒张,双肺呼吸音粗,双肺可闻及散在干啰音,双肺未闻及湿性啰音及\n[BBOX-529] 胸膜摩擦音。心率87次/分,律齐,各瓣膜未闻及明显病理性杂音。腹部平软,全腹\n[BBOX-530] 邻无压痛,反跳痛,肠鸣音正常。四肢运动自如,双下肢无水肿。\n[BBOX-531] 辅助检查:\n[BBOX-532] 初步诊断:\n[BBOX-533] 西医诊断:1.支气管哮喘(急性发作期)\n[BBOX-534] 处理意见:自备布地奈德福莫特罗320一次1吸,一天2次\n[BBOX-535] 醋酸泼尼松片(国基)(5mg*100片)10.000mg\n[BBOX-536] 1次/天 口服 6.00片\n[BBOX-537] 建议:建议患者结果回报后请及时至我科门诊复诊,若出现病情变化或病情加重\n[BBOX-538] 无好转等,请及时至急诊科门诊复诊。\n[BBOX-539] 医生签名:\n[BBOX-540] 温馨提示:1.请妥善保管好病历及各种检查检验报告单。\n[BBOX-541] 2.复诊时,请携带本病历记录,谢谢!\n[BBOX-542] 第1页(共1页)\n[BBOX-543] CS 扫描全能王\n[BBOX-544] 3亿人都在用的扫描App\n[BBOX-545] 广东省医疗门诊收费票据（电子）\n[BBOX-546] 广东省\n[BBOX-547] 财政部监制\n[BBOX-548] 票据代码：44\n[BBOX-549] 票据号码：9148286284\n[BBOX-550] 校验码：89a81f\n[BBOX-551] 交款人\n[BBOX-552] 开票日期：2025-11-24\n[BBOX-553] 项目名称\n[BBOX-554] 数量/单位\n[BBOX-555] 金额（元）\n[BBOX-556] 备注\n[BBOX-557] 项目名称\n[BBOX-558] 数量/单位\n[BBOX-559] 金额（元）\n[BBOX-560] 备注\n[BBOX-561] 西药费\n[BBOX-562] 1\n[BBOX-563] 0.25\n[BBOX-564] 以下是清单项\n[BBOX-565] 醋酸泼尼松片（国基）\n[BBOX-566] 6\n[BBOX-567] 0.25\n[BBOX-568] 金额合计（大写）贰角伍分\n[BBOX-569] (小写)0.25\n[BBOX-570] 业务流水号：SF10481981\n[BBOX-571] 门\n[BBOX-572] 就诊日期：20251124\n[BBOX-573] 其他信息\n[BBOX-574] 医疗机构类型：综合医院\n[BBOX-575] 医保类型：现金(自费)\n[BBOX-576] 医保编号：\n[BBOX-577] 性别：女\n[BBOX-578] 医保统筹基金支付：0.00\n[BBOX-579] 其他支付：0.00\n[BBOX-580] 个人账户支付：0.00\n[BBOX-581] 个人现金支付：0.25\n[BBOX-582] 个人自付：0.00\n[BBOX-583] 个人自费：0.25\n[BBOX-584] 政策性减免：\n[BBOX-585] 收款单位（章）\n[BBOX-586] 人民医院\n[BBOX-587] 复核人：吴亮梅\n[BBOX-588] 收款人：吴亮梅\n[BBOX-589] 说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。\n[BBOX-590] 单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dipj.czt.gd.gov.cn/billcheck查验本省财政电子票据。\n[BBOX-591] CS 扫描全能王\n[BBOX-592] 3亿人都在用的扫描App\n[BBOX-593] 10:15\n[BBOX-594] 淘\n[BBOX-595] 交易成功\n[BBOX-596] 医药仁康堂医药专营店>\n[BBOX-597] 【信必可】布地奈德福莫特罗[\n[BBOX-598] ¥213\n[BBOX-599] 放心买药\n[BBOX-600] 正品保障\n[BBOX-601] 1盒装\n[BBOX-602] 不支持7天无理由 假一赔四>\n[BBOX-603] x1\n[BBOX-604] 专业药师在线服务\n[BBOX-605] 上天猫放心买药\n[BBOX-606] 用药小贴士 1.哮喘。2.慢性阻塞性肺疾病(慢阻肺;...\n[BBOX-607] 申请售后\n[BBOX-608] 商品总价\n[BBOX-609] ¥213\n[BBOX-610] 运费(含服务费)\n[BBOX-611] ¥8\n[BBOX-612] 应付款\n[BBOX-613] ¥221^\n[BBOX-614] 订单信息 2026-01-20\n[BBOX-615] 收起^\n[BBOX-616] 订单编号\n[BBOX-617] 4501919772001020746\n[BBOX-618] 交易快照\n[BBOX-619] 发生交易争议时，可作为判断依据>\n[BBOX-620] 成交时间\n[BBOX-621] 2026-01-26 22:25:02\n[BBOX-622] 发货时间\n[BBOX-623] 2026-01-21 12:24:52\n[BBOX-624] 付款时间\n[BBOX-625] 2026-01-20 19:25:06\n[BBOX-626] 创建时间\n[BBOX-627] 2026-01-20 19:24:30\n[BBOX-628] 支付宝交易号\n[BBOX-629] 2026012022001134951454085519\n[BBOX-630] 天猫积分\n[BBOX-631] 获得106点积分>\n[BBOX-632] 客服\n[BBOX-633] 更多\n[BBOX-634] 查看处方\n[BBOX-635] 查看物流\n[BBOX-636] 评价\n[BBOX-637] 扫描全能王\n[BBOX-638] 扫描全能王\n[BBOX-639] 3亿人都在用的扫描App\n[BBOX-640] 电子发票(普通发票)\n[BBOX-641] 发票号码：26322000000914042776\n[BBOX-642] 开票日期：2026年02月02日\n[BBOX-643] 江苏省税务局\n[BBOX-644] 购买方信息\n[BBOX-645] 名称：\n[BBOX-646] 统一社会信用代码/纳税人识别号：\n[BBOX-647] 销售方信息\n[BBOX-648] 名称：阜宁仁康堂大药房有限公司\n[BBOX-649] 统一社会信用代码/纳税人识别号：91320923MAK1XP619R\n[BBOX-650] 项目名称\n[BBOX-651] 规格型号\n[BBOX-652] 单位\n[BBOX-653] 数量\n[BBOX-654] 单价\n[BBOX-655] 金额\n[BBOX-656] 税率/征收率\n[BBOX-657] 税额\n[BBOX-658] *生物化学药品*其他生物\n[BBOX-659] 1\n[BBOX-660] 218.811881188119\n[BBOX-661] 218.81\n[BBOX-662] 1%\n[BBOX-663] 2.19\n[BBOX-664] 化学药品\n[BBOX-665] 合计\n[BBOX-666] ￥218.81\n[BBOX-667] ￥2.19\n[BBOX-668] 价税合计（大写）\n[BBOX-669] 贰佰贰拾壹圆整\n[BBOX-670] (小写)￥221.00\n[BBOX-671] 备注\n[BBOX-672] 开票人：杨雪\n[BBOX-673] CS 扫描全能王\n[BBOX-674] 3亿人都在用的扫描App"
  }
]
2026-08-10 11:42:19,903 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:42:19,926 INFO     29 [SmartSplitter] SmartSplitter done: 11 chunks from 11 LLM segments (all bbox_id). Types: {'OutpatientRecord': 6, 'MedicationRecord': 5}
2026-08-10 11:42:19,943 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 11:42:19,943 INFO     29 [Trace] task=38277e3a | doc=LZQ 64 哮喘 深圳二院.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "675 items", "markdown": "", "text": "", "name": "LZQ 64 哮喘 深圳二院.pdf", "output_format": "chunks", "chunks": "11 items, types={'OutpatientRecord': 6, 'MedicationRecord': 5}"}
2026-08-10 11:42:19,943 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 11:42:19,945 INFO     29 [ChunkRouter] Routed 11 chunks into 2 groups: {'chunks_Clinical': 6, 'chunks_Medication': 5}
2026-08-10 11:42:19,957 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 11:42:19,957 INFO     29 [Trace] task=38277e3a | doc=LZQ 64 哮喘 深圳二院.pdf | ChunkRouter:Router | outputs={"html": "", "json": "675 items", "markdown": "", "text": "", "name": "LZQ 64 哮喘 深圳二院.pdf", "output_format": "chunks", "chunks": "11 items, types={'OutpatientRecord': 6, 'MedicationRecord': 5}", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Medication\": 5}"}
2026-08-10 11:42:19,957 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 11:42:19,963 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:42:19,963 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:42:20,727 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:42:20,735 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 11:42:20,736 INFO     29 [Trace] task=38277e3a | doc=LZQ 64 哮喘 深圳二院.pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "675 items", "markdown": "", "text": "", "name": "LZQ 64 哮喘 深圳二院.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Medication\": 5}"}
2026-08-10 11:42:20,736 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 11:42:20,742 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:42:20,742 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:42:21,145 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:42:21,155 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 11:42:21,155 INFO     29 [Trace] task=38277e3a | doc=LZQ 64 哮喘 深圳二院.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "675 items", "markdown": "", "text": "", "name": "LZQ 64 哮喘 深圳二院.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Medication\": 5}"}
2026-08-10 11:42:21,155 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 11:42:21,165 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:42:21,166 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:42:21,166 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:42:21,166 INFO     29 [qwen-vl-text] positions(131): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:42:21,166 INFO     29 [qwen-vl-text] page grouping: [0, 1, 2, 3], lines per page: [35, 35, 37, 24]
2026-08-10 11:42:21,423 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:42:21,667 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:42:21,958 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:42:22,169 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:42:22,173 INFO     29 [qwen-vl-text] LLM extraction start, text_len=2847
2026-08-10 11:42:22,173 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:42:22,173 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 130, \"encounter_dates\": [\"2024-01-10\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊病历\n科室:呼吸与危重症医学科\n门\n联系人\n性别:女\n年龄:62岁\n婚姻状况:其他\n2024-01-10 10:27 初诊记录\n主诉:发作性喘息12年余\n现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年\n余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现\n气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行\n听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并\n规律使用信必可320ug bid后症状缓解。近日活动后气促再发,否认喘\n鸣音。无发热、胸痛。\n既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。\n既往病史:\n1.2022.12.10肝囊肿,持续;\n2.2023.10.31鼻窦炎,持续;\n3.2023.10.31双肺良性小结节,持续;\n4.2023.11.03-2023.12.13,肺肺部感染;\n一年内支气管哮喘急性发作病史:\n12023.11.03-2023.11.08,支气管哮喘急性发作,8mg、4mg甲泼尼龙qd\n各服用3天;\n22023.12.13-2023.12.15,支气管哮喘急性发作,4mg甲泼尼龙片qd,服用\n3天。\n一年内合并用药:\n1.左氧氟沙星片,2023.11.03-2023.12.01,0.5g,qd,po,用于治疗肺部感染\n2.甲泼尼龙片,2023.11.03-2023.11.05,8mg,qd,po,用于治疗支气管哮喘急\n性发作。\n3.甲泼尼龙片,2023.11.06-2023.11.08,4mg,qd,po,用于治疗支气管哮喘急\n性发作。\n4.孟鲁司特钠片,2023.11.03-2023.11.12,10mg,qn,po,用于治疗支气管哮喘\n急性发作。\n第1页\n门诊病历\n科室:呼吸与危重症医学科\n姓名\n性别:女\n年龄:62岁\n婚姻状况:其他\n联系方式\n2024-01-10 10:27 初诊记录\n5.桉柠蒎肠溶软胶囊,2023.11.03-2023.11.15,0.3g,tid,po,用于治疗肺部感\n染。\n7.甲泼尼龙片,2023.12.13-2023.12.15,4mg,qd,po,用于治疗支气管哮喘急\n性发作。\n8.布地奈德福莫特罗粉吸入剂,2022.11.27开始,持续使用,\n320ug,bid,经口腔吸入,用于控制哮喘。\n过敏史:否认食物、药物过敏史。\n体格检查 收缩压（mmHg）:107;舒张压（mmHg）:75\n其他体格检查:身高:153cm,体重:48.5kg,\n09:50进行生命体征测量:体温:36.4℃,血压:107/75mmHg,呼吸:19\n次/分,脉搏:78次/分;\n查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见\n皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅\n大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。\n耳廓正常无畸形,外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无\n鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿\n大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中\n肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动\n正常,双肺呼吸音粗,未闻及干湿罗音。心律齐。双下肢无水肿。心率\n78次/分,心音正常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛\n反跳痛,无液波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触\n及,肾脏未触及,Murphy征阴性,移动性浊音阴性,肠鸣音正常。外生殖\n器未查、肛门直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无\n异常,其他无异常。\n第2页\nCS 扫描全能王\n3亿人都在用的扫描App\n科室:呼吸与危重症医学科\n姓名:\n性别:女\n门诊\n联系方式\n596\n年龄:62岁\n婚姻状况:其他\n2024-01-10 10:27 初诊记录\n检验检查:阅片见双肺轻度支气管扩张,未见明显急性炎症病灶,余肺基本同前\n(正式报告为准)\n初步诊断:1.鼻窦炎;2.支气管哮喘;\n处理:药品:\n(省采3)硫酸沙丁胺醇吸入气雾剂200揿(100μg/揿)/瓶(1【瓶】) sig:\n(200【揿】)吸入pm(需要时);\n检查:心脏电生理:心电图(十二导联心电图);CT检查:副鼻窦平扫;\n使用螺旋扫描加收;普放:DR胸部正侧位片*(2);呼吸专科检查:支气管\n舒张试验、流速容量曲线;\n检验:凝血四项、肾功能六项+肝功能八项+血脂六项*+电解质六项+空\n腹血糖(门诊使用)+肝酶学补充7项+心肌损伤六项、血常规5分类、尿\n常规加化学分析、感染八项\n治疗:静脉采血\n根据患者病情,认为患者基本符合“评价SHR-1905注射液在重度未\n控制哮喘患者中的有效性及安全性-多中心、随机、双盲、安慰剂对照\n平行设计II期临床研究(SHR-1905-201)”的筛选要求,2024.01.10 09:15\n生向患者__及其家属详细介绍该试验目的、试验设计、受试\n者风险及受益、受试者义务及研究者义务等。根据方案(版本号:2.0,\n版本日期:2022年8月31日)要求,筛选期所有受试者均进行吸入支气\n管扩张剂前后肺功能检查,若受试者无法提供筛选前一年内气道可逆\n性检测报告(吸入沙丁胺醇后FEV1增加≥12%且FEV1绝对值增加≥\n200mL),则筛选期肺功能检查需要满足吸入沙丁胺醇后FEV1增加≥\n12%且FEV1绝对值增加≥200mL。符合要求后才可以入组,受试者表\n示同意。患者.__及其家属表示已充分了解以上告知内容,同意参加\n该临床试验,\n医生与患者__于2024.01.10 09:47同时签署了知\n情同意书(版本号:2.0,版本日期:2022年08月31日),一式两份,一份\n第3页\n门诊病历\n科室:呼吸与危重症医学科\n姓名:\n性别:女\n门诊\n联系方式\n年龄:62岁\n婚姻状况:其他\n2024-01-10 10:27 初诊记录\n交给患者保存,一份保存在研究中心。签署知情同意书后患者进入筛选\n流程,受试者筛选号为CN..\n新增AE:\n1.高尿酸血症,2024.01.10开始,轻度,持续,与研究药物肯定无关,对研\n究药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。\n2.高脂血症,2024.01.10开始,轻度,持续,与研究药物肯定无关,对研究\n药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。\n3.白细胞计数降低,2024.01.10开始,轻度,持续,与研究药物肯定无关\n对研究药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。此项\n指标与患者临床症状不符,考虑让其一周内复测。\n规律使用吸入药物,用后漱口,定期复诊;避免接触可能过敏原;不用地\n毯,不养动物\n医师签\n门诊病历专用\n※提醒:复诊时,请携带本病历记录,谢谢!※",
    "role": "user"
  }
]
2026-08-10 11:42:27,570 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:42:27.569+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 24, "failed": 0, "current": {"38277e3a94b011f1bd9827cf206dfa2d": {"id": "38277e3a94b011f1bd9827cf206dfa2d", "doc_id": "370244ae94b011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479740, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362000249, "task_type": "dataflow", "root_trace_id": "96cd8dab6bb7455194a762d3f16e1d52", "root_traceparent": "00-96cd8dab6bb7455194a762d3f16e1d52-1e133766dfd81337-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:42:31,678 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:42:31,678 INFO     29 [qwen-vl-text] LLM output (len=1654):
{
  "encounter_date": "2024-01-10",
  "chief_complaint": "发作性喘息12年余",
  "present_illness": "发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并规律使用信必可320ug bid后症状缓解。近日活动后气促再发,否认喘鸣音。无发热、胸痛。",
  "past_history": "否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。既往病史:1.2022.12.10肝囊肿,持续;2.2023.10.31鼻窦炎,持续;3.2023.10.31双肺良性小结节,持续;4.2023.11.03-2023.12.13,肺肺部感染;一年内支气管哮喘急性发作病史:12023.11.03-2023.11.08,支气管哮喘急性发作,8mg、4mg甲泼尼龙qd各服用3天;22023.12.13-2023.12.15,支气管哮喘急性发作,4mg甲泼尼龙片qd,服用3天。一年内合并用药:1.左氧氟沙星片,2023.11.03-2023.12.01,0.5g,qd,po,用于治疗肺部感染2.甲泼尼龙片,2023.11.03-2023.11.05,8mg,qd,po,用于治疗支气管哮喘急性发作。3.甲泼尼龙片,2023.11.06-2023.11.08,4mg,qd,po,用于治疗支气管哮喘急性发作。4.孟鲁司特钠片,2023.11.03-2023.11.12,10mg,qn,po,用于治疗支气管哮喘急性发作。5.桉柠蒎肠溶软胶囊,2023.11.03-2023.11.15,0.3g,tid,po,用于治疗肺部感染。7.甲泼尼龙片,2023.12.13-2023.12.15,4mg,qd,po,用于治疗支气管哮喘急性发作。8.布地奈德福莫特罗粉吸入剂,2022.11.27开始,持续使用,320ug,bid,经口腔吸入,用于控制哮喘。",
  "diagnosis": "1.鼻窦炎;2.支气管哮喘;",
  "treatment_plan": {
    "medications": [
      {
        "name": "硫酸沙丁胺醇吸入气雾剂",
        "spec": "200揿(100μg/揿)/瓶",
        "dosage": "200揿",
        "frequency": "pm(需要时)",
        "route": "吸入"
      }
    ],
    "examinations": [
      "心脏电生理:心电图(十二导联心电图)",
      "CT检查:副鼻窦平扫;使用螺旋扫描加收",
      "普放:DR胸部正侧位片*(2)",
      "呼吸专科检查:支气管舒张试验、流速容量曲线"
    ],
    "labs": [
      "凝血四项",
      "肾功能六项+肝功能八项+血脂六项*+电解质六项+空腹血糖(门诊使用)+肝酶学补充7项+心肌损伤六项",
      "血常规5分类",
      "尿常规加化学分析",
      "感染八项"
    ],
    "treatments": [
      "静脉采血"
    ],
    "notes": "根据患者病情,认为患者基本符合“评价SHR-1905注射液在重度未控制哮喘患者中的有效性及安全性-多中心、随机、双盲、安慰剂对照平行设计II期临床研究(SHR-1905-201)”的筛选要求...规律使用吸入药物,用后漱口,定期复诊;避免接触可能过敏原;不用地毯,不养动物"
  }
}
2026-08-10 11:42:31,679 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-01-10]
2026-08-10 11:42:31,681 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1450843, prompt_len=1482
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共35行）
["门诊病历", "科室:呼吸与危重症医学科", "门", "联系人", "性别:女", "年龄:62岁", "婚姻状况:其他", "2024-01-10 10:27 初诊记录", "主诉:发作性喘息12年余", "现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年", "余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现", "气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行", "听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并", "规律使用信必可320ug bid后症状缓解。近日活动后气促再发,否认喘", "鸣音。无发热、胸痛。", "既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。", "既往病史:", "1.2022.12.10肝囊肿,持续;", "2.2023.10.31鼻窦炎,持续;", "3.2023.10.31双肺良性小结节,持续;", "4.2023.11.03-2023.12.13,肺肺部感染;", "一年内支气管哮喘急性发作病史:", "12023.11.03-2023.11.08,支气管哮喘急性发作,8mg、4mg甲泼尼龙qd", "各服用3天;", "22023.12.13-2023.12.15,支气管哮喘急性发作,4mg甲泼尼龙片qd,服用", "3天。", "一年内合并用药:", "1.左氧氟沙星片,2023.11.03-2023.12.01,0.5g,qd,po,用于治疗肺部感染", "2.甲泼尼龙片,2023.11.03-2023.11.05,8mg,qd,po,用于治疗支气管哮喘急", "性发作。", "3.甲泼尼龙片,2023.11.06-2023.11.08,4mg,qd,po,用于治疗支气管哮喘急", "性发作。", "4.孟鲁司特钠片,2023.11.03-2023.11.12,10mg,qn,po,用于治疗支气管哮喘", "急性发作。", "第1页"]

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
2026-08-10 11:42:44,648 INFO     29 [qwen-vl-text] coord API raw response (len=2299):
[
	{"text": "门诊病历", "bbox": [420, 20, 590, 41]},
	{"text": "科室:呼吸与危重症医学科", "bbox": [104, 51, 338, 67]},
	{"text": "门", "bbox": [512, 51, 532, 67]},
	{"text": "联系人", "bbox": [512, 78, 566, 94]},
	{"text": "性别:女", "bbox": [105, 105, 175, 121]},
	{"text": "年龄:62岁", "bbox": [512, 105, 603, 121]},
	{"text": "婚姻状况:其他", "bbox": [666, 105, 795, 121]},
	{"text": "2024-01-10 10:27 初诊记录", "bbox": [101, 149, 379, 166]},
	{"text": "主诉:发作性喘息12年余", "bbox": [101, 173, 400, 191]},
	{"text": "现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年", "bbox": [100, 198, 911, 217]},
	{"text": "余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现", "bbox": [203, 223, 911, 242]},
	{"text": "气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行", "bbox": [203, 248, 911, 267]},
	{"text": "听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并", "bbox": [203, 273, 911, 292]},
	{"text": "规律使用信必可320ug bid后症状缓解。近日活动后气促再发,否认喘", "bbox": [203, 298, 911, 317]},
	{"text": "鸣音。无发热、胸痛。", "bbox": [203, 323, 425, 342]},
	{"text": "既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。", "bbox": [104, 349, 863, 367]},
	{"text": "既往病史:", "bbox": [203, 374, 307, 392]},
	{"text": "1.2022.12.10肝囊肿,持续;", "bbox": [203, 399, 480, 417]},
	{"text": "2.2023.10.31鼻窦炎,持续;", "bbox": [203, 424, 480, 442]},
	{"text": "3.2023.10.31双肺良性小结节,持续;", "bbox": [203, 449, 572, 467]},
	{"text": "4.2023.11.03-2023.12.13,肺肺部感染;", "bbox": [203, 474, 585, 492]},
	{"text": "一年内支气管哮喘急性发作病史:", "bbox": [203, 499, 539, 517]},
	{"text": "12023.11.03-2023.11.08,支气管哮喘急性发作,8mg、4mg甲泼尼龙qd", "bbox": [203, 523, 911, 542]},
	{"text": "各服用3天;", "bbox": [203, 548, 328, 567]},
	{"text": "22023.12.13-2023.12.15,支气管哮喘急性发作,4mg甲泼尼龙片qd,服用", "bbox": [203, 573, 909, 592]},
	{"text": "3天。", "bbox": [203, 598, 255, 616]},
	{"text": "一年内合并用药:", "bbox": [203, 623, 377, 642]},
	{"text": "1.左氧氟沙星片,2023.11.03-2023.12.01,0.5g,qd,po,用于治疗肺部感染", "bbox": [203, 649, 910, 667]},
	{"text": "2.甲泼尼龙片,2023.11.03-2023.11.05,8mg,qd,po,用于治疗支气管哮喘急", "bbox": [203, 673, 909, 692]},
	{"text": "性发作。", "bbox": [203, 698, 285, 716]},
	{"text": "3.甲泼尼龙片,2023.11.06-2023.11.08,4mg,qd,po,用于治疗支气管哮喘急", "bbox": [203, 723, 909, 742]},
	{"text": "性发作。", "bbox": [203, 748, 285, 766]},
	{"text": "4.孟鲁司特钠片,2023.11.03-2023.11.12,10mg,qn,po,用于治疗支气管哮喘", "bbox": [203, 773, 909, 792]},
	{"text": "急性发作。", "bbox": [203, 798, 308, 817]},
	{"text": "第1页", "bbox": [475, 832, 540, 849]}
]
2026-08-10 11:42:44,648 INFO     29 [qwen-vl-text] coord API: raw_items=35, valid_items=35, elapsed=13.0s
2026-08-10 11:42:44,648 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[420, 20, 590, 41]
2026-08-10 11:42:44,648 INFO     29 [qwen-vl-text] coord item[1]: text=科室:呼吸与危重症医学科, bbox=[104, 51, 338, 67]
2026-08-10 11:42:44,648 INFO     29 [qwen-vl-text] coord item[2]: text=门, bbox=[512, 51, 532, 67]
2026-08-10 11:42:44,648 INFO     29 [qwen-vl-text] coord item[3]: text=联系人, bbox=[512, 78, 566, 94]
2026-08-10 11:42:44,649 INFO     29 [qwen-vl-text] coord item[4]: text=性别:女, bbox=[105, 105, 175, 121]
2026-08-10 11:42:44,649 INFO     29 [qwen-vl-text] coord item[5]: text=年龄:62岁, bbox=[512, 105, 603, 121]
2026-08-10 11:42:44,649 INFO     29 [qwen-vl-text] coord item[6]: text=婚姻状况:其他, bbox=[666, 105, 795, 121]
2026-08-10 11:42:44,649 INFO     29 [qwen-vl-text] coord item[7]: text=2024-01-10 10:27 初诊记录, bbox=[101, 149, 379, 166]
2026-08-10 11:42:44,649 INFO     29 [qwen-vl-text] coord item[8]: text=主诉:发作性喘息12年余, bbox=[101, 173, 400, 191]
2026-08-10 11:42:44,649 INFO     29 [qwen-vl-text] coord item[9]: text=现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年, bbox=[100, 198, 911, 217]
2026-08-10 11:42:44,649 INFO     29 [qwen-vl-text] coord item[10]: text=余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现, bbox=[203, 223, 911, 242]
2026-08-10 11:42:44,649 INFO     29 [qwen-vl-text] coord item[11]: text=气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行, bbox=[203, 248, 911, 267]
2026-08-10 11:42:44,649 INFO     29 [qwen-vl-text] coord item[12]: text=听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并, bbox=[203, 273, 911, 292]
2026-08-10 11:42:44,649 INFO     29 [qwen-vl-text] coord item[13]: text=规律使用信必可320ug bid后症状缓解。近日活动后气促再发,否认喘, bbox=[203, 298, 911, 317]
2026-08-10 11:42:44,649 INFO     29 [qwen-vl-text] coord item[14]: text=鸣音。无发热、胸痛。, bbox=[203, 323, 425, 342]
2026-08-10 11:42:44,649 INFO     29 [qwen-vl-text] coord item[15]: text=既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。, bbox=[104, 349, 863, 367]
2026-08-10 11:42:44,649 INFO     29 [qwen-vl-text] coord item[16]: text=既往病史:, bbox=[203, 374, 307, 392]
2026-08-10 11:42:44,649 INFO     29 [qwen-vl-text] coord item[17]: text=1.2022.12.10肝囊肿,持续;, bbox=[203, 399, 480, 417]
2026-08-10 11:42:44,649 INFO     29 [qwen-vl-text] coord item[18]: text=2.2023.10.31鼻窦炎,持续;, bbox=[203, 424, 480, 442]
2026-08-10 11:42:44,649 INFO     29 [qwen-vl-text] coord item[19]: text=3.2023.10.31双肺良性小结节,持续;, bbox=[203, 449, 572, 467]
2026-08-10 11:42:44,649 INFO     29 [qwen-vl-text] coord item[20]: text=4.2023.11.03-2023.12.13,肺肺部感染;, bbox=[203, 474, 585, 492]
2026-08-10 11:42:44,649 INFO     29 [qwen-vl-text] coord item[21]: text=一年内支气管哮喘急性发作病史:, bbox=[203, 499, 539, 517]
2026-08-10 11:42:44,649 INFO     29 [qwen-vl-text] coord item[22]: text=12023.11.03-2023.11.08,支气管哮喘急性发作,8mg、4mg甲泼尼龙qd, bbox=[203, 523, 911, 542]
2026-08-10 11:42:44,650 INFO     29 [qwen-vl-text] coord item[23]: text=各服用3天;, bbox=[203, 548, 328, 567]
2026-08-10 11:42:44,650 INFO     29 [qwen-vl-text] coord item[24]: text=22023.12.13-2023.12.15,支气管哮喘急性发作,4mg甲泼尼龙片qd,服用, bbox=[203, 573, 909, 592]
2026-08-10 11:42:44,650 INFO     29 [qwen-vl-text] coord item[25]: text=3天。, bbox=[203, 598, 255, 616]
2026-08-10 11:42:44,650 INFO     29 [qwen-vl-text] coord item[26]: text=一年内合并用药:, bbox=[203, 623, 377, 642]
2026-08-10 11:42:44,650 INFO     29 [qwen-vl-text] coord item[27]: text=1.左氧氟沙星片,2023.11.03-2023.12.01,0.5g,qd,po,用于治疗肺部感染, bbox=[203, 649, 910, 667]
2026-08-10 11:42:44,650 INFO     29 [qwen-vl-text] coord item[28]: text=2.甲泼尼龙片,2023.11.03-2023.11.05,8mg,qd,po,用于治疗支气管哮喘急, bbox=[203, 673, 909, 692]
2026-08-10 11:42:44,650 INFO     29 [qwen-vl-text] coord item[29]: text=性发作。, bbox=[203, 698, 285, 716]
2026-08-10 11:42:44,650 INFO     29 [qwen-vl-text] coord item[30]: text=3.甲泼尼龙片,2023.11.06-2023.11.08,4mg,qd,po,用于治疗支气管哮喘急, bbox=[203, 723, 909, 742]
2026-08-10 11:42:44,650 INFO     29 [qwen-vl-text] coord item[31]: text=性发作。, bbox=[203, 748, 285, 766]
2026-08-10 11:42:44,650 INFO     29 [qwen-vl-text] coord item[32]: text=4.孟鲁司特钠片,2023.11.03-2023.11.12,10mg,qn,po,用于治疗支气管哮喘, bbox=[203, 773, 909, 792]
2026-08-10 11:42:44,650 INFO     29 [qwen-vl-text] coord item[33]: text=急性发作。, bbox=[203, 798, 308, 817]
2026-08-10 11:42:44,650 INFO     29 [qwen-vl-text] coord item[34]: text=第1页, bbox=[475, 832, 540, 849]
2026-08-10 11:42:44,651 INFO     29 [qwen-vl-text] page=0 — 35/35 coords, api_time=13.0s
2026-08-10 11:42:44,654 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1406002, prompt_len=1525
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共35行）
["门诊病历", "科室:呼吸与危重症医学科", "姓名", "性别:女", "年龄:62岁", "婚姻状况:其他", "联系方式", "2024-01-10 10:27 初诊记录", "5.桉柠蒎肠溶软胶囊,2023.11.03-2023.11.15,0.3g,tid,po,用于治疗肺部感", "染。", "7.甲泼尼龙片,2023.12.13-2023.12.15,4mg,qd,po,用于治疗支气管哮喘急", "性发作。", "8.布地奈德福莫特罗粉吸入剂,2022.11.27开始,持续使用,", "320ug,bid,经口腔吸入,用于控制哮喘。", "过敏史:否认食物、药物过敏史。", "体格检查 收缩压（mmHg）:107;舒张压（mmHg）:75", "其他体格检查:身高:153cm,体重:48.5kg,", "09:50进行生命体征测量:体温:36.4℃,血压:107/75mmHg,呼吸:19", "次/分,脉搏:78次/分;", "查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见", "皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅", "大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。", "耳廓正常无畸形,外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无", "鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿", "大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中", "肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动", "正常,双肺呼吸音粗,未闻及干湿罗音。心律齐。双下肢无水肿。心率", "78次/分,心音正常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛", "反跳痛,无液波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触", "及,肾脏未触及,Murphy征阴性,移动性浊音阴性,肠鸣音正常。外生殖", "器未查、肛门直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无", "异常,其他无异常。", "第2页", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-10 11:42:58,903 INFO     29 [qwen-vl-text] coord API raw response (len=2343):
[
	{"text": "门诊病历", "bbox": [428, 18, 594, 35]},
	{"text": "科室:呼吸与危重症医学科", "bbox": [111, 44, 346, 61]},
	{"text": "姓名", "bbox": [111, 72, 154, 89]},
	{"text": "性别:女", "bbox": [111, 100, 184, 117]},
	{"text": "年龄:62岁", "bbox": [518, 100, 609, 117]},
	{"text": "婚姻状况:其他", "bbox": [670, 100, 797, 117]},
	{"text": "联系方式", "bbox": [518, 72, 597, 89]},
	{"text": "2024-01-10 10:27 初诊记录", "bbox": [109, 145, 389, 163]},
	{"text": "5.桉柠蒎肠溶软胶囊,2023.11.03-2023.11.15,0.3g,tid,po,用于治疗肺部感", "bbox": [212, 169, 911, 189]},
	{"text": "染。", "bbox": [212, 196, 247, 213]},
	{"text": "7.甲泼尼龙片,2023.12.13-2023.12.15,4mg,qd,po,用于治疗支气管哮喘急", "bbox": [212, 221, 910, 241]},
	{"text": "性发作。", "bbox": [212, 248, 295, 265]},
	{"text": "8.布地奈德福莫特罗粉吸入剂,2022.11.27开始,持续使用,", "bbox": [212, 272, 778, 291]},
	{"text": "320ug,bid,经口腔吸入,用于控制哮喘。", "bbox": [212, 298, 601, 318]},
	{"text": "过敏史:否认食物、药物过敏史。", "bbox": [114, 351, 460, 369]},
	{"text": "体格检查 收缩压（mmHg）:107;舒张压（mmHg）:75", "bbox": [114, 375, 656, 394]},
	{"text": "其他体格检查:身高:153cm,体重:48.5kg,", "bbox": [214, 400, 656, 419]},
	{"text": "09:50进行生命体征测量:体温:36.4℃,血压:107/75mmHg,呼吸:19", "bbox": [214, 425, 913, 444]},
	{"text": "次/分,脉搏:78次/分;", "bbox": [214, 450, 450, 469]},
	{"text": "查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见", "bbox": [214, 475, 911, 494]},
	{"text": "皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅", "bbox": [214, 500, 911, 519]},
	{"text": "大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。", "bbox": [214, 525, 900, 544]},
	{"text": "耳廓正常无畸形,外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无", "bbox": [214, 550, 911, 569]},
	{"text": "鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿", "bbox": [214, 575, 911, 594]},
	{"text": "大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中", "bbox": [214, 600, 911, 619]},
	{"text": "肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动", "bbox": [214, 625, 911, 644]},
	{"text": "正常,双肺呼吸音粗,未闻及干湿罗音。心律齐。双下肢无水肿。心率", "bbox": [214, 650, 911, 669]},
	{"text": "78次/分,心音正常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛", "bbox": [214, 675, 911, 694]},
	{"text": "反跳痛,无液波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触", "bbox": [214, 700, 911, 719]},
	{"text": "及,肾脏未触及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖", "bbox": [214, 725, 911, 744]},
	{"text": "器未查、肛门直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无", "bbox": [214, 750, 911, 769]},
	{"text": "异常,其他无异常。", "bbox": [214, 775, 420, 794]},
	{"text": "第2页", "bbox": [485, 835, 548, 852]},
	{"text": "CS 扫描全能王", "bbox": [861, 958, 977, 974]},
	{"text": "3亿人都在用的扫描App", "bbox": [861, 977, 976, 986]}
]
2026-08-10 11:42:58,908 INFO     29 [qwen-vl-text] coord API: raw_items=35, valid_items=35, elapsed=14.2s
2026-08-10 11:42:58,908 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[428, 18, 594, 35]
2026-08-10 11:42:58,908 INFO     29 [qwen-vl-text] coord item[1]: text=科室:呼吸与危重症医学科, bbox=[111, 44, 346, 61]
2026-08-10 11:42:58,908 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[111, 72, 154, 89]
2026-08-10 11:42:58,908 INFO     29 [qwen-vl-text] coord item[3]: text=性别:女, bbox=[111, 100, 184, 117]
2026-08-10 11:42:58,908 INFO     29 [qwen-vl-text] coord item[4]: text=年龄:62岁, bbox=[518, 100, 609, 117]
2026-08-10 11:42:58,908 INFO     29 [qwen-vl-text] coord item[5]: text=婚姻状况:其他, bbox=[670, 100, 797, 117]
2026-08-10 11:42:58,908 INFO     29 [qwen-vl-text] coord item[6]: text=联系方式, bbox=[518, 72, 597, 89]
2026-08-10 11:42:58,908 INFO     29 [qwen-vl-text] coord item[7]: text=2024-01-10 10:27 初诊记录, bbox=[109, 145, 389, 163]
2026-08-10 11:42:58,908 INFO     29 [qwen-vl-text] coord item[8]: text=5.桉柠蒎肠溶软胶囊,2023.11.03-2023.11.15,0.3g,tid,po,用于治疗肺部感, bbox=[212, 169, 911, 189]
2026-08-10 11:42:58,908 INFO     29 [qwen-vl-text] coord item[9]: text=染。, bbox=[212, 196, 247, 213]
2026-08-10 11:42:58,908 INFO     29 [qwen-vl-text] coord item[10]: text=7.甲泼尼龙片,2023.12.13-2023.12.15,4mg,qd,po,用于治疗支气管哮喘急, bbox=[212, 221, 910, 241]
2026-08-10 11:42:58,908 INFO     29 [qwen-vl-text] coord item[11]: text=性发作。, bbox=[212, 248, 295, 265]
2026-08-10 11:42:58,908 INFO     29 [qwen-vl-text] coord item[12]: text=8.布地奈德福莫特罗粉吸入剂,2022.11.27开始,持续使用,, bbox=[212, 272, 778, 291]
2026-08-10 11:42:58,908 INFO     29 [qwen-vl-text] coord item[13]: text=320ug,bid,经口腔吸入,用于控制哮喘。, bbox=[212, 298, 601, 318]
2026-08-10 11:42:58,909 INFO     29 [qwen-vl-text] coord item[14]: text=过敏史:否认食物、药物过敏史。, bbox=[114, 351, 460, 369]
2026-08-10 11:42:58,909 INFO     29 [qwen-vl-text] coord item[15]: text=体格检查 收缩压（mmHg）:107;舒张压（mmHg）:75, bbox=[114, 375, 656, 394]
2026-08-10 11:42:58,909 INFO     29 [qwen-vl-text] coord item[16]: text=其他体格检查:身高:153cm,体重:48.5kg,, bbox=[214, 400, 656, 419]
2026-08-10 11:42:58,909 INFO     29 [qwen-vl-text] coord item[17]: text=09:50进行生命体征测量:体温:36.4℃,血压:107/75mmHg,呼吸:19, bbox=[214, 425, 913, 444]
2026-08-10 11:42:58,909 INFO     29 [qwen-vl-text] coord item[18]: text=次/分,脉搏:78次/分;, bbox=[214, 450, 450, 469]
2026-08-10 11:42:58,909 INFO     29 [qwen-vl-text] coord item[19]: text=查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见, bbox=[214, 475, 911, 494]
2026-08-10 11:42:58,909 INFO     29 [qwen-vl-text] coord item[20]: text=皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅, bbox=[214, 500, 911, 519]
2026-08-10 11:42:58,909 INFO     29 [qwen-vl-text] coord item[21]: text=大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。, bbox=[214, 525, 900, 544]
2026-08-10 11:42:58,909 INFO     29 [qwen-vl-text] coord item[22]: text=耳廓正常无畸形,外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无, bbox=[214, 550, 911, 569]
2026-08-10 11:42:58,909 INFO     29 [qwen-vl-text] coord item[23]: text=鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿, bbox=[214, 575, 911, 594]
2026-08-10 11:42:58,909 INFO     29 [qwen-vl-text] coord item[24]: text=大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中, bbox=[214, 600, 911, 619]
2026-08-10 11:42:58,909 INFO     29 [qwen-vl-text] coord item[25]: text=肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动, bbox=[214, 625, 911, 644]
2026-08-10 11:42:58,909 INFO     29 [qwen-vl-text] coord item[26]: text=正常,双肺呼吸音粗,未闻及干湿罗音。心律齐。双下肢无水肿。心率, bbox=[214, 650, 911, 669]
2026-08-10 11:42:58,909 INFO     29 [qwen-vl-text] coord item[27]: text=78次/分,心音正常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛, bbox=[214, 675, 911, 694]
2026-08-10 11:42:58,909 INFO     29 [qwen-vl-text] coord item[28]: text=反跳痛,无液波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触, bbox=[214, 700, 911, 719]
2026-08-10 11:42:58,909 INFO     29 [qwen-vl-text] coord item[29]: text=及,肾脏未触及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖, bbox=[214, 725, 911, 744]
2026-08-10 11:42:58,909 INFO     29 [qwen-vl-text] coord item[30]: text=器未查、肛门直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无, bbox=[214, 750, 911, 769]
2026-08-10 11:42:58,909 INFO     29 [qwen-vl-text] coord item[31]: text=异常,其他无异常。, bbox=[214, 775, 420, 794]
2026-08-10 11:42:58,909 INFO     29 [qwen-vl-text] coord item[32]: text=第2页, bbox=[485, 835, 548, 852]
2026-08-10 11:42:58,909 INFO     29 [qwen-vl-text] coord item[33]: text=CS 扫描全能王, bbox=[861, 958, 977, 974]
2026-08-10 11:42:58,909 INFO     29 [qwen-vl-text] coord item[34]: text=3亿人都在用的扫描App, bbox=[861, 977, 976, 986]
2026-08-10 11:42:58,910 INFO     29 [qwen-vl-text] page=1 — 35/35 coords, api_time=14.2s
2026-08-10 11:42:58,917 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1645213, prompt_len=1562
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共37行）
["科室:呼吸与危重症医学科", "姓名:", "性别:女", "门诊", "联系方式", "596", "年龄:62岁", "婚姻状况:其他", "2024-01-10 10:27 初诊记录", "检验检查:阅片见双肺轻度支气管扩张,未见明显急性炎症病灶,余肺基本同前", "(正式报告为准)", "初步诊断:1.鼻窦炎;2.支气管哮喘;", "处理:药品:", "(省采3)硫酸沙丁胺醇吸入气雾剂200揿(100μg/揿)/瓶(1【瓶】) sig:", "(200【揿】)吸入pm(需要时);", "检查:心脏电生理:心电图(十二导联心电图);CT检查:副鼻窦平扫;", "使用螺旋扫描加收;普放:DR胸部正侧位片*(2);呼吸专科检查:支气管", "舒张试验、流速容量曲线;", "检验:凝血四项、肾功能六项+肝功能八项+血脂六项*+电解质六项+空", "腹血糖(门诊使用)+肝酶学补充7项+心肌损伤六项、血常规5分类、尿", "常规加化学分析、感染八项", "治疗:静脉采血", "根据患者病情,认为患者基本符合“评价SHR-1905注射液在重度未", "控制哮喘患者中的有效性及安全性-多中心、随机、双盲、安慰剂对照", "平行设计II期临床研究(SHR-1905-201)”的筛选要求,2024.01.10 09:15", "生向患者__及其家属详细介绍该试验目的、试验设计、受试", "者风险及受益、受试者义务及研究者义务等。根据方案(版本号:2.0,", "版本日期:2022年8月31日)要求,筛选期所有受试者均进行吸入支气", "管扩张剂前后肺功能检查,若受试者无法提供筛选前一年内气道可逆", "性检测报告(吸入沙丁胺醇后FEV1增加≥12%且FEV1绝对值增加≥", "200mL),则筛选期肺功能检查需要满足吸入沙丁胺醇后FEV1增加≥", "12%且FEV1绝对值增加≥200mL。符合要求后才可以入组,受试者表", "示同意。患者.__及其家属表示已充分了解以上告知内容,同意参加", "该临床试验,", "医生与患者__于2024.01.10 09:47同时签署了知", "情同意书(版本号:2.0,版本日期:2022年08月31日),一式两份,一份", "第3页"]

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
2026-08-10 11:43:12,035 INFO     29 [qwen-vl-text] coord API raw response (len=2449):
[
	{"text": "科室:呼吸与危重症医学科", "bbox": [88, 35, 327, 53]},
	{"text": "姓名:", "bbox": [88, 64, 115, 82]},
	{"text": "性别:女", "bbox": [88, 92, 161, 109]},
	{"text": "门诊", "bbox": [503, 35, 567, 53]},
	{"text": "联系方式", "bbox": [503, 64, 585, 81]},
	{"text": "596", "bbox": [670, 69, 704, 80]},
	{"text": "年龄:62岁", "bbox": [503, 92, 596, 109]},
	{"text": "婚姻状况:其他", "bbox": [659, 92, 788, 109]},
	{"text": "2024-01-10 10:27 初诊记录", "bbox": [84, 137, 368, 155]},
	{"text": "检验检查:阅片见双肺轻度支气管扩张,未见明显急性炎症病灶,余肺基本同前", "bbox": [84, 163, 881, 181]},
	{"text": "(正式报告为准)", "bbox": [199, 189, 367, 207]},
	{"text": "初步诊断:1.鼻窦炎;2.支气管哮喘;", "bbox": [84, 215, 446, 234]},
	{"text": "处理:药品:", "bbox": [84, 242, 243, 260]},
	{"text": "(省采3)硫酸沙丁胺醇吸入气雾剂200揿(100μg/揿)/瓶(1【瓶】) sig:", "bbox": [192, 268, 906, 287]},
	{"text": "(200【揿】)吸入pm(需要时);", "bbox": [189, 294, 546, 313]},
	{"text": "检查:心脏电生理:心电图(十二导联心电图);CT检查:副鼻窦平扫;", "bbox": [189, 320, 890, 339]},
	{"text": "使用螺旋扫描加收;普放:DR胸部正侧位片*(2);呼吸专科检查:支气管", "bbox": [189, 346, 904, 365]},
	{"text": "舒张试验、流速容量曲线;", "bbox": [189, 372, 460, 390]},
	{"text": "检验:凝血四项、肾功能六项+肝功能八项+血脂六项*+电解质六项+空", "bbox": [189, 398, 899, 416]},
	{"text": "腹血糖(门诊使用)+肝酶学补充7项+心肌损伤六项、血常规5分类、尿", "bbox": [189, 423, 904, 442]},
	{"text": "常规加化学分析、感染八项", "bbox": [189, 449, 474, 467]},
	{"text": "治疗:静脉采血", "bbox": [189, 474, 338, 492]},
	{"text": "根据患者病情,认为患者基本符合“评价SHR-1905注射液在重度未", "bbox": [187, 500, 904, 518]},
	{"text": "控制哮喘患者中的有效性及安全性-多中心、随机、双盲、安慰剂对照", "bbox": [187, 525, 904, 544]},
	{"text": "平行设计II期临床研究(SHR-1905-201)”的筛选要求,2024.01.10 09:15", "bbox": [187, 551, 904, 570]},
	{"text": "生向患者__及其家属详细介绍该试验目的、试验设计、受试", "bbox": [238, 577, 904, 595]},
	{"text": "者风险及受益、受试者义务及研究者义务等。根据方案(版本号:2.0,", "bbox": [187, 603, 890, 621]},
	{"text": "版本日期:2022年8月31日)要求,筛选期所有受试者均进行吸入支气", "bbox": [187, 629, 904, 647]},
	{"text": "管扩张剂前后肺功能检查,若受试者无法提供筛选前一年内气道可逆", "bbox": [187, 654, 899, 673]},
	{"text": "性检测报告(吸入沙丁胺醇后FEV1增加≥12%且FEV1绝对值增加≥", "bbox": [187, 680, 902, 699]},
	{"text": "200mL),则筛选期肺功能检查需要满足吸入沙丁胺醇后FEV1增加≥", "bbox": [185, 706, 880, 725]},
	{"text": "12%且FEV1绝对值增加≥200mL。符合要求后才可以入组,受试者表", "bbox": [187, 732, 904, 750]},
	{"text": "示同意。患者.__及其家属表示已充分了解以上告知内容,同意参加", "bbox": [185, 758, 904, 776]},
	{"text": "该临床试验,", "bbox": [185, 783, 314, 802]},
	{"text": "医生与患者__于2024.01.10 09:47同时签署了知", "bbox": [364, 783, 904, 802]},
	{"text": "情同意书(版本号:2.0,版本日期:2022年08月31日),一式两份,一份", "bbox": [185, 809, 904, 828]},
	{"text": "第3页", "bbox": [462, 843, 526, 861]}
]
2026-08-10 11:43:12,035 INFO     29 [qwen-vl-text] coord API: raw_items=37, valid_items=37, elapsed=13.1s
2026-08-10 11:43:12,035 INFO     29 [qwen-vl-text] coord item[0]: text=科室:呼吸与危重症医学科, bbox=[88, 35, 327, 53]
2026-08-10 11:43:12,035 INFO     29 [qwen-vl-text] coord item[1]: text=姓名:, bbox=[88, 64, 115, 82]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[2]: text=性别:女, bbox=[88, 92, 161, 109]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[3]: text=门诊, bbox=[503, 35, 567, 53]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[4]: text=联系方式, bbox=[503, 64, 585, 81]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[5]: text=596, bbox=[670, 69, 704, 80]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:62岁, bbox=[503, 92, 596, 109]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[7]: text=婚姻状况:其他, bbox=[659, 92, 788, 109]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[8]: text=2024-01-10 10:27 初诊记录, bbox=[84, 137, 368, 155]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[9]: text=检验检查:阅片见双肺轻度支气管扩张,未见明显急性炎症病灶,余肺基本同前, bbox=[84, 163, 881, 181]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[10]: text=(正式报告为准), bbox=[199, 189, 367, 207]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[11]: text=初步诊断:1.鼻窦炎;2.支气管哮喘;, bbox=[84, 215, 446, 234]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[12]: text=处理:药品:, bbox=[84, 242, 243, 260]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[13]: text=(省采3)硫酸沙丁胺醇吸入气雾剂200揿(100μg/揿)/瓶(1【瓶】) sig:, bbox=[192, 268, 906, 287]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[14]: text=(200【揿】)吸入pm(需要时);, bbox=[189, 294, 546, 313]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[15]: text=检查:心脏电生理:心电图(十二导联心电图);CT检查:副鼻窦平扫;, bbox=[189, 320, 890, 339]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[16]: text=使用螺旋扫描加收;普放:DR胸部正侧位片*(2);呼吸专科检查:支气管, bbox=[189, 346, 904, 365]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[17]: text=舒张试验、流速容量曲线;, bbox=[189, 372, 460, 390]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[18]: text=检验:凝血四项、肾功能六项+肝功能八项+血脂六项*+电解质六项+空, bbox=[189, 398, 899, 416]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[19]: text=腹血糖(门诊使用)+肝酶学补充7项+心肌损伤六项、血常规5分类、尿, bbox=[189, 423, 904, 442]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[20]: text=常规加化学分析、感染八项, bbox=[189, 449, 474, 467]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[21]: text=治疗:静脉采血, bbox=[189, 474, 338, 492]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[22]: text=根据患者病情,认为患者基本符合“评价SHR-1905注射液在重度未, bbox=[187, 500, 904, 518]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[23]: text=控制哮喘患者中的有效性及安全性-多中心、随机、双盲、安慰剂对照, bbox=[187, 525, 904, 544]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[24]: text=平行设计II期临床研究(SHR-1905-201)”的筛选要求,2024.01.10 09:15, bbox=[187, 551, 904, 570]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[25]: text=生向患者__及其家属详细介绍该试验目的、试验设计、受试, bbox=[238, 577, 904, 595]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[26]: text=者风险及受益、受试者义务及研究者义务等。根据方案(版本号:2.0,, bbox=[187, 603, 890, 621]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[27]: text=版本日期:2022年8月31日)要求,筛选期所有受试者均进行吸入支气, bbox=[187, 629, 904, 647]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[28]: text=管扩张剂前后肺功能检查,若受试者无法提供筛选前一年内气道可逆, bbox=[187, 654, 899, 673]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[29]: text=性检测报告(吸入沙丁胺醇后FEV1增加≥12%且FEV1绝对值增加≥, bbox=[187, 680, 902, 699]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[30]: text=200mL),则筛选期肺功能检查需要满足吸入沙丁胺醇后FEV1增加≥, bbox=[185, 706, 880, 725]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[31]: text=12%且FEV1绝对值增加≥200mL。符合要求后才可以入组,受试者表, bbox=[187, 732, 904, 750]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[32]: text=示同意。患者.__及其家属表示已充分了解以上告知内容,同意参加, bbox=[185, 758, 904, 776]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[33]: text=该临床试验,, bbox=[185, 783, 314, 802]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[34]: text=医生与患者__于2024.01.10 09:47同时签署了知, bbox=[364, 783, 904, 802]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[35]: text=情同意书(版本号:2.0,版本日期:2022年08月31日),一式两份,一份, bbox=[185, 809, 904, 828]
2026-08-10 11:43:12,036 INFO     29 [qwen-vl-text] coord item[36]: text=第3页, bbox=[462, 843, 526, 861]
2026-08-10 11:43:12,037 INFO     29 [qwen-vl-text] page=2 — 37/37 coords, api_time=13.1s
2026-08-10 11:43:12,038 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=916763, prompt_len=1120
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共24行）
["门诊病历", "科室:呼吸与危重症医学科", "姓名:", "性别:女", "门诊", "联系方式", "年龄:62岁", "婚姻状况:其他", "2024-01-10 10:27 初诊记录", "交给患者保存,一份保存在研究中心。签署知情同意书后患者进入筛选", "流程,受试者筛选号为CN..", "新增AE:", "1.高尿酸血症,2024.01.10开始,轻度,持续,与研究药物肯定无关,对研", "究药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。", "2.高脂血症,2024.01.10开始,轻度,持续,与研究药物肯定无关,对研究", "药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。", "3.白细胞计数降低,2024.01.10开始,轻度,持续,与研究药物肯定无关", "对研究药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。此项", "指标与患者临床症状不符,考虑让其一周内复测。", "规律使用吸入药物,用后漱口,定期复诊;避免接触可能过敏原;不用地", "毯,不养动物", "医师签", "门诊病历专用", "※提醒:复诊时,请携带本病历记录,谢谢!※"]

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
2026-08-10 11:43:20,282 INFO     29 [qwen-vl-text] coord API raw response (len=1482):
[
	{"text": "门诊病历", "bbox": [396, 45, 571, 68]},
	{"text": "科室:呼吸与危重症医学科", "bbox": [68, 76, 310, 93]},
	{"text": "姓名:", "bbox": [70, 105, 117, 121]},
	{"text": "性别:女", "bbox": [70, 132, 142, 148]},
	{"text": "门诊", "bbox": [490, 77, 541, 94]},
	{"text": "联系方式", "bbox": [490, 105, 562, 121]},
	{"text": "年龄:62岁", "bbox": [490, 133, 584, 148]},
	{"text": "婚姻状况:其他", "bbox": [649, 133, 779, 148]},
	{"text": "2024-01-10 10:27 初诊记录", "bbox": [65, 176, 354, 194]},
	{"text": "交给患者保存,一份保存在研究中心。签署知情同意书后患者进入筛选", "bbox": [170, 202, 899, 220]},
	{"text": "流程,受试者筛选号为CN..", "bbox": [170, 228, 471, 246]},
	{"text": "新增AE:", "bbox": [170, 254, 264, 272]},
	{"text": "1.高尿酸血症,2024.01.10开始,轻度,持续,与研究药物肯定无关,对研", "bbox": [170, 279, 899, 297]},
	{"text": "究药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。", "bbox": [170, 304, 827, 323]},
	{"text": "2.高脂血症,2024.01.10开始,轻度,持续,与研究药物肯定无关,对研究", "bbox": [170, 330, 899, 348]},
	{"text": "药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。", "bbox": [170, 356, 804, 374]},
	{"text": "3.白细胞计数降低,2024.01.10开始,轻度,持续,与研究药物肯定无关", "bbox": [170, 381, 899, 399]},
	{"text": "对研究药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。此项", "bbox": [170, 407, 899, 425]},
	{"text": "指标与患者临床症状不符,考虑让其一周内复测。", "bbox": [170, 433, 690, 451]},
	{"text": "规律使用吸入药物,用后漱口,定期复诊;避免接触可能过敏原;不用地", "bbox": [170, 458, 899, 477]},
	{"text": "毯,不养动物", "bbox": [170, 484, 317, 502]},
	{"text": "医师签", "bbox": [652, 523, 755, 540]},
	{"text": "门诊病历专用", "bbox": [77, 568, 315, 590]},
	{"text": "※提醒:复诊时,请携带本病历记录,谢谢!※", "bbox": [70, 646, 583, 664]}
]
2026-08-10 11:43:20,283 INFO     29 [qwen-vl-text] coord API: raw_items=24, valid_items=24, elapsed=8.2s
2026-08-10 11:43:20,283 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[396, 45, 571, 68]
2026-08-10 11:43:20,283 INFO     29 [qwen-vl-text] coord item[1]: text=科室:呼吸与危重症医学科, bbox=[68, 76, 310, 93]
2026-08-10 11:43:20,283 INFO     29 [qwen-vl-text] coord item[2]: text=姓名:, bbox=[70, 105, 117, 121]
2026-08-10 11:43:20,283 INFO     29 [qwen-vl-text] coord item[3]: text=性别:女, bbox=[70, 132, 142, 148]
2026-08-10 11:43:20,283 INFO     29 [qwen-vl-text] coord item[4]: text=门诊, bbox=[490, 77, 541, 94]
2026-08-10 11:43:20,283 INFO     29 [qwen-vl-text] coord item[5]: text=联系方式, bbox=[490, 105, 562, 121]
2026-08-10 11:43:20,283 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:62岁, bbox=[490, 133, 584, 148]
2026-08-10 11:43:20,283 INFO     29 [qwen-vl-text] coord item[7]: text=婚姻状况:其他, bbox=[649, 133, 779, 148]
2026-08-10 11:43:20,283 INFO     29 [qwen-vl-text] coord item[8]: text=2024-01-10 10:27 初诊记录, bbox=[65, 176, 354, 194]
2026-08-10 11:43:20,283 INFO     29 [qwen-vl-text] coord item[9]: text=交给患者保存,一份保存在研究中心。签署知情同意书后患者进入筛选, bbox=[170, 202, 899, 220]
2026-08-10 11:43:20,283 INFO     29 [qwen-vl-text] coord item[10]: text=流程,受试者筛选号为CN.., bbox=[170, 228, 471, 246]
2026-08-10 11:43:20,283 INFO     29 [qwen-vl-text] coord item[11]: text=新增AE:, bbox=[170, 254, 264, 272]
2026-08-10 11:43:20,283 INFO     29 [qwen-vl-text] coord item[12]: text=1.高尿酸血症,2024.01.10开始,轻度,持续,与研究药物肯定无关,对研, bbox=[170, 279, 899, 297]
2026-08-10 11:43:20,283 INFO     29 [qwen-vl-text] coord item[13]: text=究药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。, bbox=[170, 304, 827, 323]
2026-08-10 11:43:20,283 INFO     29 [qwen-vl-text] coord item[14]: text=2.高脂血症,2024.01.10开始,轻度,持续,与研究药物肯定无关,对研究, bbox=[170, 330, 899, 348]
2026-08-10 11:43:20,283 INFO     29 [qwen-vl-text] coord item[15]: text=药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。, bbox=[170, 356, 804, 374]
2026-08-10 11:43:20,283 INFO     29 [qwen-vl-text] coord item[16]: text=3.白细胞计数降低,2024.01.10开始,轻度,持续,与研究药物肯定无关, bbox=[170, 381, 899, 399]
2026-08-10 11:43:20,283 INFO     29 [qwen-vl-text] coord item[17]: text=对研究药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。此项, bbox=[170, 407, 899, 425]
2026-08-10 11:43:20,283 INFO     29 [qwen-vl-text] coord item[18]: text=指标与患者临床症状不符,考虑让其一周内复测。, bbox=[170, 433, 690, 451]
2026-08-10 11:43:20,283 INFO     29 [qwen-vl-text] coord item[19]: text=规律使用吸入药物,用后漱口,定期复诊;避免接触可能过敏原;不用地, bbox=[170, 458, 899, 477]
2026-08-10 11:43:20,283 INFO     29 [qwen-vl-text] coord item[20]: text=毯,不养动物, bbox=[170, 484, 317, 502]
2026-08-10 11:43:20,283 INFO     29 [qwen-vl-text] coord item[21]: text=医师签, bbox=[652, 523, 755, 540]
2026-08-10 11:43:20,283 INFO     29 [qwen-vl-text] coord item[22]: text=门诊病历专用, bbox=[77, 568, 315, 590]
2026-08-10 11:43:20,283 INFO     29 [qwen-vl-text] coord item[23]: text=※提醒:复诊时,请携带本病历记录,谢谢!※, bbox=[70, 646, 583, 664]
2026-08-10 11:43:20,284 INFO     29 [qwen-vl-text] page=3 — 24/24 coords, api_time=8.2s
2026-08-10 11:43:20,284 INFO     29 [qwen-vl-text] new_positions (131):
[[0, 249.89999999999998, 351.05, 16.84, 34.522], [0, 61.879999999999995, 201.10999999999999, 42.942, 56.414], [0, 304.64, 316.53999999999996, 42.942, 56.414], [0, 304.64, 336.77, 65.676, 79.148], [0, 62.474999999999994, 104.125, 88.41, 101.88199999999999], [0, 304.64, 358.78499999999997, 88.41, 101.88199999999999], [0, 396.27, 473.025, 88.41, 101.88199999999999], [0, 60.095, 225.505, 125.458, 139.772], [0, 60.095, 238.0, 145.666, 160.822], [0, 59.5, 542.045, 166.716, 182.714], [0, 120.785, 542.045, 187.766, 203.76399999999998], [0, 120.785, 542.045, 208.816, 224.814], [0, 120.785, 542.045, 229.86599999999999, 245.864], [0, 120.785, 542.045, 250.916, 266.914], [0, 120.785, 252.875, 271.966, 287.964], [0, 61.879999999999995, 513.485, 293.858, 309.014], [0, 120.785, 182.665, 314.908, 330.06399999999996], [0, 120.785, 285.59999999999997, 335.95799999999997, 351.114], [0, 120.785, 285.59999999999997, 357.008, 372.164], [0, 120.785, 340.34, 378.058, 393.214], [0, 120.785, 348.075, 399.108, 414.264], [0, 120.785, 320.705, 420.15799999999996, 435.31399999999996], [0, 120.785, 542.045, 440.366, 456.364], [0, 120.785, 195.16, 461.416, 477.414], [0, 120.785, 540.855, 482.466, 498.464], [0, 120.785, 151.725, 503.51599999999996, 518.672], [0, 120.785, 224.315, 524.566, 540.564], [0, 120.785, 541.4499999999999, 546.458, 561.614], [0, 120.785, 540.855, 566.6659999999999, 582.664], [0, 120.785, 169.575, 587.716, 602.872], [0, 120.785, 540.855, 608.766, 624.764], [0, 120.785, 169.575, 629.816, 644.972], [0, 120.785, 540.855, 650.866, 666.864], [0, 120.785, 183.26, 671.9159999999999, 687.914], [0, 282.625, 321.3, 700.544, 714.858], [1, 254.66, 353.43, 15.155999999999999, 29.47], [1, 66.045, 205.87, 37.048, 51.361999999999995], [1, 66.045, 91.63, 60.623999999999995, 74.938], [1, 66.045, 109.47999999999999, 84.2, 98.514], [1, 308.21, 362.35499999999996, 84.2, 98.514], [1, 398.65, 474.215, 84.2, 98.514], [1, 308.21, 355.215, 60.623999999999995, 74.938], [1, 64.855, 231.45499999999998, 122.08999999999999, 137.246], [1, 126.14, 542.045, 142.298, 159.138], [1, 126.14, 146.965, 165.03199999999998, 179.346], [1, 126.14, 541.4499999999999, 186.082, 202.922], [1, 126.14, 175.525, 208.816, 223.13], [1, 126.14, 462.90999999999997, 229.024, 245.022], [1, 126.14, 357.59499999999997, 250.916, 267.756], [1, 67.83, 273.7, 295.542, 310.698], [1, 67.83, 390.32, 315.75, 331.748], [1, 127.33, 390.32, 336.8, 352.798], [1, 127.33, 543.235, 357.84999999999997, 373.848], [1, 127.33, 267.75, 378.9, 394.89799999999997], [1, 127.33, 542.045, 399.95, 415.948], [1, 127.33, 542.045, 421.0, 436.998], [1, 127.33, 535.5, 442.05, 458.048], [1, 127.33, 542.045, 463.09999999999997, 479.09799999999996], [1, 127.33, 542.045, 484.15, 500.14799999999997], [1, 127.33, 542.045, 505.2, 521.198], [1, 127.33, 542.045, 526.25, 542.2479999999999], [1, 127.33, 542.045, 547.3, 563.298], [1, 127.33, 542.045, 568.35, 584.348], [1, 127.33, 542.045, 589.4, 605.398], [1, 127.33, 542.045, 610.4499999999999, 626.448], [1, 127.33, 542.045, 631.5, 647.4979999999999], [1, 127.33, 249.89999999999998, 652.55, 668.548], [1, 288.575, 326.06, 703.0699999999999, 717.384], [1, 512.295, 581.3149999999999, 806.636, 820.108], [1, 512.295, 580.72, 822.634, 830.212], [2, 52.36, 194.565, 29.47, 44.626], [2, 52.36, 68.425, 53.888, 69.044], [2, 52.36, 95.795, 77.464, 91.77799999999999], [2, 299.28499999999997, 337.365, 29.47, 44.626], [2, 299.28499999999997, 348.075, 53.888, 68.202], [2, 398.65, 418.88, 58.098, 67.36], [2, 299.28499999999997, 354.62, 77.464, 91.77799999999999], [2, 392.10499999999996, 468.85999999999996, 77.464, 91.77799999999999], [2, 49.98, 218.95999999999998, 115.354, 130.51], [2, 49.98, 524.1949999999999, 137.246, 152.402], [2, 118.405, 218.36499999999998, 159.138, 174.29399999999998], [2, 49.98, 265.37, 181.03, 197.028], [2, 49.98, 144.58499999999998, 203.76399999999998, 218.92], [2, 114.24, 539.0699999999999, 225.656, 241.654], [2, 112.455, 324.87, 247.548, 263.546], [2, 112.455, 529.55, 269.44, 285.438], [2, 112.455, 537.88, 291.332, 307.33], [2, 112.455, 273.7, 313.224, 328.38], [2, 112.455, 534.905, 335.116, 350.272], [2, 112.455, 537.88, 356.166, 372.164], [2, 112.455, 282.03, 378.058, 393.214], [2, 112.455, 201.10999999999999, 399.108, 414.264], [2, 111.265, 537.88, 421.0, 436.156], [2, 111.265, 537.88, 442.05, 458.048], [2, 111.265, 537.88, 463.942, 479.94], [2, 141.60999999999999, 537.88, 485.834, 500.99], [2, 111.265, 529.55, 507.726, 522.882], [2, 111.265, 537.88, 529.6179999999999, 544.774], [2, 111.265, 534.905, 550.668, 566.6659999999999], [2, 111.265, 536.6899999999999, 572.56, 588.558], [2, 110.07499999999999, 523.6, 594.452, 610.4499999999999], [2, 111.265, 537.88, 616.3439999999999, 631.5], [2, 110.07499999999999, 537.88, 638.236, 653.3919999999999], [2, 110.07499999999999, 186.82999999999998, 659.286, 675.284], [2, 216.57999999999998, 537.88, 659.286, 675.284], [2, 110.07499999999999, 537.88, 681.178, 697.1759999999999], [2, 274.89, 312.96999999999997, 709.8059999999999, 724.962], [3, 235.61999999999998, 339.745, 37.89, 57.256], [3, 40.46, 184.45, 63.992, 78.306], [3, 41.65, 69.615, 88.41, 101.88199999999999], [3, 41.65, 84.49, 111.14399999999999, 124.616], [3, 291.55, 321.895, 64.834, 79.148], [3, 291.55, 334.39, 88.41, 101.88199999999999], [3, 291.55, 347.47999999999996, 111.98599999999999, 124.616], [3, 386.155, 463.505, 111.98599999999999, 124.616], [3, 38.675, 210.63, 148.192, 163.34799999999998], [3, 101.14999999999999, 534.905, 170.084, 185.23999999999998], [3, 101.14999999999999, 280.245, 191.976, 207.132], [3, 101.14999999999999, 157.07999999999998, 213.868, 229.024], [3, 101.14999999999999, 534.905, 234.91799999999998, 250.07399999999998], [3, 101.14999999999999, 492.065, 255.968, 271.966], [3, 101.14999999999999, 534.905, 277.86, 293.01599999999996], [3, 101.14999999999999, 478.38, 299.752, 314.908], [3, 101.14999999999999, 534.905, 320.80199999999996, 335.95799999999997], [3, 101.14999999999999, 534.905, 342.69399999999996, 357.84999999999997], [3, 101.14999999999999, 410.54999999999995, 364.586, 379.74199999999996], [3, 101.14999999999999, 534.905, 385.63599999999997, 401.63399999999996], [3, 101.14999999999999, 188.61499999999998, 407.52799999999996, 422.68399999999997], [3, 387.94, 449.22499999999997, 440.366, 454.68], [3, 45.815, 187.42499999999998, 478.256, 496.78], [3, 41.65, 346.885, 543.932, 559.088]]
2026-08-10 11:43:20,284 INFO     29 [qwen-vl-text] ═══ DONE ═══ 131 positions, pages=4, time=59.1s
2026-08-10 11:43:20,284 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:43:20,291 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:43:20,291 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:43:20,291 INFO     29 [qwen-vl-text] positions(86): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:43:20,291 INFO     29 [qwen-vl-text] page grouping: [4, 5, 6], lines per page: [34, 37, 15]
2026-08-10 11:43:20,983 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:43:21,889 INFO     29 [qwen-vl-text] page=5, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:43:22,071 INFO     29 [qwen-vl-text] page=6, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:43:22,074 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1738
2026-08-10 11:43:22,075 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:43:22,075 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 133, \"bbox_end\": 218, \"encounter_dates\": [\"2024-03-21\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊病历\n科室:呼吸与危重症医学科\n姓名:\n性别:女\n门诊\n联系方\n年龄:62岁\n婚姻状况:其他\n2024-03-21 08:40 初诊记录\n主诉:SHR-1905-201 试验复筛\n现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年\n余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现\n气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行\n听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并\n规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可\n320ug bid,近日活动后气促再发,否认喘鸣音。无发热、胸痛。\n2024.01.10参加SHR-1905-201临床试验,因白细胞计数<3.0*10^9/L符\n合排除标准第12条筛败,于2024.03.01血液科就诊,无特殊处理,\n2024.03.06进行SHR-1905-201试验二次知情。受试者今日返院完成V3\n访视。\n既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。\n既往病史:\n1.2022.12.10肝囊肿,持续;\n2.2023.10.31鼻窦炎,持续;\n3.2023.10.31双肺良性小结节,持续;\n4.2023.11.03-2023.12.13,肺肺部感染;\n5.2024.03.01开始,白细胞数降低1级;\n6.2024.01.10开始,高脂蛋白a血症,\n过敏史:否认食物、药物过敏史。\n体格检查收缩压(mmHg):113;舒张压(mmHg):76\n其他体格检查:09:37进行生命体征测量:体温:36.5℃,血压:\n113/76mmHg,呼吸:18次/分,脉搏:98次/分;\n查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见\n第1页\n科室:呼吸与危重症医学科\n姓名\n性别:女\n门诊\n联系方\n年龄:62岁\n婚姻状况:其他\n2024-03-21 08:40 初诊记录\n皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅\n大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。\n耳廓正常无畸形,外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无\n鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿\n大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中\n肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动\n正常,双肺呼吸音粗,未闻及干湿罗音。心律齐。双下肢无水肿。心音正\n常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛、反跳痛,无液\n波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触及,肾脏未触\n及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖器未查、肛门\n直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无异常,其他无\n异常。.\n检验检查:无\n初步诊断:支气管哮喘\n处理:\nCM 跟踪:\n1、布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,\n320ug,bid,经口腔吸入,用于控制哮喘。\n处理:\n1、2024.03.14-2024.03.21 家用峰流速仪使用 ePRO 系统填写依从性\n7/7*100%=100%,嘱托患者按照自己实际情况及时填写日志,如有问题\n随时沟通。\n2、无新增 AE,CM,无临床试验安全性事件。\n3、今日回收硫酸沙丁胺醇吸入气雾剂,发放新的硫酸沙丁胺醇吸入气\n雾剂1盒,并嘱托受试者正确保存和使用。\n4、绝经期女性,未做血、尿妊娠检查。\n第2页\nCS 扫描全能王\n3亿人都在用的扫描App\n科室:呼吸与危重症医学科\n门诊\n姓名\n联系方式\n性别:女\n年龄:62岁\n婚姻状况:其他\n2024-03-21 08:40 初诊记录\n5、受试者所有检查结果经再次核对入排,符合所有入选标准,不符合任\n一排除标准,可随机入组,分配随机号:_,随机分层信息:中剂量\nICS,嗜酸性粒细胞计数<300/ul,未联合使用LAMA。\n6、嘱托受试者2024.03.22来院行V4随访。\n医师签\n门诊病历专用章\n※提醒:复诊时,请携带本病历记录,谢谢!※",
    "role": "user"
  }
]
2026-08-10 11:43:22,077 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:43:22.076+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 24, "failed": 0, "current": {"38277e3a94b011f1bd9827cf206dfa2d": {"id": "38277e3a94b011f1bd9827cf206dfa2d", "doc_id": "370244ae94b011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479740, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362000249, "task_type": "dataflow", "root_trace_id": "96cd8dab6bb7455194a762d3f16e1d52", "root_traceparent": "00-96cd8dab6bb7455194a762d3f16e1d52-1e133766dfd81337-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:43:27,561 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:43:27,561 INFO     29 [qwen-vl-text] LLM output (len=760):
{
  "encounter_date": "2024-03-21",
  "chief_complaint": "SHR-1905-201 试验复筛",
  "present_illness": "发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可320ug bid,近日活动后气促再发,否认喘鸣音。无发热、胸痛。2024.01.10参加SHR-1905-201临床试验,因白细胞计数<3.0*10^9/L符合排除标准第12条筛败,于2024.03.01血液科就诊,无特殊处理,2024.03.06进行SHR-1905-201试验二次知情。受试者今日返院完成V3访视。",
  "past_history": "否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。既往病史:1.2022.12.10肝囊肿,持续;2.2023.10.31鼻窦炎,持续;3.2023.10.31双肺良性小结节,持续;4.2023.11.03-2023.12.13,肺肺部感染;5.2024.03.01开始,白细胞数降低1级;6.2024.01.10开始,高脂蛋白a血症。过敏史:否认食物、药物过敏史。",
  "diagnosis": "支气管哮喘",
  "treatment_plan": [
    "布地奈德福莫特罗粉吸入剂 320ug bid 经口腔吸入",
    "硫酸沙丁胺醇吸入气雾剂 1盒"
  ]
}
2026-08-10 11:43:27,561 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-03-21]
2026-08-10 11:43:27,565 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1352976, prompt_len=1493
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共34行）
["门诊病历", "科室:呼吸与危重症医学科", "姓名:", "性别:女", "门诊", "联系方", "年龄:62岁", "婚姻状况:其他", "2024-03-21 08:40 初诊记录", "主诉:SHR-1905-201 试验复筛", "现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年", "余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现", "气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行", "听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并", "规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可", "320ug bid,近日活动后气促再发,否认喘鸣音。无发热、胸痛。", "2024.01.10参加SHR-1905-201临床试验,因白细胞计数<3.0*10^9/L符", "合排除标准第12条筛败,于2024.03.01血液科就诊,无特殊处理,", "2024.03.06进行SHR-1905-201试验二次知情。受试者今日返院完成V3", "访视。", "既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。", "既往病史:", "1.2022.12.10肝囊肿,持续;", "2.2023.10.31鼻窦炎,持续;", "3.2023.10.31双肺良性小结节,持续;", "4.2023.11.03-2023.12.13,肺肺部感染;", "5.2024.03.01开始,白细胞数降低1级;", "6.2024.01.10开始,高脂蛋白a血症,", "过敏史:否认食物、药物过敏史。", "体格检查收缩压(mmHg):113;舒张压(mmHg):76", "其他体格检查:09:37进行生命体征测量:体温:36.5℃,血压:", "113/76mmHg,呼吸:18次/分,脉搏:98次/分;", "查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见", "第1页"]

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
2026-08-10 11:43:40,311 INFO     29 [qwen-vl-text] coord API raw response (len=2262):
[
	{"text": "门诊病历", "bbox": [417, 42, 585, 66]},
	{"text": "科室:呼吸与危重症医学科", "bbox": [92, 74, 334, 91]},
	{"text": "姓名:", "bbox": [92, 101, 115, 118]},
	{"text": "性别:女", "bbox": [93, 130, 165, 146]},
	{"text": "门诊", "bbox": [510, 74, 561, 91]},
	{"text": "联系方", "bbox": [510, 103, 565, 118]},
	{"text": "年龄:62岁", "bbox": [510, 131, 598, 146]},
	{"text": "婚姻状况:其他", "bbox": [660, 131, 787, 146]},
	{"text": "2024-03-21 08:40 初诊记录", "bbox": [90, 175, 375, 192]},
	{"text": "主诉:SHR-1905-201 试验复筛", "bbox": [90, 201, 441, 219]},
	{"text": "现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年", "bbox": [88, 227, 900, 245]},
	{"text": "余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现", "bbox": [193, 252, 900, 270]},
	{"text": "气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行", "bbox": [193, 277, 900, 295]},
	{"text": "听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并", "bbox": [193, 302, 900, 320]},
	{"text": "规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可", "bbox": [193, 327, 861, 346]},
	{"text": "320ug bid,近日活动后气促再发,否认喘鸣音。无发热、胸痛。", "bbox": [193, 353, 792, 371]},
	{"text": "2024.01.10参加SHR-1905-201临床试验,因白细胞计数<3.0*10^9/L符", "bbox": [193, 378, 900, 396]},
	{"text": "合排除标准第12条筛败,于2024.03.01血液科就诊,无特殊处理,", "bbox": [193, 403, 844, 421]},
	{"text": "2024.03.06进行SHR-1905-201试验二次知情。受试者今日返院完成V3", "bbox": [193, 429, 900, 447]},
	{"text": "访视。", "bbox": [193, 454, 252, 472]},
	{"text": "既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。", "bbox": [90, 479, 854, 498]},
	{"text": "既往病史:", "bbox": [193, 506, 299, 523]},
	{"text": "1.2022.12.10肝囊肿,持续;", "bbox": [193, 531, 474, 549]},
	{"text": "2.2023.10.31鼻窦炎,持续;", "bbox": [193, 557, 474, 575]},
	{"text": "3.2023.10.31双肺良性小结节,持续;", "bbox": [193, 582, 565, 600]},
	{"text": "4.2023.11.03-2023.12.13,肺肺部感染;", "bbox": [193, 608, 578, 626]},
	{"text": "5.2024.03.01开始,白细胞数降低1级;", "bbox": [193, 633, 587, 651]},
	{"text": "6.2024.01.10开始,高脂蛋白a血症,", "bbox": [193, 659, 563, 677]},
	{"text": "过敏史:否认食物、药物过敏史。", "bbox": [90, 736, 444, 754]},
	{"text": "体格检查收缩压(mmHg):113;舒张压(mmHg):76", "bbox": [90, 761, 643, 780]},
	{"text": "其他体格检查:09:37进行生命体征测量:体温:36.5℃,血压:", "bbox": [193, 787, 796, 805]},
	{"text": "113/76mmHg,呼吸:18次/分,脉搏:98次/分;", "bbox": [193, 812, 682, 831]},
	{"text": "查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见", "bbox": [193, 838, 902, 856]},
	{"text": "第1页", "bbox": [470, 870, 534, 887]}
]
2026-08-10 11:43:40,311 INFO     29 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=12.7s
2026-08-10 11:43:40,312 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[417, 42, 585, 66]
2026-08-10 11:43:40,312 INFO     29 [qwen-vl-text] coord item[1]: text=科室:呼吸与危重症医学科, bbox=[92, 74, 334, 91]
2026-08-10 11:43:40,312 INFO     29 [qwen-vl-text] coord item[2]: text=姓名:, bbox=[92, 101, 115, 118]
2026-08-10 11:43:40,312 INFO     29 [qwen-vl-text] coord item[3]: text=性别:女, bbox=[93, 130, 165, 146]
2026-08-10 11:43:40,312 INFO     29 [qwen-vl-text] coord item[4]: text=门诊, bbox=[510, 74, 561, 91]
2026-08-10 11:43:40,312 INFO     29 [qwen-vl-text] coord item[5]: text=联系方, bbox=[510, 103, 565, 118]
2026-08-10 11:43:40,312 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:62岁, bbox=[510, 131, 598, 146]
2026-08-10 11:43:40,312 INFO     29 [qwen-vl-text] coord item[7]: text=婚姻状况:其他, bbox=[660, 131, 787, 146]
2026-08-10 11:43:40,312 INFO     29 [qwen-vl-text] coord item[8]: text=2024-03-21 08:40 初诊记录, bbox=[90, 175, 375, 192]
2026-08-10 11:43:40,312 INFO     29 [qwen-vl-text] coord item[9]: text=主诉:SHR-1905-201 试验复筛, bbox=[90, 201, 441, 219]
2026-08-10 11:43:40,312 INFO     29 [qwen-vl-text] coord item[10]: text=现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年, bbox=[88, 227, 900, 245]
2026-08-10 11:43:40,313 INFO     29 [qwen-vl-text] coord item[11]: text=余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现, bbox=[193, 252, 900, 270]
2026-08-10 11:43:40,313 INFO     29 [qwen-vl-text] coord item[12]: text=气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行, bbox=[193, 277, 900, 295]
2026-08-10 11:43:40,313 INFO     29 [qwen-vl-text] coord item[13]: text=听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并, bbox=[193, 302, 900, 320]
2026-08-10 11:43:40,313 INFO     29 [qwen-vl-text] coord item[14]: text=规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可, bbox=[193, 327, 861, 346]
2026-08-10 11:43:40,313 INFO     29 [qwen-vl-text] coord item[15]: text=320ug bid,近日活动后气促再发,否认喘鸣音。无发热、胸痛。, bbox=[193, 353, 792, 371]
2026-08-10 11:43:40,313 INFO     29 [qwen-vl-text] coord item[16]: text=2024.01.10参加SHR-1905-201临床试验,因白细胞计数<3.0*10^9/L符, bbox=[193, 378, 900, 396]
2026-08-10 11:43:40,313 INFO     29 [qwen-vl-text] coord item[17]: text=合排除标准第12条筛败,于2024.03.01血液科就诊,无特殊处理,, bbox=[193, 403, 844, 421]
2026-08-10 11:43:40,313 INFO     29 [qwen-vl-text] coord item[18]: text=2024.03.06进行SHR-1905-201试验二次知情。受试者今日返院完成V3, bbox=[193, 429, 900, 447]
2026-08-10 11:43:40,313 INFO     29 [qwen-vl-text] coord item[19]: text=访视。, bbox=[193, 454, 252, 472]
2026-08-10 11:43:40,313 INFO     29 [qwen-vl-text] coord item[20]: text=既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。, bbox=[90, 479, 854, 498]
2026-08-10 11:43:40,313 INFO     29 [qwen-vl-text] coord item[21]: text=既往病史:, bbox=[193, 506, 299, 523]
2026-08-10 11:43:40,313 INFO     29 [qwen-vl-text] coord item[22]: text=1.2022.12.10肝囊肿,持续;, bbox=[193, 531, 474, 549]
2026-08-10 11:43:40,313 INFO     29 [qwen-vl-text] coord item[23]: text=2.2023.10.31鼻窦炎,持续;, bbox=[193, 557, 474, 575]
2026-08-10 11:43:40,313 INFO     29 [qwen-vl-text] coord item[24]: text=3.2023.10.31双肺良性小结节,持续;, bbox=[193, 582, 565, 600]
2026-08-10 11:43:40,313 INFO     29 [qwen-vl-text] coord item[25]: text=4.2023.11.03-2023.12.13,肺肺部感染;, bbox=[193, 608, 578, 626]
2026-08-10 11:43:40,313 INFO     29 [qwen-vl-text] coord item[26]: text=5.2024.03.01开始,白细胞数降低1级;, bbox=[193, 633, 587, 651]
2026-08-10 11:43:40,313 INFO     29 [qwen-vl-text] coord item[27]: text=6.2024.01.10开始,高脂蛋白a血症,, bbox=[193, 659, 563, 677]
2026-08-10 11:43:40,313 INFO     29 [qwen-vl-text] coord item[28]: text=过敏史:否认食物、药物过敏史。, bbox=[90, 736, 444, 754]
2026-08-10 11:43:40,313 INFO     29 [qwen-vl-text] coord item[29]: text=体格检查收缩压(mmHg):113;舒张压(mmHg):76, bbox=[90, 761, 643, 780]
2026-08-10 11:43:40,313 INFO     29 [qwen-vl-text] coord item[30]: text=其他体格检查:09:37进行生命体征测量:体温:36.5℃,血压:, bbox=[193, 787, 796, 805]
2026-08-10 11:43:40,314 INFO     29 [qwen-vl-text] coord item[31]: text=113/76mmHg,呼吸:18次/分,脉搏:98次/分;, bbox=[193, 812, 682, 831]
2026-08-10 11:43:40,314 INFO     29 [qwen-vl-text] coord item[32]: text=查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见, bbox=[193, 838, 902, 856]
2026-08-10 11:43:40,314 INFO     29 [qwen-vl-text] coord item[33]: text=第1页, bbox=[470, 870, 534, 887]
2026-08-10 11:43:40,315 INFO     29 [qwen-vl-text] page=4 — 34/34 coords, api_time=12.7s
2026-08-10 11:43:40,321 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1857056, prompt_len=1462
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共37行）
["科室:呼吸与危重症医学科", "姓名", "性别:女", "门诊", "联系方", "年龄:62岁", "婚姻状况:其他", "2024-03-21 08:40 初诊记录", "皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅", "大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。", "耳廓正常无畸形,外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无", "鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿", "大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中", "肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动", "正常,双肺呼吸音粗,未闻及干湿罗音。心律齐。双下肢无水肿。心音正", "常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛、反跳痛,无液", "波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触及,肾脏未触", "及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖器未查、肛门", "直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无异常,其他无", "异常。.", "检验检查:无", "初步诊断:支气管哮喘", "处理:", "CM 跟踪:", "1、布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,", "320ug,bid,经口腔吸入,用于控制哮喘。", "处理:", "1、2024.03.14-2024.03.21 家用峰流速仪使用 ePRO 系统填写依从性", "7/7*100%=100%,嘱托患者按照自己实际情况及时填写日志,如有问题", "随时沟通。", "2、无新增 AE,CM,无临床试验安全性事件。", "3、今日回收硫酸沙丁胺醇吸入气雾剂,发放新的硫酸沙丁胺醇吸入气", "雾剂1盒,并嘱托受试者正确保存和使用。", "4、绝经期女性,未做血、尿妊娠检查。", "第2页", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord API raw response (len=2361):
[
	{"text": "科室:呼吸与危重症医学科", "bbox": [102, 48, 339, 65]},
	{"text": "姓名", "bbox": [104, 75, 144, 92]},
	{"text": "性别:女", "bbox": [104, 102, 175, 118]},
	{"text": "门诊", "bbox": [513, 48, 564, 65]},
	{"text": "联系方", "bbox": [513, 75, 569, 92]},
	{"text": "年龄:62岁", "bbox": [513, 102, 603, 118]},
	{"text": "婚姻状况:其他", "bbox": [664, 102, 790, 118]},
	{"text": "2024-03-21 08:40 初诊记录", "bbox": [100, 145, 381, 162]},
	{"text": "皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅", "bbox": [202, 170, 905, 188]},
	{"text": "大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。", "bbox": [202, 194, 892, 212]},
	{"text": "耳廓正常无畸形,外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无", "bbox": [202, 218, 905, 236]},
	{"text": "鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿", "bbox": [202, 242, 904, 260]},
	{"text": "大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中", "bbox": [202, 266, 904, 284]},
	{"text": "肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动", "bbox": [202, 290, 904, 308]},
	{"text": "正常,双肺呼吸音粗,未闻及干湿罗音。心律齐。双下肢无水肿。心音正", "bbox": [202, 314, 904, 332]},
	{"text": "常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛、反跳痛,无液", "bbox": [202, 338, 904, 356]},
	{"text": "波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触及,肾脏未触", "bbox": [202, 362, 904, 380]},
	{"text": "及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖器未查、肛门", "bbox": [202, 386, 904, 404]},
	{"text": "直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无异常,其他无", "bbox": [202, 410, 904, 428]},
	{"text": "异常。.", "bbox": [202, 434, 268, 456]},
	{"text": "检验检查:无", "bbox": [100, 465, 227, 483]},
	{"text": "初步诊断:支气管哮喘", "bbox": [100, 490, 320, 508]},
	{"text": "处理:", "bbox": [100, 515, 204, 533]},
	{"text": "CM 跟踪:", "bbox": [202, 540, 300, 558]},
	{"text": "1、布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,", "bbox": [202, 564, 777, 582]},
	{"text": "320ug,bid,经口腔吸入,用于控制哮喘。", "bbox": [202, 588, 591, 607]},
	{"text": "处理:", "bbox": [202, 614, 259, 632]},
	{"text": "1、2024.03.14-2024.03.21 家用峰流速仪使用 ePRO 系统填写依从性", "bbox": [202, 638, 858, 657]},
	{"text": "7/7*100%=100%,嘱托患者按照自己实际情况及时填写日志,如有问题", "bbox": [202, 663, 904, 681]},
	{"text": "随时沟通。", "bbox": [202, 687, 308, 705]},
	{"text": "2、无新增 AE,CM,无临床试验安全性事件。", "bbox": [202, 711, 650, 729]},
	{"text": "3、今日回收硫酸沙丁胺醇吸入气雾剂,发放新的硫酸沙丁胺醇吸入气", "bbox": [202, 735, 904, 753]},
	{"text": "雾剂1盒,并嘱托受试者正确保存和使用。", "bbox": [202, 759, 628, 777]},
	{"text": "4、绝经期女性,未做血、尿妊娠检查。", "bbox": [202, 783, 595, 801]},
	{"text": "第2页", "bbox": [470, 815, 535, 832]},
	{"text": "CS 扫描全能王", "bbox": [861, 958, 977, 974]},
	{"text": "3亿人都在用的扫描App", "bbox": [861, 977, 976, 986]}
]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord API: raw_items=37, valid_items=37, elapsed=14.1s
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[0]: text=科室:呼吸与危重症医学科, bbox=[102, 48, 339, 65]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[1]: text=姓名, bbox=[104, 75, 144, 92]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[2]: text=性别:女, bbox=[104, 102, 175, 118]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[3]: text=门诊, bbox=[513, 48, 564, 65]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[4]: text=联系方, bbox=[513, 75, 569, 92]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[5]: text=年龄:62岁, bbox=[513, 102, 603, 118]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[6]: text=婚姻状况:其他, bbox=[664, 102, 790, 118]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[7]: text=2024-03-21 08:40 初诊记录, bbox=[100, 145, 381, 162]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[8]: text=皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅, bbox=[202, 170, 905, 188]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[9]: text=大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。, bbox=[202, 194, 892, 212]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[10]: text=耳廓正常无畸形,外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无, bbox=[202, 218, 905, 236]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[11]: text=鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿, bbox=[202, 242, 904, 260]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[12]: text=大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中, bbox=[202, 266, 904, 284]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[13]: text=肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动, bbox=[202, 290, 904, 308]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[14]: text=正常,双肺呼吸音粗,未闻及干湿罗音。心律齐。双下肢无水肿。心音正, bbox=[202, 314, 904, 332]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[15]: text=常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛、反跳痛,无液, bbox=[202, 338, 904, 356]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[16]: text=波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触及,肾脏未触, bbox=[202, 362, 904, 380]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[17]: text=及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖器未查、肛门, bbox=[202, 386, 904, 404]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[18]: text=直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无异常,其他无, bbox=[202, 410, 904, 428]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[19]: text=异常。., bbox=[202, 434, 268, 456]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[20]: text=检验检查:无, bbox=[100, 465, 227, 483]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[21]: text=初步诊断:支气管哮喘, bbox=[100, 490, 320, 508]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[22]: text=处理:, bbox=[100, 515, 204, 533]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[23]: text=CM 跟踪:, bbox=[202, 540, 300, 558]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[24]: text=1、布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,, bbox=[202, 564, 777, 582]
2026-08-10 11:43:54,425 INFO     29 [qwen-vl-text] coord item[25]: text=320ug,bid,经口腔吸入,用于控制哮喘。, bbox=[202, 588, 591, 607]
2026-08-10 11:43:54,426 INFO     29 [qwen-vl-text] coord item[26]: text=处理:, bbox=[202, 614, 259, 632]
2026-08-10 11:43:54,426 INFO     29 [qwen-vl-text] coord item[27]: text=1、2024.03.14-2024.03.21 家用峰流速仪使用 ePRO 系统填写依从性, bbox=[202, 638, 858, 657]
2026-08-10 11:43:54,426 INFO     29 [qwen-vl-text] coord item[28]: text=7/7*100%=100%,嘱托患者按照自己实际情况及时填写日志,如有问题, bbox=[202, 663, 904, 681]
2026-08-10 11:43:54,426 INFO     29 [qwen-vl-text] coord item[29]: text=随时沟通。, bbox=[202, 687, 308, 705]
2026-08-10 11:43:54,426 INFO     29 [qwen-vl-text] coord item[30]: text=2、无新增 AE,CM,无临床试验安全性事件。, bbox=[202, 711, 650, 729]
2026-08-10 11:43:54,426 INFO     29 [qwen-vl-text] coord item[31]: text=3、今日回收硫酸沙丁胺醇吸入气雾剂,发放新的硫酸沙丁胺醇吸入气, bbox=[202, 735, 904, 753]
2026-08-10 11:43:54,426 INFO     29 [qwen-vl-text] coord item[32]: text=雾剂1盒,并嘱托受试者正确保存和使用。, bbox=[202, 759, 628, 777]
2026-08-10 11:43:54,426 INFO     29 [qwen-vl-text] coord item[33]: text=4、绝经期女性,未做血、尿妊娠检查。, bbox=[202, 783, 595, 801]
2026-08-10 11:43:54,426 INFO     29 [qwen-vl-text] coord item[34]: text=第2页, bbox=[470, 815, 535, 832]
2026-08-10 11:43:54,426 INFO     29 [qwen-vl-text] coord item[35]: text=CS 扫描全能王, bbox=[861, 958, 977, 974]
2026-08-10 11:43:54,426 INFO     29 [qwen-vl-text] coord item[36]: text=3亿人都在用的扫描App, bbox=[861, 977, 976, 986]
2026-08-10 11:43:54,426 INFO     29 [qwen-vl-text] page=5 — 37/37 coords, api_time=14.1s
2026-08-10 11:43:54,427 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=545220, prompt_len=878
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共15行）
["科室:呼吸与危重症医学科", "门诊", "姓名", "联系方式", "性别:女", "年龄:62岁", "婚姻状况:其他", "2024-03-21 08:40 初诊记录", "5、受试者所有检查结果经再次核对入排,符合所有入选标准,不符合任", "一排除标准,可随机入组,分配随机号:_,随机分层信息:中剂量", "ICS,嗜酸性粒细胞计数<300/ul,未联合使用LAMA。", "6、嘱托受试者2024.03.22来院行V4随访。", "医师签", "门诊病历专用章", "※提醒:复诊时,请携带本病历记录,谢谢!※"]

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
2026-08-10 11:43:59,881 INFO     29 [qwen-vl-text] coord API raw response (len=869):
[
	{"text": "科室:呼吸与危重症医学科", "bbox": [77, 50, 318, 67]},
	{"text": "门诊", "bbox": [498, 50, 550, 67]},
	{"text": "姓名", "bbox": [77, 78, 118, 96]},
	{"text": "联系方式", "bbox": [498, 78, 577, 95]},
	{"text": "性别:女", "bbox": [77, 107, 150, 123]},
	{"text": "年龄:62岁", "bbox": [498, 107, 589, 123]},
	{"text": "婚姻状况:其他", "bbox": [651, 107, 781, 123]},
	{"text": "2024-03-21 08:40 初诊记录", "bbox": [73, 152, 363, 170]},
	{"text": "5、受试者所有检查结果经再次核对入排,符合所有入选标准,不符合任", "bbox": [180, 177, 901, 196]},
	{"text": "一排除标准,可随机入组,分配随机号:_,随机分层信息:中剂量", "bbox": [180, 202, 901, 222]},
	{"text": "ICS,嗜酸性粒细胞计数<300/ul,未联合使用LAMA。", "bbox": [180, 229, 741, 248]},
	{"text": "6、嘱托受试者2024.03.22来院行V4随访。", "bbox": [180, 255, 619, 274]},
	{"text": "医师签", "bbox": [652, 295, 715, 312]},
	{"text": "门诊病历专用章", "bbox": [77, 328, 327, 363]},
	{"text": "※提醒:复诊时,请携带本病历记录,谢谢!※", "bbox": [80, 415, 584, 434]}
]
2026-08-10 11:43:59,882 INFO     29 [qwen-vl-text] coord API: raw_items=15, valid_items=15, elapsed=5.5s
2026-08-10 11:43:59,882 INFO     29 [qwen-vl-text] coord item[0]: text=科室:呼吸与危重症医学科, bbox=[77, 50, 318, 67]
2026-08-10 11:43:59,882 INFO     29 [qwen-vl-text] coord item[1]: text=门诊, bbox=[498, 50, 550, 67]
2026-08-10 11:43:59,882 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[77, 78, 118, 96]
2026-08-10 11:43:59,882 INFO     29 [qwen-vl-text] coord item[3]: text=联系方式, bbox=[498, 78, 577, 95]
2026-08-10 11:43:59,882 INFO     29 [qwen-vl-text] coord item[4]: text=性别:女, bbox=[77, 107, 150, 123]
2026-08-10 11:43:59,882 INFO     29 [qwen-vl-text] coord item[5]: text=年龄:62岁, bbox=[498, 107, 589, 123]
2026-08-10 11:43:59,882 INFO     29 [qwen-vl-text] coord item[6]: text=婚姻状况:其他, bbox=[651, 107, 781, 123]
2026-08-10 11:43:59,882 INFO     29 [qwen-vl-text] coord item[7]: text=2024-03-21 08:40 初诊记录, bbox=[73, 152, 363, 170]
2026-08-10 11:43:59,883 INFO     29 [qwen-vl-text] coord item[8]: text=5、受试者所有检查结果经再次核对入排,符合所有入选标准,不符合任, bbox=[180, 177, 901, 196]
2026-08-10 11:43:59,883 INFO     29 [qwen-vl-text] coord item[9]: text=一排除标准,可随机入组,分配随机号:_,随机分层信息:中剂量, bbox=[180, 202, 901, 222]
2026-08-10 11:43:59,883 INFO     29 [qwen-vl-text] coord item[10]: text=ICS,嗜酸性粒细胞计数<300/ul,未联合使用LAMA。, bbox=[180, 229, 741, 248]
2026-08-10 11:43:59,883 INFO     29 [qwen-vl-text] coord item[11]: text=6、嘱托受试者2024.03.22来院行V4随访。, bbox=[180, 255, 619, 274]
2026-08-10 11:43:59,883 INFO     29 [qwen-vl-text] coord item[12]: text=医师签, bbox=[652, 295, 715, 312]
2026-08-10 11:43:59,883 INFO     29 [qwen-vl-text] coord item[13]: text=门诊病历专用章, bbox=[77, 328, 327, 363]
2026-08-10 11:43:59,883 INFO     29 [qwen-vl-text] coord item[14]: text=※提醒:复诊时,请携带本病历记录,谢谢!※, bbox=[80, 415, 584, 434]
2026-08-10 11:43:59,883 INFO     29 [qwen-vl-text] page=6 — 15/15 coords, api_time=5.5s
2026-08-10 11:43:59,884 INFO     29 [qwen-vl-text] new_positions (86):
[[4, 248.11499999999998, 348.075, 35.364, 55.571999999999996], [4, 54.739999999999995, 198.73, 62.308, 76.622], [4, 54.739999999999995, 68.425, 85.042, 99.356], [4, 55.335, 98.175, 109.46, 122.932], [4, 303.45, 333.79499999999996, 62.308, 76.622], [4, 303.45, 336.175, 86.726, 99.356], [4, 303.45, 355.81, 110.30199999999999, 122.932], [4, 392.7, 468.265, 110.30199999999999, 122.932], [4, 53.55, 223.125, 147.35, 161.664], [4, 53.55, 262.395, 169.242, 184.398], [4, 52.36, 535.5, 191.134, 206.29], [4, 114.835, 535.5, 212.184, 227.34], [4, 114.835, 535.5, 233.23399999999998, 248.39], [4, 114.835, 535.5, 254.284, 269.44], [4, 114.835, 512.295, 275.334, 291.332], [4, 114.835, 471.23999999999995, 297.226, 312.382], [4, 114.835, 535.5, 318.276, 333.432], [4, 114.835, 502.17999999999995, 339.32599999999996, 354.48199999999997], [4, 114.835, 535.5, 361.21799999999996, 376.37399999999997], [4, 114.835, 149.94, 382.268, 397.424], [4, 53.55, 508.13, 403.318, 419.316], [4, 114.835, 177.905, 426.05199999999996, 440.366], [4, 114.835, 282.03, 447.102, 462.258], [4, 114.835, 282.03, 468.99399999999997, 484.15], [4, 114.835, 336.175, 490.044, 505.2], [4, 114.835, 343.90999999999997, 511.936, 527.092], [4, 114.835, 349.265, 532.986, 548.1419999999999], [4, 114.835, 334.98499999999996, 554.8779999999999, 570.034], [4, 53.55, 264.18, 619.712, 634.8679999999999], [4, 53.55, 382.585, 640.762, 656.76], [4, 114.835, 473.62, 662.654, 677.81], [4, 114.835, 405.78999999999996, 683.704, 699.702], [4, 114.835, 536.6899999999999, 705.596, 720.752], [4, 279.65, 317.72999999999996, 732.54, 746.8539999999999], [5, 60.69, 201.70499999999998, 40.416, 54.73], [5, 61.879999999999995, 85.67999999999999, 63.15, 77.464], [5, 61.879999999999995, 104.125, 85.884, 99.356], [5, 305.235, 335.58, 40.416, 54.73], [5, 305.235, 338.555, 63.15, 77.464], [5, 305.235, 358.78499999999997, 85.884, 99.356], [5, 395.08, 470.04999999999995, 85.884, 99.356], [5, 59.5, 226.695, 122.08999999999999, 136.404], [5, 120.19, 538.475, 143.14, 158.296], [5, 120.19, 530.74, 163.34799999999998, 178.504], [5, 120.19, 538.475, 183.55599999999998, 198.712], [5, 120.19, 537.88, 203.76399999999998, 218.92], [5, 120.19, 537.88, 223.97199999999998, 239.128], [5, 120.19, 537.88, 244.17999999999998, 259.336], [5, 120.19, 537.88, 264.388, 279.544], [5, 120.19, 537.88, 284.596, 299.752], [5, 120.19, 537.88, 304.804, 319.96], [5, 120.19, 537.88, 325.012, 340.168], [5, 120.19, 537.88, 345.21999999999997, 360.376], [5, 120.19, 159.45999999999998, 365.428, 383.952], [5, 59.5, 135.065, 391.53, 406.686], [5, 59.5, 190.39999999999998, 412.58, 427.736], [5, 59.5, 121.38, 433.63, 448.786], [5, 120.19, 178.5, 454.68, 469.83599999999996], [5, 120.19, 462.315, 474.888, 490.044], [5, 120.19, 351.645, 495.096, 511.094], [5, 120.19, 154.105, 516.9879999999999, 532.144], [5, 120.19, 510.51, 537.196, 553.194], [5, 120.19, 537.88, 558.246, 573.4019999999999], [5, 120.19, 183.26, 578.454, 593.61], [5, 120.19, 386.75, 598.662, 613.818], [5, 120.19, 537.88, 618.87, 634.026], [5, 120.19, 373.65999999999997, 639.078, 654.2339999999999], [5, 120.19, 354.025, 659.286, 674.442], [5, 279.65, 318.325, 686.23, 700.544], [5, 512.295, 581.3149999999999, 806.636, 820.108], [5, 512.295, 580.72, 822.634, 830.212], [6, 45.815, 189.20999999999998, 42.1, 56.414], [6, 296.31, 327.25, 42.1, 56.414], [6, 45.815, 70.21, 65.676, 80.832], [6, 296.31, 343.315, 65.676, 79.99], [6, 45.815, 89.25, 90.094, 103.566], [6, 296.31, 350.455, 90.094, 103.566], [6, 387.34499999999997, 464.695, 90.094, 103.566], [6, 43.434999999999995, 215.98499999999999, 127.984, 143.14], [6, 107.1, 536.095, 149.034, 165.03199999999998], [6, 107.1, 536.095, 170.084, 186.924], [6, 107.1, 440.895, 192.81799999999998, 208.816], [6, 107.1, 368.305, 214.70999999999998, 230.708], [6, 387.94, 425.42499999999995, 248.39, 262.704], [6, 45.815, 194.565, 276.176, 305.646], [6, 47.599999999999994, 347.47999999999996, 349.43, 365.428]]
2026-08-10 11:43:59,884 INFO     29 [qwen-vl-text] ═══ DONE ═══ 86 positions, pages=3, time=39.6s
2026-08-10 11:43:59,884 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:43:59,896 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:43:59,896 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:43:59,897 INFO     29 [qwen-vl-text] positions(78): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:43:59,897 INFO     29 [qwen-vl-text] page grouping: [7, 8, 9], lines per page: [35, 28, 15]
2026-08-10 11:44:00,222 INFO     29 [qwen-vl-text] page=7, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:44:00,443 INFO     29 [qwen-vl-text] page=8, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:44:00,622 INFO     29 [qwen-vl-text] page=9, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:44:00,624 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1620
2026-08-10 11:44:00,624 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:44:00,625 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 222, \"bbox_end\": 299, \"encounter_dates\": [\"2024-12-12\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "科室:呼吸与危重症医学科\n门诊\n姓名\n联系\n性别:女\n年龄:63岁\n婚姻状况:其他\n2024-12-12 09:40 初诊记录\n主诉:SHR-1905-201 临床试验 V14\n现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年\n余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现\n气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行\n听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并\n规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可\n320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:\n近日咳嗽咳痰,低烧两天,呼吸道感染。2024.12.02行V14随访\n因患者发热延迟用药。今日回院用药,留院观察1h。\n既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。\n既往病史:\n1.2022.12.10肝囊肿,持续;\n2.2023.10.31鼻窦炎,持续;\n3.2023.10.31双肺良性小结节,持续;\n4.2023.11.03-2023.12.13,肺肺部感染;\n5.2024.03.01开始,白细胞数降低1级,持续;\n6.2024.01.10开始,高脂血症,持续;\n7.十余年前,慢性浅表胃炎,持续中。\n过敏史:否认食物、药物过敏史。\n体格检查收缩压(mmHg):-;舒张压(mmHg):-\n其他体格检查:未行\n检验检查:无\n初步诊断:支气管哮喘\n处理:检查:心脏电生理:心电图(十二导联心电图);\n检验:急诊血常规(五分类)+急诊超敏C反应蛋白、急诊肝功能五项\n治疗:静脉采血\n第1页\n科室:呼吸与危重症医学科\n性别:女\n年龄:63岁\n婚姻状况:其他\n2024-12-12 09:40 初诊记录\n无新增 AE,无新增 CM,无临床试验安全性事件。\n呼吸道感染,2024.11.27-2024.12.11,中度,与试验药物关系为可能无关\n对试验药物采取的措施为延迟用药,对 AE 采取的措施为药物治疗,肺\nSAE,非 SIE,不因此退出临床试验。\n跟踪 CM:\n1.盐酸莫西沙片,2024.12.02-2024.12.11,持续中,0.4g/片,1片/次,\nqd,po,用于治疗 AE 呼吸道感染。\n2.桉柠蒎肠溶胶囊,2024.12.02-2024.12.11 持续中,0.3g/粒,1粒/次,\ntid,po,用于治疗 AE 呼吸道感染。(化痰)\n3.氯苯那敏片,2024.12.02-2024.12.11,持续中,4mg/片,1片/次,\nqn,po,用于治疗 AE 呼吸道感染。\n4.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po,用于治\n疗病史慢性浅表胃炎。\n5.复方氨酚烷胺胶囊,2024.11.27-2024.12.02,持续中,0.25g:0.1g,1粒\n/次,bid,po,用于治疗 AE 呼吸道感染。\n6.吸入沙丁胺醇气雾剂,2024.12.02-2024.12.02,400ug,吸入,once,用于支\n气管扩张检查。\nCM 跟踪:\n1、布地奈德福莫特罗粉吸入剂,2022.11.27 开始,持续使用,\n320ug,bid,经口腔吸入,用于控制哮喘。\n2、硫酸沙丁胺醇气雾剂,2024.03.06 开始,持续中,100ug,pm,经口腔吸\n入,控制哮喘急性发作。\n第2页\n门诊病历\n科室:呼吸与危重症医学科\n姓名:\n性别:女\n门诊号\n联系方式\n年龄:63岁\n婚姻状况:其他\n2024-12-12 09:40 初诊记录\n处理:\n患者于今日 12:21-12:28 完成临床试验药物的注射,药物编号为\nY6077Y4950 用药前完善必要检查后随机用药。\n医师\n门诊病历\n※提醒:复诊时,请携带本病历记录,谢谢!※",
    "role": "user"
  }
]
2026-08-10 11:44:00,627 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:44:00.626+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 24, "failed": 0, "current": {"38277e3a94b011f1bd9827cf206dfa2d": {"id": "38277e3a94b011f1bd9827cf206dfa2d", "doc_id": "370244ae94b011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479740, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362000249, "task_type": "dataflow", "root_trace_id": "96cd8dab6bb7455194a762d3f16e1d52", "root_traceparent": "00-96cd8dab6bb7455194a762d3f16e1d52-1e133766dfd81337-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:44:06,020 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:44:06,021 INFO     29 [qwen-vl-text] LLM output (len=801):
{
  "encounter_date": "2024-12-12",
  "chief_complaint": "SHR-1905-201 临床试验 V14",
  "present_illness": "发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:近日咳嗽咳痰,低烧两天,呼吸道感染。2024.12.02行V14随访因患者发热延迟用药。今日回院用药,留院观察1h。",
  "past_history": "否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。既往病史:1.2022.12.10肝囊肿,持续;2.2023.10.31鼻窦炎,持续;3.2023.10.31双肺良性小结节,持续;4.2023.11.03-2023.12.13,肺肺部感染;5.2024.03.01开始,白细胞数降低1级,持续;6.2024.01.10开始,高脂血症,持续;7.十余年前,慢性浅表胃炎,持续中。过敏史:否认食物、药物过敏史。",
  "diagnosis": "支气管哮喘",
  "treatment_plan": [
    "检查:心脏电生理:心电图(十二导联心电图)",
    "检验:急诊血常规(五分类)+急诊超敏C反应蛋白、急诊肝功能五项",
    "治疗:静脉采血",
    "临床试验药物注射:药物编号Y6077Y4950,于12:21-12:28完成注射"
  ]
}
2026-08-10 11:44:06,021 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-12-12]
2026-08-10 11:44:06,023 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1512216, prompt_len=1449
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共35行）
["科室:呼吸与危重症医学科", "门诊", "姓名", "联系", "性别:女", "年龄:63岁", "婚姻状况:其他", "2024-12-12 09:40 初诊记录", "主诉:SHR-1905-201 临床试验 V14", "现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年", "余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现", "气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行", "听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并", "规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可", "320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:", "近日咳嗽咳痰,低烧两天,呼吸道感染。2024.12.02行V14随访", "因患者发热延迟用药。今日回院用药,留院观察1h。", "既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。", "既往病史:", "1.2022.12.10肝囊肿,持续;", "2.2023.10.31鼻窦炎,持续;", "3.2023.10.31双肺良性小结节,持续;", "4.2023.11.03-2023.12.13,肺肺部感染;", "5.2024.03.01开始,白细胞数降低1级,持续;", "6.2024.01.10开始,高脂血症,持续;", "7.十余年前,慢性浅表胃炎,持续中。", "过敏史:否认食物、药物过敏史。", "体格检查收缩压(mmHg):-;舒张压(mmHg):-", "其他体格检查:未行", "检验检查:无", "初步诊断:支气管哮喘", "处理:检查:心脏电生理:心电图(十二导联心电图);", "检验:急诊血常规(五分类)+急诊超敏C反应蛋白、急诊肝功能五项", "治疗:静脉采血", "第1页"]

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
2026-08-10 11:44:18,563 INFO     29 [qwen-vl-text] coord API raw response (len=2260):
[
	{"text": "科室:呼吸与危重症医学科", "bbox": [106, 20, 338, 39]},
	{"text": "门诊", "bbox": [511, 20, 564, 39]},
	{"text": "姓名", "bbox": [106, 50, 138, 68]},
	{"text": "联系", "bbox": [511, 50, 554, 68]},
	{"text": "性别:女", "bbox": [106, 80, 177, 98]},
	{"text": "年龄:63岁", "bbox": [511, 80, 603, 98]},
	{"text": "婚姻状况:其他", "bbox": [663, 80, 791, 98]},
	{"text": "2024-12-12 09:40 初诊记录", "bbox": [103, 127, 379, 146]},
	{"text": "主诉:SHR-1905-201 临床试验 V14", "bbox": [103, 154, 489, 173]},
	{"text": "现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年", "bbox": [103, 181, 904, 201]},
	{"text": "余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现", "bbox": [203, 208, 904, 228]},
	{"text": "气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行", "bbox": [203, 235, 904, 255]},
	{"text": "听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并", "bbox": [203, 262, 904, 282]},
	{"text": "规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可", "bbox": [203, 289, 865, 309]},
	{"text": "320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:", "bbox": [203, 316, 837, 336]},
	{"text": "近日咳嗽咳痰,低烧两天,呼吸道感染。2024.12.02行V14随访", "bbox": [270, 343, 904, 363]},
	{"text": "因患者发热延迟用药。今日回院用药,留院观察1h。", "bbox": [203, 370, 727, 390]},
	{"text": "既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。", "bbox": [103, 397, 857, 416]},
	{"text": "既往病史:", "bbox": [203, 424, 307, 443]},
	{"text": "1.2022.12.10肝囊肿,持续;", "bbox": [203, 451, 478, 470]},
	{"text": "2.2023.10.31鼻窦炎,持续;", "bbox": [203, 477, 478, 497]},
	{"text": "3.2023.10.31双肺良性小结节,持续;", "bbox": [203, 504, 569, 524]},
	{"text": "4.2023.11.03-2023.12.13,肺肺部感染;", "bbox": [203, 531, 582, 550]},
	{"text": "5.2024.03.01开始,白细胞数降低1级,持续;", "bbox": [203, 557, 659, 577]},
	{"text": "6.2024.01.10开始,高脂血症,持续;", "bbox": [203, 584, 569, 604]},
	{"text": "7.十余年前,慢性浅表胃炎,持续中。", "bbox": [203, 611, 578, 630]},
	{"text": "过敏史:否认食物、药物过敏史。", "bbox": [103, 638, 448, 658]},
	{"text": "体格检查收缩压(mmHg):-;舒张压(mmHg):-", "bbox": [103, 665, 603, 685]},
	{"text": "其他体格检查:未行", "bbox": [203, 692, 397, 711]},
	{"text": "检验检查:无", "bbox": [103, 718, 228, 738]},
	{"text": "初步诊断:支气管哮喘", "bbox": [103, 745, 320, 765]},
	{"text": "处理:检查:心脏电生理:心电图(十二导联心电图);", "bbox": [173, 772, 668, 791]},
	{"text": "检验:急诊血常规(五分类)+急诊超敏C反应蛋白、急诊肝功能五项", "bbox": [203, 798, 862, 818]},
	{"text": "治疗:静脉采血", "bbox": [203, 825, 349, 844]},
	{"text": "第1页", "bbox": [471, 858, 535, 876]}
]
2026-08-10 11:44:18,563 INFO     29 [qwen-vl-text] coord API: raw_items=35, valid_items=35, elapsed=12.5s
2026-08-10 11:44:18,563 INFO     29 [qwen-vl-text] coord item[0]: text=科室:呼吸与危重症医学科, bbox=[106, 20, 338, 39]
2026-08-10 11:44:18,563 INFO     29 [qwen-vl-text] coord item[1]: text=门诊, bbox=[511, 20, 564, 39]
2026-08-10 11:44:18,563 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[106, 50, 138, 68]
2026-08-10 11:44:18,563 INFO     29 [qwen-vl-text] coord item[3]: text=联系, bbox=[511, 50, 554, 68]
2026-08-10 11:44:18,563 INFO     29 [qwen-vl-text] coord item[4]: text=性别:女, bbox=[106, 80, 177, 98]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[5]: text=年龄:63岁, bbox=[511, 80, 603, 98]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[6]: text=婚姻状况:其他, bbox=[663, 80, 791, 98]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[7]: text=2024-12-12 09:40 初诊记录, bbox=[103, 127, 379, 146]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[8]: text=主诉:SHR-1905-201 临床试验 V14, bbox=[103, 154, 489, 173]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[9]: text=现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年, bbox=[103, 181, 904, 201]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[10]: text=余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现, bbox=[203, 208, 904, 228]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[11]: text=气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行, bbox=[203, 235, 904, 255]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[12]: text=听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并, bbox=[203, 262, 904, 282]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[13]: text=规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可, bbox=[203, 289, 865, 309]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[14]: text=320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:, bbox=[203, 316, 837, 336]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[15]: text=近日咳嗽咳痰,低烧两天,呼吸道感染。2024.12.02行V14随访, bbox=[270, 343, 904, 363]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[16]: text=因患者发热延迟用药。今日回院用药,留院观察1h。, bbox=[203, 370, 727, 390]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[17]: text=既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。, bbox=[103, 397, 857, 416]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[18]: text=既往病史:, bbox=[203, 424, 307, 443]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[19]: text=1.2022.12.10肝囊肿,持续;, bbox=[203, 451, 478, 470]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[20]: text=2.2023.10.31鼻窦炎,持续;, bbox=[203, 477, 478, 497]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[21]: text=3.2023.10.31双肺良性小结节,持续;, bbox=[203, 504, 569, 524]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[22]: text=4.2023.11.03-2023.12.13,肺肺部感染;, bbox=[203, 531, 582, 550]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[23]: text=5.2024.03.01开始,白细胞数降低1级,持续;, bbox=[203, 557, 659, 577]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[24]: text=6.2024.01.10开始,高脂血症,持续;, bbox=[203, 584, 569, 604]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[25]: text=7.十余年前,慢性浅表胃炎,持续中。, bbox=[203, 611, 578, 630]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[26]: text=过敏史:否认食物、药物过敏史。, bbox=[103, 638, 448, 658]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[27]: text=体格检查收缩压(mmHg):-;舒张压(mmHg):-, bbox=[103, 665, 603, 685]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[28]: text=其他体格检查:未行, bbox=[203, 692, 397, 711]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[29]: text=检验检查:无, bbox=[103, 718, 228, 738]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[30]: text=初步诊断:支气管哮喘, bbox=[103, 745, 320, 765]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[31]: text=处理:检查:心脏电生理:心电图(十二导联心电图);, bbox=[173, 772, 668, 791]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[32]: text=检验:急诊血常规(五分类)+急诊超敏C反应蛋白、急诊肝功能五项, bbox=[203, 798, 862, 818]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[33]: text=治疗:静脉采血, bbox=[203, 825, 349, 844]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] coord item[34]: text=第1页, bbox=[471, 858, 535, 876]
2026-08-10 11:44:18,564 INFO     29 [qwen-vl-text] page=7 — 35/35 coords, api_time=12.5s
2026-08-10 11:44:18,566 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1178711, prompt_len=1415
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共28行）
["科室:呼吸与危重症医学科", "性别:女", "年龄:63岁", "婚姻状况:其他", "2024-12-12 09:40 初诊记录", "无新增 AE,无新增 CM,无临床试验安全性事件。", "呼吸道感染,2024.11.27-2024.12.11,中度,与试验药物关系为可能无关", "对试验药物采取的措施为延迟用药,对 AE 采取的措施为药物治疗,肺", "SAE,非 SIE,不因此退出临床试验。", "跟踪 CM:", "1.盐酸莫西沙片,2024.12.02-2024.12.11,持续中,0.4g/片,1片/次,", "qd,po,用于治疗 AE 呼吸道感染。", "2.桉柠蒎肠溶胶囊,2024.12.02-2024.12.11 持续中,0.3g/粒,1粒/次,", "tid,po,用于治疗 AE 呼吸道感染。(化痰)", "3.氯苯那敏片,2024.12.02-2024.12.11,持续中,4mg/片,1片/次,", "qn,po,用于治疗 AE 呼吸道感染。", "4.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po,用于治", "疗病史慢性浅表胃炎。", "5.复方氨酚烷胺胶囊,2024.11.27-2024.12.02,持续中,0.25g:0.1g,1粒", "/次,bid,po,用于治疗 AE 呼吸道感染。", "6.吸入沙丁胺醇气雾剂,2024.12.02-2024.12.02,400ug,吸入,once,用于支", "气管扩张检查。", "CM 跟踪:", "1、布地奈德福莫特罗粉吸入剂,2022.11.27 开始,持续使用,", "320ug,bid,经口腔吸入,用于控制哮喘。", "2、硫酸沙丁胺醇气雾剂,2024.03.06 开始,持续中,100ug,pm,经口腔吸", "入,控制哮喘急性发作。", "第2页"]

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
2026-08-10 11:44:30,871 INFO     29 [qwen-vl-text] coord API raw response (len=1947):
[
	{"text": "科室:呼吸与危重症医学科", "bbox": [102, 27, 332, 44]},
	{"text": "性别:女", "bbox": [102, 84, 170, 100]},
	{"text": "年龄:63岁", "bbox": [504, 84, 594, 100]},
	{"text": "婚姻状况:其他", "bbox": [656, 84, 784, 100]},
	{"text": "2024-12-12 09:40 初诊记录", "bbox": [96, 129, 372, 147]},
	{"text": "无新增 AE,无新增 CM,无临床试验安全性事件。", "bbox": [196, 207, 664, 226]},
	{"text": "呼吸道感染,2024.11.27-2024.12.11,中度,与试验药物关系为可能无关", "bbox": [196, 260, 898, 279]},
	{"text": "对试验药物采取的措施为延迟用药,对 AE 采取的措施为药物治疗,肺", "bbox": [196, 286, 898, 304]},
	{"text": "SAE,非 SIE,不因此退出临床试验。", "bbox": [196, 312, 531, 330]},
	{"text": "跟踪 CM:", "bbox": [196, 338, 288, 356]},
	{"text": "1.盐酸莫西沙片,2024.12.02-2024.12.11,持续中,0.4g/片,1片/次,", "bbox": [196, 364, 830, 383]},
	{"text": "qd,po,用于治疗 AE 呼吸道感染。", "bbox": [196, 390, 512, 409]},
	{"text": "2.桉柠蒎肠溶胶囊,2024.12.02-2024.12.11 持续中,0.3g/粒,1粒/次,", "bbox": [196, 416, 827, 435]},
	{"text": "tid,po,用于治疗 AE 呼吸道感染。(化痰)", "bbox": [196, 442, 591, 461]},
	{"text": "3.氯苯那敏片,2024.12.02-2024.12.11,持续中,4mg/片,1片/次,", "bbox": [196, 468, 794, 487]},
	{"text": "qn,po,用于治疗 AE 呼吸道感染。", "bbox": [196, 494, 512, 513]},
	{"text": "4.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po,用于治", "bbox": [196, 520, 897, 539]},
	{"text": "疗病史慢性浅表胃炎。", "bbox": [196, 546, 414, 565]},
	{"text": "5.复方氨酚烷胺胶囊,2024.11.27-2024.12.02,持续中,0.25g:0.1g,1粒", "bbox": [196, 572, 896, 591]},
	{"text": "/次,bid,po,用于治疗 AE 呼吸道感染。", "bbox": [196, 598, 569, 617]},
	{"text": "6.吸入沙丁胺醇气雾剂,2024.12.02-2024.12.02,400ug,吸入,once,用于支", "bbox": [196, 624, 896, 643]},
	{"text": "气管扩张检查。", "bbox": [196, 650, 344, 669]},
	{"text": "CM 跟踪:", "bbox": [196, 677, 288, 695]},
	{"text": "1、布地奈德福莫特罗粉吸入剂,2022.11.27 开始,持续使用,", "bbox": [196, 703, 768, 722]},
	{"text": "320ug,bid,经口腔吸入,用于控制哮喘。", "bbox": [196, 729, 581, 748]},
	{"text": "2、硫酸沙丁胺醇气雾剂,2024.03.06 开始,持续中,100ug,pm,经口腔吸", "bbox": [196, 755, 896, 774]},
	{"text": "入,控制哮喘急性发作。", "bbox": [196, 781, 434, 799]},
	{"text": "第2页", "bbox": [460, 842, 524, 860]}
]
2026-08-10 11:44:30,871 INFO     29 [qwen-vl-text] coord API: raw_items=28, valid_items=28, elapsed=12.3s
2026-08-10 11:44:30,871 INFO     29 [qwen-vl-text] coord item[0]: text=科室:呼吸与危重症医学科, bbox=[102, 27, 332, 44]
2026-08-10 11:44:30,871 INFO     29 [qwen-vl-text] coord item[1]: text=性别:女, bbox=[102, 84, 170, 100]
2026-08-10 11:44:30,871 INFO     29 [qwen-vl-text] coord item[2]: text=年龄:63岁, bbox=[504, 84, 594, 100]
2026-08-10 11:44:30,871 INFO     29 [qwen-vl-text] coord item[3]: text=婚姻状况:其他, bbox=[656, 84, 784, 100]
2026-08-10 11:44:30,871 INFO     29 [qwen-vl-text] coord item[4]: text=2024-12-12 09:40 初诊记录, bbox=[96, 129, 372, 147]
2026-08-10 11:44:30,871 INFO     29 [qwen-vl-text] coord item[5]: text=无新增 AE,无新增 CM,无临床试验安全性事件。, bbox=[196, 207, 664, 226]
2026-08-10 11:44:30,871 INFO     29 [qwen-vl-text] coord item[6]: text=呼吸道感染,2024.11.27-2024.12.11,中度,与试验药物关系为可能无关, bbox=[196, 260, 898, 279]
2026-08-10 11:44:30,872 INFO     29 [qwen-vl-text] coord item[7]: text=对试验药物采取的措施为延迟用药,对 AE 采取的措施为药物治疗,肺, bbox=[196, 286, 898, 304]
2026-08-10 11:44:30,872 INFO     29 [qwen-vl-text] coord item[8]: text=SAE,非 SIE,不因此退出临床试验。, bbox=[196, 312, 531, 330]
2026-08-10 11:44:30,872 INFO     29 [qwen-vl-text] coord item[9]: text=跟踪 CM:, bbox=[196, 338, 288, 356]
2026-08-10 11:44:30,872 INFO     29 [qwen-vl-text] coord item[10]: text=1.盐酸莫西沙片,2024.12.02-2024.12.11,持续中,0.4g/片,1片/次,, bbox=[196, 364, 830, 383]
2026-08-10 11:44:30,872 INFO     29 [qwen-vl-text] coord item[11]: text=qd,po,用于治疗 AE 呼吸道感染。, bbox=[196, 390, 512, 409]
2026-08-10 11:44:30,872 INFO     29 [qwen-vl-text] coord item[12]: text=2.桉柠蒎肠溶胶囊,2024.12.02-2024.12.11 持续中,0.3g/粒,1粒/次,, bbox=[196, 416, 827, 435]
2026-08-10 11:44:30,872 INFO     29 [qwen-vl-text] coord item[13]: text=tid,po,用于治疗 AE 呼吸道感染。(化痰), bbox=[196, 442, 591, 461]
2026-08-10 11:44:30,872 INFO     29 [qwen-vl-text] coord item[14]: text=3.氯苯那敏片,2024.12.02-2024.12.11,持续中,4mg/片,1片/次,, bbox=[196, 468, 794, 487]
2026-08-10 11:44:30,872 INFO     29 [qwen-vl-text] coord item[15]: text=qn,po,用于治疗 AE 呼吸道感染。, bbox=[196, 494, 512, 513]
2026-08-10 11:44:30,872 INFO     29 [qwen-vl-text] coord item[16]: text=4.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po,用于治, bbox=[196, 520, 897, 539]
2026-08-10 11:44:30,872 INFO     29 [qwen-vl-text] coord item[17]: text=疗病史慢性浅表胃炎。, bbox=[196, 546, 414, 565]
2026-08-10 11:44:30,872 INFO     29 [qwen-vl-text] coord item[18]: text=5.复方氨酚烷胺胶囊,2024.11.27-2024.12.02,持续中,0.25g:0.1g,1粒, bbox=[196, 572, 896, 591]
2026-08-10 11:44:30,872 INFO     29 [qwen-vl-text] coord item[19]: text=/次,bid,po,用于治疗 AE 呼吸道感染。, bbox=[196, 598, 569, 617]
2026-08-10 11:44:30,872 INFO     29 [qwen-vl-text] coord item[20]: text=6.吸入沙丁胺醇气雾剂,2024.12.02-2024.12.02,400ug,吸入,once,用于支, bbox=[196, 624, 896, 643]
2026-08-10 11:44:30,872 INFO     29 [qwen-vl-text] coord item[21]: text=气管扩张检查。, bbox=[196, 650, 344, 669]
2026-08-10 11:44:30,872 INFO     29 [qwen-vl-text] coord item[22]: text=CM 跟踪:, bbox=[196, 677, 288, 695]
2026-08-10 11:44:30,872 INFO     29 [qwen-vl-text] coord item[23]: text=1、布地奈德福莫特罗粉吸入剂,2022.11.27 开始,持续使用,, bbox=[196, 703, 768, 722]
2026-08-10 11:44:30,872 INFO     29 [qwen-vl-text] coord item[24]: text=320ug,bid,经口腔吸入,用于控制哮喘。, bbox=[196, 729, 581, 748]
2026-08-10 11:44:30,872 INFO     29 [qwen-vl-text] coord item[25]: text=2、硫酸沙丁胺醇气雾剂,2024.03.06 开始,持续中,100ug,pm,经口腔吸, bbox=[196, 755, 896, 774]
2026-08-10 11:44:30,872 INFO     29 [qwen-vl-text] coord item[26]: text=入,控制哮喘急性发作。, bbox=[196, 781, 434, 799]
2026-08-10 11:44:30,872 INFO     29 [qwen-vl-text] coord item[27]: text=第2页, bbox=[460, 842, 524, 860]
2026-08-10 11:44:30,872 INFO     29 [qwen-vl-text] page=8 — 28/28 coords, api_time=12.3s
2026-08-10 11:44:30,873 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=509416, prompt_len=827
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共15行）
["门诊病历", "科室:呼吸与危重症医学科", "姓名:", "性别:女", "门诊号", "联系方式", "年龄:63岁", "婚姻状况:其他", "2024-12-12 09:40 初诊记录", "处理:", "患者于今日 12:21-12:28 完成临床试验药物的注射,药物编号为", "Y6077Y4950 用药前完善必要检查后随机用药。", "医师", "门诊病历", "※提醒:复诊时,请携带本病历记录,谢谢!※"]

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
2026-08-10 11:44:36,276 INFO     29 [qwen-vl-text] coord API raw response (len=901):
[
	{"text": "门诊病历", "bbox": [413, 50, 588, 74]},
	{"text": "科室:呼吸与危重症医学科", "bbox": [85, 84, 326, 100]},
	{"text": "姓名:", "bbox": [85, 112, 264, 129]},
	{"text": "性别:女", "bbox": [87, 142, 157, 158]},
	{"text": "门诊号", "bbox": [506, 84, 590, 100]},
	{"text": "联系方式", "bbox": [506, 112, 588, 129]},
	{"text": "年龄:63岁", "bbox": [507, 142, 603, 157]},
	{"text": "婚姻状况:其他", "bbox": [666, 142, 797, 157]},
	{"text": "2024-12-12 09:40 初诊记录", "bbox": [80, 189, 369, 206]},
	{"text": "处理:", "bbox": [185, 242, 242, 260]},
	{"text": "患者于今日 12:21-12:28 完成临床试验药物的注射,药物编号为", "bbox": [187, 267, 842, 285]},
	{"text": "Y6077Y4950 用药前完善必要检查后随机用药。", "bbox": [187, 294, 671, 312]},
	{"text": "医师", "bbox": [665, 334, 721, 351]},
	{"text": "门诊病历", "bbox": [85, 365, 348, 413]},
	{"text": "※提醒:复诊时,请携带本病历记录,谢谢!※", "bbox": [87, 457, 595, 475]},
	{"text": "“若有高血压糖尿病诊断,建议您到居住地附近社康中心,建立居民健康档案”", "bbox": [90, 487, 912, 505]}
]
2026-08-10 11:44:36,277 INFO     29 [qwen-vl-text] coord API: raw_items=16, valid_items=16, elapsed=5.4s
2026-08-10 11:44:36,277 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[413, 50, 588, 74]
2026-08-10 11:44:36,277 INFO     29 [qwen-vl-text] coord item[1]: text=科室:呼吸与危重症医学科, bbox=[85, 84, 326, 100]
2026-08-10 11:44:36,277 INFO     29 [qwen-vl-text] coord item[2]: text=姓名:, bbox=[85, 112, 264, 129]
2026-08-10 11:44:36,277 INFO     29 [qwen-vl-text] coord item[3]: text=性别:女, bbox=[87, 142, 157, 158]
2026-08-10 11:44:36,277 INFO     29 [qwen-vl-text] coord item[4]: text=门诊号, bbox=[506, 84, 590, 100]
2026-08-10 11:44:36,278 INFO     29 [qwen-vl-text] coord item[5]: text=联系方式, bbox=[506, 112, 588, 129]
2026-08-10 11:44:36,278 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:63岁, bbox=[507, 142, 603, 157]
2026-08-10 11:44:36,278 INFO     29 [qwen-vl-text] coord item[7]: text=婚姻状况:其他, bbox=[666, 142, 797, 157]
2026-08-10 11:44:36,278 INFO     29 [qwen-vl-text] coord item[8]: text=2024-12-12 09:40 初诊记录, bbox=[80, 189, 369, 206]
2026-08-10 11:44:36,278 INFO     29 [qwen-vl-text] coord item[9]: text=处理:, bbox=[185, 242, 242, 260]
2026-08-10 11:44:36,278 INFO     29 [qwen-vl-text] coord item[10]: text=患者于今日 12:21-12:28 完成临床试验药物的注射,药物编号为, bbox=[187, 267, 842, 285]
2026-08-10 11:44:36,278 INFO     29 [qwen-vl-text] coord item[11]: text=Y6077Y4950 用药前完善必要检查后随机用药。, bbox=[187, 294, 671, 312]
2026-08-10 11:44:36,278 INFO     29 [qwen-vl-text] coord item[12]: text=医师, bbox=[665, 334, 721, 351]
2026-08-10 11:44:36,278 INFO     29 [qwen-vl-text] coord item[13]: text=门诊病历, bbox=[85, 365, 348, 413]
2026-08-10 11:44:36,278 INFO     29 [qwen-vl-text] coord item[14]: text=※提醒:复诊时,请携带本病历记录,谢谢!※, bbox=[87, 457, 595, 475]
2026-08-10 11:44:36,278 INFO     29 [qwen-vl-text] coord item[15]: text=“若有高血压糖尿病诊断,建议您到居住地附近社康中心,建立居民健康档案”, bbox=[90, 487, 912, 505]
2026-08-10 11:44:36,278 INFO     29 [qwen-vl-text] page=9 — 15/15 coords, api_time=5.4s
2026-08-10 11:44:36,279 INFO     29 [qwen-vl-text] new_positions (78):
[[7, 63.07, 201.10999999999999, 16.84, 32.838], [7, 304.04499999999996, 335.58, 16.84, 32.838], [7, 63.07, 82.11, 42.1, 57.256], [7, 304.04499999999996, 329.63, 42.1, 57.256], [7, 63.07, 105.315, 67.36, 82.51599999999999], [7, 304.04499999999996, 358.78499999999997, 67.36, 82.51599999999999], [7, 394.48499999999996, 470.645, 67.36, 82.51599999999999], [7, 61.285, 225.505, 106.934, 122.932], [7, 61.285, 290.955, 129.668, 145.666], [7, 61.285, 537.88, 152.402, 169.242], [7, 120.785, 537.88, 175.136, 191.976], [7, 120.785, 537.88, 197.87, 214.70999999999998], [7, 120.785, 537.88, 220.60399999999998, 237.444], [7, 120.785, 514.675, 243.338, 260.178], [7, 120.785, 498.015, 266.072, 282.912], [7, 160.65, 537.88, 288.806, 305.646], [7, 120.785, 432.565, 311.53999999999996, 328.38], [7, 61.285, 509.91499999999996, 334.274, 350.272], [7, 120.785, 182.665, 357.008, 373.006], [7, 120.785, 284.40999999999997, 379.74199999999996, 395.74], [7, 120.785, 284.40999999999997, 401.63399999999996, 418.474], [7, 120.785, 338.555, 424.368, 441.20799999999997], [7, 120.785, 346.28999999999996, 447.102, 463.09999999999997], [7, 120.785, 392.10499999999996, 468.99399999999997, 485.834], [7, 120.785, 338.555, 491.728, 508.568], [7, 120.785, 343.90999999999997, 514.462, 530.46], [7, 61.285, 266.56, 537.196, 554.036], [7, 61.285, 358.78499999999997, 559.93, 576.77], [7, 120.785, 236.215, 582.664, 598.662], [7, 61.285, 135.66, 604.5559999999999, 621.396], [7, 61.285, 190.39999999999998, 627.29, 644.13], [7, 102.935, 397.46, 650.024, 666.0219999999999], [7, 120.785, 512.89, 671.9159999999999, 688.756], [7, 120.785, 207.655, 694.65, 710.648], [7, 280.245, 318.325, 722.4359999999999, 737.592], [8, 60.69, 197.54, 22.733999999999998, 37.048], [8, 60.69, 101.14999999999999, 70.728, 84.2], [8, 299.88, 353.43, 70.728, 84.2], [8, 390.32, 466.47999999999996, 70.728, 84.2], [8, 57.12, 221.34, 108.618, 123.774], [8, 116.61999999999999, 395.08, 174.29399999999998, 190.292], [8, 116.61999999999999, 534.31, 218.92, 234.91799999999998], [8, 116.61999999999999, 534.31, 240.81199999999998, 255.968], [8, 116.61999999999999, 315.945, 262.704, 277.86], [8, 116.61999999999999, 171.35999999999999, 284.596, 299.752], [8, 116.61999999999999, 493.84999999999997, 306.488, 322.486], [8, 116.61999999999999, 304.64, 328.38, 344.378], [8, 116.61999999999999, 492.065, 350.272, 366.27], [8, 116.61999999999999, 351.645, 372.164, 388.162], [8, 116.61999999999999, 472.43, 394.056, 410.054], [8, 116.61999999999999, 304.64, 415.948, 431.94599999999997], [8, 116.61999999999999, 533.715, 437.84, 453.83799999999997], [8, 116.61999999999999, 246.32999999999998, 459.73199999999997, 475.72999999999996], [8, 116.61999999999999, 533.12, 481.62399999999997, 497.62199999999996], [8, 116.61999999999999, 338.555, 503.51599999999996, 519.514], [8, 116.61999999999999, 533.12, 525.408, 541.406], [8, 116.61999999999999, 204.67999999999998, 547.3, 563.298], [8, 116.61999999999999, 171.35999999999999, 570.034, 585.1899999999999], [8, 116.61999999999999, 456.96, 591.9259999999999, 607.924], [8, 116.61999999999999, 345.695, 613.818, 629.816], [8, 116.61999999999999, 533.12, 635.7099999999999, 651.708], [8, 116.61999999999999, 258.22999999999996, 657.602, 672.7579999999999], [8, 273.7, 311.78, 708.9639999999999, 724.12], [9, 245.73499999999999, 349.85999999999996, 42.1, 62.308], [9, 50.574999999999996, 193.97, 70.728, 84.2], [9, 50.574999999999996, 157.07999999999998, 94.304, 108.618], [9, 51.765, 93.41499999999999, 119.564, 133.036], [9, 301.07, 351.05, 70.728, 84.2], [9, 301.07, 349.85999999999996, 94.304, 108.618], [9, 301.66499999999996, 358.78499999999997, 119.564, 132.194], [9, 396.27, 474.215, 119.564, 132.194], [9, 47.599999999999994, 219.55499999999998, 159.138, 173.452], [9, 110.07499999999999, 143.98999999999998, 203.76399999999998, 218.92], [9, 111.265, 500.98999999999995, 224.814, 239.97], [9, 111.265, 399.245, 247.548, 262.704], [9, 395.67499999999995, 428.995, 281.228, 295.542], [9, 50.574999999999996, 207.06, 307.33, 347.746], [9, 51.765, 354.025, 384.794, 399.95]]
2026-08-10 11:44:36,279 INFO     29 [qwen-vl-text] ═══ DONE ═══ 78 positions, pages=3, time=36.4s
2026-08-10 11:44:36,279 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:44:36,292 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:44:36,293 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:44:36,293 INFO     29 [qwen-vl-text] positions(88): [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:44:36,293 INFO     29 [qwen-vl-text] page grouping: [10, 11, 12], lines per page: [36, 34, 18]
2026-08-10 11:44:36,656 INFO     29 [qwen-vl-text] page=10, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:44:36,908 INFO     29 [qwen-vl-text] page=11, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:44:37,115 INFO     29 [qwen-vl-text] page=12, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:44:37,117 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1856
2026-08-10 11:44:37,117 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:44:37,117 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 301, \"bbox_end\": 388, \"encounter_dates\": [\"2025-07-31\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊病历\n科室:呼吸与危重症医学科\n姓名\n性别:女\n门诊\n联系方式\n年龄:63岁\n婚姻状况:其他\n2025-07-31 17:13 初诊记录\n主诉:SHR-1905V19随访\n现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年\n余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现\n气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行\n听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并\n规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可\n320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:\n20036.。近日无咳嗽咳痰,无胸闷气喘,无发热,无支气管哮喘急性发作\n今日回院行V19随访。\n既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。\n既往病史:\n1.2022.12.10肝囊肿,持续;\n2.2023.10.31鼻窦炎,持续;\n3.2023.10.31双肺良性小结节,持续;\n4.2023.11.03-2023.12.13,肺肺部感染;\n5.2024.03.01开始,白细胞数降低1级,持续;\n6.2024.01.10高脂血症,持续中\n过敏史:否认食物、药物过敏史。\n体格检查收缩压(mmHg):103;舒张压(mmHg):64\n其他体格检查:进行生命体征测量:体温:36.4℃,血压:\n103/64mmHg,呼吸:18次/分,脉搏:76次/分;\n查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见\n皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅\n大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。\n耳廓正常无畸形外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无\n鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿\n第1页\n门诊病历\n科室:呼吸与危重症医学科\n性别:女\n门诊\n联系方式:\n年龄:63岁\n婚姻状况:其他\n2025-07-31 17:13 初诊记录\n大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中\n肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动\n正常,左肺呼吸音清,未闻及粗干啰音。心律齐。双下肢无水肿。心音正\n常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛、反跳痛,无液\n波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触及,肾脏未触\n及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖器未查、肛门\n直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无异常,其他无\n异常。\n检验检查:已完善试验相关检验检查\n初步诊断:支气管哮喘\n处理:尿常规检查尿隐血,建议定期检查,必要时肾内科就诊。\n无临床试验安全性事,无新增 AE。\n新增合并用药:硫酸沙丁胺醇吸入气雾剂,2025.07.31-\n2025.078.31,400ug,once,吸入,用于支气管扩张检查。\nCM 跟踪:\n1、布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,\n320ug,bid,经口腔吸入,用于控制哮喘。\n2、硫酸沙丁胺醇气雾剂,2024.03.06开始,持续中,100ug,pm,经口腔吸\n入,控制哮喘急性发作。\n3.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po.用于治\n疗病史慢性浅表胃炎。\n处理:\n12025.05.13-2025.07.31 家用峰流速仪使用 ePRO 系统填写依从性大于\n80%,今日已解绑 ePRO 系统。\n2遵从临床试验方案完成 IgE,PK,ADA 采血,完成 ACQ-6,AQLQ 问卷填\n写。\n门诊病历\n科室:呼吸与危重症医学科\n姓名\n性别:女\n门诊\n联系\n年龄:63岁\n婚姻状况:其他\n2025-07-31 17:13 初诊记录\n3.患者于今日肺功能检查前已停用基础吸入药物布地奈德福莫特罗粉\n吸入剂大于12h,停药时间2025.07.30上午,具体时间不详。\n4.患者已于今日完成随访期随访。\n5.因患者未找到发放万托林,可能已经丢失故不予回收。\n6.嘱患者规律使用吸入药物布地奈德福莫特罗粉吸入剂,药物自备。\n医师\n门诊病历专用章\n※提醒:复诊时,请携带本病历记录,谢谢!※\n“若有高血压糖尿病诊断,建议您到居住地附近社康中心,建立居民健康档案”",
    "role": "user"
  }
]
2026-08-10 11:44:37,119 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:44:37.118+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 24, "failed": 0, "current": {"38277e3a94b011f1bd9827cf206dfa2d": {"id": "38277e3a94b011f1bd9827cf206dfa2d", "doc_id": "370244ae94b011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479740, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362000249, "task_type": "dataflow", "root_trace_id": "96cd8dab6bb7455194a762d3f16e1d52", "root_traceparent": "00-96cd8dab6bb7455194a762d3f16e1d52-1e133766dfd81337-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:44:44,777 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:44:44,777 INFO     29 [qwen-vl-text] LLM output (len=1197):
{
  "encounter_date": "2025-07-31",
  "chief_complaint": "SHR-1905V19随访",
  "present_illness": "发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:20036.。近日无咳嗽咳痰,无胸闷气喘,无发热,无支气管哮喘急性发作今日回院行V19随访。",
  "past_history": "否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。既往病史:1.2022.12.10肝囊肿,持续;2.2023.10.31鼻窦炎,持续;3.2023.10.31双肺良性小结节,持续;4.2023.11.03-2023.12.13,肺肺部感染;5.2024.03.01开始,白细胞数降低1级,持续;6.2024.01.10高脂血症,持续中。过敏史:否认食物、药物过敏史。",
  "diagnosis": "支气管哮喘",
  "treatment_plan": [
    "尿常规检查尿隐血,建议定期检查,必要时肾内科就诊。",
    "硫酸沙丁胺醇吸入气雾剂,2025.07.31-2025.078.31,400ug,once,吸入,用于支气管扩张检查。",
    "布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,320ug,bid,经口腔吸入,用于控制哮喘。",
    "硫酸沙丁胺醇气雾剂,2024.03.06开始,持续中,100ug,pm,经口腔吸入,控制哮喘急性发作。",
    "泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po.用于治疗病史慢性浅表胃炎。",
    "2025.05.13-2025.07.31 家用峰流速仪使用 ePRO 系统填写依从性大于80%,今日已解绑 ePRO 系统。",
    "遵从临床试验方案完成 IgE,PK,ADA 采血,完成 ACQ-6,AQLQ 问卷填写。",
    "患者于今日肺功能检查前已停用基础吸入药物布地奈德福莫特罗粉吸入剂大于12h,停药时间2025.07.30上午,具体时间不详。",
    "患者已于今日完成随访期随访。",
    "因患者未找到发放万托林,可能已经丢失故不予回收。",
    "嘱患者规律使用吸入药物布地奈德福莫特罗粉吸入剂,药物自备。"
  ]
}
2026-08-10 11:44:44,777 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-07-31]
2026-08-10 11:44:44,781 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2068148, prompt_len=1551
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共36行）
["门诊病历", "科室:呼吸与危重症医学科", "姓名", "性别:女", "门诊", "联系方式", "年龄:63岁", "婚姻状况:其他", "2025-07-31 17:13 初诊记录", "主诉:SHR-1905V19随访", "现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年", "余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现", "气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行", "听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并", "规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可", "320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:", "20036.。近日无咳嗽咳痰,无胸闷气喘,无发热,无支气管哮喘急性发作", "今日回院行V19随访。", "既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。", "既往病史:", "1.2022.12.10肝囊肿,持续;", "2.2023.10.31鼻窦炎,持续;", "3.2023.10.31双肺良性小结节,持续;", "4.2023.11.03-2023.12.13,肺肺部感染;", "5.2024.03.01开始,白细胞数降低1级,持续;", "6.2024.01.10高脂血症,持续中", "过敏史:否认食物、药物过敏史。", "体格检查收缩压(mmHg):103;舒张压(mmHg):64", "其他体格检查:进行生命体征测量:体温:36.4℃,血压:", "103/64mmHg,呼吸:18次/分,脉搏:76次/分;", "查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见", "皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅", "大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。", "耳廓正常无畸形外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无", "鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿", "第1页"]

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
2026-08-10 11:44:59,309 INFO     29 [qwen-vl-text] coord API raw response (len=2403):
[
	{"text": "门诊病历", "bbox": [418, 2, 583, 27]},
	{"text": "科室:呼吸与危重症医学科", "bbox": [114, 35, 339, 53]},
	{"text": "姓名", "bbox": [114, 65, 150, 82]},
	{"text": "性别:女", "bbox": [114, 94, 182, 110]},
	{"text": "门诊", "bbox": [507, 37, 553, 54]},
	{"text": "联系方式", "bbox": [507, 65, 583, 82]},
	{"text": "年龄:63岁", "bbox": [507, 94, 595, 110]},
	{"text": "婚姻状况:其他", "bbox": [655, 94, 779, 110]},
	{"text": "2025-07-31 17:13 初诊记录", "bbox": [110, 140, 379, 158]},
	{"text": "主诉:SHR-1905V19随访", "bbox": [110, 166, 394, 185]},
	{"text": "现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年", "bbox": [108, 192, 891, 212]},
	{"text": "余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现", "bbox": [208, 218, 891, 239]},
	{"text": "气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行", "bbox": [208, 244, 891, 265]},
	{"text": "听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并", "bbox": [208, 270, 891, 291]},
	{"text": "规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可", "bbox": [208, 296, 853, 317]},
	{"text": "320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:", "bbox": [208, 323, 826, 343]},
	{"text": "20036.。近日无咳嗽咳痰,无胸闷气喘,无发热,无支气管哮喘急性发作", "bbox": [208, 349, 891, 369]},
	{"text": "今日回院行V19随访。", "bbox": [208, 375, 426, 394]},
	{"text": "既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。", "bbox": [108, 401, 845, 420]},
	{"text": "既往病史:", "bbox": [208, 427, 308, 446]},
	{"text": "1.2022.12.10肝囊肿,持续;", "bbox": [208, 453, 476, 472]},
	{"text": "2.2023.10.31鼻窦炎,持续;", "bbox": [208, 479, 476, 498]},
	{"text": "3.2023.10.31双肺良性小结节,持续;", "bbox": [208, 505, 565, 524]},
	{"text": "4.2023.11.03-2023.12.13,肺肺部感染;", "bbox": [208, 531, 577, 550]},
	{"text": "5.2024.03.01开始,白细胞数降低1级,持续;", "bbox": [208, 557, 653, 576]},
	{"text": "6.2024.01.10高脂血症,持续中", "bbox": [208, 583, 513, 602]},
	{"text": "过敏史:否认食物、药物过敏史。", "bbox": [108, 610, 448, 629]},
	{"text": "体格检查收缩压(mmHg):103;舒张压(mmHg):64", "bbox": [108, 636, 640, 656]},
	{"text": "其他体格检查:进行生命体征测量:体温:36.4℃,血压:", "bbox": [208, 662, 737, 681]},
	{"text": "103/64mmHg,呼吸:18次/分,脉搏:76次/分;", "bbox": [208, 688, 679, 707]},
	{"text": "查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见", "bbox": [208, 713, 891, 733]},
	{"text": "皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅", "bbox": [208, 739, 891, 758]},
	{"text": "大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。", "bbox": [208, 765, 880, 784]},
	{"text": "耳廓正常无畸形外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无", "bbox": [208, 790, 891, 810]},
	{"text": "鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿", "bbox": [208, 816, 891, 836]},
	{"text": "第1页", "bbox": [472, 848, 535, 865]}
]
2026-08-10 11:44:59,310 INFO     29 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=14.5s
2026-08-10 11:44:59,310 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[418, 2, 583, 27]
2026-08-10 11:44:59,310 INFO     29 [qwen-vl-text] coord item[1]: text=科室:呼吸与危重症医学科, bbox=[114, 35, 339, 53]
2026-08-10 11:44:59,310 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[114, 65, 150, 82]
2026-08-10 11:44:59,310 INFO     29 [qwen-vl-text] coord item[3]: text=性别:女, bbox=[114, 94, 182, 110]
2026-08-10 11:44:59,310 INFO     29 [qwen-vl-text] coord item[4]: text=门诊, bbox=[507, 37, 553, 54]
2026-08-10 11:44:59,310 INFO     29 [qwen-vl-text] coord item[5]: text=联系方式, bbox=[507, 65, 583, 82]
2026-08-10 11:44:59,310 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:63岁, bbox=[507, 94, 595, 110]
2026-08-10 11:44:59,310 INFO     29 [qwen-vl-text] coord item[7]: text=婚姻状况:其他, bbox=[655, 94, 779, 110]
2026-08-10 11:44:59,310 INFO     29 [qwen-vl-text] coord item[8]: text=2025-07-31 17:13 初诊记录, bbox=[110, 140, 379, 158]
2026-08-10 11:44:59,310 INFO     29 [qwen-vl-text] coord item[9]: text=主诉:SHR-1905V19随访, bbox=[110, 166, 394, 185]
2026-08-10 11:44:59,310 INFO     29 [qwen-vl-text] coord item[10]: text=现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年, bbox=[108, 192, 891, 212]
2026-08-10 11:44:59,310 INFO     29 [qwen-vl-text] coord item[11]: text=余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现, bbox=[208, 218, 891, 239]
2026-08-10 11:44:59,310 INFO     29 [qwen-vl-text] coord item[12]: text=气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行, bbox=[208, 244, 891, 265]
2026-08-10 11:44:59,311 INFO     29 [qwen-vl-text] coord item[13]: text=听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并, bbox=[208, 270, 891, 291]
2026-08-10 11:44:59,311 INFO     29 [qwen-vl-text] coord item[14]: text=规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可, bbox=[208, 296, 853, 317]
2026-08-10 11:44:59,311 INFO     29 [qwen-vl-text] coord item[15]: text=320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:, bbox=[208, 323, 826, 343]
2026-08-10 11:44:59,311 INFO     29 [qwen-vl-text] coord item[16]: text=20036.。近日无咳嗽咳痰,无胸闷气喘,无发热,无支气管哮喘急性发作, bbox=[208, 349, 891, 369]
2026-08-10 11:44:59,311 INFO     29 [qwen-vl-text] coord item[17]: text=今日回院行V19随访。, bbox=[208, 375, 426, 394]
2026-08-10 11:44:59,311 INFO     29 [qwen-vl-text] coord item[18]: text=既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。, bbox=[108, 401, 845, 420]
2026-08-10 11:44:59,311 INFO     29 [qwen-vl-text] coord item[19]: text=既往病史:, bbox=[208, 427, 308, 446]
2026-08-10 11:44:59,311 INFO     29 [qwen-vl-text] coord item[20]: text=1.2022.12.10肝囊肿,持续;, bbox=[208, 453, 476, 472]
2026-08-10 11:44:59,311 INFO     29 [qwen-vl-text] coord item[21]: text=2.2023.10.31鼻窦炎,持续;, bbox=[208, 479, 476, 498]
2026-08-10 11:44:59,311 INFO     29 [qwen-vl-text] coord item[22]: text=3.2023.10.31双肺良性小结节,持续;, bbox=[208, 505, 565, 524]
2026-08-10 11:44:59,311 INFO     29 [qwen-vl-text] coord item[23]: text=4.2023.11.03-2023.12.13,肺肺部感染;, bbox=[208, 531, 577, 550]
2026-08-10 11:44:59,311 INFO     29 [qwen-vl-text] coord item[24]: text=5.2024.03.01开始,白细胞数降低1级,持续;, bbox=[208, 557, 653, 576]
2026-08-10 11:44:59,311 INFO     29 [qwen-vl-text] coord item[25]: text=6.2024.01.10高脂血症,持续中, bbox=[208, 583, 513, 602]
2026-08-10 11:44:59,311 INFO     29 [qwen-vl-text] coord item[26]: text=过敏史:否认食物、药物过敏史。, bbox=[108, 610, 448, 629]
2026-08-10 11:44:59,311 INFO     29 [qwen-vl-text] coord item[27]: text=体格检查收缩压(mmHg):103;舒张压(mmHg):64, bbox=[108, 636, 640, 656]
2026-08-10 11:44:59,311 INFO     29 [qwen-vl-text] coord item[28]: text=其他体格检查:进行生命体征测量:体温:36.4℃,血压:, bbox=[208, 662, 737, 681]
2026-08-10 11:44:59,311 INFO     29 [qwen-vl-text] coord item[29]: text=103/64mmHg,呼吸:18次/分,脉搏:76次/分;, bbox=[208, 688, 679, 707]
2026-08-10 11:44:59,311 INFO     29 [qwen-vl-text] coord item[30]: text=查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见, bbox=[208, 713, 891, 733]
2026-08-10 11:44:59,311 INFO     29 [qwen-vl-text] coord item[31]: text=皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅, bbox=[208, 739, 891, 758]
2026-08-10 11:44:59,311 INFO     29 [qwen-vl-text] coord item[32]: text=大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。, bbox=[208, 765, 880, 784]
2026-08-10 11:44:59,311 INFO     29 [qwen-vl-text] coord item[33]: text=耳廓正常无畸形外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无, bbox=[208, 790, 891, 810]
2026-08-10 11:44:59,311 INFO     29 [qwen-vl-text] coord item[34]: text=鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿, bbox=[208, 816, 891, 836]
2026-08-10 11:44:59,311 INFO     29 [qwen-vl-text] coord item[35]: text=第1页, bbox=[472, 848, 535, 865]
2026-08-10 11:44:59,313 INFO     29 [qwen-vl-text] page=10 — 36/36 coords, api_time=14.5s
2026-08-10 11:44:59,318 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1658218, prompt_len=1460
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共34行）
["门诊病历", "科室:呼吸与危重症医学科", "性别:女", "门诊", "联系方式:", "年龄:63岁", "婚姻状况:其他", "2025-07-31 17:13 初诊记录", "大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中", "肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动", "正常,左肺呼吸音清,未闻及粗干啰音。心律齐。双下肢无水肿。心音正", "常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛、反跳痛,无液", "波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触及,肾脏未触", "及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖器未查、肛门", "直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无异常,其他无", "异常。", "检验检查:已完善试验相关检验检查", "初步诊断:支气管哮喘", "处理:尿常规检查尿隐血,建议定期检查,必要时肾内科就诊。", "无临床试验安全性事,无新增 AE。", "新增合并用药:硫酸沙丁胺醇吸入气雾剂,2025.07.31-", "2025.078.31,400ug,once,吸入,用于支气管扩张检查。", "CM 跟踪:", "1、布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,", "320ug,bid,经口腔吸入,用于控制哮喘。", "2、硫酸沙丁胺醇气雾剂,2024.03.06开始,持续中,100ug,pm,经口腔吸", "入,控制哮喘急性发作。", "3.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po.用于治", "疗病史慢性浅表胃炎。", "处理:", "12025.05.13-2025.07.31 家用峰流速仪使用 ePRO 系统填写依从性大于", "80%,今日已解绑 ePRO 系统。", "2遵从临床试验方案完成 IgE,PK,ADA 采血,完成 ACQ-6,AQLQ 问卷填", "写。"]

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
2026-08-10 11:45:11,735 INFO     29 [qwen-vl-text] coord API raw response (len=2231):
[
	{"text": "门诊病历", "bbox": [407, 20, 583, 45]},
	{"text": "科室:呼吸与危重症医学科", "bbox": [76, 55, 319, 72]},
	{"text": "性别:女", "bbox": [76, 114, 150, 130]},
	{"text": "门诊", "bbox": [500, 55, 554, 72]},
	{"text": "联系方式:", "bbox": [500, 84, 588, 101]},
	{"text": "年龄:63岁", "bbox": [500, 114, 595, 130]},
	{"text": "婚姻状况:其他", "bbox": [660, 114, 793, 130]},
	{"text": "2025-07-31 17:13 初诊记录", "bbox": [70, 161, 359, 179]},
	{"text": "大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中", "bbox": [174, 188, 912, 208]},
	{"text": "肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动", "bbox": [174, 214, 912, 234]},
	{"text": "正常,左肺呼吸音清,未闻及粗干啰音。心律齐。双下肢无水肿。心音正", "bbox": [174, 240, 912, 260]},
	{"text": "常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛、反跳痛,无液", "bbox": [174, 266, 912, 286]},
	{"text": "波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触及,肾脏未触", "bbox": [174, 292, 912, 312]},
	{"text": "及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖器未查、肛门", "bbox": [174, 318, 912, 340]},
	{"text": "直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无异常,其他无", "bbox": [174, 346, 912, 366]},
	{"text": "异常。", "bbox": [174, 378, 234, 397]},
	{"text": "检验检查:已完善试验相关检验检查", "bbox": [68, 405, 444, 425]},
	{"text": "初步诊断:支气管哮喘", "bbox": [68, 432, 295, 452]},
	{"text": "处理:尿常规检查尿隐血,建议定期检查,必要时肾内科就诊。", "bbox": [68, 460, 772, 480]},
	{"text": "无临床试验安全性事,无新增 AE。", "bbox": [172, 487, 541, 506]},
	{"text": "新增合并用药:硫酸沙丁胺醇吸入气雾剂,2025.07.31-", "bbox": [172, 514, 758, 534]},
	{"text": "2025.078.31,400ug,once,吸入,用于支气管扩张检查。", "bbox": [172, 540, 763, 561]},
	{"text": "CM 跟踪:", "bbox": [172, 568, 273, 587]},
	{"text": "1、布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,", "bbox": [172, 595, 780, 615]},
	{"text": "320ug,bid,经口腔吸入,用于控制哮喘。", "bbox": [172, 622, 583, 642]},
	{"text": "2、硫酸沙丁胺醇气雾剂,2024.03.06开始,持续中,100ug,pm,经口腔吸", "bbox": [172, 650, 912, 670]},
	{"text": "入,控制哮喘急性发作。", "bbox": [172, 677, 430, 697]},
	{"text": "3.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po.用于治", "bbox": [172, 704, 912, 724]},
	{"text": "疗病史慢性浅表胃炎。", "bbox": [172, 731, 405, 751]},
	{"text": "处理:", "bbox": [172, 760, 227, 779]},
	{"text": "12025.05.13-2025.07.31 家用峰流速仪使用 ePRO 系统填写依从性大于", "bbox": [172, 787, 895, 807]},
	{"text": "80%,今日已解绑 ePRO 系统。", "bbox": [172, 814, 495, 834]},
	{"text": "2遵从临床试验方案完成 IgE,PK,ADA 采血,完成 ACQ-6,AQLQ 问卷填", "bbox": [172, 841, 912, 861]},
	{"text": "写。", "bbox": [172, 868, 204, 887]}
]
2026-08-10 11:45:11,736 INFO     29 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=12.4s
2026-08-10 11:45:11,736 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[407, 20, 583, 45]
2026-08-10 11:45:11,736 INFO     29 [qwen-vl-text] coord item[1]: text=科室:呼吸与危重症医学科, bbox=[76, 55, 319, 72]
2026-08-10 11:45:11,736 INFO     29 [qwen-vl-text] coord item[2]: text=性别:女, bbox=[76, 114, 150, 130]
2026-08-10 11:45:11,736 INFO     29 [qwen-vl-text] coord item[3]: text=门诊, bbox=[500, 55, 554, 72]
2026-08-10 11:45:11,736 INFO     29 [qwen-vl-text] coord item[4]: text=联系方式:, bbox=[500, 84, 588, 101]
2026-08-10 11:45:11,736 INFO     29 [qwen-vl-text] coord item[5]: text=年龄:63岁, bbox=[500, 114, 595, 130]
2026-08-10 11:45:11,737 INFO     29 [qwen-vl-text] coord item[6]: text=婚姻状况:其他, bbox=[660, 114, 793, 130]
2026-08-10 11:45:11,737 INFO     29 [qwen-vl-text] coord item[7]: text=2025-07-31 17:13 初诊记录, bbox=[70, 161, 359, 179]
2026-08-10 11:45:11,737 INFO     29 [qwen-vl-text] coord item[8]: text=大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中, bbox=[174, 188, 912, 208]
2026-08-10 11:45:11,737 INFO     29 [qwen-vl-text] coord item[9]: text=肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动, bbox=[174, 214, 912, 234]
2026-08-10 11:45:11,737 INFO     29 [qwen-vl-text] coord item[10]: text=正常,左肺呼吸音清,未闻及粗干啰音。心律齐。双下肢无水肿。心音正, bbox=[174, 240, 912, 260]
2026-08-10 11:45:11,737 INFO     29 [qwen-vl-text] coord item[11]: text=常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛、反跳痛,无液, bbox=[174, 266, 912, 286]
2026-08-10 11:45:11,737 INFO     29 [qwen-vl-text] coord item[12]: text=波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触及,肾脏未触, bbox=[174, 292, 912, 312]
2026-08-10 11:45:11,737 INFO     29 [qwen-vl-text] coord item[13]: text=及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖器未查、肛门, bbox=[174, 318, 912, 340]
2026-08-10 11:45:11,737 INFO     29 [qwen-vl-text] coord item[14]: text=直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无异常,其他无, bbox=[174, 346, 912, 366]
2026-08-10 11:45:11,737 INFO     29 [qwen-vl-text] coord item[15]: text=异常。, bbox=[174, 378, 234, 397]
2026-08-10 11:45:11,738 INFO     29 [qwen-vl-text] coord item[16]: text=检验检查:已完善试验相关检验检查, bbox=[68, 405, 444, 425]
2026-08-10 11:45:11,738 INFO     29 [qwen-vl-text] coord item[17]: text=初步诊断:支气管哮喘, bbox=[68, 432, 295, 452]
2026-08-10 11:45:11,738 INFO     29 [qwen-vl-text] coord item[18]: text=处理:尿常规检查尿隐血,建议定期检查,必要时肾内科就诊。, bbox=[68, 460, 772, 480]
2026-08-10 11:45:11,738 INFO     29 [qwen-vl-text] coord item[19]: text=无临床试验安全性事,无新增 AE。, bbox=[172, 487, 541, 506]
2026-08-10 11:45:11,738 INFO     29 [qwen-vl-text] coord item[20]: text=新增合并用药:硫酸沙丁胺醇吸入气雾剂,2025.07.31-, bbox=[172, 514, 758, 534]
2026-08-10 11:45:11,738 INFO     29 [qwen-vl-text] coord item[21]: text=2025.078.31,400ug,once,吸入,用于支气管扩张检查。, bbox=[172, 540, 763, 561]
2026-08-10 11:45:11,738 INFO     29 [qwen-vl-text] coord item[22]: text=CM 跟踪:, bbox=[172, 568, 273, 587]
2026-08-10 11:45:11,738 INFO     29 [qwen-vl-text] coord item[23]: text=1、布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,, bbox=[172, 595, 780, 615]
2026-08-10 11:45:11,738 INFO     29 [qwen-vl-text] coord item[24]: text=320ug,bid,经口腔吸入,用于控制哮喘。, bbox=[172, 622, 583, 642]
2026-08-10 11:45:11,738 INFO     29 [qwen-vl-text] coord item[25]: text=2、硫酸沙丁胺醇气雾剂,2024.03.06开始,持续中,100ug,pm,经口腔吸, bbox=[172, 650, 912, 670]
2026-08-10 11:45:11,738 INFO     29 [qwen-vl-text] coord item[26]: text=入,控制哮喘急性发作。, bbox=[172, 677, 430, 697]
2026-08-10 11:45:11,738 INFO     29 [qwen-vl-text] coord item[27]: text=3.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po.用于治, bbox=[172, 704, 912, 724]
2026-08-10 11:45:11,738 INFO     29 [qwen-vl-text] coord item[28]: text=疗病史慢性浅表胃炎。, bbox=[172, 731, 405, 751]
2026-08-10 11:45:11,738 INFO     29 [qwen-vl-text] coord item[29]: text=处理:, bbox=[172, 760, 227, 779]
2026-08-10 11:45:11,738 INFO     29 [qwen-vl-text] coord item[30]: text=12025.05.13-2025.07.31 家用峰流速仪使用 ePRO 系统填写依从性大于, bbox=[172, 787, 895, 807]
2026-08-10 11:45:11,738 INFO     29 [qwen-vl-text] coord item[31]: text=80%,今日已解绑 ePRO 系统。, bbox=[172, 814, 495, 834]
2026-08-10 11:45:11,739 INFO     29 [qwen-vl-text] coord item[32]: text=2遵从临床试验方案完成 IgE,PK,ADA 采血,完成 ACQ-6,AQLQ 问卷填, bbox=[172, 841, 912, 861]
2026-08-10 11:45:11,739 INFO     29 [qwen-vl-text] coord item[33]: text=写。, bbox=[172, 868, 204, 887]
2026-08-10 11:45:11,740 INFO     29 [qwen-vl-text] page=11 — 34/34 coords, api_time=12.4s
2026-08-10 11:45:11,745 INFO     29 [qwen-vl-text] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=939736, prompt_len=946
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共18行）
["门诊病历", "科室:呼吸与危重症医学科", "姓名", "性别:女", "门诊", "联系", "年龄:63岁", "婚姻状况:其他", "2025-07-31 17:13 初诊记录", "3.患者于今日肺功能检查前已停用基础吸入药物布地奈德福莫特罗粉", "吸入剂大于12h,停药时间2025.07.30上午,具体时间不详。", "4.患者已于今日完成随访期随访。", "5.因患者未找到发放万托林,可能已经丢失故不予回收。", "6.嘱患者规律使用吸入药物布地奈德福莫特罗粉吸入剂,药物自备。", "医师", "门诊病历专用章", "※提醒:复诊时,请携带本病历记录,谢谢!※", "“若有高血压糖尿病诊断,建议您到居住地附近社康中心,建立居民健康档案”"]

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
2026-08-10 11:45:18,051 INFO     29 [qwen-vl-text] coord API raw response (len=1060):
[
	{"text": "门诊病历", "bbox": [417, 28, 592, 52]},
	{"text": "科室:呼吸与危重症医学科", "bbox": [93, 60, 333, 77]},
	{"text": "姓名", "bbox": [93, 87, 115, 104]},
	{"text": "性别:女", "bbox": [93, 115, 164, 132]},
	{"text": "门诊", "bbox": [512, 60, 564, 77]},
	{"text": "联系", "bbox": [512, 87, 552, 104]},
	{"text": "年龄:63岁", "bbox": [512, 115, 604, 132]},
	{"text": "婚姻状况:其他", "bbox": [668, 115, 797, 132]},
	{"text": "2025-07-31 17:13 初诊记录", "bbox": [90, 161, 375, 179]},
	{"text": "3.患者于今日肺功能检查前已停用基础吸入药物布地奈德福莫特罗粉", "bbox": [191, 187, 900, 206]},
	{"text": "吸入剂大于12h,停药时间2025.07.30上午,具体时间不详。", "bbox": [191, 211, 795, 230]},
	{"text": "4.患者已于今日完成随访期随访。", "bbox": [191, 238, 534, 257]},
	{"text": "5.因患者未找到发放万托林,可能已经丢失故不予回收。", "bbox": [191, 264, 769, 283]},
	{"text": "6.嘱患者规律使用吸入药物布地奈德福莫特罗粉吸入剂,药物自备。", "bbox": [191, 290, 888, 309]},
	{"text": "医师", "bbox": [668, 382, 722, 400]},
	{"text": "门诊病历专用章", "bbox": [103, 423, 337, 448]},
	{"text": "※提醒:复诊时,请携带本病历记录,谢谢!※", "bbox": [95, 502, 597, 520]},
	{"text": "“若有高血压糖尿病诊断,建议您到居住地附近社康中心,建立居民健康档案”", "bbox": [97, 531, 911, 550]}
]
2026-08-10 11:45:18,052 INFO     29 [qwen-vl-text] coord API: raw_items=18, valid_items=18, elapsed=6.3s
2026-08-10 11:45:18,052 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[417, 28, 592, 52]
2026-08-10 11:45:18,052 INFO     29 [qwen-vl-text] coord item[1]: text=科室:呼吸与危重症医学科, bbox=[93, 60, 333, 77]
2026-08-10 11:45:18,053 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[93, 87, 115, 104]
2026-08-10 11:45:18,053 INFO     29 [qwen-vl-text] coord item[3]: text=性别:女, bbox=[93, 115, 164, 132]
2026-08-10 11:45:18,053 INFO     29 [qwen-vl-text] coord item[4]: text=门诊, bbox=[512, 60, 564, 77]
2026-08-10 11:45:18,053 INFO     29 [qwen-vl-text] coord item[5]: text=联系, bbox=[512, 87, 552, 104]
2026-08-10 11:45:18,053 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:63岁, bbox=[512, 115, 604, 132]
2026-08-10 11:45:18,053 INFO     29 [qwen-vl-text] coord item[7]: text=婚姻状况:其他, bbox=[668, 115, 797, 132]
2026-08-10 11:45:18,053 INFO     29 [qwen-vl-text] coord item[8]: text=2025-07-31 17:13 初诊记录, bbox=[90, 161, 375, 179]
2026-08-10 11:45:18,053 INFO     29 [qwen-vl-text] coord item[9]: text=3.患者于今日肺功能检查前已停用基础吸入药物布地奈德福莫特罗粉, bbox=[191, 187, 900, 206]
2026-08-10 11:45:18,053 INFO     29 [qwen-vl-text] coord item[10]: text=吸入剂大于12h,停药时间2025.07.30上午,具体时间不详。, bbox=[191, 211, 795, 230]
2026-08-10 11:45:18,053 INFO     29 [qwen-vl-text] coord item[11]: text=4.患者已于今日完成随访期随访。, bbox=[191, 238, 534, 257]
2026-08-10 11:45:18,053 INFO     29 [qwen-vl-text] coord item[12]: text=5.因患者未找到发放万托林,可能已经丢失故不予回收。, bbox=[191, 264, 769, 283]
2026-08-10 11:45:18,053 INFO     29 [qwen-vl-text] coord item[13]: text=6.嘱患者规律使用吸入药物布地奈德福莫特罗粉吸入剂,药物自备。, bbox=[191, 290, 888, 309]
2026-08-10 11:45:18,053 INFO     29 [qwen-vl-text] coord item[14]: text=医师, bbox=[668, 382, 722, 400]
2026-08-10 11:45:18,053 INFO     29 [qwen-vl-text] coord item[15]: text=门诊病历专用章, bbox=[103, 423, 337, 448]
2026-08-10 11:45:18,053 INFO     29 [qwen-vl-text] coord item[16]: text=※提醒:复诊时,请携带本病历记录,谢谢!※, bbox=[95, 502, 597, 520]
2026-08-10 11:45:18,053 INFO     29 [qwen-vl-text] coord item[17]: text=“若有高血压糖尿病诊断,建议您到居住地附近社康中心,建立居民健康档案”, bbox=[97, 531, 911, 550]
2026-08-10 11:45:18,054 INFO     29 [qwen-vl-text] page=12 — 18/18 coords, api_time=6.3s
2026-08-10 11:45:18,054 INFO     29 [qwen-vl-text] new_positions (88):
[[10, 248.70999999999998, 346.885, 1.684, 22.733999999999998], [10, 67.83, 201.70499999999998, 29.47, 44.626], [10, 67.83, 89.25, 54.73, 69.044], [10, 67.83, 108.28999999999999, 79.148, 92.61999999999999], [10, 301.66499999999996, 329.03499999999997, 31.154, 45.467999999999996], [10, 301.66499999999996, 346.885, 54.73, 69.044], [10, 301.66499999999996, 354.025, 79.148, 92.61999999999999], [10, 389.72499999999997, 463.505, 79.148, 92.61999999999999], [10, 65.45, 225.505, 117.88, 133.036], [10, 65.45, 234.42999999999998, 139.772, 155.76999999999998], [10, 64.25999999999999, 530.145, 161.664, 178.504], [10, 123.75999999999999, 530.145, 183.55599999999998, 201.238], [10, 123.75999999999999, 530.145, 205.44799999999998, 223.13], [10, 123.75999999999999, 530.145, 227.34, 245.022], [10, 123.75999999999999, 507.53499999999997, 249.232, 266.914], [10, 123.75999999999999, 491.46999999999997, 271.966, 288.806], [10, 123.75999999999999, 530.145, 293.858, 310.698], [10, 123.75999999999999, 253.47, 315.75, 331.748], [10, 64.25999999999999, 502.775, 337.642, 353.64], [10, 123.75999999999999, 183.26, 359.534, 375.532], [10, 123.75999999999999, 283.21999999999997, 381.426, 397.424], [10, 123.75999999999999, 283.21999999999997, 403.318, 419.316], [10, 123.75999999999999, 336.175, 425.21, 441.20799999999997], [10, 123.75999999999999, 343.315, 447.102, 463.09999999999997], [10, 123.75999999999999, 388.53499999999997, 468.99399999999997, 484.99199999999996], [10, 123.75999999999999, 305.235, 490.88599999999997, 506.88399999999996], [10, 64.25999999999999, 266.56, 513.62, 529.6179999999999], [10, 64.25999999999999, 380.79999999999995, 535.512, 552.352], [10, 123.75999999999999, 438.515, 557.404, 573.4019999999999], [10, 123.75999999999999, 404.005, 579.2959999999999, 595.294], [10, 123.75999999999999, 530.145, 600.346, 617.1859999999999], [10, 123.75999999999999, 530.145, 622.2379999999999, 638.236], [10, 123.75999999999999, 523.6, 644.13, 660.1279999999999], [10, 123.75999999999999, 530.145, 665.18, 682.02], [10, 123.75999999999999, 530.145, 687.072, 703.9119999999999], [10, 280.84, 318.325, 714.016, 728.3299999999999], [11, 242.165, 346.885, 16.84, 37.89], [11, 45.22, 189.80499999999998, 46.309999999999995, 60.623999999999995], [11, 45.22, 89.25, 95.988, 109.46], [11, 297.5, 329.63, 46.309999999999995, 60.623999999999995], [11, 297.5, 349.85999999999996, 70.728, 85.042], [11, 297.5, 354.025, 95.988, 109.46], [11, 392.7, 471.835, 95.988, 109.46], [11, 41.65, 213.605, 135.56199999999998, 150.718], [11, 103.53, 542.64, 158.296, 175.136], [11, 103.53, 542.64, 180.188, 197.028], [11, 103.53, 542.64, 202.07999999999998, 218.92], [11, 103.53, 542.64, 223.97199999999998, 240.81199999999998], [11, 103.53, 542.64, 245.864, 262.704], [11, 103.53, 542.64, 267.756, 286.28], [11, 103.53, 542.64, 291.332, 308.17199999999997], [11, 103.53, 139.23, 318.276, 334.274], [11, 40.46, 264.18, 341.01, 357.84999999999997], [11, 40.46, 175.525, 363.74399999999997, 380.584], [11, 40.46, 459.34, 387.32, 404.15999999999997], [11, 102.33999999999999, 321.895, 410.054, 426.05199999999996], [11, 102.33999999999999, 451.01, 432.788, 449.628], [11, 102.33999999999999, 453.98499999999996, 454.68, 472.36199999999997], [11, 102.33999999999999, 162.435, 478.256, 494.25399999999996], [11, 102.33999999999999, 464.09999999999997, 500.99, 517.8299999999999], [11, 102.33999999999999, 346.885, 523.7239999999999, 540.564], [11, 102.33999999999999, 542.64, 547.3, 564.14], [11, 102.33999999999999, 255.85, 570.034, 586.874], [11, 102.33999999999999, 542.64, 592.768, 609.608], [11, 102.33999999999999, 240.975, 615.502, 632.342], [11, 102.33999999999999, 135.065, 639.92, 655.918], [11, 102.33999999999999, 532.525, 662.654, 679.494], [11, 102.33999999999999, 294.525, 685.3879999999999, 702.228], [11, 102.33999999999999, 542.64, 708.122, 724.962], [11, 102.33999999999999, 121.38, 730.856, 746.8539999999999], [12, 248.11499999999998, 352.24, 23.576, 43.784], [12, 55.335, 198.135, 50.519999999999996, 64.834], [12, 55.335, 68.425, 73.25399999999999, 87.568], [12, 55.335, 97.58, 96.83, 111.14399999999999], [12, 304.64, 335.58, 50.519999999999996, 64.834], [12, 304.64, 328.44, 73.25399999999999, 87.568], [12, 304.64, 359.38, 96.83, 111.14399999999999], [12, 397.46, 474.215, 96.83, 111.14399999999999], [12, 53.55, 223.125, 135.56199999999998, 150.718], [12, 113.645, 535.5, 157.454, 173.452], [12, 113.645, 473.025, 177.662, 193.66], [12, 113.645, 317.72999999999996, 200.396, 216.394], [12, 113.645, 457.555, 222.28799999999998, 238.286], [12, 113.645, 528.36, 244.17999999999998, 260.178], [12, 397.46, 429.59, 321.644, 336.8], [12, 61.285, 200.515, 356.166, 377.216], [12, 56.525, 355.215, 422.68399999999997, 437.84], [12, 57.714999999999996, 542.045, 447.102, 463.09999999999997]]
2026-08-10 11:45:18,054 INFO     29 [qwen-vl-text] ═══ DONE ═══ 88 positions, pages=3, time=41.8s
2026-08-10 11:45:18,055 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:45:18,067 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:45:18,067 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:45:18,067 INFO     29 [qwen-vl-text] positions(37): [[13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:45:18,067 INFO     29 [qwen-vl-text] page grouping: [13], lines per page: [37]
2026-08-10 11:45:18,396 INFO     29 [qwen-vl-text] page=13, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:45:18,402 INFO     29 [qwen-vl-text] LLM extraction start, text_len=783
2026-08-10 11:45:18,402 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:45:18,402 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 390, \"bbox_end\": 426, \"encounter_dates\": [\"2025-10-25\"], \"department\": \"呼吸内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊\n姓名：\n门(急)诊初诊病历\n性别：女\n科室：呼吸内科门诊\n年龄：63岁\n就诊日期：2025-10-25 15:22\n主诉：支气管哮喘复诊\n现病史：患者支气管哮喘复诊，目前规律吸入布地奈德福莫特罗320ug 一次1吸，\n一天2次。目前诉有咳嗽、咳痰，有气促感，无胸闷，无发热，无鼻塞、流涕，无咯\n血、痰中带血，无头痛、头晕、视物旋转，无饮水呛咳，无咽痛、腹痛、腹胀等不\n适。未予处理及就医。现患者为求进一步诊治，故至我院科门诊就医。\n既往史：否认高血压、否认糖尿病、否认冠心病等慢性疾病病史，否认肝炎、结核\n等传染病史，否认手术外伤输血史 过敏史：无食物、药物过敏史。。否认饮酒史。\n个人史：已婚已育\n家族史：否认家族病史。\n体格检查：T：36.8℃ P：87次/分 R：21次/分 BP：108/73mmHg 指脉氧：\n9%。神志清楚，精神尚可，呼吸平顺，口唇无发绀，咽部无充血，扁桃体无肿大，\n双侧颈静脉无怒张，双肺呼吸音粗，双肺可闻及干啰音，双肺未闻及湿性啰音及胸膜\n摩擦音。心率87次/分，律齐，各瓣膜未闻及明显病理性杂音。腹部平软，全腹部无\n玉痛，反跳痛，肠鸣音正常。四肢运动自如，双下肢无水肿。\n辅助检查：患者自行购买布地奈德福莫特罗320ug 一次1吸，一天2次。\n初步诊断：\n西医诊断：1.支气管哮喘(急性发作期)\n处理意见：\n醋酸泼尼松片（国基）(5mg*100片) 20.000mg\n1次/天 口服\n12.00片\n硫酸沙丁胺醇吸入气雾剂（省3、国基）(200揿：\n100μg) 200.000μg\n1次/天 吸入\n1.00瓶\n建议：建议患者结果回报后请及时至我科门诊复诊，若出现病情变化或病情加重\n无好转等，请及时至急诊科门诊复诊。\n温馨提示：1.请妥善保管好病历及各种检查检验报告单。\n2.复诊时，请携带本病历记录，谢谢！\n第1页(共1页)",
    "role": "user"
  }
]
2026-08-10 11:45:18,405 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:45:18.403+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 24, "failed": 0, "current": {"38277e3a94b011f1bd9827cf206dfa2d": {"id": "38277e3a94b011f1bd9827cf206dfa2d", "doc_id": "370244ae94b011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479740, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362000249, "task_type": "dataflow", "root_trace_id": "96cd8dab6bb7455194a762d3f16e1d52", "root_traceparent": "00-96cd8dab6bb7455194a762d3f16e1d52-1e133766dfd81337-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:45:22,688 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:45:22,689 INFO     29 [qwen-vl-text] LLM output (len=693):
{
  "encounter_date": "2025-10-25",
  "chief_complaint": "支气管哮喘复诊",
  "present_illness": "患者支气管哮喘复诊，目前规律吸入布地奈德福莫特罗320ug 一次1吸，一天2次。目前诉有咳嗽、咳痰，有气促感，无胸闷，无发热，无鼻塞、流涕，无咯血、痰中带血，无头痛、头晕、视物旋转，无饮水呛咳，无咽痛、腹痛、腹胀等不适。未予处理及就医。现患者为求进一步诊治，故至我院科门诊就医。",
  "past_history": "否认高血压、否认糖尿病、否认冠心病等慢性疾病病史，否认肝炎、结核等传染病史，否认手术外伤输血史 过敏史：无食物、药物过敏史。。否认饮酒史。",
  "diagnosis": "西医诊断：1.支气管哮喘(急性发作期)",
  "treatment_plan": [
    {
      "drug_name": "醋酸泼尼松片（国基）",
      "dosage": "20.000mg",
      "frequency": "1次/天",
      "route": "口服",
      "quantity": "12.00片"
    },
    {
      "drug_name": "硫酸沙丁胺醇吸入气雾剂（省3、国基）",
      "dosage": "200.000μg",
      "frequency": "1次/天",
      "route": "吸入",
      "quantity": "1.00瓶"
    }
  ]
}
2026-08-10 11:45:22,689 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-10-25]
2026-08-10 11:45:22,695 INFO     29 [qwen-vl-text] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2599809, prompt_len=1507
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共37行）
["门诊", "姓名：", "门(急)诊初诊病历", "性别：女", "科室：呼吸内科门诊", "年龄：63岁", "就诊日期：2025-10-25 15:22", "主诉：支气管哮喘复诊", "现病史：患者支气管哮喘复诊，目前规律吸入布地奈德福莫特罗320ug 一次1吸，", "一天2次。目前诉有咳嗽、咳痰，有气促感，无胸闷，无发热，无鼻塞、流涕，无咯", "血、痰中带血，无头痛、头晕、视物旋转，无饮水呛咳，无咽痛、腹痛、腹胀等不", "适。未予处理及就医。现患者为求进一步诊治，故至我院科门诊就医。", "既往史：否认高血压、否认糖尿病、否认冠心病等慢性疾病病史，否认肝炎、结核", "等传染病史，否认手术外伤输血史 过敏史：无食物、药物过敏史。。否认饮酒史。", "个人史：已婚已育", "家族史：否认家族病史。", "体格检查：T：36.8℃ P：87次/分 R：21次/分 BP：108/73mmHg 指脉氧：", "9%。神志清楚，精神尚可，呼吸平顺，口唇无发绀，咽部无充血，扁桃体无肿大，", "双侧颈静脉无怒张，双肺呼吸音粗，双肺可闻及干啰音，双肺未闻及湿性啰音及胸膜", "摩擦音。心率87次/分，律齐，各瓣膜未闻及明显病理性杂音。腹部平软，全腹部无", "玉痛，反跳痛，肠鸣音正常。四肢运动自如，双下肢无水肿。", "辅助检查：患者自行购买布地奈德福莫特罗320ug 一次1吸，一天2次。", "初步诊断：", "西医诊断：1.支气管哮喘(急性发作期)", "处理意见：", "醋酸泼尼松片（国基）(5mg*100片) 20.000mg", "1次/天 口服", "12.00片", "硫酸沙丁胺醇吸入气雾剂（省3、国基）(200揿：", "100μg) 200.000μg", "1次/天 吸入", "1.00瓶", "建议：建议患者结果回报后请及时至我科门诊复诊，若出现病情变化或病情加重", "无好转等，请及时至急诊科门诊复诊。", "温馨提示：1.请妥善保管好病历及各种检查检验报告单。", "2.复诊时，请携带本病历记录，谢谢！", "第1页(共1页)"]

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
2026-08-10 11:45:37,002 INFO     29 [qwen-vl-text] coord API raw response (len=2385):
[
	{"text": "门诊", "bbox": [91, 81, 133, 100]},
	{"text": "姓名：", "bbox": [91, 102, 155, 120]},
	{"text": "门(急)诊初诊病历", "bbox": [347, 90, 606, 113]},
	{"text": "性别：女", "bbox": [645, 104, 723, 120]},
	{"text": "科室：呼吸内科门诊", "bbox": [91, 124, 273, 141]},
	{"text": "年龄：63岁", "bbox": [645, 125, 745, 141]},
	{"text": "就诊日期：2025-10-25 15:22", "bbox": [94, 150, 379, 167]},
	{"text": "主诉：支气管哮喘复诊", "bbox": [94, 168, 312, 185]},
	{"text": "现病史：患者支气管哮喘复诊，目前规律吸入布地奈德福莫特罗320ug 一次1吸，", "bbox": [94, 187, 863, 204]},
	{"text": "一天2次。目前诉有咳嗽、咳痰，有气促感，无胸闷，无发热，无鼻塞、流涕，无咯", "bbox": [91, 206, 886, 223]},
	{"text": "血、痰中带血，无头痛、头晕、视物旋转，无饮水呛咳，无咽痛、腹痛、腹胀等不", "bbox": [91, 225, 874, 242]},
	{"text": "适。未予处理及就医。现患者为求进一步诊治，故至我院科门诊就医。", "bbox": [91, 243, 750, 260]},
	{"text": "既往史：否认高血压、否认糖尿病、否认冠心病等慢性疾病病史，否认肝炎、结核", "bbox": [94, 262, 886, 279]},
	{"text": "等传染病史，否认手术外伤输血史 过敏史：无食物、药物过敏史。。否认饮酒史。", "bbox": [91, 280, 874, 298]},
	{"text": "个人史：已婚已育", "bbox": [94, 300, 269, 317]},
	{"text": "家族史：否认家族病史。", "bbox": [94, 319, 324, 336]},
	{"text": "体格检查：T：36.8℃ P：87次/分 R：21次/分 BP：108/73mmHg 指脉氧：", "bbox": [94, 338, 827, 355]},
	{"text": "9%。神志清楚，精神尚可，呼吸平顺，口唇无发绀，咽部无充血，扁桃体无肿大，", "bbox": [91, 357, 869, 374]},
	{"text": "双侧颈静脉无怒张，双肺呼吸音粗，双肺可闻及干啰音，双肺未闻及湿性啰音及胸膜", "bbox": [91, 376, 889, 393]},
	{"text": "摩擦音。心率87次/分，律齐，各瓣膜未闻及明显病理性杂音。腹部平软，全腹部无", "bbox": [91, 395, 884, 412]},
	{"text": "玉痛，反跳痛，肠鸣音正常。四肢运动自如，双下肢无水肿。", "bbox": [91, 413, 662, 430]},
	{"text": "辅助检查：患者自行购买布地奈德福莫特罗320ug 一次1吸，一天2次。", "bbox": [94, 432, 762, 449]},
	{"text": "初步诊断：", "bbox": [94, 451, 190, 468]},
	{"text": "西医诊断：1.支气管哮喘(急性发作期)", "bbox": [130, 470, 499, 487]},
	{"text": "处理意见：", "bbox": [94, 489, 190, 506]},
	{"text": "醋酸泼尼松片（国基）(5mg*100片) 20.000mg", "bbox": [91, 508, 525, 525]},
	{"text": "1次/天 口服", "bbox": [632, 508, 754, 525]},
	{"text": "12.00片", "bbox": [790, 508, 865, 525]},
	{"text": "硫酸沙丁胺醇吸入气雾剂（省3、国基）(200揿：", "bbox": [91, 527, 543, 544]},
	{"text": "100μg) 200.000μg", "bbox": [91, 545, 285, 563]},
	{"text": "1次/天 吸入", "bbox": [632, 527, 754, 544]},
	{"text": "1.00瓶", "bbox": [790, 527, 855, 544]},
	{"text": "建议：建议患者结果回报后请及时至我科门诊复诊，若出现病情变化或病情加重", "bbox": [91, 640, 883, 657]},
	{"text": "无好转等，请及时至急诊科门诊复诊。", "bbox": [91, 659, 443, 676]},
	{"text": "温馨提示：1.请妥善保管好病历及各种检查检验报告单。", "bbox": [85, 721, 616, 738]},
	{"text": "2.复诊时，请携带本病历记录，谢谢！", "bbox": [188, 743, 551, 760]},
	{"text": "第1页(共1页)", "bbox": [421, 765, 548, 782]}
]
2026-08-10 11:45:37,002 INFO     29 [qwen-vl-text] coord API: raw_items=37, valid_items=37, elapsed=14.3s
2026-08-10 11:45:37,002 INFO     29 [qwen-vl-text] coord item[0]: text=门诊, bbox=[91, 81, 133, 100]
2026-08-10 11:45:37,002 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[91, 102, 155, 120]
2026-08-10 11:45:37,002 INFO     29 [qwen-vl-text] coord item[2]: text=门(急)诊初诊病历, bbox=[347, 90, 606, 113]
2026-08-10 11:45:37,002 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女, bbox=[645, 104, 723, 120]
2026-08-10 11:45:37,002 INFO     29 [qwen-vl-text] coord item[4]: text=科室：呼吸内科门诊, bbox=[91, 124, 273, 141]
2026-08-10 11:45:37,002 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：63岁, bbox=[645, 125, 745, 141]
2026-08-10 11:45:37,002 INFO     29 [qwen-vl-text] coord item[6]: text=就诊日期：2025-10-25 15:22, bbox=[94, 150, 379, 167]
2026-08-10 11:45:37,002 INFO     29 [qwen-vl-text] coord item[7]: text=主诉：支气管哮喘复诊, bbox=[94, 168, 312, 185]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[8]: text=现病史：患者支气管哮喘复诊，目前规律吸入布地奈德福莫特罗320ug 一次1吸，, bbox=[94, 187, 863, 204]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[9]: text=一天2次。目前诉有咳嗽、咳痰，有气促感，无胸闷，无发热，无鼻塞、流涕，无咯, bbox=[91, 206, 886, 223]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[10]: text=血、痰中带血，无头痛、头晕、视物旋转，无饮水呛咳，无咽痛、腹痛、腹胀等不, bbox=[91, 225, 874, 242]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[11]: text=适。未予处理及就医。现患者为求进一步诊治，故至我院科门诊就医。, bbox=[91, 243, 750, 260]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[12]: text=既往史：否认高血压、否认糖尿病、否认冠心病等慢性疾病病史，否认肝炎、结核, bbox=[94, 262, 886, 279]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[13]: text=等传染病史，否认手术外伤输血史 过敏史：无食物、药物过敏史。。否认饮酒史。, bbox=[91, 280, 874, 298]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[14]: text=个人史：已婚已育, bbox=[94, 300, 269, 317]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[15]: text=家族史：否认家族病史。, bbox=[94, 319, 324, 336]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[16]: text=体格检查：T：36.8℃ P：87次/分 R：21次/分 BP：108/73mmHg 指脉氧：, bbox=[94, 338, 827, 355]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[17]: text=9%。神志清楚，精神尚可，呼吸平顺，口唇无发绀，咽部无充血，扁桃体无肿大，, bbox=[91, 357, 869, 374]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[18]: text=双侧颈静脉无怒张，双肺呼吸音粗，双肺可闻及干啰音，双肺未闻及湿性啰音及胸膜, bbox=[91, 376, 889, 393]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[19]: text=摩擦音。心率87次/分，律齐，各瓣膜未闻及明显病理性杂音。腹部平软，全腹部无, bbox=[91, 395, 884, 412]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[20]: text=玉痛，反跳痛，肠鸣音正常。四肢运动自如，双下肢无水肿。, bbox=[91, 413, 662, 430]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[21]: text=辅助检查：患者自行购买布地奈德福莫特罗320ug 一次1吸，一天2次。, bbox=[94, 432, 762, 449]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[22]: text=初步诊断：, bbox=[94, 451, 190, 468]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[23]: text=西医诊断：1.支气管哮喘(急性发作期), bbox=[130, 470, 499, 487]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[24]: text=处理意见：, bbox=[94, 489, 190, 506]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[25]: text=醋酸泼尼松片（国基）(5mg*100片) 20.000mg, bbox=[91, 508, 525, 525]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[26]: text=1次/天 口服, bbox=[632, 508, 754, 525]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[27]: text=12.00片, bbox=[790, 508, 865, 525]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[28]: text=硫酸沙丁胺醇吸入气雾剂（省3、国基）(200揿：, bbox=[91, 527, 543, 544]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[29]: text=100μg) 200.000μg, bbox=[91, 545, 285, 563]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[30]: text=1次/天 吸入, bbox=[632, 527, 754, 544]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[31]: text=1.00瓶, bbox=[790, 527, 855, 544]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[32]: text=建议：建议患者结果回报后请及时至我科门诊复诊，若出现病情变化或病情加重, bbox=[91, 640, 883, 657]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[33]: text=无好转等，请及时至急诊科门诊复诊。, bbox=[91, 659, 443, 676]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[34]: text=温馨提示：1.请妥善保管好病历及各种检查检验报告单。, bbox=[85, 721, 616, 738]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[35]: text=2.复诊时，请携带本病历记录，谢谢！, bbox=[188, 743, 551, 760]
2026-08-10 11:45:37,003 INFO     29 [qwen-vl-text] coord item[36]: text=第1页(共1页), bbox=[421, 765, 548, 782]
2026-08-10 11:45:37,004 INFO     29 [qwen-vl-text] page=13 — 37/37 coords, api_time=14.3s
2026-08-10 11:45:37,004 INFO     29 [qwen-vl-text] new_positions (37):
[[13, 54.144999999999996, 79.13499999999999, 68.202, 84.2], [13, 54.144999999999996, 92.225, 85.884, 101.03999999999999], [13, 206.465, 360.57, 75.78, 95.146], [13, 383.775, 430.185, 87.568, 101.03999999999999], [13, 54.144999999999996, 162.435, 104.408, 118.722], [13, 383.775, 443.275, 105.25, 118.722], [13, 55.93, 225.505, 126.3, 140.614], [13, 55.93, 185.64, 141.456, 155.76999999999998], [13, 55.93, 513.485, 157.454, 171.768], [13, 54.144999999999996, 527.17, 173.452, 187.766], [13, 54.144999999999996, 520.03, 189.45, 203.76399999999998], [13, 54.144999999999996, 446.25, 204.606, 218.92], [13, 55.93, 527.17, 220.60399999999998, 234.91799999999998], [13, 54.144999999999996, 520.03, 235.76, 250.916], [13, 55.93, 160.055, 252.6, 266.914], [13, 55.93, 192.78, 268.598, 282.912], [13, 55.93, 492.065, 284.596, 298.90999999999997], [13, 54.144999999999996, 517.055, 300.594, 314.908], [13, 54.144999999999996, 528.9549999999999, 316.592, 330.906], [13, 54.144999999999996, 525.98, 332.59, 346.904], [13, 54.144999999999996, 393.89, 347.746, 362.06], [13, 55.93, 453.39, 363.74399999999997, 378.058], [13, 55.93, 113.05, 379.74199999999996, 394.056], [13, 77.35, 296.905, 395.74, 410.054], [13, 55.93, 113.05, 411.738, 426.05199999999996], [13, 54.144999999999996, 312.375, 427.736, 442.05], [13, 376.03999999999996, 448.63, 427.736, 442.05], [13, 470.04999999999995, 514.675, 427.736, 442.05], [13, 54.144999999999996, 323.085, 443.734, 458.048], [13, 54.144999999999996, 169.575, 458.89, 474.046], [13, 376.03999999999996, 448.63, 443.734, 458.048], [13, 470.04999999999995, 508.72499999999997, 443.734, 458.048], [13, 54.144999999999996, 525.385, 538.88, 553.194], [13, 54.144999999999996, 263.585, 554.8779999999999, 569.192], [13, 50.574999999999996, 366.52, 607.082, 621.396], [13, 111.86, 327.84499999999997, 625.606, 639.92], [13, 250.49499999999998, 326.06, 644.13, 658.444]]
2026-08-10 11:45:37,004 INFO     29 [qwen-vl-text] ═══ DONE ═══ 37 positions, pages=1, time=18.9s
2026-08-10 11:45:37,004 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:45:37,005 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:45:37,006 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:45:37,007 INFO     29 [qwen-vl-text] positions(30): [[16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:45:37,007 INFO     29 [qwen-vl-text] page grouping: [16], lines per page: [30]
2026-08-10 11:45:37,288 INFO     29 [qwen-vl-text] page=16, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:45:37,290 INFO     29 [qwen-vl-text] LLM extraction start, text_len=732
2026-08-10 11:45:37,290 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:45:37,290 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 513, \"bbox_end\": 542, \"encounter_dates\": [\"2025-11-24\"], \"department\": \"呼吸内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊号\n姓名\n科室:呼吸内科门诊\n门(急)诊初诊病历\n电话\n性别:女\n年龄:63岁\n就诊日期:2025-11-24 15:01\n主诉:支气管哮喘复诊\n现病史:患者支气管哮喘复诊,目前规律吸入布地奈德福莫特罗320一次1吸,一天2次(患者自行网购药物),目前有咳嗽、咳痰,咳嗽时有气喘感。无胸闷,无发热,无鼻塞、流涕,无咯血、痰中带血,无头痛、头晕、视物旋转,无饮水呛咳,无咽痛、腹痛、腹胀等不适。未予处理及就医。现患者为求进一步诊治,故至我院科门诊就医。\n既往史:否认高血压、否认糖尿病、否认冠心病等慢性疾病病史,否认肝炎、结核等传染病史,否认手术外伤输血史过敏史:无食物、药物过敏史。。否认饮酒史。\n个人史:已婚已育\n家族史:否认家族病史。\n体格检查:T:36.8℃ P:87次/分 R:21次/分 BP:108/73mmHg 指脉氧:\n9%。神志清楚,精神尚可,呼吸平顺,口唇无发绀,咽部无充血,扁桃体无肿大,\n双侧颈静脉无怒张,双肺呼吸音粗,双肺可闻及散在干啰音,双肺未闻及湿性啰音及\n胸膜摩擦音。心率87次/分,律齐,各瓣膜未闻及明显病理性杂音。腹部平软,全腹\n邻无压痛,反跳痛,肠鸣音正常。四肢运动自如,双下肢无水肿。\n辅助检查:\n初步诊断:\n西医诊断:1.支气管哮喘(急性发作期)\n处理意见:自备布地奈德福莫特罗320一次1吸,一天2次\n醋酸泼尼松片(国基)(5mg*100片)10.000mg\n1次/天 口服 6.00片\n建议:建议患者结果回报后请及时至我科门诊复诊,若出现病情变化或病情加重\n无好转等,请及时至急诊科门诊复诊。\n医生签名:\n温馨提示:1.请妥善保管好病历及各种检查检验报告单。\n2.复诊时,请携带本病历记录,谢谢!\n第1页(共1页)",
    "role": "user"
  }
]
2026-08-10 11:45:41,335 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:45:41,335 INFO     29 [qwen-vl-text] LLM output (len=679):
{
  "encounter_date": "2025-11-24",
  "chief_complaint": "支气管哮喘复诊",
  "present_illness": "患者支气管哮喘复诊,目前规律吸入布地奈德福莫特罗320一次1吸,一天2次(患者自行网购药物),目前有咳嗽、咳痰,咳嗽时有气喘感。无胸闷,无发热,无鼻塞、流涕,无咯血、痰中带血,无头痛、头晕、视物旋转,无饮水呛咳,无咽痛、腹痛、腹胀等不适。未予处理及就医。现患者为求进一步诊治,故至我院科门诊就医。",
  "past_history": "否认高血压、否认糖尿病、否认冠心病等慢性疾病病史,否认肝炎、结核等传染病史,否认手术外伤输血史过敏史:无食物、药物过敏史。。否认饮酒史。",
  "diagnosis": "西医诊断:1.支气管哮喘(急性发作期)",
  "treatment_plan": [
    {
      "drug_name": "布地奈德福莫特罗320",
      "dosage": "1吸",
      "frequency": "一天2次",
      "route": "吸入",
      "note": "自备"
    },
    {
      "drug_name": "醋酸泼尼松片(国基)",
      "dosage": "10.000mg",
      "frequency": "1次/天",
      "route": "口服",
      "quantity": "6.00片"
    }
  ]
}
2026-08-10 11:45:41,335 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-11-24]
2026-08-10 11:45:41,341 INFO     29 [qwen-vl-text] coord API call start, page=16, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1525336, prompt_len=1435
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共30行）
["门诊号", "姓名", "科室:呼吸内科门诊", "门(急)诊初诊病历", "电话", "性别:女", "年龄:63岁", "就诊日期:2025-11-24 15:01", "主诉:支气管哮喘复诊", "现病史:患者支气管哮喘复诊,目前规律吸入布地奈德福莫特罗320一次1吸,一天2次(患者自行网购药物),目前有咳嗽、咳痰,咳嗽时有气喘感。无胸闷,无发热,无鼻塞、流涕,无咯血、痰中带血,无头痛、头晕、视物旋转,无饮水呛咳,无咽痛、腹痛、腹胀等不适。未予处理及就医。现患者为求进一步诊治,故至我院科门诊就医。", "既往史:否认高血压、否认糖尿病、否认冠心病等慢性疾病病史,否认肝炎、结核等传染病史,否认手术外伤输血史过敏史:无食物、药物过敏史。。否认饮酒史。", "个人史:已婚已育", "家族史:否认家族病史。", "体格检查:T:36.8℃ P:87次/分 R:21次/分 BP:108/73mmHg 指脉氧:", "9%。神志清楚,精神尚可,呼吸平顺,口唇无发绀,咽部无充血,扁桃体无肿大,", "双侧颈静脉无怒张,双肺呼吸音粗,双肺可闻及散在干啰音,双肺未闻及湿性啰音及", "胸膜摩擦音。心率87次/分,律齐,各瓣膜未闻及明显病理性杂音。腹部平软,全腹", "邻无压痛,反跳痛,肠鸣音正常。四肢运动自如,双下肢无水肿。", "辅助检查:", "初步诊断:", "西医诊断:1.支气管哮喘(急性发作期)", "处理意见:自备布地奈德福莫特罗320一次1吸,一天2次", "醋酸泼尼松片(国基)(5mg*100片)10.000mg", "1次/天 口服 6.00片", "建议:建议患者结果回报后请及时至我科门诊复诊,若出现病情变化或病情加重", "无好转等,请及时至急诊科门诊复诊。", "医生签名:", "温馨提示:1.请妥善保管好病历及各种检查检验报告单。", "2.复诊时,请携带本病历记录,谢谢!", "第1页(共1页)"]

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
2026-08-10 11:45:52,650 INFO     29 [qwen-vl-text] coord API raw response (len=2023):
[
	{"text": "门诊号", "bbox": [56, 44, 127, 65]},
	{"text": "姓名", "bbox": [56, 71, 105, 92]},
	{"text": "科室:呼吸内科门诊", "bbox": [54, 100, 268, 119]},
	{"text": "门(急)诊初诊病历", "bbox": [357, 57, 657, 86]},
	{"text": "电话", "bbox": [702, 49, 744, 69]},
	{"text": "性别:女", "bbox": [702, 74, 788, 93]},
	{"text": "年龄:63岁", "bbox": [702, 100, 811, 118]},
	{"text": "就诊日期:2025-11-24 15:01", "bbox": [58, 130, 390, 149]},
	{"text": "主诉:支气管哮喘复诊", "bbox": [58, 153, 313, 172]},
	{"text": "现病史:患者支气管哮喘复诊,目前规律吸入布地奈德福莫特罗320一次1吸,一天2次(患者自行网购药物),目前有咳嗽、咳痰,咳嗽时有气喘感。无胸闷,无发热,无鼻塞、流涕,无咯血、痰中带血,无头痛、头晕、视物旋转,无饮水呛咳,无咽痛、腹痛、腹胀等不适。未予处理及就医。现患者为求进一步诊治,故至我院科门诊就医。", "bbox": [52, 176, 969, 287]},
	{"text": "既往史:否认高血压、否认糖尿病、否认冠心病等慢性疾病病史,否认肝炎、结核等传染病史,否认手术外伤输血史过敏史:无食物、药物过敏史。。否认饮酒史。", "bbox": [52, 292, 964, 337]},
	{"text": "个人史:已婚已育", "bbox": [56, 339, 259, 358]},
	{"text": "家族史:否认家族病史。", "bbox": [56, 362, 324, 381]},
	{"text": "体格检查:T:36.8℃ P:87次/分 R:21次/分 BP:108/73mmHg 指脉氧:", "bbox": [56, 385, 899, 404]},
	{"text": "9%。神志清楚,精神尚可,呼吸平顺,口唇无发绀,咽部无充血,扁桃体无肿大,", "bbox": [48, 408, 945, 427]},
	{"text": "双侧颈静脉无怒张,双肺呼吸音粗,双肺可闻及散在干啰音,双肺未闻及湿性啰音及", "bbox": [48, 431, 967, 450]},
	{"text": "胸膜摩擦音。心率87次/分,律齐,各瓣膜未闻及明显病理性杂音。腹部平软,全腹", "bbox": [48, 454, 961, 473]},
	{"text": "邻无压痛,反跳痛,肠鸣音正常。四肢运动自如,双下肢无水肿。", "bbox": [48, 477, 757, 496]},
	{"text": "辅助检查:", "bbox": [54, 499, 165, 518]},
	{"text": "初步诊断:", "bbox": [54, 521, 165, 540]},
	{"text": "西医诊断:1.支气管哮喘(急性发作期)", "bbox": [94, 544, 519, 563]},
	{"text": "处理意见:自备布地奈德福莫特罗320一次1吸,一天2次", "bbox": [52, 567, 695, 586]},
	{"text": "醋酸泼尼松片(国基)(5mg*100片)10.000mg", "bbox": [45, 590, 550, 609]},
	{"text": "1次/天 口服 6.00片", "bbox": [671, 590, 920, 609]},
	{"text": "建议:建议患者结果回报后请及时至我科门诊复诊,若出现病情变化或病情加重", "bbox": [50, 704, 950, 723]},
	{"text": "无好转等,请及时至急诊科门诊复诊。", "bbox": [44, 726, 454, 745]},
	{"text": "医生签名:", "bbox": [746, 756, 854, 775]},
	{"text": "温馨提示:1.请妥善保管好病历及各种检查检验报告单。", "bbox": [44, 824, 648, 843]},
	{"text": "2.复诊时,请携带本病历记录,谢谢!", "bbox": [164, 850, 574, 869]},
	{"text": "第1页(共1页)", "bbox": [426, 875, 570, 893]}
]
2026-08-10 11:45:52,650 INFO     29 [qwen-vl-text] coord API: raw_items=30, valid_items=30, elapsed=11.3s
2026-08-10 11:45:52,650 INFO     29 [qwen-vl-text] coord item[0]: text=门诊号, bbox=[56, 44, 127, 65]
2026-08-10 11:45:52,650 INFO     29 [qwen-vl-text] coord item[1]: text=姓名, bbox=[56, 71, 105, 92]
2026-08-10 11:45:52,650 INFO     29 [qwen-vl-text] coord item[2]: text=科室:呼吸内科门诊, bbox=[54, 100, 268, 119]
2026-08-10 11:45:52,650 INFO     29 [qwen-vl-text] coord item[3]: text=门(急)诊初诊病历, bbox=[357, 57, 657, 86]
2026-08-10 11:45:52,650 INFO     29 [qwen-vl-text] coord item[4]: text=电话, bbox=[702, 49, 744, 69]
2026-08-10 11:45:52,651 INFO     29 [qwen-vl-text] coord item[5]: text=性别:女, bbox=[702, 74, 788, 93]
2026-08-10 11:45:52,651 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:63岁, bbox=[702, 100, 811, 118]
2026-08-10 11:45:52,651 INFO     29 [qwen-vl-text] coord item[7]: text=就诊日期:2025-11-24 15:01, bbox=[58, 130, 390, 149]
2026-08-10 11:45:52,651 INFO     29 [qwen-vl-text] coord item[8]: text=主诉:支气管哮喘复诊, bbox=[58, 153, 313, 172]
2026-08-10 11:45:52,651 INFO     29 [qwen-vl-text] coord item[9]: text=现病史:患者支气管哮喘复诊,目前规律吸入布地奈德福莫特罗320一次1吸,一天2次(患者自行网购药物),目前有咳嗽、咳痰,咳嗽时有气喘感。无胸闷,无发热,无鼻塞、流涕,无咯血、痰中带血,无头痛、头晕、视物旋转,无饮水呛咳,无咽痛、腹痛、腹胀等不适。未予处理及就医。现患者为求进一步诊治,故至我院科门诊就医。, bbox=[52, 176, 969, 287]
2026-08-10 11:45:52,651 INFO     29 [qwen-vl-text] coord item[10]: text=既往史:否认高血压、否认糖尿病、否认冠心病等慢性疾病病史,否认肝炎、结核等传染病史,否认手术外伤输血史过敏史:无食物、药物过敏史。。否认饮酒史。, bbox=[52, 292, 964, 337]
2026-08-10 11:45:52,651 INFO     29 [qwen-vl-text] coord item[11]: text=个人史:已婚已育, bbox=[56, 339, 259, 358]
2026-08-10 11:45:52,651 INFO     29 [qwen-vl-text] coord item[12]: text=家族史:否认家族病史。, bbox=[56, 362, 324, 381]
2026-08-10 11:45:52,651 INFO     29 [qwen-vl-text] coord item[13]: text=体格检查:T:36.8℃ P:87次/分 R:21次/分 BP:108/73mmHg 指脉氧:, bbox=[56, 385, 899, 404]
2026-08-10 11:45:52,651 INFO     29 [qwen-vl-text] coord item[14]: text=9%。神志清楚,精神尚可,呼吸平顺,口唇无发绀,咽部无充血,扁桃体无肿大,, bbox=[48, 408, 945, 427]
2026-08-10 11:45:52,651 INFO     29 [qwen-vl-text] coord item[15]: text=双侧颈静脉无怒张,双肺呼吸音粗,双肺可闻及散在干啰音,双肺未闻及湿性啰音及, bbox=[48, 431, 967, 450]
2026-08-10 11:45:52,651 INFO     29 [qwen-vl-text] coord item[16]: text=胸膜摩擦音。心率87次/分,律齐,各瓣膜未闻及明显病理性杂音。腹部平软,全腹, bbox=[48, 454, 961, 473]
2026-08-10 11:45:52,651 INFO     29 [qwen-vl-text] coord item[17]: text=邻无压痛,反跳痛,肠鸣音正常。四肢运动自如,双下肢无水肿。, bbox=[48, 477, 757, 496]
2026-08-10 11:45:52,651 INFO     29 [qwen-vl-text] coord item[18]: text=辅助检查:, bbox=[54, 499, 165, 518]
2026-08-10 11:45:52,651 INFO     29 [qwen-vl-text] coord item[19]: text=初步诊断:, bbox=[54, 521, 165, 540]
2026-08-10 11:45:52,651 INFO     29 [qwen-vl-text] coord item[20]: text=西医诊断:1.支气管哮喘(急性发作期), bbox=[94, 544, 519, 563]
2026-08-10 11:45:52,651 INFO     29 [qwen-vl-text] coord item[21]: text=处理意见:自备布地奈德福莫特罗320一次1吸,一天2次, bbox=[52, 567, 695, 586]
2026-08-10 11:45:52,651 INFO     29 [qwen-vl-text] coord item[22]: text=醋酸泼尼松片(国基)(5mg*100片)10.000mg, bbox=[45, 590, 550, 609]
2026-08-10 11:45:52,651 INFO     29 [qwen-vl-text] coord item[23]: text=1次/天 口服 6.00片, bbox=[671, 590, 920, 609]
2026-08-10 11:45:52,651 INFO     29 [qwen-vl-text] coord item[24]: text=建议:建议患者结果回报后请及时至我科门诊复诊,若出现病情变化或病情加重, bbox=[50, 704, 950, 723]
2026-08-10 11:45:52,651 INFO     29 [qwen-vl-text] coord item[25]: text=无好转等,请及时至急诊科门诊复诊。, bbox=[44, 726, 454, 745]
2026-08-10 11:45:52,651 INFO     29 [qwen-vl-text] coord item[26]: text=医生签名:, bbox=[746, 756, 854, 775]
2026-08-10 11:45:52,651 INFO     29 [qwen-vl-text] coord item[27]: text=温馨提示:1.请妥善保管好病历及各种检查检验报告单。, bbox=[44, 824, 648, 843]
2026-08-10 11:45:52,651 INFO     29 [qwen-vl-text] coord item[28]: text=2.复诊时,请携带本病历记录,谢谢!, bbox=[164, 850, 574, 869]
2026-08-10 11:45:52,651 INFO     29 [qwen-vl-text] coord item[29]: text=第1页(共1页), bbox=[426, 875, 570, 893]
2026-08-10 11:45:52,652 INFO     29 [qwen-vl-text] page=16 — 30/30 coords, api_time=11.3s
2026-08-10 11:45:52,652 INFO     29 [qwen-vl-text] new_positions (30):
[[16, 33.32, 75.565, 37.048, 54.73], [16, 33.32, 62.474999999999994, 59.782, 77.464], [16, 32.129999999999995, 159.45999999999998, 84.2, 100.198], [16, 212.415, 390.91499999999996, 47.994, 72.41199999999999], [16, 417.69, 442.68, 41.257999999999996, 58.098], [16, 417.69, 468.85999999999996, 62.308, 78.306], [16, 417.69, 482.54499999999996, 84.2, 99.356], [16, 34.51, 232.04999999999998, 109.46, 125.458], [16, 34.51, 186.23499999999999, 128.826, 144.82399999999998], [16, 30.939999999999998, 576.555, 148.192, 241.654], [16, 30.939999999999998, 573.5799999999999, 245.864, 283.75399999999996], [16, 33.32, 154.105, 285.438, 301.436], [16, 33.32, 192.78, 304.804, 320.80199999999996], [16, 33.32, 534.905, 324.17, 340.168], [16, 28.56, 562.275, 343.536, 359.534], [16, 28.56, 575.365, 362.902, 378.9], [16, 28.56, 571.795, 382.268, 398.26599999999996], [16, 28.56, 450.41499999999996, 401.63399999999996, 417.632], [16, 32.129999999999995, 98.175, 420.15799999999996, 436.156], [16, 32.129999999999995, 98.175, 438.68199999999996, 454.68], [16, 55.93, 308.805, 458.048, 474.046], [16, 30.939999999999998, 413.525, 477.414, 493.412], [16, 26.775, 327.25, 496.78, 512.778], [16, 399.245, 547.4, 496.78, 512.778], [16, 29.75, 565.25, 592.768, 608.766], [16, 26.18, 270.13, 611.292, 627.29], [16, 443.87, 508.13, 636.552, 652.55], [16, 26.18, 385.56, 693.808, 709.8059999999999], [16, 97.58, 341.53, 715.6999999999999, 731.698], [16, 253.47, 339.15, 736.75, 751.906]]
2026-08-10 11:45:52,652 INFO     29 [qwen-vl-text] ═══ DONE ═══ 30 positions, pages=1, time=15.6s
2026-08-10 11:45:52,667 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 11:45:52,668 INFO     29 [Trace] task=38277e3a | doc=LZQ 64 哮喘 深圳二院.pdf | Extractor:Clinical | outputs={"chunks": "6 items, types={'OutpatientRecord': 6}", "html": "", "json": "675 items", "markdown": "", "text": "", "name": "LZQ 64 哮喘 深圳二院.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Medication\": 5}"}
2026-08-10 11:45:52,668 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 11:45:52,668 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:45:52.668+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 24, "failed": 0, "current": {"38277e3a94b011f1bd9827cf206dfa2d": {"id": "38277e3a94b011f1bd9827cf206dfa2d", "doc_id": "370244ae94b011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479740, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362000249, "task_type": "dataflow", "root_trace_id": "96cd8dab6bb7455194a762d3f16e1d52", "root_traceparent": "00-96cd8dab6bb7455194a762d3f16e1d52-1e133766dfd81337-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:45:52,677 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:45:52,679 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:45:52,679 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 11:45:52,679 INFO     29 [qwen-vl-text] positions(48): [[14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:45:52,679 INFO     29 [qwen-vl-text] page grouping: [14], lines per page: [48]
2026-08-10 11:45:52,873 INFO     29 [qwen-vl-text] page=14, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 11:45:52,876 INFO     29 [qwen-vl-text] LLM extraction start, text_len=545
2026-08-10 11:45:52,876 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:45:52,876 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 427, \"bbox_end\": 474, \"encounter_dates\": [\"2025-10-25\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "广东省医疗门诊收费票据（电子）\n广东省\n财政部监制\n票据代码：44060125\n票据号码：9148002082\n校验码： 831306\n开票日期：2025-10-25\n项目名称\n数量/单位\n金额（元）\n备注\n项目名称\n数量/单位\n金额（元）\n备注\n西药费\n1\n13.05\n以下是清单项\n醋酸泼尼松片（国基）\n12\n0.50\n硫酸沙丁胺醇吸入气雾剂（省3\n1\n12.55\n、国基）\n金额合计（大写）壹拾叁元零伍分\n(小写)13.05\n业务流水号：SF10390911\n门诊\n就诊日期：20251025\n其他信息\n医疗机构类型：综合医院\n医保类型：现金(自费)\n医保编号：\n性别：女\n医保统筹基金支付：0.00\n其他支付：0.00\n个人账户支付：0.00\n个人现金支付：13.05\n个人自付：0.00\n个人自费：13.05\n政策性减免：\n收款单位（章）深圳市龙岗区第人民医院\n复核人：掌上医院\n收款人：掌上医院\n说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。\n单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dzpj.czt.gd.gov.cn/billcheck查验本省财政电子票据。",
    "role": "user"
  }
]
2026-08-10 11:45:56,549 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:45:56,549 INFO     29 [qwen-vl-text] LLM output (len=680):
{
  "encounter_date": "2025-10-25",
  "pharmacy": "深圳市龙岗区第人民医院",
  "medications": [
    {
      "name": "醋酸泼尼松片",
      "specification": null,
      "dosage": null,
      "quantity": 12,
      "unit_price": 0.50,
      "total_price": 6.00,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    },
    {
      "name": "硫酸沙丁胺醇吸入气雾剂",
      "specification": null,
      "dosage": null,
      "quantity": 1,
      "unit_price": 12.55,
      "total_price": 12.55,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 13.05,
  "payment_method": "现金"
}
2026-08-10 11:45:56,549 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-10-25]
2026-08-10 11:45:56,554 INFO     29 [qwen-vl-text] coord API call start, page=14, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=928201, prompt_len=1302
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共48行）
["广东省医疗门诊收费票据（电子）", "广东省", "财政部监制", "票据代码：44060125", "票据号码：9148002082", "校验码： 831306", "开票日期：2025-10-25", "项目名称", "数量/单位", "金额（元）", "备注", "项目名称", "数量/单位", "金额（元）", "备注", "西药费", "1", "13.05", "以下是清单项", "醋酸泼尼松片（国基）", "12", "0.50", "硫酸沙丁胺醇吸入气雾剂（省3", "1", "12.55", "、国基）", "金额合计（大写）壹拾叁元零伍分", "(小写)13.05", "业务流水号：SF10390911", "门诊", "就诊日期：20251025", "其他信息", "医疗机构类型：综合医院", "医保类型：现金(自费)", "医保编号：", "性别：女", "医保统筹基金支付：0.00", "其他支付：0.00", "个人账户支付：0.00", "个人现金支付：13.05", "个人自付：0.00", "个人自费：13.05", "政策性减免：", "收款单位（章）深圳市龙岗区第人民医院", "复核人：掌上医院", "收款人：掌上医院", "说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。", "单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dzpj.czt.gd.gov.cn/billcheck查验本省财政电子票据。"]

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
2026-08-10 11:46:18,139 INFO     29 [qwen-vl-text] coord API raw response (len=3972):
[
	{"text": "广东省医疗门诊收费票据（电子）", "bbox": [316, 65, 701, 102]},
	{"text": "广东省", "bbox": [490, 100, 537, 118]},
	{"text": "财政部监制", "bbox": [474, 132, 552, 157]},
	{"text": "票据代码：44060125", "bbox": [97, 164, 210, 181]},
	{"text": "票据号码：9148002082", "bbox": [653, 164, 781, 181], "bbox": [653, 164, 781, 181]},
	{"text": "校验码： 831306", "bbox": [652, 190, 754, 207], "bbox": [652, 190, 754, 207]},
	{"text": "开票日期：2025-10-25", "bbox": [652, 216, 780, 233], "bbox": [652, 216, 780, 233]},
	{"text": "项目名称", "bbox": [164, 251, 216, 268], "bbox": [164, 251, 216, 268]},
	{"text": "数量/单位", "bbox": [300, 251, 365, 268], "bbox": [300, 251, 365, 268]},
	{"text": "金额（元）", "bbox": [391, 251, 448, 268], "bbox": [391, 251, 448, 268]},
	{"text": "备注", "bbox": [472, 251, 496, 268], "bbox": [472, 251, 496, 268]},
	{"text": "项目名称", "bbox": [579, 251, 632, 268], "bbox": [579, 251, 632, 268]},
	{"text": "数量/单位", "bbox": [715, 251, 780, 268], "bbox": [715, 251, 780, 268]},
	{"text": "金额（元）", "bbox": [806, 251, 862, 268], "bbox": [806, 251, 862, 268]},
	{"text": "备注", "bbox": [883, 251, 906, 268], "bbox": [883, 251, 906, 268]},
	{"text": "西药费", "bbox": [98, 287, 139, 305], "bbox": [98, 287, 139, 305]},
	{"text": "1", "bbox": [303, 290, 309, 304], "bbox": [303, 290, 309, 304]},
	{"text": "13.05", "bbox": [421, 290, 454, 304], "bbox": [421, 290, 454, 304]},
	{"text": "以下是清单项", "bbox": [98, 343, 178, 361], "bbox": [98, 343, 178, 361]},
	{"text": "醋酸泼尼松片（国基）", "bbox": [98, 373, 225, 391], "bbox": [98, 373, 225, 391]},
	{"text": "12", "bbox": [300, 376, 313, 390], "bbox": [300, 376, 313, 390]},
	{"text": "0.50", "bbox": [425, 376, 454, 390], "bbox": [425, 376, 454, 390]},
	{"text": "硫酸沙丁胺醇吸入气雾剂（省3", "bbox": [513, 373, 695, 391], "bbox": [513, 373, 695, 391]},
	{"text": "1", "bbox": [717, 376, 723, 390], "bbox": [717, 376, 723, 390]},
	{"text": "12.55", "bbox": [836, 376, 867, 390], "bbox": [836, 376, 867, 390]},
	{"text": "、国基）", "bbox": [513, 396, 560, 414], "bbox": [513, 396, 560, 414]},
	{"text": "金额合计（大写）壹拾叁元零伍分", "bbox": [101, 559, 297, 577], "bbox": [101, 559, 297, 577]},
	{"text": "(小写)13.05", "bbox": [565, 560, 639, 577], "bbox": [565, 560, 639, 577]},
	{"text": "业务流水号：SF10390911", "bbox": [127, 595, 267, 612], "bbox": [127, 595, 267, 612]},
	{"text": "门诊", "bbox": [339, 595, 365, 612], "bbox": [339, 595, 365, 612]},
	{"text": "就诊日期：20251025", "bbox": [739, 595, 854, 612], "bbox": [739, 595, 854, 612]},
	{"text": "其他信息", "bbox": [106, 625, 118, 760], "bbox": [106, 625, 118, 760]},
	{"text": "医疗机构类型：综合医院", "bbox": [127, 641, 267, 658], "bbox": [127, 641, 267, 658]},
	{"text": "医保类型：现金(自费)", "bbox": [339, 641, 461, 658], "bbox": [339, 641, 461, 658]},
	{"text": "医保编号：", "bbox": [525, 641, 583, 658], "bbox": [525, 641, 583, 658]},
	{"text": "性别：女", "bbox": [739, 641, 787, 658], "bbox": [739, 641, 787, 658]},
	{"text": "医保统筹基金支付：0.00", "bbox": [127, 685, 267, 702], "bbox": [127, 685, 267, 702]},
	{"text": "其他支付：0.00", "bbox": [339, 685, 424, 702], "bbox": [339, 685, 424, 702]},
	{"text": "个人账户支付：0.00", "bbox": [525, 685, 640, 702], "bbox": [525, 685, 640, 702]},
	{"text": "个人现金支付：13.05", "bbox": [739, 685, 860, 702], "bbox": [739, 685, 860, 702]},
	{"text": "个人自付：0.00", "bbox": [127, 724, 216, 741], "bbox": [127, 724, 216, 741]},
	{"text": "个人自费：13.05", "bbox": [339, 724, 430, 741], "bbox": [339, 724, 430, 741]},
	{"text": "政策性减免：", "bbox": [339, 760, 409, 778], "bbox": [339, 760, 409, 778]},
	{"text": "收款单位（章）深圳市龙岗区第人民医院", "bbox": [100, 805, 361, 825], "bbox": [100, 805, 361, 825]},
	{"text": "复核人：掌上医院", "bbox": [565, 805, 664, 825], "bbox": [565, 805, 664, 825]},
	{"text": "收款人：掌上医院", "bbox": [739, 805, 841, 825], "bbox": [739, 805, 841, 825]},
	{"text": "说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。", "bbox": [114, 838, 853, 856], "bbox": [114, 838, 853, 856]},
	{"text": "单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dzpj.czt.gd.gov.cn/billcheck查验本省财政电子票据。", "bbox": [161, 856, 826, 873], "bbox": [161, 856, 826, 873]}
]
2026-08-10 11:46:18,139 INFO     29 [qwen-vl-text] coord API: raw_items=48, valid_items=48, elapsed=21.6s
2026-08-10 11:46:18,139 INFO     29 [qwen-vl-text] coord item[0]: text=广东省医疗门诊收费票据（电子）, bbox=[316, 65, 701, 102]
2026-08-10 11:46:18,139 INFO     29 [qwen-vl-text] coord item[1]: text=广东省, bbox=[490, 100, 537, 118]
2026-08-10 11:46:18,139 INFO     29 [qwen-vl-text] coord item[2]: text=财政部监制, bbox=[474, 132, 552, 157]
2026-08-10 11:46:18,139 INFO     29 [qwen-vl-text] coord item[3]: text=票据代码：44060125, bbox=[97, 164, 210, 181]
2026-08-10 11:46:18,139 INFO     29 [qwen-vl-text] coord item[4]: text=票据号码：9148002082, bbox=[653, 164, 781, 181]
2026-08-10 11:46:18,139 INFO     29 [qwen-vl-text] coord item[5]: text=校验码： 831306, bbox=[652, 190, 754, 207]
2026-08-10 11:46:18,139 INFO     29 [qwen-vl-text] coord item[6]: text=开票日期：2025-10-25, bbox=[652, 216, 780, 233]
2026-08-10 11:46:18,139 INFO     29 [qwen-vl-text] coord item[7]: text=项目名称, bbox=[164, 251, 216, 268]
2026-08-10 11:46:18,139 INFO     29 [qwen-vl-text] coord item[8]: text=数量/单位, bbox=[300, 251, 365, 268]
2026-08-10 11:46:18,139 INFO     29 [qwen-vl-text] coord item[9]: text=金额（元）, bbox=[391, 251, 448, 268]
2026-08-10 11:46:18,139 INFO     29 [qwen-vl-text] coord item[10]: text=备注, bbox=[472, 251, 496, 268]
2026-08-10 11:46:18,139 INFO     29 [qwen-vl-text] coord item[11]: text=项目名称, bbox=[579, 251, 632, 268]
2026-08-10 11:46:18,139 INFO     29 [qwen-vl-text] coord item[12]: text=数量/单位, bbox=[715, 251, 780, 268]
2026-08-10 11:46:18,139 INFO     29 [qwen-vl-text] coord item[13]: text=金额（元）, bbox=[806, 251, 862, 268]
2026-08-10 11:46:18,139 INFO     29 [qwen-vl-text] coord item[14]: text=备注, bbox=[883, 251, 906, 268]
2026-08-10 11:46:18,139 INFO     29 [qwen-vl-text] coord item[15]: text=西药费, bbox=[98, 287, 139, 305]
2026-08-10 11:46:18,139 INFO     29 [qwen-vl-text] coord item[16]: text=1, bbox=[303, 290, 309, 304]
2026-08-10 11:46:18,139 INFO     29 [qwen-vl-text] coord item[17]: text=13.05, bbox=[421, 290, 454, 304]
2026-08-10 11:46:18,139 INFO     29 [qwen-vl-text] coord item[18]: text=以下是清单项, bbox=[98, 343, 178, 361]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[19]: text=醋酸泼尼松片（国基）, bbox=[98, 373, 225, 391]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[20]: text=12, bbox=[300, 376, 313, 390]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[21]: text=0.50, bbox=[425, 376, 454, 390]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[22]: text=硫酸沙丁胺醇吸入气雾剂（省3, bbox=[513, 373, 695, 391]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[23]: text=1, bbox=[717, 376, 723, 390]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[24]: text=12.55, bbox=[836, 376, 867, 390]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[25]: text=、国基）, bbox=[513, 396, 560, 414]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[26]: text=金额合计（大写）壹拾叁元零伍分, bbox=[101, 559, 297, 577]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[27]: text=(小写)13.05, bbox=[565, 560, 639, 577]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[28]: text=业务流水号：SF10390911, bbox=[127, 595, 267, 612]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[29]: text=门诊, bbox=[339, 595, 365, 612]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[30]: text=就诊日期：20251025, bbox=[739, 595, 854, 612]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[31]: text=其他信息, bbox=[106, 625, 118, 760]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[32]: text=医疗机构类型：综合医院, bbox=[127, 641, 267, 658]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[33]: text=医保类型：现金(自费), bbox=[339, 641, 461, 658]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[34]: text=医保编号：, bbox=[525, 641, 583, 658]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[35]: text=性别：女, bbox=[739, 641, 787, 658]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[36]: text=医保统筹基金支付：0.00, bbox=[127, 685, 267, 702]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[37]: text=其他支付：0.00, bbox=[339, 685, 424, 702]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[38]: text=个人账户支付：0.00, bbox=[525, 685, 640, 702]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[39]: text=个人现金支付：13.05, bbox=[739, 685, 860, 702]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[40]: text=个人自付：0.00, bbox=[127, 724, 216, 741]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[41]: text=个人自费：13.05, bbox=[339, 724, 430, 741]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[42]: text=政策性减免：, bbox=[339, 760, 409, 778]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[43]: text=收款单位（章）深圳市龙岗区第人民医院, bbox=[100, 805, 361, 825]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[44]: text=复核人：掌上医院, bbox=[565, 805, 664, 825]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[45]: text=收款人：掌上医院, bbox=[739, 805, 841, 825]
2026-08-10 11:46:18,140 INFO     29 [qwen-vl-text] coord item[46]: text=说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。, bbox=[114, 838, 853, 856]
2026-08-10 11:46:18,141 INFO     29 [qwen-vl-text] coord item[47]: text=单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dzpj.czt.gd.gov.cn/billcheck查验本省财政电子票据。, bbox=[161, 856, 826, 873]
2026-08-10 11:46:18,141 INFO     29 [qwen-vl-text] page=14 — 48/48 coords, api_time=21.6s
2026-08-10 11:46:18,141 INFO     29 [qwen-vl-text] new_positions (48):
[[14, 266.072, 590.242, 38.675, 60.69], [14, 412.58, 452.154, 59.5, 70.21], [14, 399.108, 464.784, 78.53999999999999, 93.41499999999999], [14, 81.67399999999999, 176.82, 97.58, 107.695], [14, 549.826, 657.602, 97.58, 107.695], [14, 548.984, 634.8679999999999, 113.05, 123.16499999999999], [14, 548.984, 656.76, 128.51999999999998, 138.635], [14, 138.088, 181.87199999999999, 149.345, 159.45999999999998], [14, 252.6, 307.33, 149.345, 159.45999999999998], [14, 329.222, 377.216, 149.345, 159.45999999999998], [14, 397.424, 417.632, 149.345, 159.45999999999998], [14, 487.518, 532.144, 149.345, 159.45999999999998], [14, 602.03, 656.76, 149.345, 159.45999999999998], [14, 678.6519999999999, 725.804, 149.345, 159.45999999999998], [14, 743.486, 762.852, 149.345, 159.45999999999998], [14, 82.51599999999999, 117.038, 170.765, 181.475], [14, 255.126, 260.178, 172.54999999999998, 180.88], [14, 354.48199999999997, 382.268, 172.54999999999998, 180.88], [14, 82.51599999999999, 149.876, 204.08499999999998, 214.795], [14, 82.51599999999999, 189.45, 221.935, 232.64499999999998], [14, 252.6, 263.546, 223.72, 232.04999999999998], [14, 357.84999999999997, 382.268, 223.72, 232.04999999999998], [14, 431.94599999999997, 585.1899999999999, 221.935, 232.64499999999998], [14, 603.7139999999999, 608.766, 223.72, 232.04999999999998], [14, 703.9119999999999, 730.014, 223.72, 232.04999999999998], [14, 431.94599999999997, 471.52, 235.61999999999998, 246.32999999999998], [14, 85.042, 250.07399999999998, 332.60499999999996, 343.315], [14, 475.72999999999996, 538.038, 333.2, 343.315], [14, 106.934, 224.814, 354.025, 364.14], [14, 285.438, 307.33, 354.025, 364.14], [14, 622.2379999999999, 719.068, 354.025, 364.14], [14, 89.252, 99.356, 371.875, 452.2], [14, 106.934, 224.814, 381.395, 391.51], [14, 285.438, 388.162, 381.395, 391.51], [14, 442.05, 490.88599999999997, 381.395, 391.51], [14, 622.2379999999999, 662.654, 381.395, 391.51], [14, 106.934, 224.814, 407.575, 417.69], [14, 285.438, 357.008, 407.575, 417.69], [14, 442.05, 538.88, 407.575, 417.69], [14, 622.2379999999999, 724.12, 407.575, 417.69], [14, 106.934, 181.87199999999999, 430.78, 440.895], [14, 285.438, 362.06, 430.78, 440.895], [14, 285.438, 344.378, 452.2, 462.90999999999997], [14, 84.2, 303.962, 478.97499999999997, 490.875], [14, 475.72999999999996, 559.088, 478.97499999999997, 490.875], [14, 622.2379999999999, 708.122, 478.97499999999997, 490.875], [14, 95.988, 718.226, 498.60999999999996, 509.32], [14, 135.56199999999998, 695.492, 509.32, 519.435]]
2026-08-10 11:46:18,141 INFO     29 [qwen-vl-text] ═══ DONE ═══ 48 positions, pages=1, time=25.5s
2026-08-10 11:46:18,141 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:46:18,142 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:46:18,142 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 11:46:18,142 INFO     29 [qwen-vl-text] positions(35): [[15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:46:18,142 INFO     29 [qwen-vl-text] page grouping: [15], lines per page: [35]
2026-08-10 11:46:18,386 INFO     29 [qwen-vl-text] page=15, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 11:46:18,390 INFO     29 [qwen-vl-text] LLM extraction start, text_len=297
2026-08-10 11:46:18,390 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:46:18,390 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 477, \"bbox_end\": 511, \"encounter_dates\": [\"2025-11-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "电子发票(普通发票)\n发票号码：25447000001429974977\n开票日期：2025年11月05日\n广东省税务局\n购买方信息\n名称：\n统一社会信用代码/纳税人识别号：\n销售方信息\n名称：阿里健康大药房医药连锁有限公司\n统一社会信用代码/纳税人识别号：91440101681325547Y\n项目名称\n规格型号\n单位\n数量\n单价\n金额\n税率/征收率\n税额\n*化学药品制剂*布地奈德\n盒\n3\n176.70\n530.09\n13%\n68.91\n福莫特罗吸入粉雾剂\n合计\n￥530.09\n￥68.91\n价税合计（大写）\n伍佰玖拾玖圆整\n(小写)￥599.00\n备注\n开票人：董茜玲\nCS 扫描全能王",
    "role": "user"
  }
]
2026-08-10 11:46:20,772 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:46:20,772 INFO     29 [qwen-vl-text] LLM output (len=422):
{
  "encounter_date": "2025-11-05",
  "pharmacy": "阿里健康大药房医药连锁有限公司",
  "medications": [
    {
      "name": "布地奈德福莫特罗吸入粉雾剂",
      "specification": null,
      "dosage": null,
      "quantity": 3,
      "unit_price": 176.70,
      "total_price": 530.09,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 599.00,
  "payment_method": null
}
2026-08-10 11:46:20,772 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-11-05]
2026-08-10 11:46:20,777 INFO     29 [qwen-vl-text] coord API call start, page=15, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=848797, prompt_len=1015
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共35行）
["电子发票(普通发票)", "发票号码：25447000001429974977", "开票日期：2025年11月05日", "广东省税务局", "购买方信息", "名称：", "统一社会信用代码/纳税人识别号：", "销售方信息", "名称：阿里健康大药房医药连锁有限公司", "统一社会信用代码/纳税人识别号：91440101681325547Y", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*化学药品制剂*布地奈德", "盒", "3", "176.70", "530.09", "13%", "68.91", "福莫特罗吸入粉雾剂", "合计", "￥530.09", "￥68.91", "价税合计（大写）", "伍佰玖拾玖圆整", "(小写)￥599.00", "备注", "开票人：董茜玲", "CS 扫描全能王"]

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
2026-08-10 11:46:36,949 INFO     29 [qwen-vl-text] coord API raw response (len=2841):
[
	{"text": "电子发票(普通发票)", "bbox": [340, 66, 630, 107]},
	{"text": "发票号码：25447000001429974977", "bbox": [728, 82, 961, 103]},
	{"text": "开票日期：2025年11月05日", "bbox": [727, 126, 916, 146]},
	{"text": "广东省税务局", "bbox": [458, 152, 526, 173]},
	{"text": "购买方信息", "bbox": [43, 220, 57, 336], "bbox_2d": [43, 220, 57, 336]},
	{"text": "名称：", "bbox": [67, 250, 88, 270], "bbox_2d": [67, 250, 88, 270]},
	{"text": "统一社会信用代码/纳税人识别号：", "bbox": [67, 275, 283, 295], "bbox_2d": [67, 275, 283, 295]},
	{"text": "销售方信息", "bbox": [507, 220, 521, 336], "bbox_2d": [507, 220, 521, 336]},
	{"text": "名称：阿里健康大药房医药连锁有限公司", "bbox": [530, 250, 791, 270], "bbox_2d": [530, 250, 791, 270]},
	{"text": "统一社会信用代码/纳税人识别号：91440101681325547Y", "bbox": [530, 275, 958, 295], "bbox_2d": [530, 275, 958, 295]},
	{"text": "项目名称", "bbox": [92, 354, 150, 373], "bbox_2d": [92, 354, 150, 373]},
	{"text": "规格型号", "bbox": [206, 354, 264, 373], "bbox_2d": [206, 354, 264, 373]},
	{"text": "单位", "bbox": [326, 354, 364, 373], "bbox_2d": [326, 354, 364, 373]},
	{"text": "数量", "bbox": [450, 354, 488, 373], "bbox_2d": [450, 354, 488, 373]},
	{"text": "单价", "bbox": [565, 354, 603, 373], "bbox_2d": [565, 354, 603, 373]},
	{"text": "金额", "bbox": [685, 354, 722, 373], "bbox_2d": [685, 354, 722, 373]},
	{"text": "税率/征收率", "bbox": [757, 354, 838, 373], "bbox_2d": [757, 354, 838, 373]},
	{"text": "税额", "bbox": [923, 354, 961, 373], "bbox_2d": [923, 354, 961, 373]},
	{"text": "*化学药品制剂*布地奈德", "bbox": [36, 385, 196, 405], "bbox_2d": [36, 385, 196, 405]},
	{"text": "盒", "bbox": [338, 385, 354, 405], "bbox_2d": [338, 385, 354, 405]},
	{"text": "3", "bbox": [480, 387, 489, 404], "bbox_2d": [480, 387, 489, 404]},
	{"text": "176.70", "bbox": [560, 387, 603, 404], "bbox_2d": [560, 387, 603, 404]},
	{"text": "530.09", "bbox": [679, 387, 722, 404], "bbox_2d": [679, 387, 722, 404]},
	{"text": "13%", "bbox": [770, 387, 792, 404], "bbox_2d": [770, 387, 792, 404]},
	{"text": "68.91", "bbox": [924, 387, 960, 404], "bbox_2d": [924, 387, 960, 404]},
	{"text": "福莫特罗吸入粉雾剂", "bbox": [36, 413, 168, 434], "bbox_2d": [36, 413, 168, 434]},
	{"text": "合计", "bbox": [106, 610, 119, 629], "bbox_2d": [106, 610, 119, 629]},
	{"text": "￥530.09", "bbox": [669, 611, 722, 629], "bbox_2d": [669, 611, 722, 629]},
	{"text": "￥68.91", "bbox": [915, 611, 960, 629], "bbox_2d": [915, 611, 960, 629]},
	{"text": "价税合计（大写）", "bbox": [100, 656, 208, 676], "bbox_2d": [100, 656, 208, 676]},
	{"text": "伍佰玖拾玖圆整", "bbox": [314, 656, 417, 676], "bbox_2d": [314, 656, 417, 676]},
	{"text": "(小写)￥599.00", "bbox": [685, 656, 790, 676], "bbox_2d": [685, 656, 790, 676]},
	{"text": "备注", "bbox": [43, 737, 57, 780], "bbox_2d": [43, 737, 57, 780]},
	{"text": "开票人：董茜玲", "bbox": [100, 853, 202, 873], "bbox_2d": [100, 853, 202, 873]},
	{"text": "CS 扫描全能王", "bbox": [903, 942, 984, 962], "bbox_2d": [903, 942, 984, 962]}
]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord API: raw_items=35, valid_items=35, elapsed=16.2s
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[0]: text=电子发票(普通发票), bbox=[340, 66, 630, 107]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[1]: text=发票号码：25447000001429974977, bbox=[728, 82, 961, 103]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[2]: text=开票日期：2025年11月05日, bbox=[727, 126, 916, 146]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[3]: text=广东省税务局, bbox=[458, 152, 526, 173]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[4]: text=购买方信息, bbox=[43, 220, 57, 336]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[5]: text=名称：, bbox=[67, 250, 88, 270]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[6]: text=统一社会信用代码/纳税人识别号：, bbox=[67, 275, 283, 295]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[7]: text=销售方信息, bbox=[507, 220, 521, 336]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[8]: text=名称：阿里健康大药房医药连锁有限公司, bbox=[530, 250, 791, 270]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[9]: text=统一社会信用代码/纳税人识别号：91440101681325547Y, bbox=[530, 275, 958, 295]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[10]: text=项目名称, bbox=[92, 354, 150, 373]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[11]: text=规格型号, bbox=[206, 354, 264, 373]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[12]: text=单位, bbox=[326, 354, 364, 373]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[13]: text=数量, bbox=[450, 354, 488, 373]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[14]: text=单价, bbox=[565, 354, 603, 373]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[15]: text=金额, bbox=[685, 354, 722, 373]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[16]: text=税率/征收率, bbox=[757, 354, 838, 373]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[17]: text=税额, bbox=[923, 354, 961, 373]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[18]: text=*化学药品制剂*布地奈德, bbox=[36, 385, 196, 405]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[19]: text=盒, bbox=[338, 385, 354, 405]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[20]: text=3, bbox=[480, 387, 489, 404]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[21]: text=176.70, bbox=[560, 387, 603, 404]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[22]: text=530.09, bbox=[679, 387, 722, 404]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[23]: text=13%, bbox=[770, 387, 792, 404]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[24]: text=68.91, bbox=[924, 387, 960, 404]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[25]: text=福莫特罗吸入粉雾剂, bbox=[36, 413, 168, 434]
2026-08-10 11:46:36,950 INFO     29 [qwen-vl-text] coord item[26]: text=合计, bbox=[106, 610, 119, 629]
2026-08-10 11:46:36,951 INFO     29 [qwen-vl-text] coord item[27]: text=￥530.09, bbox=[669, 611, 722, 629]
2026-08-10 11:46:36,951 INFO     29 [qwen-vl-text] coord item[28]: text=￥68.91, bbox=[915, 611, 960, 629]
2026-08-10 11:46:36,951 INFO     29 [qwen-vl-text] coord item[29]: text=价税合计（大写）, bbox=[100, 656, 208, 676]
2026-08-10 11:46:36,951 INFO     29 [qwen-vl-text] coord item[30]: text=伍佰玖拾玖圆整, bbox=[314, 656, 417, 676]
2026-08-10 11:46:36,951 INFO     29 [qwen-vl-text] coord item[31]: text=(小写)￥599.00, bbox=[685, 656, 790, 676]
2026-08-10 11:46:36,951 INFO     29 [qwen-vl-text] coord item[32]: text=备注, bbox=[43, 737, 57, 780]
2026-08-10 11:46:36,951 INFO     29 [qwen-vl-text] coord item[33]: text=开票人：董茜玲, bbox=[100, 853, 202, 873]
2026-08-10 11:46:36,951 INFO     29 [qwen-vl-text] coord item[34]: text=CS 扫描全能王, bbox=[903, 942, 984, 962]
2026-08-10 11:46:36,951 INFO     29 [qwen-vl-text] page=15 — 35/35 coords, api_time=16.2s
2026-08-10 11:46:36,951 INFO     29 [qwen-vl-text] new_positions (35):
[[15, 286.28, 530.46, 39.269999999999996, 63.665], [15, 612.976, 809.1619999999999, 48.79, 61.285], [15, 612.134, 771.2719999999999, 74.97, 86.86999999999999], [15, 385.63599999999997, 442.892, 90.44, 102.935], [15, 36.205999999999996, 47.994, 130.9, 199.92], [15, 56.414, 74.096, 148.75, 160.65], [15, 56.414, 238.286, 163.625, 175.525], [15, 426.894, 438.68199999999996, 130.9, 199.92], [15, 446.26, 666.0219999999999, 148.75, 160.65], [15, 446.26, 806.636, 163.625, 175.525], [15, 77.464, 126.3, 210.63, 221.935], [15, 173.452, 222.28799999999998, 210.63, 221.935], [15, 274.492, 306.488, 210.63, 221.935], [15, 378.9, 410.89599999999996, 210.63, 221.935], [15, 475.72999999999996, 507.726, 210.63, 221.935], [15, 576.77, 607.924, 210.63, 221.935], [15, 637.394, 705.596, 210.63, 221.935], [15, 777.1659999999999, 809.1619999999999, 210.63, 221.935], [15, 30.311999999999998, 165.03199999999998, 229.075, 240.975], [15, 284.596, 298.068, 229.075, 240.975], [15, 404.15999999999997, 411.738, 230.265, 240.38], [15, 471.52, 507.726, 230.265, 240.38], [15, 571.718, 607.924, 230.265, 240.38], [15, 648.34, 666.864, 230.265, 240.38], [15, 778.0079999999999, 808.3199999999999, 230.265, 240.38], [15, 30.311999999999998, 141.456, 245.73499999999999, 258.22999999999996], [15, 89.252, 100.198, 362.95, 374.255], [15, 563.298, 607.924, 363.54499999999996, 374.255], [15, 770.43, 808.3199999999999, 363.54499999999996, 374.255], [15, 84.2, 175.136, 390.32, 402.21999999999997], [15, 264.388, 351.114, 390.32, 402.21999999999997], [15, 576.77, 665.18, 390.32, 402.21999999999997], [15, 36.205999999999996, 47.994, 438.515, 464.09999999999997], [15, 84.2, 170.084, 507.53499999999997, 519.435], [15, 760.326, 828.528, 560.49, 572.39]]
2026-08-10 11:46:36,951 INFO     29 [qwen-vl-text] ═══ DONE ═══ 35 positions, pages=1, time=18.8s
2026-08-10 11:46:36,951 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:46:36,957 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:46:36,957 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 11:46:36,958 INFO     29 [qwen-vl-text] positions(46): [[17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:46:36,958 INFO     29 [qwen-vl-text] page grouping: [17], lines per page: [46]
2026-08-10 11:46:37,206 INFO     29 [qwen-vl-text] page=17, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 11:46:37,209 INFO     29 [qwen-vl-text] LLM extraction start, text_len=497
2026-08-10 11:46:37,209 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:46:37,209 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 545, \"bbox_end\": 590, \"encounter_dates\": [\"2025-11-24\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "广东省医疗门诊收费票据（电子）\n广东省\n财政部监制\n票据代码：44\n票据号码：9148286284\n校验码：89a81f\n交款人\n开票日期：2025-11-24\n项目名称\n数量/单位\n金额（元）\n备注\n项目名称\n数量/单位\n金额（元）\n备注\n西药费\n1\n0.25\n以下是清单项\n醋酸泼尼松片（国基）\n6\n0.25\n金额合计（大写）贰角伍分\n(小写)0.25\n业务流水号：SF10481981\n门\n就诊日期：20251124\n其他信息\n医疗机构类型：综合医院\n医保类型：现金(自费)\n医保编号：\n性别：女\n医保统筹基金支付：0.00\n其他支付：0.00\n个人账户支付：0.00\n个人现金支付：0.25\n个人自付：0.00\n个人自费：0.25\n政策性减免：\n收款单位（章）\n人民医院\n复核人：吴亮梅\n收款人：吴亮梅\n说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。\n单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dipj.czt.gd.gov.cn/billcheck查验本省财政电子票据。",
    "role": "user"
  }
]
2026-08-10 11:46:37,211 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:46:37.211+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 24, "failed": 0, "current": {"38277e3a94b011f1bd9827cf206dfa2d": {"id": "38277e3a94b011f1bd9827cf206dfa2d", "doc_id": "370244ae94b011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479740, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362000249, "task_type": "dataflow", "root_trace_id": "96cd8dab6bb7455194a762d3f16e1d52", "root_traceparent": "00-96cd8dab6bb7455194a762d3f16e1d52-1e133766dfd81337-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:46:39,278 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:46:39,278 INFO     29 [qwen-vl-text] LLM output (len=398):
{
  "encounter_date": "2025-11-24",
  "pharmacy": "人民医院",
  "medications": [
    {
      "name": "醋酸泼尼松片",
      "specification": null,
      "dosage": null,
      "quantity": 6,
      "unit_price": null,
      "total_price": 0.25,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 0.25,
  "payment_method": "现金"
}
2026-08-10 11:46:39,278 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-11-24]
2026-08-10 11:46:39,282 INFO     29 [qwen-vl-text] coord API call start, page=17, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=866040, prompt_len=1248
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共46行）
["广东省医疗门诊收费票据（电子）", "广东省", "财政部监制", "票据代码：44", "票据号码：9148286284", "校验码：89a81f", "交款人", "开票日期：2025-11-24", "项目名称", "数量/单位", "金额（元）", "备注", "项目名称", "数量/单位", "金额（元）", "备注", "西药费", "1", "0.25", "以下是清单项", "醋酸泼尼松片（国基）", "6", "0.25", "金额合计（大写）贰角伍分", "(小写)0.25", "业务流水号：SF10481981", "门", "就诊日期：20251124", "其他信息", "医疗机构类型：综合医院", "医保类型：现金(自费)", "医保编号：", "性别：女", "医保统筹基金支付：0.00", "其他支付：0.00", "个人账户支付：0.00", "个人现金支付：0.25", "个人自付：0.00", "个人自费：0.25", "政策性减免：", "收款单位（章）", "人民医院", "复核人：吴亮梅", "收款人：吴亮梅", "说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。", "单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dipj.czt.gd.gov.cn/billcheck查验本省财政电子票据。"]

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
2026-08-10 11:47:01,531 INFO     29 [qwen-vl-text] coord API raw response (len=3870):
[
	{"text": "广东省医疗门诊收费票据（电子）", "bbox": [318, 57, 672, 93]},
	{"text": "广东省", "bbox": [478, 91, 522, 109], "bbox": [478, 91, 522, 109]},
	{"text": "财政部监制", "bbox": [465, 120, 538, 145], "bbox": [465, 120, 538, 145]},
	{"text": "票据代码：44", "bbox": [116, 151, 188, 168], "bbox": [116, 151, 188, 168]},
	{"text": "票据号码：9148286284", "bbox": [629, 151, 746, 168], "bbox": [629, 151, 746, 168]},
	{"text": "校验码：89a81f", "bbox": [629, 177, 722, 194], "bbox": [629, 177, 722, 194]},
	{"text": "交款人", "bbox": [116, 202, 152, 219], "bbox": [116, 202, 152, 219]},
	{"text": "开票日期：2025-11-24", "bbox": [629, 202, 746, 219], "bbox": [629, 202, 746, 219]},
	{"text": "项目名称", "bbox": [179, 238, 228, 254], "bbox": [179, 238, 228, 254]},
	{"text": "数量/单位", "bbox": [306, 238, 366, 254], "bbox": [306, 238, 366, 254]},
	{"text": "金额（元）", "bbox": [389, 238, 443, 254], "bbox": [389, 238, 443, 254]},
	{"text": "备注", "bbox": [464, 238, 488, 254], "bbox": [464, 238, 488, 254]},
	{"text": "项目名称", "bbox": [562, 238, 611, 254], "bbox": [562, 238, 611, 254]},
	{"text": "数量/单位", "bbox": [687, 238, 745, 254], "bbox": [687, 238, 745, 254]},
	{"text": "金额（元）", "bbox": [769, 238, 821, 254], "bbox": [769, 238, 821, 254]},
	{"text": "备注", "bbox": [842, 238, 865, 254], "bbox": [842, 238, 865, 254]},
	{"text": "西药费", "bbox": [119, 273, 156, 290], "bbox": [119, 273, 156, 290]},
	{"text": "1", "bbox": [308, 274, 314, 290], "bbox": [308, 274, 314, 290]},
	{"text": "0.25", "bbox": [422, 274, 449, 290], "bbox": [422, 274, 449, 290]},
	{"text": "以下是清单项", "bbox": [119, 328, 193, 346], "bbox": [119, 328, 193, 346]},
	{"text": "醋酸泼尼松片（国基）", "bbox": [119, 359, 237, 376], "bbox": [119, 359, 237, 376]},
	{"text": "6", "bbox": [308, 360, 315, 376], "bbox": [308, 360, 315, 376]},
	{"text": "0.25", "bbox": [422, 360, 449, 376], "bbox": [422, 360, 449, 376]},
	{"text": "金额合计（大写）贰角伍分", "bbox": [123, 542, 267, 560], "bbox": [123, 542, 267, 560]},
	{"text": "(小写)0.25", "bbox": [552, 542, 615, 559], "bbox": [552, 542, 615, 559]},
	{"text": "业务流水号：SF10481981", "bbox": [147, 578, 276, 595], "bbox": [147, 578, 276, 595]},
	{"text": "门", "bbox": [344, 577, 355, 595], "bbox": [344, 577, 355, 595]},
	{"text": "就诊日期：20251124", "bbox": [713, 577, 817, 594], "bbox": [713, 577, 817, 594]},
	{"text": "其他信息", "bbox": [127, 609, 140, 743], "bbox": [127, 609, 140, 743]},
	{"text": "医疗机构类型：综合医院", "bbox": [147, 623, 277, 640], "bbox": [147, 623, 277, 640]},
	{"text": "医保类型：现金(自费)", "bbox": [344, 622, 458, 640], "bbox": [344, 622, 458, 640]},
	{"text": "医保编号：", "bbox": [518, 623, 570, 640], "bbox": [518, 623, 570, 640]},
	{"text": "性别：女", "bbox": [713, 622, 757, 640], "bbox": [713, 622, 757, 640]},
	{"text": "医保统筹基金支付：0.00", "bbox": [147, 668, 277, 685], "bbox": [147, 668, 277, 685]},
	{"text": "其他支付：0.00", "bbox": [344, 668, 423, 685], "bbox": [344, 668, 423, 685]},
	{"text": "个人账户支付：0.00", "bbox": [518, 668, 623, 685], "bbox": [518, 668, 623, 685]},
	{"text": "个人现金支付：0.25", "bbox": [713, 668, 817, 685], "bbox": [713, 668, 817, 685]},
	{"text": "个人自付：0.00", "bbox": [147, 708, 230, 725], "bbox": [147, 708, 230, 725]},
	{"text": "个人自费：0.25", "bbox": [344, 708, 423, 725], "bbox": [344, 708, 423, 725]},
	{"text": "政策性减免：", "bbox": [344, 744, 411, 761], "bbox": [344, 744, 411, 761]},
	{"text": "收款单位（章）", "bbox": [121, 790, 202, 809], "bbox": [121, 790, 202, 809]},
	{"text": "人民医院", "bbox": [327, 788, 367, 807], "bbox": [327, 788, 367, 807]},
	{"text": "复核人：吴亮梅", "bbox": [557, 788, 637, 807], "bbox": [557, 788, 637, 807]},
	{"text": "收款人：吴亮梅", "bbox": [717, 788, 797, 807], "bbox": [717, 788, 797, 807]},
	{"text": "说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。", "bbox": [135, 825, 819, 842], "bbox": [135, 825, 819, 842]},
	{"text": "单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dipj.czt.gd.gov.cn/billcheck查验本省财政电子票据。", "bbox": [178, 842, 797, 859], "bbox": [178, 842, 797, 859]}
]
2026-08-10 11:47:01,532 INFO     29 [qwen-vl-text] coord API: raw_items=46, valid_items=46, elapsed=22.2s
2026-08-10 11:47:01,532 INFO     29 [qwen-vl-text] coord item[0]: text=广东省医疗门诊收费票据（电子）, bbox=[318, 57, 672, 93]
2026-08-10 11:47:01,532 INFO     29 [qwen-vl-text] coord item[1]: text=广东省, bbox=[478, 91, 522, 109]
2026-08-10 11:47:01,532 INFO     29 [qwen-vl-text] coord item[2]: text=财政部监制, bbox=[465, 120, 538, 145]
2026-08-10 11:47:01,532 INFO     29 [qwen-vl-text] coord item[3]: text=票据代码：44, bbox=[116, 151, 188, 168]
2026-08-10 11:47:01,532 INFO     29 [qwen-vl-text] coord item[4]: text=票据号码：9148286284, bbox=[629, 151, 746, 168]
2026-08-10 11:47:01,532 INFO     29 [qwen-vl-text] coord item[5]: text=校验码：89a81f, bbox=[629, 177, 722, 194]
2026-08-10 11:47:01,532 INFO     29 [qwen-vl-text] coord item[6]: text=交款人, bbox=[116, 202, 152, 219]
2026-08-10 11:47:01,532 INFO     29 [qwen-vl-text] coord item[7]: text=开票日期：2025-11-24, bbox=[629, 202, 746, 219]
2026-08-10 11:47:01,532 INFO     29 [qwen-vl-text] coord item[8]: text=项目名称, bbox=[179, 238, 228, 254]
2026-08-10 11:47:01,532 INFO     29 [qwen-vl-text] coord item[9]: text=数量/单位, bbox=[306, 238, 366, 254]
2026-08-10 11:47:01,532 INFO     29 [qwen-vl-text] coord item[10]: text=金额（元）, bbox=[389, 238, 443, 254]
2026-08-10 11:47:01,532 INFO     29 [qwen-vl-text] coord item[11]: text=备注, bbox=[464, 238, 488, 254]
2026-08-10 11:47:01,532 INFO     29 [qwen-vl-text] coord item[12]: text=项目名称, bbox=[562, 238, 611, 254]
2026-08-10 11:47:01,533 INFO     29 [qwen-vl-text] coord item[13]: text=数量/单位, bbox=[687, 238, 745, 254]
2026-08-10 11:47:01,533 INFO     29 [qwen-vl-text] coord item[14]: text=金额（元）, bbox=[769, 238, 821, 254]
2026-08-10 11:47:01,533 INFO     29 [qwen-vl-text] coord item[15]: text=备注, bbox=[842, 238, 865, 254]
2026-08-10 11:47:01,533 INFO     29 [qwen-vl-text] coord item[16]: text=西药费, bbox=[119, 273, 156, 290]
2026-08-10 11:47:01,533 INFO     29 [qwen-vl-text] coord item[17]: text=1, bbox=[308, 274, 314, 290]
2026-08-10 11:47:01,533 INFO     29 [qwen-vl-text] coord item[18]: text=0.25, bbox=[422, 274, 449, 290]
2026-08-10 11:47:01,533 INFO     29 [qwen-vl-text] coord item[19]: text=以下是清单项, bbox=[119, 328, 193, 346]
2026-08-10 11:47:01,533 INFO     29 [qwen-vl-text] coord item[20]: text=醋酸泼尼松片（国基）, bbox=[119, 359, 237, 376]
2026-08-10 11:47:01,533 INFO     29 [qwen-vl-text] coord item[21]: text=6, bbox=[308, 360, 315, 376]
2026-08-10 11:47:01,533 INFO     29 [qwen-vl-text] coord item[22]: text=0.25, bbox=[422, 360, 449, 376]
2026-08-10 11:47:01,533 INFO     29 [qwen-vl-text] coord item[23]: text=金额合计（大写）贰角伍分, bbox=[123, 542, 267, 560]
2026-08-10 11:47:01,533 INFO     29 [qwen-vl-text] coord item[24]: text=(小写)0.25, bbox=[552, 542, 615, 559]
2026-08-10 11:47:01,533 INFO     29 [qwen-vl-text] coord item[25]: text=业务流水号：SF10481981, bbox=[147, 578, 276, 595]
2026-08-10 11:47:01,533 INFO     29 [qwen-vl-text] coord item[26]: text=门, bbox=[344, 577, 355, 595]
2026-08-10 11:47:01,533 INFO     29 [qwen-vl-text] coord item[27]: text=就诊日期：20251124, bbox=[713, 577, 817, 594]
2026-08-10 11:47:01,533 INFO     29 [qwen-vl-text] coord item[28]: text=其他信息, bbox=[127, 609, 140, 743]
2026-08-10 11:47:01,533 INFO     29 [qwen-vl-text] coord item[29]: text=医疗机构类型：综合医院, bbox=[147, 623, 277, 640]
2026-08-10 11:47:01,533 INFO     29 [qwen-vl-text] coord item[30]: text=医保类型：现金(自费), bbox=[344, 622, 458, 640]
2026-08-10 11:47:01,533 INFO     29 [qwen-vl-text] coord item[31]: text=医保编号：, bbox=[518, 623, 570, 640]
2026-08-10 11:47:01,534 INFO     29 [qwen-vl-text] coord item[32]: text=性别：女, bbox=[713, 622, 757, 640]
2026-08-10 11:47:01,534 INFO     29 [qwen-vl-text] coord item[33]: text=医保统筹基金支付：0.00, bbox=[147, 668, 277, 685]
2026-08-10 11:47:01,534 INFO     29 [qwen-vl-text] coord item[34]: text=其他支付：0.00, bbox=[344, 668, 423, 685]
2026-08-10 11:47:01,534 INFO     29 [qwen-vl-text] coord item[35]: text=个人账户支付：0.00, bbox=[518, 668, 623, 685]
2026-08-10 11:47:01,534 INFO     29 [qwen-vl-text] coord item[36]: text=个人现金支付：0.25, bbox=[713, 668, 817, 685]
2026-08-10 11:47:01,534 INFO     29 [qwen-vl-text] coord item[37]: text=个人自付：0.00, bbox=[147, 708, 230, 725]
2026-08-10 11:47:01,534 INFO     29 [qwen-vl-text] coord item[38]: text=个人自费：0.25, bbox=[344, 708, 423, 725]
2026-08-10 11:47:01,534 INFO     29 [qwen-vl-text] coord item[39]: text=政策性减免：, bbox=[344, 744, 411, 761]
2026-08-10 11:47:01,534 INFO     29 [qwen-vl-text] coord item[40]: text=收款单位（章）, bbox=[121, 790, 202, 809]
2026-08-10 11:47:01,534 INFO     29 [qwen-vl-text] coord item[41]: text=人民医院, bbox=[327, 788, 367, 807]
2026-08-10 11:47:01,534 INFO     29 [qwen-vl-text] coord item[42]: text=复核人：吴亮梅, bbox=[557, 788, 637, 807]
2026-08-10 11:47:01,534 INFO     29 [qwen-vl-text] coord item[43]: text=收款人：吴亮梅, bbox=[717, 788, 797, 807]
2026-08-10 11:47:01,534 INFO     29 [qwen-vl-text] coord item[44]: text=说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。, bbox=[135, 825, 819, 842]
2026-08-10 11:47:01,534 INFO     29 [qwen-vl-text] coord item[45]: text=单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dipj.czt.gd.gov.cn/billcheck查验本省财政电子票据。, bbox=[178, 842, 797, 859]
2026-08-10 11:47:01,535 INFO     29 [qwen-vl-text] page=17 — 46/46 coords, api_time=22.2s
2026-08-10 11:47:01,535 INFO     29 [qwen-vl-text] new_positions (46):
[[17, 267.756, 565.824, 33.915, 55.335], [17, 402.476, 439.524, 54.144999999999996, 64.855], [17, 391.53, 452.996, 71.39999999999999, 86.27499999999999], [17, 97.672, 158.296, 89.845, 99.96], [17, 529.6179999999999, 628.132, 89.845, 99.96], [17, 529.6179999999999, 607.924, 105.315, 115.42999999999999], [17, 97.672, 127.984, 120.19, 130.305], [17, 529.6179999999999, 628.132, 120.19, 130.305], [17, 150.718, 191.976, 141.60999999999999, 151.13], [17, 257.652, 308.17199999999997, 141.60999999999999, 151.13], [17, 327.538, 373.006, 141.60999999999999, 151.13], [17, 390.688, 410.89599999999996, 141.60999999999999, 151.13], [17, 473.204, 514.462, 141.60999999999999, 151.13], [17, 578.454, 627.29, 141.60999999999999, 151.13], [17, 647.4979999999999, 691.2819999999999, 141.60999999999999, 151.13], [17, 708.9639999999999, 728.3299999999999, 141.60999999999999, 151.13], [17, 100.198, 131.352, 162.435, 172.54999999999998], [17, 259.336, 264.388, 163.03, 172.54999999999998], [17, 355.324, 378.058, 163.03, 172.54999999999998], [17, 100.198, 162.506, 195.16, 205.87], [17, 100.198, 199.554, 213.605, 223.72], [17, 259.336, 265.23, 214.2, 223.72], [17, 355.324, 378.058, 214.2, 223.72], [17, 103.566, 224.814, 322.49, 333.2], [17, 464.784, 517.8299999999999, 322.49, 332.60499999999996], [17, 123.774, 232.392, 343.90999999999997, 354.025], [17, 289.64799999999997, 298.90999999999997, 343.315, 354.025], [17, 600.346, 687.914, 343.315, 353.43], [17, 106.934, 117.88, 362.35499999999996, 442.085], [17, 123.774, 233.23399999999998, 370.685, 380.79999999999995], [17, 289.64799999999997, 385.63599999999997, 370.09, 380.79999999999995], [17, 436.156, 479.94, 370.685, 380.79999999999995], [17, 600.346, 637.394, 370.09, 380.79999999999995], [17, 123.774, 233.23399999999998, 397.46, 407.575], [17, 289.64799999999997, 356.166, 397.46, 407.575], [17, 436.156, 524.566, 397.46, 407.575], [17, 600.346, 687.914, 397.46, 407.575], [17, 123.774, 193.66, 421.26, 431.375], [17, 289.64799999999997, 356.166, 421.26, 431.375], [17, 289.64799999999997, 346.062, 442.68, 452.79499999999996], [17, 101.88199999999999, 170.084, 470.04999999999995, 481.35499999999996], [17, 275.334, 309.014, 468.85999999999996, 480.16499999999996], [17, 468.99399999999997, 536.3539999999999, 468.85999999999996, 480.16499999999996], [17, 603.7139999999999, 671.074, 468.85999999999996, 480.16499999999996], [17, 113.67, 689.598, 490.875, 500.98999999999995], [17, 149.876, 671.074, 500.98999999999995, 511.10499999999996]]
2026-08-10 11:47:01,535 INFO     29 [qwen-vl-text] ═══ DONE ═══ 46 positions, pages=1, time=24.6s
2026-08-10 11:47:01,535 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:47:01,536 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:47:01,536 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 11:47:01,537 INFO     29 [qwen-vl-text] positions(44): [[18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:47:01,537 INFO     29 [qwen-vl-text] page grouping: [18], lines per page: [44]
2026-08-10 11:47:01,699 INFO     29 [qwen-vl-text] page=18, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:47:01,702 INFO     29 [qwen-vl-text] LLM extraction start, text_len=397
2026-08-10 11:47:01,703 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:47:01,703 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 593, \"bbox_end\": 636, \"encounter_dates\": [\"2026-01-20\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "10:15\n淘\n交易成功\n医药仁康堂医药专营店>\n【信必可】布地奈德福莫特罗[\n¥213\n放心买药\n正品保障\n1盒装\n不支持7天无理由 假一赔四>\nx1\n专业药师在线服务\n上天猫放心买药\n用药小贴士 1.哮喘。2.慢性阻塞性肺疾病(慢阻肺;...\n申请售后\n商品总价\n¥213\n运费(含服务费)\n¥8\n应付款\n¥221^\n订单信息 2026-01-20\n收起^\n订单编号\n4501919772001020746\n交易快照\n发生交易争议时，可作为判断依据>\n成交时间\n2026-01-26 22:25:02\n发货时间\n2026-01-21 12:24:52\n付款时间\n2026-01-20 19:25:06\n创建时间\n2026-01-20 19:24:30\n支付宝交易号\n2026012022001134951454085519\n天猫积分\n获得106点积分>\n客服\n更多\n查看处方\n查看物流\n评价",
    "role": "user"
  }
]
2026-08-10 11:47:03,773 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:47:03,774 INFO     29 [qwen-vl-text] LLM output (len=405):
{
  "encounter_date": "2026-01-20",
  "pharmacy": "医药仁康堂医药专营店",
  "medications": [
    {
      "name": "布地奈德福莫特罗",
      "specification": "1盒装",
      "dosage": null,
      "quantity": 1,
      "unit_price": 213,
      "total_price": 213,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 221,
  "payment_method": "支付宝"
}
2026-08-10 11:47:03,774 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-20]
2026-08-10 11:47:03,775 INFO     29 [qwen-vl-text] coord API call start, page=18, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=822515, prompt_len=1142
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共44行）
["10:15", "淘", "交易成功", "医药仁康堂医药专营店>", "【信必可】布地奈德福莫特罗[", "¥213", "放心买药", "正品保障", "1盒装", "不支持7天无理由 假一赔四>", "x1", "专业药师在线服务", "上天猫放心买药", "用药小贴士 1.哮喘。2.慢性阻塞性肺疾病(慢阻肺;...", "申请售后", "商品总价", "¥213", "运费(含服务费)", "¥8", "应付款", "¥221^", "订单信息 2026-01-20", "收起^", "订单编号", "4501919772001020746", "交易快照", "发生交易争议时，可作为判断依据>", "成交时间", "2026-01-26 22:25:02", "发货时间", "2026-01-21 12:24:52", "付款时间", "2026-01-20 19:25:06", "创建时间", "2026-01-20 19:24:30", "支付宝交易号", "2026012022001134951454085519", "天猫积分", "获得106点积分>", "客服", "更多", "查看处方", "查看物流", "评价"]

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
2026-08-10 11:47:16,148 INFO     29 [qwen-vl-text] coord API raw response (len=2330):
[
	{"text": "10:15", "bbox": [233, 13, 291, 27]},
	{"text": "淘", "bbox": [321, 13, 343, 27]},
	{"text": "交易成功", "bbox": [435, 57, 561, 80]},
	{"text": "医药仁康堂医药专营店>", "bbox": [224, 137, 466, 153]},
	{"text": "【信必可】布地奈德福莫特罗[", "bbox": [382, 177, 666, 193]},
	{"text": "¥213", "bbox": [718, 177, 770, 194]},
	{"text": "放心买药", "bbox": [304, 196, 340, 203]},
	{"text": "正品保障", "bbox": [303, 207, 341, 214]},
	{"text": "1盒装", "bbox": [370, 204, 423, 219]},
	{"text": "不支持7天无理由 假一赔四>", "bbox": [370, 230, 616, 245]},
	{"text": "x1", "bbox": [748, 231, 770, 244]},
	{"text": "专业药师在线服务", "bbox": [264, 239, 314, 245]},
	{"text": "上天猫放心买药", "bbox": [260, 247, 318, 254]},
	{"text": "用药小贴士 1.哮喘。2.慢性阻塞性肺疾病(慢阻肺;...", "bbox": [237, 275, 709, 291]},
	{"text": "申请售后", "bbox": [667, 317, 749, 333]},
	{"text": "商品总价", "bbox": [225, 367, 321, 384]},
	{"text": "¥213", "bbox": [715, 369, 770, 386]},
	{"text": "运费(含服务费)", "bbox": [225, 411, 365, 427]},
	{"text": "¥8", "bbox": [738, 411, 770, 428]},
	{"text": "应付款", "bbox": [225, 457, 298, 474]},
	{"text": "¥221^", "bbox": [681, 455, 770, 475]},
	{"text": "订单信息 2026-01-20", "bbox": [225, 520, 442, 537]},
	{"text": "收起^", "bbox": [706, 520, 770, 536]},
	{"text": "订单编号", "bbox": [225, 558, 309, 574]},
	{"text": "4501919772001020746", "bbox": [547, 558, 770, 574]},
	{"text": "交易快照", "bbox": [225, 595, 309, 611]},
	{"text": "发生交易争议时，可作为判断依据>", "bbox": [436, 595, 763, 611]},
	{"text": "成交时间", "bbox": [225, 632, 309, 648]},
	{"text": "2026-01-26 22:25:02", "bbox": [569, 632, 770, 648]},
	{"text": "发货时间", "bbox": [225, 669, 309, 685]},
	{"text": "2026-01-21 12:24:52", "bbox": [569, 669, 770, 685]},
	{"text": "付款时间", "bbox": [225, 705, 309, 721]},
	{"text": "2026-01-20 19:25:06", "bbox": [569, 705, 770, 721]},
	{"text": "创建时间", "bbox": [225, 741, 309, 757]},
	{"text": "2026-01-20 19:24:30", "bbox": [569, 741, 770, 757]},
	{"text": "支付宝交易号", "bbox": [225, 777, 351, 793]},
	{"text": "2026012022001134951454085519", "bbox": [442, 777, 770, 793]},
	{"text": "天猫积分", "bbox": [225, 814, 309, 830]},
	{"text": "获得106点积分>", "bbox": [607, 814, 763, 830]},
	{"text": "客服", "bbox": [222, 876, 255, 889]},
	{"text": "更多", "bbox": [275, 876, 306, 889]},
	{"text": "查看处方", "bbox": [369, 864, 452, 880]},
	{"text": "查看物流", "bbox": [518, 864, 601, 880]},
	{"text": "评价", "bbox": [688, 865, 728, 880]}
]
2026-08-10 11:47:16,149 INFO     29 [qwen-vl-text] coord API: raw_items=44, valid_items=44, elapsed=12.4s
2026-08-10 11:47:16,149 INFO     29 [qwen-vl-text] coord item[0]: text=10:15, bbox=[233, 13, 291, 27]
2026-08-10 11:47:16,149 INFO     29 [qwen-vl-text] coord item[1]: text=淘, bbox=[321, 13, 343, 27]
2026-08-10 11:47:16,149 INFO     29 [qwen-vl-text] coord item[2]: text=交易成功, bbox=[435, 57, 561, 80]
2026-08-10 11:47:16,149 INFO     29 [qwen-vl-text] coord item[3]: text=医药仁康堂医药专营店>, bbox=[224, 137, 466, 153]
2026-08-10 11:47:16,149 INFO     29 [qwen-vl-text] coord item[4]: text=【信必可】布地奈德福莫特罗[, bbox=[382, 177, 666, 193]
2026-08-10 11:47:16,149 INFO     29 [qwen-vl-text] coord item[5]: text=¥213, bbox=[718, 177, 770, 194]
2026-08-10 11:47:16,150 INFO     29 [qwen-vl-text] coord item[6]: text=放心买药, bbox=[304, 196, 340, 203]
2026-08-10 11:47:16,150 INFO     29 [qwen-vl-text] coord item[7]: text=正品保障, bbox=[303, 207, 341, 214]
2026-08-10 11:47:16,150 INFO     29 [qwen-vl-text] coord item[8]: text=1盒装, bbox=[370, 204, 423, 219]
2026-08-10 11:47:16,150 INFO     29 [qwen-vl-text] coord item[9]: text=不支持7天无理由 假一赔四>, bbox=[370, 230, 616, 245]
2026-08-10 11:47:16,150 INFO     29 [qwen-vl-text] coord item[10]: text=x1, bbox=[748, 231, 770, 244]
2026-08-10 11:47:16,150 INFO     29 [qwen-vl-text] coord item[11]: text=专业药师在线服务, bbox=[264, 239, 314, 245]
2026-08-10 11:47:16,150 INFO     29 [qwen-vl-text] coord item[12]: text=上天猫放心买药, bbox=[260, 247, 318, 254]
2026-08-10 11:47:16,150 INFO     29 [qwen-vl-text] coord item[13]: text=用药小贴士 1.哮喘。2.慢性阻塞性肺疾病(慢阻肺;..., bbox=[237, 275, 709, 291]
2026-08-10 11:47:16,150 INFO     29 [qwen-vl-text] coord item[14]: text=申请售后, bbox=[667, 317, 749, 333]
2026-08-10 11:47:16,150 INFO     29 [qwen-vl-text] coord item[15]: text=商品总价, bbox=[225, 367, 321, 384]
2026-08-10 11:47:16,150 INFO     29 [qwen-vl-text] coord item[16]: text=¥213, bbox=[715, 369, 770, 386]
2026-08-10 11:47:16,150 INFO     29 [qwen-vl-text] coord item[17]: text=运费(含服务费), bbox=[225, 411, 365, 427]
2026-08-10 11:47:16,150 INFO     29 [qwen-vl-text] coord item[18]: text=¥8, bbox=[738, 411, 770, 428]
2026-08-10 11:47:16,150 INFO     29 [qwen-vl-text] coord item[19]: text=应付款, bbox=[225, 457, 298, 474]
2026-08-10 11:47:16,151 INFO     29 [qwen-vl-text] coord item[20]: text=¥221^, bbox=[681, 455, 770, 475]
2026-08-10 11:47:16,151 INFO     29 [qwen-vl-text] coord item[21]: text=订单信息 2026-01-20, bbox=[225, 520, 442, 537]
2026-08-10 11:47:16,151 INFO     29 [qwen-vl-text] coord item[22]: text=收起^, bbox=[706, 520, 770, 536]
2026-08-10 11:47:16,151 INFO     29 [qwen-vl-text] coord item[23]: text=订单编号, bbox=[225, 558, 309, 574]
2026-08-10 11:47:16,151 INFO     29 [qwen-vl-text] coord item[24]: text=4501919772001020746, bbox=[547, 558, 770, 574]
2026-08-10 11:47:16,151 INFO     29 [qwen-vl-text] coord item[25]: text=交易快照, bbox=[225, 595, 309, 611]
2026-08-10 11:47:16,151 INFO     29 [qwen-vl-text] coord item[26]: text=发生交易争议时，可作为判断依据>, bbox=[436, 595, 763, 611]
2026-08-10 11:47:16,151 INFO     29 [qwen-vl-text] coord item[27]: text=成交时间, bbox=[225, 632, 309, 648]
2026-08-10 11:47:16,151 INFO     29 [qwen-vl-text] coord item[28]: text=2026-01-26 22:25:02, bbox=[569, 632, 770, 648]
2026-08-10 11:47:16,151 INFO     29 [qwen-vl-text] coord item[29]: text=发货时间, bbox=[225, 669, 309, 685]
2026-08-10 11:47:16,151 INFO     29 [qwen-vl-text] coord item[30]: text=2026-01-21 12:24:52, bbox=[569, 669, 770, 685]
2026-08-10 11:47:16,151 INFO     29 [qwen-vl-text] coord item[31]: text=付款时间, bbox=[225, 705, 309, 721]
2026-08-10 11:47:16,151 INFO     29 [qwen-vl-text] coord item[32]: text=2026-01-20 19:25:06, bbox=[569, 705, 770, 721]
2026-08-10 11:47:16,151 INFO     29 [qwen-vl-text] coord item[33]: text=创建时间, bbox=[225, 741, 309, 757]
2026-08-10 11:47:16,151 INFO     29 [qwen-vl-text] coord item[34]: text=2026-01-20 19:24:30, bbox=[569, 741, 770, 757]
2026-08-10 11:47:16,152 INFO     29 [qwen-vl-text] coord item[35]: text=支付宝交易号, bbox=[225, 777, 351, 793]
2026-08-10 11:47:16,152 INFO     29 [qwen-vl-text] coord item[36]: text=2026012022001134951454085519, bbox=[442, 777, 770, 793]
2026-08-10 11:47:16,152 INFO     29 [qwen-vl-text] coord item[37]: text=天猫积分, bbox=[225, 814, 309, 830]
2026-08-10 11:47:16,152 INFO     29 [qwen-vl-text] coord item[38]: text=获得106点积分>, bbox=[607, 814, 763, 830]
2026-08-10 11:47:16,152 INFO     29 [qwen-vl-text] coord item[39]: text=客服, bbox=[222, 876, 255, 889]
2026-08-10 11:47:16,152 INFO     29 [qwen-vl-text] coord item[40]: text=更多, bbox=[275, 876, 306, 889]
2026-08-10 11:47:16,152 INFO     29 [qwen-vl-text] coord item[41]: text=查看处方, bbox=[369, 864, 452, 880]
2026-08-10 11:47:16,152 INFO     29 [qwen-vl-text] coord item[42]: text=查看物流, bbox=[518, 864, 601, 880]
2026-08-10 11:47:16,152 INFO     29 [qwen-vl-text] coord item[43]: text=评价, bbox=[688, 865, 728, 880]
2026-08-10 11:47:16,152 INFO     29 [qwen-vl-text] page=18 — 44/44 coords, api_time=12.4s
2026-08-10 11:47:16,153 INFO     29 [qwen-vl-text] new_positions (44):
[[18, 138.635, 173.14499999999998, 10.946, 22.733999999999998], [18, 190.995, 204.08499999999998, 10.946, 22.733999999999998], [18, 258.825, 333.79499999999996, 47.994, 67.36], [18, 133.28, 277.27, 115.354, 128.826], [18, 227.29, 396.27, 149.034, 162.506], [18, 427.21, 458.15, 149.034, 163.34799999999998], [18, 180.88, 202.29999999999998, 165.03199999999998, 170.926], [18, 180.285, 202.89499999999998, 174.29399999999998, 180.188], [18, 220.14999999999998, 251.685, 171.768, 184.398], [18, 220.14999999999998, 366.52, 193.66, 206.29], [18, 445.06, 458.15, 194.50199999999998, 205.44799999999998], [18, 157.07999999999998, 186.82999999999998, 201.238, 206.29], [18, 154.7, 189.20999999999998, 207.974, 213.868], [18, 141.015, 421.85499999999996, 231.54999999999998, 245.022], [18, 396.865, 445.655, 266.914, 280.38599999999997], [18, 133.875, 190.995, 309.014, 323.328], [18, 425.42499999999995, 458.15, 310.698, 325.012], [18, 133.875, 217.17499999999998, 346.062, 359.534], [18, 439.10999999999996, 458.15, 346.062, 360.376], [18, 133.875, 177.31, 384.794, 399.108], [18, 405.195, 458.15, 383.11, 399.95], [18, 133.875, 262.99, 437.84, 452.154], [18, 420.07, 458.15, 437.84, 451.312], [18, 133.875, 183.855, 469.83599999999996, 483.308], [18, 325.465, 458.15, 469.83599999999996, 483.308], [18, 133.875, 183.855, 500.99, 514.462], [18, 259.42, 453.98499999999996, 500.99, 514.462], [18, 133.875, 183.855, 532.144, 545.616], [18, 338.555, 458.15, 532.144, 545.616], [18, 133.875, 183.855, 563.298, 576.77], [18, 338.555, 458.15, 563.298, 576.77], [18, 133.875, 183.855, 593.61, 607.082], [18, 338.555, 458.15, 593.61, 607.082], [18, 133.875, 183.855, 623.922, 637.394], [18, 338.555, 458.15, 623.922, 637.394], [18, 133.875, 208.845, 654.2339999999999, 667.706], [18, 262.99, 458.15, 654.2339999999999, 667.706], [18, 133.875, 183.855, 685.3879999999999, 698.86], [18, 361.16499999999996, 453.98499999999996, 685.3879999999999, 698.86], [18, 132.09, 151.725, 737.592, 748.538], [18, 163.625, 182.07, 737.592, 748.538], [18, 219.55499999999998, 268.94, 727.4879999999999, 740.9599999999999], [18, 308.21, 357.59499999999997, 727.4879999999999, 740.9599999999999], [18, 409.35999999999996, 433.15999999999997, 728.3299999999999, 740.9599999999999]]
2026-08-10 11:47:16,153 INFO     29 [qwen-vl-text] ═══ DONE ═══ 44 positions, pages=1, time=14.6s
2026-08-10 11:47:16,153 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:47:16,164 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:47:16,164 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-10 11:47:16,165 INFO     29 [qwen-vl-text] positions(33): [[19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:47:16,165 INFO     29 [qwen-vl-text] page grouping: [19], lines per page: [33]
2026-08-10 11:47:16,412 INFO     29 [qwen-vl-text] page=19, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 11:47:16,414 INFO     29 [qwen-vl-text] LLM extraction start, text_len=284
2026-08-10 11:47:16,414 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:47:16,414 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 640, \"bbox_end\": 672, \"encounter_dates\": [\"2026-02-02\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "电子发票(普通发票)\n发票号码：26322000000914042776\n开票日期：2026年02月02日\n江苏省税务局\n购买方信息\n名称：\n统一社会信用代码/纳税人识别号：\n销售方信息\n名称：阜宁仁康堂大药房有限公司\n统一社会信用代码/纳税人识别号：91320923MAK1XP619R\n项目名称\n规格型号\n单位\n数量\n单价\n金额\n税率/征收率\n税额\n*生物化学药品*其他生物\n1\n218.811881188119\n218.81\n1%\n2.19\n化学药品\n合计\n￥218.81\n￥2.19\n价税合计（大写）\n贰佰贰拾壹圆整\n(小写)￥221.00\n备注\n开票人：杨雪",
    "role": "user"
  }
]
2026-08-10 11:47:16,417 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:47:16.416+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 24, "failed": 0, "current": {"38277e3a94b011f1bd9827cf206dfa2d": {"id": "38277e3a94b011f1bd9827cf206dfa2d", "doc_id": "370244ae94b011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479740, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786362000249, "task_type": "dataflow", "root_trace_id": "96cd8dab6bb7455194a762d3f16e1d52", "root_traceparent": "00-96cd8dab6bb7455194a762d3f16e1d52-1e133766dfd81337-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:47:18,560 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:47:18,560 INFO     29 [qwen-vl-text] LLM output (len=432):
{
  "encounter_date": "2026-02-02",
  "pharmacy": "阜宁仁康堂大药房有限公司",
  "medications": [
    {
      "name": "*生物化学药品*其他生物化学药品",
      "specification": null,
      "dosage": null,
      "quantity": 1,
      "unit_price": 218.811881188119,
      "total_price": 218.81,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 221.00,
  "payment_method": null
}
2026-08-10 11:47:18,560 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-02]
2026-08-10 11:47:18,562 INFO     29 [qwen-vl-text] coord API call start, page=19, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=918020, prompt_len=996
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["电子发票(普通发票)", "发票号码：26322000000914042776", "开票日期：2026年02月02日", "江苏省税务局", "购买方信息", "名称：", "统一社会信用代码/纳税人识别号：", "销售方信息", "名称：阜宁仁康堂大药房有限公司", "统一社会信用代码/纳税人识别号：91320923MAK1XP619R", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*生物化学药品*其他生物", "1", "218.811881188119", "218.81", "1%", "2.19", "化学药品", "合计", "￥218.81", "￥2.19", "价税合计（大写）", "贰佰贰拾壹圆整", "(小写)￥221.00", "备注", "开票人：杨雪"]

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
2026-08-10 11:47:34,821 INFO     29 [qwen-vl-text] coord API raw response (len=2747):
[
	{"text": "电子发票(普通发票)", "bbox": [328, 54, 640, 98]},
	{"text": "发票号码：26322000000914042776", "bbox": [733, 74, 955, 94]},
	{"text": "开票日期：2026年02月02日", "bbox": [732, 114, 908, 134]},
	{"text": "江苏省税务局", "bbox": [461, 147, 535, 168]},
	{"text": "购买方信息", "bbox": [33, 218, 46, 330], "bbox_2d": [33, 218, 46, 330]},
	{"text": "名称：", "bbox": [61, 224, 100, 244], "bbox_2d": [61, 224, 209, 260]},
	{"text": "统一社会信用代码/纳税人识别号：", "bbox": [60, 295, 257, 314], "bbox_2d": [60, 295, 257, 314]},
	{"text": "销售方信息", "bbox": [507, 218, 519, 330], "bbox_2d": [507, 218, 519, 330]},
	{"text": "名称：阜宁仁康堂大药房有限公司", "bbox": [533, 224, 747, 244], "bbox_2d": [533, 224, 747, 244]},
	{"text": "统一社会信用代码/纳税人识别号：91320923MAK1XP619R", "bbox": [532, 295, 946, 314], "bbox_2d": [532, 295, 946, 314]},
	{"text": "项目名称", "bbox": [80, 355, 140, 373], "bbox_2d": [80, 355, 140, 373]},
	{"text": "规格型号", "bbox": [202, 355, 262, 373], "bbox_2d": [202, 355, 262, 373]},
	{"text": "单位", "bbox": [321, 355, 365, 373], "bbox_2d": [321, 355, 365, 373]},
	{"text": "数量", "bbox": [443, 355, 487, 373], "bbox_2d": [443, 355, 487, 373]},
	{"text": "单价", "bbox": [561, 355, 604, 373], "bbox_2d": [561, 355, 604, 373]},
	{"text": "金额", "bbox": [681, 355, 724, 373], "bbox_2d": [681, 355, 724, 373]},
	{"text": "税率/征收率", "bbox": [745, 355, 827, 373], "bbox_2d": [745, 355, 827, 373]},
	{"text": "税额", "bbox": [919, 355, 963, 373], "bbox_2d": [919, 355, 963, 373]},
	{"text": "*生物化学药品*其他生物", "bbox": [26, 376, 189, 396], "bbox_2d": [26, 376, 189, 396]},
	{"text": "1", "bbox": [480, 380, 488, 396], "bbox_2d": [480, 380, 488, 396]},
	{"text": "218.811881188119", "bbox": [498, 380, 604, 396], "bbox_2d": [498, 380, 604, 396]},
	{"text": "218.81", "bbox": [680, 380, 723, 396], "bbox_2d": [680, 380, 723, 396]},
	{"text": "1%", "bbox": [781, 380, 797, 396], "bbox_2d": [781, 380, 797, 396]},
	{"text": "2.19", "bbox": [940, 380, 970, 396], "bbox_2d": [940, 380, 970, 396]},
	{"text": "化学药品", "bbox": [26, 405, 86, 425], "bbox_2d": [26, 405, 86, 425]},
	{"text": "合计", "bbox": [102, 615, 115, 632], "bbox_2d": [102, 615, 115, 632]},
	{"text": "计", "bbox": [176, 615, 190, 632], "bbox_2d": [176, 615, 190, 632]},
	{"text": "￥218.81", "bbox": [672, 612, 725, 630], "bbox_2d": [672, 612, 725, 630]},
	{"text": "￥2.19", "bbox": [930, 612, 970, 630], "bbox_2d": [930, 612, 970, 630]},
	{"text": "价税合计（大写）", "bbox": [85, 657, 195, 676], "bbox_2d": [85, 657, 195, 676]},
	{"text": "贰佰贰拾壹圆整", "bbox": [300, 651, 406, 673], "bbox_2d": [300, 651, 406, 673]},
	{"text": "(小写)￥221.00", "bbox": [689, 653, 801, 674], "bbox_2d": [689, 653, 801, 674]},
	{"text": "备注", "bbox": [33, 727, 46, 785], "bbox_2d": [33, 727, 46, 785]},
	{"text": "开票人：杨雪", "bbox": [97, 863, 184, 883], "bbox_2d": [97, 863, 184, 883]}
]
2026-08-10 11:47:34,822 INFO     29 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=16.3s
2026-08-10 11:47:34,822 INFO     29 [qwen-vl-text] coord item[0]: text=电子发票(普通发票), bbox=[328, 54, 640, 98]
2026-08-10 11:47:34,822 INFO     29 [qwen-vl-text] coord item[1]: text=发票号码：26322000000914042776, bbox=[733, 74, 955, 94]
2026-08-10 11:47:34,822 INFO     29 [qwen-vl-text] coord item[2]: text=开票日期：2026年02月02日, bbox=[732, 114, 908, 134]
2026-08-10 11:47:34,822 INFO     29 [qwen-vl-text] coord item[3]: text=江苏省税务局, bbox=[461, 147, 535, 168]
2026-08-10 11:47:34,822 INFO     29 [qwen-vl-text] coord item[4]: text=购买方信息, bbox=[33, 218, 46, 330]
2026-08-10 11:47:34,822 INFO     29 [qwen-vl-text] coord item[5]: text=名称：, bbox=[61, 224, 100, 244]
2026-08-10 11:47:34,822 INFO     29 [qwen-vl-text] coord item[6]: text=统一社会信用代码/纳税人识别号：, bbox=[60, 295, 257, 314]
2026-08-10 11:47:34,822 INFO     29 [qwen-vl-text] coord item[7]: text=销售方信息, bbox=[507, 218, 519, 330]
2026-08-10 11:47:34,822 INFO     29 [qwen-vl-text] coord item[8]: text=名称：阜宁仁康堂大药房有限公司, bbox=[533, 224, 747, 244]
2026-08-10 11:47:34,823 INFO     29 [qwen-vl-text] coord item[9]: text=统一社会信用代码/纳税人识别号：91320923MAK1XP619R, bbox=[532, 295, 946, 314]
2026-08-10 11:47:34,823 INFO     29 [qwen-vl-text] coord item[10]: text=项目名称, bbox=[80, 355, 140, 373]
2026-08-10 11:47:34,823 INFO     29 [qwen-vl-text] coord item[11]: text=规格型号, bbox=[202, 355, 262, 373]
2026-08-10 11:47:34,823 INFO     29 [qwen-vl-text] coord item[12]: text=单位, bbox=[321, 355, 365, 373]
2026-08-10 11:47:34,823 INFO     29 [qwen-vl-text] coord item[13]: text=数量, bbox=[443, 355, 487, 373]
2026-08-10 11:47:34,823 INFO     29 [qwen-vl-text] coord item[14]: text=单价, bbox=[561, 355, 604, 373]
2026-08-10 11:47:34,823 INFO     29 [qwen-vl-text] coord item[15]: text=金额, bbox=[681, 355, 724, 373]
2026-08-10 11:47:34,823 INFO     29 [qwen-vl-text] coord item[16]: text=税率/征收率, bbox=[745, 355, 827, 373]
2026-08-10 11:47:34,823 INFO     29 [qwen-vl-text] coord item[17]: text=税额, bbox=[919, 355, 963, 373]
2026-08-10 11:47:34,823 INFO     29 [qwen-vl-text] coord item[18]: text=*生物化学药品*其他生物, bbox=[26, 376, 189, 396]
2026-08-10 11:47:34,823 INFO     29 [qwen-vl-text] coord item[19]: text=1, bbox=[480, 380, 488, 396]
2026-08-10 11:47:34,823 INFO     29 [qwen-vl-text] coord item[20]: text=218.811881188119, bbox=[498, 380, 604, 396]
2026-08-10 11:47:34,823 INFO     29 [qwen-vl-text] coord item[21]: text=218.81, bbox=[680, 380, 723, 396]
2026-08-10 11:47:34,823 INFO     29 [qwen-vl-text] coord item[22]: text=1%, bbox=[781, 380, 797, 396]
2026-08-10 11:47:34,823 INFO     29 [qwen-vl-text] coord item[23]: text=2.19, bbox=[940, 380, 970, 396]
2026-08-10 11:47:34,823 INFO     29 [qwen-vl-text] coord item[24]: text=化学药品, bbox=[26, 405, 86, 425]
2026-08-10 11:47:34,823 INFO     29 [qwen-vl-text] coord item[25]: text=合计, bbox=[102, 615, 115, 632]
2026-08-10 11:47:34,824 INFO     29 [qwen-vl-text] coord item[26]: text=计, bbox=[176, 615, 190, 632]
2026-08-10 11:47:34,824 INFO     29 [qwen-vl-text] coord item[27]: text=￥218.81, bbox=[672, 612, 725, 630]
2026-08-10 11:47:34,824 INFO     29 [qwen-vl-text] coord item[28]: text=￥2.19, bbox=[930, 612, 970, 630]
2026-08-10 11:47:34,824 INFO     29 [qwen-vl-text] coord item[29]: text=价税合计（大写）, bbox=[85, 657, 195, 676]
2026-08-10 11:47:34,824 INFO     29 [qwen-vl-text] coord item[30]: text=贰佰贰拾壹圆整, bbox=[300, 651, 406, 673]
2026-08-10 11:47:34,824 INFO     29 [qwen-vl-text] coord item[31]: text=(小写)￥221.00, bbox=[689, 653, 801, 674]
2026-08-10 11:47:34,824 INFO     29 [qwen-vl-text] coord item[32]: text=备注, bbox=[33, 727, 46, 785]
2026-08-10 11:47:34,824 INFO     29 [qwen-vl-text] coord item[33]: text=开票人：杨雪, bbox=[97, 863, 184, 883]
2026-08-10 11:47:34,825 INFO     29 [qwen-vl-text] page=19 — 33/33 coords, api_time=16.3s
2026-08-10 11:47:34,825 INFO     29 [qwen-vl-text] new_positions (33):
[[19, 276.176, 538.88, 32.129999999999995, 58.309999999999995], [19, 617.1859999999999, 804.11, 44.03, 55.93], [19, 616.3439999999999, 764.536, 67.83, 79.72999999999999], [19, 388.162, 450.46999999999997, 87.46499999999999, 99.96], [19, 27.785999999999998, 38.732, 129.71, 196.35], [19, 51.361999999999995, 84.2, 133.28, 145.18], [19, 50.519999999999996, 216.394, 175.525, 186.82999999999998], [19, 426.894, 436.998, 129.71, 196.35], [19, 448.786, 628.9739999999999, 133.28, 145.18], [19, 447.94399999999996, 796.5319999999999, 175.525, 186.82999999999998], [19, 67.36, 117.88, 211.225, 221.935], [19, 170.084, 220.60399999999998, 211.225, 221.935], [19, 270.282, 307.33, 211.225, 221.935], [19, 373.006, 410.054, 211.225, 221.935], [19, 472.36199999999997, 508.568, 211.225, 221.935], [19, 573.4019999999999, 609.608, 211.225, 221.935], [19, 627.29, 696.334, 211.225, 221.935], [19, 773.798, 810.846, 211.225, 221.935], [19, 21.892, 159.138, 223.72, 235.61999999999998], [19, 404.15999999999997, 410.89599999999996, 226.1, 235.61999999999998], [19, 419.316, 508.568, 226.1, 235.61999999999998], [19, 572.56, 608.766, 226.1, 235.61999999999998], [19, 657.602, 671.074, 226.1, 235.61999999999998], [19, 791.48, 816.74, 226.1, 235.61999999999998], [19, 21.892, 72.41199999999999, 240.975, 252.875], [19, 85.884, 96.83, 365.925, 376.03999999999996], [19, 148.192, 159.98, 365.925, 376.03999999999996], [19, 565.824, 610.4499999999999, 364.14, 374.84999999999997], [19, 783.06, 816.74, 364.14, 374.84999999999997], [19, 71.57, 164.19, 390.91499999999996, 402.21999999999997], [19, 252.6, 341.852, 387.34499999999997, 400.435], [19, 580.138, 674.442, 388.53499999999997, 401.03], [19, 27.785999999999998, 38.732, 432.565, 467.075]]
2026-08-10 11:47:34,825 INFO     29 [qwen-vl-text] ═══ DONE ═══ 33 positions, pages=1, time=18.7s
2026-08-10 11:47:34,839 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 11:47:34,839 INFO     29 [Trace] task=38277e3a | doc=LZQ 64 哮喘 深圳二院.pdf | Extractor:Medication | outputs={"chunks": "5 items, types={'MedicationRecord': 5}", "html": "", "json": "675 items", "markdown": "", "text": "", "name": "LZQ 64 哮喘 深圳二院.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Medication\": 5}"}
2026-08-10 11:47:34,839 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 11:47:34,848 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:47:34,848 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:47:35,787 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:47:35,794 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 11:47:35,795 INFO     29 [Trace] task=38277e3a | doc=LZQ 64 哮喘 深圳二院.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "675 items", "markdown": "", "text": "", "name": "LZQ 64 哮喘 深圳二院.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Medication\": 5}"}
2026-08-10 11:47:35,795 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 11:47:35,800 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:47:35,800 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:47:36,261 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:47:36,273 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 11:47:36,273 INFO     29 [Trace] task=38277e3a | doc=LZQ 64 哮喘 深圳二院.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "675 items", "markdown": "", "text": "", "name": "LZQ 64 哮喘 深圳二院.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Medication\": 5}"}
2026-08-10 11:47:36,273 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 11:47:36,283 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:47:36,283 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:47:36,775 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:47:36,783 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 11:47:36,783 INFO     29 [Trace] task=38277e3a | doc=LZQ 64 哮喘 深圳二院.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "675 items", "markdown": "", "text": "", "name": "LZQ 64 哮喘 深圳二院.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Medication\": 5}"}
2026-08-10 11:47:36,783 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 11:47:36,790 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:47:36,790 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:47:37,905 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:47:37,915 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 11:47:37,915 INFO     29 [Trace] task=38277e3a | doc=LZQ 64 哮喘 深圳二院.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "675 items", "markdown": "", "text": "", "name": "LZQ 64 哮喘 深圳二院.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Medication\": 5}"}
2026-08-10 11:47:37,915 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 11:47:37,927 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:47:37,927 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:47:38,390 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:47:38,396 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 11:47:38,396 INFO     29 [Trace] task=38277e3a | doc=LZQ 64 哮喘 深圳二院.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "675 items", "markdown": "", "text": "", "name": "LZQ 64 哮喘 深圳二院.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Medication\": 5}"}
2026-08-10 11:47:38,396 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 11:47:38,398 INFO     29 [ChunkMerger] Merged 11 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 6, 'Extractor:Medication': 5, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 7 noise chunks)
2026-08-10 11:47:38,410 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 11:47:38,410 INFO     29 [Trace] task=38277e3a | doc=LZQ 64 哮喘 深圳二院.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "11 items, types={'OutpatientRecord': 6, 'MedicationRecord': 5}", "name": "LZQ 64 哮喘 深圳二院.pdf"}
2026-08-10 11:47:38,410 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 11:47:38,630 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786362002261, 'update_date': datetime.datetime(2026, 8, 10, 11, 40, 2), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 936198, 'status': '1'}
2026-08-10 11:47:38,858 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=门诊病历
科室:呼吸与危重症医学科
门
联系人
性别:女
年龄:62岁
婚姻状况:其他
2024-01-10 10:27 初诊记录
主诉:发作性喘息12年余
现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年
余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现
气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行
听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并
规律使用信必可320ug bid后症状缓解。近日活动后气促再发,否认喘
鸣音。无发热、胸痛。
既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。
既往病史:
1.2022.12.10肝囊肿,持续;
2.2023.10.31鼻窦炎,持续;
3.2023.10.31双肺良性小结节,持续;
4.2023.11.03-2023.12.13,肺肺部感染;
一年内支气管哮喘急性发作病史:
12023.11.03-2023.11.08,支气管哮喘急性发作,8mg、4mg甲泼尼龙qd
各服用3天;
22023.12.13-2023.12.15,支气管哮喘急性发作,4mg甲泼尼龙片qd,服用
3天。
一年内合并用药:
1.左氧氟沙星片,2023.11.03-2023.12.01,0.5g,qd,po,用于治疗肺部感染
2.甲泼尼龙片,2023.11.03-2023.11.05,8mg,qd,po,用于治疗支气管哮喘急
性发作。
3.甲泼尼龙片,2023.11.06-2023.11.08,4mg,qd,po,用于治疗支气管哮喘急
性发作。
4.孟鲁司特钠片,2023.11.03-2023.11.12,10mg,qn,po,用于治疗支气管哮喘
急性发作。
第1页
门诊病历
科室:呼吸与危重症医学科
姓名
性别:女
年龄:62岁
婚姻状况:其他
联系方式
2024-01-10 10:27 初诊记录
5.桉柠蒎肠溶软胶囊,2023.11.03-2023.11.15,0.3g,tid,po,用于治疗肺部感
染。
7.甲泼尼龙片,2023.12.13-2023.12.15,4mg,qd,po,用于治疗支气管哮喘急
性发作。
8.布地奈德福莫特罗粉吸入剂,2022.11.27开始,持续使用,
320ug,bid,经口腔吸入,用于控制哮喘。
过敏史:否认食物、药物过敏史。
体格检查 收缩压（mmHg）:107;舒张压（mmHg）:75
其他体格检查:身高:153cm,体重:48.5kg,
09:50进行生命体征测量:体温:36.4℃,血压:107/75mmHg,呼吸:19
次/分,脉搏:78次/分;
查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见
皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅
大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。
耳廓正常无畸形,外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无
鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿
大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中
肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动
正常,双肺呼吸音粗,未闻及干湿罗音。心律齐。双下肢无水肿。心率
78次/分,心音正常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛
反跳痛,无液波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触
及,肾脏未触及,Murphy征阴性,移动性浊音阴性,肠鸣音正常。外生殖
器未查、肛门直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无
异常,其他无异常。
第2页
CS 扫描全能王
3亿人都在用的扫描App
科室:呼吸与危重症医学科
姓名:
性别:女
门诊
联系方式
596
年龄:62岁
婚姻状况:其他
2024-01-10 10:27 初诊记录
检验检查:阅片见双肺轻度支气管扩张,未见明显急性炎症病灶,余肺基本同前
(正式报告为准)
初步诊断:1.鼻窦炎;2.支气管哮喘;
处理:药品:
(省采3)硫酸沙丁胺醇吸入气雾剂200揿(100μg/揿)/瓶(1【瓶】) sig:
(200【揿】)吸入pm(需要时);
检查:心脏电生理:心电图(十二导联心电图);CT检查:副鼻窦平扫;
使用螺旋扫描加收;普放:DR胸部正侧位片*(2);呼吸专科检查:支气管
舒张试验、流速容量曲线;
检验:凝血四项、肾功能六项+肝功能八项+血脂六项*+电解质六项+空
腹血糖(门诊使用)+肝酶学补充7项+心肌损伤六项、血常规5分类、尿
常规加化学分析、感染八项
治疗:静脉采血
根据患者病情,认为患者基本符合“评价SHR-1905注射液在重度未
控制哮喘患者中的有效性及安全性-多中心、随机、双盲、安慰剂对照
平行设计II期临床研究(SHR-1905-201)”的筛选要求,2024.01.10 09:15
生向患者__及其家属详细介绍该试验目的、试验设计、受试
者风险及受益、受试者义务及研究者义务等。根据方案(版本号:2.0,
版本日期:2022年8月31日)要求,筛选期所有受试者均进行吸入支气
管扩张剂前后肺功能检查,若受试者无法提供筛选前一年内气道可逆
性检测报告(吸入沙丁胺醇后FEV1增加≥12%且FEV1绝对值增加≥
200mL),则筛选期肺功能检查需要满足吸入沙丁胺醇后FEV1增加≥
12%且FEV1绝对值增加≥200mL。符合要求后才可以入组,受试者表
示同意。患者.__及其家属表示已充分了解以上告知内容,同意参加
该临床试验,
医生与患者__于2024.01.10 09:47同时签署了知
情同意书(版本号:2.0,版本日期:2022年08月31日),一式两份,一份
第3页
门诊病历
科室:呼吸与危重症医学科
姓名:
性别:女
门诊
联系方式
年龄:62岁
婚姻状况:其他
2024-01-10 10:27 初诊记录
交给患者保存,一份保存在研究中心。签署知情同意书后患者进入筛选
流程,受试者筛选号为CN..
新增AE:
1.高尿酸血症,2024.01.10开始,轻度,持续,与研究药物肯定无关,对研
究药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。
2.高脂血症,2024.01.10开始,轻度,持续,与研究药物肯定无关,对研究
药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。
3.白细胞计数降低,2024.01.10开始,轻度,持续,与研究药物肯定无关
对研究药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。此项
指标与患者临床症状不符,考虑让其一周内复测。
规律使用吸入药物,用后漱口,定期复诊;避免接触可能过敏原;不用地
毯,不养动物
医师签
门诊病历专用
※提醒:复诊时,请携带本病历记录,谢谢!※
---
门诊病历
科室:呼吸与危重症医学科
姓名:
性别:女
门诊
联系方
年龄:62岁
婚姻状况:其他
2024-03-21 08:40 初诊记录
主诉:SHR-1905-201 试验复筛
现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年
余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现
气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行
听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并
规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可
320ug bid,近日活动后气促再发,否认喘鸣音。无发热、胸痛。
2024.01.10参加SHR-1905-201临床试验,因白细胞计数<3.0*10^9/L符
合排除标准第12条筛败,于2024.03.01血液科就诊,无特殊处理,
2024.03.06进行SHR-1905-201试验二次知情。受试者今日返院完成V3
访视。
既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。
既往病史:
1.2022.12.10肝囊肿,持续;
2.2023.10.31鼻窦炎,持续;
3.2023.10.31双肺良性小结节,持续;
4.2023.11.03-2023.12.13,肺肺部感染;
5.2024.03.01开始,白细胞数降低1级;
6.2024.01.10开始,高脂蛋白a血症,
过敏史:否认食物、药物过敏史。
体格检查收缩压(mmHg):113;舒张压(mmHg):76
其他体格检查:09:37进行生命体征测量:体温:36.5℃,血压:
113/76mmHg,呼吸:18次/分,脉搏:98次/分;
查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见
第1页
科室:呼吸与危重症医学科
姓名
性别:女
门诊
联系方
年龄:62岁
婚姻状况:其他
2024-03-21 08:40 初诊记录
皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅
大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。
耳廓正常无畸形,外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无
鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿
大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中
肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动
正常,双肺呼吸音粗,未闻及干湿罗音。心律齐。双下肢无水肿。心音正
常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛、反跳痛,无液
波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触及,肾脏未触
及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖器未查、肛门
直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无异常,其他无
异常。.
检验检查:无
初步诊断:支气管哮喘
处理:
CM 跟踪:
1、布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,
320ug,bid,经口腔吸入,用于控制哮喘。
处理:
1、2024.03.14-2024.03.21 家用峰流速仪使用 ePRO 系统填写依从性
7/7*100%=100%,嘱托患者按照自己实际情况及时填写日志,如有问题
随时沟通。
2、无新增 AE,CM,无临床试验安全性事件。
3、今日回收硫酸沙丁胺醇吸入气雾剂,发放新的硫酸沙丁胺醇吸入气
雾剂1盒,并嘱托受试者正确保存和使用。
4、绝经期女性,未做血、尿妊娠检查。
第2页
CS 扫描全能王
3亿人都在用的扫描App
科室:呼吸与危重症医学科
门诊
姓名
联系方式
性别:女
年龄:62岁
婚姻状况:其他
2024-03-21 08:40 初诊记录
5、受试者所有检查结果经再次核对入排,符合所有入选标准,不符合任
一排除标准,可随机入组,分配随机号:_,随机分层信息:中剂量
ICS,嗜酸性粒细胞计数<300/ul,未联合使用LAMA。
6、嘱托受试者2024.03.22来院行V4随访。
医师签
门诊病历专用章
※提醒:复诊时,请携带本病历记录,谢谢!※
---
科室:呼吸与危重症医学科
门诊
姓名
联系
性别:女
年龄:63岁
婚姻状况:其他
2024-12-12 09:40 初诊记录
主诉:SHR-1905-201 临床试验 V14
现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年
余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现
气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行
听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并
规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可
320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:
近日咳嗽咳痰,低烧两天,呼吸道感染。2024.12.02行V14随访
因患者发热延迟用药。今日回院用药,留院观察1h。
既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。
既往病史:
1.2022.12.10肝囊肿,持续;
2.2023.10.31鼻窦炎,持续;
3.2023.10.31双肺良性小结节,持续;
4.2023.11.03-2023.12.13,肺肺部感染;
5.2024.03.01开始,白细胞数降低1级,持续;
6.2024.01.10开始,高脂血症,持续;
7.十余年前,慢性浅表胃炎,持续中。
过敏史:否认食物、药物过敏史。
体格检查收缩压(mmHg):-;舒张压(mmHg):-
其他体格检查:未行
检验检查:无
初步诊断:支气管哮喘
处理:检查:心脏电生理:心电图(十二导联心电图);
检验:急诊血常规(五分类)+急诊超敏C反应蛋白、急诊肝功能五项
治疗:静脉采血
第1页
科室:呼吸与危重症医学科
性别:女
年龄:63岁
婚姻状况:其他
2024-12-12 09:40 初诊记录
无新增 AE,无新增 CM,无临床试验安全性事件。
呼吸道感染,2024.11.27-2024.12.11,中度,与试验药物关系为可能无关
对试验药物采取的措施为延迟用药,对 AE 采取的措施为药物治疗,肺
SAE,非 SIE,不因此退出临床试验。
跟踪 CM:
1.盐酸莫西沙片,2024.12.02-2024.12.11,持续中,0.4g/片,1片/次,
qd,po,用于治疗 AE 呼吸道感染。
2.桉柠蒎肠溶胶囊,2024.12.02-2024.12.11 持续中,0.3g/粒,1粒/次,
tid,po,用于治疗 AE 呼吸道感染。(化痰)
3.氯苯那敏片,2024.12.02-2024.12.11,持续中,4mg/片,1片/次,
qn,po,用于治疗 AE 呼吸道感染。
4.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po,用于治
疗病史慢性浅表胃炎。
5.复方氨酚烷胺胶囊,2024.11.27-2024.12.02,持续中,0.25g:0.1g,1粒
/次,bid,po,用于治疗 AE 呼吸道感染。
6.吸入沙丁胺醇气雾剂,2024.12.02-2024.12.02,400ug,吸入,once,用于支
气管扩张检查。
CM 跟踪:
1、布地奈德福莫特罗粉吸入剂,2022.11.27 开始,持续使用,
320ug,bid,经口腔吸入,用于控制哮喘。
2、硫酸沙丁胺醇气雾剂,2024.03.06 开始,持续中,100ug,pm,经口腔吸
入,控制哮喘急性发作。
第2页
门诊病历
科室:呼吸与危重症医学科
姓名:
性别:女
门诊号
联系方式
年龄:63岁
婚姻状况:其他
2024-12-12 09:40 初诊记录
处理:
患者于今日 12:21-12:28 完成临床试验药物的注射,药物编号为
Y6077Y4950 用药前完善必要检查后随机用药。
医师
门诊病历
※提醒:复诊时,请携带本病历记录,谢谢!※
---
门诊病历
科室:呼吸与危重症医学科
姓名
性别:女
门诊
联系方式
年龄:63岁
婚姻状况:其他
2025-07-31 17:13 初诊记录
主诉:SHR-1905V19随访
现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年
余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现
气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行
听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并
规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可
320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:
20036.。近日无咳嗽咳痰,无胸闷气喘,无发热,无支气管哮喘急性发作
今日回院行V19随访。
既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。
既往病史:
1.2022.12.10肝囊肿,持续;
2.2023.10.31鼻窦炎,持续;
3.2023.10.31双肺良性小结节,持续;
4.2023.11.03-2023.12.13,肺肺部感染;
5.2024.03.01开始,白细胞数降低1级,持续;
6.2024.01.10高脂血症,持续中
过敏史:否认食物、药物过敏史。
体格检查收缩压(mmHg):103;舒张压(mmHg):64
其他体格检查:进行生命体征测量:体温:36.4℃,血压:
103/64mmHg,呼吸:18次/分,脉搏:76次/分;
查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见
皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅
大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。
耳廓正常无畸形外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无
鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿
第1页
门诊病历
科室:呼吸与危重症医学科
性别:女
门诊
联系方式:
年龄:63岁
婚姻状况:其他
2025-07-31 17:13 初诊记录
大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中
肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动
正常,左肺呼吸音清,未闻及粗干啰音。心律齐。双下肢无水肿。心音正
常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛、反跳痛,无液
波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触及,肾脏未触
及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖器未查、肛门
直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无异常,其他无
异常。
检验检查:已完善试验相关检验检查
初步诊断:支气管哮喘
处理:尿常规检查尿隐血,建议定期检查,必要时肾内科就诊。
无临床试验安全性事,无新增 AE。
新增合并用药:硫酸沙丁胺醇吸入气雾剂,2025.07.31-
2025.078.31,400ug,once,吸入,用于支气管扩张检查。
CM 跟踪:
1、布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,
320ug,bid,经口腔吸入,用于控制哮喘。
2、硫酸沙丁胺醇气雾剂,2024.03.06开始,持续中,100ug,pm,经口腔吸
入,控制哮喘急性发作。
3.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po.用于治
疗病史慢性浅表胃炎。
处理:
12025.05.13-2025.07.31 家用峰流速仪使用 ePRO 系统填写依从性大于
80%,今日已解绑 ePRO 系统。
2遵从临床试验方案完成 IgE,PK,ADA 采血,完成 ACQ-6,AQLQ 问卷填
写。
门诊病历
科室:呼吸与危重症医学科
姓名
性别:女
门诊
联系
年龄:63岁
婚姻状况:其他
2025-07-31 17:13 初诊记录
3.患者于今日肺功能检查前已停用基础吸入药物布地奈德福莫特罗粉
吸入剂大于12h,停药时间2025.07.30上午,具体时间不详。
4.患者已于今日完成随访期随访。
5.因患者未找到发放万托林,可能已经丢失故不予回收。
6.嘱患者规律使用吸入药物布地奈德福莫特罗粉吸入剂,药物自备。
医师
门诊病历专用章
※提醒:复诊时,请携带本病历记录,谢谢!※
“若有高血压糖尿病诊断,建议您到居住地附近社康中心,建立居民健康档案”
---
门诊
姓名：
门(急)诊初诊病历
性别：女
科室：呼吸内科门诊
年龄：63岁
就诊日期：2025-10-25 15:22
主诉：支气管哮喘复诊
现病史：患者支气管哮喘复诊，目前规律吸入布地奈德福莫特罗320ug 一次1吸，
一天2次。目前诉有咳嗽、咳痰，有气促感，无胸闷，无发热，无鼻塞、流涕，无咯
血、痰中带血，无头痛、头晕、视物旋转，无饮水呛咳，无咽痛、腹痛、腹胀等不
适。未予处理及就医。现患者为求进一步诊治，故至我院科门诊就医。
既往史：否认高血压、否认糖尿病、否认冠心病等慢性疾病病史，否认肝炎、结核
等传染病史，否认手术外伤输血史 过敏史：无食物、药物过敏史。。否认饮酒史。
个人史：已婚已育
家族史：否认家族病史。
体格检查：T：36.8℃ P：87次/分 R：21次/分 BP：108/73mmHg 指脉氧：
9%。神志清楚，精神尚可，呼吸平顺，口唇无发绀，咽部无充血，扁桃体无肿大，
双侧颈静脉无怒张，双肺呼吸音粗，双肺可闻及干啰音，双肺未闻及湿性啰音及胸膜
摩擦音。心率87次/分，律齐，各瓣膜未闻及明显病理性杂音。腹部平软，全腹部无
玉痛，反跳痛，肠鸣音正常。四肢运动自如，双下肢无水肿。
辅助检查：患者自行购买布地奈德福莫特罗320ug 一次1吸，一天2次。
初步诊断：
西医诊断：1.支气管哮喘(急性发作期)
处理意见：
醋酸泼尼松片（国基）(5mg*100片) 20.000mg
1次/天 口服
12.00片
硫酸沙丁胺醇吸入气雾剂（省3、国基）(200揿：
100μg) 200.000μg
1次/天 吸入
1.00瓶
建议：建议患者结果回报后请及时至我科门诊复诊，若出现病情变化或病情加重
无好转等，请及时至急诊科门诊复诊。
温馨提示：1.请妥善保管好病历及各种检查检验报告单。
2.复诊时，请携带本病历记录，谢谢！
第1页(共1页)
---
门诊号
姓名
科室:呼吸内科门诊
门(急)诊初诊病历
电话
性别:女
年龄:63岁
就诊日期:2025-11-24 15:01
主诉:支气管哮喘复诊
现病史:患者支气管哮喘复诊,目前规律吸入布地奈德福莫特罗320一次1吸,一天2次(患者自行网购药物),目前有咳嗽、咳痰,咳嗽时有气喘感。无胸闷,无发热,无鼻塞、流涕,无咯血、痰中带血,无头痛、头晕、视物旋转,无饮水呛咳,无咽痛、腹痛、腹胀等不适。未予处理及就医。现患者为求进一步诊治,故至我院科门诊就医。
既往史:否认高血压、否认糖尿病、否认冠心病等慢性疾病病史,否认肝炎、结核等传染病史,否认手术外伤输血史过敏史:无食物、药物过敏史。。否认饮酒史。
个人史:已婚已育
家族史:否认家族病史。
体格检查:T:36.8℃ P:87次/分 R:21次/分 BP:108/73mmHg 指脉氧:
9%。神志清楚,精神尚可,呼吸平顺,口唇无发绀,咽部无充血,扁桃体无肿大,
双侧颈静脉无怒张,双肺呼吸音粗,双肺可闻及散在干啰音,双肺未闻及湿性啰音及
胸膜摩擦音。心率87次/分,律齐,各瓣膜未闻及明显病理性杂音。腹部平软,全腹
邻无压痛,反跳痛,肠鸣音正常。四肢运动自如,双下肢无水肿。
辅助检查:
初步诊断:
西医诊断:1.支气管哮喘(急性发作期)
处理意见:自备布地奈德福莫特罗320一次1吸,一天2次
醋酸泼尼松片(国基)(5mg*100片)10.000mg
1次/天 口服 6.00片
建议:建议患者结果回报后请及时至我科门诊复诊,若出现病情变化或病情加重
无好转等,请及时至急诊科门诊复诊。
医生签名:
温馨提示:1.请妥善保管好病历及各种检查检验报告单。
2.复诊时,请携带本病历记录,谢谢!
第1页(共1页)
---
广东省医疗门诊收费票据（电子）
广东省
财政部监制
票据代码：44060125
票据号码：9148002082
校验码： 831306
开票日期：2025-10-25
项目名称
数量/单位
金额（元）
备注
项目名称
数量/单位
金额（元）
备注
西药费
1
13.05
以下是清单项
醋酸泼尼松片（国基）
12
0.50
硫酸沙丁胺醇吸入气雾剂（省3
1
12.55
、国基）
金额合计（大写）壹拾叁元零伍分
(小写)13.05
业务流水号：SF10390911
门诊
就诊日期：20251025
其他信息
医疗机构类型：综合医院
医保类型：现金(自费)
医保编号：
性别：女
医保统筹基金支付：0.00
其他支付：0.00
个人账户支付：0.00
个人现金支付：13.05
个人自付：0.00
个人自费：13.05
政策性减免：
收款单位（章）深圳市龙岗区第人民医院
复核人：掌上医院
收款人：掌上医院
说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。
单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dzpj.czt.gd.gov.cn/billcheck查验本省财政电子票据。
---
电子发票(普通发票)
发票号码：25447000001429974977
开票日期：2025年11月05日
广东省税务局
购买方信息
名称：
统一社会信用代码/纳税人识别号：
销售方信息
名称：阿里健康大药房医药连锁有限公司
统一社会信用代码/纳税人识别号：91440101681325547Y
项目名称
规格型号
单位
数量
单价
金额
税率/征收率
税额
*化学药品制剂*布地奈德
盒
3
176.70
530.09
13%
68.91
福莫特罗吸入粉雾剂
合计
￥530.09
￥68.91
价税合计（大写）
伍佰玖拾玖圆整
(小写)￥599.00
备注
开票人：董茜玲
CS 扫描全能王
---
广东省医疗门诊收费票据（电子）
广东省
财政部监制
票据代码：44
票据号码：9148286284
校验码：89a81f
交款人
开票日期：2025-11-24
项目名称
数量/单位
金额（元）
备注
项目名称
数量/单位
金额（元）
备注
西药费
1
0.25
以下是清单项
醋酸泼尼松片（国基）
6
0.25
金额合计（大写）贰角伍分
(小写)0.25
业务流水号：SF10481981
门
就诊日期：20251124
其他信息
医疗机构类型：综合医院
医保类型：现金(自费)
医保编号：
性别：女
医保统筹基金支付：0.00
其他支付：0.00
个人账户支付：0.00
个人现金支付：0.25
个人自付：0.00
个人自费：0.25
政策性减免：
收款单位（章）
人民医院
复核人：吴亮梅
收款人：吴亮梅
说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。
单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dipj.czt.gd.gov.cn/billcheck查验本省财政电子票据。
---
10:15
淘
交易成功
医药仁康堂医药专营店>
【信必可】布地奈德福莫特罗[
¥213
放心买药
正品保障
1盒装
不支持7天无理由 假一赔四>
x1
专业药师在线服务
上天猫放心买药
用药小贴士 1.哮喘。2.慢性阻塞性肺疾病(慢阻肺;...
申请售后
商品总价
¥213
运费(含服务费)
¥8
应付款
¥221^
订单信息 2026-01-20
收起^
订单编号
4501919772001020746
交易快照
发生交易争议时，可作为判断依据>
成交时间
2026-01-26 22:25:02
发货时间
2026-01-21 12:24:52
付款时间
2026-01-20 19:25:06
创建时间
2026-01-20 19:24:30
支付宝交易号
2026012022001134951454085519
天猫积分
获得106点积分>
客服
更多
查看处方
查看物流
评价
---
电子发票(普通发票)
发票号码：26322000000914042776
开票日期：2026年02月02日
江苏省税务局
购买方信息
名称：
统一社会信用代码/纳税人识别号：
销售方信息
名称：阜宁仁康堂大药房有限公司
统一社会信用代码/纳税人识别号：91320923MAK1XP619R
项目名称
规格型号
单位
数量
单价
金额
税率/征收率
税额
*生物化学药品*其他生物
1
218.811881188119
218.81
1%
2.19
化学药品
合计
￥218.81
￥2.19
价税合计（大写）
贰佰贰拾壹圆整
(小写)￥221.00
备注
开票人：杨雪
2026-08-10 11:47:39,634 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 11:47:39,634 INFO     29 [Trace] task=38277e3a | doc=LZQ 64 哮喘 深圳二院.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "11 items, types={'OutpatientRecord': 6, 'MedicationRecord': 5}", "name": "LZQ 64 哮喘 深圳二院.pdf", "embedding_token_consumption": 9173}
2026-08-10 11:47:39,634 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 11:47:39,966 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 11:47:39,967 INFO     29 [Trace] task=38277e3a | doc=LZQ 64 哮喘 深圳二院.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":11,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 11:47:39,973 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:47:39,973 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:47:39,973 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:47:39,973 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:47:39,973 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:47:39,973 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:47:39,973 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:47:39,973 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:47:39,973 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:47:39,974 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:47:39,974 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:47:39,980 INFO     29 set_progress(38277e3a94b011f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 11:47:39 [DOC Engine]:
Start to index...
2026-08-10 11:47:40,011 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.026s]
2026-08-10 11:47:40,016 INFO     29 set_progress(38277e3a94b011f1bd9827cf206dfa2d), progress: 0.8090909090909091, progress_msg: 
2026-08-10 11:47:40,042 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.018s]
2026-08-10 11:47:40,066 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.015s]
2026-08-10 11:47:40,078 INFO     29 set_progress(38277e3a94b011f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 11:47:40 Indexing done (0.10s). Task done (440.99s)
2026-08-10 11:47:40,082 INFO     29 [Done], chunks(11), token(9173), elapsed:440.99
2026-08-10 11:47:40,284 INFO     29 handle_task done for task {"id": "38277e3a94b011f1bd9827cf206dfa2d", "doc_id": "370244ae94b011f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479740, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786362000249, "task_type": "dataflow", "root_trace_id": "96cd8dab6bb7455194a762d3f16e1d52", "root_traceparent": "00-96cd8dab6bb7455194a762d3f16e1d52-1e133766dfd81337-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
