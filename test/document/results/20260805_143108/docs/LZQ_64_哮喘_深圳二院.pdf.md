# 基准结果：LZQ 64 哮喘 深圳二院.pdf

## 基本信息

- 文件：`LZQ 64 哮喘 深圳二院.pdf`
- 大小：50273.2 KB
- PDF 总页数：20
- doc_id：`d7626528908c11f1a3da71efcdd7cc1f`
- 上传方式：existing
- 状态：run=None (code=None)  progress=None
- 开始时间：2026-08-05T14:31:16  完成时间：2026-08-05T14:31:17  耗时：0.9s
- progress_msg：`05:24:53 Indexing done (0.07s). Task done (448.78s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 23a18ef5 | 4 | 1-4 | 门诊病历 科室:呼吸与危重症医学科 门 联系人 性别:女 年龄:62岁 婚姻状况 |
| 2 | 3c2975f1 | 3 | 5-7 | 门诊病历 科室:呼吸与危重症医学科 姓 性别:女 门诊 联系方 年龄:62岁 婚 |
| 3 | ccdcef2f | 3 | 8-10 | 科室:呼吸与危重症医学科 门诊 姓名 联系 性别:女 年龄:63岁 婚姻状况:其 |
| 4 | 13cd3a3d | 3 | 11-13 | 门诊病历 科室:呼吸与危重症医学科 姓名 性别:女 门诊 联系方式 年龄:63岁 |
| 5 | fdb1a4e8 | 1 | 14-14 | 门诊 姓名： 门(急)诊初诊病历 性别：女 科室：呼吸内科门诊 年龄：63岁 就 |
| 6 | be2980a6 | 1 | 15-15 | 广东省医疗门诊收费票据（电子） 广东省 财政部监制 票据代码：44060125  |
| 7 | afa649a3 | 1 | 16-16 | 电子发票(普通发票) 发票号码：25447000001429974977 开票日 |
| 8 | 30a50751 | 1 | 17-17 | 门诊号 姓名 科室:呼吸内科门诊 门(急)诊初诊病历 电话 性别:女 年龄:63 |
| 9 | afc41d4c | 1 | 18-18 | 广东省医疗门诊收费票据（电子） 广东省 财政部监制 票据代码：44 票据号码：9 |
| 10 | e7f32e20 | 1 | 19-19 | 10:15 淘 交易成功 医药仁康堂医药专营店> 【信必可】布地奈德福莫特罗 ¥ |
| 11 | 2bbc5f2a | 1 | 20-20 | 电子发票(普通发票) 发票号码：26322000000914042776 开票日 |

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
- ChunkMerger：`{"found": true, "merged": 11, "sources": 8, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 6, "Extractor:Medication": 5, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1}, "filtered_noise": 6}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-05 05:24:51,895 INFO     29 [ChunkMerger] Merged 11 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 6, 'Extractor:Medication': 5, 'Extractor:Presc`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-05 05:16:41,829 INFO     29 handle_task begin for task {"id": "d7b98bb4908c11f1a3da71efcdd7cc1f", "doc_id": "d7626528908c11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479738, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785907001430, "task_type": "dataflow", "root_trace_id": "ea6d5499d1eb4a3cabaa8fb5a06c80f8", "root_traceparent": "00-ea6d5499d1eb4a3cabaa8fb5a06c80f8-0f37f835e898f31c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-05 05:16:42,020 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.002s]
2026-08-05 05:16:42,060 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-05 05:16:42,090 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-05 05:16:42,090 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-05 05:16:42,104 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-05 05:16:42,104 INFO     29 ============================================================
2026-08-05 05:16:42,104 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-05 05:16:42,104 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-05 05:16:42,104 INFO     29 ============================================================
2026-08-05 05:16:42,104 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-05 05:16:42,104 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-05 05:16:42,106 INFO     29 No torch found.
2026-08-05 05:16:44,682 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=20
2026-08-05 05:16:44,833 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1272276, prompt_len=644
2026-08-05 05:16:46,141 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:16:46,141 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-05 05:16:46,150 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1272276, prompt_len=401
2026-08-05 05:16:51,195 INFO     29 [qwen-vl-parser] text API response (len=898):
["门诊病历", "科室:呼吸与危重症医学科", "门", "联系人", "性别:女", "年龄:62岁", "婚姻状况:其他", "2024-01-10 10:27 初诊记录", "主诉:发作性喘息12年余", "现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年", "余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现", "气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行", "听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并", "规律使用信必可320ug bid后症状缓解。近日活动后气促再发,否认喘", "鸣音。无发热、胸痛。", "既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。", "既往病史:", "1.2022.12.10肝囊肿,持续;", "2.2023.10.31鼻窦炎,持续;", "3.2023.10.31双肺良性小结节,持续;", "4.2023.11.03-2023.12.13,肺肺部感染;", "一年内支气管哮喘急性发作病史:", "12023.11.03-2023.11.08,支气管哮喘急性发作,8mg、4mg甲泼尼龙qd", "各服用3天;", "22023.12.13-2023.12.15,支气管哮喘急性发作,4mg甲泼尼龙片qd,服用", "3天。", "一年内合并用药:", "1.左氧氟沙星片,2023.11.03-2023.12.01,0.5g,qd,po,用于治疗肺部感染", "2.甲泼尼龙片,2023.11.03-2023.11.05,8mg,qd,po,用于治疗支气管哮喘急", "性发作。", "3.甲泼尼龙片,2023.11.06-2023.11.08,4mg,qd,po,用于治疗支气管哮喘急", "性发作。", "4.孟鲁司特钠片,2023.11.03-2023.11.12,10mg,qn,po,用于治疗支气管哮喘", "急性发作。", "第1页", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 05:16:51,195 INFO     29 [qwen-vl-parser] page=1 text: 37 lines (bbox 0-36)
2026-08-05 05:16:51,196 INFO     29 [qwen-vl-parser] page=1 text: 37 sections
2026-08-05 05:16:51,351 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1361374, prompt_len=644
2026-08-05 05:16:52,672 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:16:52,673 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-05 05:16:52,696 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1361374, prompt_len=401
2026-08-05 05:16:54,454 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:16:54.453+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 16, "failed": 0, "current": {"d7b98bb4908c11f1a3da71efcdd7cc1f": {"id": "d7b98bb4908c11f1a3da71efcdd7cc1f", "doc_id": "d7626528908c11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479738, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785907001430, "task_type": "dataflow", "root_trace_id": "ea6d5499d1eb4a3cabaa8fb5a06c80f8", "root_traceparent": "00-ea6d5499d1eb4a3cabaa8fb5a06c80f8-0f37f835e898f31c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:16:57,744 INFO     29 [qwen-vl-parser] text API response (len=913):
["门诊病历", "科室:呼吸与危重症医学科", "姓名", "性别:女", "联系方式", "年龄:62岁", "婚姻状况:其他", "2024-01-10 10:27 初诊记录", "5.桉柠蒎肠溶软胶囊,2023.11.03-2023.11.15,0.3g,tid,po,用于治疗肺部感", "染。", "7.甲泼尼龙片,2023.12.13-2023.12.15,4mg,qd,po,用于治疗支气管哮喘急", "性发作。", "8.布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,", "320ug,bid,经口腔吸入,用于控制哮喘。", "过敏史:否认食物、药物过敏史。", "体格检查 收缩压（mmHg）:107;舒张压（mmHg）:75", "其他体格检查:身高:153cm,体重:48.5kg,", "09:50进行生命体征测量:体温:36.4℃,血压:107/75mmHg,呼吸:19", "次/分,脉搏:78次/分;", "查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见", "皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅", "大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。", "耳廓正常无畸形,外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无", "鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿", "大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中", "肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动", "正常,双肺呼吸音粗,未闻及干湿罗音。心律齐。双下肢无水肿。心率", "78次/分,心音正常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛", "反跳痛,无液波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触", "及,肾脏未触及,Murphy征阴性,移动性浊音阴性,肠鸣音正常。外生殖", "器未查、肛门直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无", "异常,其他无异常。.", "第2页", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 05:16:57,745 INFO     29 [qwen-vl-parser] page=2 text: 35 lines (bbox 37-71)
2026-08-05 05:16:57,745 INFO     29 [qwen-vl-parser] page=2 text: 35 sections
2026-08-05 05:16:57,925 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1581395, prompt_len=644
2026-08-05 05:16:59,256 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:16:59,256 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-05 05:16:59,265 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1581395, prompt_len=401
2026-08-05 05:17:07,460 INFO     29 [qwen-vl-parser] text API response (len=978):
["科室:呼吸与危重症医学科", "姓名:", "性别:女", "门诊", "联系方式", "596", "年龄:62岁", "婚姻状况:其他", "2024-01-10 10:27 初诊记录", "检验检查:阅片见双肺轻度支气管扩张,未见明显急性炎症病灶,余肺基本同前", "(正式报告为准)", "初步诊断:1.鼻窦炎;2.支气管哮喘;", "处理:药品:", "(省采3)硫酸沙丁胺醇吸入气雾剂200揿(100μg/揿)/瓶(1【瓶】) sig:", "(200【揿】)吸入pm(需要时);", "检查:心脏电生理:心电图(十二导联心电图);CT检查:副鼻窦平扫;", "使用螺旋扫描加收;普放:DR胸部正侧位片*(2);呼吸专科检查:支气管", "舒张试验、流速容量曲线;", "检验:凝血四项、肾功能六项+肝功能八项+血脂六项*+电解质六项+空", "腹血糖(门诊使用)+肝酶学补充7项+心肌损伤六项、血常规5分类、尿", "常规加化学分析、感染八项", "治疗:静脉采血", "根据患者病情,认为患者基本符合“评价SHR-1905注射液在重度未", "控制哮喘患者中的有效性及安全性-多中心、随机、双盲、安慰剂对照", "平行设计II期临床研究(SHR-1905-201)”的筛选要求,2024.01.10 09:15", "生向患者__及其家属详细介绍该试验目的、试验设计、受试", "者风险及受益、受试者义务及研究者义务等。根据方案(版本号:2.0,", "版本日期:2022年8月31日)要求,筛选期所有受试者均进行吸入支气", "管扩张剂前后肺功能检查,若受试者无法提供筛选前一年内气道可逆", "性检测报告(吸入沙丁胺醇后FEV1增加≥12%且FEV1绝对值增加≥", "200mL),则筛选期肺功能检查需要满足吸入沙丁胺醇后FEV1增加≥", "12%且FEV1绝对值增加≥200mL。符合要求后才可以入组,受试者表", "示同意。患者.__及其家属表示已充分了解以上告知内容,同意参加", "该临床试验,", "医生与患者__于2024.01.10 09:47同时签署了知", "情同意书(版本号:2.0,版本日期:2022年08月31日),一式两份,一份", "第3页", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 05:17:07,460 INFO     29 [qwen-vl-parser] page=3 text: 39 lines (bbox 72-110)
2026-08-05 05:17:07,460 INFO     29 [qwen-vl-parser] page=3 text: 39 sections
2026-08-05 05:17:07,583 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=880816, prompt_len=644
2026-08-05 05:17:08,900 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:17:08,900 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-05 05:17:08,906 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=880816, prompt_len=401
2026-08-05 05:17:11,893 INFO     29 [qwen-vl-parser] text API response (len=536):
["门诊病历", "科室:呼吸与危重症医学科", "姓名:", "性别:女", "门诊", "联系方式", "年龄:62岁", "婚姻状况:其他", "2024-01-10 10:27 初诊记录", "交给患者保存,一份保存在研究中心。签署知情同意书后患者进入筛选", "流程,受试者筛选号为CN..", "新增AE:", "1.高尿酸血症,2024.01.10开始,轻度,持续,与研究药物肯定无关,对研", "究药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。", "2.高脂血症,2024.01.10开始,轻度,持续,与研究药物肯定无关,对研究", "药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。", "3.白细胞计数降低,2024.01.10开始,轻度,持续,与研究药物肯定无关", "对研究药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。此项", "指标与患者临床症状不符,考虑让其一周内复测。", "规律使用吸入药物,用后漱口,定期复诊;避免接触可能过敏原;不用地", "毯,不养动物", "医师签", "门诊病历专用", "※提醒:复诊时,请携带本病历记录,谢谢!※", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 05:17:11,894 INFO     29 [qwen-vl-parser] page=4 text: 26 lines (bbox 111-136)
2026-08-05 05:17:11,894 INFO     29 [qwen-vl-parser] page=4 text: 26 sections
2026-08-05 05:17:12,054 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1312119, prompt_len=644
2026-08-05 05:17:13,348 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:17:13,349 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-05 05:17:13,363 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1312119, prompt_len=401
2026-08-05 05:17:18,294 INFO     29 [qwen-vl-parser] text API response (len=879):
["门诊病历", "科室:呼吸与危重症医学科", "姓", "性别:女", "门诊", "联系方", "年龄:62岁", "婚姻状况:其他", "2024-03-21 08:40 初诊记录", "主诉:SHR-1905-201 试验复筛", "现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年", "余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现", "气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行", "听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并", "规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可", "320ug bid,近日活动后气促再发,否认喘鸣音。无发热、胸痛。", "2024.01.10参加SHR-1905-201临床试验,因白细胞计数<3.0*10^9/L符", "合排除标准第12条筛败,于2024.03.01血液科就诊,无特殊处理,", "2024.03.06进行SHR-1905-201试验二次知情。受试者今日返院完成V3", "访视。", "既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。", "既往病史:", "1.2022.12.10肝囊肿,持续;", "2.2023.10.31鼻窦炎,持续;", "3.2023.10.31双肺良性小结节,持续;", "4.2023.11.03-2023.12.13,肺肺部感染;", "5.2024.03.01开始,白细胞数降低1级;", "6.2024.01.10开始,高脂蛋白a血症,", "过敏史:否认食物、药物过敏史。", "体格检查收缩压(mmHg):113;舒张压(mmHg):76", "其他体格检查:09:37进行生命体征测量:体温:36.5℃,血压:", "113/76mmHg,呼吸:18次/分,脉搏:98次/分;", "查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见", "第1页"]
2026-08-05 05:17:18,294 INFO     29 [qwen-vl-parser] page=5 text: 34 lines (bbox 137-170)
2026-08-05 05:17:18,295 INFO     29 [qwen-vl-parser] page=5 text: 34 sections
2026-08-05 05:17:18,470 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1571361, prompt_len=644
2026-08-05 05:17:19,834 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:17:19,835 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-05 05:17:19,850 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1571361, prompt_len=401
2026-08-05 05:17:24,495 INFO     29 [qwen-vl-parser] text API response (len=850):
["科室:呼吸与危重症医学科", "姓名", "性别:女", "门诊", "联系方", "年龄:62岁", "婚姻状况:其他", "2024-03-21 08:40 初诊记录", "皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅", "大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。", "耳廓正常无畸形,外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无", "鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿", "大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中", "肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动", "正常,双肺呼吸音粗,未闻及干湿罗音。心律齐。双下肢无水肿。心音正", "常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛、反跳痛,无液", "波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触及,肾脏未触", "及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖器未查、肛门", "直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无异常,其他无", "异常。.", "检验检查:无", "初步诊断:支气管哮喘", "处理:", "CM 跟踪:", "1、布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,", "320ug,bid,经口腔吸入,用于控制哮喘。", "处理:", "1、2024.03.14-2024.03.21 家用峰流速仪使用 ePRO 系统填写依从性", "7/7*100%=100%,嘱托患者按照自己实际情况及时填写日志,如有问题", "随时沟通。", "2、无新增 AE,CM,无临床试验安全性事件。", "3、今日回收硫酸沙丁胺醇吸入气雾剂,发放新的硫酸沙丁胺醇吸入气", "雾剂1盒,并嘱托受试者正确保存和使用。", "4、绝经期女性,未做血、尿妊娠检查。", "第2页", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 05:17:24,495 INFO     29 [qwen-vl-parser] page=6 text: 37 lines (bbox 171-207)
2026-08-05 05:17:24,495 INFO     29 [qwen-vl-parser] page=6 text: 37 sections
2026-08-05 05:17:24,585 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=524906, prompt_len=644
2026-08-05 05:17:25,762 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:17:25,763 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-05 05:17:25,781 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=524906, prompt_len=401
2026-08-05 05:17:27,496 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:17:27.496+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 16, "failed": 0, "current": {"d7b98bb4908c11f1a3da71efcdd7cc1f": {"id": "d7b98bb4908c11f1a3da71efcdd7cc1f", "doc_id": "d7626528908c11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479738, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785907001430, "task_type": "dataflow", "root_trace_id": "ea6d5499d1eb4a3cabaa8fb5a06c80f8", "root_traceparent": "00-ea6d5499d1eb4a3cabaa8fb5a06c80f8-0f37f835e898f31c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:17:27,538 INFO     29 [qwen-vl-parser] text API response (len=301):
["科室:呼吸与危重症医学科", "门诊", "姓名", "联系方式", "性别:女", "年龄:62岁", "婚姻状况:其他", "2024-03-21 08:40 初诊记录", "5、受试者所有检查结果经再次核对入排,符合所有入选标准,不符合任", "一排除标准,可随机入组,分配随机号:_,随机分层信息:中剂量", "ICS,嗜酸性粒细胞计数<300/ul,未联合使用LAMA。", "6、嘱托受试者2024.03.22来院行V4随访。", "医师签", "门诊病历专用章", "※提醒:复诊时,请携带本病历记录,谢谢!※", "第3页", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 05:17:27,538 INFO     29 [qwen-vl-parser] page=7 text: 18 lines (bbox 208-225)
2026-08-05 05:17:27,539 INFO     29 [qwen-vl-parser] page=7 text: 18 sections
2026-08-05 05:17:27,700 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1355651, prompt_len=644
2026-08-05 05:17:29,012 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:17:29,013 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=None
2026-08-05 05:17:29,029 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1355651, prompt_len=401
2026-08-05 05:17:34,439 INFO     29 [qwen-vl-parser] text API response (len=837):
["科室:呼吸与危重症医学科", "门诊", "姓名", "联系", "性别:女", "年龄:63岁", "婚姻状况:其他", "2024-12-12 09:40 初诊记录", "主诉:SHR-1905-201 临床试验 V14", "现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年", "余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现", "气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行", "听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并", "规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可", "320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:", "近日咳嗽咳痰,低烧两天,呼吸道感染。2024.12.02行V14随访", "因患者发热延迟用药。今日回院用药,留院观察1h。", "既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。", "既往病史:", "1.2022.12.10肝囊肿,持续;", "2.2023.10.31鼻窦炎,持续;", "3.2023.10.31双肺良性小结节,持续;", "4.2023.11.03-2023.12.13,肺肺部感染;", "5.2024.03.01开始,白细胞数降低1级,持续;", "6.2024.01.10开始,高脂血症,持续;", "7.十余年前,慢性浅表胃炎,持续中。", "过敏史:否认食物、药物过敏史。", "体格检查收缩压(mmHg):-;舒张压(mmHg):-", "其他体格检查:未行", "检验检查:无", "初步诊断:支气管哮喘", "处理:检查:心脏电生理:心电图(十二导联心电图);", "检验:急诊血常规(五分类)+急诊超敏C反应蛋白、急诊肝功能五项", "治疗:静脉采血", "第1页"]
2026-08-05 05:17:34,439 INFO     29 [qwen-vl-parser] page=8 text: 35 lines (bbox 226-260)
2026-08-05 05:17:34,440 INFO     29 [qwen-vl-parser] page=8 text: 35 sections
2026-08-05 05:17:34,578 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1105548, prompt_len=644
2026-08-05 05:17:35,883 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:17:35,883 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-05 05:17:35,892 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1105548, prompt_len=401
2026-08-05 05:17:43,386 INFO     29 [qwen-vl-parser] text API response (len=801):
["科室:呼吸与危重症医学科", "性别:女", "年龄:63岁", "婚姻状况:其他", "2024-12-12 09:40 初诊记录", "无新增 AE,无新增 CM,无临床试验安全性事件。", "呼吸道感染,2024.1127-2024.12.11,中度,与试验药物关系为可能无关", "对试验药物采取的措施为延迟用药,对 AE 采取的措施为药物治疗,肺", "SAE,非 SIE,不因此退出临床试验。", "跟踪 CM:", "1.盐酸莫西沙片,2024.12.02-2024.12.11,持续中,0.4g/片,1片/次,", "qd,po,用于治疗 AE 呼吸道感染。", "2.桉柠蒎肠溶胶囊,2024.12.02-2024.12.11 持续中,0.3g/粒,1粒/次,", "tid,po,用于治疗 AE 呼吸道感染。(化痰)", "3.氯苯那敏片,2024.12.02-2024.12.11,持续中,4mg/片,1片/次,", "qn,po,用于治疗 AE 呼吸道感染。", "4.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po.用于治", "疗病史慢性浅表胃炎。", "5.复方氨酚烷胺胶囊,2024.11.27-2024.12.02,持续中,0.25g:0.1g,1粒", "/次,bid,po,用于治疗 AE 呼吸道感染。", "6.吸入沙丁胺醇气雾剂,2024.12.02-2024.12.02,400ug,吸入,once,用于支", "气管扩张检查。", "CM 跟踪:", "1、布地奈德福莫特罗粉吸入剂,2022.1127 开始,持续使用,", "320ug,bid,经口腔吸入,用于控制哮喘。", "2、硫酸沙丁胺醇气雾剂,2024.03.06 开始,持续中,100ug,pm,经口腔吸", "入,控制哮喘急性发作。", "第2页"]
2026-08-05 05:17:43,387 INFO     29 [qwen-vl-parser] page=9 text: 28 lines (bbox 261-288)
2026-08-05 05:17:43,387 INFO     29 [qwen-vl-parser] page=9 text: 28 sections
2026-08-05 05:17:43,479 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=484906, prompt_len=644
2026-08-05 05:17:44,718 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:17:44,719 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=None
2026-08-05 05:17:44,725 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=484906, prompt_len=401
2026-08-05 05:17:46,191 INFO     29 [qwen-vl-parser] text API response (len=256):
["门诊病历", "科室:呼吸与危重症医学科", "姓名:", "性别:女", "门诊号", "联系方式", "年龄:63岁", "婚姻状况:其他", "2024-12-12 09:40 初诊记录", "处理:", "患者于今日12:21-12:28完成临床试验药物的注射，药物编号为", "Y6077Y4950 用药前完善必要检查后随机用药。", "医师", "门诊病历", "※提醒:复诊时,请携带本病历记录,谢谢!※", "“若有高血压糖尿病诊断,建议您到居住地附近社康中心,建立居民健康档案”", ""]
2026-08-05 05:17:46,191 INFO     29 [qwen-vl-parser] page=10 text: 16 lines (bbox 289-304)
2026-08-05 05:17:46,191 INFO     29 [qwen-vl-parser] page=10 text: 16 sections
2026-08-05 05:17:46,372 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1693459, prompt_len=644
2026-08-05 05:17:47,754 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:17:47,754 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=None
2026-08-05 05:17:47,761 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1693459, prompt_len=401
2026-08-05 05:17:53,076 INFO     29 [qwen-vl-parser] text API response (len=967):
["门诊病历", "科室:呼吸与危重症医学科", "姓名", "性别:女", "门诊", "联系方式", "年龄:63岁", "婚姻状况:其他", "2025-07-31 17:13 初诊记录", "主诉:SHR-1905V19随访", "现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年", "余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现", "气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行", "听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并", "规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可", "320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:", "20036.。近日无咳嗽咳痰,无胸闷气喘,无发热,无支气管哮喘急性发作", "今日回院行V19随访。", "既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。", "既往病史:", "1.2022.12.10肝囊肿,持续;", "2.2023.10.31鼻窦炎,持续;", "3.2023.10.31双肺良性小结节,持续;", "4.2023.11.03-2023.12.13,肺肺部感染;", "5.2024.03.01开始,白细胞数降低1级,持续;", "6.2024.01.10高脂血症,持续中", "过敏史:否认食物、药物过敏史。", "体格检查收缩压(mmHg):103;舒张压(mmHg):64", "其他体格检查:进行生命体征测量:体温:36.4℃,血压:", "103/64mmHg,呼吸:18次/分,脉搏:76次/分;", "查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见", "皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅", "大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。", "耳廓正常无畸形外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无", "鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿", "第1页", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 05:17:53,076 INFO     29 [qwen-vl-parser] page=11 text: 38 lines (bbox 305-342)
2026-08-05 05:17:53,076 INFO     29 [qwen-vl-parser] page=11 text: 38 sections
2026-08-05 05:17:53,249 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1486615, prompt_len=644
2026-08-05 05:17:54,605 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:17:54,605 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=None
2026-08-05 05:17:54,612 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1486615, prompt_len=401
2026-08-05 05:17:59,293 INFO     29 [qwen-vl-parser] text API response (len=876):
["门诊病历", "科室:呼吸与危重症医学科", "性别:女", "门诊", "联系方式:", "年龄:63岁", "婚姻状况:其他", "2025-07-31 17:13 初诊记录", "大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中", "肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动", "正常,左肺呼吸音清,未闻及粗干啰音。心律齐。双下肢无水肿。心音正", "常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛、反跳痛,无液", "波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触及,肾脏未触", "及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖器未查、肛门", "直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无异常,其他无", "异常。", "检验检查:已完善试验相关检验检查", "初步诊断:支气管哮喘", "处理:尿常规检查尿隐血,建议定期检查,必要时肾内科就诊。", "无临床试验安全性事,无新增 AE。", "新增合并用药:硫酸沙丁胺醇吸入气雾剂,2025.07.31-", "2025.078.31,400ug,once,吸入,用于支气管扩张检查。", "CM 跟踪:", "1、布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,", "320ug,bid,经口腔吸入,用于控制哮喘。", "2、硫酸沙丁胺醇气雾剂,2024.03.06开始,持续中,100ug,pm,经口腔吸", "入,控制哮喘急性发作。", "3.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po.用于治", "疗病史慢性浅表胃炎。", "处理:", "12025.05.13-2025.07.31 家用峰流速仪使用 ePRO 系统填写依从性大于", "80%,今日已解绑 ePRO 系统。", "2遵从临床试验方案完成 IgE,PK,ADA 采血,完成 ACQ-6,AQLQ 问卷填", "写。", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 05:17:59,294 INFO     29 [qwen-vl-parser] page=12 text: 36 lines (bbox 343-378)
2026-08-05 05:17:59,294 INFO     29 [qwen-vl-parser] page=12 text: 36 sections
2026-08-05 05:17:59,416 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=785150, prompt_len=644
2026-08-05 05:18:00,392 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:18:00.389+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 16, "failed": 0, "current": {"d7b98bb4908c11f1a3da71efcdd7cc1f": {"id": "d7b98bb4908c11f1a3da71efcdd7cc1f", "doc_id": "d7626528908c11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479738, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785907001430, "task_type": "dataflow", "root_trace_id": "ea6d5499d1eb4a3cabaa8fb5a06c80f8", "root_traceparent": "00-ea6d5499d1eb4a3cabaa8fb5a06c80f8-0f37f835e898f31c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:18:00,770 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:18:00,770 INFO     29 [qwen-vl-parser] page=13 classify=text report_date=None
2026-08-05 05:18:00,793 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=785150, prompt_len=401
2026-08-05 05:18:02,779 INFO     29 [qwen-vl-parser] text API response (len=341):
["门诊病历", "科室:呼吸与危重症医学科", "姓名", "性别:女", "门诊", "联系", "年龄:63岁", "婚姻状况:其他", "2025-07-31 17:13 初诊记录", "3.患者于今日肺功能检查前已停用基础吸入药物布地奈德福莫特罗粉", "吸入剂大于12h,停药时间2025.07.30上午,具体时间不详。", "4.患者已于今日完成随访期随访。", "5.因患者未找到发放万托林,可能已经丢失故不予回收。", "6.嘱患者规律使用吸入药物布地奈德福莫特罗粉吸入剂,药物自备。", "医师", "门诊病历专用章", "※提醒:复诊时,请携带本病历记录,谢谢!※", "“若有高血压糖尿病诊断,建议您到居住地附近社康中心,建立居民健康档案”", "第3页"]
2026-08-05 05:18:02,780 INFO     29 [qwen-vl-parser] page=13 text: 19 lines (bbox 379-397)
2026-08-05 05:18:02,780 INFO     29 [qwen-vl-parser] page=13 text: 19 sections
2026-08-05 05:18:03,025 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2492696, prompt_len=644
2026-08-05 05:18:04,356 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:18:04,357 INFO     29 [qwen-vl-parser] page=14 classify=text report_date=None
2026-08-05 05:18:04,367 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2492696, prompt_len=401
2026-08-05 05:18:12,642 INFO     29 [qwen-vl-parser] text API response (len=895):
["门诊", "姓名：", "门(急)诊初诊病历", "性别：女", "科室：呼吸内科门诊", "年龄：63岁", "就诊日期：2025-10-25 15:22", "主诉：支气管哮喘复诊", "现病史：患者支气管哮喘复诊，目前规律吸入布地奈德福莫特罗320ug 一次1吸，", "一天2次。目前诉有咳嗽、咳痰，有气促感，无胸闷，无发热，无鼻塞、流涕，无咯", "血、痰中带血，无头痛、头晕、视物旋转，无饮水呛咳，无咽痛、腹痛、腹胀等不", "适。未予处理及就医。现患者为求进一步诊治，故至我院科门诊就医。", "既往史：否认高血压、否认糖尿病、否认冠心病等慢性疾病病史，否认肝炎、结核", "等传染病史，否认手术外伤输血史 过敏史：无食物、药物过敏史。。否认饮酒史。", "个人史：已婚已育", "家族史：否认家族病史。", "体格检查：T：36.8℃ P：87次/分 R：21次/分 BP：108/73mmHg 指脉氧：", "9%。神志清楚，精神尚可，呼吸平顺，口唇无发绀，咽部无充血，扁桃体无肿大，", "双侧颈静脉无怒张，双肺呼吸音粗，双肺可闻及干啰音，双肺未闻及湿性啰音及胸膜", "摩擦音。心率87次/分，律齐，各瓣膜未闻及明显病理性杂音。腹部平软，全腹部无", "玉痛，反跳痛，肠鸣音正常。四肢运动自如，双下肢无水肿。", "辅助检查：患者自行购买布地奈德福莫特罗320ug 一次1吸，一天2次。", "初步诊断：", "西医诊断：1.支气管哮喘(急性发作期)", "处理意见：", "醋酸泼尼松片（国基）(5mg*100片) 20.000mg", "1次/天 口服", "12.00片", "硫酸沙丁胺醇吸入气雾剂（省3、国基）(200揿：", "100μg) 200.000μg", "1次/天 吸入", "1.00瓶", "建议：建议患者结果回报后请及时至我科门诊复诊，若出现病情变化或病情加重", "无好转等，请及时至急诊科门诊复诊。", "温馨提示：1.请妥善保管好病历及各种检查检验报告单。", "2.复诊时，请携带本病历记录，谢谢！", "第1页(共1页)"]
2026-08-05 05:18:12,644 INFO     29 [qwen-vl-parser] page=14 text: 37 lines (bbox 398-434)
2026-08-05 05:18:12,644 INFO     29 [qwen-vl-parser] page=14 text: 37 sections
2026-08-05 05:18:12,766 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=899102, prompt_len=644
2026-08-05 05:18:14,034 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:18:14,034 INFO     29 [qwen-vl-parser] page=15 classify=text report_date=None
2026-08-05 05:18:14,040 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=899102, prompt_len=401
2026-08-05 05:18:17,849 INFO     29 [qwen-vl-parser] text API response (len=835):
["广东省医疗门诊收费票据（电子）", "广东省", "财政部监制", "票据代码：44060125", "票据号码：9148002082", "校验码：831306", "开票日期：2025-10-25", "项目名称", "数量/单位", "金额（元）", "备注", "项目名称", "数量/单位", "金额（元）", "备注", "西药费", "1", "13.05", "", "", "", "", "", "以下是清单项", "", "", "", "", "", "", "", "醋酸泼尼松片（国基）", "12", "0.50", "", "硫酸沙丁胺醇吸入气雾剂（省3", "1", "12.55", "", "、国基）", "", "", "", "", "", "", "", "金额合计（大写）壹拾叁元零伍分", "(小写)13.05", "", "", "业务流水号：SF10390911", "门诊", "", "", "就诊日期：20251025", "其他信息", "医疗机构类型：综合医院", "医保类型：现金(自费)", "医保编号：", "性别：女", "医保统筹基金支付：0.00", "其他支付：0.00", "个人账户支付：0.00", "个人现金支付：13.05", "个人自付：0.00", "个人自费：13.05", "", "", "政策性减免：", "", "", "收款单位（章）深圳市龙岗区第人民医院", "复核人：掌上医院", "收款人：掌上医院", "说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。", "单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dzpj.czt.gd.gov.cn/billcheck查验本省财政电子票据。", "CS 扫描全能王", "3 亿人都在用的扫描 App"]
2026-08-05 05:18:17,849 INFO     29 [qwen-vl-parser] page=15 text: 50 lines (bbox 435-484)
2026-08-05 05:18:17,849 INFO     29 [qwen-vl-parser] page=15 text: 50 sections
2026-08-05 05:18:17,966 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=750717, prompt_len=644
2026-08-05 05:18:19,283 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:18:19,284 INFO     29 [qwen-vl-parser] page=16 classify=text report_date=None
2026-08-05 05:18:19,297 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=750717, prompt_len=401
2026-08-05 05:18:21,536 INFO     29 [qwen-vl-parser] text API response (len=419):
["电子发票(普通发票)", "发票号码：25447000001429974977", "开票日期：2025年11月05日", "广东省税务局", "购买方信息", "名称：", "统一社会信用代码/纳税人识别号：", "销售方信息", "名称：阿里健康大药房医药连锁有限公司", "统一社会信用代码/纳税人识别号：91440101681325547Y", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*化学药品制剂*布地奈德", "盒", "3", "176.70", "530.09", "13%", "68.91", "福莫特罗吸入粉雾剂", "合计", "￥530.09", "￥68.91", "价税合计（大写）", "伍佰玖拾玖圆整", "(小写)￥599.00", "备注", "开票人：董茜玲", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 05:18:21,537 INFO     29 [qwen-vl-parser] page=16 text: 36 lines (bbox 485-520)
2026-08-05 05:18:21,537 INFO     29 [qwen-vl-parser] page=16 text: 36 sections
2026-08-05 05:18:21,710 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1499579, prompt_len=644
2026-08-05 05:18:22,980 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:18:22,981 INFO     29 [qwen-vl-parser] page=17 classify=text report_date=None
2026-08-05 05:18:22,993 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1499579, prompt_len=401
2026-08-05 05:18:27,519 INFO     29 [qwen-vl-parser] text API response (len=804):
["门诊号", "姓名", "科室:呼吸内科门诊", "门(急)诊初诊病历", "电话", "性别:女", "年龄:63岁", "就诊日期:2025-11-24 15:01", "主诉:支气管哮喘复诊", "现病史:患者支气管哮喘复诊,目前规律吸入布地奈德福莫特罗320一次1吸,一天2次(患者自行网购药物),目前有咳嗽、咳痰,咳嗽时有气喘感。无胸闷,无发热,无鼻塞、流涕,无咯血、痰中带血,无头痛、头晕、视物旋转,无饮水呛咳,无咽痛、腹痛、腹胀等不适。未予处理及就医。现患者为求进一步诊治,故至我院科门诊就医。", "既往史:否认高血压、否认糖尿病、否认冠心病等慢性疾病病史,否认肝炎、结核等传染病史,否认手术外伤输血史过敏史:无食物、药物过敏史。。否认饮酒史。", "个人史:已婚已育", "家族史:否认家族病史。", "体格检查:T:36.8℃ P:87次/分 R:21次/分 BP:108/73mmHg 指脉氧:99%。神志清楚,精神尚可,呼吸平顺,口唇无发绀,咽部无充血,扁桃体无肿大,双侧颈静脉无怒张,双肺呼吸音粗,双肺可闻及散在干啰音,双肺未闻及湿性啰音及胸膜摩擦音。心率87次/分,律齐,各瓣膜未闻及明显病理性杂音。腹部平软,全腹部无压痛,反跳痛,肠鸣音正常。四肢运动自如,双下肢无水肿。", "辅助检查:", "初步诊断:", "西医诊断:1.支气管哮喘(急性发作期)", "处理意见:自备布地奈德福莫特罗320一次1吸,一天2次", "醋酸泼尼松片(国基)(5mg*100片)10.000mg", "1次/天 口服 6.00片", "建议:建议患者结果回报后请及时至我科门诊复诊,若出现病情变化或病情加重无好转等,请及时至急诊科门诊复诊。", "医生签名:", "温馨提示:1.请妥善保管好病历及各种检查检验报告单。", "2.复诊时,请携带本病历记录,谢谢!", "第1页(共1页)"]
2026-08-05 05:18:27,519 INFO     29 [qwen-vl-parser] page=17 text: 25 lines (bbox 521-545)
2026-08-05 05:18:27,519 INFO     29 [qwen-vl-parser] page=17 text: 25 sections
2026-08-05 05:18:27,631 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=811880, prompt_len=644
2026-08-05 05:18:28,836 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:18:28,837 INFO     29 [qwen-vl-parser] page=18 classify=text report_date=None
2026-08-05 05:18:28,848 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=811880, prompt_len=401
2026-08-05 05:18:32,053 INFO     29 [qwen-vl-parser] text API response (len=664):
["广东省医疗门诊收费票据（电子）", "广东省", "财政部监制", "票据代码：44", "票据号码：9148286284", "校验码：89a81f", "交款人", "开票日期：2025-11-24", "项目名称", "数量/单位", "金额（元）", "备注", "项目名称", "数量/单位", "金额（元）", "备注", "西药费", "1", "0.25", "以下是清单项", "醋酸泼尼松片（国基）", "6", "0.25", "金额合计（大写）贰角伍分", "(小写)0.25", "业务流水号：SF10481981", "门", "就诊日期：20251124", "其他信息", "医疗机构类型：综合医院", "医保类型：现金(自费)", "医保编号：", "性别：女", "医保统筹基金支付：0.00", "其他支付：0.00", "个人账户支付：0.00", "个人现金支付：0.25", "个人自付：0.00", "个人自费：0.25", "政策性减免：", "收款单位（章）", "人民医院", "复核人：吴亮梅", "收款人：吴亮梅", "说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。", "单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dipj.czt.gd.gov.cn/billcheck查验本省财政电子票据。", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 05:18:32,053 INFO     29 [qwen-vl-parser] page=18 text: 48 lines (bbox 546-593)
2026-08-05 05:18:32,053 INFO     29 [qwen-vl-parser] page=18 text: 48 sections
2026-08-05 05:18:32,163 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=729091, prompt_len=644
2026-08-05 05:18:33,411 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:18:33,412 INFO     29 [qwen-vl-parser] page=19 classify=text report_date=None
2026-08-05 05:18:33,433 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=729091, prompt_len=401
2026-08-05 05:18:33,448 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:18:33.447+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 16, "failed": 0, "current": {"d7b98bb4908c11f1a3da71efcdd7cc1f": {"id": "d7b98bb4908c11f1a3da71efcdd7cc1f", "doc_id": "d7626528908c11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479738, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785907001430, "task_type": "dataflow", "root_trace_id": "ea6d5499d1eb4a3cabaa8fb5a06c80f8", "root_traceparent": "00-ea6d5499d1eb4a3cabaa8fb5a06c80f8-0f37f835e898f31c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:18:36,489 INFO     29 [qwen-vl-parser] text API response (len=563):
["10:15", "淘", "交易成功", "医药仁康堂医药专营店>", "【信必可】布地奈德福莫特罗", "¥213", "放心买药", "正品保障", "1盒装", "不支持7天无理由 假一赔四>", "x1", "专业药师在线服务", "上天猫放心买药", "用药小贴士 1.哮喘。2.慢性阻塞性肺疾病(慢阻肺;...", "申请售后", "商品总价", "¥213", "运费(含服务费)", "¥8", "应付款", "¥221^", "订单信息 2026-01-20", "收起^", "订单编号", "4501919772001020746", "交易快照", "发生交易争议时，可作为判断依据>", "成交时间", "2026-01-26 22:25:02", "发货时间", "2026-01-21 12:24:52", "付款时间", "2026-01-20 19:25:06", "创建时间", "2026-01-20 19:24:30", "支付宝交易号", "2026012022001134951454085519", "天猫积分", "获得106点积分>", "客服", "更多", "查看处方", "查看物流", "评价", "扫描全能王", "扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 05:18:36,489 INFO     29 [qwen-vl-parser] page=19 text: 47 lines (bbox 594-640)
2026-08-05 05:18:36,489 INFO     29 [qwen-vl-parser] page=19 text: 47 sections
2026-08-05 05:18:36,617 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=799608, prompt_len=644
2026-08-05 05:18:37,972 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 05:18:37,972 INFO     29 [qwen-vl-parser] page=20 classify=text report_date=None
2026-08-05 05:18:37,984 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=799608, prompt_len=401
2026-08-05 05:18:40,258 INFO     29 [qwen-vl-parser] text API response (len=412):
["电子发票(普通发票)", "发票号码：26322000000914042776", "开票日期：2026年02月02日", "江苏省税务局", "购买方信息", "名称：", "统一社会信用代码/纳税人识别号：", "销售方信息", "名称：阜宁仁康堂大药房有限公司", "统一社会信用代码/纳税人识别号：91320923MAK1XP619R", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*生物化学药品*其他生物", "化学药品", "1", "218.811881188119", "218.81", "1%", "2.19", "合计", "¥218.81", "¥2.19", "价税合计（大写）", "贰佰贰拾壹圆整", "(小写)¥221.00", "备注", "开票人：杨雪", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-05 05:18:40,258 INFO     29 [qwen-vl-parser] page=20 text: 35 lines (bbox 641-675)
2026-08-05 05:18:40,258 INFO     29 [qwen-vl-parser] page=20 text: 35 sections
2026-08-05 05:18:40,258 INFO     29 [qwen-vl-parser] parse_pdf done: 676 sections from 20 pages.
2026-08-05 05:18:40,266 INFO     29 Close text detector.
2026-08-05 05:18:40,593 INFO     29 Close text recognizer.
2026-08-05 05:18:40,941 INFO     29 Close recognizer.
2026-08-05 05:18:41,290 INFO     29 Close recognizer.
2026-08-05 05:18:43,209 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-05 05:18:43,209 INFO     29 [Trace] task=d7b98bb4 | doc=LZQ 64 哮喘 深圳二院.pdf | Parser:MedLink | outputs={"html": "", "json": "676 items", "markdown": "", "text": "", "name": "LZQ 64 哮喘 深圳二院.pdf", "output_format": "json"}
2026-08-05 05:18:43,209 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-05 05:18:43,235 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:18:43,235 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。只有主诉，病史的也属于OutpatientRecord（门诊病历）\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 门诊病历\n[BBOX-1] 科室:呼吸与危重症医学科\n[BBOX-2] 门\n[BBOX-3] 联系人\n[BBOX-4] 性别:女\n[BBOX-5] 年龄:62岁\n[BBOX-6] 婚姻状况:其他\n[BBOX-7] 2024-01-10 10:27 初诊记录\n[BBOX-8] 主诉:发作性喘息12年余\n[BBOX-9] 现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年\n[BBOX-10] 余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现\n[BBOX-11] 气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行\n[BBOX-12] 听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并\n[BBOX-13] 规律使用信必可320ug bid后症状缓解。近日活动后气促再发,否认喘\n[BBOX-14] 鸣音。无发热、胸痛。\n[BBOX-15] 既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。\n[BBOX-16] 既往病史:\n[BBOX-17] 1.2022.12.10肝囊肿,持续;\n[BBOX-18] 2.2023.10.31鼻窦炎,持续;\n[BBOX-19] 3.2023.10.31双肺良性小结节,持续;\n[BBOX-20] 4.2023.11.03-2023.12.13,肺肺部感染;\n[BBOX-21] 一年内支气管哮喘急性发作病史:\n[BBOX-22] 12023.11.03-2023.11.08,支气管哮喘急性发作,8mg、4mg甲泼尼龙qd\n[BBOX-23] 各服用3天;\n[BBOX-24] 22023.12.13-2023.12.15,支气管哮喘急性发作,4mg甲泼尼龙片qd,服用\n[BBOX-25] 3天。\n[BBOX-26] 一年内合并用药:\n[BBOX-27] 1.左氧氟沙星片,2023.11.03-2023.12.01,0.5g,qd,po,用于治疗肺部感染\n[BBOX-28] 2.甲泼尼龙片,2023.11.03-2023.11.05,8mg,qd,po,用于治疗支气管哮喘急\n[BBOX-29] 性发作。\n[BBOX-30] 3.甲泼尼龙片,2023.11.06-2023.11.08,4mg,qd,po,用于治疗支气管哮喘急\n[BBOX-31] 性发作。\n[BBOX-32] 4.孟鲁司特钠片,2023.11.03-2023.11.12,10mg,qn,po,用于治疗支气管哮喘\n[BBOX-33] 急性发作。\n[BBOX-34] 第1页\n[BBOX-35] CS 扫描全能王\n[BBOX-36] 3亿人都在用的扫描App\n[BBOX-37] 门诊病历\n[BBOX-38] 科室:呼吸与危重症医学科\n[BBOX-39] 姓名\n[BBOX-40] 性别:女\n[BBOX-41] 联系方式\n[BBOX-42] 年龄:62岁\n[BBOX-43] 婚姻状况:其他\n[BBOX-44] 2024-01-10 10:27 初诊记录\n[BBOX-45] 5.桉柠蒎肠溶软胶囊,2023.11.03-2023.11.15,0.3g,tid,po,用于治疗肺部感\n[BBOX-46] 染。\n[BBOX-47] 7.甲泼尼龙片,2023.12.13-2023.12.15,4mg,qd,po,用于治疗支气管哮喘急\n[BBOX-48] 性发作。\n[BBOX-49] 8.布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,\n[BBOX-50] 320ug,bid,经口腔吸入,用于控制哮喘。\n[BBOX-51] 过敏史:否认食物、药物过敏史。\n[BBOX-52] 体格检查 收缩压（mmHg）:107;舒张压（mmHg）:75\n[BBOX-53] 其他体格检查:身高:153cm,体重:48.5kg,\n[BBOX-54] 09:50进行生命体征测量:体温:36.4℃,血压:107/75mmHg,呼吸:19\n[BBOX-55] 次/分,脉搏:78次/分;\n[BBOX-56] 查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见\n[BBOX-57] 皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅\n[BBOX-58] 大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。\n[BBOX-59] 耳廓正常无畸形,外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无\n[BBOX-60] 鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿\n[BBOX-61] 大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中\n[BBOX-62] 肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动\n[BBOX-63] 正常,双肺呼吸音粗,未闻及干湿罗音。心律齐。双下肢无水肿。心率\n[BBOX-64] 78次/分,心音正常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛\n[BBOX-65] 反跳痛,无液波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触\n[BBOX-66] 及,肾脏未触及,Murphy征阴性,移动性浊音阴性,肠鸣音正常。外生殖\n[BBOX-67] 器未查、肛门直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无\n[BBOX-68] 异常,其他无异常。.\n[BBOX-69] 第2页\n[BBOX-70] CS 扫描全能王\n[BBOX-71] 3亿人都在用的扫描App\n[BBOX-72] 科室:呼吸与危重症医学科\n[BBOX-73] 姓名:\n[BBOX-74] 性别:女\n[BBOX-75] 门诊\n[BBOX-76] 联系方式\n[BBOX-77] 596\n[BBOX-78] 年龄:62岁\n[BBOX-79] 婚姻状况:其他\n[BBOX-80] 2024-01-10 10:27 初诊记录\n[BBOX-81] 检验检查:阅片见双肺轻度支气管扩张,未见明显急性炎症病灶,余肺基本同前\n[BBOX-82] (正式报告为准)\n[BBOX-83] 初步诊断:1.鼻窦炎;2.支气管哮喘;\n[BBOX-84] 处理:药品:\n[BBOX-85] (省采3)硫酸沙丁胺醇吸入气雾剂200揿(100μg/揿)/瓶(1【瓶】) sig:\n[BBOX-86] (200【揿】)吸入pm(需要时);\n[BBOX-87] 检查:心脏电生理:心电图(十二导联心电图);CT检查:副鼻窦平扫;\n[BBOX-88] 使用螺旋扫描加收;普放:DR胸部正侧位片*(2);呼吸专科检查:支气管\n[BBOX-89] 舒张试验、流速容量曲线;\n[BBOX-90] 检验:凝血四项、肾功能六项+肝功能八项+血脂六项*+电解质六项+空\n[BBOX-91] 腹血糖(门诊使用)+肝酶学补充7项+心肌损伤六项、血常规5分类、尿\n[BBOX-92] 常规加化学分析、感染八项\n[BBOX-93] 治疗:静脉采血\n[BBOX-94] 根据患者病情,认为患者基本符合“评价SHR-1905注射液在重度未\n[BBOX-95] 控制哮喘患者中的有效性及安全性-多中心、随机、双盲、安慰剂对照\n[BBOX-96] 平行设计II期临床研究(SHR-1905-201)”的筛选要求,2024.01.10 09:15\n[BBOX-97] 生向患者__及其家属详细介绍该试验目的、试验设计、受试\n[BBOX-98] 者风险及受益、受试者义务及研究者义务等。根据方案(版本号:2.0,\n[BBOX-99] 版本日期:2022年8月31日)要求,筛选期所有受试者均进行吸入支气\n[BBOX-100] 管扩张剂前后肺功能检查,若受试者无法提供筛选前一年内气道可逆\n[BBOX-101] 性检测报告(吸入沙丁胺醇后FEV1增加≥12%且FEV1绝对值增加≥\n[BBOX-102] 200mL),则筛选期肺功能检查需要满足吸入沙丁胺醇后FEV1增加≥\n[BBOX-103] 12%且FEV1绝对值增加≥200mL。符合要求后才可以入组,受试者表\n[BBOX-104] 示同意。患者.__及其家属表示已充分了解以上告知内容,同意参加\n[BBOX-105] 该临床试验,\n[BBOX-106] 医生与患者__于2024.01.10 09:47同时签署了知\n[BBOX-107] 情同意书(版本号:2.0,版本日期:2022年08月31日),一式两份,一份\n[BBOX-108] 第3页\n[BBOX-109] CS 扫描全能王\n[BBOX-110] 3亿人都在用的扫描App\n[BBOX-111] 门诊病历\n[BBOX-112] 科室:呼吸与危重症医学科\n[BBOX-113] 姓名:\n[BBOX-114] 性别:女\n[BBOX-115] 门诊\n[BBOX-116] 联系方式\n[BBOX-117] 年龄:62岁\n[BBOX-118] 婚姻状况:其他\n[BBOX-119] 2024-01-10 10:27 初诊记录\n[BBOX-120] 交给患者保存,一份保存在研究中心。签署知情同意书后患者进入筛选\n[BBOX-121] 流程,受试者筛选号为CN..\n[BBOX-122] 新增AE:\n[BBOX-123] 1.高尿酸血症,2024.01.10开始,轻度,持续,与研究药物肯定无关,对研\n[BBOX-124] 究药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。\n[BBOX-125] 2.高脂血症,2024.01.10开始,轻度,持续,与研究药物肯定无关,对研究\n[BBOX-126] 药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。\n[BBOX-127] 3.白细胞计数降低,2024.01.10开始,轻度,持续,与研究药物肯定无关\n[BBOX-128] 对研究药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。此项\n[BBOX-129] 指标与患者临床症状不符,考虑让其一周内复测。\n[BBOX-130] 规律使用吸入药物,用后漱口,定期复诊;避免接触可能过敏原;不用地\n[BBOX-131] 毯,不养动物\n[BBOX-132] 医师签\n[BBOX-133] 门诊病历专用\n[BBOX-134] ※提醒:复诊时,请携带本病历记录,谢谢!※\n[BBOX-135] CS 扫描全能王\n[BBOX-136] 3亿人都在用的扫描App\n[BBOX-137] 门诊病历\n[BBOX-138] 科室:呼吸与危重症医学科\n[BBOX-139] 姓\n[BBOX-140] 性别:女\n[BBOX-141] 门诊\n[BBOX-142] 联系方\n[BBOX-143] 年龄:62岁\n[BBOX-144] 婚姻状况:其他\n[BBOX-145] 2024-03-21 08:40 初诊记录\n[BBOX-146] 主诉:SHR-1905-201 试验复筛\n[BBOX-147] 现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年\n[BBOX-148] 余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现\n[BBOX-149] 气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行\n[BBOX-150] 听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并\n[BBOX-151] 规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可\n[BBOX-152] 320ug bid,近日活动后气促再发,否认喘鸣音。无发热、胸痛。\n[BBOX-153] 2024.01.10参加SHR-1905-201临床试验,因白细胞计数<3.0*10^9/L符\n[BBOX-154] 合排除标准第12条筛败,于2024.03.01血液科就诊,无特殊处理,\n[BBOX-155] 2024.03.06进行SHR-1905-201试验二次知情。受试者今日返院完成V3\n[BBOX-156] 访视。\n[BBOX-157] 既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。\n[BBOX-158] 既往病史:\n[BBOX-159] 1.2022.12.10肝囊肿,持续;\n[BBOX-160] 2.2023.10.31鼻窦炎,持续;\n[BBOX-161] 3.2023.10.31双肺良性小结节,持续;\n[BBOX-162] 4.2023.11.03-2023.12.13,肺肺部感染;\n[BBOX-163] 5.2024.03.01开始,白细胞数降低1级;\n[BBOX-164] 6.2024.01.10开始,高脂蛋白a血症,\n[BBOX-165] 过敏史:否认食物、药物过敏史。\n[BBOX-166] 体格检查收缩压(mmHg):113;舒张压(mmHg):76\n[BBOX-167] 其他体格检查:09:37进行生命体征测量:体温:36.5℃,血压:\n[BBOX-168] 113/76mmHg,呼吸:18次/分,脉搏:98次/分;\n[BBOX-169] 查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见\n[BBOX-170] 第1页\n[BBOX-171] 科室:呼吸与危重症医学科\n[BBOX-172] 姓名\n[BBOX-173] 性别:女\n[BBOX-174] 门诊\n[BBOX-175] 联系方\n[BBOX-176] 年龄:62岁\n[BBOX-177] 婚姻状况:其他\n[BBOX-178] 2024-03-21 08:40 初诊记录\n[BBOX-179] 皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅\n[BBOX-180] 大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。\n[BBOX-181] 耳廓正常无畸形,外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无\n[BBOX-182] 鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿\n[BBOX-183] 大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中\n[BBOX-184] 肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动\n[BBOX-185] 正常,双肺呼吸音粗,未闻及干湿罗音。心律齐。双下肢无水肿。心音正\n[BBOX-186] 常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛、反跳痛,无液\n[BBOX-187] 波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触及,肾脏未触\n[BBOX-188] 及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖器未查、肛门\n[BBOX-189] 直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无异常,其他无\n[BBOX-190] 异常。.\n[BBOX-191] 检验检查:无\n[BBOX-192] 初步诊断:支气管哮喘\n[BBOX-193] 处理:\n[BBOX-194] CM 跟踪:\n[BBOX-195] 1、布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,\n[BBOX-196] 320ug,bid,经口腔吸入,用于控制哮喘。\n[BBOX-197] 处理:\n[BBOX-198] 1、2024.03.14-2024.03.21 家用峰流速仪使用 ePRO 系统填写依从性\n[BBOX-199] 7/7*100%=100%,嘱托患者按照自己实际情况及时填写日志,如有问题\n[BBOX-200] 随时沟通。\n[BBOX-201] 2、无新增 AE,CM,无临床试验安全性事件。\n[BBOX-202] 3、今日回收硫酸沙丁胺醇吸入气雾剂,发放新的硫酸沙丁胺醇吸入气\n[BBOX-203] 雾剂1盒,并嘱托受试者正确保存和使用。\n[BBOX-204] 4、绝经期女性,未做血、尿妊娠检查。\n[BBOX-205] 第2页\n[BBOX-206] CS 扫描全能王\n[BBOX-207] 3亿人都在用的扫描App\n[BBOX-208] 科室:呼吸与危重症医学科\n[BBOX-209] 门诊\n[BBOX-210] 姓名\n[BBOX-211] 联系方式\n[BBOX-212] 性别:女\n[BBOX-213] 年龄:62岁\n[BBOX-214] 婚姻状况:其他\n[BBOX-215] 2024-03-21 08:40 初诊记录\n[BBOX-216] 5、受试者所有检查结果经再次核对入排,符合所有入选标准,不符合任\n[BBOX-217] 一排除标准,可随机入组,分配随机号:_,随机分层信息:中剂量\n[BBOX-218] ICS,嗜酸性粒细胞计数<300/ul,未联合使用LAMA。\n[BBOX-219] 6、嘱托受试者2024.03.22来院行V4随访。\n[BBOX-220] 医师签\n[BBOX-221] 门诊病历专用章\n[BBOX-222] ※提醒:复诊时,请携带本病历记录,谢谢!※\n[BBOX-223] 第3页\n[BBOX-224] CS 扫描全能王\n[BBOX-225] 3亿人都在用的扫描App\n[BBOX-226] 科室:呼吸与危重症医学科\n[BBOX-227] 门诊\n[BBOX-228] 姓名\n[BBOX-229] 联系\n[BBOX-230] 性别:女\n[BBOX-231] 年龄:63岁\n[BBOX-232] 婚姻状况:其他\n[BBOX-233] 2024-12-12 09:40 初诊记录\n[BBOX-234] 主诉:SHR-1905-201 临床试验 V14\n[BBOX-235] 现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年\n[BBOX-236] 余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现\n[BBOX-237] 气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行\n[BBOX-238] 听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并\n[BBOX-239] 规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可\n[BBOX-240] 320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:\n[BBOX-241] 近日咳嗽咳痰,低烧两天,呼吸道感染。2024.12.02行V14随访\n[BBOX-242] 因患者发热延迟用药。今日回院用药,留院观察1h。\n[BBOX-243] 既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。\n[BBOX-244] 既往病史:\n[BBOX-245] 1.2022.12.10肝囊肿,持续;\n[BBOX-246] 2.2023.10.31鼻窦炎,持续;\n[BBOX-247] 3.2023.10.31双肺良性小结节,持续;\n[BBOX-248] 4.2023.11.03-2023.12.13,肺肺部感染;\n[BBOX-249] 5.2024.03.01开始,白细胞数降低1级,持续;\n[BBOX-250] 6.2024.01.10开始,高脂血症,持续;\n[BBOX-251] 7.十余年前,慢性浅表胃炎,持续中。\n[BBOX-252] 过敏史:否认食物、药物过敏史。\n[BBOX-253] 体格检查收缩压(mmHg):-;舒张压(mmHg):-\n[BBOX-254] 其他体格检查:未行\n[BBOX-255] 检验检查:无\n[BBOX-256] 初步诊断:支气管哮喘\n[BBOX-257] 处理:检查:心脏电生理:心电图(十二导联心电图);\n[BBOX-258] 检验:急诊血常规(五分类)+急诊超敏C反应蛋白、急诊肝功能五项\n[BBOX-259] 治疗:静脉采血\n[BBOX-260] 第1页\n[BBOX-261] 科室:呼吸与危重症医学科\n[BBOX-262] 性别:女\n[BBOX-263] 年龄:63岁\n[BBOX-264] 婚姻状况:其他\n[BBOX-265] 2024-12-12 09:40 初诊记录\n[BBOX-266] 无新增 AE,无新增 CM,无临床试验安全性事件。\n[BBOX-267] 呼吸道感染,2024.1127-2024.12.11,中度,与试验药物关系为可能无关\n[BBOX-268] 对试验药物采取的措施为延迟用药,对 AE 采取的措施为药物治疗,肺\n[BBOX-269] SAE,非 SIE,不因此退出临床试验。\n[BBOX-270] 跟踪 CM:\n[BBOX-271] 1.盐酸莫西沙片,2024.12.02-2024.12.11,持续中,0.4g/片,1片/次,\n[BBOX-272] qd,po,用于治疗 AE 呼吸道感染。\n[BBOX-273] 2.桉柠蒎肠溶胶囊,2024.12.02-2024.12.11 持续中,0.3g/粒,1粒/次,\n[BBOX-274] tid,po,用于治疗 AE 呼吸道感染。(化痰)\n[BBOX-275] 3.氯苯那敏片,2024.12.02-2024.12.11,持续中,4mg/片,1片/次,\n[BBOX-276] qn,po,用于治疗 AE 呼吸道感染。\n[BBOX-277] 4.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po.用于治\n[BBOX-278] 疗病史慢性浅表胃炎。\n[BBOX-279] 5.复方氨酚烷胺胶囊,2024.11.27-2024.12.02,持续中,0.25g:0.1g,1粒\n[BBOX-280] /次,bid,po,用于治疗 AE 呼吸道感染。\n[BBOX-281] 6.吸入沙丁胺醇气雾剂,2024.12.02-2024.12.02,400ug,吸入,once,用于支\n[BBOX-282] 气管扩张检查。\n[BBOX-283] CM 跟踪:\n[BBOX-284] 1、布地奈德福莫特罗粉吸入剂,2022.1127 开始,持续使用,\n[BBOX-285] 320ug,bid,经口腔吸入,用于控制哮喘。\n[BBOX-286] 2、硫酸沙丁胺醇气雾剂,2024.03.06 开始,持续中,100ug,pm,经口腔吸\n[BBOX-287] 入,控制哮喘急性发作。\n[BBOX-288] 第2页\n[BBOX-289] 门诊病历\n[BBOX-290] 科室:呼吸与危重症医学科\n[BBOX-291] 姓名:\n[BBOX-292] 性别:女\n[BBOX-293] 门诊号\n[BBOX-294] 联系方式\n[BBOX-295] 年龄:63岁\n[BBOX-296] 婚姻状况:其他\n[BBOX-297] 2024-12-12 09:40 初诊记录\n[BBOX-298] 处理:\n[BBOX-299] 患者于今日12:21-12:28完成临床试验药物的注射，药物编号为\n[BBOX-300] Y6077Y4950 用药前完善必要检查后随机用药。\n[BBOX-301] 医师\n[BBOX-302] 门诊病历\n[BBOX-303] ※提醒:复诊时,请携带本病历记录,谢谢!※\n[BBOX-304] “若有高血压糖尿病诊断,建议您到居住地附近社康中心,建立居民健康档案”\n[BBOX-305] 门诊病历\n[BBOX-306] 科室:呼吸与危重症医学科\n[BBOX-307] 姓名\n[BBOX-308] 性别:女\n[BBOX-309] 门诊\n[BBOX-310] 联系方式\n[BBOX-311] 年龄:63岁\n[BBOX-312] 婚姻状况:其他\n[BBOX-313] 2025-07-31 17:13 初诊记录\n[BBOX-314] 主诉:SHR-1905V19随访\n[BBOX-315] 现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年\n[BBOX-316] 余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现\n[BBOX-317] 气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行\n[BBOX-318] 听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并\n[BBOX-319] 规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可\n[BBOX-320] 320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:\n[BBOX-321] 20036.。近日无咳嗽咳痰,无胸闷气喘,无发热,无支气管哮喘急性发作\n[BBOX-322] 今日回院行V19随访。\n[BBOX-323] 既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。\n[BBOX-324] 既往病史:\n[BBOX-325] 1.2022.12.10肝囊肿,持续;\n[BBOX-326] 2.2023.10.31鼻窦炎,持续;\n[BBOX-327] 3.2023.10.31双肺良性小结节,持续;\n[BBOX-328] 4.2023.11.03-2023.12.13,肺肺部感染;\n[BBOX-329] 5.2024.03.01开始,白细胞数降低1级,持续;\n[BBOX-330] 6.2024.01.10高脂血症,持续中\n[BBOX-331] 过敏史:否认食物、药物过敏史。\n[BBOX-332] 体格检查收缩压(mmHg):103;舒张压(mmHg):64\n[BBOX-333] 其他体格检查:进行生命体征测量:体温:36.4℃,血压:\n[BBOX-334] 103/64mmHg,呼吸:18次/分,脉搏:76次/分;\n[BBOX-335] 查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见\n[BBOX-336] 皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅\n[BBOX-337] 大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。\n[BBOX-338] 耳廓正常无畸形外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无\n[BBOX-339] 鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿\n[BBOX-340] 第1页\n[BBOX-341] CS 扫描全能王\n[BBOX-342] 3亿人都在用的扫描App\n[BBOX-343] 门诊病历\n[BBOX-344] 科室:呼吸与危重症医学科\n[BBOX-345] 性别:女\n[BBOX-346] 门诊\n[BBOX-347] 联系方式:\n[BBOX-348] 年龄:63岁\n[BBOX-349] 婚姻状况:其他\n[BBOX-350] 2025-07-31 17:13 初诊记录\n[BBOX-351] 大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中\n[BBOX-352] 肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动\n[BBOX-353] 正常,左肺呼吸音清,未闻及粗干啰音。心律齐。双下肢无水肿。心音正\n[BBOX-354] 常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛、反跳痛,无液\n[BBOX-355] 波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触及,肾脏未触\n[BBOX-356] 及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖器未查、肛门\n[BBOX-357] 直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无异常,其他无\n[BBOX-358] 异常。\n[BBOX-359] 检验检查:已完善试验相关检验检查\n[BBOX-360] 初步诊断:支气管哮喘\n[BBOX-361] 处理:尿常规检查尿隐血,建议定期检查,必要时肾内科就诊。\n[BBOX-362] 无临床试验安全性事,无新增 AE。\n[BBOX-363] 新增合并用药:硫酸沙丁胺醇吸入气雾剂,2025.07.31-\n[BBOX-364] 2025.078.31,400ug,once,吸入,用于支气管扩张检查。\n[BBOX-365] CM 跟踪:\n[BBOX-366] 1、布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,\n[BBOX-367] 320ug,bid,经口腔吸入,用于控制哮喘。\n[BBOX-368] 2、硫酸沙丁胺醇气雾剂,2024.03.06开始,持续中,100ug,pm,经口腔吸\n[BBOX-369] 入,控制哮喘急性发作。\n[BBOX-370] 3.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po.用于治\n[BBOX-371] 疗病史慢性浅表胃炎。\n[BBOX-372] 处理:\n[BBOX-373] 12025.05.13-2025.07.31 家用峰流速仪使用 ePRO 系统填写依从性大于\n[BBOX-374] 80%,今日已解绑 ePRO 系统。\n[BBOX-375] 2遵从临床试验方案完成 IgE,PK,ADA 采血,完成 ACQ-6,AQLQ 问卷填\n[BBOX-376] 写。\n[BBOX-377] CS 扫描全能王\n[BBOX-378] 3亿人都在用的扫描App\n[BBOX-379] 门诊病历\n[BBOX-380] 科室:呼吸与危重症医学科\n[BBOX-381] 姓名\n[BBOX-382] 性别:女\n[BBOX-383] 门诊\n[BBOX-384] 联系\n[BBOX-385] 年龄:63岁\n[BBOX-386] 婚姻状况:其他\n[BBOX-387] 2025-07-31 17:13 初诊记录\n[BBOX-388] 3.患者于今日肺功能检查前已停用基础吸入药物布地奈德福莫特罗粉\n[BBOX-389] 吸入剂大于12h,停药时间2025.07.30上午,具体时间不详。\n[BBOX-390] 4.患者已于今日完成随访期随访。\n[BBOX-391] 5.因患者未找到发放万托林,可能已经丢失故不予回收。\n[BBOX-392] 6.嘱患者规律使用吸入药物布地奈德福莫特罗粉吸入剂,药物自备。\n[BBOX-393] 医师\n[BBOX-394] 门诊病历专用章\n[BBOX-395] ※提醒:复诊时,请携带本病历记录,谢谢!※\n[BBOX-396] “若有高血压糖尿病诊断,建议您到居住地附近社康中心,建立居民健康档案”\n[BBOX-397] 第3页\n[BBOX-398] 门诊\n[BBOX-399] 姓名：\n[BBOX-400] 门(急)诊初诊病历\n[BBOX-401] 性别：女\n[BBOX-402] 科室：呼吸内科门诊\n[BBOX-403] 年龄：63岁\n[BBOX-404] 就诊日期：2025-10-25 15:22\n[BBOX-405] 主诉：支气管哮喘复诊\n[BBOX-406] 现病史：患者支气管哮喘复诊，目前规律吸入布地奈德福莫特罗320ug 一次1吸，\n[BBOX-407] 一天2次。目前诉有咳嗽、咳痰，有气促感，无胸闷，无发热，无鼻塞、流涕，无咯\n[BBOX-408] 血、痰中带血，无头痛、头晕、视物旋转，无饮水呛咳，无咽痛、腹痛、腹胀等不\n[BBOX-409] 适。未予处理及就医。现患者为求进一步诊治，故至我院科门诊就医。\n[BBOX-410] 既往史：否认高血压、否认糖尿病、否认冠心病等慢性疾病病史，否认肝炎、结核\n[BBOX-411] 等传染病史，否认手术外伤输血史 过敏史：无食物、药物过敏史。。否认饮酒史。\n[BBOX-412] 个人史：已婚已育\n[BBOX-413] 家族史：否认家族病史。\n[BBOX-414] 体格检查：T：36.8℃ P：87次/分 R：21次/分 BP：108/73mmHg 指脉氧：\n[BBOX-415] 9%。神志清楚，精神尚可，呼吸平顺，口唇无发绀，咽部无充血，扁桃体无肿大，\n[BBOX-416] 双侧颈静脉无怒张，双肺呼吸音粗，双肺可闻及干啰音，双肺未闻及湿性啰音及胸膜\n[BBOX-417] 摩擦音。心率87次/分，律齐，各瓣膜未闻及明显病理性杂音。腹部平软，全腹部无\n[BBOX-418] 玉痛，反跳痛，肠鸣音正常。四肢运动自如，双下肢无水肿。\n[BBOX-419] 辅助检查：患者自行购买布地奈德福莫特罗320ug 一次1吸，一天2次。\n[BBOX-420] 初步诊断：\n[BBOX-421] 西医诊断：1.支气管哮喘(急性发作期)\n[BBOX-422] 处理意见：\n[BBOX-423] 醋酸泼尼松片（国基）(5mg*100片) 20.000mg\n[BBOX-424] 1次/天 口服\n[BBOX-425] 12.00片\n[BBOX-426] 硫酸沙丁胺醇吸入气雾剂（省3、国基）(200揿：\n[BBOX-427] 100μg) 200.000μg\n[BBOX-428] 1次/天 吸入\n[BBOX-429] 1.00瓶\n[BBOX-430] 建议：建议患者结果回报后请及时至我科门诊复诊，若出现病情变化或病情加重\n[BBOX-431] 无好转等，请及时至急诊科门诊复诊。\n[BBOX-432] 温馨提示：1.请妥善保管好病历及各种检查检验报告单。\n[BBOX-433] 2.复诊时，请携带本病历记录，谢谢！\n[BBOX-434] 第1页(共1页)\n[BBOX-435] 广东省医疗门诊收费票据（电子）\n[BBOX-436] 广东省\n[BBOX-437] 财政部监制\n[BBOX-438] 票据代码：44060125\n[BBOX-439] 票据号码：9148002082\n[BBOX-440] 校验码：831306\n[BBOX-441] 开票日期：2025-10-25\n[BBOX-442] 项目名称\n[BBOX-443] 数量/单位\n[BBOX-444] 金额（元）\n[BBOX-445] 备注\n[BBOX-446] 项目名称\n[BBOX-447] 数量/单位\n[BBOX-448] 金额（元）\n[BBOX-449] 备注\n[BBOX-450] 西药费\n[BBOX-451] 1\n[BBOX-452] 13.05\n[BBOX-453] 以下是清单项\n[BBOX-454] 醋酸泼尼松片（国基）\n[BBOX-455] 12\n[BBOX-456] 0.50\n[BBOX-457] 硫酸沙丁胺醇吸入气雾剂（省3\n[BBOX-458] 1\n[BBOX-459] 12.55\n[BBOX-460] 、国基）\n[BBOX-461] 金额合计（大写）壹拾叁元零伍分\n[BBOX-462] (小写)13.05\n[BBOX-463] 业务流水号：SF10390911\n[BBOX-464] 门诊\n[BBOX-465] 就诊日期：20251025\n[BBOX-466] 其他信息\n[BBOX-467] 医疗机构类型：综合医院\n[BBOX-468] 医保类型：现金(自费)\n[BBOX-469] 医保编号：\n[BBOX-470] 性别：女\n[BBOX-471] 医保统筹基金支付：0.00\n[BBOX-472] 其他支付：0.00\n[BBOX-473] 个人账户支付：0.00\n[BBOX-474] 个人现金支付：13.05\n[BBOX-475] 个人自付：0.00\n[BBOX-476] 个人自费：13.05\n[BBOX-477] 政策性减免：\n[BBOX-478] 收款单位（章）深圳市龙岗区第人民医院\n[BBOX-479] 复核人：掌上医院\n[BBOX-480] 收款人：掌上医院\n[BBOX-481] 说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。\n[BBOX-482] 单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dzpj.czt.gd.gov.cn/billcheck查验本省财政电子票据。\n[BBOX-483] CS 扫描全能王\n[BBOX-484] 3 亿人都在用的扫描 App\n[BBOX-485] 电子发票(普通发票)\n[BBOX-486] 发票号码：25447000001429974977\n[BBOX-487] 开票日期：2025年11月05日\n[BBOX-488] 广东省税务局\n[BBOX-489] 购买方信息\n[BBOX-490] 名称：\n[BBOX-491] 统一社会信用代码/纳税人识别号：\n[BBOX-492] 销售方信息\n[BBOX-493] 名称：阿里健康大药房医药连锁有限公司\n[BBOX-494] 统一社会信用代码/纳税人识别号：91440101681325547Y\n[BBOX-495] 项目名称\n[BBOX-496] 规格型号\n[BBOX-497] 单位\n[BBOX-498] 数量\n[BBOX-499] 单价\n[BBOX-500] 金额\n[BBOX-501] 税率/征收率\n[BBOX-502] 税额\n[BBOX-503] *化学药品制剂*布地奈德\n[BBOX-504] 盒\n[BBOX-505] 3\n[BBOX-506] 176.70\n[BBOX-507] 530.09\n[BBOX-508] 13%\n[BBOX-509] 68.91\n[BBOX-510] 福莫特罗吸入粉雾剂\n[BBOX-511] 合计\n[BBOX-512] ￥530.09\n[BBOX-513] ￥68.91\n[BBOX-514] 价税合计（大写）\n[BBOX-515] 伍佰玖拾玖圆整\n[BBOX-516] (小写)￥599.00\n[BBOX-517] 备注\n[BBOX-518] 开票人：董茜玲\n[BBOX-519] CS 扫描全能王\n[BBOX-520] 3亿人都在用的扫描App\n[BBOX-521] 门诊号\n[BBOX-522] 姓名\n[BBOX-523] 科室:呼吸内科门诊\n[BBOX-524] 门(急)诊初诊病历\n[BBOX-525] 电话\n[BBOX-526] 性别:女\n[BBOX-527] 年龄:63岁\n[BBOX-528] 就诊日期:2025-11-24 15:01\n[BBOX-529] 主诉:支气管哮喘复诊\n[BBOX-530] 现病史:患者支气管哮喘复诊,目前规律吸入布地奈德福莫特罗320一次1吸,一天2次(患者自行网购药物),目前有咳嗽、咳痰,咳嗽时有气喘感。无胸闷,无发热,无鼻塞、流涕,无咯血、痰中带血,无头痛、头晕、视物旋转,无饮水呛咳,无咽痛、腹痛、腹胀等不适。未予处理及就医。现患者为求进一步诊治,故至我院科门诊就医。\n[BBOX-531] 既往史:否认高血压、否认糖尿病、否认冠心病等慢性疾病病史,否认肝炎、结核等传染病史,否认手术外伤输血史过敏史:无食物、药物过敏史。。否认饮酒史。\n[BBOX-532] 个人史:已婚已育\n[BBOX-533] 家族史:否认家族病史。\n[BBOX-534] 体格检查:T:36.8℃ P:87次/分 R:21次/分 BP:108/73mmHg 指脉氧:99%。神志清楚,精神尚可,呼吸平顺,口唇无发绀,咽部无充血,扁桃体无肿大,双侧颈静脉无怒张,双肺呼吸音粗,双肺可闻及散在干啰音,双肺未闻及湿性啰音及胸膜摩擦音。心率87次/分,律齐,各瓣膜未闻及明显病理性杂音。腹部平软,全腹部无压痛,反跳痛,肠鸣音正常。四肢运动自如,双下肢无水肿。\n[BBOX-535] 辅助检查:\n[BBOX-536] 初步诊断:\n[BBOX-537] 西医诊断:1.支气管哮喘(急性发作期)\n[BBOX-538] 处理意见:自备布地奈德福莫特罗320一次1吸,一天2次\n[BBOX-539] 醋酸泼尼松片(国基)(5mg*100片)10.000mg\n[BBOX-540] 1次/天 口服 6.00片\n[BBOX-541] 建议:建议患者结果回报后请及时至我科门诊复诊,若出现病情变化或病情加重无好转等,请及时至急诊科门诊复诊。\n[BBOX-542] 医生签名:\n[BBOX-543] 温馨提示:1.请妥善保管好病历及各种检查检验报告单。\n[BBOX-544] 2.复诊时,请携带本病历记录,谢谢!\n[BBOX-545] 第1页(共1页)\n[BBOX-546] 广东省医疗门诊收费票据（电子）\n[BBOX-547] 广东省\n[BBOX-548] 财政部监制\n[BBOX-549] 票据代码：44\n[BBOX-550] 票据号码：9148286284\n[BBOX-551] 校验码：89a81f\n[BBOX-552] 交款人\n[BBOX-553] 开票日期：2025-11-24\n[BBOX-554] 项目名称\n[BBOX-555] 数量/单位\n[BBOX-556] 金额（元）\n[BBOX-557] 备注\n[BBOX-558] 项目名称\n[BBOX-559] 数量/单位\n[BBOX-560] 金额（元）\n[BBOX-561] 备注\n[BBOX-562] 西药费\n[BBOX-563] 1\n[BBOX-564] 0.25\n[BBOX-565] 以下是清单项\n[BBOX-566] 醋酸泼尼松片（国基）\n[BBOX-567] 6\n[BBOX-568] 0.25\n[BBOX-569] 金额合计（大写）贰角伍分\n[BBOX-570] (小写)0.25\n[BBOX-571] 业务流水号：SF10481981\n[BBOX-572] 门\n[BBOX-573] 就诊日期：20251124\n[BBOX-574] 其他信息\n[BBOX-575] 医疗机构类型：综合医院\n[BBOX-576] 医保类型：现金(自费)\n[BBOX-577] 医保编号：\n[BBOX-578] 性别：女\n[BBOX-579] 医保统筹基金支付：0.00\n[BBOX-580] 其他支付：0.00\n[BBOX-581] 个人账户支付：0.00\n[BBOX-582] 个人现金支付：0.25\n[BBOX-583] 个人自付：0.00\n[BBOX-584] 个人自费：0.25\n[BBOX-585] 政策性减免：\n[BBOX-586] 收款单位（章）\n[BBOX-587] 人民医院\n[BBOX-588] 复核人：吴亮梅\n[BBOX-589] 收款人：吴亮梅\n[BBOX-590] 说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。\n[BBOX-591] 单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dipj.czt.gd.gov.cn/billcheck查验本省财政电子票据。\n[BBOX-592] CS 扫描全能王\n[BBOX-593] 3亿人都在用的扫描App\n[BBOX-594] 10:15\n[BBOX-595] 淘\n[BBOX-596] 交易成功\n[BBOX-597] 医药仁康堂医药专营店>\n[BBOX-598] 【信必可】布地奈德福莫特罗\n[BBOX-599] ¥213\n[BBOX-600] 放心买药\n[BBOX-601] 正品保障\n[BBOX-602] 1盒装\n[BBOX-603] 不支持7天无理由 假一赔四>\n[BBOX-604] x1\n[BBOX-605] 专业药师在线服务\n[BBOX-606] 上天猫放心买药\n[BBOX-607] 用药小贴士 1.哮喘。2.慢性阻塞性肺疾病(慢阻肺;...\n[BBOX-608] 申请售后\n[BBOX-609] 商品总价\n[BBOX-610] ¥213\n[BBOX-611] 运费(含服务费)\n[BBOX-612] ¥8\n[BBOX-613] 应付款\n[BBOX-614] ¥221^\n[BBOX-615] 订单信息 2026-01-20\n[BBOX-616] 收起^\n[BBOX-617] 订单编号\n[BBOX-618] 4501919772001020746\n[BBOX-619] 交易快照\n[BBOX-620] 发生交易争议时，可作为判断依据>\n[BBOX-621] 成交时间\n[BBOX-622] 2026-01-26 22:25:02\n[BBOX-623] 发货时间\n[BBOX-624] 2026-01-21 12:24:52\n[BBOX-625] 付款时间\n[BBOX-626] 2026-01-20 19:25:06\n[BBOX-627] 创建时间\n[BBOX-628] 2026-01-20 19:24:30\n[BBOX-629] 支付宝交易号\n[BBOX-630] 2026012022001134951454085519\n[BBOX-631] 天猫积分\n[BBOX-632] 获得106点积分>\n[BBOX-633] 客服\n[BBOX-634] 更多\n[BBOX-635] 查看处方\n[BBOX-636] 查看物流\n[BBOX-637] 评价\n[BBOX-638] 扫描全能王\n[BBOX-639] 扫描全能王\n[BBOX-640] 3亿人都在用的扫描App\n[BBOX-641] 电子发票(普通发票)\n[BBOX-642] 发票号码：26322000000914042776\n[BBOX-643] 开票日期：2026年02月02日\n[BBOX-644] 江苏省税务局\n[BBOX-645] 购买方信息\n[BBOX-646] 名称：\n[BBOX-647] 统一社会信用代码/纳税人识别号：\n[BBOX-648] 销售方信息\n[BBOX-649] 名称：阜宁仁康堂大药房有限公司\n[BBOX-650] 统一社会信用代码/纳税人识别号：91320923MAK1XP619R\n[BBOX-651] 项目名称\n[BBOX-652] 规格型号\n[BBOX-653] 单位\n[BBOX-654] 数量\n[BBOX-655] 单价\n[BBOX-656] 金额\n[BBOX-657] 税率/征收率\n[BBOX-658] 税额\n[BBOX-659] *生物化学药品*其他生物\n[BBOX-660] 化学药品\n[BBOX-661] 1\n[BBOX-662] 218.811881188119\n[BBOX-663] 218.81\n[BBOX-664] 1%\n[BBOX-665] 2.19\n[BBOX-666] 合计\n[BBOX-667] ¥218.81\n[BBOX-668] ¥2.19\n[BBOX-669] 价税合计（大写）\n[BBOX-670] 贰佰贰拾壹圆整\n[BBOX-671] (小写)¥221.00\n[BBOX-672] 备注\n[BBOX-673] 开票人：杨雪\n[BBOX-674] CS 扫描全能王\n[BBOX-675] 3亿人都在用的扫描App"
  }
]
2026-08-05 05:18:59,093 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:18:59,106 INFO     29 [SmartSplitter] SmartSplitter done: 11 chunks from 11 LLM segments (all bbox_id). Types: {'OutpatientRecord': 6, 'MedicationRecord': 5}
2026-08-05 05:18:59,116 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-05 05:18:59,116 INFO     29 [Trace] task=d7b98bb4 | doc=LZQ 64 哮喘 深圳二院.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "676 items", "markdown": "", "text": "", "name": "LZQ 64 哮喘 深圳二院.pdf", "output_format": "chunks", "chunks": "11 items, types={'OutpatientRecord': 6, 'MedicationRecord': 5}"}
2026-08-05 05:18:59,116 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-05 05:18:59,117 INFO     29 [ChunkRouter] Routed 11 chunks into 2 groups: {'chunks_Clinical': 6, 'chunks_Medication': 5}
2026-08-05 05:18:59,125 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-05 05:18:59,125 INFO     29 [Trace] task=d7b98bb4 | doc=LZQ 64 哮喘 深圳二院.pdf | ChunkRouter:Router | outputs={"html": "", "json": "676 items", "markdown": "", "text": "", "name": "LZQ 64 哮喘 深圳二院.pdf", "output_format": "chunks", "chunks": "11 items, types={'OutpatientRecord': 6, 'MedicationRecord': 5}", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Medication\": 5}"}
2026-08-05 05:18:59,125 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-05 05:18:59,129 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:18:59,129 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m05:18:59 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:18:59,130 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:19:00,051 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:19:00,057 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-05 05:19:00,057 INFO     29 [Trace] task=d7b98bb4 | doc=LZQ 64 哮喘 深圳二院.pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "676 items", "markdown": "", "text": "", "name": "LZQ 64 哮喘 深圳二院.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Medication\": 5}"}
2026-08-05 05:19:00,057 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-05 05:19:00,062 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:19:00,062 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m05:19:00 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:19:00,063 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:19:00,673 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:19:00,679 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-05 05:19:00,680 INFO     29 [Trace] task=d7b98bb4 | doc=LZQ 64 哮喘 深圳二院.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "676 items", "markdown": "", "text": "", "name": "LZQ 64 哮喘 深圳二院.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Medication\": 5}"}
2026-08-05 05:19:00,680 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-05 05:19:00,687 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:19:00,688 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 05:19:00,688 INFO     29 [qwen-vl-text] positions(135): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:19:00,688 INFO     29 [qwen-vl-text] page grouping: [0, 1, 2, 3], lines per page: [37, 35, 39, 24]
2026-08-05 05:19:00,939 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:19:01,165 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:19:01,438 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:19:01,644 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:19:01,647 INFO     29 [qwen-vl-text] LLM extraction start, text_len=2891
2026-08-05 05:19:01,647 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:19:01,648 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 134, \"encounter_dates\": [\"2024-01-10\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊病历\n科室:呼吸与危重症医学科\n门\n联系人\n性别:女\n年龄:62岁\n婚姻状况:其他\n2024-01-10 10:27 初诊记录\n主诉:发作性喘息12年余\n现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年\n余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现\n气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行\n听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并\n规律使用信必可320ug bid后症状缓解。近日活动后气促再发,否认喘\n鸣音。无发热、胸痛。\n既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。\n既往病史:\n1.2022.12.10肝囊肿,持续;\n2.2023.10.31鼻窦炎,持续;\n3.2023.10.31双肺良性小结节,持续;\n4.2023.11.03-2023.12.13,肺肺部感染;\n一年内支气管哮喘急性发作病史:\n12023.11.03-2023.11.08,支气管哮喘急性发作,8mg、4mg甲泼尼龙qd\n各服用3天;\n22023.12.13-2023.12.15,支气管哮喘急性发作,4mg甲泼尼龙片qd,服用\n3天。\n一年内合并用药:\n1.左氧氟沙星片,2023.11.03-2023.12.01,0.5g,qd,po,用于治疗肺部感染\n2.甲泼尼龙片,2023.11.03-2023.11.05,8mg,qd,po,用于治疗支气管哮喘急\n性发作。\n3.甲泼尼龙片,2023.11.06-2023.11.08,4mg,qd,po,用于治疗支气管哮喘急\n性发作。\n4.孟鲁司特钠片,2023.11.03-2023.11.12,10mg,qn,po,用于治疗支气管哮喘\n急性发作。\n第1页\nCS 扫描全能王\n3亿人都在用的扫描App\n门诊病历\n科室:呼吸与危重症医学科\n姓名\n性别:女\n联系方式\n年龄:62岁\n婚姻状况:其他\n2024-01-10 10:27 初诊记录\n5.桉柠蒎肠溶软胶囊,2023.11.03-2023.11.15,0.3g,tid,po,用于治疗肺部感\n染。\n7.甲泼尼龙片,2023.12.13-2023.12.15,4mg,qd,po,用于治疗支气管哮喘急\n性发作。\n8.布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,\n320ug,bid,经口腔吸入,用于控制哮喘。\n过敏史:否认食物、药物过敏史。\n体格检查 收缩压（mmHg）:107;舒张压（mmHg）:75\n其他体格检查:身高:153cm,体重:48.5kg,\n09:50进行生命体征测量:体温:36.4℃,血压:107/75mmHg,呼吸:19\n次/分,脉搏:78次/分;\n查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见\n皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅\n大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。\n耳廓正常无畸形,外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无\n鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿\n大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中\n肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动\n正常,双肺呼吸音粗,未闻及干湿罗音。心律齐。双下肢无水肿。心率\n78次/分,心音正常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛\n反跳痛,无液波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触\n及,肾脏未触及,Murphy征阴性,移动性浊音阴性,肠鸣音正常。外生殖\n器未查、肛门直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无\n异常,其他无异常。.\n第2页\nCS 扫描全能王\n3亿人都在用的扫描App\n科室:呼吸与危重症医学科\n姓名:\n性别:女\n门诊\n联系方式\n596\n年龄:62岁\n婚姻状况:其他\n2024-01-10 10:27 初诊记录\n检验检查:阅片见双肺轻度支气管扩张,未见明显急性炎症病灶,余肺基本同前\n(正式报告为准)\n初步诊断:1.鼻窦炎;2.支气管哮喘;\n处理:药品:\n(省采3)硫酸沙丁胺醇吸入气雾剂200揿(100μg/揿)/瓶(1【瓶】) sig:\n(200【揿】)吸入pm(需要时);\n检查:心脏电生理:心电图(十二导联心电图);CT检查:副鼻窦平扫;\n使用螺旋扫描加收;普放:DR胸部正侧位片*(2);呼吸专科检查:支气管\n舒张试验、流速容量曲线;\n检验:凝血四项、肾功能六项+肝功能八项+血脂六项*+电解质六项+空\n腹血糖(门诊使用)+肝酶学补充7项+心肌损伤六项、血常规5分类、尿\n常规加化学分析、感染八项\n治疗:静脉采血\n根据患者病情,认为患者基本符合“评价SHR-1905注射液在重度未\n控制哮喘患者中的有效性及安全性-多中心、随机、双盲、安慰剂对照\n平行设计II期临床研究(SHR-1905-201)”的筛选要求,2024.01.10 09:15\n生向患者__及其家属详细介绍该试验目的、试验设计、受试\n者风险及受益、受试者义务及研究者义务等。根据方案(版本号:2.0,\n版本日期:2022年8月31日)要求,筛选期所有受试者均进行吸入支气\n管扩张剂前后肺功能检查,若受试者无法提供筛选前一年内气道可逆\n性检测报告(吸入沙丁胺醇后FEV1增加≥12%且FEV1绝对值增加≥\n200mL),则筛选期肺功能检查需要满足吸入沙丁胺醇后FEV1增加≥\n12%且FEV1绝对值增加≥200mL。符合要求后才可以入组,受试者表\n示同意。患者.__及其家属表示已充分了解以上告知内容,同意参加\n该临床试验,\n医生与患者__于2024.01.10 09:47同时签署了知\n情同意书(版本号:2.0,版本日期:2022年08月31日),一式两份,一份\n第3页\nCS 扫描全能王\n3亿人都在用的扫描App\n门诊病历\n科室:呼吸与危重症医学科\n姓名:\n性别:女\n门诊\n联系方式\n年龄:62岁\n婚姻状况:其他\n2024-01-10 10:27 初诊记录\n交给患者保存,一份保存在研究中心。签署知情同意书后患者进入筛选\n流程,受试者筛选号为CN..\n新增AE:\n1.高尿酸血症,2024.01.10开始,轻度,持续,与研究药物肯定无关,对研\n究药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。\n2.高脂血症,2024.01.10开始,轻度,持续,与研究药物肯定无关,对研究\n药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。\n3.白细胞计数降低,2024.01.10开始,轻度,持续,与研究药物肯定无关\n对研究药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。此项\n指标与患者临床症状不符,考虑让其一周内复测。\n规律使用吸入药物,用后漱口,定期复诊;避免接触可能过敏原;不用地\n毯,不养动物\n医师签\n门诊病历专用\n※提醒:复诊时,请携带本病历记录,谢谢!※",
    "role": "user"
  }
]
[92m05:19:01 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:19:01,650 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:19:06,240 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:19:06.239+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 16, "failed": 0, "current": {"d7b98bb4908c11f1a3da71efcdd7cc1f": {"id": "d7b98bb4908c11f1a3da71efcdd7cc1f", "doc_id": "d7626528908c11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479738, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785907001430, "task_type": "dataflow", "root_trace_id": "ea6d5499d1eb4a3cabaa8fb5a06c80f8", "root_traceparent": "00-ea6d5499d1eb4a3cabaa8fb5a06c80f8-0f37f835e898f31c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:19:12,267 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:19:12,267 INFO     29 [qwen-vl-text] LLM output (len=1368):
{
  "encounter_date": "2024-01-10",
  "chief_complaint": "发作性喘息12年余",
  "present_illness": "发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并规律使用信必可320ug bid后症状缓解。近日活动后气促再发,否认喘鸣音。无发热、胸痛。一年内支气管哮喘急性发作病史:1.2023.11.03-2023.11.08,支气管哮喘急性发作,8mg、4mg甲泼尼龙qd各服用3天;2.2023.12.13-2023.12.15,支气管哮喘急性发作,4mg甲泼尼龙片qd,服用3天。一年内合并用药:1.左氧氟沙星片,2023.11.03-2023.12.01,0.5g,qd,po,用于治疗肺部感染;2.甲泼尼龙片,2023.11.03-2023.11.05,8mg,qd,po,用于治疗支气管哮喘急性发作;3.甲泼尼龙片,2023.11.06-2023.11.08,4mg,qd,po,用于治疗支气管哮喘急性发作;4.孟鲁司特钠片,2023.11.03-2023.11.12,10mg,qn,po,用于治疗支气管哮喘急性发作;5.桉柠蒎肠溶软胶囊,2023.11.03-2023.11.15,0.3g,tid,po,用于治疗肺部感染;7.甲泼尼龙片,2023.12.13-2023.12.15,4mg,qd,po,用于治疗支气管哮喘急性发作;8.布地奈德福莫特罗粉吸入剂,2022.11.27开始,持续使用,320ug,bid,经口腔吸入,用于控制哮喘。",
  "past_history": "否认吸烟史、饮酒史。2015年绝经,1988年外院行结扎术。既往病史:1.2022.12.10肝囊肿,持续;2.2023.10.31鼻窦炎,持续;3.2023.10.31双肺良性小结节,持续;4.2023.11.03-2023.12.13,肺部感染。过敏史:否认食物、药物过敏史。",
  "diagnosis": "1.鼻窦炎;2.支气管哮喘",
  "treatment_plan": "药品:(省采3)硫酸沙丁胺醇吸入气雾剂200揿(100μg/揿)/瓶 1瓶 sig:200揿 吸入 pm(需要时)。检查:心脏电生理:心电图(十二导联心电图);CT检查:副鼻窦平扫(使用螺旋扫描加收);普放:DR胸部正侧位片*(2);呼吸专科检查:支气管舒张试验、流速容量曲线。检验:凝血四项、肾功能六项+肝功能八项+血脂六项+电解质六项+空腹血糖(门诊使用)+肝酶学补充7项+心肌损伤六项、血常规5分类、尿常规加化学分析、感染八项。治疗:静脉采血。临床试验:患者符合“评价SHR-1905注射液在重度未控制哮喘患者中的有效性及安全性-多中心、随机、双盲、安慰剂对照平行设计II期临床研究(SHR-1905-201)”筛选要求,签署知情同意书进入筛选流程。医嘱:规律使用吸入药物,用后漱口,定期复诊;避免接触可能过敏原;不用地毯,不养动物。"
}
2026-08-05 05:19:12,267 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-01-10]
2026-08-05 05:19:12,270 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1450843, prompt_len=1510
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共37行）
["门诊病历", "科室:呼吸与危重症医学科", "门", "联系人", "性别:女", "年龄:62岁", "婚姻状况:其他", "2024-01-10 10:27 初诊记录", "主诉:发作性喘息12年余", "现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年", "余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现", "气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行", "听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并", "规律使用信必可320ug bid后症状缓解。近日活动后气促再发,否认喘", "鸣音。无发热、胸痛。", "既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。", "既往病史:", "1.2022.12.10肝囊肿,持续;", "2.2023.10.31鼻窦炎,持续;", "3.2023.10.31双肺良性小结节,持续;", "4.2023.11.03-2023.12.13,肺肺部感染;", "一年内支气管哮喘急性发作病史:", "12023.11.03-2023.11.08,支气管哮喘急性发作,8mg、4mg甲泼尼龙qd", "各服用3天;", "22023.12.13-2023.12.15,支气管哮喘急性发作,4mg甲泼尼龙片qd,服用", "3天。", "一年内合并用药:", "1.左氧氟沙星片,2023.11.03-2023.12.01,0.5g,qd,po,用于治疗肺部感染", "2.甲泼尼龙片,2023.11.03-2023.11.05,8mg,qd,po,用于治疗支气管哮喘急", "性发作。", "3.甲泼尼龙片,2023.11.06-2023.11.08,4mg,qd,po,用于治疗支气管哮喘急", "性发作。", "4.孟鲁司特钠片,2023.11.03-2023.11.12,10mg,qn,po,用于治疗支气管哮喘", "急性发作。", "第1页", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-05 05:19:27,835 INFO     29 [qwen-vl-text] coord API raw response (len=2409):
[
	{"text": "门诊病历", "bbox": [420, 20, 590, 42]},
	{"text": "科室:呼吸与危重症医学科", "bbox": [104, 51, 338, 67]},
	{"text": "门", "bbox": [512, 51, 531, 67]},
	{"text": "联系人", "bbox": [512, 78, 566, 94]},
	{"text": "性别:女", "bbox": [105, 105, 176, 121]},
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
	{"text": "1.左氧氟沙星片,2023.11.03-2023.12.01,0.5g,qd,po,用于治疗肺部感染", "bbox": [203, 648, 910, 667]},
	{"text": "2.甲泼尼龙片,2023.11.03-2023.11.05,8mg,qd,po,用于治疗支气管哮喘急", "bbox": [203, 673, 909, 692]},
	{"text": "性发作。", "bbox": [203, 698, 285, 716]},
	{"text": "3.甲泼尼龙片,2023.11.06-2023.11.08,4mg,qd,po,用于治疗支气管哮喘急", "bbox": [203, 723, 909, 742]},
	{"text": "性发作。", "bbox": [203, 748, 285, 766]},
	{"text": "4.孟鲁司特钠片,2023.11.03-2023.11.12,10mg,qn,po,用于治疗支气管哮喘", "bbox": [203, 773, 909, 792]},
	{"text": "急性发作。", "bbox": [203, 798, 308, 817]},
	{"text": "第1页", "bbox": [475, 831, 540, 849]},
	{"text": "CS 扫描全能王", "bbox": [861, 958, 977, 974]},
	{"text": "3亿人都在用的扫描App", "bbox": [861, 977, 976, 987]}
]
2026-08-05 05:19:27,835 INFO     29 [qwen-vl-text] coord API: raw_items=37, valid_items=37, elapsed=15.6s
2026-08-05 05:19:27,835 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[420, 20, 590, 42]
2026-08-05 05:19:27,836 INFO     29 [qwen-vl-text] coord item[1]: text=科室:呼吸与危重症医学科, bbox=[104, 51, 338, 67]
2026-08-05 05:19:27,836 INFO     29 [qwen-vl-text] coord item[2]: text=门, bbox=[512, 51, 531, 67]
2026-08-05 05:19:27,836 INFO     29 [qwen-vl-text] coord item[3]: text=联系人, bbox=[512, 78, 566, 94]
2026-08-05 05:19:27,836 INFO     29 [qwen-vl-text] coord item[4]: text=性别:女, bbox=[105, 105, 176, 121]
2026-08-05 05:19:27,836 INFO     29 [qwen-vl-text] coord item[5]: text=年龄:62岁, bbox=[512, 105, 603, 121]
2026-08-05 05:19:27,836 INFO     29 [qwen-vl-text] coord item[6]: text=婚姻状况:其他, bbox=[666, 105, 795, 121]
2026-08-05 05:19:27,836 INFO     29 [qwen-vl-text] coord item[7]: text=2024-01-10 10:27 初诊记录, bbox=[101, 149, 379, 166]
2026-08-05 05:19:27,836 INFO     29 [qwen-vl-text] coord item[8]: text=主诉:发作性喘息12年余, bbox=[101, 173, 400, 191]
2026-08-05 05:19:27,836 INFO     29 [qwen-vl-text] coord item[9]: text=现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年, bbox=[100, 198, 911, 217]
2026-08-05 05:19:27,836 INFO     29 [qwen-vl-text] coord item[10]: text=余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现, bbox=[203, 223, 911, 242]
2026-08-05 05:19:27,836 INFO     29 [qwen-vl-text] coord item[11]: text=气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行, bbox=[203, 248, 911, 267]
2026-08-05 05:19:27,836 INFO     29 [qwen-vl-text] coord item[12]: text=听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并, bbox=[203, 273, 911, 292]
2026-08-05 05:19:27,836 INFO     29 [qwen-vl-text] coord item[13]: text=规律使用信必可320ug bid后症状缓解。近日活动后气促再发,否认喘, bbox=[203, 298, 911, 317]
2026-08-05 05:19:27,836 INFO     29 [qwen-vl-text] coord item[14]: text=鸣音。无发热、胸痛。, bbox=[203, 323, 425, 342]
2026-08-05 05:19:27,836 INFO     29 [qwen-vl-text] coord item[15]: text=既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。, bbox=[104, 349, 863, 367]
2026-08-05 05:19:27,836 INFO     29 [qwen-vl-text] coord item[16]: text=既往病史:, bbox=[203, 374, 307, 392]
2026-08-05 05:19:27,836 INFO     29 [qwen-vl-text] coord item[17]: text=1.2022.12.10肝囊肿,持续;, bbox=[203, 399, 480, 417]
2026-08-05 05:19:27,836 INFO     29 [qwen-vl-text] coord item[18]: text=2.2023.10.31鼻窦炎,持续;, bbox=[203, 424, 480, 442]
2026-08-05 05:19:27,836 INFO     29 [qwen-vl-text] coord item[19]: text=3.2023.10.31双肺良性小结节,持续;, bbox=[203, 449, 572, 467]
2026-08-05 05:19:27,836 INFO     29 [qwen-vl-text] coord item[20]: text=4.2023.11.03-2023.12.13,肺肺部感染;, bbox=[203, 474, 585, 492]
2026-08-05 05:19:27,837 INFO     29 [qwen-vl-text] coord item[21]: text=一年内支气管哮喘急性发作病史:, bbox=[203, 499, 539, 517]
2026-08-05 05:19:27,837 INFO     29 [qwen-vl-text] coord item[22]: text=12023.11.03-2023.11.08,支气管哮喘急性发作,8mg、4mg甲泼尼龙qd, bbox=[203, 523, 911, 542]
2026-08-05 05:19:27,837 INFO     29 [qwen-vl-text] coord item[23]: text=各服用3天;, bbox=[203, 548, 328, 567]
2026-08-05 05:19:27,837 INFO     29 [qwen-vl-text] coord item[24]: text=22023.12.13-2023.12.15,支气管哮喘急性发作,4mg甲泼尼龙片qd,服用, bbox=[203, 573, 909, 592]
2026-08-05 05:19:27,837 INFO     29 [qwen-vl-text] coord item[25]: text=3天。, bbox=[203, 598, 255, 616]
2026-08-05 05:19:27,837 INFO     29 [qwen-vl-text] coord item[26]: text=一年内合并用药:, bbox=[203, 623, 377, 642]
2026-08-05 05:19:27,837 INFO     29 [qwen-vl-text] coord item[27]: text=1.左氧氟沙星片,2023.11.03-2023.12.01,0.5g,qd,po,用于治疗肺部感染, bbox=[203, 648, 910, 667]
2026-08-05 05:19:27,837 INFO     29 [qwen-vl-text] coord item[28]: text=2.甲泼尼龙片,2023.11.03-2023.11.05,8mg,qd,po,用于治疗支气管哮喘急, bbox=[203, 673, 909, 692]
2026-08-05 05:19:27,837 INFO     29 [qwen-vl-text] coord item[29]: text=性发作。, bbox=[203, 698, 285, 716]
2026-08-05 05:19:27,837 INFO     29 [qwen-vl-text] coord item[30]: text=3.甲泼尼龙片,2023.11.06-2023.11.08,4mg,qd,po,用于治疗支气管哮喘急, bbox=[203, 723, 909, 742]
2026-08-05 05:19:27,837 INFO     29 [qwen-vl-text] coord item[31]: text=性发作。, bbox=[203, 748, 285, 766]
2026-08-05 05:19:27,837 INFO     29 [qwen-vl-text] coord item[32]: text=4.孟鲁司特钠片,2023.11.03-2023.11.12,10mg,qn,po,用于治疗支气管哮喘, bbox=[203, 773, 909, 792]
2026-08-05 05:19:27,837 INFO     29 [qwen-vl-text] coord item[33]: text=急性发作。, bbox=[203, 798, 308, 817]
2026-08-05 05:19:27,837 INFO     29 [qwen-vl-text] coord item[34]: text=第1页, bbox=[475, 831, 540, 849]
2026-08-05 05:19:27,837 INFO     29 [qwen-vl-text] coord item[35]: text=CS 扫描全能王, bbox=[861, 958, 977, 974]
2026-08-05 05:19:27,837 INFO     29 [qwen-vl-text] coord item[36]: text=3亿人都在用的扫描App, bbox=[861, 977, 976, 987]
2026-08-05 05:19:27,837 INFO     29 [qwen-vl-text] page=0 — 37/37 coords, api_time=15.6s
2026-08-05 05:19:27,841 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1406002, prompt_len=1525
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共35行）
["门诊病历", "科室:呼吸与危重症医学科", "姓名", "性别:女", "联系方式", "年龄:62岁", "婚姻状况:其他", "2024-01-10 10:27 初诊记录", "5.桉柠蒎肠溶软胶囊,2023.11.03-2023.11.15,0.3g,tid,po,用于治疗肺部感", "染。", "7.甲泼尼龙片,2023.12.13-2023.12.15,4mg,qd,po,用于治疗支气管哮喘急", "性发作。", "8.布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,", "320ug,bid,经口腔吸入,用于控制哮喘。", "过敏史:否认食物、药物过敏史。", "体格检查 收缩压（mmHg）:107;舒张压（mmHg）:75", "其他体格检查:身高:153cm,体重:48.5kg,", "09:50进行生命体征测量:体温:36.4℃,血压:107/75mmHg,呼吸:19", "次/分,脉搏:78次/分;", "查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见", "皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅", "大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。", "耳廓正常无畸形,外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无", "鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿", "大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中", "肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动", "正常,双肺呼吸音粗,未闻及干湿罗音。心律齐。双下肢无水肿。心率", "78次/分,心音正常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛", "反跳痛,无液波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触", "及,肾脏未触及,Murphy征阴性,移动性浊音阴性,肠鸣音正常。外生殖", "器未查、肛门直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无", "异常,其他无异常。.", "第2页", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-05 05:19:40,114 INFO     29 [qwen-vl-text] coord API raw response (len=2343):
[
	{"text": "门诊病历", "bbox": [428, 18, 594, 35]},
	{"text": "科室:呼吸与危重症医学科", "bbox": [111, 44, 346, 61]},
	{"text": "姓名", "bbox": [111, 72, 154, 89]},
	{"text": "性别:女", "bbox": [111, 100, 184, 117]},
	{"text": "联系方式", "bbox": [518, 72, 597, 89]},
	{"text": "年龄:62岁", "bbox": [518, 100, 609, 117]},
	{"text": "婚姻状况:其他", "bbox": [670, 100, 796, 117]},
	{"text": "2024-01-10 10:27 初诊记录", "bbox": [109, 145, 389, 162]},
	{"text": "5.桉柠蒎肠溶软胶囊,2023.11.03-2023.11.15,0.3g,tid,po,用于治疗肺部感", "bbox": [212, 170, 911, 188]},
	{"text": "染。", "bbox": [212, 196, 247, 213]},
	{"text": "7.甲泼尼龙片,2023.12.13-2023.12.15,4mg,qd,po,用于治疗支气管哮喘急", "bbox": [212, 221, 910, 240]},
	{"text": "性发作。", "bbox": [212, 247, 295, 265]},
	{"text": "8.布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,", "bbox": [212, 272, 778, 290]},
	{"text": "320ug,bid,经口腔吸入,用于控制哮喘。", "bbox": [212, 298, 601, 317]},
	{"text": "过敏史:否认食物、药物过敏史。", "bbox": [114, 351, 460, 369]},
	{"text": "体格检查 收缩压（mmHg）:107;舒张压（mmHg）:75", "bbox": [114, 375, 656, 394]},
	{"text": "其他体格检查:身高:153cm,体重:48.5kg,", "bbox": [214, 400, 656, 419]},
	{"text": "09:50进行生命体征测量:体温:36.4℃,血压:107/75mmHg,呼吸:19", "bbox": [214, 425, 913, 444]},
	{"text": "次/分,脉搏:78次/分;", "bbox": [214, 451, 450, 469]},
	{"text": "查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见", "bbox": [214, 475, 911, 494]},
	{"text": "皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅", "bbox": [214, 500, 911, 519]},
	{"text": "大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。", "bbox": [214, 525, 900, 544]},
	{"text": "耳廓正常无畸形,外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无", "bbox": [214, 550, 911, 569]},
	{"text": "鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿", "bbox": [214, 575, 910, 594]},
	{"text": "大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中", "bbox": [214, 600, 910, 619]},
	{"text": "肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动", "bbox": [214, 625, 910, 644]},
	{"text": "正常,双肺呼吸音粗,未闻及干湿罗音。心律齐。双下肢无水肿。心率", "bbox": [214, 650, 910, 669]},
	{"text": "78次/分,心音正常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛", "bbox": [214, 675, 910, 694]},
	{"text": "反跳痛,无液波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触", "bbox": [214, 700, 910, 719]},
	{"text": "及,肾脏未触及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖", "bbox": [214, 725, 910, 744]},
	{"text": "器未查、肛门直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无", "bbox": [214, 750, 910, 769]},
	{"text": "异常,其他无异常。.", "bbox": [214, 776, 420, 794]},
	{"text": "第2页", "bbox": [485, 835, 548, 852]},
	{"text": "CS 扫描全能王", "bbox": [861, 958, 977, 974]},
	{"text": "3亿人都在用的扫描App", "bbox": [861, 977, 976, 986]}
]
2026-08-05 05:19:40,114 INFO     29 [qwen-vl-text] coord API: raw_items=35, valid_items=35, elapsed=12.3s
2026-08-05 05:19:40,115 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[428, 18, 594, 35]
2026-08-05 05:19:40,115 INFO     29 [qwen-vl-text] coord item[1]: text=科室:呼吸与危重症医学科, bbox=[111, 44, 346, 61]
2026-08-05 05:19:40,115 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[111, 72, 154, 89]
2026-08-05 05:19:40,115 INFO     29 [qwen-vl-text] coord item[3]: text=性别:女, bbox=[111, 100, 184, 117]
2026-08-05 05:19:40,115 INFO     29 [qwen-vl-text] coord item[4]: text=联系方式, bbox=[518, 72, 597, 89]
2026-08-05 05:19:40,115 INFO     29 [qwen-vl-text] coord item[5]: text=年龄:62岁, bbox=[518, 100, 609, 117]
2026-08-05 05:19:40,115 INFO     29 [qwen-vl-text] coord item[6]: text=婚姻状况:其他, bbox=[670, 100, 796, 117]
2026-08-05 05:19:40,115 INFO     29 [qwen-vl-text] coord item[7]: text=2024-01-10 10:27 初诊记录, bbox=[109, 145, 389, 162]
2026-08-05 05:19:40,115 INFO     29 [qwen-vl-text] coord item[8]: text=5.桉柠蒎肠溶软胶囊,2023.11.03-2023.11.15,0.3g,tid,po,用于治疗肺部感, bbox=[212, 170, 911, 188]
2026-08-05 05:19:40,115 INFO     29 [qwen-vl-text] coord item[9]: text=染。, bbox=[212, 196, 247, 213]
2026-08-05 05:19:40,115 INFO     29 [qwen-vl-text] coord item[10]: text=7.甲泼尼龙片,2023.12.13-2023.12.15,4mg,qd,po,用于治疗支气管哮喘急, bbox=[212, 221, 910, 240]
2026-08-05 05:19:40,116 INFO     29 [qwen-vl-text] coord item[11]: text=性发作。, bbox=[212, 247, 295, 265]
2026-08-05 05:19:40,116 INFO     29 [qwen-vl-text] coord item[12]: text=8.布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,, bbox=[212, 272, 778, 290]
2026-08-05 05:19:40,116 INFO     29 [qwen-vl-text] coord item[13]: text=320ug,bid,经口腔吸入,用于控制哮喘。, bbox=[212, 298, 601, 317]
2026-08-05 05:19:40,116 INFO     29 [qwen-vl-text] coord item[14]: text=过敏史:否认食物、药物过敏史。, bbox=[114, 351, 460, 369]
2026-08-05 05:19:40,116 INFO     29 [qwen-vl-text] coord item[15]: text=体格检查 收缩压（mmHg）:107;舒张压（mmHg）:75, bbox=[114, 375, 656, 394]
2026-08-05 05:19:40,116 INFO     29 [qwen-vl-text] coord item[16]: text=其他体格检查:身高:153cm,体重:48.5kg,, bbox=[214, 400, 656, 419]
2026-08-05 05:19:40,116 INFO     29 [qwen-vl-text] coord item[17]: text=09:50进行生命体征测量:体温:36.4℃,血压:107/75mmHg,呼吸:19, bbox=[214, 425, 913, 444]
2026-08-05 05:19:40,116 INFO     29 [qwen-vl-text] coord item[18]: text=次/分,脉搏:78次/分;, bbox=[214, 451, 450, 469]
2026-08-05 05:19:40,116 INFO     29 [qwen-vl-text] coord item[19]: text=查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见, bbox=[214, 475, 911, 494]
2026-08-05 05:19:40,116 INFO     29 [qwen-vl-text] coord item[20]: text=皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅, bbox=[214, 500, 911, 519]
2026-08-05 05:19:40,116 INFO     29 [qwen-vl-text] coord item[21]: text=大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。, bbox=[214, 525, 900, 544]
2026-08-05 05:19:40,116 INFO     29 [qwen-vl-text] coord item[22]: text=耳廓正常无畸形,外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无, bbox=[214, 550, 911, 569]
2026-08-05 05:19:40,116 INFO     29 [qwen-vl-text] coord item[23]: text=鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿, bbox=[214, 575, 910, 594]
2026-08-05 05:19:40,116 INFO     29 [qwen-vl-text] coord item[24]: text=大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中, bbox=[214, 600, 910, 619]
2026-08-05 05:19:40,116 INFO     29 [qwen-vl-text] coord item[25]: text=肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动, bbox=[214, 625, 910, 644]
2026-08-05 05:19:40,116 INFO     29 [qwen-vl-text] coord item[26]: text=正常,双肺呼吸音粗,未闻及干湿罗音。心律齐。双下肢无水肿。心率, bbox=[214, 650, 910, 669]
2026-08-05 05:19:40,116 INFO     29 [qwen-vl-text] coord item[27]: text=78次/分,心音正常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛, bbox=[214, 675, 910, 694]
2026-08-05 05:19:40,117 INFO     29 [qwen-vl-text] coord item[28]: text=反跳痛,无液波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触, bbox=[214, 700, 910, 719]
2026-08-05 05:19:40,117 INFO     29 [qwen-vl-text] coord item[29]: text=及,肾脏未触及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖, bbox=[214, 725, 910, 744]
2026-08-05 05:19:40,117 INFO     29 [qwen-vl-text] coord item[30]: text=器未查、肛门直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无, bbox=[214, 750, 910, 769]
2026-08-05 05:19:40,117 INFO     29 [qwen-vl-text] coord item[31]: text=异常,其他无异常。., bbox=[214, 776, 420, 794]
2026-08-05 05:19:40,117 INFO     29 [qwen-vl-text] coord item[32]: text=第2页, bbox=[485, 835, 548, 852]
2026-08-05 05:19:40,117 INFO     29 [qwen-vl-text] coord item[33]: text=CS 扫描全能王, bbox=[861, 958, 977, 974]
2026-08-05 05:19:40,117 INFO     29 [qwen-vl-text] coord item[34]: text=3亿人都在用的扫描App, bbox=[861, 977, 976, 986]
2026-08-05 05:19:40,117 INFO     29 [qwen-vl-text] page=1 — 35/35 coords, api_time=12.3s
2026-08-05 05:19:40,121 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1645213, prompt_len=1590
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共39行）
["科室:呼吸与危重症医学科", "姓名:", "性别:女", "门诊", "联系方式", "596", "年龄:62岁", "婚姻状况:其他", "2024-01-10 10:27 初诊记录", "检验检查:阅片见双肺轻度支气管扩张,未见明显急性炎症病灶,余肺基本同前", "(正式报告为准)", "初步诊断:1.鼻窦炎;2.支气管哮喘;", "处理:药品:", "(省采3)硫酸沙丁胺醇吸入气雾剂200揿(100μg/揿)/瓶(1【瓶】) sig:", "(200【揿】)吸入pm(需要时);", "检查:心脏电生理:心电图(十二导联心电图);CT检查:副鼻窦平扫;", "使用螺旋扫描加收;普放:DR胸部正侧位片*(2);呼吸专科检查:支气管", "舒张试验、流速容量曲线;", "检验:凝血四项、肾功能六项+肝功能八项+血脂六项*+电解质六项+空", "腹血糖(门诊使用)+肝酶学补充7项+心肌损伤六项、血常规5分类、尿", "常规加化学分析、感染八项", "治疗:静脉采血", "根据患者病情,认为患者基本符合“评价SHR-1905注射液在重度未", "控制哮喘患者中的有效性及安全性-多中心、随机、双盲、安慰剂对照", "平行设计II期临床研究(SHR-1905-201)”的筛选要求,2024.01.10 09:15", "生向患者__及其家属详细介绍该试验目的、试验设计、受试", "者风险及受益、受试者义务及研究者义务等。根据方案(版本号:2.0,", "版本日期:2022年8月31日)要求,筛选期所有受试者均进行吸入支气", "管扩张剂前后肺功能检查,若受试者无法提供筛选前一年内气道可逆", "性检测报告(吸入沙丁胺醇后FEV1增加≥12%且FEV1绝对值增加≥", "200mL),则筛选期肺功能检查需要满足吸入沙丁胺醇后FEV1增加≥", "12%且FEV1绝对值增加≥200mL。符合要求后才可以入组,受试者表", "示同意。患者.__及其家属表示已充分了解以上告知内容,同意参加", "该临床试验,", "医生与患者__于2024.01.10 09:47同时签署了知", "情同意书(版本号:2.0,版本日期:2022年08月31日),一式两份,一份", "第3页", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-05 05:19:55,955 INFO     29 [qwen-vl-text] coord API raw response (len=2559):
[
	{"text": "科室:呼吸与危重症医学科", "bbox": [88, 35, 327, 53]},
	{"text": "姓名:", "bbox": [88, 64, 114, 82]},
	{"text": "性别:女", "bbox": [88, 92, 161, 109]},
	{"text": "门诊", "bbox": [503, 35, 568, 53]},
	{"text": "联系方式", "bbox": [503, 64, 585, 81]},
	{"text": "596", "bbox": [670, 69, 704, 80]},
	{"text": "年龄:62岁", "bbox": [503, 92, 596, 109]},
	{"text": "婚姻状况:其他", "bbox": [659, 92, 788, 109]},
	{"text": "2024-01-10 10:27 初诊记录", "bbox": [84, 137, 368, 155]},
	{"text": "检验检查:阅片见双肺轻度支气管扩张,未见明显急性炎症病灶,余肺基本同前", "bbox": [84, 163, 882, 181]},
	{"text": "(正式报告为准)", "bbox": [199, 189, 367, 207]},
	{"text": "初步诊断:1.鼻窦炎;2.支气管哮喘;", "bbox": [84, 215, 446, 234]},
	{"text": "处理:药品:", "bbox": [84, 242, 243, 260]},
	{"text": "(省采3)硫酸沙丁胺醇吸入气雾剂200揿(100μg/揿)/瓶(1【瓶】) sig:", "bbox": [192, 268, 906, 287]},
	{"text": "(200【揿】)吸入pm(需要时);", "bbox": [189, 294, 546, 313]},
	{"text": "检查:心脏电生理:心电图(十二导联心电图);CT检查:副鼻窦平扫;", "bbox": [189, 320, 890, 338]},
	{"text": "使用螺旋扫描加收;普放:DR胸部正侧位片*(2);呼吸专科检查:支气管", "bbox": [189, 346, 905, 364]},
	{"text": "舒张试验、流速容量曲线;", "bbox": [189, 372, 460, 390]},
	{"text": "检验:凝血四项、肾功能六项+肝功能八项+血脂六项*+电解质六项+空", "bbox": [189, 398, 900, 416]},
	{"text": "腹血糖(门诊使用)+肝酶学补充7项+心肌损伤六项、血常规5分类、尿", "bbox": [189, 424, 904, 442]},
	{"text": "常规加化学分析、感染八项", "bbox": [189, 450, 474, 468]},
	{"text": "治疗:静脉采血", "bbox": [189, 475, 338, 493]},
	{"text": "根据患者病情,认为患者基本符合“评价SHR-1905注射液在重度未", "bbox": [187, 500, 904, 519]},
	{"text": "控制哮喘患者中的有效性及安全性-多中心、随机、双盲、安慰剂对照", "bbox": [187, 526, 904, 544]},
	{"text": "平行设计II期临床研究(SHR-1905-201)”的筛选要求,2024.01.10 09:15", "bbox": [187, 552, 904, 570]},
	{"text": "生向患者__及其家属详细介绍该试验目的、试验设计、受试", "bbox": [238, 577, 904, 596]},
	{"text": "者风险及受益、受试者义务及研究者义务等。根据方案(版本号:2.0,", "bbox": [187, 603, 890, 622]},
	{"text": "版本日期:2022年8月31日)要求,筛选期所有受试者均进行吸入支气", "bbox": [187, 629, 904, 647]},
	{"text": "管扩张剂前后肺功能检查,若受试者无法提供筛选前一年内气道可逆", "bbox": [187, 655, 898, 673]},
	{"text": "性检测报告(吸入沙丁胺醇后FEV1增加≥12%且FEV1绝对值增加≥", "bbox": [187, 681, 902, 699]},
	{"text": "200mL),则筛选期肺功能检查需要满足吸入沙丁胺醇后FEV1增加≥", "bbox": [185, 707, 880, 725]},
	{"text": "12%且FEV1绝对值增加≥200mL。符合要求后才可以入组,受试者表", "bbox": [187, 733, 904, 751]},
	{"text": "示同意。患者.__及其家属表示已充分了解以上告知内容,同意参加", "bbox": [185, 758, 904, 777]},
	{"text": "该临床试验,", "bbox": [185, 784, 314, 802]},
	{"text": "医生与患者__于2024.01.10 09:47同时签署了知", "bbox": [364, 784, 904, 802]},
	{"text": "情同意书(版本号:2.0,版本日期:2022年08月31日),一式两份,一份", "bbox": [185, 810, 904, 828]},
	{"text": "第3页", "bbox": [462, 844, 526, 861]},
	{"text": "CS 扫描全能王", "bbox": [861, 958, 977, 974]},
	{"text": "3亿人都在用的扫描App", "bbox": [861, 977, 976, 987]}
]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord API: raw_items=39, valid_items=39, elapsed=15.8s
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[0]: text=科室:呼吸与危重症医学科, bbox=[88, 35, 327, 53]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[1]: text=姓名:, bbox=[88, 64, 114, 82]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[2]: text=性别:女, bbox=[88, 92, 161, 109]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[3]: text=门诊, bbox=[503, 35, 568, 53]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[4]: text=联系方式, bbox=[503, 64, 585, 81]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[5]: text=596, bbox=[670, 69, 704, 80]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:62岁, bbox=[503, 92, 596, 109]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[7]: text=婚姻状况:其他, bbox=[659, 92, 788, 109]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[8]: text=2024-01-10 10:27 初诊记录, bbox=[84, 137, 368, 155]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[9]: text=检验检查:阅片见双肺轻度支气管扩张,未见明显急性炎症病灶,余肺基本同前, bbox=[84, 163, 882, 181]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[10]: text=(正式报告为准), bbox=[199, 189, 367, 207]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[11]: text=初步诊断:1.鼻窦炎;2.支气管哮喘;, bbox=[84, 215, 446, 234]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[12]: text=处理:药品:, bbox=[84, 242, 243, 260]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[13]: text=(省采3)硫酸沙丁胺醇吸入气雾剂200揿(100μg/揿)/瓶(1【瓶】) sig:, bbox=[192, 268, 906, 287]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[14]: text=(200【揿】)吸入pm(需要时);, bbox=[189, 294, 546, 313]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[15]: text=检查:心脏电生理:心电图(十二导联心电图);CT检查:副鼻窦平扫;, bbox=[189, 320, 890, 338]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[16]: text=使用螺旋扫描加收;普放:DR胸部正侧位片*(2);呼吸专科检查:支气管, bbox=[189, 346, 905, 364]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[17]: text=舒张试验、流速容量曲线;, bbox=[189, 372, 460, 390]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[18]: text=检验:凝血四项、肾功能六项+肝功能八项+血脂六项*+电解质六项+空, bbox=[189, 398, 900, 416]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[19]: text=腹血糖(门诊使用)+肝酶学补充7项+心肌损伤六项、血常规5分类、尿, bbox=[189, 424, 904, 442]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[20]: text=常规加化学分析、感染八项, bbox=[189, 450, 474, 468]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[21]: text=治疗:静脉采血, bbox=[189, 475, 338, 493]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[22]: text=根据患者病情,认为患者基本符合“评价SHR-1905注射液在重度未, bbox=[187, 500, 904, 519]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[23]: text=控制哮喘患者中的有效性及安全性-多中心、随机、双盲、安慰剂对照, bbox=[187, 526, 904, 544]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[24]: text=平行设计II期临床研究(SHR-1905-201)”的筛选要求,2024.01.10 09:15, bbox=[187, 552, 904, 570]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[25]: text=生向患者__及其家属详细介绍该试验目的、试验设计、受试, bbox=[238, 577, 904, 596]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[26]: text=者风险及受益、受试者义务及研究者义务等。根据方案(版本号:2.0,, bbox=[187, 603, 890, 622]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[27]: text=版本日期:2022年8月31日)要求,筛选期所有受试者均进行吸入支气, bbox=[187, 629, 904, 647]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[28]: text=管扩张剂前后肺功能检查,若受试者无法提供筛选前一年内气道可逆, bbox=[187, 655, 898, 673]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[29]: text=性检测报告(吸入沙丁胺醇后FEV1增加≥12%且FEV1绝对值增加≥, bbox=[187, 681, 902, 699]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[30]: text=200mL),则筛选期肺功能检查需要满足吸入沙丁胺醇后FEV1增加≥, bbox=[185, 707, 880, 725]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[31]: text=12%且FEV1绝对值增加≥200mL。符合要求后才可以入组,受试者表, bbox=[187, 733, 904, 751]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[32]: text=示同意。患者.__及其家属表示已充分了解以上告知内容,同意参加, bbox=[185, 758, 904, 777]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[33]: text=该临床试验,, bbox=[185, 784, 314, 802]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[34]: text=医生与患者__于2024.01.10 09:47同时签署了知, bbox=[364, 784, 904, 802]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[35]: text=情同意书(版本号:2.0,版本日期:2022年08月31日),一式两份,一份, bbox=[185, 810, 904, 828]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[36]: text=第3页, bbox=[462, 844, 526, 861]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[37]: text=CS 扫描全能王, bbox=[861, 958, 977, 974]
2026-08-05 05:19:55,956 INFO     29 [qwen-vl-text] coord item[38]: text=3亿人都在用的扫描App, bbox=[861, 977, 976, 987]
2026-08-05 05:19:55,957 INFO     29 [qwen-vl-text] page=2 — 39/39 coords, api_time=15.8s
2026-08-05 05:19:55,960 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=916763, prompt_len=1120
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
2026-08-05 05:20:03,836 INFO     29 [qwen-vl-text] coord API raw response (len=1482):
[
	{"text": "门诊病历", "bbox": [396, 45, 571, 68]},
	{"text": "科室:呼吸与危重症医学科", "bbox": [68, 76, 310, 93]},
	{"text": "姓名:", "bbox": [70, 105, 116, 120]},
	{"text": "性别:女", "bbox": [70, 133, 142, 148]},
	{"text": "门诊", "bbox": [490, 77, 542, 94]},
	{"text": "联系方式", "bbox": [490, 106, 562, 120]},
	{"text": "年龄:62岁", "bbox": [490, 133, 584, 148]},
	{"text": "婚姻状况:其他", "bbox": [649, 133, 779, 148]},
	{"text": "2024-01-10 10:27 初诊记录", "bbox": [65, 177, 354, 194]},
	{"text": "交给患者保存,一份保存在研究中心。签署知情同意书后患者进入筛选", "bbox": [170, 203, 898, 220]},
	{"text": "流程,受试者筛选号为CN..", "bbox": [170, 228, 471, 246]},
	{"text": "新增AE:", "bbox": [170, 254, 264, 272]},
	{"text": "1.高尿酸血症,2024.01.10开始,轻度,持续,与研究药物肯定无关,对研", "bbox": [170, 279, 898, 297]},
	{"text": "究药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。", "bbox": [170, 304, 827, 322]},
	{"text": "2.高脂血症,2024.01.10开始,轻度,持续,与研究药物肯定无关,对研究", "bbox": [170, 330, 898, 348]},
	{"text": "药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。", "bbox": [170, 356, 804, 373]},
	{"text": "3.白细胞计数降低,2024.01.10开始,轻度,持续,与研究药物肯定无关", "bbox": [170, 381, 898, 399]},
	{"text": "对研究药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。此项", "bbox": [170, 406, 898, 424]},
	{"text": "指标与患者临床症状不符,考虑让其一周内复测。", "bbox": [170, 432, 690, 450]},
	{"text": "规律使用吸入药物,用后漱口,定期复诊;避免接触可能过敏原;不用地", "bbox": [170, 458, 898, 476]},
	{"text": "毯,不养动物", "bbox": [170, 484, 317, 502]},
	{"text": "医师签", "bbox": [652, 523, 755, 540]},
	{"text": "门诊病历专用", "bbox": [77, 568, 315, 590]},
	{"text": "※提醒:复诊时,请携带本病历记录,谢谢!※", "bbox": [70, 646, 583, 664]}
]
2026-08-05 05:20:03,836 INFO     29 [qwen-vl-text] coord API: raw_items=24, valid_items=24, elapsed=7.9s
2026-08-05 05:20:03,837 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[396, 45, 571, 68]
2026-08-05 05:20:03,837 INFO     29 [qwen-vl-text] coord item[1]: text=科室:呼吸与危重症医学科, bbox=[68, 76, 310, 93]
2026-08-05 05:20:03,837 INFO     29 [qwen-vl-text] coord item[2]: text=姓名:, bbox=[70, 105, 116, 120]
2026-08-05 05:20:03,837 INFO     29 [qwen-vl-text] coord item[3]: text=性别:女, bbox=[70, 133, 142, 148]
2026-08-05 05:20:03,837 INFO     29 [qwen-vl-text] coord item[4]: text=门诊, bbox=[490, 77, 542, 94]
2026-08-05 05:20:03,837 INFO     29 [qwen-vl-text] coord item[5]: text=联系方式, bbox=[490, 106, 562, 120]
2026-08-05 05:20:03,837 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:62岁, bbox=[490, 133, 584, 148]
2026-08-05 05:20:03,837 INFO     29 [qwen-vl-text] coord item[7]: text=婚姻状况:其他, bbox=[649, 133, 779, 148]
2026-08-05 05:20:03,837 INFO     29 [qwen-vl-text] coord item[8]: text=2024-01-10 10:27 初诊记录, bbox=[65, 177, 354, 194]
2026-08-05 05:20:03,837 INFO     29 [qwen-vl-text] coord item[9]: text=交给患者保存,一份保存在研究中心。签署知情同意书后患者进入筛选, bbox=[170, 203, 898, 220]
2026-08-05 05:20:03,837 INFO     29 [qwen-vl-text] coord item[10]: text=流程,受试者筛选号为CN.., bbox=[170, 228, 471, 246]
2026-08-05 05:20:03,837 INFO     29 [qwen-vl-text] coord item[11]: text=新增AE:, bbox=[170, 254, 264, 272]
2026-08-05 05:20:03,837 INFO     29 [qwen-vl-text] coord item[12]: text=1.高尿酸血症,2024.01.10开始,轻度,持续,与研究药物肯定无关,对研, bbox=[170, 279, 898, 297]
2026-08-05 05:20:03,837 INFO     29 [qwen-vl-text] coord item[13]: text=究药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。, bbox=[170, 304, 827, 322]
2026-08-05 05:20:03,837 INFO     29 [qwen-vl-text] coord item[14]: text=2.高脂血症,2024.01.10开始,轻度,持续,与研究药物肯定无关,对研究, bbox=[170, 330, 898, 348]
2026-08-05 05:20:03,837 INFO     29 [qwen-vl-text] coord item[15]: text=药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。, bbox=[170, 356, 804, 373]
2026-08-05 05:20:03,837 INFO     29 [qwen-vl-text] coord item[16]: text=3.白细胞计数降低,2024.01.10开始,轻度,持续,与研究药物肯定无关, bbox=[170, 381, 898, 399]
2026-08-05 05:20:03,837 INFO     29 [qwen-vl-text] coord item[17]: text=对研究药物采取的措施不适用,非SAE,非SIE,未采取对症治疗。此项, bbox=[170, 406, 898, 424]
2026-08-05 05:20:03,837 INFO     29 [qwen-vl-text] coord item[18]: text=指标与患者临床症状不符,考虑让其一周内复测。, bbox=[170, 432, 690, 450]
2026-08-05 05:20:03,837 INFO     29 [qwen-vl-text] coord item[19]: text=规律使用吸入药物,用后漱口,定期复诊;避免接触可能过敏原;不用地, bbox=[170, 458, 898, 476]
2026-08-05 05:20:03,837 INFO     29 [qwen-vl-text] coord item[20]: text=毯,不养动物, bbox=[170, 484, 317, 502]
2026-08-05 05:20:03,837 INFO     29 [qwen-vl-text] coord item[21]: text=医师签, bbox=[652, 523, 755, 540]
2026-08-05 05:20:03,837 INFO     29 [qwen-vl-text] coord item[22]: text=门诊病历专用, bbox=[77, 568, 315, 590]
2026-08-05 05:20:03,837 INFO     29 [qwen-vl-text] coord item[23]: text=※提醒:复诊时,请携带本病历记录,谢谢!※, bbox=[70, 646, 583, 664]
2026-08-05 05:20:03,838 INFO     29 [qwen-vl-text] page=3 — 24/24 coords, api_time=7.9s
2026-08-05 05:20:03,838 INFO     29 [qwen-vl-text] new_positions (135):
[[0, 249.89999999999998, 351.05, 16.84, 35.364], [0, 61.879999999999995, 201.10999999999999, 42.942, 56.414], [0, 304.64, 315.945, 42.942, 56.414], [0, 304.64, 336.77, 65.676, 79.148], [0, 62.474999999999994, 104.72, 88.41, 101.88199999999999], [0, 304.64, 358.78499999999997, 88.41, 101.88199999999999], [0, 396.27, 473.025, 88.41, 101.88199999999999], [0, 60.095, 225.505, 125.458, 139.772], [0, 60.095, 238.0, 145.666, 160.822], [0, 59.5, 542.045, 166.716, 182.714], [0, 120.785, 542.045, 187.766, 203.76399999999998], [0, 120.785, 542.045, 208.816, 224.814], [0, 120.785, 542.045, 229.86599999999999, 245.864], [0, 120.785, 542.045, 250.916, 266.914], [0, 120.785, 252.875, 271.966, 287.964], [0, 61.879999999999995, 513.485, 293.858, 309.014], [0, 120.785, 182.665, 314.908, 330.06399999999996], [0, 120.785, 285.59999999999997, 335.95799999999997, 351.114], [0, 120.785, 285.59999999999997, 357.008, 372.164], [0, 120.785, 340.34, 378.058, 393.214], [0, 120.785, 348.075, 399.108, 414.264], [0, 120.785, 320.705, 420.15799999999996, 435.31399999999996], [0, 120.785, 542.045, 440.366, 456.364], [0, 120.785, 195.16, 461.416, 477.414], [0, 120.785, 540.855, 482.466, 498.464], [0, 120.785, 151.725, 503.51599999999996, 518.672], [0, 120.785, 224.315, 524.566, 540.564], [0, 120.785, 541.4499999999999, 545.616, 561.614], [0, 120.785, 540.855, 566.6659999999999, 582.664], [0, 120.785, 169.575, 587.716, 602.872], [0, 120.785, 540.855, 608.766, 624.764], [0, 120.785, 169.575, 629.816, 644.972], [0, 120.785, 540.855, 650.866, 666.864], [0, 120.785, 183.26, 671.9159999999999, 687.914], [0, 282.625, 321.3, 699.702, 714.858], [0, 512.295, 581.3149999999999, 806.636, 820.108], [0, 512.295, 580.72, 822.634, 831.054], [1, 254.66, 353.43, 15.155999999999999, 29.47], [1, 66.045, 205.87, 37.048, 51.361999999999995], [1, 66.045, 91.63, 60.623999999999995, 74.938], [1, 66.045, 109.47999999999999, 84.2, 98.514], [1, 308.21, 355.215, 60.623999999999995, 74.938], [1, 308.21, 362.35499999999996, 84.2, 98.514], [1, 398.65, 473.62, 84.2, 98.514], [1, 64.855, 231.45499999999998, 122.08999999999999, 136.404], [1, 126.14, 542.045, 143.14, 158.296], [1, 126.14, 146.965, 165.03199999999998, 179.346], [1, 126.14, 541.4499999999999, 186.082, 202.07999999999998], [1, 126.14, 175.525, 207.974, 223.13], [1, 126.14, 462.90999999999997, 229.024, 244.17999999999998], [1, 126.14, 357.59499999999997, 250.916, 266.914], [1, 67.83, 273.7, 295.542, 310.698], [1, 67.83, 390.32, 315.75, 331.748], [1, 127.33, 390.32, 336.8, 352.798], [1, 127.33, 543.235, 357.84999999999997, 373.848], [1, 127.33, 267.75, 379.74199999999996, 394.89799999999997], [1, 127.33, 542.045, 399.95, 415.948], [1, 127.33, 542.045, 421.0, 436.998], [1, 127.33, 535.5, 442.05, 458.048], [1, 127.33, 542.045, 463.09999999999997, 479.09799999999996], [1, 127.33, 541.4499999999999, 484.15, 500.14799999999997], [1, 127.33, 541.4499999999999, 505.2, 521.198], [1, 127.33, 541.4499999999999, 526.25, 542.2479999999999], [1, 127.33, 541.4499999999999, 547.3, 563.298], [1, 127.33, 541.4499999999999, 568.35, 584.348], [1, 127.33, 541.4499999999999, 589.4, 605.398], [1, 127.33, 541.4499999999999, 610.4499999999999, 626.448], [1, 127.33, 541.4499999999999, 631.5, 647.4979999999999], [1, 127.33, 249.89999999999998, 653.3919999999999, 668.548], [1, 288.575, 326.06, 703.0699999999999, 717.384], [1, 512.295, 581.3149999999999, 806.636, 820.108], [1, 512.295, 580.72, 822.634, 830.212], [2, 52.36, 194.565, 29.47, 44.626], [2, 52.36, 67.83, 53.888, 69.044], [2, 52.36, 95.795, 77.464, 91.77799999999999], [2, 299.28499999999997, 337.96, 29.47, 44.626], [2, 299.28499999999997, 348.075, 53.888, 68.202], [2, 398.65, 418.88, 58.098, 67.36], [2, 299.28499999999997, 354.62, 77.464, 91.77799999999999], [2, 392.10499999999996, 468.85999999999996, 77.464, 91.77799999999999], [2, 49.98, 218.95999999999998, 115.354, 130.51], [2, 49.98, 524.79, 137.246, 152.402], [2, 118.405, 218.36499999999998, 159.138, 174.29399999999998], [2, 49.98, 265.37, 181.03, 197.028], [2, 49.98, 144.58499999999998, 203.76399999999998, 218.92], [2, 114.24, 539.0699999999999, 225.656, 241.654], [2, 112.455, 324.87, 247.548, 263.546], [2, 112.455, 529.55, 269.44, 284.596], [2, 112.455, 538.475, 291.332, 306.488], [2, 112.455, 273.7, 313.224, 328.38], [2, 112.455, 535.5, 335.116, 350.272], [2, 112.455, 537.88, 357.008, 372.164], [2, 112.455, 282.03, 378.9, 394.056], [2, 112.455, 201.10999999999999, 399.95, 415.106], [2, 111.265, 537.88, 421.0, 436.998], [2, 111.265, 537.88, 442.892, 458.048], [2, 111.265, 537.88, 464.784, 479.94], [2, 141.60999999999999, 537.88, 485.834, 501.832], [2, 111.265, 529.55, 507.726, 523.7239999999999], [2, 111.265, 537.88, 529.6179999999999, 544.774], [2, 111.265, 534.31, 551.51, 566.6659999999999], [2, 111.265, 536.6899999999999, 573.4019999999999, 588.558], [2, 110.07499999999999, 523.6, 595.294, 610.4499999999999], [2, 111.265, 537.88, 617.1859999999999, 632.342], [2, 110.07499999999999, 537.88, 638.236, 654.2339999999999], [2, 110.07499999999999, 186.82999999999998, 660.1279999999999, 675.284], [2, 216.57999999999998, 537.88, 660.1279999999999, 675.284], [2, 110.07499999999999, 537.88, 682.02, 697.1759999999999], [2, 274.89, 312.96999999999997, 710.648, 724.962], [2, 512.295, 581.3149999999999, 806.636, 820.108], [2, 512.295, 580.72, 822.634, 831.054], [3, 235.61999999999998, 339.745, 37.89, 57.256], [3, 40.46, 184.45, 63.992, 78.306], [3, 41.65, 69.02, 88.41, 101.03999999999999], [3, 41.65, 84.49, 111.98599999999999, 124.616], [3, 291.55, 322.49, 64.834, 79.148], [3, 291.55, 334.39, 89.252, 101.03999999999999], [3, 291.55, 347.47999999999996, 111.98599999999999, 124.616], [3, 386.155, 463.505, 111.98599999999999, 124.616], [3, 38.675, 210.63, 149.034, 163.34799999999998], [3, 101.14999999999999, 534.31, 170.926, 185.23999999999998], [3, 101.14999999999999, 280.245, 191.976, 207.132], [3, 101.14999999999999, 157.07999999999998, 213.868, 229.024], [3, 101.14999999999999, 534.31, 234.91799999999998, 250.07399999999998], [3, 101.14999999999999, 492.065, 255.968, 271.12399999999997], [3, 101.14999999999999, 534.31, 277.86, 293.01599999999996], [3, 101.14999999999999, 478.38, 299.752, 314.066], [3, 101.14999999999999, 534.31, 320.80199999999996, 335.95799999999997], [3, 101.14999999999999, 534.31, 341.852, 357.008], [3, 101.14999999999999, 410.54999999999995, 363.74399999999997, 378.9], [3, 101.14999999999999, 534.31, 385.63599999999997, 400.792], [3, 101.14999999999999, 188.61499999999998, 407.52799999999996, 422.68399999999997], [3, 387.94, 449.22499999999997, 440.366, 454.68], [3, 45.815, 187.42499999999998, 478.256, 496.78], [3, 41.65, 346.885, 543.932, 559.088]]
2026-08-05 05:20:03,838 INFO     29 [qwen-vl-text] ═══ DONE ═══ 135 positions, pages=4, time=63.2s
2026-08-05 05:20:03,838 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:20:03,838 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 05:20:03,839 INFO     29 [qwen-vl-text] positions(87): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:20:03,839 INFO     29 [qwen-vl-text] page grouping: [4, 5, 6], lines per page: [34, 37, 16]
2026-08-05 05:20:04,079 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:20:04,313 INFO     29 [qwen-vl-text] page=5, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:20:04,490 INFO     29 [qwen-vl-text] page=6, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:20:04,492 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1740
2026-08-05 05:20:04,492 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:20:04,492 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 137, \"bbox_end\": 223, \"encounter_dates\": [\"2024-03-21\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊病历\n科室:呼吸与危重症医学科\n姓\n性别:女\n门诊\n联系方\n年龄:62岁\n婚姻状况:其他\n2024-03-21 08:40 初诊记录\n主诉:SHR-1905-201 试验复筛\n现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年\n余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现\n气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行\n听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并\n规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可\n320ug bid,近日活动后气促再发,否认喘鸣音。无发热、胸痛。\n2024.01.10参加SHR-1905-201临床试验,因白细胞计数<3.0*10^9/L符\n合排除标准第12条筛败,于2024.03.01血液科就诊,无特殊处理,\n2024.03.06进行SHR-1905-201试验二次知情。受试者今日返院完成V3\n访视。\n既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。\n既往病史:\n1.2022.12.10肝囊肿,持续;\n2.2023.10.31鼻窦炎,持续;\n3.2023.10.31双肺良性小结节,持续;\n4.2023.11.03-2023.12.13,肺肺部感染;\n5.2024.03.01开始,白细胞数降低1级;\n6.2024.01.10开始,高脂蛋白a血症,\n过敏史:否认食物、药物过敏史。\n体格检查收缩压(mmHg):113;舒张压(mmHg):76\n其他体格检查:09:37进行生命体征测量:体温:36.5℃,血压:\n113/76mmHg,呼吸:18次/分,脉搏:98次/分;\n查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见\n第1页\n科室:呼吸与危重症医学科\n姓名\n性别:女\n门诊\n联系方\n年龄:62岁\n婚姻状况:其他\n2024-03-21 08:40 初诊记录\n皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅\n大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。\n耳廓正常无畸形,外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无\n鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿\n大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中\n肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动\n正常,双肺呼吸音粗,未闻及干湿罗音。心律齐。双下肢无水肿。心音正\n常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛、反跳痛,无液\n波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触及,肾脏未触\n及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖器未查、肛门\n直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无异常,其他无\n异常。.\n检验检查:无\n初步诊断:支气管哮喘\n处理:\nCM 跟踪:\n1、布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,\n320ug,bid,经口腔吸入,用于控制哮喘。\n处理:\n1、2024.03.14-2024.03.21 家用峰流速仪使用 ePRO 系统填写依从性\n7/7*100%=100%,嘱托患者按照自己实际情况及时填写日志,如有问题\n随时沟通。\n2、无新增 AE,CM,无临床试验安全性事件。\n3、今日回收硫酸沙丁胺醇吸入气雾剂,发放新的硫酸沙丁胺醇吸入气\n雾剂1盒,并嘱托受试者正确保存和使用。\n4、绝经期女性,未做血、尿妊娠检查。\n第2页\nCS 扫描全能王\n3亿人都在用的扫描App\n科室:呼吸与危重症医学科\n门诊\n姓名\n联系方式\n性别:女\n年龄:62岁\n婚姻状况:其他\n2024-03-21 08:40 初诊记录\n5、受试者所有检查结果经再次核对入排,符合所有入选标准,不符合任\n一排除标准,可随机入组,分配随机号:_,随机分层信息:中剂量\nICS,嗜酸性粒细胞计数<300/ul,未联合使用LAMA。\n6、嘱托受试者2024.03.22来院行V4随访。\n医师签\n门诊病历专用章\n※提醒:复诊时,请携带本病历记录,谢谢!※\n第3页",
    "role": "user"
  }
]
[92m05:20:04 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:20:04,493 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:20:04,494 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:20:04.493+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 16, "failed": 0, "current": {"d7b98bb4908c11f1a3da71efcdd7cc1f": {"id": "d7b98bb4908c11f1a3da71efcdd7cc1f", "doc_id": "d7626528908c11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479738, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785907001430, "task_type": "dataflow", "root_trace_id": "ea6d5499d1eb4a3cabaa8fb5a06c80f8", "root_traceparent": "00-ea6d5499d1eb4a3cabaa8fb5a06c80f8-0f37f835e898f31c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:20:13,320 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:20:13,320 INFO     29 [qwen-vl-text] LLM output (len=1082):
{
  "encounter_date": "2024-03-21",
  "chief_complaint": "SHR-1905-201 试验复筛",
  "present_illness": "发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可320ug bid,近日活动后气促再发,否认喘鸣音。无发热、胸痛。2024.01.10参加SHR-1905-201临床试验,因白细胞计数<3.0*10^9/L符合排除标准第12条筛败,于2024.03.01血液科就诊,无特殊处理,2024.03.06进行SHR-1905-201试验二次知情。受试者今日返院完成V3访视。",
  "past_history": "否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。既往病史:1.2022.12.10肝囊肿,持续;2.2023.10.31鼻窦炎,持续;3.2023.10.31双肺良性小结节,持续;4.2023.11.03-2023.12.13,肺肺部感染;5.2024.03.01开始,白细胞数降低1级;6.2024.01.10开始,高脂蛋白a血症。过敏史:否认食物、药物过敏史。",
  "diagnosis": "支气管哮喘",
  "treatment_plan": [
    "布地奈德福莫特罗粉吸入剂 320ug bid 经口腔吸入 持续使用（2022.11.27开始）",
    "2024.03.14-2024.03.21 家用峰流速仪使用 ePRO 系统填写依从性7/7*100%=100%，嘱托患者按照自己实际情况及时填写日志，如有问题随时沟通",
    "无新增 AE,CM,无临床试验安全性事件",
    "今日回收硫酸沙丁胺醇吸入气雾剂，发放新的硫酸沙丁胺醇吸入气雾剂1盒，并嘱托受试者正确保存和使用",
    "绝经期女性，未做血、尿妊娠检查",
    "受试者所有检查结果经再次核对入排，符合所有入选标准，不符合任一排除标准，可随机入组，分配随机号:_，随机分层信息:中剂量ICS，嗜酸性粒细胞计数<300/ul，未联合使用LAMA",
    "嘱托受试者2024.03.22来院行V4随访"
  ]
}
2026-08-05 05:20:13,320 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-03-21]
2026-08-05 05:20:13,325 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1352976, prompt_len=1491
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共34行）
["门诊病历", "科室:呼吸与危重症医学科", "姓", "性别:女", "门诊", "联系方", "年龄:62岁", "婚姻状况:其他", "2024-03-21 08:40 初诊记录", "主诉:SHR-1905-201 试验复筛", "现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年", "余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现", "气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行", "听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并", "规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可", "320ug bid,近日活动后气促再发,否认喘鸣音。无发热、胸痛。", "2024.01.10参加SHR-1905-201临床试验,因白细胞计数<3.0*10^9/L符", "合排除标准第12条筛败,于2024.03.01血液科就诊,无特殊处理,", "2024.03.06进行SHR-1905-201试验二次知情。受试者今日返院完成V3", "访视。", "既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。", "既往病史:", "1.2022.12.10肝囊肿,持续;", "2.2023.10.31鼻窦炎,持续;", "3.2023.10.31双肺良性小结节,持续;", "4.2023.11.03-2023.12.13,肺肺部感染;", "5.2024.03.01开始,白细胞数降低1级;", "6.2024.01.10开始,高脂蛋白a血症,", "过敏史:否认食物、药物过敏史。", "体格检查收缩压(mmHg):113;舒张压(mmHg):76", "其他体格检查:09:37进行生命体征测量:体温:36.5℃,血压:", "113/76mmHg,呼吸:18次/分,脉搏:98次/分;", "查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见", "第1页"]

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
2026-08-05 05:20:28,214 INFO     29 [qwen-vl-text] coord API raw response (len=2260):
[
	{"text": "门诊病历", "bbox": [417, 42, 585, 65]},
	{"text": "科室:呼吸与危重症医学科", "bbox": [92, 74, 334, 91]},
	{"text": "姓", "bbox": [92, 102, 114, 118]},
	{"text": "性别:女", "bbox": [93, 131, 165, 147]},
	{"text": "门诊", "bbox": [510, 74, 561, 91]},
	{"text": "联系方", "bbox": [510, 103, 565, 118]},
	{"text": "年龄:62岁", "bbox": [510, 131, 598, 147]},
	{"text": "婚姻状况:其他", "bbox": [660, 131, 787, 147]},
	{"text": "2024-03-21 08:40 初诊记录", "bbox": [90, 175, 375, 193]},
	{"text": "主诉:SHR-1905-201 试验复筛", "bbox": [90, 201, 441, 219]},
	{"text": "现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年", "bbox": [89, 227, 900, 246]},
	{"text": "余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现", "bbox": [194, 252, 900, 270]},
	{"text": "气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行", "bbox": [194, 277, 900, 295]},
	{"text": "听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并", "bbox": [194, 302, 900, 320]},
	{"text": "规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可", "bbox": [194, 327, 861, 346]},
	{"text": "320ug bid,近日活动后气促再发,否认喘鸣音。无发热、胸痛。", "bbox": [194, 353, 792, 371]},
	{"text": "2024.01.10参加SHR-1905-201临床试验,因白细胞计数<3.0*10^9/L符", "bbox": [194, 378, 900, 396]},
	{"text": "合排除标准第12条筛败,于2024.03.01血液科就诊,无特殊处理,", "bbox": [194, 403, 843, 421]},
	{"text": "2024.03.06进行SHR-1905-201试验二次知情。受试者今日返院完成V3", "bbox": [194, 428, 900, 447]},
	{"text": "访视。", "bbox": [194, 454, 252, 472]},
	{"text": "既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。", "bbox": [90, 479, 854, 498]},
	{"text": "既往病史:", "bbox": [194, 506, 299, 524]},
	{"text": "1.2022.12.10肝囊肿,持续;", "bbox": [194, 531, 474, 549]},
	{"text": "2.2023.10.31鼻窦炎,持续;", "bbox": [194, 557, 474, 575]},
	{"text": "3.2023.10.31双肺良性小结节,持续;", "bbox": [194, 582, 565, 600]},
	{"text": "4.2023.11.03-2023.12.13,肺肺部感染;", "bbox": [194, 608, 578, 626]},
	{"text": "5.2024.03.01开始,白细胞数降低1级;", "bbox": [194, 633, 586, 651]},
	{"text": "6.2024.01.10开始,高脂蛋白a血症,", "bbox": [194, 659, 563, 677]},
	{"text": "过敏史:否认食物、药物过敏史。", "bbox": [90, 736, 443, 754]},
	{"text": "体格检查收缩压(mmHg):113;舒张压(mmHg):76", "bbox": [90, 761, 643, 780]},
	{"text": "其他体格检查:09:37进行生命体征测量:体温:36.5℃,血压:", "bbox": [194, 787, 796, 805]},
	{"text": "113/76mmHg,呼吸:18次/分,脉搏:98次/分;", "bbox": [194, 812, 682, 831]},
	{"text": "查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见", "bbox": [194, 838, 902, 856]},
	{"text": "第1页", "bbox": [470, 870, 534, 887]}
]
2026-08-05 05:20:28,215 INFO     29 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=14.9s
2026-08-05 05:20:28,215 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[417, 42, 585, 65]
2026-08-05 05:20:28,215 INFO     29 [qwen-vl-text] coord item[1]: text=科室:呼吸与危重症医学科, bbox=[92, 74, 334, 91]
2026-08-05 05:20:28,215 INFO     29 [qwen-vl-text] coord item[2]: text=姓, bbox=[92, 102, 114, 118]
2026-08-05 05:20:28,215 INFO     29 [qwen-vl-text] coord item[3]: text=性别:女, bbox=[93, 131, 165, 147]
2026-08-05 05:20:28,215 INFO     29 [qwen-vl-text] coord item[4]: text=门诊, bbox=[510, 74, 561, 91]
2026-08-05 05:20:28,215 INFO     29 [qwen-vl-text] coord item[5]: text=联系方, bbox=[510, 103, 565, 118]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:62岁, bbox=[510, 131, 598, 147]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[7]: text=婚姻状况:其他, bbox=[660, 131, 787, 147]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[8]: text=2024-03-21 08:40 初诊记录, bbox=[90, 175, 375, 193]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[9]: text=主诉:SHR-1905-201 试验复筛, bbox=[90, 201, 441, 219]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[10]: text=现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年, bbox=[89, 227, 900, 246]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[11]: text=余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现, bbox=[194, 252, 900, 270]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[12]: text=气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行, bbox=[194, 277, 900, 295]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[13]: text=听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并, bbox=[194, 302, 900, 320]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[14]: text=规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可, bbox=[194, 327, 861, 346]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[15]: text=320ug bid,近日活动后气促再发,否认喘鸣音。无发热、胸痛。, bbox=[194, 353, 792, 371]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[16]: text=2024.01.10参加SHR-1905-201临床试验,因白细胞计数<3.0*10^9/L符, bbox=[194, 378, 900, 396]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[17]: text=合排除标准第12条筛败,于2024.03.01血液科就诊,无特殊处理,, bbox=[194, 403, 843, 421]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[18]: text=2024.03.06进行SHR-1905-201试验二次知情。受试者今日返院完成V3, bbox=[194, 428, 900, 447]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[19]: text=访视。, bbox=[194, 454, 252, 472]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[20]: text=既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。, bbox=[90, 479, 854, 498]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[21]: text=既往病史:, bbox=[194, 506, 299, 524]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[22]: text=1.2022.12.10肝囊肿,持续;, bbox=[194, 531, 474, 549]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[23]: text=2.2023.10.31鼻窦炎,持续;, bbox=[194, 557, 474, 575]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[24]: text=3.2023.10.31双肺良性小结节,持续;, bbox=[194, 582, 565, 600]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[25]: text=4.2023.11.03-2023.12.13,肺肺部感染;, bbox=[194, 608, 578, 626]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[26]: text=5.2024.03.01开始,白细胞数降低1级;, bbox=[194, 633, 586, 651]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[27]: text=6.2024.01.10开始,高脂蛋白a血症,, bbox=[194, 659, 563, 677]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[28]: text=过敏史:否认食物、药物过敏史。, bbox=[90, 736, 443, 754]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[29]: text=体格检查收缩压(mmHg):113;舒张压(mmHg):76, bbox=[90, 761, 643, 780]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[30]: text=其他体格检查:09:37进行生命体征测量:体温:36.5℃,血压:, bbox=[194, 787, 796, 805]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[31]: text=113/76mmHg,呼吸:18次/分,脉搏:98次/分;, bbox=[194, 812, 682, 831]
2026-08-05 05:20:28,216 INFO     29 [qwen-vl-text] coord item[32]: text=查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见, bbox=[194, 838, 902, 856]
2026-08-05 05:20:28,217 INFO     29 [qwen-vl-text] coord item[33]: text=第1页, bbox=[470, 870, 534, 887]
2026-08-05 05:20:28,217 INFO     29 [qwen-vl-text] page=4 — 34/34 coords, api_time=14.9s
2026-08-05 05:20:28,222 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1857056, prompt_len=1462
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
2026-08-05 05:20:40,401 INFO     29 [qwen-vl-text] coord API raw response (len=2361):
[
	{"text": "科室:呼吸与危重症医学科", "bbox": [102, 48, 338, 65]},
	{"text": "姓名", "bbox": [104, 75, 142, 92]},
	{"text": "性别:女", "bbox": [104, 102, 175, 118]},
	{"text": "门诊", "bbox": [513, 48, 564, 65]},
	{"text": "联系方", "bbox": [513, 75, 569, 92]},
	{"text": "年龄:62岁", "bbox": [513, 102, 603, 118]},
	{"text": "婚姻状况:其他", "bbox": [664, 102, 790, 118]},
	{"text": "2024-03-21 08:40 初诊记录", "bbox": [100, 145, 381, 162]},
	{"text": "皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅", "bbox": [202, 170, 905, 188]},
	{"text": "大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。", "bbox": [202, 194, 892, 212]},
	{"text": "耳廓正常无畸形,外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无", "bbox": [202, 218, 905, 237]},
	{"text": "鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿", "bbox": [202, 242, 904, 261]},
	{"text": "大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中", "bbox": [202, 266, 904, 285]},
	{"text": "肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动", "bbox": [202, 290, 904, 309]},
	{"text": "正常,双肺呼吸音粗,未闻及干湿罗音。心律齐。双下肢无水肿。心音正", "bbox": [202, 314, 904, 333]},
	{"text": "常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛、反跳痛,无液", "bbox": [202, 338, 904, 357]},
	{"text": "波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触及,肾脏未触", "bbox": [202, 362, 904, 381]},
	{"text": "及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖器未查、肛门", "bbox": [202, 386, 904, 405]},
	{"text": "直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无异常,其他无", "bbox": [202, 410, 904, 429]},
	{"text": "异常。.", "bbox": [202, 435, 267, 454]},
	{"text": "检验检查:无", "bbox": [100, 465, 226, 483]},
	{"text": "初步诊断:支气管哮喘", "bbox": [100, 490, 320, 508]},
	{"text": "处理:", "bbox": [100, 515, 204, 533]},
	{"text": "CM 跟踪:", "bbox": [202, 540, 300, 558]},
	{"text": "1、布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,", "bbox": [202, 564, 777, 583]},
	{"text": "320ug,bid,经口腔吸入,用于控制哮喘。", "bbox": [202, 588, 591, 607]},
	{"text": "处理:", "bbox": [202, 614, 258, 632]},
	{"text": "1、2024.03.14-2024.03.21 家用峰流速仪使用 ePRO 系统填写依从性", "bbox": [202, 638, 858, 657]},
	{"text": "7/7*100%=100%,嘱托患者按照自己实际情况及时填写日志,如有问题", "bbox": [202, 662, 904, 681]},
	{"text": "随时沟通。", "bbox": [202, 687, 308, 705]},
	{"text": "2、无新增 AE,CM,无临床试验安全性事件。", "bbox": [202, 711, 650, 729]},
	{"text": "3、今日回收硫酸沙丁胺醇吸入气雾剂,发放新的硫酸沙丁胺醇吸入气", "bbox": [202, 735, 904, 754]},
	{"text": "雾剂1盒,并嘱托受试者正确保存和使用。", "bbox": [202, 759, 628, 778]},
	{"text": "4、绝经期女性,未做血、尿妊娠检查。", "bbox": [202, 783, 594, 802]},
	{"text": "第2页", "bbox": [470, 815, 535, 832]},
	{"text": "CS 扫描全能王", "bbox": [861, 958, 977, 974]},
	{"text": "3亿人都在用的扫描App", "bbox": [861, 977, 976, 986]}
]
2026-08-05 05:20:40,401 INFO     29 [qwen-vl-text] coord API: raw_items=37, valid_items=37, elapsed=12.2s
2026-08-05 05:20:40,402 INFO     29 [qwen-vl-text] coord item[0]: text=科室:呼吸与危重症医学科, bbox=[102, 48, 338, 65]
2026-08-05 05:20:40,402 INFO     29 [qwen-vl-text] coord item[1]: text=姓名, bbox=[104, 75, 142, 92]
2026-08-05 05:20:40,402 INFO     29 [qwen-vl-text] coord item[2]: text=性别:女, bbox=[104, 102, 175, 118]
2026-08-05 05:20:40,402 INFO     29 [qwen-vl-text] coord item[3]: text=门诊, bbox=[513, 48, 564, 65]
2026-08-05 05:20:40,402 INFO     29 [qwen-vl-text] coord item[4]: text=联系方, bbox=[513, 75, 569, 92]
2026-08-05 05:20:40,402 INFO     29 [qwen-vl-text] coord item[5]: text=年龄:62岁, bbox=[513, 102, 603, 118]
2026-08-05 05:20:40,402 INFO     29 [qwen-vl-text] coord item[6]: text=婚姻状况:其他, bbox=[664, 102, 790, 118]
2026-08-05 05:20:40,402 INFO     29 [qwen-vl-text] coord item[7]: text=2024-03-21 08:40 初诊记录, bbox=[100, 145, 381, 162]
2026-08-05 05:20:40,402 INFO     29 [qwen-vl-text] coord item[8]: text=皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅, bbox=[202, 170, 905, 188]
2026-08-05 05:20:40,402 INFO     29 [qwen-vl-text] coord item[9]: text=大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。, bbox=[202, 194, 892, 212]
2026-08-05 05:20:40,402 INFO     29 [qwen-vl-text] coord item[10]: text=耳廓正常无畸形,外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无, bbox=[202, 218, 905, 237]
2026-08-05 05:20:40,402 INFO     29 [qwen-vl-text] coord item[11]: text=鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿, bbox=[202, 242, 904, 261]
2026-08-05 05:20:40,402 INFO     29 [qwen-vl-text] coord item[12]: text=大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中, bbox=[202, 266, 904, 285]
2026-08-05 05:20:40,402 INFO     29 [qwen-vl-text] coord item[13]: text=肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动, bbox=[202, 290, 904, 309]
2026-08-05 05:20:40,402 INFO     29 [qwen-vl-text] coord item[14]: text=正常,双肺呼吸音粗,未闻及干湿罗音。心律齐。双下肢无水肿。心音正, bbox=[202, 314, 904, 333]
2026-08-05 05:20:40,402 INFO     29 [qwen-vl-text] coord item[15]: text=常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛、反跳痛,无液, bbox=[202, 338, 904, 357]
2026-08-05 05:20:40,402 INFO     29 [qwen-vl-text] coord item[16]: text=波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触及,肾脏未触, bbox=[202, 362, 904, 381]
2026-08-05 05:20:40,403 INFO     29 [qwen-vl-text] coord item[17]: text=及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖器未查、肛门, bbox=[202, 386, 904, 405]
2026-08-05 05:20:40,403 INFO     29 [qwen-vl-text] coord item[18]: text=直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无异常,其他无, bbox=[202, 410, 904, 429]
2026-08-05 05:20:40,403 INFO     29 [qwen-vl-text] coord item[19]: text=异常。., bbox=[202, 435, 267, 454]
2026-08-05 05:20:40,403 INFO     29 [qwen-vl-text] coord item[20]: text=检验检查:无, bbox=[100, 465, 226, 483]
2026-08-05 05:20:40,403 INFO     29 [qwen-vl-text] coord item[21]: text=初步诊断:支气管哮喘, bbox=[100, 490, 320, 508]
2026-08-05 05:20:40,403 INFO     29 [qwen-vl-text] coord item[22]: text=处理:, bbox=[100, 515, 204, 533]
2026-08-05 05:20:40,403 INFO     29 [qwen-vl-text] coord item[23]: text=CM 跟踪:, bbox=[202, 540, 300, 558]
2026-08-05 05:20:40,403 INFO     29 [qwen-vl-text] coord item[24]: text=1、布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,, bbox=[202, 564, 777, 583]
2026-08-05 05:20:40,403 INFO     29 [qwen-vl-text] coord item[25]: text=320ug,bid,经口腔吸入,用于控制哮喘。, bbox=[202, 588, 591, 607]
2026-08-05 05:20:40,403 INFO     29 [qwen-vl-text] coord item[26]: text=处理:, bbox=[202, 614, 258, 632]
2026-08-05 05:20:40,403 INFO     29 [qwen-vl-text] coord item[27]: text=1、2024.03.14-2024.03.21 家用峰流速仪使用 ePRO 系统填写依从性, bbox=[202, 638, 858, 657]
2026-08-05 05:20:40,403 INFO     29 [qwen-vl-text] coord item[28]: text=7/7*100%=100%,嘱托患者按照自己实际情况及时填写日志,如有问题, bbox=[202, 662, 904, 681]
2026-08-05 05:20:40,404 INFO     29 [qwen-vl-text] coord item[29]: text=随时沟通。, bbox=[202, 687, 308, 705]
2026-08-05 05:20:40,404 INFO     29 [qwen-vl-text] coord item[30]: text=2、无新增 AE,CM,无临床试验安全性事件。, bbox=[202, 711, 650, 729]
2026-08-05 05:20:40,404 INFO     29 [qwen-vl-text] coord item[31]: text=3、今日回收硫酸沙丁胺醇吸入气雾剂,发放新的硫酸沙丁胺醇吸入气, bbox=[202, 735, 904, 754]
2026-08-05 05:20:40,404 INFO     29 [qwen-vl-text] coord item[32]: text=雾剂1盒,并嘱托受试者正确保存和使用。, bbox=[202, 759, 628, 778]
2026-08-05 05:20:40,404 INFO     29 [qwen-vl-text] coord item[33]: text=4、绝经期女性,未做血、尿妊娠检查。, bbox=[202, 783, 594, 802]
2026-08-05 05:20:40,404 INFO     29 [qwen-vl-text] coord item[34]: text=第2页, bbox=[470, 815, 535, 832]
2026-08-05 05:20:40,404 INFO     29 [qwen-vl-text] coord item[35]: text=CS 扫描全能王, bbox=[861, 958, 977, 974]
2026-08-05 05:20:40,404 INFO     29 [qwen-vl-text] coord item[36]: text=3亿人都在用的扫描App, bbox=[861, 977, 976, 986]
2026-08-05 05:20:40,405 INFO     29 [qwen-vl-text] page=5 — 37/37 coords, api_time=12.2s
2026-08-05 05:20:40,407 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=545220, prompt_len=885
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共16行）
["科室:呼吸与危重症医学科", "门诊", "姓名", "联系方式", "性别:女", "年龄:62岁", "婚姻状况:其他", "2024-03-21 08:40 初诊记录", "5、受试者所有检查结果经再次核对入排,符合所有入选标准,不符合任", "一排除标准,可随机入组,分配随机号:_,随机分层信息:中剂量", "ICS,嗜酸性粒细胞计数<300/ul,未联合使用LAMA。", "6、嘱托受试者2024.03.22来院行V4随访。", "医师签", "门诊病历专用章", "※提醒:复诊时,请携带本病历记录,谢谢!※", "第3页"]

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
2026-08-05 05:20:45,611 INFO     29 [qwen-vl-text] coord API raw response (len=917):
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
	{"text": "6、嘱托受试者2024.03.22来院行V4随访。", "bbox": [180, 255, 618, 274]},
	{"text": "医师签", "bbox": [652, 295, 715, 312]},
	{"text": "门诊病历专用章", "bbox": [77, 328, 327, 363]},
	{"text": "※提醒:复诊时,请携带本病历记录,谢谢!※", "bbox": [80, 415, 584, 434]},
	{"text": "第3页", "bbox": [459, 850, 521, 866]}
]
2026-08-05 05:20:45,612 INFO     29 [qwen-vl-text] coord API: raw_items=16, valid_items=16, elapsed=5.2s
2026-08-05 05:20:45,612 INFO     29 [qwen-vl-text] coord item[0]: text=科室:呼吸与危重症医学科, bbox=[77, 50, 318, 67]
2026-08-05 05:20:45,612 INFO     29 [qwen-vl-text] coord item[1]: text=门诊, bbox=[498, 50, 550, 67]
2026-08-05 05:20:45,612 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[77, 78, 118, 96]
2026-08-05 05:20:45,612 INFO     29 [qwen-vl-text] coord item[3]: text=联系方式, bbox=[498, 78, 577, 95]
2026-08-05 05:20:45,612 INFO     29 [qwen-vl-text] coord item[4]: text=性别:女, bbox=[77, 107, 150, 123]
2026-08-05 05:20:45,612 INFO     29 [qwen-vl-text] coord item[5]: text=年龄:62岁, bbox=[498, 107, 589, 123]
2026-08-05 05:20:45,612 INFO     29 [qwen-vl-text] coord item[6]: text=婚姻状况:其他, bbox=[651, 107, 781, 123]
2026-08-05 05:20:45,612 INFO     29 [qwen-vl-text] coord item[7]: text=2024-03-21 08:40 初诊记录, bbox=[73, 152, 363, 170]
2026-08-05 05:20:45,612 INFO     29 [qwen-vl-text] coord item[8]: text=5、受试者所有检查结果经再次核对入排,符合所有入选标准,不符合任, bbox=[180, 177, 901, 196]
2026-08-05 05:20:45,612 INFO     29 [qwen-vl-text] coord item[9]: text=一排除标准,可随机入组,分配随机号:_,随机分层信息:中剂量, bbox=[180, 202, 901, 222]
2026-08-05 05:20:45,612 INFO     29 [qwen-vl-text] coord item[10]: text=ICS,嗜酸性粒细胞计数<300/ul,未联合使用LAMA。, bbox=[180, 229, 741, 248]
2026-08-05 05:20:45,612 INFO     29 [qwen-vl-text] coord item[11]: text=6、嘱托受试者2024.03.22来院行V4随访。, bbox=[180, 255, 618, 274]
2026-08-05 05:20:45,612 INFO     29 [qwen-vl-text] coord item[12]: text=医师签, bbox=[652, 295, 715, 312]
2026-08-05 05:20:45,613 INFO     29 [qwen-vl-text] coord item[13]: text=门诊病历专用章, bbox=[77, 328, 327, 363]
2026-08-05 05:20:45,613 INFO     29 [qwen-vl-text] coord item[14]: text=※提醒:复诊时,请携带本病历记录,谢谢!※, bbox=[80, 415, 584, 434]
2026-08-05 05:20:45,613 INFO     29 [qwen-vl-text] coord item[15]: text=第3页, bbox=[459, 850, 521, 866]
2026-08-05 05:20:45,613 INFO     29 [qwen-vl-text] page=6 — 16/16 coords, api_time=5.2s
2026-08-05 05:20:45,614 INFO     29 [qwen-vl-text] new_positions (87):
[[4, 248.11499999999998, 348.075, 35.364, 54.73], [4, 54.739999999999995, 198.73, 62.308, 76.622], [4, 54.739999999999995, 67.83, 85.884, 99.356], [4, 55.335, 98.175, 110.30199999999999, 123.774], [4, 303.45, 333.79499999999996, 62.308, 76.622], [4, 303.45, 336.175, 86.726, 99.356], [4, 303.45, 355.81, 110.30199999999999, 123.774], [4, 392.7, 468.265, 110.30199999999999, 123.774], [4, 53.55, 223.125, 147.35, 162.506], [4, 53.55, 262.395, 169.242, 184.398], [4, 52.955, 535.5, 191.134, 207.132], [4, 115.42999999999999, 535.5, 212.184, 227.34], [4, 115.42999999999999, 535.5, 233.23399999999998, 248.39], [4, 115.42999999999999, 535.5, 254.284, 269.44], [4, 115.42999999999999, 512.295, 275.334, 291.332], [4, 115.42999999999999, 471.23999999999995, 297.226, 312.382], [4, 115.42999999999999, 535.5, 318.276, 333.432], [4, 115.42999999999999, 501.585, 339.32599999999996, 354.48199999999997], [4, 115.42999999999999, 535.5, 360.376, 376.37399999999997], [4, 115.42999999999999, 149.94, 382.268, 397.424], [4, 53.55, 508.13, 403.318, 419.316], [4, 115.42999999999999, 177.905, 426.05199999999996, 441.20799999999997], [4, 115.42999999999999, 282.03, 447.102, 462.258], [4, 115.42999999999999, 282.03, 468.99399999999997, 484.15], [4, 115.42999999999999, 336.175, 490.044, 505.2], [4, 115.42999999999999, 343.90999999999997, 511.936, 527.092], [4, 115.42999999999999, 348.66999999999996, 532.986, 548.1419999999999], [4, 115.42999999999999, 334.98499999999996, 554.8779999999999, 570.034], [4, 53.55, 263.585, 619.712, 634.8679999999999], [4, 53.55, 382.585, 640.762, 656.76], [4, 115.42999999999999, 473.62, 662.654, 677.81], [4, 115.42999999999999, 405.78999999999996, 683.704, 699.702], [4, 115.42999999999999, 536.6899999999999, 705.596, 720.752], [4, 279.65, 317.72999999999996, 732.54, 746.8539999999999], [5, 60.69, 201.10999999999999, 40.416, 54.73], [5, 61.879999999999995, 84.49, 63.15, 77.464], [5, 61.879999999999995, 104.125, 85.884, 99.356], [5, 305.235, 335.58, 40.416, 54.73], [5, 305.235, 338.555, 63.15, 77.464], [5, 305.235, 358.78499999999997, 85.884, 99.356], [5, 395.08, 470.04999999999995, 85.884, 99.356], [5, 59.5, 226.695, 122.08999999999999, 136.404], [5, 120.19, 538.475, 143.14, 158.296], [5, 120.19, 530.74, 163.34799999999998, 178.504], [5, 120.19, 538.475, 183.55599999999998, 199.554], [5, 120.19, 537.88, 203.76399999999998, 219.762], [5, 120.19, 537.88, 223.97199999999998, 239.97], [5, 120.19, 537.88, 244.17999999999998, 260.178], [5, 120.19, 537.88, 264.388, 280.38599999999997], [5, 120.19, 537.88, 284.596, 300.594], [5, 120.19, 537.88, 304.804, 320.80199999999996], [5, 120.19, 537.88, 325.012, 341.01], [5, 120.19, 537.88, 345.21999999999997, 361.21799999999996], [5, 120.19, 158.86499999999998, 366.27, 382.268], [5, 59.5, 134.47, 391.53, 406.686], [5, 59.5, 190.39999999999998, 412.58, 427.736], [5, 59.5, 121.38, 433.63, 448.786], [5, 120.19, 178.5, 454.68, 469.83599999999996], [5, 120.19, 462.315, 474.888, 490.88599999999997], [5, 120.19, 351.645, 495.096, 511.094], [5, 120.19, 153.51, 516.9879999999999, 532.144], [5, 120.19, 510.51, 537.196, 553.194], [5, 120.19, 537.88, 557.404, 573.4019999999999], [5, 120.19, 183.26, 578.454, 593.61], [5, 120.19, 386.75, 598.662, 613.818], [5, 120.19, 537.88, 618.87, 634.8679999999999], [5, 120.19, 373.65999999999997, 639.078, 655.076], [5, 120.19, 353.43, 659.286, 675.284], [5, 279.65, 318.325, 686.23, 700.544], [5, 512.295, 581.3149999999999, 806.636, 820.108], [5, 512.295, 580.72, 822.634, 830.212], [6, 45.815, 189.20999999999998, 42.1, 56.414], [6, 296.31, 327.25, 42.1, 56.414], [6, 45.815, 70.21, 65.676, 80.832], [6, 296.31, 343.315, 65.676, 79.99], [6, 45.815, 89.25, 90.094, 103.566], [6, 296.31, 350.455, 90.094, 103.566], [6, 387.34499999999997, 464.695, 90.094, 103.566], [6, 43.434999999999995, 215.98499999999999, 127.984, 143.14], [6, 107.1, 536.095, 149.034, 165.03199999999998], [6, 107.1, 536.095, 170.084, 186.924], [6, 107.1, 440.895, 192.81799999999998, 208.816], [6, 107.1, 367.71, 214.70999999999998, 230.708], [6, 387.94, 425.42499999999995, 248.39, 262.704], [6, 45.815, 194.565, 276.176, 305.646], [6, 47.599999999999994, 347.47999999999996, 349.43, 365.428], [6, 273.10499999999996, 309.995, 715.6999999999999, 729.172]]
2026-08-05 05:20:45,614 INFO     29 [qwen-vl-text] ═══ DONE ═══ 87 positions, pages=3, time=41.8s
2026-08-05 05:20:45,614 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:20:45,614 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 05:20:45,614 INFO     29 [qwen-vl-text] positions(79): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:20:45,615 INFO     29 [qwen-vl-text] page grouping: [7, 8, 9], lines per page: [35, 28, 16]
2026-08-05 05:20:45,944 INFO     29 [qwen-vl-text] page=7, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:20:46,149 INFO     29 [qwen-vl-text] page=8, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:20:46,319 INFO     29 [qwen-vl-text] page=9, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:20:46,321 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1652
2026-08-05 05:20:46,321 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:20:46,321 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 226, \"bbox_end\": 304, \"encounter_dates\": [\"2024-12-12\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "科室:呼吸与危重症医学科\n门诊\n姓名\n联系\n性别:女\n年龄:63岁\n婚姻状况:其他\n2024-12-12 09:40 初诊记录\n主诉:SHR-1905-201 临床试验 V14\n现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年\n余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现\n气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行\n听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并\n规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可\n320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:\n近日咳嗽咳痰,低烧两天,呼吸道感染。2024.12.02行V14随访\n因患者发热延迟用药。今日回院用药,留院观察1h。\n既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。\n既往病史:\n1.2022.12.10肝囊肿,持续;\n2.2023.10.31鼻窦炎,持续;\n3.2023.10.31双肺良性小结节,持续;\n4.2023.11.03-2023.12.13,肺肺部感染;\n5.2024.03.01开始,白细胞数降低1级,持续;\n6.2024.01.10开始,高脂血症,持续;\n7.十余年前,慢性浅表胃炎,持续中。\n过敏史:否认食物、药物过敏史。\n体格检查收缩压(mmHg):-;舒张压(mmHg):-\n其他体格检查:未行\n检验检查:无\n初步诊断:支气管哮喘\n处理:检查:心脏电生理:心电图(十二导联心电图);\n检验:急诊血常规(五分类)+急诊超敏C反应蛋白、急诊肝功能五项\n治疗:静脉采血\n第1页\n科室:呼吸与危重症医学科\n性别:女\n年龄:63岁\n婚姻状况:其他\n2024-12-12 09:40 初诊记录\n无新增 AE,无新增 CM,无临床试验安全性事件。\n呼吸道感染,2024.1127-2024.12.11,中度,与试验药物关系为可能无关\n对试验药物采取的措施为延迟用药,对 AE 采取的措施为药物治疗,肺\nSAE,非 SIE,不因此退出临床试验。\n跟踪 CM:\n1.盐酸莫西沙片,2024.12.02-2024.12.11,持续中,0.4g/片,1片/次,\nqd,po,用于治疗 AE 呼吸道感染。\n2.桉柠蒎肠溶胶囊,2024.12.02-2024.12.11 持续中,0.3g/粒,1粒/次,\ntid,po,用于治疗 AE 呼吸道感染。(化痰)\n3.氯苯那敏片,2024.12.02-2024.12.11,持续中,4mg/片,1片/次,\nqn,po,用于治疗 AE 呼吸道感染。\n4.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po.用于治\n疗病史慢性浅表胃炎。\n5.复方氨酚烷胺胶囊,2024.11.27-2024.12.02,持续中,0.25g:0.1g,1粒\n/次,bid,po,用于治疗 AE 呼吸道感染。\n6.吸入沙丁胺醇气雾剂,2024.12.02-2024.12.02,400ug,吸入,once,用于支\n气管扩张检查。\nCM 跟踪:\n1、布地奈德福莫特罗粉吸入剂,2022.1127 开始,持续使用,\n320ug,bid,经口腔吸入,用于控制哮喘。\n2、硫酸沙丁胺醇气雾剂,2024.03.06 开始,持续中,100ug,pm,经口腔吸\n入,控制哮喘急性发作。\n第2页\n门诊病历\n科室:呼吸与危重症医学科\n姓名:\n性别:女\n门诊号\n联系方式\n年龄:63岁\n婚姻状况:其他\n2024-12-12 09:40 初诊记录\n处理:\n患者于今日12:21-12:28完成临床试验药物的注射，药物编号为\nY6077Y4950 用药前完善必要检查后随机用药。\n医师\n门诊病历\n※提醒:复诊时,请携带本病历记录,谢谢!※\n“若有高血压糖尿病诊断,建议您到居住地附近社康中心,建立居民健康档案”",
    "role": "user"
  }
]
[92m05:20:46 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:20:46,323 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:20:46,323 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:20:46.322+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 16, "failed": 0, "current": {"d7b98bb4908c11f1a3da71efcdd7cc1f": {"id": "d7b98bb4908c11f1a3da71efcdd7cc1f", "doc_id": "d7626528908c11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479738, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785907001430, "task_type": "dataflow", "root_trace_id": "ea6d5499d1eb4a3cabaa8fb5a06c80f8", "root_traceparent": "00-ea6d5499d1eb4a3cabaa8fb5a06c80f8-0f37f835e898f31c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:20:57,008 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:20:57,008 INFO     29 [qwen-vl-text] LLM output (len=1303):
{
  "encounter_date": "2024-12-12",
  "chief_complaint": "SHR-1905-201 临床试验 V14",
  "present_illness": "发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:近日咳嗽咳痰,低烧两天,呼吸道感染。2024.12.02行V14随访因患者发热延迟用药。今日回院用药,留院观察1h。无新增 AE,无新增 CM,无临床试验安全性事件。呼吸道感染,2024.11.27-2024.12.11,中度,与试验药物关系为可能无关,对试验药物采取的措施为延迟用药,对 AE 采取的措施为药物治疗,非SAE,非 SIE,不因此退出临床试验。患者于今日12:21-12:28完成临床试验药物的注射，药物编号为Y6077Y4950 用药前完善必要检查后随机用药。",
  "past_history": "否认吸烟史、饮酒史。2015年绝经,1988年外院行结扎术。既往病史:1.2022.12.10肝囊肿,持续;2.2023.10.31鼻窦炎,持续;3.2023.10.31双肺良性小结节,持续;4.2023.11.03-2023.12.13,肺部感染;5.2024.03.01开始,白细胞数降低1级,持续;6.2024.01.10开始,高脂血症,持续;7.十余年前,慢性浅表胃炎,持续中。过敏史:否认食物、药物过敏史。",
  "diagnosis": "支气管哮喘",
  "treatment_plan": [
    "检查:心脏电生理:心电图(十二导联心电图)",
    "检验:急诊血常规(五分类)+急诊超敏C反应蛋白、急诊肝功能五项",
    "治疗:静脉采血",
    "盐酸莫西沙星片 0.4g/片 1片/次 qd po (用于治疗AE呼吸道感染)",
    "桉柠蒎肠溶胶囊 0.3g/粒 1粒/次 tid po (用于治疗AE呼吸道感染,化痰)",
    "氯苯那敏片 4mg/片 1片/次 qn po (用于治疗AE呼吸道感染)",
    "泮托拉唑钠肠溶片 40mg/片 1片/次 qd po (用于治疗病史慢性浅表胃炎)",
    "复方氨酚烷胺胶囊 0.25g:0.1g 1粒/次 bid po (用于治疗AE呼吸道感染)",
    "吸入沙丁胺醇气雾剂 400ug once 吸入 (用于支气管扩张检查)",
    "布地奈德福莫特罗粉吸入剂 320ug bid 经口腔吸入 (用于控制哮喘)",
    "硫酸沙丁胺醇气雾剂 100ug pm 经口腔吸入 (控制哮喘急性发作)"
  ]
}
2026-08-05 05:20:57,008 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-12-12]
2026-08-05 05:20:57,011 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1512216, prompt_len=1449
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
2026-08-05 05:21:09,034 INFO     29 [qwen-vl-text] coord API raw response (len=2260):
[
	{"text": "科室:呼吸与危重症医学科", "bbox": [106, 20, 338, 39]},
	{"text": "门诊", "bbox": [511, 20, 564, 39]},
	{"text": "姓名", "bbox": [106, 50, 138, 68]},
	{"text": "联系", "bbox": [511, 50, 555, 68]},
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
	{"text": "检验检查:无", "bbox": [103, 718, 229, 738]},
	{"text": "初步诊断:支气管哮喘", "bbox": [103, 745, 320, 765]},
	{"text": "处理:检查:心脏电生理:心电图(十二导联心电图);", "bbox": [174, 772, 668, 791]},
	{"text": "检验:急诊血常规(五分类)+急诊超敏C反应蛋白、急诊肝功能五项", "bbox": [203, 798, 862, 818]},
	{"text": "治疗:静脉采血", "bbox": [203, 825, 349, 844]},
	{"text": "第1页", "bbox": [471, 858, 535, 876]}
]
2026-08-05 05:21:09,034 INFO     29 [qwen-vl-text] coord API: raw_items=35, valid_items=35, elapsed=12.0s
2026-08-05 05:21:09,034 INFO     29 [qwen-vl-text] coord item[0]: text=科室:呼吸与危重症医学科, bbox=[106, 20, 338, 39]
2026-08-05 05:21:09,034 INFO     29 [qwen-vl-text] coord item[1]: text=门诊, bbox=[511, 20, 564, 39]
2026-08-05 05:21:09,034 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[106, 50, 138, 68]
2026-08-05 05:21:09,034 INFO     29 [qwen-vl-text] coord item[3]: text=联系, bbox=[511, 50, 555, 68]
2026-08-05 05:21:09,034 INFO     29 [qwen-vl-text] coord item[4]: text=性别:女, bbox=[106, 80, 177, 98]
2026-08-05 05:21:09,034 INFO     29 [qwen-vl-text] coord item[5]: text=年龄:63岁, bbox=[511, 80, 603, 98]
2026-08-05 05:21:09,034 INFO     29 [qwen-vl-text] coord item[6]: text=婚姻状况:其他, bbox=[663, 80, 791, 98]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[7]: text=2024-12-12 09:40 初诊记录, bbox=[103, 127, 379, 146]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[8]: text=主诉:SHR-1905-201 临床试验 V14, bbox=[103, 154, 489, 173]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[9]: text=现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年, bbox=[103, 181, 904, 201]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[10]: text=余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现, bbox=[203, 208, 904, 228]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[11]: text=气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行, bbox=[203, 235, 904, 255]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[12]: text=听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并, bbox=[203, 262, 904, 282]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[13]: text=规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可, bbox=[203, 289, 865, 309]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[14]: text=320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:, bbox=[203, 316, 837, 336]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[15]: text=近日咳嗽咳痰,低烧两天,呼吸道感染。2024.12.02行V14随访, bbox=[270, 343, 904, 363]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[16]: text=因患者发热延迟用药。今日回院用药,留院观察1h。, bbox=[203, 370, 727, 390]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[17]: text=既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。, bbox=[103, 397, 857, 416]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[18]: text=既往病史:, bbox=[203, 424, 307, 443]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[19]: text=1.2022.12.10肝囊肿,持续;, bbox=[203, 451, 478, 470]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[20]: text=2.2023.10.31鼻窦炎,持续;, bbox=[203, 477, 478, 497]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[21]: text=3.2023.10.31双肺良性小结节,持续;, bbox=[203, 504, 569, 524]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[22]: text=4.2023.11.03-2023.12.13,肺肺部感染;, bbox=[203, 531, 582, 550]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[23]: text=5.2024.03.01开始,白细胞数降低1级,持续;, bbox=[203, 557, 659, 577]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[24]: text=6.2024.01.10开始,高脂血症,持续;, bbox=[203, 584, 569, 604]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[25]: text=7.十余年前,慢性浅表胃炎,持续中。, bbox=[203, 611, 578, 630]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[26]: text=过敏史:否认食物、药物过敏史。, bbox=[103, 638, 448, 658]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[27]: text=体格检查收缩压(mmHg):-;舒张压(mmHg):-, bbox=[103, 665, 603, 685]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[28]: text=其他体格检查:未行, bbox=[203, 692, 397, 711]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[29]: text=检验检查:无, bbox=[103, 718, 229, 738]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[30]: text=初步诊断:支气管哮喘, bbox=[103, 745, 320, 765]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[31]: text=处理:检查:心脏电生理:心电图(十二导联心电图);, bbox=[174, 772, 668, 791]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[32]: text=检验:急诊血常规(五分类)+急诊超敏C反应蛋白、急诊肝功能五项, bbox=[203, 798, 862, 818]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[33]: text=治疗:静脉采血, bbox=[203, 825, 349, 844]
2026-08-05 05:21:09,035 INFO     29 [qwen-vl-text] coord item[34]: text=第1页, bbox=[471, 858, 535, 876]
2026-08-05 05:21:09,036 INFO     29 [qwen-vl-text] page=7 — 35/35 coords, api_time=12.0s
2026-08-05 05:21:09,038 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1178711, prompt_len=1413
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共28行）
["科室:呼吸与危重症医学科", "性别:女", "年龄:63岁", "婚姻状况:其他", "2024-12-12 09:40 初诊记录", "无新增 AE,无新增 CM,无临床试验安全性事件。", "呼吸道感染,2024.1127-2024.12.11,中度,与试验药物关系为可能无关", "对试验药物采取的措施为延迟用药,对 AE 采取的措施为药物治疗,肺", "SAE,非 SIE,不因此退出临床试验。", "跟踪 CM:", "1.盐酸莫西沙片,2024.12.02-2024.12.11,持续中,0.4g/片,1片/次,", "qd,po,用于治疗 AE 呼吸道感染。", "2.桉柠蒎肠溶胶囊,2024.12.02-2024.12.11 持续中,0.3g/粒,1粒/次,", "tid,po,用于治疗 AE 呼吸道感染。(化痰)", "3.氯苯那敏片,2024.12.02-2024.12.11,持续中,4mg/片,1片/次,", "qn,po,用于治疗 AE 呼吸道感染。", "4.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po.用于治", "疗病史慢性浅表胃炎。", "5.复方氨酚烷胺胶囊,2024.11.27-2024.12.02,持续中,0.25g:0.1g,1粒", "/次,bid,po,用于治疗 AE 呼吸道感染。", "6.吸入沙丁胺醇气雾剂,2024.12.02-2024.12.02,400ug,吸入,once,用于支", "气管扩张检查。", "CM 跟踪:", "1、布地奈德福莫特罗粉吸入剂,2022.1127 开始,持续使用,", "320ug,bid,经口腔吸入,用于控制哮喘。", "2、硫酸沙丁胺醇气雾剂,2024.03.06 开始,持续中,100ug,pm,经口腔吸", "入,控制哮喘急性发作。", "第2页"]

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
2026-08-05 05:21:26,992 INFO     29 [qwen-vl-text] coord API raw response (len=2774):
[
	{"text": "科室:呼吸与危重症医学科", "bbox": [102, 27, 332, 44]},
	{"text": "性别:女", "bbox": [102, 84, 170, 100]},
	{"text": "年龄:63岁", "bbox": [504, 84, 594, 100], "bbox_2": [504, 84, 594, 100]},
	{"text": "婚姻状况:其他", "bbox": [656, 84, 784, 100], "bbox_2": [656, 84, 784, 100]},
	{"text": "2024-12-12 09:40 初诊记录", "bbox": [96, 129, 372, 147], "bbox_2": [96, 129, 372, 147]},
	{"text": "无新增 AE,无新增 CM,无临床试验安全性事件。", "bbox": [196, 207, 664, 226], "bbox_2": [196, 207, 664, 226]},
	{"text": "呼吸道感染,2024.1127-2024.12.11,中度,与试验药物关系为可能无关", "bbox": [196, 260, 898, 279], "bbox_2": [196, 260, 898, 279]},
	{"text": "对试验药物采取的措施为延迟用药,对 AE 采取的措施为药物治疗,肺", "bbox": [196, 286, 898, 305], "bbox_2": [196, 286, 898, 305]},
	{"text": "SAE,非 SIE,不因此退出临床试验。", "bbox": [196, 312, 531, 331], "bbox_2": [196, 312, 531, 331]},
	{"text": "跟踪 CM:", "bbox": [196, 339, 288, 357], "bbox_2": [196, 339, 288, 357]},
	{"text": "1.盐酸莫西沙片,2024.12.02-2024.12.11,持续中,0.4g/片,1片/次,", "bbox": [196, 365, 830, 384], "bbox_2": [196, 365, 830, 384]},
	{"text": "qd,po,用于治疗 AE 呼吸道感染。", "bbox": [194, 390, 512, 409], "bbox_2": [194, 390, 512, 409]},
	{"text": "2.桉柠蒎肠溶胶囊,2024.12.02-2024.12.11 持续中,0.3g/粒,1粒/次,", "bbox": [194, 416, 827, 436], "bbox_2": [194, 416, 827, 436]},
	{"text": "tid,po,用于治疗 AE 呼吸道感染。(化痰)", "bbox": [194, 442, 591, 461], "bbox_2": [194, 442, 591, 461]},
	{"text": "3.氯苯那敏片,2024.12.02-2024.12.11,持续中,4mg/片,1片/次,", "bbox": [194, 468, 794, 487], "bbox_2": [194, 468, 794, 487]},
	{"text": "qn,po,用于治疗 AE 呼吸道感染。", "bbox": [194, 494, 512, 513], "bbox_2": [194, 494, 512, 513]},
	{"text": "4.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po.用于治", "bbox": [194, 520, 897, 539], "bbox_2": [194, 520, 897, 539]},
	{"text": "疗病史慢性浅表胃炎。", "bbox": [194, 546, 414, 565], "bbox_2": [194, 546, 414, 565]},
	{"text": "5.复方氨酚烷胺胶囊,2024.11.27-2024.12.02,持续中,0.25g:0.1g,1粒", "bbox": [194, 572, 896, 591], "bbox_2": [194, 572, 896, 591]},
	{"text": "/次,bid,po,用于治疗 AE 呼吸道感染。", "bbox": [194, 598, 569, 617], "bbox_2": [194, 598, 569, 617]},
	{"text": "6.吸入沙丁胺醇气雾剂,2024.12.02-2024.12.02,400ug,吸入,once,用于支", "bbox": [194, 624, 896, 643], "bbox_2": [194, 624, 896, 643]},
	{"text": "气管扩张检查。", "bbox": [194, 650, 344, 669], "bbox_2": [194, 650, 344, 669]},
	{"text": "CM 跟踪:", "bbox": [194, 677, 288, 695], "bbox_2": [194, 677, 288, 695]},
	{"text": "1、布地奈德福莫特罗粉吸入剂,2022.1127 开始,持续使用,", "bbox": [194, 703, 768, 722], "bbox_2": [194, 703, 768, 722]},
	{"text": "320ug,bid,经口腔吸入,用于控制哮喘。", "bbox": [194, 729, 581, 748], "bbox_2": [194, 729, 581, 748]},
	{"text": "2、硫酸沙丁胺醇气雾剂,2024.03.06 开始,持续中,100ug,pm,经口腔吸", "bbox": [194, 755, 896, 774], "bbox_2": [194, 755, 896, 774]},
	{"text": "入,控制哮喘急性发作。", "bbox": [194, 781, 435, 799], "bbox_2": [194, 781, 435, 799]},
	{"text": "第2页", "bbox": [460, 843, 524, 860], "bbox_2": [460, 843, 524, 860]}
]
2026-08-05 05:21:26,993 INFO     29 [qwen-vl-text] coord API: raw_items=28, valid_items=28, elapsed=18.0s
2026-08-05 05:21:26,993 INFO     29 [qwen-vl-text] coord item[0]: text=科室:呼吸与危重症医学科, bbox=[102, 27, 332, 44]
2026-08-05 05:21:26,993 INFO     29 [qwen-vl-text] coord item[1]: text=性别:女, bbox=[102, 84, 170, 100]
2026-08-05 05:21:26,993 INFO     29 [qwen-vl-text] coord item[2]: text=年龄:63岁, bbox=[504, 84, 594, 100]
2026-08-05 05:21:26,993 INFO     29 [qwen-vl-text] coord item[3]: text=婚姻状况:其他, bbox=[656, 84, 784, 100]
2026-08-05 05:21:26,993 INFO     29 [qwen-vl-text] coord item[4]: text=2024-12-12 09:40 初诊记录, bbox=[96, 129, 372, 147]
2026-08-05 05:21:26,993 INFO     29 [qwen-vl-text] coord item[5]: text=无新增 AE,无新增 CM,无临床试验安全性事件。, bbox=[196, 207, 664, 226]
2026-08-05 05:21:26,993 INFO     29 [qwen-vl-text] coord item[6]: text=呼吸道感染,2024.1127-2024.12.11,中度,与试验药物关系为可能无关, bbox=[196, 260, 898, 279]
2026-08-05 05:21:26,993 INFO     29 [qwen-vl-text] coord item[7]: text=对试验药物采取的措施为延迟用药,对 AE 采取的措施为药物治疗,肺, bbox=[196, 286, 898, 305]
2026-08-05 05:21:26,993 INFO     29 [qwen-vl-text] coord item[8]: text=SAE,非 SIE,不因此退出临床试验。, bbox=[196, 312, 531, 331]
2026-08-05 05:21:26,993 INFO     29 [qwen-vl-text] coord item[9]: text=跟踪 CM:, bbox=[196, 339, 288, 357]
2026-08-05 05:21:26,993 INFO     29 [qwen-vl-text] coord item[10]: text=1.盐酸莫西沙片,2024.12.02-2024.12.11,持续中,0.4g/片,1片/次,, bbox=[196, 365, 830, 384]
2026-08-05 05:21:26,993 INFO     29 [qwen-vl-text] coord item[11]: text=qd,po,用于治疗 AE 呼吸道感染。, bbox=[194, 390, 512, 409]
2026-08-05 05:21:26,993 INFO     29 [qwen-vl-text] coord item[12]: text=2.桉柠蒎肠溶胶囊,2024.12.02-2024.12.11 持续中,0.3g/粒,1粒/次,, bbox=[194, 416, 827, 436]
2026-08-05 05:21:26,993 INFO     29 [qwen-vl-text] coord item[13]: text=tid,po,用于治疗 AE 呼吸道感染。(化痰), bbox=[194, 442, 591, 461]
2026-08-05 05:21:26,994 INFO     29 [qwen-vl-text] coord item[14]: text=3.氯苯那敏片,2024.12.02-2024.12.11,持续中,4mg/片,1片/次,, bbox=[194, 468, 794, 487]
2026-08-05 05:21:26,994 INFO     29 [qwen-vl-text] coord item[15]: text=qn,po,用于治疗 AE 呼吸道感染。, bbox=[194, 494, 512, 513]
2026-08-05 05:21:26,994 INFO     29 [qwen-vl-text] coord item[16]: text=4.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po.用于治, bbox=[194, 520, 897, 539]
2026-08-05 05:21:26,994 INFO     29 [qwen-vl-text] coord item[17]: text=疗病史慢性浅表胃炎。, bbox=[194, 546, 414, 565]
2026-08-05 05:21:26,994 INFO     29 [qwen-vl-text] coord item[18]: text=5.复方氨酚烷胺胶囊,2024.11.27-2024.12.02,持续中,0.25g:0.1g,1粒, bbox=[194, 572, 896, 591]
2026-08-05 05:21:26,994 INFO     29 [qwen-vl-text] coord item[19]: text=/次,bid,po,用于治疗 AE 呼吸道感染。, bbox=[194, 598, 569, 617]
2026-08-05 05:21:26,994 INFO     29 [qwen-vl-text] coord item[20]: text=6.吸入沙丁胺醇气雾剂,2024.12.02-2024.12.02,400ug,吸入,once,用于支, bbox=[194, 624, 896, 643]
2026-08-05 05:21:26,994 INFO     29 [qwen-vl-text] coord item[21]: text=气管扩张检查。, bbox=[194, 650, 344, 669]
2026-08-05 05:21:26,994 INFO     29 [qwen-vl-text] coord item[22]: text=CM 跟踪:, bbox=[194, 677, 288, 695]
2026-08-05 05:21:26,994 INFO     29 [qwen-vl-text] coord item[23]: text=1、布地奈德福莫特罗粉吸入剂,2022.1127 开始,持续使用,, bbox=[194, 703, 768, 722]
2026-08-05 05:21:26,994 INFO     29 [qwen-vl-text] coord item[24]: text=320ug,bid,经口腔吸入,用于控制哮喘。, bbox=[194, 729, 581, 748]
2026-08-05 05:21:26,994 INFO     29 [qwen-vl-text] coord item[25]: text=2、硫酸沙丁胺醇气雾剂,2024.03.06 开始,持续中,100ug,pm,经口腔吸, bbox=[194, 755, 896, 774]
2026-08-05 05:21:26,994 INFO     29 [qwen-vl-text] coord item[26]: text=入,控制哮喘急性发作。, bbox=[194, 781, 435, 799]
2026-08-05 05:21:26,994 INFO     29 [qwen-vl-text] coord item[27]: text=第2页, bbox=[460, 843, 524, 860]
2026-08-05 05:21:26,995 INFO     29 [qwen-vl-text] page=8 — 28/28 coords, api_time=18.0s
2026-08-05 05:21:26,998 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=509416, prompt_len=864
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共16行）
["门诊病历", "科室:呼吸与危重症医学科", "姓名:", "性别:女", "门诊号", "联系方式", "年龄:63岁", "婚姻状况:其他", "2024-12-12 09:40 初诊记录", "处理:", "患者于今日12:21-12:28完成临床试验药物的注射，药物编号为", "Y6077Y4950 用药前完善必要检查后随机用药。", "医师", "门诊病历", "※提醒:复诊时,请携带本病历记录,谢谢!※", "“若有高血压糖尿病诊断,建议您到居住地附近社康中心,建立居民健康档案”"]

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
2026-08-05 05:21:33,509 INFO     29 [qwen-vl-text] coord API raw response (len=899):
[
	{"text": "门诊病历", "bbox": [413, 50, 588, 74]},
	{"text": "科室:呼吸与危重症医学科", "bbox": [85, 84, 326, 100]},
	{"text": "姓名:", "bbox": [85, 112, 264, 129]},
	{"text": "性别:女", "bbox": [87, 142, 157, 158]},
	{"text": "门诊号", "bbox": [506, 84, 590, 100]},
	{"text": "联系方式", "bbox": [506, 112, 588, 129]},
	{"text": "年龄:63岁", "bbox": [507, 142, 603, 158]},
	{"text": "婚姻状况:其他", "bbox": [666, 142, 797, 158]},
	{"text": "2024-12-12 09:40 初诊记录", "bbox": [80, 189, 369, 206]},
	{"text": "处理:", "bbox": [185, 242, 242, 260]},
	{"text": "患者于今日12:21-12:28完成临床试验药物的注射，药物编号为", "bbox": [186, 267, 842, 285]},
	{"text": "Y6077Y4950 用药前完善必要检查后随机用药。", "bbox": [186, 294, 671, 312]},
	{"text": "医师", "bbox": [665, 334, 718, 351]},
	{"text": "门诊病历", "bbox": [98, 380, 334, 401]},
	{"text": "※提醒:复诊时,请携带本病历记录,谢谢!※", "bbox": [87, 457, 595, 475]},
	{"text": "“若有高血压糖尿病诊断,建议您到居住地附近社康中心,建立居民健康档案”", "bbox": [90, 487, 912, 505]}
]
2026-08-05 05:21:33,509 INFO     29 [qwen-vl-text] coord API: raw_items=16, valid_items=16, elapsed=6.5s
2026-08-05 05:21:33,509 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[413, 50, 588, 74]
2026-08-05 05:21:33,509 INFO     29 [qwen-vl-text] coord item[1]: text=科室:呼吸与危重症医学科, bbox=[85, 84, 326, 100]
2026-08-05 05:21:33,509 INFO     29 [qwen-vl-text] coord item[2]: text=姓名:, bbox=[85, 112, 264, 129]
2026-08-05 05:21:33,509 INFO     29 [qwen-vl-text] coord item[3]: text=性别:女, bbox=[87, 142, 157, 158]
2026-08-05 05:21:33,510 INFO     29 [qwen-vl-text] coord item[4]: text=门诊号, bbox=[506, 84, 590, 100]
2026-08-05 05:21:33,510 INFO     29 [qwen-vl-text] coord item[5]: text=联系方式, bbox=[506, 112, 588, 129]
2026-08-05 05:21:33,510 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:63岁, bbox=[507, 142, 603, 158]
2026-08-05 05:21:33,510 INFO     29 [qwen-vl-text] coord item[7]: text=婚姻状况:其他, bbox=[666, 142, 797, 158]
2026-08-05 05:21:33,510 INFO     29 [qwen-vl-text] coord item[8]: text=2024-12-12 09:40 初诊记录, bbox=[80, 189, 369, 206]
2026-08-05 05:21:33,510 INFO     29 [qwen-vl-text] coord item[9]: text=处理:, bbox=[185, 242, 242, 260]
2026-08-05 05:21:33,510 INFO     29 [qwen-vl-text] coord item[10]: text=患者于今日12:21-12:28完成临床试验药物的注射，药物编号为, bbox=[186, 267, 842, 285]
2026-08-05 05:21:33,510 INFO     29 [qwen-vl-text] coord item[11]: text=Y6077Y4950 用药前完善必要检查后随机用药。, bbox=[186, 294, 671, 312]
2026-08-05 05:21:33,510 INFO     29 [qwen-vl-text] coord item[12]: text=医师, bbox=[665, 334, 718, 351]
2026-08-05 05:21:33,510 INFO     29 [qwen-vl-text] coord item[13]: text=门诊病历, bbox=[98, 380, 334, 401]
2026-08-05 05:21:33,510 INFO     29 [qwen-vl-text] coord item[14]: text=※提醒:复诊时,请携带本病历记录,谢谢!※, bbox=[87, 457, 595, 475]
2026-08-05 05:21:33,510 INFO     29 [qwen-vl-text] coord item[15]: text=“若有高血压糖尿病诊断,建议您到居住地附近社康中心,建立居民健康档案”, bbox=[90, 487, 912, 505]
2026-08-05 05:21:33,511 INFO     29 [qwen-vl-text] page=9 — 16/16 coords, api_time=6.5s
2026-08-05 05:21:33,511 INFO     29 [qwen-vl-text] new_positions (79):
[[7, 63.07, 201.10999999999999, 16.84, 32.838], [7, 304.04499999999996, 335.58, 16.84, 32.838], [7, 63.07, 82.11, 42.1, 57.256], [7, 304.04499999999996, 330.22499999999997, 42.1, 57.256], [7, 63.07, 105.315, 67.36, 82.51599999999999], [7, 304.04499999999996, 358.78499999999997, 67.36, 82.51599999999999], [7, 394.48499999999996, 470.645, 67.36, 82.51599999999999], [7, 61.285, 225.505, 106.934, 122.932], [7, 61.285, 290.955, 129.668, 145.666], [7, 61.285, 537.88, 152.402, 169.242], [7, 120.785, 537.88, 175.136, 191.976], [7, 120.785, 537.88, 197.87, 214.70999999999998], [7, 120.785, 537.88, 220.60399999999998, 237.444], [7, 120.785, 514.675, 243.338, 260.178], [7, 120.785, 498.015, 266.072, 282.912], [7, 160.65, 537.88, 288.806, 305.646], [7, 120.785, 432.565, 311.53999999999996, 328.38], [7, 61.285, 509.91499999999996, 334.274, 350.272], [7, 120.785, 182.665, 357.008, 373.006], [7, 120.785, 284.40999999999997, 379.74199999999996, 395.74], [7, 120.785, 284.40999999999997, 401.63399999999996, 418.474], [7, 120.785, 338.555, 424.368, 441.20799999999997], [7, 120.785, 346.28999999999996, 447.102, 463.09999999999997], [7, 120.785, 392.10499999999996, 468.99399999999997, 485.834], [7, 120.785, 338.555, 491.728, 508.568], [7, 120.785, 343.90999999999997, 514.462, 530.46], [7, 61.285, 266.56, 537.196, 554.036], [7, 61.285, 358.78499999999997, 559.93, 576.77], [7, 120.785, 236.215, 582.664, 598.662], [7, 61.285, 136.255, 604.5559999999999, 621.396], [7, 61.285, 190.39999999999998, 627.29, 644.13], [7, 103.53, 397.46, 650.024, 666.0219999999999], [7, 120.785, 512.89, 671.9159999999999, 688.756], [7, 120.785, 207.655, 694.65, 710.648], [7, 280.245, 318.325, 722.4359999999999, 737.592], [8, 60.69, 197.54, 22.733999999999998, 37.048], [8, 60.69, 101.14999999999999, 70.728, 84.2], [8, 299.88, 353.43, 70.728, 84.2], [8, 390.32, 466.47999999999996, 70.728, 84.2], [8, 57.12, 221.34, 108.618, 123.774], [8, 116.61999999999999, 395.08, 174.29399999999998, 190.292], [8, 116.61999999999999, 534.31, 218.92, 234.91799999999998], [8, 116.61999999999999, 534.31, 240.81199999999998, 256.81], [8, 116.61999999999999, 315.945, 262.704, 278.702], [8, 116.61999999999999, 171.35999999999999, 285.438, 300.594], [8, 116.61999999999999, 493.84999999999997, 307.33, 323.328], [8, 115.42999999999999, 304.64, 328.38, 344.378], [8, 115.42999999999999, 492.065, 350.272, 367.11199999999997], [8, 115.42999999999999, 351.645, 372.164, 388.162], [8, 115.42999999999999, 472.43, 394.056, 410.054], [8, 115.42999999999999, 304.64, 415.948, 431.94599999999997], [8, 115.42999999999999, 533.715, 437.84, 453.83799999999997], [8, 115.42999999999999, 246.32999999999998, 459.73199999999997, 475.72999999999996], [8, 115.42999999999999, 533.12, 481.62399999999997, 497.62199999999996], [8, 115.42999999999999, 338.555, 503.51599999999996, 519.514], [8, 115.42999999999999, 533.12, 525.408, 541.406], [8, 115.42999999999999, 204.67999999999998, 547.3, 563.298], [8, 115.42999999999999, 171.35999999999999, 570.034, 585.1899999999999], [8, 115.42999999999999, 456.96, 591.9259999999999, 607.924], [8, 115.42999999999999, 345.695, 613.818, 629.816], [8, 115.42999999999999, 533.12, 635.7099999999999, 651.708], [8, 115.42999999999999, 258.825, 657.602, 672.7579999999999], [8, 273.7, 311.78, 709.8059999999999, 724.12], [9, 245.73499999999999, 349.85999999999996, 42.1, 62.308], [9, 50.574999999999996, 193.97, 70.728, 84.2], [9, 50.574999999999996, 157.07999999999998, 94.304, 108.618], [9, 51.765, 93.41499999999999, 119.564, 133.036], [9, 301.07, 351.05, 70.728, 84.2], [9, 301.07, 349.85999999999996, 94.304, 108.618], [9, 301.66499999999996, 358.78499999999997, 119.564, 133.036], [9, 396.27, 474.215, 119.564, 133.036], [9, 47.599999999999994, 219.55499999999998, 159.138, 173.452], [9, 110.07499999999999, 143.98999999999998, 203.76399999999998, 218.92], [9, 110.67, 500.98999999999995, 224.814, 239.97], [9, 110.67, 399.245, 247.548, 262.704], [9, 395.67499999999995, 427.21, 281.228, 295.542], [9, 58.309999999999995, 198.73, 319.96, 337.642], [9, 51.765, 354.025, 384.794, 399.95], [9, 53.55, 542.64, 410.054, 425.21]]
2026-08-05 05:21:33,511 INFO     29 [qwen-vl-text] ═══ DONE ═══ 79 positions, pages=3, time=47.9s
2026-08-05 05:21:33,511 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:21:33,512 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 05:21:33,512 INFO     29 [qwen-vl-text] positions(93): [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:21:33,512 INFO     29 [qwen-vl-text] page grouping: [10, 11, 12], lines per page: [38, 36, 19]
2026-08-05 05:21:33,857 INFO     29 [qwen-vl-text] page=10, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:21:34,095 INFO     29 [qwen-vl-text] page=11, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:21:34,283 INFO     29 [qwen-vl-text] page=12, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:21:34,286 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1904
2026-08-05 05:21:34,286 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:21:34,286 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 305, \"bbox_end\": 397, \"encounter_dates\": [\"2025-07-31\"], \"department\": \"呼吸与危重症医学科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊病历\n科室:呼吸与危重症医学科\n姓名\n性别:女\n门诊\n联系方式\n年龄:63岁\n婚姻状况:其他\n2025-07-31 17:13 初诊记录\n主诉:SHR-1905V19随访\n现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年\n余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现\n气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行\n听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并\n规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可\n320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:\n20036.。近日无咳嗽咳痰,无胸闷气喘,无发热,无支气管哮喘急性发作\n今日回院行V19随访。\n既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。\n既往病史:\n1.2022.12.10肝囊肿,持续;\n2.2023.10.31鼻窦炎,持续;\n3.2023.10.31双肺良性小结节,持续;\n4.2023.11.03-2023.12.13,肺肺部感染;\n5.2024.03.01开始,白细胞数降低1级,持续;\n6.2024.01.10高脂血症,持续中\n过敏史:否认食物、药物过敏史。\n体格检查收缩压(mmHg):103;舒张压(mmHg):64\n其他体格检查:进行生命体征测量:体温:36.4℃,血压:\n103/64mmHg,呼吸:18次/分,脉搏:76次/分;\n查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见\n皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅\n大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。\n耳廓正常无畸形外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无\n鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿\n第1页\nCS 扫描全能王\n3亿人都在用的扫描App\n门诊病历\n科室:呼吸与危重症医学科\n性别:女\n门诊\n联系方式:\n年龄:63岁\n婚姻状况:其他\n2025-07-31 17:13 初诊记录\n大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中\n肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动\n正常,左肺呼吸音清,未闻及粗干啰音。心律齐。双下肢无水肿。心音正\n常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛、反跳痛,无液\n波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触及,肾脏未触\n及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖器未查、肛门\n直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无异常,其他无\n异常。\n检验检查:已完善试验相关检验检查\n初步诊断:支气管哮喘\n处理:尿常规检查尿隐血,建议定期检查,必要时肾内科就诊。\n无临床试验安全性事,无新增 AE。\n新增合并用药:硫酸沙丁胺醇吸入气雾剂,2025.07.31-\n2025.078.31,400ug,once,吸入,用于支气管扩张检查。\nCM 跟踪:\n1、布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,\n320ug,bid,经口腔吸入,用于控制哮喘。\n2、硫酸沙丁胺醇气雾剂,2024.03.06开始,持续中,100ug,pm,经口腔吸\n入,控制哮喘急性发作。\n3.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po.用于治\n疗病史慢性浅表胃炎。\n处理:\n12025.05.13-2025.07.31 家用峰流速仪使用 ePRO 系统填写依从性大于\n80%,今日已解绑 ePRO 系统。\n2遵从临床试验方案完成 IgE,PK,ADA 采血,完成 ACQ-6,AQLQ 问卷填\n写。\nCS 扫描全能王\n3亿人都在用的扫描App\n门诊病历\n科室:呼吸与危重症医学科\n姓名\n性别:女\n门诊\n联系\n年龄:63岁\n婚姻状况:其他\n2025-07-31 17:13 初诊记录\n3.患者于今日肺功能检查前已停用基础吸入药物布地奈德福莫特罗粉\n吸入剂大于12h,停药时间2025.07.30上午,具体时间不详。\n4.患者已于今日完成随访期随访。\n5.因患者未找到发放万托林,可能已经丢失故不予回收。\n6.嘱患者规律使用吸入药物布地奈德福莫特罗粉吸入剂,药物自备。\n医师\n门诊病历专用章\n※提醒:复诊时,请携带本病历记录,谢谢!※\n“若有高血压糖尿病诊断,建议您到居住地附近社康中心,建立居民健康档案”\n第3页",
    "role": "user"
  }
]
[92m05:21:34 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:21:34,287 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:21:34,288 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:21:34.286+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 16, "failed": 0, "current": {"d7b98bb4908c11f1a3da71efcdd7cc1f": {"id": "d7b98bb4908c11f1a3da71efcdd7cc1f", "doc_id": "d7626528908c11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479738, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785907001430, "task_type": "dataflow", "root_trace_id": "ea6d5499d1eb4a3cabaa8fb5a06c80f8", "root_traceparent": "00-ea6d5499d1eb4a3cabaa8fb5a06c80f8-0f37f835e898f31c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:21:41,141 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:21:41,141 INFO     29 [qwen-vl-text] LLM output (len=887):
{
  "encounter_date": "2025-07-31",
  "chief_complaint": "SHR-1905V19随访",
  "present_illness": "发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:20036。近日无咳嗽咳痰,无胸闷气喘,无发热,无支气管哮喘急性发作。今日回院行V19随访。",
  "past_history": "否认吸烟史、饮酒史。2015年绝经,1988年外院行结扎术。既往病史:1.2022.12.10肝囊肿,持续;2.2023.10.31鼻窦炎,持续;3.2023.10.31双肺良性小结节,持续;4.2023.11.03-2023.12.13,肺部感染;5.2024.03.01开始,白细胞数降低1级,持续;6.2024.01.10高脂血症,持续中。过敏史:否认食物、药物过敏史。",
  "diagnosis": "支气管哮喘",
  "treatment_plan": [
    "尿常规检查尿隐血,建议定期检查,必要时肾内科就诊",
    "硫酸沙丁胺醇吸入气雾剂 400ug once 吸入 (用于支气管扩张检查)",
    "布地奈德福莫特罗粉吸入剂 320ug bid 经口腔吸入 (持续使用,用于控制哮喘)",
    "硫酸沙丁胺醇气雾剂 100ug pm 经口腔吸入 (持续中,控制哮喘急性发作)",
    "泮托拉唑钠肠溶片 40mg/片 1片/次 qd po (持续中,用于治疗病史慢性浅表胃炎)",
    "嘱患者规律使用吸入药物布地奈德福莫特罗粉吸入剂,药物自备"
  ]
}
2026-08-05 05:21:41,141 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-07-31]
2026-08-05 05:21:41,146 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2068148, prompt_len=1579
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共38行）
["门诊病历", "科室:呼吸与危重症医学科", "姓名", "性别:女", "门诊", "联系方式", "年龄:63岁", "婚姻状况:其他", "2025-07-31 17:13 初诊记录", "主诉:SHR-1905V19随访", "现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年", "余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现", "气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行", "听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并", "规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可", "320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:", "20036.。近日无咳嗽咳痰,无胸闷气喘,无发热,无支气管哮喘急性发作", "今日回院行V19随访。", "既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。", "既往病史:", "1.2022.12.10肝囊肿,持续;", "2.2023.10.31鼻窦炎,持续;", "3.2023.10.31双肺良性小结节,持续;", "4.2023.11.03-2023.12.13,肺肺部感染;", "5.2024.03.01开始,白细胞数降低1级,持续;", "6.2024.01.10高脂血症,持续中", "过敏史:否认食物、药物过敏史。", "体格检查收缩压(mmHg):103;舒张压(mmHg):64", "其他体格检查:进行生命体征测量:体温:36.4℃,血压:", "103/64mmHg,呼吸:18次/分,脉搏:76次/分;", "查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见", "皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅", "大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。", "耳廓正常无畸形外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无", "鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿", "第1页", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-05 05:21:54,203 INFO     29 [qwen-vl-text] coord API raw response (len=2513):
[
	{"text": "门诊病历", "bbox": [418, 2, 583, 27]},
	{"text": "科室:呼吸与危重症医学科", "bbox": [114, 35, 339, 53]},
	{"text": "姓名", "bbox": [114, 65, 150, 81]},
	{"text": "性别:女", "bbox": [114, 94, 182, 110]},
	{"text": "门诊", "bbox": [507, 37, 552, 53]},
	{"text": "联系方式", "bbox": [507, 65, 583, 81]},
	{"text": "年龄:63岁", "bbox": [507, 94, 595, 110]},
	{"text": "婚姻状况:其他", "bbox": [655, 94, 779, 110]},
	{"text": "2025-07-31 17:13 初诊记录", "bbox": [110, 140, 379, 158]},
	{"text": "主诉:SHR-1905V19随访", "bbox": [110, 166, 394, 185]},
	{"text": "现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年", "bbox": [108, 192, 891, 211]},
	{"text": "余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现", "bbox": [208, 218, 891, 238]},
	{"text": "气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行", "bbox": [208, 244, 891, 264]},
	{"text": "听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并", "bbox": [208, 270, 891, 290]},
	{"text": "规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可", "bbox": [208, 296, 853, 316]},
	{"text": "320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:", "bbox": [208, 323, 826, 343]},
	{"text": "20036.。近日无咳嗽咳痰,无胸闷气喘,无发热,无支气管哮喘急性发作", "bbox": [208, 349, 891, 368]},
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
	{"text": "体格检查收缩压(mmHg):103;舒张压(mmHg):64", "bbox": [108, 636, 640, 655]},
	{"text": "其他体格检查:进行生命体征测量:体温:36.4℃,血压:", "bbox": [208, 662, 736, 681]},
	{"text": "103/64mmHg,呼吸:18次/分,脉搏:76次/分;", "bbox": [208, 688, 679, 707]},
	{"text": "查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见", "bbox": [208, 714, 891, 733]},
	{"text": "皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅", "bbox": [208, 740, 891, 759]},
	{"text": "大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。", "bbox": [208, 765, 880, 784]},
	{"text": "耳廓正常无畸形外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无", "bbox": [208, 791, 891, 810]},
	{"text": "鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿", "bbox": [208, 817, 891, 836]},
	{"text": "第1页", "bbox": [472, 848, 535, 865]},
	{"text": "CS 扫描全能王", "bbox": [861, 958, 977, 974]},
	{"text": "3亿人都在用的扫描App", "bbox": [861, 978, 977, 987]}
]
2026-08-05 05:21:54,204 INFO     29 [qwen-vl-text] coord API: raw_items=38, valid_items=38, elapsed=13.1s
2026-08-05 05:21:54,204 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[418, 2, 583, 27]
2026-08-05 05:21:54,204 INFO     29 [qwen-vl-text] coord item[1]: text=科室:呼吸与危重症医学科, bbox=[114, 35, 339, 53]
2026-08-05 05:21:54,204 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[114, 65, 150, 81]
2026-08-05 05:21:54,204 INFO     29 [qwen-vl-text] coord item[3]: text=性别:女, bbox=[114, 94, 182, 110]
2026-08-05 05:21:54,204 INFO     29 [qwen-vl-text] coord item[4]: text=门诊, bbox=[507, 37, 552, 53]
2026-08-05 05:21:54,204 INFO     29 [qwen-vl-text] coord item[5]: text=联系方式, bbox=[507, 65, 583, 81]
2026-08-05 05:21:54,204 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:63岁, bbox=[507, 94, 595, 110]
2026-08-05 05:21:54,205 INFO     29 [qwen-vl-text] coord item[7]: text=婚姻状况:其他, bbox=[655, 94, 779, 110]
2026-08-05 05:21:54,205 INFO     29 [qwen-vl-text] coord item[8]: text=2025-07-31 17:13 初诊记录, bbox=[110, 140, 379, 158]
2026-08-05 05:21:54,205 INFO     29 [qwen-vl-text] coord item[9]: text=主诉:SHR-1905V19随访, bbox=[110, 166, 394, 185]
2026-08-05 05:21:54,205 INFO     29 [qwen-vl-text] coord item[10]: text=现病史:发作性喘息,诊断支气管哮喘2年余,起始信必可160ug bid吸入,1年, bbox=[108, 192, 891, 211]
2026-08-05 05:21:54,205 INFO     29 [qwen-vl-text] coord item[11]: text=余前因急性发作外院改用320ug bid吸入。平时平路快走或爬楼梯出现, bbox=[208, 218, 891, 238]
2026-08-05 05:21:54,205 INFO     29 [qwen-vl-text] coord item[12]: text=气促。1月前有咳嗽,白痰,咽喉部黏着感,快走诱发气促,严重时可自行, bbox=[208, 244, 891, 264]
2026-08-05 05:21:54,205 INFO     29 [qwen-vl-text] coord item[13]: text=听到喘鸣音,休息可部分缓解。偶需加吸信必可。予口服激素等治疗并, bbox=[208, 270, 891, 290]
2026-08-05 05:21:54,205 INFO     29 [qwen-vl-text] coord item[14]: text=规律使用信必可320ug bid后症状缓解。2023.11.03规律使用信必可, bbox=[208, 296, 853, 316]
2026-08-05 05:21:54,205 INFO     29 [qwen-vl-text] coord item[15]: text=320ug bid,2024.03.21进行SHR-1905-201试验随机,分配随机号:, bbox=[208, 323, 826, 343]
2026-08-05 05:21:54,205 INFO     29 [qwen-vl-text] coord item[16]: text=20036.。近日无咳嗽咳痰,无胸闷气喘,无发热,无支气管哮喘急性发作, bbox=[208, 349, 891, 368]
2026-08-05 05:21:54,205 INFO     29 [qwen-vl-text] coord item[17]: text=今日回院行V19随访。, bbox=[208, 375, 426, 394]
2026-08-05 05:21:54,205 INFO     29 [qwen-vl-text] coord item[18]: text=既往史:否认吸烟史、饮酒史。2015.UK.UK绝经,1988年外院行结扎术。, bbox=[108, 401, 845, 420]
2026-08-05 05:21:54,205 INFO     29 [qwen-vl-text] coord item[19]: text=既往病史:, bbox=[208, 427, 308, 446]
2026-08-05 05:21:54,205 INFO     29 [qwen-vl-text] coord item[20]: text=1.2022.12.10肝囊肿,持续;, bbox=[208, 453, 476, 472]
2026-08-05 05:21:54,205 INFO     29 [qwen-vl-text] coord item[21]: text=2.2023.10.31鼻窦炎,持续;, bbox=[208, 479, 476, 498]
2026-08-05 05:21:54,205 INFO     29 [qwen-vl-text] coord item[22]: text=3.2023.10.31双肺良性小结节,持续;, bbox=[208, 505, 565, 524]
2026-08-05 05:21:54,206 INFO     29 [qwen-vl-text] coord item[23]: text=4.2023.11.03-2023.12.13,肺肺部感染;, bbox=[208, 531, 577, 550]
2026-08-05 05:21:54,206 INFO     29 [qwen-vl-text] coord item[24]: text=5.2024.03.01开始,白细胞数降低1级,持续;, bbox=[208, 557, 653, 576]
2026-08-05 05:21:54,206 INFO     29 [qwen-vl-text] coord item[25]: text=6.2024.01.10高脂血症,持续中, bbox=[208, 583, 513, 602]
2026-08-05 05:21:54,206 INFO     29 [qwen-vl-text] coord item[26]: text=过敏史:否认食物、药物过敏史。, bbox=[108, 610, 448, 629]
2026-08-05 05:21:54,207 INFO     29 [qwen-vl-text] coord item[27]: text=体格检查收缩压(mmHg):103;舒张压(mmHg):64, bbox=[108, 636, 640, 655]
2026-08-05 05:21:54,207 INFO     29 [qwen-vl-text] coord item[28]: text=其他体格检查:进行生命体征测量:体温:36.4℃,血压:, bbox=[208, 662, 736, 681]
2026-08-05 05:21:54,207 INFO     29 [qwen-vl-text] coord item[29]: text=103/64mmHg,呼吸:18次/分,脉搏:76次/分;, bbox=[208, 688, 679, 707]
2026-08-05 05:21:54,207 INFO     29 [qwen-vl-text] coord item[30]: text=查体:一般情况良好,神志清楚,查体合作。全身皮肤黏膜色泽正常,未见, bbox=[208, 714, 891, 733]
2026-08-05 05:21:54,207 INFO     29 [qwen-vl-text] coord item[31]: text=皮疹,下腹部正中可见长约2cm瘢痕;全身浅表淋巴结未扪及肿大。头颅, bbox=[208, 740, 891, 759]
2026-08-05 05:21:54,207 INFO     29 [qwen-vl-text] coord item[32]: text=大小正常无畸形。眼睑正常,结膜正常,巩膜无黄染,对光反射正常。, bbox=[208, 765, 880, 784]
2026-08-05 05:21:54,207 INFO     29 [qwen-vl-text] coord item[33]: text=耳廓正常无畸形外耳道未见分泌物,乳突无压痛。鼻外观正常无畸形,无, bbox=[208, 791, 891, 810]
2026-08-05 05:21:54,207 INFO     29 [qwen-vl-text] coord item[34]: text=鼻翼扇动,副鼻窦体表区无压痛。口唇红润,口腔黏膜正常,扁桃体无肿, bbox=[208, 817, 891, 836]
2026-08-05 05:21:54,208 INFO     29 [qwen-vl-text] coord item[35]: text=第1页, bbox=[472, 848, 535, 865]
2026-08-05 05:21:54,208 INFO     29 [qwen-vl-text] coord item[36]: text=CS 扫描全能王, bbox=[861, 958, 977, 974]
2026-08-05 05:21:54,208 INFO     29 [qwen-vl-text] coord item[37]: text=3亿人都在用的扫描App, bbox=[861, 978, 977, 987]
2026-08-05 05:21:54,209 INFO     29 [qwen-vl-text] page=10 — 38/38 coords, api_time=13.1s
2026-08-05 05:21:54,213 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1658218, prompt_len=1488
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共36行）
["门诊病历", "科室:呼吸与危重症医学科", "性别:女", "门诊", "联系方式:", "年龄:63岁", "婚姻状况:其他", "2025-07-31 17:13 初诊记录", "大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中", "肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动", "正常,左肺呼吸音清,未闻及粗干啰音。心律齐。双下肢无水肿。心音正", "常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛、反跳痛,无液", "波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触及,肾脏未触", "及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖器未查、肛门", "直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无异常,其他无", "异常。", "检验检查:已完善试验相关检验检查", "初步诊断:支气管哮喘", "处理:尿常规检查尿隐血,建议定期检查,必要时肾内科就诊。", "无临床试验安全性事,无新增 AE。", "新增合并用药:硫酸沙丁胺醇吸入气雾剂,2025.07.31-", "2025.078.31,400ug,once,吸入,用于支气管扩张检查。", "CM 跟踪:", "1、布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,", "320ug,bid,经口腔吸入,用于控制哮喘。", "2、硫酸沙丁胺醇气雾剂,2024.03.06开始,持续中,100ug,pm,经口腔吸", "入,控制哮喘急性发作。", "3.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po.用于治", "疗病史慢性浅表胃炎。", "处理:", "12025.05.13-2025.07.31 家用峰流速仪使用 ePRO 系统填写依从性大于", "80%,今日已解绑 ePRO 系统。", "2遵从临床试验方案完成 IgE,PK,ADA 采血,完成 ACQ-6,AQLQ 问卷填", "写。", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-05 05:22:07,675 INFO     29 [qwen-vl-text] coord API raw response (len=2341):
[
	{"text": "门诊病历", "bbox": [407, 20, 583, 45]},
	{"text": "科室:呼吸与危重症医学科", "bbox": [76, 55, 319, 72]},
	{"text": "性别:女", "bbox": [76, 114, 150, 130]},
	{"text": "门诊", "bbox": [500, 55, 554, 72]},
	{"text": "联系方式:", "bbox": [500, 84, 588, 101]},
	{"text": "年龄:63岁", "bbox": [500, 114, 595, 130]},
	{"text": "婚姻状况:其他", "bbox": [660, 114, 793, 130]},
	{"text": "2025-07-31 17:13 初诊记录", "bbox": [70, 161, 359, 179]},
	{"text": "大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中", "bbox": [174, 188, 912, 207]},
	{"text": "肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动", "bbox": [174, 214, 912, 234]},
	{"text": "正常,左肺呼吸音清,未闻及粗干啰音。心律齐。双下肢无水肿。心音正", "bbox": [174, 240, 912, 260]},
	{"text": "常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛、反跳痛,无液", "bbox": [174, 266, 912, 286]},
	{"text": "波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触及,肾脏未触", "bbox": [174, 292, 912, 312]},
	{"text": "及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖器未查、肛门", "bbox": [174, 319, 912, 340]},
	{"text": "直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无异常,其他无", "bbox": [174, 346, 912, 366]},
	{"text": "异常。", "bbox": [174, 378, 234, 397]},
	{"text": "检验检查:已完善试验相关检验检查", "bbox": [67, 405, 444, 424]},
	{"text": "初步诊断:支气管哮喘", "bbox": [67, 432, 295, 451]},
	{"text": "处理:尿常规检查尿隐血,建议定期检查,必要时肾内科就诊。", "bbox": [67, 460, 772, 479]},
	{"text": "无临床试验安全性事,无新增 AE。", "bbox": [172, 487, 541, 506]},
	{"text": "新增合并用药:硫酸沙丁胺醇吸入气雾剂,2025.07.31-", "bbox": [172, 514, 758, 534]},
	{"text": "2025.078.31,400ug,once,吸入,用于支气管扩张检查。", "bbox": [172, 540, 763, 560]},
	{"text": "CM 跟踪:", "bbox": [172, 568, 273, 587]},
	{"text": "1、布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,", "bbox": [172, 595, 780, 615]},
	{"text": "320ug,bid,经口腔吸入,用于控制哮喘。", "bbox": [172, 622, 583, 642]},
	{"text": "2、硫酸沙丁胺醇气雾剂,2024.03.06开始,持续中,100ug,pm,经口腔吸", "bbox": [172, 650, 912, 670]},
	{"text": "入,控制哮喘急性发作。", "bbox": [172, 677, 430, 696]},
	{"text": "3.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po.用于治", "bbox": [172, 704, 912, 724]},
	{"text": "疗病史慢性浅表胃炎。", "bbox": [172, 731, 405, 750]},
	{"text": "处理:", "bbox": [172, 759, 227, 778]},
	{"text": "12025.05.13-2025.07.31 家用峰流速仪使用 ePRO 系统填写依从性大于", "bbox": [172, 786, 895, 806]},
	{"text": "80%,今日已解绑 ePRO 系统。", "bbox": [172, 813, 495, 833]},
	{"text": "2遵从临床试验方案完成 IgE,PK,ADA 采血,完成 ACQ-6,AQLQ 问卷填", "bbox": [172, 840, 912, 860]},
	{"text": "写。", "bbox": [172, 867, 203, 887]},
	{"text": "CS 扫描全能王", "bbox": [861, 958, 977, 974]},
	{"text": "3亿人都在用的扫描App", "bbox": [861, 977, 976, 986]}
]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=13.5s
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[407, 20, 583, 45]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[1]: text=科室:呼吸与危重症医学科, bbox=[76, 55, 319, 72]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[2]: text=性别:女, bbox=[76, 114, 150, 130]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[3]: text=门诊, bbox=[500, 55, 554, 72]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[4]: text=联系方式:, bbox=[500, 84, 588, 101]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[5]: text=年龄:63岁, bbox=[500, 114, 595, 130]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[6]: text=婚姻状况:其他, bbox=[660, 114, 793, 130]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[7]: text=2025-07-31 17:13 初诊记录, bbox=[70, 161, 359, 179]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[8]: text=大,咽正常无充血。声音正常。颈部无抵抗,颈动脉搏动正常,气管居中, bbox=[174, 188, 912, 207]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[9]: text=肝颈静脉回流征阴性,甲状腺无肿大。胸廓正常,胸骨无叩痛。呼吸运动, bbox=[174, 214, 912, 234]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[10]: text=正常,左肺呼吸音清,未闻及粗干啰音。心律齐。双下肢无水肿。心音正, bbox=[174, 240, 912, 260]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[11]: text=常,未闻及杂音,未闻及心包摩擦音。腹部柔软,无压痛、反跳痛,无液, bbox=[174, 266, 912, 286]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[12]: text=波震颤,未触及腹部包块,肝脏肋下未触及,脾脏肋下未触及,肾脏未触, bbox=[174, 292, 912, 312]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[13]: text=及,Murphy 征阴性,移动性浊音阴性,肠鸣音正常。外生殖器未查、肛门, bbox=[174, 319, 912, 340]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[14]: text=直肠未查。脊柱正常,活动度正常。脊柱四肢、神经系统无异常,其他无, bbox=[174, 346, 912, 366]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[15]: text=异常。, bbox=[174, 378, 234, 397]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[16]: text=检验检查:已完善试验相关检验检查, bbox=[67, 405, 444, 424]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[17]: text=初步诊断:支气管哮喘, bbox=[67, 432, 295, 451]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[18]: text=处理:尿常规检查尿隐血,建议定期检查,必要时肾内科就诊。, bbox=[67, 460, 772, 479]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[19]: text=无临床试验安全性事,无新增 AE。, bbox=[172, 487, 541, 506]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[20]: text=新增合并用药:硫酸沙丁胺醇吸入气雾剂,2025.07.31-, bbox=[172, 514, 758, 534]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[21]: text=2025.078.31,400ug,once,吸入,用于支气管扩张检查。, bbox=[172, 540, 763, 560]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[22]: text=CM 跟踪:, bbox=[172, 568, 273, 587]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[23]: text=1、布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,, bbox=[172, 595, 780, 615]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[24]: text=320ug,bid,经口腔吸入,用于控制哮喘。, bbox=[172, 622, 583, 642]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[25]: text=2、硫酸沙丁胺醇气雾剂,2024.03.06开始,持续中,100ug,pm,经口腔吸, bbox=[172, 650, 912, 670]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[26]: text=入,控制哮喘急性发作。, bbox=[172, 677, 430, 696]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[27]: text=3.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po.用于治, bbox=[172, 704, 912, 724]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[28]: text=疗病史慢性浅表胃炎。, bbox=[172, 731, 405, 750]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[29]: text=处理:, bbox=[172, 759, 227, 778]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[30]: text=12025.05.13-2025.07.31 家用峰流速仪使用 ePRO 系统填写依从性大于, bbox=[172, 786, 895, 806]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[31]: text=80%,今日已解绑 ePRO 系统。, bbox=[172, 813, 495, 833]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[32]: text=2遵从临床试验方案完成 IgE,PK,ADA 采血,完成 ACQ-6,AQLQ 问卷填, bbox=[172, 840, 912, 860]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[33]: text=写。, bbox=[172, 867, 203, 887]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[34]: text=CS 扫描全能王, bbox=[861, 958, 977, 974]
2026-08-05 05:22:07,676 INFO     29 [qwen-vl-text] coord item[35]: text=3亿人都在用的扫描App, bbox=[861, 977, 976, 986]
2026-08-05 05:22:07,677 INFO     29 [qwen-vl-text] page=11 — 36/36 coords, api_time=13.5s
2026-08-05 05:22:07,678 INFO     29 [qwen-vl-text] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=939736, prompt_len=953
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共19行）
["门诊病历", "科室:呼吸与危重症医学科", "姓名", "性别:女", "门诊", "联系", "年龄:63岁", "婚姻状况:其他", "2025-07-31 17:13 初诊记录", "3.患者于今日肺功能检查前已停用基础吸入药物布地奈德福莫特罗粉", "吸入剂大于12h,停药时间2025.07.30上午,具体时间不详。", "4.患者已于今日完成随访期随访。", "5.因患者未找到发放万托林,可能已经丢失故不予回收。", "6.嘱患者规律使用吸入药物布地奈德福莫特罗粉吸入剂,药物自备。", "医师", "门诊病历专用章", "※提醒:复诊时,请携带本病历记录,谢谢!※", "“若有高血压糖尿病诊断,建议您到居住地附近社康中心,建立居民健康档案”", "第3页"]

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
2026-08-05 05:22:13,835 INFO     29 [qwen-vl-text] coord API raw response (len=1108):
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
	{"text": "3.患者于今日肺功能检查前已停用基础吸入药物布地奈德福莫特罗粉", "bbox": [192, 187, 899, 205]},
	{"text": "吸入剂大于12h,停药时间2025.07.30上午,具体时间不详。", "bbox": [192, 211, 795, 230]},
	{"text": "4.患者已于今日完成随访期随访。", "bbox": [192, 238, 534, 257]},
	{"text": "5.因患者未找到发放万托林,可能已经丢失故不予回收。", "bbox": [192, 264, 769, 283]},
	{"text": "6.嘱患者规律使用吸入药物布地奈德福莫特罗粉吸入剂,药物自备。", "bbox": [192, 290, 888, 309]},
	{"text": "医师", "bbox": [668, 382, 721, 400]},
	{"text": "门诊病历专用章", "bbox": [104, 423, 337, 448]},
	{"text": "※提醒:复诊时,请携带本病历记录,谢谢!※", "bbox": [95, 502, 597, 520]},
	{"text": "“若有高血压糖尿病诊断,建议您到居住地附近社康中心,建立居民健康档案”", "bbox": [98, 531, 911, 550]},
	{"text": "第3页", "bbox": [466, 867, 531, 884]}
]
2026-08-05 05:22:13,835 INFO     29 [qwen-vl-text] coord API: raw_items=19, valid_items=19, elapsed=6.2s
2026-08-05 05:22:13,835 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[417, 28, 592, 52]
2026-08-05 05:22:13,835 INFO     29 [qwen-vl-text] coord item[1]: text=科室:呼吸与危重症医学科, bbox=[93, 60, 333, 77]
2026-08-05 05:22:13,835 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[93, 87, 115, 104]
2026-08-05 05:22:13,835 INFO     29 [qwen-vl-text] coord item[3]: text=性别:女, bbox=[93, 115, 164, 132]
2026-08-05 05:22:13,835 INFO     29 [qwen-vl-text] coord item[4]: text=门诊, bbox=[512, 60, 564, 77]
2026-08-05 05:22:13,835 INFO     29 [qwen-vl-text] coord item[5]: text=联系, bbox=[512, 87, 552, 104]
2026-08-05 05:22:13,835 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:63岁, bbox=[512, 115, 604, 132]
2026-08-05 05:22:13,835 INFO     29 [qwen-vl-text] coord item[7]: text=婚姻状况:其他, bbox=[668, 115, 797, 132]
2026-08-05 05:22:13,835 INFO     29 [qwen-vl-text] coord item[8]: text=2025-07-31 17:13 初诊记录, bbox=[90, 161, 375, 179]
2026-08-05 05:22:13,835 INFO     29 [qwen-vl-text] coord item[9]: text=3.患者于今日肺功能检查前已停用基础吸入药物布地奈德福莫特罗粉, bbox=[192, 187, 899, 205]
2026-08-05 05:22:13,835 INFO     29 [qwen-vl-text] coord item[10]: text=吸入剂大于12h,停药时间2025.07.30上午,具体时间不详。, bbox=[192, 211, 795, 230]
2026-08-05 05:22:13,835 INFO     29 [qwen-vl-text] coord item[11]: text=4.患者已于今日完成随访期随访。, bbox=[192, 238, 534, 257]
2026-08-05 05:22:13,835 INFO     29 [qwen-vl-text] coord item[12]: text=5.因患者未找到发放万托林,可能已经丢失故不予回收。, bbox=[192, 264, 769, 283]
2026-08-05 05:22:13,835 INFO     29 [qwen-vl-text] coord item[13]: text=6.嘱患者规律使用吸入药物布地奈德福莫特罗粉吸入剂,药物自备。, bbox=[192, 290, 888, 309]
2026-08-05 05:22:13,835 INFO     29 [qwen-vl-text] coord item[14]: text=医师, bbox=[668, 382, 721, 400]
2026-08-05 05:22:13,835 INFO     29 [qwen-vl-text] coord item[15]: text=门诊病历专用章, bbox=[104, 423, 337, 448]
2026-08-05 05:22:13,836 INFO     29 [qwen-vl-text] coord item[16]: text=※提醒:复诊时,请携带本病历记录,谢谢!※, bbox=[95, 502, 597, 520]
2026-08-05 05:22:13,836 INFO     29 [qwen-vl-text] coord item[17]: text=“若有高血压糖尿病诊断,建议您到居住地附近社康中心,建立居民健康档案”, bbox=[98, 531, 911, 550]
2026-08-05 05:22:13,836 INFO     29 [qwen-vl-text] coord item[18]: text=第3页, bbox=[466, 867, 531, 884]
2026-08-05 05:22:13,836 INFO     29 [qwen-vl-text] page=12 — 19/19 coords, api_time=6.2s
2026-08-05 05:22:13,836 INFO     29 [qwen-vl-text] new_positions (93):
[[10, 248.70999999999998, 346.885, 1.684, 22.733999999999998], [10, 67.83, 201.70499999999998, 29.47, 44.626], [10, 67.83, 89.25, 54.73, 68.202], [10, 67.83, 108.28999999999999, 79.148, 92.61999999999999], [10, 301.66499999999996, 328.44, 31.154, 44.626], [10, 301.66499999999996, 346.885, 54.73, 68.202], [10, 301.66499999999996, 354.025, 79.148, 92.61999999999999], [10, 389.72499999999997, 463.505, 79.148, 92.61999999999999], [10, 65.45, 225.505, 117.88, 133.036], [10, 65.45, 234.42999999999998, 139.772, 155.76999999999998], [10, 64.25999999999999, 530.145, 161.664, 177.662], [10, 123.75999999999999, 530.145, 183.55599999999998, 200.396], [10, 123.75999999999999, 530.145, 205.44799999999998, 222.28799999999998], [10, 123.75999999999999, 530.145, 227.34, 244.17999999999998], [10, 123.75999999999999, 507.53499999999997, 249.232, 266.072], [10, 123.75999999999999, 491.46999999999997, 271.966, 288.806], [10, 123.75999999999999, 530.145, 293.858, 309.856], [10, 123.75999999999999, 253.47, 315.75, 331.748], [10, 64.25999999999999, 502.775, 337.642, 353.64], [10, 123.75999999999999, 183.26, 359.534, 375.532], [10, 123.75999999999999, 283.21999999999997, 381.426, 397.424], [10, 123.75999999999999, 283.21999999999997, 403.318, 419.316], [10, 123.75999999999999, 336.175, 425.21, 441.20799999999997], [10, 123.75999999999999, 343.315, 447.102, 463.09999999999997], [10, 123.75999999999999, 388.53499999999997, 468.99399999999997, 484.99199999999996], [10, 123.75999999999999, 305.235, 490.88599999999997, 506.88399999999996], [10, 64.25999999999999, 266.56, 513.62, 529.6179999999999], [10, 64.25999999999999, 380.79999999999995, 535.512, 551.51], [10, 123.75999999999999, 437.91999999999996, 557.404, 573.4019999999999], [10, 123.75999999999999, 404.005, 579.2959999999999, 595.294], [10, 123.75999999999999, 530.145, 601.188, 617.1859999999999], [10, 123.75999999999999, 530.145, 623.0799999999999, 639.078], [10, 123.75999999999999, 523.6, 644.13, 660.1279999999999], [10, 123.75999999999999, 530.145, 666.0219999999999, 682.02], [10, 123.75999999999999, 530.145, 687.914, 703.9119999999999], [10, 280.84, 318.325, 714.016, 728.3299999999999], [10, 512.295, 581.3149999999999, 806.636, 820.108], [10, 512.295, 581.3149999999999, 823.476, 831.054], [11, 242.165, 346.885, 16.84, 37.89], [11, 45.22, 189.80499999999998, 46.309999999999995, 60.623999999999995], [11, 45.22, 89.25, 95.988, 109.46], [11, 297.5, 329.63, 46.309999999999995, 60.623999999999995], [11, 297.5, 349.85999999999996, 70.728, 85.042], [11, 297.5, 354.025, 95.988, 109.46], [11, 392.7, 471.835, 95.988, 109.46], [11, 41.65, 213.605, 135.56199999999998, 150.718], [11, 103.53, 542.64, 158.296, 174.29399999999998], [11, 103.53, 542.64, 180.188, 197.028], [11, 103.53, 542.64, 202.07999999999998, 218.92], [11, 103.53, 542.64, 223.97199999999998, 240.81199999999998], [11, 103.53, 542.64, 245.864, 262.704], [11, 103.53, 542.64, 268.598, 286.28], [11, 103.53, 542.64, 291.332, 308.17199999999997], [11, 103.53, 139.23, 318.276, 334.274], [11, 39.864999999999995, 264.18, 341.01, 357.008], [11, 39.864999999999995, 175.525, 363.74399999999997, 379.74199999999996], [11, 39.864999999999995, 459.34, 387.32, 403.318], [11, 102.33999999999999, 321.895, 410.054, 426.05199999999996], [11, 102.33999999999999, 451.01, 432.788, 449.628], [11, 102.33999999999999, 453.98499999999996, 454.68, 471.52], [11, 102.33999999999999, 162.435, 478.256, 494.25399999999996], [11, 102.33999999999999, 464.09999999999997, 500.99, 517.8299999999999], [11, 102.33999999999999, 346.885, 523.7239999999999, 540.564], [11, 102.33999999999999, 542.64, 547.3, 564.14], [11, 102.33999999999999, 255.85, 570.034, 586.0319999999999], [11, 102.33999999999999, 542.64, 592.768, 609.608], [11, 102.33999999999999, 240.975, 615.502, 631.5], [11, 102.33999999999999, 135.065, 639.078, 655.076], [11, 102.33999999999999, 532.525, 661.812, 678.6519999999999], [11, 102.33999999999999, 294.525, 684.5459999999999, 701.386], [11, 102.33999999999999, 542.64, 707.28, 724.12], [11, 102.33999999999999, 120.785, 730.014, 746.8539999999999], [11, 512.295, 581.3149999999999, 806.636, 820.108], [11, 512.295, 580.72, 822.634, 830.212], [12, 248.11499999999998, 352.24, 23.576, 43.784], [12, 55.335, 198.135, 50.519999999999996, 64.834], [12, 55.335, 68.425, 73.25399999999999, 87.568], [12, 55.335, 97.58, 96.83, 111.14399999999999], [12, 304.64, 335.58, 50.519999999999996, 64.834], [12, 304.64, 328.44, 73.25399999999999, 87.568], [12, 304.64, 359.38, 96.83, 111.14399999999999], [12, 397.46, 474.215, 96.83, 111.14399999999999], [12, 53.55, 223.125, 135.56199999999998, 150.718], [12, 114.24, 534.905, 157.454, 172.60999999999999], [12, 114.24, 473.025, 177.662, 193.66], [12, 114.24, 317.72999999999996, 200.396, 216.394], [12, 114.24, 457.555, 222.28799999999998, 238.286], [12, 114.24, 528.36, 244.17999999999998, 260.178], [12, 397.46, 428.995, 321.644, 336.8], [12, 61.879999999999995, 200.515, 356.166, 377.216], [12, 56.525, 355.215, 422.68399999999997, 437.84], [12, 58.309999999999995, 542.045, 447.102, 463.09999999999997], [12, 277.27, 315.945, 730.014, 744.328]]
2026-08-05 05:22:13,836 INFO     29 [qwen-vl-text] ═══ DONE ═══ 93 positions, pages=3, time=40.3s
2026-08-05 05:22:13,836 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:22:13,836 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 05:22:13,836 INFO     29 [qwen-vl-text] positions(37): [[13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:22:13,836 INFO     29 [qwen-vl-text] page grouping: [13], lines per page: [37]
2026-08-05 05:22:14,151 INFO     29 [qwen-vl-text] page=13, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:22:14,154 INFO     29 [qwen-vl-text] LLM extraction start, text_len=783
2026-08-05 05:22:14,154 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:22:14,155 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 398, \"bbox_end\": 434, \"encounter_dates\": [\"2025-10-25\"], \"department\": \"呼吸内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊\n姓名：\n门(急)诊初诊病历\n性别：女\n科室：呼吸内科门诊\n年龄：63岁\n就诊日期：2025-10-25 15:22\n主诉：支气管哮喘复诊\n现病史：患者支气管哮喘复诊，目前规律吸入布地奈德福莫特罗320ug 一次1吸，\n一天2次。目前诉有咳嗽、咳痰，有气促感，无胸闷，无发热，无鼻塞、流涕，无咯\n血、痰中带血，无头痛、头晕、视物旋转，无饮水呛咳，无咽痛、腹痛、腹胀等不\n适。未予处理及就医。现患者为求进一步诊治，故至我院科门诊就医。\n既往史：否认高血压、否认糖尿病、否认冠心病等慢性疾病病史，否认肝炎、结核\n等传染病史，否认手术外伤输血史 过敏史：无食物、药物过敏史。。否认饮酒史。\n个人史：已婚已育\n家族史：否认家族病史。\n体格检查：T：36.8℃ P：87次/分 R：21次/分 BP：108/73mmHg 指脉氧：\n9%。神志清楚，精神尚可，呼吸平顺，口唇无发绀，咽部无充血，扁桃体无肿大，\n双侧颈静脉无怒张，双肺呼吸音粗，双肺可闻及干啰音，双肺未闻及湿性啰音及胸膜\n摩擦音。心率87次/分，律齐，各瓣膜未闻及明显病理性杂音。腹部平软，全腹部无\n玉痛，反跳痛，肠鸣音正常。四肢运动自如，双下肢无水肿。\n辅助检查：患者自行购买布地奈德福莫特罗320ug 一次1吸，一天2次。\n初步诊断：\n西医诊断：1.支气管哮喘(急性发作期)\n处理意见：\n醋酸泼尼松片（国基）(5mg*100片) 20.000mg\n1次/天 口服\n12.00片\n硫酸沙丁胺醇吸入气雾剂（省3、国基）(200揿：\n100μg) 200.000μg\n1次/天 吸入\n1.00瓶\n建议：建议患者结果回报后请及时至我科门诊复诊，若出现病情变化或病情加重\n无好转等，请及时至急诊科门诊复诊。\n温馨提示：1.请妥善保管好病历及各种检查检验报告单。\n2.复诊时，请携带本病历记录，谢谢！\n第1页(共1页)",
    "role": "user"
  }
]
[92m05:22:14 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:22:14,157 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:22:14,157 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:22:14.156+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 16, "failed": 0, "current": {"d7b98bb4908c11f1a3da71efcdd7cc1f": {"id": "d7b98bb4908c11f1a3da71efcdd7cc1f", "doc_id": "d7626528908c11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479738, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785907001430, "task_type": "dataflow", "root_trace_id": "ea6d5499d1eb4a3cabaa8fb5a06c80f8", "root_traceparent": "00-ea6d5499d1eb4a3cabaa8fb5a06c80f8-0f37f835e898f31c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:22:21,088 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:22:21,089 INFO     29 [qwen-vl-text] LLM output (len=486):
{
  "encounter_date": "2025-10-25",
  "chief_complaint": "支气管哮喘复诊",
  "present_illness": "患者支气管哮喘复诊，目前规律吸入布地奈德福莫特罗320ug 一次1吸，一天2次。目前诉有咳嗽、咳痰，有气促感，无胸闷，无发热，无鼻塞、流涕，无咯血、痰中带血，无头痛、头晕、视物旋转，无饮水呛咳，无咽痛、腹痛、腹胀等不适。未予处理及就医。现患者为求进一步诊治，故至我院科门诊就医。",
  "past_history": "否认高血压、否认糖尿病、否认冠心病等慢性疾病病史，否认肝炎、结核等传染病史，否认手术外伤输血史。过敏史：无食物、药物过敏史。否认饮酒史。",
  "diagnosis": "西医诊断：1.支气管哮喘(急性发作期)",
  "treatment_plan": [
    "醋酸泼尼松片（国基）(5mg*100片) 20mg 1次/天 口服 12片",
    "硫酸沙丁胺醇吸入气雾剂（省3、国基）(200揿：100μg) 200μg 1次/天 吸入 1瓶"
  ]
}
2026-08-05 05:22:21,089 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-10-25]
2026-08-05 05:22:21,096 INFO     29 [qwen-vl-text] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2599809, prompt_len=1507
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
2026-08-05 05:22:35,021 INFO     29 [qwen-vl-text] coord API raw response (len=2385):
[
	{"text": "门诊", "bbox": [90, 81, 133, 100]},
	{"text": "姓名：", "bbox": [90, 102, 158, 120]},
	{"text": "门(急)诊初诊病历", "bbox": [347, 90, 606, 113]},
	{"text": "性别：女", "bbox": [645, 104, 723, 120]},
	{"text": "科室：呼吸内科门诊", "bbox": [90, 124, 273, 141]},
	{"text": "年龄：63岁", "bbox": [645, 125, 745, 141]},
	{"text": "就诊日期：2025-10-25 15:22", "bbox": [93, 149, 379, 166]},
	{"text": "主诉：支气管哮喘复诊", "bbox": [93, 168, 312, 185]},
	{"text": "现病史：患者支气管哮喘复诊，目前规律吸入布地奈德福莫特罗320ug 一次1吸，", "bbox": [93, 187, 863, 204]},
	{"text": "一天2次。目前诉有咳嗽、咳痰，有气促感，无胸闷，无发热，无鼻塞、流涕，无咯", "bbox": [90, 206, 886, 223]},
	{"text": "血、痰中带血，无头痛、头晕、视物旋转，无饮水呛咳，无咽痛、腹痛、腹胀等不", "bbox": [90, 225, 874, 242]},
	{"text": "适。未予处理及就医。现患者为求进一步诊治，故至我院科门诊就医。", "bbox": [90, 244, 750, 261]},
	{"text": "既往史：否认高血压、否认糖尿病、否认冠心病等慢性疾病病史，否认肝炎、结核", "bbox": [93, 263, 886, 280]},
	{"text": "等传染病史，否认手术外伤输血史 过敏史：无食物、药物过敏史。。否认饮酒史。", "bbox": [90, 282, 874, 299]},
	{"text": "个人史：已婚已育", "bbox": [93, 301, 269, 318]},
	{"text": "家族史：否认家族病史。", "bbox": [93, 320, 324, 337]},
	{"text": "体格检查：T：36.8℃ P：87次/分 R：21次/分 BP：108/73mmHg 指脉氧：", "bbox": [93, 339, 827, 356]},
	{"text": "9%。神志清楚，精神尚可，呼吸平顺，口唇无发绀，咽部无充血，扁桃体无肿大，", "bbox": [88, 358, 869, 375]},
	{"text": "双侧颈静脉无怒张，双肺呼吸音粗，双肺可闻及干啰音，双肺未闻及湿性啰音及胸膜", "bbox": [88, 377, 889, 394]},
	{"text": "摩擦音。心率87次/分，律齐，各瓣膜未闻及明显病理性杂音。腹部平软，全腹部无", "bbox": [88, 396, 884, 413]},
	{"text": "玉痛，反跳痛，肠鸣音正常。四肢运动自如，双下肢无水肿。", "bbox": [88, 415, 663, 432]},
	{"text": "辅助检查：患者自行购买布地奈德福莫特罗320ug 一次1吸，一天2次。", "bbox": [93, 434, 762, 451]},
	{"text": "初步诊断：", "bbox": [93, 453, 190, 470]},
	{"text": "西医诊断：1.支气管哮喘(急性发作期)", "bbox": [128, 472, 499, 489]},
	{"text": "处理意见：", "bbox": [93, 491, 190, 508]},
	{"text": "醋酸泼尼松片（国基）(5mg*100片) 20.000mg", "bbox": [88, 510, 525, 527]},
	{"text": "1次/天 口服", "bbox": [632, 510, 754, 527]},
	{"text": "12.00片", "bbox": [790, 510, 864, 527]},
	{"text": "硫酸沙丁胺醇吸入气雾剂（省3、国基）(200揿：", "bbox": [88, 529, 543, 546]},
	{"text": "100μg) 200.000μg", "bbox": [88, 548, 285, 565]},
	{"text": "1次/天 吸入", "bbox": [632, 529, 754, 546]},
	{"text": "1.00瓶", "bbox": [790, 529, 855, 546]},
	{"text": "建议：建议患者结果回报后请及时至我科门诊复诊，若出现病情变化或病情加重", "bbox": [90, 640, 882, 657]},
	{"text": "无好转等，请及时至急诊科门诊复诊。", "bbox": [85, 659, 443, 676]},
	{"text": "温馨提示：1.请妥善保管好病历及各种检查检验报告单。", "bbox": [85, 721, 616, 738]},
	{"text": "2.复诊时，请携带本病历记录，谢谢！", "bbox": [188, 743, 551, 760]},
	{"text": "第1页(共1页)", "bbox": [421, 765, 548, 782]}
]
2026-08-05 05:22:35,022 INFO     29 [qwen-vl-text] coord API: raw_items=37, valid_items=37, elapsed=13.9s
2026-08-05 05:22:35,022 INFO     29 [qwen-vl-text] coord item[0]: text=门诊, bbox=[90, 81, 133, 100]
2026-08-05 05:22:35,022 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[90, 102, 158, 120]
2026-08-05 05:22:35,022 INFO     29 [qwen-vl-text] coord item[2]: text=门(急)诊初诊病历, bbox=[347, 90, 606, 113]
2026-08-05 05:22:35,022 INFO     29 [qwen-vl-text] coord item[3]: text=性别：女, bbox=[645, 104, 723, 120]
2026-08-05 05:22:35,022 INFO     29 [qwen-vl-text] coord item[4]: text=科室：呼吸内科门诊, bbox=[90, 124, 273, 141]
2026-08-05 05:22:35,022 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：63岁, bbox=[645, 125, 745, 141]
2026-08-05 05:22:35,022 INFO     29 [qwen-vl-text] coord item[6]: text=就诊日期：2025-10-25 15:22, bbox=[93, 149, 379, 166]
2026-08-05 05:22:35,022 INFO     29 [qwen-vl-text] coord item[7]: text=主诉：支气管哮喘复诊, bbox=[93, 168, 312, 185]
2026-08-05 05:22:35,022 INFO     29 [qwen-vl-text] coord item[8]: text=现病史：患者支气管哮喘复诊，目前规律吸入布地奈德福莫特罗320ug 一次1吸，, bbox=[93, 187, 863, 204]
2026-08-05 05:22:35,022 INFO     29 [qwen-vl-text] coord item[9]: text=一天2次。目前诉有咳嗽、咳痰，有气促感，无胸闷，无发热，无鼻塞、流涕，无咯, bbox=[90, 206, 886, 223]
2026-08-05 05:22:35,022 INFO     29 [qwen-vl-text] coord item[10]: text=血、痰中带血，无头痛、头晕、视物旋转，无饮水呛咳，无咽痛、腹痛、腹胀等不, bbox=[90, 225, 874, 242]
2026-08-05 05:22:35,022 INFO     29 [qwen-vl-text] coord item[11]: text=适。未予处理及就医。现患者为求进一步诊治，故至我院科门诊就医。, bbox=[90, 244, 750, 261]
2026-08-05 05:22:35,022 INFO     29 [qwen-vl-text] coord item[12]: text=既往史：否认高血压、否认糖尿病、否认冠心病等慢性疾病病史，否认肝炎、结核, bbox=[93, 263, 886, 280]
2026-08-05 05:22:35,022 INFO     29 [qwen-vl-text] coord item[13]: text=等传染病史，否认手术外伤输血史 过敏史：无食物、药物过敏史。。否认饮酒史。, bbox=[90, 282, 874, 299]
2026-08-05 05:22:35,022 INFO     29 [qwen-vl-text] coord item[14]: text=个人史：已婚已育, bbox=[93, 301, 269, 318]
2026-08-05 05:22:35,022 INFO     29 [qwen-vl-text] coord item[15]: text=家族史：否认家族病史。, bbox=[93, 320, 324, 337]
2026-08-05 05:22:35,022 INFO     29 [qwen-vl-text] coord item[16]: text=体格检查：T：36.8℃ P：87次/分 R：21次/分 BP：108/73mmHg 指脉氧：, bbox=[93, 339, 827, 356]
2026-08-05 05:22:35,023 INFO     29 [qwen-vl-text] coord item[17]: text=9%。神志清楚，精神尚可，呼吸平顺，口唇无发绀，咽部无充血，扁桃体无肿大，, bbox=[88, 358, 869, 375]
2026-08-05 05:22:35,023 INFO     29 [qwen-vl-text] coord item[18]: text=双侧颈静脉无怒张，双肺呼吸音粗，双肺可闻及干啰音，双肺未闻及湿性啰音及胸膜, bbox=[88, 377, 889, 394]
2026-08-05 05:22:35,023 INFO     29 [qwen-vl-text] coord item[19]: text=摩擦音。心率87次/分，律齐，各瓣膜未闻及明显病理性杂音。腹部平软，全腹部无, bbox=[88, 396, 884, 413]
2026-08-05 05:22:35,023 INFO     29 [qwen-vl-text] coord item[20]: text=玉痛，反跳痛，肠鸣音正常。四肢运动自如，双下肢无水肿。, bbox=[88, 415, 663, 432]
2026-08-05 05:22:35,023 INFO     29 [qwen-vl-text] coord item[21]: text=辅助检查：患者自行购买布地奈德福莫特罗320ug 一次1吸，一天2次。, bbox=[93, 434, 762, 451]
2026-08-05 05:22:35,023 INFO     29 [qwen-vl-text] coord item[22]: text=初步诊断：, bbox=[93, 453, 190, 470]
2026-08-05 05:22:35,023 INFO     29 [qwen-vl-text] coord item[23]: text=西医诊断：1.支气管哮喘(急性发作期), bbox=[128, 472, 499, 489]
2026-08-05 05:22:35,023 INFO     29 [qwen-vl-text] coord item[24]: text=处理意见：, bbox=[93, 491, 190, 508]
2026-08-05 05:22:35,023 INFO     29 [qwen-vl-text] coord item[25]: text=醋酸泼尼松片（国基）(5mg*100片) 20.000mg, bbox=[88, 510, 525, 527]
2026-08-05 05:22:35,023 INFO     29 [qwen-vl-text] coord item[26]: text=1次/天 口服, bbox=[632, 510, 754, 527]
2026-08-05 05:22:35,023 INFO     29 [qwen-vl-text] coord item[27]: text=12.00片, bbox=[790, 510, 864, 527]
2026-08-05 05:22:35,023 INFO     29 [qwen-vl-text] coord item[28]: text=硫酸沙丁胺醇吸入气雾剂（省3、国基）(200揿：, bbox=[88, 529, 543, 546]
2026-08-05 05:22:35,023 INFO     29 [qwen-vl-text] coord item[29]: text=100μg) 200.000μg, bbox=[88, 548, 285, 565]
2026-08-05 05:22:35,023 INFO     29 [qwen-vl-text] coord item[30]: text=1次/天 吸入, bbox=[632, 529, 754, 546]
2026-08-05 05:22:35,023 INFO     29 [qwen-vl-text] coord item[31]: text=1.00瓶, bbox=[790, 529, 855, 546]
2026-08-05 05:22:35,023 INFO     29 [qwen-vl-text] coord item[32]: text=建议：建议患者结果回报后请及时至我科门诊复诊，若出现病情变化或病情加重, bbox=[90, 640, 882, 657]
2026-08-05 05:22:35,023 INFO     29 [qwen-vl-text] coord item[33]: text=无好转等，请及时至急诊科门诊复诊。, bbox=[85, 659, 443, 676]
2026-08-05 05:22:35,023 INFO     29 [qwen-vl-text] coord item[34]: text=温馨提示：1.请妥善保管好病历及各种检查检验报告单。, bbox=[85, 721, 616, 738]
2026-08-05 05:22:35,023 INFO     29 [qwen-vl-text] coord item[35]: text=2.复诊时，请携带本病历记录，谢谢！, bbox=[188, 743, 551, 760]
2026-08-05 05:22:35,023 INFO     29 [qwen-vl-text] coord item[36]: text=第1页(共1页), bbox=[421, 765, 548, 782]
2026-08-05 05:22:35,025 INFO     29 [qwen-vl-text] page=13 — 37/37 coords, api_time=13.9s
2026-08-05 05:22:35,025 INFO     29 [qwen-vl-text] new_positions (37):
[[13, 53.55, 79.13499999999999, 68.202, 84.2], [13, 53.55, 94.00999999999999, 85.884, 101.03999999999999], [13, 206.465, 360.57, 75.78, 95.146], [13, 383.775, 430.185, 87.568, 101.03999999999999], [13, 53.55, 162.435, 104.408, 118.722], [13, 383.775, 443.275, 105.25, 118.722], [13, 55.335, 225.505, 125.458, 139.772], [13, 55.335, 185.64, 141.456, 155.76999999999998], [13, 55.335, 513.485, 157.454, 171.768], [13, 53.55, 527.17, 173.452, 187.766], [13, 53.55, 520.03, 189.45, 203.76399999999998], [13, 53.55, 446.25, 205.44799999999998, 219.762], [13, 55.335, 527.17, 221.446, 235.76], [13, 53.55, 520.03, 237.444, 251.75799999999998], [13, 55.335, 160.055, 253.44199999999998, 267.756], [13, 55.335, 192.78, 269.44, 283.75399999999996], [13, 55.335, 492.065, 285.438, 299.752], [13, 52.36, 517.055, 301.436, 315.75], [13, 52.36, 528.9549999999999, 317.43399999999997, 331.748], [13, 52.36, 525.98, 333.432, 347.746], [13, 52.36, 394.48499999999996, 349.43, 363.74399999999997], [13, 55.335, 453.39, 365.428, 379.74199999999996], [13, 55.335, 113.05, 381.426, 395.74], [13, 76.16, 296.905, 397.424, 411.738], [13, 55.335, 113.05, 413.42199999999997, 427.736], [13, 52.36, 312.375, 429.41999999999996, 443.734], [13, 376.03999999999996, 448.63, 429.41999999999996, 443.734], [13, 470.04999999999995, 514.0799999999999, 429.41999999999996, 443.734], [13, 52.36, 323.085, 445.418, 459.73199999999997], [13, 52.36, 169.575, 461.416, 475.72999999999996], [13, 376.03999999999996, 448.63, 445.418, 459.73199999999997], [13, 470.04999999999995, 508.72499999999997, 445.418, 459.73199999999997], [13, 53.55, 524.79, 538.88, 553.194], [13, 50.574999999999996, 263.585, 554.8779999999999, 569.192], [13, 50.574999999999996, 366.52, 607.082, 621.396], [13, 111.86, 327.84499999999997, 625.606, 639.92], [13, 250.49499999999998, 326.06, 644.13, 658.444]]
2026-08-05 05:22:35,025 INFO     29 [qwen-vl-text] ═══ DONE ═══ 37 positions, pages=1, time=21.2s
2026-08-05 05:22:35,025 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:22:35,025 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 05:22:35,025 INFO     29 [qwen-vl-text] positions(25): [[16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:22:35,025 INFO     29 [qwen-vl-text] page grouping: [16], lines per page: [25]
2026-08-05 05:22:35,269 INFO     29 [qwen-vl-text] page=16, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:22:35,271 INFO     29 [qwen-vl-text] LLM extraction start, text_len=728
2026-08-05 05:22:35,272 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:22:35,272 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 521, \"bbox_end\": 545, \"encounter_dates\": [\"2025-11-24\"], \"department\": \"呼吸内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门诊号\n姓名\n科室:呼吸内科门诊\n门(急)诊初诊病历\n电话\n性别:女\n年龄:63岁\n就诊日期:2025-11-24 15:01\n主诉:支气管哮喘复诊\n现病史:患者支气管哮喘复诊,目前规律吸入布地奈德福莫特罗320一次1吸,一天2次(患者自行网购药物),目前有咳嗽、咳痰,咳嗽时有气喘感。无胸闷,无发热,无鼻塞、流涕,无咯血、痰中带血,无头痛、头晕、视物旋转,无饮水呛咳,无咽痛、腹痛、腹胀等不适。未予处理及就医。现患者为求进一步诊治,故至我院科门诊就医。\n既往史:否认高血压、否认糖尿病、否认冠心病等慢性疾病病史,否认肝炎、结核等传染病史,否认手术外伤输血史过敏史:无食物、药物过敏史。。否认饮酒史。\n个人史:已婚已育\n家族史:否认家族病史。\n体格检查:T:36.8℃ P:87次/分 R:21次/分 BP:108/73mmHg 指脉氧:99%。神志清楚,精神尚可,呼吸平顺,口唇无发绀,咽部无充血,扁桃体无肿大,双侧颈静脉无怒张,双肺呼吸音粗,双肺可闻及散在干啰音,双肺未闻及湿性啰音及胸膜摩擦音。心率87次/分,律齐,各瓣膜未闻及明显病理性杂音。腹部平软,全腹部无压痛,反跳痛,肠鸣音正常。四肢运动自如,双下肢无水肿。\n辅助检查:\n初步诊断:\n西医诊断:1.支气管哮喘(急性发作期)\n处理意见:自备布地奈德福莫特罗320一次1吸,一天2次\n醋酸泼尼松片(国基)(5mg*100片)10.000mg\n1次/天 口服 6.00片\n建议:建议患者结果回报后请及时至我科门诊复诊,若出现病情变化或病情加重无好转等,请及时至急诊科门诊复诊。\n医生签名:\n温馨提示:1.请妥善保管好病历及各种检查检验报告单。\n2.复诊时,请携带本病历记录,谢谢!\n第1页(共1页)",
    "role": "user"
  }
]
[92m05:22:35 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:22:35,273 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:22:38,946 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:22:38,947 INFO     29 [qwen-vl-text] LLM output (len=475):
{
  "encounter_date": "2025-11-24",
  "chief_complaint": "支气管哮喘复诊",
  "present_illness": "患者支气管哮喘复诊,目前规律吸入布地奈德福莫特罗320一次1吸,一天2次(患者自行网购药物),目前有咳嗽、咳痰,咳嗽时有气喘感。无胸闷,无发热,无鼻塞、流涕,无咯血、痰中带血,无头痛、头晕、视物旋转,无饮水呛咳,无咽痛、腹痛、腹胀等不适。未予处理及就医。现患者为求进一步诊治,故至我院科门诊就医。",
  "past_history": "否认高血压、否认糖尿病、否认冠心病等慢性疾病病史,否认肝炎、结核等传染病史,否认手术外伤输血史过敏史:无食物、药物过敏史。。否认饮酒史。",
  "diagnosis": "西医诊断:1.支气管哮喘(急性发作期)",
  "treatment_plan": [
    "自备布地奈德福莫特罗320一次1吸,一天2次",
    "醋酸泼尼松片(国基)(5mg*100片)10.000mg 1次/天 口服 6.00片"
  ]
}
2026-08-05 05:22:38,947 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-11-24]
2026-08-05 05:22:38,951 INFO     29 [qwen-vl-text] coord API call start, page=16, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1525336, prompt_len=1416
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["门诊号", "姓名", "科室:呼吸内科门诊", "门(急)诊初诊病历", "电话", "性别:女", "年龄:63岁", "就诊日期:2025-11-24 15:01", "主诉:支气管哮喘复诊", "现病史:患者支气管哮喘复诊,目前规律吸入布地奈德福莫特罗320一次1吸,一天2次(患者自行网购药物),目前有咳嗽、咳痰,咳嗽时有气喘感。无胸闷,无发热,无鼻塞、流涕,无咯血、痰中带血,无头痛、头晕、视物旋转,无饮水呛咳,无咽痛、腹痛、腹胀等不适。未予处理及就医。现患者为求进一步诊治,故至我院科门诊就医。", "既往史:否认高血压、否认糖尿病、否认冠心病等慢性疾病病史,否认肝炎、结核等传染病史,否认手术外伤输血史过敏史:无食物、药物过敏史。。否认饮酒史。", "个人史:已婚已育", "家族史:否认家族病史。", "体格检查:T:36.8℃ P:87次/分 R:21次/分 BP:108/73mmHg 指脉氧:99%。神志清楚,精神尚可,呼吸平顺,口唇无发绀,咽部无充血,扁桃体无肿大,双侧颈静脉无怒张,双肺呼吸音粗,双肺可闻及散在干啰音,双肺未闻及湿性啰音及胸膜摩擦音。心率87次/分,律齐,各瓣膜未闻及明显病理性杂音。腹部平软,全腹部无压痛,反跳痛,肠鸣音正常。四肢运动自如,双下肢无水肿。", "辅助检查:", "初步诊断:", "西医诊断:1.支气管哮喘(急性发作期)", "处理意见:自备布地奈德福莫特罗320一次1吸,一天2次", "醋酸泼尼松片(国基)(5mg*100片)10.000mg", "1次/天 口服 6.00片", "建议:建议患者结果回报后请及时至我科门诊复诊,若出现病情变化或病情加重无好转等,请及时至急诊科门诊复诊。", "医生签名:", "温馨提示:1.请妥善保管好病历及各种检查检验报告单。", "2.复诊时,请携带本病历记录,谢谢!", "第1页(共1页)"]

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
2026-08-05 05:22:48,885 INFO     29 [qwen-vl-text] coord API raw response (len=1804):
[
	{"text": "门诊号", "bbox": [56, 44, 127, 65]},
	{"text": "姓名", "bbox": [56, 71, 105, 92]},
	{"text": "科室:呼吸内科门诊", "bbox": [54, 100, 268, 119]},
	{"text": "门(急)诊初诊病历", "bbox": [357, 58, 657, 86]},
	{"text": "电话", "bbox": [702, 49, 745, 69]},
	{"text": "性别:女", "bbox": [702, 74, 788, 93]},
	{"text": "年龄:63岁", "bbox": [702, 100, 811, 118]},
	{"text": "就诊日期:2025-11-24 15:01", "bbox": [58, 130, 390, 149]},
	{"text": "主诉:支气管哮喘复诊", "bbox": [58, 153, 313, 172]},
	{"text": "现病史:患者支气管哮喘复诊,目前规律吸入布地奈德福莫特罗320一次1吸,一天2次(患者自行网购药物),目前有咳嗽、咳痰,咳嗽时有气喘感。无胸闷,无发热,无鼻塞、流涕,无咯血、痰中带血,无头痛、头晕、视物旋转,无饮水呛咳,无咽痛、腹痛、腹胀等不适。未予处理及就医。现患者为求进一步诊治,故至我院科门诊就医。", "bbox": [52, 176, 968, 287]},
	{"text": "既往史:否认高血压、否认糖尿病、否认冠心病等慢性疾病病史,否认肝炎、结核等传染病史,否认手术外伤输血史过敏史:无食物、药物过敏史。。否认饮酒史。", "bbox": [52, 292, 964, 337]},
	{"text": "个人史:已婚已育", "bbox": [56, 339, 259, 358]},
	{"text": "家族史:否认家族病史。", "bbox": [56, 362, 324, 381]},
	{"text": "体格检查:T:36.8℃ P:87次/分 R:21次/分 BP:108/73mmHg 指脉氧:99%。神志清楚,精神尚可,呼吸平顺,口唇无发绀,咽部无充血,扁桃体无肿大,双侧颈静脉无怒张,双肺呼吸音粗,双肺可闻及散在干啰音,双肺未闻及湿性啰音及胸膜摩擦音。心率87次/分,律齐,各瓣膜未闻及明显病理性杂音。腹部平软,全腹部无压痛,反跳痛,肠鸣音正常。四肢运动自如,双下肢无水肿。", "bbox": [48, 384, 968, 495]},
	{"text": "辅助检查:", "bbox": [54, 498, 165, 517]},
	{"text": "初步诊断:", "bbox": [54, 520, 165, 539]},
	{"text": "西医诊断:1.支气管哮喘(急性发作期)", "bbox": [94, 543, 519, 562]},
	{"text": "处理意见:自备布地奈德福莫特罗320一次1吸,一天2次", "bbox": [52, 566, 695, 585]},
	{"text": "醋酸泼尼松片(国基)(5mg*100片)10.000mg", "bbox": [45, 589, 550, 608]},
	{"text": "1次/天 口服 6.00片", "bbox": [671, 590, 920, 609]},
	{"text": "建议:建议患者结果回报后请及时至我科门诊复诊,若出现病情变化或病情加重无好转等,请及时至急诊科门诊复诊。", "bbox": [44, 704, 950, 744]},
	{"text": "医生签名:", "bbox": [746, 756, 854, 775]},
	{"text": "温馨提示:1.请妥善保管好病历及各种检查检验报告单。", "bbox": [43, 823, 649, 843]},
	{"text": "2.复诊时,请携带本病历记录,谢谢!", "bbox": [163, 849, 575, 868]},
	{"text": "第1页(共1页)", "bbox": [426, 874, 570, 893]}
]
2026-08-05 05:22:48,885 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=9.9s
2026-08-05 05:22:48,885 INFO     29 [qwen-vl-text] coord item[0]: text=门诊号, bbox=[56, 44, 127, 65]
2026-08-05 05:22:48,885 INFO     29 [qwen-vl-text] coord item[1]: text=姓名, bbox=[56, 71, 105, 92]
2026-08-05 05:22:48,886 INFO     29 [qwen-vl-text] coord item[2]: text=科室:呼吸内科门诊, bbox=[54, 100, 268, 119]
2026-08-05 05:22:48,886 INFO     29 [qwen-vl-text] coord item[3]: text=门(急)诊初诊病历, bbox=[357, 58, 657, 86]
2026-08-05 05:22:48,886 INFO     29 [qwen-vl-text] coord item[4]: text=电话, bbox=[702, 49, 745, 69]
2026-08-05 05:22:48,886 INFO     29 [qwen-vl-text] coord item[5]: text=性别:女, bbox=[702, 74, 788, 93]
2026-08-05 05:22:48,886 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:63岁, bbox=[702, 100, 811, 118]
2026-08-05 05:22:48,886 INFO     29 [qwen-vl-text] coord item[7]: text=就诊日期:2025-11-24 15:01, bbox=[58, 130, 390, 149]
2026-08-05 05:22:48,886 INFO     29 [qwen-vl-text] coord item[8]: text=主诉:支气管哮喘复诊, bbox=[58, 153, 313, 172]
2026-08-05 05:22:48,886 INFO     29 [qwen-vl-text] coord item[9]: text=现病史:患者支气管哮喘复诊,目前规律吸入布地奈德福莫特罗320一次1吸,一天2次(患者自行网购药物),目前有咳嗽、咳痰,咳嗽时有气喘感。无胸闷,无发热,无鼻塞、流涕,无咯血、痰中带血,无头痛、头晕、视物旋转,无饮水呛咳,无咽痛、腹痛、腹胀等不适。未予处理及就医。现患者为求进一步诊治,故至我院科门诊就医。, bbox=[52, 176, 968, 287]
2026-08-05 05:22:48,886 INFO     29 [qwen-vl-text] coord item[10]: text=既往史:否认高血压、否认糖尿病、否认冠心病等慢性疾病病史,否认肝炎、结核等传染病史,否认手术外伤输血史过敏史:无食物、药物过敏史。。否认饮酒史。, bbox=[52, 292, 964, 337]
2026-08-05 05:22:48,886 INFO     29 [qwen-vl-text] coord item[11]: text=个人史:已婚已育, bbox=[56, 339, 259, 358]
2026-08-05 05:22:48,886 INFO     29 [qwen-vl-text] coord item[12]: text=家族史:否认家族病史。, bbox=[56, 362, 324, 381]
2026-08-05 05:22:48,886 INFO     29 [qwen-vl-text] coord item[13]: text=体格检查:T:36.8℃ P:87次/分 R:21次/分 BP:108/73mmHg 指脉氧:99%。神志清楚,精神尚可,呼吸平顺,口唇无发绀,咽部无充血,扁桃体无肿大,双侧颈静脉无怒张,双肺呼吸音粗,双肺可闻及散在干啰音,双肺未闻及湿性啰音及胸膜摩擦音。心率87次/分,律齐,各瓣膜未闻及明显病理性杂音。腹部平软,全腹部无压痛,反跳痛,肠鸣音正常。四肢运动自如,双下肢无水肿。, bbox=[48, 384, 968, 495]
2026-08-05 05:22:48,886 INFO     29 [qwen-vl-text] coord item[14]: text=辅助检查:, bbox=[54, 498, 165, 517]
2026-08-05 05:22:48,886 INFO     29 [qwen-vl-text] coord item[15]: text=初步诊断:, bbox=[54, 520, 165, 539]
2026-08-05 05:22:48,886 INFO     29 [qwen-vl-text] coord item[16]: text=西医诊断:1.支气管哮喘(急性发作期), bbox=[94, 543, 519, 562]
2026-08-05 05:22:48,886 INFO     29 [qwen-vl-text] coord item[17]: text=处理意见:自备布地奈德福莫特罗320一次1吸,一天2次, bbox=[52, 566, 695, 585]
2026-08-05 05:22:48,887 INFO     29 [qwen-vl-text] coord item[18]: text=醋酸泼尼松片(国基)(5mg*100片)10.000mg, bbox=[45, 589, 550, 608]
2026-08-05 05:22:48,887 INFO     29 [qwen-vl-text] coord item[19]: text=1次/天 口服 6.00片, bbox=[671, 590, 920, 609]
2026-08-05 05:22:48,887 INFO     29 [qwen-vl-text] coord item[20]: text=建议:建议患者结果回报后请及时至我科门诊复诊,若出现病情变化或病情加重无好转等,请及时至急诊科门诊复诊。, bbox=[44, 704, 950, 744]
2026-08-05 05:22:48,887 INFO     29 [qwen-vl-text] coord item[21]: text=医生签名:, bbox=[746, 756, 854, 775]
2026-08-05 05:22:48,887 INFO     29 [qwen-vl-text] coord item[22]: text=温馨提示:1.请妥善保管好病历及各种检查检验报告单。, bbox=[43, 823, 649, 843]
2026-08-05 05:22:48,887 INFO     29 [qwen-vl-text] coord item[23]: text=2.复诊时,请携带本病历记录,谢谢!, bbox=[163, 849, 575, 868]
2026-08-05 05:22:48,887 INFO     29 [qwen-vl-text] coord item[24]: text=第1页(共1页), bbox=[426, 874, 570, 893]
2026-08-05 05:22:48,887 INFO     29 [qwen-vl-text] page=16 — 25/25 coords, api_time=9.9s
2026-08-05 05:22:48,888 INFO     29 [qwen-vl-text] new_positions (25):
[[16, 33.32, 75.565, 37.048, 54.73], [16, 33.32, 62.474999999999994, 59.782, 77.464], [16, 32.129999999999995, 159.45999999999998, 84.2, 100.198], [16, 212.415, 390.91499999999996, 48.836, 72.41199999999999], [16, 417.69, 443.275, 41.257999999999996, 58.098], [16, 417.69, 468.85999999999996, 62.308, 78.306], [16, 417.69, 482.54499999999996, 84.2, 99.356], [16, 34.51, 232.04999999999998, 109.46, 125.458], [16, 34.51, 186.23499999999999, 128.826, 144.82399999999998], [16, 30.939999999999998, 575.9599999999999, 148.192, 241.654], [16, 30.939999999999998, 573.5799999999999, 245.864, 283.75399999999996], [16, 33.32, 154.105, 285.438, 301.436], [16, 33.32, 192.78, 304.804, 320.80199999999996], [16, 28.56, 575.9599999999999, 323.328, 416.78999999999996], [16, 32.129999999999995, 98.175, 419.316, 435.31399999999996], [16, 32.129999999999995, 98.175, 437.84, 453.83799999999997], [16, 55.93, 308.805, 457.20599999999996, 473.204], [16, 30.939999999999998, 413.525, 476.572, 492.57], [16, 26.775, 327.25, 495.938, 511.936], [16, 399.245, 547.4, 496.78, 512.778], [16, 26.18, 565.25, 592.768, 626.448], [16, 443.87, 508.13, 636.552, 652.55], [16, 25.584999999999997, 386.155, 692.966, 709.8059999999999], [16, 96.985, 342.125, 714.858, 730.856], [16, 253.47, 339.15, 735.908, 751.906]]
2026-08-05 05:22:48,888 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=13.9s
2026-08-05 05:22:48,906 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-05 05:22:48,907 INFO     29 [Trace] task=d7b98bb4 | doc=LZQ 64 哮喘 深圳二院.pdf | Extractor:Clinical | outputs={"chunks": "6 items, types={'OutpatientRecord': 6}", "html": "", "json": "676 items", "markdown": "", "text": "", "name": "LZQ 64 哮喘 深圳二院.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Medication\": 5}"}
2026-08-05 05:22:48,907 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-05 05:22:48,907 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:22:48.907+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 16, "failed": 0, "current": {"d7b98bb4908c11f1a3da71efcdd7cc1f": {"id": "d7b98bb4908c11f1a3da71efcdd7cc1f", "doc_id": "d7626528908c11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479738, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785907001430, "task_type": "dataflow", "root_trace_id": "ea6d5499d1eb4a3cabaa8fb5a06c80f8", "root_traceparent": "00-ea6d5499d1eb4a3cabaa8fb5a06c80f8-0f37f835e898f31c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:22:48,913 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:22:48,913 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 05:22:48,913 INFO     29 [qwen-vl-text] positions(48): [[14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:22:48,914 INFO     29 [qwen-vl-text] page grouping: [14], lines per page: [48]
2026-08-05 05:22:49,103 INFO     29 [qwen-vl-text] page=14, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:22:49,105 INFO     29 [qwen-vl-text] LLM extraction start, text_len=544
2026-08-05 05:22:49,105 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:22:49,105 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 435, \"bbox_end\": 482, \"encounter_dates\": [\"2025-10-25\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "广东省医疗门诊收费票据（电子）\n广东省\n财政部监制\n票据代码：44060125\n票据号码：9148002082\n校验码：831306\n开票日期：2025-10-25\n项目名称\n数量/单位\n金额（元）\n备注\n项目名称\n数量/单位\n金额（元）\n备注\n西药费\n1\n13.05\n以下是清单项\n醋酸泼尼松片（国基）\n12\n0.50\n硫酸沙丁胺醇吸入气雾剂（省3\n1\n12.55\n、国基）\n金额合计（大写）壹拾叁元零伍分\n(小写)13.05\n业务流水号：SF10390911\n门诊\n就诊日期：20251025\n其他信息\n医疗机构类型：综合医院\n医保类型：现金(自费)\n医保编号：\n性别：女\n医保统筹基金支付：0.00\n其他支付：0.00\n个人账户支付：0.00\n个人现金支付：13.05\n个人自付：0.00\n个人自费：13.05\n政策性减免：\n收款单位（章）深圳市龙岗区第人民医院\n复核人：掌上医院\n收款人：掌上医院\n说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。\n单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dzpj.czt.gd.gov.cn/billcheck查验本省财政电子票据。",
    "role": "user"
  }
]
[92m05:22:49 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:22:49,106 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:22:52,585 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:22:52,585 INFO     29 [qwen-vl-text] LLM output (len=673):
{
  "encounter_date": "2025-10-25",
  "pharmacy": null,
  "medications": [
    {
      "name": "醋酸泼尼松片",
      "specification": null,
      "dosage": null,
      "quantity": 12,
      "unit_price": 0.5,
      "total_price": null,
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
      "total_price": null,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 13.05,
  "payment_method": "现金(自费)"
}
2026-08-05 05:22:52,585 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-10-25]
2026-08-05 05:22:52,589 INFO     29 [qwen-vl-text] coord API call start, page=14, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=928201, prompt_len=1301
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共48行）
["广东省医疗门诊收费票据（电子）", "广东省", "财政部监制", "票据代码：44060125", "票据号码：9148002082", "校验码：831306", "开票日期：2025-10-25", "项目名称", "数量/单位", "金额（元）", "备注", "项目名称", "数量/单位", "金额（元）", "备注", "西药费", "1", "13.05", "以下是清单项", "醋酸泼尼松片（国基）", "12", "0.50", "硫酸沙丁胺醇吸入气雾剂（省3", "1", "12.55", "、国基）", "金额合计（大写）壹拾叁元零伍分", "(小写)13.05", "业务流水号：SF10390911", "门诊", "就诊日期：20251025", "其他信息", "医疗机构类型：综合医院", "医保类型：现金(自费)", "医保编号：", "性别：女", "医保统筹基金支付：0.00", "其他支付：0.00", "个人账户支付：0.00", "个人现金支付：13.05", "个人自付：0.00", "个人自费：13.05", "政策性减免：", "收款单位（章）深圳市龙岗区第人民医院", "复核人：掌上医院", "收款人：掌上医院", "说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。", "单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dzpj.czt.gd.gov.cn/billcheck查验本省财政电子票据。"]

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
2026-08-05 05:23:15,495 INFO     29 [qwen-vl-text] coord API raw response (len=3971):
[
	{"text": "广东省医疗门诊收费票据（电子）", "bbox": [316, 65, 701, 102]},
	{"text": "广东省", "bbox": [490, 100, 537, 118]},
	{"text": "财政部监制", "bbox": [474, 132, 552, 157]},
	{"text": "票据代码：44060125", "bbox": [97, 164, 210, 181]},
	{"text": "票据号码：9148002082", "bbox": [653, 164, 781, 181], "bbox": [653, 164, 781, 181]},
	{"text": "校验码：831306", "bbox": [652, 190, 754, 207], "bbox": [652, 190, 754, 207]},
	{"text": "开票日期：2025-10-25", "bbox": [652, 216, 780, 233], "bbox": [652, 216, 780, 233]},
	{"text": "项目名称", "bbox": [164, 251, 216, 268], "bbox": [164, 251, 216, 268]},
	{"text": "数量/单位", "bbox": [300, 251, 365, 268], "bbox": [300, 251, 365, 268]},
	{"text": "金额（元）", "bbox": [391, 251, 448, 268], "bbox": [391, 251, 448, 268]},
	{"text": "备注", "bbox": [472, 251, 497, 268], "bbox": [472, 251, 497, 268]},
	{"text": "项目名称", "bbox": [579, 251, 632, 268], "bbox": [579, 251, 632, 268]},
	{"text": "数量/单位", "bbox": [714, 251, 780, 268], "bbox": [714, 251, 780, 268]},
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
	{"text": "金额合计（大写）壹拾叁元零伍分", "bbox": [100, 559, 297, 577], "bbox": [100, 559, 297, 577]},
	{"text": "(小写)13.05", "bbox": [565, 560, 639, 577], "bbox": [565, 560, 639, 577]},
	{"text": "业务流水号：SF10390911", "bbox": [127, 595, 267, 612], "bbox": [127, 595, 267, 612]},
	{"text": "门诊", "bbox": [339, 595, 365, 612], "bbox": [339, 595, 365, 612]},
	{"text": "就诊日期：20251025", "bbox": [739, 595, 854, 612], "bbox": [739, 595, 854, 612]},
	{"text": "其他信息", "bbox": [105, 625, 118, 760], "bbox": [105, 625, 118, 760]},
	{"text": "医疗机构类型：综合医院", "bbox": [127, 641, 267, 658], "bbox": [127, 641, 267, 658]},
	{"text": "医保类型：现金(自费)", "bbox": [339, 641, 461, 658], "bbox": [339, 641, 461, 658]},
	{"text": "医保编号：", "bbox": [525, 641, 583, 658], "bbox": [525, 641, 583, 658]},
	{"text": "性别：女", "bbox": [739, 641, 787, 658], "bbox": [739, 641, 787, 658]},
	{"text": "医保统筹基金支付：0.00", "bbox": [127, 685, 267, 702], "bbox": [127, 685, 267, 702]},
	{"text": "其他支付：0.00", "bbox": [339, 685, 423, 702], "bbox": [339, 685, 423, 702]},
	{"text": "个人账户支付：0.00", "bbox": [525, 685, 640, 702], "bbox": [525, 685, 640, 702]},
	{"text": "个人现金支付：13.05", "bbox": [739, 685, 860, 702], "bbox": [739, 685, 860, 702]},
	{"text": "个人自付：0.00", "bbox": [127, 724, 216, 741], "bbox": [127, 724, 216, 741]},
	{"text": "个人自费：13.05", "bbox": [339, 724, 430, 741], "bbox": [339, 724, 430, 741]},
	{"text": "政策性减免：", "bbox": [339, 760, 409, 778], "bbox": [339, 760, 409, 778]},
	{"text": "收款单位（章）深圳市龙岗区第人民医院", "bbox": [100, 805, 361, 825], "bbox": [100, 805, 361, 825]},
	{"text": "复核人：掌上医院", "bbox": [565, 805, 664, 825], "bbox": [565, 805, 664, 825]},
	{"text": "收款人：掌上医院", "bbox": [738, 805, 841, 825], "bbox": [738, 805, 841, 825]},
	{"text": "说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。", "bbox": [114, 838, 853, 856], "bbox": [114, 838, 853, 856]},
	{"text": "单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dzpj.czt.gd.gov.cn/billcheck查验本省财政电子票据。", "bbox": [160, 856, 826, 873], "bbox": [160, 856, 826, 873]}
]
2026-08-05 05:23:15,496 INFO     29 [qwen-vl-text] coord API: raw_items=48, valid_items=48, elapsed=22.9s
2026-08-05 05:23:15,496 INFO     29 [qwen-vl-text] coord item[0]: text=广东省医疗门诊收费票据（电子）, bbox=[316, 65, 701, 102]
2026-08-05 05:23:15,496 INFO     29 [qwen-vl-text] coord item[1]: text=广东省, bbox=[490, 100, 537, 118]
2026-08-05 05:23:15,496 INFO     29 [qwen-vl-text] coord item[2]: text=财政部监制, bbox=[474, 132, 552, 157]
2026-08-05 05:23:15,496 INFO     29 [qwen-vl-text] coord item[3]: text=票据代码：44060125, bbox=[97, 164, 210, 181]
2026-08-05 05:23:15,496 INFO     29 [qwen-vl-text] coord item[4]: text=票据号码：9148002082, bbox=[653, 164, 781, 181]
2026-08-05 05:23:15,496 INFO     29 [qwen-vl-text] coord item[5]: text=校验码：831306, bbox=[652, 190, 754, 207]
2026-08-05 05:23:15,496 INFO     29 [qwen-vl-text] coord item[6]: text=开票日期：2025-10-25, bbox=[652, 216, 780, 233]
2026-08-05 05:23:15,496 INFO     29 [qwen-vl-text] coord item[7]: text=项目名称, bbox=[164, 251, 216, 268]
2026-08-05 05:23:15,496 INFO     29 [qwen-vl-text] coord item[8]: text=数量/单位, bbox=[300, 251, 365, 268]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[9]: text=金额（元）, bbox=[391, 251, 448, 268]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[10]: text=备注, bbox=[472, 251, 497, 268]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[11]: text=项目名称, bbox=[579, 251, 632, 268]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[12]: text=数量/单位, bbox=[714, 251, 780, 268]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[13]: text=金额（元）, bbox=[806, 251, 862, 268]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[14]: text=备注, bbox=[883, 251, 906, 268]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[15]: text=西药费, bbox=[98, 287, 139, 305]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[16]: text=1, bbox=[303, 290, 309, 304]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[17]: text=13.05, bbox=[421, 290, 454, 304]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[18]: text=以下是清单项, bbox=[98, 343, 178, 361]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[19]: text=醋酸泼尼松片（国基）, bbox=[98, 373, 225, 391]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[20]: text=12, bbox=[300, 376, 313, 390]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[21]: text=0.50, bbox=[425, 376, 454, 390]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[22]: text=硫酸沙丁胺醇吸入气雾剂（省3, bbox=[513, 373, 695, 391]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[23]: text=1, bbox=[717, 376, 723, 390]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[24]: text=12.55, bbox=[836, 376, 867, 390]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[25]: text=、国基）, bbox=[513, 396, 560, 414]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[26]: text=金额合计（大写）壹拾叁元零伍分, bbox=[100, 559, 297, 577]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[27]: text=(小写)13.05, bbox=[565, 560, 639, 577]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[28]: text=业务流水号：SF10390911, bbox=[127, 595, 267, 612]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[29]: text=门诊, bbox=[339, 595, 365, 612]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[30]: text=就诊日期：20251025, bbox=[739, 595, 854, 612]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[31]: text=其他信息, bbox=[105, 625, 118, 760]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[32]: text=医疗机构类型：综合医院, bbox=[127, 641, 267, 658]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[33]: text=医保类型：现金(自费), bbox=[339, 641, 461, 658]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[34]: text=医保编号：, bbox=[525, 641, 583, 658]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[35]: text=性别：女, bbox=[739, 641, 787, 658]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[36]: text=医保统筹基金支付：0.00, bbox=[127, 685, 267, 702]
2026-08-05 05:23:15,497 INFO     29 [qwen-vl-text] coord item[37]: text=其他支付：0.00, bbox=[339, 685, 423, 702]
2026-08-05 05:23:15,498 INFO     29 [qwen-vl-text] coord item[38]: text=个人账户支付：0.00, bbox=[525, 685, 640, 702]
2026-08-05 05:23:15,498 INFO     29 [qwen-vl-text] coord item[39]: text=个人现金支付：13.05, bbox=[739, 685, 860, 702]
2026-08-05 05:23:15,498 INFO     29 [qwen-vl-text] coord item[40]: text=个人自付：0.00, bbox=[127, 724, 216, 741]
2026-08-05 05:23:15,498 INFO     29 [qwen-vl-text] coord item[41]: text=个人自费：13.05, bbox=[339, 724, 430, 741]
2026-08-05 05:23:15,498 INFO     29 [qwen-vl-text] coord item[42]: text=政策性减免：, bbox=[339, 760, 409, 778]
2026-08-05 05:23:15,498 INFO     29 [qwen-vl-text] coord item[43]: text=收款单位（章）深圳市龙岗区第人民医院, bbox=[100, 805, 361, 825]
2026-08-05 05:23:15,498 INFO     29 [qwen-vl-text] coord item[44]: text=复核人：掌上医院, bbox=[565, 805, 664, 825]
2026-08-05 05:23:15,498 INFO     29 [qwen-vl-text] coord item[45]: text=收款人：掌上医院, bbox=[738, 805, 841, 825]
2026-08-05 05:23:15,498 INFO     29 [qwen-vl-text] coord item[46]: text=说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。, bbox=[114, 838, 853, 856]
2026-08-05 05:23:15,498 INFO     29 [qwen-vl-text] coord item[47]: text=单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dzpj.czt.gd.gov.cn/billcheck查验本省财政电子票据。, bbox=[160, 856, 826, 873]
2026-08-05 05:23:15,498 INFO     29 [qwen-vl-text] page=14 — 48/48 coords, api_time=22.9s
2026-08-05 05:23:15,498 INFO     29 [qwen-vl-text] new_positions (48):
[[14, 266.072, 590.242, 38.675, 60.69], [14, 412.58, 452.154, 59.5, 70.21], [14, 399.108, 464.784, 78.53999999999999, 93.41499999999999], [14, 81.67399999999999, 176.82, 97.58, 107.695], [14, 549.826, 657.602, 97.58, 107.695], [14, 548.984, 634.8679999999999, 113.05, 123.16499999999999], [14, 548.984, 656.76, 128.51999999999998, 138.635], [14, 138.088, 181.87199999999999, 149.345, 159.45999999999998], [14, 252.6, 307.33, 149.345, 159.45999999999998], [14, 329.222, 377.216, 149.345, 159.45999999999998], [14, 397.424, 418.474, 149.345, 159.45999999999998], [14, 487.518, 532.144, 149.345, 159.45999999999998], [14, 601.188, 656.76, 149.345, 159.45999999999998], [14, 678.6519999999999, 725.804, 149.345, 159.45999999999998], [14, 743.486, 762.852, 149.345, 159.45999999999998], [14, 82.51599999999999, 117.038, 170.765, 181.475], [14, 255.126, 260.178, 172.54999999999998, 180.88], [14, 354.48199999999997, 382.268, 172.54999999999998, 180.88], [14, 82.51599999999999, 149.876, 204.08499999999998, 214.795], [14, 82.51599999999999, 189.45, 221.935, 232.64499999999998], [14, 252.6, 263.546, 223.72, 232.04999999999998], [14, 357.84999999999997, 382.268, 223.72, 232.04999999999998], [14, 431.94599999999997, 585.1899999999999, 221.935, 232.64499999999998], [14, 603.7139999999999, 608.766, 223.72, 232.04999999999998], [14, 703.9119999999999, 730.014, 223.72, 232.04999999999998], [14, 431.94599999999997, 471.52, 235.61999999999998, 246.32999999999998], [14, 84.2, 250.07399999999998, 332.60499999999996, 343.315], [14, 475.72999999999996, 538.038, 333.2, 343.315], [14, 106.934, 224.814, 354.025, 364.14], [14, 285.438, 307.33, 354.025, 364.14], [14, 622.2379999999999, 719.068, 354.025, 364.14], [14, 88.41, 99.356, 371.875, 452.2], [14, 106.934, 224.814, 381.395, 391.51], [14, 285.438, 388.162, 381.395, 391.51], [14, 442.05, 490.88599999999997, 381.395, 391.51], [14, 622.2379999999999, 662.654, 381.395, 391.51], [14, 106.934, 224.814, 407.575, 417.69], [14, 285.438, 356.166, 407.575, 417.69], [14, 442.05, 538.88, 407.575, 417.69], [14, 622.2379999999999, 724.12, 407.575, 417.69], [14, 106.934, 181.87199999999999, 430.78, 440.895], [14, 285.438, 362.06, 430.78, 440.895], [14, 285.438, 344.378, 452.2, 462.90999999999997], [14, 84.2, 303.962, 478.97499999999997, 490.875], [14, 475.72999999999996, 559.088, 478.97499999999997, 490.875], [14, 621.396, 708.122, 478.97499999999997, 490.875], [14, 95.988, 718.226, 498.60999999999996, 509.32], [14, 134.72, 695.492, 509.32, 519.435]]
2026-08-05 05:23:15,498 INFO     29 [qwen-vl-text] ═══ DONE ═══ 48 positions, pages=1, time=26.6s
2026-08-05 05:23:15,499 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:23:15,499 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 05:23:15,499 INFO     29 [qwen-vl-text] positions(36): [[15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:23:15,499 INFO     29 [qwen-vl-text] page grouping: [15], lines per page: [36]
2026-08-05 05:23:15,727 INFO     29 [qwen-vl-text] page=15, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:23:15,728 INFO     29 [qwen-vl-text] LLM extraction start, text_len=310
2026-08-05 05:23:15,728 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:23:15,728 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 485, \"bbox_end\": 520, \"encounter_dates\": [\"2025-11-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "电子发票(普通发票)\n发票号码：25447000001429974977\n开票日期：2025年11月05日\n广东省税务局\n购买方信息\n名称：\n统一社会信用代码/纳税人识别号：\n销售方信息\n名称：阿里健康大药房医药连锁有限公司\n统一社会信用代码/纳税人识别号：91440101681325547Y\n项目名称\n规格型号\n单位\n数量\n单价\n金额\n税率/征收率\n税额\n*化学药品制剂*布地奈德\n盒\n3\n176.70\n530.09\n13%\n68.91\n福莫特罗吸入粉雾剂\n合计\n￥530.09\n￥68.91\n价税合计（大写）\n伍佰玖拾玖圆整\n(小写)￥599.00\n备注\n开票人：董茜玲\nCS 扫描全能王\n3亿人都在用的扫描App",
    "role": "user"
  }
]
[92m05:23:15 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:23:15,729 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:23:18,181 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:23:18,181 INFO     29 [qwen-vl-text] LLM output (len=420):
{
  "encounter_date": "2025-11-05",
  "pharmacy": "阿里健康大药房医药连锁有限公司",
  "medications": [
    {
      "name": "布地奈德福莫特罗吸入粉雾剂",
      "specification": null,
      "dosage": null,
      "quantity": 3,
      "unit_price": 176.7,
      "total_price": 530.09,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 599.0,
  "payment_method": null
}
2026-08-05 05:23:18,181 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-11-05]
2026-08-05 05:23:18,182 INFO     29 [qwen-vl-text] coord API call start, page=15, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=848797, prompt_len=1031
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共36行）
["电子发票(普通发票)", "发票号码：25447000001429974977", "开票日期：2025年11月05日", "广东省税务局", "购买方信息", "名称：", "统一社会信用代码/纳税人识别号：", "销售方信息", "名称：阿里健康大药房医药连锁有限公司", "统一社会信用代码/纳税人识别号：91440101681325547Y", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*化学药品制剂*布地奈德", "盒", "3", "176.70", "530.09", "13%", "68.91", "福莫特罗吸入粉雾剂", "合计", "￥530.09", "￥68.91", "价税合计（大写）", "伍佰玖拾玖圆整", "(小写)￥599.00", "备注", "开票人：董茜玲", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-05 05:23:33,539 INFO     29 [qwen-vl-text] coord API raw response (len=2931):
[
	{"text": "电子发票(普通发票)", "bbox": [340, 66, 630, 107]},
	{"text": "发票号码：25447000001429974977", "bbox": [728, 82, 961, 103]},
	{"text": "开票日期：2025年11月05日", "bbox": [727, 126, 916, 146]},
	{"text": "广东省税务局", "bbox": [458, 152, 526, 173]},
	{"text": "购买方信息", "bbox": [43, 220, 57, 336], "bbox_2d": [43, 220, 57, 336]},
	{"text": "名称：", "bbox": [67, 250, 88, 270], "bbox_2d": [67, 250, 88, 270]},
	{"text": "统一社会信用代码/纳税人识别号：", "bbox": [67, 275, 283, 295], "bbox_2d": [67, 275, 283, 295]},
	{"text": "销售方信息", "bbox": [507, 220, 521, 336], "bbox_2d": [507, 220, 521, 336]},
	{"text": "名称：阿里健康大药房医药连锁有限公司", "bbox": [530, 250, 792, 270], "bbox_2d": [530, 250, 792, 270]},
	{"text": "统一社会信用代码/纳税人识别号：91440101681325547Y", "bbox": [530, 275, 958, 295], "bbox_2d": [530, 275, 958, 295]},
	{"text": "项目名称", "bbox": [92, 354, 150, 373], "bbox_2d": [92, 354, 150, 373]},
	{"text": "规格型号", "bbox": [206, 354, 264, 373], "bbox_2d": [206, 354, 264, 373]},
	{"text": "单位", "bbox": [326, 354, 364, 373], "bbox_2d": [326, 354, 364, 373]},
	{"text": "数量", "bbox": [450, 354, 488, 373], "bbox_2d": [450, 354, 488, 373]},
	{"text": "单价", "bbox": [565, 354, 603, 373], "bbox_2d": [565, 354, 603, 373]},
	{"text": "金额", "bbox": [686, 354, 723, 373], "bbox_2d": [686, 354, 723, 373]},
	{"text": "税率/征收率", "bbox": [757, 354, 838, 373], "bbox_2d": [757, 354, 838, 373]},
	{"text": "税额", "bbox": [923, 354, 961, 373], "bbox_2d": [923, 354, 961, 373]},
	{"text": "*化学药品制剂*布地奈德", "bbox": [36, 385, 196, 405], "bbox_2d": [36, 385, 196, 405]},
	{"text": "盒", "bbox": [338, 385, 354, 405], "bbox_2d": [338, 385, 354, 405]},
	{"text": "3", "bbox": [480, 387, 489, 404], "bbox_2d": [480, 387, 489, 404]},
	{"text": "176.70", "bbox": [560, 387, 603, 404], "bbox_2d": [560, 387, 603, 404]},
	{"text": "530.09", "bbox": [679, 387, 723, 404], "bbox_2d": [679, 387, 723, 404]},
	{"text": "13%", "bbox": [770, 387, 792, 404], "bbox_2d": [770, 387, 792, 404]},
	{"text": "68.91", "bbox": [924, 387, 960, 404], "bbox_2d": [924, 387, 960, 404]},
	{"text": "福莫特罗吸入粉雾剂", "bbox": [36, 413, 168, 434], "bbox_2d": [36, 413, 168, 434]},
	{"text": "合计", "bbox": [106, 610, 119, 629], "bbox_2d": [106, 610, 119, 629]},
	{"text": "￥530.09", "bbox": [669, 611, 723, 629], "bbox_2d": [669, 611, 723, 629]},
	{"text": "￥68.91", "bbox": [915, 611, 960, 629], "bbox_2d": [915, 611, 960, 629]},
	{"text": "价税合计（大写）", "bbox": [100, 656, 208, 676], "bbox_2d": [100, 656, 208, 676]},
	{"text": "伍佰玖拾玖圆整", "bbox": [314, 656, 417, 676], "bbox_2d": [314, 656, 417, 676]},
	{"text": "(小写)￥599.00", "bbox": [686, 656, 790, 676], "bbox_2d": [686, 656, 790, 676]},
	{"text": "备注", "bbox": [43, 737, 57, 780], "bbox_2d": [43, 737, 57, 780]},
	{"text": "开票人：董茜玲", "bbox": [100, 853, 202, 873], "bbox_2d": [100, 853, 202, 873]},
	{"text": "CS 扫描全能王", "bbox": [903, 942, 983, 962], "bbox_2d": [903, 942, 983, 962]},
	{"text": "3亿人都在用的扫描App", "bbox": [903, 969, 983, 980], "bbox_2d": [903, 969, 983, 980]}
]
2026-08-05 05:23:33,540 INFO     29 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=15.4s
2026-08-05 05:23:33,540 INFO     29 [qwen-vl-text] coord item[0]: text=电子发票(普通发票), bbox=[340, 66, 630, 107]
2026-08-05 05:23:33,540 INFO     29 [qwen-vl-text] coord item[1]: text=发票号码：25447000001429974977, bbox=[728, 82, 961, 103]
2026-08-05 05:23:33,540 INFO     29 [qwen-vl-text] coord item[2]: text=开票日期：2025年11月05日, bbox=[727, 126, 916, 146]
2026-08-05 05:23:33,541 INFO     29 [qwen-vl-text] coord item[3]: text=广东省税务局, bbox=[458, 152, 526, 173]
2026-08-05 05:23:33,541 INFO     29 [qwen-vl-text] coord item[4]: text=购买方信息, bbox=[43, 220, 57, 336]
2026-08-05 05:23:33,541 INFO     29 [qwen-vl-text] coord item[5]: text=名称：, bbox=[67, 250, 88, 270]
2026-08-05 05:23:33,541 INFO     29 [qwen-vl-text] coord item[6]: text=统一社会信用代码/纳税人识别号：, bbox=[67, 275, 283, 295]
2026-08-05 05:23:33,541 INFO     29 [qwen-vl-text] coord item[7]: text=销售方信息, bbox=[507, 220, 521, 336]
2026-08-05 05:23:33,541 INFO     29 [qwen-vl-text] coord item[8]: text=名称：阿里健康大药房医药连锁有限公司, bbox=[530, 250, 792, 270]
2026-08-05 05:23:33,541 INFO     29 [qwen-vl-text] coord item[9]: text=统一社会信用代码/纳税人识别号：91440101681325547Y, bbox=[530, 275, 958, 295]
2026-08-05 05:23:33,541 INFO     29 [qwen-vl-text] coord item[10]: text=项目名称, bbox=[92, 354, 150, 373]
2026-08-05 05:23:33,541 INFO     29 [qwen-vl-text] coord item[11]: text=规格型号, bbox=[206, 354, 264, 373]
2026-08-05 05:23:33,541 INFO     29 [qwen-vl-text] coord item[12]: text=单位, bbox=[326, 354, 364, 373]
2026-08-05 05:23:33,541 INFO     29 [qwen-vl-text] coord item[13]: text=数量, bbox=[450, 354, 488, 373]
2026-08-05 05:23:33,541 INFO     29 [qwen-vl-text] coord item[14]: text=单价, bbox=[565, 354, 603, 373]
2026-08-05 05:23:33,541 INFO     29 [qwen-vl-text] coord item[15]: text=金额, bbox=[686, 354, 723, 373]
2026-08-05 05:23:33,541 INFO     29 [qwen-vl-text] coord item[16]: text=税率/征收率, bbox=[757, 354, 838, 373]
2026-08-05 05:23:33,541 INFO     29 [qwen-vl-text] coord item[17]: text=税额, bbox=[923, 354, 961, 373]
2026-08-05 05:23:33,542 INFO     29 [qwen-vl-text] coord item[18]: text=*化学药品制剂*布地奈德, bbox=[36, 385, 196, 405]
2026-08-05 05:23:33,542 INFO     29 [qwen-vl-text] coord item[19]: text=盒, bbox=[338, 385, 354, 405]
2026-08-05 05:23:33,542 INFO     29 [qwen-vl-text] coord item[20]: text=3, bbox=[480, 387, 489, 404]
2026-08-05 05:23:33,542 INFO     29 [qwen-vl-text] coord item[21]: text=176.70, bbox=[560, 387, 603, 404]
2026-08-05 05:23:33,542 INFO     29 [qwen-vl-text] coord item[22]: text=530.09, bbox=[679, 387, 723, 404]
2026-08-05 05:23:33,542 INFO     29 [qwen-vl-text] coord item[23]: text=13%, bbox=[770, 387, 792, 404]
2026-08-05 05:23:33,542 INFO     29 [qwen-vl-text] coord item[24]: text=68.91, bbox=[924, 387, 960, 404]
2026-08-05 05:23:33,542 INFO     29 [qwen-vl-text] coord item[25]: text=福莫特罗吸入粉雾剂, bbox=[36, 413, 168, 434]
2026-08-05 05:23:33,543 INFO     29 [qwen-vl-text] coord item[26]: text=合计, bbox=[106, 610, 119, 629]
2026-08-05 05:23:33,543 INFO     29 [qwen-vl-text] coord item[27]: text=￥530.09, bbox=[669, 611, 723, 629]
2026-08-05 05:23:33,543 INFO     29 [qwen-vl-text] coord item[28]: text=￥68.91, bbox=[915, 611, 960, 629]
2026-08-05 05:23:33,543 INFO     29 [qwen-vl-text] coord item[29]: text=价税合计（大写）, bbox=[100, 656, 208, 676]
2026-08-05 05:23:33,543 INFO     29 [qwen-vl-text] coord item[30]: text=伍佰玖拾玖圆整, bbox=[314, 656, 417, 676]
2026-08-05 05:23:33,543 INFO     29 [qwen-vl-text] coord item[31]: text=(小写)￥599.00, bbox=[686, 656, 790, 676]
2026-08-05 05:23:33,543 INFO     29 [qwen-vl-text] coord item[32]: text=备注, bbox=[43, 737, 57, 780]
2026-08-05 05:23:33,543 INFO     29 [qwen-vl-text] coord item[33]: text=开票人：董茜玲, bbox=[100, 853, 202, 873]
2026-08-05 05:23:33,543 INFO     29 [qwen-vl-text] coord item[34]: text=CS 扫描全能王, bbox=[903, 942, 983, 962]
2026-08-05 05:23:33,543 INFO     29 [qwen-vl-text] coord item[35]: text=3亿人都在用的扫描App, bbox=[903, 969, 983, 980]
2026-08-05 05:23:33,544 INFO     29 [qwen-vl-text] page=15 — 36/36 coords, api_time=15.4s
2026-08-05 05:23:33,544 INFO     29 [qwen-vl-text] new_positions (36):
[[15, 286.28, 530.46, 39.269999999999996, 63.665], [15, 612.976, 809.1619999999999, 48.79, 61.285], [15, 612.134, 771.2719999999999, 74.97, 86.86999999999999], [15, 385.63599999999997, 442.892, 90.44, 102.935], [15, 36.205999999999996, 47.994, 130.9, 199.92], [15, 56.414, 74.096, 148.75, 160.65], [15, 56.414, 238.286, 163.625, 175.525], [15, 426.894, 438.68199999999996, 130.9, 199.92], [15, 446.26, 666.864, 148.75, 160.65], [15, 446.26, 806.636, 163.625, 175.525], [15, 77.464, 126.3, 210.63, 221.935], [15, 173.452, 222.28799999999998, 210.63, 221.935], [15, 274.492, 306.488, 210.63, 221.935], [15, 378.9, 410.89599999999996, 210.63, 221.935], [15, 475.72999999999996, 507.726, 210.63, 221.935], [15, 577.612, 608.766, 210.63, 221.935], [15, 637.394, 705.596, 210.63, 221.935], [15, 777.1659999999999, 809.1619999999999, 210.63, 221.935], [15, 30.311999999999998, 165.03199999999998, 229.075, 240.975], [15, 284.596, 298.068, 229.075, 240.975], [15, 404.15999999999997, 411.738, 230.265, 240.38], [15, 471.52, 507.726, 230.265, 240.38], [15, 571.718, 608.766, 230.265, 240.38], [15, 648.34, 666.864, 230.265, 240.38], [15, 778.0079999999999, 808.3199999999999, 230.265, 240.38], [15, 30.311999999999998, 141.456, 245.73499999999999, 258.22999999999996], [15, 89.252, 100.198, 362.95, 374.255], [15, 563.298, 608.766, 363.54499999999996, 374.255], [15, 770.43, 808.3199999999999, 363.54499999999996, 374.255], [15, 84.2, 175.136, 390.32, 402.21999999999997], [15, 264.388, 351.114, 390.32, 402.21999999999997], [15, 577.612, 665.18, 390.32, 402.21999999999997], [15, 36.205999999999996, 47.994, 438.515, 464.09999999999997], [15, 84.2, 170.084, 507.53499999999997, 519.435], [15, 760.326, 827.6859999999999, 560.49, 572.39], [15, 760.326, 827.6859999999999, 576.555, 583.1]]
2026-08-05 05:23:33,544 INFO     29 [qwen-vl-text] ═══ DONE ═══ 36 positions, pages=1, time=18.0s
2026-08-05 05:23:33,544 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:23:33,544 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 05:23:33,545 INFO     29 [qwen-vl-text] positions(47): [[17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0], [17, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:23:33,545 INFO     29 [qwen-vl-text] page grouping: [17], lines per page: [47]
2026-08-05 05:23:33,794 INFO     29 [qwen-vl-text] page=17, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:23:33,797 INFO     29 [qwen-vl-text] LLM extraction start, text_len=506
2026-08-05 05:23:33,797 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:23:33,797 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 546, \"bbox_end\": 592, \"encounter_dates\": [\"2025-11-24\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "广东省医疗门诊收费票据（电子）\n广东省\n财政部监制\n票据代码：44\n票据号码：9148286284\n校验码：89a81f\n交款人\n开票日期：2025-11-24\n项目名称\n数量/单位\n金额（元）\n备注\n项目名称\n数量/单位\n金额（元）\n备注\n西药费\n1\n0.25\n以下是清单项\n醋酸泼尼松片（国基）\n6\n0.25\n金额合计（大写）贰角伍分\n(小写)0.25\n业务流水号：SF10481981\n门\n就诊日期：20251124\n其他信息\n医疗机构类型：综合医院\n医保类型：现金(自费)\n医保编号：\n性别：女\n医保统筹基金支付：0.00\n其他支付：0.00\n个人账户支付：0.00\n个人现金支付：0.25\n个人自付：0.00\n个人自费：0.25\n政策性减免：\n收款单位（章）\n人民医院\n复核人：吴亮梅\n收款人：吴亮梅\n说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。\n单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dipj.czt.gd.gov.cn/billcheck查验本省财政电子票据。\nCS 扫描全能王",
    "role": "user"
  }
]
[92m05:23:33 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:23:33,798 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:23:33,799 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:23:33.798+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 16, "failed": 0, "current": {"d7b98bb4908c11f1a3da71efcdd7cc1f": {"id": "d7b98bb4908c11f1a3da71efcdd7cc1f", "doc_id": "d7626528908c11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479738, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785907001430, "task_type": "dataflow", "root_trace_id": "ea6d5499d1eb4a3cabaa8fb5a06c80f8", "root_traceparent": "00-ea6d5499d1eb4a3cabaa8fb5a06c80f8-0f37f835e898f31c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:23:36,415 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:23:36,415 INFO     29 [qwen-vl-text] LLM output (len=406):
{
  "encounter_date": "2025-11-24",
  "pharmacy": "人民医院",
  "medications": [
    {
      "name": "醋酸泼尼松片（国基）",
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
  "payment_method": "现金(自费)"
}
2026-08-05 05:23:36,415 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-11-24]
2026-08-05 05:23:36,418 INFO     29 [qwen-vl-text] coord API call start, page=17, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=866040, prompt_len=1260
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共47行）
["广东省医疗门诊收费票据（电子）", "广东省", "财政部监制", "票据代码：44", "票据号码：9148286284", "校验码：89a81f", "交款人", "开票日期：2025-11-24", "项目名称", "数量/单位", "金额（元）", "备注", "项目名称", "数量/单位", "金额（元）", "备注", "西药费", "1", "0.25", "以下是清单项", "醋酸泼尼松片（国基）", "6", "0.25", "金额合计（大写）贰角伍分", "(小写)0.25", "业务流水号：SF10481981", "门", "就诊日期：20251124", "其他信息", "医疗机构类型：综合医院", "医保类型：现金(自费)", "医保编号：", "性别：女", "医保统筹基金支付：0.00", "其他支付：0.00", "个人账户支付：0.00", "个人现金支付：0.25", "个人自付：0.00", "个人自费：0.25", "政策性减免：", "收款单位（章）", "人民医院", "复核人：吴亮梅", "收款人：吴亮梅", "说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。", "单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dipj.czt.gd.gov.cn/billcheck查验本省财政电子票据。", "CS 扫描全能王"]

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
2026-08-05 05:24:00,477 INFO     29 [qwen-vl-text] coord API raw response (len=3923):
[
	{"text": "广东省医疗门诊收费票据（电子）", "bbox": [318, 57, 672, 93]},
	{"text": "广东省", "bbox": [478, 90, 522, 109], "bbox": [478, 90, 522, 109]},
	{"text": "财政部监制", "bbox": [465, 120, 538, 144]},
	{"text": "票据代码：44", "bbox": [116, 151, 188, 168], "bbox": [116, 151, 188, 168]},
	{"text": "交款人", "bbox": [116, 177, 152, 194], "bbox": [116, 177, 152, 194]},
	{"text": "票据号码：9148286284", "bbox": [629, 151, 746, 168], "bbox": [629, 151, 746, 168]},
	{"text": "校验码：89a81f", "bbox": [629, 177, 722, 194], "bbox": [629, 177, 722, 194]},
	{"text": "开票日期：2025-11-24", "bbox": [629, 202, 746, 219], "bbox": [629, 202, 746, 219]},
	{"text": "项目名称", "bbox": [179, 238, 228, 254], "bbox": [179, 238, 228, 254]},
	{"text": "数量/单位", "bbox": [306, 238, 366, 254], "bbox": [306, 238, 366, 254]},
	{"text": "金额（元）", "bbox": [389, 238, 443, 254], "bbox": [389, 238, 443, 254]},
	{"text": "备注", "bbox": [464, 238, 488, 254], "bbox": [464, 238, 488, 254]},
	{"text": "项目名称", "bbox": [562, 238, 611, 254], "bbox": [562, 238, 611, 254]},
	{"text": "数量/单位", "bbox": [687, 238, 745, 254], "bbox": [687, 238, 745, 254]},
	{"text": "金额（元）", "bbox": [769, 238, 821, 254], "bbox": [769, 238, 821, 254]},
	{"text": "备注", "bbox": [843, 238, 865, 254], "bbox": [843, 238, 865, 254]},
	{"text": "西药费", "bbox": [119, 273, 156, 290], "bbox": [119, 273, 156, 290]},
	{"text": "1", "bbox": [308, 274, 315, 290], "bbox": [308, 274, 315, 290]},
	{"text": "0.25", "bbox": [422, 274, 449, 290], "bbox": [422, 274, 449, 290]},
	{"text": "以下是清单项", "bbox": [119, 328, 193, 346], "bbox": [119, 328, 193, 346]},
	{"text": "醋酸泼尼松片（国基）", "bbox": [119, 359, 237, 376], "bbox": [119, 359, 237, 376]},
	{"text": "6", "bbox": [308, 360, 315, 376], "bbox": [308, 360, 315, 376]},
	{"text": "0.25", "bbox": [422, 360, 449, 376], "bbox": [422, 360, 449, 376]},
	{"text": "金额合计（大写）贰角伍分", "bbox": [123, 542, 267, 560], "bbox": [123, 542, 267, 560]},
	{"text": "(小写)0.25", "bbox": [552, 542, 615, 560], "bbox": [552, 542, 615, 560]},
	{"text": "业务流水号：SF10481981", "bbox": [147, 578, 276, 595], "bbox": [147, 578, 276, 595]},
	{"text": "门", "bbox": [344, 577, 355, 595], "bbox": [344, 577, 355, 595]},
	{"text": "就诊日期：20251124", "bbox": [713, 578, 817, 595], "bbox": [713, 578, 817, 595]},
	{"text": "其他信息", "bbox": [127, 609, 140, 743], "bbox": [127, 609, 140, 743]},
	{"text": "医疗机构类型：综合医院", "bbox": [147, 623, 277, 640], "bbox": [147, 623, 277, 640]},
	{"text": "医保类型：现金(自费)", "bbox": [344, 623, 458, 640], "bbox": [344, 623, 458, 640]},
	{"text": "医保编号：", "bbox": [518, 623, 570, 640], "bbox": [518, 623, 570, 640]},
	{"text": "性别：女", "bbox": [713, 623, 757, 640], "bbox": [713, 623, 757, 640]},
	{"text": "医保统筹基金支付：0.00", "bbox": [147, 668, 277, 685], "bbox": [147, 668, 277, 685]},
	{"text": "其他支付：0.00", "bbox": [344, 668, 423, 685], "bbox": [344, 668, 423, 685]},
	{"text": "个人账户支付：0.00", "bbox": [518, 668, 623, 685], "bbox": [518, 668, 623, 685]},
	{"text": "个人现金支付：0.25", "bbox": [713, 668, 817, 685], "bbox": [713, 668, 817, 685]},
	{"text": "个人自付：0.00", "bbox": [147, 708, 230, 725], "bbox": [147, 708, 230, 725]},
	{"text": "个人自费：0.25", "bbox": [344, 708, 423, 725], "bbox": [344, 708, 423, 725]},
	{"text": "政策性减免：", "bbox": [344, 743, 411, 761], "bbox": [344, 743, 411, 761]},
	{"text": "收款单位（章）", "bbox": [121, 790, 202, 809], "bbox": [121, 790, 202, 809]},
	{"text": "人民医院", "bbox": [328, 788, 367, 807], "bbox": [328, 788, 367, 807]},
	{"text": "复核人：吴亮梅", "bbox": [557, 788, 637, 807], "bbox": [557, 788, 637, 807]},
	{"text": "收款人：吴亮梅", "bbox": [717, 788, 797, 807], "bbox": [717, 788, 797, 807]},
	{"text": "说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。", "bbox": [135, 825, 819, 842], "bbox": [135, 825, 819, 842]},
	{"text": "单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dipj.czt.gd.gov.cn/billcheck查验本省财政电子票据。", "bbox": [178, 842, 797, 859], "bbox": [178, 842, 797, 859]},
	{"text": "CS 扫描全能王", "bbox": [903, 943, 984, 962], "bbox": [903, 943, 984, 962]}
]
2026-08-05 05:24:00,477 INFO     29 [qwen-vl-text] coord API: raw_items=47, valid_items=47, elapsed=24.1s
2026-08-05 05:24:00,477 INFO     29 [qwen-vl-text] coord item[0]: text=广东省医疗门诊收费票据（电子）, bbox=[318, 57, 672, 93]
2026-08-05 05:24:00,477 INFO     29 [qwen-vl-text] coord item[1]: text=广东省, bbox=[478, 90, 522, 109]
2026-08-05 05:24:00,477 INFO     29 [qwen-vl-text] coord item[2]: text=财政部监制, bbox=[465, 120, 538, 144]
2026-08-05 05:24:00,478 INFO     29 [qwen-vl-text] coord item[3]: text=票据代码：44, bbox=[116, 151, 188, 168]
2026-08-05 05:24:00,478 INFO     29 [qwen-vl-text] coord item[4]: text=交款人, bbox=[116, 177, 152, 194]
2026-08-05 05:24:00,478 INFO     29 [qwen-vl-text] coord item[5]: text=票据号码：9148286284, bbox=[629, 151, 746, 168]
2026-08-05 05:24:00,478 INFO     29 [qwen-vl-text] coord item[6]: text=校验码：89a81f, bbox=[629, 177, 722, 194]
2026-08-05 05:24:00,478 INFO     29 [qwen-vl-text] coord item[7]: text=开票日期：2025-11-24, bbox=[629, 202, 746, 219]
2026-08-05 05:24:00,478 INFO     29 [qwen-vl-text] coord item[8]: text=项目名称, bbox=[179, 238, 228, 254]
2026-08-05 05:24:00,478 INFO     29 [qwen-vl-text] coord item[9]: text=数量/单位, bbox=[306, 238, 366, 254]
2026-08-05 05:24:00,478 INFO     29 [qwen-vl-text] coord item[10]: text=金额（元）, bbox=[389, 238, 443, 254]
2026-08-05 05:24:00,478 INFO     29 [qwen-vl-text] coord item[11]: text=备注, bbox=[464, 238, 488, 254]
2026-08-05 05:24:00,478 INFO     29 [qwen-vl-text] coord item[12]: text=项目名称, bbox=[562, 238, 611, 254]
2026-08-05 05:24:00,478 INFO     29 [qwen-vl-text] coord item[13]: text=数量/单位, bbox=[687, 238, 745, 254]
2026-08-05 05:24:00,478 INFO     29 [qwen-vl-text] coord item[14]: text=金额（元）, bbox=[769, 238, 821, 254]
2026-08-05 05:24:00,478 INFO     29 [qwen-vl-text] coord item[15]: text=备注, bbox=[843, 238, 865, 254]
2026-08-05 05:24:00,478 INFO     29 [qwen-vl-text] coord item[16]: text=西药费, bbox=[119, 273, 156, 290]
2026-08-05 05:24:00,478 INFO     29 [qwen-vl-text] coord item[17]: text=1, bbox=[308, 274, 315, 290]
2026-08-05 05:24:00,478 INFO     29 [qwen-vl-text] coord item[18]: text=0.25, bbox=[422, 274, 449, 290]
2026-08-05 05:24:00,478 INFO     29 [qwen-vl-text] coord item[19]: text=以下是清单项, bbox=[119, 328, 193, 346]
2026-08-05 05:24:00,478 INFO     29 [qwen-vl-text] coord item[20]: text=醋酸泼尼松片（国基）, bbox=[119, 359, 237, 376]
2026-08-05 05:24:00,478 INFO     29 [qwen-vl-text] coord item[21]: text=6, bbox=[308, 360, 315, 376]
2026-08-05 05:24:00,478 INFO     29 [qwen-vl-text] coord item[22]: text=0.25, bbox=[422, 360, 449, 376]
2026-08-05 05:24:00,478 INFO     29 [qwen-vl-text] coord item[23]: text=金额合计（大写）贰角伍分, bbox=[123, 542, 267, 560]
2026-08-05 05:24:00,478 INFO     29 [qwen-vl-text] coord item[24]: text=(小写)0.25, bbox=[552, 542, 615, 560]
2026-08-05 05:24:00,479 INFO     29 [qwen-vl-text] coord item[25]: text=业务流水号：SF10481981, bbox=[147, 578, 276, 595]
2026-08-05 05:24:00,479 INFO     29 [qwen-vl-text] coord item[26]: text=门, bbox=[344, 577, 355, 595]
2026-08-05 05:24:00,479 INFO     29 [qwen-vl-text] coord item[27]: text=就诊日期：20251124, bbox=[713, 578, 817, 595]
2026-08-05 05:24:00,479 INFO     29 [qwen-vl-text] coord item[28]: text=其他信息, bbox=[127, 609, 140, 743]
2026-08-05 05:24:00,479 INFO     29 [qwen-vl-text] coord item[29]: text=医疗机构类型：综合医院, bbox=[147, 623, 277, 640]
2026-08-05 05:24:00,479 INFO     29 [qwen-vl-text] coord item[30]: text=医保类型：现金(自费), bbox=[344, 623, 458, 640]
2026-08-05 05:24:00,479 INFO     29 [qwen-vl-text] coord item[31]: text=医保编号：, bbox=[518, 623, 570, 640]
2026-08-05 05:24:00,479 INFO     29 [qwen-vl-text] coord item[32]: text=性别：女, bbox=[713, 623, 757, 640]
2026-08-05 05:24:00,479 INFO     29 [qwen-vl-text] coord item[33]: text=医保统筹基金支付：0.00, bbox=[147, 668, 277, 685]
2026-08-05 05:24:00,479 INFO     29 [qwen-vl-text] coord item[34]: text=其他支付：0.00, bbox=[344, 668, 423, 685]
2026-08-05 05:24:00,479 INFO     29 [qwen-vl-text] coord item[35]: text=个人账户支付：0.00, bbox=[518, 668, 623, 685]
2026-08-05 05:24:00,479 INFO     29 [qwen-vl-text] coord item[36]: text=个人现金支付：0.25, bbox=[713, 668, 817, 685]
2026-08-05 05:24:00,479 INFO     29 [qwen-vl-text] coord item[37]: text=个人自付：0.00, bbox=[147, 708, 230, 725]
2026-08-05 05:24:00,479 INFO     29 [qwen-vl-text] coord item[38]: text=个人自费：0.25, bbox=[344, 708, 423, 725]
2026-08-05 05:24:00,479 INFO     29 [qwen-vl-text] coord item[39]: text=政策性减免：, bbox=[344, 743, 411, 761]
2026-08-05 05:24:00,479 INFO     29 [qwen-vl-text] coord item[40]: text=收款单位（章）, bbox=[121, 790, 202, 809]
2026-08-05 05:24:00,479 INFO     29 [qwen-vl-text] coord item[41]: text=人民医院, bbox=[328, 788, 367, 807]
2026-08-05 05:24:00,479 INFO     29 [qwen-vl-text] coord item[42]: text=复核人：吴亮梅, bbox=[557, 788, 637, 807]
2026-08-05 05:24:00,479 INFO     29 [qwen-vl-text] coord item[43]: text=收款人：吴亮梅, bbox=[717, 788, 797, 807]
2026-08-05 05:24:00,479 INFO     29 [qwen-vl-text] coord item[44]: text=说明：财政电子票据是财务收支和会计核算的原始凭证，财政电子票据和纸质票据具有同等法律效力，是财会监督、审计监督等的重要依据。, bbox=[135, 825, 819, 842]
2026-08-05 05:24:00,479 INFO     29 [qwen-vl-text] coord item[45]: text=单位或个人可关注“广东财政”公众号或登录广东省财政电子票据查验网http://dipj.czt.gd.gov.cn/billcheck查验本省财政电子票据。, bbox=[178, 842, 797, 859]
2026-08-05 05:24:00,479 INFO     29 [qwen-vl-text] coord item[46]: text=CS 扫描全能王, bbox=[903, 943, 984, 962]
2026-08-05 05:24:00,479 INFO     29 [qwen-vl-text] page=17 — 47/47 coords, api_time=24.1s
2026-08-05 05:24:00,480 INFO     29 [qwen-vl-text] new_positions (47):
[[17, 267.756, 565.824, 33.915, 55.335], [17, 402.476, 439.524, 53.55, 64.855], [17, 391.53, 452.996, 71.39999999999999, 85.67999999999999], [17, 97.672, 158.296, 89.845, 99.96], [17, 97.672, 127.984, 105.315, 115.42999999999999], [17, 529.6179999999999, 628.132, 89.845, 99.96], [17, 529.6179999999999, 607.924, 105.315, 115.42999999999999], [17, 529.6179999999999, 628.132, 120.19, 130.305], [17, 150.718, 191.976, 141.60999999999999, 151.13], [17, 257.652, 308.17199999999997, 141.60999999999999, 151.13], [17, 327.538, 373.006, 141.60999999999999, 151.13], [17, 390.688, 410.89599999999996, 141.60999999999999, 151.13], [17, 473.204, 514.462, 141.60999999999999, 151.13], [17, 578.454, 627.29, 141.60999999999999, 151.13], [17, 647.4979999999999, 691.2819999999999, 141.60999999999999, 151.13], [17, 709.8059999999999, 728.3299999999999, 141.60999999999999, 151.13], [17, 100.198, 131.352, 162.435, 172.54999999999998], [17, 259.336, 265.23, 163.03, 172.54999999999998], [17, 355.324, 378.058, 163.03, 172.54999999999998], [17, 100.198, 162.506, 195.16, 205.87], [17, 100.198, 199.554, 213.605, 223.72], [17, 259.336, 265.23, 214.2, 223.72], [17, 355.324, 378.058, 214.2, 223.72], [17, 103.566, 224.814, 322.49, 333.2], [17, 464.784, 517.8299999999999, 322.49, 333.2], [17, 123.774, 232.392, 343.90999999999997, 354.025], [17, 289.64799999999997, 298.90999999999997, 343.315, 354.025], [17, 600.346, 687.914, 343.90999999999997, 354.025], [17, 106.934, 117.88, 362.35499999999996, 442.085], [17, 123.774, 233.23399999999998, 370.685, 380.79999999999995], [17, 289.64799999999997, 385.63599999999997, 370.685, 380.79999999999995], [17, 436.156, 479.94, 370.685, 380.79999999999995], [17, 600.346, 637.394, 370.685, 380.79999999999995], [17, 123.774, 233.23399999999998, 397.46, 407.575], [17, 289.64799999999997, 356.166, 397.46, 407.575], [17, 436.156, 524.566, 397.46, 407.575], [17, 600.346, 687.914, 397.46, 407.575], [17, 123.774, 193.66, 421.26, 431.375], [17, 289.64799999999997, 356.166, 421.26, 431.375], [17, 289.64799999999997, 346.062, 442.085, 452.79499999999996], [17, 101.88199999999999, 170.084, 470.04999999999995, 481.35499999999996], [17, 276.176, 309.014, 468.85999999999996, 480.16499999999996], [17, 468.99399999999997, 536.3539999999999, 468.85999999999996, 480.16499999999996], [17, 603.7139999999999, 671.074, 468.85999999999996, 480.16499999999996], [17, 113.67, 689.598, 490.875, 500.98999999999995], [17, 149.876, 671.074, 500.98999999999995, 511.10499999999996], [17, 760.326, 828.528, 561.0849999999999, 572.39]]
2026-08-05 05:24:00,480 INFO     29 [qwen-vl-text] ═══ DONE ═══ 47 positions, pages=1, time=26.9s
2026-08-05 05:24:00,480 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:24:00,480 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 05:24:00,480 INFO     29 [qwen-vl-text] positions(46): [[18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0], [18, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:24:00,480 INFO     29 [qwen-vl-text] page grouping: [18], lines per page: [46]
2026-08-05 05:24:00,634 INFO     29 [qwen-vl-text] page=18, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 05:24:00,636 INFO     29 [qwen-vl-text] LLM extraction start, text_len=408
2026-08-05 05:24:00,637 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:24:00,637 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 594, \"bbox_end\": 639, \"encounter_dates\": [\"2026-01-20\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "10:15\n淘\n交易成功\n医药仁康堂医药专营店>\n【信必可】布地奈德福莫特罗\n¥213\n放心买药\n正品保障\n1盒装\n不支持7天无理由 假一赔四>\nx1\n专业药师在线服务\n上天猫放心买药\n用药小贴士 1.哮喘。2.慢性阻塞性肺疾病(慢阻肺;...\n申请售后\n商品总价\n¥213\n运费(含服务费)\n¥8\n应付款\n¥221^\n订单信息 2026-01-20\n收起^\n订单编号\n4501919772001020746\n交易快照\n发生交易争议时，可作为判断依据>\n成交时间\n2026-01-26 22:25:02\n发货时间\n2026-01-21 12:24:52\n付款时间\n2026-01-20 19:25:06\n创建时间\n2026-01-20 19:24:30\n支付宝交易号\n2026012022001134951454085519\n天猫积分\n获得106点积分>\n客服\n更多\n查看处方\n查看物流\n评价\n扫描全能王\n扫描全能王",
    "role": "user"
  }
]
[92m05:24:00 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:24:00,638 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:24:03,207 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:24:03,208 INFO     29 [qwen-vl-text] LLM output (len=405):
{
  "encounter_date": "2026-01-20",
  "pharmacy": "仁康堂医药专营店",
  "medications": [
    {
      "name": "信必可布地奈德福莫特罗",
      "specification": null,
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
2026-08-05 05:24:03,208 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-20]
2026-08-05 05:24:03,210 INFO     29 [qwen-vl-text] coord API call start, page=18, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=822515, prompt_len=1159
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共46行）
["10:15", "淘", "交易成功", "医药仁康堂医药专营店>", "【信必可】布地奈德福莫特罗", "¥213", "放心买药", "正品保障", "1盒装", "不支持7天无理由 假一赔四>", "x1", "专业药师在线服务", "上天猫放心买药", "用药小贴士 1.哮喘。2.慢性阻塞性肺疾病(慢阻肺;...", "申请售后", "商品总价", "¥213", "运费(含服务费)", "¥8", "应付款", "¥221^", "订单信息 2026-01-20", "收起^", "订单编号", "4501919772001020746", "交易快照", "发生交易争议时，可作为判断依据>", "成交时间", "2026-01-26 22:25:02", "发货时间", "2026-01-21 12:24:52", "付款时间", "2026-01-20 19:25:06", "创建时间", "2026-01-20 19:24:30", "支付宝交易号", "2026012022001134951454085519", "天猫积分", "获得106点积分>", "客服", "更多", "查看处方", "查看物流", "评价", "扫描全能王", "扫描全能王"]

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
2026-08-05 05:24:24,103 INFO     29 [qwen-vl-text] coord API raw response (len=3775):
[
	{"text": "10:15", "bbox": [233, 13, 291, 28]},
	{"text": "淘", "bbox": [320, 13, 343, 27], "bbox": [320, 13, 343, 27]},
	{"text": "交易成功", "bbox": [435, 57, 561, 80], "bbox": [435, 57, 561, 80]},
	{"text": "医药仁康堂医药专营店>", "bbox": [224, 137, 466, 153], "bbox": [224, 137, 466, 153]},
	{"text": "【信必可】布地奈德福莫特罗", "bbox": [382, 176, 666, 193], "bbox": [382, 176, 666, 193]},
	{"text": "¥213", "bbox": [717, 177, 770, 194], "bbox": [717, 177, 770, 194]},
	{"text": "放心买药", "bbox": [304, 196, 340, 203], "bbox": [304, 196, 340, 203]},
	{"text": "正品保障", "bbox": [303, 207, 341, 214], "bbox": [303, 207, 341, 214]},
	{"text": "1盒装", "bbox": [370, 204, 422, 219], "bbox": [370, 204, 422, 219]},
	{"text": "不支持7天无理由 假一赔四>", "bbox": [370, 230, 616, 245], "bbox": [370, 230, 616, 245]},
	{"text": "x1", "bbox": [748, 231, 770, 245], "bbox": [748, 231, 770, 245]},
	{"text": "专业药师在线服务", "bbox": [264, 239, 314, 245], "bbox": [264, 239, 314, 245]},
	{"text": "上天猫放心买药", "bbox": [260, 247, 318, 254], "bbox": [260, 247, 318, 254]},
	{"text": "用药小贴士 1.哮喘。2.慢性阻塞性肺疾病(慢阻肺;...", "bbox": [237, 275, 709, 291], "bbox": [237, 275, 709, 291]},
	{"text": "申请售后", "bbox": [667, 317, 748, 333], "bbox": [667, 317, 748, 333]},
	{"text": "商品总价", "bbox": [225, 367, 321, 384], "bbox": [225, 367, 321, 384]},
	{"text": "¥213", "bbox": [715, 369, 770, 386], "bbox": [715, 369, 770, 386]},
	{"text": "运费(含服务费)", "bbox": [225, 411, 365, 427], "bbox": [225, 411, 365, 427]},
	{"text": "¥8", "bbox": [738, 412, 770, 428], "bbox": [738, 412, 770, 428]},
	{"text": "应付款", "bbox": [225, 457, 298, 474], "bbox": [225, 457, 298, 474]},
	{"text": "¥221^", "bbox": [680, 455, 770, 475], "bbox": [680, 455, 770, 475]},
	{"text": "订单信息 2026-01-20", "bbox": [225, 520, 442, 536], "bbox": [225, 520, 442, 536]},
	{"text": "收起^", "bbox": [706, 520, 770, 536], "bbox": [706, 520, 770, 536]},
	{"text": "订单编号", "bbox": [225, 558, 309, 574], "bbox": [225, 558, 309, 574]},
	{"text": "4501919772001020746", "bbox": [547, 558, 770, 574], "bbox": [547, 558, 770, 574]},
	{"text": "交易快照", "bbox": [225, 595, 309, 611], "bbox": [225, 595, 309, 611]},
	{"text": "发生交易争议时，可作为判断依据>", "bbox": [436, 595, 763, 611], "bbox": [436, 595, 763, 611]},
	{"text": "成交时间", "bbox": [225, 632, 309, 648], "bbox": [225, 632, 309, 648]},
	{"text": "2026-01-26 22:25:02", "bbox": [569, 632, 770, 648], "bbox": [569, 632, 770, 648]},
	{"text": "发货时间", "bbox": [225, 669, 309, 685], "bbox": [225, 669, 309, 685]},
	{"text": "2026-01-21 12:24:52", "bbox": [569, 669, 770, 685], "bbox": [569, 669, 770, 685]},
	{"text": "付款时间", "bbox": [225, 705, 309, 721], "bbox": [225, 705, 309, 721]},
	{"text": "2026-01-20 19:25:06", "bbox": [569, 705, 770, 721], "bbox": [569, 705, 770, 721]},
	{"text": "创建时间", "bbox": [225, 741, 309, 757], "bbox": [225, 741, 309, 757]},
	{"text": "2026-01-20 19:24:30", "bbox": [569, 741, 770, 757], "bbox": [569, 741, 770, 757]},
	{"text": "支付宝交易号", "bbox": [225, 777, 351, 793], "bbox": [225, 777, 351, 793]},
	{"text": "2026012022001134951454085519", "bbox": [442, 777, 770, 793], "bbox": [442, 777, 770, 793]},
	{"text": "天猫积分", "bbox": [225, 814, 309, 830], "bbox": [225, 814, 309, 830]},
	{"text": "获得106点积分>", "bbox": [607, 814, 763, 830], "bbox": [607, 814, 763, 830]},
	{"text": "客服", "bbox": [222, 877, 255, 889], "bbox": [222, 877, 255, 889]},
	{"text": "更多", "bbox": [275, 877, 306, 889], "bbox": [275, 877, 306, 889]},
	{"text": "查看处方", "bbox": [369, 865, 452, 880], "bbox": [369, 865, 452, 880]},
	{"text": "查看物流", "bbox": [518, 865, 601, 880], "bbox": [518, 865, 601, 880]},
	{"text": "评价", "bbox": [688, 865, 728, 880], "bbox": [688, 865, 728, 880]},
	{"text": "扫描全能王", "bbox": [755, 914, 788, 921], "bbox": [755, 914, 788, 921]},
	{"text": "扫描全能王", "bbox": [890, 960, 976, 974], "bbox": [890, 960, 976, 974]}
]
2026-08-05 05:24:24,104 INFO     29 [qwen-vl-text] coord API: raw_items=46, valid_items=46, elapsed=20.9s
2026-08-05 05:24:24,104 INFO     29 [qwen-vl-text] coord item[0]: text=10:15, bbox=[233, 13, 291, 28]
2026-08-05 05:24:24,104 INFO     29 [qwen-vl-text] coord item[1]: text=淘, bbox=[320, 13, 343, 27]
2026-08-05 05:24:24,104 INFO     29 [qwen-vl-text] coord item[2]: text=交易成功, bbox=[435, 57, 561, 80]
2026-08-05 05:24:24,104 INFO     29 [qwen-vl-text] coord item[3]: text=医药仁康堂医药专营店>, bbox=[224, 137, 466, 153]
2026-08-05 05:24:24,105 INFO     29 [qwen-vl-text] coord item[4]: text=【信必可】布地奈德福莫特罗, bbox=[382, 176, 666, 193]
2026-08-05 05:24:24,105 INFO     29 [qwen-vl-text] coord item[5]: text=¥213, bbox=[717, 177, 770, 194]
2026-08-05 05:24:24,105 INFO     29 [qwen-vl-text] coord item[6]: text=放心买药, bbox=[304, 196, 340, 203]
2026-08-05 05:24:24,105 INFO     29 [qwen-vl-text] coord item[7]: text=正品保障, bbox=[303, 207, 341, 214]
2026-08-05 05:24:24,105 INFO     29 [qwen-vl-text] coord item[8]: text=1盒装, bbox=[370, 204, 422, 219]
2026-08-05 05:24:24,105 INFO     29 [qwen-vl-text] coord item[9]: text=不支持7天无理由 假一赔四>, bbox=[370, 230, 616, 245]
2026-08-05 05:24:24,105 INFO     29 [qwen-vl-text] coord item[10]: text=x1, bbox=[748, 231, 770, 245]
2026-08-05 05:24:24,105 INFO     29 [qwen-vl-text] coord item[11]: text=专业药师在线服务, bbox=[264, 239, 314, 245]
2026-08-05 05:24:24,105 INFO     29 [qwen-vl-text] coord item[12]: text=上天猫放心买药, bbox=[260, 247, 318, 254]
2026-08-05 05:24:24,105 INFO     29 [qwen-vl-text] coord item[13]: text=用药小贴士 1.哮喘。2.慢性阻塞性肺疾病(慢阻肺;..., bbox=[237, 275, 709, 291]
2026-08-05 05:24:24,105 INFO     29 [qwen-vl-text] coord item[14]: text=申请售后, bbox=[667, 317, 748, 333]
2026-08-05 05:24:24,105 INFO     29 [qwen-vl-text] coord item[15]: text=商品总价, bbox=[225, 367, 321, 384]
2026-08-05 05:24:24,105 INFO     29 [qwen-vl-text] coord item[16]: text=¥213, bbox=[715, 369, 770, 386]
2026-08-05 05:24:24,105 INFO     29 [qwen-vl-text] coord item[17]: text=运费(含服务费), bbox=[225, 411, 365, 427]
2026-08-05 05:24:24,105 INFO     29 [qwen-vl-text] coord item[18]: text=¥8, bbox=[738, 412, 770, 428]
2026-08-05 05:24:24,105 INFO     29 [qwen-vl-text] coord item[19]: text=应付款, bbox=[225, 457, 298, 474]
2026-08-05 05:24:24,105 INFO     29 [qwen-vl-text] coord item[20]: text=¥221^, bbox=[680, 455, 770, 475]
2026-08-05 05:24:24,105 INFO     29 [qwen-vl-text] coord item[21]: text=订单信息 2026-01-20, bbox=[225, 520, 442, 536]
2026-08-05 05:24:24,105 INFO     29 [qwen-vl-text] coord item[22]: text=收起^, bbox=[706, 520, 770, 536]
2026-08-05 05:24:24,105 INFO     29 [qwen-vl-text] coord item[23]: text=订单编号, bbox=[225, 558, 309, 574]
2026-08-05 05:24:24,106 INFO     29 [qwen-vl-text] coord item[24]: text=4501919772001020746, bbox=[547, 558, 770, 574]
2026-08-05 05:24:24,106 INFO     29 [qwen-vl-text] coord item[25]: text=交易快照, bbox=[225, 595, 309, 611]
2026-08-05 05:24:24,106 INFO     29 [qwen-vl-text] coord item[26]: text=发生交易争议时，可作为判断依据>, bbox=[436, 595, 763, 611]
2026-08-05 05:24:24,106 INFO     29 [qwen-vl-text] coord item[27]: text=成交时间, bbox=[225, 632, 309, 648]
2026-08-05 05:24:24,106 INFO     29 [qwen-vl-text] coord item[28]: text=2026-01-26 22:25:02, bbox=[569, 632, 770, 648]
2026-08-05 05:24:24,106 INFO     29 [qwen-vl-text] coord item[29]: text=发货时间, bbox=[225, 669, 309, 685]
2026-08-05 05:24:24,106 INFO     29 [qwen-vl-text] coord item[30]: text=2026-01-21 12:24:52, bbox=[569, 669, 770, 685]
2026-08-05 05:24:24,106 INFO     29 [qwen-vl-text] coord item[31]: text=付款时间, bbox=[225, 705, 309, 721]
2026-08-05 05:24:24,106 INFO     29 [qwen-vl-text] coord item[32]: text=2026-01-20 19:25:06, bbox=[569, 705, 770, 721]
2026-08-05 05:24:24,106 INFO     29 [qwen-vl-text] coord item[33]: text=创建时间, bbox=[225, 741, 309, 757]
2026-08-05 05:24:24,106 INFO     29 [qwen-vl-text] coord item[34]: text=2026-01-20 19:24:30, bbox=[569, 741, 770, 757]
2026-08-05 05:24:24,106 INFO     29 [qwen-vl-text] coord item[35]: text=支付宝交易号, bbox=[225, 777, 351, 793]
2026-08-05 05:24:24,106 INFO     29 [qwen-vl-text] coord item[36]: text=2026012022001134951454085519, bbox=[442, 777, 770, 793]
2026-08-05 05:24:24,106 INFO     29 [qwen-vl-text] coord item[37]: text=天猫积分, bbox=[225, 814, 309, 830]
2026-08-05 05:24:24,107 INFO     29 [qwen-vl-text] coord item[38]: text=获得106点积分>, bbox=[607, 814, 763, 830]
2026-08-05 05:24:24,107 INFO     29 [qwen-vl-text] coord item[39]: text=客服, bbox=[222, 877, 255, 889]
2026-08-05 05:24:24,107 INFO     29 [qwen-vl-text] coord item[40]: text=更多, bbox=[275, 877, 306, 889]
2026-08-05 05:24:24,107 INFO     29 [qwen-vl-text] coord item[41]: text=查看处方, bbox=[369, 865, 452, 880]
2026-08-05 05:24:24,107 INFO     29 [qwen-vl-text] coord item[42]: text=查看物流, bbox=[518, 865, 601, 880]
2026-08-05 05:24:24,107 INFO     29 [qwen-vl-text] coord item[43]: text=评价, bbox=[688, 865, 728, 880]
2026-08-05 05:24:24,107 INFO     29 [qwen-vl-text] coord item[44]: text=扫描全能王, bbox=[755, 914, 788, 921]
2026-08-05 05:24:24,107 INFO     29 [qwen-vl-text] coord item[45]: text=扫描全能王, bbox=[890, 960, 976, 974]
2026-08-05 05:24:24,108 INFO     29 [qwen-vl-text] page=18 — 46/46 coords, api_time=20.9s
2026-08-05 05:24:24,108 INFO     29 [qwen-vl-text] new_positions (46):
[[18, 138.635, 173.14499999999998, 10.946, 23.576], [18, 190.39999999999998, 204.08499999999998, 10.946, 22.733999999999998], [18, 258.825, 333.79499999999996, 47.994, 67.36], [18, 133.28, 277.27, 115.354, 128.826], [18, 227.29, 396.27, 148.192, 162.506], [18, 426.615, 458.15, 149.034, 163.34799999999998], [18, 180.88, 202.29999999999998, 165.03199999999998, 170.926], [18, 180.285, 202.89499999999998, 174.29399999999998, 180.188], [18, 220.14999999999998, 251.08999999999997, 171.768, 184.398], [18, 220.14999999999998, 366.52, 193.66, 206.29], [18, 445.06, 458.15, 194.50199999999998, 206.29], [18, 157.07999999999998, 186.82999999999998, 201.238, 206.29], [18, 154.7, 189.20999999999998, 207.974, 213.868], [18, 141.015, 421.85499999999996, 231.54999999999998, 245.022], [18, 396.865, 445.06, 266.914, 280.38599999999997], [18, 133.875, 190.995, 309.014, 323.328], [18, 425.42499999999995, 458.15, 310.698, 325.012], [18, 133.875, 217.17499999999998, 346.062, 359.534], [18, 439.10999999999996, 458.15, 346.904, 360.376], [18, 133.875, 177.31, 384.794, 399.108], [18, 404.59999999999997, 458.15, 383.11, 399.95], [18, 133.875, 262.99, 437.84, 451.312], [18, 420.07, 458.15, 437.84, 451.312], [18, 133.875, 183.855, 469.83599999999996, 483.308], [18, 325.465, 458.15, 469.83599999999996, 483.308], [18, 133.875, 183.855, 500.99, 514.462], [18, 259.42, 453.98499999999996, 500.99, 514.462], [18, 133.875, 183.855, 532.144, 545.616], [18, 338.555, 458.15, 532.144, 545.616], [18, 133.875, 183.855, 563.298, 576.77], [18, 338.555, 458.15, 563.298, 576.77], [18, 133.875, 183.855, 593.61, 607.082], [18, 338.555, 458.15, 593.61, 607.082], [18, 133.875, 183.855, 623.922, 637.394], [18, 338.555, 458.15, 623.922, 637.394], [18, 133.875, 208.845, 654.2339999999999, 667.706], [18, 262.99, 458.15, 654.2339999999999, 667.706], [18, 133.875, 183.855, 685.3879999999999, 698.86], [18, 361.16499999999996, 453.98499999999996, 685.3879999999999, 698.86], [18, 132.09, 151.725, 738.434, 748.538], [18, 163.625, 182.07, 738.434, 748.538], [18, 219.55499999999998, 268.94, 728.3299999999999, 740.9599999999999], [18, 308.21, 357.59499999999997, 728.3299999999999, 740.9599999999999], [18, 409.35999999999996, 433.15999999999997, 728.3299999999999, 740.9599999999999], [18, 449.22499999999997, 468.85999999999996, 769.588, 775.482], [18, 529.55, 580.72, 808.3199999999999, 820.108]]
2026-08-05 05:24:24,108 INFO     29 [qwen-vl-text] ═══ DONE ═══ 46 positions, pages=1, time=23.6s
2026-08-05 05:24:24,108 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 05:24:24,108 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 05:24:24,108 INFO     29 [qwen-vl-text] positions(35): [[19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0], [19, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 05:24:24,109 INFO     29 [qwen-vl-text] page grouping: [19], lines per page: [35]
2026-08-05 05:24:24,347 INFO     29 [qwen-vl-text] page=19, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 05:24:24,350 INFO     29 [qwen-vl-text] LLM extraction start, text_len=306
2026-08-05 05:24:24,350 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:24:24,350 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 641, \"bbox_end\": 675, \"encounter_dates\": [\"2026-02-02\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "电子发票(普通发票)\n发票号码：26322000000914042776\n开票日期：2026年02月02日\n江苏省税务局\n购买方信息\n名称：\n统一社会信用代码/纳税人识别号：\n销售方信息\n名称：阜宁仁康堂大药房有限公司\n统一社会信用代码/纳税人识别号：91320923MAK1XP619R\n项目名称\n规格型号\n单位\n数量\n单价\n金额\n税率/征收率\n税额\n*生物化学药品*其他生物\n化学药品\n1\n218.811881188119\n218.81\n1%\n2.19\n合计\n¥218.81\n¥2.19\n价税合计（大写）\n贰佰贰拾壹圆整\n(小写)¥221.00\n备注\n开票人：杨雪\nCS 扫描全能王\n3亿人都在用的扫描App",
    "role": "user"
  }
]
[92m05:24:24 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:24:24,352 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:24:24,352 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T05:24:24.351+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 16, "failed": 0, "current": {"d7b98bb4908c11f1a3da71efcdd7cc1f": {"id": "d7b98bb4908c11f1a3da71efcdd7cc1f", "doc_id": "d7626528908c11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479738, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785907001430, "task_type": "dataflow", "root_trace_id": "ea6d5499d1eb4a3cabaa8fb5a06c80f8", "root_traceparent": "00-ea6d5499d1eb4a3cabaa8fb5a06c80f8-0f37f835e898f31c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 05:24:27,264 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:24:27,264 INFO     29 [qwen-vl-text] LLM output (len=414):
{
  "encounter_date": "2026-02-02",
  "pharmacy": "阜宁仁康堂大药房有限公司",
  "medications": [
    {
      "name": "其他生物化学药品",
      "specification": null,
      "dosage": null,
      "quantity": 1,
      "unit_price": 218.81,
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
2026-08-05 05:24:27,264 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-02]
2026-08-05 05:24:27,267 INFO     29 [qwen-vl-text] coord API call start, page=19, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=918020, prompt_len=1024
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共35行）
["电子发票(普通发票)", "发票号码：26322000000914042776", "开票日期：2026年02月02日", "江苏省税务局", "购买方信息", "名称：", "统一社会信用代码/纳税人识别号：", "销售方信息", "名称：阜宁仁康堂大药房有限公司", "统一社会信用代码/纳税人识别号：91320923MAK1XP619R", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*生物化学药品*其他生物", "化学药品", "1", "218.811881188119", "218.81", "1%", "2.19", "合计", "¥218.81", "¥2.19", "价税合计（大写）", "贰佰贰拾壹圆整", "(小写)¥221.00", "备注", "开票人：杨雪", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord API raw response (len=2923):
[
	{"text": "电子发票(普通发票)", "bbox": [328, 54, 640, 98]},
	{"text": "发票号码：26322000000914042776", "bbox": [733, 74, 955, 94]},
	{"text": "开票日期：2026年02月02日", "bbox": [732, 114, 908, 134]},
	{"text": "江苏省税务局", "bbox": [461, 146, 535, 168]},
	{"text": "购买方信息", "bbox": [33, 217, 46, 330], "bbox_2d": [33, 217, 46, 330]},
	{"text": "名称：", "bbox": [61, 224, 100, 244], "bbox_2d": [61, 224, 209, 260]},
	{"text": "统一社会信用代码/纳税人识别号：", "bbox": [60, 295, 257, 314], "bbox_2d": [60, 295, 257, 314]},
	{"text": "销售方信息", "bbox": [507, 217, 519, 330], "bbox_2d": [507, 217, 519, 330]},
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
	{"text": "化学药品", "bbox": [26, 405, 86, 425], "bbox_2d": [26, 405, 86, 425]},
	{"text": "1", "bbox": [480, 380, 488, 396], "bbox_2d": [480, 380, 488, 396]},
	{"text": "218.811881188119", "bbox": [498, 380, 604, 396], "bbox_2d": [498, 380, 604, 396]},
	{"text": "218.81", "bbox": [680, 380, 723, 396], "bbox_2d": [680, 380, 723, 396]},
	{"text": "1%", "bbox": [781, 380, 796, 396], "bbox_2d": [781, 380, 796, 396]},
	{"text": "2.19", "bbox": [940, 380, 970, 396], "bbox_2d": [940, 380, 970, 396]},
	{"text": "合计", "bbox": [102, 615, 115, 632], "bbox_2d": [102, 615, 115, 632]},
	{"text": "计", "bbox": [177, 615, 190, 632], "bbox_2d": [177, 615, 190, 632]},
	{"text": "¥218.81", "bbox": [672, 613, 725, 630], "bbox_2d": [672, 613, 725, 630]},
	{"text": "¥2.19", "bbox": [930, 613, 970, 630], "bbox_2d": [930, 613, 970, 630]},
	{"text": "价税合计（大写）", "bbox": [85, 657, 195, 676], "bbox_2d": [85, 657, 195, 676]},
	{"text": "贰佰贰拾壹圆整", "bbox": [300, 652, 406, 673], "bbox_2d": [300, 652, 406, 673]},
	{"text": "(小写)¥221.00", "bbox": [689, 654, 801, 674], "bbox_2d": [689, 654, 801, 674]},
	{"text": "备注", "bbox": [33, 727, 46, 745], "bbox_2d": [33, 727, 46, 745]},
	{"text": "开票人：杨雪", "bbox": [97, 863, 184, 882], "bbox_2d": [97, 863, 184, 882]},
	{"text": "CS 扫描全能王", "bbox": [903, 943, 983, 962], "bbox_2d": [903, 943, 983, 962]},
	{"text": "3亿人都在用的扫描App", "bbox": [903, 970, 983, 980], "bbox_2d": [903, 970, 983, 980]}
]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=15.4s
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[0]: text=电子发票(普通发票), bbox=[328, 54, 640, 98]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[1]: text=发票号码：26322000000914042776, bbox=[733, 74, 955, 94]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[2]: text=开票日期：2026年02月02日, bbox=[732, 114, 908, 134]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[3]: text=江苏省税务局, bbox=[461, 146, 535, 168]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[4]: text=购买方信息, bbox=[33, 217, 46, 330]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[5]: text=名称：, bbox=[61, 224, 100, 244]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[6]: text=统一社会信用代码/纳税人识别号：, bbox=[60, 295, 257, 314]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[7]: text=销售方信息, bbox=[507, 217, 519, 330]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[8]: text=名称：阜宁仁康堂大药房有限公司, bbox=[533, 224, 747, 244]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[9]: text=统一社会信用代码/纳税人识别号：91320923MAK1XP619R, bbox=[532, 295, 946, 314]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[10]: text=项目名称, bbox=[80, 355, 140, 373]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[11]: text=规格型号, bbox=[202, 355, 262, 373]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[12]: text=单位, bbox=[321, 355, 365, 373]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[13]: text=数量, bbox=[443, 355, 487, 373]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[14]: text=单价, bbox=[561, 355, 604, 373]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[15]: text=金额, bbox=[681, 355, 724, 373]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[16]: text=税率/征收率, bbox=[745, 355, 827, 373]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[17]: text=税额, bbox=[919, 355, 963, 373]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[18]: text=*生物化学药品*其他生物, bbox=[26, 376, 189, 396]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[19]: text=化学药品, bbox=[26, 405, 86, 425]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[20]: text=1, bbox=[480, 380, 488, 396]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[21]: text=218.811881188119, bbox=[498, 380, 604, 396]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[22]: text=218.81, bbox=[680, 380, 723, 396]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[23]: text=1%, bbox=[781, 380, 796, 396]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[24]: text=2.19, bbox=[940, 380, 970, 396]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[25]: text=合计, bbox=[102, 615, 115, 632]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[26]: text=计, bbox=[177, 615, 190, 632]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[27]: text=¥218.81, bbox=[672, 613, 725, 630]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[28]: text=¥2.19, bbox=[930, 613, 970, 630]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[29]: text=价税合计（大写）, bbox=[85, 657, 195, 676]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[30]: text=贰佰贰拾壹圆整, bbox=[300, 652, 406, 673]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[31]: text=(小写)¥221.00, bbox=[689, 654, 801, 674]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[32]: text=备注, bbox=[33, 727, 46, 745]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[33]: text=开票人：杨雪, bbox=[97, 863, 184, 882]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[34]: text=CS 扫描全能王, bbox=[903, 943, 983, 962]
2026-08-05 05:24:42,626 INFO     29 [qwen-vl-text] coord item[35]: text=3亿人都在用的扫描App, bbox=[903, 970, 983, 980]
2026-08-05 05:24:42,627 INFO     29 [qwen-vl-text] page=19 — 35/35 coords, api_time=15.4s
2026-08-05 05:24:42,627 INFO     29 [qwen-vl-text] new_positions (35):
[[19, 276.176, 538.88, 32.129999999999995, 58.309999999999995], [19, 617.1859999999999, 804.11, 44.03, 55.93], [19, 616.3439999999999, 764.536, 67.83, 79.72999999999999], [19, 388.162, 450.46999999999997, 86.86999999999999, 99.96], [19, 27.785999999999998, 38.732, 129.11499999999998, 196.35], [19, 51.361999999999995, 84.2, 133.28, 145.18], [19, 50.519999999999996, 216.394, 175.525, 186.82999999999998], [19, 426.894, 436.998, 129.11499999999998, 196.35], [19, 448.786, 628.9739999999999, 133.28, 145.18], [19, 447.94399999999996, 796.5319999999999, 175.525, 186.82999999999998], [19, 67.36, 117.88, 211.225, 221.935], [19, 170.084, 220.60399999999998, 211.225, 221.935], [19, 270.282, 307.33, 211.225, 221.935], [19, 373.006, 410.054, 211.225, 221.935], [19, 472.36199999999997, 508.568, 211.225, 221.935], [19, 573.4019999999999, 609.608, 211.225, 221.935], [19, 627.29, 696.334, 211.225, 221.935], [19, 773.798, 810.846, 211.225, 221.935], [19, 21.892, 159.138, 223.72, 235.61999999999998], [19, 21.892, 72.41199999999999, 240.975, 252.875], [19, 404.15999999999997, 410.89599999999996, 226.1, 235.61999999999998], [19, 419.316, 508.568, 226.1, 235.61999999999998], [19, 572.56, 608.766, 226.1, 235.61999999999998], [19, 657.602, 670.232, 226.1, 235.61999999999998], [19, 791.48, 816.74, 226.1, 235.61999999999998], [19, 85.884, 96.83, 365.925, 376.03999999999996], [19, 149.034, 159.98, 365.925, 376.03999999999996], [19, 565.824, 610.4499999999999, 364.73499999999996, 374.84999999999997], [19, 783.06, 816.74, 364.73499999999996, 374.84999999999997], [19, 71.57, 164.19, 390.91499999999996, 402.21999999999997], [19, 252.6, 341.852, 387.94, 400.435], [19, 580.138, 674.442, 389.13, 401.03], [19, 27.785999999999998, 38.732, 432.565, 443.275], [19, 81.67399999999999, 154.928, 513.485, 524.79], [19, 760.326, 827.6859999999999, 561.0849999999999, 572.39]]
2026-08-05 05:24:42,627 INFO     29 [qwen-vl-text] ═══ DONE ═══ 35 positions, pages=1, time=18.5s
2026-08-05 05:24:42,635 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-05 05:24:42,636 INFO     29 [Trace] task=d7b98bb4 | doc=LZQ 64 哮喘 深圳二院.pdf | Extractor:Medication | outputs={"chunks": "5 items, types={'MedicationRecord': 5}", "html": "", "json": "676 items", "markdown": "", "text": "", "name": "LZQ 64 哮喘 深圳二院.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Medication\": 5}"}
2026-08-05 05:24:42,636 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-05 05:24:42,639 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:24:42,640 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m05:24:42 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:24:42,641 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:24:46,622 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:24:46,630 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-05 05:24:46,630 INFO     29 [Trace] task=d7b98bb4 | doc=LZQ 64 哮喘 深圳二院.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "676 items", "markdown": "", "text": "", "name": "LZQ 64 哮喘 深圳二院.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Medication\": 5}"}
2026-08-05 05:24:46,630 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-05 05:24:46,638 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:24:46,638 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m05:24:46 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:24:46,639 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:24:49,757 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:24:49,766 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-05 05:24:49,766 INFO     29 [Trace] task=d7b98bb4 | doc=LZQ 64 哮喘 深圳二院.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "676 items", "markdown": "", "text": "", "name": "LZQ 64 哮喘 深圳二院.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Medication\": 5}"}
2026-08-05 05:24:49,766 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-05 05:24:49,772 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:24:49,772 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-05 05:24:50,365 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 05:24:50,372 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-05 05:24:50,372 INFO     29 [Trace] task=d7b98bb4 | doc=LZQ 64 哮喘 深圳二院.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "676 items", "markdown": "", "text": "", "name": "LZQ 64 哮喘 深圳二院.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Medication\": 5}"}
2026-08-05 05:24:50,372 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-05 05:24:50,378 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 05:24:50,378 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m05:24:50 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:24:50,379 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 05:24:51,882 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 05:24:51,893 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-05 05:24:51,893 INFO     29 [Trace] task=d7b98bb4 | doc=LZQ 64 哮喘 深圳二院.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "676 items", "markdown": "", "text": "", "name": "LZQ 64 哮喘 深圳二院.pdf", "output_format": "chunks", "chunks_Clinical": "6 items, types={'OutpatientRecord': 6}", "chunks_Medication": "5 items, types={'MedicationRecord': 5}", "route_summary": "{\"chunks_Clinical\": 6, \"chunks_Medication\": 5}"}
2026-08-05 05:24:51,893 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-05 05:24:51,895 INFO     29 [ChunkMerger] Merged 11 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 6, 'Extractor:Medication': 5, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1} (filtered 6 noise chunks)
2026-08-05 05:24:51,906 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-05 05:24:51,907 INFO     29 [Trace] task=d7b98bb4 | doc=LZQ 64 哮喘 深圳二院.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "11 items, types={'OutpatientRecord': 6, 'MedicationRecord': 5}", "name": "LZQ 64 哮喘 深圳二院.pdf"}
2026-08-05 05:24:51,907 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-05 05:24:52,113 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1785907002015, 'update_date': datetime.datetime(2026, 8, 5, 5, 16, 42), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 202528, 'status': '1'}
2026-08-05 05:24:52,335 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=门诊病历
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
CS 扫描全能王
3亿人都在用的扫描App
门诊病历
科室:呼吸与危重症医学科
姓名
性别:女
联系方式
年龄:62岁
婚姻状况:其他
2024-01-10 10:27 初诊记录
5.桉柠蒎肠溶软胶囊,2023.11.03-2023.11.15,0.3g,tid,po,用于治疗肺部感
染。
7.甲泼尼龙片,2023.12.13-2023.12.15,4mg,qd,po,用于治疗支气管哮喘急
性发作。
8.布地奈德福莫特罗粉吸入剂,2022.1127开始,持续使用,
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
异常,其他无异常。.
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
CS 扫描全能王
3亿人都在用的扫描App
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
姓
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
第3页
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
呼吸道感染,2024.1127-2024.12.11,中度,与试验药物关系为可能无关
对试验药物采取的措施为延迟用药,对 AE 采取的措施为药物治疗,肺
SAE,非 SIE,不因此退出临床试验。
跟踪 CM:
1.盐酸莫西沙片,2024.12.02-2024.12.11,持续中,0.4g/片,1片/次,
qd,po,用于治疗 AE 呼吸道感染。
2.桉柠蒎肠溶胶囊,2024.12.02-2024.12.11 持续中,0.3g/粒,1粒/次,
tid,po,用于治疗 AE 呼吸道感染。(化痰)
3.氯苯那敏片,2024.12.02-2024.12.11,持续中,4mg/片,1片/次,
qn,po,用于治疗 AE 呼吸道感染。
4.泮托拉唑钠肠溶片,2024.12.02,持续中,40mg/片,1片/次,qd,po.用于治
疗病史慢性浅表胃炎。
5.复方氨酚烷胺胶囊,2024.11.27-2024.12.02,持续中,0.25g:0.1g,1粒
/次,bid,po,用于治疗 AE 呼吸道感染。
6.吸入沙丁胺醇气雾剂,2024.12.02-2024.12.02,400ug,吸入,once,用于支
气管扩张检查。
CM 跟踪:
1、布地奈德福莫特罗粉吸入剂,2022.1127 开始,持续使用,
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
患者于今日12:21-12:28完成临床试验药物的注射，药物编号为
Y6077Y4950 用药前完善必要检查后随机用药。
医师
门诊病历
※提醒:复诊时,请携带本病历记录,谢谢!※
“若有高血压糖尿病诊断,建议您到居住地附近社康中心,建立居民健康档案”
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
CS 扫描全能王
3亿人都在用的扫描App
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
CS 扫描全能王
3亿人都在用的扫描App
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
第3页
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
体格检查:T:36.8℃ P:87次/分 R:21次/分 BP:108/73mmHg 指脉氧:99%。神志清楚,精神尚可,呼吸平顺,口唇无发绀,咽部无充血,扁桃体无肿大,双侧颈静脉无怒张,双肺呼吸音粗,双肺可闻及散在干啰音,双肺未闻及湿性啰音及胸膜摩擦音。心率87次/分,律齐,各瓣膜未闻及明显病理性杂音。腹部平软,全腹部无压痛,反跳痛,肠鸣音正常。四肢运动自如,双下肢无水肿。
辅助检查:
初步诊断:
西医诊断:1.支气管哮喘(急性发作期)
处理意见:自备布地奈德福莫特罗320一次1吸,一天2次
醋酸泼尼松片(国基)(5mg*100片)10.000mg
1次/天 口服 6.00片
建议:建议患者结果回报后请及时至我科门诊复诊,若出现病情变化或病情加重无好转等,请及时至急诊科门诊复诊。
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
校验码：831306
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
3亿人都在用的扫描App
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
CS 扫描全能王
---
10:15
淘
交易成功
医药仁康堂医药专营店>
【信必可】布地奈德福莫特罗
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
扫描全能王
扫描全能王
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
化学药品
1
218.811881188119
218.81
1%
2.19
合计
¥218.81
¥2.19
价税合计（大写）
贰佰贰拾壹圆整
(小写)¥221.00
备注
开票人：杨雪
CS 扫描全能王
3亿人都在用的扫描App
2026-08-05 05:24:53,072 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-05 05:24:53,072 INFO     29 [Trace] task=d7b98bb4 | doc=LZQ 64 哮喘 深圳二院.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "11 items, types={'OutpatientRecord': 6, 'MedicationRecord': 5}", "name": "LZQ 64 哮喘 深圳二院.pdf", "embedding_token_consumption": 9296}
2026-08-05 05:24:53,072 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-05 05:24:53,216 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-05 05:24:53,216 INFO     29 [Trace] task=d7b98bb4 | doc=LZQ 64 哮喘 深圳二院.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":11,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-05 05:24:53,220 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:24:53,221 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:24:53,221 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:24:53,221 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:24:53,221 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:24:53,221 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:24:53,221 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:24:53,221 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:24:53,221 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:24:53,221 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:24:53,221 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 05:24:53,226 INFO     29 set_progress(d7b98bb4908c11f1a3da71efcdd7cc1f), progress: 0.82, progress_msg: 05:24:53 [DOC Engine]:
Start to index...
2026-08-05 05:24:53,249 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.018s]
2026-08-05 05:24:53,254 INFO     29 set_progress(d7b98bb4908c11f1a3da71efcdd7cc1f), progress: 0.8090909090909091, progress_msg: 
2026-08-05 05:24:53,276 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.014s]
2026-08-05 05:24:53,291 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.009s]
2026-08-05 05:24:53,299 INFO     29 set_progress(d7b98bb4908c11f1a3da71efcdd7cc1f), progress: 1.0, progress_msg: 05:24:53 Indexing done (0.07s). Task done (448.78s)
2026-08-05 05:24:53,307 INFO     29 [Done], chunks(11), token(9296), elapsed:448.78
2026-08-05 05:24:53,502 INFO     29 handle_task done for task {"id": "d7b98bb4908c11f1a3da71efcdd7cc1f", "doc_id": "d7626528908c11f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "type": "pdf", "location": "LZQ 64 \u54ee\u5598 \u6df1\u5733\u4e8c\u9662.pdf", "size": 51479738, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1785907001430, "task_type": "dataflow", "root_trace_id": "ea6d5499d1eb4a3cabaa8fb5a06c80f8", "root_traceparent": "00-ea6d5499d1eb4a3cabaa8fb5a06c80f8-0f37f835e898f31c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
